---
author: Yin
---

# Four moving-map pullbacks with g_n=z^n-z-1

## Question and scope

This ordinary author computation for Yin tests only n=5,7,9,13 in
\[
 F_n(z)=g_n(z)^{10}P_L\bigl(g_n^*(z)/g_n(z)\bigr),
 \qquad g_n(z)=z^n-z-1,
\]
where
\[
 P_L(z)=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1,
 \qquad g_n^*(z)=1-z^{n-1}-z^n.
\]
The map changes with n; this is not iteration of the fixed cubic map.
The n=3 input is exactly the first layer already retained in [J141](../Yin_J_G0141/readme.md) and was not recomputed here.
The finite question is growth of positive irreducible-factor count within each complete output, with all multiplicities included.
New factors appearing at different n do not by themselves constitute that growth.
The bottleneck-diagnosis delegate prepared and inspected this finite computation for Yin under the main research agent's construction assignment.
No n>13 or additional exponent was included.

## Construction and exact checks

For each assigned odd n, the exact endpoint data are
\[
 g_n(0)=-1,\quad g_n^*(0)=1,\quad
 g_n(1)=g_n^*(1)=-1,\quad
 g_n(-1)=-1,\quad g_n^*(-1)=1.
\]
Consequently the rational map has values -1 at zero and infinity, 1 at 1, and -1 at -1.
The identities P_L(1)=-1 and P_L(-1)=1 give actual degree 10n, leading and constant coefficients one, and
\[
 F_n(1)=-1,\qquad F_n(-1)=1.
\]
Reversal exchanges g_n and g_n*, and reciprocity of P_L preserves reciprocity of F_n.
The program verifies these exact coefficient and endpoint conclusions and gcd(g_n,g_n*)=1 separately at each of the four inputs.

The two reductions
\[
 \overline{g_n}=z^n+z+1,\qquad
 \overline{g_n^*}=z^n+z^{n-1}+1
\]
are distinct for these n.
Thus the sufficient condition g*=g modulo two used in the preceding parity test is not supplied by this construction.
This observation is not an exclusion of other possible arithmetic auxiliaries.
It also supplies no uniform comparison with the fixed-map constants in the earlier cubic iteration.

Construction uses homogeneous Horner evaluation over ZZ, retaining the complete integer coefficient list including all zeros.
SymPy factor_list computes the full irreducible factorization over ZZ.
The program checks content one, multiplies all returned factors with their multiplicities back to the original polynomial, and checks the complete degree sum.
Every factor is checked to be monic with unit constant coefficient.
Its exact is_cyclotomic predicate separates the zero-measure factors; every remaining irreducible unit factor is positive by the accepted [Kronecker characterization](../../../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
No exact factor classification is inferred from numerical roots.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Complete exact construction and factorization followed by 50-digit full-root diagnostics for exactly the four assigned inputs. |
| [exact_results.json](../../outputs/Yin_J_G0142/exact_results.json) | Complete input and factor coefficients, multiplicities, cyclotomic classifications, exact factor counts and reconstruction checks. |
| [results.json](../../outputs/Yin_J_G0142/results.json) | Completed numerical summary for the four inputs, with links by filename to their complete root data. |
| [roots_n5.json](../../outputs/Yin_J_G0142/roots_n5.json) | All 50 computed roots and individual log-plus contributions at n=5. |
| [roots_n7.json](../../outputs/Yin_J_G0142/roots_n7.json) | All 70 computed roots and individual log-plus contributions at n=7. |
| [roots_n9.json](../../outputs/Yin_J_G0142/roots_n9.json) | All 90 computed roots and individual log-plus contributions at n=9. |
| [roots_n13.json](../../outputs/Yin_J_G0142/roots_n13.json) | All 130 computed roots and individual log-plus contributions at n=13. |

Generated results are replaceable local outputs in this J's responsible output directory.
The retained program constructs every input directly and requires neither previous generated data nor external input files.

## Reproduction

The following command completed successfully from the repository root.

```
python mathematics/computations/programs/Yin_J_G0142/main.py
```

Its fixed INPUTS tuple is exactly (5,7,9,13).
All four exact factorizations finish before the numerical phase begins in the same process.
The exact output is published after the complete assigned algebra calculation, and each numerical root file is published atomically after its input finishes.
Numerical exceptions would be recorded without converting a failed root calculation into a completed one.
The actual process completed all four root calculations without a restart.
The output location is derived from the actual containing J directory and does not depend on the caller's working directory.

The completed run used Python 3.14.3, SymPy 1.14.0 and mpmath 1.3.0.
SymPy nroots used 50 decimal digits and maxsteps=200 for every exact factor.
Each computed root contributes log(max(1,abs(root))), with no exterior tolerance or cutoff.
The program retains every individual contribution, the complete root lists, scaled polynomial residuals and the logarithm of the product of root moduli.
Known cyclotomic factors would contribute exact zero to the classified total, with raw root sums retained separately; none occurred at these inputs.
No double-precision root calculation or extra-precision rerun was performed.
There is no randomness, interval root isolation or certified numerical error bound.

## Results and limits

All four inputs are themselves irreducible over Q, with multiplicity one, and none is cyclotomic.
Thus each actual output has exactly one positive-measure irreducible factor and cyclotomic degree zero.
The complete factor product and degree checks passed for all four inputs.

| n | Degree | Cyclotomic degree | Positive-factor degrees | r_+ with multiplicity | Uncertified total m |
| --- | --- | --- | --- | --- | --- |
| 5 | 50 | 0 | 50 | 1 | 3.1735647331415596752 |
| 7 | 70 | 0 | 70 | 1 | 2.8380213370923340423 |
| 9 | 90 | 0 | 90 | 1 | 2.8739251022335282849 |
| 13 | 130 | 0 | 130 | 1 | 2.8296021004963169533 |

Since each polynomial has one positive factor, its minimum positive-factor measure equals its total measure.
The exact maximum absolute coefficients are respectively 1058,1416,1699,1699.
The generated exact file retains every original and factor coefficient rather than only this summary.
The numerical solver returned the full degree-many root list at each input and reported no convergence failure.
The largest observed scaled polynomial residual was below 5.2 times 10^-50, and the absolute logarithmic root-product discrepancy was below 1.1 times 10^-49.
These diagnostics do not certify root accuracy or a numerical enclosure and are not used to establish factor counts or positivity.
No concrete numerical failure or discrepancy requiring an additional precision run was encountered in the assigned calculation.

There is no within-output growth of the positive-factor count in these four inputs.
The finite result does not prove irreducibility at other exponents, bounded factor count over the whole family, a measure limit, or an obstruction for all varying maps.
In particular, distinct factors found at different n do not supply the unbounded within-input count required by the factor-proliferation mechanism.
The n=3 result remains at its existing J141 home; no earlier computation or fixed-map theorem is silently promoted to a uniform statement for this moving family.

## Inspection summary

The author delegate read the actual native program and inspected all four exact factor classifications, multiplicities, degree totals and reconstruction checks.
The retained numerical root and contribution counts were checked to be 50,70,90,130 respectively, and the completed totals and diagnostic residuals were inspected.
This is an ordinary author computation, not an independent irreducibility certificate or formal review of a general theorem.
