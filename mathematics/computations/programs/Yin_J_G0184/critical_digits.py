"""Compute critical Teichmueller congruences over prime fields, without rounding."""
import sympy as sp

u, v, inverse = sp.symbols('u v inverse')
a = (u**2 - 3*u - 1) * (u**2 - 4*u - 1)
a_star = (1 - 3*u - u**2) * (1 - 4*u - u**2)
f = sp.Poly(a*v**2 + u**2*v + a_star, u, v, domain=sp.ZZ)


def first_digit(p):
    frobenius = sp.Poly.from_dict({(p*i, p*j): c for (i, j), c in f.terms()},
                                  (u, v), domain=sp.ZZ)
    difference = frobenius - f**p
    return difference.exquo_ground(p).set_modulus(p).as_expr()


def check_support(p, slope, basis, digit, derivative):
    survivors = {
        (3, (1, 0)): (u**2 + 1, -u),
        (13, (1, 0)): (u**2 + 1, 2*u - 6),
        (19, (1, 1)): (u**2 - 5*u + 1, 7*u + 7),
        (19, (1, 18)): (u**2 + 5*u + 1, 7*u + 4),
    }
    expected = (u**2 - 1, 1) if p == 5 else survivors.get((p, slope))
    if expected is None:
        assert list(basis) == [1], (p, slope, basis)
        return
    q, g = expected
    exponent = 16 if p == 5 else 1
    for relation in (q, v-g):
        assert basis.reduce(sp.expand(relation**exponent))[1] == 0
    modulus = sp.Poly(q, u, modulus=p)
    image = sp.Poly(g, u, modulus=p)
    assert modulus.is_sqf and modulus.gcd(image * sp.Poly(u, u, modulus=p)).degree() == 0
    for equation in (f.as_expr(), digit, derivative):
        # Horner reduction keeps high powers of g small during substitution.
        value = sp.Poly(0, u, modulus=p)
        for coefficient in sp.Poly(equation, v).all_coeffs():
            value = (image*value + sp.Poly(coefficient, u, modulus=p)) % modulus
        assert value.is_zero
    if p == 19:
        power = 2 if slope == (1, 1) else 8
        assert modulus.is_irreducible
        assert ((image**power - sp.Poly(u, u, modulus=p)) % modulus).is_zero
        assert ((image**20 - 1) % modulus).is_zero
        for proper_power in (4, 10):
            assert not ((image**proper_power - 1) % modulus).is_zero


def solve(p):
    digit = first_digit(p)
    equation = f.as_expr()
    for k, ell in [(0, 1)] + [(1, ell) for ell in range(p)]:
        derivative = k*u*equation.diff(u) + ell*v*equation.diff(v)
        # The inverse variable cuts out the torus before reducing the digit.
        critical = sp.groebner([inverse*u*v - 1, equation, derivative],
                               inverse, v, u, modulus=p, order='lex')
        remainder = critical.reduce(digit)[1]
        basis = sp.groebner([*critical, remainder], inverse, v, u,
                            modulus=p, order='lex')
        check_support(p, (k, ell), basis, digit, derivative)
        print(p, (k, ell), list(basis), flush=True)


if __name__ == '__main__':
    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        solve(prime)
