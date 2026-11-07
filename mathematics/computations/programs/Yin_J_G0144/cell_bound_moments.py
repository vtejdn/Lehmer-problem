"""Enclose all 32 Newton sums for the fixed degree-64 root cell, over the full box."""

from fractions import Fraction
from math import ceil, floor, prod

from trace64_cell import N, D, SEPARATORS, disk_rows


def circle_polynomials(t):
    # C_k(2 cos u)=2 cos(ku); U_k(2 cos u)=sin((k+1)u)/sin u.
    first, second = [Fraction(2), t], [Fraction(1), t]
    for k in range(2, N+1):
        first.append(t*first[-1] - first[-2])
        second.append(t*second[-1] - second[-2])
    return first, second


def criticals_above(tables, k):
    # At each interior critical t=2 cos(l*pi/k), C_k(t)=2(-1)^l.
    # The Sturm chain U_{k-1},...,U_0 counts these criticals above t.
    # Successive polynomials obey negative Euclidean remainders and
    # U_{k-2} and U'_{k-1} have the same sign at each zero of U_{k-1}.
    vals = tables[1][:k][::-1]
    assert vals[0] != 0
    signs = [v > 0 for v in vals if v]
    return sum(a != b for a,b in zip(signs, signs[1:]))


def moment_ranges():
    circle = [circle_polynomials(Fraction(a, 1000)) for a in SEPARATORS]
    disks = disk_rows()
    ranges = []
    for k in range(1, N+1):
        above = [criticals_above(table,k) for table in circle]
        assert above[0] == k-1 and above[-1] == 0
        low = high = Fraction(0)
        for j,(p,q) in enumerate(zip(above, above[1:])):
            assert p >= q
            extrema = [circle[j][0][k], circle[j+1][0][k]]
            extrema.extend(2*(-1)**ell for ell in range(q+1, p+1))
            low += min(extrema)
            high += max(extrema)
        # A conjugate pair of trace roots contributes 2 Re C_k(w).
        center = 2 * disks[0][0][k]
        error = 2 * sum(abs(real[k])+abs(imag[k]) for real,imag in disks[1:])
        low += Fraction(center-error, D**N)
        high += Fraction(center+error, D**N)
        lower, upper = ceil(low), floor(high)
        ranges.append((lower, upper))
    return ranges


def prefix_counts(ranges, depth):
    counts = [0]*depth
    def visit(prefix, sums):
        k = len(prefix)+1
        lower, upper = ranges[k-1]
        offset = -sum(a*s for a,s in zip(prefix, reversed(sums)))
        for a in range(-3,4):
            value = offset-k*a
            if lower <= value <= upper:
                counts[k-1] += 1
                if k < depth:
                    visit((*prefix,a), (*sums,value))
    visit((), ())
    return counts


if __name__ == "__main__":
    ranges = moment_ranges()
    caps = [min(7, 1 + (hi-lo)//k) for k,(lo,hi) in enumerate(ranges,1)]
    print("Closed integer Newton-sum intervals in order k=1,...,32:", ranges)
    print("Maximum children per prefix in order:", caps)
    print("Product upper bound:", prod(caps))
    counts = prefix_counts(ranges, 8)
    print("Exact numbers of height-three prefixes passing these bounds to depth 8:", counts)
    print("Global upper bound using exact depth-8 count:", counts[-1]*prod(caps[8:]))
