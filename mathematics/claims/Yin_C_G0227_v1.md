---
author: Yin
---

# Exact neutral symmetric realizations, entropy overhead and integral metric rigidity

This owns the complete reusable arguments from the original2026-10-06 L21–L23, preserving their accepted-source and restricted-domain boundaries.
The original L retain substantive comparison, failed shortcuts and historical fixed inputs.

## Statement

Write M for multiplicative Mahler measure, m=log M, and let lambda_0 be the exact Lehmer number in MS12.
All matrix sizes N and polynomial degrees d below are positive integers.
For an ordinary symmetric integer A of size N, the integer symplectic automorphism B_A=[[A,-I],[I,0]] has characteristic polynomial R_A=t^N det((t+t^-1)I-A) and full algebraic entropy m(R_A).
If chi_A=Qr with monic integral factors of degrees d and N−d, then R_A=PC, P=t^dQ(t+t^-1), C=t^(N−d)r(t+t^-1), and its entropy is m(P)+m(C).
Thus m(C)<=a m(P), a>=0 and m(P)>0, implies m(P)>=log(lambda_0)/(1+a).

For Q0=y^7−8y^5+19y^3−12y+1 and P0=t^14−t^12+t^7−t^2+1, put tau=M(P0).
The accepted source gives1<tau<13/10 and excludes tau from its exact sixteen indecomposable matrix measures below13/10.
There is no ordinary symmetric integer A with chi_A=Q0 r and every root of r in[−2,2].
More generally each ordinary symmetric integer realization with Q0 dividing chi_A pays m(C)>=log(gamma/tau)>0, where gamma=min({13/10} union {v in F:v>tau}) for that exact finite catalogue F.
This is a conditional bound on any such realization, not an assertion that a realization exists or a substitution of rounded table values.
Tau is a measure, not a positive root of P0.

For every squarefree monic Q in Z[y] of degree d with all roots real, there is a finite N>=d and rational symmetric A with chi_A=Q(y)y^(N−d).
Its rational block automorphism has characteristic polynomial P(t)(t^2+1)^(N−d), P=t^dQ(t+t^-1), and entropy m(P).
It admits an A-stable full lattice in Q^N, giving an integral similar A0 and a positive definite integral metric G with GA0=A0^T G.
The integral B_A0 preserves [[0,G],[-G,0]], which need not be unimodular, and has the same entropy; no ordinary integral symmetry or uniformly conditioned integral basis is guaranteed.
In particular Q0 is squarefree totally real and has such neutral rational and integral-metric realizations, but no ordinary symmetric integer neutral realization.
For contrast the rational scalar A=2+1/q, integer q>=2, has primitive characteristic polynomial qt^2−(2q+1)t+q and entropy log q+log(lambda_q), although lambda_q decreases to1.
No irreducibility of this scalar polynomial is required.

