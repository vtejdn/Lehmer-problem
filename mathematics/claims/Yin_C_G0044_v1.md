---
author: Yin
---
# Quantitative totally real trace-lattice half-profiles without unit-exponent selection

Date: 2026-10-12T05:57.
Human author Yin.
Provenance: project deduction using the precise retained project and source interfaces.
This organization preserves the ENTIRE original dated author account below.
Its whole-author review is distinct from the actual registered-statement/interface review, which remains pending.

## Statement

Let P be an ACTUAL monic irreducible reciprocal non-torsion integer-unit minimal polynomial, K=Q(alpha), degree d=2s, F=Q(tau), tau=alpha+alpha^(-1), with F TOTALLY REAL and [K:F]=2.
First assume s>=2.
Fix an actual full order Z[tau] subset B subset Z[alpha] intersection F, actual integral basis b_j, real embeddings rho_i, V_B=(rho_i(b_j)), D=abs(det V_B)=sqrt(disc B) and K_B=||V_B^(-1)||_(infinity->infinity).
Choose an actual exterior trace place rho_0.
Use C11's seed w=1-alpha if rho_0(tau)>2, w=1+alpha if rho_0(tau)<-2; c=w sigma(w)=2-tau or2+tau, c_j=rho_j(c), k=-c_0>0 and kappa=Norm_K(w)=P(1) orP(-1).

Put H=max(1,max_j|c_j|), t=min(k,1)/(1+k), epsilon^2=t/[64(s+H)], L=epsilon^(-(s-1)) and B_star=2D L.
The order B and numerical B_star are distinct.

**A. Actual finite integer choice and positive rational simplex.**
For EACH i there exists nonzero a_i in B with off-axis |rho_j(a_i)|<=epsilon for j!=i, L<=|rho_i(a_i)|<=B_star and1<=|Norm_F(a_i)|<=2D.
A finite search over nonzero integral basis columns bounded by ceil(K_B B_star), at most (2ceil(K_B B_star)+1)^s columns, suffices; no search was executed.
The complete local strict-volume lattice proof is retained.

The s+1 actual targets u_i=a_i and u_c=w a_0 have strictly positive normalized RATIONAL weights satisfying sum_i lambda_i a_i^2+lambda_c c a_0^2=1/2 in F.
The explicit perturbation proof gives lambda_0,lambda_c>t/2 and1/4<M_i lambda_i<3/4 for i>=1, where M_i=rho_i(a_i)^2.
For the unscaled actual INTEGER coefficient/normalization matrix A_Z, the actual initial weight denominator obeys

    M_profile divides2|det A_Z|,
    M_profile<=2(s+1)^((s+1)/2)H_Z^(s+1),
    H_Z=max(1,K_B H B_star^2),
    M_profile>(4/3)M_i>=(4/3)L^2 for each i>=1.

The lower bound concerns this indexed axis-simplex construction, not all possible profiles.

**B. Constructive circle upper bound.**
For ALL original roots alpha_l define

    J_P=sum_l product_(h!=l)(1+|alpha_h|)/|P'(alpha_l)|,
    W=max(1,max_l|w(alpha_l)|)<=1+exp(m(P)).

Actual ordinary integer representatives of the above targets have coefficient absolute sums at most W B_star J_P.
Therefore the FULL C37 profile infimum obeys the actual upper estimate

    c_infty(P)<=4(disc B)W^2 J_P^2[64(s+H)/t]^(s-1).

This is a finite actual profile, not a dual reformulation or a hypothetical selection premise.
When s=1, the existing signed quadratic1,w construction separately gives the bound1+3/[2(a-1)] with |tau|=a>=3; no dimension-zero box is used.

**C. Exact remaining degree/measure costs.**
If rho_0 has largest exterior log radius and0<m(P)<=1, then t>=m(P)^2/(3s^2), H<8,W<4 and

    c_infty(P)<=64(disc B)J_P^2[192s^2(s+8)/m(P)^2]^(s-1).

