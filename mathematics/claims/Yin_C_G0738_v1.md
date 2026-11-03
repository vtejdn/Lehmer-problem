---
author: Yin
---

# Complete parity-zero source extensions and a height-one obstruction in their larger subfamily

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the even-coefficient projection, complete Chebyshev pairing, multiplier choice, local Laurent orders, stronger separated-support obstruction and generic finite-precision application.
The characteristic_zero_bridge agent checked all original-source, root, integer carry, endpoint, factor, degree, layer and Haar interfaces and authored the integrated PA1--PA12, HB1--HB10 and NF1--NF3 argument.
Root read the entire saved PA/HB proof and then the entire NF addition.
Both agents are contributors; this open fixed candidate awaits fresh isolated whole review and a separate acceptance decision.
No native coefficient expansion, sign search or rank calculation is used.

<a id="complete-source-parity-zero-multiplier"></a>
## Statement

Use C_0=2,C_1=X,C_(j+1)=XC_j-C_(j-1), with bars for coefficient reduction modulo2.
For odd n>1, B_n is the complete polynomial over F_2 of traces of all nonidentity n-th roots, one per inverse pair, and W_n is its complete primitive-order version.
For each monic integer trace T define the SAME actual canonical polynomials

    a(T)=rem_T(T(C_2))/2,
    b(T)=rem_T(T(C_3))/3,
    c(T)=rem_T(T(C_5))/5,
    F(T)=rem_T(2c(T)^2-3a(T)^5),
    G(T)=rem_T(c(T)^3-2b(T)^5),
    X_s(T)=rem_T(b(T)^2-a(T)^3+s G(T)), s in{1,-1}.

All scalar divisions take place in Z[X] before binary reduction, and all remainders are taken at the indicated OWN monic divisor.
For an integer polynomial P, height1 means that every coefficient is in{0,1,-1} and its maximum absolute coefficient is1.
For a binary polynomial f, put Lambda(f)=sum_(h>=0)[X^(2^h)]f, including every such exponent through its full degree.

### A. Two complete-source extensions, with separately paid degrees

Start with any actual BOUNDED representative Y from the retained [C691 DG1--DG8 construction](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), carrying its selected fresh odd order n_star and exact triple irreducible psi_star outside B.
Retain ell>=82, Q=2^ell, m=Q/4-2, the complete source H, B=X^(Q-m)H(chi), phi=X^2+X+1 and chi=Xphi^2.
Set H_0=X^(2m)Y, U_0=H_0phi^(14m), R_0=H_0phi^(12m)B and d=30m+deg Y.
Here n_star is the retained auxiliary fresh order, distinct from the fourteen-prime order n_- inside H, and n_star<4Q^2+80Q+1.
Every original complete factor, multiplicity and actual source condition remains part of the input.

Make either of the following EXPLICIT choices, without identifying their ranges:

    a_mul=30Q n_star ceil(d/(60Q n_star))>=d/2,
    n_starred=2a_mul+1,
    Y_star=Y B_(n_starred)^2,
    U_star=U_0 B_(n_starred)^2,
    R_star=R_0 B_(n_starred)^2,
    d_star=d+2a_mul;

    a_big=30Q n_star ceil(d/(30Q n_star))>=d,
    n_big=2a_big+1,
    Y_big=Y B_(n_big)^2,
    U_big=U_0 B_(n_big)^2,
    R_big=R_0 B_(n_big)^2,
    d_big=d+2a_big.

The proof uses n for n_starred in PA and explicitly resets n=n_big inside HB.
Both new representatives are monic complete polynomials prime to Xphi, retain both full C_3/C_5 forward divisibilities, every multiplicity at least2, the same DG3 low/high jets and character, and the original selected exact triple factor outside B.
They retain the full nonzero canonical remainder, sole unsaturated phi orders14m/12m, all doubled16m root/gate identities and derivative X^(8m) divisibility specified in PA10--PA11.
Both satisfy Lambda(U_new)=0, hence their complete reciprocal binary support size is divisible by4.
This removes the necessary support-parity obstruction WITHIN the complete forward/canonical source domain.

Their complete costs are

| Choice | deg Y_new | d_new=deg U_new |
| --- | --- | --- |
| a_mul>=d/2 | <29040Q^3+7212Q^2+308Q | <29040Q^3+7212Q^2+316Q |
| a_big>=d | <43440Q^3+8418Q^2+436Q | <43440Q^3+8418Q^2+444Q |

In both cases deg R_new increases by the same2a as deg U_new, so the strict gap remains m-8-5deg H>5m/256.
For every q=2^k the actual maximal Frobenius power of U_new^q, R_new^q and the original reciprocal binary polynomial is q.
The original reciprocal polynomial degree is2q d_new, not a finite-jet dimension.
The old DG8 numerical bounds are NOT claimed for the enlarged representatives.
The same actual integer layer vector a_0=12mq, a_b=0 for b>=1 remains, with the complete enlarged synthetic integer G_int,new of degree q deg R_new, reduction R_new^q and zero normalized circle Haar logarithmic integral.
That synthetic polynomial is not identified with the canonical integer G(T), and no original irreducible input, field norm or total-Mahler bound is supplied by this assertion.

### B. Height-one obstruction ONLY for the larger choice

For the a_big>=d choice, let q=2^k and let P_q be ANY monic reciprocal integer polynomial of constant1 and height1 with full binary reduction

    [z^(d_big)U_big(z+z^(-1))]^q.

