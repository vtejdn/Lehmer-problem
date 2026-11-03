---
author: Yin
---

# Sharp normal integral entropy gap and the rational mixed-conjugate obstruction

The complete reusable mathematics is retained from L24's original2026-10-06 direct proof.
This is a restricted control class, not a reduction of the reciprocal hard core.

## Statement

Let N>=1 and A in GL_N(Z) satisfy AA^T=A^T A.
With full algebraic entropy h(A)=m(det(tI−A)) and natural logarithms, one has h(A)=0 or h(A)>=log(phi), phi=(1+sqrt5)/2.
The positive bound is attained by [[1,1],[1,0]], and by its direct sum with[−1] if determinant one is required.

Let T be a rational d-by-d matrix with irreducible characteristic polynomial p having both a real and a nonreal root.
There is no rational positive definite symmetric G for which T commutes with its G-adjoint G^-1 T^T G.
The same impossibility holds for every rational U with characteristic polynomial p c where p occurs once and c is coprime to p, if U is required normal in a rational positive metric.
In particular every Salem minimal polynomial of degree at least4 is excluded even after arbitrary cyclotomic padding.
This does not rule out real metrics with irrational entries or claim an entropy gap for general nonnormal integral flows.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:49 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All ordinary normal unimodular integer matrices of arbitrary positive size, exact sharp log(phi) entropy, and all irreducible rational mixed-real/nonreal factors including any coprime neutral padding under rational positive metrics. |
| argument | [Argument](#argument) | Full integer Frobenius trace and signwise exponential-merging proof, exact equality controls, rational cyclic-centralizer/adjoint action contradiction and reducing rational subspace argument under padding. |
| dependency | [Exact entropy normalization](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Full finite-dimensional rational characteristic-polynomial entropy, specializing to monic integral units with no leading penalty or rank normalization. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:50 |
| status | proved |
| reason | Actual complete current theorem and proof self-review confirms the exact retained arguments and accepted inputs, with every restricted domain, entropy normalization and negative-result boundary explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All ordinary normal unimodular integer matrices of arbitrary positive size, exact sharp log(phi) entropy, and all irreducible rational mixed-real/nonreal factors including any coprime neutral padding under rational positive metrics. |
| argument | [Argument](#argument) | Full integer Frobenius trace and signwise exponential-merging proof, exact equality controls, rational cyclic-centralizer/adjoint action contradiction and reducing rational subspace argument under padding. |
| dependency | [Exact entropy normalization](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Full finite-dimensional rational characteristic-polynomial entropy, specializing to monic integral units with no leading penalty or rank normalization. |
| review | [Complete actual self-review](../audits/reviews/Yin_R_G0514_v1.md#current-normal-obstruction-finding) | Exact complete statement and full necessary proof, source applicability and controls; no isolated independent or general research conclusion is asserted. |

## Argument

<a id="normal-integral-gap"></a>
### A sharp elementary normal-matrix gap

Let A in GL_N(Z) satisfy AA^T=A^T A.
Its eigenvalues lambda_i have product of absolute values one.
Put u_i=log|lambda_i| and

    m=sum_i max(0,u_i)=h_alg(A).

The entropy identity is the accepted monic integral characteristic-polynomial formula from the Task.
Normality gives

    tr(A^T A)=sum_i exp(2u_i),

which is an integer.
If m>0, strict arithmetic-geometric mean implies tr(A^T A)>N, hence tr(A^T A)-N>=1.

The positive u_i sum to m; the absolute values of the negative u_i also sum to m.
For nonnegative x,y,

    (exp(x)-1)+(exp(y)-1) <= exp(x+y)-1,
    (exp(-x)-1)+(exp(-y)-1) <= exp(-(x+y))-1.

Both follow by expanding the product of the two respective deviations from one.
Merge each sign class to obtain

    1 <= tr(A^T A)-N <= exp(2m)+exp(-2m)-2.

Thus M=exp(m)>1 satisfies M^2+M^(-2)>=3, so

    m>=log(phi),  phi=(1+sqrt(5))/2.

The bound is attained by [[1,1],[1,0]], whose eigenvalues are phi and -phi^(-1).
A determinant-one example is its direct sum with [-1].
These are exact algebraic controls, not numerical experiments.
Without normality the trace identity fails: the integer unipotent matrix [[1,1],[0,1]] has entropy zero but tr(A^T A)=3.

<a id="mixed-conjugate-normal-obstruction"></a>
### Why a rational positive metric does not normalize Salem dynamics

Let T be a rational d-by-d matrix with irreducible characteristic polynomial p, having both a real root and a nonreal root.
Suppose a rational positive definite symmetric G made T normal for that metric.
Its adjoint T^dagger=G^(-1)T^T G would commute with T.

Since p is irreducible, T is cyclic.
Its rational centralizer is Q[T], so T^dagger=f(T) for some rational polynomial f of degree below d.
For completeness, choose a cyclic vector v: a commuting map is determined by its value on v, which is uniquely f(T)v in the basis v,Tv,...,T^(d-1)v.
Commutation then determines the map on the entire basis.

The real matrix G^(1/2) T G^(-1/2) is normal, and unitary diagonalization shows that its adjoint acts on the lambda eigenspace by conjugate(lambda).
Therefore

    f(lambda)=conjugate(lambda)

for every root of p.
At a real root alpha this gives f(alpha)=alpha.
Irreducibility forces p to divide f(t)-t, so the equality f(lambda)=lambda holds at every conjugate.
Combined with the previous display it would make every root real, a contradiction.

Consequently no such rational metric exists for an irreducible mixed-real/nonreal polynomial.
This includes every Salem minimal polynomial of degree at least four.
The obstruction is not merely a large condition number or a bad choice of an integral basis.

Adding only neutral factors does not fix it.
If a rational matrix U has characteristic polynomial p*c, with p occurring once and c coprime to p, and a rational positive metric makes U normal, then V=ker p(U) is a rational invariant subspace of dimension d.
The adjoint commutes with U, so V is also adjoint-invariant.
Restricting the metric and operators to V yields precisely the impossible model above.
For a noncyclotomic p and cyclotomic c the coprimality and single-occurrence conditions hold automatically.
Thus arbitrary cyclotomic padding cannot produce a rational normal model of Salem dynamics.

### Relation to the preceding trace construction

[L G0022](Yin_C_G0227_v1.md#neutral-rational-symmetric-realization) made the trace operator symmetric over Q.
It did not make its block entropy automorphism normal.
The present obstruction explains why that additional step is unavailable for Salem factors, even though an arbitrary real metric could normalize a real diagonalizable operator.
Rationality of the adjoint is essential in the argument.

The normal integral gap above therefore supplies a useful control class, not a gap for its invariant factors under unrestricted realizations.
A real-normal representation with irrational metric does not have the integral Frobenius-norm identity used in the first section.
