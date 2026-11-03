---
author: Yin
---

# Opposite trace-cluster cycles: exclusion of all weight-one and weight-two clusters

Human author Yin.
Root and paid_comparison supplied the original OC1--OC13 theorem; root and original_law supplied and checked the UD1--UD21 extensions retained from physical v2 and v3.
Root supplied UD22--UD24 in physical v4; root and original_law supplied and checked UD25--UD29 in physical v5 at their previously stated contributor scopes.
For the present UD30--UD34 extension, root supplied the arbitrary-ramification numerator divisibility and minimum-distance contradiction; original_law checked the exact original valuation normalization, every root-count inequality and the equality endpoint as a contributor.
No contributor supplies independent review of this revision.
The entire v5 mathematics is retained unchanged, including its historical k-dependent conditional conclusions.
This revision proves k=0 and strengthens the local exclusion to every N_i>=3, while leaving the unconditional degree bound d>=6hL and order31 bound90 unchanged.
Fixed predecessor assessments and reviews remain at their exact physical locators and do not review this new extension.
No native computation, external source acquisition, foundational source-proof upgrade, exclusion of weight-three clusters, original realization or unrestricted Task completion is claimed.

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

The complete cyclic count through UD11 gives the following degree bound, strengthened by UD16 and UD21 below:

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

<a id="opposite-cycle-no-unit-extension"></a>
### Every original cluster has total weight at least two

Under ALL the preceding original hypotheses, every named cluster satisfies

    N_i=sum_(p in i)E_p m_p>=2.                            (UD21)

In particular no directed edge of cluster weights(1,2) exists, and the complete original degree satisfies

    sum_i N_i>=2L,
    r_cycle>=2hL,
    d=2r>=4hL.                                            (UD15--UD16)

For all five primitive-order31 factors in the SAME actual Tbar, L=5,h=3, hence r_cycle>=30 and d>=60.
This is the degree bound proved through UD21; the new UD22--UD24 below strengthen it, while d>=54,48,36 remain weaker deductions.

The proof retains two exact original-field obstructions.
First, a hypothetical directed(1,2) edge would force its constant distances to be16 and3 and the second cluster to have A=2,B=3,C=5.
Every distance in its arbitrary successor would then be below3 with complete integer sum sum m_q j_q=2.
At a maximal-distance successor prime, the actual values C=1 and B=2t_* force t_*=3/10, hence j_*>=3, contradicting that sum2.

The stronger obstruction rules out any N_i=1 directly.
Its unique original prime has E=m=1, t=5u+1 and(A,B,C)=(2u,3u,5u) for a positive integer u.
Both neighboring clusters have all distances below t and exact positive integer sums J_+=2u and J_-=3u.
Maximal-distance original primes in these clusters have respectively

    t_+=3(2u-1)/5, C_+=2u-1,
    t_-=2(3u-1)/5, C_-=3u-1.                            (UD17--UD20)

Their positive integer budgets m_+j_+<=2u and m_-j_-<=3u force simultaneously u=3 modulo5 and u=2 modulo5, an impossibility.
The complete root products, original quotient by5, arbitrary ramification and all prime weights are proved in Sections13--17.

This is a lower bound on complete multiplicity, not on the number of primes in each cluster.
A single original prime may have E_p m_p>=2.
The independently retained distance-diversity conclusion still requires distinct actual primes of different normalized distances in at least one cluster.
No attainability at degree60, full opposite-cycle exclusion, upper bound on cancellation depth, characteristic-zero realization or unrestricted G0001 completion is asserted.


<a id="opposite-cycle-weight-two-successor-extension"></a>
### Weight-two clusters require weight-at-least-four successors

Retain ALL the original hypotheses and every conclusion above.
Every named cluster satisfies the further necessary restriction

    N_i=2 implies N_(i+1)>=4.                              (UD22)

In particular every directed(2,2) or(2,3) edge is impossible.
This holds for a constant-distance weight-two source, including one ramified prime or one prime with m_p=2, as well as a source with two actual unramified primes at different integer distances.
No one-prime or unramified assumption is added to its arbitrary successor.

More precisely, if N_i=2, every distance in the successor is strictly smaller than every distance in the source.
Its complete positive integer distance sum S=sum_(q in i+1)n_q t_q=sum_(q in i+1)m_q j_q and its maximal actual distance v obey

    S>1, v=3(S-1)/10,
    10S<=3N_(i+1)(S-1).                                  (UD23)

All original prime weights and the division by5 remain in these formulas.
The complete original degree therefore satisfies

    sum_i N_i>=3L,
    r_cycle>=3hL,
    d=2r>=6hL.                                            (UD24)

For all five primitive-order31 cubic factors in the SAME actual Tbar, this gives r_cycle>=45 and d>=90.
This is the unconditional numerical bound through UD24; UD29 below adds the exact dependence on the number of weight-two clusters.
All lower bounds and the independent actual-prime distance-diversity conclusion above remain valid.
The new proof uses only the full original residual ratios and previously proved actual-root interfaces; no native calculation or new external source is required.
No equality attainment at degree90, complete opposite-cycle exclusion, bound on cancellation depth, original realization or unrestricted Task completion is asserted.

<a id="opposite-cycle-weight-four-exclusion-extension"></a>
### A weight-two source requires a successor of weight at least five

Retain the ENTIRE preceding original domain, all original prime/root/degree weights and BOTH residual equations.
The necessary successor restriction strengthens to

    N_i=2 implies N_(i+1)>=5.                              (UD28)

