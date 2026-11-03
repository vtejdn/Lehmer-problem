---
author: Yin
---
# Fixed-efficiency row obstruction beyond the efficiency-eight boundary

Date: 2026-10-14T20:18.
Human author Yin.
Root supplies the following substantive candidate for continued algebraic investigation under unchanged G0001.
It is NOT a proved or independently reviewed theorem.

## Responsible candidate and source obligations

For every fixed K>8, try to adapt C109's four-prime star to a common PRIME base whose every selected order has efficiency below K.
The proposed construction needs precise primary-source support for prime-reciprocal divergence in a reduced arithmetic progression, existence of arbitrarily large primes in the needed classes, and primitive roots at odd prime powers.
These are recognized classical inputs to CHECK before using; neither mere infinitude nor an uninspected theorem name supplies the reciprocal-divergence premise.
Existing source records should be reused if adequate.
Retain all source/applicability limits and a complete actual CRT/base argument.

## Root's substantive mechanism to verify

Fix K>8.
Choose three sufficiently large odd primes q1,q2,q3, each3 modulo4, such that gcd(qi-1,qj-1)=2 for distinct i,j and no qi divides qj-1.
A candidate sequential choice takes each new prime congruent to-1 modulo4 times all older primes and odd parts of their predecessors, and larger than the old data.
With suitably checked Dirichlet input this would permit product_i qi/(qi-1) as close to1 as needed.

For every core g=q1^a1 q2^a2 q3^a3 with all ai>=1, these conditions give pairwise gcd of prime-power totients exactly2 and therefore

    lambda(g)=phi(g)/4,
    g/lambda(g)=4 product_i qi/(qi-1),

where lambda here is the exponent of the unit group, not a Salem root.
Verify this exact identity for every exponent, not only a squarefree core.

Choose all external primes r in the reduced class-1 modulo

    M=4 product_i qi product_i oddpart(qi-1),

and above a fixed sufficiently large threshold.
Then v2(r-1)=1 and gcd(lambda(g),r-1)=2 for every such core.
For each FINITE star, choose a common integer base primitive at the actual maximal qi prime powers and at every selected external r, using the odd-prime-power primitive-root theorem and CRT.
A further checked prime-in-progression input should make this base itself a prime without a size bound being claimed.
For every selected b=gr its order would then be

    ord_b(base)=lambda(g)(r-1)/2,
    b/ord_b(base)=8 product_i qi/(qi-1) * r/(r-1)<K.

The anchor's efficiency is4 times the same product.
The base may depend on the finite star.
No assertion about one fixed base across all stars is intended.

Adapt C109's divisor-grid construction to anchor a=(q1q2q3)^E.
For each external prime r, choose exponents u,v in fixed multiples of log r so q1^u q2^v<=r^(2/3), then the least w with D=q1^u q2^v q3^w>=r gives r<=D<q3 r.
With E large enough, every g=a/D retains all three primes.
Neighbors b=ar/D lie below a, have lcm(a,b)=ar, distinct labels, and phi(b) bounded below by a fixed positive multiple of a.
Their number per r should be bounded below by a fixed positive multiple of(log r)^2.
Reciprocal divergence for ONLY the selected progression would then imply unbounded oriented row/N, just as in C109's dyadic contradiction.
All constants can depend on K and the three fixed primes, but not on the growing finite parameter.

This is a proposed failure of a uniform oriented ROW theorem for every efficiency K>8.
It would not refute positive-density capture, an averaged-pair bound or the actual G0001 objective.
Check whether C109's vanishing-density/capture bounds transfer with the different fixed smooth base, and state the actual scope.
An admissible residue-order inventory and a chosen prime do not supply a near-one irreducible polynomial, valuations or small original Mahler cost.

## Continuation ownership

The g_bridge_audit AI is assigned to verify, develop or refute this candidate and may change direction on evidence.
Root supplied the main proof mechanism above and is a contributor.
Develop all substantive reasoning, useful failure and exact finite/source guards here.
No new native program or source-global edit is authorized merely by this assignment; coordinate any needed source registration.
A separate noncontributor must review any resulting whole argument.

<a id="fixed-efficiency-reuse-and-source-inputs"></a>
## Reuse and checked classical inputs

