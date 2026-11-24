---
author: Yin
---

# Six-term double contacts under a power-field drop or a reflection of the support

<a id="statement"></a>
## Two coefficient-independent gaps

Let \(G(X)=\sum_{i=1}^6 c_iX^{a_i}\) be a rational Laurent polynomial with six distinct occupied exponents.
Suppose that a nontorsion algebraic unit \(\alpha\) has reciprocal minimal polynomial and \(G\) has a double zero at \(\alpha\), where “double” includes higher multiplicity.
Put \(g=\gcd_{i,j}|a_i-a_j|\), \(b_i=(a_i-\min_j a_j)/g\), \(\beta=\alpha^g\), and \(H_{\rm ab}=\mathbb Q^{\rm ab}\).
Write \(m(\alpha)=[\mathbb Q(\alpha):\mathbb Q]h(\alpha)\) for total logarithmic Mahler measure.

If \(\mathbb Q(\beta^k)\subsetneq\mathbb Q(\beta)\) for some positive integer \(k\), then \(m(\alpha)\) is bounded below by an absolute positive constant.
More precisely, if distinct conjugates of \(\beta\) have quotient \(\zeta\) of finite order \(q\), then the six \(b_i\) are pairwise distinct modulo \(q\).
Let \(e_i=\gcd_{j,l\ne i}|b_j-b_l|\) be the gcd after deleting term \(i\).
Then
\[
 [H_{\rm ab}(\beta^{e_i}):H_{\rm ab}]\le6\quad(1\le i\le6),
 \qquad [H_{\rm ab}(\beta):H_{\rm ab}]\le36 .
\]
In particular \(q\ge6\).
Along a sequence with \(m(\alpha)\to0\), every positive power of \(\beta\) eventually generates \(\mathbb Q(\beta)\), simultaneously for all powers.
For primitive support \(g=1\) this assertion concerns the original root \(\alpha\).

