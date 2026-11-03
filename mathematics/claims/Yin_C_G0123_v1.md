---
author: Yin
---

# Trace-residual primal construction with relative-symbol correction

Date: 2026-10-15T07:12.
Human author Yin.
The strategy_critique AI authors this continuation under the unchanged G0001 contract and the resumed shared execution period.
Root supplied the direction to enlarge the admission class beyond C122, not a proof step.
Root owns execution, Task, strategy, navigation and fixed decisions.

## Responsible question

Can the explicit-factor/exact-symbol-repair/corrected-income mechanism admit original reciprocal integer inputs outside C122's known fixed-gap seed family, without assuming a fixed exterior-root gap?
Seek a genuinely different correction or admission mechanism with explicit original degree, coefficient field, norm, denominator and regularization expenses.
A computable sufficient criterion is not unrestricted near-one coverage; a varying small parameter must not be replaced by a fixed positive gain.

## Starting inputs and bounded reuse

Read the actual adopted C122 and R476, C110 v2, C113's localized correction, C120 and C103's quadratic seed identity at their exact domains.
The known C122 family and its already positive class gap are not new results to repeat.
A targeted local search for central residuals, trace-polynomial division, relative-symbol PSD corrections and general seed constructions found no prior statement for the candidate below.
L174 supplies a separate plastic-seed Salem family and fixed-seed phase mechanism, a possible later discriminator rather than a premise for the initial algebra.
The elementary square completion and symmetric polynomial division below use existing finite Gram/Jensen conventions; no new general factorization theorem is assumed.
No native mathematical program is proposed.

## First candidate retained before further development

For an original monic reciprocal P(z)=z^h T(z+z^-1), choose a SUPPLIED rational b>1, s=b+b^-1, and delta=T(s).
The symmetric quotient C_b=(P-delta z^h)/(1-sz+z^2) is an explicit rational polynomial with original width d-2 and constant1.
The known quadratic seed g_b=b-2z+b^-1 z^2 has the same circle modulus as1-sz+z^2.
Thus the coefficient outer product of C_b g_b is a PSD Gram of the approximate symbol |P-delta z^h|^2 and objective b^2.

Let p be the original coefficient vector, e the central coordinate vector, and u>0 rational.
The exact-symbol matrix and a rank-at-most-two PSD correction can be chosen as

    Q=(coeff(C_b g_b))(coeff(C_b g_b))^T
                     +delta(p e^T+e p^T)-delta^2 e e^T,
    R=(delta^2/u)pp^T+(u+delta^2)ee^T.

Then Q has EXACT symbol |P|^2, while Q+R is PSD by one explicit square completion.
Its corrected symbol is exactly

    (1+delta^2/u)(|P|^2+u).

The resulting normalized objective is (b^2+delta^2/u)/(1+delta^2/u).
This retains correction terms relative to the ORIGINAL symbol instead of paying a generic N epsilon I.
All algebra, costs, valid regularization bounds, delta0, possible positive margin and near-one limitations remain to be developed and checked below.
No complete new theorem or unconditional coverage is asserted at this stage.

<a id="relative-correction-first-complete-calculation"></a>
## 1. Exact calculation of the relative-symbol repair

Let P be monic real reciprocal of degree d=2h>=2 with constant1.
The standard original trace identity from L66 is P(z)=z^h T(z+z^-1), with T monic real of degree h (integral if P is integral).
For a supplied b>1, set s=b+b^-1 and delta=T(s).
Divisibility of T(X)-T(s) by X-s gives

    C_b(z)=z^(h-1)[T(z+z^-1)-T(s)]/[z+z^-1-s],
    P-delta z^h=(1-sz+z^2)C_b.

The displayed C_b is a reciprocal ordinary polynomial of degree d-2 and constant1.
It can equivalently be computed by the lower-half recurrence c0=1, c_k=p_k+s c_(k-1)-c_(k-2) for k<=h-1 and reflection c_k=c_(d-2-k); this is explicit in P and b, not an unknown factorization of P.
Put f=coeff(C_b(b-2z+b^-1 z^2)), p=coeff P and e=e_h.
The quadratic identity in C103 gives |f(z)|^2=|P-delta z^h|^2 and f0=b.

For u>0 let a=delta^2/u.
The exact same-symbol Q and PSD R in the initial candidate satisfy the matrix identity

    Q+R=ff^T+(delta/sqrt(u) p+sqrt(u)e)
                         (delta/sqrt(u) p+sqrt(u)e)^T.

Its second outer product can be stored rationally as a pp^T+delta(pe^T+ep^T)+u ee^T when the data are rational; no irrational square root is a coefficient-field premise.
On the circle,

    v^*Rv=a|P|^2+u+delta^2,
    v^*(Q+R)v=(1+a)(|P|^2+u),
    (Q+R)00=b^2+a.

