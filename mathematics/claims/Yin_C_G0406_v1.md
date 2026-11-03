---
author: Yin
---

# Arithmetic conditioning of the actual Salem critical polynomial and its unavoidable global-product expense

This retains the complete necessary mathematical argument from [complete original L371 proof and boundaries](../ledger/Yin_L_G0371_v1.md#salem-critical-primitive-squarefree-arithmetic).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.
The substantive derivation was prepared by salem_review AI for Yin after the recorded2026-10-11T13:29 handoff; the preceding allocation contained no developed proof.
The full allocation/handoff and source/review account remains at the original L371.

## Statement

Let P=z^s Q(z+z^-1) be the complete irreducible minimal polynomial of a genuine Salem number beta>1, with d=2s>=4, x_0=beta+beta^-1 and H=sum|a_j|. Retain precisely the critical polynomial F=(z^2-1)z^(s-1)Q'(z+z^-1)=zP'-sP and nearest-root constant c_P of C402, with every original root, leading factor and multiplicity; no freely rescaled polynomial is substituted.
Put h=content(Q')=content(F), a=s/h>=1, e=1 if Q'(2)=0 and0 otherwise, V=Q'/[h(x-2)^e], t=s-1-e, R=F/[h(z-1)^(2e)]=(z^2-1)z^t V(z+z^-1), and n=d-2e. Then R is primitive integral, has leading coefficient a and is squarefree, including t=0 where s=2,e=1,V=1,R=z^2-1. Its full polynomial discriminant is Delta=4|disc V|^2|V(2)V(-2)|^3>=1, with disc V=1 in degrees0/1; disc F or a field discriminant cannot replace it.
Let b be1 when V has its unique possible exterior trace root y>2, otherwise0. For e=0 this is exactly Q'(2)<0; e=1 forces b=0. Let Lambda=beta if b=1, otherwise1, L=n-2b be the distinct circle-root count, C_n=(n-1)^((n-1)/2) and B_*=h sqrt(Delta)/[C_n(a Lambda)^(n-2)]. Every circle root eta of R satisfies |(hR)'(eta)|>=B_*. Define tau_*=|V(2)|/[a4^(s-2)(x_0+2)] in the exterior branch and delta_*=min{4,|V(2)|/[a4^max(t-1,0)]} in the e=1 branch. The actual c_P has these coefficient-exact root-data-free lower bounds: (2/H)2^(-(L-1))B_* for e=b=0; that same expression times tau_* for e=0,b=1; and (2/H)2^(-(L+1))B_*delta_* for e=1. Each full leading/content/endpoint/off-circle factor is retained.
For every fixed B>1 and1<beta<=B, writing X_B=B+B^-1+2, all branches imply c_P>=[H2^d d^(d/2)(sB)^(d-2)s4^(s-2)X_B]^-1 and H<=2^(d-2)X_B, hence log(1/c_P)=O_B(d log d). This is a degree-paid upper bound on conditioning expense, not uniform conditioning.
In the reverse direction, let q=1 if b=0 and q=y-2 if b=1. The same specified constant satisfies c_P<=2sLq/[H2^(L-1)]. For m_*=1 when e=0 and3 when e=1, J=16d+2 and K_P^tr=L/pi+2Jpi^(m_*-1)/(2^(m_*)c_P), this gives K_P^tr-L/pi>=JHpi^(m_*-1)2^(L-1-m_*)/(sLq). With q_B=max{1,B+B^-1-2}, K_P^tr>=2H2^d/(d q_B). For every fixed C>0,A>=0 and integer1<=N<=Cd^A, its displayed sufficient tail T_N=(m_*+1)K_P^tr N^(-1/(m_*+1)) is at least4H2^d/[q_B sqrt(C)d^(1+A/2)]. Tuning the arc radius inside that same global estimate cannot remove the exponential-over-polynomial complementary term. These are lower bounds for this specified sufficient expression, not actual moments, optimal constants or every other method. Any hypothetical beta->1 sequence necessarily has d->infinity; its existence is not asserted.
On the accepted no-padding irreducible Salem progression N=120k+9,k>=1, P_N=z^(N+3)-z^(N+1)-z^N+1-z^2-z^3, the actual degree is d=N+3=2s, H=6, plastic<beta_N<4/3 and beta_N tends to the plastic root above1. Exact symbolic substitution gives Q'(2)=(-N^2+14N-1)/4<0, Q'(-2)=-(N^2+2N+17)/4, h=1,a=s,e=0,b=1,m_*=1,L=d-2 and0<q<1/12. Therefore K_(P_N)^tr>144*2^d/(d-2). This actual bounded-measure family disproves degree-uniform control of this K on beta<4/3, while its total measure tends to positive log(plastic). No arbitrary function of the exact beta, justified near-one restriction, different local/signed-tail estimate, actual finite certificate or unrestricted Mahler gap is excluded or established. No new source proof, program, root isolation or parameter scan was performed.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:51 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Complete actual critical polynomial and constant](Yin_C_G0402_v1.md#smaller-salem-critical-polynomial) | Full genuine Salem trace/interlacing domain, F leading degree and every root/multiplicity, exact gamma/c_P/J/K and tail definitions; no uniform-constant premise. |
| dependency | [Classical cofactor mechanism](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Only the complete Vandermonde/Hadamard method and original-root cost comparison; the present nonmonic leading/content adaptation is proved here. |
| dependency | [Accepted no-padding original Salem progression](Yin_C_G0336_v1.md#argument) | Only actual whole-polynomial irreducibility, original degree, plastic-limit and beta<4/3 at N=120k+9,k>=1; no selector execution or new family proof audit. |
| support | [Retained classical discriminant attribution](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Only the existing Section9 polynomial-discriminant/Hadamard/cofactor mechanism and its exact leading-factor boundary, not other source theorems or a new primary reading. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:54 |
| status | proved |
| reason | Adopt the actual complete SELF finding for the unchanged necessary theorem and proof after checking every primitive/nonmonic/endpoint/root factor, both estimate directions, finite constants, exact original family and all sufficient-expression/source/near-one limits. Original R273 UNKNOWN and author contribution/check remain separate; no fresh source/native run or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0402_v1.md#smaller-salem-critical-polynomial) | Full genuine Salem trace/interlacing domain, F leading degree and every root/multiplicity, exact gamma/c_P/J/K and tail definitions; no uniform-constant premise. |
| dependency | [Exact accepted input](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Only the complete Vandermonde/Hadamard method and original-root cost comparison; the present nonmonic leading/content adaptation is proved here. |
| dependency | [Exact accepted input](Yin_C_G0336_v1.md#argument) | Only actual whole-polynomial irreducibility, original degree, plastic-limit and beta<4/3 at N=120k+9,k>=1; no selector execution or new family proof audit. |
| support | [Exact support](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Only the existing Section9 polynomial-discriminant/Hadamard/cofactor mechanism and its exact leading-factor boundary, not other source theorems or a new primary reading. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0609_v1.md#current-salem-conditioning-whole-finding) | Complete exact Statement and necessary Sections1–4/(1)–(12) plus source/verification boundaries, all original-root/leading/content/endpoint expenses, explicit family and limitations. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:26 |
| status | proved |
| reason | Adopt the actual new complete independent finding after autonomous statement obligations, every necessary proof and precise accepted-input inspection, followed by whole original-account comparison. Original UNKNOWN/SELF arrangements, finite/native/source depths and all partial/negative/cost/nonuniformity limits remain separate; no new program, source-proof audit or unrestricted Task result is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0402_v1.md#smaller-salem-critical-polynomial) | Full genuine Salem trace/interlacing domain, F leading degree and every root/multiplicity, exact gamma/c_P/J/K and tail definitions; no uniform-constant premise. |
| dependency | [Exact accepted input](Yin_C_G0384_v1.md#derivative-discriminant-cost) | Only the complete Vandermonde/Hadamard method and original-root cost comparison; the present nonmonic leading/content adaptation is proved here. |
| dependency | [Exact accepted input](Yin_C_G0336_v1.md#argument) | Only actual whole-polynomial irreducibility, original degree, plastic-limit and beta<4/3 at N=120k+9,k>=1; no selector execution or new family proof audit. |
| support | [Exact support](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Only the existing Section9 polynomial-discriminant/Hadamard/cofactor mechanism and its exact leading-factor boundary, not other source theorems or a new primary reading. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0614_v1.md#isolated-salem-conditioning-whole-finding) | Whole exact current Statement and complete necessary proof; full original whole scope, all source/finite/endpoint/sign/conditioning/limit boundaries and the original useful negative conclusions, with actual isolated inputs disclosed. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="salem-critical-primitive-squarefree-arithmetic"></a>
## 1. Primitive squarefree reduction without dropping a leading or endpoint factor

Use L369's actual genuine Salem input P=z^s Q(z+z^-1), degree d=2s>=4, beta>1, x_0=beta+beta^-1, and H=sum|a_j|.
Retain its exact F and its displayed constant c_P, rather than a freely rescaled polynomial.
There is the coefficient-exact identity

    F=zP'-sP=sum_(j=0)^d (j-s)a_j z^j,
    content(F)=content(Q')=:h,   a=s/h in Z_(>=1).       (1)

Indeed z^(s-1)Q'(z+z^-1) has the same content as Q': read its coefficients from the highest Laurent power down, a triangular integer transformation with diagonal1.
Multiplication by the primitive monic z^2-1 preserves that content.
Equivalently the same conclusion follows by applying this triangular argument after dividing both inputs by the proposed content.
Thus h divides s and h>=1.
No content division will remove the h factor from F's paid derivative bound.

Put e=1 if Q'(2)=0 and e=0 otherwise.
By the already proved interlacing, e is the exact simple root multiplicity of2 in Q', no derivative root equals-2, and e=1 excludes an exterior derivative root.
Define

    V(x)=Q'(x)/[h(x-2)^e],    t=deg V=s-1-e,
    R(z)=F(z)/[h(z-1)^(2e)]
        =(z^2-1)z^t V(z+z^-1),   n=deg R=d-2e.        (2)

Division by the monic x-2, when needed, stays integral and primitive.
The same triangular coefficient transformation shows R primitive integral with leading coefficient a.
All its roots are simple.
The roots+1 and-1 are simple; each root y of V in(-2,2) contributes a simple inverse circle pair; its only possible off-circle pair is rho,rho^-1 with1<rho<beta, from the sole possible y>2.
In particular n>=2.
If t=0, necessarily s=2,e=1,h=s,a=1,V=1 and R=z^2-1.

Let Delta=|disc R|>=1 be the FULL polynomial discriminant of this primitive polynomial.
There is an exact coefficient-arithmetic identity

    Delta=4 |disc V|^2 |V(2)V(-2)|^3.                   (3)

Here disc V=1 for degree0 or1.
To check every leading factor, write V=a product_(j=1)^t(x-y_j) and G=z^t V(z+z^-1)=a product_j(z^2-y_j z+1).
Each quadratic has discriminant y_j^2-4 and the resultant of two such monic quadratics is(y_i-y_j)^2.
Including the factor a gives disc G=(disc V)^2 V(2)V(-2).
The resultant with z^2-1 has absolute value |G(1)G(-1)|=|V(2)V(-2)|.
The product-discriminant formula with disc(z^2-1)=4 proves(3), including the constant V=1 case directly.
The endpoints V(+/-2) are nonzero integers.
A field discriminant or disc F, which is zero when e=1, cannot substitute for Delta.

<a id="salem-critical-root-data-free-lower-constant"></a>
## 2. An explicit root-data-free lower bound on the actual c_P

Let b=1 if V has its one exterior root y>2 and b=0 otherwise.
This is an exact branch determined by V's real interlacing; it can also be determined from the sign of Q'(2) when e=0: all other derivative roots are below2, so b=1 exactly when Q'(2)<0.
Put

    Lambda=beta if b=1, and Lambda=1 if b=0,
    C_n=(n-1)^((n-1)/2),
    B_*=h sqrt(Delta)/[C_n (a Lambda)^(n-2)].            (4)

The letter B_* is a bound on a derivative of the squarefree polynomial hR, not the phase symbol |P|^2.
For EVERY circle root eta of R,

    |(hR)'(eta)|>=B_*.

This is L361's Vandermonde cofactor mechanism, with the nonmonic leading factor now explicit.
If R=a product_j(z-alpha_j), then

    1/|R'(eta)|=a^(n-2)
                   |Vandermonde(alpha_j:alpha_j!=eta)|/sqrt(Delta).

The cofactor has n-1 columns1,z,...,z^(n-2).
Hadamard bounds it by C_n product_(alpha_j!=eta)max(1,|alpha_j|)^(n-2).
Every omitted-root product is at most Lambda, since eta is on the circle and the only possible expanding root of R is rho<beta.
This proves(4) after multiplying by h.
It is the retained classical Hadamard/discriminant mechanism from Smy08-U003, adapted directly rather than an invocation of a monic theorem outside its hypotheses.

Use the exact L369 notation: eta_1,...,eta_L are all distinct circle roots of F, with actual multiplicities m_i; gamma_i is its complete nearest-root product and c_P=(2/H)min_i gamma_i.
The root set on the circle is the same for R, and L=n-2b.
The following coefficient-exact lower bounds contain no individual root separation or computed critical root:

    e=0,b=0:  c_P >= (2/H) 2^(-(L-1)) B_*;

    e=0,b=1:  c_P >= (2/H) 2^(-(L-1)) B_* tau_*,
       tau_*=|V(2)|/[a 4^(s-2)(x_0+2)] >0;

    e=1:      c_P >= (2/H) 2^(-(L+1)) B_* delta_*,
       delta_*=min{4, |V(2)|/[a 4^max(t-1,0)]}>0.       (5)

Proof for e=0.
Full factorization gives

    gamma_i=2^(-(L-1)) |F'(eta_i)|
            product_(xi off circle) ||xi|-1|/|eta_i-xi|.

When b=0 the product is empty.
When b=1, write y=rho+rho^-1.
On the circle the product of the two radial distances is y-2, while

    |eta-rho||eta-rho^-1|=y-(eta+eta^-1)<=y+2.

Thus their ratio is at least(y-2)/(y+2).
The COMPLETE nonzero integer endpoint value satisfies

    |V(2)|=a(y-2) product_(other derivative roots u)(2-u)
           <=a(y-2)4^(s-2).

Since y<x_0, the ratio is at least tau_*.
The two off-circle members, the actual leading factor, and the endpoint integer have all been used.
Neither a bound on beta alone nor integrality alone is being mistaken for a uniform gap rho-1.

Proof for e=1.
All R roots are on the circle and F=(z-1)^2(hR).
At eta_i=1,

    gamma_i=2^(-(L-1)) |(hR)'(1)|;

at every other eta_i,

    gamma_i=2^(-(L+1))
                         |(hR)'(eta_i)| |eta_i-1|^2.

The root-1 has squared distance4 from1.
Every other root corresponds to a trace root u of V, so |eta_i-1|^2=2-u.
If t>=1, the complete integer value V(2)=a product_u(2-u) gives2-u>=|V(2)|/(a4^(t-1)).
If t=0 there are only+/-1, and the stated conservative delta_* is still at most4.
Taking the minimum with4 also makes the root+1 formula dominate the common bound in(5).
This proves all cases, including the quartic endpoint degeneracy.
No separation between different interior roots was silently imposed.

In particular(5) yields a genuine degree/measure bound even without evaluating any discriminant.
If1<beta<=B is a fixed upper bracket, set X_B=B+B^-1+2.
Since h sqrt(Delta)>=1, a<=s, Lambda<=B, L<=d, and the positive integer endpoint values have modulus at least1, every branch gives the conservative common bound

    c_P >= [H 2^d d^(d/2) (sB)^(d-2)
                         s 4^(s-2) X_B]^-1.           (6)

For example, the factor tau_* is at least1/[s4^(s-2)X_B]; the delta_* branch is no smaller than that same deliberately weakened factor.
Also

    H <= product_(original roots alpha)(1+|alpha|)
       =2^(d-2)(beta+beta^-1+2)
       <=2^(d-2)X_B.

Thus(6) contains only d and B after that last substitution and proves log(1/c_P)=O_B(d log d) as an upper bound.
Retaining Delta,h and the exact endpoint values in(5) can improve this coarse bound.
It does not turn it into degree-uniform conditioning.
The original L369 formula then gives a fully explicit upper bound on K_P^tr by replacing c_P with the applicable right side of(5) or(6).
No critical root data or numerical scan has been computed.

<a id="salem-nearest-product-exponential-cost"></a>
## 3. The same displayed constant necessarily pays an exponential degree cost

The next inequality is an UPPER bound on the actual c_P.
Consequently better arithmetic lower bounds cannot make this particular constant exceed it.
Put q=1 when b=0, and q=y-2=(rho-1)^2/rho when b=1.
For the exact L369 product,

    c_P <= 2sL q/[H 2^(L-1)].                          (7)

To prove it, let C(z)=product_(i=1)^L(z-eta_i), the monic polynomial of ALL distinct circle roots; C need not be integral.
When e=0, every m_i=1 and the off-circle radial product is q.
Consequently

    gamma_i=s 2^(-(L-1)) q |C'(eta_i)|.

When e=1, b=0 and+1 has multiplicity3.
For eta_i=1 this same formula with q=1 holds.
For eta_i!=1 it is multiplied by |eta_i-1|^2/4<=1.
Therefore in every branch

    min_i gamma_i <=s 2^(-(L-1))q min_i |C'(eta_i)|.

Hadamard on the complete L-by-L Vandermonde with circle rows gives |Vandermonde(eta_1,...,eta_L)|^2<=L^L, because each row has norm sqrt L.
The exact derivative product is product_i|C'(eta_i)|=|Vandermonde|^2, so its minimum is at most L.
This proves(7).
No evenly spaced configuration, root separation, arithmetic positivity or approximation is assumed.

Write m_*=1 for e=0 and m_*=3 for e=1, exactly as in L369, and J=16d+2.
Its specified constant is

    K_P^tr=L/pi+2J pi^(m_*-1)/(2^(m_*)c_P).

Combining this formula with(7) gives the lower bound

    K_P^tr-L/pi
           >= JH pi^(m_*-1)2^(L-1-m_*)/(sLq).           (8)

For1<beta<=B put q_B=max{1,B+B^-1-2}.
We have q<=q_B, d-2<=L<=d, J/s>=32, and pi^(m_*-1)/2^(m_*)>=1/2 in both cases.
Therefore a common, simpler consequence is

    K_P^tr >= 2H 2^d/(d q_B).                          (9)

This is forced even if the roots are otherwise well conditioned.
The penalty comes from L369's EXACT global nearest-root factors, each of which divides an independent distance by2.
The integer discriminant estimate in Section2 supplies a finite upper bound on K_P^tr; it cannot invalidate(7)--(9).
These are bounds on a specified sufficient-bound constant, not lower bounds on |mu_k| or on the best possible constant in a different proof.

For completeness the specific displayed tail certificate in L369 is

    T_N=(m_*+1)K_P^tr N^(-1/(m_*+1)).

For any fixed C>0,A>=0 and1<=N<=C d^A, equations(8)--(9), m_*+1>=2 and1/(m_*+1)<=1/2 give

    T_N >=4H 2^d/[q_B sqrt(C) d^(1+A/2)].               (10)

Hence this particular sufficient tail expression diverges on every bounded-beta, unbounded-degree sequence at every polynomial-degree window.
It cannot certify a fixed small remainder there.
One may choose a different estimate, use the minimum with L368's distinct general canceled-rational constant, or exploit signed tails; none is ruled out by(10).
Optimizing the deleted-arc radius inside the SAME global bound does not repair the early polynomial window: with0<r<=1 its complementary derivative term is at least [2J pi^(m_*-1)/(2^(m_*)c_P)]/k, already exponential over polynomial k by(8).

Any hypothetical genuine Salem sequence with beta->1 necessarily has d->infinity: the coefficient bound H<=2^(d-2)(beta+beta^-1+2) makes the monic integer polynomials of bounded degree and bounded beta finite, whereas a sequence of positive measures tending to zero needs infinitely many distinct inputs.
Thus the near-one obstruction(10) applies conditionally without asserting that such a sequence exists.
When b=1, the additional factor q<=beta+beta^-1-2=4sinh(log(beta)/2)^2 exposes a further actual small-measure expense; it is not canceled by omitting the reciprocal off-circle member.

<a id="actual-plastic-salem-conditioning-control"></a>
## 4. An actual bounded-measure irreducible Salem family exhibits the cost

This obstruction is also realized on an already retained family, without a near-one existence hypothesis.
Use [L131's no-padding progression](../ledger/Yin_L_G0131_v1.md), whose actual irreducible Salem status and complete cyclotomic exclusions reuse [L38](../ledger/Yin_L_G0038_v1.md#family-cyclotomic-factors).
For

    N=120k+9, k>=1,
    P_N=z^(N+3)-z^(N+1)-z^N+1-z^2-z^3,
    d=N+3=2s, H=6,

those fixed inputs have theta<beta_N<4/3 and beta_N->theta>1, with theta the plastic root.
Their whole original polynomial, not a newly selected factor, is used.
The original local Rouche/cyclotomic proof is accepted at its retained scope, rather than newly rerun; the earlier ineffective external Salem-construction threshold is not needed here.

The following arithmetic substitutions are new direct symbolic calculations, not program outputs.
From the six coefficients,

    P_N(1)=-2,      P_N'(1)=-(N+3),
    P_N''(1)=-N^2+5N-2.

Since F=zP'-sP and F'(1)=2Q'(2), this gives

    Q'(2)=(-N^2+14N-1)/4<0.                             (11)

Also P_N(-1)=2, P_N'(-1)=-(N+3), P_N''(-1)=N^2+3N+10.
Here s=60k+6 is even, so F'(-1)=2Q'(-2), yielding

    Q'(-2)=-(N^2+2N+17)/4.

Both endpoint values are explicit nonzero integers.
The coefficient content h is1: the two present consecutive coefficients at z^2,z^3 in F have magnitudes |s-2| and |s-3|, whose gcd is1.
Thus a=s; none of the full leading expense disappears by primitive normalization.

The negative sign in(11) and real interlacing force exactly one derivative trace root y>2, so e=0,b=1,m_*=1,L=d-2.
Its off-circle cost satisfies

    0<q=y-2<x_0-2<4/3+3/4-2=1/12.

Equation(8), H=6 and J/s>=32 consequently give the explicit bound

    K_(P_N)^tr >144 2^d/(d-2).                          (12)

This is an actual genuine irreducible Salem bounded-measure, constant-coefficient-length family with divergent displayed conditioning cost, rather than reducible cyclotomic padding.
The polynomial discriminant and the complete derivative endpoints still satisfy the exact identities above.
It disproves a degree-uniform bound on THIS K_P^tr over the bounded-measure class beta<4/3.
It does not disprove an arbitrarily assigned function of the exact individual beta, a useful restriction sufficiently near1, or a different moment estimate.
Its total measure tends to the fixed positive log(theta), not zero.

<a id="salem-conditioning-outcome-and-freeze"></a>
## 5. Outcome and source/verification boundaries

The completed changed result is a two-sided conditioning account.
Equations(1)--(6) retain the full primitive leading/content, endpoint, discriminant and possible off-circle factors and bound c_P from below without individual critical-root data.
Equations(7)--(10) show that L369's exact global nearest-root constant necessarily loses exponentially with degree, before any exceptional clustering; the actual no-padding Salem family in(11)--(12) witnesses that loss even at H=6 and bounded total measure.
Merely certifying more roots, setting Delta>=1, or tuning a large finite moment cutoff cannot remove this cost.

The discriminant/Hadamard method is attributed at the existing Smy08-U003 and L361 scope.
The trace and critical multiplicities are accepted from L66/L369, and the actual bounded-measure family from L131/L38 with their original proof/source limits.
No new external theorem or unverified separation assertion is a premise.
No original source-proof re-audit, novelty certification, numerical root isolation, finite moment evaluation, mathematical program, J or parameter scan was performed.
The argument is symbolic; subsequent material-format checks are operational checks only.
