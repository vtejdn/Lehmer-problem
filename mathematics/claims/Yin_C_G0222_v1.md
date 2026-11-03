---
author: Yin
---

# All-power-stable six-term Salem completions have no uniform finite-time entropy rate

This retains the complete original2026-10-06 [L20](../ledger/Yin_L_G0020_v1.md) proof and exact positive-limit boundary.
All entropy expressions in this statement use natural logarithms.

## Statement

Let f(x)=x^3−x−1 and let theta>1 be its real root.
There is an unspecified threshold N0, supplied by the accepted Salem construction, such that for every integer N>=max(N0,16),

    q_N=x^N f+f*=x^(N+3)−x^(N+1)−x^N+1−x^2−x^3

has exactly six nonzero coefficients and factors as the monic minimal polynomial p_N of a Salem number tau_N times a monic cyclotomic product c_N.
One has theta<tau_N<4/3, tau_N tends to theta, m(q_N)=m(p_N)=log(tau_N), and m(c_N)=0.
The tau_N are pairwise distinct and their degrees d_N tend to infinity; every positive integer power has degree d_N.
For every integer1<=n<=d_N, all2^n binary digit sums at tau_N are distinct, so normalized log-support, Shannon entropy and order-two Renyi entropy for fair digits all equal log2.
The limiting support rate is log(tau_N)<log(4/3); the other two limiting rates are at most that value.
For each finite observation length n there is such a member whose finite normalized value exceeds its respective limiting rate by more than log(3/2).
The same exact digit-injectivity conclusion holds for length-n words in z maps to tau_N z and z maps to tau_N z+1.
Thus all-power degree preservation, M<4/3 and a six-term zero-extra-entropy cyclotomic completion do not give a uniform finite-time convergence bound.
The construction supplies no effective N0 and does not claim N=16 alone clears it.
Its positive limiting measure log(theta) is not a vanishing-entropy family or a counterexample to Lehmer.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:13 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The fixed plastic Pisot seed and all sufficiently large integers N, with the external threshold retained, every positive power, all1<=n<=d_N finite windows, natural-log entropy comparisons and the exact no-uniform-time quantifier. |
| argument | [Argument](#argument) | Complete cubic/Pisot and six-term sign calculation, b=4/3 bound, threshold caveat, distinctness/degree escape, all-power degree, binary injectivity, Shannon/Renyi and affine-word consequences, with positive limiting entropy. |
| dependency | [Salem construction](../audits/literature/Smy15/Yin_U002.md#smy15-u002) | Accepted sufficiently-large-N construction for the nonreciprocal Pisot cubic and plus sign; no effective threshold or original Salem proof audit. |
| dependency | [Actual binary support attainment](Yin_C_G0210_v1.md#pisot-salem-attainment) | Tau_N in(1,4/3) is an algebraic integer with one expanding root, giving the exact limiting support rate log(tau_N). |
| dependency | [Positive-power expanding fibers](Yin_C_G0219_v1.md#expanding-prime-count) | r=1 forces degree preservation for every positive integer power, without a total degree bound. |
| dependency | [Collision and entropy directions](Yin_C_G0212_v1.md#collision-entropy-directions) | Existence/comparison of normalized support, Shannon and order-two rates, with the stated natural-log conversion; no equality of their limits asserted. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:14 |
| status | proved |
| reason | Adopt the exact complete retained theorem after actual whole current self-review, retaining every source, parameter, finite-time and unrestricted-goal boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The fixed plastic Pisot seed and all sufficiently large integers N, with the external threshold retained, every positive power, all1<=n<=d_N finite windows, natural-log entropy comparisons and the exact no-uniform-time quantifier. |
| argument | [Argument](#argument) | Complete cubic/Pisot and six-term sign calculation, b=4/3 bound, threshold caveat, distinctness/degree escape, all-power degree, binary injectivity, Shannon/Renyi and affine-word consequences, with positive limiting entropy. |
| dependency | [Salem construction](../audits/literature/Smy15/Yin_U002.md#smy15-u002) | Accepted sufficiently-large-N construction for the nonreciprocal Pisot cubic and plus sign; no effective threshold or original Salem proof audit. |
| dependency | [Actual binary support attainment](Yin_C_G0210_v1.md#pisot-salem-attainment) | Tau_N in(1,4/3) is an algebraic integer with one expanding root, giving the exact limiting support rate log(tau_N). |
| dependency | [Positive-power expanding fibers](Yin_C_G0219_v1.md#expanding-prime-count) | r=1 forces degree preservation for every positive integer power, without a total degree bound. |
| dependency | [Collision and entropy directions](Yin_C_G0212_v1.md#collision-entropy-directions) | Existence/comparison of normalized support, Shannon and order-two rates, with the stated natural-log conversion; no equality of their limits asserted. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0510_v1.md#current-salem-delay-finding) | Entire exact Statement and Argument after actual current contributor self-review, with resolved accepted inputs and no isolated-review or original-proof-audit claim. |

## Complete retained argument

<a id="argument"></a>

<a id="sparse-salem-delay-family"></a>
## A six-term family and its actual irreducible factors

Let f=x^3-x-1 and let theta be its real root greater than one.
This cubic is irreducible over Q by the rational-root test, and its discriminant is -23.
Its other two roots are nonreal conjugates with modulus theta^(-1/2)<1, since the product of all three roots is 1.
Thus theta is Pisot.
Also theta<4/3, because f is strictly increasing on [1,infinity), f(1)<0 and f(4/3)=1/27>0.

For sufficiently large integers N define

    q_N(x)=x^N f(x)+f*(x)
          =x^(N+3)-x^(N+1)-x^N+1-x^2-x^3.

For N>3 it has exactly six nonzero coefficients and length six.
The accepted construction gives q_N=p_N c_N, with p_N the monic minimal polynomial of a Salem number tau_N and c_N a monic product of cyclotomic factors.
In particular m(c_N)=0 and m(q_N)=m(p_N)=log(tau_N).

The selected root lies above theta.
Indeed q_N(theta)=1-theta^2-theta^3=-theta^2-theta<0.
At b=4/3,

    q_N(b)=(b^N-85)/27>0  for N>=16.

The unique root outside the unit circle supplied by the construction must therefore satisfy theta<tau_N<4/3, once N is also beyond the construction's unspecified threshold.
The same argument with any fixed b>theta shows tau_N->theta.
No claim that N=16 itself clears the external threshold is made.

These tau_N are pairwise distinct: a common root tau>theta of q_N and q_M would imply tau^N=-f*(tau)/f(tau)=tau^M and hence N=M.
Their degrees d_N tend to infinity.
For each fixed d bound, monic integer minimal polynomials of degree at most d and measure below 4/3 have bounded coefficients, by |a_j|<=binomial(d,j)M with the actual degree in each polynomial.
There are only finitely many such polynomials and roots; distinctness therefore excludes infinitely many bounded-degree members.

Every positive power of tau_N has degree d_N by the one-expanding-conjugate argument in C219.
Thus this family already satisfies all-power reduction and has cyclotomic support complexity at most six.
Its degree escape cannot be removed by the degree-lowering operation from C218.

<a id="no-uniform-finite-time-rate"></a>
## Finite trajectories and a fixed error

Let X_n(tau) be the binary digit sums from C210.
If n<=d_N, two distinct words cannot have the same sum: their difference would be a nonzero polynomial of degree at most n-1<d_N vanishing at tau_N.
Consequently

    |X_n(tau_N)|=2^n,  (1/n)log|X_n(tau_N)|=log2
    for every 1<=n<=d_N.

Nevertheless C210 gives the limiting support rate log(tau_N)<log(4/3).
For every finite observation length n, there is therefore a member for which

    (1/n)log|X_n(tau_N)| - H(tau_N,{0,1}) > log(3/2).

There is no uniform convergence time even on the class specified above.
For independent fair digits, injectivity makes the time-n distribution uniform on 2^n points.
Its normalized Shannon and order-two Renyi entropies also equal log2 throughout that window, while their limiting rates are at most the support rate.
The same fixed error applies.
This does not assert equality of the three limiting rates.

In the affine semigroup with generators z -> tau_N*z and z -> tau_N*z+1, distinct length-n words have distinct translations exactly when the binary sums do.
Hence the example also excludes inferring uniformly visible asymptotic growth from long initial free word windows under these same restrictions.
