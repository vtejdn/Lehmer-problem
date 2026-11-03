---
author: Yin
---

# Complete mod2 obstruction between equal-scalar positive integral forms

## Current complete proof home

The full mathematical statement and argument now belong to [the current Claim](../claims/Yin_C_G0295_v1.md#binary-congruence-fixed-scope).
The original complete mathematical body and meaningful failed-method/source/cost history remain below as the actual input to the original whole finding.
Dated active/pending/freeze and adoption statements describe the original2026-10-10 round; current Task/execution authority remains with its responsible selected materials, and this maintenance resumes no research.


Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="binary-congruence-fixed-scope"></a>
## Current adopted scope

For every k>=3, the two exact L330 integral forms have mod2 symmetrization ranks3k-epsilon_k and k+4-epsilon_k, with positive difference2k-4.
Explicit parameterizations exhaust both kernels at every k.
Consequently they are not integrally congruent, even after both receive the same arbitrary finite integral direct-sum block.
All four finite controls and eight full native rank/kernel/operation certificates are independently verified.
The unchanged full scalar, original measure, rank, energy and cover costs remain those of L330.
This excludes transferring that particular cheaper form by an integral basis change; it leaves open other cheaper forms within the expensive class and does not make the binary invariant a complete classification.

The complete D201 author proof and review follow without abridgment.
Historical pending-review, pending-adoption and stopped-execution handoff sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.
G0001 remains active and unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## A binary congruence obstruction for equal-scalar positive sparse forms

Date: 2026-10-10.
All eight routes remain active; the unrestricted Task is unresolved.

### Assigned question

Root authors this new structural round after the whole L330/J82 review.
Determine whether the displayed expensive and cheaper integral forms V_k,Z_k actually can be congruent.
Start with elementary mod2 symmetrization rank, using the full literal forms and all k>=3; preserve the distinction between excluding this cheaper target and excluding every cheaper representative in V_k's class.
The complete scalar/rank/energy match and all original positive-measure costs remain L330.
Develop any all-k kernel/rank calculation here before finite controls.
A new coherent J82 continuation may verify exactly k3,4,5,6, full symmetrized matrices/rank certificates, aggregate60second author cap, preserving earlier native artifacts.
No broad search, changed seed or automatic k extension.
Full author freeze and a separate noncontributor review are required.

Develop substantive work here; first inspect exact retained inputs and applicable reuse rules.
Reusable programs and outputs belong in a coordinated J with a declared finite domain before running.
Preserve unsuccessful implications, uncertainty, full original costs and source boundaries.
Freeze the complete author argument before whole separately organized noncontributor review.
Allocation asserts no result.


<a id="binary-congruence-reuse"></a>
### 1. Responsible inputs and the exact new question

The entire [L330 proof and independent review](Yin_L_G0330_v1.md#complete-retained-proof-and-review) and the complete [J82 literal controls](../computations/programs/Yin_J_G0082/readme.md#complete-positive-scalar-independent-review) were read before this new derivation.
Root was L330's reviewer, not its author, and now authors THIS different congruence question; those roles are distinct.
D9's existing actual congruence/mutation interface was also checked.
L330 deliberately proves equality of complete scalar polynomials, ranks and energies without inferring integer congruence.
Its actual matrices V_k and Z_k, k>=3, are the inputs here.

For clarity, V_k has k consecutive signed diamonds on a_0,...,a_k, with middle vertices b_i,c_i, and an edge a_0-a_k.
The signs are the exact L330 ones.
There is an additional independent path a_0,z_1,...,z_k,a_k.
It has n=4k+1 vertices, height1 and energy5k+2.
Z_k is the negative forked cycle on u,z_1,...,z_k,v, with edge u-v and two separate leaves at each endpoint, followed by k-1 blocks K2=[[1,-2],[0,1]] and k-3 singleton identity blocks.
It has the same n and energy, height2 and the same complete scalar polynomial.
The actual standard vertex orders, every neutral factor and all full measure costs remain those in L330.

The intended cheaper-target question is whether there exists any integer unimodular Q with Q^T V_k Q=Z_k.
A scalar identity alone cannot answer it.
A basic binary invariant does, as follows.
For an integral matrix B let

    S_2(B)=(B+B^T) mod2, and r_2(B)=rank over F_2 of S_2(B).   (1)

If C=Q^T B Q with det Q=+/-1, reduction mod2 gives S_2(C)=bar Q^T S_2(B)bar Q, with bar Q invertible.
Thus r_2(C)=r_2(B).
This elementary change-of-basis/rank identity is proved directly and needs no classification theorem or source premise.
In characteristic two all L330 signs disappear and the diagonal2 vanishes; S_2(V_k) is exactly the unweighted support adjacency matrix.
The weight-two K2 edges vanish as well in S_2(Z_k).

We calculate these ranks for EVERY k>=3, rather than infer them from finite examples.

<a id="binary-diamond-nullspace"></a>
### 2. Complete kernel of the expensive form over F_2

Use a vector of vertex values A_i,B_i,C_i,Z_j in F_2.
The b_i and c_i adjacency equations are both

    A_i+A_(i+1)=0, 0<=i<k.

Hence all A_i equal a common A.
Put U_i=B_i+C_i.
Each interior a_i equation is U_(i-1)+U_i=0, so all U_i equal U.
Thus the k independent choices B_i determine C_i=U+B_i.
The two endpoint equations and all path-interior equations are

    U+A+Z_1=0, U+A+Z_k=0,
    Z_(j-1)+Z_(j+1)=0, 1<=j<=k,
    Z_0=Z_(k+1)=A.                                      (2)

These are the full equations: each b/c row, each a row and each z row is accounted for.
Starting with Z_1=T, the path recurrence forces every even-indexed Z_j=A and every odd-indexed Z_j=T.

If k is odd, its endpoint index k+1 is even and the prescribed final value A is automatic.
Also Z_k=T, so both endpoint equations say U=A+T.
The free coordinates are

    A,T,B_0,...,B_(k-1),             k+2 free bits.       (3a)

If k is even, its endpoint index k+1 is odd and therefore T=A.
Now both endpoint equations force U=0.
The free coordinates are

    A,B_0,...,B_(k-1),               k+1 free bits.       (3b)

Every assignment of these free bits satisfies all the equations after the indicated substitutions, and the original vector uniquely recovers them from its displayed coordinates.
These are linear bijections with the whole kernel, not merely lists of selected null vectors.
In particular, with epsilon_k=1 for odd k and0 for even k,

    nullity S_2(V_k)=k+1+epsilon_k,
    r_2(V_k)=3k-epsilon_k.                              (4)

The even rank in(4), as expected for a symmetric zero-diagonal form in characteristic two, is a consistency check and not the proof.

<a id="binary-cheaper-nullspace"></a>
### 3. Complete kernel of the cheaper form over F_2

Consider first the forked-cycle block Y_k of dimension k+6.
Let its endpoint values be U,V, its path values Z_j, and its two leaf values at each end L_1,L_2 and R_1,R_2.
Each leaf row forces its endpoint value zero, so U=V=0.
The path equations force even-indexed Z_j=0 and odd-indexed Z_j=T, with Z_0=Z_(k+1)=0.

If k is odd, the final boundary is automatic and T is free.
The two endpoint equations become

    L_1+L_2=T, R_1+R_2=T.

Thus T,L_1,R_1 are three independent free bits and determine the entire kernel.
If k is even, the final boundary forces T=0; both leaf pairs have equal values, and L_1,R_1 are the two free bits.
Once again the assignments are bijective with the entire kernel, including both endpoint and every leaf/path equation.
Therefore

    nullity S_2(Y_k)=2+epsilon_k,
    rank S_2(Y_k)=k+4-epsilon_k.                         (5)

Every K2 block has symmetrization [[2,-2],[-2,2]], zero mod2.
Every singleton identity also has zero symmetrization mod2.
They contribute 2(k-1)+(k-3)=3k-5 free kernel dimensions and no rank.
For the whole Z_k we obtain

    nullity S_2(Z_k)=3k-3+epsilon_k,
    r_2(Z_k)=k+4-epsilon_k.                              (6)

The k=3 boundary has no singleton blocks; formula(6) includes it exactly.
In particular the rank difference is independent of parity:

    r_2(V_k)-r_2(Z_k)=2k-4>0 for EVERY k>=3.             (7)

<a id="binary-noncongruence-consequence"></a>
### 4. A definite obstruction, including common stabilization

Equations(1) and(7) prove:

**Theorem.** The actual proper integral forms V_k and Z_k of L330 are not integrally congruent for any k>=3, despite their identical complete scalar polynomial, dimension and strict squared energy.
More strongly, for every finite integral square matrix B of ANY rank, V_k direct-sum B and Z_k direct-sum B are not integrally congruent.

For the strengthened statement, binary symmetrization is block diagonal on a direct sum and ranks add.
Adding the same r_2(B) to both sides leaves the difference2k-4 unchanged.
The conclusion also holds for any realignment of the summand vertices because permutations are integral unimodular changes of basis.
No definiteness, symmetry, unimodularity or properness assumption on the common B is needed.
This is a common-stabilization obstruction, not a theorem about two different arbitrarily selected added forms.

L330's complete original polynomial remains

    p_V=p_Z=(t+1)^(k-1)(t-1)^(2k-2)F_k,
    log4<m(p_V)=m(p_Z)<log5.

Its entire expensive companion measure grows linearly, whereas the whole Z-cover measure is less than2log5.
The present theorem shows that this particular saving cannot be transferred to V_k by an integral basis change, even after the same arbitrary stabilization.
It does NOT prove that every other representative of V_k's class has high companion cost.
There might exist a different cheaper proper representative preserving r_2(V_k), and nothing here bounds that optimization.
The argument likewise does not assert that the binary rank is a complete classification invariant: equal r_2 would merely pass this necessary screen.

The changed useful test for future mutation/congruence searches is now explicit: any candidate congruent to V_k must retain r_2=3k-epsilon_k, in addition to its complete polynomial and all original costs.
Passing the scalar, rank and energy tests while changing this rank certifies a different integral form.
No near-one input or unrestricted realization is supplied.

<a id="binary-invariant-finite-declaration"></a>
### 5. Bounded exact controls, declared before execution

The infinite proof is the explicit complete-kernel parameterization above.
A new coherent J82 continuation is declared for precisely the already fixed k=3,4,5,6 and the two ORIGINAL V,Z presentations only.
It introduces congruence information, without rerunning any earlier determinant or changing those native files.
Aggregate author60second cap, standard-library binary arithmetic, no search or k extension.
New filenames: binary-invariants.py and binary-invariants.json.
The first output is preserved, complete versus incomplete status explicit.

For each input retain the entire original integer matrix, its complete mod2 symmetrization, all row operations and their full accumulated invertible row matrix, entire binary reduced row-echelon form, pivot columns, the whole nullspace basis from free coordinates, and an independently constructed whole basis from(3)/(5) with each identity checked.
Retain both ranks, nullities and the exact difference2k-4.
Elementary row operations are either a row swap or adding a DIFFERENT row, hence invertible; the accumulated identity ES=R and the complete RREF certify the rank without a numerical threshold or Smith-form oracle.
The theorem-basis vectors are checked to satisfy every equation and to be independent at the predicted dimension.

The original V/Z matrices are the completely independently verified J82 inputs.
Reconstruct their exact stated graph before comparing those copies, so a saved input is not its own oracle.
All original scalar and measure facts are reused at the fixed L330 scope; this continuation adds no finite irreducibility or approximate root claim.
Separate whole noncontributor proof review and a different-method verification of every new native field remain required.
Current status of this declaration: NOT YET RUN.


<a id="binary-invariant-author-outcome"></a>
### 6. Complete first finite outcome and whole author self-check

The first and sole declared binary execution began2026-10-10T11:56 and completed 2026-10-10T11:56, with recorded0.048641900008078665seconds against its60second cap, Python3.12.14 and exact standard-library arithmetic.
All four inputs and both original matrices per input completed.
There was no failed or partial mathematical execution, no additional k, no changed precision and no repeated historical determinant computation.

| k | Actual dimension | r_2(V_k) | r_2(Z_k) | Full rank difference |
| --- | --- | --- | --- | --- |
| 3 | 13 | 8 | 6 | 2 |
| 4 | 17 | 12 | 8 | 4 |
| 5 | 21 | 14 | 8 | 6 |
| 6 | 25 | 18 | 10 | 8 |

The complete binary-invariants.json (`mathematics/computations/outputs/Yin_J_G0082/binary-invariants.json`) retains every original and binary matrix entry, row operation, row-transform entry, RREF, pivot, free-variable kernel vector, formula-derived kernel vector and scalar/status field.
[binary-invariants.py](../computations/programs/Yin_J_G0082/binary-invariants.py) explicitly reuses only the previously inspected graph constructor in J82's root-authored review_independent.py; it imports no historical author runner and performs no determinant computation on import.
It rebuilds the whole graph and matches the existing independently checked input before its new binary work.
The old four observed program/result files remained unchanged.
These observations are contemporaneous accident checks, not historical content gates or extra mathematical evidence.

The row-operation sequence uses only swaps or addition of a different row over F_2, so each operation is invertible.
Accumulating the same operations on the identity gives E and verifies ES=R.
The exact RREF has one pivot in each nonzero row and zero entries elsewhere in each pivot column; its full nullspace basis follows by choosing every free variable once.
The independently formula-generated vectors from Sections2--3 are all annihilated and have the predicted full dimension.
These finite checks supplement the complete all-k parameterization; they do not prove its untested cases by extrapolation.
No Smith normal form, floating rank threshold or finite-field library assertion is used.

Root's whole author self-check covered every V row type, path parity and end condition, free-bit bijectivity, every Y leaf and endpoint equation, the empty singleton block at k3, all vanished weight2 and diagonal entries mod2, preservation of binary rank under an arbitrary integral unimodular congruence, and additivity under a common integral stabilization.
It checked both full dimension formulas and the positive rank difference for every allowed k, along with the finite program's complete output and status bounds.
The literal original scalar, neutral factors and measure costs are unchanged accepted L330 facts, not recomputed conjectures.

The only proposed new mathematical conclusion is noncongruence of THESE particular full forms, even after a common stabilization.
It does not settle optimized companion cost within V_k's class or exclude a different cheaper representative with the same binary rank.
Its author has no separate independent-review role on this new derivation.
Whole noncontributor proof review and different-method verification of all new native fields remain pending at author freeze.
All eight candidate routes and G0001 remain active and unresolved.


ENTIRE AUTHOR FREEZE: 2026-10-10T11:57.
Complete Sections1--6/(1)--(7), the all-k kernel proof, common stabilization and exact finite native scope are frozen for separately organized whole noncontributor review.
No independent pass is asserted.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0159_v1.md#section22--4-complete-expensive-form-kernel), with its original inspected scope and relationship.
