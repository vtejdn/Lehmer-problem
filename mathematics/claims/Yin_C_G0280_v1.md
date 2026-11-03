---
author: Yin
---

# Complete fair binary entropy comparison in arbitrary abelian groups

This retains the entire original2026-10-07 [L89 argument](../ledger/Yin_L_G0089_v1.md).
Every hypothesis, complete derivation, exact cost and source/probability/uniformity boundary is retained.
No source or computation is newly executed and no Task is resumed.

## Statement

Let G be any abelian group and let S=sum_(i=1)^n X_i g_i for arbitrary g_i in G and independent fair Bernoulli{0,1}variables.
Zero/repeated elements, torsion including2-torsion, uncountable groups and no topology are permitted.
All laws have finite support and natural logarithms are used.
Then

    H1(S)<=H_(1/2)(S)<=2H_infinity(S)<=2H2(S).

The full largest-fiber/XOR proof below handles noninjectivity of doubling by the concave square-root pushforward inequality, rather than asserting an affine injection in a group with2-torsion.
Only the original real-weight result is attributed to Li26; the arbitrary-group extension is the retained local argument.

For any endomorphism T of G and g in G, S_n=sum_(j<n)X_j T^j g has normalized Shannon/collision/min/support entropy limits h1,h2,h_infinity,h0, all equal to the respective infima and without an injectivity assumption on T.
They satisfy

    h1/2<=h_infinity<=h2<=h1<=h0.

For every n>=1, max_x P(S_n=x) and Col(S_n) are both at most exp(-n h1/2), with no initial-time loss or prefactor.
This supplies no positive rate when h1 is unknown or zero.

For a nontorsion algebraic unit alpha with monic irreducible P and m=log M(P)>0, the accepted symbolic BV20 constant c_B>0 in natural units gives h1>=c_B min(log2,m).
The fair-sign and fair-bit laws have identical fibers by their characteristic-zero affine bijection.
Thus

    h_infinity,h2>=c_B min(log2,m)/2,
    max p_n,Col_binary(n)<=exp[-(c_B/2)n min(log2,m)]
    for every n>=1.

The constants are uniform in degree/house/expanding multiplicity, with no value0.44 adopted and no all-power degree, one-expanding-place or attractor-volume assumption.
The existing support upper bound is h0<=min(log2,m).
A common positive Mahler gap is equivalent to a common positive min/collision-rate gap through these implications, but none is proved.
The result is restricted to the independent fair binary class, fails uniformly over arbitrary Bernoulli biases, does not adopt the source H0<=2H_infinity conjecture and does not identify distinct entropy orders or infer an unproved high-moment estimate.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:13 |
| status | open |
| reason | Register the complete original mathematical conclusions and exact existing inputs; actual current whole review and adoption follow separately. No unsupported uniform gap or inherited independent review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire arbitrary-abelian fair-sum theorem, exact noninjective flow-rate/infimum and all-time comparisons, symbolic BV20 normalization and every degree/fairness/support/gap boundary. |
| argument | [Entire original proof](#argument) | Complete retained largest-fiber/XOR/likelihood/conditional-pushforward/Cauchy--Schwarz proof, all four subadditive entropy arguments, sign/log-base conversion, uniform Mahler-proportional consequence and biased-law limitations. |
| dependency | [Accepted BV20 entropy input](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Only the retained qualitative absolute symbolic Shannon/Mahler theorem and support upper bound, with its original analytic/source-proof limits; no numerical0.44 or new source audit. |
| support | [Inspected Li real-weight proof](../audits/literature/Li26/Yin_U001.md#li26-u001) | Original arXivv2 Theorem1.4 and complete Section2 at recorded proof depth, fair real weights only; the group/torsion extension is fully proved here and no H0 endpoint or Section3 is imported. |
| support | [Actual linear-moment cost](Yin_C_G0277_v1.md#linear-moment-necessary-cost) | Existing necessary moment/Mahler cost and elementary house bound remain compatible; no new common high-moment hypothesis follows from the comparison. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:21 |
| status | proved |
| reason | Adopt the complete original arbitrary-abelian fair-sum entropy comparison, noninjective flow-rate proof and exact every-n symbolic Mahler consequences after actual whole self-review. The real-source/local-torsion roles, full fairness and source-proof scopes remain; no biased-law, H0 endpoint, high-moment hypothesis or common gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire arbitrary-abelian fair-sum theorem, exact noninjective flow-rate/infimum and all-time comparisons, symbolic BV20 normalization and every degree/fairness/support/gap boundary. |
| argument | [Argument](#argument) | Complete retained largest-fiber/XOR/likelihood/conditional-pushforward/Cauchy--Schwarz proof, all four subadditive entropy arguments, sign/log-base conversion, uniform Mahler-proportional consequence and biased-law limitations. |
| dependency | [Dependency](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Only the retained qualitative absolute symbolic Shannon/Mahler theorem and support upper bound, with its original analytic/source-proof limits; no numerical0.44 or new source audit. |
| support | [Support](../audits/literature/Li26/Yin_U001.md#li26-u001) | Original arXivv2 Theorem1.4 and complete Section2 at recorded proof depth, fair real weights only; the group/torsion extension is fully proved here and no H0 endpoint or Section3 is imported. |
| support | [Support](Yin_C_G0277_v1.md#linear-moment-necessary-cost) | Existing necessary moment/Mahler cost and elementary house bound remain compatible; no new common high-moment hypothesis follows from the comparison. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0535_v1.md#current-fair-group-entropy-finding) | Entire exact current statement, complete retained original argument and every selected interface, self-reviewed; old findings retain their actual fixed inputs and relationship scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="abelian-binary-entropy-comparison"></a>
### Finite-time comparison, including torsion

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
### Binary flows and finite-time bounds from their rates

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
### The retained BV20 estimate supplies collision and min-entropy

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
### Boundaries

Uniform comparison fails for unrestricted laws and for a bound uniform over all Bernoulli biases.
A single Bernoulli(p) has H_1~p log(1/p) and H_infinity~p as p tends to zero.
This is a boundary of the proposed generalization, not a counterexample to (1).
Conjecture1.1 in Li26 concerns H_0<=2H_infinity and is not used.
The present positive-order result does not assert H_0=log M, H_1=log M, equality of different entropy orders, or positivity of the volume/interior of an attractor.

The initial bounded source search also located general Sidon/subgaussian characterizations, but none was selected or used as an arithmetic input.
Their bare formulation would leave the size of the Sidon/subgaussian constant to be proved.
L G0086 already supplies an elementary house-dependent bound and a necessary Mahler-dependent cost.
Once (9) was found, the source search stopped after this one selected article rather than treating a general harmonic-analysis characterization as a new degree-uniform arithmetic estimate.
