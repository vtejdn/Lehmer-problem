---
author: Yin
---

<a id="ope26c-u003"></a>
# Ope26c-U003: the degree-31 non-Pisot singular example and its arithmetic certificate

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26c; [retained PDF](../../../literature/pdf/Ope26c.pdf).

Passages: Manuscript dated 3 October 2026 at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; complete Section 6 (printed/PDF pp. 17--25) and Appendix A (pp. 25--35), including Theorem 6.1, root bounds, character identities, integral estimate, typical-prefix count and certificate error bounds; verification/verify_degree31.py.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148. The coordinating AI directly read all of nonpisot.tex, certificate.tex and the original 486-line Python verifier, rederived the analytic interfaces below, and visually checked the rendered certificate page 30. The original exact-arithmetic program and a separate scalar-margin program actually ran successfully; retained evidence is in J G0013. This is a source-proof review, not formal verification.


## Assessment, statement and conventions

**Audited within scope; no mathematical defect found in the complete Section 6 and Appendix A proof chain.**
This includes the analytic passage from finite computations to infinite products and singularity.
The exact program replay alone has a narrower scope, detailed in [J G0013](../../../computations/programs/Yin_J_G0013/readme.md).

All terminating decimals in this unit are exact rationals.
Set
$$p(t)=t^{31}-2t^{30}+\sum_{j=0}^{9}(t^{3j+1}-t^{3j}),\qquad
(t^2+t+1)p(t)=t^{33}-t^{32}-t^{31}-t^{30}-1.$$
Theorem 6.1 asserts that $p$ has a unique real root $\beta\in(1.8392,1.8393)$, that $\beta$ is not Pisot, and that the law of $\sum_{j\ge0}\epsilon_j\beta^{-j}$ for independent fair signs is singular.
Natural logarithms are used in the exponential estimates.
The proof works with fair bits and transfers measure type by an invertible affine change.

## Roots, lattice and characters

The supplied rational root disks have radius $10^{-35}$ and distinct centers.
Exact Horner residual and derivative estimates, followed by the displayed Taylor/Rouche bound, isolate 31 simple roots.
The expanding ones are $\beta,\alpha,\bar\alpha$, with
$$1.0002089<|\alpha|^2<1.0002094,\qquad |\alpha|^{-1}<.9999;$$
the other 28 roots are nonreal and have modulus less than .994.
Conjugation and the exhaustive disk count justify the real/nonreal classification.

Irreducibility of $p$ is not assumed.
If the minimal polynomial of $\beta$ were Pisot, its monic integral quotient in $p$ would have constant term of magnitude one and contain the weakly expanding pair.
If it contains no stable root its root-modulus product exceeds one; if it contains any, that product is at most $1.0002094\cdot.994<1$.
Both contradict its integral unit constant term.
The argument proves non-Pisot without silently asserting that every root of $p$ is a conjugate of $\beta$.

Reduction modulo the monic $p$ sends every finite word to $\mathbb Z^{31}$.
Evaluation at all 31 distinct roots is an invertible real-linear Vandermonde map, so word vectors lie in a fixed full lattice.
Stable coordinates and normalized expanding coordinates remain in fixed boxes.
Restoring expanding coordinates has real Jacobian
$$\mathcal M^N=(\beta|\alpha|^2)^N,\qquad \log\mathcal M<\log\beta+.0002094.$$
The complex coordinate counts twice in real dimension.
This again needs squarefreeness, not irreducibility.

The stable/expanding Laurent coefficient sequence $C_0(m)$ of $1/p$ decays exponentially in both directions; $C_1(m)=C_0(m+3)-C_0(m)+C_0(m-1)$.
Lagrange interpolation gives the required integral character identities, including the negative-index and word-reversal cases.
Centering fair bits accounts for the source's cosine normalization.
Infinite random-sign character products are justified by absolute summability, not by a finite-word approximation without a tail estimate.

## Positive factors and the integral bound

The predictor is the source's fixed combination of a constant, one lag-33 character and 753 rationally weighted shifted characters with lags 30 through 2000.
The coefficient norm is below .199.
The certified stationary moments satisfy
$$\mathbb E\operatorname{Re}(ZG)>.000210,\quad
\mathbb E|G|^2<.000145,\quad |\mathbb E Z^2G^2|<.000007.$$
These are verified bounds for the displayed predictor, not an optimization certificate.

The positive factors are
$$F_i=(1-\eta_i|G|^2)\{1+(1-|G|^2)(ZG+\overline{ZG})\}.$$
Only 21 positions of each block of length 22 are used.
The relation $\beta^3-\beta^2-\beta-1=\beta^{-30}$ yields the source's states $0,A^\pm,B^\pm,C^\pm$, with allowed terminal states $0,C^\pm$.
Enumerating admissible patterns gives cost $S_*<.081$.
The damping satisfies $\eta_i|G|^2\le S_*/3$, with mean $\eta_i/(1-S_*/3)<.101$.

