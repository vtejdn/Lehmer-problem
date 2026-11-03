"""Four declared controls; exact Laurent moments and rational intervals only."""

from fractions import Fraction as F
from math import factorial
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sys

BITS = 100
LOG_TERMS = 128
DEPTH = 64
EPSILON = F(1, 4)
CASES = {
    "cyclotomic_linear": [-1, 1],
    "cyclotomic_quadratic": [1, 1, 1],
    "positive_reciprocal_quadratic": [1, -3, 1],
    "lehmer_degree_ten": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}


# Public metadata uses logical locators; actual subprocess/file paths stay resolved.
def _record_path(value):
    try:
        return Path(value).resolve().relative_to(_J_ROOT).as_posix()
    except ValueError:
        return '<external-location>'


def _record_command(values):
    result = []
    for value in values:
        option, separator, argument = value.partition('=')
        if separator and option.startswith('-') and Path(argument).is_absolute():
            result.append(option + '=' + _record_path(argument))
        else:
            result.append('python' if value == sys.executable else
                          _record_path(value) if Path(value).is_absolute() else value)
    return result


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return {k: v for k, v in out.items() if v}


def moments(p, h):
    b = mul(dict(enumerate(p)), {-i: a for i, a in enumerate(p)})
    v = add(scale(b, 2), {0: -h * h})
    older, current = {0: 1}, v
    out = [F(1)]
    for k in range(1, DEPTH + 1):
        bound = h ** (2 * k)
        assert all(isinstance(a, int) and abs(a) <= bound for a in current.values())
        out.append(F(current.get(0, 0), bound))
        older, current = current, add(scale(mul(v, current), 2), scale(older, -h**4))

    # Independent explicit binomial formula for T_k, substituted into s=2B/H^2-1.
    s = scale(v, F(1, h * h))
    powers = [{0: F(1)}]
    for _ in range(8):
        powers.append(mul(powers[-1], s))
    for k in range(1, 9):
        exact = F(0)
        for j in range(k // 2 + 1):
            c = F((-1)**j * k * factorial(k - j - 1) * 2**(k - 2 * j),
                  2 * factorial(j) * factorial(k - 2 * j))
            exact += c * powers[k - 2 * j].get(0, 0)
        assert exact == out[k], (k, exact, out[k])
    return out


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def ineg(a):
    return -a[1], -a[0]


def isub(a, b):
    return iadd(a, ineg(b))


def imul(a, b):
    vals = [x * y for x in a for y in b]
    return min(vals), max(vals)


def idiv(a, b):
    assert b[0] > 0
    return imul(a, (1 / b[1], 1 / b[0]))


def point(x):
    return F(x), F(x)


def root_point(x, n):
    assert x >= 0 and n >= 1
    if not x:
        return point(0)
    denom = 2**BITS
    lo = 0
    hi = max(denom, ((x.numerator + x.denominator - 1) // x.denominator) * denom)
    target = x.numerator * denom**n
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**n * x.denominator <= target:
            lo = mid
        else:
            hi = mid
    assert lo**n * x.denominator <= target <= hi**n * x.denominator
    return F(lo, denom), F(hi, denom)


def iroot(x, n):
    return root_point(x[0], n)[0], root_point(x[1], n)[1]


def unit_log(x):
    assert 1 <= x <= 2
    t = (x - 1) / (x + 1)
    power = t
    total = F(0)
    for j in range(LOG_TERMS):
        total += 2 * power / (2 * j + 1)
        power *= t * t
    tail = 2 * power / ((2 * LOG_TERMS + 1) * (1 - t * t))
    return total, total + tail


LN2 = unit_log(F(2))


def log_point(x):
    assert x > 0
    exponent = 0
    while x > 2:
        x /= 2
        exponent += 1
    while x < 1:
        x *= 2
        exponent -= 1
    return iadd(unit_log(x), imul(point(exponent), LN2))


def ilog(x):
    return log_point(x[0])[0], log_point(x[1])[1]


def outward(x):
    scale10 = 10**18
    lo = (x[0] * scale10).numerator // (x[0] * scale10).denominator
    hi = -((-x[1] * scale10).numerator // (-x[1] * scale10).denominator)
    assert F(lo, scale10) <= x[0] <= x[1] <= F(hi, scale10)
    return {"lower_numerator": lo, "upper_numerator": hi, "denominator": scale10}


def certificate(p, mu, h):
    eps = point(EPSILON)
    t = iroot(point(F(h * h) + EPSILON**2), 2)
    rho = idiv(isub(t, eps), iadd(t, eps))
    assert 0 < rho[0] <= rho[1] < 1
    series = ilog(idiv(iadd(t, eps), point(2)))
    power = point(1)
    for k in range(1, DEPTH + 1):
        power = imul(power, rho)
        series = iadd(series, imul(power, point(F((-1)**(k + 1), k) * mu[k])))
    tail = idiv(imul(power, rho), imul(point(DEPTH + 1), isub(point(1), rho)))
    d = len(p) - 1
    u = iroot(eps, d)
    half_u = idiv(u, point(2))
    error = imul(point(d), ilog(iadd(half_u, iroot(iadd(point(1), imul(half_u, half_u)), 2))))
    lower = isub(isub(series, tail), error)
    return series, tail, error, lower


def main():
    records = {}
    for name, p in CASES.items():
        h = sum(abs(a) for a in p)
        mu = moments(p, h)
        series, tail, error, lower = certificate(p, mu, h)
        status = "generic_error_cost_vacuous"
        if name.startswith("cyclotomic"):
            assert lower[1] < 0
            assert isub(series, tail)[0] <= error[1]
            status = "zero_measure_direction_passed"
        if name == "positive_reciprocal_quadratic":
            exact_measure = ilog(idiv(iadd(point(3), iroot(point(5), 2)), point(2)))
            assert 0 < lower[0] < lower[1] < exact_measure[0]
            assert exact_measure[1] < ilog(point(3))[0]
            status = "strict_positive_lower_certificate_passed"
        if name == "lehmer_degree_ten":
            assert lower[1] < 0
        records[name] = {
            "coefficients_ascending": p,
            "degree": len(p) - 1,
            "coefficient_l1": h,
            "moments": [{"numerator": x.numerator, "denominator": x.denominator} for x in mu],
            "regularized_series": outward(series),
            "chebyshev_tail": outward(tail),
            "global_root_error": outward(error),
            "mahler_lower_certificate": outward(lower),
            "status": status,
        }
    output = {'arithmetic': 'exact integers and Fraction; outward rational algebraic/log intervals', 'scope': {'epsilon': '1/4', 'depth': DEPTH, 'algebraic_bits': BITS, 'log_terms': LOG_TERMS, 'independent_binomial_moment_depth': 8, 'case_count': 4}, 'cases': records, 'result': 'all declared finite checks passed'}
    path = (_J_OUTPUT / 'data.json')
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": _record_path(path), "result": output["result"],
                      "certificates": {k: v["mahler_lower_certificate"] for k, v in records.items()}}, indent=2))


if __name__ == "__main__":
    main()
