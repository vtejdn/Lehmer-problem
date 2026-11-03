---
author: Yin
---
# Uniform full-gate CRT and the normalized multiplicity-sixteen complement reduction

Human author Yin.
Root supplied the uniform full-gate CRT proposal, including the necessary eleventh-root correction when S starts at order4m.
The same_trace contributor checked all root/error precisions and formal necessity/sufficiency, derived the exact multiplicity-sixteen targets and their symbolic old-image comparison, and retained the complete original support and degree bridge.
Both are mathematical contributors; neither independently reviews this new proof.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this bounded continuation.
Focused reuse inspected adopted C643v2's complete homogeneous-cube classification, C636's higher-order formal CRT and exact T_(1,0) membership, C630's order-four quotient class, and the actual C197/C199 normalized interfaces.
The C636 root simplification applies at its higher correction order; the present proof retains the extra root term needed at general order4m.
The [D1 candidate](../drafts/Yin_D_G0001.md#uniform-homogeneous-full-crt-candidate) is development provenance, not a logical input.
No native computation or larger-quotient group construction is used.
The result is initially open for fresh isolated whole mathematical review.

## Statement

### Complete formal equivalence throughout the homogeneous branch

Work over F_2 and put phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi).
Let m>=1.
Let S be a specified class modulo phi^(8m), divisible by phi^(4m).
Let B be any monic phi-unit polynomial with deg B<4m, and Y any polynomial prime to Xphi with X^(4m) dividing Y'.
Define

    H_0=X^(2m)Y, V_0=H_0B,
    C_00=X^(2m)Y(chi)Psi^(14m),
    D_0=H_0B+C_00^3.

Assume the inherited initial order D_0 in phi^(2m).
Let Z_0 be the unique unit class satisfying

    Z_0^11=H_0C_00^2 modulo phi^(6m).

The old support relation and full unit gate

    H_0^6=C_00^21 modulo phi^(8m),
    Z_0D_0+H_0V_0S=0 modulo phi^(8m)                       (HC2)

are independent of the lift of Z_0 under the stated initial D_0 order.
They hold if and only if there are UNIQUE data Q,H with

    Q a power of2, 2m<Q<5m,
    H in F_2[t], H(0)=1, 5deg H<5m-Q,
    B=X^(Q-m)H(chi),

and the SAME Y satisfies the following two exact CRT jets.

Use the adopted formal inverse x(t) of chi at0 and, for Q=2^s, put

    h_Q(X)=1+sum_(i=0)^(s-1)X^(Q-2^i),
    L(t)=[(1+t+t^2)^(7m)H(t)h_Q(x(t))]^(-1)
                          modulo t^(2m), deg L<2m.       (HC1)

Choose N with2^N>=8m and2^N congruent to Q modulo3, and put beta=X^(2^N) as a class modulo phi^(8m).
Then the two jets are

    Y=L(X^2) modulo X^(4m),
    Y=X^(-2m)B^(-7)+beta X^(-2m)B^(-13)S
                                        modulo phi^(8m). (HC3)

All X and B inverses in (HC3) are phi-local units.
The inverse in (HC1) is a formal unit at t=0.
The class beta satisfies beta^3=1, has residue X^Q at phi, and is independent of the admissible choice of N at every precision used here.

More precisely, put delta=H_0+B^(-7) in the local quotient.
Under the equivalent conditions,

    C_00=beta^2B^(-2), C_00^3=B^(-6),
    delta=beta B^(-13)S                         modulo phi^(8m),
    ord_phi D_0>=4m.

The corrected root is

    Z_0=beta^2B^(-1)(1+B^7delta)                modulo phi^(6m), (HC4)

or equivalently

    Z_0=beta^2B^(-1)(1+beta B^(-6)S)            modulo phi^(6m). (HC5)

This correction may be nonzero at root precision.
It disappears from the PRODUCT Z_0D_0 only because delta^2 has order at least8m.

