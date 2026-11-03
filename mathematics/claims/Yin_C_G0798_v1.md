---
author: Yin
---

# Multiple neutral modes: exact steering, integral seeds and paid packet amplification

Human author Yin.
Root developed the complete higher-degree steering, source-seed and amplification arguments below after directly inspecting the CFMZ26 quartic method and its independent source finding.
This is a substantive local extension, not a conclusion attributed to the quartic source.
The exact source method and edition are retained in [CFMZ26-U002](../audits/literature/CFMZ26/Yin_U002.md#cfmz26-u002); its qualitative theorem is not a premise of the proof below.
No computation or independent review is claimed here.
The actual missing sequence of packets remains explicit.

## Statement

Let beta in (1,2) be any Salem number with monic irreducible polynomial P of degree d=2s+2, s>=1.
Its roots are beta,r=beta^(-1),zeta_1,conj(zeta_1),...,zeta_s,conj(zeta_s), with the zeta_j chosen in the open upper unit semicircle.
Use the original independent digit probabilities Pr(U=0)=1/2 and Pr(U=+1)=Pr(U=-1)=1/4, and put

    p_n=Pr(sum_(j=0)^(n-1) U_j beta^j=0), p_0=1,
    R=(lim_(n->infinity) p_n^(1/n))^(-1).

The limit exists and 1<R; no finite-core or critical-mean hypothesis is imposed.
All constants below may depend on the complete fixed P and s.
No constant is asserted uniform as P varies or beta decreases to1.

Set

    Omega={zeta_j:1<=j<=s}
          union {zeta_j zeta_k:1<=j,k<=s}
          union {zeta_j/zeta_k:j!=k},
    delta=min_(omega in Omega)|1-omega|>0,
    L=ceil(32s/delta)+1, K=16s^(3/2),
    D=diag(zeta_1,...,zeta_s), one=(1,...,1).

Every block of L consecutive integers contains an m with

    ||D^m z+one||_2<=K whenever ||z||_2<=K.                 (ST1)

The dependence on every frequency separation and on s is retained.

<a id="multiple-neutral-packet-definition"></a>
**Definition (localized packet with multiple neutral modes).**
Here is the complete packet convention used in the new assertion.
Let (Sy)_j=y_(j+1) and V(t)=-log(cos^2(pi t)) for |t|<1/2.
A packet for P with constants0<eta<1/4 and h>0 consists of real bilateral sequences Y,H, integer ell>=1 and a nonzero vector gamma in C^s such that

    kappa=P(S)Y is a nonzero integer-valued sequence,
    supp(kappa) subset {0,...,ell-1},
    Y_i=H_i+1_(i>=ell) 2Re sum_(j=1)^s gamma_j zeta_j^(i-ell),
    |H_i|<=1/2-2eta,
    |H_i|<=h r^dist(i,{0,...,ell-1}) outside the core.

Define

    Delta=2||gamma||_2>0,
    E=sum_(i in Z)V(H_i), Vcal=sum_(i in Z)|V'(H_i)|.

Both sums are finite.
For every epsilon>0 there exists at least one actual packet with0<Delta<epsilon, with some eta>0,h>0, and with an integral symmetric Laurent-polynomial source.
This existence does NOT bound its action, core length or boundary margin uniformly in epsilon.
In particular it does not provide the sequence needed below.

For any actual packet and integer N>2ell+d, put

    b_N=floor(N/L), a_N=floor((N-ell)/2),
    e_N=2h r^a_N/(1-r^N), u_N=K Delta+e_N,
    C_eta=2pi^2 csc^2(pi eta),
    C_N=E+u_N Vcal+C_eta N u_N^2,
    Theta_N=log b_N-C_N.

If b_N>=1 and u_N<eta, there is an explicit c(P,eta)>0 below, independent of M,N and the packet, such that every integer M>=2 admits an integer d+1<=n<2NM with

    log(beta^n p_n)>M Theta_N-log b_N
                  -(d+1)log M-(d+1)log N-d log2+log c(P,eta). (ST2)

If Theta_N>0, then

    log(beta/R)>=Theta_N/(2N)>0.                           (ST3)

Consequently a sequence of actual packets with COMMON eta,h, and

    Delta_k->0, Delta_k ell_k->0,
    E_k=o(log(1/Delta_k)),                                 (ST4)

implies R<beta for this fixed P.
No such sequence is supplied here for general s>=2.
The exact unresolved requirement is ST4 with its common boundary and tail constants; merely having arbitrarily small source amplitudes is insufficient.
No new strict higher-degree radius, critical mean, finite-time native certificate, degree-uniform entropy bound, total-Mahler gap or unrestricted G0001 conclusion is asserted.

## Complete argument

<a id="multiple-neutral-packet-argument"></a>
### MP1. The exact torus formula and original radius

Write P(X)=sum_(j=0)^d p_j X^j, p_0=p_d=1.
Let T on R^d/Z^d be the companion observation automorphism

    T(x_0,...,x_(d-1))=(x_1,...,x_(d-1),-sum_(j=0)^(d-1)p_j x_j).

Its determinant has absolute value1.
The first d character vectors v_j=(T^j)^transpose e_0 are the standard basis and satisfy the recurrence P.
For any integer polynomial A(X), division by monic P gives

    sum_j A_j v_j=0 iff P divides A iff A(beta)=0.

Thus Haar integration of the expansion

    cos^2(pi t)=(exp(2pi i t)+2+exp(-2pi i t))/4

gives exactly

    p_n=integral_(R^d/Z^d) product_(i=0)^(n-1) cos^2(pi y_i(x)) dx, (MP1)

where y_i is the canonical first coordinate in[-1/2,1/2).
There is no approximate collision or changed digit law.
Every real bilateral sequence in that range with integer P(S) forcing is the canonical observation sequence of its first d coordinates modulo Z^d: the recurrence holds modulo integers and T is invertible in both time directions.

Independent consecutive zero blocks give p_(n+m)>=p_n p_m.
Fekete's lemma yields the limit in the statement and identifies it with sup_n p_n^(1/n).
To see it is less than1, represent p_n as the collision probability of the fair-sign sum sum_(j<n) epsilon_j r^j, using half-differences and reversal.
Choose a fixed q with r^q<1/2 and condition on the signs outside positions0,q,2q,... .
Two different choices of the remaining signs have different sums: their first differing term has magnitude2r^(kq), greater than the sum of all possible later differences.
Every atom therefore has mass at most2^(-ceil(n/q)), and the collision sum is at most this maximum atom.
Hence R>=2^(1/q)>1.
Neither this source-dependent spacing nor ST3 is asserted uniform in beta.

### MP2. A simultaneous steering lemma with its full cost

Every frequency in Omega is different from1.
Indeed the zeta_j are distinct in the upper semicircle, none is1, and the product of two has argument strictly between0 and2pi.
For every starting integer m_0 and omega in Omega the geometric sum gives

    |L^(-1) sum_(m=m_0)^(m_0+L-1) omega^m|
          <=2/(L|1-omega|)<1/(16s).                       (MP2)

Fix z with t=||z||_2>0, and put f_m=Re sum_j z_j zeta_j^m.
Then |f_m|<=sqrt(s)t and MP2 implies

    |average f_m|<t/(16sqrt(s)),
    average f_m^2>=(1/2-1/16)t^2=7t^2/16.                (MP3)

For the second inequality expand f_m^2 as one half the real part of the square of the complex sum plus one half its squared modulus.
The diagonal constant contribution is t^2/2.
The remaining averages have total absolute value at most

    (1/(32s))[(sum|z_j|)^2+((sum|z_j|)^2-t^2)]
       <=t^2/16.

This accounts for both sum and difference frequencies and for the individual squares.
Set a=1/(16sqrt(s)).
If every f_m>=-a t, then

    (f_m+a t)(f_m-sqrt(s)t)<=0,
    f_m^2<=(sqrt(s)-a)t f_m+a sqrt(s)t^2.

Averaging and using MP3 would give average f_m^2<=t^2/8, a contradiction.
So some m has f_m<-t/(16sqrt(s)).
For that m,

    ||D^m z+one||_2^2=t^2+s+2f_m
                     <t^2+s-t/(8sqrt(s)).                (MP4)

The right-hand side is convex in t on[0,K]; its endpoint values are s and K^2-s because K=16s^(3/2).
Both are at most K^2.
The case t=0 gives norm sqrt(s)<=K directly.
This proves ST1 on every block, not only on a favorable initial block.

### MP3. Actual integral seeds in every fixed Salem degree

Reciprocity writes P(X)=X^(s+1)Q(X+X^(-1)) with Q monic integral of degree s+1.
Its roots are t_+=beta+r and t_j=zeta_j+conj(zeta_j), j1,...,s.
Q is irreducible: a proper factor would give a proper Laurent, hence polynomial, factor of P.
Equivalently [Q(beta):Q(t_+)]=2 and [Q(t_+):Q]=s+1, since beta satisfies X^2-t_+ X+1 and P has degree2s+2.
In particular a nonzero polynomial A of degree<=s vanishes at none of these trace roots.

For any prescribed epsilon_0>0, there is such a nonzero A in Z[X] with |A(t_j)|<epsilon_0 for all j1,...,s.
To prove it, evaluate all(N+1)^(s+1) coefficient vectors in{0,...,N}^(s+1) at the s neutral trace roots.
Their images lie in a box with each side O_P(N).
Partition it into half-open cubes of side epsilon_0.
There are O_(P,epsilon_0)((N+1)^s) cubes, fewer than coefficient vectors for large N.
The difference of two vectors in one cube is a nonzero A of degree<=s with the required strict inequalities.
No equality of neutral trace values or free choice of a Galois conjugate is used.

Set K_0(X)=A(X+X^(-1)), an integral symmetric Laurent polynomial, and C_lambda=1/P'(lambda).
All K_0(lambda) are nonzero.
Choose epsilon_0 small enough to make

    Delta=2(sum_j |C_(zeta_j)K_0(zeta_j)|^2)^(1/2)
          <min(epsilon,1/(100sqrt(s))).                   (MP5)

The trace sums sum_(P(lambda)=0)lambda^m/P'(lambda) equal0 for0<=m<d-1 and1 for m=d-1, by Lagrange interpolation.
The recurrence P with constant coefficient1 propagates their integrality to all integers m.
Expanding K_0 shows that sum_lambda C_lambda lambda^(i-1)K_0(lambda) is an integer for every integer i.
Also reciprocity gives

    P'(lambda^(-1))=-lambda^(2-d) P'(lambda).

Define

    xi_i=-C_beta beta^(i-1)K_0(beta),
    chi_i=2Re sum_j C_(zeta_j) zeta_j^(i-1)K_0(zeta_j).

The trace identity and reciprocity imply

    xi_i=xi_(d-i)+chi_i modulo Z.                         (MP6)

No xi_i belongs to Z+1/2.
If it did, it would be a rational half-integer and fixed by the embedding beta->zeta_1.
That image has modulus |C_(zeta_1)K_0(zeta_1)|<=Delta/2<1/2, impossible for a half-integer.
Set Y_i=can(xi_i).
It has integer P(S) forcing, since xi is homogeneous and Y-xi is integer-valued.
Choose an integer a<=0 sufficiently negative that h=|xi_a| satisfies h beta^(d-1)<1/100, and set b=d-a, ell=b-a+1.
Then Y_i=xi_i through i=a+d-1, so P(S)Y vanishes for i<a.
For i>b, MP6 and |chi_i|<=sqrt(s)Delta<1/100 give the canonical identity

    Y_i=xi_(d-i)+chi_i.

That sequence is homogeneous there, so the forcing also vanishes for i>b.
It cannot vanish everywhere: a homogeneous bilateral sequence decaying at negative infinity and bounded at positive infinity must be zero, by its distinct exponential modes; Y agrees with the nonzero xi on the left tail.
Thus its forcing is nonzero and supported in[a,b].

Define H_i=Y_i for i<=b and H_i=xi_(d-i) for i>b.
Both exterior tails have the exact bound h r^dist(i,[a,b]).
The finite core has a positive distance from the centering boundary because every xi_i avoids half-integers.
Together with the small tails this gives some eta in(0,1/4) with |H_i|<=1/2-2eta everywhere.
Shifting indices by a gives the packet convention in the statement; its gamma_j becomes C_(zeta_j)zeta_j^b K_0(zeta_j), preserving MP5.
The finite core and geometric tails give finite E and Vcal.
This proof supplies no control of these constants as epsilon_0 decreases, and no ST4 conclusion.

### MP4. Many genuine placements with bounded combined neutral waves

Fix a packet satisfying the hypotheses of ST2 and M>=2.
Choose starts0=tau_0<tau_1<...<tau_(M-1), with successive spacings in[N,2N-1].
Put psi_0=one and

    psi_j=D^(tau_j-tau_(j-1)) psi_(j-1)+one.

Partition the N allowed spacings into b_N complete disjoint blocks of L integers and a remainder.
ST1 supplies at least b_N admissible choices at every stage, keeping ||psi_j||_2<=K.
There are at least b_N^(M-1) admissible placement lists.

For each list set y_i=sum_j Y_(i-tau_j).
The emitted waves at any site come from a prefix ending at some j.
Their sum is

    2Re sum_l gamma_l zeta_l^(i-tau_j-ell) psi_(j,l),

whose absolute value is at most Delta K by Cauchy--Schwarz.
Assign each integer site to a nearest translated core.
Its distance from every other core is at least a_N, and successive further cores are separated by at least N.
Their combined localized tails are at most e_N.
Thus at a site assigned to core j,

    |y_i-H_(i-tau_j)|<=u_N<eta,
    |y_i|<1/2-eta.                                        (MP7)

The forcing is integral, so MP1 realizes this sequence as a canonical torus orbit.
For n=tau_(M-1)+ell+d one has d+1<=n<2NM.
On the interval of MP7, V''<=C_eta.
Taylor's theorem, the nonnegativity of V and the disjoint assignment of sites give

    sum_(i=0)^(n-1)V(y_i)
       <=M(E+u_N Vcal)+(C_eta/2)n u_N^2
       <=M C_N.                                          (MP8)

The forcing identifies the placement list uniquely.
For F=supp(kappa), gaps within a copy of F are at most ell-1, while gaps between different copies exceed ell.
Their supports are disjoint, so integer values do not cancel.
Cutting the total support at gaps larger than ell recovers its copies; subtract min F from each first position to recover the starts.
The observed forcing indices0,...,n-d-1 contain every copy, including its last coordinate.
At most(M-1)N+1<=MN values of n occur.
For some common n, at least b_N^(M-1)/(MN) distinct observed forcing words therefore occur.

### MP5. The full d-dimensional box and logarithmic comparison

Use the real mode matrix V_P whose rows at times0,...,d-1 are the values of

    beta^i, r^i, cos(i theta_1), sin(i theta_1),...,
                       cos(i theta_s), sin(i theta_s),

where zeta_j=exp(i theta_j).
It is invertible, since its modes are a nonsingular change of basis from the distinct complex Vandermonde modes.
Choose the fixed rho_box=eta/(16d).
Around each orbit center above add a homogeneous perturbation z_i with expanding coefficient bounded in absolute value by rho_box beta^(-(n-1))/n and each of the other d-1 coefficients by rho_box/n.
Then |z_i|<=d rho_box/n for0<=i<n.
The perturbed observations remain canonical and at distance at least eta/2 from the boundary.
There |V'|<=2pi cot(pi eta/2)<=4/eta, so their total action rises by at most4d rho_box/eta=1/4<1.

The initial-coordinate box has volume

    |det V_P|(2rho_box)^d beta^(-(n-1))n^(-d).

Its torus projection is injective because each coordinate difference is at most2d rho_box/n<1.
Homogeneous perturbation leaves every observed forcing coordinate unchanged.
Thus boxes for different observed forcing words are disjoint on the torus, including across a fundamental-cube boundary.
Integrating MP1 over the boxes and applying MP8 yields

    beta^n p_n >= c(P,eta)n^(-d)
                  [b_N^(M-1)/(MN)] exp(-M C_N),
    c(P,eta)=beta|det V_P|(2rho_box)^d exp(-1)>0.           (MP9)

Taking logarithms and using n<2NM proves ST2 with every volume and common-length loss retained.
If Theta_N>0, the right-hand side is positive for large M.
Moreover n>=(M-1)N+ell+d tends to infinity, while

    [log(beta^n p_n)]/n >=[M Theta_N-O_(P,N,packet)(log M)]/(2NM)

once its numerator is positive.
Its left side tends to log(beta/R) by MP1's Fekete limit.
Taking the limit gives ST3.
This is an original-law statement; the torus integral has not replaced its probability normalization.

### MP6. The exact sequence obligation

For common eta,h the derivative sum satisfies Vcal_k<=C_(P,eta,h)(ell_k+1).
The core terms are bounded by2pi cot(2pi eta); on either tail only a fixed number of sites precede h r^j<=1/4, and the remaining |V'(H_i)| are bounded by a fixed geometric series using V'(t)=O(t).
The same observations prove convergence of each E_k.

Assume ST4 and set N_k=ceil(Delta_k^(-1)).
Then ell_k/N_k->0, so N_k>2ell_k+d eventually.
Also a_(N_k)>=N_k/4-1 eventually and

    e_(N_k)/Delta_k
      <=2h N_k r^(N_k/4-1)/(1-r^(N_k))->0.

It follows that u_(N_k)=O_P(Delta_k),

    u_(N_k)Vcal_k->0, N_k u_(N_k)^2->0.

Eventually b_(N_k)>=N_k/(2L), so

    Theta_(N_k)>=log(1/Delta_k)-E_k-log(2L)-o(1)->infinity.

ST3 applies to a finite member of this sequence and gives R<beta.
MP3 alone does not supply common eta,h, Delta_k ell_k->0 or the action comparison.
No higher-degree analogue of the quartic controlled-return iteration is asserted by this proof.
In particular the s-dependent steering cost and the full d-dimensional box cannot be suppressed when comparing different polynomials or seeking a uniform Mahler gap.

## Current assessment
[Selected decision](#decision-multiple-neutral-packets-open)

## Assessment history

### Decision multiple-neutral-packets-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T13:11 |
| status | open |
| reason | Fix the complete local extension to any fixed Salem degree: simultaneous steering with all frequency and dimension costs, actual integral small-amplitude seeds, exact original torus formula, full multidimensional disjoint-box amplification and conditional packet-sequence strict-pressure criterion. Independent whole review remains outstanding. No general sequence with the required common margin, tail, length and action control is supplied, and neither a higher-degree strict radius nor a uniform Mahler gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete higher-degree statement](#statement) | Every fixed Salem beta in(1,2), full original law, exact steering constants and packet definitions, unconditional seed existence, finite amplification, quantitative conditional radius comparison and unresolved sequence boundary. |
| argument | [Complete MP1--MP6](#multiple-neutral-packet-argument) | Original character identity, all sum/difference-frequency moments, complete integral trace source and forcing support, admissible placements, disjoint d-dimensional volume, and exact limiting costs. |
| support | [Inspected quartic source method](../audits/literature/CFMZ26/Yin_U002.md#cfmz26-u002) | Explicit attribution and comparison for the torus/packet/mirror approach, especially Definitions3.2/4.2 and Proposition3.4/Corollary3.5; not a source theorem claiming this higher-degree extension and not a mathematical premise replacing any MP step. |
| support | [Original collision convention](Yin_C_G0405_v1.md#statement) | Established original-law p_n/R normalization for comparison; MP1 independently proves the exact facts used here without importing essential-radius or recurrence conclusions. |
