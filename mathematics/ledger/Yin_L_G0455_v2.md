---
author: Yin
---
# Minimal weighted invariant extension at three rotations

Date: 2026-11-06.
This is a bounded continuation of the [joint-evaluation comparison in L455 v1](Yin_L_G0455_v1.md#joint-evaluation-test) under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The bottleneck_diagnosis contributor derived the integer-module comparison and performed the exact finite calculation as author work for Yin.
No formal independent review, new Claim assessment or unrestricted gap conclusion is claimed.
The earlier v1 remains fixed; its smoothing, coordinate-kernel and rational-evaluation arguments are not restated or revised here.

The question is whether adjoining the missing invariant double difference supplies additional mod-4 or mod-8 information beyond the already explicit Boolean factors.
The calculation constructs the smallest polynomial module containing that double difference and tests two actual weighted windows on the existing quartic control.
Its native evidence is [J137](../computations/programs/Yin_J_G0137/readme.md).

<a id="q3-minimal-invariant-module"></a>
## The actual integer module

Reuse [L445's integral germs and private-branch independence](Yin_L_G0445_v1.md#rotated-radicals) at their retained author/source scope.
Let P be monic, irreducible, reciprocal and noncyclotomic, with constant coefficient one, degree d, and preservation of degree under every positive power of a root.
Set U=P_2, V=P_4, F=sqrt(UV), with constant coefficient one and F/U=1+2h for h in Z[[x]].
Fix a primitive cube root zeta and write U_j=U(zeta^j x), F_j=F(zeta^j x) for j=0,1,2.
The eight mask products are independent over Q(zeta)(x).
Put
\[
 S=F_1+F_2,\quad T=F_1F_2,\quad
 R=\zeta F_1+\zeta^2F_2,\quad C=U_1U_2.
\]
All four series are Galois invariant, and their coefficients are algebraic integers, hence rational integers.
The old module is
\[
 \mathcal L_0=\mathbb Z[x]\langle1,F_0,S,T,F_0S,F_0T\rangle.
\]

Decompose the integer polynomial U uniquely as
\[
 U(x)=u_0(x^3)+x u_1(x^3)+x^2u_2(x^3),
\]
and define
\[
 A=u_0(x^3)-x^2u_2(x^3),\qquad
 B=xu_1(x^3)-x^2u_2(x^3).
\]
Then
\[
 U_1=A+\zeta B,\quad U_2=A+\zeta^2B,\quad
 C=A^2-AB+B^2,
\]
with deg A,deg B at most d and deg C at most 2d.
Writing delta_j=F_j-U_j and delta_12=delta_1 delta_2 gives the exact identity
\[
 \delta_{12}=T-(A-B)S+B R+C.                         \tag{Q1}
\]
Indeed U_2F_1+U_1F_2=(A-B)S-BR.

Consequently the smallest Z[x]-module containing the old module and delta_12 is
\[
 \boxed{\mathcal L_7=\mathcal L_0+\mathbb Z[x]\delta_{12}
                    =\mathcal L_0+\mathbb Z[x]BR.}  \tag{Q2}
\]
If B=0 there is no added direction, since delta_12 already belongs to the old module.
For B nonzero, the seven displayed generators are independent over Q(x): in the full independent mask basis, R has coefficients zeta,zeta^2 on F_1,F_2, whereas every element of the old rational span has equal coefficients there.
Thus adjoining delta_12 adds exactly one rational direction.
Replacing BR by R would enlarge the polynomial module unless the needed division by B were separately justified.
No such division, coefficient saturation or additional F_0 delta_12 generator is made here.
The full invariant eight-dimensional mask lattice also contains the separate direction F_0R; this calculation does not claim to close that larger module under multiplication by F_0.

<a id="q3-weighted-window"></a>
## Weighted finite lattice and explicit factors

The remainder of the seven-generator comparison assumes B is nonzero.
For a positive integer N, use the ordered generators
\[
 (f_0,\ldots,f_6)=(1,F_0,S,T,F_0S,F_0T,\delta_{12})
\]
and weights
\[
 (w_0,\ldots,w_6)=(0,d,d,2d,2d,3d,2d).
\]
Define the finite free integer lattice
\[
 \mathcal L_{7,N}
   =\bigoplus_{i=0}^6\ 
      \bigoplus_{0\le j<(N-w_i)_+}\mathbb Z\,x^jf_i. \tag{Q3}
\]
This definition charges the new direction weight 2d rather than treating it as an unweighted extra orbit sum.
Equation (Q1) replaces delta_12 by BR within this same weighted lattice: the coefficients of S and 1 have degrees at most d and 2d, respectively, and the inverse replacement obeys the same bounds.
The exact column count is
\[
 D_N=N+2(N-d)_++3(N-2d)_++(N-3d)_+,
\]
so the extension adds exactly (N-2d)_+ columns to the old weighted window.
For N at least 3d, D_N=7N-11d.

Put U_sum=U_1+U_2=2A-B and delta_sum=delta_1+delta_2=S-U_sum.
The following ordered generators give another basis of the same finite integer lattice:
\[
 (g_0,\ldots,g_6)=
 (1,\delta_0,\delta_{\rm sum},T-C,
       \delta_0\delta_{\rm sum},\delta_0(T-C),\delta_{12}). \tag{Q4}
\]
The change from f to g is polynomial unitriangular.
For example delta_0 delta_sum=F_0S-U_sum F_0-U_0S+U_0U_sum, and delta_0(T-C)=F_0T-CF_0-U_0T+U_0C.
Every coefficient has degree at most the difference of the corresponding weights, and the inverse change has the same property.
Therefore the induced change of finite monomial bases in (Q3) is unimodular over Z, without enlarging N.

Since delta_j=2U_j h(zeta^j x), the seven columns in (Q4) have the explicit binary exponents
\[
 (e_0,\ldots,e_6)=(0,1,1,1,2,2,2).                 \tag{Q5}
\]
For the fourth generator, use T-C=U_1 delta_2+U_2 delta_1+delta_1 delta_2.
The invariant quotients g_i/2^{e_i} again have integral coefficients: they are Galois invariant and have coefficients integral over Z after the displayed factor extraction.
The complete explicit full-minor exponent is
\[
 V_N=2(N-d)_++5(N-2d)_++2(N-3d)_+,                 \tag{Q6}
\]
which equals 9N-18d for N at least 3d.
This is only a guaranteed contribution for general inputs; the normalized residual matrix could have further divisibility.
In particular no division by four is used to adjoin delta_12/4 to the original lattice for free.

<a id="finite-normalized-evaluation"></a>
## Exact normalized finite evaluation

Take the same quartic as L455 v1:
\[
 P(t)=t^4-t^3-t^2-t+1,\quad
 U=1-3x+x^2-3x^3+x^4,\quad
 V=1-7x-15x^2-7x^3+x^4.
\]
Here A=1-x^2-3x^3 and B=x^4-x^2-3x are explicit nonzero integer polynomials, so (Q2) is genuinely a seven-dimensional extension.
The Phi_5 reduction of this quartic belongs to an already covered positive-gap class; it is not evidence for near-zero coverage.

For M rows define
\[
 E_{M,N}[n,(i,j)]=[x^{n-j}]g_i,
 \qquad 0\le n<M,\quad0\le j<(N-w_i)_+,
\]
with negative coefficient indices interpreted as zero and columns ordered first by i, then j.
Let H_{M,N} be the integer matrix obtained by dividing its (i,j)-column by 2^{e_i}.
The [native exact program](../computations/programs/Yin_J_G0137/verify.py) reconstructs all entries from the constant-one recurrence for F^2=UV, using only integer arithmetic and elimination over F_2.
It checks the divisibility of every computed generator coefficient, the following row certificates, and full binary column rank.
The original calculation generated 96 coefficients; all decisive entries occur by order 48, and the retained native program recomputes precisely that sufficient prefix.

| N | M | Columns | Rank of H over F_2 | Rows of an odd full-column minor | Original dyadic Smith exponents |
| --- | --- | --- | --- | --- | --- |
| 9 | 25 | 22 | 22 | 0 through 18, then 21,22,24 | 0 repeated 9 times; 1 repeated 11 times; 2 repeated 2 times |
| 13 | 49 | 47 | 47 | 0 through 45, then 48 | 0 repeated 13 times; 1 repeated 23 times; 2 repeated 11 times |

The corresponding total valuations are V_9=15 and V_13=45.
To justify the complete dyadic profiles rather than only a determinant bound, write E=H diag(2^{e_i}), repeating each exponent for its allowed shifts.
The certified odd full-column minor makes H a split full-column injection over Z_2.
Invertible row operations over Z_2 therefore reduce H to an identity block followed by zeros, and reduce E to the displayed powers of two followed by zeros.
The unimodular finite basis change (Q4) transfers this result back to the actual original lattice (Q3).
Thus the stated complete rectangular evaluations have exactly the listed dyadic Smith exponents.
There is no additional residual mod-2 loss and no exponent at least three in either map.
This does not assert that every selected square minor has the same valuation.

<a id="q3-outcome-and-limits"></a>
## Outcome and limits

The missing invariant direction has now been placed in a concrete integer module with its coefficient multiplier, finite window and new column count paid.
On the two actual quartic windows, every dyadic gain is explained by the explicit factors in (Q5); the newly admitted double difference supplies no further mod-4 or mod-8 relation in the complete evaluated lattice.
This closes only this finite test, not the general joint Smith-profile question for other original inputs or windows.
It gives no asymptotic upper bound for all normalized residual valuations.

The new generator still uses both original rotations and the multiplier B in (Q1), with degree up to d.
The elementary bound |delta_12| <= (|F_1|+|U_1|)(|F_2|+|U_2|) does not give an improved complex-place price from small total Mahler measure.
No favorable capacity, all-input arithmetic supply or near-zero sequence follows from the enlarged lattice.
A reason to revisit this small complementary test would be an actual candidate input from the main construction direction with residual divisibility not explained by these factors, followed by a complete original-input arithmetic and complex-place comparison.
Neither a finite extra digit in a specially chosen minor nor replacing BR by R without its cost would supply that comparison.
