---
author: Yin
---

# The radical closure of the two Chebyshev units

2026-11-24T19:20 UTC.

<a id="statement"></a>
## The least measure and the relative unit index

Use the [Chebyshev construction](Yin_C_G0902_v1.md#minimum) with \(q\) sufficiently large, \(p=q+1\), \(M=pq\), \(L=p+q\), and even \(n\ge4\) satisfying \(4^{n-1}\le2M\).
Its positive trace root \(w<1/M\) gives \(T+T^{-1}=2+w\), \(T>1\), and \(Y=(pT-q)/(p-qT)\).
Write \(B=\mathbb Q(w)\), \(K=\mathbb Q(T)\), \(U=\ker(N_{K/B}:\mathcal O_K^\times\to\mathcal O_B^\times)\), and \(H=\langle T,Y\rangle\).
Let
\[
 \mathcal R=\{\gamma\in\overline{\mathbb Q}^{\times}:
                 \gamma^r\in\mu_\infty H\text{ for some positive integer }r\}.
\]
The index \(I=[U:\{\pm1\}H]\) is finite.
The least positive total logarithmic Mahler measure \(\mu\) in \(\mathcal R\) is attained in \(U\).

Take the distinguished real embedding and one embedding \(\sigma:K\hookrightarrow\mathbb C\) over the nonreal trace place, chosen so \(|\sigma(T)|>1\).
For each nontorsion \(u\in U\),
\[
 [K:\mathbb Q(u)]\in\{1,3\},\qquad
 m(u)=\frac{|\log|u||+2|\log|\sigma u||}{[K:\mathbb Q(u)]}.
\]
Index three requires \(3\mid n\).
Consequently for \(3\nmid n\) every nontorsion relative unit has degree \(2n\), and the two logarithms account for all of its exterior conjugates.

Put \(\lambda(u)=(\log|u|,\log|\sigma u|)\) and \(D_H=|\det(\lambda(T),\lambda(Y))|\).
The bounds
\[
       \frac{m(T)}I\ \le\ \mu\ \le\ 2\sqrt{D_H/I},\qquad
       D_H\sim\tfrac12(n-1)(\log M)^2                                      \tag{1}
\]
hold uniformly over the indicated degrees as \(q\to\infty\).
In particular \(I/(n(\log M)^2)\to\infty\) would suffice for a sequence with positive measures tending to zero, whereas such a sequence in this radical closure requires \(I/\log M\to\infty\).
The index growth in this sufficient condition remains open.

<a id="fields"></a>
## Neutral places and the degree of each unit

The [trace-root calculation](Yin_C_G0902_v1.md#conjugates) gives \([B:\mathbb Q]=n\), with the root \(w>0\), \(n-3\) roots in \((-4,0)\), and one conjugate nonreal pair.
In \(K/B\) the involution \(\iota\) takes \(T,Y\) to their inverses, the real place of \(w\) splits into two real embeddings, and each real trace in \((-4,0)\) gives a complex conjugate pair.
The nonreal trace pair gives two embeddings over either member and their complex conjugates over the other.
A unit \(u\in U\) has modulus one at the \(n-3\) neutral pairs.
The real split pair has opposite logarithms, as do the two extensions at either nonreal trace embedding.
Complex conjugation duplicates the latter pair.
These are the [relative-unit logarithm coordinates](Yin_C_G0345_v75.md#cyclic) for this signature.
An algebraic integer in this fixed field with bounded logarithms at both selected embeddings has bounded conjugate moduli and hence belongs to a finite set.
Thus \(\lambda(U)\) is discrete, and its kernel consists of roots of unity, which in the distinguished real field \(K\) are just \(\{\pm1\}\).
The [independence of \(T,Y\)](Yin_C_G0902_v1.md#products) makes their two vectors a rank-two sublattice of finite index in \(\lambda(U)\), since discreteness prevents two independent group elements from spanning a real line.
In particular \(\operatorname{covol}\lambda(U)=D_H/I\).

At the real split pair any nontorsion \(u\in U\) contributes exactly one exterior embedding, as a real value of modulus one would be \(\pm1\).
Suppose \(|\sigma u|=1\).
There would be exactly one exterior embedding among all \(2n\) embeddings of \(K\), counted with multiplicity.
The number of exterior embeddings of \(K\) is \([K:\mathbb Q(u)]\) times the number of exterior conjugates of \(u\), so \(K=\mathbb Q(u)\).
But \(\sigma(\iota u)=(\sigma u)^{-1}=\overline{\sigma u}\) would then imply \(\sigma\circ\iota=\overline{\sigma}\) on \(K\).
Its fixed field \(B\) would map into \(\mathbb R\) under the chosen nonreal trace embedding, a contradiction.
Hence the nonreal trace place contributes exactly two exterior embeddings.
The field index therefore divides three, and the sum of positive logarithms over \(K\) gives the stated formula.
Since \([K:\mathbb Q]=2n\), if the index is three then \(3\mid n\).
In that case \(u\) has exactly one exterior conjugate, necessarily real, and its reciprocal is its only interior conjugate.

<a id="radicals"></a>
## Reduction of arbitrary radicals to the trace extension

Every element of \(U\) belongs to \(\mathcal R\) because \(I\) is finite.
For the other direction let \(\gamma\in\mathcal R\) be nontorsion and absorb its torsion factor into the exponent, obtaining \(\theta=\gamma^r\in H\).
Then \(\gamma\) and its inverse are algebraic integers since powers of both are algebraic integers.
Put \(F=\mathbb Q(\theta)\subset K\), \(s=[\mathbb Q(\gamma):F]\), and \(v=N_{\mathbb Q(\gamma)/F}\gamma\).
The identity \(v^r=\theta^s\) gives \(h(v)=s h(\gamma)>0\), so
\[
                       m(\gamma)=[F:\mathbb Q(v)]m(v).
\]
Here \(h\) denotes absolute logarithmic height.
The unit \(v\in F\) has \(N_{K/B}(v)^r=1\) since \(\theta\in H\).
Its norm is thus a real root of unity in \(B\).
At any one of the \(n-3\ge1\) neutral real places of \(B\) this norm is a positive squared modulus, forcing it to equal \(+1\).
Therefore \(v\in U\) and \(m(v)\le m(\gamma)\).
The positive minimum in \(U\) exists by bounded degree and the finiteness of monic integer polynomials of bounded degree and measure.
This proves equality of the two minima, taking account of potential proper subfields in the norm descent.

<a id="index"></a>
## Lattice area and an index test

For \(u\in U\) nontorsion, \(u^I\) is \(\pm1\) times a nontrivial element of \(H\).
The [minimum in the two-generator group](Yin_C_G0902_v1.md#minimum) therefore gives \(m(T)\le m(u^I)\le I m(u)\).
In \(\mathbb R^2\) the diamond \(|x|+2|y|\le t\) has area \(t^2\).
Minkowski's convex body theorem on \(\lambda(U)\), followed by discreteness at equality, yields a nonzero lattice point with \(|x|+2|y|\le2\sqrt{D_H/I}\).
The degree formula gives the upper bound in (1).

For the determinant asymptotic use \(d_0=n-3\) and \(C_{d_0}\) from the Chebyshev construction.
Put \(\delta=1-Mw\), so that the exact polynomial equation gives
\[
       \delta=\frac{w^{n-1}(w+4)}{2C_{d_0}(w)},\qquad
       Y+Y^{-1}-2=\frac{2L^2 C_{d_0}(w)}{(w+4)w^{n-2}} .
\]
Write \(2+w=2\cosh t_0\).
The [small-root estimate](Yin_C_G0902_v1.md#conjugates) gives \(w=M^{-1}+O(M^{-n})\) and \(t_0=M^{-1/2}+O(M^{-3/2})\).
Since \(n=O(\log M)\), the formula \(U_j(\cosh t_0)=\sinh((j+1)t_0)/\sinh t_0\) gives \(C_{d_0}(w)=(2d_0+1)(1+O(n^2/M))\).
It follows uniformly that
\[
   \log Y=(n-1)\log M+\log(2(2d_0+1))+O(n^2/M).
\]
At the chosen complex embedding [the two unit estimates](Yin_C_G0902_v1.md#products) give
\(\log|\sigma T|=\frac12\log(2M)+O(n^2/M)\) and \(\log|\sigma Y|=O(M^{-1/2})\).
Expanding the absolute determinant now gives (1).

<a id="parity"></a>
## The two-primary obstruction to a large index

The parity of the index is determined by
\[
                         2\mid I\quad\Longleftrightarrow\quad
                                     \delta\in B^{\times2}.               \tag{2}
\]
Indeed a positive real \(z\in U\) is a square modulo signs in \(U\) exactly when \(z+z^{-1}+2\) is a square in \(B\).
One implication follows from taking the square of \(v+v^{-1}\) for \(v^2=z\), since a negative real number cannot be a square in \(K\).
Conversely for \(s\in B^\times\) with \(s^2=z+z^{-1}+2\), the element \(v=(1+z)/s\) satisfies \(v^2=z\) and \(N_{K/B}v=1\).
It is a unit since both it and its inverse have integral squares.

Here \(T+T^{-1}+2=w+4\), of norm \(H_{\rm tr}(-4)=2L^2\) in \(B/\mathbb Q\), where \(H_{\rm tr}\) denotes the degree-\(n\) trace polynomial.
This evaluation uses \(n\) even and \(C_{d_0}(-4)=-1\).
Also \(N_{B/\mathbb Q}\delta=L^2\) by [evaluation at \(1/M\)](Yin_C_G0902_v1.md#products), and
\[
 Y+Y^{-1}+2=(w+4)/\delta,\qquad
 TY+(TY)^{-1}+2=(2+pw)^2/\delta .
\]
The last identity follows by multiplying \(1+TY=T(2+pw)/(p-qT)\) by its inverse-place conjugate.
Thus neither \(T\) nor \(Y\) has square class zero in \(U/\{\pm1\}\), since the two trace norms are \(2L^2\) and \(2\).
Their classes span the two-dimensional reduction of this free rank-two group modulo two unless \(TY\) has square class zero.
This proves (2).

If \(v_2(M)=1\), the unique place of \(B\) above two has normalized valuation \(v(w)=1,\ v(2)=n\), since \(H_{\rm tr}\) is Eisenstein at two.
The residue field is \(\mathbb F_2\).
If \(\delta=x^2\) there, then \(v(x)=0\) and \(x=1+s\) with \(v(s)\ge1\).
When \(v(s)<n\), the valuation of \(x^2-1=s(2+s)\) is the even integer \(2v(s)\).
When \(v(s)\ge n\), it is at least \(2n\).
Neither equals \(v(\delta-1)=n+1\), which is odd and smaller than \(2n\).
For these \(q\), equivalently \(q\equiv1,2\bmod4\), the index \(I\) is odd.

## Assessment history

### Decision chebyshev-relative-unit-index

| Field | Value |
| --- | --- |
| date | 2026-11-24T19:30 |
| status | proved |
| reason | The relative norm descends every radical to the rank-two relative unit group. Counting the exterior embeddings fixes the degree factor, and the logarithm lattice and square tests yield the index bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The minimum in the radical closure, the two possible field indices, the index estimates and the parity test. |
| argument | [fields](#fields) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [radicals](#radicals) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [index](#index) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [parity](#parity) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0902_v1.md#minimum) | The unpowered subgroup minimum. |
| dependency | [Input](Yin_C_G0902_v1.md#conjugates) | The trace signature and local behavior. |
| dependency | [Input](Yin_C_G0902_v1.md#products) | The two generator estimates. |
| dependency | [Input](Yin_C_G0345_v75.md#cyclic) | Discreteness and multiplicities in the relative-unit coordinates. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1062.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-chebyshev-relative-unit-index)
