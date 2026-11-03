---
author: Yin
---
# An exponential joint defect norm floor over a totally real field

Human author Yin.
Root is the sole contributor to the new joint-norm argument extracted from D35 Section8 (author checkpoint 2026-10-15T16:39); root also contributed to the inherited C149/C151/C153 inputs.
Yin now authorizes only independent review and result organization while G0001 remains paused.
This fixed candidate retains the complete Section8 mathematics, including original equation numbers (29)--(35), sharpness, original-polynomial costs and the failed quadratic comparison.
D35 Sections1--7 are outside this candidate and remain continuing author material.
The extraction is not a proof dependency or acceptance.

The new object is the field norm of the sum of THREE trace-defect squares.
C149's sum of separate full norm squares, C150's weighted common ideals and C153v2's two-label completion are distinct earlier results.
This comparison asserts no global novelty.
Only corrected C153v2 is used; the erroneous v1 and its changes-required review remain unchanged.

## Statement

Let F be a totally real number field of degree r and a,b,c nonzero algebraic integers in F.
Put e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5 and h=e^2+f^2+g^2.
Then h is totally positive and Norm_(F/Q)(h)>=2^r.
The constant2 is sharp among these abstract integral triples, without asserting that the sharp triple is realized by the Frobenius values of an original polynomial.

For every original monic irreducible reciprocal nontorsion integer-unit P of degree d=2r whose ACTUAL trace field Q(alpha+alpha^(-1)) is totally real, use the C153v2 integral trace quotients and C149 H23,H25,H35.
The exact three-label positive completion A_3,B_3 in(32) has full original norm Norm_K(B_3(alpha))>=2^d, supplied denominator972000^2 and ordinary numerator degree30d.
It satisfies(34), with full30m(P) radial fee and scalar Haar normalization, while its coefficient energy obeys integral Q_P>= (67/25)^2>2.
Thus the named quadratic-mean/covariance estimate still cannot contradict this guaranteed floor.
No direct moving-logarithm control, changed-auxiliary coverage or unrestricted Mahler gap is asserted.

<a id="argument"></a>
## 1. General totally-real integral triple

Let F be a totally real number field of degree r, and let a,b,c be NONZERO algebraic integers in F.
Define

    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    h=e^2+f^2+g^2.

C153v2 proves that(e,g) and(f,g) cannot both vanish.
Thus h is a totally positive algebraic integer: at least one fixed nonzero defect remains nonzero at every embedding.
The conclusion is

    Norm_(F/Q)(h)>=2^r.                              (29)

If at least two defects x,y are nonzero, every real embedding satisfies sigma(h)>=sigma(x)^2+sigma(y)^2>=2|sigma(x)sigma(y)|.
Multiplication over ALL r embeddings gives Norm_F(h)>=2^r|Norm_F(x)Norm_F(y)|>=2^r.
The last step uses the nonzero integer norms of the actual integral defects.

The only remaining possibility is e=f=0 and g!=0.
The other two singleton cases are excluded by C153v2's totally-real field lemma.
Put v=b/a, so v^2=a,v^3=b, and gamma=2c/v^5, so gamma^2=6.
These are FIELD identities; no monogenic-order inverse is asserted.
Let q=Norm_F(v), a nonzero rational number.
Since q^2=Norm_F(a) is an integer, rational denominator reduction implies q is an integer.
Taking norms of c^2=(3/2)v^10 gives

    2^r Norm_F(c)^2=3^r q^10,
    2^r divides q^10,
    |q|^15>=2^(3r/2).                                (30)

All norms here are full F norms, and the second line uses coprimality of2 and3 in the INTEGER identity.
There is no rounding-away of ramification or use of an unproved lower valuation for v.

The quadratic subfield Q(gamma) has degree2 by the same X^2-6 irreducibility already proved in C153v2, so r is even.
Direct algebra gives

    g=kappa v^15, kappa=(3gamma-8)/4,
    Norm_(Q(gamma)/Q)(kappa)=(64-54)/16=5/8,
    |Norm_F(g)|=(5/8)^(r/2)|q|^15>=5^(r/2).          (31)