The proof retains the following complete necessary arithmetic and endpoint facts.
For any N_i=2, write J=i+1, S=sum_(q in J)m_q j_q and v=max_(q in J)t_q, as in UD23.
The sum S is even, and its original integer numerator budget forces

    S=10a+6, v=(6a+3)/2, a in Z_(>=0).

Every actual prime q in J satisfies B_q=2t_q and C_q=10t_q/3.
If N_J=4, the original positive integer pairs(E_*,m_*) at a maximal-distance prime can only be(4,1),(2,2),(2,1).
The complete budget and minimum-distance comparison exclude every a>=1.
At a=0, equality S=N_J v=6 forces all actual distances in J to equal3/2, with A=2,B=3,C=5.
Its arbitrary next successor would then have exact positive integer sum2 but a maximal-distance original numerator at least3, a contradiction.
These statements are UD25--UD27, proved with all ramification and multiplicity cases in Sections20--22.

If k=card{i:N_i=2}, their distinct successors of weight at least5 give the complete original degree refinement

    sum_i N_i>=3L+k,
    r_cycle>=h(3L+k),
    d=2r>=2h(3L+k).                                       (UD29)

For all five primitive-order31 cubic factors in the SAME actual Tbar, d>=90+6k.
In particular k>0 implies d>=96, while k=0 retains d>=90; no unconditional96 conclusion is asserted.
All other original primes remain in the exact original degree and norm sums.
The independent actual-prime distance-diversity theorem remains separate from these total root-weight counts.
No claim of equality attainment, general weight-three exclusion, complete opposite-cycle exclusion, cancellation-depth upper bound, original realization or unrestricted G0001 completion follows.

<a id="opposite-cycle-no-weight-two-extension"></a>
### Every named original cluster has complete weight at least three

Under the ENTIRE preceding original field, polynomial, signed residual and opposite-cycle hypotheses,

    N_i>=3 for EVERY named cluster,
    k=card{i:N_i=2}=0.                                     (UD33)

The decisive integer statement uses each prime's ORIGINAL value group even when that prime is ramified.
If a hypothetical weight-two cluster had successor J, every original successor prime q would satisfy

    v_q(c)=E_q C_q=10j_q/3 in Z,
    3 divides j_q, j_q>=3.                                 (UD30--UD31)

Writing N=N_J>=5 and w for the minimum actual successor distance, the complete same-cluster C5 product and its actual division by5 give

    w>=3/N, (N-10/3)w<=1.                                  (UD32)

Thus N<=5, and equality with the retained lower bound forces N=5 and w=3/5.
At the original minimum prime this requires E=5,j=3,m=1, consuming the entire weight5.
Its complete distance sum is then S=3, contradicting the already proved evenness of S.
The full proof in Sections24--25 retains every actual prime and root multiplicity until that equality forces uniqueness.

Summing the local conclusion gives

    sum_i N_i>=3L, r_cycle>=3hL, d=2r>=6hL.                (UD34)

For all five primitive-order31 cubic factors in the SAME actual Tbar and under BOTH complete original residual equations, this remains d>=90.
The new local theorem does not improve the previous unconditional numerical bound.
The earlier fixed conditional d>=90+6k and its k>0 implication d>=96 are preserved above; UD33 proves that k>0 cannot occur under these full hypotheses, and yields no unconditional96 conclusion.
The independent actual-prime distance-diversity theorem remains valid, and total root weights are not replaced by prime counts.
No weight-three exclusion, attainability, complete opposite-cycle exclusion, original realization, cancellation-depth upper bound or unrestricted G0001 completion is asserted.

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
This is the degree bound obtained through UD11; the bounds d>=48 and d>=36 are weaker consequences, and UD16 below strengthens it further.
The independent distance-diversity conclusion still forces different ACTUAL primes with different normalized distances in some cluster, whereas UD11 counts complete multiplicities and does not identify them with prime counts.
No attainability at degree54, full opposite-cycle exclusion, cancellation-depth upper bound, original realization or unrestricted G0001 solution follows.
All original field, complete residual, periodic-lift, root-count and source-depth hypotheses from C646 are retained throughout.

<a id="opposite-cycle-unit-two-forced-values"></a>
### 13. Exact forced values if a directed(1,2) edge existed

Suppose for contradiction N_i=1 and N_(i+1)=2.
The original integer weights n_p=E_p m_p imply that cluster i consists of one actual prime with E_p=m_p=1.
It has one distance t>0 and is constant-distance.
By the complete nonconstant-weight-two argument in v2 Section11, cluster i+1 cannot be nonconstant-distance when preceded by N_i=1.
It therefore has one common distance u>0, allowing one ramified prime, one prime with m_p=2 or two primes of weight1 at equal distance.
None of these possibilities is removed from the original complete product.

If t<=u, the forward C2 baseline from the unit cluster and its exact constant-distance value imply

    (2/5)(t-1)>=2t,

which is impossible for t>0.
Thus t>u, so EVERY matching comparison on this edge has unequal displacements and attains its minimum exactly.
Forward C2 has two matching roots at distance u and reverse C3 has one matching root at distance t; the source C2/C3 image distances are t and u respectively.
Nonmatching roots contribute units, and division by2 or3 does not alter the normalized values.
The two exact equations are consequently

    (2/5)(t-1)=2u,
    (3/5)(2u-1)=u.

