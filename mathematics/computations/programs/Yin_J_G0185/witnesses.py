"""Check the q=2 Salem factor and the bounded nonmonic-parent search."""

from math import gcd

from flint import fmpz_poly


X = fmpz_poly([0, 1])
SALEM = X**6 - X**5 - X**3 - X + 1
COFACTOR = 2 * X**8 - X**7 - X**6 + X**5 + X**3 - X**2 - X + 2


def search(q, first_v, last_v, max_u):
    count = 0
    found = []
    for v in range(first_v, last_v + 1):
        for u in range(1, min(v, max_u + 1)):
            if gcd(u, v) != 1:
                continue
            for b in (-(q + 1), q + 1):
                for sign in (-1, 1):
                    parent = q * (1 + sign * X**(u + v)) + b * (X**u + sign * X**v)
                    content, factors = parent.factor()
                    product = fmpz_poly([content])
                    for factor, multiplicity in factors:
                        product *= factor**multiplicity
                        if factor.leading_coefficient() == 1 and abs(factor[0]) == 1:
                            if not factor.is_cyclotomic():
                                found.append((u, v, b, sign, factor, multiplicity))
                    assert product == parent
                    count += 1
    print(f"q={q}, u<={max_u}, {first_v}<=v<={last_v}: {count} parents, {len(found)} hits")
    return found


def main():
    assert SALEM * COFACTOR == 2 * (1 + X**14) - 3 * (X + X**13)
    assert SALEM(1) == -1 and SALEM(2) == 23
    for q in range(2, 13):
        expected = [(1, 13, -3, 1, SALEM, 1), (1, 13, 3, 1, SALEM(-X), 1)] if q == 2 else []
        assert search(q, 2, 70, 6) == expected
    assert not search(3, 71, 190, 4)
    assert not search(4, 71, 160, 2)


if __name__ == "__main__":
    main()
