---
author: Yin
---

# Retained project review: Negative-unit stabilization, rank-three descent and exact companion costs

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0312_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="negative-line-complete-independent-review"></a>

### Complete independent review of the negative-line classification and full costs

Date: 2026-10-10T09:21.
Human record author: Yin.
Reviewer: structural_research, separately assigned by the coordinating AI.
This is a whole-proof noncontributor review of the final D179 Sections1--7, equations(1)--(17), and the retained author correction at #negative-line-block-scope-correction.
The first inspected author revision was the 20242-byte freeze of2026-10-10T09:12; the final checked revision is the21643-byte author refreeze of2026-10-10T09:18.
The reviewer read the complete text directly, reconstructed all substantive obligations below, followed the actually used fixed interfaces, and inspected the selected canonical FKMR16 source passages.
This is not a review of a summary or only selected algebra.

The review is nonblind: the assignment supplied the claimed scope, the shared task context contains prior structural work, and the author supplied its refreeze/correction account.
The reviewer contributed none of the author's primitive-kernel classification, negative-line construction, orbit descent or cost optimum.
Its earlier authorship of D9's signed-cover interface and earlier complete review of L262's relaxed full-entry lift are disclosed upstream roles.
These interfaces were checked again at their actual invocation, not treated as newly independent work on those old results.
The small four-cycle countercontrol below was derived during this review to diagnose a scope objection; it is not part of the author's original theorem or a hidden premise of the accepted classification.
Root independently reported the same scope concern after this reviewer had identified it and sent the author its finding.
No contribution to the current descent or construction was supplied by root's observation.

**Final finding.**
The complete corrected proof passes at its stated scope, with no remaining mathematical defect or unresolved proof input.
One substantive applicability overstatement was found and repaired before this finding: the first revision extended a block-bipartite formula to arbitrary bipartite support orderings.
The author withdrew that extension and retained the correction.
The main rank-three classification, integer congruence, unrestricted rank-three fixed-scalar optimum and distinction between proper and relaxed cover costs are unchanged and verified.
This finding does not establish higher-rank universal scalar coverage, sufficiency for every binary form of content4, or G0001 completion.

#### Obligations and the resolved scope objection

The obligations were: the complete rank-three pencil and primitive integer kernel; all sign/zero cases in reducing to the positive integer equation; termination and completeness of its unrestricted Vieta orbit classification; an integral two-sided orthogonal split with no index loss; transfer of primitive norm and alternating content; the actual displayed unimodular change of basis and minimal-degree claim; exact applicability of the block formula; all original, absolute and literal-cover factors; the optimum across EVERY proper rank-three realization of the fixed full polynomial; the distinct full-entry nonproper operation; and attribution/source boundaries.
Each is addressed below.

In the first frozen Section5, the inference from L191 to "no bipartite proper matrix" at any rank exceeded that premise.
L191's determinant formula is for the ordered block form [[I_r,C],[0,I_s]], not for all interleavings of a bipartite undirected support.
The distinction is material.
For the actual proper matrix with strict-upper entries V12=V23=V34=3 and V14=-3, all others zero, the support is a four-cycle and hence bipartite.
Put s=t+1.
Direct determinant expansion by the matchings and two oriented full cycles gives

    p_V=s^4-36t s^2+162t^2+81(t^3+t)
       =t^4+49t^3+96t^2+49t+1
       =(t+1)^2(t^2+47t+1).

Thus arbitrary ordered bipartite support can have negative off-circle roots.
This countercontrol invalidates the proposed general reason; it is not an assertion that the particular factor t^2+18t+1 is realized in that broader class.

The final Section5 now explicitly imposes [[I_r,C],[0,I_s]], arbitrary integral rectangular C, and says it does not cover arbitrary support orderings.
Orthogonal singular-value changes used only to evaluate this actual matrix give paired factors t^2+(2-sigma_j^2)t+1 and exactly |r-s| unpaired factors t+1; zero singular values retain both of their neutral roots.
Hence every reciprocal trace is sigma_j^2-2>=-2.
The trace -18 of Q_- is impossible in this exact class, at any rank and irrespective of extra neutral factors.
This is the corrected claim.
The author also aligned the reuse/self-check labels and retained the initial overstatement and withdrawal in its dated correction.
All three changed locations and that correction were reread.
No repair to the other arguments was required.

