---
author: Yin
---
# Universal proper-sextic coefficient obstruction, all signed-unit forms and full costs

The complete original proof, necessary native evidence, construction/failures, contribution and cost boundaries are retained.
The original L remains meaningful exploration and a fixed original review input; its historical active/pending wording does not resume the research Task/E.

## Statement

For EVERY integral UPPER-unitriangular6-by6 matrix U, with no bound on entries, signs, energy, ordering, basis or bilinear-form class, transposition gives

    p_U(t)=det(tU+U^T)
          =t^6+a(U)t^5+b(U)t^4+c(U)t^3+b(U)t^2+a(U)t+1.

If (a,b,c) has parity(0,1,1), then NECESSARILY

    (a,b,c) modulo4 is(2,3,3) or(0,1,3),
    c=3 modulo4 and a+b=1 modulo4.

These are necessary residue conditions, not a prescribed-polynomial sufficiency theorem.
In particular NO such U has either COMPLETE target

    F=Phi6*P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    P4=t^4-t^3-t^2-t+1,
    S6=t^6-t^4-t^3-t^2+1.

Both targets have the required parity and a+b=-1, violating the necessary class.
The conclusion concerns proper rank6 integer realizations across ALL forms/lattices/orderings, not only a basis orbit of the exterior form.

The complete finite certificate is retained at J65.
ALL32768 binary strict-upper masks and the exact INTEGER coefficient-polynomial expansion

    f(U0+2X)=f(U0)+2 Df(U0)X modulo4

represent ALL4^15=1073741824 upper-entry residues.
Exactly375 binary bases have target parity; each has f(U0)=(2,3,3) modulo4 and complete derivative image{000,011}, with(a,b,c) in bits0,1,2.
Every one of5625 derivative columns, every integer base triple/right side and every witness3 is retained.
The unfiltered determinant-permutation/Boolean author cross-check and original independent subset-determinant/cofactor derivative implementation cover the complete parity domain without relying on the annihilator or cyclic screen.
There was no literal billion-case loop, bounded-height extrapolation, floating comparison or bit-flip substitute for the step-two derivative.
The necessary prefilter's390 forms include15 noncyclic controls; parity coverage is not inferred from the375 cyclic cases alone.

The changed-form construction and its complete expenses remain substantive parts of the result.
Use the ACTUAL standard-lattice matrix

    V=[[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],
       [2,1,0,2,1,1],[0,-1,-1,0,-1,0],
       [1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]],
    C=-V^-1 V^T, R=C^2+C^-2.

The exact identities are det V=det C=det R=1, C^T V C=V, R^T V=VR, RC=CR, and both R and R^-1 are integral.
The trace factorization F=t^3(y-1)(y^2-y-3), y=t+t^-1, proves det R=1 exactly, without a full unit-group or lattice classification.
For EVERY n in Z and epsilon in{+1,-1},

    B_(epsilon,n)=epsilon V R^n,
    B_(epsilon,n)^T=-B_(epsilon,n)C,
    det(t B_(epsilon,n)+B_(epsilon,n)^T)=F.

For EVERY integer k and e in{0,1}, congruence by the actual unimodular Q=R^k gives

    Q^T(epsilon V R^e)Q=epsilon V R^(2k+e).

Thus positive upper-unitriangular integer-basis existence for the ENTIRE signed integer-power family reduces to V,-V,VR,-VR, without claiming these are distinct or exhaustive among all forms with pencil F.
V retains the fixed C496 obstruction.
For EACH of the THREE new representatives -V,VR,-VR, the original complete actual Gram test has375 forms and5625 binary bases, with ALL21 lower-plus-diagonal modulus4 equations inconsistent for every basis.
Original independent norm-one-column recursion reproduces the complete basis SET and checks all16875 witnesses, rank19 derivative systems and complete two-dimensional left kernels.
The old V classification was reused, not rerun by this changed-form author program.
No family member has a positive upper-unitriangular integer basis, and the universal coefficient theorem also excludes EVERY other form with either displayed full target at this rank.

For EACH representative B, define the full-entry A=-abs(B) and literal rank12 lift W_cov by replacing b<=0 with b I2 and b>0 with -b times the two-sheet swap, INCLUDING diagonal and lower entries.
The exact sheet identity gives p_W_cov=p_B*p_A, without claiming a proper-cover construction on these NONPROPER B.
All four complete matrices, every original/absolute/cover coefficient and all52 exact rank12 pencil-node controls are retained.
Their exact costs are

    B=V or -V:
      ranks/degrees(B,A,W_cov)=6,6,12,
      heights=2,2,2; whole squared-entry sums=33,33,66,
      p_B=F, p_A=-(t^6-7t^4-11t^3-7t^2+1),
      log2<m(p_A)<=log27;
    B=VR or -VR:
      ranks/degrees=6,6,12,
      heights=7,7,7; whole squared-entry sums=263,263,526,
      p_B=F,
      p_A=5t^6+28t^5+51t^4+55t^3+51t^2+28t+5,
      log5<=m(p_A)<=log223.