Use its OWN monic integer trace and canonical system.
If its X_s residual is coefficientwise even for either sign, then for some integer L of degree2d-2 with L(0)=1 and L^*=-L,

    P_q(z)=L(z^q)(1-z^(2n_big q)),
    L^*(z)=z^(2d-2)L(z^(-1)).

Both displayed factors are nonconstant, so P_q is reducible and contains the cyclotomic factor z-1.
Consequently this larger completed subfamily has no irreducible height1 input passing even the own second residual's first bit.
This statement is NOT extended to the original C691 source, the weaker a_mul>=d/2 choice or differently selected complete multipliers.
It does not claim inconsistency of all three algebraic sign systems: any passing sign solutions in the larger subfamily yield reducible inputs.

### C. Actual generic finite precision on EITHER enlarged source

For either source, and each separately fixed sign s, invoke the adopted GENERIC C730/C733 construction anew at the chosen original dyadic q with a_src=2m and h_b=2m+deg Y_new.
The source hypotheses and h_b>145a_src are verified in NF1; no old output is multiplied, pulled back or relabeled.
There exist actual monic traces of SAME degree D_new=q d_new with:

| Original q | Actual output precision | Derivative divisor | Genuine next-error powers |
| --- | --- | --- | --- |
| q>=2^41 | F=X_s=0 modulo1024 | q/2^31 | (F/1024)bar,(X_s/1024)bar in F_2[X^(q/2^41)] |
| q>=2^43 | F=0 modulo2048, X_s=0 modulo1024 | q/2^32 | (F/2048)bar in F_2[X^(q/2^43)], (X_s/1024)bar in F_2[X^(q/2^42)] |

The full H_0=(X^(2m)Y_new)^q primary residuals retain precision2^17.
The traces have Tbar=U_new^q and actual G(T)bar=R_new^q!=0, with degree gap q(m-8-5deg H)>5qm/256 and the NEW full degree bounds in Part A multiplied by q.
The original reciprocal degree is2D_new.
The outputs for different signs need not be the same integer trace.
No height1 or irreducibility conclusion follows from these finite constructions; if a larger-source output happened to have height1, Part B would force it to be reducible.
No simultaneous2048, arbitrary precision, characteristic-zero system, synthetic/canonical identification or unrestricted G0001 conclusion is asserted.

## Complete argument

### Actual input, multiplier and enlarged costs

Start with ANY actual representative Y from the retained C691 construction, carrying its selected fresh odd order n_star and its exact triple irreducible psi_star outside B.
Retain ell>=82, Q=2^ell, m=Q/4-2, the complete H, B=X^(Q-m)H(chi), phi=X^2+X+1, chi=Xphi^2 and C_3bar=X^3+X.
Use the full polynomials

    H_0=X^(2m)Y, U_0=H_0 phi^(14m),
    R_0=H_0 phi^(12m)B, V_0=H_0 B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m),
    d=deg U_0=30m+deg Y.

The order n_star is the C691 Section5 fresh order, NOT the fourteen-prime n_- used inside H.
Its actual bounds are

    L_0=4Q, D_B=deg B<Q,
    K_0=max(30L_0,4D_B^2),
    K_0<n_star<=K_0+20L_0+1<4Q^2+80Q+1,
    gcd(n_star,15)=1.                            (PA1)

The selected psi_star is an irreducible factor of the COMPLETE primitive trace polynomial W_(n_star), has exact multiplicity3 in both Y and YB, and is prime to Xphi B.
No linear-in-Q bound on n_star is substituted for PA1.

Define the ordinary positive integers and actual complete polynomial

    t=ceil(d/(60Q n_star)),
    a_mul=30Q n_star t, n=2a_mul+1,
    J=B_n=1+sum_(j=1)^(a_mul) C_jbar,
    M=J^2,
    Y_star=Y M, U_star=U_0 M, R_star=R_0 M.       (PA2)

Here a_mul is a multiplier degree, not the canonical polynomial a(T); J is a complete nonidentity odd-order trace polynomial and M is its square.
Then

    a_mul>=d/2,
    gcd(n,15 n_star)=1,
    v_2(a_mul)>=ell+1,
    d<=2a_mul<d+60Q n_star.                      (PA3)

The new representative is monic, complete, prime to Xphi, and has every occurring irreducible multiplicity at least2.
It satisfies BOTH original forward divisibilities and the SAME full DG3 finite class.
The original selected psi_star still has exact multiplicity3 in Y_star and Y_star B.
In particular Y_star and Y_star B, and hence U_star and R_star, remain nonsquare.
Moreover the COMPLETE dyadic coefficient functional satisfies

    Lambda(U_star):=sum_(h>=0)[X^(2^h)]U_star=0.  (PA4)

This is an actual complete representative passing the necessary support-parity test, rather than a polynomial satisfying only the two jets.

The exact degrees and conservative fully paid bounds are

    deg Y_star=deg Y+2a_mul
               <deg Y+d+60Q n_star
               <29040Q^3+7212Q^2+308Q,
    d_star=deg U_star=d+2a_mul
               <2d+60Q n_star
               <29040Q^3+7212Q^2+316Q,
    deg R_star=deg R_0+2a_mul,
    d_star-deg R_star=d-deg R_0
                      =m-8-5deg H>5m/256.       (PA5)

The original DG8 numerical upper bound is NOT claimed for Y_star.
The full reciprocal binary degree is2d_star, and after raising by q=2^k it is2q d_star.
All added factors and their degrees are included.

