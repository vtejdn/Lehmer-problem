---
author: Yin
---

# G0001: finite carry domination and the central-fiber obstruction

Date: 2026-10-06.
Status: preserved original exploration, failed-inference comparison and uniformity boundary.
The complete precise theorem is now adopted in [C213 v2](../claims/Yin_C_G0213_v2.md#statement); the actual formal findings belong to [R505](../audits/reviews/Yin_R_G0505_v1.md), and original native evidence belongs to [J117](../computations/programs/Yin_J_G0117/readme.md).


The proposed inference has a precise conditional form: a finite weighted operator that dominates every relevant carry transition can give an exponential return bound, and a proved polynomial multiplicity factor does not change its rate.
However, polynomially many central endpoint states do not establish that operator comparison.
Exact finite algebraic quotients have leading spectral radius 1; arbitrary finite truncations can have a misleading strict gap.

This draft gives an explicit non-discrete hyperbolic projection for the quartic Salem example, a counterexample to repairing omitted transitions by a polynomial endpoint count, and a valid all-length block certificate for that Salem example.
The last certificate does not improve the already available per-parameter bound and does not supply a uniform gap.

## 1. Reuse and exact question

The current route is [S G0002](../strategies/Yin_S_G0002.md#next-step-and-decision-conditions), supporting [T G0001](../tasks/Yin_T_G0001_v1.md#contract).
Reuse [C212 carry theorem](../claims/Yin_C_G0212_v1.md#carry-state-bound) for the carry formula, digit probabilities, embedding bounds and the distinction between finite collision counts and an all-length lower estimate.
Reuse [L G0003](Yin_L_G0003_v1.md) for the exact quartic reciprocal example and the finite-time induction boundary, and [C209](../claims/Yin_C_G0209_v1.md#gram-lower-certificate) for the integer Gram/discriminant bound.

Shared structure across families; current organization requires the common representation to retain the complete target data; here that means both the arithmetic state and transition probabilities.
Uniform descent and finite closure; current organization requires a comparison on the actual domain, rather than on chosen representatives with unproved lifting.
These are applicability guides, not extra theorem inputs.

The existing local carry identities and ordinary direct calculations suffice for this test.
No new primary source is selected, downloaded or invoked.
No novelty claim is made for the block-escape calculation or the elementary Markov/operator inequalities below.

Let $\lambda$ be an algebraic unit, $R=\mathbb Z[\lambda]$, and

$$
c_{j+1}=\lambda^{-1}(c_j+\delta_j),\quad c_0=0,
\qquad
\mathbb P(\delta=-1,0,1)=(1/4,1/2,1/4).
$$

Then $q_n=\mathbb P(c_n=0)$ is the collision probability of the fair binary digit sum, and $h_2=\lim_n-\log_2(q_n)/n$.
The existence and direction of this limit have their complete adopted proof in [C212](../claims/Yin_C_G0212_v1.md#collision-entropy-directions).

<a id="valid-finite-domination"></a>
## 2. The sufficient finite comparison, with its whole-domain obligation

Let $S\subset R$ contain every intermediate state of every finite path from 0 back to 0.
It may be infinite.
Kill a transition when it leaves $S$, and let $T$ be the resulting substochastic kernel.
Every returning path remains in $S$, so

$$
q_n=(T^n)_{00}.
$$

Suppose $\pi:S\to Q$ takes values in a finite set, and $v:Q\to(0,\infty)$ satisfies $v(\pi(0))=1$.
For a fixed block length $N$, the sufficient hypothesis is the pointwise inequality

$$
T^N(v\circ\pi)(c)\le\theta\,v(\pi(c))
\quad\text{for every }c\in S,\qquad \theta<1. \tag{1}
$$

By induction, $q_{jN}\le\theta^j$ and therefore

$$
h_2\ge-\frac{\log_2\theta}{N}. \tag{2}
$$

There is no need to multiply by the number of central states in this proof.
The comparison is already pointwise on all states.
Checking (1) only at one representative per cell does not prove it on that cell.

One sufficient finite-matrix implementation is a nonnegative matrix $K$ such that, for every $c\in S$ and every $b\in Q$,

$$
\sum_{\substack{d\in S\\\pi(d)=b}} T^N(c,d)
\le K_{\pi(c),b}.
$$

If $Kv\le\theta v$, (1) follows.
Taking a separate supremum for each destination cell is valid but may make row sums larger than 1; it must not be renormalized downward.
A digit whose image can lie in several cells must be covered with its full probability in every upper-bound entry that needs it.
Deleting ambiguous transitions instead produces a lower model, unsuitable for an upper bound on $q_n$.

A weaker, explicitly proved comparison

$$
q_n\le C_\lambda(1+n)^{s_\lambda}
\theta_\lambda^{\lfloor n/N_\lambda\rfloor} \tag{3}
$$

would also give (2) with the corresponding parameter-dependent constants.
For each fixed parameter, a finite exponent $s_\lambda$ and prefactor $C_\lambda$ do not affect the limiting rate.
A uniform positive result additionally requires

$$
\inf_\lambda\frac{-\log_2\theta_\lambda}{N_\lambda}>0.
$$

The endpoint-state bound in L G0005 supplies neither (1) nor (3).
In particular, a path lifting estimate must control the **total probability weight of lifted paths**, not merely the number of possible endpoints.

## 3.
Exact finite algebraic quotients have no killed spectral gap

For an integer $m\ge2$, the quotient $R/mR$ is a finite ring of size $m^d$, where $d=[\mathbb Q(\lambda):\mathbb Q]$.
Since $\lambda$ is a unit, each map

$$
\bar c\longmapsto\bar\lambda^{-1}(\bar c+\bar\delta)
$$

is a permutation.
The quotient carry kernel is a convex combination of three permutation matrices.
Its row sums equal 1 and its leading spectral radius is exactly 1.

More concretely, write $\bar X_n$ for the binary digit sum modulo $mR$.
Then its quotient return probability is

$$
\bar q_n=\mathbb P(\bar X_n=\bar X'_n)
=\sum_{a\in R/mR}\mathbb P(\bar X_n=a)^2
\ge m^{-d} \quad\text{for every }n. \tag{4}
$$

The genuine event is contained in the modular event, so $q_n\le\bar q_n$.
The positive lower floor in (4) makes this upper bound incapable of proving exponential decay.
A gap between the largest and second largest quotient eigenvalues, when present, is a mixing statement and is not the strict leading-radius bound required in (1).
This obstruction applies to the quartic Salem parameter itself, not only to a cyclotomic control.

For the quartic order and $m=2$, the four digits at exponents $0,1,2,3$ give each element of the 16-element quotient exactly once.
Thus $\bar X_4$ is uniform.
Subsequent multiplication by the unit $\bar\beta$ and addition of an independent digit preserve that uniform distribution, so $\bar q_n=1/16$ for every $n\ge4$.

The case of the one-element quotient is especially transparent: its kernel is $[1]$.
Replacing it by a killed matrix such as $[1/2]$ is an additional restriction on paths, not a quotient operation.

<a id="quartic-projection-obstruction"></a>
## 4. An explicit non-discrete projection for the quartic Salem order

Take

$$
p(t)=t^4-t^3-t^2-t+1,
$$

and let $\beta>1$ be its expanding real root.
As checked in L G0003, $p$ is irreducible, and its roots are $\beta,\beta^{-1},\zeta,\bar\zeta$, with $|\zeta|=1$.
Dividing by $t^2$ gives the trace equation $y^2-y-3=0$, so

$$
y_+=\beta+\beta^{-1}=\frac{1+\sqrt{13}}2,\qquad
y_-=\zeta+\bar\zeta=\frac{1-\sqrt{13}}2.
$$

Define

$$
a=y_+-2=\frac{\sqrt{13}-3}{2}\in(0,1),\qquad
\eta=\beta+\beta^{-1}-2\in\mathbb Z[\beta].
$$

The order membership is exact, because

$$
\beta^{-1}=-\beta^3+\beta^2+\beta+1.
$$

At the two real embeddings, $\eta$ has value $a$.
At the two unit-circle embeddings, it has value

$$
y_--2=-\frac{\sqrt{13}+3}{2}=-a^{-1}.
$$

Thus for every integer $k\ge1$, the nonzero order element $\eta^k$ satisfies

$$
\pi_{\rm hyp}(\eta^k)=(a^k,a^k)\longrightarrow(0,0),\qquad
\sigma_{\rm cen}(\eta^k)=(-a^{-1})^k. \tag{5}
$$

Its absolute field norm equals 1.
This is an explicit sequence proving that the hyperbolic projection of $\mathbb Z[\beta]$ is not discrete.
Any fixed open hyperbolic rectangle around 0 contains infinitely many such projected points.

The projection does not have a nonzero arithmetic kernel: even one field embedding is injective.
Hence the order has no nonzero subgroup lying wholly in the geometric central subspace.
There is no direct operation of quotienting the order by a rank-two central lattice to obtain a discrete rank-two hyperbolic lattice.
The full Minkowski embedding is a lattice, but its hyperbolic projection is not.

The elements in (5) are ambient order elements.
This draft does **not** assert that every one occurs on a binary-digit return path.
Their role is to refute the inference “bounded hyperbolic coordinates exhaust a finite state region.” Reachability would need a separate argument.

For an actual return path of length $n$, the central coordinate has size at most $n$, by L G0005.
Together with the fixed hyperbolic bounds this gives only $O_\beta((1+n)^2)$ possible lattice states, by packing in the full four-real-dimensional Minkowski lattice.
The constant depends on the order and its embedding.
Keeping the full norm explains what projection discards: for a nonzero order element $x$,

$$
1\le |N_{\mathbb Q(\beta)/\mathbb Q}(x)|
=|\sigma_+(x)\sigma_-(x)|\,|\sigma_{\rm cen}(x)|^2.
$$

Bounding the central coordinate by $O(n)$ yields a separation that deteriorates with $n$, not a fixed separation of the projected states.
Exact projection retains algebraic identities; replacing its non-discrete image by independently rounded coordinates loses that arithmetic information unless a comparison is proved.

<a id="polynomial-fiber-counterexample"></a>
## 5. Polynomial endpoint fibers do not control weighted path fibers

There are two different issues.

First, for an ordinary probability distribution $p$ on a finite set and a map $\pi$ with fibers of size at most $M$,

$$
\sum_xp(x)^2
\le\sum_y\left(\sum_{\pi(x)=y}p(x)\right)^2
\le M\sum_xp(x)^2. \tag{6}
$$

This is the valid endpoint comparison.
If the target has a fixed finite size and $M$ grows only polynomially with time, (6) forces zero collision entropy rate: the middle expression is bounded below by the reciprocal target size.
Thus a positive-rate digit sum cannot have its **whole unconditioned endpoint support** represented by a fixed finite quotient with only polynomially many endpoints over each quotient point.

The polynomial carry-state count concerns intermediate states on a path already constrained to return.
It is not a polynomial bound on the whole unconditioned digit-sum support.
Normalizing the conditional midpoint distribution discards precisely the unknown probability of the returning event.

Second, a fixed central truncation can discard exponentially much return weight even when the whole accessible central region has only polynomially many states.
The exact control is $\lambda=1$:

$$
c_{j+1}=c_j+\delta_j,\qquad
q_n=\frac{\binom{2n}{n}}{4^n}\ge\frac1{2n+1}. \tag{7}
$$

The identity follows by summing the squared binomial probabilities, and the inequality follows because the central binomial coefficient is the largest of the $2n+1$ coefficients whose sum is $4^n$.
Only $2n+1$ states are reachable at time $n$.

Now truncate to the single central state $\{0\}$ and kill excursions.
The finite matrix is $[1/2]$, with strict leading spectral radius $1/2$, and its return probability is $2^{-n}$.
Nevertheless

$$
\frac{q_n}{2^{-n}}\ge\frac{2^n}{2n+1}. \tag{8}
$$

No polynomial multiplicative correction repairs this finite truncation.
Already the two-digit path $(+1,-1)$ leaves the truncation and returns; all such omitted excursions carry the missing weight.
The exact one-state quotient instead retains all digits and has matrix $[1]$, as Section 3 requires.

This control is cyclotomic and does not refute a theorem with additional verified Salem-specific transition estimates.
It does refute the proposed inference from “finite truncated matrix with a strict gap” plus “polynomially many omitted central states” alone.

<a id="salem-block-certificate"></a>
## 6. A valid all-length certificate despite the central conjugates

A positive per-parameter certificate need not solve the full central-state enumeration.
Let $\beta>1$ be a real algebraic unit having $\beta^{-1}$ as a conjugate.
The quartic example has this property.
At the contracting embedding, write $y_j=\sigma_-(c_j)$.
Then

$$
y_{j+1}=\beta(y_j+\delta_j).
$$

Every returning path stays in

$$
J=(-R,R),\qquad R=\frac{\beta}{\beta-1}.
$$

Choose $N\ge1$ such that $\beta^N>R$.
Starting from any $y\in J$, condition on the last $N-1$ digits of the next block.
The two endpoints obtained by choosing the first digit $+1$ or $-1$ differ by $2\beta^N>2R$.
They cannot both lie in $J$.
The excluded choice has conditional probability $1/4$.
Therefore the probability that the block endpoint remains in $J$ is at most $3/4$, uniformly in its starting point and in the conditioned digits.

A returning path must pass this test at every complete block.
Successive conditioning gives the all-length bound

$$
q_n\le(3/4)^{\lfloor n/N\rfloor},\qquad
h_2(\beta)\ge\frac{\log_2(4/3)}{N}. \tag{9}
$$

Killing at intermediate exits only decreases survival further.
This is a valid one-cell **domination** at block length $N$; it is not the assertion that all states in that cell have identical transition probabilities.
Central coordinates may be ignored here because a genuine return must satisfy the retained necessary condition, and the inequality was proved for every real starting point in the enlarged interval.

For the quartic root, $\beta>\varphi$.
Indeed $y_+^2=(7+\sqrt{13})/2>5$, while $\varphi+\varphi^{-1}=\sqrt5$ and $t+t^{-1}$ is increasing on $t>1$.
Hence $\beta(\beta-1)>1$, so $\beta^2>R$.
Taking $N=2$ gives the exact control

$$
q_n\le(3/4)^{\lfloor n/2\rfloor},\qquad
h_2(\beta)\ge\tfrac12\log_2(4/3)>0. \tag{10}
$$

This bound is weaker than the selected-digit bound already obtainable from L G0005: $\beta^2>2$ permits selecting every second binary digit, yielding $h_2\ge1/2$.
Its purpose is to exhibit the full-state domination proof that a finite carry model needs, not to improve a known numerical lower bound.

For $\beta$ approaching 1, this block choice has $N$ of order $\log(1/(\beta-1))/(\beta-1)$, so the supplied lower bound tends to zero.
No degree-uniform or parameter-uniform positive constant has been obtained.

## 7. A rigorous limitation of the continuous one-place relaxation

The preceding calculation has a useful exact upper limit on what its entire class of bounded positive weights could prove.
Use the closed interval $J=[-R,R]$, which differs from the open interval only by endpoints for integration, and define the killed operator on nonnegative functions by

$$
Pf(x)=\sum_{\delta=-1}^1w_\delta
\mathbf 1_J\bigl(\beta(x+\delta)\bigr)
f\bigl(\beta(x+\delta)\bigr).
$$

For all three digits, $\beta(J+\delta)$ contains $J$, because $(\beta-1)R=\beta$.
A change of variables in each summand gives, for integrable $f\ge0$,

$$
\int_J Pf(x)\,dx=\beta^{-1}\int_Jf(x)\,dx,
\qquad
\int_J P^Nf(x)\,dx=\beta^{-N}\int_Jf(x)\,dx. \tag{11}
$$

If $0<\int_Jf<\infty$ and $P^Nf\le\theta f$ on every point, then necessarily

$$
\theta\ge\beta^{-N},\qquad
\frac{-\log_2\theta}{N}\le\log_2\beta. \tag{12}
$$

In particular, finite piecewise-positive weights covering the entire real interval cannot certify a rate bounded away from zero along parameters tending to 1.
The statement is conditional on such a family existing in the selected arithmetic class; it does not presume Salem numbers tending to 1.
Nor does (12) rule out sharper certificates that retain several conjugates and exact arithmetic reachability.
It identifies the information deliberately lost by this particular one-place relaxation.

## 8. Relation to support attainment and the Gram route

Support and collision weight must stay separate.
For any real $1<\beta\le2$, set $I=[0,1/(\beta-1)]$.
The elementary covering identity

$$
I=\beta^{-1}I\ \cup\ \beta^{-1}(1+I)
$$

iterates and, after scaling by $\beta^n$, yields

$$
\beta^n I=\bigcup_{x\in D_n(\beta)}(x+I).
$$

Interval length therefore gives $|D_n(\beta)|\ge\beta^n$ for every $n$.
For the Pisot/Salem cases with $M(\beta)=\beta$, the already accepted support packing upper bound gives support rate $\log\beta$.
Unit-circle conjugates do not prevent this support conclusion.
The covering gives no upper bound on $\sum_xr_n(x)^2$ and therefore does not close the collision problem.
The complete current local-entropy statement and source scope belong to [C210](../claims/Yin_C_G0210_v1.md#pisot-salem-attainment); the original scoped check is retained in [R800](../audits/reviews/Yin_R_G0800_v1.md#original-coordinating-domination-finding).
It is not promoted to a new literature attribution.

On the Gram side, L G0004 retains

$$
|\operatorname{disc}p|\,G_N
\le\prod_{i=1}^d\sum_{j=0}^{N-1}|\alpha_i|^{2j}
\le N^dM(p)^{2(N-1)}.
$$

Each unit-circle factor is exactly $N$.
At fixed polynomial, logarithms of polynomial factors divided by $N$ vanish.
This does not make them negligible in a proposed uniform finite certificate at $N$ proportional to a varying degree.
In the carry problem the additional missing step comes earlier: the polynomial state count does not yet imply any upper comparison for return weights.

The next useful gate is therefore an arithmetic transition/weight inequality on the complete returning domain, such as (1) or a proved version of (3).
Finite algebraic quotients alone fail this gate by (4).
Representative truncation plus a polynomial central count fails by (8).
The valid quartic domination (10) passes the all-length gate but fails uniformity, and the continuous relaxation limitation (12) explains why its rate cannot remove that loss by finer interval weights alone.

## 9. Original finite controls and scoped findings

The [complete original source, JSON and finite table](../computations/programs/Yin_J_G0117/readme.md) retain all quartic n=0–16 and cyclotomic n=0–64 assertions and both original 2026-10-06 executions.
Finite tables do not prove the all-length operator comparisons or a uniform gap; those arguments remain completely stated above and in C213.
The [original author check](../audits/reviews/Yin_R_G0505_v1.md#original-author-domination-check), [complete coordinating finding/replay](../audits/reviews/Yin_R_G0800_v1.md#original-coordinating-domination-finding) and [separate Sections4/7 finding](../audits/reviews/Yin_R_G0800_v1.md#original-projection-interval-finding) retain their exact original scopes and distinct actual relationships.
The current complete v2 self-check does not establish historical context isolation, and this maintenance runs no program.
