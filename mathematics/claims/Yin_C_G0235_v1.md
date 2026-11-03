---
author: Yin
---

# All-time greedy atom bounds and exact one-expanding Renyi rate comparison

This retains the complete L30 argument and its parameter-dependent boundaries.
Its first-place elementary digit separation uses no inaccessible MS25 theorem.

## Statement

Let lambda be a nonzero algebraic number and sigma:Q(lambda) to C an embedding with beta=sigma(lambda), rho=|beta|>1.
For independent fair binary digits, put X_n=sum_{j=0}^{n−1} B_j lambda^j, a=log(1+rho)/log(rho)>1, J_n=1+floor((n−1)/a).
For every integer n>=1, the largest atom and collision probability of X_n are both at most2^{-J_n}.
For every fixed Renyi order alpha in[0,infinity], including Shannon at1 and maximum-atom order infinity, the finite-distribution entropies are subadditive and

    h_alpha=lim_n H_alpha(X_n)/n=inf_n H_alpha(X_n)/n
           >= log2 log(rho)/log(1+rho).

All logarithms are natural.
If in addition lambda=beta is a real algebraic integer in(1,2) with every other conjugate of modulus at most1, put m=log beta.
Then there are finite parameter-dependent C_beta>0,s>=0 such that for every n>=1 and every order,

    J_n log2 <= H_alpha(X_n) <= n m+s log n+log C_beta,
    m log2/log(1+exp m) <= h_infinity <= h_alpha <= h_0=m,
    0 <= m−h_alpha <= m^2/(2 log2).

