---
author: Yin
---

# Unit-circle roots and eventual reciprocity in each factor of the odd-prime square family

Provenance: project deduction from the Gaussian specialization and relative small-point equidistribution.
The statement and argument arose in the bounded discussion of the 7 November 2026 commit.
An integral formula for the off-circle fraction of a complete specialization has related precedents.
For example the discussion preceding Table 1 on printed p. 432 of [Stankov's paper](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.422.pdf) concerns complete reciprocal polynomials.
The present argument applies separately to each changing rational irreducible factor and derives its reciprocity.
The comparison with Stankov supplies context only.

<a id="statement"></a>
## Factorwise root counts

For each odd prime \(p\), let \(f\) be any monic irreducible rational factor of
\[
 H_p(z)=\frac{((z-1)\Phi_{8p}(z))^2+((z+1)\Phi_{4p}(z)^2)^2}{2}.
\]
Write \(e=\deg f\), and denote by \(N_{\ne1}(f)\) the number of its roots of modulus different from one.
Ignoring the finitely many undefined angles, set
\[
 r(\theta)=\frac{2\tan(\theta/2)\cos^2\theta}{\cos(2\theta)},\qquad
 \kappa=\frac{1}{2\pi}\operatorname{meas}\{\theta\in(-\pi,\pi):0<r(\theta)<2\}.
\]
Then
\[
 \sup_{f\mid H_p\ {\rm irreducible}}
 \left|N_{\ne1}(f)/e-\kappa\right|\longrightarrow0,
 \qquad 1/12\le\kappa<1/2 .
\]
Every irreducible factor of \(H_p\) is reciprocal for every sufficiently large prime \(p\).
Uniformly over those factors the fraction of roots strictly outside the unit circle tends to \(\kappa/2\).
The number of nonreal conjugate pairs of roots of the trace polynomial of such a factor is \((\kappa+o(1))e/4\).
In particular that number tends to infinity along any choice of factors.
The argument gives no explicit threshold on \(p\) and no rate of convergence.

<a id="inputs"></a>
## The Gaussian orbit and its limiting angular measure

The [odd-prime construction](../ledger/Yin_L_G0458_v4.md#prime-square-family-inputs) gives monicity, unit constant, absence of real roots and [absence of cyclotomic factors](../ledger/Yin_L_G0458_v4.md#prime-square-no-cyclotomic-factors).
The [height estimate](../ledger/Yin_L_G0458_v4.md#prime-square-root-height-upper) bounds the absolute logarithmic Weil height of every root by \(9\log 2/(2p-10)\) for \(p>5\).
Thus along any sequence of primes tending to infinity the roots have positive heights tending to zero.
Each fixed root can occur only finitely often, and their degrees tend to infinity by Northcott finiteness.

Set \(K=\mathbb Q(i)\), \(U=(z-1)(z^2+1)^2\), \(V=(z+1)(z^4+1)\) and \(W=2iV/(U-iV)\).
For each \(f\) choose a complex root \(\beta\) on the Gaussian component
\[
 t+t^{-1}=W(z),\qquad z=\beta,\quad t=\beta^{2p}.
\]
This choice is possible because \(A_p/B_p=\pm i\) at the roots and complex conjugation exchanges the signs.
The component identity and the absence of common zeros of \(U,V\) are recorded in the [Gaussian specialization](../ledger/Yin_L_G0458_v5.md#prime-template-absolute-components).
In particular a pole of \(W\) cannot be an actual solution.
Since \(i\in\mathbb Q(\beta)\), the \(K\)-orbit of \(\beta\) has size \(e/2\), and its complex conjugate supplies the other half of the rational orbit.
Both halves have the same modulus counts.

Apply [Baker and Rumely, Theorem 2.3](../audits/literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution) over \(K\) with the squaring map at its complex place.
The height and Haar measure identifications for this relative application are also worked out in the [earlier relative-orbit argument](../ledger/Yin_L_G0450_v5.md#moving-map-uniform-asymptotic).
It follows that the empirical measures of these complete \(K\)-orbits converge weakly on the sphere to Haar probability on the unit circle.
If necessary one passes to distinct roots on a subsequence, which suffices since a fixed root cannot recur infinitely often.
In particular a sector with fixed angular endpoints and a fixed open annulus around the unit circle has limiting mass equal to its angular length divided by \(2\pi\).

<a id="local-circle-test"></a>
## When proximity forces exact modulus one

On the unit circle, away from the finitely many exceptional points,
\[
 U(e^{i\theta})/V(e^{i\theta})=i\,r(\theta),\qquad
 W(e^{i\theta})=\frac{2}{r(\theta)-1}.
\]
The function is nonconstant rational in \(e^{i\theta}\), so its poles, the zeros of \(V\) and its level points at \(W=\pm2\) form a finite exceptional set.
On an arc with \(|W|>2\), no solution on that arc can have \(|z|=1\), since then \(t=z^{2p}\) is a unit complex number and \(t+t^{-1}\in[-2,2]\).

Now choose any compact subarc of \(|W|<2\) avoiding exceptional points.
Near each point of the arc the two solutions \(T_1(z),T_2(z)\) of \(T^2-W(z)T+1=0\) are distinct nonzero holomorphic functions.
Both have modulus one on the circle in that patch.
On a slightly smaller patch both logarithmic derivatives are bounded.
Integration along a short radial segment therefore gives
\[
 |\log |T_j(z)||\le C|\log |z||,\qquad j=1,2.
\]
Indeed the derivative in the radial coordinate \(s=\log|z|\) is the real part of \(zT_j'(z)/T_j(z)\).
A finite cover gives a common constant and an annular neighborhood for the compact subarc.
For an actual solution \(z\) there, \(T_j(z)=z^{2p}\) for one of the two branches.
Once \(2p>C\), the preceding inequality forces \(\log |z|=0\).
This argument controls exact equality of the moduli, which weak convergence alone cannot detect.

<a id="factorwise-consequences"></a>
## From arcs to factors

Remove short open arcs around the exceptional points with arbitrarily small total length.
On the remaining compact subarcs the two alternatives just proved classify the roots in a sufficiently thin fixed annulus by angle.
The relative orbit equidistribution bounds the omitted fraction by the Haar mass of the removed arcs in the limit, and the mass outside the annulus tends to zero.
Let the removed length decrease to zero.
The off-circle fraction tends to the Haar length of \(|W|>2\), which equals \(\kappa\), since \(|2/(r-1)|>2\) exactly for \(0<r<2\) away from the exceptional points.
This holds along every choice of factors, proving the stated uniform convergence.

For \(0<\theta<\pi/6\) one has \(0<r(\theta)\le4\tan(\pi/12)<2\), giving \(\kappa\ge1/12\).
Oddness of \(r\) bounds the measure of its positive set by half the circle.
Near \(\theta=\pi/4\) on the left, \(r>2\) on an interval of positive length, so \(\kappa<1/2\).
Consequently every sufficiently large \(p\) has a unit-circle conjugate in every factor.
That root is nonreal because \(H_p\) has no real roots.
Its inverse is its complex conjugate, so irreducibility over the rationals identifies \(f\) with its monic reciprocal associate.
Its constant term is \(+1\) because all roots occur in conjugate pairs and the constant term is a unit.
Hence strictly exterior roots account for half the off-circle roots.
For the reciprocal factor write \(f(z)=z^{e/2}Q_f(z+z^{-1})\).
Every off-circle root supplies a quartet \(z,\bar z,z^{-1},\bar z^{-1}\) of distinct roots and precisely one nonreal conjugate trace pair.
The absence of real roots ensures there is no other source of such quartets or any real off-circle pair.
This proves the trace count.

The fixed-single-pair signature in the [trace-cell construction](../ledger/Yin_L_G0462_v1.md#complex-trace-cells) can therefore meet this family only for finitely many primes.
The signature argument alone leaves the [sublinear degree criterion](../ledger/Yin_L_G0458_v4.md#prime-square-sublinear-factor-criterion) undecided.
The separate [eventual irreducibility theorem](Yin_C_G0877_v1.md#statement) excludes that possibility.

## Assessment history

### Decision unit-circle-roots

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:02 |
| status | proved |
| reason | The complete factorwise arc count, exact circle stabilization and reciprocity argument passed independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Uniform limiting root counts, eventual reciprocity and the trace signature. |
| argument | [Proof section](#inputs) | Gaussian orbit selection and relative equidistribution. |
| argument | [Proof section](#local-circle-test) | The two arc tests and exact unit modulus on compact interior arcs. |
| argument | [Proof section](#factorwise-consequences) | Uniform passage, explicit arc bounds and all factor conclusions. |
| review | [Independent finding](../audits/reviews/Yin_R_G1098_v1.md#unit-circle-roots) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-unit-circle-roots)

