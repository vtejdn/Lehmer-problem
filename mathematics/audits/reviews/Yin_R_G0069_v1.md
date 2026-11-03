---
author: Yin
---

# Retained project review: An infinite original-digit return core for the original Lehmer Salem unit

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0170_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

## Independent review of the original Lehmer joint neutral descent

Assigned AI resultant_research for Yin, 2026-10-09.
The coordinator requested independent review of D G0017 and J G0022.
The reviewer did not derive the eight-dimensional block construction or write its discovery or verifier.
Shared G0001 conversation context and the author's frozen text are available; this is not blind or human review.

### Scope

Review the complete partial-descent proof, exact input/domain argument, original digit/word convention, full joint geometry, outward interval verifier and reproducible finite output.
Preserve author outputs.
Do not infer compact termination, an infinite actual Lehmer core, uniform law bounds or a Mahler gap.

<a id="lehmer-joint-descent-review"></a>

### Finding: no defect in the stated partial theorem

At 2026-10-09T15:51 the separately assigned reviewer completed the full mathematical review of [D G0017](../../ledger/Yin_L_G0170_v1.md#lehmer-joint-neutral-descent), Sections 1--5, and the complete [J G0022 verifier](../../computations/programs/Yin_J_G0022/verify.py), with the retained integer words in reused-cover.json.
No mathematical defect was found within the stated partial-descent scope.
The exact conclusion reviewed is the original-digit descent, for actual x in Z[beta] with |x_+|<=1, |x_-|<=S and rho>=1500, to an endpoint in the same narrow real domain with squared neutral norm reduced by at least 5589/1000; all intermediate states obey the broader real strips, and iteration reaches the finite residue K_L.

This is a separately organized local exploratory review.
It does not itself create a fixed R/L result, adopt a Claim assessment or complete G0001.
The reviewer read the frozen proof, full discovery/reuse/verifier programs, their README and saved exact output.
It also read D G0013's prior quartic proof and review descriptions, including the later corollaries, for the method interface; no prior conclusion was used as a substitute for checking D G0017's new eight-dimensional geometry.
Shared G0001 context and earlier coordination were available, but the reviewer did not supply D G0017's construction, simplex table or derivation.
The root assigned this review after those materials were frozen.
This is neither blind review, independent human refereeing nor formal verification.

### Input, embedding and digit checks

The complete trace identity P(t)=t^5Q(t+t^(-1)) was checked in the written proof and integer verifier.
The encoded polynomial modulo two is u^5+u^4+u^3+u^2+1.
The verifier's five Frobenius squarings check Q divides u^32-u; its constant and parity tests exclude roots zero and one.
Because five is prime, every factor degree in the squarefree Frobenius product is either one or five, so these tests force irreducibility.
The reviewer followed the exact finite-field and trace-extension interfaces in [L G0004, Section 9](../../ledger/Yin_L_G0004_v1.md).

Each of the five rational brackets has a strict sign change, and they are disjoint.
A quintic with those five distinct real roots has no unaccounted roots or repeated roots.
The four interior trace roots yield four conjugate unit-circle pairs; the remaining trace root yields beta>1 and beta^(-1).
In the field Q(u), a square cannot become negative under a real embedding, so an interior trace root proves u^2-4 is not a square.
The quadratic extension has degree ten, which proves irreducibility of P, including the exterior-root embedding used for x_+.
This is not an inference from numerical discovery roots.

For an original word eta_1,...,eta_k, direct expansion of x->beta*x+eta gives endpoint beta^k x+sum eta_i beta^(k-i).
At every unit root the same word becomes zeta_j^k(z_j+sum eta_i zeta_j^(-i)).
The order of digits and inverse powers in the verifier are correct.
Conjugation equals inversion because the certified zeta_j lies exactly on the unit circle.
The fact that its numerical enclosure is a rectangle does not alter this identity for the underlying root.
All four pairs are retained with the stated coordinate order, and rho^2 is exactly the ordinary Euclidean norm squared of that eight-vector; no extra factor of two is needed.

The independent implementation in [J G0023](../../computations/programs/Yin_J_G0023/readme.md) additionally checks P's irreducibility by exact factorization and independently isolates all trace roots in rational intervals.
It forms displacements by first computing the forward endpoint translation and then dividing by zeta_j^k, providing a different implementation of the word convention.

### Joint geometry and interval arithmetic

The author's interval addition, negation, multiplication, division, squaring and integer-square-root routines all enclose the indicated exact operations.
Division checks separation from zero.
The grid rounding is outward, including negative numbers.
In sqrt_interval, floor followed by integer square root gives a valid lower bound, and incrementing the upper square root gives a strict or weak valid upper enclosure.
Exact rational operations outside the grid also preserve enclosure.

The augmented matrix has the nine joint vertices as columns with a final row of ones.
Interval Gauss--Jordan elimination has a valid exact-matrix interpretation: earlier pivot columns are identity columns, row swaps occur only among remaining rows, every pivot excludes zero, and setting an eliminated entry to zero or a normalized pivot to one uses an exact algebraic identity for the underlying matrix.
Thus the returned rows enclose its inverse and the actual affine barycentric functions.
Positive lower intercepts place zero strictly inside the full eight-dimensional simplex, while b_i(lower)/||g_i||(upper) is a valid lower distance to every facet.
The coefficient errors and root dependencies may widen those intervals but cannot invalidate containment.

Consequently the ball of the certified radius about zero is in the simplex.
For every joint z, its point in direction -z supplies a convex combination with inner product -r||z||; at least one retained vertex therefore has no greater inner product.
The selected word's coordinatewise rotation preserves the full norm even though different vertices can have different word lengths.
Combining that vertex with its complete squared-norm upper bound proves the stated descent.
No pairwise projection or separate choice of a word for each conjugate is used.

The reviewer reran the original exact verifier with only input/output path routing, producing a separate source-verification.json (`mathematics/computations/outputs/Yin_J_G0023/source-verification.json`).
Every mathematical output field matched the author's verification.json, including 50 cells, 450 word uses, 17 distinct simplices, threshold 1500 and lower drop 5589/1000.
The rerun left the author's file unchanged; this is an output-preservation check.

The reviewer also wrote a distinct [checker](../../computations/programs/Yin_J_G0023/verify.py).
It uses exact SymPy real-root isolation and 300-bit Arb enclosures, forms an 8 by 8 edge matrix based at one vertex instead of the author's augmented 9 by 9 matrix, and reconstructs the ninth barycentric coordinate as one minus the other eight.
All 17 simplex ball/margin checks passed.
This independently authored geometry implementation reuses the retained integer words, not the author's interval routines, root approximations, inverse matrices or saved geometry.
It also checked all 450 complete closed expanding-cell images and every intermediate expanding-strip bound.
Independent output (`mathematics/computations/outputs/Yin_J_G0023/independent-verification.json`) retains the precision, root brackets and individual cell margin enclosures.
Both commands ran under Python 3.12.14 on 2026-10-09; the author's original Python 3.13.15 metadata was preserved.

### Real strips, extension of the cells and termination scope

The fifty closed cells cover [1/2,1], including all shared endpoints.
Every chosen word works for the entire closed cell, so selecting a vertex according to the joint neutral direction does not compromise expanding-coordinate legality.
Reflection x->-x and negation of every digit transfer the conclusion to [-1,-1/2].

For 0<|x_+|<1/2, the first zero-prefix crossing lies in [1/2,beta/2), which is inside [1/2,1].
Each prefix is finite, preserves the neutral norm and contracts the other real coordinate.
Since the actual field embedding is injective, x_+=0 forces x=0 and cannot occur above the neutral threshold.
A uniform bound on the number of prefixed zeros is not needed for this partial theorem and is not asserted by it.

The contracting strip is invariant at every digit because beta^(-1)S+1=S.
For an intermediate state with r remaining digits, the final strict |x'_+|<1 gives

    |x_+|<beta^(-r)+(1-beta^(-r))/(beta-1)<B

when r>0, since B>1; the endpoint also lies strictly inside B.
The zero-prefix states have magnitude below one.
Thus the broader expanding strip holds throughout, even though the narrow strip is required only at block endpoints.
The independent finite checks of every retained prefix agree with this general backward argument.

Each block executed outside K_L reduces the nonnegative squared neutral norm by a fixed strictly positive amount.
A descent sequence cannot execute infinitely many such blocks, and every individual prefix/word is finite.
When the threshold is crossed, the endpoint has rho<1500 with both real coordinates still bounded.
Irreducibility and distinct embeddings make the image of the free rank-ten module Z[beta] a full lattice in R^2 x C^4.
A bounded set in those ten real coordinates contains only finitely many lattice points, so K_L is finite.

No step supplies a path from every point of K_L to zero, and the proof explicitly does not claim one.
The review did not enumerate K_L, search longer words, rerun the numerical optimizer, test optimizer optimality, review the full Mercat source proof, establish reachability from zero, prove an infinite actual Lehmer core, or obtain a weighted-law or uniform near-one estimate.
These are limitations of the claimed result, not defects in this partial theorem.
No correction to the mathematical proof or certificate was requested before this finding was recorded.

The retained quartic method material is the [fixed quartic descent](../../ledger/Yin_L_G0169_v1.md#quartic-neutral-descent) and the [compact certificate](../../ledger/Yin_L_G0169_v1.md#quartic-compact-termination).
This review does not cover the full quartic-retention argument; the earlier D G0013/D G0014 names above describe the historical context actually read by this reviewer.

<a id="preserved-d0023"></a>

**Preserved original dated D G0023 review history.**
The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Independent review of normalized radius-eight Lehmer descent

Assigned AI resultant_research for Yin, 2026-10-09.
This separately requested full review targets frozen D G0020/J G0024 and their original Lehmer domain.
The reviewer did not derive the normalized construction, choose its blocks or write its verifier.
Shared context includes the coordinator's summary of its contribution to the normalized linear-functional implication and positive-denominator/additive-drop guards; that is disclosed rather than treated as blind independence.

<a id="normalized-lehmer-radius-eight-review"></a>

### Finding: no defect in the normalized partial-descent theorem

At 2026-10-09T15:59 the separately assigned reviewer completed the full review of [D G0020](../../ledger/Yin_L_G0170_v1.md#normalized-lehmer-radius-eight), Sections 1--5, and [J G0024](../../computations/programs/Yin_J_G0024/readme.md)'s complete discovery/verifier programs, retained integer-word table and exact result.
No mathematical defect was found at the stated scope.
The checked conclusion is original-digit descent on the actual Lehmer field from |x_+|<=1, |x_-|<=S and rho>=8 to a new narrow-domain endpoint whose squared neutral norm falls by at least 57/100, with both real strips respected throughout, followed by finite reduction to K_8.

This is a new local exploratory review of the new normalized body, not an automatic transfer of the preceding simplex review.
Its exact original-field, interval-primitive and strip interfaces were read and checked again against the earlier [D G0019 finding](#lehmer-joint-descent-review), which this same independently assigned reviewer had completed before this assignment.
The root reported having contributed the normalized linear-functional implication and positive-denominator/uniform-drop guards, and having performed its own contributor-aware local checks.
Those summaries were available before this review; their conclusions were not used in place of the checks below.
The reviewer did not contribute to the new proof, numerical search, target selection or certificate.
This is not blind review, human refereeing, formal verification or a fixed Claim/Task adoption.

### Normalization, joint convexity and uniform additive gain

For every actual saved word, the full eight-vector c has squared norm m_w>0 and normalized vector u=c/m_w.
The coordinatewise endpoint rotations may depend on word length, but each preserves the entire Euclidean norm.
Thus

    ||z+c||^2-||z||^2=m_w(1+2 z.u)

is the correct change for each particular word.
The denominator is the sum of all eight real-coordinate squares, not a projected-pair norm or a coordinate-dependent rescaling.

Within each fixed expanding cell, all retained words are legal for every point in that closed cell.
All sixteen signed axis targets lie in the convex hull of the union of that cell's normalized vertices.
Different targets may use different nine-word simplices; this does not weaken their membership in the same union hull.
Their hull contains {y:||y||_1<=t}, and Cauchy--Schwarz gives ||y||_1<=sqrt(8)||y||_2.
The Euclidean ball of radius r=t/sqrt(8) is therefore contained in that full eight-dimensional hull.
No independently chosen words for separate root pairs are combined.

For every nonzero z, the point -r z/||z|| is a convex combination of retained vertices.
Applying the linear functional z dot y to that combination shows that at least one actual retained u_w satisfies z.u_w<=-r||z||.
If rho=||z||>=8 and 16r-1>0, its own original displacement then satisfies

    ||z+c_w||^2-||z||^2
       <=-m_w(2r rho-1)
       <=-m_min(16r-1).

The direction of the inequality using m_w>=m_min is correct because the preceding factor is strictly positive.
This is the needed additive, uniform decrease; merely knowing strict directional descent or m_w>0 separately would not give it.
The exact certificate supplies the minimum across every retained word for each cell, so it covers whichever word the support-functional argument selects.

### Exact axis certificates and reproduction

The verifier reuses the unchanged, already inspected J G0022 exact primitives.
Its trace identity, degree-five finite-field test, disjoint rational root isolation, unit-root construction, complex multiplication and interval Gauss--Jordan proof have the same domain as the reviewed D G0017 input.
The new code recomputes every c from its integer word and every norm denominator as an outward interval of the complete sum of squares.
Every denominator lower endpoint is positive before division.

The new augmented 9 by 9 matrices have normalized vertices as columns and a final row of ones.
The exact inverse interpretation established for the interval elimination therefore supplies the actual barycentric solution at each rational axis point.
Each solution has strictly positive enclosed coordinates; its sum is exactly one for the underlying actual solution because the last row of the matrix is ones.
No saved numerical LP weight, approximate radial optimum, or root approximation is a premise.
The tuple check covers exactly all sixteen signed axes for each of the two cells, and the inherited block checks enforce original integer digits and length at most eleven.

The separate [J G0027](../../computations/programs/Yin_J_G0027/readme.md) ran the source verifier with only its output destination routed into the review group.
Every mathematical field matched the author's result: two cells, 32 axis targets, 288 word uses, 217 distinct words, maximum length eleven, radius threshold eight, and uniform lower drop 57/100.
The author's verification.json was checked unchanged.
The reviewer rerun used Python 3.12.14; the original Python 3.13.15 metadata remains in the author output.
Source rerun output (`mathematics/computations/outputs/Yin_J_G0027/source-verification.json`) records the actual reviewer environment.

The reviewer also separately implemented the normalized geometry in J G0027.
It reused only its own J G0023 functions for exact root isolation and forward-endpoint displacement evaluation, not author interval primitives or geometry.
At 300-bit precision with root intervals of width at most 2^(-240), it recalculated each positive norm denominator, solved an 8 by 8 edge system at each rational axis point, and obtained the base barycentric coordinate by subtracting the other eight from one.
All 32 strict-positivity tests passed.
It checked all 288 words over their complete closed cells, including every intermediate expanding-strip bound, and independently recovered lower bounds at least as strong as both reported cell-specific norm, weight and drop bounds.

The independent interval drops are approximately 0.5707382335... and 0.5971013309..., with propagated error enclosures retained in independent-verification.json (`mathematics/computations/outputs/Yin_J_G0027/independent-verification.json`).
Those are summaries of certified intervals, not the source of a rounded floating-point proof.
In particular they validate the stated rational bounds 57/100 and 597/1000.
The radius, denominator and minimum-cost computations all concern the same cell-specific collection of normalized vectors.

### Complete actual domain and finite iteration

The cells [1/2,3/4] and [3/4,1] cover the positive annulus, including the shared endpoint.
The full-cell legality checks ensure that the word chosen according to the current joint neutral direction remains legal for its actual expanding coordinate.
Negating the state and all digits gives the negative annulus with exactly the same norm bounds.

For 0<|x_+|<1/2, the first zero-prefix crossing belongs to [1/2,beta/2), hence remains below one.
It is finite for each nonzero actual state; the field embedding x->x_+ is injective, so x_+=0 would force x=0 and rho=0, outside this descent case.
The prefix rotates all neutral coordinates without changing their complete norm and contracts the other real coordinate.
The subsequent normalized body works for every joint direction, including the rotated one.

The contracting strip follows digit by digit from beta^(-1)S+1=S.
The broader expanding strip follows backward from the strict narrow endpoint and beta>1 with B=1/(beta-1)>1, exactly as rechecked in D G0019; the independent code also checked every retained intermediate prefix over the complete input cells.
The narrow endpoint domain is preserved for repetition.
A fixed drop of 57/100 in a nonnegative squared norm allows only finitely many blocks before rho<8; each zero prefix and word is finite individually.
The full rank-ten embedding lattice and the two real bounds make K_8 finite.

This proof does not need, and does not give, a state-independent bound on the number of prefixed zero digits.
Existence of the selected direction-dependent word does not identify its probability under the original law.
Neither the author certificate nor the independent check enumerates K_8, proves every residual state returns to zero, proves original reachability for an infinite set, or establishes an infinite actual Lehmer core.
No weighted-law or uniform near-one conclusion is supported.
The numerical optimizer was inspected but not rerun, and no optimality or completeness of its search is claimed.
No mathematical correction was requested before recording this finding.

<a id="preserved-d0024"></a>

**Preserved original dated D G0024 review history.**
The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Independent completeness review of the Lehmer radius-eight enumeration

Assigned AI resultant_research for Yin, 2026-10-10.
Root requested an independent full completeness review of frozen enumeration artifacts in D G0022/J G0026.
The reviewer did not derive or implement this enumeration.
Shared context includes the root's conceptual ellipsoid/LDL suggestion and preliminary reading, so this is not blind review.
Later path-search artifacts are outside the initial review scope.

<a id="lehmer-compact-enumeration-review"></a>

### Finding: the original finite superset is complete

At 2026-10-09T16:07 the separately assigned reviewer completed the proof/code review and final independent reproduction of [D G0022, Sections 1--4](../../ledger/Yin_L_G0170_v1.md#lehmer-compact-complete-enumeration) and the frozen enumeration files in [J G0026](../../computations/programs/Yin_J_G0026/readme.md).
No mathematical defect was found in the assertion that compact-states.bin contains every actual point of K_8, with 797507 distinct retained states.
The conclusion is a complete finite superset, not exact membership of every retained state.

The checked author files are estimate.py/estimate.json, prepare.py/enumeration-certificate.json, Enumerate.cs/run.ps1, compact-states.bin/enumeration.json, verify_certificate.py/certificate-verification.json and their enumeration README, together with the unchanged J G0022 root/interval primitives.
The full written Sections 1--4 were read after the author declared them frozen.
Later path-search files and Sections 5--6 are explicitly outside this finding.
The reviewer received a summary of their progress but did not use a path result to justify completeness.

This is a separately organized local review by a noncontributor to the enumeration.
The root's conceptual ellipsoid/LDL suggestion, preliminary read and no-issue report were disclosed in shared context before final findings; they do not replace the review below.
The reviewer had separately checked the original field and descent domain in D G0019/G0023, and reused only its own previously written exact-root helper for the new computational check.
This review is neither blind, human refereeing nor formal verification, and does not itself create fixed L/R support or a Claim/Task assessment.

### Coefficient bounds and actual embedding domain

The actual degree-ten field and its ordered real coordinates are those independently checked in [D G0019](#lehmer-joint-descent-review): two real embeddings followed by the real parts and imaginary parts of the four upper unit roots.
Thus the exact embedding matrix M has rows of powers of beta, beta^(-1), and those eight neutral real coordinates.
For the column a of power-basis coefficients, y=M a.
All roots are distinct and P is irreducible, so M is invertible and every actual element of Z[beta] has a unique such integer vector.

For a row of M^(-1), the two real-coordinate contributions are bounded by the row's absolute coefficients times 1 and S.
Cauchy--Schwarz bounds its neutral contribution by 8 times the Euclidean norm of its last eight entries.
The author's inverse enclosure and floor of the resulting upper bound therefore imply

    |a_i|<=(7,6,7,7,6,5,5,5,5,6)_i.

The independent [J G0028](../../computations/programs/Yin_J_G0028/readme.md) recomputes M using exact rational root isolation and Arb, inverts it with a separate implementation, and verifies every real upper bound is strictly less than the corresponding saved integer bound plus one.
Integrality then yields the same bounds without depending on the author's floor routine.
The complete original box size 108561184875 is independently recovered.

The polynomial discriminant was also recomputed independently as 1332031009=36497^2, and the real-coordinate embedding determinant enclosure agrees with 36497/16.
The factor 16 is 2^4 for the four complex pairs when replacing complex embeddings by real and imaginary parts.
The cylinder and ellipsoid volume ratios were read as diagnostic estimates only; neither their closeness to the later count nor any lattice-volume heuristic enters the coverage proof.

### Two rounding errors and the unimodular convention

Since |x_+|<=1, |x_-|<=S<67/10 and rho<8, the weighted vector satisfies

    8 x_+^2+8 x_-^2/(67/10)^2+rho^2<80.

Using a non-strict enclosing radius therefore loses no K_8 point.
The positive coordinate weights are used only for enumeration.
They do not replace the neutral norm or the dynamical domain.

The integer matrix B stores basis vectors by rows.
If a is a row coefficient vector, its rounded weighted embedding is aB/Q, Q=10^8.
The exact coordinate errors are bounded using the already proved |a_i| bounds, so the Euclidean error epsilon_B covers every original K_8 point, including root and square-root enclosure error.
It is not estimated from the small observed candidate set.

The retained U has determinant -1 and an integer inverse, independently verified by exact matrix arithmetic.
Thus a=bU is a bijection of integer coefficient vectors, and b=aU^(-1).
The necessary b_j bounds correctly use column j of U^(-1), giving the retained list (96,74,40,56,40,28,5,12,11,5).
No property of the LLL algorithm is needed after this candidate transformation has been verified.

For G=(UB)(UB)^T/Q^2, the exact positive LDL^T identity gives T_true=L sqrt(D), with

    ||b T_true||^2=bG b^T=||aB/Q||^2.

The lower-triangular row convention is correct.
The second error epsilon_T is bounded using the transformed b bounds, not the original a bounds.
It includes every entry of the scaled triangular approximation T/H, H=10^5.
The two Euclidean errors are then added by the triangle inequality before squaring.
The independent check verifies the exact LDL matrix identity, positive diagonal, unit lower-triangular structure, both error enclosures and

    (sqrt(80)+epsilon_B+epsilon_T)^2
        < 800554833912/(10^5)^2.

Its separately computed values are approximately epsilon_B=7.7700136791e-7, epsilon_T=0.0031003012665 and required squared radius 80.0554833911701, with full ball errors retained.
These decimals are summaries; the program uses validated interval comparisons.
No saved decimal error, orthogonal-basis assumption or LLL quality assertion is a premise.

### Traversal completeness and conservative filters

With the lower-triangular T, coordinate j of bT depends only on b_j,...,b_9.
Assigning b_9 down to b_0 is therefore the correct order.
Once the tail is fixed, every admissible next integer lies between

    ceil((-floor(sqrt(remaining))-center)/T_jj)
    and floor((floor(sqrt(remaining))-center)/T_jj),

intersected with the necessary b_j bound.
The diagonal is strictly positive.
The source's signed floor/ceiling divisions handle negative numerators correctly; its floating square-root seed is corrected in both directions by exact integer square comparisons.
Every selected integer has a nonnegative remaining budget.
The recursion therefore visits every integer vector in the certified ellipsoid and box, and visits it once.
Caps only stop the computation with an incomplete flag; the retained completed run is far below either cap.

The transform a=bU is exact.
Its original-box rejection is justified by the independently checked coefficient bounds.
The integer embedding intervals are outward: a positive coefficient uses the lower/upper endpoints in their normal order, while a negative coefficient reverses them.
The two real filters reject only intervals disjoint from the closed required strips, with the stable strip enlarged to a certified outer bound.
For a neutral coordinate, MinSquare is zero when its interval crosses zero and otherwise the smaller endpoint square.
Summing these lower bounds can reject only a state whose actual rho^2 is at least 64.
This is compatible with the strict rho<8 definition of K_8.
There is no inward rounding at the real or neutral boundary.

The compiled traversal was read completely, including the run script's matrix orientation and data types.
The reviewer independently checked operation bounds rather than relying only on the checked keyword.
Before the original-box rejection, transformed coefficient magnitudes are bounded by 423; the largest full triangular-coordinate bound is 41725592.
After the box check, the largest scaled embedding-coordinate bound is 130898983, and the sum of the eight neutral scaled coordinate-square upper bounds is 11120219802139125, well within signed 64-bit range.
Centers, their addition to square-root spans, adjusted square comparisons, coefficient transforms, filter squares and threshold products are all covered.
The few division/sign operations outside an explicit checked block cannot encounter the minimum signed integer in these verified ranges.
Loop bounds and counters are bounded by the small coefficient boxes and explicit caps.

### Independently implemented enumeration and encoding

The reviewer did not simply rerun the compiled C# traversal.
J G0028 uses Python arbitrary-precision integers and math.isqrt for the complete branching, and a separately written NumPy integer batch formulation for the outward filters.
Every NumPy int64 intermediate is covered by the independently verified bounds above.
The code imports no author preparation, interval, certificate-checker or traversal implementation; only the reviewer's own J G0023 root-isolation helper is reused.
Its enclosure check uses exact SymPy matrix identities and 320-bit Arb with root intervals of width at most 2^(-240).

The independent traversal completed below both caps and recovered exactly:

    recursion nodes:        4818379
    full ellipsoid leaves:  3077691
    retained unique states: 797507.

More decisively, it decoded and compared the entire mathematical state set to the author's compact-states.bin; equality held.
The output sequence order also matched.
This comparison is over all state keys, not merely a comparison of counts.
Independent verification (`mathematics/computations/outputs/Yin_J_G0028/verification.json`) and independent binary (`mathematics/computations/outputs/Yin_J_G0028/independent-states.bin`) retain the actual result.
The final independent run took about 5.91 seconds for its enumeration/comparison stage under Python 3.12.14, NumPy 2.3.5, SymPy 1.14.0 and python-flint 0.9.0.
Author outputs were read only.

Encoding is injective on the proved coefficient box: nibble i stores a_i+8, with every a_i in [-7,7].
The fields use disjoint groups of four bits and no bits above bit 39.
Explicit little-endian uint64 decoding avoids the native-endian assumption of array('Q') on other hosts; the author's executed Windows host is little-endian.
The independent result checks uniqueness and every decoded coordinate, and irreducibility makes distinct degree-below-ten coefficient vectors distinct actual algebraic states.

One nonblocking wording issue was reported before edits: D G0022 said the coefficient bounds lie "strictly within" the encoding range [-8,7], although the upper bound seven is permitted and attained by that bound.
"Fit within" is accurate.
The code checks a_i<=7 and the proof needs inclusion, so this has no mathematical effect.
The root had independently noticed the same wording issue.
No substantive correction was requested.

### Scope retained for the next review

This finding supports complete coverage of K_8 by the original 797507-state superset.
It does not prove that every candidate belongs to K_8.
It does not check the later seventy exclusions, any ancestry edge, zero-path coverage, compact termination, an infinite actual Lehmer core or a probability estimate.
The author reported adding path material in separate files and new D G0022 Sections 5--6 while leaving the frozen enumeration chain unchanged; those additions require their own review.
No candidate was removed or reclassified during this completeness review.

<a id="lehmer-full-review-history"></a>

**Preserved original dated D G0025 review history.**
The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Independent complete-chain review of the original Lehmer actual return core

Date: 2026-10-10, Asia/Hong_Kong.
Separately assigned structural_research AI review for Yin.
The reviewer contributed none of the Lehmer joint-block, normalized-body, compact-enumeration, path or proposed final bridge derivations.
Shared author/coordinator progress explanations and earlier component review findings were read first; this is not blind review.

### Obligations and inspected interfaces

The complete chain must retain the actual degree-ten order and original digits, all eight real neutral coordinates, positive additive descent and strict radius-eight boundary, a complete compact superset, exact integer path coverage or rigorous exclusion of every retained candidate, reciprocal reachability with the exact two real strips, lattice infinitude in the degree-ten setting, and the accepted L157 consequences.
Any time/probability corollary must retain its bounded-radius/real-strip hypotheses and distinguish existence of one finite path from a bound for all random paths.

The reviewer has read D G0017/D G0019, D G0020/D G0023 and D G0022, together with the complete exact interval, normalized-body, enumeration, path and exclusion programs in J G0022/J G0024/J G0026.
The existing D19 and D23 findings are reused only for their precisely stated partial-descent and certificate scopes; neither supplies compact termination.
The author J26 path report now has 1044588 acyclic parent nodes, 797437 covered candidates and 70 exact exclusions from the complete 797507-state superset, with maximum path length25.
This report is an input to review, not itself the review finding.

Initial code and interface checks have found no defect.
Independent finite-path/exclusion verification and the final assembled proof remain to be checked before an end-to-end disposition is recorded.
The old ESS proof is not being re-audited; L157 is an accepted interface.
No fixed adoption or G0001 completion is asserted.

<a id="lehmer-path-and-coverage-review"></a>

### Exact compact-termination interface finding

At 2026-10-09T16:11 the reviewer completed the new finite-path and exclusion checks in [J G0029](../../computations/programs/Yin_J_G0029/readme.md).
No defect was found.
Every actual element of K_8 has a verified original-digit continuation to zero of at most25 digits, conditional only on the separately reviewed complete enumeration, whose exact interface was read as described below.
This finding is not yet the final assembled infinitude/time theorem review.

#### Reused component findings and their actual scopes

The full [D G0019 joint-descent review](#lehmer-joint-descent-review) and [D G0023 normalized-body review](#normalized-lehmer-radius-eight-review) were read, including their nonblind arrangements, exact implementations and limitations.
D19 supplies the degree-ten field, all ten real embedding coordinates, original digit convention and reviewed interval primitives; D23 supplies the radius-eight domain and positive drop57/100 from the two complete cells.
Its 32 rational signed-axis certificates all concern the same eight-dimensional hull of c/||c||^2, with strictly positive norm denominators.
The full root, matrix-inverse, normalized barycentric and word-image verifier code in J22/J24 was also read directly during this review.

The trace identity and five disjoint sign-changing quintic brackets account for the exact original Lehmer roots.
The mod-two Frobenius test and exclusion of linear factors are sufficient because five is prime.
A negative discriminant image in a real embedding of the irreducible trace field excludes a square, so the quadratic extension has degree ten.
The constant term one gives an integral unit, beta>1 makes it nontorsion, and the power-basis embedding is injective with full rank.
The four complex pairs contribute eight real coordinates, with rho^2 the sum of four complex absolute squares, not twice that sum.

For each fixed cell, all its saved words are legal on the entire closed interval.
The contained coordinate cross-polytope gives the Euclidean radius t/sqrt(8).
Selecting one normalized vertex in the opposite direction to the current joint neutral vector gives a decrease bounded below by its own positive displacement cost times the positive factor16r-1.
Thus the minimum displacement cost gives the correct additive bound; neither a direction-dependent denominator nor a different word for each conjugate enters.
Negative cells, finite zero prefixes and the injectivity exclusion of a nonzero x_+=0 state cover the complete narrow real domain.
The digitwise stable strip and backward expanding-strip estimate hold through the complete words.
A fixed positive squared-norm drop gives finite entry into the strict rho<8 residue.
These interfaces have been checked here in addition to reading the prior findings; the new review does not claim a second implementation or rerun of every earlier geometry check.

The complete [D G0024 enumeration review](#lehmer-compact-enumeration-review), recorded at 2026-10-09T16:07, was also read.
Its 797507-state conclusion is completeness of a finite superset, not exact membership.
That reviewer independently recomputed inverse-embedding coefficient bounds, both rounding-error enclosures, the integer unimodular convention, signed-integer safety bounds and the entire state set.
Its J28 arbitrary-integer traversal and outward filters reproduce all4818379 recursion nodes,3077691 leaves and every retained state, including set equality rather than merely matching counts.
The finding expressly excludes the later paths and70 exclusions, so those are supplied by the present new check rather than silently inherited.

The present reviewer also read all of the author C# traversal and rational certificate checker.
The lower-triangular row convention makes descending-coordinate recursion complete; floor-square-root adjustment and signed divisions preserve every eligible integer.
Necessary original/reduced coefficient bounds and the two additive norm errors are computed for the whole enclosing domain, not fitted to returned states.
Stable filters are outward and neutral rejection at a lower squared bound>=64 is compatible with strict rho<8.
The original four-bit encoding fits the coefficient bounds; no arithmetic change or new restriction arises when this output is consumed by the path certificate.
No new independent enumeration was run by the present reviewer: that independently reproduced component is reused at D24's actual scope.

#### Path graph and algebraic identity

The author `Paths.cs`, `verify_paths.py` and `classify_uncovered.py` were read completely.
Floating embeddings in `Paths.cs` only guide which reverse states are found.
The actual certificate consists of packed integer vectors, parent indices and digits.
Neither exhaustive discovery nor membership of every intermediate point in K_8 is needed once a valid finite chain to zero is retained for each target.

A four-bit candidate key decodes a_i as nibble_i-8; a five-bit path key decodes a_i as field_i-16.
Both encodings are injective on their specified ranges.
The reviewer implementation uses explicit little-endian reads, checks no high bits occur, checks the original797507 keys are distinct after conversion, and compares actual integer state keys across the two formats.
Thus it does not rely on their binary integers being equal before repacking.

For each nonzero node a, digit d and parent b, J G0029 forms all eleven coefficients of

    t a(t)+d-b(t)

and verifies they are exactly a_9 times P(t).
This proves beta*a+d=b in the actual degree-ten order; it is a different implementation from updating each coefficient with the author's forward recurrence.
Every digit is checked to be -1,0 or1.
The initial node is the zero polynomial, with the prescribed base record.
Every later parent index is strictly smaller than its child index, so induction proves that every node reaches zero in finitely many exact steps, with no unchecked directed cycle.
The program recomputes depths from those parents.
All1044588 distinct retained nodes pass and the maximum recomputed depth is25.

The checker reads all declared retained parts and compares the intersection with the original complete target set.
Exactly797437 original candidates are covered.
The set difference is exactly70 and agrees elementwise with the retained uncovered keys.
This is not a coverage count inferred from a discovery summary.
Unused search nodes, floating pruning and the search cap play no role in that finite certificate argument.

#### Every uncovered candidate is outside the required compact set

The new checker imports no author helper.
It bisects the five rational sign-changing trace intervals again, at rational width at most10^(-50), constructs beta and the four upper unit roots using independent Fraction/square-root enclosures, and evaluates every uncovered integer polynomial at all ten real coordinates.
It reconstructs S=beta/(beta-1) from those intervals.
No saved classifications, numerical roots or author interval code are used.

The interval operations were checked for correct endpoint orientation, all four multiplication corners, inversion only away from zero, squaring across zero, and integer-square-root lower/upper enclosure.
Exact Fraction calculations preserve the enclosure without relying on floating precision.
Powers and complex multiplication are propagated through degree nine.
The underlying root definitions are the same exact roots as in the previously checked domain, although their interval endpoints are computed afresh.

Of the70 actual set-difference states,68 have a certified lower bound rho^2>=64, and two have their contracting-coordinate interval strictly outside the closed required strip.
The former are excluded because K_8 has rho<8, including equality at its boundary; the latter are excluded with strict outward separation from S.
None requires excluding an ambiguous boundary.
Every unclassified point would cause a failure, and there are none.
The new output retains each state and exclusion reason.
Thus no actual member of K_8 remains without a verified finite path.

#### Execution and current scope

The independent program [J G0029 verify.py](../../computations/programs/Yin_J_G0029/verify.py) ran successfully under Python3.12.14 using only its standard library.
It writes only to its own verification.json (`mathematics/computations/outputs/Yin_J_G0029/verification.json`); author proof and certificate files were not modified.
This is a separately implemented finite-path and exclusion verification by a noncontributor to those inputs, under the nonblind review arrangement at the start of this document.
It is not a formal proof-assistant check or independent rediscovery of the paths.

The combined component interfaces therefore establish complete co-return for every actual state in the narrow real domain after the normalized descent.
The actual infinite reachable-and-returning core, the final exact theorem statement and any optional quantitative extension still require the final consolidated proof to be read before the complete-chain review is closed.
Those obligations are kept separate below when supplied.

<a id="lehmer-complete-chain-review"></a>

### Complete D G0027 assembly finding

At 2026-10-09T16:17 the same separately assigned reviewer completed the full read of [D G0027](../../ledger/Yin_L_G0170_v1.md#lehmer-infinite-core-theorem), including all four theorem items, its complete proof, copied-component harmonization, the new degree-ten reciprocal/pigeonhole bridge, the explicit timing/probability conclusion, and provenance/source boundaries.
No substantive mathematical defect or missing hypothesis was found in that frozen four-item version.
The exact fixed-input conclusions are supported by the complete chain described here.
This is not a Claim adoption, fixed allocation, human review, formal proof or G0001 completion.

#### Assembly and component interfaces

The actual polynomial, degree-ten order, original digits, two real embeddings and complete eight-real-dimensional neutral norm agree throughout the assembled proof and all three computation layers.
The radius-eight descent replaces the older radius1500 bound; the old simplex theorem is used for its unchanged input/word/interval interfaces, not as though its weaker radius already established the smaller residue.
D23's normalized-body finding and J24/J27 supply the new threshold and positive drop.
The exact compact domain has closed real strips and strict neutral inequality rho<8 in both the descent and enumeration.
D24's independently reproduced superset may include outer points; the seventy exclusions in the present review remove only points rigorously outside that actual domain.

The complete D G0022 Sections5--6 were also read after their addition.
Their forward polynomial recurrence, original digit code, acyclic ancestry and claim of at most25 digits agree with the independently checked J29 evidence above.
No intermediate-state requirement from the numerical reverse search is imported into the exact continuation theorem.
The new compact argument covers every actual K_8 point, so finite descent from every narrow-domain algebraic input followed by its certified compact word proves theorem item1.
There is no reachability assumption hidden in this co-return conclusion.

The copied proofs and the consolidated four-item theorem agree in every required quantifier and constant.
In particular theorem item4 explicitly retains |x_+|<=1 and |x_-|<=S as well as rho<=R; it does not repeat the earlier quartic draft's omitted-strip wording.
The change from "strictly within" to "fit within" the inclusive encoding range is correct and has no mathematical effect.
The actual complete theorem and proof were inspected, rather than inferred from the component PASS findings or computational summaries.

#### New reciprocal reachability and infinitude

Irreducibility and reciprocity ensure beta^(-1) is a conjugate and generates the same field.
The field map sigma(beta)=beta^(-1) is therefore an automorphism of this same degree-ten field with square the identity.
Since beta is an algebraic unit, beta^(-1) lies in Z[beta]; sigma and multiplication by beta^(-1) preserve its integral additive lattice.
Consequently T(x)=beta^(-1)sigma(x) is an additive involution of that lattice.
It is not used as a ring homomorphism or as preserving a real order, and the assembly explicitly makes that convention clear.

For an n-digit zero continuation of y, dividing the endpoint equation by beta^n gives y=-sum_(i=1)^n eta_i beta^(-i).
Applying T gives -sum eta_i beta^(i-1), exactly the state reached from zero by (-eta_n,...,-eta_1).
This checks both the digit signs and their reversal.
The empty word at zero is harmless.
The conversion works with the same original alphabet and actual algebraic states.

Since beta<2, beta<S.
Every x in Omega has the narrow co-return bounds.
The two real values T(x)_+=x_-/beta and T(x)_-=beta*x_+ also have those bounds; their neutral coordinates need no bound because theorem item1 already holds throughout the unbounded neutral domain.
Co-return of T(x) yields a genuine word from zero to x, while co-return of x yields its return to zero.
Their concatenation is an actual zero-to-zero word through x.
No projection, ambient spectrum claim, larger digit alphabet or assumed reversibility of an arbitrary path is being substituted for this construction.

For the counting step, degree ten gives (N+1)^10 different power-basis elements.
Each real embedding is a fixed linear function of their coefficients, so its range length is bounded by a fixed constant times N.
A partition into cells of fixed positive widths1 and beta therefore uses at most C(N+1)^2 cells.
At least one contains at least c(N+1)^8 points.
Differences from one point are distinct elements with strict coordinate differences below1 and beta.
Their increasing cardinality proves infinitude even if the selected cell and base point change with N.
This explicitly rechecks the higher-rank generalization of the quartic bridge; the earlier quartic theorem alone was not treated as a theorem about this beta.
Thus theorem item2 follows.

#### New timing and probability conclusion

For a nonzero order element, its field norm is a nonzero integer and factors into the two real values times the four complex squared absolute values.
AM--GM applied to those four nonnegative numbers gives

    product_j |x(zeta_j)|^2 <= (rho^2/4)^4 <= R^8/256.

Together with |x_-|<=S<67/10 this yields the strict lower bound |x_+|>2560/(67R^8).
The bound S<67/10 is supplied by the full exact root intervals and was separately checked in the enumeration; it does not follow merely from the weaker displayed beta>117/100 approximation.
The proof invokes the full root interval bound correctly.

The threshold (117/100)^k>=67R^8/5120, combined with beta>117/100 and the strict lower bound just obtained, ensures that at most K_R zero digits exceed expanding magnitude1/2.
The first-crossing rule therefore needs no more than K_R zeros, lands below beta/2<1, and preserves the other necessary conditions.
An endpoint already of magnitude at least1/2 needs none.
The norm bound is required only at nonzero pre-K_8 endpoints; zero already belongs to K_8.

Every later endpoint has rho<=R because its neutral square decreases; intermediate values within a selected block need not obey that bound and are not used by the argument.
The definition N_R=floor((R^2-64)/delta)+1 gives R^2-N_R delta<64, including R=8.
Thus at most N_R finite blocks, each of length at most K_R+11, are needed to enter K_8.
An initial point inside K_8 uses zero such blocks.
Adding the at most25-digit compact path proves the stated length bound.
The growth N_R=O(R^2), K_R=O(log R) has constants for this fixed beta; it supplies no degree-uniform estimate.

A particular permitted word of length l has product probability at least4^(-l) under the independent probabilities(1/4,1/2,1/4).
The event of following that prefix forces a zero hit by time l, even if it hits earlier.
Since l<=L_R+25, theorem item4's lower probability follows.
It is an existence/hitting estimate uniform on the stated bounded-radius narrow domain, not a bound on every random trajectory, a first-return tail or an unconditional entropy estimate.
All these distinctions remain explicit in the theorem.

#### Accepted consequence and source boundaries

The accepted L G0157 v1 Sections4--5 require a nontorsion algebraic unit, its actual order, original digits and the full actual returning-state set.
Every hypothesis is now supplied.
Its finite-core equivalences give unbounded nonzero norms, no finite common prime-ideal support for nonzero states, unbounded integer quotient heights among H(Pq)<=1, and nonregularity of the finite zero-word language.
The restricted finite-prime core is not substituted for the full core.
The theorem's prime-support phrase is understood on nonzero states, as required by L157; explicitly writing D minus{0} was suggested to the coordinator for precision, without changing the intended result.

The reviewer directly reread L G0004 Section9's finite-field and trace-extension interface and used the previously inspected fixed L157 interface at its accepted scope.
Their prior proof histories and ESS's original proof were not re-audited.
The Mercat citation is methodological context for a different quartic, with its existing acquisition/inspection boundary; no source table or source theorem supplies this degree-ten certificate.
There is no new literature-novelty or exhaustive-priority assertion.
All new substantive proof steps in this assembly have either the explicit prior component findings at their exact scopes or the direct end-to-end checks above.

The review is independently organized relative to the Lehmer derivations: this reviewer authored none of the block, normalized-body, enumeration, path, bridge or timing mathematics.
It did author independent checking code and the review itself.
Parent/author progress, the earlier component findings and the author's proof were available before this finding, as disclosed from the start.
The supported conclusion is the exact four-item fixed-original-Lehmer theorem, not the unrestricted G0001 goal.
A subsequent strengthening requires its own added scope check rather than inheriting this finding automatically.

<a id="exact-strip-growth-review"></a>

### Separate exact-strip and geometric-growth finding

At 2026-10-09T16:22 the same separately assigned, noncontributing reviewer completed the full read and proof check of [D G0028](../../ledger/Yin_L_G0170_v1.md#exact-salem-return-strip), including its general conditional theorem, fixed-input boundary observation and [two-sided state count](../../ledger/Yin_L_G0170_v1.md#return-core-neutral-growth).
The coordinator authored these deductions and had explained the proposed strengthening before this review; the review is independent of their derivation but not blind.
No mathematical defect or missing hypothesis was found.
This new finding supplements, rather than retroactively enlarges, the 00:17 review above.

The general statement expressly assumes narrow-domain co-return for the actual order, original digits and the same beta.
It does not assert that premise for every Salem unit.
The independently supported quartic and original Lehmer results supply it at their two fixed inputs.
The reciprocal automorphism and additive involution used here have precisely the unit, irreducibility and reciprocity hypotheses already checked; no assumption about arbitrary real projected points replaces actual order membership.

For 1<u<B, the proposed greedy step beta*u-1 is strictly positive and smaller than u.
Thus the sign stays fixed while the rule is used, and the displayed recurrence is valid until the first u<=1.
If such a step never occurred, B+beta^k(u_0-B) would eventually be negative, a contradiction.
The last value is positive because its predecessor exceeds one and beta>1.
The contracting strip is invariant under every digit.
The finite prefix may increase the neutral radius, but the narrow co-return premise has no neutral bound, so no extra uniformity is required.
This proves generalized co-return on the stated half-open pair of real bounds.

The map T sends the full open strip into itself because S/beta=B and beta*B=S.
Both x and T(x) therefore co-return; the exact reversed-negated word identity from the preceding review supplies reachability of x.
Necessity uses the two finite geometric sums with the correct indices, giving strict bounds for every nonempty word, while an empty word contributes only zero.
Thus the equality with the actual return core and the strict boundaries are proved.
The conclusion does not merely describe a projection or closure.

For each of the two specified polynomials, P(1)=-1 implies P(t)+1=(t-1)Q_1(t) with Q_1 integral.
Evaluation at beta gives (beta-1)Q_1(beta)=1, proving B belongs to O without requiring maximal-order integrality.
Its two real values are B and -S.
Injectivity of either real field embedding makes +/-B the only possible actual lattice states on any of the four closed-strip boundary lines.
They are excluded by the strict necessity inequalities, so weakening both bounds adds exactly two states.
This boundary conclusion was checked only for the two specified P(1)=-1 inputs; it is not silently included in the general conditional theorem without that premise.

For the upper count, the complete real embedding of the degree-d order is a full lattice.
A fixed positive separation radius gives disjoint balls about all counted states.
Enlarging both bounded real coordinates by that radius and the neutral ball radius by the same amount supplies a containing cylinder of volume O((R+1)^(d-2)); no discreteness of the two-real projection is assumed.
For the lower count, degree d makes all (N+1)^d coefficient-box elements distinct, and fixed linear embedding coordinates use O((N+1)^2) cells of widths1 and beta.
Differences within one half-open cell have both strict narrow bounds.
Since beta<2, beta<S and 1<B, these are actual core states.
Their coefficients have absolute value at most N, so each neutral modulus is at most dN and rho<=d*sqrt(r)*N.
Taking N=floor(R/(d*sqrt(r))) and reducing the positive constant after subtracting the chosen base point proves the lower estimate for every sufficiently large R, not only a subsequence.
The constants remain input-dependent.
The count concerns states, not words, weights, return probabilities, equidistribution or a Mahler gap.

No new computation is needed or claimed for these elementary deductions.
The narrow-domain certificate, earlier review scopes and accepted external interfaces remain exactly those identified above.
In particular the explicit L_R+25 timing/probability bound continues to have D G0027's narrow real-strip and bounded-radius hypotheses; the new open-strip identity does not extend that numerical bound automatically.

At the same 2026-10-09T16:22 check, D G0027 theorem item3 was reread after the coordinator's sole clarification to "prime-ideal divisors across the nonzero states in D have no finite global cover".
This resolves the earlier precision suggestion and matches L157 exactly.
The initial observation and its original scope remain preserved above; no other theorem quantifier, constant or proof dependency changed in that correction.
The final D27 four-item statement and the separately reviewed D28 strengthening are ready for coordinating fixed-input adoption.
This review neither adopts a C decision nor completes G0001.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original joint-simplex finding](#lehmer-joint-descent-review) | [Historical radius1500 component](../../ledger/Yin_L_G0170_v1.md#lehmer-joint-neutral-descent) | Full original D17 Sections1--5, original algebraic input and joint-simplex partial descent only, with J22/J23 execution and limitations preserved. |
| [Normalized-body finding](#normalized-lehmer-radius-eight-review) | [Normalized radius-eight component](../../ledger/Yin_L_G0170_v1.md#normalized-lehmer-radius-eight) | Full original D20 Sections1--5 and J24/J27 evidence: complete real domain, joint body, positive denominators and squared-norm drop57/100; no inherited compact termination. |
| [Complete enumeration finding](#lehmer-compact-enumeration-review) | [Complete finite-superset component](../../ledger/Yin_L_G0170_v1.md#lehmer-compact-complete-enumeration) | Original D22 Sections1--4 only: exact containing ellipsoid, integer traversal/filters and full797507-state reproduction by J28; excludes later paths and70 exclusions. |
| [Finite paths and exclusions](#lehmer-path-and-coverage-review) | [Exact compact continuations](../../ledger/Yin_L_G0170_v1.md#lehmer-compact-exact-zero-continuations) | Original D22 Sections5--6 and independently implemented J29 check of all1044588 nodes, target-set difference and70 exact exclusions, maximum25 digits; complete-enumeration finding reused at its stated scope. |
| [Complete original-Lehmer assembly](#lehmer-complete-chain-review) | [Original-Lehmer theorem](../../ledger/Yin_L_G0170_v1.md#lehmer-infinite-core-theorem) | All four fixed-input conclusions and exact hypotheses, with the subsequently checked nonzero-state wording clarification recorded in the following finding. |
| [Complete original-Lehmer assembly](#lehmer-complete-chain-review) | [Complete original-Lehmer proof](../../ledger/Yin_L_G0170_v1.md#lehmer-infinite-core-proof) | Entire D27 algebraic, descent, enumeration/path, reciprocal, infinitude and bounded-radius timing/probability chain, with prior component findings reused only at their explicit scopes and L157 as accepted interface. |
| [Original targeted nonzero-state clarification](#lehmer-original-nonzero-state-clarification-finding) | [Original-Lehmer theorem](../../ledger/Yin_L_G0170_v1.md#lehmer-infinite-core-theorem) | Final item3 clarification explicitly restricts prime-ideal supports to nonzero states; no other quantifier, constant or dependency changed. |
| [Exact strip, growth and final clarification](#exact-strip-growth-review) | [General conditional strip theorem and proof](../../ledger/Yin_L_G0170_v1.md#exact-salem-return-strip) | Entire D28 strip proof under its explicit narrow co-return premise, applicability to the two fixed inputs and their P(1)=-1 boundary observation. |
| [Exact strip, growth and final clarification](#exact-strip-growth-review) | [Fixed-input geometric state growth](../../ledger/Yin_L_G0170_v1.md#return-core-neutral-growth) | Entire two-sided R^(d-2) counting proof with input-dependent constants, actual full lattice, all sufficiently large R, and state/word/probability boundaries. |

## Review relationships

These declarations preserve every original date, complete mathematical/native account, input, scope, finding, suggestion and verdict above.
They distinguish original program-level independent implementation from the actual agent-review relationship; titles, separate assignment, noncontribution and nonblind wording alone establish neither isolation nor substantive shared target context.
This is administrative retention of the original arrangements, without a new mathematical/source-proof review or native execution.

For the original23:51 radius1500 partial theorem, the account discloses shared G0001 context and earlier coordination, but does not establish the substantive content and initial order needed to decide whether the new eight-dimensional target mathematics was shared before the finding.
The previously frozen quartic method and its review descriptions are upstream fixed inputs.
They do not automatically make the new Lehmer target self-reviewed, and the generic shared-context disclosure does not establish isolation.
That whole original D17 Sections1--5/algebraic/joint-simplex/full-cell/strip/finite-residue/J22/J23 scope remains unknown and needs fresh independent coverage at that actual partial scope.

For the original23:59 normalized-body finding, the account specifically states that the coordinator's normalized linear-functional implication and positive-denominator/additive-drop guards were available before review.
These are substantive mathematics of that target, so the whole normalized D20 Sections1--5/J24/J27 arrangement is known self-review.
The original00:07 enumeration arrangement likewise discloses the coordinator's conceptual enclosing-ellipsoid/LDL contribution before the findings, in addition to preliminary reading; the complete D22 Sections1--4/J26/J28 scope is self-reviewed.
For the original00:11 paths/exclusions and00:17 complete assembly, the retained account says earlier component findings and author/coordinator progress explanations were read first.
The actual earlier findings above contain the target's normalized-drop and exact complete-enumeration conclusions.
This establishes shared substantive target-mathematical context for the whole new path/coverage and complete bridge/timing assembly arrangements.
Their separate polynomial/interval/enumeration implementations remain actual computational facts, not isolated whole mathematical review.

For the original 2026-10-09T16:22 exact-strip/growth finding, the phrase "explained the proposed strengthening" does not preserve that explanation's actual mathematical content or the needed initial arrangement.
The already fixed narrow co-return theorem is a necessary frozen premise; knowing it and its component findings is not by itself substantive prior sharing of the new greedy strip/boundary/counting deductions.
The retained account therefore establishes neither isolation nor known substantive target sharing for that distinct whole D28 scope.
Its entire conditional actual-order strip proof, both fixed P(1)=-1 boundary observations, every sufficiently large R two-sided full-lattice state count and all original limitations remain unknown for independent-review purposes.
Fresh isolated coverage is still needed for that whole target; a later current self-check does not close it.

The same 2026-10-09T16:22 event also actually reread only D27 theorem item3 after the nonzero-state wording clarification.
That targeted original-Lehmer reread follows the already known shared complete-chain arrangement, so it is self-reviewed.
Its precise binding below is separated from the distinct whole D28 finding; this does not create a new historical inspection or claim an additional whole corrected-chain review.
The complete initial suggestion and actual later clarification remain verbatim above.

| Review | Relationship |
| --- | --- |
| [Original joint-simplex partial finding](#lehmer-joint-descent-review) | unknown |
| [Original whole normalized-body finding](#normalized-lehmer-radius-eight-review) | self-reviewed |
| [Original whole enumeration finding](#lehmer-compact-enumeration-review) | self-reviewed |
| [Original whole paths and exclusions finding](#lehmer-path-and-coverage-review) | self-reviewed |
| [Original whole original-Lehmer assembly](#lehmer-complete-chain-review) | self-reviewed |
| [Original whole exact-strip and growth finding](#exact-strip-growth-review) | unknown |
| [Original targeted nonzero-state clarification](#lehmer-original-nonzero-state-clarification-finding) | self-reviewed |

<a id="lehmer-original-nonzero-state-clarification-finding"></a>
## Original targeted nonzero-state clarification

Date: 2026-10-09T16:22.
At the same actual event recorded in the preceding original account, the reviewer reread D27 theorem item3 after the coordinator clarified that the finite-prime-support statement concerns nonzero states.
This matches the original L157 interface and resolves the initial precision suggestion without changing another quantifier, constant or dependency.
The reread covered that actual changed item only.
The complete initial00:17 assembly finding remains at its original scope, and no additional complete corrected-proof inspection or native run is invented.
This targeted finding is self-reviewed under the same known prior component-conclusion/shared-chain arrangement; it does not alter the distinct whole D28 unknown relationship.
