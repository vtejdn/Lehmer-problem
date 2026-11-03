"""Validated finite residue coefficients for the plastic phase map.

For g=-f*/f and its unique exterior pole theta, the kth Haar moment is
1-Res_theta(g(z)^k/z). The responsible draft proves this contour identity
and its actual primitive Salem-root interpretation.
"""

from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

import flint
from flint import arb, fmpq, ctx

HERE = (_J_PROGRAM / 'main.py').parent
PRECISION = 400
MAX_K = 32


def ball_fraction(q):
    return arb(fmpq(q.numerator,q.denominator))


def plastic_root():
    lo,hi = F(13,10),F(4,3)
    def f(x): return x**3-x-1
    assert f(lo)<0<f(hi)
    while hi-lo > F(1,2**320):
        mid = (lo+hi)/2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return arb(fmpq(((lo+hi)/2).numerator,((lo+hi)/2).denominator),
               fmpq(((hi-lo)/2).numerator,((hi-lo)/2).denominator)), [str(lo),str(hi)]


def multiply(a,b,n):
    out = [arb(0) for _ in range(n)]
    for i,x in enumerate(a[:n]):
        for j,y in enumerate(b[:n-i]):
            out[i+j] += x*y
    return out


def inverse(a,n):
    assert not a[0].contains(0)
    out = [1/a[0]]
    for j in range(1,n):
        out.append(-sum(a[i]*out[j-i] for i in range(1,min(j+1,len(a))))/a[0])
    return out


def power(a,k,n):
    out = [arb(1)]+[arb(0)]*(n-1)
    while k:
        if k&1:
            out = multiply(out,a,n)
        k //= 2
        if k:
            a = multiply(a,a,n)
    return out


def main():
    ctx.prec = PRECISION
    theta,bracket = plastic_root()
    moments = {}
    for k in range(1,MAX_K+1):
        # t*g(theta+t) = -f*(theta+t)/(f(theta+t)/t).
        numerator = [theta*(theta+1),3*theta*theta+2*theta,3*theta+1,arb(1)]
        denominator = [3*theta*theta-1,3*theta,arb(1)]
        regular = multiply(numerator,inverse(denominator,k),k)
        residue_series = multiply(power(regular,k,k),inverse([theta,arb(1)],k),k)
        moment = 1-residue_series[k-1]
        assert moment.is_finite() and abs(moment) <= 1
        moments[k] = moment
    q = theta*(theta+1)/(3*theta*theta-1)
    regular_constant = (2*theta+3*theta*theta)/(3*theta*theta-1)-3*theta*theta*(theta+1)/(3*theta*theta-1)**2
    assert moments[1].overlaps(1-q/theta)
    assert moments[2].overlaps(1-(2*q*regular_constant/theta-q*q/theta**2))
    pairs = []
    for k in range(1,MAX_K//2+1):
        income = -moments[k]*moments[2*k]/k
        sign = 1 if income>0 else -1 if income<0 else 0
        pairs.append({"k":k,"c_k":moments[k].str(55),"c_2k":moments[2*k].str(55),
                      "mixed_mode_income_per_N":income.str(55),"certified_sign":sign})
    result = {'precision_bits': PRECISION, 'theta_root_interval': bracket, 'theta': theta.str(55), 'moments': {str(k): v.str(55) for k, v in moments.items()}, 'dyadic_pairs': pairs, 'closed_formula_crosschecks': [1, 2], 'scope': 'Validated finite phase-map residues only. Actual-root asymptotics and irreducible-family hypotheses are written in D29. Total measure tends to the fixed plastic value, not zero.'}
    ((_J_OUTPUT / 'results.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    for row in pairs:
        print(row["k"],row["certified_sign"],row["mixed_mode_income_per_N"])


if __name__ == "__main__":
    main()