The field-norm tower retains all r/2 copies; kappa is not declared integral or a unit.
In this singleton case h=g^2, so Norm_F(h)>=5^r>2^r, completing(29).

The constant2 is sharp for the broader FIELD-TRIPLE theorem: a=b=c=1 gives(e,f,g)=(0,-1,-1), h=2 and Norm_F(h)=2^r in every totally real F.
This is an abstract integral triple, NOT an asserted Frobenius triple of an original P and not a near-one counterexample.

<a id="original-polynomial-return"></a>
## 2. Return to the actual reciprocal polynomial

Let P be the original monic irreducible reciprocal nontorsion integer-unit polynomial, d=2r, with ACTUAL totally real trace field F.
Use precisely the integral trace quotients a,b,c and phases of [C153v2 Section3](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
Let Hj,qj be the actual C149 numerators and denominators72,800,30375.
With the exact common denominator L=lcm(72,800,30375)=972000 define

    A_3(t)=(L/72)^2 t^(9d)H23(t)^2
             +(L/800)^2 t^(5d)H25(t)^2
             +(L/30375)^2 H35(t)^2 in Z[t],
    B_3(t)=t^(-15d) A_3(t)/L^2.                      (32)

Here L/qj are13500,1215,32.
A_3 is reciprocal of exact degree30d, with constant and leading coefficient49*32^2=50176; the other two supports are[9d,21d] and[5d,25d].
The supplied L^2 is not called the least denominator.
Circle reciprocity and the actual squared phases give

    B_3(z)=sum_j |Hj(z)/qj|^2=Q_P(z) for |z|=1,
    B_3(alpha)=h in Z[z_trace],
    Norm_K(B_3(alpha))=Norm_F(h)^2>=2^d,
    Norm_K(A_3(alpha))=L^(2d)Norm_F(h)^2.             (33)

The variable z in the first line is a circle point; z_trace=alpha+alpha^(-1) is the algebraic trace generator.
They are not identified.
The centering monomial has full norm1, since Norm_K(alpha)=1.
Every original conjugate and every smaller-own-field multiplicity remains in the displayed norms.

Let J=sup_circle Q_P.
The already paid maximum-principle return of C153v2, applied to A_3 and its centering monomial, yields the exact original inequality

    log2<=log Norm_K(B_3(alpha))/d<=log J+30m(P),
    integral log B_3 dmu=m(A_3)-2log L.               (34)

The logarithmic circle integral uses the nonzero polynomial A_3 and is well-defined with its integrable logarithmic zeros; strict circle positivity is not needed.
The identity is the adopted F109 scalar normalization.
The lower bound in(34) is stronger arithmetic income than merely norm>=1, but it does not identify the actual original average with its Haar average or remove coefficient/regularity costs.

<a id="quadratic-estimate-obstruction"></a>
## 3. The named quadratic estimate still cannot exploit this floor

For an actual reciprocal P as above, its integer coefficient energy A=sum p_j^2 is at least4.
A=2 would force a torsion binomial.
A=3 would force exactly one interior coefficient+/-1; reciprocity places it at d/2, giving t^(2r)+/-t^r+1, again with all roots of unity.
Thus both are outside the domain.
No assertion about optimal larger integer energy is needed.

Use the exact [C151 H25 moment calculation](Yin_C_G0151_v1.md#untransformed-three-defect-energy-obstruction), now with ||P||_10>=sqrt(A)>=2.
Monotonicity gives

    ||H25||_2>=75*2^5-64*2^2=2144,
    E25>=(2144/800)^2=(67/25)^2>2,
    integral Q_P dmu>=E25>2.                         (35)

Therefore J>2 and the same quadratic-mean/covariance upper estimate remains greater than log2 throughout its permitted domain.
The new arithmetic income does not close that previously specified method.
It leaves a direct logarithmic estimate or a changed actual auxiliary as an unresolved next question, not as an automatically valid inference.

<a id="author-check-and-extraction"></a>
## Author check and extraction boundary

The original author check reconstructed the exhaustive singleton cases, full rational norm integrality and2-adic integer divisibility, the quadratic-subfield norm5/8 with all multiplicities, the exact common denominator and centered supports, original2^d floor, nonmonic Jensen scaling and30m fee, and reciprocal coefficient-energy exclusions.
No numerical test, new source acquisition or independent review was used to develop that proof.
At 2026-10-15T16:51 root extracted the unchanged Section8 mathematics, added the explicit statement and direct-input bindings, and retained the original formula identifiers.
Its new fixed assessment remains proof draft pending actual independent whole review.
The historical pause checkpoint did not claim acceptance; this review assignment grants no resumption of G0001 exploration.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:51 |
| status | open |
| reason | Fix the entire D35 Section8 joint-norm argument, abstract sharpness, reciprocal return and quadratic-cost obstruction for the human-requested independent review. G0001 remains paused; no new exploration or unrestricted gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete joint-norm statement](#statement) | Nonzero integral triples in every totally real field, exact original reciprocal domain, sharp abstract constant and all cost limits. |
| argument | [Entire three-section proof](#argument) | All formulas29--35, singleton/two-defect cases, sharpness, original completion, full norms, logarithmic normalization and quadratic-method limitation. |
| dependency | [Corrected pairwise field theorem](Yin_C_G0153_v2.md#argument) | The (e,g) and (f,g) simultaneous-zero exclusions in a totally real field and the quadratic radical subfield in the remaining singleton case. |
| dependency | [Actual reciprocal trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral a,b,c in the actual degree-r trace field, exact6r/10r/15r phases, K/F quadratic and genuine Salem applicability without automatic total reality for all reciprocal P. |
| dependency | [Original numerator and norm identities](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, exact denominators72/800/30375 and degrees6d/10d/15d, with original conjugates and possible zero individual labels. |
| dependency | [Paid positive-completion return](Yin_C_G0153_v2.md#two-label-positive-completion-exact-cost) | Polynomial maximum principle and centered Laurent return with the full30m fee; the new three-label completion and stronger norm floor are proved locally. |
| dependency | [Exact H25 moment calculation](Yin_C_G0151_v1.md#untransformed-three-defect-energy-obstruction) | Reverse triangle, normalized Haar power invariance and Lp monotonicity; the reciprocal coefficient-energy threshold4 is proved locally. |
| dependency | [Existing coupled quadratic estimate](Yin_C_G0151_v1.md#argument) | Section5 common-window quadratic mean/covariance estimate in its stated small-u domain, including nonnegative error factors; no new moving-logarithm theorem. |
| dependency | [Scalar Haar normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent Jensen identity, full scalar972000^2 and allowed integrable circle zeros, without replacing the original-root distribution by Haar. |

### Decision whole-reviewed-2026-10-16

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T17:00 |
| status | proved |
| reason | Adopt the complete joint-norm theorem, abstract sharpness, actual reciprocal completion and paid supremum/energy limitation after the whole independent R373 review. The old covariance expression is compared numerically only; no new-norm covariance-transfer inequality is asserted or adopted. This closes Yin's specifically authorized bounded review while G0001 remains paused. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete joint-norm statement](#statement) | Nonzero integral triples in every totally real field, exact original reciprocal domain, sharp abstract constant and all cost limits. |
| argument | [Entire three-section proof](#argument) | All formulas29--35, singleton/two-defect cases, sharpness, original completion, full norms, logarithmic normalization and quadratic-method limitation. |
| dependency | [Corrected pairwise field theorem](Yin_C_G0153_v2.md#argument) | The (e,g) and (f,g) simultaneous-zero exclusions in a totally real field and the quadratic radical subfield in the remaining singleton case. |
| dependency | [Actual reciprocal trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral a,b,c in the actual degree-r trace field, exact6r/10r/15r phases, K/F quadratic and genuine Salem applicability without automatic total reality for all reciprocal P. |
| dependency | [Original numerator and norm identities](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, exact denominators72/800/30375 and degrees6d/10d/15d, with original conjugates and possible zero individual labels. |
| dependency | [Paid positive-completion return](Yin_C_G0153_v2.md#two-label-positive-completion-exact-cost) | Polynomial maximum principle and centered Laurent return with the full30m fee; the new three-label completion and stronger norm floor are proved locally. |
| dependency | [Exact H25 moment calculation](Yin_C_G0151_v1.md#untransformed-three-defect-energy-obstruction) | Reverse triangle, normalized Haar power invariance and Lp monotonicity; the reciprocal coefficient-energy threshold4 is proved locally. |
| dependency | [Existing coupled quadratic estimate](Yin_C_G0151_v1.md#argument) | Section5 common-window quadratic mean/covariance estimate in its stated small-u domain, including nonnegative error factors; no new moving-logarithm theorem. |
| dependency | [Scalar Haar normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent Jensen identity, full scalar972000^2 and allowed integrable circle zeros, without replacing the original-root distribution by Haar. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0373_v1.md#totally-real-joint-norm-whole-independent-finding) | Complete statement and three-section argument/formulas29--35, all seven direct interfaces, extraction, exact norms/scalars/degrees, sharpness and restricted covariance comparison. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:45 |
| status | proved |
| reason | Select adopted C_F6 as the current complete responsible home of the identical retained scalar Haar/Jensen normalization. Its actual selected adoption and complete normalization section were read and matched to the original fixed L_F5 text, including Laurent shifts, leading coefficients, all root multiplicities and integrable circle zeros. Only that normalization is reused here, with every original scalar, phase and cost retained; no Gram optimization, root-distribution transfer or new review is supplied. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete joint-norm statement](#statement) | Nonzero integral triples in every totally real field, exact original reciprocal domain, sharp abstract constant and all cost limits. |
| argument | [Entire three-section proof](#argument) | All formulas29--35, singleton/two-defect cases, sharpness, original completion, full norms, logarithmic normalization and quadratic-method limitation. |
| dependency | [Corrected pairwise field theorem](Yin_C_G0153_v2.md#argument) | The (e,g) and (f,g) simultaneous-zero exclusions in a totally real field and the quadratic radical subfield in the remaining singleton case. |
| dependency | [Actual reciprocal trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral a,b,c in the actual degree-r trace field, exact6r/10r/15r phases, K/F quadratic and genuine Salem applicability without automatic total reality for all reciprocal P. |
| dependency | [Original numerator and norm identities](Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23,H25,H35, exact denominators72/800/30375 and degrees6d/10d/15d, with original conjugates and possible zero individual labels. |
| dependency | [Paid positive-completion return](Yin_C_G0153_v2.md#two-label-positive-completion-exact-cost) | Polynomial maximum principle and centered Laurent return with the full30m fee; the new three-label completion and stronger norm floor are proved locally. |
| dependency | [Exact H25 moment calculation](Yin_C_G0151_v1.md#untransformed-three-defect-energy-obstruction) | Reverse triangle, normalized Haar power invariance and Lp monotonicity; the reciprocal coefficient-energy threshold4 is proved locally. |
| dependency | [Existing coupled quadratic estimate](Yin_C_G0151_v1.md#argument) | Section5 common-window quadratic mean/covariance estimate in its stated small-u domain, including nonnegative error factors; no new moving-logarithm theorem. |
| dependency | [Scalar Haar normalization](Yin_C_F0006_v1.md#scalar-capacity-normalization) | Nonmonic/Laurent Jensen identity, full scalar972000^2 and allowed integrable circle zeros, without replacing the original-root distribution by Haar. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0373_v1.md#totally-real-joint-norm-whole-independent-finding) | Complete statement and three-section argument/formulas29--35, all seven direct interfaces, extraction, exact norms/scalars/degrees, sharpness and restricted covariance comparison. |
