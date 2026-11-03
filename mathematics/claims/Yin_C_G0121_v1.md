---
author: Yin
---
# Ancestor-chain residual capacities beyond bounded terminal size

Date: 2026-10-15.
Human author Yin.
The g_bridge_audit AI authors this inquiry.
Root requested progress for balanced terminal remainders, but has not supplied a proof step for the residual-capacity argument below.

<a id="ancestor-residual-question"></a>
## Question and bounded reuse

Can C119's stopping-chain geometry be combined with actual phi capacities and the linear original window to replace bounded terminal SIZE by a broader structural condition, without merely repeating C114's bounded mean of omega of the ORIGINAL orders?
Preserve every ancestor core, original root weight, merged bucket capacity and physical time; terminal residues are not actual smaller polynomials.

Read [C114's original-law finite-core and mean-support theorem](Yin_C_G0114_v1.md#statement), C116's full prime-price/coverage boundaries, [C119's complete canonical tree/ancestor-chain proof](Yin_C_G0119_v1.md#argument) and the pertinent earlier C91/C102/C106 residual-bucket formulas.
The initial broad text search was truncated and supplies no absence evidence; the subsequent narrower screen covered the exact C86/C91/C102/C106/L159 residual, phi and bucket passages.
The new needed step is uniform control after merging actual ancestor orders by o/gcd(o,G), which is distinct from assuming bounded original support.
C119 now selects [its whole-reviewed decision](Yin_C_G0119_v1.md#decision-whole-reviewed-2026-10-15), adopting R474; this actual status was checked before the final argument.
No new recognized external theorem or source is invoked.
Continued native mathematics would require a J; none is needed for the direct finite identities.

<a id="ancestor-residual-working"></a>
## Incremental deductions and failure boundaries

Preserve substantive formulas and useful failed closure here; do not modify the frozen preceding original.
A complete positive result is not presumed.

<a id="exact-merged-residual-capacity"></a>
<a id="argument"></a>
## 1. Exact merged residual capacity, with its unavoidable core factor

Fix any positive integer G and define u(o)=o/gcd(o,G).
Then for EVERY positive integer u,

    sum_(o:u(o)=u) phi(o)=G phi(u).                    (1)

The fiber is finite.
To check it, write E=v_p(G), f=v_p(u).
The equation for the exponent e=v_p(o) is max(e-E,0)=f.
If f>0, necessarily e=E+f and phi(p^(E+f))=p^E phi(p^f), including E0.
If f=0, e runs from0 to E and sum_(e=0)^E phi(p^e)=p^E.
Multiplying these exact finite factors gives(1), including G1,u1,p2.
This is a direct expansion of the established divisor-totient identity already used in C91/C106, not an imported new source theorem.

For any subset of distinct original labels with0<w_o<=phi(o), merge residual buckets by

    z_u=(1/G)sum_(o:u(o)=u)w_o.

Then0<z_u<=phi(u) after zero buckets are removed.
The merged total is M/G, where M is the ORIGINAL mass of that subset.
For integer k>=1,

    u(o)|k iff o|Gk,

so captures restore by multiplication by G at the exact physical time Gk.
There is no loss from merging, but neither mass nor degree can be read as if M/G were original root count.
For a triple, lcm(u(a),u(b),u(c)) is the residual of the original lcm relative to G, so

    G lcm(u(a),u(b),u(c))=lcm(G,a,b,c).                (2)

Thus original compatibility lcm(a,b,c)<=X automatically transfers to quotient compatibility in floor(X/G) when G divides that original lcm (as it does if G is the core of a deepest coordinate in C119).
Without such a condition the transfer is not valid in general: G2, X3 and the triple(3,3,3) have original lcm3 but residual lcm3>floor(3/2).
Divisibility by G is a sufficient guard, not a claimed necessary condition in every individual instance.

The factor G in(1) is sharp even under full capacities and a linear window.
Take all divisors of G with w_o=phi(o), W=G, X=G.
Every residual is1, its merged original mass is G, triple density1 and H_X=W.
This is an exact capacity/linear-window control, not an actual polynomial or near-one counterexample.
It rules out a core-independent upper bound on the UNNORMALIZED residual bucket; it does not refute correctly normalized capture.

<a id="ancestor-complexity-interface-and-gap"></a>
## 2. What the ancestor-chain reduction does and does not close

For a C119 node with core G, take original labels stopping at that node or its ancestors.
An ancestor label o=G_i r_i has G_i|G, so its residual u(o)=o/gcd(o,G) divides r_i.
Consequently omega(u(o))<=omega(r_i).
Formula(1) makes their merged normalized weights legitimate C114 capacities.
A bound on the mean terminal omega for THIS ancestor stock therefore passes to its residual law with no support-union assumption.

The missing step is global aggregation.
Different deepest nodes use different G, merged arrays and ancestor masses M_G.
Applying C114 separately bounds the entire residual triple mass of each ancestor stock, not just the triples with a coordinate stopping at that deepest node.
Summing these full bounds can repeatedly charge the same ancestor mass.
Also the ORIGINAL global mean of omega(r_X(o)) does not automatically bound every conditional ancestor-stock mean.
Neither a depth-free summation estimate nor a favorable conditional density is supplied by(1).
This prevents claiming that C114's original mean theorem has already transferred to terminal mean complexity.

The issue is not the elementary capacity normalization: that is exactly settled by(1).
It is the correlation between the deepest-coordinate weight, its ancestor law and the charged G/time ratio.
No unrestricted balanced-remainder capture or bounded-terminal-mean theorem is claimed in this round.

<a id="relative-remainder-pair-certificate"></a>
<a id="statement"></a>
## 3. A direct paid relative-remainder certificate

There is a separate elementary way to use the C119 chain without requiring bounded terminal size.
Keep its canonical tree, arbitrary positive original weights, total W, original window X and ordered triple density delta_X.
For a FIXED integer K>=1 set L_K=lcm(1,...,K).
For eligible labels a,c whose stopping nodes satisfy v(a)<=v(c) in the ancestor order (including equality), define

    e(a|c)=r_X(a)/gcd(r_X(a),r_X(c)).

Let the ORIGINAL directed pair cost be

    psi_K=(1/W^2)sum_(eligible a,c:
              v(a)<=v(c), e(a|c)>K)w_a w_c.           (3)

This is a finite directly specified statistic; ineligible labels stay in W.
It is neither an unconditioned prime incidence nor an assumed bound on the remainder magnitudes.

For fixed eligible c, every ancestor label a with e(a|c)<=K divides L_K c.
Indeed its core G_a divides G_c, and r_X(a) divides e(a|c)r_X(c), while e(a|c)|L_K.
Thus its total original mass is at most H_(L_K X), because c<=X.
Every compatible triple has a deepest stopping coordinate by C119.
If both other directed pairs into that coordinate are good, its total contribution, summed over the three possible deepest positions, is at most3H_(L_K X)^2 W.

Any compatible triple not covered by that good estimate has a bad directed pair in one of the SIX ordered coordinate positions.
The full third mass is at most W, so the union bound costs at most6 psi_K W^3.
Repetitions and deepest ties are included by the union bound, not excluded.
Consequently

    delta_X <= 6 psi_K+3[H_(L_K X)/W]^2.              (4)

In particular, if delta_X>=delta>0 and6 psi_K<=delta-lambda for fixed lambda>0 and K, then one n<=L_K X captures at least sqrt(lambda/3)W.
This is a positive structural certificate at unbounded remainder SIZE and unbounded original omega.
It does NOT show that psi_K is small, and its factor6 is an explicitly paid union bound.
No capacity hypothesis was required in this separate argument.

A simple sufficient condition is that all eligible terminal remainders have the form r_X(o)=g b_o with one common positive integer g and1<=b_o<=K.
Then e(a|c)=b_a/gcd(b_a,b_c)<=K for every comparable pair, so psi_K=0.
The common g may be unbounded; the return time is L_K c<=L_K X, not g L_K X, because the deepest label ALREADY contains g.
This is a relative-divisibility condition, not an uncharged growing size threshold.
It still does not follow from positive triple density or bounded global terminal mean.

For an ACTUAL monic irreducible nontorsion integer-unit polynomial P of original degree d, with a good prime ell not dividing disc(P), complete selected original-root group counts W>=gamma d, and integer1<=X<=Cd as in C119, the positive gap in(4) gives complete original local income at least gamma sqrt(lambda/3)d log ell at one n<=L_K C d.
Keep D_n=Res(P,t^n-1)=Norm_(Q(alpha)/Q)(alpha^n-1), its sign before absolute logarithm, and every original root/depth.
The single auxiliary t^n-1 has full degree n<=L_K C d, content1 and squared coefficient norm2.
L168 therefore yields a strict positive Mahler bound with eta=gamma sqrt(lambda/3)log2 and time constant L_K C.

Conversely, under hypothetical near-one actual inputs retaining fixed gamma,delta,C, its full original budget U_(L_K C)(P)->0 gives from(4)

    liminf psi_K >=delta/6                            (5)

for EVERY FIXED K.
This is an explicitly directed relative-remainder incompatibility along ancestor pairs, not a prime collision claim or an automatic general localization theorem.

<a id="capacity-linear-window-controls"></a>
## 4. Controls satisfying capacity, linear window and positive density

The [elementary dyadic-prime consequence already proved in L395](../ledger/Yin_L_G0395_v1.md#individual-support-star-cover-failure), using its checked L17 prime-reciprocal divergence, supplies arbitrarily large intervals(Q,2Q] containing at least any requested finite k primes.
For each integer k>=4 choose such an interval with Q>max(4,2k), select EXACTLY k distinct primes in it, and set g equal to their product.
Then

    phi(g)/g=product_(q|g)(1-1/q)
              >=1-sum_(q|g)1/q>1-k/Q>1/2,
    max_(q|g)q<=2Q<sqrt(g).

The last inequality follows from g>Q^k and k>=4,Q>4.
All factors have exponent1, so g is a balanced terminal remainder at any root window at least g.
These existence facts require no quantitative prime theorem and no numerical search.

**A. The conditional-mean shortcut really fails within the full finite constraints.**
Choose the unique integer power of2 with g<X<2g, equivalently X=2^ceil(log_2 g); g is odd and greater than1, so equality cannot occur.
Use just the two labels g and X, with REAL weights

    w_g=X/k,  w_X=X/2=phi(X).

Since X<2g and k>=4, w_g<g/2<phi(g).
The total W=X(1/2+1/k) obeys X<2W.
Both labels are eligible.
The g-label stops at the ROOT with terminal remainder g, whereas the power-of2 label successively strips powers of2 and stops with terminal remainder1.
Their original global mean terminal complexity is

    [w_g omega(g)+w_X omega(1)]/W
      =1/(1/2+1/k)=2k/(k+2)<2.

But the ancestor stock of the ROOT stopping node consists solely of g, and its conditional mean complexity is k.
Thus no uniform bound on EVERY ancestor-stock mean follows from this bounded global mean.
Triple density is at least the all-X diagonal proportion

    delta_X >=[w_X/W]^3=[k/(k+2)]^3>=8/27.

All capacity and linear-window constraints are explicit.
The two labels are coprime, their lcm=gX>X, and H_X=w_X, so the construction is readily captured; it is NOT a counterexample to bounded-terminal-mean capture or to the general density goal.
It isolates only the failed conditional-mean inference.
No actual polynomial or near-one realization is claimed.

**B. The relative certificate is strictly broader than the bounded-mean hypotheses at the abstract capacity scope.**
Instead use the SINGLE label g with full weight phi(g), X=g.
Then X<2W, delta_X=1, terminal remainder g and psi_1=0.
Meanwhile both original mean omega and terminal mean omega equal k, which is unbounded.
Thus the fixed-K relative-divisibility certificate does not require either of those bounded means, even with full integer capacities and linear windows.
This simple control is already trivially capturable; it distinguishes hypotheses, not difficulty or novelty of its capture.
It does not claim separation from C114's WIDER paid-core/gap condition, from all earlier sufficient classes, or at the unconstructed near-one actual-polynomial scope.

<a id="ancestor-residual-final-boundaries"></a>
## 5. Exact scope, boundaries and contributions

Section1 settles the merged capacity and its factor G completely.
Section2 preserves the actual unclosed global-aggregation/conditional-law obstacle.
Section3 gives a proved relative-remainder PAIR certificate and corresponding necessary directed-pair escape, with every union-bound and physical-time factor present.
Section4 supplies controls satisfying the full advertised finite constraints, not examples with a hidden superlinear window.
These are useful deductions from the existing tree, not a general solution for its balanced remainders.

In §3 zero weights may be removed; W>0 is assumed.
If there are no eligible labels, psi_K=delta_X=0 and the inequality is immediate.
K is a FIXED positive integer, L_1=1, and every same-node pair is included in both directions as its actual ordered pair.
No symmetry of e(a|c) is assumed.
A zero psi_K is allowed.
Repeated coordinates have e(a|a)=1; this is consistent with the full triple counting.
The good ancestor mass at a fixed c is bounded at the ONE time L_K c; no sum of local norm incomes at different c is taken.
All such times lie in the same finite window and H is attained.
The factor L_K may contain the original good prime ell; every higher and exceptional depth is retained by the [L74 local floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail).
The [L168 finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) and [uniform original budget](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) are used with the FULL fixed multiplier L_K C.
Letting K grow requires paying that multiplier anew and supplies no uniform conclusion here.

Root requested this leap but supplied no new proof step of the merged-capacity identity, relative-pair certificate or controls; its contribution to the reused C119 prime-power tree remains credited there.
The g_bridge_audit AI authored all new derivations in this round.
The direct finite identity reuses the established divisor-totient formula; the only external-source-linked construction input is the already retained L395/L17 dyadic-prime consequence at its existing scope.
No new external theorem, program, J, actual polynomial construction, automatic coverage or unrestricted gap is claimed.
The bounded-terminal-mean/global aggregation question remains OPEN after this round.

<a id="ancestor-residual-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T21:26.
Freeze the ENTIRE bounded author account: exact merged phi-capacity identity and sharp G normalization; physical-time/lcm guard and its finite failure control; preserved global-aggregation gap; complete directed relative-remainder certificate, factor6 pair loss and factor3 deepest-coordinate count; actual full signed norm and L_K degree costs; fixed-K near-one directed-pair escape; capacity/linear-window/positive-density conditional-mean control and strict bounded-mean hypothesis separation; existing source scope, all nonimplications and contributions.
The author self-check covers finite fibers, shared primes and p2, u1/G1, no hidden primitive-part or mass normalization, empty eligibility, both pair directions at equal nodes, repeats/deepest ties, original versus terminal-law distinction, exact construction weights and all density/window/capacity inequalities, and fixed versus varying K.
No bounded-terminal-mean theorem or automatically small psi_K has been obtained.
Independent review must cover the actual fixed material before adoption; the structural check is not mathematical acceptance.

## Fixed organization

The entire final author original is retained: exact merged capacity and core/time guard, the unclosed aggregation question, full relative-pair certificate, actual norm transfer, capacity/linear-window controls, source and contribution limits, and final author check.
Root supplied the inquiry only and its older tree contribution is disclosed; separate review of this actual whole fixed artifact is pending.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:26 |
| status | open |
| reason | Retain the exact merged capacities and directed relative-remainder sufficient certificate with complete original weights and fixed L_K costs. Bounded-terminal-mean aggregation and automatic small pair cost remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Relative-remainder certificate](#statement) | Entire finite directed-pair estimate, actual original-norm sufficient class, fixed-K escape and declared controls and limits. |
| argument | [Complete capacity and pair proof](#argument) | Entire Sections 1--5, every original/quotient capacity, time, weight, conditional-law and finite-control distinction. |
| dependency | [Canonical tree](Yin_C_G0119_v1.md#canonical-power-stripping-tree) | Exact canonical stopping nodes, cores, terminal remainders and finite eligibility. |
| dependency | [Compatible stopping chains](Yin_C_G0119_v1.md#argument) | Full original-window ancestor-chain implication and deepest-coordinate counting interface. |
| dependency | [Original local norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Same-time full original-root local income, with all extra depths retained. |
| dependency | [Original norm decay](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Fixed L_K C degree multiplier and full original norm budget. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Actual strict positive Mahler bound from the fully paid single-time income. |
| dependency | [Existing dyadic prime consequence](../ledger/Yin_L_G0395_v1.md#individual-support-star-cover-failure) | Only the exact elementary prime supply used in the two finite scope controls, retaining its L17 input limits. |
| support | [Original mean capture](Yin_C_G0114_v1.md#statement) | Comparison with conditional residual laws; no general terminal-mean closure is claimed. |
