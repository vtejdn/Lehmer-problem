---
author: Yin
---

# Parity normalization and full Salem tails for the actual quotient process

The complete current mathematical home is [C559](../claims/Yin_C_G0559_v1.md#normalized-quotient-tail-fixed-scope), adopted at 2026-10-22T19:13 after the [actual current whole SELF](../audits/reviews/Yin_R_G0744_v1.md#current-complete-whole-self-finding).
The original dated argument and frozen input below remain the actual input of R138; current links do not backfill that review or supply its missing relationship declaration.

Date: 2026-10-10.
The original2026-10-10 coordinating account adopted this restricted result after its separately organized noncontributor review at the original scope.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="normalized-quotient-tail-fixed-scope"></a>
## Original adopted scope and fixed review input

An explicit parity-periodic positive eigenfunction normalizes the complete weighted integer quotient kernel to a genuine Markov chain with conditionally symmetric digits and bounded conditional variance.
Exact closed-path identities retain original observation probabilities and every finite degree/lag factor.
A martingale estimate removes the former exponential selector loss from the complete Salem quotient-height tail, permitting square-root n log n cutoffs at polynomial absolute tolerance for each fixed input and theta<1.
Every fixed finite arithmetic endpoint projection still has zero return exponent, with an explicit modulus-dependent steering cost.
An actual quartic control is exact; no retained-box sum, relative-error certificate, uniform near-one pressure separation or gap is asserted.


<a id="complete-retained-proof-and-review"></a>
## Complete original author proof and dated review input

## Integer pressure beyond finite parity information

Date: 2026-10-10.
Starting question: Develop a geometry-sensitive continuation of the complete integer return-pressure formula in L235.
Investigate whether finite arithmetic projections, joint occupation constraints or a normalized finite-memory digit representation can discriminate actual integer return from the zero-information binary relaxation.
Aim for genuinely changed full-law bounds or a precise useful boundary; include all integer states, original weights, finite degree costs and varying-input limitations.



<a id="normalized-quotient-reuse"></a>
### Reuse and changed mechanism

The fixed [L235 complete integer pressure](Yin_L_G0235_v1.md#unbounded-quotient-pressure-fixed-scope) retains every returning quotient and proves existence of the genuine partial-observation collision exponent.
Its binary projection has zero normalized exponent; its Salem height tail is absolute and includes an exponential selector factor for theta>0.
[L77](Yin_L_G0077_v1.md#finite-periodic-data-do-not-concatenate), [L79](Yin_L_G0079_v1.md#exact-cyclotomic-crt-defect) and [L81](Yin_L_G0081_v1.md#binary-primitive-entropy-boundary) already warn that fixed finite quotient data do not concatenate into an entropy bound.
A larger fixed quotient is therefore not presumed sufficient.
The original probabilities and the observation-boundary interface remain those of [L227](Yin_L_G0227_v1.md#partial-mask-boundary-linear-fiber).

The new deduction is an explicit positive parity-periodic eigenfunction for L235's weighted kernel on the WHOLE integer state space.
Its direct diagonal normalization gives a genuine Markov law with predictable symmetric digits and controlled conditional variance.
Closed-path weights telescope exactly.
This both strengthens the complete Salem tail and allows an all-modulus, explicitly costed extension of the binary-projection obstruction.
The normalization is the standard positive-eigenfunction construction; older [L181](Yin_L_G0181_v1.md#finite-critical-return-profile) uses a finite critical Doob chain, whose critical eigenvector and recurrence assumptions are NOT reused here.
The present eigenfunction is computed directly, without a critical stationary law, finite core or Perron existence theorem.
Every needed new fact is proved below.
No new source, source-proof acceptance, program or historical novelty claim is involved.

<a id="explicit-periodic-kernel-normalization"></a>
### 1. An explicit positive eigenfunction on every integer state

Let P(t)=sum_(i=0)^d p_i t^i be the actual monic irreducible minimal polynomial of an algebraic unit, p_0=+/-1, and let

    ell=min{i>=1:p_i is odd}, w=d-ell,
    0<=theta<1, z=(1-theta)/(1+theta),
    c=(1+z)/2=1/(1+theta).                            (1)

Torsion is allowed until a Salem hypothesis is introduced.
A state q has integer coordinates (x_(-d)...,x_(-1)).
With a digit e in{-1,0,1}, define its new quotient coefficient and successor by

    x_0=p_0(e-sum_(i=1)^d p_i x_(-i)),
    S_e(q)=(x_(-d+1)...,x_(-1),x_0).

Use the original difference probabilities mu(0)=1/2, mu(+/-1)=1/4.
For j=0,...,ell-1 define the BINARY quantities

    sigma_j(q)=(sum_(i=ell)^d p_i x_(j-i)) mod2,
    B(q)=sum_(j=0)^(ell-1) sigma_j(q),
    s(q)=sigma_0(q),  H_z(q)=z^(B(q)).                (2)

All indices j-i lie between-d and-1.
These are the first ell state parities before fresh digits can enter them.
In particular B is an ordinary integer in[0,ell], H_z(0)=1 and

    z^ell<=H_z(q)<=1.

Let K_z be L235's complete kernel, K_z(q,S_e(q))=mu(e)z^(s(q)).
Its transitions S_e(q) are distinct in the integer state space.
No core, box or quotient is imposed.
Define also

    tau(q)=(s(q)+sum_(i=ell+1)^d p_i x_(ell-i)) mod2,
    b(q,e)=(e mod2)+tau(q) mod2.                     (3)

The displayed sum is empty when ell=d.
Directly shifting the coordinates in(2) gives

    sigma_j(S_e(q))=sigma_(j+1)(q) for j<ell-1,
    sigma_(ell-1)(S_e(q))=b(q,e),
    B(S_e(q))-B(q)=-s(q)+b(q,e).                     (4)

For the last equality of parities, the new x_0 enters with odd coefficient p_ell, x_0 mod2=e mod2+s(q), and all remaining coordinates are the old ones in(3).
This verifies the shift also when ell=1.
Hence

    (K_z H_z)(q)
      =H_z(q) sum_e mu(e) z^(b(q,e))=c H_z(q).      (5)

Indeed mu assigns probability1/2 to each digit parity, so b has total mass1/2 at each of its two possible values, regardless of tau(q).
This is an exact positive eigenfunction at eigenvalue c for EVERY integer q; it is not an eigenfunction postulated from finite approximation.

<a id="predictable-symmetric-martingale-chain"></a>
### 2. The normalized chain and exact closed-word correspondence

Define the genuine Markov transition probabilities on Z^d by

    T_theta(q,S_e(q))
       =K_z(q,S_e(q)) H_z(S_e(q))/(c H_z(q))
       =mu(e) z^(b(q,e))/c.                         (6)

Equation(5) gives row sum one.
Explicitly,

    Pr_theta(e=0 | q)=(1+(-1)^tau(q) theta)/2,
    Pr_theta(e=+1 | q)=Pr_theta(e=-1 | q)
                         =(1-(-1)^tau(q) theta)/4. (7)

Thus the digit has conditional mean zero, with conditional variance in[(1-theta)/2,(1+theta)/2].
Every transition has probability at least delta_theta=(1-theta)/4>0.
The probability of a zero digit at the zero state is (1+theta)/2.
The dependence is through d recent QUOTIENT parities.
No claim is made that it is a fixed-window function of past raw digits, that the e_j are iid, or that the original input law has been changed for free.

There is an exact innovation realization if useful.
Given q, choose b as an independent Bernoulli bit of probability z/(1+z)=(1-theta)/2, then put eta=b+tau(q) mod2.
If eta=0 use e=0; if eta=1 choose a fresh independent fair sign for e.
This gives(7).
The selector eta is state dependent; this description does not identify it with independent thinning of the actual algebraic endpoint.

For any finite path q_0,...,q_n, multiplication of(6) telescopes:

    Pr_theta(path)
       =c^(-n) [H_z(q_n)/H_z(q_0)]
                         product_(j=0)^(n-1) mu(e_j)z^(s(q_j)). (8)

In particular, writing a_n(z)=K_z^n(0,0) and b_n(theta)=T_theta^n(0,0), one has the EXACT closed-path equality, also after restricting to any collection of returned words,

    b_n(theta)=(1+theta)^n a_n(z).                   (9)

The original weights are precisely those in the product on the right of(8).
The auxiliary Markov law is justified by this equality, not substituted for the original binary law without cost.

Let K_n(theta),Q_n(theta) retain L235's meanings: genuine carry collisions after independent partial observation, respectively before and after disclosing the complete2d+w-bit boundary.
For n>=d, its finite comparison becomes

    2^(d-w)(1+theta)^(-ell) b_n(theta)
       <=Q_n(theta)<=2^d(1+theta)^(-ell) b_n(theta),
    K_n(theta)<=Q_n(theta)<=2^(2d+w)K_n(theta),
    2^(-d-2w)(1+theta)^(-ell) b_n(theta)
       <=K_n(theta)<=2^d(1+theta)^(-ell) b_n(theta). (10)

The same first comparison applies termwise to a specified set of genuine quotients.
Therefore the actual exponent I_P(theta) is the negative logarithm of the return-pressure limit of T_theta.
The preceding fixed-input limit and its existence are L235 reuse.
Equation(10) is a stronger finite-time organization: the exponential selector factor has been absorbed into an explicitly normalized, mean-zero Markov law, leaving the displayed finite degree/lag factors.
There is still no l2-radius identification, critical invariant probability, attainment assumption or input-uniform positive exponent.

<a id="all-finite-quotient-pressure-boundary"></a>
### 3. Every fixed finite arithmetic endpoint projection still has zero exponent

Let m>=2 be even.
The chain(6)--(7) projects exactly to the m^d states of (Z/mZ)^d because its integer recurrence is linear affine and its probabilities depend only on parity.
Call the projected matrix T_(theta,m), and put D_m=m^d-1.

Its directed transition graph is strongly connected.
Here is a complete integer argument.
Write S_e(q)=Aq+e v, where v=p_0 times the last standard basis vector, and A is the zero-digit companion update.
Since p_d=1 and p_0=+/-1, A is integral unimodular.
The vectors

    v, A v, ..., A^(d-1)v

form a unimodular integer basis: ordered in this way, their first nonzero coordinates run from the last to the first, each equal to p_0; the resulting matrix is triangular after reversing coordinate order.
On the finite quotient, S_0 and S_+ are permutations.
A semigroup generated by finite permutations contains their inverses, as positive powers.
The group they generate contains S_+ S_0^(-1), which is translation by v, and conjugating by A gives translations by every A^j v.
These translations act transitively by the basis assertion.
Therefore their permitted directed digit paths connect every pair of residues.
This proves graph connectivity for every actual unit, without assuming irreducibility of P modulo m or prime m.

From each residue there is a simple directed path to zero of length at most D_m.
Pad it at zero with zero digits to exactly D_m.
All steps have probability at least delta_theta, including the padding.
Thus

    T_(theta,m)^(D_m)(q,0)>=delta_theta^(D_m),
    delta_theta^(D_m)<=T_(theta,m)^n(0,0)<=1
                              for every n>=D_m.     (11)

The second line sums over the state reached at time n-D_m.
It follows that every FIXED even modulus gives return exponent zero.
This proves a true finite-time lower bound, not an unquantified mixing assertion.
The cost D_m and log(1/delta_theta)=log(4/(1-theta)) can be large and remain explicit.

Since H_z is parity periodic, (8) also descends to this even-modulus quotient, and its closed-path entries satisfy the same equality(9).
Hence the raw K_z quotient pressure is exactly c, and its observation-normalized pressure is one, extending L235's binary case to EVERY even modulus.

More generally, consider ANY fixed finite-index additive subgroup Lambda of Z^d, or finitely many such endpoint tests simultaneously.
Their intersection contains m Z^d for an even positive integer m: the index annihilates each finite quotient, so twice the product of the indices is one possible m.
No invariant-subgroup hypothesis is needed for this comparison.
The event q_n=0 modulo m implies membership in that intersection.
Under T_theta its probability is bounded below by(11); hence the larger event also has zero exponential rate.
For the original potential-weighted paths ending in Lambda, (8) and z^ell<=H_z<=1 give

    c^n Pr_theta(q_n in Lambda)
       <=sum_(q in Lambda) K_z^n(0,q)
       <=c^n z^(-ell) Pr_theta(q_n in Lambda).       (12)

Thus their raw pressure is likewise c and their normalized exponent zero.
This statement is about fixed finite arithmetic ENDPOINT projections.
It does not exclude increasing moduli, intermediate geometric restrictions, nonperiodic tests or other coupled finite certificates.

There is a quantitative growing-modulus boundary as well.
From(11), whenever n>=m^d-1,

    0<=-log T_(theta,m)^n(0,0)/n
       <=[(m^d-1)/n] log(4/(1-theta)).               (13)

Consequently if a sequence of actual inputs, even moduli, disclosure parameters and times satisfies the right-hand side tending to zero, this projected rate necessarily tends to zero, regardless of their measures.
For fixed d and theta, m(n)^d=o(n) is sufficient.
Varying d and theta retain the full displayed cost; no fixed-degree estimate has been declared uniform.
This does not say that a larger or faster-growing modulus is sufficient for the true integer rate.

<a id="normalized-salem-full-height-tail"></a>
### 4. A stronger complete Salem tail without exponential selector loss

Assume now that P is a Salem polynomial of degree d=2s+2 with s>=1, real roots beta>1,beta^(-1), and neutral pairs zeta_l,bar zeta_l.
Keep the exact L235 constants

    C_0=1/(|P'(beta)|(beta-1))
           +1/(|P'(beta^(-1))|(1-beta^(-1))),
    C_1=2 sum_(l=1)^s 1/|P'(zeta_l)|.              (14)

For EVERY returned digit path and H=E/P, L235's partial-fraction argument proves

    ht(H)<=C_0+C_1 max_(0<=j<n,1<=l<=s)
                         |sum_(k=0)^j e_k zeta_l^k|. (15)

This is a deterministic returned-path statement: it uses the exact contracting-place endpoint and all neutral pairs, so it remains valid under T_theta.
No finite quotient alphabet or degree-uniform root separation is assumed.

Under T_theta the increments e_j have conditional mean zero, and their conditional nonzero probability v_j is at most v_*=(1+theta)/2, where v_*>=1/2.
For any real a with |a|<=1 and any real t,

    E_theta[exp(t a e_j) | past]
      =1-v_j+v_j cosh(ta)
      <=1-v_*+v_* cosh(ta)
      <=exp(v_* t^2 a^2/2).                         (16)

To prove the final inequality directly, for v>=1/2 and u>=0 differentiate log(1-v+v cosh u).
Its derivative is v sinh u/(1-v+v cosh u).
The denominator is at least(1+cosh u)/2; thus sinh u divided by the denominator is at most2tanh(u/2)<=u.
Integration from zero gives log(1-v+v cosh u)<=v u^2/2; evenness covers negative u.
This proves(16) without independent increments or an uninspected concentration theorem.

Normalize the exponential of a real or imaginary neutral partial sum by its actual conditional moment-generating factors.
The resulting positive process has conditional expectation preserved.
Stopping at the first finite crossing, partitioning by its time and conditioning each step proves its stopped expectation is one.
Each factor is bounded by(16), so the same finite-crossing estimate and optimization as in L235 now give

    Pr_theta{max_(j<n,l)|sum_(k=0)^j e_k zeta_l^k|>R}
             <=4s exp[-R^2/(2(1+theta)n)].          (17)

Indeed for one signed real coordinate the exponent is -u^2/(2v_*n); use u=R/sqrt2, both signs, both coordinates and all s pairs.
The adapted state-dependent digit probabilities cause no independence assumption: conditional mean zero and the conditional bound(16) suffice.

Let b_n^(>H_*) be the T_theta mass of all exact-return paths whose integer quotient has height greater than H_*>C_0.
Combining(15)--(17), and then the termwise closed-path comparison(10), proves

    b_n^(>H_*)<=4s exp[-(H_*-C_0)^2/(2(1+theta)n C_1^2)],
    0<=Q_n(theta)-Q_n^(<=H_*)(theta)
       <=2^(d+2)s(1+theta)^(-ell)
                    exp[-(H_*-C_0)^2/(2(1+theta)n C_1^2)]. (18)

Q_n^(<=H_*) is the exact retained original-observation sum, with all true selector ranks, observed-value weights and boundary averages.
It is not a renormalized conditional law.
All integer signs, all parities and all heights above the cutoff have been summed.
In contrast to L235's earlier valid bound, no factor (1+theta)^n remains.
The variance cost1+theta is retained.
At theta=0 the concentration constant agrees with the old original-iid calculation; for theta>0 this organization changes the time cost, rather than only adjusting a numeric prefactor.

For any prescribed0<epsilon<=1 and n>=d, the cutoff

    H_*=C_0+C_1 sqrt(2(1+theta)n[
             (d+2)log2+log s-ell log(1+theta)+log(1/epsilon)]) (19)

makes the omitted Q mass at most epsilon.
The bracket is positive because ell<=d and log(1+theta)<log2.
For each fixed input and theta<1, polynomial tolerance epsilon=n^(-a), a>0, requires only O(sqrt(n log n)) height.
Exponentially small tolerance still needs a linear-in-n height with the full constants in(19).
These are ABSOLUTE errors; neither polynomial error nor a fixed finite box is asserted to approximate an exponentially small return relatively.

There is also an explicit full ORIGINAL binary-law upper bound.
Let T_(theta,H_*) be the submatrix on the finite box of integer coordinates |q_i|<=H_*, with exiting mass killed.
Its zero-to-zero entry counts exactly the quotients with ht(H)<=H_*; there are no extra returns inside or outside the box.
For n>=d and H_*>C_0, combining p_n<=2^(2d)Q_n from L227 with(10),(18) gives

    p_n<=2^(3d)(1+theta)^(-ell) [T_(theta,H_*)^n(0,0)
             +4s exp[-(H_*-C_0)^2/(2(1+theta)n C_1^2)]]. (20)

This is an upper bound for the complete original p_n, not merely the new Markov return law.
The finite matrix has at most(2 floor H_*+1)^d states, and its probabilities are rational when theta is rational.
No entries or powers of it have been computed in this round.
Its retained entry and its full omitted error are distinct obligations; a fixed-box spectral radius alone gives no upper bound on the complete return pressure.
Formula(20) is a finite-time interface with every original-law, degree and truncation cost retained, not a proved uniform exponent.

<a id="quartic-normalized-chain-exact-control"></a>
### 5. The actual infinite-core quartic has a simple parity-controlled law

Use the retained actual Salem polynomial P=t^4-t^3-t^2-t+1, whose infinite core is fixed in [L169](Yin_L_G0169_v1.md#quartic-infinite-core-theorem).
Here ell=1,w=3 and

    x_0=e+x_(-1)+x_(-2)+x_(-3)-x_(-4),
    s(q)=(x_(-1)+x_(-2)+x_(-3)+x_(-4)) mod2,
    tau(q)=x_(-4) mod2,
    H_z(q)=z^(s(q)).                                  (21)

The formula for tau follows by cancelling the three overlapping parities in(3), not by assuming independent quotient bits.
At theta=1/2 the normalized law assigns digit probabilities(0,+1,-1) equal to(3/4,1/8,1/8) when the oldest quotient coordinate is even, and(1/4,3/8,3/8) when it is odd.
It is a martingale digit law with infinitely many integer states, controlled only by their parity.
This is an exact auxiliary representation of the original partial-observation experiment through(8)--(10), not a claim that the original digits already have these probabilities.

There are complete short-word checks without a program.
At n=4, only the zero polynomial can return, so

    b_4(theta)=[(1+theta)/2]^4.

At n=5 the only quotients are H=0,+1,-1.
The two nonzero words are plus or minus P; their first four nonzero digits see even oldest coordinate and their last sees an odd one.
Thus

    b_5(theta)=(1+theta)^5/32
                       +(1+theta)(1-theta)^4/512.   (22)

The same expression follows independently from(7) of L235: the zero word has mass1/32, the two nonzero words have total original mass1/512 and wt(FU)=4, and(9) multiplies their sum by(1+theta)^5.
At theta=1/2, b_5=3891/16384, including zero-word mass3888/16384.
For the actual observation itself, N=1 and its four active rows are identical.
If no row is disclosed, Q_5=(1+1/16)/2=17/32; if at least one is disclosed, the internal bit is fixed.
Therefore

    Q_5(theta)=1-(15/32)(1-theta)^4,
    Q_5(1/2)=497/512.                                (23)

This demonstrates explicitly that the auxiliary return probability and the real observed collision are not equal without the charged comparison.
It also checks the weights of genuine nonzero quotient paths.

The actual constants C_0,C_1 have the exact radical expressions retained in [L235's quartic specialization](Yin_L_G0235_v1.md#quartic-unbounded-parity-tail-control).
At theta=1/2, s=1 and d=4, (18) becomes

    Q_n-Q_n^(<=H_*)<=(128/3)
                  exp[-(H_*-C_0)^2/(3n C_1^2)].      (24)

For example H_*=C_0+C_1 sqrt(3n[log(128/3)+a log n]) ensures full omitted mass at most n^(-a), for n>=4.
The old valid estimate at the same positive theta had an exponential(3/2)^(n-1) expense and required a linear height for that polynomial tolerance.
The new statement removes that expense by the exact normalized martingale law.
Neither formula evaluates the retained mass, bounds the critical mean, or produces near-one input coverage.

### 6. Contribution, self-check scope and unresolved pressure separation

The coordinator supplied only the broad question.
The structural_research author developed the explicit H_z and shift identity, the normalized transition probabilities and closed-path telescoping, the costed every-modulus obstruction, the adapted martingale tail and full original-law finite-box inequality, and the exact quartic checks.
The positive-eigenfunction change of kernel, finite-group connectivity and exponential-martingale ideas are standard elementary mechanisms; the needed instances are proved here and no general novelty is asserted.
The retained L235/L227 original law and partial-fraction interfaces are reused exactly.
No critical Fourier or stationary occupation conclusion from L236 is transferred to this different chain.

The new concrete target is now the complete return probability of the explicit parity-controlled martingale chain.
Its full finite congruence projections have zero exponent, with(13) quantifying a growing-modulus range that also loses the rate.
Its neutral quotient tail has the complete finite-time upper bound(18), and(20) states what a retained computation would still have to establish about the mass that remains.
A pressure separation requires an actual integer-geometry argument beyond finite congruences and beyond concentration of unrestricted trajectories.
The displayed conditional variance floor does not establish such separation; even torsion inputs satisfy it.
Fixed degree, root-derivative constants, disclosure parameter, state-box size and chronological time cannot be dropped from a varying-input assertion.
All actual states and original probabilities remain accounted for, while the uniform near-one gap stays open.


The complete original author SELF account is retained in [R744](../audits/reviews/Yin_R_G0744_v1.md#original-g239-author-self-finding), at its original input and date precision.
No inference from variance alone, a finite quotient, critical attainment or a stationary Fourier law is made.

Author freeze: 2026-10-09T22:58.
Complete Sections1--6, equations(1)--(24), source/reuse and contribution boundaries, all original-law finite costs and the actual quartic control were the original frozen input of the subsequently recorded full noncontributor review.
Independent review and adoption were separate subsequent actions in that original author account.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0780_v1.md#normalized-integer-pressure-complete-independent-review), with its original inspected scope and relationship.
