---
author: Yin
---

# Complete Toeplitz lattice duality and the exact first low-energy window

Date: 2026-10-11T18:39.
Human author: Yin.
Provenance: project deduction with checked classical supporting-plane attribution.
Internal organization under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied both substantive core candidates; the author supplied the complete continuity/normal-limit and bounded-integer-powers implementations.
Their actual contribution and checking relationships remain below.
No manuscript main-theorem designation or objective change is made.

## Statement

Let P be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, degree d>=2.
Let O be a specified full order of K=Q(alpha) containing alpha and alpha^-1, with an actual integral basis.
For an allowed coefficient window [0,T], N=T+1, let A be the integer d-by-N matrix of the powers1,alpha,...,alpha^T in that basis.
A has full row rank for T>=d-1.

An allowed rational coordinate f in Q^N has ACTUAL NONZERO residue Af in Z^d minus{0}.
Finite packets use positive normalized rational weights omega_b, exact lag cancellation sum_b omega_b sum_j f_(b,j) f_(b,j+h)=0 for EVERY1<=h<=T, and energy E=sum_b omega_b ||f_b||^2.
Let E_T^Q be its energy INFIMUM.
The formal-real version E_T^R allows real coefficients and weights while RETAINING the same integer coordinate condition Af in Z^d minus{0}, not only a numerical test at a chosen embedding.
It does not close the finite integer moment hull.

**A. Exact dual completeness at full row rank.** For T>=d-1 and rational symmetric POSITIVE DEFINITE Toeplitz W with diagonal1, put

    G_W=(A W^-1 A^T)^-1,
    mu(W)=min_(0!=r in Z^d) r^T G_W r,
    Gamma_T^Q=sup_W mu(W).

Then

    Gamma_T^Q=E_T^Q=E_T^R.

For every eta>0 some such rational W has mu(W)>E_T^Q-eta.
Each lattice minimum is attained, but the Toeplitz supremum and packet infima are NOT asserted attained.
No rational maximizing form, finite residue cutoff or denominator/algorithm bound follows.
The result applies to the ACTUAL chosen order basis and carries no maximal-order substitution.

**B. The first below-one window in O_0=Z[alpha] is exactly d.** In this monogenic order,

    E_T^Q=E_T^R=1 for T<d,
    E_d^Q=E_d^R<1.

There is therefore a finite RATIONAL exact complementary packet of energy below1, all values nonzero actual O_0 integers, and ACTUAL common union width exactly d.
This existence follows from a strict inequality for the infimum and does not assert an optimizer.
A specified overorder also admits a packet in allowed window[0,d], but may admit one at smaller width; the first-window equality is only for O_0.
Neither unit-only residues nor a prescribed seed norm/ideal inventory is imposed.

**C. Full costs and remaining uniformity obligation.** For every rational packet take its ACTUAL least coefficient denominator q, integer numerators F_b=q f_b, least final weight denominator M_w and m_b=M_w omega_b.
If D_b=Norm_K(f_b(alpha)), then all D_b are nonzero signed integers and

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(m_b)=q^(d M_w)product_b D_b^(m_b),
    (1/d)sum_b omega_b log|D_b|-(1/2)log E <=(T/d)m(P).

Contents, common Laurent shifts and possible Norm(alpha)^a signs are charged as in the argument.
Thus for every allowed window/order E_T^Q>=exp(-2T m(P)/d), and the formal-real infimum has the same bound by its equality with E_T^Q.
In particular exp(-2m(P))<=E_d<1 in O_0.
A hypothetical original total m(P)->0 sequence MUST have E_d->1.
No input-uniform positive deficit, arithmetic surplus, q/M_w/height/norm bound or unrestricted Mahler gap is established.

