---
author: Yin
---

# Complete selected boundary modules, trace quotients and small-measure metric pivots

This is the SAME actual selected primitive edge and coefficient sequence, with all complete [L311](../ledger/Yin_L_G0311_v1.md), [L313](../ledger/Yin_L_G0313_v1.md) and [L315](../ledger/Yin_L_G0315_v1.md) proof chains retained.
Original formal findings and source/authorship/input histories remain at R210/R212/R214; known R212 independence is not erased by current SELF.

<a id="statement"></a>
## Complete statement

Let P be the ACTUAL monic irreducible reciprocal nontorsion unit of degree d=2s, constant1,TOTAL m=log M(P)>0, P=t^s Q(t+t^-1), O=Z[alpha],B=Z[tau],tau=alpha+alpha^-1.
Q is monic irreducible degree s, without total-reality/maximal-order/unramified hypotheses.
Use U_0=1,U_1=x,U_(j+1)=xU_j-U_(j-1); S_Q is the coefficient matrix of (Q(x)-Q(y))/(x-y) in ascending monomials.
At ONE fixed n>=s, choose the LEAST diagonal minimizer k of Pi=R^T H^-1R, R=[r_1...r_n].
With r_l=coeff rem_Q U_(l-1),H=sum_(l=1)^n r_l r_l^T,ell=r_k^T H^-1r_k<=s/n, retain the POSITIVE RATIONAL primitive scale q and primitive integer w=qH^-1r_k.
Let a have coefficients S_Q w,nu=|Norm_(Q(tau)/Q)(a)|>=1,c_l=w^Tr_l for EVERY l>=1, and B_a(z)=z^(s-1)a(z+z^-1).
Then a is nonzero/primitive, sum c_l z^(l-1)=B_a/P has no cancellation at any original root, and F=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)) is the ACTUAL primitive selected auxiliary.
Future observations never reselect w or get free coefficient energy.
All d original roots and the actual characteristic-zero degree are retained.

For EVERY b>=1, K_b=(c_(b+i+j))_(0<=i,j<d) is a finite Hankel matrix and
    det K_b=(-1)^s nu², v_p(det K_b)=2v_p(nu)
