---
author: Yin
---
# Fourier square-energy and Salem Sobolev costs of the actual projection cubic

Date: 2026-10-18T13:56.
Human author Yin.
Root proposed testing C158's actual cubic joint angular expense by coefficient l2 and weighted Sobolev estimates instead of Wiener l1.
Root subsequently supplied the sharper projection diagonal-square estimate and its proposed difference-quotient transfer to the cubic.
Root also supplied the direct Salem circle-root contact improvement and the nested-projection correction question; both are developed below with their full hypotheses.
The loglog_cyclic_review agent develops the complete finite comparison below.
Both are contributors; this is author work, not independent review or an adopted gap theorem.
No mathematical program, numerical evaluation or new source acquisition is used.
This complete author proof is now registered for separate whole review.

<a id="projection-square-energy-reuse"></a>
## Actual inputs and changed question

The bounded reuse screen read [C92's short-annihilator effective-support statement](Yin_C_G0092_v1.md), [C145's actual angular contact and approximation expense](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy), [C158's complete cubic construction](Yin_C_G0158_v1.md#statement), [C159's exact finite-frequency envelope](Yin_C_G0159_v1.md#statement), and [the retained linear/coherence comparison](../ledger/Yin_L_G0430_v1.md#linear-projection-coherence-expense).
C92 already compares phase Gram energy with a squared radial error, while C145 explicitly records the square-root frequency-dimension price obtained from bounded range, Parseval and coefficient Cauchy--Schwarz.
That comparison, now retained in L430, already shows that applying the refined envelope directly to the linear kernel gives a stronger coherence rate than crude cubic compression.
Those results are reused at their actual scopes rather than called a new l2 mechanism.

The genuinely changed joint-moment input below is the already accepted [L167 complete Salem discriminant energy](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy), specialized at power n=1.
Its full proof, including diagonal self-energy, regularization correction and all original conjugates, was read before this application.
The [Pri11 method reading](../audits/literature/Pri11/readme.md#pri11-actual-product-energy), [accepted U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) and [accepted restricted U002](../audits/literature/Pri11/Yin_U002.md#pri11-u002) were also read to distinguish their actual source domains.
L167 proves the circle energy directly; the present use does not insert the circle cubic into a planar theorem without proving an extension, compact support, continuity modulus, energy and exterior-root costs.
No new external theorem or novelty claim is needed for finite Fourier Cauchy--Schwarz or the finite Fejer identity proved below.

<a id="statement"></a>
## Complete statement

Let P be a monic irreducible nontorsion integer-unit polynomial of degree d>=2 and total logarithmic Mahler measure m>0.
Put N=2d,T=2d-1,L=3T.
Let A be the N-by-d full coefficient matrix of P,tP,...,t^(d-1)P and define

    R=I_N-A(A^tA)^(-1)A^t,
    v_N(z)=(1,z,...,z^(N-1))^t,
    k(z)=N^(-1)v_N(z^-1)^t R v_N(z),
    G3=log2-(1-k)/2-(1-k)^2/8-(1-k)^3/24,
    H(f)=sum_(n!=0)|n||fhat(n)|^2, gamma=log(4/3).

H is the SQUARED half-Sobolev seminorm counting BOTH frequency signs, using normalized Haar coefficients.
R is the actual rational rank-d orthogonal projection; on the circle0<=k<=1 and integral k=1/2, while Laurent evaluation gives k(alpha_i)=1 at every original root.
The full phase measure nu=d^(-1)sum_i delta_(alpha_i/|alpha_i|) retains all d labels, including repeated phases.
The complete l2/envelope comparisons and Fejer lower bound in Sections1--2 hold on this domain, with every stated cutoff and C159 domain guard.

The generic actual projection bounds are

    H(k)<=d/8,
    (1/4)H(k)<=H(G3)<=(49/64)H(k)<=49d/512.

The k bound is sharp on the larger projection domain allowing the torsion polynomial t^d-1; sharpness is not asserted on the irreducible nontorsion domain.
H(k)=(2/N^2)sum_(n=1)^(N-1)n(sum_j R_(j,j+n))^2 is exact and rational.
Positive-frequency-only energy is half of the displayed two-sided energy.

For a GENUINE Salem P of degree d>=4, put q=d-2 and, for0<rho<1, define

    B_rho=2(q+1)m+4q log2+q log(1/(1-rho))
                         -q(q-1)log(rho)/2,
    C_(m,d)=2m+4log2+log(6d-2)+1/6.

Every real Laurent polynomial f of degree at most L satisfies

    |integral f dnu-integral f dmu|
       <=sqrt(2rho^(-L)H(f)B_rho)/d+2osc(f)/d,

where mu is normalized Haar measure and osc is the circle maximum minus minimum.
The last term retains the two original real-root phase labels.
All finite conditional budgets(9)--(13),(20)--(22) hold with their stated positivity guards.
Direct Salem contact gives the stronger lower bounds

    H(k)>=d(1/2-4/d)^2/[2exp(1)C_(m,d)], d>8,
    H(G3)>=d[gamma-1/32-(2log2+4/3)/d]^2
                                  /[2exp(1)C_(m,d)],

with the second asserted only when its square bracket is POSITIVE.
For every fixed finite M0>0, both energies are consequently at least c(M0)d/log d for every actual genuine Salem input with0<m<=M0 and sufficiently large d, for some c(M0)>0.
This does not assert existence in every prescribed subclass; C160 supplies actual bounded-positive-measure families of unbounded degrees.
No Wiener/kappa divergence, near-one family or unrestricted gap follows.

For any two real orthogonal projections R1,R2 with nested ranges in the SAME N-coordinate window and rank difference c, normalize both kernels by N as above.
Then

    |sqrt(H(k_R2))-sqrt(H(k_R1))|
       <=(1/2)sqrt(c(1-c/N))<=sqrt(c)/2.

The inclusion may be reversed; a mere rank bound on a nonprojective difference is insufficient.
All source, comparison, sharpness and failed-budget boundaries are part of the complete argument below.

<a id="actual-cubic-l2-cost"></a>
## 1. Exact original setting and the ordinary l2 expense

Let P be a monic irreducible nontorsion integer unit polynomial of original degree d>=2 and total logarithmic Mahler measure m>0.
Write all original conjugates as alpha_i=r_i z_i, with |z_i|=1, retaining all d labels even when their phases coincide.
Put nu=d^(-1)sum_i delta_(z_i), let mu be normalized Haar measure and write

    s_n=integral z^n dnu=(1/d)sum_i z_i^n.

Use the ACTUAL C158 residual projection in N=2d coordinates, T=2d-1, its kernel k, and the cubic

    0<=k<=1, integral k=1/2,
    G=G_3=log2-(1-k)/2-(1-k)^2/8-(1-k)^3/24,
    L=3T, G(z)=sum_(|n|<=L)c_n z^n,
    gamma=log(4/3), Delta_G=integral G dnu-integral G dmu.

L is an allowed full frequency cutoff even if some top coefficients vanish.
C145/C158/C159 give the exact contact lower estimate

    Delta_G>=gamma-(log2)D-1/16,
    D=integral(1-k)dnu, 0<=D<=4m.                    (1)

The safe loss1/16 charges both uniform1/32 approximation errors; no original logarithmic norm is replaced by an angular average.
The constant Fourier term cancels, so

    Delta_G=sum_(0<|n|<=L)c_n s_n.

The scalar cubic is increasing on [0,1] and its endpoint difference is2/3.
Thus its range is contained in [log2-2/3,log2].
For a real function with range in [a,b], integrating (f-a)(b-f)>=0 gives variance at most (b-mean f)(mean f-a)<=(b-a)^2/4.
By finite Parseval this proves

    V_G:=sum_(0<|n|<=L)|c_n|^2<=1/9.

Ordinary coefficient Cauchy--Schwarz therefore gives

    |Delta_G|<=sqrt(V_G) sqrt(sum_(0<|n|<=L)|s_n|^2)
              <=(1/3)sqrt(sum_(0<|n|<=L)|s_n|^2).   (2)

Let E(u)=e_ref(u) be exactly C159's increasing envelope, defined for0<u<=exp(-40).
If0<Lm/d<=exp(-40), its complete original-label frequency bound yields

    |Delta_G|<=sqrt(V_G) sqrt(2sum_(n=1)^L E(nm/d)^2)
              <=sqrt(2L) E(Lm/d)/3.                (3)

The factor sqrt(L) is present even though the function has a uniform range.
At L=3(2d-1), the last expression is of order sqrt(d*m)[log(1/m)]^2 in the small-m regime, with the declared envelope and cutoff domains retained; it is not a degree-free quantity tending to zero from m alone.

More generally, for ANY positive weights w_n on0<|n|<=L,

    |Delta_G|<=sqrt(sum w_n|c_n|^2)
                 sqrt(sum |s_n|^2/w_n)
              <=sqrt(sum w_n|c_n|^2)
                 sqrt(sum E(|n|m/d)^2/w_n).        (4)

The last inequality needs the same C159 domain.
Taking w_n=|n|^(2s) gives the finite order-s Sobolev pairing.
For fixed actual coefficients, the final expression in (4) is at least sum |c_n|E(|n|m/d), by Cauchy--Schwarz.
Thus applying Cauchy--Schwarz only to the existing individual envelopes is a relaxation of C159's actual weighted l1 sum, not a stronger conditional criterion.
A gain must come from genuinely better JOINT control of the moments or from additional information about their association with these particular coefficients.

<a id="phase-alias-fejer-lower-bound"></a>
## 2. A finite d-label lower bound prevents automatic l2 decay

For ANY d labelled points z_i on the circle and any integer L>=1, define the finite Fejer polynomial

    F_L(z)=abs(1+z+...+z^L)^2/(L+1)
          =sum_(|n|<=L)(1-|n|/(L+1))z^n>=0.

The coefficient formula follows by counting the L+1-|n| pairs with difference n.
Since F_L(1)=L+1, summing over ALL ordered pairs of labels gives

    1+sum_(0<|n|<=L)(1-|n|/(L+1))|s_n|^2
        =(1/d^2)sum_(i,j)F_L(z_i conjugate(z_j))
        >=(L+1)/d.                                 (5)

Only the d diagonal terms were retained in the inequality; every other term is nonnegative.
Repeated phases therefore cause no exception and may only add further terms.
For the actual cutoff L=3(2d-1), (5) becomes

    sum_(0<|n|<=L)(1-|n|/(L+1))|s_n|^2
        >=5-2/d,
    sum_(0<|n|<=L)|s_n|^2>=5-2/d.                  (6)

Consequently an automatic o(1) bound on this unweighted joint moment norm is impossible at the declared cutoff, even before arithmetic restrictions are considered.
In particular, if one uses ONLY the generic coefficient estimate sqrt(V_G)<=1/3 in (2), any valid upper bound for the second factor is at least sqrt(5-2/d), so the resulting numerical upper certificate is at least2/3 for d>=2.
This exceeds gamma<1/3 and cannot beat the positive contact target in (1).
The inequality gamma<1/3 is log(1+x)<x at x=1/3.
This diagnoses that particular pair of estimates, not the actual size of V_G or impossibility of a coefficient-sensitive l2 estimate.
It does not assert that the lower bound (6) is attained by an admissible integer input.

<a id="salem-half-sobolev-budget"></a>
## 3. A different joint bound from the full Salem discriminant energy

Now restrict P to a GENUINE Salem polynomial of degree d>=4.
Choose its exterior root alpha=exp(m)>1, so its roots are exp(m),exp(-m) and q=d-2 distinct unit-circle roots gamma_1,...,gamma_q.
The two exterior/interior roots have the SAME phase1; they still contribute two original labels.
For n>=1 put S_n=sum_(j=1)^q gamma_j^n, so s_n=(S_n+2)/d.

For EVERY regularization parameter0<rho<1, L167 at power1 proves

    E_rho=sum_(n>=1)rho^n|S_n|^2/n<=B_rho,
    B_rho=2(q+1)m+4q log2+q log(1/(1-rho))
                         -[q(q-1)/2]log rho.       (7)

The nonzero integer discriminant pays the off-diagonal energy.
The q log(1/(1-rho)) term is the diagonal self-energy, and the last term is the full off-diagonal regularization correction.
Neither term may be removed when choosing rho near1.
The normalized quantities here use q central roots inside S_n but ORIGINAL degree d in every empirical average below.

For a real Laurent polynomial G of degree at most L define its SQUARED half-Sobolev seminorm

    H(G)=sum_(0<|n|<=L)|n||c_n|^2.

Its exact angular discrepancy splits as

    Delta_G=(1/d)sum_(0<|n|<=L)c_n S_n
                         +(2/d)(G(1)-integral G),

where S_(-n)=conjugate(S_n).
Apply finite Cauchy--Schwarz with coefficient weights |n|rho^(-|n|).
The other squared factor is sum_(0<|n|<=L)rho^|n| |S_n|^2/|n|<=2E_rho.
The coefficient factor is at most rho^(-L)H(G).
It follows that

    |Delta_G|<=sqrt(2rho^(-L)H(G)B_rho)/d
                                +2osc(G)/d.        (8)

For the actual G3, osc(G)<=2/3, so the last term is at most4/(3d).
This explicitly pays the two off-circle labels without substituting their nonunit moduli into a circle polynomial or dropping them.
It is a JOINT energy bound from L167, rather than a Cauchy--Schwarz relaxation of C159's individual frequency envelope.

For genuine Salem inputs C145 additionally gives D<=2/d, since k=1 at every original unit-circle root and0<=k<=1 on every phase.
Thus define

    delta_S=gamma-(log2)min(4m,2/d)-1/16.

Combining (1), (7) and (8) gives the complete necessary finite budget

    delta_S<=sqrt(2rho^(-L)H(G3)B_rho)/d+4/(3d).    (9)

If delta_S>4/(3d), equivalently

    H(G3)>=(d delta_S-4/3)^2/[2rho^(-L)B_rho].       (10)

If that positivity condition fails, (9) is still valid but squaring a negative numerator is not justified.
A supplied strict upper bound below the right side of (10), at its actual m,d,rho, would exclude that input.
No such automatic arithmetic upper bound has been proved.

### A fully explicit degree-scale regularization

Keep L=3(2d-1) and choose rho=exp(-1/L), so rho^(-L)=exp(1).
The inequality exp(1/L)>=1+1/L gives1-rho>=1/(L+1).
Also L>=3d for d>=1 and q<=d, so (7) implies

    B_rho<=d C_(m,d),
    C_(m,d)=2m+4log2+log(6d-2)+1/6.                (11)

Indeed the last correction is q(q-1)/(2L)<=d/6; all other terms are bounded separately by their displayed contributions in (11).
Consequently

    |Delta_G3|<=sqrt([2exp(1)H(G3)/d] C_(m,d))
                                        +4/(3d).  (12)

For delta_S>4/(3d), the weaker but completely explicit necessary condition is

    H(G3)>=d[delta_S-4/(3d)]^2/[2exp(1)C_(m,d)].     (13)

In a DECLARED regime d->infinity with0<m<=M0 for one fixed finite M0, one has C_(m,d)=log d+O_(M0)(1) and delta_S->gamma-1/16>0.
Thus (13) forces H(G3)=Omega_(M0)(d/log d).
In particular an independently proved H(G3)=o(d/log d) on a purported bounded-measure Salem family with unbounded degree would contradict (12) and the actual contact lower bound.
This includes any hypothetical near-one Salem sequence with unbounded degree; no such sequence or energy upper estimate is asserted.
The bounded-measure and growing-degree conditions are essential to this stated asymptotic threshold.
At finite degree or for m growing without a stated bound one must use (9)--(13), not replace their costs by an o-symbol.

<a id="generic-cubic-sobolev-loss"></a>
## 4. What the automatic coefficient estimates actually pay

Derivatives in this section are with respect to angular theta, with normalized Haar L2 norm.
The kernel has Fourier cutoff T, range[0,1] and mean1/2, hence

    ||k-1/2||_2<=1/2,
    ||k'||_2<=T/2.

The second estimate is finite Parseval with n^2<=T^2.
For G3=Phi(k), direct differentiation gives

    Phi'(x)=1/2+(1-x)/4+(1-x)^2/8,
    1/2<=Phi'(x)<=7/8 for0<=x<=1.

Therefore ||G3'||_2<=7T/16.
Combining this with sqrt(V_G)<=1/3 and finite coefficient Cauchy--Schwarz gives

    H(G3)<=sqrt(sum_(n!=0)|c_n|^2)
                sqrt(sum_(n!=0)n^2|c_n|^2)
           <=7T/48.                                (14)

This is an automatic O(d) upper bound, not the o(d/log d) condition.
Substituting (14) into (12) gives only

    |Delta_G3|<=sqrt([7exp(1)T/(24d)] C_(m,d))
                                     +4/(3d),       (15)

which retains a square-root log d expense for bounded m and growing d.
The last conclusion concerns THIS upper estimate; it does not claim the actual discrepancy grows or the actual energy attains (14).

### The actual projection gives a sharper generic constant, still of order d

Write the real symmetric rank-d projection as R=(R_ij)_(0<=i,j<N), with N=2d, and put

    a_n=sum_(j=0)^(N-1-n)R_(j,j+n),
    khat(n)=a_n/N for1<=n<N,
    H_+(k)=sum_(n=1)^(N-1)n|a_n/N|^2.

This H_+ counts only POSITIVE frequencies, whereas H(k)=2H_+(k) uses both signs throughout (7)--(15).
For each n, finite Cauchy--Schwarz and n(N-n)<=N^2/4 give

    |a_n|^2<=(N-n)sum_j |R_(j,j+n)|^2,
    H_+(k)<= (1/4)sum_(i<j)|R_ij|^2.               (16)

The projection identity R^2=R and trace R=d imply

    sum_(i<j)|R_ij|^2=(d-sum_i R_ii^2)/2.

Also sum_i R_ii^2>=(sum_i R_ii)^2/N=d/2.
Combining these exact finite identities proves

    H_+(k)<=d/16, H(k)<=d/8.                       (17)

The constants are sharp for the broader residual-projection construction before the nontorsion/irreducibility restriction.
Indeed P(t)=t^d-1 has relation-column matrix[-I_d;I_d] in the2d window and residual projection

    R=(1/2)[I_d I_d; I_d I_d],
    k(z)=1/2+(z^d+z^(-d))/4.

Here a_d=d/2 and every other positive a_n is zero, so H_+(k)=d/16.
This is a reducible torsion polynomial for d>=2, not an admissible counterexample to a stronger arithmetic bound on the original domain.
It shows why the universal projection identity alone cannot yield a little-o improvement over (17).

For completeness, every finite Laurent polynomial f satisfies the exact normalized difference-quotient identity

    H(f)=double_integral_(T x T)
          |f(z)-f(w)|^2/|z-w|^2 dmu(z)dmu(w).      (18)

The diagonal has product measure zero and the quotient has a bounded limiting extension for a trigonometric polynomial.
To verify the identity, set z=wu and first integrate over w; distinct Fourier exponents are orthogonal and their cross terms disappear.
For n>0 the remaining factor is |(u^n-1)/(u-1)|^2=|1+u+...+u^(n-1)|^2, whose normalized integral is n.
For n<0 its modulus differs only by a unit monomial from the corresponding expression with |n|, giving |n|; the constant term contributes zero.
This proves every factor in (18), without an uninspected Sobolev normalization convention.

The derivative bounds1/2<=Phi'<=7/8 on[0,1] imply

    (1/2)|k(z)-k(w)|
       <=|Phi(k(z))-Phi(k(w))|
       <=(7/8)|k(z)-k(w)|.

Squaring and integrating (18) therefore yields

    (1/4)H(k)<=H(G3)<=(49/64)H(k)<=49d/512.         (19)

In the positive-frequency-only convention the final upper bound is49d/1024.
The factor2 between these conventions is retained in the discrepancy and joint-energy formulas.
The quantity H(k)=(2/N^2)sum_(n=1)^(N-1)n a_n^2 is an exact rational expression in the actual projection entries, without expanding the cubic.
Equation(19) also proves that H(G3)=o(d/log d) and H(k)=o(d/log d) are equivalent on any declared growing-degree family.
Thus changing from k to the fixed cubic does not by itself create a different asymptotic energy class.

Using (19) in the finite Salem inequality gives the actual-k version

    |Delta_G3|<=(7/8)sqrt(2rho^(-L)H(k)B_rho)/d
                                         +4/(3d).

With the same explicit rho=exp(-1/L) and C_(m,d) from (11), this becomes

    |Delta_G3|<=sqrt([49exp(1)H(k)/(32d)]C_(m,d))
                                         +4/(3d). (20)

For delta_S>4/(3d), the corresponding necessary rational-energy condition is

    H(k)>=32d[delta_S-4/(3d)]^2
                         /[49exp(1)C_(m,d)].        (21)

A supplied strict upper bound below that threshold would exclude the input, with every radial/contact and regularization expense shown.
Substituting only the automatic H(k)<=d/8 instead gives

    |Delta_G3|<=(7/16)sqrt(exp(1)C_(m,d))+4/(3d),   (22)

so even this sharper universal constant retains the square-root log d loss in the bounded-m, growing-d regime.
No new numerical value, actual energy evaluation or arithmetic little-o upper estimate is inferred.

<a id="actual-bounded-measure-salem-energy-floor"></a>
## 5. Direct Salem contact makes the bounded-measure energy floor unconditional

For a genuine Salem input, every one of the d-2 original circle roots is already its own phase and satisfies k=1.
The other two original phases both equal1.
Thus the exact kernel discrepancy is

    integral k dnu-integral k dmu
       =(d-2+2k(1))/d-1/2>=1/2-2/d.               (23)

There is no small-m radial estimate in this formula.
The cubic has G3=log2 at all d-2 circle roots and G3(1)>=log2-2/3>0.
For the last strict sign, the derivative of log x-2(x-1)/(x+1) is (x-1)^2/[x(x+1)^2], so log2>2/3.
The C158 Haar bound is integral G3<=log(3/2)+1/32.
Consequently

    Delta_G3>=gamma-1/32-(2log2)/d.                (24)

The exact phase average is [(d-2)log2+2G3(1)]/d; the last inequality merely drops its nonnegative final term.
This proves the stated improvement without replacing the one-sided approximation by two error terms.

The general L167-backed estimate (8) applies to k as well, using the same valid cutoff L=3(2d-1), regularization rho=exp(-1/L) and constant C_(m,d), while osc(k)<=1.
Combining it with (23), and using (11), gives for d>8

    H(k)>=d(1/2-4/d)^2/[2exp(1)C_(m,d)].          (25)

The2/d off-circle comparison cost in (8) is subtracted in addition to the2/d already present in (23); this explains the4/d in the positive numerator.
Using (24) instead, with the cubic's4/(3d) comparison cost, gives

    H(G3)>=d[gamma-1/32-(2log2+4/3)/d]^2
                              /[2exp(1)C_(m,d)]   (26)

whenever the expression inside the square is positive.
No squared negative-numerator inference is made for smaller degrees.
Equations(25)--(26) strengthen the earlier general-contact thresholds while preserving (9)--(13) as valid finite bounds.

For every fixed M0>0, these are ACTUAL lower bounds for every genuine Salem input with0<m<=M0 and sufficiently large degree.
In particular both H(k) and H(G3) are bounded below by c(M0)d/log d for some positive constant and all sufficiently large such d, directly from the explicit C_(m,d).
This is not merely a statement conditional on m tending to zero, and it does not assert the existence of any input in an empty prescribed subclass.
The already accepted [C160 bounded-measure family](Yin_C_G0160_v1.md#statement) supplies actual unbounded-degree Salem families of bounded positive total measure, so a universal little-o budget based ONLY on bounded total measure would already fail on existing inputs.
No near-one counterexample is involved.

This weighted coefficient energy can be carried by high frequencies of bounded coefficient mass.
For example the finite kernel comparison k=1/2+(z^d+z^(-d))/4 has nonconstant Wiener mass1/2 and H(k)=d/8.
Accordingly neither (25) nor (26) asserts divergence of kappa or Wiener l1 mass; the torsion comparison illustrates the distinction without being used as an admissible Salem example.
The earlier near-one Wiener divergence retained in L430 uses a different argument and remains at its own declared scope.

### A same-window nested-projection correction with its exact rank price

Let E be ANY real orthogonal projection of rank c in a fixed N-dimensional coefficient window,0<=c<=N, and normalize k_E(z)=N^(-1)v_N(z)^*E v_N(z) on the circle.
The proof of (16), now with trace E=c, gives the TWO-SIDED estimate

    H(k_E)<=(1/4)(c-sum_i E_ii^2)
            <=c(1-c/N)/4<=c/4.                    (27)

Indeed the positive-frequency estimate is one eighth of c-sum E_ii^2, and doubling restores both signs.
The diagonal-square bound is sum E_ii^2>=c^2/N.
This includes c=0 and c=N, where the energy is zero.

Suppose R_1,R_2 are real orthogonal projections in the SAME N-coordinate window and range(R_1) is contained in range(R_2).
Then E=R_2-R_1 is an orthogonal projection of rank c=rank(R_2)-rank(R_1).
Using the SAME normalization by N, one has k_(R_2)-k_(R_1)=k_E.
The seminorm sqrt(H) is the Euclidean norm of the nonconstant coefficient vector multiplied by sqrt(|n|), so its reverse triangle inequality and (27) give

    abs(sqrt(H(k_(R_2)))-sqrt(H(k_(R_1))))
       <=(1/2)sqrt(c(1-c/N))<=sqrt(c)/2.           (28)

The same statement holds after reversing a nested inclusion.
Merely knowing that a difference has rank c is insufficient; the difference must be the displayed projection, and changing the normalization window also changes the formula.
No particular cofactor or relation-space construction is assumed to satisfy this nesting condition without checking its actual spaces.
This is a reusable rank-priced comparison, not a new integral value, norm income or upper estimate for all original kernels.

The new finite criterion (9)--(13) is a different conditional way to price the actual dense test using accepted joint moment energy.
It is not an automatic improvement in arithmetic coverage, and it is not a new existence theorem for a favorable Haar auxiliary.
The generic l2/envelope relaxation is already dominated by C159, while the additional Salem joint-energy interface still needs a genuinely sharper upper estimate for H(G3) or a more precise coefficient-moment association.
C92's effective support, the coherence divergence retained in L430 and C145's contact obstruction remain consistent with all these necessary estimates.
No ordering between these distinct supplied structural conditions is claimed without an actual bound relating their quantities.

The author checked the complete original-label normalization, both signs of each Fourier frequency, repeated phases, the Fejer diagonal count, the exact range and derivative constants, every use of Cauchy--Schwarz, every L167 term, the two off-circle phases, the contact approximation loss, the positive-numerator guard and the declared asymptotic regimes.
The sharper projection account was also checked at its exact rank/window, diagonal-square and positive-versus-two-sided frequency conventions, with the complete difference-quotient identity and the out-of-domain torsion sharpness control retained.
The direct Salem contact and nested correction were checked separately for both repeated phase1 labels, the1/32 cubic Haar error, every positive-numerator restriction, bounded-M versus near-one quantifiers, the exact c/N normalization and the necessary range inclusion.
The complete argument remains author-checked pending separate whole review, without a Task-status change or unrestricted gap.

## Current assessment
[Selected decision](#decision-current-actual-product-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T14:10 |
| status | open |
| reason | Register the full actual projection half-Sobolev theorem and paid-budget comparison for separate whole review. Direct Salem contact forces energy growth on all actual bounded-measure growing-degree Salem inputs; generic sharp projection bounds and same-window nested rank corrections are explicit. Root and loglog_cyclic_review are contributors. No Wiener divergence or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Original projection/phase conventions, finite l2 comparisons, Salem joint energy and actual lower bounds, generic sharp bound and same-window nested rank correction. |
| argument | [Complete proof](#actual-cubic-l2-cost) | All five sections and28 formulas, full positivity/cutoff/normalization guards, source and comparison limits. |
| dependency | [Projection and cubic](Yin_C_G0158_v1.md#statement) | Actual rank/window, Laurent values, circle range/mean, fixed cubic and one-sided Haar approximation. |
| dependency | [Salem discriminant energy](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy) | Complete power1 joint energy, all central roots, diagonal regularization and full original costs. |
| dependency | [General contact](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | General radial/contact bounds in the earlier finite comparison, before the direct Salem improvement. |
| dependency | [Individual angular envelope](Yin_C_G0159_v1.md#statement) | Exact individual envelope and small-u domain only in Sections1--2. |
| dependency | [Actual bounded-measure family](Yin_C_G0160_v1.md#statement) | Existing unbounded original degrees and bounded positive total measure only; no new calculation or Wiener divergence. |
| support | [Effective-support comparison](Yin_C_G0092_v1.md#statement) | Existing scope comparison, not new arithmetic coverage. |
| support | [Planar-energy source boundary](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Method comparison only; no unproved planar extension or new external theorem premise. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T14:19 |
| status | proved |
| reason | Adopt the complete actual projection-energy theorem through R403 whole noncontributor review. All original-domain and Salem-specific finite bounds, direct bounded-measure energy growth, sharp generic projection constants and same-window nested correction are checked. These are paid analytic cost and scoped failure results, not Wiener divergence, automatic arithmetic coverage or a Task stop. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Original projection/phase conventions, finite l2 comparisons, Salem joint energy and actual lower bounds, generic sharp bound and same-window nested rank correction. |
| argument | [Complete proof](#actual-cubic-l2-cost) | All five sections and28 formulas, full positivity/cutoff/normalization guards, source and comparison limits. |
| dependency | [Projection and cubic](Yin_C_G0158_v1.md#statement) | Actual rank/window, Laurent values, circle range/mean, fixed cubic and one-sided Haar approximation. |
| dependency | [Salem discriminant energy](../ledger/Yin_L_G0167_v1.md#actual-powered-salem-discriminant-energy) | Complete power1 joint energy, all central roots, diagonal regularization and full original costs. |
| dependency | [General contact](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | General radial/contact bounds in the earlier finite comparison, before the direct Salem improvement. |
| dependency | [Individual angular envelope](Yin_C_G0159_v1.md#statement) | Exact individual envelope and small-u domain only in Sections1--2. |
| dependency | [Actual bounded-measure family](Yin_C_G0160_v1.md#statement) | Existing unbounded original degrees and bounded positive total measure only; no new calculation or Wiener divergence. |
| support | [Effective-support comparison](Yin_C_G0092_v1.md#statement) | Existing scope comparison, not new arithmetic coverage. |
| support | [Planar-energy source boundary](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Method comparison only; no unproved planar extension or new external theorem premise. |
| review | [Whole projection-energy finding](../audits/reviews/Yin_R_G0403_v1.md#projection-sobolev-whole-independent-finding) | Complete fixed statement, all five sections/28 formulas and declarations; both frequency signs, every domain and positivity guard, actual bounded-measure quantifiers, generic sharpness, rank correction and prior source/review scopes. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C390/C394 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Original projection/phase conventions, finite l2 comparisons, Salem joint energy and actual lower bounds, generic sharp bound and same-window nested rank correction. |
| argument | [Exact retained argument](#actual-cubic-l2-cost) | All five sections and28 formulas, full positivity/cutoff/normalization guards, source and comparison limits. |
| dependency | [Exact retained dependency](Yin_C_G0158_v1.md#statement) | Actual rank/window, Laurent values, circle range/mean, fixed cubic and one-sided Haar approximation. |
| dependency | [Exact retained dependency](Yin_C_G0390_v1.md#actual-powered-salem-discriminant-energy) | Complete power1 joint energy, all central roots, diagonal regularization and full original costs. |
| dependency | [Exact retained dependency](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) | General radial/contact bounds in the earlier finite comparison, before the direct Salem improvement. |
| dependency | [Exact retained dependency](Yin_C_G0159_v1.md#statement) | Exact individual envelope and small-u domain only in Sections1--2. |
| dependency | [Exact retained dependency](Yin_C_G0160_v1.md#statement) | Existing unbounded original degrees and bounded positive total measure only; no new calculation or Wiener divergence. |
| support | [Exact retained support](Yin_C_G0092_v1.md#statement) | Existing scope comparison, not new arithmetic coverage. |
| support | [Exact retained support](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Method comparison only; no unproved planar extension or new external theorem premise. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0403_v1.md#projection-sobolev-whole-independent-finding) | Complete fixed statement, all five sections/28 formulas and declarations; both frequency signs, every domain and positivity guard, actual bounded-measure quantifiers, generic sharpness, rank correction and prior source/review scopes. |
