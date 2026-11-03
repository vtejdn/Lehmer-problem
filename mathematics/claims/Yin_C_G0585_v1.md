---
author: Yin
---

# Complete actual trace positivity and two rational doubling boundary controls

The complete original mathematical argument is retained from [L442](../ledger/Yin_L_G0442_v1.md#actual-trace-positivity-interlacing-screen).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
All three original author stages2026-10-20T10:34,12:30 and14:38 and their distinct root/draft_inventory_later/draft_comparison_cleanup contributions are retained. The actual MS05/Schinzel passage inspection remains at its old depth; no original proof or source rereview is claimed.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Part A uses an ACTUAL monic irreducible reciprocal nontorsion integer-unit P of degree d=2r and actual totally real trace field F=Q(delta), trace polynomial T, a=rem_T T(C2)(delta)/2.
If a is totally positive, A=rem_T T(C2)/2 need not itself give a positive-residue quotient: A/T has residues a_i/T'(delta_i), with alternating T' signs.
The CORRECT B=rem_T(A T') has
    B/T=sum_i a_i/(X-delta_i),deg B=r-1,lc(B)=K=Tr_F(a)>0.
It interlaces T with actual leading K; dividing K away changes the scalar cost.
Under actual f=0, Norm_F(a)>=2^ceil(r/5) and K>=r2^(1/5).
All actual original embedding multiplicities, output identities and nonzero-resultant exclusions in the complete argument are retained.
The genuine integer Salem quartic P=z^4-2z^3+z²-2z+1 has actual a=3 totally positive and expanding root<2, but fails f=0.
The accepted totally-positive Schinzel bound for sqrt(a), with the fully paid upper coefficient height H, gives only m>=log(2phi/H)/2, where phi=(1+sqrt5)/2, negative for H>=4; no free original gap follows.

Part B is a RATIONAL boundary class, not an integer-unit family.
For EVERY integer j>=0 put n=2^(2j+5),q=1/n,
    T_n=X²-(3/2)X-1-q,
    P_n=z^4-(3/2)z³+(1-q)z²-(3/2)z+1,
    delta_±=(3±sqrt(25+16q))/4.
Then T_n and P_n are irreducible over Q, F_n has degree2 and all trace conjugates are real; exactly one original positive reciprocal pair expands/contracts and the other pair is on the circle.
The ACTUAL a_n=T_n(C2(delta))/2 is totally positive.
The full archimedean Mahler measure is positive and <sqrt2/(5n), tending to0, while
    Norm_F(a_n)=(q/4)(3/2-q)(75/8+(15/2)q-q²)<4/n,
    Res(P_n,P_n(z²))=16 Norm_F(a_n)^2<256/n² ->0.
The actual a_n is not integral.
The primitive integer polynomial nP_n has leading n and absolute logarithmic height(log n+m_arch(P_n))/4 ->infinity.
All DP1--DP8 bounds, actual original four roots and signs are included.

Part C.
For EVERY positive integer n put q=1/(2n²),
    T_q=(X+2)²-q,P_q=(z+1)^4-qz².
These are irreducible over Q; the original roots have a NEGATIVE expanding reciprocal pair and a circle pair.
The ACTUAL a=T_q(C2(delta))/2=(delta^4-q)/2 is totally positive.
The full archimedean measure satisfies0<m_arch=arcosh(1+sqrt(q)/2)<=q^(1/4)->0.
Yet
    Norm_F(T_q(C2(delta)))=q^4-18q³+49q²-288q+256 ->256,
    Res(P_q,P_q(z²)) ->2^16.
Thus the positivity-only upper comparison with4log2+4C m_arch fails on this rational class.
Its a has the exact nonintegral odd-numerator denominator64n^8 of DC6; primitive integer2n²P_q has leading2n² and height tending to infinity.
The residual f does not vanish eventually: c tends to0 while a tends to8.
Every DC1--DC7 exact formula and all original roots/scalars remain.
Neither rational sequence is an integer Lehmer counterexample, a small-height sequence, a full f=0 triple or an actual admissible original residual realization; the two classes and directions are distinct.

## Current assessment

[Selected decision](#decision-complete-fixed-registration-open)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:58 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Actual positive theta2 interlacing and full trace/height/scalar loss, genuine integral quartic control, complete DP1--DP8 positive-expanding rational sequence and DC1--DC7 negative-expanding rational sequence, all irreducibility/norm/resultant/primitive-leading-height/residual limits. |
| argument | [Entire complete argument](#argument) | Actual positive theta2 interlacing and full trace/height/scalar loss, genuine integral quartic control, complete DP1--DP8 positive-expanding rational sequence and DC1--DC7 negative-expanding rational sequence, all irreducibility/norm/resultant/primitive-leading-height/residual limits. |
| dependency | [Exact fixed input](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-order-index) | Actual trace quotient integrality, full field and reciprocal phase normalization. |
| dependency | [Exact fixed input](Yin_C_G0178_v1.md#statement) | Full f=0 two-adic a-norm floor at original degree. |
| support | [Exact fixed input](Yin_C_G0191_v2.md#statement) | Later stronger actual residual norm floor, not a premise retrospectively inserted into original source analysis. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only accepted reported Schinzel totally-real statement for sqrt(a), not a new original-source proof inspection. |
| dependency | [Exact fixed input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact all-place absolute-height and leading-scalar normalization. |

## Complete original argument

<a id="argument"></a>

### Original account: Actual trace positivity: interlacing costs and two rational boundary controls

Original mathematical dates: 2026-10-20T10:34,2026-10-20T12:30 and2026-10-20T14:38, as separated below.
Fixed content extraction: 2026-10-20T15:51.
Human author Yin.
Root and draft_inventory_later authored the original interlacing, integer quartic and paid-height comparison; the original source inspection is attributed within that section.
The draft_comparison_cleanup agent authored DP1--DP8, with root supplying its question and scope but no construction step.
Entropy_attainment_bridge proposed DC's clustered family and root supplied its complete checking and proof, as recorded in that separate section.
The present extraction preserves these completed author comparisons and their complete distinct controls, without new mathematics or an independent review.
No mathematical computation, scan, source acquisition or fresh original-source reading accompanies this retention.
Existing accepted sources and Claims keep their own review boundaries.

The precise common question is whether actual trace-quotient positivity and its real-root geometry pay a uniform original logarithmic return.
The integer quartic refutes a positivity-only exclusion below log2; it does not approach measure1.
DP retains actual self-composition along a rational near-boundary family with resultant tending to0.
DC retains that positivity along a different rational family with resultant tending to2^16 and defeats the proposed dlog2+Cdm_arch upper bound.
Neither rational control is an original integer-unit or full-residual counterexample, and they cannot replace one another.
Their full denominator, height, norm, irreducibility and embedding proofs remain below.

The original18:34 norm estimate(38)/(42) is retained at its valid weaker scope.
The later adopted [C191v2](Yin_C_G0191_v2.md#statement) proves the stronger actual f=0 norm/resultant income with all dyadic clusters.
It does not convert either rational family into an original input, or supply the missing logarithmic upper estimate.
The present L makes no new arithmetic-theorem adoption.

<a id="actual-trace-positivity-interlacing-screen"></a>
## 10. Actual trace positivity, interlacing and the unpaid original return

Date:2026-10-20T10:34.
Human author Yin.
Root proposed testing the necessary positivity supplied by f=0 and supplied the exact trace-quadratic control below.
The draft_inventory_later agent checked the current fixed inputs, actual MS05 passages, residue conversion, norm normalization and complete control, and supplied the interface analysis in this section.
This is author research and source-applicability screening, not an independent review or adoption.
No new mathematical program, parameter scan, numerical root calculation or source acquisition was performed.

### Actual original objects and the bounded reuse screen

Let P be an actual monic irreducible reciprocal nontorsion integer-unit polynomial, constant1, degree d=2r.
Write P(z)=z^r T(z+z^-1), F=Q(delta), delta=alpha+alpha^-1, with the actual monic irreducible degree-r integer T and [Q(alpha):F]=2.
For this screen assume F is totally real; a genuine Salem input has this property, while an arbitrary reciprocal input need not.
The exact [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies

    C2(x)=x^2-2, C5(x)=x^5-5x^3+5x,
    A(x)=rem_T T(C2(x))/2 in Z[x], deg A<r,
    a=A(delta)!=0, c=rem_T T(C5(x))/5 evaluated at delta!=0.

Both values belong to Z[delta], not merely to an unspecified extension or a freely chosen positive field.
The defect f=2c^2-3a^5=0 forces every real embedding of a to be strictly positive.
The positivity screen below also makes sense under that necessary condition alone; that relaxed condition must not be confused with the full f=0 equation.

The actual [C148 trace-cusp reduction](Yin_C_G0148_v1.md#trace-cusp-exact-reduction), [C149 original expenses](Yin_C_G0149_v1.md#three-prime-cost-and-scope), C153v2 and [L66 trace-degree/order interface](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) retain nonzero integral quotient values, their phases and full degrees.
They do not supply a uniform total-m(P) bound merely from positivity of this quotient.
[L369's genuine Salem derivative-interlacing result](../ledger/Yin_L_G0369_v1.md#salem-interlacing-critical-orders) controls a different phase's critical multiplicities with input-dependent constants; it does not pay the present original-root logarithmic cost.
This is the conclusion of the original bounded applicability screen, not an exhaustive literature assertion.

For the real/circular-interlacing comparison, the actual source is McKee--Smyth, *There are Salem numbers of every trace*, retained arXiv:math/0308213v2,31March2004, title-page date19February2004.
The current [MS05-U001 construction interface](../audits/literature/MS05/Yin_U001.md#ms05-circular-interlacing) was read, followed by direct text inspection of the retained [MS05 PDF](../literature/pdf/MS05.pdf), printed/PDF pages3--5: Lemma4, the circular-interlacing definition, Proposition5(a), its real-line conversion and Proposition6.
That actual source inspection belongs to draft_inventory_later at the original date above; the present extraction does not repeat or enlarge it.
Those exact source statements and their applicability are used at the already recorded acceptance scope.
No journal-version substitution, complete original-proof audit, torsion-coset rereview or new source theorem is claimed.

### Alternating residues versus the correct positive-residue quotient

Order the actual roots of T as delta_1<...<delta_r and put a_i=A(delta_i)>0.
For r>=2 the proper rational function A/T has residues

    a_i/T'(delta_i),

whose signs alternate, since sign T'(delta_i)=(-1)^(r-i).
Thus positivity of every a_i is not the positive-residue hypothesis of MS05 Lemma4 for A/T.
The r=1 case has no alternating-sign obstruction, but does not supply the missing arbitrary-degree theorem.

The correct positive-residue numerator is

    B(x)=rem_T(A(x)T'(x)) in Z[x], deg B<r,
    B(x)/T(x)=sum_(i=1)^r a_i/(x-delta_i).             (36)

Indeed B(delta_i)=a_i T'(delta_i), so the two proper rational functions have identical residues and their difference has no pole or polynomial part.
This proves the identity, including every original trace embedding even when a has smaller own degree.
Its expansion at infinity gives

    deg B=r-1, leading(B)=K=Tr_(F/Q)(a)>0.            (37)

MS05 Lemma4 now gives exactly one simple real zero of B between each consecutive pair of roots of T.
Equivalently, on each pole gap the right side of(36) strictly decreases from positive infinity to negative infinity.
This is an actual real interlacer, without replacing a by an unrelated positive element.

The scalar K is a positive integer and must remain in any normalization.
Replacing B by B/K produces a monic rational interlacer and positive weights a_i/K of sum1; it does not automatically produce a monic integer polynomial.
Conversely, keeping the integer B keeps its actual leading scalar K.
Nonmonicity of this numerator is not itself forbidden by MS05 Proposition5(a): that proposition requires its denominator p to be monic, and permits a nonmonic numerator q.
The scalar issue is a normalization/cost boundary, not a false source hypothesis.

### What f=0 adds, and what the interlacing conversion loses

At every prime mathfrak p of F over2, put e_mathfrak p=v_mathfrak p(2), A_mathfrak p=v_mathfrak p(a), C_mathfrak p=v_mathfrak p(c).
The integral nonzero equation2c^2=3a^5 gives

    5A_mathfrak p=e_mathfrak p+2C_mathfrak p
                       >=e_mathfrak p.

Summing with all residue-degree weights and using sum e_mathfrak p f_mathfrak p=r yields

    v_2(Norm_F a)>=ceil(r/5),
    Norm_F a>=2^ceil(r/5),
    K=sum_i a_i>=r (Norm_F a)^(1/r)>=r 2^(1/5).       (38)

The norm is positive because a is totally positive.
No assumption that a generates F is used, and the ceiling belongs to the integer norm valuation.
These are necessary consequences of the actual f=0 relation; positivity alone gives only K>=r by the same full-norm AM--GM argument.

The scale in(38) does not make the numerator in(36) small or bound its coefficients, denominator after normalization, or values at the original conjugates.
In particular the relaxed information consisting only of positive residues, the norm lower bound in(38) and real interlacing admits the artificial choice A=2, B=2T' for every real-rooted integer T.
That relaxed choice has Norm_F(2)=2^r and K=2r, regardless of the original Salem measure.
It generally is not the actual quotient rem_T T(C2)/2 and is not asserted to satisfy the original f=0 system.
Thus those relaxed interlacing/scale facts alone discard precisely the self-composition arithmetic that a new original-domain argument must use.
This observation constructs no small-measure sequence and does not refute the possibility of a stronger theorem retaining that arithmetic.

For a genuine Salem input, one root of T is delta_r=lambda+lambda^-1>2 and the others lie in(-2,2).
The polynomial T therefore does not itself correspond to a denominator whose roots all lie on the unit circle in MS05's circular-interlacing premise.
The largest root of B is only known to lie in(delta_(r-1),delta_r); its position relative to2 is not controlled by(36).
Removing the exterior linear factor does not preserve an integer polynomial merely because that factor is real.
No actual integral circular pair p,q has been provided whose source output (z^2-1)p-zq is the original P.
Even for a different candidate pair, this output identity, common-factor/cyclotomic exclusions and all original scalars must be checked separately.
The source construction theorem is not an estimate for the original quotient a or an identification of its discrete mean with a Haar mean.
The original quadratic norm multiplicity d=2r is unchanged throughout this screen.

### Exact positive-quotient control below log2

Root's supplied control is

    T(x)=x^2-2x-1,
    P(z)=z^4-2z^3+z^2-2z+1.

Its trace roots are delta_+=1+sqrt2 in(2,5/2) and delta_-=1-sqrt2 in(-2,2).
The trace polynomial is irreducible since its discriminant8 is not a rational square.
In F=Q(sqrt2), the quadratic X^2-delta_+X+1 is irreducible: its discriminant delta_+^2-4 has a negative conjugate at delta_-, whereas every square in this totally real field has nonnegative real conjugates.
Consequently P is an actual irreducible degree-four Salem polynomial.
Its exterior root lambda>1 satisfies lambda+lambda^-1=delta_+<5/2=2+1/2, hence lambda<2 and m(P)=log lambda<log2.
These are exact inequalities, without numerical root evaluation.

Modulo T, x^2=2x+1 and C2(x)=2x-1, giving

    T(C2(x))=6 modulo T, so A(x)=3 and a_i=3
    at both trace embeddings.                         (39)

Thus no negative-embedding argument can exclude every positive quotient below log2.
The control does not satisfy f=0: a=3 is a unit at every2-prime, while2c^2=3a^5 would require5v_mathfrak p(a)=e_mathfrak p+2v_mathfrak p(c)>0 for integral c.
It is a counterexample to the proposed positivity-only exclusion, not a residual singleton or a counterexample to the original norm target.

### The standard totally-positive height bound still pays the original coefficient cost

The additional source comparison uses the already accepted [Smy08-U002 restricted-height statement](../audits/literature/Smy08/Yin_U002.md#smy08-restricted-height-gap), which records Smy08 Section6.1, equation(22), printed pages330--331.
Its Schinzel statement is M(u)>=phi^(deg(u)/2) for a totally real algebraic integer u outside{0,1,-1}, with phi=(1+sqrt5)/2.
The source unit accepts that reported statement at its recorded scope; this screen does not claim a new inspection of Schinzel's original paper or proof.
The [absolute-height convention](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) retains all places and invariance under enlargement of the field.

Under the actual f=0 hypothesis, a!=1: at any2-prime the equation5v(a)=e+2v(c)>0 contradicts v(1)=0.
Choose a square root u=sqrt(a) in the algebraic closure.
It is an algebraic integer by the monic equation X^2-a and transitivity of integrality.
Every conjugate of u is one of the two real square roots of a positive conjugate of a, so its own number field is totally real.
Since a is nonzero and not1, u is outside{0,1,-1}.
Schinzel and the ordinary power identity for absolute height give

    h_abs(u)>=log(phi)/2,
    h_abs(a)=2h_abs(u)>=log(phi).                     (40)

This uses the actual degree of u only in the source theorem; its conversion to absolute height loses no embedding multiplicity.

Put H=||P||_1 and m=m(P).
At every original embedding alpha_j, the actual centered trace quotient is

    a_j=alpha_j^(-d) P(alpha_j^2)/2,
    |a_j|<=(H/2) max{|alpha_j|,|alpha_j|^-1}^d.

The full original field has d embeddings and each of the r trace embeddings occurs twice.
Since a is integral, its finite-place height contributions vanish; using these d embeddings is therefore a valid computation of h_abs(a), even if its own field is smaller.
The unit product and complete Mahler measure give sum_j abs(log|alpha_j|)=2m.
As H>=3 in the nontorsion integer-unit domain, log(H/2)>0, and averaging the preceding pointwise bound proves

    h_abs(a)<=log(H/2)+2m,
    2m>=log(2phi/H).                                 (41)

The second line is the exact consequence of combining the standard source lower bound with this paid original upper bound.
For H>=4 it is negative because phi<2, and hence supplies no positive measure floor.
The only potentially positive integer coefficient-length case left by this comparison is H=3; that already has at most three nonzero coefficients and belongs to the accepted [C27 bounded-support class](Yin_C_G0027_v1.md#statement) and its DS17 source scope.
No new unrestricted input class is obtained by this comparison.
In particular the additional norm information(38) alone gives only h_abs(a)>=log2/5, which is weaker than(40), and cannot repair(41).
This is a failure of the particular standard-height/coefficient-cost combination, not a theorem that the exact self-composition positivity or f=0 condition can never yield a sharper bound.

### Remaining original-domain obligation

The actual extra inputs still available are the self-composition identity defining A, the integral fifth-power/square relation with the actual theta5 quotient, and their full original norms.
Returning(38) through the actual quotient, without replacing the original polynomial, gives

    Res(P(z),P(z^2))=2^d (Norm_F a)^2
        >=2^(d+2ceil(r/5))>=2^(6d/5).                (42)

Indeed P(alpha^2)=2alpha^d a and Norm_(Q(alpha)/Q)(alpha)=1, while the quadratic tower repeats every trace norm twice.
The resultant is nonzero by the existing cross-power separation; its sign in(42) is positive.
This is an increased arithmetic income for the exact self-composition resultant, not a bound on its original archimedean expense.
The inspected L66 and C149 interfaces retain that distinction, and no checked MS05 passage supplies a cancellation estimate for the coupled actual T(C2) and T(C5) evaluations.
A useful next step must combine those inputs with a controlled original-root or coefficient estimate; replacing them by the mere existence of a positive real interlacer loses the needed arithmetic.
No checked MS05 statement in this screen supplies that estimate, and the positive lower scale(38) does not supply an upper expense.
This remains an obligation on the original logarithmic upper expense; the later C191 arithmetic improvement below does not supply that upper bound.

<a id="actual-doubling-positive-rational-control"></a>
## A complete rational failure control for the real-order doubling screen

Date:2026-10-20T12:30.
Human author Yin.
Root requested a narrow source-free examination of the actual condition T(C2(delta_i))>0 at every real trace root, after C191v2 closed the all-prime original unbuffered arithmetic gate.
The draft_comparison_cleanup agent supplies the explicit rational family and complete proof below.
Root supplied the question and scope boundary, not a step of this construction.
This is new author mathematics pending separate independent review; no acceptance is claimed.
No mathematical program, coefficient grid, root approximation or new source theorem was used.

### Exact question and the one relaxed assumption

For an original monic integer reciprocal input with totally real trace field, f=0 forces the actual quotient a=T(C2(delta))/2 to be totally positive.
The preceding [actual interlacing comparison](#actual-trace-positivity-interlacing-screen) proves that converting this positivity to an interlacer loses the actual normalization and supplies no paid original return.
The present question keeps the ACTUAL self-composition and all real roots, instead of replacing a by an arbitrary positive element.
It tests whether this real-order condition alone, together with rational irreducibility, reciprocity and the full Salem-type root arrangement, could force a positive lower bound for the archimedean Mahler quantity.
The following family proves that it cannot.
Its coefficients are rational rather than integral, a difference that is explicitly measured below.
No member is asserted to satisfy the full f=0 equation, and no original integer-unit counterexample is produced.

For every integer j>=0 put

    n=2^(2j+5), q=1/n,
    T_n(X)=X^2-(3/2)X-(1+q),
    delta_+=(3+sqrt(25+16q))/4,
    delta_-=(3-sqrt(25+16q))/4,
    P_n(Z)=Z^2 T_n(Z+Z^(-1))
          =Z^4-(3/2)Z^3+(1-q)Z^2-(3/2)Z+1.       (DP1)

Then T_n and P_n are monic irreducible polynomials over Q, P_n is reciprocal with constant1, and its actual trace field F_n=Q(delta_+) is totally real of degree2.
Its four roots consist of a positive real pair lambda_n,lambda_n^(-1), with lambda_n>1, and one nonreal unit-circle pair.
In particular it is nontorsion, but it is NOT an integer-unit polynomial or a Salem minimal polynomial in the usual algebraic-integer sense.
The exact root ranges are

    -1<delta_-<-1/2, 2<delta_+<5/2.                (DP2)

With C2(X)=X^2-2 define the actual element

    a_n=T_n(C2(delta_+))/2 in F_n.

Both conjugates of a_n are strictly positive.
Nevertheless

    0<m_arch(P_n)=log(lambda_n)<sqrt(2/(5n))->0,
    0<Norm_(F_n/Q)(a_n)<4/n<=1/8.                 (DP3)

Here m_arch of the monic rational polynomial means the sum of log^+ of the absolute values of its four roots.
It is not a replacement for absolute height when the roots are not algebraic integers.

### Rational irreducibility and all four original roots

The radical in(DP1) has square

    25+16q=(25*2^(2j+1)+1)/2^(2j+1).

Its2-adic valuation is-(2j+1), an odd integer, so it is not a square in Q.
The quadratic discriminant of T_n differs from this number by the rational square factor1/4.
Thus T_n is irreducible over Q and F_n has degree2, with precisely the two real embeddings displayed in(DP1).
Because0<q<=1/32, one has5<sqrt(25+16q)<7, proving(DP2).

Over the embedding delta_+, consider X^2-delta_+X+1.
Its discriminant delta_+^2-4 has negative conjugate delta_-^2-4 at the other real embedding.
A square in F_n cannot have a negative real conjugate, so this quadratic is irreducible over F_n.
Its larger root lambda_n therefore has degree4 over Q, and its monic degree4 polynomial is exactly P_n.
The other root above delta_+ is lambda_n^(-1).
Above delta_- in(-1,-1/2), the two roots of X^2-delta_-X+1 are distinct nonreal conjugates with product1, hence both lie on the unit circle.
These are all four conjugates, with none removed from the degree or measure calculation.
An exterior root greater than1 also rules out torsion.

### The complete positive self-composition condition

For any real x,

    C2(x)-x=(x-2)(x+1).

At delta_- in(-1,-1/2), this is negative, so C2(delta_-)<delta_-.
At delta_+>2 it is positive, so C2(delta_+)>delta_+.
A monic real quadratic with roots delta_-<delta_+ is positive outside the closed root interval.
Consequently

    T_n(C2(delta_-))>0,
    T_n(C2(delta_+))>0.                            (DP4)

These are the values of the one actual self-composition polynomial at EVERY root of T_n.
They are not artificially assigned residues and do not involve dropping a negative embedding or replacing a_n by a constant.
Thus the preceding exact positive-quotient/interlacing construction applies at the real level, with the actual self-composition retained.
Integrality of its coefficient and residue objects is not inferred for this rational family.

Since delta_+=2cosh(log lambda_n), rationalizing(DP1) gives

    delta_+-2=4q/(sqrt(25+16q)+5)<2q/5.

For x>0 the elementary inequality2cosh(x)>2+x^2 follows from the exponential series, or its strictly positive even terms after the quadratic term.
Therefore(log lambda_n)^2<delta_+-2<2q/5.
Only lambda_n is outside the unit circle, so this proves the full first assertion in(DP3), including its effective upper bound and limiting value.

### Exact norm, resultant and the missing integrality

The failure is visible in the actual positive quotient's full field norm.
For i in{+,-} and the other index k, write

    T_n(C2(delta_i))
       =(C2(delta_i)-delta_i)(C2(delta_i)-delta_k).

The first factor is(delta_i-2)(delta_i+1).
Using delta_i+delta_k=3/2 and delta_i^2=(3/2)delta_i+1+q, the second is(5/2)(delta_i-1)+q.
Their products over both trace embeddings are

    product_i (delta_i-2)(delta_i+1)
       =T_n(2)T_n(-1)=-q(3/2-q),
    product_i [(5/2)(delta_i-1)+q]
       =(25/4)T_n(1-2q/5)
       =-75/8-(15/2)q+q^2.

Paying the division by2 at BOTH embeddings proves the exact identity

    Norm_(F_n/Q)(a_n)
       =(q/4)(3/2-q)(75/8+(15/2)q-q^2).           (DP5)

Every factor on the last line is positive for0<q<=1/32.
Moreover3/2-q<3/2 and75/8+(15/2)q-q^2<75/8+15/64=615/64<10.
Thus this norm is strictly less than15q/4<4q, proving the second assertion of(DP3) for every member, not just in a limit.
A nonzero algebraic integer has nonzero integer norm, so a_n is not an algebraic integer for ANY j>=0.
This explicitly identifies the lost quotient-integrality step.
It is not a contradiction to the integral quotient theorem, whose premise requires the monic integer T of the original problem.

The usual original phase still holds as a rational-field identity:

    P_n(lambda_n^2)=2lambda_n^4 a_n,
    Norm_(Q(lambda_n)/Q)(lambda_n)=1,
    Res(P_n(Z),P_n(Z^2))=16 Norm_(F_n/Q)(a_n)^2
                              <256/n^2->0.        (DP6)

The quadratic trace-field multiplicity is retained in this formula.
This positive resultant is rational, not a nonzero integer resultant under the original hypotheses.
It therefore cannot supply the integer norm income of an original P.

Clearing the ACTUAL coefficient denominators gives

    nP_n(Z)=nZ^4-(3n/2)Z^3+(n-1)Z^2
                         -(3n/2)Z+n.             (DP7)

It is primitive in Z[Z]: n and n-1 already have greatest common divisor1, and3n/2 is an integer.
It is the primitive irreducible integer polynomial of lambda_n, with leading and constant coefficients n, not1.
Accordingly, in the ordinary absolute logarithmic height convention already used in the preceding interlacing comparison,

    h_abs(lambda_n)=(log n+m_arch(P_n))/4
                                        ->infinity. (DP8)

The missing finite-place cost is exactly visible in log n.
Norm(lambda_n)=1 by itself does not make this nonintegral algebraic number an algebraic unit.
The small archimedean quantity in(DP3) is therefore neither a small-height example nor a Lehmer counterexample.

### Precise consequence for the original positivity inquiry

The family keeps a fixed trace degree2, rational irreducibility, full reciprocal degree4, the actual totally real trace field, one exterior reciprocal pair, all original conjugates and the exact self-composition sign condition.
Even with all these real-order facts, the monic archimedean quantity has no positive lower bound.
Thus a proof using only that real-root ordering or doubling-sign condition cannot establish a uniform original measure gap without an additional integer/arithmetic step.
The obstruction is sharper than the earlier single integer quartic with m<log2: this is an explicit rational near-boundary sequence, while its exact denominators show why it cannot be promoted to the original integer class.
The norm and resultant identities above expose that difference rather than conceal it.

The full f=0 equation with the actual theta5 quotient is not imposed in this control.
The adopted C191v2 uses precisely such actual integral self-composition arithmetic to recover new norm income; its conclusions are unaffected.
This completed negative screen does not prove that actual integer f=0 is impossible, does not rule out a further integer root-order argument, and does not pay the original logarithmic-transfer cost.
Those remain separate mathematical questions about the original input and its paid transfer.

<a id="clustered-rational-doubling-upper-control"></a>
## A complete rational control for the positivity-only doubling upper bound

Date: 2026-10-20T14:38.
Human author Yin.
Entropy_attainment_bridge proposed the clustered trace family below while screening the actual doubling upper-bound interface.
Root supplied and checked the complete irreducibility, positivity, resultant, normalization, height and residual-limit argument.
Both are contributors; this is an author-level exact control, not an independent review or an original integer counterexample.
No numerical calculation or parameter scan is used.

The [actual f=0 doubling income](Yin_C_G0191_v2.md#statement) has log Res(P,P(z^2))>=(14/11)d log2 on the original monic integer domain.
A valid upper bound d log2+C d m(P) there would be useful, but the known [exact radial/angular split](Yin_C_G0001_v1.md#doubling-exact-radial-angular-split) retains its entire mixed angular term.
The [existing two-frequency control](Yin_C_G0001_v1.md#two-frequency-linear-coupling-control) already prevents replacing that term by one-point discrepancy without additional arithmetic.
The following family tests precisely whether actual trace positivity and real root ordering, by themselves, supply the missing upper bound after integrality and the full residual equation have been dropped.
The earlier [rational positive self-composition control above](#actual-doubling-positive-rational-control) has a doubling resultant tending to zero and does not test this upper-bound assertion.

For each integer n>=1 put

    q=1/(2n^2), T_q(X)=(X+2)^2-q,
    P_q(z)=z^2T_q(z+z^(-1))=(z+1)^4-q z^2.
                                                            (DC1)

The two trace roots are delta_+=-2+sqrt(q) in(-2,-1) and delta_-=-2-sqrt(q)<-2.
The trace polynomial is irreducible over Q because q is not a rational square, and its field is Q(sqrt(2)).
For a root delta, the quadratic z^2-delta z+1 has discriminant delta^2-4.
At the embedding delta_+, this is q-4sqrt(q)<0, so it cannot be a square in the totally real trace field.
Thus every root alpha generates a degree-four extension of Q, proving irreducibility of P_q over Q.
The polynomial is monic rational, reciprocal and has constant1, but is not an integer polynomial.
One inverse pair of roots lies on the circle and the pair over delta_- is real with one root of modulus>1, so it is nontorsion.
Its monic archimedean Mahler logarithm is exactly

    m_arch(P_q)=arcosh(1+sqrt(q)/2)
                     <=q^(1/4) ->0.             (DC2)

The inequality follows from cosh(u)>=1+u^2/2 for u>=0.
It is not the Mahler logarithm of a primitive integer minimal polynomial.

Use the actual divided value a_q=T_q(C2(delta))/2, with C2(X)=X^2-2, without asserting its integrality.
Since C2(delta)+2=delta^2,

    T_q(C2(delta))=delta^4-q>0                   (DC3)

at both real trace embeddings: q<1 and |delta|>=2-sqrt(q)>1.
Thus a_q is actually totally positive, not a freely chosen positive element.
Writing u=delta+2, u^2=q gives

    T_q(C2(delta))=16+23q+q^2-(32+8q)u,
    D(q)=Norm_(F/Q)T_q(C2(delta))
         =(16+23q+q^2)^2-q(32+8q)^2
         =q^4-18q^3+49q^2-288q+256.             (DC4)

The degree-four norm retains the quadratic trace tower and the original phase:
P_q(alpha^2)=alpha^4 T_q(C2(delta)) and Norm_(K/Q)(alpha)=1.
Consequently

    Res(P_q(z),P_q(z^2))=D(q)^2 ->2^16,
    (1/4)log Res(P_q,P_q(z^2))-log2 ->3log2.     (DC5)

In particular no fixed finite C can give
log Res(P_q,P_q(z^2))<=4log2+4C m_arch(P_q)
for every sufficiently large n in this relaxed class.
This is a complete failure of the proposed positivity-only upper, not a failure under the original integer or full-residual hypotheses.

The missing integrality is explicit even at the actual quotient value.
Substituting q=1/(2n^2) in(DC4) gives

    Norm_(F/Q)(a_q)
      =[1-36n^2+196n^4-2304n^6+4096n^8]/(64n^8).
                                                            (DC6)

The numerator is odd, so this rational norm is not an integer.
Hence a_q is not an algebraic integer at any n.
Clearing the polynomial denominator gives the primitive integer polynomial

    P_prim=2n^2(z+1)^4-z^2,
    leading(P_prim)=constant(P_prim)=2n^2.

It is primitive because its middle coefficient is12n^2-1, coprime to2n^2, and irreducible by the rational irreducibility just proved.
The exact absolute-height normalization from [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) therefore gives

    m(P_prim)=log(2n^2)+m_arch(P_q),
    h(alpha)=[log(2n^2)+m_arch(P_q)]/4 ->infinity.
                                                            (DC7)

Neither the leading scalar nor the denominator has disappeared.
Finally, C5(-2)=-2, so at both trace embeddings c_q=T_q(C5(delta))/5 tends to0 while a_q tends to8.
By the displayed polynomial expressions and continuity,
2c_q^2-3a_q^5 tends to -3*8^5, a nonzero negative number.
Thus the f=0 equation also fails at both trace embeddings for all sufficiently large n.
This separates the tested relaxed implication from every actual use of C191 or the full residual system.

The control proves that total reality and actual quotient positivity alone do not supply the proposed upper bound.
It drops both integrality and the residual relation, so it does not separately establish that either one is necessary or that their combination suffices.
It constructs no original near-one algebraic units and does not settle the full signed comparison of the rational regularizer.
