"""Separate complete short-root column test, capped at 114*6=684 pairs.

This changes the root class; it is not continuation of the reflection annealer.
No fresh random proposal or expansion of the original 25000 cap is performed.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp
from search import first_coefficients, upper, energy

BASE=(_J_PROGRAM / 'short_replacements.py').parent
source=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
verification=json.loads(((_J_OUTPUT / 'verification.json')).read_text(encoding='utf-8'))
G0=sp.Matrix(source['seed_gram'])
roots=verification['all_short_roots']
assert len(roots)==114
target=(-2,1)
records=[]; found=[]; tested=0
for record in roots:
    r=record['coordinates']
    for i in range(6):
        tested+=1
        if abs(r[i])!=1:
            continue
        Q=sp.eye(6);Q[:,i]=sp.Matrix(r)
        G=Q.T*G0*Q
        assert Q.det() in (-1,1) and list(G.diagonal())==[2]*6
        g=[[int(G[a,b]) for b in range(6)] for a in range(6)]
        coeffs=first_coefficients(g)
        result={'column':i,'root':r,'mod2_weight':record['mod2_weight'],
                'first_coefficients':list(coeffs),'energy':energy(g)}
        records.append(result)
        if coeffs==target:
            t=sp.symbols('t');V=sp.Matrix(upper(g))
            p=sp.Poly((t*V+V.T).det(),t)
            assert p==sp.Poly((t*t-t+1)*(t**4-t**3-t*t-t+1),t)
            Vm=sp.eye(6)
            for a in range(6):
                for b in range(a+1,6):Vm[a,b]=-abs(V[a,b])
            pm=sp.Poly((t*Vm+Vm.T).det(),t)
            found.append(result|{'basis':[[int(Q[a,b]) for b in range(6)] for a in range(6)],
                                  'matrix':upper(g),'polynomial':[int(v) for v in p.all_coeffs()],
                                  'absolute_polynomial':[int(v) for v in pm.all_coeffs()],
                                  'cover_polynomial':[int(v) for v in (p*pm).all_coeffs()]})
assert tested==684
matching_mod2=sum(row['first_coefficients'][0]%2==0 and row['first_coefficients'][1]%2==1 for row in records)
assert matching_mod2==0
out={'passed':True,'declared_pair_cap':684,'all_pairs_tested':tested,
     'unimodular_replacements':len(records),'target_count':len(found),
     'target_mod2_count':matching_mod2,
     'target_witnesses':found,'all_admissible_results':records}
((_J_OUTPUT / 'short_replacements.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('passed','all_pairs_tested','unimodular_replacements','target_count','target_witnesses')}))
