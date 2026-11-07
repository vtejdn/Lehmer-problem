---
author: Yin
---

# Root measures, Brown potentials and the arithmetic constraints in Lehmer's problem

Date: 2026-11-07.
Human author: Yin.
This synthesis retains the bounded discussion of Mahler measure, logarithmic potentials and Brown measure, including the arithmetic and normalization limits of that reformulation.
The coordinating AI agent assembled the discussion and checked the elementary identities below as ordinary checks within the exposition.
This is a synthesis of standard inputs and direct finite-dimensional calculations, with no novelty claim, formal project-review finding or new Claim assessment.
The [unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

<a id="scope-and-reused-inputs"></a>
## Scope and reused inputs

The question is how integrality appears in the Brown measure of a polynomial's roots, and what these conditions do and do not imply about a uniform positive Mahler gap.
The present record fixes the dictionary, complete finite-dimensional arithmetic domain and useful failed implications from the discussion.
It supplies no new uniform-gap proof or counterexample family.

| Responsible input | Scope reused here |
| --- | --- |
| [MS17 Brown interfaces](../audits/literature/MS17/Yin_U001.md#ms17-u001) | Chapter 11, Theorem 5 and Definition 6, printed p. 268, equations (11.6)-(11.7), and normal specialization on printed p. 270: normalized Brown potential, distributional Laplacian and the normal spectral law. These are accepted source inputs at the recorded inspection scope. |
| [Den09 determinant conventions](../audits/literature/Den09/Yin_U001.md#fk-determinant) and [Mahler conventions](../audits/literature/Den09/Yin_U001.md#mahler-measure) | Faithful finite trace, unmodified Fuglede--Kadison determinant, logarithmic singularities, Haar normalization and the one-variable Jensen identity. |
| [Smy08 height normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), [Section 4 lower-bound scope](../audits/literature/Smy08/Yin_U001.md#section-4-checked-mechanisms-and-external-theorems) and [discriminant interface](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation) | Total Mahler measure versus degree-normalized height, the reported degree-dependent lower-bound benchmark, and the complete discriminant estimate with its dimension loss. |
| [L454 arithmetic-measure conventions](Yin_L_G0454_v1.md#arithmetic-measure-and-potential-conventions) and [realization costs](Yin_L_G0454_v1.md#realization-theorem-ranges) | The distinct limiting-measure notion, exact source hypotheses and the actual realization costs; those arguments remain at their existing home. |

The source records above were reused at their stated editions, passage locators and inspection limits.
No new audit of the original Brown construction or the lower-bound theorems was performed.
The existing fixed-input scalar determinant mechanism in [C18](../claims/Yin_C_G0018_v1.md#statement) is related background, not a new proof input or a uniform-gap conclusion of this record.

<a id="root-measures-and-potentials"></a>
## Root measures and logarithmic potentials

**Definition (root measures and positive logarithmic potential).**
Let P be a nonzero complex polynomial of degree d>=1, written as
\[
 P(z)=a_d\prod_{j=1}^d(z-\alpha_j),\qquad a_d\ne0,
\]
with roots listed with algebraic multiplicity.
Its root counting measure, root probability measure and positive-kernel potential are
\[
 \nu_P=\sum_{j=1}^d\delta_{\alpha_j},\qquad
 \mu_P=\frac1d\nu_P,\qquad
 \Phi_P(z)=\int\log|z-w|\,d\nu_P(w).
\]
Use natural logarithms, log 0=-infinity, log^+ r=max(0,log r) for r>0, and log^+ 0=0.
The Laplacian is Delta_z=partial_x^2+partial_y^2 and is taken in the sense of distributions.
Thus
\[
 \log|P(z)|=\log|a_d|+\Phi_P(z),\qquad
 \frac1{2\pi}\Delta_z\Phi_P=\nu_P.
\tag{1}
\]
The normalization follows from Delta_z log|z-w|=2pi delta_w, whose flux through a small circle centered at w is 2pi.
Using the potential kernel log(1/|z-w|) instead reverses the sign of its Laplacian.

Let sigma be Haar probability on the unit circle, with d sigma(e^{it})=dt/(2pi).
The one-variable Jensen identity gives
\[
 g(w)=\int_{\mathbb T}\log|w-z|\,d\sigma(z)
      =\log^+|w|,\qquad
 \frac1{2\pi}\Delta g=\sigma.
\tag{2}
\]
Consequently
\[
 m(P)=\log M(P)
 =\log|a_d|+\int g\,d\nu_P
 =\log|a_d|+d\int g\,d\mu_P
 =\int_{\mathbb T}\log|P(z)|\,d\sigma(z).
\tag{3}
\]
The logarithmic singularities from roots on the circle are integrable.
The cross-integral between sigma and the finite root measure is therefore well defined, including circle roots.
It is not the self-energy of the atomic root measure.

If every root satisfies |alpha_j|>1, log|P| is harmonic on a neighborhood of the closed unit disk, and
\[
 m(P)=\log|P(0)|=\log|a_d|+\Phi_P(0).
\tag{4}
\]
For a monic integer polynomial in this restricted class, |P(0)| is an integer greater than one, so m(P)>=log 2.
This restricted class does not contain the unresolved small-gap difficulty.

<a id="brown-measure-and-trace-normalization"></a>
## Brown measure and trace normalization

**Definition (Brown potential and the matrix specialization).**
For a bounded element T in a finite von Neumann algebra with faithful normal tracial state tau, write
\[
 u_T(z)=\log\operatorname{Det}_{\tau}(zI-T)
       =\tau(\log|zI-T|),\qquad
 \operatorname{Br}_T=\frac1{2\pi}\Delta_z u_T.
\tag{5}
\]
The determinant is the unmodified Fuglede--Kadison determinant and may vanish; correspondingly u_T may be -infinity.
This is the positive-log-potential convention in the reused MS17 and Den09 interfaces, with Det_tau reserved for the determinant to distinguish it from the Laplacian.

For A in M_d(C), use tau_d=Tr/d.
The product of singular values gives, also in the singular case by the determinant-zero convention,
\[
 \operatorname{Det}_{\tau_d}(zI-A)
   =|\det(zI-A)|^{1/d}.
\]
If P=det(zI-A), equations (1) and (5) give
\[
 u_A(z)=\frac1d\log|P(z)|,\qquad
 \operatorname{Br}_A=\mu_P.
\tag{6}
\]
No normality or diagonalizability of A is required.
For a monic integer P, its integer companion matrix C_P has this characteristic polynomial and realizes exactly the required Brown measure.
The diagonal normal matrix with entries alpha_j has the same Brown measure, but its entries need not be integers.
In the commutative algebra L^infinity(T,sigma), multiplication by the coordinate is a Haar unitary U with Br_U=sigma and u_U=g.

The specified dimension d is additional information beyond mu_P.
Indeed P and P^k have the same root probability measure for every integer k>=1, while their degrees and total logarithmic Mahler measures are multiplied by k.
Likewise A and a direct sum of k copies of A have the same normalized Brown measure.
For a nonmonic P, the roots also fail to record the leading-coefficient contribution log|a_d| in (3).

For a normal realization D_P, functional calculus gives
\[
 \int\log^+|z|\,d\operatorname{Br}_{D_P}(z)
 =\tau_d(\log^+|D_P|).
\]
For a general nonnormal integer companion matrix, the left side concerns eigenvalues whereas tau_d(log^+|C_P|) concerns singular values.
There is no such general equality, and replacing one by the other would change the required quantity.

<a id="finite-arithmetic-constraints"></a>
## Exact finite arithmetic constraints

At a specified dimension d, the condition on a finite root probability measure is that
\[
 \mu=\frac1d\sum_{j=1}^d\delta_{\alpha_j},\qquad
 \prod_{j=1}^d(z-\alpha_j)\in\mathbb Z[z].
\tag{7}
\]
Equivalently the elementary symmetric functions of the d listed roots are integers.
Equivalently, grouping roots into complete conjugacy orbits gives
\[
 \mu=\frac1d\sum_Q n_Q\sum_{Q(\alpha)=0}\delta_\alpha,
 \qquad n_Q\in\mathbb Z_{\ge0},\qquad
 d=\sum_Q n_Q\deg Q,
\tag{8}
\]
where Q runs over finitely many distinct monic irreducible integer polynomials.
In (8), each Q has simple roots, and its exponent n_Q supplies their common multiplicity.
The forward implication is the factorization of P over the rational numbers; conversely the product of these Q to their listed powers is an integer polynomial and its companion matrix realizes mu.
Thus the atoms are algebraic integers and their full Galois orbits occur with constant multiplicity within each orbit.
This characterizes existence of an integer-matrix realization of the Brown measure; it does not recover the entries, Jordan structure or an integral lattice for an arbitrarily selected operator having that measure.

For such an integer matrix A and P=det(zI-A), define
\[
 s_k=d\int z^k\,d\mu(z)=\operatorname{Tr}(A^k),\qquad k\ge1.
\]
Then s_k is an integer, and in formal power series
\[
 \exp\left(-\sum_{k\ge1}\frac{s_k}{k}t^k\right)
 =\det(I-tA)\in\mathbb Z[t].
\tag{9}
\]
The identity follows by expanding the formal logarithm of the product of (1-t alpha_j).
It retains the Newton-identity divisibility conditions as well as integrality of individual traces.
For every prime p and k>=1 one also has
\[
 s_{pk}\equiv s_k\pmod p.
\tag{10}
\]
To check (10), reduce B=A^k modulo p and triangularize over the algebraic closure of F_p.
The trace of B^p is the pth power of the trace of B, which equals the trace of B in F_p.
These are necessary moment constraints; the individual trace conditions alone are not asserted to characterize (7).

For Q in Z[z] with gcd(P,Q)=1, the monic resultant identity gives
\[
 \begin{aligned}
 d\int\log|Q(z)|\,d\mu(z)
 &=\log|\det Q(A)|\\
 &=\log|\operatorname{Res}(P,Q)|\ge0.
 \end{aligned}
\tag{11}
\]
Indeed the determinant is the product of Q(alpha_j), with all original multiplicities, and is a nonzero integer.
Equivalently, Det_tau_d(Q(A))=|Res(P,Q)|^(1/d)>=1.
Equality is possible when the resultant has absolute value one.
If P and Q have a common root, the integral is -infinity and (11)'s nonnegative conclusion is unavailable.

For squarefree P, the nonzero integer discriminant further gives
\[
 \frac1{d^2}\sum_{i\ne j}\log|\alpha_i-\alpha_j|
 =\frac1{d^2}\log|\operatorname{disc}(P)|\ge0.
\tag{12}
\]
This is the off-diagonal logarithmic energy.
For repeated roots the displayed nonnegative statement fails because the discriminant vanishes; the full atomic self-energy is -infinity even in the squarefree case.
The existing [Smy08 discriminant comparison](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation) states exactly
\[
 2(d-1)m(P)\ge\log|\operatorname{disc}(P)|-d\log d
\]
for d>=2 and nonzero discriminant.
Merely knowing that the discriminant is a nonzero integer does not overcome the d log d subtraction.

<a id="finite-versus-limiting-arithmetic-measures"></a>
## Finite root measures and limiting arithmetic measures

The finite conditions (7)-(11) must be distinguished from the [arithmetic probability measure of L454](Yin_L_G0454_v1.md#arithmetic-measure-and-potential-conventions).
That source-based limiting notion requires conjugation symmetry and
\[
 \int\log|Q|\,d\mu\ge0
 \quad\text{for every }0\ne Q\in\mathbb Z[z],
\]
at its recorded compact-support and source scope.
A finite root measure mu_P fails this condition for Q=P, since the integral is -infinity.
Thus an integer matrix's Brown measure is not itself an arithmetic measure in that particular limiting sense.
The finite coprimality restriction and the limiting all-polynomial tests are different assertions.
The realization results and their inability to guarantee the needed total-Mahler accuracy remain at [L454](Yin_L_G0454_v1.md#realization-theorem-ranges), without repeating or expanding their source inspection here.

<a id="lehmer-gap-and-limit-obstruction"></a>
## The gap question and the weak-limit obstruction

For monic integer P the exact quantity is
\[
 E(P)=d\int g\,d\operatorname{Br}_{C_P}=m(P).
\]
The existing Lehmer contract is therefore equivalently
\[
 \exists c>0\ \forall d\ge1\ \forall A\in M_d(\mathbb Z):
 \quad
 d\int\log^+|z|\,d\operatorname{Br}_A(z)
 \in\{0\}\cup[c,\infty).
\tag{13}
\]
Every monic integer P is realized by a companion matrix, and every integer matrix has a monic integer characteristic polynomial, giving both directions.
For arbitrary nonzero integer polynomials the leading-coefficient case |a_d|>=2 already has m(P)>=log 2, so existence of a gap is equivalent to this monic formulation.
It is the existence question, not the stronger proposed optimal value at Lehmer's degree-ten example.

At probability-measure scale the target positive lower bound is c/d, rather than a positive constant independent of d.
The exact control families
\[
 P_d(z)=z^d-2,\qquad R_d(z)=z^d-1
\]
have root measures uniform on the d equally spaced points of radii 2^(1/d) and 1, respectively.
Both probability measures converge weakly to sigma: their angular sums are Riemann sums and 2^(1/d) tends to one.
Nevertheless
\[
 d\int g\,d\mu_{P_d}=\log2,
 \qquad
 d\int g\,d\mu_{R_d}=0.
\tag{14}
\]
The example refutes recovery of total Mahler measure from the limiting Brown law alone.
It does not refute Lehmer's conjecture.

For an integer unit polynomial, meaning monic P with P(0)=1 or -1, one has
\[
 \int\log|z|\,d\nu_P=0,\qquad
 m(P)=\frac12\int|\log|z||\,d\nu_P.
\tag{15}
\]
This follows by splitting the zero sum of the logarithmic moduli into its positive and negative parts.
In particular Det_tau_d(C_P)=1 can coexist with m(P)>0; determinant positivity at Q(z)=z alone cannot supply the desired gap.
Equations (11)-(12) yield additional nonnegativity constraints, but no comparison proved here forces E(P)>=c whenever E(P)>0.

The existing [Smy08 lower-bound account](../audits/literature/Smy08/Yin_U001.md#section-4-checked-mechanisms-and-external-theorems) reports the Dobrowolski-type benchmark
\[
 m(P)\ge c_0\left(\frac{\log\log d}{\log d}\right)^3
\]
for nonzero nontorsion algebraic integers with irreducible minimal polynomial P, an absolute c_0>0 and the applicable sufficiently large degree range.
This is a reused source report, not a new proof or a claim about the latest best constant.
Its right side tends to zero and does not establish (13).

The unresolved obligation is to obtain a strictly positive total-Mahler bound uniform in d from the full arithmetic conditions, or to construct actual integer polynomials violating such a bound.
Weak convergence, arbitrary positive root measures, trace integrality by itself, and an uncharged replacement by singular-value data do not discharge that obligation.
Any continuation would have to preserve the original integer polynomial, full conjugate multiplicities and the degree factor, and establish the missing quantitative comparison at that scale.

For the normalized finite free convolutions, [MSS15-U001](../audits/literature/MSS15/Yin_U001.md#arithmetic-brown-application-boundary) retains exact degree-two failures of integer coefficient closure, including a multiplicative failure for irreducible unit inputs.
Its coefficient formulas and denominator costs identify the additional arithmetic conditions needed before using those operations in this Brown-measure formulation.
The complementary [L460 comparison](Yin_L_G0460_v1.md#scope-and-source-interfaces) retains integral coefficient subclasses, the signed Hadamard variant, a finite-difference normalization failure and their precise Lehmer-use limits.