The last-block expansion eliminates forbidden patterns using a squared-sinc weight with Fourier support in $[-.1,.1]$.
The first forbidden fast state has magnitude above 1.5, while the remaining fast and slow contributions are below 1.192 and .025.
For an incorrect terminal state the retained margin is above $.839-.005-.649$.
The slow terms use the exact near-cubic identity, at most five terms per selected position.
These margins ensure the relevant final frequencies lie outside the Fourier support, including their $\beta^i/|p'(\beta)|$ scale.
Admissible patterns are bounded by AM--GM with the stated damping.
Removing the last block preserves positivity of earlier factors; induction gives the required integral bound at every fixed weakly expanding coordinate.
No cancellation of an absolute value or invalid repeated use of positivity is needed.

For $x=|G|<.199$ and $u=ZG+\overline{ZG}$, the source's logarithm inequality holds for either sign of $u$; its cubic remainder has coefficient satisfying $C_*x<.136$.
Together with damping, the coefficient charged to $\mathbb E|G|^2$ is at most 1.237.
Consequently the average logarithmic gain per original position obeys
$$\gamma\ge\frac{21}{22}\bigl(2\cdot.000210-1.237\cdot.000145-.000007\bigr)>.000222.$$
The unused twenty-second position is included in this factor, rather than omitted from the normalization.

## From stationary expectations to singularity

Truncating the exponentially summable character coefficients uniformly approximates the bounded logarithmic factors.
For fixed truncation, sufficiently separated blocks depend on disjoint finite sets of bits, giving variance $O(1/N)$.
Taking the length limit before removing truncation proves that the finite-word product exceeds $\exp(.000220N)$ with probability tending to one; no uniform mixing rate is presumed.

Fixed small balls around distinct points of the evaluation lattice are disjoint.
Their perturbation changes the logarithm of the product by $O(1)$, uniformly in $N$: for every expanding root $r$, the relevant sum is bounded by $\sum_{i<N}|r|^{i-N}\le1/(|r|-1)$.
The weak pair makes this constant large but finite for this fixed polynomial.
The normalization Jacobian is $\mathcal M^N$, and the stable-coordinate box and weak-coordinate integral range have fixed size.
The integral bound therefore yields at most
$$C\exp\bigl((\log\mathcal M-.000216)N\bigr)$$
typical lattice points.
This counts points rather than words, so exact collisions do not invalidate the covering argument.

The projected prefixes, with their remaining tails, are covered by intervals of length $O(\beta^{-N})$.
Their total length is at most $C\exp(-.0000066N)$, while their Bernoulli mass tends to one.
Choosing a subsequence with summable lengths and summable missing masses gives a Lebesgue-null set of full measure.
This proves singularity; it does not equate singularity with a dimension deficit.

## Appendix A and actual finite evidence

The original verifier was inspected before execution.
It imports only `Fraction`, uses no file/network/process operations, and all finite assertions are integer/rational, with the prescribed rounding order.
Its 31 root disks, 753 rows, exact moment and Gram numerators and three upper-rounded products passed with assertions enabled.
Original program/license bytes, necessary exact certificate values and the separate 19 scalar-margin conditions and outcome are retained in [J G0013](../../../computations/programs/Yin_J_G0013/readme.md).
The latter checks import none of the source helpers; they do not independently reconstruct every root or moment.

The analytic error budget was separately checked.
Rounded Laurent-coefficient errors are below $7\cdot10^{-20}$ and $2.1\cdot10^{-19}$; trigonometric evaluation error is below $10^{-15}$; the finite 5100-factor error is below $3\cdot10^{-11}$.
The negative tail costs less than $5\cdot10^{-8}$, and the discarded strongly expanding part less than $10^{-20}$.
The weak tail is not dropped: its moments of orders 2,4,6 are summed geometrically with every complex cross term included.
Denominators exceed .00019; exponential evaluation contributes less than $4\cdot10^{-9}$, and the log-cosine remainder less than $3\cdot10^{-6}$.
The sum is below $3.055\cdot10^{-6}<\Delta=5\cdot10^{-6}$.

For the anisotropy term the corrected Gram quantity satisfies $T<.000116$, hence $\sqrt T<.011$.
On the exceptional index range $[-70,0]$, $|\tan(\pi f)|<.06$.
Expanding in the Walsh basis and applying the displayed Cauchy--Schwarz bound gives the source's $B_2<.011$, $B_1<.015$, $B_0<.0032$ and final anisotropy less than $.0000056968<.000007$.
These bounds retain the larger exceptional factors; treating every cosine as close to one would not prove the claimed estimate.

