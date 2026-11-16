---
author: Yin
---

# Review of the trace obstruction for positive-constant Pisot polynomials

On 2026-11-16T13:45 UTC an agent outside the development of [C345v7](../../claims/Yin_C_G0345_v7.md#statement) reviewed its complete statement and argument for Yin.
The assignment supplied the fixed target and scope without development discussion, author explanations or a proposed verdict.
I derived the trace and endpoint formulas and checked their consequences before consulting the earlier review of the torsion lemma.

<a id="trace-obstruction-review"></a>
## The first branch and the integral multiplier obstruction

The proof establishes the uniform positive excess on the first branch and the stated divergence of the infimum along every sequence with \(\delta\to0\), including sequences with varying \(j\).

### Descent to the trace variable

The product of the absolute values of the interior conjugates gives \(q/\theta<1\), and their real factors and conjugate pairs give \(f(1)<0\).
The [delay-one construction](../../ledger/Yin_L_G0462_v32.md#boyd-return) counts at most one exterior root with multiplicity by taking the limit of \(zf+tg\) as \(t\uparrow1\).
Since \(D(1)<0\), a positive exterior root exists and is simple, and reciprocity leaves exactly one interior root.
As in the [crossing argument](../../ledger/Yin_L_G0462_v34.md#crossings), the winding number of \(W=zf/g\) equals the total multiplicity of the remaining roots, so every preimage of \(-1\) on the circle is a simple upward crossing.
These two inputs apply to the whole associate, including its cyclotomic factors.

The identity \(g/D=1-zY\) gives \(Y(1/z)=z-z^2Y(z)\), so \(R=(1-z^2)Y-q+z\) is invariant.
The expansion \(Y=F/(1+zF)=q+(j-1)z+O(z^2)\), with \(F=f/g\), gives \(R=jz+O(z^2)\).
The inverse of \(x=z+z^{-1}\) at \(z=0\) solves \(z=x^{-1}(1+z^2)\) coefficient by coefficient over \(\mathbb Z\).
Hence the Laurent series for \(R\) at infinity is integral with initial term \(j/x\).
At \(z=1\) the denominator is nonzero, giving \(R(2)=1-q\).
At \(z=-1\) the possible pole of \(Y\) is simple and is canceled by \(1-z^2\).
Since \(x+2=(z+1)^2/z\), regularity there excludes a pole at \(x=-2\).
Pairing the other roots leaves a monic integral trace polynomial \(B\) in either parity of \(\deg D\).

At a nonreal circle root, \(\Psi'(u)=\zeta W'(\zeta)/W(\zeta)=-\zeta W'(\zeta)>0\).
Changing the local coordinate to \(x\) multiplies the residue of \(Y\) by \(1-\zeta^{-2}\), in addition to the factor \(1-\zeta^2\) in \(R\).
Their product is \(4\sin^2u\), and each reciprocal pair yields one positive trace residue.
At the exterior root the same product is negative, \(D'(\sigma)>0\), and \(f(\sigma)<0\) since the [two-point inequality](../../claims/Yin_C_G0345_v4.md#two-points) gives \(1<\sigma<T<2+\delta\le\theta\).
Thus \(B\) is the reduced denominator, with a genuine simple pole at each root, and the residues sum to \(j\).
Multiplying the integral expansion by \(B\) gives the coefficients of the polynomial \(C\), of degree \(\deg B-1\) and leading coefficient \(j\).
Between successive poles its quotient \(C/B\) has strictly negative derivative and takes both signs.
The sign at \(2\) places the final zero to the left of \(2\), and the leftmost gap begins above \(-2\).
When \(B\) is linear, \(C\) is the constant \(j\).
For every monic irreducible factor \(U_0\) of \(C\), \(z^{\deg U_0}U_0(z+z^{-1})\) is monic with constant one and all roots on the unit circle, exactly the nonzero-root case of [Kronecker's theorem](../literature/MV226/Yin_U001.md#mv226-kronecker-algorithm).

### The polynomial division and the atom

The first two coefficients of \(R_0=R/j\) at infinity are \(1,a\), the mass and mean of the normalized residues.
In \(L=x-a-1/R_0\) the polynomial part therefore vanishes, and every pole at a zero \(y\) of \(C\) has residue \(-1/R_0'(y)>0\).
All such \(y<2\), so \(0\le L(2)=2-a+j/(q-1)\le4+j/(q-1)\).
Weighting by \(G^2/c\) kills the zeros of \(A\) and leaves a positive measure on the traces belonging to \(U\).
Subtracting its transform from \(G^2L/c\) leaves a polynomial by the divided difference for \(G^2\).
The only possible proper part is consequently the proper part of \(-AH^2B/U\), since \(j=tc\), \(G=AH\) and \(1/R_0=cB/(UA)\).
Monic division gives \(-E/U\) with integral expansion at infinity, whose coefficient at \(x^{-1}\) is the total mass.
Because \(C(2)= (1-q)B(2)\ne0\), evaluation gives
\[
 -E(2)/U(2)=V(2)-tG(2)^2 B(2)/C(2)
            =V(2)+tG(2)^2/(q-1).
\]
When \(U=1\), the zero transform satisfies the same identity, which forces the positive summand to be an integer for admissible \(G\).

Under the symmetric circle lift, the recurrence for \(v^k+v^{-k}\) makes \(2\int v^k\,d\widetilde\lambda\) integral, and \(|1-v|^2=2-y\) gives the weighted mass \(s'\).
For the adjusted measure \(\nu\), the difference between its mass and its \(n\)-th Fourier coefficient is the integral of \(|1-v^n|^2/|1-v|^2\) against \(\widetilde\lambda\).
Expanding the geometric sum yields \(n\) times the integral mass plus integer multiples of the paired moments.
Symmetry also gives the negative indices.
The support is contained in a single finite cyclic group for each input, and the lift gives no mass to \(1\).
These are the finite support, positivity and integrality hypotheses of [one-sided isolation](../../claims/Yin_C_G0345_v6.md#statement).
I checked the growing-denominator argument and compared the [prior independent review](Yin_R_G0562_v6.md#atom-isolation-review), which verifies the signed-coset input from Sanders at statement level.
This review uses that external theorem at the same depth.

### Uniformity and the integer branches

The [derivative identity](../../ledger/Yin_L_G0462_v36.md#second) and \(|H_q'(0)|\le2\) hold before fixing \(j\).
Thus \(1\le j\le\delta(q+\theta^{-1}+2)\) forces \(q\to\infty\) when \(\delta\to0\), and division by \(q-1\) then gives \(j/(q-1)\to0\).
Conversely, at fixed \(j\), the bound \(j/\delta\ge q+\theta^{-1}-2\) suffices as \(q\to\infty\).
The admissible set contains \(G=A\) because \(A(2)\ne0\).
If the infimum failed to diverge, on a subsequence where it is bounded one could choose multipliers whose ratios exceed it by at most one.
The estimate for \(s\) and the weighted mass bound then bound \(\lceil2s'\rceil\) uniformly while \(0<h=tG(2)^2/(q-1)\le(j/(q-1))\|G\|^2/c\to0\).
For \(0<2h<1\), integrality of \(V(2)\) gives \(\lceil2s'\rceil-2s'=1-2h\), contradicting the left neighbourhood of \(1\) excluded for that uniform mass bound.

For \(j=1\), the primitive nonmonic product is \(1\), so \(G=1\) rules out a sequence of positive excesses tending to zero.
Together with the fixed-\(j\) converse this also excludes all the proposed radial limits at \(j=1\).
If \(j\le J\), there are at most \(\log_2 J\) positive-leading nonmonic factors and \(c\le J\).
A subsequence on which their degrees were bounded would give bounded \(\deg A\) and \(\|A\|^2/c\le J\,16^{\deg A}\), contradicting divergence.
In particular \(j=2\) eventually requires a nonmonic factor, and the leading-coefficient product then forces exactly one with leading coefficient two.
This argument provides no numerical value for the positive gap or existence assertion on the higher branches.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Trace obstruction](#trace-obstruction-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Trace obstruction](#trace-obstruction-review) | [C345v7 statement](../../claims/Yin_C_G0345_v7.md#statement) | Uniform first-branch gap, all normalized integral multipliers and consequences at bounded branch index. |
| [Trace obstruction](#trace-obstruction-review) | [C345v7 trace](../../claims/Yin_C_G0345_v7.md#trace) | Reciprocal descent, branch points, integrality, pole signs, interlacing and torsion traces. |
| [Trace obstruction](#trace-obstruction-review) | [C345v7 multiplier](../../claims/Yin_C_G0345_v7.md#strip) | Proper parts, positivity, monic division, integer moments, endpoint fraction and empty support. |
| [Trace obstruction](#trace-obstruction-review) | [C345v7 torsion atom](../../claims/Yin_C_G0345_v7.md#atom) | All Fourier indices, uniform mass, one-sided contradiction and branch deductions. |
| [Trace obstruction](#trace-obstruction-review) | [Exterior root](../../ledger/Yin_L_G0462_v32.md#boyd-return) | Root count with multiplicity for the full reciprocal associate. |
| [Trace obstruction](#trace-obstruction-review) | [Unit-circle roots](../../ledger/Yin_L_G0462_v34.md#crossings) | Simplicity, upward orientation and use of the full neutral fiber. |
| [Trace obstruction](#trace-obstruction-review) | [Two-point inequality](../../claims/Yin_C_G0345_v4.md#two-points) | Ordering of the exterior root of the associate and the Pisot root. |
| [Trace obstruction](#trace-obstruction-review) | [Integral series](../../ledger/Yin_L_G0462_v36.md#limit) | Integral Taylor series at zero with constant \(j\). |
| [Trace obstruction](#trace-obstruction-review) | [First derivative](../../ledger/Yin_L_G0462_v36.md#second) | Exact identity and its absolute bound, uniformly in \(j\). |
| [Trace obstruction](#trace-obstruction-review) | [Kronecker criterion](../literature/MV226/Yin_U001.md#mv226-kronecker-algorithm) | Monic lift with nonzero constant and all roots of modulus one. |
| [Trace obstruction](#trace-obstruction-review) | [Atom isolation](../../claims/Yin_C_G0345_v6.md#statement) | Left neighbourhood of one for a common mass bound and arbitrary finite cyclic groups. |
