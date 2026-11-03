---
author: Yin
---

# Exponential concentration: exact signed span, general-rank obstruction and power-orbit time

This retains the complete direct mathematics originally written on2026-10-07 in [L93](../ledger/Yin_L_G0093_v1.md).
The rejected NV11 use and actual theorem/erratum statement-reading evidence remain in [NV11-U001](../audits/literature/NV11/Yin_U001.md#nv11-u001).
Only fixed-parameter statements were screened; their proofs and the erratum proof were not audited or adopted.
The original checking account is retained in the formal review linked by L93.
No source, computation or Task is newly executed.

## Statement

For any finite indexed list v1,...,vn in an abelian group, let rho be the maximum atom of its independent fair-bit sum.
Every inclusion-maximal dissociated sublist D, of size k, satisfies rho<=2^(-k), and every weight is in its signed span with coefficients in{-1,0,1}.
Thus rho>=exp(-epsilon n) implies k<=epsilon n/log2, with no exceptions and progression cardinality at most3^k.
This progression may be improper.

For every epsilon>0 and every fixed exception fraction0<=delta<1, choose an integer L>=1 with log(1+L(L+1)/2)/L<=epsilon.
For every integer r>=1, the n=rL distinct nonzero weights j e_i in Z^r,1<=i<=r,1<=j<=L, have rho>=exp(-epsilon n).
Any retained sublist of at least(1-delta)n weights requires symmetric progression rank at least ceil((1-delta)r), and affine progression rank at least ceil((1-delta)r)-1.
A Q-independent real embedding preserves every fiber and the same bounds.
No one-dimensional integer, algebraic power-orbit or small-Mahler realization is asserted.

For every nonzero algebraic number alpha of degree d, the fair sum of its first n powers has rho_n=2^(-n) for n<=d and rho_n<=2^(-d) for n>=d.
For0<epsilon<log2, the condition rho_n>=exp(-epsilon n) is impossible at n<=d and requires n>=d log2/epsilon thereafter.
At a permissible time the generic signed-span budget epsilon n/log2 is already at least d.
These statements retain the distinction between fixed-C polynomial concentration, exponential concentration, generic weights and arithmetic power-orbit restrictions.
They give no uniform Mahler gap or input-independent inverse rank.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:42 |
| status | open |
| reason | Complete original direct arguments retained at their mathematical responsible home; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire indexed fair-sum signed-span theorem, distinct-nonzero general-weight rank controls and exact nonzero-algebraic power-orbit concentration/time boundary, including every exception, affine and embedding limitation. |
| argument | [Complete argument](#argument) | Complete original maximal-dissociation reuse, axis-product pigeonhole control, rational-dimension and real-fiber argument, and degree-conditioning/time proof with all failed-use and arithmetic boundaries. |
| dependency | [Existing dissociation proof](Yin_C_G0279_v1.md#dissociated-colors-and-cost) | Exact conditioning and maximal indexed dissociation signed-span arguments; no proper progression or below-degree orbit rank follows. |
| support | [Original source screen](../audits/literature/NV11/Yin_U001.md#nv11-u001) | Only retained NV11 Theorems2.1/2.5 statement/applicability reading and continuous-erratum scope, preserving fixed-C dependencies and no source-proof adoption. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:51 |
| status | proved |
| reason | Adopt the complete original signed-span, distinct-weight rank obstruction and algebraic-power time theorem after actual whole self-review; retain the NV11 fixed-parameter screen solely at its original statement/applicability scope and all arithmetic/uniformity limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire indexed fair-sum signed-span theorem, distinct-nonzero general-weight rank controls and exact nonzero-algebraic power-orbit concentration/time boundary, including every exception, affine and embedding limitation. |
| argument | [Argument](#argument) | Complete original maximal-dissociation reuse, axis-product pigeonhole control, rational-dimension and real-fiber argument, and degree-conditioning/time proof with all failed-use and arithmetic boundaries. |
| dependency | [Dependency](Yin_C_G0279_v1.md#dissociated-colors-and-cost) | Exact conditioning and maximal indexed dissociation signed-span arguments; no proper progression or below-degree orbit rank follows. |
| support | [Support](../audits/literature/NV11/Yin_U001.md#nv11-u001) | Only retained NV11 Theorems2.1/2.5 statement/applicability reading and continuous-erratum scope, preserving fixed-C dependencies and no source-proof adoption. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-exponential-concentration-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire indexed fair-sum signed-span theorem, distinct-nonzero general-weight rank controls and exact nonzero-algebraic power-orbit concentration/time boundary, including every exception, affine and embedding limitation. |
| argument | [Argument](#argument) | Complete original maximal-dissociation reuse, axis-product pigeonhole control, rational-dimension and real-fiber argument, and degree-conditioning/time proof with all failed-use and arithmetic boundaries. |
| dependency | [Dependency](Yin_C_G0279_v1.md#dissociated-colors-and-cost) | Exact conditioning and maximal indexed dissociation signed-span arguments; no proper progression or below-degree orbit rank follows. |
| support | [Support](../audits/literature/NV11/Yin_U001.md#nv11-u001) | Only retained NV11 Theorems2.1/2.5 statement/applicability reading and continuous-erratum scope, preserving fixed-C dependencies and no source-proof adoption. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0537_v1.md#current-exponential-concentration-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual fixed inputs and exact relationship scopes. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0545_v1.md#f-g287) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
<a id="elementary-exponential-signed-span"></a>
### The exact inverse statement already available by local reuse

For a finite indexed list v_1,...,v_n in an abelian group, let rho be the maximal atom of sum_i X_i v_i for independent fair bits.
Let D be any inclusion-maximal dissociated sublist, of size k.
The conditioning and maximality arguments already proved in [C G0280](Yin_C_G0279_v1.md#dissociated-colors-and-cost) and [its signed-span boundary](Yin_C_G0279_v1.md#embedding-and-rank-color-boundaries) give

    rho<=2^(-k),
    every v_i belongs to span_{-1,0,1}(D).

Thus the exact implication in the exponential range is

    rho>=exp(-epsilon n)
       => k<=epsilon n/log2,
          all weights lie in a signed progression of rank k. (1)

There are no exceptional weights in (1).
The progression need not be proper: dissociation only excludes relations with coefficients -1,0,1, whereas equality between two signed coefficient vectors can involve -2 or 2.
Its cardinality is at most 3^k.
This distinction prevents rebranding (1) as the proper bounded-rank progression of the screened source.

This is reuse of existing direct arguments, not a new theorem attributed to Li26 Section3.
The latter source's maximal-dissociated proof is compatible with it, but the current Li26 source unit deliberately audits Section2 only.
No source-audit scope is silently enlarged here.

<a id="generic-exponential-rank-obstruction"></a>
### A distinct-nonzero control excludes bounded-rank conclusions in this regime

Fix integers L>=1 and r>=1.
In the torsion-free group Z^r take the n=rL pairwise distinct nonzero weights

    v_(i,j)=j e_i,       1<=i<=r, 1<=j<=L,

where e_i is the standard basis.
Their fair sum is a product of r independent copies of W_L=sum_(j=1)^L j X_j.
Each W_L takes integer values in [0,L(L+1)/2].
By the pigeonhole principle its largest atom is at least 1/K_L, where

    K_L=1+L(L+1)/2.

Independence of the coordinates therefore gives

    rho>=K_L^(-r)=exp[-epsilon_L n],
    epsilon_L=log(K_L)/L ->0 as L->infinity.              (2)

The limit follows from K_L<= (L+1)^2 and log(L+1)/L->0.
Consequently, for each prescribed epsilon>0, fixing sufficiently large L makes (2) imply rho>=exp(-epsilon n) for every r.

Nevertheless, any retained sublist containing at least (1-delta)n weights, with 0<=delta<1, uses at least ceil((1-delta)r) distinct axes, because each axis contains only L of the original weights.
Choosing one retained nonzero vector from each used axis proves that the rational rank of the retained list is at least that number.
If it lies in a symmetric generalized arithmetic progression of rank R, its rational span has dimension at most R.
Hence

    R>=ceil((1-delta)r)=ceil((1-delta)n/L).                (3)

For an affine progression a_0+sum_(j=1)^R [-N_j,N_j]a_j, the corresponding bound is R>=ceil((1-delta)r)-1.
The same rational-dimension proof applies.
Properness cannot evade either bound.

This yields, for fixed epsilon and any fixed exception fraction delta<1, a sequence with exponentially large atoms but with the necessary progression rank growing linearly in n.
Sending the e_i to Q-linearly independent real numbers gives the same example with pairwise distinct nonzero real weights and exactly the same fibers; no integer-valued one-dimensional version is claimed.
The example rules out a rank bound depending only on epsilon and delta for general real or torsion-free-group weights.
It does not optimize the coefficient of n in (1), and does not assert that the constructed weights form an algebraic power orbit or arise from a small-Mahler unit.

<a id="power-orbit-inverse-time-cost"></a>
### The power orbit pays the missing time cost before inversion begins

Let alpha be any nonzero algebraic number of degree d over Q.
The first d powers 1,alpha,...,alpha^(d-1) are Q-linearly independent.
For n>=d, conditioning on all digits with j>=d makes the first d binary sums distinct and equiprobable.
Therefore

    rho_n<=2^(-d)                 (n>=d),
    rho_n=2^(-n)                  (n<=d).                 (4)

In particular, when 0<epsilon<log2, the hypothesis

    rho_n>=exp(-epsilon n)

is impossible for n<=d, and for n>=d it requires

    n>=d log2/epsilon.                                   (5)

At any permitted time, the upper bound epsilon n/log2 in (1) is already at least d.
Thus this general inverse rank bound cannot force the signed spanning set below the ambient field dimension.
This conclusion uses no unproved small-Mahler family, all-power degree claim or per-input entropy limit.

The same distinction prevents using a fixed-C polynomial-concentration theorem merely by choosing a time n=O(d): sufficiently small epsilon would violate the prerequisite (5).
Conversely, allowing the necessary n of order d/epsilon restores an O(epsilon n) budget of order d, and the generic rank argument is no contradiction.

All-power degree preservation and small Mahler measure might impose further arithmetic restrictions on which signed progressions can contain long orbit segments.
Neither (1), the screened fixed-C theorem nor generic entropy comparisons establish those restrictions.
A useful next inverse step would need such an additional power-orbit statement with explicit time, rank and exception costs.
Merely obtaining another O(epsilon n) signed-span bound would repeat the already available estimate.