The second gives6u-3=5u, hence u=3, and the first gives t=16.
At EVERY original prime of the second cluster the exact values are

    u=3, A_p=2, B_p=3, C_p=5.                         (UD12)

These are a consequence of the hypothetical edge, not freely prescribed local data.
The reverse C3 count uses the target orbit and its complete geometric-root count; no pointwise inverse identity is used.

<a id="opposite-cycle-unit-two-successor-contradiction"></a>
### 14. Any actual successor gives an integer contradiction

Let J denote the next cluster i+2 modulo L.
It is present and distinct from the first two clusters because L>=3.
It may have any positive total weight, any number of actual primes, and arbitrary ramification and residue multiplicities.
Fix a source prime in cluster i+1.
Its C2 image displacement is exactly3, and its full evaluation has A_p=2 by UD12.
If even one actual target prime q in J had t_q>=3, its n_q>=1 matching roots alone would contribute at least3 to the C2 baseline, contradicting A_p=2.
Thus ALL primes q in J satisfy t_q<3.
Every matching root comparison is now unequal and exact, while all other original roots are unit factors.
Therefore the COMPLETE target-cluster sum satisfies

    J_J:=sum_(q in J)n_q t_q=sum_(q in J)m_q j_q=2.      (UD13)

Each summand m_q j_q is a positive INTEGER.
The equality is not inferred by reversing a lower bound: unequal distances make every factor value equal its minimum, so the entire original C2 product equals this sum.

Choose an actual prime q_* in this finite cluster with maximal distance t_*=j_*/E_*.
In a common complete splitting field, fix one source root from q_* and its periodic lift eta.
The full C5 expansion of v2 Section7 proves

    v_5(C5(delta_*)-C5(eta))>t_*.

This strict inequality holds for EVERY positive rational t_*; no integral-distance assumption or unit first Taylor coefficient is needed here.
C5 acts by Frobenius on the residue orbit of J, so its target lift is in this SAME cluster.
Every matching actual target root has distance t_q<=t_*, including all n_q copies at the actual geometric target residue.
Consequently its difference from C5(delta_*) has valuation exactly t_q, even when several primes attain the maximum.
Nonmatching factors are units, and the actual quotient by5 subtracts exactly1.
The complete product gives at the original prime q_*

    C_(q_*)=J_J-1=1.                                    (UD14)

Its reverse C3 target is cluster i+1, with total multiplicity2 and constant distance3.
Since t_*<3 and the C3 derivative is a unit, each of those two matching root comparisons has exact value t_*.
Hence B_(q_*)=2t_*.
The full residual relations give B_(q_*)=3C_(q_*)/5=3/5, and therefore

    t_*=3/10, 10j_*=3E_*.

Both j_* and E_* are positive integers in the ORIGINAL completion.
The last equality forces3 to divide j_*, so j_*>=3.
But m_*>=1 and UD13 give m_* j_*<=2, a contradiction.
All primes and all positive contributions to that integer sum are retained; no uniform ramification bound or one-prime assumption was used.
We have proved the stronger directed prohibition

    (N_i,N_(i+1))!=(1,2) for every i modulo L.          (UD15)

This directed-edge argument also excludes the earlier(1,2,2) and(1,2,1) candidates.
It alone does not exclude the opposite directed edge(2,1); the stronger argument in Section17 excludes all unit clusters.

<a id="opposite-cycle-double-degree-bound"></a>
### 15. Full original degree at least four times the cycle size times h

Let I={i:N_i=1} and k=card(I).
The adjacent-unit exclusion UD6 and the new directed exclusion UD15 show that EVERY i in I has N_(i+1)>=3.
The cyclic successor map is injective, and none of these successors lies in I.
Thus k distinct clusters have weight at least3, the k unit clusters have weight1, and every remaining cluster has positive integer weight at least2.
In particular2k<=L and

    sum_i N_i>=k+3k+2(L-2k)=2L.

The argument includes k=0, when every weight is at least2.
Keeping every other original prime in r=sum_(p|5)E_p f_p yields

    r_cycle=h sum_i N_i>=2hL,
    d=2r>=4hL.                                          (UD16)

For the five primitive-order31 clusters, L=5,h=3, the conditional original-degree bound is d>=60.
The hypotheses require ALL five factors in the same actual Tbar and BOTH complete original residual equations, as before.
The independent distance-diversity conclusion of v2 remains valid and separate; the total weight N_i is never identified with a count of distinct primes.
The weaker d>=54,48,36 deductions remain valid at their fixed scopes.
No claim of equality attainment, arbitrary opposite-cycle exclusion, upper bound on cancellation depth, original characteristic-zero realization or unrestricted G0001 completion follows.

<a id="opposite-cycle-unit-neighbor-exact-budgets"></a>
### 16. A hypothetical unit cluster forces two exact neighbor budgets

Suppose N_i=1.
Its only actual prime p has E_p=m_p=n_p=1, and its normalized distance t=j_p is a positive integer.
The full C5 formula of v2 Section7 gives C_p=t-1.
At this original prime the integer-normalized conclusion OC6 is (v_p(a),v_p(b),v_p(c))=(2u,3u,5u) for one positive INTEGER u.
Because E_p=1, the normalized values are the same, and therefore

    t=5u+1, A_p=2u, B_p=3u, C_p=5u, u in Z_(>0).       (UD17)

