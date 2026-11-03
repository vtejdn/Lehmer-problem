"""Directed change from a 7+1 mod-two tree to a possible 3+5 partition.

Only the two central columns of one explicit path basis and the114 already
enumerated short roots are considered: exactly228 pairs, not a larger scan.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp
from search import first_coefficients, upper, energy

BASE=(_J_PROGRAM / 'path_replacements.py').parent
source=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
checked=json.loads(((_J_OUTPUT / 'verification.json')).read_text(encoding='utf-8'))
G0=sp.Matrix(source['seed_gram']); Q0=sp.eye(6)
for i in range(1,6):Q0[i-1,i]=-1
assert Q0.det()==1 and list((Q0.T*G0*Q0).diagonal())==[2]*6
inverse=Q0.inv(); t=sp.symbols('t')
rows=[]; witnesses=[]; tested=0
for root in checked['all_short_roots']:
    r=sp.Matrix(root['coordinates']); c=inverse*r
    for i in (2,3):
        tested+=1
        if abs(c[i])!=1:continue
        Q=Q0.copy();Q[:,i]=r
        assert Q.det() in (-1,1)
        G=Q.T*G0*Q
        assert list(G.diagonal())==[2]*6
        g=[[int(G[a,b]) for b in range(6)] for a in range(6)]
        coeffs=first_coefficients(g)
        row={'column':i,'root':list(map(int,r)),'coefficient_in_path_basis':list(map(int,c)),
             'first_coefficients':list(coeffs),'energy':energy(g)}
        rows.append(row)
        if coeffs!=(-2,1):continue
        V=sp.Matrix(upper(g));Vm=sp.eye(6)
        for a in range(6):
            for b in range(a+1,6):Vm[a,b]=-abs(V[a,b])
        p=sp.Poly((t*V+V.T).det(),t);pm=sp.Poly((t*Vm+Vm.T).det(),t)
        assert p==sp.Poly((t*t-t+1)*(t**4-t**3-t*t-t+1),t)
        witnesses.append(row|{'basis':[[int(Q[a,b]) for b in range(6)] for a in range(6)],
                             'gram':g,'matrix':upper(g),
                             'polynomial':list(map(int,p.all_coeffs())),
                             'absolute_polynomial':list(map(int,pm.all_coeffs())),
                             'cover_polynomial':list(map(int,(p*pm).all_coeffs()))})
assert tested==228
matching_mod2=sum(row['first_coefficients'][0]%2==0 and row['first_coefficients'][1]%2==1 for row in rows)
assert matching_mod2==64
out={'passed':True,'declared_pair_cap':228,'pairs_tested':tested,
     'path_basis':[[int(Q0[a,b]) for b in range(6)] for a in range(6)],
     'admissible_replacements':len(rows),'target_count':len(witnesses),
     'target_mod2_count':matching_mod2,
     'all_admissible_results':rows,'target_witnesses':witnesses}
((_J_OUTPUT / 'path_replacements.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('passed','pairs_tested','admissible_replacements','target_count','target_witnesses')}))
