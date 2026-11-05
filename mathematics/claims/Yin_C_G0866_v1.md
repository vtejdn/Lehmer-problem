---
author: Yin
---

# Actual degree costs for primitive Salem conjugate-monomial radicals

Human author Yin.
The arithmetic-return contributor and coordinating agent developed the positive coordinate-norm descent on 2026-11-05 as contributors.
The contributor supplied the ordinary norm calculation for external radical extensions, and the coordinator checked its torsion, field-containment and degree steps.
The integer-monomial square-norm comparison and its full orbit count are included directly below.
The complete proof has a selected independent whole assessment at the exact scope stated below.
Its extraction source is [D1's saturation inquiry](../drafts/Yin_D_G0001.md#p2-salem-monomial-radical-degree); that mutable provenance and the earlier AR calculation are not proof dependencies.

## Exact fixed inputs and their boundaries

[C165's monomial field theorem](Yin_C_G0165_v1.md#fixed-support-salem-monomial-proof), using its [complete independence proof](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof), supplies independence modulo roots of unity for one oriented conjugate from each Salem inverse pair, the signed-exponent orbit interpretation, and Q(eta^n)=Q(eta) for every positive integer n and every nontrivial integer monomial eta.
These facts hold for genuine Salem numbers of arbitrary degree at least four, including negative exponents and the real inverse pair.
Its AM16 height bounds and later complete-packet comparison are not used.
The classical independence attribution and original source-inspection limits remain at that fixed material.

[C383's actual Salem kernel](Yin_C_G0383_v1.md#salem-kernel-class-population) supplies the conjugate complex-conjugation patterns, the even-weight inversion subgroup, and the full inversion subgroup when the number of inverse pairs is even.
Its selected assessment is SELF, with the retained classical CM10 attribution and source-inspection limits.
No split-extension theorem, full symmetric top group, Frobenius density, regulator or prime bound is imported.
The elementary sign-pattern and support counts needed in the present proof are given explicitly.

[C485's full-field norm-one identity](Yin_C_G0485_v1.md#salem-relative-regulator-identity), at its [selected SELF scope](Yin_C_G0485_v1.md#decision-complete-current-self-adoption), identifies the kernel of the ordinary norm from a Salem field to its totally real trace field as the signed integer powers of the smallest Salem generator.
Only that full-ring kernel and the positivity excluding norm -1 are used, not any regulator formula or conjectural bound.
The accepted source is [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001), Lemma 2 and Proposition 3, at the retained selected statement/displayed-proof inspection:
every positive power of a Salem number retains its degree and field, and every Salem number in its full field is a positive power of the smallest one.
Its original Salem publications are not newly inspected.

The bounded local and primary-oriented reuse screen found no further result needed for the degree bound below.
No novelty, exhaustive literature coverage, favorable new p=1 coverage, or universal Mahler gap is claimed.
The explicit control below attains the degree-multiplier loss relative to its integer monomial, not the final factor-one-half bound relative to the original Salem source.
Neither a universal raw-p2 lower bound nor the real-or-circle theorem is a premise.

## Statement

All logarithms are natural.
For an algebraic integer unit z of actual degree D, count all D complex embeddings, including both members of each nonreal pair, and define

    m(z)=sum_(i=1)^D log^+|z_i|,
    M_2(z)=[D sum_(i=1)^D log^2|z_i|]^(1/2).

The second is the raw degree-weighted p=2 quantity.
All finite-place contributions vanish for units; no FM13 operator identity is assumed.

### A. External radicals, torsion and the exact degree multiplier

Let alpha>1 be a genuine Salem number of degree d=2t>=4, and let K=Q(alpha), L its splitting field and G=Gal(L/Q).
For Parts A--B suppose alpha is PRIMITIVE in its full field: it is the smallest Salem number in K in the accepted fixed-field sense.
Write m=log alpha and choose one oriented root u_i from each of its t inverse pairs.

Let b=(b_1,...,b_t) be a nonzero integer vector with gcd(|b_1|,...,|b_t|)=1, put

    eta=product_(i=1)^t u_i^(b_i),
    N=[Q(eta):Q],

and let g,s be coprime positive integers.
For any algebraic number beta satisfying

    beta^s=xi eta^g,    xi a root of unity,                    (S1)

with no containment assumption on xi or beta, define

    D=[Q(beta):Q], E=L(beta), q=[E:L], epsilon=gcd(s,2).

Then beta is a nontorsion algebraic integer unit and

    Q(eta) is contained in Q(beta),
    s divides 2q,
    q<=D/N,
    D>=sN/epsilon.                                            (S2)

Its full actual measures satisfy

    m(beta)=(gD/(sN))m(eta),
    M_2(beta)=(gD/(sN))M_2(eta)
             >=(g/epsilon)M_2(eta)
             >=(g/epsilon)M_2(alpha),                         (S3)

where M_2(alpha)=sqrt(2d)m.
In particular M_2(beta)>=M_2(alpha)/2.
For odd s there is no raw-norm loss relative to the primitive integer monomial.
If beta belongs to L, then q=1 and the reduced denominator s divides 2.
Part E gives an actual quadratic example attaining the degree-multiplier factor two relative to eta; it does not attain the final factor-one-half comparison with alpha.

The normalization covers every nonzero rational exponent vector in the conjugate-generated group modulo torsion:
collect a common denominator, extract the gcd of the numerator coordinates, and cancel any common factor of that gcd and the denominator into the torsion factor.

### B. The exact internal coordinate assertion

More generally, let Gamma in L be nonzero and satisfy

    Gamma^s=zeta product_i u_i^(A_i),
    zeta in mu(L), A_i in Z, s>=1.                            (S4)

Then Gamma is a unit and s divides 2A_i for every i.
For a nonzero exponent vector, s therefore divides 2gcd(|A_1|,...,|A_t|).

Specifically, let c_i be the conjugate complex conjugation fixing inverse pair i and flipping every other pair.
The coordinate norm

    delta_i=Gamma c_i(Gamma)

belongs to Q(u_i), satisfies delta_i^s=u_i^(2A_i), and becomes the positive real value alpha^(j_i), j_i in Z, under any chosen automorphism sending u_i to alpha.
The exponent j_i may be zero or negative.
The exact exponent identity is s j_i=2A_i.
No hypothesis on the order of mu(L) or on the parity of t is needed.

### C. The complete integer-monomial raw norm

For every nonzero integer exponent vector b, without the gcd-one requirement and without requiring alpha primitive, let eta=product_i u_i^(b_i), N=[Q(eta):Q], and r=|supp(b)|.
Then

    M_2(eta)=N m sqrt((sum_i b_i^2)/t)
             >=2sqrt(t)m=M_2(alpha).                         (S5)

This uses the actual own degree N.
The full support-orbit counts are

    N>=2^r t/r                         if r<t,
    N>=2^(t-1)                         if r=t>=3,
    N>=4                               if r=t=2.             (S6)

No generic Galois group or unproved subgroup inclusion is assumed.

### D. Nonprimitive source and ancillary odd-trace-degree observation

If the source is not primitive, write alpha=alpha_0^A with A>=1 and alpha_0 the smallest Salem number of K.
The original and primitive sources have the same degree, field and splitting field.
For the same normalized data b,g,s in the original conjugates, the conclusions retain

    s divides 2Aq,
    D>=sN/gcd(s,2A),
    M_2(beta)>=(g/gcd(s,2A))M_2(eta)
              >=M_2(alpha)/(2A)
               =sqrt(2d)m(alpha_0)/2.                         (S7)

The exact two scaling identities in S3 are unchanged.
Thus an unbounded original power A is not discarded.

When t is odd, mu(L)={1,-1}.
This ancillary observation is proved below and is not a premise of the degree bounds.
No claim about mu(L) for even t, classification of quadratic saturation, or a uniform raw bound relative to an arbitrary nonprimitive source is made.

### E. An actual primitive quartic attains the quadratic degree loss

Let v=(-1+sqrt(-3))/2, choose the root beta of X^2-vX+1 outside the unit circle, and put

    alpha=beta*conjugate(beta)>1,
    z=beta/conjugate(beta), eta=alpha*z=beta^2.

Then alpha is the primitive Salem number with minimal polynomial

    P_alpha(X)=X^4-X^3-3X^2-X+1,

and z is one of its unit-circle conjugates.
The minimal polynomials of beta and eta are, respectively,

    P_beta(X)=X^4+X^3+3X^2+X+1,
    P_eta(X)=X^4+5X^3+9X^2+5X+1.

Both have degree four, and beta belongs to the splitting field L of P_alpha, of degree eight.
Thus S1 holds with b=(1,1), g=1, s=2, xi=1 and q=1, and D=N=4 attains D=sN/2.
Writing m=log alpha, the exact measures are

    M_2(beta)=2m=M_2(eta)/2=M_2(alpha)/sqrt(2),
    m(beta)=m(alpha)=m, m(eta)=2m.                           (S8)

Here alpha>2 and m(alpha)>log(2).
This is one fixed positive-measure control, not a near-zero family or a classification of all even-denominator cases.

<a id="argument"></a>
## Complete argument

<a id="salem-monomial-orbits"></a>
### 1. The actual exponent orbit and every positive power field

The exact C165 independence input applies to the selected t roots, including the real pair and every negative exponent.
For clarity, its mechanism is the following.
If product_i u_i^(a_i) is a root of unity, choose a Galois automorphism sending u_i to alpha for one fixed i.
Every other selected inverse pair maps to a nonreal unit-circle pair, because inversion commutes with the Galois action and the selected pairs were distinct.
Taking absolute values gives alpha^(a_i)=1 and hence a_i=0.
Doing this for every i makes all a_i zero.
This is the classical argument retained and attributed in C165, not a new independence theorem.

Represent the multiplicative group generated by the original roots by Z^t using the chosen orientations.
G acts by signed permutations of exponent vectors.
Independence modulo torsion implies that h(eta)=eta exactly when h(b)=b, and hence

    N=|G.b|.                                                   (P1)

If h(eta^n)=eta^n for an integer n>=1, then h(eta)/eta is a root of unity.
The same independence forces h(b)=b.
Thus the stabilizers of eta^n and eta in the finite Galois field L coincide, and Galois correspondence gives

    Q(eta^n)=Q(eta) for every n>=1.                            (P2)

The monomial is a nontorsion algebraic integer unit because its exponent vector is nonzero and each original root and its inverse are integral.
This establishes precisely the C165 interfaces used below.

### 2. The complete raw norm and support count

Average squared logarithmic absolute values of h(eta) over all h in G.
At any one h, at most one chosen inverse pair maps to the unique real inverse pair of the Salem input.
All other factors then have modulus one.
Therefore squaring the logarithm introduces no cross terms.

For each fixed i, transitivity distributes h(u_i) uniformly among the d original roots.
Its logarithm is +m at alpha, -m at alpha^(-1), and zero at all others.
The exact average is consequently

    (1/|G|)sum_(h in G)log^2|h(eta)|
      =(2m^2/d)sum_i b_i^2
      =(m^2/t)sum_i b_i^2.                                  (P3)

Each embedding of Q(eta) occurs with the same stabilizer multiplicity in this average.
Thus multiplication by its actual degree N gives the equality in S5.
No joint-field or normal-closure degree replaces N.

Let the distinct supports of vectors in G.b be a family F.
The induced action of G on the t inverse pairs is transitive.
Since the original support is nonempty, its orbit union is all t pairs: a group element can send any chosen supported pair to any prescribed pair.
Every support has r elements, so counting that union gives

    |F|>=t/r.                                                 (P4)

The actual inversion subgroup contains every even-weight flip, as recorded in C383.
Here the elementary source pattern is c_i=1+e_i in the flip vector space F_2^t:
complex conjugation fixing pair i flips every other pair, and transitivity supplies all c_i.
Their pairwise products give the weight-two vectors e_i+e_j, which span the even-weight subgroup.
When t is even, product_i c_i is the all-one vector, so each individual e_i is also generated and the subgroup is full.

If r<t, choose an exponent vector with a particular support S in F.
Every sign pattern on S extends to an even-weight flip by choosing the sign at one unused coordinate.
Hence that one support contributes 2^r distinct exponent vectors.
They are distinct because every supported coefficient is nonzero, and different supports cannot give the same vector.
Summing over F and using P1--P4 proves N>=2^r t/r.

If r=t, the even-weight subgroup supplies 2^(t-1) distinct exponent vectors.
For t=r=2 the stronger even-t full subgroup supplies four.
These prove S6 without requiring all support subsets to occur, a full symmetric top action, or a split Galois extension.

Since sum_i b_i^2>=r, the r<t case gives

    M_2(eta)>=2^r sqrt(t/r)m>=2sqrt(t)m.

The last step is 4^(r-1)>=r, which holds at r=1 and is preserved inductively because 4r>=r+1.
For r=t>=3, the exact norm gives M_2(eta)>=2^(t-1)m>=2sqrt(t)m.
The latter holds at t=3 and its left/right ratio increases under t to t+1 by 2sqrt(t/(t+1))>1.
For t=r=2, it gives M_2(eta)>=4m>2sqrt(2)m.
The original Salem input has precisely two nonzero logarithms +/-m, so M_2(alpha)=sqrt(2d)m=2sqrt(t)m.
This completes the full proof of S5.

<a id="coordinate-norm-descent"></a>
### 3. Positive coordinate norms descend without a torsion-order bound

Let Gamma satisfy S4.
The right side and its inverse are algebraic integers, so the monic equations for Gamma and Gamma^(-1) show that both are integral.
Thus Gamma is a unit.

For every i, choose g_i in G with g_i(u_i)=alpha and set c_i=g_i^(-1)c g_i, where c is ordinary complex conjugation on L subset C.
It fixes pair i pointwise and flips every other pair.
This sign pattern determines the automorphism on L because the original roots generate L.

Let H_i=Gal(L/Q(u_i)).
Every h in H_i fixes the oriented root u_i and hence its inverse pair.
It only permutes and reorients the other pairs, so conjugating the all-other-pairs flip pattern by h leaves it unchanged.
Faithfulness on the roots gives

    h c_i=c_i h for every h in H_i.                           (P5)

Every c_i acts by inversion on every root of unity zeta in L:

    c_i(zeta)=g_i^(-1)((g_i(zeta))^(-1))=zeta^(-1).            (P6)

Define delta_i=Gamma c_i(Gamma).
Applying S4 and P6, all monomial factors except the i-th cancel, and

    delta_i^s=u_i^(2A_i).                                    (P7)

For h in H_i, P7 says that h(delta_i)/delta_i is an s-th root of unity.
At the embedding g_i both terms are positive real numbers:

    g_i(delta_i)=|g_i(Gamma)|^2>0,
    g_i h(delta_i)=|g_i h(Gamma)|^2>0.                         (P8)

The second equality uses P5 and g_i c_i=c g_i.
A positive real root of unity is one, so injectivity forces h(delta_i)=delta_i for every h in H_i.
Galois correspondence therefore gives

    delta_i in Q(u_i),
    v_i=g_i(delta_i) in K,
    v_i>0, v_i^s=alpha^(2A_i).                               (P9)

This exact descent is valid even when mu(L) contains nonreal roots of unity.

### 4. The primitive full-field kernel pays each coordinate denominator

Let F_0=Q(alpha+alpha^(-1)) and let sigma be the inverse involution of K/F_0.
These are the actual Salem trace field and quadratic involution from the accepted C485/Smy15 interface.
The unit

    nu_i=Norm_(K/F_0)(v_i)

satisfies nu_i^s=1 by P9 and Norm_(K/F_0)(alpha)=1.
Since F_0 is totally real, nu_i is either 1 or -1.
At any of its t-1 nonsplit real places, this norm is a positive squared complex modulus.
Such a place exists because t>=2, so nu_i cannot equal -1 and hence nu_i=1.

The full-ring kernel in C485 is {+/-tau^j:j in Z}, where tau is the smallest Salem number of K.
Under the primitive hypothesis tau=alpha.
Because v_i is positive in the distinguished real embedding, P9 gives

    v_i=alpha^(j_i), j_i in Z,
    s j_i=2A_i.                                               (P10)

If A_i=0, P9 and positivity give v_i=1 and j_i=0.
All coordinates therefore satisfy the divisibility in B.
This use of the kernel does not assume membership in the smaller original power-basis order, and uses no regulator estimate.

<a id="external-radical-degree"></a>
### 5. Ordinary norms pay external radicals and external torsion

Return to S1.
The preceding monomial facts make eta a nontorsion unit.
Its product with xi is also a unit, and monic power equations make beta and beta^(-1) integral.
Nontorsion follows because a torsion beta would force eta^g torsion.
Thus beta is a nontorsion algebraic integer unit.

The torsion element need not lie in L, but the equation itself gives

    xi=beta^s/eta^g in E=L(beta).

Let w be its actual finite order.
Then beta^(sw)=eta^(gw), and the power-stability identity P2 gives

    Q(eta)=Q(eta^(gw)) subset Q(beta).                        (P11)

In particular N divides D.
The minimal polynomial of beta over Q(eta) has degree D/N and can also be viewed over L, because Q(eta) is contained in L.
Its minimal polynomial over L has degree q, so

    q<=D/N.                                                   (P12)

Only this inequality is used; no general equality for compositum degrees is presumed.

Take the ordinary relative norm Gamma=Norm_(E/L)(beta).
It is a unit of L.
Multiplicativity gives

    Gamma^s=zeta eta^(gq),
    zeta=Norm_(E/L)(xi) in mu(L).                             (P13)

The norm of xi is torsion because any power annihilating xi also annihilates its norm.
This remains valid for a non-Galois extension E/L.

Apply the internal coordinate result P10 to P13 with A_i=gq b_i.
It gives s dividing 2gq b_i for every i.
Since the b_i have gcd one, integer Bezout coefficients give s dividing 2gq.
Since gcd(s,g)=1, it follows that s divides 2q, equivalently s/epsilon divides q.
Combining with P12 proves S2.
If beta is already in L, then q=1 and s divides 2.

### 6. Both measures use the full actual degree

Take any number field containing beta, eta and xi.
At every place its absolute values satisfy

    s log|beta|=g log|eta|,

since roots of unity have absolute value one.
For archimedean embeddings, averaging these squared identities over that common field counts each embedding of Q(beta) and Q(eta) with its own constant extension multiplicity.
Consequently

    (1/D)sum_(beta embeddings)log^2|beta_i|
       =(g/s)^2 (1/N)sum_(eta embeddings)log^2|eta_i|.

This proves M_2(beta)=(gD/(sN))M_2(eta).
Taking positive parts instead gives m(beta)=(gD/(sN))m(eta), because g/s>0.
Every finite-place term is zero by the already established unit status.

The degree bound S2 implies gD/(sN)>=g/epsilon.
Combining with the complete integer-monomial estimate S5 proves S3, including odd-denominator no-loss and the allowed factor-two bound.
No arbitrary radical-degree equality, normalized relative norm or torsion-representative degree is inserted.

### 7. Nonprimitive sources and the ancillary torsion remark

If alpha is nonprimitive, the accepted fixed-field theorem gives alpha=alpha_0^A, where alpha_0 is the smallest Salem number of K and A>=1.
It also gives Q(alpha)=Q(alpha_0) with the same degree.
Their splitting fields coincide:
alpha_0 is a rational polynomial in alpha and conversely alpha is a power of alpha_0, and these relations hold after every embedding.
The original inverse pairs therefore correspond to A-th powers of the primitive inverse pairs.

In P9 the coordinate norm now satisfies v_i^s=alpha_0^(2A A_i).
The full-field kernel and positivity give v_i=alpha_0^(j_i), hence s j_i=2A A_i.
For the external norm P13, this yields s dividing 2Agq and, because gcd(s,g)=1, s dividing 2Aq.
Thus s/gcd(s,2A) divides q.
The field inclusion P11, degree inequality P12 and both exact measure identities are unchanged.
Combining them with the original integer-monomial bound S5 gives all inequalities in S7.
An unbounded original power A can therefore permit the old reduction to alpha_0; it is not treated as a uniform saving on primitive inputs.

Finally suppose t is odd.
The automorphisms c_i commute because all are inversion patterns on the same inverse pairs.
Their product fixes every original root, since each pair is flipped t-1 times, so product_i c_i is identity.
Each c_i inverts every root of unity by P6.
As t is odd, the identity product consequently acts by inversion on every root of unity, forcing zeta=zeta^(-1).
Thus mu(L)={1,-1}.
This is independent of, and unnecessary for, the positivity descent and external norm argument above.
No assertion about even-t torsion is used.

<a id="quadratic-saturation-control"></a>
### 8. Exact quadratic saturation in a primitive quartic

The coordinating agent supplied this control, and the arithmetic-return contributor checked all polynomial, field, primitive-generator and norm calculations below.
The number v is a primitive cube root of unity, with v+conjugate(v)=-1 and v*conjugate(v)=1.
The discriminant v^2-4 of X^2-vX+1 has norm

    Norm_(Q(v)/Q)(v^2-4)=21.

It cannot be a square in Q(v), because the norm of a square would be a rational square.
Hence the chosen beta has degree four, and the trace substitution gives its displayed monic minimal polynomial P_beta.
The trace v is nonreal, so neither root of that quadratic is real or on the unit circle; their product is one, and exactly one has modulus greater than one.
Choose that root as beta.

Set alpha=|beta|^2>1 and z=beta/conjugate(beta), and write A=alpha+alpha^(-1), Z=z+z^(-1).
Direct expansion gives

    A+Z=(beta+beta^(-1))
          *(conjugate(beta)+conjugate(beta)^(-1))=1,
    AZ=beta^2+beta^(-2)+conjugate(beta)^2
                            +conjugate(beta)^(-2)=-5.

Thus A,Z are the roots of Y^2-Y-5.
Since A>2,

    A=(1+sqrt(21))/2>2,
    Z=(1-sqrt(21))/2 in(-2,2).

In particular z is nonreal and lies on the unit circle.
The discriminant A^2-4=A+1 is negative at the other real embedding of Q(sqrt(21)), because Z+1<0.
It is therefore nonsquare in that totally real field.
It follows that alpha has degree four and minimal polynomial P_alpha(X)=X^2[(X+X^(-1))^2-(X+X^(-1))-5].
Its roots are alpha,alpha^(-1),z,z^(-1), so it is a genuine Salem number with trace field F=Q(sqrt(21)).
Since A=(1+sqrt(21))/2>5/2=2+1/2 and x+x^(-1) is strictly increasing for x>1, alpha>2 and m(alpha)>log(2).

To prove that alpha is primitive, suppose there were a smaller Salem tau in K=Q(alpha).
The accepted fixed-field theorem and compatible inverse involution imply that h=tau+tau^(-1) belongs to F, with h in(2,A) and its other embedding h' in(-2,2).
Write h=(a+b sqrt(21))/2, where a=Tr_(F/Q)(h) is an integer and b is initially rational.
The discriminant a^2-4Norm_(F/Q)(h)=21b^2 is an integer.
Writing b in lowest terms shows that its denominator squared divides the squarefree integer 21, hence b is an integer.
Moreover

    0<h-h'=b sqrt(21)<A+2<5,

so b=1.
The inequality h'>-2 gives a>sqrt(21)-4>0 and hence a>=1, whereas h<A gives a<1.
This contradiction proves primitiveness, with no finite enumeration or numerical root estimate.

For eta=beta^2, its trace over Q(v) is v^2-2=-v-3, which generates Q(v).
The discriminant of its quadratic is

    (v^2-2)^2-4=v^2(v^2-4),

still nonsquare in Q(v) because v^2 is a square there.
Therefore eta also has degree four.
Its two trace conjugates have sum -5 and product 7, giving the displayed P_eta by the same reciprocal trace substitution.
Since eta belongs to Q(beta) and both degrees are four, their fields agree.

Let E=Q(beta,conjugate(beta)).
It contains Q(v), and both beta and conjugate(beta) satisfy quadratics over Q(v), so [E:Q]<=8.
It contains every root alpha,alpha^(-1),z,z^(-1), hence contains the Salem splitting field L.
For the actual quartic alpha, C383's even-t full inversion kernel has order four and the transitive action on its two pairs has order two.
Thus [L:Q]=8, so E=L and beta belongs to L.
This proves all asserted degree equalities without presuming that an arbitrary square root stays in the splitting field.

Finally |beta|=sqrt(alpha), so its four logarithmic absolute values are +m/2,+m/2,-m/2,-m/2.
Those of eta are +m,+m,-m,-m, and those of alpha are +m,-m,0,0.
The definitions of total measure and raw M_2 give S8 exactly.
The degree loss relative to eta is attained, while the final comparison with alpha has factor 1/sqrt(2), not 1/2.

## Consequence and review limits

For primitive sources the full rational radical class in S1 cannot supply M_2(beta)<=C m(alpha) with one fixed C at unbounded original degree:
S3 gives M_2(beta)/m(alpha)>=sqrt(2d)/2.
This conclusion includes arbitrary external extensions and arbitrary torsion factors.
It is a cost restriction on this specific construction class, not a proof of the unrestricted [G0001 total-Mahler gap](../tasks/Yin_T_G0001_v1.md#contract).
The even-denominator degree-multiplier factor two is attained by Part E, but its full class is not classified and sharpness of the final M_2(alpha)/2 bound is not asserted.
The exact total-measure scaling supplies no new favorable p=1 coverage claim here.

No numerical experiment, polynomial enumeration or native computation is used.
The contributor checks of the full proof, field identities, source conditions and ordinary norm costs are distinct from the selected independent whole finding.
That finding preserves the exact accepted-source and prior-review limits recorded above.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T22:22 |
| status | proved |
| reason | Adopt entire A--E and complete Sections 1--8 after independent R1088. Positive coordinate norms force the internal denominator cost; an ordinary relative norm pays arbitrary external torsion and radical extensions at actual degrees. The complete integer-monomial bound and nonprimitive power cost are retained, and a primitive quartic attains the quadratic degree multiplier without attaining the final half-alpha bound. Prior SELF/unknown relationships and source-proof limits remain unchanged. This excludes the specified raw-p2 compression mechanism at unbounded primitive Salem degree, not the unrestricted G0001 gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--E and S1--S8, arbitrary external torsion and radicals, every support/sign, actual degrees, odd/even denominators, primitive and nonprimitive boundaries and exact quartic control. |
| argument | [Complete proof](#argument) | Complete Sections 1--8, signed-exponent orbit, full support counts, positive coordinate descent, full-field kernel interface, ordinary norm, both full-degree measure scalings and symbolic control. |
| dependency | [Integer monomial fields](Yin_C_G0165_v1.md#fixed-support-salem-monomial-proof) | Exact signed-exponent stabilizer and every-positive-power field equality at actual own degree; no AM16 or later packet comparison. |
| dependency | [Independence modulo torsion](Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | One oriented root from every Salem inverse pair, arbitrary integer signs and all genuine Salem degrees; the necessary local proof is also written directly here. |
| dependency | [Actual sign kernel](Yin_C_G0383_v1.md#salem-kernel-class-population) | Conjugate complex-conjugation patterns, even flips and full kernel for even t, at retained SELF/source scope; no full symmetric top group, splitting theorem or prime bound. |
| dependency | [Full-field norm-one kernel](Yin_C_G0485_v1.md#salem-relative-regulator-identity) | Only the actual trace signature, inverse involution, norm-minus-one exclusion and signed powers of the smallest Salem generator, preserving the ancestor's SELF scope. |
| support | [Smy15 fixed-field source](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Accepted Lemma 2/Proposition 3, positive-power field/degree and primitive generator at retained statement/displayed-proof inspection; no new original-Salem proof audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v1.md#whole-salem-radical-degree-finding) | Entire A--E, complete argument and exact control, all accepted interfaces, unchanged ancestor relationships and all remaining unrestricted and sharpness limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
