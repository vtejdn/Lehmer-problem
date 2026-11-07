---
author: Yin
---

# The limiting Mahler measure per degree of every factor in the odd-prime square family

<a id="statement"></a>
## Factorwise height estimates

For an odd prime \(p\), let \(A_p=(z-1)\Phi_{8p}\), \(B_p=(z+1)\Phi_{4p}^2\) and \(H_p=(A_p^2+B_p^2)/2\).
For a monic irreducible factor \(f\) over \(\mathbb Q\), let \(e=\deg f\), let \(\beta\) be a root, and write \(m(f)=e h(\beta)\), using the logarithmic Mahler measure and absolute logarithmic Weil height.
Put
\[
 U=(z-1)(z^2+1)^2,\qquad V=(z+1)(z^4+1),\qquad
 q(z,t)=\frac{U(t^2+1)-iV(t+1)^2}{1-i}.
\]
Write \(J=m_2(q)\) for its logarithmic Mahler measure on the two-dimensional unit torus, and put \(C=(4+2\sqrt2)(1+\sqrt5)/2\).
Then
\[
    m(f)\le \frac{e\log C}{4p-5},\qquad
    \sup_{f\mid H_p,\ f\ {\rm monic\ irreducible}}
          \left|(4p-5)\frac{m(f)}{\deg f}-J\right|\ \longrightarrow\ 0
          \quad(p\longrightarrow\infty).
\]
The constant satisfies \(J=m_2(q\overline q)/2\ge(\log 2)/4\), where the bar conjugates the coefficients.
The convergence assertion supplies no effective error rate.

<a id="argument"></a>
## Trace equation and explicit height bound

