---
author: Yin
---

# Actual critical reflection blocks, reciprocal drift payment and unit singular modes

Human author Yin.
Root proposed the true-H stochastic reversible conversion of the reflected kernel and the obstruction for arbitrary J-invariant drift functions.
Contributor original_signed_asymptotic checked the complete actual-law conventions, identified and reused C203's existing raw reflection/coset geometry, and developed the finite actual-H matrices, general reciprocal drift-payment identity, finite block certificate and weighted one-step singular-mode conclusions.
The raw finite reflection-block geometry is an existing C203 input, not a new contribution.
This is an author candidate with no independent review or adoption asserted.

## Statement

Use the fixed quartic P(t)=t^4-t^3-t^2-t+1, its Salem root beta, actual order O=Z[beta] and involution iota(beta)=beta^(-1).
The complete original digit probabilities are p_0=1/2 and p_(-1)=p_1=1/4.
Write B=1/(beta-1), S=beta B and use the entire actual core

    D={x in O: |x_+|<B, |x_-|<S}.

Let P_D(x,y)=p_e when y=beta x+e belongs to D, and0 otherwise.
Use the TRUE critical radius R and ACTUAL first-hit function H, with H(0)=1,0<H<=1,H=R P_D H, and the stochastic critical kernel

    Q(x,y)=R P_D(x,y)H(y)/H(x).

The critical return mean mu may be infinite.
Put

    Jx=beta^(-1)iota(x),       (mathsf J f)(x)=f(Jx),
    sigma(x)=H(x)H(Jx),
    L=mathsf J Q,             L(x,y)=Q(Jx,y),
    A=mathsf J P_D,           A(x,y)=P_D(Jx,y).               (RB1)

Here J maps D to D and J^2=identity.
The positive weight sigma is the actual unnormalized complete-excursion occupation, with sigma(0)=1 and sum_D sigma=mu, including infinity.

C203 already proves that A is symmetric and decomposes over paired integer cosets.
For this quartic each connected component C of the positive-edge graph of A has at most SIX vertices.
It is contained in[(x+Z) union(iota(x)+Z)] intersect D for any x in C.
These finite components partition the infinite actual core, so infinitely many components avoid any prescribed finite subset.

The NEW actual-weighted conversion is

    L(x,y)=R A(x,y)H(y)/H(Jx),
    sigma(x)L(x,y)=R A(x,y)H(x)H(y)=sigma(y)L(y,x).            (RB2)

Consequently L is stochastic and each finite component C is closed and reversible for the positive finite weight sigma restricted to C.
No summability of sigma on D is needed.

For every pointwise finite real function W on D, define d_W=W-QW.
Every such function has finite row sums because each original row has at most three successors.
The exact reciprocal block-payment identity is

    sum_(z in JC) sigma(z)d_W(z)
       =sum_(x in C) sigma(x)[W(Jx)-W(x)].                   (RB3)

Thus if d_W>=g on JC, then

    sum_(x in C) sigma(x)[W(Jx)-W(x)]
       >=sum_(x in C) sigma(x)g(Jx).                        (RB4)

For unit drift g=1, the right side is sigma(C).
If W=s+b with s composed with J=s, its entire block-average payment in RB3 depends only on b(Jx)-b(x).
Adding a J-invariant term cannot change this block-average drift.

For EVERY pointwise finite real f with f composed with J=f, no finite set F makes Qf-f strictly negative at EVERY x outside F.
No positivity, boundedness, monotonicity, regularity or integrability of f is assumed.
The same obstruction holds for the killed kernel Q_0 away from a finite set, where Q_0 removes transitions into zero.
The conclusion is ONE-step only; it does not assert the analogous claim for arbitrary powers Q^m or stopping rules.

There is also a finite actual-H matrix form.
For each component C, define

    r(x)=H(x)/H(Jx)>0,
    M_C(x,y)=R sqrt(r(x)) A(x,y) sqrt(r(y)),
    w_C(x)=sqrt(sigma(x)).                                  (RB5)

The matrix M_C is symmetric, has all eigenvalues in[-1,1], and has a simple largest eigenvalue1 with positive eigenvector w_C.
In particular

    M_C w_C=w_C,     I-M_C is positive semidefinite,
    det(I-M_C)=0.                                          (RB6)

