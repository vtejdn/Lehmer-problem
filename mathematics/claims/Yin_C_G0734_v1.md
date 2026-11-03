---
author: Yin
---

# Exact low dyadic contributions and the limit of finite-jet parity information

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the complete low B_n/W_n formula, first-term evaluation and three-term cancellation.
The characteristic_zero_bridge agent checked all eight residue cases, complete divisor inversion, source exponents, formal inverse truncations and endpoints, and supplied the precisely scoped finite-jet perturbation.
Root read the entire saved DY1--DY8 argument and finite-jet parity-flip proof.
Both agents are contributors; this open fixed candidate awaits fresh isolated whole review and a separate adoption decision.
No native coefficient expansion, prime search or rank calculation is used.
The source exponent is ell, while j_star independently indexes the large dyadic perturbation; these have distinct quantifiers.

<a id="dg3-fixed-dyadic-contributions"></a>
## Statement

Use the integer trace recurrence C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), with bars for reduction modulo2.
For odd n, B_n is the complete polynomial of traces of nonidentity n-th roots over the algebraic closure of F_2, one per inverse pair, with B_1=1; W_n is the complete primitive order-n trace polynomial for n>1.
Retain the ACTUAL full [C691 DG1--DG8 source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), with

    S_13={3,7,11,19,23,31,43,47,59,67,71,79,83},
    n_-=103 product_(p in S_13)p,
    A=(1/4)product_(p in S_13)(p+1), A_-=104A,
    ell>=82, Q=2^ell, m=Q/4-2,
    k_m=ceil(m/(2A_-)), b_m=k_m A_--m/2,
    H=W_(n_-)^(k_m)W_3^(b_m),
    phi=1+X+X^2, chi=Xphi^2,
    h_Q(X)=1+sum_(i=0)^(ell-1)X^(Q-2^i),
    x=chi^(-1) at0,
    H(X)^(-1)=sum_(j>=0)h_j X^j.

For every actual complete Y supplied at these parameters, put U_0=X^(2m)Y phi^(14m), d=deg U_0, and Lambda(f)=sum_(t>=0)[X^(2^t)]f for a polynomial f over F_2.
The source polynomial h_Q(X) and the scalar coefficient h_j have their distinct displayed meanings.
All inverse series are in F_2[[X]], and every source factor, multiplicity and finite-jet condition is retained.

For EVERY positive odd n,

    B_n=(1+X)^((n^2-1)/8) modulo X^3.

For squarefree odd n>1, the corresponding primitive factor has the integer exponent product_(p|n)(p^2-1)/8 in that same unit group.
For the actual fourteen-prime n_- this gives W_(n_-)=1 modulo X^3, while b_m=1 modulo4.
Consequently H^(-1)=1+X+X^2 modulo X^3 and h_2=1.

The DG3 low class determines U_0 modulo X^(10m), and the only possibly nonzero dyadic coefficient positions strictly below10m are Q/2,Q,2Q.
Their exact values are

    [X^(Q/2)]U_0=h_2=1,
    [X^Q]U_0=h_(Q/4+2),
    [X^(2Q)]U_0=h_(3Q/4+2)+h_(Q/4+2)+h_2.

Thus their sum is h_(3Q/4+2), and the COMPLETE parity is

    Lambda(U_0)=h_(3Q/4+2)
          +sum_(4Q<=2^t<=d)[X^(2^t)]U_0.

The complete degree remains d=30m+deg Y<=14400Q^3+1206Q^2+128Q.
The value h_(3Q/4+2) and every later contribution in the displayed tail remain unevaluated.
By the adopted [C731 support obstruction](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25), Lambda(U_0)=w/2 modulo2 for the full reciprocal binary support size w, and a passing height1 first-bit sign lift requires Lambda(U_0)=0.
The first contribution1 is not a verdict on that total parity or on the three restricted sign systems.

There is also an exact counterexample to determining Lambda from the TWO finite jets alone, in an explicitly wider polynomial domain.
For every dyadic L=2^j_star>max(d,60m), define

    Y_tilde=Y+X^(L-2m)phi^(16m),
    U_tilde=X^(2m)Y_tilde phi^(14m).

