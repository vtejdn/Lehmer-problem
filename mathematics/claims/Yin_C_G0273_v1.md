---
author: Yin
---

# Complete Mercat sextic binary support deficit with an exact Mahler certificate

This retains the entire original 2026-10-07 [L82 argument](../ledger/Yin_L_G0082_v1.md).
All original hypotheses, complete proofs, useful failures, source/evidence limits and remaining obligations are retained.
No source inspection or native calculation is newly executed.

## Statement

Let P(t)=t^6+t^5+t^4-t^3+t^2+t+1 and let alpha be any root.
For T_n(alpha)={sum_(j<n)epsilon_j alpha^j:epsilon_j in{0,1}}, let rho=lim_n log|T_n|/n, using natural logarithms.
The polynomial is irreducible and reciprocal, all its roots are algebraic units, and its six roots form one nonreal pair each inside, on and outside the unit circle.
Its trace cubic u^3+u^2-2u-3 has discriminant-87 and its unique real root satisfies3867/2500<u<1547/1000.
For the outside pair, M(P)=|alpha_out|^2 and

    511/256<M(P)<2, M(P)^8>(511/256)^8>252.

These inequalities have the complete exact elimination, monotonicity and four rational-sign proof below, without numerical roots or library factorization as premises.
For eight binary digits, the only nontrivial fibers are exactly the disjoint pairs of low-power-first bitmasks

    {8,119}, {136,247}, {16,238}, {17,239}.

Thus |T_8|=252 and for every n>=1,

    |T_n|<=252^floor(n/8) 2^(n mod8),
    rho<=log252/8<log M(P).

