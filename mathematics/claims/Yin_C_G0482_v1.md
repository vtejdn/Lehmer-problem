---
author: Yin
---
# Coherent odd-prime triangular bases, one binary obstruction and complete integer costs

All original six sections/equations1--11 and both complete finite cost tables are retained.
L270 remains the meaningful exploration/failed branch/contribution/source record and original fixed review input; no mathematical Task/E resumes.
The [later complete comparison of original R169](../audits/reviews/Yin_R_G0697_v1.md#l270-and-r169) preserves its whole historical UNKNOWN, exact inputs/date/verdict/source/native/contribution limits and separate original author SELF.
The unchanged checking account and earlier decision below record the actual 2026-10-21T23:35 whole SELF,2026-10-21T23:36 adoption and then-retained original input, distinct from the selected 2026-10-22T00:06 new whole independent adoption.

## Statement

For EVERY integer n>=1, EVERY n-by-n integral bilinear form V with det V=1 and EVERY ODD prime p, suppose the specified Qbar in SL_n(F_p) makes Qbar^T*V*Qbar upper triangular with every diagonal entry+1.
There is a compatible Q in SL_n(Z_p), reducing to that Qbar, for which Q^T*V*Q is upper triangular with every diagonal+1.
Here Z_p means compatible residues modulo all p powers; positive pivot means+1 and imposes no order on Z_p.
The entire determinant/lower/first-n-minus-one-diagonal derivative is surjective: on upper-triangular right corrections its square restriction has determinant+/-2^(n-1), so the full compatible-residue construction works indefinitely.
Both nonsymmetric normalized-column elimination and direct derivative/Taylor proofs are included.
This conclusion is LOCAL; no integer or rational basis/local-to-global assertion follows and no prime2 square-root or full-rank assertion is imported.

For the ACTUAL integral form

    V0=[[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],
        [2,1,0,2,1,1],[0,-1,-1,0,-1,0],
        [1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]],
    F=det(t*V0+V0^T)=Phi6(t)*(t^4-t^3-t^2-t+1),
    det V0=1,

all original and cyclotomic factors remain.
The saved F3 basis is normalized from determinant2 to1 by its last-column sign; it lifts to an ACTUAL Q in SL_6(Z3), with complete pencil F.
The21-by-36 concrete derivative has rank21 and the retained selected integer minor16.
All three saved corrections at9,27,81 retain all21 selected equations, all SIX diagonal entries, all15 lower zeros, all seven full pencil coefficients and compatibility with the previous modulus.
Their finite nature is distinct from the two written infinite-lifting proofs.
No other odd-prime starting basis is supplied or tested.

For the saved unimodular Q2 class, the derivative has rank20, its left-kernel error pairing is1 and augmented rank21.
For EVERY integral correction R=Q2*(I+2X), the zero-based sum of Gram positions(4,1),(1,1)-1,(4,4)-1 stays2 modulo4, because the exact initial sum is-6 and its linear variation vanishes over F2.
Hence NO R in that WHOLE fixed modulo2 class gives upper-unitriangular Gram with diagonal1 modulo4, even without requiring exact det R=1.
This excludes no alternative F2 basis class or all integral realizations of F; rank deficiency alone is not the obstruction proof.

Retain EXACTLY the five saved INTEGER representatives at moduli2,3,9,27,81, with respective actual determinants

    1,1,-782,-11789414,1580171410.

For each Q, D=det Q, B=Q^T*V0*Q, A=-abs(B) entrywise and the literal full-entry two-sheet W satisfy the COMPLETE polynomial identity

    p_B=D^2*F, p_W=p_B*p_A,
    m(p_B)=2log(abs(D))+log beta4,
    m(p_W)=2log(abs(D))+log beta4+m(p_A),
    log(abs(leading(p_A)))<=m(p_A)<=log(sum(abs(coefficients(p_A)))),

where beta4>1 is the exterior root of t^4-t^3-t^2-t+1 and1<beta4<2.
Every B/A has rank6 and every W rank12; complete degrees are6,6,12, respectively.
NONE of these five integer B or W matrices is upper-unitriangular.
The entire reciprocal p_A coefficients/leading integers/content and every determinant/height/whole squared-entry energy/coefficient-l1 cost are retained in the two exact tables and full native arrays.
All five leading magnitudes are at least107, so each full representative cover has measure at least2log(abs(D))+log beta4+log107>2log beta4, exceeding the separate actual proper rank6/rank12 comparison.
The full-entry sheet splitting proves the factorization for all entries without properness;65 exact12-by-12 determinant evaluations independently check the complete degree12 polynomials, not just a selected factor.
The original V0 costs/rank6 height2 energy33 and literal rank12 energy66/strictly more than2log beta4 remain.
No real absolute-entry/Mahler expense is assigned to the limiting3-adic basis itself, and none of these five finite representative costs bounds a future integer lift or optimizes over other bases.
No global prime compatibility, proper integral target construction, ordinary small-measure or unrestricted gap theorem follows.

<a id="argument"></a>
## Complete original argument

The complete original author text follows.
Its pilot/declaration/pending-review/active-route sentences describe the original2026-10-10 development, not current execution authority; the selected assessment below governs this retained home.

<a id="coherent-local-triangularization-scope"></a>
### 1. Reuse and declared changed test

Date:2026-10-10.
[L262](Yin_C_G0456_v1.md#argument) gives the exact integral zero-diagonal form V0, det V0=1, and complete determinant F=Phi6 P4.
[L266](Yin_C_G0466_v2.md#statement) excludes every integer final pivot after its prescribed small-coordinate prefixes, but supplies actual positive triangular bases for the ORIGINAL V0 over F2 and F3.
This round changes the whole local-basis interface, without enlarging that excluded terminal search.

The needed intermediate mechanism is the familiar polynomial/Hensel lifting procedure.
A bounded local screen located [L64's elementary complete-ring lifting proof](Yin_C_G0241_v1.md#direct-etale-frobenius-lift), which addresses one variable and not this whole matrix system; registered Stacks formal-parameter material does not directly assert the p-adic basis conclusion.
A precise primary statement is being inspected for attribution.
The matrix-specific constraints and finite certificates below will have a direct proof; no novel general Hensel theorem or literature-wide absence is claimed.

The declared finite test uses ONLY p=2 and p=3 and the two actual bases retained in [J60](../computations/programs/Yin_J_G0060/readme.md).
Normalize the determinant to1 modulo p by changing the sign of the last column when necessary.
Such a diagonal sign congruence preserves each diagonal1 and every lower zero.
At a basis Q impose det Q=1, all15 strict-lower entries of Q^T V0 Q equal0, and its FIRST FIVE diagonal entries equal1.
These21 polynomial equations imply the last diagonal1 whenever Q is invertible: the transformed determinant is(det Q)^2 det V0=1 and the first five diagonal factors are1.
Do not divide by2 or assume an arbitrary field witness already has determinant1.

Compute the complete21-by-36 derivative with respect to the right correction Q -> Q(I+epsilon X), including tr X from the determinant equation.
Retain its exact row rank, pivot columns and a nonzero maximal minor modulo p if it has full row rank.
If full rank holds, construct compatible corrections only through p^4, verifying ALL36 transformed entries required for triangularity, determinant1 modulo the current modulus, and every coefficient of the entire degree-six pencil polynomial.
The declared runtime cap is120 seconds for these two tests, with at most three correction steps per prime.
If the derivative is deficient or a correction inconsistent, preserve that exact result and stop rather than scanning other starting bases or primes.
All continuing code and outputs belong to [J61](../computations/programs/Yin_J_G0061/readme.md); no integral basis, positive ordinary Mahler bound or complete prime set follows merely from these finite controls.

The first declared run completed with rank21 at p=3 (the retained pivot minor has integer determinant16), and all three exact corrections through modulus81 passed.
At p=2 the rank is20, so that branch stopped as declared before any correction.
Rank deficiency alone does not prove a lift obstruction.
The following extension is declared before execution: use precisely the SAME normalized modulo2 basis, compute the one-dimensional left kernel of the21-by-36 derivative, pair it with the actual first error quotient, and decide the single linear congruence for a correction modulo4.
Retain a complete linear consistency or inconsistency certificate and, only if consistent, one resulting basis modulo4 with full constraint checks.
No alternative starting basis, higher power at2 or new prime is searched; this added check has a120-second cap.


<a id="odd-prime-coherent-triangular-basis"></a>
### 2. A reusable odd-prime lifting theorem

Let V be any n-by-n integral matrix of determinant1 and p an ODD prime.
Suppose Qbar in SL_n(F_p) gives Ubar=Qbar^T V Qbar upper triangular with every diagonal1.
Then there is Q in SL_n(Z_p), reducing to Qbar, such that U=Q^T V Q is upper triangular with every diagonal1.
Here Z_p means compatible residues modulo all p powers.
The word positive in a positive unit pivot denotes the entry+1; it does not order Z_p.
This conclusion is LOCAL and asserts no integer or rational basis.

The elementary proof can reuse exactly the single-variable complete-ring lifting mechanism in [L64](Yin_C_G0241_v1.md#direct-etale-frobenius-lift).
Lift Qbar to an integer matrix Q0.
Its determinant is a p-adic unit, so its columns are a Z_p basis.
Its bilinear Gram B=Q0^T V Q0 reduces to Ubar.
Its first norm a is congruent to1 modulo p.
The equation s^2=a has a unique solution s=1 modulo p: the derivative2s is a unit and the L64 Newton proof applies.
Divide the first column v by s to make its norm1, and replace every other column w by w-B(w,v)v, using the NORMALIZED v.
This clears the lower first column exactly.
Since the lower pairings vanish modulo p and s=1 modulo p, the basis is unchanged modulo p.
The remaining Gram still reduces to the corresponding upper unitriangular submatrix.
Repeat in every dimension.
All operations are invertible over Z_p and preserve the specified reduction, so the final U is upper triangular with diagonal1.
Its determinant is1, hence(det Q)^2 det V=1.
Because det V=1 and det Q=1 modulo the odd prime, det Q=+1: Z_p is a domain, the only roots of z^2-1 are+1 and-1, and-1 has the wrong residue.
This proves the theorem.
The case n=1 is included directly.

For completeness the corresponding full-constraint derivative has a particularly simple exact rank proof.
At any upper-unitriangular U over a field of odd characteristic take the infinitesimal right correction I+epsilon X.
The variation of the Gram and determinant is

    dU=X^T U+UX,      d(det Q)=tr X                 (1)

when det Q=1.
Retain every strict-lower equation, the first n-1 diagonal equations and the determinant equation, in that order.
Restrict X to upper-triangular matrices.
For i>j,

    (dU)_(i,j)=sum_(k<=j) X_(k,i) U_(k,j).          (2)

For each fixed i, successively increasing j determines X_(j,i), because U_(j,j)=1.
Thus the strictly upper entries of X solve all lower errors, without using its diagonal.
After those are fixed,

    (dU)_(i,i)=2 X_(i,i)+sum_(k<i) X_(k,i) U_(k,i).
                                                            (3)

The first n-1 diagonal errors determine X_(i,i) using the inverse of2.
The determinant error then determines the final diagonal entry through tr X.
Hence this square n(n+1)/2-dimensional restriction is invertible; its determinant is+/-2^(n-1), after any fixed ordering of equations and these variables.
This argument is valid for every U and every odd prime, not inferred from the one p=3 numerical instance.
At characteristic2 the division is unavailable, and no full-rank claim is made.

Here is also the explicit compatible-residue version used by the finite program.
Put F(Q) equal to the determinant-minus-one, strict-lower, and first n-1 diagonal-minus-one constraints.
If F(Q_r)=0 modulo p^r, choose X_r modulo p solving

    J_(Qbar) X_r=-F(Q_r)/p^r modulo p,
    Q_(r+1)=Q_r(I+p^r X_r) modulo p^(r+1).          (4)

Taylor expansion has remainder divisible by p^(2r), hence by p^(r+1).
The same derivative modulo p remains valid at every step since Q_r has the same reduction; equation(1) uses det Q_r=1 modulo p.
The surjectivity just proved therefore solves(4) indefinitely.
The exact lower zeros and first n-1 unit diagonal entries in the limit force the last diagonal1 by its determinant.
This is the elementary multivariable form of the same Hensel mechanism, not a new general lifting theorem.
The familiar source attribution and actual inspection limits are recorded in Section6; neither proof assumes a local-to-global principle.

<a id="actual-three-adic-triangularization"></a>
### 3. The actual sextic over Z3

Use exactly L262's V0 and F=Phi6 P4.
The J60 witness has determinant2 modulo3.
Negating its last column preserves upper triangularity and every diagonal1 under congruence and changes the determinant to1.
Its normalized least nonnegative representative is

    Q3=[
       [1,2,0,1,2,0],
       [0,0,0,1,2,2],
       [0,1,1,0,0,0],
       [0,0,1,2,2,1],
       [0,2,2,1,2,1],
       [1,2,2,2,1,0]].                              (5)

Consequently Section2 proves an ACTUAL Q in SL_6(Z3) for which Q^T V0 Q has all lower entries0 and all diagonal entries1, with COMPLETE determinant polynomial F.
The last statement follows from the exact congruence identity det(tQ^T V0 Q+(Q^T V0 Q)^T)=(det Q)^2 F=F.
No original or cyclotomic factor is removed.
This is a realization over Z3, not over Z.

The independently reviewable finite author certificate computes the entire21-by-36 derivative at(5), with variables X_(i,j) in row-major order.
It has rank21.
The retained pivot columns (zero-based) are

    0,1,2,3,4,5,6,8,9,10,11,13,15,16,17,19,22,23,24,29,35,

and the corresponding actual integer minor has determinant16, a3-adic unit.
This is a separate concrete certificate, not a replacement for Section2's general proof.
Exactly three corrections were executed, at moduli9,27,81.
Every one satisfies determinant1, all six diagonal-one constraints, all15 lower zeros, and every one of the seven coefficients of F modulo its modulus; successive bases agree at the previous modulus.

At modulus81 the retained representative and transformed Gram are

    Q81=[
       [1,71,9,64,2,24],
       [0,27,0,1,77,62],
       [12,19,64,75,24,54],
       [0,72,1,56,29,61],
       [24,38,47,43,62,64],
       [1,26,11,11,55,72]],

    Q81^T V0 Q81 modulo81=[
       [1,70,32,75,15,69],
       [0,1,80,15,16,57],
       [0,0,1,41,74,12],
       [0,0,0,1,43,21],
       [0,0,0,0,1,15],
       [0,0,0,0,0,1]].                              (6)

The finite check stops at its declared p^4; infinite coherent lifting follows from the written theorem, not from extrapolation of three steps.
No other odd prime was tested, and existence of its starting field basis is still a hypothesis of Section2.

<a id="actual-two-adic-branch-obstruction"></a>
### 4. An actual modulo2 basis that cannot lift even modulo4

The retained J60 modulo2 basis is

    Q2=[
       [0,0,0,0,1,1],
       [1,1,1,1,1,1],
       [0,1,1,1,1,1],
       [0,0,0,1,1,0],
       [1,1,1,0,0,0],
       [1,1,0,0,0,1]].                              (7)

It has determinant1 over Z.
Its integer Gram B=Q2^T V0 Q2 is already upper-unitriangular MODULO2.
Every integer matrix R reducing to Q2 modulo2 can be written R=Q2(I+2X) with integral X, since Q2 is unimodular; equivalently this parametrizes every correction modulo4.
Its Gram is

    R^T V0 R=B+2(X^T B+BX) modulo4.                 (8)

Let ell(H)=H_(4,1)+H_(1,1)+H_(4,4), with all indices zero-based.
Directly from the retained upper Gram U2=B modulo2, which has off-diagonal ones exactly at(0,3),(1,4),(2,5),(3,5), one obtains

    ell(X^T U2+U2 X)=0 modulo2 for EVERY X.          (9)

Indeed its(4,1) entry is X_(1,4)+X_(4,1), its(1,1) entry is X_(4,1), and its(4,4) entry is X_(1,4), modulo2.
Each variable occurs twice.
The exact integer Gram B instead satisfies

    B_(4,1)+(B_(1,1)-1)+(B_(4,4)-1)=-6.             (10)

Equations(8)--(10) prove that this sum remains2 modulo4 throughout the entire residue class of Q2.
A positive upper-unitriangular Gram modulo4 would make it0.
This is a contradiction.
Therefore NO matrix R congruent to Q2 modulo2, even allowing any invertible determinant rather than imposing det R=1, gives an upper-unitriangular Gram with diagonal1 modulo4.
In particular no integer unimodular or2-adic triangular basis lies in that residue class.

The complete derivative test first found rank20, not21.
Its unique left-kernel vector has ones precisely on the three constraint rows in(9) and zero on the determinant row.
The actual error quotient pairing is1 modulo2, and the augmented system has rank21.
The program retains the full vectors and matrices; equations(8)--(10) give a short proof independent of trusting a rank computation.
Failure is confined to THIS residue-class basis.
The fact that another modulo2 basis might lift remains unresolved; no search over alternative bases or higher powers of2 was performed.
This result sharpens the earlier observation that a finite-field witness alone supplies no coherent lift, without excluding all integral realizations of F.


<a id="local-witness-complete-costs"></a>
### 5. Integral representatives, full factors and the cost boundary

Neither a3-adic matrix nor its congruence class has an ordinary real entrywise absolute value or an Archimedean Mahler cost.
The local theorem is therefore NOT a proper integral companion construction.
Its exact local polynomial remains F, but it supplies no integer entry-height, energy or favorable full-cover estimate.

To retain the expenses of the actual finite witnesses without mislabelling them, the following cost-only verification is declared before execution.
Use exactly the five already retained integer representatives: Q2 and the normalized modulo3,9,27,81 bases.
For each Q form B=Q^T V0 Q over Z, with D=det Q.
Verify the COMPLETE identity p_B=D^2 F, keep the full-entry absolute A=-|B| and the literal full-entry rank12 lift W from L262, and compute ALL coefficients of p_A and p_W=p_B p_A.
Direct evaluation of the actual12-by-12 determinant at13 distinct integers independently checks the latter polynomial equality.
Retain actual ranks, determinants, entry heights, whole squared-entry sums and whether the matrices are genuinely integer upper-unitriangular.
This is five fixed cost checks, not another basis or modulus search; its runtime cap is120 seconds.
An identically zero absolute/lift polynomial, if encountered, must be reported without assigning a finite logarithmic measure.

For every nonzero absolute factor the exact measure identity and explicit coefficient bounds are

    m(p_B)=2 log|D|+log beta4,
    m(p_W)=2 log|D|+log beta4+m(p_A),
    0<=m(p_A)<=log(sum_j |[t^j]p_A|).               (11)

The first equation retains the ENTIRE constant factor D^2; the second retains every original and absolute factor.
The upper bound follows from the circle triangle inequality and integrability of log of a nonzero polynomial.
Since p_A is a nonzero integer polynomial, its entire Mahler measure is nonnegative.
No primitive-factor cancellation is represented as an actual matrix realization.
For any B of height H one can alternatively use log(6!)+6log(2H) as a coarse bound on its entire determinant polynomial when nonzero.
These bounds are exact in scope, not optimized estimates or an energy-to-measure replacement.
The whole squared-entry sums for B and A agree, and W doubles them; both properness and determinant degree are checked explicitly rather than inferred from a product alone.

The original fixed V0 itself keeps every L262 cost: rank6, height2, whole squared-entry sum33, full-entry absolute factor -(t^6-7t^4-11t^3-7t^2+1), and literal rank12 lift with whole sum66 and total measure GREATER than2log beta4.
The achieved proper L191 Phi2^2 P4 construction remains a separate cheaper comparison with full cover Phi2^4 P4^2 and measure2log beta4.
This round changes local solvability information, not these accepted integral costs.


All five cost checks completed.
Every B and A has rank6, and every literal W has rank12; degrees are6,6,12 respectively.
NONE of the five integer B or W matrices is upper-unitriangular.
For the reciprocal absolute factor write

    p_A=a(t^6+1)+b(t^5+t)+c(t^4+t^2)+d t^3.

The complete coefficients, including the leading integer and any content, are:

| modulus | a | b | c | d |
| --- | ---: | ---: | ---: | ---: |
| 2 | 107 | 280 | -79 | -529 |
| 3 | -49463 | -192338 | -314339 | -346177 |
| 9 | -11291866964 | -38791043408 | -54211454312 | -53546967832 |
| 27 | -1975611420550502506 | -10257506675639983384 | -23407968648817491070 | -30258083148167139908 |
| 81 | -31219449814105681832650 | -88079821954388452367420 | -73791062068852493583644 | -34278942068814164794772 |

Together with p_B=D^2 F and p_W=D^2 F p_A these specify every polynomial coefficient and factor, without numerical root approximations.
The actual integer costs are:

| modulus | D=det Q | height B=height A=height W | E_all(B)=E_all(A) | E_all(W) | coefficient norm of p_A |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2 | 1 | 6 | 362 | 724 | 1461 |
| 3 | 1 | 15 | 2356 | 4712 | 1458457 |
| 9 | -782 | 342 | 618796 | 1237592 | 262135697200 |
| 27 | -11789414 | 3807 | 113442400 | 226884800 | 101540256638183093828 |
| 81 | 1580171410 | 28998 | 6876770680 | 13753541360 | 420459609743507420362200 |

Here the coefficient norm is the sum in(11), not a numerical Mahler evaluation.
Since the leading coefficient of every p_A has magnitude at least107, each ENTIRE representative cover has measure at least2log|D|+log beta4+log107, which is greater than2log beta4.
Thus even ignoring the failure of the integer triangular condition, none of these five local representatives improves the proper L191 complete-cover comparison.
This is not a bound on a future integer lift or an optimum over other bases.
The exact12-by-12 determinant was checked at all13 declared integers for every W, in addition to the explicit sheet decomposition proving the whole identity.
The matrices and full expanded degree12 polynomials are retained in J61's cost certificate (`mathematics/computations/outputs/Yin_J_G0061/cost_result.json`).

<a id="local-triangular-lifting-source-and-execution"></a>
### 6. Attribution, actual execution and remaining scope

The standard lifting mechanism is attributed to the already registered [The Stacks Project, The26b](../audits/literature/The26b/Yin_U004.md#the26b-u004) and specifically the official [Henselian local rings section, Tag04GE](https://stacks.math.columbia.edu/tag/04GE), accessed2026-10-10.
Definition10.153.1 and Lemma10.153.3(1)--(2) state the simple-root lifting criterion, including the nonmonic equivalent.
For s^2-a over Z_p the residual root1 is simple exactly at the odd primes used in Section2.
The displayed HTML statements and the nearby uniqueness proof were read; the whole equivalence proof, its deeper etale inputs and the existing retained chapter PDF were NOT audited in this round.
Existence in the complete ring is supplied by the directly read L64 Newton proof, and the actual successive pivot/constraint argument is fully written above.
This is checked attribution plus local proof, not acceptance of a new whole-source theorem.

The broader official Tag09XI henselian-pair equivalence was inspected as a possible route but is not needed.
Two unrelated Stacks tags returned by a further locator attempt supplied no input and are not attributed as relevant theorems.
A primary-author search lead, Joshua Grochow's A note on multivariate Hensel lifting, was located; a direct tool attempt to open its author-hosted PDF timed out.
It was not inspected, adopted, registered as a new input or used to infer an exact statement.
The simpler existing single-variable input made further acquisition unnecessary.
No new source-home or shared-registry write was performed, and no priority or literature-wide absence claim is made.

The three author programs completed their declared domains within their120-second caps.
All mathematical arithmetic is exact integer, rational or modular.
The first result's rank20 and declared stop at2 are preserved rather than relabelled as a successful Hensel step.
The subsequently declared modulo4 test has a separate program/output.
No other basis, prime, higher power, underlying root search or cost optimization was attempted.
No native program required a correction after its first execution; the proof distinguishes derivative deficiency, an actual incompatible error and a merely unproved global conclusion.

The author's self-check revisited the last-column sign at3;
the determinant equation and omitted-final-diagonal implication at every modulus;
the triangular restriction of the general derivative; the normalized-first-column convention in nonsymmetric elimination;
the exact three-entry identity at2;
and all real versus p-adic, proper versus full-entry and unimodular versus finite-index cost boundaries.
In particular, a least-residue basis modulo81 need not have determinant+/-1 over Z: its actual determinant1580171410 is retained and produces the charged constant square, not a silently primitive polynomial.
The modulo2 obstruction fixes the whole residue class of Q2 and does not contradict a different local branch.
The local3-adic theorem and the finite tests are independently justified parts of the result.

The coordinator assigned the broad continuation question and J allocation, warned about the known modulo3 determinant2, and authorized the separately declared compatibility check after the author reported the first ranks.
The author had already included determinant normalization in the declared system.
All current mathematical derivations and programs are by orbit_research AI for Yin; prior reviewed L262/L266 and L64 mechanisms are reused with their stated roles.
These are contribution disclosures, not an independent review.
Full noncontributor review is required before fixed adoption.

The next genuine integer question must use another modulo2 basis class, different earlier pivots/completions, or a different realizing bilinear form.
The present class of Q2 is excluded outright, whereas the displayed Q3 class is coherently unobstructed at every3 power.
No compatibility across all primes, integral local-to-global principle, positive integer triangular basis for Phi6 P4, optimized complete cost or unrestricted near-one gap has been proved.
All mathematical routes remain active; stopping the declared experiment does not pause or refute a route.

The author self-check covers complete Sections1--6, equations(1)--(11), all three exact programs and retained outputs.

### Actual whole checking and preserved limits

The maintaining agent read every line of the only L270 version and ENTIRE R169, all four J61 sources and all four native JSON records, plus the readme and actual J60 field-input payload.
The complete C456/C466v2/C241/C458v2 mechanisms are sufficiently reused after comparison; no existing home supplied this entire odd-prime/coherent-residue/same-class-parity/all-five-cost proof.
The nonsymmetric normalized-pivot order, specified reduction and odd-prime determinant sign were checked separately from the full upper-X derivative/trace/last-diagonal/Taylor proof, including n1.
Every concrete3-adic normalization/minor/correction/polynomial coefficient, characteristic2 whole-class functional and actual error pairing, every full factor/rank/degree/height/energy/leading/coefficient cost and cheaper quartic comparison was checked without dropping determinant squares or neutral factors.
Only the original standard-library reviewer main was replayed in its complete unchanged original domain/cap: both fields, saved9/27/81 steps, sameQ2mod4, five costs/65nodes and the three original reversed-priority controls.
It completed in0.15632329997606575seconds within120seconds; every normalized JSON field equals the retained reviewer report and all ten original source/readme/native/J60-input files stayed byte-identical across replay.
No author producer/import, new field/basis/modulus/cost search/output/source passage/PDF/proof inspection or Task/E execution occurred.
The original author whole SELF remains at recorded2026-10-10 day precision; the separate 2026-10-10T02:34 original review completion is not invented as an author-check/source-read minute.
R169's assignment/author progress explanations are disclosed, but the retained record does not specify their exact additional initial target contents/order; upstream reviewing or generic signed-cover authorship alone proves neither a target contribution nor isolation.
Its ENTIRE whole finding remains UNKNOWN with precise old inputs, whole verdict/date/body and all original source/native/two-run-label/negative boundaries retained; current whole SELF supplies no fresh isolated replacement.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:34 |
| status | open |
| reason | Retain the ENTIRE original odd-prime normalized-basis/coherent-residue theorem and two direct proofs, actual3-adic branch/sameQ2mod4 obstruction/all five exact integer representative factor and cost tables, with every source/native/contribution/failed/global-limit boundary. Adequate prior interfaces are reused without substituting their narrower statements for this complete proof; actual whole finding/adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire local/cost theorem](#statement) | Every n>=1/integral det-one nonsymmetric form/every odd prime and specified SL field basis, full coherent lift/derivative; actual sextic3-adic branch/singleQ2mod4 exclusion and all five full integer representative costs/negative boundaries. |
| argument | [Entire complete proof](#argument) | All original Sections1--6/equations1--11/Q2/Q3/Q81 and full transformed matrices/two exact cost tables, both infinite local proofs/parity identity/all derivative and representative/source/execution/contribution limits. |
| dependency | [Actual V0 and full-entry sheet proof](Yin_C_G0456_v1.md#argument) | Entire determinant-one actual sextic V0/full Phi6 P4 pencil and nontriangular full-entry absolute/literal-sheet decomposition, with all original/absolute/cover factors, not a proper integer companion. |
| dependency | [Exact original field witnesses and prefix limit](Yin_C_G0466_v2.md#finite-field-positive-basis-discriminator) | Actual original J60 F2/F3 positive triangular bases and det2-at3 guard; no rerun of earlier6670-call or846532-candidate producer and no enlarged terminal exclusion. |
| dependency | [Complete-ring simple-root Newton proof](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Only elementary Newton/error-squaring and factored-difference uniqueness in the fixed residue class, applied to s^2-a over Z_p at odd p; surrounding unramified Frobenius theorem is not imported. |
| dependency | [Proper rank6-to12 quartic comparison](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Explicit actual k4 rank6 height1/E5 Phi2^2 P4 proper construction and entire rank12 height1/E10 Phi2^4 P4^2 cover/measure2log beta4, with beta4<2; no neutral factor deletion or finite-index primitive cancellation. |
| support | [Exact original simple-root attribution](../audits/literature/The26b/Yin_U004.md#the26b-u004) | Distinct original10/10 author/reviewer official Tag04GE statements/nearby uniqueness-proof reading, unknown exact read minutes/snapshot, uninspected full equivalence/etale/chapter PDF and unadopted Tag09XI/Grochow-timeout scope; no new source reading. |
| support | [Fixed full native certificate](../computations/programs/Yin_J_G0061/readme.md) | Original two field bases/21-by-36 systems/3-adic steps only9,27,81/singleQ2mod4/five integer cost representatives/65 literal determinant nodes and three original reviewer reverse-priority controls, all exact. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:36 |
| status | proved |
| reason | Adopt after actual complete C482/R693 whole SELF check of all original Sections1--6/equations1--11/two full cost tables, both odd-prime coherent-lifting proofs/full derivative, actual3-adic branch/singleQ2mod4 obstruction/every determinant-square/original-absolute-cover polynomial/leading/rank/degree/height/energy/cost and source/native/global negative boundary. Original-domain reviewer-only replay matched every native field with all ten files unchanged. R169 retains its ENTIRE original UNKNOWN scope and original author day-precision SELF; no fresh isolated review, all-basis2-adic/global integral theorem, new source proof/producer/domain/output or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire local/cost theorem](#statement) | Every n>=1/integral det-one nonsymmetric form/every odd prime and specified SL field basis, full coherent lift/derivative; actual sextic3-adic branch/singleQ2mod4 exclusion and all five full integer representative costs/negative boundaries. |
| argument | [Entire complete proof](#argument) | All original Sections1--6/equations1--11/Q2/Q3/Q81 and full transformed matrices/two exact cost tables, both infinite local proofs/parity identity/all derivative and representative/source/execution/contribution limits. |
| dependency | [Actual V0 and full-entry sheet proof](Yin_C_G0456_v1.md#argument) | Entire determinant-one actual sextic V0/full Phi6 P4 pencil and nontriangular full-entry absolute/literal-sheet decomposition, with all original/absolute/cover factors, not a proper integer companion. |
| dependency | [Exact original field witnesses and prefix limit](Yin_C_G0466_v2.md#finite-field-positive-basis-discriminator) | Actual original J60 F2/F3 positive triangular bases and det2-at3 guard; no rerun of earlier6670-call or846532-candidate producer and no enlarged terminal exclusion. |
| dependency | [Complete-ring simple-root Newton proof](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Only elementary Newton/error-squaring and factored-difference uniqueness in the fixed residue class, applied to s^2-a over Z_p at odd p; surrounding unramified Frobenius theorem is not imported. |
| dependency | [Proper rank6-to12 quartic comparison](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Explicit actual k4 rank6 height1/E5 Phi2^2 P4 proper construction and entire rank12 height1/E10 Phi2^4 P4^2 cover/measure2log beta4, with beta4<2; no neutral factor deletion or finite-index primitive cancellation. |
| support | [Exact original simple-root attribution](../audits/literature/The26b/Yin_U004.md#the26b-u004) | Distinct original10/10 author/reviewer official Tag04GE statements/nearby uniqueness-proof reading, unknown exact read minutes/snapshot, uninspected full equivalence/etale/chapter PDF and unadopted Tag09XI/Grochow-timeout scope; no new source reading. |
| support | [Fixed full native certificate](../computations/programs/Yin_J_G0061/readme.md) | Original two field bases/21-by-36 systems/3-adic steps only9,27,81/singleQ2mod4/five integer cost representatives/65 literal determinant nodes and three original reviewer reverse-priority controls, all exact. |
| review | [Actual complete whole SELF](../audits/reviews/Yin_R_G0693_v1.md#coherent-local-whole-self-finding) | Entire exact statement/argument/selected inputs, all six original sections/11equations/full two cost tables and every odd-prime/all-dimension/specified-field-basis/actual3-adic/sameQ2mod4/full integer representative/source/native/negative limit; no fresh isolated replacement or narrow-only finding. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:06 |
| status | proved |
| reason | Adopt the actual fresh whole independent finding after directly reading the entire R697, its exact fixed Statement/Argument coverage, real initial and post-comparison sequence, all source/native/negative limits and disclosed repeated-scope exposure. Preserve original whole UNKNOWN, original author SELF, prior current whole SELF and every actual date, accepted input and unrestricted boundary. No historical independence is backfilled and no Task/E resumes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every n>=1/integral det-one nonsymmetric form/every odd prime and specified SL field basis, full coherent lift/derivative; actual sextic3-adic branch/singleQ2mod4 exclusion and all five full integer representative costs/negative boundaries. |
| argument | [Exact argument](#argument) | All original Sections1--6/equations1--11/Q2/Q3/Q81 and full transformed matrices/two exact cost tables, both infinite local proofs/parity identity/all derivative and representative/source/execution/contribution limits. |
| dependency | [Exact dependency](Yin_C_G0456_v1.md#argument) | Entire determinant-one actual sextic V0/full Phi6 P4 pencil and nontriangular full-entry absolute/literal-sheet decomposition, with all original/absolute/cover factors, not a proper integer companion. |
| dependency | [Exact dependency](Yin_C_G0466_v2.md#finite-field-positive-basis-discriminator) | Actual original J60 F2/F3 positive triangular bases and det2-at3 guard; no rerun of earlier6670-call or846532-candidate producer and no enlarged terminal exclusion. |
| dependency | [Exact dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Only elementary Newton/error-squaring and factored-difference uniqueness in the fixed residue class, applied to s^2-a over Z_p at odd p; surrounding unramified Frobenius theorem is not imported. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Explicit actual k4 rank6 height1/E5 Phi2^2 P4 proper construction and entire rank12 height1/E10 Phi2^4 P4^2 cover/measure2log beta4, with beta4<2; no neutral factor deletion or finite-index primitive cancellation. |
| support | [Exact support](../audits/literature/The26b/Yin_U004.md#the26b-u004) | Distinct original10/10 author/reviewer official Tag04GE statements/nearby uniqueness-proof reading, unknown exact read minutes/snapshot, uninspected full equivalence/etale/chapter PDF and unadopted Tag09XI/Grochow-timeout scope; no new source reading. |
| support | [Exact support](../computations/programs/Yin_J_G0061/readme.md) | Original two field bases/21-by-36 systems/3-adic steps only9,27,81/singleQ2mod4/five integer cost representatives/65 literal determinant nodes and three original reviewer reverse-priority controls, all exact. |
| review | [Exact review](../audits/reviews/Yin_R_G0697_v1.md#c486-whole-independent-finding) | Entire exact statement/argument/selected inputs, all six original sections/11equations/full two cost tables and every odd-prime/all-dimension/specified-field-basis/actual3-adic/sameQ2mod4/full integer representative/source/native/negative limit; whole new independent review, with prior whole SELF, original whole UNKNOWN and original complete author SELF retained at their own actual scopes. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0060](../computations/programs/Yin_J_G0060/readme.md#reproducing-reviewed-runs), [Yin_J_G0061](../computations/programs/Yin_J_G0061/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
