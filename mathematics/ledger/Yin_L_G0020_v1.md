---
author: Yin
---

# G0001: long free digit windows despite sparse neutral completion

Date: 2026-10-06.
This tests whether the bounded-support route of [L G0019](Yin_L_G0019_v1.md#controlled-entropy-completion), together with all-power degree preservation, can yield a uniform finite-time approximation of entropy.
The answer is negative even below Mahler measure 4/3.
This is not a Lehmer counterexample: the entropies below approach a fixed positive value.

## Inputs and search

Reused local inputs: [L G0007](Yin_L_G0007_v1.md#pisot-salem-attainment) for binary support attainment, [L G0016](Yin_L_G0016_v1.md#expanding-prime-count) for all-power preservation when there is one expanding conjugate, and [L G0005](Yin_L_G0005_v1.md#collision-entropy-directions) for entropy comparisons.
The new established external input is the [Salem construction statement](../audits/literature/Smy15/Yin_U002.md#smy15-u002), with its original proof boundary explicit.
The currently adopted full versions of the reused support and collision inputs are [C210](../claims/Yin_C_G0210_v1.md#pisot-salem-attainment) and [C212](../claims/Yin_C_G0212_v1.md#collision-entropy-directions); these current proof entrances do not change the original input record.

The bounded search on 2026-10-06 first considered sparse multiples and positive-root restrictions.
It did not establish an obstruction in the low-measure class, so no result from those hits was adopted.
The more relevant query was "Salem construction x^n (x^2-x-1) reciprocal polynomials Salem numbers golden ratio limit".
The author-hosted Smy15 Section 3.1 supplied the needed construction; the cubic seed below puts the example closer to the small-measure regime.
No exhaustive search or new construction is claimed.

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

Every positive power of tau_N has degree d_N by the one-expanding-conjugate argument in L G0016.
Thus this family already satisfies all-power reduction and has cyclotomic support complexity at most six.
Its degree escape cannot be removed by the degree-lowering operation from L G0014.

<a id="no-uniform-finite-time-rate"></a>
## Finite trajectories and a fixed error

Let X_n(tau) be the binary digit sums from L G0007.
If n<=d_N, two distinct words cannot have the same sum: their difference would be a nonzero polynomial of degree at most n-1<d_N vanishing at tau_N.
Consequently

    |X_n(tau_N)|=2^n,  (1/n)log|X_n(tau_N)|=log2
    for every 1<=n<=d_N.

Nevertheless L G0007 gives the limiting support rate log(tau_N)<log(4/3).
For every finite observation length n, there is therefore a member for which

    (1/n)log|X_n(tau_N)| - H(tau_N,{0,1}) > log(3/2).

There is no uniform convergence time even on the class specified above.
For independent fair digits, injectivity makes the time-n distribution uniform on 2^n points.
Its normalized Shannon and order-two Renyi entropies also equal log2 throughout that window, while their limiting rates are at most the support rate.
The same fixed error applies.
This does not assert equality of the three limiting rates.

In the affine semigroup with generators z -> tau_N*z and z -> tau_N*z+1, distinct length-n words have distinct translations exactly when the binary sums do.
Hence the example also excludes inferring uniformly visible asymptotic growth from long initial free word windows under these same restrictions.

## Review and route consequence

The original complete author check is retained at [R510](../audits/reviews/Yin_R_G0510_v1.md#original-salem-delay-author-check).
The current complete six-term family and finite-time theorem is [C222](../claims/Yin_C_G0222_v1.md#argument), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0510_v1.md#current-salem-delay-finding).

This strengthens the earlier cyclic-induction warning by keeping all-power degree preservation and a six-term zero-extra-entropy completion, inside M<4/3.
A uniform sparse-presentation theorem could still prove a gap through DS17; it must not be bundled with a false uniform finite-time convergence assertion.
The actual remaining target is a low-entropy structural representation or a direct arithmetic estimate.
The sequence here has m(p_N)->log(theta)>0 and cannot refute Lehmer.
