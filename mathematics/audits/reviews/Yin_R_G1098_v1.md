---
author: Yin
---

# Factorwise height and unit-circle distribution in the odd-prime square family

A separately assigned agent for Yin checked the complete statements and arguments of the working-copy versions C873 v1 and C874 v1 at 2026-11-07T16:54 UTC.
The reviewer had no role in developing either proof and received the two fixed texts and their dependency locations without exploration discussion, author explanations or previous findings on these two claims.
The inputs common to both findings are the [family and endpoint identities](../../ledger/Yin_L_G0458_v4.md#prime-square-family-inputs), the [cyclotomic exclusion](../../ledger/Yin_L_G0458_v4.md#prime-square-no-cyclotomic-factors) and the [Gaussian specialization](../../ledger/Yin_L_G0458_v5.md#prime-template-specialization-limit).
For the equidistribution step I checked the [source unit](../literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution) against Baker and Rumely's Theorem 2.3 on printed pp. 631 and 659 and checked the [relative-orbit application](../../ledger/Yin_L_G0450_v5.md#moving-map-uniform-asymptotic).
The external theorem is used at statement and hypothesis level.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Factor heights](#factor-heights) | independently reviewed |
| [Unit-circle roots](#unit-circle-roots) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Factor heights](#factor-heights) | [C873 statement](../../claims/Yin_C_G0873_v1.md#statement) | Explicit bound, uniform limiting measure per degree and strict positivity of its limiting constant. |
| [Factor heights](#factor-heights) | [C873 argument](../../claims/Yin_C_G0873_v1.md#argument) | Gaussian embedding, coefficient norms and all local height bounds. |
| [Factor heights](#factor-heights) | [C873 finite contribution](../../claims/Yin_C_G0873_v1.md#dyadic-identity) | Local orbits, valuations at every finite place and absolute norm. |
| [Factor heights](#factor-heights) | [C873 limit](../../claims/Yin_C_G0873_v1.md#relative-limit) | Exact identity, projective continuity, complete relative orbits, torus integration and lower bound. |
| [Unit-circle roots](#unit-circle-roots) | [C874 statement](../../claims/Yin_C_G0874_v1.md#statement) | All rational irreducible factors, limiting fractions, eventual reciprocity and trace pairs. |
| [Unit-circle roots](#unit-circle-roots) | [C874 orbit argument](../../claims/Yin_C_G0874_v1.md#inputs) | Small heights, degree growth, Gaussian half-orbits and angular limits. |
| [Unit-circle roots](#unit-circle-roots) | [C874 local argument](../../claims/Yin_C_G0874_v1.md#local-circle-test) | Boundary values, compact arcs and the radial derivative estimate forcing exact unit modulus. |
| [Unit-circle roots](#unit-circle-roots) | [C874 consequences](../../claims/Yin_C_G0874_v1.md#factorwise-consequences) | Uniform passage to angles, the lower and strict upper bounds for the off-circle fraction, reciprocity and trace counting. |

<a id="factor-heights"></a>
## Height bounds and the limiting measure

The complete statement follows.
Coprimality gives \(i=A_p(\beta)/B_p(\beta)\) for one choice of embedding, and the specialized reciprocal quadratic has the two roots \(t=\beta^{2p}\) and \(t^{-1}\).
In increasing powers of \(z\) the coefficients of \(a\) are \((-i,1,-1-i,1+i,-i,1)\), while \(b=(i-1)V\).
Thus \(\|a\|_1=4+2\sqrt2\) dominates \(\|b\|_1=4\sqrt2\), also under complex conjugation.
The lack of common zeros gives \(a(\beta)\ne0\).
Taking the height of \([a(\beta):b(\beta)]\) and bounding the inverse of \(s\mapsto s-s^{-1}\) on \([1,\infty)\) gives the claimed archimedean factor \((1+\sqrt5)/2\).
At finite places unequal norms give the dominant term of \(t+t^{-1}\), while a unit gives \(s=1\).
Averaging \(|\log|t|_v|\) gives \(2h(t)=4p h(\beta)\), so subtracting the degree-five evaluation term gives \(4p-5\), positive even for \(p=3\).

At odd residue characteristic a nonunit \(a(\beta)\) would force \(b(\beta)\) nonunit by the trace equation for the unit \(t\).
The common reduction would be a common zero of \(U,V\), ruled out by \(V(1)=4\) and \(V(z)=2(z+1)\) when \(z^2=-1\).
At two, \((U-V)/(1-i)\) vanishes in the residue field, so \(a\) is a unit away from the root one.
The two roots above one form a single local orbit because each generates a field containing \(\mathbb Q_2(i)\) and there are only two roots with that reduction, counting multiplicity.
The valuation \(v_2(H_p(1))=1\) therefore gives \(v_2(\beta-1)=v_2(\beta+1)=1/2\) on that orbit.
It follows successively that \(v_2(\beta^2-1)=1\), \(v_2(\beta^2+1)\ge1\), \(v_2(\beta^4-1)\ge2\) and \(v_2(\beta^4+1)=1\).
Hence \(v_2(V)=3/2\), \(v_2(U)\ge5/2\) and \(v_2(a)=1\).
The [binary endpoint allocation](../../claims/Yin_C_G0871_v1.md#statement) and reduction of the linear factorization of \(f\) count \(\delta\) embeddings there, giving \(|N(a(\beta))|=2^\delta\).

The homogeneous quadratic measure stays continuous when its top coefficient vanishes, since normalized linear factors have compact coefficient pairs and their limit product is a nonzero form.
The leading \(z^5\) coefficient of \(a\) prevents a zero limiting form after scaling at infinity.
Averaging the logarithmic measure of the two reciprocal roots contributes \(4p h(\beta)\) from \(t\), and the leading coefficient contributes \(+\delta\log 2/e\).
Subtracting \(5h(\beta)\) to form the bounded continuous test yields the stated identity with the correction \(-\delta\log 2/e\) on solving for \((4p-5)h(\beta)\).
Positive heights tending to zero force degree growth by Northcott and give a further sequence of distinct roots in any subsequence.
Theorem 2.3 for squaring over \(\mathbb Q(i)\) applies to the complete orbit over this fixed field, and conjugation carries the other orbit and its test to the same Haar integral.
The positive part of the torus integrand is bounded and its inner log means are continuous, so integrating the negative part is justified even at torus zeros.
The exact template norm \(q\overline q=\mathcal G\) and the [complete-measure lower bound](../../ledger/Yin_L_G0458_v4.md#prime-square-original-factor-cost) give \(J\ge(\log2)/4\).
Applying the argument to an arbitrary purported exceptional sequence establishes uniformity over factors.
Neither an effective error estimate nor existence of factors with sublinear degree follows from this finding.

<a id="unit-circle-roots"></a>
## Exact placement of conjugates on the circle

The complete statement follows.
The [earlier height bound](../../ledger/Yin_L_G0458_v4.md#prime-square-root-height-upper) suffices for all large primes independently of C873.
For the sign selected by \(A_p/B_p=i\), one obtains \(W=2iV/(U-iV)\), with no pole at any actual solution.
The inclusion \(\mathbb Q(i)\subset\mathbb Q(\beta)\) gives a full orbit of \(e/2\) points for the fixed complex embedding and complex conjugation gives the other \(e/2\), with identical modulus counts.
Their relative equidistribution applies to fixed annular sectors because the angular boundaries meet the circle in finitely many points and the radial boundaries miss it.

On the circle \((z-1)/(z+1)=i\tan(\theta/2)\) and \((z^2+1)^2/(z^4+1)=2\cos^2\theta/\cos(2\theta)\), verifying the sign in \(W=2/(r-1)\).
When \(|W|>2\), even a single exact unit-circle solution is impossible.
On each compact good arc with \(|W|<2\), the two reciprocal simple branches start at modulus one, and shrinking the branch neighborhoods bounds \(|zT_j'/T_j|\) on radial segments from the circle.
A finite cover supplies both a common radial width and a constant \(C\) for the whole arc.
At a solution, \(2p|\log|z||\le C|\log|z||\) forces exact unit modulus for \(2p>C\).
The nonconstant rational map has finitely many poles and points with \(W=\pm2\), and the zeros of \(V\) are finite as well.
For any prescribed omitted angular length one may first fix the good arcs and their annulus and then take \(p\) large.
Every sequence of choices of factors has this limiting separation, giving the uniform fraction for \(0<r<2\).

The interval \((0,\pi/6)\) gives Haar mass \(1/12\), since \(r\le4\tan(\pi/12)<2\) there.
Oddness pairs positive and negative values, and an interval on the left of \(\pi/4\) has \(r>2\), proving the strict upper bound \(1/2\).
Thus all large-prime factors have a unit-circle conjugate.
Its inverse is also a root of the same irreducible rational factor, and absence of real roots makes the unit constant term positive.
The roots off the circle split into distinct quartets under conjugation and inversion.
For a nonreal member \(z\) of such a quartet, \(\Im(z+z^{-1})=(|z|-|z|^{-1})\sin(\arg z)\ne0\).
Two nonzero roots have equal trace exactly when they agree or are inverses, so each quartet gives precisely one nonreal trace pair and two exterior roots.
This proves both counts, and positive \(\kappa\) with uniform degree growth gives divergence of the number of trace pairs.
It rules out the [fixed one-pair trace signature](../../ledger/Yin_L_G0462_v1.md#complex-trace-cells) along an unbounded sequence of primes.
The argument provides no effective threshold for reciprocity and leaves the [existence of sublinear factor degrees](../../ledger/Yin_L_G0458_v4.md#prime-square-sublinear-factor-criterion) open.
The comparison with whole-specialization root fractions on printed p. 432 of [Stankov's published article](https://www.numdam.org/item/10.5802/crmath.422.pdf) is contextual, with no use of that article as proof of the factorwise statement.
