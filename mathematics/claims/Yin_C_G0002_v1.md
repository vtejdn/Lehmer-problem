---
author: Yin
---

# Integral Stokes covers, mutation energy and unbounded presentation cost

Date: 2026-10-10T14:16.
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
| date | 2026-10-10T14:16 |
| status | open |
| reason | Complete historical argument extracted for precise registration; current extraction-interface review and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the explicitly enumerated conclusions and hypotheses. |
| argument | [Argument](#argument) | The selected completed derivations retained below; speculative and computational-history passages are excluded as proof premises. |


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
| review | [Extraction finding](../audits/reviews/Yin_R_G0001_v1.md#c2-extraction) | Exact current statement and argument interfaces; relies on unchanged historical mathematical reviews at their preserved scopes. |

## Statement

For an integral upper unitriangular \(n\times n\) matrix \(V\), put
\[
 p_V(t)=\det(tV+V^T),\quad E(V)=\sum_{i<j}V_{ij}^2,\quad
 (V^-)_{ii}=1,\quad(V^-)_{ij}=-|V_{ij}|\ (i<j).
\]
Write \(m(p)\) for the full unnormalized logarithmic Mahler measure and \(M(p)=e^{m(p)}\).
A sign-switchable matrix is one made nonpositive above the diagonal by a diagonal matrix of signs.

**A. Two-sheet cover.**
The integral upper unitriangular \(2n\times2n\) matrix \(W\) defined in [the cover construction](#signed-cover-identity), with diagonal blocks \(I_2\), block \(aI_2\) for \(a=V_{ij}\le0\), and block \(-aS\) for \(a>0\), where \(S\) swaps two coordinates, satisfies
\[
 p_W=p_{V^-}p_V,\qquad m(p_W)=m(p_{V^-})+m(p_V).
\]
Here \(p_V\) is monic integral reciprocal with constant coefficient one; if \(V\) is sign-switchable then \(p_{V^-}=p_V\).

**B. Adjacent mutation.**
At \(a=V_{i,i+1}\), the two allowed basis changes have blocks
\[
 Q_+(a)=\begin{pmatrix}0&1\\1&-a\end{pmatrix},\qquad
 Q_-(a)=\begin{pmatrix}-a&1\\1&0\end{pmatrix}.
\]
Their congruences preserve upper unitriangularity and the full \(p_V\).
For the external coupling vectors \(x,y\) defined in [the energy calculation](#mutation-and-energy),
\[
 \Delta E_+=a^2\|y\|^2-2a\langle x,y\rangle,\qquad
 \Delta E_-=a^2\|x\|^2-2a\langle x,y\rangle.
\]

**C. Dense neutral controls.**
For \(V_n\) with every strictly upper entry equal to one, the displayed integral basis change gives the negative superdiagonal chain \(C_n\), and
\[
 p_{V_n}=p_{C_n}=1+t+\cdots+t^n,\quad m(p_{C_n^-})=0,\quad
 \operatorname{tr}T_{V_n^-}=2^n-2n-1,\quad
 M(p_{V_n^-})\ge(2^n-2n-1)/n\longrightarrow\infty,
\]
where \(T_U=-U^{-1}U^T\).
No assertion that this particular congruence is a braid word is included.

**D. A literal strict-descent trap.**
The complete five-dimensional matrix \(U\) in [the plateau control](#rank-five-plateau) has \(E=5\), \(p_U=1+t+\cdots+t^5\), and no strictly decreasing adjacent mutation.
It is not sign-switchable and \(m(p_{U^-})>0\).
The stated two forward mutations give energies \(5,5,4\) and end at a sign-switchable chain.

**E. Fixed-degree unbounded cost.**
For the complete ten-dimensional \(V_0\) in [the fixed-degree witness](#fixed-degree-unbounded-cover), let \(V_k\) be obtained by \(2k\) forward mutations at positions \((2,3)\), \(k\ge0\).
Then
\[
 p_{V_k}=L(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1,
\]
\[
 (u_k,v_k)=(2,-4)\begin{pmatrix}1&-3\\3&-8\end{pmatrix}^k,\qquad
 u_{k+2}=-7u_{k+1}-u_k.
\]
The displayed coupling gives \(E(V_k)\to\infty\), while
\[
 M(p_{V_k^-})\ge(E(V_k)-10)/10\longrightarrow\infty.
\]
This concerns arbitrary presentations of the same polynomial, not the minimum cost within a mutation orbit.
No irreducibility assertion is required for this statement.

The finite random sample, universal scalar coverage, optimized cover cost and global descent conjectures are not conclusions of this Claim.

## Argument

Parts A--E are the complete direct determinant, matrix, energy, recurrence and root-sum arguments (1)--(8) retained below.
There is no external Coxeter gap premise.
McM02, dlP19 and FW24 retain their stated attribution/reuse boundaries.
The historical irreducibility reference to L G0033 is additional context, not a premise of the exact fixed-polynomial assertion.
Native computations stay in J G0016.
The original local review checked the written argument; its separate finite Bareiss checks and its unrerun random discovery sample retain their distinct scopes.
Later L G0230 strengthens a cost bound; it is a descendant, not a dependency of this Claim.

### Organization and extraction provenance

The entire text of Yin_D_G0009 dated 2026-10-09 is retained below, including its original title, derivations, equation labels, historical reviews, failed attempts, source boundaries and open questions.
Only heading depth and relocated link targets change.
Its historical statements that adoption was outstanding describe that date; the explicit Current assessment above owns the present judgment.
The source draft is extraction ancestry, not a mutable proof dependency.
Open questions and historical future plans remain historical/exploratory and do not authorize execution while G0001 is paused.
Programs and native certificates remain in their J homes.

### G0001: signed Coxeter covers, Stokes mutations and exact descent traps

Date: 2026-10-09.
Authoring agent structural_research for Yin under the current G0001 continuation.
Rolling exploratory draft, not an adopted result or independent review.

#### Question and scope

Can integral unitriangular bilinear-form presentations expose an arithmetic feature of reciprocal scalar Mahler measure that is absent from fixed-support graph compression?
For an integral upper unitriangular matrix V, the polynomial det(t V + V^T) is monic reciprocal and is the characteristic polynomial of -V^{-1}V^T.
Candidate coverage and any dimension-independent gap are open.
We will test signed presentations, endpoint restrictions, and neutral cyclotomic repair before claiming a useful bridge.

#### Reuse screen

Read S_G0001 current parallel policy, S_G0003, S_G0006, the full graph-return and amalgamation argument L_G0041, and Smy08-U004's knot-polynomial scope.
Existing bounded-support/excess equivalences and primitive realization machinery do not provide this unitriangular presentation.
A 2026-10-09 primary-source search located McMullen's Coxeter paper and de la Pena's survey/chapter on Coxeter polynomials; exact passages and findings will be recorded below.
No external theorem has yet been adopted.

#### Round result and evidence status

The signed-to-unsigned double cover has an exact additional determinant factor.
That factor has unbounded Mahler measure even in dimension ten with the original polynomial fixed to Lehmer's polynomial.
Thus raw signed presentations cannot support an entropy-only cover-cost estimate.
This is a presentation obstruction, not a failure of the whole geometric direction.

There is also a constructive positive control: a dense family with cyclotomic determinant admits an explicit integral bilinear congruence to a chain with zero added Mahler entropy.
An exact rank-five example shows why a strictly decreasing adjacent-mutation search can miss this simplification; one equal-cost step followed by a decreasing step escapes.
A seeded finite sample in the Lehmer mutation orbit finds the same algorithmic issue beyond the cyclotomic control.

All derivations below are authoring-agent work with the separately organized local review recorded at the end.
The executed exact computations are in [J G0016](../computations/programs/Yin_J_G0016/readme.md).
No accepted Claim, new fixed L, unrestricted representation theorem, or G0001 completion is asserted.

<a id="reuse-and-source-scope"></a>
#### Source reuse and the changed question

The local search of G-line ledger and draft files for Coxeter, Seifert, symplectic, bilinear form and related terms found the rational symmetric and symplectic interfaces in L G0021--22, but no signed Stokes mutation treatment.
The responsible S6 obstacles concerning fixed coefficient support and graph excess remain in force; the present operation preserves the whole determinant through integral bilinear congruence rather than through a bounded-support claim.
[L G0041](../ledger/Yin_L_G0041_v1.md#branch-return-budget) was read in full to avoid presenting a small displayed matrix or a time change as entropy compression.
[Smy08-U004](../audits/literature/Smy08/Yin_U004.md) was read at its knot-polynomial section; its restricted knot input does not supply the present coverage.

A bounded primary-source search on 2026-10-09 used the terms `Salem numbers Coxeter transformations integral symmetric Cartan matrix`, `unitriangular Coxeter polynomial`, `reciprocal polynomial Seifert`, and then `Stokes matrices braid Coxeter upper triangular integral` after the mutation mechanism was identified.
The decisive primary passages read online were:

- [McM02](../literature/pdf/McM02.pdf), Curtis T. McMullen, *Coxeter groups, Salem numbers and the Hilbert metric*, Publications Mathematiques de l'IHES 95 (2002), 151--183, [publisher PDF](https://www.numdam.org/item/PMIHES_2002__95__151_0.pdf): Introduction Theorem 1.1 and the geometric representation discussion, plus pp.180--181.
  The theorem states a Lehmer-number lower bound for spectral radii greater than one in the canonical geometric action of a Coxeter system.
  The later passages explicitly distinguish lattice isometries from reflection-group elements.
  Only the displayed statements and scope were read, not the full theorem proof or finite classification.
  This is motivation for a prospective implication, not an adopted premise of the local propositions below.
  No unrestricted signed-matrix theorem is inferred.
- [dlP19](../literature/pdf/dlP19.pdf), Jose-Antonio de la Pena, *Cyclotomic and Littlewood Polynomials Associated to Algebras* (2019), DOI 10.5772/intechopen.82309, [primary chapter](https://www.intechopen.com/chapters/66597), sections 2.4--2.5: the endpoint-square argument and its failure to characterize even cyclotomic Coxeter polynomials.
  The apparent endpoint observation was therefore recognized as established and not pursued as a new contribution.
- [FW24](../literature/pdf/FW24.pdf), Yu-Wei Fan and Junho Peter Whang, *Stokes matrices and exceptional isomorphisms*, Mathematische Annalen 390 (2024), 4041--4086, [primary article](https://link.springer.com/article/10.1007/s00208-024-02850-8), Introduction and section 5.1: the integral unitriangular Coxeter invariant and the explicit braid action.
  The publisher page reports a correction dated 26 August 2024; the correction and the orbit-finiteness proof were not inspected, and no such theorem is adopted.
  The directly checked local transformations below are the same Stokes/Hurwitz framework up to generator and sign conventions, rather than a newly invented formalism.

These readings provide attribution and future source leads.
The authoring agent subsequently acquired and registered all three PDFs on 2026-10-09 and inspected their rendered title pages; their exact editions remain those inspected.
FW24's retained edition identifies itself as corrected publication 2024; that identification does not inspect the correction's mathematical content.
No full source audit was completed, and no broad negative or novelty claim follows from the search.
Search stopped because the precise existing framework and the needed elementary identities were located.
A scoped theorem audit would be needed before promoting an external theorem to a selected dependency.

<a id="signed-cover-identity"></a>
#### The exact signed-cover cost

Let V be an n by n integral upper unitriangular matrix, and write

\[
 p_V(t)=\det(tV+V^T)=\det(tI+V^{-1}V^T),
 \qquad T_V=-V^{-1}V^T.
\]

Thus p_V is a monic degree-n integral polynomial with constant term one.
Transposition gives t^n p_V(1/t)=p_V(t).
We always use its ordinary, unnormalized logarithmic Mahler measure m(p_V).

Set V^- to have diagonal one and strict upper entries -|V_ij|.
Define a 2n by 2n upper unitriangular matrix W in vertex-then-sheet order.
Its diagonal 2 by 2 blocks are I_2.
At i<j, for a=V_ij, use

\[
 W_{ij}=\begin{cases}a I_2,&a\le0,\\-a S,&a>0,\end{cases}
 \qquad S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Every strict upper entry of W is nonpositive.
The subspaces with equal and opposite sheet coordinates are invariant under W and W^T.
Their restrictions are respectively V^- and V.
Consequently

\[
 p_W=p_{V^-}p_V,\qquad m(p_W)=m(p_{V^-})+m(p_V).                 \tag{1}
\]

The decomposition is over Q (or orthogonally over R after scaling).
No normalized trace or division by two is present.
In particular a nonnegative extra cost cannot be dropped when returning to the scalar measure.

When all nonzero V_ij are plus or minus one, W is the unitriangular matrix of an ordinary simply-laced Coxeter graph.
In that restricted case the cited external Coxeter gap would make a bound m(p_{V^-})<=K m(p_V) useful, giving m(p_V)>=log(lambda_Lehmer)/(1+K) whenever m(p_V)>0.
This is only a proposed interface: neither such an optimized bound nor coverage of all small scalar inputs is established.
The larger integral entries produced below are not silently identified with the canonical representation of a Coxeter system.

A diagonal sign change D with entries plus or minus one preserves p_V under V->DVD.
The presentation is called switchable here if some D has DVD=V^-.
Equivalently, the product of edge signs around every cycle is (-1)^(cycle length).
In that case p_{V^-}=p_V, and the cover doubles the logarithmic measure.
A forest is automatically switchable.

The classical endpoint condition p_V(-1)=det(V^T-V) is a nonnegative integer square in even dimension and zero in odd dimension.
It is necessary, not sufficient for a presentation.
Allowing a factor t+1 makes the zero endpoint condition vacuous; it therefore does not close neutral completion.

<a id="dense-neutral-control"></a>
#### Dense neutral data with a constructive simplification

Take V_n to have every entry on or above the diagonal equal to one.
Let P have columns e_i-e_{i+1} for i<n and e_n as its last column.
Direct calculation gives P^T V_n P lower bidiagonal, with diagonal one and subdiagonal minus one.
Reversing the column/row order produces the upper bidiagonal chain C_n with diagonal one and superdiagonal minus one.
Both changes are unimodular, so

\[
 p_{V_n}=p_{C_n}=1+t+\cdots+t^n.                              \tag{2}
\]

The last identity follows also from the determinant recurrence Q_n=(t+1)Q_{n-1}-tQ_{n-2}, Q_0=1, Q_1=t+1.
Hence the original and chain measures are zero, and C_n^-=C_n.

On the other hand V_n^- has every strict upper entry minus one.
Its inverse has entry 2^(j-i-1) at i<j.
Therefore

\[
 \operatorname{tr}T_{V_n^-}=2^n-2n-1.
\]

For any monic degree-n polynomial q with roots beta_j, each |beta_j|<=M(q), so M(q)>=|sum beta_j|/n.
It follows that

\[
 M(p_{V_n^-})\ge\frac{2^n-2n-1}{n}\longrightarrow\infty.      \tag{3}
\]

Thus the same neutral determinant has both a cover with unbounded added entropy and an explicitly congruent chain with zero added entropy.
This only disproves a bound on arbitrary presentations.
It supports investigating reductions before estimating the cover cost.
It does not prove that the displayed congruence is a braid word, or that any analogous reduction exists for an indefinite form.

<a id="mutation-and-energy"></a>
#### Exact adjacent mutations and the elementary descent criterion

For adjacent indices i,i+1 put a=V_i,i+1 and let Q_i(a) be the identity outside this pair, with pair block

\[
 Q(a)=\begin{pmatrix}0&1\\1&-a\end{pmatrix}.
\]

Then mu_i(V)=Q_i(a)^T V Q_i(a) is again integral upper unitriangular, the new adjacent entry is -a, and p_mu_i(V)=p_V.
The inverse move has pair block [[-a,1],[1,0]], evaluated with the current a.
These assertions follow by multiplication of the pair block and the external row/column pairs.
Congruence preserves det(tV+V^T) because det(Q)^2=1.
In particular every finite mutation preserves the full polynomial and all eigenvalue multiplicities, not just its dominant root.

Let E(V)=sum_(i<j) V_ij^2.
Form vectors x,y from all external pairs: (V_ki,V_k,i+1) for k<i, and (V_ik,V_i+1,k) for k>i+1.
The forward move changes each pair (x,y) to (y,x-ay), while the inverse changes it to (y-ax,x).
The adjacent square a^2 is unchanged.
Thus

\[
 E(\mu_iV)-E(V)=a^2\|y\|^2-2a\langle x,y\rangle,
\quad E(\mu_i^{-1}V)-E(V)=a^2\|x\|^2-2a\langle x,y\rangle.     \tag{4}
\]

This gives an exact inexpensive descent test, but a strict local minimum for these particular moves is not an orbit minimum.

<a id="rank-five-plateau"></a>
#### A verified rank-five trap and a successful plateau escape

The greedy rule in J G0016 tries both directions at each adjacent pair and chooses minimum E, breaking ties by the smaller index and then the forward direction; it executes a move only when E strictly decreases.
Starting from V_5, it reaches

\[
 U=\begin{pmatrix}
 1&-1&1&0&1\\0&1&0&0&0\\0&0&1&-1&1\\0&0&0&1&0\\0&0&0&0&1
 \end{pmatrix},\qquad E(U)=5.                                \tag{5}
\]

Its polynomial remains 1+t+...+t^5.
The energy changes for the forward/inverse moves at the four pairs are, in order, (0,2),(0,0),(0,2),(0,0).
Hence no single allowed move strictly decreases E.
Its triangle on vertices 1,3,5 has all positive edges, so U is not switchable.
Its absolute presentation has

\[
 p_{U^-}=t^5-t^4-5t^3-5t^2-t+1,
\]

which has a real root greater than one: its value at one is negative and its leading coefficient is positive.
Thus added Mahler entropy remains at this local trap.

Apply the forward moves at one-based pairs (3,4), then (4,5).
Their energies are 5,5,4 and the last matrix is

\[
 \begin{pmatrix}
 1&-1&0&1&0\\0&1&0&0&0\\0&0&1&0&1\\0&0&0&1&-1\\0&0&0&0&1
 \end{pmatrix}.
\]

Its underlying graph is a chain and is switchable.
Its original and absolute measures are both zero.
These are exact matrix and determinant checks, not floating-point eigenvalue observations.
The example explains why the next search must permit equal-cost transitions or use a different potential; it does not establish that equal-cost transitions always suffice.

<a id="fixed-degree-unbounded-cover"></a>
#### Unbounded extra cost at the fixed irreducible Lehmer polynomial

The stronger control uses the following ten-dimensional matrix V_0, retained literally in the J program:

```text
1  2 -4  4  4  0 -1  1  1  0
0  1 -3  3  3  0 -1  1  1  0
0  0  1  0  0  0  1 -1  0  0
0  0  0  1  1  0 -1  0  0  0
0  0  0  0  1  1  0  0  0  0
0  0  0  0  0  1  1  0  0  1
0  0  0  0  0  0  1  0  0  0
0  0  0  0  0  0  0  1  0  0
0  0  0  0  0  0  0  0  1  0
0  0  0  0  0  0  0  0  0  1
```

Its determinant is exactly

\[
 L(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1.                   \tag{6}
\]

The J computation checked this both as the characteristic polynomial of -V_0^{-1}V_0^T and through the direct determinants det(zV_0+V_0^T) at the eleven integers -5 through 5.
Both compared polynomials have degree at most ten, so the direct finite comparison verifies equality.
L is the usual irreducible Lehmer polynomial, already used in [L G0033](../ledger/Yin_L_G0033_v1.md#lehmer-two-cycle-realization).
Its known irreducibility is not required for the identity or divergence argument, but makes clear that neutral padding is absent from this control.

Let V_k be obtained by 2k forward mutations at the one-based pair (2,3).
The adjacent entry returns to a=-3 after every two moves.
The composite pair change is the constant matrix

\[
 H=Q(-3)Q(3)=\begin{pmatrix}1&-3\\3&-8\end{pmatrix},
 \qquad \det H=1,\quad\operatorname{tr}H=-7.
\]

The first row's pair is therefore (u_k,v_k)=(2,-4)H^k.
Cayley--Hamilton gives u_(k+2)=-7u_(k+1)-u_k, with u_0=2,u_1=-10.
The signs alternate; the positive magnitudes satisfy b_(k+2)=7b_(k+1)-b_k and grow at least geometrically (b_1>=5b_0, and thereafter b_(k+1)>=6b_k).
Consequently E(V_k)>=u_k^2 tends to infinity, while p_(V_k)=L for every k.

For any upper unitriangular V, put A=I-V^-, a nonnegative strictly upper triangular matrix.
Then (V^-)^{-1}=I+A+...+A^(n-1), so

\[
 \operatorname{tr}T_{V^-}
 =-n+\sum_{i<j}((I-A)^{-1})_{ij}A_{ij}
 \ge -n+\sum_{i<j}A_{ij}^2=E(V)-n.                         \tag{7}
\]

Combining (7) with the elementary root-sum bound above gives

\[
 M(p_{V_k^-})\ge\frac{E(V_k)-10}{10}\longrightarrow\infty,
 \qquad p_{V_k}=L.                                        \tag{8}
\]

Thus naive cover cost has no bound depending only on m(p_V), even after fixing the degree and the entire positive irreducible polynomial.
This does not say that the minimum cover cost in the congruence or mutation orbit diverges.
The ordinary Y_(2,3,7) matrix has the same polynomial and is already switchable.
The discovery of V_0 used a seeded mutation walk, but neither the 3151-step discovery walk nor a claim that every presentation with polynomial L lies in the same orbit is a premise of (6)--(8).

<a id="finite-orbit-test"></a>
#### Executed finite scope and next conjectural experiment

On 2026-10-09, J G0016 ran with Python 3.12.14 and SymPy 1.14.0, using exact integer/rational matrices and polynomial arithmetic throughout.
It verified (2) and the explicit congruence for n=2,...,12; the full cover factorization for n=2,...,7; the rank-five trap and escape; (6) by the two polynomial calculations; and seven members k=0,...,6 of the fixed-degree family.
Those finite checks support the displayed algebra, whose all-parameter arguments are given separately above.

The exploratory orbit sample started at the ten-vertex Y_(2,3,7) matrix with three arm lengths 1,2,6.
It used random seed 926104, 80 independent walks of 24 moves, retaining choices with E<=60, followed by strict greedy descent.
All 80 final matrices were distinct as literal ordered matrices and all had exactly polynomial L.
Their energies were 9,10,11,12,13; 66 of these 80 were nonswitchable.
Literal distinctness is not classification up to signs or any other equivalence.
The sample is not uniform over an orbit, is not exhaustive, and establishes no frequency or asymptotic assertion.

The useful conjectural direction is now to compare *optimized* added cover entropy after actual determinant-preserving moves, and to use a mutation graph with plateau transitions rather than a strictly decreasing energy rule.
A first finite question is whether each retained small-entry Lehmer trap can reach a switchable representative without increasing E above its starting value; the rank-five example shows why this is plausible enough to test.
Success on this known orbit would validate only the search mechanism, not new scalar coverage.
Failure would identify the required energy barrier and invite a different potential.

A broader leap worth keeping open is that sufficiently small positive scalar measure could force a low-cost integral Stokes presentation after cyclotomic stabilization and a suitable choice within its mutation/congruence classes.
Neither existence of such a presentation nor a uniform bound on its optimized cost is known here.
These are separate obligations.
The exact fixed-degree control explains why estimating arbitrary representatives cannot answer the question, while the constructive and plateau controls keep reduction experiments active.

#### Self-review and limitations

Authoring-agent checks covered reciprocity, unnormalized cover decomposition, integral congruence preservation, both adjacent mutation directions, the energy formula, the literal trap, both determinant computations for V_0, the two-move recurrence, and the trace lower bound.
Initial program execution exposed a SymPy Boolean conversion issue, then refuted the initially overstrong trial assertion that strict greedy descent always makes the dense neutral controls switchable; both were corrected, and the latter failure is preserved above.
All claimed runs completed after correction.
No floating-point Mahler computation, external theorem proof audit, source correction inspection or exhaustive orbit analysis was performed.

#### Separately organized local review

At 2026-10-09T15:16 the coordinating AI for Yin reviewed the complete direct mathematical argument (1)--(8) and the J G0016 program.
It rechecked the symmetric/antisymmetric cover factors, determinant and endpoint conventions, dense-family congruence and trace, both mutation directions and all external pair energy terms, the literal plateau escape, and the fixed-degree recurrence and trace-to-Mahler implication.
It found no mathematical defect at this scope.
The reviewer had supplied the broad exploration assignment and received author progress explanations; it had not contributed the displayed construction or derivations.
It had asked for literal-matrix sample counts to be distinguished from equivalence classes.

For the central fixed-degree witness, the reviewer wrote [review_witness.py](../computations/programs/Yin_J_G0016/review_witness.py) using standard-library integer Bareiss determinants and the constant two-move congruence, without importing the author's mutation or characteristic-polynomial implementation.
Its completed run checked 77 determinant values for k=0,...,6 and matched all seven saved energies and coupling rows.
These finite tests supplement the all-k written recurrence proof; they do not substitute for it.
The reviewer inspected but did not rerun the 80-walk discovery sample or the full source literature, and adopts no uninspected Coxeter theorem or source correction.
This is a local exploratory review, not a fixed R/L acceptance finding or a new Claim/Task decision.
