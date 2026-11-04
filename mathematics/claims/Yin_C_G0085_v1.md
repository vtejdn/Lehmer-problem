---
author: Yin
---
# Exact faithful-profile retention, complete paired-place costs and height-uniform Salem dilution

Date: 2026-10-12T17:03.
Human author Yin.
Internal fixed extraction under continuing G0001 authorization.
The review-recovery AI authored all new mathematics in the complete D39 original00:43 proof and the actual00:53 C46 attribution amendment.
The rounding-recovery AI separately WHOLE-reviewed that amended original in R312 and NOW authors this new statement and extraction wrapper; it is a contributor to this artifact and cannot independently review this extraction.
Root supplied only the broad question and will arrange a distinct actual extraction review.
The original candidate, full proof, failed shortcut and its explicit withdrawal, original freeze, dated source correction, amended freeze and all source/role limits are retained in full below.

## Statement

Let P be an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit polynomial of original degree d=2s>=2.
Set K=Q(alpha), sigma(alpha)=alpha^-1, F=Q(alpha+alpha^-1), and let O be a full sigma-stable order containing alpha and alpha^-1.
The total logarithmic Mahler measure is m=m(P)>0 and Norm_(K/Q)(alpha)=1.
All field norms below use the ORIGINAL degree d and all embeddings.

An actual complementary packet means a finite indexed family of rational Laurent polynomials f_b, with positive normalized RATIONAL weights omega_b, all f_b(alpha) nonzero in O, and the exact Laurent identity

    sum_b omega_b f_b(t)f_b(t^-1)=E>0.

Its ACTUAL common width T is the span of the union of all coefficient supports.
After ONE common monomial normalization to[0,T], write D_b=Norm_(K/Q)(f_b(alpha)), Lambda=(1/d)sum_b omega_b log|D_b| and sigma_packet=Lambda-(1/2)log E.
The common shift has full norm1 and relative value1.
Every indexed label remains present even if some field values agree.

**A. Faithful profiles and exact rational energy.**
Suppose a supplied finite profile consists of nonzero a_i in O and positive normalized rational lambda_i with the ACTUAL field identity

    sum_i lambda_i a_i sigma(a_i)=E0 in Q, 0<E0<1,
    kappa_i=Norm_(K/Q)(a_i) in Z minus{0},
    Lambda0=(1/d)sum_i lambda_i log|kappa_i|>=0.

A faithful completion retains every original value a_i at its original indexed label, assigns it weight mu lambda_i for one0<mu<=1, and adds ONLY values+1 or-1 at the remaining positive weights.
These values are stated before the later common monomial normalization.
Any such complementary completion has

    e=mu E0+1-mu,
    mu=(1-e)/(1-E0),
    Lambda_final=mu Lambda0,
    sigma_final=mu Lambda0-(1/2)log e.

At e=E0 this identity forces mu=1 and no positive added mass, without deciding endpoint existence.
The following assertions use E0<e<1.

Whenever an accepted nonzero-target lifting interface supplies faithful rational packets with energy arbitrarily close ABOVE E0, EVERY prescribed rational e in(E0,1) has a faithful packet of EXACT energy e.
The qualitative availability is the old C11/C13 result at its actual respective domains, or an independently supplied applicable lift; this assertion does not create a new arbitrary-profile existence theorem from a unit-only input.

More precisely, take one actual rational lift e_* in(E0,e), with coordinate polynomials V_b, weights omega_b^*, original weights lambda_i/Z, actual coefficient denominator q_*, indexed denominator M_*, copies m_b=M_*omega_b^*, width T_* and full signed norms D_b.
Set theta=(1-e)/(1-e_*)=A/B in lowest positive terms,0<A<B, and h=gcd(A,M_*).
Keep every V_b at weight theta omega_b^*, adding constant1 at weight1-theta.
Then

    q_new=q_*,
    M_new=B M_*/h,
    copies_old,b=A m_b/h,
    copy_new=(B-A)M_*/h,
    signed copied value norm=(product_b D_b^m_b)^(A/h).

For the old paired-repair lift H/r+1,H/r-1, exponent0 already belongs to the actual union, so T_new=T_* EXACTLY.
More generally this width conclusion holds whenever0 is already in that union; otherwise adding1 can enlarge it.
No first-lift upper bound on q_*,M_* or T_* is supplied.
All old labels/copies and numerator contents are retained.

**B. Complete paired-place identity at ANY energy.**
For ANY actual reciprocal complementary packet as above with arbitrary E>0, select ONE root beta_j with |beta_j|>=1 from EACH inverse pair, j=1,...,s, including a separate pair for each conjugate nonreal trace embedding.
Put

    ell_j=log|beta_j|>=0, sum_j ell_j=m,
    c_bj=f_b(beta_j)f_b(beta_j^-1)!=0,
    V_j=sum_b omega_b |c_bj|,
    J_j=log V_j-sum_b omega_b log|c_bj|,
    Gamma=sum_j log(V_j/E).

The complex products c_bj are not replaced by squared moduli away from the circle.
Then

    V_j>=E, J_j>=0,
    d sigma_packet=Gamma-sum_j J_j,
    V_j<=E exp(T ell_j),
    Gamma<=Tm.

At circle pairs, V_j=E.
If T>0, the paired upper inequality is STRICT at EVERY off-circle pair, hence Gamma<Tm.
The T0 case has only the weak statement.
Equality J_j=0 holds precisely when all positive-weight |c_bj| are equal.
At a real trace place, if A_j^- is the weighted sum of absolute negative c_bj, then V_j=E+2A_j^-; this signed formula is not applied at genuinely nonreal trace places.
This is the old C10 finite positive-Poisson/reversal mechanism with explicit complete paired log loss and all original multiplicities.

**C. Intrinsic retained-mass, actual-window and FINAL-M gates.**
For the initial profile in A let c_ij^0=rho_j(a_i sigma(a_i)) and V_j^0=sum_i lambda_i |c_ij^0|>=E0, using all s inverse-pair embeddings.
Every faithful complementary completion with e in(E0,1) has mu from A and ACTUAL width T>0, and satisfies

    V_j^final=1-mu+mu V_j^0,
    Gamma_e=sum_j log[(1-mu+mu V_j^0)/e],
    d[mu Lambda0-(1/2)log e]+sum_j J_j^final
        =Gamma_e<Tm.

For every off-circle pair let R_j=exp(T ell_j)>1.
Then the exact necessary retained-mass bound is

    mu<(R_j-1)/[V_j^0-E0+(R_j-1)(1-E0)].

The denominator is positive; the bound can be weaker than mu<=1 at a given place.
The sum function

    Gamma(mu)=sum_j log[(1+mu(V_j^0-1))/(1-mu(1-E0))]

is continuous and STRICTLY increasing on[0,1], with Gamma(0)=0.
If0<Tm<Gamma(1), there is a unique mu_* in(0,1) with Gamma(mu_*)=Tm, and every such completion has mu<mu_*.
This is a necessary gate, not a sufficient construction or optimizer.
Equivalently the actual paired product is strictly less than exp(Tm)e^s.

