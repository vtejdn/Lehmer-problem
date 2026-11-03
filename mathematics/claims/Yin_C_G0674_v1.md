---
author: Yin
---

# Partial-H complete products and weak-forward canonical Haar lifts

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
This entire statement and proof are initially open for fresh isolated whole mathematical review.

<a id="partial-h-completion-candidate"></a>
Root proposed the complete complement, the elementary smooth-order proof, the full degree accounting and the strong-C3 obstruction.
Original_law checked all root multiplicities and costs, completed the finite criterion and canonical proof, and derived the explicit normalized-multiplicity24 synthetic family using the adopted C670 character.
Both are contributors, not independent reviewers of this new theorem.
The new content is an extension of C667 to partial H with weaker forward divisibility, not a revision of that theorem's stronger complete-Y conclusion.
The old complete-H synthesis is retained separately in C698v2.
No new native calculation, support scan or original realization is used.

The exact inputs are [C654](Yin_C_G0654_v1.md#decision-whole-reviewed-2026-10-23), [C664](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24), [C667](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24), the [all-representative C649 gate](Yin_C_G0649_v1.md#statement), the [C652 character calibrations](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) and the [adopted C670 finite classification](Yin_C_G0670_v1.md#decision-whole-reviewed-2026-10-24).
C670 is used only for its exact f_31 character and primitive order; no native computation is rerun here.
The integer trace/Haar interface is the one fully retained in C667 and its accepted C199 dependencies.
No C683 theorem about actual original inputs is applied to synthetic objects.

<a id="partial-h-completion-statement"></a>
## Statement

Work over F_2 with phi=X^2+X+1, chi=Xphi^2 and C_3=X^3+X.
For every positive odd n let B_n be the complete trace polynomial of all nonidentity n-th roots, one trace per inverse pair, with B_1=1; W_n is its complete primitive-order factor.
Thus W_5=phi, deg W_n=varphi(n)/2, and B_n=product_(d|n,d>1)W_d.
An allowed complete product means a finite nonnegative product of whole W_n for odd n>1,n!=5.
Put R_N=F_2[X]/chi^N and use the adopted exact finite character Pi_N:R_N^*->Z/(2^floor(log_2N)) with G_N=ker Pi_N, where G_N is the group of allowed complete products in R_N^*.
Write ell for the normalized character on 1+tF_2[[t]], with ell(1+t)=1.

### A. Completion of every zero-character target

Let N>=1, let H in F_2[t] satisfy H(0)=1, put J=H(chi), and let B be any specified nonzero polynomial.
For a unit class c in R_N, the condition Pi_N(c)=0 is equivalent to existence of a monic polynomial Y prime to Xphi representing c such that YJ is an allowed complete product.
When this condition holds, Y can simultaneously be chosen so that

    Y divides Y(C_3)^2, Y divides Y(chi)^2,
    every occurring irreducible Y factor has multiplicity at least2,
    Y and YB are nonsquares.                              (PH1)

A single irreducible factor has exact multiplicity3 in both Y and YB.
There is no assertion that Y itself is complete or that either forward exponent can be replaced by1.

For an explicit construction let mu_max be the largest irreducible multiplicity in J, with mu_max=0 if J=1, and put E_pad=2mu_max+2.
Every irreducible trace order in J is odd, greater than1, and different from5.
For each occurring order 3^a5^b d with d>1 and gcd(d,15)=1, include every 3^u5^v d, 0<=u<=a,0<=v<=b, in the finite set M.
Let M_smooth be the occurring orders 3^a5^b>1; each such W_n is irreducible, and let mu_n be its actual multiplicity in J.
Define

    C_comp=product_(n in M) W_n^(E_pad)
                    product_(n in M_smooth) W_n^(mu_n),
    Y_seed=C_comp/J,
    D_C=E_pad sum_(n in M) varphi(n)/2
                      +sum_(n in M_smooth) mu_n varphi(n)/2,
    D_seed=D_C-5degH=degY_seed>=0, D_B=degB.              (PH2)

All products and sums are finite, including when empty, and the division is exact.
The symbols D_C,D_seed are degree costs; they are distinct from the canonical ERROR POLYNOMIAL D_0 below.
Let L be the least power of2 at least2N+1, let e be3 times the least power of2 at least2N, and define

    K=max(30L,4(D_seed+D_B)^2),
    k_0=floor(K/(10L))+1,
    k=k_0 if 3 does not divide 1+10Lk_0, and k=k_0+1 otherwise,
    n_fresh=1+10Lk.

Then gcd(n_fresh,15)=1 and K<n_fresh<=K+20L+1.
One may choose

    Y=Y_seed Z B_(n_fresh)^3,
    degZ<=75L^2(e+1),
    degY=D_seed+degZ+3(n_fresh-1)/2
             <=D_seed+75L^2(e+1)+3(n_fresh-1)/2,         (PH3)

where Z is an allowed complete product with each irreducible multiplicity at least2, primitive support below30L and both stronger forward divisibilities.
All support and completion costs are paid in PH2--PH3.

### B. Full canonical and root/gate specialization

Let m>=1, let Q be a power of2 with 2m<Q<5m, and require 5degH<5m-Q.
Set B=X^(Q-m)H(chi), so D_B=Q-m+5degH<4m, and put N=4m.
Let S be a specified square class modulo phi^(8m), divisible by phi^(4m).
Let x(t) be the inverse of chi at0, put h_Q(X)=1+sum_(i=0)^(log_2Q-1)X^(Q-2^i), and define the full unit CRT class c by

    L_0(t)=[(1+t+t^2)^(7m)H(t)h_Q(x(t))]^(-1)
                                  modulo t^(2m), degL_0<2m,
    c=L_0(X^2) modulo X^(4m),
    c=X^(-2m)B^(-7)+beta X^(-2m)B^(-13)S
                                  modulo phi^(8m),       (PH4)

where beta=X^(2^a),2^a>=8m,2^a=Q modulo3.
Assume Pi_(4m)(c)=0 and take the Y in PH1--PH3 for this target and this entire B.
Set

    H_0=X^(2m)Y, U_0=H_0phi^(14m),
    R_0=H_0phi^(12m)B, V_0=H_0B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m), D_0=V_0+C_00^3.

