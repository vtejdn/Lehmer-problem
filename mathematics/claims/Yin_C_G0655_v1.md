---
author: Yin
---
# The actual top-layer norm correction and multiplicity-thirty-two exclusion

Human author Yin.
Root proposed evaluating the refined finite character on the actual full target, including its surviving quadratic determinant term, and the bounded multiplicity-thirty-two hand classification.
The same_trace contributor checked the exact completed lifts, all determinant orders and residue blocks, original layer index and integer value, calibrated character formula, dyadic congruence and complete bounded application.
Both are mathematical contributors, not independent reviewers of this new argument.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes the work.
Focused reuse inspected the full C649/C650 target and original layer identity, C652's calibrated base norm and complete bounded degree-three list, and C654's lift-independent refined finite character.
The new result evaluates precisely the top quadratic term left unresolved in C654; it does not alter the fixed predecessors or assume extra actual coefficients.
No native mathematical computation, support scan or enumeration outside the stated hand degree bound is used.
The [D1 top-norm section](../drafts/Yin_D_G0001.md#actual-top-quadratic-norm-candidate) is development provenance, not a logical dependency.
This statement is initially open for fresh isolated whole mathematical review.

## Statement

### The complete original domain and fixed canonical data

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For an original root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Define C_p by C_p(z+z^(-1))=z^p+z^(-p), and use the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2 and R_can=G_can mod2.
Assume the normalized circle Haar mean of log(G_can(z+z^(-1))^2), using the integrable logarithm at zeros, is0.
Put phi=X^2+X+1 and assume

    ord_phi R_can<ord_phi U,
    ord_psi R_can>=ord_psi U for every irreducible psi dividing U,
                                               psi!=phi.

Let q=2^k be the ACTUAL maximal power of2 for which U is a q-th power, retaining the canonical U=U_0^q and R_can=R_0^q.
Write A_0=ord_XU/q=2m and chi=Xphi^2, and retain the SAME complete canonical data

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3)=X^(2m)Yphi^(12m)B,
    H_0=X^(2m)Y, V_0=H_0B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m), D_0=V_0+C_00^3.

Here Y is monic prime to Xphi, and B is the unique COMPLETE monic phi-unit complement of degree below4m, with every saturated surplus and extra remainder factor.
The adopted homogeneous classification gives

    m even,
    B=X^(Q-m)H(chi),
    Q a power of2, 2m<Q<5m,
    H in F_2[t], H(0)=1, 5deg H<5m-Q.                      (T1)

The symbol Q is the endpoint exponent, distinct from the original maximal Frobenius power q.

For n>=3 define the integer trace polynomial F_n by Phi_n(z)=z^(phi(n)/2)F_n(z+z^(-1)), with phi(n) Euler's totient.
Retain the actual integer factorization and all original layers

    G_can=V_int product_(b>=0)F_(2^b*5)^(a_b),
    a_b>=0 integers of finite support,
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq,
    a_b=0 whenever lambda_b>8mq,
    S_star=sum_(a_b odd,4mq<lambda_b<12mq)
       X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                          phi^(12m-lambda_b/q).

The sign and all other integer factors remain in V_int; none of the a_b is divided by q or reassigned.
Define the exact finite polynomial

    Sigma(t)=sum_(a_b odd,4m<lambda_b/q<=8m)
                         t^(6m-lambda_b/(2q)),
    epsilon=[t^(2m)]Sigma(t).                              (T2)

Thus Sigma lies in t^(2m)F_2[t].
If m is not a power of2, epsilon=0.
If m=2^j, then

    epsilon=a_(k+j+4) in{0,1},
    sum_(b!=k+j+4)a_b lambda_b=(12-8epsilon)mq.             (T3)

The first equality is the actual INTEGER exponent of the original layer lambda=8mq, not merely a free parity parameter.

### The full known CRT and the refined character value

Let x(t) be the formal inverse of chi at0 and, for Q=2^e, put

    h_Q(X)=1+sum_(i=0)^(e-1)X^(Q-2^i),
    Ltilde(t)=[phi(t)^(7m)H(t)h_Q(x(t))]^(-1).