Suppose instead that the support is invariant under a reflection \(a\mapsto L-a\) and that \(X^LG(X^{-1})\) is not proportional to \(G\).
Then \([\mathbb Q(\beta^{e_i}):\mathbb Q]\le6\) for each deletion,
\([\mathbb Q(\beta):\mathbb Q]\le18\), and \(m(\alpha)\ge(\log2)/24\).
For a Salem root \(\alpha>1\), this gives \([\mathbb Q(\alpha):\mathbb Q]\le6\).
In an ordinary graph \(G=U(X^p)+XV(X^p)\) with both rows nonzero and \(p>2\), the condition \(UU^\iota-VV^\iota\ne0\), where \(\iota(Y)=Y^{-1}\), ensures nonproportionality whenever the support is invariant under reflection.
For coprime integer rows the [individual height bound](Yin_C_G0345_v408.md#lower) then gives \(\max(\|U\|_1,\|V\|_1)\ge2^{p/24}\) in the reflection case.
The two asserted gaps impose no bound on coefficient size.

<a id="cancellation"></a>
## Removing one term over a coefficient field

After translating and dividing the exponents, the polynomial \(f(X)=\sum_i c_iX^{b_i}\) has double zeros at every conjugate of \(\beta\) and its inverse.
Indeed \(G(X)=X^{\min a_j}f(X^g)\), the power substitution is unramified at \(\alpha\), and inversion sends \(\alpha\) to a conjugate.
The six normalized exponents have gcd of differences one.
For any two distinct indices \(i,j\) the integers \(e_i,e_j\) are coprime.
Any common prime divisor would make each of the two surviving support lists constant modulo that prime, and a shared exponent makes their two residues agree.
Their union is the whole support.

We use the [five-term interpolation argument](Yin_C_G0903_v2.md#interpolation) over a coefficient field \(K\subseteq\overline{\mathbb Q}\).
If a polynomial with \(s\le5\) nonzero coefficients \(d_j\in K\) has double zeros at \(z,z^{-1}\), and its exponent differences have gcd \(e\), then \([K(z^e):K]\le6\).
To see this, translate and normalize its exponents to integers \(n_j\) with difference gcd one, put \(y=z^e\), and let \(D_j=\prod_{l\ne j}(n_j-n_l)\).
The two Euler equations for each sign put the vectors \((d_jy^{\pm n_j})_j\) in the kernel of the two moment rows \(1,n_j\).
Vandermonde excludes \(s\le2\).
Lagrange interpolation identifies these vectors as \((Q_\pm(n_j)/D_j)_j\) with \(\deg Q_\pm\le s-3\).
The product \(Q_+Q_-\) takes the values \((d_jD_j)^2\in K\), and its degree \(2(s-3)\) or less is strictly smaller than \(s\).
It belongs to \(K[t]\).
The monic normalization of \(Q_+\) has at most \(\binom{2(s-3)}{s-3}\le6\) conjugates over \(K\), counting monic divisors of the product of the given degree.
Ratios of its nonzero values at the nodes recover every \(y^{n_j-n_l}\) over its coefficient field, since \(d_jD_j,d_lD_l\in K^\times\).
These powers generate \(K(y)\) by Bézout's identity.
We also use the [four-term exclusion](Yin_C_G0903_v2.md#real), which applies to real Laurent polynomials with double zeros at \(z,z^{-1}\) and \(|z|\ne1\).

<a id="torsion"></a>
## Rotating two conjugate roots

A degree drop on powering is equivalent by separability to two distinct conjugates \(x,\zeta x\) of \(\beta\) having torsion quotient.
By Kronecker's theorem some conjugate of this nontorsion unit lies off the circle.
Applying a Galois automorphism to the pair, choose \(|x|\ne1\), preserving the order \(q\) of its quotient.
Fix a node \(b_i\), choose a root of unity \(\omega\) with \(\omega^2=\zeta\), and form
\[
 B_i(Y)=\frac{f(\omega Y)-\zeta^{b_i} f(Y/\omega)}
                  {{\rm i}\,\omega^{b_i}} .
\]
Its coefficient at \(b_j\) is \(c_j(\omega^{b_j-b_i}-\omega^{-(b_j-b_i)})/{\rm i}\), which is real and belongs to \(H_{\rm ab}\).
It vanishes exactly when \(b_j\equiv b_i\bmod q\).
At least one coefficient survives because the normalized differences generate \(\mathbb Z\) and \(q>1\).
At \(Y=\omega x\) the arguments are \(\zeta x,x\), and at \(Y=(\omega x)^{-1}\) they are \(x^{-1},(\zeta x)^{-1}\).
Each summand at each point has a double zero.
The four-term exclusion forces at least five coefficients to survive, so only the selected \(b_i\) is removed.
Applying this at every node proves pairwise distinctness modulo \(q\).
The interpolation bound gives \([H_{\rm ab}(x^{e_i}):H_{\rm ab}]\le6\), since \(\omega\in H_{\rm ab}\).
Normality of \(H_{\rm ab}/\mathbb Q\) gives the same degree for \(\beta^{e_i}\).
Any two deletion gcds are coprime, so the compositum of the corresponding power fields over \(H_{\rm ab}\) contains \(\beta\) and has degree at most \(36\).

<a id="measure"></a>
## The gap for the original root

Take \(j=g e_i\), \(K_0=\mathbb Q(\alpha^j)\), \(K_1=\mathbb Q(\alpha)\), \(l=[K_1:K_0]\) and \(u=N_{K_1/K_0}(\alpha)\).
All \(l\) conjugates in this norm have the same \(j\)-th power, so \(u^j=\alpha^{jl}\), \(u\) is a nontorsion unit and \(h(u)=l h(\alpha)\).
Consequently \(m(\alpha)=[K_0:\mathbb Q]h(u)\).
The degree \(D=[H_{\rm ab}(u):H_{\rm ab}]\) is at most \([H_{\rm ab}(\alpha^j):H_{\rm ab}]\le6\), and also at most \([K_0:\mathbb Q]\).
The [rational-base consequence of Amoroso and Delsinne, Theorem 1.3](../audits/literature/AD07/Yin_U001.md#rational-base) gives
\[
 m(\alpha)\ge D h(u)\ge
 c_0\min_{1\le v\le6,\ v\in\mathbb Z}
        \frac{(\log\log(5v))^3}{(\log(2v))^4}>0 .
\]
Here \(c_0>0\) is absolute.
For its application to \(H_{\rm ab}\), take a finite abelian field containing \(\mathbb Q(\sqrt5)\) and all coefficients of the minimal polynomial of \(u\) over \(H_{\rm ab}\).
Its relative degree for \(u\) is still \(D\).
Use the unconditional theorem with fixed base \(\mathbb Q(\sqrt5)\), whose discriminant is \(5\), and this finite abelian extension.
This uses the source at theorem-statement scope with an unspecified absolute prefactor. [ESI preprint, Theorem 1.3](https://www.esi.ac.at/preprints/esi1848.pdf)

<a id="reflection"></a>
## Cancellation with the reflected polynomial

Write \(N=\max_i b_i\) and \(f^*(X)=X^Nf(X^{-1})\).
Reflection preserves the normalized support, and both \(f\) and \(f^*\) have double zeros at every conjugate of \(\beta\) and its inverse.
For each \(i\) choose the rational scalar \(s_i\) cancelling coefficient \(b_i\) in \(f-s_if^*\).
This polynomial is nonzero by nonproportionality and has at least five terms by the four-term exclusion applied at an off-circle conjugate.
It therefore deletes just the chosen index.
Interpolation over \(\mathbb Q\) gives \([\mathbb Q(\beta^{e_i}):\mathbb Q]\le6\), and the [five-term measure bound](Yin_C_G0903_v2.md#statement) applies to \(\alpha\) by using the same cancelled polynomial at \(X^g\).
For distinct indices \(i,j\), the two power fields generate \(\mathbb Q(\beta)\) and intersect in a field containing \(\beta^{e_i e_j}\).
This power has degree at least two since it is a nontorsion unit.
The compositum bound thus gives \([\mathbb Q(\beta):\mathbb Q]\le6^2/2=18\).
For a Salem root its unique conjugate of modulus greater than one ensures all its nonzero powers generate its field, so any one deletion gives the sharper degree bound six.

Finally, the support of the two-row graph occupies exactly \(0,1\bmod p\).
A reflection preserving it must exchange the two residues when \(p>2\), since fixing both would require \(2\equiv0\bmod p\).
Thus \(L=1+ph\).
Proportionality of \(G\) and \(X^LG(X^{-1})\) would give proportionality constant \(\pm1\) by applying reflection twice, and \(U(Y)=\pm Y^hV(Y^{-1})\).
This would make their reflected determinant zero.

## Assessment history

### Decision six-term-power-and-reflection

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:35 |
| status | proved |
| reason | The two cancellation arguments control the original total measure at their respective field and support hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Six-term power drops and reflection-invariant supports with a reciprocal double contact. |
| argument | [cancellation](#cancellation) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [torsion](#torsion) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [measure](#measure) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [reflection](#reflection) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0903_v2.md#interpolation) | Interpolation after cancellation controls the relative power degree. |
| dependency | [Input](Yin_C_G0903_v2.md#real) | Four terms cannot retain a double off-circle inverse pair after the indicated rotation. |
| dependency | [Relative height bound](../audits/literature/AD07/Yin_U001.md#ad07-u001) | The relative height inequality is applied at bounded relative degree after norm descent. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1051.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-six-term-power-and-reflection)
