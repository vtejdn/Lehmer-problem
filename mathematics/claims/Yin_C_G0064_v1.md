---
author: Yin
---
# Exponentially many frozen original quartic bridges and zero global replacement gap

Date: 2026-10-12T11:52.
Human author Yin.
The rounding-recovery author supplied the entire original D15 proof and original J92 exploration.
g0001_review_recovery independently checked its actual19:25 whole body and original program/output, and separately authored and actually ran J92's independent reconstruction, recorded in R279.
That reviewer NOW authors this new fixed statement/wrapper and therefore cannot independently review its actual extraction.
Root supplied broad assignment/execution coordination only and will arrange the separate actual review.
Initial status is proof draft / under review.
The ENTIRE original proof, all29 certificate cells, native/history/source limits and author correction are retained below.

## Statement

Fix the ACTUAL irreducible Salem quartic

    P(t)=1-t-t^2-t^3+t^4,
    p=(1,-1,-1,-1,1), beta>1 its real root,
    zeta a nonreal original conjugate with |zeta|=1.

For every integer n>=4 put N=2n and L=2n-4.
Let Omega_n contain EVERY eta in{-1,0,1}^N whose polynomial F_eta(t)=sum_(j=0)^(N-1)eta_j t^j has COMPLETE original field return F_eta(beta)=0.
Each word has a UNIQUE integer quotient

    F_eta=P A_eta, A_eta=sum_(j=0)^(L-1)a_j t^j.

Conversely include every integer quotient whose product has all N digits legal; no quotient-coefficient cutoff is imposed.
For z(eta) the number of original zero digits, retain the original independent digit probabilities1/4,1/2,1/4 and define

    W_n=sum_(eta in Omega_n)2^z(eta)>0,
    Pr(original return at2n)=W_n/4^(2n),
    pi_n(eta)=2^z(eta)/W_n.

Join two distinct vertices when their quotients differ in exactly one coordinate, equivalently when their original words differ by delta t^j P for a nonzero integer delta and both words are legal.
Let K_j be exact conditional resampling of a_j under pi_n given all other quotient coordinates, T_n=(1/L)sum_j K_j, and

    E_n(g,g)=<g,(I-T_n)g>_(pi_n),
    lambda_n=inf_(Var_pi_n(g)>0) E_n(g,g)/Var_pi_n(g).

This is the C60 original-law auxiliary dynamics, with one uniformly chosen site per update; it is not the chronological digit walk.

**A. Complete move and frozen criteria.**
At site j, put

    s_(j,r)=p_r eta_(j+r),
    m_j=min_(0<=r<=4)s_(j,r), M_j=max_(0<=r<=4)s_(j,r).

The ENTIRE legal integer update set is

    -1-m_j<=delta<=1-M_j, delta in Z.

The vertex is frozen, meaning it has no distinct neighbor, IF AND ONLY IF every five-digit window contains both+1 and-1 among its signed entries p_r eta_(j+r).
For an all-nonzero returned word this is equivalent to avoiding both p and-p as five-digit windows; this criterion by itself does not assert that a proposed word returns.
Jumps of size2 have legal intermediate unit jumps, so allowing all legal updates or only unit quotient changes gives the SAME connected components.
The zero word is not frozen, since every shifted +/-P is legal.

**B. Explicit blocks and safe concatenation.**
In ascending coefficient order define

    F=(1,-1,0,-1,-1,-1,-1,0,-1,1),
    G=(1,-1,-1,0,-1,1,-1,1,-1,0,-1,-1,1),
    H=(1,-1,-1,0,-1,1,-1,1,-1,-1,1,-1,1,-1,0,-1,-1,1).

Their lengths are10,13,18 and their original integer quotients are

    A_F=1+t^2+t^3+t^5,
    A_G=1+t^3-t^4+t^5+t^8,
    A_H=1+t^3-t^4+t^5+t^8-t^9+t^10+t^13.

Every block is an ACTUAL P-multiple, is internally frozen, has exactly two zeros, begins(1,-1) and ends(-1,1).
The complete retained proof supplies a valid positive/negative signed-entry pair at EVERY internal site:6 for F,9 for G,14 for H.

Any concatenation of independently signed copies of these blocks is a legal returned frozen word.
It remains so after l leading and r trailing zeros with0<=l,r<=2.
More generally the same seam proof applies to internally frozen legal P-multiple blocks of length at least4 whose signed first/last pairs are(sigma,-sigma) and(-sigma,sigma).
These assertions retain every crossing window and every legal integer jump.
Arbitrary padding is not allowed: three leading zeros already introduce a movable first window for this endpoint pattern.

