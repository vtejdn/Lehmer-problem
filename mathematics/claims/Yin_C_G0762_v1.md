---
author: Yin
---

<a id="copied-cyclotomic-block-repair-and-short-core-obstruction"></a>
# Cyclotomic block copies repair two old primaries and force the added zero mask

Human author Yin.
At author registration, this fixed candidate was OPEN pending fresh independent whole review and separate adoption.
Root proposed the actual large cyclotomic block multiplier, the question of its remaining Mahler cost, and the final exact reciprocal-core removal.
Salem_completion checked the actual height1 factorization, both exact old-primary dyadic orders, the short-core added-mask obstruction, the nonempty zero-mask fiber and every integer trace factor below.
Root read the entirety of the saved CB1--CB7, including the actual K and J_n factorization and all scope limits.
Root and Salem_completion are substantive contributors, not independent reviewers.
The fixed inputs are [adopted C759](Yin_C_G0759_v1.md#decision-whole-reviewed-2026-10-25), [C747's actual added-mask theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) and [C736's integral Delta product identity](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25).
These adequate fixed inputs and the complete-row identity consumed in C759 suffice; the new steps are direct integer polynomial calculations, without a numerical sign search or a new external source premise.
The separate [D5 original-mask obstruction](../drafts/Yin_D_G0005.md#lower-half-old-padding-sign-obstruction) was read as contributor context and is not a logical input.
The [D1 CB1--CB7 author section](../drafts/Yin_D_G0001.md#copied-cyclotomic-block-repair-and-short-core-obstruction) is extraction provenance only; the full necessary proof is retained here.
The distinct SR1--SR4 sign-run inquiry is not included in this Claim.

## Statement

Fix ANY complete initial witness and every parameter of C759 LB1--LB5, with Q=2^ell, ell>=82, m=Q/4-2, and ANY integer s>=s_min there.
All original source factors, multiplicities, degree expenses, fixed constants and the actual threshold are those of that adopted construction, not freely substituted binary polynomials.
For a sufficient explicit consuming interface retain its full Y_1, d_1, h=2d_1-4m, g, Delta_crit=h+2g+1, and B_step, and put

    rho=Q-9,
    N=1+2B_step Delta_crit s,
    d=d_1+rho B_step Delta_crit s,
    n=d+g,
    r=2d-2=rho N+h-1,
    U_out=X^(2m)Y_1 B_N^rho phi^(14m)B_n^2,
    R_out=R_1 B_N^rho B_n^2,
    d_out=d+n-1.

Here phi=X^2+X+1 over F_2, B_b is the COMPLETE trace polynomial of all nonidentity b-th roots, and R_1 is the fixed C759 canonical binary source remainder.
In particular h<N, N and n are odd, gcd(N,n)=gcd(N,15)=gcd(n,15)=1, B_N is prime to X Y_1 phi B_n, and the multiplier a=(n-1)/2 belongs to [ceil(d/2),d-2].
For the binary reciprocal transform P_f=z^(deg f)f(z+z^(-1)), C759 supplies the actual reciprocal support polynomial

    Dbar=P_(X^(2m)Y_1 B_N^rho phi^(14m))/(z^2+1)
         =H(z)(1+z^N)^rho/(1+z),
    deg H=h, H(1)=1.

Use bars for coefficient reduction modulo2, and let C_j be the actual integer trace recurrence C_0=2, C_1=X, C_(j+1)=XC_j-C_(j-1).
For ANY monic integer trace V, define the SIX OWN canonical polynomials by actual integer monic division and scalar division before coefficient reduction:

    a_V=rem_V(V(C_2))/2,
    b_V=rem_V(V(C_3))/3,
    c_V=rem_V(V(C_5))/5,
    F_V=rem_V(2c_V^2-3a_V^5),
    G_V=rem_V(c_V^3-2b_V^5),
    X_(epsilon,V)=rem_V(b_V^2-a_V^3+epsilon G_V),
    epsilon in{1,-1}.

The prime scalar divisions are integral by the Frobenius congruence and monic division; they are never performed in F_2.
Every monic V with Vbar=U_out has b_Vbar=0 and G_Vbar=R_out!=0 by the full C759 source interface.
Let

    H_big=product_(j=4)^(ell-1)(1+z^(2^j N)),
    D_0=H(z)(1+z^N)^7/(1+z),
    r_0=7N+h-1.

For EVERY actual height1 integer L_0 with L_0bar=D_0 and L_0(0)=1, use its reversal at degree r_0 and form

    L=H_big L_0,
    P=L+z^(2n)L^*,
    P_0=L_0+z^(2n)L_0^*.

The reversal of L is at degree r.
The following conclusions hold simultaneously.

1. These are actual height1 lifts with P=H_big P_0, P and P_0 monic reciprocal with constant1, and full degrees r+2n and r_0+2n.
   Their monic integer traces satisfy T=A_big T_0, where A_big=product_(k=3)^(ell-2)C_(2^kN), A_bigbar=X^(Q/2-8)B_N^(Q-16), and T_0bar=X^4Y_1B_N^7phi^(14m)B_n^2.
2. The OWN canonical a_T has exact orders ord_X(a_Tbar)=Q/2-8 and ord_psi(a_Tbar)=Q-18 for EVERY irreducible psi|B_N.
   Thus both F_Tbar and X_(epsilon,T)bar vanish on the full old X^(2m) and B_N^rho, for either epsilon, and the nonzero global G_Tbar=R_out is unchanged.
3. Either added condition B_n^2|F_Tbar or B_n^2|X_(epsilon,T)bar is equivalent to L_0^*=-L_0.
   If wt(D_0)=2k_core, exactly2^(k_core-1)>0 copied-block members satisfy these equivalent conditions.
   Every one has the zero added mask and P=H_big L_0(1-z^(2n)); none is coprime to z^(2n)-1.
   The original four-active-pair C759 mask is not retained by this new sign class.
4. The actual multiplier has m(H_big)=0 and |Res(H_big,z^(2n)-1)|=(Q/16)^2, with no common root with that binomial.
   Nevertheless the FULL resultant of every added-passing P is0, so the nonzero-resultant Mahler bound of C757 does not apply to this class.
5. For every added-passing output, L_0=(1-z^2)K with K monic reciprocal integer, constant1 and degree r_0-2=7N+h-3.
   Exactly P=H_big(1-z^2)(1-z^(2n))K and m(P)=m(K), with all degrees and multiplicities counted.
   Writing J_n=1+sum_(j=1)^((n-1)/2)C_(2j), the actual trace factorization is T=A_big(X^2-4)J_nT_K, where J_nbar=B_n^2 and T_Kbar=X^2Y_1B_N^7phi^(14m).

The complete actual source and cost hypotheses above are retained in CB1--CB7, which are part of the statement's precise scope.
No condition on the remaining old Y_1 or phi primaries is proved, and no canonical residual precision is transferred to T_0 or T_K.
No height1 bound for K, irreducibility, complete residual solution, uniform positive Mahler gap, nearzero sequence or unrestricted G0001 conclusion is asserted.
The proposed copied-block repair is assessed on its actual new sign class; the separate original-mask obstruction and the sign-run inquiry are not incorporated as new conclusions.

## Complete argument

### CB1. Exact domain and the short binary core

Fix every C759 initial source and constant, and any s>=s_min.
In particular retain Q=2^ell, ell>=82, m=Q/4-2, rho=Q-9, odd coprime indices N,n, and the complete identities

    U_out=X^(2m)Y_1 B_N^rho phi^(14m) B_n^2,
    Dbar=H(z)(1+z^N)^rho/(1+z),
    deg H=h<N, H(1)=1,
    r=deg Dbar=rho N+h-1=2d-2,
    2n=rho N+Delta_crit,
    Delta_crit=h+2g+1>0.                       (CB1)

All coprimalities from C759 remain actual full-source assertions: B_N is squarefree and prime to X,Y_1,phi,B_n, and B_n is prime to the complete pre-outer source.
Thus the exact multiplicities of X and every irreducible factor of B_N in U_out are 2m and rho.
No factors, multiplicities, source degrees or outer-row costs are changed here.
Put

    H_big(z)=product_(j=4)^(ell-1)(1+z^(2^j N))
            =sum_(k=0)^(Q/16-1)z^(16Nk),
    e_big=deg H_big=(Q-16)N,
    D_0(z)=H(z)(1+z^N)^7/(1+z) in F_2[z],
    r_0=deg D_0=7N+h-1.                       (CB2)

The equality defining H_big is an INTEGER polynomial identity: each binary subset of the exponents 2^4,...,2^(ell-1) occurs exactly once.
Its binary reduction is (1+z^N)^(Q-16), so Dbar=H_bigbar D_0 and r=e_big+r_0.
The denominator in D_0 divides (1+z^N), since N is odd; no formal power series replaces this polynomial.
Both H_bigbar and Dbar are monic reciprocal with constant1, hence D_0 is also monic reciprocal with constant1 by cancellation in F_2[z].
Its degree r_0 is even because h is even and N is odd.
Moreover

    r_0<8N<16N,
    n-1-r_0=((Q-23)N+Delta_crit-2h)/2>0.       (CB3)

For the last strict inequality, Delta_crit=h+2g+1 and h<N give a numerator greater than (Q-24)N+2g+1, which is positive in the actual Q>=2^82 domain.
Thus r_0<n-1 and in particular 2n>r_0.
Finally D_0 has exact order6 at z=1, since H(1)=1 and 1+z^N has a simple root there in characteristic2.
For an even-degree reciprocal binary polynomial, the value at1 is its middle coefficient because the other coefficients pair and cancel.
The middle coefficient of D_0 is consequently zero.

### CB2. Genuine integer copied-block lifts and their trace factor

Choose ANY actual integer height1 polynomial L_0 with L_0bar=D_0 and L_0(0)=1.
Its degree is exactly r_0 and its leading coefficient may be either1 or-1.
Let L_0^*=z^(r_0)L_0(z^(-1)) and set

    L=H_big L_0,
    P=L+z^(2n)L^*=H_big P_0,
    P_0=L_0+z^(2n)L_0^*.                     (CB4)

Here the reversal of L uses ambient degree r, and the factorization follows from the actual reciprocity of H_big.
Because r_0<16N, the shifted copies z^(16Nk)L_0 have disjoint coefficient intervals.
Thus L is genuinely height1, not merely congruent to a height1 polynomial, and Lbar=Dbar.
The two large blocks of P are disjoint because 2n>r; this is C759's n>=d+1 and r=2d-2.
Likewise 2n>r_0 makes P_0 height1.
Both P and P_0 are monic reciprocal integer polynomials with constant1: their top coefficient is L_0(0)=1, regardless of the leading sign of L_0.
Their full degrees are 2n+r and 2n+r_0, respectively.
Consequently they have unique monic integer traces T and T_0, of degrees d_out=n+r/2 and n+r_0/2.

Write C_j for the actual integer trace polynomials.
Each factor of H_big has the exact trace expression

    1+z^(2^jN)=z^(2^(j-1)N) C_(2^(j-1)N)(z+z^(-1)).

Therefore, with

    A_big(X)=product_(k=3)^(ell-2) C_(2^k N)(X),
    deg A_big=(Q/2-8)N,
    T=A_big T_0,                              (CB5)

the last equality is an ACTUAL integer factorization, obtained by cancelling the equal powers of z in the reciprocal trace identities.
The complete-row identity C_Nbar=X B_N^2 and dyadic composition C_(2^kN)bar=C_Nbar^(2^k) give

    A_bigbar=X^(Q/2-8) B_N^(Q-16),
    T_0bar=X^4 Y_1 B_N^7 phi^(14m) B_n^2.     (CB6)

The second identity follows by cancelling the first from Tbar=U_out in the polynomial domain F_2[X].
It retains the full Y_1, all its multiplicities, the entire B_N and B_n rows, and phi^(14m).
There is no assertion that the canonical residuals of T_0 inherit those of T.

### CB3. Actual dyadic carry and two repaired old primaries

For every integer polynomial V put Delta(V)=(V(C_2)-V^2)/2.
This is an integer polynomial, and a_T=rem_T Delta(T), as in C736.
All divisions by2 in this section take place in Z[X] before reduction.
The actual Chebyshev identity C_j(C_2)=C_(2j)=C_j^2-2 gives

    Delta(C_j)=-1.

Reducing the integer product rule from C736 yields

    Delta(A_big)bar
       =sum_(k=3)^(ell-2)
           product_(i=3, i!=k)^(ell-2) C_(2^iN)bar^2.    (CB7)

At X, the factor C_(2^kN)bar has exact order2^k.
At EVERY irreducible psi|B_N it has exact order2^(k+1), since B_N is squarefree and prime to X.
In CB7 the UNIQUE lowest-order summand is the one omitting the largest factor, k=ell-2.
Every other summand has strictly larger order, so its nonzero leading term cannot cancel.
The exact orders are accordingly

    ord_X Delta(A_big)bar=Q/2-16,
    ord_psi Delta(A_big)bar=Q-32, psi|B_N.      (CB8)

Now apply the same integer product rule to T=A_big T_0:

    Delta(T)bar=T_0bar^2 Delta(A_big)bar
                         +A_bigbar^2 Delta(T_0)bar.      (CB9)

By CB6 the first term has exact X order8+(Q/2-16)=Q/2-8 and exact psi order14+(Q-32)=Q-18.
The second term has X order at least Q-16 and psi order at least2Q-32, respectively.
These are strictly greater than the corresponding first-term orders.
The own canonical monic remainder differs from Delta(T)bar by a multiple of U_out, whose X and psi orders are 2m=Q/2-4 and rho=Q-9.
Both are also strictly greater than the displayed first-term orders.
Hence the OWN canonical polynomial has the exact, lift-independent valuations

    ord_X a_Tbar=Q/2-8,
    ord_psi a_Tbar=Q-18 for every psi|B_N.      (CB10)

This calculation neither assumes that a factor quotient has the full precision nor divides by2 in a modular quotient.
At the same T, C759's actual full source gives b_Tbar=0 and G_Tbar=R_out, and R_out is divisible by X^(2m)B_N^rho.
Reduction of the actual residuals therefore gives F_Tbar=a_Tbar^5 and X_(epsilon,T)bar=a_Tbar^3 on each of these two old moduli, for BOTH epsilon=1,-1.
The inequalities

    3(Q/2-8)>=Q/2-4,
    3(Q-18)>=Q-9

hold in the actual domain; the fifth powers vanish as well.
Thus EVERY copied-block sign choice CB4 passes BOTH residual first-bit conditions on the FULL old X^(2m) and B_N^rho.
It still has the unchanged nonzero canonical G_Tbar=R_out globally.
No passage on the remaining old Y_1 or phi primaries has been proved.

### CB4. The added condition forces the zero mask

Define the actual half-sums

    S_0=(L_0+L_0^*)/2,
    S=(L+L^*)/2=H_big S_0.                    (CB11)

These are integer polynomials because D_0 is reciprocal and L_0bar=D_0.
Every coefficient of S_0 is0,1 or-1: a supported reflected pair consists of two signs, and unsupported pairs are both zero.
This coefficient restriction includes the central position, which is zero by CB1.
Suppose either of the equivalent added-modulus residual conditions of C747 holds, namely B_n^2|F_Tbar or B_n^2|X_(epsilon,T)bar.
C747 applies at this SAME complete binary source and the actual n=2a+1, with ceil(d/2)<=a<=d-2 already paid by C759.
Its true integer carry theorem requires

    Sbar=(1+z)(1+z^n)J

for an admissible reflection mask J; in particular 1+z^n divides Sbar.
Put Sigma_n=(1+z^n)/(1+z).
Since n is odd, Sigma_n is squarefree and has no root at1.
Since gcd(n,N)=1, it is coprime to 1+z^N, and hence to H_bigbar=(1+z^N)^(Q-16).
Thus CB11 forces Sigma_n|S_0bar in F_2[z].
But deg S_0<=r_0<n-1=deg Sigma_n by CB3, so S_0bar=0.
Because every actual coefficient of S_0 lies in{0,1,-1}, this implies S_0=0 over Z, not merely an even nonzero half-sum.
It follows that

    L_0^*=-L_0,
    L^*=-L,
    P=H_big L_0(1-z^(2n)).                   (CB12)

Conversely, any such antisymmetric L_0 gives S=0, the C747 zero mask, and both added-modulus conditions.
Therefore in the copied-block class the added first-bit condition is equivalent to CB12.
EVERY such output has a cyclotomic factor1-z^(2n), and NONE is coprime to z^(2n)-1.
In particular this repair cannot retain C759's four-active-pair nonzero even mask or its coprime branch.
The obstruction uses the actual integer coefficient range of S_0; a general even polynomial could not be set to zero by its binary reduction.

The surviving zero-mask subfamily is nonempty.
Write wt(D_0)=2k_core; this is even because D_0 is reciprocal with zero middle coefficient, and k_core>=1 since its two endpoint coefficients are1.
Assign opposite signs to each supported reflected pair, with the constant sign1.
There are exactly2^(k_core-1) such actual L_0 and hence that many copied-block outputs satisfying the added conditions.
They ALL satisfy the two old-primary conditions in CB3 as well.
The original full-source degree, exact fresh factor, canonical nonzero binary G and original positive source gap remain unchanged because their binary U_out is unchanged.
These are zero-mask solutions of three local parts of the system, not full residual solutions or irreducible outputs.

### CB5. The actual cyclotomic multiplier on the outer roots

The integer H_big is a monic product of polynomials1+z^k, each of whose roots lies on the unit circle.
Consequently m(H_big)=0 and CB4 gives m(P)=m(P_0), with ALL multiplicities retained.
It is also nonvanishing at EVERY root of z^(2n)-1.
Indeed n is odd, so such a root has order with2-part at most2, whereas a root of1+z^(2^jN), j>=4, has order with2-part exactly2^(j+1).
Here nonvanishing is not a claim of being a unit in a ring of algebraic integers or in the binary quotient.

For completeness, its exact full cyclic resultant is

    |Res(H_big,z^(2n)-1)|=(Q/16)^2.           (CB13)

For each j, gcd(2^jN,2n)=2, and powering the full set of2n-th roots by2^jN maps it onto the n-th roots with every fiber of size2.
Since n is odd, product_(eta^n=1)(1+eta)=2, so each displayed factor contributes absolute resultant4.
There are ell-4 factors, giving4^(ell-4)=(Q/16)^2.
For an arbitrary copied-block choice and a root zeta^(2n)=1 one has the exact evaluation P(zeta)=2H_big(zeta)S_0(zeta).
On the actual added-passing subfamily, CB12 makes S_0=0, so Res(P,z^(2n)-1)=0 despite CB13.
The nonzero-resultant premise of C757 is therefore false here.
Neither that theorem nor removing H_big supplies a positive numerical Mahler lower bound for this subfamily.
This is a failure of this particular certificate, not a proof that its Mahler measures are small or that no other gap exists.

### CB6. Exact remaining reciprocal core and its own degree

For an added-passing output, r_0 is even and L_0^*=-L_0.
Evaluating at1 and-1 gives L_0(1)=L_0(-1)=0 over the integers.
Therefore there is an actual integer polynomial K with

    L_0=(1-z^2)K,
    K(0)=1, deg K=r_0-2,
    K monic and reciprocal.                  (CB14)

Integer divisibility follows from the two monic linear factors and then their distinct actual roots, or from successive integer monic divisions.
The leading coefficient of L_0 is-1 because its constant coefficient is1 and it is antisymmetric.
Division by1-z^2 thus makes K monic; reversing CB14 and cancelling the nonzero factor1-z^2 proves reciprocity.
No height1 bound for K is asserted: polynomial division can accumulate coefficients.
The exact full factorization and Mahler identity are

    P=H_big(1-z^2)(1-z^(2n))K,
    m(P)=m(K).                                (CB15)

All three removed factors are actual monic or signed-monic cyclotomic polynomials of measure0; there is no root deletion without multiplicity or degree accounting.
Let T_K be the unique monic integer trace of K, of degree (r_0-2)/2=(7N+h-3)/2, and define the actual monic integer trace polynomial

    J_n(X)=1+sum_(j=1)^((n-1)/2) C_(2j)(X).

Its reciprocal transform is

    z^(n-1)J_n(z+z^(-1))
            =(z^(2n)-1)/(z^2-1)=sum_(j=0)^(n-1)z^(2j),

so J_n has degree n-1 and J_nbar=B_n^2 by the complete B_n trace identity.
Using the cancellation of the two minus signs in CB15 gives the ACTUAL integer trace factorization

    T=A_big (X^2-4) J_n T_K,
    T_Kbar=X^2 Y_1 B_N^7 phi^(14m).           (CB16)

The trace identity follows from z^2[(z+z^(-1))^2-4]=(z^2-1)^2 and the displayed reciprocal identity for J_n.
The binary identity follows by polynomial cancellation from CB6, since the new outer factors have binary X^2 and B_n^2.
The complete degree check is

    deg T=(Q/2-8)N+2+(n-1)+(7N+h-3)/2
         =n+r/2=d_out.

Thus the removed reciprocal degrees are e_big,2,2n and the remaining reciprocal degree is r_0-2, adding to r+2n exactly.
In particular the remaining core has X multiplicity2 and B_N multiplicity7 in its binary TRACE polynomial; it is not the original complete source with X multiplicity2m.
The actual canonical residuals of T_K must use T_K's own divisor.
C736's precise weighted factor-transfer identities do not transfer the full T's local or global precision to T_K automatically, especially in the presence of their displayed common binary factors.

### CB7. Scope and next discriminating question

The construction is an actual repair of the full OLD-X and OLD-B_N first-bit conditions for a new copied-block sign class, with no change of the C759 binary source or costs.
Adding the new B_n^2 condition forces a nonempty zero-mask class, with the exact factorization, sign count and core measure identity above.
There is NO nonzero added mask, NO coprime output and hence NO application of the C757 nonzero cyclic-resultant lower bound within this repair.
The remaining old Y_1 and phi equations and the own canonical system of T_K have not been solved or identified with one another.
The core K is reciprocal and may be reducible; no nonreciprocal Mahler theorem is applied to it, and neither a uniform positive gap nor a nearzero sequence is proved.
The separate original C759 four-active-pair obstruction and the present copied-block zero-mask obstruction concern different sign classes.
This bounded author result leaves a possible different mask, different non-copied block structure or different source as a distinct question, without starting that further investigation here.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision copied-cyclotomic-block-zero-mask-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T23:10 |
| status | open |
| reason | Register the complete CB1--CB7 author theorem after root read the entire saved argument. Genuine copied height1 blocks factor through an actual cyclotomic multiplier and repair both full old X and B_N primaries with exact own canonical a orders. The actual added condition is equivalent to an antisymmetric short core, giving a nonempty exact zero-mask fiber but no coprime output. The nonzero multiplier resultant is distinguished from the zero full resultant, and all remaining cyclotomic factors are removed with exact degrees, trace factors and total Mahler equality. No core precision inheritance, remaining-old-primary solution, Mahler gap, nearzero construction or unrestricted Task conclusion is asserted. Root and Salem_completion are contributors; fresh independent whole review and separate adoption were outstanding at author registration. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete copied-block theorem](#statement) | Entire C759-consuming parameter domain and all six actual canonical definitions; actual height1 factorization, exact old-X and old-B_N orders and residuals, added iff antisymmetry and exact count, multiplier/full resultant distinction, full cyclotomic removal and new binary core, with all precision and measure exclusions. |
| argument | [Complete integer and core proof](#complete-argument) | Entire CB1--CB7/equations CB1--CB16: actual disjoint blocks and trace factor, unique minimal Delta summands, true monic remainder orders, short binary mask cancellation and coefficient-lift zero, nonempty fiber, exact complex-root multiplier resultant, full integer K/J_n factorization and degree/Mahler accounting. |
| dependency | [Adopted actual lower-half complete source](Yin_C_G0759_v1.md#decision-whole-reviewed-2026-10-25) | LB1--LB5 exact original Q/Y_1/H/constants and threshold, coupled N/n full coprimalities, complete binary source through the outer row, full canonical b=0 and G=R_out!=0, exact multiplicities and degrees. Only this source/support interface is consumed; its original four-active-pair mask and its free-sign fiber are not claimed retained. |
| dependency | [Adopted actual added-mask theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Part B genuine integer half-sum and own-canonical added-B_n^2 equivalence, zero-mask antisymmetry, applied to the actual same binary source and paid range of a. Its old-X and global conclusions are not assumed for the new class; CB3 proves the needed old orders directly. |
| dependency | [Adopted integral canonical factor rule](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT2 integral Delta_2 product identity and a_V=rem_V Delta(V), actual same-divisor monic reduction, plus the precise limitation of weighted cofactor transfer. No arbitrary factor precision preservation is invoked. |
| dependency | [Adopted complete trace row identity](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete nonidentity odd-root row and squarefree inverse-pair partition, C_Nbar=X B_N^2 and B_n=1+sum C_jbar in the precise complete-row sense already consumed in C759. No support certificate or unrelated norm gate is used. |
| support | [Nonzero cyclic-resultant comparison](Yin_C_G0757_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: its nonzero full-resultant premise fails on the added-passing copied-block class. No Mahler lower bound from C757 is inferred from the nonzero resultant of H_big alone. |
| support | [Absolute Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Full root-product definition and multiplicity-sensitive additivity used in the elementary actual cyclotomic removal; no degree-normalized measure or Task completion inference. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T23:20 |
| status | proved |
| reason | Adopt the complete standalone statement and CB1--CB7 through fresh independent whole R982, whose full finding root read. All actual height1 support, complete trace factors, unique exact old X/BN Delta and own-canonical orders, both full old-primary residuals, added iff integer antisymmetry and positive exact count, multiplier/full-resultant distinction, and K/J_n factorization with complete degrees and binary profile passed without substantive repair. This copied-block class repairs two old primaries but its added-passing outputs necessarily have zero mask and explicit cyclotomic factors; total measure equals that of the retained reciprocal K. The original nonzero C759 mask is not retained, and no C757 nonzero-resultant gap applies. Root and Salem_completion remain contributors. No remaining Y1/phi solution, automatic core precision, absence of further core cyclotomic factors, core height/irreducibility bound, uniform Mahler gap, nearzero family, additional raised-q theorem or unrestricted Task completion is adopted here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete copied-block theorem](#statement) | Entire C759-consuming parameter domain and all six actual canonical definitions; actual height1 factorization, exact old-X and old-B_N orders and residuals, added iff antisymmetry and exact count, multiplier/full resultant distinction, full cyclotomic removal and new binary core, with all precision and measure exclusions. |
| argument | [Complete integer and core proof](#complete-argument) | Entire CB1--CB7/equations CB1--CB16: actual disjoint blocks and trace factor, unique minimal Delta summands, true monic remainder orders, short binary mask cancellation and coefficient-lift zero, nonempty fiber, exact complex-root multiplier resultant, full integer K/J_n factorization and degree/Mahler accounting. |
| dependency | [Adopted actual lower-half complete source](Yin_C_G0759_v1.md#decision-whole-reviewed-2026-10-25) | LB1--LB5 exact original Q/Y_1/H/constants and threshold, coupled N/n full coprimalities, complete binary source through the outer row, full canonical b=0 and G=R_out!=0, exact multiplicities and degrees. Only this source/support interface is consumed; its original four-active-pair mask and its free-sign fiber are not claimed retained. |
| dependency | [Adopted actual added-mask theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Part B genuine integer half-sum and own-canonical added-B_n^2 equivalence, zero-mask antisymmetry, applied to the actual same binary source and paid range of a. Its old-X and global conclusions are not assumed for the new class; CB3 proves the needed old orders directly. |
| dependency | [Adopted integral canonical factor rule](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT2 integral Delta_2 product identity and a_V=rem_V Delta(V), actual same-divisor monic reduction, plus the precise limitation of weighted cofactor transfer. No arbitrary factor precision preservation is invoked. |
| dependency | [Adopted complete trace row identity](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete nonidentity odd-root row and squarefree inverse-pair partition, C_Nbar=X B_N^2 and B_n=1+sum C_jbar in the precise complete-row sense already consumed in C759. No support certificate or unrelated norm gate is used. |
| support | [Nonzero cyclic-resultant comparison](Yin_C_G0757_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: its nonzero full-resultant premise fails on the added-passing copied-block class. No Mahler lower bound from C757 is inferred from the nonzero resultant of H_big alone. |
| support | [Absolute Mahler convention](../tasks/Yin_T_G0001_v1.md#contract) | Full root-product definition and multiplicity-sensitive additivity used in the elementary actual cyclotomic removal; no degree-normalized measure or Task completion inference. |
| review | [Fresh independent whole copied-block finding](../audits/reviews/Yin_R_G0982_v1.md#whole-copied-block-finding) | Entire standalone statement and CB1--CB7, all actual source/parameter/sign/canonical/factor/count/resultant/core endpoints and precise accepted interfaces, without added raised or inheritance conclusions. |