Choose J with2^J>=8m and2^J congruent to Q modulo3, and let beta=X^(2^J) modulo phi^(8m).
The adopted full gate supplies the SAME actual Y and corrected root

    Y=Ltilde(X^2) modulo X^(4m),
    Y=X^(-2m)B^(-7)+beta X^(-2m)B^(-13)S_star
                                             modulo phi^(8m),
    Z_0=beta^2B^(-1)(1+beta B^(-6)S_star)
                                             modulo phi^(6m). (T4)

The exact root satisfies Z_0^11=H_0C_00^2 at6m, the old relation is H_0^6=C_00^21 at8m, and the full gate is Z_0D_0+H_0V_0S_star=0 at8m.
The correction at root precision is retained; this result does not replace that equation by a shorter root.

Put

    N=4m, K_N=2^ceil(log_2(N+1)).

Thus K_N is the least power of2 STRICTLY greater than N; it is unrelated to the field K.
Use the C652 character ell:1+tF_2[[t]]->Z_2, normalized by ell(1+t)=1, with kernel consisting of h(t)^5/h(chi(t)).
Use the C654 completed-pair character

    Phi(u,v)=ell(N_high(v))-(4/5)ell(u),
    Pi_N=Phi/2 modulo K_N/2,

where N_high is the rank-four high-branch norm of chi(X)=t, and Pi_N is defined on F_2[X]/chi(X)^N independently of EVERY lift.
For the actual full target (T4),

    Phi(Y)=(-330m+74Q-660ell(H))/25+epsilon N
                                                  modulo K_N,
    Pi_N(Y)=(-165m+37Q-330ell(H))/25+epsilon N/2
                                                  modulo K_N/2. (T5)

The denominators5 and25 are odd units in Z_2.
The expression Phi(Y) modulo K_N refers equally to any completed lift of the actual class; no higher actual coefficient is stipulated.
Complete support requires Pi_N(Y)=0.

If m is not dyadic, K_N equals the old least power of2 at least4m, epsilon=0, and (T5) gives exactly C652's earlier necessary condition.
If m is dyadic, then Q=N=4m, K_N=8m, and the new necessary condition is

    ell(H)=-m/2+m epsilon modulo2m.                        (T6)

Thus epsilon0 requires -m/2, while epsilon1 requires +m/2, in the SAME residue group modulo2m.
This is only a necessary relation between the original top layer and the complete complement; it is not sufficient complete-group membership or an original realization.

### The multiplicity-thirty-two consequence and retained costs

No original input in this domain has A_0=32.
At that value m=16, Q=64 and deg H<=3; the eight complete degree-bounded possibilities and their characters are

| H | ell(H) |
| --- | --- |
| 1 | 0 |
| W_3=1+t | 1 |
| W_3^2 | 2 |
| W_5=1+t+t^2 | -1 |
| W_3^3 | 3 |
| W_3W_5 | 0 |
| W_7=1+t^2+t^3 | 2 |
| W_9=1+t+t^3 | -3 |

None has residue8 or24 modulo32, so both actual epsilon values fail (T6).
Intersecting with the adopted prior remaining set gives

    A_0 in{24,28} union {4j:j>=9}.                         (T7)

In particular A_0=24 and28 are NOT excluded by this theorem, and no remaining value is asserted to occur.
All canonical costs remain

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(5m-Q-5deg H)>0.                                 (T8)

The original maximal q, nonsquare U_0/R_0, complete canonical remainder, all integer layers, fields and characteristic-zero residual equations remain unchanged.
There is no inference of a global square from a finite jet, all-depth kernel equality, smaller original input, arbitrary-H degree estimate or unrestricted Task completion.

## Argument

### 1. Exact original layers and the legal completed lift

The adopted C650 theorem eliminates all actual layers above8mq and proves the homogeneous description (T1).
Its exact identity for an occurring ell_b=lambda_b/q is

    X^(6m)S_(ell_b)=chi^(6m-ell_b/2)(1+phi^ell_b),
    X^(6m)S_(ell_b)-chi^(6m-ell_b/2)
                       =X^(6m-ell_b/2)phi^(12m).

