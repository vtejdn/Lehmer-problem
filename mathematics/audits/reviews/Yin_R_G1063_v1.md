---
author: Yin
---

# Whole independent review of the binary period-six coefficient-gap theorem

Human record author Yin.
Review act: 2026-10-28T22:08 UTC.
The reviewer is a separately assigned agent outside the substantive development of C843.
The assignment supplied the fixed C843 path, its complete requested scope and operational limits, without proof-development dialogue, mutable Draft contents, author explanations or a prior C843 verdict.
The reviewer read the entire 306-line fixed candidate, formed obligations from its complete statement, and checked every part of BP1--BP6 before consulting the earlier C842 review's arrangement and binding declarations.
C842's exact adopted theorem, finite-family interface, EF1--EF6 effective proof and PF3 energy argument were inspected as accepted inputs.
The earlier R1062 supplies independently reviewed evidence for C842 at its recorded scope; neither it nor C842's adoption supplies review of the new period-six cases.
No mutable Draft was read, no native mathematical program was executed, and no substantive proof repair was supplied by this reviewer.
The inspected target is the OPEN decision [binary-period-six-gap-open](../../claims/Yin_C_G0843_v1.md#decision-binary-period-six-gap-open).
This R records evidence and makes no Claim adoption or Task-completion decision.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole binary period-six finding](#whole-binary-period-six-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-binary-period-six-finding) | [C843 exact statement](../../claims/Yin_C_G0843_v1.md#statement) | Entire A--D, ST1--ST4 and accompanying conditions: original irreducible reciprocal unit domain, every actual residue tuple and degree, all 48 labeled degree-six lifts, signed support-run lemma and all exceptional products, original ideal/zero/support/length/degree costs, computable rational gap, low degrees and finite-union corollary, with all exclusions. |
| [Whole finding](#whole-binary-period-six-finding) | [C843 complete argument](../../claims/Yin_C_G0843_v1.md#complete-argument) | Every step of BP1--BP6, including degree parity, all three reflection shapes, exact two-block identity, integral ideal membership, strictness and circle zeros, complete support case splits, both cyclotomic cases, golden-ratio case, bijective reversal, fixed finite family, effective transfer and all-degree restoration. |
| [Whole finding](#whole-binary-period-six-finding) | [C843 fixed OPEN decision](../../claims/Yin_C_G0843_v1.md#decision-binary-period-six-gap-open) | Exact statement/argument selections and its sole adopted C842 dependency; this binding does not itself change the assessment. |
| [Whole finding](#whole-binary-period-six-finding) | [C842 adopted decision](../../claims/Yin_C_G0842_v1.md#decision-whole-reviewed-2026-10-28) | Reused ST1--ST6 and FG2--FG3/EF1--EF6 finite-family theorem, actual integer ideal and zero-value treatment, effective rational certificate and C394 low-degree completion; PF3 and retained total-Mahler conventions; binary periods through five only for the finite-union corollary. Exact applicability was checked without repeating C842's whole review or upgrading its source limits. |
| [Whole finding](#whole-binary-period-six-finding) | [C842 fixed-reversal auxiliary class](../../claims/Yin_C_G0842_v1.md#fixed-reversal-auxiliary-class) | Monic finite integral family, actual degree in reversal, M(G)<2, original nontorsion irreducible unit P and original exponent D; hypotheses matched for all D above the effective cutoff. |
| [Whole finding](#whole-binary-period-six-finding) | [C842 effective finite-family proof](../../claims/Yin_C_G0842_v1.md#effective-fixed-reversal-auxiliary-gap) | EF1--EF6 interfaces: finite negativity search, D>6J frequency cutoff, raw modulus-two scaling, original norm and nonzero guard, K=14/S=7/C=7/4 large-degree substitution, B0=max(55,6J), independent bounded-degree height floor and strict rational output. Algorithms are reused, not executed. |
| [Whole finding](#whole-binary-period-six-finding) | [C842 strict coefficient energy](../../claims/Yin_C_G0842_v1.md#pf3-the-strict-coefficient-energy-test) | Nonmonomial strict Jensen/Parseval including integrable circle zeros, monic monomial convention and applicability to G and (x-1)G. |
| [Whole finding](#whole-binary-period-six-finding) | [C892 prior independent finding](Yin_R_G1062_v1.md#whole-short-period-gap-finding) | Its arrangement and explicit bindings were inspected after the new target's initial mathematical findings, solely to confirm the accepted C842 input scope; no earlier period-six review or new whole C842 audit is asserted. |

## Original domain, reflection and auxiliary identity

For odd reciprocal degree, P(-1)=0.
Irreducibility would then force P=x+1, which is cyclotomic, so the original admissible degree is even and at least two.
For every D>=8 the inner indices 1,...,D-1 contain all six residue classes.
Reciprocity therefore gives the full relation r_j=r_(s-j), with s=D modulo 6 in {0,2,4}; unused residues at D=2,4,6 are not constrained by this argument.

The involution j -> s-j has four orbits in each allowed class.
For s=0 they are {0},{3},{1,5},{2,4}; for s=2 they are {0,2},{1},{3,5},{4}; for s=4 they are {0,4},{1,3},{2},{5}.
These give exactly the three displayed integral shapes and 16 binary orbit assignments in each shape.
The lifts selected below preserve every orbit equality over the integers, which is stronger than the required binary equality.

In (x^6-1)Q_D, the low coefficients at exponents 0,...,6 are

    (-1,-c_1,-c_2,-c_3,-c_4,-c_5,1-c_0).

Periodicity cancels every coefficient strictly between the low and high blocks.
The high block at D,...,D+6 is

    (c_0-1,c_5,c_4,c_3,c_2,c_1,1),

because c_(s-j)=c_j.
These are precisely the coefficients of -G* and x^D G respectively.
The blocks are disjoint for D>=8, including D=8, and every G is monic of actual degree six even when its constant coefficient vanishes.
Thus BP1 is an exact integer polynomial identity under the stated domain, rather than a congruence extrapolated to unrepresented residues.

Every selected c_j has the prescribed binary residue, so R=(P-Q_D)/2 belongs to Z[x].
Consequently F_D=(x^6-1)P-2(x^6-1)R belongs to (P,2) for the same original P and exponent D.
At an original root alpha, F_D(alpha)/2=-(alpha^6-1)R(alpha) is integral because alpha is an algebraic integer.
This calculation does not imply a nonzero value; the zero branch remains an explicit part of the adopted transfer.

## Strict coefficient energy and signed support intervals

C842 PF3 applies to every nonzero polynomial used here, with its retained full Mahler measure and integrable logarithm conventions.
For a nonmonomial H, the extreme Fourier coefficient of abs(H)^2 is a single nonzero product, so abs(H) is nonconstant on the circle and Jensen/Parseval is strict.
Hence at most four coefficients of magnitude one give M(H)<2, and the only monomial G needed here is monic and has measure one.

For a maximal contiguous support interval [a_i,b_i] of constant sign sigma_i, multiplication by x-1 gives exactly sigma_i(x^(b_i+1)-x^a_i).
Within an interval a_i<b_i+1; between intervals b_i+1<a_(i+1), since at least one zero separates their supports.
All 2r boundary exponents are therefore distinct, even when the first support exponent is positive or the signs of different intervals differ.
The squared coefficient norm is exactly 2r.
The product (x-1)G is nonzero and vanishes at one, so it cannot be a monomial.
Multiplicativity and M(x-1)=1 then give the claimed strict bound M(G)<sqrt(2r), including r=1 and r=2.
No case with a sign change inside a single support interval is covered by this lemma or silently included in its use below.

## Exhaustive degree-zero class

Choosing H in {0,1} congruent to r_0-1 and A=H+1 represents both r_0 possibilities; when r_0=0 the lift c_0=2 is allowed and still gives the coefficient H=1 in G.
The orbit {0} is fixed, so this choice does not force a conflicting lift in another position.
The other three orbit lifts B,C,E independently range over {0,1}, giving all 16 patterns.

With at most four terms, strict coefficient energy applies.
If H=0 and at least five terms occur, support occupies at least five of positions 1,...,6, so there is at most one missing position and at most two positive support intervals.
If H=1 and at least five terms occur, the endpoints 0 and 6 are present and at most two interior positions are absent.
The only admissible two-position omissions are {1,5} or {2,4}; the other possible omission is the singleton {3}.
Combining that singleton with either pair would remove three positions and leave the already excluded small-support branch.
Thus the only three-interval cases are exactly the two paired omissions listed in BP3.
Both have E=1, so replacing E by -1 preserves the actual binary residue and the fixed reflection orbit.

Direct multiplication verifies

    (x^2+x+1)(x^4-x^3+x^2-x+1)
      =x^6+x^4-x^3+x^2+1,
    (x^2+x+1)(x^4-x^2+1)
      =x^6+x^5-x^3+x+1.

The displayed factors are Phi_3, Phi_10 and Phi_12 respectively.
Their roots are roots of unity, as also follows from their usual quotients of x^3-1, x^5+1 and x^6+1; hence each displayed product has measure one.
This checks the claimed exceptional measure bounds without a root-location theorem or a finite scan.
There is no omitted endpoint or support-size case.

## Exhaustive degree-two class

For c_0=c_2=A=1, the constant coefficient is zero and the other six positions have coefficients in {0,1}.
Four or fewer occupied positions use strict coefficient energy; five or six occupied positions have at most one hole and use the positive support-interval bound.
This covers all eight assignments of the other orbit residues in this branch.

For A=0, the chosen lifts give

    G=x^6+B x^5-C x^3-E x^2-C x-1,
    number of terms=2+B+2C+E,

with B,C,E in {0,1} and a compulsory zero at exponent four.
If the number of terms exceeds four, necessarily C=1 and B+E>=1.
This leaves exactly (B,E)=(1,1),(0,1),(1,0).
The first two have the negative interval [0,3] and respectively the positive interval [5,6] or singleton {6}; both meet the signed-interval lemma literally.
The remaining case has the prescribed B=1,C=1,E=0.
Replacing the lift c_1 by -1 leaves its fixed reflection orbit and binary residue unchanged.

Direct multiplication gives

    (x^2+x+1)(x^2-x+1)=x^4+x^2+1,
    (x^4+x^2+1)(x^2-x-1)=x^6-x^5-x^3-x-1.

The first two quadratic factors are Phi_3 and Phi_6.
The last quadratic has roots phi=(1+sqrt(5))/2 and -1/phi, with 1<phi<2, so the full product has Mahler measure phi<2.
All other choices had at most four terms and were already covered independently of their signs.
Thus all 16 degree-two patterns are accounted for, including every A=0 assignment.

## Exhaustive degree-four class and reversal

For A=1 the constant coefficient again vanishes, all remaining coefficients are zero or one, and the same four-term or one-hole split applies to positions 1,...,6.
For A=0, every old degree-two polynomial has constant coefficient -1, so -G_old* is monic of actual degree six and has constant coefficient -1.
Its integral lift is c'_0=0 and c'_j=-c_(6-j) for 1<=j<=5.
In particular c'_4=-c_2=0, as required by c'_0=c'_4.
The other old equalities give c'_1=c'_3, while c'_2 and c'_5 are free; this is exactly the degree-four reflection shape.

Modulo two, the signs disappear.
The residue substitution r_i=r'_(6-i) is inverse to the new substitution and takes each degree-four A=0 orbit assignment to one degree-two A=0 assignment.
It is therefore a bijection of all eight assignments, including the old exceptional lift c_1=-1.
Reversal and multiplication by -1 preserve full Mahler measure.
The displayed golden-ratio example also multiplies correctly:

    (x^4+x^2+1)(x^2+x-1)=x^6+x^5+x^3+x-1.

This example is not needed to extrapolate any other case; the proved bijection supplies every case directly.
Together with the A=1 branch, all 16 degree-four patterns are covered.

## Fixed family, original costs and effective all-degree transfer

The case prescriptions construct a nonempty finite set with at most 48 labels, independent of D and the original coefficient sizes.
Every selected G is monic of degree six, has coefficients in {0,+1,-1}, and has its strict M(G)<2 bound established by the cases above.
Repeated polynomials do not affect the criterion, and no minimal count is needed.

For the original auxiliary, each of the two blocks has at most seven coefficients of magnitude one.
Thus its support is at most 14 and its normalized coefficient length is at most 14/2=7.
Its leading coefficient at exponent D+6 is one and cannot cancel with G*, so F_D is nonzero of degree D+6.
For D>=8, D+6<=7D/4, with equality at D=8.
These costs concern F_D itself; the degree-seven polynomial (x-1)G is used only for the measure bound and is never substituted into the original norm or degree estimate.

The adopted C842 finite-family domain matches the present monic irreducible noncyclotomic unit P, with m=2 and k=6.
Its finite certificate search uses only the fixed family and the strict promises M(G)<2.
In particular no quantitative separation from two or rate of convergence has to be provided by the present proof.
The uniform finiteness needed for the search is supplied by the complete finite list, not by a degree-dependent choice from an infinite family.

The EF proof separates D>B0=max(55,6J) from D<=B0.
Every degree in the first range is at least eight, so the complete reflection construction and ideal identity apply wherever the large-degree proof requires them.
The actual auxiliary degree is T=D+6, and h=T log M(P)/D<=7 log M(P)/4 in this range.
The choices K=14 and S=7 satisfy the actual support and normalized length hypotheses, while C=7/4 may replace the generic C=1+k/2=4 in that inequality.
The same finite frequency bound D>6J, the raw modulus scaling delta_raw=2 delta and B_raw=4B, and the original integral norm remain in force.
The short-annihilator step excludes F_D(alpha)=0 under the small-measure contradiction hypothesis before the nonzero norm is used.
No nonzero norm is assigned to an unchecked zero value.

For D<=B0, C842 EF6's accepted C394 input supplies a positive rational v_low below a height floor for every nontorsion unit in that bounded degree range, without a periodic-residue hypothesis.
Since log M(P)=D times absolute height, it also supplies the needed lower bound for the original total logarithmic measure.
This completes degrees 2,4,6 and every other degree at most B0 without assuming a nonexistent full reflection pattern at the small degrees.
The finite algorithmic output g=(1/2)min(u/C,v_low) is positive rational and yields the strict inequality log M(P)>g in both ranges.
Thus the initial D>=8 restriction has been fully discharged at the theorem's stated all-degree scope.

Taking the minimum with the adopted C842 binary bound through period five gives the asserted bound through period six.
The period-six construction includes periods dividing six, while the finite union with C842 supplies periods four and five as well; no divisibility implication between all periods one through six is assumed.
This finite union makes no arbitrary-period or modulus-uniform assertion.

## Dependency, source and verification limits

C842's adopted finite-family theorem, effective proof and strict energy lemma are resolved inputs at their exact accepted scope.
Its R1062 relationship and binding declarations match those interfaces; this review does not recursively re-audit C842, C137, C92, C394 or the original external sources.
The present deduction has no cycle through C843, the mutable D44, or a not-yet-run computation.
D44 is extraction provenance only and was not consulted.

The named analytic inputs retain C842's recorded Jensen, total Mahler, integrable-circle-zero and accepted-source boundaries.
The new polynomial products, root-of-unity factors and quadratic roots are direct finite algebraic checks, not new uses of an unverified root-classification result.
The general-coefficient historical attribution lead already marked unverified in C842 remains unverified; it supplies no premise for these period-six templates.
No novelty or priority search is asserted, and no existing source's original proof-inspection depth is enlarged.
No new source-attribution gap or unresolved mathematical dependency was found in this deduction.

The verification was a whole symbolic proof inspection, with explicit case exhaustion, multiplication and interface calculations as recorded above.
No native enumeration, root computation, numerical certificate, Fourier calculation or numerical value of the gap was executed.
Computability is a theorem inherited through the checked effective interface; neither practical complexity nor a usable numerical magnitude has been verified.
The unrestricted Lehmer Task remains outside this special-class conclusion.

## Whole binary period-six finding

PASS: no mathematical gap was found in the entire fixed C843 statement and BP1--BP6 argument at the stated adopted-input and source-inspection scope.
The complete binary period-six template theorem, strict M(G)<2 bounds, original auxiliary costs, algorithmically computable positive rational total-Mahler gap and finite-union corollary through period six are supported.
This is an independent whole-proof finding for the inspected fixed version, with the accepted C842 theorem reused at its actual scope.
It gives no ternary period-six theorem, arbitrary-period theorem, modulus-uniform bound, near-one construction, unrestricted Lehmer conclusion, numerical algorithm execution or new source-proof certification.
Responsible adoption remains a separate Claim decision.