**C. An explicit all-n family and its complete original probabilities.**
At EVERY integer n>=5 write n=5k+e with k>=1 and0<=e<=4.
Use this fixed template, choosing each of the k block signs independently:

| e | Ordered blocks | Leading zeros l | Trailing zeros r | r_e=l+r |
| --- | --- | --- | --- | --- |
| 0 | k copies of F | 0 | 0 | 0 |
| 1 | k copies of F | 1 | 1 | 2 |
| 2 | k copies of F | 2 | 2 | 4 |
| 3 | G followed by k-1 copies of F | 1 | 2 | 3 |
| 4 | H followed by k-1 copies of F | 0 | 0 | 0 |

Every resulting word has length EXACTLY2n, returns at EVERY original conjugate and is frozen.
There are exactly2^k DISTINCT nonzero template words; each has exactly2k+r_e zero digits.
Consequently EACH has unconditional probability2^(2k+r_e)/4^(2n), and the COMPLETE family has

    unconditional probability=2^(3k+r_e)/4^(2n),
    conditional mass under pi_n=2^(3k+r_e)/W_n>0.

Each individual conditional probability is2^(2k+r_e)/W_n.
No original zero-digit factor or full return normalizer is removed.
These formulas do not assert a nonvanishing conditional proportion or an asymptotic estimate for W_n.

The full graph therefore has at least2^floor(n/5) frozen vertices and at least2^floor(n/5)+1 connected components for EVERY n>=5.
The extra component contains the all-zero word, which is positive-mass, outside this family and nonfrozen.

**D. Exact all-n global gap obstruction.**
For EVERY n>=5,

    lambda_n=0.

Indeed the indicator of any template singleton has positive variance pi_n(v)(1-pi_n(v)) and zero Dirichlet energy under the ACTUAL full original law.
Nonnegativity of the form supplies equality.
This conclusion does not use finite table extrapolation, a numerical eigensolver or an estimate for component masses, and rescaling the update clock does not make this global gap positive.
Positive averaged conditional coordinate variances do not imply connectivity.

**E. Separately bounded exact finite graph data.**
Complete exhaustive enumeration, independently reconstructed at ONLY n=4,...,10, gives the following ACTUAL graph counts and original integer masses:

| n | Returned words | W_n | Undirected edges | Components | Frozen vertices | Zero component size | Zero component mass |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 11 | 328 | 16 | 1 | 0 | 11 | 328 |
| 5 | 29 | 1532 | 50 | 3 | 2 | 27 | 1524 |
| 6 | 75 | 7296 | 160 | 7 | 6 | 69 | 7200 |
| 7 | 201 | 35120 | 486 | 11 | 6 | 171 | 34096 |
| 8 | 547 | 170848 | 1496 | 15 | 8 | 449 | 163392 |
| 9 | 1481 | 835448 | 4478 | 23 | 14 | 1165 | 785520 |
| 10 | 4083 | 4119392 | 13560 | 51 | 34 | 3063 | 3799280 |

The return probability in each row is W_n/4^(2n), and a component's conditional mass is its displayed integer mass divided by W_n.
In particular n4 is connected; n5 is the first disconnected value IN THIS tested range.
No assertion about n<4 is supplied here.
All vertices, unique quotient vectors, original weights, neighbor lists, component labels/members/masses, frozen IDs and zero-word information are retained in J92.

The original program used complete contiguous-half matching and all legal shifted-P perturbations.
The separate independent program used complete even/odd-position matching from generic polynomial remainders, low-end quotient reconstruction, quotient-coordinate fiber cliques and union-find.
Its single actual fixed-domain run compared EVERY mathematical field, including all6,427 vertices and20,246 undirected edges across the seven rows, with exact equality.
No author helper was imported and no original output was overwritten.
This finite evidence proves only the stated finite data; Parts B--D have their independent complete hand proof.

**F. Midpoint and inference boundary.**
With the ORIGINAL neutral midpoint

    Z_n(eta)=-zeta^(-n)sum_(j=0)^(n-1)eta_j zeta^j,

EVERY member of the template family in C satisfies |Z_n(eta)|<=18, uniformly in n and all signs.
Every completed block evaluates to zero at zeta, and at most one length-at-most18 block is cut.
This family therefore supplies no diffusive midpoint witness.
Its exact original probability remains as stated in C; neither growth nor boundedness of the full midpoint second moment follows from this family bound.

