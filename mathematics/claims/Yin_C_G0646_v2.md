---
author: Yin
---

# Opposite trace-cluster cycles, distance diversity and original degree bounds

Human author Yin.
The original opposite-cycle theorem below retains the contributions of root and paid_comparison: the full weighted baseline, residual ratio, complete local-root count, necessary finite tripling cancellation, integer/parity refinement and primitive-order31 example.
For the present extension, root supplied the constant-distance separation and distance-diversity argument and the later local(1,2,1) obstruction and five-thirds degree candidate.
Original_law checked and completed these arguments as a contributor and derived the intervening adjacent-unit-multiplicity degree bound.
All three are contributors, not independent reviewers of this revision.
The complete mathematics of the adopted physical v1 is retained below; its fixed decisions and review remain at their exact predecessor locators.
This revision adds necessary original-field restrictions, not a complete opposite-cycle exclusion or an original realization.
No native computation, residue scan, new source acquisition or general-source proof upgrade is used.

## Statement

Let P be the ACTUAL monic irreducible reciprocal nontorsion polynomial in Z[z], with P(0)=1 and degree d=2r.
For an original root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and F=Q(delta).
Assume the actual trace field F is totally real, as in the fixed C624v5 domain.
The exact degrees and trace polynomial are

    [K:F]=2, [F:Q]=r,
    P(z)=z^r T(z+z^(-1)), T in Z[X] monic irreducible of degree r.

Use the integral trace polynomials C_0=2,C_1=X,C_(n+1)=X C_n-C_(n-1), and specifically

    C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X,
    a=T(C2(delta))/2, b=T(C3(delta))/3, c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

The elements a,b,c are the actual NONZERO algebraic integers in Z[delta].
Impose the complete residual equations

    f=0, e+s g=0, g!=0, s in{1,-1}.                           (OC1)

In particular e=-s g is nonzero.
These are trace elements in the original field F; they are not replacements by arbitrarily prescribed local values.

Let Phi_0,...,Phi_(L-1), L>=3, be pairwise distinct monic irreducible factors of Tbar in F_5[X], ALL present, with common degree h>=1.
Let Omega_i be their geometric root orbits.
Assume every Omega_i avoids0,1,-1 and that, with indices modulo L,

    C2:Omega_i -> Omega_(i+1),
    C3:Omega_i -> Omega_(i-1)                                  (OC2)

are bijections.
Other factors of Tbar, every reduction multiplicity, and other actual primes are allowed and retained in the full original field.

For every actual prime p of F above5 let v_p have value group Z, E_p=v_p(5), f_p=[k_p:F_5], and phi_p be the minimal polynomial of delta_bar over F_5.
For p in cluster i, meaning phi_p=Phi_i, put

    m_p=f_p/h, n_p=E_p m_p,
    eta_p=the unique C_(5^h)-fixed lift of delta_bar in O_(F_p),
    j_p=v_p(delta-eta_p), t_p=j_p/E_p,
    A_p=v_p(a)/E_p, B_p=v_p(b)/E_p, C_p=v_p(c)/E_p.             (OC3)

Here m_p,n_p,j_p are positive integers and t_p is positive and finite.
The letters A_p,B_p,C_p are normalized valuation scalars, not polynomials.
The complete original degree accounting is

    r=sum_(p|5) E_p f_p,
    r_cycle=h sum_(p in the L clusters) n_p<=r,
    d=2r>=2r_cycle.                                           (OC4)

No assumption that Z_5[delta] is the maximal order, that a factor corresponds to one prime, or that a prime is unramified is made.

Define the finite baseline and actual weighted evaluations

    E_cycle=sum_(i=0)^(L-1) sum_(p in i)sum_(q in i+1)
                              n_p n_q min(t_p,t_q),
    S_2=sum_(p in the cycle) n_p A_p,
    S_3=sum_(p in the cycle) n_p B_p,
    X_2=S_2-E_cycle, X_3=S_3-E_cycle.                          (OC5)

Then EVERY prime in these clusters has A_p,B_p,C_p>0, and in its original INTEGER-normalized valuation there is u_p in Z_(>0) with

    (v_p(a),v_p(b),v_p(c))=(2u_p,3u_p,5u_p).                   (OC6)

The complete product baselines in the two directions are identical, and

    S_2>=E_cycle, S_3>=E_cycle,
    2S_3=3S_2,
    X_2,X_3 in Z_(>=0), E_cycle in Z_(>0),
    2X_3-3X_2=E_cycle,
    X_3>=E_cycle/2>0.                                       (OC7)

The original restricted norm valuations are exactly

    h S_2=sum_(p in the cycle)f_p v_p(a),
    h S_3=sum_(p in the cycle)f_p v_p(b).                      (OC8)

These are the contributions of precisely the named actual primes to the full F-norm valuations; other primes remain in the full norm and degree sums.
In fact, with M_i=sum_(p in i)m_p,

    E_cycle=sum_(i,p in i,q in i+1)
                    m_p m_q min(E_q j_p,E_p j_q)
             >=sum_i M_i M_(i+1)>=L.                         (OC9)

The parity refinement is

    X_2=E_cycle modulo2,
    X_3>=E_cycle/2 if E_cycle is even,
    X_3>=(E_cycle+3)/2 if E_cycle is odd.                     (OC10)

