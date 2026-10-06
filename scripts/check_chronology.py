"""Synthetic date fixtures: admission is an evaluation mask, never a trade filter."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fixtures.chronology import (
    decision_admission, embargo_dates, guarded_confirmation_read, holding_path,
)

checks = []

def check(name, condition):
    checks.append(name)
    if not condition:
        raise AssertionError(name)

grid = [f"S{i:02d}" for i in range(20)]
for horizon in range(2, 11):
    check(f"horizon_{horizon}_next_session", holding_path(grid, "S00", horizon, "S00", "S19") == grid[1:horizon+1])
for invalid in (True, False, 1, 11, 2.0, "2", None):
    check(f"invalid_horizon_{invalid!r}", holding_path(grid, "S00", invalid, "S00", "S19") is None)
check("missing_decision", holding_path(grid, "absent", 2, "S00", "S19") is None)
check("terminal_path", holding_path(grid, "S18", 2, "S00", "S19") is None)
check("cross_boundary", holding_path(grid, "S08", 2, "S00", "S09") is None)
check("decision_outside", holding_path(grid, "S00", 2, "S01", "S19") is None)

# Explicit synthetic session sequence, no calendar-provider or price dependency.
sessions = ["2026-01-" + d for d in (
    "02", "05", "06", "07", "08", "09", "12", "13", "14", "15",
    "16", "20", "21", "22", "23", "26", "27", "28", "29", "30",
)] + ["2026-02-" + d for d in ("02", "03", "04", "05", "06")]
inputs = {("TEST", date): True for date in sessions}
check("explicit_ten_date_embargo", embargo_dates(sessions) == sessions[:10])
rows = [decision_admission("TEST", date, sessions, inputs) for date in sessions]
# Independent expected mask: first ten embargoed, last ten incomplete.
check("all_mask_rows", [row["evaluation_admitted"] for row in rows] == [False]*10 + [True]*5 + [False]*10)
check("first_entry", rows[10]["entry_session"] == "2026-01-20")
check("tenth_exit", rows[10]["maximum_exit_session"] == "2026-02-02")
check("embargo_reason", rows[9]["reasons"] == "validation_embargo")
missing_current = dict(inputs)
missing_current[("TEST", sessions[10])] = False
check("missing_current_reason", "input_not_admitted" in decision_admission("TEST", sessions[10], sessions, missing_current)["reasons"])
missing_future = dict(inputs)
missing_future[("TEST", sessions[11])] = False
check("future_missing_censor", decision_admission("TEST", sessions[10], sessions, missing_future)["reasons"] == "future_input_unavailable")
check("original_observations_retained", len(rows) == len(sessions) and len(missing_future) == len(inputs))
check("outside_window", "outside_study_windows" in decision_admission("TEST", "2025-09-10", sessions, {})["reasons"])

calls = []
for contract in ({}, {"status": "qualified", "access_enabled": True, "start": "future", "end": "future"}):
    try:
        guarded_confirmation_read(contract, lambda: calls.append("called"))
    except PermissionError:
        check("confirmation_denied_" + str(len(contract)), True)
    else:
        raise AssertionError("confirmation guard allowed access")
check("confirmation_loader_never_called", calls == [])
print(json.dumps({"checks": len(checks), "passed": True, "scope": "synthetic date controls only"}))
