---
author: Yin
---

# G0001: fair binary entropy comparisons in abelian groups

Date: 2026-10-07.
Direct adaptation by assigned AI ms25_source for Yin of Li's largest-fiber proof.
The coordinator independently read the source and contributed the extension to groups with 2-torsion through the pushforward inequality.
The source interface is in [Li26-U001](../audits/literature/Li26/Yin_U001.md#li26-largest-fiber-proof).
No novelty claim is made.

<a id="abelian-binary-entropy-comparison"></a>
## Finite-time comparison, including torsion

Let G be any abelian group, let g_1,...,g_n be any elements, and let X_1,...,X_n be independent fair Bernoulli variables on {0,1}.
For S=sum_i X_i g_i, using natural logarithms,

    H_1(S)<=H_(1/2)(S)<=2H_infinity(S)<=2H_2(S).           (1)

The finite support makes every entropy unambiguous, even if G has no topology or is uncountable.
Zero or repeated elements and torsion are allowed.
The statement is about the uniform binary input law, not an arbitrary distribution on its support.

Here is the full extension of the inspected real-weight proof.
Put f(t)=P(S=t), rho=max f, choose tau realizing rho, and take Y independently uniform on the fiber B={x in {0,1}^n:sum x_i g_i=tau}.
Let Z=X XOR Y.
Direct counting gives Z uniform and independent of Y.
For the conditional mass f_z(t)=P(S=t|Z=z),

    f_z(t)<=f(t)/rho,       average_z f_z(t)=f(t).         (2)

For f(t)>0, write phi_z(t)=f_z(t)/f(t).
Since phi_z<=rho^(-1), sqrt(phi_z)>=sqrt(rho) phi_z.
Average and sum to obtain

    sum_t sqrt(f(t))
       <=rho^(-1/2) average_z sum_t sqrt(f_z(t)).          (3)

For a fixed z, put I={i:z_i=0}.
Under the original product law define U=sum_(i in I) X_i g_i, V=sum_(i notin I) X_i g_i and c=sum_(i notin I) g_i.
These U,V are independent and U+V has law f.
The XOR identity shows that f_z is the image of the conditional law of U given U+V=tau under

    T_z(u)=c-tau+2u.                                    (4)

For completeness, Y is distributed as X conditioned on S=tau, and remains so after conditioning on Z=z.
Then sum_i (Y_i XOR z_i)g_i=c-tau+2 sum_(i in I)Y_i g_i, proving (4).

The map T_z may fail to be injective when G has 2-torsion.
This improves the needed inequality: for any finite mass p(u),

    sum_t sqrt(sum_(u:T_z(u)=t) p(u))<=sum_u sqrt(p(u)).

With a(u)=P(U=u), b(v)=P(V=v), the conditional mass before this pushforward is a(u)b(tau-u)/rho.
Therefore Cauchy--Schwarz gives

    sum_t sqrt(f_z(t))
       <=rho^(-1/2) sum_u sqrt(a(u)b(tau-u))
       <=rho^(-1/2).                                    (5)

Combining (3)--(5) proves sum sqrt(f)<=rho^(-1), or H_(1/2)<=2H_infinity.
Monotonicity gives the other inequalities in (1).
Thus no real embedding, order on G or injectivity of multiplication by two is required for this extension.
Only the original real-weight statement is attributed to Li26; this explicit group adaptation is the local argument.

<a id="binary-flow-renyi-rate-comparison"></a>
## Binary flows and finite-time bounds from their rates

Let T:G->G be an endomorphism, choose g in G, and set

    S_n=sum_(j=0)^(n-1) X_j T^j g.

No injectivity of T is assumed.
Write H_1(n), H_2(n), H_infinity(n) and H_0(n) for Shannon, collision, min- and support entropy.
Their normalized limits h_1,h_2,h_infinity,h_0 exist and equal their infima over n>=1.

Indeed, S_(n+k) has the distribution of S_n+T^n S'_k with independent blocks.
Shannon entropy is subadditive under independent summation and cannot increase under a deterministic map.
Support sizes are submultiplicative.
For min-entropy, choose maximal atoms of each block; their simultaneous event contributes at least the product mass to one atom of the sum.
For collision entropy use independent copies of both blocks: simultaneous blockwise equality implies equality of the sums, so

    Col(S_(n+k))>=Col(S_n)Col(S_k).

The map T^n cannot decrease the second factor's collision probability.
These facts prove subadditivity of all four nonnegative entropy sequences.
Fekete's lemma gives the stated limits; H_q(n)<=n log2 makes them finite.

Apply (1) at each n and pass to the limits:

    h_1/2<=h_infinity<=h_2<=h_1<=h_0.                    (6)

More strongly, the infimum characterization gives H_1(n)>=n h_1, so for every n>=1,

    max_x P(S_n=x)<=exp(-n h_1/2),
    Col(S_n)<=exp(-n h_1/2).                             (7)

There is no unspecified initial time or multiplicative constant in (7).
The comparison uses a Shannon rate that has already been established for that flow.
It does not supply a positive rate when h_1 is unknown or zero.

For an algebraic unit alpha, G may be Z[alpha], T multiplication by alpha and g=1.
More generally, the finite complex-weight version follows directly from Li's original theorem: the finitely generated additive subgroup of any finite complex list embeds additively into R by sending a free integer basis to Q-linearly independent real numbers.
For the algebraic flow one fixed injective Q-linear map on Q(alpha) works for every n.
This preserves all binary fibers, although it need not preserve multiplication or absolute values.
The group proof above renders this auxiliary embedding unnecessary.

<a id="mahler-to-binary-min-entropy"></a>
## The retained BV20 estimate supplies collision and min-entropy

Let alpha be a nontorsion algebraic unit, let P be its monic irreducible polynomial and put m=log M(P)>0.
The retained [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-random-walk-entropy) accepts an absolute unspecified c_B>0 such that, after converting the source's base-two convention to natural logarithms,

    h_1(alpha)>=c_B min(log2,m).                          (8)

The source uses fair signs {-1,1}.
Their sum is 2S_n-sum_(j<n) alpha^j, an injective affine image of the {0,1} sum in characteristic zero, so all finite entropies and their rates agree.
Multiplying the source inequality by log2 gives exactly (8), with the same dimensionless c_B.
No numerical value such as 0.44 is adopted.

Combining (6)--(8), for every such alpha and every n>=1,

    h_infinity(alpha)>=c_B min(log2,m)/2,
    h_2(alpha)>=c_B min(log2,m)/2,
    max_x P(S_n=x), Col(S_n)
          <=exp[-c_B n min(log2,m)/2].                   (9)

These constants are uniform in degree, house and the number of expanding conjugates.
All-power degree preservation, a single expanding embedding and a positive-volume self-affine set are unnecessary.
The usual support bound from the same retained source gives h_0<=min(log2,m), consistently with (6).

The conclusion supplies the previously missing valid Shannon-to-collision comparison for this exact fair binary class.
It does not prove Lehmer's conjecture: when m tends to zero, the right side of the rate lower bound tends to zero with m.
An input-independent positive min-entropy or collision-rate gap would still imply a Mahler gap through h_infinity<=h_2<=h_0<=m.
Conversely, a Mahler gap implies both rate gaps by (9).

In particular, a degree-uniform collision bound proportional to m is already available by combining these accepted inputs.
Reproving only that target through Sidon, dissociation or linear-order moment estimates would not strengthen the present result.
Any next moment mechanism must supply additional information, such as a positive rate independent of m or a genuinely stronger arithmetic restriction.
L G0086's necessary 1/m-scale moment cost remains consistent with (9); the present argument does not infer its high-moment hypothesis.

<a id="fairness-and-support-boundaries"></a>
## Boundaries

Uniform comparison fails for unrestricted laws and for a bound uniform over all Bernoulli biases.
A single Bernoulli(p) has H_1~p log(1/p) and H_infinity~p as p tends to zero.
This is a boundary of the proposed generalization, not a counterexample to (1).
Conjecture1.1 in Li26 concerns H_0<=2H_infinity and is not used.
The present positive-order result does not assert H_0=log M, H_1=log M, equality of different entropy orders, or positivity of the volume/interior of an attractor.

The initial bounded source search also located general Sidon/subgaussian characterizations, but none was selected or used as an arithmetic input.
Their bare formulation would leave the size of the Sidon/subgaussian constant to be proved.
L G0086 already supplies an elementary house-dependent bound and a necessary Mahler-dependent cost.
Once (9) was found, the source search stopped after this one selected article rather than treating a general harmonic-analysis characterization as a new degree-uniform arithmetic estimate.

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C280](../claims/Yin_C_G0280_v1.md#argument), with its actual selected assessment.
The [current whole finding](../audits/reviews/Yin_R_G0535_v1.md#current-fair-group-entropy-finding) is self-reviewed.
The [complete original checking account and precise findings](../audits/reviews/Yin_R_G0535_v1.md#historical-fair-group-author-finding) retain their original2026-10-07 inputs, actual contributions, coverage and limitations.
Original independent or collaborator wording does not establish unrecorded initial context or bind a later C to an old finding.
