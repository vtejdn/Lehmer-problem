---
author: Yin
---
# Effective finite first-window dictionaries with bounded rational packet arithmetic

Date: 2026-10-12T11:12.
Human author Yin.
Root authored the entire original D14 mathematical proof.
g0001_review_recovery independently reviewed its original18:57 scope in R268 and its actual19:05 corrected whole scope in R269, and NOW authors this new fixed statement/wrapper.
This reviewer is therefore a contributor to the new extraction and cannot independently review it.
The ENTIRE corrected author body, original freeze, literal norm-field objection and dated correction are retained below.
Initial status remains proof draft / under review pending a different noncontributor's actual extraction review.

## Statement

Let P=sum_(j=0)^d p_j t^j in Z[t] be an ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, p_d=1 and p_0 in{+1,-1}.
Use actual O0=Z[alpha], the ORIGINAL field Q(alpha), its integer power-basis remainder matrix A=[I_d,a_d], and coefficient height H=max_j|p_j|>=1.
No reciprocity, trace signature, coefficient flatness or unit-only residue inventory is required.

Let E_d^Q be the infimum of weighted coefficient energy over finite rational coefficient packets in allowed window[0,d], positive normalized RATIONAL weights, every value a NONZERO actual O0 integer, and EVERY aggregate positive lag equal to zero.
Supply a PROVED RATIONAL deficit

    0<delta<=1/2, E_d^Q<=1-delta

for this SAME actual input.
The adopted C57 elementary delta_elem(d) is one available rational choice, independent of coefficient height; no optional house theorem is needed for that choice.
The theorem below does not assume an optimizer of E_d^Q.

**A. Explicit finite rational dictionary.**
Define

    N=d+1, eta=delta/100, D=N+1,
    B=ceil(8N^2/eta),
    R=4(4d)^d, rho=1/R^2,
    L=ceil(D/eta), F=L d R, J=N H,
    Q=ceil(D J(2F+J)/eta),
    U=Q max{B+2,R+F H}, K_bound=N U^2,
    M_max=N! K_bound^N.

Here Q is the GRID coefficient denominator, not the eventual actual denominator q or FINAL weight denominator M.
K_bound is an INTEGER bound, not a number field; it equals the original proof's scalar K=N U^2.
All constants are finite integers/rationals computed from d,H,delta.

Let Dcal be the union of these FINITE atom sets, identifying duplicate coefficient vectors if desired:

1. All INTEGER polynomials z of degree<=d with every |z_j|<=B+2 and Az nonzero.
2. All g_(r,k)=sum_(j=0)^(d-1)r_j t^j+(k/Q)P(t), for NONZERO r in Z^d with |r_j|<=R and integers |k|<=QF.

Every atom has a NONZERO actual value in O0, coefficient denominator dividing Q and integer numerator Qg of height at most U.
The actual atoms1 and1+/-t^h,1<=h<=d, belong to Dcal.
This definition uses exact remainder arithmetic, with no numerical embedding or native enumeration premise.

**B. Strict finite optimum, bounded support and ACTUAL denominators.**
On Dcal minimize weighted coefficient energy subject to nonnegative weights summing1 and ALL d positive-lag equations.
Its finite minimum c obeys

    0<c<1-delta/4.

There is an ACTUAL optimizing packet of r<=N=d+1 DISTINCT positive-weight atoms with RATIONAL weights, after zero labels are omitted.
For a packet supplied by the independent-column reduction in the retained proof, the ACTUAL least coefficient denominator q and ACTUAL least FINAL indexed weight denominator M satisfy

    q divides Q, 1<=q<=Q,
    1<=M<=M_max, r<=d+1.

Its ACTUAL common union width is EXACTLY d.
This is an optimizer of the declared FINITE dictionary LP, not an asserted optimizer or value formula for unrestricted E_d^Q.
Equality q=Q, a least possible M among all optimizers, or a practical complexity bound is not asserted.

**C. Complete original signed arithmetic and explicit size.**
For each selected atom f_i put

    D_i=Norm_(Q(alpha)/Q)(f_i(alpha)) in Z minus{0},
    F_i=q f_i in Z[t], m_i=M omega_i in Z_(>0),
    sum_i m_i=M, E=c,
    Lambda=(1/d)sum_i omega_i log|D_i|>=0.

All ORIGINAL degree-d roots, signs, contents, repeated values and actual final copies are retained.
One has

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(m_i)=q^(dM)product_i D_i^(m_i),
    S_int=sum_i omega_i||F_i||_2^2=q^2E,
    I=(1/(dM))log|product_i Res(P,F_i)^(m_i)|
      =log q+Lambda,
    Lambda-(1/2)log E=I-(1/2)log S_int<=m(P).