For any integral A and positive real symmetric G with GA=A^T G, put kappa=lambda_max(G)/lambda_min(G) and rho=rho(A).
If2(kappa−1)/(kappa+1) sqrt(kappa) rho<1, then A=A^T.
If kappa<=3/2, then h_alg(B_A)=0 or h_alg(B_A)>=log(lambda_0), independently of N.
For every neutral integral Q0-model in every integral basis, each self-adjointness metric satisfies kappa>4/3.
These statements do not assert such a bound for arbitrary low-entropy objects, cover nonreal trace roots, or establish a gap for all integral G-self-adjoint matrices.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:42 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every positive matrix size, squarefree totally real monic integral trace polynomial, exact neutral completion, positive self-adjointness metric and stated condition-number bound; full entropy with natural logarithms, no rank normalization or whole-core realization claim. |
| argument | [Argument](#argument) | Complete block determinant/symplectic and product arguments, exact excluded-example overhead, rational LDL/sum-of-squares realization, stable integral lattice with transported metric, denominator penalty and both sharp norm thresholds, with local exact coarse Lehmer and seven-real-root checks. |
| dependency | [MS12 exact accepted spectrum](../audits/literature/MS12/Yin_U001.md#ms12-u001) | Exact Lehmer gap, sixteen indecomposable measures below13/10 and excluded Q/P pair; original classification and computations remain accepted external proofs. |
| dependency | [Rational entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Finite-dimensional rational Yuzvinski with the full primitive leading-coefficient contribution; original source inspection limits remain. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:44 |
| status | proved |
| reason | The complete registered theorem and every necessary argument have actual full current self-review at the exact accepted-source scope; all entropy, neutral-factor and metric-condition restrictions remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every positive matrix size, squarefree totally real monic integral trace polynomial, exact neutral completion, positive self-adjointness metric and stated condition-number bound; full entropy with natural logarithms, no rank normalization or whole-core realization claim. |
| argument | [Argument](#argument) | Complete block determinant/symplectic and product arguments, exact excluded-example overhead, rational LDL/sum-of-squares realization, stable integral lattice with transported metric, denominator penalty and both sharp norm thresholds, with local exact coarse Lehmer and seven-real-root checks. |
| dependency | [MS12 exact accepted spectrum](../audits/literature/MS12/Yin_U001.md#ms12-u001) | Exact Lehmer gap, sixteen indecomposable measures below13/10 and excluded Q/P pair; original classification and computations remain accepted external proofs. |
| dependency | [Rational entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Finite-dimensional rational Yuzvinski with the full primitive leading-coefficient contribution; original source inspection limits remain. |
| review | [Complete current self-review](../audits/reviews/Yin_R_G0512_v1.md#current-matrix-realization-finding) | Actual entire registered statement, complete proof and exact source interfaces, including the added elementary real-root and coarse-constant checks; no isolated or whole external classification proof certification. |

## Argument

The following exact elementary checks make the explicit example and coarse constants fully local; they do not add to the source's historical inspection scope.

### Exact real roots of the excluded trace polynomial

Q0(y)=y(y^2−1)(y^2−3)(y^2−4)+1.
At−3 and−2 its values are−719 and1, so it has a root in(−3,−2).
At−sqrt3,−sqrt2,−1 its values are1,1−2sqrt2,1, giving a root in each intervening interval.
At0,1/2,1 its values are1,−367/128,1, giving two further roots.
At sqrt3,sqrt(7/2),2 its values are1,1−(5/8)sqrt(7/2),1; the middle is negative since175/128>1, giving two further roots.
These seven disjoint intervals give all seven roots, hence squarefreeness, with one root below−2 and the other six in(−2,2).
This proves the hypothesis needed to apply the rational construction to Q0.

### Exact coarse bounds for the Lehmer root

For the Lehmer polynomial ell(t)=t^10+t^9−t^7−t^6−t^5−t^4−t^3+t+1, one has ell(t)/t^5=F(t+t^-1),

    F(y)=y^5+y^4−5y^3−5y^2+4y+3.

F(2)=−1, F'(2)=36, F''(2)=138 and F'''(y)>0 for y>=2, so F is strictly increasing there.
On[2,101/50], F'(y)<=5(101/50)^4+4(101/50)^3−76<41.
For t=23/20, y=929/460=2+9/460 lies in this interval, and F(y)<=−1+369/460<0.
For t=6/5, y=61/30=2+1/30 and F(y)>=−1+36/30>0.
The unique positive outer Lehmer root therefore satisfies23/20<lambda_0<6/5.
Consequently lambda_0^2>529/400>13/10 and lambda_0<6/5<sqrt(3/2), without any rounded catalogue value.

<a id="symmetric-entropy-lift"></a>
### The actual entropy-bearing automorphism

For an N-by-N symmetric integer matrix A set

    B_A = [[A,-I],[I,0]],   J=[[0,I],[-I,0]].

Block multiplication gives B_A^T J B_A=J.
Its inverse is [[0,I],[-I,A]], so it is an integer automorphism, and its determinant is 1.
The Schur-complement identity, first for t nonzero and then as a polynomial identity, gives

    det(tI-B_A)=t^N det((t+t^-1)I-A)=R_A(t).

The accepted rational entropy formula therefore gives h_alg(B_A)=m(R_A).
This is the entropy of the full 2N-dimensional automorphism, with no normalization by N.

If chi_A=Q*r for monic integer Q of degree d and monic integer r, define

    P=t^d Q(t+t^-1),   C=t^(N-d)r(t+t^-1).

Both are monic integer polynomials with constant coefficient 1, and R_A=P*C.
Hence

    h_alg(B_A)=m(P)+m(C).

Even when a desired algebraic number occurs among the eigenvalues of A, this only identifies a factor; it does not eliminate m(C).
If m(C)<=a*m(P) with fixed a>=0 and m(P)>0, the accepted matrix gap would give m(P)>=log(lambda_0)/(1+a).
Establishing such controlled overhead is an additional obligation.
Real symmetry also requires all roots of Q to be real, so this representation cannot automatically cover the full reciprocal core with nonreal trace roots.

<a id="no-neutral-symmetric-completion"></a>
### An explicit failure even allowing neutral padding

Take the source's exact pair

    Q(x)=x^7-8x^5+19x^3-12x+1,
    P(t)=t^7 Q(t+t^-1)=t^14-t^12+t^7-t^2+1.

Write tau=M(P).
The accepted source statement places 1<tau<1.3 and excludes tau from its sixteen matrix measures below 1.3.
The displayed approximation 1.20261 is only an identifier, not a new numerical certificate.
In particular, tau is a measure, not a claimed positive root of the displayed P; its sign pattern must be retained.

There is no symmetric integer A such that chi_A=Q*r and all roots of r lie in [-2,2].
Indeed that spectral condition gives m(C)=0, so M(R_A)=tau.
Permute A into indecomposable symmetric integer blocks.
Their reciprocal measures multiply.
Each noncyclotomic block has measure at least lambda_0; since lambda_0^2>1.3, there can be only one such block when the product is tau<1.3.
Its measure would be tau, contrary to Theorem4 and the explicit exclusion.
Here lambda_0 is the exact Lehmer root from Corollary2; the coarse inequality lambda_0^2>1.3 is far from the numerical boundary.
Thus adding arbitrarily many neutral eigenvalues cannot repair this example.

More generally, for any A with Q dividing chi_A, the extra entropy is bounded away from zero, provided such a realization is chosen.
Let F be the finite set of sixteen exact measures specified by the source's graph catalogue, and put

    gamma=min({13/10} union {v in F : v>tau}).

Then gamma>tau, and the same block argument shows M(R_A)>=gamma: below 1.3 there is at most one noncyclotomic block, its measure is in F, multiplicativity gives M(R_A)>=tau, and equality is excluded.
Consequently m(C)>=log(gamma/tau)>0.
No rounded table number is substituted for gamma, and no effective numerical overhead is claimed.

<a id="neutral-rational-symmetric-realization"></a>
### Direct construction

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
### What clearing denominators actually preserves

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

In particular, the [explicit excluded Q from L G0021](#no-neutral-symmetric-completion) has such a neutral rational realization and such an integral G-self-adjoint realization.
If the latter could always be replaced by an ordinary symmetric integer matrix while preserving its neutral characteristic factors, it would contradict that record.
Thus the needed integral metric improvement is not automatic.
This refutes a representation shortcut, not a uniform gap for the broader G-self-adjoint class.

### A denominator sanity check

Entry denominators alone do not determine algebraic entropy.
For contrast, take the rational scalar A=(2+1/q), q>=2.
Its block automorphism has monic rational characteristic polynomial t^2-(2+1/q)t+1.
The primitive integer polynomial is

    q*t^2-(2q+1)*t+q.

Its roots are lambda_q and lambda_q^(-1), with lambda_q>1 and lambda_q->1, but its algebraic entropy is log(q)+log(lambda_q), not log(lambda_q).
Thus dropping the leading-coefficient term would manufacture a false small-entropy family.
The constructed neutral model above avoids this term because its characteristic polynomial itself, not merely its eigenvalues viewed as complex numbers, is monic integral.

<a id="metric-rigidity"></a>
### Integer skew part versus a well-conditioned metric

Let A be an integer N-by-N matrix and G a real symmetric positive definite matrix such that GA=A^T G.
Write kappa=lambda_max(G)/lambda_min(G), and rho=rho(A).
All norms below are Euclidean operator norms.
The symmetric matrix S=G^(1/2) A G^(-1/2) satisfies ||S||=rho, so

    ||A|| <= sqrt(kappa)*rho.

Scale G by the midpoint of its smallest and largest eigenvalues, writing the result I+E.
Then

    ||E||=(kappa-1)/(kappa+1)=epsilon,
    A-A^T=A^T E-EA.

Consequently

    ||A-A^T|| <= 2 epsilon sqrt(kappa) rho.              (1)

A nonzero integer matrix has operator norm at least one, since some entry has absolute value at least one.
Therefore

    2*(kappa-1)/(kappa+1)*sqrt(kappa)*rho < 1
       implies A=A^T.                                  (2)

No bound on N, integrality of G, or determinant condition on G is needed.
The condition is invariant under multiplying G by a positive scalar, but is not invariant under arbitrary integral changes of basis.

<a id="conditioned-matrix-gap"></a>
### A dimension-independent restricted entropy gap

Let R_A(t)=t^N det((t+t^(-1))I-A), which is monic integral and reciprocal.
Its measure M=M(R_A) is at least one.
Since the eigenvalues theta of A are real, their reciprocal quadratic factors show

    rho <= M+M^(-1).

Indeed, for |theta|<=2 this follows from M+M^(-1)>=2.
Otherwise the corresponding factor has measure u>1 with |theta|=u+u^(-1), and u<=M.

If kappa<=3/2 and M<sqrt(3/2), then epsilon<=1/5 and monotonicity of x+x^(-1) on [1,infinity) gives

    2 epsilon sqrt(kappa) rho
      < (2/5)*sqrt(3/2)*(sqrt(3/2)+sqrt(2/3)) = 1.

Thus A is an ordinary integer symmetric matrix.
MS12 supplies M=1 or M>=lambda_0, where lambda_0 is Lehmer's number.
If instead M>=sqrt(3/2), the same lower bound already holds because lambda_0<sqrt(3/2).
Hence every such conditioned model satisfies

    h_alg([[A,-I],[I,0]])=0 or >=log(lambda_0).           (3)

The exact entropy identity is the characteristic-polynomial calculation in L G0021.
There is no rank normalization.
Equation (3) is not an unconditional gap for G-self-adjoint integer matrices: L G0022 gave no upper bound on kappa in an integral basis.

### A quantitative obstruction for the existing excluded example

For the P,Q of [L G0021](#no-neutral-symmetric-completion), consider any integral model A with chi_A=Q*r and neutral r, and any positive metric G making A self-adjoint.
If kappa<=4/3, then M(R_A)=M(P)<13/10 and

    2 epsilon sqrt(kappa) rho
       < (2/7)*(2/sqrt(3))*(13/10+10/13)
       = 538/(455*sqrt(3)) < 1.

It would follow that A is symmetric, contradicting L G0021.
Thus every such neutral integral model, in every integral basis, has kappa(G)>4/3 for every self-adjointness metric.
This uses only the accepted exact upper bound M(P)<1.3, not rounded table entries.
It gives a real obstruction to attempting to improve the L G0022 metric arbitrarily close to Euclidean; it does not show that condition numbers must diverge along a hypothetical vanishing-entropy family.

### Precise retained domains

The scalar parameter q in the denominator example is an integer at least2; all characteristic polynomials and entropy formulas concern the complete automorphism.
The metric bound is Euclidean in the chosen integral basis and invariant under positive rescaling of G, but not arbitrary changes of integral basis.
No graph classification, primary-source proof audit, numerical experiment or new research execution is used.