#### Full rank-three identity and all-integer descent, Sections2--3

Expanding det(tV+V^T) gives coefficients1,3-E+abc,3-E+abc,1.
Factoring t+1 therefore proves(1), with the entire neutral factor present.
For a nonzero triple the3-by-3 alternating matrix has rank2, and multiplication gives its rational kernel (c,-b,a).
Division by g makes the generator primitive, so every integral vector on that line is an integer multiple of it.
Its quadratic value is (a^2+b^2+c^2-abc)/g^2.
The all-zero case is the positive identity, with no negative vector and a different kernel rank; it is explicitly excluded rather than passed through division by g.

Primitive norm minus one forces abc=E+g^2>0.
None of the entries can vanish.
A diagonal sign congruence first makes a and b positive, and positivity of the invariant triple product makes c positive too.
It preserves g, p_V and all entry magnitudes.
Substitution of the positive magnitudes gX,gY,gZ proves exactly(3), including gcd1.
Conversely that gcd and equation suffice for primitive norm minus one; no condition was inferred merely from the scalar pencil.

All four parity counts in Lemma1 check.
With zero or one odd coordinate the right side is divisible by4 while the left side is1 or2 modulo4; with two odd coordinates it is even while the left side is3.
Thus all coordinates are odd and g is a positive multiple of4.
The other root gXY-Z equals (X^2+Y^2+1)/Z, proving both its integrality and strict positivity.
Replacing a maximal coordinate above the vertex strictly decreases the positive integer height; sorting after each step does not change the equation or g.
Therefore the process stops with X<=Y<=Z<=gXY/2.
The quadratic is decreasing on the whole interval containing Y and Z, so its value at Y is nonnegative.
For X>=2, gX-2>=6 and Y>=X make that value at most1-5X^2<0.
For X=1 the inequality2-(g-2)Y^2>=0 forces g=4,Y=1.
The two possible last roots1 and3 are resolved by the terminal bound Z<=2.

These arguments cover arbitrary positive coordinates and arbitrary positive g, not a finite search.
Every step is an involution, and the positive-other-root identity remains valid at each generated solution.
Reversing a terminating descent proves completeness of the orbit from(1,1,1).
The gcd is invariant under the replacement and a permutation; oddness is preserved because4XY-Z is odd.
The base is primitive, so every positive solution automatically is.
Substituting into D gives D=-16 and g=4, proving BOTH directions of Theorem2 and the full polynomial F.
The theorem does not claim that the scalar polynomial alone determines the primitive kernel norm.

#### Integral splitting, binary exclusions and the actual congruence, Sections4--5

For v in the alternating kernel, G(v,x)=G(x,v).
With G(v,v)=-1, the displayed x_perp=x+G(x,v)v annihilates both cross pairings and stays integral.
The linear functional G(.,v) takes the unit value -1 at v, so its kernel and Zv form a direct integral decomposition.
This verifies existence of an integer basis of the complement and absence of any finite-index factor.
In determinant-one rank3 the complementary determinant is -1.
The converse has the indicated kernel equality exactly when the complement's alternating form is nondegenerate.

For binary B with det B=-1 and s!=t, its alternating block is nondegenerate and the stabilized primitive kernel is precisely the negative line.
Under a unimodular congruence, all new alternating entries are integer combinations of old ones and vice versa, so their positive gcd is invariant.
Theorem2 therefore forces |s-t|=4 for any proper presentation, independently of the size of the new basis entries.
Direct expansion gives leading and constant coefficient ru-st=-1 and middle coefficient2ru-s^2-t^2=-(s-t)^2-2, exactly(9).
The negative line contributes -(t+1); the two minus signs cancel in the stabilized full polynomial.
When s=t, the entire form is symmetric with a negative vector, while a symmetric proper upper-unitriangular matrix must be I.
This proves the separate zero-content exclusion.
Necessity is not promoted to sufficiency for all content4 binary congruence classes.

For B0 the determinant is20-21=-1, its integer quadratic values are even, and det(B0+B0^T)=80-100=-20.
Thus its lack of norm-one vectors is an actual even indefinite phenomenon.
Multiplication of the two displayed Q matrices in either order gives I.
Their determinant is1.
With v=(1,-1,1), the actual V0 pairing functional on the first two coordinate vectors is1 and3, and the last two columns of Q are precisely their projections.
The four complementary pairings are2,7,3,10; v has norm-1 and both cross rows vanish.
This proves every entry of Q^T V0 Q=G0 and the inverse congruence, without a rational basis or a dropped diagonal sign.

