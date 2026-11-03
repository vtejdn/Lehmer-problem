---
author: Yin
---
# The complete normalized multiplicity-two cyclotomic gate has no support

Human author Yin.
The same_trace contributor developed AG1--AG7 and authored the complete16-class computation after fixing the earlier coprime5 support certificate.
The [D1 author section](../drafts/Yin_D_G0001.md#full-a2-support-contradiction) is extraction provenance, not a logical input.
The work is under the [current all-strategy continuation](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The reuse check inspected the exact C199v5 complete normalized gate and support bridge, C608's character/target/period proof, the prior coprime15 construction and the proposed complete order25 factor.
The new argument covers all remaining odd orders divisible by5 through exact predivision periodicity and divisor induction; it does not increase a numerical order cutoff or integer lifting modulus.
This material is an open candidate awaiting isolated whole mathematical and native review.
It excludes only the full normalized A_0=2 domain if confirmed and does not claim completion of G0001.

## Statement


Let W_n and Y=product_(n odd,n>1,n!=5)W_n^(b_n) have the exact complete-group meaning in [C608's statement](Yin_C_G0608_v1.md#statement), with arbitrary nonnegative integer multiplicities of finite support.
There is NO such Y satisfying its stated low-X condition and full normalized A_0=2 gate, for either epsilon=0 or epsilon=1.
The claim is about complete groups, not an arbitrary polynomial whose roots form selected partial order orbits.

For the original-input application, let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree2r.
For an original root alpha set delta=alpha+alpha^(-1), assume F=Q(delta) is totally real, and let T in Z[X] be the actual monic degree-r minimal polynomial of delta.
Thus P(z)=z^r T(z+z^(-1)).
Define C_p by C_p(z+z^(-1))=z^p+z^(-p), and use the actual integer polynomials theta_p=rem_T(T(C_p))/p for p=2,3,5.
Assume a=theta_2(delta), b=theta_3(delta), c=theta_5(delta) are all nonzero and, for one sign s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), U=T mod2, R=G mod2 and phi=X^2+X+1.
Assume the normalized circle Haar integral of log(G(z+z^(-1))^2) is0, with its integrable logarithm at circle zeros, and assume

    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U for every irreducible psi|U, psi!=phi.

These are exactly the relevant complete original hypotheses in [C199v5](Yin_C_G0199_v5.md#statement).
Let q be the maximal power of2 for which U is a q-th power in F_2[X], put A=ord_X U, and retain the normalized multiplicity A_0=A/q supplied by C199v5.
The new conclusion excludes A_0=2 for every original q; combined with C199's inherited evenness it leaves A_0>=4 on that full domain.
It does not exclude multiple unsaturated factors, another normalized multiplicity, a positive canonical Haar branch or the unrestricted Lehmer Task.

The exact prior interfaces needed are C608 SG4--SG11: M=X^4phi^8, the character lambda(u)=[X^13](u'/u)+[X^15](u'/u), its vanishing on every complete group of order coprime to5, and its value1 on both possible full-gate targets.
Those fixed inputs were under separate review during the derivation; their selected responsible decisions own their actual status, which this argument does not change.
The new step covers all remaining n divisible by5 without a numerical order cutoff.

## Argument

### Exact predivision period and legitimate unit quotients

Retain phi=X^2+X+1 and the squarefree polynomial B_n of all nonidentity n-th-root traces for odd n.
If5 divides n, the complete order5 factor phi occurs EXACTLY ONCE in B_n.
Indeed z^n-1 has distinct roots in characteristic two because n is odd, and distinct inverse pairs have distinct traces by the quadratic identity z^2+xz+1=0.
There are exactly the two order5 trace values, whose polynomial is phi; no trace from a different odd order can coincide with one of them.
Also B_n(0)=1, so

    D_n=B_n/phi in F_2[X],
    gcd(D_n,X phi)=1 for odd n with5|n.          (AG1)

This quotient is ordinary exact polynomial division, not inversion of phi in a primary quotient.
Let

    M=X^4phi^8,
    M_tilde=X^4phi^9=M phi.                     (AG2)

For the recurrence matrix A=[[X,1],[1,0]], the proved polynomial identities are

    A^8-I=X^4A^4,
    A^5-I=phi[phi A+(X+1)I].

Raise the second identity to the sixteenth power using commuting matrices in characteristic two.
It gives A^80-I divisible by phi^16 and hence by phi^9.
The first identity gives A^80=(A^8)^10=I modulo X^4.
CRT therefore yields A^80=I modulo M_tilde, and the same initial-vector argument for the B_n recurrence gives

    B_(n+160)-B_n divisible by M_tilde
                                      for every odd n>=1.

When5|n, both sides can be divided by the exact polynomial phi, giving

    D_(n+160)=D_n modulo M.                     (AG3)

Dividing first is essential: retaining only B_n modulo M would not give the required precision after division by phi.
The factor X^4 also remains in M_tilde and M, so the quotient's low-X coefficients are retained.
No phi-primary-only approximation or freely chosen quotient unit is substituted for D_n.

### Complete sixteen-class certificate and the order25 candidate

The odd multiples of5 have exactly the16 representatives

    n=5,15,25,...,155 modulo160.

The new finite certificate computes B_n by its exact recurrence modulo M_tilde, divides its canonical representative by phi with zero remainder, and computes D_n prime divided by D_n modulo M.
Because M_tilde is itself divisible by phi, this canonical quotient is exactly the class in (AG1)--(AG3), independent of the discarded multiple of M_tilde.
Every quotient has degree below20 and is a unit by (AG1).
The certificate checks

    lambda(D_n)=0 for all16 representatives.    (AG4)

The complete finite polynomial certificate is as follows; hexadecimal bit j encodes the coefficient of X^j.
For each row, multiplying D_n by its displayed logarithmic derivative modulo M yields D_n prime, and the exact predivision multiplication phi D_n gives B_n modulo M_tilde.

| n | B_n modulo M_tilde | D_n modulo M | D(D_n) modulo M |
| --- | --- | --- | --- |
| 5 | 0x000007 | 0x00001 | 0x00000 |
| 15 | 0x0000d1 | 0x0002b | 0x85b2b |
| 25 | 0x001d0d | 0x0046f | 0x80a3f |
| 35 | 0x037303 | 0x0a66d | 0x05114 |
| 45 | 0x037303 | 0x0a66d | 0x05114 |
| 55 | 0x001d0d | 0x0046f | 0x80a3f |
| 65 | 0x0000d1 | 0x0002b | 0x85b2b |
| 75 | 0x000007 | 0x00001 | 0x00000 |
| 85 | 0x000007 | 0x00001 | 0x00000 |
| 95 | 0x0000d1 | 0x0002b | 0x85b2b |
| 105 | 0x001d0d | 0x0046f | 0x80a3f |
| 115 | 0x037303 | 0x0a66d | 0x05114 |
| 125 | 0x037303 | 0x0a66d | 0x05114 |
| 135 | 0x001d0d | 0x0046f | 0x80a3f |
| 145 | 0x0000d1 | 0x0002b | 0x85b2b |
| 155 | 0x000007 | 0x00001 | 0x00000 |


It records every quotient, inverse and logarithmic derivative, and a separately implemented coefficient-set verifier checks the exact division and inverse using a multiplication linear system.
Neither implementation uses a BFS membership oracle or assumes a subgroup order.
Both are author programs, not independent agent reviews.
The all-order assertion follows from (AG3), not from finite extrapolation.

The order25 row gives explicitly

    D_25=W_25=phi(chi)=Psi=0x46f,
    D(D_25)=0x80a3f modulo M,
    lambda(D_25)=0.                             (AG5)

Here hexadecimal notation encodes polynomial coefficients in bits as in C608.
The equality W_25=phi(chi) also follows from roots: z^5 has primitive order5 exactly when z has order25, and the degree is10 on both sides.
Thus adjoining any multiplicity of the complete order25 group to the earlier coprime5 supports cannot change their character0 to either target's character1.
The general argument below subsumes that particular failed support choice.

### Complete divisor induction and contradiction

The exact partition of all nonidentity n-th roots into their primitive orders gives, for odd n divisible by5,

    D_n=product_(d|n,d>1,d!=5) W_d.             (AG6)

For n=5 this is the empty product D_5=1; phi itself is excluded because it is not a unit modulo M and is already the separately retained distinguished primary factor.
For n>5 divisible by5, solve (AG6) in the UNIT GROUP of F_2[X]/M for W_n by dividing by every proper-divisor factor W_d with d!=5.
All these factors are units: their exact odd order is neither1 nor5.
The character is additive on products and inverses, so induction on n proves lambda(W_n)=0.
The induction starts with the already covered orders coprime to5, and every proper divisor divisible by5 other than5 is strictly smaller than n.
Equation (AG4), extended through (AG3), supplies lambda(D_n)=0 at each step.
This covers arbitrary powers of5 and arbitrary additional odd prime factors, rather than only25 or a bounded list of orders.

Consequently

    lambda(W_n)=0 for every odd n>1,n!=5,
    lambda(Y)=sum_n (b_n mod2)lambda(W_n)=0.     (AG7)

But the full normalized gate and low-X condition force Y to one of C608's two CRT classes, each with character1.
This contradiction proves the complete formal support assertion, and C199v5's complete-group bridge gives its original-input application at every original q.
No existence of an actual T or a smaller normalized characteristic-zero polynomial is assumed to produce the contradiction.

The SAME-T coefficient search on A_0=2 is therefore unnecessary if this candidate is confirmed: its full old support premises already have no solution, before either the C624 first error or the separate K_T error needs to be solved.
This makes no claim that FE5 is independently stronger on another branch or that the unrestricted original-root/Haar comparison is complete.
The present bounded discriminator stops at this full A_0=2 support result and does not begin an A_0>=4 classification.

## Exact inputs and review scope

| Input | Exact use and limitation |
| --- | --- |
| [C608 complete fixed character argument](Yin_C_G0608_v1.md#argument) | SG4--SG11: both full normalized target classes, M and well-defined additive character, complete32-row coprime5 certificate, and every coprime5 complete group. No adoption or independent review of that input is invented here. |
| [C608 formal conditions](Yin_C_G0608_v1.md#statement) | Exact whole-group, low-X and normalized unit-gate domain for the first statement; no arbitrary partial order orbit. |
| [C199v5 original complete theorem](Yin_C_G0199_v5.md#statement) | Only the original-input application: exact residual/field/zero-Haar/unique-unsaturated hypotheses, arbitrary original q, normalized A_0 and its evenness, complete local gate and original layer parity. |
| [C199v5 complete support bridge](Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | The original reduction has Y formed from complete groups of every odd order other than1 and5 with all normalized multiplicities; no individual original integer cyclotomic exponent is divided byq. |
| [J120 exact16-row certificate](../computations/programs/Yin_J_G0120/readme.md#results-and-limits) | Complete native support for AG2--AG5: predivision matrix period, all16 exact quotients, their inverses/logarithmic derivatives/zero character and the order25 case, checked by separate author arithmetic implementations. |

A reviewer must inspect the full exact quotient period, retention of X^4, squarefree/simple phi factor, all16 certificate identities, complete divisor induction including arbitrary5-powers, and the precise original-input transfer.
The existing C608 proof and32-row certificate remain necessary exact inputs at their actual selected scope.
Native reproduction supports only the16 stated rows; all-order coverage is supplied by the complete algebraic reduction above.
No actual T coefficient calculation, full integer Gamma construction, A_0>=4 classification or global Mahler comparison was performed.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:56 |
| status | open |
| reason | Register the complete AG1--AG7 candidate: exact predivision160-period, unit quotients for every odd multiple of5, all16 native certificate rows, full divisor induction and contradiction with both normalized A_0=2 target characters. The proposed conclusion excludes that entire support branch for every originalq, but requires isolated whole review and valid exact upstream inputs before adoption. No unrestricted Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete formal and original-input assertion](#statement) | Nonexistence of a complete-group Y with the full normalized multiplicity-two gate, either parity and arbitrary finite multiplicities, with the exact original common residual, trace-field, zero-Haar, unique-unsaturated and originalq domain. |
| argument | [Complete AG1--AG7 proof](#argument) | Exact simple phi factor, predivision modulus and160-period, all16 quotient/character identities, order25 boundary, full divisor induction over arbitrary5-powers and precise actual-input contradiction. |
| dependency | [Fixed coprime5 character and target proof](Yin_C_G0608_v1.md#argument) | Exact SG4--SG11 interfaces, complete32-row certificate and all-order coprime5 factor argument; no broader source or realization assumption. |
| dependency | [Formal normalized gate contract](Yin_C_G0608_v1.md#statement) | The exact complete-group, low-X and full local-unit conditions referred to by the formal statement. |
| dependency | [Original normalized-domain theorem](Yin_C_G0199_v5.md#statement) | Original-input application only, retaining all fields, residuals, q, zero-Haar/unique-unsaturated hypotheses, normalized evenness and layer parity. |
| dependency | [Exact original complete-group bridge](Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | Original Y has the full group product used in AG6--AG7, with no omitted factor or separately realized normalized polynomial. |
| support | [Entire new finite native certificate](../computations/programs/Yin_J_G0120/readme.md#results-and-limits) | Every16 predivision, quotient, inverse and character calculation plus the matrix-period and order25 checks; two author arithmetic implementations, not independent agent review. |