All these constraints use the ACTUAL ratios r, not freely chosen block weights.
For every real vector u on C, the exact finite energy identity is

    u^T(I-M_C)u
      =(R/2)sum_(x,y in C) A(x,y)H(x)H(y)
          [u(x)/sqrt(sigma(x))-u(y)/sqrt(sigma(y))]^2.        (RB7)

For arbitrary pointwise finite W,g, put u_C(x)=sqrt(sigma(x))W(x).
Then the FULL componentwise drift condition on JC is exactly

    W-QW>=g on JC
    iff
    M_C u_C(x)<=sqrt(sigma(x))[W(Jx)-g(Jx)] for every x in C. (RB8)

The right side retains all actual values on JC, which need not equal C.
This is a finite reformulation for each block, not a finite collection covering all D and not a supplied successful drift witness.
RB4 is necessary for RB8 but is not asserted sufficient.

On the actual complex Hilbert space l2(D,sigma), mathsf J is unitary and selfadjoint, L is a selfadjoint contraction, and

    Q=mathsf J L,      Q^*=L mathsf J,
    Q^*Q=L^2.                                             (RB9)

Every normalized component indicator

    e_C=1_C/sqrt(sigma(C))

belongs to this Hilbert space and satisfies

    L e_C=e_C,     Q^*Q e_C=e_C,
    Q e_C=1_(JC)/sqrt(sigma(C)),    ||Qe_C||=1.              (RB10)

The infinitely many distinct C give an infinite orthonormal family and an infinite-dimensional subspace on which Q preserves the one-step norm.
These are singular modes, not a claim that e_C is an eigenvector of Q.
No conclusion about powers Q^m, spectral radius, convergence rate, finite/infinite mu, linear bridge-level growth or an unrestricted Mahler gap is asserted.
The older counting-measure l2(P_D) norm and two-step bounds remain at C203/C408's different scope.

## Complete argument

### Reuse and exact mathematical boundary