Both2u and3u are strictly smaller than t.
If the successor cluster i+1 had an actual prime q with t_q>=t, its n_q>=1 matching roots would already contribute at least t to the C2 baseline, contradicting A_p=2u.
The same argument with C3 and B_p=3u excludes t_q>=t in the predecessor cluster i-1.
Thus every distance in BOTH adjacent clusters is strictly less than t.
The actual C2/C3 image distances at p are exactly t by their unit derivatives, so every matching root comparison in both directions is unequal and exact.
All nonmatching roots are units, and the complete original products give

    J_+:=sum_(q in i+1)n_q t_q=sum_(q in i+1)m_q j_q=2u,
    J_-:=sum_(q in i-1)n_q t_q=sum_(q in i-1)m_q j_q=3u. (UD18)

Every summand is a positive INTEGER, retaining all primes, ramification and residue multiplicities.
These are exact same-T evaluations, not upper or lower inequalities reinterpreted as equalities.

<a id="opposite-cycle-unit-incompatible-congruences"></a>
### 17. Maximal original distances force incompatible residues modulo five

Choose a prime q_+ of maximal distance t_+=j_+/E_+ in the successor cluster.
The strict C5 displacement increase holds for every positive rational distance, by the complete Taylor expansion of v2 Section7.
Thus its image displacement is greater than t_+, hence greater than or equal to every target distance in the same cluster, strictly greater in every comparison.
There are precisely n_q matching roots per original prime q at the actual geometric Frobenius target residue.
Every such root difference has value exactly t_q, and every nonmatching factor is a unit.
Dividing the complete monic T evaluation by5 subtracts exactly1, giving

    C_(q_+)=J_+-1=2u-1.

The C3 target of this successor is the unit cluster i.
Its single matching root has distance t>t_+, so the reverse C3 evaluation is exactly B_(q_+)=t_+.
The full residual ratio B=3C/5 yields

    t_+=3(2u-1)/5, 5j_+=3(2u-1)E_+.                    (UD19)

If5 does not divide2u-1, the integer3(2u-1) is coprime to5.
The displayed equality then forces5 to divide E_+ and

    j_+>=3(2u-1)=6u-3>2u,

where the strict inequality uses u>=1.
But m_+>=1 and the complete positive sum J_+=2u imply m_+j_+<=2u, a contradiction.
Therefore5 divides2u-1 and u=3 modulo5.

Choose similarly a prime q_- of maximal distance t_-=j_-/E_- in the predecessor cluster.
Exactly the same COMPLETE C5 root product, now using J_-, gives C_(q_-)=3u-1.
The C2 target is the unit cluster i and its unique matching root has distance t>t_-, so A_(q_-)=t_- exactly.
The other full residual ratio A=2C/5 yields

    t_-=2(3u-1)/5, 5j_-=2(3u-1)E_-.                    (UD20)

If5 does not divide3u-1, the numerator2(3u-1) is coprime to5, so5 divides E_- and

    j_->=2(3u-1)=6u-2>3u,

again using u>=1.
This contradicts m_-j_-<=J_-=3u with m_->=1.
Thus5 divides3u-1 and u=2 modulo5.
The same original positive integer u cannot be both2 and3 modulo5.
The hypothetical unit cluster is therefore impossible, and

    N_i>=2 for EVERY cluster i.                         (UD21)

The argument uses separate actual neighbor primes, their original integer E,m,j and the two distinct C2/C3 directions.
It neither identifies C3 with a pointwise inverse nor replaces actual primes with an arbitrary distance table.
The maximum-distance product remains exact when several primes share that maximum and allows arbitrary ramification.
Summing UD21 immediately recovers UD16: sum_i N_i>=2L, r_cycle>=2hL and d>=4hL, hence d>=60 for the complete five-factor order31 case.
UD21 strengthens the earlier local exclusions but does not itself say any cluster has multiple primes; a single prime can have E_p m_p>=2.
The independent v2 distance-diversity theorem supplies the actual distinct-prime conclusion in at least one cluster.
No equality attainment, complete opposite-cycle exclusion, cancellation-depth upper bound, realization or unrestricted Task conclusion is asserted.

<a id="opposite-cycle-weight-two-exact-successor"></a>
### 18. Exact successor distances for every weight-two source

Suppose N_i=2 and let J denote the successor cluster i+1.
It is an arbitrary actual cluster, with all original primes and arbitrary ramification and residue multiplicities.
We first show that EVERY distance in J is strictly smaller than EVERY distance in i.

If the source cluster is constant-distance of value t, Section7 gives its exact original value

    A_p=(2/5)(2t-1)<t.

Its C2 image displacement is exactly t.
If any target prime q had t_q>=t, its positive integer multiplicity n_q alone would contribute at least t to the complete C2 baseline, a contradiction.
Thus all target distances are strictly below t, and every matching comparison attains its minimum.
The entire monic root product, including all unit nonmatching factors and the unit denominator2, gives

    S:=sum_(q in J)n_q t_q=sum_(q in J)m_q j_q=A_p>0.

This is a positive integer.
The constant-distance case includes a single ramified prime, one prime with m_p=2, or two weight-one primes at a common distance.

If the weight-two source is nonconstant, its two positive integer prime weights must both equal1.
Thus there are exactly two actual primes with E=m=1 and distinct positive INTEGER distances j<J_max.
At the higher-distance source the C5 image displacement is strictly greater than J_max, hence greater than both target distances in its same cluster.
The complete C5 quotient at that source is exactly

    C_high=j+J_max-1,
    A_high=(2/5)(j+J_max-1)<J_max.

There are exactly two matching target roots, one at each distance, and the division by5 subtracts1.
No term from another residue factor is omitted; all such differences are units.

