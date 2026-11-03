"""Only the original mod2 witness: exact single-step compatibility modulo4."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json,time
import sympy as sp
from lift import equations,rref,verify,reduce,array

def run():
    start=time.perf_counter()
    old=json.loads((_J_OUTPUT / 'lift_result.json').read_text(encoding='utf8'))
    row=next(r for r in old['tests'] if r['prime']==2);a=row['jacobian'];q=sp.Matrix(row['initial']['basis'])
    err=equations(q);assert all(v%2==0 for v in err);rhs=[-(v//2)%2 for v in err]
    at=[list(v) for v in zip(*a)];rr,piv=rref(at,2);free=[j for j in range(21) if j not in piv]
    assert len(free)==1
    left=[0]*21;left[free[0]]=1
    for i,c in enumerate(piv):left[c]=sum(rr[i][j]*left[j] for j in free)%2
    assert all(sum(left[i]*a[i][j] for i in range(21))%2==0 for j in range(36))
    obstruction=sum(x*y for x,y in zip(left,rhs))%2
    aug,apiv=rref([r+[v] for r,v in zip(a,rhs)],2)
    out=dict(scope=dict(prime=2,start_exponent=1,target_exponent=2,starting_basis='unchanged J60 witness normalized as in lift_result.json'),
             initial_basis=array(q),equation_errors=err,right_hand_side_mod2=rhs,
             derivative_rank=20,left_kernel_vector=left,left_kernel_pairing=obstruction,
             augmented_rank=len(apiv),compatible=obstruction==0)
    if obstruction:
        assert len(apiv)==21 and apiv[-1]==36
        out['conclusion']='No lift of this residue-class basis to SL6(Z/4) with positive upper-unitriangular congruence.'
    else:
        assert len(apiv)==20 and 36 not in apiv
        sol=[0]*36
        for i,c in enumerate(apiv):sol[c]=aug[i][-1]
        assert all(sum(x*y for x,y in zip(r,sol))%2==v for r,v in zip(a,rhs))
        x=sp.Matrix(6,6,sol);nq=reduce(q*(sp.eye(6)+2*x),4)
        out.update(correction=array(x),lift=verify(nq,4),conclusion='One compatible full basis modulo4; no higher power or integer claim.')
    assert time.perf_counter()-start<120
    return out
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'two_adic_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in out.items() if k in ['derivative_rank','left_kernel_pairing','augmented_rank','compatible','conclusion']}))
