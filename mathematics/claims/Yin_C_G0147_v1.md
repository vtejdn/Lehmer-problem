---
author: Yin
---
# A frequency-weighted modulus for complete original cyclic norms

Date: 2026-10-15T13:10.
Human author Yin.
New delegated F-inspired proof inquiry by f_unitary_scope under the continuing G0001 goal.
Root supplied the SUBSTANTIVE candidate: combine C137's all-original-root radial regularization with C131's frequency-weighted sum, choose r=1-t and delta=t/sqrt(r), and balance t=[h log^2(1/h)]^(1/5) at a finite cutoff J.
Root is a mathematical contributor and cannot independently review the resulting proof.
This author will verify or repair all domains, constants, original norms and finite tails directly here.
No native mathematical program or J is proposed.

## Responsible question and reuse decision

For every original monic irreducible nontorsion integer unit alpha of degree d, total m>0 and integer n>=1, put h=n*m/d.
Prove a universal complete cyclic norm upper bound of order [h log^2(1/h)]^(1/5) as h tends to zero, with an explicit small-h cutoff and no reciprocity/Salem assumption, or retain the exact failure.
All original conjugates and degree drops after powering must remain paid.
This would improve the quantitative modulus of L209, not give a positive Mahler gap or automatic arithmetic coverage.