Then

    R_0=rem_(U_0)(U_0(chi)^3),
    U_0 divides U_0(C_3)^2,
    X^(4m)|Y', D_0 in phi^(4m),
    H_0^6=C_00^21 modulo phi^(8m),
    Z_0^11=H_0C_00^2 modulo phi^(6m),
    Z_0D_0+H_0V_0S=0 modulo phi^(8m),
    Z_0=beta^2B^(-1)(1+beta B^(-6)S)
                                  modulo phi^(6m).       (PH5)

The root is the unique high unit root with its correction retained.
The factor phi is the unique unsaturated U_0 factor, with orders14m in U_0 and12m in R_0; every other U_0 factor is saturated.
Both U_0 and R_0 are nonsquares.
For every q=2^k, U=U_0^q and R=R_0^q have actual maximal Frobenius power q separately, R=rem_U(U(chi)^3), and U divides U(C_3)^2.
The root and gate raise with all actual ingredients to precisions6mq and8mq and correction S^q.
The exact costs are

    r_deg=degU=q(30m+degY),
    w_deg=degR=q(26m+degY+D_B),
    r_deg-w_deg=q(5m-Q-5degH)>0.                          (PH6)

If an original reciprocal realization existed its degree would be2r_deg, not20m.
The separately defined squarefree odd parts Y=J_U^2W_U and V_0=J_G^2W_G satisfy

    W_U!=1, X^(4m)|W_U', degW_U>=4m+1,
    W_G!=1, phi^(8m)|W_G', degW_G>=16m+1.                (PH7)

### C. Integer layers and the zero-Haar lift without whole H

For a specified q, suppose the S in PH4 is the exact correction from given finite nonnegative INTEGER data a_b satisfying

    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq, a_b=0 if lambda_b>8mq,
    S=sum_(a_b odd,4mq<lambda_b<12mq)
        X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                            phi^(12m-lambda_b/q).         (PH8)

All exponents in this normalized formula are integers; a_b and their indices are not divided by q.
Then V_0 is complete away from the endpoint, since

    V_0=X^(m+Q) C_comp Z B_(n_fresh)^3
       =X^v product_(j odd,j>1,j!=5)W_j^(nu_j), v=m+Q.

For the monic integer trace polynomial F_j defined by
Phi_j(z)=z^(varphi(j)/2)F_j(z+z^(-1)) and F_4=X, the polynomial

    G_int=F_4^(qv) product_j F_j^(q nu_j)
                          product_b F_(2^b*5)^(a_b)      (PH9)

