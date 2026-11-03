---
author: Yin
---

# Degree-lowering powers and the finite-capture counterexample class

Date: 2026-10-06.
Coordinating AI agent for Yin under [T G0001](../tasks/Yin_T_G0001_v1.md#contract).
This is a known source reduction with a direct norm proof and its stated consequences for the current entropy route.
It is not a Lehmer resolution.

## Reuse, source attribution and scope

The retained Mig78 Lemma 2, printed 39-04 / PDF p.5, states that a prime power lowering algebraic degree permits replacement by a number of smaller degree and no larger Mahler measure.
Its statement was read on the rendered page during the preceding Proposition 5 source lookup; the original proof continues onto printed 39-05 and was not audited in full.
The direct norm proof below is separately complete.
It uses the degree/absolute-height normalization already retained in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), and is consistent with the fixed-seed degree accounting in [L G0003](Yin_L_G0003_v1.md).
No new source was acquired, and the reduction is not claimed novel.

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

The [rational primary criterion](Yin_L_G0002_v1.md#capture-equivalence) makes this relevant to the primary route.
Given hypothetical failed finite capture with summable distinct positive irreducible weights, all but finitely many positive components are monic units (nonmonic or nonunit weights are at least log2).
Replacing the remaining parameters by the reduced ones gives positive weights bounded by the original summable weights.
Extract a distinct subsequence and take the direct sum of the corresponding simple rational primary flows.
This new finite-positive-entropy flow still fails finite capture by L G0002.
Its numerical entropy need not equal that of the original flow.
The statement reduces the existence of a counterexample; it does not preserve the original flow or assert that one exists.

## Review and continuation boundary

The original norm/consequence contributor checks and the separate consequence finding are retained at [R509](../audits/reviews/Yin_R_G0509_v1.md#original-degree-contributor-checks), with their actual scopes and day precision.
The complete current proof is [C218](../claims/Yin_C_G0218_v1.md#argument), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0509_v1.md#current-degree-reduction-finding); no old isolation fact is inferred.

This reduction makes the all-prime degree condition in the accepted Mat96 statement a potentially legitimate restriction when studying gap failure.
The degree/discriminant estimate and any implication from it still require a separate explicit application; no uniform bound on that ratio is established here.
The full Lehmer objective remains unresolved.
