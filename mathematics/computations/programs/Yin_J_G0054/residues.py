"""Declared complete mod3/mod9 checks of four unbounded column systems."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as s
from equations import equations, x

BASE=(_J_PROGRAM / 'residues.py').parent
def main():
    records=[];total=0
    for i in (2,3):
        for case in equations(i)['cases']:
            N=s.sympify(case['norm_equation']); A=s.sympify(case['coefficient_equation'])
            variables=sorted(N.free_symbols|A.free_symbols,key=str)
            assert len(variables)==4
            f=s.lambdify(variables,(N,A),modules='math')
            for modulus in (3,9):
                survivors=[]
                for v in product(range(modulus),repeat=4):
                    total+=1
                    n,a=f(*v)
                    assert isinstance(n,int) and isinstance(a,int)
                    if n%modulus==0 and a%modulus==0:survivors.append(list(v))
                records.append({'column':i,'pfaffian':case['pfaffian'],'modulus':modulus,
                                'variables':list(map(str,variables)),'tuples':modulus**4,
                                'survivor_count':len(survivors),'survivors':survivors})
    assert total==26568
    result={'passed':True,'declared_total_tuple_cap':26568,'total_tuples':total,'systems':records}
    ((_J_OUTPUT / 'residues.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='systems'}))
    for row in records:print({k:v for k,v in row.items() if k!='survivors'})
if __name__=='__main__':main()