Each actual numerator F_i has coefficient height<=U, even when q is a proper divisor of Q.
If it has content b_i, the factor b_i^d remains in its full resultant and is not removed.
Any common unit monomial used in a representation retains its full possibly negative Norm(alpha) factor; no reciprocal sign assumption is imposed.
The complete dictionary already lies in[0,d].
The elementary monic root bound gives

    |beta|<=1+H for EVERY original root,
    |f_i(beta)|<=N(U/Q)(1+H)^d,
    1<=|D_i|<=[N(U/Q)(1+H)^d]^d.

This upper norm bound is not a lower income estimate.
The SAME log q cancels only after both actual norm and coefficient-energy charges.

**D. Literal finite exact algorithm.**
Enumerate the specified boxes/grid and their exact nonzero remainders, form rational normalization/lag/energy columns, enumerate supports of size<=N and nonsingular row minors, solve the corresponding integer-scaled systems, check every constraint and nonnegative weight, and choose the least exact rational energy.
At least one enumerated support is optimal.
Omitting zero labels and computing actual q,M, contents and signed resultants uses finite integer/rational arithmetic.
The proof gives finite termination once an applicable proved rational delta is supplied, with no floating inverse, oracle, unknown optimization tolerance or presumed endpoint infimum.
No mathematical program implementing this algorithm has been authored or run here; no favorable size/runtime claim, solver output or J is supplied.

The constructive bounds follow from a locally proved finite supporting plane, integer-box approximate positivity including BOTH zero-remainder repairs, a bounded actual-P grid, a finite-box conditioning argument and direct REAL-form weak dual on rational packets.
A rational maximizing dual form is not required.
Optimality-preserving support reduction gives independent constraint columns; after scaling all rows by Q^2 an integer minor has entries bounded by K_bound.
Its determinant bounds the actual weight denominator by M_max.
These proof interfaces remain explicit in the complete retained argument.

**E. Complete indexed product and effective energy windows.**
For any rational0<theta<1 take the actual optimizing packet above and put

    k=ceil(log(1/theta)/[-log(1-delta/4)])>=1.

Keep ALL ordered k-tuples of its labels, with product polynomials and product weights, without merging equal labels.
The C57 indexed-product theorem gives actual energy E^k<theta, ACTUAL union width kd, and EXACT actual denominators

    q_k=q^k<=Q^k, M_k=M^k<=M_max^k,
    k<=ceil(4log(1/theta)/delta).

The same least k is obtained by repeatedly multiplying the RATIONAL number1-delta/4 until it is at most theta; no transcendental evaluation is necessary for execution.
All product values are nonzero integers in the SAME O0 and their norm degree remains the ORIGINAL d.
For tuple b=(b_1,...,b_k), retain

    F_b^(k)=product_j F_(b_j),
    m_b^(k)=product_j m_(b_j), D_b^(k)=product_j D_(b_j),
    Lambda_k=k Lambda,
    Res(P,F_b^(k))=q^(kd)D_b^(k),
    product_b Res(P,F_b^(k))^(m_b^(k))
      =q^(kd M^k)[product_i D_i^(m_i)]^(k M^(k-1)),
    S_int,k=q^(2k)E^k,
    Lambda_k-(1/2)log(E^k)
      =k[Lambda-(1/2)log E]<=k m(P).

