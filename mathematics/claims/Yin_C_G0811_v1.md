---
author: Yin
---

# Complete-cofactor norm obstruction at a fixed fifteenth-order cyclotomic profile

Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract and continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25).
Root proposed the three-shift cyclotomic identity, its inverse-norm consequence and the incompatible first/second leading-unit conditions.
Earlier_bit_obstruction checked the complete cofactor domain, finite-field cancellations, actual original b-value, both valuation alternatives and every field, multiplicity and canonical-divisor limit.
Both are substantive contributors, not independent reviewers.
The [D5 development](../drafts/Yin_D_G0005.md#fifteenth-profile-cofactor-norm-obstruction) is provenance only; the full needed proof is fixed below.
The complete trace and odd-order interfaces are adopted C752/C760 and the original integer canonical convention is adopted C736.
The adopted [C810 UF6--UF9 calculation](Yin_C_G0810_v1.md#decision-whole-reviewed-2026-10-26), authored by Root and Characteristic_zero_bridge, supplies the fixed parameter and a/c factor-unit interface; its mathematical attribution is retained and every arbitrary-cofactor substitution is justified below.
The new b-leading-unit and complete cofactor inverse-norm arguments are included in full.
C763 is a comparison of necessary profiles only, not a realization premise or a proof of either unit cancellation.
No native computation, numerical scan, C810 second-residual observation or the separate F_9^4 B_187 test is an input.
This complete candidate is initially open for a whole reading and fresh independent review; no author check or registration itself adopts it.

## Statement

### CN1. Actual factors, statement and precise excluded class

For n>2 let F_n be the COMPLETE monic integer primitive-order trace polynomial, with

    z^(varphi(n)/2) F_n(z+z^(-1))=Phi_n(z).

Put f_r=F_rbar for odd r>1, where bars denote reduction modulo2.
Let C_j be the integral trace polynomial satisfying C_j(z+z^(-1))=z^j+z^(-j).
Fix the actual integer polynomials

    R_0=(X-2)^2 F_15^2 F_3^2 F_5^3,
    V=F_480=F_30(C_16),
    T=R_0 V Z.                                (CN1)

The cofactor Z is ANY finite product of X-2, X+2 and complete F_n with arbitrary nonnegative integer multiplicities, subject to the following restriction on every occurring n>2.
Write n=2^a r with r odd.
Allow r=1, or allow r>1 with gcd(r,3)=1 and r!=5.
The empty product Z=1 is included.
The restriction r!=5 excludes the EXACT odd part5, not every odd part divisible by5; odd parts such as35 are allowed.
No selected irreducible binary factor may replace a complete F_n.

Every T in this domain is monic integer with fully cyclotomic reciprocal polynomial, and its original trace and reciprocal degrees are

    deg T=82+deg Z, deg P_T=164+2deg Z.        (CN2)

All factors and multiplicities of Z are counted in these costs; no upper bound for deg Z is imposed.
Use the OWN actual original canonical polynomials at T:

    a=rem_T T(C_2)/2, b=rem_T T(C_3)/3,
    c=rem_T T(C_5)/5,
    F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5),
    X_epsilon=rem_T(b^2-a^3+epsilon G),
    epsilon in{1,-1}.                          (CN3)

Every scalar division is on actual integer coefficients before reduction.
The canonical residual F is distinct from the indexed trace factors F_n.

No T in CN1 can satisfy BOTH coefficientwise F=0 modulo4 and X_epsilon=0 modulo2, for either sign.
More precisely, for EVERY primitive480 root zeta, theta=zeta+zeta^(-1), and EVERY normalized dyadic valuation v with v(2)=1 on a number field containing these roots, put zeta=rho eta with rho primitive15, eta primitive32, pi=eta-1, and x=(rho+rho^(-1))bar.
Let y=x^3+x=x^10 and z_y=Zbar(y).
Then the following exhaustive alternative holds:

    if z_y=1, v(F(theta))=5/4;
    if z_y!=1, v(X_epsilon(theta))=3/8
                    for BOTH signs.          (CN4)

The first alternative excludes F modulo4 and the second excludes X modulo2.
For a fixed Z, the alternative is the same at all these roots and places: z_y=1 is equivalent to f_5 dividing Zbar+1.
The argument does NOT assert that F is globally even for arbitrary Z; its coefficient valuation in the first case is at most1, and equals1 only if that separate parity is known.
In the second case the actual X_epsilon has coefficient valuation0.
At the full f_15^18 primary all these T have nonzero binary canonical G of exact order6, as proved in CN6.

## Complete argument

### CN2. Complete-factor units and the exact finite-field inverse norm

C760's full odd-order reduction gives

    Zbar=X^a_Z product_(r>1 odd) f_r^(e_r),

where only r prime to3 with r!=5 occur and all e_r are the actual summed dyadic weights of the complete integer factors.
Explicitly an F_(2^a r) with r>1 contributes weight1 for a=0,1 and weight2^(a-1) for a>=2.
Each pure2 trace factor F_(2^a), a>=2, reduces to X^(2^(a-2)), while both endpoints reduce to X.
These last assertions also follow directly because all primitive2-power roots reduce to1, so all their trace roots reduce to0 with their full degree.

The complete primitive15 trace polynomial is

    F_15=X^4-X^3-4X^2+4X+1,
    f_15=X^4+X^3+1.

The binary quartic has no linear factor and has remainder X upon division by X^2+X+1, hence is irreducible.
Thus every x in CN1 lies in a copy of F_16 in the residue field.
Direct reduction by x^4=x^3+1 gives

    x^15=1, x+1=x^12, x^2+x+1=x^7,
    x^5=x^3+x+1, y=x^10=x^3+x,
    y^2+y+1=0, y!=1.                          (CN5)

The element x has multiplicative order15: its degree excludes orders1,3, and the displayed x^5 differs from1.
Both primitive fifth-order traces are y and y^2; the unique primitive third-order trace is1.
By the distinct full odd-order trace sets in C760, every allowed f_r has nonzero values at x,y,1.
Its value at1 lies in F_2 and hence equals1.
Endpoint and pure2 factors also have nonzero values at x,y and value1 at1.

For an odd r>1 with gcd(r,3)=1, let omega be a primitive third root.
The full cyclotomic product gives the EXACT identity

    product_(j=0)^2 Phi_r(z omega^j)=Phi_r(z^3).
                                                  (CN6)

Indeed for each primitive r-th root xi, the product of the three factors z omega^j-xi is z^3-xi^3, and cubing permutes all primitive r-th roots.
Both sides are monic of the same degree, so no scalar or partial factor is omitted.
Now reduce at a primitive15 root rhobar and set omega=rhobar^5.
Writing d=varphi(r)/2, the three centering monomials on the left multiply to rhobar^(3d), exactly the centering monomial on the right.
Their trace arguments are respectively

    rhobar+rhobar^(-1)=x,
    rhobar^6+rhobar^(-6)=y^2,
    rhobar^11+rhobar^(-11)=x^4,

where the last identity uses11=-4 modulo15.
Cancelling the nonzero centering monomial therefore yields

    f_r(x) f_r(y)^2 f_r(x)^4=f_r(y),
    f_r(x)^5 f_r(y)^2=f_r(y).                 (CN7)

For r!=5 the value f_r(y) is nonzero, so legitimate FIELD cancellation gives

    f_r(y)=f_r(x)^(-5)=f_r(x)^10.             (CN8)

The last equality uses the order15 of F_16^*, not an inversion in a nonreduced primary quotient.
The endpoint factor X obeys y=x^10 as well.
Multiplication and arbitrary nonnegative factor powers give

    Zbar(1)=1, Zbar(x)!=0, Zbar(y)!=0,
    Zbar(y)=Zbar(x)^10.                       (CN9)

Equivalently the right side is the inverse of the finite-field norm Zbar(x)^5 from F_16 to F_4; the explicit calculation CN6--CN8 supplies the needed relation.
This norm relation is proved for the stated COMPLETE factor products and is not assumed for an arbitrary monic cofactor or for an isolated factor of f_r.

### CN3. Actual primitive roots, dyadic parameter and a/c leading units

Fix any root and place from CN1.
The accepted C760 root-difference interface, also used in C810 UF6, gives v(pi)=1/16 and the exact identity

    2=product_(1<=j<32,j odd)(1-eta^j),
    2/pi^16 ->1.                              (CN10)

Each quotient (1-eta^j)/pi has residue1, which proves the last arrow with its actual unit coefficient.
The element pi need not be a uniformizer in a larger containing number field.
Arrows denote residue reduction of genuine valuation-nonnegative algebraic quantities; the normalized a,b,c values below are units.
Distinct odd roots and inverse trace pairs remain distinct at this place by C760, so x and y have exactly the meanings in CN5.

For odd p, put t_p=rho^p+rho^(-p).
Expanding eta^p and eta^(-p) at eta=1 gives

    [C_p(theta)-t_p]/pi -> t_pbar.

For p=2, eta^2-1=pi(pi+2) and v(2/pi)>0 instead give

    [C_2(theta)-t_2]/pi^2 -> x^2.

These expansions imply

    F_15(C_2(theta))/pi^2 -> x^6,
    F_3(C_5(theta))/pi ->1,
    F_5(C_3(theta))/pi ->y.                   (CN11)

The first uses f_15'(x^2)=x^4; the second uses t_5=-1 and F_3=X+1; the third uses F_5(t_3)=0 and f_5'=1.
Every displayed leading residue is nonzero, so the orders in these divisions are exact.

Since V(theta)=0, the actual canonical identities at the ORIGINAL divisor T give

    a(theta)=[V(C_2(theta))/2]R_0(C_2(theta))Z(C_2(theta)),
    b(theta)=[V(C_3(theta))/3]R_0(C_3(theta))Z(C_3(theta)),
    c(theta)=[V(C_5(theta))/5]R_0(C_5(theta))Z(C_5(theta)).
                                                  (CN12)

These are evaluations of T(C_p)=TQ_p+p theta_p(T), with its actual integer quotient; they are not the own unweighted canonical values of V.
For p=2, C_32(theta)=t_2 is an exact primitive15 trace and V(C_2(theta))=F_30(t_2).
The roots of F_30 are the negatives of all primitive15 traces.
Its full product at t_2 contains a unique factor2t_2; dividing that factor by2 and reducing the other distinct factors gives

    V(C_2(theta))/2 -> x^2 f_15'(x^2)=x^6.

The remaining a-factors have normalized residues x^12 from F_15^2/pi^4, x^4 from the endpoint, x^4+1 from F_3^2, x^12 from F_5^3, and Zbar(x)^2 from Z(C_2(theta)).
Using (x^4+1)x^12=1 gives the C810 base-unit calculation with the actual new cofactor:

    a(theta)/pi^4 -> x^7 Zbar(x)^2.           (CN13)

For p=5, C_80(theta)=1 because zeta^80=-rho^5 and t_5=-1.
Consequently V(C_5(theta))=F_30(1)=F_15(-1)=-5, so V(C_5(theta))/5 has residue1.
The endpoint, F_15^2 and F_5^3 factors each have residue1, F_3(C_5(theta))^2/pi^2 has residue1, and Z(C_5(theta)) has residue Zbar(1)=1.
Thus

    c(theta)/pi^2 ->1.                        (CN14)

Equations CN13--CN14 generalize exactly the fixed factor calculation of C810 UF8--UF9, without importing its special B_n residue classes or global coefficient parity.

### CN4. The new original b-leading unit

Put t=t_3=rho^3+rho^(-3), an exact primitive5 trace, with t^2+t-1=0.
Since zeta^48=-rho^3, C_48(theta)=-t and

    V(C_3(theta))=F_30(-t)=F_15(t)=3t.        (CN15)

For the last equality reduce X^4-X^3-4X^2+4X+1 modulo X^2+X-1: X^3=2X-1 and X^4=2-3X, leaving exactly3X.
Thus V(C_3(theta))/3=t is an actual integral unit, with residue y.
After the division by pi^3 in CN12, the other factors have residues

    F_5(C_3(theta))^3/pi^3 -> y^3,
    (C_3(theta)-2)^2 -> y^2,
    F_15(C_3(theta))^2 -> f_15(y)^2=y^2,
    F_3(C_3(theta))^2 ->(y+1)^2=y,
    Z(C_3(theta)) -> Zbar(y).

Here f_15(y)=y, y^3=1 and y+1=y^2 follow from CN5.
Including the factor V(C_3(theta))/3, the product of all fixed residues is y^(1+3+2+2+1)=y^9=1.
Therefore the exact original leading value is

    b(theta)/pi^3 -> Zbar(y).                (CN16)

Together CN13, CN14 and CN16 prove

    v(a(theta))=4/16, v(b(theta))=3/16,
    v(c(theta))=2/16.                         (CN17)

All are below1 and all hold at every primitive480 trace and every normalized dyadic place, with no chosen complex or residue embedding.

### CN5. The two required leading cancellations are incompatible

Evaluation at theta annihilates the actual divisor in the canonical F and X_epsilon remainders, so their values equal the ORIGINAL numerator values.
The two first-residual terms have value20/16, and CN10/CN13/CN14 give

    F(theta)/pi^20 ->1+x^5 Zbar(x)^10.        (CN18)

For the second residual, b^2 and c^3 have value6/16, while a^3 has value12/16 and 2b^5 has value31/16.
Both signs epsilon have residue1, so

    X_epsilon(theta)/pi^6 ->Zbar(y)^2+1.      (CN19)

If z_y=1, the norm relation CN9 makes Zbar(x)^10=1, and CN18 is the nonzero element1+x^5.
It follows that v(F(theta))=20/16=5/4.
If z_y!=1, its square differs from1 in characteristic2, so CN19 is nonzero and v(X_epsilon(theta))=6/16=3/8 for both signs.
This proves CN4 and shows directly that one of the two global congruences must fail.
Indeed an integer polynomial divisible coefficientwise by4 has value at least2 at the algebraic integer theta, and one divisible by2 has value at least1.

Equivalently, F modulo4 would force Zbar(x)^10=x^(-5)=x^10=y, while X_epsilon modulo2 would force Zbar(y)=1, contradicting CN9 and y!=1.
These are necessary leading cancellations, not sufficiency assertions when a leading term vanishes.
Because the two roots of f_5 are y,y^2 and Zbar has F_2 coefficients, Zbar(y)=1 at one of them holds exactly when it holds at both, namely when f_5 divides Zbar+1.
Thus the exhaustive alternative is independent of the selected primitive480 root and dyadic place.
Global F parity is not supplied by this local calculation; if F is separately known even in the first branch, then and only then the value5/4 implies its exact coefficient valuation1.

<a id="cn6-full-primary-check-exact-c805-comparison-and-remaining-scope"></a>
### CN6. Full-primary check, exact C763 comparison and remaining scope

No allowed Z factor has odd part3,5 or15, so the full binary f_15 multiplicity in T is exactly18, the f_3 multiplicity is2 and the f_5 multiplicity is3.
The endpoint multiplicity may increase from2, but it is a unit on f_15 and on its third/fifth image traces.
On the FULL f_15^18 primary, C760's actual Delta product gives a unique largest odd dyadic weight16 from V, with the cofactor contributing f_15^2; hence

    ord_(f_15)(abar)=2(18-16)=4.

For bbar, C_3bar=x^3+x maps primitive15 traces to primitive5 traces and has derivative x^2+1 nonzero there.
Only the full f_5^3 factor vanishes at that image, with Zbar(y) a unit, so bbar has exact f_15 order3.
For cbar, C_5bar=X(X^2+X+1)^2 maps those traces to1 and has nonzero derivative f_5(x)^2; only f_3^2 vanishes there, and Zbar(1)=1.
Thus cbar has exact f_15 order2.
Actual reduction modulo T cannot change these orders below18, and

    ord_(f_15)(Gbar)=ord_(f_15)(cbar^3)=6<18. (CN20)

In particular the excluded class has nonzero binary canonical G, not merely nonzero integer G.
This full-primary conclusion does not assert that other primary residuals pass.

The triple E=18, B=2, D=3 with u=2,w=16 satisfies C763's h=15 necessary multiplicity and valuation-tie conditions in its branch B<2u.
The present result supplies a further obstruction for the specified actual fixed R_0,V and complete cofactor class; it does not refute those necessary conditions or claim their sufficiency.
The two leading-cancellation equations cannot be eliminated in this way for a cofactor with an odd part divisible by3, or with odd part5, because the field identity or the unit cancellation used in CN7--CN9 is then unavailable.
In particular an F_9 factor is outside the proved class.
No conclusion about the separately investigated F_9^4 B_187 example is inferred from this theorem, and no native output from that investigation is consumed.
General h divisible by15, different actual multiplicity profiles, incomplete primitive factors and arbitrary cofactor values require their own compatible unit analysis.
No global exclusion of all cyclotomic F4/X2 inputs with nonzero binary G, no higher-coefficient sufficiency claim and no unrestricted Task completion follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision complete-cofactor-norm-obstruction-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T18:17 |
| status | open |
| reason | Register the full CN1--CN6 candidate for the ACTUAL fixed R_0=(X-2)^2F_15^2F_3^2F_5^3, V=F_480 and arbitrary finite complete-factor cofactor Z whose odd parts are1 or prime to3 and unequal to5. Every factor, dyadic weight, endpoint and degree is retained. The exact three-shift cyclotomic product and legitimate finite-field cancellation give Zbar(1)=1 and Zbar(y)=Zbar(x)^10. Actual original-divisor evaluations give a/pi^4 -> x^7 Zbar(x)^2, c/pi^2 ->1 and the new b/pi^3 ->Zbar(y). At EVERY primitive480 trace and normalized dyadic place, the exhaustive branch Zbar(y)=1 gives exact v(F)=5/4, while the other branch gives exact v(X_epsilon)=3/8 for both signs. Thus the simultaneous global F modulo4/X modulo2 gates fail throughout this class. The full f_15^18 primary has a/b/c/G orders4/3/2/6, hence nonzero binary G. Root and Earlier_bit_obstruction are contributors; the adopted C810 a/c provenance retains Root and Characteristic_zero_bridge attribution. Whole reading and fresh independent review remain outstanding. No global F evenness or exact coefficient valuation1 is inferred for arbitrary Z; the local dichotomy, coefficient at-most1 versus X coefficient0 conclusions and the extra-parity qualification remain explicit. No other cofactor class, incomplete primitive factor, general15-divisible profile, native probe, higher-cancellation sufficiency, positive Mahler claim or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete cofactor-class exclusion and every-root dichotomy](#statement) | CN1--CN4 with CN9/CN13--CN20: finite arbitrary complete Z products including empty/endpoints/pure2 and all multiplicities, exact excluded odd parts, original degrees and canonical divisor, both signs, every primitive480 trace and every normalized dyadic place, leading units and global gate failure, precise local-versus-coefficient valuation limits and full-primary nonzero G. |
| argument | [Entire norm, canonical-unit and obstruction proof](#complete-argument) | CN2--CN6: complete binary reductions and units, full three-shift primitive product with centering, F_16 inverse norm and arbitrary powers, genuine dyadic parameter and a/c factors, exact F_15(t_3)=3t_3 primitive-fifth-trace b evaluation, all residual term values and exhaustive incompatibility, root/place independence, actual Delta/composition primary orders and scope limits. |
| dependency | [Adopted full cyclotomic trace classification](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3 complete integer trace factors and endpoint multiplicities, symmetric-Laurent definition and reciprocal degrees. No E=7A profile conclusion, noncyclotomic degree bound or positivity statement is applied to the present fully cyclotomic family. |
| dependency | [Adopted odd-order trace and root/Delta interface](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | OT3--OT10 full f_r reductions and dyadic weights, distinct odd traces at every dyadic place, genuine primitive2-power root product/valuation, complete largest-weight Delta unit. Used at the actual fifteenth-order primary with all factors retained; no zero-beta conclusion for orders prime to3 is transferred to h=15. The accepted Bel17/The26b inspection and normalization limits remain unchanged. |
| dependency | [Adopted actual original canonical integer identities](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT2 integer prime-divisible monic remainders and actual factor-weighted evaluation at a root of V. All expressions remain the ORIGINAL T canonical polynomials, with no division in a binary quotient or unweighted factor inheritance. |
| dependency | [Adopted fixed primitive480 parameter and a/c factors](Yin_C_G0810_v1.md#decision-whole-reviewed-2026-10-26) | UF6--UF9 complete x-field identities, every primitive480 root/place, v(pi)=1/16 and2/pi^16 unit, and fixed V/R_0 factors in original a/c evaluation. CN3 explicitly supplies Z(C_2)->Zbar(x)^2 and Z(C_5)->1 for the NEW complete class, and CN4 derives b in full. No B_n finite residue table, special-family global F parity, native second-residual observation or arbitrary-cofactor conclusion is imported. |
| support | [Necessary fifteenth-order profile comparison](Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: E=18,B=2,D=3,u=2,w=16 satisfies the arithmetic and valuation-tie necessities. Those necessary conditions are not treated as a realization or unit-cancellation input, and the present exclusion is not extended to all profiles they allow. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T18:45 |
| status | proved |
| reason | Adopt the unchanged complete CN1--CN6 statement and argument after the responsible main agent read the entire fixed C811 and the entire isolated independent R1031 finding. The full cofactor domain, exact inverse-norm identity, original weighted a/b/c values, every-root/place dichotomy and coefficient-versus-local valuation limits are covered, with all actual factors and multiplicities retained. The accepted dependencies and source-inspection limits remain exactly those selected below. The first branch does not assert global F parity; the second has both X signs odd. Odd part5, odd parts divisible by3, incomplete factors, other multiplicity profiles, native candidate probes and unrestricted G0001 completion remain outside the result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete cofactor-class exclusion and every-root dichotomy](#statement) | CN1--CN4 with CN9/CN13--CN20: finite arbitrary complete Z products including empty/endpoints/pure2 and all multiplicities, exact excluded odd parts, original degrees and canonical divisor, both signs, every primitive480 trace and every normalized dyadic place, leading units and global gate failure, precise local-versus-coefficient valuation limits and full-primary nonzero G. |
| argument | [Entire norm, canonical-unit and obstruction proof](#complete-argument) | CN2--CN6: complete binary reductions and units, full three-shift primitive product with centering, F_16 inverse norm and arbitrary powers, genuine dyadic parameter and a/c factors, exact F_15(t_3)=3t_3 primitive-fifth-trace b evaluation, all residual term values and exhaustive incompatibility, root/place independence, actual Delta/composition primary orders and scope limits. |
| dependency | [Adopted full cyclotomic trace classification](Yin_C_G0752_v1.md#decision-whole-reviewed-2026-10-25) | CY3 complete integer trace factors and endpoint multiplicities, symmetric-Laurent definition and reciprocal degrees. No E=7A profile conclusion, noncyclotomic degree bound or positivity statement is applied to the present fully cyclotomic family. |
| dependency | [Adopted odd-order trace and root/Delta interface](Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) | OT3--OT10 full f_r reductions and dyadic weights, distinct odd traces at every dyadic place, genuine primitive2-power root product/valuation, complete largest-weight Delta unit. Used at the actual fifteenth-order primary with all factors retained; no zero-beta conclusion for orders prime to3 is transferred to h=15. The accepted Bel17/The26b inspection and normalization limits remain unchanged. |
| dependency | [Adopted actual original canonical integer identities](Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT2 integer prime-divisible monic remainders and actual factor-weighted evaluation at a root of V. All expressions remain the ORIGINAL T canonical polynomials, with no division in a binary quotient or unweighted factor inheritance. |
| dependency | [Adopted fixed primitive480 parameter and a/c factors](Yin_C_G0810_v1.md#decision-whole-reviewed-2026-10-26) | UF6--UF9 complete x-field identities, every primitive480 root/place, v(pi)=1/16 and2/pi^16 unit, and fixed V/R_0 factors in original a/c evaluation. CN3 explicitly supplies Z(C_2)->Zbar(x)^2 and Z(C_5)->1 for the NEW complete class, and CN4 derives b in full. No B_n finite residue table, special-family global F parity, native second-residual observation or arbitrary-cofactor conclusion is imported. |
| support | [Necessary fifteenth-order profile comparison](Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25) | Comparison only: E=18,B=2,D=3,u=2,w=16 satisfies the arithmetic and valuation-tie necessities. Those necessary conditions are not treated as a realization or unit-cancellation input, and the present exclusion is not extended to all profiles they allow. |
| review | [Whole independent complete-cofactor finding](../audits/reviews/Yin_R_G1031_v1.md#whole-finding) | Entire fixed statement and CN1--CN6 argument, every allowed complete cofactor/multiplicity, both signs and every root/place, exact source/dependency interfaces, local and global coefficient consequences, full-primary nonzero G and all stated exclusions. No native computation or broader cyclotomic exclusion is adopted. |

