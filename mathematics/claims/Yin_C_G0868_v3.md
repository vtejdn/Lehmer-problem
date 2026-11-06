---
author: Yin
---

# Matrix analytic damping and exact original-input realization costs

This project deduction extends C868's integer analytic-germ mechanism to square matrix functions and tests two concrete original-input realizations.
The dimension-independent estimate uses the total logarithmic determinant price of the multiplier, not a price divided by matrix size.
This version's mathematical status and evidence are owned by the selected assessment below.
Its own whole-proof finding supplies the matrix review; predecessor findings retain their original scopes.

## Inputs and retained scope

[C868 v1](Yin_C_G0868_v1.md#statement) retains AM1-AM2 and CG1-CG5 with their exact scalar and cyclotomic hypotheses and [selected assessment](Yin_C_G0868_v1.md#decision-whole-independent-review-2026-11-05).
[C868 v2](Yin_C_G0868_v2.md#statement) retains GM1-GM2 and RG1-RG6, its general reciprocal-block domain and [selected assessment](Yin_C_G0868_v2.md#decision-whole-general-block-review-2026-11-05).
Those fixed results are unchanged; the matrix statements below have their own hypotheses and proof.
The scalar finite-germ comparison is the [v2 first-crossing argument](Yin_C_G0868_v2.md#germ-first-crossing), not an assumption that the full meromorphic matrix germ lies in H2.
The [original-input tests in L133 v6](../ledger/Yin_L_G0133_v6.md#reciprocal-ratio-comparison) explain why the scalar ratio P*/P degenerates on reciprocal inputs.
That ledger is motivation, not a missing proof of the matrix assertions below.

Only the fixed positive-measure companion control uses an adopted external-data interface through [C227](Yin_C_G0227_v1.md#statement): its exact polynomial P0 and the bound 1<M(P0)<13/10.
The comparison retains [C227's selected scope](Yin_C_G0227_v1.md#decision-complete-retained-proof-adoption), including the MS12 source limits, without a new numerical or original-source check.
The matrix-germ, companion identities and rational-pole rigidity are proved directly here.

## Statement

Let D be the open unit disk, T its boundary with normalized Haar measure, and r>=1 a matrix size.
For a complex matrix X, X* denotes conjugate transpose and ||X||op its Euclidean operator norm.
All logarithms are natural.
Put

    c_mat=(1/2)log(5/4)>0.

### M1. Matrix integer germs and a total determinant price

Let F be a matrix-valued analytic germ at0 with

    F(z)=I_r+sum_(n>=1) C_n z^n,       C_n in M_r(Z).

Suppose Q and U are holomorphic on D and satisfy

    ||Q(z)||op<=1,       ||U(z)||op<=1       for z in D,
    Q0:=Q(0) is invertible,
    U=FQ on a neighborhood of0,
    tau=-log|det Q0|.                                      (M1)

Then tau>=0.
If F is not the constant germ I_r, and N is its first positive index with C_N nonzero, then

    ||C_N||op<=2sqrt(exp(2tau)-1),
    tau>=(1/2)log(1+||C_N||op^2/4)>=c_mat.                 (M2)

The constant is independent of r and N.
No continuation of F itself throughout D, no boundary H2 assumption on F and no rationality assumption on Q or U is imposed.
Equivalently, tau<c_mat forces F to be the constant germ I_r.

### M2. A positive metric has an explicit conditioning price

Let H be a fixed positive definite Hermitian r-by-r matrix and write

    kappa=lambda_max(H)/lambda_min(H)>=1.

Replace the two contraction hypotheses in (M1) by

    Q(z)*H Q(z)<=H,       U(z)*H U(z)<=H       for z in D,

while keeping the same integral germ, invertible Q0 and tau=-log|det Q0|.
Then a nonconstant F satisfies

    tau>=(1/2)log(1+1/(4kappa)).                            (M3)

No uniform bound on kappa is asserted for original G0001 inputs.
The conditioning dependence cannot simply be removed from this metric model, even at fixed size2 and fixed integral germ.
Indeed, for every kappa>=1, put

    F(z)=I_2+z E_12,       H_kappa=diag(kappa^(-1),1),
    a=kappa^(-1/2),       L=(sqrt(4+a^2)+a)/2,
    Q=L^(-1)I_2,          U=FQ.

Here E_12 has entry1 in position(1,2) and zero entries elsewhere.
These satisfy all the metric-model hypotheses, but

    tau=2log L ->0       as kappa->infinity.                (M4)

This is an exact analytic-germ control, not an original polynomial realization or a counterexample to Lehmer's problem.

### M3. Scalar replication keeps the full rank cost

If Q=q I_r and q(0)=exp(-a) with a>=0, then the total price in (M1) is

    tau=r a.                                               (M5)

Whenever the other hypotheses of (M1) hold and F is nonconstant, (M2) yields only a>=c_mat/r from this replication.
In particular substituting a=m(P) does not give a degree-independent original Mahler gap when r grows.

### M4. Direct companion reversal and its exact failure terms

For any C in GL_r(Z), define matrix rational functions

    D_C(z)=I_r-zC,
    R_C(z)=(zI_r-C^T)D_C(z)^(-1),
    G_C(z)=-C^(-T)R_C(z)
          =(I_r-zC^(-T))(I_r-zC)^(-1).                    (M6)

They are analytic near0 and G_C belongs to I_r+z M_r(Z[[z]]).
Here C^(-T)=(C^(-1))^T.
For z in T where D_C is invertible,

    R_C(z)*R_C(z)-I_r
      =D_C(z)^(-*)[CC^T-C^TC]D_C(z)^(-1).                 (M7)

Thus R_C is unitary almost everywhere on T if and only if C is normal, meaning CC^T=C^TC.
The normalization to constant coefficient I_r has a stronger restriction:

    G_C is unitary almost everywhere on T
       if and only if C^(-T)=C.                            (M8)

An integer orthogonal C is a signed permutation matrix and has zero characteristic-polynomial Mahler measure.
Therefore the normalized candidate G_C is not circle-unitary for any C whose characteristic polynomial has positive Mahler measure.
For reciprocal characteristic polynomial P with P(0)=1, both det R_C and det G_C are identically1, so this determinant identity does not supply the missing matrix norm control.

There is also a price at the constant coefficient of the unnormalized candidate.
Suppose Q and U are disk-holomorphic Euclidean contractions, Q0=Q(0) is invertible, and U=R_C Q near0.
Then

    tau=-log|det Q0|>=log||C||op.                           (M9)

For the standard companion of

    P0(t)=t^14-t^12+t^7-t^2+1,

the adopted C227 bound gives 0<m(P0)<log(13/10), whereas (M9) gives tau>=log2.
Hence this particular unnormalized realization cannot charge exactly tau=m(P0).
This fixed-positive comparison does not exclude a larger uniform multiplier of m(P), or a different construction.

### M5. A unit-circle conjugate excludes the original polynomial as an all-pass denominator

Let P in Q[z] be irreducible, with P(0) nonzero and at least one root on T.
Let W be an r-by-r matrix whose entries belong to

    Q[z,z^(-1),P(z)^(-1)].

Suppose W is holomorphic near0, W(0)=I_r, and W(z) is unitary for almost every z in T where it is defined.
Then

    W(z)=I_r                                               (M10)

as a rational matrix identity.
The conclusion holds for every r and every allowed denominator multiplicity.
The final rigidity step does not require the Taylor coefficients of W to be integral.

Consequently, for an irreducible original polynomial having a unit-circle conjugate, a nonconstant rational circle-unitary replacement of P*/P cannot use only that original P for its finite nonzero poles while retaining constant coefficient I_r.
Additional denominator factors, nonrational coefficient fields and general nonunitary Schur quotients are outside (M10).
No determinant-cost or arithmetic control for those alternatives is supplied.

### Original-target boundary

An actual realization of every positive-measure original reciprocal P by (M1), with nonconstant integral F and tau<=C_tr m(P) for one positive degree-independent scalar C_tr, would give m(P)>=c_mat/C_tr.
Such a realization is not constructed here.
The matrix criterion alone, a formal determinant identity, or an indefinite symplectic identity does not supply it.
No new original-input coverage, positive sequence tending to zero or resolution of the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) is asserted.

<a id="sources-and-contribution"></a>
## Reuse, source limits and contribution

[C296](Yin_C_G0296_v1.md#endpoint-row-hardy-closure) and [C475](Yin_C_G0475_v1.md#statement) retain the scalar finite-Blaschke, coefficient-space and finite-compression mechanisms with their actual rank and original-input limits.
The current argument uses ordinary vector Parseval directly, not an unproved cross-application of their probability or asymptotic conclusions.
[C65](Yin_C_G0065_v1.md#statement) and [C67](Yin_C_G0067_v1.md#statement) concern rational Laurent paraunitary matrices with universal original-order membership and explicit support or row-width restrictions.
They do not directly assert (M2), whose functions need not be Laurent, or (M10), which instead assumes an irreducible rational pole factor with a circle root and imposes no row-width bound.
[C36](Yin_C_G0036_v1.md#statement) retains its particular rational completion and full denominator, pole and original-root expenses.
[C90](Yin_C_G0090_v1.md#statement) concerns a fixed independent power dictionary and its coefficient quotient, not integer Taylor matrix germs with a small determinant normalization.
Those restrictions are preserved rather than silently applied to the present objects.

The inspected [AJL16 source account](../audits/literature/AJL16/Yin_U001.md#ajl16-u001) supplies related attribution for complex rational circle-isometries and rank-one Blaschke-Potapov factors, at arXiv:1410.0283v2, Theorem3.1, equations(3.2)-(3.5), printed/PDF pages10-11.
It supplies no rational or integer descent, original-input realization or determinant-cost estimate here.
No external Potapov theorem is needed for the proofs below, and its original proofs are not newly audited.
The finite companion comparison uses only C227's exact retained P0 measure interval, not a new execution or enlargement of its source classification.
No literature-priority claim is made.

The matrix_integer_return agent derived the Hilbert-Schmidt determinant-defect estimate, checked the companion identities, and independently identified the original-polynomial circle-pole obstruction.
The coordinating agent supplied the stronger column-Parseval estimate used in (M2), independently supplied the circle-pole obstruction, and proposed the exact varying-metric control (M4).
Both agents checked those deductions as contributors.
These are author-side checks, not independent mathematical review of this version.

<a id="argument"></a>
## Complete argument

<a id="matrix-column-determinant-gap"></a>
### 1. Column Parseval and the first integral matrix coefficient

Let Q(z)=sum_(n>=0)Q_n z^n and U(z)=sum_(n>=0)U_n z^n on D.
For any v in C^r and any radius 0<rho<1, the contraction hypothesis and vector Parseval give

    sum_(n>=0) rho^(2n)||Q_n v||^2
      =integral_T ||Q(rho zeta)v||^2 dmu(zeta)<=||v||^2.

Monotone convergence of the nonnegative series as rho increases to1 gives the same inequality without the rho factors.
The identical argument applies to U.
Since F(0)=I_r and U=FQ near0, one has U_0=Q_0.
Consequently, for every n>=1,

    ||Q_n v||^2<=||v||^2-||Q_0v||^2,
    ||U_n v||^2<=||v||^2-||Q_0v||^2.                       (1)

All these estimates concern disk-holomorphic Q and U, not the full germ F.

If F is nonconstant, analyticity supplies a least positive index N with C_N nonzero.
Multiplying the convergent germs near0 gives the exact coefficient identity

    U_N-Q_N=C_N Q_0.                                       (2)

In particular the order of multiplication is retained.
Using ||a-b||^2<=2||a||^2+2||b||^2 with (1)-(2) yields

    ||C_N Q_0v||^2
       <=4(||v||^2-||Q_0v||^2).                            (3)

Let s_1,...,s_r be the positive singular values of Q_0.
The contraction at0 gives s_i<=1.
Thus tau=-sum_i log s_i>=0, and

    min_i s_i>=product_i s_i=exp(-tau),
    ||Q_0^(-1)||op<=exp(tau).                              (4)

For any w in C^r put v=Q_0^(-1)w in (3).
Using (4),

    ||C_N w||^2
      <=4(||Q_0^(-1)w||^2-||w||^2)
      <=4(exp(2tau)-1)||w||^2.                             (5)

Taking the supremum over unit w proves the first inequality in (M2).
A nonzero integer matrix C_N has a column with Euclidean norm at least1, so ||C_N||op>=1.
Rearranging (5) proves the complete (M2).
No factor r occurs in this column estimate or in the lower singular-value estimate (4).

<a id="matrix-metric-and-copy-costs"></a>
### 2. Positive metrics, a genuine degenerating metric control and scalar copies

Let S=H^(1/2) be the positive definite square root of H.
Define

    F_tilde=S F S^(-1),
    Q_tilde=S Q S^(-1),       U_tilde=S U S^(-1).

The metric inequalities are exactly Euclidean contractivity of Q_tilde and U_tilde.
They still satisfy U_tilde=F_tilde Q_tilde near0, F_tilde(0)=I_r, and

    det Q_tilde(0)=det Q_0.

The first nonzero coefficient of F_tilde is C_tilde=S C_N S^(-1).
Although C_tilde need not have integer coefficients, the original C_N is integral and nonzero.
Therefore

    1<=||C_N||op
      <=||S^(-1)||op ||C_tilde||op ||S||op
      =sqrt(kappa)||C_tilde||op.                           (6)

The argument through (5), before the integrality step, applies to these transformed functions.
Combining it with (6) gives

    1/kappa<=4(exp(2tau)-1),

which is (M3).
An indefinite form has no positive square root giving this Hilbert-space contraction argument and is not a replacement hypothesis.

For the fixed-size control (M4), the positive square root is S=diag(kappa^(-1/2),1), and

    S F(z) S^(-1)=[[1,a z],[0,1]],       a=kappa^(-1/2).

For a shear [[1,w],[0,1]], its squared singular values have product1 and sum2+|w|^2.
Solving that quadratic gives its largest singular value as

    (sqrt(4+|w|^2)+|w|)/2.

This expression increases with |w|.
Its supremum for |z|<1 is exactly L in (M4).
Since L>=1, Q=L^(-1)I_2 is contractive in the H_kappa metric, and the same calculation proves contractivity of U=FQ.
Both are disk-holomorphic and Q_0 is invertible.
The determinant is L^(-2), so tau=2log L tends to0 as a tends to0.
The integral germ F stays fixed and nonconstant.
This proves that a general statement removing all metric dependence would be false, not merely unsupported by estimate (6).
It proves no sharpness claim for the particular dependence in (M3).

Finally, if Q=q I_r and q(0)=exp(-a), its determinant at0 is exp(-ra).
This gives (M5) exactly and proves the stated rank expense upon substitution into (M2).
The scalar price must not be substituted for the matrix determinant price.

<a id="companion-reversal-cost"></a>
### 3. The original companion candidate and its exact norm obstruction

Because C is an integer unimodular matrix, C^(-1) is integral.
The germ inverse of I-zC is sum_(n>=0) z^n C^n, which converges on some neighborhood of0.
Thus the functions in (M6) have the stated germs, and the normalized G_C has integer Taylor coefficients and constant coefficient I_r.

For |z|=1 put N_C=zI_r-C^T, so R_C=N_C D_C^(-1).
Direct multiplication gives

    N_C* N_C=I_r-z C-z^(-1)C^T+CC^T,
    D_C* D_C=I_r-z C-z^(-1)C^T+C^TC.

Subtracting and conjugating by D_C^(-1) proves (M7) wherever that inverse exists.
The exceptional set on T is finite because det D_C is a nonzero polynomial with value1 at0.
If R_C is unitary almost everywhere, (M7) forces CC^T-C^TC=0 at any regular point in that full-measure set.
Conversely that constant matrix equality gives the unitary identity at every regular point of T.
This proves the stated equivalence.

For the normalized candidate let K_C=I_r-zC^(-T), so G_C=K_C D_C^(-1).
The equation G_C*G_C=I_r is equivalent, at regular boundary points, to K_C*K_C=D_C*D_C.
Their difference is the Laurent polynomial matrix

    z(C-C^(-T))+z^(-1)(C^T-C^(-1))
       +C^(-1)C^(-T)-C^TC.                                (7)

Vanishing almost everywhere on T makes every Fourier coefficient of (7) zero.
In particular C-C^(-T)=0.
Conversely this equality makes C orthogonal and G_C identically I_r as a rational function.
This proves (M8).
An orthogonal integer matrix has integer columns of squared norm1 and mutually orthogonal columns, so each column has a single signed unit in a distinct row.
Its finite signed permutation action has all eigenvalues roots of unity, proving the zero-measure assertion.

If P(t)=det(tI_r-C) is reciprocal with P(0)=1, then

    det D_C(z)=z^r P(1/z)=P(z),
    det(zI_r-C^T)=P(z).

Thus det R_C=1.
Also det(-C^(-T))=1/P(0)=1, giving det G_C=1.
These determinant equalities retain no assertion that any individual singular value is1.

For the unnormalized candidate R_C(0)=-C^T.
If U=R_C Q near0 and both U,Q are Euclidean contractions, then

    1>=||U(0)||op=||C^T Q_0||op
       >=sigma_min(Q_0)||C||op
       >=exp(-tau)||C||op,

where (4) applies to Q_0.
Taking logarithms proves (M9).

For a standard companion, the first r-1 power-basis vectors are shifted to their successors and the last column is

    (-p_0,-p_1,...,-p_(r-1))^T

when P(t)=t^r+sum_(j=0)^(r-1) p_j t^j.
For P0 in the statement this column has exactly four entries of absolute value1, so its Euclidean norm is2 and ||C||op>=2.
The exact adopted C227 interval 1<M(P0)<13/10 now gives the strict mismatch between tau>=log2 and m(P0)<log(13/10).
No root computation or new numerical evidence is used, and this comparison does not require P0 to be irreducible.
This verifies the stated fixed-positive control at its actual scope.

<a id="original-circle-pole-rigidity"></a>
### 4. Rational circle poles and irreducibility

Let beta be a root of P on T.
Since P(0) is nonzero, beta is nonzero.
The rational unitary identity implies that every entry of W has absolute value at most1 at almost every regular point of T.
A genuine rational pole at beta contradicts this bound: in a local coordinate it has a nonzero leading polar coefficient, so its absolute value tends to infinity along the circle toward beta.
The bound holds on a full-measure subset of every sufficiently small punctured arc, which is enough for the contradiction.
Thus every entry is regular at beta.

Write one entry, after removing common factors, as a rational function whose denominator divides a power of z times a power of P.
If P remained in the reduced denominator, its numerator would not be divisible by P.
Irreducibility over Q would then make that numerator nonzero at beta.
The remaining positive power of P would produce a genuine pole at beta, a contradiction.
This argument also removes every possible multiplicity of P from the reduced denominator.
The possible power of z is removed by holomorphy at0.
Consequently each entry of W is a polynomial.

Expand W(z)=sum_(n>=0)W_n z^n, now a finite sum, with W_0=I_r.
For the i-th row, boundary unitarity and scalar Parseval give

    sum_(n>=0)sum_j |(W_n)_(ij)|^2=1.

Its constant row already has squared norm1.
Every remaining nonnegative summand must vanish, so W_n=0 for n>=1.
This proves (M10).
Rational coefficients were used in the irreducibility cancellation; integer Taylor coefficients were unnecessary for the final Parseval step.
There is no dimension, support or polynomial-degree restriction in this argument.

<a id="matrix-original-return-boundary"></a>
### 5. The actual original-input boundary

The matrix estimate (M2) supplies a positive absolute lower bound on a complete determinant normalization whenever its genuine integral-germ and contraction hypotheses are supplied.
It does not itself supply Q,U or connect their normalization to a given original P.
The scalar copy pays r times the scalar price, the positive-metric version pays its actual condition number, and the fixed metric control shows that uniformity over all such metrics would be false.
The raw companion candidate fails the desired normalization price on the retained positive control, while its constant-normalized version is circle-unitary only for zero-measure integer orthogonal inputs.
The original-polynomial pole argument excludes every rational circle-unitary replacement with only the original P as finite nonzero denominator when P has a circle conjugate.

That pole argument does not apply to arbitrary nonunitary Schur quotients UQ^(-1), nor to additional polynomial denominator factors or a larger coefficient field.
Such alternatives must retain their actual determinant price and restore the required integer Taylor coefficients rather than inheriting them from a formal factorization theorem.
The bounds above neither rule out every possible matrix construction nor provide one with tau<=C_tr m(P) uniformly in the original degree.
Accordingly the unchanged unrestricted G0001 goal remains unresolved.

## Assessment history

### Decision whole-matrix-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T19:22 |
| status | proved |
| reason | Adopt the complete matrix integer-germ estimate and its exact realization boundaries after the independent whole-proof finding R1091 v3. The total determinant price is at least (1/2)log(5/4), independently of matrix size and the first nonzero coefficient index, under the stated contraction hypotheses. The metric and scalar-copy prices, companion controls and rational circle-pole rigidity are included. No uniform positive-measure original-input realization, new original-input coverage or unrestricted G0001 gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete matrix statement](#statement) | M1-M10, the operator-norm estimate, conditioning and replication costs, exact controls and the conditional positive-measure original-input interface. |
| argument | [Complete matrix proof](#argument) | All five sections: column Parseval, determinant normalization, metric control, companion identities and prices, rational pole cancellation and original-target limitations. |
| dependency | [Accepted C227 example](Yin_C_G0227_v1.md#statement) | Only the exact P0=t^14-t^12+t^7-t^2+1 and 1<M(P0)<13/10 interval for the fixed companion comparison, with C227's retained MS12 acceptance and review limits. |
| review | [Independent matrix whole-proof finding](../audits/reviews/Yin_R_G1091_v3.md#matrix-whole-proof-finding) | Entire exact statement and argument, all controls, the isolated accepted-data interface and original-target scope; no substantive proof repair supplied by the reviewer. |

## Current assessment

[Selected decision](#decision-whole-matrix-review-2026-11-05)
