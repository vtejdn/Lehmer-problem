---
author: Yin
---

# An effective total-Mahler gap for binary period-six inner coefficients

Human author Yin.
Root proposed the complete binary reflection classification, signed support-run reduction and exceptional factorizations.
Contributor characteristic_zero_bridge checked and assembled all cases, endpoints, reversal and original costs.
Both are substantive author contributors, not independent reviewers.
The [selected adopted decision](#decision-whole-reviewed-2026-10-28) is proved through [whole independent R1063](../audits/reviews/Yin_R_G1063_v1.md#whole-binary-period-six-finding).
The initial OPEN decision and fixed argument retain their historical wording; the separate review covers the complete new period-six proof at its exact adopted-input scope.
No native computation, polynomial enumeration, root calculation, numerical gap or new source acquisition has been performed.

## Statement

### A. Original irreducible class and computable all-degree gap

Use the [periodic inner-coefficient convention of adopted C842](Yin_C_G0842_v1.md#periodic-inner-coefficient-class), specialized to modulus2 and period6.
Precisely, let

    P(x)=x^D+sum_(j=1..D-1)a_j x^j+1 in Z[x]

be monic, reciprocal, irreducible over Q and noncyclotomic, and suppose there are binary residues r_0,...,r_5 with a_j=r_(j mod6) modulo2 for every ACTUAL inner index1<=j<D.
Then there is an algorithmically computable positive rational g_(2,6), independent of D and the residue tuple, such that

    log M(P)>g_(2,6)>0.                                  (ST1)

M is the full multiplicative Mahler measure; logarithms are natural, and no degree normalization is made.
Only actual inner indices impose residue conditions; absent classes in degrees2,4,6 impose no condition.
The endpoint coefficients remain exactly1.
No numerical value or efficient running-time bound is asserted.
Taking the minimum with C842's accepted binary bounds through period5 gives a computable positive rational bound for all binary inner residue periods at most6.
This last statement is a finite union, not an arbitrary-period assertion.

### B. Complete finite templates and original auxiliary costs

The original degree D is even.
For every D>=8, s=D modulo6 is0,2 or4, and reciprocity forces r_j=r_(s-j).
There is an explicitly specified finite set of at most48 labeled monic degree-six integer polynomials G, independent of D, with coefficients in{0,+1,-1} and M(G)<2, such that every compatible tuple has an exact integral reflection lift c_j=c_(s-j) and

    Q_D=x^D+sum_(j=1..D-1)c_(j mod6)x^j+1,
    G=x^6+c_1x^5+c_2x^4+c_3x^3+c_4x^2+c_5x+(c_0-1),
    G*=x^6G(1/x),
    F_D=x^D G-G*=(x^6-1)Q_D in(P,2).                   (ST2)

Every reversal uses the actual degree6, even when G(0)=0.
The exact templates and all three degree classes are given in BP3--BP5 below, including both cyclotomic exceptions in the s=0 class, the golden-ratio exception and every reversed s=4 case.
For the SAME original P and exponent D,

    F_D!=0, #supp F_D<=14, ||F_D||_1/2<=7,
    deg F_D=D+6<=(7/4)D, D>=8.                          (ST3)

At a root alpha of P, F_D(alpha)/2 is an algebraic integer, with zero allowed.
The already adopted finite-family transfer pays that zero-value branch before using an integer norm.
The low degrees2,4,6 are completed by C842's accepted effective bounded-degree floor, without extending the reflection constraints to unused residues.

### C. Signed support-run lemma and all exceptions

Let G be a nonzero polynomial with coefficients in{0,+1,-1}, constant in sign on each of its r maximal contiguous support intervals[a_i,b_i].
Write sigma_i for the sign on the ith run.
Then the2r boundary exponents in

    (x-1)G=sum_i sigma_i(x^(b_i+1)-x^a_i)

are distinct and ||(x-1)G||_2^2=2r.
Since(x-1)G is nonmonomial, strict Jensen gives M(G)<sqrt(2r); in particular at most two such runs give M(G)<2.
This permits different signs on separated runs but not a sign change within a run.
The other direct case is at most four coefficients of magnitude1, with a monic monomial treated separately.
The only extra factorization mechanisms needed for the complete reflection list are

    x^6+x^4-x^3+x^2+1=Phi_3 Phi_10,
    x^6+x^5-x^3+x+1=Phi_3 Phi_12,
    x^6-x^5-x^3-x-1=Phi_3 Phi_6 (x^2-x-1),              (ST4)

and sign-reversal of the last or of other templates from the D=2 modulo6 class.
The measures in ST4 are1,1 and the golden ratio phi=(1+sqrt5)/2<2, respectively.
All products and reflection compatibilities are proved below rather than inferred from a finite scan.

### D. Effective input and limits

Apply the [adopted C842 finite-family criterion](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) to the complete finite set in ST2 with modulus2 and k=6.
Its effective proof has cutoff B0=max(55,6J); every degree above it satisfies D>=8 and ST2.
The sharper original large-degree budgets K=14,S=7,C=7/4 in ST3 are valid for its error step, while its generic ratio1+k/2 would also suffice.
C842's C391 bounded-degree completion covers every degree at most B0.
The proof does not reproduce C842's certificate algorithm, qualitative alternative or earlier period cases, and does not execute any of them.

There is no ternary period-six result, arbitrary residue period, uniform arbitrary-modulus bound, near-one construction, new root-distribution theorem or unrestricted Lehmer conclusion.
The inputs are the actual original irreducible polynomials, not reducible cyclotomic witnesses from a different residual system.
The full total measure, original degree and accepted source-inspection limits remain explicit.

## Exact input and extraction scope

[C842's adopted ST1--ST6/FG2--FG3/EF1--EF6](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) supplies the finite reversal-family theorem, the terminating effective certificate, actual ideal/zero-value treatment and bounded-degree completion.
Its [PF3 strict energy argument](Yin_C_G0842_v1.md#pf3-the-strict-coefficient-energy-test) supplies strict Jensen/Parseval with integrable circle zeros, alongside the retained full Mahler multiplicativity and monomial conventions.
Its earlier binary period cases are used only for the finite-union corollary through period6.
C842's independent review covers those accepted inputs, not the new case proof below; no source's inspection depth or proof status is upgraded.
The exact cyclotomic products and quadratic roots needed here are displayed and checked locally, without a Rouche theorem or external root-classification premise.

The proof originated at [D7's binary period-six section](../drafts/Yin_D_G0007.md#binary-period-six-coefficient-gap); this is extraction provenance only.
The separate source/lift and scalar-energy investigations in that draft are not dependencies.
The entire new BP1--BP6 argument follows, with no mutable Draft or unrun native program supplying a premise.

## Complete argument

### BP1. Original domain and the exact degree-six reversal identity

Let P=x^D+sum_(j=1..D-1)a_j x^j+1 be monic reciprocal irreducible noncyclotomic in Z[x], with a_j congruent to r_(j mod6) modulo2 for fixed binary residues r_0,...,r_5.
The original degree D is even, by the usual root-1 consequence for odd reciprocal degree.
For D>=8 every residue class modulo6 occurs among the inner indices.
Thus reciprocity forces r_j=r_(s-j), s=D modulo6, and s is one of0,2,4.
Incompatible patterns supply no P at that degree.
The complete integral reflection shapes are

| s | (c_0,c_1,c_2,c_3,c_4,c_5) |
| --- | --- |
| 0 | (A,B,C,E,C,B) |
| 2 | (A,B,A,C,E,C) |
| 4 | (A,B,E,B,A,C) |

The letters denote residue lifts chosen below; their names within each row are local to that row.
Each row has four independent binary orbit residues, so there are16 labeled patterns per degree class.
For any exact integral reflection lift put

    Q_D=x^D+sum_(j=1..D-1)c_(j mod6)x^j+1,
    G=x^6+c_1x^5+c_2x^4+c_3x^3+c_4x^2+c_5x+(c_0-1),
    G*=x^6G(1/x).

Every G is monic of actual degree6; that degree is retained in its reversal even if G(0)=0.
The exact integer identity is

    (x^6-1)Q_D=x^D G-G*, D>=8.                         (BP1)

Its low coefficients at0,...,6 are(-1,-c_1,-c_2,-c_3,-c_4,-c_5,1-c_0), its high coefficients at D,...,D+6 are(c_0-1,c_5,c_4,c_3,c_2,c_1,1), and all intervening coefficients cancel by periodicity.
Reciprocity gives precisely the displayed high block.
These two ranges are disjoint, including at the smallest allowed even D=8.
Since Q_D is reciprocal and congruent to P modulo2, writing P=Q_D+2R gives

    F_D=x^D G-G*=(x^6-1)P-2(x^6-1)R in(P,2).          (BP2)

This is ideal membership for the SAME original P and original exponent D.
At every root alpha of P, F_D(alpha)/2 is integral, with a zero value allowed by the finite criterion's already paid zero branch.
For D=2,4,6, absent residue classes impose no constraints; those degrees will be handled by the bounded-degree completion.

<a id="signed-support-run-energy"></a>
### BP2. Strict energy and signed support runs

Reuse the complete strict Jensen/Parseval argument in [C842 PF3](Yin_C_G0842_v1.md#pf3-the-strict-coefficient-energy-test): a nonmonomial H satisfies M(H)<||H||_2, and a monic monomial has M=1.
In particular, a monic polynomial with at most four nonzero coefficients, all of magnitude1, has M<2.
Circle zeros are included in that argument's integrable-logarithm convention.

For a nonzero polynomial G with coefficients in{0,+1,-1}, suppose every maximal contiguous support run has a constant sign.
Write its runs as intervals[a_i,b_i], ordered with a_(i+1)>=b_i+2, and its sign on that run as sigma_i in{+1,-1}.
Then

    G=sum_(i=1..r) sigma_i sum_(j=a_i..b_i)x^j,
    (x-1)G=sum_(i=1..r) sigma_i(x^(b_i+1)-x^(a_i)),
    ||(x-1)G||_2^2=2r.                                (BP3)

The2r endpoint exponents are distinct because of the strict gap between runs, including when the constant coefficient of G is zero.
Thus no uncounted cancellation or opposite-sign adjacency is hidden in BP3.
The nonzero polynomial(x-1)G vanishes at1, so it cannot be a monomial.
Since M(x-1)=1, r<=2 implies

    M(G)=M((x-1)G)<sqrt(2r)<=2.                        (BP4)

A sign change within one contiguous support run is NOT covered by this lemma.
The exceptional cases below are handled by exact factorizations instead.

### BP3. Degree zero modulo six

For s=0 choose H,B,C,E in{0,1}, with H representing r_0-1, and set A=H+1.
The resulting polynomial is

    G=x^6+B(x^5+x)+C(x^4+x^2)+E x^3+H.                 (BP5)

The class0 is fixed by reflection, so replacing its lift by H+1 does not constrain any other residue orbit.
If G has at most four terms, BP2 applies directly.
Suppose instead it has at least five terms.
If H=0, its support lies in{1,...,6} and has at most one missing position; hence it has at most two contiguous runs, all positive.
This gives M(G)<2 by BP4.

If H=1, both endpoints0 and6 are present, and there are at most two zero positions among1,...,5.
The possible zeros are the pair{1,5} when B=0, the pair{2,4} when C=0, and the single position3 when E=0.
With at most two zeros, the only three-run patterns are EXACTLY{1,5} or{2,4}; a single zero gives at most two runs, and no zeros gives one.
Thus every other case is already covered by BP4.
For these two remaining patterns change only the lift E from1 to-1, preserving its binary residue and reflection, and use

    x^6+x^4-x^3+x^2+1
        =(x^2+x+1)(x^4-x^3+x^2-x+1)=Phi_3 Phi_10,
    x^6+x^5-x^3+x+1
        =(x^2+x+1)(x^4-x^2+1)=Phi_3 Phi_12.            (BP6)

Both products follow by multiplying the displayed polynomials and have Mahler measure1.
This treats all16 degree-zero reflection patterns, including every endpoint and support size.

### BP4. Degree two modulo six

For s=2 the shape is(c_0,c_1,c_2,c_3,c_4,c_5)=(A,B,A,C,E,C).
First let A=1 and choose B,C,E in{0,1}.
Then

    G=x^6+B x^5+x^4+C x^3+E x^2+C x.

Its constant coefficient is zero and all other coefficients are0 or1.
If there are at most four terms, BP2 applies; with at least five terms, at most one of the six positions1,...,6 is absent, so BP4 applies.

Now let A=0 and let B,C,E in{0,1} denote the remaining binary residues.
Choose the actual lifts c_1=B, c_3=c_5=-C and c_4=-E, giving

    G=x^6+B x^5-C x^3-E x^2-C x-1.                    (BP7)

There is a compulsory zero at position4.
The support size is2+B+2C+E.
Size at most four is again handled directly, regardless of signs.
For size at least five one must have C=1 and B+E>=1, leaving exactly three possibilities.
If B=E=1, the runs are[0,3] with sign-1 and[5,6] with sign+1.
If B=0,E=1, the runs are[0,3] with sign-1 and{6} with sign+1.
Both have M(G)<2 by BP4.

The sole remaining case is B=1,E=0,C=1.
Change c_1 from+1 to-1, retaining all binary residues and the exact reflection.
Then

    G=x^6-x^5-x^3-x-1
       =(x^4+x^2+1)(x^2-x-1)
       =Phi_3 Phi_6 (x^2-x-1).                         (BP8)

Direct multiplication proves both factorizations.
The roots of x^2-x-1 are phi=(1+sqrt5)/2 and-1/phi, so its Mahler measure is phi<2 because sqrt5<3.
Therefore BP8 has M(G)<2 as required.
All16 s=2 reflection patterns are now covered.

### BP5. Degree four modulo six and exact reversal of the zero-orbit cases

For s=4, use the shape(A,B,E,B,A,C).
If A=1, choose the other lifts in{0,1}; the polynomial has constant coefficient0 and all other coefficients0 or1.
The same at-most-four-term or at-most-one-hole argument in positions1,...,6 proves M(G)<2.

If A=0, all patterns are obtained bijectively from the s=2,A=0 patterns by

    G_new=-G_old*,
    c'_0=0, c'_j=-c_(6-j), 1<=j<=5.                   (BP9)

The old constant coefficient is-1, so G_new is monic of degree6 and has constant coefficient-1, exactly as required for c'_0=0.
Modulo2 the minus signs do not change residues.
The old equality c_i=c_(2-i) implies c'_j=c'_(4-j), including c'_4=0, so the new integral reflection is exact.
For prescribed new residues, the inverse substitution r_i=r'_(6-i) gives the unique old s=2 pattern; thus no s=4 case is omitted.
Reversal and multiplication by-1 preserve Mahler measure, so the complete s=2 conclusion, including its small-support cases, supplies M(G_new)<2.
For example the reversal of BP8 is

    x^6+x^5+x^3+x-1=(x^4+x^2+1)(x^2+x-1),

again of measure phi.
This example is illustrative; the bijection BP9 covers every one of the eight A=0 cases without a further case assumption.
Together with A=1 it gives all16 s=4 patterns.

### BP6. Finite set, exact budgets and the all-degree consequence

Let Gset_2,6 consist of the templates selected in BP3--BP5, retaining at most3*16=48 labels.
Every member is monic of actual degree6, has coefficients in{0,+1,-1}, and satisfies M(G)<2.
Repeated polynomials may be retained or removed; no minimality or enumeration result is claimed.
For D>=8 the original auxiliary BP2 therefore has

    #supp F_D<=14,
    ||F_D||_1/2<=7,
    deg F_D=D+6<=(7/4)D.                              (BP10)

The auxiliary is nonzero because its leading term x^(D+6) cannot cancel against G*.
Its original degree and length are those in BP10, not the degree or support of(x-1)G used only for the measure bound.

Applying [C842's fixed finite-reversal criterion and effective proof](Yin_C_G0842_v1.md#fixed-reversal-auxiliary-class) to m=2 and this finite set gives a computable positive rational gap for the large-degree class.
The actual large-degree budgets are K=14,S=7,C=7/4.
The generic effective proof has k=6 and cutoff B0=max(55,6J), so every original degree above the cutoff satisfies D>=8 and the exact reflection/ideal construction.
Its already paid C391 bounded-degree height floor handles every smaller degree, in particular D=2,4,6, without imposing constraints on unused residues.
The sharper degree ratio in BP10 is valid in that large-degree error step; the generic criterion would also remain valid with its unsharpened ratio1+k/2.
No new algorithm, root computation, Fourier calculation, finite polynomial enumeration or numerical gap has been run.

Thus the complete author deduction yields an algorithmically computable positive rational g_(2,6), independent of the binary tuple and original degree, such that

    log M(P)>g_(2,6)>0

for every monic reciprocal irreducible noncyclotomic integer P whose inner coefficient residues have period dividing6 modulo2.
Together with C842's binary periods through5, taking a minimum gives the corresponding author conclusion through period6 modulo2.
The generic finite-family input is adopted in C842; no adoption or independent review of this separate period-six extension is asserted here.
No modulus-three period-six result, arbitrary residue period, uniform arbitrary-modulus theorem, near-one construction or unrestricted Lehmer conclusion follows.
The full original total measure, irreducibility and degree are retained throughout, and all inherited source-attribution and inspection limits remain those of C842.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision binary-period-six-gap-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:03 |
| status | open |
| reason | Fix the complete binary period-six finite template theorem and effective total-Mahler gap: all48 labeled reflection choices, exact original reversal congruence, strict signed-run and small-support bounds, all factored exceptions and reversal cases, original K14/S7/C7/4 costs and complete low-degree handling. Root and characteristic_zero_bridge are substantive contributors. Adopted C842 supplies the precise finite/effective transfer; this new proof awaits its own whole independent review and responsible adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire binary period-six theorem](#statement) | ST1--ST4 and all accompanying conditions: original irreducible reciprocal full measure, every degree/tuple,48 labeled finite lifts, signed-run lemma and exceptions, exact ideal/scalar/zero/degree costs, effective cutoff/small degrees and no ternary/general-period/unrestricted conclusion. |
| argument | [Complete BP1--BP6](#complete-argument) | All reciprocal classes and endpoint blocks, strict Jensen/support-run endpoints with signs and zero constants, complete s0/s2/s4 case split, explicit cyclotomic/golden-ratio products, bijective reversal, finite-set budgets and exact accepted-criterion application. |
| dependency | [Adopted effective finite-reversal criterion and earlier binary cases](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | ST1--ST6/FG2--FG3/EF1--EF6 only for the general finite-G transfer, actual original ideal/zero-value/degree conditions, effective certificate and C391 low-degree completion; PF3 for strict Jensen/Parseval and full Mahler conventions; earlier binary periods through5 only for the finite-union corollary. Its entire proof and source limits are reused without duplicate derivation or transferred review coverage for BP. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T22:11 |
| status | proved |
| reason | Adopt the entire binary period-six theorem and BP1--BP6 proof after root read the complete author argument, fixed statement and fresh whole independent R1063. All 48 reflection labels, signed-run endpoints, cyclotomic and golden-ratio exceptions, bijective reversal, original K14/S7/C7/4 costs, exact effective C842 interface and low degrees are covered. The finite union gives binary periods through six. No ternary period-six, arbitrary-period, numerical algorithm execution, modulus-uniform or unrestricted Lehmer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire binary period-six theorem](#statement) | ST1--ST4 and all accompanying conditions: original irreducible reciprocal full measure, every degree/tuple,48 labeled finite lifts, signed-run lemma and exceptions, exact ideal/scalar/zero/degree costs, effective cutoff/small degrees and no ternary/general-period/unrestricted conclusion. |
| argument | [Complete BP1--BP6](#complete-argument) | All reciprocal classes and endpoint blocks, strict Jensen/support-run endpoints with signs and zero constants, complete s0/s2/s4 case split, explicit cyclotomic/golden-ratio products, bijective reversal, finite-set budgets and exact accepted-criterion application. |
| dependency | [Adopted effective finite-reversal criterion and earlier binary cases](Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | ST1--ST6/FG2--FG3/EF1--EF6 only for the general finite-G transfer, actual original ideal/zero-value/degree conditions, effective certificate and C391 low-degree completion; PF3 for strict Jensen/Parseval and full Mahler conventions; earlier binary periods through5 only for the finite-union corollary. Its entire proof and source limits are reused without duplicate derivation or transferred review coverage for BP. |
| review | [Whole independent binary period-six finding](../audits/reviews/Yin_R_G1063_v1.md#whole-binary-period-six-finding) | Entire fixed statement/ST1--ST4 and BP1--BP6, all cases and exact adopted C842 effective/zero-value/low-degree/finite-union scopes; eight precise bindings, no author dialogue, mutable Draft, prior target verdict or substantive repair. |

