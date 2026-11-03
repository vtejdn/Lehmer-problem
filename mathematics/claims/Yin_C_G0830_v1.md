---
author: Yin
---

# Next-half transport and a complete four-coset screen for the fixed cyclotomic family

Human author Yin.
Root proposed the next original-half response and four-coset screen.
Primitive_second_eight checked the complete mixed-characteristic carry and positive common-word argument, derived the higher-source exponent and corrected half-period, and assembled this theorem and its exact finite-screen scope.
C828's accepted native image, ranks and positive target words are reused at their selected scope; no new native source, image, word or residual calculation is performed here.
The unchanged symbolic theorem is adopted through [whole independent R1049](../audits/reviews/Yin_R_G1049_v1.md#whole-finding), as selected by the [current decision](#decision-whole-reviewed-2026-10-28).

## Statement

### A. Actual family and normalized next half

For positive j use C_j(z+z^(-1))=z^j+z^(-j), with C_0=2,C_1=X and C_(j+1)=XC_j-C_(j-1).
For n>2 use the complete monic primitive trace F_n defined by z^(varphi(n)/2)F_n(z+z^(-1))=Phi_n(z).
For odd n>1 put B_n=1+sum_(j=1..(n-1)/2)C_j.
Fix

    P=F_15=X^4-X^3-4X^2+4X+1, f=Pbar=X^4+X^3+1,
    V=F_960, J=P^4V,
    H_0=(X-2)^2F_3^2F_5^3F_9^4B_187,
    T_0=JH_0^2, deg J=144, deg T_0=374.

Let M consist of all finite actual products of X-2 and B_n(C_(3^a5^b)), with n>1 odd prime to15 and a,b>=0, including the empty product, all repetitions and complete-factor overlaps.
For Q=(X-2)^k product B_n(C_(3^a5^b))^e retain T_Q=T_0Q and

    deg Q=k+sum e*3^a5^b(n-1)/2,
    original trace degree=374+deg Q,
    full reciprocal degree=2(374+deg Q).                       (ST1)

Every q value in this cost is its ACTUAL integer, not a residue representative substituted into a prior word.
At the SAME original divisor define

    a_Q=rem_(T_Q)(T_Q(C_2))/2,
    b_Q=rem_(T_Q)(T_Q(C_3))/3,
    c_Q=rem_(T_Q)(T_Q(C_5))/5,
    F_Q=rem_(T_Q)(2c_Q^2-3a_Q^5),
    G_Q=rem_(T_Q)(c_Q^3-2b_Q^5),
    X_(epsilon,Q)=rem_(T_Q)(b_Q^2-a_Q^3+epsilon G_Q),
    epsilon in{1,-1}.

Every prime division is a genuine integer coefficient division before modular reduction.
All restrictions below use the full original weighted system, with the exact global equivalence supplied by C824/C820.
Write

    R_j=F_2[X]/f^j, p(Y)=Y^2+Y+1,
    S_(3,j)=F_2[Y]/(Y+1)^j, S_(5,j)=F_2[Y]/p(Y)^j,
    lambda=X^3+X, chi=X(X^2+X+1)^2,
    delta=(V-P^32)/2 in Z[X],
    B_F=(Z/4)[X]/(V,2P^28),
    Omega(Q)=Q(C_5)^2/Q(C_2)^5 in B_F^times.

Use the adopted C826 maps Xi_16 and Theta, and define their one further source extension by

    Xi_16(Q)=(Qbar mod f^16,Qbar(Y) mod(Y+1)^24,Qbar(Y) mod p(Y)^12),
    Xi_plus(Q)=(Qbar mod f^16,Qbar(Y) mod(Y+1)^28,Qbar(Y) mod p(Y)^14),
    Theta(Q)=(Xi_plus(Q),Omega(Q)),
    Xi_2(Q)=(Qbar mod f^16,Qbar(Y) mod(Y+1)^32,Qbar(Y) mod p(Y)^16),
    Theta_2(Q)=(Xi_2(Q),Omega(Q)).                             (ST2)

Every coordinate comes from the SAME actual cofactor and is a unit.
The full F8 gate depends exactly on Omega by C820's fixed original-base character criterion.

<a id="next-normalized-second-half-response"></a>
**Definition (next normalized second half and source response).**
Assume original X2 at Q.
Form the genuine global half before J restriction,

    x_(epsilon,Q)=[X_(epsilon,Q)/2]_J in Z[X]/J,
    beta_Q=b_Jbar/f^6 in R_30,
    gamma_Q=c_Jbar/f^4 in R_32.

If x_(epsilon,Q)bar is divisible by f^8 in R_36, define

    g2_(epsilon,Q)=(x_(epsilon,Q)bar/f^8) mod f^4 in R_4.

For an ACTUAL K with Xi_plus(K)=1 define the NEXT source increments

    r_K=(Kbar(Y)-1)/p(Y)^14 mod p(Y)^2 in S_(5,2),
    s_K=(Kbar(Y)-1)/(Y+1)^28 mod(Y+1)^4 in S_(3,4),
    L2_Q(r,s)=deltabar[beta_Q^2 p(X)^28 r(lambda)^2
                       +gamma_Q^3 (X+1)^28 s(chi)] mod f^4.   (ST3)

These r,s differ from C826's earlier source increments; their full required source depths are16 and32.
The displayed binary divisions precede projection.
The true integer carry proves both-direction preservation of original X2 and of the half class modulo f^8, and then

    g2_(epsilon,QK)-g2_(epsilon,Q)=L2_Q(r_K,s_K).              (ST4)

No Omega(K)=1 or F4 hypothesis is needed for this transport.
The two g2 signs agree at this precision because their genuine-half difference is G_Q of binary f-order12.
They are not identified at higher precision or in the complete X4 quotient.

### B. Higher-source exponent, corrected periods and actual direction

The binary unit exponents in Xi_2 divide240,32,48 and the full Theta_2 exponent divides960.
In particular every actual Q satisfies Theta_2(Q^960)=1, so its NEXT r,s increments are zero.
This conclusion is proved directly at source depths32/16, not inferred from the old Theta exponent.

In the source3 coordinate let e=Y+1 and put

    c_0=(1,1+e^16,1;1), d_0=(1,1+e^31,1;1),

in the order(first,source3,source5;Omega).
For every allowed actual rectangle the exact half-period is

    Theta_2(B_(n+480)(C_q))
       =c_0 d_0^(1_(3|q)) Theta_2(B_n(C_q)).                 (ST5)

Thus n960 and q480 are sufficient full periods, with no least-period claim.
The extra e^31 term pays the failed old depth32 nonunit cancellation.
The actual factors B_481 and B_481(C_3) have images c_0 and c_0d_0, respectively, and trace degrees240 and720.
Together with the old4192 endpoint/lower-row labels of C826 they form a sufficient4194-label alphabet for the full Theta_2 image.
The old lower rows are n in{2<=n<=479:gcd(n,480)=1} and the33 ACTUAL smooth q representatives fixed in C826 ST5, of sum539881; their n degree sum is15296.
Set

    D_2=1+539881*15296+240+720.

Every attained Theta_2 image has an actual representative with4194 exponents in0..959, cofactor degree at most959D_2 and original trace degree at most374+959D_2.
Every reciprocal degree is twice the corresponding original trace degree.
This proves sufficiency of the labels, not distinctness of images or insufficiency of the former4193 labels.

The exact positive word

    D_shift=B_481 B_481(C_3), deg D_shift=960

satisfies Theta(D_shift)=1 and has next increments(r,s)=(0,e^3).
It preserves original full F8, and when g2 is defined its exact response is

    g2_(epsilon,Q D_shift)-g2_(epsilon,Q)
       =f^3 deltabar gamma_Q^3 (X+1)^31 mod f^4 !=0.          (ST6)

Its added trace/reciprocal costs are960/1920.
This is one actual source direction, not a claimed repair of a particular target or an X4 witness.

### C. Entire Theta fibers and four representatives per remaining old fiber

<a id="next-source-kernel-and-four-coset-screen"></a>
**Definition (actual next source kernel and four-coset screen).**
Let Sigma_2 consist of the pairs(r_K,s_K) in ST3 from ACTUAL K in M with Theta(K)=1.
It is an intrinsic F_2 subspace of S_(5,2) direct_sum S_(3,4), identified with the full kernel of Theta_2(M)->Theta(M); its dimension is not computed here.
For any actual reference Q satisfying F8/X2 and xbar divisible by f^8, the following are equivalent:

1. g2_Q is in L2_Q(Sigma_2).
2. An actual Theta-kernel extension QK passes original F8 and has BOTH genuine second halves zero modulo f^12 in their binary J classes.
3. An actual member of the ENTIRE Theta(Q) fiber has those same properties. (ST7)

The proof uses actual K_1=Q^959Q', K_2=Q^960 and common word QK_1=Q'K_2, of original degree374+960deg Q+deg Q'.
The new exponent proves the higher increments of K_2 vanish; no formal inverse integer polynomial is used.
A target outside even the AMBIENT image of L2_Q excludes both complete X4 gates throughout that Theta fiber.
A target in the ambient image need not lie in the actual image; even ST7 only gives half vanishing through f^12, not complete X4.

Now take the16 exact remaining references R_i of adopted C825, and the actual kernel W_plus, common map Phi_R and attained target words of adopted C828.
They have dimensions59 and57, respectively, with each target attained.
Therefore each target preimage has exactly four vectors in W_plus and exactly four corresponding Theta images.
Choose the two independent nullspace vectors by ordered elimination of the59 retained basis-image vectors, tracking their59-bit coefficients, and obtain actual positive words N_1,N_2 by multiplying the corresponding retained basis words.
There are exactly two zero reductions; their distinct current basis indices prove independence and their dimension proves completeness.
No new nullspace coefficient or word is numerically evaluated here.
For each retained target word K_(i,0), the four representatives are

    Q_(i,e1,e2)=R_i K_(i,0) N_1^e1 N_2^e2,
    e1,e2 in{0,1}.                                           (ST8)

These four Theta fibers cover every possible original F8 plus f^8-half-zero member of Xi16(R_i).
All factors have actual positive exponents; each literal original degree is374+deg R_i+deg K_(i,0)+e1 deg N_1+e2 deg N_2, with reciprocal degree twice that amount.
Using the original C826 alphabet and the proved exponent960, each combined kernel word can alternatively be represented at cost at most959D_alphabet, where D_alphabet=1+539881*15296+240.
The stronger Theta_2 exponent justifies preservation of g2 under such final exponent reduction, though no existing fixed word is silently changed.

For all64 representatives, the response coefficient classes are the SAME accepted values

    deltabar=1+X^8,
    beta_Q^2=gamma_Q^3=X^6+X^10 in R_4.                      (ST9)

These follow from C825's reference values and C824's Xi16 coefficient constancy; no new response columns or ranks are computed.
The actual g2 targets still belong to their respective original inputs.
If ALL64 targets are outside the complete ambient image of this L2 map, then the ENTIRE exact monoid M has no simultaneous original F8/either-X4 input at this fixed base T_0.
The proof combines the four-fiber coverage with C825's exclusion of the other16 old fibers.
If any target is an ambient member, that case remains unresolved; no actual cofactor correction or full X4 result follows.
No outcome of those64 tests is asserted in this theorem.

Every input in this fixed family is fully cyclotomic, with total logarithmic Mahler measure0 and the retained reducible base factors.
Neither possible screen outcome supplies the irreducible reciprocal nontorsion input with controlled total positive measure required by the C720 same-input exactness route.
A local f-order increase is not an extra global coefficient-divisibility bit.
No irreducible lift, improved degree/precision asymptotic, complete X4 witness, higher-modulus result or unrestricted G0001 conclusion is claimed.

## Complete argument

The original carry and source argument below is complete at the new precisions; adequate C824/C826 interfaces are invoked at their adopted scope rather than reproved.
The native evidence for the finite rank and reference premises remains the exact selected C828/C825 evidence, with no new execution.

### NH1. Actual kernel, genuine lifts and the retained original weights

Use P=F_15, f=Pbar, V=F_960, J=P^4V, delta=(V-P^32)/2, A=Z[X]/J and A_4=A/4A.
Retain the actual monoid M, full integer T_Q=JH_0^2Q and own-divisor canonical a_Q,b_Q,c_Q,F_Q,G_Q,X_(epsilon,Q) of C824.
All original prime divisions precede J restriction.
For an ACTUAL K in M with Xi_plus(K)=1, put k_p=K(C_p) in A.
There is no Omega(K)=1 hypothesis in the transport calculation.
C815's full source identities give

    k_2bar=1 mod f^32,
    k_3bar=1 mod f^14,
    k_5bar=1 mod f^28.

After canonical integer J reduction, choose genuine lift classes

    k_2=1+P^32 H+2T,
    k_3=1+P^14 U+2R_3,
    k_5=1+P^28 W+2S in A.                         (NH1)

Each even remainder is divided by2 over Z; these are not modular halves.
As in C824, choose actual integer lifts of the original restricted coefficients

    a_J=P^8 A_0+2P^4 A_1,
    b_J=P^6 B_0+2P^4 B_1,
    c_J=P^4 C,
    beta_Q=b_Jbar/f^6 in R_30,
    gamma_Q=c_Jbar/f^4 in R_32.

Here beta_Q=B_0bar and gamma_Q=Cbar at the stated precisions.
The exact original weighted difference in A is

    Delta X_epsilon=(k_3^2-1)b_J^2-(k_2^3-1)a_J^3
                    +epsilon(k_5^3-1)c_J^3
                    -2epsilon(k_3^5-1)b_J^5.       (NH2)

All full factors and original scalar weights remain those of C773/C824.

### NH2. Complete modulo4 carry and the genuine next-half formula

In A_4 retain P^36=-2P^4delta, 2P^36=0 and P^68=0.
The true coefficient expansions are

    b_J^2=P^12 B_0^2,
    a_J^3=P^24 A_0^3+2P^20 A_0^2 A_1.

The square-weight term is exactly

    (k_3^2-1)b_J^2
      =2P^26 U B_0^2+P^40 U^2B_0^2
      =2P^26 U B_0^2-2P^8delta U^2B_0^2.          (NH3)

The a-weight is unchanged from C824 SX3, since its source depth remains16:

    k_2^3-1=3P^32H+2T+3P^64H^2 in A_4.

After multiplication by a_J^3, the term3P^56H A_0^3 lies in2P^24 A_4 by the true P^36 carry, the term2T P^24 A_0^3 lies there directly, and every other product vanishes using2P^36=0 and P^68=0.
Thus the entire a contribution belongs to2P^24 A_4.
For the c-weight, the cubic expansion is

    k_5^3-1=3P^28W+2S+3P^56W^2 in A_4.

The omitted P^84W^3 and2P^56W^2S vanish by the same relations; the other mixed terms are multiples of4.
Multiplying by c_J^3 gives exactly

    (k_5^3-1)c_J^3
      =3P^40W C^3+2P^12S C^3+3P^68W^2C^3
      =-6P^8delta W C^3+2P^12S C^3.              (NH4)

Finally(k_3^5-1)b_J^5 has binary f-order at least14+30=44, exceeding36.
Since A_4 is free over Z/4, its product by2 vanishes.
This removes the final term of NH2 with its actual coefficient2 paid.
Equations NH3--NH4 and the a bound therefore yield ACTUAL integer classes N,O in the free quotient A such that

    Delta X_epsilon
       =2P^8delta(B_0^2U^2+epsilon C^3W)
                          +2P^12N+4O.             (NH5)

The coefficient2 signs agree modulo4; epsilon is retained until binary reduction.
Lifting the A_4 equality to A supplies N,O, so no division by2 inside a ring with2-torsion occurs.

NH5 preserves the original X2 gates in both directions: first the restricted binary residual is unchanged, then C824's full outside-J coverage transfers this to the original global gates.
If X2 holds at Q, form its genuine global half and that of QK before restriction, x_(epsilon,Q)=[X_(epsilon,Q)/2]_J.
Halve NH5 in A and only then reduce modulo2 and project:

    x_(epsilon,QK)bar-x_(epsilon,Q)bar
       =f^8 deltabar(beta_Q^2 u_K^2+gamma_Q^3 w_K)
                                                mod f^12,
    u_K=Ubar mod f^2,
    w_K=Wbar mod f^4.                              (NH6)

In particular the half class modulo f^8 is invariant in both directions under such an actual multiplier.
If that class is zero, define

    g2_(epsilon,Q)=(x_(epsilon,Q)bar/f^8) mod f^4 in R_4.

The binary f^8 division precedes projection and is well-defined at this precision.
The two g2 signs agree because their genuine-half difference is G_Q of binary f-order12, which becomes0 modulo f^4 after this division.
This identifies neither the full second halves nor the complete X4 gates.

### NH3. The next eight source bits and exact ambient response

For an actual Xi_plus-kernel K put

    r_K=(Kbar(Y)-1)/p(Y)^14 mod p(Y)^2 in S_(5,2),
    s_K=(Kbar(Y)-1)/(Y+1)^28 mod(Y+1)^4 in S_(3,4).

These divisions require K(Y) modulo p(Y)^16 and(Y+1)^32, respectively.
The full source identities p(lambda)=p(X)f and chi+1=(X+1)f give

    u_K=p(X)^14 r_K(lambda) mod f^2,
    w_K=(X+1)^28 s_K(chi) mod f^4.

Consequently the next response is

    L2_Q(r,s)=deltabar[beta_Q^2 p(X)^28 r(lambda)^2
                       +gamma_Q^3 (X+1)^28 s(chi)] mod f^4,
    g2_(epsilon,QK)-g2_(epsilon,Q)=L2_Q(r_K,s_K).  (NH7)

The two source spaces each have dimension4, so L2_Q is an F_2-linear map from an eight-dimensional AMBIENT space into the16-dimensional R_4.
No arbitrary source pair is assumed to be attained by an actual cofactor.
The source increments add on the actual Xi_plus kernel: the product cross terms vanish after the displayed divisions and projections.
The needed beta_Q^2 and gamma_Q^3 classes are constant on each Xi_plus fiber, already by the stronger precision supplied from equality of the old Xi16 source coordinates in C824 SX4.
No Omega condition was needed for NH7; imposing Omega(K)=1 is separately sufficient to preserve full original F8 through C820's exact character.

### NH4. Entire Theta-fiber ambient obstruction with positive common words

Let Q be an actual reference with original F8 and X2, and suppose x_(epsilon,Q)bar is divisible by f^8.
Let Q' be ANY actual member of the SAME Theta fiber, Theta(Q')=Theta(Q).
Use the actual positive words

    K_1=Q^959Q', K_2=Q^960,
    Theta(K_1)=Theta(K_2)=1,
    QK_1=Q'K_2.

