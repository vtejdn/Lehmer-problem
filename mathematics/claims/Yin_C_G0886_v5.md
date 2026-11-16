---
author: Yin
---

# Triality, cycle lengths and one-cusp divisibility in the D4 Mahler gap

<a id="statement"></a>
## Statement and hypotheses

Use the lattice \(H=D_4^{\oplus r}\), \(r\ge1\), the hyperbolic plane \(U=\mathbb Ze+\mathbb Zf\) with \((e,f)=1\), the positive isometries and the transvections of the [D4-block theorem](Yin_C_G0886_v4.md#statement).
Here \(A\) is a specified word in those generators, \(P_A(z)=\det(zI-A)\) on \(H\oplus U\), and \(\lambda_{\rm L}\) denotes the degree-ten [Lehmer root](Yin_C_G0886_v2.md#statement).
Take the product \(R\) of all its positive factors in their original order.
The permutation of blocks induced by \(R\) is denoted by \(\sigma\), of order \(d\).

Each block has three orthonormal frames of unoriented lines spanned by norm-one vectors of \(D_4^*\), as described [below](#dual-frames).
For each cycle \(C\) of \(\sigma\) of length \(\ell_C\), let \(h_C\) be the action of \(R^{\ell_C}\) on one block of that cycle.
Let \(\mathcal B\) consist of the cycles on which \(h_C\) permutes the three frames as a three-cycle.
This condition is independent of the initial block.
Set
\[
k=
\begin{cases}
1,&\mathcal B=\varnothing,\\
3^{1+\max_{C\in\mathcal B}v_3(\ell_C)},&\mathcal B\ne\varnothing .
\end{cases}
\]

1. If \(M(P_A)>1\), then \(M(P_A)\ge\lambda_{\rm L}^{1/k}\), and \(1<M(P_A)^k<6/5\) implies \(M(P_A)^k=\lambda_{\rm L}\).
   The bound combines with [v4](Yin_C_G0886_v4.md#statement) to give \(M(P_A)\ge\lambda_{\rm L}^{1/\min(d,k)}\).
   In particular, arbitrarily small positive logarithmic measures in a sequence of these presentations require cycles in \(\mathcal B\) whose lengths have unbounded 3-adic valuation.
   More precisely, \(k\to\infty\) along every such sequence with \(M(P_A)\to1\) from above.
2. If every parameter at the \(f\)-cusp belongs to \(3H\), the conclusions of part 1 with exponent **one** hold for all permutations and all \(e\)-parameters.
   The same holds with \(e,f\) exchanged.
   There is no bound on rank, word length, the number of transvections or their norms.

The first assertion refines the permutation dependence of the [existing independently reviewed cover](Yin_C_G0886_v4.md#decision-d4-block-canonical-cover).
The second uses a different representation, of three times the positive dimension.
Both preserve the full Mahler measure.

<a id="argument"></a>
## Reduction to one positive isometry

The identities \(RT_{e,v}R^{-1}=T_{e,Rv}\) and \(RT_{f,v}R^{-1}=T_{f,Rv}\) follow directly because \(R\) is an isometry fixing \(e,f\).
Move every positive factor to the right to write \(A=B R\), where \(B\) is a product of transvections with parameters still in \(H\).
This operation preserves the divisibility of the individual parameters by three.
For every positive integer \(m\), the same rearrangement gives \(A^m=B_mR^m\), where \(B_m\) consists of \(B,RBR^{-1},\ldots,R^{m-1}BR^{1-m}\), in that order.
Thus an equivariant embedding for the single positive isometry \(R^m\) suffices for the [standard integer embedding theorem](Yin_C_G0886_v3.md#statement).

<a id="dual-frames"></a>
## The three frames and the cycle test

In the standard four real coordinates, the [dual-lattice calculation](Yin_C_G0886_v4.md#d4-positive-group) gives exactly 24 norm-one vectors, the eight signed coordinates and the sixteen half-vectors with coordinates \(\pm1/2\).
Pair opposite vectors into twelve lines.
Four lines form the coordinate frame.
The four half-vector lines with an even number of minus signs form a second frame, and the four with an odd number form a third.
Parity is well defined modulo simultaneous negation in dimension four.
Distinct lines within either half-vector frame have representatives differing at exactly two coordinates, so are orthogonal.
Vectors in different frames have scalar product of absolute value \(1/2\).
The orthogonality graph of the twelve lines is therefore the disjoint union of three complete graphs on four vertices.
Isometries between blocks preserve the twelve lines, their inner products up to signs and hence these three components.

An assignment of one frame per block preserved by \(R^m\) exists exactly when the return map along each cycle of its block permutation fixes a frame.
Indeed, transport a fixed initial frame around that cycle by the actual isometries on its arrows.
The return condition is necessary and sufficient for consistency at the initial block.
Changing the initial block conjugates the return map by a block isometry, preserving the criterion.
For a cycle of \(R\) of length \(\ell\), the permutation of \(R^m\) splits it into \(\gcd(\ell,m)\) cycles.
The return at any chosen block is \(R^{m\ell/\gcd(\ell,m)}\), hence conjugate to \(h_C^{m/\gcd(\ell,m)}\).
When \(h_C\) fixes a frame, every such power does.
When its frame permutation is a three-cycle, the power fixes a frame precisely if \(3\mid m/\gcd(\ell,m)\), equivalently \(v_3(m)>v_3(\ell)\).
Consequently the admissible \(m\) are exactly the multiples of \(k\).
This minimality concerns the transported-frame construction.

Choose \(m=k\), and orient the four unit lines of the assigned frame in each block arbitrarily.
Pairing with these vectors defines an isometric integer embedding \(H\to\mathbb Z^{4r}\), since each chosen unit belongs to the corresponding dual lattice.
On these coordinates \(R^k\) acts by a signed permutation, with no restriction on its order.
Apply [v3](Yin_C_G0886_v3.md#statement) to the normalized word \(B_kR^k\).
All its transvection parameters have even squared norm because \(H\) is even.
As eigenvalues of powers are the corresponding powers with multiplicities and \(P_A\) is monic, \(M(P_{A^k})=M(P_A)^k\).
This proves part 1 including its strict-interval assertion.

<a id="scaled-embedding"></a>
## Simultaneous use of all three frames

Choose one oriented unit vector per line in each of the three frames of every block.
Let \(J:H\to\mathbb Z^{12r}\) be the integer map taking all these pairings.
Each frame in a block is orthonormal, so \((Jx,Jy)=3(x,y)\) on the whole positive space.
Every positive isometry \(R_0\) extends on these coordinates to a signed permutation \(S_0\) satisfying \(S_0J=JR_0\), since its action permutes all twelve lines in each transported block.

Write \(e',f'\) for the standard hyperbolic pair in the ambient space \(\mathbb R^{12r}\oplus U_{\mathbb R}\).
Extend \(J\) to \(F\) by \(F(e)=3e'\) and \(F(f)=f'\).
Then \((Fx,Fy)=3(x,y)\) and the image is nondegenerate.
Substitution into the transvection formulas gives
\[
 FT_{e,v}=T_{e',Jv}F,\qquad
 FT_{f,w}=T_{f',Jw/3}F.
\]
Indeed \((e',Fx)=(e,x)\), \((f',Fx)=3(f,x)\) and \((Jv,Fx)=3(v,x)\), giving all linear and quadratic terms with the indicated factors.
The vector \(Jv\) is integral of even squared norm \(3(v,v)\).
If \(w=3u\) in \(H\), then \(Jw/3=Ju\) is integral of even squared norm \(3(u,u)\).
The signed permutation extensions fix \(e',f'\).
These generators form a word \(\widehat A\) on the standard integral positive lattice with its hyperbolic plane, with \(\widehat AF=FA\).
The orthogonal complement of the image is positive definite because the image already contains \(U_{\mathbb R}\).
It is invariant under \(\widehat A\), and every eigenvalue on it has modulus one.
Thus \(M(P_{\widehat A})=M(P_A)\).
The [standard-lattice gap and strict interval](Yin_C_G0886_v3.md#statement) applied to \(\widehat A\) prove part 2.
Exchanging the cusps only exchanges which hyperbolic generator is scaled by three.

<a id="positive-examples"></a>
## Positive examples with one long cycle

For \(\ell\ge2\), take a single cycle of \(\ell\) blocks.
Choose identity isometries on the arrows except at the return, where the isometry is the order-three leaf cycle of the [D4 simple basis](../ledger/Yin_L_G0462_v18.md#d4-equivariance-obstruction).
It acts as a three-cycle on the frames: if it fixed any frame, that frame's coordinate map would give an isometric integer embedding into \(\mathbb Z^4\) extending it by a signed permutation, excluded by the cited argument.
Hence the entire cycle belongs to \(\mathcal B\).

Choose \(v=(3\ell+1)\alpha\) with \(\alpha\) a root in the first block, \(n=(v,v)=2(3\ell+1)^2\), and \(w=cv\), where \(c=1\) or \(3\).
For \(A=T_{e,v}T_{f,w}R\), the diagonal coefficients at \(e,f\) are \(1-cn+c^2n^2/4\) and \(1\).
The positive-to-positive block sends \(x\mapsto Rx-v(w,Rx)\), with trace \(\operatorname{tr}(R|_H)-(w,Rv)=0\) because the cycle moves every block and \(Rv\) is supported off the first block.
Consequently \(\operatorname{tr} A=2-cn+c^2n^2/4>4\ell+2\) for the stated values.
An operator of dimension \(4\ell+2\) whose eigenvalues all have modulus at most one has absolute trace at most \(4\ell+2\), so \(M(P_A)>1\).

With \(c=1\) and \(\ell=3j+1\), \(j\ge1\), the permutation orders \(\ell\) are unbounded while \(k=3\).
With \(c=3\) and \(\ell=3^a\), \(a\ge1\), both \(d\) and \(k=3^{a+1}\) tend to infinity, while part 2 gives the unpowered gap.
These examples distinguish hypotheses of presentations; they do not establish sharpness of any spectral bound.
Unrestricted words with arbitrarily large 3-adic valuation on cycles in \(\mathcal B\) and parameters failing both cusp divisibility tests remain beyond the two uniform conclusions.
The [unrestricted Lehmer question](../tasks/Yin_T_G0001_v1.md#contract) remains open.

## Assessment history

### Decision frame-and-cusp-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T07:35 |
| status | open |
| reason | Retain the complete proposed deductions and examples for separate mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [D4 power and divisibility bounds](#statement) | Both complete-measure bounds and their strict-interval consequences. |
| argument | [Positive-factor normalization](#argument) | Normal forms for the specified word and its powers. |
| argument | [Cycle frames](#dual-frames) | Frame action, exact minimal admissible power and whole-measure transfer. |
| argument | [Three-frame similitude](#scaled-embedding) | Integral generators at the two cusps and neutral complement. |
| argument | [Examples](#positive-examples) | Actual positive spectra with unbounded permutation orders. |
| dependency | [Standard embedding theorem](Yin_C_G0886_v3.md#statement) | Exact unpowered gap and strict interval in the signed-permutation representation. |
| dependency | [D4 dual and block decomposition](Yin_C_G0886_v4.md#d4-positive-group) | Dual unit lines, full positive isometry group and ordered block action. |
| dependency | [Existing D4 permutation bound](Yin_C_G0886_v4.md#decision-d4-block-canonical-cover) | Independent bound with exponent equal to the block-permutation order. |
| dependency | [Triality obstruction](../ledger/Yin_L_G0462_v18.md#d4-equivariance-obstruction) | The order-three simple-basis automorphism used in the examples cannot act by signed permutations in an isometric integer embedding. |


### Decision d4-frames-and-similitude-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T07:42 |
| status | proved |
| reason | Adopt the frame-power bound, the unpowered bound under one-cusp divisibility and the two positive examples after independent examination of their complete arguments. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [D4 power and divisibility bounds](#statement) | Both complete-measure bounds and their strict-interval consequences. |
| argument | [Positive-factor normalization](#argument) | Normal forms for the specified word and its powers. |
| argument | [Cycle frames](#dual-frames) | Frame action, exact minimal admissible power and whole-measure transfer. |
| argument | [Three-frame similitude](#scaled-embedding) | Integral generators at the two cusps and neutral complement. |
| argument | [Examples](#positive-examples) | Actual positive spectra with unbounded permutation orders. |
| dependency | [Standard embedding theorem](Yin_C_G0886_v3.md#statement) | Exact unpowered gap and strict interval in the signed-permutation representation. |
| dependency | [D4 dual and block decomposition](Yin_C_G0886_v4.md#d4-positive-group) | Dual unit lines, full positive isometry group and ordered block action. |
| dependency | [Existing D4 permutation bound](Yin_C_G0886_v4.md#decision-d4-block-canonical-cover) | Independent bound with exponent equal to the block-permutation order. |
| dependency | [Triality obstruction](../ledger/Yin_L_G0462_v18.md#d4-equivariance-obstruction) | The order-three simple-basis automorphism used in the examples cannot act by signed permutations in an isometric integer embedding. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1114_v18.md#d4-frame-and-cusp-review) | Both assertions, every proof section and example, and the fixed dependency interfaces at their stated scopes. |

## Current assessment
[Selected decision](#decision-d4-frames-and-similitude-reviewed)
