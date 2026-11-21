"""Classify unit factors through primitive degree 44 at short exponent one."""

from flint import fmpz_poly

from witnesses import SALEM, X


def first_excluded_v(q):
    p = q + 1
    bound = (3*p - q) * (p + q)**43
    v = 2
    while 13**v <= bound * 10**v:
        v += 1
    return v


def main():
    for q in (2, 3):
        stop = first_excluded_v(q)
        parents = 0
        hits = []
        for v in range(2, stop):
            for sign in (-1, 1):
                parent = q*(1 + sign*X**(v+1)) - (q+1)*(X + sign*X**v)
                content, factors = parent.factor()
                reconstructed = fmpz_poly([content])
                for f, multiplicity in factors:
                    reconstructed *= f**multiplicity
                    if (f.degree() <= 44 and f.leading_coefficient() == 1
                            and abs(f[0]) == 1 and not f.is_cyclotomic()):
                        hit = (q, v, sign, f, multiplicity)
                        print("HIT", hit, flush=True)
                        hits.append(hit)
                if reconstructed != parent:
                    raise ArithmeticError(f"Factor reconstruction failed at {(q,v,sign)}")
                parents += 1
        expected = [(2, 13, 1, SALEM, 1)] if q == 2 else []
        if hits != expected:
            raise ArithmeticError(f"Unexpected factors at height {q}: {hits}")
        print(f"q={q}  2<=v<{stop}  {parents} normalized parents  {len(hits)} hits",
              flush=True)


if __name__ == "__main__":
    main()
