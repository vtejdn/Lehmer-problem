---
author: Yin
---

# Weighted collisions, exact carry certificates and radical rate controls

This retains the complete original 2026-10-06 mathematical argument in [L5](../ledger/Yin_L_G0005_v1.md).
The original exact finite program and all actually retained execution evidence now have their native home in [J115](../computations/programs/Yin_J_G0115/readme.md); no program is run here.

## Statement

For every nonzero algebraic lambda let X_n=sum_(j=0)^(n-1) B_j lambda^j with independent fair binary digits, and define D_n=|supp X_n|, q_n=P(X_n=X'_n), a_n=-log_2 q_n and H_n the Shannon entropy in bits.
Use D_0=q_0=1 and H_0=0.

A. The limits h_2=lim a_n/n, h_Sh,2=lim H_n/n and rho_2=lim log_2 D_n/n exist, and 0<=h_2<=h_Sh,2<=rho_2.
One has q_(n+m)>=q_n q_m, q_(n+m)<=min(q_n,q_m) and h_2=inf_(n>=1) a_n/n, so a finite a_N/N is an upper bound for h_2.
For every fixed noncyclotomic algebraic unit lambda, an expanding conjugate beta and any positive integer k with |beta|^k>2 give q_n<=2^(-floor(n/k)) and h_2>=1/k; this bound depends on lambda.
If integers N>=1 and a real K>=1 satisfy q_((j+1)N)<=K q_(jN)q_N for every j>=1, then h_2>=(a_N-log_2 K)/N.

B. For every algebraic unit lambda, the inverse-carry recurrence c_0=0, c_(j+1)=lambda^(-1)(c_j+delta_j), with delta probabilities 1/4,1/2,1/4 on -1,0,1, represents q_n as the return probability to zero.
The two-endpoint embedding bounds in the Argument apply to returning paths only.
If no conjugate has modulus one, the rigorously exhausted returning-state region is finite and yields a nonnegative substochastic matrix P with q_n=(P^n)_(0,0).
Any positive rational vector v with v(0)=1 and P^N v<=theta v, where N>=1 is an integer and 0<theta<1, gives h_2>=-log_2(theta)/N and m(lambda)>=-log(theta)/N at the accepted support/Mahler interface.
If the unit-circle conjugates have total real dimension s, the stated O_lambda((1+n)^s) lattice-state bound alone gives no positive return-probability rate.

C. At phi=(1+sqrt(5))/2 the complete possible returning region is {0,+/-(phi-1),+/-1}, with the exact transition matrix retained in the Argument.
The rational positive vector has theta=5/8, hence q_n(phi)<=(5/8)^n for every n>=0 and h_2(phi)>=log_2(8/5).
No optimum or novelty is claimed.

D. Let r>=1 be an integer and let lambda and beta be nonzero algebraic numbers with lambda^r=beta and [Q(lambda):Q(beta)]=r.
For n=qr+s, 0<=s<r, the exact support, collision and Shannon product formulas in the Argument hold, and for each fixed r all three limiting rates at lambda equal those at beta, without a factor 1/r.
For every integer k>=0, r=2^k and lambda_k=phi^(1/r), the polynomial t^(2r)-t^r-1 is irreducible, the required relative degree is r, all conjugate moduli tend to one as k grows and h_2(lambda_k)>=log_2(8/5).
Their Mahler measure is the fixed value phi, and these polynomials are nonreciprocal.
No interchange of varying-r and length limits, uniform reverse Shannon/collision comparison or arbitrary reciprocal-unit gap follows.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:41 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All A–D with every parameter, length, relative-degree, all-j/block hypothesis, bit/natural-log convention and the exact finite versus uniform exclusions. |
| argument | [Argument](#argument) | Complete weighted entropy proof, parameter-dependent atom bound, both-endpoint carry region, finite-state certificate, exhaustive golden matrix/vector and full radical irreducibility/product argument. |
| dependency | [BV20 digit-entropy interface](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Existing sign/binary entropy and algebraic-unit support/Mahler upper bound; source-theorem proof depths are unchanged. |
| dependency | [BV20 finite/asymptotic boundary](../audits/literature/BV20/Yin_U003.md#bv20-u003) | Fixed-word growth versus all-length rate and unit reduction only; no new linear-group or external structural proof audit. |
| dependency | [Smy08 restricted-family interface](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Existing nonreciprocal-family comparison and Kronecker convention only, with the recorded statement-level external theorem depth. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:43 |
| status | proved |
| reason | Adopt the actual complete A–D statement and retained argument with resolved fixed interfaces and sufficient current contributor self-review; original findings and finite executions retain their actual historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A–D with all lengths, exact algebraic and relative-degree domains, all-j/block assumptions, log units and finite/uniform exclusions. |
| argument | [Argument](#argument) | Complete weighted-collision, returning-region, golden matrix/vector and radical-product/norm-degree proofs, including the explicit Shannon/support and block-limit interfaces. |
| dependency | [BV20 digit-entropy interface](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Existing sign/binary entropy and algebraic-unit support/Mahler upper bound; source-theorem proof depths are unchanged. |
| dependency | [BV20 finite/asymptotic boundary](../audits/literature/BV20/Yin_U003.md#bv20-u003) | Fixed-word growth versus all-length rate and unit reduction only; no new linear-group or external structural proof audit. |
| dependency | [Smy08 restricted-family interface](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Existing nonreciprocal-family comparison and Kronecker convention only, with the recorded statement-level external theorem depth. |
| review | [Current complete carry finding](../audits/reviews/Yin_R_G0504_v1.md#current-complete-carry-finding) | Actual entire registered Statement and Argument, accepted source interfaces and native-retention limits; current self-review, without independent or fresh execution certification. |


### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:18 |
| status | proved |
| reason | Adopt the separately arranged isolated whole inspection of this exact fixed Statement and complete Argument in R800, with all necessary mathematical interfaces and decisive finite controls checked at their actual scopes. Preserve the fixed mathematics, original source depth, existing self-review and historical unknown/negative findings at their true inputs and dates; no broader gap or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A–D with all lengths, exact algebraic and relative-degree domains, all-j/block assumptions, log units and finite/uniform exclusions. |
| argument | [Exact retained argument](#argument) | Complete weighted-collision, returning-region, golden matrix/vector and radical-product/norm-degree proofs, including the explicit Shannon/support and block-limit interfaces. |
| dependency | [Exact retained dependency](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Existing sign/binary entropy and algebraic-unit support/Mahler upper bound; source-theorem proof depths are unchanged. |
| dependency | [Exact retained dependency](../audits/literature/BV20/Yin_U003.md#bv20-u003) | Fixed-word growth versus all-length rate and unit reduction only; no new linear-group or external structural proof audit. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Existing nonreciprocal-family comparison and Kronecker convention only, with the recorded statement-level external theorem depth. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0504_v1.md#current-complete-carry-finding) | Actual entire registered Statement and Argument, accepted source interfaces and native-retention limits; current self-review, without independent or fresh execution certification. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0800_v1.md#fresh-c212-whole) | Entire exact fixed Statement and complete Argument, necessary interfaces, every stated boundary and actual finite/source limits; independently reviewed in the isolated M04 arrangement. |

## Argument

<a id="collision-entropy-directions"></a>
### 1. The weighted collision observable and its directions

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

### 2. An asymptotic candidate that tolerates collisions

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
### 3. Exact carry states and their boundedness

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
### 4. A complete rational certificate at the golden ratio

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
### 5. Degree inflation that preserves all three rates

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

### Existence of the other two limits

For a fixed lambda, concatenation gives D_(n+m)<=D_n D_m.
The law of X_(n+m) is the image of the independent pair (X_n,lambda^n X'_m) under addition, so H_(n+m)<=H_n+H_m.
Fekete's lemma gives their limits; applying the finite entropy inequalities and the collision subadditivity already proved above gives A in the stated bit convention.
For the block certificate in B, apply positivity to P^(jN)v<=theta^j v and pass to the existing collision-rate limit along the multiples of N.
The all-j bound in A is used at every multiple jN and likewise passes to that limit; finitely many tests do not suffice.