Summing gives X^(6m)S_star=Sigma(chi) modulo phi^(12m), with every original odd layer retained.
The exponents in Sigma are distinct because the high-window lambda_b are distinct powers of2.
Its coefficient at2m comes precisely from ell_b=8m.
Such an index exists only if m is dyadic: the high window excludes lambda_0=lambda_1=1, and q is itself a power of2.
For m=2^j its exact index is b=k+j+4.
The original weight inequality a_b(8mq)<=12mq gives a_b<=1, so its parity equals the actual integer epsilon.
Removing this actual weight proves (T3).

Factoring (T4) and using the exact layer identity gives the known high class

    Y=X^(5m-7Q)H(chi)^(-7)
      [1+beta X^(-6Q)H(chi)^(-6)Sigma(chi)] modulo phi^(8m).

In C652's high algebra choose the cube-one unit tau with residue X^2 modulo phi.
Its power tau^(2Q) is the exact cube-one lift of beta, since X^(4Q)=X^Q in F_4.
Choose the following FULL completed pair, using t=chi(X) on the high branch:

    u(X)=Ltilde(X)^2,
    v(X)=X^(5m-7Q)H(t)^(-7)(1+Sigma(t)a),
    a=tau^(2Q)X^(-6Q)H(t)^(-6).                            (P1)

It agrees with the actual Y modulo X^N and phi^(2N), respectively.
Its higher coefficients are merely a chosen lift, not additional original data.
The adopted C654 theorem proves that Phi modulo K_N and Pi_N are independent of EVERY such choice.
Thus computation of (P1) at the useful norm precision is legitimate without strengthening any original jet.

### 2. The rank-four quadratic term

C652 proves

    Tr_high(a)
       =H(t)^(-6)Tr_high(tau X^(-3))^(2Q)
       in t^(2Q)F_2[[t]],                                (P2)

because Tr_high of every integral high element lies in t and2Q is a power of2.
In particular2Q>N.
Modulo t, the high algebra is F_2[X]/phi^2, with two successive F_4 residue blocks.
The residue of a is X^Q: H(0)=1, X^(-6Q)=1 in F_4, and tau^(2Q) has residue X^(4Q)=X^Q.
It is a nontrivial cube root because Q is a power of2 and hence not divisible by3.
Multiplication by this residue on either F_4 block has characteristic polynomial Z^2+Z+1 over F_2.
Consequently the rank4 multiplication characteristic polynomial modulo t is

    (Z^2+Z+1)^2=Z^4+Z^2+1.

If e_i(a) denotes its ith elementary coefficient, this proves e_2(a)=1 modulo t.
Possible off-diagonal nilpotent blocks do not change the product of the two diagonal characteristic polynomials.

The determinant expansion is exactly

    N_high(1+Sigma a)
       =1+Sigma e_1(a)+Sigma^2 e_2(a)
             +Sigma^3 e_3(a)+Sigma^4 e_4(a).               (P3)

Here e_1(a)=Tr_high(a).
Since ord_t Sigma>=2m, (P2) makes the linear term have order at least2m+2Q>N.
Terms of degree at least3 have order at least6m>N.
Finally Sigma=epsilon t^(2m)+O(t^(2m+1)), so

    Sigma^2 e_2(a)=epsilon t^(4m) modulo t^(4m+1).

Therefore the FULL high-branch norm correction is

    N_high(1+Sigma a)=1+epsilon t^N modulo t^(N+1).         (P4)

This retains the quadratic term omitted legitimately at the previous, lower t^N precision.
No original lower layer is discarded: its contribution is included in Sigma and the order estimates above show why it cannot affect this one coefficient.

### 3. Calibration of the whole norm ratio

The exact simple/high factorization gives N_high(X)=t/x(t)=phi(x(t))^2.
Thus, for the completed lift (P1), its norm ratio divided by its low component is

    [Ltilde(x(t))/Ltilde(t)]^2
       phi(x(t))^(10m-14Q)H(t)^(-28)
       N_high(1+Sigma a).                                 (P5)

