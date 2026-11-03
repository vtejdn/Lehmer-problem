---
author: Yin
---
# Full-class coefficient and finite-saving Fourier costs for polynomial shears

Human author Yin.
Root authored this full-class coefficient obstruction on 2026-10-20T11:11, reusing the actual norm family of C176 and the elementary original-energy estimate first retained in D35.
The complete energy argument is included below, so no mutable draft is a logical premise.
No parameter scan, numerical integral or new source acquisition is performed.
This second fixed version makes the opposite G sign, direct DS17 dependency and rational scalar domain explicit after preliminary review identified those interfaces.
The first fixed version remains at [C189v1](Yin_C_G0189_v1.md); no prior whole review or adoption is attributed to it.
The K1 constants and original-input domain are unchanged.
This third fixed version adds the finite-saving Wiener lower bound(K3)--(K4), authored by root on 2026-10-20T11:21.
The complete second version and its actual [R461](../audits/reviews/Yin_R_G0461_v1.md#all-shear-coefficient-whole-independent-finding) remain fixed; that earlier finding does not cover the added Fourier deduction.
Independent whole review remains separate.

## Statement

Use the actual C176 domain: P in Z[z] is monic, irreducible, reciprocal and noncyclotomic, with degree d=2r, constant coefficient1, and totally real trace field Q(alpha+alpha^(-1)).
Keep its full original coefficients and put

    A=||P||_2^2=sum_k p_k^2>=3,
    H35(z)=243 P(z^5)^3-250 P(z^3)^5,
    G(z)=-z^(-15d/2) H35(z)/30375,
    E_G=integral_T G(z)^2 dmu.

The Haar probability normalization is the one in C176, and its reciprocal real Laurent E,F are unchanged.
Here H35 and G have the opposite sign from C176; the whole shear family is identical under its parameter substitution (S,T) maps to(-S,-T), as checked below.
For ANY rational polynomials S,T in x=z+z^(-1), of arbitrary degree and denominator, form

    B=(E+S G)^2+(F+T G)^2+2G^2.

Let h be any integer for which f=z^h B/2 is an ordinary polynomial.
Its actual rational coefficient l1 norm satisfies

    ||f||_1 >= integral_T B/2 dmu >= E_G
       >= A^3(250A-243)^2/30375^2
       >= (169/30375)^2 A^5.                         (K1)

Thus a fixed normalized coefficient budget ||f||_1<=S_0, with S_0>0 independent of P, forces

    A <= (30375^2 S_0/169^2)^(1/5),
    #supp(P) <= floor((30375^2 S_0/169^2)^(1/5)).      (K2)

If the integer cap in(K2) is below3, this class is empty because A>=3.
Otherwise that original-input class is already covered directly by the accepted DS17 bounded-support positive Mahler gap.
C27 is an earlier restricted application of that source, not the general theorem invoked here.
No new gap class follows by supplying C140's fixed normalized coefficient hypothesis through this family with its prescribed2^d arithmetic floor.
In any hypothetical sequence of these original P with positive total measure tending to zero, the normalized coefficient norm tends to infinity for EVERY choice of S,T,h, even when those choices depend on P and have unrestricted degree and denominator.

There is also an actual logarithmic Fourier lower bound for the SAME full shear class.
Put I=integral_T log B dmu and W_*(log B)=sum_(k!=0)|integral_T log B(z) z^(-k) dmu|, allowing infinity.
Then

    W_*(log B)>=log(integral_T B dmu)-I
               >=log(2E_G)-I.                        (K3)

In particular any finite saving I<=log2-eta with eta>=0 satisfies

    W_*(log B)>=log E_G+eta
       >=5log A+2log(169/30375)+eta.                  (K4)

Thus along any hypothetical permitted sequence with positive total measure tending to zero, EVERY allowed choice whose Haar logarithm is at most log2 has actual W_*(log B) tending to infinity.
No fixed-input approach to the full infimum, particular geometric sequence or circle-zero assumption is required for this conclusion.
A negative right side at a small input is simply a valid weak lower bound, not a positive expense assertion at that input.

The result does not exclude a finite Haar saving, a transfer estimate in which a growing Fourier cost is compensated by a decreasing original-root discrepancy, a family without the protected2G^2 term, or use of a stronger separately proved actual norm income.
It does not assume that every actual original norm equals its guaranteed2^d lower bound.

<a id="argument"></a>
## Complete proof

### The protected component gives an actual coefficient lower bound

The G defined here equals minus the G of C176; sign reversal preserves its real reciprocal Laurent property and its square.
For each pair S,T, the present B is exactly C176's B with parameters -S,-T, so its all-rational-shear and original norm interfaces apply without changing any original value.
All of E,F,G,S(z+z^(-1)),T(z+z^(-1)) are therefore real on the unit circle, by the same reciprocity conventions.
Consequently B is nonnegative there and B>=2G^2 pointwise.
H35 is a nonzero polynomial: its degree15d leading coefficient is243-250=-7.
Thus G is nonzero and B is not the zero Laurent polynomial.
Writing B as a finite Laurent sum, its constant coefficient is exactly its Haar mean.
Multiplication by z^h merely shifts its coefficient list.
The coefficient of z^h in f=z^hB/2 therefore equals the nonnegative number integral B/2, while ||f||_1 dominates the absolute value of every one of its coefficients.
This proves the first two inequalities of(K1), including all coefficient cancellations in the expanded squares.
It is an actual lower bound, not growth of a supplied coefficient upper estimate.

Writing B=z^(-h)A_B/D with an integer numerator and a cleared positive denominator changes none of this: the normalized ordinary polynomial is exactly A_B/(2D)=f.
Increasing the common denominator or choosing another monomial shift leaves the actual coefficient norm unchanged.
The same observation applies to any positive rational scalar multiple lambda B if the guaranteed arithmetic threshold is multiplied by the same lambda: normalization by2lambda again returns B/2.
A different, stronger actual original norm may permit another normalization, but it would need its own proved quantitative bound and is outside this assertion.

### Original polynomial energy, with every exponent and constant retained

All Lp norms below use Haar probability measure on the unit circle.
Power maps preserve that measure.
Set x=||P||_10 and y=||P||_6.
Then

    ||P(z^3)^5||_2=x^5,
    ||P(z^5)^3||_2=y^3,
    y<=x, x>=||P||_2=sqrt A.

The reverse triangle inequality gives

    ||H35||_2>=250x^5-243y^3
              >=250x^5-243x^3.

The function t->250t^5-243t^3 has derivative t^2(1250t^2-729)>0 for t>=1.
As A>=3, it follows that

    ||H35||_2>=A^(3/2)(250A-243)>0.

On the circle, G is real and its squared modulus equals |H35|^2/30375^2, since the centering monomial has modulus1.
Thus E_G=||H35||_2^2/30375^2 and the third inequality in(K1) follows.
For A>=3,250A-243>=169A, giving the final inequality.
The premise A>=3 is exact: integer coefficients and monic constant-one endpoints give A>=2, while equality would force P=z^d+1, all of whose roots are roots of unity, contrary to noncyclotomic irreducibility.
No coefficient positivity, selected pair of control polynomials, vanishing defect, or near-one assumption was used in(K1).

### Actual Fourier expense of a finite Haar saving

The nonzero real Laurent polynomial B is bounded above on the circle and satisfies B>=2G^2 there.
The logarithm of G^2 is integrable because G is a nonzero Laurent polynomial with finitely many circle zeros.
Therefore log B is an integrable real function, with the inequalities understood away from the finite zero set.
Its Haar mean I is finite, and its Fourier coefficients have the normalization in the statement.

If W_*(log B) is infinite, both(K3) and(K4) hold in the extended-real sense.
If it is finite, its Fourier series including constant I converges absolutely and uniformly to a continuous function F.
The actual Fejer-uniqueness argument retained in [C177](Yin_C_G0177_v1.md#argument) identifies F with log B almost everywhere: the two functions have the same Fourier coefficients, and the Fejer means converge to the integrable function in L1 and to the continuous Fourier sum uniformly.
Consequently |log B-I|<=W_*(log B) almost everywhere.
Exponentiating and integrating gives

    integral_T B dmu<=exp(I+W_*(log B)).

Taking logarithms and using the protected-component lower bound proves(K3).
If I<=log2-eta, substitute this upper bound and then(K1) to obtain(K4).
This is a necessary bound on the ACTUAL Fourier norm, rather than a growing upper estimate for it.
The proof covers arbitrary polynomial degrees and rational coefficients, all allowed original inputs, and all finite Haar savings at the prescribed arithmetic threshold.
The possible growth of W_* does not by itself preclude an error bound multiplied by another input-dependent quantity tending to zero.
No lower bound for that complete product or for the actual original/Haar discrepancy is inferred here.

### Exact old coverage and the genuine remaining transfer issue

Since every nonzero integer coefficient contributes at least1 to A, the support bound in(K2) is immediate.
The accepted [DS17 source theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) directly gives a positive gap for each fixed positive integer support count.
If the cap in(K2) is below3 there is no input, so no nonexistent support-zero gap constant is invoked.
The earlier [C27](Yin_C_G0027_v1.md#statement) applies that same source to flat first-window inputs; its narrower project statement is not substituted for the general source theorem here.
This invocation asserts neither an effective numerical constant nor a new proof of that source theorem.
A fixed S_0 therefore restricts original inputs to an old gap class, even before any additional degree, term-count or logarithmic-saving hypotheses from [C140](Yin_C_G0140_v1.md#statement) are imposed.

Conversely, along a hypothetical positive-total-measure-to-zero sequence, that same old theorem forces #supp(P) and hence A to tend to infinity.
The uniform pointwise-in-choice lower bound(K1) then forces ||f||_1 to infinity for every sequence of the allowed shears.
This does not rely on existence of such a near-one sequence or select a cheap representative after omitting coefficients.

The accepted [C176 original norm theorem](Yin_C_G0176_v1.md#polynomial-shear-exact-infimum) supplies |Norm_Q(alpha)(B(alpha))|>=2^d with every original embedding, even though the shears can have rational coefficients.
Since alpha is a unit, |Norm(alpha^h)|=1, so |Norm(f(alpha))|>=1 in that same original field.
The coefficient obstruction concerns precisely this floor-normalized f.
It is compatible with C176's exact full-class Haar infimum and finite useful savings, and with C177's separate fixed-input near-infimum Wiener divergence.
It adds necessary all-shear coefficient and finite-saving Fourier prices on varying original inputs; it supplies no upper Fourier/radial error bound or impossibility for a paid product of a growing norm and decreasing discrepancy.
Thus the remaining D36 obligation requires a transfer budget beyond a fixed normalized l1 bound at this prescribed floor, stronger actual income, or a changed protected component.

<a id="inputs-and-limits"></a>
## Inputs and checking limits

| Input | Exact role |
| --- | --- |
| [C176 statement and argument](Yin_C_G0176_v1.md#statement) | Actual original trace-field domain, real Laurent centering, all rational polynomial shears and original norm floor. Its accepted whole and extraction reviews are reused at their fixed scopes. |
| [DS17-U001](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Direct accepted general fixed-support gap and the hypothetical near-one support-escape consequence. C27 is only an earlier restricted application/comparison. |
| [C140](Yin_C_G0140_v1.md#statement) | Comparison only: a fixed normalized coefficient l1 bound is one of its actual hypotheses; no assumption that its integral-value statement automatically covers rational shears. |
| [C177 Fejer argument](Yin_C_G0177_v1.md#argument) | Accepted L1 Fourier uniqueness interface for the new(K3) deduction, with the complete particular application supplied here. Its older fixed-input near-infimum conclusion is a comparison only. |

The elementary finite-polynomial Haar, Lp and triangle calculations are fully supplied above.
The argument's original D35 energy step has not been treated as an independently accepted result merely because it was previously written down.
This whole combined theorem needs its own independent finding.

## Current assessment
[Selected decision](#decision-finite-saving-extension-2026-10-20)

## Assessment history

### Decision finite-saving-extension-2026-10-20

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:21 |
| status | open |
| reason | Extend the same full-class cost theorem by the complete actual Wiener lower bound for every finite Haar saving, preserving v1/v2 and R461. The result does not rule out a growing Fourier norm multiplied by a shrinking original-root discrepancy; whole review of this actual extension is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full-class coefficient obstruction](#statement) | Every actual original input and every rational polynomial pair, full normalized coefficient lower bound, old coverage, actual finite-saving Wiener lower bound and conditional near-one divergence with exact limitations. |
| argument | [Complete protected-component proof](#argument) | Actual central coefficient, full Lp/power and reverse-triangle estimates, exact A>=3/constants, canonical scalar normalization, full Fourier/Fejer inequality and old-support implication. |
| dependency | [Accepted polynomial-shear family](Yin_C_G0176_v1.md#statement) | Actual original-field domain, Laurent definitions and all rational shears with their complete norm floor. |
| support | [Earlier restricted support-gap application](Yin_C_G0027_v1.md#statement) | Historical comparison only; its flat first-window domain is not a premise for the general coefficient class. |
| dependency | [Exact bounded-support source](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Accepted source statement/application scope for every fixed term count. |
| support | [Actual sparse-transfer hypotheses](Yin_C_G0140_v1.md#statement) | Normalized coefficient budget comparison only, without silently enlarging its integral-value theorem. |
| dependency | [Accepted Fejer uniqueness argument](Yin_C_G0177_v1.md#argument) | L1 function with absolutely summable Fourier coefficients agrees almost everywhere with its continuous Fourier sum; the new exponential-mean comparison is supplied in this version. |
| support | [Full source and author limits](#inputs-and-limits) | Existing upstream reviews reused, original energy calculation supplied here and no program or all-transfer impossibility assertion. |
| support | [Earlier v2 whole finding](../audits/reviews/Yin_R_G0461_v1.md#all-shear-coefficient-whole-independent-finding) | The complete previous coefficient theorem and its source/sign interfaces only; not a review of the new K3--K4 deduction. |