### The exact parity identity on the full polynomial

The C731 proof gives Lambda(C_i bar)=1 for every i>=1, while C_0bar=0 and Lambda(1)=0.
The trace product identity in characteristic2 is

    C_i bar C_j bar=C_(i+j)bar+C_(|i-j|)bar.

For i,j>=1 it follows that

    Lambda(C_i bar C_j bar)=1 if i=j,
                            0 if i!=j.          (PA6)

When i=j the second term is C_0bar=0; when i!=j both indices on the right are positive and their two contributions cancel.
Thus no constant-term convention is hidden in this diagonal pairing.

For the actual U_0, put

    V_even(X)=sum_(i>=0)[X^(2i)]U_0 X^i,
    V_odd(X)=sum_(i>=0)[X^(2i+1)]U_0 X^i,
    U_0=V_even^2+X V_odd^2.

Since U_0 is divisible by X^(2m) and2m>=2, both V_even(0) and V_odd(0) are0.
The degree of V_even is at most floor(d/2)<=a_mul.
Expand it in the monic binary trace basis as V_even=sum_(i=1)^(a_mul) v_i C_i bar, allowing zero coefficients.
No constant basis term occurs because V_even(0)=0 and every positive-index C_i bar has constant0.
Then

    Lambda(V_even J)
       =Lambda(V_even)
          +sum_(j=1)^(a_mul)Lambda(V_even C_j bar)
       =sum_i v_i+sum_j v_j=0.                  (PA7)

For any polynomial A over F_2, Lambda(A^2)=Lambda(A), while Lambda(X A^2)=A(0): only the dyadic exponent1 can occur in that odd-degree polynomial.
Therefore

    Lambda(U_0 J^2)
       =Lambda((V_even J)^2)+Lambda(X(V_odd J)^2)
       =Lambda(V_even J)+V_odd(0)J(0)=0.

This proves PA4 on the complete source, including every high dyadic coefficient beyond the DG3 range.

### Exact local orders of the complete multiplier

The definition in PA2 makes a_mul divisible by30Q n_star, so n=2a_mul+1 is odd and1 modulo every prime divisor of15 n_star.
This proves the coprimality in PA3; since n_star is odd, v_2(a_mul)=ell+1+v_2(t)>=ell+1.
The ceiling gives a_mul>=d/2 and its strict upper bound2a_mul<d+60Q n_star.

For x=z+z^(-1), the COMPLETE Laurent identity is

    B_n(x)+1
      =z^(-a_mul)(z^(a_mul)+1)(z^(a_mul+1)+1)
                                                /(z+1). (PA8)

It follows by adding the middle term z^(a_mul) to the complete geometric sum1+z+...+z^(2a_mul) and multiplying by z+1.
It is an identity of Laurent polynomials after the exact indicated division, not a division by a zero value at a selected root.
Write v=v_2(a_mul), so a_mul is even and a_mul+1 is odd.
At z=1, the two numerator factors have exact orders2^v and1, and the denominator has order1.
Thus the Laurent order is2^v.
Since x=(z+1)^2/z has exact order2 there,

    ord_X(B_n-1)=2^(v-1)>=Q.

At EVERY primitive fifth root zeta,5 divides a_mul and5 does not divide a_mul+1.
The factor z^(a_mul)+1 has exact local order2^v, because its odd-exponent part has a simple zero at zeta; the other numerator factor and denominator are units.
The trace map is unramified there:1+zeta^(-2)!=0, and the corresponding phi trace root is simple.
Hence

    ord_phi(B_n-1)=2^v>=2Q,
    M=1 modulo X^(2Q)phi^(4Q).                 (PA9)

The minus and plus signs agree in characteristic2, and the squared congruence follows from M-1=(B_n-1)^2.
The two factors of the displayed modulus are coprime.
Since8m=2Q-16<2Q and16m=4Q-32<4Q, multiplication by M preserves BOTH exact DG3 jets, and therefore the same finite character value0.

### Completeness, both forward divisibilities and the fresh triple factor

The complete polynomial B_n is the squarefree product of W_e over all e|n,e>1, with every inverse-paired nonidentity n-th root retained.
Because gcd(n,15)=1, its factors are prime to Xphi and all their original odd orders are prime to3 and5.
Powering an n-th root by3 or5 permutes the complete nonidentity set, so

    B_n divides B_n(C_3bar),
    B_n divides B_n(chi).

These are global polynomial divisibilities: B_n is squarefree and every root remains a target root.
Squaring and multiplying by the original Y forward quotients proves

    Y_star divides Y_star(C_3bar),
    Y_star divides Y_star(chi).

All new complete groups have multiplicity2, and every old multiplicity increases by an even nonnegative integer, so the floor2 is preserved.
If the retained ordinary/divided-row pattern is used, the multiplier only increases ordinary-order multiplicities and preserves each inequality v_e<=u_e.
Since gcd(n,n_star)=1, none of the added trace groups has original primitive order n_star.
An irreducible trace factor cannot have two different original odd orders, by the quadratic inverse-pair equation.
Consequently psi_star does not divide B_n and its exact multiplicity3 in both Y_star and Y_star B is unchanged.
Multiplication by the square M also leaves the entire odd-multiplicity parts of Y and YB unchanged.

### Full canonical remainder and the doubled local root identities

Define the NEW actual source quantities, without altering H,B,m or Q,

    H_star=X^(2m)Y_star=H_0 M,
    V_star=H_star B=V_0 M,
    C_star=X^(2m)Y_star(chi)phi(chi)^(14m)
           =C_00 M(chi),
    D_star=V_star+C_star^3.

