---
author: Yin
---
# Exact signed root comparison and original contact term for rational trace regularization

Date: 2026-10-20T14:29.
Human author Yin.
Root and draft_inventory_later developed the new SP1--SP12 proof in D35 on2026-10-20.
Root supplied the exact original-value decomposition and contact-term interpretation.
Draft_inventory_later derived and checked the full signed root kernel, Green equality, local cluster products and finite-parameter costs.
Both are contributors; this version is a candidate awaiting whole independent review.
The complete [physical v1](Yin_C_G0195_v1.md#argument), its selected adoption and [actual R471](../audits/reviews/Yin_R_G0471_v1.md#rational-trace-regularizer-whole-independent-finding) retain their unchanged scope.
Root's upstream author role is disclosed; the previous independent finding is reused only for those fixed regularizer identities and costs, not as review of the new signed comparison.
No computation, parameter scan, new input or source acquisition was performed.

<a id="statement"></a>
## Complete signed-comparison statement

Let P in Z[z] be monic, irreducible, reciprocal and nontorsion, of degree d=2r and constant coefficient1.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), and assume the actual trace field F=Q(delta) is totally real.
Let Theta be its monic integer minimal trace polynomial, so P(z)=z^r Theta(z+z^(-1)).
For a fixed s in{1,-1} use

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    k0=30375, L=972000=32k0,
    E=-z^(-3d)H23/72, F0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/k0,
    H=Theta(z+z^(-1))G, A0=(E+sG)^2+F0^2.

For every positive rational epsilon=p_epsilon/q_epsilon, with positive integers p_epsilon,q_epsilon, set

    B_epsilon=G^2+A0 epsilon^4/(H^2+epsilon^2)^2,
    D_epsilon=k0^2 p_epsilon^2 z^(16d)
                        +q_epsilon^2 P^2 H35^2,
    U_s=[13500z^(9d/2)H23+32sH35]^2
                                  +1215^2 z^(5d)H25^2,
    N_epsilon=1024H35^2 D_epsilon^2
                       +k0^4 p_epsilon^4 z^(32d)U_s,
    B_epsilon=z^(-15d)N_epsilon/(L^2D_epsilon^2).

These are the fixed actual regularizer and supplied polynomials of v1, without cancelling factors or changing the original value.
Write e=E(alpha), f=F0(alpha) and g=G(alpha) for the actual field values.
Let alpha_i run over all d original roots, e_i=E(alpha_i), f_i=F0(alpha_i), g_i=G(alpha_i), and Q_i=(e_i+s g_i)^2+f_i^2+g_i^2>0.
Use normalized Haar probability mu and

    L_P=(1/d)sum_i log Q_i,
    I_epsilon=integral log B_epsilon dmu,
    J_G=integral log G^2 dmu, Delta_epsilon=L_P-I_epsilon.

The following exact assertions hold.

1. With all94d numerator zeros beta and32d denominator zeros gamma, counted with multiplicity, and K_P(w)=d^(-1)log|P(w)|-log^+|w|, the complete signed equality is
   Delta_epsilon=sum_beta K_P(beta)-2sum_gamma K_P(gamma).
   It includes every removable factor and possible numerator circle zero; no original root is a numerator or denominator zero.
   Any literal64d-term pairing leaves30d numerator terms and obeys the explicit relative-distance estimate(SP5).
2. The exact Poisson/Green equality(SP6) is
   Delta_epsilon=A_P(log B_epsilon)+30m(P)+Pi_epsilon-Zeta_epsilon,
   with all original folded roots, full multiplicities, numerator-zero charge Zeta and denominator charge Pi.
   Its signed charge is not replaced by the positive pole bound.
3. If the actual field element g=G(alpha) is nonzero, then with
   D_G=2[d^(-1)log|Res(P,H35)|-m(H35)] and C_P=d^(-1)sum_i log(Q_i/g_i^2),
   one has Delta_epsilon=D_G+C_P-h_epsilon, where h_epsilon=I_epsilon-J_G>0 tends to0 and C_P>=0 is independent of epsilon.
   C_P=0 exactly when the full residual equations f=e+s g=0 hold.
   Each original-root cluster has the exact product-ratio limit(SP9), accounting for the surviving C_P despite weak signed-divisor convergence to twice the divisor of H35.
