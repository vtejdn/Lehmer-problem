"""Exact plastic/Lehmer resultant identities and certified energy constants.

The all-index asymptotic is proved in D38 using the already accepted Dim16
interface. Finite resultant checks here are not extrapolated to that limit.
"""

from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

import flint
from flint import arb, ctx, fmpq
import sympy as sp

HERE = (_J_PROGRAM / 'verify.py').parent
z = sp.Symbol("z")
f = z**3-z-1
h = 1-z**2-z**3
L = z**10+z**9-z**7-z**6-z**5-z**4-z**3+z+1


def root_ball(poly,lo,hi,bits=280):
    coefficients = [int(v) for v in sp.Poly(poly,z).all_coeffs()]
    def evaluate(t):
        ans = F(0)
        for c in coefficients:ans = ans*t+c
        return ans
    assert evaluate(lo)<0<evaluate(hi)
    while hi-lo>F(1,2**bits):
        mid = (lo+hi)/2
        if evaluate(mid)<0:lo = mid
        else:hi = mid
    assert evaluate(lo)<0<evaluate(hi)
    mid,rad = (lo+hi)/2,(hi-lo)/2
    return arb(fmpq(mid.numerator,mid.denominator),fmpq(rad.numerator,rad.denominator)),[str(lo),str(hi)]


def main():
    assert sp.expand(h**2*f.subs(z,z*z)+f**2*h.subs(z,z*z)-2*z*L) == 0
    assert sp.expand(h-z**8*f-(1-z)*L) == 0
    assert sp.resultant(f,h,z) == -1
    assert sp.resultant(f,1-z,z) == -1
    assert sp.resultant(L,f,z) == 1
    finite = []
    for N in (9,129):
        P = sp.Poly(z**N*f+h,z)
        d,q = P.degree(),N-8
        even = sum(c*z**(j//2) for (j,),c in P.terms() if j%2 == 0)
        odd = sum(c*z**((j-1)//2) for (j,),c in P.terms() if j%2 == 1)
        powered = sp.expand(even**2-z*odd**2)
        assert sp.Poly(powered,z).degree() == d and sp.LC(sp.Poly(powered,z)) == 1
        direct = int(sp.resultant(P.as_expr(),powered,z))
        plus = int(sp.resultant(L,sp.rem(z**q+1,L,z),z))
        Cq = int(abs(sp.resultant(L,sp.rem(z**q-1,L,z),z)))
        C2q = int(abs(sp.resultant(L,sp.rem(z**(2*q)-1,L,z),z)))
        assert direct == 2**d*plus and plus>0 and Cq*plus == C2q
        assert sp.resultant(P.as_expr(),f,z) == -1
        assert sp.resultant(P.as_expr(),L,z) == plus
        if N == 9:
            assert sp.resultant(P.as_expr(),P.as_expr().subs(z,z*z),z) == direct
        finite.append({"N":N,"d":d,"q":q,"full_powered_resultant":str(direct),
                       "plus_cyclic_norm":str(plus),"C_q":str(Cq),"C_2q":str(C2q),
                       "direct_powered_polynomial_identity_passed":True})
        print("Exact full identity passed",N,"quotient",plus,flush=True)
    ctx.prec = 320
    theta,theta_interval = root_ball(f,F(13,10),F(4,3))
    lam,lambda_interval = root_ball(L,F(117,100),F(118,100))
    kappa = (2*lam/(theta+1)).log()
    assert kappa.overlaps(arb(2).log()+lam.log()-3*theta.log())
    assert fmpq(119,10000)<kappa<fmpq(12,1000)
    c4 = (216755-364434*theta+94629*theta**2)/279841
    c8 = (-33746367025-182673511531*theta+168086028459*theta**2)/78310985281
    one_mode = -c4*c8/4
    remaining = kappa-one_mode
    assert one_mode>fmpq(21931,10**6) and remaining<fmpq(-1,100)
    ratio = kappa/theta.log()
    result = {'precision_bits': 320, 'polynomial_identities_and_unit_resultants_passed': True, 'finite_full_resultants': finite, 'theta_root_interval': theta_interval, 'lambda_root_interval': lambda_interval, 'theta': theta.str(50), 'lambda': lam.str(50), 'kappa_complete_energy_per_degree': kappa.str(50), 'certified_kappa_interval': ['119/10000', '3/250'], 'gamma_fourth_mode_per_degree': one_mode.str(50), 'remaining_original_angular_energy_per_degree': remaining.str(50), 'kappa_over_log_theta': ratio.str(50), 'scope': "Exact fixed polynomial identities and two direct finite powered-resultant checks; validated constants only. The all-N energy limit uses D38's proof and accepted Dim16-U001 bound, not these finite checks."}
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("kappa",kappa.str(50),"remaining",remaining.str(50),"ratio",ratio.str(50),flush=True)


if __name__ == "__main__":main()