A rank2 proper matrix has polynomial t^2+(2-h^2)t+1, which cannot equal Q_-.
Degree therefore requires at least one additional vertex if only a neutral multiplier is allowed, and V0 attains that bound.
Every reciprocal odd-degree proper polynomial has the factor t+1; because Q_- has no root-1, a degree-one neutral multiplier must be that factor.
This is a fixed-target degree statement, not a coverage theorem.
The two roots -9+/-4sqrt5 are negative reciprocal roots, one outside the circle, giving the stated positive measure.
The block-bipartite comparison has exactly the corrected scope established above.

#### Complete proper and relaxed costs, Section6

For the classified orbit, X^2+Y^2+Z^2=4XYZ-1 gives E=16(4P-1).
Replacing the three strict upper entries by negative magnitudes changes the triple product from64P to-64P.
Substitution in the full rank-three identity gives precisely(t+1)[t^2-(128P-18)t+1].
D9's literal cover uses diagonal I2 and two copies of each strict-upper squared entry; simultaneous sheet splitting of W and W^T gives the full product(14), without division by2 or by rank.
Consequently rank6, height4max(X,Y,Z), energy32(4P-1), and all three measures(15) are correct.
At P=1, the original and companion reciprocal traces have magnitudes18 and110; the latter expanding root is55+12sqrt21.
Heights4 and energies48/96 are exact.

For every proper rank3 presentation of F, not just the primitive-norm subclass, (1) forces u=abc=E+16>16.
AM--GM gives u-16>=3u^(2/3).
For y=u^(1/3)>2 the exact factorization y^3-3y^2-16=(y-4)(y^2+y+4), whose second factor is positive, forces u>=64.
Equality requires equal a^2,b^2,c^2 and u=64, hence all magnitudes4.
The absolute triple product is -u and the companion trace is2u-18>=110.
Monotonicity of ell on(2,infinity) gives the complete attained companion and cover minima.
If every entry magnitude were at most3, E<=27, contradicting E>=48; the seed therefore also attains the minimum height4.
No higher-rank optimum or ratio for varying targets follows.

The nonproper matrices have full squared-entry sums162 and163, rather than proper strict-upper energies.
Their negative-magnitude matrices are -B0 and [-1] direct-sum(-B0), so their complete pencils remain -Q_- and F.
I checked the full-entry lift directly: for each ordered entry x, equal sheet coordinates see -|x| and opposite sheet coordinates see x, including diagonal and lower entries.
The same decomposition applies to the transpose.
Thus the lifts have polynomials Q_-^2 and F^2, ranks4 and6, and squared-entry sums324 and326.
They retain nonunit diagonals/lower entries and are not D9's proper covers.
The relaxed measure2ell(18) is consequently consistent with the strictly larger attained proper rank3 minimum.
All leading signs, neutral factors and dimensions remain paid.

#### Actual dependency, source and execution scope

The reviewer read the applicable D9 signed-cover definition and proof, L191's ordered block determinant and singular-value scope, L207's direct rank-three pencil interface, L214's primitive alternating-kernel and integral splitting interface, L262's full-entry relaxed splitting, and L307's positive-half/positive-padding boundaries.
These are used only in their stated roles; the new proof reconstructs its necessary rank-three algebra and negative-line split.
Prior finite searches, the E8 comparison and the attained Lehmer benchmark provide context or scale comparisons, not hidden existence assumptions.
No proof of a general Coxeter or exceptional-lattice classification is imported.

For source attribution I directly extracted and read the retained canonical FKMR16 arXiv1504.04321v1 PDF title page and printed pp.2--4,7--10,15--16 with the installed pdftotext.
The title/author/version identification, equation(2.1) with nonnegative k, the added-one-coordinate embedding, Theorem2.7's statement, and the separate k=0 domain of Section3 all match the source record.
I read the complete displayed proofs of Lemma3.4, Theorem3.5 and Lemma3.7 in their stated domains.
These verify attribution of height/Vieta and quadratic-comparison methods.
Theorem2.7 cites reference[32], whose original proof I did not inspect; nor did I inspect the journal edition, prove edition equivalence or audit the whole source.
Its four-coordinate action does not by itself supply the needed fixed-three-coordinate orbit.
The local complete parity/descent argument supplies that result instead.
Section4 assumes positive e, so it is not an imported theorem for the negative constant here.
No external theorem remains as an unverified premise, and no priority or novelty claim is certified.

