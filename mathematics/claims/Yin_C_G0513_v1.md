---
author: Yin
---

# Complete all-prime nonreduced layer capture and paid arithmetic coverage

This retains the complete necessary mathematical argument from [Complete fixed L408](../ledger/Yin_L_G0408_v1.md#nonreduced-layer-question).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P in Z[t] be monic, irreducible, nontorsion and a unit, of original degree d, with alpha a root, K=Q(alpha), m=log M(P)>0 and the actual order O0=Z[alpha].
For EVERY rational prime p, including primes of repeated reduction or power-basis index, factor the complete reduction Pbar=product_phi phi^e_phi with distinct monic irreducible phi of nonzero constant term.
Write f_phi=deg(phi) and o_phi for the prime-to-p multiplicative order of a root of phi.
Define the finite nonnegative integer layer weights by

    b_phi(0)=f_phi,
    b_phi(a)=f_phi[min(e_phi,p^a)-min(e_phi,p^(a-1))], a>=1,
    w_(o p^a)=sum_(phi:o_phi=o)b_phi(a).

Only positive weights are retained, with a complete label weight retained whenever that label is selected.
The multiplicity e_phi is the multiplicity of the polynomial reduction and is not identified with a ramification index.
If A is the original integral companion matrix, then for every integer n>=1, with the full signed original norm D_n=Norm_(K/Q)(alpha^n-1)=det(A^n-I)=Res(P,t^n-1),

    sum_r w_r=d,  0<=w_r<=phi(r),
    h_p(n):=sum_(r|n)w_r
       =deg gcd(Pbar,t^n-1)=dim_(F_p)ker(A^n-I mod p)
       <=v_p(abs D_n).

Here D_n is nonzero, and only a lower floor is selected; all deeper Smith factors, original conjugates, other primes and powered-field multiplicities remain in the actual norm.
The exact full identity period is T_p=lcm_phi(o_phi)*p^ceil(log_p(max_phi e_phi)), and h_p(n)=d holds exactly when T_p divides n.
No index-prime ideal-valuation formula or bound T_p=O(d) is assumed.

For any nonempty selection S of complete positive layer labels, put W=sum_(r in S)w_r, and for every integer X>=1 define

    H_X=max_(1<=n<=X)sum_(r in S,r|n)w_r,
    delta_X=W^-3 sum_(a,b,c in S,lcm(a,b,c)<=X)w_a w_b w_c.

The ordered triples include repetitions, and labels above X remain in the original mass W.
For every fixed 0<s<1, let K_s be the finite, generally nonnumerical constant in C142v2 for arbitrary finite real phi-capacity arrays.
Then

    H_X>=(delta_X/K_s)^(1/s)W^2/X.

One actual integer n<=X attaining H_X satisfies log(abs D_n)>=H_X log p, with the unchanged auxiliary t^n-1 of full degree n, content1 and squared coefficient norm2.
No income from different times or selected subnorms is pooled.
For a second, purely counting criterion, choose w_r distinct formal primitive r-th roots for each label and sort all W counting angles cyclically.
For each consecutive edge with labels a,b define U_X(a,b)=sum_(c in S,lcm(a,b,c)<=X)w_c and Score_X=sum_(all W cyclic edges)U_X(a,b).
The formal angles are not asserted to be original characteristic-zero roots or roots of p-power order in F_p.
Including wraparound and the gap1 when W=1, one has H_X>=Score_X/X for every such choice.

If FIXED C>0, 0<gamma,delta<=1 satisfy W>=gamma d, 1<=X<=Cd and delta_X>=delta, then one integer n<=Cd has norm density at least eta=(delta/K_s)^(1/s)*gamma^2*log(p)/C.
For h in(0,exp(-40)] set Phi_5(h)=86 sqrt(h)[log(1/h)]^(5/2)/[log log(1/h)]^(3/2), the strictly increasing C147v5 envelope tending to zero at0.
For eta>0 let H_5(eta)=exp(-40) if eta/2>=Phi_5(exp(-40)), and otherwise let H_5(eta) be the unique h in that interval with Phi_5(h)=eta/2.
The strict capped inverse gives m>H_5(eta)/C>0.
The alternative premise Score_X>=sigma W^2 for fixed sigma>0 gives the same conclusion with eta=sigma gamma^2 log(p)/C.
Replacing log p by log2 gives a constant uniform over p; no numerical inversion, feasible value for K_s, automatic population of either class or new unrestricted gap is claimed.

For fixed C>0 with floor(Cd)>=1 put U_C(P)=max_(1<=n<=floor(Cd))log(abs D_n)/d.
For every prime, every selection with W>=gamma d and every integer 1<=X<=Cd,

    delta_X<=K_s[C U_C(P)/(gamma^2 log p)]^s,
    Score_X/W^2<=C U_C(P)/(gamma^2 log p).

Both quantities vanish if U_C(P)=0.
When 0<Cm<=exp(-40), U_C(P)<=Phi_5(Cm).
Along a hypothetical sequence m(P)->0 these density and score quantities therefore tend uniformly to zero over all primes, full-layer selections and these windows, with C,gamma,s fixed.
Existence of such a sequence is not asserted, and these parameters may not silently vary.

For EVERY integer r>=2, the original reciprocal polynomial P_r(t)=(t-1)^(2r)+2t^r of degree d=2r is irreducible by the monic Eisenstein translate P_r(t+1)=t^(2r)+2(t+1)^r, and is nontorsion because a trace root 2+2^(1/r)exp(pi i/r) is nonreal.
It is not asserted to be Salem.
Modulo2 its reduction is (t-1)^d, but D_1=P_r(1)=2 and v_2(abs D_1)=1, refuting the unpaid assignment of all d units to raw order1.
Its exact paid layer law and full-law window statistics are

    w_1=1, w_(2^a)=min(d,2^a)-min(d,2^(a-1)), a>=1,
    h_2(n)=min(d,2^v_2(n)),
    b=floor(log_2 X), H_X=min(d,2^b),
    delta_X=[min(d,2^b)/d]^3.

Thus delta_1=d^-3, whereas X=2^ceil(log_2 d)<2d captures the complete mass, including the terminal partial increment when d is not a power of2.
The existing C491 bounded-residue criterion already gives m(P_r)>=log2/4, so this is a fixed-positive-measure control, not new near-one coverage.

On the actual odd squarefree cyclotomic controls P=Phi_N, d=phi(N), choose N with q_min(N)->infinity and N/phi(N)->infinity as in C144.
For every integer 1<=n<N the full original norm is nonzero and equals abs D_n=Phi_h(1)^(d/phi(h)), h=N/gcd(N,n)>1.
For each prime p not dividing N the only layer label is N with weight d and no activation in a window X<N.
For p dividing N and M=N/p, the only positive layer weights are w_M=d/(p-1) and w_N=(p-2)d/(p-1).
For every 1<=n<N, v_p(abs D_n)=h_p(n), including all Smith depths.
For the complete law and X<N, the capture and triple density are zero if M>X, and otherwise H_X=d/(p-1), delta_X=1/(p-1)^3.
Consequently for every fixed C>0, eventually X=floor(Cd)<N and, uniformly over all primes and all allowed counting-angle choices,

    delta_X<=1/(q_min-1)^3 ->0,
    Score_X/d^2<=C/(q_min-1) ->0.

These are torsion controls and do not refute a nontorsion near-one coverage theorem.
The existence of FIXED C>=1, delta>0 and epsilon>0 forcing the complete layer law to have delta_(floor(Cd))>=delta at some prime for EVERY irreducible reciprocal nontorsion unit with 0<m(P)<=epsilon remains OPEN.
No new native calculation, selected numerical input, external-source proof audit or research continuation is supplied.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:02 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Uniform real capacity capture](Yin_C_G0142_v2.md#statement) | Every fixed exponent between zero and one, complete original capacity law, repeated triples and finite nonnumerical constant; no automatic arithmetic density. |
| dependency | [Complete cyclic norm envelope and strict inverse](Yin_C_G0147_v5.md#statement) | Original degree and actual powered-field multiplicity, fixed small-height domain, monotone envelope and capped strict inverse after supplied income. |
| dependency | [Original bounded-residue control](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Only the existing positive lower bound for the repeated-linear-factor family and its prior-coverage exclusion. |
| dependency | [Actual squarefree torsion controls](Yin_C_G0144_v1.md#zero-measure-full-window-budget) | Actual cyclotomic sequence and full signed norm tower, including all primes and depths; not a nontorsion near-one counterexample. |
| support | [Finite score antecedent](Yin_C_G0088_v1.md#statement) | Counting-angle gap and residual-bucket antecedent, with the entire needed proof reproduced for the new complete layer law. |
| support | [Complete companion period antecedent](Yin_C_G0251_v1.md#scalar-period-jordan-formula) | Existing full Jordan period; the new layer identity period is also derived directly from the retained gcd formula. |
| support | [Dyadic complete-order antecedent](Yin_C_G0050_v1.md#statement) | Earlier exact multiplicity-aware dyadic packet domain only. |
| support | [Different local multiplicity capture](../ledger/Yin_L_G0221_v1.md#local-multiplicity-scaled-depth-capture) | Comparison only; its cyclotomic auxiliaries need not share one cyclic time and do not replace the companion-corank argument. |
| support | [Same-time norm convention](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Comparison and original-norm convention; no ideal-valuation identification at index primes is imported. |
| support | [Orbital coverage comparison](Yin_C_G0146_v5.md#statement) | Earlier strategy scope only, not an assumed orbital or matching-density premise. |
| support | [Matching coverage comparison](Yin_C_G0162_v1.md#statement) | Earlier strategy scope only, not automatic high-residue-degree layer density. |
| support | [Previously covered own-ratio class](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Prior coverage comparison only, not a new subclass or near-one family. |
| dependency | [Accepted monic Eisenstein scope](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Existing monic Theorem4.1 and monic Gauss scope only for the displayed translated monic family; no nonmonic extension or new source reading. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:10 |
| status | proved |
| reason | Adopt after actually reading the entire exact Statement and unchanged complete original proof, all necessary fixed interfaces and the actual new whole SELF. All prime/index/nilpotent, one-time income, original-degree, full norm, source and torsion/control limits remain; no original proof defect, fresh independent review, native execution or automatic coverage is manufactured. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0142_v2.md#statement) | Every fixed exponent between zero and one, complete original capacity law, repeated triples and finite nonnumerical constant; no automatic arithmetic density. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | Original degree and actual powered-field multiplicity, fixed small-height domain, monotone envelope and capped strict inverse after supplied income. |
| dependency | [Exact dependency](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Only the existing positive lower bound for the repeated-linear-factor family and its prior-coverage exclusion. |
| dependency | [Exact dependency](Yin_C_G0144_v1.md#zero-measure-full-window-budget) | Actual cyclotomic sequence and full signed norm tower, including all primes and depths; not a nontorsion near-one counterexample. |
| support | [Exact support](Yin_C_G0088_v1.md#statement) | Counting-angle gap and residual-bucket antecedent, with the entire needed proof reproduced for the new complete layer law. |
| support | [Exact support](Yin_C_G0251_v1.md#scalar-period-jordan-formula) | Existing full Jordan period; the new layer identity period is also derived directly from the retained gcd formula. |
| support | [Exact support](Yin_C_G0050_v1.md#statement) | Earlier exact multiplicity-aware dyadic packet domain only. |
| support | [Exact support](Yin_C_G0532_v1.md#local-multiplicity-scaled-depth-capture) | Comparison only; its cyclotomic auxiliaries need not share one cyclic time and do not replace the companion-corank argument. |
| support | [Exact support](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Comparison and original-norm convention; no ideal-valuation identification at index primes is imported. |
| support | [Exact support](Yin_C_G0146_v5.md#statement) | Earlier strategy scope only, not an assumed orbital or matching-density premise. |
| support | [Exact support](Yin_C_G0162_v1.md#statement) | Earlier strategy scope only, not automatic high-residue-degree layer density. |
| support | [Exact support](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Prior coverage comparison only, not a new subclass or near-one family. |
| dependency | [Exact dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Existing monic Theorem4.1 and monic Gauss scope only for the displayed translated monic family; no nonmonic extension or new source reading. |
| review | [Exact review](../audits/reviews/Yin_R_G0724_v1.md#complete-all-prime-layer-whole-self-finding) | Entire exact all-prime Statement and complete original nine sections/equations1–21, full layer capacities/companion-corank/Smith floor, original single-time capture and strict capped inverse, complete reciprocal and all-prime torsion controls, source/input/contribution/negative limits and the open automatic-coverage boundary. Actual current relation is SELF; old R413 whole UNKNOWN remains separate. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-18T15:30.
Human author Yin.
The angular_envelope_review AI develops this new S4/S8 inquiry under the root's continuing all-strategy allocation.
Root supplied the arithmetic-coverage direction, not the layer construction or its proof.
This fixed bounded exploration asserts no automatic positive-density coverage or unrestricted gap.
No mathematical program or J is proposed or executed.
Current outcome: the complete all-prime layer/capture bridge, reciprocal raw-order discriminator and all-prime torsion comparison below have been proved and author-checked.
The automatic small-positive-measure coverage question remains open.

<a id="nonreduced-layer-question"></a>
## Responsible question and reuse

Can the original compatible-order capacity mechanism include EVERY rational prime, rather than discard primes with repeated reduction, while retaining the original degree and one actual exponent?
The proposed changed object distributes each multiplicity across its nilpotent activation levels instead of attaching its entire mass to the prime-to-p residue order.
The next coverage question is whether small positive total measure forces positive triple density for this complete distribution at some prime and an original linear time.
No automatic density is assumed in the structural argument.

Read the actual S4/S8 frontiers and C86/C88/C91 capacity, score and density statements.
The later accepted [C142v2](Yin_C_G0142_v2.md#decision-whole-reviewed-2026-10-15) already settles general positive-triple-density capture for arbitrary real phi-capacity arrays.
The older C91 unrestricted linear-pair estimate is false, and its historical fixed-density question is not reopened here.
Read [C146v5](Yin_C_G0146_v5.md#statement), [C147v5](Yin_C_G0147_v5.md#statement), [C162](Yin_C_G0162_v1.md#statement), and [L205](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape).
[L398](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) already covers the qualitative bounded-prime/bounded-orbital/positive-matching class through the own-ratio polynomial.
No such class or another B3 quadratic grid is the target here.

[L70](Yin_C_G0251_v1.md#scalar-period-multiplier-order) already identifies the companion's complete Jordan periods.
[C50](Yin_C_G0050_v1.md#statement) already uses the full order modulo 2, including the largest multiplicity, for its dyadic packet classification.
[C532](Yin_C_G0532_v1.md#local-multiplicity-scaled-depth-capture) already pays multiplicity-scaled local lifting and joins order-adapted cyclotomic auxiliaries; those auxiliaries need not share one cyclic time.
[L74](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) already aggregates genuine local incomes at one exponent.
The new point to check is an exact nonnegative phi-capacity decomposition of the ENTIRE companion nullity function, so that C142 applies at arbitrary bad primes without changing d, the time window, or the order.
The opening bounded G-only screen found these related interfaces, not a previously retained instance of this particular decomposition; no exhaustive priority claim is made.

<a id="nonreduced-layer-definition"></a>
## 1. Complete layer distribution

Let P be a monic irreducible nontorsion integer-unit polynomial of ORIGINAL degree d.
Write K=Q(alpha), m=log M(P)>0, and use the actual power-basis order O0=Z[alpha].
Fix ANY rational prime p and factor the COMPLETE reduction

    Pbar=product_phi phi^(e_phi),       f_phi=deg phi.

All phi are distinct monic irreducibles over F_p with nonzero constant term.
Let o_phi be the multiplicative order of any root of phi, so p does not divide o_phi.
For a>=0 put

    b_phi(0)=f_phi,
    b_phi(a)=f_phi[min(e_phi,p^a)-min(e_phi,p^(a-1))]  (a>=1),
    w_(o p^a)=sum_(phi:o_phi=o)b_phi(a).                    (1)

Only positive weights are retained.
Every label is a positive integer and its prime-to-p part and p-exponent identify o,a uniquely.
There are finitely many positive weights.
All original polynomial multiplicities enter (1); e_phi is not identified with a field ramification index.

The exact identities proved below are

    sum_n w_n=d,                 0<=w_n<=phi(n),
    h_p(n):=sum_(r|n)w_r
       =deg gcd(Pbar,t^n-1)
       =dim_(F_p) ker(A^n-I mod p)
       <=v_p |Norm_(K/Q)(alpha^n-1)|,                       (2)

where A is the ORIGINAL integral companion matrix of P.
The final inequality preserves the full original signed norm before absolute value, and is a lower bound only.
Higher Smith depths, other primes and maximal-order information are not discarded from the actual norm.

<a id="nonreduced-layer-capacity-proof"></a>
## 2. Exact capacities, nullities and full original norms

For a>=1 the increment min(e,p^a)-min(e,p^(a-1)) lies between 0 and p^a-p^(a-1)=phi(p^a).
For a=0 the corresponding multiplier is 1=phi(1).
The distinct irreducible factors of order o have disjoint sets of f_phi roots among the phi(o) primitive o-th roots in an algebraic closure of F_p.
These primitive roots are distinct because p does not divide o.
It follows, without using any reduction multiplicity in that last root count, that

    sum_(phi:o_phi=o) f_phi<=phi(o),
    w_(o p^a)<=phi(o)phi(p^a)=phi(o p^a).                 (3)

Every weight is a nonnegative integer.
For an individual factor, telescoping through a=ceil(log_p e_phi) gives total e_phi f_phi.
Summing over the factors proves sum w_r=d.
The terminal increment is exactly f_phi[e_phi-p^(a-1)] when p^(a-1)<e_phi<=p^a; it is not rounded up to a full level.
For e_phi=1 only a=0 contributes.
Thus the claimed capacities cost no factor p/(p-1) or 2.

Write n=p^b u with p not dividing u.
In characteristic p,

    t^n-1=(t^u-1)^(p^b).

The polynomial t^u-1 is separable, and phi divides it exactly when o_phi divides u.
Consequently

    deg gcd(Pbar,t^n-1)
       =sum_(phi:o_phi divides u) f_phi min(e_phi,p^b)
       =sum_(r|n)w_r=h_p(n).                            (4)

The last equality telescopes the SAME layers (1) through a=b.
These weights are dimensions of successive nilpotent layers, not a claim that each layer is a disjoint subset of p-adic conjugates with valuation one.

The original companion A acts as multiplication by t on F_p[t]/Pbar.
For any polynomial q, put g=gcd(Pbar,q), Pbar=gP1 and q=gq1.
Then Pbar divides qf if and only if P1 divides f, because gcd(P1,q1)=1.
The residue classes in this kernel are exactly P1 h with deg h<deg g.
This proves its dimension deg g, and proves the nullity identity in (2) for q=t^n-1 without a separability or maximal-order hypothesis.

The full integer matrix A^n-I has nonzero determinant

    D_n=det(A^n-I)
       =product_(i=1)^d(alpha_i^n-1)
       =Norm_(K/Q)(alpha^n-1)
       =Res(P,t^n-1).                                   (5)

Here all d ORIGINAL conjugates occur, including every repeated value after powering.
Nontorsion excludes zero determinants.
In an integer Smith form the number of diagonal factors divisible by p is exactly the mod-p nullity h_p(n).
Each such factor contributes at least one to v_p|D_n|, proving the last inequality in (2).
Equivalently row and column elimination over Z_p at the mod-p unit pivots leaves an h_p(n)-square block all of whose entries are divisible by p.
No identification of O0/pO0 with a product of residue fields or of e_phi with ramification was used.
The determinant is the field norm because it is multiplication on a full original basis, even if p divides [O_K:O0].

The entire mod-p identity period is recovered exactly:

    T_p=lcm_phi(o_phi) p^ceil(log_p max_phi e_phi),
    h_p(n)=d if and only if T_p divides n.                (6)

Indeed all the min(e_phi,p^b) terms in (4) must be saturated and every order must divide u.
This is L70's already known companion period, now recovered as the full-mass endpoint of the layer distribution.
Its size is not asserted O(d).
The factor p in individual rounding remains real: the largest level for phi is o_phi p^ceil(log_p e_phi), which is less than p o_phi e_phi when e_phi>1, and is o_phi when e_phi=1.
No p-dependent horizon is renamed an absolute constant.

<a id="nonreduced-one-time-capture"></a>
## 3. Compatible triples and circular score at arbitrary primes

Select any set S of complete positive layer labels from (1), with their actual weights w_r and total W>0.
Selection means taking those complete label weights; it does not assert that they are selected original root subsets.
For an integer X>=1 put

    H_X(S)=max_(integer 1<=n<=X) sum_(r in S,r|n)w_r,
    delta_X(S)=W^(-3) sum_(a,b,c in S,lcm(a,b,c)<=X)
                                      w_a w_b w_c.       (7)

All ordered repetitions are included, and labels above X remain in W.
Fix 0<s<1 and the finite K_s of the actually adopted C142v2 statement.
By the exact capacities (3), that theorem applies unchanged and gives

    H_X(S)>=(delta_X(S)/K_s)^(1/s) W^2/X.                (8)

There is ONE integer n<=X attaining H_X(S).
Equations (2) and (5) give at this same integer

    log|D_n|>=v_p|D_n| log p
             >=H_X(S) log p.                            (9)

All other layers, deeper Smith factors and other primes remain in the actual norm.
Only the displayed lower floor is selected.
The auxiliary is exactly t^n-1, of full degree n, content 1 and squared coefficient norm 2.
There is no mixed resultant, relative field norm, denominator, selected subnorm or aggregation of different times.

There is also the unchanged C88 circular-score mechanism on these ACTUAL integer weights.
Choose w_r distinct formal primitive r-th roots of unity for each r in S, which (3) permits, and sort their W angles cyclically.
These are counting angles, not the original characteristic-zero conjugates or finite-field roots of p-power order.
For each consecutive edge with labels a,b and circular gap g, including the single-point gap 1 when W=1, define

    U_X(a,b)=sum_(c in S,lcm(a,b,c)<=X)w_c,
    Score_X=sum_(all W cyclic edges) U_X(a,b).

Then

    H_X(S)>=Score_X/X.                                  (10)

For completeness, with L=lcm(a,b) one has g>=1/L.
If L>X the link mass is zero.
Otherwise group compatible c by j=c/gcd(c,L), so Lj<=X.
Each bucket divides the one integer Lj and therefore has weight at most H_X(S).
Hence U_X(a,b)<=XH_X(S)/L<=XH_X(S)g.
Summing all gaps, whose total is 1, proves (10).
This directly supplies every zero-link, repeated-label, wraparound and W=1 case; no new angle optimization is asserted.
The extension changes the arithmetic inventory, not C88's finite counting argument.

Suppose now W>=gamma d, X<=C d and delta_X(S)>=delta>0, for FIXED C>0 and 0<gamma,delta<=1.
Then (8)--(9) supply one n<=C d with

    log|D_n|/d>=eta,
    eta=(delta/K_s)^(1/s) gamma^2 log p/C.               (11)

C147v5's accepted complete cyclic inverse gives

    m>H_5(eta)/C>0.                                     (12)

Indeed n m/d>H_5(eta), while n/d<=C.
Its cap handles the large-height branch automatically and its original-powered-degree accounting is unchanged.
Using log 2 in (11) gives a uniform constant even when p varies.
The corresponding score premise Score_X>=sigma W^2, for fixed sigma>0, gives (11)--(12) with eta=sigma gamma^2 log p/C.
The constant K_s retains its accepted nonnumerical source-constant scope; no numerical value or feasible inversion is claimed.
L168 supplies the earlier qualitative finite-income consequence, but (12) uses the actual current C147v5 interface directly.

At a good prime every e_phi=1, so only a=0 occurs and this distribution is exactly the old complete residue-order inventory.
At a bad prime it retains all d units of layer mass while charging their activation times.
Thus (11) is a genuine extension of the finite criterion to repeated reduction and index primes.
It does not prove that the new covered class is populated by sufficiently-small-positive-measure inputs, nor that its gap consequence is outside all other existing criteria.

<a id="nonreduced-uniform-density-budget"></a>
## 4. Uniform density obstruction, with all primes kept

For fixed C>0 with floor(Cd)>=1 define the complete ORIGINAL budget

    U_C(P)=max_(1<=n<=floor(Cd)) log|D_n|/d.

For every prime p, every selected full-layer set S with W>=gamma d, and every integer 1<=X<=C d, (8)--(9) imply

    delta_X(S)<=K_s [C U_C(P)/(gamma^2 log p)]^s,
    Score_X/W^2<=C U_C(P)/(gamma^2 log p).               (13)

The first bound also covers delta_X=0.
If U_C=0, the norm floor forces H_X(S)=0, so both quantities vanish.
No prime is removed as a discriminant or power-basis-index exception.

When 0<Cm<=exp(-40), C147v5's monotonicity gives the explicit upper bound

    U_C(P)<=Phi_5(Cm),
    Phi_5(h)=86 sqrt(h)[log(1/h)]^(5/2)
                            /[log log(1/h)]^(3/2).      (14)

Every n in the original window has 0<nm/d<=Cm in that domain.
Thus along a hypothetical sequence with m(P)->0, the supremum of the two quantities in (13), over ALL primes p and ALL such layer selections and windows, tends to zero.
The inequality log p>=log 2 makes this uniform in p.
There is no claim that such a nontorsion sequence exists.

This pinpoints the unresolved automatic-coverage obligation.
Small total measure alone gives an upper budget; the new layer construction does not reverse it into positive density.
It enlarges the arithmetic objects that a prospective lower-density mechanism may use, and removes the earlier good-prime exclusion without inventing free repeated-root mass.

<a id="nonreduced-raw-order-failure"></a>
## 5. Exact reciprocal control and the price of repeated reduction

For EVERY integer r>=2 consider the actual polynomial

    P_r(t)=(t-1)^(2r)+2t^r,       d=2r.                 (15)

It is monic reciprocal with constant coefficient 1.
The translate P_r(t+1)=t^(2r)+2(t+1)^r is Eisenstein at 2: all lower coefficients are even, and its constant term is 2, not divisible by 4.
Thus P_r is irreducible over Q and defines an original algebraic integer unit.
Writing x=t+t^(-1) gives P_r(t)=t^r[(x-2)^r+2].
For r>=2 the trace root x=2+2^(1/r)exp(pi i/r) is nonreal, so its corresponding t roots cannot lie on the unit circle.
Consequently P_r is nontorsion, with positive total measure.
No statement that it is Salem is made; it generally has several non-unit-circle pairs.

Modulo 2 one has P_r=(t-1)^d, while the signed original norm at n=1 is exactly

    D_1=Res(P_r,t-1)=P_r(1)=2,
    v_2|D_1|=1.                                        (16)

The sign agrees because d is even.
If its entire multiplicity d were attached to raw residue order 1, raw triple density at X=1 would be 1, but the claimed floor d would be false for every d>1.
This disproves that uncharged repeated-root extension of the old good-prime interpretation on ACTUAL irreducible reciprocal nontorsion inputs.

The correct layer law is completely explicit:

    w_1=1,
    w_(2^a)=min(d,2^a)-min(d,2^(a-1))   (a>=1),
    h_2(n)=min(d,2^v_2(n)).                              (17)

For X>=1 put b=floor(log_2 X).
The eligible positive labels are the powers 2^a with 0<=a<=b that have positive weight, and every triple of those labels has lcm at most X.
Hence the EXACT full-law statistics are

    H_X=min(d,2^b),
    delta_X=[min(d,2^b)/d]^3.                            (18)

For X=1 this is d^(-3), consistent with (16).
For X=2^ceil(log_2 d)<2d, all mass is captured and delta_X=1.
When d is a power of 2, every nonzero weight in (17) equals its full totient capacity, including the terminal level.
For other even d the last weight is the strictly smaller partial increment prescribed in (1).
No original degree is dropped at either endpoint.

These are exact symbolic identities for one family, not a native calculation or a search.
The family does not witness new near-one coverage.
Its entire original degree is in the repeated linear factor at p=2, so the OLD L205 bound with gamma=1,F=1 gives m(P_r)>=log 2/4.
That bound already excludes its total measure tending to zero.
The control is useful precisely because it separates invalid raw-order mass, valid paid layer mass and an independently known old-class positive gap.

<a id="nonreduced-torsion-boundary"></a>
## 6. The torsion boundary still defeats all-prime short coverage

The exact [C144 control](Yin_C_G0144_v1.md#zero-measure-full-window-budget) must also be checked at the newly included bad primes.
Take its odd squarefree N with q_min the smallest prime divisor, d=phi(N), and P=Phi_N.
This input is TORSION and is outside the nontorsion conclusion (12).
For the comparison fix an integer 1<=X<N, so every norm D_n with n<=X is nonzero.

If p does not divide N, Phi_N mod p is separable and all its roots have order N.
The only layer label is N with weight d, hence H_X=delta_X=0.
If p divides N, write M=N/p, with p not dividing M.
The exact integral identity Phi_N(t)Phi_M(t)=Phi_M(t^p) reduces modulo p to

    Phi_N mod p=(Phi_M mod p)^(p-1).

Indeed the p-th roots of primitive M-th roots have orders exactly M or Mp, which proves the integral identity, and coefficientwise Frobenius gives the reduction.
The polynomial Phi_M mod p is separable and all its roots have order M.
Thus (1) has exactly the two positive labels

    w_M=phi(M)=d/(p-1),
    w_N=(p-2)phi(M),                                  (19)

with all other weights zero.
Here p>=3, so both weights are positive; the second is the partially filled terminal level, not a free weight d at M.
As X<N, this gives the exact full-law formulas

    H_X/d=1/(p-1), delta_X=1/(p-1)^3 if M<=X,
    H_X=delta_X=0                         if M>X.       (20)

The actual full local floor is exact at every such short time: v_p|D_n|=h_p(n) for ALL primes p and 1<=n<N.
To check this, C144's complete norm identity is |D_n|=Phi_h(1)^(d/phi(h)), h=N/gcd(N,n)>1.
Because h is squarefree, it gives 1 when h has at least two prime factors, and p^(d/(p-1)) exactly when h=p.
The latter is equivalent to M dividing n with p not dividing n, precisely the nonzero case in (19)--(20).
For p not dividing N both sides vanish.
Thus no omitted deep valuation invalidates the comparison.

On C144's actual sequence q_min->infinity and N/d->infinity, every fixed C>0 eventually has X=floor(Cd)<N.
Equations (19)--(20) give uniformly over EVERY prime

    delta_X<=1/(q_min-1)^3 ->0,
    Score_X/d^2<=C/(q_min-1) ->0.

The second estimate holds for every permitted counting-angle model by (10).
This is the new necessary comparison with the full nonreduced inventory; C144's earlier good-prime zero statement alone did not include (19).
It shows why merely adding all bad primes cannot distinguish these zero-measure controls from a prospective small-positive-measure case.
It is still not a nontorsion counterexample or a proof that the coverage hypothesis below fails.
The global torsion distinction and an original linear-time cost remain essential.

<a id="nonreduced-next-question"></a>
## 7. Discriminating next question and bounded continuation

The changed original-field question is now precise.
Do there exist FIXED C>=1,0<delta<=1 and epsilon>0 such that every actual irreducible reciprocal nontorsion unit P with 0<m(P)<=epsilon admits a prime p for which the FULL law (1), of mass exactly d, satisfies

    delta_(floor(Cd))>=delta?                            (21)

A weaker positive candidate may specify a genuine structural subclass, but must retain the same original norm, degree and physical time.
By (11)--(12), (21) would force a positive gap on that class.
Neither a bounded residue-degree class already covered by L205 nor the bounded pair-field class already covered through L398 should be presented as a new uncovered domain.
There is no assertion that (21) is easier than the corresponding arithmetic gap problem.

The first bounded feasibility test has been completed analytically: construct (1), prove exact capacities and nullity, distinguish it from raw repeated orders through (15)--(18), and retain the complete torsion limitation (19)--(20).
The result is positive for that interface and negative for the uncharged raw-order extension.
No J is needed for these exact formulas.
A next finite test would require a separately declared actual nonreduced input outside that simple bounded-residue-degree control, an exact finite prime/window list and a predeclared question that its factorization can discriminate.
No such numerical list or native run is silently authorized here.

The current source/reuse barriers remain substantive.
C86/C88/C91 and C142's arithmetic application originally assume good primes; their abstract capacity arguments do not identify this nonreduced companion law without (1)--(5).
C147 gives expense after income, not (21).
C146/C162's orbitals and L205's bounded-residue theorem supply their stated covered classes, not automatic high-residue-degree layer density.
C144's torsion controls and C83/C136/C141's different fixed-positive-measure controls are not nontorsion near-one counterexamples to (21).
The nilpotent layer law itself uses more of the reduction than good-prime orders, but no root-geometry or integrality argument forcing its triple density has been established.

<a id="nonreduced-author-check"></a>
## 8. Contribution and source limits

The root subsequently emphasized using the original companion determinant/corank to avoid a false ideal-valuation identification at index primes and checking the same local capacity factors.
Those safeguards agree with the author's (1)--(2); root's input is disclosed rather than treated as independent review.
No original external source proof was newly audited.
C142v2 and C147v5 keep all their declared source and review limits.
The arithmetic question (21) remains open.
No numerical experiment or unrestricted G0001 conclusion is supplied.

<a id="nonreduced-fixed-inputs"></a>
## 9. Exact input and comparison scopes

| Material | Role in this argument |
| --- | --- |
| [C142v2 adopted statement](Yin_C_G0142_v2.md#statement) | Direct dependency: general finite real phi-capacity weak moment and positive-triple capture, with its existing GW21-U002 scope and R804 retained original whole review. No fresh source proof or independent re-review of that theorem is claimed. |
| [C147v5 adopted statement](Yin_C_G0147_v5.md#statement) | Direct dependency: the same full original cyclic logarithmic norm, monotone Phi_5, capped strict inverse H_5 and powered-field multiplicities, at their declared source limits. |
| [C88 finite gap/bucket mechanism](Yin_C_G0088_v1.md#statement) | Credited combinatorial antecedent; the needed counting proof is reproduced completely at (10), with the new layer inventory justified here. Its old good-prime arithmetic scope is not silently enlarged as a premise. |
| [L205 bounded-residue theorem](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Direct dependency only for the old positive gap m(P_r)>=log 2/4 and prior-coverage exclusion of that control. |
| [C144 complete torsion norm account](Yin_C_G0144_v1.md#zero-measure-full-window-budget) | Direct dependency for the actual squarefree sequence and full cyclotomic norm identity; the new bad-prime layer formulas and uniform all-prime comparison are proved here. Its Bel17/L17 scopes remain inherited. |
| [L70 companion Jordan period](Yin_C_G0251_v1.md#scalar-period-jordan-formula), [C50 complete dyadic period](Yin_C_G0050_v1.md#statement) | Earlier exact period and congruence scope; equation (6) is also proved directly from (4), with no new period theorem claimed. |
| [L221 multiplicity-scaled capture](../ledger/Yin_L_G0221_v1.md#local-multiplicity-scaled-depth-capture), [L74 same-time norm aggregation](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Comparison and original-norm conventions; their ideal/ramification arguments are not used in place of the complete companion-nullity proof (4)--(5). |
| [C146v5](Yin_C_G0146_v5.md#statement), [C162](Yin_C_G0162_v1.md#statement), [L398 prior coverage](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Arithmetic strategy comparisons only; no orbit-size, matching-density or auxiliary-field hypothesis is presumed here. |

All new proofs, both exact controls and the remaining coverage question are retained here.
