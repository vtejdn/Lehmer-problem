---
author: Yin
---

# G0001: neutral rational symmetry and the integral metric obstruction

Date: 2026-10-06.
The current complete mathematical home is [the matrix realization and metric theorem](../claims/Yin_C_G0227_v1.md#argument), with [actual complete self-review](../audits/reviews/Yin_R_G0512_v1.md#current-matrix-realization-finding).
The original mathematical body remains here as its dated review input and substantive exploration.
This follows [L G0021](Yin_L_G0021_v1.md#symmetric-entropy-lift).
It locates which condition is lost when one tries to turn a totally real trace polynomial into a symmetric-matrix entropy model.
The construction is elementary, nonoptimal in dimension and not claimed novel.
It supplies a representation, not an entropy gap.

<a id="neutral-rational-symmetric-realization"></a>
## Direct construction

Let Q be monic, squarefree, in Z[y], of degree d, with all roots real.
In E=Q[y]/(Q), let T be the matrix of multiplication by y in the power basis.
Let H be the matrix of the bilinear trace form (u,v)->Tr_E/Q(uv).
Its entries are integers and HT=T^T H.
If theta_i are the distinct real roots, evaluation identifies

    v^T H v = sum_i v(theta_i)^2.

This is strictly positive for nonzero representatives of degree below d.
Thus H is positive definite.
Rational elimination gives H=L D L^T with L rational invertible and D diagonal with positive rational entries.
This is ordinary LDL decomposition; no irrational square roots are taken.

For completeness, a positive rational a/b with positive integers a,b is the sum of ab copies of (1/b)^2.
Applying this to each diagonal entry of D gives a rational rectangular matrix E0 with E0^T E0=D.
Set C=E0 L^T, of size N-by-d for some finite N.
Then C^T C=H, and C has rank d.
No bounded-dimension theorem or four-square theorem is needed.

Define

    A=C T H^(-1) C^T.

It is rational symmetric because TH^(-1)=H^(-1)T^T.
Moreover AC=CT, and A vanishes on ker(C^T).
The orthogonal decomposition

    Q^N = im(C) direct-sum ker(C^T)

holds over Q, since H is invertible.
Therefore

    chi_A(y)=Q(y)y^(N-d).

This exact characteristic polynomial is integral even though the entries of A need not be.
Put P(t)=t^d Q(t+t^(-1)).
For the rational symplectic matrix B_A=[[A,-I],[I,0]], the block calculation from L G0021 gives

    chi_B(t)=P(t)(t^2+1)^(N-d),
    h_alg(B_A on Q^(2N))=m(P).

The second equality uses the accepted rational entropy formula in the Task: its primitive characteristic polynomial is already monic integral.
There is no leading-coefficient penalty here.
Zero eigenvalues of A correspond to the roots +/-i of B_A, so they are neutral, not zero eigenvalues of the automorphism.

<a id="stable-lattice-metric-boundary"></a>
## What clearing denominators actually preserves

The polynomial yQ(y) annihilates A.
Consequently

    Lambda=sum_(j=0)^d A^j Z^N

is a full lattice in Q^N stable under A: it is finitely generated, has a common denominator, contains Z^N, and the highest power reduces using the monic integer relation.
In a Z-basis S of this lattice, A0=S^(-1) A S has integer entries.
Its characteristic polynomial and all entropy statements above are unchanged.

However the transported Euclidean metric is S^T S.
Multiply it by a positive integer to obtain a positive definite integral matrix G.
Then

    G A0=A0^T G.

This is self-adjointness for G, not ordinary symmetry A0=A0^T.
The block integer automorphism B_A0 preserves [[0,G],[-G,0]], which need not be unimodular; it has the same integral characteristic polynomial and entropy as B_A.
These operations do not guarantee that G can be changed to I by an integral orthogonal transformation.

In particular, the [explicit excluded Q from L G0021](Yin_L_G0021_v1.md#no-neutral-symmetric-completion) has such a neutral rational realization and such an integral G-self-adjoint realization.
If the latter could always be replaced by an ordinary symmetric integer matrix while preserving its neutral characteristic factors, it would contradict that record.
Thus the needed integral metric improvement is not automatic.
This refutes a representation shortcut, not a uniform gap for the broader G-self-adjoint class.

## A denominator sanity check

Entry denominators alone do not determine algebraic entropy.
For contrast, take the rational scalar A=(2+1/q), q>=2.
Its block automorphism has monic rational characteristic polynomial t^2-(2+1/q)t+1.
The primitive integer polynomial is

    q*t^2-(2q+1)*t+q.

Its roots are lambda_q and lambda_q^(-1), with lambda_q>1 and lambda_q->1, but its algebraic entropy is log(q)+log(lambda_q), not log(lambda_q).
Thus dropping the leading-coefficient term would manufacture a false small-entropy family.
The constructed neutral model above avoids this term because its characteristic polynomial itself, not merely its eigenvalues viewed as complex numbers, is monic integral.

## Scope, search and next action

The domain includes Salem trace polynomials and, more generally, squarefree totally real trace polynomials.
It excludes reciprocal polynomials whose trace roots are nonreal.
The rational realization is therefore not a reduction of the whole Lehmer problem to this subclass.

Local reuse checked L G0009's trace-form distinction, L G0021 and the Task's exact rational normalization.
Bounded searches on 2026-10-06 for rational symmetric characteristic polynomials, trace forms and sums of squares found known rational realization literature and Hillar's sums-of-squares paper.
These are attribution leads only; no result from an uninspected source is used.
The deliberately coarse construction above needs only rational elimination and the displayed sum-of-squares identity, so no stronger realization theorem or source acquisition is required for its proof.

The original2026-10-06 formal author check is retained at [its exact finding](../audits/reviews/Yin_R_G0512_v1.md#original-rational-lattice-check).
A useful next estimate must control the arithmetic of the metric/lattice or the entropy of an integral symmetric enlargement.
Mere rational symmetry is already available and supplies no new gap.
