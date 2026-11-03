"""Whole J80 review: binary autocorrelation and endpoint/row-Gram energies.

No author imports. The mathematical domain and 180-second cap are declared in
readme.md before this first run. Exclusive report creation preserves failures.
"""
from collections import Counter
from itertools import product
from math import gcd, lcm, isfinite
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import gzip
import json
import re
import time
import traceback
import sympy as sp

HERE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 180
DOMAINS = [('quartic', [1, -1, -1, -1, 1], b) for b in (7, 8, 9, 10)]
DOMAINS += [('lehmer', [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1], 12)]
LEAVES = 0


# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def same(actual, expected, where):
    global LEAVES
    assert type(actual) is type(expected), (where, type(actual), type(expected))
    if type(expected) is dict:
        assert actual.keys() == expected.keys(), (where, actual.keys(), expected.keys())
        for key in expected:
            same(actual[key], expected[key], where + '.' + key)
    elif type(expected) is list:
        assert len(actual) == len(expected), (where, len(actual), len(expected))
        for i, (a, e) in enumerate(zip(actual, expected)):
            same(a, e, where + '[' + str(i) + ']')
    else:
        assert actual == expected, (where, actual, expected)
        LEAVES += 1


def integers(matrix):
    return [[int(x) for x in row] for row in matrix.tolist()]


def rationals(matrix):
    return [[[int(x.p), int(x.q)] for x in row] for row in matrix.tolist()]


def load_author_result(path):
    data = json.loads(path.read_bytes())
    assert type(data) is dict and data.get('complete') is True, 'Author execution has no complete terminal result'
    pass
    return data


