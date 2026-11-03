---
author: Yin
---

# Real digit support: a covering lower bound and its entropy boundary

Preserved exploration, 2026-10-06, coordinating AI agent for Yin, under [T G0001](../tasks/Yin_T_G0001_v1.md#contract) and primary [S G0001](../strategies/Yin_S_G0001.md).
This is a standard interval-covering diagnostic, not a claimed novel theorem or a solution of the remaining arithmetic gap.
The actual targeted findings have their responsible [R503 record](../audits/reviews/Yin_R_G0503_v1.md#original-separate-interval-finding); their present relationships follow the recorded context facts.
The complete precise statement and argument have their current home in [C210](../claims/Yin_C_G0210_v1.md#statement).

## Reuse and purpose

The [cyclic-alphabet calculation](Yin_L_G0003_v1.md) distinguishes total entropy from one finite alphabet; the [carry theorem](../claims/Yin_C_G0212_v1.md#collision-entropy-directions) distinguishes support growth from collision and Shannon rates.
[BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001) supplies the accepted support upper bound for algebraic units, including polynomial factors from unit-circle conjugates.
[GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) and [DGB16-U001](../audits/literature/DGB16/Yin_U001.md#pure-essential-hull) supply total entropy on the integral cyclic flow.
Their existing external-proof inspection limits are unchanged.

The question is whether neutral conjugates already obstruct a lower bound for the number of distinct digit sums.
The following calculation shows why they do not do so for real Pisot/Salem parameters, while leaving weighted collisions separate.

A bounded search on 2026-10-06 for Mahler measure with distinct sums, binary digits, growth rate, and Pisot/Salem algebraic entropy did not verify a precise primary-source attribution for this combined formulation.
Hits concerned general entropy formulas, unrelated algebraic-geometric entropy, and nearby number-representation questions.
None is used as a premise.
The interval identity is proved below; a matching literature attribution remains a follow-up, and no novelty is inferred from the bounded search.

<a id="interval-covering"></a>
## All-length support estimate

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
## Exact local algebraic entropy in the one-expanding-conjugate case

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

## Consequence for the carry strategy

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

## Targeted review

The [original separate interval finding](../audits/reviews/Yin_R_G0503_v1.md#original-separate-interval-finding) and [coordinating unit-norm check](../audits/reviews/Yin_R_G0503_v1.md#original-coordinating-interval-check) retain their actual 2026-10-06 coverage and limitations.
The former has unknown initial inherited context, while the proposing coordinator's check is self-review.
The [complete current theorem](../claims/Yin_C_G0210_v1.md#statement) and its [actual current self-review](../audits/reviews/Yin_R_G0502_v1.md#real-support-current-finding) preserve the distinction between support, total entropy and random-digit distributions.