With E_P(rho)=(1/2)integral log(1+rho^2/|P|^2)dmu, the finite PSD vector/Jensen argument therefore gives the ACTUAL lower certificate

    m(P)>=[1/2]log[(b^2+a)/(1+a)]-E_P(sqrt(u)).

This includes circle roots with their usual integrable logarithms.
For delta!=0, the particularly simple rational choice u=delta^2 gives

    R=pp^T+2delta^2 ee^T,
    Q+R=ff^T+(p+delta e)(p+delta e)^T,
    m(P)>=[1/2]log[(b^2+1)/2]-E_P(|delta|).       (A)

The correction need NOT be small in operator norm: its original coefficient-energy part is retained.
Its analytic expense is handled by the exact multiplicative factor2, not discarded.
This is the changed mechanism compared with the scalar isotropic repair of C122.
For delta0, the uncorrected ff^T already has exact symbol and gives m(P)>=log b.
On original monic integer constant1 inputs, a rational b>1 cannot have delta0 by the rational-root theorem.

The construction applies beyond Salem inputs to every original monic reciprocal real polynomial of even degree with constant1.
Positive remaining income requires a paid bound for E_P(|delta|).
It does not follow merely from choosing b>1.

<a id="input-only-salem-construction-candidate"></a>
## 2. Candidate complete admission algorithm for the actual Salem class

The new repair suggests a concrete enlargement from C122's family to ALL actual monic irreducible Salem inputs, with degree-dependent costs and no fixed root gap.
The following candidate is being checked before final statement/freeze.

For d=2h, H1=sum|p_j|, use B=H1+1 as a known upper bound for the exterior root lambda.
At a genuine Salem input, the full integer value P(1) is nonzero and

    1<=|P(1)|<=[(lambda-1)^2/lambda]2^(d-2),

so lambda-1>=2^(1-h).
This is an elementary DEGREE-DEPENDENT separation, not a uniform gap.
Let eta=2^-h.
The C113 all-trace-pair regularization bound, with original M(P)<=B and disc(P)>=1, permits the explicit integer overestimate

    K=2^(h-1)d(d-1)^h B^(d-2),
    E_P(rho)<=K rho.

On the real interval[1,B], a derivative bound is D=d H1 B^(d-1).
An exact dyadic bisection of P between1 and B can choose a rational LOWER endpoint b satisfying

    0<lambda-b<=eta/(16KD),
    b-1>=eta,
    |delta|=|P(b)|/b^h<=eta/(16K).

Only polynomial signs and supplied integer quantities enter the algorithm; lambda appears in the verification, not as an input.
Formula(A) would then have positive remaining income at least eta/8 and, by b>=(lambda+1)/2 and the arithmetic-geometric mean, at least one eighth of the ACTUAL m(P).
The complete endpoint, exponent, operation/bit and rational-precision bounds are still being checked.
This is a proposed input-only construction of a paid per-input certificate, not a uniform gap and not a claimed efficient admission test for determining whether an arbitrary input is Salem.

<a id="statement"></a>
## Statement: exact rational relative repair and coefficient-defined admission

All Haar integrals below have total mass1, v_d(z)=(1,z,...,z^d)^T, and m(P)=integral log|P| is the TOTAL original logarithmic Mahler measure.
No degree or rank normalization is made.

**A. Explicit rational construction on a supplied scalar test.**
Let P in Q[z] be monic reciprocal of degree d=2h>=2 with P(0)=1.
For any SUPPLIED rational b>1, set s=b+b^-1, delta=b^-h P(b)=T(s), and form the rational quotient and coefficient vectors

    C_b=(P-delta z^h)/(1-sz+z^2),
    f=coeff[C_b(b-2z+b^-1z^2)], p=coeff P, e=e_h.

They all use the ORIGINAL coefficient window0,...,d.
If delta!=0, define

    Q=ff^T+delta(pe^T+ep^T)-delta^2 ee^T,
    R=pp^T+2delta^2 ee^T,
    B=Q+R=ff^T+(p+delta e)(p+delta e)^T.          (1)

Then Q has EXACT circle symbol |P|^2, R and B are rational PSD, Q00=b^2, B00=b^2+1, rank R<=2, rank B<=2, rank Q<=3, and Q has at most one negative eigenvalue.
Moreover

    v_d^* B v_d=2(|P|^2+delta^2),
    m(P)>=L(b)-E_P(|delta|),
    L(b)=(1/2)log[(b^2+1)/2],
    E_P(rho)=(1/2)integral log(1+rho^2/|P|^2).   (2)

