---
author: Yin
---

# Positive-factor counts in the Lehmer three-block delay family

## Question and scope

This computation tests A_N(z)=P_L(z)(z^(2N)+1)+z^(N+5), where P_L=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1.
Its only assigned inputs are N=1,2,3,4,5,6,10,12,15,20,24,30.
The question is whether actual positive-measure irreducible factor counts show growth relevant to the [L450 bounded-total-measure bridge](../../../ledger/Yin_L_G0450_v1.md#positive-factor-counterexample-bridge).
The count r_+ includes multiplicities within each A_N.
Different factors appearing at different N do not establish growth of that count, and a gap for the whole polynomial does not price its smallest positive factor.
The external_structural_lead delegate prepares this ordinary author computation for Yin, without independent review.

## Method and reproduction

The retained native program is [main.py](main.py).
Both of the following commands were run successfully from the repository root.

```
python mathematics/computations/programs/Yin_J_G0140/main.py --phase small
python mathematics/computations/programs/Yin_J_G0140/main.py --phase remaining
```

The first command uses N=1,2,3,4,5,6,10,12,15 and writes [small_results.json](../../outputs/Yin_J_G0140/small_results.json).
The second uses N=20,24,30 and writes [remaining_results.json](../../outputs/Yin_J_G0140/remaining_results.json).
Each command generates its inputs directly and requires no previous output.
Both outputs are replaceable and retain the complete original integer coefficient arrays, all irreducible factor coefficient arrays and multiplicities, exact cyclotomic classification, degree totals, r_+, numerical roots and measure sums.
An optional `--phase all` runs exactly the union of these assigned inputs and writes all_results.json; that optional combined command was not run for this record.
The completed two-phase calculation used Python 3.14.3, SymPy 1.14.0 and NumPy 2.4.4, and each output records actual runtime versions.
There is no randomness or external data input.

Input construction and factorization use SymPy polynomials over ZZ.
For each input, the program checks monicity, constant coefficient one and degree 2N+10 before calling factor_list.
The returned complete factorization is multiplied back exactly and checked against that input, and cyclotomic plus positive-factor degrees with multiplicity are checked against its degree.
Every irreducible factor is monic with constant coefficient 1 or -1.
SymPy's exact is_cyclotomic predicate separates zero-measure factors; every remaining irreducible unit factor has positive measure by the accepted [Kronecker characterization](../../../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
Neither irreducibility nor cyclotomic classification is inferred from floating-point roots.

For each factor NumPy computes all roots in double precision and the program sums log(max(1,abs(root))) over every computed root.
There is no exterior threshold in this measure sum.
The separate modulus threshold 1+1e-7 supplies only an optional numerical exterior-root count.
The total measure estimate adds the positive-factor measures with their multiplicities; known exact-zero cyclotomic factors contribute zero.
A separate raw root sum including their floating-point roundoff is retained in the output for comparison.
The minimum is over the actual positive-measure irreducible factors of that input, without division by degree or multiplicity.
These root calculations and all decimal measures have no certified error intervals or certified numerical root counts.

## Completed finite result

All twelve assigned inputs completed full factorization over Z; none is partial or timed out.
Every returned irreducible factor has multiplicity one in this finite set.
The total and minimum columns below are uncertified numerical root sums; the degree and r_+ columns come from exact factorization.

| N | Degree | Cyclotomic degree | Positive-factor degrees | r_+ | Approximate total m | Approximate minimum positive-factor m |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 12 | 2 | 5,5 | 2 | 0.5997885550 | 0.2998942775 |
| 2 | 14 | 0 | 14 | 1 | 0.5312195122 | 0.5312195122 |
| 3 | 16 | 0 | 16 | 1 | 0.4575644371 | 0.4575644371 |
| 4 | 18 | 0 | 18 | 1 | 0.6823528355 | 0.6823528355 |
| 5 | 20 | 2 | 18 | 1 | 0.6188628996 | 0.6188628996 |
| 6 | 22 | 0 | 22 | 1 | 0.2066616330 | 0.2066616330 |
| 10 | 30 | 0 | 30 | 1 | 0.6462887752 | 0.6462887752 |
| 12 | 34 | 0 | 34 | 1 | 0.4949560891 | 0.4949560891 |
| 15 | 40 | 0 | 40 | 1 | 0.5558955142 | 0.5558955142 |
| 20 | 50 | 0 | 50 | 1 | 0.5179961822 | 0.5179961822 |
| 24 | 58 | 0 | 58 | 1 | 0.5506202793 | 0.5506202793 |
| 30 | 70 | 0 | 70 | 1 | 0.4756520170 | 0.4756520170 |

Only N=1 has more than one positive-measure factor in this finite set.
Its exact factorization is A_1=(z^2-z+1)(z^5+z^4-z^2-z-1)(z^5+z^4+z^3-z-1).
The two degree-five factors are negatives of each other's reversals, so their full measures agree exactly; the displayed decimals approximate that common value.
The only cyclotomic factor at N=5 is also z^2-z+1, with multiplicity one.
The native outputs retain both degree-five factors and their separate full root sums, along with every other factor's exact coefficients and multiplicity.
The finite data do not show positive-factor proliferation within A_N.
They establish no bound on r_+ for untested N, no asymptotic irreducibility theorem and no positive-to-zero sequence.
Any separate whole-polynomial measure bound still leaves the L450 bridge's unbounded within-input r_+ requirement to be supplied independently.

## Inspection and limits

The author delegate inspected the generated scope, all factor degree and multiplicity classifications, the finite measures and the exact reconstruction checks.
The retained program performed no parameter beyond the twelve listed N and no interval root isolation.
This is a finite exact algebra calculation combined with exploratory numerical root measures, not independent review of a general factor-count or Mahler-measure theorem.