If J_max>=j+2, the exact integer-distance Taylor identity from Section11 gives C5 image displacement j+1 at the lower source.
The two matching target distances are j and J_max>j+1, so the complete numerator has valuation j+(j+1).
Thus its actual quotient and its residual ratio give

    C_low=2j, A_low=4j/5<j.

If instead J_max=j+1, the already exact higher-source value gives C_high=2j and A_high=4j/5<j.
These two cases exhaust the distinct positive integer distances.
The special formula j+1 is used only in the first case, at the actual unramified source; it is not extended to a fractional distance.

In either case there is an actual source with A<j and C2 image displacement at least j.
Any target distance at least j would contribute at least j through its positive integer root multiplicity, contradicting this value.
Consequently all successor distances are strictly less than j, hence less than BOTH source distances.
At the higher source every comparison is unequal, and its full C2 product now gives

    S=sum_(q in J)n_q t_q=sum_(q in J)m_q j_q=A_high>0.

All summands m_q j_q are positive integers.
Both source cases establish the claimed strict distance separation and exact S; no arbitrary distance table has replaced the actual original roots.

Choose an actual prime of J with maximal distance v.
The full C5 Taylor expansion increases every positive rational source distance strictly.
Its image displacement is therefore strictly greater than every target distance in this SAME cluster, including ties at the maximum.
Each matching root difference has exactly its target distance, so the complete actual divided quotient is

    C_max=S-1>0.

The strict positivity comes from the original residual theorem at every cycle prime, and implies S>1.
The C3 target of this prime is the original weight-two cluster i.
Its two matching roots both have distance strictly greater than v by the separation just proved.
The C3 image has exact displacement v by its unit derivative, so BOTH factors have value v and the complete quotient is

    B_max=2v.

The complete original residual ratio5B=3C consequently yields

    v=3(S-1)/10.

Every successor root distance is at most v, with its full multiplicity n_q.
Hence S<=N_J v, or

    10S<=3N_J(S-1).

If N_J<=3, the right side is at most9S-9, contradicting S>0.
Thus N_J>=4, proving UD22 and all exact statements in UD23.
No restriction on the number of successor primes, their ramification or their maximal-distance ties was introduced.

<a id="opposite-cycle-triple-degree-budget"></a>
### 19. The complete triple-average degree budget

The adopted no-unit-cluster proof in Sections16--17 gives every N_i>=2.
Let I be the indices with N_i=2 and k their number.
By UD22, every cyclic successor of an index in I has weight at least4.
The successor map is injective, and these k successors are disjoint from I.
Every remaining cluster has positive integer weight at least3, since it is outside I and all weights are at least2.
Thus 2k<=L and

    sum_i N_i>=2k+4k+3(L-2k)=3L.

This includes k=0, when all weights are at least3.
Every original prime outside the cycle remains in r=sum_(p|5)E_p f_p, so

    r_cycle=h sum_i N_i>=3hL,
    d=2r>=6hL.

For the five primitive-order31 cubic factors, L=5 and h=3, hence r_cycle>=45 and d>=90.
These statements require all five factors in the same actual Tbar and all original residual hypotheses.
The earlier distance-diversity theorem still independently requires different actual primes of different normalized distances in at least one cluster.
Numerical root multiplicities are never substituted for a count of distinct primes.
No degree90 attainment, entire opposite-cycle exclusion, cancellation-depth upper bound, characteristic-zero realization or unrestricted Task conclusion follows.


<a id="opposite-cycle-even-successor-distance-sum"></a>
### 20. An even integer sum and its forced residue modulo ten

Suppose N_i=2 and write J=i+1 for its actual successor.
By v4 Section18, every actual distance in J is strictly smaller than every distance in i, and

    S=sum_(q in J)n_q t_q=sum_(q in J)m_q j_q>1,
    v=max_(q in J)t_q=3(S-1)/10,
    N_J>=4.

Here S is the complete positive INTEGER sum, not a selected subset of roots.
In fact S is even.
For a constant-distance weight-two source with distance t, its value C=2t-1 is an integer, because2t=sum_(p in i)m_p j_p is an integer.
Its exact S=A=2C/5 is also an integer; thus5 divides C and S is even.
For a nonconstant weight-two source, the higher-distance source has E=1, and its actual integer-normalized valuation of a is2u_p by OC6.
The complete product in Section18 gives S=A_high=2u_p, again even.
These cases include a single ramified prime or a single prime of residue multiplicity2 in the constant-distance case; two primes were required only in the nonconstant case.

Choose an actual prime q_* in J attaining v, with original positive integers E_*,m_*,j_*.
The positive integer sum gives m_*j_*<=S, hence j_*<=S.
If5 does not divide S-1, then S even implies3(S-1) is coprime to10.
The equality

    10j_*=3(S-1)E_*

forces10 to divide E_*, and j_*>=3(S-1)>S because S>=2.
This contradicts j_*<=S.
Therefore5 divides S-1, and evenness gives

    S=10a+6,
    v=(6a+3)/2, a in Z_(>=0).                          (UD25)

Every source prime q in J has C3 target cluster i with total multiplicity2 and ALL target distances strictly greater than t_q.
The two complete matching root differences each have value t_q, all nonmatching differences are units and division by3 is a unit.
Thus at EVERY such original prime

    B_q=2t_q, C_q=(10/3)t_q.                            (UD26)

These are evaluations of the actual same trace polynomial and full residual ratios, with no artificial valuation assignment.

