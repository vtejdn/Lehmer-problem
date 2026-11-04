---
author: Yin
---

# An effective gap for every positive factor of a fixed delay seed

Current checking scope is owned by [R560](../audits/reviews/Yin_R_G0560_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-08.
Prepared by assigned AI `growth_arithmetic_status` for Yin and the coordinating AI during the current bounded G0001 round.
The coordinator proposed the reciprocal-gcd reduction, monotone unit-circle phase count, exterior-root separation, and all-factor gap mechanism.
This agent checked the complete mechanism and supplied the single-circle separation estimate, rational thresholds, and finite initial-root algorithm below.
These are collaborative contributions; neither contributor is an independent reviewer of the complete proof.
The completed checking account is retained below at its responsible finding scope.

No new source acquisition, numerical experiment, source-proof audit, or novelty claim is a premise.
The contextual predecessor is [L G0133](Yin_L_G0133_v1.md), whose final scope left multiple noncyclotomic factors of a fixed-seed delay family open.
The proof below does not use Smyth's theorem, Lawton's theorem, a Salem construction theorem, or an irreducibility classification.
It uses elementary polynomial algebra, the argument principle and its elementary contour-homotopy consequence, and standard effective arithmetic and root isolation for algebraic numbers.
Positivity of the factor's Mahler measure is an explicit hypothesis, so Kronecker's theorem is not needed for the gap itself.

<a id="effective-fixed-seed-factor-gap"></a>
## 1. Statement and conventions

Fix a monic f in Z[t] with f(0) in {1,-1}; degree zero is permitted, in which case f=1.
Let s=deg f, and put

    f*(t)=t^s f(t^(-1)),
    F_(N,sigma)(t)=t^N f(t)+sigma f*(t),
                  N>=1, sigma in {1,-1}.                  (1)

Every F_(N,sigma) is monic of degree N+s, has constant coefficient sigma, and satisfies

    F_(N,sigma)*=sigma F_(N,sigma),                         (2)

where this reversal has degree N+s.
Roots, including all counts and products below, are counted with multiplicity unless distinctness is explicitly asserted.

**Claim.** From f one can compute a positive integer T_f such that, with B_f=1+1/T_f, every root alpha of every polynomial in (1) satisfies precisely one of

    |alpha|<B_f^(-1),       |alpha|=1,       |alpha|>B_f.    (3)

Consequently, every monic irreducible factor P in Z[t] of any F_(N,sigma) with positive logarithmic Mahler measure satisfies

    m(P)>log B_f>=1/(T_f+1)>0.                             (4)

Thus a positive rational lower bound is effectively obtainable from the seed.
The same conclusion applies to any monic factor with positive measure; irreducibility is not used to prove the inequality.
In particular it applies simultaneously to all positive irreducible factors, regardless of how many occur or how they depend on N.

Effectivity means a terminating exact algorithm for the particular fixed input f.
No practical complexity estimate, uniform numerical bound over all seeds, or executed computation is asserted.
The bound is for m(P)=log M(P), not for the normalized height m(P)/deg P.

<a id="reciprocal-gcd-removal"></a>
## 2. Remove the entire reciprocal gcd, with multiplicities

Let g be the monic greatest common divisor of f and f* in Q[t], and let h=f/g.
Gauss's lemma implies g,h are monic integer polynomials.
Their integer constant coefficients multiply to f(0), so both are in {1,-1}.
Put eta=g(0), r=deg h.

The polynomial g* divides both f* and f.
Its leading coefficient is eta, so eta g* is a monic common divisor of the same degree as g.
By the defining gcd property,

    g*=eta g,
    f*=eta g h*,
    gcd(h,h*)=1.                                          (5)

The final assertion follows by substituting f=g h and f*=eta g h* into gcd(f,f*)=g.
This removes the whole common gcd, including repeated factors; a squarefree gcd would not suffice.
Reversal of each polynomial here is with its own degree.
Its nonzero constant coefficient ensures reversal preserves that degree.

No root of h is on the unit circle.
Indeed, if h(beta)=0 and |beta|=1, real coefficients imply

    h*(beta)=beta^r h(beta^(-1))
            =beta^r overline(h(beta))=0,

contradicting (5).
For either sign sigma, the remaining factor is

    F_(N,sigma)=g G_(N,tau),
    G_(N,tau)=t^N h+tau h*,       tau=sigma eta in {1,-1}.  (6)

It is monic of degree N+r, has constant coefficient tau, and

    G_(N,tau)*=tau G_(N,tau).                              (7)

If r=0, then h=1 and G_(N,tau)=t^N+tau has every root on the unit circle.
This case will be completed directly in Section 5; the estimates in Sections 3--4 are only needed when r>=1.

Suppose r>=1.
Let r_in and r_out count the roots of h inside and outside the unit circle, respectively, with multiplicity.
Then r_in+r_out=r.
In fact both are positive: the product of their moduli is |h(0)|=1, and none has modulus one.
In particular there is at least one exterior root to separate.

Choose an integer M>=2 such that every root beta of h satisfies

    ||beta|-1|>1/M.                                       (8)

Such an M can be found effectively by exact algebraic root isolation and comparisons, since h has no unit-circle roots.
Define the rational numbers

    delta=1/(4M),        R=1+delta,

and the integer L_h equal to the sum of the absolute values of the coefficients of h.
These will suffice for all N and both signs.

<a id="exact-unit-circle-root-count"></a>
## 3. Exact unit-circle count from a monotone phase

Since h has no zero on the circle, write on the real theta-axis

    h(e^(i theta))=|h(e^(i theta))| exp(i phi(theta)),

with a continuously differentiable lift phi.
The argument principle, or the winding number of each factor e^(i theta)-beta, gives

    phi(theta+2 pi)-phi(theta)=2 pi r_in.

Logarithmic differentiation gives, with z=e^(i theta),

    phi'(theta)=Re(z h'(z)/h(z))
               =sum_(h(beta)=0) Re(z/(z-beta)).            (9)