## Dependency and use boundary

This proof is independent of the classification and quartic Salem results.
Its required inputs are the explicitly checked certificate, elementary polynomial/lattice algebra, complex-analytic root isolation, Fourier identities, elementary probability and measure arguments.
No uninspected new external singularity theorem is used.
Historical priority and all unrelated cited papers were not audited.

The conclusion concerns one fixed polynomial, whose weak conjugates and all constants are retained.
It constructs no sequence of Mahler measures tending to one, proves no degree-uniform entropy gap, and does not resolve [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).
The original script is retained with OpenAI attribution and its upstream Apache license; a successful replay is not independent verification of the whole analytic proof.

## Independent final-count cross-check

A separate AI reviewer read the necessary source interfaces and independently rederived the final finite-word, thickening and counting argument, visually checking pp. 24--25.
It knew the coordinator had found no gap and that the finite certificate had passed; it was not a blind review and did not repeat the earlier arithmetic or automaton audit.
Its exact report follows.

## Finding and retained interfaces

**No mathematical defect found in the final finite-word-to-singularity argument.**
The review checks the lattice/Jacobian interface, finite-word passage in Proposition 6.9, Lemma 6.10 in full, and the proof of Theorem 6.1 from its typical-word and bounded-integral inputs.

The following inputs are retained at their stated source scope, not independently reverified from Appendix A or the arithmetic program here:

- Proposition 6.2: simple roots, expanding roots beta, alpha, conjugate(alpha), beta in (1.8392,1.8393), 1<|alpha|^2<1.0002094, and all remaining roots strictly contracting.
- Proposition 6.5: the specified finite predictor weights and certified moment inequalities.
- Lemma 6.6: damping bounds, in particular S_*<.081 and the normalized mean damping cost <.101.
- Proposition 6.7: for every N and every fixed complex x_alpha, the positive product has the stated bounded integral against psi in x_beta.
  Its automaton and Fourier-cancellation proof is outside this cross-check.

The exact interfaces were read in the source.
The results below are complete relative to them.
No numerical certificate replay, formal verification, source-original edit or authoritative material update was performed in this cross-check.

### Lattice, normalization, and determinant

Locators: PDF p. 18, Lemma 6.3 and (6.4)-(6.5); TeX lines 50-104.

Reduction modulo the monic degree-31 polynomial sends every word to an integer coefficient vector of length 31.
Evaluation at its 31 distinct roots is an invertible real-linear map, with one real coordinate and fifteen complex-conjugate pairs represented by two real coordinates each.
Its image of Z^31 is therefore a fixed full lattice.
Irreducibility of the polynomial is unnecessary for this statement.

For contracting roots, |y_r|<=1/(1-|r|); for expanding roots, |x_r|=|r^{-N}y_r|<=1/(|r|-1).
These are fixed, possibly large, boxes.
The three real expanding dimensions consist of the beta coordinate and the real and imaginary parts of the alpha coordinate.
Multiplication by alpha^N has real determinant |alpha|^{2N}, so the change of coordinates from (x_D,y_I) to (y_D,y_I) has determinant

    beta^N |alpha|^{2N} = M^N.

The conjugate pair is counted with the correct exponent two.
Any fixed choice of real coordinates or Lebesgue-volume normalization introduces only a constant factor, never an N-dependent determinant error.

### Stationary mean to uniformly random finite words

Locators: PDF pp. 23-24, Proposition 6.9 and (6.25)-(6.26); TeX lines 506-580.
Character interface: (6.9), TeX lines 146-170.

The mean bound correctly includes the fraction 21/22 of indices used:

    (21/22)*(2*.000210 - 1.237*.000145 - .000007)
      > .000222 > .000220.

The moment identity `2 E[(Re(ZG))^2] = E|G|^2 + Re E[Z^2G^2]` is exact, and E|G|^3<=x_* E|G|^2 supplies the stated cubic-cost bound.
The lower bound log(1-eta_i|G|^2)>=-eta_i|G|^2/(1-S_*/3) is valid because eta_i|G|^2<=S_*/3<1.
The direct logarithmic estimate in Lemma 6.8 was checked by its displayed derivative: its denominator stays positive, the positive-u derivative is bounded by the indicated positive part, and the negative-u interior critical point is a minimum.
Thus the numeric moments give the claimed logarithmic mean with the full N normalization, not only normalization by |J_N|.

For fixed truncation H of the absolutely summable C_A sequences, each periodic block sum depends on a finite interval of iid bits.
Distant block sums are independent, giving variance O_H(1/Q) for their average.
Character errors tend uniformly to zero as H grows; finite predictor weight and uniform positivity of every F_i transfer this to logarithms.
The order is first N tending to infinity for fixed H, then H growing.

