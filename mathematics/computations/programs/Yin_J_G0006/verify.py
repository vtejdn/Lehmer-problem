"""Independent exact check through Newton power sums, without main.py/SymPy.

Original sparse-polynomial traces are computed by a rolling integer recurrence.
Subtract the explicitly verified cyclotomic factors, sample powers divisible by
2**s, and reconstruct the root-squared polynomial by Newton identities. This
checks the entire retained final Graeffe coefficient array and strict inequality.
No floating root estimate or factor-list irreducibility claim is certified here.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction
import json
import math

HERE = _J_OUTPUT
SOURCE = json.loads((HERE / 'result.json').read_text(encoding='utf-8'))
CHECKS = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def polynomial(g):
    a = [0] * (6*g + 1)
    for j in range(7):
        a[g*j] += (-1)**j
    a[2*g+1] -= 1
    a[4*g-1] -= 1
    return a


def ramanujan(m, k):
    # Only the two observed cyclotomic orders are accepted in this certificate.
    if m == 6:
        return (2, 1, -1, -2, -1, 1)[k % 6]
    if m == 12:
        return (4, 0, 2, 0, -2, 0, -4, 0, -2, 0, 2, 0)[k % 12]
    raise AssertionError(('unsupported cyclotomic order', m))


def selected_power_sums(a, wanted):
    degree = len(a)-1
    lower = [(i, a[degree-i]) for i in range(1, degree+1) if a[degree-i]]
    ring = [0] * (degree+1)
    saved = {}
    for k in range(1, max(wanted)+1):
        if k <= degree:
            value = -sum(coef * ring[(k-i) % len(ring)]
                         for i, coef in lower if i < k)
            value -= k * a[degree-k]
        else:
            value = -sum(coef * ring[(k-i) % len(ring)] for i, coef in lower)
        ring[k % len(ring)] = value
        if k in wanted:
            saved[k] = value
    return saved


def reconstruct(degree, power, sums, removed):
    traces = [0]
    for i in range(1, degree+1):
        traces.append(sums[i*power] - sum(mult*ramanujan(m, i*power)
                                             for m, mult in removed))
    descending = [1]
    for k in range(1, degree+1):
        numerator = -sum(descending[k-i] * traces[i] for i in range(1, k+1))
        quotient, remainder = divmod(numerator, k)
        if remainder:
            raise AssertionError(('Newton integrality', degree, power, k))
        descending.append(quotient)
    return descending[::-1]


def verify_certificate(label, polynomial_coeffs, cert, sums, removed):
    degree = len(polynomial_coeffs)-1
    s = cert['iteration']
    power = 2**s
    check(label + ': exact target and dimensions',
          cert['status'] == 'strict_lower_certified'
          and cert['degree'] == degree
          and cert['comparison_exponent'] == power
          and (cert['target_numerator'], cert['target_denominator']) == (4, 3))
    final = reconstruct(degree, power, sums, removed)
    check(label + ': full Newton reconstruction',
          final == [int(x) for x in cert['graeffe_coefficients_ascending']])
    k = cert['coefficient_index']
    coefficient = abs(final[k])
    divisor = math.comb(degree, k)
    check(label + ': coefficient and binomial',
          coefficient == int(cert['absolute_coefficient'])
          and divisor == int(cert['binomial_divisor']))
    left, right = coefficient * 3**power, divisor * 4**power
    check(label + ': complete strict integer inequality',
          left == int(cert['left_integer']) and right == int(cert['right_integer'])
          and left > right)
    return {'label': label, 'degree': degree, 'iteration': s,
            'power_sum_max_index': degree*power,
            'full_final_coefficients_match': True,
            'strict_mahler_lower_bound': [4, 3]}


def one_case(g, data):
    prefix = f'g={g}'
    r = polynomial(g)
    check(prefix + ': original r', r == data['r_coefficients_ascending'])
    q = [0] * (7*g+1)
    q[0] = q[-1] = 1
    for n in (2*g+1, 5*g-1, 3*g+1, 4*g-1):
        q[n] -= 1
    cyclo_block = [1] + [0]*(g-1) + [1]
    check(prefix + ': displayed q identity',
          multiply(r, cyclo_block) == q == data['q_coefficients_ascending'])
    product = [1]
    neutral = []
    nonneutral = []
    for index, item in enumerate(data['factors']):
        a = item['coefficients_ascending']
        check(prefix + f': factor {index} dimension',
              len(a)-1 == item['degree'] and a[-1] == 1 and a[0] == 1)
        for _ in range(item['multiplicity']):
            product = multiply(product, a)
        if item['cyclotomic_order'] is None:
            nonneutral.append((index, item))
        else:
            m = item['cyclotomic_order']
            expected = {6: [1,-1,1], 12: [1,0,-1,0,1]}
            check(prefix + f': explicit Phi_{m}', m in expected and a == expected[m])
            neutral.append((m, item['multiplicity']))
    check(prefix + ': full exact factor product', product == r)
    check(prefix + ': single reported noncyclotomic factor',
          len(nonneutral) == 1 and nonneutral[0][1]['multiplicity'] == 1)
    index, item = nonneutral[0]
    jobs = [(prefix + ': noncyclotomic quotient', item['coefficients_ascending'],
             item['mahler_lower_certificate'], neutral)]
    if 'whole_mahler_lower_certificate' in data:
        jobs.append((prefix + ': whole polynomial', r,
                     data['whole_mahler_lower_certificate'], []))
    else:
        check(prefix + ': whole certificate alias',
              data['whole_mahler_lower_certificate_same_as_factor_index'] == index
              and r == item['coefficients_ascending'])
    wanted = set()
    for _, a, cert, _ in jobs:
        power = 2**cert['iteration']
        wanted.update(i*power for i in range(1, len(a)))
    sums = selected_power_sums(r, wanted)
    return [verify_certificate(label, a, cert, sums, removed)
            for label, a, cert, removed in jobs]


def main():
    check('exact planned parameter set', set(SOURCE['parameters']) == {'3','4','5','8','16','32'})
    results = []
    for g in (3,4,5,8,16,32):
        print(f'Newton verification g={g}', flush=True)
        results.extend(one_case(g, SOURCE['parameters'][str(g)]))
    check('4/3 above plastic root', Fraction(4,3)**3-Fraction(4,3)-1 == Fraction(1,27))
    # Four-interval analytic limit certificate, independently exact arithmetic.
    check('radical interval rational product',
          3**129 * 7**4 * 17**5 * 59**10 > 2**239 * 5**24)
    output = {              'algorithm': 'integer sparse Newton traces with rolling buffer; cyclotomic trace subtraction; Newton coefficient reconstruction',
              'checks_passed': len(CHECKS), 'checks': CHECKS, 'certificates': results,
              'limits': 'No numerical root enclosures or independent factor irreducibility certification. Earlier first-success iteration probes are not independently checked; every final certificate and its full polynomial are.'}
    (HERE/'verification.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'checks_passed': len(CHECKS), 'certificates': len(results)}), flush=True)


if __name__ == '__main__':
    main()
