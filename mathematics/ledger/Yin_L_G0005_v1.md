---
author: Yin
---

# G0001: weighted collisions and carry certificates

Date: 2026-10-06.
Status: preserved original exploration, comparison and uniformity boundary.
The complete precise result is now adopted in [C212](../claims/Yin_C_G0212_v1.md#statement), the native computation belongs to [J115](../computations/programs/Yin_J_G0115/readme.md), and the actual formal findings belong to [R504](../audits/reviews/Yin_R_G0504_v1.md).
This is the secondary collision component of the G0001 exploration.

The concrete increment is an exact carry certificate at the golden ratio, together with a family of arbitrarily large degrees on which the collision, Shannon, and support growth rates are unchanged.
This supplies a test for methods that deteriorate solely because individual conjugate moduli approach 1.
It does not give a uniform gap on the reciprocal unit family.

## Scope, sources, and reuse

The governing mathematical target is [T G0001](../tasks/Yin_T_G0001_v1.md); the existing growth route and ledger are [S G0002](../strategies/Yin_S_G0002.md) and [L G0001](Yin_L_G0001_v1.md).
The source interfaces used here are the distinction between entropy and support growth, and the unit reduction, in [BV20 U001](../audits/literature/BV20/Yin_U001.md), together with the finite versus asymptotic distinction in [BV20 U003](../audits/literature/BV20/Yin_U003.md).

The formulas below are elementary deductions written out in this draft.
No new literature theorem is adopted.
A bounded primary-source search did not establish a uniform comparison of Shannon and order-2 Rényi entropy rates within this geometric-digit family.
No claim is made that such a comparison is unknown in the literature.
In particular, no result about normalized correlation dimension is used as a uniform lower bound for an unnormalized entropy rate.

The structural reuse requirement of Shared structure across families; current organization is met by using the same exact digit relation across the probabilistic, polynomial, and carry descriptions.
The uniformity boundary emphasized by Uniform descent and finite closure; current organization is kept explicit: a certificate for each fixed parameter does not supply constants independent of the parameter.

<a id="collision-entropy-directions"></a>
## 1. The weighted collision observable and its directions

Let $\lambda\ne0$ be algebraic, let $B_j$ be independent fair $\{0,1\}$ digits, and set

$$
X_n=\sum_{j=0}^{n-1}B_j\lambda^j,\qquad
r_n(x)=\#\{b\in\{0,1\}^n:\textstyle\sum b_j\lambda^j=x\}.
$$

Replacing the digits by fair signs gives $2X_n-\sum_{j<n}\lambda^j$, an injective affine change of the finite support.
Thus support size, Shannon entropy, and all collision multiplicities agree with the sign convention.

For an independent copy $X'_n$ define

$$
q_n=\mathbb P(X_n=X'_n)=4^{-n}\sum_xr_n(x)^2,\qquad
a_n=-\log_2q_n.
$$

This is a weighted count of ternary zero polynomials: for $\delta_j=B_j-B'_j$, the probabilities of $-1,0,1$ are $1/4,1/2,1/4$.
The integer numerator weights every zero coefficient by 2 and every nonzero coefficient by 1.
Counting distinct ternary relations without these weights computes a different quantity.

Concatenating two independent collisions gives

$$
q_{n+m}\ge q_nq_m.
$$

Consequently $a_n$ is subadditive and

$$
h_2(\lambda):=\lim_{n\to\infty}\frac{a_n}{n}
=\inf_{n\ge1}\frac{a_n}{n}.
$$

Write $h_{\rm Sh,2}$ for the Shannon rate in bits and $\rho_2$ for the logarithmic support growth rate in bits.
The finite entropy inequalities give

$$
0\le h_2\le h_{\rm Sh,2}\le\rho_2.
$$

**A finite value $a_N/N$ is an upper bound for $h_2$, not a lower bound.** By contrast an estimate $q_n\le C\exp(-cn)$ for every $n$ implies $h_2\ge c/\log2$.
Convolution also gives $q_{n+m}\le\min(q_n,q_m)$, by contraction of the $\ell^2$ norm under averaging translations, but this alone gives no positive rate.

A generic distribution shows why a reverse Shannon comparison needs additional structure.
Give one atom mass $1/2$ and distribute the other $1/2$ equally among $2^n$ other atoms.
Its Shannon entropy is $1+n/2$ bits, whereas its collision probability is $(1+2^{-n})/4$ and its order-2 entropy rate is zero.
This is **not** asserted to be a geometric-digit law.
No counterexample inside the present algebraic family, and no uniform reverse comparison inside that family, is used here.

For completeness, each fixed noncyclotomic algebraic unit already has $h_2>0$ by a direct parameter-dependent argument.
Choose a conjugate $\beta$ with $|\beta|>1$, and an integer $k$ with $|\beta|^k>2$.
A nonzero finite sum with coefficients in $\{-1,0,1\}$ and exponents divisible by $k$ cannot vanish: its largest term strictly exceeds the sum of the preceding absolute values.
Condition on all digits outside one residue class modulo $k$.
The remaining $\lfloor n/k\rfloor$ digits have distinct values, so every atom has mass at most $2^{-\lfloor n/k\rfloor}$.
Therefore $q_n\le2^{-\lfloor n/k\rfloor}$ and $h_2\ge1/k$.
Existence of the expanding conjugate here uses the usual Kronecker interface for a noncyclotomic unit.
The dependence of $k$ on $\lambda$ is precisely the unresolved uniformity.

## 2. An asymptotic candidate that tolerates collisions

One possible replacement for a short free pair is a weighted return bound proved for all lengths.
For example, if fixed $N\ge1$ and $K\ge1$ satisfy

$$
q_{(j+1)N}\le Kq_{jN}q_N\quad\text{for every }j\ge1,
$$

then $q_{jN}\le K^{j-1}q_N^j$, and hence

$$
h_2\ge \frac{a_N-\log_2K}{N}.
$$

A positive bound therefore follows if $a_N>\log_2K$.
The hypothesis is an all-$j$ estimate; testing finitely many values of $j$ does not establish it.
Uniform constants with $(a_N-\log_2K)/N$ bounded below independently of the parameter would be a sufficient gap mechanism.
It permits many collisions and asks instead that their weighted concentration not persist too strongly under repeated concatenation.

<a id="carry-state-bound"></a>
## 3. Exact carry states and their boundedness

Suppose $\lambda$ is an algebraic unit.
Define

$$
c_0=0,\qquad c_{j+1}=\lambda^{-1}(c_j+\delta_j).
$$

Then $c_j\in\mathbb Z[\lambda]$, and $c_n=0$ exactly when $\sum_{i<n}\delta_i\lambda^i=0$.
For a returning path and an embedding $\sigma$ with $\sigma(\lambda)=\beta$,

$$
\sigma(c_j)=\sum_{i<j}\delta_i\beta^{i-j}
=-\sum_{i=j}^{n-1}\delta_i\beta^{i-j}.
$$

Using the first sum at expanding places and the second at contracting places gives

$$
\begin{array}{ll}
|\sigma(c_j)|<1/(|\beta|-1),&|\beta|>1,\\
|\sigma(c_j)|<1/(1-|\beta|),&|\beta|<1,\\
|\sigma(c_j)|\le\min(j,n-j),&|\beta|=1.
\end{array}
$$

These are bounds for paths that return at time $n$, not bounds for every forward trajectory.

If no conjugate lies on the unit circle, the Minkowski embedding of the order $\mathbb Z[\lambda]$ is a full lattice, and the displayed bounded region contains finitely many possible returning states.
Give each allowed transition its digit probability, discard outgoing transitions leaving the region, and, if desired, trim states that cannot lie on a path from 0 back to 0.
The resulting nonnegative substochastic matrix $P$ satisfies

$$
q_n=(P^n)_{00}.
$$

In particular, a positive rational vector $v$ with $v(0)=1$ and

$$
Pv\le\theta v,\qquad \theta<1,
$$

is a finite, exact, all-length certificate:

$$
q_n\le(P^nv)(0)\le\theta^n,\qquad h_2\ge-\log_2\theta.
$$

The block variant $P^Nv\le\theta v$ gives $h_2\ge-\log_2\theta/N$.
Positivity and rational inequalities can be checked exactly after the state region has been rigorously exhausted.
This certificate controls weighted leakage, rather than requiring all words to remain distinct.

The standard support/Mahler upper bound, $\rho_2\le m(\lambda)/\log2$, would then imply $m(\lambda)\ge-\log\theta/N$.
This conversion keeps the natural logarithm in $m$ and the bit convention in the entropy rates.

Unit-circle conjugates are a genuine boundary of this finite-state construction.
If their total real dimension is $s$, the displayed bounds allow at most $C_\lambda(1+n)^s$ lattice states, with parameter-dependent $C_\lambda$, by elementary lattice packing.
Such a count is not a return-probability estimate.
Cyclotomic examples already have polynomial state counts and zero entropy rate.
Neither a polynomial central width nor the existence of finite truncations by itself proves a gap.

<a id="golden-ratio-certificate"></a>
## 4. A complete rational certificate at the golden ratio

Put $\varphi=(1+\sqrt5)/2$, $\psi=1-\varphi=-1/\varphi$, and $u=\varphi-1$.
The returning-state inequalities for $x=a+b\varphi$, $x'=a+b\psi$, are

$$
|x|<\varphi,\qquad |x'|<\varphi^2.
$$

They imply $|b|<(\varphi+\varphi^2)/\sqrt5<2$.
For $b=0$, the possibilities are $a=-1,0,1$.
For $b=1$, intersecting the two strict inequalities forces $a=-1$; the case $b=-1$ is its negative.
Thus the whole possible returning region is exactly

$$
\{0,u,-u,1,-1\}.
$$

The returning transitions are $0\to0$ with probability $1/2$, $0\to\pm u$ with probability $1/4$ each, $\pm u\to\pm1$ with probability $1/4$, and $\pm1\to0,\pm u$ with probabilities $1/4,1/2$.
All omitted transitions leave the exhaustively bounded region and cannot participate in any return.

On symmetric functions, ordered by the classes $0,\{\pm u\},\{\pm1\}$, the matrix and an exact certificate are

$$
P_{\rm sym}=
\begin{pmatrix}
1/2&1/2&0\\
0&0&1/4\\
1/4&1/2&0
\end{pmatrix},
\qquad
v=\begin{pmatrix}1\\1/4\\3/5\end{pmatrix},
\qquad
\theta=5/8.
$$

Indeed $P_{\rm sym}v=(5/8,3/20,3/8)^T\le(5/8)v$, since $3/20\le5/32$.
Therefore

$$
q_n(\varphi)\le(5/8)^n,\qquad
h_2(\varphi)\ge\log_2(8/5)>0.
$$

This is an exact elementary control certificate, without a claim of novelty or optimality.
In particular its validity does not rest on extrapolating the finite table below.

<a id="radical-collision-control"></a>
## 5. Degree inflation that preserves all three rates

Suppose $\lambda^r=\beta$ and $[\mathbb Q(\lambda):\mathbb Q(\beta)]=r$.
The latter hypothesis is essential: it makes $1,\lambda,\ldots,\lambda^{r-1}$ linearly independent over $\mathbb Q(\beta)$.
Grouping the independent digits by their exponent modulo $r$ now gives an injective product decomposition.

For $n=qr+s$, $0\le s<r$, write $D_n(\alpha)=|\operatorname{supp}X_n(\alpha)|$ and $H_n(\alpha)$ for Shannon entropy in bits.
Then exactly

$$
\begin{aligned}
D_n(\lambda)&=D_{q+1}(\beta)^sD_q(\beta)^{r-s},\\
q_n(\lambda)&=q_{q+1}(\beta)^s q_q(\beta)^{r-s},\\
H_n(\lambda)&=sH_{q+1}(\beta)+(r-s)H_q(\beta).
\end{aligned}
$$

For every fixed $r$, taking $n\to\infty$ proves

$$
h_2(\lambda)=h_2(\beta),\qquad
h_{\rm Sh,2}(\lambda)=h_{\rm Sh,2}(\beta),\qquad
\rho_2(\lambda)=\rho_2(\beta).
$$

There is no factor $1/r$: the $r$ independent residue classes supply precisely the compensating factor.
These identities do not justify interchanging a varying-$r$ limit with $n\to\infty$.

An explicit infinite control family is

$$
r=2^k,\qquad \lambda_k=\varphi^{1/r},\qquad
p_k(t)=t^{2r}-t^r-1.
$$

Here $p_k$ is irreducible over $\mathbb Q$.
To check this without assuming the needed degree: start from the irreducible polynomial $t^2-t-1$.
At any stage the minimal polynomial is monic of even degree and constant coefficient $-1$, so the field norm of its chosen root is $-1$.
That root cannot be a square in its own field, because the rational norm of a square is a square in $\mathbb Q$.
Adjoining its square root therefore doubles the degree.
Induction gives degree $2r$, and then the tower law gives relative degree $r$ over $\mathbb Q(\varphi)$.

Every conjugate of $\lambda_k$ has modulus either $\varphi^{1/r}$ or $\varphi^{-1/r}$, tending to 1 as $k\to\infty$, while all three entropy/growth rates stay equal to those at $\varphi$.
In particular

$$
h_2(\lambda_k)\ge\log_2(8/5).
$$

This family refutes the diagnostic premise that conjugate moduli approaching 1 must force a small collision rate.
It does not establish a gap on arbitrary small-Mahler units: its Mahler measure stays equal to $\varphi$.
Its irreducible polynomials are nonreciprocal, since reversing $t^{2r}-t^r-1$ gives $1-t^r-t^{2r}$, which equals neither it nor its negative.
Thus the family lies in the class already covered by the nonreciprocal gap, as recorded in [Smy08 U002](../audits/literature/Smy08/Yin_U002.md).
It is a degree/conjugate-modulus control, not progress on the unresolved reciprocal core.

## 6. Original finite controls and native home

The [complete original program and execution record](../computations/programs/Yin_J_G0115/readme.md) retain the exact n=0–20 golden return checks, r=1,2,4,8 and n=0–16 radical-product checks, full actually retained matrix/table and cyclotomic/nonunit controls.
The author run with CPython 3.13.15 and later coordinating reproduction with CPython 3.14.7 both occurred on 2026-10-06; this maintenance performs no run.
The last-column finite entropy values remain upper bounds for the limiting h_2, and differing fixed-length radical values do not contradict equality of the asymptotic rates.
No raw complete JSON stdout was retained in this original account; the native home preserves the exact available evidence without fabricating it.

## 7. Activation gate and unresolved scope

The useful next gate is an exact weighted return certificate whose loss can be bounded independently of the parameter, or an all-length concatenation inequality with a uniform positive deficit.
The central directions at unit-circle conjugates must be handled within that proof, rather than declared harmless because their width is polynomial.

The golden-ratio certificate and its radical lifts are controls for validating such a mechanism.
Finite collision tables, finite spectral truncations, positive entropy for every fixed parameter, and a generic Shannon/Rényi comparison do not pass this gate.
This record does not claim any of them yields the Lehmer gap.
The fixed record supports the secondary strategy's next gate; source adoption remains separate.

The [original author check](../audits/reviews/Yin_R_G0504_v1.md#original-author-carry-check) and [original parent finding](../audits/reviews/Yin_R_G0800_v1.md#original-parent-carry-finding) retain their actual 2026-10-06 scopes and different declared relationships.
The [current complete self-check](../audits/reviews/Yin_R_G0504_v1.md#current-complete-carry-finding) supports the actual new C212 adoption without claiming independent historical isolation.

The complete original additional-reproduction account is retained with [J115 observations](../computations/programs/Yin_J_G0115/observed-results.md), without a new execution.
