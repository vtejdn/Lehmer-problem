---
author: Yin
---
# Complete rank-nine bipartite test for the doubled companion cost

Date: 2026-10-18T14:24.
Human author Yin.
Root develops this changed S3/S6 constructor under Yin's all-strategies-active instruction.
The complete mathematical gate received a separate read-only noncontributor precheck before execution; no native computation has yet occurred.

<a id="rank-nine-complete-question"></a>
## Actual question and retained inputs

The complete [L283 classification](../../../ledger/Yin_L_G0283_v1.md#minimum-bipartite-padding-cost) proves that the least rectangular bipartite rank for Phi2^k F is8, and every rank8 companion is more expensive than the original.
Its three-column analysis covers all row counts and gives a doubled-measure rank10 control, but explicitly leaves rank9's(5,4) partition untested.
The exact [J67 certificate](../Yin_J_G0067/readme.md) exhausts4-by4 only; no result from it is silently extended to5-by4.
The [L230 full companion trace account](../../../ledger/Yin_L_G0230_v1.md#trace-energy-companion-cost-bound) distinguishes general upper-unitriangular matrices: cycle terms prevent treating their trace as rank minus squared-entry energy.
Thus this finite reduction concerns the BIPARTITE block class only and does not solve the non-bipartite rank7 question.

Put

    P4=t^4-t^3-t^2-t+1,
    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    q(s)=s^2-5s+3,
    chi(s)=s(s-3)q(s)=s^4-8s^3+18s^2-9s.

For every integer5-by4 matrix B, use the actual proper rank9 matrix

    V_B=[[I5,-B],[0,I4]],
    p_B(t)=(t+1)det((t+1)^2 I4-t B^tB).

The full target is p_B=Phi2^3 F, equivalent to char(B^tB)=chi.
Its absolute companion uses abs(B) entrywise, and the literal proper rank18 signed cover has the FULL product p_B p_abs.
The block and cover identities are the accepted L283/L191/C2 interfaces, with every neutral factor retained.
Let beta4>1 be the exterior Salem root of P4.
The exact question is whether ANY such B has m(p_abs)=log beta4, so the full cover attains2log beta4.

<a id="rank-nine-finite-gate"></a>
## Complete finite domain

The trace coefficient of chi forces sum_(i,j)B_ij^2=8.
Conversely an energy-eight matrix is a target only after its ENTIRE Gram characteristic polynomial equals chi.
All square partitions are eight entries of absolute value1, one entry of absolute value2 and four entries of absolute value1, or two entries of absolute value2.
There are no entries of larger absolute value and no omitted nonzero entry.
The20 positions therefore give all binomial(20,8) eight-unit supports,20 binomial(19,4) one-double weighted supports, and binomial(20,2) two-double supports.
The last class has rank at most2 and cannot have the target rank3, independently of its signs.
These symbolic counts define completeness; no coefficient box or random sample is used.

Independent row and column signs preserve the full signed characteristic polynomial by diagonal orthogonal conjugacy and leave abs(B) unchanged.
On the bipartite graph of a support, choose a deterministic spanning forest and propagate vertex signs to make every forest edge positive.
Every remaining edge sign is free; enumerating all of them covers every sign class, including disconnected supports and isolated vertices.
No row or column permutation quotient is required.
The old J67 proof applies unchanged to the nine-vertex graph after the actual dimensions are updated; its old finite counts and outcomes do not apply.

<a id="rank-nine-companion-equality-gate"></a>
## Exact comparison of the whole companion cost

Let G=B^tB and H=abs(B)^t abs(B), assuming char(G)=chi.
Both are real positive semidefinite, tr G=tr H=8, and abs(G_ij)<=H_ij for every entry.
For every real unit vector x,

    x^tGx<=abs(x)^t H abs(x)<=lambda_max(H),

so lambda_max(H)>=lambda_max(G)=lambda_plus=(5+sqrt13)/2>4.
Since H is positive semidefinite and has trace8, at most one of its eigenvalues can exceed4.
The complete block polynomial associated with an eigenvalue mu has factor t^2+(2-mu)t+1.
For0<=mu<=4 this contributes zero Mahler measure, whereas for mu>4 its entire logarithmic contribution is arcosh((mu-2)/2), strictly increasing in mu.
The extra Phi2 factor is neutral.
Consequently

    m(p_abs)>=log beta4,
    equality iff lambda_max(H)=lambda_plus.         (1)

This comparison retains all eigenvalues and factors and needs no sampled root test.

If equality holds, the integer characteristic polynomial of H contains the irreducible q(s), since sqrt13 is irrational.
Write char(H)=q(s)(s^2-3s+b), with b an integer.
The other two eigenvalues are nonnegative, so b>=0.
On the other hand

    e2(H)=sum_(i<j)(H_ii H_jj-H_ij^2)
          <=sum_(i<j)(G_ii G_jj-G_ij^2)=18,

because H_ii=G_ii and abs(G_ij)<=H_ij.
Expansion of the factored polynomial gives e2(H)=18+b, forcing b=0.
Thus equality in(1) implies char(H)=chi.
The converse follows immediately from the complete same eigenvalues.
We therefore have the EXACT finite cost criterion

    m(p_abs)=log beta4 iff char(abs(B)^t abs(B))=chi;
    otherwise m(p_abs)>log beta4.                  (2)

In the equality case the entire original and companion polynomials coincide, not just their measures.
This criterion is not asserted for arbitrary non-bipartite realizations or for other Gram targets.

<a id="rank-nine-native-proposal"></a>
## Bounded complete computation to retain in a new J

Use a new native J for this5-by4 problem, preserving J67 unchanged.
Enumerate exactly the two nontrivial square partitions above, deterministic forest signs for the author implementation and a genuinely separate sign reduction for the verifier.
Check full Gram polynomials by exact integer arithmetic; retain all stage counts, every target B, its complete original/absolute/cover coefficient arrays and the distribution of absolute Gram polynomials.
Determine equality using(2), not a floating-root ranking or energy proxy.
For each distinct absolute polynomial retain one explicit B and actual V, companion and literal signed cover, with an independent full-pencil check.
No parameter or rank enlargement belongs to this first test.

The author and independent complete batches each have an aggregate300-second cap, fixed before execution.
Timeout preserves partial status and gives no complete-class conclusion; it does not authorize silently raising the cap.
The author can reuse J67's elementary algorithms with the actual5-by4 dimensions, while the independent checker must separately reconstruct the full domain and coefficients.
All output identities and the final mathematical conclusion require a separate complete review, not only equal program totals.
This complete protocol is retained in the actual J104 native home before either declared computation is executed.

If equality occurs, L283's all-rank-below9 results make rank9 the minimum bipartite rank achieving the doubled full cost for Phi2^k F.
If equality does not occur, the other rank9 partition(6,3) already has a more expensive companion by L283, and its known rank10 control makes10 the minimum for that doubled-cost objective.
Either conclusion must wait for the completed exact certificate and independent review.
The smaller-target L191 rank6 Phi2^2 P4 comparison remains different; no near-one family or unrestricted gap follows from either finite outcome.