<a id="opposite-cycle-weight-four-maximal-prime-cases"></a>
### 21. Total successor weight four reduces to the endpoint S=6

Assume for contradiction N_J=4.
The maximal distance v=(6a+3)/2 has odd numerator, so its original ramification index E_* is even.
The complete root weight E_*m_*<=4 leaves exactly the possibilities

    (E_*,m_*)=(4,1),(2,2),(2,1).

For(4,1), j_*=12a+6<=S=10a+6 forces a=0.
For(2,2), m_*j_*=2(6a+3)<=10a+6 also forces a=0.
Consequently if a>=1 the maximal prime must have(E_*,m_*)=(2,1), distance v and integer distance numerator j_*=6a+3.
The other actual primes in J then have total weight2 and remaining positive integer sum

    sum_(q!=q_*)E_qm_q=2,
    sum_(q!=q_*)m_qj_q=4a+3.

There are exactly three possible positive integer weight decompositions.
One prime with(E,m)=(2,1) has j=4a+3 and distance2a+3/2>3/2.
One prime with(E,m)=(1,2) is impossible because its sum2j would have to equal the odd number4a+3.
Otherwise there are exactly two primes with E=m=1.
At either such prime t_q=j_q is a positive integer and UD26 makes the actual integer C_q=10j_q/3, so3 divides j_q and t_q>=3.
This exhausts all original primes in J; it does not assume their number in advance.
The maximal prime also has distance v>3/2 when a>=1.
Hence all distances in J would be strictly greater than3/2.

Choose an actual source prime in J of minimal distance w.
C5 strictly increases its positive rational displacement from the periodic lift at the same-cluster Frobenius target residue.
Every matching target root has distance at least w.
The non-Archimedean inequality therefore gives at least w for EACH of the four matching root differences, including any equalities or cancellations; every other original root difference is a unit.
The complete monic product and actual division by5 imply

    C_min>=4w-1.

But UD26 at this source gives C_min=10w/3.
Therefore10w/3>=4w-1, or w<=3/2, contradicting the preceding strict lower bound.
This excludes all a>=1.
The only remaining case is

    a=0, S=6, v=3/2.

Since S=sum_(q in J)n_qt_q=6=N_J v and every positive-weight t_q<=v, equality forces EVERY original prime in J to have t_q=3/2.
Thus a hypothetical weight-four successor would be constant-distance, with its exact actual values

    C_q=4(3/2)-1=5,
    A_q=2, B_q=3.                                      (UD27)

Maximal-distance ties and all possible ramification cases are included in this equality conclusion.

<a id="opposite-cycle-weight-four-next-successor-contradiction"></a>
### 22. The constant endpoint is incompatible with its arbitrary next successor