Let M0 be the LEAST indexed denominator of the original lambda_i and M the FINAL least indexed denominator of the completion.
The original indexed copy counts give

    M mu/M0 is a POSITIVE INTEGER,
    M>=M0/mu.

These constraints do not bound q or make different target shifts cost-free.
Admissible individual signed alpha-power twists preserve relative values and full norms, but the resulting actual common width must be measured again.

**D. Genuine-Salem half-profile bound uniform over ALL norm heights.**
Now assume the stronger GENUINE Salem root configuration beta>1,beta^-1 and d-2 nonreal circle roots, with d=2s>=4 and m=log beta, and assume E0=1/2.
Let V0 be the exterior initial paired absolute sum.
The old C46 PartB floor, with V0=A_split and Lambda0=Lambda on O0, is

    V0>=2^(s-1)exp(d Lambda0)>=2.

Its finite full-norm/Jensen proof also applies to the ALREADY stated full order O: the targets remain algebraic integers, their full norms remain integers, their rational representatives imply positive circle relative values, and the exact half-profile identity holds at every pair.
This imports ONLY the moment floor.
C46's ordinary INTEGER representatives, initial q1, degree<d polynomial bound and optional house consequence are NOT inherited for arbitrary O.

For EVERY actual faithful complementary completion with EXACT e in(1/2,1), put mu=2(1-e) in(0,1) and R=exp(Tm)>1.
Then

    mu(V0-1+R/2)<R-1,
    mu<2(R-1)/V0
       <=2^(2-s)(R-1)exp(-d Lambda0),

    M>M0(V0-1+R/2)/(R-1)
       >=M0[2^(s-1)exp(d Lambda0)-1+R/2]/(R-1),
    M>M0 2^(s-2)exp(d Lambda0)/(R-1),

    0<sigma_final<2^(1-s)(R-1).

Every displayed strict sign is necessary for an actual packet; the intermediate weak sign merely substitutes the old floor.
M is the ACTUAL FINAL indexed weight denominator, not q or a chosen common multiple.

The surplus bound holds uniformly over arbitrary finite target count, positive rational weights and ALL full-norm heights Lambda0>=0.
Its new combination uses sigma_final<mu(Lambda0+1/2) and max_(y>=0)exp(-y)(y/d+1/2)=1/2.
Arbitrarily large target norms therefore do not escape the retained-mass dilution price within this faithful class.

For every fixed real C>0 and any SUPPLIED such completion of actual T<=Cd,

    sigma_final<2^(1-d/2)(exp(Cd m)-1).
    If m<=log2/(4C), then sigma_final<2 exp(-d log2/4).

Along a HYPOTHETICAL genuine-Salem sequence with m->0, C57's elementary positive degree-only measure bound forces d->infinity; no optional house theorem is needed.
This does not assert that the sequence or a degree-linear-width faithful completion exists.
The old initial split floor is credited reuse; the new conclusion combines retained mass, actual complementary width, FINAL M and height optimization.

**E. Complete signed positive nonunit control.**
On the accepted quartic

    P(t)=1-t-t^2-t^3+t^4,
    tau=alpha+alpha^-1, tau^2=tau+3,
    x=(1+sqrt13)/2, y=(1-sqrt13)/2,

the old genuine-Salem configuration has beta+beta^-1=x>2 and circle trace y in(-2,2).
Set f_+=(1+t^5)/2 and f_-=(1-t^5)/2.
Their values are

    a_+=alpha^2+alpha^3,
    a_-=1-alpha^2-alpha^3,
    a_+sigma(a_+)=2+tau,
    a_-sigma(a_-)=-1-tau,
    kappa_+=3, kappa_-=-1.

With original weights1/2,1/2 this is a half-profile with q0=2,M0=2,T0=5,Lambda0=log3/8 and a genuine nonunit.
The exact neutral mixture retains f_+,f_- and adds1 at final weights1/4,1/4,1/2, so

    mu=1/2, e=3/4, q=2, FINAL M=4,
    indexed copies=1,1,2, ACTUAL width=5,
    integer numerators=1+t^5,1-t^5,2,
    coefficient contents=1,1,2,
    full resultants=48,-16,16,
    signed copied resultant=-3*2^16,
    S_int=3, I_int=log2+log3/16,
    Lambda_final=log3/16,
    sigma_final=log2-(7/16)log3>0.

The constant is copied twice.
Its exterior V0=(4+sqrt13)/2, final exterior sum(6+sqrt13)/4 and circle final sum3/4 give

    Gamma=log[(6+sqrt13)/3],
    sum_j J_j=Gamma-[(1/4)log3+2log(4/3)]>0,
    Gamma<5log beta.

The first strict sign follows from distinct positive circle relative values; the second follows from B or the valid comparison x>13/6, beta>3/2.
The original attempted x>5/2 shortcut is FALSE and remains explicitly withdrawn in the retained author history; it is not an input to this statement.
This is a fixed positive-measure control, not a near-one family.

**F. All full arithmetic costs and exact exclusions.**
For every faithful packet above, after its one common Laurent normalization let q be the LEAST coefficient denominator, M its FINAL least indexed denominator and F_b=q f_b.
Original labels have positive integer copies M mu lambda_i.
Added labels have their own positive copies.
Then

    Res(P,F_i)=q^d kappa_i,
    Res(P,F_added)=q^d,
    product_all_copies Res(P,F)
        =q^(dM) product_i kappa_i^(M mu lambda_i),
    S_int=q^2 e>=1,
    I_int=log q+mu Lambda0,
    sigma_final=mu Lambda0-(1/2)log e.

The full norm of an added minus sign is1 because d is even.
If an integer numerator has content b_i, then b_i^d divides its full resultant.
For added labels b_i divides q; this last restriction is NOT imposed on arbitrary nonunit originals.
All original field norms, negative signs and indexed contents are kept before taking absolute logarithms.

