---
author: Yin
---

# Small residue clusters and prescribed primes for the original unit

<a id="statement"></a>
## Uniformity below three times the degree

Let \(P\) be the monic irreducible minimum of a nontorsion unit \(\alpha\), with degree \(e\ge2\) and positive logarithmic measure \(h=m(P)\le1\).
At a prime \(p\), let \(M_p\) be the largest multiplicity of a root of \(\bar P\) over \(\overline{\mathbb F}_p\).
If \(p\le3e\) and \(P\) is not of the form \(Q(X^p)\), then
\[
 \frac{\min(M_p,p)}e\ll e^{-1/4}
       +\frac{\log\log(3p)}{\log p}
       +\sqrt{\frac{p h}{e\log p}}.                                    \tag{1}
\]
All implied constants are absolute.
In particular there is an absolute \(C\) such that for all sufficiently large \(e\) and primes
\[
      C e\frac{\log\log(3e)}{\log(3e)}\le p\le 3e                      \tag{2}
\]
one has \(p\ge3M_p\) unless \(P=Q(X^p)\).
At each such noncomposition prime the [divided-difference determinant](Yin_C_G0901_v4.md#determinant) has its stated valuation for every integer offset prime to \(p\), and the same holds at \(p\ge3e\).

For every sequence of original reciprocal nontorsion unit minima of degrees \(e\to\infty\) with \(h\to0\), and every fixed \(a>0\), the [ordinary two-row test](Yin_C_G0345_v408.md#statement) has witnesses for these same polynomials at **every** prime \(p\ge ae\).
Their row widths are \(e+o(e)\), and their normalized log heights tend to zero uniformly over these primes.
Both assertions hold for all sufficiently large degrees on the sequence.
Hence an arbitrary prescribed prime \(p(e)\ge ae\) suffices in the [finite degree criterion](Yin_C_G0901_v2.md#gap), without a change of the input polynomial.
A quantitative sublinear range follows below.

<a id="local"></a>
## Localizing the divided differences

In a Galois splitting field over \(\mathbb Q_p\), the inertia orbit of a root \(x\) has size equal to the ramification index of \(\mathbb Q_p(x)\).
Indeed, if \(I\) is inertia and \(H\) fixes \(x\), the inertia subgroup of the splitting field over \(\mathbb Q_p(x)\) is \(I\cap H\), and multiplicativity of ramification indices gives the orbit size \([I:I\cap H]\).
This orbit stays in the residue class of \(x\).
If the class has size \(m\), its Teichmüller lift \(\omega\) belongs to \(\mathbb Q_p(x)\), and consequently \(v_p(x/\omega-1)\ge1/m\) with \(v_p(p)=1\).

When \(p\ge3M_p\), the proof of the [local series](Yin_C_G0901_v4.md#series) gives \(v_p((x^p/\omega^p-1)/p)\ge1/M_p>1/(p-1)\).
Powering therefore preserves all distinct conjugates: different residues have distinct images under Frobenius, and two inputs of the same residue cannot differ by a nontrivial \(p\)-th root of unity since their ratio belongs to \(v_p(u-1)>1/(p-1)\).
In particular \(\deg(\alpha^p)=e\).
In the [matrix reduction](Yin_C_G0901_v4.md#reduction) each diagonal divided difference has \(d=a+b+1\le2M_p-1\), and each off-diagonal one has \(d=a+b\le2M_p-2\).
All its node valuations are at least \(1/M_p\).
The tail bound for total degrees \(n\ge p\) is now at least \((n-d)/M_p-(n-1)/(p-1)\), positive at \(p\) and increasing thereafter.
The factorials in every reduced diagonal block remain units.
This proves (1) of [the determinant calculation](Yin_C_G0901_v4.md#determinant) with the hypothesis \(p\ge3M_p\).
It also proves the [minimum-span and norm divisibility conclusions](Yin_C_G0901_v4.md#rows) there.
Thus (4) of the [short-pair construction](Yin_C_G0901_v4.md#height) applies under this local hypothesis to every reciprocal nontorsion input, with the same constants.

<a id="degree"></a>
## The degree of the powered element

Put \(D=[\mathbb Q(\alpha^p):\mathbb Q]\), \(s=e/D\), and \(c_0=(\log2)/4\).
The relative binomial gives \(s\le p\).
If \(s=p\), the monic minimum \(Q\) of \(\alpha^p\) satisfies \(P(X)=Q(X^p)\) by divisibility and equal degree, and conversely.
In this case \(m(Q)=h\), so the [house bound](Yin_C_G0345_v869.md#degree) gives
\[
                                  h\ge c_0p/e.                           \tag{3}
\]

Otherwise \(s<p\).
Write \(z=\alpha^p,\ K=\mathbb Q(z)\) and \(\nu=N_{\mathbb Q(\alpha)/K}(\alpha)\), so \(\nu^p=z^s\).
Integers \(a,b\) with \(as+bp=1\) give \(\beta=\nu^a z^b\in K\) with \(\beta^p=z\).
Thus \(\beta/\alpha\) is a root of unity and \(\beta\) is a nontorsion algebraic unit of absolute logarithmic height \(h/e\).
Its total log measure is at most \(D h/e\) and at least \(c_0/D\) by the same house bound.
In particular
\[
                                 D\ge\sqrt{c_0 e/h}.                      \tag{4}
\]
This estimate uses neither reciprocity nor degree preservation by other powers.

<a id="pigeonhole"></a>
## An auxiliary vanishing at a finite-field residue

Take a nonzero root of \(\bar P\) of multiplicity \(m\) and residue degree \(f\), so its \(f\) distinct Frobenius conjugates each have multiplicity \(m\) and \(fm\le e\).
For every integer \(K\ge1\) put \(n=\lceil f\log p/\log(K+1)\rceil\).
At the \(p\)-th power of the residue, evaluation of polynomials of degree at most \(n\) with coefficients in \(\{0,\ldots,K\}\) takes at most \(p^f\) values.
Two different lists agree since \((K+1)^{n+1}>p^f\).
Subtracting yields a nonzero integral \(E\) with \(\deg E\le n\), \(\|E\|_1\le K(n+1)\), vanishing after reduction at every conjugate of the chosen powered residue.

For each of the \(fm\) associated characteristic-zero roots \(x_i\), write \(x_i=\omega_i(1+u_i)\) with \(v_p(u_i)\ge1/m\).
Binomial expansion gives \(v_p(x_i^p-\omega_i^p)\ge\min(1,p/m)\) at every prime, even where powering need not preserve individual distances.
The element \(E(\omega_i^p)\) lies in an unramified extension of \(\mathbb Q_p\) and has zero residue, so its valuation is at least one.
As \(E\) is integral, \(v_p(E(x_i^p))\ge\min(1,p/m)\).
When \(n<D\), the nonzero integer \(N_{\mathbb Q(\alpha)/\mathbb Q}E(\alpha^p)\) consequently satisfies
\[
 f\min(m,p)\log p
       \ \le\ \log|N E(\alpha^p)|
       \ \le\ e\log(K(n+1))+p n h .                                    \tag{5}
\]
The norm counts all \(e\) conjugates of \(\alpha\); the upper bound follows by evaluating \(E\) at each powered conjugate at the archimedean places.

To prove (1), take \(m=M_p\) and assume \(m\ge e^{3/4}\), the remaining case already being covered by the first term.
Then \(f\le e^{1/4}\).
The choice \(A=\max(1,\sqrt{(p/e)h\log p})\), \(K=\lceil\exp A\rceil\), gives \(n\le1+f\log p/A\).
For all sufficiently large \(e\), uniformly in \(p\le3e\), this upper bound is smaller than \(D\) by (4).
Divide (5) by \(ef\log p\).
The contribution of \(K(n+1)\) is at most a constant times
\[
               \frac{A+\log\log(3p)}{\log p},
\]
since \(\log(2+f\log p/A)/f\ll\log\log(3p)\).
The degree term contributes at most \((p/e)h(1/A+1/(f\log p))\).
By the choice of \(A\) and \(ph/e\le3\), these terms give (1).
Enlarging the absolute constant covers the bounded degrees as well.

For (2), write \(\sigma=p/e\).
In that range \(\log p\asymp\log e\), \(e^{-1/4}=o(\sigma)\), and the second term of (1) is at most a sufficiently small multiple of \(\sigma\) by choosing \(C\) large.
The last term is \(o(\sigma)\) because \(h\le1\) and \(\sigma\log p\gg\log\log e\).
It follows that \(\min(M_p,p)<p/3\), which implies \(M_p<p/3\).
In any fixed positive linear interval \(ae\le p\le be\), formula (1) also gives \(M_p=o(e)\) uniformly on noncomposition inputs of measure \(h\le1\) (for \(b>3\), the same proof applies with constants depending on \(b\)).

<a id="short"></a>
## Short rows at linear and sublinear primes

More precisely, consider a sequence of reciprocal unit minima with \(h\to0,\ e\to\infty\).
Take any \(0<\theta=\theta_e\le1\) with \(\theta\ge C\log\log(3e)/\log(3e)\) for the absolute constant in (2), and suppose
\[
                               h\log(2/h)=o(\theta).
\]
For every prime \(p\ge e\theta\), equation (3) excludes composition eventually, uniformly in \(p\), since \(h=o(\theta)\).
For \(p\le3e\), (2) therefore supplies the local divided-difference condition.
For larger \(p\) the [unconditional determinant estimate](Yin_C_G0901_v4.md#determinant) applies directly.

Put \(x=\sqrt{h\theta/\log(2/h)}\), \(k=\lceil ex\rceil\), \(B=e+k\), \(r=k+1\).
Eventually \(h\le x=o(1)\) and \(s=\min(r,e)=r\).
Formula (4) of the [short-pair bound](Yin_C_G0901_v4.md#height), now valid at every such \(p\), gives
\[
 \frac{\log H}{p}\ll
       \frac{h}{x}
       +\frac{\log(2e)}{e\theta x}
       +\frac{\log(2e)}{e\theta}
       +\frac{x+1/e}{\theta}\log(4\mathrm e/x),                         \tag{6}
\]
with \(\mathrm e=\exp(1)\).
Indeed \(\log(2+pB)/p\) decreases for \(p\ge e\theta\), so it is bounded there by \(O(\log(2e)/(e\theta))\), and the [common divisor cost](Yin_C_G0901_v2.md#division) is \(k\log(2\mathrm e B/k)\).
We have \(h/x=\sqrt{h\log(2/h)/\theta}=o(1)\).
Since \(x\ge h\), the part \(x\log(4\mathrm e/x)/\theta\) is bounded by a constant times the same quantity.
The house bound gives \(h\ge c_0/e\), hence \(\log(4\mathrm e/x)=O(\log(2e))\) and \(x\gg1/(\sqrt e\log(3e))\) under the lower bound on \(\theta\).
The remaining terms in (6) tend to zero as well.
Thus the score \((B-e)/e+(\log H)/p\) tends uniformly to zero for every prime above the stated cutoff, on these original seeds.
Taking \(\theta=\min(a,1)\) proves the fixed-linear-proportion assertion.
The [individual lower bound](Yin_C_G0345_v408.md#lower) proves the converse direction of the finite degree criterion.
The sublinear sufficient condition depends on the measure of each seed; it gives no arbitrary sublinear schedule independent of the rate at which those measures shrink.

<a id="exception"></a>
## An actual obstruction when the measure is bounded

The composition exception in (2) is necessary.
Take \(Q(Y)=Y^2-3Y+1\), whose larger real root \(\beta=(3+\sqrt5)/2\) is a unit with \(0<\log\beta<1\).
For every sufficiently large odd prime \(p\), \(P(X)=Q(X^p)\) is irreducible by the [prime substitution criterion](Yin_C_G0345_v387.md#substitutions), since \(\beta\) is a \(p\)-th power in \(\mathbb Q(\beta)\) for only finitely many primes by bounded degree and height.
Here \(e=2p,\ h=\log\beta\), and \(P\bmod p=(\bar Q)^p\), with distinct roots of \(\bar Q\) for \(p>5\).
Every root of \(P\) has \(p\)-th power of degree two.
An ordinary coprime graph vanishing at such a root would express the root as \(-U(\alpha^p)/V(\alpha^p)\), with nonzero denominator by coprimality.
This contradicts the degree \(2p\).
These examples have fixed positive measure, and (3) explains their exclusion along a shrinking sequence with \(p/e\) bounded below.

## Assessment history

### Decision original-seed-prime-tail

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:10 |
| status | proved |
| reason | The residue-class estimate and the power-degree alternative give prime tails on the original seed, including a quantified sublinear range. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-seed estimates](#statement) | Largest residue multiplicity, the explicit range of the determinant formula, and every fixed positive linear cutoff on shrinking sequences. |
| argument | [Local calculation](#local) | Inertia-orbit bound and the cluster-size version of the determinant. |
| argument | [Powered degree](#degree) | Exact composition exception and the lower degree bound outside it. |
| argument | [Finite-field auxiliary](#pigeonhole) | Nonvanishing, norm inequalities and optimized coefficient alphabet. |
| argument | [Short rows](#short) | Uniform row width and height on the linear and stated sublinear prime ranges. |
| argument | [Obstruction](#exception) | Irreducible quadratic power substitutions at fixed positive total measure. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1047.md#finding) | The original-seed theorem, its local and global proofs and the actual scope of the example. |

## Current assessment

[Selected decision](#decision-original-seed-prime-tail)