## Current assessment
[Selected decision](#decision-current-complete-isolated-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:39 |
| status | open |
| reason | Register the complete new dual-completeness and first-window arguments with exact sup/inf, actual-order and uniformity boundaries. Separate whole and actual C statement/interface review is pending; author self-check and retention do not themselves adopt either theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only A--C with nontorsion input, formal nonzero integer residue, full-rank dual range and O_0-specific first-window conclusion. |
| argument | [Argument](#argument) | Entire02:35 author freeze Sections1--10/Theorems1--2/real-singular-form lemma/equations1--19, including local supporting-plane and full arithmetic costs. |
| dependency | [Exact integer-moment energy and weak certificates](Yin_C_G0016_v1.md#statement) | Finite nonzero-integer moments and exact lag domain, rational/formal-real infimum equality, weighted all-representative quotient identity and weak Gamma<=E bound in the actual order basis. |
| dependency | [Monogenic short-window restriction](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Actual O_0 membership and individual width below d force integer coefficients; this fixes the endpoint E_T=1 and prevents the below-one packet from having actual union width smaller than d. |
| dependency | [Direct generic-monic window inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual rational packet's complete nonzero original integer resultants, common window and final weights; this local proof needs no reciprocal-input assumption. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T18:45 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only A--C with nontorsion input, formal nonzero integer residue, full-rank dual range and O_0-specific first-window conclusion. |
| argument | [Argument](#argument) | Entire02:35 author freeze Sections1--10/Theorems1--2/real-singular-form lemma/equations1--19, including local supporting-plane and full arithmetic costs. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Finite nonzero-integer moments and exact lag domain, rational/formal-real infimum equality, weighted all-representative quotient identity and weak Gamma<=E bound in the actual order basis. |
| dependency | [Dependency](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Actual O_0 membership and individual width below d force integer coefficients; this fixes the endpoint E_T=1 and prevents the below-one packet from having actual union width smaller than d. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual rational packet's complete nonzero original integer resultants, common window and final weights; this local proof needs no reciprocal-input assumption. |
| review | [Current finding](../audits/reviews/Yin_R_G0746_v1.md#c17-toeplitz-completeness-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-complete-isolated-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:16 |
| status | proved |
| reason | Adopt the exact complete current statement and selected full argument with R746's separately assigned isolated whole finding at this specific target. All actual-order/domain, finite/rational/formal-real, window, equality, original norm/denominator and unresolved-uniformity boundaries remain. The original UNKNOWN findings retain their actual dates, fixed inputs, source/checker/preservation facts and relationships; the new finding does not backfill their contexts or adopt any stronger conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Only A--C with nontorsion input, formal nonzero integer residue, full-rank dual range and O_0-specific first-window conclusion. |
| argument | [Exact retained argument](#argument) | Entire02:35 author freeze Sections1--10/Theorems1--2/real-singular-form lemma/equations1--19, including local supporting-plane and full arithmetic costs. |
| dependency | [Exact retained dependency](Yin_C_G0016_v1.md#statement) | Finite nonzero-integer moments and exact lag domain, rational/formal-real infimum equality, weighted all-representative quotient identity and weak Gamma<=E bound in the actual order basis. |
| dependency | [Exact retained dependency](Yin_C_G0014_v2.md#short-width-power-order-obstruction) | Actual O_0 membership and individual width below d force integer coefficients; this fixes the endpoint E_T=1 and prevents the below-one packet from having actual union width smaller than d. |
| dependency | [Exact retained dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Actual rational packet's complete nonzero original integer resultants, common window and final weights; this local proof needs no reciprocal-input assumption. |
| review | [Complete current isolated finding](../audits/reviews/Yin_R_G0746_v1.md#current-c17-complete-isolated-independent-finding) | Entire exact current Statement, complete selected Argument and all necessary interfaces, with actual complete initial judgment2026-10-22T19:11 preceding complete old-finding comparison2026-10-22T19:12; no proof repair, expanded source-proof scope or new native run. |

## Argument

The complete frozen D12 author account follows unchanged apart from first-title depth and final whitespace.
All necessary new reasoning is physically present here: finite-lag local feasibility and continuity, nearest-point normal limits with positive vertical component, whole-space PSD via rational perturbation and integer clearing, rational relative-Loewner regularization, real singular-form pigeonhole lemma, compact Gram/kernel limits and bounded integer companion powers.
No argument depends on declaring the integer moment hull closed or a primal energy attained.
The exact C inputs above supply reused current interfaces; historical comparisons are not hidden proof premises.

Classical finite-dimensional separation/support is attributed at [BV04-U001](../audits/literature/BV04/Yin_U001.md#bv04-u001).
The required application-specific geometry is proved locally in full, without importing a general SDP strong-duality or minimax theorem.
The torsion contradiction likewise uses the displayed direct integer-powers proof rather than a new external Kronecker dependency.

## Complete Toeplitz lattice duality and the first low-energy window

Date: 2026-10-12.
Authored by the paraunitary researcher AI for Yin.
This distinct draft was allocated before derivation, following the frozen D11 account now organized in C16.
Root supplied the substantive lag-value/supporting-plane/Toeplitz-regularization candidate, and subsequently the first-window compactness/companion candidate.
The author checked both in full and supplied the explicit local continuity proof, unit-normal nearest-point limit, and direct bounded-integer-powers conclusion.
Root is a contributor, not the whole noncontributor reviewer.
No native mathematical program, scan, solver, new J or new input control is used.

<a id="toeplitz-completeness-reuse-and-source"></a>
## 1. Exact previous scope and checked classical method

The complete [C16 v1 statement and argument](Yin_C_G0016_v1.md#statement), now adopted at its [organized-reviewed decision](Yin_C_G0016_v1.md#decision-organized-reviewed) after R301, are the immediate mathematical inputs.
They preserve the FINITE nonzero-integer residue moment hull, exact lag equations, rational/formal-real equality of infima and whole-lattice weighted quotient certificate.
That earlier result deliberately asserted only Gamma_T<=E_T, and no general optimizer or dual completeness.
Its displayed rational singular-range and finite-noise arguments remain its actual proof; this continuation does not silently change the old statement or claim that an old review already covered the theorem below.
The current exact [C14 v2 short-window result](Yin_C_G0014_v2.md#short-width-power-order-obstruction) and [C10 v2 generic-monic window inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) are used only at their stated interfaces.

Finite-dimensional separation/support is classical.
The author freshly read the registered primary BV04.pdf, Stephen Boyd and Lieven Vandenberghe, Convex Optimization, retained seventh printing with corrections, printed46--51/PDF60--65: Section2.5.1's nearest-point separation proof, Example2.20's separation of a point and a closed convex set, and Section2.5.2's supporting-hyperplane statement and proof.
Printed49 and51/PDF63 and65 were rendered and visually inspected to confirm inequalities and hypotheses.
The public author URL timed out; the existing registered local primary PDF was actually read.
The earlier [BV04 scoped account](../audits/literature/BV04/readme.md) covers different weak-duality/tangent/Schur passages and is NOT retroactively broadened.
This new inspection is recorded here; no source-intake write is performed by this author.

The newly retained [BV04-U001](../audits/literature/BV04/Yin_U001.md#bv04-u001) now provides the canonical selected separation/support interface, with root's distinct reading and unchanged source identity.
Its exact scope and application obligations were read before this freeze.
This navigation adds no broader theorem or inspection claim.
The two disposable rendered pages were removed from the author's temporary directory after inspection; the registered primary PDF is unchanged.

Only classical method attribution is taken from those pages.
Sections3--4 below reconstruct the entire finite-dimensional supporting-plane argument needed here, including local continuity and the nonzero vertical normal.
No general semidefinite-program strong-duality theorem, closedness of the integer moment hull, minimax interchange, primal attainment or rational maximizing form is adopted.
The final bounded-integer-powers step is also proved directly, so no additional Kronecker or geometry-of-numbers theorem is needed.

<a id="toeplitz-completeness-statement"></a>
## 2. Actual domain and the new conclusions

Fix an ACTUAL monic irreducible nontorsion integer-unit polynomial P, degree d>=2, K=Q(alpha), and a specified full order O containing alpha and alpha^-1.
Choose an actual Z-basis of O.
Let A be the integer d-by-N coordinate matrix of 1,alpha,...,alpha^T in that basis, where N=T+1 and T>=d-1.
Its rank is d because the first d powers are a rational basis of K.
In the monogenic order O_0=Z[alpha], those first d columns are I_d.

An allowed coordinate is f in Q^N with A f in Z^d minus{0}; equivalently its value is a nonzero actual O element.
The formal-real extension uses f in R^N with the SAME integer coordinate requirement A f in Z^d minus{0}.
It does not test only the numerical value at one selected embedding.
A finite packet has positive normalized weights.
Define the lag functionals and energy by

    a_h(f)=sum_(j=0)^(T-h) f_j f_(j+h), 1<=h<=T,
    a(f)=(a_1(f),...,a_T(f)),
    E=sum_b omega_b ||f_b||^2.                       (1)

Exact complementary packets require sum omega_b a(f_b)=0.
Their rational and formal-real energy infima, as in C16, are E_T^Q and E_T^R.
C16 proves

    0<E_T^Q=E_T^R<=1.

For rational symmetric POSITIVE DEFINITE Toeplitz W with diagonal1, define

    G_W=(A W^-1 A^T)^-1,
    mu(W)=min_(0!=r in Z^d)r^T G_W r,
    Gamma_T^Q=sup_W mu(W).                          (2)

All matrices and residue vectors use this actual order basis.
Each minimum in (2) is positive and attained by an integer vector, by positive-definite coercivity.
This does not assert that the supremum over W is attained.

**Theorem 1, dual completeness.** For every stated fixed input, order and window T>=d-1,

    Gamma_T^Q=E_T^Q=E_T^R.                           (3)

The equality is between a supremum and infima.
For every eta>0, some rational positive-definite Toeplitz W has mu(W)>E_T^Q-eta.
No maximizing rational W, finite residue cutoff, attained primal minimum or effective coefficient bound is asserted.

**Theorem 2, exact first window in the monogenic order.** For O=O_0,

    E_T^Q=E_T^R=1 for T<d,
    E_d^Q=E_d^R<1.                                  (4)

Consequently there exists a finite rational exact complementary packet with every value a nonzero actual O_0 integer, normalized energy below1, and ACTUAL common union width exactly d.
The existence follows from a strict inequality for the infimum, not from a claimed optimizer.
An overorder also admits a below-one packet in allowed window [0,d], but can admit one in shorter width; the exact first-window assertion is not extended to overorders.

Theorems1--2 address arbitrary nonzero integral residues, not a prescribed seed ideal/norm inventory or unit-only family.
They supply neither a uniform energy deficit below1 nor uniform coefficient/weight denominators, and do not resolve the unrestricted G0001 gap.

<a id="finite-lag-value-and-continuity"></a>
## 3. A finite-packet convex value function with a genuine lag neighborhood

Use formal-real coefficients and weights for this section.
For each a in R^T let

    v(a)=inf{sum_b omega_b ||f_b||^2:
       a=sum_b omega_b a(f_b),
       A f_b in Z^d minus{0},
       omega_b>0, sum_b omega_b=1, finite packet}.    (5)

Initially an empty feasible set would give v(a)=+infinity.
The constructions below in fact make v finite everywhere.
Convexity needs no attainment: take packets within any positive error of v(a) and v(b), mix them with weights theta and1-theta, and let the error tend to zero.
Omitting zero weights handles the endpoints theta=0,1.
Thus v is convex and v>=0.
By definition v(0)=E_*=E_T^R, with 0<E_*<=1 from C16.

For ||a||_1=s<=1, use the constant polynomial1 at weight1-s, and for each a_h!=0 use

    1+sign(a_h)t^h at weight |a_h|.

Each coordinate is integral in the specified order and nonzero at alpha: alpha^h=+1 or-1 would make alpha torsion.
Each such binomial has coefficient energy2 and only one positive-lag correlation, sign(a_h) at h.
Therefore this finite packet has exact lag vector a and energy1+s.
Zero weights are omitted, so the strict-positive-weight convention is respected.
In particular,

    0<=v(a)<=1+||a||_1<=2 when ||a||_1<=1.           (6)

For arbitrary a, choose an integer L>=1 with L^2>=s, use L(1+sign(a_h)t^h) at weights |a_h|/L^2, and use1 at the remaining weight.
The lag vector is again exactly a, all residues remain nonzero actual integers, and its energy is 1+2s-s/L^2<=1+2s.
Thus no global feasible-lag domain assumption is hidden.

Continuity at zero follows directly from (6), not from an uninspected convex-function regularity theorem.
For 0<s=||a||_1<1 put u=a/s.
Convexity gives

    v(a)<= (1-s)E_*+s v(u)<=E_*+2s.

Also 0=(a+s(-u))/(1+s), so convexity gives

    E_*<= [v(a)+s v(-u)]/(1+s),
    v(a)>=(1+s)E_*-2s>=E_*-2s.

Hence

    |v(a)-E_*|<=2||a||_1 near0.                    (7)

The dependence on actual packet residues is maintained throughout.
This is not a continuous relaxation that allows zero or arbitrary real residue vectors.

<a id="exact-supporting-plane-without-hull-closure"></a>
## 4. Complete supporting-plane argument without primal attainment

Let H be the epigraph of v, the set of (a,t) with t>=v(a), and put C=closure H in R^(T+1).
Convexity of v makes H and C convex.
Put p=(0,E_*).
This point belongs to H by the definition of epigraph, even if E_* is not achieved by any packet.
For xi>0 put p_xi=(0,E_*-xi).

Continuity (7) shows p_xi is outside C: a sequence (a_n,t_n) in H converging there would have v(a_n)->E_* and t_n>=v(a_n), a contradiction.
The set C is nonempty and closed.
There is a nearest point q_xi in C to p_xi.
To prove this without a compact-set assumption on all of C, note that p in C has distance xi; minimize distance on C intersect the closed ball of radius2xi centered at p_xi.
This set is nonempty and compact in finite dimension, and every point outside that ball is farther than the available point p.
Thus the attained minimum is global.
Its distance is positive, and

    0<||q_xi-p_xi||<=xi, ||q_xi-p||<=2xi.

Define the unit vector n_xi=(q_xi-p_xi)/||q_xi-p_xi||.
For each z in C, the segment q_xi+t(z-q_xi), 0<=t<=1, lies in C.
Minimality at t=0, applied to the squared distance to p_xi, gives

    n_xi dot(z-q_xi)>=0.                            (8)

Take xi->0 along a sequence and a subsequence of the unit normals converging to n=(h,b).
The unit sphere is compact, so ||n||=1; also q_xi->p.
Passing to the limit in (8), for every z in C,

    h dot a+b(t-E_*)>=0 whenever (a,t) in C.

Upward epigraph rays imply b>=0.
If b=0, then the points (a,2) in H for all ||a||_1<=1 would imply h dot a>=0 on a symmetric neighborhood of zero, forcing h=0.
That contradicts ||n||=1.
Hence b>0.
Set g=-h/b.
Since (a,v(a)) belongs to H for every a,

    v(a)>=E_*+g dot a for every a in R^T.            (9)

This is the needed GLOBAL real supporting affine function.
For instance testing a=+/-e_h in (6) also gives |g_h|<=2-E_*, so its coefficients are finite.
No differentiability was used.

Only the epigraph of the value function was closed as a device for constructing a supporting plane.
The finite integer moment hull from C16 is not replaced by its closure, no point of that closure is declared realizable, and the point p is not declared to be an attained primal energy.
Inequality (9) concerns the original v defined by finite packets.

<a id="support-form-and-full-positivity"></a>
## 5. The supporting form is Toeplitz and positive semidefinite on the whole space

Apply (9) to the one-coordinate packet consisting of ANY allowed formal-real f.
Its energy is ||f||^2 and its lag vector is a(f).
Since v(a(f))<=||f||^2, define W by

    W_(j,j)=1,
    W_(j,j+h)=W_(j+h,j)=-g_h/2.
    f^T W f=||f||^2-g dot a(f)>=E_*
       whenever A f in Z^d minus{0}.               (10)

The factor1/2 is required because both symmetric off-diagonal entries occur in f^T W f.
W is real symmetric Toeplitz with diagonal1; it is not yet asserted rational or positive definite.

In fact W>=0 on ALL of R^N.
If some real vector has negative W-quadratic value, continuity gives an open set of negative vectors.
The rational kernel of A is a proper subspace, since the constant column represents the nonzero element1.
Its complement intersects that open set, and rational vectors are dense there.
Choose a rational z with z^T W z<0 and A z!=0.
Clear its coefficient denominators by a positive integer k.
Then k z is an INTEGER coefficient polynomial and A(kz) is a nonzero integer vector.
It is an allowed coordinate, contradicting (10), since E_*>0 but (kz)^T W(kz)<0.

This also handles a putative negative direction inside ker A: perturb it within the open negative set to a rational vector outside ker A before clearing denominators.
No forbidden zero-residue atom is used to prove positivity.
W may remain singular and irrational.
Neither its inverse nor a quotient Gram matrix for that singular W is introduced.

<a id="rational-regularization-and-dual-completeness"></a>
## 6. Positive-definite regularization and rational certificates approach E_*

For real 0<delta,epsilon<1 put

    W_delta=(1-delta)W+delta I_N.
    W_delta>=delta I_N>0,
    f^T W_delta f>=(1-delta)E_* for all allowed f.   (11)

The last inequality follows from (10) and the nonnegative term delta||f||^2.
W_delta still has diagonal1 and is Toeplitz.
Since N>=d>=2, approximate each of its off-diagonal constants by a rational number within epsilon delta/(N-1), keeping the diagonal EXACTLY1; call the resulting symmetric Toeplitz matrix W'.

For the error D=W'-W_delta, each absolute row sum is at most epsilon delta.
Symmetry and 2|x_i x_j|<=x_i^2+x_j^2 imply |x^T D x|<=epsilon delta||x||^2.
Therefore

    W'>=W_delta-epsilon delta I_N
        >=(1-epsilon)W_delta>0.                    (12)

This gives a RATIONAL positive-definite Toeplitz matrix in the exact class (2).
Combining (11)--(12), every allowed f satisfies

    f^T W' f>=(1-epsilon)(1-delta)E_*.

For each nonzero integer r, its weighted least representative

    f_(W',r)=W'^-1 A^T(A W'^-1 A^T)^-1 r

is rational and satisfies A f_(W',r)=r, by full row rank.
Thus it is itself an allowed atom.
C16's complete-square identity, or direct substitution, now gives

    r^T G_(W') r>=(1-epsilon)(1-delta)E_*,
    mu(W')>=(1-epsilon)(1-delta)E_*.

Let delta and epsilon tend to zero.
The existing weak inequality Gamma_T^Q<=E_* and C16's rational/formal-real equality give (3).
In particular a rational certificate gets arbitrarily close below the energy infimum.
This proves Theorem1.

Rational approximation here concerns finitely many entries of an already positive-definite real matrix and preserves a verified relative Loewner inequality.
It is not an assertion that a real optimum has rational entries, or that the supporting W is invertible.
The construction uses no minimum of the open positive-definite Toeplitz domain and no attained finite-packet energy.
It supplies no coefficient or bit bound for W' and no efficient computation of its exact integer minimum.
For an actual overorder the same proof uses its actual integer basis matrix A_O; it never substitutes the maximal order or drops an index.

<a id="real-singular-form-integer-floor"></a>
## 7. A real singular form cannot retain a positive integer floor

The following elementary lemma is needed because limits of rational Gram matrices need not be rational.

**Lemma.** If a real symmetric H>=0 satisfies r^T H r>=1 for EVERY nonzero r in Z^d, then H is positive definite.

If rank H=0 the assertion is immediate by testing a coordinate vector.
Otherwise suppose rank H=k<d, and write H=B^T B for a real k-by-d matrix B of rank k.
This is ordinary finite-dimensional positive-semidefinite diagonalization; no lattice theorem is invoked.
The images of the integer grid {0,...,L}^d lie in a cube [-C L,C L]^k for one fixed finite C, obtained by summing the absolute values in each row of B.

Choose a fixed box side ell>0 with k ell^2<1 and partition that cube into at most (ceil(2CL/ell)+1)^k boxes.
For sufficiently large integer L this is less than the (L+1)^d grid points, because k<d.
Two distinct grid points therefore have images in the same box.
Their nonzero integer difference r satisfies

    r^T H r=||B r||^2<=k ell^2<1,                  (13)

a contradiction.
This proves the lemma.
It is a full argument for a REAL singular limit; the earlier rational zero-pivot witness alone would not justify it.
No finite integer search, native pigeonhole experiment, Minkowski theorem or approximation rate uniform in d is being supplied.

<a id="first-low-energy-window-exact-degree"></a>
## 8. Exactly one full extra power forces a below-one packet

Now specialize to O_0 and T=d, so N=d+1.
Write the actual columns of A as a_0,...,a_d, with a_j=e_j for0<=j<d and a_d the full integer remainder of alpha^d.
Every a_j is nonzero, since it represents a power of the nonzero alpha.

We prove Gamma_d^Q<1.
The constant packet gives E_d<=1, and weak duality gives Gamma_d^Q<=1.
Suppose instead Gamma_d^Q=1.
Choose rational positive-definite Toeplitz W_n with diagonal1 and mu_n=mu(W_n)->1.
Put

    G_n=(A W_n^-1 A^T)^-1,
    K_n=W_n-A^T G_n A>=0.                          (14)

The last inequality is the weighted quotient square completion for every real coefficient vector, not only integer residue vectors.

Since each coordinate monomial e_j is a representative of the nonzero integer residue a_j,

    mu_n<=a_j^T G_n a_j<=e_j^T W_n e_j=1
      for0<=j<=d.                                  (15)

In particular the diagonal entries of G_n, using j<d, are at most1.
Positive definiteness gives |(G_n)_(i,j)|<=1 by its two-by-two minors.
Likewise |(W_n)_(i,j)|<=1.
Extract a simultaneous entrywise convergent subsequence,

    G_n->G_*, W_n->W_*.

Both limits are positive semidefinite; W_* is Toeplitz with diagonal1.
For each FIXED nonzero integer r, r^T G_n r>=mu_n; passing to the limit gives r^T G_* r>=1.
This retains every integer r, with no claim that the minimizing vectors remain bounded.
The real-form lemma in Section7 gives G_*>0.

The j-th diagonal entry of K_n is 1-a_j^T G_n a_j, which tends to zero by (15).
Since K_n>=0, its two-by-two minors give |(K_n)_(i,j)|^2<=(K_n)_(i,i)(K_n)_(j,j), so every entry tends to zero.
Hence

    W_*=A^T G_* A.                                 (16)

Let M be the ORIGINAL integer companion matrix for multiplication by alpha in the power basis.
It satisfies M a_j=a_(j+1),0<=j<d.
For0<=i,j<d the Toeplitz shift identity in the (d+1)-by-(d+1) W_* gives

    (M^T G_* M)_(i,j)
       =a_(i+1)^T G_* a_(j+1)
       =(W_*)_(i+1,j+1)
       =(W_*)_(i,j)=(G_*)_(i,j).

Therefore M^T G_* M=G_*.
Positive definiteness provides fixed constants0<c<=C with c||x||^2<=x^T G_*x<=C||x||^2.
Every column of every nonnegative power M^n then has Euclidean norm at most sqrt(C/c), since the G_* norm is preserved.
All those matrix entries are INTEGERS.
There are only finitely many integer matrices with that entry bound, so M^u=M^v for some0<=u<v.
The actual unit companion M is invertible, hence M^(v-u)=I.
Applied to the coordinate of1, this says alpha^(v-u)=1, contradicting nontorsion.

This direct bounded-integer-powers argument proves the needed torsion implication for the whole original field without selecting or discarding conjugates and without adopting another source theorem.
It completes the contradiction Gamma_d^Q<1.
Theorem1 now gives E_d^Q<1.

Choose any number between that infimum and1.
By the definition of infimum, some ACTUAL finite rational packet has energy below that number, so it has E<1.
No optimizer is needed.
C14's actual monogenic short-width theorem gives E_T=1 for T<d, and also prevents a below-one packet in allowed window[0,d] from having actual common union width smaller than d.
Thus its actual width is d, proving Theorem2.

The extra power alpha^d is essential in this argument: window d supplies the full shifted basis a_1,...,a_d needed to compare M^T G_*M with G_*.
At window d-1 that complete Toeplitz shift comparison is unavailable, consistently with E_(d-1)=1.

For any specified overorder containing O_0, the same monogenic packet is still admissible, so allowed window[0,d] has a below-one packet there as well.
The first possible width can be smaller in an overorder, exactly as C14's fixed e=2 control already demonstrates.
No new numerical or algebraic input control is introduced in this draft.

<a id="dual-completeness-full-cost-and-uniformity-boundary"></a>
## 9. Full arithmetic cost and what the new existence does not give

Every packet asserted by Theorem2 is finite with rational coefficients and positive normalized rational weights.
For its ACTUAL least coefficient denominator q, integer numerators F_b=q f_b, ACTUAL least final weight denominator M_w, and m_b=M_w omega_b, write D_b=Norm_(K/Q)(f_b(alpha)).
All original values are nonzero algebraic integers, so D_b is a nonzero signed integer.
The full formulas are

    Res(P,F_b)=q^d D_b,
    S=q^2 E,
    I=log q+(1/d)sum_b omega_b log|D_b|,
    product_b Res(P,F_b)^(m_b)
       =q^(d M_w) product_b D_b^(m_b).              (17)

All degrees are the original d, and every norm factor and multiplicity is retained.
If labels are recorded before a common Laurent shift, the factor Norm(alpha)^a, possibly -1, must also be included.
Integer content c_b obeys c_b^d dividing q^d D_b; |D_b|=1 suffices for c_b|q but is not necessary.
No content removal or residue rescaling is part of the existence proof.

The true arithmetic surplus is at least -(1/2)log E>0 because every |D_b|>=1.
C10's complete original-root window inequality simultaneously gives

    (1/d)sum_b omega_b log|D_b|-(1/2)log E
        <=(T/d)m(P),
    E>=exp(-2T m(P)/d).                             (18)

For the monogenic first window this implies

    exp(-2m(P))<=E_d^Q<1.                           (19)

The lower inequality passes to the infimum.
Along any hypothetical sequence with original total m(P)->0, its optimum E_d MUST tend to1.
Thus the degree-linear window theorem supplies no uniform positive deficit and no uniform surplus; indeed the retained cost inequality forces that deficit to vanish on such a hypothetical sequence.

The proof is nonconstructive in its supporting normal, lattice minima, limiting Gram matrices and the strict contradiction.
It bounds neither the q and M_w of a below-one primal packet nor the denominators of near-optimal rational dual matrices.
The infinite integer residue set has not been replaced by a finite enumeration.
The infimum comparison supplies finite packets at each strictly larger level, not an algorithm or a rational optimum.

The values and their ideals/norms in the new first-window packet are unrestricted NONZERO integral residues.
Hence this does not subsume C11/C13's distinct constructions preserving a fixed seed ideal/full-norm inventory and reaching arbitrarily low normalized energy by allowing width to grow.
Nor does it close C9/C12's unit-only or relative-rank questions.
Ordinary binomial complements were already known; their use in Section3 only supplies a local lag neighborhood, not the final low-energy packet or a new binomial existence theorem.

<a id="toeplitz-completeness-author-self-check"></a>
## 10. Complete author self-check and review boundary

The author self-check covers the actual full order and full-row-rank matrix; formal-real integer residues versus single-embedding evaluation; exact lag and factor1/2 conventions; finite-packet convexity without attainment; all binomial nonvanishing, local and global weights, omitted zero labels and finite energies; the explicit two-ray continuity estimate; outside-point and nearest-point existence for the closed epigraph, unit-normal compactness, every limiting inequality and positive vertical coefficient; the distinction between epigraph closure and integer-hull realization; the negative-direction perturbation through the proper rational kernel, integer clearing and full PSD conclusion; singular/irrational support matrix versus rational PD approximants, complete row-sum Loewner error and all weighted least representatives; supremum/infimum quantifiers with no rational maximizing form.

For the new first-window theorem the check covers every nonzero monomial residue, both bounded matrix subsequences, integer inequalities surviving the limit without a finite shortest-vector list, the real singular-form pigeonhole argument in every rank, full K_n diagonal and off-diagonal convergence, exact Toeplitz shift indices0,...,d, the actual companion and all bounded INTEGER powers, invertibility and nontorsion contradiction.
The proof then uses strict infimum inequality to obtain a finite rational packet and uses the exact monogenic short-width boundary to identify its actual width.
The overorder exception, full original norms/signs/contents/denominators, the lower energy expense and all input-uniform limitations remain explicit.

Root supplied both substantive proof candidates, and the author supplied the stated local reconstruction and simplification.
This is author self-review, not a separately organized whole review.
No mathematical native program, new control, J or source-intake write was used.
Primary-PDF text extraction and rendering were read-only source inspection, not mathematical numerical evidence.
Separate whole noncontributor review and current dependency/adoption decisions remain root's responsibility.
G0001 remains active and unrestrictedly unresolved.

<a id="toeplitz-completeness-entire-author-freeze"></a>
The COMPLETE Sections1--10, Theorems1--2, the real singular-form lemma, equations(1)--(19), all supporting-plane and matrix limits, first-window consequence and full arithmetic/attainment limitations are author-frozen at2026-10-11T18:35 for a separately organized whole noncontributor review.
Scoped material validation passed before this paragraph and is repeated afterward; it verifies structure and locators, not mathematics.
Root's substantive contribution prevents treating root's coordination as the required noncontributor review.
Author work on this frozen input now stops.



## Registration and preservation operation

2026-10-11T18:39: retain the complete2026-10-11T18:35 D12 freeze directly as the Claim argument.
C16's earlier weak-duality-only statement remains unchanged at its old physical version and review scope; this distinct new C owns the strengthened conclusion and proof.
The selected first-window statement separates actual width from allowed support and the monogenic order from overorders.
New C-specific statement/argument bindings require actual inspection by the separate whole reviewer.
The original D is retired only after complete-body comparison and incoming-reference maintenance.
No native mathematical program, new allowance or Task completion accompanies registration.
