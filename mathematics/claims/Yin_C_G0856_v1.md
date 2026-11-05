---
author: Yin
---

# Critical-return mean under full-degree root extension

Human author Yin.
Contributor original_law derived the complete RM1--RM5 argument and its radical obstruction to an unrestricted uniform-mean strategy.
This is a project deduction completed on 2026-11-05, Asia/Shanghai, using the exact retained inputs below.
The complete statement and necessary argument are retained here; the selected decision below owns their assessment.
The earlier [C493 actual-core product](Yin_C_G0493_v1.md#radical-actual-core-product), [attainment equivalence](Yin_C_G0493_v1.md#radical-attainment-equivalence) and [golden controls](Yin_C_G0493_v1.md#nontorsion-radical-attainment-controls) already contain the mean scaling and fixed-measure obstruction in Parts A--B.
Part C is also the critical-law, z=1 specialization of [C511's excursion-entropy inequality](Yin_C_G0511_v1.md#prescribed-zero-mass-frontier), equation (6).
This file retains its explicit Task-facing synthesis, separate direct derivation and actual independent review; it adds no mathematical coverage beyond those earlier interfaces.

## Statement

For an algebraic unit gamma, let p_n(gamma) be the complete return probability at time n from zero for the chronological process X_(n+1)=gamma X_n+eta_(n+1), with independent digits -1,0,1 of probabilities 1/4,1/2,1/4.
Set p_0(gamma)=1, and let f_n(gamma), n>=1, be the first-positive-return probabilities, excluding nonreturning paths.
Use natural logarithms and put

    h_2(gamma)=lim_(n->infinity)-log p_n(gamma)/n,
    R_gamma=exp(h_2(gamma)),
    U_gamma(z)=sum_(n>=0)p_n(gamma) z^n,
    F_gamma(z)=sum_(n>=1)f_n(gamma) z^n,
    mu_gamma=sum_(n>=1)n R_gamma^n f_n(gamma).

The derivative sum mu_gamma is called a critical mean only when F_gamma(R_gamma)=1.
The zero-time term belongs only to U_gamma; the original positive one-step zero-digit return belongs to F_gamma and mu_gamma.

**A. Exact mean scaling.**
Let alpha and beta be algebraic units, r>=1 an integer, alpha^r=beta, and [Q(alpha):Q(beta)]=r.
If

    F_beta(R_beta)=1 and mu_beta<infinity,

then

    R_alpha=R_beta,
    F_alpha(R_alpha)=1,
    mu_alpha=mu_beta^r<infinity.

Thus critical positive recurrence is preserved under these hypotheses, with the exact displayed change of mean.
No strict first-return-radius gap is assumed or concluded.
Every asymptotic limit is taken at a fixed r.

**B. Actual unbounded means at fixed measure and rate.**
Put phi=(1+sqrt5)/2, r_j=2^j and alpha_j=phi^(1/r_j)>0, for j>=0.
The actual minimal polynomial is the irreducible x^(2r_j)-x^r_j-1, the critical first-return law is a probability, and

    1<mu_phi<infinity,
    mu_(alpha_j)=mu_phi^(2^j)->infinity,
    R_(alpha_j)=R_phi,
    h_2(alpha_j)=h_2(phi)>=log(8/5)>0,
    m(alpha_j)=log(phi)>0.

Consequently no finite critical-mean upper bound on all algebraic units can depend only on the Mahler measure or only on the collision entropy while being finite at this actual scalar value.
These examples are nonreciprocal, their j>0 members have degree-lowering powers, and their Mahler measures do not tend to one.
They do not refute an estimate essentially restricted to a justified reciprocal power-stable near-one class.

**C. Precise remaining uniformity interface.**
For any critically recurrent algebraic unit with h=log R>0 and finite critical mean mu,

    h mu>=-log F(1).

Thus simultaneous actual uniform bounds F(1)<=c0<1 and mu<=M would give h>=(-log c0)/M and hence the corresponding Mahler lower bound.
The claimed conclusions do not supply that uniform mean estimate, do not classify the retained quartic Salem mean, and do not resolve the unrestricted Lehmer contract.

## Inputs and scope

| Role | Exact input | Used scope |
| --- | --- | --- |
| Dependency | [C212 v1, exact radical collision product](Yin_C_G0212_v1.md#radical-collision-control) | RM2 and RM4: all-length product formula, equality of fixed-input collision rates, golden radical irreducibility, relative degree and fixed Mahler measure. |
| Dependency | [C212 v1, golden finite certificate](Yin_C_G0212_v1.md#golden-ratio-certificate) | RM4: the existing h_2(phi)>=log(8/5) control, after converting its bit convention; no new native run. |
| Dependency | [C212 v1, collision and support/Mahler interface](Yin_C_G0212_v1.md#statement) | RM5: h_2(gamma)<=m(gamma) for algebraic units after converting the bit convention to natural logarithms; retained external-source inspection limits are unchanged. |
| Dependency | [C479 v1, all-unit renewal and critical transform](Yin_C_G0479_v1.md#statement) | RM1--RM3: true radius, complete renewal identity, finite-mean critical transform and its invariant mass at zero. |
| Dependency | [C204 v1, general countable-chain lemma](Yin_C_G0204_v1.md#positive-branch-coupling-proof) | RM2: qualitative convergence for every irreducible countable stochastic chain with an invariant probability and a positive reference loop, as proved before that material's quartic specialization. |
| Dependency | [C526 v1, zero-neutral-place case](Yin_C_G0526_v1.md#actual-critical-polynomial-return) | RM4: actual golden critical recurrence and finite mean, with its fixed-input nonneutral constant. |
| Source attribution | [LL10 retained countable-convergence account](../audits/literature/LL10/readme.md#countable-convergence-attribution) | Classical convergence attribution and recorded inspection limits; the exact general local proof used here is C204's, without a fresh source audit. |
| Comparison input | [C474 v1, complete unweighted return estimate](Yin_C_G0474_v1.md#statement) | RM5 only: F(1)<=1/2+T_d at the stated actual-degree conditions, which does not supply a critical-mean bound. |
| Target and comparison | [Unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract) and [C850 v1 fixed-quartic criterion](Yin_C_G0850_v1.md#first-return-injection-and-strict-equivalence) | RM5 allocation boundary: an input-specific strict quartic tail would not by itself give the uniform estimate in Part C. |

## Complete argument

### RM1. Exact hypotheses, original law and retained inputs

For an algebraic unit gamma, let p_n(gamma) be the probability that the complete original chronological process returns from zero to zero after n steps, using digits -1,0,1 with probabilities 1/4,1/2,1/4.
Set p_0(gamma)=1.
Let f_n(gamma) be its first-positive-return probabilities for n>=1; paths that never return contribute no mass to these coefficients.
Write

    R_gamma=exp(h_2(gamma)),
    U_gamma(z)=sum_(n>=0)p_n(gamma) z^n,
    F_gamma(z)=sum_(n>=1)f_n(gamma) z^n,
    mu_gamma=sum_(n>=1)n R_gamma^n f_n(gamma).

Here h_2 uses natural logarithms, and mu_gamma is the mean of a probability law only when F_gamma(R_gamma)=1.
In a transient critical case the same displayed derivative sum is not called a mean.
The zero-time term belongs to U only; F and mu include the positive one-step zero-digit return.

Let alpha and beta be algebraic units, and suppose r>=1 is an integer, alpha^r=beta, and [Q(alpha):Q(beta)]=r.
Assume beta is critically recurrent and has finite critical mean:

    F_beta(R_beta)=1,  mu_beta<infinity.                 (RM1)

The exact full-degree residue decomposition is already proved in [C212, Section 5](Yin_C_G0212_v1.md#radical-collision-control).
Its collision probability is exactly the original difference-law p_n after reversing the iid digits, and its stated bit entropy converts to the natural-log convention here.
The all-unit renewal and critical transform are in [C479](Yin_C_G0479_v1.md#statement).
For the only countable-chain convergence used below, [C204, Section 2](Yin_C_G0204_v1.md#positive-branch-coupling-proof) gives a complete elementary proof for every irreducible countable stochastic chain with a positive loop at its reference state and an invariant probability.
That lemma is not restricted to the later quartic application.
Its classical attribution and actual source-inspection limit remain at [LL10's retained convergence account](../audits/literature/LL10/readme.md#countable-convergence-attribution).
No fresh source theorem or numerical experiment is needed for this direct consequence.

### RM2. Product of complete returns and the critical limit

For n=kr+s with k>=0 and 0<=s<r, C212 gives

    p_(kr+s)(alpha)=p_(k+1)(beta)^s p_k(beta)^(r-s),
    R_alpha=R_beta=:R.                                  (RM2)

The relative-degree hypothesis makes 1,alpha,...,alpha^(r-1) linearly independent over Q(beta), so vanishing of the full digit sum is equivalent to vanishing in every residue coordinate.
The coordinates use disjoint iid digits, which explains the product and retains every original word weight.
This is a formula for complete returns, not for first-return coefficients.
One must not factor f_n by residue coordinates, because an earlier simultaneous zero is a joint event.

Put a_n(gamma)=R^n p_n(gamma).
Under RM1, C479 gives the actual positive recurrent critical transform Q_beta with invariant mass pi_beta(0)=1/mu_beta and Q_beta(0,0)=R/2>0.
The exact telescoping identity gives Q_beta^n(0,0)=a_n(beta).
Applying the stated general countable-chain lemma therefore gives

    a_n(beta)->1/mu_beta.

Multiplication of RM2 by R^(kr+s) yields

    a_(kr+s)(alpha)=a_(k+1)(beta)^s a_k(beta)^(r-s)
                    ->mu_beta^(-r)=:c>0.               (RM3)

There are only r residue classes, so this is a limit along all n for each fixed r.
No limit uniform in a growing r is asserted or used.

### RM3. Recovering recurrence and the exact new mean without a converse limit theorem

The closed-word concatenation inequality gives 0<=a_n(alpha)<=1.
A direct finite-initial-segment and bounded-tail split in the geometric average proves from RM3 that

    (1-u) U_alpha(Ru)
       =(1-u)sum_(n>=0)a_n(alpha)u^n ->c,
                                   as u increases to1. (RM4)

Indeed, for every epsilon>0 choose N such that |a_n(alpha)-c|<epsilon for n>=N.
The initial finite sum, multiplied by 1-u, tends to zero; the absolute tail contribution is at most epsilon.

Since c>0, U_alpha(Ru) tends to infinity.
The complete nonnegative renewal identity U_alpha=1/(1-F_alpha) implies F_alpha(R)=1 by monotone convergence.
Consequently

    (1-F_alpha(Ru))/(1-u)
       =1/[(1-u)U_alpha(Ru)] ->1/c.

Writing b_n=R^n f_n(alpha), with sum_(n>=1)b_n=1, the same quotient is

    sum_(n>=1)b_n(1+u+...+u^(n-1)).

Every summand increases to n b_n, so monotone convergence gives the full critical mean, including all first returns and all original times:

    F_alpha(R_alpha)=1,
    mu_alpha=mu_beta^r<infinity.                         (RM5)

Thus full-degree root extension preserves critical positive recurrence under RM1 but changes its mean by an exact power.
The argument neither assumes nor establishes a strict first-return-radius gap R_f>R.

### RM4. An actual irreducible fixed-measure family with divergent critical means

Take beta=phi=(1+sqrt5)/2 and r=2^j, j>=0, with alpha_j=phi^(1/r)>0.
[C212](Yin_C_G0212_v1.md#radical-collision-control) proves that x^(2r)-x^r-1 is the actual irreducible minimal polynomial, that the relative degree is r, and that every member has Mahler measure phi.
Its [complete golden returning-state calculation](Yin_C_G0212_v1.md#golden-ratio-certificate) is an existing finite control, not a new run.

Neither conjugate of phi lies on the unit circle.
The q=0 case of [C526](Yin_C_G0526_v1.md#actual-critical-polynomial-return) therefore gives F_phi(R_phi)=1 and mu_phi<infinity, with its actual fixed-input nonneutral constant.
The chronological word (1,-1,-1) visits 1,phi-1,0, so it is a first return of length3 with original probability1/64.
Its critical weight R_phi^3/64 is positive, and the critical first-return law is a probability on positive integers.
It follows that mu_phi>1.
Applying RM5 proves

    mu_(alpha_j)=mu_phi^(2^j)->infinity,
    R_(alpha_j)=R_phi,
    m(alpha_j)=log(phi)>0.                               (RM6)

The collision rate is also bounded below by the retained C212 certificate h_2(phi)>=log(8/5)>0.
The conclusion uses the n-to-infinity limit separately at every fixed j before letting j grow.
Thus even at one fixed positive collision entropy and one fixed positive Mahler measure, the full critical means admit no common finite upper bound over all algebraic units.
In particular a bound depending only on either of those two scalar values cannot hold on the entire unit domain if it is finite at this value.

These controls are nonreciprocal, and alpha_j has a degree-lowering power for j>0.
Their Mahler measures do not tend to one.
They do not refute a mean bound essentially restricted to an actually justified reciprocal power-stable near-one class, and do not classify the retained quartic mean question.

### RM5. The first missing interface back to the unrestricted gap

For any critically recurrent input with h=log R>0 and finite mean mu, its full critical first-return law b_n=R^n f_n obeys

    F(1)=sum_(n>=1)b_n exp(-hn)>=exp(-h mu),
    h mu>=-log F(1).                                    (RM7)

For a direct verification, exp(-h(n-mu))>=1-h(n-mu) for every n, and summation against b_n gives the first inequality.
The assumed finite mu justifies summing that linear term and is essential to the stated finite-mean expression.
All times and the original one-step return remain present.
Thus a proved uniform F(1)<=c0<1 together with a proved uniform mu<=M would give h>=(-log c0)/M.
The [retained C212 collision and support/Mahler interface](Yin_C_G0212_v1.md#statement) gives h_2(gamma)<=m(gamma) in natural logarithms and hence the corresponding Mahler lower bound, with its existing source-inspection limits unchanged.
The [actual all-unit estimate in C474](Yin_C_G0474_v1.md#statement), F(1)<=1/2+T_d, supplies such an unweighted bound for sufficiently large actual degree; it supplies no critical-mean upper bound.
RM6 excludes the latter bound over the whole algebraic-unit domain, and finite mean on each input does not repair that quantifier.

A successful fixed quartic r_I<1/R would only establish a finite input-specific mean and would stop before this uniform interface.
Further work on that fixed control is therefore not selected as a substitute for a mechanism on the unrestricted inputs.
The precise unresolved possibility is an appropriately reduced near-one estimate with all reduction, degree and original-law costs paid, or a different uniform information bound not requiring this mean cap.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T16:24 |
| status | proved |
| reason | Adopt the complete critical-mean scaling theorem, actual fixed-measure unbounded-mean family and conditional uniformity interface after the whole independent R1073 finding. The reciprocal power-stable near-one class and fixed-quartic strict-tail question remain unresolved; this is not G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire Parts A--C, with the full relative-degree, critical recurrence, finite-mean and fixed-parameter hypotheses and all exclusions. |
| argument | [Complete argument](#complete-argument) | RM1--RM5, including the true original-law product, recovery of the critical mean, actual radical family and fully paid Mahler interface. |
| dependency | [Full-degree collision and rate inputs](Yin_C_G0212_v1.md#statement) | Existing all-length product, actual golden family, rate normalization and collision-to-Mahler interface at their retained source scope. |
| dependency | [Critical transform](Yin_C_G0479_v1.md#statement) | Full original-law renewal and finite-mean critical occupation, with all endpoint hypotheses. |
| dependency | [Countable convergence](Yin_C_G0204_v1.md#positive-branch-coupling-proof) | The general irreducible aperiodic countable-chain convergence proof before its quartic specialization. |
| dependency | [Nonneutral finite mean](Yin_C_G0526_v1.md#actual-critical-polynomial-return) | Only the q=0 actual-input conclusion used for phi, with its fixed-input constant. |
| support | [Unweighted comparison](Yin_C_G0474_v1.md#statement) | High-degree F(1) bound used in the conditional uniformity comparison, without a critical-mean cap. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1073_v1.md#critical-return-mean-scaling-finding) | Complete statement and RM1--RM5 review, exact dependency scopes and unchanged external-proof/native limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