Let K=J+1 modulo L be the next actual cluster.
It is present and has N_K>=2 by the no-unit theorem; it has no other imposed prime-count or ramification restriction.
Fix a source prime in the constant-distance cluster J of UD27.
Its C2 image displacement is exactly3/2 and its complete value is A=2.
Suppose an actual target prime q in K had t_q>=3/2.
If n_q>=2, that prime alone contributes at least3 to the forward C2 baseline, a contradiction.
If n_q=1, its original E_q=m_q=1, so t_q=j_q is an integer at least2 and its contribution is3/2.
Because the complete N_K>=2 and this prime contributes weight only1, at least one OTHER actual prime q' is present.
If t_(q')<3/2, its contribution is n_(q')t_(q')=m_(q')j_(q'), a positive integer at least1.
If t_(q')>=3/2, its contribution is n_(q') times3/2, at least3/2.
In both cases the two original primes already give a baseline greater than2, again a contradiction.
Thus every actual target distance in K is strictly below3/2.

All matching comparisons are now unequal and exact, so the full original C2 product gives

    sum_(q in K)n_q t_q=sum_(q in K)m_q j_q=2.

Choose an actual prime in K attaining its maximal distance w.
The strict C5 displacement increase, all complete same-cluster target roots and the actual quotient5 give C_max=2-1=1.
Its reverse C3 target is J, with four matching roots all at distance3/2>w, so B_max=4w exactly.
The residual ratio5B=3C then implies

    w=3/20, 20j_*=3E_*.

Original integer normalization forces3 to divide j_*, so j_*>=3.
This contradicts m_*j_*<=2 in the complete positive integer sum.
Therefore the endpoint UD27 is impossible, completing the exclusion of N_J=4.
Together with the adopted N_J>=4 this proves

    N_i=2 implies N_(i+1)>=5.                            (UD28)

The proof allows L=3, when K is the remaining cyclic cluster, and uses only the stated distinctness and complete original target counts.
No extension of an integer-distance Taylor identity to fractional distances occurs; all fractional-source steps use only the strict positive-distance increase already proved in Section7.

<a id="opposite-cycle-refined-count-with-weight-two-number"></a>
### 23. Refined original degree with the exact number of weight-two clusters

Let k=card{i:N_i=2}.
By UD28 their k distinct cyclic successors have weight at least5 and lie outside that set.
All remaining clusters have integer weight at least3, since every N_i>=2.
Thus2k<=L and the complete multiplicity count is

    sum_i N_i>=2k+5k+3(L-2k)=3L+k,
    r_cycle>=h(3L+k),
    d=2r>=2h(3L+k).                                     (UD29)

Every original prime outside these clusters still contributes its unchanged nonnegative original degree term.
For the complete five-factor primitive-order31 case L=5,h=3, the precise bound is d>=90+6k.
If k>0 this implies d>=96; if k=0 this argument gives d>=90, not an unconditional96.
The actual-prime distance-diversity theorem remains independent of k and of these total root-weight counts.
No claim about exclusion of all N_i=3, realization of the allowed weights, degree-bound attainability, cancellation-depth upper bounds, complete opposite-cycle exclusion or unrestricted Task completion is asserted.


<a id="opposite-cycle-all-successor-numerators-divisible"></a>
### 24. Integer numerator divisibility at every successor prime

Suppose for contradiction N_i=2 and let J=i+1 be its actual successor.
All original primes q in J remain present, with positive integers E_q,m_q,j_q and n_q=E_qm_q, t_q=j_q/E_q.
The adopted full distance separation and actual residual products give

    S=sum_(q in J)m_qj_q in 2Z_(>0),
    N:=N_J=sum_(q in J)E_qm_q>=5,
    C_q=(10/3)t_q for EVERY q in J.                     (UD30)

The equality for C_q is UD26 at each original prime, not merely at an unramified prime or a maximal-distance source.
Multiplying by its ACTUAL E_q gives

    v_q(c)=E_q C_q=(10/3)j_q in Z.

The integer prime-value group and gcd(3,10)=1 therefore force

    3 divides j_q, hence j_q>=3, for EVERY q in J.        (UD31)

This conclusion is independent of E_q: no unramified hypothesis is introduced.
Each E_q<=E_qm_q<=N, so every original distance satisfies t_q=j_q/E_q>=3/N.
Choose an actual prime q_0 at the minimum distance w; the finite actual prime set is nonempty.
Then w>=3/N.

<a id="opposite-cycle-minimum-bound-forces-weight-five"></a>
### 25. The complete minimum-root product forces total successor weight five

At an actual source root from q_0 with its periodic lift eta, the C5 expansion strictly increases the positive rational displacement w.
Its periodic target residue is in the SAME Frobenius orbit J.
Every matching target root has distance at least w, and there are exactly n_q matching roots per actual prime q at this one geometric target residue.
Hence each of all N matching root differences has valuation at least w by the non-Archimedean inequality; equal distances or cancellation can only raise it.
All nonmatching original roots contribute units.
The actual nonzero c ensures finite evaluation, and the full quotient by5 subtracts exactly1.
Thus the COMPLETE original product gives

    C_(q_0)>=Nw-1.

Using UD30 at this source, C_(q_0)=10w/3, so

    (N-10/3)w<=1, w>=3/N.                              (UD32)

If N>=6, its positive coefficient makes the left side at least

    (N-10/3)(3/N)=3-10/N>1,

a contradiction.
Thus N<=5; the already proved N>=5 forces N=5.
For N=5, UD32 gives w<=3/5, whereas w>=3/N=3/5, so w=3/5 exactly.

At the chosen original minimum prime q_0, w=j_0/E_0, with j_0>=3 and E_0<=5.
The equality j_0/E_0=3/5 therefore forces j_0=3 and E_0=5.
Its positive integer multiplicity m_0 satisfies E_0m_0<=N=5, hence m_0=1 and n_0=5.
This one actual prime consumes the entire original weight N, so there are no other primes in J.
The complete distance sum must then be

    S=sum_(q in J)m_qj_q=m_0j_0=3,

contradicting the evenness in UD30.
The hypothetical N_i=2 is impossible; with every N_i>=2 from UD21, this proves

    N_i>=3 for EVERY named cluster i,
    k=card{i:N_i=2}=0.                                  (UD33)

No root multiplicity was identified with a count of primes: uniqueness was deduced only in the forced equality endpoint from n_0=N=5.
The proof preserves arbitrary original ramification and residue multiplicities before that endpoint, and it allows several minimal distances until the complete equality forces uniqueness.

<a id="opposite-cycle-no-weight-two-degree-scope"></a>
### 26. Local strengthening with the same global numerical degree bound

Summing UD33 and keeping every other original prime in r=sum_(p|5)E_p f_p gives

    sum_i N_i>=3L, r_cycle>=3hL, d=2r>=6hL.             (UD34)

For all five primitive-order31 cubic factors under the same complete original assumptions, L=5,h=3 and d>=90.
This is a stronger local exclusion with NO increase of the previous unconditional numerical bound.
The earlier fixed implication d>=90+6k and its k>0 consequence d>=96 are preserved unchanged at their original scopes.
The new UD33 shows that their k>0 antecedent cannot occur under the complete hypotheses; it supplies no unconditional96 bound.
Neither all weight-three clusters nor all opposite cycles are excluded, and the independent actual-prime distance-diversity theorem remains in force.
No equality attainment, original realization, cancellation-depth upper bound, new source-proof scope or unrestricted Task completion is asserted.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision no-weight-two-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:23 |
| status | open |
| reason | Register the entire unchanged retained OC1--OC13 and UD1--UD29 theorem with new UD30--UD34. For a hypothetical weight-two source, every original successor prime has integer v_q(c)=10j_q/3, forcing j_q>=3 independently of ramification. The complete minimum-root product forces total successor weight at most5; the retained lower bound5 then forces one original E5,m1,j3 prime and an odd full sum3, contradicting its required evenness. Hence every N_i>=3 and k=0. The unconditional original degree remains d>=6hL and the complete order31 bound remains90, with no unconditional96 or other numerical improvement. All previous conditional statements, original root/prime/quotient5 costs and source limits remain. Root and original_law are contributors to this extension; fresh isolated whole review is required. No weight-three exclusion, attainability, full cycle exclusion, realization or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original-field theorem and all extensions](#statement) | All OC1--OC11 and UD1--UD34 with full original P/K/F/T, nonzero integral signed residual hypotheses, complete prime/root/norm/degree weights and retained source scope; every N_i>=3/k=0 and unchanged unconditional d>=6hL/order31>=90, preserving the exact old conditional k-dependent statements. |
| argument | [Complete original-field proof](#complete-argument) | Entire Sections1--26: all retained v5 mathematics, integer numerator divisibility at arbitrary original ramification, complete minimum-source root product, successor weight upper/lower bounds, forced unique(E,m,j)=(5,1,3) endpoint and evenness contradiction, followed by the exact local versus global scope distinction. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual reciprocal nontorsion P, original fields/degrees, monic minimal T and nonzero integral divided remainders; total reality remains explicit. |
| dependency | [Actual five-adic roots and lifts](Yin_C_G0624_v5.md#complete-argument) | Complete actual local factors/root multiplicities, periodic lifts and exact C5 expansion; no old common-successor cycle exclusion is imported. |
| dependency | [Full residual comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | Exact primewise residual valuation mechanism with both actual target factors present, rechecked without identifying them. |
| dependency | [Complete maximal-order count](Yin_C_G0191_v2.md#argument) | Every original completion and maximal-order residue filtration/root count, without a maximal-power-order or unramified premise. |
| dependency | [Accepted complete-field simple-root input](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Retained statement/application depth for actual completions and common finite complete field; no new source-proof audit. |
| dependency | [Original local degrees and integer values](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Full original E_p f_p degree sum and positive integer E_p,m_p,j_p, with prior source and ancestor limits. |
| support | [Adopted exact physical v5](Yin_C_G0646_v5.md#decision-whole-reviewed-2026-10-23) | Entire OC1--OC13 and UD1--UD29/Sections1--23 retained unchanged; its predecessor review does not review or adopt UD30--UD34. |
| support | [Reuse and source boundary](#reuse-and-source-boundary) | Existing actual-source statement/application limits remain; the extension uses the original integer valuation convention and proved exact products only, without native work or new source-proof scope. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:32 |
| status | proved |
| reason | Adopt the entire OC1--OC13 and UD1--UD34 theorem after main comparison of the complete retained v5 argument with every v6 change and reading of isolated whole R867. At every hypothetical weight-two successor prime the original integer valuation forces 3 to divide j. The full minimum-root inequality and all original positive root weights force total weight5 and the unique E5,m1,j3 endpoint, contradicting the exact even distance sum. Every named cluster therefore has N_i>=3 and k=0. The unconditional original degree remains d>=6hL and order31 bound90; the retained k>0 implication supplies no unconditional96 bound. All original fields, signed nonzero residuals, arbitrary ramification, source limits and retained predecessor arguments remain. No exclusion of weight3, full cycle exclusion, realization, new native work or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original-field theorem and all extensions](#statement) | All OC1--OC11 and UD1--UD34 with full original P/K/F/T, nonzero integral signed residual hypotheses, complete prime/root/norm/degree weights and retained source scope; every N_i>=3/k=0 and unchanged unconditional d>=6hL/order31>=90, preserving the exact old conditional k-dependent statements. |
| argument | [Complete original-field proof](#complete-argument) | Entire Sections1--26: all retained v5 mathematics, integer numerator divisibility at arbitrary original ramification, complete minimum-source root product, successor weight upper/lower bounds, forced unique(E,m,j)=(5,1,3) endpoint and evenness contradiction, followed by the exact local versus global scope distinction. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual reciprocal nontorsion P, original fields/degrees, monic minimal T and nonzero integral divided remainders; total reality remains explicit. |
| dependency | [Actual five-adic roots and lifts](Yin_C_G0624_v5.md#complete-argument) | Complete actual local factors/root multiplicities, periodic lifts and exact C5 expansion; no old common-successor cycle exclusion is imported. |
| dependency | [Full residual comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | Exact primewise residual valuation mechanism with both actual target factors present, rechecked without identifying them. |
| dependency | [Complete maximal-order count](Yin_C_G0191_v2.md#argument) | Every original completion and maximal-order residue filtration/root count, without a maximal-power-order or unramified premise. |
| dependency | [Accepted complete-field simple-root input](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Retained statement/application depth for actual completions and common finite complete field; no new source-proof audit. |
| dependency | [Original local degrees and integer values](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Full original E_p f_p degree sum and positive integer E_p,m_p,j_p, with prior source and ancestor limits. |
| support | [Adopted exact physical v5](Yin_C_G0646_v5.md#decision-whole-reviewed-2026-10-23) | Entire OC1--OC13 and UD1--UD29/Sections1--23 retained unchanged; its predecessor review does not review or adopt UD30--UD34. |
| support | [Reuse and source boundary](#reuse-and-source-boundary) | Existing actual-source statement/application limits remain; the extension uses the original integer valuation convention and proved exact products only, without native work or new source-proof scope. |
| review | [Independent whole v6 finding](../audits/reviews/Yin_R_G0867_v1.md#opposite-cycle-v6-whole) | Entire statement and all26 proof sections, all original root/prime/norm/degree weights, retained predecessor cases and new arbitrary-ramification integer divisibility, complete minimum-product inequality, forced equality endpoint and exact unchanged unconditional degree scope. |

