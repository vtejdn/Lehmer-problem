---
author: Yin
---

# G0001: what inverse concentration controls at exponential probability

The current complete mathematical proof is retained in [C286](../claims/Yin_C_G0286_v1.md#argument).
The original mathematical text below remains the fixed old input; current Claim adoption does not rewrite its old date or review bindings.

Date: 2026-10-07.
Bounded reuse, primary-source screening and direct scope checks by assigned AI ms25_source for Yin.
One source and its linked same-work erratum are retained solely for statement/quantifier screening; no new source theorem is adopted as a proof premise and no computation is used.
This assessment follows L G0088's dissociation boundaries and the new fair-binary entropy comparison, rather than claiming a new uniform gap.

<a id="exponential-inverse-concentration-screen"></a>
## The primary theorem screened

The original author PDF of Hoi Nguyen and Van Vu, *Optimal inverse Littlewood-Offord theorems*, was opened at [this primary locator](https://people.math.osu.edu/nguyen.1261/cikk/optimalILO-final.pdf).
For an integer multiset, Theorem2.1, internally p.6, assumes fair signs and concentration rho>=n^(-C), with C>0 and the exception fraction 0<delta<1 fixed constants.
It gives a proper symmetric generalized arithmetic progression of rank O_(C,delta)(1), covering all but delta n weights, and cardinality O_(C,delta)(rho^(-1)n^(-r/2)).
Theorem2.5, p.7, permits n^delta<=n'<=n exceptions, with size O_(C,delta)(rho^(-1)(n')^(-r/2)) and the same fixed-parameter rank convention.
These exact statements were read; their proofs were not audited.

The desired hypothesis rho>=exp(-epsilon n) corresponds formally to C=epsilon n/log n.
The displayed theorem supplies no uniform constant after that substitution: its rank and implicit constants depend on C, which now grows.
This is a scope failure of that proposed use, not a refutation of the source theorem or a claim that no other inverse theorem exists.
The [bounded source unit](../audits/literature/NV11/Yin_U001.md#nv11-exponential-screen) owns the exact retained version, statement inspection and linked erratum boundary.
The latter repairs a continuous corollary, not these discrete statements.
No source theorem is needed for the direct arguments below, and no second new work was selected.

<a id="elementary-exponential-signed-span"></a>
## The exact inverse statement already available by local reuse

For a finite indexed list v_1,...,v_n in an abelian group, let rho be the maximal atom of sum_i X_i v_i for independent fair bits.
Let D be any inclusion-maximal dissociated sublist, of size k.
The conditioning and maximality arguments already proved in [L G0088](Yin_L_G0088_v1.md#dissociated-colors-and-cost) and [its signed-span boundary](Yin_L_G0088_v1.md#embedding-and-rank-color-boundaries) give

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
## A distinct-nonzero control excludes bounded-rank conclusions in this regime

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
## The power orbit pays the missing time cost before inversion begins

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

## Original actual checks and stopping boundary

The complete original drafting, direct-review, primary-statement visual-reading and search-stopping account is retained in [R537](../audits/reviews/Yin_R_G0537_v1.md#complete-original-l93-checking-account).
Its exact original inputs, verdicts and source-proof limits remain unchanged; current finding-specific relationships are recorded there.
