---
author: Yin
---

# The quadratic Schur descendant and its remaining integral coefficient problem

This is continuing author-side work for [G0001](../tasks/Yin_T_G0001_v1.md#contract), following the power-substitution restriction in [C345v293](../claims/Yin_C_G0345_v293.md#substitution).
It studies the surviving special model \(B=D(z^2)\), not all possible Schur descendants.
The calculations below have been checked within the developing argument and have not received an independent proof review.
Their unresolved purpose is to construct an actual integral stable polynomial or obtain an obstruction uniform in this model.

<a id="quadratic-model"></a>
## The half-degree stable polynomial

Use \(N=q^2-1\), \(L=N+j\), \(0<j<q-1\), and even \(d\ge4\).
Put \(\ell=(d-2)/2\), and suppose \(D\in\mathbb Q[w]\) is monic of degree \(\ell\), with every root strictly inside the unit disk.
For \(B(z)=D(z^2)\), the inverse in C345v293 becomes
\[
 f(z)=U(z^2)-zV(z^2),\qquad
 U(w)=wD(w)+qD^*(w),\qquad
 V(w)=\frac LN\bigl(qD(w)+D^*(w)\bigr),                         \tag{1}
\]
where the stars use degree \(\ell\).
Thus the full integrality requirement is precisely \(U,V\in\mathbb Z[w]\); the parity classes do not mix.
The polynomial \(V\) is strictly stable, by Rouché applied to \(qD+D^*\).
The polynomial \(U\) has all roots strictly outside the unit disk, since on the circle \(q|D^*|>|wD|\), and \(D^*\) has no zeros inside.
A reduction in degree alone therefore leaves two simultaneous integer polynomials with opposite strict root conditions.

For an integral instance, write \(S\) for the leading coefficient of \(V\).
Since \(|D(0)|<1\),
\[
 \frac LN(q-1)<S=\frac LN(q+D(0))<\frac LN(q+1).
\]
Our restriction \(0<j<q-1\) makes the left endpoint greater than \(q-1\) and the right endpoint less than \(q+2\).
Therefore
\[
 S\in\{q,q+1\},\qquad
 V(0)=qS-L,\qquad
 D(0)=
 \begin{cases}
 -qj/L,&S=q,\\
 (N-qj)/L,&S=q+1.
 \end{cases}                                                     \tag{2}
\]

The odd and even coefficients of \(A=LzD(z^2)-ND^*(z^2)\) are disjoint.
If \(A\) is integral, the primitive denominator \(c\) of \(D\) divides both \(L\) and \(N\), hence
\[
                         c\mid\gcd(N,j).                          \tag{3}
\]
In particular (2), together with the integrality of \(ND(0)\), requires
\[
 L\mid
 \begin{cases}
 qj^2,&S=q,\\
 (q+1)j^2,&S=q+1.
 \end{cases}                                                     \tag{4}
\]
Modulo \(L\), these are equivalently \(L\mid qN^2\) or \(L\mid(q+1)N^2\).
These are necessary scalar conditions, not sufficient stability or full-integrality conditions.

<a id="coefficient-problem"></a>
## Exact congruences on the smaller stable polynomial

The smaller polynomial itself supplies a useful exact formulation.
Given \(V\in\mathbb Z[w]\) of degree \(\ell\), leading coefficient \(S\), constant \(qS-L\), and strict disk stability, set
\[
 D=\frac{qV-V^*}{L},\qquad
 U=\frac{(q^2-w)V^*+q(w-1)V}{L}.                                  \tag{5}
\]
Then \(D\) is monic and strictly stable by Rouché.
Reversal verifies (1), so the resulting \(f\) is integral precisely when
\[
             (q^2-w)V^*+q(w-1)V\equiv0\pmod L                    \tag{6}
\]
coefficientwise.
When (6) holds, (1) and the strict Schur correspondence give an integral Pisot minimal polynomial of degree \(d\) and constant \(q\).
The positive exterior sign follows from \(A(1)=(L-N)D(1)>0\).

Reversing the numerator in (6) in formal degree \(\ell+1\), and eliminating \(V^*\), gives
\[
                             N^2wV\equiv0\pmod L.
\]
Consequently every coefficient of \(V\) is divisible by
\[
                         h=\frac{L}{\gcd(L,N^2)}.                 \tag{7}
\]
This recovers (4) from the leading coefficient \(S\), but (6) remains the complete additional restriction.
For \(V=hW\), it is a congruence modulo \(L/h\) on an integral stable \(W\) with leading coefficient \(S/h\).

<a id="scalar-witness"></a>
## A scalar admissible instance and the unresolved test

The scalar conditions need not be empty below \(j=q\).
For \(d=34\), take
\[
 q=1156,\quad N=1336335,\quad j=715,\quad L=1337050,\quad S=q.
\]
Here \(\gcd(N,j)=715\), \(D(0)=-34/55\), and \(qj^2=442L\).
Equation (7) gives \(h=34\).
An actual instance of this quadratic model would therefore require a strictly stable integer polynomial \(W\) of degree \(16\), leading coefficient \(34\), constant \(-21\), and
\[
      (1156^2-w)W^*+1156(w-1)W\equiv0\pmod{39325}.                 \tag{8}
\]
No polynomial satisfying all these conditions has been produced here.
The scalar witness is not a Pisot or Salem witness, and its branch ratio is not a near-zero sequence.

The next discriminating question is whether the congruence (6) and strict stability can coexist when \(q=d^2\) and \(j/q\to0\).
Solving only (4), enlarging a continuous stable region, or matching a finite moment prefix does not settle that question.
A finite exact search must enforce (6) and certify every root condition; a numerical root estimate or an unexamined modular solution is insufficient.
