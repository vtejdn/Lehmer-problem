---
author: Yin
---
# Full norm-income barrier for every below-one flat first-window packet

Date: 2026-10-12T11:44.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
Root authored the complete original19:30 D17 mathematics.
The rounding-recovery AI independently whole-reviewed that body in R275 and NOW authors this exact statement/wrapper; it is a contributor to the new extraction and cannot independently review it.
The ENTIRE original author account follows, with its allocation/candidate history, full proof, boundaries, role record and freeze retained.
Initial status is proof draft / under review until a separate actual extraction/interface review.
No adoption or retirement is performed here.

## Statement

Let P(t)=sum_(j=0)^d p_j t^j be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, p_j in{0,+1,-1}, p_d=1 and p_0 in{+1,-1}.
Write K=Q(alpha), O0=Z[alpha], S={j:p_j!=0}, n=|S|>=4 and

    m=m(P)=sum_(P(beta)=0)log max(1,|beta|),
    a_n=1-1/n, b_n=2-4/n.

All sums/products over conjugates use the original d roots.
Reciprocity is not required.
A representative is ANY rational f of degree at most d with ACTUAL nonzero value f(alpha) in O0.
A finite packet has arbitrary positive normalized RATIONAL indexed weights omega_i and such representatives f_i.
Put

    e_i=||f_i||_2^2, E=sum_i omega_i e_i<1,
    D_i=Norm_(K/Q)(f_i(alpha)) in Z minus{0},
    Lambda=(1/d)sum_i omega_i log|D_i|>=0.

All rational representatives, fractional classes, nonzero integral residues and final weights in this first window are allowed.
There is no common bit law, common fractional multiple of P, selected norm inventory, covariance or complementarity assumption for A--C below.
Distinct labels with equal coefficients or values retain their actual weights.

**A. Old first shell and new complete second shell.**
A value is called monomial in this window exactly when it equals +/-alpha^j for some0<=j<=d, irrespective of the coefficient shape of its representative.
Every admissible representative has

    ||f||_2^2>=a_n,

and every representative whose ACTUAL residue is not monomial in this window has

    ||f||_2^2>=b_n,
    b_n-a_n=(n-3)/n>0.

The first floor is the already accepted C25 result; the new assertion is the second floor on the full nonmonomial complement.
Other algebraic units may occur in that complement.
These are individual bounds, with no assertion that a complementary packet attains either one.

Explicitly, write f=z+cP with z in Z^(d+1), c in Q.
On S put x_j=p_j z_j, mu=(1/n)sum_(j in S)x_j and v=sum_(j in S)(x_j-mu)^2; put b=sum_(j notin S)z_j^2.
Then

    ||f||_2^2>=v+b.

The complete integer cases are retained in the proof: constant support and outside coordinates; signed support range at least2; and range1 with r high coordinates, where v=r(n-r)/n.
The range1 endpoints r1,n-1 with b0 are exactly the cases used to recognize monomial values after an integer P shift.
Sparse support and arbitrary outside integer coefficients are included.

**B. Integer representative and full original norm price.**
For EVERY such f of energy e, choose an integer k nearest the signed-support mean mu and z'=z-kP.
It has the SAME actual nonzero residue, integer coefficients, degree at most d and

    1<=||z'||_1<=e+sqrt(ne)+n/2<=n+2e,
    0<=log|Norm_(K/Q)(f(alpha))|/d
        <=log(n+2e)+m.

No bound depending on the number of zero coefficient positions, real nearest-point replacement, discarded conjugate or coefficient-optimal integer representative is assumed.
Every actual monomial value has absolute norm1; all other norms, whether unit or nonunit, remain charged.

**C. Full weighted income and surplus bound over all residues.**
Let B be the set of labels whose actual residue is not monomial in the stated window and let pi=sum_(i in B)omega_i.
Then

    E>=a_n+(n-3)pi/n,
    0<=pi<1/(n-3), E>=a_n,
    0<=Lambda<=[log(3n-6)+m]/(n-3),
    0<Lambda-(1/2)logE
        <=[log(3n-6)+m]/(n-3)
             +(1/2)log[n/(n-1)].