The leading coefficient5 is retained, not divided out.
The changed trace cubic5y^3+28y^2+36y-1 has exactly three real roots in(-4,-3),(-3,-2),(0,1), giving the full two negative exterior reciprocal pairs and one neutral pair; its measure is log5 plus both exterior logarithms.
For every displayed representative, m(p_B)=log beta4, beta4<2 and

    m(p_W_cov)=log beta4+m(p_A)>2log beta4.

For the ENTIRE integer-parameter family, with height H over ALL entries,

    H(B_(epsilon,n))<=2*24^abs(n),
    sum_(i,j) B_(epsilon,n),ij^2<=144*24^(2abs(n)).

The literal cover has the same height bound and twice this full energy bound.
Original degree6, complete Phi6 and original measure log beta4 remain at every n.
Whenever the full-entry absolute polynomial is NONZERO,

    m(p_A)<=log720+6log(4*24^abs(n)),
    m(p_W_cov)=log beta4+m(p_A).

No finite logarithmic cost is assigned to a zero absolute polynomial; nonvanishing or fixed absolute rank at untested powers is not asserted.
Congruence preserves the original pencil, not its entrywise-absolute expense.
The actual proper C458v2 k4 control remains an achieved rank6/height1/strict-upper-energy5 matrix with full Phi2^2*P4 and equal absolute companion, hence proper rank12 cover Phi2^4*P4^2 and measure2log beta4.
Neither neutral factor may be deleted, and this comparison does not assert optimality over other ranks or neutral products.
No modulus beyond4, further matrix architecture, all-rank cyclotomic-stabilization obstruction, new actual scalar realization or unrestricted Mahler-gap conclusion follows.

<a id="argument"></a>
## Complete original argument

This entire original author body retains its actual original date, finite declarations, outcomes and limits.
Only adequate same-object mathematical hrefs and relative locations are maintained; no old review or dated input is rewritten as reading a later C.

## Changed integral bilinear forms for the complete sextic target

### Scope and status

