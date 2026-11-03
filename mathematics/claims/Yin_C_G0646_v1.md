---
author: Yin
---

# Opposite trace-cluster cycles and necessary tripling excess

Human author Yin.
Root supplied the opposite-cycle baseline comparison, full residual ratio and primitive-order31 application.
Paid_comparison checked and completed the actual local-factor and root-count argument, finite equal-distance cancellation conclusion, and the integer/parity refinement of the weighted excess.
Both are contributors, not independent reviewers.
This is a necessary obstruction, not a complete inverse-cycle exclusion or an original realization.
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

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision opposite-cycle-excess-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T21:58 |
| status | open |
| reason | Register the necessary complete weighted cancellation budget for opposite C2/C3 cycles in the full original residual domain. Both directions have the same baseline by complete geometric-root counts, every source prime has integer values(2u,3u,5u), and the exact identity2X3-3X2=Ecycle forces actual equal-distance tripling cancellation. The integer baseline/excess and odd/even refinement, original degree/norm weights and order31 example are fully retained. Root and paid_comparison are contributors; fresh isolated whole review remains required. No all-inverse-cycle exclusion, original realization, unproved excess upper bound or unrestricted completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original opposite-cycle statement](#statement) | OC1--OC11: complete original P/K/F/T and nonzero integral signed residual domain, all present same-degree opposite-cycle factors, every prime/ramification/residue multiplicity, exact restricted norm/degree weights, integer/parity excess and actual finite tripling cancellation, with exact order31 scope and all nonrealization limits. |
| argument | [Complete local-count and excess proof](#complete-argument) | Entire Sections1--6/OC12--OC13, complete local lattice counts and periodic lifts, unit-derivative displacement and reverse baseline, both strict residual valuation cases, original integer(2u,3u,5u) values, exact weighted excess/parity, genuine equal-distance cancellation and the five order31 trace orbits. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual irreducible reciprocal nontorsion P, original degrees d=2r, exact P=z^r T(z+z^-1), nonzero integral trace quotients and their distinction from original phase-bearing K-elements; total reality is explicitly retained as a hypothesis. |
| dependency | [Adopted five-adic original root/lift interface](Yin_C_G0624_v5.md#complete-argument) | Complete actual Q5 factors, every geometric residue root count, unique periodic lift and embedding-invariant distances; no old same-successor cycle conclusion is imported as an opposite-cycle exclusion. |
| dependency | [Previously established full residual local comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | IC3 strict-valuation mechanism when both C2/C3 target factors are present, rechecked without requiring those targets to coincide; the old proper-support degree bounds are not applied. |
| dependency | [Maximal-order local count mechanism](Yin_C_G0191_v2.md#argument) | Sections1--2 completion decomposition and full maximal-order residue filtration/root multiplicity, not an assumption that Z_5[delta] is maximal; its dyadic numerical conclusions are not imported. |
| dependency | [Accepted complete-field simple-root theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Theorem9.1 at its accepted statement/application depth, applied to C_(5^h)-X with derivative-1 in actual finite completions and a common complete field; no new original-proof audit. |
| dependency | [Original local degree and valuation conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual E_p f_p contributions, complete sum over all original F-primes above5 and integer prime-value groups, with existing source/ancestor-proof limits retained. |
| support | [Reuse and source limits](#reuse-and-source-boundary) | Focused local opposite-cycle search, exact C624/C191/C153 and U readings, preserved original source depth, direct finite order31 algebra and no native scan/realization or excess upper bound. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:05 |
| status | proved |
| reason | Adopt the complete OC1--OC13 theorem after main reading of entire C646 and isolated whole R854. Every original prime/root multiplicity and degree/norm weight is retained. The reverse-cycle baselines, primewise integer valuations(2u,3u,5u), positive integral excess and parity refinement force at least one ACTUAL finite equal-distance C3 cancellation. The order31 five-orbit example has the exact stated conditional scope; no all-opposite-cycle exclusion, original realization, excess upper bound or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire original opposite-cycle statement](#statement) | OC1--OC11: complete original P/K/F/T and nonzero integral signed residual domain, all present same-degree opposite-cycle factors, every prime/ramification/residue multiplicity, exact restricted norm/degree weights, integer/parity excess and actual finite tripling cancellation, with exact order31 scope and all nonrealization limits. |
| argument | [Complete local-count and excess proof](#complete-argument) | Entire Sections1--6/OC12--OC13, complete local lattice counts and periodic lifts, unit-derivative displacement and reverse baseline, both strict residual valuation cases, original integer(2u,3u,5u) values, exact weighted excess/parity, genuine equal-distance cancellation and the five order31 trace orbits. |
| dependency | [Actual original trace-field interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual irreducible reciprocal nontorsion P, original degrees d=2r, exact P=z^r T(z+z^-1), nonzero integral trace quotients and their distinction from original phase-bearing K-elements; total reality is explicitly retained as a hypothesis. |
| dependency | [Adopted five-adic original root/lift interface](Yin_C_G0624_v5.md#complete-argument) | Complete actual Q5 factors, every geometric residue root count, unique periodic lift and embedding-invariant distances; no old same-successor cycle conclusion is imported as an opposite-cycle exclusion. |
| dependency | [Previously established full residual local comparison](Yin_C_G0624_v5.md#additional-complete-integral-support-argument) | IC3 strict-valuation mechanism when both C2/C3 target factors are present, rechecked without requiring those targets to coincide; the old proper-support degree bounds are not applied. |
| dependency | [Maximal-order local count mechanism](Yin_C_G0191_v2.md#argument) | Sections1--2 completion decomposition and full maximal-order residue filtration/root multiplicity, not an assumption that Z_5[delta] is maximal; its dyadic numerical conclusions are not imported. |
| dependency | [Accepted complete-field simple-root theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Theorem9.1 at its accepted statement/application depth, applied to C_(5^h)-X with derivative-1 in actual finite completions and a common complete field; no new original-proof audit. |
| dependency | [Original local degree and valuation conventions](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual E_p f_p contributions, complete sum over all original F-primes above5 and integer prime-value groups, with existing source/ancestor-proof limits retained. |
| support | [Reuse and source limits](#reuse-and-source-boundary) | Focused local opposite-cycle search, exact C624/C191/C153 and U readings, preserved original source depth, direct finite order31 algebra and no native scan/realization or excess upper bound. |
| review | [Independent entire opposite-cycle finding](../audits/reviews/Yin_R_G0854_v1.md#opposite-cycle-whole-finding) | Complete original OC1--OC13 and Sections1--6, all maximal-order local counts/lifts, full signed residual ratios, exact weighted baseline/excess/integer/degree statements, actual finite cancellation and order31 example; retained source-statement/application boundaries. |

