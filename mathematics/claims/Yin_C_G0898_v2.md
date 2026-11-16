---
author: Yin
---

# Rational relations between two conjugate normalized residues

<a id="statement"></a>
## Rational graphs and rational changes of observable

Use the [strict integral odd-grid chamber](Yin_C_G0898_v1.md#statement) with odd \(p=2n+1\to\infty\), \(1<M(P)\to1\), and any fixed one of the five profiles.
Choose distinct positive integers \(a,b\) and conductors with \(\gcd(ab,p)=1\).
For a nonzero residue class \(k\bmod p\) write \([k]\in\{1,\ldots,n\}\) for its representative up to sign.
Take any limiting law of the ordered pair \((U_{[aj]},U_{[bj]})\), denoted by \((u,v)\), omitting pairs meeting poles.
In particular all distinct fixed dyadic times are allowed at every odd conductor.

View rational maps over \(\mathbb Q\) as maps of the projective line.
Let \(\psi\in\mathbb Q(z)\) be nonconstant and satisfy
\[
               \psi((-\infty,0))\cap K=\varnothing,\qquad
                        K=\psi([0,\infty]).
\]
Here \([0,\infty]\) is the closed projective real arc including infinity.
The identity map and the two-to-one observable \(\psi(z)=z+1/z\) both meet the condition.
For any fixed rational map \(f\) over \(\mathbb Q\), constants included, let \(H(X,Y)\) be an integral polynomial obtained by clearing the projective equation \(\psi(Y)=f(\psi(X))\).
More explicitly, choose coprime integral homogeneous coordinate forms of equal degree for each map, compose the forms for \(f\) with those for \(\psi\), and take the determinant against the two forms for \(\psi(Y)\), dehomogenizing at \((X,1),(Y,1)\).
It is a nonzero polynomial and detects the projective equality even at poles.
Then
\[
                         \mathbb E\log|H(u,v)|\ge0.                     \tag{1}
\]
The assertion also holds in the opposite time direction.
In particular \(v\notin\mathbb Q(u)\) and \(u\notin\mathbb Q(v)\) almost surely, by using \(\psi(z)=z\) and countably many rational maps.
The theorem also excludes relations such as \(v+v^{-1}=f(u+u^{-1})\), which can have two algebraic branches over \(u\).
For conjugate coordinates related by a positive prime power, the [quantitative Frobenius bounds](#prime) hold for every integral polynomial lift of that monomial in the corresponding characteristic.

<a id="orbits"></a>
## Sparse primitive cyclotomic orbits

Write \(c=n-\kappa\) for the last positive index and \(w=(\kappa+1/2)/p\).
By the [terminal-block estimates](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent), \(w\to0\) and \(w=p^{-o(1)}\).
Discard all cyclotomic orders \(d<p^{1/4}\), costing \(O(p^{1/2})=o(n)\) nodes by summing the orders.
All other orders eventually avoid poles and satisfy \(dw\to\infty\) uniformly.
A primitive exponent \(\ell\bmod d\) represents a negative residue exactly when its position \(\ell/d\bmod1\) has distance less than \(w\) from \(1/2\), with the boundary belonging to the positive block.
In particular \((d-1)/2\) is a primitive negative exponent.

For any interval of relative length \(L\) in a period of modulus \(d\), inclusion-exclusion gives \(L\varphi(d)+O(2^{\omega(d)})\) integers coprime to \(d\) in that interval.
Here \(\omega(d)\) counts the distinct prime factors, and the estimate follows by counting multiples of each squarefree divisor with rounding error at most two.
For any \(\epsilon>0\), \(4^{\omega(d)}=O_\epsilon(d^\epsilon)\), by bounding separately the primes less than \(4^{1/\epsilon}\).
Together with \(\varphi(d)\ge d/2^{\omega(d)}\), this bounds the proportion of negative nodes in each retained orbit by \(2w+O(d^{-1/2})=o(1)\), uniformly even when \(d\) is composite.

The quantities \(U_j\) are [rational functions of the trace with rational coefficients](Yin_C_G0893_v1.md#orbit) equivariant on every retained orbit.
Suppose \(H\) vanishes once on a retained orbit.
The \(a\)- and \(b\)-index multiplications commute with the cyclotomic Galois group, so it vanishes throughout the orbit.
Write \(W_\ell=\psi(U_{[(p/d)\ell]})\) for a primitive exponent there.
Multiplication by \(ba^{-1}\bmod d\) permutes the full set of indices and takes \(W_\ell\) to \(f(W_\ell)\).
Every \(W_\ell\) is therefore \(f\)-periodic, and the multiset of their values is one complete \(\mathbb Q\)-Galois orbit with constant multiplicity.
The fraction of that multiset outside \(K\) is the negative fraction, positive but tending uniformly to zero.
Consequently the degree of each \(W_\ell\) tends uniformly to infinity among such orbits if violations persist.
The estimate permits selection of distinct points \(W_\ell\in\psi((-\infty,0))\) of unbounded degree along any infinite sequence of violations.

<a id="dynamics"></a>
## Periodic conjugates of a nonlinear rational map

Assume \(\deg f\ge2\) and suppose such a sequence exists.
The selected projective points have canonical height zero by periodicity.
The [arithmetic equidistribution theorem of Baker and Rumely](../audits/literature/BR06/Yin_U001.md#br06-galois-small-point-equidistribution), applied over \(\mathbb Q\) at its complex place to these distinct points, sends their complete orbit laws weakly to the canonical measure \(\mu_f\) on the Riemann sphere.
The preceding proportions and the open-set inequality give \(\mu_f(\mathbb P^1(\mathbb C)\setminus K)=0\).
Its support \(S\subset K\) is infinite since \(\mu_f\) is nonatomic.
The [balance identity](../audits/literature/BR06/Yin_U001.md#br06-height-and-measure) \(f^*\mu_f=(\deg f)\mu_f\) gives \(f^{-1}(S)=S\).
Indeed the support of the pullback is \(f^{-1}(S)\), by continuity, openness of a nonconstant rational map, and positive local preimage multiplicities.

On \(\mathbb P^1(\mathbb C)\setminus S\) all iterates omit three fixed points of \(S\), so they form a normal family by Montel's theorem.
The connected set \(\psi((-\infty,0))\) lies in one component \(D\) of this open complement.
That component contains at most one real periodic point.
To see this, at any real periodic point \(y\in D\) take a return iterate \(g\) fixing \(y\) and use a real local coordinate there.
Its multiplier is real.
A multiplier of modulus above one contradicts normality, since the derivatives of \(g^k\) at \(y\) grow without bound.
A multiplier of modulus one becomes \(+1\) after squaring the return.
The germ then has expansion \(z+c z^r+O(z^{r+1})\), \(c\ne0,\ r\ge2\), because no positive iterate of a map of degree above one is the identity.
The coefficient of \(z^r\) in its \(k\)-th iterate is \(kc\), again impossible for a normal family fixing the center, by local uniform convergence along a subsequence and Cauchy's derivative formula.
Thus \(y\) is attracting.
If two distinct real periodic points belonged to \(D\), choose a common return iterate fixing both.
A subsequence of its powers converges spherically locally uniformly on \(D\) and tends to the first point near that attracting point.
The identity theorem makes the limit that same constant throughout \(D\), contrary to the fixed value at the second point.
This rules out the distinct selected periodic points outside \(K\), proving that no retained orbit can satisfy the graph equation for sufficiently large conductors in the sequence.

<a id="linear"></a>
## Constant maps and projective transformations

A constant map can have only its own value as a periodic point.
An infinite-order projective transformation can have no cycle of length three or more, since an iterate fixing three points is the identity.
Its periodic points therefore belong to the finite fixed set of its square.
Both cases contradict the unbounded degrees on any hypothetical sequence of violating orbits.

If \(f\) has finite order \(N\ge1\), an equality on a retained orbit implies \(W_{a^N\ell}=W_{b^N\ell}\) for every primitive \(\ell\).
The sign separation of \(\psi\) would therefore give identical signs at all those pairs of indices.
Divide \(a,b\) by their common factor before this argument, which only permutes the primitive indices.
Write \(A=a^N,\ B=b^N\) after reduction.
When one is even and the other odd, the primitive exponent \(\ell=(d-1)/2\) has its even multiple near zero modulo \(d\), and the odd multiple has relative distance at most \(\max(A,B)/(2d)<w\) from \(1/2\).
Their signs are opposite.

If both are odd, interchange their labels as necessary so that \(A>B\).
Fix \(1/A<\gamma_1<\gamma_2<1/B\).
Choose an odd integer \(r\) coprime to \(d\) with \(2d w\gamma_1<r<2d w\gamma_2\).
Such an integer exists uniformly on all retained orders: count residues coprime to \(2d\) in this interval using the inclusion-exclusion estimate above.
The main term has order at least \(dw/2^{\omega(2d)}\), whereas the rounding error is \(O(2^{\omega(2d)})\), and \(d\ge p^{1/4}\), \(w=p^{-o(1)}\).
The primitive exponent \(\ell=(d-r)/2\) then has its \(A\)- and \(B\)-multiples at distances \(Ar/(2d)>w>Br/(2d)\) from \(1/2\) in relative angular coordinates.
These formulas have no wrap for large \(p\) since \(A,B\) are fixed and \(w\to0\).
This contradicts sign equality and finishes the orbit exclusions.

<a id="norm"></a>
## From orbit exclusion to logarithmic inequalities

Use \(s_j=(b_j-x)^2,\ Z_j=s_jU_j\) with both \(s_j,Z_j\) integral at all nodes.
For a fixed \(H\) above, write \(h_1=\deg_X H,\ h_2=\deg_Y H\).
The product over retained nodes of
\[
        s_{[aj]}^{h_1}s_{[bj]}^{h_2}H(U_{[aj]},U_{[bj]})
\]
is a nonzero rational integer for all sufficiently large \(p\), by orbit nonvanishing, integrality and invariance under conjugation.
The two multipliers permute the retained indices.
By the [grid denominator and logarithmic tail estimates](Yin_C_G0898_v1.md#limit), the normalized logarithm of the clearing factors tends to zero and the positive parts of the pair logarithms are uniformly integrable.
The tail estimate applies to these permutations because the upper logarithm of a fixed polynomial is bounded by a constant times \(1+\log^+|U_{[aj]}|+\log^+|U_{[bj]}|\).
Pass to the pair law after truncating the logarithm below, then remove that truncation to obtain (1).
In particular it gives zero mass on \(H=0\).
The marginal law is nonatomic, so both coordinates are transcendental almost surely and rational functions can be evaluated off their poles.
Together with the countable union over rational graphs this gives the stated almost sure assertions.
Algebraic dependence on a correspondence of higher degree in both coordinates is not decided in full by these tests.

<a id="prime"></a>
## Frobenius lower bounds for all polynomial lifts of a prime power

For a prime \(q\), fixed \(r\ge1\), \(L=q^r\), and \(\gcd(p,q)=1\), now let \((u,v)\) be the pair at multipliers \(1,L\).
For every fixed \(F\in\mathbb Z[X]\) with \(F(X)\equiv X^L\bmod q\) as a polynomial, and every \(k\ge0\),
\[
                 \mathbb E\log|v^{q^k}-F(u)^{q^k}|\ge(k+1)\log q.      \tag{2}
\]
Indeed \(b_{[Lj]}\equiv b_j^L\bmod q\) by the cyclotomic trace formula and Frobenius, giving the same congruence for \(Z_{[Lj]},s_{[Lj]}\) against \(Z_j^L,s_j^L\).
Put \(d_F=\deg F\ge L\), and clear \(U_{[Lj]},F(U_j)\) with common denominator \(D_j=s_{[Lj]}s_j^{d_F}\), obtaining algebraic-integer numerators \(V_j,W_j\).
Modulo \(q\) both numerators reduce to \(Z_j^L s_j^{d_F}\).
Whenever \(V-W\) is divisible by \(q^e\) with \(e\ge1\), the binomial expansion shows that \(V^q-W^q\) is divisible by \(q^{e+1}\).
Thus \(V_j^{q^k}-W_j^{q^k}\) is divisible by \(q^{k+1}\).
An equality of the powered real values would give \(U_{[Lj]}=F(U_j)\) or \(U_{[Lj]}=-F(U_j)\).
The proved orbit exclusion applied to both fixed graphs rules these out throughout the retained orbits.
The product of the nonzero numerators divided individually by \(q^{k+1}\) is an algebraic integer fixed by conjugation.
Its absolute value is at least one, and the same clearing-factor and tail argument gives (2).

## Assessment history

### Decision rational-observable-graphs

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:17 |
| status | open |
| reason | Submit the rational graph and observable exclusions, uniform primitive-orbit argument and prime-power inequalities for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two conjugate coordinates](#statement) | Distinct invertible multipliers, all five profiles, both orientations, rational sign-separating observables and the prime-power consequences. |
| argument | [Primitive orbits](#orbits) | Uniform terminal proportions, full Galois orbit of observable values and periodicity. |
| argument | [Nonlinear maps](#dynamics) | Canonical-height equidistribution, a completely invariant support and real periodic points in a normal component. |
| argument | [Projective transformations](#linear) | Both parity cases and a primitive exponent forcing opposite signs. |
| argument | [Integral products](#norm) | Nonvanishing, denominator clearing, uniform upper tails and zero mass on the graph. |
| argument | [Frobenius and powers](#prime) | Lifted congruences, growing divisibility and both possible real signs. |
| dependency | [Canonical equidistribution and balance](../audits/literature/BR06/Yin_U001.md#br06-u001) | Theorems 2.3 and 2.1(B) over the rationals at the archimedean place and periodic canonical height zero. |
| dependency | [Terminal block](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Vanishing angular width with subpower reciprocal width. |
| dependency | [Ordered grid estimates](Yin_C_G0898_v1.md#decision-ordered-frobenius-excursions-reviewed) | Cleared cyclotomic samples, denominator mean and logarithmic uniform integrability. |
| dependency | [Arithmetic marginal law](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | Nonatomic laws and equivariant normalized residues for all five profiles. |


### Decision ordered-rational-graphs-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:31 |
| status | proved |
| reason | Adopt the fixed-multiplier ordered graph exclusions and the quantitative prime-power norm inequalities after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two conjugate coordinates](#statement) | Distinct invertible multipliers, all five profiles, both orientations, rational sign-separating observables and the prime-power consequences. |
| argument | [Primitive orbits](#orbits) | Uniform terminal proportions, full Galois orbit of observable values and periodicity. |
| argument | [Nonlinear maps](#dynamics) | Canonical-height equidistribution, a completely invariant support and real periodic points in a normal component. |
| argument | [Projective transformations](#linear) | Both parity cases and a primitive exponent forcing opposite signs. |
| argument | [Integral products](#norm) | Nonvanishing, denominator clearing, uniform upper tails and zero mass on the graph. |
| argument | [Frobenius and powers](#prime) | Lifted congruences, growing divisibility and both possible real signs. |
| dependency | [Canonical equidistribution and balance](../audits/literature/BR06/Yin_U001.md#br06-u001) | Theorems 2.3 and 2.1(B) over the rationals at the archimedean place and periodic canonical height zero. |
| dependency | [Terminal block](../ledger/Yin_L_G0464_v5.md#endpoint-index-exponent) | Vanishing angular width with subpower reciprocal width. |
| dependency | [Ordered grid estimates](Yin_C_G0898_v1.md#decision-ordered-frobenius-excursions-reviewed) | Cleared cyclotomic samples, denominator mean and logarithmic uniform integrability. |
| dependency | [Arithmetic marginal law](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | Nonatomic laws and equivariant normalized residues for all five profiles. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v76.md#ordered-tail-boundary-review) | All five profiles, both orders, nonlinear and projective dynamics and every stated Frobenius lift. |

## Current assessment
[Selected decision](#decision-ordered-rational-graphs-reviewed)