PA9 gives M=1 modulo phi^(4Q).
Its low part also gives M(chi)=1 modulo phi^(4Q), because chi has exact phi-order2 and M-1 is divisible by X^(2Q).
Thus H_star,V_star,C_star agree with their old counterparts modulo phi^(16m).
All source DG6 identities persist at their FULL stated precision, with the same cube-one unit beta and the same Z_0=beta^2 B^(-1):

    H_star=B^(-7), C_star=beta^2 B^(-2),
    D_star=0, H_star^6=C_star^21,
    Z_0^11=H_star C_star^2, Z_0 D_star=0
                                           modulo phi^(16m). (PA10)

The unit root remains unique at this precision by the same C691 unit-group argument; neither the precision nor the root is replaced by a lower projection.
Also Y_star'=Y' M, so X^(8m) divides Y_star'.

The global C667 all-primary mechanism now applies with every hypothesis checked, and can be seen directly.
One has

    U_star(chi)^3+R_star=phi^(12m)D_star.

It vanishes modulo phi^(14m) by PA10.
It also vanishes modulo H_star: the new forward divisibility gives H_star|C_star, and R_star=H_star phi^(12m)B.
Since H_star is coprime to phi, U_star divides the entire difference.
The strict degree gap in PA5 then gives the ACTUAL monic remainder

    R_star=rem_(U_star)(U_star(chi)^3)!=0,
    U_star divides U_star(C_3bar).               (PA11)

For the second statement multiply the original U_0 forward quotient by the proven M forward quotient.
The sole unsaturated primary factor is still phi, with orders14m and12m; every other full primary factor of U_star is saturated in R_star.
Thus for ANY monic integer trace T reducing to U_star, its actual odd divided remainders have bbar=0 and canonical Gbar=R_star!=0.
No choice of T's dyadic quotient or of its higher coefficients is supplied by this conclusion.

### Exact Frobenius normalization, original layers, Haar and final costs

For every q=2^k, the actual maximal Frobenius power of U_star^q and R_star^q is q, because the retained psi_star exponent is exactly3q.
The full canonical and C_3 identities raise to those actual q-th powers, and PA10 raises to the original precision16mq with Z=Z_0^q.
The full original degrees and gap are

    r_star=q(d+2a_mul),
    w_star=q(deg R_0+2a_mul),
    r_star-w_star=q(m-8-5deg H)>5qm/256,
    original reciprocal degree=2r_star.          (PA12)

The original binary reciprocal polynomial also retains maximal power q.
Indeed, with S_n(z)=1+z+...+z^(n-1), the exact trace identity gives

    z^(d_star) U_star(z+z^(-1))
       =[z^d U_0(z+z^(-1))] S_n(z)^2.

The base reciprocal is nonsquare by the adopted C731 source proof; multiplying by a square preserves that property in characteristic2.
This is a statement about the full binary polynomial, not an asserted factorization of a height1 integer lift.

The same actual integer layer vector a_0=12mq, a_b=0 for b>=1 still has its original total weight and strict-window correction0.
The complete new V_star is V_0 times B_n^2, so every additional primitive order e|n,e>1 is odd and different from5 and occurs twice more than before.
Use the accepted C667/C199 monic integer trace factors F_e and the OLD complete synthetic G_int from C691 DG7.
Then the NEW actual synthetic integer polynomial is

    G_int,star=G_int product_(e|n,e>1) F_e^(2q).

It has reduction R_star^q, full degree w_star, and zero normalized circle Haar integral of log(G_int,star(z+z^(-1))^2), counting every added cyclotomic factor and multiplicity and using the integrable logarithm convention at its zeros.
This follows directly from the retained complete trace-factor identity and adds exactly2q deg B_n=2q a_mul to the integer degree.
It is NOT identified with the actual canonical integer G(T); no original irreducible polynomial, field norm or total-Mahler bound is inferred from that synthetic Haar value.

For the numerical bounds in PA5, use the actual original bounds

    deg Y<=14400Q^3+1206Q^2+120Q,
    d<=14400Q^3+1206Q^2+128Q,
    60Q n_star<240Q^3+4800Q^2+60Q.

Adding these to the exact ceiling cost in PA3 gives respectively the coefficients29040,7212,308 and29040,7212,316 in PA5.
These are the new paid bounds, not the original DG8 budget.

The functional identity in the C731 support proof applies to the new COMPLETE binary reciprocal source independently of its numerical degree bound: its center is0, and its full coefficient support size w_support,star satisfies w_support,star/2=Lambda(U_star)=0 modulo2.
Thus w_support,star is divisible by4, and this necessary obstruction has actually been removed within the complete forward/canonical source domain.
The C731 argument may be used with the actual new degrees and source polynomials, but its original bounded-source numerical constants are not silently reused.
There is still no assertion that any of the three NEW restricted affine sign systems is solvable, that a passing height1 lift is irreducible, or that higher precision or characteristic-zero identities hold.
The parity of the ORIGINAL chosen Y is not evaluated by constructing Y_star.
This is a complete parity-zero source construction with explicit extra cost, not a height1 realization, synthetic-to-canonical Haar identification or solution of G0001.

<a id="large-complete-multiplier-height-one-obstruction"></a>
### A larger complete multiplier forces every first-bit height1 lift to be reducible

