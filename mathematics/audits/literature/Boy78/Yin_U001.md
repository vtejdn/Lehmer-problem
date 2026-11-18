---
author: Yin
---

<a id="boy78-u001"></a>
# Boyd's fixed-delay search and near-integer Pisot seeds

<a id="fixed-delay-enumeration"></a>
## Fixed delays

In the [published edition](readme.md#editions), Section 4, equation (26), uses \(z^mP(z)+\epsilon P^*(z)\) for a Pisot minimal polynomial \(P\) with reciprocal \(P^*(z)=z^{\deg P}P(1/z)\).
Boyd takes \(\epsilon=\operatorname{sgn}P(0)\) in the reported search.
Section 5, Lemma 4, pp. 1254–1255, gives finiteness of Boyd's exact coefficient tree on a closed interval disjoint from the Pisot numbers and from \(1\), for fixed \(m\ge2\), and for \(m=1\) with the initial coefficient \(u_0\) fixed.
For the associated function of equation (28), \(u_0=|P(0)|\).
On p. 1255, the delay-two search in \([1.125,1.3]\) found 41 distinct Salem numbers from 576 seed polynomials, omitting two of the 43 known Salem numbers in that interval in 1978.
In the same discussion Boyd attributes the bulk of the calculation to the initial coefficients \(1,2,4,8,16\) and notes that \(1/(1-2z)\) lies in the second derived set of the associated function class and has delay-two value one.
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

<a id="least-fixed-norm"></a>
## The fixed initial coefficient and the cubic minimum

In the paragraph following (40) on printed p. 1256, Boyd defines \(S_u\) through a meromorphic function associated to a Pisot number \(\theta\), with pole at \(1/\theta\) and constant Taylor coefficient \(u\).
Section 2 on p. 1246 permits the signed minimal polynomial divided by its reversal for the nonunits here, giving \(u=|P(0)|\).
For \(u\ge2\) Boyd gives the cubic \(X^3-(u-1)X^2-uX-u\) for the least nontrivial value and refers to the methods of [Dufresnoy and Pisot](../DP55/Yin_U001.md#coefficient-intervals).
The displayed cubic has constant coefficient \(-u\) and degree three, hence field norm \(+u\).
The integer seed \(\theta=u\) is treated separately when considering nonlinear minimal polynomials.
In the next sentence Boyd proposes \((u+\sqrt{u^2+4})/2\) as a candidate for the least accumulation point.
The article presents the cubic as the minimum and the accumulation-point formula as a conjectural observation. [Associated functions, p. 1246](../../../literature/pdf/Boy78.pdf#page=3) · [Minimum and proposed limit point, p. 1256](../../../literature/pdf/Boy78.pdf#page=13)

Direct inspection of the journal scan checked these two passages, the coefficients, the sign and the distinction between minimum and accumulation point.
Boyd gives a reference to a method rather than a calculation of the cubic bound at this location.
The [finite Schur proof](../../../ledger/Yin_L_G0462_v159.md#cubic) separately gives the sharp bound and equality case for nonlinear minimal polynomials of absolute constant \(u\).

<a id="narrow-branches"></a>
## Narrow coefficient intervals after the first discrepancy

On 2026-11-16 agent-S for Yin read Section 3, printed pages 1249–1251, in the [published scan](readme.md#editions).
Boyd relates the asymptotic widths of the real intervals for the next series coefficient to the circle mean of \(\log(1-|F|^2)\) and the pole of the associated function.
Lemma 1 gives the two reciprocal completions near a fixed derived function of width below \((1+\sqrt{17})/4\).
Its proof uses the integer size of a first discrepancy and contraction of the next coefficient interval.
Lemma 2 uses an interval of length below \(9/4\) to obtain the two possible departures at each later index.
These are fixed-function results; the [moving-constant argument](../../../ledger/Yin_L_G0462_v40.md#first-departure) controls an initial interval uniformly as \(q\) varies.

For the [delay-two application](../../../ledger/Yin_L_G0462_v116.md#completions), a research agent for Yin checked Section 2, pp. 1246–1247, and Section 3, pp. 1249–1251, of the [author-posted journal text](readme.md#editions) on 2026-11-16.
An associated function has integral Taylor coefficients, positive constant, a single simple pole \(1/\theta\) in the open disk and boundary modulus at most one.
At a limit \(F\) of distinct associated functions the width formula at the end of p. 1249 is
\[
        w(F)=\theta^2\exp\!\left(\int_{\mathbb T}\log(1-|F|^2)\,dm\right),
\]
where \(m\) is normalized Haar measure.
The distances from the central coefficient to the upper and lower permitted endpoints both tend to \(w(F)\).
In Lemma 1 and its proof on p. 1250, if \(w(F)<(1+\sqrt{17})/4\), a sufficiently late first discrepancy is \(+1\) or \(-1\).
Equation (23) bounds the length of the next interval, with limiting length \(2(w(F)^2-1)/w(F)<1\) after either discrepancy.
The subsequent interval lengths decrease, so at most one associated function continues each signed departure.
The project uses this uniqueness and checks the orientation and membership of its two reciprocal completions directly.
This inspection used Boyd's width formula and the coefficient interval recurrence as established inputs and followed the uniqueness deduction in Lemma 1.