No upper bound for X_2 or X_3 is asserted.

There MUST be an actual characteristic-zero source root delta_* of T from one of these primes and an actual target root beta_* of T in its C3 target cluster such that, in a common finite complete splitting field with v_5(5)=1, their matching periodic lifts satisfy

    eta'=C3(eta),
    v_5(delta_*-eta)=v_5(beta_*-eta')=t>0,
    v_5(C3(delta_*)-beta_*)>t,                                (OC11)

and the last valuation is finite.
Thus equal-distance leading displacements actually cancel under tripling.
If every actual C3 matching comparison attains the minimum of its two distances, the complete configuration is impossible.
In particular it is impossible if every adjacent pair of cluster distance sets
Delta_i={t_p:p in i} and Delta_(i+1) is disjoint.
Equal distances alone are not a realization or a proof of cancellation, and the theorem does not exclude all opposite cycles.

For primitive order31 traces in characteristic5, there are precisely five irreducible degree3 trace factors.
They satisfy(OC2) with L=5,h=3 and avoid0,1,-1.
If ALL FIVE occur in the same actual Tbar, every conclusion(OC4)--(OC11) applies, with r_cycle=3 sum_p n_p and E_cycle>=5.
This is a necessary full-weight tripling-cancellation budget only: it does not exclude their simultaneous presence, construct an original P, provide an excess upper bound, or settle the unrestricted Task.

<a id="opposite-cycle-distance-and-degree-extension"></a>
### Additional distance and degree conclusions in the same complete original domain

Retain ALL preceding hypotheses, definitions, actual roots, original primes and complete residual equations OC1--OC3.
For every cluster define the positive integer N_i=sum_(p in i)n_p.
Call cluster i constant-distance when all its actual primes have the same normalized distance t_p=t_i>0; this permits multiple primes and arbitrary ramification and residue multiplicities.
Every source prime p in such a cluster satisfies the exact original quotient formulas

    C_p=N_i t_i-1,
    A_p=(2/5)(N_i t_i-1), B_p=(3/5)(N_i t_i-1),
    N_i t_i=sum_(p in i)m_p j_p in Z_(>=2).                 (UD1--UD2)

If i and i+1 are both constant-distance, the fully weighted forward C2 and reverse C3 baselines imply

    (t_i-1/N_i)(t_(i+1)-1/N_(i+1))
        >=(25/6)min(t_i,t_(i+1))^2,
    max(t_i,t_(i+1))/min(t_i,t_(i+1))>25/6.                 (UD3--UD4)

Consequently NOT every cluster can be constant-distance.
At least one named cluster contains distinct ACTUAL primes p,q with j_p/E_p!=j_q/E_q, and the necessary OC11 cancellation has at least one nonconstant-distance endpoint cluster.
This remains a restriction on actual original primes, not an arbitrary root-value table.
It yields the weaker consequence

    sum_i N_i>=L+1, d>=2h(L+1).                             (UD5)

There are no adjacent N_i=N_(i+1)=1, so the indices with N_i=1 form an independent set in the cyclic index set and

    sum_i N_i>=ceil(3L/2), d>=2h ceil(3L/2).                (UD6--UD7)

The cycle also automatically avoids the residues2,-2.
For each periodic lift eta and each positive INTEGER source displacement j=v_5(w), its exact C5 image displacement is j+1.
A nonconstant-distance cluster with N_i=2 has exactly two original primes with n_p=E_p=m_p=1 and positive integer distances j<j'.
At its lower-distance source, the complete quotient satisfies C_p>=2j and B_p>=6j/5>j.
These statements give the stronger local restrictions: a constant-distance N=2 cluster cannot be followed by an N=1 cluster, and a nonconstant-distance N=2 cluster cannot be preceded by an N=1 cluster.
In particular, for every cyclic index i,

    (N_(i-1),N_i,N_(i+1))!=(1,2,1).                       (UD8--UD10)

The complete cyclic count then gives the strongest degree bound asserted here:

    sum_i N_i>=ceil(5L/3),
    r_cycle>=h ceil(5L/3),
    d=2r>=2h ceil(5L/3).                                  (UD11)

For the five primitive-order31 factors, L=5,h=3, hence r_cycle>=27 and d>=54, provided ALL FIVE occur in the same original Tbar under all the stated residual hypotheses.
The earlier d>=48 and d>=36 consequences are weaker, separately justified bounds.
There must additionally be distinct actual primes with different normalized distances in at least one of these cubic residue clusters.
The numerical count N_i>=2 by itself does NOT imply multiple primes: it can be supplied by a single ramified prime or a single prime with m_p>=2.
The distinct-prime assertion comes from the independent nonconstant-distance conclusion, not from mistaking total root multiplicity for a prime count.
All other primes remain in r=sum_(p|5)E_p f_p and all original norm contributions.
No attainability at degree54, general opposite-cycle exclusion, cancellation-depth upper bound, characteristic-zero realization or unrestricted Task completion is asserted.

The following reuse/source account and Sections1--6 are retained from the adopted v1 at their original reading and application scope.
For Sections7--12, the present contributors additionally used its complete OC1--OC13 argument and C624v5's exact C5 expansion and original-prime/lift interface.
The elementary cyclic counting and integral-distance Taylor comparisons are proved here directly; no new source-proof depth is claimed.

## Reuse and source boundary

A focused search among nearby fixed G0600-series Claims for opposite/inverse cycles, reverse baselines and tripling excess found no existing fixed account of this conclusion.
The actual [C624v5 local-factor/periodic-lift proof](Yin_C_G0624_v5.md#complete-argument) and its integral-support residual comparison were read before this argument.
Its IC3 already supplies the local mechanism forcing B=3A/2 when both target orbits are present; that mechanism is rechecked below without its old common-successor hypothesis.
[C191v2 Sections1--2](Yin_C_G0191_v2.md#argument) were read for the maximal-order lattice count and embedding-invariant lift distances, and [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) was read for the precise original trace field, phases and nonzero integrality.

The accepted [Con26e-U001 simple-root theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) applies in the actual finite completions and a common finite complete splitting field.
[The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) supplies the original E_p f_p degree sum and integer prime-value normalization at its retained statement/application scope.
These exact source interfaces were read; no source's general proof, ancestor theorems or original foundational inputs are newly audited.
The new work is the reverse-edge complete baseline, necessary weighted excess and integer/parity consequence.
The order31 identities below are direct exact algebra, not an enumeration, computation group or characteristic-zero realization.

## Complete argument

### 1. All original local factors and every root count

The original reciprocity and nontorsion imply [K:F]=2: alpha is a root of X^2-delta X+1, and alpha->alpha^-1 is a nontrivial automorphism fixing delta.
The usual integral C_n recurrence constructs T and the degree relation makes it the minimal polynomial of delta.
Modulo a rational prime ell, C_ell(X)=X^ell and T(X^ell)=T(X)^ell, so monic division by T leaves an integer remainder divisible by ell.
Evaluating gives the integral trace quotients a,b,c.
Their nonvanishing is the actual C153 input, also explicit in our hypotheses; no powered-degree assumption is substituted.

For all primes p|5, the original completion decomposition is

    F tensor_Q Q_5=product_(p|5)F_p,
    T=product_(p|5)T_p, deg T_p=E_p f_p,
    T_p modulo5=phi_p^(E_p f_p/deg phi_p).                     (OC12)

For the last identity, multiplication by delta on the free Z_5 lattice O_(F_p) has characteristic polynomial T_p.
The filtration modulo5 has E_p successive maximal-ideal quotients, each one-dimensional over k_p.
On each quotient the F_5 characteristic polynomial of multiplication by delta_bar is phi_p^(f_p/deg phi_p).
Multiplying over the filtration proves the exact exponent in(OC12), without identifying the maximal lattice with the power order.
Consequently every geometric root of Phi_i has EXACTLY n_p roots of T_p reducing to it for EACH prime p in cluster i.
The complete cluster contribution is h sum_p n_p, and all remaining primes give their unchanged terms in r=sum E_p f_p.

For H_h(X)=C_(5^h)(X)-X one has H_h modulo5=X^(5^h)-X and derivative-1.
The accepted simple-root theorem gives eta_p in O_(F_p) with the actual residue delta_bar and H_h(eta_p)=0.
If delta=eta_p, then alpha^(5^h) equals alpha or alpha^-1 by the quadratic trace identity, so alpha is a root of unity, a contradiction.
Thus j_p is a finite positive integer.
All Q_5 embeddings of F_p preserve its extended absolute value.
In a common finite complete field Omega containing all local roots and lifts, simple-root uniqueness gives one eta_xi at each geometric residue xi.
Every root from p reducing to xi has distance t_p from eta_xi, and this multiset has n_p repetitions at EVERY Frobenius conjugate residue of Phi_i.
This establishes all definitions and exact counts in(OC3)--(OC4).

### 2. Unit-derivative displacement and the two complete baselines

Work with v_5(5)=1 in Omega, so on F_p it equals v_p/E_p.
Fix a prime p in cluster i and an embedding giving an actual root delta_* with residue xi and periodic lift eta.
The polynomials C2 and C3 commute with C_(5^h), so C2(eta) and C3(eta) are periodic lifts of their actual target residues.
Uniqueness identifies them with the target lifts, whether or not the two maps compose to the identity at the chosen point.
The expansions are

    C2(eta+w)-C2(eta)=2eta w+w^2,
    C3(eta+w)-C3(eta)=3(eta^2-1)w+3eta w^2+w^3.

The excluded source residues make both leading coefficients5-adic units.
Since v_5(w)=t_p>0, the higher terms have strictly larger valuation, so both image displacements have value EXACTLY t_p.
For any actual target root from q with matching geometric residue, its displacement has value t_q.
The corresponding root-difference value is at least min(t_p,t_q), with equality whenever t_p!=t_q.
All roots with nonmatching residue contribute zero valuation, because their differences are units.
The actual nonzero a,b imply no factor in these evaluations vanishes, so all values are finite even at ties.

Factoring the SAME monic T into ALL its actual roots and paying the unit denominators2 and3 gives

    A_p>=sum_(q in i+1)n_q min(t_p,t_q),
    B_p>=sum_(q in i-1)n_q min(t_p,t_q).                       (OC13)

The evaluations are invariant under the choice of source embedding from p, while the complete target distance counts do not depend on which geometric residue in its orbit is reached.
Thus multiplying by n_p and summing over every original prime in the cycle gives

    S_2>=sum_(i,p in i,q in i+1)n_p n_q min(t_p,t_q)=E_cycle,
    S_3>=sum_(i,p in i,q in i-1)n_p n_q min(t_p,t_q)=E_cycle.

The second equality reindexes each reverse edge and swaps p,q; its summand is symmetric.
This equality is at the Frobenius-orbit and COMPLETE local-count level.
It does not identify C3 with an analytic inverse of C2 or pair their individual root differences as equal.
Every cluster is present and every t_p,n_p is positive, so E_cycle>0 and both A_p,B_p are positive at every source prime.

### 3. Full residual ratio at each original prime

Write A,B,C for the normalized valuations at one such prime.
The first residual equation2c^2=3a^5 gives2C=5A, since2 and3 are5-adic units.
The definition c=T(C5(delta))/5 has already paid its divisor5; C is the value of the actual quotient and is not the value of its numerator.

If2B<3A, then5B<15A/2=3C.
Both defect terms have unequal valuations, so

    v_5(e)=2B, v_5(g)=5B.

The equality e=-s g contradicts B>0.
If2B>3A, then5B>3C and

    v_5(e)=3A, v_5(g)=3C=15A/2,

again contradicting A>0.
Therefore2B=3A at EVERY actual prime in the cycle.
In integer-normalized values,2v_p(b)=3v_p(a) forces v_p(a)=2u_p and v_p(b)=3u_p with u_p a positive integer.
The first residual then gives v_p(c)=5u_p.
This proves(OC6), retaining the actual positive integer valuations rather than only real proportionality.

### 4. Exact weighted excess, integer refinement and norm meaning

Summing the primewise relation gives2S_3=3S_2.
Substituting S_2=E_cycle+X_2 and S_3=E_cycle+X_3 proves

    2X_3-3X_2=E_cycle.

The baseline inequalities give X_2,X_3>=0 and therefore X_3>=E_cycle/2>0.
Every summand in E_cycle is in fact the positive integer

    n_p n_q min(t_p,t_q)
       =m_p m_q min(E_q j_p,E_p j_q).

This proves(OC9), since each minimum is at least1 and every M_i=sum_p m_p is a positive integer.
Also

    S_2=sum_p m_p v_p(a)=2sum_p m_p u_p,
    S_3=sum_p m_p v_p(b)=3sum_p m_p u_p.

Thus E_cycle,S_2,S_3 are integers, S_2 is even, and X_2,X_3 are nonnegative integers.
The equality2X_3-3X_2=E_cycle implies X_2=E_cycle modulo2.
If E_cycle is odd, X_2 is at least1, so X_3>=(E_cycle+3)/2; if even, X_3>=E_cycle/2.
These are exactly(OC7)--(OC10).

Finally h n_p A_p=f_p v_p(a) and h n_p B_p=f_p v_p(b), proving the two exact restricted norm-valuation identities(OC8).
The full F-norm includes every other prime over5 as well; their contributions are not being set to zero.
The actual degree is still d=2r with r=sum_(all p|5)E_p f_p, not a field generated by a powered root or a cluster-normalized replacement.

### 5. A real equal-distance tripling cancellation is necessary

For each p choose any one actual source embedding as in Section2 and subtract its complete C3 minimum-sum baseline from B_p.
Each matching target root contributes a nonnegative finite excess; nonmatching factors are units.
The sum of these primewise excesses weighted by n_p is exactly X_3.
Since X_3>0, at least one ACTUAL matching root difference has strict excess.
Unequal distances would force equality by the non-Archimedean triangle law, so that pair must have t_p=t_q=t>0 and satisfy(OC11).
Its difference is nonzero because T(C3(delta_*))=3b_* is nonzero.

More explicitly, choose a uniformizer pi of Omega and put k=e_Omega t, an integer.
The two units pi^-k(C3(delta_*)-C3(eta)) and pi^-k(beta_*-C3(eta)) have the SAME residue precisely when the difference valuation is greater than t.
This identifies the required cancellation of leading displacements without assuming an upper bound on its depth.
The absence of such actual C3 cancellation would force X_3=0 and contradict(OC7), regardless of any cancellation at C2.
Disjoint adjacent distance sets ensure all C3 comparisons are unequal, so are an excluded special case.
The argument makes no claim that some allowed tied pattern is realized, nor that every tied comparison cancels.

### 6. The exact order31 orbit example

In characteristic5, X^31-1 is separable and its30 nontrivial roots all have order31, since31 is prime.
They lie in F_(5^3), because5^3=125=1 modulo31.
For z of order31, the trace xi=z+z^-1 has Frobenius degree equal to the least k>0 with5^k=+1 or-1 modulo31, by the quadratic trace identity.
Neither5 nor25 is plus or minus1, whereas5^3=1, so its degree is3.
Inversion pairs the30 primitive roots into15 distinct traces, hence five distinct irreducible degree3 trace factors.

The subgroup generated by5 and-1 modulo31 is exactly

    H={1,5,25,30,26,6}.

Trace Frobenius orbits correspond to its five cosets in(Z/31Z)^*.
The residues2,4,8,16 are outside H and2^5=1 modulo31, so multiplication by2 cycles all five cosets.
Also6=-25 belongs to H, hence3H=2^-1 H.
Tripling consequently runs through those same five cosets in the opposite direction.
This is not a pointwise inverse: C3(C2(xi))=C6(xi)=xi^(25), which differs from xi because its Frobenius degree is3.
If xi=0, then z has order dividing4; if xi=1, order dividing6; if xi=-1, order dividing3.
None is possible for order31, so all derivative-unit hypotheses hold.

If all five factors occur in the same actual Tbar, apply the complete theorem with L=5,h=3.
Its exact r_cycle=3sum n_p and all original degree/norm weights remain present; E_cycle>=5 and a genuine C3 equal-distance cancellation is required.
The order31 residue computation supplies neither an original characteristic-zero polynomial nor an excess upper bound, and therefore supplies no complete exclusion of these five factors.
All other configurations and the unrestricted G0001 objective retain their previous unresolved status.

<a id="opposite-cycle-constant-distance-c5-value"></a>
### 7. Exact C5 value at every prime of a constant-distance cluster

Work in C646's common finite complete splitting field with v_5(5)=1, so v_5=v_p/E_p on an embedded original completion F_p.
Fix a source root delta_*=eta+w from a prime in a constant-distance cluster i, with v_5(w)=t_i.
The lift eta is integral, and the exact expansion is

    C5(eta+w)-C5(eta)
      =5(eta^4-3eta^2+1)w
       +5(2eta^3-3eta)w^2
       +5(2eta^2-1)w^3+5eta w^4+w^5.

For the first four terms the valuations are at least1+k t_i, k=1,2,3,4; the last has valuation5t_i.
Every one is strictly greater than t_i, and cancellation can only increase the valuation.
Thus the image displacement has value greater than t_i, with the convention v_5(0)=infinity if needed.

C5 commutes with C_(5^h), and its residue action is xi->xi^5 in the SAME Frobenius orbit Omega_i.
By the fixed unique-lift theorem, C5(eta) is the periodic lift at that exact target residue.
For EACH actual prime q in cluster i, precisely n_q characteristic-zero roots of T_q reduce to this one geometric target residue, and each is at distance t_i from that lift.
The total matching count is N_i, not hN_i; all other roots of the complete original T have nonmatching residue and contribute unit factors.
The strict inequality between the image displacement and every matching target displacement forces every matching root difference to have valuation EXACTLY t_i.
Therefore the full monic product and the ACTUAL division by5 give, at every source prime in i,

    C_p=N_i t_i-1.                                      (UD1)

There is no omitted local factor and no assumption that the power order is maximal.
The complete original sums also show

    N_i t_i=sum_(p in i)n_p t_p=sum_(p in i)m_p j_p
               in Z_(>0).

By C646 every C_p is positive, so this integer is at least2.
C646's primewise residual ratios 2C_p=5A_p and2B_p=3A_p consequently yield

    A_p=(2/5)(N_i t_i-1),
    B_p=(3/5)(N_i t_i-1), N_i t_i>1.                    (UD2)

These are normalized values at the ORIGINAL primes; their integer-normalized counterparts still satisfy the original (2u_p,3u_p,5u_p) conclusion.
The minus one in UD1 is v_5(5)=1, equivalently the subtraction of E_p before dividing the integer prime valuation by E_p.

<a id="opposite-cycle-adjacent-distance-separation"></a>
### 8. The fully paid ratio for two adjacent constant-distance clusters

Suppose clusters i and i+1 are both constant-distance.
Write t=t_i, u=t_(i+1) and a_min=min(t,u)>0.
The full C2 baseline from i to i+1 and the full C3 baseline from i+1 to i give, respectively,

    (2/5)(N_i t-1)>=N_(i+1) a_min,
    (3/5)(N_(i+1)u-1)>=N_i a_min.

These are the two different directional evaluations furnished by OC13; they do not identify C3 with a pointwise inverse of C2.
Multiply them and divide by the positive N_i N_(i+1) to obtain the exact paid inequality

    (t-1/N_i)(u-1/N_(i+1))>=(25/6)min(t,u)^2.           (UD3)

Both factors on the left are positive by UD2 and strictly smaller than t and u.
Hence tu>(25/6)min(t,u)^2 and

    max(t_i,t_(i+1))/min(t_i,t_(i+1))>25/6.             (UD4)

In particular adjacent constant-distance clusters have different normalized distances.
All factors of N_i and the original division by5 are retained; no cancellation-depth upper bound is inferred.

<a id="opposite-cycle-necessary-distance-diversity"></a>
### 9. Required nonconstant distance cluster and its original-prime consequence

Suppose for contradiction every cluster in the cycle were constant-distance.
By UD4 every adjacent pair would have distinct distances.
For each source prime in cluster i, the C3 image displacement has value t_i by C646's actual unit-derivative calculation.
Every matching target root in cluster i-1 has value t_(i-1)!=t_i, so the non-Archimedean inequality is an equality at EVERY such comparison.
Every nonmatching factor is a unit and the denominator3 is a unit.
Thus B_p equals its complete OC13 baseline for every source prime, and the actual weighted sum has X_3=0.
This contradicts C646's X_3>=E_cycle/2>0.

Therefore some cluster contains at least two ACTUAL primes p,q with

    j_p/E_p != j_q/E_q.

A single prime cannot supply this diversity, because C646 proves its normalized distance is invariant across all its embeddings and geometric residue positions.
This excludes all one-prime-per-cluster configurations, and also excludes multiple-prime configurations when each cluster nevertheless has one common normalized distance.
It does not exclude configurations with a nonconstant cluster or supply a characteristic-zero realization of them.
The required C3 cancellation must occur on an adjacent comparison with at least one nonconstant cluster, since UD4 rules it out between two constant clusters.

For the weaker degree consequence of this distance diversity, every cluster contributes at least1 to N_i and the nonconstant one contributes at least2 through its distinct original primes.
Thus

    sum_i N_i>=L+1,
    r_cycle=h sum_i N_i>=h(L+1),
    d=2r>=2h(L+1).                                      (UD5)

Section10 strengthens this degree bound; UD5 is retained as the independent elementary consequence of actual distance diversity.
All primes outside the named clusters still contribute their nonnegative terms to the COMPLETE original degree r=sum_(all p|5)E_p f_p.

<a id="opposite-cycle-unit-multiplicity-degree-bound"></a>
### 10. No adjacent unit multiplicities and the stronger original-degree bound

If N_i=1, positivity and integrality of every n_p=E_p m_p imply that cluster i has exactly one actual prime, with E_p=m_p=1 and f_p=h.
Such a cluster is constant-distance.
Assume N_i=N_(i+1)=1 for an adjacent pair and let their positive distances be t,u.
If t<=u, the FORWARD C2 baseline and UD2 give

    (2/5)(t-1)>=t,

which would imply -2>=3t and contradict t>0.
If u<=t, the REVERSE C3 baseline and UD2 give

    (3/5)(u-1)>=u,

which would imply -3>=2u and contradict u>0.
Equality t=u is covered by either case.
Therefore

    not(N_i=N_(i+1)=1) for every i modulo L.             (UD6)

Let I={i:N_i=1}.
The map i->i+1 modulo L injects I into its complement by UD6, so2 card(I)<=L and card(I)<=floor(L/2).
For every index outside I, N_i is an integer at least2.
Consequently

    sum_i N_i>=card(I)+2(L-card(I))
              >=2L-floor(L/2)=ceil(3L/2),
    r_cycle>=h ceil(3L/2),
    d=2r>=2h ceil(3L/2).                                (UD7)

This argument counts the FULL multiplicities n_p=E_p m_p, not the number of primes.
In particular N_i>=2 may come from ONE ramified prime or from one prime with m_p>=2; it does not itself imply multiple primes or distance diversity.
The different-prime conclusion is supplied separately by Section9, not by this counting step.
All other factors and all original degree contributions remain in the exact sum; no powered trace field or reduced-degree replacement is used.

For C646's five primitive-order31 trace factors, L=5 and h=3.
If all five occur under the COMPLETE original C646 residual hypotheses, UD7 gives

    r_cycle>=24, r>=24, d>=48.

Section11 below strengthens this necessary degree bound further.
The d>=36 consequence of UD5 and this d>=48 consequence of UD7 remain weaker consequences, not parallel strongest bounds.
At least one of those actual cubic residue clusters must additionally contain different original primes with different j_p/E_p by Section9.
Neither d=48 attainability, a full opposite-cycle exclusion, an excess upper bound nor an original polynomial/field realization is asserted.
The unrestricted G0001 question remains open, and the source interfaces stay at C646/C624's previously retained application depth.
No native enumeration or external source acquisition is used.

<a id="opposite-cycle-no-unit-two-unit"></a>
### 11. Exclusion of the local multiplicity pattern(1,2,1)

No Omega_i can contain2 or-2.
Either is rational over F_5, so its irreducible orbit is a singleton; C2 sends both to2 and fixes2.
This would force two of the pairwise distinct successive cycle orbits to coincide, contrary to L>=3.
Consequently, for every periodic lift eta at a cycle residue xi,

    eta^4-3eta^2+1 modulo5=(xi^2+1)^2!=0.

Indeed xi^2=-1 in characteristic5 has precisely the roots2,-2, even in the algebraic closure.
The first Taylor coefficient in Section7 therefore has valuation EXACTLY1.
If a source displacement w has positive INTEGER distance j=v_5(w), its first Taylor term has valuation j+1, whereas every other term has strictly larger valuation:
1+k j>1+j for k=2,3,4 and5j>1+j for j>=1.
There can be no tie with that first term, so

    v_5(C5(eta+w)-C5(eta))=j+1.                        (UD8)

Suppose cluster i has N_i=2 and is constant-distance with value t, while its successor has N_(i+1)=1 and value k.
If t<=k, the forward C2 baseline would give

    (2/5)(2t-1)>=t,

which is impossible because (2/5)(2t-1)<t for every t>0.
If k<=t, the reverse C3 baseline at the successor would give

    (3/5)(k-1)>=2k,

again impossible for k>0.
Thus a constant-distance N=2 cluster cannot be followed by an N=1 cluster.

Suppose instead cluster i has N_i=2 and is nonconstant-distance.
It must have exactly two ACTUAL primes, each with n_p=E_p=m_p=1, because its positive integer prime weights sum to2 and one prime alone has a single embedding-invariant distance.
Their two distances are positive integers j<j'.
Fix a source root belonging to the prime with distance j.
By UD8 its C5 image displacement is exactly j+1 from the target periodic lift in this SAME cluster.
At the exact geometric target residue there is one root from each prime: their distances are j and j'>=j+1.
The first root comparison has valuation exactly j, and the second has valuation at least j+1.
All other original factors are units, so the complete product, including the quotient by5, gives

    C_p>=j+(j+1)-1=2j,
    B_p=(3/5)C_p>=6j/5>j.                              (UD9)

All valuations are finite because the actual element c is nonzero; equality or cancellation at the second root can only increase this lower bound.

If the predecessor cluster had N_(i-1)=1 with distance k, the C3 image of this low-distance source has displacement exactly j by the unit derivative, and there is exactly one matching target root of distance k.
For k!=j the complete C3 product therefore gives B_p=min(j,k)<=j, contradicting UD9.
For k=j, apply C2 at the predecessor prime instead.
Its image has distance j, and its two matching target roots in cluster i have distances j and j'>j.
The first comparison is at least j and the second is exactly j, so A_(predecessor)>=2j.
But UD2 at the constant-distance N=1 predecessor gives A_(predecessor)=(2/5)(j-1)<j, again a contradiction.
Thus a nonconstant-distance N=2 cluster cannot be preceded by an N=1 cluster.

Both cases together prove the cyclic local prohibition

    (N_(i-1),N_i,N_(i+1))!=(1,2,1) for every i.         (UD10)

The constant-distance case permits a single ramified prime, a single prime with m_p=2, or two primes at the same distance; none was silently discarded.
The nonconstant case forces two distinct unramified primes by the complete integer weight2, not by assuming all clusters split.
Neither case asserts that arbitrary N=2 clusters are impossible.

<a id="opposite-cycle-five-thirds-degree-bound"></a>
### 12. The stronger cyclic degree budget and order31 consequence

Let k be the number of N_i=1 clusters.
For k=0 the sum is at least2L, which is at least5L/3.
For k>=1, list those k clusters in cyclic order and let g_1,...,g_k be the numbers of intervening nonunit clusters.
UD6 gives every g_j>=1 and sum_j g_j=L-k.
If b of these gaps have length1, all other gaps have length at least2, hence

    L-k>=b+2(k-b)=2k-b,
    b>=max(0,3k-L).

In a gap of length1, its unique middle multiplicity is at least3 by UD10; the baseline weight for a nonunit cluster is2.
These b gaps have distinct middle clusters, so each incurs a separate additional unit in the original full degree count.
Therefore

    sum_i N_i>=2L-k+b
              >=2L-k+max(0,3k-L)
              >=5L/3.

For the last inequality, if k<=L/3 use2L-k>=5L/3; if k>=L/3 use L+2k>=5L/3.
The sum is an integer, and the complete original degree relation consequently gives

    sum_i N_i>=ceil(5L/3),
    r_cycle>=h ceil(5L/3),
    d=2r>=2h ceil(5L/3).                               (UD11)

For L=5,h=3, this is r_cycle>=27 and d>=54.
This is the strongest degree bound asserted here; the bounds d>=48 and d>=36 remain weaker consequences of the separately retained arguments.
The independent distance-diversity conclusion still forces different ACTUAL primes with different normalized distances in some cluster, whereas UD11 counts complete multiplicities and does not identify them with prime counts.
No attainability at degree54, full opposite-cycle exclusion, cancellation-depth upper bound, original realization or unrestricted G0001 solution follows.
All original field, complete residual, periodic-lift, root-count and source-depth hypotheses from C646 are retained throughout.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision distance-degree-extension-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:37 |
| status | open |
| reason | Register the complete retained OC1--OC13 theorem and new UD1--UD11 extension in the same actual original P/K/F/T and full signed residual domain. Exact constant-distance quotient values and complete forward/reverse counts force distance diversity among actual primes; no adjacent unit multiplicities and no local(1,2,1) pattern give sum N_i>=ceil(5L/3), hence original d>=2h ceil(5L/3) and conditional order31 d>=54. Every original root, prime, ramification, norm and degree weight is retained. Root, paid_comparison and original_law are contributors at the stated scopes; fresh isolated whole review of this expanded revision remains required. No full opposite-cycle exclusion, realization, excess upper bound or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original-field statement and extension](#statement) | All OC1--OC11 and UD1--UD11: complete original polynomial/field and nonzero integral full residual hypotheses, every present opposite-cycle factor and actual prime weight, exact weighted excess and cancellation, constant-distance separation and distinct-prime diversity, both local multiplicity exclusions, strongest full original degree bound and conditional order31 d>=54, with all nonrealization limits. |
| argument | [Complete proof](#complete-argument) | Entire Sections1--12/OC12--OC13/UD1--UD11: all original local root counts and lifts, both residual valuation cases, exact excess/integer/parity/cancellation proof, order31 algebra, complete C5 Taylor product, directional min cases, two actual unramified primes at total weight2 and the full cyclic gap count. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual irreducible reciprocal nontorsion P, original degrees d=2r, exact P=z^r T(z+z^-1), nonzero integral trace quotients and their distinction from original phase-bearing K-elements; total reality remains an explicit hypothesis. |
| dependency | [Adopted five-adic original root/lift interface](Yin_C_G0624_v5.md#complete-argument) | Complete actual Q5 factors, each geometric residue root count, unique periodic lift, embedding-invariant distances and exact C5 expansion; no old same-successor cycle conclusion is imported as an opposite-cycle exclusion. |
| dependency | [Previously established full residual local comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | IC3 strict-valuation mechanism with both target factors present, retained and rechecked without identifying those targets; old proper-support numerical bounds are not applied. |
| dependency | [Maximal-order local count mechanism](Yin_C_G0191_v2.md#argument) | Completion decomposition and full maximal-order residue filtration/root multiplicity, not an assumption that Z_5[delta] is maximal; dyadic numerical conclusions are not imported. |
| dependency | [Accepted complete-field simple-root theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Theorem9.1 at retained accepted statement/application depth, applied to C_(5^h)-X in actual completions and a common finite complete field; no new foundational proof audit. |
| dependency | [Original local degree and valuation conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | All original E_p f_p degree contributions and integer valuation groups, with unchanged source/ancestor-proof limits. |
| support | [Adopted exact physical predecessor](Yin_C_G0646_v1.md#decision-whole-reviewed-2026-10-23) | The previously adopted complete OC1--OC13 and Sections1--6 are retained here without substantive change; that predecessor's independent review does not review or adopt the new UD1--UD11 extension. |
| support | [Reuse and source boundary](#reuse-and-source-boundary) | Retained predecessor source-reading/application facts and current extension's direct C646/C624 use; no new native computation, source-proof upgrade, realization or depth upper bound. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:43 |
| status | proved |
| reason | Adopt the entire expanded OC1--OC13 and UD1--UD11 theorem after main reading of complete C646v2 and isolated whole R859. All original field/root/prime counts, norm and degree weights remain. Exact constant-distance values and directional baselines force actual-prime distance diversity; the unit-unit and unit-two-unit exclusions give the necessary full degree d>=2h ceil(5L/3), conditionally d>=54 for the five order31 factors. Earlier weaker bounds and complete source-depth limits remain. No attainability, full opposite-cycle exclusion, cancellation-depth upper bound, original realization or unrestricted Task completion is asserted. Later author candidates are outside this acceptance. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original-field statement and extension](#statement) | All OC1--OC11 and UD1--UD11: complete original polynomial/field and nonzero integral full residual hypotheses, every present opposite-cycle factor and actual prime weight, exact weighted excess and cancellation, constant-distance separation and distinct-prime diversity, both local multiplicity exclusions, strongest full original degree bound and conditional order31 d>=54, with all nonrealization limits. |
| argument | [Complete proof](#complete-argument) | Entire Sections1--12/OC12--OC13/UD1--UD11: all original local root counts and lifts, both residual valuation cases, exact excess/integer/parity/cancellation proof, order31 algebra, complete C5 Taylor product, directional min cases, two actual unramified primes at total weight2 and the full cyclic gap count. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual irreducible reciprocal nontorsion P, original degrees d=2r, exact P=z^r T(z+z^-1), nonzero integral trace quotients and their distinction from original phase-bearing K-elements; total reality remains an explicit hypothesis. |
| dependency | [Adopted five-adic original root/lift interface](Yin_C_G0624_v5.md#complete-argument) | Complete actual Q5 factors, each geometric residue root count, unique periodic lift, embedding-invariant distances and exact C5 expansion; no old same-successor cycle conclusion is imported as an opposite-cycle exclusion. |
| dependency | [Previously established full residual local comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | IC3 strict-valuation mechanism with both target factors present, retained and rechecked without identifying those targets; old proper-support numerical bounds are not applied. |
| dependency | [Maximal-order local count mechanism](Yin_C_G0191_v2.md#argument) | Completion decomposition and full maximal-order residue filtration/root multiplicity, not an assumption that Z_5[delta] is maximal; dyadic numerical conclusions are not imported. |
| dependency | [Accepted complete-field simple-root theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Theorem9.1 at retained accepted statement/application depth, applied to C_(5^h)-X in actual completions and a common finite complete field; no new foundational proof audit. |
| dependency | [Original local degree and valuation conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | All original E_p f_p degree contributions and integer valuation groups, with unchanged source/ancestor-proof limits. |
| support | [Adopted exact physical predecessor](Yin_C_G0646_v1.md#decision-whole-reviewed-2026-10-23) | The previously adopted complete OC1--OC13 and Sections1--6 are retained here without substantive change; that predecessor's independent review does not review or adopt the new UD1--UD11 extension. |
| support | [Reuse and source boundary](#reuse-and-source-boundary) | Retained predecessor source-reading/application facts and current extension's direct C646/C624 use; no new native computation, source-proof upgrade, realization or depth upper bound. |
| review | [Independent entire expanded opposite-cycle finding](../audits/reviews/Yin_R_G0859_v1.md#opposite-cycle-v2-whole) | Whole physicalv2 statement and Sections1--12, retained OC and all new UD arguments, complete actual weights and finite valuations, both local exclusions and cyclic count including all endpoints, with exact source and predecessor limits. |