Root proposed this stronger explicitly restricted subfamily and its separated-support integer carry argument after the parity-zero construction.
The characteristic_zero_bridge agent checked the exact two-block representation, central coefficient, trace/reciprocal Delta identity, every nonidentity odd root, degree comparison and all raised-source consequences.
This remains part of the same author candidate, not an independent review or an assertion about every complete C691 representative.

Use the SAME original source and fresh order n_star as PA1, but now choose

    a_big=30Q n_star ceil(d/(30Q n_star)),
    n_big=2a_big+1,
    Y_big=Y B_(n_big)^2,
    U_big=U_0 B_(n_big)^2,
    R_big=R_0 B_(n_big)^2,
    d_big=d+2a_big.                              (HB1)

Then a_big>=d, gcd(n_big,15 n_star)=1 and v_2(a_big)>=ell+1.
All completeness, both forward divisibilities, exact fresh multiplicity3, original finite jets, maximal Frobenius, nonzero full canonical remainder, DG6 root identities, unchanged gap, actual integer layers and synthetic Haar conclusions proved above remain valid with this choice.
Their proofs use only the retained divisibility of a_big, the coprimality of n_big and a_big>=d/2, which this stronger choice satisfies.
The ORIGINAL numerical ceiling cost is replaced by

    2d<=2a_big<2d+60Q n_star,
    deg Y_big<deg Y+2d+60Q n_star
                <43440Q^3+8418Q^2+436Q,
    d_big<3d+60Q n_star
                <43440Q^3+8418Q^2+444Q.          (HB2)

The original reciprocal degree is2d_big, or2q d_big at a raised q, and the canonical degree gap remains exactly the original gap, multiplied by q after raising.
The complete support parity is again Lambda(U_big)=0.

Nevertheless, let P be ANY monic reciprocal integer polynomial of constant1 and height1 with binary reduction

    Pbar_big(z)=z^(d_big)U_big(z+z^(-1)).

Let T be its OWN monic integer trace polynomial of degree d_big, and use the actual canonical a,b,c,F,X_s,G for that divisor.
If X_s(T) is coefficientwise divisible by2 for EITHER sign s=1 or-1, then P is reducible and contains the explicit factor1-z^(2n_big), in particular the cyclotomic factor z-1.
In particular there is no irreducible height1 lift of this new binary source passing both first residual bits.
The conclusion only concerns HB1's larger complete-multiplier subfamily; it does not exclude such inputs for the original C691 Y or every other completion.

#### Exact separated support and the integer block representation

Put

    Pbar_old(z)=z^d U_0(z+z^(-1)),
    Dbar(z)=Pbar_old(z)/(z^2+1), r=2d-2.

This is an ACTUAL monic reciprocal polynomial in F_2[z] of degree r and constant1.
Indeed U_0 is divisible by X, and

    Dbar(z)=z^(d-1)(U_0/X)(z+z^(-1)).

The quotient U_0/X has lowest nonzero exponent2m-1>0.
In its positive Chebyshev-basis expansion there is consequently no constant basis term, so the central coefficient [z^(r/2)]Dbar is0.
This is a coefficient assertion on the full reciprocal polynomial, not a selected-root argument.

With n=n_big for this proof, the full binary geometric-sum identity gives

    Pbar_big=Pbar_old[(z^n+1)/(z+1)]^2
             =Dbar(1+z^(2n)).                    (HB3)

The complete low and high coefficient blocks in HB3 are disjoint because2n>r.
Every height1 P with this reduction therefore has the EXACT integer form

    P(z)=L(z)+z^(2n)L^*(z),
    L^*(z)=z^r L(z^(-1)),
    deg L=r, L(0)=1, Lbar=Dbar.                 (HB4)

Each supported coefficient of L is+1 or-1, and each unsupported coefficient is0.
The low leading coefficient is allowed to be either sign; the original P remains monic because the leading coefficient of the high block is L(0)=1.
Reciprocity of P, of full degree r+2n=2d_big, forces exactly the displayed reversed upper block.
Since Dbar is reciprocal, L^* and L have the same binary reduction and

    E=(L^*-L)/2 in Z[z], deg E<=r.               (HB5)

The zero central coefficient of Dbar forces the central coefficient of L itself to be zero by the height1 hypothesis.

#### Every added root imposes the same genuine canonical carry equation

All roots used in this paragraph lie in the algebraic closure of F_2, AFTER the relevant integer divisions.
Let zeta be any nonidentity n-th root, and put x=zeta+zeta^(-1).
Because gcd(n,15)=1, powering zeta by3 or5 permutes the COMPLETE nonidentity n-th roots.
Thus B_n(x)=B_n(C_3bar(x))=B_n(chi(x))=0.
The actual odd divided remainders for T consequently satisfy

    b(T)bar(x)=c(T)bar(x)=0.

This follows by reducing the integer monic division and the odd scalar division, then evaluating at the root x of Tbar=U_big.
If X_s(T) is even, its reduction at x gives a(T)bar(x)^3=0, so a(T)bar(x)=0.
The two choices of s have the same binary conclusion.

Define the integer carry polynomials

    Delta_T=[T(C_2)-T^2]/2 in Z[X],
    Delta_P=[P(z^2)-P(z)^2]/2 in Z[z].

Both are integral by coefficient Frobenius reduction.
The actual canonical a(T) is rem_T Delta_T, so its value at x agrees with Delta_Tbar(x).
From P(z)=z^(d_big)T(z+z^(-1)) one obtains the EXACT characteristic-zero Laurent identity

    Delta_P(z)=z^(2d_big)Delta_T(z+z^(-1)),       (HB6)