Read the actual adopted [C131 frequency-weighted estimate](Yin_C_G0131_v1.md#frequency-weighted-angular-bound), its constants and finite-domain proof, [C137 finite logarithmic argument](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument), and [L209 current cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus).
A corrected bounded local G Claim/ledger search by frequency-weighted sum, the exact75c^(-1/4) constant and cyclic1/5 terminology found C131 and its C134 reuse, but no already retained all-unit cyclic-norm conclusion with this modulus.
This is a bounded reuse conclusion, not an exhaustive literature or novelty claim.

C131 ALREADY proves the numerical summation and one-fifth balance; neither is a new method here.
Its original application uses Salem unit-circle trace factors and separately pays two real roots.
The present needed conclusion concerns the full norm for ALL original unit conjugates, with C137 paying both radial directions before the finite weighted angular sum.
The existing [L229 exact finite angular interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence), including its accepted Pri11/Dim19 statement and proof-inspection limits, is the common underlying input.
No new source theorem, infinite-frequency application or native computation is assumed.

The initial candidate is to set t=[h log^2(1/h)]^(1/5), r=1-t, delta=t/sqrt(r), J=ceil(log(1/h)/t).
On the circle, |1-z^n|^2+delta^2=r^(-1)|1-r z^n|^2.
Its half-logarithm has a convergent geometric Fourier expansion with an explicitly paid finite remainder.
An explicit cutoff such as h<=exp(-40) will be checked before any conclusion is asserted.
This allocation records an author question and candidate only; complete proofs follow incrementally below, and fixed adoption/independent review remain separate.

## Statement

Let P be a monic irreducible nontorsion integer unit polynomial, alpha one of its roots, d=[Q(alpha):Q] its ORIGINAL degree, and m=log M(P)>0 its TOTAL logarithmic Mahler measure.
For every integer n>=1 put

    C_n=abs Norm_(Q(alpha)/Q)(alpha^n-1),
    h=n*m/d, c=log2/4, h0=c exp(-20),
    A=75c^(-1/4), B=A+9, h_star=exp(-40).

Then C_n is a nonzero positive integer and, whenever0<h<=h_star,

    0<=log C_n/d<=B [h log^2(1/h)]^(1/5).             (1)

The upper modulus is increasing on(0,h_star] and tends to zero.
It is uniform over all such original polynomials and all n, permits arbitrary degree drops after powering, and requires no reciprocity, Salem root geometry, good prime, coefficient-height or support assumption.
For any h>0 the elementary bound log C_n/d<=log2+h remains available.
On the overlap with L209 one can take the minimum of its old modulus and(1), without declaring an unproved comparison at all finite h.

The proof is an all-original-conjugate specialization and combination of the accepted C137 radial step and C131 numerical frequency summation, with root's regularization/balance candidate and the complete new cutoff/norm accounting written below.
It is not a new summation method, source theorem or unconditional Mahler gap.

<a id="argument"></a>
<a id="complete-cyclic-norm-and-radial-cost"></a>
## 1. All original roots and the radial regularization

Write ALL original complex conjugates as alpha_i=r_i z_i, with r_i>0, |z_i|=1.
Since P is a unit,

    sum_i log^+r_i=m, sum_i |log r_i|=2m.             (2)

Global nontorsion excludes alpha_i^n=1 for every i,n.
Thus F(X)=1-X^n has degree n, coefficient l1 norm S=2, and nonzero original resultant of absolute value C_n.
The sign difference between Norm(1-alpha^n) and Norm(alpha^n-1) has modulus1 and is not an omitted root factor.
Integrality and nonvanishing give C_n>=1.

For clarity on degree drops, let d_n=[Q(alpha^n):Q].
Every distinct conjugate of alpha^n occurs d/d_n times among the d displayed powers.
Consequently

    log C_n/d=log abs Norm_(Q(alpha^n)/Q)(alpha^n-1)/d_n,
    h=m(P_(alpha^n))/d_n.                            (3)

The second identity follows by summing n log^+r_i with these exact multiplicities.
The proof below uses the d ORIGINAL labels, not a silent replacement of d by d_n.
The L229 angular interface already accounts for the same multiplicities, separately at every frequency jn.

Set V_i=F(alpha_i)/max(1,r_i)^n.
The actual local step in C137 gives

    abs(V_i-F(z_i))<=2 min(1,n abs(log r_i)),
    log C_n/d=h+(1/d)sum_i log abs V_i.              (4)

Indeed this is its coefficient-by-coefficient normalization at the full original width n.
For ANY real delta>0, psi_delta(x)=log(x^2+delta^2)/2 on x>=0 has derivative at most1/(2delta).
Therefore

    log C_n/d <= (1/d)sum_i (1/2)log(abs(1-z_i^n)^2+delta^2)
                         +(1+2/delta)h.             (5)

This uses abs(abs V_i-abs F(z_i))<=abs(V_i-F(z_i)), then(2), and includes interior, exterior and circle roots.
C137's complete coefficient-majorant statement specifies rational delta for its separate exact-rational finite construction.
ONLY its displayed radial Lipschitz calculation is reused here, and the calculation just written proves its validity for every real delta>0.
No rationality-dependent conclusion from the full C137 theorem is applied to an irrational delta.

<a id="finite-geometric-log-majorant"></a>
## 2. Exact circle identity and a genuinely finite Fourier majorant

Let0<t<1, r=1-t, lambda=-log r>0 and delta=t/sqrt(r).
For every |z|=1,

    abs(1-z^n)^2+delta^2=r^(-1) abs(1-r z^n)^2.

This follows by expanding both sides: r+r^(-1)-2=t^2/r.
The absolutely convergent elementary logarithm expansion at |r z^n|<1 gives

    (1/2)log(abs(1-z^n)^2+delta^2)
      =-(1/2)log r-sum_(j>=1) r^j Re(z^(jn))/j.     (6)

For a chosen integer J>=1 define T_J=r^(J+1)/[(J+1)t].
Since the absolute tail is at most sum_(j>J)r^j/j<=T_J, the pointwise FINITE upper bound is

    (1/2)log(abs(1-z^n)^2+delta^2)
      <=lambda/2-sum_(j=1)^J r^j Re(z^(jn))/j+T_J.   (7)

The tail is paid before using any arithmetic angular statement.
The exact circle identity at z^n=1 is harmless because delta>0; no singular log boundary or root deletion is present.
The actual largest Fourier frequency in this majorant is Jn.

For0<Jh<=h0, apply the already accepted L229 estimate separately at frequency jn, with its own original height parameter jh:

    abs((1/d)sum_i z_i^(jn))<=epsilon(jh), 1<=j<=J.

Here epsilon(x)=min(1,15sqrt(b(x))+4x), b(x)=max(x,sqrt(x/c)log sqrt(c/x)), exactly as in L229.
Equations(5)--(7) imply the complete finite estimate

    log C_n/d <=lambda/2+(1+2/delta)h
                    +sum_(j=1)^J epsilon(jh)r^j/j+T_J.   (8)

No arithmetic estimate is applied beyond j=J.
All d original conjugates are included, so the extra two-real-root subtraction used in C131's SALEM trace-factor application does not occur here.
Inserting that separate +2 term or discarding the off-circle roots would change this full-norm problem.

<a id="reused-weighted-sum-general-unit-interface"></a>
## 3. The already proved weighted numerical estimate in the new domain

Write ell=log(1/h).
Under0<Jh<=h0, the numerical part of C131, equation(2), gives

    sum_(j=1)^J epsilon(jh)r^j/j
          <=A(h/lambda)^(1/4)sqrt(ell)+4h/lambda,
    A=75c^(-1/4).                                    (9)

This is exactly its numerical inequality with a replaced by h and L by lambda.
The original C131 application was a Salem argument, but this numerical step has no root-configuration hypothesis: its proof depends only on the displayed epsilon, h,lambda,J and Jh<=h0.
To make the interface explicit, its pointwise bound on0<x<=h0 is

    epsilon(x)<=15c^(-1/4)x^(1/4)sqrt(log(1/x))+4x.

For1<=j<=J, log(1/(jh))<=ell.
The existing decreasing-integrand comparison bounds sum_(j>=1)j^(-3/4)exp(-j lambda) by5lambda^(-1/4), and the geometric sum is at most1/lambda.
These are sums of EXPLICIT NUMERICAL MAJORANTS, not extensions of epsilon or of the original-root estimate to an infinite frequency range.
They give(9) with the same constant75 and attribution.
The factor one-fifth below is the same previously proved balance; the new conclusion is its valid complete cyclic-norm application and fully supplied cutoff.

<a id="explicit-cyclic-modulus-cutoff"></a>
## 4. Explicit cutoff, all errors and the one-fifth bound

Assume0<h<=exp(-40), so ell>=40.
Set exactly

    t=h^(1/5)ell^(2/5), r=1-t,
    delta=t/sqrt(r), J=ceil(ell/t).                  (10)

All these are finite real parameters except the integer J.
The function exp(-ell/5)ell^(2/5) decreases for ell>2.
Consequently

    0<t<=exp(-8)40^(2/5)<40/2^8=5/32<1/2.

Thus r>=1/2, delta>=t, and

    t<=lambda=-log(1-t)<=t/(1-t)<=2t.                (11)

The actual angular cutoff is also valid.
Using ceil x<=x+1,

    Jh<=h ell/t+h=exp(-4ell/5)ell^(3/5)+exp(-ell)
       <=41exp(-32)<(1/8)exp(-20)<c exp(-20)=h0.    (12)

For the second line, ell^(3/5)<=ell, the function ell exp(-4ell/5) decreases for ell>=40, and exp(-ell)<=exp(-32).
For the strict comparison, exp(12)>2^12>328=8*41.
Finally log2>1/2, hence c>1/8.
This proves the actual finite-domain hypothesis from the one explicit h cutoff; it is not a limit-only assertion or an unverified numerical threshold.

The tail is small with all its factors retained.
Since (J+1)t>ell and r<=exp(-t),

    T_J<=exp(-(J+1)t)/[(J+1)t]<=h/ell<=t.           (13)

Also h<=t^2, because h/t^2=h^(3/5)ell^(-4/5)<1.
It follows from(11), delta>=t and t<1 that

    lambda/2<=t,
    (1+2/delta)h<=h+2h/t<=3t,
    4h/lambda<=4h/t<=4t.                            (14)

For the remaining term use the EXACT identity t^5=h ell^2:

    A(h/lambda)^(1/4)sqrt(ell)
          <=A(h/t)^(1/4)sqrt(ell)=A t.              (15)

Combining(8)--(9) and(13)--(15) gives log C_n/d<=(A+9)t, precisely(1).
The sum of costs is1 from lambda/2,3 from the complete radial charge,4 from the numerical linear angular term, and1 from the explicit Fourier tail, in addition to A.
No degree-normalized substitute for total m, omitted leading scalar, missing conjugate or infinite source range occurs.

For completeness, x^(1/5)log^(2/5)(1/x) has positive derivative when0<x<exp(-2), since its logarithmic derivative is [1-2/log(1/x)]/(5x).
Therefore the new modulus is increasing throughout the stated domain and tends to zero.
The elementary all-h bound in the Statement follows from abs(alpha_i^n-1)<=2 max(1,r_i)^n and(2), with the full original norm retained.

<a id="cyclic-modulus-comparison-and-source-scope"></a>
## 5. Exact earlier-modulus comparison and source boundaries

The old accepted L209 modulus is19 b(h)^(1/6), with exactly the same c,h0 and b used above.
As h tends to zero its displayed value has order h^(1/12)log^(1/6)(1/h), whereas (1) has order h^(1/5)log^(2/5)(1/h).
More precisely the ratio of the two displayed upper-bound functions has order

    h^(7/60)log^(7/30)(1/h),

which tends to zero.
Thus this is an asymptotically sharper universal bound for the SAME complete original cyclic norm.
It is not a pointwise assertion that the new bound is smaller for every h, and it is not an improvement to the lower Mahler estimate used inside L229.
On their common explicit domain both upper bounds remain valid and their minimum is available.
No optimality of1/5 or of the conservative constant A+9 is claimed.

The precise accepted source route remains L229.
Its [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), actually reread, accepts arXiv:1307.5734v1 Theorem3.1 at statement/applicability scope, including simple integral zeros, actual powered degree at least55, global Lipschitz test and compact support.
L229 provides the finite compact angular test, radial conversion and actual degree escape before producing epsilon.
The present proof uses only that already established finite angular statement at jn.
It does NOT insert the singular logarithm into Pri11 or claim a new audit of its potential-theory proof.

The house input used by L229 is retained Dim19 arXiv v1 Theorem1, at the exact [Smy08-U001 house subsection](../audits/literature/Smy08/Yin_U001.md#smy08-house): noncyclotomic monic irreducible degree greater than1, house at least2^(1/(4d)).
Its source-original proof and later accepted edition have not been newly inspected or substituted here.
The factor d/d_n in(3) and the analogous factors at jn are why the source's actual powered degree is never silently identified with d.

C131's frequency weighting and one-fifth balancing method are credited without alteration.
Its separate Salem trace-factor theorem, node cutoffs, residual matrices, two-real-root correction and product-collapse assumptions are NOT imported as hypotheses of(1).
C137's finite majorant with general coefficient cost2^J is likewise not asserted to become cheap for arbitrary dense auxiliaries: this proof uses the special EXACT geometric Fourier coefficients of the SINGLE integral binomial1-X^n.
Its degree is n, content1, coefficient l1 norm2 and squared coefficient norm2.
The real analytic smoothing parameters do not create arithmetic denominators or income.
The actual maximum test frequency Jn and its source height Jh have both been paid.

The proof assumes no supplied near-one sequence, no residue-Frobenius class restriction, and no positive lower income beyond integrality C_n>=1.
It therefore supplies an improved universal expense interface, not automatic lower norm growth, positive density coverage, or a solution to G0001.
Any use in the separate class-escape inquiry must wait for actual fixed adoption and must recheck its own moving parameters and source domain; no such downstream theorem is proved or used here.

## Contributions and completion boundary

Root supplied the substantive regularized-circle identity, its intended finite tail, the proposed combination with C137/C131, and the t,J balance.
The f_unitary_scope author checked the complete original-unit domain, the real-delta local interface, all original norm/degree-drop factors, explicit h_star=exp(-40), constants and finite cutoff inequalities, and organized the full proof and comparison.
Both are contributors; neither can independently whole-review this new account.
Earlier C131/C137 authorship and accepted source boundaries remain separately credited.
No new external theorem, source acquisition, native mathematical program, J, shared-state edit or new user thread was needed.

The complete argument is now available for a separate noncontributor whole review after fixed retention.
This author's check alone does not make the theorem adopted or authorize a downstream use.

<a id="weighted-cyclic-entire-author-freeze"></a>
## 6. Entire author self-check and freeze

2026-10-15T13:17.
The author freezes the ENTIRE present account: initial question and candidate, exact reuse/provenance, Statement, Sections1--5, all15 formulas, the old-modulus comparison, source limits and contribution boundary.
No C146 application or other downstream conditional theorem is included.

The author reread the actual saved body and checked the nonzero integer norm for every n>=1, both original unit root-sum identities, every d/d_n field-norm multiplicity, the full S=2 radial Lipschitz cost for real delta, the half-log factor and sign in the regularized circle identity, the absolute tail BEFORE source use, the real part/angular modulus inequality and every frequency jn, and the purely numerical C131 summation scope.
The cutoff check independently verifies t<1/2, delta>=t, lambda between t and2t, Jh<h0 at the explicit endpoint h=exp(-40), the ceil and tail denominators, h<=t^2, exact t^5=h ell^2, constant A+9, monotonicity and the asymptotic comparison exponents7/60 and7/30.
No arithmetic discrepancy statement is used beyond J, and no original off-circle conjugate is discarded.

Degree-one nontorsion integer units do not exist.
Torsion inputs, n=0 and h=0 are outside the theorem; no zero cyclic norm is assigned a logarithm.
C_n=1 is allowed and gives zero normalized income.
Arbitrary coefficient sizes, many exterior roots, and powered-degree drops remain within the stated unit domain.
No new numerical validation, theorem-prover check or source-proof audit is claimed.
The scoped material check returned checked1 before this final freeze and is rerun after it; such a check is structural, not mathematical review.
Root and this author remain contributors, so an independent full review must be separately organized.

## Fixed organization

Retain the complete frozen author inquiry, every original norm and degree-drop multiplicity, finite regularization and Fourier cutoff, explicit constants, earlier-modulus comparison, accepted source limits and contribution account.
The new all-unit cyclic-norm interface is not already owned by the earlier Salem trace-factor theorem, and its numerical summation is explicitly reused from that theorem.
Root and f_unitary_scope are new-proof contributors.
No downstream Frobenius application or unrestricted Mahler gap is selected here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-15)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:19 |
| status | open |
| reason | Retain the complete finite frequency-weighted cyclic-norm modulus with explicit all-unit original-domain and powered-height costs. Independent whole review is pending; no arithmetic lower-income coverage or G0001 completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire universal modulus](#statement) | Every original nontorsion integer unit and positive exponent, explicit small-height cutoff, all degree drops, monotonicity and stated comparison. |
| argument | [Entire argument](#argument) | All six sections and fifteen numbered formulas, exact original norm, real regularization, finite frequency cutoff, full costs and source/contribution limits. |
| dependency | [Finite angular modulus](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon at each jn with actual original height jh, finite domain, powered-degree multiplicities and inherited Pri11/Dim19 statement-inspection limits. |
| dependency | [Existing weighted numerical sum](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) | Numerical equation(2), constant75c^(-1/4) and explicit majorant summation; no Salem-specific geometric or extra-two-root premise. |
| dependency | [Original-root radial calculation](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Displayed radial normalization and Lipschitz step only, locally reproved for every real delta; the separate rational-coefficient majorant theorem is not applied outside its domain. |
| support | [Earlier complete cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact comparison for the same full original norm, common-domain minimum and asymptotic ratio; not an automatic arithmetic income input. |

### Decision whole-reviewed-2026-10-15

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T13:26 |
| status | proved |
| reason | Adopt the actual whole noncontributor review of the universal complete cyclic-norm modulus, with every original conjugate and powered-degree drop, explicit finite cutoff and real-regularization source interfaces paid. No positive arithmetic lower-income coverage or unrestricted Mahler gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire universal modulus](#statement) | Every original nontorsion integer unit and positive exponent, explicit small-height cutoff, all degree drops, monotonicity and stated comparison. |
| argument | [Entire argument](#argument) | All six sections and fifteen numbered formulas, exact original norm, real regularization, finite frequency cutoff, full costs and source/contribution limits. |
| dependency | [Finite angular modulus](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon at each jn with actual original height jh, finite domain, powered-degree multiplicities and inherited Pri11/Dim19 statement-inspection limits. |
| dependency | [Existing weighted numerical sum](Yin_C_G0131_v1.md#frequency-weighted-angular-bound) | Numerical equation(2), constant75c^(-1/4) and explicit majorant summation; no Salem-specific geometric or extra-two-root premise. |
| dependency | [Original-root radial calculation](Yin_C_G0137_v1.md#finite-logarithmic-auxiliary-argument) | Displayed radial normalization and Lipschitz step only, locally reproved for every real delta; the separate rational-coefficient majorant theorem is not applied outside its domain. |
| support | [Earlier complete cyclic modulus](../ledger/Yin_L_G0209_v1.md#height-uniform-cyclic-cost-modulus) | Exact comparison for the same full original norm, common-domain minimum and asymptotic ratio; not an automatic arithmetic income input. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0359_v1.md#frequency-weighted-cyclic-whole-independent-finding) | Complete all-unit statement and six-section fifteen-formula proof, every selected dependency and support, all finite-domain costs and exact inherited source/contribution limits. |