This is a MASS bound, not a count bound.
It includes n4 and pi0.
For pi>0 the complete proof retains the actual bad-label energy E_B=sum_(i in B)omega_i e_i and the conditional Jensen bound

    Lambda<=pi[log(n+2E_B/pi)+m]
           <=pi[log(n+2/pi)+m].

The scalar function x[log(n+2/x)+m] is increasing for x>0,n>=4,m>=0, yielding the displayed endpoint.
No potentially nonunit norm is omitted; for pi0 the income is exactly zero.
The weak final inequalities do not assert an endpoint optimizer.

Along ANY sequence of actual inputs satisfying these hypotheses with n tending to infinity and bounded m(P), the full surplus of EVERY such below-one first-window packet tends to zero, uniformly over all actual representatives, q, final weights and residue classes.
No such sequence is asserted to exist, and no support-growth assertion for a hypothetical near-one sequence is assumed.

**D. Complementary packets, actual width and every scalar/copy cost.**
Now additionally require EVERY positive aggregate lag to vanish:

    sum_i omega_i sum_j f_(i,j)f_(i,j+h)=0,
                                1<=h<=d.

The circle covariance is then the constant E.
Its ACTUAL common union width is EXACTLY d: a smaller common width could be shifted into[0,d-1] in the same monogenic order and would force E>=1.
This exact assertion is not extended to an overorder.

Let q be the ACTUAL least common coefficient denominator, F_i=q f_i in Z[t], M the ACTUAL least denominator of the complete FINAL indexed weights and k_i=M omega_i in Z_(>0), so sum k_i=M.
With every full signed original norm D_i retained,

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(k_i)=q^(dM)product_i D_i^(k_i),
    S_int=sum_i omega_i||F_i||_2^2=q^2E,
    I_income=(1/(dM))log|product_i Res(P,F_i)^(k_i)|
             =logq+Lambda,
    I_income-(1/2)logS_int=Lambda-(1/2)logE<=m.

The last inequality invokes C10's generic direct original-root argument only after complementarity, on the SAME final weights and actual T/d=1.
It can be combined with C on that same packet.
q need not equal M or be bounded; no uniform bound on the indexed weight denominator, primitive-numerator assumption or unit-only inventory is imposed.
If F_i has content b_i>1, its full resultant retains b_i^d.
Negative signs and every copy exponent remain in the product before taking absolute logarithms.

One COMMON monomial normalization of an initially shifted window of width d preserves E, Lambda, q and the final indexed weights, because alpha is an actual O0 unit.
The corresponding power of the signed unit norm remains in every norm and its copied product.
The monomial-residue classification is made relative to the normalized window.
This is not permission to shift different atoms separately while declaring the original common physical width unchanged.