def main():
    start = time.perf_counter()
    output = (_J_OUTPUT / 'review_result.json')
    assert not output.exists(), 'Preserve the first reviewer report; do not overwrite'
    completed = []
    report = {'schema': 'J80-complete-independent-review-v1', 'domains': completed, 'complete': False}

    def cap():
        assert time.perf_counter() - start <= CAP, 'Declared aggregate reviewer cap exceeded'

    native = [(_J_PROGRAM / 'profile.py'), (_J_OUTPUT / 'result.json')]
    native += [_J_OUTPUT / f'{name}_b{b}.json.gz' for name, p, b in DOMAINS]
    before = {path: path.read_bytes() for path in native}
    draft = (_J_ROOT / 'mathematics/drafts/Yin_D_G0190.md')
    draft_before = draft.read_bytes() if draft.exists() else None
    try:
        data = load_author_result((_J_OUTPUT / 'result.json'))
        assert type(data) is dict
        assert set(data) == {'schema', 'domains', 'total_raw_words', 'total_endpoints', 'complete', 'all_passed'}
        same(data['schema'], 'J80-original-profile-v1', 'schema')
        pass
        assert type(data['domains']) is list and len(data['domains']) == len(DOMAINS)
        symbol = sp.Symbol('t')
        for index, (name, coefficients, b) in enumerate(DOMAINS):
            cap()
            d = len(coefficients) - 1
            k = b - d
            polynomial = sp.Poly.from_list(list(reversed(coefficients)), symbol, domain=sp.ZZ)
            cols = []
            for j in range(b):
                remainder = sp.rem(sp.Poly(symbol ** j, symbol, domain=sp.ZZ), polynomial)
                cols.append([int(remainder.nth(i)) for i in range(d)])
            X = sp.Matrix(cols).T
            Q = X * X.T
            Qi = Q.inv(method='DM')
            relation = sp.zeros(b, k)
            for j in range(k):
                shifted = sp.Poly(symbol ** j * polynomial.as_expr(), symbol, domain=sp.ZZ)
                for i in range(b):
                    relation[i, j] = shifted.nth(i)
            G = relation.T * relation
            Gi = G.inv(method='DM')
            assert X.rank() == d and relation.rank() == k and X * relation == sp.zeros(d, k)
            assert sp.eye(b) - relation * Gi * relation.T == X.T * Qi * X
            qden = lcm(*(int(x.q) for x in Qi))
            qint = [[int(x * qden) for x in row] for row in Qi.tolist()]
            energy_terms = [(i, j, qint[i][j] * (1 if i == j else 2))
                            for i in range(d) for j in range(i, d) if qint[i][j]]

            # Direct binary word enumeration, then ALL ordered-pair differences.
            binary = Counter()
            for word in product((0, 1), repeat=b):
                endpoint = tuple(sum(word[j] * cols[j][i] for j in range(b)) for i in range(d))
                binary[endpoint] += 1
            assert sum(binary.values()) == 2 ** b
            points = list(binary.items())
            zero = (0,) * d
            counts = {zero: sum(c * c for c in binary.values())}
            pair_visits = 0
            for i, (x, cx) in enumerate(points):
                if i % 64 == 0:
                    cap()
                for j in range(i):
                    y, cy = points[j]
                    z = tuple(x[h] - y[h] for h in range(d))
                    opposite = tuple(-v for v in z)
                    weight = cx * cy
                    counts[z] = counts.get(z, 0) + weight
                    counts[opposite] = counts.get(opposite, 0) + weight
                    pair_visits += 1
            assert pair_visits == len(points) * (len(points) - 1) // 2
            c0 = counts[zero]
            assert sum(counts.values()) == 4 ** b
            assert all(counts[tuple(-v for v in z)] == c for z, c in counts.items())
            payload_name = f'{name}_b{b}.json.gz'
            rows = json.loads(gzip.decompress(before[_J_OUTPUT / payload_name]))
            assert type(rows) is list and len(rows) == len(counts)
            maxima = {}
            max_witnesses = {}
            failures = []
            equalities = []
            previous = None
            for row_index, row in enumerate(rows):
                if row_index % 4096 == 0:
                    cap()
                assert type(row) is list and len(row) == 5
                zlist, c, numerator, denominator, passed = row
                assert type(zlist) is list and len(zlist) == d
                assert all(type(v) is int for v in zlist)
                z = tuple(zlist)
                assert previous is None or previous < z
                previous = z
                expected_count = counts.pop(z)
                n = sum(coefficient * z[i] * z[j] for i, j, coefficient in energy_terms)
                divisor = gcd(n, qden)
                A, B = n // divisor, qden // divisor
                assert 0 <= A <= b * B
                left, right = pow(expected_count, B) << A, pow(c0, B)
                success = left <= right
                same(row, [list(z), expected_count, A, B, success], payload_name + ':' + str(row_index))
                if left == right:
                    equalities.append(list(z))
                if not success:
                    failures.append([list(z), expected_count, A, B])
                if c not in maxima or A * maxima[c][1] > maxima[c][0] * B:
                    maxima[c] = (A, B)
                    max_witnesses[c] = list(z)
            assert not counts
            assert equalities == [list(zero)]
            item = data['domains'][index]
            assert type(item) is dict
            certificates = item['count_energy_certificate']
            assert type(certificates) is list and len(certificates) == len(maxima)
            for cert_index, (certificate, count) in enumerate(zip(certificates, sorted(maxima))):
                assert type(certificate) is dict
                assert set(certificate) == {'count', 'energy', 'endpoint', 'word', 'left', 'right', 'passed'}
                word = certificate['word']
                assert type(word) is list and len(word) == b
                assert all(type(v) is int and v in (-1, 0, 1) for v in word)
                z = tuple(sum(word[j] * cols[j][i] for j in range(b)) for i in range(d))
                # Count witness independently by binary autocorrelation at this endpoint.
                witness_count = sum(cx * binary.get(tuple(x[h] - z[h] for h in range(d)), 0)
                                    for x, cx in points)
                n = sum(coefficient * z[i] * z[j] for i, j, coefficient in energy_terms)
                divisor = gcd(n, qden)
                A, B = n // divisor, qden // divisor
                assert witness_count == count and (A, B) == maxima[count]
                left, right = pow(count, B) << A, pow(c0, B)
                expected_cert = {'count': count, 'energy': [A, B], 'endpoint': list(z), 'word': word,
                                 'left': left, 'right': right, 'passed': left <= right}
                same(certificate, expected_cert, f'domain{index}.certificate{cert_index}')
            expected = {'name': name, 'polynomial': coefficients, 'degree': d, 'window': b,
                        'rank': d, 'nullity': k, 'raw_words': 3 ** b, 'columns': cols,
                        'Q': integers(Q), 'Q_inverse': rationals(Qi), 'relations': integers(relation),
                        'relation_gram': integers(G), 'relation_gram_inverse': rationals(Gi),
                        'projection_identity': True, 'normalization': 4 ** b, 'denominator': 4 ** b,
                        'endpoint_count': len(rows), 'zero_count': c0, 'symmetry': True,
                        'equality_count': len(equalities), 'failures': failures, 'all_passed': not failures,
                        'count_energy_certificate': certificates, 'payload': payload_name,
                        'payload_schema': ['endpoint', 'count', 'energy_numerator', 'energy_denominator', 'passed']}
            same(item, expected, 'domain' + str(index))
            done = {'name': name, 'polynomial': coefficients, 'window': b, 'binary_words': 2 ** b, 'binary_endpoints': len(binary), 'unordered_binary_endpoint_pairs': pair_visits, 'raw_ternary_words': 3 ** b, 'payload_rows': len(rows), 'count_energy_classes': len(maxima), 'zero_count': c0, 'equality_endpoints': equalities, 'failure_count': len(failures), 'all_native_mathematical_fields_and_types_match': True}
            completed.append(done)
            print(json.dumps(done), flush=True)
        same(data['total_raw_words'], sum(x['raw_ternary_words'] for x in completed), 'total_raw_words')
        same(data['total_endpoints'], sum(x['payload_rows'] for x in completed), 'total_endpoints')
        same(data['complete'], True, 'complete')
        same(data['all_passed'], all(x['failure_count'] == 0 for x in completed), 'all_passed')
        assert sum(x['payload_rows'] for x in completed) == 489937
        assert sum(x['count_energy_classes'] for x in completed) == 605
        assert sum(x['raw_ternary_words'] for x in completed) == 618921
        assert all(path.read_bytes() == content for path, content in before.items())
        assert draft_before is None or draft.read_bytes() == draft_before
        cap()
        report.update({'complete': True, 'all_mathematical_checks_passed': True, 'total_payload_rows': 489937, 'total_count_energy_classes': 605, 'total_raw_ternary_words': 618921, 'strict_scalar_comparisons': LEAVES})
    except Exception as error:
        report.update({'error_type': type(error).__name__, 'error': _record_text(str(error)),
                       'traceback': _record_text(traceback.format_exc()), 'strict_scalar_comparisons': LEAVES})
        raise
    finally:
        pass
        with output.open('x', encoding='utf-8') as handle:
            json.dump(report, handle, indent=2)
        print(json.dumps({'complete': report['complete'], 'report': output.name}), flush=True)


if __name__ == '__main__':
    main()