For every admissible m,Q,H and S, (HC3) determines a unique class modulo X^(4m)phi^(8m).
Every polynomial representative is prime to Xphi and satisfies the low-X derivative, inherited D_0 order, root, old support and full unit equations just stated.
There is no bound on the degree of an arbitrary representative and no assertion about its complete odd-order factor pattern or all-primary canonical remainder.
The formal S in this theorem need not be a square; an actual original application below retains its specified square layer sum and every further original constraint.

### Four exact multiplicity-sixteen targets

At m=8 the homogeneous classification permits only Q=32 and H_eta(t)=1+eta t, eta in{0,1}.
Put

    B_eta=X^24 H_eta(chi),
    S_epsilon=epsilon X^32(X+1)^64phi^32,
    epsilon in{0,1}.

Take beta=X^128:128>=64 and128 is congruent to Q=32 modulo3.
The four distinct full CRT classes modulo X^32phi^64 are

    Y=(1+X^16)/(1+eta X^2) modulo X^32,
    Y=X^8H_eta(chi)^(-7)
       +epsilon X^24(X+1)^64phi^32 H_eta(chi)^(-13)
                                         modulo phi^64.   (HC6)

For eta=0 the low class is1+X^16.
For eta=1 it is sum_(i=0)^7 X^(2i).
These are all four FORMAL targets, including the genuine nonsquare complement B_1.
No complete-support representative of a new full target is asserted.

In the old ring R=F_2[X]/(X^8phi^16), let G be the image of all complete primitive odd-order trace polynomials W_n with odd n>1,n!=5, at arbitrary finite nonnegative multiplicities.
Let y be the unit with components

    y=1+X^4 modulo X^8, y=X^2 modulo phi^16.

Write U_eta for the projection of either epsilon target in (HC6) to R.
Then the exact cosets are

    U_0G=G, U_1G=yG!=G.                                  (HC7)

More exactly, U_0=y^4 and U_1=T_(1,0)y^21, where T_(1,0) is C636's fixed member of G with components

    T_(1,0)=(1+X^4)/(1+X^2) modulo X^8,
    T_(1,0)=X^14/(1+chi)^7 modulo phi^16.

The positive old projection U_0 does not establish membership of either full X^32phi^64 target in a complete-support image.
It is separate from the arbitrary-polynomial formal CRT solvability.

### Exact original domain and the surviving complete complement

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For an original root alpha put K=Q(alpha), delta_original=alpha+alpha^(-1), and suppose F=Q(delta_original) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, with P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta_original), b=theta_3(delta_original),
    c=theta_5(delta_original).

