---
author: Yin
---

# Quantitative Salem lifts in arbitrary dyadic classes and irreducible constant-Mahler towers

Human author Yin.
Provenance: project deduction with the precise prior construction and classical source scopes below.
Root proposed the bounded coefficient CRT, Chebyshev dominance and linear Salem bound, the extra modulo25 norm condition for an irreducible dyadic tower, and the explicit characteristic-zero first-residual separation.
Same_trace checked every coefficient and central adjustment, D=2 and n=1 endpoints, all root/field and measure assertions, the nonsquare and positive-root arguments, and the exact C708 coefficient/degree applications below.
The existing [C450 reciprocal CRT mechanism](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma), [C527 modulo9 Eisenstein realization](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization), and [C685 actual finite-gate real lift](Yin_C_G0685_v1.md#statement) were directly read and are credited.
C685 locates every trace root above2 and charges every exterior pair in its separation-dependent measure expense; it does not give the Salem location or the bound proved here.
The related [C164 theorem](Yin_C_G0164_v1.md#statement) prescribes particular Salem Galois/ramification families, not an arbitrary coefficient class or this quantitative bound.
The [C212 radical control](Yin_C_G0212_v1.md#radical-collision-control) already contains a nonreciprocal norm-minus-one dyadic tower; its nonsquare argument does not cover these reciprocal norm-one inputs.
The needed commuting trace and exact canonical covariance are the adopted [C697 DP7](Yin_C_G0697_v1.md#statement).
The monic rational-factor property and monic Eisenstein criterion are the accepted [Con26d-U001 v2](../audits/literature/Con26d/Yin_U001.md#con26d-u001), Theorems2.1 and4.1 on pages2--4 of Keith Conrad's Irreducibility tests in Q[T].
Their applicability is exactly to the monic translate P(z+1), whose lower coefficients are divisible by3 and whose constant has3-adic valuation one.
That source is retained for the classical attribution and Gauss input, with its recorded selected-page proof-inspection limits; the complete elementary Eisenstein argument is also given below.
Salem_completion rechecked the complete retained construction and its direct fixed/source interfaces before registration; this is contributor scrutiny, not independent review.
No native coefficient search, numerical root approximation or uninspected external irreducibility theorem is used.
This is author mathematics awaiting fresh whole review.

## Statement

### SL1: prescribed coefficient class and two completely bounded choices

Let D>=2, n>=1, M=2^(n+1), and let T_0 in Z[X] be ANY monic degree-D polynomial.
Set P_0(z)=z^D T_0(z+z^(-1)), and r_j=[z^(2D-j)]P_0 for1<=j<=D.
There are two choices of a fixed auxiliary modulus:

    basic choice: L=3M;
    tower choice: L=75M.                            (SL1)

For each2<=j<=D choose c_j in[-L/2,L/2-1] satisfying

    c_j=r_j modulo M,
    c_j=(-1)^j binom(2D,j) modulo3,
    c_j=binom(2D,j)+5*1_(j=D) modulo25
                         in the tower choice only. (SL2)

These are unique centered integer CRT representatives.
Write a_j=c_j for2<=j<D and b_0=c_D; the a_j list is empty when D=2.
Choose the unique smallest integer B>=LD/2 with

    -B=r_1 modulo M,
    -B=-2D modulo3,
    -B=2D modulo25 in the tower choice only.         (SL3)

Thus LD/2<=B<LD/2+L and B is positive.
Form the reciprocal polynomial below initially with b=b_0.
If its value at1 is divisible by9, replace b by b_0+L; otherwise keep b=b_0.
Define

    P(z)=z^(2D)+1-B(z^(2D-1)+z)
               +sum_(j=2)^(D-1) a_j(z^(2D-j)+z^j)
               +b z^D,
    T(X)=C_D(X)-B C_(D-1)(X)
               +sum_(j=2)^(D-1) a_j C_(D-j)(X)+b,  (SL4)

where C_0=2, C_1=X and C_(j+1)=X C_j-C_(j-1).
In particular C_j(z+z^(-1))=z^j+z^(-j).
The coefficient of the basis element1 in this Chebyshev expansion is b, rather than b C_0; the identity is P=z^D T(z+z^(-1)).

Both choices give an irreducible monic reciprocal integer polynomial P of degree2D and constant1, with a genuine Salem root beta>1.
It has exactly the two real roots beta,beta^(-1), and all other2D-2 roots lie on the unit circle and are nonreal.
The irreducible trace polynomial T has D-1 simple roots in(-2,2) and exactly one root tau>2.
The trace field Q(tau) is totally real of degree D, while Q(beta) has signature(2,D-1) and is not totally real.

Define H(P) as its maximum absolute coefficient and m(P) as its full logarithmic Mahler measure, with natural logarithms.
Then

    H(P)<LD/2+L,
    (L/2-2)D+1<beta<(L/2+2)D+L-2,
    m(P)=log beta=log D+O_n(1).                    (SL5)

The explicit inequalities, not an unpriced asymptotic, apply to every prescribed T_0.
For M=32 the basic choice gives

    46D+1<beta<50D+94, H(P)<48D+96,                (SL6)

and the tower choice gives

    1198D+1<beta<1202D+2398, H(P)<1200D+2400.       (SL7)

In particular this varying-degree Salem construction is not near one in total Mahler measure.

### SL2: actual canonical data preserved at the stated dyadic precision

Coefficientwise P=P_0 modulo M and T=T_0 modulo M.
For ANY monic integer trace polynomial A define the actual canonical divided remainders and residuals

    a(A)=rem_A(A(C_2))/2,
    b(A)=rem_A(A(C_3))/3, c(A)=rem_A(A(C_5))/5,
    F(A)=rem_A(2c(A)^2-3a(A)^5),
    X_s(A)=rem_A(b(A)^2-a(A)^3+s(c(A)^3-2b(A)^5)),
    G(A)=rem_A(c(A)^3-2b(A)^5), s in{1,-1}.

These are integer canonical polynomials with the SAME indicated divisor.
The constructed T satisfies

    a(T)=a(T_0) modulo2^n,
    b(T)=b(T_0), c(T)=c(T_0) modulo M,
    F(T)=F(T_0), X_s(T)=X_s(T_0) modulo2^n.          (SL8)

Both signs are preserved at their actual input scope.
Thus an actual simultaneous residual solution modulo2^n acquires a Salem lift in the SAME trace degree and the SAME full coefficient class modulo2^(n+1).
All characteristic-two support and canonical data determined by this reduction remain unchanged.
At the distinguished trace root tau, a(T)(tau), b(T)(tau), c(T)(tau) are strictly positive, hence nonzero field elements whose values at every trace embedding are nonzero.
No positivity at the other embeddings is asserted.

### SL3: the additional norm condition and the complete irreducible tower

For the tower choice one additionally has

    P(-1)=5(-1)^D modulo25,
    v_5(P(-1))=1.                                 (SL9)

The Salem root beta is not a square in K=Q(beta).
For EVERY integer r>=0 put k=2^r and

    theta_r=beta^(1/k)>1,
    P_r(z)=P(z^k), T_r(X)=T(C_k(X)).                (SL10)

Then P_r is the irreducible minimal polynomial of theta_r, with actual degree2Dk, and T_r is irreducible of degree Dk.
All P_r are monic reciprocal integer unit polynomials, with

    H(P_r)=H(P),
    m(P_r)=m(P)=log beta>0,
    max_(P_r(z)=0)|z|=beta^(1/k) ->1.               (SL11)

There are exactly k roots outside the unit circle, k inside, and (2D-2)k on it, counted with their actual simple multiplicities.
Only the base r=0 is Salem; for r>=1 there is more than one exterior root.
The maximum root modulus tending to1 is not total Mahler measure tending to1, and the logarithmic measure does not tend to zero.

For each canonical expression a,b,c,F,X_s,G, exact INTEGER monic-division covariance gives its value at T_r by composing its canonical polynomial at T with C_k.
In particular every simultaneous residual congruence modulo2^n persists through the entire tower.
Modulo2, T_rbar=Tbar^k and G(T_r)bar=G(T)bar^k.
Every full irreducible multiplicity is multiplied by k; a proved common maximal Frobenius exponent and a nonzero canonical degree gap are multiplied by k as well.
No original maximality is inferred in the absence of that premise.

<a id="sl4-actual-c744-residual-solutions-and-every-degree-cost"></a>
### SL4: actual C708 residual solutions and every degree cost

Take an adopted C708 input from C691 with Q=2^ell, ell>=82, m=Q/4-2, its complete Y and H_aux, and original q_0>=8192 a power of2.
Write d_0=q_0(30m+degY).
C708 supplies an ACTUAL monic T_0 of degree D=2d_0 satisfying F(T_0)=X_s(T_0)=0 modulo16 for the selected sign.
Apply the present theorem with n=4 and M=32.
The resulting P is an actual Salem minimal polynomial of degree4d_0, and its trace polynomial has BOTH actual canonical residuals divisible by16 coefficientwise.
In the basic choice,

    92d_0+1<beta<100d_0+94, H(P)<96d_0+96.          (SL12)

For a fixed tower-choice base, let q_r=2^r q_0.
At every r>=0 the ACTUAL irreducible polynomial P_r and its trace have

    degP_r=4q_r(30m+degY),
    degT_r=2q_r(30m+degY),
    T_rbar=U_0^(2q_r), G(T_r)bar=R_0^(2q_r),
    degT_r-deg(G(T_r)bar)
              =2q_r(m-8-5degH_aux)>5q_r m/128.     (SL13)

Here U_0,R_0 are the SAME complete C691 characteristic-two polynomials and their exact fresh triple factor proves that their common maximal exponent in SL13 is2q_r.
The complete synthetic integer layer vector is a_0=24mq_r and a_j=0 for j>=1, retaining its original separate zero-Haar status.
For the fixed base, including the permitted choice q_0=8192, the tower has fixed height and fixed POSITIVE full measure, with

    2396d_0+1<beta<2404d_0+2398,
    H(P_r)<2400d_0+2400,
    m(P_r)=log beta.                               (SL14)

The source bound gives degP_r<=4q_r(14400Q^3+1206Q^2+128Q).
Every repeated and higher-five component and every degree multiplier is retained.
The Salem CRT lift does not preserve unproved actual J_2 factors or a prescribed integer factorization of G(T); no identification G_int=G_can, actual integer canonical-degree equality, characteristic-zero residual identities or original small-Mahler realization follows.
The tower receives no Salem or totally-real-field assertion beyond the explicitly stated base conclusions.

For M>=32, BOTH constructions also have the following explicit characteristic-zero boundary at their largest trace root tau:

    F(T)(tau)<-(7/1600)tau^(10D)<0.                 (SL15)

Every tower polynomial inherits a nonzero first characteristic-zero residual by exact covariance.
Thus these particular bounded CRT representatives fail that exact identity despite preserving the stated finite congruences.
No assertion that all other lifts of their coefficient classes fail is made.

## Complete argument

### SL5: integral trace coordinates, CRT and the central Eisenstein adjustment

The recurrence shows C_j is monic integral of degree j for j>=1 and C_j has the parity of j.
The set1,C_1,...,C_D is an integral triangular basis, with diagonal entries1, for integer polynomials of degree at most D.
Thus T_0 has a unique expansion

    T_0=C_D+sum_(j=1)^(D-1) r_j C_(D-j)+r_D.

Substitution X=z+z^(-1) proves that these r_j are exactly the reciprocal coefficients defined in SL1, including the center coefficient r_D with no division by2.
All prescribed CRT moduli are coprime, and their product is L.
The centered interval has exactly L integers, and SL3 has exactly one admissible B in[LD/2,LD/2+L).
The final central adjustment changes b by either0 or L, so it preserves all congruences modulo M and, when required, modulo25.
It also gives

    |a_j|<=L/2, |b|<=3L/2-1.

The paired binomial coefficients are symmetric at indices j and2D-j, and (-1)^(2D-j)=(-1)^j.
Consequently P(z)=(z-1)^(2D) modulo3, including its center and endpoints.
Hence3 divides P(1).
Since v_3(L)=1 in BOTH choices, adding L when9 divides the preliminary value makes3 divide the final P(1) exactly once.
Only the single center coefficient is changed, so P(1) changes by L rather than2L.
It follows that P(z+1) is monic, every lower coefficient is divisible by3, and its constant coefficient has exact3-adic valuation1.
The credited Eisenstein mechanism proves irreducibility: any monic integral factorization would reduce modulo3 to two powers of z with both constants divisible by3, contradicting that exact valuation.
The monic rational-factor conclusion follows by the same Gauss argument used in C685; translation preserves rational reducibility.
If T factored rationally, its two monic trace factors would give nonconstant monic reciprocal factors of P after substitution, so T is irreducible as well.

The recurrence identity also proves P=z^D T(z+z^(-1)), monicity, reciprocity and constant1 directly.
CRT gives P=P_0 modulo M.
The integral triangular basis, or successive comparison of the highest reciprocal coefficients, then gives T=T_0 coefficientwise modulo M even when M is even.
No invertibility of2 is used in this inverse trace step.

### SL6: every trace root, the Salem field and full quantitative bounds

For X=2cos theta the recurrence gives C_j(X)=2cos(j theta), so |C_j(X)|<=2 on[-2,2].
Put N=D-1>=1 and x_l=2cos(l pi/N), 0<=l<=N.
These are D strictly decreasing real points from2 to-2, and C_N(x_l)=2(-1)^l.
The complete remaining part of T has magnitude at most

    2+L(D-2)+(3L/2-1)=LD-L/2+1<LD<=2B.

The strict inequality holds for n>=1 because L>=12; it includes D=2, where the middle sum is empty.
Therefore T(x_l) has sign -(-1)^l.
There is a root in each of the D-1 disjoint open intervals between consecutive x_l.
Also T(2)<0 and T is monic, so there is a root tau>2.
These are D distinct roots of a degree-D polynomial; they exhaust its roots and are all simple.
In particular neither endpoint2 nor-2 is a root.

Every trace root in(-2,2) gives exactly two distinct nonreal unit-circle roots of z^2-xz+1.
The root tau gives beta=(tau+sqrt(tau^2-4))/2>1 and its positive reciprocal.
Different trace roots cannot share a reciprocal root.
Together with irreducibility and constant1 this proves that beta is a genuine Salem algebraic unit of degree2D.
It also proves the stated trace-field degree and the signature(2,D-1) of Q(beta).

The coefficient of X^(D-1) in T is exactly -B: C_D has the opposite parity at that degree and C_(D-1) is monic.
Thus the sum of all D trace roots is B.
The D-1 interior roots have sum strictly between -2(D-1) and2(D-1), giving

    B-2(D-1)<tau<B+2(D-1).

For tau>2 one has tau-1<beta<tau.
Combining this with the exact interval for B proves SL5's beta bounds.
All coefficients of P other than -B have magnitude at most max(1,3L/2-1), strictly less than LD/2+L for D>=2.
This proves the height bound, including both boundary cases D=2 and n=1.
Only beta lies outside the unit circle, so the FULL logarithmic Mahler measure is exactly log beta.
Substitution L=96 or2400 yields SL6--SL7 and SL12--SL14.

At the largest trace root tau>2, C_p(tau)>tau for p=2,3,5: write tau=t+t^(-1), t>1, and compare t^p+t^(-p) with t+t^(-1).
Because T is monic and all its roots are at most tau, T(C_p(tau))>0.
Evaluating the actual monic division gives the three claimed positive divided values.
Irreducibility of T makes their other trace embeddings nonzero by injectivity of embeddings.

### SL7: actual dyadic coefficient continuity and exact composition

For any monic integer A, C_p=X^p modulo p and A(C_p)=A^p modulo p; hence the actual monic remainder is coefficientwise divisible by p.
Monic division uses only coefficient addition and multiplication, so it commutes with reduction modulo M even when the reductions have repeated factors.
The congruence T=T_0 modulo2^(n+1) therefore gives congruent actual numerators at that precision.
Dividing the even numerator by2 gives a(T)=a(T_0) modulo2^n; dividing by3 or5 preserves congruence modulo M because they are odd units there.
Polynomial arithmetic and a further actual monic division prove SL8 for both residuals.
These are comparisons of their unique degree<D coefficient polynomials, not merely values at selected roots.

For the tower use the exact C697 DP7 mechanism.
The recurrence and injective Laurent substitution give C_i(C_j)=C_(ij)=C_j(C_i).
If R=AQ+R_0 is actual monic division, then R(C_k)=A(C_k)Q(C_k)+R_0(C_k), with degR_0(C_k)<k degA.
Thus actual remainder and legitimate integer division commute with composition, proving all stated canonical covariance including G.
In characteristic2, C_(2^r)=X^(2^r), so each reduction is the actual k-th power of its predecessor.
This proves preservation of every full multiplicity, nonzero canonical degree gap and already established maximal Frobenius exponent.

### SL8: nonsquareness from the additional norm and positive-root induction

In the tower choice, all paired coefficients and the center give

    P(z)=(z+1)^(2D)+5z^D modulo25.

The central+L adjustment preserves this because25 divides L.
Evaluation at-1 proves SL9, in particular P(-1) is nonzero with odd5-adic valuation.
Let alpha=beta+beta^(-1), F=Q(alpha) and K=Q(beta).
The already proved degrees give[K:F]=2, and its involution sigma sends beta to beta^(-1).
Suppose beta=gamma^2 for gamma in K.
Then sigma(gamma)=gamma^(-1) or -gamma^(-1).
In the first case gamma+gamma^(-1) is in F and its square is alpha+2.
But

    Norm_(F/Q)(alpha+2)=(-1)^D T(-2)=P(-1)

has odd5-adic valuation, whereas the norm of a square in F is a rational square.
In the second case gamma-gamma^(-1) is in F and its square is alpha-2.
At any of the D-1 interior real trace embeddings, alpha-2 is negative, which cannot be a square in that real field.
The assumption D>=2 ensures such an embedding exists.
Both alternatives are impossible, so beta is not square in K.

Now take the positive roots theta_r and fields E_r=K(theta_r), all inside the chosen real embedding.
Starting with theta_0=beta nonsquare in E_0=K, assume theta_(r-1) is positive and nonsquare in E_(r-1).
Then E_r=E_(r-1)+E_(r-1)theta_r has degree2 over E_(r-1).
If theta_r=(u+v theta_r)^2 in E_r, comparison in this basis gives

    u^2+theta_(r-1)v^2=0, 2uv=1.

The first equality over real numbers with theta_(r-1)>0 forces u=v=0, contradicting the second.
Thus theta_r remains nonsquare in E_r, completing the induction and proving[E_r:K]=2^r.
Since beta=theta_r^(2^r), the field Q(theta_r) already contains K, so it equals E_r.
Its degree is2Dk, exactly the degree of P(z^k), proving irreducibility without an additional composition-irreducibility theorem.
The trace factorization argument from SL5 also proves irreducibility of T(C_k).

For each nonzero root lambda of P, its k roots in P(z^k) all have modulus |lambda|^(1/k).
Their total logarithmic Mahler contribution is log max(1,|lambda|), exactly its old contribution.
All roots remain simple, since P is separable and nonzero at0 in characteristic zero.
This proves the complete root counts, constant full measure, house and unchanged coefficient height in SL11.
It also makes explicit why the tower is not Salem for r>=1 and why its limiting house supplies no vanishing-Mahler conclusion.

<a id="sl9-full-c744-application-and-retained-original-boundary"></a>
### SL9: full C708 application and retained original boundary

C708 supplies the actual T_0 and residual congruences required by SL8 with D=2d_0 and n=4.
Its statement and adopted LF0c retain U_0^(2q_0), R_0^(2q_0), actual degree2d_0, gap, and exact maximal exponent2q_0 from C691's fresh triple factor.
The coefficient CRT changes none of these characteristic-two data and directly preserves the actual residuals modulo16.
It supplies the genuine irreducible Salem minimal polynomial that was not included in C708.

For the tower fix this one base, and apply the exact covariance and multiplicity scaling of SL7 at every k=2^r.
This gives SL13 with q_r=kq_0, with no unproved exchange of a growing-degree and precision limit.
The source synthetic integer layer vector scales to a_0=24mq_r, all other entries zero; this retains complete factors and its separate Haar interpretation, not an equality with actual G(T_r).
The source degree upper bound and strict gap multiply by the displayed k, giving the stated full expense.
The constant height and positive measure bounds depend on the fixed base d_0 and never shrink toward zero along the tower.
No characteristic-zero residual identity, actual integer G factorization or unrestricted G0001 completion is claimed; the next section explicitly separates these representatives from the first exact identity.

### SL10: explicit separation from the first characteristic-zero equation

Assume M>=32, so L>=96 in either choice.
Write t=tau for the unique exterior trace root.
The proof in SL6 gives t>46D+2>=94.
Set u=C_2(t)=t^2-2 and v=C_5(t)=t^5-5t^3+5t.
Both exceed t, so T(u),T(v)>0.
Every other trace root x_i is in(-2,2); hence

    T(u)>(t^2-t-2)(t^2-4)^(D-1)
         =t^(2D)(1-1/t-2/t^2)(1-4/t^2)^(D-1).

The elementary integer-power inequality (1-x)^j>=1-jx on0<=x<=1, obtained by induction, gives

    T(u)>t^(2D)[1-1/t-(4D-2)/t^2].

Since D<(t-2)/46, the omitted error is less than25/(23t), which is less than1/50 for t>94.
Thus T(u)>(49/50)t^(2D).
Also v+2<t^5 for t>2, so every positive factor of T(v) is smaller than t^5 and T(v)<t^(5D).
At the actual root t the canonical remainders therefore satisfy

    a(T)(t)=T(u)/2>(49/100)t^(2D),
    c(T)(t)=T(v)/5<(1/5)t^(5D).

Evaluation removes the final monic remainder, giving

    F(T)(t)=2c(T)(t)^2-3a(T)(t)^5
      <[2/25-(3/32)(49/50)^5]t^(10D)
      <=[2/25-27/320]t^(10D)
      =-(7/1600)t^(10D).

The coefficient comparison uses (49/50)^5>=1-5/50=9/10.
This proves SL15 with the actual canonical a,c,F, without selecting independent quotient coordinates.
For the tower, at the distinguished real trace theta_r+theta_r^(-1), C_k takes the value t.
The exact covariance therefore gives the same negative value for F(T_r), so it is not the zero polynomial.
Only the constructed representatives and their towers are covered by this nonvanishing assertion.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision quantitative-salem-tower-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T14:06 |
| status | open |
| reason | Register the complete bounded construction in every monic degree-D dyadic coefficient class, its irreducible Salem lift with linear house/height bounds, all actual finite canonical residual congruences, the norm-controlled irreducible dyadic tower with fixed positive full Mahler measure, exact C708 source costs and explicit characteristic-zero first-residual failure for M>=32. The full author proof and classical source applicability are retained; fresh isolated whole review and acceptance remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire quantitative lift and tower](#statement) | SL1--SL15: every D>=2, n>=1 and monic input, both bounded CRT choices, all roots and field signatures, full coefficient/canonical precision, all r>=0 tower degrees and measures, original C708 costs and exact stated characteristic-zero boundary. |
| argument | [Complete six-part proof](#complete-argument) | SL5--SL10: integer trace basis, centered CRT and central Eisenstein adjustment, full alternating root count and expenses, actual monic coefficient continuity and covariance, norm nonsquareness and every positive-root degree step, original application and strict nonzero first residual. |
| support | [Classical monic rational factors and Eisenstein](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Accepted Theorems2.1 and4.1, pages2--4, at the precise monic translated integer polynomial and prime3 hypotheses. Retain the actual selected-page proof-inspection scope; the elementary Eisenstein contradiction is also reproduced. |
| support | [Earlier reciprocal local CRT realization](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma) | Credited coefficientwise trace CRT and translated reciprocal Eisenstein mechanism only; no unrelated local-depth, prime-income or measure assertion is imported. |
| support | [Earlier binary and 3-Eisenstein realization](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | Credited compatible dyadic coefficient and translated 3-Eisenstein construction only; no simplicity, local-depth or total-measure claim is imported. |
| support | [Earlier actual finite-gate real lift](Yin_C_G0685_v1.md#decision-whole-reviewed-2026-10-24) | Credited same-divisor coefficient continuity, irreducible trace/reciprocal mechanism and largest-trace nonvanishing. Its all-roots-above2 construction and large complete measure are a comparison, not a Salem premise. |
| dependency | [Adopted exact trace covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 exact integer monic-division covariance for every trace composition, plus its uncorrected reciprocal and binary multiplicity/degree scaling; no higher corrected-level existence is assumed. |
| dependency | [Adopted actual simultaneous-sixteen input](Yin_C_G0708_v1.md#decision-whole-reviewed-2026-10-25) | LF0a--LF0c actual degree2d0 input, both residuals16 for the chosen sign, original complete binary canonical data, exact maximal2q0 and degree/gap/layer costs. No actual J2 factor is presumed after the new CRT lift. |
| dependency | [Adopted complete source and synthetic costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 original Q/m/Y/H_aux family, actual U0/R0, exact fresh triple factor and common maximality, full degree/gap bounds and separate synthetic integer layer/zero-Haar statement. This synthetic polynomial is not identified with actual G. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T14:16 |
| status | proved |
| reason | Adopt the entire fixed SL1--SL15 statement and SL5--SL10 argument after complete main-agent reading and fresh isolated whole R932v2. Both bounded arbitrary-class Salem constructions, all exact root/height/measure and canonical precision claims, the norm-controlled irreducible dyadic tower and complete C708 source expenses are supported with the recorded classical-source scope. The tower keeps fixed positive full Mahler measure while its house tends to one. For M>=32 these constructed representatives have the explicitly negative first characteristic-zero residual; this does not exclude other lifts or resolve the unrestricted Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire quantitative lift and tower](#statement) | SL1--SL15: every D>=2, n>=1 and monic input, both bounded CRT choices, all roots and field signatures, full coefficient/canonical precision, all r>=0 tower degrees and measures, original C708 costs and exact stated characteristic-zero boundary. |
| argument | [Complete six-part proof](#complete-argument) | SL5--SL10: integer trace basis, centered CRT and central Eisenstein adjustment, full alternating root count and expenses, actual monic coefficient continuity and covariance, norm nonsquareness and every positive-root degree step, original application and strict nonzero first residual. |
| support | [Classical monic rational factors and Eisenstein](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Accepted Theorems2.1 and4.1, pages2--4, at the precise monic translated integer polynomial and prime3 hypotheses. Retain the actual selected-page proof-inspection scope; the elementary Eisenstein contradiction is also reproduced. |
| support | [Earlier reciprocal local CRT realization](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma) | Credited coefficientwise trace CRT and translated reciprocal Eisenstein mechanism only; no unrelated local-depth, prime-income or measure assertion is imported. |
| support | [Earlier binary and 3-Eisenstein realization](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | Credited compatible dyadic coefficient and translated 3-Eisenstein construction only; no simplicity, local-depth or total-measure claim is imported. |
| support | [Earlier actual finite-gate real lift](Yin_C_G0685_v1.md#decision-whole-reviewed-2026-10-24) | Credited same-divisor coefficient continuity, irreducible trace/reciprocal mechanism and largest-trace nonvanishing. Its all-roots-above2 construction and large complete measure are a comparison, not a Salem premise. |
| dependency | [Adopted exact trace covariance](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | DP7 exact integer monic-division covariance for every trace composition, plus its uncorrected reciprocal and binary multiplicity/degree scaling; no higher corrected-level existence is assumed. |
| dependency | [Adopted actual simultaneous-sixteen input](Yin_C_G0708_v1.md#decision-whole-reviewed-2026-10-25) | LF0a--LF0c actual degree2d0 input, both residuals16 for the chosen sign, original complete binary canonical data, exact maximal2q0 and degree/gap/layer costs. No actual J2 factor is presumed after the new CRT lift. |
| dependency | [Adopted complete source and synthetic costs](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 original Q/m/Y/H_aux family, actual U0/R0, exact fresh triple factor and common maximality, full degree/gap bounds and separate synthetic integer layer/zero-Haar statement. This synthetic polynomial is not identified with actual G. |
| review | [Independent whole quantitative Salem and tower review](../audits/reviews/Yin_R_G0932_v2.md#whole-quantitative-salem-and-tower-finding) | Entire exact SL1--SL15 statement and SL5--SL10 argument, all endpoint/root/field/canonical/tower/degree/measure conclusions, accepted classical-source and full original-family interfaces, and the strict characteristic-zero residual bound. The corrected review wording in v2 preserves the performed isolated review; no target repair occurred. |

