---
author: Yin
---

# Complete even-complement criterion for one-negative-line binary realization

The complete current one-negative-line object is [C598 statement](../claims/Yin_C_G0598_v1.md#statement) with [all three entire arguments](../claims/Yin_C_G0598_v1.md#argument), adopted after [actual whole current SELF](../audits/reviews/Yin_R_G0766_v1.md#whole-negative-line-binary-self).
[R789](../audits/reviews/Yin_R_G0789_v1.md#even-binary-complete-independent-review) retains every original whole finding/author SELF and actual frozen input, date, correction and individual arrangement disclosure.
Current G0001 execution remains paused and unresolved; dated pending language below remains original history.

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="even-binary-realization-fixed-scope"></a>
## Original adopted mathematical scope

For every nonsymmetric integral binary form B with determinant minus one, adding exactly one orthogonal negative unit line admits a positive upper-unitriangular integer basis if and only if B is even and its alternating content is4.
A self-contained discriminant5 decreasing-leading-coefficient reduction and explicit orientation correction identify the unique relevant binary congruence class and produce the proper V(4,4,4) realization.
All full scalar, neutral and companion costs remain those of the actual fixed target; a coordinate reduction does not bound the change-of-basis height or remove the large positive Mahler cost.
The complete author proof and whole noncontributor review follow, with the bounded Dum21 method attribution and its printed source limitations.
No unrestricted gap, arbitrary higher-rank sufficiency or near-one realization is asserted.


<a id="complete-retained-proof-and-review"></a>
## Complete retained original author proof

## Even binary complements and exact one-negative-line realization

Date: 2026-10-10.

### Assigned question

Determine whether L314's evenness plus alternating content4 is also sufficient for a nonsymmetric determinant-minus-one binary form to acquire a proper integral rank-three basis after one negative unit.
Seek an all-integer construction or a genuine residual obstruction, retaining full scalar, companion and basis costs.
Use elementary self-contained reduction if possible; do not import an unaudited class-number assertion or substitute finite scans.
The unrestricted contract and small-measure boundary remain unchanged.

<a id="even-binary-complete-reuse"></a>
### 1. Exact inputs and the changed question

The actual premises are [L312's integral negative-line split and necessary content](Yin_L_G0312_v1.md#negative-line-orthogonal-split), its [displayed successful even complement](Yin_L_G0312_v1.md#even-indefinite-negative-line-rescue), its [whole proper scalar and companion optimum](Yin_L_G0312_v1.md#negative-line-complete-companion-optimum), and [L314's all-basis even-complement necessity](Yin_L_G0314_v1.md#negative-kernel-characteristic-parity).
Their complete relevant statements and proofs were read.
They concern actual integral bilinear forms, not just a scalar polynomial.
In the nonsymmetric binary determinant-minus-one domain, they establish necessity of evenness and alternating content4 but leave sufficiency open.
The [L314 full-entry lift](Yin_L_G0314_v1.md#odd-binary-relaxed-complete-cost) supplies the already checked distinction between that relaxed operation and the proper signed cover.

The needed new step is an integral congruence classification of the EVEN binary forms with determinant minus one and alternating content4.
Root's bounded registry/audit screen and the author's local search for discriminant5, indefinite binary forms and Gauss reduction did not find an exact retained source result; this is a bounded search finding, not an absence or novelty claim.
The descent below is recognized as elementary binary quadratic form reduction.
A bounded primary-source attribution check has been coordinated with root; its status is recorded in Section6.
No class-number table, indefinite-form classification theorem or external existence assertion is a proof premise.
The new proof is self-contained.
Root assigned the broad question and source/review coordination, without supplying a derivation; structural_research was separately assigned to review only the frozen whole text and has supplied no proof suggestion.
All new derivations here are by joint_boundary_research for Yin.

<a id="discriminant-five-elementary-descent"></a>
### 2. A complete integer descent at discriminant five

For an integral binary quadratic polynomial

    f(x,y)=a x^2+b xy+c y^2,  b^2-4ac=5,             (1)

a change of variables is an actual matrix in SL_2(Z), acting by substitution on the column (x,y).
No definiteness or sign restriction on a is imposed.
Neither a nor c can vanish, since that would give the impossible integer equation b^2=5.
Also b is odd, because b^2=5 modulo4.

**Lemma 1.** Every f in(1) is equivalent under SL_2(Z) to

    f_*(x,y)=x^2+xy-y^2.                            (2)

*Proof.* For h in Z let S_h=[[1,h],[0,1]].
Substituting (x+h y,y) replaces the coefficients by

    (a,b,c) -> (a,b+2ah,ah^2+bh+c).                (3)

Choose h so that the new middle coefficient b' satisfies |b'|<=|a|.
This is possible by taking a nearest representative modulo2a, for either sign of a.
Discriminant is preserved, so the new final coefficient is c'=(b'^2-5)/(4a), a nonzero integer.
If |a|>=2, then

    |c'| <= max{5,a^2-5}/(4|a|) < |a|.             (4)

Indeed 0<=b'^2<=a^2, and both 5 and a^2-5 are strictly smaller than4a^2 when |a|>=2.
The rotation R=[[0,-1],[1,0]], also of determinant1, changes (a,b',c') to(c',-b',a).
Thus a shear followed by this rotation strictly decreases the positive integer |a| whenever it is at least2.
Repeating must terminate at |a|=1.
This is an unbounded integer descent, with no finite scan or class-number assumption.

At termination apply a shear again to have |b|<=1.
Since b is odd, b=+/-1, and c=-1/a=-a.
If a=-1, apply R once to obtain a=1,c=-1, with b still +/-1.
If the resulting b=-1, apply S_1; its new middle coefficient is1 and its last coefficient remains-1.
The result is exactly(2).
All operations were in SL_2(Z), and their finite product gives the required integer matrix.
This also gives a terminating algorithm specified by elementary formulas, although no program implementing it was run here.

The orientation restriction matters: the proof uses determinant1 throughout, so it controls the alternating part of the underlying nonsymmetric bilinear form.
It is stronger than an unoriented quadratic-value identification alone.
No assertion about all positive discriminants or arbitrary class numbers follows from the special inequality(4).

<a id="even-binary-complete-classification"></a>
### 3. Necessary and sufficient conditions on the actual binary form

For an integer matrix A write p_A(t)=det(tA+A^T).
A proper matrix means an upper-triangular integer matrix with every diagonal entry1.
Let B=[[r,s],[t,u]] be an integral binary matrix with det B=-1 and s!=t, and put G=[-1] direct-sum B.
Say B is even when w^T Bw is even for every w in Z^2; explicitly this means r,u,s+t are even.

**Theorem 2.** The following are equivalent:

1. G admits a proper integral rank-three basis, that is, some H in GL_3(Z) makes H^T G H proper.
2. B is even and |s-t|=4.
3. B is integrally congruent to B_0=[[2,7],[3,10]].

Moreover when these conditions hold there is a basis giving exactly V_0=[[1,4,4],[0,1,4],[0,0,1]], with the orientation and actual basis described below.
Thus there is precisely one GL_2(Z) congruence class in this even content4 binary domain.

*Proof.* The implication1=>2 is exactly L312's content theorem and L314's even-complement theorem, with their hypotheses satisfied by the primitive alternating-kernel line Ze_0 of this actual G and its norm minus one.
We now prove2=>3 without importing any classification.

Write epsilon=(s-t)/4 in {1,-1}, a=r/2, c=u/2, and b=(s+t)/2.
These are integers, and

    B=[[2a,b+2epsilon],[b-2epsilon,2c]],
    det B=4ac-b^2+4=-1,
    b^2-4ac=5.                                    (5)

Let J=[[0,1],[-1,0]].
The symmetric and alternating decomposition is

    B=[[2a,b],[b,2c]]+2epsilon J,
    w^T Bw=2 f(w).                                 (6)

For every integer2-by-2 matrix P, direct multiplication gives P^T J P=(det P)J.
If epsilon=-1 first use D=diag(1,-1), which changes the alternating sign to positive and takes f(x,y) to f(x,-y), still with discriminant5.
If epsilon=1 take D=I.
Lemma1 then supplies a determinant1 matrix A for the resulting quadratic form.
Thus P=DA has determinant epsilon and

    P^T B P=B_*=[[2,3],[-1,-2]].                    (7)

The symmetric part follows from twice(2), and its alternating term remains2J; together they determine every entry, proving(7) for the nonsymmetric matrix itself.
This is not an inference from equal scalar polynomials.

Set U=[[1,-2],[0,1]].
Direct multiplication gives U^T B_0 U=B_*.
Hence for T=P U^(-1),

    T^T B T=B_0,  det T=epsilon.                    (8)

This proves2=>3.
Finally L312 supplies the exact matrices

    Q=[[1,2,3],[-1,-1,-2],[1,1,3]],
    Q^(-1)=[[-1,-3,-1],[1,0,-1],[0,1,1]],
    Q^T V_0 Q=[-1] direct-sum B_0, det Q=1.

Consequently the actual integral matrix

    H=diag(1,T) Q^(-1),  det H=epsilon,
    H^T G H=V_0                                  (9)

proves3=>1 as well as the stated explicit realization.
Every transformation is unimodular; no rational change, finite-index complement, additional neutral line or sign-renormalized diagonal is used.
Conversely evenness and alternating content are preserved under any GL_2(Z) congruence, consistent with the equivalence.

This is an existence classification across all integer bases.
It does not say that an arbitrary chosen basis is proper.
The symmetric case s=t is outside the stated nonsymmetric domain; L312 separately excludes it because a symmetric proper form is positive identity whereas G has a negative vector.

<a id="even-binary-full-expenses"></a>
### 4. Full scalar, basis, companion and cover expenses

Keep the ENTIRE polynomials

    Q_-(t)=t^2+18t+1, F(t)=(t+1)Q_-(t),
    ell18=log(9+4sqrt5), ell110=log(55+12sqrt21).

For every B in Theorem2, the direct binary determinant expansion in L312 gives p_B=-Q_-, and the negative line contributes -(t+1), so p_G=F.
Congruence in(9) preserves the whole polynomial, since det H^2=1.
Both roots of Q_- are -9+/-4sqrt5, and every original positive logarithmic measure here is ell18.
The neutral root-1, the binary leading sign-1 and actual degrees2 and3 are retained.
One negative line is sufficient by(9); the even binary form itself has no norm-one vector, so it cannot already be proper.
Also Q_- has no proper rank-two scalar realization, as in L312.
This is an exact fixed-target degree cost, not a general stabilization theorem.

In the original coordinates(5) set

    h_B=max{2|a|,2|c|,|b+2epsilon|,|b-2epsilon|},
    E_B=4a^2+4c^2+2b^2+8.                          (10)

These are the full matrix height and full squared-entry sum.
G has height h_B and full sum E_B+1.
The elementary reduction specifies the complete matrix P as a finite product of displayed shears, rotations and possibly D; T and H are exactly(8)--(9).
It preserves rank and lattice index, but does not assert a uniform bound on the entries of P,T or H as B varies.
Thus the basis change is not treated as a bound on original coefficients or basis height.
The final proper matrix V_0 has height4, strict-upper energy48 and full squared-entry sum51.
Its D9 proper companion has full polynomial(t+1)(t^2-110t+1), and its literal proper cover has rank6, height4, strict-upper energy96, full sum102 and entire polynomial

    (t+1)^2 Q_-(t)(t^2-110t+1).                    (11)

The original, proper-companion and proper-cover logarithmic measures are respectively ell18, ell110 and ell18+ell110.
L312 proves these height/energy and companion/cover minima over ALL proper rank-three forms with full scalar F, so the construction attains the existing optima.
No invariance of the absolute-companion operation under the original congruence is assumed.

For precision the relaxed FULL-entry companion of the original binary matrix is B^-=-|B|, with absolute value entry by entry.
Its pencil determinant is

    p_(B^-)(t)=d_abs(t^2+1)+[8|ac|-2b^2-8]t,
    d_abs=4|ac|-|b^2-4|.                           (12)

Because b is odd and ac=(b^2-5)/4, there are exactly two cases: if |b|=1 then ac=-1 and(12) is(t-1)^2; if |b|>=3 then ac>=1 and(12) is-Q_-.
Therefore with G^-=[-1] direct-sum B^-, the full ternary companion polynomial is respectively -(t+1)(t-1)^2 or F.
The full-entry literal sheet operation replaces each scalar x<=0 by xI_2 and x>0 by -xS, where S exchanges the two sheets.
Equal/opposite sheet coordinates carry -|G| and G, including all diagonal and lower entries.
The same splitting applies to the transpose, so the literal lift has the product p_G p_(G^-).
Its exact cases are:

| Original full-entry lift | Rank | Entire polynomial for abs(b)=1 | Entire polynomial for abs(b)>=3 | Logarithmic measures in the two cases |
| --- | --- | --- | --- | --- |
| binary B | 4 | -Q_-(t)(t-1)^2 | Q_-(t)^2 | ell18; 2ell18 |
| ternary G | 6 | -(t+1)^2 Q_-(t)(t-1)^2 | F(t)^2 | ell18; 2ell18 |

In this table the column conditions refer to the integer parameter b in(5); the displayed polynomials include every sign and neutral factor.
Each relaxed companion has the same height and full sum as its original.
Each literal lift has that same height and twice the original full sum, namely2E_B or2(E_B+1).
These are relaxed lifts with their actual diagonal and lower blocks, not proper covers.
In particular B_* has a neutral relaxed companion whereas B_0 does not, despite their integral congruence.
The full-entry absolute operation is basis dependent, so the proper cost ell18+ell110 remains paid after conversion.
No basis change transfers the cheaper relaxed value into an uncharged proper cover.

<a id="even-binary-complete-self-check"></a>
### 5. Scope, retained unsuccessful route and complete self-check

The formerly tempting content-only sufficiency is false by L314's odd example, and that failed implication remains unchanged.
The corrected conjunction, evenness AND content4, is now sufficient as well as necessary in the exact nonsymmetric binary determinant-minus-one domain.
A possible residual ideal-class obstruction was initially an unresolved alternative; it is discharged here by the explicit orientation-preserving descent at discriminant5.
No class-number assertion was needed.
This does not classify arbitrary odd forms, arbitrary discriminants, higher-rank complements or paid higher-rank stabilization.
All scalar measures in the new positive class remain the fixed large ell18.
There is no varying near-one family or unrestricted gap consequence, and G0001 remains active and unresolved.

The complete original author SELF, contribution and no-program account is retained in [R789](../audits/reviews/Yin_R_G0789_v1.md#original-even-binary-author-self), preserving every original scope, source limit and actual clarification.

<a id="even-binary-source-attribution-status"></a>
### 6. Source-attribution status and freeze

The elementary reduction in Section2 is a specialization of classical integral binary quadratic form reduction.
The [Dum21 selected source inspection](../audits/literature/Dum21/readme.md#selected-binary-reduction-attribution), completed by root and read by this author, supplies precise METHOD attribution: Evan Dummit's2021 Math4527 lecture35, PDF18--27, uses determinant-one substitutions and shear/swap reduction.
Root also inspected the complete PDF38 example and visually checked PDF21,25,38.
This author read the resulting canonical inspection record, not a fresh copy of the PDF.
The source's printed shear matrix on PDF25 has the incorrect offdiagonal a+mb/2, whereas direct multiplication and its following polynomial give am+b/2 and b+2am.
Its PDF21 tie definition conflicts with the PDF26 stopping rule, including the exact(1,1,-1) boundary relevant here.
The apparent discriminant5 sentence on PDF38 belongs to an actual discriminant13 example.
Consequently neither the source's general reduction theorem nor that example is imported.
The correct elementary substitution method is attributed at its inspected scope; formulas(3)--(4), the complete discriminant5 termination and the nonsymmetric orientation accounting are proved here.
No class-number result, complete source audit or priority claim is accepted by implication.
This resolves the bounded method-attribution check without converting the source discrepancies into proof premises.
Existing L312/L314 source and proof boundaries remain those of their retained complete reviews.

The entire author text, Sections1--6, equations(1)--(12) and the two-row full-expense table, is frozen after self-check at2026-10-10T10:08.
The whole noncontributor review will append its own finding without rewriting this author prefix.
No mathematical proof gap or unresolved source-attribution identification remains at the explicitly stated local scope; independent review, fixed adoption and the unrestricted Task remain separate.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0789_v1.md#even-binary-complete-independent-review), with its original inspected scope and relationship.
