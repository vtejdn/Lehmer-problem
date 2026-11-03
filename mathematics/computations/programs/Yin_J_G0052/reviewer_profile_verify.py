"""Independent same-scope C822 profile verification using R1180 graph helpers.

No author mathematical module is imported.  Integer square roots decide exact
quadratic signs; C301 coefficients and real-place products are formed directly
from original coordinates.  The author output is read after reconstruction.
"""
import argparse
from fractions import Fraction as Q
from functools import cmp_to_key
import json
from math import isqrt, lcm
from pathlib import Path

import reviewer_midpoint_verify as checked

TIMES = (16, 32, 64, 128)
THRESHOLDS = tuple(map(Q, ('1/20', '1/10', '1/5', '1/2', '1', '2')))
ROOT_LO, ROOT_HI = Q(3605551275463989, 10**15), Q(3605551275463990, 10**15)


def sign(pair):
    x, y = map(Q, pair)
    denominator = lcm(x.denominator, y.denominator)
    a, b = int(x*denominator), int(y*denominator)
    if b == 0:
        return (a > 0) - (a < 0)
    # sqrt(13*b*b) is strictly between this integer and the next one.
    k = isqrt(13*b*b)
    assert k*k < 13*b*b < (k+1)*(k+1)
    if b > 0:
        return 1 if a >= -k else -1
    return 1 if a > k else -1


def envelope(pair):
    a, b = map(Q, pair)
    low, high = sorted((a+b*ROOT_LO, a+b*ROOT_HI))
    return {'rational_part': checked.ratio(a), 'sqrt13_part': checked.ratio(b),
            'lower': checked.ratio(low), 'upper': checked.ratio(high),
            'decimal_rational_enclosure': [checked.ratio(Q(checked.floor(low*10**6), 10**6)),
                                            checked.ratio(Q(checked.ceil(high*10**6), 10**6))]}


def real_mark(a):
    # Independently use beta^k+beta^-k, whose first value is (1+sqrt13)/2.
    plus = (Q(1, 2), Q(1, 2))
    powers = [(Q(2), Q(0)), plus]
    for k in (2, 3):
        multiple = checked.field_mul(plus, powers[-1])
        powers.append(tuple(multiple[j]-powers[-2][j] for j in (0, 1)))
    s = [sum(a[j]*a[j+k] for j in range(4-k)) for k in range(4)]
    return (Q(s[0])+sum(s[k]*powers[k][0] for k in (1, 2, 3)),
            sum(s[k]*powers[k][1] for k in (1, 2, 3))), sum(s[1:])


def reverse_state(a):
    power, result = (1, 0, 0, 0), [0]*4
    for coefficient in a:
        power = checked.previous_original(power, 0)
        result = [x+coefficient*y for x, y in zip(result, power)]
    return tuple(result)


def check_statement_tables(rows):
    # Exact decimal literals from C822's three fixed tables, in midpoint order.
    moment_quantile = [
        ('0.061732', '0.061733', '1/16', '1/16', '0.475346', '0.475347'),
        ('0.079301', '0.079302', '0.103211', '0.103212', '0.340885', '0.340886'),
        ('0.098866', '0.098867', '0.170442', '0.170443', '0.562933', '0.562934'),
        ('0.105968', '0.105969', '0.162630', '0.162631', '0.537130', '0.537131')]
    tail_lowers = [
        ('0.547766', '0.443721', '0.421337', '0.056828', '0.006894', '0.000118'),
        ('0.657545', '0.637166', '0.350770', '0.079645', '0.014030', '0.000101'),
        ('0.822607', '0.633273', '0.310902', '0.130928', '0.010925', '0.000157'),
        ('0.816225', '0.577449', '0.386639', '0.107237', '0.012949', '0.000215')]
    signed_lowers = ('-0.040071', '-0.049122', '-0.059066', '-0.063001')
    for i, row in enumerate(rows):
        for obj, lower, upper in zip(
                (row['scaled_fourth_moment'], *(q['scaled_squared_radius'] for q in row['quantiles'])),
                moment_quantile[i][::2], moment_quantile[i][1::2], strict=True):
            a, b = Q(**obj['rational_part']), Q(**obj['sqrt13_part'])
            if lower == upper:
                assert a == Q(lower) and b == 0
            else:
                assert sign((a-Q(lower), b)) > 0 and sign((Q(upper)-a, -b)) > 0
        for tail, lower in zip(row['tails'], tail_lowers[i], strict=True):
            assert Q(lower) < Q(**tail['probability']) < Q(lower)+Q(1, 10**6)
        assert Q(signed_lowers[i]) < Q(**row['C301_signed_ratio_B_over_nC']) < Q(signed_lowers[i])+Q(1, 10**6)


