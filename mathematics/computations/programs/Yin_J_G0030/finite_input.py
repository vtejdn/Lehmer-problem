"""One validated actual P_129 mixed Fourier coefficient, using Newton sums.

The irreducible Salem family is an accepted input from L38/L131; no factor
classification is recomputed here. The new exact Salem damping identity
is proved in D29. Exact rational root signs and Arb enclosures handle the
large cancellation between integral Newton sums and exterior-root powers.
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

HERE = (_J_PROGRAM / 'finite_input.py').parent
N = 129
n = 4*N
d = N+3
BITS = 800


def polynomial_sign(t):
    a,b = t.numerator,t.denominator
    # b^(N+3) P_N(a/b), evaluated as an exact integer.
    return a**N*(a**3-a*b*b-b**3) + b**N*(b**3-a*a*b-a**3)


def main():
    assert N%120 == 9 and N>=16
    lo,hi = F(13,10),F(4,3)
    assert polynomial_sign(lo)<0<polynomial_sign(hi)
    while hi-lo>F(1,2**BITS):
        mid = (lo+hi)/2
        if polynomial_sign(mid)<0:
            lo = mid
        else:
            hi = mid
    assert polynomial_sign(lo)<0<polynomial_sign(hi)
    ctx.prec = 1000
    mid,rad = (lo+hi)/2,(hi-lo)/2
    tau = arb(fmpq(mid.numerator,mid.denominator),fmpq(rad.numerator,rad.denominator))
    # x^d + sum_j a_j x^(d-j), retaining all six nonzero coefficients.
    coeff = {2:-1,3:-1,N:-1,N+1:-1,d:1}
    s = [d]
    for k in range(1,2*n+1):
        value = -sum(a*s[k-j] for j,a in coeff.items() if j<k)
        if k<=d:
            value -= k*coeff.get(k,0)
        s.append(value)
    q = 1/tau
    U_n = s[n]-tau**n-q**n
    U_2n = s[2*n]-tau**(2*n)-q**(2*n)
    b_n,b_2n = U_n+2*q**n,U_2n+2*q**(2*n)
    C = b_n*b_2n+2*q**n*(1-q**(2*n))
    by_pair_types = U_n*U_2n+2*q**n*U_2n+2*q**(2*n)*U_n+2*q**n+2*q**(3*n)
    assert C.overlaps(by_pair_types)
    assert abs(U_n)<d-2 and abs(U_2n)<d-2
    contribution_per_degree = -C/(n*d)
    assert contribution_per_degree>fmpq(2,100)
    result = {'N': N, 'degree': d, 'frequency': n, 'precision_bits': 1000, 'tau_root_interval': [str(lo), str(hi)], 'tau': tau.str(45), 'integer_Newton_s_n': str(s[n]), 'integer_Newton_s_2n': str(s[2 * n]), 'U_n': U_n.str(45), 'U_2n': U_2n.str(45), 'C_n': C.str(45), 'minus_C_n_over_n_d': contribution_per_degree.str(45), 'certified_lower_bound': '1/50', 'scope': 'One actual P_129 input; exact root bracket signs, Newton sums and interval cancellation control. Family irreducibility/Salem geometry uses fixed L38/L131. No resultant lower bound is inferred from a single Fourier term.'}
    ((_J_OUTPUT / 'finite-result.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("P_129 degree",d,"frequency",n,"contribution/d",contribution_per_degree.str(45))


if __name__ == "__main__":
    main()
