"""Declared13828 residues at the final parity-compatible column4."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as s
from equations import equations
BASE=(_J_PROGRAM / 'last_column_residues.py').parent

def main():
    records=[];total=0
    for case in equations(4)['cases']:
        N=s.sympify(case['norm_equation']);A=s.sympify(case['coefficient_equation'])
        variables=sorted(N.free_symbols|A.free_symbols,key=str)
        assert len(variables)==4
        f=s.lambdify(variables,(N,A),'math')
        for m in (2,4,3,9):
            survivors=[]
            for point in product(range(m),repeat=4):
                total+=1;n,a=f(*point)
                if n%m==0 and a%m==0:survivors.append(list(point))
            records.append({'column':4,'pfaffian':case['pfaffian'],'modulus':m,
                            'variables':list(map(str,variables)),
                            'tuples':m**4,'survivor_count':len(survivors),'survivors':survivors})
    assert total==13828
    result={'passed':True,'declared_residue_cap':13828,'total_tuples':total,'systems':records}
    ((_J_OUTPUT / 'last_column_residues.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for r in records:print({k:v for k,v in r.items() if k!='survivors'})
if __name__=='__main__':main()