because z^2+z^(-2)=C_2(z+z^(-1)).
Division by2 precedes reduction throughout HB6.
Since zeta!=0, the preceding canonical conclusion implies Delta_Pbar(zeta)=0 for EVERY nonidentity n-th root.

For any integer polynomial A(z), write Delta(A)=[A(z^2)-A(z)^2]/2.
The exact two-block identity HB4 gives

    Delta_P=Delta(L)+z^(4n)Delta(L^*)
                          -z^(2n)L L^*.

Using L^*=L+2E, an independent integer expansion gives

    Delta(L^*)-Delta(L)=E(z^2)-2LE-2E^2.

After reduction and evaluation at zeta, zeta^(2n)=zeta^(4n)=1 and Lbar=L^*bar=Dbar, so

    Delta_Pbar(zeta)
       =Ebar(zeta)^2+Dbar(zeta)^2
       =[Ebar(zeta)+Dbar(zeta)]^2.               (HB7)

This retains the full canonical carry; the division by2 is not performed in a binary quotient and is not replaced by arbitrary trace coordinates.
Therefore Ebar+Dbar vanishes at all n-1 DISTINCT nonidentity n-th roots, since n is odd.
Its degree is at most r=2d-2, while

    r=2d-2<n-1=2a_big.

The polynomial must be zero identically:

    Ebar=Dbar in F_2[z].                         (HB8)

No assumption that Dbar is nonzero at a selected n-th root was used; all possible overlaps with the old source are included.

#### Height1 turns the carry into exact antisymmetry and a factorization

At each supported paired index j,r-j, both coefficients of L are in{1,-1}.
HB8 says that half their difference, (L_(r-j)-L_j)/2, is odd.
They must therefore have opposite integer signs.
At unsupported indices both coefficients are0, and the central coefficient was already proved0.
Thus the binary carry equality forces the EXACT integer identity

    L^*=-L,
    P(z)=L(z)(1-z^(2n_big)).                     (HB9)

Both factors are nonconstant, since r=2d-2>0 and n_big>1.
In particular P contains roots of unity and is reducible over Q.
This conclusion requires only evenness of the own second residual, not the first residual or a claimed solution of the full affine systems.

Finally let q=2^k and suppose a height1 monic reciprocal integer P_q has reduction Pbar_big^q.
The [exact support and canonical-composition argument of C724](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25), also retained in C731, gives P_q=Q_int(z^q) for a height1 base Q_int with reduction Pbar_big, and its own trace is T_base(C_q).
The base reciprocal is nonsquare by the retained fresh-factor argument, so q is its actual maximal binary and integer dyadic exponent.
Exact canonical covariance and injectivity of binary composition by X^q show that evenness of X_s for P_q implies evenness of the base X_s.
Applying HB9 gives

    P_q(z)=L(z^q)(1-z^(2n_big q)).                (HB10)

It too is reducible and has an explicit cyclotomic factor, with the full original degree2q d_big retained.
No total-reality assumption, normalized Mahler measure or unconstructed field norm is used.
This does NOT claim that the three algebraic sign systems for U_big are all inconsistent: any passing solutions, if they exist, yield reducible inputs of the displayed form.
The original complete C691 family and smaller or differently chosen complete multipliers retain their unresolved height1 feasibility questions.

<a id="complete-multiplier-generic-finite-residual-transfer"></a>
### Both enlarged sources retain the actual generic1024 and first2048 construction

