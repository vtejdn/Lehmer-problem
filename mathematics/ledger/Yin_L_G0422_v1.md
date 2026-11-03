---
author: Yin
---
# Degree-three neighbor rigidity and exclusion of small closed carry components

Current complete mathematical home: [C551](../claims/Yin_C_G0551_v1.md#statement), with [complete proof](../claims/Yin_C_G0551_v1.md#argument) and [actual current adoption](../claims/Yin_C_G0551_v1.md#decision-complete-current-self-adoption).
The current C owns the exact complete statement and full proof at this original account's scope.
The current whole [R743 finding](../audits/reviews/Yin_R_G0743_v1.md#current-g423-complete-self-finding) is constructor SELF.
The original proof, exploration limits, contributions, source/native facts and old review bindings remain preserved below; the current entry creates no retrospective old-R binding or independent finding.
Original author account date2026-10-18T17:19 and mechanical retention2026-10-18T17:26 are preserved as historical facts.

Date: 2026-10-18T17:19.
Human author Yin.
Root asks for a bounded structural discriminator for cyclic branching components after the low-degree and high-core results.
The entropy_attainment_bridge agent authors all new arguments below.
No carry-length scan, program, source acquisition or numerical estimate is used.

<a id="degree-three-fixed-inputs"></a>
## Actual graph and exact target of the screen

Use the same actual quartic P=t^4-t^3-t^2-t+1, exterior Salem root beta, B=1/(beta-1), S=beta B and O=Z[beta].
The two vertex copies are c and y in the ACTUAL core D={q in O:|q_+|<B,|q_-|<S}, with

    y=beta^4 c+theta,
    theta=eta_0+eta_1 beta+eta_2 beta^2+eta_3 beta^3.    (1)

Chronological time reads(eta_3,eta_2,eta_1,eta_0).
[L414](Yin_L_G0414_v1.md#union-carry-original-incidence) proves that this is the entire normalized b2 union, with one legal four-word per edge, actual original tails and finite appearance onsets.
[L419](Yin_L_G0419_v1.md#low-degree-exact-classification) supplies the exact degree<=2 thresholds and reciprocal J=beta^-1 iota symmetry.
The [L421 high-core argument](Yin_L_G0421_v1.md#one-low-neighbor) proves that every vertex has at most one neighbor of degree<=2 and that the induced graph on vertices of degree>=3 has minimum degree2.
Its complete independent review is [R432](../audits/reviews/Yin_R_G0432_v1.md#branching-core-whole-independent-finding), reused at that exact upstream scope.

All degrees mean COMPLETE-UNION degrees, not the currently visible finite-length degree.
The new statements are the exact degree3 threshold and neighbor shape, the impossibility of two degree3 vertices with identical neighbor sets, and the absence of every non-isolated FINITE union component on at most7 vertices.
They do not rule out larger finite components, prove uniqueness of an infinite component or bound the full original component defect.

<a id="degree-three-threshold"></a>
## 1. Three-neighbor states are an exact narrow fringe

First note the actual quartic root satisfies

    beta^2<3, beta+1<2B.                              (2)

Indeed P(sqrt3)=7-4sqrt3>0, since49>48.
The accepted Salem root description gives the only root above1 as beta and P(t)<0 for1<t<beta, while sqrt3>1.
Thus beta<sqrt3, and multiplying beta+1<2/(beta-1) by beta-1 shows it is equivalent to beta^2<3.
No approximate root is used.
The accepted17/10<beta<18/10 also gives B>1 and beta>1.

Call a chronological state central when |q_+|<b0=B/beta.
It then has at least two legal successors.
If there are exactly two, L419 proves that they differ by1 and at least one is central, since two forced states cannot have that spacing.
If there are three, their middle successor has expanding value beta q_+, with |beta q_+|<B-1<b0, and is central too.
Thus every branching state has a central successor, and a branch can be followed by a further branch at every remaining step.
All other prefix words also have a legal continuation, since every core state has a successor.
If the first branching occurs at chronological step j<=2, there are therefore at least6-j>=4 distinct completed four-words.
They cannot coalesce as endpoints because the four powers in(1) are linearly independent.
Consequently a degree-at-most3 outgoing vertex must have its first TWO steps forced.

By sign reversal assume these forced digits are negative, so c_+>0.
Write c_+=B-epsilon with epsilon>0.
Two forced steps are equivalent to epsilon<beta^-2, using the exact forced-region threshold and q_i=B-beta^i epsilon.
Put

    r=beta^4 epsilon, 0<r<beta^2,
    T=1+beta+beta^2+beta^3.                            (3)

The first two chronological digits contribute the fixed high powers-beta^3-beta^2.
Changing either of the last two digits from-1 to0 or+1 gives precisely the increments

    V={0,1,2,beta,beta+1,beta+2,
                         2beta,2beta+1,2beta+2}.

Each candidate has y_+=B-r+v.
By the actual-core incidence theorem, it is legal exactly when r-2B<v<r; the stable strip is preserved by every digit and no intermediate core constraint is lost.

If0<r<2, the lower bound is negative because2B>2.
The legal increments are respectively{0}, {0,1}, {0,1,beta} as r lies in(0,1),(1,beta),(beta,2).
At r=1,beta,2 the putative c is B-beta^-4, B-beta^-3, B-2beta^-4 respectively; each has stable coordinate below-S and is absent from D.

If2<r<2B, the four increments0,1,beta,2 are all legal.
If2B<=r<beta^2, the four increments1,beta,2,beta+1 are all legal: beta+1<2B<=r, and r-2B<beta^2-2B<1 by beta^2<3 and B>1.
These two cases cover all r>2 in(3), including r=2B without a threshold omission.
Hence

    deg(c)<=3 iff |c_+|>B-2beta^-4,
    deg(c)=3 iff B-2beta^-4<|c_+|<B-beta^-3.            (4)

There is no additional degree3 central case, by the first-branch argument.
Both endpoints of the displayed interval are absent from D by the same explicit stable-coordinate check.

<a id="degree-three-distinct-neighborhoods"></a>
## 2. Degree-three vertices cannot have identical neighbor sets

For a positive degree3 vertex c, its ENTIRE neighbor set is

    {beta^4 c-T, beta^4 c-T+1, beta^4 c-T+beta}.         (5)

For a negative degree3 vertex it is the global sign reversal of such a set.
In expanding order, the gaps of(5) are(1,beta-1), while the negative case has gaps(beta-1,1).
Because beta!=2 these patterns are distinct.
Two positive degree3 vertices with identical neighbor sets have the same least expanding neighbor and hence the same c.
The negative case similarly uses the greatest neighbor.
An opposite-sign pair cannot have identical sets because the ordered gap patterns differ.
Thus no two DISTINCT outgoing vertices of degree3 have the same full neighbor set.
The reciprocal graph involution c--y -> J y--J c gives exactly the same assertion for incoming degree3 vertices.
This is a statement about the complete sets, not about two vertices sharing one or two neighbors.

<a id="small-closed-component-exclusion"></a>
## 3. Every non-isolated finite closed component has at least eight vertices

Let C be a finite complete union component distinct from an isolated edge.
Partition it into H vertices of union degree>=3 and L vertices of degree<=2.
The preceding high-core theorem gives a nonempty induced graph on H with minimum degree2; hence its bipartition has at least2 vertices on each side and |H|>=4.
Suppose |C|<=7.

If |H|=4, its induced graph is K_(2,2).
Each H vertex has two H neighbors, needs at least one low neighbor to reach degree3, and has at most one such neighbor.
Thus there are exactly four H--L incidences, two at either high bipartite side.
If |L|<=2, at least two low vertices are necessary and both must have degree2, with no edge between them.
Each low vertex connects two H vertices of the same side, so one low vertex joins both high c vertices and the other joins both high y vertices.
The high c vertices then have degree3 and identical three-neighbor sets, contradicting Section2.
If |L|=3, its induced graph has either no edge or one edge, by L419.
With one low--low edge, four H--L incidences force all three low vertices to have degree2.
The low pair then supplies one high port of each side, whereas the low singleton supplies two high ports on just one side.
The resulting high-port counts are(3,1) or(1,3), contradicting the required(2,2).
With no low--low edge, the low degrees must be(2,1,1).
The degree2 low vertex joins both high vertices of one side, again making those two degree3 high vertices have identical neighborhoods.
This exhausts |H|=4.

If |H|=5, its bipartition has sizes2 and3, and minimum degree2 forces K_(2,3).
Each of the three high vertices on the larger side needs a low neighbor to reach total degree3.
Here |L|<=2, and fewer than two low vertices cannot supply the three required ports.
An edge between the two low vertices leaves at most two H--L incidences and cannot supply the three required ports.
Without such an edge, both low vertices must be on the side opposite those three high vertices, because one low vertex supplies at most two ports and no vertex connects across both bipartite sides.
At least one low vertex connects two of the three high vertices.
Those two high vertices each have degree3 and the same two H neighbors plus that low neighbor, contradicting Section2.

If |H|=6, then |L|<=1.
A high bipartition of sizes2 and4 would force K_(2,4), requiring four low ports on the larger side, impossible with one low vertex.
For parts3 and3, minimum degree2 says the induced high graph is K_(3,3) minus a matching.
Any missing edge leaves a degree2 high endpoint on BOTH sides, each needing a low neighbor.
One low vertex cannot connect to both sides, so there are no missing edges.
The induced graph is K_(3,3).
Whether the low set is empty or consists of one vertex, all three high vertices on at least one side receive no low neighbor; they have degree3 and identical high neighborhoods.
This again contradicts Section2.

If |H|=7, the low set is empty and every total degree is at least3.
Its bipartition must have sizes3 and4; each vertex on the four-vertex side connects to all three vertices of the other side.
Thus it is K_(3,4), and four degree3 vertices have identical neighbor sets, impossible.
There are no other H sizes under |C|<=7.
Therefore

    every finite union component is either an isolated
    edge or has at least8 vertices and a cycle in H.   (6)

This is an analytic exhaustion of the stated small COMPONENT domain, not a scan over carry lengths or original words.
A larger complete component may contain any of these configurations as a nonclosed subgraph; they are not forbidden merely as subgraphs.
No assertion is made that an eight-vertex closed component exists.

<a id="small-component-original-law-boundary"></a>
## 4. Original-law scope and the remaining problem

Every vertex and edge above belongs to the actual order and the two open real strips.
For a finite union component, L414's finite edge onsets can be maximized, so the whole component appears and remains closed in every later sufficiently long normalized endpoint graph.
C170 then identifies its whole original returned-word component with all conditional tail fibers, not merely one chosen representative word.
Thus(6) excludes genuine persistent finite components at the stated size, without claiming anything about accidental small components that later acquire new neighbors.
In particular finite n5--7 J106 components are not contradicted: they were never known to be closed in the entire union.

For any hypothetical larger component, its exact original mass is still the full sum in the preceding high-core argument, with denominator c_(2n)(0) and all endpoint multiplicities and middle zero-digit weights.
No new component is constructed here, so there is no new positive component-mass lower certificate.
The existing8/13 original mass on H--H edges does not force one H component to carry that mass and does not bound full chi.
The true midpoint bound D_(n,2)<=4 and digit-work divisor n+2 remain unchanged.
The global cyclic-closure question and the uniform weighted-energy question remain separate.

The first remaining finite candidate has at least8 vertices and must have a genuine high-degree cycle, every extra legal four-word neighbor, and complete closure in both real strips.
A finite diagram satisfying abstract degree constraints alone is not an actual arithmetic candidate.
No further size enumeration, graph-length experiment or parameter box is authorized or run by this draft.

<a id="degree-three-inputs"></a>
## Exact inputs and author check

| Input | Actual role |
| --- | --- |
| [L414 actual incidence](Yin_L_G0414_v1.md#union-carry-original-incidence) | Full original four-step graph, exact two-strip core, finite onsets and reciprocal reversal. |
| [L191 quartic root proof](Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Actual quartic has one exterior root above1 and its remaining roots on the circle or reciprocal inside; used for beta<sqrt3, not a numeric approximation. |
| [L419 degree input](Yin_L_G0419_v1.md#low-degree-exact-classification), [R428](../audits/reviews/Yin_R_G0428_v1.md#low-degree-carry-whole-independent-finding) | Exact branching/central/degree<=2 input and independent upstream review; this author contributed L419. |
| [L421 high-core theorem](Yin_L_G0421_v1.md#branching-core-topology), [R432](../audits/reviews/Yin_R_G0432_v1.md#branching-core-whole-independent-finding) | Every vertex has at most one low neighbor, induced H minimum degree2 and full original mass boundaries; reused at its independently reviewed fixed scope. |
| [C170 full law](../claims/Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix), [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Four-word uniqueness, complete original fibers and unchanged midpoint/clock costs; no new native run or independent reproof claimed. |

The complete original author SELF finding is retained at [R743](../audits/reviews/Yin_R_G0743_v1.md#original-g423-v1-author-self-finding).
All new arguments are authored by entropy_attainment_bridge; root supplied the bounded question only.