This identity includes repeated roots.
Since |z-beta|>=||beta|-1|>1/M, it follows that

    phi'(theta)>-r M.

On the circle, h*(e^(i theta))=e^(i r theta) overline(h(e^(i theta))).
Therefore

    G_(N,tau)(e^(i theta))
      =|h(e^(i theta))| exp(i(r theta-phi(theta)))
         [exp(i W_N(theta))+tau],

    W_N(theta)=(N-r)theta+2 phi(theta),
    W_N'(theta)>N-r-2rM.                                 (10)

Set

    N_ph=r+2rM+1.

For every N>=N_ph, the phase is strictly increasing, and

    W_N(theta+2 pi)-W_N(theta)
       =2 pi(N-r+2r_in)=2 pi(N+r-2r_out).                  (11)

The last integer q_N=N+r-2r_out is positive.
A strictly increasing continuous phase with increase 2 pi q_N crosses the equation exp(i W_N)=-tau exactly q_N times in a half-open period, for either sign tau.
Thus G_(N,tau) has exactly

    N+r-2r_out                                             (12)

distinct unit-circle roots.
They are simple as polynomial roots: differentiate (10) at a zero.
The nonvanishing prefactor and W_N'>0 give a nonzero theta-derivative, which equals i e^(i theta) G_(N,tau)'(e^(i theta)).

By (7), inversion maps off-circle roots to off-circle roots on the opposite side, with the same multiplicity.
Its degree N+r and (12) leave exactly 2r_out off-circle roots.
Consequently, for N>=N_ph, there are precisely r_out roots outside the unit circle and r_out inside, counted with multiplicity.
This proves the exact count; neither a lower bound on the number of circle roots nor an asymptotic winding statement would suffice for the next step.

