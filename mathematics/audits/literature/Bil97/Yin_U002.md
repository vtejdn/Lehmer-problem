---
author: Yin
---
# Bil97-U002: fixed finite sums of small points with nontorsion pair ratios

Date: 2026-10-18T12:33.
Human record author Yin.
Root proposed the torsion-character-block argument for a fixed finite sum and its zero-output, fixed-output and Salem-monomial consequences.
The entropy_attainment_bridge AI supplies the reuse comparison and complete statement/applicability checks below.
Both are contributors to this application; the earlier R537 review covers U001 only and is not an independent review of this new unit.
This is a direct consequence of the accepted torus Bogomolov theorem, not a new small-point theorem or a claim of priority.
No numerical scan, new Claim or original source-proof audit is performed.

<a id="bil97-u002"></a>
## Read; accepted source and author-checked finite-sum application

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Yuri Bilu, Limit distribution of small points on algebraic tori, Duke Mathematical Journal89(3) (1997), 465--476; same retained Bil97--published.pdf as U001, with printed465 at PDF1.

Passages: Printed465/PDF1 for the absolute projective tuple-height convention; printed474--475/PDF10--11 for the complete Theorem5.1, the torsion-subvariety convention and its Qbar scope.

Inspection: The assigned author directly text-read and visually inspected these passages during the preceding source/application review and reuses their exact accepted statements here. The present weaker pairwise hypothesis, character blocks, zero/fixed-output cases, height bound and own-degree consequence are newly author-checked. No original Bilu, Zhang or Bombieri--Zannier proof audit.