Every product content, sign and actual copy remains.
Product amplification does not improve surplus per unit window.
Taking the elementary C57 deficit makes the energy-window multiplier depend only on d and theta, while the explicit coefficient/weight/norm bounds additionally depend on H.
The constants can grow extremely rapidly.
No absolute constant times d window, degree-uniform deficit, unrestricted-capacity optimizer or unrestricted G0001 completion is obtained.
Overorders may admit earlier windows; the exact first-window statement here belongs to O0.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:12 |
| status | open |
| reason | Register the explicit finite dictionary, strict finite LP optimum, actual support/q/M/norm bounds, literal terminating exact algorithm and indexed energy-window extension. The complete corrected D14 proof and original norm-field defect/correction history are retained. R269 covers the actual19:05 corrected original body only; its reviewer now authors this new wrapper, requiring another noncontributor to inspect the actual extraction before adoption. No native algorithm execution, unrestricted optimizer, practical complexity or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual original-unit/order/degree, supplied proved rational deficit, all explicit constants, finite dictionary/optimizer/algorithm and initial/product full arithmetic and limitations. |
| argument | [Complete retained proof](#argument) | ENTIRE actual corrected D14 allocation/reuse, Sections1--9/equations1--18, original18:57 freeze, R268 norm-field defect and dated19:05 complete corrected freeze. |
| dependency | [C17 finite packet and first-window interface](Yin_C_G0017_v1.md#statement) | Actual finite rational nonzero-integer domain, weighted quotient, positive energy and monogenic short-width rigidity; no unrestricted primal optimizer is assumed. |
| dependency | [C17 actual supporting/quotient interface](Yin_C_G0017_v1.md#finite-lag-value-and-continuity) | Prior finite-lag neighborhood and local supporting-plane method; present finite dictionary epigraph/separation and real weak-dual proof are reconstructed locally. |
| dependency | [C57 supplied quantitative and indexed product theorem](Yin_C_G0057_v1.md#statement) | Elementary rational degree-only deficit as an applicable example, local integer-conditioning mechanism and full indexed q^k/M^k/kd/copy/energy identities. Its optional house theorem is not used. |
| dependency | [C10 full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual finite complementary rational packet, all nonzero full signed original resultants, final weights/copies and physical width. |
| support | [Original notation objection](../audits/reviews/Yin_R_G0268_v1.md#finite-dictionary-original-norm-field-finding) | Original18:57 literal norm-field collision and its separately performed substantive checking; negative history retained, not current corrected acceptance. Finding relationship: self-reviewed. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0269_v1.md#finite-dictionary-corrected-whole-finding) | Complete ACTUAL19:05 corrected D14 only, with original R268 preserved; this finding does not cover the new registered wrapper written by that same reviewer. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:22 |
| status | proved |
| reason | Adopt the separately performed corrected whole R269 and actual extraction R272 findings, retaining R268 original negative notation scope and the complete dated correction. The finite dictionary, exact optimizing packet and bounded arithmetic are effective existence results; no practical runtime, unrestricted capacity optimizer or uniform gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E, actual original-unit/order/degree, supplied proved rational deficit, all explicit constants, finite dictionary/optimizer/algorithm and initial/product full arithmetic and limitations. |
| argument | [Complete retained proof](#argument) | ENTIRE actual corrected D14 allocation/reuse, Sections1--9/equations1--18, original18:57 freeze, R268 norm-field defect and dated19:05 complete corrected freeze. |
| dependency | [C17 finite packet and first-window interface](Yin_C_G0017_v1.md#statement) | Actual finite rational nonzero-integer domain, weighted quotient, positive energy and monogenic short-width rigidity; no unrestricted primal optimizer is assumed. |
| dependency | [C17 actual supporting/quotient interface](Yin_C_G0017_v1.md#finite-lag-value-and-continuity) | Prior finite-lag neighborhood and local supporting-plane method; present finite dictionary epigraph/separation and real weak-dual proof are reconstructed locally. |
| dependency | [C57 supplied quantitative and indexed product theorem](Yin_C_G0057_v1.md#statement) | Elementary rational degree-only deficit as an applicable example, local integer-conditioning mechanism and full indexed q^k/M^k/kd/copy/energy identities. Its optional house theorem is not used. |
| dependency | [C10 full original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same actual finite complementary rational packet, all nonzero full signed original resultants, final weights/copies and physical width. |
| support | [Original notation objection](../audits/reviews/Yin_R_G0268_v1.md#finite-dictionary-original-norm-field-finding) | Original18:57 literal norm-field collision and its separately performed substantive checking; negative history retained, not current corrected acceptance. Finding relationship: self-reviewed. |
| support | [Corrected original whole finding](../audits/reviews/Yin_R_G0269_v1.md#finite-dictionary-corrected-whole-finding) | Complete ACTUAL19:05 corrected D14 only, with original R268 preserved; this finding does not cover the new registered wrapper written by that same reviewer. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0272_v1.md#c59-finite-dictionary-extraction-finding) | Entire actual A--E, preserved corrected proof/history and all current direct interfaces, separately inspected after actual allocation. Finding relationship: self-reviewed. |

## Registration and complete preservation

Date: 2026-10-12T11:12.
The complete corrected D14 body below is retained with only repeated author front matter removed, its first title demoted once and final whitespace normalized.
Its valid existing relative links are retained.
The wrapper names the integer determinant-entry bound K_bound to avoid the original field-symbol ambiguity; the unchanged proof's K=N U^2 is that same integer.
Both active statements define the original norm field explicitly as Q(alpha)/Q.
The old erroneous Norm_(K/Q) sentence remains only in the actual dated correction and original negative finding.

Every mathematical proof, constant, algorithm, norm/copy/sign/content distinction, source/reuse/contribution paragraph and both freeze/correction scopes survive.
No source intake, mathematical native run, historical finding rewrite, draft retirement or adoption accompanies this extraction.
The extractor's prior independent reviews remain at their completed original scopes; authoring this NEW wrapper is a substantive contribution and excludes a self-supplied independent extraction verdict.
Root must arrange a different noncontributor's actual statement/preservation/interface review.

## Argument

## Effective finite rational dictionary for the first energy window

Date: 2026-10-12T10:48.
Human author Yin.
Root AUTHOR investigation under the unchanged G0001 continuation; root owns the substantive finite-net and conditioning candidate and cannot independently review it.
This new normal allocation inherits no historical meaning of its address.
No native mathematical program is planned: the finite algorithm below will be proved symbolically, not executed.

## Bounded reuse and present question

The adopted [C17](Yin_C_G0017_v1.md#statement) supplies the exact rational/formal-real capacity duality and first-window strict decrease; [C57](Yin_C_G0057_v1.md#statement) supplies an explicit height-independent degree-only first-window deficit and tensor amplification, but no bounded rational primal coordinates or weight denominator.
Bounded actual reads of C17's separation/regularization proof and [C23](Yin_C_G0023_v1.md#statement), [C24](Yin_C_G0024_v1.md#statement), [C25](Yin_C_G0025_v1.md#statement), [C31](Yin_C_G0031_v1.md#statement) found no general finite dictionary carrying explicit coefficient and weight denominator bounds.
This bounded screen is not a novelty claim.

## Candidate and retained obligations

Let P be the ACTUAL monic irreducible minimal polynomial of a nontorsion integer unit, degree d>=2, O0=Z[alpha], A=[I,a_d].
Given a proved rational 0<delta<=1/2 with E_d<=1-delta (for example C57's elementary constant), construct a finite rational atom dictionary whose LP has an actual rational complementary packet of energy strictly below 1-delta/4.
All atoms must have nonzero actual integer remainder, not only an integral value at one embedding.

The candidate dictionary combines a bounded box of integer polynomials with bounded remainder vectors plus rational-grid multiples of P.
If its optimum c were at least 1-delta/4, finite separation would give a Toeplitz W with diagonal1 and atom values>=c.
The explicit atoms 1 and 1+/-t^h bound every off-diagonal entry.
A large integer box should force W>=-eta I, eta=delta/100, by rounding a negative eigenvector and, if its remainder vanishes, replacing it with z+/-1.
Then V=W+2eta I is positive definite.
A sufficiently fine coefficient-height-dependent P grid approximates every small-remainder V minimizer.
C57's bounded simultaneous approximation conditioning argument should convert this local integer floor to a global floor for G=(A(V/(1+2eta))^-1 A^T)^-1, contradicting the supplied capacity deficit.

Finite rational LP vertices would then give support at most d+1 and explicit bounds on the ACTUAL coefficient denominator q (dividing the grid denominator) and FINAL weight denominator M through an integer basis determinant.
Every nonzero signed norm, original degree, numerator content and physical width must remain.
No practical complexity, executed enumeration, full optimum, absolute degree-linear constant-energy window, source theorem or unrestricted gap is asserted.
Finite separation, the approximate-PSD lemma, grid error, local-to-global floor, real dual passage and exact denominator/weight bounds remain author obligations until fully proved below and independently reviewed.

## Status

Developing author candidate.
No result is adopted from this allocation; substantive argument continues here.
Original full costs and actual finite primal witnesses are the target.
This may make a fixed-degree existence theorem effective while leaving its severe degree loss unchanged.


<a id="finite-dictionary-domain-constants"></a>
## 1. Exact input, supplied deficit and explicit finite constants

Work throughout with the ACTUAL monic irreducible P=sum_(j=0)^d p_j t^j in Z[t], d>=2, p_d=1, p_0=+/-1, and nontorsion alpha.
All residues use the ORIGINAL power basis of O0=Z[alpha], all field norms the original degree d, and A=[I_d,a_d] is actual remainder modulo P.
Write N=d+1 and H=max_j |p_j|>=1.
Choose a SUPPLIED proved rational delta with

    0<delta<=1/2, E_d^Q<=1-delta.                    (1)

For example the elementary rational delta_elem(d) of adopted C57 satisfies this without any house-source input.
An improved rational deficit may be substituted ONLY if its own proof applies to this same actual input.
Set the following explicit positive rationals/integers, all computed from d,H,delta:

    eta=delta/100, D=N+1,
    B=ceil(8N^2/eta),
    R=4(4d)^d, rho=1/R^2=1/[16(4d)^(2d)],
    L=ceil(D/eta), F=L d R,
    J=N H,
    Q=ceil(D J(2F+J)/eta),
    U=Q max{B+2, R+F H}, K=N U^2,
    M_max=N! K^N.                                   (2)

The letter Q here is a coefficient-grid denominator, NOT C57's box parameter 4d, not the actual resulting least coefficient denominator q, and not the FINAL weight denominator M.
F is an integer bound for a minimizing representative, not a Claim or polynomial numerator name.
R,F,Q,U,K are integers; eta is rational.
All sizes are deliberately coarse and no practical complexity is claimed.

Define a FINITE dictionary Dcal of actual coefficient vectors of length N, retaining each distinct vector once if desired:

(i) every INTEGER polynomial z of degree at most d with |z_j|<=B+2 and nonzero actual integer remainder Az;

(ii) every polynomial

    g_(r,k)(t)=sum_(j=0)^(d-1) r_j t^j+(k/Q)P(t),
    r in Z^d minus{0}, |r_j|<=R, k in Z, |k|<=Q F.  (3)

All atoms have a nonzero O0 value.
For (ii) it is exactly sum r_j alpha^j, which is nonzero by minimal degree.
Both families have coefficient denominator dividing Q and integer numerator Qg with absolute coefficients at most U.
The dictionary contains 1 and 1+/-t^h for every 1<=h<=d: they lie in (i), and alpha^h=+/-1 would contradict nontorsion.
It is nonempty, finite, and its exact rational coefficients and nonzero-remainder checks are specified using only the actual integer P.
No embedding approximation or native enumeration is involved in its definition.

<a id="finite-dictionary-main-theorem"></a>
## 2. Finite dictionary and actual arithmetic theorem

**Theorem.**
The exact finite linear program on Dcal that minimizes weighted coefficient energy subject to nonnegative normalized weights and ALL d positive-lag cancellations has minimum c satisfying

    0<c<1-delta/4.                                  (4)

It has an ACTUAL rational optimizing packet of r<=N distinct positive-weight atoms, after omitting zero weights.
For a packet obtained by the independent-column reduction proved in Section7, its actual least coefficient denominator q and FINAL least weight denominator M satisfy

    q | Q, 1<=q<=Q,
    1<=M<=M_max, r<=d+1.                            (5)

The original common physical union width is exactly d.
No equality q=Q or a least possible M among all optimal packets is asserted.
The theorem is a bounded FINITE first-window construction from the supplied deficit, not a formula for the unrestricted capacity E_d or its optimizer.
It yields a finite terminating exact enumeration algorithm but no favorable runtime, executed scan or new finite numerical result.

Each actual value has a nonzero SIGNED norm D_i=Norm_(Q(alpha)/Q)(f_i(alpha)) in Z minus{0}; hence Lambda=(1/d)sum_i omega_i log|D_i|>=0.
With actual numerators F_i=q f_i in Z[t], actual positive copies m_i=M omega_i, and E=c, all original costs are

    Res(P,F_i)=q^d D_i,
    product_i Res(P,F_i)^(m_i)=q^(d M)product_i D_i^(m_i),
    S_int=sum_i omega_i ||F_i||^2=q^2 E,
    I=(1/(dM))log|product_i Res(P,F_i)^(m_i)|=log q+Lambda,
    I-(1/2)log S_int=Lambda-(1/2)log E<=m(P).         (6)

The actual finite nonzero signed products, primitive contents when present, FINAL copies and common physical width are mandatory.
In particular the log q cancellation is derived from both actual charges, not from discarding denominators.
Section8 supplies explicit coefficient/norm bounds and the exact finite-algorithm interpretation.
This result alone does not change the severe degree dependence of delta in C57 or the unrestricted uniform bottleneck.

<a id="finite-dictionary-support-form"></a>
## 3. Finite primal support plane with a bounded Toeplitz form

For an atom f let a(f)=(a_h(f))_(h=1)^d, a_h(f)=sum_(j=0)^(d-h) f_j f_(j+h).
The finite weight simplex is compact.
The constraints sum omega_i a(f_i)=0 and sum omega_i=1 are closed, and 1 alone is feasible.
Thus the finite LP has a real minimizer c<=1.
It also has c>0 because the finite set of nonzero coefficient vectors has a positive minimum squared norm.
No rationality of a minimizing weight vector is assumed here.

Define v(a) as the minimum energy over this finite simplex with lag a if feasible, and +infinity otherwise.
The epigraph is the convex hull of the finitely many (a(f),||f||^2) plus an upward vertical ray, hence closed.
To see closedness directly, any convergent sequence has convergent subsequence of its weights in the compact simplex and a convergent nonnegative vertical slack, since atom energies are bounded and the target height converges.
For ||a||_1<=1 the actual atoms 1 and 1+/-t^h give

    0<=v(a)<=1+||a||_1<=2.                          (7)

Mixing weights proves convexity.
C17's local continuity proof applies verbatim on this neighborhood: for 0<s=||a||_1<1 use a/s and -a/s in (7) and convexity to get |v(a)-c|<=2s.
A global value outside the finite lag polytope is not asserted.

For completeness the same local supporting-plane proof does not need an LP duality black box.
Let p=(0,c) in this closed convex epigraph and p_xi=(0,c-xi) below it.
Their positive separation has a closest point, by restricting to a closed finite-dimensional ball around p_xi containing p.
Normalize the vector from p_xi to that closest point.
Along xi down to0 take a convergent subsequence of unit normals.
The limit (h,b) has unit length and obeys

    h dot a+b(t-c)>=0

on the entire epigraph.
Upward rays give b>=0.
If b=0, (7) provides a symmetric neighborhood of lag vectors and forces h=0, impossible.
Thus b>0, put g=-h/b, and for EVERY atom

    ||f||^2-g dot a(f)>=c.                          (8)

Define W with W_jj=1 and W_(j,j+h)=W_(j+h,j)=-g_h/2.
It is real symmetric Toeplitz and f^T W f>=c on the finite dictionary.
Testing 1+/-t^h gives 2+/-2W_(0,h)>=c, hence

    |W_(0,h)|<=(2-c)/2<=1, ||W||_op<=N.             (9)

For the norm inequality, |x^T W x|<= (sum |x_j|)^2<=N||x||^2; no PSD premise is hidden.
The form is not yet positive definite and its entries need not be rational.
This supporting construction is a local specialization of C17's fully proved separation method, not a new imported convex-duality theorem.

<a id="finite-dictionary-approximate-positivity"></a>
## 4. The bounded integer box forces approximate positivity

Assume for contradiction c>=1-delta/4.
In particular c>0.
We claim W>=-eta I.
If it had a unit eigenvector v with eigenvalue less than -eta, round every coordinate of Bv to a nearest integer to obtain z=Bv+e, ||e||<=sqrt(N)/2.
By (9),

    z^T W z< -eta B^2+N^(3/2)B+N^2/4
              <=-(3/4)eta B^2<-1.                 (10)

Indeed eta B>=8N^2>=8N^(3/2) makes the middle term at most eta B^2/8, and B^2>=2N^2/eta makes the last term at most eta B^2/8.
The explicit B from (2), N>=3 and eta<=1/200 ensure both and (3/4)eta B^2>1.
Every |z_j|<=B+1.
If Az is nonzero, z is a dictionary atom contradicting f^T W f>=c>0.
If Az=0, both z+e_0 and z-e_0 have nonzero integer remainder, both lie in the B+2 coefficient box, and

    [(z+e_0)^T W(z+e_0)+(z-e_0)^T W(z-e_0)]/2
         =z^T W z+1<0.

At least one again contradicts (8).
Neither a zero residue nor a zero atom is tested as an admissible value.
Therefore W>=-eta I as claimed.
Set

    V=W+2eta I, W'=V/(1+2eta).

Both are real positive definite Toeplitz, W' has diagonal1, and

    eta I<=V, ||V||_op<=N+2eta<=D.                 (11)

This argument used only the actual finite integer box, not all rational rays.

<a id="finite-dictionary-grid-error"></a>
## 5. Small integer remainders are controlled by the finite P grid

Fix nonzero r in Z^d with |r_j|<=R.
Write f0=(r_0,...,r_(d-1),0), and let f* be the unique V-minimizer under Af=r.
Full row rank of A and V>0 give existence by direct weighted orthogonal projection, exactly as in C17; uniqueness also follows from strict positivity.
Comparing to f0 and using (11),

    eta ||f*||^2<=f*^T V f*<=f0^T V f0<=D||r||^2,
    ||f*||<=sqrt(D/eta) sqrt(d)R<=L d R=F.          (12)

Since ker A is the real span of the ACTUAL monic coefficient vector P, f*=f0+theta P, and its last coefficient theta satisfies |theta|<=F.
Choose an integer k with |k|<=QF and |theta-k/Q|<=1/Q (a nearest grid point or an endpoint).
The corresponding g from (3) is an ACTUAL dictionary atom.
Since ||P||<=sqrt(N)H<=J,

    ||g-f*||<=J/Q,
    |g^T V g-f*^T V f*|
        <=D(J/Q)(2F+J/Q)
        <=D J(2F+J)/Q<=eta.                       (13)

This coarse error does not assume rational f* or a rational theta; the dictionary already contains every grid point.
Because g^T W g>=c and V-W=2eta I>=0, it follows that f*^T V f*>=c-eta.
Put

    G=(A (W')^-1 A^T)^-1,
    c'=(c-eta)/(1+2eta).

The weighted quotient formula and scaling give

    r^T G r>=c' for EVERY nonzero r in [-R,R]^d.    (14)

Also G>0 and each diagonal G_jj<=1 by testing the allowed representative t^j under W'.
Under the assumed c>=1-delta/4,

    c'>1-delta and c'>1/2, c'<=1.                 (15)

For the first strict inequality, subtract (1-delta)(1+2eta) from 1-delta/4-eta: the result is 3delta/4-3eta+2eta delta>0.
The second follows from delta<=1/2 and eta<=1/200; for example its numerator is at least 7/8-1/200 and denominator at most101/100.
Finally c<=1 implies c'<1, so the weaker stated c'<=1 is safe.

<a id="finite-dictionary-local-to-global-floor"></a>
## 6. A bounded integer floor becomes global and contradicts the deficit

The conditioning proof of C57 uses only the bounded remainders already tested in (14).
Here are its exact bounds.
If lambda_min(G)<=rho, choose a Euclidean unit eigenvector v.
Put Q0=4d and N0=Q0^d.
The N0+1 fractional vectors jv for0<=j<=N0 in Q0^d half-open boxes give an integer 1<=k<=N0 and integer z with ||kv-z||_infinity<1/Q0.
If z=0 then k=||kv||<sqrt(d)/Q0<1, a contradiction.
Moreover |z_j|<N0+1<=R, so (14) applies.
Diag G<=1 implies lambda_max(G)<=d.
The triangle inequality for the G norm gives

    sqrt(z^T G z)
       <=k sqrt(lambda_min(G))+sqrt(d)||z-kv||
       <N0 sqrt(rho)+d/Q0=1/2.

Thus z^T G z<1/4, contradicting (14)--(15).
We have proved lambda_min(G)>rho with ONLY this local finite floor.
This is the same locally proved simultaneous pigeonhole mechanism already credited in C57; no new source or lattice result is adopted.

For an integer r outside [-R,R]^d one has ||r||>R, hence r^T G r>rho R^2=1>=c'.
Together with (14), every nonzero integer r therefore has r^T G r>=c'.
For any ACTUAL finite complementary packet with residues r_i in Z^d minus{0}, weighted least squares gives f_i^T W' f_i>=r_i^T G r_i>=c'.
Since W' is Toeplitz with diagonal1, all aggregate lags vanish and

    sum_i omega_i ||f_i||^2
       =sum_i omega_i f_i^T W' f_i>=c'.

Taking the infimum over rational finite packets yields E_d^Q>=c'>1-delta, contradicting (1).
This weak-dual step works with a REAL positive W' because its quadratic inequalities are tested directly on each actual rational packet; no rational maximizer, continuity of an integer minimum or extra rational-dual passage is required.
We have proved (4).

<a id="finite-dictionary-rational-weights"></a>
## 7. Rational optimizer, small support and FINAL denominator

Start with any real optimal finite weight vector and discard zero weights.
Let b_i in Q^N be its constraint column (1,a_1(f_i),...,a_d(f_i)).
If these positive-support columns are linearly dependent, take a nonzero real vector u with sum u_i b_i=0.
Its first row gives sum u_i=0, so u has both signs.
Both sufficiently small plus and minus weight perturbations are feasible.
Optimality forces sum u_i ||f_i||^2=0; otherwise one perturbation would improve the energy.
Move along u until a first weight becomes zero.
This preserves feasibility and energy, and removes at least one positive-support column.
Iterating finitely produces linearly INDEPENDENT columns, so the resulting positive support r is at most N.

Write n_i=Q f_i in Z^N with |n_(i,j)|<=U.
Multiplying EVERY constraint row by Q^2 produces an integer matrix: its first row is Q^2 and its lag-h entry is sum_j n_(i,j)n_(i,j+h).
The right side is (Q^2,0,...,0)^T.
Every absolute entry is at most K=N U^2, since U>=Q.
The r columns are independent, so some r rows form an invertible integer square matrix B0.
The same unique support weights solve this subsystem with an integer right side.
Elementary elimination/Cramer's determinant formula gives rational weights whose common least denominator M divides |det B0|.
The determinant expansion, with r! terms each at most K^r, gives

    M<=|det B0|<=r!K^r<=N!K^N=M_max.               (16)

This proves existence of rational optimal weights, their FINAL least denominator bound and the positive support claim.
It does not compute a small determinant nor assert a chosen basis contains all N rows.
All positive copies m_i=M omega_i are integers, sum_i m_i=M and gcd_i m_i=1 by leastness.
Actual coefficient denominators divide Q, hence their lcm q also divides Q.
No denominator of an intermediate real W, f*, or LP-support normal enters the actual final packet.

All atoms lie in [0,d], so the actual union width is at most d.
If it were smaller than d, a SINGLE common monomial shift normalizes it into [0,d-1].
Since alpha is a unit, every actual value remains nonzero in O0, coefficient energy and aggregate lag cancellations are unchanged, and the accepted monogenic short-width boundary of C17 gives energy>=1, contradicting (4).
Therefore its actual physical width is exactly d.
This does not assert exact first-window width for arbitrary overorders.

<a id="finite-dictionary-full-costs-algorithm"></a>
## 8. Original norms, explicit bounds and the finite algorithm

For the original monic polynomial, D_i is a nonzero SIGNED integer, without any unit-norm assertion.
Multiplicativity and the ORIGINAL d give (6).
If F_i has content b_i>1, its exact factor b_i^d remains in Res(P,F_i); it is never divided away.
The actual numerator satisfies |(F_i)_j|<=U because q<=Q and each coefficient of f_i has magnitude at most U/Q.
Thus the actual q and the stated U bound remain valid if q is a proper divisor of Q.
Common unit monomial normalization, if used to state the actual width, retains its original signed norm in the copies; the dictionary proof itself needs no such change to its actual [0,d] coordinates.

For an optional completely explicit size bound, every original root beta obeys |beta|<=1+H.
If x=|beta|>1+H, the leading equation would imply x^d<=H sum_(j<d)x^j<H x^d/(x-1)<x^d, impossible.
Hence

    |f_i(beta)|<=N(U/Q)(1+H)^d,
    1<=|D_i|<=[N(U/Q)(1+H)^d]^d.                  (17)

This is a coarse upper bound; it is not used as a lower income estimate.
All q factors, every original conjugate and each FINAL multiplicity still occur in (6).
The accepted C10 direct inequality applies to these actual complementary packets in width d and gives Lambda-(1/2)log E<=m(P), with no reciprocity restriction.
This is compatible with the supplied deficit; it does not add a degree-uniform gap when delta tends to0.

There is a finite terminating exact algorithm in the literal sense: enumerate the specified integer boxes/grid, compute each rational coefficient vector and its actual integer remainder, form all constraint/energy columns, enumerate supports of size<=N and nonsingular row submatrices, solve their integer linear systems, retain normalized nonnegative feasible weights, and choose the least exact rational energy.
At least one enumerated support is optimal by Section7; feasibility checks and rational comparisons terminate.
Omit zero-weight labels and compute actual q, M, signed resultants and coefficient contents by exact integer/rational arithmetic.
No floating-point inverse or external oracle is required to execute THIS finite algorithm once a proved delta is supplied.
Enormous enumeration size is acknowledged, and no such mathematical program has been authored or run in this inquiry.
There is no J, solver output or experimental claim.

For a prescribed rational 0<theta<1, C57's indexed-product theorem can now be applied to the actual packet just constructed.
Since E<1-delta/4, any integer k with (1-delta/4)^k<=theta gives E^k<theta at ACTUAL width kd, with EXACT indexed q_k=q^k and M_k=M^k.
Consequently

    q_k<=Q^k, M_k<=M_max^k,
    k=ceil(log(1/theta)/[-log(1-delta/4)])
       <=ceil(4log(1/theta)/delta).                 (18)

A purely rational stopping loop that multiplies 1-delta/4 until it is at most theta avoids needing to evaluate a transcendental ceiling; it produces the same least such integer k.
Every indexed product's norm, copy and coefficient content is inherited as specified in C57.
This makes the previous existence window effective in coefficient height as well as degree, while still leaving the absolute C*d quantitative target unresolved.

<a id="finite-dictionary-author-freeze"></a>
## 9. Complete author self-check and frozen scope

The root author checked the actual arbitrary-signature monogenic unit domain, rational supplied-deficit boundary and all integer constants; every atom's full integer remainder, nonzero-value test and numerator bound; compact finite feasibility and the precise supporting-plane normal sign; bounded off-diagonal entries without PSD; negative-direction rounding with the two valid zero-remainder repairs; every regularization and grid error; the local conditioning proof's actually bounded integer witness and the outside-box coercive step; the REAL-form weak dual inequality directly on rational packets; strict versus weak infimum endpoints; support reduction, optimality-preserving directions, rational weights and true FINAL determinant denominator; actual width d and common unit sign; all original signed norms, contents and q/M copies; explicit norm size, finite algorithm and indexed-product extension.
The proof introduces no unrestricted optimal packet, practical complexity or source theorem.
No defect was found in this author check; that is not independent evidence.

The ENTIRE original allocation and Sections1--9, Theorem/relations(1)--(18), all boundaries, reuse, contribution and cost paragraphs are AUTHOR-FROZEN at 2026-10-12T10:57.
Root authored the candidate and proof and cannot independently review it.
A separate whole noncontributor review must inspect this actual full account; a later new fixed Claim wrapper, if any, requires its own actual extraction review.
No native mathematical process was run and no fresh source or shared execution allowance was created.


<a id="finite-dictionary-norm-notation-correction"></a>
## Dated notation correction and complete corrected freeze

2026-10-12T11:05.
The separately performed [R268 original-scope finding](../audits/reviews/Yin_R_G0268_v1.md#finite-dictionary-original-norm-field-finding) identified a literal notation conflict: Section1 defines the INTEGER bound K=N U^2, while the original Section2 sentence read `D_i=Norm_(K/Q)(f_i(alpha))` without defining a field K.
This original wording is preserved here as the exact corrected defect, not as a valid field norm.
The active Section2 sentence now reads `D_i=Norm_(Q(alpha)/Q)(f_i(alpha))`, naming the actual original degree-d field explicitly.
The integer K bound and every formula/proof/denominator/norm-copy statement are unchanged.
This is an author correction following independent review, not a claim that the original finding passed.

Freeze the ENTIRE corrected document, original allocation, Sections1--9/equations1--18, original18:57 freeze and this dated correction.
Root remains the mathematical author.
The original R268 finding remains at its original negative scope; a new actual complete corrected-body review finding is required before adoption.
No program, experiment or new source was introduced.