<a id="uniform-exterior-root-separation"></a>
## 4. One contour separates every exterior root

On the circle |z|=R=1+delta, (8) gives, for every root beta of h,

    |z-beta|>=||beta|-R|>3delta.

For an exterior root the lower bound follows from |beta|>1+1/M=1+4delta; for an interior root the stronger lower bound 5delta follows from |beta|<1-4delta.
Since h is monic,

    |h(z)|>(3delta)^r,
    |h*(z)|<=L_h R^r.                                    (13)

The second estimate uses the unchanged coefficient sum under reversal and R>=1.
Find the first integer a>=0 for which

    R^a(3delta)^r>L_h,                                   (14)

and put N_R=r+a.
This search uses only exact rational powers and comparisons and terminates because R>1.
For N>=N_R, (13)--(14) give, on the complete contour |z|=R,

    |z^N h(z)|>|h*(z)|.

For clarity, the root-count principle needed here can be applied directly by the contour homotopy

    z^N h(z)+u tau h*(z),       0<=u<=1.

The strict inequality keeps the entire homotopy nonzero on |z|=R.
Its winding number, and therefore its number of zeros inside that circle counted with multiplicity, are constant.
At u=0 there are N+r_in zeros inside: the N zeros at zero and exactly the r_in interior roots of h.
Every exterior root of h has modulus >R.
Thus G_(N,tau) has exactly r_out roots outside |z|=R and none on that contour.
This is the usual Rouché argument with all constants specified.

Let

    N_*=max(N_ph,N_R).                                    (15)

For every N>=N_* and both signs tau, Section 3 counts r_out roots outside 1, while this contour counts the same number outside R.
There are therefore no roots in 1<|z|<=R.
All exterior roots satisfy |z|>R, including repeated exterior roots.
By reciprocity, all interior roots satisfy |z|<R^(-1).
The remaining roots are the simple roots on the unit circle counted in (12).
The estimates are uniform in N and the choice of sign for this fixed h.

No separate discs, separation between distinct exterior roots, or simplicity of those roots is required.
In particular the proof does not exclude or discard repeated roots of the seed.

<a id="finite-initial-delays-and-factor-gap"></a>
## 5. Include the fixed gcd and every initial delay effectively

For r>=1, keep R and N_* from (8)--(15).
For r=0 set R=2 and N_*=1 instead; then every residual G_(N,tau)=t^N+tau has only unit-circle roots, so the large-delay conclusion holds in that case without any root isolation of h.

Form the finite list A of the moduli strictly greater than one of roots of the following polynomials:

    g;
    F_(N,+1) and F_(N,-1), for 1<=N<N_*.

Multiplicity may be retained or omitted in this finite minimum.
The list can be empty.
Compute its members and their comparisons with one by exact algebraic root isolation.
All polynomials have integer coefficients and are nonzero.
This is a finite task on at most 2(N_*-1)+1 polynomials; their total degrees are

    deg g+(N_*-1)N_*+2s(N_*-1).

No irreducible factorization of any delay polynomial is necessary for this construction.
Exact comparison decides unit modulus even when those finite polynomials have repeated or unit-circle roots.

Choose the first integer T_f>=1 such that

    1+1/T_f<R,
    1+1/T_f<a for every a in A.                            (16)

This is another terminating exact search: R>1 and every member of the finite list A is >1.
Empty-list conditions are vacuous.
Put B_f=1+1/T_f.

Let alpha be any exterior root of any F_(N,sigma).
If N<N_*, its modulus belongs to A.
If N>=N_*, the factorization (6) puts it either among the fixed roots of g, again listed in A, or among the roots of G_(N,tau), where Section 4 gives |alpha|>R when r>=1.
For r=0 the residual has no exterior roots.
Thus in every case |alpha|>B_f.
The reciprocal symmetry (2) implies the matching interior bound |alpha|<B_f^(-1).
This proves (3).