The adopted calibration is

    ell(phi)=-1, ell(h_Q)=Q/2,
    ell(f(x))=ell(f)/5,
    ell(Ltilde)=7m-ell(H)-Q/10.

Accordingly the character of the FIRST three factors of (P5), as exact formal units, is

    2(1/5-1)(7m-ell(H)-Q/10)
       -(10m-14Q)/5-28ell(H)
       =(-330m+74Q-660ell(H))/25.                         (P6)

This base expression is exact and not limited to the old t^N modulus.
C652's finite character rule applied to (P4) determines the correction modulo K_N from its jet modulo t^(N+1).
If epsilon=0 it is0.
If epsilon=1, the actual layer argument in Section1 implies m and N are dyadic, so1+t^N=(1+t)^N and ell(1+t^N)=N exactly.
Thus its correction is epsilon N modulo K_N, proving the first line of (T5).
The whole character is even by C654, so division by2 gives the second line at modulus K_N/2.
No assertion is made that ell(1+t^N)=N for nondyadic N; such an extension is unnecessary because the actual coefficient is0 there.

The SAME actual Y has finite complete membership at N by C654's composition-removal theorem applied to actual complete V_0=X^(m+Q)YH(chi).
Hence Pi_N(Y)=0, establishing the required vanishing of (T5).
Alternatively C652's exact complete V_0 norm bridge gives the vanishing character before passage to the finite quotient; neither route requires global completeness of Y or H individually.

### 4. The dyadic condition and original top weight

When m is not dyadic, N is not a power of2, so K_N is the least power of2 at least N and epsilon=0.
Equation (T5) is therefore exactly C652's existing condition at its original modulus.

When m is dyadic, the only power of2 strictly between2m and5m is Q=4m=N, and K_N=8m.
Vanishing of the second line of (T5) becomes

    (-17m-330ell(H))/25+2m epsilon=0 modulo4m.

The actual m is even.
Multiplying by25 and dividing by2 gives

    165ell(H)=-17m/2+25m epsilon modulo2m.                 (P7)

The coefficient165 is odd, so the solution for ell(H) modulo2m is unique.
Substitution of ell(H)=-m/2+m epsilon changes the two sides by

    -74m+140m epsilon=2m(-37+70epsilon),

which is divisible by2m.
This proves (T6) without dropping the odd coefficient or altering its modulus.
Its epsilon is the actual integer from (T3), with the exact remaining integer weight stated there.
All other canonical and root/gate constraints remain imposed; the character condition is necessary only.

### 5. The complete authorized hand case and degree accounting

At A_0=32 one has m=16, Q=64, and5deg H<80-64=16, hence deg H<=3.
The entire constant-one monic polynomial list at this degree is the eight-item list already proved in C652.
For completeness the only degree1 irreducible is1+t, the only irreducible quadratic is phi, and the only constant-one irreducible cubics are1+t^2+t^3 and1+t+t^3, since a cubic is irreducible exactly when it has no F_2 root.
Factoring the reducible cases yields exactly the eight displayed H, with no omitted high coefficient.
The adopted calibration gives their characters0,1,2,-1,3,0,2,-3.
For epsilon0, (T6) requires -8=24 modulo32; for epsilon1 it requires8 modulo32.
No listed character meets either value.
Thus the entire original A_0=32 branch is impossible for every actual q and every original lower-layer multiplicity.

