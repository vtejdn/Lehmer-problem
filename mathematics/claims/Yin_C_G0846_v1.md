---
author: Yin
---

# Actual distance-eight boundary communication and complete diagonal transfer

Human author Yin.
Contributor jt26_source_check obtained and directly verified the finite boundary relation, complete local rows, positive words and native certificates.
Root identified the complete forced-first-step diagonal comparison and supplied the finite Laurent/uniform-constant formulation; both are proof contributors.
Contributor dns17_interface supplied the bounded static author-side check described below, not a whole independent review.
This project deduction is [adopted at its whole conditional scope](#decision-whole-reviewed-2026-10-28), through [whole independent mathematical/native R1066](../audits/reviews/Yin_R_G1066_v1.md#whole-distance-eight-boundary-finding).
The [D9 source section](../drafts/Yin_D_G0009.md#distance-eight-existing-boundary-channels) supplies extraction provenance only; the entire necessary proof is fixed here, with native witnesses retained in J52.

## Statement

Use the actual quartic q(X)=X^4-X^3-X^2-X+1, exterior real root beta>1, O=Z[beta], original strict-strip core D, and original affine law x->beta*x+e with probabilities1/4,1/2,1/4 for e=-1,0,1.
Let d(x) be the shortest original legal word length from x to0, and put K={x in D:d(x)<=8}, including0, G=D minus K, and B_K equal to the original kernel killed on leaving G, without row renormalization.
Use the complete boundary A=U union V, first-positive-A-return matrix Lambda, exterior Green matrix Gamma and complete deleted-diagonal series D_K from the [exact conventions](#adopted-conventions).
All IDs mean the exact ascending integral tuples in the [boundary table](#actual-domain-and-complete-boundary) and declared J52 input; they impose no unproved distance or graph-completeness assumption.
The entire result is as follows.

1. K has47 states; U={51,52,59,68,72,75,82,85,88,105}, V={47,...,56}, and A has18 states.
   The true FULL-exterior mutual-reachability classes restricted to A are I={47,48,49,50,53,54,55,56,75,82} and eight singleton classes.
   This does not enumerate all vertices in the exterior class containing I.
2. The positive support of Lambda is exactly I times I, S_0 times I with S_0={72,85,88,105}, and(59,51),(68,52):142 positive and182 identically zero entries.
   The two exceptional positive entries, also equal to their Gamma entries, are t/4.
   The full Gamma reachability relation has150 positive pairs including empty identities and174 zero entries; all eight singleton diagonal Gamma entries equal1.
3. DC2--DC4 retain the eight complete special successor rows, complete predecessor exclusions and all necessary positive words.
   Every outside first step from S_0 enters one of{61,66,74,83,113,122}, all in I's true exterior class by twelve explicit anchor connectors.
   The60 first-edge/destination transfer terms retain complete original chronological probabilities and closing words.
4. For EVERY t>0, D_K(t)<infinity implies all18-by18 boundary Gamma entries are finite, with

       max_(u,v in A)Gamma_uv(t)<=H_8(t)(1+D_K(t)).

   The exact finite Laurent H_8 is defined in [DC5](#boundary-connector-majorant).
   On1<=t<=2, the stated single finite rational C_8 is obtained from the saved connector weights without needing numerical optimization.
5. If an actual t_*>R satisfies D_K(t_*)<infinity, then R_f>R, the actual critical first-return law has a positive exponential moment, and its mean is finite.
   Equivalently alpha=limsup_n d_n(K)^(1/n)<1/R is sufficient, where d_n(K)=sum_(x in G)B_K^n(x,x).
   No bound on alpha or D_K, unconditional radius/mean classification, or general inequality R_f>=1/alpha is asserted.

The finite certificates use only417 supplied states, exact local three-digit predecessor/successor tests and explicit original words, with combined16MiB input and120-second runtime limits for each program.
Complete K/level9 uses its exact accepted scope; full depth24 or417-state BFS completeness is not a premise.
Legal outside-list tuples remain unknown, are never searched and are never treated as killed.

<a id="adopted-conventions"></a>
## Definitions and exact adopted inputs

**Definitions and conventions.**
Use [C833's shortest-word definition](Yin_C_G0833_v1.md#shortest-first-deviation-definition), with d(0)=0, and [C841's excursion definition](Yin_C_G0841_v1.md#finite-boundary-excursion-matrix) and [whole-exterior component convention](Yin_C_G0841_v1.md#finite-boundary-condensation-criterion), specialized only to this K.
Explicitly, U is all exterior successors of K, V all exterior predecessors of K, and A=U union V.
Lambda_uv(t) sums original probabilities times t to the original length over positive G paths u->v with no intermediate A state.
Gamma_uv(t)=sum_(n>=0)t^n B_K^n(u,v) includes the empty identity.
D_K(t)=sum_(n>=1)t^n sum_(x in G)B_K^n(x,x) includes ALL actual exterior states and excludes the infinite length-zero trace.
All series are nonnegative extended sums before convergence is proved.
Boundary communication means existence of positive original G paths, allowing intermediate A visits; it is not induced finite-graph communication.
R and R_f are the true complete-return and first-positive-return radii of the same original law.

[Adopted C785](Yin_C_G0785_v1.md#decision-whole-reviewed-2026-10-26) supplies the actual quartic coordinates, strict-strip core and original probabilities used by every local test.
[Adopted C833](Yin_C_G0833_v1.md#decision-whole-reviewed-2026-10-28) and [its R1053 native finding](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) supply the accepted complete57 states through distance9 and required exact target checks at their declared scope.
Only that complete finite core/level input is reused; the old full depth24 calculation and author core-resummation verifier are not promoted to independent evidence.
[Adopted C841](Yin_C_G0841_v1.md#decision-whole-reviewed-2026-10-28) supplies the boundary-series conventions, connector comparison and paid conditional near-R finite coupling, with its actual recurrence and positive first-hit premises unchanged.
This extraction adds the actual K8 crossing proof and supplies no diagonal estimate.
No prior review covers this new whole statement or native calculation.

## Complete argument

<a id="actual-domain-and-complete-boundary"></a>
### DC1. Actual domain, complete core and complete boundary

Use the unchanged quartic q(X)=X^4-X^3-X^2-X+1 and its real root beta>1.
In ascending integral coordinates x=(a,b,c,d), the original transition and its unique predecessor for a chosen digit e are

    T_e(a,b,c,d)=(-d+e,a+d,b+d,c+d),
    T_e^(-1)(a,b,c,d)=(a+b-e,a+c-e,a+d-e,e-a).

The actual strict strip is |x_+|<B, |x_-|<S, with B=beta^3-beta-2 and S=beta^3-beta-1.
An original digit e=-1,0,1 has probability1/4,1/2,1/4 respectively; leaving this strict strip is killing, with no row renormalization.
The accepted complete distance-through9 scope from [R1053](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) supplies exactly57 states through9 and47 through8, identified as IDs0--46 in the saved J52 shortest-hit input.
The full417-state depth24 calculation is only a supplied finite list here; its global completeness and all its distances are not needed or newly independently accepted.

For each of the47 actual K states, the new programs check all three T_e and all three T_e^(-1) candidates in the strict strip.
Every allowed candidate in these94 complete local rows lies in the supplied list.
Consequently the actual outgoing and incoming exterior boundaries are exactly

    U={51,52,59,68,72,75,82,85,88,105},
    V={47,48,49,50,51,52,53,54,55,56},
    A=U union V.                                      (DC1)

This proves the whole18-state A without a depth24 completeness assumption.
Also V is exactly the complete distance9 level: an outside predecessor of K has distance at most9 and at least9, while a shortest word from every distance9 state next visits distance8.
IDs are fixed by shortest_first_hit_24.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_24.json`), and their actual boundary tuples are as follows.

| ID | Ascending integral tuple | ID | Ascending integral tuple |
| --- | --- | --- | --- |
| 47 | (-2,-1,3,-1) | 48 | (-1,-3,2,0) |
| 49 | (-1,0,-3,2) | 50 | (0,-2,3,-1) |
| 51 | (0,-1,2,-1) | 52 | (0,1,-2,1) |
| 53 | (0,2,-3,1) | 54 | (1,0,3,-2) |
| 55 | (1,3,-2,0) | 56 | (2,1,-3,1) |
| 59 | (-2,1,-2,1) | 68 | (2,-1,2,-1) |
| 72 | (-2,2,1,-1) | 75 | (-1,3,0,-1) |
| 82 | (1,-3,0,1) | 85 | (2,-2,-1,1) |
| 88 | (-2,0,2,-1) | 105 | (2,0,-2,1) |

<a id="complete-local-rows-and-boundary-communication"></a>
### DC2. Complete local exclusion and positive communication

Let G=D minus K and B_K be the original kernel killed on leaving G.
Write I={47,48,49,50,53,54,55,56,75,82} and S_0={72,85,88,105}.
The following are complete ORIGINAL successor rows for the other eight boundary states; a killed entry means the strict-strip test fails, while a target in K is killed only by B_K.

| Starting ID | Digit -1, weight1/4 | Digit0, weight1/2 | Digit+1, weight1/4 |
| --- | --- | --- | --- |
| 51 | killed | killed | 45 in K |
| 52 | 36 in K | killed | killed |
| 59 | killed | killed | 51 |
| 68 | 52 | killed | killed |
| 72 | killed | 122 | 66 |
| 85 | 61 | 113 | killed |
| 88 | killed | killed | 83 |
| 105 | 74 | killed | killed |

The complete predecessor tests show that59,68 and every u in S_0 have no predecessor in G.
State51 has exactly the G predecessor59, with digit+1, and52 has exactly the G predecessor68, with digit-1.
All other allowed predecessors of these eight states lie in K.
The author checker result (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_check.json`), field core_and_boundary_local_certificates, retains every tested tuple, digit, original weight, legal verdict, supplied ID and four exact rational strip-margin intervals for all65 states in K union A.
These finite local exclusions hold in the full actual exterior, regardless of any unknown distant vertices.

The producer result (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_existing.json`), fields first_A_channels and positive_boundary_words, supplies positive original digit words for every ordered pair in I times I and S_0 times I.
First-A words have positive length, stay in G and have no intermediate A vertex.
The author checker reconstructs every integer step, checks every strict-strip membership and K avoidance, and multiplies the complete original chronological probability.
Thus I lies in one true exterior communicating class.
The predecessor exclusions prevent any exterior path entering59,68 or S_0; the successor rows stop paths at51 or52, and entering these two sinks from anywhere else would require their excluded source59 or68.
It follows that the equivalence classes on A induced by true full-exterior mutual reachability are precisely

    I, {51}, {52}, {59}, {68}, {72}, {85}, {88}, {105}. (DC2)

The only interclass reachability directions are59->51,68->52 and each u in S_0 to every v in I.
This is a complete classification on the finite boundary A, not an enumeration of all vertices in its possibly infinite exterior communicating classes.
It proves150 ordered reachability pairs including the18 empty-word identities and174 impossible ordered pairs.
Absence in the finite induced graph is never used as an actual nonreachability argument.

<a id="complete-first-boundary-channel-support"></a>
### DC3. First-boundary-return channels

Use C841's original-clock Lambda_uv(t), counting positive G paths from u to v with no intermediate A, and Gamma_uv(t)=sum_(n>=0)t^n B_K^n(u,v).
The complete support of Lambda on A times A is I times I, S_0 times I and the two pairs(59,51),(68,52).
There are142 positive and182 identically zero channels.
The complete local rows give

    Lambda_59,51(t)=Gamma_59,51(t)=t/4,
    Lambda_68,52(t)=Gamma_68,52(t)=t/4.                 (DC3)

Each of the eight singleton diagonal Green entries is1 and its positive diagonal coefficients vanish.
The closed forward/backward first-A searches certify184 channels with empty allowable interior: the182 zero series and the two polynomials in DC3.
The remaining140 positive first-A channels are not asserted to have bounded length or a finite closed searched domain.
They are instead bounded conditionally by the diagonal transfer in DC5.

<a id="forced-successors-and-connector-words"></a>
### DC4. All forced first-step targets and complete connectors

Every G successor of S_0 is one of

    61=(-2,3,-1,0),    66=(2,-3,1,0),
    74=(-2,3,1,-1),    83=(2,-3,-1,1),
    113=(-1,3,-1,0),   122=(1,-3,1,0).                  (DC4)

All six are in the same true exterior communicating class as I.
For example, anchor47 has the following actual positive digit words in both directions; each word stays in G and the displayed weights are the full original word probabilities.
The symbols -,0,+ denote digits-1,0,+1.

| Target z | Word47 to z | Weight | Word z to47 | Weight |
| --- | --- | --- | --- | --- |
| 61 | 00 | 1/4 | -+0+-+--- | 1/131072 |
| 66 | 0-+0+0 | 1/512 | +0--- | 1/512 |
| 74 | 00000 | 1/32 | -0-----0- | 1/65536 |
| 83 | 0-+00+++- | 1/32768 | +++-+-+--- | 1/1048576 |
| 113 | 0+ | 1/8 | ----+-00+--- | 1/4194304 |
| 122 | 0-+0+- | 1/1024 | +++0++-+-+--- | 1/33554432 |

The full integer digit arrays and intermediate ID sequences are retained in forced_first_step.connector_words in the producer result.
For every v in I and every required target z, concatenate the saved v->47 word with the saved47->z word.
Let its positive weight be c_vz and its chronological length ell_vz.
All60 required terms, one per actual outside first edge from S_0 and target v in I, are retained separately in forced_first_step.transfer_terms with that edge's digit and weight and the full closing word.
The longest of these closing words has21 steps.
The checker verifies all terms and that no actual outside successor has been omitted.

<a id="forced-first-step-diagonal-transfer"></a>
### DC5. Exact forced-first-step diagonal bound

Let d_n(K)=sum_(x in G)B_K^n(x,x) for n>=1 and D_K(t)=sum_(n>=1)t^n d_n(K), as in C841.
This sum includes every actual exterior state, including the six nonboundary targets in DC4.
Fix t>0 and suppose D_K(t)<infinity.
For z as above and v in I, appending the chosen v->z closing word to any length-m G path from z to v gives a distinct original closed path at z with the same prefix.
All weights are nonnegative and chronological, so for m>=0

    c_vz B_K^m(z,v)<=B_K^(m+ell_vz)(z,z),
    Gamma_zv(t)<=(1+D_K(t))/(c_vz t^ell_vz).            (DC5)

The harmless1 permits a zero-length connector when the general comparison is used within I; the saved connectors to DC4 have positive length.
This follows by summing the first inequality after multiplication by t^m and bounding the shifted diagonal subseries by1+D_K(t).

For u in S_0 the complete DC2 row, rather than one selected edge, gives the exact identity

    Gamma_uv(t)=t sum_(z in Z_u) P_D(u,z)Gamma_zv(t),
    Gamma_uv(t)<=t(1+D_K(t))
                    sum_(z in Z_u)P_D(u,z)/(c_vz t^ell_vz)<infinity,
                              u in S_0, v in I,       (DC6)

where Z_72={122,66}, Z_85={61,113}, Z_88={83}, Z_105={74} and all first-edge probabilities are those in DC2.
The identity follows by partitioning every positive-length path at its first step; u differs from every v in I, so the zero-length coefficient is zero.
In particular Lambda_uv(t)<=Gamma_uv(t) pays every one of the40 source-to-I first-A channels.
C841's same-class connector comparison pays all I times I Green entries using the verified positive words in DC2.
DC3 pays the two other crossing channels, all remaining off-diagonal entries vanish, and the eight singleton diagonals equal1.
Thus, for this ACTUAL K={d<=8},

    D_K(t)<infinity
        ==> Gamma_uv(t)<infinity for every u,v in A.   (DC7)

No enlargement of A or exhaustive enumeration of the communicating class is necessary.
All42 nonzero cross-component first-A channels have been paid; the condition is the complete actual diagonal sum, not a diagonal truncation or a sum only over A.

<a id="boundary-connector-majorant"></a>
**Definition (finite boundary connector majorant).**
The following function uses these actual finite boundary sets and specified positive words, with parameter t>0.
It is a project-specific finite construction, not a new meaning of C841's Green or excursion matrices.
For u,v in I, let c_uv and ell_uv be the weight and length of the saved closing word v->u, allowing the empty identity when u=v.
Define

    H_8(t)=max{1,t/4,
         max_(u,v in I)1/(c_uv t^ell_uv),
         max_(u in S_0,v in I)
                 sum_(z in Z_u)P_D(u,z)t^(1-ell_vz)/c_vz}.

Then max_(u,v in A)Gamma_uv(t)<=H_8(t)(1+D_K(t)) for every t>0 with D_K(t)<infinity.
Every coefficient and exponent in H_8 is retained by the positive_boundary_words and forced_first_step.transfer_terms fields.
For1<=t<=2, all forced closing lengths are positive and the internal closing lengths are nonnegative, so one may replace t/4 by1/2 and every t^(1-ell_vz) or t^(-ell_uv) by1.
This gives a single finite rational constant C_8 for that interval, for example the maximum of3/2 and the resulting finite coefficient sums and internal inverse weights.
No optimized or numerically evaluated value of C_8 is needed for DC7, and this finite factor supplies no bound on D_K itself.

<a id="conditional-critical-consequence"></a>
### DC6. Conditional critical consequence and remaining obligation

If an actual t_*>R with D_K(t_*)<infinity is supplied, DC7 and [C841's paid finite-coupling argument](Yin_C_G0841_v1.md#conditional-critical-radius-transfer) imply R_f>R, a positive exponential moment of the actual critical first-return law and finite critical mean.
Equivalently, with alpha=limsup_(n->infinity)d_n(K)^(1/n), the strict inequality alpha<1/R suffices by choosing R<t_*<1/alpha, with the usual infinite endpoint when alpha=0.
This removes the separate acyclic-crossing convergence obligation for this particular distance-eight core.
It does not establish the remaining diagonal inequality or give an unconditional radius or mean classification.
The finite coupling inside K is paid only near R by C841; a pole from repeated finite-core excursions may occur below1/alpha.
Consequently no assertion R_f>=1/alpha or convergence of F at every t<1/alpha is made.
The [earlier FC1--FC9 obstruction](../drafts/Yin_D_G0009.md#finite-core-resummed-geodesic-test) concerns a different normalized row test and remains unchanged; it is comparison context, not a premise here.

<a id="native-certificate-and-author-verification"></a>
### DC7. Native evidence and exact scope

The completed producer and distinct exact author checker use only the417 saved vertices, with combined input cap16MiB and runtime cap120 seconds each.
The latter imports only generic exact polynomial and interval helpers, independently implements the producer's local transition checks using polynomial multiplication/reduction, and reconstructs closed domains with depth-first searches and the boundary relation with Boolean matrix closure.
It remains AUTHOR verification because the current contributor developed this mathematics and code; distinct code does not supply an independent R.
Contributor dns17_interface additionally read both programs and the saved results for local closure, counts and transfer-word orientation, without rerunning them or auditing the accepted helper/core inputs.
That bounded static author-side check found no concrete defect and is not a whole independent mathematical/native review.
Both programs check all1251 successor and1251 predecessor candidates, and the checker retains390 complete local candidate certificates for K union A.
The rational root bracket in its output is obtained from43/25<beta<173/100 by60 bisections with endpoint signs and a positive derivative bound; all four margin intervals are resolved exactly, including strict exclusion of zero margins.
All648 saved word occurrences are checked; the largest length is28, and all60 forced-first-step transfer terms are covered.

The76 legal forward and52 legal predecessor edges leaving the supplied list remain explicitly UNKNOWN frontier tuples in the producer result.
They are never enqueued as graph vertices or silently treated as killed.
The verified boundary exclusions use complete local rows or complete finite forward/backward first-A closure; no conclusion depends on arbitrary full depth24 distances, a graph-size extrapolation or finite induced nonreachability.
No new state, larger radius, height, word-time graph generation or parameter grid was used.
Root completed a whole author-side reading of DC1--DC7, both new programs, their directly used strict-strip/polynomial helpers and the saved native evidence before this extraction.
This supplies no independent review of a proof to which root contributed.
[Whole independent mathematical/native R1066](../audits/reviews/Yin_R_G1066_v1.md#whole-distance-eight-boundary-finding) subsequently covered the complete fixed argument and reproduced both unchanged programs with equality of both entire outputs; the [selected decision](#decision-whole-reviewed-2026-10-28) adopts that scope.
The actual complete diagonal estimate remains the next mathematical input.

### Exact native input and witness bindings

All native files below belong to the existing [J52 group](../computations/programs/Yin_J_G0052/readme.md#distance-eight-existing-boundary-channels), which remains the responsible home for the complete tuples, digit arrays and exact rational certificates.
The fixed proof uses these actual fields and coverage rather than a copied JSON payload.

| Exact file | Selected scope and role |
| --- | --- |
| shortest_first_hit_24.json (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_24.json`) |417 distinct supplied tuples, ID map and saved original successor rows; no whole distance24 completeness premise. |
| geodesic_level9_check.json (`mathematics/computations/outputs/Yin_J_G0052/geodesic_level9_check.json`) | Previously accepted complete57 states through9 and required target checks, determining the actual47-state K. |
| finite_core_resummation_8.json (`mathematics/computations/outputs/Yin_J_G0052/finite_core_resummation_8.json`) | Only core_states and exit_targets compared with the newly checked local rows; no inverse matrix, normalized row cost or asymptotic premise. |
| [boundary_channels_existing.py](../computations/programs/Yin_J_G0052/boundary_channels_existing.py) | Whole bounded producer; imports only StrictCore from shortest_first_hit.py and never invokes its BFS. |
| [verify_boundary_channels_existing.py](../computations/programs/Yin_J_G0052/verify_boundary_channels_existing.py) | Whole distinct AUTHOR checker using verify_shortest_witness.py's generic polynomial/interval helpers, without producer search imports or new graph generation. |
| boundary_channels_8_existing.json (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_existing.json`) | Complete A,65 local row pairs,36 search domains/frontiers,324 first_A_channels,150 positive_boundary_words, exact exclusions and forced_first_step's complete rows/twelve connectors/60 transfer terms. |
| boundary_channels_8_check.json (`mathematics/computations/outputs/Yin_J_G0052/boundary_channels_8_check.json`) | Passed exact verification, root interval,390 complete local candidate certificates with four margin intervals,648 checked word occurrences,60 transfer terms and no unpaid crossing. |

The producer reads the first three JSON inputs; the checker adds the producer result as its fourth input.
Each invocation enforces combined16MiB input,417 supplied vertices and a120-second guard, without enlarging the searched set.
The completed reproduction commands, from the repository root in this order, were

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/boundary_channels_existing.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0052/verify_boundary_channels_existing.py
```

Both succeeded and atomically published their completed outputs.
A caught producer failure writes a separate incomplete result; an earlier successful file cannot establish success of a failed invocation.
The mathematics is the complete DC1--DC7 argument with its exact native certificate boundary, not a finite scan extrapolation.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision distance-eight-boundary-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:31 |
| status | open |
| reason | Fix the entire actual K8/A18 boundary, communication and support result, DC1--DC7 complete rows/connectors/forced-first-step proof, H_8 and symbolic C_8, whole native certificate and strictly conditional critical consequence. Contributor author checks are retained at their actual scope; fresh whole independent mathematical/native review and adoption remain outstanding. No diagonal estimate, unconditional mean classification or R_f>=1/alpha conclusion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Whole actual K8 boundary/support/true-exterior communication, exact diagonal transfer, finite majorant, native scope and conditional radius/mean conclusion only. |
| argument | [Complete argument](#complete-argument) | All DC1--DC7, local exclusions and positive words, original chronological first-step/connector sums, H_8/C_8 and whole native bindings/coverage/limits. |
| dependency | [C841 adopted boundary criterion](Yin_C_G0841_v1.md#decision-whole-reviewed-2026-10-28) | Exact original-clock Green/excursion and complete diagonal conventions, same-class connector bound and paid near-R finite coupling; no diagonal estimate inherited. |
| dependency | [C785 adopted actual graph](Yin_C_G0785_v1.md#decision-whole-reviewed-2026-10-26) | Same quartic order coordinates, actual strict-strip core and original probabilities for all local allowed/killed tests. |
| dependency | [C833 adopted distance interface](Yin_C_G0833_v1.md#decision-whole-reviewed-2026-10-28) | Original shortest-word definition and complete actual low-distance input only, not its differently normalized operator. |
| support | [R1053 accepted finite native scope](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) | Complete57 states through9 and required targets already independently checked there; not review of this new statement or whole417 BFS. |
| support | [J52 whole new certificate](../computations/programs/Yin_J_G0052/readme.md#distance-eight-existing-boundary-channels) | Declared three inputs/two programs/two outputs,648 word occurrences/390 local candidate certificates/60 transfer terms and76/52 unknown frontiers; new author verification only. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:49 |
| status | proved |
| reason | Adopt the entire actual K8/A18 statement and DC1--DC7 argument after root read the complete author proof, both programs, fixed statement and whole independent mathematical/native R1066. The actual complete rows and predecessor exclusions, full-exterior boundary communication, every support count and original connector, all sixty forced-first-step transfer terms, entrywise H_8 and uniform C_8, and paid conditional near-R coupling are covered. Both complete unchanged programs were independently reproduced with entire output equality at the declared 417-state/16MiB/120-second scope. Accepted low-distance completeness and unknown-frontier limits remain exact. No actual diagonal estimate, unconditional mean classification or general R_f>=1/alpha conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Whole actual K8 boundary/support/true-exterior communication, exact diagonal transfer, finite majorant, native scope and conditional radius/mean conclusion only. |
| argument | [Complete argument](#complete-argument) | All DC1--DC7, local exclusions and positive words, original chronological first-step/connector sums, H_8/C_8 and whole native bindings/coverage/limits. |
| dependency | [C841 adopted boundary criterion](Yin_C_G0841_v1.md#decision-whole-reviewed-2026-10-28) | Exact original-clock Green/excursion and complete diagonal conventions, same-class connector bound and paid near-R finite coupling; no diagonal estimate inherited. |
| dependency | [C785 adopted actual graph](Yin_C_G0785_v1.md#decision-whole-reviewed-2026-10-26) | Same quartic order coordinates, actual strict-strip core and original probabilities for all local allowed/killed tests. |
| dependency | [C833 adopted distance interface](Yin_C_G0833_v1.md#decision-whole-reviewed-2026-10-28) | Original shortest-word definition and complete actual low-distance input only, not its differently normalized operator. |
| support | [R1053 accepted finite native scope](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) | Complete57 states through9 and required targets already independently checked there; not review of this new statement or whole417 BFS. |
| support | [J52 whole new certificate](../computations/programs/Yin_J_G0052/readme.md#distance-eight-existing-boundary-channels) | Declared three inputs/two programs/two outputs,648 word occurrences/390 local candidate certificates/60 transfer terms and76/52 unknown frontiers; new author verification only. |
| review | [Whole independent distance-eight finding](../audits/reviews/Yin_R_G1066_v1.md#whole-distance-eight-boundary-finding) | Entire fixed Statement and DC1--DC7, exact adopted interfaces, complete code/helpers, full producer/checker reproduction and whole output equality, every displayed tuple/row/word/weight and all sixty transfers, conditional finite-core payment and all unknown-frontier/diagonal/source limits. |

