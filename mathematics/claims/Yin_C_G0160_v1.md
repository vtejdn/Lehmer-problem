---
author: Yin
---
# Uniform original-degree projection costs in the fixed Perron-seed Salem family

Human author Yin.
The angular_envelope_review agent supplied the complete author proof developed in D41; root assigned the family question without contributing a proof step.
The fixed result includes the actual cyclotomic removal and original-degree normalization, not only the irreducible numerator progression.
The elementary inverse-power mechanism is attributed at the exact inspected DMS84 manuscript scope; its constants and local application are proved here.
No numerical program, matrix evaluation or parameter scan is used.
This registered candidate awaits independent whole review and adoption.

## Statement

Let n>=16 be an integer and set

    f(t)=t^3-t-1, q(t)=1-t^2-t^3,
    P_n(t)=t^n f(t)+q(t), D=n+3.

Let c_n be the product of precisely the cyclotomic factors in the following table, each with multiplicity one, and put p_n=P_n/c_n, c=deg c_n, d=D-c.

| Factor in c_n | Exact condition |
| --- | --- |
| Phi_2 | n=0 mod2 |
| Phi_8 | n=7 mod8 |
| Phi_12 | n=10 mod12 |
| Phi_18 | n=14 mod18 |
| Phi_30 | n=21 mod30 |

The accepted L38 family theorem supplies that p_n is the actual Salem minimal polynomial and c<=12.
In particular p_n is monic, irreducible, reciprocal and nontorsion, of its ORIGINAL degree d, and its total measure lies strictly between log theta and log(4/3), where theta is the real root greater than one of f.
These are reused family hypotheses and conclusions, not new assertions of irreducibility or measure decay.

Use the full M=2d coordinate window and let A_p be the M-by-d coefficient matrix of p_n,t p_n,...,t^(d-1)p_n.
Define

    R_p=I_M-A_p(A_p^t A_p)^(-1)A_p^t,
    a_h=sum_(j=0)^(M-1-h)(R_p)_(j,j+h),
    kappa=(2/d)sum_(h=1)^(M-1)|a_h|,
    v_M(t)=(1,t,...,t^(M-1))^t,
    k(t)=M^(-1)v_M(t^-1)^t R_p v_M(t),
    G_3(t)=log2-(1-k(t))/2-(1-k(t))^2/8-(1-k(t))^3/24.

The Laurent evaluation uses t^-1, with Hermitian interpretation only on the unit circle.
Put the numerical constants

    rho=1-1/36864,
    C0=(1/36)[1/(1-rho)+12rho/(1-rho)^2],
    K=36C0+24, W=(1+K)/2.

Then for every stated n,

    kappa_(2d)(p_n)<=36C0+2c<=K,
    sum_(h!=0)|G3hat(h)|<=W/2+W^2/8+W^3/24.          (S)

All Fourier coefficients use normalized unit-circle Haar measure, and the second sum contains both signed nonzero frequencies.
These constants are independent of n and the original degree d; no small or sharp constant is asserted.
The exact original p_n, all complete cyclotomic factors and the original window M=2d remain in the statement.
In the irreducible progression n=9 mod120, n>=129, c=0 and the first bound improves to 36C0.

The proof also establishes the following explicit finite intermediates.
For every complex polynomial X with deg X<=n+2,

    ||P_n X||_2^2 >= ||X||_2^2/1024,
    ||P_n X||_2 <=6||X||_2.

For every full coefficient Gram G of r consecutive shifts of P_n with 1<=r<=n+3, its spectrum lies in [1/1024,36] and every inverse row and column has absolute sum at most C0.
The actual original-window comparison uses r=D-2c=d-c>0 and pays the rank-c difference between the numerator and original-factor residual projections.

