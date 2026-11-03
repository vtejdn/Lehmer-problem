"""Complete modulus-four test of three self-adjoint-unit changed forms.

The binary primitives are explicitly reused from fixed J63; this author run
is not an independent implementation of that routine. Every actual Gram,
error, full finite set and whole scalar cost is recomputed here.
"""
import importlib.util
import json
import time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as sp

HERE=(_J_PROGRAM / 'changed.py').parent
source=(_J_ROOT / 'mathematics/computations/programs/Yin_J_G0063/classify.py')
spec=importlib.util.spec_from_file_location('j63_binary',source)
binary=importlib.util.module_from_spec(spec)
spec.loader.exec_module(binary)

def array(m): return [[int(x) for x in row] for row in m.tolist()]
def coeff(p,t): return [int(x) for x in sp.Poly(p,t).all_coeffs()][::-1]

def run():
    start=time.monotonic()
    def guard():
        if time.monotonic()-start>120: raise TimeoutError('Declared total 120-second cap reached')
    v=sp.Matrix(binary.V);c=-v.inv()*v.T;r=c**2+c**-2
    assert all(x.q==1 for x in c) and all(x.q==1 for x in r)
    assert v.det()==1 and c.det()==1 and r.det()==1
    assert c.T*v*c==v and r.T*v==v*r and r*c==c*r
    ri=r.inv(); assert all(x.q==1 for x in ri)
    t=sp.Symbol('t');f=t**6-2*t**5+t**4-t**3+t*t-2*t+1
    assert c.charpoly(t).as_expr()==f
    original=[('V',v),('-V',-v),('VR',v*r),('-VR',-v*r)]
    result={'scope':{'new_forms':['-V','VR','-VR'],'all_upper_forms':32768,'image_vectors':64,
                     'modulus':4,'binary_primitives_reused':'J63/classify.py',
                     'old_V_classification_rerun':False},
            'V':array(v),'C':array(c),'R':array(r),'R_inverse':array(ri),
            'complete':False,'classifications':[],'costs':[]}
    c0=binary.rows(array(c));assert binary.annihilates(c0)
    cyclic={w:binary.krylov(c0,w) for w in range(64)}
    cyclic={w:k for w,k in cyclic.items() if binary.inv(k) is not None}
    assert cyclic
    result['cyclic_C_rows']=c0;result['cyclic_C_vectors']=list(cyclic)
    models=[]
    for name,b in original[1:]:
        bb=array(b)
        pair=[[sum(((a>>i)&1)*bb[i][j]*((z>>j)&1) for i in range(6) for j in range(6))
               for z in range(64)] for a in range(64)]
        model={'name':name,'matrix':bb,'forms':[],'counts':{'congruent_forms':0,'binary_bases':0,
               'liftable_bases':0,'nonliftable_bases':0}}
        models.append((model,pair,set()))
        result['classifications'].append(model)
    counts={'processed_upper_forms':0,'nonsingular_symmetric_forms':0,'annihilator_forms':0,'cyclic_forms':0}
    result['common_counts']=counts
    try:
        for mask in range(32768):
            if mask%32==0:guard()
            u=binary.IDENT[:]
            for k,(i,j) in enumerate(binary.UP):u[i] |= ((mask>>k)&1)<<j
            counts['processed_upper_forms']+=1
            ut=binary.transpose(u)
            if binary.inv([x^y for x,y in zip(u,ut)]) is None:continue
            counts['nonsingular_symmetric_forms']+=1
            cu=binary.mm(binary.inv(u),ut)
            if not binary.annihilates(cu):continue
            counts['annihilator_forms']+=1
            vu=None
            for vv in range(64):
                ki=binary.inv(binary.krylov(cu,vv))
                if ki is not None:vu=vv;break
            if vu is None:continue
            counts['cyclic_forms']+=1
            candidates=[]
            for w,k in cyclic.items():
                q=binary.mm(k,ki)
                assert binary.inv(q) is not None
                candidates.append((w,q,binary.transpose(q)))
            rank,rr,ops,pivots=binary.reduction(u)
            for model,pair,seen in models:
                fr={'upper_mask':mask,'upper_rows':u,'cyclic_vector':vu,'linear_rank':rank,
                    'left_kernel_basis':ops[rank:],'bases':[]}
                for w,q,cols in candidates:
                    b=[[pair[x][y] for y in cols] for x in cols]
                    if binary.rows(b)!=u:continue
                    assert tuple(q) not in seen;seen.add(tuple(q))
                    e=0
                    for k,(i,j) in enumerate(binary.SELECT):
                        numerator=b[i][j]-int(i==j);assert numerator%2==0
                        e |= ((numerator//2)&1)<<k
                    rec={'Q_rows':q,'image_vector':w,'error_bits':e}
                    z=next((z for z in ops[rank:] if (z&e).bit_count()%2),None)
                    model['counts']['binary_bases']+=1
                    if z is not None:
                        rec['inconsistency_witness']=z;model['counts']['nonliftable_bases']+=1
                    else:
                        x=sum(((ops[i]&e).bit_count()%2)<<pivots[i] for i in range(rank))
                        xx=[(x>>(6*i))&63 for i in range(6)]
                        h=[x^y for x,y in zip(binary.mm(binary.transpose(xx),u),binary.mm(u,xx))]
                        gram=[[(b[i][j]+2*((h[i]>>j)&1))%4 for j in range(6)] for i in range(6)]
                        assert all(gram[i][j]==int(i==j) for i,j in binary.SELECT)
                        rec.update({'correction_bits':x,'gram_mod4':gram});model['counts']['liftable_bases']+=1
                    fr['bases'].append(rec)
                if fr['bases']:
                    model['counts']['congruent_forms']+=1;model['forms'].append(fr)
        for name,b in original:
            guard(); assert b.det()==1 and -b.inv()*b.T==c
            pb=sp.expand((t*b+b.T).det(method='domain-ge'));assert pb==f
            a=-b.applyfunc(abs);pa=sp.expand((t*a+a.T).det(method='domain-ge'))
            w=sp.zeros(12)
            for i in range(6):
                for j in range(6):
                    x=int(b[i,j])
                    for sheet in range(2):w[2*i+sheet,2*j+(sheet if x<=0 else 1-sheet)]=-abs(x)
            pw=sp.expand(pb*pa)
            for val in range(-6,7):
                guard();assert (val*w+w.T).det(method='domain-ge')==pw.subs(t,val)
            result['costs'].append({'name':name,'matrix':array(b),'absolute_matrix':array(a),'literal_cover':array(w),
              'original_polynomial':coeff(pb,t),'absolute_polynomial':coeff(pa,t),'cover_polynomial':coeff(pw,t),
              'absolute_factorization':str(sp.factor(pa)),'absolute_zero':pa==0,
              'ranks':[int(b.rank()),int(a.rank()),int(w.rank())],
              'degrees':[int(sp.degree(pb,t)),None if pa==0 else int(sp.degree(pa,t)),None if pw==0 else int(sp.degree(pw,t))],
              'heights':[max(abs(int(x)) for x in m) for m in [b,a,w]],
              'whole_squared_entry_sums':[sum(int(x)**2 for x in m) for m in [b,a,w]],
              'absolute_coefficient_l1':sum(abs(x) for x in coeff(pa,t)),
              'proper_upper_unitriangular':all(b[i,j]==int(i==j) for i in range(6) for j in range(i+1)),
              'direct_cover_evaluations':13})
        guard();result['complete']=True
    except TimeoutError as exc:result['cap_failure']=str(exc)
    pass
    return result

if __name__=='__main__':
    data=run();((_J_OUTPUT / 'changed_result.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'complete': data['complete'], 'common_counts': data['common_counts'], 'classifications': [{k: v for k, v in a.items() if k not in ['forms', 'matrix']} for a in data['classifications']], 'costs': [{k: v for k, v in a.items() if k in ['name', 'absolute_polynomial', 'heights', 'whole_squared_entry_sums', 'ranks']} for a in data['costs']]}, indent=2))
