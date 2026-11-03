---
author: Yin
---

# Uniform primitive height for complete trace-norm capacity approximation: corrected rounding statement and full costs

The complete theorem and argument below distinguish the rounded vector z from its primitive normalization c=z/g.
The [v1 preimage](Yin_C_G0524_v1.md#statement) remains open and retains its incorrect extra c/H distance sentence and its actual decisions; that statement error does not refute the original primitive-height theorem.
The complete original argument, pre-freeze sign correction, author/source facts, exact J68 controls and original review input remain inspectable in [L284](../ledger/Yin_L_G0284_v1.md#complete-retained-proof-and-review) and [R137](../audits/reviews/Yin_R_G0137_v1.md#uniform-height-complete-independent-review).
R137 contains no Review relationships declaration, so missing declaration is distinguished from an explicit unknown row; the old noncontribution account does not establish context isolation.

## Statement

Let P be an actual monic irreducible reciprocal nontorsion unit polynomial in Z[t] of degree d=2s, s>=1, constant coefficient1, and write P(t)=t^s Q(t+t^-1).
Its actual trace polynomial Q is monic integral irreducible of degree s.
Let U_0=1, U_1=x and U_(j+1)=xU_j-U_(j-1).
For nonzero c in Z^s put

    V_c=sum_(j=0)^(s-1)c_j U_j,
    C_c=sum_j c_j[t^(s+j+1)-t^(s-j-1)],
    N(c)=Res(Q,V_c),
    E(c)=2sum_j c_j^2,
    B_P(c)=log|P(1)P(-1)|/(2s)+(log|N(c)|)/s-(1/2)log E(c).

N is a real homogeneous integral degree-s form with N(c)!=0 for every nonzero integral c.
Set M=max_(||u||=1)|N(u)|>0 and let b(P) be the supremum of B_P(c) over primitive nonzero integral c.
Then b(P)=log|P(1)P(-1)|/(2s)-log2/2+(log M)/s.
This is the entire formal-degree-d anti-reciprocal class; it does not assert that every member arises from a pair of actual centered windows.

For perpendicular real unit vectors u,v the restriction T(theta)=N(u cos theta+v sin theta) has frequencies -s,-s+2,...,s and

    |T'(theta)|<=L_s M,   L_s=sqrt[s(s+1)(s+2)/3].

The checked QZ19-U001 classical Bernstein theorem gives the same derivative bound with L_s replaced by s.

Let u be a maximizing unit vector.
For an integer H>=1 round each H u_j to a nearest integer, and replace a zero highest coordinate by sign(u_(s-1)), with +1 when that real coordinate is exactly 0.
Write z for this rounded and highest-coordinate-corrected integer vector, before dividing its coefficient gcd.
Then z is nonzero, z_(s-1)!=0, height(z)<=H+1 and

    ||z/H-u||_2<=sqrt(s+3)/(2H)<=sqrt(s)/H.

Put g=gcd_j(|z_j|)>0 and c=z/g.
The primitive c has c_(s-1)!=0, the same unit direction as z, B_P(c)=B_P(z), and height(c)=height(z)/g<=H+1.
In particular deg C_c=2s and cont(C_c)=1.
The displayed distance bound concerns z/H; no corresponding bound for c/H is asserted after content removal.

With H_0=4s(s+1), every such P has a primitive c satisfying

    B_P(c)>=b(P)-log2/s,   height(c)<=4s(s+1)+1,
    deg C_c=2s,   cont(C_c)=1.

For s=1 the vector c=(1) attains b exactly.
With the sharper checked Bernstein constant s instead, H_1=ceil(4s sqrt(s)) works and

    height(c)<=H_1+1<=6s^(3/2),
    S_2(C_c)=sqrt(E(c))<=sqrt(2s)(H_1+1)<=6sqrt(2)s^2<9s^2,
    M(C_c)<=S_2(C_c)<9s^2,   rho(C_c)<=d.

For arbitrary 0<eta<1, H=ceil(2s sqrt(s)/eta) gives

    B_P(c)>=b(P)+log(1-eta)/s,
    height(c)<=H+1,   deg C_c=d,   cont(C_c)=1,
    M(C_c)<=sqrt(2s)(H+1),   rho(C_c)<=d.

For the finite grid b_H(P) over primitive c with c_(s-1)!=0 and height<=H+1,

    b(P)+log(1-eta)/s<=b_H(P)<=b(P),

the set has at most(2H+3)^s vectors, and each comparison is exact because exp(2sB)=|P(1)P(-1)|N(c)^2/E(c)^s is rational.
For each integer k>=1, with H_1 and eta=1/2, C515's exact moment lower bounds b_k satisfy

    b_k(P)-log2/s<=b_H1(P)<=b(P)<=b_k(P)+log D_(s,k)/(2ks),
    D_(s,k)=binomial((k+1)s-1,s-1).

For each primitive c with c_(s-1)!=0, let r_1,...,r_(s-1) be all roots of V_c, with multiplicities, and let z_i,z_i^-1 be the two roots of t^2-r_i t+1.
The exact complete identities are

    Res(P,C_c)=P(1)P(-1)N(c)^2!=0,
    cont(C_c)=gcd_j(c_j)=1,
    rho(C_c)=2(sum_j|c_j|)^2/sum_j c_j^2<=d,
    C_c(t)=b(t^2-1)product_(i=1)^(s-1)(t^2-r_i t+1),   b=c_(s-1)!=0,
    M(C_c)=|b|product_i max(1,|z_i|,|z_i|^-1).

All roots, multiplicities, signed values and nonreal trace roots are retained.
For a witness furnished by the H_1 construction, and every delta>0, the number of roots of C_c with modulus at least 1+delta, counted with multiplicity, is at most log(9s^2)/log(1+delta).

For the actual Lehmer input P=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1 and Q=x^5+x^4-5x^3-5x^2+4x+3, the two declared J68 grids H=45 and H=179 produce the primitive vectors (7,-9,17,-38,-14) and (29,-34,67,-150,-56), with N=2896629273 and2791077805721, E=4118 and64244, leading absolute values14 and56, complete measures 42<M(C)<91/2 and168<M(C)<182, and signed original resultants exactly -N^2 because P(1)P(-1)=-1.
Both have content1, actual degree10, trace polynomials V_45=-14x^4-38x^3+59x^2+67x-24 and V_179=-56x^4-150x^3+235x^2+266x-94, exact rho values14450/2059 and112896/16061, and strict rational margins N(c)^2/E(c)^5>(343/320)(1434031/1219123)^10.
These are two finite controls with discovery-only B decimals, not the general theorem.

If a hypothetical sequence of the actual inputs has0<m(P_i)->0 and uniform positive excess b(P_i)-m(P_i)>=delta>0, then its degrees tend to infinity and there are primitive witnesses c_i with

    B_(P_i)(c_i)-m(P_i)>=delta-log2/s_i,
    height(c_i)<=6s_i^(3/2),   M(C_i)<9s_i^2,   rho(C_i)<=d_i.

Conversely a uniform positive margin in any subclass implies that margin for b itself, but this converse does not prove the uniform excess.
The statement does not show that b(P)-m(P) stays positive, that one fixed moment detects every actual near-one input, or that a bounded-height witness is an actual coupled centered column.
It does not prescribe local primes or depths, reduce the full auxiliary Mahler expense to zero, or eliminate the leading/root costs in a later transfer.
The exterior-root count gives radial mass control only; the support/coherence information required for the unrestricted gap remains a separate mathematical gate, and exact fixed-degree attainment can still need unbounded denominator/height.
The unrestricted G0001 gap and all original route, source and negative boundaries remain unresolved.

## Current assessment
[Selected decision](#decision-complete-corrected-independent-adoption)

## Assessment history

### Decision corrected-rounding-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T17:47 |
| status | open |
| reason | Correct v1's substantive statement error by applying the distance estimate only to rounded and highest-coordinate-corrected z, before content removal; primitive c retains direction, B_P and no larger height. The complete primitive-height theorem, both Bernstein constants, exact costs, controls and unresolved boundaries are retained. This fixed revision awaits actual review of its exact current Statement and complete argument and a genuine adopting decision; original R137 neither binds this C nor has a relationship declaration. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | ENTIRE corrected current Statement, distinguishing pre-content-removal z/H from primitive c and preserving the original D151 theorem: actual irreducible reciprocal nontorsion unit domain, integral U basis and complete norm form, primitive supremum b(P), elementary and QZ19 Bernstein derivative bounds, sign-preserving rounding with failed-rule disclosure, H_0/H_1/eta grids and exact finite-grid/moment interfaces, all resultant/content/degree/Mahler/rho and exterior-root costs, the two exact J68 controls and the conditional near-one implication, with every original negative, source and Task limit. |
| argument | [Entire argument](#argument) | ENTIRE original D151 Sections1--6/equations(1)--(19): changed mechanism/reuse and QZ19 source boundary, elementary sphere derivative bound, sign-preserving rounding correction, H_0/H_1 full-height and arbitrary-accuracy derivations, complete (7)--(19) factor/content/Mahler/rho costs, finite-grid and moment interfaces, the two exact J68 controls and the exact conditional near-one/remaining-gate argument with the original author self-check and freeze retained at their fixed L284 input. |
| dependency | [Exact trace-norm moment input](Yin_C_G0515_v1.md#trace-norm-moment-hierarchy) | Only the complete anti-reciprocal norm-form representation, primitive supremum b(P) and exact moment bounds of L280; no new source reading, theorem import or proof. |
| dependency | [Exact cost conventions](Yin_C_G0515_v1.md#trace-moment-complete-costs) | Only the original root/content/leading/Mahler/rho and b_k/D_(s,k) conventions; no new estimate or near-one claim. |
| dependency | [Exact height-growth boundary](Yin_C_G0492_v1.md#statement) | Only the necessity of unbounded primitive height for exact asymptotic saturation (L273); no near-one capacity excess, actual-window realization or uniformity assertion. |
| dependency | [Sharp Bernstein derivative input](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Only Theorem1.1's exact complex trigonometric-polynomial derivative bound at printed/PDF p.3 of the retained arXiv1903.10801v1; the neighboring Riesz mechanism and the unread Section5 correction body retain their actual read/audit limits. |
| support | [Original coefficient conventions](../ledger/Yin_L_G0229_v1.md#joint-coefficient-energy-reuse) | Only original-degree/content/S1/S2/rho normalizations and the L229 convention interface; no discrepancy or external lower-bound theorem. |
| support | [J68 author control](../computations/programs/Yin_J_G0068/readme.md) | Exactly the two declared inputs/grids, the sole author run under the120-second aggregate cap and all native fields; not the general theorem or a search. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0068/readme.md#recorded-runs) | The original exact standard-library reconstruction of both grids, complete coefficients/resultants/roots/costs and reviewer-run facts; finite evidence only, not a present rerun. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0068/review_result.json`; this target locates its run account. |


### Decision complete-corrected-independent-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:03 |
| status | proved |
| reason | Adopt the actual new independent complete re-review of the corrected z/H versus primitive-c Statement and complete Sections1--6 chain, including both Bernstein bounds, full costs, finite-grid/moment interfaces and retained J68 evidence. R878 remains SELF, v1 remains its exact preimage, original R137 scope is not rewritten, and no uniform excess, window realization or unrestricted gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | ENTIRE corrected current Statement, distinguishing pre-content-removal z/H from primitive c and preserving the original D151 theorem: actual irreducible reciprocal nontorsion unit domain, integral U basis and complete norm form, primitive supremum b(P), elementary and QZ19 Bernstein derivative bounds, sign-preserving rounding with failed-rule disclosure, H_0/H_1/eta grids and exact finite-grid/moment interfaces, all resultant/content/degree/Mahler/rho and exterior-root costs, the two exact J68 controls and the conditional near-one implication, with every original negative, source and Task limit. |
| argument | [Exact argument](#argument) | ENTIRE original D151 Sections1--6/equations(1)--(19): changed mechanism/reuse and QZ19 source boundary, elementary sphere derivative bound, sign-preserving rounding correction, H_0/H_1 full-height and arbitrary-accuracy derivations, complete (7)--(19) factor/content/Mahler/rho costs, finite-grid and moment interfaces, the two exact J68 controls and the exact conditional near-one/remaining-gate argument with the original author self-check and freeze retained at their fixed L284 input. |
| dependency | [Exact dependency](Yin_C_G0515_v1.md#trace-norm-moment-hierarchy) | Only the complete anti-reciprocal norm-form representation, primitive supremum b(P) and exact moment bounds of L280; no new source reading, theorem import or proof. |
| dependency | [Exact dependency](Yin_C_G0515_v1.md#trace-moment-complete-costs) | Only the original root/content/leading/Mahler/rho and b_k/D_(s,k) conventions; no new estimate or near-one claim. |
| dependency | [Exact dependency](Yin_C_G0492_v1.md#statement) | Only the necessity of unbounded primitive height for exact asymptotic saturation (L273); no near-one capacity excess, actual-window realization or uniformity assertion. |
| dependency | [Exact dependency](../audits/literature/QZ19/Yin_U001.md#qz19-u001) | Only Theorem1.1's exact complex trigonometric-polynomial derivative bound at printed/PDF p.3 of the retained arXiv1903.10801v1; the neighboring Riesz mechanism and the unread Section5 correction body retain their actual read/audit limits. |
| review | [Complete corrected independent finding](../audits/reviews/Yin_R_G0733_v1.md#corrected-c531-v2-complete-independent-finding) | Entire exact current Statement and Argument, complete correction and affected necessary input chain at the explicitly bound scopes; actual independent re-review, without widening source, native-computation or Task authority. |

## Complete argument

<a id="argument"></a>
<a id="complete-retained-proof-and-review"></a>
<a id="uniform-primitive-height-fixed-scope"></a>

<a id="uniform-primitive-height-working"></a>
### 1. Changed mechanism, reuse and actual domain

The original 2026-10-10 argument was developed by the resultant_research AI for Yin from the coordinator's broad question, which supplied no approximation derivation.
The exact input is [L280's complete norm-form representation and primitive supremum](Yin_C_G0515_v1.md#trace-norm-moment-hierarchy), together with its [full cost conventions](Yin_C_G0515_v1.md#trace-moment-complete-costs).
The current question is whether approximate attainment of that supremum needs uncontrolled primitive height.
The answer below is negative: an explicit polynomial-height grid suffices, with an O(1/d) loss, uniformly over the input.
Exact attainment and its sharper fixed-degree limits are separate matters.

A local G-ledger/bibliography screen for fixed auxiliaries, bounded height, sign chambers, polarization, Gaussian product, Fischer/Bombieri and norm moments found L273's necessity of height growth for exact asymptotic saturation, but no uniform grid statement at this norm-form interface.
A preliminary Gaussian-contraction/discriminant approach was considered but no estimate from it is adopted here; in particular no general Gaussian-product assertion is used.
The present finite Fourier calculation is elementary.
The sharper classical Bernstein inequality is the precisely accepted [QZ19-U001](../audits/literature/QZ19/Yin_U001.md#qz19-u001), Theorem1.1 on printed/PDFp.3 of the public arXiv1903.10801v1; the neighboring Riesz interpolation proof on pp.4--5 was read and followed, without independently auditing every interpolation identity or the whole paper.
The author directly read both primary online and retained local passages.
Root separately read the source and handled canonical acquisition; that source assistance supplied none of the present approximation derivation.
The directly inspected publisher Change history identifies a Section5/Mahler-p=0 proof and reference correction, while the full correction body remains unread.
Section5 is not consumed.
The [source record](../audits/literature/QZ19/readme.md#bernstein-derivative-inspection) preserves these distinctions.
The independent elementary bound below already proves polynomial height without invoking the sharper constant.
No novelty priority is claimed for the general use of Bernstein control and rational rounding.

Let P be an actual monic irreducible reciprocal nontorsion unit polynomial of degree d=2s, s>=1, and P=t^s Q(t+t^-1).
In the integral second-kind basis U_j, write V_c=sum_(j=0)^(s-1)c_j U_j and

    N(c)=Res(Q,V_c),  C_c=sum_j c_j[t^(s+j+1)-t^(s-j-1)],
    E(c)=2||c||_2^2,
    B_P(c)=log|P(1)P(-1)|/(2s)+(log|N(c)|)/s
                                                -(1/2)log E(c).  (1)

N is a real homogeneous integral polynomial of degree s.
It need not factor into real linear forms: no all-real trace-root or Salem assumption is made.
Every nonzero integer c has N(c)!=0.
Set M=max_(||u||=1)|N(u)|>0.
L280 proves

    b(P)=sup_(primitive integer c!=0) B_P(c)
        =log|P(1)P(-1)|/(2s)-log2/2+(log M)/s.           (2)

This is the entire formal-degree-d anti-reciprocal class.
It does not assert that every member arises from a pair of actual centered windows.

### 2. Input-independent control on the sphere

For two perpendicular real unit vectors u,v, the restriction T(theta)=N(u cos theta+v sin theta) is a trigonometric polynomial with frequencies -s,-s+2,...,s, since N is homogeneous of degree s.
Its absolute value is at most M on the whole real line.
Writing its Fourier coefficients a_j, normalized Parseval gives sum|a_j|^2<=M^2.
Hence ordinary Cauchy--Schwarz gives the complete elementary bound

    |T'(theta)| <= L_s M,
    L_s=sqrt[sum_(j=-s,-s+2,...,s) j^2]
       =sqrt[s(s+1)(s+2)/3].                           (3)

There is no root-separation constant, coefficient height of P or source theorem hidden in(3).
Integration along a shortest great circle gives |N(u)-N(v)|<=L_s M*angle(u,v).
For s=1 the sphere has two points and approximation will be treated directly; the great-circle statement is needed only for s>=2.
The checked classical Bernstein theorem gives the stronger bound with L_s replaced by s.
The polynomial-height deduction will be stated both in its self-contained version and in that explicitly sourced refinement.

### 3. Rounding with a nonzero highest coordinate

Let u be a maximizing unit vector.
For an integer H>=1, round each H u_j to a nearest integer z_j, using either convention at exact half ties.
If the highest coordinate z_(s-1) is zero, replace it by the sign of u_(s-1), with +1 when that real coordinate is exactly zero.
The resulting integer z is nonzero and has z_(s-1)!=0.
Its coefficient height is at most H+1, and

    ||z/H-u||_2 <= sqrt(s+3)/(2H) <= sqrt(s)/H.         (4)

Every ordinary rounded coordinate has error at most1/(2H); the exceptional highest coordinate has error at most1/H under the specified sign choice.
This proves(4).
Author working self-check: an initial attempted rule always replaced zero by+1, which could have error3/(2H) at a small negative coordinate.
The sign-preserving rule above repairs that preliminary rounding rule before any program or author freeze; all final bounds use the repaired rule.

Assume epsilon=||z/H-u||<=1/2 and put w=z/||z||.
Since u dot(z/H)>=1-epsilon>0, the angle theta between u and w is acute.
The distance from u to the line through z/H is sin theta and is at most epsilon; therefore theta<=arcsin epsilon<=2epsilon.
Combining with(3) gives

    |N(w)| >= (1-2 L_s sqrt(s)/H) M                  (5)

whenever the right-hand relative error is below1.
Let g=gcd_j(|z_j|)>0 and c=z/g.
Then c is primitive, c/||c||=z/||z||=w, c_(s-1)!=0 and height(c)=height(z)/g<=H+1.
Homogeneity gives N(c)=N(z)/g^s and E(c)=E(z)/g^2, so B_P(c)=B_P(z)=log|P(1)P(-1)|/(2s)-log2/2+log|N(w)|/s.
Thus (5) gives the stated B loss without a distance estimate for c/H.
For example, for the admissible quadratic P=t^2-3t+1, s=1, u=(1) and H=3, rounding gives z=(3), g=3 and c=(1): ||z/H-u||=0 while ||c/H-u||=2/3>1/3.
This refutes the additional c/H sentence in [v1's Statement](Yin_C_G0524_v1.md#statement), not the original primitive-height or B_P approximation theorem.
The actual C_c then has degree exactly2s and nonzero constant coefficient, so no zero-root multiplicity is silently removed.

Take the self-contained integer grid H_0=4s(s+1).
Since L_s sqrt(s)=s sqrt((s+1)(s+2)/3)<=s(s+1), the error in(5) is at most1/2 and epsilon<=1/2.
Thus for every actual P there is such a primitive c with

    B_P(c)>=b(P)-log2/s,
    height(c)<=4s(s+1)+1,
    deg C_c=2s,   cont(C_c)=1.                         (6)

For s=1 simply take c=(1): it attains b exactly and meets all bounds.
Using the checked Bernstein constant s instead yields the smaller grid H_1=ceil(4s sqrt(s)), with the same margin loss.
These conclusions are uniform over actual P, including arbitrary coefficient height and nonreal trace roots.
This preliminary always-positive rounding failure was corrected before the original program and the 2026-10-10T04:25 author freeze.


The original [J68](../computations/programs/Yin_J_G0068/readme.md) domain was fixed before execution: one actual input, the original Lehmer polynomial, its retained L280 direction c=(196,-235,458,-1024,-384), and exactly the two deterministic rounded grids H=45 and179.
These are ceil(4s sqrt(s)) and ceil(16s sqrt(s)) for s=5.
The aggregate author mathematical cap was 120 seconds; the sole run and both complete outcomes are retained below.
The complete theorem is independent of this two-point control, and the retained starting direction need not be a global maximizer.

<a id="uniform-height-full-expenses"></a>
### 4. Complete expenses, arbitrary accuracy and the finite grid

Use M(C) for multiplicative Mahler measure and m(C)=log M(C); neither denotes the spherical maximum M in(2).
For the sharper grid H_1=ceil(4s sqrt(s)), the primitive coefficient vector in(6) satisfies

    H(c)<=H_1+1<=6s^(3/2),
    S_2(C)=sqrt[E(c)]<=sqrt(2s)(H_1+1)
                       <=6sqrt(2)s^2<9s^2,
    M(C)<=S_2(C)<9s^2.                               (7)

Here H(c) is ordinary maximum coefficient height, also the coefficient height of C, because its positive and negative exponent ranges are disjoint.
The Mahler inequality follows directly by Jensen's inequality for log on circle probability measure and Parseval; it includes the leading coefficient.
The self-contained grid H_0 instead gives the fully explicit bound M(C)<=sqrt(2s)[4s(s+1)+1].
Thus polynomial cost does not depend on accepting the sharper derivative constant.
In either case the input-independent margin loss is log2/s, the actual original resultant uses every one of the d=2s conjugates, and actual degree is exactly d.

Let b=c_(s-1)!=0 and let r_1,...,r_(s-1) be all roots of V_c, with multiplicities.
The exact factorization is

    C_c(t)=b(t^2-1) product_(i=1)^(s-1)(t^2-r_i t+1).
                                                               (8)

It follows by expanding t^(s-1)V_c(t+t^-1)(t^2-1), or the U_j identity in(1).
Consequently

    M(C_c)=|b| product_i max(1,|z_i|,|z_i|^-1),       (9)

where z_i,z_i^-1 are the two roots of t^2-r_i t+1.
This also applies to nonreal r_i; no circle-root assumption is used.
Repeated roots and t=+/-1 are retained.
The constant coefficient is -b, so all roots are nonzero and reciprocal pairs account for all d roots.
Equations(7)--(9) charge the full leading and exterior-root expense; they do not merely bound a monic residual factor.
For the H_1 witnesses satisfying (7), they imply, for every fixed delta>0,

    #{roots z of C: |z|>=1+delta}
         <= log(9s^2)/log(1+delta),                  (10)

with multiplicities; the same count holds for |z|<=(1+delta)^-1 by reciprocity.
The remaining roots need not lie on the circle, and no angular regularity follows.
In particular m(C)/d tends to0 as s tends to infinity for these witnesses, while m(C) itself need not tend to0.
This is no assertion that the actual original input measure m(P) tends to0.

The full original norm identity, coefficient content and the L229 coherence ratio are

    Res(P,C)=P(1)P(-1) N(c)^2 !=0,
    cont(C)=gcd_j(c_j)=1,
    rho(C)=S_1(C)^2/S_2(C)^2
          =2(sum_j|c_j|)^2/sum_j c_j^2 <=2s=d.       (11)

Removing an initial scalar gcd g divides the trace norm by g^s, the original resultant by g^(2s), and E by g^2; B is unchanged.
This checks that primitive normalization does not create income.
The separate degree-energy mean sum_l l|[t^l]C|^2/E equals s by pairing exponents s+j+1 and s-j-1.
It is not rho(C).
Changing the direction can change all local valuations: no prescribed prime, all-root floor, or earlier local depth is asserted to survive the rounding.
The nonzero complete resultant in(11) is the arithmetic income actually controlled.

More generally let 0<eta<1 and choose the integer H=ceil(2s sqrt(s)/eta).
Applying the same rounding and Bernstein bound gives

    B_P(c)>=b(P)+log(1-eta)/s,
    H(c)<=H+1,  deg C=d,  cont(C)=1,
    M(C)<=sqrt(2s)(H+1),  rho(C)<=d.                 (12)

The epsilon condition holds since sqrt(s)/H<=eta/(2s)<1/2; the angular error is at most eta.
For s=1 the exact vector c=(1) is again enough.
This proves an explicit tradeoff for any prescribed accuracy without requiring an effective method to find the maximizing direction.

Define b_H(P) to be the maximum of B_P(c) over all primitive integer vectors with c_(s-1)!=0 and H(c)<=H+1.
The set is finite and nonempty.
Equation(12) yields

    b(P)+log(1-eta)/s <= b_H(P) <= b(P).              (13)

The search has at most(2H+3)^s vectors.
Each comparison is exact: exp(2s B)=|P(1)P(-1)|N(c)^2/E(c)^s is rational.
There is no polynomial-time algorithm claim; the finite enumeration may be exponential in dimension and the norm-form coefficients can be large.
The full-degree grid nevertheless approximates the entire supremum, including directions whose unrounded C has smaller actual degree.

For every integer k>=1, writing b_k for C515's exact moment lower approximation and D_(s,k)=binomial((k+1)s-1,s-1), the special choice eta=1/2 combines without interchanging limits to give

    b_k(P)-log2/s <= b_H1(P) <= b(P)
                <= b_k(P)+log D_(s,k)/(2ks).         (14)

The left inequality uses(13) and b>=b_k, not a claim that a moment-maximizing integer vector is known.
This is a degree-uniform height and accuracy interface alongside the earlier degree-uniform moment interface; it is not a new lower bound for the moments.

<a id="rounded-lehmer-complete-controls"></a>
### 5. Actual small-measure Lehmer control with both complete costs

Use the original actual irreducible Salem polynomial

    P=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,
    Q=x^5+x^4-5x^3-5x^2+4x+3.                       (15)

L280 retains its actual input identity, beta>1, m(P)=log beta, and the exact upper endpoint beta<1434031/1219123.
Its direction (196,-235,458,-1024,-384) has exp(10(B-m))>7/5.
The unrestricted norm-form supremum is at least this value.
Applying(12) to a maximizing direction with eta=1/8, s=5, H=ceil(80sqrt5)=179, gives an existence statement

    B_P(c)-m(P)>log(343/320)/10>0,
    H(c)<=180,  M(C)<=180sqrt10<570.                 (16)

Indeed exp(10 times the loss)=exp(2log(7/8))=(7/8)^2, so (7/5)(7/8)^2=343/320.
This conclusion does not assume that the retained direction is a global maximizer.
It already demonstrates lower fully charged height and Mahler expenses than the retained particular witness with height1024 and M(C)>1152; it does not compare unknown globally optimal witnesses.

The one declared J68 run then checked the retained direction itself at both prescribed grids.
Exact rounding of H*c_j/sqrt(sum c_i^2), sign-preserving highest-coordinate repair and positive gcd normalization give the following complete records.
These are two controls, not an optimization search or a proof of(12).

| Grid | Primitive c in increasing U_j order | N(c) | E(c) | Leading absolute value | Complete M(C) |
| --- | --- | --- | --- | --- | --- |
| H=45 | (7,-9,17,-38,-14) | 2896629273 | 4118 | 14 | 42<M(C)<91/2 |
| H=179 | (29,-34,67,-150,-56) | 2791077805721 | 64244 | 56 | 168<M(C)<182 |

Both have content1 and actual degree10; their original signed resultants are respectively -8390461145200508529 and -7790115317588352220329841, exactly -N(c)^2 because P(1)P(-1)=-1.
Their trace polynomials are

    V_45=-14x^4-38x^3+59x^2+67x-24,
    V_179=-56x^4-150x^3+235x^2+266x-94.              (17)

The native output retains disjoint exact rational isolating intervals for all four simple real roots of each V.
Three lie in(-2,2); the remaining root lies in(-7/2,-17/5).
Its associated quadratic contributes one exterior root magnitude R satisfying 3<R<13/4: the increasing function R+R^-1 has value10/3 at3 and185/52>7/2 at13/4.
Thus(8) yields exactly the strict full Mahler intervals in the table.
All other auxiliary roots, including +/-1, have modulus1.
The leading factor14 or56 is essential and is included.

The exact positive-margin checks in the program are the rational inequalities

    N(c)^2/E(c)^5 > (343/320)(1434031/1219123)^10.   (18)

Both passed, so both actual controls satisfy the strict margin in(16), with no numerical root or logarithm inference.
Their exact rho values are14450/2059 and112896/16061, respectively, both below10.
The displayed discovery-only B decimals are approximately0.1958012719 and0.1962679829; neither decimal is the certificate.
Full C coefficients, content, signed norm, all trace-root isolating intervals and exact ratios remain in [J68](../computations/programs/Yin_J_G0068/readme.md).
The actual execution used Python3.12.14/SymPy1.14.0 and took0.0622088seconds, the only author run under the declared aggregate120-second cap.
No author failure or additional grid search occurred.

The smaller grid has the smaller full height and Mahler cost, while the larger grid has a slightly larger normalized norm margin.
Both are retained.
Choosing one does not establish a global cost optimum.
This is a fixed actual small positive m control, not a sequence with m tending to0, a near-one coverage theorem, or an actual centered-window realization.

<a id="uniform-height-near-one-boundary"></a>
### 6. Exact near-one implication, remaining gate and author self-check

For a hypothetical sequence of the actual inputs in Section1 with 0<m(P_i)->0, their degrees tend to infinity.
Indeed bounded degree and bounded Mahler measure bound every integer coefficient by the elementary-symmetric estimate |a_j|<=binomial(d,j)M(P); only finitely many such polynomials exist.
A finite set of strictly positive logarithmic measures cannot approach0.
Consequently log2/s_i->0.
Equations(6)--(14) prove that any uniform positive excess b(P_i)-m(P_i)>=delta>0 has primitive, actual-degree-d_i witnesses with

    B_(P_i)(c_i)-m(P_i)>=delta-log2/s_i,
    H(c_i)<=6s_i^(3/2),
    M(C_i)<9s_i^2,  rho(C_i)<=d_i.                  (19)

Conversely a uniform positive margin in any subclass implies that margin for b itself.
Thus approximate polynomial height is no independent missing existence condition for a uniformly positive whole-class capacity excess.
This is conditional on that excess, which remains unproved on unrestricted near-one inputs.
Exact maximum attainment at fixed degree can still need unbounded denominator/height as the desired error tends to0, consistently with L273 and L280.

The theorem does not show that b(P)-m(P) stays positive, that one fixed moment detects every actual near-one input, or that a bounded-height witness is an actual coupled centered column.
It does not prescribe local primes or depths, reduce full auxiliary Mahler expense to zero, or eliminate the leading/root costs in a later transfer.
The exterior-root count(10) gives radial mass control only.
The support/coherence information required to use a witness in the unrestricted gap problem remains a separate mathematical gate.
L237's existing uniform scalar margin is not reproved or relabeled missing.
The unrestricted G0001 gap remains unresolved.

The remaining mathematical questions are the actual moment/capacity excess and an actual-window approximation to these completely charged, full-degree low-height grids.
A stronger radial/angular relation could also matter, but(10) alone supplies none.
A near-one family is neither assumed to exist nor constructed here.

The original author self-check on 2026-10-10 and the 2026-10-10T04:25 frozen input remain inspectable in [L284](../ledger/Yin_L_G0284_v1.md#uniform-height-near-one-boundary).
The original [R137 whole finding](../audits/reviews/Yin_R_G0137_v1.md#uniform-height-complete-independent-review) records the 2026-10-10T04:29 inspection of that full frozen Sections 1--6/(1)--(19) argument and both J68 controls.
R137 has no Review relationships declaration; its historical relationship is unestablished, and no current C statement or argument binding is retroactively attributed to it.
The consumed source theorem is confined to the precise QZ19-U001 refinement; the elementary alternative remains complete.
G0001 is not solved by this result.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0068](../computations/programs/Yin_J_G0068/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
