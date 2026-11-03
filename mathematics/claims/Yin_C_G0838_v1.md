---
author: Yin
---

# Nested finite-core geodesic elimination and bounded supersolution transfer

Human author Yin.
Contributor core_feedback_structure derived the finite-shell word partition, bounded comparison of the geodesic baselines, complete-potential and supersolution transfers, l-infinity criterion and two finite Markov examples.
Root supplied and checked the normalized shell-elimination formulation, the convergence requirement from original words, the generic-example boundary and the spectral argument through bounded potentials.
Contributor original_signed_asymptotic developed the full finite-core block primitive that prompted this nested comparison.
The current adopted assessment is [the whole-reviewed decision](#decision-whole-reviewed-2026-10-28), selecting [whole independent R1058](../audits/reviews/Yin_R_G1058_v1.md#whole-nested-core-finding).
The larger original-core convergence hypothesis and unresolved actual all-state and radius obligations retain their precise scope.

## Statement

Let D={0} union D_0 be countable and P a substochastic kernel with finitely many positive entries in each row.
Assume every nonzero state has a positive-weight finite path to0, write d(x) for the shortest such length with d(0)=0, and assume every level L_j={d=j} is finite.
For each j>=1 put C_j={1<=d<=j} and O_j={d>j}.
Fix integers1<=m<n and one parameter t>0 such that the ORIGINAL matrix geometric series sum_(k>=0)(t P_(C_n,C_n))^k converges.
If O_n is empty, the outside conclusions below are vacuous; otherwise put S=C_n minus C_m and O=O_n.
Use the exact geodesic/nongeodesic classification, convergent finite-core first-hit column u_j, terminal baseline g_j, and complete normalized block kernel T_j defined in the [original-clock definitions](#original-clock-definitions).
Every block includes its full original probability and t raised to its full chronological length, including all internal core detours and every possible exit.

The shell series Z=sum_(k>=0)T_(m,SS)^k converges.
With h=Z1_S, r=1_O+T_(m,OS)h and That=T_(m,OO)+T_(m,OS)Z T_(m,SO), one has

    h=u_n|S/g_m|S,             r=g_n|O/g_m|O,
    T_n=diag(r)^(-1) That diag(r),
    1<=r(x)<=max_(s in L_n)u_n(s)/g_m(s)<infinity.

For the minimal complete first-hit potentials v_j=Hcal_t|O_j/g_j=sum_(k>=0)T_j^k1, allowing infinity,

    v_(m,O)=diag(r)v_n,
    v_(m,S)=h+Z T_(m,SO)diag(r)v_n.

Thus pointwise finiteness on the whole respective exterior, and separately uniform boundedness, are equivalent for the two cores.
At their common exterior states v_n<=v_m.
Every nonnegative pointwise finite supersolution w_n>=1+T_nw_n transfers by these same formulas, with v replaced by w, to w_m>=1+T_mw_m; conversely every such old supersolution gives w_(m,O)/r>=1+T_n(w_(m,O)/r).

The kernel T_m is bounded on l-infinity(O_m) if and only if T_n is bounded on l-infinity(O).
Under these equivalent boundedness conditions,

    rho_(l-infinity)(T_m)<1
                 if and only if rho_(l-infinity)(T_n)<1.

There is no universal ordering of the individual normalized row costs T_j1 under these hypotheses: the [two exact finite Markov examples](#finite-markov-row-counterexamples) have all complete first-hit sums finite at t=1, but respectively change a row from13/10 to17/20 and from1/90 to1/9.
These examples are general finite Markov chains, not the actual quartic digit law.
The statement asserts no numerical ordering of spectral radii, no boundedness from finite row support alone, and no spectral assertion on a different coefficient space.

## Exact inputs, source scope and extraction

The complete general argument below is self-contained under the stated hypotheses.
[C833's actual shortest-word definition and complete decomposition](Yin_C_G0833_v1.md#shortest-first-deviation-definition) supplies the geodesic convention and original-word mechanism motivating the construction; its numerical level obstruction is not an input.
[C590's finite original escape resolvent](Yin_C_G0590_v1.md#finite-original-escape-resolvent) is credited for the reused finite-killing mechanism and the requirement to justify the nonnegative geometric series, rather than infer convergence from invertibility.
The present proof pays that requirement directly from the larger original core hypothesis and the complete shell-word partition.
[C511's complete first-hit convention](Yin_C_G0511_v1.md#prescribed-zero-mass-frontier) supplies only the actual canonical interpretation and separate R/R_f boundary used in the application discussion.
No numerical FC9 premise, general stochastic-complement theorem or newly acquired external source is used, and no novelty claim is made.

The argument was developed at [D9's nested finite-core question](../drafts/Yin_D_G0009.md#nested-finite-core-geodesic-elimination), which is extraction provenance only and supplies no fixed proof dependency.
The entire mathematical argument and both hand calculations are retained here; no J computation or native output is needed for their reproduction.

## Complete argument

<a id="original-clock-definitions"></a>
### Definition: original-clock finite-core block operators

Let D={0} union D_0 be countable, and let P(x,y)>=0 be a finite-row substochastic kernel, so every state has finitely many positive successors and each original row has sum at most one.
Missing mass represents killing and is never renormalized.
Assume every x in D_0 has a positive-weight finite path to0, write d(x) for its shortest such length, and assume each level L_j={x:d(x)=j} is finite.
Put d(0)=0 and Hcal_t(0)=1.
For x!=0, Hcal_t(x) is the sum of p(w)t^|w| over all finite original words first hitting0, with infinity allowed.
No infinite non-hitting path contributes to this sum.
The row at0 is irrelevant to the present first-hit construction.

An original edge x->y with x!=0 satisfies d(y)>=d(x)-1.
Call it geodesic when equality holds and nongeodesic otherwise.
Fix integers1<=m<n and a SINGLE parameter t>0, and assume that the matrix geometric series for t P_(C_n,C_n) converges.
The smaller core series converges by the inclusion of its nonnegative paths.
For j=m,n put O_j={d>j}, and define

    Z_j=sum_(k>=0)(t P_(C_j,C_j))^k,
    u_j=Z_j t P_(C_j,0),
    V_j=Z_j t P_(C_j,O_j).

The column u_j sums every first-hit word that stays in C_j until it reaches0.
The matrix V_j sums every word staying in C_j until its first exit to O_j.
Both retain the full original probability and t raised to the entire chronological length.
Every core state has a geodesic path to0 inside that core, so u_j is strictly positive.

Let A_j be P restricted to geodesic edges with both endpoints in O_j, let A_(j,C) be its geodesic edges from O_j to C_j, and let N_j be P restricted to nongeodesic edges with both endpoints in O_j.
A nongeodesic edge starting in O_j cannot enter C_j.
Write

    E_j=sum_(k>=0)(t A_j)^k,
    U_j=E_j t A_(j,C),
    g_j=u_j on C_j,              g_j=U_j u_j on O_j,
    W_j=E_j t N_j+U_j V_j,
    T_j=diag(g_j|O_j)^(-1) W_j diag(g_j|O_j).

The series E_j is rowwise finite because geodesic distance strictly decreases, and is not a claim about a bounded inverse on a sequence space.
Every g_j(x) is finite and strictly positive.
Every W_j and T_j row has finite support: a geodesic prefix has bounded length at a fixed starting state, original rows have finite support, and the finite core has only finitely many exit targets.
The terminal pieces counted by g_j are a geodesic prefix to C_j followed by any internal core path ending at0 without an exit.
The W_j blocks end at either the first outside nongeodesic edge or the first exit following entry into C_j and arbitrary internal core detours.
The unique complete-word partition therefore gives

    Hcal_t|O_j=g_j+W_j Hcal_t|O_j,
    v_j:=Hcal_t|O_j/g_j=sum_(k>=0)T_j^k 1,

as identities of extended nonnegative sums.
Every normalized block has the original t^length factor and a g_j endpoint ratio, and these endpoint ratios telescope.



<a id="exact-nested-elimination"></a>
### Exact shell elimination and its convergence proof

Put S=C_n minus C_m and O=O_n, so O_m=S union O, and write the blocks of T_m using these two sets.
Assume O is nonempty; otherwise the outside assertions are vacuous and the finite-core first-hit statement already applies on all D_0.
The existence of a shortest path from any state in O makes L_n nonempty.
Define

    Z=sum_(k>=0)T_(m,SS)^k,
    h=Z 1_S,
    r=1_O+T_(m,OS)h,
    That=T_(m,OO)+T_(m,OS)Z T_(m,SO).

Then all finite-shell series converge and

    h(s)=u_n(s)/g_m(s),                     s in S,
    r(x)=g_n(x)/g_m(x),                     x in O,
    T_n=diag(r)^(-1) That diag(r).                     (NC1)

To prove convergence before using the inverse notation, take a first-hit word confined to C_n and starting in S.
Its old m-blocks have endpoints in S until the old terminal piece finishes the word.
A geodesic prefix starting in S cannot leave C_n because distance decreases; the only possible exit of an old block is its final nongeodesic edge or its final exit from C_m.
Thus retaining exactly those old blocks with endpoints in S retains precisely the original words confined to C_n, with no lost or repeated word.
Their normalized nonnegative sum is

    u_n(s)/g_m(s)=sum_(k>=0)(T_(m,SS)^k 1)(s)<infinity. (NC2)

The last inequality follows from the ASSUMED ORIGINAL core convergence and the positive finite g_m(s), not from a formal matrix inverse.
Write h for this sum and H=max_(s in S)h(s), which is finite with H>=1.
Nonnegative summation gives T_(m,SS)h=h-1<=(1-1/H)h.
The positive finite diagonal normalization by h is therefore a strict contraction, proving convergence of the matrix geometric series Z and its equality with(I-T_(m,SS))^(-1).

Starting in O, the n-terminal words consist of an old m-terminal word, or an old block entering S followed by zero or more old blocks ending in S and an old terminal word.
An old block entering S cannot previously have made a nongeodesic edge outside C_n, because that would already have ended the block outside C_n.
This gives g_n/g_m=1+T_(m,OS)h.
An n-block consists either of one old block ending in O, or of an old block entering S, zero or more old blocks ending in S, and an old block exiting to O.
This gives That before changing the normalization, and then the last identity in NC1.
These partitions use actual chronological words, so neither shell elimination nor internal core resummation replaces a visit by one unit of original time.

<a id="bounded-baseline-ratio"></a>
### Uniform comparison of the changed baselines

The ratio r in NC1 satisfies the global estimate

    1<=r(x)<=M_(m,n):=max_(s in L_n)u_n(s)/g_m(s)
                   <infinity,             x in O.     (NC3)

Indeed h>=1 on S by NC2, and both g_m and g_n obey the same original geodesic harmonic equation above level n.
For a geodesic edge before level n, the weights t P(x,y)g_m(y)/g_m(x) sum to one.
Following that auxiliary geodesic law reaches L_n after exactly d(x)-n steps.
The ratio r(x) is its convex average of u_n(s)/g_m(s) at that endpoint, proving NC3.
This auxiliary finite-length law is not the actual critical Q.
In particular the bounded comparison holds for every outside starting state, not only for the finitely many states in a computed profile.

<a id="complete-potential-supersolution-transfer"></a>
### Complete first-hit potentials and supersolution certificates

With v_j=sum_(k>=0)T_j^k 1 as above, the complete word partition gives

    v_(m,O)=diag(r)v_n,
    v_(m,S)=h+Z T_(m,SO)diag(r)v_n,                    (NC4)

allowing infinity.
These are regroupings of finite first-hit words, not uniqueness claims for arbitrary infinite-valued fixed points.
The finite-row condition makes every shell-to-outside sum finite whenever its individual outside values are finite.
Consequently v_m is finite at every state if and only if v_n is finite at every outside state.
By NC3, the finite set S and its finite exit support, v_m is uniformly bounded if and only if v_n is uniformly bounded.
At common outside states, v_n=v_m/r<=v_m, so the complete normalized potential has a valid monotonic comparison even though its first row-cost term need not.

More generally, any nonnegative pointwise finite w_n satisfying w_n>=1+T_n w_n gives an old supersolution through

    w_(m,O)=diag(r)w_n,
    w_(m,S)=h+Z T_(m,SO)diag(r)w_n,
    w_m>=1+T_m w_m.                                   (NC5)

On S this is equality by the definition of Z and h.
On O the right side is r+That diag(r)w_n=diag(r)(1+T_n w_n), which is at most diag(r)w_n.
Conversely, let w_m>=1+T_m w_m be a nonnegative pointwise finite old supersolution.
Iterating its shell inequality and dropping the nonnegative remainder gives w_(m,S)>=h+Z T_(m,SO)w_(m,O).
Substitution in its outside inequality gives w_(m,O)>=r+That w_(m,O), hence w_(m,O)/r>=1+T_n(w_(m,O)/r).
This supplies both directions without presuming that the supersolution is the minimal first-hit potential.
For example, a positive weight w>=1 with T_j w<=q w for q<1 gives the inhomogeneous supersolution w/(1-q), and NC5 transfers it exactly.

<a id="bounded-infinity-spectral-criterion"></a>
### The strictly subunit spectral criterion on l-infinity

Finite row support alone does not assert boundedness on l-infinity.
Here T_m defines a bounded operator on l-infinity(O_m) if and only if T_n defines a bounded operator on l-infinity(O).
To see this, the finite blocks T_(m,SS) and T_(m,SO) are bounded, and T_(m,OS) is bounded because T_(m,OS)1<=T_(m,OS)h=r-1 is uniformly bounded by NC3.
If T_m is bounded, NC1 and NC3 make T_n bounded.
Conversely, bounded T_n makes That=diag(r)T_n diag(r)^(-1) bounded, and positivity gives T_(m,OO)<=That; adding the bounded remaining blocks makes T_m bounded.

When these bounded-operator conditions hold, their spectral radii satisfy exactly

    rho_(l-infinity)(T_m)<1
                 if and only if rho_(l-infinity)(T_n)<1. (NC6)

For any bounded positive kernel T on l-infinity, rho(T)<1 gives norm convergence of sum_k T^k and therefore a uniformly bounded v=sum_k T^k 1.
Conversely, if this potential is uniformly bounded by M, then1<=v<=M and Tv=v-1<=(1-1/M)v.
The weighted sup norm defined by v is equivalent to the ordinary sup norm, and T is a contraction with factor at most1-1/M in that norm.
Thus rho(T)<1.
Apply this equivalence to NC4 and NC3 to obtain NC6.
No spectral radius on a different weighted space, no numerical ordering of the two radii, and no boundedness of a merely row-finite infinite matrix are asserted.
In particular, finite-core enlargement preserves the existence of a strict contraction certificate with a positive weight bounded above and below, while it may change whether the constant weight1 works.

<a id="finite-markov-row-counterexamples"></a>
### Two exact finite Markov examples excluding a generic row order

These examples concern the general kernel setting just stated, not the actual quartic digit law.
They use t=1, an absorbing zero, C_1={z}, and P(z,0)=1.
All unlisted transitions have probability zero, and every displayed nonzero row sums to one.
The distances and rational calculations follow directly from the listed rows and require no native computation or J artifact.

First take states b,a with d(b)=2 and d(a)=3 and rows

    P(b,b)=3/5,    P(b,a)=1/4,    P(b,z)=3/20,
    P(a,a)=3/5,    P(a,b)=2/5.

For m=1, the geodesic baseline is g_1(b)=3/20 and g_1(a)=3/50.
The a row of T_1 has the direct a-loop cost3/5, the cost3/5 of a geodesic step to b followed by a b-loop, and the cost1/10 of a geodesic step to b followed by b->a.
Therefore

    (T_1 1)(a)=3/5+3/5+1/10=13/10>1.

For n=2, the only nonzero eigenvalue of the original killed core on{z,b} is3/5, so its geometric series converges.
It gives u_2(b)=(3/20)/(1-3/5)=3/8 and g_2(a)=(2/5)(3/8)=3/20.
The new outside is the singleton{a}, and its complete feedback cost is

    (T_2 1)(a)=3/5+(2/5)(1/4)/(1-3/5)=17/20<1.

Thus an old violating row can become subunit after genuine core resummation.
The original chain reaches0 almost surely: from either nonzero state a or b there is a fixed positive probability of following a path to0 within three steps, and the finite maximum of the resulting survival probabilities is strictly below one.
All its complete first-hit sums at t=1 are finite.

For the reverse row comparison, take d(b)=d(c)=2 and d(a)=d(x)=3 with

    P(b,b)=9/10,   P(b,z)=1/10,   P(c,z)=1,
    P(a,b)=1,      P(x,c)=9/10,   P(x,a)=1/10.

Now g_1(a)=1/10 and g_1(x)=9/10, while the convergent core{z,b,c} has u_2(b)=u_2(c)=1, giving g_2(a)=1 and g_2(x)=9/10.
The only nongeodesic block from x before its geodesic terminal path is the edge x->a, and neither the c path nor its larger-core continuation adds feedback.
Hence

    (T_1 1)(x)=(1/10)(1/10)/(9/10)=1/90,
    (T_2 1)(x)=(1/10)(1)/(9/10)=1/9.

This row increases after enlargement.
The b self-loop eventually exits almost surely, and every other path reaches that loop or reaches0 directly, so all complete original first-hit sums at t=1 again equal one.
The two examples together disprove either universal ordering of normalized row costs under these hypotheses, including when the full first-hit sums are finite.
They establish no particular row change for the actual quartic.

<a id="actual-quartic-radius-boundary"></a>
## Actual quartic specialization and true-radius limits

For the original quartic q(X)=X^4-X^3-X^2-X+1, use the actual accessible/coaccessible core and original digit probabilities pi_(-1)=pi_1=1/4 and pi_0=1/2 from [C833](Yin_C_G0833_v1.md#statement).
[C590](Yin_C_G0590_v1.md#statement) supplies finite original shortest distances on that actual core.
The finite-level hypothesis follows because a word of bounded length determines its starting state and there are finitely many such words.
These facts verify only the geometric setting of the general statement.
The original killed matrix convergence for any newly chosen larger C_n at the selected t remains a required separate input; no smaller-core certificate or formal inverse supplies it automatically.

Let R be the radius of the complete original return series and R_f the radius of its complete first-return series F.
For this actual rooted law, [C511](Yin_C_G0511_v1.md#prescribed-zero-mass-frontier) identifies Hcal_t with the finite canonical H_t on0<t<R_f.
Outside that interval the word formulas allow infinity and do not infer finiteness of the complete first-hit sums from finite-core convergence.
With the actual row at0 restored, the complete first-return series satisfies

    F(t)=t P(0,0)+t sum_(y!=0)P(0,y)Hcal_t(y),

allowing infinity.
An actual finite pointwise supersolution on the full exterior, together with the convergent finite core and finite original exit rows, makes all first-hit values finite and hence F(t)<infinity.
Indeed iteration bounds the minimal exterior potential by that supersolution, while original core decomposition reconstructs the finitely many core values from their finite exit sums.
If this certificate were obtained at a separately verified t>R, it would imply R_f>=t>R.
No such actual supersolution, larger-core convergence certificate, strict radius gap, finite critical mean, value of R or R_f, or unrestricted G0001 conclusion follows from the elimination identities or the generic finite examples.
An obstruction for a specific old normalized row test cannot be imported unchanged into a different core; a successful enlarged-core supersolution must pay the complete feedback and then transfers exactly as proved here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision nested-core-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:33 |
| status | open |
| reason | Fix the complete general nested-core author theorem and proof NC1--NC6, including original-clock convergence, bounded baseline ratio, finite/infinite potentials, two-way supersolutions, bounded l-infinity criterion and both exact finite Markov row counterexamples. Separate whole review and adoption remain outstanding; actual larger-core convergence and an all-state certificate at t>R are not supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire countable finite-row substochastic setting, finite shortest-distance levels, fixed parameter and larger ORIGINAL core convergence, exact nested normalization, bounded ratio, pointwise/uniform potentials, supersolution transfer, bounded l-infinity strict spectral criterion and both generic counterexamples. |
| argument | [Complete NC1--NC6 argument](#complete-argument) | Full original-clock definitions, unique finite-word partitions, convergence before inversion, finite-level convex averaging, finite/infinite reconstruction, both supersolution directions, explicit coefficient-space proof and both complete rational Markov examples. |
| support | [Actual shortest-word convention](Yin_C_G0833_v1.md#shortest-first-deviation-definition) | Definition and original-word mechanism attribution, and actual quartic setting in the specialization; no numerical level obstruction is invoked. |
| dependency | [Whole-core deterministic termination](Yin_C_G0590_v1.md#statement) | Only finite original shortest distances for the actual quartic specialization; the general theorem assumes finite distances and proves its own convergence implications. |
| support | [Paid finite original resolvent](Yin_C_G0590_v1.md#finite-original-escape-resolvent) | Reused finite-killing mechanism and convergence requirement attribution, not an automatic assertion of convergence at the newly selected t or larger core. |
| dependency | [Canonical first-hit and separate radii](Yin_C_G0511_v1.md#prescribed-zero-mass-frontier) | Actual interior interpretation on0<t<R_f, full first-return convention and separate R/R_f scope; no critical-mean or radius classification is imported. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T20:41 |
| status | proved |
| reason | Root read the complete standalone C838 statement/NC1--NC6 proof and whole independent R1058 finding. Adopt the exact original-clock shell elimination, bounded baseline comparison, complete-potential and two-way supersolution transfer, bounded l-infinity criterion and both finite Markov counterexamples. The larger ORIGINAL core convergence hypothesis, actual all-state certificate and separately verified t>R remain required for the quartic application; no radius or critical-mean classification is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire countable finite-row substochastic setting, finite shortest-distance levels, fixed parameter and larger ORIGINAL core convergence, exact nested normalization, bounded ratio, pointwise/uniform potentials, supersolution transfer, bounded l-infinity strict spectral criterion and both generic counterexamples. |
| argument | [Complete NC1--NC6 argument](#complete-argument) | Full original-clock definitions, unique finite-word partitions, convergence before inversion, finite-level convex averaging, finite/infinite reconstruction, both supersolution directions, explicit coefficient-space proof and both complete rational Markov examples. |
| support | [Actual shortest-word convention](Yin_C_G0833_v1.md#shortest-first-deviation-definition) | Definition and original-word mechanism attribution, and actual quartic setting in the specialization; no numerical level obstruction is invoked. |
| dependency | [Whole-core deterministic termination](Yin_C_G0590_v1.md#statement) | Only finite original shortest distances for the actual quartic specialization; the general theorem assumes finite distances and proves its own convergence implications. |
| support | [Paid finite original resolvent](Yin_C_G0590_v1.md#finite-original-escape-resolvent) | Reused finite-killing mechanism and convergence requirement attribution, not an automatic assertion of convergence at the newly selected t or larger core. |
| dependency | [Canonical first-hit and separate radii](Yin_C_G0511_v1.md#prescribed-zero-mass-frontier) | Actual interior interpretation on0<t<R_f, full first-return convention and separate R/R_f scope; no critical-mean or radius classification is imported. |
| review | [Whole independent nested-core finding](../audits/reviews/Yin_R_G1058_v1.md#whole-nested-core-finding) | Entire fixed statement and self-contained NC1--NC6 argument, both exact finite examples, complete sequence-space/domain hypotheses and each selected actual-model interface; independently reviewed with the original-clock and unresolved-application limits retained. |

