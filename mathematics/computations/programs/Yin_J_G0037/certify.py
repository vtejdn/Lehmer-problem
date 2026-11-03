"""One 64-term recursive seed; rigorous root-ball Mahler lower certificate."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction
import json
import time
import flint
from flint import acb_poly, arb, ctx, fmpz_poly

HERE = (_J_PROGRAM / 'certify.py').parent


def main():
    started = time.monotonic()
    p, q = [1], [1]
    levels = []
    for j in range(6):
        p, q = p + q, p + [-c for c in q]
        assert len(p) == len(q) == 2**(j+1)
        assert set(p) <= {-1, 1} and set(q) <= {-1, 1}
        # Laurent autocorrelation identity on the circle.
        n = len(p)
        for shift in range(n):
            val = sum(p[i]*p[i+shift]+q[i]*q[i+shift]
                      for i in range(n-shift))
            assert val == (2*n if shift == 0 else 0)
        levels.append({'level': j+1, 'terms': n, 'paired_squared_norm': 2*n})
    if p[-1] == -1:
        p = [-c for c in p]
    polynomial = fmpz_poly(p)
    assert polynomial.gcd(polynomial.derivative()).degree() == 0
    ctx.prec = 192
    roots = acb_poly(p).roots(tol=arb(2)**-100, maxprec=768)
    assert len(roots) == 63
    assert all(not roots[i].overlaps(roots[j])
               for i in range(63) for j in range(i))
    lower_product = arb(1)
    outside = 0
    undecided = 0
    root_data = []
    for z in roots:
        radius = abs(z)
        if radius > 1:
            lower_product *= radius
            outside += 1
            tag = 'strictly outside'
        elif radius < 1:
            tag = 'strictly inside'
        else:
            undecided += 1
            tag = 'unit-circle comparison undecided; omitted from lower product'
        root_data.append({'real': z.real.str(45), 'imag': z.imag.str(45),
                          'modulus': radius.str(45), 'use': tag})
    assert lower_product**3 > 128
    assert lower_product > arb(137)/20
    f_sup = 2*128**2+1
    ratio = Fraction(2*(3*f_sup**2+2*f_sup),1)/Fraction(34,5)**12
    assert ratio < Fraction(2,3)
    result = {'precision_bits': 192, 'maxprec': 768, 'degree': 63, 'coefficients_ascending': p, 'levels': levels, 'exact_paired_norm_identity': True, 'squarefree_exact': True, 'all_roots_isolated_disjoint': True, 'outside_count': outside, 'unit_comparison_undecided': undecided, 'certified_outside_product': lower_product.str(45), 'certified_simple_lower_bound': '137/20', 'four_copy_f_sup_bound': f_sup, 'four_copy_phase_exp_upper_ratio': str(ratio), 'four_copy_ratio_less_than_two_thirds': True, 'required_comparison': 'M(h0)^3 > 128 = squared sup-norm bound', 'comparison_passed': True, 'roots': root_data, 'scope': 'One fixed recursive height-one seed. Outside root balls alone give the Mahler lower bound; no irreducibility or full-root-location claim is required.'}
    ((_J_OUTPUT / 'certificate.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('degree',63,'outside',outside,'undecided',undecided,
          'Mahler lower product',lower_product.str(20),flush=True)


if __name__ == '__main__':
    main()