For finite words coupled to stationary bits b_0,...,b_{N-1}, the truncated formulas agree for H+2000<=i<=N-1-H.
This includes every predictor shift (the type-1 term has center i-33).
Only O_H(1) boundary indices remain, their logarithms are uniformly bounded, and the omitted fixed initial i0 and incomplete last block cost only O(1) terms.
The finite/stationary normalized log difference therefore tends uniformly to zero.
Typical finite words have probability tending to one with threshold .000220 N.
No independence of the original infinite-range stationary factors was assumed.

### Fixed-radius thickening: no hidden N loss

Locators: PDF pp. 24-25, Lemma 6.10 and (6.27); TeX lines 592-624.
Factor definitions: TeX lines 199-235 and 371-381.

The fixed lattice has a positive minimum distance.
Choose rho<=1 strictly below half that distance; the corresponding balls about distinct vectors are disjoint and have one common positive volume.
An O(1) perturbation of y_r gives an O(|r|^{-N}) perturbation of x_r, so the change in the phase of Z_j^(0,N) is bounded by a constant times

    sum_{r in D} |r|^{j-N}/|p'(r)|.

Every underlying type-0 phase in F_i has index at most i.
In particular, the type-1 predictor Z_(i-33)^(1,N) uses indices i-36, i-33 and i-32; the other predictor indices are i-k with 30<=k<=2000.
Complex conjugation and the factors |G_i|^2 do not introduce a higher index.

The factors are uniformly positive: the damping part is at least 1-S_*/3 and the oscillatory part is at least 1-2x_*>0.
The finite coefficient sums and periodic damping coefficients are uniformly bounded.
Therefore log F_i is a uniformly Lipschitz function of its unit phases.
Its total variation is bounded by C sum_r |r|^{i-N}.

Summing i in J_N subset {0,...,N-1} gives, for each expanding root,

    sum_{i=0}^{N-1}|r|^{i-N} < 1/(|r|-1).

The weak expansion of alpha makes this constant large but finite and independent of N.
There is no need for it to be small.
For large enough N, the fixed loss C_thick is less than (.000220-.000216)N, proving the product lower bound exp(.000216N) throughout every typical ball.

### Positive integral to cardinality

Locators: PDF p. 25, (6.28); TeX lines 626-651.

Thickened balls still lie in fixed boxes in (x_D,y_I), since rho<=1 and |r|^{-N}<=1 in the expanding directions.
The real expanding box can safely be taken inside [-3,3]: 1/(beta-1)+1<3 under the stated beta bound.
The sinc-squared function psi has no zero on that interval, so its minimum there is positive.

For each complex expanding coordinate, nonnegativity and Proposition 6.7 bound the integral over the real box by a constant.
Integrating over the fixed complex and contracting boxes gives another fixed constant.
The product has no contracting-coordinate dependence.
Returning to y multiplies this integral by M^N.
Comparing it with the disjoint equal-volume typical balls gives exactly

    #Y_N <= C_count exp((log M-.000216)N).

Counting distinct vectors, rather than words, is required and is what the source does.
Coincident words do not invalidate the probability statement, and possible coincidences after projection only reduce the cover count.

### Cardinality to a full-measure Lebesgue-null set

Locators: PDF p. 25, (6.29) and final paragraph; TeX lines 653-675.
All logs in this section are natural.

With b_k=a_{N-1-k},

    beta*x_beta(a) = sum_{k=0}^{N-1} b_k beta^{-k}.

Thus the projection used is the actual finite bit-prefix distribution; the factor beta in front is correct.
Its remaining positive tail has maximum beta^{-N}/(1-beta^{-1}).
Attaching these closed intervals to all projected typical values gives a compact K_N with mu(K_N) at least the typical-word probability, hence tending to one.

The tail factor cancels beta^N in the volume estimate.
Since log M=log beta+log|alpha|^2<log beta+.0002094, the cover length is

    |K_N| <= C_cover exp((.0002094-.000216)N)
          = C_cover exp(-.0000066N).

The .000004N thickening margin and .0000066N final cover margin are different margins and are both correctly charged.
The 21/22 unused-index cost was already included in the typical-word rate and must not be charged again here.

Choose a strictly increasing subsequence N_j with complementary mu-mass less than 2^{-j}.
Summability makes liminf K_(N_j) have full mu-mass.
Its Lebesgue measure is zero because |K_(N_j)| tends to zero (or by Fatou for the indicators).
Finally the bit-to-sign affine map X -> 2X-(1-beta^{-1})^{-1} preserves singularity.
This establishes the claimed final implication without a pure-type assumption or any additional limiting regularity claim.
