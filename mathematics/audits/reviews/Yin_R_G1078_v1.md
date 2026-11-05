---
author: Yin
---
# Independent whole review of the three-pair sign margin and its original-window consequence

Human record author Yin.
Review act: 2026-11-04T17:38 UTC.
The reviewed artifact is the fixed [C862v1](../../claims/Yin_C_G0862_v1.md#statement) text dated 2026-11-05, Asia/Shanghai, including the explicit positive-integer n in its binary phase specialization and before initial assessment.
This is an initial whole review, including the four-pair comparison, rather than a review of unrestricted G0001 completion.

## Arrangement and inputs

The reviewing agent did not participate in substantive proof development and received the fixed statement, proof, necessary dependency locations and review scope directly.
No D16 or D13 development draft, proof-generation dialogue, author explanation of a proof step or prior review conclusion about C862 was consulted.
An agent-availability inventory incidentally displayed the contributor's completion notice, comprising the fixed-file location, a list of the same section scopes and allocation/freeze information.
That notice contained no derivation, proposed justification or review finding and supplied no mathematical support for this review.
The reviewer formed the initial findings by reconstructing the coefficient multiplication, resonance count and arithmetic interfaces from the fixed text.
The author's J134 program and generated output were neither read nor rerun, and no frequency sampling or numerical quadrature supplies evidence here.
The needed current C141, C139, C92 and scalar-normalization interfaces were read directly.
Their selected decisions retain their actual earlier relationships; in particular C141 and C139 currently select self-reviewed findings, which this review does not relabel.
The phase-index wording was clarified to state explicitly that n is a positive integer, as already required by its polynomial domain, and the resulting statement was reread.
The reviewer supplied no substantive repair or new proof step.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-c0862-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-c0862-finding) | [Statement](../../claims/Yin_C_G0862_v1.md#statement) | All frequency/sign quantifiers, uniform margin, original-field auxiliary conditions, strict positive bound and positive-integer phase specialization. |
| [Whole finding](#whole-c0862-finding) | [Normalization and small cases](../../claims/Yin_C_G0862_v1.md#normalization-and-small-cases) | Integer exponents, Haar measure, half-integer substitution, logarithmic integrability and every sign for one or two pairs. |
| [Whole finding](#whole-c0862-finding) | [Complete argument](../../claims/Yin_C_G0862_v1.md#argument) | Whole three-pair proof, all eleven coefficient shapes, resonance exhaustion, sign product and Jensen estimate; subsequent arithmetic and comparison sections are also explicitly bound below. |
| [Whole finding](#whole-c0862-finding) | [Original-window consequence](../../claims/Yin_C_G0862_v1.md#binary-original-window-consequence) | Integral quotient in the original field, exact support/length/degree, C141 substitution, zero and nonzero branches and complete phase reduction. |
| [Whole finding](#whole-c0862-finding) | [Four-pair comparison](../../claims/Yin_C_G0862_v1.md#four-pair-second-moment-obstruction) | Exact product, all twelve coefficient shapes, rational second moment and explicit tuple without relations of coefficient length at most eight; failure only of the stated sufficient estimate. |
| [Whole finding](#whole-c0862-finding) | [C141 assembly](../../claims/Yin_C_G0141_v1.md#reuse-zero-removal) | Accepted Section1 hypotheses, constants and two-case implication as invoked here, excluding its separate finite-prime results. |
| [Whole finding](#whole-c0862-finding) | [C139 interface](../../claims/Yin_C_G0139_v1.md#statement) | Accepted nonzero integral-quotient theorem at K=S=6, q=2, with positive constant fixed before the actual inputs; no new audit of inherited source proof. |
| [Whole finding](#whole-c0862-finding) | [C92 interface](../../claims/Yin_C_G0092_v1.md#automatic-fixed-rank-power-independence) | Accepted threshold K0*r^(-64) and applicability to the actual support/span in the zero branch; no new audit of inherited angular/source arguments. |
| [Whole finding](#whole-c0862-finding) | [Scalar normalization](../../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Mahler integral/root convention retaining content, circle zeros and monomial invariance. |

<a id="whole-c0862-finding"></a>
## Whole finding

No mathematical gap remains in the exact reviewed C862 statement and complete argument under its stated accepted inputs.
The uniform sign conclusion and supplied-auxiliary original-window consequence are supported throughout their stated domains.
The four-pair comparison proves failure of the indicated sufficient estimate and supplies no counterexample to good-sign existence.

### Polynomial and analytic normalization

In both parity classes, K+a_j and K-a_j are distinct nonnegative integers, with both endpoints present and degree exactly 2K.
The circle factor 2i*exp(i*K*theta) contributes exactly log2, with no division by polynomial degree.
For half-integers, theta=2u transforms dtheta/(2pi) into du/pi on [0,pi]; the doubled frequencies are all odd, so the absolute sine sum has period pi and the resulting integral is its full-circle normalized mean.
This is only an analytic change of variable and leaves the original polynomial and field intact.
The one-pair binomial and both two-pair factorizations were directly expanded, including their signs and positive integer exponents, giving zero logarithmic measure for every sign choice.
Distinct positive frequencies make each three-pair sine factor a nonzero trigonometric polynomial.
Finite-order circle zeros therefore justify its logarithmic integrability, the product logarithm and the regularized Jensen limit.

### Three-variable multiplication and all resonances

The reviewer reconstructed q=16Q_3 from 4u_j=2-X_j-X_j^(-1) and multiplied its coefficient types directly.
All eleven partitions of absolute exponent sum at most four in three coordinates were checked; their signed permutation multiplicities total 129 vectors.
For representatives (1,0,0), (2,0,0), (1,1,0) and (2,1,1), the coefficient decompositions are respectively

    -48+8-64=-104,
    -12+16+16=20,
    24+32-8+16=64,
    -4+8=4.

The other seven representatives reproduce 186, 8, -8, -48, 1, 6 and -4 in the corresponding displayed rows.
The list is exhaustive because q has absolute exponent sum at most two and exact sign/permutation symmetry.
After X_j=exp(2i*a_j*theta), the constant term is exactly the sum over v dot a=0; the factor two creates no additional resonances.
Every positive row except the origin and (2,1,1) forces a zero frequency or equality of two positive frequencies.
For a fixed doubled coordinate, the sum and absolute-difference alternatives cannot both hold and each valid alternative determines one opposite pair.
Hence at most six such vectors contribute, including every simultaneous resonance across distinct doubled coordinates.
Dropping all negative contributions yields 186+6*4=210 and therefore integral Q_3^2<=105/128.
The four-sign product is exactly Q_3, and its mean logarithm followed by concavity gives the factor 1/8 in eta_3=(1/8)log(128/105).
The resulting margin is positive, less than one and independent of the frequencies or parity class.

### Same-field arithmetic and binary phase specialization

The frequencies a_j=T/2-e_j have K=T/2 and the required common parity, producing an actual degree-T polynomial with exactly 2s terms, coefficient length 2s<=6 and nonzero endpoints.
Since A=V modulo2, the polynomial (A-V)/2 is integral and A(alpha)/2 is an algebraic integer in Q(alpha), including either possible zero value.
No smaller-order condition or powered-field substitution is needed.
The C141 Section1 hypotheses match with K_support=S_length=6, q=2, eta=eta_3 and the original C, d and total m(P).
If m(P)<=gamma_3(C) and A(alpha)=0, then T*m(P)/d<=K0*6^(-64)<=K0*(2s)^(-64), so the accepted C92 threshold excludes that nontrivial rational relation.
The remaining nonzero quotient satisfies C139 and gives m(P)>g>=gamma_3(C).
This proves the strict minimum bound even at the assumed equality boundary, without a norm logarithm at zero.
The fixed absolute source constant remains that inherited by C139; no fully numerical source-free value of g is asserted.

A seed coefficient of absolute value two would exhaust the energy budget and force a single monomial, and H(0)!=0 would make it one of the excluded constants +/-2.
Thus every nonzero coefficient is +/-1 and there are at most four.
For every positive integer n, the endpoint coefficients of V are h_k and sigma*h_k and its degree is exactly n+k, even with overlapping intervals or a constant seed +/-1.
At this degree V*=sigma*V; any central coincident coefficient is (1+sigma)*h_r and is even.
Its binary support therefore consists of one to four reflected pairs with endpoints present, and the assumed at-most-three case is exactly S2.
There is no phase-separation or nonzero-value condition hidden in this deduction.

### Four-variable comparison

Pairing the final two signs and then the second sign verifies the exact eight-sign product Q^2-64u_1u_2u_3u_4.
The reviewer expanded q_4 and the correction -64*product U_j independently of the author's program.
All twelve partitions of absolute exponent sum at most four in four coordinates were checked, with multiplicities totaling 321 vectors.
For the five squarefree shapes of sizes zero through four, q_4^2 gives 1192, -560, 248, -96 and 24, while the correction gives -1024, +512, -256, +128 and -64.
Their sums are the displayed 168, -48, -8, 32 and -40.
The other seven shapes are absent from product U_j and give 40, -16, 4, 6, 16, -4 and 1 as displayed.
The sum of squared coefficients with multiplicities is 136872, giving 136872/65536=17109/8192>1 under the stated orthogonality hypothesis.
For (1,9,81,729), a highest nonzero power contributes at least 9^k while all lower contributions have absolute value at most 7*9^(k-1); the case k=0 has no lower term.
Thus no nonzero relation of absolute coefficient sum at most eight vanishes, and the obstruction holds on an actual circle tuple.
It obstructs only the universal direct second-moment estimate below one, leaving sharper logarithmic estimates and individual favorable signs open.

## Scope limits

This finding covers all new fixed C862 mathematics and the exact applicability of its accepted arithmetic premises.
It does not re-prove the inherited C92 angular theory, C139's source inequality or unrelated C141 sections, nor upgrade their historical self-reviewed relationships.
The bounded literature search and J134 execution account are not proof premises and were not separately audited.
No unrestricted auxiliary-supply theorem, four-pair good-sign theorem, novelty result or Lehmer completion follows.
Any C862 assessment remains a separate adoption of this finding and its declared premises by the coordinating agent.
