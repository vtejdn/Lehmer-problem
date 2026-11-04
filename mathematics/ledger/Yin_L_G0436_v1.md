---
author: Yin
---
# Quantitative positive reciprocal completion and its logarithmic Fourier price

Date: 2026-10-20T09:22.
Human author Yin.
Root authored the original completion on2026-10-15T15:39 and the explicit parameter and Fourier-price continuation on2026-10-20T09:16.
This fixed original author account combines the complete necessary original-value construction with the new quantitative argument.
The later [whole R444](../audits/reviews/Yin_R_G0444_v1.md#positive-completion-whole-independent-finding), [Claim extraction R446](../audits/reviews/Yin_R_G0446_v1.md#positive-completion-claim-extraction-finding) and [C175 adoption](../claims/Yin_C_G0175_v1.md#decision-whole-reviewed-2026-10-20) now own their actual later assessments.
It supplies explicit input-dependent prices, not a degree-uniform transfer theorem or a completed G0001 objective.
No numerical program or source acquisition was used; the original author account itself is not an independent review.

<a id="positive-reciprocal-completion-return"></a>
## Positive reciprocal completion and original values


Let P be monic irreducible reciprocal integer of degree d=2r, constant1, with a nontorsion unit root alpha and total measure m>0.
Put K=Q(alpha), P2(t)=P(t^2).
For every positive integer q define

    A_q(t)=q^2 P2(t)^2+t^d P(t)^2, deg A_q=4d,
    B_q(z)=z^(-2d) A_q(z)/(4q^2).                      (16)

P and P2 are reciprocal of their respective degrees, so for |z|=1,

    B_q(z)=|P(z^2)|^2/4+|P(z)|^2/(4q^2)>0.            (17)

Strict positivity follows because P and P2 have no common root.
If beta were one, beta and beta^2 would both be conjugates of the nontorsion alpha, contradicting the finite-order automorphism argument already accepted in [L59](Yin_L_G0059_v1.md#mixed-power-resultant-identities) and restated in [C149](../claims/Yin_C_G0149_v1.md#three-prime-nonvanishing).
This proof uses only actual cross-power nonvanishing; no assumed generic root separation or totally-real trace field is needed.

Thus A_q is an ordinary integer reciprocal polynomial with degree4d, constant and leading coefficient q^2, and no circle zeros.
It is not asserted irreducible or a new original minimal polynomial.
The normalized Laurent symbol B_q is rational, real and strictly positive on the circle.
It admits the already established finite positive-Gram/Fejer--Riesz descriptions at their precise scopes; those descriptions give no uniform degree/coefficient/denominator estimate for an unknown optimizer.
The construction is elementary positive completion, related to [C10v2](../claims/Yin_C_G0010_v2.md#arbitrary-nonzero-value-rational-lifting-extension), not a first-ever positive auxiliary or a replacement for its additional field-profile hypotheses.

At the ORIGINAL alpha, P(alpha)=0 and a=P(alpha^2)/2 is the old nonzero element of Z[alpha].
Therefore

    A_q(alpha)/(4q^2)=a^2,
    B_q(alpha)=alpha^(-2d)a^2 in Z[alpha], nonzero,
    Norm_K(A_q(alpha))=(4q^2)^d Norm_K(a)^2,
    log|Norm_K B_q(alpha)|/d=2log|Norm_K a|/d>=0.       (18)

The inverse alpha powers are integral because alpha is a unit.
Norm_K alpha=1 for this reciprocal even-degree P, so the Laurent monomial carries no rational norm cost.
Every original embedding and any smaller own field of a remain in the full K norm.
The degree4d and the actual denominator4q^2 are retained.

### Negative circle logarithm exists at each small-measure input

On the circle B_q decreases to |P(z^2)|^2/4 as q tends to infinity.
Its logarithm is bounded below by log(|P(z^2)|^2/4), which has integrable logarithmic zeros, and above by the bounded continuous log B_1.
These give an integrable domination for the logarithms.
The accepted scalar Mahler identity and Haar power invariance consequently yield

    integral log B_q dmu -> 2m-log4.                    (19)

Equivalently the left side is m(A_q)-log(4q^2), since the monomial has circle modulus1.
The limit is a fixed-input assertion, with P and d held fixed, not a uniform degree estimate.
Circle zeros of P2 do not invalidate logarithmic integrability or dominated convergence.

For EVERY actual P with0<m<log2, set Delta=log4-2m>0.
There exists an actual integer q=q(P) such that

    integral log B_q dmu<=-Delta/2<0.                   (20)

No algorithmic or uniform bound on q(P) is supplied by this limit.
The full original average is nonetheless nonnegative by(18).
Thus for that SAME selected positive symbol,

    (1/d)sum_i log|B_q(alpha_i)|-integral log B_q dmu
          >=Delta/2.                                   (21)

All logarithms at original roots exist by nonvanishing.
Their circle counterpart is log B_q by strict positivity.
This is an actual fixed-input discrepancy between the original-root average and Haar average, not an unpriced identification of the two distributions.

If a hypothetical sequence of such inputs had positive m tending to zero and q(P) were chosen as above, the right side would tend to log2.
No existence of that sequence is asserted.
This proves that strict circle positivity, degree-linear width and a negative Haar logarithm BY THEMSELVES cannot justify a moving-test error tending to zero with m: any transfer for these actual selected tests must still pay their varying coefficient/denominator/regularity costs.
It does not rule out another uniformly priced family or a useful restricted class.

### Consequence for the proposed homogeneous positive family

The scalar/Gram formulas of [L_F5](Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) concern the specified polynomial and its Haar determinant.
They do not replace the first term of(21) by the second.
The example already has one positive ordinary auxiliary, original integral norm income and negative fixed-input Haar cost; therefore repeating positivity with a larger degree30d or60d mixed-defect construction would not by itself resolve the necessary transfer.

The substantive remaining question is a controlled price on the ACTUAL joint auxiliary logarithm, or a different original-root arithmetic comparison.
The present completion supplies neither.
This bounded calculation records a useful failed shortcut and a precise reuse boundary, not a new Claim of unrestricted input coverage or Mahler gap.

<a id="completion-explicit-q-and-log-budget"></a>
## Explicit parameter selection and the complete logarithmic price

The question is whether the preceding completion's unspecified q(P) can be replaced by an explicit finite choice and a completely priced logarithmic Fourier budget, without claiming that a degree-dependent budget resolves the uniform transfer problem.
The local reuse screen checked the full original completion, [L358's zero-compatible root error](Yin_L_G0358_v1.md#zero-compatible-root-error), [the scalar weight baseline](Yin_L_G0431_v1.md#regularization-and-direction), [C113's original-root refinements](../claims/Yin_C_G0113_v1.md#statement), and the existing integer-adjugate/resultant methods of [L63](Yin_L_G0063_v1.md#coefficient-pairing-sylvester-presentation).
L358 already supplies the quantitative regularization step; the explicit integer linear-map argument below supplies the only coefficient separation bound needed here.
The logarithmic root expansion is the scalar Jensen/geometric-series identity at the normalization already used in L431 and L358, with its coefficients written out below.
No new external theorem, numerical integration, root isolation or program is used.
This original author stage preceded the later separate review and C175 adoption identified above.

### Exact original family and effective choice

Retain the preceding monic irreducible reciprocal integer unit P of even original degree d>=2 and m=m(P)>0, with P_2(z)=P(z^2), H=sum abs(p_i) and M=exp(m).
For integer q>=1 keep EXACTLY

    A_q=q^2 P_2^2+z^d P^2,
    B_q=z^(-2d)A_q/(4q^2)
       =(|P(z^2)|^2+q^(-2)|P(z)|^2)/4 on T,
    I_q=integral log B_q dmu.                         (Q1)

P and P_2 are coprime by the preceding finite-order conjugacy argument.
Thus B_q is strictly positive, A_q has no circle root, its actual degree is4d and its leading and constant coefficients are q^2.
The original integral value and full norm remain those of(18); no input or auxiliary is substituted.

The lower bound B_q>=|P(z^2)|^2/4 and the upper bound |P(z)|<=H imply

    0<=I_q-(2m-log4)
       <=2[m_(H/q)(P)-m(P)]
       <=2d asinh((H/(qM))^(1/d)/2)
       <=d(H/(qM))^(1/d).                            (Q2)

Here m_epsilon(P)=(1/2)integral log(|P|^2+epsilon^2), and the last two steps are the accepted L358 bound and asinh(x)<=x for x>=0.
Haar power invariance uses P(z^2) in the upper regularization without changing its original root degree d.
All inequalities hold for every q>=1; the integrable zeros in the lower comparison do not create an undefined integral.

If a supplied constant m0 satisfies0<m<=m0<log2, put eta=log4-2m0>0 and choose the actual integer

    q0=ceil(H(2d/eta)^d).
    Then I_(q0)<=-eta/2<0.                           (Q3)

Indeed M>=1 makes the last error in(Q2) at most eta/2 and2m-log4<=-eta.
This is an effective selection rule on the stated input class, not an input-uniform bound on q0, bit size or coefficient precision.
The original width remains4d, while the original denominator4q0^2 is fully retained.

### Integer separation with every coefficient charged

Consider the integer coefficient map

    (U,V) maps to U P+V P_2,
    deg U<2d, deg V<d,

between two free modules of rank3d, using the monomial coefficient bases.
Its matrix S has integer entries of absolute value at most H.
Over Q the map is injective: from UP=-VP_2 and coprimality, P divides V, forcing V=0 and then U=0.
Thus det S is a nonzero integer.
Apply the ordinary adjugate identity to the coefficient vector of1.
It gives integer U,V with UP+VP_2=det S and

    ||U||_1+||V||_1<=C,
    C=(3d)! H^(3d-1).                               (Q4)

Each adjugate entry is bounded by(3d-1)! H^(3d-1) by its finite determinant expansion, and there are3d coefficients in U,V together.
Consequently, at every z on T,

    max(|P(z)|,|P(z^2)|)>=1/C,
    |A_q(z)|=q^2|P(z^2)|^2+|P(z)|^2>=1/C^2.

The second equality uses reciprocity and the actual centering phase; its modulus has no cancellation on T.
This is a lower bound for the original positive symbol, with no assumed uniform resultant size or uncharged Bezout coefficients.

Set n=4d and H_A=(q^2+1)H^2, so ||A_q||_1<=H_A.
Every root beta of A_q has positive modulus and satisfies

    r_beta=min(|beta|,|beta|^(-1))<=1-delta_q,
    delta_q=1/[6n H_A C^2].                         (Q5)

To see this, let t=abs(|beta|-1) and choose the circle point on the same radial ray.
If t<=1/n, the segment stays in |z|<=1+1/n, and the derivative bound from the full coefficient sum is

    |A_q'(z)|<=n H_A(1+1/n)^(n-1)<3n H_A.

The circle lower bound therefore gives t>=1/(3n H_A C^2).
For an interior root,1-r_beta=t; for an exterior root in this segment it is t/|beta|>=t/2, proving(Q5).
If t>1/n, an interior root has1-r_beta>1/n and an exterior root has1-r_beta>1/(n+1); both exceed delta_q.
Multiplicities are retained and no numerical root computation is needed.

### Finite Fourier budget and a necessary divergent price

Use normalized Haar Fourier coefficients and

    W_*(log B_q)=sum_(h!=0)|widehat(log B_q)(h)|.

For a root beta away from T, its circle logarithm has constant log max(1,|beta|) and nonconstant terms obtained from

    log|1-r exp(it)|=-Re sum_(k>=1) r^k exp(ikt)/k.

Each root therefore contributes at most sum_(k>=1)r_beta^k/k=-log(1-r_beta) to the full signed nonconstant Wiener norm.
The scalar normalizer4q^2 and centering monomial change only the constant circle logarithm.
By(Q5), with all n roots counted,

    W_*(log B_q)<=n log(1/delta_q),
    sum_(|h|>T)|widehat(log B_q)(h)|
       <=n(1-delta_q)^(T+1)/[(T+1)delta_q]
       for every integer T>=0.                     (Q6)

The second bound follows by summing the geometric tail after1/k<=1/(T+1).
It prices the complete tail, rather than a numerical set of selected coefficients.
The expansions are absolutely convergent, which justifies the triangle inequality and the point evaluations used next.

If P has at least one circle root, choose zeta on T with P(zeta^2)=0.
Coprimality forces P(zeta)!=0, and(Q1)--(Q2) give

    W_*(log B_q)>=I_q-log B_q(zeta)
       >=2log q+2m-2log H.                          (Q7)

For the deterministic q0 in(Q3), this is at least2d log(2d/eta)+2m.
Thus the explicit worst-case-error selection has a logarithmic Fourier expense growing at least on the order of d log d on a growing-degree class with fixed eta, even though the ordinary polynomial width is only4d.
For each fixed circle-root input the expense also diverges as q tends to infinity.
These lower bounds do not say that q0 is necessary or optimal, and do not exclude a smaller useful q or another restricted input class.

The new result supplies an explicit finite negative-Haar completion and a fully priced finite Fourier approximation for the SAME original values.
Its coefficients, denominator, root separation and logarithmic budget are explicit but not degree-uniform.
Consequently it does not complete the original uniform transfer/coverage question, and it cannot justify replacing the original-root logarithmic average by the Haar average for free.
The remaining possible improvement is an arithmetic estimate that genuinely reduces these actual costs on a useful class, or a different original-root comparison; selecting a larger q under(Q3) alone does not provide it.