Every monic factor P of F_(N,sigma) has Mahler measure given by

    M(P)=product_(P(alpha)=0) max(1,|alpha|).

If m(P)>0, at least one of its roots is exterior.
The root bound then gives M(P)>B_f and m(P)>log B_f.
Finally, for x>0,

    log(1+x)=integral_0^x dt/(1+t)>=x/(1+x),

so log B_f>=1/(T_f+1).
This proves (4).
In particular positive irreducible factors have an effective rational gap.
Such factors are automatically unit polynomials because the constant coefficient of the whole monic integral polynomial is +/-1.
If one wishes to replace the explicit phrase "positive measure" by "noncyclotomic", the usual Kronecker characterization may be used at its retained interface in [Smy08 U001](../audits/literature/Smy08/Yin_U001.md).
That characterization is not needed for any estimate above.

<a id="fixed-seed-factor-gap-scope"></a>
## 6. Effectivity, comparison, and the unresolved scope

The complete effective recipe is: compute the monic gcd g and h=f/g exactly; if h is nonconstant, choose M by its algebraic radial separation, compute the rational threshold (14), and take (15); isolate roots of the explicitly finite initial list and of g; then perform the integer search (16).
Every search terminates for the reasons proved above.
The output 1/(T_f+1) is a positive rational number.
The construction is effective even though its threshold and finite list may be large; neither a numerical value nor an implementation run is claimed in this record.

This strengthens the fixed-seed boundary of L G0133 in a different direction from its full-polynomial Mahler limit.
That earlier limit does not by itself exclude small positive factors when several noncyclotomic factors occur.
Here every positive factor of both twists at every delay is covered, with no uniqueness of the core, cyclotomic-degree bound, or factor degree-growth hypothesis.
The reason is the effective separation of every exterior root, not an inference from the sum of the factors' measures.

The constant depends on the actual seed through its residual radial separation and its finite early polynomials.
No lower bound independent of f is supplied.
A fixed finite collection of seeds also has a positive effective gap, by taking the minimum of their constants.
To seek measures tending to one through this precise delay construction, one must therefore leave every fixed finite seed collection.
Varying the seed is a necessary possibility left open, not a sufficient construction of near-one inputs.
This does not establish a Lehmer gap, arithmetic coverage for all inputs, or a solution of G0001.


## Contributions and actual review

The coordinator proposed the reciprocal-gcd reduction, monotone phase count, exterior-root separation and all-factor gap, and checked the complete final (1)--(16).
The assigned growth_arithmetic_status AI verified that mechanism, supplied the single-contour separation, exact rational thresholds and finite initial-root algorithm, and authored the assembled proof.
These are collaborator checks.

On 2026-10-08, the separately assigned execution_and_deliverables AI for Yin independently checked every (1)--(16) and the complete Sections 1--6.
The question and proof outline were supplied beforehand, so this was not a blind review.
The reviewer contributed no proof mechanism or file correction.
It rederived the full monic reciprocal gcd including multiplicities, residual coprimality and exclusion of unit-circle roots, both twist identities, the constant residual and f=1 cases, continuous phase lift and winding, exact simple circle-root count, inverse-root multiplicities, and both strict rational large-delay thresholds.
It checked that the one-contour homotopy accounts for every exterior root, that finite root isolation includes both signs and every initial delay plus the fixed gcd, and that the final strict annular separation implies the positive rational bound for every positive monic factor.
It also checked the effective finite recipe, degree sum, empty list, and fixed-seed versus varying-seed limitations.
No substantive defect or missing hypothesis was found.

This is complete independent written-proof review.
It does not claim formal verification, execution of the root-isolation recipe, or an audit of source-original proofs.
The argument does not use Smyth, Lawton, a Salem construction, or Kronecker for its positive-factor inequality.
The coordinator accepted it for fixed-ledger preservation on 2026-10-08 under the current G0001 instruction.
The unrestricted Task remains unresolved.
