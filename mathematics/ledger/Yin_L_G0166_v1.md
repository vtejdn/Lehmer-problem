---
author: Yin
---

# An explicit conditional joint-moment prime bound on the regular trace domain

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001/S_G0008 result by assigned AI `growth_arithmetic_status` for Yin.
This AI selected and inspected the explicit analytic statement and derived the full constant and cost comparison below.
The coordinator supplied the finite joint transfer, whose complete proof and group-domain classification belong to the companion [L G0165](Yin_L_G0165_v1.md#regular-joint-finite-prime-budget), written by `entropy_status` with the coordinator's contribution.
That fixed result is used here only at its stated interface; it is not newly proved in this record.
Complete noncontributor independent AI review and fixed adoption are recorded below.
No prime scan or numerical mathematics run occurred.

The fixed interfaces are [L164](Yin_L_G0164_v1.md#matching-finite-prime-error-transfer) for the matching character and prime-power accounting, [L162](Yin_L_G0162_v1.md#matching-union-local-cost) for original-degree local norm mass and small-prime lifts, and [L75](Yin_L_G0075_v1.md#chebotarev-period-cost) for the original-field discriminant bound.
The new external source is used only as an explicit conditional statement and application; its analytic proof and constant-verification programs are not audited.

<a id="explicit-dedekind-error-input"></a>
## 1. The selected analytic statement and its exact domain

For a number field E, put n_E=[E:Q], D_E=|disc(E)|, and let psi_E(x) include all prime-ideal powers of absolute norm at most x, with the usual log Norm(q) weights.
The selected Grenie--Molteni Corollary 1.2, equation (1.5), states under GRH for zeta_E that, for every real x>=100,

    |psi_E(x)-x|<=E_E(x),
    E_E(x)=sqrt(x)[A(x)log D_E+B(x)n_E],
    A(x)=log x/(2pi)+2,
    B(x)=(log x)^2/(8pi)+2.                               (1)

The selected accepted statement is [GM16-U001](../audits/literature/GM16/Yin_U001.md#gm16-u001), bound to the retained arXiv:1312.4463v4 manuscript dated 17 September 2015.
The coordinator read pp.1--3 and visually checked pp.2--3, confirming (1) with exactly the displayed constants and range in Corollary 1.2/(1.5), printed/PDF p.3.
This is a conditional statement/application inspection, not an analytic-proof or constant-program audit.
The author's earlier version-2 reading is separately preserved in Section 6.

The work is Loic Grenie and Giuseppe Molteni, *Explicit versions of the prime ideal theorem for Dedekind zeta functions under GRH*, Mathematics of Computation 85 (298), 2016, 889--906, [DOI 10.1090/mcom3031](https://doi.org/10.1090/mcom3031).
The inspected v2 is available from the [authors' institutional repository](https://aisberg.unibg.it/retrieve/handle/10446/58029/79537/131216-Grenie-v2.pdf).
Section 6 records exact search and inspection scope.

<a id="regular-trace-joint-error-gate"></a>
## 2. The finite joint interface to which (1) is applied

Let P be an actual irreducible Salem polynomial of degree d=2s>=4, K=Q(alpha), F=Q(alpha+alpha^(-1)), and L its splitting field.
Let H be its action on inverse pairs and V the kernel, as in L162.
Assume H is regular, equivalently that the degree-s trace field F is Galois over Q.
Write M(g) for the number of roots matched with their inverses and put A_set={g:M(g)>=s}.

The companion joint theorem distinguishes this domain from a nonregular H.
Only its regular-domain finite interface is used below.
Its exact outside-selector threshold is

    b=2ceil(s/2)-2                  if V=F_2^s;
    b=4floor((s-1)/4)               if V is even-weight.

The second case has odd s.
Define c=1-b/s and a=1+c=2-b/s.
These exact formulas give

    1/s<=c<=3/s,        0<c<=1,        1<a<=2,
    hence 2/d<=c<=6/d.                                    (2)

For full V, c is 2/s when s is even and 1/s when s is odd.
For even V, c is 1/s or 3/s according as s is 1 or 3 modulo 4.
The low cases s=2 and s=3 are included; in particular c may equal one.
No asymptotic substitution for these constants is used.

Let S_F(x), S_K(x) denote the rational prime sums of their permutation characters, both restricted to p<=x and p not dividing D_K, with weight log p.
Let Theta_A(x) be the same log-prime sum restricted further to Frobenius in A_set.
Put

    R_K(x)=sum_(p<=x,p|D_K)log p,
    B_F(x)=s sqrt(x)log x+s R_K(x).

The companion finite theorem supplies the following exact transfer whenever |psi_F(x)-x|<=E_F(x) and |psi_K(x)-x|<=E_K(x):

    (d-b)Theta_A(x)>=a S_F(x)-S_K(x)
       >=c x-a E_F(x)-E_K(x)-a B_F(x).                    (3)

Its one-sided removal of prime powers and ramified primes is important: the omitted K contribution is nonnegative and can be dropped.
No second K removal budget is added.
The common rational unramified set is exactly p not dividing D_K, as proved in L164.

Assuming GRH separately for zeta_F and zeta_K, (1) applies to both fields with degrees s and d.
No GRH for a whole splitting field, Artin holomorphy assumption, or unproved cancellation of their error terms is used.
The concrete sufficient gate is

    c x>a E_F(x)+E_K(x)+a B_F(x),       x>=100.             (4)

If (4) holds, Theta_A(x)>0 and there is a rational prime p<=x, unramified in K and L, with M(g_p)>=d/2.

<a id="literal-joint-error-cost"></a>
## 3. A necessary cost for this particular sufficient gate

All terms in (1) are nonnegative.
In particular

    E_K(x)>=d sqrt(x)(log x)^2/(8pi).

Therefore (4), with exactly the displayed analytic upper bounds and removal budget, can hold only if

    sqrt(x)>d(log x)^2/(8pi c)
             >=d^2(log x)^2/(48pi),
    equivalently x>d^4(log x)^4/(2304pi^2).                (5)

For every fixed C>0, the choice x=C d log d fails (5) for all sufficiently large d.
More generally the recipe cannot have degree scale smaller than order d^4(log d)^4 asymptotically.
For this last assertion, x>=100 in (5) first implies x>=C_0 d^4 for an absolute C_0>0; hence log x>=4log d+log C_0.
Substitution back into (5) gives the stated order as d tends to infinity.

This is a restriction on successfully verifying (4) with these particular sufficient upper bounds.
It is not a lower bound on the least actual prime in A_set, the actual analytic error, or the performance of every possible prime theorem.
No lower bound on D_K is needed for this screen: the degree term alone suffices.

<a id="explicit-regular-trace-prime-recipe"></a>
## 4. A completely explicit sufficient prime range

Fix m_0>=0 and restrict to inputs with m=log M(P)<=m_0.
Set

    u=1+m_0,       lambda=log(2d),
    X=2^20 u^4 d^4 lambda^4,
    sqrt(X)=1024 u^2 d^2 lambda^2.                        (6)

Then under the two GRH assumptions, (4) holds at x=X.
In particular a matching prime p<=X exists on the stated regular trace domain.
Here is a full conservative constant verification.

Since d>=4, lambda>=log 8>2, u>=1, and X>=100.
The tower discriminant inequality from L164 and the L75 height bound give

    2log D_F<=log D_K=:D,
    D<=d log d+(2d-2)m_0<=u d lambda.                     (7)

Let tau=log X.
Then

    tau=20log2+4log u+4log d+4log lambda
       <=[20/3+2(u-1)+4+4]lambda
       <=15u lambda.                                     (8)

The first inequality uses lambda>=3log2, log u<=u-1, lambda>2, log d<=lambda, and log lambda<=lambda.
Thus at X,

    A(X)<=tau+2<=16u lambda,
    B(X)<=tau^2+2<=226u^2 lambda^2.                       (9)

Using [F:Q]=d/2, (7), a<=2, and (1),

    a E_F(X)+E_K(X)
      <=(1+a/2)sqrt(X)[A(X)D+B(X)d]
      <=484u^2 d sqrt(X)lambda^2.                        (10)

For the removal term, R_K(X)<=D and 2s=d give

    a B_F(X)<=d sqrt(X)tau+dD
       <=15u d sqrt(X)lambda+u d^2 lambda
       <=9u^2 d sqrt(X)lambda^2.                         (11)

Indeed the first summand is at most 8u^2 d sqrt(X)lambda^2 because lambda>2 and u>=1.
The second is at most u^2 d sqrt(X)lambda^2 by (6).
This explicitly includes rational ramification and higher prime powers.

On the other hand (2) and (6) imply

    cX>=2X/d=2048u^2 d sqrt(X)lambda^2
       >493u^2 d sqrt(X)lambda^2
       >=a E_F(X)+E_K(X)+a B_F(X).                       (12)

This proves (4) strictly.
No numerical parameter optimization or unreported large-degree threshold enters (6)--(12).

<a id="regular-prime-common-exponent-cost"></a>
## 5. What the selected prime gives for the actual norm

The selected prime p<=X has at least d/2 matched original roots.
L162 therefore gives, with actual original-field norms,

    v_p(C_((p+1)p^r))>=(r+1)d/2       for integers r>=0.

For p=2 take r=2 and n=12; for p=3 take r=1 and n=12.
Their respective certificates are m>=log2/6 and m>=log(3/2)/3, using d>=4.
For p>=5 take n=p+1 and put

    a_0=1/2-log2/log5>0.

Since log t/t decreases for t>=5 and p+1<=6p/5,

    m>=a_0 d log p/(p+1)
       >=(5a_0/6)d log p/p
       >=(5a_0/6)d log X/X.                              (13)

Thus one explicit conditional degree-dependent consequence is

    m>=min{log2/6,log(3/2)/3,(5a_0/6)d log X/X}.           (14)

For fixed m_0, the last term has order d^(-3)(log d)^(-3), rather than a degree-independent lower bound.
The common return exponent is at most X+1, with the small-prime choices n=12 already included because X>=100.
Equivalently for p>=5, p/(d log p)<=X/(d log X); this direction follows from monotonicity of t/log t above e.
No such monotonicity was used across the interval from 2 to e.

The result is a positive restricted conditional many-matching-prime coverage theorem using only the fields F and K in its analytic input.
It avoids the exponential actual Salem splitting degree, but does not meet L162's degree-uniform prime budget.
It is not claimed to improve existing general degree-dependent Mahler bounds.
Nonregular trace groups and the unrestricted reciprocal near-one core remain outside this conclusion.
The companion joint theorem owns the nonregular first-moment limitation; this source does not assert that other statistics or actual prime coverage fail there.

<a id="grenie-source-inspection"></a>
## 6. Bounded source inspection and review boundary

The sole exact public query was:

`Grenie Molteni explicit Chebyshev function number fields GRH 2016 psi error theorem arxiv`

The primary institutional [publication metadata](https://expertise.unimi.it/resource/item/498547?language=en-US) identifies the journal, year, volume, issue, pages and DOI above.
The [repository record](https://aisberg.unibg.it/handle/10446/58029) distinguishes the open postprint from a restricted publisher PDF.
The author read the open v2's identity and definitions on p.1, the GRH conventions and Theorem 1.1 on p.2 for orientation, and all of Corollary 1.2/(1.5) on p.3.
Adjacent Corollary 1.3 was visible but is not selected or used.
No part of the analytic proof or the source's constant-verification programs was audited.

The attempted arXiv v2 abstract and PDF openings returned web DisabledError.
A web screenshot of the institutional title page returned HTTP403; the author claims no visual-page inspection or artifact acquisition.
The original statement inspection was from the primary PDF's extracted text.
The coordinator separately acquired the final v4 from https://arxiv.org/pdf/1312.4463v4 and confirmed the same statement in the retained 17-page PDF.
The recorded artifact size is240421bytes.
Version v4 was submitted 17 September 2015, 08:30:31 UTC; the postprint's 2015 to-appear header is distinguished from the journal's 2016 publication.
The coordinator owns source registration, accepted-statement allocation and the visual verification recorded above.
No source-wide proof review is inferred from these checks, and no source identifier is allocated by this draft.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0065_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