Any proved upper bound E_P(|delta|)<=e_P therefore gives the actually checkable remaining income L(b)-e_P.
For general rational u>0, the same Q with

    R_u=(delta^2/u)pp^T+(u+delta^2)ee^T

satisfies Q+R_u>=0 and yields

    m(P)>=(1/2)log[(b^2+delta^2/u)/(1+delta^2/u)]
                                -E_P(sqrt(u)). (3)

If delta0, ff^T is already exact PSD with objective b^2, giving m(P)>=log b.
A rational b>1 cannot have delta0 when P is monic integral with constant1.
These are explicit formulas, not a request to approximate an unknown maximizing matrix.

**B. A finite coefficient-only admission algorithm.**
Suppose in addition P is INTEGER, squarefree, d=2h>=4, P(-1)!=0 and P(1)<0.
No irreducibility, Salem classification or fixed exterior-root separation is assumed.
Put

    H1=sum_(j=0)^d |p_j|, B0=H1+1,
    eta=1/[2(B0+1)^(d-1)],
    K=2^(h-1)d(d-1)^h B0^(d-2),
    D=d H1 B0^(d-1),
    k=min{k>=0:2^k>=16KD(B0-1)/eta}.             (4)

Perform exactly k rational sign bisections of [1,B0], retaining P(left)<0<P(right), and let b be the final LOWER endpoint.
Then b is rational, b>1, delta!=0 and

    |delta|<=eta/(16K), b>=1+eta,
    E_P(rho)<=K rho for every rho>=0.            (5)

The rational matrices(1) therefore have certified positive remaining income

    m(P)>=L(b)-K|delta|>=3eta/16>0.              (6)

All checks and construction inputs are original integer coefficients and the specified finite bisection.
Neither an exterior root nor an algebraic trace value is supplied to the algorithm.
The rational floor3eta/16 requires no numerical logarithm evaluation.
The same conclusion applies to the coefficient-defined branch P(-1)<0, P(1)!=0 after the explicit sign substitution z->-z and diagonal sign conjugation of the output matrices.

**C. Coverage and relative income on every actual positive Salem input.**
Every original monic irreducible positive Salem polynomial belongs to B's class.
If lambda>1 is its exterior root, the algorithm in B produces b satisfying b>=(lambda+1)/2.
Its EXACT remaining-income expression obeys

    L(b)-K|delta| >= (3/16)log(lambda)
                    =(3/16)m(P).              (7)

Lambda is used only to prove this comparison, not as an algorithmic input.
On this actual Salem class Q has EXACTLY one negative eigenvalue; its positive objective does not contradict the rational exact-PSD ceiling.
No absolute positive margin independent of P is supplied: along a hypothetical Salem sequence m(P)->0, b<lambda->1 and the raw objective b^2 also tends to1.
Complete admission of this class at a varying positive income is distinct from the uniform-income requirement of G0001.

**D. All original arithmetic and finite costs.**
For the INTEGER-input algorithm in B and its specialization C, write the output b=a/c with positive integers a,c, taking c=2^k if desired without reduction.
Then

    q=(ac)^d                                             (8)

is an explicit clearing denominator for Q,R,B in(1).
It is not asserted least.
The quotient and f have coefficient denominators dividing(ac)^h, delta also has denominator dividing(ac)^h, and the PSD factorizations in(1) are over Q with no number-field root or irrational square root.
If L0=log2(2dH1), the specified k is O(dL0); cleared entries have O(d^2 L0) bits.
A dense full original-width presentation uses O(d^4 L0) bits and can be constructed with conservative O(d^6 L0^3) bit work using exact integer Horner evaluation and schoolbook arithmetic.
These bounds include the finite sign search, scalar residual evaluation, rational factor construction and dense matrices, but do not claim optimality or a new general root-isolation algorithm.
Squarefreeness/reciprocity and the two endpoint conditions are the theorem's explicit input guards; no Salem recognition procedure is assumed.

This is a concrete enlargement of C122's certificate admission from one already fixed-gap family to the stated coefficient class, including ALL original positive Salem inputs.
It does not improve the elementary number-theoretic gap already implied by the sign-change/root argument.
Its new content is the explicit small-rank rational same-symbol primal construction, relative-symbol correction and complete finite costs.
No unrestricted positive Mahler gap, counterfamily or Task completion follows.

<a id="argument"></a>
## Complete argument for the final statement

<a id="trace-residual-exact-factor-and-psd-repair"></a>
### 3. Exact symmetric division and relative correction