Taking B=Z[tau] also gives disc B<=[4exp(m)]^(s(s-1)) and J_P<=d[1+exp(m)]^(d-1)[2exp(m)]^((d-1)(d-2)/2), by the COMPLETE original integer discriminants.
Thus the choice no longer depends on unspecified unit powers or a regulator, but its displayed bound retains severe dimension/discriminant/interpolation costs.
Integer norm forces the axis amplitude>=epsilon^(-(s-1)) under these particular box demands.
This is not a lower bound on the optimized c_infty or a proof that other profiles must pay these costs.

**D. Full original costs and limits.**
Write n_i=Norm_F(a_i).
Full degree-d signed norms are n_i^2 between1and4disc B and kappa n_0^2 of absolute value at most4|kappa|disc B.
Their signs, variable ideals/norm inventory, initial q=1, actual copies and contents remain; the full norm sign of kappa is not inferred from one negative trace place.
Later exact complementary completion has its OWN actual q, FINAL M_w, changed weights, full signed original norms and physical width.
No pending faster filter is a premise.
The result does not preserve C11's fixed norm inventory, cover nonreal trace fields, prove an input-uniform O(m^-2) selection, or resolve unrestricted G0001.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T05:57 |
| status | open |
| reason | Register the precise statement and retain the complete original proof and history. The separate whole-author finding covers its exact dated original freeze; actual extraction and interface acceptance remain pending. No unrestricted uniform estimate or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Complete retained argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Actual trace field and negative seed](Yin_C_G0011_v1.md#integral-seed-positive-field-profiles-all-trace-degrees) | Actual totally real trace degree, order domain, non-torsion exterior place and old existence; new finite boxes and quantitative simplex are proved locally. |
| dependency | [Exact fixed seed](Yin_C_G0011_v1.md#one-fixed-integral-seed-norm-and-ideal) | Actual 1±alpha seed and full original signed norm; new positive integer targets have variable bounded inventory. |
| dependency | [Actual full profile domain](Yin_C_G0037_v1.md#statement) | All finite nonzero actual integral rational half-profiles; later full completion only at its own paid scope. |
| dependency | [Original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only a later actually complementary packet, retaining all original scalar/norm/weight/width charges. |
| support | [Whole-author finding](../audits/reviews/Yin_R_G0242_v1.md#trace-box-profile-whole-independent-finding) | Exact original author freeze only, with the actual registered-statement and interface finding still pending. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T07:03 |
| status | proved |
| reason | Adopt the complete separately reviewed totally-real trace-lattice construction and its actual registered-statement/interface finding. The explicit original-input upper bound removes unspecified unit exponents but retains dimension, discriminant, interpolation, weight and variable-inventory costs. No dimension-independent upper selection, nonreal extension or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact registered statement, all hypotheses, actual costs and limitations. |
| argument | [Complete retained argument](#argument) | Entire original author account, all proofs, source/reuse boundaries, costs and freeze. |
| dependency | [Actual trace field and negative seed](Yin_C_G0011_v1.md#integral-seed-positive-field-profiles-all-trace-degrees) | Actual totally real trace degree, order domain, non-torsion exterior place and old existence; new finite boxes and quantitative simplex are proved locally. |
| dependency | [Exact fixed seed](Yin_C_G0011_v1.md#one-fixed-integral-seed-norm-and-ideal) | Actual 1±alpha seed and full original signed norm; new positive integer targets have variable bounded inventory. |
| dependency | [Actual full profile domain](Yin_C_G0037_v1.md#statement) | All finite nonzero actual integral rational half-profiles; later full completion only at its own paid scope. |
| dependency | [Original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Only a later actually complementary packet, retaining all original scalar/norm/weight/width charges. |
| support | [Whole-author finding](../audits/reviews/Yin_R_G0242_v1.md#trace-box-profile-whole-independent-finding) | Exact original author freeze only; the actual registered-statement and interface finding is separately selected below. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0242_v1.md#c44-trace-box-profile-extraction-finding) | Exact registered statement, entire retained argument, actual source/dependency interfaces, finite-choice and original-cost limits, and full preservation checked by a separate noncontributor. |

## Argument

The complete author account follows, with only front matter, first-title depth and final whitespace normalized.
Earlier pending/status and contributor paragraphs retain their historical scope.
This registration does not turn a contributor into an independent reviewer or enlarge an accepted source inspection.

## Quantitative trace-lattice simplex profiles without unit exponents

Date: 2026-10-12.
Responsible bounded AUTHOR inquiry on G0001 under root's mathematical assignment.
The proposed question is whether the actual trace-order lattice can replace the uncontrolled sufficiently-large unit-cone exponent in C11 by explicit anisotropic integer boxes, with all resulting dimension, discriminant, seed and power-basis interpolation costs charged.
This author supplies the candidate and its proof or failure analysis.
This author's prior independent D5 review does not independently review this new work.

## Starting domain and questions

Begin with ACTUAL monic irreducible reciprocal nontorsion integer-unit P, K=Q(alpha), degree d=2s, TOTALLY REAL trace field F=Q(alpha+alpha^-1), actual O0=Z[alpha], and a fixed full trace order B contained in O0 intersect F.
A bounded reuse read of C11/C13/C16 identified the accepted unit-cone construction, its unbounded exponent/phase-return and exact finite integer-hull boundaries.
Con26 records classical Minkowski foundations.
The narrower proposed mechanism uses arbitrary nonzero integral targets rather than preserving C11's fixed norm inventory.
No nonreal-signature extension is presumed.

The candidate is to use anisotropic boxes in the full real trace lattice to produce s elements whose off-axis embeddings are absolutely small while the selected embedding is bounded above explicitly and bounded below by integral norm.
Use the actual negative relative-norm seed from C11 at one exterior trace place, and prove a quantitatively positive rational affine simplex solution at field energy one half.
Then bound the ordinary integer representatives and their circle profile using the ACTUAL full power-basis interpolation operator.
Determine exactly which dimension/discriminant/seed-separation/interpolation factors remain; do not assert dimension-independent O(m(P)^(-2)) from a large explicit bound.

All substantial derivation, source attribution and author self-check will be retained here before freezing.
No mathematical native program, numerical scan, solver or J is authorized in this bounded inquiry.
Newly recognized source use will be checked at exact primary-statement scope or the local argument will be proved in full; source intake remains root-owned.

<a id="trace-box-profile-reuse-and-inputs"></a>
## 1. Actual reused inputs and classical attribution

Read the complete actual [C11 field-profile construction](Yin_C_G0011_v1.md#integral-seed-positive-field-profiles-all-trace-degrees), its [fixed negative seed](Yin_C_G0011_v1.md#one-fixed-integral-seed-norm-and-ideal), [C13 nonreal statement](Yin_C_G0013_v2.md#statement) and log-cone/phase-return account, and [C16 finite integer domain](Yin_C_G0016_v1.md#statement).
C11 already proves existence by actual units, preserves one fixed seed norm and uses an unspecified sufficiently large cone exponent.
C13 needs additional complex directions and a common phase-return subsequence.
The present argument is TOTALLY REAL only and intentionally allows variable integral seed norms; it does not assert the old fixed-inventory property.
C16 supplies no normalized integer profile merely from a positive Gram.
The candidate here produces actual finite integer atoms and positive rational weights directly, not a hull closure or equivalent dual statement.

The existing [Con26-U001](../audits/literature/Con26/Yin_U001.md#con26-u001) and [Con26-U002](../audits/literature/Con26/Yin_U002.md#con26-u002) identify the classical Minkowski/lattice foundations of the earlier unit construction.
This author then directly text-read Keith Conrad's primary [27-page author notes](https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf), Section 3, printed pp.4--6: the order's Euclidean embedding, norm as coordinate product, and the compact centrally symmetric convex-body use with volume greater than 2^s times lattice covolume.
This is fresh selected text inspection, not a new U, artifact acquisition, original Minkowski proof audit or extension of the existing units.
The exact box lemma needed below is also proved locally by the classical fundamental-cell averaging argument.
The Minkowski convex-body mechanism is attributed, not claimed new.
No external unit algorithm, regulator estimate, simultaneous phase-return theorem or new original-source proof is imported.

Fix s>=2 and the actual totally real trace field F=Q(tau), tau=alpha+alpha^-1, [K:F]=2 and d=2s, as in C11.
Choose ANY specified full order

    Z[tau] subset B subset O0 intersection F,
    O0=Z[alpha],

with an actual integral Z-basis b_1,...,b_s.
Containment of Z[tau] ensures that the later seed relative norm c belongs to B; no arbitrary smaller trace-order assertion is made.
In particular B=Z[tau] and the ordinary trace-power basis are permitted.
Let rho_0,...,rho_(s-1) be the real embeddings of F, V_B=(rho_i(b_j)) and

    D=abs(det V_B)=sqrt(disc B)>=1,
    K_B=||V_B^(-1)||_(infinity->infinity).

The embeddings are linearly independent: for the trace-power basis this is the nonzero Vandermonde determinant on the distinct conjugates of tau; an actual rational basis change preserves invertibility.
The trace Gram matrix is V_B^T V_B, with integer entries, so its positive determinant is disc B=D^2, a positive integer.
This also proves the stated covolume convention without a maximal-order substitution.

Choose an actual exterior real trace place rho_0, whose existence is already supplied by C11's Kronecker/domain argument.
Use its existing seed

    w=1-alpha, c=2-tau, if rho_0(tau)>2;
    w=1+alpha, c=2+tau, if rho_0(tau)<-2.

Write c_j=rho_j(c), k=-c_0>0, kappa=Norm_K(w)=P(1) or P(-1), and set

    H=max(1,max_j abs(c_j)),
    t=min(k,1)/(1+k),
    epsilon^2=t/[64(s+H)],
    L=epsilon^(-(s-1)), B_star=2D L.                 (1)

Thus 0<t<=1/2, 0<epsilon<1, L^2>=64s/t and H epsilon^2<=t/64.
Here B_star is a numerical box height, distinct from the order B.
Neither c nor w is assumed invertible in the order.
All quantities in (1), the actual embeddings and V_B are fixed original-input data.

<a id="anisotropic-trace-box-lemma"></a>
## 2. Exact anisotropic integer boxes, finite search and norm bounds

For EACH i there is a nonzero a_i in B such that

    abs(rho_j(a_i))<=epsilon, j!=i,
    L<=abs(rho_i(a_i))<=B_star,
    1<=abs(Norm_F(a_i))<=2D.                         (2)

Here is a complete proof of the lattice step.
For a full lattice Lambda=V_B Z^s, let F0 be a half-open fundamental parallelepiped of volume D.
If a bounded measurable set S has volume greater than D, the integer-valued multiplicity N(x)=sum_(lambda in Lambda)1_S(x+lambda), integrated over F0, has integral vol(S)>D.
The sum is finite uniformly on bounded F0 because the lattice is discrete and S is bounded.
Thus N(x)>=2 at some x (indeed on a set of positive measure), giving distinct points of S whose difference is a nonzero lattice vector.
For a centered box C, take S=C/2: differences of points of C/2 lie in C, by its convexity and central symmetry.
A box of volume greater than 2^s D therefore contains a nonzero lattice point.
No boundary-equality case is needed.

Apply this to the box with i-th half-length B_star and all other half-lengths epsilon.
Its volume is 2^s B_star epsilon^(s-1)=2^(s+1)D, strictly above the threshold.
The resulting nonzero order element has nonzero integer field norm; hence 1<=product_j abs(rho_j(a_i))<=abs(rho_i(a_i))epsilon^(s-1), proving the lower selected-coordinate bound.
The same product and upper box bounds give the upper norm 2D.
Every embedding of a_i is nonzero by field injectivity.

This is a finite constructive choice in the actual integral basis.
Every point in the box has all coordinates at most B_star, hence its integer coefficient column n satisfies ||n||_infinity<=K_B B_star.
Enumerating the finite nonzero integer columns with

    ||n||_infinity<=ceil(K_B B_star)

and testing the stated algebraic inequalities must find a suitable a_i.
There are at most (2ceil(K_B B_star)+1)^s candidates.
This describes a finite mathematical procedure and bound; no enumeration or program was run.
Exact real algebraic comparisons are possible because the original roots, c_j, D, t and epsilon are algebraic.
No unknown unit exponent, regulator basis or asymptotic phase-return time remains in this choice.

<a id="quantitative-trace-simplex-half-profile"></a>
## 3. A quantitatively positive rational half-profile

Use the s+1 actual integral targets

    u_i=a_i for 0<=i<s, and u_c=w a_0.

They are nonzero elements of O0.
Put q_ij=rho_j(a_i)^2>0 and M_i=q_ii.
Thus M_i>=L^2=:M, while q_ij<=epsilon^2 for i!=j.
The relative norms of the targets in F are a_i^2 and c a_0^2.
We prove that there are strictly positive RATIONAL normalized weights with

    sum_i lambda_i a_i^2+lambda_c c a_0^2=1/2 in F. (3)

Set E=1/2 and scaled unknowns x=(lambda_0,lambda_c,mu_1,...,mu_(s-1)), where mu_i=M_i lambda_i.
The exact embedding and normalization equations are

    lambda_0-k lambda_c
      +sum_(i>=1)q_i0 mu_i/(M_i M_0)=E/M_0,
    lambda_0+lambda_c+sum_(i>=1)mu_i/M_i=1,
    q_0j lambda_0+c_j q_0j lambda_c
      +sum_(i>=1)q_ij mu_i/M_i=E, 1<=j<s.           (4)

Let A_* be the matrix obtained by deleting every off-diagonal q_ij term and every 1/M_i in the normalization row.
Its first two rows are (1,-k) and (1,1), with an identity block on the mu variables.
For b_*=(0,1,E,...,E),

    x_*=(k/(1+k),1/(1+k),E,...,E),
    min coordinates x_* >= t, ||x_*||_infinity<=1,
    ||A_*^(-1)||_infinity<=2.

For the actual A=A_*+Delta, row sums of Delta are bounded respectively by

    s(H epsilon^2)/M^2,
    s/M,
    2H epsilon^2+s(H epsilon^2)/M.

Since M>=64s/t and H epsilon^2<=t/64, each is strictly less than t/16.
For example the last is at most t/32+t^2/4096<t/16.
Consequently ||A_*^(-1)Delta||<t/8<=1/16.
The geometric series sum_(n>=0)(-A_*^(-1)Delta)^n converges absolutely in this matrix norm, is the inverse of I+A_*^(-1)Delta, and gives ||A^(-1)||<4.
The right-side perturbation is ||b-b_*||=E/M_0<=t/(128s)<=t/256.
Hence

    ||x-x_*||_infinity
       <=||A^(-1)|| (||b-b_*||+||Delta|| ||x_*||)
       <(17/64)t<t/2.                              (5)

Every coordinate is therefore positive, lambda_0,lambda_c>t/2, and 1/4<mu_i<3/4 for i>=1.
Dividing by M_i gives positive lambda_i; the exact normalization row makes their total with lambda_c equal to 1.
Thus no limiting or zero-weight profile is used.

For rationality return to the UNSCALED equations.
Express each a_i^2 and c a_0^2 in the actual Z-basis of B and include the normalization row.
This gives an INTEGER (s+1)-by-(s+1) matrix A_Z with right side half an integer vector.
The actual embedding matrix and the positive diagonal column scales are invertible; (4)'s proved invertibility therefore implies det A_Z!=0.
Its unique weights are rational and solve the exact field identity (3), not only approximate embedding equations.
No maximal-order or finite-hull relaxation appears.

The actual least initial denominator M_profile divides 2 abs(det A_Z).
With

    H_Z=max(1,K_B H B_star^2),

every entry of A_Z is at most H_Z in absolute value.
Hadamard's elementary determinant bound, obtained from volume at most the product of column lengths, yields

    M_profile<=2(s+1)^((s+1)/2) H_Z^(s+1).

Conversely each i>=1 has lambda_i<3/(4M_i), so positivity of the integer M_profile lambda_i gives

    M_profile>(4/3)M_i>=(4/3)L^2.                  (6)

The denominator is bounded above explicitly but is not small.
This lower bound is for THIS axis-simplex construction; it is not an obstruction to other C37 profiles.

<a id="trace-box-circle-upper-bound"></a>
## 4. Actual ordinary representatives and full circle bound

Here c_infty(P) denotes the infimum of the circle maximum over the FULL C37 class: all finite positive normalized rational half-energy profiles of nonzero actual O0 integers, represented by their unique ordinary integer polynomials of degree<d.
Our s+1 targets form one member of that full class; they do not redefine it.

For the d original roots alpha_l define the ordinary Lagrange polynomials

    ell_l(z)=P(z)/[(z-alpha_l)P'(alpha_l)],
    J_P=sum_l [product_(h!=l)(1+abs(alpha_h))]/abs(P'(alpha_l)),
    W=max(1,max_l abs(w(alpha_l)))<=1+exp(m(P)).

The roots are simple in characteristic zero.
Direct interpolation at all d roots gives the degree<d representative f_u(z)=sum_l u(alpha_l)ell_l(z).
All target values here are actual O0 integers, so monic division and the power basis ensure that these representatives have INTEGER coefficients.
The interpolation formula identifies those unique representatives; it does not replace the actual order by a norm surrogate.

For |z|=1, abs(ell_l(z)) is at most its coefficient absolute sum, which is at most product_(h!=l)(1+abs(alpha_h))/abs(P'(alpha_l)).
The same product expansion bounds the coefficient absolute sum of f_u by J_P max_l abs(u(alpha_l)).
Each a_i lies in F, so its two K-embeddings over a trace place have the same a_i value and are at most B_star.
The final seed target has absolute values at most W B_star.
The definition W>=1 also bounds the positive targets.
It follows that the ACTUAL profile (3) obeys

    C=max_circle sum lambda_j f_j f_j*
       <=W^2 B_star^2 J_P^2
       =4(disc B)W^2 J_P^2
          [64(s+H)/t]^(s-1).
    c_infty(P)<=C.                                (7)

The normalized positive weights are the actual ones just proved, and this is an UPPER bound from an actual profile.
It is neither a dual reformulation nor a hypothetical availability implication.
It applies to every original totally real trace input with s>=2, with explicit actual-input constants.
The proposed pending improved C37 realization is not used.
The already adopted C37 may subsequently consume this actual finite supplied profile at its own exact costs.

For s=1 use C11's existing 1,w profile.
With |tau|=a>=3 its circle maximum is 1+3/[2(a-1)] after the corresponding sign of the binomial, as also retained in the current quadratic work.
No box lemma in dimension zero or epsilon exponent is used for this branch.

<a id="trace-box-dimension-and-conditioning"></a>
## 5. The explicit degree/measure dependence and remaining obstruction

Choose rho_0 to have largest exterior log radius ell_0 among real split trace places.
The totally real trace configuration partitions the original roots into reciprocal real pairs and circle pairs; therefore m=sum_(exterior places)ell_j<=s ell_0.
Its chosen seed has

    k=2(cosh ell_0-1)>=ell_0^2>=m^2/s^2.

If 0<m<=1, then ell_0<=m<=1, k<=2(cosh1-1)<2, H<=2+2exp(m)<8 and W<=1+exp(m)<4.
Since min(k,1)>=m^2/s^2 in this range and 1+k<3, we have t>=m^2/(3s^2).
Thus the explicitly constructed circle bound satisfies

    c_infty(P)
      <=64(disc B)J_P^2
             [192 s^2(s+8)/m^2]^(s-1).             (8)

This is not dimension-independent O(m^-2).
It carries m^(-2(s-1)), trace-order discriminant and actual full-root interpolation amplification.
The mechanism REMOVES the unspecified unit exponent/regulator/phase-return choice in the totally real branch, while paying those explicit quantities instead.

The basic axis-concentration cost cannot be removed while retaining these box demands: every nonzero integral a with s-1 conjugates of absolute value at most epsilon must have remaining absolute value at least epsilon^(-(s-1)), by its nonzero integer norm.
Equation(6) additionally proves large ACTUAL weight denominators for this constructed simplex.
Neither observation is a lower bound of this order for the optimized c_infty(P): interpolation can have structure, different profiles may avoid axis isolation, and denominator size alone does not obstruct the later full-cost cancellation.
Thus the result identifies the precise dimension/conditioning terms in this construction, not unconditional failure of the uniform selection gate.

For an entirely degree/measure-explicit albeit much worse bound take B=Z[tau].
All abs(alpha_l)<=exp(m), all abs(tau_j)<=2exp(m), hence

    disc B<= [4exp(m)]^(s(s-1)).

Also abs(disc P)>=1.
For a fixed root alpha_l, separate the pairs involving l in the discriminant product and bound the remaining pair distances by 2exp(m).
This gives

    abs(P'(alpha_l))
       >=[2exp(m)]^(-(d-1)(d-2)/2),
    J_P<=d[1+exp(m)]^(d-1)
                    [2exp(m)]^((d-1)(d-2)/2).      (9)

The original P is monic irreducible and hence has nonzero integer discriminant, which is the necessary arithmetic guard in this crude conversion.
These inequalities eliminate unspecified conditioning parameters at the price of explicit exponential dependence on d.
They prove no usable uniform near-one rate.
No claim is made that the bounds in (7)--(9) are sharp or that the selected basis minimizes the geometric constants.

<a id="trace-box-original-arithmetic-costs"></a>
## 6. Full original arithmetic and the changed inventory

Write n_i=Norm_F(a_i), a nonzero signed integer.
The initial profile's full signed original degree-d norms are

    D_i=Norm_K(a_i)=n_i^2, 1<=D_i<=4 disc B,
    D_c=Norm_K(w a_0)=kappa n_0^2,
    1<=abs(D_c)<=4 abs(kappa) disc B.               (10)

This follows from [K:F]=2, not from assigning a trace-degree resultant to the original polynomial.
All d original conjugates are included.
The negative trace-place relative norm does not determine the sign of kappa; retain its actual full sign.
The ideals and full norms generally vary with the box choices.
They are bounded as in (10), not fixed to C11's unit/one-seed inventory.
There is no cost-free conversion back to that stronger property.

Every ordinary initial f_j has INTEGER coefficients and nonzero actual residue, so its common scalar coefficient denominator is 1.
Its coefficient absolute sum is at most W B_star J_P.
The ACTUAL positive rational initial weights have the denominator M_profile in Section3 and positive copies m_j=M_profile lambda_j.
The exact copied initial norm product is

    product_(i=0)^(s-1) n_i^(2m_i)
                      times (kappa n_0^2)^(m_c),

with no inferred prime divisibility beyond those actual integers.
Dividing an f_j by its primitive content changes both its residue norm by the d-th power and its weighted square by the square; such a change is not performed.
The initial symbol has coefficient mean at least1 and field value1/2, so it is nonconstant and is not already a below-one complementary packet.

For a later LEGITIMATE C37 completion let q be its actual common coefficient denominator, M_w its FINAL least weight denominator, omega_b its final weights and m_b=M_w omega_b.
With actual nonzero integral final residues v_b(alpha), D_b=Norm_K(v_b(alpha)) and ONE common monomial, the accepted original identities remain

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^m_b
                  =q^(d M_w) product_b D_b^m_b,
    Lambda=(1/d)sum_b omega_b log abs(D_b),
    Lambda-(1/2)log E_final
                     <=(T_actual/d)m(P).            (11)

The same log q cancels only after the coefficient-energy and norm scalar costs are both present.
Common monomials have full norm1 at the original even reciprocal degree.
Original profile weights generally change on completion, so the preliminary m_i and M_profile cannot be substituted for the FINAL data.
Statement (11) is only the existing [C10 direct full-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality), after actual exact constant covariance.
No pending faster damping recipe, new arithmetic income theorem or uniform small physical width is a premise here.

<a id="trace-box-author-selfcheck-and-outcome"></a>
## 7. Complete author self-check and bounded outcome

This author checked the complete actual Sections1--6/equations(1)--(11): actual reciprocal trace degree/order/basis and exterior seed; full trace discriminant/covolume convention; classical fundamental-cell averaging with finite bounded multiplicity and STRICT volume threshold; selected-axis box volume; nonzero integer norm giving BOTH diagonal lower bound and norm upper bound; finite integer-coordinate search cutoff without a run; every finite perturbation matrix entry, normalization row and rational unscaled system; exact t,epsilon,M and row-sum inequalities, inverse geometric-series guard and17t/64 positivity margin; actual rational weights, determinant denominator upper and positive-copy denominator lower bounds; actual original-degree integer representatives and complete full-root interpolation; coefficient absolute sums rather than unattested numerical interpolation stability; all constants in(7), largest exterior ell_0, total m=sum ell_j, m<=1 guards and(8); both discriminant product estimates in(9); all original norm/sign/content/copy and future-final-denominator costs.

The final formulation deliberately sets W=max(1,max abs(w(alpha_l))) so no extra strict W>1 argument is needed to bound all positive targets.
This was an author-side pre-freeze clarification, not independent review.
The original s=1 C11 branch remains separate.
The current work proves no complex-place simplex or phase-return bound for C13; real order embeddings and squared real values are essential in the present positive-axis construction.
Changing the norm inventory is also essential to this method's stated gain, and it must not be presented as quantitative improvement preserving C11's fixed-seed property.

The concrete completed mechanism gives an ACTUAL finite constructive upper bound on the full c_infty(P) for every TOTALLY REAL trace input, including explicit finite atom-search and rational-weight denominator bounds, with no selected unit generator or uncontrolled exponent.
It removes that specific previous qualitative choice.
The paid cost remains exponential in trace degree through axis concentration, discriminant and full-root interpolation; the displayed near-one estimate scales like m^(-2(s-1)), not dimension-independent m^-2.
This is meaningful quantitative fixed-input control, not a solution of the surviving uniform gate.
The unavoidable norm concentration and this construction's denominator lower bound do not prove such growth for the optimal c_infty, and no near-one sequence is constructed.

The adequate local C11/C13/C16/Con26 inputs and the selected primary Conrad passage are explicitly attributed.
The elementary box, perturbation, interpolation and discriminant calculations are local, with no new unit algorithm, source theorem acceptance, canonical U expansion, original classical proof audit or novelty claim.
This is AUTHOR checking only.
A separately organized noncontributor whole review, any fixed extraction/acceptance and navigation remain root's responsibility.
No mathematical native program, J, package, source intake or global write occurred.

<a id="trace-box-profile-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T05:31.
The COMPLETE Sections1--7/equations(1)--(11), actual order/seed/signature scope, locally proved finite box method, quantitatively positive rational simplex and both denominator bounds, actual full-root coefficient/circle upper bound, near-one dimension/conditioning cost and its precise nonobstruction limits, all changed norm-inventory/full original costs and source/contribution history are AUTHOR-FROZEN after complete local self-check.
The bounded author inquiry stops here.
This is not independent review or an adopted Claim, and no uniform O(m^-2) theorem or unrestricted G0001 completion is asserted.

Scoped material checking returned checked1 before the final clarifications/freeze and is repeated on this complete file.
No source/global/native mathematical artifact was changed.

## Registration and preservation operation

2026-10-12T05:57.
The full author account was copied from the responsible working material without abridgment.
Every original argument, example, failed transfer, cost, source boundary and author freeze remains above.
The working address is not retired until actual extraction review, acceptance if warranted, exact preservation comparison and consumer repair are complete.
