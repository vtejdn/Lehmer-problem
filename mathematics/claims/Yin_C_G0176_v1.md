---
author: Yin
---
# Polynomial mixed-defect forms: exact shear infimum and complete approximation costs

Human author Yin.
The draft_inventory_later agent authored the complete arguments below on2026-10-20T09:08 and2026-10-20T09:14.
Root supplied the question, requested explicit costs and pointed to existing regularization and positive-completion comparisons, as disclosed in the preserved argument sections.
This Claim registers the reusable mathematics already fully retained in [L437](../ledger/Yin_L_G0437_v1.md), whose original author account remains preserved.
The actual whole [R445 finding](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) covers that source proof; the later [R448](../audits/reviews/Yin_R_G0448_v1.md#c176-statement-extraction-finding) checks this Claim's actual statement and extraction before the selected adoption below.
No new proof, numerical computation or source acquisition is introduced by this registration.
The later original-conjugate and Fourier-cost continuation in D36 is not part of this Claim.

## Statement

Let P be a monic irreducible reciprocal nontorsion polynomial in Z[z], of even degree d=2r and constant coefficient1, with alpha a root, K=Q(alpha) and totally real F=Q(alpha+alpha^(-1)).
Use the actual nonzero integral trace quotients a,b,c from C153v2 and their defects e=b^2-a^3, f=2c^2-3a^5 and g=c^3-2b^5, which may individually vanish.
Define the unreduced polynomials and real centered circle functions

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72, F_0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375, L=972000.

All circle integrals use normalized Haar measure, and all algebraic norms below use the full original fields.
The following three parts, including every explicit normalization and cost in the numbered formulas, form the selected statement.

**A. Integral matrix mixing invariant under three rotations.**
For every M(X) in Mat_3(Z[X]) with nonzero determinant polynomial D(X), let h be its largest entry degree, X(z)=z^3+z^(-3), and B_M=2||M(X(z))(E,F_0,G)^t||^2 on the circle, with its algebraic sum-of-squares extension.
If D(alpha^3+alpha^(-3))!=0, then Norm_K B_M(alpha)>=2^d; this holds automatically for every nonzero constant determinant and every unimodular polynomial matrix.
The exact integral numerator, degree bound30d+12h, denominator L^(2d), scalar Haar identity and radial fee(30+12h/d)m(P) are(M1)--(M5).
For each of the two J102 original controls separately, the entire matrix class obeys(M6)--(M8), without a degree, coefficient-size or conditioning restriction: I_M>log2+11/30 on the quartic and I_M>log2+21/10 on Lehmer.
The circle conclusion needs only the determinant polynomial to be nonzero and does not require its value at the original trace point to be nonzero.
These two controls are exactly P=z^4-z^3-z^2-z+1 and P=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1.

**B. Complete rational polynomial-shear infimum and finite construction.**
With x=z+z^(-1), for every S,T in Q[x] put B_(S,T)=(E+S(x)G)^2+(F_0+T(x)G)^2+2G^2 and J_G=integral log G^2.
Every such symbol has Norm_K B_(S,T)(alpha)>=2^d, and

    inf_(S,T in Q[x]) integral log B_(S,T)=log2+J_G.

No polynomial pair, including a real-coefficient pair, attains this full-class infimum.
The explicit shears(P5) have exact ordinary numerator degree(60N+80)d, denominator and leading coefficient(P6)--(P7), full norm/scalar/radial identities(P8), and normalized coefficient/term-count bounds(P8a).
Their complete finite-error bound(P9) and sufficient integer choice(P10) retain the actual degree15d, coefficient sums and all denominators, with no squarefree or circle-root exclusion.
For each fixed input with J_G<0, every strict saving eta with0<eta<-J_G is achieved by a finite pair; the existing two certified controls have such pairs with Haar mean below log2-1.
No numerical N or parameter has been evaluated here.

**C. Fixed degree and the unresolved uniform scope.**
For every fixed input P and integer h>=0, the functional on real polynomial pairs of degree at most h is continuous and coercive and attains a minimum strictly greater than log2+J_G.
The rational-pair infimum at that degree is the same real minimum, without an assertion of rational attainment; its positive gap is delta(P,h) in(P11).
Thus any fixed-input sequence approaching the full-class infimum must have unbounded and eventually arbitrarily large shear degree; coefficients or denominators alone at fixed degree do not suffice.
The actual original-conjugate discrepancy obeys(P12).
There is no claim of a uniform delta(P,h) over varying P, a necessary infinite degree for one fixed saving, an input-uniform transfer bound, or a covering Mahler gap.

<a id="polynomial-mixing-direct-inputs"></a>
## Exact direct inputs and reuse limits

| Input | Actual use and boundary |
| --- | --- |
| [C153v2 pairwise exclusions](Yin_C_G0153_v2.md#argument) | Nonzero integral a,b,c in a totally real field imply (e,g)!=(0,0) and (f,g)!=(0,0); the distinct e=f=0 case is not excluded. |
| [C153v2 actual trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original d=2r, actual K/F quadratic extension, integral nonzero trace quotients and exact centered defect values. |
| [C149 original defect polynomials](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Complete H23,H25,H35, their degree6d/10d/15d, leading coefficients1/11/7 and scalar denominators72/800/30375. |
| [C157v3 exact original and circle interfaces](Yin_C_G0157_v3.md#statement) | Centered real functions, L=972000 and original trace-field domain; its constant-parameter theorem is not claimed to cover the new polynomial parameters. |
| [L401 constant positive-definite obstruction](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen) | Prior determinant screen and comparison boundary; nonconstant matrices require the new proof below. |
| [J102 analytic rotation reduction](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | Exact V, nonmonic Laurent normalization and Lambda_P definition for the same original defects. |
| [J102 certified controls](../computations/programs/Yin_J_G0102/readme.md#certified-results) and [R397 whole finding](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) | Only the quartic and Lehmer inputs, nonzero determinants and existing certified Lambda bounds; no newly executed reconstruction or root isolation. |
| [C379 zero-compatible regularization](Yin_C_G0379_v1.md#zero-compatible-root-error) | Full degree-D product bound with actual M(H), repeated roots and nonmonic scalar; no squarefree simplification or free normalization. |
| [J100 component results](../computations/programs/Yin_J_G0100/readme.md#certified-results) and [R379 whole finding](../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) | Existing J_G<-2 on the same two controls, at their certified-error and shared-library limits; no new N evaluation or parameter scan. |
| [D1 positive completion](../drafts/Yin_D_G0001.md#positive-reciprocal-completion-return) | Comparison only: the already retained degree4d fixed-input negative-Haar/nonnegative-norm mechanism is not a new premise or independently reviewed result supplied here. |
| [C140 normalized sparse transfer](Yin_C_G0140_v1.md#argument) and [original explicit-norm comparison, retained in C587](Yin_C_G0587_v2.md#paid-transfer-reuse) | Comparison of missing degree, term-count and normalized coefficient budgets; the original specialization was an author-only comparison at this record, and its later fixed proof/review is not attributed here; no automatic coverage of the new dense family is imported. |

<a id="argument"></a>
## Complete argument

<a id="rotation-invariant-polynomial-mixing"></a>
## Integral polynomial mixing invariant under the three rotations

2026-10-20T09:08.
The draft_inventory_later agent develops the following author argument for Yin under the resumed four-inquiry allocation.
Root supplied the remaining mixed-form question and required a genuine original-object conclusion; root did not supply a proof step in this argument.
No independent review, new numerical calculation or parameter scan is asserted.

The allowed classes must first be distinguished.
[C157v3](Yin_C_G0157_v3.md#statement) has constant quadratic matrix determinant b>=2, so [L401](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen) already excludes its entire parameter family on the Lehmer control.
Increasing its clearing denominator does not evade that determinant obstruction.
L401 does not itself cover arbitrary z-dependent matrices, rank-two semidefinite forms or sufficiently small positive determinants with a separately justified arithmetic floor.
The present argument treats a nonconstant polynomial-matrix class and retains those other questions.

### Construction, original-field income and complete degree cost

Let P satisfy the actual C157v3 trace-field domain: P is monic irreducible reciprocal and nontorsion, of degree d=2r and constant coefficient1, and F=Q(alpha+alpha^(-1)) is totally real.
Put K=Q(alpha), and let v(z)=(E(z),F_0(z),G(z))^t be the exact three real centered Laurent polynomials in [C157v3](Yin_C_G0157_v3.md#statement), with common denominator L=972000.
Their values at alpha are the integral trace defects e,f,g of [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
In particular v(alpha)!=(0,0,0).

Choose a three-by-three matrix M(X) with entries in Z[X], with nonzero determinant polynomial D(X)=det M(X), and let h be the largest entry degree.
Define

    X(z)=z^3+z^(-3), chi=alpha^3+alpha^(-3),
    w(z)=M(X(z))v(z),
    B_M(z)=2 sum_(i=1)^3 w_i(z)^2.                    (M1)

Assume D(chi)!=0 for the arithmetic conclusion.
This condition is automatic when D is a nonzero constant, and in particular for every unimodular polynomial matrix.
No restriction on the size of the entries, h or a condition number is imposed.
Since alpha is a unit, chi is an algebraic integer in F; the vector M(chi)(e,f,g)^t therefore has integral entries in F and is nonzero.
At every embedding of the totally real field F its sum of squares is positive.
Its full norm is consequently a positive integer at least1, whence

    Norm_F(B_M(alpha))>=2^r,
    Norm_K(B_M(alpha))=Norm_F(B_M(alpha))^2>=2^d.       (M2)

The second equality uses the actual [K:F]=2 and keeps every original conjugate.
This is an automatic floor for this stated construction; it is not inferred from its circle behavior.
More generally the same arithmetic conclusion holds whenever M(chi)(e,f,g)^t is nonzero, even if D(chi)=0, but no automatic assertion is made in that singular case.

The entries of L v are integral Laurent polynomials with support inside [-15d/2,15d/2].
Every entry of M(X(z)) has support inside [-3h,3h].
Set

    W=15d+6h,
    A_M(z)=L^2 z^W B_M(z)
          =2z^W sum_i [L w_i(z)]^2 in Z[z].          (M3)

Then deg A_M<=2W=30d+12h, the centered support of B_M is contained in [-W,W], and

    Norm_K(B_M(alpha))=Res(P,A_M)/L^(2d),
    integral log B_M dmu=m(A_M)-2log L.             (M4)

The first equality uses Norm_K(alpha)=1.
The actual content, zero multiplicities, leading coefficient and any monomial factor of A_M remain in the second identity.
Only an upper degree bound is claimed, since outer terms may cancel before the sum of squares is formed.
On the circle X is real and B_M is nonnegative.
It is not the zero Laurent polynomial: outside the finitely many zeros of D(X(z)), M(X(z)) is invertible and the nonzero vector v cannot vanish identically.
Some w_i is therefore a nonzero real Laurent polynomial; its square supplies an integrable logarithmic lower bound for B_M away from its finite zero set.
Together with boundedness above, this proves the logarithmic integrability used in (M4).

For S_M=sup_circle B_M>0, the ordinary disk estimate for A_M and its width-2W reciprocal identity give

    |B_M(t)|<=S_M max{|t|,|t|^(-1)}^W
        for every nonzero complex t,
    log2<=log Norm_K(B_M(alpha))/d
        <=log S_M+(30+12h/d)m(P).                    (M5)

Indeed L^2 B_M is a symmetric Laurent polynomial, so z^(2W)A_M(z^(-1))=A_M(z) even if the two outer coefficients vanish.
Apply the disk estimate at t and t^(-1), then use sum_beta |log|beta||=2m(P) over all d original roots.
Thus h<=H d would give the explicit degree-uniform radial coefficient30+12H.
Neither that linear degree condition nor (M5) replaces the supremum by a Haar average or bounds expanded coefficient mass.

### Complete all-matrix circle obstruction on both existing controls

For either original J102 control, let omega=exp(2pi i/3), let V(z) be the row matrix with rows v(omega^j z)^t for j=0,1,2, and use the exact quantity

    Lambda_P=(log2+2 integral log|det V| dmu)/3

from [J102's analytic reduction](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen).
Its determinant is a nonzero Laurent polynomial on each control, as established by the [complete J102 certificates](../computations/programs/Yin_J_G0102/readme.md#certified-results) and [R397](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding).
No new determinant or Mahler value is calculated here.

The identity X(omega z)=X(z) makes the transformed row matrix equal to V(z)M(X(z))^t.
Its rows, after multiplication by sqrt2, have squared Euclidean lengths B_M(z), B_M(omega z), B_M(omega^2 z).
Hadamard's inequality therefore gives

    product_(j=0)^2 B_M(omega^j z)
       >=8 |D(X(z))|^2 |det V(z)|^2.                 (M6)

All three logarithms are integrable.
In addition to the preceding proof for B_M, both nonzero Laurent polynomials D(X(z)) and det V have only finitely many finite-order circle zeros.
Taking logarithms away from those finite sets and using Haar rotation invariance yields

    I_M:=integral log B_M dmu
       >=Lambda_P+(2/3)log2+(2/3)m(D(X(z)))
       >=Lambda_P+(2/3)log2.                        (M7)

The last inequality does not assume that M is unimodular.
If k=deg D, then z^(3k)D(z^3+z^(-3)) is a nonzero ordinary integer polynomial of degree6k whose leading coefficient is the nonzero integer leading coefficient of D.
The scalar Jensen formula therefore gives m(D(X(z)))>=0; the same assertion for constant D is log|D|>=0.
This pays the entire variable determinant rather than treating a z-dependent matrix as a constant one.
The circle obstruction (M7) requires only D nonzero as a polynomial, not D(chi)!=0.

The existing J102 enclosures give Lambda_P>0.6342978356>3/5 on the quartic and Lambda_P>2.3906764770>7/3 on Lehmer.
The elementary inequality exp(7/10)>1+7/10+49/200+343/6000>2 gives log2<7/10.
Consequently (M7) implies the exact strict margins

    I_M>log2+11/30       on the quartic control,
    I_M>log2+21/10       on the Lehmer control.      (M8)

Thus every integral polynomial matrix in this class with nonzero determinant fails every sub-log2 Haar target on both prescribed controls, regardless of degree, coefficient size or conditioning.
This includes all nonconstant unimodular choices, whose original arithmetic floor (M2) is automatic.
The result excludes this entire allowed construction class, rather than a sampled parameter set.
It does not exclude matrix entries depending on z+z^(-1) without the three-rotation invariance, rank-deficient matrices, rational matrix determinants with negative Haar logarithm, or a separately proved larger arithmetic income with a different comparison target.
Those possibilities still need their own original-field nonvanishing, full norm, degree and transfer costs.
The original mixed-form inquiry is not complete merely because this new class has been excluded.

<a id="polynomial-shear-exact-infimum"></a>
## Exact Haar infimum for rational polynomial shears with the full norm floor

2026-10-20T09:14.
The draft_inventory_later agent supplies this new author construction, its infimum, finite error bound and complete costs for Yin.
Root requested an explicit error and pointed to the existing C113/L358 regularization interfaces and the need to compare D35's positive completion; root supplied no formula or proof step below.
No new native computation, selected numerical N or independent review is asserted.

This inquiry concerns the prescribed three mixed defects and the unchanged full original norm floor2^d.
[D1's positive reciprocal completion](../drafts/Yin_D_G0001.md#positive-reciprocal-completion-return) already gives degree4d fixed-input negative Haar logarithm with nonnegative original norm on every input with0<m(P)<log2.
Thus existence of a favorable circle function is not a new general transfer mechanism.
The result here is the exact infimum of a different specified class, while retaining its stronger2^d arithmetic floor and paying all approximation costs.

### The entire polynomial-shear class and its arithmetic domain

Keep the same original reciprocal totally-real trace-field domain as in (M1)--(M5).
Write x=z+z^(-1).
Reciprocity gives rational polynomials E_0,F_0,G_0 in x with

    E(z)=E_0(x), F(z)=F_0(x), G(z)=G_0(x),
    deg E_0=3d, deg F_0=5d, deg G_0=15d/2.           (P1)

Their leading coefficients are -1/72, -11/800 and -7/30375 respectively, by the exact numerator endpoints in C157v3.
Here F(z) denotes the centered H25 function, and F_0(x) its trace polynomial; the number field remains F.
For any rational polynomials S,T define

    B_(S,T)(z)=(E(z)+S(x)G(z))^2
                 +(F(z)+T(x)G(z))^2+2G(z)^2,
    I(S,T)=integral log B_(S,T) dmu,
    J_G=integral log G^2 dmu.                        (P2)

Every such B has

    Norm_K(B_(S,T)(alpha))>=2^d.                    (P3)

Indeed S(alpha+alpha^(-1)) and T(alpha+alpha^(-1)) are in the totally real field F.
If the field element g is nonzero, at every embedding sigma the actual value of B is at least2sigma(g)^2>0; multiplication gives Norm_F B>=2^r|Norm_F g|^2>=2^r.
The transformed coordinates may be nonintegral; only the original nonzero integral g norm is used.
If g=0, C153v2 gives e and f nonzero, and the actual value is e^2+f^2.
The embeddingwise AM-GM inequality and the two original integer norms give Norm_F B>=2^r in this case too.
The actual quadratic norm tower then proves (P3).
There is no requirement that S or T have rational values at alpha, or that their coefficients be fixed under every embedding after evaluation; each embedded square remains nonnegative.

The same circle family can be considered for real polynomial S,T, but (P3) is asserted only for the rational-coefficient family just defined.
Since B_(S,T)>=2G^2 and G is a nonzero Laurent polynomial, all of its circle logarithms are integrable.
Therefore

    inf_(S,T in Q[x]) I(S,T)=log2+J_G.             (P4)

The infimum is never attained in this class.
The lower bound follows pointwise; the explicit construction below proves the opposite infimum inequality.
If equality held for finite S,T, the nonnegative logarithmic difference would vanish almost everywhere, forcing E_0+S G_0 and F_0+T G_0 to be zero polynomials.
Already the first identity is impossible because deg G_0>deg E_0 and E_0 is nonzero.
Thus I(S,T)>log2+J_G for every individual pair, including real polynomial pairs.

### Explicit approximating shears, coefficients and original radial cost

Let

    A_0=(||H23||_1/72)^2+(||H25||_1/800)^2,
    c=1+(||H35||_1/30375)^2=a/b,

where a,b are positive integers.
These are input-dependent rational constants, with E^2+F^2<=A_0 and0<=G^2<c on the circle.
For N>=0 put

    U=1-G_0^2/c,
    S_N=-(E_0 G_0/c) sum_(k=0)^N U^k,
    T_N=-(F_0 G_0/c) sum_(k=0)^N U^k,
    R_N=U^(N+1).

The finite geometric identity gives exactly

    E_0+S_N G_0=E_0 R_N,
    F_0+T_N G_0=F_0 R_N,
    B_N: =B_(S_N,T_N)
         =(E^2+F^2)(1-G^2/c)^(2N+2)+2G^2.          (P5)

At every circle point with G!=0, B_N decreases to2G^2.
Its logarithm is bounded below by the integrable log(2G^2) and above by an integrable fixed upper function, for example max{log B_0,log(2G^2)}.
Dominated convergence proves I(S_N,T_N) decreases to log2+J_G, including all finite-order zeros of G and repeated zeros of H35.

All degrees and denominators in this construction remain explicit.
The trace-polynomial degrees of the two shears are (15N+21/2)d and (15N+25/2)d.
Set

    W_N=(30N+40)d,
    D_N=L^2(a*30375^2)^(2N+2),
    A_N(z)=D_N z^(W_N) B_N(z).                     (P6)

Then A_N is an integer reciprocal polynomial of exact degree2W_N=(60N+80)d.
Its leading and constant coefficient is exactly

    121*1215^2*(49b)^(2N+2)>0.                     (P7)

To check these claims, z^(-15d)H35^2/30375^2=G^2 and hence a*30375^2 clears1-G^2/c.
The common L^2 clears E^2+F^2 and2G^2.
The highest trace degree in (P5) is the F_0^2 term times G_0^(4N+4), giving W_N=10d+(30N+30)d with no competitor at that degree.
Its coefficient is (11/800)^2(7^2/(c*30375^2))^(2N+2); multiplying by D_N gives (P7).
Centering a real polynomial in z+z^(-1) gives the same nonzero coefficient at both Laurent endpoints, so there is no hidden width cancellation.
Consequently the exact full norm, Haar identity and supremum return are

    Norm_K(B_N(alpha))=Res(P,A_N)/D_N^d>=2^d,
    I(S_N,T_N)=m(A_N)-log D_N,
    log2<=log Norm_K(B_N(alpha))/d
         <=log sup_circle B_N+(60N+80)m(P).         (P8)

The radial proof is the centered width-W_N disk estimate used in (M5).
No denominator cancellation, lost original embedding or replacement of the supremum by Haar is permitted.
There is also a direct complete upper account for the normalized coefficient budget.
Put G_1=||H35||_1/30375 and f_N=A_N/(2D_N).
Laurent coefficient convolution, the definitions of A_0 and c, and the monomial invariance of coefficient l1 give

    term_count(f_N)<=2W_N+1,
    ||f_N||_1<= (A_0/2)(1+G_1^2/c)^(2N+2)+G_1^2.   (P8a)

Indeed ||1-G^2/c||_1<=1+G_1^2/c and ||E^2+F^2||_1<=A_0.
These are upper budgets with the actual original coefficient norms, not necessary growth rates for the individual f_N.
They supply no input-independent bound on term count, degree multiplier or normalized size.

### Explicit finite N error, including all circle zeros

Write D=15d, the exact ordinary degree of H35.
For any rho>0 define

    C(rho)=1+log_+(A_0/(2rho^2))/log2,
    epsilon_N=I(S_N,T_N)-(log2+J_G),

where log_+(u)=max{0,log u}.
Then

    0<epsilon_N
      <=2 C(rho) E_(30375rho)(H35)
             +A_0/(2rho^2) exp(-2(N+1)rho^2/c)
      <=D C(rho)(30375rho/7)^(1/D)
             +A_0/(2rho^2) exp(-2(N+1)rho^2/c).     (P9)

Here E_delta(H)=(1/2)integral log(1+delta^2/|H|^2), with its normalization exactly as in [C379's all-root product bound](Yin_C_G0379_v1.md#zero-compatible-root-error).
That bound permits repeated roots and nonmonic scalar factors, which is needed for H35; no squarefree hypothesis from C113 is inserted.

For the first inequality, split the circle into G^2<rho^2 and its complement.
On the complement use (1-G^2/c)^(2N+2)<=exp(-2(N+1)G^2/c), followed by log(1+y)<=y.
On the small set use

    log(1+A_0/(2G^2))
       <=log_+(A_0/(2rho^2))+log(1+rho^2/G^2).

The small-set measure is at most integral log(1+rho^2/G^2)/log2.
Enlarging these nonnegative integrals to the entire circle gives the first bound in (P9).
Since |G|=|H35|/30375 on the circle, this is exactly the stated regularization input.
L358 gives E_delta(H35)<=D asinh((delta/M(H35))^(1/D)/2).
The leading coefficient7 implies M(H35)>=7; using asinh y<=y proves the second bound without discarding the actual denominator30375.

In particular the bound supplies a fully explicit sufficient integer N for any prescribed error0<epsilon<=1.
Put

    C_A=1+log_+(A_0*(30375/7)^2/2)/log2,
    k=ceil(max{4,2log_2(2D(C_A+2D)/epsilon)}),
    rho=(7/30375)2^(-kD),
    N=ceil[(c/(2rho^2))log_+(A_0/(epsilon rho^2))].   (P10)

Then epsilon_N<=epsilon.
Indeed C(rho)<=C_A+2kD<=k(C_A+2D).
For integers k>=4, k<=2^(k/2), so the first term in (P9) is at most D(C_A+2D)2^(-k/2)<=epsilon/2.
The chosen N+1 bounds the second term by epsilon/2, including the case when its log_+ is zero.
This is a sufficient estimate, not a necessary lower bound on N or a claim of optimal approximation.
Its rho contains the full exponent D=15d and its degree/denominator consequences are exactly (P6)--(P8).

### Fixed degree has an attained real minimum strictly above the full infimum

Fix this same P and an integer h>=0.
Let V_h be the finite-dimensional space of real polynomials of degree at most h, including the zero polynomial, with its usual coefficient norm.
The functional I on V_h times V_h is continuous and coercive.
Consequently there is a positive constant delta(P,h) such that

    min_(S,T in V_h) I(S,T)
      =inf_(S,T in Q[x], deg S,deg T<=h) I(S,T)
      =log2+J_G+delta(P,h),  delta(P,h)>0.           (P11)

The real minimum is attained.
Attainment by a rational pair is not asserted.

For continuity, coefficientwise convergence at this fixed degree gives uniform convergence of the shears and of B_(S,T) on the circle.
In a bounded neighborhood of the limiting coefficients those symbols have a common finite upper bound C>=1.
They all have the same integrable lower logarithm log(2G^2) outside the finite zero set of G.
Their logarithms therefore converge almost everywhere and are dominated in absolute value by an integrable function depending only on C and log(2G^2).
Dominated convergence proves continuity even when one or both shears are zero or their actual degrees drop.

For coercivity, put g_0=deg G_0=15d/2 and n=2(g_0+h).
The maps

    S -> z^(g_0+h)[S G_0](z+z^(-1)),
    T -> z^(g_0+h)[T G_0](z+z^(-1))

are injective linear maps from V_h to ordinary polynomial coefficient spaces of degree at most n.
Multiplication by the nonzero G_0 is injective, and a nonzero polynomial in x remains nonzero upon substitution x=z+z^(-1), as its highest Laurent coefficient shows.
An injective linear map on a fixed finite-dimensional space bounds its output norm below by a positive multiple of the input norm: restrict to the compact coefficient unit sphere and take the positive minimum of the continuous output norm.
After adding the fixed E_0 or F_0 term, it follows that if the coefficient norm of the pair (S,T) tends to infinity, the maximum of the two coefficient norms of

    Q_E(z)=z^(g_0+h)(E_0+S G_0)(z+z^(-1)),
    Q_F(z)=z^(g_0+h)(F_0+T G_0)(z+z^(-1))

tends to infinity.
Neither polynomial is zero for any S,T, since deg E_0 and deg F_0 are both strictly below deg G_0.
This includes constant and zero shears.

For any nonzero ordinary polynomial Q of degree at most n, its root factorization and the elementary symmetric coefficient formula give

    max_j |Q_j|<=2^n M(Q).

Each product of a subset of root moduli is bounded by the product of max{1,|root|}, and the sum of the relevant binomial coefficients is at most2^n; leading scalars and zero roots are retained.
Thus m(Q)>=log(max_j |Q_j|)-n log2.
On the circle B_(S,T) is at least the square of either real component E+SG or F+TG, so

    I(S,T)>=2 max{m(Q_E),m(Q_F)}.

The preceding coefficient escape proves that I tends to infinity when the pair's coefficient norm does.
A continuous coercive function on this finite-dimensional real space attains its minimum on a sufficiently large closed ball.
Every individual pair has the strict inequality proved after (P4), hence the attained minimum has a strictly positive difference delta(P,h).
Rational pairs are dense in the real coefficient space; continuity at a real minimizer gives the equality of the rational infimum and the real minimum in (P11).

It follows that for a fixed P, any sequence of rational polynomial shears with I tending to log2+J_G must have max{0,deg S,deg T} tending to infinity.
Arbitrarily large coefficients or denominators at bounded shear degree cannot approach that full-class infimum.
This necessary degree escape concerns approximation to the exact infimum only.
It does not exclude a finite degree for a prescribed strict saving above that infimum, and the constants delta(P,h) are not asserted uniform when P varies.

### What is resolved, and the transfer obligation that remains

For any fixed input with J_G<0 and any0<eta<-J_G, (P10) with0<epsilon<min{1,-J_G-eta} produces an actual rational polynomial pair with I(S_N,T_N)<log2-eta and the actual original norm floor2^d.
[J100's retained certified values](../computations/programs/Yin_J_G0100/readme.md#certified-results) have J_G<-2 on both prescribed controls.
Thus choosing eta=1 and any0<epsilon<1 in (P10) gives actual finite shears with I<log2-1 on both controls, without a parameter scan, an evaluated N or a new numerical certificate.
The arithmetic statement uses the original P and trace defects; no auxiliary replacement of the original field has occurred.

This settles the Haar infimum and attainment question for the entire rational polynomial-shear class with buffer2G^2.
It also gives a constructive finite-error certificate with every degree, denominator and radial expense.
It does not supply bounded N, bounded normalized coefficient mass or a degree-uniform Haar-to-original-root transfer on varying original inputs.
Indeed for every constructed pair the actual discrepancy obeys

    (1/d)log Norm_K(B_N(alpha))-I(S_N,T_N)
         >=log2-I(S_N,T_N),
    liminf_(N->infinity)
       [(1/d)log Norm_K(B_N(alpha))-I(S_N,T_N)]
         >=-J_G.                                   (P12)

Whenever J_G<0 this lower bound is positive.
The new flexibility achieves a favorable circle value by explicitly increasing polynomial degree and denominator; it cannot license an unpriced distribution replacement.
The [retained original norm-only comparison](Yin_C_G0587_v2.md#paid-transfer-reuse) would require a uniformly bounded ordinary degree multiplier and normalized coefficient/term-count budgets for A_N/(2D_N), or a different proved transfer budget.
Those missing bounds, and coverage by inputs whose actual J_G is useful, remain the unresolved original-object part of D36.

## Current assessment
[Selected decision](#decision-current-complete-constant-spd-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T09:35 |
| status | open |
| reason | Register the complete reusable polynomial-mixing and polynomial-shear statements with their unchanged full proofs from L437. The source proof has R445 whole coverage, while this exact Claim statement and extraction interfaces await review; no adoption or uniform-transfer conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete three-part statement](#statement) | Exact original reciprocal totally-real trace domain, matrix construction and two-control obstruction, all rational polynomial shears, full norm floor, exact unattained infimum, explicit finite-error/degree/denominator/coefficient costs and fixed-degree attainment boundary. |
| argument | [Complete local argument](#argument) | Entire M1--M8 and P1--P12 including P8a, all cases and original dates/contributions; no proof is left behind a ledger redirect. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | The exclusions e=g=0 and f=g=0 for the original nonzero integral triple, including g=0 and transformed-singleton boundaries. |
| dependency | [Actual trace and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original d=2r, quadratic K/F, integral nonzero trace quotients, unit phases and original defects. |
| dependency | [Original numerator identities](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Complete H23,H25,H35, degrees6d/10d/15d, leading coefficients1/11/7 and actual scalar denominators. |
| dependency | [Centered original interface](Yin_C_G0157_v3.md#statement) | Exact real centered functions, common L, total-real trace domain and full original norm conventions; no polynomial-parameter extension is assumed from its printed theorem. |
| dependency | [Original three-rotation reduction](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | The same two controls, exact row determinant and Lambda normalization with every scalar and multiplicity. |
| dependency | [Existing two-control certificates](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only the certified nonzero determinants and Lambda bounds for the quartic and Lehmer inputs. |
| dependency | [Complete nonmonic regularization](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Degree-D product bound with actual Mahler scale, repeated roots and all circle-zero cases, used at D=15d for H35. |
| dependency | [Existing H35 component values](../computations/programs/Yin_J_G0100/readme.md#certified-results) | J_G<-2 only on the original two controls, with the retained certified-error and no-new-run limits. |
| support | [J102 whole independent finding](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) | Existing analytic and numerical coverage of the exact reused determinant certificates; not a review of the new mixing argument. |
| support | [J100 whole independent finding](../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) | Existing scope of the reused two component values and shared numerical-library limitation. |
| support | [Constant-matrix prior boundary](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen) | Comparison only: the unchanged constant two-shear class is already excluded; variable matrices require the new local proof. |
| support | [Normalized sparse-transfer comparison](Yin_C_G0140_v1.md#argument) | Exact degree, term-count and normalized-size requirements remain unpaid uniformly for the new dense family; no new automatic coverage is imported. |
| support | [Original full author account](../ledger/Yin_L_G0437_v1.md#polynomial-mixing-direct-inputs) | Extraction provenance and complete original input/comparison scope; the selected argument is now the full proof in this Claim. |
| support | [Source-proof whole finding](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Actual whole independent review of the unchanged L437 mathematics; does not by itself review this new Claim's selected statement and extraction interfaces. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T09:51 |
| status | proved |
| authority | Internal adoption under Yin's selected continuation of the retained D36 inquiry. |
| reason | Adopt the complete unchanged polynomial-mixing and shear-infimum proof through whole R445 plus actual registered-statement/extraction R448. The clarified domain permits individual defects to vanish while retaining nonzero integral a,b,c. The two-control obstruction, rational-polynomial norm floor, exact unattained infimum, full costs and fixed-degree boundary are proved at their exact scopes; varying-input transfer remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete three-part statement](#statement) | Exact original reciprocal totally-real trace domain, matrix construction and two-control obstruction, all rational polynomial shears, full norm floor, exact unattained infimum, explicit finite-error/degree/denominator/coefficient costs and fixed-degree attainment boundary. |
| argument | [Complete local argument](#argument) | Entire M1--M8 and P1--P12 including P8a, all cases and original dates/contributions; no proof is left behind a ledger redirect. |
| dependency | [Totally real pairwise exclusions](Yin_C_G0153_v2.md#argument) | The exclusions e=g=0 and f=g=0 for the original nonzero integral triple, including g=0 and transformed-singleton boundaries. |
| dependency | [Actual trace and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original d=2r, quadratic K/F, integral nonzero trace quotients, unit phases and original defects. |
| dependency | [Original numerator identities](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Complete H23,H25,H35, degrees6d/10d/15d, leading coefficients1/11/7 and actual scalar denominators. |
| dependency | [Centered original interface](Yin_C_G0157_v3.md#statement) | Exact real centered functions, common L, total-real trace domain and full original norm conventions; no polynomial-parameter extension is assumed from its printed theorem. |
| dependency | [Original three-rotation reduction](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | The same two controls, exact row determinant and Lambda normalization with every scalar and multiplicity. |
| dependency | [Existing two-control certificates](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only the certified nonzero determinants and Lambda bounds for the quartic and Lehmer inputs. |
| dependency | [Complete nonmonic regularization](../ledger/Yin_L_G0358_v1.md#zero-compatible-root-error) | Degree-D product bound with actual Mahler scale, repeated roots and all circle-zero cases, used at D=15d for H35. |
| dependency | [Existing H35 component values](../computations/programs/Yin_J_G0100/readme.md#certified-results) | J_G<-2 only on the original two controls, with the retained certified-error and no-new-run limits. |
| support | [J102 whole independent finding](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) | Existing analytic and numerical coverage of the exact reused determinant certificates; not a review of the new mixing argument. |
| support | [J100 whole independent finding](../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) | Existing scope of the reused two component values and shared numerical-library limitation. |
| support | [Constant-matrix prior boundary](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen) | Comparison only: the unchanged constant two-shear class is already excluded; variable matrices require the new local proof. |
| support | [Normalized sparse-transfer comparison](Yin_C_G0140_v1.md#argument) | Exact degree, term-count and normalized-size requirements remain unpaid uniformly for the new dense family; no new automatic coverage is imported. |
| support | [Original full author account](../ledger/Yin_L_G0437_v1.md#polynomial-mixing-direct-inputs) | Extraction provenance and complete original input/comparison scope; the selected argument is now the full proof in this Claim. |
| support | [Source-proof whole finding](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Actual whole independent review of the unchanged L437 mathematics; does not by itself review this new Claim's selected statement and extraction interfaces. |
| review | [Whole original-proof finding](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Complete M1--M8 and P1--P12/P8a, all eleven input roles and exact original-field/scalar/degree cases. |
| review | [Registered-statement extraction finding](../audits/reviews/Yin_R_G0448_v1.md#c176-statement-extraction-finding) | Final three-part statement, entire unchanged owned proof, eight dependencies and six supports; opening-sentence clarification read back and nonblind arrangements disclosed. |


### Decision current-complete-root-error-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:22 |
| status | proved |
| reason | The unchanged complete all-root product and normalized scalar bound is now owned by C379, including its nonmonic, repeated-root, circle-zero and actual Mahler-scale cases. Retain the current statement, full argument, every other input and actual existing review scopes; the old reviewers are not described as having inspected this later proof-home placement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original reciprocal totally-real trace domain, matrix construction and two-control obstruction, all rational polynomial shears, full norm floor, exact unattained infimum, explicit finite-error/degree/denominator/coefficient costs and fixed-degree attainment boundary. |
| argument | [Exact argument](#argument) | Entire M1--M8 and P1--P12 including P8a, all cases and original dates/contributions; no proof is left behind a ledger redirect. |
| dependency | [Exact dependency](Yin_C_G0153_v2.md#argument) | The exclusions e=g=0 and f=g=0 for the original nonzero integral triple, including g=0 and transformed-singleton boundaries. |
| dependency | [Exact dependency](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original d=2r, quadratic K/F, integral nonzero trace quotients, unit phases and original defects. |
| dependency | [Exact dependency](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Complete H23,H25,H35, degrees6d/10d/15d, leading coefficients1/11/7 and actual scalar denominators. |
| dependency | [Exact dependency](Yin_C_G0157_v3.md#statement) | Exact real centered functions, common L, total-real trace domain and full original norm conventions; no polynomial-parameter extension is assumed from its printed theorem. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | The same two controls, exact row determinant and Lambda normalization with every scalar and multiplicity. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only the certified nonzero determinants and Lambda bounds for the quartic and Lehmer inputs. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Degree-D product bound with actual Mahler scale, repeated roots and all circle-zero cases, used at D=15d for H35. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0100/readme.md#certified-results) | J_G<-2 only on the original two controls, with the retained certified-error and no-new-run limits. |
| support | [Exact support](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) | Existing analytic and numerical coverage of the exact reused determinant certificates; not a review of the new mixing argument. |
| support | [Exact support](../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) | Existing scope of the reused two component values and shared numerical-library limitation. |
| support | [Exact support](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen) | Comparison only: the unchanged constant two-shear class is already excluded; variable matrices require the new local proof. |
| support | [Exact support](Yin_C_G0140_v1.md#argument) | Exact degree, term-count and normalized-size requirements remain unpaid uniformly for the new dense family; no new automatic coverage is imported. |
| support | [Exact support](../ledger/Yin_L_G0437_v1.md#polynomial-mixing-direct-inputs) | Extraction provenance and complete original input/comparison scope; the selected argument is now the full proof in this Claim. |
| support | [Exact support](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Actual whole independent review of the unchanged L437 mathematics; does not by itself review this new Claim's selected statement and extraction interfaces. |
| review | [Exact review](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Complete M1--M8 and P1--P12/P8a, all eleven input roles and exact original-field/scalar/degree cases. |
| review | [Exact review](../audits/reviews/Yin_R_G0448_v1.md#c176-statement-extraction-finding) | Final three-part statement, entire unchanged owned proof, eight dependencies and six supports; opening-sentence clarification read back and nonblind arrangements disclosed. |


### Decision current-complete-constant-spd-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:31 |
| status | proved |
| reason | The complete unchanged constant-matrix comparison proof is now retained in C486, including all SPD/determinant/logarithmic-zero/matrix-entry denominator and finite-input/arithmetic limits. Preserve the selected statement/argument, every mathematical assessment and other relation, all original review scopes and historical facts; the old reviewers are not described as having read this later proof-home placement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original reciprocal totally-real trace domain, matrix construction and two-control obstruction, all rational polynomial shears, full norm floor, exact unattained infimum, explicit finite-error/degree/denominator/coefficient costs and fixed-degree attainment boundary. |
| argument | [Exact argument](#argument) | Entire M1--M8 and P1--P12 including P8a, all cases and original dates/contributions; no proof is left behind a ledger redirect. |
| dependency | [Exact dependency](Yin_C_G0153_v2.md#argument) | The exclusions e=g=0 and f=g=0 for the original nonzero integral triple, including g=0 and transformed-singleton boundaries. |
| dependency | [Exact dependency](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original d=2r, quadratic K/F, integral nonzero trace quotients, unit phases and original defects. |
| dependency | [Exact dependency](Yin_C_G0149_v1.md#original-polynomials-and-norms) | Complete H23,H25,H35, degrees6d/10d/15d, leading coefficients1/11/7 and actual scalar denominators. |
| dependency | [Exact dependency](Yin_C_G0157_v3.md#statement) | Exact real centered functions, common L, total-real trace domain and full original norm conventions; no polynomial-parameter extension is assumed from its printed theorem. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | The same two controls, exact row determinant and Lambda normalization with every scalar and multiplicity. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only the certified nonzero determinants and Lambda bounds for the quartic and Lehmer inputs. |
| dependency | [Exact dependency](Yin_C_G0379_v1.md#zero-compatible-root-error) | Degree-D product bound with actual Mahler scale, repeated roots and all circle-zero cases, used at D=15d for H35. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0100/readme.md#certified-results) | J_G<-2 only on the original two controls, with the retained certified-error and no-new-run limits. |
| support | [Exact support](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding) | Existing analytic and numerical coverage of the exact reused determinant certificates; not a review of the new mixing argument. |
| support | [Exact support](../audits/reviews/Yin_R_G0379_v1.md#two-input-h35-finding) | Existing scope of the reused two component values and shared numerical-library limitation. |
| support | [Exact support](Yin_C_G0486_v1.md#constant-spd-determinant-screen) | Comparison only: the unchanged constant two-shear class is already excluded; variable matrices require the new local proof. |
| support | [Exact support](Yin_C_G0140_v1.md#argument) | Exact degree, term-count and normalized-size requirements remain unpaid uniformly for the new dense family; no new automatic coverage is imported. |
| support | [Exact support](../ledger/Yin_L_G0437_v1.md#polynomial-mixing-direct-inputs) | Extraction provenance and complete original input/comparison scope; the selected argument is now the full proof in this Claim. |
| support | [Exact support](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Actual whole independent review of the unchanged L437 mathematics; does not by itself review this new Claim's selected statement and extraction interfaces. |
| review | [Exact review](../audits/reviews/Yin_R_G0445_v1.md#polynomial-mixing-whole-independent-finding) | Complete M1--M8 and P1--P12/P8a, all eleven input roles and exact original-field/scalar/degree cases. |
| review | [Exact review](../audits/reviews/Yin_R_G0448_v1.md#c176-statement-extraction-finding) | Final three-part statement, entire unchanged owned proof, eight dependencies and six supports; opening-sentence clarification read back and nonblind arrangements disclosed. |

