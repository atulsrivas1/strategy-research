"""Versioned offline execution receipts. Not a sandbox for untrusted Python."""
import hashlib
import ast
import inspect
import json
import platform
import marshal
import sys
import types
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def _codes(code):
    yield code
    for value in code.co_consts:
        if isinstance(value, types.CodeType):
            yield from _codes(value)


def source_manifest(engine, root):
    """Discover referenced local modules/functions and reject stale loaded code.

    Dynamic imports, callable objects and runtime-generated functions are outside
    this contract. The evaluator must declare any such additional dependencies.
    """
    root = Path(root).resolve()
    pending, seen, result = [engine], set(), {}
    while pending:
        module = pending.pop()
        if module in seen:
            continue
        seen.add(module)
        path = Path(module.__file__).resolve()
        if not path.is_relative_to(root) or path.suffix != '.py':
            raise ValueError('engine/dependency must be local Python source')
        raw = path.read_bytes()
        parsed = ast.parse(raw)
        for node in ast.walk(parsed):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and any(isinstance(child, (ast.Import, ast.ImportFrom)) for child in ast.walk(node)):
                raise ValueError('function-local imports require a different execution contract')
        compiled = tuple(_codes(compile(raw, str(path), 'exec')))
        for value in vars(module).values():
            if inspect.isclass(value) and value.__module__ == module.__name__:
                raise ValueError('class-based engines require a different execution contract')
            dependency = value if inspect.ismodule(value) else inspect.getmodule(value) if inspect.isfunction(value) else None
            if dependency is not None and getattr(dependency, '__file__', None):
                dep_path = Path(dependency.__file__).resolve()
                if dep_path.is_relative_to(root) and dep_path.suffix == '.py':
                    pending.append(dependency)
            if inspect.isfunction(value) and value.__module__ == module.__name__:
                if not any(value.__code__ == code for code in compiled):
                    raise ValueError('loaded function differs from source')
        result[path.relative_to(root).as_posix()] = {
            'sha256_exact': digest(raw),
            'sha256_lf': digest(raw.replace(b'\r\n', b'\n')),
        }
    return result


def verify_sources(manifest, engine, root):
    actual = source_manifest(engine, root)
    if actual != manifest:
        raise ValueError('source coverage/bytes changed')


def _callback(function):
    if not inspect.isfunction(function):
        raise ValueError('explicit source-backed callback required')
    path = Path(function.__code__.co_filename).resolve()
    raw = path.read_bytes()
    if not any(function.__code__ == code for code in _codes(compile(raw, str(path), 'exec'))):
        raise ValueError('callback differs from source')
    return {'sha256_exact': digest(raw), 'code_sha256': digest(marshal.dumps(function.__code__))}


def _execution_sources(engine, root, callbacks):
    manifest = source_manifest(engine, root)
    for callback in callbacks:
        for value in callback.__globals__.values():
            dependency = value if inspect.ismodule(value) else inspect.getmodule(value) if inspect.isfunction(value) else None
            if dependency is not None and getattr(dependency, '__file__', None):
                path = Path(dependency.__file__).resolve()
                if path.is_relative_to(Path(root).resolve()) and path.suffix == '.py':
                    manifest.update(source_manifest(dependency, root))
    return manifest


def execute(attempt, engine, root, protocol, inputs, allowed_inputs, loader, evaluator):
    """Single-attempt guard; loader receives frozen bytes, never source paths.

    allowed_inputs is the preregistered explicit development allowlist. Callers
    must enforce their real holdout map; no path-name heuristic grants access.
    protocol includes declared source hashes for any dynamic dependencies.
    Failed attempts are retained and cannot be reused.
    """
    attempt = Path(attempt)
    attempt.mkdir(parents=True, exist_ok=False)
    receipt = {'state': 'preparing', 'scope': 'offline explicit inputs'}
    def save():
        temp = attempt / 'receipt.tmp'
        temp.write_text(json.dumps(receipt, sort_keys=True, indent=2), encoding='utf-8')
        temp.replace(attempt / 'receipt.json')
    try:
        paths = {name: Path(path).resolve() for name, path in inputs.items()}
        allowed = {Path(path).resolve() for path in allowed_inputs}
        if not paths or not set(paths.values()).issubset(allowed):
            raise ValueError('input outside frozen development allowlist')
        manifest = _execution_sources(engine, root, (loader, evaluator))
        if not manifest:
            raise ValueError('missing engine')
        spec = json.dumps(protocol, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
        callbacks = {'loader': _callback(loader), 'evaluator': _callback(evaluator)}
        guard = digest(Path(__file__).read_bytes())
        snapshots = {name: path.read_bytes() for name, path in paths.items()}
        receipt.update(state='frozen', source=manifest, protocol_sha256=digest(spec),
                       callbacks=callbacks, guard_sha256=guard,
                       input_sha256={name: digest(raw) for name, raw in snapshots.items()},
                       environment={'python': sys.version, 'platform': platform.platform()},
                       engine=Path(engine.__file__).resolve().relative_to(Path(root).resolve()).as_posix())
        save()
        (attempt / 'protocol.json').write_bytes(spec)
        (attempt / 'inputs').mkdir()
        for raw in snapshots.values():
            (attempt / 'inputs' / digest(raw)).write_bytes(raw)
        (attempt / 'sources').mkdir()
        for name, info in manifest.items():
            (attempt / 'sources' / info['sha256_exact']).write_bytes((Path(root)/name).read_bytes())
        def verify():
            if manifest != _execution_sources(engine, root, (loader, evaluator)):
                raise ValueError('execution dependency coverage/bytes changed')
            if callbacks != {'loader': _callback(loader), 'evaluator': _callback(evaluator)} or guard != digest(Path(__file__).read_bytes()):
                raise ValueError('execution callbacks/guard changed')
        verify()
        prepared = loader(dict(snapshots))
        verify()
        result = evaluator(engine, prepared)
        verify()
        payload = json.dumps(result, sort_keys=True, allow_nan=False).encode()
        (attempt / 'result.json').write_bytes(payload)
        receipt.update(state='complete', result_sha256=digest(payload))
        save()
        return result
    except BaseException as error:
        receipt.update(state='failed', error_type=type(error).__name__)
        save()
        raise
