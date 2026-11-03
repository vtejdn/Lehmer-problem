---
author: Yin
---

# G0001: greedy digit separation gives an all-time entropy comparison

Date: 2026-10-06.
The complete current mathematical home is [the responsible Claim](../claims/Yin_C_G0235_v1.md#argument), with [actual whole self-review](../audits/reviews/Yin_R_G0516_v1.md#current-greedy-renyi-finding).
The original mathematical body remains its historical fixed input and substantive exploration.
Direct argument supplied by assigned AI ms25_source after its bounded acquisition task ended, and checked by the coordinating AI for Yin.
This develops [L G0005's selected-digit method](Yin_L_G0005_v1.md#collision-entropy-directions) without using the inaccessible MS25 method.
No novelty claim is made.
The complete currently adopted selected-digit and entropy argument is [C212](../claims/Yin_C_G0212_v1.md#collision-entropy-directions), with the same parameter-dependent boundary as the original L5 input.

<a id="greedy-atom-bound"></a>
## A bound for every word length

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
## Entropy rates, including their existence

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
## The one-expanding-conjugate interface

Now assume the exact [L G0007 scope](Yin_L_G0007_v1.md#pisot-salem-attainment): real algebraic integer 1<beta<2, all other conjugates of modulus at most one.
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

## Consequence and limitations

Along any hypothetical Salem sequence with m tending to zero, all fixed-order rates, including Shannon, collision and maximum-atom rates, necessarily satisfy h_alpha/m -> 1.
No existence of such a sequence is assumed.
A separate uniform Shannon-versus-collision comparison is therefore not an unresolved obstacle in that regime.
The all-time lower bound still tends to zero and proves no Lehmer gap.

For general units the argument captures only one expanding conjugate's log rho; it cannot replace that value by the sum over all expanding conjugates.
The next arithmetic question must either exclude small total Mahler measure itself or exploit multiple expanding places together.
Parameter-dependent C_beta does not supply a uniform finite-time convergence rate, so this result is consistent with [L G0020's long transient obstruction](Yin_L_G0020_v1.md#no-uniform-finite-time-rate).

## Review and provenance

The assigned agent checked local G0005, G0007, G0008, G0011 and G0020 before deriving the greedy refinement; no MS25 proof was available or used.
The root checked strict domination for complex beta, integer exponent selection, conditional averaging, the Renyi merging argument and the exact quadratic bound.
The spectral support input remains external at L G0007's accepted BV20 scope.
These are direct consequences of the existing selected-digit idea and elementary probability; no broad literature priority claim or independent human review is made.
G0001 remains unresolved and the primary/secondary strategy order is unchanged.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0006_v1.md#independent-entropy-review), with its original inspected scope and relationship.
