"""Enumerate integral square roots of ternary residue adjustments on exact shells."""
import argparse
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path
import sys

from flint import arb, ctx, fmpz_mat, fmpz_poly

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'Yin_J_G0150'))
from moments import sign_columns, target_cut


def inputs(p, k):
    n = p // 2
    t = fmpz_poly([0, 1])
    trace = [fmpz_poly([2]), t]
    for _ in range(2, p):
        trace.append(t * trace[-1] - trace[-2])
    B = sum(trace[1:n+1], fmpz_poly([1]))
    D = B - trace[n]
    h = fmpz_poly([1])
    odd = set()
    for a in sign_columns(p, k):
        d = 1
        while a % 3 == 0:
            d *= 3
            a //= 3
        u = a if a % 2 else p // d - a
        h = h * (trace[u] // t)(trace[d]) % B
        odd.symmetric_difference_update([d])
    for d in odd:
        h = h * trace[d] % B
    return t, B, D, h


def jacobi(n):
    a = fmpz_mat(n, n)
    for i in range(n-1):
        a[i, i+1] = a[i+1, i] = 1
    a[n-1, n-1] = -1
    return a


def identity(n):
    a = fmpz_mat(n, n)
    for i in range(n):
        a[i, i] = 1
    return a


def multiply_matrix(poly, J, I):
    result = fmpz_mat(J.nrows(), J.nrows())
    for a in reversed(poly.coeffs()):
        result = J * result + a * I
    return result


def upper_pivots(G):
    """Fraction-free LDL; rows contain a leading minor and its mixed minors."""
    a = [[int(v) for v in row] for row in G.tolist()]
    previous = 1
    rows = []
    for i in range(len(a)):
        pivot = a[i][i]
        assert pivot > 0
        rows.append(a[i][i:])
        for j in range(i+1, len(a)):
            for k in range(j, len(a)):
                value = pivot * a[j][k] - a[i][j] * a[i][k]
                assert value % previous == 0
                a[j][k] = value // previous
        previous = pivot
    return rows


def half_shell(rows, target):
    """One representative modulo simultaneous negation, on the shell only."""
    z = [0] * len(rows)

    def extend(i, budget, any_nonzero):
        if i < 0:
            if budget == 0 and any_nonzero:
                yield tuple(z)
            return
        pivot, *cross = rows[i]
        prev = rows[i-1][0] if i else 1
        center = sum(a*j for a, j in zip(cross, z[i+1:]))
        bound = isqrt(budget * prev)
        first = -((bound + center) // pivot)
        if not any_nonzero:
            first = max(0, first)
        for v in range(first, (bound-center)//pivot + 1):
            loss = (pivot*v + center)**2
            z[i] = v
            yield from extend(i-1, (budget*prev-loss)//pivot, any_nonzero or v != 0)

    if target > 0:
        yield from extend(len(rows)-1, rows[-1][0]*target, False)


def root_poly(w, t):
    prev, cur = fmpz_poly([]), fmpz_poly([1])
    result = fmpz_poly([])
    for v in w:
        result += v * cur
        prev, cur = cur, t * cur - prev
    return result


def whole_measure(Q):
    d = Q.degree()
    z = fmpz_poly([0, 1])
    P = sum((Q[i]*z**(d-i)*(1+z*z)**i for i in range(d+1)), fmpz_poly([]))
    # FLINT encloses all distinct complex roots of each squarefree factor.
    # Intersect each modulus contribution with the defining max(1, |root|).
    with ctx.workprec(192):
        total = arb(1)
        roots = P.complex_roots()
        assert sum(mult for _, mult in roots) == 2*d
        for root, mult in roots:
            total *= abs(root).max(arb(1))**mult
        assert total.rad() < arb('1e-13')
        return str(total)


def check_separator(p, y):
    """Certify the gap by Sturm signs and the product needed for the half-unit bound."""
    n = p // 2
    a, b = y.as_integer_ratio()
    prev, cur = 1, a+b
    old_sign, changes = 1, 0
    for i in range(1, n+1):
        if i > 1:
            prev, cur = cur, a*cur-b*b*prev
        if cur:
            sign = 1 if cur > 0 else -1
            changes += sign != old_sign
            old_sign = sign
    assert cur and changes == n-target_cut(p)
    return p*abs(cur) > 2*b**n


def quadratic_separator_243():
    """Certify the next-moment restriction at p=243 by integer comparisons."""
    p, n = 243, 121
    t = fmpz_poly([0, 1])
    B0, B = fmpz_poly([1]), 1+t
    for _ in range(2, n+1):
        B0, B = B, t*B - B0
    F = 4 + 4*t - t*t
    for a, b, sign in [(-5, 6, -1), (-33, 40, 1), (-41, 50, 1)]:
        check_separator(p, Fraction(a,b))
        assert sign * (4*b*b + 4*a*b - a*a) > 0
    resultant = abs(B.resultant(F))
    for delta, bound in [(1, 2), (2**53, 3)]:
        assert n**n * p * delta * resultant > (bound*p)**n
    print(f'p=243 |Res(B,F)|={resultant}; mass >2 for every nonzero norm, >3 at 2^53')
    assert all(10*target_cut(3**m) >= 3**m for m in range(3, 10))
    y = Fraction(-41, 50)
    T4 = y**4 - 4*y*y + 2
    for moment, radius in [(2, Fraction(83,50)), (0, Fraction(199,100))]:
        assert 16 - 4*moment + T4 > radius**4 + radius**-4
    for y, radius in [(Fraction(-7,6), Fraction(7,5)), (Fraction(-37,27), Fraction(7,6))]:
        w = radius + 1/radius - 2
        assert 20*w + 8*w*w + w**3 < Fraction(184,27) + y**3 - 2*y*y


def next_profiles():
    p = 6561
    y = Fraction(-68, 45)
    assert check_separator(p, y)
    allowed = []
    for x in range(-2, 3):
        K, L, N = x*x+2, -4*x, 6+2*x*x
        W = (2+y)*L - 2*y*K - N
        lower_U = -1-2*x
        upper_E = N-y*L-6*(L-y*K)+16*(K-(2+y)*lower_U)
        if min(W, upper_E) > Fraction(1, 2):
            allowed.append(x)
    assert allowed == [-1]
    print('p=6561 k=746: only x=-1 survives these two tests when N also matches')


def run(p, profiles, witnesses):
    k = target_cut(p)
    a, b = {27:(1,2), 81:(-1,3), 243:(-5,6)}[p]
    t, B, D, h = inputs(p, k)
    n = B.degree()
    J, I = jacobi(n), identity(n)
    H = multiply_matrix(h, J, I)
    G = (b * J - a * I) * H
    delta = abs(int(B.resultant(h)))
    assert delta == abs(H.det())
    # Certification of the separator and positive definiteness uses exact pivots.
    Gred, change = G.lll(transform=True, rep='gram', gram='exact')
    assert abs(change.det()) == 1 and Gred == change * G * change.transpose()
    rows = upper_pivots(Gred)
    Hred = change * H * change.transpose()
    print(f'p={p} k={k} delta={delta} det(G)={rows[-1][0]}', flush=True)
    for x in profiles:
        K, L = x*x+2, -4*x
        target = b*L - a*K
        count = Counter()
        samples = []
        for z in half_shell(rows, target):
            count['half_shell'] += 1
            row = fmpz_mat([z])
            if (row * Hred * row.transpose())[0, 0] != K:
                continue
            count['both'] += 1
            v = root_poly((row * change).entries(), t)
            if abs(v.resultant(B)) != 1:
                continue
            count['units'] += 1
            adjusted = (h*v*v) % B
            C = (D*adjusted) % B
            assert C[n-1] == K and C[n-2]-B[n-1]*K == L
            Q = (t-2*x)*B+C
            assert abs(B.resultant(Q)) == delta
            endpoint = int((-1)**(n+1) * Q(-2))
            count['endpoint'] += int(endpoint > 0)
            samples.append((adjusted, endpoint, whole_measure(Q)))
        print(f'x={x} radius2={target} shell={count["half_shell"]} both={count["both"]} '
              f'units={count["units"]} endpoint={count["endpoint"]}', flush=True)
        for adjusted, endpoint, measure in samples:
            print(f'  P(-1)={endpoint} M={measure}', flush=True)
            if witnesses:
                print('  h ascending:', adjusted.coeffs(), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('p', type=int, choices=(27, 81, 243, 6561))
    parser.add_argument('--x', type=int, nargs='+', choices=range(-2,3))
    parser.add_argument('--separator', action='store_true',
                        help='check the separator certificate at 243 or 6561')
    parser.add_argument('--witnesses', action='store_true')
    args = parser.parse_args()
    if args.separator and args.p == 243 and args.x is None:
        quadratic_separator_243()
    elif args.separator and args.p == 6561 and args.x is None:
        next_profiles()
    elif args.x and not args.separator and args.p in (27, 81, 243):
        run(args.p, args.x, args.witnesses)
    else:
        parser.error('select an implemented raw shell with --x, or a certificate with --separator')