Then Y_tilde is monic, prime to Xphi, and has the same low class modulo X^(8m) and high class modulo phi^(16m) as Y.
Its actual degree is L+30m, the difference U_tilde-U_0=X^L phi^(30m) has degree L+60m<2L, and Lambda(U_tilde)=Lambda(U_0)+1.
This perturbation is NOT asserted to satisfy completeness, either forward divisibility, the multiplicity floor, the fresh-factor requirement or the original C691 degree budget.
Its canonical identity and nonzero G are not asserted.
Freedom of parity among admissible COMPLETE C691 representatives, actual support parity, sign feasibility, original irreducibility and higher precision all remain unresolved.

## Complete argument

Retain EVERY parameter and full factor of C691: ell>=82, Q=2^ell, m=Q/4-2, n_-=103 product_(p in S_13)p with the fourteen stated distinct odd primes, A_-=104A, k_m=ceil(m/(2A_-)), b_m=k_m A_--m/2, and

    H=W_(n_-)^(k_m) W_3^(b_m),
    U_0=X^(2m)Y phi^(14m), d=deg U_0,
    phi=1+X+X^2, chi=Xphi^2=X+X^3+X^5,
    h_Q(X)=1+sum_(i=0)^(ell-1) X^(Q-2^i),
    x=chi^(-1) at0,
    H(X)^(-1)=sum_(j>=0)h_j X^j.                 (DY1)

The source polynomial h_Q is distinct from the scalar coefficients h_j.
All series operations here are in F_2[[X]], with constant-one units and the stated compositional inverse.
For every actual full Y representing C691 DG3, the conclusions are

    h_2=1,
    [X^(Q/2)]U_0=h_2,
    [X^Q]U_0=h_(Q/4+2),
    [X^(2Q)]U_0=h_(3Q/4+2)+h_(Q/4+2)+h_2,
    sum_(2^t<10m)[X^(2^t)]U_0=h_(3Q/4+2).       (DY2)

The sum includes only the three possibly nonzero dyadic positions Q/2,Q,2Q; all smaller positions vanish.
Neither h_(3Q/4+2) nor the total dyadic coefficient sum is evaluated by this statement.

### Complete trace factors to order two

For any positive odd n let r=(n-1)/2.
The full C608 Laurent identity and injective trace substitution give

    B_n=1+sum_(j=1)^r C_jbar.

Indeed multiplying the right side after trace substitution by z^r gives the complete geometric sum1+z+...+z^(n-1), which equals(z^n+1)/(z+1) in characteristic2.
This retains every nonidentity odd-order trace and also includes B_1=1.
For j=2^t v with v odd, C_jbar=C_vbar^(2^t), the odd polynomial C_v has only odd-degree monomials, and its linear coefficient is1.
The last assertion follows from differentiating the Chebyshev recurrence at0 as in the explicit HS14 proof; even-index constant terms are zero modulo2 and C_1'(0)=1.
Thus the coefficient of X in B_n counts odd j in[1,r], while the coefficient of X^2 counts j=2 modulo4 in that interval.
These counts are respectively ceil(r/2) and floor((r+2)/4), reduced modulo2.

Put E_n=(n^2-1)/8=r(r+1)/2, an ordinary nonnegative integer.
Its residue modulo4 and the two counts agree with the coefficients of(1+X)^(E_n), as this complete eight-case table shows:

| n modulo16 | E_n modulo4 | [X]B_n | [X^2]B_n |
| --- | --- | --- | --- |
| 1 | 0 | 0 | 0 |
| 3 | 1 | 1 | 0 |
| 5 | 3 | 1 | 1 |
| 7 | 2 | 0 | 1 |
| 9 | 2 | 0 | 1 |
| 11 | 3 | 1 | 1 |
| 13 | 1 | 1 | 0 |
| 15 | 0 | 0 | 0 |