Root proposed checking this corollary; characteristic_zero_bridge directly read the adopted [C730 AS512.1 generic source statement](Yin_C_G0730_v1.md#decision-whole-reviewed-2026-10-25) and [C733 G1024.1 and G10.3/G10.12 outputs](Yin_C_G0733_v1.md#decision-whole-reviewed-2026-10-25), and checked the following exact parameter mapping.
Both are contributors to this application; it is part of the same fixed author candidate and is not an independent review of those adopted inputs.

Let Y_new be EITHER the PA representative Y_star or the HB representative Y_big, and use the corresponding U_new,R_new,d_new.
In the GENERIC C730 domain take

    a_src=2m, H_b0=X^(a_src)Y_new,
    h_b=deg H_b0=a_src+deg Y_new,
    C_b0=X^(a_src)Y_new(chi)phi(chi)^(7a_src),
    A=a_src q, h=q h_b,
    D_new=h+14A=q d_new.                        (NF1)

The exponent a_src is even and at least2, Y_new is monic and prime to Xphi, both full forward divisibilities hold, and every FULL H_b0 multiplicity is at least2, including the X exponent.
The actual PA10 identities give H_b0^6=C_b0^21 modulo phi^(16m)=phi^(8a_src), exactly the required old8a source condition.
The degree margin is not assumed from an unchanged numerical witness: the original construction contains B_(n_star)^3 and n_star>120Q, so deg Y>=3(n_star-1)/2>=180Q.
Consequently h_old=a_src+deg Y satisfies h_old-361a_src>=1440>0, and both positive-degree squared multipliers increase h_b beyond h_old.
In particular h_b>145a_src, as required by C730 AS512.1.

Choose one fixed monic integer lift for each FULL irreducible factor, consistently across every occurrence, with the X lift equal to X, and form the new H_b and C_b precisely as in that generic statement.
Invoke the source preparation and finite construction ANEW for the chosen original dyadic q and this complete enlarged source.
Neither multiplication of an old integer output by a guessed lift of B_n^2 nor a trace pullback of an old output is used.
Fix one residual sign s in{1,-1} separately; the existence statements for different signs need not use the same integer polynomial.

The adopted C730 source theorem supplies all actual prepared coordinates, stronger integer factors, changed K and global512 input required by C733.
The latter therefore gives actual monic integer traces of the SAME degree D_new, with these exact outputs:

| Originally selected q | Actual output | Canonical residual precision | Integer derivative divisor | Genuine next-error global powers |
| --- | --- | --- | --- | --- |
| q>=2^41 | T_1024 | F(T_1024)=X_s(T_1024)=0 modulo1024 | q/2^31 | (F/1024)bar and (X_s/1024)bar lie in F_2[X^(q/2^41)] |
| q>=2^43 | T_first2048 | F(T_first2048)=0 modulo2048 and X_s(T_first2048)=0 modulo1024 | q/2^32 | (F/2048)bar lies in F_2[X^(q/2^43)] and (X_s/1024)bar lies in F_2[X^(q/2^42)] |

All displayed coefficient quotients are genuine integer divisions at the constructed actual divisor.
The complete H_0=H_b0^q primary components retain residual precision2^17 under the adopted theorem, with all original multiplicities.
At q=2^41 the first row has derivative divisor1024 and only first-power guarantees for its next errors.
At q=2^43 the second row has derivative divisor2048, a square guarantee for its next second error and only a first-power guarantee for its next first error.
No vanishing of that next second error modulo phi^A, simultaneous2048 or further induction is inferred.

Because every source and later correction is even and the full PA canonical identities hold, these actual outputs retain

    Tbar=U_new^q, G(T)bar=R_new^q!=0,
    deg T-deg(G(T)bar)
         =q(m-8-5deg H)>5qm/256.                (NF2)

The actual maximal Frobenius power of both displayed binary polynomials is q, as proved by the retained exact triple factor.
The full costs use the NEW representative, not the old DG8 numerical bound:

    D_star<q(29040Q^3+7212Q^2+316Q),
    D_big<q(43440Q^3+8418Q^2+444Q),
    original reciprocal polynomial degree=2D_new. (NF3)

The separate actual synthetic integer layer remains12mq with all other layers zero, with the enlarged complete integer factorization and zero-Haar meaning proved in PA.
It is not identified with the constructed canonical integer G(T), and no total-Mahler or field-norm bound is supplied.
This application consumes the GENERIC C730/C733 domain; Y_star and Y_big are not relabeled as witnesses satisfying the original DG8 numerical budget.
The conclusion supplies no height1 or irreducibility guarantee.
For the HB source specifically, any constructed original reciprocal polynomial that happened to have height1 would be reducible by HB10, since its own second residual is already even.
Thus the actual high finite-precision existence and the restricted height1 obstruction coexist with their stated distinct hypotheses.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision complete-parity-height-one-boundary-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T18:57 |
| status | open |
| reason | Register the complete PA1--PA12, HB1--HB10 and NF1--NF3 author theorem after whole contributor reading. Actual complete squared multipliers preserve all full-source canonical/root/fresh/layer/Haar data and enforce parity0 at explicitly enlarged degree cost. The stronger a_big>=d subfamily has the exact own-second-bit height1 factorization obstruction at every raised q, without extending it to the original or weaker family. Generic C730/C733 still supply actual same-degree both1024 and first2048/X1024 traces with their genuine derivative/error powers on either new source. Neither sign feasibility nor irreducible height1 existence is inferred. Fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete multiplier, stronger-subfamily obstruction and finite transfer](#statement) | Parts A--C with both distinct multiplier choices, every original ell/q/source, all exact canonical and full root/multiplicity/layer/Haar costs, precise new degree bounds, only the stronger-subfamily own-second-bit height1 obstruction, and separately fixed-sign generic actual finite outputs with all retained exclusions. |
| argument | [Entire PA/HB/NF proof](#complete-argument) | PA1--PA12 exact functional pairing, local orders and global source preservation; HB1--HB10 separated support, integer Delta carry, all-root degree bound, exact antisymmetry/factorization and raised descent; NF1--NF3 generic hypothesis map, h145 margin, actual derivative/error endpoints and full new expense. |
| dependency | [Adopted complete actual source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 actual H/B/Y, both jets, full canonical/root/gap/layer data and original bounded witness; Section5's retained n_star and exact triple factor, with its quadratic bound. These inputs are preserved with explicitly NEW enlarged bounds, not by calling Y_star or Y_big old DG8 numerical witnesses. |
| dependency | [Adopted full forward and integer-lift mechanisms](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC6 complete ordinary/divided rows, both global forward quotients, exact fresh B_n_star cubed factor, full-primary canonical remainder and full integer cyclotomic-trace/Haar interface C8/FC13, including all multiplicities and source-inspection limits. The new multiplier and stronger height1 obstruction are proved here. |
| dependency | [Adopted complete trace Laurent identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n/W_n root and inverse-pair definitions, squarefreeness, Laurent geometric sum, constant term and full divisor partition only; no finite native support certificate or old gate exclusion is imported. |
| dependency | [Adopted support functional and height1 source interface](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25) | HS12--HS14 complete reciprocal support and Lambda(C_j)=1, source reciprocal nonsquareness, allowed height1 sign/support and exact descent. Its mathematical support argument applies with the actual enlarged degree; its original numerical budget and any unproved sign feasibility are not imported. |
| dependency | [Adopted all-six exact covariance and descent](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact integer trace composition, all-six canonical covariance and exact coefficient orders, height1 support descent and maximal dyadic exponent. Applied to raised height1 inputs without assuming irreducibility or using an unconstructed field norm. |
| dependency | [Adopted generic actual two-jet source](Yin_C_G0730_v1.md#decision-whole-reviewed-2026-10-25) | AS512.1 generic even-a/full-forward/floor/old8a/h_b>145a input and its actual prepared512 output, stronger factors and low coordinates. NF1 verifies this input for each NEW source and original q; its original C691 numerical expense specialization is not reused. |
| dependency | [Adopted generic actual1024 and first2048 outputs](Yin_C_G0733_v1.md#decision-whole-reviewed-2026-10-25) | G1024.1, G10.3 and G10.12 at newly selected original q>=2^41 or2^43: same-degree actual residuals, full primary2^17, derivative divisors and next-error powers, with the uncomputed next second-low quarter and no simultaneous2048 retained. No height1, irreducibility or total-Mahler premise is imported. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T19:07 |
| status | proved |
| reason | Adopt the complete Parts A--C and PA1--PA12/HB1--HB10/NF1--NF3 theorem after fresh isolated whole R958 PASS. Root read the full integrated author argument, fixed standalone statement and full independent finding. Both complete parity-zero multipliers retain every forward/source/root/canonical/fresh-factor/layer condition with their separately enlarged paid degrees. Only the larger a_big>=d choice forces an own-second-first-bit height1 lift, and every raised height1 lift, into the exact reducible L(z^q)(1-z^(2n_big q)) form. The generic C730/C733 application is newly invoked on each enlarged source with its actual new degree and separate sign, retaining finite1024/first2048 and complete component costs. This does not exclude the original C691 or weaker multiplier family, decide all sign systems, identify synthetic and canonical G, or produce an irreducible height1 or small-Mahler realization. The unrestricted Task remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete multiplier, stronger-subfamily obstruction and finite transfer](#statement) | Parts A--C with both distinct multiplier choices, every original ell/q/source, all exact canonical and full root/multiplicity/layer/Haar costs, precise new degree bounds, only the stronger-subfamily own-second-bit height1 obstruction, and separately fixed-sign generic actual finite outputs with all retained exclusions. |
| argument | [Entire PA/HB/NF proof](#complete-argument) | PA1--PA12 exact functional pairing, local orders and global source preservation; HB1--HB10 separated support, integer Delta carry, all-root degree bound, exact antisymmetry/factorization and raised descent; NF1--NF3 generic hypothesis map, h145 margin, actual derivative/error endpoints and full new expense. |
| dependency | [Adopted complete actual source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 actual H/B/Y, both jets, full canonical/root/gap/layer data and original bounded witness; Section5's retained n_star and exact triple factor, with its quadratic bound. These inputs are preserved with explicitly NEW enlarged bounds, not by calling Y_star or Y_big old DG8 numerical witnesses. |
| dependency | [Adopted full forward and integer-lift mechanisms](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC6 complete ordinary/divided rows, both global forward quotients, exact fresh B_n_star cubed factor, full-primary canonical remainder and full integer cyclotomic-trace/Haar interface C8/FC13, including all multiplicities and source-inspection limits. The new multiplier and stronger height1 obstruction are proved here. |
| dependency | [Adopted complete trace Laurent identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n/W_n root and inverse-pair definitions, squarefreeness, Laurent geometric sum, constant term and full divisor partition only; no finite native support certificate or old gate exclusion is imported. |
| dependency | [Adopted support functional and height1 source interface](Yin_C_G0731_v1.md#decision-whole-reviewed-2026-10-25) | HS12--HS14 complete reciprocal support and Lambda(C_j)=1, source reciprocal nonsquareness, allowed height1 sign/support and exact descent. Its mathematical support argument applies with the actual enlarged degree; its original numerical budget and any unproved sign feasibility are not imported. |
| dependency | [Adopted all-six exact covariance and descent](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact integer trace composition, all-six canonical covariance and exact coefficient orders, height1 support descent and maximal dyadic exponent. Applied to raised height1 inputs without assuming irreducibility or using an unconstructed field norm. |
| dependency | [Adopted generic actual two-jet source](Yin_C_G0730_v1.md#decision-whole-reviewed-2026-10-25) | AS512.1 generic even-a/full-forward/floor/old8a/h_b>145a input and its actual prepared512 output, stronger factors and low coordinates. NF1 verifies this input for each NEW source and original q; its original C691 numerical expense specialization is not reused. |
| dependency | [Adopted generic actual1024 and first2048 outputs](Yin_C_G0733_v1.md#decision-whole-reviewed-2026-10-25) | G1024.1, G10.3 and G10.12 at newly selected original q>=2^41 or2^43: same-degree actual residuals, full primary2^17, derivative divisors and next-error powers, with the uncomputed next second-low quarter and no simultaneous2048 retained. No height1, irreducibility or total-Mahler premise is imported. |
| review | [Fresh independent whole complete-source and height1 finding](../audits/reviews/Yin_R_G0958_v1.md#whole-complete-parity-height-one-finding) | Entire fixed Parts A--C, all PA/HB/NF arguments, exact bounded starting source, both enlarged costs and full parity/source preservation, every integer carry/root/height1 endpoint, raised factorization and generic finite-output application with all exclusions. |

