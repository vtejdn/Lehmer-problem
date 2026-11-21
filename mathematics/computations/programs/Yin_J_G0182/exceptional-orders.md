---
author: Yin
---

# The sixteen small Frobenius orders at first prime 59

<a id="result"></a>
## Finite scope and reproduction

For each prime \(59<q\le410\) with \(\operatorname{ord}_q(59)\le58\), each \(55\le n\le58\), each \(\epsilon=\pm1\) and every integer \(a\ge3\), the exterior Salem root of \(G_a(X)=X^{n+1}-aX^n+\epsilon(aX-1)\) has no positive \(59q\)-th radical in its own field.
The calculation excludes all 128 prime, delay and sign choices.
The [other J182 search](readme.md#search) treats larger multiplicative orders by a separate method.

Run the [exact verifier](exceptional_orders.py) from the repository root with Python 3.
The recorded run used Python 3.14.3, standard-library integer arithmetic and no external input files.
It prints the seed lifts, all sixteen order and coverage counts, and any unresolved rows cause failure.

~~~text
python mathematics/computations/programs/Yin_J_G0182/exceptional_orders.py
~~~

| \(q\) | \(\operatorname{ord}_q(59)\) | Rows excluded in characteristic 59 | Rows excluded in characteristic \(q\) | Delays requiring characteristic \(q\), both signs |
| ---: | ---: | ---: | ---: | --- |
| 67 | 11 | 8 | 0 | — |
| 83 | 41 | 8 | 0 | — |
| 103 | 51 | 8 | 0 | — |
| 127 | 18 | 4 | 4 | 56, 57 |
| 137 | 17 | 8 | 0 | — |
| 139 | 46 | 8 | 0 | — |
| 151 | 5 | 6 | 2 | 55 |
| 157 | 52 | 8 | 0 | — |
| 163 | 6 | 2 | 6 | 55, 56, 57 |
| 181 | 5 | 6 | 2 | 55 |
| 193 | 48 | 8 | 0 | — |
| 197 | 49 | 8 | 0 | — |
| 277 | 46 | 8 | 0 | — |
| 281 | 7 | 8 | 0 | — |
| 337 | 16 | 8 | 0 | — |
| 353 | 32 | 8 | 0 | — |

<a id="trace"></a>
## Four trace congruences modulo the prime squared

Assume a positive \(59q\)-th radical \(\gamma\) exists in the field of the exterior root \(r\).
For either \(h\in\{59,q\}\), also \(r^{1/h}\) belongs to this field.
If \(s_j(a)\) denotes the sum of the \(j\)-th powers of the roots of \(G_a\), the [integral power trace congruence](../../../claims/Yin_C_G0345_v681.md#traces) gives \(s_{hj}(a)\equiv s_j(a)\bmod h^2\).
At this step \(h\) is odd and fixes the linear cofactor roots \(1,-1\) under powering, and there is no upper restriction on \(h\) in the congruence.
The program applies it for \(1\le j\le4\).

The Newton sums \(s_j(T)\) are integer polynomials in the indeterminate seed.
Over \(\mathbb F_h[T]\) Frobenius gives \(s_h(T)=s_1(T)^h=T^h\), for example by taking the sums in a splitting field of \(\mathbb F_h(T)\).
Hence \(s_h'(T)\equiv0\bmod h\), and \(s_h(c+ht)\equiv s_h(c)\bmod h^2\) for all integers \(c,t\).
For each \(c\bmod h\) the first congruence therefore specifies the unique lift \(a\equiv s_h(c)\bmod h^2\), since \(s_1(a)=a\).
The three remaining congruences are tested on this lift.
Newton's identity at index \(j\) contributes \(-j b_j\) when the coefficient \(b_j\) at degree \(n+1-j\) is present and \(-b_i s_{j-i}\) for each smaller positive index \(i\).
Only \(i=1,n,n+1\) can have nonzero \(b_i\).

For \(h=59\), the surviving lifts modulo \(59^2\) are exactly \(0,1,-1\) at delays 55, 56 and 57 and \(1,-1\) at delay 58, for either sign.
For every reverse-direction row in the table the surviving lifts modulo \(q^2\) are exactly \(0,1,-1\).
Thus each surviving reduction of \(G_a\) agrees with that of \(G_c\) at a cyclotomic seed \(c=0,1,-1\).

<a id="orbits"></a>
## The cost of a noncanonical root orbit

Write \(h\ell=59q\) and \(U=\prod(X-t)\) over the linear cofactor roots \(t=\pm1\) with \(t^{n-1}=\epsilon\).
The [field and Frobenius argument](../../../claims/Yin_C_G0345_v708.md#reduction) gives the reciprocal minimal polynomial \(S\) of \(\gamma\).
The \(\ell\)-th powers of the roots of its reduction modulo \(h\), counted with multiplicity, must give the entire multiset of roots of the reduction of \(P_c=G_c/U\).
Indeed the additional \(h\)-th powering preserves every reduced multiset defined over \(\mathbb F_h\).
The roots of the reduced \(S\) are nonzero and their multiplicities are invariant under both Frobenius and inversion.

The specialization \(G_0=X^{n+1}-\epsilon\) gives every primitive order dividing \(n+1\) at positive sign, or dividing \(2(n+1)\) and not dividing \(n+1\) at negative sign.
For \(c=\pm1\), the factorization \(G_c=(X-c)(X^n+\epsilon c)\) supplies the analogous binomial orders and one linear root.
Subtracting the cofactor gives a common multiplicity \(\mu_s\) at all primitive roots of each remaining order \(s\).
The verifier uses this description only when each retained order is coprime to \(h\ell\).
The binomials then contribute the indicated distinct primitive roots, with any repeats recorded by \(\mu_s\).
If this coprimality test fails, the direction supplies no exclusion for that seed.

For \(m\) coprime to \(h\) put \(D_m=|\langle h,-1\rangle|\) in \((\mathbb Z/m\mathbb Z)^\times\), taking \(D_1=1\).
This is the size of the joint Frobenius and inversion orbit of any primitive \(m\)-th root.
As \(\ell\) is prime and coprime to \(s\), a preimage of a primitive \(s\)-th root under \(\ell\)-th powering has order either \(s\) or \(s\ell\).
An orbit of preimages with the second order maps onto one target orbit with exactly \(D_{s\ell}/D_s\) points above each target point.
This follows from the surjective reduction of the two-generator subgroup modulo \(s\ell\) onto the corresponding subgroup modulo \(s\), or from transitivity and constant fiber size.
Thus even one copy of such an orbit requires multiplicity \(D_{s\ell}/D_s\) at each of its images.
If \(D_{s\ell}/D_s>\mu_s\) at every retained order, every preimage has the original order.
Powering permutes the primitive roots of that order, whose target multiplicities are equal, so the whole inverse multiset is exactly that of \(P_c\) and \(\overline S=\overline P_c\).
The program computes the group sizes by repeated multiplication modulo \(m\), retaining both signs.
For each delay and sign it first checks all surviving seeds in characteristic 59, and if any remain it checks all surviving seeds independently in characteristic \(q\).

<a id="norm"></a>
## The integer norm at a forced cyclotomic seed

Once \(\overline S=\overline P_c\) in characteristic \(h\), evaluation at \(\gamma\) gives \(G_c(\gamma)\in h\mathcal O_{\mathbb Q(r)}\).
This algebraic integer is nonzero since all roots of \(G_c\) are roots of unity and \(\gamma>1\).
Its absolute norm is at least \(h^d\), where \(d=[\mathbb Q(r):\mathbb Q]\).
On the other hand the sum of absolute coefficients of \(G_c\) is at most four, and the Salem radical has multiplicative Mahler measure \(\gamma\).
Therefore the absolute norm is at most \(4^d\gamma^{n+1}\).
The [first radical bound](../../../claims/Yin_C_G0345_v702.md#statement) gives \(\gamma^q=r^{1/59}<59\).
Since \(n+1\le59<q\), we get \(4^d\gamma^{n+1}<4^d59<59^d\le h^d\) for every degree in the table, all at least 54.
This contradiction excludes every row served by either direction.