The qualitative availability in A is accepted prior mathematics.
B holds for arbitrary actual reciprocal complementary packets and ANY E>0.
C applies to faithful completions at E0<e<1.
The stronger uniform-height bound D is restricted to GENUINE Salem inputs, half-profiles E0=1/2 and final e in(1/2,1).
No arbitrary packet is asserted to have this decomposition; changing original relative weight ratios or adding other nonunit values escapes the faithful hypotheses.
There is no input-uniform bound for the first lift's q/M, degree-linear-width construction, positive uniform surplus, unrestricted same-exponent arithmetic-income theorem or Mahler gap.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:03 |
| status | open |
| reason | Register the exact faithful-retention/energy/cost theorem, full paired-place identity and genuine-Salem half-profile height-uniform dilution combination while retaining the ENTIRE actual amended D39. The old qualitative lift and C46 split floor remain credited. R312 whole-reviewed the actual original00:43 proof plus00:53 amendment only; its reviewer now authors this wrapper, which requires another actual extraction review before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual full order and original degree, conditional qualitative interface, ANY-E paired budget, strict faithful gates, half-profile/genuine-Salem special domain, all signs/copies/denominators/width and exclusions. |
| argument | [Entire amended original author body](#argument) | COMPLETE actual amended D39: candidate, Sections1--7/equations1--19, all11 anchors, original00:43 freeze, false-shortcut withdrawal, actual00:53 C46 correction and amended freeze, all source and role limits. |
| dependency | [C10 reciprocal field and order](Yin_C_G0010_v2.md#reciprocal-field-and-order-preliminaries) | Actual inversion, original even degree, sigma-stable order, every root and full Norm(alpha)=1. |
| dependency | [C10 finite analytic mechanism](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite positive-Poisson/reversal bound for the same actual packet and physical width; the present strictness and all paired log costs are proved in the retained argument. |
| dependency | [C10 paired repair](Yin_C_G0010_v2.md#nonzero-unit-residue-completion) | H/r+1,H/r-1 nonzero repair and support0 accounting; not an automatic nonunit-target extension. |
| dependency | [C11 nonzero-target lift](Yin_C_G0011_v1.md#arbitrary-nonzero-value-rational-lifting-extension) | Old actual nonzero-target/totally-real-trace lifting domain, preserved original ratios and +/-1 additions, rational energies arbitrarily close above E0. |
| dependency | [C13 checked nonreal lift](Yin_C_G0013_v2.md#nonreal-fixed-inventory-and-lifting-costs) | Separate explicitly checked combined nonzero-target/nonreal branch and actual profile domain; no wider availability inferred. |
| dependency | [C46 old split floor](Yin_C_G0046_v1.md#statement) | ONLY PartB A_split>=2^(s-1)exp(d Lambda), exactly credited as old on O0; other parts and optional house input are not used. |
| dependency | [C46 moment proof](Yin_C_G0046_v1.md#salem-coupled-moment-obstruction) | Full original norm and finite Jensen argument; retained D39 explicitly checks its moment-only applicability to full O without integer-representative or initial-q inheritance. |
| dependency | [C57 elementary degree bound](Yin_C_G0057_v1.md#statement) | ONLY elementary PartsB/D positive fixed-degree measure bound to force d->infinity along hypothetical m->0; no optional house sharpening or tensor input. |
| dependency | [Accepted quartic control domain](Yin_C_G0076_v1.md#statement) | Old actual irreducible Salem quartic and root configuration only; no heat-bath or native result is a premise. |
| support | [Original amended whole finding](../audits/reviews/Yin_R_G0312_v1.md#paired-profile-whole-independent-finding) | Complete original00:43 proof plus actual00:53 attribution correction/amended freeze, directly reconstructed before this wrapper; no prospective coverage of the new statement or extraction. Referenced finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T17:19 |
| status | proved |
| reason | Adopt actual amended whole R312 and separate ACTUAL extraction R313. Fix exact faithful retention/energy and paired-place costs, with height-uniform dilution only for genuine-Salem half-profiles retaining old indexed ratios and adding only signs. C11/C13 qualitative existence and C46 moment floor retain their old credit, and both original and amended histories survive. No unrestricted packet obstruction or uniform gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual full order and original degree, conditional qualitative interface, ANY-E paired budget, strict faithful gates, half-profile/genuine-Salem special domain, all signs/copies/denominators/width and exclusions. |
| argument | [Entire amended original author body](#argument) | COMPLETE actual amended D39: candidate, Sections1--7/equations1--19, all11 anchors, original00:43 freeze, false-shortcut withdrawal, actual00:53 C46 correction and amended freeze, all source and role limits. |
| dependency | [C10 reciprocal field and order](Yin_C_G0010_v2.md#reciprocal-field-and-order-preliminaries) | Actual inversion, original even degree, sigma-stable order, every root and full Norm(alpha)=1. |
| dependency | [C10 finite analytic mechanism](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Finite positive-Poisson/reversal bound for the same actual packet and physical width; the present strictness and all paired log costs are proved in the retained argument. |
| dependency | [C10 paired repair](Yin_C_G0010_v2.md#nonzero-unit-residue-completion) | H/r+1,H/r-1 nonzero repair and support0 accounting; not an automatic nonunit-target extension. |
| dependency | [C11 nonzero-target lift](Yin_C_G0011_v1.md#arbitrary-nonzero-value-rational-lifting-extension) | Old actual nonzero-target/totally-real-trace lifting domain, preserved original ratios and +/-1 additions, rational energies arbitrarily close above E0. |
| dependency | [C13 checked nonreal lift](Yin_C_G0013_v2.md#nonreal-fixed-inventory-and-lifting-costs) | Separate explicitly checked combined nonzero-target/nonreal branch and actual profile domain; no wider availability inferred. |
| dependency | [C46 old split floor](Yin_C_G0046_v1.md#statement) | ONLY PartB A_split>=2^(s-1)exp(d Lambda), exactly credited as old on O0; other parts and optional house input are not used. |
| dependency | [C46 moment proof](Yin_C_G0046_v1.md#salem-coupled-moment-obstruction) | Full original norm and finite Jensen argument; retained D39 explicitly checks its moment-only applicability to full O without integer-representative or initial-q inheritance. |
| dependency | [C57 elementary degree bound](Yin_C_G0057_v1.md#statement) | ONLY elementary PartsB/D positive fixed-degree measure bound to force d->infinity along hypothetical m->0; no optional house sharpening or tensor input. |
| dependency | [Accepted quartic control domain](Yin_C_G0076_v1.md#statement) | Old actual irreducible Salem quartic and root configuration only; no heat-bath or native result is a premise. |
| support | [Original amended whole finding](../audits/reviews/Yin_R_G0312_v1.md#paired-profile-whole-independent-finding) | Complete original00:43 proof plus actual00:53 attribution correction/amended freeze, directly reconstructed before this wrapper; no prospective coverage of the new statement or extraction. Referenced finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0313_v1.md#c85-faithful-profile-actual-extraction-finding) | ENTIRE actual A--F, complete amended original and every direct qualitative/analytic/moment/control/cost interface; old C46 credit and original R312 scope retained. |

## Argument

The ENTIRE actual amended D39 follows.
Only its short author front matter is omitted and its first title lowered by one heading level.
No sentence, displayed equation, anchor, candidate, failed attempt, scope restriction, original author-freeze account, dated correction or later amended freeze is omitted or mathematically rewritten.
All11 original explicit anchors and all19 equations remain.
Existing relative links remain valid from this fixed Claim directory and require no rebasing.

The historical00:43 claim about the author's original check remains at its original date; the missing C46 attribution was actually corrected at00:53 and that complete supplement is also retained.
This extraction makes no source-completeness claim for the earlier revision and does not backdate the correction.
Root and reviewer coordination are not proof contributions; this new wrapper is a separate author contribution and awaits separate actual extraction review.
Current assessment belongs to the decision above, while retained pending-review statements remain historical.

## Quantitative retention and paired-place costs for nonunit profile completion

Date: 2026-10-12T16:28.
Human author Yin.
New AUTHOR inquiry by g0001_review_recovery after the broad root question on arbitrary nonzero integral targets.
Root supplied no construction, formula or proof.
This author has unrelated previous Claim-wrapper and review roles, none independently certifying this new argument.
No native mathematical program or external source acquisition is proposed.

## Resolved qualitative reuse and remaining question

The actual [C9](Yin_C_G0009_v1.md#statement) concerns UNIT-only profiles and the negative-relative-embedding condition.
[C10 v2](Yin_C_G0010_v2.md#statement) supplies its general reciprocal unit lift and the expressly checked totally-real nonzero-target branch, with full costs.
The actual [C11](Yin_C_G0011_v1.md#statement) ALREADY removes the unit-only obstruction on every reciprocal input with totally real trace field, including genuine Salem: its fixed integral seed1-alpha or1+alpha is not required to be a unit, and its complete changed target interface is proved.
The existing [C13 v2](Yin_C_G0013_v2.md#statement) supplies the separate nonreal trace-field profile construction and explicitly checked combined nonzero-target lift.
These qualitative results, their fixed seed norm/ideal inventory and their source limits are prior mathematics, not new contributions here.

The bounded read also located C10's retained L389 single distinguished inverse-root-product price and C35's subsequent damping-budget use.
Repeating that bound, L229 aggregation, a fixed-input capacity limit or the known L237 degree-linear auxiliary margin would not settle quantitative controllability.
C57's effective first-window deficit and exact indexed tensor costs must likewise retain their original degree-dependent bounds rather than be promoted to a uniform packet construction.
Full targeted readings and source/interface details continue below before any new theorem is frozen.

<a id="paired-profile-controllability-candidate"></a>
## Candidate before proof

Fix an ACTUAL rational field profile of nonzero integral targets with energy E0 in(0,1), and consider complementary lifts that preserve every original target and its relative weight ratios while adding only values+1 or-1.
Investigate whether exact prescribed rational final energy e in(E0,1) fixes the retained original total weight, and whether that exact e can be realized by the already proved lifts plus a fully paid neutral mixture.
This is a controllability refinement of the old existence theorem, not new profile availability; actual coefficient denominator, final indexed weight denominator and common width must remain explicit.

For every original reciprocal root pair, consider the weighted SUM of absolute relative target products, rather than only one distinguished coordinate.
Test a complete paired-place width budget, including all real split, definite and nonreal trace places with their correct multiplicities, and an exact weighted logarithmic defect that separates full norm income from this absolute-product sum.
A local elementary proof may refine the quantitative interpolation interface, but no mere change of notation for C10/L229 should be advertised as a new unrestricted result.
A fixed nonunit control should distinguish a strict refinement from an unproved uniform or near-one assertion.

All substantive development, failures, exact statements and full signed costs will be retained here.
No new source theorem, floating root, native computation, Claim adoption or uniform Mahler gap is asserted at allocation.


<a id="paired-profile-reuse-resolved"></a>
## 1. What is already proved and what is actually new here

The complete C9/C10/C11/C13 arguments were read, including the original signed/full-order hypotheses, cone matrices, rationality, nonreal phase return, second-order correction, damping, rational Gram/LDL and nonzero-value repair.
The complete canonical L390 and L392 proof bodies were separately read and directly compared with their entire retained occurrences in C10 and C11; those bodies are identical there, not summaries substituted for the proofs.
L237 and the entire C57 first-window/tensor argument were also read.

C11 ALREADY proves the requested qualitative removal of the unit-only obstruction on every reciprocal input with TOTALLY REAL trace field.
Its seed1-alpha or1+alpha has a negative relative value at an exterior real trace place and need not be a unit.
Its sole nonunit norm/ideal inventory is fixed per input; every target inverse used in a log cone belongs to an actual trace UNIT, never to that nonunit seed.
C13 v2 ALREADY treats the nonreal trace field with fixed integer-linear seeds, actual cone units and a shared phase-return subsequence, and explicitly re-proves the combined nonzero-target/nonreal lift.
Thus no new qualitative availability theorem is claimed here.
General arbitrary targets do not inherit a unit-only lift merely by changing terminology.

The old C10 finite Poisson/reversal argument and L389 distinguished-pair price are used below.
C35 already quantifies the coefficient damping cost of one chosen cone sequence, and C37/C42/C43/C56 provide stronger completion rules under supplied circle bounds or restricted profiles.
They do not provide input-uniform initial-profile selection.
The existing repair-parameter statements explicitly leave prescribed EXACT final rational energy unasserted.
The elementary exact-energy refinement below fills that small controllability point without improving their construction widths.
Its main companion is a necessary cost determined by ALL actual relative target values, and a genuine-Salem half-profile dilution bound uniform over all target norm heights.

L237's universal primitive linear-degree auxiliary has positive coefficient-energy margin but only rho<=2d; it is not a constant-covariance prescribed-value lift.
C57's degree-dependent first-window deficit and its indexed products permit norm inventories to change, and give no retained-target control.
Their exact results remain credited.
No optional Dim19 statement is needed in the new proof.
C57's elementary degree-only branch suffices if degree divergence along a hypothetical m->0 sequence is mentioned.
L229's epsilon and its accepted Pri11/Dim19 source scopes are unchanged and are NOT invoked as a new estimate below.

The later actual C46 check, requested by the independent whole reviewer and recorded at the dated amendment below, found that [C46 statement PartB](Yin_C_G0046_v1.md#statement) ALREADY contains the exact half-profile split-moment floor used as(11): A_split>=2^(s-1)exp(d Lambda).
Its [complete moment proof](Yin_C_G0046_v1.md#salem-coupled-moment-obstruction) was now actually read.
This OLD floor and its allowance for arbitrary finite positive rational weights and arbitrarily high nonunit norms are credited reuse, not a new D39 contribution.
C46 states O0 targets; the same moment-only proof is explicitly checked below for this draft's already stated full order O.
The new combination concerns faithful retained mass, the later actual complementary window, FINAL M and the uniform-over-height optimization in(12)--(15).
Neither the original floor nor its high-norm scope is being rediscovered.

The finite positive-Poisson argument is already completely supplied in [C10's direct inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality).
Its classical attribution keeps its old scope.
Cauchy--Schwarz and the elementary logarithm inequality used below are verified at the exact finite arrays; no new external source, named information-theory theorem or numerical calculation is a premise.

<a id="faithful-profile-exact-energy-and-retention"></a>
## 2. Faithful target retention and exact rational output energy

Fix an ACTUAL monic irreducible self-reciprocal nontorsion integer-unit polynomial P of original degree d=2s>=2.
Put K=Q(alpha), F=Q(alpha+alpha^-1), sigma(alpha)=alpha^-1, and let O be a full sigma-stable order containing alpha and alpha^-1.
In particular O0=Z[alpha] is allowed.
The reciprocal preliminaries are exactly C10's: K/F is quadratic, Norm_K(alpha)=1 and all original roots are retained.
Let a_1,...,a_k in O minus{0} and positive normalized rational lambda_i satisfy the ACTUAL field identity

    sum_i lambda_i a_i sigma(a_i)=E0 in Q, 0<E0<1.
    kappa_i=Norm_(K/Q)(a_i) in Z minus{0},
    Lambda0=(1/d)sum_i lambda_i log abs(kappa_i)>=0.      (1)

A faithful completion here means a finite rational Laurent packet with every original value a_i retained at an indexed original label, original weights mu*lambda_i for a common0<mu<=1, and only added values+1 or-1 at the remaining positive normalized rational weights.
Its full Laurent covariance is a constant e>0.
Values are stated BEFORE one later common monomial normalization.
Added labels are not dropped, and repeated original values still keep their indexed weights.
This definition permits any construction satisfying it, not only one damping recipe.

Evaluation at alpha gives the exact identity

    e=mu E0+(1-mu),
    mu=(1-e)/(1-E0),
    Lambda_final=mu Lambda0,
    sigma_final=mu Lambda0-(1/2)log e.                  (2)

For E0<e<1 there is0<mu<1.
Thus the energy fixes original retained mass exactly.
Neither a large coefficient denominator nor a different Gram repair can retain a larger mu at the same e under these value/ratio hypotheses.
If e=E0 then mu=1 and there can be no positive added weight; this equation does not decide existence of such an endpoint completion.

**Proposition1 (exact rational energy refinement).**
Whenever the accepted lifting interface supplies arbitrarily close-above-E0 faithful packets, EVERY prescribed rational e in(E0,1) has a faithful packet with that EXACT covariance, not just an approximation to e.
This applies to the already proved C11 profiles and C13 profiles at their respective actual domains, and to other supplied profiles for which the nonzero-target lift is explicitly available.
No extension of a unit-only existence premise is being assumed.

**Proof and exact finite costs.**
Choose one of those actual lifts with rational E0<e_*<e.
Its rationality follows from finite rational covariance.
Write its coefficients as V_b, weights omega_b^*, least coefficient denominator q_*, actual common width T_*, least indexed weight denominator M_*, copies m_b, and signed full values D_b.
The old lift has original weights lambda_i/Z and added+/-1 weights; hence e_*=1-(1-E0)/Z.
Its complete paired repair includes two polynomials H/r+1,H/r-1 differing by2.
Therefore exponent0 belongs to the actual unnormalized union support, including the constant-H branch.

Set theta=(1-e)/(1-e_*) in Q intersect(0,1).
Keep EVERY V_b at weight theta*omega_b^* and add the constant polynomial1 at weight1-theta.
Its exact covariance is theta e_*+1-theta=e.
Every original value is unchanged; its weight is theta lambda_i/Z=mu lambda_i with the mu in(2).
All values remain nonzero actual O integers.
Because exponent0 was already in the union and all old coordinates are retained, its ACTUAL common width stays T_*.
The new coefficient denominator is EXACTLY q_*: a constant integral coordinate adds no denominator and no old one is removed.
There is one extra indexed label, irrespective of duplicate values.

For theta=A/B in lowest positive terms,0<A<B, put h=gcd(A,M_*).
The FINAL least indexed denominator and copies are

    q_new=q_*, T_new=T_*,
    M_new=B M_*/h,
    copies_old,b=A m_b/h,
    copy_new=(B-A)M_*/h.                                (3)

Indeed the common numerator gcd is gcd(A m_b over b,(B-A)M_*)=gcd(A,M_*), using gcd_b m_b=1 and gcd(A,B)=1.
The signed copied value norm is (product_b D_b^m_b)^(A/h), since the new constant norm is1.
After the SAME common monomial and q_*, the integer copied resultant is q_*^(d M_new) times that signed product.
All numerator contents remain and S_int=q_*^2 e, I_int=log q_*+mu Lambda0.
No cheaper M or q is inferred from merging labels, and no construction bound uniform in the input is supplied.
This proves the proposition by one exact rational mixture, with no rational-square representability assertion about a single repair parameter.

The same dilution formula applies directly to ANY already supplied exact complementary packet of energy e_*<e<1, preserving its actual values and relative weights.
In that more general use, adding1 can enlarge the window if0 is absent; the unchanged-width assertion above specifically uses the old paired-repair support, or another explicitly supplied packet whose union contains0.

<a id="complete-paired-place-variation-budget"></a>
## 3. The complete paired-place budget for any reciprocal packet

Consider ANY finite positive rational-weight complementary packet f_i with original nonzero O values, actual common width T and exact energy E>0 on this reciprocal input.
Normalize by one common monomial to ordinary polynomials in[0,T].
Its actual full norm values are D_i, Lambda=(1/d)sum_i omega_i log abs(D_i), and sigma=Lambda-(1/2)log E.
Choose ONE root beta_j with |beta_j|>=1 from EACH inverse pair, j=1,...,s.
For a nonreal trace place its conjugate pair is counted separately; there are EXACTLY s pairs and all d original roots.
Put

    ell_j=log|beta_j|>=0, sum_j ell_j=m(P),
    c_ij=f_i(beta_j) f_i(beta_j^-1)!=0,
    V_j=sum_i omega_i abs(c_ij),
    J_j=log V_j-sum_i omega_i log abs(c_ij),
    Gamma=sum_j log(V_j/E).                             (4)

These c_ij are the embeddings of the actual relative values f_i(alpha)sigma(f_i(alpha)).
They may be real signed numbers or genuinely complex numbers.
Complex squares are NOT replaced by squared moduli before taking the absolute value in V_j.
Every source value is nonzero, so all logarithms exist.
Evaluation of the exact Laurent covariance gives sum_i omega_i c_ij=E.
Thus V_j>=E.
At a circle pair, beta_j^-1=conjugate(beta_j), so c_ij=abs(f_i(beta_j))^2>0 and V_j=E.

**Theorem2.**
The exact identity and necessary bounds are

    d sigma=Gamma-sum_j J_j,
    J_j>=0,
    V_j<=E exp(T ell_j),
    d sigma+sum_j J_j=Gamma<=T m(P).                    (5)

If T>0, the inequality at EVERY off-circle pair is STRICT; consequently Gamma<Tm(P).
Equality J_j0 holds exactly when abs(c_ij) is constant across all indexed i.
The T0 case retains the weak identities without a false strict claim.

**Proof.**
Apply the already proved finite positive-Poisson/reversal bound to the SAME vector and weights at beta_j and beta_j^-1.
Its two squared-norm sums are at most E exp(2T ell_j) and E.
Weighted Cauchy--Schwarz then gives V_j<=E exp(T ell_j).
If ell_j>0, the inverse root lies strictly inside the disk.
Equality in the positive-kernel Cauchy--Schwarz step for a polynomial requires that polynomial to be constant on the circle.
Since T>0 is the ACTUAL common width, at least one normalized coordinate is nonconstant and has strictly positive weight; its inside-disk inequality is strict.
Hence the aggregate and paired inequality are strict.
This uses no maximum principle beyond the finite kernel proof already in C10.

For J_j, apply log x<=x-1 to x=abs(c_ij)/V_j and sum weights.
The right side sums to0, giving J_j>=0, with equality only if every such x1.
Every original norm is the product of its s paired products, so d Lambda=sum_j sum_i omega_i log abs(c_ij).
Subtract s log E, using d=2s, to obtain the identity in(5).
Summing the paired upper bounds uses exactly sum ell_j=m(P).
This proves every factor and sign/multiplicity convention in(5).

The quantity sum J_j is the full weighted logarithmic concavity loss at the paired absolute products.
It is a computable target-profile cost, not an assertion that the two Cauchy--Schwarz/Poisson bounds are attained.
This refines the old full-norm inequality by displaying its paid loss and combines ALL labels/places, rather than claiming the old one-coordinate paired argument as a new analytic theorem.
Arbitrary common coefficient denominator q multiplies c_ij,V_j,E by q^2; their ratios and J_j stay the same.
The q^d norm and q^2 energy costs therefore cancel only after being explicitly included, not by removing content.

At a real trace place, let A_j^- be the sum of omega_i abs(c_ij) over its negative c_ij.
Then V_j=E+2A_j^- and the local price is T ell_j>=log(1+2A_j^-/E).
At a nonreal trace place this signed formula is not used; (4)--(5) keep the actual complex phases and both conjugate trace places.
The formula remains valid for nonunits, many expanding pairs and arbitrary E>0, provided the actual complementary packet exists.

<a id="faithful-profile-retention-width-gate"></a>
## 4. Intrinsic width and weight gate for the supplied profile

For the fixed initial profile(1), define c_ij=rho_j(a_i sigma(a_i)) and

    V_j^0=sum_i lambda_i abs(c_ij)>=E0.

A faithful completion of energy e in(E0,1) has mu from(2), and its relative absolute sums are EXACTLY

    V_j^final=1-mu+mu V_j^0,
    Gamma_e=sum_j log[(1-mu+mu V_j^0)/e].               (6)

Every added+/-1 has relative value1 at every place.
A common monomial has relative norm1, so it does not change(6).
The resulting target-based necessary budget, independent of coefficient choice, is

    d[mu Lambda0-(1/2)log e]+sum_j J_j^final
         =Gamma_e<Tm(P).                               (7)

T>0 holds here: a width-zero rational packet, after common normalization, consists of nonzero rational algebraic integers and therefore nonzero integers, whose positive-weight average square is at least1, contradicting e<1.
The same formulas are unaffected by any admissible individual signed alpha-power twists of the initial targets, since their relative values and full norms are unchanged; the actual resulting common width must still be measured, not declared invariant.

For each off-circle pair put R_j=exp(T ell_j)>1.
Its STRICT retained-mass constraint is

    mu < (R_j-1)/[V_j^0-E0+(R_j-1)(1-E0)].             (8)

The denominator is strictly positive.
This is simply1+mu(V_j^0-1)<R_j[1-mu(1-E0)], with every term retained.
It may be weaker than mu<=1 at a particular place, which is not an error.
Equation(7) is the summed full-original-measure version; the individual gates(8) are also retained rather than being replaced by their weaker average.

The function Gamma(mu)=sum_j log[(1+mu(V_j^0-1))/(1-mu(1-E0))] increases on[0,1].
The derivative of its j-th summand is

    (V_j^0-E0)/[(1+mu(V_j^0-1))(1-mu(1-E0))]>=0.      (9)

All denominators are positive on that interval.
At least one numerator is positive for an integral below-one profile: if every V_j^0=E0, logarithmic concavity would give d Lambda0<=s log E0<0, contradicting Lambda0>=0.
Thus the increase is strict.
Consequently, when Tm(P)<Gamma(1), equation Gamma(mu_*)=Tm(P) has a UNIQUE real solution mu_* in(0,1), and any faithful packet must have mu<mu_*.
This is a necessary exact one-variable gate, not a sufficient construction or a numerical root estimate.

Let M0 be the ACTUAL indexed denominator of the original lambda_i and M that of final weights.
Writing lambda_i=a_i'/M0 with integer positive gcd-one multiplicities, all M mu a_i'/M0 are integers.
Their integer Bezout combination gives

    M mu/M0 is a POSITIVE INTEGER, hence M>=M0/mu.      (10)

Combining(8) with(10) provides explicit lower prices for the actual FINAL M.
This does not bound q, identify M with a Gram dimension, or remove any original signed norm.
The strict polynomial-product equivalent of(7) is product_j(1-mu+mu V_j^0)<exp(Tm(P))*e^s, with each actual embedding multiplicity kept.


<a id="salem-half-profile-uniform-norm-height-price"></a>
## 5. A genuine-Salem half-profile bound uniform over all target norm heights

Now specialize to a GENUINE Salem input of original degree d=2s>=4: its unique expanding root is beta>1, its inverse is beta^-1, and all other s-1 inverse pairs lie on the unit circle.
Thus m(P)=log beta.
Suppose the supplied actual integral profile(1) has E0=1/2.
No upper bound on any target norm, height, number of labels or original denominator M0 is imposed.
Write V0 for its exterior paired absolute sum and keep the original Lambda0>=0.

The split-moment floor(11) below is EXACTLY the old [C46 PartB A_split floor](Yin_C_G0046_v1.md#statement) when O=O0, with V0=A_split and Lambda0=Lambda.
Its actual proof is [C46 Section3/equation(9)](Yin_C_G0046_v1.md#salem-coupled-moment-obstruction).
C46's initial ordinary INTEGER representatives and degree d-1 are needed for its further circle-polynomial bound, but not for that moment-only floor.
We do not import its initial q1 or its polynomial-circle bound into this draft's larger-order setting.

For the ALREADY stated full sigma-stable order O containing alpha and alpha^-1, each a_i is still an algebraic integer, so its nonzero original full norm is an integer and Lambda0>=0.
Every a_i has a rational representative in the same K=Q(alpha).
At a circle embedding rho, rho(sigma(a_i)) is the complex conjugate of rho(a_i), by the real rational coefficients and alpha^-1=conjugate(alpha) there.
Thus its relative value is positive, the profile identity evaluates to1/2 at each such place, and the full K/Q norm still factors over ALL inverse pairs.
These are precisely the hypotheses of C46's finite moment/Jensen argument.
The following already present calculation checks this O0-to-O applicability interface directly; it makes no automatic extension of C46's separate integer-coefficient or ordinary-degree assertions and is not a new general floor theorem.

At each of the s-1 circle pairs, every relative value is positive and has lambda-weighted sum1/2.
The elementary logarithm inequality therefore bounds its weighted log by-log2.
At the exterior pair the same inequality bounds the weighted log of the absolute relative values by log V0.
Multiplying over ALL original root pairs yields

    d Lambda0<=log V0-(s-1)log2,
    V0>=2^(s-1) exp(d Lambda0).                        (11)

The possible negative exterior relative values are not discarded; only their absolute values enter V0.
In particular V0>=2.
This is an original-degree/full-norm bound, not a relative-degree or unit-only identity.

**Theorem3 (faithful half-profile dilution price).**
For EVERY actual faithful complementary completion of this profile, with exact e in(1/2,1), actual common width T, original retained mass mu=2(1-e), and R=exp(Tm(P))>1, all of the following necessary bounds hold:

    mu(V0-1+R/2)<R-1,
    mu<2(R-1)/V0
       <=2^(2-s)(R-1) exp(-d Lambda0),                 (12)

    M > M0 (V0-1+R/2)/(R-1)
      >=M0 [2^(s-1)exp(d Lambda0)-1+R/2]/(R-1),
    M > M0 2^(s-2)exp(d Lambda0)/(R-1),                (13)

    0<sigma_final
      <2^(1-s)(R-1)
       =2^(1-d/2)(exp(Tm(P))-1).                       (14)

Here M is the ACTUAL FINAL indexed weight denominator, not a selected common multiple or the coefficient denominator q.
All inequalities with a strict sign are necessary for an actual packet.
The middle weak sign in(13) is just substitution of(11).

**Proof.**
The first inequality in(12) is(8) with E0=1/2.
Since V0>=2 and R>1, V0-1+R/2>V0/2.
This proves the remaining statements in(12).
Apply M>=M0/mu from(10) to the strict bound for mu to get the first line of(13); use(11) for its second comparison and the coarser denominator V0/2 for the last bound.
Positivity of sigma follows from Lambda0>=0 and e<1.

For the upper bound, use0<mu<1 and the elementary inequality-log(1-x)<2x for0<x<1/2.
At x=mu/2 it gives

    sigma_final=mu Lambda0-(1/2)log(1-mu/2)
                <mu(Lambda0+1/2).

Set y=d Lambda0>=0.
The function exp(-y)(y/d+1/2) has derivative exp(-y)[(1-y)/d-1/2]<=0 for d>=2, and hence is at most1/2.
Substituting(12) proves(14).
Thus even arbitrarily large nonunit norms cannot defeat this bound within the faithful half-profile class: their possible extra norm income is accompanied by the exponential dilution factor exp(-d Lambda0).
This proof uses neither a bound on those norms nor a negative-norm UNIT.

For a fixed positive C and a supplied common width T<=Cd, (14) implies

    sigma_final<2^(1-d/2)(exp(Cd m(P))-1).
    If m(P)<=log2/(4C), then
    sigma_final<2 exp[-d log2/4].                      (15)

These are quantitative NECESSARY bounds.
They neither construct a faithful packet of that width nor prove that arbitrary complementary packets admit a faithful half-profile decomposition.
On a HYPOTHETICAL genuine-Salem sequence with m(P)->0, the elementary fixed-degree branch already proved in C57 forces d->infinity.
Thus any such degree-linear-width faithful half-profile completions have exponentially vanishing surplus once(15)'s small-measure threshold holds.
This is stronger than merely dropping the paired logarithmic losses and obtaining sigma<=C m(P).
The initial profiles may change arbitrarily along the sequence, including all their target norm heights and positive rational weights.
No unrestricted Mahler gap follows: changing the mechanism, the retained relative weight ratios or the allowed added values escapes these hypotheses.

<a id="paired-profile-exact-nonunit-positive-control"></a>
## 6. Exact positive control with all signs, roots and costs

Use the original quartic

    P(t)=1-t-t^2-t^3+t^4,
    tau=alpha+alpha^-1, tau^2-tau-3=0,
    x=(1+sqrt13)/2, y=(1-sqrt13)/2.

It has the accepted genuine-Salem root pattern: x>2 gives beta>1 and beta^-1, while -2<y<2 gives the one circle pair.
Irreducibility and this root pattern are already part of the old quartic controls, including [C76](Yin_C_G0076_v1.md#statement); they are not new here.
The binomial mechanism itself is old.
This control computes its complete paired budget and a paid exact-energy refinement, not a new existence mechanism or a near-one family.

The relation P(alpha)=0 gives alpha^5=2alpha^3+2alpha^2-1.
Start with

    f_+=(1+t^5)/2, f_-=(1-t^5)/2,
    lambda_+=lambda_-=1/2, E0=1/2,
    q0=2, M0=2, T0=5.

Their actual values are a_+=alpha^2+alpha^3 and a_-=1-alpha^2-alpha^3 in O0.
For either trace embedding, the recurrence for alpha^k+alpha^-k gives alpha^5+alpha^-5=4tau+6.
Therefore the exact relative values and original-degree norms are

    a_+ sigma(a_+)=2+tau,
    a_- sigma(a_-)=-1-tau,
    kappa_+=(2+x)(2+y)=3,
    kappa_-=(-1-x)(-1-y)=-1,
    Lambda0=log3/8.                                    (16)

Both values are nonzero; the first is a genuine nonunit and the second a unit with signed full norm-1.
Their relative sum is1, giving the initial half-profile identity.
The exterior minus relative value is negative; both circle relative values are positive.
No real/complex place or original norm sign is omitted.

Add the constant1 by the exact neutral mixture theta=1/2.
The actual final packet is f_+,f_-,1 at weights1/4,1/4,1/2, so mu=1/2, e=3/4, q=2, FINAL M=4, indexed copies1,1,2, and the ACTUAL common support[0,5] has width5.
Its integer numerators are1+t^5,1-t^5,2 with contents1,1,2.
Their full original-degree resultants are48,-16,16; the constant is copied twice.
Consequently

    signed copied resultant=-3*2^16,
    S_int=3,
    I_int=log2+log3/16,
    Lambda_final=log3/16,
    sigma_final=log3/16+(1/2)log(4/3)
                =log2-(7/16)log3>0.                   (17)

For the last strict sign,2^16>3^7, an exact integer comparison.
The energy is also verified directly by(1/4)*2+(1/4)*2+(1/2)*4=3.
Its norm product is48*(-16)*16^2=-3*2^16; neither the duplicated constant content nor the negative unit norm has been removed.

The initial exterior absolute sum is V0=(4+sqrt13)/2, and the final one is V_ext=(6+sqrt13)/4.
The circle absolute sum is exactly e=3/4.
Thus the entire two-pair budget and its paid loss are

    Gamma=log[(6+sqrt13)/3],
    sum_j J_j=Gamma-[(1/4)log3+2log(4/3)]>0.           (18)

Strict positivity follows already at the circle place: its three positive relative values2+y,-1-y,1 are not all equal and all three weights are positive.
This checks that the displayed concavity cost can be nonzero on a legal positive-surplus packet; it is not a claimed new best width bound for this fixed quartic.
The strict upper bound Gamma<5log beta follows from Theorem2, or directly: x>5/2 implies beta>2, hence beta^5>32>(6+sqrt13)/3.
These comparisons use x=(1+sqrt13)/2>2, but x>5/2 is FALSE; this attempted stronger elementary comparison is withdrawn below before the author freeze.
The correct elementary comparison is x>13/6, which gives beta>3/2 because beta+beta^-1 is strictly increasing for beta>1 and3/2+2/3=13/6.
Then beta^5>243/32>10/3>(6+sqrt13)/3, since sqrt13<4.
The exact budget proof did not use the withdrawn comparison.

The control is a fixed positive-measure input.
It neither supplies a hypothetical near-one sequence nor contradicts the profile-dependent or small-measure bounds(11)--(15).

<a id="paired-profile-full-costs-and-boundaries"></a>
## 7. Complete arithmetic interfaces and remaining limits

For any packet covered by Sections2,4,5, take its actual common Laurent support interval and multiply EVERY coordinate by the same monomial alpha^b to normalize the coefficient polynomials to[0,T].
Since alpha is an actual order unit with original Norm(alpha)=1, the original values become alpha^b a_i and the added values become+/-alpha^b; their relative values and full signed norms are unchanged.
This normalization neither enlarges the actual width nor makes individually chosen shifts free.

Let q be the LEAST positive coefficient denominator of this actual entire rational packet, M its FINAL least indexed weight denominator, and let F_b=q times each normalized coordinate.
For the indexed original label i its positive integer copy count is M mu lambda_i; the added labels have their own positive integer counts, and every copy is retained.
Full original-degree resultants and costs are

    Res(P,F_i)=q^d kappa_i,
    Res(P,F_added)=q^d,
    product_all_copies Res(P,F)
       =q^(dM) product_i kappa_i^(M mu lambda_i),
    S_int=q^2 e,
    I_int=log q+mu Lambda0,
    sigma=mu Lambda0-(1/2)log e.                       (19)

The added minus sign contributes1 to its full norm because d is even.
Every numerator is nonzero at alpha.
If its integer coefficient content is b_i, then b_i^d divides the corresponding resultant q^d kappa_i; for added labels b_i^d divides q^d, hence b_i divides q.
No analogous b_i|q assertion is imposed on nonunit original targets.
These contents stay in(19).
The original Lambda0 and all kappa_i always use the original d and full K/Q norm, not just the trace field.

The coefficient denominator q and indexed denominator M remain different arithmetic costs.
Integrality gives the generic coefficient-energy floor q^2 e>=1, since each nonzero integer coefficient vector has squared norm at least1 and all weights are positive normalized.
The new argument gives necessary M bounds(10),(13) and preserves the exact q in the neutral-mix refinement(3); it supplies no upper bound for the first lift's q or M.
The rational weights are never replaced by an arbitrary real measure or a cheaper unindexed denominator.
All heights used in the proof are actual value/profile magnitudes and the actual common coefficient width.

The conclusions have three distinct domains.
Section2 is a conditional controllability refinement of already AVAILABLE faithful profiles; it does not extend the unit-only lift without the old C11/C13 checks.
Section3 is a necessary full paired-place identity for ANY actual reciprocal complementary packet at ANY E>0, including nonreal trace places with both conjugate multiplicities.
Section5 is the stronger uniform-over-norm-heights obstruction for faithful HALF-profile completions on a genuine-Salem input.
Multiple expanding pairs or genuinely complex exterior trace places are not silently included in that specialized theorem.

No new qualitative profile availability, bound uniform in the first lift's arithmetic complexity, degree-linear width construction, positive uniform surplus or unrestricted Mahler lower gap is claimed.
In particular it remains open here whether packets with changed target ratios or arbitrary added nonunit values evade this faithful-completion obstruction in a quantitatively useful way.
Existing C11/C13 availability, C10's analytic mechanism and C46 PartB's split-moment floor(11) retain credit.
The new deductions here are exact-energy interpolation with actual costs, the complete profile-specific paired loss/retention accounting, and the combination of the OLD C46 floor with faithful retained mass and actual complementary width to obtain(12)--(15).
In particular the uniform-over-height dilution optimization, rather than the initial high-norm split floor itself, is the claimed new conclusion.
Root supplied only the broad research question and no new proof step; g0001_review_recovery is the sole author of these new arguments, so this draft requires a genuinely noncontributing whole reviewer.


<a id="paired-profile-complete-author-freeze"></a>
## Complete author freeze and local verification boundary

2026-10-12T16:43.
ENTIRE Sections1--7, equations(1)--(19), the allocation candidate, all reuse limits and the explicitly withdrawn elementary control comparison above are retained in this author freeze.
The corrected control uses beta>3/2, never the false x>5/2 assertion.
The old argument is recorded as an attempted shortcut, not an active premise or independently reviewed result.

The author rechecked the full inverse-pair multiplicities, arbitrary E>0 versus faithful e<1 domains, all positivity/strictness and endpoint cases, the exact gcd denominator in(3), support0 requirement for width preservation, the original-copy Bezout cost(10), original-degree integer norms in(11), all retained-mass and denominator inequality directions, and the exponential optimization over ALL Lambda0>=0.
The quartic alpha^5/relative-value reductions, signed norms, coefficient energies, indexed multiplicities and all constants in(16)--(18) were reconstructed by hand.
The complete original-source bodies/interfaces stated in Section1 were actually read; no missing nonunit lift was inferred from a unit-only result.
This is author verification, not an independent Review or Claim acceptance.

The scoped material check of this D succeeded before freeze; it certifies structure and locators only, not these mathematical claims.
No native mathematical execution, external source acquisition or adoption was performed.
The complete draft is now ready for a separate noncontributing whole review; no pending downstream wrapper or another agent's developing extension is a premise.


<a id="paired-profile-c46-attribution-correction"></a>
## Dated C46 credit and original-order applicability correction

2026-10-12T16:53.
The separately organized whole reviewer identified an omitted existing-result attribution, not a reported failure of the displayed mathematics: equation(11) already appears in adopted C46 statement PartB as its A_split floor, with the complete proof in C46 Section3/equation(9).
The author has now actually read that statement, selected adopted decision and full moment derivation.
The initial bounded reuse account omitted this applicable Claim and must not be read as establishing novelty of that floor.
The reviewer's pointer and this correction are retained explicitly rather than silently presenting the prior result as new.

For preservation, the former Section7 contribution sentence was:

> Existing C11/C13 availability and C10's analytic mechanism retain credit; the new contributions are exact-energy interpolation with actual costs, the complete profile-specific paired loss/retention accounting, and the half-profile degree/height dilution bound above.

That sentence has been replaced in the ACTIVE scope account by explicit C46 credit and the precise distinction between its OLD initial floor and the retained-mass/complementary-width/FINAL-M/dilution combination in(12)--(15).
Section1 now records the corrected reuse result.
Section5 identifies V0=A_split and Lambda0=Lambda for O0 and checks the already stated larger full-order O interface: nonzero integer norms, the exact half-profile identity, positive circle relative values and the complete paired norm factorization suffice for the same finite Jensen calculation.
C46's separate ordinary INTEGER degree<d representatives, initial q1 and polynomial-circle cost are NOT inferred for arbitrary O.
Its optional Dim19/house consequence is not imported.
No equation(1)--(19), construction, mathematical domain or conclusion has been changed, and no new theorem or research extension is added by this credit repair.

The original allocation candidate, all original history and the ENTIRE00:43 author-freeze account remain verbatim at their old anchor/date.
That old source-completeness/contribution account is now supplemented by this actual correction; the initial freeze is not silently replaced or backdated.
The whole reviewer still owns its independent finding on the actual amended complete draft.
No fixed Claim extraction, native mathematical run, new source acquisition, global source record or shared navigation change was performed.

<a id="paired-profile-amended-entire-author-freeze"></a>
## Amended entire author freeze after C46 credit repair

2026-10-12T16:53.
Freeze the ENTIRE actual amended D39: original allocation/candidate, Sections1--7/equations(1)--(19), complete original00:43 freeze, the active C46 attribution and full-order applicability explanation, and the dated correction above.
The mathematical formulas and conclusions are unchanged.
The exact existing split-moment floor is now properly credited to C46, while its retained-mass and actual-width application is distinguished.
This remains an AUTHOR proof draft pending the separately organized noncontributor whole finding; the correction does not manufacture an independent PASS or adopt a result.
