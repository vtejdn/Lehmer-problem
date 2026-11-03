"""Exact Q(theta) certificate for the decisive fourth/eighth phase moments.

No Arb calculation or stored output is used as an oracle. The residue
formula is derived in D29. This separately implements finite formal series
over the cubic number field and checks signs by rational interval arithmetic.
"""

from fractions import Fraction as F
from math import lcm, gcd
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

import sympy as sp

HERE = (_J_PROGRAM / 'exact.py').parent
x = sp.Symbol("x")
root = sp.CRootOf(x**3-x-1, 0)
K = sp.QQ.algebraic_field(root)
theta = K.from_sympy(root)
zero, one = K.zero, K.one
assert theta**3-theta-one == zero


def convolution(a,b,n):
    return [sum((a[i]*b[j] for i in range(len(a)) for j in range(len(b))
                 if i+j == k), zero) for k in range(n)]


def reciprocal(a,n):
    result = [one/a[0]]
    for k in range(1,n):
        result.append(-sum((a[j]*result[k-j] for j in range(1,min(k+1,len(a)))),zero)/a[0])
    assert convolution(a,result,n) == [one]+[zero]*(n-1)
    return result


def moment(k):
    num = [theta*(theta+one),3*theta**2+2*theta,3*theta+one,one]
    den = [3*theta**2-one,3*theta,one]
    regular = convolution(num,reciprocal(den,k),k)
    powered = [one]+[zero]*(k-1)
    for _ in range(k):
        powered = convolution(powered,regular,k)
    return one-convolution(powered,reciprocal([theta,one],k),k)[k-1]


def coefficients(a):
    # ANP's list is descending and may omit leading zeros.
    vals = [F(int(v.numerator),int(v.denominator)) for v in a.to_list()][::-1]
    vals += [F(0)]*(3-len(vals))
    denominator = lcm(*(v.denominator for v in vals))
    numerator = [int(v*denominator) for v in vals]
    common = gcd(denominator,gcd(*numerator))
    return [v//common for v in numerator],denominator//common


def enclose(a,lo,hi):
    nums,den = coefficients(a)
    lower = upper = F(0)
    for i,num in enumerate(nums):
        bounds = (lo**i,hi**i) if num>=0 else (hi**i,lo**i)
        lower += F(num,den)*bounds[0]
        upper += F(num,den)*bounds[1]
    assert lower<=upper
    return lower,upper


def main():
    # These exact endpoint signs isolate the unique real root, since f'>0 here.
    lo,hi = F(13247179572447,10**13),F(13247179572448,10**13)
    assert lo**3-lo-1<0<hi**3-hi-1 and lo>1
    c4,c8 = moment(4),moment(8)
    income = -c4*c8/4
    items = {}
    for label,value,target in [
        ("c4",c4,(F(-358,1000),F(-357,1000))),
        ("c8",c8,(F(245,1000),F(246,1000))),
        ("minus_c4_c8_over_4",income,(F(21931,10**6),F(21932,10**6))),
    ]:
        bounds = enclose(value,lo,hi)
        assert target[0]<bounds[0]<=bounds[1]<target[1]
        nums,den = coefficients(value)
        items[label] = {"numerator_ascending":nums,"denominator":den,
                        "rational_interval":[str(t) for t in bounds],
                        "certified_coarse_interval":[str(t) for t in target]}
        print(label,nums,den,items[label]["certified_coarse_interval"])
    output = {'field_polynomial': 'x^3-x-1', 'root_interval': [str(lo), str(hi)], 'quantities': items, 'scope': 'Exact algebraic finite residues and rational sign certificates. No finite Salem polynomial roots are numerically approximated.'}
    ((_J_OUTPUT / 'exact-results.json')).write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")


if __name__ == "__main__":
    main()
