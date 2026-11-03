---
author: Yin
---
# Congruence-preserving compact descent and exact arithmetic isolation

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit adoption instruction after the complete separately organized noncontributor review.
This is a restricted mathematical adoption, not C acceptance or Task completion.
G0001 remains active and unresolved.

<a id="ideal-control-fixed-scope"></a>
## Current adopted scope

For actual narrow-domain states in a nonzero ideal I of a degree-d Salem order, d=2s+2, [integer norm gives the isolation scale](#ideal-zero-class-isolation-scale) J(I)=sqrt(s)([O:I]/S)^(1/(d-2)).
The [conditional termination bridge](#zero-congruence-control-termination-bridge) requires an original-digit zero-class-preserving convex cover whose normalized ball radius exceeds 1/(2J(I)).
Together with a finite strict legal-entry certificate from the ordinary compact residue, this would prove actual co-return.
Neither constructive hypothesis is supplied by the theorem.

The [all-residue counting obstruction](#all-residue-descent-linear-radius-cost) requires a radius at least linear in q if all represented classes modulo qO must be preserved.
It is distinct from the zero-class-only bridge.
The [sparse-label interval and permutation obstruction](#sparse-labels-and-permutation-automaton-boundary) retain arbitrary fixed sparse labels on a common interval, while excluding a state-independent reset word in a nontrivial quotient.
They do not solve the coupled free-digit/residue condition or exclude state-dependent branching.

The complete original D G0055 proof and author-checking/contribution account follow.
Historical pending-review/adoption wording is superseded only by this current adoption statement.
Heading depth and navigation are relocated; statements, constants, hypotheses, source boundaries and review history are preserved.

<a id="retained-ideal-control-argument"></a>
## Complete original argument and checking scope

## Congruence-preserving descent: exact isolation scale and necessary residue cost

Date: 2026-10-10.

The question is whether congruence-preserving compact descent can bridge [L183's remaining actual-order termination gate](Yin_L_G0183_v1.md#compact-termination-certificate-interface).
The coordinator supplied the question; the deductions below are the drafting agent's.
This is a working argument pending independent review.

### Question

The actual order removes the explicit nonzero fractional-module class obstruction, but that does not itself give legal exact returns.
Quantify the arithmetic isolation radius of qO and the minimum compact size forced by preserving all residue classes.
State separately the analytic hypothesis needed to enter the desired residue and the hypothesis needed to reduce while preserving it.

<a id="ideal-zero-class-isolation-scale"></a>
### 1. Exact norm isolation inside the actual order

Fix a Salem beta of degree d=2s+2, s>=1, with1<beta<phi when invoking the fixed global control theorem.
Use O=Z[beta], S=beta/(beta-1), and

    N={x in O: |x_+|<=1, |x_-|<=S},
    rho(x)^2=sum_(j=1)^s |x(zeta_j)|^2,
    K_R={x in N: rho(x)<=R}.

Let I be a nonzero ideal of O and write n(I)=[O:I].
This index is finite by the argument in [L183](Yin_L_G0183_v1.md#original-digit-finite-quotient-connectivity).
For nonzero x in I, the inclusions xO subset I subset O and multiplicativity of finite group indices give

    |N_field(x)|=[O:xO]=n(I)[I:xO]>=n(I).

The two real bounds and the arithmetic-geometric mean inequality for the s nonnegative squared neutral moduli give

    n(I)<=|N_field(x)|
         <=S product_j |x(zeta_j)|^2
         <=S (rho(x)^2/s)^s.

Thus every nonzero x in I intersect N satisfies

    rho(x)>=J(I):=sqrt(s)(n(I)/S)^(1/(d-2)).         (1)

For the integer ideal I=qO, q>=2, n(I)=q^d because O is a free rank-d abelian group.
Therefore

    J(qO)=sqrt(s) S^(-1/(d-2)) q^(d/(d-2)),
    R<J(qO) implies K_R intersect qO={0}.            (2)

The strict radius inequality is kept; no equality case is silently discarded.
This is a fixed-input arithmetic isolation estimate in the actual order, with the full norm and all neutral pairs counted.
It does not identify which ideal classes can be reached by a real-legal path.

The fractional-module obstruction of L183 disappears for an initial x in O, since its class in the larger quotient M/O is then zero and all original operations preserve O.
This only removes that particular obstruction.
Choosing a large ideal containing x is not a substitute for entering its zero class: every such I contains xO and therefore n(I)<=|N_field(x)|.
If x is a unit, it belongs to no proper ideal at all.
Thus arbitrary moduli cannot be chosen around a fixed unit state by that shortcut.

<a id="zero-congruence-control-termination-bridge"></a>
### 2. A sufficient congruence-control bridge with an exact margin

For a word w of length n define its unnormalized translation

    D_w=sum_(i=1)^n eta_i beta^(n-i),
    T_w(x)=beta^n x+D_w.

Call a word zero-class preserving modulo I when D_w belongs to I.
Since beta is a unit, such a word sends I into I.
It need not fix other classes; preserving every class would be a stronger and different condition.

Suppose that the annulus[1/2,1] has a finite strict original-digit convex cover using only zero-class-preserving words, and that the hulls of their nonzero normalized neutral displacements c_w/||c_w||^2 all contain a centered ball of radius r_I>0.
Assume

    r_I>1/(2J(I)).                                   (3)

Choose R with1/(2r_I)<R<J(I), and let m_I>0 be the minimum squared norm of the finitely many nonzero displacements.
The [L176 calculation](Yin_L_G0176_v1.md#joint-neutral-pointwise-control) then gives a squared-neutral drop of at least

    delta_I=m_I(2r_I R-1)>0                          (4)

whenever the state norm is at least R.
All chosen endpoints are strictly narrow.
Negating a word preserves D_w in I, and initial zero digits preserve I, so the sign and zero-prefix extension to N intersect I retains the ideal condition.
The stable bound stays invariant.
Each nonzero real coordinate below1/2 reaches the annulus after finitely many zeros, while an actual algebraic state with real coordinate zero is zero.

Repeated descent reaches K_R intersect I after finitely many drops.
By(1) this set is{0}.
Consequently the displayed finite control cover and margin prove exact co-return for every state of N intersect I.
This is a complete conditional theorem; it requires the stated ideal-preserving cover and quantitative margin, neither of which follows merely from ordinary global PC.

To conclude co-return for all of N, one must additionally show legal entry into N intersect I.
A finite version suffices: first use the ordinary fixed L180 compact reduction into its completely covered finite residue K_(R0), then for each member give an original word whose endpoint is both narrow and in I.
These are exact finite congruence-entry certificates; after them, the ideal-preserving reduction just proved ends at zero.
Original finite-quotient connectivity in L183 supplies no such narrow-endpoint guard.
The two obligations must be retained separately.

For qO the threshold(3) reads explicitly

    r_q > S^(1/(d-2)) q^(-d/(d-2))/(2sqrt(s)).       (5)

Thus a family of proved zero-class-preserving covers with radii R_q=o(q^(d/(d-2))) would eventually fall below the isolation scale, provided its actual descent constants and legal entry certificates were also established.
This is a useful target, not a claimed construction or an inference from all finite congruences being solvable.

<a id="all-residue-descent-linear-radius-cost"></a>
### 3. Preserving all residues forces a growing compact radius

Here is an exact obstruction to keeping the ordinary compact radius fixed while demanding preservation of every residue class.
There are fixed-input constants c_beta,C_beta>0 such that

    number of residue classes of N modulo qO
        >=c_beta q^(d-2),
    |K_R|<=C_beta(R+1)^(d-2).                        (6)

We prove both bounds directly.
Consider the q^d distinct representatives

    V_q={sum_(i=0)^(d-1) a_i beta^i:0<=a_i<q}.

Their real values lie between0 and(q-1)C_+, and their stable values between0 and(q-1)C_-, where C_+=sum_(i=0)^(d-1)beta^i and C_-=sum_(i=0)^(d-1)beta^(-i).
Partition these ranges into half-open cells of widths1 and S.
At most

    q^2 C_cell cells are needed,
    C_cell=(C_++1)(C_-/S+1).

Some cell contains at least q^(d-2)/C_cell representatives.
Subtract one selected representative from all the others in this cell.
Every difference is in N, with the two real magnitudes strictly less than1 and S.
Their classes modulo qO remain distinct, because the original coefficient representatives were distinct.
This proves the first bound in(6) with c_beta=1/C_cell, including the zero difference; integer rounding can only strengthen the count.

For the second bound, use the full real embedding lattice in R^d.
Choose0<epsilon<=1 so that the open coordinate cubes of side2epsilon centered at distinct lattice points are disjoint.
Such epsilon exists because the coefficient-to-embedding map is invertible and every nonzero integral coefficient vector has Euclidean length at least1.
The cubes around K_R lie in the box with the first two coordinate radii1+epsilon and S+epsilon, and every remaining coordinate radius at most R+epsilon.
Volume comparison gives

    |K_R|<=(1+epsilon)(S+epsilon)(R+epsilon)^(d-2)/epsilon^d
         <=C_K(R+1)^(d-2),
    C_K=(1+epsilon)(S+epsilon)/epsilon^d.             (7)

Now suppose every x in N has a continuation ending in K_(R_q) and in the same class as x modulo qO.
No condition on its intermediate congruences or chosen policy is needed for this count.
The endpoint set must represent every class represented by N.
Equations(6)--(7) force

    R_q+1 >= q/(C_cell C_K)^(1/(d-2)).               (8)

Therefore no fixed radius can support such an all-class-preserving reduction for all q.
This lower bound applies to the stronger all-residue demand, not just to zero-class-preserving control on N intersect qO.
It does not refute the bridge in Section2: its linear lower scale is smaller than q^(d/(d-2)) at every fixed finite degree, although the exponent difference2/(d-2) becomes small in high degree.
No degree-uniform constants are supplied by this counting argument.

<a id="sparse-labels-and-permutation-automaton-boundary"></a>
### 4. What the sparse binary construction does and does not prescribe

The coordinator suggested investigating a finite residue automaton within L180's sparse free-slot proof.
This was a research question, not a supplied derivation.
The following exact extension and obstruction distinguish two versions of that idea.

Use beta<phi, B=1/(beta-1), and a gap L satisfying the inequality in the preserved original D51 Section2.
Let S_0 be prescribed positions with gaps at least L, and let W=sum_(i in S_0)beta^(-i).
The fixed free-slot proof shows that binary sums on the other positions fill[0,B-W].
For any prescribed pattern e_i in{0,1} on S_0, write D=sum_(i in S_0)e_i beta^(-i).
Its possible complete sums are exactly

    [D,D+B-W].

Since0<=D<=W, every prescribed pattern is compatible with every target in the common interval

    [W,B-W], provided W<=B/2.                        (9)

This is the exact common interval: the all-zero and all-one patterns force its two endpoints.
By starting the sparse set sufficiently late, W can be made smaller than the distance of a fixed interior target from either endpoint of[0,B].
Thus arbitrary fixed sparse binary labels, not only prescribed zeros, can coexist with a strictly interior real target.
This extension preserves the original alphabet after the sign-dependent shift used in L180.

It does not yet enforce a residue.
At a finite horizon, every unprescribed digit also contributes to the residue equation.
The conclusion has the order 'for every fixed prescribed pattern, there exists a completing free pattern'; it is not a construction in which prescribed and free digits can then independently be changed to repair the finite residue.
A state-dependent automaton rule would impose a coupled condition on both groups of digits.
Neither(9) nor unconstrained quotient connectivity proves that coupled real-and-congruence condition.

There is also an exact obstruction to one simple synchronization proposal.
For any nontrivial finite quotient O/I, every fixed original word acts as

    r -> beta^n r+D_w modulo I.

This is a permutation, since beta is a unit.
Consequently no state-independent fixed word sends all residues to zero, or even merges two distinct residues.
A common reset block cannot exist in this automaton.
This does not exclude choosing different words according to the current state, nor more elaborate branching with real overlap.
It isolates the missing task: construct an actual state-dependent family which retains strict real representability while achieving the required translation congruences, and then quantify its normalized hull margin as in(3).

As a second quantitative caution, if a finite family of nonzero zero-class-preserving words is strictly legal at real0, its endpoints lie in N intersect I, and their neutral norms equal ||c_w||.
Formula(1) implies

    ||c_w/||c_w||^2||<=1/J(I).

Any centered ball in that particular normalized hull therefore has radius at most1/J(I).
Large legal endpoint amplitudes are not automatically cheap normalized control vectors.
This bound concerns a family legal at zero; it is not asserted for every annulus family in Section2.
It does not itself contradict the required lower margin1/(2J(I)).

### 5. Current result, unresolved gate and checking boundary

The new bridge is quantitative and conditional: ideal-preserving convex control with margin(3), plus genuine legal entry into its zero class, forces termination by exact norm isolation.
The two proved limitations are also precise: preserving all residue classes requires radius at least linear in q, and no fixed residue reset word is available.
Sparse prescribed labels retain a common real interval, but no combined residue-aware expansion theorem is supplied by that fact.

The actual-order restriction removes L183's explicit fractional class obstruction.
It does not on its own supply either missing constructive hypothesis.
The decisive next test is a completely proved finite-residue/real-overlap construction for one modulus, with all free-digit contributions and its normalized geometric margin visible.
A successful ideal-preserving finite cover with margin below(3), or a quotient path with no strict real endpoint, would not establish termination.
No broad enumeration or unsupported universal claim has been substituted for these obligations.

The reuse screen read L176/L180's normalized descent, sparse free-slot proof and exact real conventions; L183's quotient connectivity and fractional-module scope; and the coefficient-box infinitude mechanism retained in L170.
The present residue-class count adapts that coefficient-box mechanism while keeping distinct classes modulo q; its statement and constants are proved here.
All new steps use elementary integer norm, finite group indices, real lattice packing and the fixed binary interval lemma.
No new external source, program or J is a premise.
The coordinator supplied the research questions and received checkpoints, but none of these derivations.

Author checking covered the ideal index divisor, full conjugate-pair norm, strict isolation inequality, zero-class versus all-class quantifiers, finite descent drop and real guards, distinct coefficient residues after subtraction, all packing constants, sparse-pattern interval endpoints and permutation obstruction.
Complete independent review and fixed adoption remain pending.
Universal actual compact termination, original-law costs and G0001 remain unresolved.




## Retention and contribution boundary

The structural drafting agent supplied the ideal norm isolation, conditional descent bridge, residue count, sparse-label extension and permutation analysis.
The exact original listed author check remains [SELF in R86](../audits/reviews/Yin_R_G0086_v1.md#ideal-control-original-author-check-finding), with its original2026-10-10 day precision and then-pending disposition.
On2026-10-10 the coordinating AI checked the complete frozen D55 Sections1--5/formulas(1)--(9), all constants and guards, and found no mathematical defect.
Its exact mathematical input is the original [retained ideal-control argument](#retained-ideal-control-argument): actual-order norm/index isolation, conditional zero-class margin and separate strict entry, all-class counting/packing radius, arbitrary sparse-pattern intervals and permutation/no-reset/legal-at-zero bounds.
The ideal-preserving cover and strict compact-entry construction remained unresolved hypotheses, not supplied certificates.
The coordinator assigned the research questions and received checkpoints, progress summaries and shared context but contributed none of those new deductions.
It authored the already fixed L180 control input; that is ordinary upstream participation.
The actual initial target mathematics in the additional communications remains unestablished, so the original whole relationship is unknown.

The original2026-10-10 fixed-retention instruction above followed that complete noncontributor check.
The structural agent implemented the restricted adoption and retained the D55 proof; this was not C acceptance or Task completion.
The [later R660 whole finding](../audits/reviews/Yin_R_G0660_v1.md#isolated-ideal-control-whole-finding) is a new2026-10-22 inspection of C451v1 and an explicit comparison of that entire old scope, including every source, negative, contribution and unconstructed-hypothesis limit.
It does not change the old adoption date or establish old isolation.
There is no computation group or J for this round.
Earlier fixed mathematical bodies and unrelated drafts remain unchanged.
