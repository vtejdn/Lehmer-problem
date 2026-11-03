---
author: Yin
---

# The exact matching character, a small-field Euler object, and its scalar-moment limit

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001/S_G0008 candidate written by assigned AI `entropy_status` for Yin.
Self-checked; complete noncontributor independent AI review and fixed-ledger adoption are recorded below.
The question is whether the matching observable of L162 has a smaller arithmetic realization than a whole-splitting-field class selector.
There is such an exact Euler object, but its scalar first moment does not by itself provide the required large-match prime.

Reuse [L66](Yin_L_G0066_v1.md#reciprocal-trace-domain), [L75](Yin_L_G0075_v1.md#chebotarev-period-cost), [L160](Yin_L_G0160_v1.md#inversion-matched-frobenius-return), [L161](Yin_L_G0161_v1.md#trace-factor-common-exponent), and [L162](Yin_L_G0162_v1.md#actual-inversion-matching-average).
No new prime scan, numerical calculation, analytic prime theorem, or uniform Mahler gap is claimed.

<a id="matching-induced-character"></a>
## 1. An exact induced-character identity

Let P be a monic irreducible reciprocal noncyclotomic integer polynomial of degree d=2s>=4 and constant coefficient one.
Let alpha be a root, K=Q(alpha), F=Q(alpha+alpha^(-1)), L the splitting field inside C, and G=Gal(L/Q).
L66 gives [K:F]=2 and [F:Q]=s.
Write J=Gal(L/F), J_0=Gal(L/K).
Then J_0 is normal of index two in J; let eta:J->{1,-1} be its nontrivial quotient character.

Let W=C[Omega] be the permutation representation on the d roots.
Inversion I(e_rho)=e_(rho^-1) commutes with G.
Its plus and minus eigenspaces W_+,W_- both have dimension s.
The plus basis consists of inverse-pair sums, so W_+ is the permutation representation on G/J.
The minus line for the pair {alpha,alpha^-1} has stabilizer J and J acts on it by eta; its G-translates are the other pair-difference lines.
Consequently, with characters denoted by chi,

    W_+=Ind_J^G 1,             W_-=Ind_J^G eta,
    chi_K=chi_++chi_-,         chi_F=chi_+,
    M(g):=#{rho:g(rho)=rho^-1}
         =Tr(I g|W)=chi_+(g)-chi_-(g)=2chi_F(g)-chi_K(g).   (1)

Here chi_K is the root permutation character.
In the trace formula, the diagonal entry indexed by rho is one exactly when (g(rho))^-1=rho.
This proves the normalization, with no missing factor of two: one flipped fixed pair contributes two to M.
The character chi_- has no invariant vector, since eta is nontrivial; equivalently a G-invariant vector of W is constant and lies in W_+.
Thus the trivial multiplicity in the virtual character M is one, as in L162's exact average.
M itself is not a genuine character: M(1)=0, while its average is one and it is not identically zero.

For an actual Salem input the signed representation has an additional rigidity.
By L162, V, the pair-action kernel, is full F_2^s or the even-weight subspace with odd s>=3.
On V, W_- is the sum of the s distinct, nontrivial coordinate characters v->(-1)^(v_i).
For full V this is immediate.
For even V, if i!=j choose a third index k and use v=e_i+e_k to separate coordinates i and j; the same vectors show nontriviality.
A V-invariant subspace of W_- is a sum of coordinate-character lines, and G permutes these lines transitively.
Therefore W_- is irreducible of degree s.             (2)

Also V acts trivially on W_+, so chi_- does not occur in chi_+.
If M=chi_A-chi_B for two genuine complex representations A,B, the chi_- multiplicity in B is one more than that in A.
Thus

    dim B>=s,                dim A=dim B>=s.                (3)

This concerns every genuine-character decomposition of this exact observable.
It does not exclude a different statistic, estimates using additional analytic cancellation, or another analytic object.
Rewriting the same M as a difference of genuine characters does not evade (3).
The dimension s may still be much smaller than the splitting-field degree.

<a id="matching-small-field-euler-product"></a>
## 2. A positive Euler product over the trace field

For Re(w)>1 define, by the absolutely convergent Dedekind products,

    Z_M(w)=zeta_F(w)^2/zeta_K(w).                            (4)

For each finite prime ideal q of F set x=(Norm q)^(-w).
There are exactly three relative quadratic possibilities.
The contribution of q to (4) is

    1                         if q splits in K/F;
    (1+x)/(1-x)               if q is inert in K/F;
    (1-x)^(-1)                if q ramifies in K/F.          (5)

Indeed the K-local factors are respectively (1-x)^(-2), (1-x^2)^(-1), and (1-x)^(-1), whereas the squared F factor is always (1-x)^(-2).
The inert logarithmic derivative contributes 2 log(Norm q) sum_(a>=1 odd) (Norm q)^(-a w); the ramified one contributes log(Norm q) sum_(a>=1) (Norm q)^(-a w).
All coefficients of -Z_M'/Z_M are consequently nonnegative.
This is a direct Euler calculation, including relative ramification; no analytic continuation or Artin holomorphy assumption is needed.

If p is unramified in L and g_p is a Frobenius element, permutation cycles on embeddings give the usual zeta local factors.
For every integer a>=1 the coefficient at the rational prime power p^a is

    Lambda_M(p^a)=M(g_p^a) log p.                            (6)

For example the first coefficient is twice log p times the number of degree-one F-primes over p inert in K/F.
Higher residue degrees and their odd lifts occur at p^a with their actual a; they are not degree-one rational-prime mass.
This agrees with L161's common-exponent condition.
No condition p not dividing disc(P) is needed for (6), only field unramifiedness as stated.

In standard Artin notation the known permutation-zeta and direct-sum identities identify

    L(w,chi_-)=zeta_K(w)/zeta_F(w),
    Z_M(w)=zeta_F(w)/L(w,chi_-),
    conductor(chi_-)=D_K/D_F,                               (7)

where D_E is the absolute field discriminant.
The induced eta is the relative quadratic character, so the first function can also be viewed as its quadratic Artin L-function over F.
Identifying it further with a Hecke character uses class field theory, which is not needed for (4)--(6) or the finite estimates below.

The identities and conductor convention in (7) are standard attributed facts, not new analytic results; their selected source scope is recorded in Section 5.
A signed total degree zero for M is not a conductor-free analytic estimate.
For the two genuine constituents chi_+,chi_-, the total degree is 2s=d and the product of conductors is D_F*(D_K/D_F)=D_K.
Alternatively (4) uses fields of degrees s and d directly.
The tower discriminant identity gives D_F^2<=D_K, and the fixed L75 estimate gives

    log D_K<=d log d+(2d-2)m,       m=log M(P).              (8)

These expressions use K and F directly, without requiring the normal-closure parameters [L:Q],D_L.
The degree and absolute discriminant are no larger and may be smaller; equality is allowed when K=L.
They do not supply a prime-error estimate or a large-match selector.

<a id="matching-finite-prime-error-transfer"></a>
## 3. Finite prime-power and ramification losses

Define Lambda_E(n) by -zeta_E'/zeta_E=sum Lambda_E(n)n^(-w), and psi_E(x)=sum_(n<=x) Lambda_E(n), for real x>=2.
Formula (5) shows

    Lambda_M=2Lambda_F-Lambda_K>=0,
    0<=Lambda_M(p^a)<=d log p,
    Psi_M(x):=sum_(n<=x)Lambda_M(n)=2psi_F(x)-psi_K(x).      (9)

For the upper bound, Lambda_F(p^a)=log p sum_(q|p,f_q|a) f_q is at most s log p because sum e_q f_q=s.
Subtracting the nonnegative Lambda_K proves (9), including rational ramification.

A rational prime is unramified in K exactly when it is unramified in its normal closure L.
One direction follows by passage to a subfield.
For the other, the completions of K at such a prime are unramified extensions of Q_p; every conjugate lies in the maximal unramified extension, and their finite compositum is unramified.
Thus both excluded-prime sets are precisely p|D_K.

Put

    S_M(x)=sum_(p<=x,p not dividing D_K) M(g_p) log p,
    R_K(x)=sum_(p<=x,p dividing D_K) log p,
    B_K(x)=d sqrt(x)log x+d R_K(x).

Then for every x>=2,

    0<=Psi_M(x)-S_M(x)<=B_K(x)
                           <=d sqrt(x)log x+d log D_K.     (10)

Indeed omitted prime powers have p<=sqrt(x); for each such p, their number times log p is at most log x.
There are at most sqrt(x) such primes.
The omitted first powers at ramified primes are bounded separately by d R_K(x).
This proves (10) without a prime-counting theorem and includes every omitted coefficient.

Consequently any actually established estimates |psi_F(x)-x|<=E_F(x), |psi_K(x)-x|<=E_K(x) would imply

    |S_M(x)-x|<=2E_F(x)+E_K(x)+B_K(x).                     (11)

The functions E_F,E_K are placeholders for additional proved analytic input, not estimates established by this candidate.
Keeping R_K rather than its crude discriminant bound is permitted.
A large upper estimate in (10) is not evidence of large actual ramification loss.
No ERH, unconditional error term, hidden degree-uniform constant or effective least-prime conclusion is introduced in (11).

<a id="matching-scalar-moment-stop"></a>
## 4. Why the scalar first moment does not select enough roots

Let theta_K(x)=sum_(p<=x,p not dividing D_K)log p and let Theta_A(x) be the same weighted sum restricted to M(g_p)>=s.
Since M is even and at most d, put b_s=2ceil(s/2)-2.
Separating the matching and nonmatching primes gives the exact finite test

    S_M(x)<=b_s theta_K(x)+(d-b_s)Theta_A(x),
    Theta_A(x)>=max(0,[S_M(x)-b_s theta_K(x)]/(d-b_s)).      (12)

For s>=3, b_s>=2.
A scalar first-moment estimate with main term S_M(x) approximately theta_K(x), even with negligible relative error, does not make the right side positive.
Specifically if S_M(x)<=[1+epsilon]theta_K(x), theta_K(x)>0 and epsilon<=b_s-1, that right side is zero.
For s=2, b_s=0 and positive first mass does detect A; that exceptional fixed degree is not an unbounded-degree near-one transfer.

There is an actual-group diagnostic showing the loss is not just poor constants in (12).
For any actual Salem input with s>=4, if V is full, it contains a vector v of weight one, with M(v)=2<s.
If V is even, s is odd and at least five; it contains a weight-two vector with M(v)=4<s.
Write a=M(v).
The probability measure assigning mass 1/a to v and 1-1/a to the identity has

    expected M=1,          measure{M>=s}=0.                 (13)

It can be averaged over G-conjugation to become a class-invariant measure with the same properties.
All its support elements belong to the actual G of the input.
This is a countermodel to an inference from the scalar matching mean alone, not a proposed Frobenius distribution, near-one family, or claim that actual useful primes do not exist.
It does not preserve all other character moments.
Joint information about chi_F and chi_K, higher correlations, or a direct many-matching prime theorem may distinguish it.

Stop the isolated scalar-first-moment transfer here.
The exact small-field object (4) is available for a new argument, but merely proving its expected first-order prime asymptotic does not fill L162's M(g_p)>=d/2 coverage at p<=B d log p.
A nontrivial new transfer must use more information than that scalar mean, and must retain the residue-degree, ramification, and exponent costs.
This limitation does not close the direct aggregate norm method.

## 5. Attribution, search, and contribution boundary

Local reuse inspected L66/L74/L75/L160--L162 and the CLOZ25 source screen before any external query.
The two exact bounded queries were:

1. `site.jmilne.org Artin L-functions induced representation Dedekind zeta permutation representation`
2. `site.math.mit.edu Artin L functions induction Dedekind zeta permutation character`

The sole selected attribution is John W. Jones and David P. Roberts, *Artin L-functions of small conductor*, Research in Number Theory 3, article 16 (2017), DOI 10.1007/s40993-017-0079-5.
The [publisher's open full text](https://link.springer.com/article/10.1007/s40993-017-0079-5) was read at Sections 2.2, 2.4 and 2.5, especially equation (2.3): permutation characters give the field zeta function and field discriminant as conductor; direct sums multiply L-functions and conductors.
This exactly supplies the known attribution in (7).
No analytic lower bound, later theorem, table or full source proof was adopted or audited.
This author downloaded no PDF.
Kedlaya's public course Chapter 22 was inspected as discovery background only, and is not a second selected proof dependency.

The assigned entropy_status AI derived the representation, Salem irreducibility, Euler factors, finite removal bound and scalar-moment limitation.
The coordinator selected the bounded research question and required the source and claim-scope checks, but did not supply a derivation in this source.
The sibling's relative inert-prime bound is a separate candidate and is not used here.
All mathematical assertions were self-checked before the complete independent review recorded below.


The coordinator subsequently retained and verified the fixed arXiv v1 artifact, compared the same Sections 2.2/2.4/2.5 and equation (2.3) on printed/PDF pp.3--4, and visually read both rendered pages.
[JR17's compact reading](../audits/literature/JR17/readme.md#jr17-matching-character-attribution) retains that standard-identity scope.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0063_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