Each entry follows from the two displayed integer counts; shifting r by8 preserves their parity and preserves E_n modulo4, so the table covers EVERY positive odd n.
Since(1+X)^4=1 modulo X^3, it follows that

    B_n=(1+X)^((n^2-1)/8) modulo X^3.            (DY3)

The adopted complete divisor partition gives, for squarefree odd n>1,

    W_n=product_(e|n) B_e^(mu_Mob(n/e)).

Here mu_Mob is the ordinary divisor sign, distinct from any coefficient parameter; inverse signs are interpreted only in the constant-one unit group modulo X^3 or in formal series.
No constructed polynomial H receives a negative factor multiplicity.
Using DY3, the total integer exponent is

    sum_(e|n) mu_Mob(n/e)(e^2-1)/8
       =(1/8)product_(p|n)(p^2-1).              (DY4)

The constant terms cancel because the divisor signs sum to0 for n>1, and the remaining product is the direct expansion obtained by choosing each prime divisor in or out.
For n=n_- there are fourteen distinct odd primes, each with p^2-1 divisible by8.
The integer in DY4 is therefore divisible by2^39, in particular by4, giving

    W_(n_-)=1 modulo X^3.

Also W_3=1+X exactly.
The integer A from C691 is integral, and A_-=104A is divisible by4.
Since m/2=Q/8-1 is3 modulo4 for ell>=82,

    b_m=k_m A_--m/2=1 modulo4.

It follows that

    H=1+X modulo X^3,
    H^(-1)=1+X+X^2 modulo X^3,
    h_2=1.                                      (DY5)

This evaluates the first contribution without evaluating any full Y coefficient list or the later parity terms.

### The exact DG3 range and the inverse-composition truncation

C691 DG3 says

    Y=phi^(-14m)H^(-2)h_Q(x)^(-2) modulo X^(8m).

Multiplying by the actual unit phi^(14m) and then by X^(2m) gives the exact low class

    U_0=X^(2m)[H^(-1)h_Q(x)^(-1)]^2
                                             modulo X^(10m). (DY6)

Thus the coefficients strictly BELOW10m=5Q/2-20 are fixed by this class.
For Q>=2^82 one has Q/4<2m=Q/2-4<Q/2 and2Q<10m<4Q.
Consequently the only possibly nonzero positive2-power positions in the determined range are EXACTLY Q/2,Q,2Q.
The full degree d=30m+deg Y exceeds2Q, so all three are actual polynomial coefficient positions.

Set J=3Q/4+2.
One has J<4m=Q-8, so the squared class in DY6 supplies all three needed square-root coefficients through J.
The inverse equation chi(x)=X gives x=X+O(X^3).
The two lowest-order terms of h_Q(x)-1 satisfy

    x^(Q/2)=X^(Q/2)+O(X^(3Q/2)),
    x^(3Q/4)=(x^3)^(Q/4)
             =X^(3Q/4)+O(X^(5Q/4)).

These use Frobenius powers Q/2 and Q/4 and x^3=X^3+O(X^5), not a low-order Taylor approximation applied beyond its range.
Every other summand x^(Q-2^i) has order at least7Q/8.
All three error bounds3Q/2,5Q/4,7Q/8 are strictly greater than J; for the smallest one this uses Q/8>2.
Hence

    h_Q(x)=1+X^(Q/2)+X^(3Q/4) modulo X^(J+1).

The square of its nonconstant part has order at least Q>J, so the inverse geometric series has only its constant and linear parts in that same exact quotient:

    h_Q(x)^(-1)=1+X^(Q/2)+X^(3Q/4)
                                      modulo X^(J+1). (DY7)

Writing f=H^(-1)h_Q(x)^(-1), DY6 extracts

    [X^(Q/2)]U_0=[X^2]f=h_2,
    [X^Q]U_0=[X^(Q/4+2)]f=h_(Q/4+2),
    [X^(2Q)]U_0=[X^J]f
                     =h_J+h_(Q/4+2)+h_2.

The first two indices are below Q/2, and at J the two shifts in DY7 leave exactly Q/4+2 and2.
Adding these three coefficients in F_2 cancels the two repeated terms, proving DY2 with its precise endpoint range.

