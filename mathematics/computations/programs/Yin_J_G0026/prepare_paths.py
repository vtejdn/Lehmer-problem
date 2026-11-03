"""Nonbinding floating search-region data; exact path proof uses integers only."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import estimate as e

beta,M=e.embeddings()
b=float(sum(beta)/2)
out={'embedding':[[float(sum(v)/2) for v in row] for row in M],
     'expanding_bound':1/(b-1),'contracting_bound':b/(b-1),
     'radius':8,'node_cap':6000000,'scope':'floating discovery pruning only'}
((_J_OUTPUT / 'path-parameters.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='embedding'},indent=2))
