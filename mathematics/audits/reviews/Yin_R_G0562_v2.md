---
author: Yin
---

# Review of the prescribed-constant inverse for a fixed Salem polynomial

At 2026-11-16T12:52 UTC a separate reviewer for Yin checked the statement, all three proof sections and the cited interfaces in C345v2.
The reviewer did not develop the inverse construction and received its fixed text and the review scope without the proposing agent's development discussion, explanations or prior findings on this claim.
The reviewer previously contributed to the forward result in L462v32.
Its application here was checked against the fixed lemma, whose [own independent review](Yin_R_G1114_v30.md#pisot-coefficient-review) covers the underlying forward argument.

<a id="prescribed-constant-inverse-review"></a>
## Finding on the inverse construction and its optimal excess

The proof gives a strict Pisot minimal polynomial for every sufficiently large integer \(q\) at each fixed Salem polynomial \(P\).
For \(T=\sigma+\sigma^{-1}\) the minimum excess is \(T-2+O_P(1/q)\).
Both the threshold and the error constant can depend on \(P\).

The trace factorization gives \(P=(z^2-Tz+1)V\), where \(V\) is monic reciprocal of degree \(2m-2\) and has \(2m-2\) simple circular roots, none at \(1\) or \(-1\).
Multiplication of the quadratic reciprocal sum by \(V\) gives precisely \((z+1)P\).
The powers of \(z\) in \(z^{m-1}H'(z+z^{-1})\) range from \(1\) to \(2m-3\) and are symmetric about \(m-1\), including the case \(m=2\).
Multiplication by \(1-z\) gives the required antisymmetry about \((2m-1)/2\) and fixes the constant and leading coefficient of the perturbed polynomial.
The prescribed pair sums are integers, and no pair consists of a single index since \(2m-1\) is odd.
Rounding one entry in each free pair changes each entry by at most \(1/2\) in absolute value.
The endpoint pair is already integral, so this gives a uniform circle bound \(m\) for the error and preserves \(f_q(0)=q\).

At a node \(e^{it}\) with \(0<t<\pi\), the tangent factor from differentiating \(V\) is \(2i\sin(t)e^{i(m-1)t}H'(2\cos t)\).
The component of \(LE\) in the real coordinate \(C(e^{it})/(i e^{i(m-1/2)t})\) is \(-2L\sin(t/2)H'(2\cos t)\).
A single \(L\) makes each of these finitely many nonzero components strictly larger than the rounding bound in magnitude.
The real part of \(e^{-it/2}p_q(e^{it})\) equals \(\cos(3t/2)-(T-1)\cos(t/2)=(2\cos t-T)\cos(t/2)<0\), independently of \(q\).
The inverse of this complex number also has negative real part.
These two strict signs give a negative derivative of the log modulus at every node and its conjugate.
The quadratic factor starts with one interior root and one exterior root by its signs at \(0,1,q\) and its positive leading coefficient.
Along the perturbed path a circular root must also annihilate \(D\).
At the nodes of \(V\) the value is \(sC(e^{it})\ne0\) for \(s>0\), while at \(-1\) the initial value \((2q+T)V(-1)\) dominates the bounded perturbation uniformly in \(s\).
This accounts for the entire possible crossing set.
The absence of a boundary zero for \(0<s\le1\) and monicity preserve the root count there, and \(f_q(1)=P(1)<0\) locates the unique exterior root on the positive real axis.
Every nonconstant monic integer factor missing this root would have nonzero integral constant of absolute value less than one.
Thus \(f_q\) is irreducible and all its other conjugates are strictly inside.

The fixed endpoint sum and the bound \(2m-1\) on the absolute sum of the interior roots give \(\theta_q=q+O_P(1)\).
Here the coefficients of \(C=LE+U\) are bounded uniformly in \(q\) for fixed \(P\), and \(\deg C\le\deg V\).
Since \(V\) is fixed and monic, \(C(\theta_q)/V(\theta_q)=O_P(1)\).
Dividing the quadratic equation with this bounded error by \(\theta_q\) gives the asserted \(O_P(1/q)\), using \(q/\theta_q=1+O_P(1/q)\).
For every competing representation at the same \(q\), the sign in Boyd's Lemma 5 is positive and the sole exterior root of the fixed associate is \(\sigma\).
Its inequality gives the lower bound \((T-2)q(q-1)/(q+1)^2=T-2+O_P(1/q)\).
Among competitors up to the constructed \(\theta_q\), the degree and Mahler measure bound each integer coefficient, proving attainment of the minimum.
For a sequence of varying Salem polynomials the threshold and error can be met successively while enforcing any prescribed lower bounds on the \(q\)'s.
Conversely the positive-constant forward lemma applies to the stated strict Pisot inputs and rules out quadratic outputs eventually when their exterior roots approach one.
The equivalence concerns existence of near-one Salem numbers and gives no conclusion about existence of such numbers or about other reciprocal units.

The McKee–Smyth source unit reports the older plus representation with cofactor \(z^2+1\) and a Pisot polynomial in the source's convention.
This supplies the historical comparison without supplying the prescribed constant or the new estimate.
The Boyd bound was checked at the statement and sign interface recorded in the source unit.
The inspection found no correction needed and did not re-audit either external proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Fixed-output statement](../../claims/Yin_C_G0345_v2.md#statement) | Every large positive integer constant, fixed degree and cofactor, optimal excess, both implications and the fixed-output dependence. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Rounding](../../claims/Yin_C_G0345_v2.md#rounding) | Trace factor, real comparison seed, reversal indices, integral endpoints and the uniform paired rounding error. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Root motion](../../claims/Yin_C_G0345_v2.md#inward) | Simultaneous inward derivative, every possible circle crossing, positivity of the exterior root and irreducibility. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Optimum](../../claims/Yin_C_G0345_v2.md#optimum) | Uniform error in the constructed root, Boyd bound for every competitor, minimum and choice for varying outputs. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Boyd source unit](../literature/Boy78/Yin_U001.md#boy78-u001) | Positive-sign delay-one inequality at the fixed exterior root and positive constant. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Positive delay-one return](../../ledger/Yin_L_G0462_v32.md#boyd-return) | Applicability of the previously established forward lemma, including eventual exclusion of reciprocal quadratics. |
| [Prescribed-constant inverse](#prescribed-constant-inverse-review) | [Earlier Pisot representation](../literature/MS12b/Yin_U001.md#ms12b-u001) | Historical comparison with Boyd's infinite plus family at cofactor \(z^2+1\). |
