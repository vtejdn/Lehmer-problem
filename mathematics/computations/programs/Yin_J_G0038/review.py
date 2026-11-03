"""Independent fixed-seed certificate reconstruction for D45/J37.

Binary sign parity reconstructs the coefficients without importing author code.
All root decisions use fresh 320-bit rigorous Arb balls; the underlying FLINT
root-isolation library is shared with the author and is not independently proved.
"""

from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import hashlib
import json
import time
import flint
from flint import acb_poly, arb, ctx, fmpz_poly

HERE = (_J_PROGRAM / 'review.py').parent
AUTHOR = (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0037')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

started = time.monotonic()
author_hashes = {name:digest((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0037' if name == 'certificate.json' else AUTHOR) / name) for name in ["certify.py","certificate.json","readme.md"]}
saved = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0037/certificate.json')).read_text(encoding="utf-8"))

def binary_pair(j):
    p = [(-1)**((n & (n >> 1)).bit_count()) for n in range(2**j)]
    q = [v*(-1 if n>=2**(j-1) else 1) for n,v in enumerate(p)] if j else [1]
    return p,q

levels = []
previous_p,previous_q = binary_pair(0)
for j in range(1,7):
    p,q = binary_pair(j)
    assert p==previous_p+previous_q
    assert q==previous_p+[-a for a in previous_q]
    for lag in range(len(p)):
        autocorrelation = sum(p[n]*p[n+lag]+q[n]*q[n+lag] for n in range(len(p)-lag))
        assert autocorrelation == (2**(j+1) if lag==0 else 0)
    levels.append({"level":j,"terms":2**j,"paired_squared_norm":2**(j+1)})
    previous_p,previous_q=p,q

coefficients = [p[-1]*a for a in p]
assert coefficients==saved["coefficients_ascending"]
assert levels==saved["levels"]
assert coefficients[-1]==1 and len(coefficients)==64
assert all(abs(a)==1 for a in coefficients)
poly=fmpz_poly(coefficients)
assert poly.degree()==63
assert poly.gcd(poly.derivative()).degree()==0

ctx.prec=320
roots=acb_poly(coefficients).roots(tol=arb(2)**-180,maxprec=1024)
assert len(roots)==63
assert all(not roots[i].overlaps(roots[j]) for i in range(63) for j in range(i))
outside,inside=[],[]
root_data=[]
for root in roots:
    modulus=abs(root)
    if modulus>1:
        outside.append(modulus)
        side="outside"
    else:
        assert modulus<1
        inside.append(modulus)
        side="inside"
    # Evaluation containment is a supplementary consistency check;
    # isolation/completeness is supplied by acb_poly.roots, not this alone.
    assert acb_poly(coefficients)(root).contains(0)
    root_data.append({"real":root.real.str(70),"imag":root.imag.str(70),
                      "modulus":modulus.str(70),"classification":side})
assert len(outside)==31 and len(inside)==32
measure=arb(1)
for modulus in outside:measure*=modulus
assert measure>arb(137)/20
assert measure**3>128
assert saved["outside_count"]==31 and saved["unit_comparison_undecided"]==0

supremum=2*128**2+1
ratio=Fraction(2*(3*supremum**2+2*supremum),1)/Fraction(34,5)**12
assert supremum==32769
assert ratio<Fraction(2,3)
assert str(ratio)==saved["four_copy_phase_exp_upper_ratio"]
# Rational comparisons behind the stated elementary pi<4 error estimates.
assert Fraction(8,1100)<Fraction(1,137)
assert Fraction(8,320)==Fraction(1,40)<Fraction(4,137)
assert Fraction(34,5)**3>128
D4=64**4-1
cutoff4=320*D4*(D4+1)

assert author_hashes=={name:digest((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0037' if name == 'certificate.json' else AUTHOR) / name) for name in author_hashes}
result={'working_precision_bits': 320, 'maximum_isolation_precision_bits': 1024, 'all_assertions_passed': True, 'degree': 63, 'binary_parity_coefficients_equal_author': True, 'six_exact_paired_norm_identities': levels, 'squarefree_exact': True, 'root_balls_complete_and_pairwise_disjoint': True, 'outside_count': len(outside), 'inside_count': len(inside), 'mahler_enclosure': measure.str(70), 'mahler_exceeds': '137/20', 'four_copy_phase_exp_upper_ratio': str(ratio), 'four_copy_ratio_less_than_two_thirds': True, 'effective_error_rational_comparisons_passed': True, 'four_copy_D': D4, 'four_copy_n_cutoff': cutoff4, 'root_balls': root_data, 'author_files': list(author_hashes), 'scope': 'Independently written one-seed reconstruction and stronger-precision rerun sharing FLINT/Arb. No high-degree specialization expanded, no source proof of FLINT or formal verification.'}
((_J_OUTPUT / 'review.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("PASS degree",63,"outside",len(outside),"inside",len(inside),"Mahler",measure.str(30))
print("four-copy cutoff",cutoff4,"author artifacts preserved")
