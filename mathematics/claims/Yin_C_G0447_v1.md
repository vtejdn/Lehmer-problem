---
author: Yin
---

# Complete ideal isolation, congruence-control bridge and residue-radius obstructions

The complete necessary original D55 proof is retained from [L187](../ledger/Yin_L_G0187_v1.md#retained-ideal-control-argument).
The structural drafting agent supplied the ideal, residue-count and sparse-label deductions; the coordinator assigned the questions and received checkpoints without supplying those deductions.
The original2026-10-10 whole check's exact five-section scope and unknown initial relationship are retained in [the later explicit comparison](../audits/reviews/Yin_R_G0660_v1.md#comparison-after-the-autonomous-initial-findings).
Generic shared context/progress descriptions do not establish its initial target mathematics, and authorship of fixed L180 does not itself establish a SELF relationship for this target.
The exact original [listed author checks](../audits/reviews/Yin_R_G0086_v1.md#ideal-control-original-author-check-finding) remain SELF at their recorded scope.
No source/PDF reading, new program/J, native execution or research Task/E is added.

## Statement

Let beta>1 be a Salem number of degree d=2s+2, integer s>=1, with neutral conjugate representatives zeta_1,...,zeta_s.
Set O=Z[beta], S=beta/(beta-1), B=1/(beta-1), and

    N={x in O: |x_+|<=1, |x_-|<=S},
    rho(x)^2=sum_(j=1)^s|x(zeta_j)|^2,
    K_R={x in N:rho(x)<=R}, R>=0.

Here x_+ and x_- are the distinguished beta and beta^-1 real embeddings; all digits remain{-1,0,1}.
For every nonzero ideal I of O its finite index n(I)=[O:I] gives the exact isolation bound

    0!=x in I cap N => rho(x)>=J(I),
    J(I)=sqrt(s)(n(I)/S)^(1/(d-2)).

In particular, for each integer q>=2,

    n(qO)=q^d,
    J(qO)=sqrt(s)S^(-1/(d-2))q^(d/(d-2)),
    0<=R<J(qO) => K_R cap qO={0}.

The strict comparison does not remove a possible equality case.
Any ideal containing a fixed nonzero x has index at most |N_field(x)|; a unit belongs to no proper ideal.
One cannot isolate a fixed unit by choosing arbitrarily large containing ideals.

For a word w of length n use D_w=sum_(i=1)^n eta_i beta^(n-i), endpoint T_w(x)=beta^n x+D_w and the exact neutral displacement c_w defined below.
Call it zero-class preserving when D_w lies in I.
It then preserves I, without fixing every other residue class.
Assume a finite closed-cell cover of[1/2,1] by strictly legal original-word families all satisfying D_w in I, such that every corresponding hull of the nonzero vectors c_w/||c_w||^2 contains the centered closed ball of one common radius r_I>0.
If

    r_I>1/(2J(I)),

then every actual x in N cap I has a finite original-digit co-return to zero, with all intermediate states in the original real strip and stable bound.
More precisely choose1/(2r_I)<R<J(I), and let m_I>0 be the minimum retained squared displacement norm.
Every chosen reduction outside rho<R drops squared norm by at least

    delta_I=m_I(2r_I R-1)>0.

The assumed strict cover itself forces beta<2; its full original-word/sign/zero-prefix/real/stable proof is retained below.
No such ideal-preserving cover or quantitative margin is constructed here.
For qO the required bound is

    r_q>S^(1/(d-2))q^(-d/(d-2))/(2sqrt(s)).

To conclude co-return for every x in N, assume additionally beta<phi=(1+sqrt(5))/2 and a finite strict legal-entry certificate into N cap I for every state of a completely covered ordinary compact residue K_(R0) provided by the complete global control theorem.
This certificate and the ideal-preserving cover are separate obligations.
Finite quotient connectivity alone has no strict real endpoint guarantee.
A family of actual compact descent radii R_q=o(q^(d/(d-2))) would eventually be smaller than J(qO), only if its descent constants and strict legal entry certificates are actually proved.

Separately there are fixed-input constants

    C_+=sum_(i=0)^(d-1)beta^i, C_-=sum_(i=0)^(d-1)beta^(-i),
    C_cell=(C_++1)(C_-/S+1),
    C_K=(1+epsilon)(S+epsilon)/epsilon^d,

where0<epsilon<=1 makes the full embedding lattice's open coordinate cubes of side2epsilon disjoint.
For every integer q>=2 and every real R>=0,

    #classes represented by N modulo qO>=q^(d-2)/C_cell,
    |K_R|<=C_K(R+1)^(d-2).

Consequently any continuation assigning to every x in N an endpoint in K_(R_q) with the same class modulo qO must satisfy

    R_q+1>=q/(C_cell C_K)^(1/(d-2)).

No restriction on intermediate congruences or a common policy is needed for this count.
This linear lower scale concerns preservation of all represented classes, not just control on the zero class.
It neither contradicts the larger fixed-degree isolation exponent nor supplies degree-uniform constants.

For the sparse-label statement assume beta<phi and choose an integer L>=2 such that

    B-beta^(-1)/(1-beta^(-L))>1.

For every prescribed set S_0 of positive positions with consecutive gaps at least L, set W=sum_(i in S_0)beta^(-i).
Every pattern e_i in{0,1} on S_0, with D=sum_(i in S_0)e_i beta^(-i), has exactly the complete real-sum interval[D,D+B-W] after arbitrary free completion.
The common interval over all patterns is exactly[W,B-W] when W<=B/2.
Starting the prescribed set sufficiently late accommodates every such pattern for each fixed strictly interior target in[0,B].
The sign-dependent binary shift preserves the original alphabet.
The quantifier is for every fixed prescribed pattern there exists a free completion; it does not allow independently repairing finite residue contributions after free digits have been chosen.

For every nontrivial finite quotient O/I and every fixed original word, the map r->beta^n r+D_w is a permutation.
Thus no state-independent fixed word resets every residue to zero or merges two distinct residues.
State-dependent words or branching with real overlap are not excluded.
If a finite family of zero-class-preserving words with c_w!=0 is strictly legal at real zero, then each normalized vector has norm at most1/J(I), so any centered ball in that particular hull has radius at most1/J(I).
This legal-at-zero upper bound is not asserted for arbitrary annulus families and does not contradict the required lower margin1/(2J(I)).

The bridge is a complete conditional theorem with its two constructive hypotheses unresolved.
Actual-order membership removes the separate fractional-module class obstruction but supplies neither hypothesis.
Universal actual compact termination, original-law costs, coupled real/residue expansion and a uniform Mahler gap remain unproved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-r807-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:30 |
| status | open |
| reason | Retain the entire quantitative ideal-control theorem, every norm/degree/q/real/finite-cover/sparse-pattern assumption, both constructive termination obligations and all exact limitations. Complete actual current whole self-check and adoption follow separately; the original whole UNKNOWN and listed author SELF remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire precise conditional theorem and obstructions](#statement) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| argument | [All necessary original mathematical proofs](#argument) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| dependency | [Complete normalized convex control and legal compact descent](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only exact original-word neutral cocycle/positive normalization/finite strict covers/common positive displacement lower bound, squared-norm drop, zero/sign extensions, stable invariance and backward open real strip. No unconstrained cover is assumed to preserve an ideal. |
| dependency | [Complete beta-less-than-phi global and sparse binary control](Yin_C_G0428_v1.md#small-salem-global-pointwise-control) | Only ordinary finite compact reduction and the arbitrary sparse prescribed-position free binary interval at beta<phi, exact gap inequality and sign-dependent original-alphabet shift. It provides no ideal-preserving margin, coupled finite congruence or legal-entry certificate. |
| dependency | [Complete actual compact certificate and quotient distinction](Yin_C_G0435_v1.md#compact-termination-certificate-interface) | Completely covered finite actual compact residue/finite exact original-word termination criterion, full embedding lattice and finite index, with separate original-digit quotient connectivity and fractional-module obstruction below. No breadth-first finite failure or policy cycle is a nonreturn certificate. |
| dependency | [Complete original-digit finite quotient connectivity](Yin_C_G0435_v1.md#original-digit-finite-quotient-connectivity) | Every algebraic-unit order/nonzero proper ideal and common-length0/1 quotient word, without any real-strip or narrow-endpoint guarantee. It does not discharge the additional strict legal-entry obligation. |
| dependency | [Complete fractional-module obstruction at its exact scope](Yin_C_G0435_v1.md#fractional-module-five-class-obstruction) | Only preservation of M/O and a genuine nonzero fractional class obstruction outside O; that class is zero for actual initial x in O, without proving actual termination. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:32 |
| status | proved |
| reason | Adopt after actual complete current self-check of the whole ideal-index/norm/isolation proof, quantitative zero-class normalized cover and exact finite-drop/sign/zero-prefix/stable/backward-strip chain, separate compact legal-entry obligation, all-residue coefficient/packing counts and radius constants, sparse prescribed labels/free completion quantifiers, finite quotient permutation and legal-at-zero normalized bound. Every original mathematical argument and necessary interface is retained; zero normalized displacements are explicitly excluded and the assumed strict cover itself enforces beta<2. No substantive defect or missing hypothesis was found. The current authored whole SELF does not close original R86 whole UNKNOWN or enlarge its precise listed author SELF. No ideal-cover/entry construction, universal termination, original-law or uniform Mahler gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| argument | [Exact retained argument](#argument) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| dependency | [Exact retained dependency](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only exact original-word neutral cocycle/positive normalization/finite strict covers/common positive displacement lower bound, squared-norm drop, zero/sign extensions, stable invariance and backward open real strip. No unconstrained cover is assumed to preserve an ideal. |
| dependency | [Exact retained dependency](Yin_C_G0428_v1.md#small-salem-global-pointwise-control) | Only ordinary finite compact reduction and the arbitrary sparse prescribed-position free binary interval at beta<phi, exact gap inequality and sign-dependent original-alphabet shift. It provides no ideal-preserving margin, coupled finite congruence or legal-entry certificate. |
| dependency | [Exact retained dependency](Yin_C_G0435_v1.md#compact-termination-certificate-interface) | Completely covered finite actual compact residue/finite exact original-word termination criterion, full embedding lattice and finite index, with separate original-digit quotient connectivity and fractional-module obstruction below. No breadth-first finite failure or policy cycle is a nonreturn certificate. |
| dependency | [Exact retained dependency](Yin_C_G0435_v1.md#original-digit-finite-quotient-connectivity) | Every algebraic-unit order/nonzero proper ideal and common-length0/1 quotient word, without any real-strip or narrow-endpoint guarantee. It does not discharge the additional strict legal-entry obligation. |
| dependency | [Exact retained dependency](Yin_C_G0435_v1.md#fractional-module-five-class-obstruction) | Only preservation of M/O and a genuine nonzero fractional class obstruction outside O; that class is zero for actual initial x in O, without proving actual termination. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0651_v1.md#current-ideal-control-whole-finding) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. Actual current whole relationship is self-reviewed; original whole UNKNOWN and exact listed author SELF remain separate. |


### Decision complete-isolated-whole-r807-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:15 |
| status | proved |
| reason | Adopt the complete fresh isolated whole finding after coordinator full reading of its exact mathematical reconstruction, all original whole/source/author/negative comparisons and truthful dates; no target repair and no retrospective change to old UNKNOWN or SELF. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| argument | [Complete selected argument](#argument) | Entire original D55 Sections1--5/formulas(1)--(9) and explicit needed original-digit/neutral/strict-strip conventions: every Salem beta/order/all s conjugate pairs/nonzero ideal with finite index, exact norm/index isolation and strict equality guard, every integer q>=2/q^d index/fixed-state-unit restriction, finite strictly legal zero-class cover with nonzero individually normalized vectors/rI>1/(2J)/positive minimum displacement/exact drop and automatic beta<2 guard/sign and zero-prefix rotation/stable and backward real bounds, separate beta<phi ordinary finite compact entry obligation without a quotient legality inference, exact distinct-residue coefficient count/packing constants/linear all-class radius lower bound and degree dependence, every sparse prescribed set/pattern/common interval/free-digit quantifier/golden-ratio guard, finite quotient permutation/no state-independent reset and legal-at-zero nonzero-vector upper margin. No required cover/strict entry certificate/state-dependent residue-aware expansion/universal termination/original-law bound is constructed; all old source, contribution and execution limits remain. |
| dependency | [Exact accepted input](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) | Only exact original-word neutral cocycle/positive normalization/finite strict covers/common positive displacement lower bound, squared-norm drop, zero/sign extensions, stable invariance and backward open real strip. No unconstrained cover is assumed to preserve an ideal. |
| dependency | [Exact accepted input](Yin_C_G0428_v1.md#small-salem-global-pointwise-control) | Only ordinary finite compact reduction and the arbitrary sparse prescribed-position free binary interval at beta<phi, exact gap inequality and sign-dependent original-alphabet shift. It provides no ideal-preserving margin, coupled finite congruence or legal-entry certificate. |
| dependency | [Exact accepted input](Yin_C_G0435_v1.md#compact-termination-certificate-interface) | Completely covered finite actual compact residue/finite exact original-word termination criterion, full embedding lattice and finite index, with separate original-digit quotient connectivity and fractional-module obstruction below. No breadth-first finite failure or policy cycle is a nonreturn certificate. |
| dependency | [Exact accepted input](Yin_C_G0435_v1.md#original-digit-finite-quotient-connectivity) | Every algebraic-unit order/nonzero proper ideal and common-length0/1 quotient word, without any real-strip or narrow-endpoint guarantee. It does not discharge the additional strict legal-entry obligation. |
| dependency | [Exact accepted input](Yin_C_G0435_v1.md#fractional-module-five-class-obstruction) | Only preservation of M/O and a genuine nonzero fractional class obstruction outside O; that class is zero for actual initial x in O, without proving actual termination. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0660_v1.md#isolated-ideal-control-whole-finding) | Whole exact ideal index/isolation/conditional legal control/separate compact entry theorem and all residue/sparse/permutation/packing/strict/source and unconstructed-hypothesis limits. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-ideal-control-argument"></a>
<a id="ideal-control-fixed-scope"></a>

### Exact original alphabet, displacement and strict-strip conventions

Let phi=(1+sqrt(5))/2 and B=1/(beta-1).
A word w=(eta_1,...,eta_n) has positive integer length n and every eta_i in{-1,0,1}.
For one neutral root zeta_j from each conjugate pair, use

    b_w=sum_(i=1)^n eta_i beta^(-i),
    c_w=(sum_(i=1)^n eta_i zeta_j^(-i))_(j=1)^s,
    A=diag(zeta_1,...,zeta_s),
    z(T_w(x))=A^n(z(x)+c_w),
    T_w(x)_+=beta^n(x_++b_w).

The complex neutral space C^s has its usual real inner product and norm rho.
A word is strictly legal on a closed real interval when its final real coordinate has absolute value less than one at every point of that interval.
The finite cover below assigns finitely many such words to each of finitely many closed cells covering[1/2,1].
Every normalized vector c_w/||c_w||^2 excludes c_w=0.
In the final legal-at-zero normalized-hull statement, the nonzero-word condition means precisely c_w!=0, equivalently D_w!=0, rather than merely a nonempty digit list.

The assumed strict cover already forces beta<2.
Indeed for beta>=2, starting at x_+=1 every original word of length n satisfies

    T_w(1)>=beta^n-(beta^n-1)/(beta-1)
           =[(beta-2)beta^n+1]/(beta-1)>=1.

It cannot be strictly legal at that covered endpoint.
Thus whenever the conditional cover exists, B>1 and the zero-prefix first crossing of[1/2,infinity) lies below beta/2<1.
Each such prefix only rotates the neutral state and has zero displacement.
At the suffix one chooses the decreasing vertex for that actual rotated direction; the common margin and positive lower squared displacement norm remain unchanged.
Every original digit preserves |x_-|<=S, since beta^-1 S+1=S.
If a length-n word has a strict narrow final real value, then a state with k remaining digits satisfies

    |x_+|<beta^-k+B(1-beta^-k)
          =B-(B-1)beta^-k<B.

This proves every intermediate real value lies in the original open strip, without a new hypothesis on intermediate compact radii.
For negative starts use the negated word, and if the distinguished real coordinate is zero the field element itself is zero.
The quantitative conditional bridge therefore applies at every actual point of N intersect I.
The stronger beta<phi guard is needed only for the already proved ordinary global compact reduction and the sparse binary interval lemma used below.
Norm isolation and the all-residue counting argument themselves apply to any Salem beta>1.

<a id="ideal-zero-class-isolation-scale"></a>
### 1. Exact norm isolation inside the actual order

Fix a Salem beta of degree d=2s+2, s>=1, with 1<beta<phi when invoking the fixed global control theorem.
Use O=Z[beta], S=beta/(beta-1), and

    N={x in O: |x_+|<=1, |x_-|<=S},
    rho(x)^2=sum_(j=1)^s |x(zeta_j)|^2,
    K_R={x in N: rho(x)<=R}.

Let I be a nonzero ideal of O and write n(I)=[O:I].
This index is finite by the argument in [complete quotient theorem](Yin_C_G0435_v1.md#original-digit-finite-quotient-connectivity).
For nonzero x in I, the inclusions xO subset I subset O and multiplicativity of finite group indices give

    |N_field(x)|=[O:xO]=n(I)[I:xO]>=n(I).

The two real bounds and the arithmetic-geometric mean inequality for the s nonnegative squared neutral moduli give

    n(I)<=|N_field(x)|
         <=S product_j |x(zeta_j)|^2
         <=S (rho(x)^2/s)^s.

Thus every nonzero x in I intersect N satisfies

    rho(x)>=J(I):=sqrt(s)(n(I)/S)^(1/(d-2)).         (1)

For the integer ideal I=qO, q>=2, n(I)=q^d because O is a free rank-d abelian group.
Therefore

    J(qO)=sqrt(s) S^(-1/(d-2)) q^(d/(d-2)),
    R<J(qO) implies K_R intersect qO={0}.            (2)

The strict radius inequality is kept; no equality case is silently discarded.
This is a fixed-input arithmetic isolation estimate in the actual order, with the full norm and all neutral pairs counted.
It does not identify which ideal classes can be reached by a real-legal path.

The fractional-module obstruction retained in C435 disappears for an initial x in O, since its class in the larger quotient M/O is then zero and all original operations preserve O.
This only removes that particular obstruction.
Choosing a large ideal containing x is not a substitute for entering its zero class: every such I contains xO and therefore n(I)<=|N_field(x)|.
If x is a unit, it belongs to no proper ideal at all.
Thus arbitrary moduli cannot be chosen around a fixed unit state by that shortcut.

<a id="zero-congruence-control-termination-bridge"></a>
### 2. A sufficient congruence-control bridge with an exact margin

For a word w of length n define its unnormalized translation

    D_w=sum_(i=1)^n eta_i beta^(n-i),
    T_w(x)=beta^n x+D_w.

Call a word zero-class preserving modulo I when D_w belongs to I.
Since beta is a unit, such a word sends I into I.
It need not fix other classes; preserving every class would be a stronger and different condition.

Suppose that the annulus[1/2,1] has a finite strict original-digit convex cover using only zero-class-preserving words, and that the hulls of their nonzero normalized neutral displacements c_w/||c_w||^2 all contain a centered ball of radius r_I>0.
Assume

    r_I>1/(2J(I)).                                   (3)

Choose R with1/(2r_I)<R<J(I), and let m_I>0 be the minimum squared norm of the finitely many nonzero displacements.
The [complete normalized calculation](Yin_C_G0416_v1.md#joint-neutral-pointwise-control) then gives a squared-neutral drop of at least

    delta_I=m_I(2r_I R-1)>0                          (4)

whenever the state norm is at least R.
All chosen endpoints are strictly narrow.
Negating a word preserves D_w in I, and initial zero digits preserve I, so the sign and zero-prefix extension to N intersect I retains the ideal condition.
The stable bound stays invariant.
Each nonzero real coordinate below1/2 reaches the annulus after finitely many zeros, while an actual algebraic state with real coordinate zero is zero.

Repeated descent reaches K_R intersect I after finitely many drops.
By(1) this set is{0}.
Consequently the displayed finite control cover and margin prove exact co-return for every state of N intersect I.
This is a complete conditional theorem; it requires the stated ideal-preserving cover and quantitative margin, neither of which follows merely from ordinary global PC.

To conclude co-return for all of N, one must additionally show legal entry into N intersect I.
A finite version suffices: first use the ordinary complete C428 compact reduction into its completely covered finite residue K_(R0), then for each member give an original word whose endpoint is both narrow and in I.
These are exact finite congruence-entry certificates; after them, the ideal-preserving reduction just proved ends at zero.
Original finite-quotient connectivity in C435 supplies no such narrow-endpoint guard.
The two obligations must be retained separately.

For qO the threshold(3) reads explicitly

    r_q > S^(1/(d-2)) q^(-d/(d-2))/(2sqrt(s)).       (5)

Thus a family of proved zero-class-preserving covers with radii R_q=o(q^(d/(d-2))) would eventually fall below the isolation scale, provided its actual descent constants and legal entry certificates were also established.
This is a useful target, not a claimed construction or an inference from all finite congruences being solvable.

<a id="all-residue-descent-linear-radius-cost"></a>
### 3. Preserving all residues forces a growing compact radius

Here is an exact obstruction to keeping the ordinary compact radius fixed while demanding preservation of every residue class.
There are fixed-input constants c_beta,C_beta>0 such that

    number of residue classes of N modulo qO
        >=c_beta q^(d-2),
    |K_R|<=C_beta(R+1)^(d-2).                        (6)

We prove both bounds directly.
Consider the q^d distinct representatives

    V_q={sum_(i=0)^(d-1) a_i beta^i:0<=a_i<q}.

Their real values lie between0 and(q-1)C_+, and their stable values between0 and(q-1)C_-, where C_+=sum_(i=0)^(d-1)beta^i and C_-=sum_(i=0)^(d-1)beta^(-i).
Partition these ranges into half-open cells of widths1 and S.
At most

    q^2 C_cell cells are needed,
    C_cell=(C_++1)(C_-/S+1).

Some cell contains at least q^(d-2)/C_cell representatives.
Subtract one selected representative from all the others in this cell.
Every difference is in N, with the two real magnitudes strictly less than1 and S.
Their classes modulo qO remain distinct, because the original coefficient representatives were distinct.
This proves the first bound in(6) with c_beta=1/C_cell, including the zero difference; integer rounding can only strengthen the count.

For the second bound, use the full real embedding lattice in R^d.
Choose0<epsilon<=1 so that the open coordinate cubes of side2epsilon centered at distinct lattice points are disjoint.
Such epsilon exists because the coefficient-to-embedding map is invertible and every nonzero integral coefficient vector has Euclidean length at least1.
The cubes around K_R lie in the box with the first two coordinate radii1+epsilon and S+epsilon, and every remaining coordinate radius at most R+epsilon.
Volume comparison gives

    |K_R|<=(1+epsilon)(S+epsilon)(R+epsilon)^(d-2)/epsilon^d
         <=C_K(R+1)^(d-2),
    C_K=(1+epsilon)(S+epsilon)/epsilon^d.             (7)

Now suppose every x in N has a continuation ending in K_(R_q) and in the same class as x modulo qO.
No condition on its intermediate congruences or chosen policy is needed for this count.
The endpoint set must represent every class represented by N.
Equations(6)--(7) force

    R_q+1 >= q/(C_cell C_K)^(1/(d-2)).               (8)

Therefore no fixed radius can support such an all-class-preserving reduction for all q.
This lower bound applies to the stronger all-residue demand, not just to zero-class-preserving control on N intersect qO.
It does not refute the bridge in Section2: its linear lower scale is smaller than q^(d/(d-2)) at every fixed finite degree, although the exponent difference2/(d-2) becomes small in high degree.
No degree-uniform constants are supplied by this counting argument.

<a id="sparse-labels-and-permutation-automaton-boundary"></a>
### 4. What the sparse binary construction does and does not prescribe

The coordinator suggested investigating a finite residue automaton within the original sparse free-slot proof now retained in C428.
This was a research question, not a supplied derivation.
The following exact extension and obstruction distinguish two versions of that idea.

Use beta<phi, B=1/(beta-1), and a gap L satisfying the inequality in the complete C428 Section2.
Let S_0 be prescribed positions with gaps at least L, and let W=sum_(i in S_0)beta^(-i).
The fixed free-slot proof shows that binary sums on the other positions fill[0,B-W].
For any prescribed pattern e_i in{0,1} on S_0, write D=sum_(i in S_0)e_i beta^(-i).
Its possible complete sums are exactly

    [D,D+B-W].

Since0<=D<=W, every prescribed pattern is compatible with every target in the common interval

    [W,B-W], provided W<=B/2.                        (9)

This is the exact common interval: the all-zero and all-one patterns force its two endpoints.
By starting the sparse set sufficiently late, W can be made smaller than the distance of a fixed interior target from either endpoint of[0,B].
Thus arbitrary fixed sparse binary labels, not only prescribed zeros, can coexist with a strictly interior real target.
This extension preserves the original alphabet after the sign-dependent shift retained in C428.

It does not yet enforce a residue.
At a finite horizon, every unprescribed digit also contributes to the residue equation.
The conclusion has the order 'for every fixed prescribed pattern, there exists a completing free pattern'; it is not a construction in which prescribed and free digits can then independently be changed to repair the finite residue.
A state-dependent automaton rule would impose a coupled condition on both groups of digits.
Neither(9) nor unconstrained quotient connectivity proves that coupled real-and-congruence condition.

There is also an exact obstruction to one simple synchronization proposal.
For any nontrivial finite quotient O/I, every fixed original word acts as

    r -> beta^n r+D_w modulo I.

This is a permutation, since beta is a unit.
Consequently no state-independent fixed word sends all residues to zero, or even merges two distinct residues.
A common reset block cannot exist in this automaton.
This does not exclude choosing different words according to the current state, nor more elaborate branching with real overlap.
It isolates the missing task: construct an actual state-dependent family which retains strict real representability while achieving the required translation congruences, and then quantify its normalized hull margin as in(3).

As a second quantitative caution, if a finite family of zero-class-preserving words with c_w!=0 is strictly legal at real0, its endpoints lie in N intersect I, and their neutral norms equal ||c_w||.
Formula(1) implies

    ||c_w/||c_w||^2||<=1/J(I).

Any centered ball in that particular normalized hull therefore has radius at most1/J(I).
Large legal endpoint amplitudes are not automatically cheap normalized control vectors.
This bound concerns a family legal at zero; it is not asserted for every annulus family in Section2.
It does not itself contradict the required lower margin1/(2J(I)).

### 5. Current result, unresolved gate and checking boundary

The new bridge is quantitative and conditional: ideal-preserving convex control with margin(3), plus genuine legal entry into its zero class, forces termination by exact norm isolation.
The two proved limitations are also precise: preserving all residue classes requires radius at least linear in q, and no fixed residue reset word is available.
Sparse prescribed labels retain a common real interval, but no combined residue-aware expansion theorem is supplied by that fact.

The actual-order restriction removes C435's explicit fractional class obstruction.
It does not on its own supply either missing constructive hypothesis.
The decisive next test is a completely proved finite-residue/real-overlap construction for one modulus, with all free-digit contributions and its normalized geometric margin visible.
A successful ideal-preserving finite cover with margin below(3), or a quotient path with no strict real endpoint, would not establish termination.
No broad enumeration or unsupported universal claim has been substituted for these obligations.

The original reuse screen read L176/L180's normalized descent, sparse free-slot proof and exact real conventions; L183's quotient connectivity and fractional-module scope; and the coefficient-box infinitude mechanism retained in L170.
The present residue-class count adapts that coefficient-box mechanism while keeping distinct classes modulo q; its statement and constants are proved here.
All new steps use elementary integer norm, finite group indices, real lattice packing and the fixed binary interval lemma.
No new external source, program or J is a premise.
The coordinator supplied the research questions and received checkpoints, but none of these derivations.

## Exact original history and present remaining obligations

The original structural author supplied these ideal, residue-count and automaton deductions.
The coordinator supplied the research questions and received checkpoints/progress summaries, without a retained description establishing their actual initial mathematical contents.
L187 retains the original whole check's exact frozen input, date, positive verdict and source/contribution boundaries, while R660 compares that entire historical scope.
Its unestablished initial relationship remains unknown as a historical fact.
The original listed author check is retained separately at day precision and is not enlarged into a whole original author-review event.
The original coefficient-box mechanism is reused, while the present distinct-residue constants and full lattice packing proof are local and complete.
No new source, program, native run or execution state is introduced.
The future construction/test proposal remains historical exploration; this mathematical retention does not select a Task or resume research.
