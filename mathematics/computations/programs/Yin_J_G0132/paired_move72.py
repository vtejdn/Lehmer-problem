"""Only Pi11*Pi59; true original restrictions in degree72 J, modulo4.

No full degree357 T or cofactor H is expanded.
"""
from pathlib import Path
import json
from main import add, mul, rem, power, compose, chebyshev, canonical_mod4, trim
from odd_support_probe import binary_order, binary_initial_unit


def kernel(n):
    result = [1]
    for j in range(1, (n-1)//2+1):
        result = add(result, chebyshev(j))
    return result


def monic_division(a, b):
    assert b[-1] == 1
    work = list(a)
    quotient = [0]*max(1, len(a)-len(b)+1)
    while work != [0] and len(work) >= len(b):
        shift = len(work)-len(b)
        lead = work[-1]
        quotient[shift] = lead
        for j, value in enumerate(b):
            work[shift+j] -= lead*value
        trim(work)
    return trim(quotient), work


def main():
    f3, f5, f9 = [1, 1], [-1, 1, 1], [1, -3, 0, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    divisor = mul(power(f15, 2), compose(f30, chebyshev(16)))
    assert len(divisor)-1 == 72
    moves = {}
    for n in (11, 59):
        bn = kernel(n)
        dn, residue = monic_division(compose(bn, chebyshev(3)), bn)
        assert residue == [0] and len(dn)-1 == n-1
        pi = mul(bn, power(dn, 2))
        assert len(pi)-1 == 5*(n-1)//2
        moves[n] = dict(B_coefficients=bn, D_coefficients=dn, Pi_coefficients=pi)
    factors = [('endpoint', [-2, 1], 2), ('F3', f3, 2), ('F5', f5, 3),
               ('F9', f9, 4), ('B187', kernel(187), 1),
               ('Pi11', moves[11]['Pi_coefficients'], 1),
               ('Pi59', moves[59]['Pi_coefficients'], 1)]
    original = []
    weights = {}
    canonical_j = {}
    for p in (2, 3, 5):
        cp = chebyshev(p)
        weight = [1]
        for _, factor, exponent in factors:
            contribution = power(compose(factor, cp, divisor, 4), exponent, divisor, 4)
            weight = rem(mul(weight, contribution, 4), divisor, 4)
        theta = canonical_mod4(divisor, p)
        weights[p], canonical_j[p] = weight, theta
        original.append(rem(mul(weight, theta, 4), divisor, 4))
    a, b, c = original
    f = rem(add([2*v for v in power(c, 2, divisor, 4)], power(a, 5, divisor, 4), -3), divisor, 4)
    g = rem(add(power(c, 3, divisor, 4), power(b, 5, divisor, 4), -2), divisor, 4)
    base = add(power(b, 2, divisor, 4), power(a, 3, divisor, 4), -1)
    xp, xm = rem(add(base, g), divisor, 4), rem(add(base, g, -1), divisor, 4)
    residues = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
    valuations = {key: (0 if any(v % 2 for v in poly)
                        else 1 if any(poly) else 'at_least_2')
                  for key, poly in residues.items()}
    halves = {key: [v//2 for v in poly] for key, poly in residues.items()
              if all(v % 2 == 0 for v in poly)}
    gates = dict(F_mod4=(f == [0]), X_plus_mod2=all(v % 2 == 0 for v in xp),
                 X_minus_mod2=all(v % 2 == 0 for v in xm), G_nonzero_mod2=any(v % 2 for v in g))
    payload = dict(scope='only Q=Pi11 Pi59; original weighted degree72 restrictions',
                   selected_moves=[11, 59], quotient_degree=72, full_trace_degree=357,
                   full_reciprocal_degree=714, full_radical_degree=201,
                   J_coefficients=divisor, moves=moves,
                   cofactor_factor_list=[dict(name=name, coefficients=factor, exponent=e)
                                         for name, factor, e in factors],
                   canonical_J_mod4=canonical_j, cofactor_weights_mod4=weights,
                   original_restrictions_mod4=residues,
                   restriction_valuations_through_mod4=valuations,
                   global_gates_via_GR6=gates,
                   binary_f15_orders={key: binary_order(poly, f15) for key, poly in residues.items()},
                   half_f15_orders={key: binary_order(poly, f15) for key, poly in halves.items()},
                   half_f15_initial_units={key: binary_initial_unit(poly, f15) for key, poly in halves.items()})
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    tmp = output/'paired_move72_result.json.partial'
    tmp.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'paired_move72_result.json')
    print(json.dumps({key: payload[key] for key in ('global_gates_via_GR6',
                      'restriction_valuations_through_mod4', 'binary_f15_orders',
                      'half_f15_orders', 'half_f15_initial_units')}))


if __name__ == '__main__':
    main()