Use the [cyclotomic exclusion and unit-root properties](../ledger/Yin_L_G0458_v4.md#prime-square-family-inputs), the [absolute components and their specialization](../ledger/Yin_L_G0458_v5.md#prime-template-specialization-limit) and the [binary block and endpoint allocation](Yin_C_G0871_v1.md#statement).
Here the unit property means algebraic integrality with integral inverse.
The rational function \(A_p/B_p\) takes a value in \(\{i,-i\}\) at every root of \(H_p\), since its numerator and denominator are coprime.
Choose the embedding of \(\mathbb Q(i)\) in \(L=\mathbb Q(\beta)\) by setting \(i=A_p(\beta)/B_p(\beta)\).
Then \(t=\beta^{2p}\) satisfies \(q(\beta,t)=0\).
Write \(q=a(t^2+1)-bt\), where
\[
       a=(U-iV)/(1-i),\qquad b=2iV/(1-i).
\]
The polynomials \(a,b\) are Gaussian integral since \(U-V\) has even coefficients.
They have no common zero over \(\mathbb C\), because \(U,V\) have disjoint zero sets.
In particular \(a(\beta)\ne0\), and \(b(\beta)/a(\beta)=t+t^{-1}\).

The coefficient one-norm of \(a\) is \(4+2\sqrt2\), and that of \(b\) is \(4\sqrt2\).
At each archimedean place the logarithm of \(\max(|a(\beta)|,|b(\beta)|)\) is at most \(5\log^+|\beta|+\log(4+2\sqrt2)\).
At finite places the same inequality holds with the last constant removed by integrality.
Their projective height therefore bounds \(h(t+t^{-1})\) by \(5h(\beta)+\log(4+2\sqrt2)\).
At an archimedean place, \(s=\max(|t|,|t|^{-1})\) satisfies \(s-s^{-1}\le |t+t^{-1}|\), whence \(s\le(1+\sqrt5)\max(1,|t+t^{-1}|)/2\).
At a finite place, \(s\le\max(1,|t+t^{-1}|)\), by the ultrametric inequality with equality of the dominant norm when \(|t|\ne1\).
The normalized place average of \(\log s\) is \(2h(t)=4p h(\beta)\) by the product formula.
Together these estimates give the explicit bound.

<a id="dyadic-identity"></a>
## The exact finite contribution

Give the dyadic valuation its normalization \(v(2)=1\), and let \(\delta\in\{0,2\}\) be the multiplicity of \(z+1\) in the reduction of \(f\) modulo two.
The other conjugates have nonzero residues different from one.
At every finite place, \(a(\beta)\) is integral and \(b(\beta)=a(\beta)(t+t^{-1})\), with \(t\) a unit.
An odd residue characteristic cannot divide both evaluated coefficients.
Indeed, a common zero would have \(U=V=0\) in the residue field, whereas \(V(1)=4\) and at a root of \(z^2+1\) the value of \(V\) is \(2(z+1)\ne0\).
At characteristic two, \(a=V+(U-V)/(1-i)\) reduces to \(V=(z+1)^5\), so \(a(\beta)\) is again a unit except at the endpoint.

There are precisely two roots of \(H_p\) in \(\overline{\mathbb Q}_2\) reducing to one, counted with multiplicity, by reducing its complete monic integral factorization into linear factors.
They are conjugate over \(\mathbb Q_2\).
Indeed a local orbit through either root lies among these two roots and contains at least two elements, since the field of that root contains a square root of \(-1\), which is absent from \(\mathbb Q_2\) by reduction of an odd square modulo four.
The product formula for the linear factors at the argument \(1\), together with \(H_p(1)=2\), gives \(v(\beta-1)=1/2\) at each endpoint root.
Then \(v(\beta+1)=1/2\), \(v(\beta^2-1)=1\), \(v(\beta^2+1)\ge1\), and \(v(\beta^4-1)\ge2\), so \(v(\beta^4+1)=1\).
Consequently \(v(V(\beta))=3/2\) and \(v(U(\beta))\ge5/2\), hence \(v(a(\beta))=1\).
Counting all \(e\) dyadic embeddings of \(L\), exactly \(\delta\) give this valuation.
The absolute norm of \(a(\beta)\) is thus \(2^\delta\) in absolute value.

<a id="relative-limit"></a>
## Continuous relative-orbit test

For an embedding of \(\mathbb Q(i)\) in \(\mathbb C\), use the corresponding coefficients \(q_\sigma\) and define
\[
 g_\sigma(z)=\log M_t(q_\sigma(z,t))-5\log^+|z|,
\]
where \(M_t\) denotes the multiplicative one-variable Mahler measure.
This test extends continuously to the Riemann sphere.
Indeed for a nonzero binary quadratic form its homogeneous Mahler measure is the product, over any decomposition into two linear factors, of the maximum of the absolute values of the two coefficients of each factor.
This follows from the linear Mahler formula, also for a constant dehomogenized factor.
Continuity can be seen by scaling both coefficient pairs to have maximum norm one, taking convergent subsequences of these pairs, and using that the product of the two limiting linear forms is nonzero.
The remaining scalar then converges in absolute value to the Mahler measure of the limiting nonzero form.
For finite \(z\) the coefficients \(a,b\) do not vanish together.
At infinity divide by \(z^5\) before taking the measure, obtaining a limiting nonzero form since \(a\) has degree five.
This proves continuity including all degree drops and infinity.

At an archimedean embedding \(\tau:L\hookrightarrow\mathbb C\) the two roots of the specialized quadratic are \(\tau t,(\tau t)^{-1}\), including multiplicities.
Its logarithmic measure is \(\log|\tau a(\beta)|+|\log|\tau t||\).
As \(\beta,t\) are units, averaging over all complex embeddings and using the computed norm gives the exact identity
\[
 (4p-5)h(\beta)=
 \frac1e\sum_{\tau:L\hookrightarrow\mathbb C}
              g_{\tau|_{\mathbb Q(i)}}(\tau\beta)
 -\frac{\delta\log2}{e}.
\]
The explicit bound forces all root heights to zero as \(p\) grows.
Kronecker's theorem and the cyclotomic exclusion give each root positive height, so Northcott finiteness forces the minimum factor degree to tend to infinity.
In particular the endpoint correction vanishes uniformly.

Apply [Baker and Rumely, Theorem 2.3](../audits/literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution) over the fixed field \(\mathbb Q(i)\) with the map \(z\mapsto z^2\).
The associated canonical height is \(h\) and the archimedean canonical probability measure is normalized Haar measure on the circle, as in the [relative-orbit application to a different family](../ledger/Yin_L_G0450_v5.md#moving-map-uniform-asymptotic).
For an arbitrary sequence of primes tending to infinity and one chosen factor at each, choose a complex conjugate of each root if needed to give the fixed embedding of \(i\).
The theorem applies along every subsequence of distinct selected roots.
Positive heights converging to zero ensure that any subsequence has a further subsequence of distinct roots.
Thus every complete relative orbit average of the continuous test converges to its Haar integral, and the conjugate embedding has the same integral.
On the unit circle the subtracted term vanishes, and the iterated Mahler integral equals \(m_2(q)\) by Jensen's formula and integration in \(z\).
Here nonzero specialization for every circle point ensures continuous finite inner logarithmic means, while the positive part of the two-variable integrand is bounded on the compact torus, so the negative part is integrable.
An arbitrary violating sequence of factors would contradict the resulting convergence in the exact identity.
Finally \(q\overline q=\mathcal G\) for the [fixed template and its positive complete-measure limit](../ledger/Yin_L_G0458_v4.md#prime-square-original-factor-cost), where \(m_2(\mathcal G)\ge(\log2)/2\).
Conjugation preserves the torus integral and logarithmic measure is additive, giving the stated value and lower bound for \(J\).

## Scope

This project deduction grew from the discussion of the endpoint allocation on 2026-11-07 UTC.
The factorwise asymptotic controls the measure of a factor once its degree is known.
An actual positive-to-zero sequence would require global factors of sublinear degree in \(p\), a possibility subsequently excluded by the [eventual irreducibility theorem](Yin_C_G0877_v1.md#statement).
The external equidistribution theorem is used at the statement and applicability scope of its linked source unit.

## Assessment history

### Decision factor-heights

| Field | Value |
| --- | --- |
| date | 2026-11-07T17:02 |
| status | proved |
| reason | The explicit bound, exact finite-place correction and uniform factorwise limit passed complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All odd primes, every irreducible factor, both height bounds and the limiting constant. |
| argument | [Proof section](#argument) | The trace equation and explicit height bound. |
| argument | [Proof section](#dyadic-identity) | The exact norm including its dyadic contribution. |
| argument | [Proof section](#relative-limit) | The continuous test, orbit normalization and uniform limit. |
| review | [Independent finding](../audits/reviews/Yin_R_G1098_v1.md#factor-heights) | All of the selected statement and argument at the source scope specified in the finding. |

## Current assessment

[Selected decision](#decision-factor-heights)