Author proof completed under [G0001](../tasks/Yin_T_G0001_v1.md#contract) and the current human-resumed execution authority.
The complete coefficient congruence in Section5 excludes the two prescribed proper rank6 polynomials independently of bilinear form; the changed signed-unit family and all costs are retained.
Separate full review and fixed adoption are still pending.
All candidate routes remain active.

<a id="selfadjoint-unit-changed-form-reuse"></a>
### 1. Reuse and a genuinely changed bilinear form

Date:2026-10-10.
[L274](Yin_C_G0496_v1.md#statement) excludes EVERY integer or two-adic positive upper-unitriangular basis of the particular exterior form V0, and of its modulo4 congruence class.
There is no reason to search another basis of that form.
[L262](Yin_C_G0456_v1.md#sextic-integral-bilinear-realization) supplies its complete construction and monodromy identities; [L270](Yin_C_G0482_v1.md#statement) distinguishes odd-prime lifting from the integer problem.
The L246 bipartite and L214 common-stabilizer obstructions retain their exact narrower scopes.
None classifies every integral form with the same scalar polynomial.
The proper [L191 comparison](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) remains available with full Phi2^2 P4 and complete cover measure2log beta4.

The new construction changes the nonsymmetric bilinear form by an integral SELF-ADJOINT UNIT in its actual monodromy algebra.
It is not presented as an unproved basis operation.
All identities below are direct consequences of the already retained integral matrices and elementary matrix multiplication; no integral-lattice classification, unit-group classification, spin-group or local-to-global theorem is used.
The existing source screen and fixed direct exterior calculation suffice at this scope.

Use the actual matrix

    V=V0=[
      [0,-1,-2,0,-1,0], [1,0,-1,1,0,1],
      [2,1,0,2,1,1], [0,-1,-1,0,-1,0],
      [1,-1,-1,1,0,1], [1,-1,-1,0,-1,0]].          (1)

It has det V=1 and complete pencil

    F(t)=Phi6(t) P4(t)
        =t^6-2t^5+t^4-t^3+t^2-2t+1,
    P4(t)=t^4-t^3-t^2-t+1.

Let C=-V^(-1)V^T.
This is an integral unimodular matrix with det(tI-C)=F.
Transposition and V^T=-VC give C^T V C=V, hence C^T V=VC^(-1).
Define

    R=C^2+C^(-2)=(C+C^(-1))^2-2I.                (2)

It follows immediately that R is integral, commutes with C and satisfies R^T V=VR.
Its determinant is1, as follows without a numerical eigenvalue calculation.
The trace polynomial of F is

    F(t)=t^3 (y-1)(y^2-y-3), y=t+t^(-1).

Thus the six eigenvalues of C+C^(-1), with multiplicity, are1,u_+,u_- each twice, where u_++u_-=1 and u_+u_-=-3.
The polynomial y^2-2 equals-1 at1 and y+1 at either u.
Since (u_++1)(u_-+1)=-1,

    det R=(-1)^2[(u_++1)(u_-+1)]^2=1.              (3)

The eigenvalue argument computes a polynomial determinant and does not require a selected real ordering or an irreducibility assumption beyond the already fixed factors.
Alternatively it is an immediate characteristic-polynomial reduction.
In particular R^(-1) is integral by the adjugate formula.

<a id="all-power-selfadjoint-form-family"></a>
### 2. An exact infinite changed-form family and four representatives

For EVERY n in Z and epsilon in{+1,-1} put

    V_(epsilon,n)=epsilon V R^n.                  (4)

This is an actual integral determinant-one rank6 form on the standard lattice.
Self-adjointness, including inverse powers, gives

    V_(epsilon,n)^T=-V_(epsilon,n) C,
    det(t V_(epsilon,n)+V_(epsilon,n)^T)=F(t).      (5)

Every member retains the complete degree-two Phi6 factor and logarithmic measure log beta4; there is no deletion or normalization of a scalar factor.
These matrices have not been claimed upper-unitriangular.
Their entrywise absolute factors and literal full-entry covers still have to be charged as full polynomials.

There is a useful exact reduction of the WHOLE integer-parameter family, rather than a search over a few powers.
For k in Z and e in{0,1}, the actual unimodular integer matrix Q=R^k satisfies

    Q^T (epsilon V R^e) Q=epsilon V R^(2k+e).      (6)

Therefore existence of a positive upper-unitriangular integer basis in the entire family reduces to the four actual representatives V,-V,VR,-VR.
The same implication holds for bases modulo4 and over Z_2.
This is not a claim that the four representatives are inequivalent or that they exhaust all forms with determinant F.
The positive-even representative V is already excluded by L274; the other three require an actual new compatibility test.

<a id="changed-selfadjoint-finite-domain"></a>
### 3. Declared complete local discriminator

Before computation, the continuing [J65](../computations/programs/Yin_J_G0065/readme.md) test is declared as follows.
Construct exactly V,-V,VR,-VR by integer arithmetic and verify (1)--(6), the full F and actual determinant.
For the THREE representatives -V,VR,-VR, perform the complete modulo2-basis and modulus4-lift classification from the written L274 cyclic-vector reduction, using each ACTUAL new Gram form.
All32768 upper-unitriangular U and all64 image vectors per cyclic U are in scope.
Every compatible binary congruence basis must be retained and its complete15 lower plus6 diagonal equations checked.
The derivative omits no diagonal and imposes no unnecessarily stronger determinant-one equation.
Retain all surviving corrections or full inconsistency witnesses.
The total runtime cap is120 seconds; a capped run is incomplete and cannot prove an all-basis obstruction.
No pivot search, higher modulus, additional parameter family or arbitrary larger coefficient box is authorized by this declaration.

The new forms have the SAME monodromy C, so its once-verified cyclic-vector reduction and necessary filters may be reused computationally, but the full congruence Q^T B Q=U and the integer error modulo4 must be checked separately for each actual B.
A candidate is not accepted merely because it intertwines C.
All four actual full-entry absolute polynomials and literal rank12 cover products will be retained, including any zero-factor or nonproper case.
This cost calculation is a finite check, not a basis search.
The prior V classification is reused as fixed evidence, not claimed independently rerun in this new program.

<a id="all-proper-target-coefficient-extension"></a>
### 4. A justified complete target-coefficient extension, declared before execution

The first declared run completed in1.031 seconds.
Each of the three new representatives has375 actual binary upper forms and5625 congruence bases, every one incompatible with its full Gram lift modulo4.
The full F persists.
The form VR has height7 and whole squared-entry sum263, and its full absolute factor is5t^6+28t^5+51t^4+55t^3+51t^2+28t+5.
These facts do not yet show whether the new representatives lie in different modulo4 congruence classes.
No such inequivalence is inferred merely from their changed entries.

A more discriminating next finite question follows from these shared failures: is the COMPLETE prescribed polynomial itself incompatible with positive upper-unitriangularity modulo4, independently of a particular realizing bilinear form?
This is a genuinely broader target than the preceding congruence tests.
Its complete finite domain has an exact linear reduction, which is now stated before any such run.

For ANY integral upper-unitriangular six-dimensional matrix U, transposing the determinant gives a monic reciprocal polynomial

    p_U(t)=t^6+a(U)t^5+b(U)t^4+c(U)t^3
                      +b(U)t^2+a(U)t+1.          (7)

Each of a,b,c is an INTEGER polynomial in the15 strict upper entries, by determinant expansion.
Let U0 be the binary representative of U.
Every lift modulo4 is uniquely U0+2X with X strictly upper and binary.
For f=(a,b,c), polynomial expansion gives the EXACT congruence

    f(U0+2X)=f(U0)+2 A_(U0) x modulo4,
    A_(U0),j=[f(U0+2E_j)-f(U0)]/2 modulo2.        (8)

All terms involving two increments vanish modulo4.
The displayed finite difference gives the derivative modulo2 even when the coefficient polynomial has repeated entry variables; replacing it by an ordinary binary bit-flip difference would not be justified.
There are no diagonal or determinant variables in this target test: U0+2X already has diagonal1 and exact integer determinant1.

First require f(U0)=(-2,1,-1) modulo2.
For such a U0 the full target modulo4 occurs exactly when

    A_(U0) x=[(-2,1,-1)-f(U0)]/2 modulo2.         (9)

This has only3 equations in15 bits.
Its complete image contains at most8 vectors, so an exact image-space list or a left-kernel/error certificate settles ALL32768 lifts of a given U0.
It is not a bounded integer coefficient search.

The additional test now declared in J65 is ALL32768 binary upper forms.
The safe necessary prefilter F(C_U)=0 modulo2 may be reused: every target has characteristic polynomial F modulo2 and therefore this annihilation.
Its390 survivors from the actual new run will have f(U0) recomputed EXACTLY over Z and checked for the full target parity; no cyclicity assumption is required to discard a form.
For EVERY target-parity survivor compute all15 increment columns in(8), retain the complete image space, actual right side and any solution or inconsistency certificate.
The new total runtime cap is120 seconds.
This extension is motivated by the common failure of the signed-unit family and the coefficient-polynomial linearization, not by a larger coordinate radius.
No extra modulus, pivot search or further matrix architecture is included.
A complete contradiction would exclude ALL proper rank6 integer realizations of this exact full target; a survivor would be only modular compatibility.
Either outcome will be retained without a further discovery extension in this round.

<a id="universal-rank-six-coefficient-congruence"></a>
### 5. Complete coefficient certificate and an all-form obstruction

**Theorem, supported by the complete exact finite certificate below.**
Let U be ANY integral upper-unitriangular matrix of size6, with complete polynomial(7).
If a is even and b,c are odd, then

    (a,b,c) modulo4 is either(2,3,3) or(0,1,3).
    In particular c=3 modulo4 and a+b=1 modulo4.  (10)

There is no bound on its entries, energy, signs, ordering or graph.
No symmetric lattice, prescribed monodromy or congruence to the exterior construction is assumed.
In consequence there is NO such U with either of the complete polynomials

    Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    S6=t^6-t^4-t^3-t^2+1.                        (11)

For the first target a+b=-1 and for the second a+b=-1 also, so both violate(10).
This resolves the exact six-dimensional realization questions for these two full polynomials, not the possibility of a larger neutral completion.
S6 is the same secondary scalar polynomial retained in L254; its previously checked root/irreducibility facts are not needed for this polynomial nonrealization conclusion.

The [target.py](../computations/programs/Yin_J_G0065/target.py) run completed in0.734000 seconds.
Of all32768 binary upper forms,390 satisfy the safe annihilator test and exactly375 have the required coefficient parity(0,1,1).
For EVERY one of those375 forms, the exact integer base triple satisfies

    f(U0)=(2,3,3) modulo4,
    image(A_(U0))={ (0,0,0),(1,1,0) } over F2.    (12)

All15 derivative columns, the base triple, complete image, target right side and inconsistency witness are retained individually in target_result.json (`mathematics/computations/outputs/Yin_J_G0065/target_result.json`).
The image equality is stronger than checking just its rank: it says that a and b can change together by2, while c cannot change modulo4.
Inserting(12) into(8) proves(10) for every integer lift.
Each binary form has32768 lifts modulo4, represented by its full linear system; all4^15=1073741824 upper-entry residue matrices are covered by the32768 binary cases and this exact expansion.
Most binary cases are rejected by their coefficient parity.
No such billion-case literal loop was claimed or needed.

The three coefficient equations for Phi6 P4 fail in all375 cases.
Their left-kernel witness is always z=(1,1,0), encoded as3 with(a,b,c) assigned bits0,1,2.
Its pairing with every derivative column is0 and its pairing with the actual error is1.
For S6 the same image equality establishes the contradiction directly; no extra S6 scan is asserted.
Unlike the earlier fixed-root and fixed-form results, (10) is a necessary condition for EVERY proper integer matrix of this size and parity type.

A readable initial example is the upper form with15-bit mask657, whose binary row integers are[35,18,12,8,16,32].
Its exact coefficients are(2,3,3), and its only nonzero derivative columns are positions(0,4),(1,5),(4,5); each column is(1,1,0).
For the prescribed F its error vector is(0,1,0).
Thus the single functional a+b immediately contradicts a lift.
The complete record verifies the same image and base residue for the other374 forms, rather than extrapolating from this example.

There is also an author self-check of the WHOLE parity classification independent of the annihilator screen and trace formulas.
[verify.py](../computations/programs/Yin_J_G0065/verify.py) expands the integer determinant by all720 permutations.
On binary strict-upper entries, each monomial reduces to its support indicator.
Summing its integer coefficient over all contained supports by the exact Boolean subset-sum recurrence gives the coefficient triple at every one of the32768 binary matrices.
Exactly the same375 masks have parity(0,1,1), with every exact base triple matching.
Formal differentiation of those determinant monomials gives all5625 derivative columns independently of the step-two evaluation in target.py; the complete image is always exactly(12).
This is an AUTHOR cross-check with a different algebraic calculation, not the separately assigned noncontributor review still required.

The self-adjoint family in Section2 is thus genuinely realized as integral bilinear matrices with full F, but NONE of its members has a positive upper-unitriangular integer basis.
The earlier three local tests already prove that within the family, while the new general theorem proves that changing to ANY other integral bilinear form with the same complete F cannot solve the rank6 target either.
It is not necessary to claim or decide whether the four family representatives are inequivalent modulo4.
All all-form conclusions rest on the proper-coefficient theorem, not on an unproved classification of bilinear forms.

<a id="selfadjoint-family-complete-expenses"></a>
### 6. Complete changed-form expenses and proper comparisons

For reproducibility the actual new matrices in(2) are

    R=[
      [2,0,-1,2,1,2], [-3,0,2,-2,0,-1],
      [2,1,0,2,2,2], [2,-1,-2,0,-2,-1],
      [-2,0,1,-1,0,0], [2,2,2,2,3,2]],
    R^(-1)=[
      [0,1,1,1,0,0], [-2,-2,1,0,2,0],
      [1,0,-2,0,0,1], [1,-2,-4,-2,-1,1],
      [0,2,2,0,-2,-1], [0,0,1,1,2,0]].            (13)

Their product in both orders is I.
The genuinely changed representative is

    VR=[
      [1,-2,-3,-1,-4,-3], [4,0,-1,2,0,1],
      [5,0,-1,3,1,3], [3,-1,-3,1,-2,-1],
      [7,0,-3,4,0,2], [5,-1,-4,3,-1,1]].         (14)

Its determinant is1 and full pencil is F, including the Phi6 factor.
These are actual integer forms, not synthetic reciprocal spectra.
The signs epsilon do not affect the absolute matrix.
For EACH form B define the full-entry A=-|B| and literal rank12 lift W by replacing an entry b<=0 with b I2 and b>0 with -b times the two-sheet swap, including diagonal and below-diagonal entries.
Symmetric/antisymmetric sheets carry A and B, so

    p_W=p_B p_A.                                 (15)

This is the same explicitly proved full-entry identity from L262; it is NOT a proper upper-unitriangular cover theorem applied to a nonproper B.
The four controls have:

| B | ranks B,A,W | heights B,A,W | whole squared-entry sums B,A,W | complete p_A |
| --- | --- | --- | --- | --- |
| V or -V | 6,6,12 | 2,2,2 | 33,33,66 | -(t^6-7t^4-11t^3-7t^2+1) |
| VR or -VR | 6,6,12 | 7,7,7 | 263,263,526 | 5t^6+28t^5+51t^4+55t^3+51t^2+28t+5 |

Every original degree is6, every absolute degree6 and every literal cover degree12.
The original polynomial is exactly F in every row, while the FULL cover is F times the displayed factor.
All matrices and all13 cover coefficients are retained in changed_result.json (`mathematics/computations/outputs/Yin_J_G0065/changed_result.json`).
In particular det A=5 in the second row; that scalar is not divided away.
None of the four B is proper upper-unitriangular, and Theorem(10) precludes such a basis altogether.
No proper target companion or favorable proper-cover measure is invented.

Write m_B=m(p_B)=log beta4.
For V and -V, L262/L274 retain the exact two exterior pairs of p_A and in particular log2<m(p_A)<=log27.
For VR and -VR,

    p_A(t)=t^3 [5y^3+28y^2+36y-1],
    log5<=m(p_A)<=log223,
    m(p_W)=log beta4+m(p_A)>2log beta4.            (16)

The lower bound already follows from the actual leading coefficient5; the upper bound is its complete coefficient-l1 sum223.
More explicitly the trace cubic has values-17,8,-1,-1,68 at-4,-3,-2,0,1.
It therefore has exactly three distinct real roots in(-4,-3),(-3,-2),(0,1).
Two yield negative expanding reciprocal pairs and the third a neutral pair.
Its full measure is log5 plus the two expanding logarithms.
This verifies the complete root-count scope without a numerical approximation.
For both rows, beta4<2, so the entire literal-cover cost exceeds the achieved proper comparison.
Neither energy nor a single exterior root replaces the complete measure.

The infinite family also has an explicit coarse coefficient-cost boundary.
Since H(V)=2 and H(R),H(R^(-1))<=4, ordinary matrix multiplication gives

    H(V_(epsilon,n))<=2*24^|n|,
    sum_(i,j) V_(epsilon,n),ij^2<=144*24^(2|n|).   (17)

The literal full-entry cover has the same height bound and twice the whole squared-entry sum.
Its original degree and logarithmic measure remain6 and log beta4, with the full Phi6 retained.
For any nonzero full-entry absolute polynomial its logarithmic measure is at most log720+6log(4*24^|n|), by the6! determinant expansion on the unit circle; the cover measure adds this to the unchanged original measure by(15).
If such an absolute polynomial were zero, no finite Mahler cost would be assigned to it.
No assertion of nonvanishing or fixed absolute rank for all untested n is needed or made; the four actual representatives above have fully checked nonzero factors and ranks.
Their integer congruence relation preserves the original pencil, not entrywise absolute cost.

The proper benchmark is still L191 at k=4: an explicit rank6 unit-diagonal integer matrix has full Phi2^2 P4 and absolute companion equal to it, strict-upper energy5, height1 and proper rank12 cover Phi2^4 P4^2 with measure2log beta4.
Both neutral multipliers have degree2, but they are different actual polynomials.
The theorem rules out replacing its Phi2^2 by Phi6 at rank6; it does not permit deletion of either factor, and does not assert minimality among all other ranks or neutral products.
Stabilizing changes the rank and falls outside(10); every added factor and the resulting proper companion must be recomputed.

<a id="all-form-coefficient-selfcheck-and-handoff"></a>
### 7. Execution, full self-check, contribution and the changed boundary

The actual programs are [J65](../computations/programs/Yin_J_G0065/readme.md).
Python3.12.14 and SymPy1.14.0 were used.
The first declared changed-form test ran in1.031000 seconds.
Its common32768-form loop has13888 nonsingular symmetric forms,390 annihilator forms and375 cyclic forms.
For each of -V,VR,-VR it retained375 actual upper forms and5625 binary congruence bases, all with inconsistent21-equation Gram systems modulo4.
Every matrix multiplication, inversion, determinant, congruence and error in that conclusion is exact.
Binary primitives are explicitly imported from the fixed J63 implementation; this is reused AUTHOR code, not an independent new classification implementation.
Each changed Gram and its entire error/certificate set are recomputed.

The justified second declaration enlarged the mathematical domain to ALL proper matrices, not the coordinate bounds.
target.py uses an exact upper-triangular inverse and integer Newton trace identities for a,b,c, checking divisibility by2 and6 before integer division.
Its step-two evaluation computes the true mod2 derivative of the INTEGER coefficient polynomial; no invalid bit-flip derivative or floating polynomial comparison is used.
It finished its complete32768-case loop and375 systems in0.734000 seconds.
No cap, partial publication or mathematical failed assertion occurred in either discovery run.
A redundant vacuous truth condition in the target witness generator was removed after that run as code cleanup; it did not affect any generated candidate, witness or output field.

The separate author verify.py then rebuilt all32768 binary triples from the determinant's720 permutations using Boolean subset sums, rebuilt all5625 derivative columns by formal differentiation, checked all16875 saved changed-form inconsistency certificates directly, and recomputed all four FULL original and absolute polynomials by ordinary polynomial convolution and determinant permutation expansion.
It checked every literal cover-entry definition, full product, height, energy and coefficient-l1 field.
This completed in0.797000 seconds, with all assertions passing.
The original changed.py additionally checked the actual rank12 pencil at13 distinct integer nodes per representative,52 total; degree at most12 makes those exact checks a complete polynomial test, alongside the analytic sheet proof.
The author check is not relabelled independent review.

The mathematical self-check covered: integrality of positive and negative unit powers; the V-adjoint orientation; determinant and complete F under the changed form; all-n reduction to four representatives without inequivalence assumptions; necessity rather than sufficiency of the cyclic prefilter; integer coefficient-polynomial Taylor expansion at step2; all three reciprocal coefficients and the absence of a hidden endpoint-only match; complete binary coverage including the15 noncyclic annihilator controls; all derivative images and both target contradictions; every scalar/neutral/absolute factor; whole-entry versus strict-upper energy; and the difference between a nonproper literal lift and an actual proper cover.

The coordinating AI supplied only the broad changed-form question, responsible homes, authorization and reviewer arrangement.
The self-adjoint-unit construction, all-power reduction, justified full coefficient extension, exact programs and theorem(10) were derived by orbit_research AI for Yin.
Earlier fixed inputs and their actual attribution/review scopes remain unchanged.
No new source theorem, acquisition, assertion about a full unit group, or literature-priority claim is made.
The full coefficient congruence is certified at its displayed finite residue domain and then extended to unbounded integers by the exact polynomial identity; it is not extrapolated from sampled heights or a numerical pattern.

The next realization must change the COMPLETE scalar target by a genuinely charged neutral product/rank, or select a different scalar input outside the exact obstruction.
For the two polynomials(11), merely changing the six-dimensional bilinear form, lattice or ordering can no longer help.
This is an advance beyond L274's single-form class, while its rank/parity boundary is essential.
It supplies neither a universal cyclotomic-stabilization obstruction nor a lower bound for unrestricted Mahler measure.
All candidate routes and the unrestricted Task remain active.
This bounded round stops here; complete separate noncontributor review is required before fixed adoption.

Final author freeze:2026-10-10T03:48.
All Sections1--7 and equations(1)--(17), together with the seven native J65 files listed in its readme, are held for the separately assigned complete review.
The two residues in(10) are stated as a necessary condition, not a prescribed-polynomial sufficiency theorem.
No further discovery is included after this freeze.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T03:14 |
| status | open |
| reason | Register the complete original all-proper coefficient theorem, infinite signed-unit family and all native/cost/source/contribution/negative scope. The actual written Statement and complete Argument must be read and whole-checked before a new formal finding and separate adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete universal coefficient and signed-unit result](#statement) | Every unrestricted integral proper rank6 matrix at the exact parity, complete integer-polynomial extension/two full targets, all integer signed-unit powers/four representatives/complete native failures/all absolute and literal costs/negative boundaries. |
| argument | [Entire original author proof](#argument) | Complete original scope/reuse/Sections1--7/equations1--17/actual matrices/all-power family/declared finite domains/full coefficient theorem/native proof/complete root and scalar expenses/proper comparison/source-contribution-self-check and preserved failures/limits. |
| dependency | [Actual exterior realization and full-entry sheet proof](Yin_C_G0456_v1.md#sextic-integral-bilinear-realization) | Complete fixed actual V0/monodromy/F and full-entry two-sheet product at its nonproper domain; not a proper upper-unitriangular-cover theorem outside its hypotheses. |
| dependency | [Fixed-form complete basis obstruction](Yin_C_G0496_v1.md#statement) | Entire actual V0 modulo4 all-basis classification including cyclic completeness, all21 Gram equations and original/full absolute costs; exact unchanged positive-even representative, not the new all-form coefficient conclusion. |
| support | [Odd-prime versus integral gate](Yin_C_G0482_v1.md#statement) | Complete conditional odd-prime coherent lifting and exact integer-representative costs as comparison; no local-to-global integer realization premise. |
| support | [Full quartic constructive Gram family](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Complete actual P4 family and proper integral Gram mechanism, without scalar neutral-factor deletion. |
| support | [Explicit achieved k4 full costs](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Actual k4 rank6/height1/energy5/full Phi2^2 P4 and rank12 Phi2^4 P4^2 measure2log beta4; achieved comparison, no global minimality claim. |
| dependency | [J65 actual finite protocol and evidence](../computations/programs/Yin_J_G0065/readme.md) | Entire original declared two120-second author domains, all seven author-native files plus separately written checker/output, old runtimes and cleanup boundary; current static reading is not a new native execution. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | All three375-form/5625-basis actual Gram/error/witness sets, every C/R/inverse/matrix and four full degree6/6/12 cost payloads, including old-V-classification-not-rerun. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/changed_result.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | All375 parity bases/5625 actual derivative columns/integer triples/full image spaces/errors/witnesses and exact finite domain, with no larger integer-height test. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/target_result.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | Actual unfiltered32768 Boolean coefficient reconstruction/formal derivatives/all16875 Gram witnesses/full costs; original AUTHOR check, not new independent execution. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/verification.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | Actual unfiltered subset determinant/cofactor columns/all three complete basis SETs/full Gram kernels/errors and all full costs/52nodes at the original fixed scope; no present-day rerun or expanded conclusion. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/review_result.json`; this target locates its run account. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T03:24 |
| status | proved |
| reason | Adopt the complete universal proper-sextic theorem and signed-unit/full-cost proof after actual entire Statement/Argument/native-code-and-record inspection under its explicit whole SELF finding. Adequate original exact finite evidence and R178 independent inspection are reused at their actual original scope; no new native execution or isolated current review is invented. All rank/parity/zero-factor/neutral-cost/source and Task/E limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete universal coefficient and signed-unit result](#statement) | Every unrestricted integral proper rank6 matrix at the exact parity, complete integer-polynomial extension/two full targets, all integer signed-unit powers/four representatives/complete native failures/all absolute and literal costs/negative boundaries. |
| argument | [Entire original author proof](#argument) | Complete original scope/reuse/Sections1--7/equations1--17/actual matrices/all-power family/declared finite domains/full coefficient theorem/native proof/complete root and scalar expenses/proper comparison/source-contribution-self-check and preserved failures/limits. |
| dependency | [Actual exterior realization and full-entry sheet proof](Yin_C_G0456_v1.md#sextic-integral-bilinear-realization) | Complete fixed actual V0/monodromy/F and full-entry two-sheet product at its nonproper domain; not a proper upper-unitriangular-cover theorem outside its hypotheses. |
| dependency | [Fixed-form complete basis obstruction](Yin_C_G0496_v1.md#statement) | Entire actual V0 modulo4 all-basis classification including cyclic completeness, all21 Gram equations and original/full absolute costs; exact unchanged positive-even representative, not the new all-form coefficient conclusion. |
| support | [Odd-prime versus integral gate](Yin_C_G0482_v1.md#statement) | Complete conditional odd-prime coherent lifting and exact integer-representative costs as comparison; no local-to-global integer realization premise. |
| support | [Full quartic constructive Gram family](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Complete actual P4 family and proper integral Gram mechanism, without scalar neutral-factor deletion. |
| support | [Explicit achieved k4 full costs](Yin_C_G0458_v2.md#quartic-six-to-twelve-cover-costs) | Actual k4 rank6/height1/energy5/full Phi2^2 P4 and rank12 Phi2^4 P4^2 measure2log beta4; achieved comparison, no global minimality claim. |
| dependency | [J65 actual finite protocol and evidence](../computations/programs/Yin_J_G0065/readme.md) | Entire original declared two120-second author domains, all seven author-native files plus separately written checker/output, old runtimes and cleanup boundary; current static reading is not a new native execution. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | All three375-form/5625-basis actual Gram/error/witness sets, every C/R/inverse/matrix and four full degree6/6/12 cost payloads, including old-V-classification-not-rerun. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/changed_result.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | All375 parity bases/5625 actual derivative columns/integer triples/full image spaces/errors/witnesses and exact finite domain, with no larger integer-height test. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/target_result.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | Actual unfiltered32768 Boolean coefficient reconstruction/formal derivatives/all16875 Gram witnesses/full costs; original AUTHOR check, not new independent execution. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/verification.json`; this target locates its run account. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0065/readme.md#recorded-runs) | Actual unfiltered subset determinant/cofactor columns/all three complete basis SETs/full Gram kernels/errors and all full costs/52nodes at the original fixed scope; no present-day rerun or expanded conclusion. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0065/review_result.json`; this target locates its run account. |
| review | [Entire current SELF finding](../audits/reviews/Yin_R_G0719_v1.md#current-universal-sextic-whole-self-finding) | ENTIRE actual Statement and original seven-section/17-equation proof, all integer signed-unit powers/four representatives/complete three Gram and universal coefficient domains/full native evidence/every original-absolute-literal scalar-root-rank-cost/contribution/negative boundary. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0065](../computations/programs/Yin_J_G0065/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