is monic, reduces to R, has degree w_deg and satisfies

    integral_(circle) log(G_int(z+z^(-1))^2)dnu_1=0.

Here nu_1 is probability Haar and the logarithm has its integrable convention at zeros.
This implication requires the GIVEN layer representation PH8; it does not assert that every arbitrary square S can be realized by those layers.
No completeness of H or Y individually is required.

### D. A sharp obstruction to replacing the forward square by a first power

For any odd n>1 coprime to3, if YJ is complete and Y divides Y(C_3), then the multiplicity function of J on the primitive-order-n traces is invariant under C_3.
At order31 this implies that J has the same multiplicity on all three irreducible degree5 primitive trace factors.
Consequently for H=f_31=1+t^2+t^5 and J=H(chi), there is NO polynomial Y such that YJ is complete and Y divides Y(C_3).
This obstruction applies at arbitrary degree and finite precision.
It does not apply to the weaker square in PH1.

### E. A synthetic normalized-multiplicity24 family

For EVERY q=2^k, set

    m=12, Q=32, H=f_31=1+t^2+t^5,
    B=X^20H(chi), S=0, a_0=144q, a_b=0 for b>=1.        (PH10)

The full PH4 target has Pi_48(c)=0 and admits the simultaneous construction PH1--PH9.
Its full cost can be bounded by

    C_comp=W_31^4 W_155^4,
    D_C=300, D_seed=275, D_B=45,
    L=128, e=384, n_fresh=410881,
    degY<=473704595,
    r_deg<=473704955q, w_deg<=473704952q,
    r_deg-w_deg=3q.                                     (PH11)

Here V_0=X^44 C_comp Z B_(410881)^3, and the integer layer factor in G_int is F_5^(144q).
The value A_0=24 describes the matched formal normalization m=12; it is not an original realization claim.
The strong-C3 obstruction above holds for this same H, so the weaker construction cannot be silently upgraded to C667's stronger divisibility.

### Exact realization boundary

These are simultaneous characteristic-two canonical data and, under PH8, synthetic integer zero-Haar data with all displayed costs.
They do NOT construct one monic integer T whose actual divided remainders theta_p=rem_T(T(C_p))/p satisfy the original shared equations and make G_int its canonical G_can.
SAME-T modulo4/modulo8, the characteristic-zero residual equations, irreducibility, total reality, original nonzero field values and the original reciprocal polynomial remain unestablished.
No original A_0=24 input is constructed or excluded, and the unrestricted task is not solved.

<a id="partial-h-completion-argument"></a>
## Complete argument

### PC1. Actual trace orders and smooth-order irreducibility

For a nonzero alpha in the algebraic closure of F_2, the two roots of z^2+alpha z+1 are distinct, nonzero and inverse to one another.
Neither is1, and their finite-field multiplicative order is a uniquely determined odd n>1.
This identifies every irreducible factor of J with one primitive trace order, and different orders have disjoint roots.
Since J(0)=1 and J modulo phi is H(0)=1, neither order1 nor order5 occurs.
All W_n are squarefree, because inverse pairing of primitive roots has no fixed point for odd n>1.

For p=3,g=2^2=1+3 or p=5,g=2^4=1+15, one has v_p(g-1)=1.
If v_p(u-1)=r>=1, the first term p(u-1) of the binomial expansion of u^p-1 has valuation r+1.
Each intermediate term has valuation at least1+2r>r+1, and the final term has valuation pr>r+1.
Thus v_p(u^p-1)=r+1, and induction gives v_p(g^(p^j)-1)=j+1.
For h positive and prime to p, the geometric sum 1+u+...+u^(h-1) is h modulo p, so v_p(u^h-1)=v_p(u-1).
It follows that g^e=1 modulo p^a exactly when p^(a-1) divides e.
Reduction modulo p requires the exponent of2 to be divisible by2 for p=3, and by4 for p=5.
Consequently

    ord_(3^a)(2)=2*3^(a-1),
    ord_(5^b)(2)=4*5^(b-1), a,b>=1.

