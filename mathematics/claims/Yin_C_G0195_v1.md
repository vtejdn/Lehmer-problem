---
author: Yin
---
# Rational trace-congruent regularization with complete denominator and pole costs

Date: 2026-10-20T12:44.
Human author Yin.
Root proposed the rational regularizer and the question of its full denominator and original-return costs.
The entropy_attainment_bridge agent supplied the exact clearing, finite error, comparison and pole specialization; both are contributors to this proof.
The argument was developed in D36 on2026-10-20 and is retained completely here as a candidate, without new computation or source acquisition.
The present author contributed to the upstream C191 arithmetic theorem and reuses its independent R468; the present proof itself has not yet been independently reviewed.

<a id="statement"></a>
## Exact theorem statement

Let P in Z[z] be monic, irreducible, reciprocal and nontorsion, of degree d=2r and constant coefficient1.
Let alpha be a root, K=Q(alpha), and assume that its actual trace field F=Q(alpha+alpha^(-1)) is totally real.
Let Theta in Z[x] be its monic degree-r trace polynomial, so P(z)=z^r Theta(z+z^(-1)).
Use the actual unreduced integer polynomials and real centered Laurent functions

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72, F0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375,
    H=Theta(z+z^(-1))G, J_G=integral_T log G^2 dmu.

Here mu is normalized Haar probability, m(P) is total logarithmic Mahler measure, and every original conjugate is counted with original degree d.
Write E0,F00,G0 for the rational polynomials in x=z+z^(-1) whose pullbacks are E,F0,G.
Let e=E(alpha), f=F0(alpha), g=G(alpha), the actual integral trace defects of C153/C191.
For each s in{1,-1} and positive rational epsilon use the rational shears and B_epsilon of(RR1).
Then all of the following hold.

1. The exact original value is Q_s=(e+s g)^2+f^2+g^2, with full norm Norm_K Q_s=Norm_F(Q_s)^2>=2^d.
   In the residual case f=0 and e+s g=0 it is at least2^(12d/11).
   The Haar integral I_epsilon is strictly greater than J_G and tends to J_G as epsilon decreases to0.
   Formulas(RR10)--(RR11) give a finite zero-compatible error and a sufficient rational parameter using the full degree16d polynomial P H35 and its leading scalar7.
2. Both rational shears have degree bounded independently of epsilon.
   The resulting B_epsilon has the exact supplied ordinary numerator N_epsilon of degree94d and denominator D_epsilon^2 of degree64d, with D_epsilon of degree32d.
   Formulas(RR4)--(RR6) retain their endpoint coefficients, supplied scalar L^2*30375^4*p_epsilon^4, every original resultant and the unchanged norm.
   No reduced-degree, primitive-content or minimal-denominator assertion is imposed.
3. The normalized denominator R_epsilon=1+H^2/epsilon^2 equals1 at every original conjugate.
   Nevertheless the polynomial clearing C_epsilon=B_epsilon R_epsilon^2 is pointwise at least the old constant-shear symbol(E+sG)^2+F0^2+G^2.
   Thus its Haar mean is greater than log2 for every epsilon on both actual J99 controls.
   Its exact logarithmic price and limiting growth are(RR12)--(RR14), and its legitimate polynomial radial fee is94m(P).
4. Keeping the rational function gives the complete original-root bound(RR15), with radial fee30m(P) and the full nonnegative Green pole charge Pi_epsilon.
   For every epsilon it is a valid supplied-denominator bound, whether or not some finite poles are removable.
   Cancellation of a finite denominator root can occur only at the explicitly characterized finite exceptional set of positive epsilon in the proof.
   For all sufficiently small positive epsilon the approaching poles are genuine, and Pi_epsilon tends to infinity for each fixed P.
   The exact original/Haar discrepancy instead tends to the finite value L_P-J_G; pole-charge divergence alone is not a divergence assertion about that discrepancy.
