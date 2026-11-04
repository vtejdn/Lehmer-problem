---
author: Yin
---
# From almost-positive Gram certificates to actual integer-input structure

Date: 2026-10-14T20:15.
Human author Yin.
Continuing F0010-inspired research under the unchanged active G0001 goal.

## Responsible question

The adopted C110 v2 supplies a valid almost-positive lower certificate and exact arithmetic precision costs, but no automatic input-uniform objective gain.
Seek a substantive bridge to ACTUAL varying-degree integer polynomials: a new structural condition that forces usable certificates, a sharper error mechanism exploiting original arithmetic, a constructive discriminator on a genuinely changing family, or a different justified leap from the single-Haar formula.
Start from the exact existing material so that direct substitutions of C110, the fixed quartic alone, or another free-denominator approximation are not mistaken for progress on this missing bridge.
Positive and negative routes to the original unrestricted objective both remain available.

## Current investigation

The f_unitary_scope AI authors this continuation after completing C109 review.
Root supplies direction only.
Develop substantial mathematics and useful failures directly here, with actual inputs, all quantifiers and costs.
Native mathematical experiments require a separately declared responsible J before execution; no numerical scope is preauthorized by this paragraph.

<a id="all-place-regularization-reuse"></a>
## 1. Exact reuse, the genuinely changed step and contribution history