The delegated author read the complete accepted [C109](Yin_C_G0109_v1.md#argument), including its dyadic divergence contradiction, finite grid, capture/triple-density estimates and every-common-base efficiency escape.
The present construction changes the core and the entire external-prime set to remove that last obstruction; it does not transfer C109's unrestricted-prime reciprocal divergence to a progression without a new premise.
C106 supplies the positive efficiency-eight boundary, and C109 supplies the structural counting method.
A bounded local registry/bibliography/ledger screen found Dirichlet-unit and simultaneous-approximation sources, but no existing retained source for the needed progression-prime or prime-power-unit interfaces.
No novelty or exhaustive literature claim is made.

Three primary sources were directly text-read online on2026-10-15:

1. Andrew V. Sutherland, MIT18.785, Fall2021, [Lecture18, dated2021-11-10](https://math.mit.edu/classes/18.785/2021fa/LectureNotes18.pdf),13 pages: Theorem18.1 on p.1 and §18.4 on pp.7–8.
   For each fixed reduced class c modulo M, the inspected character-sum calculation gives sum_(r prime,r=c mod M)r^(-sigma)=log(zeta(sigma))/phi(M)+O_M(1) as real sigma decreases to1.
   This is stronger than mere prime infinitude.
   Only this fixed-modulus divergence interface is used; no asymptotic uniformity in M or prime-counting lower estimate is imported.
2. Sutherland, the same course, [Lecture19, dated2021-11-15](https://math.mit.edu/classes/18.785/2021fa/LectureNotes19.pdf),12 pages: Theorem19.16 and its proof on p.12 establish nonvanishing at1 for every nonprincipal Dirichlet L-function, the stated missing premise in Lecture18.
   The displayed proof reduces through the cyclotomic zeta factorization and analytic class number formula; those general foundational arguments were not newly audited here.
   The classical nonvanishing theorem is accepted at its checked statement/applicability scope, not advertised as an independent whole-source proof review.
3. Keith Conrad, [Prime Powers Units and Finite Subgroups of GL_n(Q)](https://kconrad.math.uconn.edu/blurbs/gradnumthy/primepowerunitsandGLnQ.pdf), undated9-page author notes: Theorem1.1 and its argument on pp.1–2, and TheoremA.6 with its argument on p.8.
   These give cyclicity of the unit group modulo every odd prime power, including exponent1.
   The p-adic auxiliary facts in the prime-power proof are not newly reaudited.
   The exact cyclicity statements are accepted classical inputs.
   No date was inferred from search-engine metadata, and no finite-linear-group theorem from the same notes is used.

The progression reciprocal consequence used here needs no additional Tauberian assertion: if sum_(r=c mod M)1/r were finite, every sum of r^(-sigma),sigma>1, would be bounded by it, contradicting the displayed divergence as sigma decreases to1.
Removing finitely many primes preserves divergence and therefore infinitude above any fixed threshold.
Every modulus used below is fixed before its associated limit, and every residue is explicitly coprime to that modulus.
Source-global intake has been coordinated with root; this author has not edited the bibliography, registry or global source units.
The local mathematical proof below remains separate from those classical theorem interfaces.

Canonical source intake and selected-local-passage readings were completed by root after the author freeze, without changing the mathematical interfaces: [Sut21-U001](../audits/literature/Sut21/Yin_U001.md#sut21-u001), [Sut21b-U001](../audits/literature/Sut21b/Yin_U001.md#sut21b-u001), and [Con26c-U001](../audits/literature/Con26c/Yin_U001.md#con26c-u001).
Acquisition/version facts remain in the registry.
The source units distinguish accepted classical input from new project theorem review.

## Statement

Fix ANY real K>8.
For a prime ell and an integer o>=2 coprime to ell write

    e_ell(o)=o/ord_o(ell),

where ord_o(ell) is the multiplicative order of ell modulo o.
There is no finite constant C(K), independent of ell, such that every integer anchor a>=2 coprime to ell with e_ell(a)<K obeys

    sum_(2<=b<=a, gcd(b,ell)=1,
          e_ell(b)<K, lcm(a,b)<=X)phi(b) <= C(K) X

for all X>=a.
Failure occurs even with a having exactly THREE distinct prime factors and every selected neighbor having exactly FOUR.

More precisely, for every K>8 there are fixed distinct odd primes q1<q2<q3 and a sequence of finite arrays S_m with full integer capacities w_o=phi(o), anchors a_m, integer windows X_m>=a_m and common PRIME bases ell_m>X_m, such that EVERY selected label has e_(ell_m)(o)<K and lies in the anchor's oriented compatible row.
Their total masses satisfy

    W_m>m X_m,
    X_m/W_m ->0,
    H_(X_m)/W_m ->0,
    0<T_(X_m)/W_m^3 ->0.                               (1)

Here H_X is the maximum divisor-captured mass over positive integers n<=X, and T_X is the full ordered compatible triple mass, including repeated labels.
In particular, no uniformly bounded number of divisor sets at times<=X_m covers the whole arrays.
The bases ell_m may depend on the entire finite array; no single fixed base or bound on their size is asserted.

The result refutes a uniform ROW extension for every efficiency cap strictly above8.
It does not refute a mass-averaged pair bound, fixed-positive-density capture or the G0001 gap.
The arrays have vanishing normalized triple density, and no near-one irreducible polynomial, valuations or small full original Mahler cost is constructed.

## Argument

<a id="efficient-core-prime-choice"></a>
### 1. Three fixed large core primes with exact coprimality

Choose an integer B>=3 so large that

    (B/(B-1))^3<K/8.                                  (2)

Choose q1>B prime with q1=-1 modulo4.
Inductively, after q1,...,qj have been chosen, put h_i=(q_i-1)/2 and choose a prime q_(j+1), larger than all prior q_i and B, in the reduced class-1 modulo

    4 product_(i<=j) q_i h_i.                          (3)

The checked Dirichlet input supplies arbitrarily large primes in each class because -1 is coprime to the displayed positive modulus.
The modulus for each selection is fixed once the earlier primes are chosen.

All q_i are3 modulo4, so every h_i is odd.
For i<j, congruence(3) gives q_j-1=-2 modulo h_i and modulo q_i.
Hence gcd(h_i,q_j-1)=1 and q_i does not divide q_j-1.
Also q_j>q_i implies q_j does not divide q_i-1.
Consequently

    gcd(q_i-1,q_j-1)=2,
    gcd(h_i q_i^u,h_j q_j^v)=1
      for every i!=j and all u,v>=0.                  (4)

No assumption about primality of h_i or a special finite list of primes is needed.
Set

    Q=q1 q2 q3,
    alpha=product_i(1-1/q_i),  C_core=1/alpha.

Then C_core<(B/(B-1))^3<K/8 by(2).
All these constants depend only on the chosen K and the fixed primes.

<a id="efficient-core-and-external-orders"></a>
### 2. Carmichael exponent and the restricted external progression

For a core g=product_i q_i^(a_i) with all a_i>=1, the cyclic odd-prime-power unit theorem gives local group exponents

    phi(q_i^(a_i))=2 h_i q_i^(a_i-1).

Their odd parts are pairwise coprime by(4), and all have exactly one factor2.
Their least common multiple is therefore exactly twice the product of their odd parts.
By the Chinese remainder decomposition of the unit group this proves, for EVERY exponent vector,

    lambda(g)=phi(g)/4,
    g/lambda(g)=4 C_core.                              (5)

Here lambda is the exponent of the finite unit group and has no connection with an algebraic expanding root.

Fix

    M=4 product_i q_i h_i,

and choose an integer threshold R_min>max(4,q3) large enough that

    8 C_core R_min/(R_min-1)<K.                        (6)

Let P be the set of primes r>=R_min satisfying r=-1 modulo M.
This is a fixed reduced progression with only finitely many primes removed, so sum_(r in P)1/r diverges.
In particular no r equals any q_i.
For every r in P, v_2(r-1)=1 and the odd part of r-1 is coprime to EVERY q_i h_i: reduction modulo any odd prime factor of that product gives r-1=-2, a nonzero residue.
Thus

    gcd(lambda(g),r-1)=2                               (7)

for every allowed core g, uniformly in all its exponents.
Possible repeated prime factors of M cause no problem; only the prime divisors and the explicit modulo4 condition are needed.

<a id="progression-dyadic-reciprocal-subsequence"></a>
### 3. Reciprocal divergence supplies the needed finite subsequence

Let L(r)=floor(log_2 r), defined equivalently by2^L(r)<=r<2^(L(r)+1), and for integer R>=R_min put

    A(R)=sum_(r in P,r<=R)L(r)^2.

Then A(R)/R is unbounded.
Indeed, if A(R)<=C R for all sufficiently large integer R, the number of P-primes in[2^j,2^(j+1)) would be at most C2^(j+1)/j^2 for all sufficiently large j.
The reciprocal contribution of each such interval would be at most2C/j^2, making sum_(r in P)1/r converge, a contradiction.
Initial intervals contribute only finitely many terms.
This is exactly the dyadic implication needed; mere infinitude would not imply it.

Let e_i be the least positive integer with q_i<=2^(e_i), and set

    kappa=alpha/(18 q3 e1 e2)>0.                       (8)

Starting with R_0=R_min-1, define R_m for m>=1 to be the LEAST integer R>R_(m-1), R>=R_min, for which

    kappa A(R)>m R.                                    (9)

This exists because deleting finitely many arguments leaves an unbounded sequence of ratios.
It is a precise finite definition using integer powers, integer prime tests and rational comparisons; no efficient computation, actual numerical value or native enumeration has been performed.
R_m is strictly increasing and tends to infinity.

<a id="efficient-finite-divisor-grid"></a>
### 4. Full finite stars and all exponent guards

Fix any integer R>=R_min.
Let

    L=floor(log_2 R), E=1+ceil(log_2 R),
    a=Q^E, X=aR.                                      (10)

Thus L>=2, E<=L+2 and2^(E-1)>=R.
For EACH r in P with r<=R take ALL integer pairs

    0<=u<=floor(L(r)/(3e1)),
    0<=v<=floor(L(r)/(3e2)).                            (11)

Let w be the least nonnegative integer satisfying

    D=q1^u q2^v q3^w>=r.

Since

    q1^u q2^v<=2^(e1u+e2v)
                 <=2^(2L(r)/3)<=r^(2/3)<r,

we have w>=1, and minimality gives

    r<=D<q3 r.                                        (12)

Also u,v<=E-1.
Since q3^(E-1)>=2^(E-1)>=R>=r, taking w=E-1 already suffices, so w<=E-1.
Consequently D divides a and

    g=a/D=q1^(E-u)q2^(E-v)q3^(E-w)

retains ALL three core primes with positive exponents.
Define

    b(r,u,v)=r g=ar/D.

The external prime r cannot equal the q_i-smooth integer D, so (12) actually gives D>r and b<a.
Every neighbor has exactly four distinct prime factors.
Further,

    lcm(a,b)=ar<=aR=X.                                 (13)

The labels are distinct: their unique external prime recovers r, and the prime exponents in a r/b then recover u,v,w.
None equals a.

Let S_R contain a and every selected b, with the exact weight phi(o) at each label.
Since phi(g)=alpha g and r>=2,

    phi(b)=alpha(r-1)g
           >alpha a(r-1)/(q3 r)>=alpha a/(2q3).       (14)

The number of pairs in(11) is at least L(r)^2/(9e1e2).
Thus the total selected mass satisfies

    W_R>kappa a A(R).                                  (15)

At R=R_m, equation(9) yields W_R>m aR=mX.
This counts full capacities throughout; there is no normalization by the number of labels or by the size of the external prime set.

<a id="common-prime-base-crt-realization"></a>
### 5. A common PRIME base for the entire finite star

Choose, for each i, a generator c_i of the unit group modulo q_i^E.
Its reduction modulo q_i^j is a generator for EVERY1<=j<=E: reduction is a surjective group homomorphism, and the image of a generator of a cyclic group generates the entire quotient.
Choose also a generator c_r modulo each selected external prime r.

The moduli q1^E,q2^E,q3^E and all selected r are pairwise coprime.
The ordinary Chinese remainder theorem gives a single residue c modulo

    Z=Q^E product_(r in P,r<=R)r

whose components are all these chosen generators.
Every component is a unit, so gcd(c,Z)=1.
The checked prime-in-progression theorem therefore provides a prime ell>X in the reduced class c modulo Z.
This step supplies a prime base, not just a coprime integer.
It gives no upper size bound and is used separately for each finite R.

For the anchor, ell has full order on every prime-power factor, so ord_a(ell)=lambda(a).
For every selected b=gr, reduction to its three core powers and its external prime, together with(5) and(7), gives EXACTLY

    ord_b(ell)=lcm(lambda(g),r-1)=lambda(g)(r-1)/2,
    e_ell(a)=4 C_core<K,
    e_ell(b)=8 C_core r/(r-1)<K.                       (16)

The last strict inequality follows from r>=R_min and(6).
Thus ALL labels of the full finite array, including the anchor, satisfy the same fixed efficiency cap with the same prime base.
Equations(13),(15),(16) prove the asserted failure of every row constant C(K) uniform in the prime base.
A constant allowed to depend on one fixed base is a different proposition; no fixed-base counterfamily is asserted here.

<a id="efficient-star-capture-decay"></a>
### 6. Peak capture still vanishes

Group the neighbors by their external prime r and let V_r be the total mass of the group.
Each label is below a and each pair count in(11) is at most(L+1)^2.
Therefore

    V_r<=a(L+1)^2,  phi(a)<=a.                         (17)

Let e_Q be the least positive integer with Q<=2^(e_Q), and put C_H=2(e_Q+1).
For n<=X, any captured neighbor's external prime must divide n, so at most log_2 X different groups can be captured.
From(10),

    log_2 X<=e_Q(L+2)+(L+1)
                 <=(e_Q+1)(L+2)<=C_H L,

because L>=2.
Consequently

    H_X<=a[1+C_H L(L+1)^2].                            (18)

Along the exact sequence R_m,

    X/W_R<1/m,
    H_X/W_R<[1+C_H L(L+1)^2]/(mR) ->0.                (19)

Only fixed constants depend on K and the core primes.
The limit uses R_m->infinity and(log R)^3/R->0.
A union of k divisor sets at times<=X captures at most kH_X, so complete covers require k>=W_R/H_X, which tends to infinity despite the fixed efficiency cap.

<a id="efficient-star-triple-density-decay"></a>
### 7. Every compatible triple is counted, and density tends to zero

Let T_X=sum_(o1,o2,o3 in S_R,lcm(o1,o2,o3)<=X)phi(o1)phi(o2)phi(o3), with ordered triples and repetitions.
The repeated anchor gives T_X>0.

The total weight of triples with an anchor coordinate is at most3aW_R^2.
Triples with two neighbors sharing an external prime have total weight at most

    3W_R sum_r V_r^2<=3a(L+1)^2 W_R^2.                (20)

For the remaining triples the three external primes r1,r2,r3 are distinct and absent from all cores.
By(12), each core exceeds a/(q3 R), and

    lcm(b1,b2,b3)=r1 r2 r3 lcm(g1,g2,g3).

If all external primes exceeded Y=(q3 R^2)^(1/3), this lcm would exceed q3R^2*a/(q3R)=X.
Thus every remaining compatible triple has some r<=Y.
There are at most Y such positive integer candidates, so their group mass is at most

    Y a(L+1)^2<=q3 a R^(2/3)(L+1)^2.

Triples with a coordinate in those groups have mass at most three times this expression times W_R^2.
The union of these three classes covers EVERY compatible triple; multiple counting only enlarges the upper bound.
Therefore

    0<T_X/W_R^3
      <=[3a+3a(L+1)^2(1+q3R^(2/3))]/W_R
      <[3+3(L+1)^2(1+q3R^(2/3))]/(mR) ->0             (21)

along R=R_m.
This proves all parts of(1).
The bound applies to the original full array with its same prime base, weights and time window.

<a id="fixed-efficiency-method-boundary"></a>
## Consequences and limits

C106's positive row theorem at efficiency at most8, together with the present failure for every K>8, identifies an exact efficiency threshold for a row bound UNIFORM in the common prime base.
An improvement beyond8 cannot come from proving the same whole-row inequality with a larger K-dependent constant.
The root-supplied progression modification is essential: C109's unrestricted external primes force efficiency escape, whereas every label here has controlled efficiency at the common prime chosen for its finite star.

The same construction still loses normalized triple density.
Hence a genuine fixed-positive-density localization, a mass-averaged pair estimate or an argument using additional structure of actual irreducible inputs remains logically possible.
No mass-averaged pair divergence is proved by this heavy row.
The subgroup orders and prime bases are actual, but no near-one irreducible polynomial, original root partition with good-prime valuations, small auxiliary coefficient norm or affordable full Mahler cost has been supplied.
In particular the uncontrolled size of the CRT prime cannot silently be treated as a free bounded parameter.

This round used no native program, numerical prime search or new J.
Root is a substantive contributor through the initial core/progression/CRT mechanism.
The delegated author verified it, supplied exact finite choices, complete all-exponent and common-base arguments, checked/accepted the classical source interfaces, and extended the full capture/triple accounting with explicit constants.
Neither contributor can supply an independent whole review.
The accepted external inputs are restricted to the checked statements above; original proof foundations outside the inspected passages remain outside the claimed audit depth.

<a id="fixed-efficiency-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T20:24.
The complete original is author-checked and frozen for fixed retention and a separately organized noncontributor whole review: original substantive root mechanism; exact primary-source statements and actual inspection/acceptance depth; Statement; Argument Sections1–7/equations1–21; prime choices and every-exponent gcd/lambda identities; fixed external progression reciprocal divergence; all finite grid guards and distinct/full capacities; simultaneous primitive residues and a single PRIME base for each complete finite star; original capture and full repeated-label triple-density limits; and the exact uniform-base, averaged-pair, fixed-density and near-one boundaries.
A scoped material check returned checked1 and supplies no independent mathematical acceptance.
No native program or experiment was needed.
Canonical source-intake links may be attached after root returns the registered identities, without changing these inspected mathematical interfaces or claiming a broader source audit.

## Fixed organization

The entire author-frozen original above is retained, including the substantive original root proposal, complete developed argument, exact classical inputs and subsequent canonical source locators, all finite and density costs, contribution accounts and unsuccessful implications.
Direct retention is not acceptance.
Root and the delegated algebraic author contributed the proof; another reviewer must inspect this entire actual fixed artifact.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-15)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:29 |
| status | open |
| reason | Retain the complete fixed-efficiency K>8 uniform-common-prime-base row obstruction for actual whole independent review. Positive-density, averaged-pair, fixed-base and actual near-one polynomial conclusions remain unproved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every K>8, no uniform-in-prime-base row constant, with complete capture and triple-density decay and all common-base/near-one restrictions. |
| argument | [Entire argument](#argument) | All finite arithmetic choices, progression divergence, exponent grid, CRT primitive residues, prime-base selection and repeated-triple accounting. |
| dependency | [Support and efficiency predecessor](Yin_C_G0109_v1.md#argument) | Adopted star/counting mechanism; the new progression/core/CRT proof separately supplies bounded efficiency. |
| dependency | [Efficiency-eight positive boundary](Yin_C_G0106_v1.md#statement) | Adopted whole-row upper bound at efficiency at most8; exact method-threshold comparison only. |
| dependency | [Progression divergence](../audits/literature/Sut21/Yin_U001.md#sut21-u001) | Exact accepted fixed-modulus classical interface and elementary reciprocal consequence, no effectiveness or uniform-modulus claim. |
| dependency | [Nonvanishing premise](../audits/literature/Sut21b/Yin_U001.md#sut21b-u001) | Accepted nonprincipal Dirichlet L-function nonvanishing at1, with foundational proof-inspection limits explicit. |
| dependency | [Odd-prime-power cyclic units](../audits/literature/Con26c/Yin_U001.md#con26c-u001) | Exact accepted classical interface for each actual finite local modulus. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:35 |
| status | proved |
| reason | Adopt the complete independent R348 review of the actual K>8 construction and all source/predecessor interfaces. Together with C106, efficiency8 is the exact threshold for this row method uniform in the common prime base. The full constructed arrays have vanishing triple density and changing unbounded prime bases; no averaged-pair failure, fixed-base counterfamily or original near-one realization is implied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every K>8, no uniform-in-prime-base row constant, with complete capture and triple-density decay and all common-base/near-one restrictions. |
| argument | [Entire argument](#argument) | All finite arithmetic choices, progression divergence, exponent grid, CRT primitive residues, prime-base selection and repeated-triple accounting. |
| dependency | [Support and efficiency predecessor](Yin_C_G0109_v1.md#argument) | Adopted star/counting mechanism; the new progression/core/CRT proof separately supplies bounded efficiency. |
| dependency | [Efficiency-eight positive boundary](Yin_C_G0106_v1.md#statement) | Adopted whole-row upper bound at efficiency at most8; exact method-threshold comparison only. |
| dependency | [Progression divergence](../audits/literature/Sut21/Yin_U001.md#sut21-u001) | Exact accepted fixed-modulus classical interface and elementary reciprocal consequence, no effectiveness or uniform-modulus claim. |
| dependency | [Nonvanishing premise](../audits/literature/Sut21b/Yin_U001.md#sut21b-u001) | Accepted nonprincipal Dirichlet L-function nonvanishing at1, with foundational proof-inspection limits explicit. |
| dependency | [Odd-prime-power cyclic units](../audits/literature/Con26c/Yin_U001.md#con26c-u001) | Exact accepted classical interface for each actual finite local modulus. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0348_v1.md#fixed-efficiency-row-actual-whole-independent-finding) | Entire actual statement and argument, all direct input interfaces and source/contribution limits; no unrestricted Task completion. |

