"""Test endpoint norm divisibility for both signs of every admissible short power."""

from collections import Counter

from pole_catalogue import pole_value, table_rows


def root_power_sums(coefficients, limit):
    degree = len(coefficients) - 1
    terms = [(j, c) for j, c in enumerate(coefficients) if j and c]
    powers = [degree]
    for k in range(1, limit + 1):
        total = k * coefficients[k] if k <= degree else 0
        for j, c in terms:
            if j >= k:
                break
            total += c * powers[k-j]
        powers.append(-total)
    return powers


def powered_polynomial(powers, u, degree):
    first_half = [1]
    for j in range(1, degree//2 + 1):
        numerator = -sum(first_half[j-k] * powers[k*u] for k in range(1, j+1))
        coefficient, remainder = divmod(numerator, j)
        if remainder:
            raise ArithmeticError("Newton coefficient is nonintegral")
        first_half.append(coefficient)
    return tuple(first_half + first_half[-2::-1])


def main():
    counts = Counter()
    for line, degree, _, _, original in table_rows():
        if degree > 44:
            continue
        counts["rows"] += 1
        limit = max(2*degree-1, (18*degree-1)//7)
        powers = root_power_sums(original, (degree//2)*limit)
        for u in range(1, limit+1):
            polynomial = powered_polynomial(powers, u, degree)
            if u == 1 and polynomial != original:
                raise ArithmeticError(f"Source reconstruction failed at line {line}")
            counts["powers"] += 1
            first_q = 5 if u < 2*degree else 7
            last_q = (18*degree-1)//u
            for sign in (1, -1):
                coeff = tuple(c * sign**j for j, c in enumerate(polynomial))
                endpoint = abs(sum((-1)**j * c for j, c in enumerate(coeff)))
                if not endpoint:
                    raise ArithmeticError(f"Torsion root at line {line}")
                linear = degree + coeff[1]
                for q in range(first_q, last_q+1):
                    group = "5-6" if q <= 6 else "7-11" if q <= 11 else "12+"
                    counts[group, "tuples"] += 1
                    modulus = q*(q+1)
                    if modulus > endpoint+1 and linear % modulus:
                        continue
                    counts[group, "evaluations"] += 1
                    pole = pole_value(coeff, q)
                    if not pole:
                        raise ArithmeticError(f"Rational nonunit root at line {line}")
                    if endpoint % pole == 0:
                        counts[group, "hits"] += 1
                        print(f"HIT {line=} {degree=} {u=} {sign=} {q=} {pole=} {endpoint=}",
                              flush=True)
    if counts["rows"] != 944:
        raise ArithmeticError(f"Expected 944 rows, read {counts['rows']}")
    print(f"rows={counts['rows']} powers={counts['powers']}")
    for group in ("5-6", "7-11", "12+"):
        print(f"q={group} signed tuples={counts[group, 'tuples']} "
              f"pole evaluations={counts[group, 'evaluations']} hits={counts[group, 'hits']}")


if __name__ == "__main__":
    main()
