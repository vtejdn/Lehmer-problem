"""Fixed endpoint-integral and density-cap duals for the first N=7 triple.

One 1000-node LP, a 15-second limit, and rational rounding at denominator
10**6 per selected proposal command. Numerical optimization proposes a polynomial; verification
integrates its positive-part penalty over the entire continuous interval.
"""

import argparse
from fractions import Fraction as F
import json
from math import comb
from pathlib import Path

from flint import arb, fmpq, ctx
from negative_one_higher import trace_differences

TRIPLE = (10, 18, 27)
ATOM = F(-15, 16)
CUT_LEFT = F(-1609663, 10**6)
CUT_RIGHT = F(-1609662, 10**6)
NODES = 1000
DENOMINATOR = 10**6


def ball(value):
    value = F(value)
    return arb(fmpq(value.numerator, value.denominator))


def evaluate(coefficients, point):
    value = 0
    for coefficient in reversed(coefficients):
        value = value * point + coefficient
    return value


def differences():
    return trace_differences([3, 4, 7, *TRIPLE])


def moments(cut, atom=ATOM):
    D = differences()
    original = [(2*atom**(j+1)-cut**(j+1)-D[j+1])/F(j+1)
                for j in range(7)]
    return [sum(F(comb(j,k))*2**(j-k)*original[k] for k in range(j+1))
            /4**(j+1) for j in range(7)]


def output_home():
    source = Path(__file__).resolve()
    path = source.parents[2] / 'outputs' / source.parent.name
    path.mkdir(parents=True, exist_ok=True)
    return path


def positive_penalty(q, kernel):
    import sympy as sp
    assert kernel in (0,1)
    variable = sp.Symbol('u')
    sign_coefficients = [-F(1)]+q if kernel else q
    r = sp.Poly(sum(sp.Rational(v.numerator,v.denominator)*variable**j
                    for j,v in enumerate(sign_coefficients)), variable)
    isolated = r.intervals(eps=sp.Rational(1,10**14))
    boxes = []
    for (left,right), multiplicity in isolated:
        a,b = F(int(left.p),int(left.q)),F(int(right.p),int(right.q))
        if b <= 0 or a >= 1:
            continue
        assert 0 < a <= b < 1
        boxes.append((a,b))
    assert all(boxes[i][1]<boxes[i+1][0] for i in range(len(boxes)-1))
    if kernel:
        assert evaluate(sign_coefficients,F(0)) == -1
    primitive = [F(0)] + [v/F(j+1) for j,v in enumerate(q)]
    primitive_ball = list(map(ball,primitive))
    q_ball = list(map(ball,q))
    penalty = arb(0)
    previous = F(0)
    for a,b in boxes+[(F(1),F(1))]:
        if a > previous:
            midpoint = (a+previous)/2
            sign = evaluate(sign_coefficients,midpoint)
            assert sign != 0
            if sign > 0:
                integral = (evaluate(primitive_ball,ball(a))
                            -evaluate(primitive_ball,ball(previous)))
                if kernel:
                    assert previous > 0
                    integral -= ball(a/previous).log()
                assert integral > 0
                penalty += integral.upper()
        if a < b:
            interval = ball(a).union(ball(b))
            upper = (evaluate(q_ball,interval)-kernel/interval).upper()
            if upper > 0:
                penalty += ball(b-a)*upper
        previous = b
    penalty=penalty.upper()
    assert penalty.is_exact() and penalty>=0
    return penalty,boxes,primitive


def verify(coefficients, atom=ATOM, kernel=1, verbose=True):
    assert len(coefficients) == 7
    q = list(map(F, coefficients))
    ctx.prec = 256
    penalty,boxes,primitive = positive_penalty(q,kernel)
    primitive_ball=list(map(ball,primitive))
    # F(t)=integral_0^((t+2)/4) q(u) du; compute D(F) exactly.
    original_primitive = [F(0)]*8
    for j,v in enumerate(primitive):
        for k in range(j+1):
            original_primitive[k] += v*F(comb(j,k))*2**(j-k)/4**j
    D_F = sum(v*d for v,d in zip(original_primitive,differences()))
    cut = ball(CUT_LEFT).union(ball(CUT_RIGHT))
    dual_value = (2*evaluate(primitive_ball,ball((atom+2)/4))
                  -evaluate(primitive_ball,(cut+2)/4)-ball(D_F)-penalty)
    required = 2*ball(2+atom).log()-(2+cut).log() if kernel else arb(0)
    record = {'triple':list(TRIPLE),'atom':str(atom),'precision':256,
              'kind':'endpoint' if kernel else 'density-cap',
              'q':[str(v) for v in q], 'root_boxes':[[str(a),str(b)] for a,b in boxes],
              'penalty_upper':str(penalty),'dual_lower_ball':str(dual_value),
              'required_ball':str(required),'difference_ball':str(dual_value-required),
              'gap_lower':str((dual_value-required).lower()),
              'gap_upper':str((dual_value-required).upper()),
              'excludes_whole_cut_interval': bool(dual_value > required)}
    if verbose:
        print(json.dumps(record,indent=2),flush=True)
    return record