The original trace identity is the elementary reciprocal part of [C243](Yin_C_G0243_v1.md#reciprocal-trace-domain), with no field-degree conclusion needed here.
For completeness, define X=z+z^-1 and C_0(X)=2, C_1(X)=X, C_(j+1)=X C_j-C_(j-1).
Then C_j(X)=z^j+z^-j, and

    T(X)=p_h+sum_(j=1)^h p_(h+j) C_j(X)

is monic of degree h with P=z^h T(X).
Its coefficients are rational or integral with those of P.
The divided difference [T(X)-T(s)]/(X-s) is a polynomial of degree h-1.
Multiplication by z^(h-1) gives a reciprocal ordinary polynomial of degree d-2, constant and leading coefficient1, and exactly the C_b in A.
This proves division is exact.
The lower-half recurrence in Section1 and reflection are an explicit alternative construction requiring no factorization of P.

On the circle the supplied quadratic g_b=b-2z+b^-1 z^2 has the same modulus as1-sz+z^2.
This is the elementary identity already used in [C103](Yin_C_G0103_v1.md#explicit-salem-trace-field-certificates), now at the SUPPLIED s rather than the unknown trace of P.
Thus the vector f has symbol |P-delta z^h|^2 and f0=b.
Reciprocity gives z^-h P real on the circle, so

    |P|^2-|P-delta z^h|^2
         =delta(z^-h P+z^h conjugate(P))-delta^2.

The last expression is exactly the symbol of delta(pe^T+ep^T)-delta^2 ee^T.
Hence Q has exact symbol, Q00=b^2, and the rank bound follows from range Q being contained in span{f,p,e}.
On the codimension-one subspace e^T x=0 its quadratic form is (f^T x)^2>=0.
A two-dimensional negative subspace would intersect that hyperplane nontrivially, which is impossible; hence Q has at most one negative eigenvalue.
Expanding (p+delta e)(p+delta e)^T proves(1), with R,B explicitly PSD and of rank at most2.

For general u>0, the additional square is

    (delta/sqrt(u) p+sqrt(u)e)
                   (delta/sqrt(u) p+sqrt(u)e)^T.

This proves PSD; storing its expansion uses only rational coefficients when u,delta,p are rational.
Its total symbol is

    |P|^2+(delta^2/u)|P|^2+u+delta^2
        =(1+delta^2/u)(|P|^2+u).

The finite PSD vector/Jensen argument in [C113's correction proof](Yin_C_G0113_v1.md#localized-gram-correction) therefore gives

    (1/2)log(b^2+delta^2/u)
       <=m(P)+(1/2)log(1+delta^2/u)+E_P(sqrt(u)).  (9)

Rearrangement proves(3), and u=delta^2 proves(2).
This is an explicit adaptation of the Jensen proof, not a claim that R satisfies C113's bounded-additive-symbol hypothesis with a small uniform rho.
R contains a full pp^T term; its original coefficient norm and symbol are retained, and its multiplicative factor2 is subtracted exactly.
Circle zeros have integrable logarithms, and the regularized expression at u>0 is strictly positive.
At delta0 the unregularized finite Gram inequality directly gives the stated bound.

For monic integer P with constant1, a rational root must be an integer dividing1: writing a/c in lowest terms in its monic equation forces c1, and the constant term then forces a=+/-1.
Hence no b>1 has P(b)=0, so delta!=0 on B's class.
No unpriced limit at delta0 is needed in the algorithm.

<a id="coefficient-only-sign-search-and-error-budget"></a>
### 4. A finite sign search with every root-distance and analytic cost paid

At any root alpha with |alpha|>=1, monicity gives

    |alpha|^d<=sum_(j<d)|p_j||alpha|^j
                  <=(H1-1)|alpha|^(d-1).

Thus all original roots satisfy |alpha|<B0=H1+1.
Also the coefficient triangle inequality on the circle and the scalar Jensen formula give M(P)<=H1<B0, retaining the TOTAL product rather than only the house.
For real x=B0,

    P(B0)>=B0^d-(H1-1)B0^(d-1)>0.

Combined with P(1)<0 this gives the initial sign bracket.
For every real root lambda>1, the complete original integer evaluation supplies

    1<=|P(1)|=product_i |1-alpha_i|
       <=(lambda-1)(B0+1)^(d-1).

Therefore lambda-1>=2eta with eta as in(4).
This familiar integer-evaluation mechanism is the same full-norm principle recorded at [C107](Yin_C_G0107_v1.md#signed-norm-gap-assessment), here with ALL remaining roots bounded by B0 instead of a Salem-only circle bound.
It is an explicitly degree/height-dependent price, not a new or uniform root-gap theorem.

The all-trace-pair bound of [C113](Yin_C_G0113_v1.md#statement), equation4, applies: P is monic integral squarefree reciprocal, degree2h>=4, and P(1)P(-1)!=0.
It retains all original pairs, including complex off-circle pairs.
Using M(P)<B0, |disc P|>=1 and (d-1)^((d-1)/2)<=(d-1)^h gives the integer K in(4), so E_P(rho)<=K rho.
No trace-only norm or input-independent conditioning constant replaces that bound.

The number 16KD(B0-1)/eta is a positive integer.
Thus the declared k is obtained by its binary length and an exact power-of-two comparison; computing k does not require a numerical logarithm or root oracle.

For every x in[1,B0],

    |P'(x)|<=sum_(j=1)^d j|p_j|B0^(j-1)
                         <=dH1 B0^(d-1)=D.         (10)

No midpoint of the prescribed bisection can be a root, because it is rational and strictly greater than1.
Thus every one of the k steps retains strict opposite signs.
The final interval [b,c_right] has width

    (B0-1)2^-k<=eta/(16KD).                         (11)

It contains some real root lambda>1 by the intermediate value theorem.
Uniqueness is NOT assumed on the general coefficient class.
Every such root is at least1+2eta, so

    b>=lambda-eta/(16KD)>=1+eta.

Applying(10) between b and this root gives |P(b)|<=D(c_right-b)<=eta/(16K).
Since b^h>=1, the same bound holds for |delta|=b^-h|P(b)|.
This proves(5), including b>1 and the nonzero residual.
All quantities K,D,eta,k are computed from original coefficients before the search; no unknown root separation appears in its stopping rule.

The exact inequality (b^2+1)/2>=b gives L(b)>=(1/2)log b.
Since eta<=1 and b>=1+eta,

    L(b)>=(1/2)log(1+eta)
        >=eta/[2(1+eta)]>=eta/4.

Together with K|delta|<=eta/16, formula(2) now proves(6).
The final rational floor3eta/16 was established algebraically, not by a floating logarithm or an input's previously known Mahler value.

If P(-1)<0 and P(1)!=0, set Ptilde(z)=P(-z).
Since d is even this remains monic reciprocal with constant1, squarefree and with the same H1, M and degree.
Apply the construction to Ptilde and conjugate Q,R,B by diag(1,-1,1,...,(-1)^d).
The resulting matrices have the exact original |P(z)|^2 symbol, the same constant objectives and the same PSD/rational/bit costs.
This proves the sign-substitution assertion without changing the original determinant normalization.

<a id="all-salem-admission-versus-uniform-income"></a>
### 5. All actual positive Salem inputs, without a fixed gap

For an actual monic irreducible positive Salem P, the nonreal circle roots occur in conjugate pairs.
At1 their factors are positive squared moduli, while (1-lambda)(1-lambda^-1)<0.
Thus P(1)<0; P(-1)!=0, squarefreeness and reciprocity also hold.
Such P therefore satisfies every guard of B.
For real x>1 the circle-pair factors and x-lambda^-1 are positive, so the sole sign-changing root on this interval is its actual exterior lambda.
The final bracket therefore contains THAT lambda and has b<lambda.

The general root-distance price gave lambda-1>=2eta, while(11) gives lambda-b<=eta/(16KD)<=eta.
Hence

    b>=lambda-eta>=(lambda+1)/2>=sqrt(lambda).

Consequently L(b)>=(1/2)log b>=(1/4)log lambda.
Also K|delta|<=eta/16<=L(b)/4.
Formula(2) gives the claimed remaining income

    L(b)-K|delta|>=(3/4)L(b)>=(3/16)m(P).

This is a comparison of the constructed expression with actual m(P), not an assumption about m used by the algorithm.
The preliminary Section2 Salem-specific endpoint bound was sufficient but unnecessary; the final algorithm uses the broader coefficient-only eta in(4).
Its stronger known Salem root floor remains credited old information, not a new estimate.

The [C103 rational ceiling](Yin_C_G0103_v1.md#irreducible-all-padding-obstruction) applies to this actual irreducible integer polynomial with circle roots: a rational same-symbol PSD Gram has objective at most1.
Since Q00=b^2>1, Q is not PSD.
The at-most-one argument of Section3 therefore gives exactly one negative eigenvalue for every constructed Salem Q.
This extends the explicitly controlled negative-index construction beyond C110's fixed quartic, while preserving the actual input-dependent objective and correction costs.

Along a HYPOTHETICAL sequence of actual Salem inputs with m(P)->0, the selected b lies in(1,lambda), so Q00=b^2->1 and L(b)->0.
Thus a fixed positive fraction of each input's actual measure does not supply a fixed absolute margin.
The result admits every Salem input as a per-input finite primal certificate, including any hypothetical near-one inputs, but does not prove that those inputs cannot exist or that Salem inputs exhaust the unrestricted reciprocal hard core.
The root sign bracket alone already proves m(P)>0; the new result is its fully priced same-symbol primal realization.

<a id="relative-repair-rational-and-bit-costs"></a>
### 6. Full rational coefficient, norm and bit expenses

Take b=a/c, with positive integers a,c and c=2^k available from the exact bisection.
Then a<=B0 2^k and s=(a^2+c^2)/(ac).
The lower-half recurrence for C_b shows that its k0-th coefficient for0<=k0<=h-1 has denominator dividing(ac)^k0.
Reflection gives the same common denominator(ac)^(h-1) for the whole factor.
Multiplication by b-2z+b^-1z^2 therefore gives f with denominator dividing(ac)^h.
Direct evaluation delta=b^-h P(b), or the integral T(s), has that same denominator because d=2h.
Thus q=(ac)^(2h) clears every matrix in(1), proving(8).
No minimal-denominator assertion or free cancellation is made.

For explicit size control, use the recurrence U0=1,U1=s,U_(j+1)=sU_j-U_(j-1), whose finite-sum formula at s=b+b^-1 is U_j=sum_(r=0)^j b^(j-2r).
Since1<b<B0,

    |c_j|<=hH1 B0^(h-1) for every factor coefficient,
    |f_j|<=(B0+3)hH1 B0^(h-1)=:F0.                (12)

The proof is the lower-half convolution c_j=sum_(r=0)^j p_r U_(j-r) and reflection, exactly the coefficient mechanism used in [C117](Yin_C_G0117_v1.md#full-original-field-height-costs), without an unknown field embedding.
Also |delta|<=eta/(16K)<1, and |p_j|<=H1.
Therefore

    |Qij|<=F0^2+2H1+1,
    |Rij|<=H1^2+2,
    |Bij|<=F0^2+(H1+1)^2.                         (13)

In particular the correction norm is NOT claimed small: trace R=||p||_2^2+2delta^2.
This entire original coefficient-energy cost is kept in its matrix representation and is handled analytically by the exact relative-symbol factor in(9).

Formula(4) has log2(1/eta)=1+(d-1)log2(B0+1), log2 K=O(d(log d+log B0)) and log2 D=O(d log B0+log(dH1)).
Hence k=O(d log2(2dH1))=O(dL0).
Each rational bisection sign can be evaluated by integer Horner arithmetic for c^d P(a/c), using O(d) integer operations.
The integers have O(d(k+log B0)+log H1) bits.
Midpoint roots cannot occur on the declared domain, so there is no unaccounted equality branch or adaptive root separation query.

The quotient recurrence, scalar delta and the explicit matrices use O(d^2) further arithmetic operations on integers of the same order of bit length when normalized to the stated common denominators.
The computations of the integer constants in(4) fit within these bounds.
There are O(dk+d^2) such operations in total, each using at most O(d(k+log B0)+log H1)=O(d^2L0) bits.
Schoolbook multiplication yields the conservative O(d^6L0^3) total bit bound; exact dense matrix storage costs O(d^4L0) bits.
The symbolic two-vector representation of B and R can be stored more compactly, but this is not needed for the stated upper bounds.

All finite outputs are rational.
No native program has been run, no root-isolation software is an uncharged oracle, and no algebraic norm of an irrational Gram factor is invoked.
These are proved construction bounds, not a numerical performance claim.
The input guards can be checked separately by ordinary coefficient/reversal/gcd/sign operations; this result does not import a Salem-classification or generic algebraic-root isolation algorithm.

<a id="relative-repair-outcome-and-boundaries"></a>
## 7. Genuine changes, controls and still missing uniformity

The constant-window epsilon I repair of C122 pays the symbol expense N epsilon.
Here the exact original coefficient P supplies a rank-two correction whose relative part is exactly a|P|^2; scalar normalization removes that part only after its full cost has been recorded.
The remaining error is the original E_P(sqrt(u)).
The affine same-symbol identity, positive square completion and normalization are all necessary: simply asserting a small residual or a small correction rank would not prove(2).

The construction is not the unknown outer factor of P and not rational rounding of an unknown maximizing matrix.
It uses a supplied rational scalar b, a symmetric divided difference and explicit two-vector squares.
The finite admission procedure fixes its precision from original coefficients and uses only k exact polynomial-sign evaluations.
Its very conservative K can be replaced by a sharper ACTUALLY PROVED original regularization bound, such as a family phase bound, without changing the matrix identity; this is an allowed input substitution, not an assumed uniform estimate.

C110 already establishes arbitrary-precision rational existence from actual optimizer entries, and C103 already constructs exact algebraic trace-field certificates on each Salem input.
The new mechanism instead gives a rational coefficient-only algorithm with explicit original-width, denominator and bit costs, plus a relative-symbol correction that does not pay N times a generic eigenvalue tolerance.
It neither claims a new proof that Salem numbers have positive individual measure nor improves known number-theoretic lower bounds.
The broader negative-endpoint coefficient class need not be irreducible or Salem; its measure still means the full original product.

For a candidate b on a general reciprocal input, delta need not be small and the remaining expression can be nonpositive.
Part A is a certificate formula, not automatic admission.
Part B supplies admission exactly on its stated coefficient class; no claim is made for reciprocal inputs with both endpoint values positive, complex exterior-root configurations with no suitable real sign change, or unrestricted G0001 coverage.
The sign-substitution corollary does not remove that boundary.
Part C covers hypothetical near-one SALEM inputs only at their own vanishing positive income.
A uniform lower gap still requires a new arithmetic reason for a degree-independent positive margin, not merely this per-input computation.

The working Section2 candidate used a sharper Salem-specific root floor; the final general procedure did not need it.
This development is retained to distinguish the initial lead from the completed coefficient-defined scope.
The prior plastic-seed family remains a reuse-screen lead; no unproved phase estimate or new plastic-family theorem is a premise.
No mathematical native computation, J evidence, external source theorem or additional execution authority has been created.

<a id="trace-residual-entire-author-freeze"></a>
## 8. Complete author check and freeze

2026-10-15T07:32.
The author freezes the ENTIRE current D36 for separate actual whole review: responsible question, reuse and initial relative-repair derivation, useful sharper Salem candidate, final Statement A--D, all13 numbered formulas and the complete proofs/limits in Sections3--7.
The final actual reread rebuilt the reciprocal divided difference and both original endpoints; the exact same-symbol rank-three signed Gram; the rational two-square repair, relative symbol normalization and Jensen direction; delta0 and rational integer-root cases; every C113 all-pair hypothesis and original M bound; all-root integer endpoint expense; strict sign bisection without an unknown root or uniform gap; its dyadic onset, derivative and residual bounds; general multiple-real-root versus unique Salem scope; coefficient-defined positive floor and actual-m comparison; the at-most-one and exact-one negative-index arguments; sign conjugation; common denominator powers, all coefficient/norm sizes and every arithmetic/bit bound.
No remaining gap was found by this author check.
The source/dependency inputs are reused at the precise recorded scope and no new external theorem is invoked.
No native mathematical program or numerical spectral test was run.
Structural checking is separate from proof review.
Root supplied direction and read progress, without supplying a proof step or correction.
This freeze is not independent acceptance, a new number-theoretic lower bound, uniform-income coverage or completion of G0001.

## Fixed organization

The entire final author account is retained: initial candidate, exact relative-symbol repair, final coefficient-defined admission algorithm, full original Salem coverage at an input-dependent income, all arithmetic and bit costs, failed uniformity inference, contribution history and author freeze.
Root supplied direction only and has not supplied a proof step or correction.
Separate whole review of this actual fixed artifact is pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T07:40 |
| status | open |
| reason | Retain the exact rational trace-residual same-symbol construction and relative correction, coefficient-only finite admission on the stated endpoint class, all positive Salem inputs at their own positive income, and complete original-width arithmetic costs. No uniform Mahler gap or unrestricted admission follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full relative-repair statement](#statement) | Entire A--D, all guards, ranks, inequalities and explicit rational/bit costs. |
| argument | [Entire retained argument](#argument) | Complete Sections 1--8, all13 numbered formulas, original candidate and final construction, provenance, author check and limits. |
| dependency | [Reciprocal trace identity](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Elementary original polynomial trace decomposition only; no field-degree or smaller-determinant replacement. |
| dependency | [Quadratic circle identity](Yin_C_G0103_v1.md#explicit-salem-trace-field-certificates) | Exact modulus identity at a supplied rational b; no unknown trace input. |
| dependency | [Rational exact-PSD ceiling](Yin_C_G0103_v1.md#irreducible-all-padding-obstruction) | Actual irreducible Salem scope only, proving the constructed Q has exactly one negative eigenvalue. |
| dependency | [All original trace-pair regularization](Yin_C_G0113_v1.md#statement) | Equation4 with all squarefree, reciprocal, endpoint and original discriminant/Mahler hypotheses. |
| dependency | [Finite PSD Jensen argument](Yin_C_G0113_v1.md#localized-gram-correction) | Proof adapted explicitly to the relative-symbol multiplicative factor; no small additive correction assumption. |
| support | [Full integer-evaluation mechanism](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Credited old mechanism, rederived locally with original coefficient root bounds. |
| support | [Recurrence coefficient mechanism](Yin_C_G0117_v1.md#full-original-field-height-costs) | Credited finite-sum mechanism, rederived at rational b with no unpriced field operation. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T07:45 |
| status | proved |
| reason | Adopt R478 actual whole noncontributor review of the exact rational trace-residual construction, relative-symbol correction, coefficient-only admission, complete positive Salem input coverage at an input-dependent income and full arithmetic costs. No uniform income, new number-theoretic gap or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full relative-repair statement](#statement) | Entire A--D, all guards, ranks, inequalities and explicit rational/bit costs. |
| argument | [Entire retained argument](#argument) | Complete Sections 1--8, all13 numbered formulas, original candidate and final construction, provenance, author check and limits. |
| dependency | [Reciprocal trace identity](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Elementary original polynomial trace decomposition only; no field-degree or smaller-determinant replacement. |
| dependency | [Quadratic circle identity](Yin_C_G0103_v1.md#explicit-salem-trace-field-certificates) | Exact modulus identity at a supplied rational b; no unknown trace input. |
| dependency | [Rational exact-PSD ceiling](Yin_C_G0103_v1.md#irreducible-all-padding-obstruction) | Actual irreducible Salem scope only, proving the constructed Q has exactly one negative eigenvalue. |
| dependency | [All original trace-pair regularization](Yin_C_G0113_v1.md#statement) | Equation4 with all squarefree, reciprocal, endpoint and original discriminant/Mahler hypotheses. |
| dependency | [Finite PSD Jensen argument](Yin_C_G0113_v1.md#localized-gram-correction) | Proof adapted explicitly to the relative-symbol multiplicative factor; no small additive correction assumption. |
| support | [Full integer-evaluation mechanism](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Credited old mechanism, rederived locally with original coefficient root bounds. |
| support | [Recurrence coefficient mechanism](Yin_C_G0117_v1.md#full-original-field-height-costs) | Credited finite-sum mechanism, rederived at rational b with no unpriced field operation. |
| review | [Whole actual finding](../audits/reviews/Yin_R_G0798_v1.md#trace-residual-whole-independent-finding) | Entire actual statement and proof, direct dependencies, all thirteen equations, initial candidate, finite algorithm and explicit limits. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--D, all guards, ranks, inequalities and explicit rational/bit costs. |
| argument | [Argument](#argument) | Complete Sections 1--8, all13 numbered formulas, original candidate and final construction, provenance, author check and limits. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Elementary original polynomial trace decomposition only; no field-degree or smaller-determinant replacement. |
| dependency | [Dependency](Yin_C_G0103_v1.md#explicit-salem-trace-field-certificates) | Exact modulus identity at a supplied rational b; no unknown trace input. |
| dependency | [Dependency](Yin_C_G0103_v1.md#irreducible-all-padding-obstruction) | Actual irreducible Salem scope only, proving the constructed Q has exactly one negative eigenvalue. |
| dependency | [Dependency](Yin_C_G0113_v1.md#statement) | Equation4 with all squarefree, reciprocal, endpoint and original discriminant/Mahler hypotheses. |
| dependency | [Dependency](Yin_C_G0113_v1.md#localized-gram-correction) | Proof adapted explicitly to the relative-symbol multiplicative factor; no small additive correction assumption. |
| support | [Support](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Credited old mechanism, rederived locally with original coefficient root bounds. |
| support | [Support](Yin_C_G0117_v1.md#full-original-field-height-costs) | Credited finite-sum mechanism, rederived at rational b with no unpriced field operation. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#trace-residual-whole-independent-finding) | Entire actual statement and proof, direct dependencies, all thirteen equations, initial candidate, finite algorithm and explicit limits. |


### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--D, all guards, ranks, inequalities and explicit rational/bit costs. |
| argument | [Argument](#argument) | Complete Sections 1--8, all13 numbered formulas, original candidate and final construction, provenance, author check and limits. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Elementary original polynomial trace decomposition only; no field-degree or smaller-determinant replacement. |
| dependency | [Dependency](Yin_C_G0103_v1.md#explicit-salem-trace-field-certificates) | Exact modulus identity at a supplied rational b; no unknown trace input. |
| dependency | [Dependency](Yin_C_G0103_v1.md#irreducible-all-padding-obstruction) | Actual irreducible Salem scope only, proving the constructed Q has exactly one negative eigenvalue. |
| dependency | [Dependency](Yin_C_G0113_v1.md#statement) | Equation4 with all squarefree, reciprocal, endpoint and original discriminant/Mahler hypotheses. |
| dependency | [Dependency](Yin_C_G0113_v1.md#localized-gram-correction) | Proof adapted explicitly to the relative-symbol multiplicative factor; no small additive correction assumption. |
| support | [Support](Yin_C_G0107_v1.md#signed-norm-gap-assessment) | Credited old mechanism, rederived locally with original coefficient root bounds. |
| support | [Support](Yin_C_G0117_v1.md#full-original-field-height-costs) | Credited finite-sum mechanism, rederived at rational b with no unpriced field operation. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g123-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
