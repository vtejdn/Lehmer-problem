---
author: Yin
---
# Signed quadratic norms of actual trace defects

Date: 2026-10-18T13:42.
Human author Yin.
Root proposed the nonsquare quadratic norm, the two defect choices, the actual prime/field checks for the old controls and the bounded forty-form question.
The entropy_attainment_bridge AI checks reuse and develops the complete field, original-polynomial, scalar, signed-norm and source-cost account below.
Both are contributors; the complete proof is registered for separate whole independent review.
No numerical program, parameter evaluation, integration or new source acquisition is performed.

<a id="signed-defect-reuse"></a>
## Reuse and changed mathematical target

The accepted [C153v2 pairwise exclusions](Yin_C_G0153_v2.md#argument) and [actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supply the original nonzero defect pairs and phases.
The exact polynomial coefficients and denominators are the existing [C149 formulas](Yin_C_G0149_v1.md#original-polynomials-and-norms).
The accepted [C157v3 common-phase construction](Yin_C_G0157_v3.md#original-return) and [C_F6 scalar Jensen convention](Yin_C_F0006_v1.md#scalar-capacity-normalization) are reusable normalization interfaces.
No positivity or norm floor from C157v3 is assigned to the changed signed expression.

The bounded local screen read [C30's indefinite trace-form distinction](Yin_C_G0030_v1.md#statement), [C107's signed coefficient Gram](Yin_C_G0107_v1.md#statement), and the [C9](Yin_C_G0009_v1.md#statement)/[C12](Yin_C_G0012_v1.md#statement) relative-unit profile scopes.
They concern different quadratic values, coefficient Grams or relative-unit mixtures and do not supply the exact gate below.
The algebraic identity u^2-pv^2=Norm_(F(sqrt(p))/F)(u+sqrt(p)v) is the ordinary quadratic norm identity; the complete nonvanishing argument needed here is elementary and retained below.
No new external theorem or novelty assertion is needed.

[J102's three-rotation screen](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) applies Hadamard to squared Euclidean row norms of a POSITIVE form.
The signed form below is not a squared Euclidean norm, can change sign and can have nonzero isotropic arguments.
That screen is therefore not applicable merely because the same E,F_0,G appear.
This does not claim that every other screen fails or that a favorable parameter exists.

<a id="signed-defect-statement"></a>
## Exact candidate statement

Let F be a totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Set

    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

Choose X from{e,f}, an integer s and a rational prime p such that sqrt(p) is NOT in F.
Then

    U_(X,s,p)=(X+s g)^2-pg^2

is a NONZERO algebraic integer in F and

    abs(Norm_(F/Q)(U_(X,s,p)))>=1.                  (1)

It is not asserted totally positive, or of a prescribed norm sign.
The integer s restriction is essential to the asserted integrality without an additional denominator cost.
The prime condition may be replaced by an explicitly supplied nonsquare in F with the corresponding integral coefficient, but only rational primes are used here.

For the original-polynomial return let P in Z[z] be monic, irreducible, reciprocal and nontorsion, with constant1 and degree d=2r.
For a root alpha, set K=Q(alpha) and F=Q(alpha+alpha^-1), and ASSUME this actual trace field is totally real.
Use its actual C153v2 integral nonzero trace quotients a,b,c to define e,f,g.
For each choice X=e or X=f, use the corresponding centered circle function J_X=E or J_X=F_0, where

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72,
    F_0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375.

These are GLOBAL unreduced Laurent polynomials, real on the unit circle.
Put L=972000 and

    W_e=13500 z^(9d/2)H23,
    W_f=1215 z^(5d/2)H25,
    Z=32H35,
    A_(X,s,p)=(W_X+sZ)^2-pZ^2 in Z[z],
    N_(X,s,p)=z^(-15d)A_(X,s,p)/L^2.

Then

    N_(X,s,p)=(J_X+sG)^2-pG^2,
    N_(X,s,p)(alpha)=U_(X,s,p),                     (2)
    deg A_(X,s,p)=30d,
    lc(A_(X,s,p))=A_(X,s,p)(0)=50176(s^2-p)!=0.     (3)

The numerator is reciprocal, with a possibly NEGATIVE leading coefficient.
Its exact centered support is[-15d,15d].
Since p is prime and s is an integer, s^2-p cannot be zero.
The full original norm, including every proper-subfield repetition, is

    Norm_(K/Q)(N(alpha))=Norm_(F/Q)(U)^2>=1,
    Norm_(K/Q)(N(alpha))=Res(P,A)/L^(2d)>0.          (4)

The circle logarithm uses the ABSOLUTE value and is integrable, even when the circle polynomial has zeros:

    I_(X,s,p)=integral_T log|N_(X,s,p)| dmu
            =m(A_(X,s,p))-2log L.                 (5)

Here mu is normalized Haar probability measure and m(A) includes log|lc(A)| and all root multiplicities.
There is no division by the polynomial degree in (5).
The original supremum return is

    0<=log Norm_(K/Q)(N(alpha))/d
       <=log sup_T|N|+30m(P).                     (6)

The relevant arithmetic threshold for a hoped-for negative Haar cost is ZERO.
Neither a norm floor2^d nor a comparison against log2 is available for this signed gate.

<a id="signed-defect-proof"></a>
## 1. Nonvanishing, integrality and exact norm floor

The C153v2 exclusions say that neither (e,g) nor (f,g) can equal(0,0) in the stated totally real field.
Hence (X,g)!=(0,0) for either selected X.
If g=0, then X!=0 and U=X^2!=0.
If g!=0 and U=0, then ((X+s g)/g)^2=p.
This puts a square root of p in F, contrary to the hypothesis.
Thus U never vanishes.
The integer s and p and the integral defects make U an algebraic integer.
Its full signed norm is a nonzero rational integer, proving (1).
Each embedding of a nonzero field element stays nonzero; no embedding-dependent choice of a defect is made.

Equivalently F(sqrt(p))/F is a genuine quadratic extension and U is the relative norm of X+s g+sqrt(p)g.
This elementary interpretation does not identify that auxiliary extension with the original K/F or change any original multiplicity.

The floor1 cannot be replaced by a universal larger floor at the abstract triple level.
For F=Q and a=b=c=1 one has e=0,f=g=-1.
Taking X=e,s=1,p=2 gives U=-1, while sqrt(2) is not in Q.
The same value results from X=f,s=0,p=2.
Any quadratic original extension would square this norm to1.
No original polynomial realizing this abstract triple is asserted.

## 2. Actual trace phases, signed endpoints and all original factors

The accepted trace construction gives P(z)=z^r T(z+z^-1), [F:Q]=r and [K:F]=2.
With C_0(x)=2,C_1(x)=x,C_(j+1)=xC_j-C_(j-1), the values at alpha+alpha^-1 of the integral remainders rem_T(T(C_2)/2), rem_T(T(C_3)/3), rem_T(T(C_5)/5) are the nonzero a,b,c.
The original C149/C153v2 phases are

    H23(alpha)=-72alpha^(3d)e,
    H25(alpha)=-800alpha^(5d)f,
    H35(alpha)=-30375alpha^(15d/2)g.

All half-degree exponents are integers because d is even.
The common GLOBAL phase is

    W_X=-L z^(15d/2)J_X,
    Z=-L z^(15d/2)G.

This proves the exact Laurent identity in (2), including the cross-term sign, and its original value.
The source polynomials have degrees6d,10d,15d and leading/constant coefficients1,11,7.
Thus W_e has support[9d/2,21d/2], W_f has support[5d/2,25d/2] and Z has support[0,15d], each centered at15d/2.
Only the coefficient(s^2-p)Z^2 reaches the quadratic endpoints0 and30d.
Its endpoint coefficient is224^2(s^2-p)=50176(s^2-p), which proves (3) and excludes an unnoticed degree drop.
The numerator may be imprimitive; no content is removed from (5).
The common denominator L^2 is supplied exactly and not claimed minimal.

Because U lies in F, the tower identity gives Norm_K(U)=Norm_F(U)^2, a POSITIVE integer at least1.
The norm of alpha is1, since P is monic of even degree and constant1.
Taking the complete K norm of z^(-15d)A/L^2 at alpha therefore proves (4).
In particular the resultant in (4) is positive even if A has negative leading coefficient.
If U lies in a proper own subfield, its further repetitions are still present in Norm_F and Norm_K.
No original root is discarded or replaced by an independent phase sample.

## 3. Log absolute value, circle zeros and the paid source cost

The signed real circle function N need not be nonnegative and is not bounded below by a positive multiple of G^2.
Nevertheless A is a nonzero ordinary polynomial of exact degree30d and nonzero constant term.
It has only finitely many circle zeros, each of finite order.
Near each such point log|A| has a finite multiple of log angular distance plus a bounded term, hence is integrable.
Away from those points it is continuous.
The same holds for log|N| because the monomial has modulus1 on the circle and the denominator is constant.
F109's full scalar root/Jensen identity now gives (5), retaining the absolute leading coefficient, repeated roots and roots on the circle.
No positivity, singularity deletion or numerical regularization is used.

Put M_N=sup_T|N|>0.
On the circle |A|=L^2|N|<=L^2M_N.
The maximum principle for A on the disk and its degree30d reciprocal gives

    |N(z)|<=M_N max(|z|,|z|^-1)^(15d), z!=0.

At original roots N is nonzero, so logarithms are legal.
The original unit identity sum_i|log|alpha_i||=2m(P), followed by division by d, gives (6).
This is a supremum estimate, not an original-root/Haar transfer.

There is a useful difference from the rational positive two-shear gate.
The ordinary rational auxiliary F_aux=A/L^2 has

    F_aux(alpha)=alpha^(15d)U in O_K minus{0},
    Norm_K(F_aux(alpha))=Norm_K(U)>=1,
    m(F_aux)=I_(X,s,p), deg(F_aux)=30d.             (7)

Here alpha is an integral unit and U is integral, so ACTUAL integrality holds, not only a norm lower bound.
There is no division by2: doing so would lose this guaranteed floor and can lose integrality.
The [C140 normalized sparse theorem](Yin_C_G0140_v1.md#statement) therefore has its integral-value hypothesis available with integer numerator A and scalar q=L^2.
Its other hypotheses still require a useful negative Haar gap and UNIFORM bounds on the expanded term count and ||A||_1/L^2.
A fixed number of quadratic terms or fixed finite s,p set does not bound the expanded P-dependent support or coefficient mass.
Thus (7) is a correctly normalized potential input, not a completed uniform Mahler-gap proof.

<a id="missing-quadratic-prime-domain"></a>
## 4. The actual prime condition and the two fixed controls

For a general degree-r field the condition sqrt(p) notin F is real arithmetic information.
If r is odd, it holds for every rational prime p by the quadratic subfield tower formula.
More generally F can contain sqrt(p) for at most v_2(r) DISTINCT rational primes p, where v_2(r) is the exponent of2 in r.
This is the same multiquadratic prime-support mechanism already used in [L42](Yin_C_G0257_v1.md#unbounded-iteration-inflation), not a new field-degree theorem.
For completeness, for distinct primes p_1,...,p_k the compositum Q(sqrt(p_1),...,sqrt(p_k)) has degree2^k.
An inductive proof uses the basis product_(j in S)sqrt(p_j) and its distinct sign characters for the first k-1 primes.
If sqrt(p_k) belonged to that field, each sign automorphism would send it to plus or minus itself, so it would be a common eigenvector and hence a rational multiple of one basis element.
Squaring contradicts the odd p_k-adic valuation of p_k, since p_k occurs in none of the earlier basis products.
Thus adjoining sqrt(p_k) doubles the degree and extends the sign group, completing the induction.
If the compositum lies in F,2^k divides r, proving the asserted bound.
It follows that at least one of the first v_2(r)+1 primes is admissible.
This is a DEGREE-DEPENDENT supply, not a uniformly bounded prime over unrestricted r, and no useful Haar estimate follows from that supply alone.

The only proposed finite controls are the EXACT J97 inputs [quartic_Salem_seed and Lehmer_degree10](../computations/programs/Yin_J_G0097/input.json), whose irreducibility, original degree and total-real trace fields are retained in [J97's exact account](../computations/programs/Yin_J_G0097/readme.md#finite-results).
Their trace polynomials are

    quartic: T(x)=x^2-x-3, r=2,
    Lehmer: T(x)=x^5+x^4-5x^3-5x^2+4x+3, r=5.

For the quartic, the actual field is Q(sqrt(13)), since the discriminant of T is13.
None of sqrt(2),sqrt(3),sqrt(5),sqrt(7) lies in it.
Indeed if sqrt(p)=u+v sqrt(13) with u,v rational, squaring forces uv=0; either sqrt(p) is rational, or p/13 is a rational square, both impossible for these primes.
For Lehmer, r=5 is odd, so every rational prime satisfies the exclusion.
Hence BOTH X choices and EVERY combination of s in{-2,-1,0,1,2} and p in{2,3,5,7} meet the exact nonvanishing gate on both controls.
No computation of the field, prime search or norm is performed here.

<a id="signed-finite-proposal"></a>
## 5. Bounded finite question, not executed

After this COMPLETE gate has a separately retained whole review and is adopted, the proposed finite family consists of

    original P in{quartic_Salem_seed,Lehmer_degree10},
    X in{e,f}, s in{-2,-1,0,1,2}, p in{2,3,5,7}.

There are exactly40 forms per original input and80 forms in total.
The test variable is I=integral log|N| and the first mathematical question is whether any retained form has I<0.
If an operational saving margin is later declared, it must be measured below ZERO, not below log2.
An eventual J must preserve the original coefficients, exact numerator and L^2 scalar, signed leading coefficient, actual degree and all root multiplicities.
Complete-root Jensen certification naturally includes circle roots and avoids treating zero sample values as certified negative infinity.
Any exploratory phase ranking remains separate from a certified sign; a finite failed grid cannot exclude all integers s or all admissible primes.
No candidate, numerical sign, parameter optimum, new J output or expanded test is supplied by this draft.
Root owns the separate J allocation and any exact run protocol after gate adoption.

## Author conclusion and independence boundary

The signed quadratic gate is complete at author-check level: both nonvanishing cases, actual integrality, quadratic-subfield exclusion, complete phases and endpoints, full original norm1, logarithmic zeros, exact Jensen normalization, radial fee and the two fixed-input prime domains have been checked.
The floor is weaker than the positive family's2^d floor and is never relabeled as log2 income.
The changed sign makes J102's positive row-norm argument inapplicable, but does not prove a useful negative Haar cost.
Root and entropy_attainment_bridge are contributors and cannot provide the independent whole review.
This is a new signed-value claim family: the value domain, norm1 threshold and nonsquare-field mechanism differ from the positive C157 family.
The original unrestricted G0001 objective remains unresolved.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T13:42 |
| status | open |
| reason | Register the complete signed quadratic-norm gate for the changed finite test. Nonzero actual integral values, full original norm1, signed endpoints, all Jensen scalars and the degree-dependent prime domain are retained; useful negative Haar cost and uniform transfer budgets remain open. Root and entropy_attainment_bridge contributed, requiring a separate whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete signed gate](#signed-defect-statement) | Both actual defects, all integer shears, primes excluded from the actual trace field, full original polynomial and norm, exact signed Haar normalization and supremum return. |
| argument | [Complete argument](#signed-defect-proof) | Nonvanishing and norm floor, all original phases and scalar factors, logarithmic integrability and radial cost, ordinary integral auxiliary, prime supply and both fixed controls. |
| dependency | [Pairwise exclusions and trace values](Yin_C_G0153_v2.md#argument) | Actual totally real pair exclusions, integral nonzero trace quotients and original extension degree. |
| dependency | [Original defect polynomials](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact three numerator coefficients and trace phases. |
| dependency | [Aligned original construction](Yin_C_G0157_v3.md#original-return) | Common phase and L=972000 only; no positive norm floor is imported. |
| dependency | [Scalar Jensen identity](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Absolute leading coefficient, scalar and all root multiplicities. |
| support | [Normalized sparse theorem](Yin_C_G0140_v1.md#statement) | Actual integrality hypothesis is available; negative Haar gap and uniform expanded budgets are not supplied. |
| support | [Original fixed inputs](../computations/programs/Yin_J_G0097/input.json) | Exactly the quartic and Lehmer coefficients, with prime exclusion proved here. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T13:58 |
| status | proved |
| reason | Adopt the complete signed quadratic-norm gate through the whole noncontributor R400 finding. Actual nonzero integral values and the full original norm1 threshold are proved, with all signed Jensen factors and prime/trace-field exclusions retained. The finite J103 interface is eligible for its declared bounded test; this supplies no favorable Haar value, certified grid minimum or uniform coefficient/transfer budget. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete signed gate](#signed-defect-statement) | Both actual defects, all integer shears, primes excluded from the actual trace field, full original polynomial and norm, exact signed Haar normalization and supremum return. |
| argument | [Complete argument](#signed-defect-proof) | Nonvanishing and norm floor, all original phases and scalar factors, logarithmic integrability and radial cost, ordinary integral auxiliary, prime supply and both fixed controls. |
| dependency | [Pairwise exclusions and trace values](Yin_C_G0153_v2.md#argument) | Actual totally real pair exclusions, integral nonzero trace quotients and original extension degree. |
| dependency | [Original defect polynomials](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact three numerator coefficients and trace phases. |
| dependency | [Aligned original construction](Yin_C_G0157_v3.md#original-return) | Common phase and L=972000 only; no positive norm floor is imported. |
| dependency | [Scalar Jensen identity](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Absolute leading coefficient, scalar and all root multiplicities. |
| support | [Normalized sparse theorem](Yin_C_G0140_v1.md#statement) | Actual integrality hypothesis is available; negative Haar gap and uniform expanded budgets are not supplied. |
| support | [Original fixed inputs](../computations/programs/Yin_J_G0097/input.json) | Exactly the quartic and Lehmer coefficients, with prime exclusion proved here. |
| review | [Whole signed-gate finding](../audits/reviews/Yin_R_G0400_v1.md#signed-defect-whole-independent-finding) | Complete statement and proof, all actual trace/nonvanishing/norm/scalar domains, degree-dependent prime supply, two fixed controls and C140 boundary; C157v3 upstream authorship/R541 reuse and no numerical-code review are disclosed. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:45 |
| status | proved |
| reason | Select adopted C_F6 as the current complete responsible home of the identical retained scalar Haar/Jensen normalization. Its actual selected adoption and complete normalization section were read and matched to the original fixed L_F5 text, including Laurent shifts, leading coefficients, all root multiplicities and integrable circle zeros. Only that normalization is reused here, with every original scalar, phase and cost retained; no Gram optimization, root-distribution transfer or new review is supplied. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete signed gate](#signed-defect-statement) | Both actual defects, all integer shears, primes excluded from the actual trace field, full original polynomial and norm, exact signed Haar normalization and supremum return. |
| argument | [Complete argument](#signed-defect-proof) | Nonvanishing and norm floor, all original phases and scalar factors, logarithmic integrability and radial cost, ordinary integral auxiliary, prime supply and both fixed controls. |
| dependency | [Pairwise exclusions and trace values](Yin_C_G0153_v2.md#argument) | Actual totally real pair exclusions, integral nonzero trace quotients and original extension degree. |
| dependency | [Original defect polynomials](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Exact three numerator coefficients and trace phases. |
| dependency | [Aligned original construction](Yin_C_G0157_v3.md#original-return) | Common phase and L=972000 only; no positive norm floor is imported. |
| dependency | [Scalar Jensen identity](Yin_C_F0006_v1.md#scalar-capacity-normalization) | Absolute leading coefficient, scalar and all root multiplicities. |
| support | [Normalized sparse theorem](Yin_C_G0140_v1.md#statement) | Actual integrality hypothesis is available; negative Haar gap and uniform expanded budgets are not supplied. |
| support | [Original fixed inputs](../computations/programs/Yin_J_G0097/input.json) | Exactly the quartic and Lehmer coefficients, with prime exclusion proved here. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0400_v1.md#signed-defect-whole-independent-finding) | Complete statement and proof, all actual trace/nonvanishing/norm/scalar domains, degree-dependent prime supply, two fixed controls and C140 boundary; C157v3 upstream authorship/R541 reuse and no numerical-code review are disclosed. |
