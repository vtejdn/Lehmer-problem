---
author: Yin
---
# A linear bound for bases of primitive permutation groups

<a id="ls99-u001"></a>
<a id="base"></a>
## Base size and alternating sections

For \(G\le\operatorname{Sym}(\Omega)\), a **base** is a subset \(B\subseteq\Omega\) whose pointwise stabilizer in \(G\) is trivial.
The base size \(b(G)\) is the minimum cardinality of such a subset for the specified action.
Section 1.4 defines these terms, then explicitly identifies involvement of the alternating group \(A_d\) with the existence of a subgroup of \(G\) having a quotient isomorphic to \(A_d\).
If \(d\ge5\), \(G\) is finite and primitive on \(\Omega\) and \(G\) has no \(A_d\) section, Theorem 1.4 bounds \(b(G)\) by a linear function of \(d\).
Equivalently one may take \(b(G)\le A d+B_0\) for absolute nonnegative constants \(A,B_0\).
The paper quotes no numerical pair in the theorem. [Journal facsimile, §1.4 and Theorem 1.4, pp. 499–500](../../../literature/pdf/LS99--journal.pdf#page=4)

The proof starts with \(d\ge5\), uses an earlier reduction to the almost simple and primitive linear affine cases, and allows an additional \(20+2\log d\) when passing back to the general primitive group.
It treats the almost simple case on pp. 502–503 and the affine case with Lemmas 2.1 and 2.2 on pp. 503–504.
The cited classification and base-size inputs are used here through the published theorem. [Journal facsimile, proof of Theorem 1.4, pp. 502–504](../../../literature/pdf/LS99--journal.pdf#page=6)

For \(n=|\Omega|\ge2\), order a minimal base as a tuple of length \(b(G)\).
Its orbit has size \(|G|\), and there are at most \(n^{b(G)}\) tuples.
For \(t=\theta(G)\) in Babai's convention set \(d=\max(5,t+1)\).
Then \(A_d\) is absent as a section by definition, and \(2\le t\) gives \(d\le5t/2\).
Consequently
\[
 |G|\le n^{b(G)}\le n^{Ad+B_0}
      \le n^{((5A+B_0)/2)t}.
\]
This also covers groups of thickness below five and gives an exponent multiplier independent of the group, the degree and the excluded alternating section. [Babai's definition](../Bab18/Yin_U001.md#thickness)

<a id="almost-simple"></a>
## Theorem 1.3 for an almost simple primitive group

Let \(G\) be a finite primitive permutation group that is almost simple, so \(T\le G\le\operatorname{Aut}(T)\) for its nonabelian simple socle \(T\).
Theorem 1.3 gives an absolute constant \(c\) such that \(b(G)\le c\) unless \(G\) has one of the following permutation representations.

1. \(G=A_m\) or \(S_m\) acts on the \(k\)-subsets of an \(m\)-element set, or on its partitions into \(k\) parts of equal size \(m/k\).
2. \(T\) is classical and \(G\) has a subspace action in the sense of §1.1.

Consequently \(\log |G|/\log|\Omega|>c\) in such an action forces one of the two listed representations.
In the first case \(m\) is the degree of the underlying natural symmetric or alternating group, while \(|\Omega|\) is the number of subsets or partitions in the representation.
For actions outside both families the theorem also gives probability tending to one that a uniformly random \(c\)-tuple is a base as \(|G|\) tends to infinity. [Theorem 1.3, pp. 499–500](../../../literature/pdf/LS99--journal.pdf#page=4)

<a id="subspace-action"></a>
### Subspace actions in §1.1

Let \(T\) be a finite simple classical group with natural module \(V\) in characteristic \(p\).
In the terminology of §1.1 a **subspace action** is the action of \(G\) on the cosets of a maximal subgroup \(M\) of one of these three kinds.

1. \(M=G_U\) for a proper nonzero subspace \(U\le V\).
   For \(T=\operatorname{PSL}(V)\) any such \(U\) is allowed.
   In the groups with a form, \(U\) is totally singular or nondegenerate, or is a nonsingular one-dimensional space for an orthogonal group in characteristic two.
2. \(T=\operatorname{PSL}(V)\), \(G\) contains a graph automorphism of \(T\), and \(M=G_{U,W}\) stabilizes the subspace configuration formed by proper nonzero \(U,W\).
   Their dimensions satisfy \(\dim U+\dim W=\dim V\), and either \(U\subseteq W\) or \(V=U\oplus W\).
3. \(T=\operatorname{Sp}_{2m}(q)\) in characteristic two, and \(M\cap T=\operatorname{O}^{+}_{2m}(q)\) or \(\operatorname{O}^{-}_{2m}(q)\).

Thus a criterion that excludes only actions on individual subspaces of \(V\) still has to account for the graph-automorphism pairs and the even-characteristic symplectic coset actions. [Definition of subspace subgroup and action, pp. 497–498](../../../literature/pdf/LS99--journal.pdf#page=1)

<a id="least-degree"></a>
## Least degree of a faithful classical action

At the start of §2 the authors write \(\mathrm{Cl}(n,q)\) for the almost simple groups with classical socle over \(\mathbb F_q\) and natural dimension \(n\).
In the proof of Theorem 1.1 they define \(P(G)\) as the smallest degree of a faithful permutation representation of \(G\).
They infer from the bounds in Kleidman and Liebeck, §5.2.2, that \(P(G)>q^{n/2}\) outside finitely many possibilities for \(G\).
The argument there estimates fixed points in a non-subspace action, but this particular bound concerns the group invariant \(P(G)\).
Every faithful permutation action of the same \(G\), including a subspace action, therefore has degree at least \(P(G)\).
The finite exceptions are not enumerated in this passage. [Journal facsimile, p. 501, proof of Theorem 1.1](../../../literature/pdf/LS99--journal.pdf#page=5)

Section 3 specifies that the field of the natural module has order \(Q=q^u\), where \(u=2\) for unitary groups and \(u=1\) otherwise.
In terms of \(Q\), the lower bound is \(Q^{n/4}\) in the unitary case and \(Q^{n/2}\) in the other cases. [Field convention, printed p. 508](../../../literature/pdf/LS99--journal.pdf#page=12)
