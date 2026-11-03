"""Exact bounded checks backing the family proof; no numerical root scan.

Run: .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0002/check_family.py
All-N positivity/cyclotomic completeness require the companion hand proof.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s
from fractions import Fraction

t=s.symbols('t')
conditions={2:(2,0),8:(8,7),12:(12,10),18:(18,14),30:(30,21)}

def orders(N):
    return [d for d,(mod,r) in conditions.items() if N%mod==r]

def net(coeffs,limit):
    trace=[0]*(limit+1)
    b=[0]*(limit+1)
    for m in range(1,limit+1):
        am=coeffs[m] if m<len(coeffs) else 0
        trace[m]=-m*am-sum(coeffs[i]*trace[m-i]
                            for i in range(1,min(m,len(coeffs))))
        T=sum(int(s.mobius(m//d))*trace[d] for d in s.divisors(m))
        assert T%m==0
        b[m]=T//m
    return b

baseline=net([1,0,-1,-1],30)
canonical_rows=[]
for N in range(4,391):
    q=[0]*(N+4)
    for i,c in [(0,1),(2,-1),(3,-1),(N,-1),(N+1,-1),(N+3,1)]:
        q[i]+=c
    bq=net(q,30)
    bc=[0]*31
    for d in orders(N):
        for j in s.divisors(d):
            bc[j]+=int(s.mobius(d//j))
    bp=[x-y for x,y in zip(bq,bc)]
    neg={str(i):v for i,v in enumerate(bp) if v<0}
    expected={'2':-1} if N%12==10 else {}
    assert neg==expected, (N,neg)
    if neg:
        assert orders(N)==[2,12]
        assert bp[1]==1
        repaired=bp[:]
        repaired[1]-=1
        repaired[2]+=1
        assert min(repaired)>=0
    canonical_rows.append({'N':N,'cyclotomic_orders':orders(N),'negative_net_counts':neg})

matrix_rows=[]
for N in list(range(2,17))+[22,34]:
    A=s.zeros(N+3)
    edges=[(0,1),(1,2),(2,0),(2,1)]
    edges += [(3+j,3+(j+1)%N) for j in range(N)]
    edges += [(3+N-2,2),(1,3)]
    for src,dst in edges:
        A[dst,src]+=1
    assert max(A)==1 and min(A)==0
    assert sum(A)==N+6
    expected=t**(N+3)-t**(N+1)-t**N+1-t**2-t**3
    actual=A.charpoly(t).as_expr()
    assert s.expand(actual-expected)==0
    assert abs(A.det())==1
    matrix_rows.append({'N':N,'dimension':N+3,'edges':N+6,'excess':3,
                        'determinant':int(A.det()),'characteristic_polynomial_matches':True})

classification=json.loads((_J_OUTPUT.parent / 'Yin_J_G0001/result.json').read_text(encoding='utf-8'))
lower_trace=Fraction(33,25)+Fraction(25,33)
upper_trace=Fraction(4,3)+Fraction(3,4)
for row in classification['exact_groups_and_isolations']:
    assert (Fraction(row['trace_upper'])<lower_trace or
            Fraction(row['trace_lower'])>upper_trace)
assert (s.Rational(33,25)**3-s.Rational(33,25)-1)<0

result={
    'scope':'Finite exact checks; full-family proof is separate',
    'baseline_net_counts_1_to_30':baseline[1:],
    'canonical_checks_N_range':[4,390],
    'period_after_N_greater_than_30':360,
    'all_canonical_repair_checks_passed':True,
    'degree_one_Phi2_repair_when_needed_passed':True,
    'all_13_Salem_groups_excluded_from_interval':["33/25","4/3"],
    'maximum_degree_cyclotomic_factor':max(sum(int(s.totient(d)) for d in orders(N))
                                         for N in range(360)),
    'canonical_rows':canonical_rows,
    'matrix_checks':matrix_rows,
}
Path(__file__).with_name('family_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['canonical_rows','matrix_checks']},indent=2))
print('Matrix parameters:',[r['N'] for r in matrix_rows])
