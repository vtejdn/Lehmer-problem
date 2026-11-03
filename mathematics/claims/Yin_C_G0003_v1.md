---
author: Yin
---

# Triangle-free Stokes rigidity and a sharp one-unit five-cycle surgery

Date: 2026-10-10T14:17.
Human author: Yin.
Provenance: project deduction.

Context: [G0001](../tasks/Yin_T_G0001_v1.md), presently paused.
The user requested completed drafts to be placed in the material area matching their role.
This is result organization, not renewed exploration or a change to that Task decision.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:17 |
| status | open |
| reason | Complete historical argument extracted for precise registration; current extraction-interface review and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the explicitly enumerated conclusions and hypotheses. |
| argument | [Argument](#argument) | The selected completed derivations retained below; speculative and computational-history passages are excluded as proof premises. |
| dependency | [Stokes mutations and energy](Yin_C_G0002_v1.md#mutation-and-energy) | Both current-entry adjacent transformations, full determinant preservation and the exact energy differences. |


### Decision organized-reviewed
| Field | Value |
| --- | --- |
| date | 2026-10-10T14:24 |
| status | proved |
| reason | The precisely enumerated completed results have unchanged complete historical arguments and reviews; the fixed extraction finding checks the new statement and actual dependency interfaces. Original conjectures, finite discovery statistics and unchecked source generalizations are excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exactly the enumerated parts with all their separate hypotheses and exclusions. |
| argument | [Argument](#argument) | The complete selected retained derivations, with their explicit supporting inputs and historical review boundaries. |
| dependency | [Stokes mutations and energy](Yin_C_G0002_v1.md#mutation-and-energy) | Both current-entry adjacent transformations, full determinant preservation and the exact energy differences. |
| review | [Extraction finding](../audits/reviews/Yin_R_G0001_v1.md#c3-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |

## Statement

Use the integral upper unitriangular matrices, \(p_V\), \(E(V)\), two adjacent mutations and sign-switchability of [C G0002](Yin_C_G0002_v1.md#statement).
Only those adjacent mutations and diagonal sign changes are allowed below.

**A. Sign quotient.**
Fix a deterministic spanning forest of the support graph.
Making all forest edges negative, with root sign one in each component, gives a unique matrix representative of each sign-equivalence class.
Both mutation directions are equivariant modulo signs.
Thus a component closed under all allowed nonincreasing neighbors in the normalized graph excludes a nonincreasing escape from its represented states.

**B. Triangle-free rigidity.**
If all strictly upper entries of \(V\) belong to \(\{0,\pm1\}\) and the simple support graph is triangle-free, every path whose energy is nonincreasing at each step preserves its signed graph up to vertex permutation and vertex sign changes.
In particular a nonswitchable \(V\) cannot reach a switchable presentation along such a path.
For an adjacent nonzero entry the two energy differences are \(\deg(i+1)-1\) and \(\deg(i)-1\).

**C. Sharp barrier for a specific Lehmer presentation.**
For the literal ten-dimensional matrix specified by all ten signed edges in [the witness](#lehmer-unit-barrier), \(p_V=L(t)\) as defined in C G0002 and \(E(V)=10\).
The smallest possible maximum energy above its starting energy among allowed paths to a switchable presentation is exactly one.
The forward \((1,2)\), forward \((2,3)\), inverse \((3,4)\) path has energies \(10,11,11,9\), ends at the stated \(Y_{2,3,7}\) tree, and a final diagonal sign change makes every edge negative.

**D. Five-cycle surgery with arbitrary right attachments.**
Take exactly the integer \(4\times4\) matrices \(A,P\) displayed in [the block construction](#five-cycle-surgery).
For every \(r\ge1\), every integral upper unitriangular \(r\times r\) matrix \(B\), every standard coordinate vector \(e\in\mathbb Z^r\), and every \(b\in\mathbb Z^r\) with \(e^Tb=0\), put
\[
 R=\begin{pmatrix}-e^T\\0\\0\\-e^T+b^T\end{pmatrix},\qquad
 V=\begin{pmatrix}A&R\\0&B\end{pmatrix},\qquad Q=\operatorname{diag}(P,I_r).
\]
Then \(W=Q^TVQ\) is integral upper unitriangular, \(p_W=p_V\),
\[
 P^TR=\begin{pmatrix}0\\0\\b^T\\-e^T\end{pmatrix},\qquad E(W)=E(V)-1.
\]
The same three moves have intermediate energies relative to the starting value \(+1,+1,-1\).
The assertion imposes the displayed front-block condition; arbitrary earlier-vertex couplings are not covered.

Finite sample frequencies, exhaustive classification of the original 66 inputs, universal energy barriers, scalar representation coverage and global compression are excluded.

## Argument

The proof is the retained complete direct argument (1)--(7).
Its only nonlocal mathematical interface is C G0002's exact mutation and energy calculation, now fixed without changing those formulas.
The literal witness and path remain fully displayed.
J G0017 retains computational records; the structural all-parameter proof does not extrapolate from a finite test size.
FW24 is method attribution, not an orbit theorem premise.
The later L G0184 extends the surgery; it is downstream, not used to prove this earlier scope.
Historical plans partly fulfilled there remain dated history.

### Organization and extraction provenance

The entire text of Yin_D_G0012 dated 2026-10-09 is retained below, including its original title, derivations, equation labels, historical reviews, failed attempts, source boundaries and open questions.
Only heading depth and relocated link targets change.
Its historical statements that adoption was outstanding describe that date; the explicit Current assessment above owns the present judgment.
The source draft is extraction ancestry, not a mutable proof dependency.
Open questions and historical future plans remain historical/exploratory and do not authorize execution while G0001 is paused.
Programs and native certificates remain in their J homes.

### G0001: plateau Stokes descent and reflection-lattice structure

Date: 2026-10-09.
Authoring agent structural_research for Yin.
Rolling exploratory draft under the resumed G0001 execution; the later local review is recorded below.
This is not a fixed adopted result.

#### Question and starting scope

Continue the exact mutation mechanism in [D G0009](Yin_C_G0002_v1.md) without changing that material during independent review.
First determine whether the 66 retained nonswitchable Lehmer terminals in [J G0016](../computations/programs/Yin_J_G0016/readme.md) admit nonincreasing-energy mutation paths to switchable presentations, with explicit bounds and checked paths.
Then identify a structural invariant or reduction mechanism worth developing beyond this known determinant orbit.
General Stokes representation and neutral-stabilization coverage remain open.

#### Reuse and initial status

Reuse the exact mutation formula and its determinant preservation from D G0009, whose full formulas were reread.
That draft owns the source search identifying Fan--Whang's integral Stokes braid action; no claim of a new formalism is made.
The new experiment starts from retained literal matrices, does not require their discovery walks, and does not assume that a failed bounded search proves an energy barrier.
Computation and derived findings will be recorded here.

<a id="round-result"></a>
#### Result of this bounded round

The plateau extension succeeds on 44 of the 66 retained nonswitchable Lehmer matrices.
The remaining outcomes are 15 completely explored plateau components and 7 explicit node-cap stops.
These facts do not alone decide whether a different earlier decreasing move could succeed for an original input.

One closed component has a useful explanation that is independent of enumeration: a triangle-free simple signed graph cannot change its signed-graph isomorphism class under any nonincreasing-energy path made from adjacent Stokes mutations and diagonal sign changes.
A concrete Lehmer presentation of energy 10 therefore needs a temporary increase.
An exact three-move path has energies 10,11,11,9 and ends at the usual Y_(2,3,7) tree.
Its minimum necessary increase is exactly one.

The path extends to a local block identity with arbitrary integral attachments.
It removes one unit of energy from a frustrated five-cycle configuration while preserving the entire characteristic polynomial, but necessarily passes through energy one unit higher on the isolated triangle-free control.
This supplies a concrete additional reduction move rather than a stopping condition for the geometric route.

All mathematics here is authoring-agent derivation, with its self-check and the later separately organized local review below.
[J G0017](../computations/programs/Yin_J_G0017/readme.md) retains inputs, paths, closed-component data and a separately implemented dense verifier written by the same agent.
No Claim adoption is asserted.

<a id="operations-and-gauge"></a>
#### Operations and exact quotient by sign changes

For an integral upper unitriangular n by n matrix V, write p_V(t)=det(tV+V^T) and E(V)=sum_(i<j)V_ij^2.
At a=V_i,i+1 the forward pair change is Q(a)=[[0,1],[1,-a]] and the inverse pair change is [[-a,1],[1,0]].
Both act by integral congruence and keep the result upper unitriangular.
The displayed p_V, including all eigenvalue multiplicities, is preserved.
These are the Stokes transformations attributed in [FW24, section 5.1](../literature/pdf/FW24.pdf); the exact convention and elementary proof are in [D G0009](Yin_C_G0002_v1.md#mutation-and-energy).
No external orbit-finiteness theorem is needed.

The sign operation V->DVD uses a diagonal D with entries plus or minus one and also preserves E and p_V.
The search normalizes signs by taking a deterministic spanning forest of the graph of nonzero entries and making every forest edge negative.
The root sign is fixed to one in each connected component.
This gives a unique representative of a sign-equivalence class once the deterministic forest is fixed: two compatible vertex-sign choices differ only by a global sign on each component, which acts trivially on V.

This quotient does not omit mutation transitions.
Start with a signed basis (d_i e_i).
If its adjacent entry is a'=d_i d_(i+1)a, the forward new pair is

\[
 (d_{i+1}e_{i+1},\ d_i(e_i-ae_{i+1})).                    \tag{1}
\]

It is the original forward-mutated pair with the two signs exchanged.
The same calculation holds for the inverse.
Hence mutation is equivariant modulo signs.
Energy and switchability are sign invariant.
A closed component in the normalized graph is consequently sufficient to exclude nonincreasing escape from its represented states, provided all admissible neighbors were actually checked.

Here switchable means sign-equivalent to a matrix with nonpositive strict upper entries.
For a simple signed graph, the condition on a cycle of length l is that its edge-sign product equals (-1)^l.

<a id="triangle-free-rigidity"></a>
#### Triangle-free support forces an actual energy barrier

**Local assertion.**
Suppose every strict upper entry of V is 0,1 or -1 and its underlying simple graph contains no triangle.
Every path of adjacent mutations and diagonal sign changes with nonincreasing E preserves the signed graph up to vertex permutation and vertex sign changes.
In particular, if V is nonswitchable, such a path cannot reach a switchable presentation.

**Proof.**
Diagonal sign changes already have the asserted property.
If a=0, an adjacent mutation is just the interchange of the two basis vectors, so it relabels the graph.
Suppose a=plus or minus one.
Use the external neighbor vectors x,y of the adjacent vertices as in D G0009.
A common external neighbor would form a triangle, so their supports are disjoint and <x,y>=0.
Their squared norms are deg(i)-1 and deg(i+1)-1.
The exact energy changes are therefore

\[
 E(\mu_iV)-E(V)=\deg(i+1)-1,\qquad
 E(\mu_i^{-1}V)-E(V)=\deg(i)-1.                           \tag{2}
\]

Both are nonnegative.
Equality in the forward direction means i+1 is a leaf.
The neighbor-pair replacement (x,0)->(0,x) interchanges the leaf and its neighbor; the sign of their common edge reverses, which is undone by a sign change at the new leaf.
Thus the resulting signed graph is isomorphic up to vertex signs to the original.
The inverse equality case is identical with the endpoints reversed.

A nonincreasing step can therefore only have zero energy change and preserves the signed-graph class.
It remains simple and triangle-free, so the argument applies inductively to every subsequent step.
This proves the assertion.
There is no degree bound, positivity assumption or Mahler-measure hypothesis.
The statement concerns these specific adjacent mutations and sign changes, not arbitrary integral congruences or neutral stabilization.

The proof uses the previously derived exact local energy formula, which supplies the needed conclusion without further source searching.
No novelty claim for signed-graph or Stokes theory is made.

<a id="lehmer-unit-barrier"></a>
#### A sharp one-unit barrier at the actual Lehmer polynomial

Let V be the ten-dimensional upper unitriangular matrix whose nonzero strict upper entries are specified by these signed edges, using one-based vertex numbers:

```text
(1,2,-1) (1,6,-1) (2,3,-1) (3,4,+1) (4,5,-1)
(4,6,-1) (5,7,-1) (7,8,-1) (8,9,-1) (9,10,-1).
```

Thus E(V)=10.
The only cycle is 1-2-3-4-6-1, of length five and sign product plus one; hence the matrix is triangle-free and nonswitchable.
Its exact polynomial is

\[
 p_V(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1=L(t).          \tag{3}
\]

This determinant was checked directly in J G0017 and is also preserved along the retained path from J G0016 source trial 75.
Since E is integer valued, the preceding local assertion forces any path of the specified operations from V to a switchable presentation to visit E>=11.

There is an explicit path attaining this lower bound: apply the forward moves at pairs (1,2) and (2,3), followed by the inverse move at (3,4).
The energy sequence is

\[
 10\longrightarrow11\longrightarrow11\longrightarrow9.  \tag{4}
\]

The resulting graph is a tree with edges 1-2,2-4,3-4,3-5,4-6,5-7,7-8,8-9,9-10.
A final sign change at vertices 1 and 2 makes all entries negative.
Its center 4 has branch lengths 1,2,6, so this is the ordinary Y_(2,3,7) presentation with exactly the same polynomial.
The minimum required energy increase from this particular V is therefore one.

The normalized nonincreasing component containing V has 50 states.
The dense verifier checked all 314 admissible directed transitions in that stored component, including their closure modulo signs, and confirmed that none is switchable.
This independently implemented finite check supports the structural proof but is not an independent-agent review.
The three-move excursion search found the path after discovering 77 states with energy ceiling 11; a 30000-node cap had been specified and was not approached.

<a id="five-cycle-surgery"></a>
#### An exact five-cycle surgery with arbitrary attachments

The short path is an all-parameter block operation.
Set

\[
 A=\begin{pmatrix}
 1&-1&0&0\\0&1&-1&0\\0&0&1&1\\0&0&0&1
 \end{pmatrix},\qquad
 P=\begin{pmatrix}
 0&0&-1&1\\1&0&-1&1\\0&1&-1&1\\0&0&1&0
 \end{pmatrix}.
\]

Let B be any integral upper unitriangular r by r matrix, r>=1.
Let e be a standard coordinate vector in Z^r and b any integral vector with e^T b=0.
Form

\[
 V=\begin{pmatrix}A&R\\0&B\end{pmatrix},\qquad
 R=\begin{pmatrix}-e^T\\0\\0\\-e^T+b^T\end{pmatrix}.   \tag{5}
\]

The first four vertices and the distinguished e-vertex form the signed five-cycle just used.
B and b may contain arbitrary integer entries; no tree, bounded support, positivity, irreducibility or small-measure assumption is imposed on the rest.

The three adjacent moves from (4) have pair entries a=-1,-1,+1 and composite basis change P on the first four coordinates.
Direct multiplication gives

\[
 A'=P^TAP=
 \begin{pmatrix}
 1&-1&0&0\\0&1&0&1\\0&0&1&-1\\0&0&0&1
 \end{pmatrix},\qquad
 R'=P^TR=\begin{pmatrix}0\\0\\b^T\\-e^T\end{pmatrix}. \tag{6}
\]

Since P is unimodular, W=diag(P,I_r)^T V diag(P,I_r) satisfies p_W=p_V.
Both matrices are upper unitriangular.
The four-dimensional core has three coefficient units before and after the operation.
Because e^T b=0,

\[
 \|R\|_F^2=2+\|b\|^2,\qquad
 \|R'\|_F^2=1+\|b\|^2,
 \quad E(W)=E(V)-1.                                    \tag{7}
\]

The intermediate excesses relative to E(V) are +1,+1,-1.
This follows either by the individual neighbor replacements or by multiplying the first one and first two pair changes in (5); the arbitrary b and B contributions remain equal at each stage.
The first two steps only move the rows containing -e, and the last step transfers the b row without duplicating it.

Thus the displayed local pattern admits an exact determinant-preserving reduction of one energy unit with an intermediate increase of one.
When the outside data are the simple tail in (3), the pattern becomes the familiar D5-shaped tree with that tail attached.
For general B,b the operation need not remove every cycle or make the complete presentation switchable.
It is a usable local surgery under its explicit block hypothesis, not a universal compression theorem.
An internal occurrence with earlier-vertex couplings would need those couplings accounted for separately; no such broader extension is asserted here.

J G0017 checks the block products and intermediate energy identities symbolically with b=(0,u,v) and a fully variable three-dimensional unitriangular B.
The displayed arbitrary-r argument, rather than extrapolation from that test size, proves (5)--(7).

<a id="experiment-scope"></a>
#### Bounded search and its actual interpretation

The input is exactly the 66 nonswitchable terminal matrices in J G0016's retained results.
The new search uses exact integer tuples, the deterministic spanning-forest sign gauge, and a breadth-first search at each current energy level.
It stops at the first strict decrease or switchable matrix, then repeats if a decrease was found.
Each level permits at most 4000 discovered normalized states; a path permits at most 12 such segments.
When the state cap is reached, the existing queue is still processed but any discarded new neighbor marks the result inconclusive.
This prevents a truncated frontier from being reported as a closed component.

The completed output has 44 switchable endpoints, 15 fully explored terminal plateaus and 7 capped searches.
The 44 successful paths have at most nine moves in this run and end at E=9.
There are 74307 discovered states over all search segments.
The separate dense verifier replayed all 261 recorded mutations across the 66 inputs, including partial paths, checked full accumulated integral congruence and nonincreasing energy, and checked p_V=L for every initial input.

Some of the 15 closed components are reached after selecting an earlier strict descent.
Closure at that endpoint does not exclude a different nonincreasing path from the original input.
In particular, neither those counts nor the seven node caps are classified as 22 proved initial-input barriers.
The explicit example (3) is itself a valid new starting presentation and has the separately proved exact barrier.

The search is a mechanism test on a known Lehmer determinant orbit.
It does not test coverage of arbitrary small-Mahler polynomials, count braid orbits, or give an asymptotic probability of successful reduction.

<a id="next-direction"></a>
#### Consequence and next direction

The useful change is to organize a search by exact local surgeries with an explicitly bounded temporary cost.
Nonincreasing adjacent energy is too rigid even for a presentation already known to reduce to a Lehmer tree.
Formula (5) supplies one macro move that a next implementation can recognize directly instead of rediscovering it through a large mutation graph.
More general frustrated cycles and their attachment patterns are a natural next mathematical test, but no uniform bound on the number or height of required excursions is conjectured as established.

Optimized cover cost and scalar representation coverage remain separate.
The new surgery changes a presentation of a given polynomial; it does not produce an integral Stokes presentation for an arbitrary reciprocal polynomial.
No additional realization theorem was selected in this round.

The broad possibility of low-cost Stokes representation after controlled neutral stabilization remains open for exploration.
The present result gives a concrete way to improve some existing presentations and a precise warning about a natural monotonicity assumption, while preserving the Task's unrestricted scope.

#### Verification and source-intake boundary

All three programs in J G0017 completed with Python 3.12.14 and the dense/symbolic verifier used SymPy 1.14.0.
No floating-point root finding was used.
The triangle-free assertion, sign equivariance and block surgery were self-reviewed directly.

During this round the three D G0009 sources McM02, dlP19 and FW24 were acquired through the framework registration command, with pre-acquisition identity checks and the shared bibliography/registry lock.
Their publisher PDFs were validated, title pages rendered and inspected, and edition/inspection facts added to the sole registry.
FW24's retained title page explicitly says corrected publication 2024; the separate correction and source proof remain uninspected.
These acquisitions do not expand D G0009's source-adoption scope.
D G0009 and J G0016 were kept read-only while the coordinator reviewed them.

#### Separately organized local review

At 2026-10-09T15:32 the coordinating AI for Yin separately reviewed the complete direct argument (1)--(7), the concrete witness and the dense verification code.
It checked sign equivariance and canonical sign classes; the absence of common neighbors and both leaf equality cases in the triangle-free proof; preservation of the class under iteration; the actual five-cycle and tree; the lower/upper bounds proving the sharp one-unit barrier; and the arbitrary-r block identity, orthogonality e^T b=0 and unchanged outside contributions at all three steps.
It found no mathematical defect at the stated operation and attachment scope.

The reviewer had assigned the plateau experiment and received author progress explanations, but had supplied none of the displayed rigidity proof, witness or surgery derivation.
It reran the author's dense verifier successfully under Python 3.12.14/SymPy 1.14.0: 261 saved mutations, 44 successful paths, all 314 nonincreasing neighbors of the selected 50-state component, and the symbolic surgery checks passed.
This is a separate execution and code inspection of the author's verifier, not a third implementation or a rerun of the full discovery search.
It does not independently certify every search statistic or re-audit FW24.
The review retains all seven cap outcomes and the distinction between endpoint closure and original-input impossibility.
It is an exploratory local review, not a fixed acceptance finding or a Claim/Task decision.
