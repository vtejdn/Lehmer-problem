---
author: Yin
---
# Powered Frobenius ratios and the existing auxiliary residue criterion

The complete current mathematical statement and necessary original proof are adopted in [C580](../claims/Yin_C_G0580_v1.md#decision-complete-current-self-adoption), with [actual constructor whole SELF review](../audits/reviews/Yin_R_G0758_v1.md#current-g436-complete-self-finding).
The complete original analysis, source/contribution boundaries, useful failures and mathematical continuation questions remain below.


Initial powered-lift analysis dated 2026-10-18T10:48.
Human author Yin.
The main agent assigned a reuse-first inquiry into automatic Frobenius class coverage under continuing G0001 authority.
The assigned author supplies the powered-lift construction below; the main agent's question did not supply its power selection, algebra or constants.
This complete author argument was fixed for separate whole review.
The later [R443 whole finding](../audits/reviews/Yin_R_G0443_v1.md#powered-ratio-whole-independent-finding) and [strategy adoption](../strategies/Yin_S_G0001.md#powered-ratio-adoption-2026-10-20) apply at the unchanged supplied-parameter scope; no Claim or Task completion is inferred.
No mathematical program, numerical inversion, prime search or near-one example is used.

## Exact question and bounded reuse

Can a controlled positive power of an actual residue-Frobenius lift have a bounded global conjugacy class even when the original lift does not, with its prime-power height and original-norm costs retained?
Read the complete accepted C146v5 and C147v5, the actual C146v2 own-field and signed-norm interfaces, C146v1's original-Galois coverage comparison, L160/L162's Salem classes and least-prime boundaries, and L397's full local-lift symmetrization and abelian-trace-field screen.
A focused search of G Claims/ledgers and relevant source audits for abelian subgroups, bounded index, decomposition groups, cyclic lift order, dihedral groups and class size found no fixed powered-lift version of the own-ratio theorem among the inspected matches.
This is a bounded reuse observation, not a novelty claim.

The tempting bounded-index-abelian application was then checked against primary literature before developing it as a new coverage result.
The retained AM16 author manuscript, printed pages 1--4, points to Amoroso--Zannier 2010 for dihedral fields.
The exact AZ10 institutional author manuscript was obtained and registered; its printed page 2 Theorem 1.2 gives a stronger uniform absolute-height theorem depending only on the abelian base degree.
Its exact statement and applicability are retained in [AZ10-U001](../audits/literature/AZ10/Yin_U001.md#az10-u001).
Thus bounded-index-abelian coverage is classical, including nonnormal original fields, and is not a new gap domain of this inquiry.

<a id="powered-frobenius-statement"></a>
## Candidate complete powered-lift statement

Let alpha be a nontorsion algebraic integer unit of original degree d and total logarithmic Mahler measure m>0.
Let L be its normal closure, G=Gal(L/Q), and let sigma be an actual residue-Frobenius lift at a chosen prime of O_L above a rational prime p.
Fix any integer f>=1, put q=p^f and tau=sigma^f, and let kappa_f be the actual G-conjugacy-class size of tau.
Write H_5 for the complete capped threshold in the accepted [C147v5 statement](../claims/Yin_C_G0147_v5.md#statement).
For any supplied integer k>=kappa_f, the proposed exact consequence is

    m > H_5(log p/k) / [p(q+1)k] > 0.                  (1)

No bound on f, p or k is automatic in this statement.
It specializes to the accepted C146v5 supplied-class criterion when f=1.
It differs from substituting q as a rational prime: the local income remains log p, and the binomial amplification still uses p.

The responsible arithmetic objects and full original return are derived next, before any use of this candidate as a new input.

<a id="powered-frobenius-proof"></a>
## Complete local derivation with every original cost

Let H_alpha=Gal(L/Q(alpha)), H'=H_alpha intersection C_G(tau), K'=L^(H'), d'=[K':Q]=r d, and rho=alpha^q/tau(alpha).
The same subgroup index injection as [C146v1](../claims/Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) gives r<=kappa_f.
Tau centralizes H', so it restricts to an actual finite-order automorphism of K'.
Both alpha and tau(alpha) lie in K', and rho is an algebraic integer unit.
If rho^M=1 for an integer M>=1, then alpha^(qM)=tau(alpha)^M; iteration through the finite order t of tau forces alpha^((q^t-1)M)=1, a contradiction since q>=2.
Thus rho is nontorsion.
Put E=Q(rho), D=[E:Q] and m_rho=log M(P_rho); then 2<=D<=d'<=kappa_f d.

The actual residue action of tau is the q-th power, because sigma is a residue-Frobenius lift and f is an integer.
For every selected K'-embedding represented by gamma in C_G(tau), the commuting identity gives

    gamma(rho)=gamma(alpha)^q/tau(gamma(alpha))=1
                           modulo the chosen prime.

There are d'/kappa_f such embeddings, and each E-embedding has exactly d'/D extensions to K'.
Consequently at least D/kappa_f distinct original rho-conjugates have positive depth.
Each lies in its own degree-D field, so its normalized valuation is at least 1/D under v(p)=1 by the accepted [The26b-U001 degree interface](../audits/literature/The26b/Yin_U001.md#the26b-u001).
For an element at depth t>0, p-th powering gives depth at least min(pt,1+t), hence at least min(pt,1).
With

    n=p^ceil(log_p D)<pD,

all selected depths are at least 1 after those steps, including p=2 and arbitrary ramification.
All other conjugates contribute nonnegative valuations.
Non-torsion makes the full rational integer norm nonzero, giving

    log abs Norm_(E/Q)(rho^n-1)/D >= log p/kappa_f.     (2)

The full positive and negative logarithmic sums over K' give

    h_abs(rho)<=(q+1)m/d,
    m_rho<=kappa_f(q+1)m,
    u=n m_rho/D <p m_rho<=p(q+1)kappa_f m.             (3)

The denominator d'/D and every original conjugate have been retained.
Apply C147v5 to rho as its ORIGINAL degree-D unit and n as its exponent; its further powered-degree drops are already included.
If kappa_f<=k, equation (2) supplies income at least log p/k, and its complete inverse implication gives u>H_5(log p/k).
Together with (3), this proves the strict candidate bound (1) for every m>0, including u above the small-height domain.
The cap and endpoint do not require any numerical inversion.

For the original-field return put beta=alpha^(qn)-tau(alpha)^n and xi=Norm_(K'/Q(alpha))(beta).
The identity beta=tau(alpha)^n(rho^n-1) yields the complete signed norm

    xi in O_(Q(alpha)), xi!=0,
    Norm_(Q(alpha)/Q)(xi)
      =epsilon Norm_(E/Q)(rho^n-1)^(d'/D),
    epsilon in {1,-1},
    log abs Norm_(Q(alpha)/Q)(xi)/d'
      =log abs Norm_(E/Q)(rho^n-1)/D.                  (4)

Its separable relative product has r factors, at most 2^r signed conjugate monomials before collection, and total conjugate exponent at most rqn.
The exact time bounds are

    n<p kappa_f d, qn<pq kappa_f d,
    rqn<pq kappa_f^2 d.                               (5)

These expenses are original-degree linear only when p, f and kappa_f are controlled.
Integrality is in the full original integer ring, with no cheap power-basis representative or bounded one-variable coefficient mass asserted.
The proof does not presume that tau is itself a residue-Frobenius lift for a new rational prime q.

<a id="bounded-abelian-index-screen"></a>
## A concrete automatic power selection, already classically covered

Suppose G has an abelian subgroup A of index b; A need not be normal.
For a supplied sigma, act on the b left cosets G/A and follow the orbit of A.
Its length f is an integer with 1<=f<=b, and sigma^f A=A, hence tau=sigma^f belongs to A.
Since A is abelian, A is contained in C_G(tau), giving kappa_f<=b.
Using p=2 and q=2^f<=2^b in (1) therefore gives the explicit candidate method bound

    m > H_5(log2/b)/[2(2^b+1)b].                      (6)

This really supplies a controlled power for every local lift, without finding a special prime or assuming a small unpowered class.
The nonnormal subgroup does not require passage to its core or a factorial index bound.

However, AZ10 Theorem 1.2 already gives much stronger coverage.
With F=L^A one has [F:Q]=b and L/F is Galois with abelian group A, even when F/Q is not normal.
Every intermediate F(alpha)/F is therefore abelian.
The source theorem gives

    h_abs(alpha)>3^(-b^2-2b-6),
    m=d h_abs(alpha)>d*3^(-b^2-2b-6).                  (7)

For b bounded this is a classical uniform positive absolute-height bound, stronger in coverage and degree behavior than (6).
This exact source check closes the proposed bounded-index-abelian application as a new gap route.
Its retained value is the paid-power interface and the distinction between actual unpowered and powered conjugacy classes.
No new Claim is needed merely for the source specialization (7).

<a id="local-order-global-class-boundary"></a>
## Why small local order is not the missing class bound

At an unramified prime, the decomposition group is cyclic generated by its Frobenius element.
This supplies no uniform upper bound on that element's GLOBAL conjugacy-class size in terms of its order alone: it only places the decomposition group inside the centralizer.
The resulting inequality is |class(sigma)|<=|G|/|D_p|, with the uncontrolled global group order still present.
[L397](Yin_L_G0397_v1.md#all-local-lifts-symmetrization) already proves that taking all places returns a positive power of the same global class product and does not eliminate its price.

As an elementary group-only diagnostic, in S_s a transposition has order 2 and a cyclic subgroup of order 2, but its conjugacy class has size s(s-1)/2.
This does not assert an actual low-measure polynomial with that Galois action or any fixed small prime realizing that cycle.
The existing actual Salem calculation [L162](Yin_L_G0162_v1.md#salem-kernel-class-population) is the relevant arithmetic-domain comparison: complex conjugation has order 2 and class size d/2 in degree d.
It likewise supplies no fixed-prime realization or near-one family.
Thus bounded order alone cannot be relabelled as bounded unpowered class; when one uses a bounded power instead, the q=p^f expense in (1) and (5) must be paid.

## Original author check and application question

The C147v5 inverse applies at the same n and to the same full ratio norm; the angular C159 estimate is not used.
The original complete powered-stage author checklist is retained at [its responsible formal SELF finding](../audits/reviews/Yin_R_G0758_v1.md#original-powered-author-self-finding), with the actual original date precision.

No substantive new near-one coverage beyond known classical domains has been established.
A potentially useful further condition would supply a bounded p and bounded f with bounded class(sigma^f) in a family not already covered by known height theorems.
Small total m has not been shown to supply that condition.
At the initial check the application question remained unfinished; the bounded-index-abelian case was already closed by the classical theorem above.
The later complete comparison below identifies the old auxiliary criterion covering the entire bounded-parameter condition, without asserting that the original criterion supplies those parameters automatically.

<a id="powered-lift-residue-transfer"></a>
## Entire supplied-parameter class inside the old auxiliary residue criterion

Continuation dated 2026-10-20T09:13.
The draft_comparison_cleanup AI supplies the following full powered-parameter comparison under root's request to resolve the remaining application question.
Root supplied the research question and requested precise coverage distinctions, not a step of this argument.
This continuation was prepared as author work for the later whole review identified above.

The bounded reuse check read [L398's exact own-ratio comparison](Yin_L_G0398_v1.md#own-ratio-old-mass-proof) and [L205's accepted bounded-residue mass theorem](Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape), with its [whole R104 scope](../audits/reviews/Yin_R_G0104_v1.md#minimal-frobenius-local-complete-independent-review).
L398 treats q=p and does not silently authorize q=p^f in a prime slot.
The argument below derives the actual powered ratio and reduced-root count before applying L205 at the same rational prime p, with reduction-factor degree cutoff one.
The initial external screen of central powers and local degree led back to these sufficient local inputs; no further external theorem is needed or invoked.

### Exact old criterion and the inclusion being proved

For a nontorsion monic irreducible integer-unit polynomial Q of degree D, let W_(p,1)(Q) be the total degree in its linear irreducible factors modulo p, including their polynomial multiplicities.
The accepted L205 equation(14) states that for every supplied 0<delta<=1,

    W_(p,1)(Q)>=delta D
       implies
    m(Q)>=delta log2/[(p-1)p^(ceil(1/delta)+1)].     (8)

It has no small-m threshold, unramifiedness, distinct-reduction, power-basis-index or bounded ambient-ramification premise.
In particular it applies to the primitive minimal polynomial of ANY nontorsion algebraic integer unit, whether or not it generates the original alpha field.

Thus the already available auxiliary-transfer condition, for fixed p,C>0 and 0<delta<=1, is the existence of an actual nontorsion algebraic integer unit eta satisfying

    m(eta)<=C m(alpha),
    W_(p,1)(P_eta)>=delta deg(P_eta).               (9)

The old criterion gives m(alpha)>=delta log2/[C(p-1)p^(ceil(1/delta)+1)] whenever (9) holds.
This is merely division of (8) by C, not a newly claimed height theorem.
The substantive question for the powered construction is whether its original-input hypotheses actually supply such an eta at bounded C and positive delta.

Retain the exact original input, prime p, chosen prime above p, residue-Frobenius lift sigma, integer f>=1, q=p^f, tau=sigma^f and kappa=kappa_f from (1)--(5).
For every supplied positive integer k>=kappa, the powered construction supplies (9) with

    eta=rho=alpha^q/tau(alpha),
    C=k(q+1), delta=1/k.                           (10)

Consequently its entire stated supplied-parameter class obeys

    m(alpha)>=log2/
       [k^2(p-1)(p^f+1)p^(k+1)].                  (11)

This conclusion is an exact inclusion in the old auxiliary-transfer domain (9).
It does not claim that L205 itself previously stated the powered original-input hypothesis, that (9) implies existence of a controlled Frobenius power, or that the two parameterized numerical lower bounds (1) and (11) are ordered.

### Actual ratio, complete conjugate fibers and repeated reductions

Set H_alpha=Gal(L/Q(alpha)), C_tau=C_G(tau), H'=H_alpha intersection C_tau and K'=L^(H').
As in the earlier powered derivation, d'=[K':Q]=r d with r<=kappa.
The element tau centralizes H', hence normalizes it and induces a finite-order automorphism of K'.
Both alpha and tau(alpha) are integral units in K', so rho is one as well.
If rho^v=1 for v>=1, iteration of tau(alpha)^v=alpha^(qv) through the finite order t of tau gives alpha^((q^t-1)v)=1.
Since q>=2 and alpha is nontorsion, this is impossible.
Put E=Q(rho), D=[E:Q]; then D>=2 and E is a subfield of K'.

Embeddings of K' represented by C_tau comprise exactly

    [C_tau:H']=d'/kappa

distinct embeddings.
For each such representative gamma, the residue action of tau at the chosen prime is q-th powering, and commutation gives

    gamma(rho)=gamma(alpha)^q/tau(gamma(alpha))
                  congruent to 1 modulo that prime.

The denominator is a unit.
The residue action is valid even if gamma does not preserve the chosen prime: it is applied to the actual algebraic integer gamma(alpha) by tau, which does preserve that prime.
No Frobenius-at-q interpretation is used.

Each distinct E-embedding has exactly d'/D extensions to K'.
Therefore the selected embeddings give at least D/kappa distinct original conjugates of rho reducing to 1.
If that quotient is not an integer, the actual count is at least its ceiling.
Reducing the factorization of the monic minimal polynomial P_rho over a local splitting field preserves all D root labels.
Hence T-1 occurs in its mod-p reduction with multiplicity at least D/kappa, and

    W_(p,1)(P_rho)/D>=1/kappa>=1/k.                (12)

This count does not identify distinct conjugates with distinct residue values; all selected conjugates may reduce to the same value 1.
Neither the ramification of L nor a good power basis is being bounded.

The complete positive and negative original logarithmic sums of alpha each equal m(alpha).
Galois invariance of height and the elementary height inequality consequently give

    h_abs(rho)<=q h_abs(alpha)+h_abs(tau(alpha))
                 =(q+1)m(alpha)/d,
    m(rho)=D h_abs(rho)<=kappa(q+1)m(alpha)
                           <=k(q+1)m(alpha).      (13)

The multiplier D is rho's own degree, not d or d'.
Equations (12)--(13) prove (10).
Applying (8) with Q=P_rho and delta=1/k uses ceil(1/delta)=k exactly and gives

    m(rho)>=log2/[k(p-1)p^(k+1)].

Division by k(q+1) proves (11).
This proof retains p=2, k=1, every f>=1, arbitrary repeated reduction and all original total-measure normalizations.
It neither invokes the conclusion of C147 nor assumes any Mahler gap under investigation.

### Uniform constants and the exact remaining distinction

Fix a finite nonempty set of rational primes Pset and positive integers F,K.
For every original input admitting p in Pset, 1<=f<=F and kappa_f<=K, apply (12)--(13) directly with delta=1/K and C=K(p^F+1).
One obtains the degree-independent positive bound

    m(alpha)>=min_(p in Pset)
       log2/[K^2(p-1)(p^F+1)p^(K+1)]>0.          (14)

No monotonicity through a ceiling or a choice of constants depending on the original degree is needed.
The same conclusion covers all finite-order and torsion-twisted special cases of tau(alpha); the preceding ratio proof did not assume multiplicative independence or a bounded order for a root-of-unity twist.
The bounded-index-abelian specialization remains additionally covered by AZ10 as already recorded.

This supplies a complete old-criterion derivation for the entire bounded-p,f,kappa sufficient condition, not just its abelian or unramified subcases.
Its content is the explicit powered original-input-to-auxiliary bridge and the honest cost (10), not a new source height theorem.
That bridge may be a useful formulation even though its positive-gap consequence lies in the already available transfer criterion.
No global assertion that the literature contains no other applications is made.
In particular, a genuinely new automatic theorem forcing these parameters on previously unresolved inputs would still be additional mathematics; the mere statement of bounded p,f,kappa does not establish one.
Neither the original argument nor this comparison proves that small total measure supplies controlled powered classes.
Quantitative refinements with growing p,f,kappa and constructions outside (9) are not excluded by (14), but they are outside the fixed-parameter application pursued here.

<a id="powered-lift-fixed-inputs"></a>
## Exact inputs for the complete powered argument and coverage comparison

| Role | Fixed target | Exact use |
| --- | --- | --- |
| Supplied-class antecedent | [C146v5](../claims/Yin_C_G0146_v5.md#statement) | Existing f=1 comparison; its class criterion is not silently applied with a composite rational prime. |
| Subgroup and original-field interface | [C146v1](../claims/Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Centralizer index injection and actual original-field construction, with the powered variant fully derived here. |
| Complete cyclic norm | [C147v5](../claims/Yin_C_G0147_v5.md#statement) | Exact H5 and its strict full-range inverse, applied to rho in (1)--(5); not needed to prove (11)--(14). |
| Local residue and valuation interface | [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Actual residue-Frobenius action and degree-D valuation denominator in the earlier candidate proof, including ramification. |
| Existing auxiliary comparison | [L398](Yin_L_G0398_v1.md#own-ratio-old-mass-proof) | Unpowered q=p mechanism and reuse lead; no automatic extension of its original statement to q=p^f is assumed. |
| Accepted old mass theorem | [L205](Yin_L_G0205_v1.md#bounded-residue-mass-near-one-escape) and [R104](../audits/reviews/Yin_R_G0104_v1.md#minimal-frobenius-local-complete-independent-review) | Whole own-input bounded-residue theorem (14), with F=1, delta=1/k or 1/K, no small-height guard and full repeated-reduction scope. |
| Classical bounded-index domain | [AZ10-U001](../audits/literature/AZ10/Yin_U001.md#az10-u001) | Exact source theorem and nonnormal-base specialization for (7); source proof remains unreviewed at the previously recorded scope. |
| Local/global class warning | [L397](Yin_L_G0397_v1.md#all-local-lifts-symmetrization) and [L162](Yin_L_G0162_v1.md#salem-kernel-class-population) | Existing full-class multiplicity and actual Salem involution comparison, not prime-existence or near-one-realization inputs. |
