---
author: Yin
---

# Degree-lowering prime powers and the exact finite-capture counterexample reduction

This retains the complete original2026-10-06 [L14](../ledger/Yin_L_G0014_v1.md) local proof and consequences, with Mig78 attribution and original source-proof limits.

## Statement

Let alpha be any nonzero nontorsion algebraic integer of degree d and p a prime with deg(alpha^p)<d.
Put beta=alpha^p, K=Q(beta), e=[Q(alpha):K], and b=norm_(Q(alpha)/K)(alpha), so 2<=e<=p and b^p=beta^e.
If e=p, beta has degree d/p and m(beta)=m(alpha)>0.
If e<p, choose integers u,v with eu+pv=1 and put gamma=b^u beta^v.
Then gamma=alpha times a p-th root of unity, Q(gamma)=K, gamma is integral nonzero nontorsion, and m(gamma)=m(alpha)/e>0.
Both branches preserve being a unit.
Repeated actual reductions terminate in strictly lower positive degrees at an endpoint satisfying deg(gamma^q)=deg(gamma) for every prime q.
The infimum of positive logarithmic Mahler measures is unchanged by restricting to these prime-stable endpoints, also within units; every hypothetical vanishing positive sequence has a termwise reduced vanishing sequence with a distinct subsequence.
Once a unit input has m<log(theta0), where theta0>1 solves t^3−t−1=0, the endpoint is reciprocal by the accepted nonreciprocal gap, without asserting reciprocity is twist invariant.
If a finite-entropy rational flow fails finite capture, this construction and a distinct summable subsequence give another such flow with prime-stable positive unit factors.
This reduces counterexample existence, neither constructing a counterexample nor preserving the original flow or its numerical entropy.
The endpoint condition is only the displayed prime condition; no automatic all-composite-power stability, finite test of every prime, or preserved discriminant is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:55 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nonzero nontorsion algebraic integer and every degree-lowering prime, both relative-degree branches, units, exact infima and conditional sequence/counterexample-existence conclusions with the precise reciprocity threshold. |
| argument | [Argument](#argument) | Full relative norm/Bezout derivation, field equality, integrality, height and measure factors, finite descent and summable distinct-primary reconstruction, with prime-only endpoint and non-preserved entropy/discriminant limits. |
| dependency | [Height and Kronecker conventions](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Absolute logarithmic height, exact degree factor and positive measure for nonzero nontorsion algebraic integers. |
| dependency | [Known nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Accepted theta0-root gap only, with m<log(theta0); no twist-invariance of reciprocity asserted. |
| dependency | [Rational primary formula and capture](Yin_C_G0205_v1.md#capture-equivalence) | Exact rational simple-primary/direct-sum criterion, including summable distinct positive factors; not a general abelian decomposition. |
| dependency | [Mig78 statement attribution](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | The original degree-reduction Lemma2 statement was read; its full original proof was not audited and the local norm/Bezout proof here supplies the argument. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:59 |
| status | proved |
| reason | Adopt the exact complete retained theorem after actual whole current self-review with resolved inputs; every restricted-family, source and failed-generalization boundary remains. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every nonzero nontorsion algebraic integer and every degree-lowering prime, both relative-degree branches, units, exact infima and conditional sequence/counterexample-existence conclusions with the precise reciprocity threshold. |
| argument | [Argument](#argument) | Full relative norm/Bezout derivation, field equality, integrality, height and measure factors, finite descent and summable distinct-primary reconstruction, with prime-only endpoint and non-preserved entropy/discriminant limits. |
| dependency | [Height and Kronecker conventions](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Absolute logarithmic height, exact degree factor and positive measure for nonzero nontorsion algebraic integers. |
| dependency | [Known nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Accepted theta0-root gap only, with m<log(theta0); no twist-invariance of reciprocity asserted. |
| dependency | [Rational primary formula and capture](Yin_C_G0205_v1.md#capture-equivalence) | Exact rational simple-primary/direct-sum criterion, including summable distinct positive factors; not a general abelian decomposition. |
| dependency | [Mig78 statement attribution](../audits/literature/Mig78/Yin_U001.md#mig78-u001) | The original degree-reduction Lemma2 statement was read; its full original proof was not audited and the local norm/Bezout proof here supplies the argument. |
| review | [Complete current finding](../audits/reviews/Yin_R_G0509_v1.md#current-degree-reduction-finding) | Actual whole exact Statement/Argument verification; constructor self-review, without a new isolated or original-source inspection claim. |

## Complete retained argument

<a id="argument"></a>

<a id="power-degree-reduction"></a>
## Direct norm proof, including positive entropy

Let alpha be a nonzero algebraic integer which is not a root of unity, let p be prime, and suppose deg(alpha^p)<deg(alpha)=d.
Set L=Q(alpha), beta=alpha^p, K=Q(beta), and e=[L:K].
Since alpha satisfies t^p-beta over K, 2<=e<=p.
Let b=N_(L/K)(alpha).
Then b is nonzero and

\[
b^p=N_{L/K}(\alpha^p)=\beta^e. \tag{1}
\]

If e=p, keep beta.
Its degree is d/p, it is a nonzero non-torsion algebraic integer, and the height identity h(beta)=p h(alpha) gives m(beta)=m(alpha).

If e<p, choose integers u,v with eu+pv=1 and put gamma=b^u beta^v in K.
Equation (1) gives gamma^p=beta=alpha^p, so gamma=alpha eta for a p-th root of unity eta.
Thus gamma is integral even if the displayed norm formula uses negative exponents.
It is nonzero and is not a root of unity.
Moreover Q(gamma)=K: containment in K is built in, while gamma^p=beta generates K.
Therefore

\[
\deg\gamma=d/e<d,\qquad h(\gamma)=h(\alpha),\qquad
0<m(\gamma)=m(\alpha)/e\le m(\alpha). \tag{2}
\]

The equality of heights follows place by place because roots of unity have absolute value one.
If alpha is a unit, both the e=p replacement and gamma remain units.
Reciprocity is not asserted to survive an arbitrary root-of-unity twist.

For comparison with the source's conjugate-product construction, zeta=b/alpha^e is a p-th root of unity lying in L; gamma=alpha zeta^u, and L=K(zeta).
No additional norm argument for eliminating zeta is needed.

## Reduction of the gap and nonattainment questions

Call an algebraic number power-degree-stable here if deg(alpha^p)=deg(alpha) for every prime p.
This phrase is only local shorthand for that explicit condition.
Whenever it fails, the preceding construction strictly lowers the positive integer degree while keeping 0<m(new)<=m(old).
Repetition therefore terminates after finitely many actual reductions at a power-degree-stable nonzero non-torsion algebraic integer.
This is an existence reduction, not a finite algorithm for verifying the universal prime condition.

Consequently the infimum of positive logarithmic Mahler measures m over nonzero non-torsion algebraic integers is unchanged on restriction to this class.
The same conclusion holds within algebraic units.
Any hypothetical sequence m(alpha_n)>0 tending to zero can be replaced termwise by such a sequence; positivity is preserved, and a distinct subsequence exists because finitely many fixed positive weights cannot tend to zero.

For a sufficiently small-measure unit sequence, reciprocity can also be retained at the endpoint using the already accepted nonreciprocal gap in [Smy08-U002](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number): write theta_0>1 for the real root of t^3-t-1.
Once the original logarithmic measure satisfies m(alpha)<log(theta_0), equivalently M(alpha)<theta_0, a replacement of no larger measure cannot be nonreciprocal.
This uses the known arithmetic gap for that restricted class, not invariance of reciprocity under the twist.

The [rational primary criterion](Yin_C_G0205_v1.md#capture-equivalence) makes this relevant to the primary route.
Given hypothetical failed finite capture with summable distinct positive irreducible weights, all but finitely many positive components are monic units (nonmonic or nonunit weights are at least log2).
Replacing the remaining parameters by the reduced ones gives positive weights bounded by the original summable weights.
Extract a distinct subsequence and take the direct sum of the corresponding simple rational primary flows.
This new finite-positive-entropy flow still fails finite capture by C205.
Its numerical entropy need not equal that of the original flow.
The statement reduces the existence of a counterexample; it does not preserve the original flow or assert that one exists.