For a pure odd prime power the only solutions of x^2=1 are plus/minus1, since gcd(x-1,x+1) divides2.
The half-order power of2 is therefore-1, and the trace orbit has length varphi(n)/2.
For a,b>0, CRT gives ord_(3^a5^b)(2)=4*3^(a-1)*5^(b-1)=varphi(3^a5^b)/2.
Half this order is divisible by ord_(3^a)(2), so its power of2 is1 modulo3^a, not-1.
The cyclic group generated by2 has a unique element of order2; hence-1 is not a power of2 modulo the mixed modulus.
The trace orbit length, the least positive k with 2^k=plus/minus1 modulo n, is again varphi(n)/2.
Every primitive trace therefore lies in a single Frobenius orbit, proving irreducibility of W_(3^a5^b) for all positive such orders.
This is an elementary proof, not an assumed primitive-root theorem or a finite scan.

### PC2. The complete complement and both actual multiplicity inequalities

The finite set M contains every nonsmooth order of J and all its descendants obtained by removing powers of3 or5.
Every smooth-order factor of J is the whole W_n, by PC1, with its actual multiplicity mu_n.
Thus J divides C_comp exactly, and ALL smooth-order factors cancel from Y_seed.
At each root of each order in M, the multiplicity in Y_seed is E_pad minus its multiplicity in J, the latter being zero when absent.
It lies between E_pad-mu_max and E_pad and is at least2.

At alpha=z+z^(-1), the identities C_3(alpha)=z^3+z^(-3) and chi(alpha)=z^5+z^(-5) give image orders n/gcd(n,3) and n/gcd(n,5).
These orders remain in M because their core d>1 is unchanged.
The derivative C_3'=(X+1)^2 vanishes only at the order3 trace1, and chi'=phi^2 only at primitive fifth traces.
Neither critical source is in M.
Composition therefore preserves the local multiplicity of the target polynomial at every source root in M.
For either map f, each source multiplicity of Y_seed is at most E_pad while its target multiplicity in Y_seed is at least E_pad-mu_max.
The exact inequality

    E_pad<=2(E_pad-mu_max)

proves Y_seed|Y_seed(f)^2 root by root.
It also gives Y_seed|Y_seed(chi)^3.
Factors outside M create no divisibility obligation on the left.
This proves the two forward-square statements without treating whole groups as single irreducibles or discarding any partial multiplicity.

### PC3. The finite character criterion and bounded complete row correction

C654 gives J modulo chi^N in G_N for EVERY H with H(0)=1.
C_comp is an allowed complete product, so Y_seed=C_comp/J also has class in G_N.
If Pi_N(c)=0, the class c/Y_seed is in ker Pi_N=G_N by C664.
Use C664's exact5L complete rows and exponent vector in {0,...,e-1} for this class.
Replace each exponent1 by e+1, leaving other exponents unchanged.
Every row has order dividing e, so the class and each exponent parity are unchanged; every positive row exponent is at least2.
The resulting product Z has all irreducible multiplicities at least2, primitive support below30L and degZ<=75L^2(e+1).
The full source/predivision moduli remain X^Nphi^(2N) and X^Nphi^(2N+1), respectively.

As proved from complete roots in C667, these rows have product shape

    Z=product_(d>1,gcd(d,15)=1) W_d^(u_d) W_(5d)^(v_d),
    0<=v_d<=u_d.

The identities W_d(chi)=W_d W_(5d), W_(5d)(chi)=W_(25d), and W_j(C_3)=W_j W_(3j) for3 not dividing j give both Z|Z(chi) and Z|Z(C_3).
They preserve every root and multiplicity; neither derivative is critical at these nonzero target preimages.
Conversely, if a representative Y has YJ an allowed complete product, then both YJ and J have class in G_N, so Y does too and Pi_N(c)=0.
This proves the equivalence, including necessity without any forward-divisibility assumption.

### PC4. A paid fresh nonsquare factor and the entire degree cost

Let D_bad=deg(Y_seed B)=D_seed+D_B.
The specified choice of k makes n_fresh prime to15, congruent1 modulo10L and strictly greater than max(30L,4D_bad^2).
At most one increment of k_0 is needed because10L is nonzero modulo3.
C664's safe period gives B_(n_fresh)=B_1=1 in the FULL R_N.
No search for a prime in a progression is used.

For every positive odd n=product_p p^(a_p),

    varphi(n)^2/n=product_p p^(a_p-2)(p-1)^2>=1.

