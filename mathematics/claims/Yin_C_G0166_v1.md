---
author: Yin
---
# Integral positive Mobius contractions of Salem numbers have a uniform source-height floor

Date: 2026-10-18T12:24.
Human author Yin.
Root proposed the varying-function question and supplied the content, root-geometry and exceptional-graph proof sketch.
The loglog_cyclic_review author checks the exact local and global interfaces and develops the complete argument below.
Root and this author are proof contributors; neither is an independent reviewer of this candidate.
No polynomial enumeration, prime scan, numerical constant evaluation or mathematical program is used.
This is a complete author argument prepared for separate whole review; no independent acceptance is asserted.

<a id="salem-mobius-reuse"></a>
## Reuse, source scope and target boundary

The [Bil97 fixed-function input](../audits/literature/Bil97/Yin_U001.md#fixed-rational-function-height-gap) only supplies a constant for each FIXED rational graph.
Its [Theorem5.1 complement](../audits/literature/Bil97/Yin_U001.md#torus-bogomolov-complement) and complete graph application are accepted at the source unit's explicit statement/applicability scope, without a new audit of Bilu's proof or the original Zhang/Bombieri--Zannier arguments.
This draft uses it only for the single exceptional graph F(X)=(3X+1)/(X+3), after an elementary argument covers all other coefficient pairs uniformly.
The family a,b otherwise varies freely subject to the exact hypotheses below.

The other analytic input is [C147v5](Yin_C_G0147_v5.md#statement), the accepted complete ORIGINAL cyclic norm bound and capped inverse H_5, used solely at n=1 for the original input alpha.
No angular bound is substituted for log|P(1)|/d.
The [Con26d monic rational-factor interface](../audits/literature/Con26d/Yin_U001.md#con26d-u001) supplies the ordinary integer minimal-polynomial/Gauss convention when output integrality is used; its Eisenstein criterion is not needed here.
All actual polynomial-content and valuation estimates are proved directly below.

The bounded local screen read the exact fixed-field [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001) and [L385 relative-unit account](../ledger/Yin_L_G0385_v1.md#actual-order-relative-unit-generator), besides the preceding Bil97, C147 and Con26d interfaces.
Smy15 Lemma2/Proposition3 were reread in the retained primary printed/PDF pages2--4.
They imply that alpha and any integral Salem output here are powers of a smallest Salem number in their common field.
They do not supply a uniform lower height as that field, degree and power exponents vary; no such extra conclusion is borrowed.
The exact rational transformation and its whole coefficient content require the present separate calculation.
There is nevertheless an immediate OLD exclusion: if alpha is already the smallest, or primitive, Salem generator of its field, the smaller same-field Salem output beta is impossible.
Every admitted contraction therefore starts from a nonprimitive power of that field generator.
The new uniform source-height estimate is an additional quantitative restriction, not new coverage of a primitive Salem gap frontier.

A bounded primary-oriented online search used Salem numbers with linear-fractional or Mobius transformations and integer Blaschke maps.
The returned modular/golden-mean note and general survey leads supplied no inspected theorem giving this moving-a,b uniform height floor.
The useful fixed-field survey lead was resolved through its already retained exact Smy15 unit rather than a new acquisition.
This is not an exhaustive priority search, a novelty claim or a classification of all rational transformations.

The target is a uniform ABSOLUTE HEIGHT floor for the SOURCE alpha when the specified contracted output is integral.
It is not a uniform positive output measure theorem for all varying coefficients.
Large-height sources contracting to smaller Salem outputs remain outside the exclusion proved here.
The argument is restricted to the positive symmetric Mobius maps stated below, not arbitrary PGL2 maps or arbitrary non-Salem algebraic units.

<a id="salem-mobius-statement"></a>
## Statement

Let alpha>1 be a genuine Salem number with monic irreducible reciprocal minimal polynomial P of even degree d>=4.
Write m(alpha)=log alpha=d h_abs(alpha).
For coprime positive integers a>b>=1, put

    F_(a,b)(X)=(aX+b)/(bX+a),
    beta=F_(a,b)(alpha), S=a+b, Delta=a^2-b^2.

Assume beta is an algebraic integer.
Then beta is a genuine Salem unit of the SAME degree and field as alpha, with

    1<beta<alpha,
    Q(beta)=Q(alpha),
    h_abs(beta)<h_abs(alpha).                            (1)

By the accepted fixed-field Salem structure there is a primitive Salem generator tau_0 of their common field and integers j>k>=1 with alpha=tau_0^j and beta=tau_0^k.
Thus no primitive Salem alpha admits such an integral positive contraction; that qualitative exclusion is already classical.

There is an absolute constant h_0>0, independent of alpha,d,a,b, such that EVERY such integral contraction satisfies

    h_abs(alpha)>h_0,
    m(alpha)>d h_0.                                      (2)

One exact choice is

    delta=(1/4)log(45/16),
    h_0=min{H_5(delta), eta_(3,1)/2},                    (3)

where H_5 is the accepted C147v5 capped threshold and eta_(3,1)>0 is the Bil97 Theorem5.1 graph-height infimum for the fixed graph Y=(3X+1)/(X+3) after removing its contained torsion subvarieties.
The source graph account applies to every nontorsion first coordinate.
No effective numerical value of eta_(3,1) or numerical inversion of H_5 is asserted.

For all (a,b)!=(3,1), a stronger explicit intermediate conclusion is

    log|P(1)|/d>delta.                                  (4)

For opposite parity one may replace delta in (4) by (1/4)log(9/2).
The constant (3) excludes an integral contraction anywhere in this family along a source sequence with h_abs(alpha) tending to zero.
It does not by itself exclude small total output measure obtained from sources whose heights stay large.

<a id="argument"></a>
## Complete argument

<a id="salem-mobius-proof"></a>
### 1. Exact output roots, field and content

The determinant Delta is positive.
Every original root alpha_i avoids the pole -a/b: the two real roots are positive and all other roots have modulus1, whereas -a/b<-1.
The inverse identity is

    alpha=(a beta-b)/(a-b beta),
    a-b beta=Delta/(b alpha+a)!=0.

Thus Q(beta)=Q(alpha), independently of the output's integrality, and its degree is d.
The real distinguished values satisfy

    beta-1=(a-b)(alpha-1)/(b alpha+a)>0,
    alpha-beta=b(alpha^2-1)/(b alpha+a)>0.

For |u|=1 one has |au+b|=|bu+a|, so its image has modulus1.
The map commutes with inversion, and its real coefficients and nonzero determinant prevent a nonreal input from having real image.
It therefore sends the original real reciprocal pair to beta,beta^(-1), and all d-2 nonreal circle roots to distinct nonreal circle roots.
These are exactly all conjugates because the original field is preserved.
Once beta is integral, this is a genuine Salem number of degree d.

Put

    f(X,Y)=Y^d P(X/Y)=product_i(X-alpha_i Y),
    Q(y)=f(ay-b,a-by),
    L=f(a,-b)=product_i(a+b alpha_i).                   (5)

This is an integer polynomial of degree d and leading coefficient L.
The positive real pair contributes a positive factor and each circle pair contributes |a+b u|^2>0, so L>0.
The reciprocal identity f(X,Y)=f(Y,X) gives Q(0)=f(-b,a)=L.
The factorization in (5) also shows directly that Q's roots are the displayed beta-conjugates.
If beta is integral, its monic minimal polynomial P_beta belongs to Z[y], has degree d, and

    Q(y)=L P_beta(y).

Consequently the positive coefficient content c of Q is EXACTLY L: every coefficient is divisible by L and the leading coefficient is L.
Moreover P_beta(0)=1, so beta is a unit.
Its unique expanding conjugate gives (1)'s strict height inequality because both degrees equal d.
The argument does not confuse an integral rational polynomial multiple with the primitive monic output polynomial.
The accepted Smy15 fixed-field theorem now gives alpha=tau_0^j and beta=tau_0^k for a smallest Salem tau_0 in this field.
Their strict order gives j>k>=1, proving the stated classical primitive-input exclusion.

### 2. All primes in the content and the precise factor2 cost

The original binary form f is primitive, since its X^d coefficient is1.
If a rational prime ell does not divide Delta, the linear substitution

    (X,Y) maps to (aX-bY,aY-bX)

is invertible over F_ell.
It cannot turn the nonzero reduction of f into the zero polynomial.
Evaluating a homogeneous degree-d polynomial at (y,1) retains its complete coefficient list, so ell cannot divide the content c of Q.
Thus every prime dividing c divides Delta.

For an odd ell dividing a-b, coprimality gives ell not dividing a+b.
Evaluate

    Q(-1)=f(-S,S)=S^d P(-1),
    Q(1)=f(a-b,a-b)=(a-b)^d P(1).                     (6)

It follows that v_ell(c)<=v_ell(P(-1)) in the a-b case.
For an odd ell dividing a+b, coprimality instead gives ell not dividing a-b, so v_ell(c)<=v_ell(P(1)).
An odd prime cannot divide both a-b and a+b.
The values P(1),P(-1) are nonzero integers, since neither1 nor-1 is a Salem conjugate.
These estimates cover every odd prime in the content, including arbitrary prime powers in a plus or minus b.

If a,b have opposite parity then Delta is odd, so2 does not divide c and

    c divides |P(1)P(-1)|,
    c<=|P(1)P(-1)|.                                   (7)

If both are odd, coprimality implies gcd(a-b,a+b)=2 and hence min{v_2(a-b),v_2(a+b)}=1.
Use the evaluation in (6) whose scalar factor has that valuation1.
It gives either v_2(c)<=d+v_2(P(1)) or v_2(c)<=d+v_2(P(-1)), according to which scalar has minimal valuation.
In either case

    c divides 2^d |P(1)P(-1)|,
    c<=2^d |P(1)P(-1)|.                              (8)

No claim that c is supported only at primes dividing P(1) or P(-1) without the extra2 factor is made in the odd-odd case.
No local squarefreeness or unramifiedness is used.

### 3. Full circle and real-pair comparison

For every circle root u,

    |a+b u|^2-(S^2/4)|1+u|^2
       =((a-b)^2/4)|1-u|^2>=0.                       (9)

Hence |a+b u|>=(S/2)|1+u|.
The real pair obeys

    (a+b alpha)(a+b/alpha)
       -ab(1+alpha)(1+1/alpha)=(a-b)^2>0.            (10)

Also P(-1)>0: its real-pair factor is positive and its other paired factors are |1+u|^2>0.
Multiplying (9) over ALL d-2 circle roots and (10) over the one real pair therefore gives

    L>ab(S/2)^(d-2) P(-1).                           (11)

All original roots occur with their actual multiplicities, and strictness already follows from (10).
There is no angular averaging, omitted real factor or use of the smaller output field in this inequality.

### 4. A positive norm density except for one fixed coefficient pair

Let kappa=0 for opposite parity and kappa=1 for both odd.
Using c=L, equations(7)--(8) and (11), and canceling the positive P(-1), gives

    |P(1)|>ab(S/2)^(d-2)/2^(kappa d).

Consequently

    log|P(1)|/d
       >log(S/2)-kappa log2+(1/d)log(4ab/S^2).       (12)

Because a>b, the last logarithm is negative.
Since d>=4, replacing 1/d by1/4 makes that term no larger.
Also ab>=S-1 for positive integers of fixed sum S.
It follows that

    log|P(1)|/d
       >(1/4)log[S^2(S-1)/(4*2^(4kappa))].           (13)

For opposite parity S is odd and S>=3, so (13) is at least (1/4)log(9/2)>0.
For both odd, the only S=4 possibility with a>b>=1 is (a,b)=(3,1).
All other odd-odd pairs have S>=6, and (13) is then at least (1/4)log(45/16)>0.
The product S^2(S-1) is increasing for integers S>=2, so these minima are exact lower comparisons; no numerical optimization or prime scan is involved.
Since9/2>45/16, this proves (4) uniformly over every nonexceptional pair.

### 5. The original n=1 norm and the fixed exceptional graph

For the ORIGINAL alpha, the complete cyclic norm at n=1 is

    C_1=abs Norm_(Q(alpha)/Q)(alpha-1)=|P(1)|.

Its parameter in C147v5 is h=m(alpha)/d=h_abs(alpha).
The supplied density (4), and the actual capped inverse statement in that Claim, therefore give

    h_abs(alpha)>H_5(delta)                          (14)

for every nonexceptional pair, with all cap and large-height cases included.
The inequality is a direct application at n=1, not a replacement of a logarithmic norm by angular moments.

For the exceptional pair, fix F(X)=(3X+1)/(X+3).
It is nonzero and nonconstant, with nonzero finite zero -1/3 and pole -3, so it is not +/-X^k for any integer k.
The Bil97 graph statement therefore applies to every nontorsion alpha at which F is defined and nonzero.
The graph complement is nonempty, for instance the first coordinate2 is nontorsion and F(2)=7/5, so its infimum eta_(3,1) is a fixed positive number.
The original alpha here is nontorsion and its beta is defined and nonzero.
By the accepted graph application and its full projective-height inequality,

    eta_(3,1)<=H_2(alpha,beta)
                <=h_abs(alpha)+h_abs(beta)
                 <2h_abs(alpha).

Thus h_abs(alpha)>eta_(3,1)/2.
This use needs independence of the SINGLE first coordinate, meaning nontorsion; it does not assume the pair alpha,beta is multiplicatively independent.
Indeed, under the current hypotheses, the accepted fixed-field Salem theorem makes the pair alpha,beta multiplicatively dependent.
Combining this exceptional bound with (14) proves (2)--(3).

### 6. A reused exact nonempty control

The hypothesis is not asserted only for a possibly empty class.
Let tau be the already accepted degree-four Salem root of R(X)=X^4-X^3-X^2-X+1 from [L169's exact input](../ledger/Yin_L_G0169_v1.md#quartic-neutral-descent).
Only that algebraically proved input is used, not the later return-core computation.
The polynomial identity

    (X-1)R(X)=X^5-2X^4+2X-1

gives tau(tau^4+2)=2tau^4+1.
Thus alpha=tau^4 and beta=tau satisfy beta=F_(2,1)(alpha), with both algebraic integer Salem units of degree4 by the accepted Smy15 power statement.
This is a direct reuse of a fixed known input, not a new polynomial search or numerical test.
It gives no near-one sequence or degree-uniform output behavior.

## Exact scope and author check

All admissible maps are genuine positive contractions at the real Salem root, and every integral output is a same-field, same-degree Salem unit.
The integrality premise is decisive: without it c need not equal L and the content comparison does not establish the asserted uniform source-height floor.
The statement is uniform over all coprime positive a>b>=1, but does not extend to arbitrary PGL2 coefficients, arbitrary algebraic units or degree2 reciprocal numbers.

The conclusion excludes this integral output whenever the SOURCE absolute height tends to zero, including a hypothetical Salem total-measure-to-zero sequence.
It does not prove a uniform positive total measure for beta across all admitted pairs: the contraction ratio can vary and the argument imposes a source-height condition.
In particular large-height alpha with smaller beta is not ruled out, and no existence or impossibility of that remaining regime is asserted.
The known same-field power structure does not erase this distinction.
An attempted large-power-source to primitive-output construction already presupposes or encodes that smaller field generator; this theorem supplies no automatic new small Salem family.
The uniform source-height floor is additional quantitative control on a class whose primitive-source case is already excluded by Smy15.

The author checked the inverse denominator and field degree, all real/circle images, primitive output factor and exact positive content, every odd-prime allocation, the2-adic minimal-valuation case, signs of P(plus or minus1), the full root-product inequality and its strict real-pair factor, the negative logarithm direction using d>=4, all smallest sums and the unique exception, the C147 original n1 normalization, and the Bil97 graph complement without a false pair-independence assumption.
This complete author argument remains ready for separate whole review; no independent review or fixed acceptance is claimed.

## Current assessment
[Selected decision](#decision-current-actual-order-relative-unit-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T12:30 |
| status | open |
| reason | Register the complete uniform source-height floor for integral positive symmetric Möbius contractions of genuine Salem inputs, including exact output field/unit geometry, full polynomial content, parity-dependent norm density, the single fixed-graph exception and a reused nonempty control. Root and the author contribute; whole noncontributor review is required. The classical primitive-source exclusion and the absence of a uniform varying-output measure conclusion are explicit; no novelty or unrestricted-gap claim is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete contraction statement](#statement) | Every genuine Salem source d>=4 and coprime positive a>b>=1 with integral output; same-degree Salem unit and contraction, classical primitive-power classification, uniform source absolute-height floor, exact nonexception norm density and all source/output boundaries. |
| argument | [Complete content and geometry proof](#argument) | Sections1--6 and scope/author checks; invertible Möbius field identity, c=L, every odd/2-adic content valuation, full real/circle product and sign, negative-log comparison and both minimum sums, capped original n1 inverse, the (3,1) graph without joint-pair independence, and exact reused nonempty input. |
| dependency | [Complete cyclic norm inverse](Yin_C_G0147_v5.md#statement) | Only the ORIGINAL n=1 norm abs P(1) and its actual density, with the accepted capped H_5 implication; no angular substitute or numerical inversion. |
| dependency | [Fixed rational graph height input](../audits/literature/Bil97/Yin_U001.md#bil97-u001) | The accepted Theorem5.1 graph complement and full tuple-height application for the SINGLE fixed F=(3X+1)/(X+3); nontorsion of its first coordinate suffices. Source-original proof-inspection limits remain unchanged. |
| dependency | [Monic integer factor convention](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Ordinary monic minimal-polynomial/Gauss interface when beta is integral; no Eisenstein criterion or uninspected local irreducibility theorem is used. |
| dependency | [Classical fixed Salem field structure](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Same-field Salem numbers are positive powers of the smallest generator, excluding primitive sources, and powers retain Salem degree in the nonempty control; no degree-uniform fundamental-unit or height bound is inferred. |
| dependency | [Existing exact quartic input](../ledger/Yin_L_G0169_v1.md#quartic-neutral-descent) | Only the algebraic degree-four Salem input R=X^4-X^3-X^2-X+1; the relation beta=F_(2,1)(beta^4) is proved here, and no return-core computation is used. |
| support | [Earlier actual-order relative-unit account](../ledger/Yin_L_G0385_v1.md#actual-order-relative-unit-generator) | Reuse comparison for primitive Salem power structure and order distinctions; the present full-field integral contraction does not assume membership in the original power-basis order. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T12:43 |
| status | proved |
| reason | Adopt the complete uniform source-height floor after R393 whole noncontributor review, retaining the separately independently checked R537 upstream application and its disclosed authorship. All coefficient pairs, content valuations, original-root norm costs, the single fixed-graph exception, classical primitive-source exclusion and exact nonempty control are covered. This is a source-height obstruction, not a varying-output gap or resolution of G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete contraction statement](#statement) | Every genuine Salem source d>=4 and coprime positive a>b>=1 with integral output; same-degree Salem unit and contraction, classical primitive-power classification, uniform source absolute-height floor, exact nonexception norm density and all source/output boundaries. |
| argument | [Complete content and geometry proof](#argument) | Sections1--6 and scope/author checks; invertible M枚bius field identity, c=L, every odd/2-adic content valuation, full real/circle product and sign, negative-log comparison and both minimum sums, capped original n1 inverse, the (3,1) graph without joint-pair independence, and exact reused nonempty input. |
| dependency | [Complete cyclic norm inverse](Yin_C_G0147_v5.md#statement) | Only the ORIGINAL n=1 norm abs P(1) and its actual density, with the accepted capped H_5 implication; no angular substitute or numerical inversion. |
| dependency | [Fixed rational graph height input](../audits/literature/Bil97/Yin_U001.md#bil97-u001) | The accepted Theorem5.1 graph complement and full tuple-height application for the SINGLE fixed F=(3X+1)/(X+3); nontorsion of its first coordinate suffices. Source-original proof-inspection limits remain unchanged. |
| dependency | [Monic integer factor convention](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Ordinary monic minimal-polynomial/Gauss interface when beta is integral; no Eisenstein criterion or uninspected local irreducibility theorem is used. |
| dependency | [Classical fixed Salem field structure](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Same-field Salem numbers are positive powers of the smallest generator, excluding primitive sources, and powers retain Salem degree in the nonempty control; no degree-uniform fundamental-unit or height bound is inferred. |
| dependency | [Existing exact quartic input](../ledger/Yin_L_G0169_v1.md#quartic-neutral-descent) | Only the algebraic degree-four Salem input R=X^4-X^3-X^2-X+1; the relation beta=F_(2,1)(beta^4) is proved here, and no return-core computation is used. |
| support | [Earlier actual-order relative-unit account](../ledger/Yin_L_G0385_v1.md#actual-order-relative-unit-generator) | Reuse comparison for primitive Salem power structure and order distinctions; the present full-field integral contraction does not assume membership in the original power-basis order. |
| review | [Whole contraction finding](../audits/reviews/Yin_R_G0393_v1.md#integral-contraction-whole-independent-finding) | Complete statement, all six argument sections and every declared dependency/support; upstream Bil97 authorship and independently accepted R537 source/application evidence are explicitly separated. |


### Decision current-quartic-input-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:50 |
| status | proved |
| reason | Select the complete C396 proof home for exactly the originally used L169 algebraic degree-four Salem input, with no return-core computation imported into this consumer. Preserve the statement, argument, status, every other relation and all existing review scopes. The actual old input reading remains fixed; this proof-home decision does not claim that the earlier reviewer inspected the later C396 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Every genuine Salem source d>=4 and coprime positive a>b>=1 with integral output; same-degree Salem unit and contraction, classical primitive-power classification, uniform source absolute-height floor, exact nonexception norm density and all source/output boundaries. |
| argument | [Exact retained argument](#argument) | Sections1--6 and scope/author checks; invertible M枚bius field identity, c=L, every odd/2-adic content valuation, full real/circle product and sign, negative-log comparison and both minimum sums, capped original n1 inverse, the (3,1) graph without joint-pair independence, and exact reused nonempty input. |
| dependency | [Exact retained dependency](Yin_C_G0147_v5.md#statement) | Only the ORIGINAL n=1 norm abs P(1) and its actual density, with the accepted capped H_5 implication; no angular substitute or numerical inversion. |
| dependency | [Exact retained dependency](../audits/literature/Bil97/Yin_U001.md#bil97-u001) | The accepted Theorem5.1 graph complement and full tuple-height application for the SINGLE fixed F=(3X+1)/(X+3); nontorsion of its first coordinate suffices. Source-original proof-inspection limits remain unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Ordinary monic minimal-polynomial/Gauss interface when beta is integral; no Eisenstein criterion or uninspected local irreducibility theorem is used. |
| dependency | [Exact retained dependency](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Same-field Salem numbers are positive powers of the smallest generator, excluding primitive sources, and powers retain Salem degree in the nonempty control; no degree-uniform fundamental-unit or height bound is inferred. |
| dependency | [Exact retained dependency](Yin_C_G0396_v1.md#quartic-neutral-descent) | Only the algebraic degree-four Salem input R=X^4-X^3-X^2-X+1; the relation beta=F_(2,1)(beta^4) is proved here, and no return-core computation is used. |
| support | [Exact retained support](../ledger/Yin_L_G0385_v1.md#actual-order-relative-unit-generator) | Reuse comparison for primitive Salem power structure and order distinctions; the present full-field integral contraction does not assume membership in the original power-basis order. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0393_v1.md#integral-contraction-whole-independent-finding) | Complete statement, all six argument sections and every declared dependency/support; upstream Bil97 authorship and independently accepted R537 source/application evidence are explicitly separated. |

### Decision current-actual-order-relative-unit-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:10 |
| status | proved |
| reason | Select the complete C454 proof home for exactly the earlier L385 actual-order relative-unit comparison; preserve every mathematical input scope, assessment field and other tuple. This current home maintenance does not claim that the earlier full C166 reviewer read the later C454 home. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every genuine Salem source d>=4 and coprime positive a>b>=1 with integral output; same-degree Salem unit and contraction, classical primitive-power classification, uniform source absolute-height floor, exact nonexception norm density and all source/output boundaries. |
| argument | [Exact argument](#argument) | Sections1--6 and scope/author checks; invertible M枚bius field identity, c=L, every odd/2-adic content valuation, full real/circle product and sign, negative-log comparison and both minimum sums, capped original n1 inverse, the (3,1) graph without joint-pair independence, and exact reused nonempty input. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | Only the ORIGINAL n=1 norm abs P(1) and its actual density, with the accepted capped H_5 implication; no angular substitute or numerical inversion. |
| dependency | [Exact dependency](../audits/literature/Bil97/Yin_U001.md#bil97-u001) | The accepted Theorem5.1 graph complement and full tuple-height application for the SINGLE fixed F=(3X+1)/(X+3); nontorsion of its first coordinate suffices. Source-original proof-inspection limits remain unchanged. |
| dependency | [Exact dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Ordinary monic minimal-polynomial/Gauss interface when beta is integral; no Eisenstein criterion or uninspected local irreducibility theorem is used. |
| dependency | [Exact dependency](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Same-field Salem numbers are positive powers of the smallest generator, excluding primitive sources, and powers retain Salem degree in the nonempty control; no degree-uniform fundamental-unit or height bound is inferred. |
| dependency | [Exact dependency](Yin_C_G0396_v1.md#quartic-neutral-descent) | Only the algebraic degree-four Salem input R=X^4-X^3-X^2-X+1; the relation beta=F_(2,1)(beta^4) is proved here, and no return-core computation is used. |
| support | [Exact support](Yin_C_G0454_v1.md#actual-order-relative-unit-generator) | Reuse comparison for primitive Salem power structure and order distinctions; the present full-field integral contraction does not assume membership in the original power-basis order. |
| review | [Exact review](../audits/reviews/Yin_R_G0393_v1.md#integral-contraction-whole-independent-finding) | Complete statement, all six argument sections and every declared dependency/support; upstream Bil97 authorship and independently accepted R537 source/application evidence are explicitly separated. |