This is uniform coefficient control for one fixed positive-measure family.
It neither asserts a positive-gap sequence tending to zero, a bound over changing seeds or all Salem polynomials, a full-logarithm Wiener bound, nor an unrestricted Mahler gap.
The already accepted six-term short-annihilator restriction and L38's fixed positive limit continue to separate this family from a hypothetical total-measure-to-zero regime.

<a id="fixed-seed-scope"></a>
## Question, existing inputs and exact scope

Does the existing Perron-seed Salem family give unbounded actual N=2d projection coherence or unbounded cubic Fourier mass while its total Mahler measure remains below log(4/3)?
The existing [L38 family](../ledger/Yin_L_G0038_v1.md#excess-three-family), its [complete cyclotomic table](../ledger/Yin_L_G0038_v1.md#family-cyclotomic-factors), [L154 irreducible progression](../ledger/Yin_L_G0154_v1.md#salem-first-return-tail-control), [L326 degree-twenty control](../ledger/Yin_L_G0326_v1.md#h4-actual-counterexample) and [J79 actual family review](../computations/programs/Yin_J_G0079/readme.md#reciprocal-family-complete-independent-review) were read.
The relevant analytic interfaces are [L321's exact inverse-Gram identity](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity), [C92's short-annihilator theorem](Yin_C_G0092_v1.md#statement), [C143's large-measure obstruction](Yin_C_G0143_v1.md#statement), [C145's moving-logarithm expense](Yin_C_G0145_v1.md#kernel-finite-logarithm-expenses) and [C158's actual cubic](Yin_C_G0158_v1.md#statement).
The fixed L38 family and its cyclotomic table identify the fixed positive measure limit and, at n=18 with only Phi_2 removed, the same degree20 factor in L326 with measure below log(4/3).
Those facts are reused, not new results here.

Set

    f(t)=t^3-t-1, q(t)=1-t^2-t^3=t^3 f(t^-1),
    P_n(t)=t^n f(t)+q(t), D=n+3, n>=16,
    P_n=p_n c_n, c=deg c_n, d=deg p_n=D-c.

The accepted L38 statement supplies the actual Salem minimal polynomial p_n and the complete squarefree cyclotomic product c_n, with c<=12.
It also supplies theta<exp(m(p_n))<4/3, m(p_n)=m(P_n), and convergence of these measures to log theta>0.
Thus the original irreducible degree in every conclusion below is d, not D when c_n is nontrivial.
No new family, irreducibility theorem or near-one sequence is being inferred.

The argument below gives an explicit, deliberately crude constant independent of n for both actual kappa_(2d)(p_n) and the nonconstant Fourier coefficient sum of its C158 cubic.
Consequently this particular family cannot exhibit unbounded values of either quantity as n grows.
The bound does not assert a small constant, a numerical improvement of H4, or uniform control for varying seeds or hypothetical inputs with total measure tending to zero.

<a id="argument"></a>
<a id="fixed-support-already-excludes-near-one"></a>
## 1. The near-one diagnostic is already excluded by C92

P_n is a six-term rational annihilator of every original root of p_n, with all six coefficient moduli equal to one.
Its actual width is D=n+3, and its effective support rho is exactly six.
For n>=16, d>=n-9 and hence D/d<3.
If the total measures of any such inputs tended to zero, the accepted C92 inequality would eventually require

    5 epsilon(h)+12h>=1, h=D m(p_n)/d<=3m(p_n),

while both terms tend to zero, a contradiction.
This is a direct application of the accepted annihilator theorem, not a new family gap proof.
L38 already gives the much stronger explicit fixed lower limit log theta.
Bounded seed support therefore makes this family unsuitable for testing a hypothetical total-m-to-zero transfer, irrespective of its original degree growth or cyclotomic cancellation.
It can still test conjectures on the larger fixed-positive-measure range m<log(4/3), as L326 already did for the false bound four.

<a id="fixed-seed-gram-coercivity"></a>
## 2. Uniform lower bound for the actual short relation Gram

We first prove a finite coefficient inequality independent of n.
Let X be any complex polynomial of degree at most n+2 and put Y=P_n X.
The symbol q has constant coefficient one, so its formal power-series inverse at zero exists.
Direct multiplication gives

    f/q = -1-t-t^2-t^3-2t^4-2t^5 mod t^6.             (1)

For n>=6, the first six coefficients of Y equal those of qX.
Therefore the first six coefficients of fX are obtained from those same six Y coefficients by the lower-triangular convolution in (1).
The sum of absolute values of its six coefficients is eight; the elementary l2 convolution inequality gives

    ||(fX)_(0,...,5)||_2 <= 8 ||Y_(0,...,5)||_2.        (2)

For completeness that inequality follows by writing convolution as a sum of six scalar multiples of zero-padded shifts, each of which is an l2 contraction, and applying the triangle inequality.
It requires neither an infinite inverse norm nor a bound on all coefficients of 1/q.

Because deg(qX)<=n+5, every coefficient of fX at index j>=6 is exactly the coefficient of Y at index n+j.
Those output positions lie at or above n+6 and are disjoint from the first six positions.
Combining their squared sums with (2) yields

    ||fX||_2^2 <= 64||Y||_2^2.                       (3)

All zero padding and boundary coefficients are included.
No information is required from the middle six overlap positions of Y.

There is a simple fixed lower bound for f on the unit circle.
With x=cos(theta), direct expansion gives

    |f(exp(i theta))|^2 = 5+8x-4x^2-8x^3.

The endpoint values at x=+/-1 are one; the only critical points solve 3x^2+x-1=0.
Evaluating them shows that the minimum on [-1,1] is (97-26sqrt(13))/27.
This is greater than 1/16: the equivalent comparison 1525>416sqrt(13) follows after squaring from 2325625>2249728.
Parseval and (3) consequently give

    ||P_n X||_2^2 > ||X||_2^2/1024.                  (4)

Also ||P_n||_1=6 gives the elementary upper bound ||P_n X||_2<=6||X||_2 by the same finite-shift argument.
Thus, for every relation matrix A consisting of r consecutive shifts of P_n with 1<=r<=n+3, its full coefficient Gram G=A^t A obeys

    (1/1024) I <= G <= 36 I.                         (5)

The strict lower inequality from (4) has only been weakened here.
This is uniform in the actual matrix dimension r, without an assumption of finite diagonal dominance.

<a id="fixed-seed-cyclic-inverse-sum"></a>
## 3. Uniform inverse row sums from the actual cyclic sparsity

The full autocorrelation of P_n is

    P_n(t)P_n(t^-1)
      =2 f(t)f(t^-1)+t^(n-3)f(t)^2
                         +t^(-n+3)f(t^-1)^2.         (6)

Hence its nonzero offsets have absolute value at most three or lie between n-3 and n+3.
For an r-by-r Gram with r<=n+3, any occurring latter offset h<=r-1 satisfies r-h<=6.
Accordingly every nonzero matrix entry has cyclic distance at most six, where the cyclic distance on indices modulo r is min(|i-j|,r-|i-j|).
This is a finite matrix support statement, not an assertion that the Gram is circulant.

Put

    rho=1-1/36864,
    Z=I-G/36,
    C0=(1/36)[1/(1-rho)+12rho/(1-rho)^2].             (7)

By (5), 0<=Z<=rho I in the spectral order.
Every entry of Z^j has modulus at most rho^j.
The product support has cyclic distance at most 6j, because each factor moves by distance at most six and the cyclic distance satisfies the triangle inequality.
A cyclic ball of radius 6j has at most 12j+1 indices, including when that bound exceeds r.
Therefore each row of Z^j has absolute sum at most (12j+1)rho^j.

The finite-dimensional geometric series G^-1=(1/36)sum_(j>=0) Z^j converges in operator norm.
The preceding summable row bounds justify absolute entrywise summation and yield

    max_i sum_j |(G^-1)_(i,j)| <= C0.                 (8)

The same bound holds for columns by symmetry.
The explicit C0 is very large; only its independence of n and r is relevant here.
No uncharged graph-volume or condition-number dependence is hidden.
This elementary power-series proof does not require any external band-matrix inverse theorem as a mathematical premise.
Its relation to classical inverse-decay results is separately recorded below, without a novelty claim.

<a id="fixed-seed-original-factor-projection"></a>
## 4. Original Salem factor and the bounded cyclotomic correction

Work in the required original coefficient window M=2d for p_n.
Put r=M-D=D-2c=d-c.
For n>=22, c<=12 ensures r>=n-21>=1.
For 16<=n<=21 the actual cyclotomic table gives c respectively 1,0,1,0,1,8, so r is also positive.
Always r<=D=n+3, so (5)--(8) apply to the r relation columns P_n,tP_n,...,t^(r-1)P_n in this same M-coordinate window.
Let R_P be their residual projection and R_p the actual rank-d residual projection for all d shifts of the irreducible p_n.
The former has rank D=d+c, rather than d.

Define B_r(t)=v_r(t^-1)^t G^-1 v_r(t).
Equation (8) gives ||B_r||_W<=r C0, retaining the entire inverse rather than only a diagonal approximation.
The elementary coefficient derivation of L321's identity applies to this monic P_n with its full relation columns, whether or not P_n is irreducible:

    v_M(t^-1)^t R_P v_M(t)=M-P_n(t)P_n(t^-1)B_r(t).

The relation columns are independent by their distinct leading degrees, and no root or arithmetic hypothesis is used in that identity.
The symbol in (6) has Wiener norm at most ||P_n||_1^2=36.
If a_h(R) is the h-th upper diagonal sum, it follows that

    (2/d)sum_(h>=1)|a_h(R_P)| <=36 C0 r/d<=36 C0.      (9)

The normalization in (9) deliberately uses the original Salem degree d; it does not mislabel rank(R_P) as d.

Every P_n multiple in this window is a p_n multiple, so the corresponding relation spaces are nested.
Thus E=R_P-R_p is an orthogonal projection of rank c and is positive semidefinite.
For any positive semidefinite M-by-M matrix E,

    sum_(i<j)|E_ij| <= (M-1)trace(E)/2.

Indeed |E_ij|<=sqrt(E_ii E_jj), and the sum is bounded using the square of the sum of diagonal square roots and Cauchy--Schwarz.
Grouping into diagonals and using trace(E)=c proves

    (2/d)sum_(h>=1)|a_h(E)| <= (2d-1)c/d <2c

when c>0, with equality zero when c=0.
The triangle inequality and (9) now give the actual original-input result

    kappa_(2d)(p_n) <= 36 C0+2c <=36 C0+24=:K.         (10)

All cyclotomic factors are included through the complete accepted table and paid by their actual removed degree.
No projection is computed at the numerator degree and then silently relabeled as an original-degree result.
The irreducible progression n=9 mod120, n>=129, has c=0 and satisfies the sharper 36C0 bound directly.

<a id="fixed-seed-cubic-wiener-bound"></a>
## 5. The actual cubic Fourier cost and the diagnostic decision

For the actual p_n kernel k in C158 at M=2d, the constant coefficient is 1/2 and its nonconstant absolute coefficient sum is kappa_(2d)(p_n)/2.
Thus v=1-k has

    ||v||_W=(1+kappa_(2d)(p_n))/2 <=(1+K)/2=:W.

The actual cubic is G_3=log2-v/2-v^2/8-v^3/24.
Finite coefficient convolution and removal of the constant term give

    sum_(h!=0)|G3hat(h)| <= W/2+W^2/8+W^3/24.        (11)

This bound is uniform in n for this fixed family.
It bounds the requested cubic Wiener cost, not a newly asserted Wiener norm of the full logarithm h=log(1+k).
C158's actual cubic support, original values and 1/32 approximation error remain exactly as accepted.
The full rational scalar normalization and original-root/Haar transfer requirements have not been altered.

Therefore no growing-degree scan of this one Perron seed can establish unbounded kappa or unbounded cubic Fourier mass: the author argument (10)--(11), if accepted after separate review, rules both out.
The existing n18 value above four remains fully compatible with the deliberately crude fixed upper bound.
This is also compatible with C143, whose square-root growth family has different growing input coefficients and large total measure.
It does not answer the corresponding question for varying seeds or all Salem inputs below log(4/3).

No new numerical proposal is warranted merely to search for divergence in this family.
The concrete next verification is independent checking of the coefficient recovery, cyclic-support argument and rank-correction normalization above.
If any of those steps fails, retain the failed implication before deciding whether a bounded finite calculation can distinguish the remaining alternatives.
If they pass, terminate this family's divergence diagnostic and return to an input class not already covered by fixed-support annihilator control.
No such broader computational class has been selected or run here.

## Source attribution and author-check boundary

The local targeted reuse searches found the L321 finite diagonal-dominance bound, but no retained theorem establishing (4)--(11) for this specific family.
An initial PowerShell wildcard-path search failed; it was replaced by rg include globs over the responsible directories, so that failed command supplies no absence evidence.
The subsequent broader hits concerning circular root distances, finite-range entropy and scalar determinant theory did not provide the needed matrix argument.
This is a bounded reuse screen, not an exhaustive novelty search.

The inverse-power argument is an instance of the classical matrix-power-support decay mechanism identified in [DMS84-U001](../audits/literature/DMS84/Yin_U001.md#dms84-matrix-power-support).
The actual inspected source is the first appended author manuscript in the registered Georgia Tech report bundle, not an asserted copy of the nine-page journal edition.
Its Proposition 5.1, manuscript p.17 / PDF p.24, gives inverse-entry decay outside the union of supports of the first matrix powers, and Example 2 on the following page explicitly discusses periodic corner entries.
The source statement, power-support definitions and periodic example were visually checked; Proposition 2.2 and its spectral-polynomial proof were text-read with the statement visually checked.
The published edition and upstream approximation proof were not independently audited.
The exact source serves attribution, not a proof premise: (7)--(8) retain their own geometric-series constants and explicit cyclic-volume proof, rather than importing the source's sharper approximation constants.
No novelty is claimed for this inverse-decay mechanism; the family-specific coefficient recovery, original-degree normalization and cyclotomic correction are the local deductions.

Author checks covered the six recovered boundary coefficients, the disjoint known output ranges, the exact circle minimum, every spectral and cyclic-ball constant, the r versus d versus D distinction, the small-n positive-column guard, the nested relation spaces and positive rank-c correction, both signed Fourier diagonals, and the cubic rather than full-logarithm scope.
The mathematical deduction is currently author-checked only and needs a separate noncontributor review before acceptance.
The source identification is resolved at its actual recorded manuscript statement scope, without upgrading the depth of the external proof inspection.

## Current assessment
[Selected decision](#decision-current-excess-three-family-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:56 |
| status | open |
| reason | Register the full fixed-seed original-degree projection theorem for separate whole review, with explicit finite spectral/inverse constants, complete cyclotomic correction and actual cubic Fourier scope. The classical mechanism attribution is resolved at the inspected manuscript statement scope; no external proof upgrade, near-one coverage or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete family statement](#statement) | Every n>=16, actual Salem factor p_n and original degree d, full M=2d residual, explicit uniform kappa/cubic bounds and finite Gram/inverse intermediates. |
| argument | [Complete local argument](#argument) | Sections 1--5, all eleven formulas, recovered boundary coefficients, exact circle minimum, cyclic support and series, all original-degree/rank corrections and stated limitations. |
| dependency | [Accepted Salem family](../ledger/Yin_L_G0038_v1.md#excess-three-family) | Actual Salem minimal factor, monicity/reciprocity/nontorsion, fixed positive measure interval and original factorization scope for n>=16. |
| dependency | [Complete cyclotomic table](../ledger/Yin_L_G0038_v1.md#family-cyclotomic-factors) | Exact five residue conditions, squarefree complete cyclotomic part and c<=12, including the small-n positive-column guard. |
| dependency | [Inverse-Gram coefficient identity](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact coefficient derivation K_R=M-H_P B_r; its purely algebraic generalization to the reducible numerator is proved explicitly here without importing its irreducible arithmetic scope. |
| dependency | [Actual cubic interface](Yin_C_G0158_v1.md#statement) | Actual N=2d rank-d kernel, constant coefficient 1/2, signed Fourier normalization, cubic coefficients and distinction from the full logarithm. |
| dependency | [Short-annihilator comparison](Yin_C_G0092_v1.md#statement) | Only Part A for the six-term annihilator of width/original-degree ratio below three; reused to explain why this fixed family is not a total-measure-to-zero diagnostic. |
| support | [Classical inverse-power attribution](../audits/literature/DMS84/Yin_U001.md#dms84-u001) | Actual manuscript Proposition 5.1 and periodic-corner Example 2 identify the established matrix-power-support decay mechanism; no external quantitative constant or original proof is a premise of the local geometric-series bound. |
| support | [Existing degree-twenty H4 failure](../ledger/Yin_L_G0326_v1.md#h4-actual-counterexample) | Previously accepted original-degree counterexample to the bound four, compatible with the coarse uniform family bound; no native value is recomputed. |
| support | [Separate large-measure obstruction](Yin_C_G0143_v1.md#statement) | The square-root-growth family changes the input and pays large measure, so it is not contradicted or covered by this fixed-seed result. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:59 |
| status | proved |
| reason | Adopt the complete original-degree uniform fixed-seed projection/cubic bound after the actual noncontributor whole R385 review, including every boundary coefficient, cyclic inverse cost and cyclotomic-rank correction. This closes only that family's divergence diagnostic; changing-seed and near-one arithmetic coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete family statement](#statement) | Every n>=16, actual Salem factor p_n and original degree d, full M=2d residual, explicit uniform kappa/cubic bounds and finite Gram/inverse intermediates. |
| argument | [Complete local argument](#argument) | Sections 1--5, all eleven formulas, recovered boundary coefficients, exact circle minimum, cyclic support and series, all original-degree/rank corrections and stated limitations. |
| dependency | [Accepted Salem family](../ledger/Yin_L_G0038_v1.md#excess-three-family) | Actual Salem minimal factor, monicity/reciprocity/nontorsion, fixed positive measure interval and original factorization scope for n>=16. |
| dependency | [Complete cyclotomic table](../ledger/Yin_L_G0038_v1.md#family-cyclotomic-factors) | Exact five residue conditions, squarefree complete cyclotomic part and c<=12, including the small-n positive-column guard. |
| dependency | [Inverse-Gram coefficient identity](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact coefficient derivation K_R=M-H_P B_r; its purely algebraic generalization to the reducible numerator is proved explicitly here without importing its irreducible arithmetic scope. |
| dependency | [Actual cubic interface](Yin_C_G0158_v1.md#statement) | Actual N=2d rank-d kernel, constant coefficient 1/2, signed Fourier normalization, cubic coefficients and distinction from the full logarithm. |
| dependency | [Short-annihilator comparison](Yin_C_G0092_v1.md#statement) | Only Part A for the six-term annihilator of width/original-degree ratio below three; reused to explain why this fixed family is not a total-measure-to-zero diagnostic. |
| support | [Classical inverse-power attribution](../audits/literature/DMS84/Yin_U001.md#dms84-u001) | Actual manuscript Proposition 5.1 and periodic-corner Example 2 identify the established matrix-power-support decay mechanism; no external quantitative constant or original proof is a premise of the local geometric-series bound. |
| support | [Existing degree-twenty H4 failure](../ledger/Yin_L_G0326_v1.md#h4-actual-counterexample) | Previously accepted original-degree counterexample to the bound four, compatible with the coarse uniform family bound; no native value is recomputed. |
| support | [Separate large-measure obstruction](Yin_C_G0143_v1.md#statement) | The square-root-growth family changes the input and pays large measure, so it is not contradicted or covered by this fixed-seed result. |
| review | [Whole family finding](../audits/reviews/Yin_R_G0385_v1.md#fixed-seed-projection-whole-independent-finding) | Complete fixed statement and all eleven proof formulas, five declared dependencies and three support interfaces, all finite/original-degree/cyclic constants, exact classical attribution and limited diagnostic scope. |

### Decision current-excess-three-family-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:25 |
| status | proved |
| reason | Select the complete retained C248 proof as the current responsible home for the identical previously used L38 Salem-family interface at exactly the selected anchors below. The original whole argument and the current complete retained proof were read, including the actual all-N factorization and the n>=16 expanding-root guard. This changes only the current proof locator; statement, argument, relation scopes, mathematical status, all other inputs and the actual original R finding remain unchanged. Historical decisions and reviews keep their actual fixed L38 targets, and no new independent review or stronger family theorem is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete family statement](#statement) | Every n>=16, actual Salem factor p_n and original degree d, full M=2d residual, explicit uniform kappa/cubic bounds and finite Gram/inverse intermediates. |
| argument | [Complete local argument](#argument) | Sections 1--5, all eleven formulas, recovered boundary coefficients, exact circle minimum, cyclic support and series, all original-degree/rank corrections and stated limitations. |
| dependency | [Accepted Salem family](Yin_C_G0248_v1.md#excess-three-family) | Actual Salem minimal factor, monicity/reciprocity/nontorsion, fixed positive measure interval and original factorization scope for n>=16. |
| dependency | [Complete cyclotomic table](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Exact five residue conditions, squarefree complete cyclotomic part and c<=12, including the small-n positive-column guard. |
| dependency | [Inverse-Gram coefficient identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Exact coefficient derivation K_R=M-H_P B_r; its purely algebraic generalization to the reducible numerator is proved explicitly here without importing its irreducible arithmetic scope. |
| dependency | [Actual cubic interface](Yin_C_G0158_v1.md#statement) | Actual N=2d rank-d kernel, constant coefficient 1/2, signed Fourier normalization, cubic coefficients and distinction from the full logarithm. |
| dependency | [Short-annihilator comparison](Yin_C_G0092_v1.md#statement) | Only Part A for the six-term annihilator of width/original-degree ratio below three; reused to explain why this fixed family is not a total-measure-to-zero diagnostic. |
| support | [Classical inverse-power attribution](../audits/literature/DMS84/Yin_U001.md#dms84-u001) | Actual manuscript Proposition 5.1 and periodic-corner Example 2 identify the established matrix-power-support decay mechanism; no external quantitative constant or original proof is a premise of the local geometric-series bound. |
| support | [Existing degree-twenty H4 failure](Yin_C_G0592_v2.md#h4-actual-counterexample) | Previously accepted original-degree counterexample to the bound four, compatible with the coarse uniform family bound; no native value is recomputed. |
| support | [Separate large-measure obstruction](Yin_C_G0143_v1.md#statement) | The square-root-growth family changes the input and pays large measure, so it is not contradicted or covered by this fixed-seed result. |
| review | [Whole family finding](../audits/reviews/Yin_R_G0385_v1.md#fixed-seed-projection-whole-independent-finding) | Complete fixed statement and all eleven proof formulas, five declared dependencies and three support interfaces, all finite/original-degree/cyclic constants, exact classical attribution and limited diagnostic scope. |