Assume a,b,c are nonzero and, for one sgn in{1,-1},

    2c^2=3a^5,
    b^2-a^3+sgn(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2 and R_can=G_can mod2.
Assume the normalized circle Haar integral of log(G_can(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Assume the unique unsaturated factor is phi:

    ord_phi R_can<ord_phi U,
    ord_psi R_can>=ord_psi U for every irreducible psi dividing U,
                                               psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power.
Retain C199's actual canonical roots U=U_0^q,R_can=R_0^q, and put A_0=ord_XU/q=2m.
Then

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3)=X^(2m)Yphi^(12m)B,

with B the COMPLETE monic complement, prime to phi and of degree below4m.
Retain all original nonnegative integer layer multiplicities a_b in the SAME zero-Haar integer factorization of G_can, with

    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq,
    S_star=sum_(a_b odd, 4mq<lambda_b<12mq)
       X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                       phi^(12m-lambda_b/q).

No a_b or original layer index is divided by q.

If NO odd original layer occurs with8m<lambda_b/q<=10m, the actual S_star lies in phi^(4m), and (HC1)--(HC5) hold necessarily for this SAME Y,B and specified S=S_star.
This gives full two-primary targets, not a sufficient original construction.
The exact degrees are

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(4m-deg B)=q(5m-Q-5deg H)>0.

In particular, at A_0=16, m=8, the unique complete complement MUST be

    B=X^24.                                               (HC8)

The actual correction is S_star=S_epsilon with epsilon=a_(k+7) in{0,1}, at the original index k+7.
All lower original layers remain, with their paid total weight96q-64q epsilon.
The conditional original degrees are

    r=q(240+deg Y), w=q(232+deg Y),
    r-w=8q, 2w=d-16q.

The formal alternative B=X^24(1+chi), whose hypothetical degree gap would be3q, is excluded by the complete support projection (HC7).
The two remaining full targets for B=X^24 have not been tested in their complete larger image.
No original realization, full A_0=16 exclusion, A_0=14 inhomogeneous conclusion or unrestricted Task completion is asserted.

## Argument

### Cube constants, root precision and classified low coefficients

The finite ring F_2[X]/phi^(6m) has unit-group order3*4^(6m-1).
Since11 is prime to this order, the eleventh-power map is an automorphism and the unit root Z_0 exists uniquely.
The initial order D_0 in phi^(2m) makes its full product independent of the chosen root lift: an error in phi^(6m) contributes only in phi^(8m).

For any N as in the statement,

    beta^3+1=(X^3+1)^(2^N)
            =(X+1)^(2^N)phi^(2^N)=0 modulo phi^(8m).

The residue X^(2^N) agrees with X^Q because nonzero phi residues have order3.
An admissible N exists by choosing its parity and then making it sufficiently large.
For a principal unit1+u, u in(phi), the exact factor

    (1+u)^3+1=u(1+u+u^2)

has the same phi order as u.
Thus the cube-one lift of a fixed nonzero residue is unique, and all admissible beta choices give the same local class.

Suppose the formal gate (HC2) holds.
As S lies in phi^(4m), the gate and the unit Z_0 force D_0 in phi^(4m).
The actual low-X derivative assumption gives a unique polynomial L_0 of degree below2m with

    Y=L_0(X^2) modulo X^(4m), L_0(0)=1.
    Q_aux=X^mPsi^(7m)L_0(chi).

Substitution pays precisely the doubled phi order because ord_phi chi=2.
Therefore

    C_00=Q_aux^2 modulo phi^(8m).

From H_0B=C_00^3 modulo phi^(4m), taking sixth powers raises the error order to at least8m.
Use H_0^6=C_00^21 at that precision and divide by the unit C_00^18.
This gives B^6C_00^3=1 modulo phi^(8m).
After substituting Q_aux^2, exact square valuation yields

    (BQ_aux)^3=1 modulo phi^(4m).

Apply the [adopted C643v2 complete homogeneous classification](Yin_C_G0643_v2.md#statement) to f=X^mB and auxiliary polynomial (1+t+t^2)^(7m)L_0(t).
It applies to the entire B, with deg B<4m and arbitrary auxiliary coefficients.
It supplies the unique Q,H, the sharp bounds2m<Q<5m and5deg H<5m-Q, and L_0=L from (HC1).
This proves the necessary first jet.

Conversely, for any classified Q,H and the prescribed L, the same C643v2 if-and-only-if theorem gives(BQ_aux)^3=1 modulo phi^(4m).
Its residue is X^Q, since H(0)=L(0)=1 and Psi=1 at phi.
Uniqueness of the cube-one lift therefore gives BQ_aux=beta modulo phi^(4m).
Squaring and using C_00=Q_aux^2 at8m gives

    C_00=beta^2B^(-2), C_00^3=B^(-6)
                                                modulo phi^(8m).

These formulas follow from the first jet in either direction, with all low and high auxiliary bits accounted for.
No root precision is increased without paying the square factor.

### The corrected eleventh root and the second jet

Work in the local quotient at8m, and put delta=H_0+B^(-7).
In the necessity direction, D_0 is divisible by phi^(4m), and the preceding C_00^3 identity gives

    D_0=Bdelta modulo phi^(8m),
    delta in phi^(4m).

The equality with Bdelta is a congruence at the displayed precision, not a global polynomial identity.
Set u=B^7delta, so u^2=0 modulo phi^(8m).
The proposed root representative is

    Z_*=beta^2B^(-1)(1+u).

Because all powers u^i with i>=2 vanish at8m, its eleventh power is

    Z_*^11=beta B^(-11)(1+B^7delta)
           =beta B^(-11)+beta B^(-4)delta
           =H_0C_00^2 modulo phi^(8m).

Here beta^22=beta and C_00^2=beta B^(-4) at the same precision.
In particular it has the required root equation at6m, so uniqueness gives (HC4).
The root class may retain its u correction; replacing it by the constant factor is not generally allowed.

Multiplying by the actual D_0, however, gives

    Z_0D_0=beta^2delta+beta^2B^7delta^2
           =beta^2delta modulo phi^(8m).

The error from replacing the root by Z_* modulo phi^(6m) has order at least10m because D_0 is now in phi^(4m).
Also

    H_0V_0S=H_0^2BS
           =(B^(-14)+delta^2)BS
           =B^(-13)S modulo phi^(8m).

Thus the full gate is equivalent to

    beta^2delta+B^(-13)S=0 modulo phi^(8m),
    delta=beta B^(-13)S modulo phi^(8m).

Multiplying H_0=B^(-7)+delta by X^(-2m) gives exactly the second jet in (HC3).
All coefficients divided here are local units, and beta^(-2)=beta at8m.

### Sufficiency, all representatives and formal limitations

Conversely suppose both jets (HC3) hold for the classified data.
The first jet gives the two C_00 formulas already proved.
The second gives delta=beta B^(-13)S, so delta is in phi^(4m) and the actual D_0 is in phi^(4m).
Every nonconstant term in the sixth power of B^(-7)+delta contains delta^2.
Consequently

    H_0^6=B^(-42)=C_00^21 modulo phi^(8m).

The corrected root calculation applies and now reads (HC5).
Its product with D_0 is B^(-13)S at8m, while H_0V_0S is the same class.
Their sum is0 in characteristic2, proving the full gate.

The moduli X^(4m) and phi^(8m) are coprime.
The first component has constant1.
The second is

    X^(-2m)B^(-7)(1+beta B^(-6)S),

a phi-unit because S is nilpotent at phi.
Thus CRT gives a unique class, with a canonical representative of degree below20m and all polynomial representatives Y=Y_*+X^(4m)phi^(8m)K, K in F_2[X].
Every representative remains prime to Xphi.
Its even low-X jet implies X^(4m)|Y', since the derivative of X^(4m) is zero.
Substitution of the fixed low jet determines C_00 at8m, so every representative satisfies the proved old/root/gate system.
Arbitrary K can increase the degree without bound; this is not a bound on any actual original Y.

This formal equivalence uses only the explicitly listed equations.
It constructs no all-primary equality R_0=rem_(U_0)(U_0(chi)^3), complete-order support, global maximal q, integer cyclotomic factorization, monic characteristic-zero T or original residual solution.
The arbitrary formal S is not reassigned to the actual layer sum in an original application.
When the actual S is square, as C199 requires, that fact and every further inherited condition remain intact.

### Exact symbolic multiplicity-sixteen targets

At m=8, the sharp power range16<Q<40 contains only32.
The degree bound5deg H<40-32=8 gives H=1 or1+t.
These are exactly H_eta, including the nonsquare B_1=X^24(1+chi).

For Q=32, the smallest exponent in h_32-1 is16.
Since x(t) has order1,

    h_32(x(t))=1 modulo t^16.

Frobenius gives(1+t+t^2)^56=1+t^8 modulo t^16.
The inverse of1+t^8 at this precision is itself.
Therefore

    L_eta(t)=(1+t^8)/(1+eta t) modulo t^16.

For eta=0 this is1+t^8; for eta=1 it is the exact polynomial sum_(i=0)^7 t^i.
Substituting X^2 proves the first component of (HC6).

The admissible beta=X^128 has the required residue and precision.
In the phi-local ring,

    X^192+1=(X^3+1)^64=(X+1)^64phi^64,

so X^192=1 modulo phi^64.
For B_eta=X^24H_eta(chi), the base term of (HC3) has X exponent-16-7*24=-184, congruent to8 modulo192.
The S correction has exponent128-16-13*24+32=-168, congruent to24 modulo192.
This proves the second component of (HC6) exactly, with no finite program.

The original correction window at A_0=16 is STRICTLY

    32q<lambda_b<96q.

It contains only64q, at b=k+7.
The32q layer is the excluded lower endpoint; its original integer multiplicity remains paid in the full factorization and is not an S_star term.
There is no power of two in(64,80], so every actual m=8 input belongs to the homogeneous branch.
The total weight96q bounds a_(k+7) by1, hence epsilon is its actual value, not an independently reassigned normalized layer.

For epsilon=1, the correction in (HC5) has exact phi order32, below the root precision48.
It is therefore nonzero in the root equation and cannot be discarded.
Its product with D_0 has order64, exactly the full precision where it vanishes.
This directly records the root-correction boundary of the uniform theorem.

The two eta values have different low-X classes, already at X^2.
For fixed eta, the two epsilon values differ by a phi-unit times phi^32, nonzero modulo phi^64.
Thus all four full classes are distinct.
Their formal CRT solvability and the following complete-support obstruction are different assertions.

### Symbolic comparison in the adopted old complete image

Use the complete image G in R stated above.
The [adopted C630 theorem](Yin_C_G0630_v1.md#statement) gives exact order4 for yG.
The [adopted C636 theorem](Yin_C_G0636_v1.md#statement) gives T_(1,0) in G with precisely the two components in the statement.
These are fixed mathematical membership inputs; no native output is extended to a new modulus.

The correction term of (HC6) is in phi^32, so it vanishes upon projection to phi^16.
The two projected components are

    U_eta=(1+eta X^2)^(-1) modulo X^8,
    U_eta=X^8(1+eta chi)^(-7) modulo phi^16.

For eta=0 these are exactly the components of y^4:
(1+X^4)^4=1 modulo X^8 and(X^2)^4=X^8.
Thus U_0=y^4 and its coset is G.

For eta=1, division by the fixed T_(1,0) gives

    U_1/T_(1,0)=(1+X^4)^(-1)=1+X^4 modulo X^8,
    U_1/T_(1,0)=X^(-6) modulo phi^16.

The exact identity X^48=1 modulo phi^16 follows by raising X^3+1=(X+1)phi to the16th power.
Thus X^(-6)=X^42=(X^2)^21 there.
Also(1+X^4)^21=1+X^4 modulo X^8.
CRT therefore gives the exact identity

    U_1=T_(1,0)y^21.

Since T_(1,0) belongs to G and yG has order4, U_1G=yG!=G.
This proves (HC7) for both epsilon values, without any new bounded computation or assumption about the larger image.

### The actual complete-factor bridge, original precision and costs

Retain the full original hypotheses in the statement.
The [actual C199 normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) supplies the specified original integer sum S_star, its square property, inherited orders and6m/8m root/error precision.
The [complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) supplies the full B, including every saturated surplus and every extra factor.
The [C197 derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives X^(4m)|Y' through the normalized T-support odd part.
The [C643v2 original dichotomy](Yin_C_G0643_v2.md#statement) proves that absence of an odd intermediate layer gives S_star in phi^(4m), retaining every original index and coefficient.
Thus the formal equivalence applies NECESSARILY to the SAME actual Y,B,S_star.
It does not replace them by a different CRT solution.

For general H the theorem does not infer that Y separately has complete group multiplicities merely from its two jets.
At m=8, however, both H_eta(chi) are complete allowed products.
The identity

    1+chi=B_3(chi)=B_15/phi=W_3W_15

is retained at its exact polynomial scope in the [C636 complete-factor proof](Yin_C_G0636_v1.md#argument).
The actual normalized V_0 has the [complete group factorization inherited from the same integer zero-Haar factorization](Yin_C_G0199_v4.md#argument), with the uniform multiplicities divided by the ACTUAL common q, not by freely divided integer layers.
Here

    V_0=X^40YH_eta(chi).

For eta=0 there is no factor to remove.
For eta=1 remove the complete factors W_3 and W_15, each with its uniform multiplicity1.
They divide the actual V_0 because H_eta(chi) does, so removal leaves nonnegative uniform multiplicities.
Since Y is prime to Xphi, this proves that its class belongs to G.
This argument retains all other odd orders, including arbitrary higher5 orders, without a support-order or degree cutoff.

If eta=1, its necessary projected class is U_1, which is outside G by (HC7).
This contradiction excludes that COMPLETE complement, proving (HC8).
For eta=0 the old projected class lies in G, but that fact does not construct a complete Y with either stronger full jet.
Neither an all-primary canonical condition nor the original characteristic-zero equations is inferred from that old projection.

Finally the complete exact factors give

    deg U_0=30m+deg Y,
    deg R_0=26m+deg Y+deg B.

The zero-Haar integer factorization has leading coefficient1 or-1, so reduction preserves the degree of G_can.
Restoring the actual q gives all degree identities in the statement.
At m=8, deg B=24+5eta, so the conditional gap is q(8-5eta):8q for the surviving monomial and3q for the excluded formal alternative.
No factor or surplus is discarded by the support argument.
The maximal q and nonsquare normalized U_0,R_0 stay actual C199 conclusions, not consequences of the formal CRT.
The A_0=14 inhomogeneous branch and all unresolved original realization questions remain outside this result.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:14 |
| status | open |
| reason | Register the all-m formal old/root/gate CRT equivalence with the necessary6m root correction, all low/high auxiliary bits and full8m products; retain every formal target and the complete original applicability boundary. At A_0=16 the four exact targets are derived analytically, and the eta=1 complete complement is excluded by an exact identity in the adopted old image, leaving only B=X^24 and two untested stronger support targets. All original q/layers/degree costs remain. No new native computation or original realization is claimed. Fresh isolated whole mathematical review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform CRT and original complement statement](#statement) | HC1--HC8: complete formal iff, unique classified B and low jet, corrected root, formal CRT feasibility, all four m=8 targets, exact old cosets and original necessary B=X^24. |
| argument | [Whole root, CRT and complete-support argument](#argument) | Every unit and6m/8m lift/error calculation, corrected eleventh power and its product cancellation, all formal representatives, exact m=8 layers/targets, symbolic T_(1,0)y^21 identity and actual factor/degree bridge. |
| dependency | [Complete homogeneous classification](Yin_C_G0643_v2.md#statement) | Sharp Q/H classification, unique auxiliary class at2m and actual homogeneous-branch dichotomy; no descent of original inputs. |
| dependency | [Formal inverse and cube precision proof](Yin_C_G0643_v2.md#argument) | Exact x,h_Q definitions, all auxiliary high bits and square/cube valuation interfaces reused at4m/8m. |
| dependency | [Original normalized domain](Yin_C_G0199_v5.md#statement) | Same original P,T,fields,divided remainders,residual,Haar/unsaturation and actual maximal q. |
| dependency | [Actual normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Original integer a_b/lambda_b/weight, S_star, root6m/error8m, old relation and lift independence. |
| dependency | [Complete complement and canonical costs](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Full B with every saturated surplus and extra factor, strict degree bound and canonical degree identities. |
| dependency | [Actual complete normalized group factorization](Yin_C_G0199_v4.md#argument) | Uniform nonnegative order multiplicities of V_0 after actual q extraction, used only with the complete m=8 H_eta factors. |
| dependency | [Normalized derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divides Y' through the actual T-support odd part. |
| dependency | [Fixed T_(1,0) membership](Yin_C_G0636_v1.md#statement) | Exact old quotient G, T_(1,0) components and membership, not a statement about the new full modulus. |
| dependency | [Complete factor identity](Yin_C_G0636_v1.md#argument) | Exact1+chi=W_3W_15 and removal of complete nonnegative factors; no native target is reinterpreted. |
| dependency | [Order-four old quotient class](Yin_C_G0630_v1.md#statement) | Exact order4 of yG, so U_0=y^4 is a member and U_1=T_(1,0)y^21 is a nonmember in that old ring only. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T22:25 |
| status | proved |
| reason | Adopt the entire HC1--HC8 theorem after main reading of complete C649 and isolated whole R857. The full formal iff, all CRT representatives, required6m root correction and8m product cancellation are proved with every original applicability restriction. All four m8 targets and exact old-ring cosets are retained; the actual complete-factor bridge excludes eta1 and forces B=X24 at A0=16. Both remaining full support targets are untested here; old membership is not enlarged, and no actual realization, full A0=16 exclusion, A0=14 assertion or unrestricted Task completion follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform CRT and original complement statement](#statement) | HC1--HC8: complete formal iff, unique classified B and low jet, corrected root, formal CRT feasibility, all four m=8 targets, exact old cosets and original necessary B=X^24. |
| argument | [Whole root, CRT and complete-support argument](#argument) | Every unit and6m/8m lift/error calculation, corrected eleventh power and its product cancellation, all formal representatives, exact m=8 layers/targets, symbolic T_(1,0)y^21 identity and actual factor/degree bridge. |
| dependency | [Complete homogeneous classification](Yin_C_G0643_v2.md#statement) | Sharp Q/H classification, unique auxiliary class at2m and actual homogeneous-branch dichotomy; no descent of original inputs. |
| dependency | [Formal inverse and cube precision proof](Yin_C_G0643_v2.md#argument) | Exact x,h_Q definitions, all auxiliary high bits and square/cube valuation interfaces reused at4m/8m. |
| dependency | [Original normalized domain](Yin_C_G0199_v5.md#statement) | Same original P,T,fields,divided remainders,residual,Haar/unsaturation and actual maximal q. |
| dependency | [Actual normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Original integer a_b/lambda_b/weight, S_star, root6m/error8m, old relation and lift independence. |
| dependency | [Complete complement and canonical costs](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Full B with every saturated surplus and extra factor, strict degree bound and canonical degree identities. |
| dependency | [Actual complete normalized group factorization](Yin_C_G0199_v4.md#argument) | Uniform nonnegative order multiplicities of V_0 after actual q extraction, used only with the complete m=8 H_eta factors. |
| dependency | [Normalized derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | X^(4m) divides Y' through the actual T-support odd part. |
| dependency | [Fixed T_(1,0) membership](Yin_C_G0636_v1.md#statement) | Exact old quotient G, T_(1,0) components and membership, not a statement about the new full modulus. |
| dependency | [Complete factor identity](Yin_C_G0636_v1.md#argument) | Exact1+chi=W_3W_15 and removal of complete nonnegative factors; no native target is reinterpreted. |
| dependency | [Order-four old quotient class](Yin_C_G0630_v1.md#statement) | Exact order4 of yG, so U_0=y^4 is a member and U_1=T_(1,0)y^21 is a nonmember in that old ring only. |
| review | [Independent entire uniform-CRT finding](../audits/reviews/Yin_R_G0857_v1.md#whole-uniform-crt-a16-finding) | Entire HC1--HC8 and proof, all units/root/lift/CRT cases, exact m8 target distinctions and old cosets, original complete-factor/layer/degree bridge, with prior classification, native and source scopes preserved. |

