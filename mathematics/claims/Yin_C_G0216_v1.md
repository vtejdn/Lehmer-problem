---
author: Yin
---

# A full-place continuous carry dual measure with neutral-boundary control

The complete proof below is retained from the original 2026-10-06 [L11](../ledger/Yin_L_G0011_v1.md); it is an explicit continuous-relaxation functional and boundary analysis, with its original arithmetic limitations.
No research execution, new source inspection or numerical program is introduced.

## Statement

Let lambda be any algebraic unit in characteristic zero and take every real embedding and one from each complex-conjugate pair, with real dimensions d_sigma=1 or 2, respectively.
Put beta_sigma=sigma(lambda), U={|beta_sigma|<1}, S={|beta_sigma|>1}, C={|beta_sigma|=1}, A_sigma=beta_sigma^(-1), and M=product_(|beta_sigma|>1)|beta_sigma|^(d_sigma).
Use the exact products J_U,J_S, full Euclidean E_C, weights (1/4,1/2,1/4), shared-digit branches and killed operator P defined in the Argument; f is evaluated only on surviving points, equivalently after zero extension outside D.
For every nonnegative Borel f on D=J_U times J_S times E_C and every positive integer N, the jointly stationary contracting-coordinate law nu_S and measure mu=dx_U dnu_S dx_C satisfy

    integral_D P^N f dmu = M^(-N) integral_D f dmu,

with extended integrals allowed.
The full real determinant of A is one; its U determinant is M.
For each fixed N, b=norm(v_C), R>Nb and I_R=integral_(J_U times J_S times B_R) f dmu, the exact sandwich is

    M^(-N) I_(R-Nb) <= integral_(J_U times J_S times B_R) P^N f dmu <= M^(-N) I_(R+Nb).