at EVERY prime including ramification/index primes.
The same exact determinant holds for every NONZERO INTEGRAL row-space w without selection.
Its complete factorization V diag(B_a(alpha_h)alpha_h^b/P'(alpha_h))V^T uses transpose, ALL original roots, the unit root-product and exact Vandermonde cancellation.
It recovers the full EDGE norm nu², not Res(P,F).
The forward original-degree recurrence sum_(j=0)^d p_j c_(l+j)=0,l>=1, gives an integral unimodular companion J and
    K_(b+h)=J^h K_b=K_b(J^T)^h,h>=0.
For ANY finite collection of full windows, horizontal joining has exactly the earliest full block's integer column lattice, index/maximal-minor gcd nu²; vertical joining has its same row lattice.
Adding future individual state columns preserves this module.
Block-diagonal r-fold repetition has normalized log determinant2log(nu)/d, so it creates no normalized arithmetic gain.
Lower-order invariants are NOT determined by nu alone.
No unchanged analytic/operator growth is claimed.

With actual entry multiplicities mu_j=min(j+1,2d-1-j),
    E_b=sum_(j=0)^(2d-2)mu_j c_(b+j)²>=d nu^(4/d),
    sum_(j=0)^(2d-2)c_(b+j)²>=nu^(4/d).
No d consecutive terms are all zero, but an individual next coefficient may vanish.
On the RAW projection scale eta_l=c_l/q, gamma=nu^(1/s)/q,
    det(eta_(b+i+j))=(-1)^s nu²/q^d,
    v_p(det eta)=2v_p(nu)-d v_p(q),
    sum mu_j eta_(b+j)²>=d gamma²,
    E_b/S_2(F)²>=d gamma²/(2ell)>=n gamma².
These rational and primitive integer determinants are distinct.
At n<=Cs the b=n+1 block ends at n+2d-1<=(C/2+2)d.
For fixed degree-linear windows, sufficiently small TOTAL m makes delta_k=content(r_k)=1 and q=L_k integer, without an upper bound on that scale or a universal positive gamma payment.

Let M_a be multiplication by a in actual basis1,tau,...,tau^(s-1).
For EVERY b, K_b is LEFT/RIGHT INTEGER unimodularly equivalent to M_a direct_sum M_a, so
    coker_Z K_b≅(B/aB) direct_sum(B/aB).
The proof uses the actual unimodular coefficient pairing G_P and actual integral O=B direct_sum alpha B, not a rational index division.
If e_1|...|e_s are positive invariant factors of M_a INCLUDING trivial1s, K_b has exactly e_1,e_1,...,e_s,e_s.
Primitivity gives e_1=1, hence its first TWO factors are1.
For D_r the gcd of ALL r-minors,D_0=1,
    D_(2j)=(e_1...e_j)²,0<=j<=s,
    D_(2j+1)=(e_1...e_j)² e_(j+1),0<=j<s.
At EVERY prime p let g_p=gcd(Q modp,a modp),h_p=deg g_p∈[0,s-1].
Then nullity(K_b modp)=2h_p,rank=2(s-h_p)>=2 and
    |ker(K_b modp^H)|=p^[2sum_j min(H,v_p(e_j))],H>=1.
No squarefreeness/residue-degree assumption is made.
The EXACT modular gcd of P and B_a is t^h_p g_p(t+t^-1), degree2h_p, including repeated/characteristic2 factors.
The minimal reduced recurrence denominator has degree2(s-h_p), constant1.
This modular loss never changes the original characteristic-zero degree.

EVERY d-consecutive coefficient block has gcd1.
For B_n=max(1,floor(n/d)),
    sum_(l=1)^n c_l²>=B_n,sum|c_l|>=B_n,#nonzero c_l>=B_n,
    q²>=n B_n/s,S_2(F)²>=2B_n,S_1(F)>=2B_n.
This is a LOWER scale bound, with no unjustified rho lower bound from unequal coefficients.
For the REUSED actual P=t²-A t+1,A>=3,n2,unique selected k=1,w=1,a=1, ALL invariant factors stay1 while q=L=1+A² and complete leading measures M(F)=A,M(edge)=A²-1 grow.
All signed norm(1+A²)²(4-A²), degree4, radial2m and full coefficients remain.
Its TOTAL m grows; it refutes only an invariant-list/d/n-only upper scale bound and is no near-one counterexample.

For the further small-m theorem fix real C>2,n=ceil(Cs),u=(C+1)m and ACTUAL pivot j=c_k=qell∈Z_(>0).
Let E=sum c_l²=q²ell=qj,A1=sum|c_l|,rho=2A1²/E,S_2²=2E,S_1=2A1.
The full monomial-removed degree T satisfies0<T<=2n,Tm/d<=u.
Retain c0=log2/4,h0=c0 exp(-20),
    b(u)=max(u,sqrt(u/c0)log sqrt(c0/u)),
    epsilon(u)=min(1,15sqrt(b(u))+4u),D(u)=epsilon(u)+4u,
for0<u<=h0.
These are increasing,epsilon>=u,epsilon<=1 and epsilon=O(u^(1/4)(1+log(1/u))^(1/2)).
The SAME exponent full resultant q^d Z_(2k),Z_(2k)>=1, and complete coefficient-energy inequality give
    exp(-2u)<=2ell[1-epsilon(u)+rho D(u)].
Integer coefficients give A1<=E and ell rho<=2j², hence
    4j²D(u)>=exp(-2u)-2ell[1-epsilon(u)].
The right side need not be positive in the entire initial domain.
For
    u<=min(h0,u_C),u_C=log[2C/(C+2)]/2,
    kappa_C=(C-2)/(40C),
the explicit uniform bounds are
    j²>=kappa_C/epsilon(u),height(F)>=j,
    q>=C sqrt(kappa_C/epsilon(u)),
    S_2(F)²>=(C-2)/(20epsilon(u)).
For sufficiently small positive TOTAL m, j,height,q are at least constant_C m^(-1/8)(1+log(1/m))^(-1/4) and tend to infinity along ANY hypothetical such sequence, regardless of ell tending to0.
No sequence is constructed, and C2/torsion/m0 are excluded.
At the established delta1 scope these are genuine lower bounds on the INTEGER Gram order L, without a new prime-distribution claim.

For fixed C>2,H>=1, a class with height of THIS selected primitive F<=H has a complete CONDITIONAL gap:
choose0<u_*<=min(h0,u_C) with epsilon(u_*)<kappa_C/H²; no covered input has m<=u_* /(C+1).
No such selected-height upper bound is supplied, and bounded original P or arbitrary row-space witnesses do not instantiate it.
For actual edge norm nu and gamma,
    gamma²<=nu^(2/s)epsilon(u)/(C²kappa_C).
A uniformly bounded nu^(1/s) on a hypothetical near-one sequence forces gamma->0; no such sequence/trace-unit occurrence is asserted.
Conversely gamma>=gamma0>0 forces
    nu^(1/s)>=gamma0 C sqrt(kappa_C/epsilon(u)),
    log(nu)/s>=log(1/epsilon(u))/2+log(gamma0 C sqrt(kappa_C)).
No upper bound on nu is proved.

Every original norm/depth/rational normalization, complete leading/root/Mahler/positive-evaluation cost and ACTUAL monomial-removed Tm/d remain.
The large log L cancels its matching coefficient scale and supplies no new positive SAME-exponent cyclic income.
The actual powered-degree escape retains all norm multiplicities.
The original pre-freeze maximal-minor-versus-lower-invariant clarification, coefficient-pairing wording clarification and superseded weaker fixed-margin pivot inference remain in their complete accounts.
HR08 supplies only selected classical Hankel factorization attribution; Hun74-U005 supplies the already checked finite commutative-PID classification at its original SELF/source-completion boundary.
All project-specific determinant/module/metric/pivot transitions are fully proved locally.
No uniform future-coefficient/coherence/edge-measure upper bound, existence of near-one inputs or unrestricted gap is established; no source/native/program execution occurs.

## Complete argument

<a id="argument"></a>

## Entire all-shift determinant and integer-module proof

<a id="joint-boundary-reuse-and-domain"></a>
### 1. Changed question, reuse and actual domain

The joint_boundary_research AI for Yin develops this proof-only contribution after the preceding resultant_research turn ended without substantive D178 content or a live mathematical computation.
The coordinator assigned the question but supplied no derivation.
The exact Task, actual actor binding and applicable knowledge-reuse and writing rules were read.
This work asks what arithmetic and energy information is obtained by inspecting MANY actual consecutive boundary indices of the SAME selected column.
It does not select another column after each boundary observation.

The direct inputs are [L300's order/content and original norm formulas](Yin_C_G0571_v1.md#statement), [L304's selected dual system](Yin_C_G0588_v1.md#selected-edge-dual-system), and [L308's complete formal generating identity](Yin_C_G0588_v1.md#trace-edge-formal-generating-identity).
L308 has already ruled out a mandatory nonzero NEXT coefficient on an actual globally selected unbounded-degree family; its fixed positive total measure is not a near-one counterexample.
The present result instead applies on EVERY actual input, including any hypothetical sequence of total measures tending to zero.
It gives an exact full-degree determinant and a limitation on accumulating arithmetic through shifted full boundary windows.

Before sustained derivation, a bounded local search for Hankel matrices, moment determinants, consecutive zeros, primitive remainder orders and boundary energy checked the pertinent G ledgers and drafts, the source registry and audit navigation.
[L147](../ledger/Yin_L_G0147_v1.md) has a Hankel matrix of the coefficients of P and a sampling estimate, not the coefficient sequence B_a/P used below.
[L107](Yin_C_G0304_v1.md#canonical-trace-defect) supplies the algebraic Lagrange/trace normalization already consumed by L304; its no-unit-circle dynamical hypotheses are NOT transferred.
The local [BR10 definition supplement](../audits/literature/BR10/Yin_U002.md#formal-hankel-rank) distinguishes a formal Hankel matrix from a bounded operator.
We use only finite matrices with constant anti-diagonals and import no analytic Hankel-operator theorem.

A bounded external recognition search used the exact terms "Hankel determinant resultant rational generating function Bezout matrix determinant theorem".
The primary [Heinig--Rost, Bezoutians, Chemnitz preprint](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf) was opened at its title, foreword and contents: Sections7.1--7.2 are explicitly about rational generating functions and Vandermonde factorization of Hankel matrices.
Subsequent tool searches of the fetched PDF failed to resolve text and a later open timed out.
No formula, theorem, source-proof acceptance or locally retained artifact is asserted from that incomplete screen.
This confirms the classical structured-matrix setting, not novelty of a general Hankel/resultant mechanism.
The exact specialization below is proved directly from the retained algebraic trace identity; no unavailable external statement is a premise.
One initial local rg invocation used an unsupported Windows wildcard path and was immediately corrected with a filename glob; it produced no mathematical output or mutation.

The coordinator subsequently acquired the exact [HR08 preprint](../literature/pdf/HR08.pdf).
At 2026-10-10T09:11 the author inspected Sections7.1--7.2 through Proposition7.8, with the exact source/consumer normalization recorded in the [selected source note](../audits/literature/HR08/readme.md#selected-hankel-factorization-inspection).
Its classical rational Hankel factorization is explicitly attributed; the project-specific determinant and integral-module conclusions below retain complete proofs.

Let P be monic irreducible reciprocal nontorsion of ACTUAL degree d=2s, with constant coefficient1, and write

    P(t)=t^s Q(t+t^-1), m=log M(P)>0.

All d original roots alpha_1,...,alpha_d are retained, with no power-degree reduction.
The s distinct trace roots are tau_j=alpha+alpha^-1.
Put B=Z[tau], and write Norm_+(a) for the field norm of a in Q(tau), not a maximal-order norm or a normalized average.

At a fixed anti window n>=s, retain the L304 matrices r_l=coeff rem_Q U_(l-1), R_n, H_n and Pi_n, where U_0=1,U_1=x,U_(j+1)=xU_j-U_(j-1).
Choose the LEAST diagonal minimizer k, and its positive primitive scale q=q_k and primitive integral vector w=q H_n^-1 r_k.
In particular q can be rational.
Write

    a(x)=polynomial with coefficient vector S_Q w,
    c_l=w^T r_l for EVERY l>=1,
    B_a(z)=z^(s-1)a(z+z^-1),
    sum_(l>=1)c_l z^(l-1)=B_a(z)/P(z),
    F=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)),
    nu=|Norm_+(a)| in Z_(>0).                         (1)

The c_l are integers, a is nonzero and primitive, and B_a is an integral polynomial formally reciprocal at degree d-2.
It has no common original root with P.
These are the exact L304/L308 conclusions.
The extended c_l for l>n are observations of the SAME w; they are not coefficients of the original finite F and need their own energy charge.

<a id="joint-boundary-full-degree-determinant"></a>
### 2. An exact determinant of every full original boundary block

For an integer b>=1 define the d-by-d finite Hankel matrix

    K_b=(c_(b+i+j))_(0<=i,j<d).                       (2)

Thus K_(n+1) uses the actual extended indices n+1 through n+2d-1.
The term Hankel here means exactly that the entries depend on i+j.
No boundedness, positivity or infinite-operator interpretation is asserted.

**Proposition.** For every input and actual selected column in(1), and every b>=1,

    det K_b=(-1)^s Norm_+(a)^2=(-1)^s nu^2.            (3)

In particular the determinant does not vanish and is independent of the boundary location b.
The same formula holds for every nonzero integral row-space vector w, without a minimizer hypothesis; its relevance here is that all quantities in(1) come from the actual selected primitive column.

**Proof.** Keep every original inverse pair.
At a root alpha with trace tau,

    P'(alpha)=alpha^(s-1)(alpha-alpha^-1)Q'(tau),
    B_a(alpha)/P'(alpha)=a(tau)/[(alpha-alpha^-1)Q'(tau)].

All denominators are nonzero: P and Q are separable in characteristic zero, and alpha is not plus or minus1.
The pair alpha,alpha^-1 consequently contributes

    a(tau)(alpha^l-alpha^-l)/[(alpha-alpha^-1)Q'(tau)]
      =a(tau)U_(l-1)(tau)/Q'(tau)

to the following exact trace expansion, which is also L304's formula:

    c_l=sum_(h=1)^d [B_a(alpha_h)/P'(alpha_h)] alpha_h^l.
                                                               (4)

No complex conjugation is inserted.
Nonreal original roots and nonreal trace embeddings remain present in their complete algebraic trace.
Put V_(i,h)=alpha_h^i for0<=i<d.
Equation(4) gives the FULL factorization

    K_b=V diag(B_a(alpha_h)alpha_h^b/P'(alpha_h)) V^T. (5)

The elementary Vandermonde formula and the product of all derivatives are

    (det V)^2=product_(i<j)(alpha_j-alpha_i)^2,
    product_h P'(alpha_h)
       =(-1)^(d(d-1)/2) product_(i<j)(alpha_j-alpha_i)^2.

Thus every separation factor cancels algebraically, before any absolute-value estimate.
Since product_h alpha_h=1, its b-th power contributes1.
Finally

    product_h B_a(alpha_h)
       =(product_h alpha_h)^(s-1) product_h a(tau_h)
       =Norm_+(a)^2,

because each trace embedding occurs twice among the d original roots.
As d=2s, d(d-1)/2 has parity s.
Taking determinants of(5) proves(3).
This is exact original-conjugate coherence; it neither replaces a signed sum by its absolute values nor discards a discriminant cost in an inequality.
The cancellation occurs in an identity.
Q irreducible and deg a<s ensure nu>0.
This completes the proof.

The full determinant's prime depths are therefore

    v_p(det K_b)=2v_p(Norm_+(a))                       (6)

at EVERY rational prime, including ramified and index primes.
This is a statement about the determinant; it does not assign equal local depths to its individual entries or to original conjugates.
The edge A of L304 satisfies Res(P,A)=nu^2, so(3) has recovered exactly the existing complete EDGE norm.
It has not produced the different auxiliary resultant Res(P,F).

<a id="joint-boundary-integral-window-module"></a>
### 3. Several full windows yield the same integral arithmetic module

Write P(t)=sum_(j=0)^d p_j t^j with p_0=p_d=1.
Reciprocity and the full generating identity in(1) imply the forward recurrence

    sum_(j=0)^d p_j c_(l+j)=0 for every l>=1.          (7)

Indeed, the coefficient of z^(l+d-1) in P(z)sum c_r z^(r-1) vanishes because deg B_a<=d-2.
Reversing its p-indices uses p_j=p_(d-j) and yields(7).
There is no cancellation of the original degree-d recurrence.

Let J be the integral d-by-d matrix with ones at positions(i,i+1) for0<=i<d-1, zero other entries in these first d-1 rows, and last row

    (-p_0,-p_1,...,-p_(d-1)).

Then det J=(-1)^d p_0=1.
Its inverse is integral: the previous first coordinate is solved from the last row using p_0=1.
Applying(7) to every column of K_b, and then using symmetry, gives

    K_(b+1)=J K_b=K_b J^T,
    K_(b+h)=J^h K_b=K_b(J^T)^h for h>=0.             (8)

**Proposition.** Choose ANY finite collection of actual boundary locations b_1,...,b_r>=1 and let b_*=min b_j.
Their horizontal joint matrix

    X=[K_(b_1) K_(b_2) ... K_(b_r)]

has precisely the same lattice of integer column combinations as K_(b_*):

    X Z^(rd)=K_(b_*) Z^d,
    [Z^d : X Z^(rd)]=nu^2.                           (9)

The greatest common divisor of ALL its d-by-d minors is exactly nu^2.
The analogous vertical joint matrix has the same lattice of integer row combinations as K_(b_*).
These statements also hold if additional individual consecutive future state columns are inserted after one full K_(b_*) block.

**Proof.** By(8) every block is K_(b_*) times an integral matrix, and a block equal to K_(b_*) is present.
These two inclusions prove the column-lattice equality.
Its index is |det K_(b_*)| by ordinary integral volume, equal to nu^2 by(3).
Alternatively, without an index theorem, every maximal minor of X is det K_(b_*) times an integer minor of its right factor; one such minor is det K_(b_*) itself.
This proves the gcd assertion directly.
Transposition gives the row assertion.
Every further state column is an integral combination of the first d by(7), proving the final statement.
Equivalently, subtracting the appropriate integer combinations of the first block's columns reduces X to [K_(b_*),0,...,0]; this specifies the actual integer equivalence and requires no uninspected Smith-normal-form theorem.
This completes the proof.

Consequently the arithmetic gcd of the maximal minors has depth EXACTLY2v_p(nu) at p, however many such windows are used.
In particular when the actual selected a is a trace unit (nu=1), every K_b is unimodular and this joint invariant is1 on the ENTIRE input, not merely on a radical example.
A large auxiliary floor L_k supplies no extra divisor of these boundary determinants.
This is an all-input limitation on this specific proposed source of arithmetic income, valid equally on any hypothetical near-one input whose selected edge is a unit.

Taking a block DIAGONAL product instead of joining the windows gives determinant magnitude nu^(2r), but also dimension rd.
Its normalized logarithmic determinant remains

    log|det diag(K_(b_1)...,K_(b_r))|/(rd)
       =2log(nu)/d.                                 (10)

Thus repeating full-window determinant income does not improve its dimension-normalized value.
This does not say that the entries, operator norms or analytic growth at different boundaries are redundant.
Equation(8) can amplify those quantities strongly; the theorem identifies only the integral module and determinant data.

The common module can have lower-order determinantal divisors not specified by its index nu^2.
We have proved that adjoining shifted full windows does not change that module; we have NOT proved that every invariant of the first window is determined by nu alone.
The explicit norm-only conclusion concerns its determinant and the gcd of its maximal minors.

<a id="joint-boundary-energy-and-selected-scale"></a>
### 4. Compulsory joint energy and the selected normalization

There is a genuine multi-index energy consequence.
Put

    mu_j=min(j+1,2d-1-j) for0<=j<=2d-2,
    E_b=sum_(j=0)^(2d-2) mu_j c_(b+j)^2=||K_b||_F^2.

The weights are1,2,...,d-1,d,d-1,...,1 and are actual entry multiplicities.
If sigma_1,...,sigma_d are the positive singular values of the REAL matrix K_b, then product sigma_i=|det K_b|=nu^2.
Arithmetic--geometric mean applied to sigma_i^2 proves

    E_b>=d nu^(4/d),
    sum_(j=0)^(2d-2)c_(b+j)^2>=nu^(4/d).              (11)

The second inequality uses mu_j<=d.
In particular there cannot be d consecutive zero terms anywhere: such terms would be the first row of some K_b, contradicting(3).
A zero single next coefficient is fully compatible with(11), as L308 already demonstrates.
These are exact lower bounds on the indicated finite set of ACTUAL coefficients; no all-real trace-root hypothesis is used.

For the selected column write

    ell=r_k^T H_n^-1 r_k,
    eta_l=c_l/q=r_l^T H_n^-1 r_k,
    sum_(l=1)^n eta_l^2=ell<=s/n,
    gamma=nu^(1/s)/q>0.                              (12)

The raw eta_l are usually rational, not primitive integral coefficients.
Dividing(3) and(11) by the appropriate powers of q gives the exact identities and bound

    det(eta_(b+i+j))=(-1)^s nu^2/q^d,
    sum_(j=0)^(2d-2) mu_j eta_(b+j)^2>=d gamma^2,
    gamma^2=nu^(4/d)/q^2.                            (13)

At every prime the first rational determinant has valuation

    2v_p(nu)-d v_p(q).                               (14)

Here v_p(q) has its usual rational meaning; no integrality is claimed for the raw determinant.
The primitive integer determinant(3) and the projection-scale determinant(13) must not be interchanged.

Since S_2(F)^2=2q^2 ell, the joint energy relative to the ORIGINAL auxiliary's coefficient energy also satisfies

    E_b/S_2(F)^2 >= d nu^(4/d)/(2q^2 ell)
                         >= n gamma^2.              (15)

This is a lower bound, not the missing upper control on conjugate expense.
At degree-linear n<=Cs, the boundary block b=n+1 ends at n+2d-1<=(C/2+2)d.
Hence it is still a fixed degree-linear collection of indices; making the block full-dimensional has not silently introduced an exponentially late time.

The actual small-TOTAL-measure consequence supplied by [L300](Yin_C_G0571_v1.md#near-one-primitive-trace-remainders), using [L168](Yin_C_G0391_v1.md#bounded-power-degree-escape), is that for fixed C and m tending to zero, EVERY trace-remainder content delta_k is1 at s<=n<=Cs.
Thus the selected q becomes the integer L_k, and(13)--(15) become

    gamma^2=nu^(4/d)/L_k^2,
    E_b/S_2(F)^2>=n nu^(4/d)/L_k^2.                 (16)

The cited inputs delta_k=1 and nu>=1 supply no upper bound on L_k or positive input-independent lower bound on nu^(1/s)/L_k.
This paper proves no such bound, and does not construct small-m inputs with unbounded L_k.
Therefore integer nonvanishing of the joint boundary determinant cannot by itself be called a degree-uniform PAYMENT on the raw projection scale.
The exact omitted quantity is gamma, not a missing original-root label or a missing choice of boundary location.
Several normalized determinants still carry the SAME gamma and the SAME valuations(14); the lattice conclusion(9) supplies no new independent divisibility merely by adjoining windows to repair that normalization.

The old L308 selected radical control has nu=1 and q=74, so gamma=1/74, even at unbounded degree.
This is quoted only as an already established check of the normalization: it is not a new computation, a new fixed-positive example or a statement that gamma tends to zero in the near-one domain.
The essential new boundary(9) is an ALL-input theorem and uses no fixed-measure control to infer a small-measure obstruction.

<a id="joint-boundary-complete-cost-scope"></a>
### 5. Full costs retained and the precise remaining discriminator

All formulas above retain the entire actual P and the primitive selected auxiliary F.
The simultaneous L300/L304 arithmetic formulas remain, with delta=content(r_k), u=r_k/delta, q=L/delta:

    H_n w=L u,
    Res(P,F)=L^d P(1)P(-1) Norm_+(u(tau))^2,
    Res(P,A)=nu^2,
    A(alpha_i)=alpha_i^(n+s)a(tau_i),
    S_2(F)^2=2q^2 ell,
    rho(F)=2(sum_(l=1)^n |c_l|)^2/sum_(l=1)^n c_l^2,
    v_p(F(alpha_i))=v_p(L)+v_p(alpha_i-alpha_i^-1)
                                  +v_p(u(tau_i)).    (17)

Every original p-adic label, ramification and repeated reduction is covered by(17).
Boundary determinant valuations(6) are instead edge-norm valuations and do not inherit the auxiliary floor L.
No cyclic norm at a new exponent has been produced by(3) or(9).
The columns remain selected at the original window n; their future eta_l need not satisfy projection-diagonal bounds belonging to a newly selected larger window.

If an initial monomial is removed from F, its actual remaining degree T<=2n must still pay Tm/d; the coefficient norms, contents, rho and original resultant remain unchanged.
Full leading coefficients and all roots of F and A remain part of M(F) and M(A).
Their coefficient bounds M(F)<=S_2(F), M(A)<=S_2(A) are only upper bounds; nu=1 does not make M(A)=1 or the original positive evaluations sum_i log^+|A(alpha_i)| vanish.
No estimate in this paper pays L229's complete conjugate-coherence expense, changes that inequality, or converts the auxiliary floor to same-exponent cyclic income.

The resulting discriminator is concrete.
A proposed joint-boundary proof that uses only determinant nonvanishing, gcds of maximal minors, prime divisibility of THOSE quantities or products of the full Hankel determinants has exactly the arithmetic content of the already known edge norm nu^2.
It cannot claim additional independent arithmetic merely by adding locations.
A changed proof must use quantitative information not contained in that invariant, for example a uniform small-total-m estimate on gamma together with a genuinely useful analytic upper bound for the SAME weighted future coefficients, a useful lower-order module invariant already present in one full block, or a signed original-conjugate constraint stronger than the determinant.
Such an upper bound must still pay the future coefficient, primitive-scale, leading, radial and full coherence costs; proving gamma bounded below alone is not asserted to solve G0001.

This contribution gives an exact joint determinant, its integral-module invariance under arbitrarily many actual boundary shifts, and the full normalization of its compulsory energy.
It does not prove that a near-one sequence exists, that selected trace edges are always units, that gamma has a positive universal lower bound, or that all conceivable joint-boundary analytic mechanisms fail.
G0001 remains unresolved and its current execution is paused.
No mathematical program, finite scan or J payload was created.
The coordinator's HR08 acquisition has its separate canonical provenance; the author performed the selected source reading just stated.


## Entire selected trace-quotient and modular recurrence proof

<a id="lower-boundary-reuse-and-domain"></a>
### 1. Exact question and reused inputs

This is proof-only work by the joint_boundary_research AI for Yin.
The coordinator supplied the broad question and no derivation.
The applicable rules, actual actor binding and exact unrestricted Task contract remain those checked in the preceding contribution.
The new question concerns ALL lower-order integral invariants of the SAME actual selected boundary matrices, rather than repeating their full determinant.

The direct input [L311](#joint-boundary-full-degree-determinant) supplies its complete selected sequence, original-degree Hankel factorization and unimodular shift.
A targeted local search for coefficient pairings, Smith/invariant factors, trace direct sums and multiplication cokernels found precisely the two required older mechanisms: [L63's unimodular coefficient pairing](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) and [L66's actual trace-order direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index).
Both were read at their full consumed scope.
L66 already uses the direct sum to obtain two-copy Frobenius quotients.
The new identification is of the ACTUAL selected Hankel quotient with the quotient by its trace edge; the general two-copy method and coefficient pairing are not new results here.
[L107](Yin_C_G0304_v1.md#canonical-trace-defect) supplies the already checked algebraic identity between coefficient extraction and Tr(h/P'); its no-neutral dynamical hypotheses are not used.

The recognized invariant-factor input has a precise existing source check: [Hun74-U005](../audits/literature/Hun74/Yin_U005.md#hun74-u005), IV.6.12, printed p.225, and IV.6.13, p.226, classify finitely generated modules over a commutative PID by invariant factors.
Here the PID is Z and all modules are finite.
We retain that source audit's actual self-review, proof completions and cross-chapter boundary; no new source-wide audit is claimed.
The integral matrix equivalence below is proved directly.
Its Smith-matrix interpretation is explained by elementary integer row/column reduction, rather than attributing a matrix statement to a source passage that was only inspected in module language.
These adequate local inputs end the bounded reuse search; no new external theorem, download or program is needed.

Use the full L311 domain: P monic irreducible reciprocal nontorsion of ACTUAL degree d=2s and constant1, P(t)=t^s Q(t+t^-1), O=Z[alpha], B=Z[tau], tau=alpha+alpha^-1.
Q is the actual monic irreducible trace polynomial, with no total-reality or maximal-order hypothesis.
At one fixed n>=s let k be the least minimum-diagonal index of Pi_n, and retain

    r_l=coeff rem_Q U_(l-1), H_n=sum_(l=1)^n r_l r_l^T,
    ell=r_k^T H_n^-1 r_k<=s/n,
    w=q H_n^-1 r_k in Z^s primitive, q>0 rational,
    coeff(a)=S_Q w, c_l=w^T r_l for all l>=1,
    B_a(t)=t^(s-1)a(t+t^-1),
    K_b=(c_(b+i+j))_(0<=i,j<d), b>=1.                (1)

The actual primitive anti polynomial is F=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)).
The trace element a is nonzero and primitive.
Write nu=|Norm_(Q(tau)/Q)(a)|.
L311 has already proved det K_b=(-1)^s nu^2 and all-shift module invariance.
They are reused, not presented as new conclusions.
No boundary observation changes the chosen column or rescales its coefficients.

<a id="selected-hankel-trace-quotient"></a>
### 2. Complete integral reduction to two copies of the trace quotient

Let M_a be multiplication by a on the trace order B, in its actual basis1,tau,...,tau^(s-1).
This is an s-by-s integral matrix of nonzero determinant Norm(a).

**Theorem.** For every b>=1, the actual matrix K_b is equivalent by left and right unimodular INTEGER matrices to

    M_a direct_sum M_a.

Consequently

    coker_Z K_b is isomorphic to (B/aB) direct_sum (B/aB).       (2)

This includes every prime, ramification and nonreduced modular specialization, and involves all d original coordinates.
It is not a rational-basis equivalence with an omitted lattice index.

**Proof.** Let lambda_P(h) be the coefficient of t^(d-1) in rem_P h.
The already checked Lagrange identity is

    lambda_P(h)=Tr_(Q(alpha)/Q)[h(alpha)/P'(alpha)].

It holds for every polynomial h by first reducing modulo P.
In the actual power basis of O the pairing lambda_P(xy) has integral Gram matrix G_P.
Its entries are0 when i+j<d-1 and1 when i+j=d-1.
Therefore det G_P=(-1)^(d(d-1)/2), as in L63; in particular it is unimodular even at discriminant primes.

L311's full original-conjugate formula for c_l gives

    (K_b)_(ij)=lambda_P(alpha^(b+i+j) B_a(alpha)).

Write Mult_O(x) for the integral multiplication matrix of an element x of O.
Then, exactly in this power basis,

    K_b=G_P Mult_O(alpha^b B_a(alpha))
       =G_P Mult_O(alpha^(b+s-1)) Mult_O(a).          (3)

The first two factors on the last line are unimodular: G_P has just been checked, and alpha is a unit in the ACTUAL order O.
Thus K_b is integrally equivalent to Mult_O(a).
L66 supplies the integral basis

    1,tau,...,tau^(s-1), alpha,alpha tau,...,alpha tau^(s-1)

of O=B direct_sum alpha B.
Its change from the original power basis is unimodular because both are actual Z-bases, not merely field bases.
In this basis multiplication by a acts as M_a on each summand, proving the asserted matrix equivalence and(2).
This proof retains all original conjugates through lambda_P and does not require the roots of Q to be real.
This completes the proof.

The classical coefficient-pairing and direct-sum mechanisms have thus identified the entire cokernel, not just its size nu^2.
The new object is the particular ideal aB determined by the selected dual system in(1), not an arbitrarily chosen trace ideal.

<a id="doubled-lower-invariant-factors"></a>
### 3. Every invariant factor is duplicated; every prime layer is even

Let e_1|e_2|...|e_s be the positive invariant factors of M_a, INCLUDING initial factors1 so that there are exactly s terms.
Equivalently these are the orders in the finite-group decomposition of B/aB, padded by trivial summands.
Hun74's finite Z-module theorem gives uniqueness; all factors are nonzero because a!=0 in the trace field.

For completeness the matrix interpretation is elementary.
Integer row and column swaps, adding integer multiples and changing signs preserve the integral presentation.
Euclidean divisions reduce a chosen nonzero pivot until it divides its entire row and column; clearing them leaves a smaller block.
If the pivot fails to divide an entry in that block, adding its row to the pivot row and repeating division strictly reduces the positive pivot.
This terminates.
The resulting pivot divides every remaining entry; recurse on the block.
This produces a positive diagonal with each entry dividing the next.
All operations are unimodular, and the corresponding quotient is the displayed sum of cyclic groups, whose uniqueness is exactly the recorded PID-module input.
This paragraph is a direct matrix derivation of the familiar Smith interpretation, not a new classification theorem or an asserted source-wide proof inspection.

By(2), the 2s invariant factors of K_b, in order, are

    e_1,e_1,e_2,e_2,...,e_s,e_s.                     (4)

The divisibility order survives duplication, so the finite-module uniqueness applies without any reordering ambiguity.
Moreover e_1=1: the first column of M_a is the coefficient vector of a and is primitive.
Hence the gcd of ALL its entries is1, which integer operations preserve.
Thus the first TWO boundary invariant factors are1 on every actual selected input.

For a full-rank integer matrix X let D_r(X) denote the positive gcd of all its r-by-r minors, with D_0=1.
Row/column operations preserve this gcd: after one elementary addition every new minor is an integer combination of old minors, and the inverse operation gives the reverse divisibility.
On a diagonal in divisibility order, the gcd is the product of its first r diagonal entries.
Therefore(4) supplies EVERY lower-order determinantal divisor:

    D_(2j)(K_b)=(e_1...e_j)^2,              0<=j<=s,
    D_(2j+1)(K_b)=(e_1...e_j)^2 e_(j+1),   0<=j<s.  (5)

These can contain information not determined by nu=e_1...e_s, precisely the distinction left open by L311.
In particular the even-indexed determinantal divisors are squares, and D_1=D_2=1.
Formula(5) does not say that all invariants are trivial when the edge norm exceeds1.

For every rational prime p, reduce Q and a coefficientwise modulo p and put

    g_p=gcd(Q mod p,a mod p), monic, h_p=deg g_p.

Primitivity of a ensures a mod p is not the zero polynomial; hence0<=h_p<=s-1.
Multiplication by a on F_p[x]/(Q mod p) has kernel dimension h_p: writing Q=g_p Q_1 and a=g_p a_1, its kernel condition Q|af is equivalent to Q_1|f because Q_1 and a_1 are coprime.
The classes Q_1 v with deg v<h_p give exactly that kernel.
No squarefreeness of Q mod p is used.
Applying(2) gives

    dim_(F_p) ker(K_b mod p)=2h_p,
    rank_(F_p)(K_b mod p)=2(s-h_p)>=2.                (6)

Every higher prime-power layer is likewise duplicated.
More explicitly, for H>=1,

    |ker(K_b mod p^H)|
       =p^[2 sum_(j=1)^s min(H,v_p(e_j))].            (7)

This follows by solving e_j x=0 modulo p^H in each cyclic coordinate of the integral diagonal reduction.
The exponent at EACH layer is even; no residue-degree, unramified, maximal-order or separability condition over F_p is needed.
Formula(7) records entire local modules, rather than assigning an averaged valuation to every original root.

<a id="modular-selected-denominator"></a>
### 4. The exact modular recurrence loss and a primitive coefficient block

The same h_p describes the complete modular cancellation in L308's actual generating function.
Work for this paragraph over F_p and set

    G_p(t)=t^(h_p) g_p(t+t^-1).

This is a monic reciprocal polynomial of degree2h_p and constant1.
One has EXACTLY

    gcd(P mod p,B_a mod p)=G_p,
    reduced denominator of (B_a/P) mod p=(P mod p)/G_p,
    degree of that denominator=2(s-h_p).             (8)

To prove it, lift Q=g_p Q_1 and a=g_p a_1 under x=t+t^-1.
The displayed G_p divides both polynomials.
The quotient B_a/G_p is a polynomial because h_p<=s-1 and deg a_1<=s-1-h_p.
Coprimality of Q_1 and a_1 gives a Bezout identity over F_p[x].
Substitution proves that their lifts are coprime in F_p[t,t^-1].
Since P/G_p has constant1, no factor t can occur in their ordinary polynomial gcd either.
This proves(8).
The reduced numerator degree is at most2(s-h_p)-2 and its denominator constant is1.
Thus that denominator is the minimal recurrence polynomial for the reduced sequence: any other recurrence would multiply the same rational series to a polynomial and hence would be divisible by this coprime denominator.

This is an exact MODULAR degree loss, and is not a change of the original characteristic-zero degree d=2s.
In particular p=2 and repeated factors at t=plus/minus1 need no separate squarefree convention; the argument in the Laurent ring and the doubled module remain valid.

There is also a coefficient constraint at a shorter horizon than L311's full2d-1-entry Hankel block:

    gcd(c_b,c_(b+1)...,c_(b+d-1))=1 for every b>=1. (9)

Indeed, the first s remainder columns r_1,...,r_s form a unimodular matrix.
Since w is primitive, gcd(c_1,...,c_s)=1, and consequently the initial d-coordinate state has content1.
L311's forward companion matrix J is integral unimodular; it takes each d-coordinate state to the next.
An integer automorphism preserves the gcd of coordinates, in both directions, proving(9).
This proof does not conclude that any particular one of the c_l is plus or minus1.
It does imply that every such block contains a coefficient not divisible by any specified prime, even when K_b has a nontrivial mod-p kernel as in(6).

Let

    B_n=max(1,floor(n/d)).

Disjoint d-coordinate blocks among the first n terms, together with the primitive initial s-block when n<d, give the genuine size/support constraints

    sum_(l=1)^n c_l^2>=B_n,
    sum_(l=1)^n |c_l|>=B_n,
    #{l<=n:c_l!=0}>=B_n.

Since the ACTUAL selected column has sum c_l^2=q^2 ell and ell<=s/n, it follows that

    q^2>=n B_n/s,
    S_2(F)^2>=2B_n, S_1(F)>=2B_n.                    (10)

This is a LOWER bound on the original positive primitive scale, valid even when q is rational.
For long windows it is stronger than using only one nonzero integer coefficient.
It is not an upper bound paying that scale or the future conjugate expense.
The support bound does not by itself bound rho= S_1(F)^2/S_2(F)^2 below by2B_n, since the coefficients need not have equal magnitude.

<a id="lower-invariants-scale-boundary"></a>
### 5. What the complete invariants do not control

The preceding theorem supplies the exact missing lower-order invariants, but their values are arithmetic data of aB.
They do not determine the Euclidean Gram metric or primitive scale.
This failure can already be checked in the REUSED L300 all-window quadratic control, without a new radical family or computation.

Take the existing actual irreducible input P=t^2-A t+1, integer A>=3, at the fixed proportional window n=2=2s.
Its recurrence row is(1,A), so k=1 is the UNIQUE diagonal minimizer, w=1 and the trace edge a=1.
Thus ALL boundary invariant factors are1 for all A, but

    q=L=1+A^2, delta=1, ell=1/(1+A^2),
    F=A t^4+t^3-t-A,
    edge E(t)=-A+(A^2-1)t,
    S_2(F)^2=2(1+A^2), S_1(F)=2(A+1),
    Res(P,F)=(1+A^2)^2(4-A^2), Res(P,E)=1,
    M(F)=A, M(E)=A^2-1.                              (11)

These are direct specializations of the full L300/L296 formulas, whose actual irreducibility and complete circle-root/leading-factor proof are retained inputs.
The positive original root is alpha=(A+sqrt(A^2-4))/2; total m=log alpha grows with A, and the original radial charge is Tm/d=2m.
The full auxiliary degree4, both leading factors and every original root are retained.
In particular delta=1 and identical COMPLETE integral invariant factors coexist with unbounded q and unbounded coefficient size even at the same d and n/s.
This refutes a bound depending only on that invariant-factor list and d,n; it does NOT refute a bound that also uses small TOTAL m.
No new fixed-positive family is proposed as a near-one counterexample.

For fixed s<=n<=Cs and hypothetical m tending to zero, L300/L168 still supply delta_k=1 and hence q=L.
The new(10) then reads L^2>=n B_n/s.
It introduces no opposing upper bound.
The exact remaining quantities include L, the metric location of the ideal aB relative to the actual remainder Gram matrix, and the signed original-conjugate evaluations.
Even when the whole cokernel is trivial, the unimodular matrices in(3) and the trace-basis conversion have no asserted small coefficient or operator norms.

All original expenses remain as in L300/L304/L311:

    Res(P,F)=L^d P(1)P(-1) Norm(u)^2, u=r_k/delta_k,
    S_2(F)^2=2q^2 ell,
    rho(F)=2(sum|c_l|)^2/sum c_l^2,
    v_p(F(alpha_i))=v_p(L)+v_p(alpha_i-alpha_i^-1)
                                      +v_p(u(tau_i)).           (12)

These preserve every original local embedding, repeated reduction and primitive content.
The new boundary modules instead describe the trace edge a, and need not carry the L floor.
Any removal of an initial monomial from F retains the same norm and coefficient quantities but uses the actual remaining degree T<=2n in Tm/d.
The complete M(F),M(edge), leading factors and original positive evaluations are not replaced by nu or by their invariant factors.
No new cyclic norm income, full-coherence upper bound or uniform Mahler gap follows.

The contribution is the exact selected quotient(2), all duplicated lower invariants and prime-power layers, the modular recurrence loss with nonreduced cases included, and the primitive d-coordinate coefficient block leading to(10).
The failed implication in(11) specifies why integral classification alone cannot supply a primitive-scale upper bound.
A changed small-total-m proof must add actual metric/conjugate control.
G0001 remains unresolved and its current execution is paused.


## Entire small-TOTAL-measure pivot and metric-scale proof

<a id="small-measure-pivot-reuse"></a>
### 1. Changed estimate and precise reused inputs

This is proof-only work by the joint_boundary_research AI for Yin.
The coordinator supplied the broad question and no derivation.
The exact Task contract, applicable rules and actual binding retain the checks made in the preceding contribution.
The target is a genuinely SMALL-TOTAL-measure constraint on an ACTUAL selected primitive column, rather than another growing-measure countercontrol or a repetition of the integral classification.

The direct algebraic inputs are [L296's actual selected column and norm identity](Yin_C_G0571_v1.md#statement), [L300's primitive order and near-one content conclusions](Yin_C_G0571_v1.md#near-one-primitive-trace-remainders), and [L313's complete quotient classification](#selected-hankel-trace-quotient).
The analytic input is [L229's full original-conjugate coefficient-energy bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound), including its explicit epsilon and its retained Pri11/Dim19 external statement/proof-inspection boundaries.
L296 already derives a necessary GROWTH OF EFFECTIVE SUPPORT from that bound.
We reuse it and do not claim a new angular-discrepancy estimate.
The new conclusion below is growth of the actual selected primitive PIVOT COEFFICIENT and therefore its coefficient height, even if its minimum diagonal tends to zero.

A bounded local screen read these exact premises, searched adjacent projection/Gram/endpoint and primitive-scale records, and checked [L241](Yin_C_G0570_v1.md#endpoint-projection-toeplitz-interface), which warns that its fixed-input Toeplitz limit has no input-uniform linear-window rate.
No such rate is imported here.
L313 gives only a measure-free scale lower bound and an exact integral module; neither supplies the new small-m quantitative conclusion.
The needed remaining step is an integer-coefficient inequality and the exact selected diagonal identity, so these local inputs are sufficient.
No additional external theorem, acquisition, program or claimed novelty of those elementary inequalities is involved.

Let P be monic irreducible reciprocal nontorsion of ACTUAL degree d=2s and constant1, with total m=log M(P)>0.
All original roots, powered-degree multiplicities and actual trace order are those of L296/L300.
Fix a real C>2 and set n=ceil(Cs).
For the LEAST diagonal minimizer k of the actual anti projection retain

    ell=(Pi_n)_(kk)>0, ell<=s/n<=1/C,
    q>0 the positive primitive scale,
    c=q Pi_n e_k in Z^n primitive,
    F(t)=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)).           (1)

The integer j:=c_k=q ell is POSITIVE.
It is an actual coefficient of F, at exponent n+k; the coefficient at n-k is -j.
Both positions remain distinct.
Primitivity here is coefficient normalization of the entire selected column; no arbitrary row-space unit edge is substituted for it.
For now q is permitted to be rational.

Write

    E=sum_l c_l^2=q^2 ell=qj,
    A=sum_l |c_l|,
    S_2(F)^2=2E, S_1(F)=2A, rho=2A^2/E.            (2)

An initial monomial may be removed from F; this leaves every quantity in(2), its coefficient height and the original resultant unchanged.
The actual remaining degree T is positive and at most2n.
Put u=(C+1)m, so Tm/d<=u because n/s<=C+1.

For explicit finite statements reuse L229's increasing function on0<u<=h_0:

    c_0=log(2)/4, h_0=c_0 exp(-20),
    b(u)=max{u,sqrt(u/c_0) log sqrt(c_0/u)},
    epsilon(u)=min{1,15sqrt(b(u))+4u},
    D(u)=epsilon(u)+4u.                              (3)

The retained estimate gives epsilon(u)>=u and epsilon(u)->0, with

    epsilon(u)=O(u^(1/4)(1+log(1/u))^(1/2)).           (4)

These are actual original-root bounds at all required degree-linear frequencies, not estimates in the normalized height m/d with a lost degree factor.

<a id="exact-selected-pivot-coherence"></a>
### 2. Exact pivot-coherence inequality

**Proposition.** In the domain(1)--(3), whenever0<u<=h_0,

    4j^2 D(u)>=exp(-2u)-2ell[1-epsilon(u)].           (5)

This is a necessary condition on the actual selected primitive pivot j.
Its right side is allowed to be nonpositive for some parameters; positive lower bounds below state their additional domain explicitly.

**Proof.** L296 gives the SAME-exponent identity at every original root alpha_i,

    F(alpha_i)=q alpha_i^(n-k)(alpha_i^(2k)-1),
    |Res(P,F)|=q^d Z_(2k),
    Z_(2k)=|Res(P,t^(2k)-1)|>=1.                     (6)

The cyclic norm is a nonzero integer because the input is nontorsion.
No equality of actual powered degree with d is assumed.
Formula(6) remains correct for rational q and the actual primitive F, and yields log|Res(P,F)|/d>=log q.

Apply L229 to the entire monomial-removed F and increase its positive radial parameter Tm/d to u using its proved monotonicity.
All leading factors and all coefficients remain in S_2 and rho.
It gives

    log q<=log S_2(F)+u
            +(1/2)log[1+(rho-1)epsilon(u)+4rho u].

Since S_2(F)=q sqrt(2ell), subtracting log q and exponentiating gives the exact necessary inequality

    exp(-2u)<=2ell[1-epsilon(u)+rho D(u)].            (7)

The selected diagonal ell is retained here.
Replacing it prematurely by1/C gives only the older effective-support condition and loses the stronger pivot conclusion.

The crucial integrality step is

    A<=E,
    ell rho=2A^2/q^2<=2E^2/q^2=2j^2.               (8)

Indeed |c_l|<=c_l^2 for every INTEGER coefficient, including zero; the remaining equalities use(2), including E=qj.
There is no bound on how many coefficients are nonzero and no assertion that their magnitudes are equal.
Substitute(8) into(7) to obtain(5).
This completes the proof.

This argument uses the actual algebraic norm to control all original roots before applying the full coefficient/conjugate inequality.
It does not bound an isolated conjugate, treat small m as a pointwise small evaluation bound, or transfer a free integral trace direction to the selected column.

<a id="near-one-height-and-scale-divergence"></a>
### 3. A uniform small-total-measure lower bound for height and scale

Set

    u_C=(1/2)log[2C/(C+2)]>0,
    kappa_C=(C-2)/(40C)>0.

For every actual selected input above with

    0<u=(C+1)m<=min(h_0,u_C),

the following finite bounds hold:

    j^2>=kappa_C/epsilon(u),
    height(F)>=j>=sqrt(kappa_C/epsilon(u)),
    q=j/ell>=(n/s)j>=C sqrt(kappa_C/epsilon(u)),
    S_2(F)^2=2qj>=(C-2)/[20epsilon(u)].              (9)

Here height(F) is its maximum absolute INTEGER coefficient, including the full primitive normalization, not absolute Weil height.
These are lower bounds, not estimates making its coefficients cheap.

To verify all constants, epsilon<=1 and ell<=1/C give from(5)

    4j^2 D(u)>=exp(-2u)-2/C.

The condition u<=u_C ensures exp(-2u)>=(C+2)/(2C), so the last right side is at least(C-2)/(2C).
Finally D(u)<=5epsilon(u) by epsilon(u)>=u.
This proves the first bound in(9), and the others follow from j=qell and(2).
In particular, irrespective of whether ell stays bounded away from zero, every hypothetical sequence of such inputs with TOTAL m tending to zero has

    j -> infinity, height(F) -> infinity, q -> infinity.

Using the retained rate(4), the exact finite result implies

    j, height(F), q
      >=constant_C m^(-1/8)(1+log(1/m))^(-1/4)       (10)

for sufficiently small positive m.
Constants and thresholds depend only on the fixed C, not on the degree, coefficients, trace ideal or selected index.
This asserts a necessary rate for any hypothetical sequence; it constructs no such sequence.
The q estimate in(9) is quantitatively stronger than just requiring some original coefficient to be nonzero.

By L300's established degree-linear content result, sufficiently small m also forces delta_k=content(r_k)=1 and q=L_k, the actual positive additive order in Z^s/H_n Z^s.
Thus(9)--(10) are genuine lower bounds on that original INTEGER Gram order in this domain.
They do not imply that a particular rational prime dividing L_k grows: the same prime may contribute deeper powers, and no distribution assertion among its prime factors is made.

**Conditional uniform gap.** Fix C>2 and a real H>=1.
If a class of the actual inputs above has height(F)<=H for its actually selected primitive column at n=ceil(Cs), then the class has a positive total Mahler gap.
Explicitly choose u_* with

    0<u_*<=min(h_0,u_C), epsilon(u_*)<kappa_C/H^2.

Such a choice exists by(4).
No covered input can have m<=u_*/(C+1), since monotonicity and(9) would force j>H.
This complete implication requires neither bounded support nor bounded degree; its unproved coverage hypothesis is a uniform height bound for THIS selected primitive projection.
It does not assert that arbitrary bounded-height auxiliaries or bounded-height original inputs satisfy that hypothesis.

<a id="trace-ideal-metric-normalization"></a>
### 4. Consequence for the previously missing trace-ideal scale

Let a be the actual selected trace edge and nu=|Norm_+(a)|, as in L311/L313.
The raw projection-scale boundary determinant is governed by

    gamma=nu^(1/s)/q,
    |det(c_(b+i+j)/q)|^(2/d)=gamma^2.                (11)

This is the retained full-degree determinant, not a new determinant calculation.
Applying(9) gives the NEW small-total-measure upper estimate

    gamma^2<=nu^(2/s) epsilon(u)/(C^2 kappa_C).       (12)

It is conditional on the actual norm factor shown; it does not remove that expense.
In particular, if a hypothetical near-one sequence additionally satisfies nu^(1/s)<=K for a fixed K, then gamma->0 at this explicit rate.
This covers, conditionally, selected trace units nu=1, without claiming that such units occur on any actual near-one sequence.

Conversely, an attempted near-one mechanism requiring gamma>=gamma_0>0 must force

    nu^(1/s)>=gamma_0 C sqrt(kappa_C/epsilon(u)),
    log(nu)/s >=(1/2)log[1/epsilon(u)]
                          +log(gamma_0 C sqrt(kappa_C)).        (13)

Thus a bounded geometric mean of the trace-ideal norm cannot coexist with that proposed uniform normalized determinant payment in the small-m domain.
The entire trace quotient may have large or trivial lower invariant factors; (12)--(13) use its actual norm together with an independently forced metric scale.
No claim that small m bounds nu from above is supplied.

<a id="small-measure-pivot-failed-implication-and-costs"></a>
### 5. Preserved failed implication and full remaining costs

During this derivation, an initial intermediate analysis retained only L296's FIXED lower scalar margin.
Combined with integrality it suggested the weaker conditional alternative that a bounded pivot would force ell to shrink.
That alternative is superseded as a possible near-one scenario under the present hypotheses: equation(7) retains the EXACT margin -log(2ell)/2, and(8) then forces the pivot itself to grow.
No fixed mathematical statement or native output had been adopted when this correction was made.
The weaker inequalities remain true but fail to extract the full selected-column constraint.

The resulting height theorem is not a new unrestricted gap, and does not pay the original expenses.
At sufficiently small m, q=L and the exact identities remain

    Res(P,F)=L^d P(1)P(-1) Norm_+(u_k)^2,
    log|Res(P,F)|/d=log L+log Z_(2k)/d,
    log S_2(F)=log L+(1/2)log(2ell),
    v_p(F(alpha_i))=v_p(L)+v_p(alpha_i-alpha_i^-1)
                                      +v_p(u_k(tau_i)).        (14)

Every original local embedding, ramification and repeated reduction is retained.
L168 gives log Z_(2k)/d=o(1) on the actual degree-linear range2k<=2n<=(C+1)d, with its actual powered-degree and norm multiplicities.
The growing log L in(14) is therefore matched by the coefficient scale, and it is not new positive linear CYCLIC income.
The effective support rho remains fully charged by(7); its former lower bound has not become an upper bound.

All leading factors and all roots of F and its edge A remain part of M(F) and M(A).
Monomial removal changes only the actual degree charged in Tm/d; it leaves the coefficient height, S_1,S_2,rho, content and original resultant unchanged.
The edge evaluation A(alpha_i)=alpha_i^(n+s)a(tau_i), its complete norm nu^2 and all positive original evaluations are not replaced by nu^(1/s) alone.
No bound is given for future coefficients, complete signed coherence, full edge Mahler measure or the metric norms of the integral equivalences in L313.

The bounded contribution is therefore a uniform small-TOTAL-m divergence theorem for the actual selected primitive pivot, coefficient height and Gram scale; a complete conditional gap from a selected-height upper bound; and the explicit trace-norm/metric compatibility condition(12)--(13).
It isolates a concrete new coverage question: obtain a sufficiently strong height upper estimate for the ACTUAL selected column, or a different fully charged original-conjugate mechanism.
G0001 remains unresolved and its current execution is paused.
No new fixed-positive-measure control, mathematical program, J payload or source acquisition was used.


## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:15 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete actual selected edge/formal sequence](Yin_C_G0588_v1.md#statement) | Every original selected w, integral trace transform and B_a/P coefficient identity with no original-root cancellation; no reselection. |
| dependency | [Original anti/order/full costs](Yin_C_G0571_v1.md#statement) | Exact rational primitive scale, complete original norm/depth/energy, near-one delta1 and reused actual quadratic controls only. |
| dependency | [Integral coefficient pairing](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) | Actual unimodular remainder coefficient pairing, including discriminant/nonreduced primes, not a trace-pairing index assumption. |
| dependency | [Actual integral trace direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | O=B direct_sum alpha B with its genuine integer basis; no powered-degree extension is needed for the local quotient. |
| support | [Algebraic Lagrange coefficient identity](Yin_C_G0304_v1.md#canonical-trace-defect) | Only separable monic coefficient extraction identity; no no-neutral dynamics/decay transfer. |
| dependency | [Finite commutative-PID source scope](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | Existing finite Z-module classification/uniqueness with recorded SELF proof completions and cross-chapter limits; no new source proof reading. |
| dependency | [Complete original-root coefficient-energy estimate](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Entire small positive u explicit epsilon/monotonicity, actual original degree/multiplicities, full norm/rho/leading/radial expenses; Pri11/Dim19 accepted source limits unchanged. |
| dependency | [Actual powered-degree cost](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Existing degree-linear uniform cyclic cost and original multiplicities, only at its small-TOTAL-m scope. |
| support | [Original complete L311](../ledger/Yin_L_G0311_v1.md#complete-retained-proof-and-review) | Full determinant/module/energy proof and original author/source/R210 frozen input. |
| support | [Original complete L313](../ledger/Yin_L_G0313_v1.md#complete-retained-proof-and-review) | Full quotient/invariants/modular/coefficient-block proof and original author/source/R212 frozen input and known relationship. |
| support | [Original complete L315](../ledger/Yin_L_G0315_v1.md#complete-retained-proof-and-review) | Full pivot/height/scale/conditional-gap/metric proof, original weaker-inference history and author/R214 frozen input. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:18 |
| status | proved |
| reason | Adopt the entire actual selected-boundary object after actual whole SELF of the complete Statement and ALL THREE full original proof chains, preserving old R212 known independence at its original input and genuine historical unknowns separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete actual selected edge/formal sequence](Yin_C_G0588_v1.md#statement) | Every original selected w, integral trace transform and B_a/P coefficient identity with no original-root cancellation; no reselection. |
| dependency | [Original anti/order/full costs](Yin_C_G0571_v1.md#statement) | Exact rational primitive scale, complete original norm/depth/energy, near-one delta1 and reused actual quadratic controls only. |
| dependency | [Integral coefficient pairing](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) | Actual unimodular remainder coefficient pairing, including discriminant/nonreduced primes, not a trace-pairing index assumption. |
| dependency | [Actual integral trace direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | O=B direct_sum alpha B with its genuine integer basis; no powered-degree extension is needed for the local quotient. |
| support | [Algebraic Lagrange coefficient identity](Yin_C_G0304_v1.md#canonical-trace-defect) | Only separable monic coefficient extraction identity; no no-neutral dynamics/decay transfer. |
| dependency | [Finite commutative-PID source scope](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | Existing finite Z-module classification/uniqueness with recorded SELF proof completions and cross-chapter limits; no new source proof reading. |
| dependency | [Complete original-root coefficient-energy estimate](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Entire small positive u explicit epsilon/monotonicity, actual original degree/multiplicities, full norm/rho/leading/radial expenses; Pri11/Dim19 accepted source limits unchanged. |
| dependency | [Actual powered-degree cost](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Existing degree-linear uniform cyclic cost and original multiplicities, only at its small-TOTAL-m scope. |
| support | [Original complete L311](../ledger/Yin_L_G0311_v1.md#complete-retained-proof-and-review) | Full determinant/module/energy proof and original author/source/R210 frozen input. |
| support | [Original complete L313](../ledger/Yin_L_G0313_v1.md#complete-retained-proof-and-review) | Full quotient/invariants/modular/coefficient-block proof and original author/source/R212 frozen input and known relationship. |
| support | [Original complete L315](../ledger/Yin_L_G0315_v1.md#complete-retained-proof-and-review) | Full pivot/height/scale/conditional-gap/metric proof, original weaker-inference history and author/R214 frozen input. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0764_v1.md#whole-selected-modules-pivots-self) | Entire current Statement and all three complete arguments with every actual quantifier, primitive scale, integer/module/local/metric/conditional/source/negative limit; SELF only, no new isolated coverage or backfilled old input. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete actual selected edge/formal sequence](Yin_C_G0588_v1.md#statement) | Every original selected w, integral trace transform and B_a/P coefficient identity with no original-root cancellation; no reselection. |
| dependency | [Original anti/order/full costs](Yin_C_G0571_v1.md#statement) | Exact rational primitive scale, complete original norm/depth/energy, near-one delta1 and reused actual quadratic controls only. |
| dependency | [Integral coefficient pairing](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) | Actual unimodular remainder coefficient pairing, including discriminant/nonreduced primes, not a trace-pairing index assumption. |
| dependency | [Actual integral trace direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | O=B direct_sum alpha B with its genuine integer basis; no powered-degree extension is needed for the local quotient. |
| support | [Algebraic Lagrange coefficient identity](Yin_C_G0304_v1.md#canonical-trace-defect) | Only separable monic coefficient extraction identity; no no-neutral dynamics/decay transfer. |
| dependency | [Finite commutative-PID source scope](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | Existing finite Z-module classification/uniqueness with recorded SELF proof completions and cross-chapter limits; no new source proof reading. |
| dependency | [Complete original-root coefficient-energy estimate](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) | Entire small positive u explicit epsilon/monotonicity, actual original degree/multiplicities, full norm/rho/leading/radial expenses; Pri11/Dim19 accepted source limits unchanged. |
| dependency | [Actual powered-degree cost](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Existing degree-linear uniform cyclic cost and original multiplicities, only at its small-TOTAL-m scope. |
| support | [Original complete L311](../ledger/Yin_L_G0311_v1.md#complete-retained-proof-and-review) | Full determinant/module/energy proof and original author/source/R210 frozen input. |
| support | [Original complete L313](../ledger/Yin_L_G0313_v1.md#complete-retained-proof-and-review) | Full quotient/invariants/modular/coefficient-block proof and original author/source/R212 frozen input and known relationship. |
| support | [Original complete L315](../ledger/Yin_L_G0315_v1.md#complete-retained-proof-and-review) | Full pivot/height/scale/conditional-gap/metric proof, original weaker-inference history and author/R214 frozen input. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0785_v1.md#boundary-module-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R785. |