def separate_moments():
    import numpy as np
    import sympy as sp
    from scipy.optimize import linprog
    from scipy.sparse import hstack,eye
    atom=F(-489,500)
    variable=sp.Symbol('u')
    basis=[[F(sp.expand(sp.chebyshevt(j,2*variable-1)).coeff(variable,k))
            for k in range(7)] for j in range(7)]
    mu=moments((CUT_LEFT+CUT_RIGHT)/2,atom)
    target=np.array([float(sum(a*b for a,b in zip(row,mu))) for row in basis])
    points=(np.arange(NODES)+0.5)/NODES
    values=np.array([evaluate(list(map(float,row)),points) for row in basis])
    objective=np.r_[-target,np.ones(NODES)/NODES]
    constraints=hstack([values.T,-eye(NODES)],format='csr')
    result=linprog(objective,A_ub=constraints,b_ub=np.zeros(NODES),
                   bounds=[(-1,1)]*7+[(0,None)]*NODES,method='highs',
                   options={'time_limit':15.0})
    record={'atom':str(atom),'nodes':NODES,'lp_calls':1,'limit_seconds':15.0,
            'status':int(result.status),'message':str(result.message),
            'objective':float(result.fun) if result.fun is not None else None}
    if result.success:
        coefficients=[F(int(round(v*DENOMINATOR)),DENOMINATOR) for v in result.x[:7]]
        q=[sum(coefficients[j]*basis[j][k] for j in range(7)) for k in range(7)]
        record['verification']=verify(q,atom,kernel=0)
    (output_home()/'endpoint_moment_separation.json').write_text(
        json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print({key:value for key,value in record.items() if key!='verification'},flush=True)


def propose(atom=ATOM):
    import numpy as np
    from scipy.optimize import linprog
    points=(np.arange(NODES)+0.5)/NODES
    target=np.array(list(map(float,moments((CUT_LEFT+CUT_RIGHT)/2,atom))))
    result=linprog(1/points,A_eq=np.array([points**j for j in range(7)]),
                   b_eq=target,bounds=(0,1/NODES),method='highs',
                   options={'time_limit':15.0})
    record={'atom':str(atom),'nodes':NODES,'lp_calls':1,'limit_seconds':15.0,
            'status':int(result.status),'message':str(result.message),
            'objective':float(result.fun) if result.fun is not None else None,
            'continuous_feasibility_claimed_from_lp':False}
    if result.success:
        q=[F(int(round(v*DENOMINATOR)),DENOMINATOR) for v in result.eqlin.marginals]
        record['verification']=verify(q,atom)
    names={ATOM:'endpoint_dual_proposal.json',F(-489,500):'endpoint_dual_secondary.json',
           F(-239,250):'endpoint_dual_middle.json',F(-19,20):'endpoint_dual_final.json'}
    name=names[atom]
    (output_home()/name).write_text(
        json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print({key:value for key,value in record.items() if key!='verification'},flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    commands.add_parser('propose')
    commands.add_parser('secondary',help='One fixed follow-up at s=-489/500.')
    commands.add_parser('middle',help='One fixed remaining-band test at s=-239/250.')
    commands.add_parser('final',help='One fixed remaining-band test at s=-19/20.')
    commands.add_parser('separate',help='One bounded density-cap separation at s=-489/500.')
    commands.add_parser('verify-fixed',help='Verify all four retained polynomials without optimization.')
    check=commands.add_parser('verify')
    check.add_argument('--input',type=Path,required=True)
    args=parser.parse_args()
    if args.command=='propose':
        propose()
    elif args.command=='secondary':
        propose(F(-489,500))
    elif args.command=='middle':
        propose(F(-239,250))
    elif args.command=='final':
        propose(F(-19,20))
    elif args.command=='separate':
        separate_moments()
    elif args.command=='verify-fixed':
        native=json.loads((Path(__file__).resolve().parent/'inputs/endpoint_first_duals.json').read_text())
        assert native['triple']==list(TRIPLE) and len(native['certificates'])==4
        rows=[]
        for item in native['certificates']:
            assert item['kind'] in ('density-cap','endpoint')
            row=verify(item['q'],F(item['atom']),kernel=0 if item['kind']=='density-cap' else 1,verbose=False)
            assert row['excludes_whole_cut_interval']
            rows.append(row)
            print({k:row[k] for k in ('atom','kind','gap_lower','excludes_whole_cut_interval')},flush=True)
        (output_home()/'endpoint_dual_fixed_verification.json').write_text(json.dumps(rows,indent=2)+'\n')
    else:
        native=json.loads(args.input.read_text(encoding='utf-8'))
        assert native['triple']==list(TRIPLE)
        assert native['kind'] in ('density-cap','endpoint')
        verify(native['q'],F(native['atom']),kernel=0 if native['kind']=='density-cap' else 1)


if __name__=='__main__':
    main()