4. If g=0, statements1--2 and the fixed v1 Haar limit remain valid; the divergent log-resultant and coprime cluster formulas in statement3 are not used.
   The identity in(SP11) holds for every positive rational epsilon; its bound h_epsilon<=eta applies to the finite choice in statement5 only.
5. For fixed0<eta<=1, tau=log2 (or tau=(12/11)log2 on the full residual branch) and J_G<=tau-2eta, the unchanged v1 prescription(SP1) supplies a rational epsilon=1/M with0<h_epsilon<=eta and I_epsilon<=tau-eta.
   Its full input-dependent precision and coefficient prices are(SP2).
   For g!=0 the exact sandwich is D_G+C_P-eta<=Delta_epsilon<D_G+C_P; on this class Delta_epsilon>=eta.

These identities and local limits do not prove a bound Delta_epsilon<=omega_eta(m(P)) with omega_eta(t) tending to0, automatic near-one coverage, or a failure of every correctly paid rational transfer.
They identify precisely the signed potential, original relative separations and unchanged resultant term that such a proof must control.
All original phases, scalars, degrees and zero-g exceptions are retained.

<a id="argument"></a>
## Complete proof and exact quantitative boundary

### Exact scope, reused evidence and the finite parameter

Use the entire original domain and the SAME unreduced functions of [C195](Yin_C_G0195_v1.md#statement): monic irreducible reciprocal nontorsion P with constant1, degree d=2r, actual totally real trace field, original roots alpha_i counted in degree d, and the actual E,F0,G,H=Theta G and A0=(E+sG)^2+F0^2 for one fixed s in{1,-1}.
Put k0=30375 and L=972000=32k0.
The values Q_i=(e_i+s g_i)^2+f_i^2+g_i^2 are positive at every original embedding.
Use L_P=(1/d)sum_i log Q_i, I_epsilon=integral_T log B_epsilon dmu and J_G=integral_T log G^2 dmu, with the same Haar probability and original degree as C195.
The retained [C193 cost proof](Yin_C_G0193_v1.md#argument), [C177 exact original discrepancy](Yin_C_G0177_v1.md#polynomial-shear-actual-transfer-price) and [C189v4 full-symbol boundary](Yin_C_G0189_v4.md#statement) were read before this derivation.
C193/C189 do not bound a product involving a shrinking original-root discrepancy, and C177 already identifies the unchanged G resultant below; it is reused rather than announced as a new theorem.
C195(RR14) already gives the full fixed-input limit L_P-J_G, but does not give the root-pair formula or justify interchanging a singular root kernel with weak cancellation.

Fix0<eta<=1 and let tau=log2, or tau=(12/11)log2 on the full residual branch.
For the proposed useful-saving class impose J_G<=tau-2eta.
Use precisely C195(RR11), with its error tolerance eta, to choose epsilon=1/M: set

    D0=16d, A=A_s0 ||P||_1^2,
    C_A=1+log_+(A(k0/7)^2)/log2,
    k=ceil(max{4,2log_2(2D0(C_A+2D0)/eta)}),
    rho=(7/k0)2^(-kD0),
    M=ceil(max{1,(2A/(eta rho^6))^(1/4)}).
    h_epsilon=I_epsilon-J_G in(0,eta],
    I_epsilon<=tau-eta.                          (SP1)

Here A_s0 is the actual C195(RR9) coefficient expression, not a bounded surrogate.
The degree16d and leading scalar7 belong to the full P H35, with all repeated and circle zeros.
This is an input-dependent sufficient parameter, not an optimal or necessary precision.
In particular the prescription retains

    log(1/epsilon)=log M
      <=log2+(1/4)log_+(2A/eta)
           +(3/2)[log(k0/7)+kD0 log2].           (SP2)

The inequality follows from ceil(max{1,t})<=2max{1,t} and the displayed rho.
It is not an upper bound by a function of m(P) alone.
For this choice p_epsilon=1,q_epsilon=M, the supplied clearing coefficient bound is still
[A_s0+G1^2(1+H1^2 M^2)^2]/2 from C195(RR9).
The rational supplied numerator/denominator degrees remain94d/64d; clearing pays the already proved94m(P), whereas the direct meromorphic comparison below retains30m(P).
No coefficient, precision or radial price is removed merely because epsilon is now finite.

<a id="c195-exact-signed-root-kernel"></a>
### Exact root kernel with every supplied multiplicity

Write the actual supplied C195 representation as

    B_epsilon(z)=z^(-15d) N_epsilon(z)/
                                    (L^2 D_epsilon(z)^2).

Let Z_epsilon be the multiset of ALL94d roots of N_epsilon and let P_epsilon be the multiset of ALL32d roots of D_epsilon.
Multiplicity is retained, including removable factors; denominator roots have weight2 in every formula below.
Neither polynomial has a root at0, D_epsilon has no circle root, and neither has an original alpha_i as a root, by the exact original value and denominator resultants in C195(RR6).
N_epsilon may have circle roots, whose logarithmic singularities are integrable.
Its leading coefficient is1024*49^3*q_epsilon^4 and that of D_epsilon is49*q_epsilon^2.
Thus the combined leading scalar is exactly

    c0=log[1024*49/L^2]=2log(7/k0),
    I_epsilon=c0+sum_(beta in Z_epsilon)log^+|beta|
                  -2sum_(gamma in P_epsilon)log^+|gamma|.
                                                            (SP3)

For w not among the original roots define

    K_P(w)=(1/d)log|P(w)|-log^+|w|
          =(1/d)sum_i log|w-alpha_i|-log^+|w|.
    Delta_epsilon=L_P-I_epsilon
       =sum_(beta in Z_epsilon)K_P(beta)
                   -2sum_(gamma in P_epsilon)K_P(gamma).
                                                            (SP4)

This is exact, not an absolute-value majorant.
To prove it, factor both actual polynomials with their displayed leading scalars, evaluate at every alpha_i, average in the ORIGINAL degree d, and subtract(SP3).
The monomial contributes -15d times the average log|alpha_i|, which is zero because the original constant coefficient is1.
The scalar c0 cancels between the two means.
This is cancellation of known scalars and original unit phases, not permission to omit them from an individual value or resultant.
A common zero of numerator and denominator contributes its net multiplicity automatically; no generic-epsilon exception is needed for(SP4).

For a literal pairing, repeat each member of P_epsilon twice and match these64d entries injectively to64d members of Z_epsilon.
Then(SP4) is the sum of64d differences K_P(beta)-K_P(gamma) and the remaining30d numerator terms.
The matching is only an identity; no geometrically favorable matching is assumed.
For any one pair, put delta=|beta-gamma|.
The direct triangle inequality and the1-Lipschitz property of w->log^+|w| give

    K_P(beta)-K_P(gamma)
       <=(1/d)sum_i log(1+delta/|gamma-alpha_i|)
                                             +delta. (SP5)

All denominators are nonzero by the original-root condition.
The Lipschitz property follows from the derivative bound for t->log^+t on[0,infinity) and ||beta|-|gamma||<=delta.
Thus small absolute root-pair distance is insufficient: a bound from(SP5) needs the relative distances to the SAME original roots and control of the unpaired kernel sum, with all64d/30d entries.
No such estimate follows from a fixed supplied rational degree.

<a id="c195-exact-signed-green-return"></a>
### The exact signed Green return and its30m term

The pole sign and multiplicity convention are the ones in [C36's full meromorphic argument](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) and [GO08-U001](../audits/literature/GO08/Yin_U001.md#go08-u001).
The latter supplies naming and sign attribution only, with its recorded conjugation-bar correction and source-proof limits preserved.
The finite-factor calculation here does not import its uncorrected printed pole formula or an uninspected general-domain theorem.

Put q_i=alpha_i when |alpha_i|<=1 and q_i=alpha_i^(-1) otherwise, retaining all d original entries even when folded points repeat.
For an interior q define the Poisson mean

    P_q f=integral_T [(1-|q|^2)/|z-q|^2] f(z) dmu(z),
    gamma(q,w)=log|(1-conjugate(w)q)/(q-w)|
                                      for |w|<1.

For |q_i|=1 use the boundary value f(q_i), and give each interior Green term value0 there.
This boundary value is finite and locally continuous because B_epsilon(q_i)=Q_i>0.
Let f_epsilon=log B_epsilon on the circle and set

    A_P(f_epsilon)=(1/d)sum_i P_(q_i)f_epsilon-I_epsilon,
    Zeta_epsilon=(1/d)sum_i sum_(beta in Z_epsilon,|beta|<1)
                                             gamma(q_i,beta),
    Pi_epsilon=(2/d)sum_i sum_(gamma in P_epsilon,|gamma|<1)
                                             gamma(q_i,gamma).
    Delta_epsilon=A_P(f_epsilon)+30m(P)
                                    +Pi_epsilon-Zeta_epsilon. (SP6)

Every zero and pole term is counted with its full polynomial multiplicity.
The Pi in(SP6) agrees with C195(RR15): for an outside original root, reciprocity pairs the outside denominator roots with their inverses inside, with the same multiplicities.
Zeta is the previously undiscarded NONNEGATIVE numerator-zero term, so Pi-Zeta may have either sign.

Here is the full elementary equality behind(SP6).
For a single root w, the boundary function log|z-w|-log^+|w| has Poisson mean log|1-conjugate(w)q| when |w|<1, and log|q-w|-log|w| when |w|>=1.
In the first case its actual value at q equals that mean minus gamma(q,w); in the other case it equals the mean without a Green term.
These formulas follow by the convergent logarithmic power series for a strict disk parameter and the geometric-series Poisson kernel.
For |w|=1, passage to the boundary factor is valid in L1: off a small arc convergence is uniform, while on that arc the logarithmic integral is bounded uniformly by a constant times delta(1+|log delta|), using |1-r e^(it)| bounded below by a constant times |t| for r>=1/2.
The fixed interior Poisson kernel is bounded, so this also passes the Poisson mean.
Apply this finite-factor identity to every numerator and denominator root, keeping the -15d log|q| term and c0.
Reciprocity gives B_epsilon(q_i)=B_epsilon(alpha_i); summing the monomial contribution gives
15 sum_i |log|alpha_i||=30m(P).
Original circle roots give their finite boundary values and no interior Green charge.
This proves(SP6), including possible numerator circle zeros and removable factors, without replacing a Haar mean by a supremum.

Dropping Zeta and replacing every Poisson mean by log sup B_epsilon recovers the old positive-pole upper bound.
Keeping it avoids that particular loss, but(SP6) still needs a bound on the COMPLETE angular term plus signed Green charge.
C193/C189's growing Wiener lower bound is not a bound on this signed sum, and separate divergence of Pi cannot decide it.

<a id="c195-original-contact-decomposition"></a>
### The surviving original contact term when g is nonzero

First suppose the actual field element g is nonzero, so every original g_i is nonzero.
Define

    Lambda_g=(1/d)sum_i log(g_i^2),
    C_P=(1/d)sum_i log(Q_i/g_i^2)>=0,
    D_G=Lambda_g-J_G
       =2[(1/d)log|Res(P,H35)|-m(H35)].
    Delta_epsilon=D_G+C_P-h_epsilon.             (SP7)

The D_G identity is exactly the original normalization of C177(T5), reused with the same unreduced H35, k0 and full degree d.
The new decomposition follows simply from L_P=Lambda_g+C_P and I_epsilon=J_G+h_epsilon.
It refines the already fixed C195(RR14) by retaining the nonnegative original-value term; it is not a new proof of that earlier resultant identity.
On the circle log(B_epsilon/G^2) is nonnegative almost everywhere and has integral h_epsilon tending to0.
At every original conjugate, its value is the epsilon-INDEPENDENT log(Q_i/g_i^2).
Thus even fixed-input L1 convergence cannot discard those original evaluation values.
C_P=0 exactly on the full residual branch f=e+s g=0: each summand is nonnegative because the trace field is totally real, and Q_i-g_i^2=(e_i+s g_i)^2+f_i^2.
Outside that branch C_P>0, without any newly claimed uniform lower bound over varying P.

There is also an exact divisor explanation of this surviving term.
Normalize away the scalar q_epsilon by setting

    Dtilde_epsilon=D_epsilon/q_epsilon^2
                =P^2 H35^2+k0^2 epsilon^2 z^(16d),
    Ntilde_epsilon=N_epsilon/q_epsilon^4
                =1024 H35^2 Dtilde_epsilon^2
                         +k0^4 epsilon^4 z^(32d)U_s.

As epsilon decreases to0 these converge coefficientwise, with unchanged nonzero leading coefficients, to P^2H35^2 and1024P^4H35^6.
The elementary bounded-root-list argument already used in C195 proves convergence of their full zero multisets, including all multiplicities.
More explicitly, roots are bounded by their fixed leading coefficients and bounded remaining coefficients; every convergent subsequence of ordered lists factors the limiting polynomial, forcing precisely its multiplicities in disjoint neighborhoods of its roots.
Writing mu_Q for the counting measure of all roots of Q, this gives weak convergence against continuous functions on a common compact set:

    mu_(N_epsilon)-2mu_(D_epsilon)
                       ->2mu_(H35).             (SP8)

The terms4mu_P cancel in this weak limit, but K_P is singular at the roots of P.
It is not legitimate to insert K_P into(SP8).

The precise local defect can be read without an unspecified root-matching theorem.
Since g!=0, P and H35 are coprime, and every alpha_i is a simple root of P.
Take disjoint small disks around the alpha_i, avoiding all roots of H35.
For all sufficiently small epsilon, the disk about alpha_i contains exactly two D_epsilon roots gamma_i1,gamma_i2 and four N_epsilon roots beta_i1,...,beta_i4.
Factor these local monic factors from Dtilde and Ntilde and call the remaining factors d_epsilon,i and n_epsilon,i.
Their evaluations at alpha_i tend respectively to

    P'(alpha_i)^2 H35(alpha_i)^2,
    1024 P'(alpha_i)^4 H35(alpha_i)^6.

The exact C195 original-value identity gives Ntilde(alpha_i)/Dtilde(alpha_i)^2=L^2 alpha_i^(15d)Q_i.
Consequently

    product_(j=1)^4(alpha_i-beta_ij)
      /product_(j=1)^2(alpha_i-gamma_ij)^2
                   ->Q_i/g_i^2.                 (SP9)

Indeed the ratio of the remaining factors tends to1024H35(alpha_i)^2, and L^2=1024k0^2 together with g_i^2=alpha_i^(-15d)H35(alpha_i)^2/k0^2 gives exactly the displayed limit.
Neither the original phases nor the scalar has been dropped.
For contributions to K_P from other original roots, and for log^+|w|, the local limits are continuous and their four-versus-four multiplicities cancel.
The contribution at alpha_i itself is the limit of the logarithm of the absolute value of the ratio in(SP9), divided by d.
All clusters at roots of H35 are away from P and give the continuous limit2mu_(H35).
Thus(SP4) has the exact limit

    lim Delta_epsilon
       =2sum_(H35(beta)=0)K_P(beta)+C_P
       =D_G+C_P=L_P-J_G.                         (SP10)

This supplies the missing singular-kernel justification for the finite contact term, while agreeing with the already fixed C195 limit.
When C_P>0, weak zero-pole cancellation cannot make all local relative displacements in(SP5) small: such a matching would force every cluster product in(SP9) to tend to1, contrary to at least one Q_i/g_i^2>1.
This is a fixed-input failure of that proposed cancellation shortcut, not a constructed near-one sequence or an impossibility theorem for a correctly paid varying-input estimate.

### The zero-g branch and the exact stopping boundary

If g=0, irreducibility gives P|H35 and all g_i vanish.
The root formulas(SP3)--(SP6), finite parameter(SP1) and the original L_P remain valid and finite.
The Haar J_G is still finite because the unreduced H35 is a nonzero polynomial of leading coefficient7.
Neither Lambda_g nor log|Res(P,H35)| is finite, so(SP7), the coprime clustering of(SP9) and its separate D_G interpretation MUST NOT be used.
Here keep only the exact finite identity

    Delta_epsilon=(L_P-J_G)-h_epsilon,
    0<h_epsilon<=eta.                            (SP11)

The equality holds for every positive rational epsilon; the bound h_epsilon<=eta here uses the specific choice in(SP1).
The weak divisor limit(SP8) now has mass at the singular original roots and supplies no passage to its K_P integral.
No logarithm of a zero norm or subtraction of infinite terms is asserted.

For g!=0 the same finite-parameter sandwich is more informative:

    D_G+C_P-eta<=Delta_epsilon<D_G+C_P.           (SP12)

In the full residual branch C_P=0, so after the complete signed cancellation the comparison remains the SAME unreduced-G resultant/Haar discrepancy D_G, up to the proved finite error h_epsilon.
Outside it, the additional nonnegative C_P must also be controlled.
The choice epsilon=1/M has not created an independent adjustable reduction of either term.
On the proposed useful-saving class, L_P>=tau and J_G<=tau-2eta imply L_P-J_G>=2eta and Delta_epsilon>=eta.
Thus an upper bound omega_eta(m(P)) tending to0 would genuinely exclude sufficiently small positive m(P) in this class; it is not obtained merely by rewriting the two means.
No such bound is proved in this round, and no assertion that this class contains a near-one sequence is made.

The missing input is now exact: either control the full signed kernel sum(SP4), equivalently the angular-plus-signed-Green expression(SP6), by the original total measure on a useful varying class, or obtain the corresponding arithmetic bound on D_G+C_P with its actual h_epsilon.
A bound built from direct root pairs must pay the relative original-root separations in(SP5) and the remaining30d terms.
The finite prescription(SP1)--(SP2) controls the Haar error but gives no uniform root-pair separation or signed-potential estimate.
The older positive pole charge and coefficient/Wiener lower bounds likewise do not supply or refute this complete comparison.
Root separation, precision or pole statistics may not be silently replaced by a function of m(P), and a favorable fixed-input weak divisor limit does not remove the contact term.

<a id="exact-inputs"></a>
## Inputs and independent-review boundary

| Input | Exact role |
| --- | --- |
| [Entire fixed regularizer and costs](Yin_C_G0195_v1.md#argument) | Actual original domain, nonzero original Q, full N/D/scalars, finite zero-compatible Haar error, rational parameter, degree and coefficient costs, and full fixed-input limit. |
| [Actual whole v1 finding](../audits/reviews/Yin_R_G0471_v1.md#rational-trace-regularizer-whole-independent-finding) | Accepted upstream proof and all costs, with present root author relationship disclosed; not evidence for SP3--SP12 or the new singular-kernel argument. |
| [Original trace-congruent construction](Yin_C_G0193_v1.md#argument) | Unchanged original values and unreduced functions; its construction does not supply the missing uniform signed error. |
| [Earlier exact G discrepancy](Yin_C_G0177_v1.md#polynomial-shear-actual-transfer-price) | T5 resultant/Haar normalization for the same H35, k0 and original degree; that formula is reused, not proved anew. |
| [Existing full-symbol cost boundary](Yin_C_G0189_v4.md#statement) | Known coefficient/Wiener growth is a comparison limit, not a bound on the signed kernel or a shrinking-error product. |
| [Existing meromorphic comparison](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) | Pole sign and supplied-factor conventions; the exact signed finite-factor identity is proved here. |
| [GO08 source unit](../audits/literature/GO08/Yin_U001.md#go08-u001) | Naming and sign attribution only, preserving its conjugation correction and source-proof inspection limits; no general-domain theorem is imported. |
| Elementary factor, Poisson and compactness arguments | Every finite-factor equality, boundary-circle limit, root-list convergence and local product ratio is explicitly proved in this version. |

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:29 |
| status | open |
| reason | Retain the complete signed numerator-minus-denominator comparison, Green equality, singular original contact term and actual finite-parameter costs at the existing rational-regularizer home. Physical v1 and its adopted review remain unchanged. Whole independent review of the new statements and all interfaces is required; no uniform transfer or draft completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete signed-comparison theorem](#statement) | All five assertions, original hypotheses, every epsilon, both signs, all supplied roots and multiplicities, circle/removable factors, nonzero-g and zero-g cases, local cluster ratios and full finite-parameter costs. |
| argument | [Complete SP1--SP12 proof](#argument) | Full root kernel, relative pairing fee, exact signed Green formula and30m, singular-kernel contact limit, finite sandwich and precisely unresolved uniform bound. |
| dependency | [Actual regularizer construction](Yin_C_G0195_v1.md#argument) | All original field values, N/D formulas, scalars, finite Haar error, rational parameter, coefficient/degree costs and earlier full fixed-input limit. |
| dependency | [Original G resultant normalization](Yin_C_G0177_v1.md#polynomial-shear-actual-transfer-price) | Only the exact T5 identity reused in D_G, with full original degree and same unreduced H35; no new uniform estimate is assumed. |
| support | [Whole independent upstream review](../audits/reviews/Yin_R_G0471_v1.md#rational-trace-regularizer-whole-independent-finding) | Actual accepted v1 coverage, preserving root's upstream authorship and no advance coverage of new SP statements. |
| support | [Existing trace-congruent construction](Yin_C_G0193_v1.md#argument) | Actual input comparison and original values at the fixed scope. |
| support | [Full-symbol cost comparison](Yin_C_G0189_v4.md#statement) | Exact limited coefficient/Wiener obstruction, not substituted for a full signed-error bound. |
| support | [Existing pole convention](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) | Positive-pole comparison recovered by discarding Zeta; the new equality keeps its omitted term. |
| support | [Source attribution and correction boundary](../audits/literature/GO08/Yin_U001.md#go08-u001) | Names/signs only, with the actual correction and inspection limits; proof here is elementary and explicit. |
| support | [Complete input boundary](#exact-inputs) | Every used input, both authors, old versus new proof roles, finite original and Haar conventions and no computation or automatic near-one coverage. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:41 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the complete signed comparison and original contact theorem through actual whole R479. Retain every supplied root and multiplicity, the exact30m radial term, signed Green charges, the fixed-input local cluster product and epsilon-independent contact term, and all finite parameter costs. The zero-g branch and selected-parameter eta bound keep their explicit scopes. Weak divisor cancellation does not remove the contact term, and the full residual case still requires the same unreduced-G resultant/Haar estimate. This is no uniform transfer bound, automatic near-one coverage or draft completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete signed-comparison theorem](#statement) | All five assertions, original hypotheses, every epsilon, both signs, all supplied roots and multiplicities, circle/removable factors, nonzero-g and zero-g cases, local cluster ratios and full finite-parameter costs. |
| argument | [Complete SP1--SP12 proof](#argument) | Full root kernel, relative pairing fee, exact signed Green formula and30m, singular-kernel contact limit, finite sandwich and precisely unresolved uniform bound. |
| dependency | [Actual regularizer construction](Yin_C_G0195_v1.md#argument) | All original field values, N/D formulas, scalars, finite Haar error, rational parameter, coefficient/degree costs and earlier full fixed-input limit. |
| dependency | [Original G resultant normalization](Yin_C_G0177_v1.md#polynomial-shear-actual-transfer-price) | Only the exact T5 identity reused in D_G, with full original degree and same unreduced H35; no new uniform estimate is assumed. |
| support | [Whole upstream review](../audits/reviews/Yin_R_G0471_v1.md#rational-trace-regularizer-whole-independent-finding) | Actual accepted v1 coverage, preserving root's upstream authorship and no advance coverage of new SP statements. |
| support | [Existing trace-congruent construction](Yin_C_G0193_v1.md#argument) | Actual input comparison and original values at the fixed scope. |
| support | [Full-symbol cost comparison](Yin_C_G0189_v4.md#statement) | Exact limited coefficient/Wiener obstruction, not substituted for a full signed-error bound. |
| support | [Existing pole convention](Yin_C_G0036_v1.md#rational-completion-meromorphic-pole-cost) | Positive-pole comparison recovered by discarding Zeta; the new equality keeps its omitted term. |
| support | [Source attribution and correction boundary](../audits/literature/GO08/Yin_U001.md#go08-u001) | Names/signs only, with the actual correction and inspection limits; proof here is elementary and explicit. |
| support | [Complete input boundary](#exact-inputs) | Every used input, both authors, old versus new proof roles, finite original and Haar conventions and no computation or automatic near-one coverage. |
| review | [Whole signed-comparison finding](../audits/reviews/Yin_R_G0479_v1.md#signed-rational-contact-whole-independent-finding) | Entire actual SP1--SP12 and all five statement assertions, every input/dependency/support, full supplied scalar and root accounting, circle/removable factors, Green signs, singular local limits, both g branches and precisely selected finite-eta costs; final notation and scope clarifications actually read. |