The same support counts apply to fair sign digits by an invertible affine transformation.
Regrouping binary digits into any fixed block alphabet T_k under alpha^k leaves this strict deficit per original time.
The full expanding-place binary attractor has zero two-dimensional volume.
An input-dependent larger finite alphabet can still attain total algebraic entropy.
This example is the one attributed to Paul Mercat's private communication by retained BV20 v4 p.31/[36]p.33; there is no separately acquired Mercat source.
It gives no near-one family, positive real Perron root, all-power degree theorem, probability-dimension assertion, universal small-window counterexample or Lehmer-gap conclusion.
J12 retains the original single-input diagnostic and actual separate finite verifier, including failed coarse endpoint31/20; numerical roots, factorization and sextic discriminant remain exploratory verifier fields.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:37 |
| status | open |
| reason | Register the complete original mathematics and exact existing inputs; actual current whole review and adoption follow separately. No independent-review claim, new source audit, native execution or Task resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Every exact sextic field/root/Mahler assertion, complete eight-word collision and all-length/regrouping deficit, zero-volume and finite-alphabet consequences, with exact original attribution/native/probability/small-window limits. |
| argument | [Entire original proof](#argument) | Entire original trace-field irreducibility and root-location proof, quartic elimination and exact rational signs, binary polynomial-division collision proof, block count and every geometric/alphabet consequence. |
| dependency | [Positive-volume and finite-alphabet controls](Yin_C_G0239_v1.md#positive-volume-support-interface) | Only full expanding-volume implies support attainment; the separate complete coordinate-floor finite alphabet is retained in the same C under its finite-alphabet heading. |
| dependency | [Complete finite-alphabet construction](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question) | Exact integral companion coordinate-floor alphabet attaining the full expanding determinant; no binary or uniform-block restriction. |
| support | [One expanding place](Yin_C_G0210_v1.md#pisot-salem-attainment) | Existing real one-expanding Pisot/Salem equality is only a comparison; the sextic outside roots are a nonreal pair. |
| support | [Source-reported example](../audits/literature/BV20/Yin_U002.md#bv20-u002) | Only the original v4 p31 sextic/eighth-support report and p33[36] private-communication attribution, with separately retained10/6 and10/7 inspection depths; all strengthened exact algebra is proved here. |
| support | [Complete retained native diagnostic](../computations/programs/Yin_J_G0012/readme.md#results-and-limits) | Original probe.py/verify.py and both retained JSON files, finite32,640 divisions/eight powers/rational comparisons and failed coarse endpoint; current inspection is full static reading/AST/JSON only, no rerun or exploratory-field certification. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:45 |
| status | proved |
| reason | Adopt the complete original irreducible sextic, exact rational Mahler certificate, full binary collision/all-length/regrouping proof and geometric/alphabet consequences after actual whole self-review. BV20/Mercat attribution and the two historical source-inspection depths remain exact; J12 was fully statically read, not rerun, and its exploratory and failed fields remain qualified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every exact sextic field/root/Mahler assertion, complete eight-word collision and all-length/regrouping deficit, zero-volume and finite-alphabet consequences, with exact original attribution/native/probability/small-window limits. |
| argument | [Argument](#argument) | Entire original trace-field irreducibility and root-location proof, quartic elimination and exact rational signs, binary polynomial-division collision proof, block count and every geometric/alphabet consequence. |
| dependency | [Dependency](Yin_C_G0239_v1.md#positive-volume-support-interface) | Only full expanding-volume implies support attainment; the separate complete coordinate-floor finite alphabet is retained in the same C under its finite-alphabet heading. |
| dependency | [Dependency](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question) | Exact integral companion coordinate-floor alphabet attaining the full expanding determinant; no binary or uniform-block restriction. |
| support | [Support](Yin_C_G0210_v1.md#pisot-salem-attainment) | Existing real one-expanding Pisot/Salem equality is only a comparison; the sextic outside roots are a nonreal pair. |
| support | [Support](../audits/literature/BV20/Yin_U002.md#bv20-u002) | Only the original v4 p31 sextic/eighth-support report and p33[36] private-communication attribution, with separately retained10/6 and10/7 inspection depths; all strengthened exact algebra is proved here. |
| support | [Support](../computations/programs/Yin_J_G0012/readme.md#results-and-limits) | Original probe.py/verify.py and both retained JSON files, finite32,640 divisions/eight powers/rational comparisons and failed coarse endpoint; current inspection is full static reading/AST/JSON only, no rerun or exploratory-field certification. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0533_v1.md#current-mercat-sextic-finding) | Entire current statement, complete original argument and all selected interfaces at their exact scope, self-reviewed; old findings keep their original fixed inputs and relationships. |

## Complete retained argument

<a id="argument"></a>

<a id="binary-support-counterexample-source"></a>
### Retained source and exact question

The already retained [BV20 v4](../literature/pdf/BV20.pdf), arXiv:1510.04043v4, 23 April 2021, printed/PDF p.31, final paragraph before the references, explicitly gives

\[
 P(t)=t^6+t^5+t^4-t^3+t^2+t+1
 \tag{1}
\]

as an example with \(M(P)<2\) and strictly smaller binary support growth than \(\log M(P)\).
It attributes the observation to Mercat, bibliography item [36], “Private communication”, on p.33.
The stated check is that the eighth support has cardinality less than \(M(P)^8\).
Thus this is a published-in-the-retained-preprint report, not a separately acquired Mercat source.
The actual retained page p.31 was extracted and visually inspected in this round; no communication with the authors occurred.
Existing [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001) owns the artifact identity and previous inspection boundaries.
The source uses base-2 logarithms; this note uses natural logarithms.

For any root \(\alpha\) of (1), put

\[
 T_n(\alpha)=\left\{\sum_{j=0}^{n-1}\epsilon_j\alpha^j:
                    \epsilon_j\in\{0,1\}\right\},\qquad
 \rho(\alpha)=\lim_{n\to\infty}\frac{\log|T_n(\alpha)|}{n}.
\]

The limit exists by subadditivity.
Replacing binary digits by fair signs changes the values by an invertible affine transformation, so the support counts are exactly the source's counts.
We prove directly

\[
 |T_8(\alpha)|=252,
 \qquad \frac{511}{256}<M(P)<2,
 \qquad
 \rho(\alpha)\le\frac{\log252}{8}<\log M(P).
 \tag{2}
\]

This settles the general equality question negatively, even for irreducible reciprocal algebraic units.
It does not furnish a near-one family, a positive real Perron root, or a counterexample to equality on a smaller range such as \(M<\theta_0\), where \(\theta_0\) is the plastic constant.
No all-power degree-preservation claim is needed.

<a id="binary-support-counterexample-algebra"></a>
### Irreducibility and conjugate locations

Writing \(u=t+t^{-1}\), one has

\[
 t^{-3}P(t)=T(u),\qquad T(u)=u^3+u^2-2u-3.
 \tag{3}
\]

The only possible rational roots of \(T\) are \(\pm1,\pm3\), and none is a root.
Thus \(T\) is irreducible.
Its discriminant is \(-87<0\), so it has exactly one real root \(u\) and two nonreal conjugate roots.
The exact evaluations

\[
 T(3867/2500)=-2362137/15625000000<0,
 \qquad T(1547/1000)=1503323/10^9>0
 \tag{4}
\]

give \(3867/2500<u<1547/1000<2\).
In the real embedding of \(\mathbb Q(u)\), \(u^2-4<0\), hence \(u^2-4\) is not a square in that field.
Therefore \(t^2-ut+1\) is irreducible over \(\mathbb Q(u)\), and each of its roots has degree six over \(\mathbb Q\).
Since it is a root of the monic degree-six polynomial \(P\), this proves irreducibility of \(P\).
Its constant coefficient is one, so all its roots are units.

The two roots over the real trace \(u\in(-2,2)\) lie on the unit circle and are nonreal.
A root of \(t^2-zt+1\) for either nonreal trace \(z\) cannot be real or have modulus one, since both possibilities would make \(t+t^{-1}\) real.
Each such quadratic has product one, hence one root inside and one outside the circle.
Complex conjugation pairs the two outside roots and the two inside roots.
Consequently \(P\) has exactly one nonreal conjugate pair in each of the inside, unit-circle, and outside regions.
In particular, if \(\alpha\) is an outside root, then

\[
 M:=M(P)=\alpha\overline\alpha=|\alpha|^2>1.
\]

### A short rational Mahler certificate

Divide (1) by the unit-circle quadratic:

\[
 P(t)=(t^2-ut+1)
 \bigl(t^4+(1+u)t^3+(u^2+u)t^2+(1+u)t+1\bigr).
\]

Let \(s=\alpha+\overline\alpha\in\mathbb R\), with the outside pair chosen above.
The quartic is

\[
 (t^2-st+M)(t^2-(s/M)t+M^{-1}).
\]

Comparing the cubic and quadratic coefficients gives

\[
 -s(1+M^{-1})=1+u,
 \qquad M+M^{-1}+s^2/M=u^2+u.
\]

With \(x=M+M^{-1}>2\), elimination yields

\[
 F(x,u):=x^2+(2-u^2-u)x+1-u^2=0.                 \tag{5}
\]

For the interval (4), \(F\) strictly increases with \(x\ge2\): its derivative is \(2x+2-u^2-u>0\), for example using \(u<8/5\).
It strictly decreases with positive \(u\).
Exact rational arithmetic gives

\[
 F\left(\frac{511}{256}+\frac{256}{511},\frac{3867}{2500}\right)
 =-\frac{120653495247}{6684697600000000}<0,
 \qquad
 F\left(\frac52,\frac{1547}{1000}\right)=\frac{12537}{2000000}>0.
 \tag{6}
\]

Monotonicity and (4)--(5) place \(M+M^{-1}\) strictly between the two arguments in (6).
Since \(y\mapsto y+y^{-1}\) is strictly increasing for \(y>1\), this proves \(511/256<M<2\).
Finally, strict convexity, or strict Bernoulli's inequality, gives

\[
 M^8>\left(\frac{511}{256}\right)^8
 =256(1-1/512)^8>256(1-8/512)=252.               \tag{7}
\]

The exact rational signs, rather than a numerical root approximation, are the certificate.

<a id="binary-support-counterexample-collisions"></a>
### Exactly four collisions at length eight

If two binary polynomials of degree at most seven take the same value at \(\alpha\), their difference \(R\), with coefficients in \(\{-1,0,1\}\), is divisible by the irreducible monic \(P\).
Monic polynomial division gives

\[
 R(t)=P(t)(a t+b),\qquad a,b\in\mathbb Z.
\]

The constant and degree-seven coefficients give \(a,b\in\{-1,0,1\}\).
If both are nonzero, either the degree-one coefficient \(a+b\) or the degree-three coefficient \(a-b\) has absolute value two.
Hence any nonzero binary collision difference is exactly \(\pm P\) or \(\pm tP\).

Encode a binary word by the integer \(\sum_{j=0}^7\epsilon_j2^j\), with the low bit recording the constant coefficient.
The positive and negative masks of \(P\) are 119 and 8, with the free degree-seven bit; those of \(tP\) are 238 and 16, with the free constant bit.
Thus the only four unordered collision pairs are

\[
 \{8,119\},\quad\{136,247\},\quad\{16,238\},\quad\{17,239\}.
 \tag{8}
\]

Their eight endpoints are distinct, so there are no larger fibers.
The other 248 words are singletons.
Therefore \(|T_8|=248+4=252\).
The block decomposition also gives the all-length upper bound

\[
 |T_n(\alpha)|\le252^{\lfloor n/8\rfloor}2^{n\bmod8}.
 \tag{9}
\]

Equations (7) and (9) prove (2).
This is a support-count proof.
Shannon entropy is at most support entropy, but the converse comparison is not used.

### Consequences and exact remaining scope

1. A fixed binary cyclic alphabet can fail to realize the total algebraic entropy \(m(P)=\log M(P)\), although \(M(P)<2\).
   Grouping consecutive binary digits into blocks does not remove the loss: using alphabet \(T_k(\alpha)\) under multiplication by \(\alpha^k\) produces exactly \(T_{kn}(\alpha)\), so its entropy per original time remains \(\rho(\alpha)\).
2. The full expanding-place binary attractor for this example has zero two-dimensional Lebesgue measure.
   Indeed the positive-volume argument in [L G0035](Yin_C_G0239_v1.md#positive-volume-support-interface) would give \(|T_n|\ge M^n\) at every length, contradicting (2).
   Thus even an irreducible unit with expanding determinant below two need not have a positive-volume binary attractor.
   This conclusion does not supply a dimension formula or a statement about the probability weights on that attractor.
3. A parameter-dependent finite alphabet may still attain the total entropy.
   The explicit coordinate-floor alphabet in [L G0032](Yin_C_G0239_v1.md#finite-alphabet-capture-and-the-remaining-arithmetic-question), section “Finite-alphabet capture and the remaining arithmetic question”, supplies that fact for integral companion automorphisms.
   The obstruction here concerns the specified binary cyclic alphabet and its regroupings, not every finite alphabet.
4. The one-real-expanding Pisot/Salem equality in [L G0007](Yin_C_G0210_v1.md#pisot-salem-attainment) is consistent with this example: the outside roots here are a nonreal pair.
   The general equality can no longer be used as a route premise.
   A replacement must state its actual extra hypothesis, or retain the accepted proportional lower bound from BV20.
   No inference about a universal near-one entropy gap follows from this single counterexample near measure two.