def reconstruct():
    assert ROOT_LO**2 < 13 < ROOT_HI**2
    assert checked.H == 48 and checked.CAP == 100000 and checked.LIMIT == 256
    universe = checked.allowed_states()
    outgoing_set = checked.reachable(universe, checked.next_original)
    incoming_set = checked.reachable(universe, checked.previous_original)
    states = sorted(outgoing_set & incoming_set)
    indices = {a: j for j, a in enumerate(states)}
    incoming, outgoing = [], []
    for a in states:
        incoming.append([(indices[p], 2 if d == 0 else 1) for d in (-1, 0, 1)
                         if (p := checked.previous_original(a, d)) in indices])
        outgoing.append([(indices[p], 2 if d == 0 else 1) for d in (-1, 0, 1)
                         if (p := checked.next_original(a, d)) in indices])
    assert (len(incoming_set), len(states), sum(map(len, outgoing))) == (68211, 65893, 114445)
    zero = indices[checked.ZERO]
    forward = [int(j == zero) for j in range(len(states))]
    backward = forward.copy()
    midpoint_data = {}
    for time in range(1, 129):
        forward = [sum(forward[j]*w for j, w in row) for row in incoming]
        backward = [sum(backward[j]*w for j, w in row) for row in outgoing]
        assert forward[zero] == backward[zero]
        if time in TIMES:
            midpoint_data[time] = (forward.copy(), backward.copy())
    marks = [checked.norm_mark(a) for a in states]
    reals = [real_mark(a) for a in states]
    rows, boundary_counts = [], []
    expected_p = {32: Q(504250923, 2**57), 64: Q(121338835637214357477, 2**121),
                  128: Q(241348810511898190541699791270635467354265589, 2**253),
                  256: Q(264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231, 2**504)}
    for n, (forward, backward) in midpoint_data.items():
        weighted = [(j, x*y) for j, (x, y) in enumerate(zip(forward, backward)) if x*y]
        total = sum(w for _, w in weighted)
        assert Q(total, 4**(2*n)) == expected_p[2*n]
        first = [0, 0]
        fourth = [0, 0]
        signed_integer = 0
        real_sum = [Q(0), Q(0)]
        distribution = {}
        for j, weight in weighted:
            a = states[j]
            reverse = reverse_state(a)
            assert reverse_state(reverse) == a
            assert reverse in indices and forward[indices[reverse]] == backward[j]
            mark = marks[j]
            assert sign(mark) >= 0
            assert reals[j][1] == -mark[1]
            assert reals[j][0] == (Q(mark[0], 2), Q(-mark[1], 2))
            signed_integer += weight*reals[j][1]
            for k in (0, 1):
                real_sum[k] += weight*reals[j][0][k]
                first[k] += weight*mark[k]
                fourth[k] += weight*checked.field_mul(mark, mark)[k]
            distribution[mark] = distribution.get(mark, 0)+weight
        mean = tuple(Q(x, 2*n*total) for x in first)
        square_mean = checked.field_mul(mean, mean)
        fourth_mean = tuple(Q(x, 4*n*n*total) for x in fourth)
        assert sign(tuple(fourth_mean[k]-square_mean[k] for k in (0, 1))) >= 0
        real_mean = tuple(v/total for v in real_sum)
        assert real_mean == (Q(first[0], 2*total), Q(-first[1], 2*total))
        assert mean == (real_mean[0]/n, real_mean[1]/n-Q(signed_integer, n*total))
        bound = Q(430500, 130321)
        assert sign((bound-real_mean[0], -real_mean[1])) > 0
        assert sign((bound+real_mean[0], real_mean[1])) > 0
        tails, equalities = [], []
        for threshold in THRESHOLDS:
            selected = [(j, w) for j, w in weighted
                        if sign((Q(marks[j][0], 2*n)-threshold, Q(marks[j][1], 2*n))) >= 0]
            equals = [(j, w) for j, w in weighted
                      if sign((Q(marks[j][0], 2*n)-threshold, Q(marks[j][1], 2*n))) == 0]
            mass = sum(w for _, w in selected)
            contribution = tuple(Q(sum(w*marks[j][k] for j, w in selected), 2*n*total) for k in (0, 1))
            if threshold in (Q(1), Q(2)):
                fraction = Q(1, 10) if threshold == 1 else Q(3, 1000)
                assert sign(tuple(fraction*mean[k]-contribution[k] for k in (0, 1))) > 0
            if threshold == Q(1, 10) and n in (64, 128):
                assert 2*mass > total
            tails.append({'threshold': checked.ratio(threshold), 'comparison': '>=',
                          'integer_weight': mass, 'positive_states': len(selected),
                          'probability': checked.ratio(Q(mass, total)),
                          'probability_enclosure': envelope((Q(mass, total), Q(0))),
                          'scaled_second_moment_on_tail': envelope(contribution)})
            equalities.append({'threshold': checked.ratio(threshold), 'positive_states': len(equals),
                               'integer_weight': sum(w for _, w in equals)})
        assert all(tails[i]['integer_weight'] >= tails[i+1]['integer_weight'] for i in range(5))
        order = sorted(distribution, key=cmp_to_key(lambda a, b: sign((a[0]-b[0], a[1]-b[1]))))
        assert all(sign((b[0]-a[0], b[1]-a[1])) > 0 for a, b in zip(order, order[1:]))
        quantiles = []
        for probability in (Q(1, 2), Q(9, 10)):
            before = 0
            for mark in order:
                after = before+distribution[mark]
                if Q(after, total) >= probability:
                    assert Q(before, total) < probability
                    quantiles.append({'probability': checked.ratio(probability),
                                      'scaled_squared_radius': envelope(tuple(Q(v, 2*n) for v in mark)),
                                      'mass_strictly_below': checked.ratio(Q(before, total)),
                                      'mass_at_or_below': checked.ratio(Q(after, total))})
                    break
                before = after
        rows.append({'midpoint_time': n, 'total_time': 2*n, 'complete_bridge_integer_weight': total,
                     'positive_midpoint_states': len(weighted), 'distinct_radial_marks': len(distribution),
                     'scaled_second_moment': envelope(mean), 'scaled_fourth_moment': envelope(fourth_mean),
                     'fourth_integer_A_sum': fourth[0], 'fourth_integer_B_sum': fourth[1],
                     'C301_signed_ratio_B_over_nC': checked.ratio(Q(signed_integer, n*total)),
                     'C301_real_product_mean': envelope(real_mean),
                     'tail_at_1_contributes_less_than_one_tenth_of_second_moment': True,
                     'tail_at_2_contributes_less_than_three_thousandths_of_second_moment': True,
                     'tails': tails, 'quantiles': quantiles})
        boundary_counts.append({'midpoint_time': n, 'threshold_equalities': equalities})
    return {'scope': {'height': 48, 'max_total_time': 256, 'state_cap': 100000, 'midpoint_times': list(TIMES)},
            'midpoints': rows, 'threshold_boundary_counts': boundary_counts}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author-input', type=Path, default=checked.OUTPUT/'midpoint_profile.json')
    parser.add_argument('--output', type=Path, default=checked.OUTPUT/'reviewer_profile_result.json')
    args = parser.parse_args()
    result = reconstruct()
    check_statement_tables(result['midpoints'])
    author = json.loads(args.author_input.read_text(encoding='utf-8'))
    assert author['scope'] == {'polynomial_coefficients_ascending': [1, -1, -1, -1, 1],
                              'original_digit_weights': [1, 2, 1], 'digit_denominator': 4,
                              'midpoint_times': list(TIMES), 'max_total_time': 256,
                              'complete_height': 48, 'state_cap': 100000,
                              'tail_thresholds': [checked.ratio(t) for t in THRESHOLDS]}
    assert result['midpoints'] == author['midpoints']
    result['comparison'] = 'Exact full midpoint-profile payload agreement, with independently retained threshold equality masses and original reciprocal-fiber checks.'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    temporary.replace(args.output)
    print(json.dumps({'comparison': result['comparison'], 'fixed_statement_tables_checked': True,
                      'threshold_equality_state_counts': [[t['positive_states'] for t in row['threshold_equalities']]
                                                         for row in result['threshold_boundary_counts']]}, indent=2))


if __name__ == '__main__':
    main()