The identities use ONLY the adopted exponent960 of the EXISTING Theta, with source depths16,28,14 and Omega.
They do not assert an exponent or period for the new source depths16/32 of NH3.
Their common original trace degree is374+960deg Q+deg Q', with reciprocal degree twice that number.
All words retain their actual nonnegative multiplicities.

Full F8 holds at Q' and the common word by equality of Omega and the exact global character criterion.
The two-direction X2 preservation and f^8-half invariance in NH5--NH6 transfer the remaining reference hypotheses to Q' and the common word.
Thus every g2 used below is defined.
The response coefficients are the same throughout this Theta fiber, which is contained in one Xi16 fiber.
Applying NH7 on BOTH paths to the common actual polynomial gives

    g2_(epsilon,Q')-g2_(epsilon,Q)
      =L2_Q(r_(K_1)+r_(K_2),s_(K_1)+s_(K_2))
      in Im L2_Q.                                  (NH8)

This two-path argument does not need zero new increments for K_2.
NH6 below separately proves that they are zero by direct higher-source unit-group bounds, so the formula may then be simplified without assuming an unproved period.
Therefore if g2_(epsilon,Q) is outside this full ambient image, EVERY actual cofactor in this Theta fiber fails the original X_epsilon4 gate.
The lowest g2 signs agree, so the same ambient obstruction excludes both signs.
Ambient membership proves neither actual correction attainment nor a complete X4 solution.
No value of L2_Q or g2_Q has been computed here; an initial unit modulo f alone is not the full target in R_4.

### NH5. Conditional four-coset preparation and the depth32 period boundary

Adopted C828 supplies the complete joint kernel W_plus of dimension59, the common projected map Phi_R of rank57 and every attained reference target(t_R,g_R).
Each target preimage is therefore an affine coset of a two-dimensional kernel and has exactly four vectors.
Because C826's alpha_plus is injective on the actual Theta-to-Xi16 kernel, these are four distinct Theta kernel images, not four independent choices of small source coordinates.
Each vector has an actual positive word representative by C826.

Choose one actual attained word K_0 and actual positive words N_1,N_2 for a basis of ker(Phi_R|W_plus).
Then the four ACTUAL references

    Q_(e1,e2)=R K_0 N_1^e1 N_2^e2,
    e1,e2 in{0,1},

satisfy original F8/X2 and have genuine second halves zero modulo f^8 by C826.
Their literal original degree is

    374+deg R+deg K_0+e1 deg N_1+e2 deg N_2.

Alternatively reduce the final kernel label exponent vector modulo960 using C826, paying at most374+deg R+959D_alphabet for each chosen reference, with reciprocal degree twice that number.
The old Theta argument alone does not establish preservation of the new g2 class under this replacement; NH6 supplies the required stronger exponent and fiber argument.
Each chosen actual reference would require its own genuine original half data for NH7--NH8.

These four Theta values cover EVERY possible F8 plus f^8-half-zero member of the Xi16(R) fiber.
Indeed C826's comparison K_1=R^959Q', K_2=R^960 has Theta(K_2)=1, so its equivalent kernel extension has exactly Theta(Q'), and its kernel vector is one of the four target preimages.
If a separately authorized complete ambient L2 test is negative at one actual representative of EACH of the four Theta fibers, NH8 would exclude original F8/either-X4 throughout this Xi16(R) fiber.
Any positive ambient case remains unresolved.
The count for16 references would require all relevant four-coset bindings and cannot be replaced by one selected product's failure.
The ranks and retained positive target words are reused from C828; no nullspace word, four-coset reference or new ambient test is numerically evaluated in this section.

At source depth32 the old nonunit S_32 vanishing argument FAILS.
For example in F_2[z]/Phi_15bar^32, at w=z^15 one has

    S_32(w)=(w-1)^31,

of exact Phi_15bar-order31, since z^15-1 is square-free in characteristic2.
It is therefore nonzero at this depth.
No unchanged n480 transition,4193 alphabet or higher-source exponent is inferred from C826's depth28 proof.
The positive common-word argument NH4 requires only the already proved Theta exponent and is unaffected by this limitation.
The useful next object is the bounded ambient map NH7 on four actual Theta representatives, conditional on the complete rank/coset certificate, with no new image or native authorization supplied by this preparation.

### NH6. Direct higher-source exponent and the exact next-kernel criterion

Define the next source tuple, without assuming any generator-period formula,

    Xi_2(Q)=(Qbar mod f^16,
             Qbar(Y) mod(Y+1)^32,
             Qbar(Y) mod p(Y)^16),
    Theta_2(Q)=(Xi_2(Q),Omega(Q)).

All coordinates are units for the actual family.
Their binary unit exponents divide240,32,48, respectively: remove the residue-field factor of order15,1,3 and use the characteristic-two powers16,32,16 on the respective principal units.
Thus the binary exponent divides480, and C820's Omega exponent960 gives

    Theta_2(Q)^960=1 for EVERY actual Q.             (NH9)

This is a direct new bound at the required depths; it is not inferred from the old Theta exponent.
In particular K_2=Q^960 has r_(K_2)=s_(K_2)=0 at the NEW source depths of NH3.
Equation NH8 therefore simplifies to the actual single-kernel response L2_Q(r_(K_1),s_(K_1)).
Two actual cofactors in the same Theta_2 fiber have identical g2 classes whenever the reference hypotheses of NH4 hold.
The proof uses their two positive common words as in NH4; both higher-source increments now vanish.

Let Sigma_2 be the set of all pairs(r_K,s_K) from ACTUAL K in M with Theta(K)=1.
The image of Theta_2 is a finite group by NH9, and its projection to the old Theta image is onto.
Its kernel is intrinsically identified with Sigma_2: the first coordinate and Omega are1, and the two remaining coordinates are precisely1+(Y+1)^28s_K and1+p(Y)^14r_K.
Products add those increments and determine the complete kernel image.
Thus Sigma_2 is an ACTUAL F_2 subspace of the ambient eight-dimensional source, not an arbitrary CRT product.
Every element has a positive cofactor representative by the finite exponent.

For a reference Q with original F8/X2 and half class divisible by f^8, the following are equivalent:

- g2_Q belongs to L2_Q(Sigma_2).
- Some actual Theta-kernel multiplier K makes QK satisfy original F8 and have both genuine second halves zero modulo f^12 in their binary J classes.
- Some actual Q' in the entire Theta(Q) fiber has those same properties.

NH7 proves the first two equivalences locally with original-global transfer.
For the last, K_1=Q^959Q', K_2=Q^960 have the paid common word from NH4, Omega(K_2)=1 and, by NH9, zero NEW source increments.
Therefore both full F8 and the next normalized g2 class transfer unchanged on the Q' path.
This proves necessity for the entire fiber as well as sufficiency by a positive extension.
A target outside the AMBIENT image still excludes both X4 gates throughout the fiber; a target inside it need not lie in L2_Q(Sigma_2).
Even membership in this actual image only cancels the half through f^12, not the complete X4 quotient.

### NH7. Corrected half-period, a safe actual alphabet and one paid direction

The failed depth32 S_32 argument in NH5 has an exact replacement.
For the source3 coordinate work in the faithful quadratic extension of S_(3,32), with eta^2-Y eta+1=0 and epsilon=Y+1.
It is equivalently the Laurent quotient by Phi_3bar(eta)^32, since Phi_3bar=eta epsilon.
The exact binary identities are

    eta^3=1+epsilon+epsilon^2 eta,
    eta^96=1,
    eta^48=1+epsilon^16 modulo epsilon^32.

For w=eta^q, q odd, use B_n(w+w^(-1))=w^(-(n-1)/2)S_n(w).
If3 does not divide q, w-1 is a unit and S_480(w)=0 because w^480=1.
If q=3d with d odd, w^32=1 and

    S_480(w)=S_32(w)=(w-1)^31.

Here w-1=(eta^3-1)S_d(eta^3)=epsilon times a unit congruent to1 modulo epsilon, so the last expression is exactly epsilon^31 modulo epsilon^32.
The centered n->n+480 multiplier is w^(-240)=eta^(48q)=1+epsilon^16.
The extra geometric-sum term is epsilon^31 in the second case: its remaining centering factor has residue1 since w has residue1.
Also B_n(C_q(Y)) has residue B_n(0)=1 in that case.
Hence the FULL source3 transition is multiplicative:

    B_(n+480)(C_q(Y))
       =[1+epsilon^16+1_(3|q)epsilon^31] B_n(C_q(Y))
                                          mod epsilon^32. (NH10)

The first f16 coordinate has transition1 by C826's faithful Laurent calculation projected at depth16.
For the source5 coordinate use zeta^2-Y zeta+1=0 over S_(5,16).
The identity Phi_5bar=zeta^2 p(Y) gives zeta^80=1.
At w=zeta^q one has S_480(w)=6S_80(w)=0 and w^(-240)=1, without cancelling w-1 even when5 divides q.
Thus its entire source16 transition is1.
The full q-period480 holds in both source extensions, because96 and80 divide480, and in the first coordinate by the adopted f16 Laurent calculation.
C820 separately supplies Omega's n480 and q480 periods with their genuine mixed-characteristic signs and nonunit cases.

Put c_0=(1,1+epsilon^16,1;1) and d_0=(1,1+epsilon^31,1;1), in the order(first,source3,source5;Omega).
Then

    Theta_2(B_(n+480)(C_q))=c_0 d_0^(1_(3|q)) Theta_2(B_n(C_q)),
    c_0^2=d_0^2=1.                                (NH11)

In particular n960 and q480 are sufficient full periods.
At n=1, B_1=1 is used only as an identity polynomial:

    Theta_2(B_481)=c_0,
    Theta_2(B_481(C_3))=c_0d_0.

Both factors are actual members of M, with trace degrees240 and720.
Consequently the old4192 endpoint/lower-row labels of C867, together with these TWO shift labels, generate the full Theta_2 image.
For an upper-half n residue use the shift determined by whether3 divides q; residue1 gives the identity and residue481 gives the appropriate shift alone.
The same33 ACTUAL smooth q representatives of C826 remain sufficient, because divisibility by3 is unchanged modulo480.
This proves a sufficient4194-label alphabet, not distinctness of images or insufficiency of the old4193 labels.
The total label degree is

    D_2=1+539881*15296+240+720.

Every attained Theta_2 image has a positive representative with all4194 exponents0..959, cofactor degree at most959D_2 and original degree at most374+959D_2.
The full reciprocal degree is twice that original degree, with actual q values and complete factors retained.
No higher image is evaluated or proposed as an automatic next computation.

There is already one useful exact actual direction:

    D_shift=B_481 B_481(C_3), deg D_shift=960,
    Theta(D_shift)=1, Theta_2(D_shift)=d_0,
    (r_(D_shift),s_(D_shift))=(0,epsilon^3).

It preserves full original F8 and the lower-half class while NH7 gives

    g2_(epsilon,Q D_shift)-g2_(epsilon,Q)
       =f^3 deltabar gamma_Q^3 (X+1)^31 mod f^4.   (NH12)

This is nonzero because delta, gamma_Q and X+1 are f-units.
Its cost is960 additional trace degree and1920 reciprocal degree.
This identity is one paid source direction, not a computed repair of a particular target or a full X4 witness.

### NH8. Exact bounded screen preparation and its mathematical use

The finite reference system is [adopted C825](Yin_C_G0825_v1.md#retained-old-fiber-reference-system).
Its16 excluded old Xi fibers and the16 remaining required Xi16 lifts are unchanged.
The complete rank59/rank57 and all16 attained targets are supplied by [adopted C828](Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28).
Only the finite four-coset application uses those numerical premises; NH1--NH4 and NH6--NH7 do not.
No new native execution is made or authorized by this preparation.

Use all16 exact R_i reference words, their retained actual K_(i,0), and two actual positive nullspace words N_1,N_2 for the common ker(Phi_R|W_plus).
A concrete selection is to scan the59 retained kernel-basis vectors in their certificate order, reduce their57-rank images by highest-bit pivots while tracking59-bit coefficient vectors, and take the two zero reductions.
Each such coefficient vector has coefficient1 at its new current basis index and uses only earlier indices otherwise, so the two are independent.
They span the kernel because there are exactly57 independent images; the independent59 source vectors identify their coefficient relations with the actual kernel of Phi_R.
Multiplying the corresponding retained positive basis words supplies actual N_1,N_2; any final exponent reduction uses960 and retains the complete costs.
No coefficient-vector or resulting word is evaluated here.
The maps agree in C828, but each reference and its actual target/word binding remains explicit; write N_(i,j)=N_j if the common pair is used.
Construct the four literal positive products R_i K_(i,0) N_(i,1)^e1 N_(i,2)^e2 for every i.
Retain their actual exponents, complete factors and full degree costs; any deliberate exponent reduction must use NH9 and retain the resulting word and costs.
All64 labels, including any coincident words or images across different i, remain in the coverage account.
The four Theta values for each i must be checked distinct through their four distinct target-preimage vectors; partial generator counts do not prove coverage.

Adopted C825 gives deltabar=1+X^8 and beta_(R_i)^2=gamma_(R_i)^3=X^6+X^10 modulo f^4 for every remaining reference.
All four products stay in Xi16(R_i), so C824 coefficient constancy makes L2 the SAME map for all64 labels.
This reuses exact coefficient classes, not a new computed column, rank or target; the actual new g2 values remain reference-specific.
For each chosen ACTUAL reference Q, the necessary next test is the exact g2_Q from BOTH genuine original integer second halves, and all eight columns/all256 values of L2_Q at the source bases1,Y,Y^2,Y^3 in each source.
The beta_Q, gamma_Q and genuine delta classes must come from the same original J system, with the global factor/weight interface retained.
No initial unit modulo f substitutes for the complete R_4 target, and no prior mask's coefficient values are assumed for another reference.
A negative case needs a separating functional or complete normal remainder; a positive ambient case is recorded as unresolved actual-kernel attainment.
Independent exact implementations and the relevant original-array checks would supply finite evidence only within a separately authorized native phase.

If EVERY one of the64 ambient tests is negative, NH4--NH6 and the four-coset coverage exclude original F8/either-X4 in all16 remaining old fibers.
Combined with C825's already excluded16 fibers and its exhaustive old-source reduction, this would exclude joint F8/either-X4 for the ENTIRE exact endpoint/rectangle family M at this one T_0 profile.
If at least one case is an ambient member, only the negative Theta fibers are excluded; no actual correction, full X4 success or unrestricted-family result follows for a survivor.
Even actual membership in Sigma_2 would initially give only half vanishing through f^12.

Every Q used here is a complete cyclotomic product, so its full reciprocal input has m=0 and retains the fixed reducible T_0 factors.
Neither possible screen outcome supplies a monic irreducible reciprocal nontorsion integer-unit input or a controlled-total-positive-measure lift.
[C720](Yin_C_G0720_v1.md#paid-characteristic-zero-certificate) applies its exactness threshold to the SAME irreducible input, with full reciprocal degree and original coefficient precision; the present family does not satisfy that input hypothesis.
A local f-order increase is not an extra global coefficient-divisibility bit.
Consequently the screen is a bounded classification discriminator for this family, not a step that by itself beats C720's degree/precision bound or resolves G0001.
Any subsequent precision iteration would need a separate concrete comparison of actual degree, global precision, irreducibility and total Mahler measure; this preparation provides no reason to continue indefinitely by degree growth alone.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision next-half-and-four-coset-screen-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:19 |
| status | open |
| reason | Fix the complete next genuine-half response, full source32/16 unit bounds and corrected half-period, sufficient4194 actual alphabet and costs, one paid degree960 kernel direction, exact whole-Theta-fiber next-half criterion, and four-coset/all64 ambient screen implication using the adopted rank59/57 and reference evidence. Root and primitive_second_eight are substantive contributors. No new native value, word list, rank, target verdict or full X4 witness is computed. The entire family remains fully cyclotomic with m=0; no irreducible controlled-total-measure conclusion is asserted. Fresh whole review and responsible adoption remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Next transport, periods and exact four-coset discriminator](#statement) | ST1--ST9: full actual family and costs, true next halves/source bits, direct exponent960, corrected n480 transition and4194 labels, actual degree960 direction, whole-Theta-fiber criterion and exhaustive64-label conditional screen, with all positive-result and irreducibility limits. |
| argument | [Complete NH1--NH8 proof](#complete-argument) | Every weighted integer carry before halving, original global transfer, source maps, direct higher-source exponent, full nonunit period cases, paid common words, intrinsic next kernel, exact four-coset coverage and finite-screen consequence. |
| dependency | [Adopted original next-response starting interface](Yin_C_G0824_v1.md#decision-whole-reviewed-2026-10-27) | Actual family and original canonical divisions/coverage, true P4 coefficient lifts and mixed carry, binary orders, both second signs and Xi16 coefficient constancy. Its selected-mask819 numerical separator is not reused as another target. |
| dependency | [Adopted full-eighth character](Yin_C_G0820_v1.md#decision-whole-reviewed-2026-10-26) | Genuine delta and its unit property, B_F, exact original-global F8 character, Omega exponent960 and n480/q480 periods with all mixed-characteristic/nonunit cases. No higher binary-source period is borrowed. |
| dependency | [Adopted source28/14 kernel and actual alphabet](Yin_C_G0826_v1.md#decision-whole-reviewed-2026-10-27) | Exact actual Theta, complete4193 labels and degree sums, intrinsic120-bit kernel, positive representatives and arbitrary-reference/whole-Xi16 lowest-joint criterion. New source32/16 bounds and corrected transition are proved here. |
| dependency | [Adopted complete joint image and sixteen positive targets](Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28) | Complete59-dimensional W_plus, common projected rank57, all16 actual reference/target words and positive kernel basis words with costs; used only for four-coset coverage. Its one mask203 later residual failure is not used to exclude a fiber. |
| dependency | [Adopted complete old-fiber screen](Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27) | Exhaustive32 old-source reduction,16 excluded fibers and exact remaining reference system/necessary Xi16 lifts, genuine lower-gate hypotheses and common beta/gamma/delta coefficient classes. No new ambient target verdict inferred. |
| dependency | [Adopted every-depth substitutions](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | Injective S3,j/S5,j maps and exact chi+1=(X+1)f and p(lambda)=p(X)f, including depths32 and16. Local native classification is not a new proof input. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:30 |
| status | proved |
| reason | Adopt the unchanged complete symbolic theorem after whole independent R1049 and responsible inspection of the complete fixed statement, argument and actual adopted input interfaces. All original carry and genuine-half steps, direct higher-source exponent, corrected nonunit period, positive costs, intrinsic actual kernel and conditional complete64 screen are covered. No new native target outcome or unconditional family exclusion is asserted; ambient membership, full X4, irreducibility and total-positive-measure limitations remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Next transport, periods and exact four-coset discriminator](#statement) | ST1--ST9: full actual family and costs, true next halves/source bits, direct exponent960, corrected n480 transition and4194 labels, actual degree960 direction, whole-Theta-fiber criterion and exhaustive64-label conditional screen, with all positive-result and irreducibility limits. |
| argument | [Complete NH1--NH8 proof](#complete-argument) | Every weighted integer carry before halving, original global transfer, source maps, direct higher-source exponent, full nonunit period cases, paid common words, intrinsic next kernel, exact four-coset coverage and finite-screen consequence. |
| dependency | [Adopted original next-response starting interface](Yin_C_G0824_v1.md#decision-whole-reviewed-2026-10-27) | Actual family and original canonical divisions/coverage, true P4 coefficient lifts and mixed carry, binary orders, both second signs and Xi16 coefficient constancy. Its selected-mask819 numerical separator is not reused as another target. |
| dependency | [Adopted full-eighth character](Yin_C_G0820_v1.md#decision-whole-reviewed-2026-10-26) | Genuine delta and its unit property, B_F, exact original-global F8 character, Omega exponent960 and n480/q480 periods with all mixed-characteristic/nonunit cases. No higher binary-source period is borrowed. |
| dependency | [Adopted source28/14 kernel and actual alphabet](Yin_C_G0826_v1.md#decision-whole-reviewed-2026-10-27) | Exact actual Theta, complete4193 labels and degree sums, intrinsic120-bit kernel, positive representatives and arbitrary-reference/whole-Xi16 lowest-joint criterion. New source32/16 bounds and corrected transition are proved here. |
| dependency | [Adopted complete joint image and sixteen positive targets](Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28) | Complete59-dimensional W_plus, common projected rank57, all16 actual reference/target words and positive kernel basis words with costs; used only for four-coset coverage. Its one mask203 later residual failure is not used to exclude a fiber. |
| dependency | [Adopted complete old-fiber screen](Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27) | Exhaustive32 old-source reduction,16 excluded fibers and exact remaining reference system/necessary Xi16 lifts, genuine lower-gate hypotheses and common beta/gamma/delta coefficient classes. No new ambient target verdict inferred. |
| dependency | [Adopted every-depth substitutions](Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) | Injective S3,j/S5,j maps and exact chi+1=(X+1)f and p(lambda)=p(X)f, including depths32 and16. Local native classification is not a new proof input. |
| review | [Whole independent R1049](../audits/reviews/Yin_R_G1049_v1.md#whole-finding) | Entire ST1--ST9 and NH1--NH8, all six adopted input interfaces, conditional screen and every mathematical limitation; no new native computation. |
