---
author: Yin
---
# Exact finite Blaschke defect rank, complete inverse spectra and quantitative lag detection

The complete original five sections and19equations are retained with every spectral/original-law boundary and source scope.
L268 keeps its meaningful development, original contribution/fixed inputs and separate probability handoff; no Task/E execution resumes.
The [later full comparison of original R167](../audits/reviews/Yin_R_G0687_v1.md#l268-and-r167) preserves its whole historical UNKNOWN, exact09:52 author-body/09:55 review and distinct original author SELF/source/negative limits.
The unchanged whole-checking account and earlier decision below record the06:55 R684 SELF and06:56 adoption; the selected07:26 decision adopts the later R687 independent whole finding.

## Statement

Let P be the ACTUAL monic minimal polynomial of ANY nonzero algebraic integer, degree d>=1 and TOTAL logarithmic Mahler measure m>0.
Include EVERY exterior conjugate alpha_1,...,alpha_r, with multiplicities/both members of complex pairs, so1<=r<=d and sum_v log(abs(alpha_v))=m.
Set

    s=exp(-m), beta_v=1/alpha_v,
    N(z)=product_v(1-alpha_v*z),
    D(z)=product_v(1-conj(beta_v)*z),
    B(z)=s*N(z)/D(z),H(z)=s/B(z)=D(z)/N(z)
                            =sum_(j>=0)h_j*z^j,h0=1.

N,D have EXACT degree r and are coprime, with zeros strictly inside/outside the disk.
B is the actual normalized finite Blaschke product, analytic across the closed disk and unimodular on the circle, with B(0)=s>0 and real coefficients.
Original unit-circle roots remain in the separately justified outer closure; no original d or probability normalization is replaced by r.
H is formal at0/analytic only up to its first nonremovable pole, and is not assumed to have disk-boundary l2 values.

For EVERY integer n>=1, let E_n be all polynomials of degree<n with coefficient Euclidean norm, Pi_n retain their first n coefficients, T_n u=Pi_n(Bu) and Q_n u=(I-Pi_n)(Bu).
Then T_n is lower triangular with diagonal s and determinant s^n, and

    norm(u)^2=norm(T_nu)^2+norm(Q_nu)^2,
    I-T_n^*T_n=Q_n^*Q_n>=0,
    ker Q_n={D*v:deg v<n-r},
    rank Q_n=min(n,r).

The kernel is{0} for n<=r; exact degrees/coprimality prove both directions, including repeated factors, with no cancellation or nonminimal recurrence inference.
For EVERY integer n>=r, exactly n-r singular values of T_n equal1 and the other r are strictly between0 and1.
The lower Toeplitz inverse-coefficient matrix

    H_n=(h_(i-j))_(0<=j<=i<n),zero for i<j,
    H_n=s*T_n^-1

has EXACTLY n-r singular values s, while its other r values gamma_v>s obey product_v gamma_v=s^(-(n-r)).
The full noncommuting-order identity is

    H_n^*H_n-s^2I
       =s^2*T_n^(-*)*(I-T_n^*T_n)*T_n^-1>=0,

of EXACT rank r.
At n=r the flat multiplicity is0 and the large-value product is1.
Consequently, for EVERY n>=r,

    normop(H_n)>=exp[m(n/r-1)],
    normF(H_n)^2>=(n-r)exp(-2m)+r*exp[2m(n/r-1)],
    sum_(j=1)^(n-1)(n-j)*abs(h_j)^2
       >=r*(exp[2m(n/r-1)]-1)
                    -(n-r)*(1-exp(-2m)),
    max(1,max_(1<=j<n)abs(h_j))
       >=exp[m(n/r-1)]/n.

The weighted bound is strictly positive for n>r and a correct weak0 bound at n=r.
The ENTIRE n-term diagonal contribution is subtracted, and the diagonal1 in the maximum is retained; no infinite inverse square sum is used.

For EVERY real0<m<=1 and threshold A>=1, put

    x=r/m>=1,y=8*A*x>=8,
    n_A=r+ceil(2*x*log y).

There is an ACTUAL nonconstant coefficient with1<=j<n_A and abs(h_j)>A, STRICTLY.
All ceilings and guards are retained: n_A<=x*(2+2log y), the norm lower bound is>=y^2, while A*n_A<=y^2/4<y^2.
This is an explicit O((r/m)log(Ar/m)) lag budget, independent of root separation or a selected residue, not a bound independent of m,r or an original-law probability theorem.

On the ACTUAL irreducible golden radicals P_r=t^(2r)-t^r-1,r=2^u,u an integer>=0, phi=(1+sqrt5)/2, d2r and FIXED m=log phi,

    H=(1-phi^-1*z^r)/(1-phi*z^r),
    h_(kr)=phi^(k-1),k>=1,h_j=0 if r does not divide j.

For EVERY n>=r write n=q*r+t,0<=t<r.
Residue-coordinate orthogonal splitting gives the ENTIRE spectrum

    s with multiplicity n-r,
    exp(m*q) with multiplicity t,
    exp(m*(q-1)) with multiplicity r-t.

At t0 the full operator/Frobenius/weighted-energy bounds are equalities.
At q1 some large values are1 but still>s.
The first nonzero coefficient is1 at lag r, and the first coefficient STRICTLY greater than1 is at2r.
Actual irreducibility/degree/relative degree are proved before the residue argument, with no padding or chronological rate division.

The separate ANALYTIC comparison H_(m,r)=(1-exp(-m)z^r)/(1-exp(m)z^r), for arbitrary real m>0 and integer r>=1, has the same entire spectra, nonzero coefficients2sinh(m)*exp((k-1)m), and attains the spectral bounds at n divisible by r.
Its small-m threshold delay for reaching1 has order(r/m)log(1/m), without an asserted arithmetic realization or near-one counterexample.

For EACH fixed actual input and EACH fixed n>=r, the real upper digit-coordinate block C_i from actual T=R U^-1 tends entrywise to H_n^T as i->infinity, with actual pivots tending exp(2m).
Its full weighted precision therefore tends to

    G_infinity,n=(log2)*exp(2m)*(H_n^T)^*H_n^T
                =(log2)*I+K_n,K_n>=0,rank K_n=r.

All n-r baseline eigenvalues are exactly log2; the other r, their determinant product and orientation are not discarded.
For0<m<=1,A>=1 the detected coefficient above gives an INPUT-DEPENDENT onset I such that abs(T_(i,i+j))>A for EVERY i>=I.
That residual onset is neither effective nor bounded by the explicit coefficient lag n_A.

The rank-r positive penalty/singular amplitude does not alone control a translated finite integer-cube partition: its orientation, all middle entries/other directions/outside shifts and original first-d discarded rows remain costs.
Disjoint length-n_A blocks have at most chronological density1/n_A; this spectral proof supplies no uncharged loss or entropy inequality.
The separately proved C469 arbitrary-coupling theorem retains its own full original-law scope; no new cross-application is derived or adopted in this compression theorem.
The original D132--D134 reports are not premises.
Partington supplies only its already audited classical rational-tail/minimality attribution, while the complete kernel/rank/norm/threshold/transfer proof is local.
CRW08 is only the bounded original title/intro/(1.2) lead, with later proofs uninspected and no quantitative theorem adopted.
No program, native numerical evidence, new source proof, unrestricted near-one coverage, improved complete scalar cost, gap or Task completion follows.

<a id="argument"></a>
## Complete retained argument

The dated original argument retains its chronological D134/probability-gate wording; it states only this spectral theorem, without silently deriving a cross-application from the separate current block-loss proof.

<a id="inverse-compression-reuse"></a>
### 1. Needed interface, reuse and attribution

The new question after [L264](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) is quantitative: can its inverse coefficient limsup be replaced by an explicit lag budget, without assumptions about separated roots or an arbitrarily selected pole residue?
[L263](Yin_C_G0459_v1.md#all-lag-actual-center-limits) identifies these coefficients as the actual limiting digit-coordinate couplings, but does not control a long block through its whole intervening matrix.
That latter probability question remains separate.

The local G-ledger screen by inverse lag, singular values, compressed inner multiplication, defect rank and Hankel found L101/L263/L264 and earlier matrix-cost arguments, but no retained explicit inverse-threshold bound.
[L101](Yin_C_G0296_v1.md#endpoint-row-hardy-closure) supplies the actual normalized finite Blaschke factor and its isometric multiplication proof.
The literature registry then located the already audited [Par88-U001](../audits/literature/Par88/Yin_U001.md#par88-u001): Theorem3.11, printed pp.37-38, with minimality and denominator-cancellation guards.
Its classical rational-tail/finite-Hankel-rank mechanism is relevant attribution, not a claim of a new finite-rank theorem.
The finite polynomial kernel below verifies the exact compression rank directly in our conventions, without requiring a general Kronecker converse.

A bounded external terminology search also inspected the title, introduction and (1.2) on pp.1-2 of the public [Cima--Ross--Wogen author manuscript](../audits/literature/CRW08/Yin_U001.md#crw08-u001).
Its finite model-space representations concern a related compression and supply no adopted quantitative inverse-lag conclusion here.
It is a screened lead, not a registered new theorem input, and its later proofs were not audited.
No external absence or novelty claim is made.
The existing rational-tail mechanism suffices, so the search stops there.

All new deductions below use the actual exterior roots and ordinary finite-dimensional singular values.
No new program, numerical experiment or source artifact is needed.
The simultaneous D132-D134 arguments are not proof inputs.
Root reported the emerging singular-value interface to the structural agent as a candidate; that report is not a completed review or an imported premise.

<a id="finite-inner-compression-exact-rank"></a>
### 2. Actual compression and exact defect rank

Let P be the actual monic minimal polynomial of a nonzero algebraic integer, of degree d and total logarithmic Mahler measure m>0.
Include all exterior conjugates alpha_1,...,alpha_r, so 1<=r<=d and sum log|alpha_v|=m.
Use the actual functions from L264:

    s=exp(-m), beta_v=1/alpha_v,
    N(z)=product_v(1-alpha_v z),
    D(z)=product_v(1-conj(beta_v)z),
    B(z)=s N(z)/D(z),
    H(z)=s/B(z)=D(z)/N(z)=sum_(j>=0)h_j z^j,
    h_0=1.                                                 (1)

Every beta_v is nonzero and strictly inside the disk.
N and D have exact degree r and are coprime: their zeros lie strictly inside and outside the unit circle, respectively.
B is analytic on a neighborhood of the closed disk and has modulus one on the circle; H is only a formal Taylor series at zero (analytic up to its first pole).
Its finite initial coefficients are always meaningful.
Neutral original roots remain in L101's original closure argument and do not contribute factors to B.
No degree or probability normalization is changed from d to r.

Let E_n be the polynomials of degree less than n with coefficient Euclidean norm, and let Pi_n retain their first n coefficients.
Define the lower triangular n-by-n matrix

    T_n u = Pi_n(Bu),  u in E_n.                           (2)

Its diagonal is s and det T_n=s^n.
Multiplication by B is an isometry by L101, so for the tail map Q_n u=(I-Pi_n)(Bu),

    ||u||^2=||T_n u||^2+||Q_n u||^2,
    I-T_n^* T_n=Q_n^* Q_n >=0.                            (3)

Here * denotes conjugate transpose.
The exact kernel is elementary.
Q_n u=0 if and only if Bu is a polynomial of degree less than n.
Coprimality in (1) then forces D to divide u; conversely u=Dv gives Bu=sNv, with degree r+deg v=deg u<n.
Consequently

    ker Q_n={Dv:deg v<n-r},
    rank Q_n=min(n,r).                                    (4)

The first set is {0} if n<=r.
Polynomial degrees cannot cancel in this argument since N and D both have exact degree r.
It includes repeated roots and needs no chosen pole residue or root-separation estimate.
The identity also shows that the compressed tail has precisely the expected rational/Hankel rank, rather than inferring exact rank from a nonminimal annihilating recurrence.

For n>=r, exactly n-r singular values of T_n equal1 and the remaining r belong to (0,1).
Invertibility excludes zero.
Let

    H_n=(h_(i-j))_(0<=j<=i<n), with zero entries for i<j.
    H_n=s T_n^(-1).                                      (5)

Finite Taylor convolution proves (5); it does not use H on the unit circle.
Therefore exactly n-r singular values of H_n equal s, its other r singular values gamma_1,...,gamma_r exceed s, and

    product_(v=1)^r gamma_v=s^(-(n-r)).
    H_n^* H_n-s^2 I >=0,  rank(H_n^*H_n-s^2 I)=r.          (6)

For example the last matrix equals s^2 T_n^(-*) (I-T_n^*T_n) T_n^(-1); thus its rank and positivity also follow directly from (3)-(4).

<a id="inverse-spectrum-energy-budget"></a>
### 3. Explicit norm and weighted coefficient bounds

The product in (6) and the arithmetic--geometric mean inequality give, for every integer n>=r,

    ||H_n||_op >= exp[m(n/r-1)],                           (7)
    ||H_n||_F^2 >= (n-r)exp(-2m)
                    + r exp[2m(n/r-1)].                  (8)

At n=r these are nonstrict, useful baseline bounds.
Since h_0=1 and the j-th lower diagonal has n-j entries,

    sum_(j=1)^(n-1)(n-j)|h_j|^2
       >= r(exp[2m(n/r-1)]-1)
                         -(n-r)(1-exp(-2m)).              (9)

The right side is strictly positive when n>r: exp(x)>=1+x and 2m>1-exp(-2m) prove this.
Thus (9) is an actual finite energy lower bound for the INVERSE coefficients, not the direct energy equality of L264.
No infinite square-sum of H is formed.

For a simple threshold statement, put M_n=max(1,|h_1|,...,|h_(n-1)|).
Every row and column of H_n has absolute sum at most n M_n, whence ||H_n||_op<=n M_n.
(The inequality follows from Cauchy--Schwarz with row and column sums, or directly from the Frobenius bound.)
In combination with (7),

    max(1,max_(1<=j<n)|h_j|)
                  >= exp[m(n/r-1)]/n.                    (10)

The diagonal 1 in this maximum must not be forgotten when the right side is at most1.

Here is a fully explicit threshold in the near-one range.
For 0<m<=1 and any A>=1, define

    x=r/m >=1,
    y=8 A x >=8,
    n_A=r+ceil(2 x log y).                               (11)

Then there is some 1<=j<n_A with

    |h_j|>A.                                             (12)

Indeed r<=x and ceil t<=t+1 imply n_A<=x(2+2 log y).
Meanwhile (7) is at least y^2, whereas

    A n_A <= (y/8)(2+2 log y) <= y^2/4 < y^2,             (13)

using log y<=y-1.
If all nonconstant coefficients had modulus at most A, then M_(n_A)<=A and (10) would contradict (13).
All ceilings and strict inequalities are retained.
Thus a coefficient above a fixed threshold is found by an explicit O((r/m)log(Ar/m)) lag budget.
The constant is deliberately coarse, not claimed optimal; the bound is uniform over all locations and multiplicities of the actual exterior roots with those m,r.

This improves the L264 qualitative limsup to finite detection.
It does not give a lag bound independent of m,r, nor imply a useful chronological entropy correction.

<a id="actual-inverse-spectrum-sharp-control"></a>
### 4. Exact spectrum on actual irreducible radical controls

Reuse the actual [L231 dyadic radical family](Yin_C_G0212_v1.md#radical-collision-control), already checked in L263/L264:

    P_r(t)=t^(2r)-t^r-1, r=2^u,
    phi=(1+sqrt5)/2, m=log phi, d=2r,
    H(z)=(1-phi^(-1)z^r)/(1-phi z^r),
    h_(kr)=phi^(k-1) for k>=1,
    h_j=0 when r does not divide j.                       (14)

This is an actual irreducible family, not added cyclotomic padding or a freely selected analytic root set.
Its measure is fixed and positive.

For n>=r write n=qr+t, 0<=t<r.
Reordering the coefficient basis by residues modulo r splits H_n orthogonally into r single-factor blocks: t of size q+1 and r-t of size q.
Each block has degree-one normalized B with s=phi^(-1).
By the already proved exact rank-one identity (6), a size k block has singular values s repeated k-1 times and s^(-(k-1)) once.
Hence the ENTIRE spectrum is

    s with multiplicity n-r,
    exp(m q) with multiplicity t,
    exp(m(q-1)) with multiplicity r-t.                    (15)

If t=0 the r large values all coincide.
Both the norm lower bound (7) and the Frobenius lower bound (8), hence (9), are then equalities.
For q=1 some listed large values equal1; they remain strictly greater than s.
The actual family therefore attains the finite spectral bounds at all n divisible by r and demonstrates the continuing degree-dependent delay.
For example its first coefficient strictly greater than1 is at lag2r, although the first nonzero coefficient is at lag r.

For comparison only, L264's analytic normalized product

    H_(m,r)(z)=(1-exp(-m)z^r)/(1-exp(m)z^r)                (16)

has the same spectrum formulas (15) with arbitrary m>0; the nonzero coefficients become 2sinh(m)exp[(k-1)m].
This analytic class attains the spectral bounds too, but is not asserted arithmetically realizable for every m.
Its threshold lag for reaching1 grows on the order (r/m)log(1/m).
Thus exact spectral amplification is compatible with a large chronological delay even before original-law costs are considered.
It supplies no family refuting Lehmer.

<a id="inverse-compression-original-law-interface"></a>
### 5. Transfer to actual finite coupling blocks and retained costs

For each fixed n, L263 proves entrywise convergence of the actual n-by-n upper triangular digit-coordinate block beginning at index i to H_n^T, with real coefficients.
The actual pivots delta_(i+j) converge to exp(2m).
Consequently its finite weighted precision matrix converges to

    G_infinity,n = (log2) exp(2m) (H_n^T)^* H_n^T.         (17)

At every fixed actual input and fixed n>=r, (6) implies

    G_infinity,n = (log2) I + K_n,
    K_n>=0, rank K_n=r.                                  (18)

Transpose preserves singular values; here all entries are real, so the displayed adjoint conventions agree.
The n-r baseline precision eigenvalues are exactly log2.
The other r have their full determinant product and are not omitted from any volume calculation.
Equation (18) describes a real positive quadratic penalty, not its orientation relative to the integer digit cube.

Fix A>=1 and n_A from (11).
Choose the index j from (12).
Actual fixed-diagonal convergence gives an input-dependent I such that

    |T_(i,i+j)|>A for every i>=I.                         (19)

Choose the error smaller than half the positive difference |h_j|-A.
This proves an all-future actual finite-matrix statement; no uniform or effective estimate for I is obtained.
The explicit coefficient-lag budget and the still-uncontrolled residual onset are different quantities.

Even a huge singular value does not automatically lower a translated finite integer partition by a useful uniform factor.
The directions may depend on P, the other r-1 directions, the integer cube and the outside-tail translation must all be charged, and the original first d constraints were discarded by L263's triangular upper bound.
Its single-corner perturbation lemma cannot simply be invoked on an arbitrary long block with many large intervening entries.
A block estimate must retain every such entry or control its actual effect.

Further, disjoint length-n_A blocks have chronological density at most1/n_A.
A merely bounded logarithmic saving per block would still give at most that bound divided by n_A.
Equations (7)-(19) prove no saving at all until a valid original-law partition estimate is supplied.
They must not be substituted into an entropy rate without this missing argument, nor treated as an independent proof of the simultaneously explored D134 conjectures.

The changed next question is therefore concrete: use the entire finite-rank positive penalty (18), or actual integer lower-row constraints, to establish a translated digit-partition bound whose saving grows sufficiently with the full paid block length.
An explicit large inverse coefficient now exists within (11); another pole/limsup argument alone would repeat established detection.



### Actual whole checking and source limits

The maintaining agent read the only actual L268 version and ENTIRE R167, both Par88-U001 versions and the exact CRW08 original/source-metadata records, then compared the complete necessary C296/C459/C461/C212 mechanisms.
It checked every exact degree/coprimality/kernel direction, n<=r/rank boundary, polynomial isometry/tail decomposition and all inverse matrix orders/multiplicities/products, without applying an infinite boundary operator to H.
Both norm bounds and the weighted coefficient inequality retain every flat/diagonal term; the n>r positivity and max-with1 guard were checked.
The full0<m<=1,A>=1 threshold includes its strict j<n_A, all ceiling estimates and the entire contradiction, not an asymptotic-only detector.
Actual norm-minus-one degree/relative degree precedes residue splitting; every q/t/n-r spectral multiplicity, t0 equality, q1 boundary, actual first r/2r lag and separate analytic arbitrary-m limitation was checked.
The actual upper-block transpose, full weighted precision, exact baseline/rank-r penalty and all-future but unquantified onset were checked without an unproved original-law/translated-cube conclusion or free chronological density.
The current C469 theorem is a separate complete proof; no new cross-application or D132--D134 premise is supplied here.
Par88's already sufficient current unit retains the exact original theorem scope and distinct10/10 passage inspection, without new source reading.
CRW08 only retains the original bounded lead; the current publisher/title/author/page-count metadata check does not backfill the old unknown snapshot or adopt new mathematical passages/proofs.
R167's generic shared context and claimed-scope brief do not establish its exact initial proof-relevant additional content/order; necessary fixed inputs/upstream roles do not automatically establish target SELF or isolation.
Its ENTIRE original mathematical/source/control finding remains UNKNOWN, with original09:52 author-body/09:55 whole-review facts preserved.
The original coordinating author supplied the proof and day-precision SELF; those original times are not invented as source-reading/checking minutes.
No program/J/native, numerical experiment, new source proof/PDF acquisition, producer or Task/E execution occurred.
Current whole SELF supplies no fresh isolation or unrestricted gap.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:53 |
| status | open |
| reason | Retain the complete original exact polynomial kernel/defect rank, full finite inverse singular values/products/norms/weighted coefficient/strict-threshold proof, every actual and analytic control, upper-block/precision/onset/orientation/density and original source/negative limit. Adequate existing mechanisms and original source scopes were compared; no new mathematical research or producer/source-proof execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole compression and threshold theorem](#statement) | Every actual m>0 polynomial/all exterior roots/all finite n-r boundaries, exact kernel/rank/full singular products/norms/weighted coefficients, strict guarded threshold/all ceilings, entire actual/analytic spectra and actual upper-block transpose/precision/onset/orientation/density/source/negative limits. |
| argument | [Entire retained proof](#argument) | Complete original Sections1--5/equations1--19, exact degrees/coprimality/polynomial-tail kernel/H2 isometry, correct inverse matrix order/products/whole diagonal energy, strict threshold, every radical/analytic multiplicity and all finite original-law cost boundaries. |
| dependency | [Actual normalized H2 isometry](Yin_C_G0296_v1.md#endpoint-row-hardy-closure) | Complete actual normalized Blaschke/outer factorization, unit-circle-root cyclic closure and polynomial-density/Parseval isometry; no source spectral theorem or inverse boundary l2. |
| dependency | [Actual inverse/root distinction](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Full exact N-D noncancellation/interior poles/inverse recurrence and actual radical versus freely analytic coefficients/delay, no direct-l2 budget or GMR18 derivative premise. |
| dependency | [Actual fixed-diagonal limits](Yin_C_G0459_v1.md#all-lag-actual-center-limits) | Entire reversed finite residual/convolution/T=R U^-1 fixed-lag and pivot convergence, including neutral roots, actual original degree and nonunit word scope; no uniform onset or free probability loss. |
| dependency | [Actual radical degree and product](Yin_C_G0212_v1.md#radical-collision-control) | Full norm-minus-one dyadic tower/actual irreducible degree2r/relative degree r before residue splitting; no varying-r rate normalization or small-measure family. |
| support | [Sufficient classical rational-tail attribution](../audits/literature/Par88/Yin_U001.md#par88-u001) | Exact reduced-denominator/minimal-recurrence/inactive-pole guards, original9/9 audit and9/10 definitions plus distinct original10/10 author reuse/reviewer same-passage inspection retained, no new source proof or bounded-Hankel assertion for H. |
| support | [Original bounded compression lead](../audits/literature/CRW08/Yin_U001.md#crw08-u001) | Original10/10 title/intro/(1.2)pp1--2 only, later proofs not read/no quantitative theorem premise; current identity/11-page metadata and unknown old snapshot distinct from published13-page edition. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:56 |
| status | proved |
| reason | Adopt after the actual ENTIRE C475/R684 SELF inspection of all original Sections1--5/equations1--19, exact degree/coprimality/kernel/rank/isometry, full inverse matrix orders/singular products/flat-diagonal energy, guarded strict finite threshold/ceilings, every actual/analytic spectrum and upper-transpose/precision/onset/orientation/density/source/negative boundary. Adequate C296/C459/C461/C212 and original Par88/CRW08 scopes were compared; old R167 whole UNKNOWN and original author SELF remain exact. No source proof/program/PDF/new research/Task execution or fresh isolated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole compression and threshold theorem](#statement) | Every actual m>0 polynomial/all exterior roots/all finite n-r boundaries, exact kernel/rank/full singular products/norms/weighted coefficients, strict guarded threshold/all ceilings, entire actual/analytic spectra and actual upper-block transpose/precision/onset/orientation/density/source/negative limits. |
| argument | [Entire retained proof](#argument) | Complete original Sections1--5/equations1--19, exact degrees/coprimality/polynomial-tail kernel/H2 isometry, correct inverse matrix order/products/whole diagonal energy, strict threshold, every radical/analytic multiplicity and all finite original-law cost boundaries. |
| dependency | [Actual normalized H2 isometry](Yin_C_G0296_v1.md#endpoint-row-hardy-closure) | Complete actual normalized Blaschke/outer factorization, unit-circle-root cyclic closure and polynomial-density/Parseval isometry; no source spectral theorem or inverse boundary l2. |
| dependency | [Actual inverse/root distinction](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Full exact N-D noncancellation/interior poles/inverse recurrence and actual radical versus freely analytic coefficients/delay, no direct-l2 budget or GMR18 derivative premise. |
| dependency | [Actual fixed-diagonal limits](Yin_C_G0459_v1.md#all-lag-actual-center-limits) | Entire reversed finite residual/convolution/T=R U^-1 fixed-lag and pivot convergence, including neutral roots, actual original degree and nonunit word scope; no uniform onset or free probability loss. |
| dependency | [Actual radical degree and product](Yin_C_G0212_v1.md#radical-collision-control) | Full norm-minus-one dyadic tower/actual irreducible degree2r/relative degree r before residue splitting; no varying-r rate normalization or small-measure family. |
| support | [Sufficient classical rational-tail attribution](../audits/literature/Par88/Yin_U001.md#par88-u001) | Exact reduced-denominator/minimal-recurrence/inactive-pole guards, original9/9 audit and9/10 definitions plus distinct original10/10 author reuse/reviewer same-passage inspection retained, no new source proof or bounded-Hankel assertion for H. |
| support | [Original bounded compression lead](../audits/literature/CRW08/Yin_U001.md#crw08-u001) | Original10/10 title/intro/(1.2)pp1--2 only, later proofs not read/no quantitative theorem premise; current identity/11-page metadata and unknown old snapshot distinct from published13-page edition. |
| review | [Actual complete whole SELF](../audits/reviews/Yin_R_G0684_v1.md#inverse-compression-whole-self-finding) | ENTIRE exact statement/argument/inputs, every n-r/kernel/rank/singular/norm/weighted-energy/strict-threshold/ceiling/actual-and-analytic/full-precision/onset/orientation/chronological/source/control/negative scope; no new probability cross-application or isolated coverage. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:26 |
| status | proved |
| reason | Adopt the actual new whole independent R687 after direct full reading of its23647-character finding and the literal complete C475 Statement/Sections1--5/19 equations. Its necessary fixed-U source-scope prose was actually read before the first07:11 finding and supplies no new target derivation, prior PASS or development discussion; that precise actual sequence is disclosed, without claiming zero target-related prose exposure. All finite kernel/product/energy/strict-threshold and actual-block/source/law/negative limits are covered; the entire original R167 remains historically UNKNOWN and original/R684 SELF stay SELF. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every actual m>0 polynomial/all exterior roots/all finite n-r boundaries, exact kernel/rank/full singular products/norms/weighted coefficients, strict guarded threshold/all ceilings, entire actual/analytic spectra and actual upper-block transpose/precision/onset/orientation/density/source/negative limits. |
| argument | [Exact argument](#argument) | Complete original Sections1--5/equations1--19, exact degrees/coprimality/polynomial-tail kernel/H2 isometry, correct inverse matrix order/products/whole diagonal energy, strict threshold, every radical/analytic multiplicity and all finite original-law cost boundaries. |
| dependency | [Exact dependency](Yin_C_G0296_v1.md#endpoint-row-hardy-closure) | Complete actual normalized Blaschke/outer factorization, unit-circle-root cyclic closure and polynomial-density/Parseval isometry; no source spectral theorem or inverse boundary l2. |
| dependency | [Exact dependency](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Full exact N-D noncancellation/interior poles/inverse recurrence and actual radical versus freely analytic coefficients/delay, no direct-l2 budget or GMR18 derivative premise. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#all-lag-actual-center-limits) | Entire reversed finite residual/convolution/T=R U^-1 fixed-lag and pivot convergence, including neutral roots, actual original degree and nonunit word scope; no uniform onset or free probability loss. |
| dependency | [Exact dependency](Yin_C_G0212_v1.md#radical-collision-control) | Full norm-minus-one dyadic tower/actual irreducible degree2r/relative degree r before residue splitting; no varying-r rate normalization or small-measure family. |
| support | [Exact support](../audits/literature/Par88/Yin_U001.md#par88-u001) | Exact reduced-denominator/minimal-recurrence/inactive-pole guards, original9/9 audit and9/10 definitions plus distinct original10/10 author reuse/reviewer same-passage inspection retained, no new source proof or bounded-Hankel assertion for H. |
| support | [Exact support](../audits/literature/CRW08/Yin_U001.md#crw08-u001) | Original10/10 title/intro/(1.2)pp1--2 only, later proofs not read/no quantitative theorem premise; current identity/11-page metadata and unknown old snapshot distinct from published13-page edition. |
| review | [Exact review](../audits/reviews/Yin_R_G0687_v1.md#whole-compression-independent-finding) | Whole exact finite-compression kernel/rank/singular-product/norm/weighted-energy/strict-threshold theorem, complete19 equations and all actual-degree/radical/analytic controls, original upper transpose/full precision/orientation/full-tail/onset/chronology/source/probability negative boundaries. |