The exact external input and definitions are retained in [U001's Theorem5.1 account](Yin_U001.md#torus-bogomolov-complement), .
For any fixed Zariski-closed X in G_m^N over Qbar, let X* remove all torsion subvarieties contained in X, including zero-dimensional ones.
If X* is nonempty, Theorem5.1 gives

    eta_X=inf_(z in X*) H_N(z)>0,
    max_i h_abs(z_i)<=H_N(z)<=sum_i h_abs(z_i).       (1)

The constant depends on the fixed variety and ambient dimension; no effective value or uniformity over varying varieties is used.
The theorem applies to varieties defined over Qbar, which is essential for a fixed algebraic output below.
No Bilu strictness or joint multiplicative independence of the input tuple is assumed in this application.

### Reuse boundary

The accepted [ESS02 nondegenerate-equation statement](../ESS02/Yin_U001.md#ess-exact-counting-bound) counts nondegenerate solutions inside a fixed finite-rank multiplicative tuple group.
The [AV09 located improvement](../AV09/Yin_U001.md#av09-located-count) remains unaccepted at its recorded original-page access boundary.
Neither count is needed here, and neither is silently converted into the present degree-uniform height assertion.
Pairwise nontorsion ratios are not the same hypothesis as the absence of every vanishing proper subsum.
No fixed finite-rank group or subsum-nondegeneracy assumption is imposed below.
The already inspected exact Theorem5.1 is sufficient, so no further literature acquisition or search is needed for this consequence.

### Fixed finite-sum statement

Fix an integer k>=2 and nonzero rational numbers c_1,...,c_k.
Call a tuple z=(z_1,...,z_k) admissible when each z_i is a nonzero algebraic number and z_i/z_j is not a root of unity whenever i!=j.
Put

    y(z)=sum_(i=1)^k c_i z_i.

There are constants delta_c>0 and b_c>0, depending only on this fixed k and coefficient vector, such that EVERY admissible tuple with max_i h_abs(z_i)<=delta_c satisfies

    y(z)!=0 and h_abs(y(z))>=b_c.                    (2)

More precisely, for EVERY sequence of admissible tuples z_n with max_i h_abs(z_(n,i)) tending to zero, the outputs y_n are eventually nonzero and satisfy

    liminf_n h_abs(y_n)>0,
    [Q(y_n):Q] tends to infinity,
    m_own(y_n)=[Q(y_n):Q] h_abs(y_n)
        tends to infinity.                          (3)

The last two assertions refer to the eventual nonzero tail.
The inputs may have arbitrary joint multiplicative dependencies and varying generated groups.
No input or output integrality, fixed field degree or bounded multiplicative rank is required.

### 1. Character blocks on a torsion translate

Let T=zeta H be a torsion translate of a subtorus contained in some ambient coordinate torus.
Restriction of the first k coordinate functions to T has the form

    Z_i|_T=zeta_i chi_i,

where zeta_i is a root of unity and chi_i is a character of H.
If T contains a point whose first k coordinates are admissible, then the chi_i are pairwise distinct.
Indeed chi_i=chi_j would make Z_i/Z_j identically the root of unity zeta_i/zeta_j on T, contrary to that point's admissibility.
Distinct characters of a torus are linearly independent in its Laurent coordinate ring.
This includes the trivial character; for a zero-dimensional subtorus all characters are trivial, which already precludes such an admissible point when k>=2.

Consider first the fixed graph hypersurface

    X_+= {(Z_1,...,Z_k,Y) in G_m^(k+1):
              sum_i c_i Z_i-Y=0}.

If a torsion translate T inside X_+ contained an admissible-base point, its additional coordinate would restrict as Y=zeta_0 chi_0.
The characters chi_i are pairwise distinct, so chi_0 can coincide with at most one of them.
Since k>=2, at least one input character remains a singleton in the restricted linear equation, with nonzero coefficient c_i zeta_i.
Linear independence of characters makes that impossible.
Consequently every valid nonzero-output graph point with admissible input belongs to X_+*.

For the zero-output hypersurface

    X_0={Z in G_m^k:sum_i c_i Z_i=0},

the same restriction has only the k distinct input characters.
Each is a singleton with nonzero coefficient, so no contained torsion translate can contain an admissible point.
Thus every admissible zero-output tuple belongs to X_0*.

Finally fix ANY a in Qbar^* and put

    X_a={Z in G_m^k:sum_i c_i Z_i=a}.

The constant term -a is attached to the trivial character.
At most one of the pairwise distinct chi_i can be trivial; since k>=2, some other chi_i is an unmatched singleton with nonzero coefficient.
No torsion translate inside X_a can therefore contain an admissible point.
Every admitted point on X_a belongs to X_a*.
This uses no rationality assumption on a and no Galois-stability or strictness assertion about the input sequence.

### 2. Zero exclusion and a uniform output-height floor

The complement X_+* is nonempty.
To see this without a numerical choice, take z_i=q^i for an integer q>=2 outside the finite zero set of the nonzero polynomial sum_i c_i Q^i.
All pairwise ratios q^(i-j) are nontorsion and y!=0, so Section1 puts this point in X_+*.
Let eta_+>0 be its Theorem5.1 height infimum.

If X_0* is nonempty let eta_0>0 be its height infimum; if it is empty set eta_0=1 for the following harmless choice of constants.
In the empty case there are no admissible zero-output points at all.
Put

    delta_c=min(eta_0,eta_+)/(2k),
    b_c=eta_+/2.

If max_i h_abs(z_i)<=delta_c and y=0, Section1 and(1) would give

    eta_0<=H_k(z)<=sum_i h_abs(z_i)<=k delta_c
            <=eta_0/2,

unless X_0* is empty, when the point was already impossible.
Hence y!=0.
The graph point now lies in X_+*, and

    eta_+<=H_(k+1)(z,y)
             <=sum_i h_abs(z_i)+h_abs(y).

This proves(2), with no omitted finite-place or coefficient contribution.
For a sequence as in(3), the zero-output condition is eventually excluded and the same inequality gives the sharper liminf h_abs(y_n)>=eta_+.

### 3. Fixed algebraic outputs, bounded height and actual own degree

For each fixed a in Qbar^*, infinitely many outputs y_n=a would give an infinite sequence of admissible points in X_a* with H_k(z_n) tending to zero.
If X_a* is empty there are no such points; otherwise Theorem5.1 gives a positive infimum and contradicts that sequence.
Thus every fixed nonzero algebraic output occurs only finitely often.
The eventual exclusion of a=0 was already proved separately.

The output heights are bounded above as well.
Choose a positive integer B and nonzero integers b_i with c_i=b_i/B, and set C=max(B,sum_i|b_i|)>=1.
The archimedean triangle inequality and the finite-place ultrametric inequality for these integer coefficients give

    h_abs(y_n)<=log C+sum_i h_abs(z_(n,i)).           (4)

This is the same elementary fixed-rational-function height bound retained in U001; it never required independent inputs.
Equivalently use projective height of(sum_i b_i z_i:B) and the product formula.
Thus the fixed rational coefficient denominators remain included, and outputs need not be integral.

Suppose output own degrees were bounded on an infinite subsequence.
Together with(4), the elementary coefficient finiteness argument from [U001](Yin_U001.md#fixed-function-own-degree-divergence) leaves only finitely many algebraic output values: for degree n<=D and height h<=H, each primitive minimal-polynomial coefficient is bounded by 2^D exp(DH).
One output a would repeat infinitely often, contradicting the preceding fixed-fiber argument.
This proves own degree TENDING TO INFINITY, not merely unbounded degree.
Combining it with the positive lower limit of height proves the own total-measure divergence in(3).
The equality m_own(y)=deg(y)h_abs(y) includes the primitive leading coefficient when y is not integral; no input degree is substituted.

<a id="salem-varying-monomial-terms"></a>
### Salem monomial terms with varying supports and exponents

Let alpha_n be genuine Salem numbers of degree d_n and original total logarithmic measure m_n.
For each n choose one oriented representative u_(n,j) from every inverse pair.
Fix only the number k>=2 of summands and the nonzero rational coefficients c_i.
Allow integer exponent vectors v_(n,1),...,v_(n,k) to vary with n, including their supports, and assume these vectors are pairwise distinct after combining inverse-pair exponents.
Let

    z_(n,i)=product_j u_(n,j)^(v_(n,i,j)),
    A_(n,i)=sum_j |v_(n,i,j)|.

The accepted [C_G165 theorem](../../../claims/Yin_C_G0165_v1.md#decision-whole-reviewed-2026-10-18) and its classical independence proof give

    z_(n,i)/z_(n,l) is nontorsion for i!=l,
    h_abs(z_(n,i))=A_(n,i) m_n/d_n.                  (5)

A zero exponent vector gives z=1 and height zero; at most one such vector occurs because the vectors are distinct.
Arbitrary torsion prefactors may also be absorbed in the z_(n,i): height is unchanged and distinct exponent vectors still make every pairwise ratio nontorsion by independence modulo roots of unity.
This does not replace or weaken the actual ratio hypothesis in the general statement.

Whenever

    max_i A_(n,i) m_n/d_n tends to zero,              (6)

the outputs sum_i c_i z_(n,i) satisfy every conclusion in(3).
Neither the support sizes nor individual exponents must remain fixed; the ambient dimension of Theorem5.1 is k or k+1, the FIXED number of terms.
The single-term monomial height formula, not C165's separate all-support total-measure lower bound, is what is used in(5).
No normal-trace-field, small-prime or subdegree premise is added.

### Exact limits and role

The hypothesis k>=2 is essential: a single small-height term need not have an output-height floor or diverging total measure.
Pairwise nontorsion ratios are also essential; equal or opposite terms can cancel identically when their ratio is a root of unity.
The condition does not assert joint multiplicative independence and does not require nonvanishing of every proper subsum at arbitrary heights.
It is precisely what excludes the relevant torsion-character blocks.

The number of terms and rational coefficients remain fixed.
No effective numerical constants, convergence rate, growing-term-count bound or uniformity in moving coefficients is obtained.
Condition(6) is explicit; unbounded original degree or variable supports alone do not imply it.
Coincident exponent vectors must first be accounted for, and no assertion is made for a collection whose remaining pairwise ratios are torsion.
The result concerns the output's own measure, not a gap for the original Salem measure or an estimate for a different norm or projection object.

The complete source consequence is author-checked and ready for separate review if adopted by a consumer.
The accepted source Theorem5.1 and U001/R537 inspection boundary remain unchanged; R537 does not cover this newly weakened-input application.
