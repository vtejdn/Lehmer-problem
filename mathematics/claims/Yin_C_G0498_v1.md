---
author: Yin
---
# Complete collective-column Gaussian losses and actual separated-cut rank

All original seven sections/23equations, exact source/contribution/self-check/model and arithmetic boundaries remain retained.
L275 stays meaningful development and an original fixed review input; no research Task/E resumes.

The currently selected [whole independent finding R717](../audits/reviews/Yin_R_G0717_v1.md#collective-column-cut-rank-whole-independent-finding) was formed before the explicit old-review/source comparison and adopted by a later current decision; the earlier constructor whole SELF and original author/source/UNKNOWN records below retain their actual historical dates and scope.

## Statement

Put a0=log2 and, for EVERY A>=a0, define

    kappa(A)=min{sqrt(pi/A)*exp(-pi^2/a0),
                 exp(-25A/16)*(1-2^(-3/2))},
    gamma(A)=kappa(A)/32, K(A)=2+4A^2/gamma(A),
    c_a=1+2exp(-a),
    Psi_A(sigma)=log[c_A/c_(A+K(A)*gamma(A)*sigma^2)]/(2K(A)).

For EVERY integer b>=1, EVERY real unit upper triangular b-by-b C, EVERY x in R^b and exponents a_i in[a0,A], on the ENTIRE cube {-1,0,1}^b put

    D=C-I_b, y=x+D e,
    Z=sum_e exp[-sum_i a_i(e_i+y_i)^2],
    P_G(e)=exp[-sum_i a_i(e_i+y_i)^2]/Z,
    pi_a(e)=exp(-a*e^2)/c_a, Pi=product_i pi_(a_i),
    G=log[(product_i c_(a_i))/Z].

D has diagonal ZERO.
Choose p DISTINCT rows I and q DISTINCT columns J with p>=q>=1; I and J MAY intersect.
If M=D_(I,J) satisfies M^T M>=sigma^2 I_q with sigma>0, then for EVERY lambda>0

    G>=q*log[c_A/c_(A+lambda*sigma^2)]/
                           [K(A)+lambda/gamma(A)],
    Z<=product_i c_(a_i)*exp[-q*Psi_A(sigma)].

ALL other couplings, entry sizes, signs and translations are unrestricted.
The complete proof conditions independent DIGIT columns only under Pi, uses exact least squares, and charges the WHOLE relative-entropy and squared-center budgets ONCE.
It assumes neither independent center rows nor Gibbs/original returned digits.
Psi is continuous, positive and increasing for sigma>0, vanishes at0 and is at most log(c_A)/(2K(A)); overlapping choices cannot be added.

For the ACTUAL monic minimal polynomial P=sum_(j=0)^d p_j*t^j of ANY nonzero algebraic integer, d>=1, retain TOTAL m=log M(P), W=sum p_j^2 and ORIGINAL difference digits mu(0)=1/2,mu(+/-1)=1/4.
Let p_N=Pr(sum_(j=0)^(N-1)eta_j*alpha^j=0) and h2=lim_N[-log p_N]/N in natural units.
For1<=N<=d, p_N=2^-N.
For N>d, k=N-d, B_N has ALL N rows of P,tP,...,t^(k-1)P, U_(i,j)=p_(d+i-j), R is the ACTUAL Gram--Schmidt expansion and T=R U^-1.
The integral unit-upper substitution e=Uh bijects exactly the last k coefficient constraints with the retained cube; ONLY the first d inequalities are dropped, with ALL original weights/energy retained and a_i=(log2)*delta_(i+1), exp(2m)<=delta_j<=W.
For ANY disjoint consecutive blocks B having q_B selected columns, certified minimum column singular value sigma_B>0 of (T_B-I)_(I_B,J_B), and exponents bounded by A_B,

    p_N<=U_N*exp[-sum_B q_B*Psi_(A_B)(sigma_B)],
    U_N=2^-N*product_(j=1)^k(1+2^(1-delta_j))
       <=2^-d*exp[-(N-d)*g(m)],
    g(m)=log[2/(1+2^(1-exp(2m)))].

Every finite outside tail, degree boundary and block cost remains; no bounded original quotient or unit-only kernel premise is imposed on this nonunit word-law theorem.

For m>0 include ALL r exterior conjugates with multiplicities and both nonreal members.
Set N_+(z)=product_v(1-alpha_v*z), D_+(z)=product_v(1-conj(1/alpha_v)*z), H=D_+/N_+=sum h_ell*z^ell,h0=1 and a_infinity=(log2)*exp(2m).
For EVERY FIXED b>=2 and chosen finite geometry with q columns and limiting minimum column singular value sigma_infinity>0, EVERY A>a_infinity and0<epsilon<sigma_infinity admit an input-dependent all-future onset i0, independent of N, with EVERY N>d satisfying

    p_N<=2^-d*exp[-(N-d)*g(m)]*
         exp[-q*Psi_A(sigma_infinity-epsilon)*
                         max{0,floor((N-d-i0)/b)}].

First take N->infinity at FIXED input/geometry/parameters, only then A down to a_infinity and epsilon down to0, to obtain

    h2>=g(m)+(q/b)*Psi_(a_infinity)(sigma_infinity).

All onset, floor, degree, block length and column density costs remain.
Uniform near-one coverage by q/b>=c0>0 and sigma_infinity>=sigma0>0 is an OPEN extra hypothesis; IF it holds for all actual inputs0<m<=m0, fixed Astar>(log2)*exp(2m0) gives the conditional increment c0*Psi_(Astar)(sigma0/2)>0.
No uniform onset, simultaneous growing-b/N limit, free density, sum of overlapping gains or Mahler gap follows.

The complete rational Hadamard family q=4^v,v>=1, M_q=S_q/sqrt(q), C_q=[[I_q,M_q],[0,I_q]] has entries of magnitude q^-1/2 but M_q^T M_q=I_q and, for EVERY x and fixed a>=a0, Z_(C_q)(x)/c_a^(2q)<=exp[-q*Psi_a(1)] and G/(2q)>=Psi_a(1)/2>0.
It is NOT an asserted actual-polynomial realization.
For the repeated-column control tJ_q, t!=0, rank1 prevents the full-q-column condition when q>1, while at x0 the COMPLETE comparison law gives0<=G<=log(2q+1) despite its perfect matching.

For EVERY actual m>0 input the exact-degree-r constant-one N_+,D_+ have coprime strictly inside/outside zeros, INCLUDING multiplicities.
The proper reduced fraction

    A0=(H-1)/z=Q/N_+,
    Q=(D_+-N_+)/z!=0, deg Q<=r-1, gcd(Q,N_+)=1

gives for EVERY integer L>=1 the separated cross-matrix M_L=(h_(L+v-u))_(0<=u,v<L) of rank at most r, and EXACT rank r whenever L>=r.
The full recurrence/coprimality proof establishes a nonsingular leading r-by-r minor without simple-pole/residue assumptions or bounded infinite Hankel operators.
Therefore THIS separated-cut full-column certificate has q<=r and

    (q/(2L))*Psi_A(sigma)<=[r/(2L)]*log(c_A)/(2K(A)).

This bounds the displayed certificate, not actual G/h2/Mahler measure or all interlaced geometries.
Fixed actual finite-window matrices may initially have larger rank; for any fixed selection of more than r columns their minimum column singular value tends to0, so no positive all-future lower bound survives.

The ACTUAL irreducible dyadic golden radicals P_r=t^(2r)-t^r-1, r=2^v for integer v>=0, have actual d=2r and TOTAL m=log phi.
Their exact H=(1-phi^-1*z^r)/(1-phi*z^r) has h_(jr)=phi^(j-1) for j>=1 and zero other positive coefficients, so M_r=I_r and the certified increment is exactly(1/2)*Psi_((log2)*phi^2)(1), with no1/r rate factor.
This is an unpadded fixed-positive-measure control, not near-one coverage; the earlier density-one control has a different constant with no uncomputed ordering asserted.
The complete original source attribution/read depth, model-versus-arithmetic and finite-versus-infinite boundaries, contribution/self-check and all open geometric gates remain.

<a id="argument"></a>
## Complete original argument

The complete following author body is historical at its original date; its initial/pending/next-gate language supplies no current research authority.
Current mathematical/source-home hrefs preserve the same interfaces; L275/R174 retain their exact original inputs and dates.

## Joint inverse information beyond first-lag dominance

G0001 remains active and unresolved.

The author results below are a collective-column Gaussian loss, its complete original-law block transfer, a rational weak-entry control, and an exact limiting cut-rank discriminator for actual inputs.
They are initially self-reviewed only.
No independent review, fixed adoption, uniform near-one information floor or Task completion is asserted.

<a id="collective-column-reuse-and-scope"></a>
### 1. Reuse, scope and constants

Date: 2026-10-10.
The actual Task and current fixed strategy were read.
No new J, numerical run, external source acquisition, fixed-file edit or shared-navigation edit is needed.

The question is whether many weak inverse couplings can jointly lose mass without selecting one large entry in every row.
[L271](Yin_C_G0487_v1.md#statement) supplies a density-one theorem when selected pivots dominate their earlier selected-column contamination.
Its first-nonzero-lag increment is O(m^2) near one.
Its complete matching countercontrol shows that counting large entries with distinct row/column labels does not itself justify adding losses.
[L267](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) supplies dimension-independent bounds on the WHOLE finite Gaussian law.
These are the input for a different column-conditioning argument below.
[L268](Yin_C_G0475_v1.md#statement) supplies the actual rational inverse and compression context; no singular-value amplification there is automatically a cube probability bound.
[L264](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) keeps the direct/inverse distinction explicit.

A local screen for collective small-ball/entropy arguments also read the already retained L220/GK78 interface.
Its Hilbert small-ball theorem is not needed below.
The scalar completion of squares uses the accepted three-point maximum from L259/L267.
The finite Hankel-rank mechanism in Section6 is classical: the already audited [Par88-U001](../audits/literature/Par88/Yin_U001.md#par88-u001) records Theorem3.11, printed pp.37--38 / PDF pp.45--46, and the essential reduced-denominator/minimality guards.
That source unit was read here; the complete finite coefficient proof is reproduced below.
No fresh original-PDF inspection or general bounded-Hankel-operator theorem is claimed.
In particular the inverse used here has poles inside the disk.

The coordinator supplied the broad joint-amplitude question and assigned a separate rank-one analytic-model investigation to itself.
That ongoing draft was not read or used.
The collective-column inequality, its original-law assembly, the rational orthogonal control and the actual separated-cut specialization below are new deductions by structural_research for Yin, without a literature-priority claim.
Prior authorship/review roles on L263/L267/L271 remain those recorded there; they do not constitute an independent review of this material.

Put a_*=log2.
For A>=a_* reuse the explicit constants

    kappa(A)=min{sqrt(pi/A)exp(-pi^2/a_*),
                 exp(-25A/16)(1-2^(-3/2))},
    gamma(A)=kappa(A)/32,
    K(A)=2+4A^2/gamma(A),
    c_a=1+2exp(-a),
    F_a(w)=sum_(e=-1)^1 exp[-a(e+w)^2],
    pi_a(e)=exp(-a e^2)/c_a.                         (1)

All are real; gamma>0, K>0.
L259/L267 prove F_a(w)<=c_a for EVERY real w and EVERY a>=a_*, not only for a in a preselected bounded interval.
Their quantitative gamma/K estimates use the finite upper bound A.
Every logarithm is natural.

Let b>=1, C be any real unit upper triangular b-by-b matrix and x in R^b.
Write D=C-I_b, so D is strictly upper triangular.
For e in{-1,0,1}^b define

    y=x+D e,
    E(e)=sum_(i=0)^(b-1) a_i(e_i+y_i)^2,
    Z=sum_e exp[-E(e)],
    P_G(e)=exp[-E(e)]/Z,
    Pi(e)=product_i pi_(a_i)(e_i),
    G=log[(product_i c_(a_i))/Z],                    (2)

where a_*<=a_i<=A.
This finite P_G is an auxiliary normalized Gaussian cube law; Pi is an auxiliary product comparison law.
Neither is substituted for the original difference-digit law in Section3.

The exact retained L267 whole-law interface is

    G>=0,
    E_(P_G)||y||_2^2<=G/gamma(A),
    D(P_G||Pi)<=K(A)G.                              (3)

It holds for arbitrary C,x with no dimension or entry-size factor.
L267 obtains it from the full reverse entropy chain.
The actual reverse conditionals of P_G include the effect of earlier energy rows and need not equal individually normalized Gaussian factors.
We use (3), not such a conditional identification.

<a id="collective-column-gaussian-loss"></a>
### 2. A collective-column loss with arbitrary other couplings

Choose p distinct row indices I and q distinct column indices J, with p>=q>=1.
The sets I and J may intersect; within each set indices occur once.
Let

    M=D_(I,J),
    M^T M>=sigma^2 I_q,  sigma>0.                   (4)

There is no smallness, sign, diagonal-dominance or causal-order condition on any other entry of D.
For every lambda>0,

    G>= q log[c_A/c_(A+lambda sigma^2)] /
                        [K(A)+lambda/gamma(A)].     (5)

In particular define

    Psi_A(sigma)=log[c_A/c_(A+K(A)gamma(A)sigma^2)]
                                      /(2K(A)).     (6)

Then Z<=product_i c_(a_i) exp[-q Psi_A(sigma)].
The function Psi_A is continuous, positive for sigma>0, increasing in sigma, zero at0, and bounded above by log(c_A)/(2K(A)).
All these statements follow directly from (1) and (6).
No conclusion linear in sigma, or unbounded as sigma grows, is claimed.

Proof.
First, for a>=a_*, t>=0 and any w in R, completion of the scalar square gives

    E_(pi_a) exp[-t(e+w)^2]
       =exp[-a t w^2/(a+t)]
           F_(a+t)(t w/(a+t))/c_a
       <=c_(a+t)/c_a.                              (7)

The accepted scalar maximum applies because a+t>=a_*.
At t=0 this is an equality.
For fixed t>=0 the ratio c_(a+t)/c_a increases with a: with v=exp(-a), it is (1+2v exp(-t))/(1+2v), a decreasing function of v.
Therefore it is at most c_(A+t)/c_A when a<=A.

Condition Pi on all digits outside J.
The remaining f=e_J are independent with their original comparison factors pi_(a_j), and

    y_I=z+M f

for a completely arbitrary real z.
By (4), M has full column rank.
Decompose z=M w+z_perp with z_perp perpendicular to the range of M.
Then

    ||z+M f||_2^2=||M(f+w)||_2^2+||z_perp||_2^2
                    >=sigma^2 sum_(j in J)(f_j+w_j)^2.

Applying (7) independently to all q digits, with t=lambda sigma^2, proves the CONDITIONAL bound

    E_Pi(exp[-lambda||y_I||_2^2] | e_(J^c))
                       <=[c_(A+lambda sigma^2)/c_A]^q.

The right side is independent of all conditioned digits.
Thus exactly the same estimate holds unconditionally:

    E_Pi exp[-lambda||y_I||_2^2]
                       <=[c_(A+lambda sigma^2)/c_A]^q. (8)

There is no use of independence of the rows y_i.
Those rows can overlap arbitrarily in all digits.
Only the selected digit coordinates under the already established PRODUCT comparison law are conditioned independently.

For completeness the finite relative-entropy variational inequality used next follows by expanding D(P_G||Q)>=0, where Q is the normalized density exp[-lambda||y_I||^2]Pi.
It gives

    D(P_G||Pi)>=-lambda E_(P_G)||y_I||^2
                    -log E_Pi exp[-lambda||y_I||^2]
       >=q log[c_A/c_(A+lambda sigma^2)]
                                      -lambda G/gamma(A).

The last step uses DISTINCT rows, so their total squared displacement is at most the full total in (3).
Combine with D(P_G||Pi)<=K(A)G to obtain (5).
Choosing lambda=K(A)gamma(A) gives (6).

This pays the whole relative-entropy and energy budgets once.
It does not sum q separate applications of (3).
In contrast to the clean-event theorem, no earlier selected columns have to be deleted from row events.
Intersecting I and J causes no problem: D has diagonal0 and y_I is still exactly z+M f when the complement of J is fixed.

One may take the supremum in lambda in (5) for one chosen block, or choose the strongest certified submatrix.
Adding gains from overlapping choices is not justified by this theorem.
Below (6) is kept as a simple explicit certificate, so its limitations can be stated precisely.

<a id="collective-column-original-law"></a>
### 3. Complete original-law block transfer

Let P(t)=sum_(j=0)^d p_j t^j be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha, p_d=1, d>=1.
Put m=log M(P), W=sum_j p_j^2.
Preserve the original independent difference digits

    mu(0)=1/2, mu(+1)=mu(-1)=1/4,
    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0),
    h_2(alpha)=lim_(N->infinity) -log(p_N)/N.         (9)

The retained concatenation argument gives this limit.
For N<=d the exact value is p_N=2^(-N).
For N>d put k=N-d and let B_N have columns P,tP,...,t^(k-1)P in all N coefficient rows.
The exact word identity and its accepted digit-coordinate upper bound from L263/L267 are

    p_N=2^(-N) sum_(h in Z^k:||B_N h||_infinity<=1)
                                  exp[-(log2)||B_N h||_2^2]
       <=2^(-N) sum_(e in{-1,0,1}^k)
            exp[-sum_(i=0)^(k-1) a_i
                    (e_i+sum_(j>i) T_(i,j)e_j)^2],
    T=R U^(-1), U_(i,j)=p_(d+i-j),
    a_i=(log2)delta_(i+1), exp(2m)<=delta_j<=W.      (10)

Here R is the actual Gram--Schmidt expansion matrix of the shifts of P; U is integral unit upper triangular, and coefficients outside0,...,d are0.
The substitution e=Uh bijects the integer h allowed by the LAST k coefficient constraints with the entire three-point cube.
Only the FIRST d coefficient inequalities were dropped in (10).
All energy rows and original weights remain.
The original integer quotient need not be bounded.
This is a word-mass statement also for nonunits, not a claim that a unit-only state-kernel theorem extends to them.

Select pairwise disjoint consecutive blocks B inside{0,...,k-1}.
In each choose distinct local rows I_B and columns J_B, q_B=|J_B|>=1, and a certified bound

    ((T_B-I)_(I_B,J_B))^T ((T_B-I)_(I_B,J_B))
                                   >=sigma_B^2 I_(q_B),
    sigma_B>0, a_i<=A_B for all i in B.

Then

    p_N<=U_N exp[-sum_B q_B Psi_(A_B)(sigma_B)],
    U_N=2^(-N) product_(j=1)^k (1+2^(1-delta_j))
         <=2^(-d)exp[-(N-d)g(m)],
    g(m)=log[2/(1+2^(1-exp(2m)))].                  (11)

Proof.
Sum retained digits in increasing chronological order.
At a selected block all later digits are fixed, and their exact finite contributions give an arbitrary vector x in (2).
Apply Section2 uniformly in that vector.
Strict upper triangularity means that later squares are independent of already eliminated earlier digits.
At unselected indices use F_(a_i)<=c_(a_i).
Repeat through all chosen blocks.
Different blocks are disjoint, so no digit, row square or loss is charged twice.
All finite outside-tail assignments remain covered, and the original normalization2^(-N) never changes.

At worst A_B=W log2 is available.
All finite entries of T and all pivots are rational and computable from the actual polynomial; a rational lower bound on the smallest eigenvalue of M^T M is sufficient in (11).
Formula (11) itself contains every block length, every omitted early position, the degree boundary d and all original weights.
No experiment or automatic numerical certification is reported here.

<a id="collective-column-limiting-certificate"></a>
### 4. The actual limiting certificate and its paid density

Assume now m>0.
Let r count ALL exterior conjugates with multiplicity, including both members of every nonreal pair.
For the actual normalized Blaschke factor put

    s=exp(-m), Bcal(0)=s,
    H(z)=s/Bcal(z)=sum_(ell>=0) h_ell z^ell, h_0=1,
    a_infinity=(log2)exp(2m).

The exact accepted L263 limits are

    a_i->a_infinity,
    T_(i,i+ell)->h_ell for each fixed ell>=1.        (12)

All h_ell are real because the actual exterior multiset is invariant under conjugation.
Neutral roots remain in the accepted residual-closure input; they are not discarded from the original degree or law.

Fix b>=2.
Let D_infinity be the b-by-b strict upper matrix with entries h_(j-i) for i<j and0 otherwise.
Choose distinct I,J inside this block, q=|J|>=1, and suppose

    sigma_infinity:=inf_(||v||_2=1)
                      ||(D_infinity)_(I,J)v||_2>0. (13)

For every A>a_infinity and0<epsilon<sigma_infinity there is an all-future onset i_0=i_0(P,b,I,J,A,epsilon)>=0 such that every actual b-block beginning at i>=i_0 has all exponents<=A and the chosen submatrix has smallest column singular value at least sigma_infinity-epsilon.
Indeed (12) gives convergence of each of the finitely many required entries and exponents, uniformly after a maximum of their individual onsets.
The operator norm of their finite entry-error matrix tends to0.
The inequality ||(M+E)v||>=||Mv||-||E|| ||v|| then proves the asserted singular-value lower bound.
No uniform or effective input-independent onset is claimed.

Using blocks of length b beginning at i_0,i_0+b,... in (11) gives for EVERY N>d

    p_N<=2^(-d)exp[-(N-d)g(m)]
          *exp[-q Psi_A(sigma_infinity-epsilon)
                        max{0,floor((N-d-i_0)/b)}]. (14)

The maximum covers N-d<i_0.
For fixed chosen parameters first let N tend to infinity in (14), then let A decrease to a_infinity and epsilon decrease to0.
Continuity of (1),(6) gives

    h_2(alpha)>=g(m)+(q/b)Psi_(a_infinity)
                                      (sigma_infinity). (15)

This is a new conditional geometry interface.
It does not assert that every actual input has high-dimensional well-conditioned column submatrices.
A precise sufficient near-one gate would be: for every actual input in a range0<m<=m_0, some finite b,I,J satisfy q/b>=c_0>0 and sigma_infinity>=sigma_0>0, with c_0,sigma_0 independent of the input.
Taking any fixed A^*>(log2)exp(2m_0) in (14), with epsilon=sigma_0/2 interpreted as a permissible common singular-value slack, would give

    h_2(alpha)>=g(m)+c_0 Psi_(A^*)(sigma_0/2)>g(m).  (16)

The assertion of such geometric coverage is OPEN here.
Input-dependent onsets disappear only after the fixed-input infinite-time limit and are still fully paid in (14).
The finite b,d may grow with the input; the cost q/b cannot be suppressed.
Formula (16) is a conditional positive collision-rate increment, not an established Mahler gap.

For a single fixed input any finite chosen submatrix gives an admissible alternative bound in (15).
Taking a supremum over such alternatives is legitimate; summing overlapping choices is not.
L271's density-one dominance theorem remains valid and may be stronger on particular matrices.
Its first-lag amplitude comparison and L30's stronger one-expanding-root leading behavior near one are unchanged.

<a id="weak-entry-orthogonal-control"></a>
### 5. A rational weak-entry model and the repeated-column control

Here is a complete algebraic test of the changed hypothesis.
Construct integer matrices recursively by

    S_1=[1], S_(2n)=[[S_n,S_n],[S_n,-S_n]].

A block multiplication proves S_q^T S_q=q I_q for every q a power of2.
Restrict to q=4^v, v>=1, and put

    M_q=S_q/sqrt(q),
    C_q=[[I_q,M_q],[0,I_q]], b=2q.                 (17)

The entries of C_q are rational; every nonzero strict upper entry has absolute value1/sqrt(q), which tends to0.
Nevertheless M_q^T M_q=I_q.
For ANY outside shift x in R^(2q) and fixed exponent a>=log2, take I the first q rows and J the last q columns in Section2, with A=a and sigma=1.
Thus

    Z_(C_q)(x)/c_a^(2q)<=exp[-q Psi_a(1)],
    G_(C_q,x)/(2q)>=Psi_a(1)/2>0.                  (18)

The right side is independent of q.
This is a complete rational matrix family, not a sampled sphere calculation.
It proves that coefficients individually tending to0 can support an extensive Gaussian loss when their columns are collectively well-conditioned.
It does NOT realize C_q as the actual limiting matrix of an algebraic input, does not identify any Mahler measure for it, and does not assert the exact Gaussian partition or sharp constant.

For comparison, the earlier matching control C=[[I_q,t J_q],[0,I_q]], where J_q has every entry1 and t!=0, has q visibly nonzero matched entries but cross-matrix rank1.
Its columns cannot satisfy (4) with q>1.
At x=0 and common a>=log2, L271 proves G<=log(2q+1) from the event that the sum of the final q comparison digits is0.
Thus it is consistent with, and discriminates, the new theorem.
Large matching cardinality does not supply collective column independence.
Conversely a lower bound on each selected matrix entry is not required by (4), as (17) shows.
No probability loss has been counted by reusing the same full-law entropy budget q times.

<a id="actual-inverse-separated-cut-rank"></a>
### 6. Actual separated cuts have exact rank r, not their window length

The same condition has a precise actual-input limitation.
Write the exterior conjugates as alpha_1,...,alpha_r, with |alpha_v|>1, and define the actual polynomials

    N_+(z)=product_v(1-alpha_v z),
    D_+(z)=product_v(1-conj(1/alpha_v)z),
    H(z)=D_+(z)/N_+(z).

Both have exact degree r, constant coefficient1 and real coefficients.
They are coprime: zeros of N_+ are strictly inside and zeros of D_+ strictly outside the unit circle.
These are the same conventions as L268.
Put

    a_n=h_(n+1),
    A_0(z)=sum_(n>=0)a_n z^n
          =(H(z)-1)/z=Q(z)/N_+(z),
    Q(z)=(D_+(z)-N_+(z))/z.                         (19)

The degree of Q is at most r-1 and gcd(Q,N_+)=1.
Indeed a common divisor would divide D_+ and N_+ because N_+(0)=1; this contradicts their coprimality.
In particular Q is not0.
No cancellation to a smaller denominator is possible.
These statements include repeated exterior roots.

For a window L>=1, split a block of2L indices into its first L rows and final L columns.
Its limiting cross-matrix is

    M_L=(h_(L+v-u))_(0<=u,v<L).

Reversing row order turns it into the Hankel matrix (a_(u+v))_(0<=u,v<L).
The exact finite statement is

    rank M_L<=r for every L,
    rank M_L=r for every L>=r.                      (20)

Here and below finite rank is an ordinary matrix statement.
We do not assert that the infinite inverse Hankel matrix is a bounded operator; the inverse has genuine interior poles.

Proof of (20).
Write N_+(z)=1+n_1 z+...+n_r z^r.
The reduced proper fraction (19) gives

    a_n+n_1 a_(n-1)+...+n_r a_(n-r)=0 for n>=r.     (21)

For every Hankel column with index j>=r, (21) expresses it as a combination of the previous r columns, at ALL row indices.
This gives rank<=r (and rank<=L when L<r).

To prove the lower bound consider the leading r-by-r Hankel matrix.
If it were singular, there would be a nonzero vector v_0,...,v_(r-1) such that b_i=sum_(j=0)^(r-1)v_j a_(i+j)=0 for i=0,...,r-1.
Each shifted a-sequence satisfies the same recurrence in i for i>=r, so b_i=0 for all i>=0.
Let e be the largest index with v_e!=0 and set V(z)=sum_(j=0)^e v_j z^(e-j).
Every coefficient of V(z)A_0(z) at an index n>=e equals b_(n-e)=0.
Thus V A_0 is a polynomial of degree less than e (zero if e=0).
By coprimality in (19), N_+ divides V.
This is impossible because deg V<=e<r and V is nonzero.
The leading r-by-r minor is therefore nonsingular, and sits inside every L-by-L Hankel matrix with L>=r.
This proves (20) without assuming simple poles or nonzero individual residues.

The proof is the finite recurrence/minimal-denominator form of the classical mechanism recorded in Par88-U001; the present contribution is its application to the exact actual inverse cuts and the charged probability criterion, not a new general rank theorem.

Consequences for the certificate are precise.
For L>r the entire L-column cross-matrix cannot have a positive minimum column singular value.
More generally, among the final L columns, at most r can be independent when tested on ANY subset of the first L rows.
Therefore this separated-cut use of the explicit certificate (15), with b=2L, necessarily has

    q/(2L)<=r/(2L),
    (q/(2L))Psi_A(sigma)
                  <=[r/(2L)]log(c_A)/(2K(A)).        (22)

Equation (22) is an upper bound on THIS displayed certificate, not on the actual Gaussian loss, original h_2 or Mahler measure.
Actual finite Gram--Schmidt matrices need not have exactly this rank.
However their fixed-window matrices converge to M_L; for any fixed choice of more than r columns the minimum singular value tends to0.
Such a choice cannot retain a positive all-future lower bound sigma, even if an early finite matrix happens to have full rank.

As a complete actual control reuse the irreducible dyadic golden radicals from L231/L263/L268:

    P_r(t)=t^(2r)-t^r-1, r=2^v,
    phi=(1+sqrt5)/2, d=2r, m=log phi,
    H(z)=(1-phi^(-1)z^r)/(1-phi z^r),
    h_(jr)=phi^(j-1) for j>=1,
    h_ell=0 if r does not divide ell.               (23)

For L=r every index r+v-u lies between1 and2r-1, and its coefficient is nonzero exactly when u=v.
Thus M_r=I_r.
Formula (15) gives the exact certified increment (1/2)Psi_((log2)phi^2)(1), with no1/r factor.
L271 already provides a density-one control on this family; the two displayed constants differ and no numerical optimality comparison is asserted here.
This is not a newly solved small-measure family.
For every L>=r equation (20) still says the cross-rank remains r as L grows.
The degree grows in this ACTUAL unpadded family, but its Mahler measure stays fixed.
No near-one conclusion is inferred from it.

<a id="collective-column-selfcheck-and-next-gate"></a>
### 7. Self-check, retained boundaries and the next discriminator

The new mechanism uses independent DIGIT COLUMNS of the auxiliary product law after all other coordinates are fixed; it does not assert independent center rows.
The least-squares projection treats all outside shifts exactly.
All three-point sums in (7) are complete, including arbitrary real centers.
There are no deleted tails, exceptional outcomes, relaxed original probabilities or bounded original integer quotients.
Distinct row indices are essential to the single energy-budget payment in (5); full column conditioning supplies the q in its logarithm.
Rows and columns may overlap, and all intervening coefficients remain arbitrary.

The passage to actual inputs uses the full original weighted integer return identity and drops only its already identified first d coefficient inequalities.
Formula (11) is finite at every N>d with exact degree and disjoint-block costs.
Formula (14) has the complete all-future onset and floor, and uses limits only after a finite geometry has been fixed.
A parameter sequence with b or selected columns changing together with N requires additional proof; (15) does not authorize such an exchange.

The rational weak-entry model (17) and repeated-column control prove an actual distinction between collective column independence and entrywise amplitude/matching.
They are general finite matrix controls, not asserted realizations by minimal polynomials.
The rank statement (20), by contrast, concerns every actual positive-measure input with all exterior multiplicities and both members of conjugate pairs counted.
Its finite proof has no pole-residue, boundary analyticity or infinite-operator premise.
Its obstruction concerns a separated left/right cut and this full-column lower-singular-value certificate, not all interlaced arrangements or all collective information estimates.

The discriminating next question is whether actual inverse blocks have interlaced or suitably conditioned selected columns with q/b and their minimum column singular value simultaneously bounded away from0 in the near-one range, or whether a further exact structure forces degeneration even after interlacing.
A different continuation could retain lower integer coefficient constraints rather than seeking this sufficient geometric condition.
Neither is proved here.
A single well-conditioned direction is already covered by the theorem, but counting r exterior poles, a large operator norm or many matched entries cannot by itself establish (16).
This gives a specific useful gate and a complete obstruction to one tempting long separated-window design, while all research routes and the unrestricted Task remain active.

Self-checks completed in the author proof: the monotonic direction of the scalar ratio in (7); the least-squares inequality and intersecting row/column sets; signs in the variational bound; the one-time entropy/energy budget; chronological block direction and all finite outside shifts; the positive limiting singular-value onset; the finite rational recurrence and noncancellation proof; the whole-window versus selected-column rank scope; and the exact actual radical cross-matrix.
No program execution, numerical approximation or external proof audit is claimed.
A separately organized full noncontributor review is required before fixed adoption.

Author freeze: 2026-10-10T02:55.
Complete Sections1--7, equations(1)--(23), proof and limitations above are held for full noncontributor review.
The scoped material check passed before this final time/status paragraph; it is repeated on the frozen file.
No new mathematical program was used.
A pre-freeze prose comparison was tightened to avoid ranking the numerical constants of two different valid radical controls without a calculation.

### Actual whole checking and retained limits

The maintaining agent read the only complete L275 and ENTIRE R174, the sufficient C469 whole-law/shift, C445 scalar, C459 actual coordinate/limit, C475 inverse/compression, C461 direct-inverse, C487 clean/matching and C212 actual radical interfaces.
None contains the new whole collective-column or separated-cut proof; all seven original sections/23equations are retained completely.
Every scalar completion/ratio direction/selected-digit least-squares/variational sign/single entropy-energy charge, chronological original-weighted block assembly, exact onset/limit order/floor/q-over-b and both algebraic model controls were checked.
The entire reduced-denominator/noncancellation/recurrence/leading-minor proof includes all multiplicities and interior poles; the limitation is this specific separated-cut certificate.
The actual dyadic irreducibility/degree/root fibers/identity block/constant-total-measure proof was checked analytically.
Par88-U001v2 is sufficient and now records the two distinct original10/10 existing-U001v1 readings; no original PDF/proof was newly inspected and no source minute is borrowed from freeze or review.
Original U001v1 and old L/R inputs remain fixed.
R174's disclosed author summary/common context do not establish the precise additional mathematical contents before initial findings, so its ENTIRE original whole relationship remains UNKNOWN.
Upstream roles alone imply neither contribution nor isolation, and unread D143 is not a premise.
Original author whole SELF has day precision;10:55 freeze,11:11 old review and pre-freeze prose tightening to avoid an uncomputed constant ranking remain distinct.
No mathematical repair, source/PDF/proof reading, J/native run, parameter search or Task/E resumption occurred.
This current ENTIRE SELF does not close the old whole isolated-review obligation.

## Current assessment
[Selected decision](#decision-complete-current-independent-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:26 |
| status | open |
| reason | Register the complete original collective-column/full original-law/all-future limiting/actual cut-rank theorem, both model and radical controls, every density/onset/degree/source/contribution/negative qualification. Sufficient inputs are reused; actual whole finding and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire collective-column and cut theorem](#statement) | All arbitrary real matrices/shifts/exponents/selected digit geometries, complete original-law finite and fixed-input limiting certificates, both model controls, every actual reduced-denominator/multiplicity/rank/cut-density/radical/source/negative boundary. |
| argument | [Complete original argument](#argument) | Entire starting scope/Sections1--7/equations1--23/scalar-projection-entropy/full finite weighted law/onsets/floors/q-over-b/model and actual recurrence/coprimality/radical/contribution/self-check/negative scope. |
| dependency | [Whole finite Gaussian law](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) | Complete actual reverse-conditionals/total squared-center and WHOLE relative-entropy bounds, all dimensions/entries/shifts with exact gamma/K. |
| dependency | [Complete scalar maximum](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | F_a(w)<=c_a for EVERY a>=log2 and real w; finite A bounds only quantitative constants, not the shifted a+t maximum. |
| dependency | [Exact actual coordinates and limits](Yin_C_G0459_v1.md#argument) | Complete original word mass/monic integral quotient/e=Uh/T=RU^-1/all fixed-lag and pivot limits including unit-circle residual closure, no uniform rate. |
| support | [Actual inverse/compression comparison](Yin_C_G0475_v1.md#argument) | Full actual exterior N-D conventions/minimality/interior poles and prior finite compression, no borrowed probability conclusion. |
| support | [Direct versus inverse](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Exact formal inverse/noncancellation/interior poles/root multiplicities, no inverse-l2 or bounded infinite operator premise. |
| support | [Clean and matching comparison](Yin_C_G0487_v1.md#argument) | Complete earlier dominance/density-one and repeated-center matching control, keeping distinct constants unranked. |
| dependency | [Actual golden radicals](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one square-tower irreducibility/actual degree2r/root fibers/fixed total measure, no padding or near-one coverage. |
| support | [Classical finite-rank source](../audits/literature/Par88/Yin_U001.md#par88-u001) | Theorem3.11 printed37--38/PDF45--46/reduced denominator and multiplicities; exact original10/10 author/reviewer existing-U1v1 occurrences are retained at the same unit's original-collective-column-reuse-20261010 anchor. Present proof is complete finite algebra, no bounded inverse-Hankel or new PDF/proof reading. |
| support | [Original small-ball comparison](../ledger/Yin_L_G0220_v1.md#stationary-neutral-concentration-cost) | Original retained GK78/Hilbert screen only; its small-ball theorem is NOT a premise here. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:31 |
| status | proved |
| reason | Adopt after the actual ENTIRE whole SELF of all seven original sections/23equations: collective-column one-budget loss, complete original weighted finite law, fixed-input onset-floor-density limit, both models and exact actual reduced-denominator cut rank/radical controls, with every source/contribution/negative boundary. Original R174 WHOLE UNKNOWN and original author/source/freeze/review precision remain; no isolated replacement or research resumption is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire collective-column and cut theorem](#statement) | All arbitrary real matrices/shifts/exponents/selected digit geometries, complete original-law finite and fixed-input limiting certificates, both model controls, every actual reduced-denominator/multiplicity/rank/cut-density/radical/source/negative boundary. |
| argument | [Complete original argument](#argument) | Entire starting scope/Sections1--7/equations1--23/scalar-projection-entropy/full finite weighted law/onsets/floors/q-over-b/model and actual recurrence/coprimality/radical/contribution/self-check/negative scope. |
| dependency | [Whole finite Gaussian law](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) | Complete actual reverse-conditionals/total squared-center and WHOLE relative-entropy bounds, all dimensions/entries/shifts with exact gamma/K. |
| dependency | [Complete scalar maximum](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | F_a(w)<=c_a for EVERY a>=log2 and real w; finite A bounds only quantitative constants, not the shifted a+t maximum. |
| dependency | [Exact actual coordinates and limits](Yin_C_G0459_v1.md#argument) | Complete original word mass/monic integral quotient/e=Uh/T=RU^-1/all fixed-lag and pivot limits including unit-circle residual closure, no uniform rate. |
| support | [Actual inverse/compression comparison](Yin_C_G0475_v1.md#argument) | Full actual exterior N-D conventions/minimality/interior poles and prior finite compression, no borrowed probability conclusion. |
| support | [Direct versus inverse](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Exact formal inverse/noncancellation/interior poles/root multiplicities, no inverse-l2 or bounded infinite operator premise. |
| support | [Clean and matching comparison](Yin_C_G0487_v1.md#argument) | Complete earlier dominance/density-one and repeated-center matching control, keeping distinct constants unranked. |
| dependency | [Actual golden radicals](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one square-tower irreducibility/actual degree2r/root fibers/fixed total measure, no padding or near-one coverage. |
| support | [Classical finite-rank source](../audits/literature/Par88/Yin_U001.md#par88-u001) | Theorem3.11 printed37--38/PDF45--46/reduced denominator and multiplicities; exact original10/10 author/reviewer existing-U1v1 occurrences are retained at the same unit's original-collective-column-reuse-20261010 anchor. Present proof is complete finite algebra, no bounded inverse-Hankel or new PDF/proof reading. |
| support | [Original small-ball comparison](../ledger/Yin_L_G0220_v1.md#stationary-neutral-concentration-cost) | Original retained GK78/Hilbert screen only; its small-ball theorem is NOT a premise here. |
| review | [Entire current whole SELF](../audits/reviews/Yin_R_G0709_v1.md#collective-column-whole-self-finding) | ENTIRE exact Statement and complete starting/reuse/Sections1--7/equations1--23/scalar-least-squares-entropy/full original-law/onset-floor-q-over-b/finite-infinite/model/reduced proper fraction/leading-minor/multiplicity/cut/radical/source/contribution/negative scope, explicitly SELF. |


### Decision complete-current-independent-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T03:03 |
| status | proved |
| reason | Adopt the actual separate whole independent inspection of all seven sections and every actual analytic/model/arithmetic limit, first formed10:34 before explicit old-review/source comparison10:47 and publication10:58. R174 original whole UNKNOWN, day-precision author SELF, current09:29 SELF/09:31 adoption and all old source/freeze/review facts remain distinct; there was no mechanism repair or independently identified proof gap. This decision changes only the selected review, with all other state and exact relations/scopes unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All arbitrary real matrices/shifts/exponents/selected digit geometries, complete original-law finite and fixed-input limiting certificates, both model controls, every actual reduced-denominator/multiplicity/rank/cut-density/radical/source/negative boundary. |
| argument | [Exact argument](#argument) | Entire starting scope/Sections1--7/equations1--23/scalar-projection-entropy/full finite weighted law/onsets/floors/q-over-b/model and actual recurrence/coprimality/radical/contribution/self-check/negative scope. |
| dependency | [Exact dependency](Yin_C_G0469_v1.md#finite-block-entropy-loss-identity) | Complete actual reverse-conditionals/total squared-center and WHOLE relative-entropy bounds, all dimensions/entries/shifts with exact gamma/K. |
| dependency | [Exact dependency](Yin_C_G0445_v1.md#quantitative-three-point-center-loss) | F_a(w)<=c_a for EVERY a>=log2 and real w; finite A bounds only quantitative constants, not the shifted a+t maximum. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#argument) | Complete original word mass/monic integral quotient/e=Uh/T=RU^-1/all fixed-lag and pivot limits including unit-circle residual closure, no uniform rate. |
| support | [Exact support](Yin_C_G0475_v1.md#argument) | Full actual exterior N-D conventions/minimality/interior poles and prior finite compression, no borrowed probability conclusion. |
| support | [Exact support](Yin_C_G0461_v1.md#direct-inverse-coefficient-separation) | Exact formal inverse/noncancellation/interior poles/root multiplicities, no inverse-l2 or bounded infinite operator premise. |
| support | [Exact support](Yin_C_G0487_v1.md#argument) | Complete earlier dominance/density-one and repeated-center matching control, keeping distinct constants unranked. |
| dependency | [Exact dependency](Yin_C_G0212_v1.md#radical-collision-control) | Complete norm-minus-one square-tower irreducibility/actual degree2r/root fibers/fixed total measure, no padding or near-one coverage. |
| support | [Exact support](../audits/literature/Par88/Yin_U001.md#par88-u001) | Theorem3.11 printed37--38/PDF45--46/reduced denominator and multiplicities; exact original10/10 author/reviewer existing-U1v1 occurrences are retained at the same unit's original-collective-column-reuse-20261010 anchor. Present proof is complete finite algebra, no bounded inverse-Hankel or new PDF/proof reading. |
| support | [Exact support](../ledger/Yin_L_G0220_v1.md#stationary-neutral-concentration-cost) | Original retained GK78/Hilbert screen only; its small-ball theorem is NOT a premise here. |
| review | [Exact review](../audits/reviews/Yin_R_G0717_v1.md#collective-column-cut-rank-whole-independent-finding) | Entire current Statement and complete #argument, all original seven sections/23equations, full weighted law and fixed-input limiting quantifiers, both model controls, actual reduced-denominator leading-minor/cut/radical proof, every old positive/negative/source/contribution boundary, and the fixed-input limits declared by the new whole independent finding. |
