---
author: Yin
---

# Binary real digit supports and exact one-expanding-conjugate entropy

This retains the complete original 2026-10-06 interval-covering and entropy argument in [L7](../ledger/Yin_L_G0007_v1.md).
It is a standard covering result and its precise accepted-source application, without a novelty, new literature or new research-execution claim.

## Statement

For every real beta with 1<beta<=2 and every integer n>=1, put

    X_n(beta)={sum_(j=0)^(n-1) b_j beta^j : b_j in {0,1}}.

A. |X_n(beta)|>=beta^n, and the limit of log|X_n(beta)|/n exists and is at least log beta.
For beta=2 equality holds at every finite length.
No algebraicity or integrality is required in A; the interval-covering argument applies only in the specified real range.

B. If beta is an algebraic integer in (1,2) and every other conjugate has modulus at most one, then beta is an algebraic unit, m(p_beta)=log beta and

    lim_(n->infinity) log|X_n(beta)|/n
    =H(mu_beta,{0,1})=log beta=m(p_beta)=h_alg(mu_beta on Z[beta]).

Here mu_beta is multiplication by beta and H uses positive finite-sum trajectories.
The upper estimate has the form |X_n(beta)|<=C_beta n^s beta^n, where s is the number of unit-circle conjugates and C_beta is input dependent.
This includes the specified Pisot and Salem parameters below 2.

C. For a general real algebraic unit beta in (1,2), the same inputs give only log beta<=H(mu_beta,{0,1})<=m(p_beta); a product over several expanding embeddings requires additional joint covering information.
None of A–C supplies a Shannon or order-two Renyi entropy equality, an upper collision-probability bound, a uniform reverse comparison among these rates or a uniform positive Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:20 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All A–C with the exact real range, every length, algebraic-integer/unit and one-expanding-conjugate hypotheses, source depths and distributional exclusions. |
| argument | [Argument](#argument) | Entire original interval iteration, length estimate, subadditive limit, unit-norm reduction and accepted packing/total-entropy squeeze, including the multiple-expansion and collision boundaries. |
| dependency | [BV20 packing interface](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Accepted upper bound C_beta n^s exp(n m(p_beta)) for the actual algebraic-unit digit supports, including unit-circle factors; original external-proof limits unchanged. |
| dependency | [GBV15 entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Existing rational characteristic-polynomial total-entropy formula, with primitive normalization; no new original-proof audit. |
| dependency | [DGB16 cyclic-flow interface](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Existing total entropy on the integral cyclic flow at the recorded rationalization scope; only the specified unit case is interpreted here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:26 |
| status | proved |
| reason | Adopt the actual current statement and complete retained argument with its resolved exact inputs and sufficient constructor self-review. Original targeted findings retain their own historical scopes; no new research execution, independent certification or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire real range/all lengths, exact one-expanding-conjugate unit and entropy interface, multiple-expansion bound and distributional limitations, checked as the actual registered theorem. |
| argument | [Argument](#argument) | Complete physically retained proof and all required local deductions, with the exact domains, source depths and limitations in the Statement. |
| dependency | [BV20 packing interface](../audits/literature/BV20/Yin_U001.md#bv20-u001) | Accepted upper bound C_beta n^s exp(n m(p_beta)) for the actual algebraic-unit digit supports, including unit-circle factors; original external-proof limits unchanged. |
| dependency | [GBV15 entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Existing rational characteristic-polynomial total-entropy formula, with primitive normalization; no new original-proof audit. |
| dependency | [DGB16 cyclic-flow interface](../audits/literature/DGB16/Yin_U001.md#dgb16-u001) | Existing total entropy on the integral cyclic flow at the recorded rationalization scope; only the specified unit case is interpreted here. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0502_v1.md#real-support-current-finding) | Entire real range/all lengths, exact one-expanding-conjugate unit and entropy interface, multiple-expansion bound and distributional limitations, checked as the actual registered theorem. |

## Argument

<a id="interval-covering"></a>
### All-length support estimate

For every real 1<beta<=2 define

\[
X_n(\beta)=\left\{\sum_{j=0}^{n-1}b_j\beta^j:b_j\in\{0,1\}\right\},
\qquad I=[0,1/(\beta-1)].
\]

The two intervals beta^{-1} I and beta^{-1}(1+I) cover I: they have the correct extreme endpoints, and they overlap exactly when beta<=2.
Iterating this equality gives

\[
I=\bigcup_{a\in\beta^{-n}X_n(\beta)}(a+\beta^{-n}I).
\]

Reversing the order of the n digits identifies the displayed prefix set with the usual powers beta^{-1},...,beta^{-n}.
Lebesgue length is subadditive even when the intervals overlap, so

\[
|I|\le |X_n(\beta)|\beta^{-n}|I|,
\qquad |X_n(\beta)|\ge\beta^n\quad(n\ge1). \tag{1}
\]

This requires no algebraicity or integrality.
It is an all-length lower bound justified by covering a fixed interval; it does not infer an asymptotic lower bound from one finite count.
Consequently the support rate satisfies

\[
\lim_{n\to\infty}\frac{\log|X_n(\beta)|}{n}\ge\log\beta.
\]

The limit exists by the usual subadditivity of digit-sum cardinalities.
At beta=2 equality holds at every length.
The argument does not apply to a nonreal parameter, and it fails as a covering identity for beta>2.

<a id="pisot-salem-attainment"></a>
### Exact local algebraic entropy in the one-expanding-conjugate case

Let beta be a real algebraic integer in (1,2), and suppose every other conjugate has modulus at most one.
Its nonzero norm has absolute value at most beta<2, hence is 1, so beta is an algebraic unit and its multiplicative Mahler measure is beta.
Let s count unit-circle conjugates.
The retained BV20 packing upper bound gives

\[
|X_n(\beta)|\le C_\beta n^s\beta^n.
\]

Together with (1) this proves

\[
H(\mu_\beta,\{0,1\})=\log\beta=m(p_\beta)
=h_{\rm alg}(\mu_\beta\mid\mathbb Z[\beta]). \tag{2}
\]

Thus the binary alphabet already attains total algebraic entropy in this domain, which includes Pisot and Salem parameters below 2.
Unit-circle conjugates contribute the allowed polynomial factor and do not invalidate the support-rate equality.
An algebraic integer has a nonzero norm here because beta>1 and the minimal polynomial is irreducible.

For a general real unit in (1,2) with more than one expanding conjugate, only log beta<=H(mu_beta,{0,1})<=m(p_beta) follows from these arguments.
The first bound measures the selected real embedding; it cannot automatically be replaced by a product over all expanding embeddings.
Such a product would require a jointly covering set of positive volume, not a separate interval cover in each coordinate.

### Consequence for the carry strategy

Equation (2) is a local-alphabet realization, not a claim about the entropy of fair random digits.
Overlapping prefix intervals may carry very unequal digit multiplicities.
There is no deduction here that the Shannon or order-2 Renyi rate equals log beta, and a finite support count cannot bound collision probability from above.
No uniform reverse comparison among those rates is inserted.

The lower bound log beta itself tends to zero as beta decreases to one.
The argument therefore does not separate possible Salem parameters from one and does not establish a Lehmer gap.
It identifies the actual additional obligation for weighted carry methods: control the distribution of collisions, or supply independent arithmetic information restricting beta.
Neutral conjugates alone are not an obstruction to the support estimate (2).

This scope distinction will be used when assessing finite-state projections with central fibers.
It preserves the full reciprocal-unit target, which also includes multiple expanding pairs and nonreal choices of parameter.