### The complete parity still contains every later dyadic position

Define Lambda(U_0)=sum_(t>=0)[X^(2^t)]U_0, a finite sum through degree d.
The exact decomposition supplied here is

    Lambda(U_0)=h_(3Q/4+2)
          +sum_(4Q<=2^t<=d)[X^(2^t)]U_0.        (DY8)

The later sum is not removed, normalized or replaced by a chosen root subset.
The same full degree bound d<=14400Q^3+1206Q^2+128Q from C691 applies.
The support-parity connection to a height1 first-bit lift is the separately fixed [C731 interface](Yin_C_G0731_v1.md#height-one-zero-trace-support-obstruction), still at its actual selected assessment.
Evaluating h_2=1 does not imply Lambda(U_0)=1, and even evaluating the determined three-term sum would leave every displayed later contribution.
This work neither computes the restricted sign-matrix ranks nor constructs or excludes a passing irreducible height1 source.

<a id="finite-jets-do-not-fix-global-dyadic-parity"></a>
### Both finite jets alone allow a parity flip outside the admissible-completion claim

There is a precise algebraic reason not to infer the total parity from the two finite classes alone.
Starting with any fixed actual Y above, choose a dyadic L=2^j_star with

    L>max(d,60m),
    Y_tilde=Y+X^(L-2m)phi^(16m),
    U_tilde=X^(2m)Y_tilde phi^(14m).

Then Y_tilde has exactly the SAME low class modulo X^(8m) and high class modulo phi^(16m) as Y.
Indeed L-2m>58m>=8m, while the other added factor is explicitly divisible by phi^(16m).
It is still prime to Xphi, and it is monic of actual degree L+30m, because the added monic polynomial has that degree, greater than deg Y.
The corresponding full polynomial difference is

    U_tilde-U_0=X^L phi^(30m),
    deg(U_tilde-U_0)=L+60m<2L.

Its only positive2-power coefficient position is L: lower positions lie below its valuation, and the next one2L exceeds its degree.
Its coefficient at L is1, since phi(0)=1.
Therefore

    Lambda(U_tilde)=Lambda(U_0)+1.

This is an exact statement about polynomials satisfying the TWO finite jets and the unit conditions only.
It does NOT establish that Y_tilde is a complete-factor representative, satisfies either global forward divisibility, retains all multiplicity floors or the required fresh factor, or obeys the original C691 degree budget.
In particular the required canonical identity and nonzero G for a new complete source are not inferred for Y_tilde.
Thus it proves that the finite jets alone do not determine total parity, while freedom of that parity among ACTUALLY ADMISSIBLE complete C691 representatives remains unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision fixed-dyadic-contributions-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:25 |
| status | open |
| reason | Register the complete DY1--DY8 and finite-jet perturbation author argument after whole contributor reading. The actual first contribution is1; the three dyadic coefficients fixed by DG3 have the stated exact values and sum, with every later full-source contribution retained. A separate explicit polynomial perturbation proves only that the two finite jets and unit conditions do not determine global parity; it is not an admissible-completion construction. Actual total parity, higher coefficient, restricted sign ranks and original realization remain unresolved. Fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire low-contribution and finite-jet boundary statement](#statement) | Every ell>=82 and actual complete source Y, exact B/W low coefficients, first contribution1, all three determined dyadic terms and their cancellation, full degree and unevaluated tail, adopted support connection, and explicitly wider-domain parity perturbation with all missing admissibility conditions. |
| argument | [Complete DY1--DY8 and perturbation proof](#complete-argument) | Complete Laurent expansion, all eight residue classes, integer divisor exponent, fourteen-prime and b_m valuation, exact DG3 multiplication and inverse-composition truncations, every strict endpoint, full-tail decomposition, and both-jet/unit/degree/one-coefficient perturbation proof. |
| dependency | [Adopted complete canonical source and finite classes](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG3 actual negative-character whole H, fourteen-prime n_-, A_-/k_m/b_m and Q/m values, full formal low unit and both finite jets; DG8 full degree costs. Complete Y remains the actual source, and no integer residual or irreducibility existence is imported. |
| dependency | [Adopted complete B/W Laurent and divisor identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | SG6 Laurent trace identity, injective substitution and B_1/B_3, plus SG8 disjoint complete divisor partition and its exact unit-group inversion only. Its separate finite native certificate, support obstruction and gate conclusions are not premises. |
| dependency | [Adopted whole-factor prime and integer parameter interface](Yin_C_G0665_v1.md#decision-whole-reviewed-2026-10-24) | LH2 thirteen distinct odd primes and integral A, together with the complete constant-one B/W definitions, W_3=1+X and direct divisor-inversion interpretation in Section1. The older positive-character m-family is not substituted for C691's actual negative-character family. |
| dependency | [Adopted full-source height1 support obstruction](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25) | HS12--HS15 actual support w, Lambda(U_0)=w/2 modulo2, necessary w divisible4, source first-coefficient expression and original height1 scope. Only this connection is used; neither its three affine systems nor this new low-term calculation is asserted feasible or inconsistent. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:31 |
| status | proved |
| reason | Adopt the entire DY1--DY8 and finite-jet perturbation theorem after fresh isolated whole R954 PASS. Root read the complete author proof and fixed standalone statement and the complete independent finding. All odd-n trace factors, full divisor inversion, actual h2=1, exact three controlled dyadic coefficients and their sum, every formal inverse endpoint and the full unevaluated tail are supported. The retained numerical degree belongs to the actual bounded DG8 complete source. The wider polynomial perturbation preserves both finite jets and flips parity, but does not establish admissible complete-source parity freedom or preserve the global forward/multiplicity/canonical conditions. The remaining h_J, full tail, total parity, restricted signs, irreducibility and higher residual feasibility remain unresolved. No unrestricted G0001 completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire low-contribution and finite-jet boundary statement](#statement) | Every ell>=82 and actual complete source Y, exact B/W low coefficients, first contribution1, all three determined dyadic terms and their cancellation, full degree and unevaluated tail, adopted support connection, and explicitly wider-domain parity perturbation with all missing admissibility conditions. |
| argument | [Complete DY1--DY8 and perturbation proof](#complete-argument) | Complete Laurent expansion, all eight residue classes, integer divisor exponent, fourteen-prime and b_m valuation, exact DG3 multiplication and inverse-composition truncations, every strict endpoint, full-tail decomposition, and both-jet/unit/degree/one-coefficient perturbation proof. |
| dependency | [Adopted complete canonical source and finite classes](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG3 actual negative-character whole H, fourteen-prime n_-, A_-/k_m/b_m and Q/m values, full formal low unit and both finite jets; DG8 full degree costs. Complete Y remains the actual source, and no integer residual or irreducibility existence is imported. |
| dependency | [Adopted complete B/W Laurent and divisor identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | SG6 Laurent trace identity, injective substitution and B_1/B_3, plus SG8 disjoint complete divisor partition and its exact unit-group inversion only. Its separate finite native certificate, support obstruction and gate conclusions are not premises. |
| dependency | [Adopted whole-factor prime and integer parameter interface](Yin_C_G0665_v1.md#decision-whole-reviewed-2026-10-24) | LH2 thirteen distinct odd primes and integral A, together with the complete constant-one B/W definitions, W_3=1+X and direct divisor-inversion interpretation in Section1. The older positive-character m-family is not substituted for C691's actual negative-character family. |
| dependency | [Adopted full-source height1 support obstruction](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25) | HS12--HS15 actual support w, Lambda(U_0)=w/2 modulo2, necessary w divisible4, source first-coefficient expression and original height1 scope. Only this connection is used; neither its three affine systems nor this new low-term calculation is asserted feasible or inconsistent. |
| review | [Fresh independent whole dyadic-contribution finding](../audits/reviews/Yin_R_G0954_v1.md#whole-dyadic-contribution-finding) | Entire fixed statement, DY1--DY8 and complete wider-domain finite-jet parity flip, exact complete-source and bounded-witness inputs, all coefficient/truncation endpoints, full tail and admissibility exclusions. |

