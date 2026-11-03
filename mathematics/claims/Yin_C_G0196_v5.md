---
author: Yin
---
# All-width integral trace representatives and complete canonical Haar costs

Date: 2026-10-20T15:11.
Human author Yin.
This fifth fixed version preserves physical [v1](Yin_C_G0196_v1.md#statement), [v2](Yin_C_G0196_v2.md#statement), [v3](Yin_C_G0196_v3.md#statement) and [v4](Yin_C_G0196_v4.md#statement), every earlier mathematical argument and its actual source/review/adoption scope.
Root and draft_inventory_later authored the complete canonical K1--K11 screen on2026-10-20T12:29.
It is retained in full below, including the weighted cyclotomic target and original width-cost limits.
Root proposed the all-width extension and trace-order consequence; draft_comparison_cleanup supplied the complete AW1--AW8 verification on2026-10-20T14:51.
Both are contributors to that extension.
The earlier D36 paid-transfer paragraph already identified the norm-only specialization of C140.
Here draft_comparison_cleanup reconstructs its complete fixed proof and constants, crediting root's C140 two-case analytic mechanism and its accepted inputs.
The present statement and assembly are authored by draft_comparison_cleanup under root coordination; none of these roles is an independent review of this version.
C198 was pending when AW was first written; its actual adopted v1 and R480 are now the fixed input.
The older C196v4 joint budget is reused through actual R478, not relabelled as a new cutoff.
No mathematical program, parameter scan, source acquisition, actual residual realization or cutoff increment is supplied.

<a id="statement"></a>
## Complete statement and distinct thresholds

Let P in Z[z] be monic, irreducible, reciprocal and nontorsion, of degree d=2r and constant coefficient1.
For a root alpha set K=Q(alpha), delta=alpha+alpha^(-1), assume F=Q(delta) totally real, and let T in Z[X] be its actual monic minimal polynomial of degree r.
Thus P(z)=z^r T(z+z^(-1)) and[K:F]=2.
For p in{2,3,5} use theta_p=rem_T T(C_p)/p in Z[X], where C_p(z+z^(-1))=z^p+z^(-p), and put

    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    s in{1,-1}, x=e+s g,
    A_tr=Z[delta], O=O_F, J=[O:A_tr],
    t_2=dim_(F_2) O/(A_tr+2O),
    I_*=(12/11)log2.

The nonzero integral a,b,c are quotients of this SAME actual T.
All logarithmic Haar means below use circle probability, with no division by the original or auxiliary degree.

**A. Every integral representative, at every degree.**
For ANY R_1,R_2,R_3 in Z[X] satisfying R_1(delta)=x, R_2(delta)=f, R_3(delta)=g, let B_R be the sum of their squared pullbacks at z+z^(-1), let I_R=integral log B_R, and let k count the nonzero POLYNOMIALS.
Then k>=1, I_R is finite, B_R(alpha)=Q_s=x^2+f^2+g^2 with Norm_K Q_s>=2^d, and

    I_R>=log k+(2/k)sum_(R_j!=0)
              m(z^(deg R_j)R_j(z+z^(-1)))>=log k.

Consequently I_R<log2 forces R_1=R_2=0 as polynomials, R_3(delta)=g!=0 and the full actual residual equations f=e+s g=0.
R_3 must be nonconstant and have leading coefficient1 or-1.
The adopted C198 theorem then forces t_2>=ceil(r/11) and v_2(J)>=ceil(r/11).
If t_2<ceil(r/11), or v_2(J)<ceil(r/11), EVERY such triple has k>=2 and I_R>=log2 at every degree; odd J is a special case.
This concerns individual component values, not merely their squared sum, arbitrary changes of those values, rational coefficients, unequal weights or a changed normalization.

**B. Complete canonical screen and costs.**
Let Xbar,Fbar,Gbar be the unique integer representatives of x,f,g of degree below r.
Their sum of squared pullbacks has the same component-count screen.
The only possible sub-log2 branch has Xbar=Fbar=0 and actual full residual g!=0.
All remaining assertions in part B concern that full residual single-component branch.
A constant Gbar already has Haar mean at least2log2.
For w=deg Gbar>=1 set H_G=z^w Gbar(z+z^(-1)); only in this CANONICAL setting does deg H_G=2w<=d-2.
Then

    I_can=2m(H_G),
    Res(P,H_G)=Norm_F(g)^2>=2^(6d/11),
    (1/d)log Norm_K(B_can(alpha))>=I_*.

The residual threshold I_* is distinct from the strict log2 baseline in A.
If I_can<I_*, then H_G is monic up to sign, reciprocal with constant coefficient1 after that sign, and has no nonreciprocal irreducible factor.
I_can=0 holds exactly when H_G, after that common sign, is a product of cyclotomic polynomials with multiplicity, equivalently Gbar is monic up to sign and all its roots lie in[-2,2].
The complete K1--K11 proof retains all scalar, norm, factor, primitive-field, linear-form, bounded-width and cyclotomic-order qualifications.
In particular[F:Q(g)]<=w and H=Q(a,b,c)=Q(a) is contained in F; no general equality F=H or H=Q(g) is asserted.
The original five-form linear necessary screen remains such a screen; it does not undo the later adopted low-degree exclusion.

**C. Fixed canonical width and fixed margin have a paid gap.**
For fixed integer W>=1 and eta>0, canonical residual inputs with w<=W and I_can<=I_*-eta have a positive uniform original Mahler lower bound.
The exact rational auxiliary H_G^2/q and its complete coefficient, term, norm and degree costs are retained below.
The necessary norm-only C140 application is proved here: fix integers K_0>=2,S_0>=1, C_0>0 and0<eta_0<=1.
For nonzero u in Q[z] with1<=deg u<=C_0d, at most K_0 terms, ||u||_1<=S_0, m(u)<=-eta_0 and |Norm_K u(alpha)|>=1, NF1--NF8 give m(P)>h_star/C_0 with the full positive constant specified.
Integrality of u(alpha) is not required, and no zero norm is used.
Thus a hypothetical canonical fixed-saving sequence with m(P)->0 must have w->infinity; no such sequence is asserted to exist.

**D. The previous dyadic boundary remains canonical.**
On the full residual branch, C196v2's repeated-factor/saturation theorem applies to EVERY integer representative of actual g.
The adopted C196v4 result says for the actual canonical G_can that a nonzero reduction modulo2 has degree at least34, allowing degree drop.
Canonical w<=33 forces all coefficients even and I_can>=2log2.
No new cutoff, actual degree34 realization or extension of that coefficient statement to arbitrary higher-degree representatives is made.

These results do not exclude all remaining even-index inputs or all canonical widths.
They supply no uniform upper comparison for the complete signed rational-regularizer discrepancy and do not complete G0001.

<a id="argument"></a>
## Complete proofs

<a id="canonical-integral-trace-remainder-screen"></a>
## Complete original canonical K1--K11 account

Original author date: 2026-10-20T12:29.
Root proposed the screen and draft_inventory_later checked its full body, residual factorization and original-field costs.
Every K1--K11 derivation follows; only the mutable transfer invocation is replaced by the complete fixed norm-only proof below, with its parameter application explicit.
Scalar Jensen/Kronecker and the Smyth bound use the accepted Smy08-U001/U002 statements at their unchanged source-proof inspection limits.
The original norm input is adopted C191v2, not an abstract arbitrary-triple conjecture.

### The actual integer components and the nonresidual obstruction
Keep the exact original domain of C191v2: P has degree d=2r, delta=alpha+alpha^(-1), F=Q(delta) is totally real, and T is its actual monic integer minimal polynomial.
For p=2,3,5 put

    theta_p(X)=rem_T(T(C_p(X)))/p in Z[X].

Coefficientwise integrality follows before evaluation: modulo p one has C_p(X)=X^p and T(X^p)=T(X)^p, so monic division by T has remainder divisible coefficientwise by p.
Thus a=theta_2(delta), b=theta_3(delta), c=theta_5(delta) are the original quotient values, with no change of generator or maximal-order assumption.
Form the integer polynomials e_0=theta_3^2-theta_2^3, f_0=2theta_5^2-3theta_2^5 and g_0=theta_5^3-2theta_3^5.
For the fixed sign s put

    Xbar=rem_T(e_0+s g_0), Fbar=rem_T(f_0),
    Gbar=rem_T(g_0), all of degree<r.              (K1)

The zero remainder is allowed.
Because T is minimal, each remainder is zero exactly when its value at delta is zero.
For any nonzero one of these integer polynomials R, the pullback R(z+z^(-1)) is a nonzero integer Laurent polynomial: its outer coefficients are the nonzero leading coefficient of R.
It is real on the unit circle.
Let R_1,R_2,R_3 be these three pullbacks, and define

    B_can(z)=R_1(z)^2+R_2(z)^2+R_3(z)^2,
    B_can(alpha)=Q_s,
    I_can=integral_T log B_can dmu.               (K2)

There is at least one nonzero component by C153v2's pairwise exclusions.
The zeros of this nonzero nonnegative Laurent polynomial are finite and of finite order, so the logarithm is integrable.
If k of the components are nonzero, pointwise AM-GM off their finite zero sets and scalar Jensen give

    I_can>=log k+(2/k)sum_(R_j!=0)m(R_j)
          >=log k.                               (K3)

Here m of a Laurent polynomial means the normalized Haar logarithm of its modulus.
Multiplication by a monomial makes it an ordinary nonzero integer polynomial, whose Mahler measure is at least1.
This is the reason for the second inequality, not a comparison of the original conjugates with Haar.

Consequently EVERY canonical form with at least two nonzero components fails the strict baseline target I_can<log2.
C153v2 excludes the sole-Xbar case, since it would have f=g=0, and the sole-Fbar case, since it would have e=g=0.
The only remaining single component is Gbar, precisely when

    f=e+s g=0, g!=0, B_can(z)=Gbar(z+z^(-1))^2.   (K4)

The all-input arithmetic floor Norm_K(Q_s)>=2^d therefore does not make canonical reduction an automatic favorable-Haar construction.
This conclusion concerns the stated log2 baseline.
It does not exclude a different comparison using actual arithmetic income larger than that baseline.

### The remaining polynomial, full norm and possible factor types

In(K4), if Gbar is a constant k, it is a nonzero rational integer.
The original-root and Haar means then agree exactly at2log|k|.
C191v2 gives |k|>=2, so this constant case has no useful discrepancy or saving from its guaranteed norm income.
Now let w=deg Gbar>=1 and define

    H_G(z)=z^w Gbar(z+z^(-1)) in Z[z],
    deg H_G=2w<=2r-2=d-2,
    I_can=2m(H_G).                                (K5)

H_G is reciprocal, with equal nonzero leading and constant coefficients.
It is coprime to the irreducible degree-d P because its degree is smaller.
The exact original evaluation H_G(alpha)=alpha^w g and Norm_K(alpha)=1 give

    Res(P,H_G)=Norm_F(g)^2>=2^(6d/11),
    (1/d)log Norm_K(B_can(alpha))
      =(2/r)log|Norm_F(g)|>=I_*,
    I_*=(12/11)log2.                              (K6)

Every original conjugate and the quadratic tower are retained.
The candidate can therefore be compared with the stronger guaranteed residual threshold I_*, not only log2.
The statements below use the necessary condition I_can<I_*; they also apply to the narrower target I_can<log2.

That inequality forces m(H_G)<(6/11)log2<log2.
Jensen's leading-coefficient bound consequently forces the leading coefficient of Gbar to be1 or-1.
After an irrelevant common sign, H_G is a monic reciprocal integer polynomial with constant1.
Kronecker's accepted characterization gives the exact zero-Haar alternative

    I_can=0 iff H_G is a product of cyclotomic
    polynomials, with multiplicities.             (K7)

There is no monomial factor because its constant coefficient is1.
Equivalently, Gbar is monic up to sign and every one of its roots, counted with multiplicity, lies in[-2,2].
The equivalence follows by solving z+z^(-1)=x at each root x of Gbar.
Neither g!=0, nor the large original norm in(K6), nor the [field-generation theorem C188](Yin_C_G0188_v1.md#statement) excludes this alternative.

There is also a useful complete exclusion of nonreciprocal factors in the remaining low-Haar range.
If the monic reciprocal H_G has a nonreciprocal irreducible factor A, it also has its distinct monic reciprocal partner A^* with the same multiplicity.
Both are nonzero integer-unit polynomials and have the same Mahler measure.
The already accepted Smyth theorem gives

    m(H_G)>=2log(theta_0)>(6/11)log2,
    theta_0^3=theta_0+1>2, theta_0>1.              (K8)

The strict comparison follows from2log(theta_0)>(2/3)log2>(6/11)log2.
Thus this pair is incompatible with I_can<I_*.
Every surviving noncyclotomic irreducible factor must itself be reciprocal.
For those reciprocal factors there is no newly proved positive measure bound large enough to eliminate the remaining window.
Declaring them noncyclotomic would not by itself supply such a bound.

### Primitive fields, degree escape and the next controlled object

For w>=1, delta is a root of the degree-w polynomial Gbar(X)-g over Q(g), hence

    [F:Q(g)]<=w.                                  (K9)

For the actual residual triple C188 gives H=Q(a,b,c)=Q(a), and Q(g) is a subfield of H contained in F.
Therefore [F:H]<=[F:Q(g)]<=w.
This does not establish F=H or F=Q(g) for general w.
For w=1 it does establish F=H=Q(g)=Q(a).
If this degree-one canonical remainder meets I_can<I_*, it must be one of

    Gbar(X)=+/-(X-k), k in{-2,-1,0,1,2}.           (K10)

Indeed the leading coefficient is already restricted to a sign; if the integer |k|>=3, the larger root of z^2-kz+1 has modulus greater than2, contradicting m(H_G)<(6/11)log2.
The five forms surviving this leading-coefficient screen are cyclotomic after the reciprocal pullback.
This is an exact all-degree necessary classification for this smallest canonical width, not a parameter scan or an existence assertion.
The later adopted C196v4 already excludes a useful saving at this canonical width; preserving the original necessary list does not reopen those forms as actual candidates.

All fixed bounded values of w with a fixed useful saving are already within the paid sparse-transfer interface; they do not supply an unbounded-degree escape from it.
More precisely, fix W and eta>0 and suppose w<=W and I_can<=I_*-eta.
Choose once a positive rational q with exp(I_*-eta/2)<q<exp(I_*).
Then A=H_G^2/q is a rational ordinary polynomial with nonzero original norm at least1 by(K6), m(A)<=-eta/2, and degree4w<2d.
The coefficient bound |h_j|<=binom(2w,j)M(H_G), applied to its root factorization, gives

    ||H_G||_1<=2^(2W)exp(I_*/2),
    ||A||_1<=2^(4W)exp(I_*)/q,
    number of terms of A<=4W+1.

These are uniform bounds once W and eta are fixed.
The complete [norm-only sparse-transfer proof](#norm-only-sparse-transfer) below therefore gives its positive original-measure gap on this specified class, using K_0=4W+1, C_0=2, an integer S_0 at least the displayed l1 bound, and eta_0=min{eta/2,1}.
This uses the full proof-level adaptation in this fixed version, not an assertion that C140's printed integral-value statement already has the larger norm-only scope.
In particular a hypothetical sequence with m(P) tending to0 and this fixed saving would require w tending to infinity.
Neither such a sequence nor useful savings at unbounded w are asserted to exist.

The most discriminating unclosed next object is consequently the unbounded-degree cyclotomic-or-reciprocal factor structure of this SAME canonical Gbar, with its exact original resultant income.
For the zero-Haar alternative write

    H_G=product_n Phi_n^(a_n),
    sum_n a_n phi(n)=2w<d,
    sum_n a_n log|Res(P,Phi_n)|
       =2log|Norm_F(g)|>=(6d/11)log2.             (K11)

Only finitely many a_n are nonzero.
Here Phi_n is the n-th cyclotomic polynomial and phi(n)=deg(Phi_n).
The multiplicities a_1 and a_2 are even because z+z^(-1)-2 and z+z^(-1)+2 have double zeros at1 and-1.
All resultants are nonzero, and the identity retains their original multiplicities.
It is an exact cyclotomic-factor target, not a claim that any such auxiliary is attained by the actual quotient.

The next bounded theoretical test should use the actual divided self-composition and residual equations to control this weighted cyclotomic resultant expression, or to exclude the monic canonical remainder required before(K7).
A first precise order-level question is whether those equations force nontrivial coefficient content or a leading coefficient of absolute value at least2 in Gbar; the norm floor alone does not imply either.
If neither exclusion holds, any useful phase comparison must retain the full degree budget in(K11), the actual cyclotomic orders and their multiplicities.
Replacing phi(n) by n or assuming the orders stay bounded would introduce an unpaid cost.
The analogous noncyclotomic branch must retain the positive m(H_G) in its margin instead of using the zero-Haar identity.
This screen supplies no new grid, root search, general canonical-Haar exclusion or unrestricted Mahler conclusion.

<a id="norm-only-sparse-transfer"></a>
## Complete C140 application with original norm income only

The actual [C140 Sections1--3](Yin_C_G0140_v1.md#argument), with [R801's exact whole scope](../audits/reviews/Yin_R_G0801_v1.md#normalized-sparse-cost-whole-independent-finding), supplies the two-case analytic mechanism.
Its printed arithmetic hypothesis is an integral normalized value.
The complete application here proves why only a nonzero FULL original norm at least1 is needed, without a mutable-draft premise.

Fix integers K_0>=2,S_0>=1, C_0>0 and0<eta_0<=1.
Let P be a monic irreducible nontorsion integer unit of degree d>=2, let K=Q(alpha), and suppose u in Q[z] has degree1<=D_u<=C_0d, at most K_0 nonzero terms, and

    ||u||_1<=S_0, m(u)<=-eta_0,
    |Norm_(K/Q)u(alpha)|>=1.                       (NF1)

Thus every original conjugate value is nonzero, but its integrality and integer coefficients of u are not assumed.
Put beta=1/(K_0-1), D_beta=1/beta+1/(2-beta), and retain the absolute A>=1 from [BS13-U001](../audits/literature/BS13/Yin_U001.md#bs13-u001).
Its pure-imaginary measurable-set statement and ordinary-supremum convention are the only source use; the original proof and a numerical universal A are not supplied.
Choose

    L_reg=ceil(max{1,4/sqrt(eta_0),
              [16A exp(beta/2)D_beta/eta_0]^(1/beta)}),
    rho=1/L_reg, a_0=exp(-eta_0/2), B_0=S_0^2+1,
    M_0=ceil(8B_0/(eta_0 rho^2)).                  (NF2)

Then rho is positive rational, rho<=1, rho^2<=eta_0/16 and A exp(beta/2)D_beta rho^beta<=eta_0/16.
All constants are fixed before choosing P,u.
If sup_circle|u|>=a_0, the BS13 pure-imaginary substitution gives, for0<t<=a_0 and actual term count n>=2,
mu{|u|<=t}<=A(t/a_0)^(1/(n-1))<=A(t/a_0)^beta.
For t>a_0 use the trivial measure bound1; a monomial is handled directly by its constant modulus.
Thus the same sublevel bound A exp(beta/2)t^beta holds for every t>0.
The nonnegative layer-cake identity and Tonelli give

    integral (1/2)log(1+rho^2/|u|^2)
      <=A exp(beta/2)rho^beta
                    integral_0^infinity v^(beta-1)/(1+v^2) dv
      <=A exp(beta/2)D_beta rho^beta<=eta_0/16.

The integral is bounded by splitting at1 and integrating v^(beta-1) and v^(beta-3).
Both converge because0<beta<=1.
The polynomial's finite circle zeros have measure zero and integrable logarithms.
Hence in this case the regularized mean integral log(|u|^2+rho^2)/2 is at most-15eta_0/16.
If sup_circle|u|<a_0 instead, pointwise |u|^2+rho^2<=exp(-eta_0)+rho^2<exp(-eta_0/2), since
exp(-eta_0/2)-exp(-eta_0)>=eta_0/(2e)>eta_0/16.
The regularized mean is then below-eta_0/4.
The common upper bound is therefore-eta_0/4, without assuming uniform approximation to m(u) in the small-supremum case.

On the circle set H=|u|^2+rho^2, Y=1-H/B_0 and

    Phi=(log B_0)/2-(1/2)sum_(j=1)^(M_0)Y^j/j,
    c_Phi=integral Phi dmu.

Here0<=Y<=1-rho^2/B_0<1, and the nonnegative omitted log-series tail is at most B_0/[2(M_0+1)rho^2]<=eta_0/16.
Consequently

    (1/2)log H<=Phi, c_Phi<=-3eta_0/16.            (NF3)

The Laurent coefficient l1 norm of Y is at most2.
The nonconstant Fourier coefficient sum of Phi is less than2^(M_0), and all frequencies have absolute value at most M_0D_u.
A finite-matrix realization, if used, retains size2M_0D_u+1; no matrix is executed or given a degree-free size.
All nonconstant coefficients are rational, but their possibly large denominators supply no arithmetic income.

Write r_i=|alpha_i|, z_i=alpha_i/r_i, m=m(P)>0, h=D_u m/d, and V_i=u(alpha_i)/max(1,r_i)^(D_u).
The original unit identities give sum_i log^+r_i=m and sum_i|log r_i|=2m.
Coefficient comparison, using r_i^j for contracting roots and r_i^(j-D_u) for expanding ones, yields
|V_i-u(z_i)|<=S_0 min{1,D_u|log r_i|}.
The function t->log(t^2+rho^2)/2 on t>=0 has derivative at most1/(2rho).
It follows, with all d original roots, that

    (1/d)sum_i log|u(alpha_i)|
       <=(1+S_0/rho)h+(1/d)sum_i Phi(z_i).         (NF4)

For the angular part use the actual [L229 interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence).
Put c_ang=log2/4, h_0=c_ang exp(-20) and, for0<v<=h_0,

    b(v)=max{v,sqrt(v/c_ang)log sqrt(c_ang/v)},
    epsilon(v)=min{1,15sqrt(b(v))+4v}.

This increasing function tends to zero.
For0<M_0h<=h_0 it bounds every original angular mean at nonzero frequency of absolute value at most M_0D_u.
The accepted input retains the actual powered-field degree and every repeated original embedding; no degree-preserving assumption is added.
Thus

    (1/d)log|Norm_K u(alpha)|
       <=c_Phi+(1+S_0/rho)h
                             +2^(M_0)epsilon(M_0h). (NF5)

Choose the least integer ell>=32 for which

    h_star=(c_ang/M_0)2^(-ell),
    (1+S_0/rho)h_star<=eta_0/32,
    2^(M_0)epsilon(M_0h_star)<=eta_0/32.            (NF6)

Such an ell exists and M_0h_star<h_0 because32log2>20.
It defines a positive input-independent constant at the fixed budgets, without a numerical search.
If0<h<=h_star, then(NF1),(NF3),(NF5) contradict each other:

    0<=(1/d)log|Norm_K u(alpha)|
      <=-3eta_0/16+eta_0/32+eta_0/32
       =-eta_0/8<0.                              (NF7)

This is precisely the only place where C140 used integrality of its normalized value.
Here the full norm assumption supplies the same inequality.
Therefore

    m(P)>h_star/C_0>0.                            (NF8)

A constant or monomial with negative logarithmic cost cannot satisfy(NF1), since the unit norm forces its rational scalar to have modulus at least1.
No zero-value closure or logarithm of a zero norm is invoked.
This retains every finite term, coefficient, radial, frequency and source-constant cost.

In the canonical application take u=H_G^2/q with the fixed rational q in the K proof, D_u=4w<2d, K_0=4W+1, C_0=2, S_0=ceil(max{1,2^(4W)exp(I_*)/q}) and eta_0=min{eta/2,1}.
The exact full norm is at least exp(d I_*)/q^d>1, and m(u)<=-eta/2<=-eta_0.
Its term and coefficient bounds are the explicitly derived ones above, not an unpaid consequence of width alone.
If the class is nonempty then w>=1, so positive degree is automatic; an empty class requires no witness.
All constants are uniform once W and eta are fixed, with q retained in both the norm and coefficient prices.


<a id="all-width-integral-trace-representative-screen"></a>
## All integral trace representatives: the component count and index obstruction

Original author proof date: 2026-10-20T14:51.
Human author Yin.
Root proposed extending the canonical component-count screen to every integral representative and combining its residual implication with the new trace-order index theorem.
Draft_comparison_cleanup supplied the complete all-degree verification below, including zero polynomials versus zero field values, constant representatives, the precise preserved-value hypothesis and the limits of the canonical comparison.
Both contribute to this extension; it is author work, not an independent review.
The earlier canonical K1--K11 account remains the author-level account of its additional degree, factor and transfer conclusions.
The proof below is self-contained at its changed representative quantifiers and uses the fixed inputs explicitly identified here, not an unproved implication from a mutable draft.
The original proof treated C198 as pending; in this fixed version its [actual adopted decision](Yin_C_G0198_v1.md#decision-whole-reviewed-2026-10-20) and [whole R480 finding](../audits/reviews/Yin_R_G0480_v1.md#dyadic-trace-order-image-whole-finding) resolve the input to AW7--AW8.
This is a new consumer, not an independent re-review or prospective extension of R480.
No mathematical program, coefficient enumeration, new finite-degree cutoff or source acquisition is used.

### Complete original domain and componentwise preservation

Let P in Z[z] be monic, irreducible, reciprocal and nontorsion, of degree d=2r and constant coefficient1.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), assume F=Q(delta) is totally real, and let T in Z[X] be its actual monic minimal polynomial of degree r.
Thus P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use the [actual C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain):

    theta_p=rem_T T(C_p)/p in Z[X], p in{2,3,5},
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,
    x=e+s g, s in{1,-1}.                         (AW1)

Here C_p(z+z^(-1))=z^p+z^(-p), and a,b,c are the actual nonzero integral quotient values of this SAME input.
In this section x denotes a field element; X denotes the polynomial variable.
C153v2 proves the totally real pair exclusions(e,g)!=(0,0) and(f,g)!=(0,0).
In particular the field vector(x,f,g) is nonzero.

Choose ANY triple of integer polynomials R_1,R_2,R_3 in Z[X], of arbitrary degrees and coefficient sizes, subject only to the componentwise identities

    R_1(delta)=x, R_2(delta)=f, R_3(delta)=g.
    S_j(z)=R_j(z+z^(-1)),
    B_R(z)=S_1(z)^2+S_2(z)^2+S_3(z)^2,
    I_R=integral_(|z|=1) log B_R(z) dmu,
    k=#{j:R_j is not the zero polynomial}.       (AW2)

Mu is Haar probability and logarithms are natural.
Zero polynomials are allowed, but the nonzero field vector implies k>=1.
Each S_j is real on the circle, and a nonzero R_j has nonzero pullback because its outer Laurent coefficients equal its nonzero leading coefficient.
Consequently B_R is nonnegative and not identically zero.
Its original value is exactly Q_s=x^2+f^2+g^2 at alpha and at every original conjugate.
Thus the [adopted C191v2 full original norm](Yin_C_G0191_v2.md#statement) gives

    Norm_(K/Q)(B_R(alpha))
       =Norm_(F/Q)(Q_s)^2>=2^d.                 (AW3)

The original degree is d, and no monomial phase, component denominator, weight or rescaling has been introduced.
The field value Q_s is positive in every real trace embedding by the pair exclusions.
Its norm income does not itself bound I_R from above.

### The component-count inequality is independent of every degree

For every nonzero R_j put w_j=deg R_j>=0 and form the ordinary polynomial

    H_j(z)=z^(w_j)R_j(z+z^(-1)) in Z[z],
    deg H_j=2w_j.

Its leading and constant coefficients are the nonzero integer leading coefficient of R_j, including the constant-polynomial case w_j=0.
The [accepted scalar Jensen normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) gives

    integral log|S_j| dmu=m(H_j)>=0.              (AW4)

Circle zeros have integrable logarithmic singularities.
Also log B_R is integrable: it is bounded above on the compact circle and bounded below almost everywhere by2log|S_j| for any one nonzero component.
Off the finite union of the nonzero components' zero sets, arithmetic-geometric mean gives

    B_R>=k product_(R_j!=0)|S_j|^(2/k),
    I_R>=log k+(2/k)sum_(R_j!=0)m(H_j)
        >=log k.                                (AW5)

All quantities being integrated are integrable by the preceding argument, so deleting those finite zero sets loses no Haar mass or term.
The last inequality uses integer coefficients, not integrality of a selected field value alone.
No bound on w_j, no common support window and no comparison between original conjugates and Haar is a premise.
In particular k>=2 excludes the strict baseline I_R<log2 at EVERY degree.

### The only possible strict-saving branch preserves g alone

If k=1 and its sole nonzero polynomial is R_1, then f=g=0, contradicting the C153v2 pair exclusion.
If its sole nonzero polynomial is R_2, then x=g=0, so e=g=0, again a contradiction.
Therefore(AW5) proves the exact necessary implication

    I_R<log2
      => R_1=R_2=0 as polynomials,
         R_3!=0, R_3(delta)=g!=0,
         f=e+s g=0,
         I_R=2m(z^w R_3(z+z^(-1))), w=deg R_3.
                                                     (AW6)

The nonzero value g follows because otherwise the entire field vector would vanish.
The converse is not asserted: a full residual input does not guarantee a representative with small Haar logarithm.
Even on a full residual input, arbitrary nonzero multiples of T may be chosen for R_1 or R_2; they vanish at delta but still count as nonzero circle components and may trigger(AW5).

If R_3 were a constant h in the strict-saving branch, h would be a nonzero integer.
Equation(AW3) would give |h|^(2d)>=2^d, hence |h|>=2, and I_R=2log|h|>=2log2.
Thus a strict-saving representative in(AW6) necessarily has w>=1.
Its leading coefficient must be1 or-1, since(AW4) and I_R<log2 give m(H_3)<(log2)/2 and hence absolute leading coefficient below2.
These are necessary conditions, not a realization of the remaining class.

### Adopted index consequence and the all-width excluded class

Set A_tr=Z[delta], O=O_F, J=[O:A_tr], and t_2=dim_(F_2)O/(A_tr+2O).
Invoke only the exact adopted [C198v1 statement](Yin_C_G0198_v1.md#statement): full actual residual equations with g!=0 imply t_2>=ceil(r/11) and v_2(J)>=t_2.
Together with(AW6), this gives the conclusion

    I_R<log2 => t_2>=ceil(r/11),
               v_2(J)>=ceil(r/11).               (AW7)

The same adopted input gives the following stronger class formulation: on EVERY original input with

    t_2<ceil(r/11), or v_2(J)<ceil(r/11),

every triple(AW2), at every degree, satisfies

    k>=2 and I_R>=log2.                           (AW8)

Indeed either index inequality excludes the full residual system; C153v2 already excludes the other two possible one-component cases, so every such triple has at least two nonzero polynomials.
In particular(AW8) holds throughout the odd-J class, because v_2(J)=0 and r>=1.
No upper degree, coefficient height, small-m(P) premise or canonical-remainder assumption occurs in this class-wide obstruction.
It is a statement about the strict log2 baseline, not a uniform Mahler gap or an exclusion of comparisons that use a stronger actual original income.

### Precise relation to canonical representatives and changed sums

Monic division and minimality of T give R_j=R_(j,can)+T A_j with A_j in Z[X], where R_(j,can) is the unique representative of the same component value of degree below r.
The k in(AW5) counts the chosen polynomials, not the nonzero canonical remainders and not merely the nonzero field values.
Therefore the canonical argument is included, while the new statement also permits every higher-degree integer representative without silently replacing it by its remainder inside the Haar integral.

On the branch(AW6), [C196v2's adopted general-representative congruence and multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) apply to that actual R_3 at any degree.
The [adopted C196v4 degree34 consequence](Yin_C_G0196_v4.md#statement) instead concerns the canonical remainder G_can and its reduction.
It does not assert that a higher-degree R_3 has the same leading coefficient, parity or Haar logarithm as G_can.
The present all-width argument makes no new canonical cutoff and does not replace that distinction.

Finally, preserving only the value of the SUM of squares is a weaker requirement than(AW2).
For an arbitrary integral polynomial triple whose squared values sum to Q_s, the elementary inequality(AW5) still holds, but a surviving sole component would only have square Q_s.
Without the three individual value identities, it cannot be identified with g and the residual equations do not follow.
Accordingly(AW6)--(AW8) do not apply to an arbitrary matrix transformation that changes those component values, even if it preserves their squared sum or its norm.
A transformation that does preserve all three individual values is already covered by(AW2).
For rational-coefficient representatives the integer Jensen floor in(AW4) is not available as stated.
Unequal weights or a changed normalized form alter the sum comparison(AW5) even when the individual polynomials remain integral, so their actual scalar, weight and denominator costs must be retained.
The unresolved integral representative class is consequently narrowed by(AW6)--(AW7), not eliminated at all possible even indices.

<a id="retained-canonical-dyadic-boundary"></a>
## Exact inherited dyadic boundary and remaining scope

The adopted C196v2 theorem gives EVERY integer representative R of actual residual g the full support/saturation condition ord_phi Rbar>=min{3,N_phi}, and exact unsaturated order3ord_phi theta_5bar.
Its earlier valuation proof, squarefree impossibility, source and scalar limits stay in the physical version and actual R473.
C196v4 with actual R478 retains the degree34/nonzero-reduction conclusion and all-coefficient evenness with Haar>=2log2 at canonical w<=33, at every original measure and with no realization at34.
These are fixed inputs, not newly reconstructed residue graphs or a cutoff increment.

Canonical w<r, coprimality from deg H_G<d, degree4w<2d in the sparse application, and the weighted K11 degree sum are not statements about arbitrary higher-degree representatives.
The all-width AW theorem needs none of those upper bounds, but leaves the allowed even-index residual single-component question open.
The complete threshold must remain visible: log2 for the baseline screen, or I_* with its full residual income and separately paid original transfer.
Neither a bare large order index nor favorable Haar cost alone supplies that transfer.


<a id="exact-inputs"></a>
## Exact inputs and review boundaries

| Input | Exact role |
| --- | --- |
| [Actual trace and pairwise proof](Yin_C_G0153_v2.md#argument) | Same P/K/F/T, nonzero integer quotient values, totally real pair exclusions and full quadratic-tower phases. |
| [Actual arithmetic income](Yin_C_G0191_v2.md#statement) | Full original2^d baseline and residual Norm_F(g)>=2^(6r/11), giving I_* without losing any conjugate or degree factor. |
| [Primitive residual triple field](Yin_C_G0188_v1.md#statement) | Only H=Q(a,b,c)=Q(a), not F=H or Q(g)=H. |
| [Adopted trace-order index](Yin_C_G0198_v1.md#statement) | Actual maximal order and t_2>=ceil(r/11), v_2(J)>=t_2 on the full residual branch, with no upper index or existence conclusion. |
| [Normalized sparse analytic argument](Yin_C_G0140_v1.md#argument) | Prior two-case mechanism; its norm-only application is reconstructed completely as NF1--NF8, not assumed from its printed statement. |
| [Powered angular interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon, small domain, actual powered degrees and all original embeddings in NF5. |
| [Measurable-set source](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted pure-imaginary statement with absolute A and unchanged source-proof limits. |
| [Scalar Jensen and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Full integer root products, constants, integrable circle zeros and cyclotomic products with multiplicity. |
| [Nonreciprocal gap source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Accepted Smyth theorem on each nonreciprocal integer-unit partner, unchanged statement/source-proof scope. |
| [General representative multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Existing arbitrary-degree representative theorem, distinct from canonical degree restrictions. |
| [Existing canonical degree theorem](Yin_C_G0196_v4.md#statement) | Adopted degree34 and canonical w<=33 all-even/Haar consequence; no new cutoff or boundary existence. |

The canonical K proof is the original root/inventory author argument, with its original date preserved.
AW is root/comparison_cleanup author work, and NF is the complete fixed reconstruction of the already identified C140 proof-level specialization.
No independent checking of those new consumer parts is claimed.
R480 reviews C198, R478 reviews the prior canonical budget, and R495 reviews C140's actual theorem and proof; none prospectively reviews this new assembly or the changed norm-only application.
Any upstream author relationship remains disclosed in the new review and its actual fixed evidence below.
The current R459/R468/R473/R478/R480/R495 relationships are unknown, as is whole R482; their original dates, exact scopes and mathematical findings remain fixed rather than supplying current independent certification.
No source-proof upgrade, computation, matrix execution or mutable draft is a mathematical premise.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:22 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft integral-representative and paid-transfer inquiries. |
| reason | Adopt complete K1--K11, AW1--AW8 and NF1--NF8 through actual whole independent consumer/extraction R482. The arbitrary-degree componentwise integer representative obstruction, exact trace-order excluded class, complete canonical factor/field/cyclotomic costs and fixed-width fixed-margin norm-only paid gap are proved at their separate domains. All full original norms, rational denominators, finite analytic constants and source limits remain paid. Earlier physical versions and their decisions remain unchanged. No allowed even-index realization, unbounded-width transfer or unrestricted Mahler gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--D, arbitrary integer degrees and individual component values, baseline log2 versus residual I_*, exact index class, complete canonical factor/width costs and inherited dyadic boundary. |
| argument | [Complete assembled proof](#argument) | Entire K1--K11, AW1--AW8 and NF1--NF8; all original scalars, multiplicities, analytic constants, zero-polynomial versus zero-value cases and domain limits. |
| dependency | [Actual trace and pairwise proof](Yin_C_G0153_v2.md#argument) | Same P/K/F/T, nonzero integer quotient values, totally real pair exclusions and full quadratic-tower phases. |
| dependency | [Actual arithmetic income](Yin_C_G0191_v2.md#statement) | Full original2^d baseline and residual Norm_F(g)>=2^(6r/11), giving I_* without losing any conjugate or degree factor. |
| dependency | [Primitive residual triple field](Yin_C_G0188_v1.md#statement) | Only H=Q(a,b,c)=Q(a), not F=H or Q(g)=H. |
| dependency | [Adopted trace-order index](Yin_C_G0198_v1.md#statement) | Actual maximal order and t_2>=ceil(r/11), v_2(J)>=t_2 on the full residual branch, with no upper index or existence conclusion. |
| dependency | [Normalized sparse analytic argument](Yin_C_G0140_v1.md#argument) | Prior two-case mechanism; its norm-only application is reconstructed completely as NF1--NF8, not assumed from its printed statement. |
| dependency | [Powered angular interface](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Exact epsilon, small domain, actual powered degrees and all original embeddings in NF5. |
| dependency | [Measurable-set source](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted pure-imaginary statement with absolute A and unchanged source-proof limits. |
| dependency | [Scalar Jensen and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Full integer root products, constants, integrable circle zeros and cyclotomic products with multiplicity. |
| dependency | [Nonreciprocal gap source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Accepted Smyth theorem on each nonreciprocal integer-unit partner, unchanged statement/source-proof scope. |
| dependency | [General representative multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Existing arbitrary-degree representative theorem, distinct from canonical degree restrictions. |
| dependency | [Existing canonical degree theorem](Yin_C_G0196_v4.md#statement) | Adopted degree34 and canonical w<=33 all-even/Haar consequence; no new cutoff or boundary existence. |
| support | [Whole arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual C191 whole scope and its disclosed contributor relationships, not new review of K/AW/NF. |
| support | [Primitive-field whole finding](../audits/reviews/Yin_R_G0459_v1.md#positive-coordinate-field-whole-independent-finding) | Actual C188 whole scope and author boundaries. |
| support | [Trace-order whole finding](../audits/reviews/Yin_R_G0480_v1.md#dyadic-trace-order-image-whole-finding) | Actual adopted C198 evidence, with source-retention and upstream author relationships preserved. |
| support | [Normalized sparse whole finding](../audits/reviews/Yin_R_G0801_v1.md#normalized-sparse-cost-whole-independent-finding) | Exact C140 printed statement and proof; no prospective review of the norm-only consumer. |
| support | [General multiplicity whole finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Prior C196v2 scope only, not the new all-component statement. |
| support | [Joint canonical whole finding](../audits/reviews/Yin_R_G0478_v1.md#joint-c3-c5-degree34-consumer-whole-finding) | Actual C196v4 whole scope and contributor-overlapping upstream review limits. |
| support | [Complete inputs and boundaries](#exact-inputs) | All eleven direct inputs, old K/new AW/fixed NF authorship, exact source and review scopes and no mutable-D premise. |
| review | [Whole all-width and canonical-cost finding](../audits/reviews/Yin_R_G0482_v1.md#all-width-canonical-cost-whole-finding) | Complete A--D, every K/AW/NF proof step, all eleven dependencies and seven supports, exact log2 versus I_* thresholds, canonical versus arbitrary-degree scope, full norm-only analytic application and original denominator/frequency costs, with contributor-overlapping inputs explicitly reused through actual independent evidence. |

## Historical assessments

<a id="decision-initial"></a>

### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:11 |
| status | proof draft |
| review-status | unreviewed |
| reason | Preserve the complete canonical K1--K11 screen, weighted cyclotomic target and full width-cost limits; establish all-width AW1--AW8 with the actually adopted C198 input; give the complete fixed norm-only C140 application NF1--NF8. Prior physical C196 versions and their actual reviews remain unchanged. Whole independent consumer/extraction review is required; no new cutoff or uniform unrestricted transfer is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--D, arbitrary integer degrees and individual component values, baseline log2 versus residual I_*, exact index class, complete canonical factor/width costs and inherited dyadic boundary. |
| argument | [Complete assembled proof](#argument) | Entire K1--K11, AW1--AW8 and NF1--NF8; all original scalars, multiplicities, analytic constants, zero-polynomial versus zero-value cases and domain limits. |
| dependency | [Actual trace and pairwise proof](Yin_C_G0153_v2.md#argument) | Same P/K/F/T, nonzero integer quotient values, totally real pair exclusions and full quadratic-tower phases. |
| dependency | [Actual arithmetic income](Yin_C_G0191_v2.md#statement) | Full original2^d baseline and residual Norm_F(g)>=2^(6r/11), giving I_* without losing any conjugate or degree factor. |
| dependency | [Primitive residual triple field](Yin_C_G0188_v1.md#statement) | Only H=Q(a,b,c)=Q(a), not F=H or Q(g)=H. |
| dependency | [Adopted trace-order index](Yin_C_G0198_v1.md#statement) | Actual maximal order and t_2>=ceil(r/11), v_2(J)>=t_2 on the full residual branch, with no upper index or existence conclusion. |
| dependency | [Normalized sparse analytic argument](Yin_C_G0140_v1.md#argument) | Prior two-case mechanism; its norm-only application is reconstructed completely as NF1--NF8, not assumed from its printed statement. |
| dependency | [Powered angular interface](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Exact epsilon, small domain, actual powered degrees and all original embeddings in NF5. |
| dependency | [Measurable-set source](../audits/literature/BS13/Yin_U001.md#bs13-u001) | Accepted pure-imaginary statement with absolute A and unchanged source-proof limits. |
| dependency | [Scalar Jensen and Kronecker](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Full integer root products, constants, integrable circle zeros and cyclotomic products with multiplicity. |
| dependency | [Nonreciprocal gap source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Accepted Smyth theorem on each nonreciprocal integer-unit partner, unchanged statement/source-proof scope. |
| dependency | [General representative multiplicities](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Existing arbitrary-degree representative theorem, distinct from canonical degree restrictions. |
| dependency | [Existing canonical degree theorem](Yin_C_G0196_v4.md#statement) | Adopted degree34 and canonical w<=33 all-even/Haar consequence; no new cutoff or boundary existence. |
| support | [Whole arithmetic finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Actual C191 whole scope and its disclosed contributor relationships, not new review of K/AW/NF. |
| support | [Primitive-field whole finding](../audits/reviews/Yin_R_G0459_v1.md#positive-coordinate-field-whole-independent-finding) | Actual C188 whole scope and author boundaries. |
| support | [Trace-order whole finding](../audits/reviews/Yin_R_G0480_v1.md#dyadic-trace-order-image-whole-finding) | Actual adopted C198 evidence, with source-retention and upstream author relationships preserved. |
| support | [Normalized sparse whole finding](../audits/reviews/Yin_R_G0801_v1.md#normalized-sparse-cost-whole-independent-finding) | Exact C140 printed statement and proof; no prospective review of the norm-only consumer. |
| support | [General multiplicity whole finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Prior C196v2 scope only, not the new all-component statement. |
| support | [Joint canonical whole finding](../audits/reviews/Yin_R_G0478_v1.md#joint-c3-c5-degree34-consumer-whole-finding) | Actual C196v4 whole scope and contributor-overlapping upstream review limits. |
| support | [Complete inputs and boundaries](#exact-inputs) | All eleven direct inputs, old K/new AW/fixed NF authorship, exact source and review scopes and no mutable-D premise. |