The bounds concern ACTUAL flat inputs with n>=4, E<1 and the FIRST allowed window[0,d].
They assert neither full-capacity optimality nor a bound for E>=1 packets, nonflat inputs, overorders, fixed-support limiting regimes or windows larger than d.
C25's old necessary q>n/2, C29's cross-term necessity and its dense width-d+1 dyadic control remain separate accepted facts.
C31's original Lehmer and C58's original quartic packets are compatible controls only; D16's narrower common-marginal analysis is not a premise.
No uniform Mahler gap or unrestricted G0001 completion follows.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:44 |
| status | open |
| reason | Register the all-residue second-shell, nonmonomial mass and complete norm-income/surplus bounds at E<1 in the actual flat first window, with every original norm and actual denominator/copy cost. The complete original19:30 D17 remains below. R275 whole-reviewed that original body, but its reviewer now authors this wrapper and cannot independently review the new extraction; a different actual review is required before adoption. No capacity optimum, wider-window impossibility or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete A--D at actual flat original input/order and n>=4, all rational representatives/final weights with E<1, full income bounds and separately complementary physical-width/cost branch. |
| argument | [Entire retained author account](#argument) | Complete original D17 allocation/reuse/candidate history, Sections1--7/equations1--11, original19:30 freeze and every proof, norm, width, source/contribution and scope boundary. |
| dependency | [C17 monogenic short-window theorem](Yin_C_G0017_v1.md#statement) | ONLY actual common width below d implies E>=1 in O0, used to establish actual widthd in complementary branch; no overorder conclusion. |
| dependency | [C10 direct complete-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual rational complementary packet, every signed nonzero original norm/resultant and FINAL copy at physical T/d=1; generic direct argument needs no reciprocity. |
| support | [C25 exact old first-window floor](Yin_C_G0025_v1.md#statement) | Established baseline1-1/n, original residue/domain and necessary denominatorq>n/2 credited as old result; the retained proof also gives its local integer-case verification. |
| support | [C29 original projected form and wider control](Yin_C_G0029_v1.md#statement) | Existing all-integer/monomial equality context, cross-term necessity and explicitly dense actual width-d+1 example; no external second-minimum theorem imported. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0275_v1.md#flat-all-residue-whole-independent-finding) | ENTIRE original19:30 D17 proof and actual direct interfaces only. It does not review or adopt this new statement/wrapper. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:57 |
| status | proved |
| reason | Adopt the separately performed whole R275 and actual extraction R281 findings. The entire original proof/history remains. The all-residue full-income barrier applies to flat first-window E<1 packets, not wider windows, nonflat inputs or unrestricted completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete A--D at actual flat original input/order and n>=4, all rational representatives/final weights with E<1, full income bounds and separately complementary physical-width/cost branch. |
| argument | [Entire retained author account](#argument) | Complete original D17 allocation/reuse/candidate history, Sections1--7/equations1--11, original19:30 freeze and every proof, norm, width, source/contribution and scope boundary. |
| dependency | [C17 monogenic short-window theorem](Yin_C_G0017_v1.md#statement) | ONLY actual common width below d implies E>=1 in O0, used to establish actual widthd in complementary branch; no overorder conclusion. |
| dependency | [C10 direct complete-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual rational complementary packet, every signed nonzero original norm/resultant and FINAL copy at physical T/d=1; generic direct argument needs no reciprocity. |
| support | [C25 exact old first-window floor](Yin_C_G0025_v1.md#statement) | Established baseline1-1/n, original residue/domain and necessary denominatorq>n/2 credited as old result; the retained proof also gives its local integer-case verification. |
| support | [C29 original projected form and wider control](Yin_C_G0029_v1.md#statement) | Existing all-integer/monomial equality context, cross-term necessity and explicitly dense actual width-d+1 example; no external second-minimum theorem imported. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0275_v1.md#flat-all-residue-whole-independent-finding) | ENTIRE original19:30 D17 proof and actual direct interfaces only. It does not review or adopt this new statement/wrapper. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0281_v1.md#flat-all-residue-actual-extraction-finding) | Entire actual statement, completely retained argument/history and all current direct interfaces, independently inspected after allocation by a noncontributor. |

## Registration and complete preservation

The complete original19:30 D17 body follows, retaining every original paragraph, formula, anchor, role, initial candidate limitation, self-check and freeze.
Only duplicate front matter, first-title depth and line endings/separating terminal whitespace are normalized.
Existing relative links remain valid from this Claim directory.
A direct entire-body comparison accompanies the extraction.
The original D17 stays in place pending root's separate consumer/preservation/retirement work.

The extractor's original whole review R275 is evidence for that exact D17 body only.
This new precise statement and wrapper are authored work requiring a DIFFERENT actual extraction reviewer.
C25/C29 attribution remains at the accepted scopes; the locally proved integer second-shell/Jensen estimates invoke no new external theorem or source.
Current comparison-only C31/C58/D16 mentions are not promoted into logical dependencies.
This operation performs no Claim adoption, D retirement or native mathematical execution.

2026-10-12T11:45 extraction check: the actual ENTIRE original body and retained argument compare equal after only the declared normalization, with17,174 characters each.
The scoped C62/D17/R275 material check passed with checked3.
These are preservation and structural results, not an independent wrapper review.

## Argument

## All-residue norm-income barrier below unit energy in the flat first window

Date: 2026-10-12T11:23.
Human author Yin.
Root AUTHOR inquiry under the unchanged G0001 continuation.
Root owns the new second-shell/full-norm candidate and cannot independently review it.
No native computation, external theorem or new source is planned.

## Bounded reuse and genuinely broader question

The actual [C25 statement](Yin_C_G0025_v1.md#statement) ALREADY proves the full first-window energy floor 1-1/n for flat support n, exact individual denominator minima and necessary q>n/2.
[C29](Yin_C_G0029_v1.md#statement) ALREADY gives the actual all-integer projected form and monomial equality shell.
These facts are credited, not rediscovered as new.
Root also read the complete current pair construction C58 and the current all-subset common-marginal author D16.
The new target covers ALL first-window rational representatives with actual nonzero O0 residues and arbitrary FINAL positive weights, without a shared fractional class, bit law, prescribed marginals, support cutoff, diagonal covariance or unit-only inventory.
The changed issue is the ENTIRE norm income when total coefficient energy E<1, not another proof of C25's energy floor.
A bounded current G-Claim search for second shells/nonmonomial mass/norm budget found no retained matching all-residue result; this is not a novelty claim.

## Candidate mechanism and limits

Write any actual representative f=z+cP with integer z and rational c, at allowed width d, for the ACTUAL flat minimal P having n>=4 nonzero coefficients.
Its squared norm is at least the squared Euclidean projection of z perpendicular to the coefficient vector P.
Outside P's support this has integer squared coordinates; on support it is the variance of n signed integer coordinates.
The old minimum is a_n=1-1/n.
The proposed SECOND-shell floor is b_n=2-4/n for every residue not equal to one of the finitely many monomial values +/-alpha^j,0<=j<=d.
Prove it by the support integer range: range1 with2 throughn-2 exceptional coordinates costs k(n-k)/n>=b_n; range>=2 costs at least2; nonzero outside coordinates are handled separately.

If so, any packet of total E<1 has total mass p_bad<=1/(n-3) in those nonmonomial residue classes.
Each label of energy e admits an integer representative z-kP with l1 norm at most n+2e: choose k nearest the signed-support mean, use support Cauchy--Schwarz and integer outside-coordinate squares.
This bounds its COMPLETE original norm by log|Norm|/d<=log(n+2e)+m(P).
Monomial labels have absolute norm1.
Conditional Jensen on bad labels then suggests

    Lambda <= [log(3n-6)+m(P)]/(n-3),
    Lambda-(1/2)logE <= [log(3n-6)+m(P)]/(n-3)
                              +(1/2)log[n/(n-1)].

This would force full surplus to0 for bounded m and n->infinity even in the ENTIRE below-one first-window domain, independent of q/FINAL M and all fractional residue choices.
Exact representation, shell classification, representative norm bound, probability endpoint, Jensen monotonicity, all original signed costs and common-monomial width normalization still need complete proof and review.
It does not cover E>=1, windows larger than d (already materially different in C25), nonflat inputs or unrestricted G0001.
It asserts no near-one sequence.
Substantive proof will continue here.


<a id="flat-all-residue-domain-and-shells"></a>
## 1. Actual all-residue domain and the two coefficient shells

Let P=sum_(j=0)^d p_j t^j be the ACTUAL monic irreducible nontorsion integer-unit minimal polynomial, original d>=2, p_j in{0,+/-1}, p_d=1,p_0=+/-1, and n=|S|>=4 where S={j:p_j!=0}.
The original field is Q(alpha) and order O0=Z[alpha].
Put

    a_n=1-1/n, b_n=2-4/n, b_n-a_n=1-3/n>0.

Every rational f of degree at most d with nonzero actual f(alpha) in O0 can be written

    f=z+cP, z in Z^(d+1), c in Q.                  (1)

Indeed take the unique power-basis integer representative z of degree below d and divide the remaining polynomial by the actual monic minimal P.
Different integer z differ by an INTEGER multiple of P, since monicity makes the leading quotient coefficient integer.
This is the exact C25 monic/order interface, not an assumption of a maximal order or a selected real embedding.

Call a residue **monomial in this window** if f(alpha)=+/-alpha^j for some0<=j<=d.
This concerns the ACTUAL value, not whether f itself has only one coefficient.
All such values have full absolute norm1.
Other algebraic units may be in the complementary class; no assertion that every such class has norm larger than1 is made.

**Shell lemma.**
Every admissible f satisfies ||f||^2>=a_n, the already adopted C25 floor.
If its residue is NOT monomial in this window, then

    ||f||^2>=b_n=2-4/n.                            (2)

These bounds hold without any covariance condition or denominator restriction.
They need not be attained by a complementary packet.
The additional second-shell statement is proved completely next.

For an integer representative z in(1), define x_i=p_i z_i for i in S, its real average mu=(1/n)sum x_i, and

    v=sum_(i in S)(x_i-mu)^2,
    b=sum_(j notin S)z_j^2.

Orthogonal projection perpendicular to the coefficient vector of P gives

    ||f||^2>=v+b.                                  (3)

All x_i and outside z_j are integers.
If all x_i are equal to an integer k, then v0 and z-kP is supported outside S.
A nonzero value excludes b0.
If b1, exactly one outside coordinate is+/-1 and the residue is monomial; otherwise b>=2, proving both relevant floors.

If the x_i are not constant, their integer range Delta=max x_i-min x_i is at least1.
For Delta>=2, just the minimum and maximum coordinates give

    v>= (min x_i-mu)^2+(max x_i-mu)^2
          >=Delta^2/2>=2.

For Delta1, all coordinates are k or k+1, with exactly r high coordinates,1<=r<=n-1.
Direct summation gives v=r(n-r)/n>=a_n.
When r1 or r=n-1 and b0, subtracting kP or(k+1)P leaves exactly one signed support coordinate+/-1, hence a monomial residue.
If the residue is nonmonomial and b0, these two cases are excluded;2<=r<=n-2 gives v>=2(n-2)/n=b_n.
If b>=1 in any nonconstant case, v+b>=a_n+1=2-1/n>=b_n.
This proves(2) and also independently recovers the old baseline without relabeling it a new result.

The proof covers sparse support and arbitrary integer outside coefficients.
It is a direct integer-range calculation, not an uninspected assertion about a named lattice's second minima.
Its n>=4 condition is essential to the POSITIVE separation b_n-a_n; no such separation is asserted at n3.

<a id="flat-all-residue-mass-budget"></a>
## 2. Below-one total energy forces small nonmonomial mass

Take ANY finite normalized positive rational weights omega_i and ANY rational f_i in[0,d] with every actual value nonzero in O0.
Impose

    E=sum_i omega_i e_i<1, e_i=||f_i||^2.           (4)

No lag cancellation is needed yet.
Let B be the indices with residue not monomial in this window and let pi=sum_(i in B)omega_i.
The shell lemma gives

    E>=a_n(1-pi)+b_n pi
       =a_n+(1-3/n)pi,
    0<=pi<1/(n-3), E>=a_n.                        (5)

For n4 the upper endpoint is1 and the strict inequality still has its stated meaning.
The nonmonomial class may contain many distinct residues and arbitrarily small weights; (5) is a complete weighted mass bound, not a count bound or a unit-only restriction on the packet.
In particular no norm income has yet been dropped.

<a id="flat-all-residue-integer-representative-size"></a>
## 3. Every residue has an integer representative priced by its actual energy

Fix one actual f with energy e and use the integer z, x_i and mean mu from Section1.
Choose an integer k nearest mu, so |mu-k|<=1/2, and put z'=z-kP.
It is an integer coefficient polynomial of degree at most d with EXACTLY the same original nonzero residue.
On S, Cauchy--Schwarz and(3) give

    sum_(i in S)|z'_i|
      =sum_(i in S)|x_i-k|
      <=sqrt(n v)+n/2<=sqrt(n e)+n/2.

Outside S the coefficients are still integers z_j, so |z_j|<=z_j^2 and their l1 sum is at most b<=e.
Hence

    1<=||z'||_1<=e+sqrt(ne)+n/2<=n+2e.             (6)

The first inequality follows from nonzero residue, and the final bound uses sqrt(ne)<=(n+e)/2, giving the slightly sharper n+3e/2 before weakening.
A closest real coefficient projection alone would NOT be an integer representative; the explicitly chosen integer k is what preserves O0.
No dependence on the number of zero coefficient positions is hidden in (6).

At every original conjugate beta,

    |z'(beta)|<=||z'||_1 max(1,|beta|)^d.

Multiply over ALL original d conjugates.
For the ACTUAL nonzero signed norm D=Norm_(Q(alpha)/Q)(f(alpha)),

    0<=log|D|/d<=log(n+2e)+m(P).                   (7)

The lower bound is integrality; the upper bound uses(6) and the same original field and degree.
It does not estimate the norm by just one embedding, replace the residue by a rational nearest point, or assert the integer representative is coefficient-optimal.
Its role is to keep every potentially nonunit norm in the budget.

<a id="flat-all-residue-full-income-theorem"></a>
## 4. Full norm income and surplus vanish with growing flat support

Define complete norm income

    Lambda=(1/d)sum_i omega_i log|D_i|>=0.

Every index outside B has absolute norm1, so contributes zero.
If pi0 then Lambda0.
If pi>0, apply the concavity of the real logarithm to the actual conditional positive weights omega_i/pi on B.
With E_B=sum_(i in B)omega_i e_i<=E<1, equation(7) gives

    Lambda<=pi[log(n+2E_B/pi)+m]
            <=pi[log(n+2/pi)+m].                  (8)

For fixed n>=4,m>=0 the function g(x)=x[log(n+2/x)+m] is strictly increasing for x>0, since

    g'(x)=log(n+2/x)-2/(nx+2)+m
             >log n-1>=log4-1>0.

One elementary verification of log4>1 is to integrate1/t on[1,2] and[2,4], each integral being strictly greater than its right-endpoint rectangle of area1/2.
Thus (5) and(8), including the pi0 case, prove the explicit FULL income bound

    0<=Lambda<=[log(3n-6)+m]/(n-3).                (9)

The weak inequality avoids any endpoint optimizer claim.
Combining E>=a_n with(9) yields the main new all-residue statement:

**Theorem.**
For EVERY finite rational first-window packet satisfying the exact actual nonzero O0 domain and E<1, with arbitrary FINAL positive weights and no shared fractional class or representative restriction,

    0<Lambda-(1/2)logE
       <=[log(3n-6)+m(P)]/(n-3)
                   +(1/2)log[n/(n-1)].             (10)

All complete signed integer norms contribute through Lambda.
The strict positivity uses E<1 and Lambda>=0.
Neither covariance nor reciprocal structure is required for this upper estimate.
If the packet IS complementary, its full-surplus lower-bound use must also obey the accepted original-root expense recorded in Section5.

Along ANY sequence of flat inputs with n->infinity and bounded m(P), the right side of(10) tends to0.
Therefore no selection of below-one first-window packets in this ENTIRE actual residue domain can retain a fixed positive full surplus on such a sequence.
This quantifies norm income as well as C25's old energy floor.
It does not assume that a near-one sequence exists, that support grows in every such sequence, or that fixed-support inputs are covered.
It is not a theorem about windows d+1 or larger, E>=1 packets, nonflat inputs or a general uniform Mahler gap.

<a id="flat-all-residue-actual-denominators-and-norms"></a>
## 5. Exact physical width and all original scalar and copy costs

Now also assume every positive lag sum is zero, so the finite packet has constant circle covariance E.
The allowed window is[0,d].
If its ACTUAL common union width were less than d, one common monomial shift would place it in[0,d-1], retaining all nonzero O0 values because alpha is a unit, and retaining E and all lags.
The accepted monogenic short-width theorem C17 would then force E>=1, contradicting(4).
Its actual width is therefore EXACTLY d; this argument is not extended to an overorder.

Let q be the ACTUAL least common coefficient denominator, F_i=qf_i in Z[t], and M the ACTUAL least denominator of the FINAL indexed weights.
Set k_i=M omega_i>0 integers, sum k_i=M.
For every index retain D_i=Norm_(Q(alpha)/Q)(f_i(alpha)) as a nonzero SIGNED integer.
Then

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(k_i)=q^(dM)product_i D_i^(k_i),
    S_int=sum_i omega_i||F_i||^2=q^2E,
    I_income=(1/(dM))log|product_i Res(P,F_i)^(k_i)|
             =logq+Lambda,
    I_income-(1/2)logS_int=Lambda-(1/2)logE<=m(P).   (11)

The last inequality is C10's generic direct proof with actual T/d=1, applied ONLY after complementarity and using the SAME final weights.
Combining (10)--(11) is legitimate on this same packet.
Logq cancels only after both actual charges are retained; there is no assumption q=M, bounded q, primitive numerators or a unit-only norm inventory.
If a numerator F_i has content b_i>1, the factor b_i^d remains in its full signed resultant.
No normalization erases it.
Every negative norm and copy exponent remains in the product even though Lambda uses absolute logarithms.

For a packet initially supported in any interval of union width d, a single common integer monomial normalization identifies the same setting because alpha is an actual unit.
Coefficient energy, Lambda and q are unchanged; signed norms are multiplied by the known original unit norm power, so the copied signed product retains that factor.
The classification of monomial residues is then relative to the normalized window.
The theorem is not about shifting different atoms separately and pretending their common physical width is preserved.

<a id="flat-all-residue-comparisons-and-open-gate"></a>
## 6. Existing controls and the changed quantitative obligation

C25 already proves E_d>=1-1/n and necessary first-window q>n/2.
C29 already makes nonzero cross terms necessary.
The present proof adds a complete nonmonomial mass and norm-income estimate over ALL actual residues, so allowing arbitrary q, different per-atom fractions of P, larger integer coefficients, arbitrary correlations or nonunit values WITHIN E<1 and the FIRST window cannot invalidate(10).
The all-subset/common-marginal author result D16 is a narrower construction-level calculation and is not a premise for this broader theorem.
Its source and review history remain separate; no pending result is silently adopted.

At the original Lehmer input n9, the shell bounds are a9=8/9 and b9=14/9, with pi<1/6 and Lambda<=[log21+m]/6.
This does not rule out the accepted C31 below-one packet or assert its full capacity optimum.
It prices every such packet by a generally loose bound.
At the original quartic n5 the corresponding values are4/5,6/5, pi<1/2; again the bound permits the accepted C58 correlated packet.
These are substitutions in the proved formulas, not new numerical experiments or newly certified packet norms.

The first-window hypothesis has real force.
C25/C29 already record dense flat inputs with a DIFFERENT actual window d+1 admitting a dyadic E1/2 packet.
Their coefficient kernel has two directions; the one-dimensional projection identity(3) no longer describes all representatives.
Thus the present barrier neither contradicts that existing escape nor rules out a constant multiple of degree.
The unrestricted quantitative target still calls for an actual original same-packet surplus at a controlled wider width, or another domain/mechanism, with every original norm and final weight charged.
The full all-residue barrier identifies a precise reason not to pursue uniform below-one gain by merely making the FIRST-window search more complete.

<a id="flat-all-residue-entire-author-freeze"></a>
## 7. Complete author self-check and frozen handoff

Root checked the actual monic-order representation and integer ambiguity, original nonzero residue and arbitrary nonreciprocal signs; sparse support/outside-coordinate integer squares, range0/1/atleast2 cases, exact monomial exceptions and the positive shell separation only for n>=4; all per-label and averaged energy inequalities, pi0 and n4 boundaries; actual integer mean rounding rather than an illegal real representative, l1 bounds independent of zero-position count, full original-root norm product and unit-label contribution; conditional Jensen and the monotonicity endpoint; growing-support/bounded-measure quantifiers; actual physical width, common normalization, true q/FINAL M, contents/signed copies and C10 scope; all old baseline/controls and the genuine wider-window limitation.
No unproved source theorem or native process is a premise.
This self-check is author evidence only.

Freeze the ENTIRE allocation and Sections1--7/equations1--11, original reuse/contribution record, second-shell proof, all norm/width/denominator costs and all scope exclusions at 2026-10-12T11:30.
Root alone supplied this new mathematics and cannot independently review it.
A separate actual whole review and, if later extracted, a distinct new Claim-wrapper review are required before adoption.
G0001 remains active and unrestrictedly unresolved; no new execution allowance is created.
