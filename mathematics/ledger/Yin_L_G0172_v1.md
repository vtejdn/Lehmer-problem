---
author: Yin
---
# Full-strip original-law operator norms and a certified quartic two-step gain

Date: 2026-10-10, Asia/Hong_Kong.
Current reusable statements and complete arguments belong to [C203](../claims/Yin_C_G0203_v1.md#statement), and the formal collaborator finding belongs to [R495](../audits/reviews/Yin_R_G0495_v1.md#reciprocal-kernel-collaborator-review).
The dated proof body remains the original inspected input of R_G0071, with its historical adoption and pending wording interpreted at that date.
Those historical descriptions supply no current Task execution authority.
Fixed retention and adoption authorized by the coordinating AI for Yin after the complete noncontributor reviews of the qualitative operator argument and the quartic exact certificate.

For every Salem beta in (1,2), the original full-strip operator has the exact one-step and essential norm lambda_N=cos^2(pi/(2(N+1))), N=ceil(2/(beta-1)), and strictly smaller two-step norm than lambda_N^2.
For the specified quartic, the full exact phase certificate and an actual algebraic lower witness give sqrt(96)/16 < ||K^2|| <= sqrt(97)/16.
The complete hypotheses, proofs and original-law probability interfaces follow below.
The two-step probability corollary is weaker than the already retained L30 diagonal estimate; no best-known entropy improvement or uniform Mahler gap is asserted.

The original dated contribution and review accounts are preserved.
Earlier pending/no-adoption wording inside those historical findings states their actual inspection boundary, not the current disposition.
The general co-return identification and the equality of spectral radius with a diagonal rate are not silently imported into the operator argument.

## Contents

- [General full-strip operator convention](#full-strip-operator-statement), [exact one-step norm](#reciprocal-kernel-fiber-norm), [essential norm and equality profiles](#reciprocal-kernel-essential-norm), and [strict two-step loss](#reciprocal-kernel-two-step-loss).
- [Original complete collaborator check](#reciprocal-kernel-collaborator-review) and [original noncontributor review account](../audits/reviews/Yin_R_G0071_v1.md#reciprocal-kernel-independent-review).
- [Quartic quantitative statement](#quartic-two-step-certified-bound) and [complete finite-phase proof](#quartic-two-step-proof).
- [Complete quantitative review history](#quartic-two-step-review-history) and [original final frozen-input finding](../audits/reviews/Yin_R_G0803_v1.md#quartic-two-step-independent-review).

## Reciprocal symmetrization and exact original-law operator norm

Date: 2026-10-10.

Existing fixed input certificates are unchanged.
The coordinator proposed the edge-reversing reciprocal involution; this material develops its operator consequences.

<a id="full-strip-operator-statement"></a>
### Input and question

Use the original digit law p_0=1/2, p_1=p_(-1)=1/4 and the exact actual return-core strip retained with its full hypotheses in [L170](Yin_L_G0170_v1.md#exact-salem-return-strip).
For a Salem unit beta in (1,2), put O=Z[beta], B=1/(beta-1), S=beta B, and D={x in O: |x_+|<B, |x_-|<S}.
The operator calculation below is valid for this strip whether or not a general beta's strip has yet been identified with its actual core.
For the two certified fixed inputs it applies to the entire actual core.

Let sigma(beta)=beta^(-1), T(x)=beta^(-1)sigma(x), and (Uf)(x)=f(Tx).
On counting-measure l2(D) define

    (Kf)(x)=sum_eta p_eta 1_D(beta*x+eta) f(beta*x+eta).

The task is to extract quantitative information for this unchanged weighted operator, while distinguishing its norm from its spectral radius and its diagonal return probabilities.

### Reuse and search scope

Read the fixed original-law convention and full-tail boundary in [L154](Yin_L_G0154_v1.md#actual-first-return-paths), the restricted unit-kernel construction in [L156](Yin_L_G0156_v1.md#actual-unit-sojourn-tail), and the [quadratic drift obstruction](Yin_L_G0176_v1.md#original-law-quadratic-drift-obstruction).
A local search of G-ledger kernel/norm material and literature registry did not supply the present full-strip fiber calculation.
A bounded primary-source search on 2026-10-10 for Salem/Bernoulli transition-operator spectral radius and tridiagonal Toeplitz eigenvalues located the standard matrix formula in [NPR13](../literature/pdf/NPR13.pdf), author manuscript Section2, equations(4),(7), printed pp.2-3 / PDF pp.3-4.
The retained author manuscript and published journal identity are distinguished in its [scoped reading record](../audits/literature/NPR13/readme.md).
This is attribution for the ordinary finite-matrix sine eigenvectors, not a new external Salem premise.
Source registration, bounded acquisition and local title/formula validation are complete.
No novelty claim is made.

<a id="reciprocal-kernel-fiber-norm"></a>
### 1. Edge reversal and finite integer-translation fibers

The additive involution T preserves D: its two real coordinates are x_-/beta and beta*x_+.
It preserves each neutral modulus as well.
For an actual edge y=beta*x+eta,

    T(x)=beta*T(y)-eta.

Because p_eta=p_(-eta), this gives K*=UKU, with U*=U=U^(-1).
In particular H=UK is selfadjoint and ||H||=||K||.
Direct substitution fixes the convention:

    (Hf)(x)=sum_eta p_eta 1_D(sigma(x)+eta) f(sigma(x)+eta).

On l2(O), let (tau f)(x)=f(x+1), C=(2I+tau+tau*)/4, and (Vf)(x)=f(sigma(x)).
Then C=((I+tau)/2)*((I+tau)/2) is positive semidefinite, V is a selfadjoint unitary and CV=VC.
H is the compression P_D C V P_D.
In general sigma itself does not preserve D; the compression must be retained.

Partition O into cosets modulo Z.
For r in O, the integer set I_r={n:r+n in D} is an interval, possibly empty.
Its length is at most N=ceil(2B), since the expanding-coordinate condition alone is an open interval of real length 2B.
The involution sigma pairs the cosets r+Z and sigma(r)+Z.
With representatives r and sigma(r), the corresponding H block has entries p_(m-n) between I_r and I_(sigma(r)); if these cosets coincide, sigma(r)-r is an integer k, and sigma squared gives k=-k, hence k=0.
Thus in the fixed-coset case sigma(r)=r and the block is exactly a principal finite-interval compression of C.

For any two intervals I,J of cardinalities at most N, positivity of C gives

    |<f,Cg>|^2 <= <f,Cf><g,Cg>
                 <= lambda_N^2 ||f||^2 ||g||^2

for f supported on I and g supported on J, where

    lambda_N=(1+cos(pi/(N+1)))/2=cos^2(pi/(2(N+1))).

Indeed the l-by-l principal block of C has diagonal 1/2 and adjacent entries 1/4.
Its sine eigenvectors sin(j h pi/(l+1)) give eigenvalues (1+cos(h pi/(l+1)))/2, all positive and at most lambda_l<=lambda_N.
The displayed positivity inequality follows directly from C=A*A and ordinary Cauchy--Schwarz.
The paired rectangular blocks therefore have norm at most lambda_N, and their orthogonal direct sum gives

    ||K|| <= lambda_N.                                      (1)

The bound is exact.
The trace u=beta+beta^(-1) is irrational, since otherwise beta would have degree at most two.
The fractional parts of m*u are dense modulo one (the elementary compact-rotation argument already retained in [L102](Yin_L_G0102_v1.md#unit-circle-trace-witness-decay) suffices).
Because 2B is nonintegral for a Salem beta, some m has exactly N integers n satisfying |m*u+n|<B.
The element r=m*u lies in O and is fixed by sigma, so r_+=r_-.
On that coset the stable constraint |r_-+n|<S is weaker, and the whole fixed H block is precisely the N-point lazy tridiagonal matrix.
Its top sine eigenvector proves equality in (1).
This also shows that the norm is attained, without a neutral-radius cutoff.

The probability interface in fact holds for every Salem beta in (1,2), without the unresolved general co-return premise.
Every finite zero-to-zero word necessarily stays in D: its prefix bounds the contracting real coordinate strictly by S, and its suffix bounds the expanding coordinate strictly by B.
Conversely every path counted by K^n(0,0) is an original zero-to-zero word.
Thus, for the original return probability,

    p_n=K^n(0,0)<=lambda_N^n.

Identifying every point of D with an actually returning state still needs the co-return theorem; identifying this zero-point matrix coefficient does not.
This scope clarification was proposed by the drafting agent and checked by the coordinator on 2026-10-10 after the first frozen draft.

This is a full-law bound but not a uniform Mahler gap.
As beta decreases to one, -log(lambda_N) is asymptotic to pi^2(beta-1)^2/16.
Equality of the one-step norm does not assert equality of the spectral radius, nor of the exponential rate of a fixed matrix coefficient.

<a id="reciprocal-kernel-essential-norm"></a>
### 2. Essential norm and equality profiles

There are infinitely many distinct trace-fixed cosets attaining the maximal N-point interval: the dense irrational rotation visits the nonempty open set of suitable phases infinitely often, and distinct m*u differ by a noninteger.
The normalized top H eigenvectors supported on those disjoint cosets are orthogonal.
For any compact operator A, their A images tend to zero, whereas their K images have norm lambda_N.
Hence the distance of K to the compact operators is exactly lambda_N.
In particular, a finite neutral-radius truncation cannot approximate K in operator norm.
This says nothing against finite calculations with independently justified tails; it identifies the tail that such a justification must address.

We will also need the equality case of (1).
Every nonzero integer-translation fiber of a vector f satisfying ||Hf||=lambda_N||f|| has exactly N consecutive nonzero coordinates, proportional to the positive top sine vector (with a possibly complex scalar depending on the fiber).
To verify this carefully, the paired-fiber rectangular block is B_(I,J)=P_I C P_J.
If it attains lambda_N on g, choose unit f in I in the direction B_(I,J)g.
Every inequality in the positive Cauchy--Schwarz bound must be equality.
Both principal quadratic forms must attain lambda_N, which forces |I|=|J|=N and top sine profiles.
Equality in Cauchy--Schwarz means A f is a scalar multiple of A g for A=(I+tau)/2.
The map A is injective on l2(Z): its kernel would be a nonzero alternating constant-modulus sequence.
Thus f and g are proportional as vectors on Z, forcing I=J as well.
For a direct sum, the nonnegative norm deficits sum to zero only if every nonzero block attains equality.
This proves the asserted fiber profile.
The same condition applies to the top singular subspace E=ker(H^2-lambda_N^2 I), and H maps E onto E.

<a id="reciprocal-kernel-two-step-loss"></a>
### 3. A strict two-step gain from incompatible algebraic directions

**Theorem.** For the full strip operator above,

    ||K^2|| < lambda_N^2,       and consequently r(K)<lambda_N.   (2)

The inequality is strict for each fixed beta; this proof does not yet give a useful uniform numerical margin as beta tends to one.
It supplies a finite matrix problem for that margin, without any neutral-radius state enumeration.

First, endpoint legality is sufficient for every intermediate point of any word.
Starting in D, the contracting real coordinate stays strictly within S under every digit, because beta^(-1)S+1=S.
Starting backward from an endpoint in D, the expanding coordinate stays strictly within B, because beta^(-1)(B+1)=B.
Thus

    (K^2 f)(x)=sum_(a,b in {-1,0,1}) p_a p_b
                   1_D(beta^2*x+beta*a+b) f(beta^2*x+beta*a+b).

All nine original two-digit weights are retained, and distinct pairs yield distinct offsets because beta is irrational.

Let Lambda=Z+beta Z.
Partition the input state space into cosets r+Lambda and the output state space into the corresponding cosets beta^(-2)r+beta^(-2)Lambda.
The operator K^2 is an orthogonal direct sum of matrices between their intersections with D.
Each intersection is finite with a bound depending only on beta: the two real embeddings of the basis (1,beta) form the invertible matrix with rows (1,beta) and (1,beta^(-1)).
The two strip inequalities therefore enclose a bounded parallelogram in its two integer coordinates.
The same applies to beta^(-2)Lambda.

There are only finitely many possible block matrices, up to ordering.
Indeed choose each representative r by subtracting an element of Lambda so that its two-real vector belongs to a fixed compact fundamental parallelogram.
Then r's two real values, and those of beta^(-2)r, stay uniformly bounded.
The integer-coordinate sets that can meet D lie in two fixed finite boxes.
Membership selects subsets of those boxes; each matrix entry is either zero or one of the fixed nine weights.
No claim that all formal patterns are realized is needed.
At least one occurring finite block therefore attains ||K^2||, with a finitely supported unit vector f.

Suppose contrary to (2) that this norm is lambda_N^2.
Both steps in ||K^2 f||<=lambda_N||Kf||<=lambda_N^2||f|| are then equalities.
Since K=UH, f and Kf belong to E.
Set g=Hf/lambda_N.
It is finitely supported, belongs to E, and Ug=Kf/lambda_N belongs to E.
By Section2, each nonzero Z-fiber of g contains exactly N consecutive nonzero points.
Applying the same fact to Ug and pulling it back by T shows that every nonzero beta^(-1) Z-fiber of g likewise contains exactly N consecutive nonzero points.

Select one nonempty component of its finite support modulo Gamma=Z+beta^(-1) Z and write its points as r+n+m beta^(-1).
Coordinates (n,m) are unique.
Let m_0 be the smallest second coordinate in this component.
The active row m=m_0 has N consecutive first coordinates n_0,...,n_0+N-1.
The column through its rightmost point has N consecutive second coordinates; by minimality of m_0 these are m_0,...,m_0+N-1.
Thus the support contains both

    r+n_0+m_0 beta^(-1),
    r+(n_0+N-1)+(m_0+N-1) beta^(-1).

Their expanding real values differ by (N-1)(1+beta^(-1)).
But N>=3 and beta<2 give

    (N-1)(1+beta^(-1)) > 3(N-1)/2 >= N >= 2B.

Two points of D have expanding-coordinate difference strictly less than 2B.
This contradiction proves (2).
Finally r(K)<=||K^2||^(1/2), so the spectral-radius conclusion follows.
In particular K is nonnormal: a normal bounded operator would have ||K^2||=||K||^2.

### 4. Interpretation and the discriminating next calculation

This is an actual full-law loss mechanism.
The one-step extremizers are exactly pinned to long integer-translation fibers.
A second step rotates their algebraic direction to beta^(-1), and the narrow expanding strip prevents simultaneous extremality.
The stable strip is essential for reducing two-step blocks to finite matrices and obtaining a uniform strict loss for fixed beta; the contradiction at the last step uses the expanding strip alone.

For the quartic input beta in (1.72,1.73), N=3 and ||K||=(2+sqrt(2))/4.
For the original Lehmer input beta in (1.17,1.18), N=12 and ||K||=cos^2(pi/26).
These rational beta brackets already certify the values of N.
The first useful remaining test is to enumerate the finitely many planar membership patterns, or a rigorously enclosing family, and bound their rational two-step matrices.
This is a translated two-dimensional parallelogram problem, not an enumeration of the unbounded eight-dimensional neutral directions.
A bound ||K^2||<=a<lambda_N^2 would give p_n<=lambda_N^(n mod 2) a^floor(n/2) for the true return probability of every such Salem beta, by the zero-point interface above.

The earlier [L30 all-time diagonal probability and entropy comparison](Yin_L_G0030_v1.md#one-expanding-comparison) already gives a rate asymptotic to m=log(beta) on hypothetical near-one Salem inputs.
The one-step operator-norm corollary here has a quadratic rate and is weaker in that limit.
The new information is the exact full-strip norm, its essential-norm obstruction to truncation, and the rigorously strict loss between algebraic directions after two steps.
No improvement over the previously known diagonal rate is claimed without computing and comparing the actual two-step margin.
This comparison was added by the coordinator on 2026-10-10.

No positive Mahler gap follows: the displayed one-step rate tends to zero quadratically as beta tends to one, and the strict two-step proof has not controlled the size of its improvement in that regime.
Polynomial growth of the actual core, an edge-reversing involution, and a selfadjoint UK by themselves also do not equate the spectral radius with the diagonal return rate.
That identification is not used here.

### Contribution and review scope

The coordinator supplied the reciprocal edge-reversal observation and exact-core input.
This agent supplied the integer-fiber norm/equality calculation, essential-norm consequence, finite two-step block decomposition and incompatible-direction strict inequality.
The matrix sine formula is a standard attributed input with its two-line direct verification retained for normalization.
These author-self-checked operator arguments have the complete independent finding retained below and are adopted in this fixed material at that exact scope.
No proof-assistant certification is claimed.


<a id="reciprocal-kernel-collaborator-review"></a>
### Complete local collaborator check

On 2026-10-10 the coordinating AI for Yin read and checked the entire Sections 1--4.
It contributed the initial reciprocal edge-reversal observation and the explicit comparison with L30, so this is a collaborator review rather than independent review of the entire argument.
The drafting agent supplied the finite-fiber norm, equality profiles, essential norm and two-step incompatibility proof.
No mathematical defect was found.
No computation is asserted or required for this qualitative analytic result.

The check covered the counting-measure adjoint and UK convention, all actual original digit weights, the fact that sigma itself need not preserve D, the rectangular C compression, and injectivity of (I+tau)/2 on l2(Z).
It verified the upper bound by positive Cauchy--Schwarz and the exact equality profiles, including the forced common interval and nonzero top sine coordinates.
Irrational trace phases give infinitely many distinct fixed cosets attaining the maximal length N; this proves both norm attainment and the essential-norm lower bound, without mistaking the neutral projection for a discrete set.

For K^2 the input/output coset partitions correspond bijectively under multiplication by beta^2, because beta is a unit.
Their two-real embeddings are invertible rank-two lattices.
Reducing each representative into a compact fundamental parallelogram gives uniformly finite integer boxes for both sides, and only finitely many weight/membership patterns.
Thus a finite block really attains the operator norm.
Endpoint legality implies intermediate legality in both real directions, so the displayed nine-weight kernel drops no path.
Equality for two steps would put f and Kf in the top singular subspace; its H invariance then gives a nonzero finitely supported g with both required fiber profiles.
The minimal-row/rightmost-column argument stays in one unique rank-two component and forces the stated expanding diameter.
The strict inequality for N>=3 and beta<2 contradicts D's open width, establishing the qualitative gain.
The nonnormality and spectral-radius upper bound follow without identifying the spectral radius with a diagonal return exponent.

The probability scope clarification above was separately checked from finite prefix and suffix geometric sums.
It does not assume that the full strip is the actual core for arbitrary beta.
The L30 comparison was read at its accepted one-expanding-conjugate scope; it prevents relabelling a weaker m-squared diagonal corollary as new near-one entropy progress.
No quantitative two-step margin, full independent review, finite block enumeration, or uniform gap is supplied by this check.
A separate noncontributing reviewer is still needed before fixed adoption of this complete argument.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0071_v1.md#complete-independent-noncontributor-written-review), with its original inspected scope and relationship.

## Quantifying the quartic two-step reciprocal kernel

Date: 2026-10-10.

The original [D30 argument](#reciprocal-kernel-two-step-loss) and its complete independent review are retained above.

### Aim and input

For the quartic Salem root of t^4-t^3-t^2-t+1, quantify the strict inequality ||K^2||<||K||^2 for the full strip and unchanged weights (1/4,1/2,1/4).
The accepted exact strip input is [L170](Yin_L_G0170_v1.md#exact-salem-return-strip), with the quartic co-return proof in [L169](Yin_L_G0169_v1.md#quartic-infinite-core-theorem).
The present question is the finite rank-two block norm supplied by D30, not another actual-state core enumeration.

<a id="quartic-two-step-certified-bound"></a>
### The certified bound

For the quartic input and the complete original-law strip operator,

    sqrt(96)/16 < ||K^2|| <= sqrt(97)/16 < 5/8.             (1)

Both sides refer to the actual full infinite-state operator.
The upper bound covers every two-real phase, without a neutral cutoff.
The lower bound is witnessed by one actual algebraic coset, not by a relaxed phase.
The exact checks are in [J33](../computations/programs/Yin_J_G0033/readme.md), with its retained certificate (`mathematics/computations/programs/Yin_J_G0033/inputs/certificate.json`) and regenerated exact result (`mathematics/computations/outputs/Yin_J_G0033/verified.json`).
This is a computer-assisted finite certificate with the coverage argument proved below; it is author self-checked and independently reviewed by the complete finding retained below.

<a id="quartic-two-step-proof"></a>
### 1. Finite coordinate reduction

Write B=1/(beta-1), S=beta B, Lambda=Z+beta Z.
Choose each coset representative r so its two-real vector belongs to the fundamental parallelogram generated by (1,1),(beta,beta^(-1)), with coefficients in [0,1).
It is contained in the rectangle [0,1+beta] x [0,1+beta^(-1)].
Overenclosing this parallelogram by a rational rectangle is allowed for an upper bound.

An input column y=r+n+m beta belongs to D when |r_++n+m beta|<B and |r_-+n+m beta^(-1)|<S.
An output row x=beta^(-2)(r+n'+m'beta) belongs to D when |r_++n'+m'beta|<beta^2 B and |r_-+n'+m'beta^(-1)|<beta^(-2)S.
The two-step edge has a=m-m', b=n-n' in {-1,0,1}, with matrix entry w_a w_b/16, where w_0=2,w_(+/-1)=1.
This coordinate formula and the axis-boundary arrangement were proposed by the coordinator; all implemented bounds and certificates will be separately checked.

For the quartic, beta lies in (1.72,1.73), and the fundamental parallelogram is contained in the closed rational rectangle R=[0,3] x [0,2].
The following elements of Q(beta), written in the power basis, are exact:

    beta^(-1)=1+beta+beta^2-beta^3,
    B=beta^3-beta-2,             S=beta^3-beta-1,
    A:=beta^2 B=beta^3-1,
    C:=beta^(-2)S=2beta^3-beta^2-2beta-3.

Their defining identities are checked by polynomial reduction modulo the fixed quartic.
The input conditions use real half-widths (B,S); the output conditions use (A,C).

Every possible input and output coordinate pair (n,m) belongs to

    -8<=n<=8,       -7<=m<=7.                              (2)

Here is a rational enclosure proof, valid also at the boundary of R.
Set u=n+m beta and v=n+m beta^(-1).
For input columns, |u-v|<B+S+3; for output rows, |u-v|<A+C+3.
Use beta in (17/10,18/10), beta^(-1)<10/17, B<10/7, S<17/7, A<17/7+18/10, and C<B.
The gap beta-beta^(-1)>17/10-10/17.
Both quotients

    (B+S+3)/(beta-beta^(-1)),
    (A+C+3)/(beta-beta^(-1))

are therefore less than 8, as verified by substituting the displayed rational bounds.
Since u-v=m(beta-beta^(-1)), integer m lies in [-7,7].
Also |v|<S+2 for both kinds of point, since C<S, and

    |n|<=|v|+|m| beta^(-1)
         <17/7+2+7*(10/17)<9.

This proves (2).
The complete candidate coordinate box has 255 points on each side, independently of the neutral coordinates of r.

### 2. Exact phase coverage, including boundaries

For every coordinate pair in (2), place all input and output expanding thresholds

    +/-B-n-m beta,       +/-A-n-m beta

that lie strictly between 0 and 3 on the horizontal phase axis.
Likewise place all contracting thresholds

    +/-S-n-m beta^(-1),  +/-C-n-m beta^(-1)

strictly between 0 and 2 on the vertical axis.
Include the rectangle endpoints.
Equal field elements are identified by their reduced degree-three coefficient tuples.
Distinct elements are ordered by rational interval evaluation at beta.
The root enclosure is obtained from 150 exact bisections of [172/100,173/100]; endpoint signs and a positive lower bound on P' throughout that bracket are checked.
All comparisons used by this calculation have strictly separated interval signs.
The accepted quartic field identity ensures no nonzero reduced tuple represents zero.

There are 63 horizontal open intervals and 65 vertical open intervals, giving 4095 open cells.
All input/row memberships are constant in each cell.
The checker takes the exact field-valued midpoint on each axis, uses both strict inequalities for every box point, and builds the integer matrix M_cell=16 times its two-step block.
Matrix entries are exactly w_(m-m') w_(n-n'), hence 0,1,2 or 4.
Zero rows and columns may be removed because this preserves the singular norm.
The arrangement produces 138 distinct nonempty matrices, each having at most 13 rows and 13 columns.

Boundary phases require no guessed tie convention.
At any phase on a threshold or on R's boundary, every row/column that satisfies its two strict inequalities remains present throughout some relative neighborhood of that phase.
There are finitely many candidate points, so one common neighborhood works for all those active points.
Any adjacent open cell sufficiently near the phase consequently contains all its active rows and columns.
Its boundary matrix is therefore a submatrix of the adjacent cell matrix and has no larger singular norm.
Points on a threshold that fail the strict inequality are excluded, exactly as required by the original open strip.
This covers every phase of R, and hence every actual coset after reducing its representative.

The phase-cap contract was 50000 open cells, with a 60-second elapsed-time guard in the discovery and verification loops; the actual 4095 cells did not hit either cap.
No actual states were omitted by a neutral cutoff or a search-node cap.
The finite loops use the stated 255-point box and the complete threshold lists.

### 3. Rational positive-vector upper certificate

For every distinct matrix M=16K^2 restricted to a block, the certificate retains a strictly positive integer vector v with

    (M M^T)v <= 97 v                                      (3)

coordinatewise.
The exact checker reconstructs the entire phase arrangement independently of all discovery eigenvalues, requires exactly the complete set of distinct matrices, rejects duplicates or missing cases, and verifies every integer inequality in (3).
The smallest recorded integer slack is 999999951; its size is only a certificate check, not an additional analytic estimate.

To derive the norm consequence without invoking an unrecorded spectral theorem for a positive chain, let V be the diagonal matrix with entries v_i.
The nonnegative matrix V^(-1) M M^T V has all row sums at most 97, so its induced infinity norm, and therefore every eigenvalue modulus, is at most 97.
Similarity preserves eigenvalues.
The real symmetric positive-semidefinite matrix M M^T consequently has largest eigenvalue at most 97.
Thus ||M||<=sqrt(97).
Direct summing the complete blocks gives the upper bound in (1).
The last comparison sqrt(97)/16<5/8 follows from 97<100.

Numerical discovery used NumPy only to propose the integer positive vectors and choose the convenient integer 97.
The exact checker imports no NumPy, reads no approximate root or eigenvalue as input, and recomputes the masks and matrices by integer/Fraction arithmetic.
Discovery and checking share the explicit exact field/arrangement helper; this is not independent implementation evidence.
The full proof and checker require independent review before fixed adoption.

### 4. An actual-block lower witness

Take the actual element

    r=-413+774 beta-180 beta^3 in Z[beta].

Its two real embeddings lie in the phase rectangle; the exact checker verifies this, constructs sigma(r) by substitution beta -> beta^(-1), and reconstructs the strict block memberships at (r_+,r_-).
Every column is an actual point r+n+m beta in D, and every row is an actual point beta^(-2)(r+n'+m'beta) in D because beta is a unit.
Thus this is a genuine finite block of the full original operator.

The retained integer vector h for its Gram matrix G=M M^T satisfies the exact Rayleigh calculation

    h^T G h = 9633565984214612,
    h^T h   = 100000003825002,
    h^T G h > 96 h^T h.

The largest eigenvalue of G is therefore greater than 96.
This proves the strict lower bound in (1).
It is not necessary to assume that every relaxed phase pattern occurs for an actual algebraic state.
The lower witness is separately identified and checked.

### 5. Probability comparison and useful scope

Combining (1) with D30's exact one-step norm gives, for every n>=0,

    p_n <= ((2+sqrt(2))/4)^(n mod 2)
           (sqrt(97)/16)^floor(n/2),
    r(K) <= (97/256)^(1/4).

The asymptotic operator-based diagonal decay rate is at least (1/4)log(256/97).
The known [L30 diagonal return comparison](Yin_L_G0030_v1.md#one-expanding-comparison) remains stronger at this quartic input.
Numerically, only as orientation, the new rate is about 0.243 per digit, whereas L30 gives about 0.376.
The certified achievement is a substantial and explicitly bounded reduction of the operator norm after changing algebraic direction; it is not an improved best diagonal entropy bound or a uniform Mahler gap.

The interval in (1) confines the true two-step norm to approximately (0.612372,0.615554].
Thus the strict nonnormal loss from the one-step square ((2+sqrt(2))/4)^2, approximately 0.728553, is quantitatively large for this input.
The input is fixed degree four.
A Lehmer computation would need its own proved coordinate bounds, exact threshold arrangement, phase cap and certificate; none is silently covered here.

### Contribution and verification status

The coordinator suggested the coordinate form of the nine-point matrix, axis-aligned phase thresholds and rational positive-vector certification.
This agent supplied the rational containing box, exact complete arrangement, boundary argument, positive-vector certificate construction/checker, and actual algebraic lower witness.
The accepted field/core inputs and D30's block conventions are reused at their recorded scope.
No additional external theorem, source acquisition or novelty claim is needed for the direct finite-matrix calculation.

On 2026-10-10, the author completed discovery and ran the complete integer/Fraction checker successfully on all 4095 phase cells, 138 matrices and the actual lower witness.
These are the author's execution results, not an independent rerun or proof review.
The complete separately organized finding below checked these retained proof inputs and certificate files.

<a id="quartic-two-step-review-history"></a>

**Preserved original D G0035 review history.** Its preparatory observations and initial checker correction are retained before the final frozen-input disposition.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0803_v1.md#algebraic-thresholds-and-strict-boundary-coverage), with its original inspected scope and relationship.

## Original 2026-10-10 adoption and retention account

The following complete passage is the original2026-10-10 adoption/retirement and scope record, retained at its original wording and date precision.
Its independent, active, ongoing and then-pending descriptions are historical statements, without authority over current review relationships, mathematical status or Task execution.
The responsible current theorem/status remains [C203](../claims/Yin_C_G0203_v1.md#statement); actual present review relationships and checking scopes remain in [R71](../audits/reviews/Yin_R_G0071_v1.md#reciprocal-kernel-independent-review) and [R495](../audits/reviews/Yin_R_G0495_v1.md#reciprocal-kernel-collaborator-review).
No new retired correspondence, historical event, inspection or independent relationship is created by restoring this passage.

<a id="operator-fixed-retention"></a>
## Retention map and coordinating adoption

The coordinating AI for Yin directed this fixed adoption after the complete D30 noncontributor review and D35's 2026-10-09T16:51 frozen D34/J33 review.
D30's earlier review accounts recorded their date without a minute; no finer timestamp is invented here.
The independent reviewer supplied neither D30's operator derivation nor D34's proof/algorithm, and contributed only its own checking implementation and review.
The coordinator's mathematical contributions remain explicitly identified in the original accounts.
The qualitative collaborator finding is therefore self-reviewed with respect to its contributor relationship; the separate noncontributor findings retain their disclosed independent, nonblind arrangements.

| Retired working identity | Exact retained material |
| --- | --- |
| D G0030 | [Full operator convention](#full-strip-operator-statement) and all Sections1--4, source/normalization boundaries, collaborator account and [complete independent review](../audits/reviews/Yin_R_G0071_v1.md#reciprocal-kernel-independent-review) |
| D G0034 | [Quartic two-sided statement](#quartic-two-step-certified-bound) and [complete proof](#quartic-two-step-proof), including the actual lower witness and L30 comparison |
| D G0035 | [Complete review history](#quartic-two-step-review-history), including preparation, independent reproduction, initial tighter-box checker correction and [final finding](../audits/reviews/Yin_R_G0803_v1.md#quartic-two-step-independent-review) |

J G0033 and J G0034 retain the programs, necessary certificates and mathematical outputs, with their dependencies and reproduction commands.
The original author executions and separately implemented reviewer checks retain their distinct mathematical scopes.
The source-reading record for NPR13 remains at its finite Toeplitz formula scope, not a new source theorem audit.
Link maintenance does not broaden any inspected source or proof.

The new current adoption is exactly the general qualitative operator result and the fixed-quartic quantitative certificate.
G0001 remains active and unresolved.
The ongoing separated-digit long-block norm and exact spectral-radius investigations are not part of this adoption and keep their draft identities.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete collaborator check](#reciprocal-kernel-collaborator-review) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete collaborator check](#reciprocal-kernel-collaborator-review) | [General operator convention](#full-strip-operator-statement) | Original D30 Sections1--4 at the disclosed contributor-aware local-check scope; no independent relationship is inferred. |