The [adopted C203 statement and raw fiber argument](Yin_C_G0203_v1.md#decision-isolated-quartic-certificate-review-20261023) were read in full statement scope.
C203 already proves edge reversal, the reflected raw kernel A=mathsf J P_D, pairing of cosets modulo Z, finite interval fibers of length at most ceil(2B), and the fixed-coset tridiagonal form.
It also proves counting-measure one-step norms and a strict raw two-step loss; those are not estimates for the actual H-transformed Q.
Only its exact algebraic geometry and original edge weights are reused here.

The [C400 fixed-quartic strict-core theorem](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption), using its C399 narrow co-return premise, identifies the strip with the actual accessible/coaccessible core and supplies its infinitude.
The [C599 actual critical interface](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) supplies positive H<=1, true R, H=R P_D H and stochastic Q without a mean assumption.
The [C563 canonical occupation and reciprocity](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) supplies sigma=H(H composed with J), sigma composed with J=sigma and its extended total mu.

The bounded reuse screen also inspected C448's raw reciprocal edge reversal, C599's monotone radial obstruction, C847's arbitrary fixed-horizon invariant-endpoint construction, and C745's separate obstruction to reversible realizations of the original return sequence.
Targeted searches by reflected kernel, paired integer cosets, finite reversible blocks, J-invariant drift, weighted square and singular modes found no adequate true-H block account of RB2--RB10.
C203 supplies the geometric part, so its proof is not recast as a new discovery.
The new weighted conclusions below are direct finite-row, finite-matrix and nonnegative-sum calculations from these inputs.
No native graph enumeration, external source theorem or stationary normalization is needed.

### Existing raw geometry at the actual quartic and fixed operator convention

The reciprocal map has real coordinates

    (Jx)_+=beta^(-1)x_-,    (Jx)_-=beta x_+,

so it preserves the two strict inequalities defining D.
It also satisfies J^2=identity and preserves O because beta is a unit.
Direct substitution into the convention in RB1 gives

    A(x,y)=p_e if y=iota(x)+e belongs to D.

Such an edge reverses as x=iota(y)-e.
The equality p_e=p_(-e) therefore gives A(x,y)=A(y,x).
There is at most one digit for each ordered pair of vertices.

For completeness of this specialization, beta>5/3: P(5/3)=-29/81<0, and for t>1 the reciprocal factorization shows that the sign of P(t) is the sign of t-beta.
Indeed t-beta^(-1)>0 and the quadratic from the nonreal neutral pair is positive.
Thus B<3/2, so2B<3.
The expanding-coordinate condition allows at most three integer translates r+n in D on any one coset r+Z.
Every pair of successive reflected edges changes x by an integer, and an odd number gives an element of iota(x)+Z.
This is precisely C203's paired-coset geometry, specialized to at most six vertices.

Take connected components using the positive symmetric edges, with loops allowed.
No edge leaves such a component, by its definition.
Every component is finite and the components partition D.
Since D is infinite, there are infinitely many components.
Only finitely many components meet any fixed finite set, so a component disjoint from that set always exists.
This avoids any unproved density statement or estimate of the weights of remote components.

### True-H reversibility on each finite component

The definition of Q and A gives the first identity in RB2.
Multiplying by sigma(x)=H(x)H(Jx) gives the displayed symmetric conductance.
Positivity of H means A and L have exactly the same positive-edge graph.
Every row of L has sum1 because it is a row of the actual stochastic Q at Jx.
Therefore the finite component restriction L_C is a stochastic matrix.

For each y in C, symmetry of the conductance and row normalization give

    sum_(x in C) sigma(x)L(x,y)
       =sigma(y)sum_(x in C)L(y,x)=sigma(y).                 (RB11)

This is a finite equality.
In particular sigma(C) is a positive finite invariant mass, whether or not the mass over all components is finite.
No new invariant probability for the full Q has been assumed.

For any finite real function W on D, only its finitely many values on C enter

    sum_(x in C) sigma(x)(LW)(x)=sum_(x in C)sigma(x)W(x).

This identity is valid for sign-changing and globally unbounded W because C is finite.
It is not an integration of an unbounded global stationary coboundary.

### Reciprocal payment and the arbitrary invariant-function obstruction

Change variables z=Jx in the left side of RB3.
The exact equalities sigma(Jx)=sigma(x) and QW(Jx)=LW(x) give

    sum_(z in JC) sigma(z)[W(z)-QW(z)]
       =sum_(x in C) sigma(x)[W(Jx)-LW(x)].

Applying the finite equality following RB11 proves RB3.
Multiplying a pointwise lower bound d_W>=g by positive sigma and summing proves RB4.
Substitution of W=s+b with s(Jx)=s(x) proves the claimed exact cancellation.

Now suppose f(Jx)=f(x) and Qf-f<0 at every x outside a finite F.
Choose a component C disjoint from JF.
Then all z in JC lie outside F, so every summand in

    sum_(z in JC) sigma(z)[f(z)-Qf(z)]

is strictly positive.
But RB3 says this finite sum equals zero.
This contradiction proves the one-step assertion, even without a common positive drift margin.

For Q_0 choose C disjoint from JF and from{0}.
All L transitions from C stay in C and hence avoid zero.
Thus all Q transitions from JC go to C and avoid zero, so Q_0 f=Qf on JC.
The same finite contradiction applies.
The construction makes no assertion about L being Q, about C being Q-closed, or about J preserving each individual component.

The necessary unit-drift payment has a concrete consequence.
If W=s+b and s is J-invariant, then on every component with JC outside the exceptional set a unit-drift witness must satisfy

    sum_(x in C) sigma(x)[b(Jx)-b(x)]>=sigma(C).             (RB12)

A correction with b(Jx)-b(x)<1 at every x of one such component cannot pay this condition.
Changing the J-invariant term cannot repair that failure.
This remains a necessary block condition, not a proof that any proposed correction works on all blocks.

### Finite actual-H matrices and the complete local certificate

Let S_C be the diagonal matrix with entries sqrt(sigma(x)).
Direct multiplication using RB2 gives

    S_C L_C S_C^(-1)
       =R diag(sqrt(r)) A_C diag(sqrt(r))=M_C.

This proves symmetry and the exact similarity, with all H ratios retained.
Since L_C1=1, it also proves M_C w_C=w_C.

For any complex vector f on C, the elementary weighted Cauchy--Schwarz inequality in each stochastic row gives

    |(L_C f)(x)|^2<=sum_(y in C)L(x,y)|f(y)|^2.

Multiply by sigma(x), sum, and apply RB11.
Thus L_C is a contraction in its finite weighted l2 norm, and M_C is a contraction in ordinary Euclidean norm.
Its real symmetric eigenvalues consequently lie in[-1,1].

For real f on C, expansion and RB11 give

    sum_(x in C)sigma(x) f(x)[f(x)-(L_Cf)(x)]
       =(1/2)sum_(x,y in C)sigma(x)L(x,y)[f(x)-f(y)]^2.

Set f(x)=u(x)/sqrt(sigma(x)) and substitute the conductance in RB2 to obtain RB7.
It proves I-M_C positive semidefinite.
If the right side vanishes, f is equal at the endpoints of every positive edge, hence is constant on the connected component C.
Therefore the eigenspace for eigenvalue1 is one-dimensional, generated by w_C; the largest eigenvalue is exactly1 and RB6 follows.
This uses only the finite energy identity, without an irreducible-chain limit theorem or a supplied spectral gap.

Finally, the desired inequality on z=Jx is

    QW(Jx)<=W(Jx)-g(Jx),
    (L_CW_C)(x)<=W(Jx)-g(Jx).

Multiplication by sqrt(sigma(x)) gives RB8 through the same similarity.
Every original transition from JC is accounted for inside the L block C.
The vector on JC still couples this block to the full problem; replacing it by W_C or by a normalized surrogate would change the certificate.
A successful global Lyapunov construction would require these exact inequalities for every applicable component, together with its finite-region and starting-row expenses.
Neither the componentwise inequalities nor their necessary average payment are verified for a proposed global W here.

### Actual weighted one-step operators and infinitely many unit singular modes

Let l2(D,sigma) have norm squared sum_D sigma(x)|f(x)|^2.
Each sigma(x) is positive and finite, so finitely supported vectors are dense: truncate the nonnegative convergent norm sum.
The equality sigma(Jx)=sigma(x) and J^2=identity make mathsf J a selfadjoint unitary on this space.

The finite components give an orthogonal decomposition of this Hilbert space.
The previous row estimate makes every L_C a contraction; summing their nonnegative norm inequalities makes their direct sum L a contraction.
Finite conductance symmetry shows selfadjointness on finitely supported vectors, and boundedness extends this equality to the whole Hilbert space.
These assertions require no finite total sigma mass.

The pointwise identity L=mathsf J Q gives Q=mathsf J L.
Hence Q is bounded, its adjoint is L mathsf J, and direct multiplication gives RB9.
This is an identity for the actual sigma-weighted space; it is not the counting-measure identity for P_D.

Because a component is closed and all components partition D, L1_C=1_C on all of D.
Its positive finite mass makes e_C well-defined.
The same identities then give all of RB10, including sigma(JC)=sigma(C).
Distinct components are disjoint, so their normalized indicators are orthonormal.
Their closed linear span is infinite-dimensional, and Q preserves the norm there because Q^*Q acts as the identity.

Nothing in this argument says mathsf J maps a component to itself.
Accordingly Qe_C is generally a different indicator, and the next application of Q need not preserve the same component decomposition.
The result is exact one-step singular geometry only.
In particular C203's raw counting-measure strict two-step contraction cannot be silently transferred through an unbounded H-dependent change of norm.

### Remaining critical branch

The finite block system RB5--RB8 is an actual-H-sensitive constraint and an exact way to test a proposed non-J-invariant drift function.
The obstruction identifies a necessary reciprocal asymmetry that every successful one-step witness must pay.
It neither constructs such a witness nor controls how the full process moves between reflection blocks.

The total mass mu=sum_D sigma, C828's positive-level derivative g'(R), and the positive linear complete-bridge K premise remain undecided by these identities.
A finite block can always be normalized locally, which supplies no normalization of the infinite union.
Likewise infinitely many unit singular modes of one step do not classify recurrence or the mean.
No larger graph, unseen return prefix, alternative stationary law or unrestricted G0001 conclusion is introduced.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision critical-reflection-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T15:49 |
| status | open |
| reason | Fix the complete actual-weighted reflection-block theorem RB1--RB12, reusing C203's existing raw geometry. Root contributed the true-H reversible conversion and J-invariant drift obstruction; original_signed_asymptotic checked and developed the finite actual-H matrices, general antisymmetric payment/certificate and weighted one-step singular modes. Every finite/infinite-mean, operator-space, fixed-step and unresolved global-certificate boundary remains explicit. Whole independent review is outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual critical reflection statement](#statement) | RB1--RB10, actual original law/core/H/sigma, finite components and all pointwise function quantifiers, finite matrix/certificate and weighted one-step singular modes, with every stated limitation. |
| argument | [Complete argument](#complete-argument) | Complete RB1--RB12 derivation, exact old/new scope, fixed kernel convention and core geometry, finite detailed balance/payment, arbitrary invariant-function obstruction, actual-H matrix energy and certificate, and global weighted operator/domain proof. |
| dependency | [Existing raw reflection and paired cosets](Yin_C_G0203_v1.md#decision-isolated-quartic-certificate-review-20261023) | Adopted full-strip original kernel, raw edge reversal/reflection convention and finite paired integer-coset geometry. Raw counting-l2 norms and two-step loss are not imported as Q estimates. |
| dependency | [Actual entire quartic core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals original accessible/coaccessible O-core through C399's complete narrow co-return premise; actual infinitude and all embedding conventions, without a new timing assertion. |
| dependency | [True harmonic critical kernel](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) | Actual true R, positive H<=1, full H=R P_D H and stochastic Q with original p_e in either mean branch; no successful Lyapunov witness or stationary normalization. |
| dependency | [Actual reciprocal occupation weights](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) | Actual sigma=H(H composed with J), positive finite state weights, J-invariance and extended total mu; canonical factors and occupation refer to the original whole law. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T16:10 |
| status | proved |
| reason | Adopt the unchanged complete RB1--RB12 statement and argument after reading the whole fixed proof and the independently reviewed R1025 finding. The actual-H reversible finite blocks, reciprocal drift payment, arbitrary pointwise finite J-invariant one-step obstruction, exact finite matrices and weighted one-step singular modes have complete applicable coverage. Preserve C203's prior raw geometry, all exact accepted input scopes, infinite-total-mass validity and the unresolved critical-mean/global-drift branch. No claim about higher powers, a successful drift witness or the unrestricted Lehmer gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual critical reflection statement](#statement) | RB1--RB10, actual original law/core/H/sigma, finite components and all pointwise function quantifiers, finite matrix/certificate and weighted one-step singular modes, with every stated limitation. |
| argument | [Complete argument](#complete-argument) | Complete RB1--RB12 derivation, exact old/new scope, fixed kernel convention and core geometry, finite detailed balance/payment, arbitrary invariant-function obstruction, actual-H matrix energy and certificate, and global weighted operator/domain proof. |
| dependency | [Existing raw reflection and paired cosets](Yin_C_G0203_v1.md#decision-isolated-quartic-certificate-review-20261023) | Adopted full-strip original kernel, raw edge reversal/reflection convention and finite paired integer-coset geometry. Raw counting-l2 norms and two-step loss are not imported as Q estimates. |
| dependency | [Actual entire quartic core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals original accessible/coaccessible O-core through C399's complete narrow co-return premise; actual infinitude and all embedding conventions, without a new timing assertion. |
| dependency | [True harmonic critical kernel](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) | Actual true R, positive H<=1, full H=R P_D H and stochastic Q with original p_e in either mean branch; no successful Lyapunov witness or stationary normalization. |
| dependency | [Actual reciprocal occupation weights](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) | Actual sigma=H(H composed with J), positive finite state weights, J-invariance and extended total mu; canonical factors and occupation refer to the original whole law. |
| review | [Whole independent critical-reflection finding](../audits/reviews/Yin_R_G1025_v1.md#whole-critical-reflection-finding) | Complete fixed RB1--RB12 statement and argument, all four dependency interfaces, finite/killed function quantifiers and infinite-mass operator domains; independent analytic review without new native execution or formal verification. |