For a_p=1, (p-1)^2/p>=1 for p>=3; larger a_p only increase the factor.
Thus deg W_(n_fresh)>=sqrt(n_fresh)/2>D_bad.
Since W_(n_fresh) is squarefree, at least one of its irreducible factors psi does not divide the entire Y_seed B.
It is also absent from Z because its primitive order exceeds30L.
Set Y=Y_seed Z B_(n_fresh)^3.
The chosen psi has exact multiplicity3 in Y and YB; all other newly introduced factors have multiplicity at least3, and previous factors had multiplicity at least2.
This proves both nonsquareness statements and the support floor.
Since n_fresh is coprime15, its whole B factor has both stronger forward divisibilities, so the two forward-square inequalities multiply with those of Y_seed.
Its class is1, and Y represents c.

The exact degrees in PH2 follow from the complete totients and exact division J|C_comp; no smooth contribution is omitted.
Since deg B_n=(n-1)/2, the final cost is exactly PH3 before its displayed upper bound.
In the canonical specialization one may also write

    w_deg=q(25m+Q+D_C+degZ+3(n_fresh-1)/2),

which includes every completion, row and fresh-factor cost.
The finite quotient's dimension cannot replace this full polynomial degree.

### PC5. All-primary canonical divisibility and the full root/gate

C649 applies to EVERY polynomial representative of PH4, independently of completeness of Y.
It gives the low derivative, D_0 in phi^(4m), the power identity, the unique corrected eleventh root and the full gate exactly as in PH5.
It remains to prove the global canonical remainder, since finite jets alone would not do so.
From U_0(chi)=phi^(4m)C_00 one gets

    U_0(chi)^3+R_0=phi^(12m)(C_00^3+V_0)
                  =phi^(12m)D_0.

The phi part is divisible by phi^(16m), hence by the required phi^(14m).
By the proven Y|Y(chi)^2, also Y|Y(chi)^3.
The factor X^(2m) divides X^(6m), so H_0 divides C_00^3; it plainly divides V_0.
Therefore H_0 divides D_0, and gcd(H_0,phi)=1 proves U_0 divides the entire displayed difference.
Since degR_0=26m+degY+D_B<30m+degY=degU_0, this is the unique monic-division remainder.

The X component of U_0 divides its C_3 pullback, because C_3 has a simple zero at0.
The phi component also divides its C_3 pullback: cubing permutes primitive fifth traces and C_3' is a unit there.
Together with Y|Y(C_3)^2 these facts prove U_0|U_0(C_3)^2, with no first-power conclusion.
The quotient R_0/U_0=B/phi^(2m) shows that every U_0 factor other than phi is saturated and that phi has exact orders14m and12m.
The endpoint X is saturated as well, since B contains X^(Q-m) with Q>m.

The selected psi is neither X nor phi and has exact multiplicity3 in both U_0 and R_0.
Their q-th powers thus have a factor of multiplicity3q and no common Frobenius factor larger than q, separately for each polynomial.
Raising the monic division identity to q gives the canonical identity for U,R, with strict degree retained.
Every root/gate ingredient raises to its q-th power, including beta,B,H_0,C_00,D_0,Z_0,S and the precise moduli6mq,8mq.
This proves PH5--PH6.

### PC6. Separate odd parts and the actual integer layer/Haar construction

The low jet is a square and its modulus X^(4m) has zero derivative, giving X^(4m)|Y'.
Write Y=J_U^2W_U with W_U squarefree; J_U is a low unit, so X^(4m)|W_U'.
The fresh psi makes W_U nonconstant.
Since a nonconstant squarefree polynomial has nonzero derivative, degW_U>=4m+1.
The high target gives

    V_0=B^(-6)+beta B^(-12)S modulo phi^(8m).

This is a square class: beta is a square, S is a square and all displayed inverse powers are even.
Differentiating this congruence retains the full phi^(8m), whose derivative is zero.
In V_0=J_G^2W_G the square part is a high unit, so phi^(8m)|W_G'.
The same fresh psi gives W_G!=1 and degW_G>=16m+1.
These are separate squarefree odd parts, with no equality assertion.