The exact bounding comparison width m−m log2/log(1+exp m) has expansion m^2/(2 log2)+O(m^3) as m tends to0; this is not an asymptotic equality for the actual entropy deficit.
Thus along any hypothetical Salem sequence with m tending to0 all fixed-order h_alpha/m tend to1, without asserting such a sequence exists.
For general units the lower bound uses only the chosen log rho and does not replace it by total multi-place Mahler measure.
These are binary-random-sum entropies, not algebraic entropy by definition, and no parameter-uniform finite convergence time or Lehmer gap follows.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:12 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nonzero algebraic lambda with a chosen expanding complex embedding, every word length n>=1 and every fixed Renyi order in[0,infinity], with the exact real one-expanding algebraic-integer specialization and parameter-dependent finite support constants. |
| argument | [Argument](#argument) | Complete greedy exponent/count and complex domination, conditional maximum-atom and collision bounds, all-order merging/subadditivity/Fekete existence, exact support comparison, quadratic deficit and precise hypothetical-sequence/multiple-place limits. |
| dependency | [Complete one-expanding support attainment](Yin_C_G0210_v1.md#pisot-salem-attainment) | Real algebraic integer1<beta<2 with every other conjugate of modulus at most1; full parameter-dependent support upper bound and exact limiting rate log(beta), with retained accepted BV20 source boundary. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:16 |
| status | proved |
| reason | The registered exact statement, every complete retained proof and necessary accepted interface have actual current whole self-review; all finite-parameter, conditional, exceptional and no-uniform-conclusion boundaries are preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nonzero algebraic lambda with a chosen expanding complex embedding, every word length n>=1 and every fixed Renyi order in[0,infinity], with the exact real one-expanding algebraic-integer specialization and parameter-dependent finite support constants. |
| argument | [Argument](#argument) | Complete greedy exponent/count and complex domination, conditional maximum-atom and collision bounds, all-order merging/subadditivity/Fekete existence, exact support comparison, quadratic deficit and precise hypothetical-sequence/multiple-place limits. |
| dependency | [Complete one-expanding support attainment](Yin_C_G0210_v1.md#pisot-salem-attainment) | Real algebraic integer1<beta<2 with every other conjugate of modulus at most1; full parameter-dependent support upper bound and exact limiting rate log(beta), with retained accepted BV20 source boundary. |
| review | [Actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-greedy-renyi-finding) | Entire exact registered statement and full proof, all necessary dependencies and stated boundary cases; no isolated independent or research completion claim. |

## Argument

<a id="greedy-atom-bound"></a>
### A bound for every word length

Let lambda!=0 be algebraic and let one embedding send it to beta with rho=|beta|>1.
Put

    a=log(1+rho)/log(rho)>1,     J_n=1+floor((n-1)/a).

For independent fair digits B_j in {0,1}, set X_n=sum_{j=0}^{n-1}B_j lambda^j and p_n^*=max_x P(X_n=x).
Then for every integer n>=1,

    p_n^* <= 2^{-J_n},      sum_x P(X_n=x)^2 <= 2^{-J_n}.

To prove this, select exponents greedily using positive weights rho^e.
Let e_0=0, S_0=1; for j>=1 choose the smallest nonnegative integer e_j with rho^{e_j}>S_{j-1}, and put S_j=S_{j-1}+rho^{e_j}.
The exponents increase strictly.
Minimality gives rho^{e_j-1}<=S_{j-1}, hence S_j<=(1+rho)S_{j-1}<=(1+rho)^j.
Therefore

    e_j <= 1+(j-1)a <= j a.

There are at least J_n selected exponents in {0,...,n-1}.
Their binary sums are distinct even for complex beta: in a nonzero difference the largest term has modulus rho^{e_j}, strictly greater than the sum S_{j-1} of all preceding moduli.
Equality at lambda would imply equality at beta under the embedding, so their sums at lambda are also distinct.

Condition on every unselected digit.
The remaining J_n fair independent digits give 2^{J_n} distinct values, so every conditional atom is at most 2^{-J_n}.
Averaging proves the maximum-atom bound.
Collision probability is at most the maximum atom since the probabilities sum to one.
In exponential form,

    p_n^* <= exp[-(n-1) log(2) log(rho)/log(1+rho)].

No finite-state truncation, degree bound, or parameter-uniform convergence time is used.

<a id="renyi-rates"></a>
### Entropy rates, including their existence

Use natural-log Renyi entropy H_alpha for alpha in [0,infinity], with the Shannon value at 1, H_0=log support size and H_infinity=-log maximum atom.
Monotonicity in order gives H_alpha(X_n)>=J_n log2.

For each fixed alpha these entropies are subadditive in n.
Indeed, X_{n+m} has the distribution of X_n+lambda^n X'_m for an independent copy.
The entropy of the independent pair is the sum of its entropies, scaling by lambda^n!=0 preserves atom masses, and merging atoms under deterministic addition cannot increase any of these Renyi entropies.
For 0<alpha!=1 this is the elementary power-sum inequality for merged probabilities; orders 0, 1 and infinity follow from support counting, Shannon's merging inequality, and p^*_{n+m}>=p_n^*p_m^*.
Thus Fekete's lemma supplies limits

    h_alpha=lim_n H_alpha(X_n)/n=inf_n H_alpha(X_n)/n,
    h_alpha >= log(2) log(rho)/log(1+rho).

These are entropies of the binary random sum, not DGB16 algebraic entropy by definition.

<a id="one-expanding-comparison"></a>
### The one-expanding-conjugate interface

Now assume the exact [L G0007 scope](Yin_C_G0210_v1.md#pisot-salem-attainment): real algebraic integer 1<beta<2, all other conjugates of modulus at most one.
Then m=log beta is its logarithmic Mahler measure, and the accepted support estimate has the form

    |support X_n| <= C_beta n^s beta^n.

Here C_beta and s are allowed to depend on beta.
Consequently every fixed order satisfies both the finite-time bounds

    J_n log2 <= H_alpha(X_n) <= n m+s log n+log C_beta

and the asymptotic comparison

    m log2/log(1+e^m) <= h_infinity <= h_alpha <= h_0=m.

In particular

    0 <= m-h_alpha <= m^2/(2 log2).

For the last inequality write L=log2 and log(1+e^m)=L+m/2+log cosh(m/2).
The elementary bound log cosh x<=x^2/2 gives

    m-h_alpha <= m(m/2+m^2/8)/(L+m/2) <= m^2/(2L),

where the last inequality uses L<=2.
Equivalently the exact comparison width is m^2/(2 log2)+O(m^3) as m tends to zero.

### Consequence and limitations

Along any hypothetical Salem sequence with m tending to zero, all fixed-order rates, including Shannon, collision and maximum-atom rates, necessarily satisfy h_alpha/m -> 1.
No existence of such a sequence is assumed.
A separate uniform Shannon-versus-collision comparison is therefore not an unresolved obstacle in that regime.
The all-time lower bound still tends to zero and proves no Lehmer gap.

For general units the argument captures only one expanding conjugate's log rho; it cannot replace that value by the sum over all expanding conjugates.
The next arithmetic question must either exclude small total Mahler measure itself or exploit multiple expanding places together.
Parameter-dependent C_beta does not supply a uniform finite-time convergence rate, so this result is consistent with [L G0020's long transient obstruction](Yin_C_G0222_v1.md#no-uniform-finite-time-rate).

The elementary bound on log cosh used above follows by integrating tanh x<=x for x>=0 and using evenness.
This supplies no additional source theorem or uniform arithmetic premise.
