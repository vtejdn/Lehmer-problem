---
author: Yin
---

# Outer automorphisms and projective isometries of classical simple groups

<a id="byo15-u001"></a>
<a id="classical-outer"></a>
## Classical families and the outer automorphism bound

In §5 Byott writes \(q=p^e\) and takes the simple group \(T\) as the central quotient of the group \(G\) in Table 1, with \(d=|Z(G)|\) and \(|T|=|G|/d\).
On printed p. 893 he gives \(|\operatorname{Out}(T)|=d\epsilon g\), where the factors count diagonal, field and graph automorphisms respectively.
This factorization is an order formula. [Printed pp. 892–893](../../../literature/pdf/Byo15.pdf#page=10)

Write \(n\) for natural dimension and \(r\) for the symplectic or orthogonal rank.
Table 1 lists linear groups in dimension at least two, unitary groups in dimension at least three, symplectic groups in rank at least two, odd orthogonal groups in rank at least three and even orthogonal groups in rank at least four.
It excludes \(\operatorname{PSL}_2(2),\operatorname{PSL}_2(3),\operatorname{PSU}_3(2)\) and \(\operatorname{PSp}_4(2)\).
For \(\operatorname{PSL}_n(q)\) and \(\operatorname{PSU}_n(q)\), Table 2 gives \(d=\gcd(n,q-1)\) and \(\gcd(n,q+1)\) respectively.
For \(\operatorname{PSp}_{2r}(q)\) and \(\operatorname{P}\Omega_{2r+1}(q)\) it gives \(d=\gcd(2,q-1)\).
For \(\operatorname{P}\Omega_{2r}^{\pm}(q)\) it gives \(d=\gcd(4,q^r\mp1)\).
The field factor is \(2e\) for unitary and even-dimensional minus-type orthogonal groups and \(e\) for the other listed families.
The split orthogonal group of dimension eight has graph factor \(6\), including triality.
Elsewhere the listed graph factors are at most two, including the rank-two symplectic group in even characteristic.
Thus \(d\le\max(n,4)\), \(\epsilon\le2e\) and \(g\le6\).
If \(Q\) is the natural module's field size, then \(Q=q^2\) in the unitary case and \(Q=q\) otherwise, and \(e\le\log_2 Q\).
In particular the minus-type orthogonal group's field factor \(2e\) occurs even though its quadratic space is over \(\mathbb F_q\). [Natural-module convention of Liebeck and Shalev](../LS99/Yin_U001.md#least-degree)
These inequalities give the uniform estimate \(|\operatorname{Out}(T)|\ll n\log(2Q)\). [Table 2, printed p. 894](../../../literature/pdf/Byo15.pdf#page=12)

For the symplectic parameters \((r,q)\), Table 1 excludes \((2,2)\) while Table 2 prints \((4,2)\) as its exclusion.
The former group \(\operatorname{Sp}_4(2)\) is not simple.
The latter group \(\operatorname{Sp}_8(2)\) has fixed finite order, so enlarging the absolute constant covers it in the estimate without assigning it an exact outer order from that row.
Byott records the identifications \(\operatorname{P}\Omega_5(q)\simeq\operatorname{PSp}_4(q)\) and \(\operatorname{P}\Omega_{2r+1}(q)\simeq\operatorname{PSp}_{2r}(q)\) for even \(q\) in the second case. [Tables and conventions, printed pp. 892–894](../../../literature/pdf/Byo15.pdf#page=10)

<a id="projective-index"></a>
## Index in the projective linear isometry group

Let \(I\) be the full linear isometry group of the indicated form and let \(PI\) be its image modulo scalar matrices.
In the linear family take \(I=\operatorname{GL}_n(q)\).
The preceding \(d\) is the order of the center of Byott's \(G\).
To pass from the tabulated simple-group orders to \([PI:T]\), one also needs the order of \(I\) and its scalar subgroup.
The following calculations supply this comparison for the classical families in Table 1.

For the linear and unitary families the determinant maps onto the cyclic multiplicative group of order \(q-1\) or the cyclic norm-one group of order \(q+1\), respectively.
Diagonal matrices in a standard basis realize all these determinants, using an orthogonal basis in the unitary case.
The determinants of scalars are the \(n\)-th powers in the same cyclic group.
Consequently the projective indices are \(\gcd(n,q-1)\) and \(\gcd(n,q+1)\), respectively.
For the symplectic family \(PI=T\).

In the orthogonal families let \(V\) have quadratic form \(F\), with full isometry group \(O(V)\).
In each dimension used here the scalar isometries have order \(s=\gcd(2,q-1)\).
The standard hyperbolic-pair count gives \(|O_{2r+1}(q)|=s|G|\) and \(|O_{2r}^{\pm}(q)|=2|G|\) for the corresponding orders of \(G\) in Table 1.
Here is the count in both characteristics.
Upon adjoining a hyperbolic plane to an \(m\)-dimensional space \(W\), the number \(N(V)\) of zeroes, including zero, satisfies
\[
 N(V)=(q-1)q^m+qN(W).
\]
Indeed the new equation is \(xy+F(w)=0\), with \(y\) uniquely determined when \(x\ne0\) and unrestricted when \(x=0\) and \(F(w)=0\).
For each nonzero isotropic vector, there are \(q^m\) isotropic partners with polar pairing one, by choosing the \(W\)-component freely in a hyperbolic decomposition and solving for the remaining coefficient.
The complements of hyperbolic pairs are isometric by Witt cancellation, so
\[
 |O(V)|=(N(V)-1)q^m|O(W)|.
\]
The starting spaces have dimension zero, anisotropic dimension one or anisotropic dimension two, all with \(N=1\).
Their isometry orders are \(1,s,2(q+1)\), respectively.
In the last case the form is a scalar multiple of the quadratic-extension norm, with norm-one multiplications transitive on norm-one vectors and two possibilities for an isometry fixing \(1\), namely the identity and conjugation.
Induction gives \(N(V)-1=q^{2r}-1\) in odd dimension and \((q^r\mp1)(q^{r-1}\pm1)\) in even type \(\pm\).
Substitution in the order recurrence yields the stated multiples of the products in Table 1. [Simple-group orders and central quotient, printed pp. 892–893](../../../literature/pdf/Byo15.pdf#page=10)

It follows that the odd-dimensional projective orthogonal index is \(d=\gcd(2,q-1)\).
In even dimension and type \(\pm\) it is \(2\gcd(4,q^r\mp1)/s\), at most four since even \(q\) gives \(\gcd(4,q^r\mp1)=1\).
Thus all these indices are at most \(\max(n,4)\) throughout the indicated simple families.
The index calculation concerns linear isometries and, in the linear family, the projective general linear group.
Field automorphisms, similitudes and triality in the full automorphism group enter the separate outer bound above.
