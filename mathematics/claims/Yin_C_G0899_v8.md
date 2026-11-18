---
author: Yin
---

# A prime-order Salem trace resultant supported entirely in growing residue degree

<a id="statement"></a>
## The trace ideal and its residue fields

Let \(r\ge3\), let \(p>12r+1\) be a prime, and let \(N\) be any positive multiple of \(p\).
Set
\[
 f(z)=z^r-\sum_{j=0}^{r-1}z^j,\qquad g(z)=z^rf(1/z),\qquad H_\pm(z)=z^Nf(z)\pm g(z).
\]
For either sign \(H_\pm\) has a unique exterior root \(\alpha\), with \(3/2<\alpha<2\).
Its monic minimal polynomial \(P\) is a Salem polynomial of even degree \(d\) with \(N-11r\le d\le N+r\).
Let \(P(z)=z^{d/2}T_P(z+z^{-1})\), and define \(S_p\) by \(\Phi_p(z)=z^{(p-1)/2}S_p(z+z^{-1})\).
Then in \(\mathbb Z[X]\) one has
\[
                  (T_P,S_p)=(2,S_p).
\]
Consequently the [trace resultant and largest common integer modulus](Yin_C_G0899_v5.md#statement) are
\[
 B_p(P)=|\operatorname{Res}(T_P,S_p)|=2^{(p-1)/2},
 \qquad G_p(P)=\max_{a\in\mathbb Z}\gcd(T_P(a),S_p(a))=1.
\]
Every residue field of this finite quotient has characteristic two and degree
\[
 k_p=\min\{j\ge1:2^j\equiv 1\ \text{or}\ -1\bmod p\}\ \ge\log_2(p-1)
\]
over \(\mathbb F_2\).
The quotient is a product of \((p-1)/(2k_p)\) fields of this degree.

Take \(N=p^2\), let \(r\to\infty\), and allow either sign at each step.
Then \(M(P)=\alpha\to2\), \(d/p^2\to1\), and hence \(p=o(d)\).
The difference \(\log B_p(P)/(p-1)-m(P)/2\) tends to zero, whereas \(\log G_p(P)/(p-1)=0\) throughout.
These statements also hold when the primes are chosen with \(p/r\to\infty\).

<a id="salem"></a>
## The exterior root and the cyclotomic cofactor

The [multinacci polynomial](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) is irreducible, with a single Pisot root outside the disk and all other roots in its interior.
Its coefficients give \(f(3/2)=2-(3/2)^r<0\), \(g(3/2)=4-3(3/2)^r<0\), \(f(2)=1\), and \(g(2)=3-2^{r+1}\).
For \(H_+\) the signs at \(3/2\) and \(2\) are respectively negative and positive since \(N\ge r+1\).
For \(H_-\) the same signs follow from the [multinacci bracket](Yin_C_G0899_v7.md#salem), whose calculation applies to every \(r\ge3\) and \(N\ge4\).
The [circle and torsion argument](../ledger/Yin_L_G0462_v111.md#cofactor) gives at most one strictly exterior root for either sign, counting multiplicity.
Reciprocity up to sign gives its inverse as the unique strictly interior root.
The minimal factor \(P\) of \(\alpha\) has constant coefficient of absolute value one and must contain this inverse.
Thus \(P\) is reciprocal and the cofactor \(C=H_\pm/P\) is cyclotomic by Kronecker's theorem.
A real reciprocal quadratic unit in \((1,2)\) would have integral trace strictly between \(2\) and \(5/2\), so \(\alpha\) is a Salem number.

For either sign the cited torsion argument bounds the number of distinct torsion roots by \(10r\).
To count repetitions, set \(D=Nfg+z(f'g-fg')\).
Then \(zfH_\pm'-(Nf+zf')H_\pm=\mp D\), and \(D\) has degree \(2r\) because the top terms of the derivative difference cancel.
Thus the excess over simple multiplicity contributes at most \(2r\) to \(\deg C\), as in the [all-delay degree bound](Yin_C_G0899_v7.md#degree).
This gives \(\deg C\le12r<p-1\) and the asserted bounds on \(d=N+r-\deg C\).

<a id="ideal"></a>
## Removing the cyclotomic factors at the chosen order

Write \(\zeta\) for a primitive \(p\)-th root and \(t=\zeta+\zeta^{-1}\).
Since \(p\mid N\), direct evaluation gives
\[
 H_-(\zeta)=2(\zeta^r-1),\qquad
 H_+(\zeta)=-2\zeta\,\frac{1-\zeta^{r-1}}{1-\zeta}.
\]
For \(1\le j<p\), \((1-\zeta^j)/(1-\zeta)\) is an algebraic integer of absolute norm one and hence a unit.
The absolute norms of \(H_-(\zeta)\) and \(H_+(\zeta)\) in \(\mathbb Q(\zeta)\) are therefore \(2^{p-1}p\) and \(2^{p-1}\), respectively.

The norm of \(C(\zeta)\) is odd.
Indeed, a common root of a cyclotomic factor \(\Phi_m\) of \(C\) and \(\Phi_p\) in characteristic two would have order \(p\).
Writing \(m=2^a b\) with \(b\) odd, the roots of the reduction of \(\Phi_m\) have order exactly \(b\).
For \(a=0\) this follows by separability of \(z^b-1\) and its cyclotomic factorization, and for \(a\ge1\) it follows from \(\overline{\Phi}_{2^a b}=\overline{\Phi}_b^{\,2^{a-1}}\) in characteristic two.
Thus \(b=p\) would force \(\deg\Phi_m\ge p-1>\deg C\).

For the plus sign \(C(\zeta)\) now has absolute norm one, so \(P(\zeta)/2\) is a unit in \(\mathbb Z[\zeta]\).
For the minus sign, \(z-1\) divides \(H_-\) and \(P(1)\ne0\), so \(C\) contains \(z-1\).
The norm of \(C(\zeta)\) is odd and divides \(2^{p-1}p\), while the factor \(\zeta-1\) has absolute norm \(p\).
Consequently \(C(\zeta)/(\zeta-1)\) is a unit, and the formula for \(H_-(\zeta)\) again gives \(P(\zeta)/2\) a unit.
In both cases \(T_P(t)/2=\zeta^{-d/2}P(\zeta)/2\) and its inverse are real cyclotomic integers and therefore lie in \(\mathbb Z[t]\) by the [real-order argument](../ledger/Yin_L_G0462_v111.md#ideals).
It follows that \(T_P(t)\mathbb Z[t]=2\mathbb Z[t]\).
Taking inverse images under evaluation \(\mathbb Z[X]\to\mathbb Z[t]\), whose kernel is \((S_p)\), proves the ideal equality.
Taking the absolute norm from \(\mathbb Q(t)\) gives the stated trace resultant.

<a id="residue"></a>
## Frobenius orbits and integer evaluations

The quotient by the trace ideal is \(\mathbb F_2[X]/(\overline S_p)\).
Over an algebraic closure of \(\mathbb F_2\), the nontrivial \(p\)-th roots are distinct and their traces \(u+u^{-1}\) are exactly the roots of \(\overline S_p\).
Two of these traces agree precisely when the roots coincide or are inverses, since the two elements with a given trace \(t_0\) solve \(Y^2-t_0Y+1=0\).
This gives \((p-1)/2\) distinct traces and proves separability.
The \(j\)-th power of Frobenius fixes such a trace precisely when \(u^{2^j}=u^{\pm1}\), so all its orbits have length \(k_p\).
Since \(p\mid 2^{k_p}-1\) or \(p\mid 2^{k_p}+1\), one has \(k_p\ge\log_2(p-1)>1\).
Factoring \(\overline S_p\) by Frobenius orbits gives the product of residue fields in the statement.
Evaluation of the ideal equality at an integer \(a\) gives \(\gcd(T_P(a),S_p(a))=\gcd(2,S_p(a))=1\), since \(\overline S_p\) has no root in \(\mathbb F_2\).

<a id="scope"></a>
## Correct resultant rate at an order with trivial integer modulus

For fixed \(1<x<2\) the identities
\[
 (x-1)f(x)=(x-2)x^r+1,\qquad (x-1)g(x)=2x-1-x^{r+1}
\]
give \(f(x)/x^r\to(x-2)/(x-1)<0\) and \(g(x)/x^r=O_x(1)\).
With \(N=p^2\to\infty\) it follows that \(H_\pm(x)<0\) eventually, for both signs.
Together with \(H_\pm(2)>0\) and uniqueness of the exterior root this gives \(\alpha\to2\).
Since \(12r<p\), the degree bound gives \(d=N+O(p)\).
Thus the prime can exceed the seed degree by an arbitrarily large factor while remaining sublinear in \(d\).
At this order the entire exponential trace resultant lies in characteristic two, with no common root in any extension of \(\mathbb F_2\) of prescribed bounded degree once \(p\) is large enough.

At the prime equal to the seed degree the [earlier example](Yin_C_G0899_v7.md#statement) had both resultant and common modulus equal to one.
The present examples separate the two rates at the same chosen prime.
The [selection theorem](Yin_C_G0899_v6.md#selection) gives another prime for each sufficiently large delay and every seed in a fixed finite list.
For varying inputs the possibilities of choosing the prime adaptively and of proving stronger estimates confined to measures approaching one remain open.

## Assessment history

### Decision dyadic-trace-algebra-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-18T05:07 |
| status | open |
| reason | Submit the exact trace ideal for both signs and its consequence for detecting the Mahler rate by common roots of bounded residue degree. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace ideal and finite quotient](#statement) | Both multinacci returns, the Salem factors, all selected prime divisors of the delay, the residue fields, and the two asymptotic rates. |
| argument | [Exterior root and torsion factors](#salem) | Both signs, the exterior interval and the degree bound including repeated roots. |
| argument | [Cyclotomic evaluation](#ideal) | The dyadic valuation survives cofactor removal and gives the exact trace ideal in the real order. |
| argument | [Frobenius orbits](#residue) | Separability, common residue degree and failure of integer evaluation. |
| argument | [Asymptotics and scope](#scope) | Convergence of the exterior root to two and the strict difference between resultant and common-modulus rates. |
| dependency | [Multinacci roots](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) | Irreducibility, the Pisot property and the locations of the conjugates. |
| dependency | [Exterior bracket](Yin_C_G0899_v7.md#salem) | The minus sign at the endpoints for all stated seed degrees and delays. |
| dependency | [Torsion roots](../ledger/Yin_L_G0462_v111.md#cofactor) | The circle argument and bound on the distinct torsion roots at both signs. |
| dependency | [Degree at repeated roots](Yin_C_G0899_v7.md#degree) | The derivative method for the excess multiplicity, extended here to both signs. |
| dependency | [Real order](../ledger/Yin_L_G0462_v111.md#ideals) | Passing a real cyclotomic unit and its inverse to the trace order. |


### Decision dyadic-trace-algebra-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-18T05:15 |
| status | proved |
| reason | Accept the trace ideal, residue fields and the separation of the two prime-order rates after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Trace ideal and finite quotient](#statement) | Both multinacci returns, the Salem factors, all selected prime divisors of the delay, the residue fields, and the two asymptotic rates. |
| argument | [Exterior root and torsion factors](#salem) | Both signs, the exterior interval and the degree bound including repeated roots. |
| argument | [Cyclotomic evaluation](#ideal) | The dyadic valuation survives cofactor removal and gives the exact trace ideal in the real order. |
| argument | [Frobenius orbits](#residue) | Separability, common residue degree and failure of integer evaluation. |
| argument | [Asymptotics and scope](#scope) | Convergence of the exterior root to two and the strict difference between resultant and common-modulus rates. |
| dependency | [Multinacci roots](Yin_C_G0021_v1.md#multinacci-local-roots-irreducibility-and-measure) | Irreducibility, the Pisot property and the locations of the conjugates. |
| dependency | [Exterior bracket](Yin_C_G0899_v7.md#salem) | The minus sign at the endpoints for all stated seed degrees and delays. |
| dependency | [Torsion roots](../ledger/Yin_L_G0462_v111.md#cofactor) | The circle argument and bound on the distinct torsion roots at both signs. |
| dependency | [Degree at repeated roots](Yin_C_G0899_v7.md#degree) | The derivative method for the excess multiplicity, extended here to both signs. |
| dependency | [Real order](../ledger/Yin_L_G0462_v111.md#ideals) | Passing a real cyclotomic unit and its inverse to the trace order. |
| review | [Independent review of the trace ideal](../audits/reviews/Yin_R_G1114_v105.md#dyadic-trace-ideal-whole) | Both signs, cofactor multiplicities, exact ideal, all residue degrees and the asymptotic regime. |

## Current assessment

[Selected decision](#decision-dyadic-trace-algebra-reviewed)
