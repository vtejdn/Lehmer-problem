"""Exact elimination of all integer free parameters in 27 declared kernel fibers."""
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HOME=(_J_PROGRAM / 'fibers.py').parent
saved=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
a,b,c,d,e,f=sp.symbols('a b c d e f')
h,k,t=sp.symbols('h k t')
expr=[sp.sympify(saved['coefficient_equations'][z]) for z in ['t6','t5','t4']]
B=sp.Matrix(saved['B'])
records=[]
witnesses=[]
for u,v,w in product([-1,0,1],repeat=3):
    R=u*u+v*v+w*w+u-v+w-1
    sub={a:h-u,b:k+h,c:k,d:k+R+v,e:k+R-h,f:R-h-w}
    p=sp.Poly(sp.expand(expr[0].subs(sub)),h,k)
    q=sp.Poly(sp.expand((expr[1]+1).subs(sub)),h,k)
    resultant=sp.Poly(sp.resultant(p.as_expr(),q.as_expr(),h),k)
    row={'kernel':[u,v,w],'A':str(p.as_expr()),'D_plus_one':str(q.as_expr()),
         'resultant':str(sp.factor(resultant.as_expr())), 'integer_k':[],
         'candidate_fibers':[],'unresolved':False}
    if resultant.is_zero:
        row['unresolved']=True
        row['reason']='identically zero elimination resultant'
        records.append(row)
        continue
    roots=sp.polys.polytools.ground_roots(resultant)
    ints=sorted(int(x) for x in roots if x.q==1)
    row['integer_k']=ints
    for kval in ints:
        ph=sp.Poly(p.as_expr().subs(k,kval),h)
        qh=sp.Poly(q.as_expr().subs(k,kval),h)
        g=sp.gcd(ph,qh)
        item={'k':kval,'A_h':str(ph.as_expr()),'D_plus_one_h':str(qh.as_expr()),
              'gcd':str(sp.factor(g.as_expr())),'integer_h':[]}
        if g.is_zero:
            row['unresolved']=True
            item['reason']='both equations vanish identically; all integers h solve'
        else:
            hroots=sp.polys.polytools.ground_roots(g)
            hs=sorted(int(x) for x in hroots if x.q==1)
            item['integer_h']=hs
            for hval in hs:
                vals=[int(sub[z].subs({h:hval,k:kval})) if hasattr(sub[z],'subs') else int(sub[z]) for z in [a,b,c,d,e,f]]
                assert all(sp.expand(g0.subs(dict(zip([a,b,c,d,e,f],vals))))==z for g0,z in zip(expr,[0,-1,-1]))
                C=sp.Matrix([[1,vals[0],vals[1],vals[2]],[0,1,vals[3],vals[4]],[0,0,1,vals[5]],[0,0,0,1]])
                V=sp.eye(7);V[:3,3:]=-B;V[3:,3:]=C
                det=sp.Poly((t*V+V.T).det(method='domain-ge'),t)
                assert det==sp.Poly((t+1)*(t**6-t**5-t**3-t+1),t)
                witnesses.append({'kernel':[u,v,w],'h':hval,'k':kval,'params':vals,'V':V.tolist(),'polynomial':str(det.as_expr())})
        row['candidate_fibers'].append(item)
    records.append(row)
out={'scope':'27 kernel triples; all integer h,k checked when unresolved is false',
     'records':records,'all_resolved':all(not row['unresolved'] for row in records),
     'witnesses':witnesses}
((_J_OUTPUT / 'fiber_result.json')).write_text(json.dumps(out,indent=2,default=int)+'\n',encoding='utf-8')
print(json.dumps({'fibers':len(records),'unresolved':sum(row['unresolved'] for row in records),
                  'integer_k_total':sum(len(row['integer_k']) for row in records),'witnesses':witnesses},indent=2,default=int))
