---
author: Yin
---

# A small odd-part defect beyond quadratic Schur descendants

This is continuing author-side work for [G0001](../tasks/Yin_T_G0001_v1.md#contract), after the [gap for power-substitution descendants](../claims/Yin_C_G0345_v294.md#statement) at \(q=d^2\).
The exact identities below identify a next construction test; no stable integral candidate or new Salem output is asserted.
They have been checked during development, without an independent proof review.

<a id="odd-part"></a>
## The full parity decomposition

Use the [Schur correspondence](../claims/Yin_C_G0345_v293.md#correspondence), with \(d=2\ell+2\ge4\), \(q\ge2\), \(N=q^2-1\), \(L=N+j\), \(j\ge1\), and \(K=L^2-N^2\).
Write
\[
 B(z)=D(z^2)+zE(z^2),
\]
where \(D\in\mathbb Q[w]\) is monic of degree \(\ell\), and \(\deg E\le\ell-1\).
Reversal for \(D,V\) below uses formal degree \(\ell\); reversal for \(E,\Delta\) uses formal degree \(\ell-1\).
The full inverse is
\[
 \begin{split}
 f(z)&=U(z^2)-zV(z^2),\\
 U&=wD+qD^*-\frac LNw(qE+E^*),\\
 V&=\frac LN(qD+D^*)-(wE+qE^*).
 \end{split}                                                       \tag{1}
\]
Consequently an integral \(f\) has integral \(U,V\).
If \(S=[w^\ell]V\), the endpoint coefficients always satisfy
\[
                         V(0)=qS-L.                                \tag{2}
\]
Neither (1) nor strict stability of \(B\) alone makes \(D\) or \(V\) strictly stable.

For example \(B=(z-\tfrac12)^4\) is strictly stable, but its even part is
\(D(w)=w^2+\tfrac32w+\tfrac1{16}\).
Since \(D(-2)>0>D(-1)\), this \(D\) has a root outside the unit disk.
This example tests the stability implication only; it is not claimed to satisfy the full integral inverse conditions.

<a id="defect"></a>
## The exact integer defect

Define
\[
 \mathcal F(V)=(q^2-w)V^*+q(w-1)V.
\]
Substitution in (1) gives
\[
 \mathcal F(V)-LU=w\Delta,\qquad
 \Delta=\frac KN(qE+E^*)\in\mathbb Z[w],\qquad \deg\Delta\le\ell-1.     \tag{3}
\]
The integrality of \(\Delta\) follows from that of \(U,V\), cancellation of the constant term, and division by \(w\).
Moreover \(\Delta=0\) if and only if \(E=0\), since reversing \(qE+E^*=0\) and eliminating \(E^*\) gives \(NE=0\).

Conversely, start from integer \(V,\Delta\) of the indicated formal degrees, with (2) and
\[
                          \mathcal F(V)\equiv w\Delta\pmod L.
                                                                         \tag{4}
\]
Set
\[
 E=\frac{q\Delta-\Delta^*}{K},\qquad
 D=\frac{qV-V^*+NE^*}{L},\qquad
 U=\frac{\mathcal F(V)-w\Delta}{L}.                                  \tag{5}
\]
The polynomial \(D\) is monic of degree \(\ell\), by (2).
Reversal verifies (1) and (3).
If the reconstructed full polynomial \(B=D(z^2)+zE(z^2)\) is strictly stable, the Schur inverse yields an integral Pisot minimal polynomial of exactly degree \(d\) and constant \(q\).
Its positive exterior sign follows from \(A(1)=jB(1)>0\).
Thus strict stability must be imposed on the complete \(B\); replacing it by a condition on \(V\) would change this problem.

Evaluating (3) at one gives the necessary filter
\[
                         \gcd(N,j)\mid\Delta(1).                    \tag{6}
\]
Indeed \(\mathcal F(V)(1)=NV(1)\) and \(\gcd(N,L)=\gcd(N,j)\).

<a id="unit-defect"></a>
## A unit monomial defect has to occur at an endpoint

A first bounded test is
\[
                    \Delta=\varepsilon w^r,\qquad
 \varepsilon\in\{-1,1\},\qquad0\le r\le\ell-1.
\]
Equation (6) forces \(\gcd(N,L)=1\).
Reverse (3) in formal degree \(\ell+1\), use the elimination identity for \(\mathcal F\), and reduce modulo \(L\).
This gives
\[
 N^2V\equiv(q^2-w)\Delta^*-q(1-w)\Delta\pmod L.                      \tag{7}
\]
Since \(N\) is a unit modulo \(L\), (7) determines all residues of \(V\).
It does not determine its integer coefficients or imply stability.

Suppose now \(q=d^2\), \(d\ge6\), and \(0<\theta-q\le1\).
The trace of \(f\) is \(S=-[z^{d-1}]f\).
All other \(d-1\) roots have modulus less than one, so
\[
                      q-d+1<S<q+d<L.
\]
For \(0<r<\ell-1\), the coefficient of \(w^\ell\) on the right of (7) is zero.
This would make \(L\mid S\), contradicting the displayed interval.
Only the two endpoint positions remain:
\[
 \begin{array}{c|c|c}
 r & E & j^2 S\pmod L\\ \hline
 0 & \varepsilon(q-w^{\ell-1})/K & -\varepsilon\\
 \ell-1 & \varepsilon(qw^{\ell-1}-1)/K & \varepsilon q
 \end{array}                                                       \tag{8}
\]
The congruences use \(N^2\equiv j^2\pmod L\).
The condition \(d\ge6\) keeps the two endpoint cases distinct.

Each endpoint makes the coefficient of \(z^{2\ell-1}\) in \(B\) nonzero, beside its monic coefficient of \(z^{2\ell}\).
Thus its support-exponent differences have greatest common divisor one.
In any actual integral instance, the least common denominator of \(B\) is exactly \(K\): the [Schur formula](../claims/Yin_C_G0345_v293.md#descendant) makes every coefficient denominator divide \(K\), and the displayed \(E\) has a coefficient equal to \(1/K\) or \(-1/K\).
These properties only evade the earlier structural restrictions; they do not establish feasibility.

The next test is therefore to solve (4) at either endpoint in (8) and certify strict stability of the full \(B\).
The odd part has at most two terms, while \(D,V\) and \(f\) may remain dense.
Neither the earlier bounded-support obstruction nor the quadratic-model stability argument settles this full problem.