The first attempted text extraction through the repository Python failed before reading because pypdf is not installed in that environment.
The subsequent installed pdftotext reads of all declared pages succeeded.
This is an explicitly retained operational source-reading failure, not a failed mathematical certificate.
No mathematical program, numeric approximation, finite enumeration, new J, source record mutation or author proof edit was performed by this reviewer.
The four-cycle check above and every proof obligation were algebraic/manual checks.
Formal verification and a full-source audit are not claimed.

The final21643-byte author prefix, including its correction history, was preserved byte-for-byte by appending this review.
The complete finding covers the corrected argument and its actual dependencies, while preserving the original objection and its resolved disposition.
Fixed adoption and any Task decision remain the coordinator's separate actions; all broader coverage and near-one questions remain open.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete negative-line review](#negative-line-complete-independent-review) | [Primitive kernel and complete descent](../../ledger/Yin_L_G0312_v1.md#rank-three-negative-kernel-equation) | Entire Sections2--3, equations1--7, zero/sign cases and unrestricted positive-integer orbit classification. |
| [Complete negative-line review](#negative-line-complete-independent-review) | [Integral split and actual realization](../../ledger/Yin_L_G0312_v1.md#negative-line-orthogonal-split) | Entire Sections4--5, equations8--12, binary necessary conditions, actual unimodular congruence, fixed-target minimal degree and corrected block-bipartite scope. |
| [Complete negative-line review](#negative-line-complete-independent-review) | [Complete costs and optimum](../../ledger/Yin_L_G0312_v1.md#negative-line-complete-companion-optimum) | Entire Sections6--7, equations13--17, all proper rank3 same-polynomial optima, complete relaxed/proper costs and stated limits. |
| [Complete negative-line review](#negative-line-complete-independent-review) | [Reuse and source scope](../../ledger/Yin_L_G0312_v1.md#negative-line-stabilization-reuse) | Whole Section1 and all actually consumed fixed/source interfaces as enumerated in the finding; no uninspected source-wide theorem accepted. |
| [Complete negative-line review](#negative-line-complete-independent-review) | [Scope correction](../../ledger/Yin_L_G0312_v1.md#negative-line-block-scope-correction) | Initial excessive bipartite inference withdrawn, final exact block-form claim and all affected labels checked. |
| [Original complete author SELF](#original-negative-line-author-self) | [Original L312 proof](../../ledger/Yin_L_G0312_v1.md#complete-retained-proof-and-review) | Complete original author checking/contribution/no-program account with all actual source and scope limits, retaining the original correction boundaries and no invented separate act minute; not later C618. |


## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete negative-line review](#negative-line-complete-independent-review) | independently reviewed |
| [Original complete author SELF](#original-negative-line-author-self) | self-reviewed |


<a id="original-negative-line-author-self"></a>
## Original complete author SELF account

This full original author account retains its actual original L312 proof/source/correction/no-program input, not the later C618.
No separate exact author-check minute is fabricated from a later reviewer or maintenance act.

The author checked the full pencil expansion, primitive rather than rational kernel, diagonal sign reduction, all parity cases, positivity and strict termination in the Vieta descent, the exact terminal equality case, integer two-sided orthogonal splitting, congruence invariance of alternating content, both determinant signs in(9), all entries and inverses in(11)--(12), both negative reciprocal roots and the rank-two/block-bipartite exclusions, all neutral factors and the full literal-cover product, the unrestricted rank-three AM--GM optimum, and the difference between full-entry relaxed and proper absolute operations.
No program, numerical spectrum, finite experiment, unrecorded execution failure or new J was used.
Source attribution is distinct from the local proof and is completed in Section1 and the linked FKMR16 source record.
A source-text printing attempt initially failed only because the shell's default output encoding could not encode a mathematical minus sign; repeating that read with UTF-8 succeeded.
This was not a mathematical execution or failed certificate.
Root supplied no derivation.
The whole author argument awaits separately organized noncontributor review and fixed adoption; G0001 and all parallel routes remain active and unresolved.