C60's conditional implication from an ADDITIONAL eventual bound lambda_n>=c/(2n-4), c>0, remains logically valid, but D proves that this particular GLOBAL-gap premise is impossible for this actual dynamics.
Its contrapositive involving infinite chronological critical mean and liminf(2n-4)lambda_n=0 is consequently automatic here and cannot decide either mean branch.
No correction to the conditional proof, classification of all components/frozen words, componentwise mixing estimate, replacement dynamics, asymptotic midpoint lower bound, uniform-degree transfer or unrestricted Mahler conclusion is asserted.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:52 |
| status | open |
| reason | Register the full original-law frozen-family theorem for every n>=5, exact probabilities, zero global replacement gap and bounded family midpoint, separately from the complete independently reproduced n4--10 graph data. R279 covers the actual corrected original whole proof and J92 code/output/native reconstruction only. Its reviewer now authors this new statement, so a different noncontributor must inspect the actual extraction before adoption. Full original history,29 certificate cells and author correction remain. No chronological mean branch or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual quartic/original law/quotient dynamics, complete move criterion, all-n hand theorem and original probabilities, separately finite n4--10 graph data and exact midpoint/transfer limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:25 corrected D15 including allocation/history, Sections1--8/equations1--8, all29 active certificate cells, original19:23 freeze and dated F/site5 correction. |
| dependency | [C60 original returned-law and operator](Yin_C_G0060_v1.md#statement) | Actual quartic, complete original weights/quotient bijection, exact conditional-resampling operator, midpoint convention and the expressly conditional prior gap implication. |
| dependency | [C60 exact stationary/Dirichlet interface](Yin_C_G0060_v1.md#quartic-local-operator-and-energy) | Complete legal one-coordinate conditionals, positive original masses and original random-site normalization; no irreducibility or positive gap assumed. |
| dependency | [C60 gap-direction boundary](Yin_C_G0060_v1.md#quartic-local-gap-necessary-price) | Global Rayleigh definition and old lower-gap conditional implication only; the new singleton proof supplies zero gap directly. |
| dependency | [J92 original finite graph evidence](../computations/programs/Yin_J_G0092/readme.md#quartic-local-graph-native-completion) | ONLY PartE's complete n4--10 graph data, original full program/result/execution/terminal and original unequal digit weights. Not a premise of the all-n block proof. |
| support | [J92 actual independent reproduction](../computations/programs/Yin_J_G0092/readme.md#quartic-local-graph-independent-verification-completion) | Separately authored and ACTUALLY executed n4--10 exact reconstruction, all mathematical payloads compared, complete independent program/output retained with no range expansion. |
| support | [C55 explicit comparison and secondary counts](Yin_C_G0055_v1.md#statement) | ONLY old two-word comparison and original n6--10 totals; matched parity positivity is not a frozen-word or all-n premise. |
| support | [Original whole/native finding](../audits/reviews/Yin_R_G0279_v1.md#quartic-frozen-components-whole-independent-finding) | Complete corrected original19:25 D15, whole original J92 program/output and actual independent reconstruction; not this newly authored wrapper's actual extraction review. Finding relationship: self-reviewed. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:57 |
| status | proved |
| reason | Adopt the separately performed original whole/native R279 and actual extraction R282 findings. Preserve every original proof, certificate correction and declared/independently reproduced finite output. The all-n frozen/gap theorem and finite n4--10 graph data have separate evidence; neither resolves chronological mean or unrestricted G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, actual quartic/original law/quotient dynamics, complete move criterion, all-n hand theorem and original probabilities, separately finite n4--10 graph data and exact midpoint/transfer limits. |
| argument | [Complete retained proof](#argument) | ENTIRE actual19:25 corrected D15 including allocation/history, Sections1--8/equations1--8, all29 active certificate cells, original19:23 freeze and dated F/site5 correction. |
| dependency | [C60 original returned-law and operator](Yin_C_G0060_v1.md#statement) | Actual quartic, complete original weights/quotient bijection, exact conditional-resampling operator, midpoint convention and the expressly conditional prior gap implication. |
| dependency | [C60 exact stationary/Dirichlet interface](Yin_C_G0060_v1.md#quartic-local-operator-and-energy) | Complete legal one-coordinate conditionals, positive original masses and original random-site normalization; no irreducibility or positive gap assumed. |
| dependency | [C60 gap-direction boundary](Yin_C_G0060_v1.md#quartic-local-gap-necessary-price) | Global Rayleigh definition and old lower-gap conditional implication only; the new singleton proof supplies zero gap directly. |
| dependency | [J92 original finite graph evidence](../computations/programs/Yin_J_G0092/readme.md#quartic-local-graph-native-completion) | ONLY PartE's complete n4--10 graph data, original full program/result/execution/terminal and original unequal digit weights. Not a premise of the all-n block proof. |
| support | [J92 actual independent reproduction](../computations/programs/Yin_J_G0092/readme.md#quartic-local-graph-independent-verification-completion) | Separately authored and ACTUALLY executed n4--10 exact reconstruction, all mathematical payloads compared, complete independent program/output retained with no range expansion. |
| support | [C55 explicit comparison and secondary counts](Yin_C_G0055_v1.md#statement) | ONLY old two-word comparison and original n6--10 totals; matched parity positivity is not a frozen-word or all-n premise. |
| support | [Original whole/native finding](../audits/reviews/Yin_R_G0279_v1.md#quartic-frozen-components-whole-independent-finding) | Complete corrected original19:25 D15, whole original J92 program/output and actual independent reconstruction; not this newly authored wrapper's actual extraction review. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0282_v1.md#c64-frozen-components-actual-extraction-finding) | Entire actual statement, completely retained argument/history and all current direct interfaces, separately inspected after allocation by a noncontributor. Finding relationship: self-reviewed. |

## Registration and complete preservation

Date: 2026-10-12T11:52.
The actual corrected D15 body below is retained in full, with only repeated author front matter removed, its first title demoted once and terminal whitespace normalized.
All valid original relative links are retained.
The complete blocks and29-cell table, original F/site5 defect and corrected pair, native declaration/execution/discovery history, every original weight/normalizer, all proof and inference/source limits remain.

The old19:23 statement that independent native reproduction had not yet occurred remains true historical text at its original save.
The later ACTUAL independent run is explicitly recorded in J92 and R279 and described in the new statement above; preservation does not silently rewrite that past account.
LP17/TK06 remain inherited naming/attribution with their actual partial-access limits, not new external theorem premises or source-wide reviews.

The extractor's R279 finding remains at its original whole/native scope.
Authoring this new wrapper is a contribution and excludes a self-supplied independent actual-extraction verdict.
Initial status remains proof draft / under review.
No new native run, original proof/program/output edit, source acquisition, adoption or draft retirement accompanies this registration.

## Argument

## Connectivity and frozen words for original quartic local replacement dynamics

Date: 2026-10-12T11:02.
Human author Yin.
New AUTHOR inquiry following the separate D13 local-update account.
Root supplied only the broad question of exact connectivity/components/frozen returned words.
This author selects the mathematical candidates and any separately declared finite test; root supplied no formula or proof step.
The author cannot independently review this work.

## Precise question and boundaries

For the ACTUAL P=1-t-t^2-t^3+t^4 and complete original ternary return words of length2n, retain probabilities1/4,1/2,1/4 and the UNIQUE integer quotient F=P A.
Join two legal words when they differ by a nonzero integer multiple of one shifted P while all original digits remain legal.
Determine whether this exact coordinate-update graph is connected, has frozen words or has a proved obstruction persisting as n varies.
A finite connected table alone is not an all-n theorem, and padding a frozen example may add moves that destroy its isolation.

The existing D13 operator preserves the full original law and allows every legal value of the updated quotient coefficient.
Its Poincare gap is zero if the graph is disconnected; positivity requires actual connectivity, not just positive averaged coordinate variances.
All mathematics continues in this new D.
No native process is authorized at allocation.
A finite graph calculation, if needed, will have a responsible J, a complete declared range/resource/failure policy and root's specific execution confirmation before running.

## Bounded reuse and changed object

Read D13's exact legal quotient/update law and original probability proof, C55's finite matched-fiber table/witness, J91's complete original and independently reproduced n6--10 domains, and the earlier C45/C51/L332/L335 limitations.
A bounded local screen by frozen words, isolated returns, one-site/coordinate moves and local connectivity found no retained classification of this graph.
Some old uses of isolated return certificates concern temporal return paths, not graph connectivity between whole returned words.
No novelty or priority claim follows.

The next hand calculation will give an exact signed-window criterion for a legal move or frozen vertex.
A possible bounded graph test concerns connectivity of the complete returned-word set, not a rerun of the old parity moments.
It will not be interpreted as a diffusive lower moment or uniform Mahler theorem.

<a id="quartic-local-connectivity-exact-move-test"></a>
## 1. Exact move interval and frozen-word criterion

Fix n>=4, N=2n, L=N-4, p=(1,-1,-1,-1,1) and a complete legal return word eta.
Its unique integer quotient coefficients a_0,...,a_(L-1) have the exact meaning in the allocation above.
Updating a_j by delta in Z changes eta_(j+r) by delta p_r for0<=r<=4, leaving every other original digit unchanged.
Put

    s_(j,r)=p_r eta_(j+r) in {-1,0,1},
    m_j=min_r s_(j,r), M_j=max_r s_(j,r).

Because p_r^2=1, all five legality inequalities are exactly -1<=s_(j,r)+delta<=1.
Their COMPLETE intersection is

    -1-m_j<=delta<=1-M_j, delta in Z.               (1)

This interval always includes zero.
The update is forced to stay put if and only if m_j=-1 and M_j=1.
Otherwise +1 is legal when M_j<=0 and -1 is legal when m_j>=0.
The possible jump +/-2 occurs only when all s_(j,r) have the opposite sign; its intermediate unit jump is legal.
Hence the full conditional-resampling graph and the graph retaining ONLY legal unit quotient changes have exactly the SAME connected components.

Call a vertex frozen if it has no different legal neighbor at any site.
Equation (1) proves the exact all-site criterion

    eta frozen iff every five-digit window has
                  both +1 and -1 among p_r eta_(j+r).
                                                            (2)

In the all-nonzero digit subclass eta_r in {+1,-1}, this says exactly that no five-digit window equals P's coefficient word or its negative.
This is a criterion for actual returned words; it does not assert that an arbitrary pattern avoiding those two windows is divisible by P.

Every legal returned word has strictly positive ORIGINAL probability 4^(-N)2^(its zero count).
Thus a nonzero frozen word would give a positive-mass singleton component distinct from the zero word and force the global update Poincare gap to be zero at that actual n.
More generally any two components do so even when no vertex is frozen.
The zero word is never frozen here: +/-t^jP are legal nonzero neighbors at every site.
These are finite-state graph facts with the original law retained; no global connectivity or frozen-word existence is concluded yet.

The C55 positive matched pair itself supplies no frozen counterexample.
Its first word begins with -P and therefore has a legal site0 move to the zero block; the second word has the exact +P block at sites10,...,14 and has a legal site10 removal.
The non-Markov parity projection established in D13 does not by itself imply disconnectedness of the whole-word update graph.

<a id="quartic-local-connectivity-finite-declaration"></a>
## 2. Declared finite graph test and its exact reduction

The responsible [J92 declaration and program](../computations/programs/Yin_J_G0092/readme.md) specify ONLY n=4,...,10.
At this paragraph's save, the program has been statically inspected and parsed as source without importing or executing it; the D15/J92 material check passed.
The exact command and full120/115-second,512MiB and structural caps are recorded there.
Root's specific confirmation has been requested and no native process has yet run.

The finite reduction is complete.
Every length2n word splits UNIQUELY into a low n-word and a high n-word, with actual endpoint L(beta)+beta^n H(beta).
Enumerating all3^n choices on each side and matching the integer power-basis vector of L to minus that of beta^n H therefore enumerates every complete return exactly once.
The original integer word weight is the product of the two2^(zero count) factors, over4^(2n).
The program independently divides each full word by the monic original P and expands its quotient back to the complete word.
No parity matching, root approximation, endpoint cutoff or discarded original conjugate is involved.

For each complete vertex, the program tests all original digit updates for every site and delta in{-2,-1,1,2}; larger delta is impossible by (1).
It requires every legal destination to appear in the exhaustive returned-word set and checks that the actual quotient changed in exactly that one coordinate.
Exact neighbor symmetry and the separate signed-window isolated-vertex test are checked.
Complete connected-component traversal then partitions EVERY vertex and its original integer mass.
Full vertex/quotient/weight/neighbor/component payloads are retained so a later reviewer need not trust a summary alone.

The old C55 total original return counts and integer masses at n6--10 are secondary consistency checks, not an oracle supplying this new graph.
The n4--5 graph domain is also fully enumerated under the same original law.
The intended output can settle finite connectivity/frozen-word statements and identify a concrete candidate for a later hand argument.
It cannot establish connectivity for untested n, persistence under padding, a gap magnitude or the true midpoint diffusion gate.
Failure, absence of the desired witness and successful finite execution are to remain distinct outcomes.

<a id="quartic-local-connectivity-native-outcome"></a>
## 3. Actual bounded native outcome and separation from the all-n proof

2026-10-12T11:23.
Following root's recorded specific confirmation and a fresh authenticated same-window62percent reading, the declared J92 command ran ONCE and completed n4--10 with exit0.
The [actual single-run account](../computations/programs/Yin_J_G0092/readme.md#quartic-local-graph-native-completion) retains its full program, full graphs/quotients/weights, terminal and execution records, including the 1.406second supervisor duration and38,821,888byte peak observed working set.
No further native execution or expanded domain occurred.
The original pre-execution paragraphs above remain as dated history.

The finite returned-word/component/frozen counts are respectively (11,1,0), (29,3,2), (75,7,6), (201,11,6), (547,15,8), (1481,23,14), (4083,51,34) for n4 through10.
Thus the first tested disconnection is at n5.
This native run has not yet been independently reproduced.
The following new proof does NOT infer an all-n claim from these counts.
It gives explicit returned blocks and verifies every local move by hand, making the eventual claim independent of untested finite enumeration.
The calculation discovered useful short patterns, which is a disclosed discovery role rather than an external proof premise.

<a id="quartic-three-frozen-return-blocks"></a>
## 4. Three explicit returned blocks and complete local certificates

Represent a block by its ascending coefficients and retain its actual length, including any zero entries.
The following three blocks have lengths10,13,18:

    F=(1,-1,0,-1,-1,-1,-1,0,-1,1),
    G=(1,-1,-1,0,-1,1,-1,1,-1,0,-1,-1,1),
    H=(1,-1,-1,0,-1,1,-1,1,-1,-1,1,-1,1,-1,0,-1,-1,1).
                                                            (3)

Their explicit integer quotients are

    A_F=1+t^2+t^3+t^5,
    A_G=1+t^3-t^4+t^5+t^8,
    A_H=1+t^3-t^4+t^5+t^8-t^9+t^10+t^13.
                                                            (4)

Direct multiplication gives F=P A_F, G=P A_G, H=P A_H, where the letters in polynomial identities mean the polynomials with coefficients (3).
In particular each block returns at EVERY original conjugate, not just at the real beta or in a parity quotient.
One can verify every entry without division: if a is the listed quotient, its k-th product coefficient is a_k-a_(k-1)-a_(k-2)-a_(k-3)+a_(k-4), with out-of-range a zero.
Each block has exactly two zero digits, first two digits(1,-1), and last two digits(-1,1).

Here is a complete hand certificate of freezing inside each block.
A pair(r_+,r_-) in the row for site j means that p_(r_+) times the digit at j+r_+ is +1, and p_(r_-) times the digit at j+r_- is -1.
Indices are zero-based and lie between0 and4.
Every available site appears; a dash means that block has no such site.

| Site j | F pair | G pair | H pair |
| --- | --- | --- | --- |
| 0 | (0,4) | (0,4) | (0,4) |
| 1 | (2,0) | (1,0) | (1,0) |
| 2 | (1,4) | (2,0) | (2,0) |
| 3 | (1,0) | (1,2) | (1,2) |
| 4 | (1,0) | (2,0) | (2,0) |
| 5 | (1,0) | (0,2) | (0,2) |
| 6 | - | (2,0) | (2,0) |
| 7 | - | (0,4) | (0,3) |
| 8 | - | (2,0) | (1,0) |
| 9 | - | - | (2,0) |
| 10 | - | - | (0,2) |
| 11 | - | - | (2,0) |
| 12 | - | - | (0,4) |
| 13 | - | - | (2,0) |

For example F at j2 has the signed window(0,1,1,1,-1), and H at j7 has(1,1,1,-1,-1); the indicated signs occur exactly.
Formula (2) now proves every internal site forced.
Global sign reversal exchanges the two signs and preserves freezing and the original probability.

<a id="quartic-frozen-concatenation-and-padding"></a>
## 5. Concatenation and the exact safe outer-padding range

**Concatenation lemma.**
Suppose each of finitely many blocks is an actual P-multiple, is internally frozen, and, after its chosen global sign sigma, has first two digits(sigma,-sigma) and last two digits(-sigma,sigma).
Suppose each block has length at least4, as all the blocks in (3) do.
Concatenating them, with independent global signs on each block, gives another legal returned frozen word.

The returned polynomial is a sum of disjointly supported shifted P-multiples, so all digits remain in the original alphabet and its full original field value is zero.
Windows contained in one block satisfy (2).
For a boundary b, the only crossing windows start at b-4,b-3,b-2,b-1.
In the first two, the last two left-block digits occur at positions(2,3) or(1,2); both multipliers p_r equal-1 there, and those two digits have opposite nonzero signs.
In the last two, the first two right-block digits occur at positions(2,3) or(1,2), with the same conclusion.
Each such window has both signed values.
Since every block in the application has length at least10, a five-digit window crosses at most one boundary.
This proves the assertion for all concatenations used here.
For the stated length-at-least4 variant, crossing two boundaries would require at least six positions, so the same proof applies.

**Outer-padding lemma.**
Add l leading zeros and r trailing zeros, where 0<=l,r<=2, to any such concatenation.
It remains legal, returned and frozen.
Leading zeros multiply its polynomial by t^l, and trailing zeros retain its value and actual recorded word length.
The original internal windows are unchanged.
A new leading window contains the first two nonzero digits at positions(2,3) or(1,2); these are opposite signs with equal multiplier-1.
A new trailing window contains the last two nonzero digits at positions(1,2) or(2,3), again with equal multiplier-1.
Thus every new site is forced.
There is no claim for arbitrary padding: with three leading zeros the first new window sees(0,0,0,sigma,-sigma), whose signed entries are(0,0,0,-sigma,-sigma), and a nonzero legal update exists.
This explicitly explains why zero padding alone is not an unrestricted persistence principle.

The hand argument covers all possible quotient changes, including jumps of size2, because the signed-window criterion is equivalent to the complete integer interval (1); it is not a test of only selected moves.

<a id="quartic-all-n-frozen-components-and-zero-gap"></a>
## 6. All-n construction, exact original masses and the mechanical gap obstruction

**Theorem.**
For this ACTUAL quartic and original digit law, at EVERY integer n>=5 the complete length2n returned-word graph has at least 2^floor(n/5) distinct frozen vertices and at least 2^floor(n/5)+1 connected components.
The random-site conditional-resampling operator of D13 has global Poincare gap lambda_n=0 for EVERY n>=5.

Write n=5k+e, k>=1 and e in{0,1,2,3,4}.
A word template is specified by this table.
Each listed block independently takes either its positive or negative form; outer zeros are fixed.

| e | Ordered blocks before outer padding | Leading zeros l | Trailing zeros r | Total zero padding r_e | Number of blocks |
| --- | --- | --- | --- | --- | --- |
| 0 | k copies of F | 0 | 0 | 0 | k |
| 1 | k copies of F | 1 | 1 | 2 | k |
| 2 | k copies of F | 2 | 2 | 4 | k |
| 3 | G, then k-1 copies of F | 1 | 2 | 3 | k |
| 4 | H, then k-1 copies of F | 0 | 0 | 0 | k |
                                                            (5)

The lengths are respectively10k,10k+2,10k+4,13+10(k-1)+3=10k+6, and18+10(k-1)=10k+8, exactly2n in every row.
The k=1 cases include no F after G or H and are allowed.
By Sections4--5 every template instance is a returned frozen word, with the original alphabet and every original conjugate retained.
Sign choices give 2^k DISTINCT words: the block boundaries are fixed and the first coefficient of each block records its sign.
Each word is nonzero.

There are exactly2k+r_e zero digits in every member of this family.
Under independent original digits of masses1/4,1/2,1/4 its unconditional probability is exactly

    2^(2k+r_e)/4^(2n),
    total unconditional family probability=2^(3k+r_e)/4^(2n).
                                                            (6)

Define W_n as the sum of2^(zero count) over ALL complete returned words of length2n, so the actual return probability is p_(2n)=W_n/4^(2n).
Conditional on that return, each displayed frozen word has probability2^(2k+r_e)/W_n and the family has EXACT total mass

    pi_n(frozen family)=2^(3k+r_e)/W_n>0.             (7)

These identities neither estimate W_n asymptotically nor assert a nonvanishing proportion.
Every singleton is an actual positive-probability component.
The all-zero word has positive probability, is outside the family, and is not frozen because adding one shifted P is legal.
Its component supplies the extra component asserted by the theorem.

For any frozen vertex v, its indicator has strictly positive variance under the full original pi_n and has zero Dirichlet energy, since the update never exits or enters that singleton.
The defining infimum E_n(g)/Var_pi_n(g) therefore equals zero (all terms are nonnegative).
This proves lambda_n=0 without estimating eigenvalues, imposing an endpoint cutoff or appealing to native finite counts.
Rescaling the update clock does not restore a positive global gap.

The all-n conclusion is stronger than a sequence of zero-padded examples or a larger finite table: it gives explicit words, full original probabilities and a complete forced-move proof for EVERY n>=5, with exponentially many distinct singleton components.
It remains a result about this one fixed quartic and this one-site quotient dynamics.
It does not classify the other components or all frozen words, and the finite n4 connectivity in J92 remains separately native evidence.

<a id="quartic-frozen-family-midpoint-and-transfer-limit"></a>
## 7. Midpoint bound and the exact consequence for the earlier conditional route

Let zeta be the original unit-circle conjugate and

    Z_n(eta)=-zeta^(-n) sum_(j=0)^(n-1) eta_j zeta^j,

with the original midpoint convention of D13.
For every member of (5), each complete block before the cut evaluates to zero at zeta because it is a P-multiple.
Leading or trailing outer zeros contribute zero.
At most ONE block is cut by the midpoint, and that block has length at most18, with every digit of modulus at most1.
Since |zeta|=1,

    |Z_n(eta)|<=18                                  (8)

uniformly in n and all 2^k sign choices.
A cut between blocks has Z_n=0.
Thus this explicit exponentially large frozen family does not supply a diffusive midpoint witness.
Its probability in (7) is fully paid and may become small.
Neither global original midpoint variance growth nor boundedness follows from (8) on this subfamily.

The original D13 bound lambda_n m_n<=D_n and its proved implication from an UNPROVED eventual lower premise lambda_n>=c/(2n-4), c>0, remain valid conditional statements.
The present theorem proves that this PARTICULAR global-gap premise is impossible for the actual dynamics at every n>=5.
Its contrapositive mu=infinity implies liminf(2n-4)lambda_n=0 consequently becomes automatic here and cannot distinguish either chronological critical-mean branch.
No correction to the earlier conditional proof is needed, and no finite-mean or infinite-mean conclusion is obtained.

Any useful replacement would need a separately justified observable-sensitive or component-sensitive mechanism, or a different dynamics with its actual original stationary law proved.
No such replacement, component mixing estimate, matched-fiber n-growth estimate, uniform-degree statement or unrestricted Mahler result is asserted in this draft.
The actual isolated-word theorem is a precise all-n obstruction to the proposed global-gap transfer, with fixed quartic scope and all original probabilities visible.

<a id="quartic-local-connectivity-entire-author-freeze"></a>
## 8. Complete author check, attribution and freeze

2026-10-12T11:23.
The author has checked by hand the signed update interval, each product in (4), every pair in the complete certificate table, all four seam positions, both safe padding positions at each end, the five residue classes including k=1, distinctness and zero counts, original unconditional/conditional masses, the singleton Rayleigh argument and the one-partial-block midpoint bound.
This is author checking, not independent review.
The finite experiment's actual outputs retain their separately limited evidence status and require an actual independent program/output review for accepted finite graph data.

Classical finite conditional-resampling, Dirichlet and variational-gap naming is inherited with D13's local proofs and its precise ordinary LP17/TK06 attribution/access limits.
This draft invokes no new external graph, mixing, recurrence or asymptotic theorem.
The short integer polynomial/window/concatenation calculations are fully displayed local deductions; no novelty or priority is asserted.
The finite enumeration discovered the seed patterns but is not needed as a mathematical premise for Sections4--7, which are directly checkable.
No new source acquisition is claimed.

Freeze the ENTIRE actual D15, including original question/reuse/roles, pre-execution history, Sections1--8/equations(1)--(8), complete native-outcome separation and all inference limits.
The rounding-recovery agent is the sole substantive mathematical author under human Yin; root supplied only the broad question and execution/source coordination and supplied no formula or proof step.
The author cannot independently review this draft.
A separate whole review must inspect the actual complete body, not just the all-n statement.
No C assessment or adoption accompanies this freeze.
A scoped material check follows and certifies only material structure.

<a id="quartic-local-connectivity-corrected-author-freeze"></a>
### Dated certificate-cell correction and complete final freeze

2026-10-12T11:25.
A further author read found that the first saved certificate table had F/site5 pair(2,0), whose proposed positive position is actually zero.
The correct pair is(1,0): its full signed window is(-1,1,0,1,1).
The table cell above is corrected, and the original erroneous pair and exact reason are retained here.
This changes no word, quotient, local criterion, theorem, probability or native program/output; it repairs the displayed local certificate.
The scoped D15/J92 structural check passed before this read and did not detect this mathematical transcription error.
The author has re-read all other certificate cells against the displayed blocks.
Freeze the ENTIRE actual D15 including this explicit correction at19:25 for whole independent review; the earlier19:23 freeze remains historical.
No earlier independent review is asserted.
