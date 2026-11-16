---
author: Yin
---

<a id="boy78-u001"></a>
# Boyd's fixed-delay search and near-integer Pisot seeds

<a id="fixed-delay-enumeration"></a>
## Fixed delays

In the [published edition](readme.md#editions), Section 4, equation (26), uses \(z^mP(z)+\epsilon P^*(z)\) for a Pisot minimal polynomial \(P\) and its reciprocal \(P^*(z)=z^{\deg P}P(1/z)\).
Section 5, Lemma 4, pp. 1254–1255, gives finiteness of Boyd's exact coefficient tree on a closed interval disjoint from the Pisot numbers and from \(1\), for fixed \(m\ge2\), and for \(m=1\) with the initial coefficient \(u_0\) fixed.
For the associated function of equation (28), \(u_0=|P(0)|\).
On p. 1255, the delay-two search in \([1.125,1.3]\) found 41 distinct Salem numbers from 576 seed polynomials, omitting two of the 43 known Salem numbers in that interval in 1978.
At delay three Boyd searched \([1.1,1.3]\) and found 22 seed polynomials.
For delays four through eight he reports respectively 6, 2, 2, 1 and 1 seeds on \((1,1.3]\).
On p. 1254 he observes that any nondegenerate closed interval above one containing no Salem number would imply a uniform gap above one, by taking positive powers.

<a id="near-integer-lemma"></a>
## Pisot seeds near an integer

Section 6, Lemma 5, p. 1256, takes \(q=|P(0)|>1\), a Pisot root \(\theta=q+\delta\), and the delay-one value \(\sigma\) for the sign \(\epsilon=\operatorname{sgn}P(0)\).
The convention following equation (28) gives \(\sigma=1\) when the construction has no root beyond one.
Equation (38) gives the upper bound
\[
  \sigma+\sigma^{-1}-2\ \le\ \delta\,\frac{(q+1)^2}{q(q-1)}.
\]
The coefficient is at most \(9/2\) for integers \(q\ge2\), since both \((q+1)/q\) and \((q+1)/(q-1)\) decrease with \(q\).
Thus an assumed Salem gap gives a positive lower bound on \(\delta\), uniform in \(q\), for seeds with \(P(0)=q\), whose plus construction gives a Salem number.
Boyd states this consequence just after (40).
The statement and reported search ranges were checked on 2026-11-16, without rerunning the historical computation.

<a id="negative-norm-cubic"></a>
## The cubic at the lower edge of the search near \(q\)

On 2026-11-16 agent-S for Yin inspected Section 6, printed page 1256, equations (39) and (40) and the paragraph after Lemma 5 in the [author-posted journal scan](readme.md#editions).
The displayed estimates compare the delay-one trace with the first series coefficient \(u_1\), then compare \(u_1\) with the Pisot root.
In the discussion of the least point of \(S_u\), Boyd gives the cubic \(z^3-(u-1)z^2-uz-u\).
Its negative constant coefficient matters for the signed delay-one construction.
The paper also reports a bounded calculation near \(u=9\), including 27 points of \(S_9\) in \([9,9.1]\), none with positive minimal-polynomial constant.
The [normalized series for the cubic](../../../ledger/Yin_L_G0462_v36.md#sign) is calculated directly from that polynomial.