Only this authorized hand degree range is classified here.
Removing32 from C652's adopted necessary set{24,28,32,36,...} gives (T7), keeping24 and28 explicitly.
The canonical formulas from C652 give (T8) directly, since deg B=Q-m+5deg H.
Chosen completed lifts and finite complete-factor representatives do not replace the original Y, H, T or fields and cannot change these actual degree costs or the maximal q.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:33 |
| status | open |
| reason | Register the complete actual top-quadratic norm formula at the C654 lift-independent finite precision, exact original layer0/1 identification and weight, dyadic signed H-character condition, and full A0=32 hand exclusion. All original fields/canonical data/q/layers/root/gate/costs remain; A0=24/28 stay unresolved. No native calculation, all-depth kernel equality, sufficiency or Task completion is asserted. The analytical author proof requires fresh isolated whole mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual refined-character statement](#statement) | T1--T8: explicit original domain, full canonical data and Q/H, actual Sigma/epsilon/index/weight, full known jets/root, refined character, dyadic condition and exactly A0=32 consequence with retained costs. |
| argument | [Whole analytical proof](#argument) | All five sections, exact layer identity and legal completed lift, rank4 determinant including its quadratic coefficient, calibrated base and corrected norm, precise dyadic congruence, exhaustive hand factorization and original cost boundaries. |
| dependency | [Actual upper-layer and homogeneous gate](Yin_C_G0650_v1.md#statement) | Same original hypotheses, actual maximal q/canonical factors, vanishing upper integer layers, complete Q/H form and exact layer-composition identity. |
| dependency | [Full homogeneous CRT and corrected root](Yin_C_G0649_v1.md#statement) | Both full actual Y jets, original8m gate and6m root correction, with complete coefficients retained. |
| dependency | [Calibrated norm and original complement interface](Yin_C_G0652_v1.md#statement) | Exact ell/Theta calibration, h_Q identity, high norm/trace algebra and base expression, full original group bridge/costs, adopted prior range and complete degree-at-most3 H list. |
| dependency | [Refined finite norm and all-lift independence](Yin_C_G0654_v1.md#statement) | Pi_N on the SAME chi^N quotient, even character and strict-next-power precision, original finite Y membership without separate global completeness. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:43 |
| status | proved |
| reason | Adopt the entire T1--T8 theorem after main reading of complete C655 and isolated whole R868. The legal completed lift retains exactly the actual known CRT class; its full rank4 determinant leaves the quadratic correction1+epsilon t^(4m) at the refined precision. The character formula, original integer top-layer index/value/weight and precise dyadic congruence are established without extra original coefficients or finite-kernel sufficiency. The exhaustive degree-at-most3 list excludes the entire original A0=32 branch for both actual top-layer choices and all lower layers. The necessary remaining set is{24,28} union{4j:j>=9}; those values are not asserted to occur. All original q, fields, canonical remainder, corrected root, full gate and degree costs remain. No native work, new kernel equality or unrestricted completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire actual refined-character statement](#statement) | T1--T8: explicit original domain, full canonical data and Q/H, actual Sigma/epsilon/index/weight, full known jets/root, refined character, dyadic condition and exactly A0=32 consequence with retained costs. |
| argument | [Whole analytical proof](#argument) | All five sections, exact layer identity and legal completed lift, rank4 determinant including its quadratic coefficient, calibrated base and corrected norm, precise dyadic congruence, exhaustive hand factorization and original cost boundaries. |
| dependency | [Actual upper-layer and homogeneous gate](Yin_C_G0650_v1.md#statement) | Same original hypotheses, actual maximal q/canonical factors, vanishing upper integer layers, complete Q/H form and exact layer-composition identity. |
| dependency | [Full homogeneous CRT and corrected root](Yin_C_G0649_v1.md#statement) | Both full actual Y jets, original8m gate and6m root correction, with complete coefficients retained. |
| dependency | [Calibrated norm and original complement interface](Yin_C_G0652_v1.md#statement) | Exact ell/Theta calibration, h_Q identity, high norm/trace algebra and base expression, full original group bridge/costs, adopted prior range and complete degree-at-most3 H list. |
| dependency | [Refined finite norm and all-lift independence](Yin_C_G0654_v1.md#statement) | Pi_N on the SAME chi^N quotient, even character and strict-next-power precision, original finite Y membership without separate global completeness. |
| review | [Independent whole top-layer and A32 finding](../audits/reviews/Yin_R_G0868_v1.md#whole-top-layer-refined-norm-a32-finding) | Entire T1--T8 and all five proof sections, actual integer layers and weights, every-lift precision, rank4 residue blocks and all determinant terms, exact base calibration and moduli, complete bounded H list and original remaining-scope/cost boundaries. |

