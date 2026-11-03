---
author: Yin
---
# An infinite original-digit return core for the original Lehmer Salem unit

Date: 2026-10-10, Asia/Hong_Kong.
Fixed original-Lehmer result adopted by the coordinating AI for Yin under the active G0001 authorization after the separately organized complete-chain review at 2026-10-09T16:17 and the final clarification/addendum review at 2026-10-09T16:22.
The complete proof, exact-strip strengthening, computation interfaces and full substantive review histories are retained below.
This is a fixed-input result, not a resolution of the unrestricted Lehmer gap.

<a id="lehmer-infinite-core-theorem"></a>
## Theorem and precise scope

Let beta>1 be the expanding root of

    P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,

and let zeta_1,...,zeta_4 be its upper unit-circle roots.
Write x_+=x(beta), x_-=x(beta^(-1)) for x in O=Z[beta], and

    rho(x)^2=sum_(j=1)^4 |x(zeta_j)|^2,
    S=beta/(beta-1), B=1/(beta-1).

The original operations are x -> beta*x+eta, eta in {-1,0,1}.
The actual return core D consists of the states on finite original-digit words that start at zero and end at zero, including the empty word.
Then:

1. Every x in O with |x_+|<=1 and |x_-|<=S has a finite continuation to zero.
2. D contains every x in O with |x_+|<=1 and |x_-|<=beta, and is infinite.
3. Applying the accepted [L157 actual-core equivalences](Yin_L_G0157_v1.md), absolute integer norms of nonzero states in D are unbounded, prime-ideal divisors across the nonzero states in D have no finite global cover, and coefficient heights H(q) of integer polynomial quotients with H(Pq)<=1 are unbounded.
   The finite zero-word language is not regular.
4. For each R>=8 and every x in O with |x_+|<=1, |x_-|<=S and rho(x)<=R, there exists a continuation to zero of length at most L_R+25, where

       delta=57/100,
       N_R=floor((R^2-64)/delta)+1,
       K_R=min{k>=0: (117/100)^k >= 67 R^8/5120},
       L_R=N_R(K_R+11).

   For the original independent digit law with probabilities (1/4,1/2,1/4), the probability of hitting zero by that time is at least 4^(-(L_R+25)).
   This chosen-word length bound is O(R^2 log R) for this fixed beta.
   It does not bound every random trajectory or establish a useful unconditional return tail or a degree-uniform entropy estimate.

<a id="lehmer-infinite-core-proof"></a>
## Proof

### Algebraic input and word conventions

The trace identity is

    P(t)=t^5 Q(t+t^(-1)),
    Q(u)=u^5+u^4-5u^3-5u^2+4u+3.

[J G0022](../computations/programs/Yin_J_G0022/readme.md) checks this identity by integer Laurent expansion.
It checks Q's irreducibility modulo two: Q mod 2 divides u^32-u and has neither 0 nor 1 as a root.
Because five is prime, these checks establish the standard finite-field criterion explained in [L G0004, Section 9](Yin_L_G0004_v1.md).
Thus Q is irreducible over Q.
One of its real embeddings lies in (-2,2), so u^2-4 is negative there and is not a square in Q(u).
Adjoining a root of t^2-ut+1 therefore doubles the degree, proving the degree-ten irreducibility needed for the actual field embeddings.
This reuses L G0004's trace argument rather than a new irreducibility principle.

Five disjoint rational brackets, each with opposite endpoint signs, isolate Q's five roots:

    (-19/10,-18/10), (-15/10,-14/10), (-6/10,-5/10),
    (9/10,1), (2,21/10).

Degree five and five sign changes account for every root, one per bracket.
Rational bisection and integer-square-root enclosures give beta in (117/100,118/100) and the four upper unit roots via

    Re(zeta_j)=u_j/2, Im(zeta_j)=sqrt(1-u_j^2/4)>0.

Consequently beta is the original degree-ten Salem unit, and all ten real embedding coordinates form a full lattice image of Z[beta].
The program does not rely on its numerical discovery roots for this argument.

For a word w=(eta_1,...,eta_k), define the joint complex displacement

    c_w=(sum_(i=1)^k eta_i zeta_j^(-i))_(j=1)^4,

viewed as the vector (Re c_1,...,Re c_4,Im c_1,...,Im c_4) in R^8.
The endpoint neutral vector is the coordinatewise rotation

    (zeta_j^k (z_j+c_(w,j)))_(j=1)^4,

which preserves its complete Euclidean norm.
No individual projected pair is substituted for this joint vector.

### Joint normalized descent to radius eight

