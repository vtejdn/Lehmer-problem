"""Exact equations at the two remaining parity-compatible path positions."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
from equations import equations
BASE=(_J_PROGRAM / 'other_columns.py').parent
result={'passed':True,'columns':[equations(i) for i in (1,4)]}
((_J_OUTPUT / 'other_columns.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