For a layer in the strict window of PH8, its power-of-two lambda is greater than4mq and at most8mq.
Hence lambda/(2q) and lambda/q are even integers and 12m-lambda/q is even and at least4m.
The correction is consequently square and in phi^(4m), with unnormalized correction exactly S^q.
The actual integer a_b remain unchanged.
The identity YJ=C_comp Z B_(n_fresh)^3 proves the ENTIRE complete factorization of V_0 used in PH9, even when J and Y separately are partial.
The accepted integer trace identities give F_j modulo2=W_j for odd j and F_(2^b*5) modulo2=phi^(lambda_b), with integer degree2lambda_b.
Thus the full PH9 product reduces to V_0^q phi^(12mq)=R, and its degree is

    q degV_0+2 sum_b a_b lambda_b
       =q(2m+degY+D_B)+24mq=w_deg.

For each integer trace factor the cyclotomic pullback is z^(degF_j)F_j(z+z^(-1))=Phi_j(z).
Every cyclotomic polynomial has all roots on the unit circle and is monic, so its normalized logarithmic Haar mean is zero; the logarithmic singularities at its finitely many zeros are integrable.
Applying this exact factor identity, including F_4 and every actual five layer, proves the claimed mean for the square of the entire product.
No other integer residual polynomial or same-T condition is inferred.

### PC7. The strong-C3 obstruction on primitive-order cycles

Fix odd n>1 prime to3.
On its primitive trace set, C_3 is a permutation and its derivative is nonzero, since the only critical trace1 has order3.
Let a(alpha) and b(alpha) be the multiplicities of Y and J.
If Y|Y(C_3), then a(alpha)<=a(C_3(alpha)); following each finite permutation cycle makes all these inequalities equalities.
If YJ is complete, a(alpha)+b(alpha)=nu_n is constant on ALL primitive-order-n traces.
Therefore b is C_3-invariant as well.
Both polynomial multiplicity functions are also Frobenius-invariant, and trace indices already identify z with z^(-1).

At order31, the exponent subgroup

    <2,-1>={1,2,4,8,16,30,29,27,23,15}

has order10 in the30-element unit group.
The three cosets are exactly the three degree5 irreducible trace groups.
The exponent3 lies outside this subgroup and 3^3=27 lies inside it, so it cycles the three cosets.
Hence C_3-invariance forces b constant across all three groups.
For H=f_31, C670 gives precisely one primitive-order31 trace group with multiplicity1.
On primitive-order31 roots chi is the fifth-power trace permutation, and5 is prime to31; it commutes with Frobenius and inversion.
Its preimage of that one group is exactly one of the three groups, with multiplicity1 because chi' is nonzero there.
Thus J=H(chi) has multiplicities1,0,0 on the three groups, contradicting the forced invariance.
This proves the sharp limitation without assuming a pointwise inverse relation between C_3 and chi.

### PC8. Direct formal target calculation for m=12

C670's adopted finite theorem gives ell(f_31)=10 modulo16 and primitive order31; write ell(H)=10+16z with z in Z_2.
Here degB=20+25=45<48, and the chosen layers a_0=144q are even, have total weight144q=12mq and give S=0.
Define the actual completed pair

    Ltilde(t)=[phi(t)^84 H(t)h_32(x(t))]^(-1),
    u(X)=Ltilde(X)^2,
    v(X)=X^(-164)H(chi(X))^(-7).

Its two jets are exactly PH4 for N=48: the low modulus is X^48 and the high modulus phi^96.
There is no correction term because S=0.
All high inverse powers are units.
The exact C652 calibrations give

    ell(phi)=-1, ell(h_Q)=Q/2, ell(f(x))=ell(f)/5,
    ell(Ltilde)=7m-ell(H)-Q/10,
    N_high(X)=phi(x(t))^2, ell(N_high(X))=-2/5.

The scalar H in the rank-four high algebra has norm H^4.
For the general zero-correction completed high component X^(5m-7Q)H(chi)^(-7), direct evaluation yields

    Phi(u,v)=ell(N_high(v))-(4/5)ell(u)
       =-(2/5)(5m-7Q)-28ell(H)
                         -(8/5)(7m-ell(H)-Q/10)
       =(-330m+74Q-660ell(H))/25.

At m=12,Q=32 this is

    (-1592-660ell(H))/25
          =64(-128-165z)/25=0 modulo64.

C654's lift-independent finite character is Pi_48=Phi/2 modulo32, so Pi_48(c)=0.
This computes the completed formal pair before constructing Y and invokes no original-input vanishing theorem.

### PC9. Full order completion and numerical costs in the example