If theta>=0 and P^N f<=theta f mu-almost everywhere with 0<integral_D f dmu<infinity, then theta>=M^(-N).
The same conclusion holds for a pointwise inequality when 0<I_R<infinity for all sufficiently large R and limsup_(R to infinity) log^+(I_R)/R=0, including bounded strictly positive weights and the stated polynomial upper-growth class.
Thus -log(theta)/N<=log M whenever theta>0 in these classes.
The argument holds for any finite list of nonzero real/complex parameters of product |beta_sigma|^(d_sigma)=1, even without arithmetic realization.
It does not transfer reachable-lattice inequalities to positive mu-mass, certify a killed neutral-box extension, treat arbitrary unbounded weights or nonunits, or rule out arithmetic restrictions on actual spectra.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:42 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All real/complex places of every algebraic unit, and each stated finite nonarithmetic norm-one list; every nonnegative Borel f and every positive integer N, with the exact finite-mass or subexponential-neutral-mass conditions. |
| argument | [Argument](#argument) | Complete shared-digit stationary construction, full/partial real Jacobians, killed U domain, Tonelli/change-of-variable identity, all-word inverse coverage, neutral-ball sandwich, growth iteration and arithmetic/nonunit limits. |
| dependency | [Complete carry-state bounds](Yin_C_G0212_v1.md#carry-state-bound) | Actual arithmetic returning-path embedding only; not used to restrict the continuous identity. |
| dependency | [One-place and truncation comparison](Yin_C_G0213_v2.md#7-a-rigorous-limitation-of-the-continuous-one-place-relaxation) | Existing one-place baseline and finite-box boundary comparison only; the full-place construction is proved here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:46 |
| status | proved |
| reason | Adopt the complete continuous functional and neutral-boundary theorem after actual current whole self-review; the arithmetic-reachability and nonunit limitations remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All real/complex places of every algebraic unit, and each stated finite nonarithmetic norm-one list; every nonnegative Borel f and every positive integer N, with the exact finite-mass or subexponential-neutral-mass conditions. |
| argument | [Argument](#argument) | Complete shared-digit stationary construction, full/partial real Jacobians, killed U domain, Tonelli/change-of-variable identity, all-word inverse coverage, neutral-ball sandwich, growth iteration and arithmetic/nonunit limits. |
| dependency | [Complete carry-state bounds](Yin_C_G0212_v1.md#carry-state-bound) | Actual arithmetic returning-path embedding only; not used to restrict the continuous identity. |
| dependency | [One-place and truncation comparison](Yin_C_G0213_v2.md#7-a-rigorous-limitation-of-the-continuous-one-place-relaxation) | Existing one-place baseline and finite-box boundary comparison only; the full-place construction is proved here. |
| review | [Complete current full-place finding](../audits/reviews/Yin_R_G0508_v1.md#current-full-place-finding) | Actual whole statement/argument check with the exact mass, domain and neutral-boundary assumptions; contributor self-review, not new isolated coverage. |

## Complete retained argument

<a id="argument"></a>

<a id="full-place-dual-functional"></a>
## 1. Coordinates, domain and real Jacobians

Let $\lambda$ be any algebraic unit in characteristic zero.
Choose every real embedding and one embedding from each complex-conjugate pair.
Write $\beta_\sigma=\sigma(\lambda)$ and let $d_\sigma=1$ for a real place and $d_\sigma=2$ for a complex place.
Complex coordinates carry ordinary two-dimensional Lebesgue measure.

On the full real Minkowski space, split coordinates into

$$
U=\{|\beta_\sigma|<1\},\qquad
S=\{|\beta_\sigma|>1\},\qquad
C=\{|\beta_\sigma|=1\}.
$$

The letters refer to the carry map, whose linear part is

$$
A_\sigma z=\beta_\sigma^{-1}z.
$$

Thus $U$ expands, $S$ contracts, and $C$ is orthogonal as a real map.
Let $v$ have coordinate 1 at each place.
The digit branches are $F_\delta x=A(x+\delta v)$, with weights $w_{-1}=w_1=1/4$, $w_0=1/2$.

The unit norm identity and multiplicative Mahler measure give

$$
\prod_\sigma|\beta_\sigma|^{d_\sigma}=1,\qquad
M=M(\lambda)=\prod_{|\beta_\sigma|>1}|\beta_\sigma|^{d_\sigma},
$$

and therefore

$$
|\det_{\mathbb R}A|=1,\qquad
|\det_{\mathbb R}A_U|
=\prod_{|\beta_\sigma|<1}|\beta_\sigma|^{-d_\sigma}=M.
\tag{1}
$$

Multiplication by a complex number $a+ib$ has real determinant $a^2+b^2$, which explains the exponent 2 at complex places.
It would be incorrect to assign the full Minkowski map determinant $M$.

For each $U$ place take the closed interval, or complex disc, of radius

$$
R_\sigma^U=\frac1{1-|\beta_\sigma|}.
$$

Their product is $J_U$.
For all three digits,

$$
(F_\delta^U)^{-1}(J_U)\subseteq J_U,
\tag{2}
$$

because $|\beta_\sigma z-\delta|\le|\beta_\sigma|R_\sigma^U+1=R_\sigma^U$.
Equivalently $F_\delta^U(J_U)$ contains $J_U$.

At each $S$ place use radius $R_\sigma^S=1/(|\beta_\sigma|-1)$ and denote the product by $J_S$.
Here the forward inclusion holds:

$$
F_\delta^S(J_S)\subseteq J_S.
\tag{3}
$$

Use the full Euclidean space $E_C$ at the neutral places.
The enlarged continuous domain is

$$
D=J_U\times J_S\times E_C.
$$

Every returning arithmetic carry path stays in $D$, by [C212](Yin_C_G0212_v1.md#carry-state-bound).
This does not mean every continuous point or path in $D$ is arithmetically realizable.
Define the killed operator on nonnegative Borel functions by

$$
Pf(x)=\sum_\delta w_\delta\,
\mathbf 1_{J_U}(F_\delta^U x_U)\,f(F_\delta x).
\tag{4}
$$

Only the $U$ boundary causes killing.
Empty coordinate products have their usual one-point, unit-measure convention.

## 2. Contracting coordinates and the shared digit

Let $\delta_1,\delta_2,\ldots$ be independent digits with the given weights.
The vector series

$$
Z_S=\sum_{j\ge1}A_S^j\delta_j v_S
\tag{5}
$$

converges absolutely and lies in $J_S$.
Let $\nu_S$ be its probability law.
Splitting off an independent first digit proves directly

$$
\sum_\delta w_\delta(F_\delta^S)_*\nu_S=\nu_S.
\tag{6}
$$

This is a joint law on all contracting coordinates; their digits are shared, not chosen independently place by place.
The measure may be singular.
No density or full-support assertion is required.

Put

$$
d\mu=dx_U\,d\nu_S(x_S)\,dx_C
\quad\text{on }D.
$$

For each fixed digit, changing variables $y_U=F_\delta^U x_U$ in the surviving domain gives the factor $M^{-1}$ and the same integration domain $J_U$, by (1)--(2).
Changing $y_C=F_\delta^C x_C$ preserves Lebesgue measure on the whole neutral space.
Thus the two changed integration domains are independent of that digit.
Only then do we sum the remaining pushforwards $(F_\delta^S)_*\nu_S$ and use (6).
For every nonnegative Borel $f$, with extended integrals permitted,

$$
\int_D Pf\,d\mu=M^{-1}\int_D f\,d\mu.
\tag{7}
$$

In particular,

$$
\int_D P^Nf\,d\mu=M^{-N}\int_D f\,d\mu.
\tag{8}
$$

This order of operations is why the shared digit causes no missing independence assumption.
The measure is not full-dimensional Lebesgue measure: it uses Lebesgue measure on $U$ and $C$ and the joint stationary probability on $S$.

If $0<\int_D f\,d\mu<\infty$ and $P^Nf\le\theta f$ throughout $D$ (or $\mu$-almost everywhere), then

$$
\theta\ge M^{-N}.
\tag{9}
$$

When $C$ is empty, every bounded strictly positive finite-valued weight on $D$ meets this finite-integral condition.

<a id="neutral-boundary-sandwich"></a>
## 3. Neutral truncation and subexponential central mass

For nonempty $C$, use a Euclidean ball $B_R\subset E_C$.
This choice is rotation invariant; an arbitrary coordinate rectangle need not have that property under complex rotations.
Set $b=\|v_C\|$ and

$$
I_R=\int_{J_U\times J_S\times B_R}f\,d\mu.
$$

For a length-$N$ digit word, the central branch has the form

$$
x_C\longmapsto A_C^Nx_C+\xi,\qquad \|\xi\|\le Nb.
$$

Consequently its image of $B_R$ contains $B_{R-Nb}$ and lies in $B_{R+Nb}$ whenever $R>Nb$.
In the $U$ change of variables, every endpoint in $J_U$ has a complete inverse branch staying in $J_U$, by iterating (2).
Hence the length-$N$ survival restriction introduces no additional loss in this integration.

For each word apply these same central-ball inclusions; after that, average its $S$ pushforward.
The averaged $S$ measure is $\nu_S$ by the $N$-step version of (6).
This proves

$$
M^{-N}I_{R-Nb}
\le
\int_{J_U\times J_S\times B_R}P^Nf\,d\mu
\le
M^{-N}I_{R+Nb}.
\tag{10}
$$

There is a boundary term; it has not been dropped.
The two outer expressions give an exact sandwich for it.
For a uniformly bounded weight the absolute difference from $M^{-N}I_R$ is bounded by a constant times the volume of the shell $B_{R+Nb}\setminus B_{R-Nb}$, which is $O(R^{\dim E_C-1})$ for fixed $N$.

Here $P$ is still the global operator (4); only its integral is truncated.
Killing the process at a fixed central-box boundary changes the operator, so (7) is no longer its exact identity.
A strict gap of that finite-box operator can include artificial boundary loss, as the retained cyclotomic truncation in [C213](Yin_C_G0213_v2.md#polynomial-fiber-counterexample) demonstrates.
Passing from such a box to the global process requires a separate extension or uniform boundary-control argument.

Suppose now that $0<I_R<\infty$ for all sufficiently large $R$ and that its growth is subexponential:

$$
\limsup_{R\to\infty}\frac{\log^+ I_R}{R}=0.
\tag{11}
$$

This includes bounded strictly positive finite-valued weights and weights bounded above by a fixed polynomial in $\|x_C\|$, uniformly in the compact coordinates.
If $P^Nf\le\theta f$ throughout $D$, the left inequality in (10) gives

$$
\theta I_R\ge M^{-N}I_{R-Nb}.
$$

If $\theta<M^{-N}$ and $b>0$, choose $R_0$ with $I_{R_0}>0$ and iterate at $R=R_0+kNb$:

$$
I_{R_0+kNb}\ge
\left(\frac{M^{-N}}{\theta}\right)^k I_{R_0}.
$$

Taking $k$th roots contradicts (11).
The case $\theta=0$ is an immediate contradiction; if $b=0$, no truncation loss occurs and the same conclusion follows directly.
Therefore (9) remains valid for all weights in this subexponential-mass class, even though $\mu(D)=\infty$.

An integrable weight need not be bounded below, but it must have positive $\mu$-mass.
A weight growing exponentially in the neutral radius is not covered by (11).
No conclusion for arbitrary unbounded weights is asserted.

## 4. What this closes, and what it does not

For any such all-continuous-state certificate,

$$
-\frac{\log\theta}{N}\le\log M=m(\lambda).
\tag{12}
$$

This includes all real and complex expanding/contracting embeddings and all neutral directions, without expansiveness.
If all embeddings are neutral, $M=1$ and (9) excludes $\theta<1$ in this class, consistently with the cyclotomic controls.
No assumption that Salem numbers tend to 1 is made.

The necessary numerical upper bound (12) already follows for any valid collision certificate from $h_2\le m/\log2$.
It is not a second proof of a new Mahler-gap obstruction.
The additional information is the explicit dual measure (7), the neutral boundary control (10), and the fact that their construction never uses a minimal polynomial, an integer lattice, or arithmetic reachability.

Indeed the whole argument works for an arbitrary finite list of real/complex nonzero parameters $\beta_\sigma$ with $\prod|\beta_\sigma|^{d_\sigma}=1$, whether or not they are conjugates of an algebraic number.
Such continuous lists can have one real pair $e^\varepsilon,e^{-\varepsilon}$ and any fixed neutral rotations, with $M=e^\varepsilon\to1$.
Thus a uniform claim over this unrestricted continuous model fails the explicit dual test.

This does not rule out a uniform certificate on the actual arithmetic parameter family: an independent arithmetic argument could restrict its admissible spectra.
It also does not rule out certificates proved only on the actual reachable lattice states.
When $U$ has positive real dimension, the embedded order is countable and has $\mu$-measure zero, so an inequality on its reachable states alone supplies no inequality for this dual integral.
The precise consequence for route selection is to retain arithmetic reachability or supply a separate arithmetic restriction on spectra; the relaxed geometry alone does not distinguish algebraic-integer parameters from those arbitrary near-trivial continuous lists.

The unit condition is used essentially in identifying the $U$ inverse Jacobian with $M^{-1}$.
For nonunits, one must retain the field norm and, for nonintegral numbers, the leading-coefficient normalization; they are outside this draft's claim.