The author read the actual adopted [C110 v2](Yin_C_G0110_v2.md#statement), including its explicit negative-eigenvalue guard in the supplemental characteristic-polynomial comparison.
The initial attempt was to improve the regularization exponent by nearest-root geometry and integer discriminants.
A broader corrected local search found [L361](../ledger/Yin_L_G0361_v1.md#global-simple-circle-error), its [complete discriminant cofactor calculation](../ledger/Yin_L_G0361_v1.md#derivative-discriminant-cost), [L366's reciprocal pair improvement](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error), and [L358's exact one-root integral](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error).
These were then read in full at the used scope.
The squarefree linear regularization exponent, nearest-root method, one-root integral and cofactor estimate are ALREADY retained mathematics and are credited as such.

The change below is to select the nearest root among ALL complex roots, or among ALL trace roots in the reciprocal case, including the off-circle embeddings.
This removes the preceding separate radial-distance factor, at the precisely displayed cost of summing all original derivative terms.
The actual Vandermonde mechanism remains the one attributed and checked in [Smy08-U003](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation); it is not claimed as a new discriminant theorem.
The original reciprocal trace identity is the [C243 interface](Yin_C_G0243_v1.md#reciprocal-trace-domain), without replacing the original determinant.
The finite Gram/Jensen interface is [C_F6](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp), with its use in C110.
The proposed refinement of the correction matrix is proved below rather than inferred from a solver.
The applicable [R188](../audits/reviews/Yin_R_G0188_v1.md#whole-derivative-error-finding) and [R189](../audits/reviews/Yin_R_G0189_v1.md#trace-pair-complete-review) were read for the inherited proof/source and original-control scope; their findings do not review the changed argument here.

Root pointed to [C27's fixed-support/denominator coupling](Yin_C_G0027_v1.md#statement), which led the author to read its complete source scope, [DS17-U001](../audits/literature/DS17/Yin_U001.md#ds17-u001), the adjacent accepted sparse-height scope, and [L358's sparse-error comparison](../ledger/Yin_L_G0358_v1.md#single-haar-moment-lower-certificate).
DS17 ALREADY gives a positive gap for every fixed coefficient count; no new fixed-support gap is asserted here.
L358 already specializes [BGMP24-U001](../audits/literature/BGMP24/Yin_U001.md#bgmp24-u001) to a degree-independent exponent at fixed support, with its source-proof limits.
That fact is comparison, not an ingredient in the new local proofs.
Root's input was this reuse reminder and the responsible question, not any new estimate or proof step.

The author previously contributed to C103/C107/C110.
This is new AUTHOR work, not an independent review of those inputs.
All new derivations, constants, sparse obstruction and control below are the f_unitary_scope author's contributions.
There is no mathematical program, numerical scan, new source theorem or source acquisition.
A bounded local search found the exact antecedents just identified; no historical novelty claim follows.

<a id="statement"></a>
## Exact theorem statement

Write

    E_rho(P)=(1/2)integral_T log(1+rho^2/|P|^2), rho>=0,

with normalized Haar measure and E_0=0.
The original total m(P)=log M(P) is used throughout, with no division by degree or matrix size.

**A. All-root error without a radial-separation factor.**
Let P be monic squarefree of degree d>=2, with distinct complex roots alpha_i, R_i=max(1,|alpha_i|).
Then for every rho>=0,

    E_rho(P)<=sum_i asinh(2^(d-2)rho/(R_i|P'(alpha_i)|))
             <=2^(d-2)rho sum_i [R_i|P'(alpha_i)|]^-1.       (1)

For a monic squarefree INTEGER P, put D=|disc P|>=1.
The same bound implies

    E_rho(P)<=K_gen(P)rho,
    K_gen(P)=2^(d-2)d(d-1)^((d-1)/2)M(P)^(d-2)/sqrt(D).    (2)

**B. All-trace-pair improvement.**
Suppose additionally P is reciprocal of degree d=2s>=4 with P(1)P(-1)!=0, so P(z)=z^s Q(z+z^-1), Q monic squarefree.
For every original root alpha define

    W_alpha=|alpha|^(s-1)/(max(1,|alpha|)|P'(alpha)|).

Then

    E_rho(P)<=sum_alpha asinh(2^(s-1)rho W_alpha)
             <=2^(s-1)rho sum_alpha W_alpha.               (3)

If P is integral this gives

    E_rho(P)<=K_pair(P)rho,
    K_pair(P)=2^(s-1)d(d-1)^((d-1)/2)M(P)^(d-2)/sqrt(D).  (4)

All original roots and all inverse pairs occur, including complex off-circle trace pairs.
No lower bound on their radial distance from the circle is required.
On genuine Salem inputs this removes the coth(m/2)^2 factor in L366's discriminant-paid envelope, rather than assuming that factor uniformly bounded.
The original degree and complete polynomial discriminant remain.

**C. A localized correction gives a true Gram certificate.**
Let Q be a real symmetric exactly same-symbol Gram of |P|^2 on the full monomial vector v_n, n>=d.
If C is real PSD, Q+C is PSD, Q00+C00>0, and

    v_n(z)^*C v_n(z)<=rho^2 for all z in T,

then

    m(P)>=(1/2)log(Q00+C00)-E_rho(P).                     (5)

Thus (2) or (4) supplies its explicitly paid error.
For an actual monic squarefree integer input and a supplied B>=1, replace M(P) in K by B and call the resulting constant K(B,D).
Without knowing whether M(P)<=B, one still has

    m(P)>=min{log B, (1/2)log(Q00+C00)-K(B,D)rho}.        (6)

For C=epsilon times the coordinate projection onto a set S, rho^2=|S|epsilon, provided Q+C is actually PSD; a small rank by itself does not justify such a correction.
For the full identity this is exactly rho^2=(n+1)epsilon, retaining C110's factor.
For B=2 and0<gamma<=1, Q00+C00>=1+gamma and rho<=log(1+gamma)/(4K(2,D)) imply m(P)>=log(1+gamma)/4.
This is a sufficient precision certificate, not automatic existence of a gain.

**D. Sparse-support obstruction and an actual varying-degree discriminator.**
Let S={n_0=0<n_1<...<n_(r-1)} have all positive pairwise differences distinct.
Let a be a real coefficient vector with every a_i nonzero, H=sum a_i^2, and suppose there is a unit-modulus vector u with sum a_i u_i=0.
For any real symmetric G on these r coordinates representing exactly |sum a_i z^(n_i)|^2, write its target gain as G00>=a_0^2+gamma, gamma>0.
If G+epsilon I>=0, then NECESSARILY

    epsilon>=[sqrt(H^2+4gamma^2)-H]/[2(r-1)]>0.          (7)

In particular the REAL PSD same-symbol fiber on S is exactly aa^T.
The bound is independent of degree and coefficient denominator.
It concerns the specified coordinate support, not the full coefficient-Gram fiber.

The actual irreducible nontorsion integer-unit family

    P_k(z)=z^(2^k)-2z-1, k>=2,                         (8)

has such a three-coordinate fiber, H6 and a_0^2=1.
Therefore every support-only Gram with G00>=3/2 has epsilon>=(sqrt(37)-6)/4.
Its full original-degree PSD capacity, however, exceeds4; full rational exact PSD Grams with objective>3/2 exist.
Thus useful certificates on these actual changing inputs must introduce coordinates beyond the original three when asking for smaller negative tolerance.
This family has M(P_k)>2, as proved below, and is an explicitly EASY discriminator, not a near-one sequence or a new sparse-gap theorem.

<a id="all-complex-root-regularization"></a>
## 2. Nearest ALL roots and the complete arithmetic bound

First recall the exact one-root calculation from L358.
For alpha in C, R=max(1,|alpha|) and t>=0,

    (1/2)integral_T log(1+t^2/|z-alpha|^2)
                              <=asinh(t/(2R)).          (9)

Here is the full normalization check.
After division by R, the circle distribution of |z-alpha|/R is |1-rz| with0<=r<=1.
For delta=t/R>0, y=r^2 and A=1+y+delta^2, put lambda=(A+sqrt(A^2-4y))/2.
The factorization into lambda times |1-(r/lambda)z|^2 shows the half-log average of the regularized square modulus is(1/2)log lambda; the unregularized average is zero.
Its derivative in y is positive, since(A^2-4y)-(A-2)^2=4delta^2>0.
Its maximum at y1 is asinh(delta/2).
At t0 both sides vanish.
This includes alpha0, circle roots and all radii without an assumed lower distance from T.

Partition T into measurable cells by a nearest root among ALL alpha_i, breaking ties in a fixed order.
On the i-th cell, for j!=i,

    |alpha_i-alpha_j|<=|z-alpha_i|+|z-alpha_j|
                     <=2|z-alpha_j|.

Consequently the exact monic factorization gives

    |P(z)|>=2^(-(d-1))|P'(alpha_i)| |z-alpha_i|.          (10)

The logarithmic error kernel is nonnegative and decreases with its denominator.
On each cell use(10), and then enlarge its integral to the whole circle.
Equation(9) gives(1).
All roots enter the sum; none has been projected onto T or omitted because its own cell might be empty.
Empty cells merely make the upper bound looser.
Squarefreeness ensures nonzero derivatives.
The argument also covers P with no circle roots; their sharper fixed-input quadratic error may be used separately but is not assumed here.

For the integer assertion, use the already retained cofactor mechanism, now at EVERY root.
The exact full Vandermonde identity and Hadamard yield

    1/|P'(alpha_i)|
       <=(d-1)^((d-1)/2)[M(P)/R_i]^(d-2)/sqrt(D).       (11)

Indeed deleting alpha_i leaves a Vandermonde whose row at alpha_j has norm at most sqrt(d-1)R_j^(d-2).
Its determinant equals sqrt(D)/|P'(alpha_i)|.
This retains the complete polynomial discriminant; no field discriminant or smaller polynomial is substituted.
Dividing additionally by R_i and summing bounds the last sum in(1) by

    (d-1)^((d-1)/2)M(P)^(d-2)/sqrt(D)
                       times sum_i R_i^(-(d-1))
       <=d(d-1)^((d-1)/2)M(P)^(d-2)/sqrt(D).

This proves(2).
Its d^((d-1)/2) and2^(d-2) costs are explicit.
Integrality supplies D>=1, not a degree-uniform cofactor bound.

<a id="all-trace-root-regularization"></a>
## 3. Nearest ALL trace roots retains every original inverse pair

The reciprocal trace representation follows by grouping the terms z^j+z^-j, which satisfy the recurrence C_(j+1)(x)=xC_j(x)-C_(j-1)(x), C_0=2,C_1=x.
Thus its Q is monic of degree s.
A repeated root of Q would make the corresponding quadratic factor repeated in P, and a trace root+/-2 would make an original endpoint root repeated; the stated squarefree and endpoint hypotheses exclude these possibilities.
Write the distinct roots of the actual trace polynomial Q as w_j, j1--s.
For z in T put x=z+z^-1 in[-2,2], and select a nearest w_j among ALL complex trace roots.
The same triangle inequality, without requiring w_j real or inside the interval, gives

    |Q(x)|>=2^(-(s-1))|Q'(w_j)| |x-w_j|.

Let alpha,alpha^-1 be the two distinct original roots over w_j, and select the nearer of this pair to z; call it alpha.
Since P(1)P(-1)!=0, the pair is distinct.
Then

    |z-alpha^-1|>=|alpha-alpha^-1|/2,
    |x-w_j|=|z-alpha| |z-alpha^-1|,
    |P'(alpha)|=|alpha|^(s-1)|alpha-alpha^-1||Q'(w_j)|.

Thus on the corresponding measurable cell

    |P(z)|=|Q(x)|
       >=2^-s |P'(alpha)| |alpha|^(-(s-1))|z-alpha|.     (12)

Extend the nonnegative integral from each cell to T and apply(9), now with t=2^s rho |alpha|^(s-1)/|P'(alpha)|.
This proves the first part of(3), and asinh t<=t proves its second part.
The complex off-circle pair is treated by its actual original roots, not by a real trace surrogate; neither a trace-degree determinant nor a trace-normalized measure occurs.

Apply(11) with d=2s.
After multiplication by |alpha|^(s-1)/R_alpha, the extra factor is

    |alpha|^(s-1)/R_alpha^(2s-1)<=1.

For an outside root it is |alpha|^-s; for an inside root it is |alpha|^(s-1).
Inverse pairs contribute these two actual terms, and circle roots contribute1.
This proves(4), including the stated d bound on the sum.
All radial factors are retained before the final upper bound; no index or reciprocal multiplicity is discarded.

For a genuine degree-d=2s Salem input, L366's DISCRIMINANT-PAID envelope is

    rho 2^(s-2)coth(m/2)^2 (d-2)
              (d-1)^((d-1)/2)M^(d-2)/sqrt(D).

The ratio of their coefficients of rho, equivalently the new envelope(4) divided by the displayed old envelope for rho>0, is EXACTLY

    [2d/(d-2)] tanh(m/2)^2.                           (13)

This compares the two bounds, not the actual errors or unbounded derivative sums.
For M<=2, tanh(m/2)=(M-1)/(M+1)<=1/3 and d>=4, so the ratio is at most4/9.
Along a HYPOTHETICAL Salem m->0 sequence, the ratio tends to0.
Neither assertion supplies such a sequence or a degree-uniform K_pair.
L383's separately paid local derivative/complement method and BGMP's sparse bound remain distinct options; no claim that(4) dominates every retained bound is made.

The actual original Lehmer data already retained in L361 are d10, sqrt(D)=36497, M<59/50, and

    8*9^(9/2)*(59/50)^8/36497<18.

The last comparison was proved there by integer arithmetic.
Therefore the cofactor factor without the leading8 is less than9/4, and(4) gives for rho>0

    E_rho(P_Lehmer)<16*10*(9/4)rho=360rho.              (14)

This improves L366's retained <25000rho envelope on that SAME original input.
For example rho=1/18000 gives error<1/50.
No individual root, new discriminant, Gram optimizer, Chebyshev moments or numerical lower certificate was computed.
Equation(14) is a newly proved error bound using old exact input data, not a new measured Mahler value.

<a id="localized-gram-correction"></a>
## 4. Correcting only a justified coefficient subspace

Let Bmat=Q+C>=0.
A real matrix factorization gives an analytic vector polynomial F with norm squared v_n^*Bmat v_n.
Projection onto F(0) and the scalar Jensen formula give

    log(Q00+C00)<=integral_T log(v_n^*Bmat v_n)
       <=integral_T log(|P|^2+rho^2)
        =2m(P)+2E_rho(P).

This is exactly the ordinary finite Gram/Jensen device, with a different certified correction matrix.
Its scalar projection is nonzero because Q00+C00>0.
Any circle zeros are integrable, and the last upper bound is positive for rho>0.
At rho0, PSD C and its vanishing symbol force C0, and the standard unregularized bound applies.
This proves(5).

For integer P either M(P)>B, giving m(P)>log B, or M(P)<=B, permitting the monotone replacement of M by B in(2)/(4).
These disjoint branches prove(6).
For B2 and gamma<=1, the desired log(1+gamma)/4 is less than log2, and the stated precision makes the error at most that quarter-log.
This proves the sufficient positive certificate without presupposing the unknown small measure.

The correction epsilon times a coordinate projection has EXACT symbol |S|epsilon since every selected monomial has unit modulus.
This includes sparse embedded matrices when their omitted rows and columns are zero.
It is not valid merely because the negative part has low rank: its negative eigenspace need not be contained in those coordinates.
Likewise epsilon times an arbitrary rank-r projection has symbol v^*Pi v, whose supremum need not equal r; one must supply the actual bound.
No automatic sparse repair is inferred.

For reference, with the full correction and B2 the general sufficient tolerance is

    epsilon <= D [log(1+gamma)]^2 /
       [16(n+1)d^2 2^(4d-8)(d-1)^(d-1)].              (15)

The reciprocal paired version replaces2^(4d-8) by2^(3d-6).
These follow by squaring the actual constants, not by dropping original degree.
For fixed gamma and n comparable to d, using only D>=1 the logarithm of this sufficient tolerance is -d log d-O(d), whereas C110's particular coarse sufficient tolerance has logarithm -4d log d-O(d).
This is a comparison of two PROVED sufficient bounds, not a lower bound on true numerical complexity or an automatic gain construction.
The integer/rational coefficient costs of constructing Q remain separate.

<a id="support-only-gram-precision-obstruction"></a>
## 5. Why a small original support does not automatically provide a small correction space

Assume the exact support hypotheses in D.
All positive exponent differences are distinct, so each nonzero lag equation contains only ONE off-diagonal entry of G.
It forces G_ij=a_i a_j for i!=j.
The lag-zero equation is traceG=H.
Therefore

    G=aa^T+diag(delta_0,...,delta_(r-1)),
    sum_i delta_i=0.                                    (16)

The supplied unit-modulus vector u has a^T u=0.
Hence Gu=diag(delta)u and u^*Gu=sum delta_i=0.
If G were PSD, this zero quadratic value would force Gu0, so every delta_i=0.
This proves the precise REAL singleton fiber, not merely a rational ceiling.
Conversely aa^T is manifestly feasible.

For epsilon>=0 with Bmat=G+epsilon I>=0, its trace is H+r epsilon.
A PSD matrix has operator norm no larger than its trace, so

    ||Bmat u||^2 <=(H+r epsilon)u^*Bmat u
                  =(H+r epsilon)r epsilon.

The left side is sum_i(delta_i+epsilon)^2=sum delta_i^2+r epsilon^2.
Thus

    sum_i delta_i^2 <= rH epsilon+r(r-1)epsilon^2.       (17)

If delta_0>=gamma>0, the other r-1 real deltas sum to-delta_0, so Cauchy--Schwarz gives sum delta_i^2>=r gamma^2/(r-1).
Substitution into(17) and solving the quadratic in epsilon prove(7).
A unit-phase zero with all a_i nonzero requires r>=2, so the denominator r-1 is legitimate.
This proof covers rational or irrational G and every coefficient denominator.
Negative rank is not substituted for a bound on its magnitude.

The phase vector is an explicit hypothesis, not an arbitrary claim that the ORIGINAL univariate P has a circle root.
It can be an independent phase assignment which is not of the form(1,z^(n_1),...).
That difference is the mechanism: absence of additive collisions makes the restricted lag equations encode a larger phase model than the original univariate curve.
A PSD identity must respect its phase zeros, even when the original polynomial is zero-free on T.
No general polygon-closure theorem is needed for the explicit control below.

<a id="changing-integer-input-support-discriminator"></a>
## 6. Actual increasing-degree irreducible units which require extra coordinates

Take d=2^k, k>=2, and P_k=z^d-2z-1.
The support0,1,d has three distinct positive differences1,d-1,d.
Its vector a=(-1,-2,1) and u=(1,-1,-1) satisfy a^T u0, and H6.
This u is NOT the univariate evaluation vector at z=-1, since d is even.
Thus(7) with gamma1/2 gives the exact lower tolerance(sqrt(37)-6)/4 for every3-by-3 same-symbol Gram of objective at least3/2, independently of k and its denominator.

These are ACTUAL minimal polynomials, not a reducible sparse surrogate.
Substitute z=x+1.
Modulo2, iteration of(a+b)^2=a^2+b^2 gives(x+1)^d=x^d+1; hence P_k(x+1)=x^d modulo2.
Its integer constant is P_k(1)=-2, not divisible by4.
A hypothetical rational factorization of its monic form gives monic integer factors by the usual primitive-polynomial denominator clearing.
Reduction modulo2 forces both positive-degree factors to be powers of x, so both integer constants are even; their product would be divisible by4, contradiction.
This is the standard Eisenstein-at2 argument, reproduced fully.
Therefore P_k is irreducible of its ORIGINAL degree d.
Its constant-1 makes its roots algebraic units.

There is a real root in(-1/2,0): the values are P_k(0)=-1 and P_k(-1/2)=2^-d>0.
Call its modulus r<1/2.
The product of the moduli of ALL roots is1.
Consequently the product of the outside moduli is the inverse product of all inside moduli, and is at least1/r>2.
Thus M(P_k)>2.
This proves nontorsion and the claimed easy-range boundary without a root-count theorem, Selmer irreducibility theorem, a root scan or a numerical measure.
The growing original degree is exact; no smaller factor or powered field is substituted.

P_k also has no circle root.
If |z|=1 and P_k(z)=0, then2z=z^d-1.
Equality in |z^d-1|<=2 forces z^d=-1, and then z=-1.
But d is even and(-1)^d=1, a contradiction.
Hence min_T |P_k|>0 for every fixed k, with NO uniform minimum asserted.
The full same-symbol Gram fiber has a strictly positive definite point: choose eta>0 small enough that |P_k|^2-(d+1)eta is positive on T, take its real scalar spectral-factor Gram, and add eta I.
The scalar factorization is the same accepted one-variable finite interface as C_F6/C34; it is not a multivariate factorization assertion.

C_F6 gives a full PSD maximizing Gram of value M(P_k)^2>4.
It is real: complex conjugation preserves the real-coefficient feasible problem and objective, so its proved unique maximizing matrix equals its complex conjugate.
Interpolating it with that strictly positive definite feasible point retains objective>3/2 for a sufficiently small interpolation fraction.
C34's exact rational affine correction then approximates that interior matrix closely enough to preserve strict positivity and objective>3/2, while satisfying every original lag exactly.
Thus full RATIONAL PSD certificates with this gain really exist for every k.
No efficient denominator, explicit entries or uniform spectral margin has been claimed.

The support-only obstruction and this full feasibility coexist on the SAME actual minimal polynomial.
Any full exactly same-symbol matrix with Q00>=3/2 and tolerance smaller than(sqrt(37)-6)/4 must have at least one nonzero row or column outside{0,1,d}; otherwise its principal3-by-3 block contradicts(7).
This is a genuine coordinate-enlargement requirement, not a coefficient-denominator obstruction.
It does NOT yet give a lower bound tending to infinity on the number of added coordinates, and no such bound is inferred.

For comparison, the known local reciprocal family z^(2r)-4z^r+1, r a power of2, is already retained in [C393](Yin_C_G0393_v1.md#irreducible-radical-cokernel-control), with original L9/L364 inputs and has constant total measure2+sqrt3.
Reusing that family as a new varying-degree gap would add no result.
The present control instead exhibits the false support-only shortcut for a different actual primitive exponent pattern.
Its M>2 status and DS17's already established fixed-support gap mean it is a method discriminator, not progress by itself on the small reciprocal hard core.

<a id="all-place-regularization-outcome"></a>
## 7. What the bridge supplies and what it does not

The actual improvement for the original reciprocal hard core is the all-trace-root estimate(3)--(4), which pays every original derivative and discriminant but needs no separate distance of the exterior roots from T.
It can therefore be inserted into almost-positive certificates without already knowing a lower bound for the very m under investigation.
In a small-measure branch M<=2, its full finite constant is explicit from original d,D.
The actual Lehmer control reduces the retained regularization envelope to360rho; it is a useful calibration of that changed estimate and no newly executed lower certificate.

The original degree-dependent cost survives.
Even the sufficient precision in(15), improved from the particular C110 bound, does not force an input-uniform gain.
C_F6's real optimum equals M(P)^2, so free access to an increasingly accurate optimizer would only reproduce the unknown measure.
A genuine universal argument still needs an arithmetic/structural mechanism producing a fixed gain together with the required finite precision, or a different correctly directed norm-income argument.
Neither a large discriminant alone nor a small number of negative directions supplies this.

The correction-space theorem isolates a legitimate way to reduce the factor(n+1), while the explicit support-only obstruction shows why this cannot be done simply by retaining the original nonzero coefficients.
All its phases, exact lag uniqueness, trace, denominator-independent error floor and actual original-degree realization are explicit.
Fixed-support positivity is already known from DS17 and is not reintroduced as a new uniformity claim.
The full rational feasibility of the control is an existence interface with C34/C_F6, not a hidden computation or an assertion of useful uniform denominators.

The useful initial failed direction is preserved in Section1: the squarefree linear error and cofactor estimate were initially rediscovered, then correctly identified as L361/L366 ancestry.
The genuinely changed argument includes ALL trace roots and their normalization, and the new support obstruction is a separate proof.
No fixed target version or native program was edited by this author.

<a id="all-place-regularization-author-freeze"></a>
## 8. Complete author check and freeze

2026-10-14T20:29.
The author freezes the ENTIRE actual body: responsible question, exact reuse/contribution history, StatementA--D, Sections1--7 and equations(1)--(17).
The whole self-check covers the normalized one-root integral at all complex radii including0; measurable nearest-root ties and empty cells; every original reciprocal pair and complex trace root; the |alpha|^(s-1)/max(1,|alpha|) factor; all cofactor exponents and the full polynomial discriminant; rho0 versus strict positive-rho controls; the exact old-envelope ratio and Lehmer arithmetic; PSD correction versus arbitrary rank, actual correction symbols and the unknown-measure branch; every sparse lag and complex phase, the trace/PSD norm inequality and quadratic root; shifted Eisenstein, actual minimal degree/unit/nontorsion, the original full product of moduli, zero-free circle check and real/rational full-fiber feasibility.
The fixed-support gap and sparse error remain expressly credited prior inputs, and the easy M>2 control is not promoted into the hard core.

The scoped material check passed before this final paragraph and is repeated on the frozen body.
No program, numerical root or discriminant run, optimizer, explicit rational Gram output, new source adoption or fresh finite Mahler certificate was performed.
All mathematical conclusions are the displayed proofs and stated reused interfaces.
This is AUTHOR checking only; independent review and any fixed adoption belong to root's separately arranged next step.

## Fixed organization

The ENTIRE author-frozen body is retained above: responsible question, all initial rediscovery/reuse and contribution disclosures, Statement A--D, full Sections1--8/equations1--17, every source/interface limit and actual easy-family boundary.
Root supplied direction and reuse reminders only, not a new proof step.
Direct retention awaits a separate actual whole review.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:31 |
| status | open |
| reason | Preserve the all-original-root/trace-pair regularization, complete arithmetic costs, localized PSD correction and exact support obstruction/control for independent whole review. No automatic uniform gain, newly proved sparse gap or unrestricted Mahler conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Complete regularization and correction argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Inherited derivative-discriminant mechanism](../ledger/Yin_L_G0361_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Earlier reciprocal pair error](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Original one-root error](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact scalar Gram capacity](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Rational affine correction](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Prior almost-positive certificate](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:44 |
| status | proved |
| reason | Select the adopted complete C_F6/C_F7/C_F8 responsible homes, as applicable below, for the unchanged retained scalar finite Gram maximum and uniqueness. The actual selected adoptions and complete needed interface sections were read and matched to the original fixed L_F5/L_F6/L_F7 text. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; this is current proof-location maintenance with no new mathematical or independent review. Original dated decisions and all R bindings keep their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Complete regularization and correction argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Inherited derivative-discriminant mechanism](../ledger/Yin_L_G0361_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Earlier reciprocal pair error](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Original one-root error](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact scalar Gram capacity](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Rational affine correction](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Prior almost-positive certificate](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |

### Decision current-complete-root-error-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:22 |
| status | proved |
| reason | The unchanged complete all-root product and normalized scalar bound is now owned by C379, including its nonmonic, repeated-root, circle-zero and actual Mahler-scale cases. Retain the current statement, full argument, every other input and actual existing review scopes; the old reviewers are not described as having inspected this later proof-home placement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Exact argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Exact dependency](../ledger/Yin_L_G0361_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Exact dependency](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Exact dependency](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Exact dependency](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Exact review](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |


### Decision current-complete-derivative-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:09 |
| status | proved |
| reason | The complete original derivative-discriminant proof now belongs to C384 at the same exact cofactor capability. Retain the unchanged current statement, full argument, every other dependency and actual selected review scope; old readings and R bindings keep their original L361 input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Exact argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Exact dependency](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Exact dependency](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Exact dependency](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Exact dependency](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Exact review](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |


### Decision current-complete-trace-pair-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:41 |
| status | proved |
| reason | Use the complete exact original reciprocal trace-pair theorem at its actual current C395 mathematical home. The statement, proof, every other selected field/relation/review/scope and all historical input facts are retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Exact argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Exact dependency](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Exact dependency](Yin_C_G0395_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Exact dependency](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Exact dependency](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Exact review](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:39 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. All-root and all-trace-pair regularization, full discriminant and degree prices, localized PSD correction, sparse-support tolerance floor and the actual changing-degree easy-family discriminator are supported at their exact hypotheses. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Exact argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Exact dependency](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Exact dependency](Yin_C_G0395_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Exact dependency](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Exact dependency](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0113-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:35 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt complete independent [R797 original all-root-regularization](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) review of actual A--D and the entire retained body. All-root/trace-pair regularization removes the separate radial-separation cost while retaining original degree/discriminant expenses; localized corrections and the actual sparse-support obstruction/control hold at their precise scope. Automatic uniform gain and the unrestricted Mahler objective remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, all degree/squarefree/reciprocal/integer/support and phase guards. |
| argument | [Complete regularization and correction argument](#all-complex-root-regularization) | Full Sections2--8/equations1--17, nearest original roots and trace pairs, discriminant costs, corrected Grams, support obstruction and actual irreducible control. |
| dependency | [Inherited derivative-discriminant mechanism](../ledger/Yin_L_G0361_v1.md#derivative-discriminant-cost) | Exact polynomial discriminant cofactor interface and retained actual Lehmer data, locally rederived at every root. |
| dependency | [Earlier reciprocal pair error](../ledger/Yin_L_G0366_v1.md#reciprocal-trace-pairing-error) | Exact older genuine-Salem discriminant-paid coefficient for the stated comparison, not a bound on every near-one input. |
| dependency | [Original one-root error](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Prior normalized scalar integral; fully rederived for all complex radii. |
| dependency | [Exact scalar Gram capacity](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Same-original-symbol finite PSD maximum, vector Jensen mechanism, scalar factorization and uniqueness used in the actual full-fiber control. |
| dependency | [Rational affine correction](Yin_C_G0034_v1.md#statement) | Exact rational approximation inside a strictly positive real same-symbol fiber for each actual control polynomial. |
| dependency | [Prior almost-positive certificate](Yin_C_G0110_v2.md#statement) | Exact coarse sufficient precision for the explicit cost comparison; not an automatic gain input. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0797_v1.md#all-root-regularization-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |
