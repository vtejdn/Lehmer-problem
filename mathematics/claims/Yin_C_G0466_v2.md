---
author: Yin
---
# Complete all-integer binary triangularization, fixed terminal obstructions and full cover costs

The complete original proof, actual finite native domain and historical proper-cover failure are retained without abridgment.
L266 remains the meaningful exploration, declared experiment, contribution and fixed-review input; this construction resumes no Task/E.

Version1 remains open because its newly added top-level P4 expansion was mistyped; the actual F/V0, complete original proof and all native mathematics were already correct.
This physical version corrects that one new factor definition and preserves the ENTIRE Argument unchanged; it supplies no new mathematical mechanism or isolated review.

## Statement

For EVERY integral bilinear matrix B=[[a,b],[c,d]] with determinant ad-bc=1, an integral determinant-one congruence to an upper-unitriangular matrix with both diagonal entries+1 exists if and only if q(x,y)=a*x^2+(b+c)*x*y+d*y^2 represents1 over Z.
A norm-one vector is primitive, Bezout completes it, and the exact lower-entry clearing gives [[1,k],[0,1]] with k=b-c.
The COMPLETE solver includes all integer vectors, every sign of a, definite/semidefinite/indefinite cases, a=0 with a coordinate swap, and the identically-zero quadratic case a=d=0.
For a!=0 set h=b+c,Delta=k^2-4,u=2a*x+h*y; its necessary and sufficient conditions are

    u^2-Delta*y^2=4a, u=hy modulo2a.

For Delta<0 and a>0 test EVERY integer abs(y)<=sqrt(4a/(-Delta)), both square roots and full divisibility; a<0 gives no solution.
For Delta=0,a>0 a solution exists exactly when4a is a square and gcd(h,2a) divides a square root; Bezout solves the congruence, without a cube scan.
For Delta>0 the ACTUAL determinant-one bilinear isometry H=[[-c,-d],[a,b]] preserves B and gives the exact half-coordinate transformations and absolute scaling by epsilon=(abs(k)+sqrt(Delta))/2 or its inverse.
Some isometric representative of EVERY solution has abs(y)<2sqrt(abs(a)), so the finite interval abs(y)<=floor(sqrt(4abs(a)))+1 with exact integer square roots/congruences is COMPLETE.
This bounds some representative, not every vector in its original coordinates, and imports no uninspected Pell/classification theorem.

Apply this solver only AFTER the prescribed sign-normalized cube pivots in dimensions6,5,4,3, support/lexicographic order and coordinate completions, to the fixed actual form

    V0=[[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],
        [2,1,0,2,1,1],[0,-1,-1,0,-1,0],
        [1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]].

Its determinant is1 and complete polynomial is F=Phi6*P4=t^6-2t^5+t^4-t^3+t^2-2t+1, with P4=t^4-t^3-t^2-t+1.
The original20000-call/120-second prefix traversal completed6670 calls,4500 exact-form duplicates and2170 unique forms, including89 distinct binary terminals (2 zero quadratic,54 semidefinite,33 indefinite), plus211 earlier forms with no allowed cube pivot.
Every terminal lacks an integer norm-one vector.
The COMPLETE89 modular certificates first fail at2 for42 forms,3 for44 and4 for3, with every represented residue set retained and independently checked using827 pairs in the declared2,...,24 range.
This excludes arbitrary INTEGER final pivots after THESE prefixes, not larger earlier pivots, changed completions, other realizing forms or all integral bases of V0.

The separate original-field tests include EVERY normalized norm-one field line at p2,3 only, with200000-call/120-second caps per field.
They stop at actual verified SUCCESS after345/1784 calls, not complete failure or a cap.
The saved full6-dimensional bases, congruent unit-diagonal upper matrices and ALL7 polynomial coefficients modulo each prime are verified.
These witnesses refute blanket global mod2/mod3 obstructions for V0, and give no integral lift, result modulo4, prime-power compatibility or local-to-global theorem.

For EVERY integer n>=2, the exact matrices

    A=[[1,3],[0,1]], S_n=[[n,n+1],[n-1,n]],det S_n=1,
    B_n=S_n^T*A*S_n
       =[[5n^2-5n+1,5n^2],[5n^2-3,5n^2+5n+1]]

have no norm-one vector in the nonzero coordinate cube{-1,0,1}^2, while(n,1-n)=S_n^-1*e0 is an actual norm-one vector of height n and S_n^-1 supplies a complete integer positive basis.
EVERY norm-one vector has height>=n-1, by the exact substitution z=x+y,w=nz-x and5w^2+5wz+z^2=1; this is an ALL-n proof, not an inference from samples.
The four fixed controls n2,3,17,101 yield the saved solver vectors(11,-7),(15,-11),(71,-67),(407,-403), each an actual vector/basis, without a shortest-vector claim.

For any successful binary form the COMPLETE original/standard absolute polynomial is Q_k=t^2+(2-k^2)t+1, and the proper signed-cover polynomial is Q_k^2.
Ranks are2/4, height max(1,abs(k)) and strict-upper energies k^2/2k^2.
For abs(k)<=2 every root is on the circle, including repeated endpoints; for abs(k)>=3 the expanding root is epsilon^2 and complete original/cover measures are2log epsilon/4log epsilon.
For B_n, k3 fixes Q=t^2-7t+1 and the full cover t^4-14t^3+51t^2-14t+1, with achieved proper height3/energy9 and rank4 cover energy18.
The original B_n has height5n^2+5n+1 and WHOLE squared-entry sum100n^4+40n^2+11.
Its full-entry absolute matrix is-B_n and the separately defined FULL-entry lift has complete polynomial Q^2 and twice that whole sum, but is NOT upper-unitriangular.
Constant complete measure and unbounded coordinate height are kept distinct.

V0 retains height2/whole sum33, full-entry absolute factor-(t^6-7t^4-11t^3-7t^2+1), and literal rank12 relaxed lift with the ENTIRE product with F and whole sum66.
Its original measure is log beta4 and relaxed complete-cover measure>2log beta4; the achieved proper Phi2^2*P4 comparison retains its full separate rank/energy and complete2log beta4 measure.
No proper target integer realization or uncomputed favorable companion cost is asserted.
The historical control matrix mislabeled proper is preserved with nonzero lower entries and strict-upper energy20; its identical scalar polynomial did not detect that interface error.
The corrected proper matrix has identity diagonal, zero lower triangle and energy18; only that output matrix changed in each of the four original controls.
All source screens, author contribution, pre-freeze correction and original nonblind review limits remain explicit.
No global integer obstruction, near-one family, optimized target cost, external classification, unrestricted gap or Task completion follows.

<a id="argument"></a>
## Complete retained argument

The dated author proof below retains its original declarations, source/contribution scope and pre-freeze correction; its historical pending-review wording is read at that date.

<a id="binary-terminal-reuse-and-scope"></a>
### 1. Reuse and a changed unbounded terminal mechanism

Date:2026-10-10.
[L262](Yin_C_G0456_v1.md#argument) provides the full integral exterior-square form for F=Phi6 P4, its exact parameter and cost statements, and the completed small-pivot tree.
That finite failure did not exclude larger integer terminal pivots.
[L226's source screen](../ledger/Yin_L_G0226_v1.md#integral-rank-seven-fixed-scope) already considered the registered dlP19 realization discussion; its endpoint necessity is not a sufficient triangularization theorem.
A bounded local search for integral positive pivots, exceptional bases, Seifert forms and triangularization found no applicable stronger retained criterion.
No new external theorem or classification will be used below: the two-dimensional determinant identities supply a direct workable method.
No literature-wide absence or novelty is claimed.

The changed test keeps the displayed small-coordinate prefix choices but replaces the last two-dimensional cube search by an EXACT ALL-INTEGER norm-one solver.
It can either provide a larger terminal pivot and an actual full positive basis, or rigorously exclude every larger terminal pivot after every tested prefix.
The latter is still only a prefix-architecture obstruction, not a global all-bases exclusion.

<a id="complete-binary-positive-pivot"></a>
### 2. A complete integer terminal criterion

Let B=[[a,b],[c,d]] be any integral2-by-2 matrix of determinant one.
Set h=b+c, k=b-c and Delta=k^2-4.
Its quadratic value is q(x,y)=a x^2+hxy+d y^2.
An integral unimodular congruence making B upper triangular with BOTH diagonal entries+1 exists if and only if q represents1 over Z.
Necessity uses its first column.
For sufficiency, a norm-one vector v is primitive; extend it by Bezout to an integer determinant-one basis [v,w].
Replacing w by w-B(w,v)v clears the lower first entry, leaves the first diagonal1, and preserves determinant one.
The remaining diagonal is therefore1.
This criterion includes all integer vectors, with no coordinate bound.

Assume first a!=0.
Completing the square gives

    q(x,y)=1 iff u^2-Delta y^2=4a,
    u=2ax+hy, u=hy modulo2a.                         (1)

If |k|<=1, the discriminant is negative.
When a<0 the form is negative definite and cannot represent1; when a>0, every solution has |y|<=sqrt(4a/(-Delta)).
Testing those finitely many y, every integer square root u of Delta y^2+4a, and the displayed divisibility is complete.

If |k|=2, the form is semidefinite.
For a<0 there is again no solution.
For a>0 it is enough and necessary that4a be an integer square and that at least one root u satisfy gcd(h,2a)|u.
This is exactly the solvability criterion for hy=u modulo2a; Bezout constructs a y and then x.
No bounded scan replaces this linear congruence.

For |k|>=3, introduce the ACTUAL integer matrix

    H=[[-c,-d],[a,b]], det H=1,
    H^T B H=B.                                      (2)

Direct multiplication proves the second equality from ad-bc=1.
Under H, the variables of(1) change by

    u'=(k u+Delta y)/2, y'=(u+k y)/2,
    u'+sqrt(Delta)y'=[(k+sqrt(Delta))/2]
                                   [u+sqrt(Delta)y]. (3)

Let epsilon=(|k|+sqrt(Delta))/2>1.
H or its inverse multiplies the ABSOLUTE value of the last real expression by epsilon.
Any integral solution may therefore be moved, by an integer power of this bilinear isometry, into

    2sqrt(|a|)<=|u+sqrt(Delta)y|<2epsilon sqrt(|a|).

Its conjugate expression has absolute value4|a| divided by that value, at most2sqrt(|a|).
Consequently

    |y|<(epsilon+1)sqrt(|a|)/sqrt(Delta)
         <2sqrt(|a|).                                (4)

For the last inequality put K=|k|>=3: (K+2)/sqrt(K^2-4)<=sqrt5<3, so (epsilon+1)/sqrt(Delta)<2.
Thus, IF there is any integer solution, there is one with |y|<=floor(sqrt(4|a|))+1.
For this explicit finite interval test the square equation and full congruence in(1); negative radicands and nonsquares are rejected.
A surviving x,y is an actual norm-one vector.
This is a complete all-integer algorithm, although the retained answer need not recover the first input solution.
It is not an invocation of an uninspected binary-classification or Pell solvability theorem.

If a=0 but d!=0, interchange coordinates and apply the criterion.
If a=d=0, determinant one forces b=-c=+/-1; then q is identically zero and cannot represent1.
These cases cover every determinant-one B.
The exact finite square-root bounds can be evaluated with integer arithmetic, including a negative leading coefficient in the indefinite case.

<a id="terminal-repair-declared-test"></a>
### 3. Declared bounded-prefix test before execution

Use the unchanged L262 actual F=Phi6 P4 matrix V0 and its precise coordinate completion.
At dimensions6,5,4,3, examine all nonzero sign-normalized vectors in{-1,0,1}^n of quadratic value1, ordered by support size then lexicographically.
Clear the lower first column as in L262 and keep the cumulative unimodular basis.
At dimension2 apply Section2's ALL-INTEGER terminal solver, including its definite, degenerate and indefinite cases.
This changes the terminal decision from a small cube to an exhaustive arithmetic criterion; it is not an enlargement of the settled three-column root box.

Declare caps20000 recursive calls and120 seconds before execution.
Merge identical remaining forms because their future permitted prefixes and exact terminal feasibility agree.
Retain all terminal forms and outcomes, actual call counts, and a complete successful integer basis if one appears.
A success must verify unimodularity, every diagonal+1 and lower entry zero, the COMPLETE original polynomial, the complete ordinary absolute-companion factor and literal rank12 cover, with all height and energy costs.
If no success occurs before a cap, report only the actual finite prefix scope.
If the whole prefix tree completes unsuccessfully, the negative conclusion is complete for those prefixes and ARBITRARY integer final pivots, but not for larger earlier pivots or other completions.
The program and actual results belong to [J60](../computations/programs/Yin_J_G0060/readme.md).
No execution result is asserted by this declaration.

The declared run completed without a cap, with6670 calls and4500 merged duplicates.
It reached89 different binary forms:2 zero quadratic forms,54 semidefinite forms and33 indefinite forms.
Every ALL-INTEGER binary criterion returned no norm-one vector.
Another211 distinct earlier forms had no permitted small-coordinate prefix pivot.
Thus larger final pivots alone cannot repair any of these tested prefixes; larger earlier pivots or a changed realization remain outside this exclusion.

<a id="finite-field-positive-basis-discriminator"></a>
### 4. A separate finite-field discriminator declared before execution

The exact binary outputs motivate a congruence test without assuming a global obstruction.
First, on the retained89 forms only, test all pairs modulo each integer2,...,24 and retain the first modulus at which1 is absent, if any.
This is a compact auxiliary obstruction certificate, not a replacement of Section2's complete solver or a new integer-basis search.

Separately reduce the ORIGINAL six-dimensional V0 modulo2 and modulo3.
At every current dimension enumerate ALL field vectors of quadratic value1, normalized by first nonzero coordinate1.
For these two fields this only removes the sign duplication and preserves every norm-one line.
Extend such a vector by the other coordinate columns, clear the lower first column, and recurse until dimension1.
The exact same primitive completion argument now works over the field.
Unlike the integer prefix test, every norm-one vector in each finite field is included, so a completely failed tree would exclude an integral positive triangular basis for THIS V0.
A successful field basis proves only that this congruence is insufficient; it does not lift it to Z.
Different basis completions do not affect existence because they are merely other bases of the same left-orthogonal complement.

Declare caps200000 recursive calls and120 seconds for EACH of the two fields; stop upon a verified field basis or complete failure, recording a cap separately.
No extra prime, prime power or large integer-pivot scan is included.
The output must check the full field congruence, determinant and unit diagonal, not just a final boolean.
The underlying full integral original polynomial and complete L262 costs remain unchanged; a field basis is not an achieved new integral presentation.

Every binary form has a direct modular obstruction in the declared range:42 first fail modulo2,44 modulo3 and3 modulo4.
The complete represented residue sets are retained.
Thus this particular all-integer terminal failure has compact arithmetic certificates independently of the real reduction bound(4).

In contrast, both ORIGINAL-form field tests found positive triangular bases, at345 calls modulo2 and1784 calls modulo3.
Both stopped at verified success, not at complete failure or a cap.
J60 retains the actual invertible field bases, complete triangular matrices and full degree-six determinant polynomials reduced modulo the respective prime.
These are actual witnesses that a blanket mod2 or mod3 positive-triangularization obstruction for V0 is false.
They do not settle modulo4, all prime powers, coherent integral lifting or an integer basis.
The different terminal moduli therefore cannot be treated as one global obstruction.
No additional modular test is performed in this round.

<a id="unbounded-pivot-control-and-complete-costs"></a>
### 5. A genuine larger-pivot control and all costs

The complete binary algorithm is useful beyond the unsuccessful target.
For any integer n>=2, let

    A=[[1,3],[0,1]], S_n=[[n,n+1],[n-1,n]], det S_n=1,
    B_n=S_n^T A S_n
       =[[5n^2-5n+1,5n^2],[5n^2-3,5n^2+5n+1]].       (5)

The eight nonzero vectors in{-1,0,1}^2 have quadratic values among

    5n^2-5n+1, 5n^2+5n+1, 20n^2-1, 5,

all greater than1.
Nevertheless (n,1-n)=S_n^(-1)e0 is an actual norm-one vector and S_n^(-1) is an explicit positive triangularizing integer basis.
The cube failure here is therefore false as an all-integer inference at EVERY n>=2.
These controls have fixed quadratic polynomial and are not a new growing-complexity or near-one family.

The required pivot size is genuinely unbounded.
Given ANY integral solution q_(B_n)(x,y)=1, put z=x+y and w=nz-x.
Its equation becomes

    5w^2+5wz+z^2=1.                                  (6)

If z=0 it is impossible.
For |z|>=1, the supposition |w|>=2|z| would give the left side at least (5/2)w^2+z^2>=11.
Thus |w|<2|z| and |x|=|nz-w|>(n-2)|z|>=n-2.
Every norm-one vector therefore has height at least n-1.
The explicit vector above has height n.
No fixed coordinate cube can recognize all these actual realizations; this is proved symbolically, not inferred from a large search.
The chosen unimodular basis is complete, and no stabilizing or neutral factor is suppressed.

More generally, whenever Section2 succeeds on B, its determinant-one completion preserves the alternating coefficient k=b-c.
The achieved matrix is exactly [[1,k],[0,1]].
Its full polynomial, standard absolute companion, and literal rank-four cover are

    Q_k=t^2+(2-k^2)t+1,
    A^-=[[1,-|k|],[0,1]], p_(A^-)=Q_k,
    p_cover=Q_k^2.                                    (7)

This is the elementary rank-two specialization of the retained [D9 cover identity](Yin_C_G0002_v1.md#signed-cover-identity) and [L191 bipartite determinant](Yin_C_G0458_v2.md#higher-degree-phi2-realization); no new universal coverage follows.
The proper ranks are2 and4, height max(1,|k|), strict-upper energy k^2 and2k^2.
If |k|<=2 all roots are on the unit circle, including repeated endpoint factors.
If |k|>=3, put epsilon=(|k|+sqrt(k^2-4))/2: the expanding root is epsilon^2, so the COMPLETE original and cover measures are2log epsilon and4log epsilon.
Neither factor is removed or rank-normalized.

For(5), k=3 and Q=t^2-7t+1 at every n.
The transformed proper matrix has height3, energy9 and rank4 cover energy18; its complete cover measure is twice its original measure.
The untransformed B_n has height5n^2+5n+1 and whole squared-entry sum100n^4+40n^2+11.
Since all four entries are positive, its FULL-entry absolute matrix is -B_n; in even rank its determinant polynomial is also Q, and the separately defined full-entry sheet lift has full polynomial Q^2 and whole squared-entry sum twice that of B_n.
That lift is not upper-unitriangular, whereas the explicit S_n^(-1) construction is.
The measure of the complete polynomial is constant while the untransformed entry height grows, so entry size is not used as Mahler measure.

The finite author check now declared is exactly n=2,3,17,101.
Verify(5), the solver's actual integral answer and its completed basis, the explicit S_n^(-1) basis, all original/absolute/cover polynomials, determinant, height and energy, using exact arithmetic.
This is a method control for the all-n proof, not a new target scan.
The initial F form remains exactly L262's rank6 integral zero-diagonal V0, with height2 and whole squared-entry sum33; its full-entry absolute factor is -(t^6-7t^4-11t^3-7t^2+1), and its rank12 lift has the entire product with Phi6 P4, height2 and whole sum66.
Its original measure is log beta4 and its full relaxed cover measure is greater than2log beta4.
No target upper-unitriangular matrix was achieved this round, so no missing target companion receives a conjectural small cost.
The achieved proper L191 Phi2^2 P4 control remains unchanged.

All four declared controls passed exact checks.
The solver found actual larger norm-one vectors (11,-7),(15,-11),(71,-67),(407,-403), respectively, and determinant-one bases mapping B_n to A.
These are legitimate answers, not claims of shortest vectors; the explicit S_n^(-1)e0 vectors give the better height bound n in the proof.
The full cover polynomial in every case is t^4-14t^3+51t^2-14t+1.

<a id="terminal-repair-execution-and-self-check"></a>
### 6. Execution, correction, self-check and the remaining gate

The native exact programs and outputs are in J60.
terminal.py uses the complete Section2 solver after all declared earlier cube choices, with exact-form memoization.
A repeated form has the same future tree, so memoization does not remove a possible success.
The complete target prefix traversal includes the same6670 calls as L262, but its terminal decision now ranges over all integers.
Each of the89 distinct terminal forms is retained with an actual prefix and its arithmetic outcome.
congruence.py records the COMPLETE binary represented residues at the first obstructing modulus, and then produces the two actual global field-basis witnesses.
Its successful field searches do not claim enumeration of all successful bases.
All caps, exact search ranges and outputs are retained; no runtime/node cap occurred.
The same proper and relaxed cover definitions remain separated.

During author self-check, the first control.py output had correctly computed the relaxed full-entry lift but incorrectly labelled that matrix as the proper upper-unitriangular cover of A.
Both had the same scalar polynomial here, so the existing determinant assertion alone did not detect this matrix-interface error.
The first program and output are preserved as historical_control.py and historical_control_result.json.
The current program uses a separate proper_lift with identity diagonal and strict-upper blocks only, explicitly verifies every diagonal/lower entry and energy18, and was rerun successfully on the same four declared controls.
The sole changed mathematical output is that proper cover matrix; the basis, norm, factor, height and measure conclusions are unchanged.
No old file is presented as a correct proper-matrix certificate, and no historical failure is erased.

The proof itself includes direct algebraic checks of H^T B H=B, the real scaling in(3), all signs of a, the zero-leading and zero-quadratic cases, complete congruence divisibility, the integer square-root interval, and primitive determinant-one completion.
For the strict bound in(4), (K+2)^2<=5(K^2-4) is exactly4(K-3)(K+2)>=0; this supplies its full K>=3 justification.
The bound concerns some isometric representative of every solution, not every solution in its original coordinates.
The larger-pivot control was checked for every n>=2 by the displayed polynomial identities and inequalities; its four numerical parameters serve only as exact program controls of that all-parameter proof.
All mathematical decisions use integer/rational or symbolic exact arithmetic.

The coordinator supplied the broad changed-basis question, home/allocation and review coordination, without any current derivation.
orbit_research supplied the complete binary criterion, changed terminal use, modular discriminator, larger-pivot control, costs and programs.
L262's actual form and earlier bounded tree are reused with their full author and review scopes; L226's bounded source screen is not an assertion of literature-wide absence.
D9/L191 supply their existing factor interfaces, whose elementary rank-two specialization is checked here.
No new source theorem or external-source proof audit is introduced.

The remaining target gate is now more specific.
Enlarging ONLY the final two-dimensional pivots cannot rescue any of these89 actual prefixes.
A changed earlier integer pivot/completion or a different realizing form is needed.
Conversely the explicit growing-pivot control disproves a general inference from a small cube to all integers, and the successful global mod2/mod3 bases prevent treating these local modular failures as a global congruence theorem.
No claim about modulo4 or coherent integral lifting follows.
The prescribed F=Phi6 P4 still has only its relaxed bilinear realization here, and no improved complete scalar cost or unrestricted near-one mechanism has been obtained.
The unrestricted mathematical problem remains unresolved; no Task/E execution resumes.
Full separately organized noncontributor review is required before fixed adoption.


### Actual whole checking and native boundary

The maintaining agent read the only actual L266 version, ENTIRE R165, all five J60 programs and all five native outputs, including every terminal/prefix/swap/bound, represented residue, full field basis and historical/current control matrix.
C456/C2/C458's complete mechanisms were compared rather than substituting a more general statement for the binary proof.
The full binary proof was checked for both directions, all signs/zero-leading cases, exact congruences, H isometry/scaling and the some-representative integer bound; every all-n height/cost/factor assertion and all negative domains were checked.
Only the original separately implemented reviewer run() was replayed stdout-only, in its unchanged V0/20000-prefix/200000-per-field/120-second domain, original moduli/fields/control parameters.
It completed in0.409seconds and reproduced ALL native report fields,6670calls/2170unique/89terminals/827residuepairs, both complete field witnesses and all symbolic/whole-factor/historical controls; all11 program/readme/native files stayed byte-identical.
The first comparison wrapper compared raw Python integer dictionary keys with JSON string keys; normalizing the returned report through JSON resolved that serialization-only mismatch, without a verifier failure, new mathematical choice or native edit.
No author program, historical defective program, new parameter/modulus, source proof/PDF, discovery or Task/E execution ran.
R165 disclosed claimed outcomes in the initial brief and author messages, so its ENTIRE original finding is SELF for known target-context sharing, not merely because of upstream D9/L262 roles.
The original proper-cover error, current correction and exact frozen09:56/review10:00 times remain distinct.
The current whole SELF is not fresh isolation and does not close any independent corrected-chain review obligation.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:06 |
| status | open |
| reason | Retain every original binary/all-n proof, finite prefix/residue/field witness, complete proper/relaxed factor and cost, original source context and historical cover-matrix correction. Existing C456/C2/C458 do not contain the complete terminal solver; no new source theorem or research execution is needed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole binary and prefix theorem](#statement) | Every determinant-one integer binary matrix/all integer norm-one vectors/all signs and degeneracies, exact finite solver, fixed89-terminal exclusion, actual p2/3 witnesses, all-n unbounded-pivot control and every complete factor/rank/height/energy/measure/negative boundary. |
| argument | [Entire retained proof](#argument) | All original Sections1--6/equations1--7, primitive Bezout/lower clearing, exact isometry/all-sign reduction/full congruence, every finite prefix/residue/field domain and full all-n proper-versus-relaxed costs/correction/source limits. |
| dependency | [Actual relaxed sextic and all costs](Yin_C_G0456_v1.md#argument) | Complete exact V0 exterior-square realization, original sextic and absolute/literal rank12 product, full root intervals and expenses, fixed old prefix choices; no proper unitriangular conclusion imported. |
| dependency | [Exact proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Complete identity-diagonal strict-upper sheet cover and entire original/absolute factor and total-measure conventions, specialized directly at rank2. |
| dependency | [Complete Gram determinant interface](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full bipartite determinant/absolute/cover identity, including both factors, neutral padding and all complete measures; only the elementary rank2 specialization is used. |
| support | [Actual quartic proper comparison](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Existing proper Phi2^2*P4 rank6/height1/energy5 and rank12/energy10 complete-cover measure2log beta4 comparison, not the target's unachieved proper basis. |
| support | [Original bounded source context](../ledger/Yin_L_G0226_v1.md#complete-retained-proof-and-review) | Original dlP19 Section2.4 endpoint-necessity/realization screen at2019 scope and bounded local search only, no external classification/Pell proof/novelty or literature-wide absence premise. |
| support | [Exact original native scope](../computations/programs/Yin_J_G0060/readme.md) | All5 original programs/5 native outputs,89 terminals/prefixes/complete residues/two full field witnesses/four historical-current controls and caps, with complete original-cost and proper-matrix negative preserved; no producer or expanded domain. |

### Decision explicit-quartic-factor-correction

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:07 |
| status | open |
| reason | Correct only the new v1 top-level P4 expansion to t4-t3-t2-t+1, whose Phi6 product is the already correct full F. Actual V0/full native F and complete original Argument were unchanged; preserve v1 open and the exact current-authoring negative. No original L266 mechanism defect, new producer/source proof or independent corrected-chain closure is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole binary and prefix theorem](#statement) | Every determinant-one integer binary matrix/all integer norm-one vectors/all signs and degeneracies, exact finite solver, fixed89-terminal exclusion, actual p2/3 witnesses, all-n unbounded-pivot control and every complete factor/rank/height/energy/measure/negative boundary. |
| argument | [Entire retained proof](#argument) | All original Sections1--6/equations1--7, primitive Bezout/lower clearing, exact isometry/all-sign reduction/full congruence, every finite prefix/residue/field domain and full all-n proper-versus-relaxed costs/correction/source limits. |
| dependency | [Actual relaxed sextic and all costs](Yin_C_G0456_v1.md#argument) | Complete exact V0 exterior-square realization, original sextic and absolute/literal rank12 product, full root intervals and expenses, fixed old prefix choices; no proper unitriangular conclusion imported. |
| dependency | [Exact proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Complete identity-diagonal strict-upper sheet cover and entire original/absolute factor and total-measure conventions, specialized directly at rank2. |
| dependency | [Complete Gram determinant interface](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full bipartite determinant/absolute/cover identity, including both factors, neutral padding and all complete measures; only the elementary rank2 specialization is used. |
| support | [Actual quartic proper comparison](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Existing proper Phi2^2*P4 rank6/height1/energy5 and rank12/energy10 complete-cover measure2log beta4 comparison, not the target's unachieved proper basis. |
| support | [Original bounded source context](../ledger/Yin_L_G0226_v1.md#complete-retained-proof-and-review) | Original dlP19 Section2.4 endpoint-necessity/realization screen at2019 scope and bounded local search only, no external classification/Pell proof/novelty or literature-wide absence premise. |
| support | [Exact original native scope](../computations/programs/Yin_J_G0060/readme.md) | All5 original programs/5 native outputs,89 terminals/prefixes/complete residues/two full field witnesses/four historical-current controls and caps, with complete original-cost and proper-matrix negative preserved; no producer or expanded domain. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:10 |
| status | proved |
| reason | Adopt after actual ENTIRE C466v2/R674 SELF inspection of every original binary/all-n proof, every original finite prefix/residue/field/native/full-cost/historical matrix-correction/source/negative scope and complete direct mechanisms. The new v1 explicit quartic-factor typo is corrected only in v2 and v1 stays open; whole Argument/native are unchanged. Original R165 is whole SELF from known claimed-outcome sharing, not fresh isolated coverage. Full original-domain reviewer stdout reproduces all report fields with11 original files unchanged; no author producer, new source proof/PDF/domain or Task execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole binary and prefix theorem](#statement) | Every determinant-one integer binary matrix/all integer norm-one vectors/all signs and degeneracies, exact finite solver, fixed89-terminal exclusion, actual p2/3 witnesses, all-n unbounded-pivot control and every complete factor/rank/height/energy/measure/negative boundary. |
| argument | [Entire retained proof](#argument) | All original Sections1--6/equations1--7, primitive Bezout/lower clearing, exact isometry/all-sign reduction/full congruence, every finite prefix/residue/field domain and full all-n proper-versus-relaxed costs/correction/source limits. |
| dependency | [Actual relaxed sextic and all costs](Yin_C_G0456_v1.md#argument) | Complete exact V0 exterior-square realization, original sextic and absolute/literal rank12 product, full root intervals and expenses, fixed old prefix choices; no proper unitriangular conclusion imported. |
| dependency | [Exact proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Complete identity-diagonal strict-upper sheet cover and entire original/absolute factor and total-measure conventions, specialized directly at rank2. |
| dependency | [Complete Gram determinant interface](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full bipartite determinant/absolute/cover identity, including both factors, neutral padding and all complete measures; only the elementary rank2 specialization is used. |
| support | [Actual quartic proper comparison](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Existing proper Phi2^2*P4 rank6/height1/energy5 and rank12/energy10 complete-cover measure2log beta4 comparison, not the target's unachieved proper basis. |
| support | [Original bounded source context](../ledger/Yin_L_G0226_v1.md#complete-retained-proof-and-review) | Original dlP19 Section2.4 endpoint-necessity/realization screen at2019 scope and bounded local search only, no external classification/Pell proof/novelty or literature-wide absence premise. |
| support | [Exact original native scope](../computations/programs/Yin_J_G0060/readme.md) | All5 original programs/5 native outputs,89 terminals/prefixes/complete residues/two full field witnesses/four historical-current controls and caps, with complete original-cost and proper-matrix negative preserved; no producer or expanded domain. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0674_v1.md#binary-current-whole-self-finding) | ENTIRE corrected statement/unchanged original argument, all integer/sign/degenerate/isometry/congruence cases, complete fixed prefixes/residues/full field witnesses, all-n/full original-absolute-proper-relaxed costs and every source/failure/negative limit; no new isolated corrected-chain review. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:48 |
| status | proved |
| reason | Adopt the new isolated complete C466v2 finding after coordinator reading of the entire57133-character R682. It covers every determinant-one integer/sign/degenerate/isometry/solver branch, full original prefix/terminal/modular/field domains, all-n height proof and every proper-versus-relaxed full factor/cost/source limit. The wrong v1 expansion and historical proper-matrix negative remain separate later SELF comparisons and give no old-v1 whole pass. Preserve R165/R674 SELF and all actual old/current dates; no global integer obstruction or new research authority. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every determinant-one integer binary matrix/all integer norm-one vectors/all signs and degeneracies, exact finite solver, fixed89-terminal exclusion, actual p2/3 witnesses, all-n unbounded-pivot control and every complete factor/rank/height/energy/measure/negative boundary. |
| argument | [Exact argument](#argument) | All original Sections1--6/equations1--7, primitive Bezout/lower clearing, exact isometry/all-sign reduction/full congruence, every finite prefix/residue/field domain and full all-n proper-versus-relaxed costs/correction/source limits. |
| dependency | [Exact dependency](Yin_C_G0456_v1.md#argument) | Complete exact V0 exterior-square realization, original sextic and absolute/literal rank12 product, full root intervals and expenses, fixed old prefix choices; no proper unitriangular conclusion imported. |
| dependency | [Exact dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Complete identity-diagonal strict-upper sheet cover and entire original/absolute factor and total-measure conventions, specialized directly at rank2. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full bipartite determinant/absolute/cover identity, including both factors, neutral padding and all complete measures; only the elementary rank2 specialization is used. |
| support | [Exact support](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Existing proper Phi2^2*P4 rank6/height1/energy5 and rank12/energy10 complete-cover measure2log beta4 comparison, not the target's unachieved proper basis. |
| support | [Exact support](../ledger/Yin_L_G0226_v1.md#complete-retained-proof-and-review) | Original dlP19 Section2.4 endpoint-necessity/realization screen at2019 scope and bounded local search only, no external classification/Pell proof/novelty or literature-wide absence premise. |
| support | [Exact support](../computations/programs/Yin_J_G0060/readme.md) | All5 original programs/5 native outputs,89 terminals/prefixes/complete residues/two full field witnesses/four historical-current controls and caps, with complete original-cost and proper-matrix negative preserved; no producer or expanded domain. |
| review | [Exact review](../audits/reviews/Yin_R_G0682_v1.md#binary-isolated-whole) | Entire exact corrected C466v2 Statement and complete Sections1--6 Argument, full original native/prefix/all-integer/domain/source/negative/proper-versus-relaxed costs. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0060](../computations/programs/Yin_J_G0060/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