5. Formula(RR16) is a full-logarithm Wiener lower bound.
   Under the additional hypothesis that G has a circle zero, W_*(log B_epsilon) tends to infinity as epsilon decreases to0.
   A circle zero of P alone is not used to conclude this.
   Neither a divergent denominator log nor fixed rational degree is claimed to exclude a correctly paid finite rational-symbol comparison.

These are exact fixed-input mechanisms and cost boundaries.
They supply no degree-uniform original-root/Haar comparison, all-parameter failure of the rational symbols themselves, original near-one sequence, or completion of D36 or G0001.
The remaining comparison is stated precisely at the end of the proof.

<a id="argument"></a>
<a id="rational-trace-regularizer"></a>
## Complete proof

The construction uses the unreduced E,F0,G of [C193](Yin_C_G0193_v1.md#statement); no canonical trace remainder is substituted.
That fixed result supplies the original trace congruence and its polynomial alternative.
The existing [C36 meromorphic argument](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost), with its [actual extraction review](../audits/reviews/Yin_R_G0788_v1.md#c36-rational-completion-extraction-finding), already proves the complete Blaschke pole accounting and shows why a denominator equal to1 on the original roots need not have small Haar logarithm.
The new work here is this specific congruence-preserving regularizer and its paid comparison, not a new general Poisson--Jensen theorem.
The rational-coefficient Laurent-polynomial accounts do not cover a nonconstant rational-function denominator merely because both are called rational.

### Definition, exact original value and fixed rational degree

Retain every hypothesis of C193: P is monic irreducible reciprocal nontorsion of degree d=2r, its constant coefficient is1, K=Q(alpha), and its actual trace field F=Q(alpha+alpha^(-1)) is totally real.
Write x=z+z^(-1), P=z^r Theta(x), and use C193's E0,F00,G0 in Q[x], whose pullbacks are E,F0,G.
Fix s in{1,-1}.
For a positive rational epsilon put

    H=Theta(x)G(z)=-z^(-8d)P(z)H35(z)/30375,
    A0=(E+sG)^2+F0^2,
    S_epsilon=s-(E0+sG0)Theta^2 G0/
                           (Theta^2 G0^2+epsilon^2),
    V_epsilon=-F00 Theta^2 G0/
                           (Theta^2 G0^2+epsilon^2),
    B_epsilon=(E+S_epsilon G)^2+
                        (F0+V_epsilon G)^2+G^2
       =G^2+A0 epsilon^4/(H^2+epsilon^2)^2.        (RR1)

Here S_epsilon G and V_epsilon G mean evaluation of the rational functions at x followed by multiplication by G(z).
Their common x-denominator is positive for every real x.
At every original trace conjugate Theta=0, so S_epsilon=s, V_epsilon=0 and

    B_epsilon(alpha)=Q_s=(e+s g)^2+f^2+g^2,
    L_P=(1/d)log Norm_K(B_epsilon(alpha))
       =(1/r)log Norm_F(Q_s)>=log2.               (RR2)

This uses the actual all-prime original-input theorem [C191v2](Yin_C_G0191_v2.md#statement), with its [whole independent R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding).
The present author contributed to that upstream theorem; its independent finding is reused, not relabeled as a new independent check.
The full residual case f=0 and e+s g=0 retains the stronger L_P>=(12/11)log2.
In every case Q_s is a positive nonzero algebraic integer at all r embeddings.
No rational circle value away from these original points is declared integral.

Cancellation in the displayed expression gives
S_epsilon=(s epsilon^2-E0 Theta^2 G0)/(Theta^2 G0^2+epsilon^2).
Its supplied numerator degree in x is23d/2, while that of V_epsilon is27d/2 and the common denominator degree is16d.
These degrees follow from deg E0=3d, deg F00=5d, deg G0=15d/2 and deg Theta=d/2, with their nonzero leading coefficients.
Both nonzero numerators have smaller degree than the denominator, so neither rational function is a polynomial.
Reduction of a common factor can only lower their rational degrees; no exact reduced-degree assertion is needed.
Thus the polynomial-shear fixed-degree obstruction in C176 is not directly applicable to these shears.
Their degree is independent of epsilon, but their coefficients and poles are not free.

On the circle G^2<=B_epsilon<=A0+G^2, and B_epsilon tends to G^2 outside the finite zero set of H.
The lower logarithm log G^2 is integrable and the upper logarithm log(A0+G^2) is bounded above and integrable.
Dominated convergence, applied to the nonnegative difference from log G^2, therefore gives

    J_G< I_epsilon=integral log B_epsilon dmu,
    lim_(epsilon down to0) I_epsilon=J_G.          (RR3)

Strictness holds because A0 is not the zero polynomial: E+sG is nonzero by its unequal component degrees.
Its zeros, and those of G, are finite, so the logarithmic difference is positive on a set of positive measure.
Possible common circle zeros cause no loss of integrability or multiplicity.
All integrals use Haar probability and no division by d.

<a id="rational-trace-exact-clearing"></a>
### Exact integer numerator, original scalar and clearing comparison

Write epsilon=p_epsilon/q_epsilon in lowest terms, with both integers positive, and set k0=30375 and L=972000.
Use the exact integer polynomial from C193,

    U_s=[13500 z^(9d/2)H23+32s H35]^2
                              +1215^2 z^(5d)H25^2,
    D_epsilon=k0^2 p_epsilon^2 z^(16d)
                          +q_epsilon^2 P^2 H35^2,
    N_epsilon=1024 H35^2 D_epsilon^2
                      +k0^4 p_epsilon^4 z^(32d)U_s.
                                                            (RR4)

Then the exact ordinary-polynomial representation and its normalized clearing are

    B_epsilon=z^(-15d)N_epsilon/(L^2 D_epsilon^2),
    R_epsilon=1+H^2/epsilon^2
              =z^(-16d)D_epsilon/(k0^2 p_epsilon^2),
    C_epsilon=B_epsilon R_epsilon^2
              =z^(-47d)N_epsilon/
                              (L^2 k0^4 p_epsilon^4)
              =A0+G^2(1+H^2/epsilon^2)^2.         (RR5)

D_epsilon is reciprocal of exact degree32d with leading and constant coefficient49q_epsilon^2.
It has no circle root, since its centered expression is k0^2 q_epsilon^2(H^2+epsilon^2)>0.
N_epsilon is reciprocal of exact degree94d and leading and constant coefficient1024*49^3*q_epsilon^4.
Indeed its first summand has degree94d and nonzero constant, while its second has degree62d and smallest exponent32d.
Both summands are centered at47d, and the second cannot cancel either endpoint.
The supplied degree of D_epsilon^2 is64d.
These are exact supplied polynomial degrees, not an assertion that N_epsilon/D_epsilon^2 is reduced at every parameter.
The scalar L^2 k0^4 p_epsilon^4 is supplied exactly; no minimal-denominator or primitive-content claim is made.

Since P is monic and Norm_K(alpha)=1, evaluation at every original root gives

    Res(P,D_epsilon)=(k0^2 p_epsilon^2)^d,
    Norm_K B_epsilon(alpha)
       =Res(P,N_epsilon)/
             [L^(2d)Res(P,D_epsilon)^2]
       =Res(P,N_epsilon)/(L^2 k0^4 p_epsilon^4)^d
       =Norm_K C_epsilon(alpha)=Norm_F(Q_s)^2.    (RR6)

In particular R_epsilon(alpha_i)=1 for every original conjugate, including circle conjugates.
The phases alpha_i^(15d), alpha_i^(16d) and alpha_i^(47d) have full norm1, rather than being removed from an individual embedding.
The full signed resultant equalities in(RR6) precede the positive norm floor.
No denominator resultant is omitted.

Put M_epsilon=sup_circle B_epsilon and M_C=sup_circle C_epsilon.
The ordinary degree94d numerator in(RR5) and its reciprocal centering give the legitimate polynomial return

    log2<=L_P<=log M_C+94m(P).                    (RR7)

For each inside root, the centered maximum-principle price is47d*abs(log|alpha_i|), and the same price follows outside by reciprocity.
Summing over the original degree d and using sum_i abs(log|alpha_i|)=2m(P) proves the coefficient94.
There is no replacement of M_C by its Haar geometric mean in(RR7).

Put J_V=integral log F0^2 dmu.
The decisive comparison for this particular clearing is pointwise:

    C_epsilon>=A0+G^2>=F0^2,
    integral log C_epsilon>=integral log(A0+G^2)
                              >=J_V.             (RR8)

Consequently, on each of the two actual inputs in the [J99 certified account](../computations/programs/Yin_J_G0099/readme.md#certified-results), every positive epsilon gives a cleared Haar mean strictly larger than log2.
That account and its [whole finite R377 finding](../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding) give J_V=2.363883636679 for the quartic P=z^4-z^3-z^2-z+1 and J_V=1.991241720952 for the Lehmer P=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1, each with certified absolute error below1e-10.
Both exceed log2, and no new calculation is performed.
It excludes this normalized clearing from the desired sub-log2 certificate on those inputs for all epsilon, even though the rational B_epsilon approaches J_G.
On another input it only says that this clearing cannot improve the old constant-shear Haar mean.
It does not exclude another rational representation or another normalization with its independently established arithmetic costs.

For a full coefficient budget, put
A_s0=(||H23||_1/72+||H35||_1/30375)^2+(||H25||_1/800)^2,
G1=||H35||_1/30375 and H1=||P H35||_1/30375.
Convolution gives

    term_count(N_epsilon)<=94d+1,
    ||N_epsilon/(2L^2 k0^4 p_epsilon^4)||_1
       <=[A_s0+G1^2(1+H1^2/epsilon^2)^2]/2.     (RR9)

These are supplied input-dependent upper budgets.
The fixed rational degree does not bound these coefficients.

<a id="rational-trace-finite-error"></a>
### A finite zero-compatible Haar error

Set R1=||P||_1, A=A_s0 R1^2 and D=16d.
The full polynomial P H35 has exact degree D and leading coefficient7.
For rho>0 let C(rho)=1+log_+(A/rho^2)/log2.
The bound H^2<=R1^2 G^2 on the circle gives

    0<I_epsilon-J_G
      <=2C(rho) E_(k0 rho)(P H35)
          +A epsilon^4/[rho^2(rho^2+epsilon^2)^2]
      <=D C(rho)(k0 rho/7)^(1/D)
          +A epsilon^4/rho^6.                   (RR10)

Here E_delta(Q)=(1/2)integral log(1+delta^2/|Q|^2)dmu.
For completeness, off the finite zero set,
log(B_epsilon/G^2)<=log(1+A epsilon^4/[H^2(H^2+epsilon^2)^2]).
On H^2<rho^2 drop the factor epsilon^4/(H^2+epsilon^2)^2<=1.
Use log(1+A/H^2)<=log_+(A/rho^2)+log(1+rho^2/H^2) there, and bound the small-set measure by the latter logarithm's integral divided by log2.
On H^2>=rho^2 use log(1+y)<=y and the monotonicity of h(h+epsilon^2)^2 for h>=0.
This proves the first line of(RR10).
The accepted [L358 all-root bound](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) gives
E_delta(P H35)<=D asinh((delta/M(P H35))^(1/D)/2).
Its actual scalar satisfies M(P H35)>=7, and asinh y<=y gives the last line.
All zeros of both P and H35, with all multiplicities, are included.

In particular a completely rational sufficient parameter for any0<eta<=1 is

    C_A=1+log_+(A(k0/7)^2)/log2,
    k=ceil(max{4,2log_2(2D(C_A+2D)/eta)}),
    rho=(7/k0)2^(-kD),
    M=ceil(max{1,(2A/(eta rho^6))^(1/4)}),
    epsilon=1/M.                                (RR11)

The same integer inequality k<=2^(k/2) used in C193 shows that the first term of(RR10) is at most eta/2.
Indeed C(rho)<=C_A+2kD<=k(C_A+2D).
The stated M makes the second term at most eta/2.
Thus I_epsilon-J_G<=eta with fixed supplied rational degrees but fully paid denominator coefficients.
This is a sufficient error budget, not an optimal parameter or a necessary precision for the actual input.

<a id="rational-trace-haar-denominator"></a>
### Exact Haar subtraction and the expense of clearing

Let J_R=integral log R_epsilon and J_C=integral log C_epsilon.
Scalar Jensen, with every supplied constant retained, yields

    I_epsilon=m(N_epsilon)-2m(D_epsilon)-2log L,
    J_R=m(D_epsilon)-2log(k0 p_epsilon)
       =2m(P)+J_G-2log epsilon
                           +2E_(k0 epsilon)(P H35),
    J_C=I_epsilon+2J_R.                           (RR12)

The middle identity follows from
integral log H^2=2m(P)+J_G and
log R_epsilon=log(H^2+epsilon^2)-2log epsilon.
The denominator is everywhere positive on the circle, so its logarithm has no integrability ambiguity.
In particular J_R>=0, and for each fixed original P,

    J_R+2log epsilon ->2m(P)+J_G,
    J_C+4log epsilon ->4m(P)+3J_G,
    J_C>=4m(P)+3J_G-4log epsilon.                 (RR13)

Thus J_C tends to infinity as epsilon decreases to0 even though I_epsilon tends to J_G.
A necessary condition for a cleared target J_C<=log2-eta, eta>=0, is
epsilon>=exp((4m(P)+3J_G-log2+eta)/4).
This is an input-dependent necessary condition for this clearing, not a uniform exclusion of all finite rational parameters.

The full original/Haar discrepancy has the exact decomposition

    L_P-I_epsilon=(L_P-J_C)+2J_R
          ->L_P-J_G.                             (RR14)

Both summands on the right can diverge with opposite signs.
Accordingly the divergence of J_R, or of a Fourier norm of log R_epsilon, does not by itself prove divergence of the full rational-symbol Fourier norm or an impossibility theorem for its transfer.
It proves the stated cost of replacing the rational function by this cleared polynomial.

<a id="rational-trace-pole-cost"></a>
### Full original pole charge and its fixed-input limit

Let the roots of D_epsilon inside and outside the circle be counted with their full polynomial multiplicities.
There are no roots on the circle or at0.
For disk points define the same positive Green term as C36,
gamma(z,rho)=log|(1-conjugate(rho)z)/(z-rho)|.
Set

    Pi_epsilon=(2/d)[
       sum_(|alpha_i|<1)sum_(|rho|<1,D_epsilon(rho)=0)
                                      gamma(alpha_i,rho)
       +sum_(|alpha_i|>1)sum_(|rho|>1,D_epsilon(rho)=0)
                           gamma(alpha_i^(-1),rho^(-1))].
    L_P<=log M_epsilon+30m(P)+Pi_epsilon,
    M_epsilon<=sup_circle(A0+G^2).               (RR15)

The factor2 is the denominator square, not a removed quadratic field multiplicity.
The original denominator values in(RR6) ensure no alpha_i is a pole.
To verify the specialization, z^(15d)B_epsilon is regular at0.
Multiply it by the finite Blaschke product with a zero of multiplicity twice that of each inside D_epsilon root.
All finite poles cancel, even if some were already removable, and its boundary modulus is at most M_epsilon.
The maximum principle gives the inside term15d*abs(log|alpha_i|) plus twice the Green sum.
Use the reciprocal identity B_epsilon(z)=B_epsilon(z^(-1)) for every outside root.
Circle roots contribute only log M_epsilon.
The full original-unit sum then pays30m(P), proving(RR15).
This is the existing C36 proof specialized to a scalar supremum; its different constant-covariance hypothesis is not silently applied to B_epsilon.

For this fixed input, the supplied pole charge actually tends to infinity as epsilon decreases to0, and the relevant approaching poles are genuine for all sufficiently small positive epsilon.
Here are the cancellation and limit details.
At a nonzero root rho of D_epsilon,
N_epsilon(rho)=k0^4 p_epsilon^4 rho^(32d)U_s(rho).
Therefore a common root of N_epsilon and D_epsilon must be one of the finitely many nonzero roots of the fixed U_s and must satisfy H(rho)^2=-epsilon^2.
This permits at most finitely many positive epsilon.
Outside that finite exceptional set, every finite D_epsilon root is a genuine pole of B_epsilon of twice its D_epsilon multiplicity.

The monic-unit nontorsion input has an original root alpha_* strictly inside the circle, by reciprocity and the accepted [Smy08-U001 Kronecker alternative](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
Only that retained statement and its original inspection scope are used; no new audit of the historical Kronecker proof is claimed.
The polynomial
D_epsilon/q_epsilon^2=P^2H35^2+k0^2 epsilon^2 z^(16d)
has fixed leading coefficient49 and converges coefficientwise to P^2H35^2.
Its roots are uniformly bounded for0<epsilon<=1 by the elementary coefficient root bound.
If no root approached alpha_*, a subsequence of complete bounded root lists would converge to a list whose product is P^2H35^2 but contains no alpha_*.
This contradicts P(alpha_*)=0.
Thus its closest root rho_epsilon approaches alpha_*; for small epsilon it lies inside the circle and differs from alpha_* by(RR6).
The numerator in gamma(alpha_*,rho_epsilon) tends to1-|alpha_*|^2>0, while the denominator tends to0.
This proves Pi_epsilon->infinity, with a genuine pole for sufficiently small epsilon.

The exact discrepancy in(RR14) remains finite in the same limit.
Hence this divergent positive-charge upper bound is a failure of a pole-discarding or uniformly bounded-pole use of the maximum principle, not evidence that the exact original discrepancy diverges.
It does not rule out a sharper numerator-minus-denominator comparison that retains cancellations.

<a id="rational-trace-remaining-interface"></a>
### Scope of the remaining transfer question

The rational family supplies a fixed-degree approach to J_G with the unchanged full arithmetic income.
Its particular normalized polynomial clearing has been completely priced and cannot improve the old constant-shear Haar test, while its direct maximum-principle return has the full positive charge(RR15).
Neither operation supplies a degree-uniform useful bound for the actual varying-input discrepancy.

The same energy argument as C193 gives a valid full-symbol necessary Fourier cost:

    W_*(log B_epsilon)>=log(integral B_epsilon)-I_epsilon
          >=log(integral G^2)-I_epsilon.          (RR16)

Here infinity is allowed and all nonzero signed frequencies are included.
If W_* is finite, the Fejer/local-continuity argument used in C193 applies to the integrable rational logarithm: its denominator has no circle zero and its numerator has only finitely many.
It gives log B_epsilon<=I_epsilon+W_* almost everywhere, and integration after exponentiation proves(RR16).
The C189v4 energy and fixed-support inputs therefore still force this cost to grow along any permitted hypothetical near-one input sequence with a fixed useful saving.
This does not estimate its product with a shrinking original-root discrepancy.

For a fixed P for which G has a circle zero, the proof-level mechanism of [C177](Yin_C_G0177_v1.md#polynomial-shear-actual-transfer-price) also gives W_*(log B_epsilon)->infinity.
Indeed a bounded subsequence of W_*, combined with the bounded means in(RR3), would bound log B_epsilon below uniformly almost everywhere by the same absolute-series argument.
Passing to the almost-everywhere limit would bound G^2 away from0, contrary to its continuity and its circle zero.
This argument uses the full logarithm and its limiting G^2; it does not infer the conclusion from log R_epsilon alone.
If only P, and not G, has a circle zero, this particular conclusion is not supplied.
An original-root value retained at an isolated circle point does not itself create a growing-amplitude logarithmic singularity.

What remains mathematically useful is a finite, input-dependent parameter choice together with a quantified upper bound for L_P-I_epsilon through the full numerator-minus-denominator or Fourier/radial comparison.
To exclude a specified small-m(P) range, that upper bound must fall below the guaranteed margin log2-I_epsilon under that range's hypotheses, or below the stronger residual margin when applicable.
A valid upper bound is not claimed to be smaller than the actual discrepancy of an existing input.
A bound on rational degree alone, a bound on the denominator resultant alone, or a separately favorable Haar limit is insufficient.
No uniform such comparison, original near-one sequence, all-parameter failure of the rational symbols themselves, or completion of D36 or G0001 is asserted.

<a id="exact-inputs"></a>
## Exact inputs and limits

| Input | Exact use and boundary |
| --- | --- |
| [C193](Yin_C_G0193_v1.md#argument) | Actual original domain, trace congruence, U_s and unreduced phases, polynomial comparison and the complete error/energy conventions. |
| [C191v2](Yin_C_G0191_v2.md#statement) and [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Full original norm floor and stronger residual floor; the present author's upstream contribution is disclosed. |
| [C36](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) and [R788](../audits/reviews/Yin_R_G0788_v1.md#c36-rational-completion-extraction-finding) | Complete Blaschke/Green pole method and existing denominator-cost distinction, with the scalar-supremum specialization proved here. |
| [L358](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Nonmonic full degree16d product and all repeated/circle zeros in(RR10)--(RR13). |
| [J99 certified components](../computations/programs/Yin_J_G0099/readme.md#certified-results) and [R377](../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding) | Existing certified J_V>log2 on the two original controls; no numerical rerun. |
| [C189v4](Yin_C_G0189_v4.md#argument) | Original G^2 energy and accepted fixed-support consequence in(RR16), not a direct polynomial coefficient theorem for a rational function. |
| [C177](Yin_C_G0177_v1.md#argument) | Full-logarithm Fejer argument and circle-zero condition; no inference from the denominator alone. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) | Accepted measure-one characterization at its retained statement/inspection scope, giving an off-circle root for the actual nontorsion integer unit. |
| Direct algebra and fixed-polynomial root factorization | Exact scalar/resultant identities, finite exceptional cancellation set and the supplied bounded-degree root-limit argument; no new external source or native computation. |

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:04 |
| status | proved |
| authority | Internal adoption within Yin's selected actual original-transfer and mixed-form inquiries. |
| reason | Adopt the entire rational trace-congruent regularizer through whole R471. The exact original norms, finite rational parameter and Haar limit retain every denominator, numerator and pole cost. The supplied clearing fails on both retained controls for all positive parameters, and its positive pole bound diverges at fixed input while the exact numerator-minus-denominator discrepancy stays finite. These are precise method limitations; the useful uniform rational transfer remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational mechanism](#statement) | Every original P and both signs, all positive rational epsilon, full arithmetic, convergence, degree/scalar, exact clearing, pole multiplicities and Fourier boundaries. |
| argument | [Complete proof](#argument) | Entire RR1--RR16 derivation and the finite exceptional-cancellation and original-root limit arguments. |
| dependency | [Actual unbuffered arithmetic](Yin_C_G0191_v2.md#statement) | Unchanged full original norm and stronger residual income, reused through whole R468 with upstream authorship disclosed. |
| dependency | [Trace-congruent polynomial input](Yin_C_G0193_v1.md#argument) | Exact centered functions, trace quotient values, U_s and complete finite-error conventions; no free rational-degree transfer is imported. |
| dependency | [All-root regularization](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Full nonmonic degree16d P H35, all zeros and actual leading scalar7. |
| dependency | [Meromorphic pole interface](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) | Complete inside/outside Blaschke method with every pole; scalar-supremum specialization proved locally. |
| dependency | [Original energy and support inputs](Yin_C_G0189_v4.md#argument) | G^2 energy and hypothetical near-one fixed-support escape for RR16, not a polynomial coefficient assertion for a rational function. |
| dependency | [Full-logarithm Fourier mechanism](Yin_C_G0177_v1.md#argument) | Fejer/local-continuity argument and the additional G-circle-zero hypothesis, with the rational specialization supplied locally. |
| dependency | [Certified original control components](../computations/programs/Yin_J_G0099/readme.md#certified-results) | Only the existing two J_V>log2 enclosures used in the all-epsilon clearing comparison; no native rerun. |
| dependency | [Kronecker and scalar normalization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact U001, specifically its height-normalization subsection and p.322 measure-one alternative for the required off-circle root; no new historical proof audit. |
| support | [Whole upstream arithmetic review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual independent review of the author's upstream C191 contribution, not review of this new construction. |
| support | [Actual meromorphic extraction review](../audits/reviews/Yin_R_G0788_v1.md#c36-rational-completion-extraction-finding) | Exact C36 proof and source/pole-sign scope. |
| support | [Independent finite control review](../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding) | Existing complete J99 numerical and exact-input scope; no new independent computation is claimed. |
| support | [Inputs and remaining boundary](#exact-inputs) | Nine exact input rows, shared author relationships, no new source/program and unresolved full rational transfer. |
| review | [Whole independent rational-regularizer finding](../audits/reviews/Yin_R_G0471_v1.md#rational-trace-regularizer-whole-independent-finding) | Entire actual RR1--RR16 proof, all nine inputs, exact degrees/scalars/resultants, finite error, complete pole multiplicities and cancellation exceptions, fixed-input limits and Fourier scope; noncontributor review with no mathematical repair. |

## Historical assessments

<a id="decision-initial"></a>
### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:44 |
| status | proof draft |
| review-status | unreviewed |
| reason | Register the complete rational trace-congruent mechanism, its finite error and unchanged full original norm, exact supplied clearing and pole costs, and the precise method-only failures. Separate whole noncontributor review remains required; no adopted uniform transfer or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational mechanism](#statement) | Every original P and both signs, all positive rational epsilon, full arithmetic, convergence, degree/scalar, exact clearing, pole multiplicities and Fourier boundaries. |
| argument | [Complete proof](#argument) | Entire RR1--RR16 derivation and the finite exceptional-cancellation and original-root limit arguments. |
| dependency | [Actual unbuffered arithmetic](Yin_C_G0191_v2.md#statement) | Unchanged full original norm and stronger residual income, reused through whole R468 with upstream authorship disclosed. |
| dependency | [Trace-congruent polynomial input](Yin_C_G0193_v1.md#argument) | Exact centered functions, trace quotient values, U_s and complete finite-error conventions; no free rational-degree transfer is imported. |
| dependency | [All-root regularization](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Full nonmonic degree16d P H35, all zeros and actual leading scalar7. |
| dependency | [Meromorphic pole interface](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) | Complete inside/outside Blaschke method with every pole; scalar-supremum specialization proved locally. |
| dependency | [Original energy and support inputs](Yin_C_G0189_v4.md#argument) | G^2 energy and hypothetical near-one fixed-support escape for RR16, not a polynomial coefficient assertion for a rational function. |
| dependency | [Full-logarithm Fourier mechanism](Yin_C_G0177_v1.md#argument) | Fejer/local-continuity argument and the additional G-circle-zero hypothesis, with the rational specialization supplied locally. |
| dependency | [Certified original control components](../computations/programs/Yin_J_G0099/readme.md#certified-results) | Only the existing two J_V>log2 enclosures used in the all-epsilon clearing comparison; no native rerun. |
| dependency | [Kronecker and scalar normalization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact U001, specifically its height-normalization subsection and p.322 measure-one alternative for the required off-circle root; no new historical proof audit. |
| support | [Whole upstream arithmetic review](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual independent review of the author's upstream C191 contribution, not review of this new construction. |
| support | [Actual meromorphic extraction review](../audits/reviews/Yin_R_G0788_v1.md#c36-rational-completion-extraction-finding) | Exact C36 proof and source/pole-sign scope. |
| support | [Independent finite control review](../audits/reviews/Yin_R_G0377_v1.md#two-input-component-finding) | Existing complete J99 numerical and exact-input scope; no new independent computation is claimed. |
| support | [Inputs and remaining boundary](#exact-inputs) | Nine exact input rows, shared author relationships, no new source/program and unresolved full rational transfer. |