The exact finite certificate supplies, for every actual x with |x_+|<=1, |x_-|<=S and rho(x)>=8, a finite zero prefix followed by at most eleven original digits ending at x' with

    |x'_+|<1, |x'_-|<=S,
    rho(x')^2<=rho(x)^2-delta.

All intermediate states remain within |x_+|<B and |x_-|<=S.
Here is the full normalized-body argument and its finite certificate interface.

For a legal word w, let c_w be its complete eight-real-dimensional neutral displacement as defined above.
Its endpoint rotation preserves Euclidean norm.
For c_w nonzero, set

    u_w=c_w/||c_w||^2.

Then the exact squared-norm change is

    ||z+c_w||^2-||z||^2
       =||c_w||^2 (1+2 z.u_w).

Suppose the convex hull of the retained u_w contains the radius-r Euclidean ball around zero.
For every nonzero z, some retained vertex satisfies z.u_w<=-r||z||, because the hull contains -r z/||z||.
If every retained ||c_w||^2>=m>0 and ||z||>=R with 2rR>1, this gives

    ||z+c_w||^2-||z||^2 <=-m(2rR-1).

This uses each word's own cost in its normalized vector.
It avoids bounding all displacement costs by the largest one before choosing a direction.
Both the positive denominator and the strictly positive minimum displacement cost are proved by the exact certificate.

### Exact certificates in two cells

[J G0024](../computations/programs/Yin_J_G0024/readme.md) retains two complete closed expanding cells:

    I_1=[1/2,3/4], I_2=[3/4,1].

Every saved word maps its entire assigned cell strictly into (-1,1).
For each of the sixteen signed coordinate vectors +/-e_i in R^8, the computation saves nine original words and proves that the corresponding normalized vertices have a convex combination equal to +/-t e_i, where

    t_1=101/500, t_2=207/1000.

It certifies each combination by enclosing the inverse of the augmented 9 by 9 vertex matrix and proving all resulting exact barycentric coordinates are strictly positive.
The saved numerical LP weights are ignored.
Therefore the full convex hull contains the coordinate cross-polytope {y:||y||_1<=t}, hence the Euclidean ball of radius t/sqrt(8).

There are 288 word uses in the thirty-two certificates and 217 distinct integer words.
No word is longer than eleven digits.
All normalized vectors have nonzero, positively bounded squared denominators.
The exact cell-specific minimum squared costs are at least 3999/1000 and 873/250.
With R=8, the certified drops are at least 57/100 and 597/1000 respectively, so 57/100 is a uniform bound.
These are rational lower bounds; neither an approximate LP optimum nor a floating-point containment test is a proof premise.

Negative cells are obtained by negating x and every digit.
For 0<|x_+|<1/2, prepend zeros until its first crossing of 1/2.
This terminates for every nonzero actual algebraic state and lands below beta/2<1, preserving rho and contracting |x_-|.
If x_+=0 then x=0 and rho=0, outside the descent case.
The digitwise stable bound beta^(-1)S+1=S and the backward endpoint estimate for the expanding strip are proved just below.
Repetition lowers a nonnegative squared norm by at least 57/100 per block and therefore reaches K_8 in finitely many blocks.
No claim of a bounded number of zero-prefix digits independent of the initial state is made.

For completeness, the expanding intermediate bound follows without imposing an independent numerical restriction on a word's interior.
If k digits remain before the endpoint y with |y_+|<1, reversing that suffix gives

    |x_+| <= beta^(-k)|y_+|+sum_(i=1)^k beta^(-i)
           < beta^(-k)+B(1-beta^(-k)) <= B,

because B>1.
The zero prefix lies below beta/2<1 before entering a cell.
The contracting strip is invariant under every original digit.
These facts apply to every actual state, regardless of whether it was previously reachable from zero.
The lattice property makes

    K_8={x in O: |x_+|<=1, |x_-|<=S, rho(x)<8}

finite.
Iterating the positive square drop reaches this set in finitely many blocks.

### Complete finite superset of K_8

[J G0026](../computations/programs/Yin_J_G0026/readme.md) gives a certified finite superset of K_8 with **797507 distinct states**.
The complete enumeration ended normally, below both explicit caps, after 4818379 recursion nodes and 3077691 ellipsoid leaves.
These figures are actual retained run results, not estimates.

First, the inverse of the ten-real-coordinate embedding matrix gives the necessary power-basis bounds

    |a_i| <= (7,6,7,7,6,5,5,5,5,6)_i,
    x=sum_(i=0)^9 a_i beta^i.

For each inverse row A_i, the bound used is

    |a_i| <= |A_(i,0)|+S |A_(i,1)|
                  +8 sqrt(sum_(j=2)^9 A_(i,j)^2).

This is verified by outward rational interval inversion of the full embedding matrix.
Its dense integer box has 108561184875 tuples and was not traversed.

The exact polynomial discriminant, computed by a fraction-free Sylvester determinant, is 1332031009=36497^2.
Thus the real-coordinate embedding covolume is 36497/16.
The cylinder volume/covolume diagnostic predicts about 796777 states, and the ellipsoid chosen below about 3055602.
Those predictions motivated the algorithm and are not completeness or runtime bounds.

### Certified containing ellipsoid

Let S_0=67/10; the exact root intervals give S<S_0.
Define the weighted embedding Y by multiplying x_+ by sqrt(8), x_- by sqrt(8)/S_0, and leaving the eight real neutral coordinates unchanged.
Every point of K_8 satisfies

    ||Y(x)||^2=8 x_+^2+8 x_-^2/S_0^2+rho(x)^2 <=80.

The positive weighting is only an enumeration device.
It does not change the dynamical norm or the earlier descent claim.

Let B be the retained integer matrix approximating the row basis for Y at scale Q=10^8.
From the proved coefficient bounds, the exact checker bounds each coordinate of aB/Q-Y(x), then bounds its Euclidean norm by epsilon_B.
A computationally discovered integer basis transformation U is verified exactly to have determinant +/-1, and the reduced integer basis is U B.
Write a=bU.
Exact inversion of U gives necessary integer bounds for b; no LLL performance property is assumed in the proof.

The rational Gram matrix (UB)(UB)^T/Q^2 has an exact positive LDL^T decomposition.
If T_true=L sqrt(D), then ||b T_true||=||aB/Q||.
The retained lower triangular integer matrix T approximates T_true at scale H=10^5.
Using the necessary b bounds, the checker bounds ||b T/H-b T_true|| by epsilon_T.
It therefore proves

    ||b T||^2 <= H^2 (sqrt(80)+epsilon_B+epsilon_T)^2
                 <=800554833912.

The displayed right-hand side is an integer upper bound checked from exact Fractions; the saved decimal errors are not premises.
The exact certificate's nontrivial approximation steps are accounted for by these two additive norm errors.
The unimodular matrix, original and transformed coefficient bounds, triangular matrix, root-based coordinate bounds, and integer squared radius are all retained in the certificate file.

### Complete traversal and conservative filtering

For lower triangular T with positive diagonal,

    ||bT||^2=sum_(j=0)^9 (b_j T_(j,j)+sum_(i>j) b_i T_(i,j))^2.

The compiled traversal assigns b_9,b_8,...,b_0.
At each step the already assigned tail fixes a center and the remaining integer squared budget.
An integer square root, corrected by exact integer comparisons, and signed floor/ceiling division enumerate every integer b_j meeting the remaining bound.
The necessary transformed coefficient bounds only remove impossible original K_8 points.
Each full b maps bijectively to a=bU because U is unimodular.

After a full assignment, the program checks the proved original coefficient box.
It then uses outward integer-scaled intervals for all ten original embeddings.
A point is discarded only if its expanding interval misses [-1,1], its contracting interval misses a certified outer bound for [-S,S], or the sum of the lower bounds for the eight neutral coordinate squares is at least 64.
The last test is consistent with K_8's strict rho<8 inequality.
Ambiguous boundary points are retained.
Therefore every actual point of K_8 appears in the output.

The program uses checked signed 64-bit integer arithmetic.
A separate exact checker recomputes the basis/ellipsoid enclosure, verifies unimodularity, coefficient bounds, outward embedding filters, and sufficient integer-size bounds.
The retained run completed normally with no overflow or cap event.
Its caps were 50000000 recursion nodes and 2000000 retained candidates; encountering either would have marked the result incomplete.

Each retained state is packed as a little-endian uint64, with nibble i equal to a_i+8.
The proved coefficient bounds fit within that encoding's range.
The checker verifies file length, every decoded coefficient range and all 797507 states are distinct.
The binary contains a complete finite superset of K_8, not a claim that every boundary-ambiguous retained state lies in K_8 exactly.

### Exact compact continuations

The path certificate was added on 2026-10-10 after the complete enumeration was frozen.
Its original 797507-state output was unchanged by that addition.

A bounded reverse search discovered paths to zero for 797437 of those candidates.
It allowed the larger necessary expanding strip |x_+|<=1/(beta-1), the contracting strip |x_-|<=S and a numerical neutral radius-eight cutoff.
Thus it did not require intermediate states to stay in K_8's narrow expanding strip.
It exhausted its selected graph after 4003565 states, below the 6000000-node cap; it left seventy candidate states uncovered.
None of those numerical pruning or exhaustion facts is used to prove nonreturn or membership.

Every uncovered candidate was then checked with the full exact rational embedding intervals, separately from the coarse integer intervals used for enumeration.
Sixty-eight have a certified lower bound rho^2>=64, and two have contracting real embedding outside [-S,S].
Therefore all seventy lie outside the actual K_8.
They remain part of the earlier conservative superset and are not silently reclassified as an earlier enumeration error or as nonreturning states.

The retained ancestry certificate consists of 1044588 distinct algebraic states and one original digit/parent edge for each nonzero node.
Its two binary parts store a 50-bit state key, a parent index and the digit code.
A state coefficient a_i is the key's five-bit field i minus sixteen; the stored digit code minus one is in {-1,0,1}.
Node zero is exactly the zero state with its harmless zero self-reference.
Every later node has a strictly smaller parent index, so all parent chains are acyclic and terminate at zero.

The separate Python verifier checks every edge with integer arithmetic.
For P(t)=sum_(i=0)^10 p_i t^i, p_0=p_10=1, the forward recurrence is

    (a_0,...,a_9) -> (eta-a_9, a_0-a_9 p_1, ..., a_8-a_9 p_9).

It compares this exact vector with the decoded parent; it does not import the reverse-search helper.
It also checks all node keys are distinct, every parent precedes its child, every digit is original, and all original candidates except the seventy exactly excluded ones occur in the path certificate.
Dynamic programming along the parent order gives a maximum verified path length of 25.

Consequently **every actual point of K_8 admits an original {-1,0,1}-digit continuation to zero of length at most 25**.
This is the required compact termination statement.
It does not assert that all 797437 covered candidates belong to K_8 exactly; any further harmless outer candidates have valid paths anyway.

Appending these compact words proves assertion 1.
The floating-point discovery pruning is not a premise: the proof uses the complete containing set, its seventy exact exclusions, and the integer edges connecting every other candidate to zero.

### Reciprocal reachability and infinitude

Reciprocity and irreducibility of P define an automorphism sigma of K=Q(beta) with sigma(beta)=beta^(-1).
Since beta is a unit, sigma(O)=O and sigma^2=id.
Define T(x)=beta^(-1)sigma(x).
This is an additive order-preserving involution in the sense that it preserves the ring's underlying additive lattice; no ordering of real numbers is meant.
Indeed T^2=id.

If y has a continuation to zero with digits eta_1,...,eta_n, then

    y=-sum_(i=1)^n eta_i beta^(-i),
    T(y)=-sum_(i=1)^n eta_i beta^(i-1).

The reversed, negated word (-eta_n,...,-eta_1) takes zero to T(y).
Put

    Omega={x in O: |x_+|<=1, |x_-|<=beta}.

Here beta<2 implies beta<S.
Thus x belongs to the co-return domain of assertion 1.
Moreover

    T(x)_+=x_-/beta,  T(x)_-=beta*x_+,

so T(x) also belongs to that domain.
Its zero continuation gives a path from zero to T(T(x))=x, and x's own continuation then returns to zero.
Hence Omega is contained in the actual return core.

To prove Omega infinite, consider the (N+1)^10 distinct elements sum_(i=0)^9 a_i beta^i with a_i in {0,...,N}.
Distinctness follows from the degree-ten power basis.
Their two real coordinates lie in a rectangle whose side lengths are at most fixed constants times N.
Partition it into half-open cells of widths 1 and beta.
There are at most C(N+1)^2 cells for a fixed C, so one contains at least c(N+1)^8 elements.
Subtracting one chosen element from the others gives that many minus one distinct order elements with |x_+|<1 and |x_-|<beta.
The number tends to infinity, proving assertion 2 even though the chosen occupied cell may vary with N.

### Quantitative continuation length and original probabilities

At every nonzero narrow-domain endpoint with rho(x)<=R, norm integrality and the arithmetic-geometric mean inequality give

    1<=|Norm_(K/Q)(x)|
      =|x_+x_-| product_(j=1)^4 |x(zeta_j)|^2
      <=|x_+| S (rho(x)^2/4)^4
      <=|x_+| S R^8/256.

The root intervals give S<67/10, hence |x_+|>2560/(67 R^8).
If |x_+|<1/2, multiplication by beta for at most K_R zero digits brings its magnitude to at least 1/2; beta>117/100 and the displayed strict lower bound ensure this even at the chosen threshold.
The first crossing is below beta/2<1.
If already in [1/2,1] in magnitude, the zero prefix is empty.
Endpoint neutral radii never increase, so the same R and K_R apply throughout the descent iteration.
Intermediate block radii need not stay below R and are not used in this bound.

Because R^2-N_R delta<64, no more than N_R blocks are needed to enter K_8, including the boundary case R=8.
This uses only nonnegative endpoint square norms and the uniform positive drop.
Each block has at most K_R+11 digits.
A starting point already in K_8 uses no descent block.
The compact certificate adds at most 25 digits, proving assertion 4's length estimate.

Each particular word of length l has original product probability at least 4^(-l).
Following the chosen word forces a hit of zero by time l, so the asserted lower bound holds even if an earlier zero is encountered.
This bound is pointwise uniform over the displayed bounded-radius domain at this fixed beta, not over R or all Salem inputs.
Since N_R=O(R^2) and K_R=O(log R), the displayed growth statement follows.

### Accepted equivalence interface

The hypotheses of [L157](Yin_L_G0157_v1.md) are an actual nontorsion algebraic unit, O=Z[beta], the original alphabet, and actual zero-to-zero states.
They all hold here.
Its accepted equivalences turn the infinite core into the conclusions in assertion 3.
The original ESS source proof is reused only at its already accepted statement-and-applicability scope.
It is not newly proved or re-audited by this computation.
In particular the finite-prime restricted language in L157 must not be substituted for the full core D.

<a id="lehmer-consolidation-provenance"></a>
## Provenance, executed evidence and review boundaries

The substantive assembly is new: [D17](#lehmer-joint-neutral-descent) supplies the actual input and joint word conventions; [D20](#normalized-lehmer-radius-eight) replaces its radius-1500 estimate by the radius-eight normalized convex certificate; [D22](#lehmer-compact-complete-enumeration) supplies complete enumeration and compact termination.
The coordinator contributes the degree-ten reciprocal/pigeonhole bridge and the explicit norm-based length/probability deduction, following the already fixed quartic method in [L169](Yin_L_G0169_v1.md).
This fixed degree-ten theorem was not a conclusion of those earlier partial materials.
The two finite word laws and all embedding conventions have been matched explicitly above.
The sole correction to copied enumeration prose is 'fit within' for the inclusive four-bit coefficient range; no mathematical condition changes.

- [D19/J23](../audits/reviews/Yin_R_G0069_v1.md#lehmer-joint-descent-review) independently reviewed the original Lehmer algebraic input, all full-cell word checks and the older joint-simplex certificate.
  Its scope does not certify the later normalized body.
- [D23/J27](../audits/reviews/Yin_R_G0069_v1.md#normalized-lehmer-radius-eight-review) independently reviewed the new normalized body, all 32 axis certificates, 288 word uses and 217 distinct words, with a separate 300-bit Arb implementation and independently isolated roots.
  The author Fraction verifier was also rerun by the coordinator.
  The radius-eight square drop is independently supported.
- [D24/J28](../audits/reviews/Yin_R_G0069_v1.md#lehmer-compact-enumeration-review) independently checked the containing ellipsoid and complete traversal, including exact integer arithmetic bounds, conservative filters and injective encodings.
  Its separate implementation reproduced all 4818379 nodes, 3077691 leaves and the entire 797507-state output, with identical set and sequence.
  This is stronger than a count comparison.
  The review excludes later paths and exclusions.
- [D25/J29](../audits/reviews/Yin_R_G0069_v1.md#lehmer-path-and-coverage-review) independently verified all 1044588 retained path nodes by exact polynomial coefficient identities, strict parent precedence and complete target-set comparison.
  Independent rational root intervals certify all seventy exclusions.
  Maximum path length is 25.
  That review initially left the present bridge/timing/assembly open for a subsequent complete review.

Numerical discovery was used to propose words, a unimodular basis and paths.
The retained rational enclosures, exact integer traversal/cover and polynomial edge identities support the proof.
No floating-point search-exhaustion result establishes a nonreturn claim.
The computational evidence is conventional checked computation, not a formal proof-assistant proof.
The coordinating author helped with the rational ellipsoid approach and is not an independent reviewer of this assembly.
Separately assigned reviewers disclose their own exact contribution and nonblind arrangement in their findings.

The program and decisive data remain in [J22](../computations/programs/Yin_J_G0022/readme.md), [J24](../computations/programs/Yin_J_G0024/readme.md), [J26](../computations/programs/Yin_J_G0026/readme.md), and the independent review programs [J23](../computations/programs/Yin_J_G0023/readme.md), [J27](../computations/programs/Yin_J_G0027/readme.md), [J28](../computations/programs/Yin_J_G0028/readme.md), [J29](../computations/programs/Yin_J_G0029/readme.md).
Discovery environments and usable checking commands are in those responsible computation readmes.
No existing data are overwritten by this assembly.

The earlier source-method account in L169 remains applicable as methodological context: neutral descent plus a finite residue was motivated by Mercat's different quartic.
No source numerical table is transferred to this degree-ten input, and no novelty or exhaustive-priority claim is made.
This result removes the finite-core alternative for this particular original Salem input and supplies explicit unbounded return arithmetic.
It gives neither a small-M family nor the uniform quantitative estimates needed for unrestricted G0001.
The Task remains active and unresolved.

## From narrow co-return to an exact Salem return-core strip

Date: 2026-10-10.
Deduction by the coordinating AI for Yin, separately reviewed at 2026-10-09T16:22 and adopted with the original-Lehmer assembly.
It uses the completed narrow-domain co-return theorem as an explicit premise; this deduction does not replace its finite certificate.

<a id="exact-salem-return-strip"></a>
### General conditional statement

Let beta be a Salem unit with 1<beta<2 and reciprocal irreducible polynomial of degree d>=4.
Let O=Z[beta], x_+=x(beta), x_-=x(beta^(-1)), B=1/(beta-1) and S=beta B.
Use precisely the operations x -> beta*x+eta with eta in {-1,0,1}.
Suppose every actual x in O with |x_+|<=1 and |x_-|<=S has a finite continuation to zero.
Then the actual zero-to-zero return core is exactly

    D={x in O: |x_+|<B, |x_-|<S}.                 (1)

No condition on the unit-circle embeddings is present in (1).
In particular this is an equality with an actual discrete algebraic strip, not with its real projection or closure.
The narrow co-return premise has been independently supported for the fixed quartic [L169](Yin_L_G0169_v1.md#quartic-infinite-core-theorem), and its complete original-Lehmer assembly is in [D27](#lehmer-infinite-core-theorem).
The separate exact-strip/growth finding below checks this inference and its applicability to both fixed inputs.

### Proof of exactness

First extend the co-return premise to every actual state satisfying |x_+|<B and |x_-|<=S.
If |x_+|<=1, the premise applies directly.
Otherwise put u=|x_+| and choose eta=-sign(x_+).
As long as u>1,

    u'=beta*u-1>0,   u'<u,

because beta>1 and u<B.
The sign does not change during those steps.
The scalar recurrence is u_k=B+beta^k(u_0-B) while this rule continues.
It cannot stay above one indefinitely, since u_0-B<0.
At the first time u_k<=1 it is still positive.
Every original digit preserves |x_-|<=S because beta^(-1)S+1=S.
The finite prefix ends in the narrow co-return domain; its neutral coordinates may have increased but remain finite.
Appending the assumed continuation proves generalized co-return.
The proof never requires the neutral radius to stay below its initial value during this greedy prefix.

The reciprocal automorphism sigma(beta)=beta^(-1) preserves O.
The map T=beta^(-1)sigma is an additive involution with

    T(x)_+=x_-/beta,   T(x)_-=beta*x_+.

If y reaches zero with eta_1,...,eta_n, then y=-sum eta_i beta^(-i), so the reversed negated word takes zero to T(y).
For x in the right-hand side of (1), both x and T(x) satisfy generalized co-return.
A zero continuation of T(x) therefore yields reachability of x from zero, and x's own continuation completes a true return.
This proves sufficiency.

For necessity, a state x reached from zero in a digits satisfies

    |x_-|<=sum_(j=0)^(a-1) beta^(-j)
           =S(1-beta^(-a))<S

when a>0; the empty word gives x=0 and the same strict strip membership.
A continuation from x to zero in b>0 digits gives

    |x_+|<=sum_(j=1)^b beta^(-j)
           =B(1-beta^(-b))<B;

if b=0 then x=0.
Every actual returning state thus lies in the displayed open strip.
This proves (1), including the strict boundaries.

For both fixed polynomials P(t)=t^4-t^3-t^2-t+1 and P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, P(1)=-1.
Therefore beta-1 is an algebraic unit and B belongs to O.
Its two real values are B and -S.
The states +/-B are actual lattice points on the boundary, but neither can lie in D by the necessity just proved.
Injectivity of either real embedding shows that these are the only actual O elements on any of the four boundary lines of the closed natural strip.
Thus replacing both strict inequalities by weak ones adds exactly these two states for these two fixed inputs.
This last observation is not needed for (1).

<a id="return-core-neutral-growth"></a>
### A quantitative geometric consequence at fixed input

Write r=(d-2)/2, z_j=x(zeta_j), and rho(x)^2=sum_(j=1)^r |z_j|^2.
Under the same co-return premise, let D_R={x in D:rho(x)<=R}.
There are input-dependent constants c,C,R_0>0 such that

    c R^(d-2)<=|D_R|<=C(R+1)^(d-2)  for R>=R_0.    (2)

For the upper bound, the full embedding of O in R^d is a lattice.
Choose a positive radius epsilon so the Euclidean epsilon-balls about distinct lattice points are disjoint.
Balls about points of D_R lie in a cylinder whose first two coordinate widths are fixed (enlarged by 2epsilon) and whose neutral radius is at most R+epsilon.
Comparing d-dimensional volumes proves the upper estimate.
This uses the complete embedding, not a discreteness claim for the two-real projection.

For the lower bound, use the (N+1)^d distinct coefficient-box elements sum_(i=0)^(d-1) a_i beta^i, a_i in {0,...,N}.
Their two real values lie in a rectangle of side lengths O(N).
Partition into half-open cells of widths 1 and beta.
Some cell contains at least c_0(N+1)^(d-2) distinct elements.
Subtract a selected element from every other element in this cell.
The resulting states have |x_+|<1 and |x_-|<beta, so they belong to D by reciprocal co-return, since beta<2 implies beta<S and 1<B.
Each difference has power-basis coefficients of magnitude at most N; hence every neutral modulus is at most dN and rho<=d sqrt(r) N.
Taking N=floor(R/(d sqrt(r))) and adjusting constants yields the lower bound for every sufficiently large R.
Distinctness survives subtraction.

For the original degree-ten Lehmer input, (2) gives growth of order R^8; for the quartic it gives order R^2.
The constants are fixed-input constants.
This statement quantifies state counts, not counts of words or their original probabilities.
It does not imply a return-probability estimate, a degree-uniform bound, or a positive Mahler gap.
No probabilistic local limit theorem or spectral conclusion is assumed.

### Contribution, review and continuation

The coordinator supplied the greedy strip extension, exact necessary/sufficient strip identity, boundary-state observation and elementary two-sided geometric count.
These are new deductions from the explicitly identified narrow co-return premise.
The separately assigned reviewer checked them without contributing to their proof; its complete finding is preserved below.
The coordinating adoption here does not change the earlier fixed quartic material or automatically inherit its review for this new deduction.
The narrow-domain certificate remains the substantive arithmetic input.
A general Salem claim would still have to establish it for each asserted input class.
The next useful work concerns what quantitative information this exact core geometry adds about complete weighted returns, rather than merely counting a larger finite sample of reachable states.

<a id="lehmer-fixed-retention"></a>
## Fixed retention, adoption and preserved versions

This fixed-retention operation was prepared at 2026-10-09T16:24 under the coordinating AI for Yin's prior direction to adopt and retain the final checked original-Lehmer assembly and exact-strip/growth strengthening.
The independently assigned structural reviewer implements that coordinating decision.
This is not a new proof contribution, personal human inspection, C acceptance decision or Task completion.
G0001 remains active and unresolved.

The current proof above is the final corrected D G0027 assembly, and the conditional strengthening is D G0028.
The exact four-item theorem keeps its narrow real-strip and bounded-radius timing hypotheses and explicitly excludes zero in its prime-support assertion.
The new strip/growth theorem applies to the quartic already proved in L G0169 as well as to this original Lehmer input, but the old fixed L169 body remains unchanged.
The general theorem still requires its explicitly stated narrow co-return premise.

The following historical appendices preserve the original dated derivations and all substantive review findings.
Their earlier pending/open/no-adoption statements describe their actual dates, not the current outcome.
In particular the radius1500 simplex result and the poor initial radius around59923 remain useful discovery history; they are not additional current premises for the radius-eight proof.
The normalized-body and compact-input derivations are preserved as the exact targets of their component reviews, not separate live working proofs.
The original inclusive-encoding wording objection and the later nonzero-state clarification remain visible together with their resolutions.

| Retired working identity | Preserved exact scope/home |
| --- | --- |
| D G0017 | [Historical radius1500 proof, discovery and limits](#historical-lehmer-radius1500) |
| D G0019 | [Full original partial-descent review](../audits/reviews/Yin_R_G0069_v1.md#lehmer-joint-descent-review) |
| D G0020 | [Original normalized-body component](#normalized-lehmer-radius-eight) |
| D G0022 | [Original complete enumeration](#lehmer-compact-complete-enumeration) and [later compact paths](#lehmer-compact-exact-zero-continuations) |
| D G0023 | [Full normalized-body review](../audits/reviews/Yin_R_G0069_v1.md#normalized-lehmer-radius-eight-review) |
| D G0024 | [Full independent enumeration review](../audits/reviews/Yin_R_G0069_v1.md#lehmer-compact-enumeration-review) |
| D G0025 | [Full review history](../audits/reviews/Yin_R_G0069_v1.md#lehmer-full-review-history), including [path/exclusion](../audits/reviews/Yin_R_G0069_v1.md#lehmer-path-and-coverage-review), [whole-chain](../audits/reviews/Yin_R_G0069_v1.md#lehmer-complete-chain-review) and [strip/growth plus final clarification](../audits/reviews/Yin_R_G0069_v1.md#exact-strip-growth-review) |
| D G0027 | [Current exact theorem](#lehmer-infinite-core-theorem) and [complete proof](#lehmer-infinite-core-proof) |
| D G0028 | [Conditional exact strip](#exact-salem-return-strip) and [state growth](#return-core-neutral-growth) |

All seven computation groups J G0022/J G0023/J G0024/J G0026/J G0027/J G0028/J G0029 retain their necessary programs, certificates and mathematical outputs.
Only navigation and current adoption status are adjusted during retention.
The mathematical derivations and dated findings are preserved with their original contributor and nonblind-review disclosures.
No old result is relabelled as independently checked beyond the stated input scope.

<a id="historical-lehmer-radius1500"></a>

**Preserved original dated D G0017 mathematical component.** The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Joint neutral blocks for the original Lehmer input

Date: 2026-10-09.
Fourth bounded G0001 orbit round under the coordinating agent's 2026-10-09T15:34 shared usage gate.
Earlier quartic proof materials remain frozen for separate review.

### Question

For P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1 and its real Salem root beta>1, test legal original-digit blocks over one or several expanding cells.
Retain all four unit-circle conjugate pairs together as an eight-dimensional real vector.
Seek a joint displacement convex hull containing a neighborhood of zero, which would support genuine simultaneous neutral descent.
Pairwise projected containment alone is insufficient.

### Reuse and limits

This directly continues the neutral-block method and finite-certificate contract of [fixed quartic descent](Yin_L_G0169_v1.md#quartic-neutral-descent) and its completed quartic residue in [fixed compact certificate](Yin_L_G0169_v1.md#quartic-compact-termination).
The prior source screen and unchanged method are reused; no repeated broad literature search is needed.
This new domain requires its own blocks and joint geometry.
Numerical discovery, an exact certificate, a whole real-interval cover, and an infinite actual Lehmer core are separate outcomes.

<a id="lehmer-joint-neutral-descent"></a>
### 1. Obtained fixed-input joint descent

Let beta>1 be the real expanding root of P, beta^(-1) its contracting root, and zeta_1,...,zeta_4 the roots in the upper half-plane, ordered by real part.
For an actual x in Z[beta], write x_+,x_- for its two real embeddings and z=(x(zeta_1)...,x(zeta_4)).
Use the complete Euclidean neutral norm

    rho(x)^2=sum_(j=1)^4 |x(zeta_j)|^2.

Set S=beta/(beta-1), B=1/(beta-1).
The original operation is x -> beta*x+eta with eta in {-1,0,1}.

**Partial theorem supported by the exact certificate.** Every actual x satisfying

    |x_+|<=1, |x_-|<=S, rho(x)>=1500

has an original-digit finite continuation to an endpoint x' with

    |x'_+|<1, |x'_-|<=S,
    rho(x')^2 <= rho(x)^2-5589/1000.

The continuation consists of finitely many zero digits followed by at most eleven digits.
All intermediate states stay in |x_+|<B, |x_-|<=S.
Iterating reaches the finite compact residue

    K_L={x in Z[beta]: |x_+|<=1, |x_-|<=S, rho(x)<1500}.

This statement uses all eight real neutral coordinates jointly.
It does not yet prove K_L -> 0 or an infinite actual core for the Lehmer input.

### 2. Input and root certificate

The trace identity is

    P(t)=t^5 Q(t+t^(-1)),
    Q(u)=u^5+u^4-5u^3-5u^2+4u+3.

[J G0022](../computations/programs/Yin_J_G0022/readme.md) checks this identity by integer Laurent expansion.
It checks Q's irreducibility modulo two: Q mod 2 divides u^32-u and has neither 0 nor 1 as a root.
Because five is prime, these checks establish the standard finite-field criterion explained in [L G0004, Section 9](Yin_L_G0004_v1.md).
Thus Q is irreducible over Q.
One of its real embeddings lies in (-2,2), so u^2-4 is negative there and is not a square in Q(u).
Adjoining a root of t^2-ut+1 therefore doubles the degree, proving the degree-ten irreducibility needed for the actual field embeddings.
This reuses L G0004's trace argument rather than a new irreducibility principle.

Five disjoint rational brackets, each with opposite endpoint signs, isolate Q's five roots:

    (-19/10,-18/10), (-15/10,-14/10), (-6/10,-5/10),
    (9/10,1), (2,21/10).

Degree five and five sign changes account for every root, one per bracket.
Rational bisection and integer-square-root enclosures give beta in (117/100,118/100) and the four upper unit roots via

    Re(zeta_j)=u_j/2, Im(zeta_j)=sqrt(1-u_j^2/4)>0.

Consequently beta is the original degree-ten Salem unit, and all ten real embedding coordinates form a full lattice image of Z[beta].
The program does not rely on its numerical discovery roots for this argument.

### 3. Fifty cells and seventeen reusable joint simplices

For a word w=(eta_1,...,eta_k), define the joint complex displacement

    c_w=(sum_(i=1)^k eta_i zeta_j^(-i))_(j=1)^4,

viewed as the vector (Re c_1,...,Re c_4,Im c_1,...,Im c_4) in R^8.
The endpoint neutral vector is the coordinatewise rotation

    (zeta_j^k (z_j+c_(w,j)))_(j=1)^4,

which preserves its complete Euclidean norm.
No individual projected pair is substituted for this joint vector.

The saved table covers every I_a=[a/100,(a+1)/100], a=50,...,99.
Each cell carries nine original words, all of length at most eleven.
Every one maps the complete closed expanding cell strictly into (-1,1).
The nine corresponding joint vectors form an eight-dimensional simplex containing zero strictly in its interior.
Reuse across cells reduces fifty originally selected simplices to seventeen distinct simplices, with 450 block uses across the final table.

For each simplex, form the 9 by 9 matrix with columns (c_w,1).
The exact interval verifier encloses its inverse by outward-rounded rational Gauss--Jordan elimination, checking every division excludes zero.
A row of this inverse gives an affine barycentric function lambda_i(y)=g_i.y+b_i.
It verifies b_i>0 and obtains a ball radius lower bound

    r_a <= min_i b_i/||g_i||.

It separately bounds m_a>=max_w ||c_w||^2 and verifies, cell by cell,

    3000*r_a-m_a >=5589/1000.

For any z in R^8, the contained ball supplies a vertex with z.c_w<=-r_a||z||.
Therefore, when rho=||z||>=1500,

    ||z+c_w||^2 <= rho^2-2*r_a*rho+m_a
                   <=rho^2-5589/1000.

This proves descent for x_+ in [1/2,1].
Negative cells are covered by negating state and digits.
If 0<|x_+|<1/2, prepend zeros until the first crossing of 1/2; it lies below beta/2<1, leaves rho unchanged, and shrinks |x_-|.
An actual algebraic state with x_+=0 is zero, so it cannot have rho>=1500.
The contracting strip is invariant digit by digit because beta^(-1)S+1=S.
Backward estimation from the final narrow expanding endpoint gives the full intermediate bound |x_+|<B, exactly as in D G0013.

Repeated descent reaches K_L because each block reduces a nonnegative squared norm by a fixed positive amount.
K_L is finite since every one of the ten real embedding coordinates is bounded.
Neither the finiteness proof nor the block table supplies paths from those remaining points to zero.

### 4. What the experiment changed, and its cost

The first three numerical pilot cells, at expanding coordinates near 0.50, 0.75 and 0.99, all admitted genuine nine-vertex joint simplices from words of length at most eleven.
The full fifty-cell search then succeeded everywhere.
Thus there is no joint-direction separation obstruction for the retained finite block model on this domain: the exact certificate positively constructs the needed neighborhoods of zero.

The first arbitrary LP-selected simplices had a worst sufficient neutral radius around 59923, caused by a barycentric coefficient near zero.
Reusing those same integer simplices on every cell where all their words remained legal reduced the worst numerical threshold to about 1326, and the exact verifier proves the convenient common threshold 1500.
This improvement changes the geometry certificate, not the allowed word length.
The threshold is not asserted optimal, and a poorly placed simplex is not evidence of an intrinsic obstruction.

The residual now has eight real neutral coordinates and radius 1500, rather than the quartic's two neutral coordinates and radius ten.
No large compact enumeration was attempted.
The exact joint result is a useful advance, but the retained threshold makes a direct residual enumeration an unattractive next operation before improving the descent region or the termination mechanism.

Useful next tests are to optimize a common multi-vertex convex body or a rotation-invariant weighted norm, reduce the threshold while preserving exact joint coverage, or find a structural continuation scheme for the remaining high-dimensional residue.
Any changed norm must control all four pairs together and remain compatible with their independent rotations.
Existence of chosen paths remains separate from a useful full original-law tail estimate, and this fixed input supplies no uniform family near measure one.

### 5. Verification and review state

Discovery used NumPy/SciPy linear programming; integer word arrays were retained.
The final verifier uses only standard-library integers and Fractions, with every arithmetic operation rounded outward on denominator 10^40.
It ignores the saved numerical roots, weights, residuals and radii.
It checks the trace identity/domain, all 450 full-cell block images, all seventeen joint simplex inverses and all fifty descent margins.
It ran successfully and returned the exact lower bound 5589/1000.

This is an author-implemented separate exact verifier of a numerical discovery.
Independent review is pending; the earlier quartic reviews do not transfer automatically to it.
No compact termination, infinite actual Lehmer core, fixed promotion, literature novelty or G0001 gap conclusion is asserted.

<a id="preserved-d0020"></a>

**Preserved original dated D G0020 mathematical component.** The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Normalized joint displacement bodies for Lehmer descent

Date: 2026-10-09.
Fifth bounded G0001 orbit round under the coordinating agent's 2026-10-09T15:47 usage gate.
D G0017/J G0022 remain frozen for separate review.

### Structural question

For a legal joint neutral displacement c, descent of squared Euclidean norm is equivalent to 2 z.c+||c||^2<0.
Thus the convex hull of c/||c||^2, with c nonzero, directly compares directional gain to displacement cost.
Test a finite many-vertex body via contained coordinate cross-polytopes, instead of a single nine-vertex simplex followed by a global maximum-cost bound.
This may cut the retained Lehmer radius without increasing word length or enumerating the high-dimensional compact residue.

### Evidence contract

Retain all original integer blocks.
Numerical linear programs may discover convex representations; an accepted gain needs exact root intervals and exact positive barycentric certificates.
All eight real neutral coordinates remain joint.
The earlier source screen and root/domain contracts are reused.
Infinite actual core without complete compact termination remains a separate possible argument, not a premise.

<a id="normalized-lehmer-radius-eight"></a>
### 1. Radius eight with the unchanged original blocks

Use the original Lehmer field, its four upper unit-circle roots, both real embeddings and the complete Euclidean neutral norm rho from [D G0017](#lehmer-joint-neutral-descent).
The new finite certificate proves the following stronger partial descent statement:

    |x_+|<=1, |x_-|<=S=beta/(beta-1), rho(x)>=8

implies there is an original-digit continuation, consisting of finitely many zeros followed by at most eleven digits, to x' satisfying

    |x'_+|<1, |x'_-|<=S,
    rho(x')^2<=rho(x)^2-57/100.

All intermediate states satisfy |x_+|<1/(beta-1) and |x_-|<=S.
Thus the original Lehmer dynamics reduces to the finite compact residue

    K_8={x in Z[beta]: |x_+|<=1, |x_-|<=S, rho(x)<8}.

The neutral cutoff drops from 1500 to eight without increasing the eleven-digit limit.
The mechanism changes from one poorly centered simplex to a normalized many-vertex convex body.
No compact enumeration, compact termination or infinite actual Lehmer core follows solely from this result.

### 2. Why normalization measures the correct cost

For a legal word w, let c_w be its complete eight-real-dimensional neutral displacement as defined in D G0017.
Its endpoint rotation preserves Euclidean norm.
For c_w nonzero, set

    u_w=c_w/||c_w||^2.

Then the exact squared-norm change is

    ||z+c_w||^2-||z||^2
       =||c_w||^2 (1+2 z.u_w).

Suppose the convex hull of the retained u_w contains the radius-r Euclidean ball around zero.
For every nonzero z, some retained vertex satisfies z.u_w<=-r||z||, because the hull contains -r z/||z||.
If every retained ||c_w||^2>=m>0 and ||z||>=R with 2rR>1, this gives

    ||z+c_w||^2-||z||^2 <=-m(2rR-1).

This uses each word's own cost in its normalized vector.
It avoids bounding all displacement costs by the largest one before choosing a direction.
Both the positive denominator and the strictly positive minimum displacement cost are proved by the exact certificate.

### 3. Two cells, thirty-two exact axis certificates

[J G0024](../computations/programs/Yin_J_G0024/readme.md) retains two complete closed expanding cells:

    I_1=[1/2,3/4], I_2=[3/4,1].

Every saved word maps its entire assigned cell strictly into (-1,1).
For each of the sixteen signed coordinate vectors +/-e_i in R^8, the computation saves nine original words and proves that the corresponding normalized vertices have a convex combination equal to +/-t e_i, where

    t_1=101/500, t_2=207/1000.

It certifies each combination by enclosing the inverse of the augmented 9 by 9 vertex matrix and proving all resulting exact barycentric coordinates are strictly positive.
The saved numerical LP weights are ignored.
Therefore the full convex hull contains the coordinate cross-polytope {y:||y||_1<=t}, hence the Euclidean ball of radius t/sqrt(8).

There are 288 word uses in the thirty-two certificates and 217 distinct integer words.
No word is longer than eleven digits.
All normalized vectors have nonzero, positively bounded squared denominators.
The exact cell-specific minimum squared costs are at least 3999/1000 and 873/250.
With R=8, the certified drops are at least 57/100 and 597/1000 respectively, so 57/100 is a uniform bound.
These are rational lower bounds; neither an approximate LP optimum nor a floating-point containment test is a proof premise.

Negative cells are obtained by negating x and every digit.
For 0<|x_+|<1/2, prepend zeros until its first crossing of 1/2.
This terminates for every nonzero actual algebraic state and lands below beta/2<1, preserving rho and contracting |x_-|.
If x_+=0 then x=0 and rho=0, outside the descent case.
The digitwise stable bound beta^(-1)S+1=S and the backward endpoint estimate for the expanding strip are exactly those already proved in D G0017.
Repetition lowers a nonnegative squared norm by at least 57/100 per block and therefore reaches K_8 in finitely many blocks.
No claim of a bounded number of zero-prefix digits independent of the initial state is made.

### 4. What is established and what remains

This discriminating experiment establishes that much of the previous radius cost was caused by the convex certificate's treatment of displacement costs.
A joint normalized many-vertex body improves the certified cutoff by a factor 187.5, with fewer real cells and unchanged maximum word length.
No weighted norm was needed for this gain.
A pairwise projection argument would still be insufficient; all thirty-two axis targets belong to the same complete eight-dimensional vector space.

The next operation is an enumeration-feasibility assessment using exact embedding inverse coefficient bounds and a clearly labelled volume/covolume diagnostic.
Neither such a size estimate nor paths for selected reachable states will prove complete K_8 termination.
An alternative proof using an infinite invariant subset would need both original reachability and finite co-return for that subset.
These remain distinct possible routes.

### 5. Reuse and review status

The normalized convex identity is derived above.
Its finite certificate reuses the unchanged exact root and interval primitives of J G0022, including trace irreducibility, root isolation and outward Fraction Gauss--Jordan operations.
No prior certificate or mathematical text was modified.
The new verifier recomputes every denominator, every full-cell word image and every positive barycentric representation from integer words.
It ran successfully using only standard-library exact arithmetic.

The author's numerical discovery and exact verifier are separate programs, but both were written by the same agent.
Independent review of this normalized-body argument and its new certificate is pending.
Earlier independent reviews do not transfer automatically.
No fixed promotion or unrestricted G0001 result is asserted.

<a id="preserved-d0022"></a>

**Preserved original dated D G0022 mathematical component.** The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.

## Lehmer radius-eight compact residue: feasibility and exact enumeration

Date: 2026-10-09.
Authorized follow-on under the coordinating agent's 2026-10-09T15:52 shared usage gate.
The normalized geometry [D G0020](#normalized-lehmer-radius-eight) and its programs remain frozen for review.

### Scope

Assess the complete compact K_8: exact inverse-embedding coefficient bounds, actual discriminant, and a labelled volume/covolume size diagnostic.
Proceed to a bounded complete enumeration only if a concrete algorithm and budget are feasible.
Dense-box failure or a search cap is not a mathematical nonreturn result.
Any subsequent path certificate must cover a rigorously complete finite superset.

### Evidence plan

All new programs belong in a fresh J.
Reuse the exact Lehmer roots and domain.
Use lattice reduction or branch pruning only with an explicit completeness argument and exact or conservative arithmetic.
No unrestricted enumeration or original-law tail conclusion is presumed.

<a id="lehmer-compact-complete-enumeration"></a>
### 1. Exact bounds and finite-size assessment

[J G0026](../computations/programs/Yin_J_G0026/readme.md) gives a certified finite superset of K_8 with **797507 distinct states**.
The complete enumeration ended normally, below both explicit caps, after 4818379 recursion nodes and 3077691 ellipsoid leaves.
These figures are actual retained run results, not estimates.

First, the inverse of the ten-real-coordinate embedding matrix gives the necessary power-basis bounds

    |a_i| <= (7,6,7,7,6,5,5,5,5,6)_i,
    x=sum_(i=0)^9 a_i beta^i.

For each inverse row A_i, the bound used is

    |a_i| <= |A_(i,0)|+S |A_(i,1)|
                  +8 sqrt(sum_(j=2)^9 A_(i,j)^2).

This is verified by outward rational interval inversion of the full embedding matrix.
Its dense integer box has 108561184875 tuples and was not traversed.

The exact polynomial discriminant, computed by a fraction-free Sylvester determinant, is 1332031009=36497^2.
Thus the real-coordinate embedding covolume is 36497/16.
The cylinder volume/covolume diagnostic predicts about 796777 states, and the ellipsoid chosen below about 3055602.
Those predictions motivated the algorithm and are not completeness or runtime bounds.

### 2. Certified containing ellipsoid in a reduced integer basis

Let S_0=67/10; the exact root intervals give S<S_0.
Define the weighted embedding Y by multiplying x_+ by sqrt(8), x_- by sqrt(8)/S_0, and leaving the eight real neutral coordinates unchanged.
Every point of K_8 satisfies

    ||Y(x)||^2=8 x_+^2+8 x_-^2/S_0^2+rho(x)^2 <=80.

The positive weighting is only an enumeration device.
It does not change the dynamical norm or the earlier descent claim.

Let B be the retained integer matrix approximating the row basis for Y at scale Q=10^8.
From the proved coefficient bounds, the exact checker bounds each coordinate of aB/Q-Y(x), then bounds its Euclidean norm by epsilon_B.
A computationally discovered integer basis transformation U is verified exactly to have determinant +/-1, and the reduced integer basis is U B.
Write a=bU.
Exact inversion of U gives necessary integer bounds for b; no LLL performance property is assumed in the proof.

The rational Gram matrix (UB)(UB)^T/Q^2 has an exact positive LDL^T decomposition.
If T_true=L sqrt(D), then ||b T_true||=||aB/Q||.
The retained lower triangular integer matrix T approximates T_true at scale H=10^5.
Using the necessary b bounds, the checker bounds ||b T/H-b T_true|| by epsilon_T.
It therefore proves

    ||b T||^2 <= H^2 (sqrt(80)+epsilon_B+epsilon_T)^2
                 <=800554833912.

The displayed right-hand side is an integer upper bound checked from exact Fractions; the saved decimal errors are not premises.
The exact certificate's nontrivial approximation steps are accounted for by these two additive norm errors.
The unimodular matrix, original and transformed coefficient bounds, triangular matrix, root-based coordinate bounds, and integer squared radius are all retained in the certificate file.

### 3. Complete bounded traversal and conservative filtering

For lower triangular T with positive diagonal,

    ||bT||^2=sum_(j=0)^9 (b_j T_(j,j)+sum_(i>j) b_i T_(i,j))^2.

The compiled traversal assigns b_9,b_8,...,b_0.
At each step the already assigned tail fixes a center and the remaining integer squared budget.
An integer square root, corrected by exact integer comparisons, and signed floor/ceiling division enumerate every integer b_j meeting the remaining bound.
The necessary transformed coefficient bounds only remove impossible original K_8 points.
Each full b maps bijectively to a=bU because U is unimodular.

After a full assignment, the program checks the proved original coefficient box.
It then uses outward integer-scaled intervals for all ten original embeddings.
A point is discarded only if its expanding interval misses [-1,1], its contracting interval misses a certified outer bound for [-S,S], or the sum of the lower bounds for the eight neutral coordinate squares is at least 64.
The last test is consistent with K_8's strict rho<8 inequality.
Ambiguous boundary points are retained.
Therefore every actual point of K_8 appears in the output.

The program uses checked signed 64-bit integer arithmetic.
A separate exact checker recomputes the basis/ellipsoid enclosure, verifies unimodularity, coefficient bounds, outward embedding filters, and sufficient integer-size bounds.
The retained run completed normally with no overflow or cap event.
Its caps were 50000000 recursion nodes and 2000000 retained candidates; encountering either would have marked the result incomplete.

Each retained state is packed as a little-endian uint64, with nibble i equal to a_i+8.
The proved coefficient bounds lie strictly within that encoding's range.
The checker verifies file length, every decoded coefficient range and all 797507 states are distinct.
The binary contains a complete finite superset of K_8, not a claim that every boundary-ambiguous retained state lies in K_8 exactly.

### 4. Responsibility and next obligation

The author developed and checked the certificate preparation, integer traversal and separate rational certificate checker.
The coordinator independently suggested the same general rational-ellipsoid/unimodular-reduction strategy while this round was in progress; that algorithmic contribution is acknowledged.
The retained weighting and explicit triangular rounding enclosure were supplied by the orbit researcher.
This is not a claim that the two implementations were written by independent agents.

The enumeration chain is frozen for a separately assigned noncontributor review.
Its trusted mathematical inputs are the earlier exact root/interval primitives and the explicit linear algebra and enclosure proof above.
The LLL implementation supplies only a candidate unimodular matrix whose validity is subsequently checked exactly.

No path to zero is supplied by completeness alone.
The next bounded operation is an original-digit reverse search, allowing intermediate states outside K_8 if necessary, followed by exact path checks covering every retained candidate.
A cap or uncovered state will be reported as inconclusive unless a separate rigorous obstruction is proved.

<a id="lehmer-compact-exact-zero-continuations"></a>
### 5. Complete compact termination, with explicit outer-superset exclusions

Added on 2026-10-10 after freezing the enumeration in Sections 1--4.
The original 797507-state enumeration was unchanged by that addition.

A bounded reverse search discovered paths to zero for 797437 of those candidates.
It allowed the larger necessary expanding strip |x_+|<=1/(beta-1), the contracting strip |x_-|<=S and a numerical neutral radius-eight cutoff.
Thus it did not require intermediate states to stay in K_8's narrow expanding strip.
It exhausted its selected graph after 4003565 states, below the 6000000-node cap; it left seventy candidate states uncovered.
None of those numerical pruning or exhaustion facts is used to prove nonreturn or membership.

Every uncovered candidate was then checked with the full exact rational embedding intervals, separately from the coarse integer intervals used for enumeration.
Sixty-eight have a certified lower bound rho^2>=64, and two have contracting real embedding outside [-S,S].
Therefore all seventy lie outside the actual K_8.
They remain part of the earlier conservative superset and are not silently reclassified as an earlier enumeration error or as nonreturning states.

The retained ancestry certificate consists of 1044588 distinct algebraic states and one original digit/parent edge for each nonzero node.
Its two binary parts store a 50-bit state key, a parent index and the digit code.
A state coefficient a_i is the key's five-bit field i minus sixteen; the stored digit code minus one is in {-1,0,1}.
Node zero is exactly the zero state with its harmless zero self-reference.
Every later node has a strictly smaller parent index, so all parent chains are acyclic and terminate at zero.

The separate Python verifier checks every edge with integer arithmetic.
For P(t)=sum_(i=0)^10 p_i t^i, p_0=p_10=1, the forward recurrence is

    (a_0,...,a_9) -> (eta-a_9, a_0-a_9 p_1, ..., a_8-a_9 p_9).

It compares this exact vector with the decoded parent; it does not import the reverse-search helper.
It also checks all node keys are distinct, every parent precedes its child, every digit is original, and all original candidates except the seventy exactly excluded ones occur in the path certificate.
Dynamic programming along the parent order gives a maximum verified path length of 25.

Consequently **every actual point of K_8 admits an original {-1,0,1}-digit continuation to zero of length at most 25**.
This is the required compact termination statement.
It does not assert that all 797437 covered candidates belong to K_8 exactly; any further harmless outer candidates have valid paths anyway.

### 6. Scope of the completed compact input

Combining Section 5 with the normalized descent of D G0020 yields finite co-return for every actual x in Z[beta] satisfying |x_+|<=1 and |x_-|<=S, without a neutral bound.
The broader reachability/pigeonhole argument and any original-law quantitative interpretation are separate deductions, to be assembled and reviewed with the full chain.
This draft supplies the exact compact input, not a uniform Lehmer gap.

The path discovery used floating-point region tests to choose candidate edges.
The retained integer edge checks, complete target coverage and exact exclusions establish the conclusion independently of those tests.
The seventy exclusions and all 1044588 ancestry nodes were actually verified on 2026-10-10.
The author wrote both discovery and verification programs, so this is not an independent-agent review.
The separately assigned completeness review of Sections 1--4 does not automatically extend to these new path sections; their independent review remains pending.

<a id="preserved-d0019"></a>

**Preserved original dated D G0019 review history.** The following account retains its historical findings, pending statements, contributor relationship and actual inspected scope; current disposition is stated above.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0069_v1.md#finding-no-defect-in-the-stated-partial-theorem), with its original inspected scope and relationship.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0069_v1.md#exact-axis-certificates-and-reproduction), with its original inspected scope and relationship.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0069_v1.md#lehmer-compact-enumeration-review), with its original inspected scope and relationship.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0069_v1.md#execution-and-current-scope), with its original inspected scope and relationship.