H'=t^4 has no common root with H, and chi'=phi^2 has no root in J because J modulo phi is1.
Thus J=H(chi) is squarefree.
If a trace of order n maps under chi to a primitive order31 trace, then n/gcd(n,5)=31, so n is31 or155.
Both orders occur: fifth powering permutes primitive31 roots, and each such root has four further fifth-root preimages of order155.
After inverse pairing, J has degrees5 and20 in these two order groups, respectively, totaling25.
Therefore mu_max=1, E_pad=4, M={31,155}, M_smooth is empty, and

    C_comp=W_31^4W_155^4,
    D_C=4(15+60)=300, D_seed=300-25=275.

For N=48 one has L=128,e=384,D_bad=275+45=320 and

    75L^2(e+1)=473088000,
    K=max(3840,409600)=409600,
    k_0=321, n_fresh=1+1280*321=410881.

This n_fresh is1 modulo3, so no increment is required.
Its fresh-factor cost is3(410881-1)/2=616320, giving degY<=473704595.
Then r_deg=q(360+degY), w_deg=q(357+degY) and the exact gap is3q.
The completed product is V_0=X^44 C_comp Z B_(410881)^3 and all five-layer weight is the unchanged integer factor F_5^(144q).
This proves every bound in PH11, together with the full canonical, weak-forward, odd-part, maximal-q and integer-Haar assertions.
It remains a synthetic compatibility theorem, subject to the precise realization boundary in the statement.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision partial-h-completion-open

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:40 |
| status | open |
| reason | Register the exact finite criterion for a complete product YH(chi) with partial H, both forward-square divisibilities, original support floor and paid fresh nonsquare factor; retain the elementary smooth-order proof and all actual completion/row/fresh costs. The full canonical remainder, corrected root/gate, separate maximal q and odd parts, and conditional original-layer integer zero-Haar lift hold without whole H. The order31 multiplicity-cycle obstruction prevents the strong C3 upgrade for f31. The concrete m12, Q32 family has directly computed formal zero character, full costs and gap3q. Root and original_law are contributors; fresh isolated whole review is required. No SAME-T modulo4/modulo8, characteristic-zero realization, original A0=24 realization/exclusion or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire partial-H completion and specialization](#partial-h-completion-statement) | PH1--PH11: every H and zero-character finite target, both forward squares and complete product, actual support multiplicity and global nonsquareness, full canonical/root/gate/layer/Haar/q/cost scope, strong-C3 obstruction and synthetic m12 example. |
| argument | [Complete construction and boundary proof](#partial-h-completion-argument) | PC1--PC9: smooth trace irreducibility, finite order closure, every original root multiplicity, full finite rows and period, totient/fresh factor, all-primary remainder, derivatives, layers/Haar, tripling-cycle obstruction, direct formal norm and paid example. |
| dependency | [Adopted finite composition and character](Yin_C_G0654_v1.md#decision-whole-reviewed-2026-10-23) | H(chi) lies in G_N for every formal H, full high norm Phi, integrality and original-depth Pi_N; not a premise that Y or H is globally whole. |
| dependency | [Adopted all-depth kernel generation](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G_N=ker Pi_N, all original higher-five sources, exact5L complete rows, full predivision period and finite degree/exponent/support bounds. |
| dependency | [Adopted complete forward construction](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Actual chosen row pattern, strong forward multiplicities, support-floor adjustment, safe invisible period and totient method, canonical and original-layer integer-Haar interfaces; its extra whole-H implication is broadened here with a complete proof and weaker forward conclusion. |
| dependency | [All-representative CRT gate](Yin_C_G0649_v1.md#statement) | Full target for every polynomial representative, low derivative, high error/power identity, unique corrected6m root and8m gate; no original integer existence is imported. |
| dependency | [Adopted calibrated formal character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | ell(phi), ell(h_Q), inverse-composition scaling and high norm of X, used directly on the explicit legal completed pair. |
| dependency | [Adopted exact f31 character and order](Yin_C_G0670_v1.md#decision-whole-reviewed-2026-10-24) | Only the proven m12 solution f31, ell(f31)=10 modulo16, irreducibility and primitive order31. Its accepted native evidence is reused without rerun or new native assertion. |
| dependency | [Complete primitive trace definitions](Yin_C_G0608_v1.md#argument) | Whole primitive root sets, inverse pairing, B_n divisor partition, degrees and squarefreeness; no unrelated finite computation is used. |
| dependency | [Accepted integer trace/Haar interface](Yin_C_G0199_v2.md#statement) | Exact monic integer trace reductions and complete Haar factorization at the accepted chain scope explicitly retained by C667; every actual layer and degree remains present. |
| support | [Exact realization boundary](#exact-realization-boundary) | Synthetic canonical/Haar compatibility does not supply one shared integer T, its actual divided remainders or the original characteristic-zero field and reciprocal-polynomial hypotheses. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:54 |
| status | proved |
| reason | Adopt the complete partial-H theorem after full main reading and fresh independent entire R895v2. Every zero-character target admits a complete product YH(chi) with paid forward squares, multiplicity floor, nonsquareness and all actual costs. The full canonical/gate/q/odd-part and given-layer integer-Haar construction extends without separately whole H; the order31 strong-C3 obstruction and synthetic m12 family are proved. Use only the corrected v2 review: empty M gives C_comp=J and Y_seed=1, while v1's overbroad endpoint wording remains historical. No same-T or original characteristic-zero realization is supplied by this theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire partial-H completion and specialization](#partial-h-completion-statement) | PH1--PH11: every H and zero-character finite target, both forward squares and complete product, actual support multiplicity and global nonsquareness, full canonical/root/gate/layer/Haar/q/cost scope, strong-C3 obstruction and synthetic m12 example. |
| argument | [Complete construction and boundary proof](#partial-h-completion-argument) | PC1--PC9: smooth trace irreducibility, finite order closure, every original root multiplicity, full finite rows and period, totient/fresh factor, all-primary remainder, derivatives, layers/Haar, tripling-cycle obstruction, direct formal norm and paid example. |
| dependency | [Adopted finite composition and character](Yin_C_G0654_v1.md#decision-whole-reviewed-2026-10-23) | H(chi) lies in G_N for every formal H, full high norm Phi, integrality and original-depth Pi_N; not a premise that Y or H is globally whole. |
| dependency | [Adopted all-depth kernel generation](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G_N=ker Pi_N, all original higher-five sources, exact5L complete rows, full predivision period and finite degree/exponent/support bounds. |
| dependency | [Adopted complete forward construction](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Actual chosen row pattern, strong forward multiplicities, support-floor adjustment, safe invisible period and totient method, canonical and original-layer integer-Haar interfaces; its extra whole-H implication is broadened here with a complete proof and weaker forward conclusion. |
| dependency | [All-representative CRT gate](Yin_C_G0649_v1.md#statement) | Full target for every polynomial representative, low derivative, high error/power identity, unique corrected6m root and8m gate; no original integer existence is imported. |
| dependency | [Adopted calibrated formal character](Yin_C_G0652_v1.md#decision-whole-reviewed-2026-10-23) | ell(phi), ell(h_Q), inverse-composition scaling and high norm of X, used directly on the explicit legal completed pair. |
| dependency | [Adopted exact f31 character and order](Yin_C_G0670_v1.md#decision-whole-reviewed-2026-10-24) | Only the proven m12 solution f31, ell(f31)=10 modulo16, irreducibility and primitive order31. Its accepted native evidence is reused without rerun or new native assertion. |
| dependency | [Complete primitive trace definitions](Yin_C_G0608_v1.md#argument) | Whole primitive root sets, inverse pairing, B_n divisor partition, degrees and squarefreeness; no unrelated finite computation is used. |
| dependency | [Accepted integer trace/Haar interface](Yin_C_G0199_v2.md#statement) | Exact monic integer trace reductions and complete Haar factorization at the accepted chain scope explicitly retained by C667; every actual layer and degree remains present. |
| support | [Exact realization boundary](#exact-realization-boundary) | Synthetic canonical/Haar compatibility does not supply one shared integer T, its actual divided remainders or the original characteristic-zero field and reciprocal-polynomial hypotheses. |
| review | [Corrected independent entire partial-H finding](../audits/reviews/Yin_R_G0895_v2.md#whole-partial-h-canonical-haar-v2-finding) | Whole PH1--PH11 and PC1--PC9, every smooth/partial multiplicity and endpoint, finite character/row/period, paid fresh factor, all-primary canonical/root/gate/q/odd parts, exact layers/Haar, strong-C3 obstruction, formal m12 norm and complete numerical costs; v1 endpoint error explicitly corrected. |

