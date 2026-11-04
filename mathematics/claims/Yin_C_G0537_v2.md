---
author: Yin
---

# Persistent isolated edges in the complete actual four-step carry union

The complete original mathematical argument is retained from [L414](../ledger/Yin_L_G0414_v1.md#persistent-carry-reuse).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0423_v1.md#persistent-carry-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

The [initial fixed registration](Yin_C_G0537_v1.md#statement) remains open with its original statement and registration decision.
This successor states the same original result precisely; the constructor's summary revision is SELF and supplies no independent-review claim.

## Statement

Fix P=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta, O=Z[beta], B=1/(beta-1), S=beta B=B+1, b=B/beta and rho(q)=abs(q(zeta)).
Use the actual original core D={q in O:abs(q_+)<B,abs(q_-)<S} and original chronological digits x->beta x+eta with probabilities p_0=1/2,p_+=p_-=1/4.
Let c_l(v) be the full l-digit endpoint integer weight, so Pr(endpoint v)=4^-l c_l(v), and p_l=4^-l c_l(0).

For n>=5,k=n-2, normalize C170's left label by x=beta^-k a and keep right label c.
The complete bipartite union over n has two copies of D and an edge(x,c) exactly when an original four-step core path goes from c to -x.
Its unique middle polynomial satisfies x+theta+beta^4 c=0, with theta=sum_(j=0)^3 theta_j beta^j and theta_j in{-1,0,1}.
Every such edge occurs at all sufficiently large symmetric zero-padded lengths; kernel irreducibility alone is not used to infer incidence connectivity.

Put Delta=beta-beta^-1.
For every sufficiently small delta>0 with Delta delta^2<beta^-4, infinitely many nonzero w in O have abs(w_+),abs(w_-)<delta and unbounded rho(w).
For epsilon=(beta-beta^-1)w^2 define

    c=B-epsilon, q_i=B-beta^i epsilon (0<=i<=4),
    y=q_4, x=-y.

All q_i are actual core states; c has a unique four-step outgoing word(-1,-1,-1,-1) and y has a unique four-step predecessor, namely c.
Thus(x,c) is an isolated edge of the COMPLETE union, distinct from its sign partner and the zero component.
There are infinitely many such isolated components and their true midpoints

    Y=B-beta^2 epsilon

are nonzero with unbounded neutral modulus.

Let A_D,B_D>0 be the accepted fixed quartic all-core selected-path constants.
For each constructed edge choose actual words x to0 and0 to c of lengths l_x<=A_D(rho(c)+4)+B_D and l_c<=A_D rho(c)+B_D, and put k_*=max{3,l_x,l_c}.
For every k>=k_* its padded word has unconditional original probability at least

    4^(-(l_x+l_c+4)) 2^(-(2k-l_x-l_c)).

The conditional probability of this selected returned word is its unconditional original probability divided by the complete p_(2k+4).
The full word-fiber component on this edge is closed, has constant nonzero midpoint and positive mass; hence C170's global spectral gap is exactly zero for every n>=k_*+2.

For actual endpoint-word probabilities q_x,q_c, put

    a_k(x)=c_k(beta^k x), b_k(c)=c_k(c), S_k=c_(2k+4)(0),
    t_k=c_k(0)^2/S_k, D_k=p_(2k)/p_k^2,
    M_(c,k)=a_k(x)b_k(c)/S_k.

Then q_x c_k(0)<=a_k(x)<=c_k(0), q_c c_k(0)<=b_k(c)<=c_k(0), q_x q_c t_k<=M_(c,k)<=t_k and1/(256D_k)<=t_k<=1/(16D_k).
The sign partner has the same mass; the full component defect is at least M_(c,k)(1-M_(c,k)) and also at least2M_(c,k)(1-2M_(c,k)).
All tail multiplicities are retained.
No fixed mass floor, defect-to1/4 conclusion, critical-mean classification, changed-overlap theorem or unrestricted gap is proved.
This refutes the eventual positive-global-gap premise for this b2 operator, while preserving C170's conditional implication and the separate fixed-defect possibility.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision precise-current-statement-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:29 |
| status | open |
| reason | Correct the new summary's conditional-probability wording: the original unconditional selected-word probability is divided by the full return probability. Preserve the complete original proof; v1 remains open. Current SELF whole inspection and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Actual quartic strict core, entire b2 union and original law, infinitely many two-sided isolated edges, unbounded nonzero midpoint, every-late onset and full component masses with all costs; no fixed-defect or mean conclusion. |
| argument | [Entire complete argument](#argument) | Actual quartic strict core, entire b2 union and original law, infinitely many two-sided isolated edges, unbounded nonzero midpoint, every-late onset and full component masses with all costs; no fixed-defect or mean conclusion. |
| dependency | [Exact fixed input](Yin_C_G0400_v1.md#statement) | Exact actual strict quartic core, B in O and reciprocal reversal with the explicit fixed-quartic co-return premise. |
| dependency | [Exact fixed input](../ledger/Yin_L_G0309_v1.md#quartic-full-core-linear-return) | Accepted actual quartic selected original paths of length A_D rho+B_D, retaining boundary and compact constants; no mean-time theorem. |
| dependency | [Exact fixed input](../ledger/Yin_L_G0319_v1.md#actual-forced-boundary-segments) | Exact forward forced threshold B/beta and original digit law; reverse uniqueness is proved locally. |
| dependency | [Exact fixed input](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Complete b2 original word and endpoint law, tail fibers and component correspondence. |
| dependency | [Exact fixed input](Yin_C_G0519_v1.md#seed-complete-count-comparison) | Full endpoint autocorrelation and arbitrary-return concatenation, extended here to fixed constructed endpoint words. |
| dependency | [Exact fixed input](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Exact p_l normalization, p4=1/16 and t_k versus D_k; no seed-mass sufficiency premise. |
| support | [Exact fixed input](Yin_C_G0514_v2.md#bulk-component-defect) | Exact finite-component mean-variance defect used only for the paid lower bounds; no full chi upper bound. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:36 |
| status | proved |
| reason | Under the current human maintenance authorization, adopt the exact complete current statement and original fixed argument after the actually completed R737 constructor SELF whole inspection. Preserve original author/source/native evidence, old R bindings and relationships, and all initial open registrations or precision successors. No new research or producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Actual quartic strict core, entire b2 union and original law, infinitely many two-sided isolated edges, unbounded nonzero midpoint, every-late onset and full component masses with all costs; no fixed-defect or mean conclusion. |
| argument | [Entire complete argument](#argument) | Actual quartic strict core, entire b2 union and original law, infinitely many two-sided isolated edges, unbounded nonzero midpoint, every-late onset and full component masses with all costs; no fixed-defect or mean conclusion. |
| dependency | [Exact fixed input](Yin_C_G0400_v1.md#statement) | Exact actual strict quartic core, B in O and reciprocal reversal with the explicit fixed-quartic co-return premise. |
| dependency | [Exact fixed input](../ledger/Yin_L_G0309_v1.md#quartic-full-core-linear-return) | Accepted actual quartic selected original paths of length A_D rho+B_D, retaining boundary and compact constants; no mean-time theorem. |
| dependency | [Exact fixed input](Yin_C_G0601_v1.md#actual-forced-boundary-segments) | Exact forward forced threshold B/beta and original digit law; reverse uniqueness is proved locally. |
| dependency | [Exact fixed input](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Complete b2 original word and endpoint law, tail fibers and component correspondence. |
| dependency | [Exact fixed input](Yin_C_G0519_v1.md#seed-complete-count-comparison) | Full endpoint autocorrelation and arbitrary-return concatenation, extended here to fixed constructed endpoint words. |
| dependency | [Exact fixed input](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Exact p_l normalization, p4=1/16 and t_k versus D_k; no seed-mass sufficiency premise. |
| support | [Exact fixed input](Yin_C_G0514_v2.md#bulk-component-defect) | Exact finite-component mean-variance defect used only for the paid lower bounds; no full chi upper bound. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0737_v1.md#current-g415-complete-self-finding) | Entire exact current Statement and complete Argument with every listed actual input, original field/core/law/time/cost boundary and no new mathematical producer; constructor SELF, not independent. |

## Complete original argument

<a id="argument"></a>

### Original account: Persistent isolated carry edges from two real boundary directions

Date: 2026-10-18T16:34.
Human author Yin.
Root supplied the open S2/S7 question whether the union of normalized b=2 carry graphs is connected.
The entropy_attainment_bridge agent develops the construction and all new deductions below.
No new graph length, word scan, native computation or source acquisition is used.

<a id="persistent-carry-reuse"></a>
## Exact question and reused actual core

[L409](Yin_C_G0514_v2.md#nested-normalized-carry-support) proves that normalized b=2 graphs are nested and that certain early n5--7 components join zero through the connected n8 graph.
[L411](Yin_C_G0519_v1.md#seed-complete-count-comparison) prices complete-fiber weights on that fixed hub, but does not classify all later vertices.
The question here is whether EVERY fixed returned word eventually joins the zero component after symmetric padding.
The construction below answers this negatively by actual edges isolated in the entire infinite union.

Use P=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta and O=Z[beta].
Put B=1/(beta-1), S=beta B=B+1, b=B/beta and rho(q)=|q(zeta)|.
The accepted [exact-core theorem](Yin_C_G0400_v1.md#exact-salem-return-strip), applied using its explicit quartic L169 premise, states

    D={q in O: |q_+|<B, |q_-|<S}.                       (1)

These are precisely actual states on finite original zero-to-zero words.
The whole conditional strip proof and its separate [R69 applicability finding](../audits/reviews/Yin_R_G0069_v1.md#exact-strip-growth-review) were read at their explicit quartic domain.
This is not merely a relaxed strip model.
The [L309 quartic continuation theorem](../ledger/Yin_L_G0309_v1.md#quartic-full-core-linear-return) gives B=beta^3-beta-2 in O, B_-=-S, and fixed constants A_D,B_D>0 such that every q in D has a zero continuation of length at most A_D rho(q)+B_D.
The reciprocal involution J=beta^-1 iota, iota(beta)=beta^-1, preserves D and rho and reverses a chronological edge with its digit negated.
Thus the same bound supplies a word from zero to q as well.
The actual [R786 whole-path review](../audits/reviews/Yin_R_G0786_v1.md#weighted-tail-complete-independent-review) explicitly checks this quartic above the golden ratio, distinguishing it from L189's older restricted argument.
All those fixed-input constants and source/review boundaries are reused unchanged.

The original chronological kernel is K(q,beta q+eta)=p_eta for allowed endpoints in D, with p_0=1/2 and p_+=p_-=1/4.
[L319](Yin_C_G0601_v1.md#actual-forced-boundary-segments) already proves that q_+>b forces the next digit-1.
The needed reverse direction follows directly from the other real strip and is proved below.
The two-real-coordinate lattice selection reuses the mechanism of [L316](Yin_C_G0599_v1.md#actual-tangent-core-states), with an explicit square producing the two required signs.
C76's paths and C80's frozen family concern a different six-digit operator; neither is used as a frozen-state premise here.
A bounded search of existing carry/forced/singleton/union interfaces did not locate this persistent b2 obstruction; no historical novelty assertion is made.

<a id="union-carry-original-incidence"></a>
## 1. The complete union is an original four-step incidence graph

For n>=5 put k=n-2 and use C170's normalized left endpoint x=beta^-k a and right endpoint c.
Its unique middle four-digit polynomial theta satisfies

    x+theta+beta^4 c=0,
    theta=sum_(j=0)^3 theta_j beta^j,
    theta_j in{-1,0,1}.                                (2)

The union of these bipartite graphs has two copies of D as its vertex sets, and an edge(x,c) exactly when there is an original four-step path from c to -x.
To see necessity, an actual full returned word gives a path from x to zero by reversing and negating its left tail, and a path from zero to x using the negated remainder of the returned polynomial.
The right tail reaches c from zero, while beta^(k+4)c=-a-beta^k theta supplies a length-(k+4) continuation from c to zero after reversing the negative coefficient word into chronological order.
Thus c is an actual core state as well.
Equation(2), with middle digits reversed into chronological order, is a four-step path c to -x.
Every intermediate state is in D because an actual word from zero to c and a zero continuation from -x can be attached.

Conversely, let x,c in D satisfy(2) with legal four digits.
Choose actual finite paths x to zero and zero to c.
For any k at least both lengths, append zeros after the first path and prepend zeros before the second.
Reverse and negate the x-to-zero digits to get a length-k ascending tail with endpoint beta^k x; reverse the zero-to-c chronological digits for a length-k tail with endpoint c.
Together with the middle theta, their concatenation has polynomial value

    beta^k[x+theta+beta^4 c]=0.

Hence it is an actual returned word in the length2k+4 graph, and the edge persists at every larger k by symmetric zero padding.
Every q in D has arbitrarily long forward and backward core paths by attaching zero loops to a return/reachability word.
Taking a four-step portion proves that both vertex copies of q occur in the union.
This proves the claimed exact incidence identification, not a claim that irreducibility of K implies connectivity of its fixed-step bipartite incidence graph.

<a id="two-real-corner-construction"></a>
## 2. Infinitely many actual states near the opposite real boundaries

Set Delta=beta-beta^-1>0 and fix delta>0 so small that

    Delta delta^2<beta^-4.                              (3)

There are infinitely many nonzero w in O with |w_+|<delta and |w_-|<delta, with unbounded rho(w).
For completeness, the(N+1)^4 power-basis elements with coefficients in{0,...,N} have their two real coordinates in intervals of length O(N).
Partition these intervals into cells of fixed widths smaller than delta.
There are O(N^2) cells, so a fullest cell contains an unbounded number of distinct elements as N grows.
Subtract one element of that cell from the others.
The resulting distinct differences have both real magnitudes less than delta; their union is infinite.
If their neutral magnitudes were bounded, all four Minkowski coordinates would be bounded, contradicting discreteness of the original order lattice.
Nonzero field elements have nonzero values at either real embedding.

Define actual algebraic integers

    epsilon=(beta-beta^-1)w^2,
    c=B-epsilon,
    q_i=B-beta^i epsilon   (0<=i<=4),
    y=q_4, x=-y.                                       (4)

The square makes

    0<epsilon_+=Delta w_+^2<beta^-4,
    0<e:=-epsilon_-=Delta w_-^2<beta^-4<1.              (5)

Therefore c=q_0 is strictly inside the actual core, and every q_i is also in D:

    B-1<q_(i,+)<B,
    -S<q_(i,-)=-S+beta^-i e<-S+1=-B.                  (6)

For the first inequality use beta^i epsilon_+<1 when i<=4.
Since B>1 and S=B+1, both strips in(1) are strict.
No boundary state +/-B is included.

The identity beta B-1=B gives an actual legal four-step segment

    c=q_0 --(-1)--> q_1 --(-1)--> q_2
          --(-1)--> q_3 --(-1)--> q_4=y.              (7)

All four digits have their original probability1/4.
There are infinitely many distinct c: squaring a nonzero field element has at most the two preimages w and-w, while multiplication by beta-beta^-1 and translation by B are injective.
Their neutral radii are unbounded because

    rho(epsilon)=|zeta-zeta^-1| rho(w)^2,
    rho(c)>=rho(epsilon)-rho(B),                       (8)

and zeta is nonreal.

<a id="persistent-isolated-union-edges"></a>
## 3. The same edge is isolated from both sides forever

For0<=i<=3, equations(5) give

    q_(i,+)>B-beta^-1=b.

Thus L319's actual forced-digit argument makes-1 the ONLY legal next digit at every one of these four states.
Consequently the only four-step core endpoint from c is y, and the only such word is(-1,-1,-1,-1).

There is also a unique predecessor direction.
If a core state q has q_-<-B and a predecessor r=(q-eta)/beta is in D, then

    r_-=beta(q_--eta).

For eta=0 this is less than-beta B=-S; for eta=+1 it is smaller still.
Neither can lie in D.
In the segment(7), eta=-1 has the actual predecessor q_(i-1) in D, so it is the UNIQUE incoming digit at q_i for every1<=i<=4.
Working backward four times, the only core state with a four-step path to y is c, with that same unique word.

By Section1, the bipartite union therefore has the ISOLATED EDGE

    (x,c)=(-B+beta^4 epsilon, B-epsilon),
    theta=(-1,-1,-1,-1).                               (9)

Both its vertices have degree1 in the COMPLETE union, not just in one finite graph.
Its vertices are nonzero by(6), so this component is distinct from the component containing the all-zero edge.
The infinitely many c in Section2 give infinitely many distinct isolated components.
Global sign reversal gives their distinct sign partners.
No additional later word, representation or padding can attach an edge to either endpoint without contradicting one of the two real-strip uniqueness statements.

The true C170 midpoint on this component is

    Y=-beta^-2(x-1-beta)
      =beta^2 c-1-beta
      =B-beta^2 epsilon.                               (10)

Its expanding value is greater than B-beta^-2>0, so Y is nonzero.
Its neutral modulus is unbounded over this family by(8), since multiplication by beta^2 has neutral modulus1.
Every full returned word belonging to this endpoint edge has exactly this same midpoint.
The four-digit basis makes its middle word unique; no alternative middle word with the same endpoint is lost.

<a id="persistent-edge-actual-onset-and-cost"></a>
## 4. Actual finite appearance, all-late zero gap and original mass

Fix one of the constructed epsilon,c,x.
Choose original chronological words x to zero and zero to c of lengths l_x,l_c using the accepted L309 bound and reciprocal reversal.
Since rho(x)=rho(y)<=rho(c)+4 by(7), one may take

    l_x<=A_D(rho(c)+4)+B_D,
    l_c<=A_D rho(c)+B_D,
    k_* = max{3,l_x,l_c}.                              (11)

The construction of Section1 yields a returned word at EVERY k>=k_* and n=k+2, with middle four digits all-1.
Each chosen endpoint word has original probability at least4^-l_x or4^-l_c.
Appending/prepending zero digits supplies a completely explicit selected word of probability at least

    4^(-(l_x+l_c+4)) 2^(-(2k-l_x-l_c)).                 (12)

This is its UNCONDITIONAL original probability; division by the complete p_(2k+4) gives its conditional returned-word probability.
It is positive at every such length and is not treated as a fixed positive fraction of the whole law.

The full C170 word graph on this endpoint component is connected internally: keeping one complete tail allows resampling the opposite tail over all representations of its fixed endpoint, and the middle remains fixed.
Its two alternating conditional moves connect all choices of the two tail words.
It is therefore one actual closed positive-mass component of the full word chain, with nonzero constant midpoint(10).
The distinct all-zero component also has positive mass.
Hence C170's global spectral gap is EXACTLY ZERO for EVERY n>=k_*+2.
This refutes the eventual positive-global-gap premise for this specific b=2 operator, while leaving C170's conditional implication itself valid.

For the complete component mass, retain all tail representations and put

    a_k(x)=c_k(beta^k x), b_k(c)=c_k(c),
    S_k=c_(2k+4)(0), t_k=c_k(0)^2/S_k,
    M_(c,k)=a_k(x)b_k(c)/S_k.                          (13)

The middle weight is1, and isolation makes this edge its entire endpoint component.
Let q_x,q_c be the actual probabilities of the selected endpoint words.
The complete-count proof of L411 applies with these two fixed probabilities:

    q_x c_k(0)<=a_k(x)<=c_k(0),
    q_c c_k(0)<=b_k(c)<=c_k(0),
    q_x q_c t_k<=M_(c,k)<=t_k,
    1/(256D_k)<=t_k<=1/(16D_k), D_k=p_(2k)/p_k^2.       (14)

The lower bounds concatenate arbitrary original returns of the remaining length and use monotonicity of p_k; the upper bounds are complete binary autocorrelation.
All original endpoint multiplicities are retained.
The sign partner has exactly the same mass by digit symmetry.
The component indicator gives a zero-energy test, and the exact L409 defect chi is at least M_(c,k)(1-M_(c,k)); a union of both sign partners gives the further valid lower bound2M_(c,k)(1-2M_(c,k)).
No fixed lower bound approaching1/4 is inferred from these selected component masses.

<a id="persistent-carry-limits"></a>
## 5. Exact consequence for the weighted-carry direction

The union of actual normalized b2 graphs is NOT connected.
There are fixed actual returned words whose symmetric padding remains outside the zero component at every later length, and infinitely many isolated union components with nonzero unbounded midpoint values.
This is an all-late actual-core construction, not an extrapolation from J106 or the older six-digit frozen family.
The connected n8 seed and the eventual absorption of its particular early components in L409 remain correct: none of the isolated edges above can be in that connected seed.

L411's complete-fiber fixed-hub estimates remain valid on their own component, but no growth of that connected hub can absorb these isolated union edges.
A global-gap approach using exactly this fixed overlap is therefore unavailable.
L409's fixed-defect partial-path condition remains a separate possibility because it permits discarded original product mass and rare disconnected components.
Whether the total component-mass obstruction forces its defect to1/4, or whether a sufficiently large connected part carries the required mass with paid path loads, is not proved here.
The actual critical mean remains undetermined.
No new overlap, graph scan, critical-law surrogate or unrestricted Mahler-gap claim is supplied.

<a id="persistent-carry-inputs"></a>
## Exact input and author boundary

| Input | Exact role |
| --- | --- |
| [L170 exact return strip](Yin_C_G0400_v1.md#exact-salem-return-strip), [R69 strip review](../audits/reviews/Yin_R_G0069_v1.md#exact-strip-growth-review) | Actual equality with mutually reachable ORIGINAL states; explicit quartic applicability through L169 narrow co-return, strict boundaries and B in O. No beta<golden-ratio assumption. |
| [L309 all-core linear paths](../ledger/Yin_L_G0309_v1.md#quartic-full-core-linear-return), [R786](../audits/reviews/Yin_R_G0786_v1.md#weighted-tail-complete-independent-review) | Actual quartic A_D rho+B_D continuation, reciprocal reversal and all boundary/compact expenses, not an expected hitting-time estimate. |
| [L319 forced boundary](Yin_C_G0601_v1.md#actual-forced-boundary-segments), [R786](../audits/reviews/Yin_R_G0786_v1.md#forced-boundary-complete-independent-review) | Forward unique digit from the expanding strip and its exact b; the reverse uniqueness used here is proved directly from the stable strip. Original probabilities are not replaced by the critical Doob law. |
| [L316 lattice construction](Yin_C_G0599_v1.md#actual-tangent-core-states) | Full-order pigeonhole mechanism; the present two-real-coordinate use and signed square construction are written completely above. |
| [C170 exact carry graph](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix), [marks](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks), [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Actual b2 endpoint law, full tail-word fibers, unique four-digit basis, midpoint and component correspondence. This author contributed C170; R803 is the separate independent upstream finding. |
| [L409 nesting](Yin_C_G0514_v2.md#nested-normalized-carry-support), [component defect](Yin_C_G0514_v2.md#bulk-component-defect) | Normalized embeddings, exact least defect and its distinct fixed-defect condition; finite n8 connectivity is not extended to all vertices. |
| [L411 complete count comparison](Yin_C_G0519_v1.md#seed-complete-count-comparison), [original normalization](Yin_C_G0519_v1.md#seed-path-load-and-mass), [R416](../audits/reviews/Yin_R_G0416_v1.md#fixed-hub-whole-independent-finding) | Complete autocorrelation/concatenation bounds with fixed selected endpoint probabilities and exact t_k versus D_k; this author contributed L411 and reuses its independent review. |
| [C76 other endpoint paths](Yin_C_G0076_v1.md#statement), [C80 six-digit frozen family](Yin_C_G0080_v1.md#statement) | Different-operator comparisons only; no previously frozen family is transferred to b2. |

Root supplied only the question and subsequently requested verification of the exact already-read core premise; no new construction or proof step came from root.

No computation, new external theorem, actual mean classification, changed overlap or unrestricted gap is asserted.
