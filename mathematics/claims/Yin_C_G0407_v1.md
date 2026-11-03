---
author: Yin
---

# Mixed actual units, rational symbol thresholds and complete signed energy costs

This retains the complete necessary mathematical argument from [Complete original mixed-unit account](../ledger/Yin_L_G0372_v1.md#mixed-unit-reuse-and-domain).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be any actual monic irreducible reciprocal nontorsion polynomial in Z[t] with constant term1 and degree d=2s, let alpha be an actual root, K=Q(alpha), tau=alpha+alpha^-1, F=Q(tau), O=Z[alpha], B=Z[tau], and let sigma be the reciprocal K/F involution.
Retain the actual decomposition O=B direct-sum alpha B, the monic degree-s trace polynomial Q, and C_l(x) defined by C_l(t+t^-1)=t^l+t^-l.
For any finite actual unit family u_i in O^times, put c_i=u_i sigma(u_i) and reduce its unique integral representative to C_i(x)=b_i+sum_(l=1)^(s-1)b_(il)C_l(x), with every full Norm_K(u_i)=+1 or-1 retained.
Use any one common actual original residual window N>d, T=N-1 and common positive integer q: all monomial residuals F_j and selected unit residuals F_i retain their actual integral coefficients and contents and evaluate to q alpha^j and q u_i at every original root.
Let nonnegative real weights w_j,theta_i sum to1, w_0=sum_j w_j, and define G(t)=q^-2[sum_j w_j F_j(t)F_j(t^-1)+sum_i theta_i F_i(t)F_i(t^-1)]=E+sum_(l=1)^T H_l(t^l+t^-l), with E>0 and kappa=2sum_l|H_l|/E.
All original absolute resultants equal q^d; the true normalized surplus is -(1/2)log E, and the scalar target is E<=1/2.

For every such family the complete all-root quotient is E+sum_l H_l C_l(x)==w_0+sum_i theta_i C_i(x) mod Q.
If every lag l>=s vanishes, equality holds as polynomials of degree below s, giving the entire actual nonnegative circle symbol G=w_0+sum_i theta_i C_i(t+t^-1), E=w_0+sum_i theta_i b_i and H_l=sum_i theta_i b_(il) for1<=l<s.
Neither a trace identity nor a nonnegative relaxed symbol establishes actual residual covariance.
Under these cancellations, rational original weights of least denominator M give integers m_i=Mtheta_i,m_0=Mw_0 summing to M and A_M=MG=m_0+sum_i m_i C_i in Z[x].
At the target, its mean n_M=ME is an integer between1 and M/2.
The least integer L clearing every coefficient E,H_l divides M; it is distinct from original M and residual coefficient denominator q.
A nonconstant symbol requires L>=4, and a nonconstant symbol outside scaled 2 plus/minus one frequency, or any strictly positive nonconstant symbol, requires L>=6.
Consequently M<=3 allows only constants; M<=5 allows only constants or those scaled binomials, whose nonconstant cases have actual circle zeros.
These facts bound no original M from L alone and cancel no q-cost before the exact quotient is proved.

The relaxed example A=3+C_1+C_2=x^2+x+1 has G=A/6, exact L6, E=1/2, H_1=H_2=1/6, kappa=4/3 and minimum G=1/8 on the circle.
No finite collection of integer Laurent polynomials has squared moduli summing to A: the full coefficient energy3 exhausts the three-monomial, binomial-plus-monomial and trinomial cases.
The exact repair 4A=|2+t+2t^2|^2+3|1|^2 makes rational coefficient denominator2 sufficient and denominator1 impossible.
If an actual aggregate A_M equals A, then all positively weighted F_a/q cannot be integral; the displayed repair alone gives no actual input, unit norms or residual realization.

Assume now that P is a genuine Salem polynomial with beta>1, total m=log beta and s-1 unit-circle inverse pairs.
A selected full norm+1 makes c_i totally positive with Norm_F(c_i)=1 and t_i=Tr_F(c_i)/s>=1.
Exact constant G therefore forces E=1+sum_i theta_i(t_i-1); any number of positive-full-norm units gives E>=1 at every window.
With negative full norms, sum_neg theta_i(1-t_i)=1-E+sum_pos theta_i(t_i-1)>=1-E, without assigning positivity to a negative exterior trace value.
For arbitrary covariance, define e_i=||F_i||^2/q^2, p_-=sum_neg theta_i, E_-=sum_neg theta_i e_i, V_-=sum_(j=0)^T beta^(-2j), chi=V_-/s<=N/s, u_0=Tm/d, g=exp(-2u_0), Gamma_l=[beta^-l+sum_(j=1)^(s-1)cos(l theta_j)]/s and delta=max_(1<=l<=T)|Gamma_l|.
At every positive m the original two-real-embedding Cauchy--Schwarz bounds and whole signed Poisson majorant give chi E_->=g(1-p_-)-E(1+kappa delta), hence E_->=(s/N)[g(1-p_-)-E(1+kappa delta)]_+.
With rational original weights under the forced identity and total negative integer multiplicity K_-, the equivalent bound is sum_neg m_i e_i>=(s/N)[g(M-K_-)-n_M(1+kappa delta)]_+.
In particular N<=Cd, E<=1/2, g>=3/4, kappa delta<=1/4 and K_-<=M/12 imply that full negative-copy energy is at least M/(32C).
Only the optional estimate delta<=epsilon(u_0)+2u_0 uses the retained small-height domain 0<u_0<=h_0, c_0=log2/4, h_0=c_0 exp(-20), b(u)=max{u,sqrt(u/c_0)log sqrt(c_0/u)}, epsilon(u)=min{1,15sqrt(b(u))+4u}; the exact energy inequalities require no such approximation.

For the accepted actual irreducible Salem input P=t^4-2t^3+t^2-2t+1, Q=x^2-2x-1 and tau_+=1+sqrt2=beta+beta^-1, the actual integral units u_+=tau=2+2alpha^2-alpha^3 and u_-=(1-alpha)^-1=2+alpha^2-alpha^3 have full norms+1 and-1, c_+=tau^2, c_-=-tau, and c_++2c_-=1.
Their weights1/3,2/3 yield the algebraic constant profile1/3; only actual high-lag cancellation would imply G=E=1/3 and surplus(log3)/2.
The untwisted actual residuals instead obey E>20/27>1/2 for every N>d, by the contracting original root, so this actual unit lift fails every unshifted scalar target.
For every integer common twist k, with A_c=tau_+^2+2/(1-beta^-1)^2, A_e=tau_+^2+2/(1-beta)^2 and V_+=sum_(j=0)^T beta^(2j), their same-window weighted energy necessarily satisfies E_k>=max{beta^(-2k)A_c/(3V_-),beta^(2k)A_e/(3V_+)}>=sqrt(A_c A_e)/(3sqrt(V_-V_+)).
These are necessary costs, with no attainment, optimal integer twist, cheap family or covariance inferred.

The integral aggregate has center Mq^2E and lags Mq^2H_l, and full signed norm product q^(dM)product_i Norm_K(u_i)^(m_i), including every multiplicity parity and primitive content.
All original d,N,T,q,M,L, remaining signed correlations and radial charge Tm(P)/d remain distinct and fully paid.
The complete arguments below prove precisely these finite-symbol, full-sign, actual-unit and failure statements; they supply no near-one sequence, unrestricted gap, new source theorem, native computation or research resumption.

## Current assessment
[Selected decision](#decision-current-actual-quartic-home-maintenance)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:08 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Actual one-unit quotient](Yin_C_G0397_v1.md#one-unit-trace-quotient-identity) | Exact actual order, relative-norm basis, original residual evaluation and complete signed norm identity; finite linear extension is proved here. |
| dependency | [Complete integer mean-two theorem](Yin_C_G0403_v1.md#integer-mean-two-classification) | Only whole-circle nonnegative integral Laurent symbols, strict Fourier coefficients, full classification and actual circle zeros; no relaxed-to-actual realization. |
| dependency | [Full signed norm and damping input](Yin_C_G0378_v2.md#positive-norm-trace-penalty) | Genuine Salem positivity for positive full norms and original reversal/Poisson interface; no inverse-pair theorem applied to a general mixture. |
| dependency | [Original asymmetric cost boundary](Yin_C_G0385_v3.md#asymmetric-original-costs-and-next-gate) | Actual original weights and normalization must remain visible; symbolic trace identities are not covariance. |
| dependency | [Actual irreducible quartic family](../ledger/Yin_L_G0265_v1.md#actual-quartic-trace-unit-family) | Only the a=2 actual irreducible Salem polynomial, full original roots, order and positive total measure; no full orbit-energy result imported. |
| dependency | [Complete signed Poisson majorant](../ledger/Yin_L_G0318_v1.md#polynomial-poisson-majorant) | Fixed-window reversal and all signed autocorrelations before taking absolute values; no high-lag hypothesis for the damped energy inequality. |
| dependency | [Original angular input](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Only the optional increasing epsilon at its exact small-u domain and unchanged original degree, multiplicity and Pri11/Dim19 source scope. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:09 |
| status | proved |
| reason | Adopt the actual complete current SELF finding after checking the entire exact theorem and retained proof, necessary fixed inputs and original whole-review/author-check scopes. All denominators, full signs, actual-versus-relaxed boundaries, universal unshifted failure and original expenses are retained; no new computation, independent outcome or research resumption is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0397_v1.md#one-unit-trace-quotient-identity) | Exact actual order, relative-norm basis, original residual evaluation and complete signed norm identity; finite linear extension is proved here. |
| dependency | [Exact accepted input](Yin_C_G0403_v1.md#integer-mean-two-classification) | Only whole-circle nonnegative integral Laurent symbols, strict Fourier coefficients, full classification and actual circle zeros; no relaxed-to-actual realization. |
| dependency | [Exact accepted input](Yin_C_G0378_v2.md#positive-norm-trace-penalty) | Genuine Salem positivity for positive full norms and original reversal/Poisson interface; no inverse-pair theorem applied to a general mixture. |
| dependency | [Exact accepted input](Yin_C_G0385_v3.md#asymmetric-original-costs-and-next-gate) | Actual original weights and normalization must remain visible; symbolic trace identities are not covariance. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0265_v1.md#actual-quartic-trace-unit-family) | Only the a=2 actual irreducible Salem polynomial, full original roots, order and positive total measure; no full orbit-energy result imported. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0318_v1.md#polynomial-poisson-majorant) | Fixed-window reversal and all signed autocorrelations before taking absolute values; no high-lag hypothesis for the damped energy inequality. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0229_v1.md#uniform-powered-angular-coherence) | Only the optional increasing epsilon at its exact small-u domain and unchanged original degree, multiplicity and Pri11/Dim19 source scope. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0611_v1.md#current-mixed-unit-whole-finding) | Entire exact Statement and complete necessary mathematical argument, all original signed/denominator/covariance/cost and source limits, with the separately preserved original author check and established SELF R275 history. |


### Decision current-actual-quartic-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:58 |
| status | proved |
| reason | Maintain only the same-object current a2 actual quartic proof home at complete C464 after full consumer proof/current-finding reading and exact irreducibility/trace/root/order/measure comparison. Original mathematics, formulas, all OTHER selected fields/tuples/reviews, dated old input/read accounts and decisions remain unchanged. The new R671 finding is narrow administrative SELF, not a new whole mathematical or isolated review; existing whole relationship and actual old L265 bindings remain. No source proof/native run, near-one input or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0397_v1.md#one-unit-trace-quotient-identity) | Exact actual order, relative-norm basis, original residual evaluation and complete signed norm identity; finite linear extension is proved here. |
| dependency | [Exact accepted input](Yin_C_G0403_v1.md#integer-mean-two-classification) | Only whole-circle nonnegative integral Laurent symbols, strict Fourier coefficients, full classification and actual circle zeros; no relaxed-to-actual realization. |
| dependency | [Exact accepted input](Yin_C_G0378_v2.md#positive-norm-trace-penalty) | Genuine Salem positivity for positive full norms and original reversal/Poisson interface; no inverse-pair theorem applied to a general mixture. |
| dependency | [Exact accepted input](Yin_C_G0385_v3.md#asymmetric-original-costs-and-next-gate) | Actual original weights and normalization must remain visible; symbolic trace identities are not covariance. |
| dependency | [Complete actual quartic input](Yin_C_G0464_v1.md#actual-quartic-trace-unit-family) | Same actual a2 irreducible Salem polynomial, all four original roots/trace/order and fixed positive total measure only; no full orbit-energy result imported. |
| dependency | [Exact accepted input](Yin_C_G0600_v1.md#polynomial-poisson-majorant) | Fixed-window reversal and all signed autocorrelations before taking absolute values; no high-lag hypothesis for the damped energy inequality. |
| dependency | [Exact accepted input](Yin_C_G0570_v1.md#uniform-powered-angular-coherence) | Only the optional increasing epsilon at its exact small-u domain and unchanged original degree, multiplicity and Pri11/Dim19 source scope. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0611_v1.md#current-mixed-unit-whole-finding) | Entire exact Statement and complete necessary mathematical argument, all original signed/denominator/covariance/cost and source limits, with the separately preserved original author check and established SELF R275 history. |
| review | [Actual narrow quartic-home SELF finding](../audits/reviews/Yin_R_G0671_v1.md#quartic-current-consumer-home-finding) | Only same-object a2 actual polynomial/field/root/order/measure and current proof-home comparison; no new whole consumer verdict, changed mathematical scope or fresh isolated coverage. All original whole findings and their actual old L265 inputs remain. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="mixed-unit-reuse-and-domain"></a>
## 1. Exact reuse and the multi-unit domain

The complete [L367 one-unit quotient](Yin_C_G0397_v1.md#one-unit-trace-quotient-identity) supplies the original order decomposition, all-root coefficient identity and exact low-lag feasibility boundary.
[L370 mean-two theorem](Yin_C_G0403_v1.md#integer-mean-two-classification) supplies the complete integer-symbol classification and its source/proof limits.
[L357](Yin_C_G0378_v2.md#positive-norm-trace-penalty) supplies the full signed norm/Salem positivity and damped Poisson interface, while [L362](Yin_C_G0385_v3.md#asymmetric-original-costs-and-next-gate) already warns against deleting actual weight normalization or inferring covariance from a symbolic pass.
The actual quartic input below is the a=2 specialization of [L265](../ledger/Yin_L_G0265_v1.md#actual-quartic-trace-unit-family), with its retained irreducibility and complete Salem roots.

A bounded local ledger screen for mixed units, norm-sign mass, trace-unit sums and symbol denominators found these relevant interfaces and no theorem covering the changed multi-unit statements below.
No priority claim follows.
The new proofs use finite polynomial linearity, the already proved mean-two classification, elementary coefficient energy, weighted arithmetic/geometric mean and full-root Cauchy--Schwarz.
No new external theorem, source intake, native mathematical program or J is used.
Root supplied only the assigned question; all new deductions and the actual quartic identity are by integer_bundle_research AI for Yin.

Let P be an ACTUAL monic irreducible reciprocal nontorsion integer unit polynomial of degree d=2s.
Keep the original trace polynomial Q, tau=alpha+alpha^-1, original order O=Z[alpha], trace order B=Z[tau], and K/F quadratic reciprocal involution sigma as in L367.
For finitely many actual order units u_i, their complete signed norms are+1 or-1 and c_i=u_i sigma(u_i) has its actual integral representative C_i(x) of degree<s.
Write

    C_i(x)=b_i+sum_(l=1)^(s-1) b_(il) C_l(x),
    b_i,b_(il) in Z.                                  (1)

Choose the same ACTUAL original window N>d, T=N-1, common integer q and residuals F_j for every monomial and F_i for each selected unit, keeping every coefficient and content.
Nonnegative real weights w_j,theta_i sum to1; put w_0=sum_j w_j.
Define E,H_l,G exactly by the full weighted squares, divided by q^2.
Each original absolute resultant is q^d, so true surplus is-(1/2)log E and kappa=2sum_l|H_l|/E.
The target remains E<=1/2.

The same all-root calculation gives the COMPLETE quotient identity

    E+sum_(l=1)^T H_l C_l(x)
                   ==w_0+sum_i theta_i C_i(x) (mod Q).  (2)

If every lag l>=s vanishes, this is an exact degree-below-s polynomial identity.
In particular the entire actual nonnegative circle symbol is

    G(t)=w_0+sum_i theta_i C_i(t+t^-1),
    E=w_0+sum_i theta_i b_i,
    H_l=sum_i theta_i b_(il), 1<=l<s.                 (3)

Individual C_i need not be globally nonnegative; only the ACTUAL full sum G must be.
All cancelled AND unselected correlations come from the same original weights.
A trace identity supplies no nonnegative residual realization by itself.

<a id="rational-symbol-denominator-tradeoff"></a>
## 2. Charged rational denominators determine the first possible symbol shapes

Assume all original weights are rational and M is their ACTUAL least common denominator, including the separate monomial columns.
Let m_i=Mtheta_i and m_0=Mw_0.
Then m_0,m_i are nonnegative integers summing to M.
Under the low-lag hypothesis in(3),

    A_M(x)=m_0+sum_i m_i C_i(x) in Z[x], degree<s,
    M G(t)=A_M(t+t^-1),
    n_M=M E=m_0+sum_i m_i b_i in Z,
    1<=n_M<=M/2.                                    (4)

Thus the old projection denominator q cancels in this FORCED symbol only after the exact quotient identity has been proved.
It is still charged in the original coefficients and norms.
Without the high-lag cancellations, M alone need not clear the actual q^-2 coefficient correlations.

Let L be the least positive integer clearing EVERY coefficient E,H_1,...,H_(s-1) of this forced symbol.
Then L divides M.
This is an intrinsic SYMBOL denominator, distinct from the actual original weight denominator M.
The nonnegative integer Laurent polynomial A=L G has positive integer mean n=L E<=L/2.

**Proposition 1.** If the actual low-lag symbol is nonconstant, then L>=4.
If it is nonconstant and is not a constant multiple of2 plus/minus one Chebyshev frequency, then L>=6.
Every STRICTLY positive nonconstant actual low-lag symbol also requires L>=6.

*Proof.* When n=1, the strict Fourier inequality from L370 makes every nonconstant INTEGER coefficient smaller than1 in modulus, hence zero.
When n=2, L370 gives A=2 or2+sigma(t^j+t^-j).
The latter has actual circle zeros.
Nonconstant symbols consequently require n>=2 and L>=2n>=4; any other shape or strictly positive nonconstant symbol requires n>=3 and L>=6.
All conclusions apply to the exact forced aggregate, not to independently varying Fourier coefficients.
For charged original M<=3 only constant symbols can occur; for M<=5 the constant or scaled binomial cases exhaust the possibilities, even if L is smaller than M.

There is no bound on an original weight denominator from an intrinsic L alone.
Distinct monomial weights can produce the same small-denominator aggregate.
Equations(4) retain the actual integer multiplicities and the separate coefficient normalization.

<a id="mean-three-rational-square-control"></a>
## 3. Denominator six permits a new positive shape, but a second denominator remains necessary

The exact polynomial

    A(t)=3+C_1(x)+C_2(x)=x^2+x+1,
    G=A/6, x=t+t^-1                                  (5)

has actual symbol denominator L=6, E=1/2, H_1=H_2=1/6 and full kappa=4/3.
It is strictly positive everywhere: x^2+x+1=(x+1/2)^2+3/4, so G>=1/8 on the circle.
It proves that the mean-two rigidity genuinely ends at this next denominator in the nonnegative-symbol relaxation.
No actual input P, units or original residual realization is asserted by(5).

Moreover A cannot be a sum of squared moduli of ANY finite collection of integer Laurent polynomials.
If A=sum_nu |Q_nu|^2, its mean3 would force exactly three nonzero+/-1 coefficients across all Q_nu; any coefficient of magnitude2 would already cost4.
Three monomials give a constant.
A binomial and a monomial give only3 plus/minus one frequency.
A single trinomial at positions a<b<c has pair differences g=b-a,h=c-b,g+h.
If g!=h there are three distinct nonzero frequencies, all with coefficients+/-1.
If g=h, the coefficient at g is0 or+/-2, and that at2g is+/-1.
Neither case has precisely the two coefficients+1 at frequencies1 and2 in(5).
Laurent shifts do not change this argument.

The obstruction is exact and is repaired by a PAID denominator2:

    4A(t)=|2+t+2t^2|^2+3|1|^2.                      (6)

Coefficient expansion gives mean12 and coefficients4 at both frequencies1,2, proving(6) directly.
Therefore A has rational squared-modulus representation with coefficient denominator2, while coefficient denominator1 is impossible.
This does not authorize integral Fejer-Riesz factorization at mean3.

For an actual rational-weight residual bundle, equation(4) also gives

    A_M(t+t^-1)=q^-2 sum_a m_a |F_a(t)|^2

on the circle, with all original coefficients retained.
If A_M equals the example A, then q=1, or more generally F_a/q integral for EVERY positive label, would contradict the integer-square obstruction.
A genuine residual coefficient denominator is thus required in such a realization.
Formula(6) alone supplies no original unit norms, original polynomial, kernel multipliers or nonnegative residual weights.
Both the actual weight denominator and this residual-square denominator must remain visible.

The generic need for a nontrivial residual denominator at E<1 is already elementary: a nonzero integral F_a/q has squared coefficient energy at least1.
That generic scalar observation is not new mathematical income here.
The additional mean-three fact is the exact failure of EVERY integral squared-modulus decomposition of A and its explicit rational denominator2 repair, which identifies why the mean-two integral square argument cannot simply be continued.

<a id="mixed-signed-unit-constant-obstruction"></a>
## 4. Positive full norms cannot yield exact constant surplus on a Salem input

Assume now P is a genuine Salem input.
The trace field F is totally real with one exterior trace embedding and s-1 circle embeddings.
At circle embeddings c_i=|u_i|^2>0.
Signed Norm_K(u_i)=+1 makes c_i totally positive with complete Norm_F(c_i)=1, as in L357.
Therefore its mean trace t_i=s^-1 Tr_F(c_i) is at least1 by arithmetic/geometric mean.

If G in(3) is exactly constant, its all-trace-root identity is

    E=w_0+sum_i theta_i c_(ij) for every j,
    E=1+sum_i theta_i(t_i-1).                       (7)

When every selected full norm is+1 this gives E>=1.
Thus exact complementarity and ANY positive true surplus are impossible for ANY number of positive-norm actual units, at every original window.
This is stronger than the one-unit obstruction within its genuine Salem/sign scope and uses no inverse symmetry.

With negative-norm units present, (7) requires the exact deficit

    sum_(i:Norm u_i=-1) theta_i(1-t_i)
      =1-E+sum_(i:Norm u_i=+1) theta_i(t_i-1)
      >=1-E.                                        (8)

At the target, this is at least1/2.
Merely including a negative norm label is insufficient: its ACTUAL full trace deficit must pay(8).
No positivity theorem is imposed on its negative exterior embedding.
Trace degree s is used in this proved auxiliary relation, not substituted for original norm income or actual d.

<a id="negative-unit-mass-energy-cost"></a>
## 5. Tiny negative-norm mass is paid by actual coefficient energy

Continue on a genuine Salem input with expanding beta>1, total m=log beta, T=N-1 and u_0=Tm/d.
Let

    p_-=sum_(Norm u_i=-1) theta_i,
    E_-=sum_(Norm u_i=-1) theta_i e_i,
    e_i=||F_i||^2/q^2,
    V_-=sum_(j=0)^T beta^(-2j), chi=V_-/s<=N/s,
    g=exp(-2u_0),
    Gamma_l=[beta^-l+sum_(j=1)^(s-1)cos(l theta_j)]/s,
    delta=max_(1<=l<=T)|Gamma_l|.                    (9)

The weights include every original monomial and actual unit; E is their complete energy and kappa pays ALL remaining lags.
No low-lag cancellation is needed for the following inequality:

    chi E_- >=g(1-p_-)-E(1+kappa delta),
    E_- >=(s/N)[g(1-p_-)-E(1+kappa delta)]_+.        (10)

*Proof.* At each trace embedding use damping lambda_0=beta^-T and lambda_j=1 on the s-1 circle coordinates.
A positive-norm unit has positive c_i and full norm1, so its damped mean is at least(product lambda)^(1/s)=g.
A monomial c=1 has damped mean at least g as well.
For a negative-norm unit, its exterior c_(i0)<0 and every circle value is positive.
Its damped mean is therefore at least-beta^-T|c_(i0)|/s.

At both ACTUAL original real roots, F_i/q=u_i.
Cauchy--Schwarz with all N original coefficients bounds |c_(i0)| by e_i sqrt(V_+V_-), where V_+=sum_(j=0)^T beta^(2j)=beta^(2T)V_-.
Hence beta^-T|c_(i0)|/s<=chi e_i.
The full aggregate damped trace is consequently at least g(1-p_-)-chi E_-.
The same original reversal/Cauchy/Poisson argument proved in L357 bounds it ABOVE by E+2sum H_l Gamma_l<=E(1+kappa delta).
This proves the first(10).
Since0<chi<=N/s, rearrangement gives the second, including a nonpositive bracket via the positive part.
No original expanding/contracting coordinate or signed norm is discarded.

For rational original weights of least denominator M, let K_- be the total integer multiplicity of negative-norm units.
Under(4), E=n_M/M and p_-=K_-/M.
Thus

    sum_(Norm u_i=-1) m_i e_i
       >=(s/N)[g(M-K_-)-n_M(1+kappa delta)]_+.       (11)

This is an exact denomination/energy tradeoff.
For example if N<=C d, E<=1/2, g>=3/4, kappa delta<=1/4 and K_-<=M/12, then the bracket is at least M/16 and the complete negative-unit energy cost is at least M/(32C).
A bounded number of negative integer copies at growing denominator cannot remain uniformly cheap under THESE explicit analytic conditions.
They might be assigned tiny weights only by paying a growing individual residual energy; that energy is part of the original bundle, not free norm income.

Only a later estimate delta<=epsilon(u_0)+2u_0 uses L229's exact small-u domain.
The exact formulas(9)--(11) apply at every positive m.
They provide a necessary cost, not the existence of a near-one sequence or a new uniform gap theorem.

<a id="new-quartic-mixed-unit-identity"></a>
## 6. A new actual mixed-unit identity at denominator three, and its all-window energy failure

Use the ACCEPTED a=2 member of L265:

    P=t^4-2t^3+t^2-2t+1,
    Q=x^2-2x-1,
    tau=alpha+alpha^-1, tau^2=2tau+1.             (12)

This is an actual irreducible degree-four Salem unit, with trace conjugates1+sqrt2>2 and1-sqrt2 in(-1,0), and original expanding beta satisfying beta+beta^-1=1+sqrt2.
Its COMPLETE total measure is m=log beta, fixed positive.
These original input facts are reused from L265, not a new root scan or near-one family.

There are two explicit actual order units, with full original degree-four norm signs retained:

    u_+=tau=2+2alpha^2-alpha^3, Norm_K(u_+)=+1,
    u_-=(1-alpha)^-1=2+alpha^2-alpha^3, Norm_K(u_-)=-1,
    c_+=u_+sigma(u_+)=tau^2,
    c_-=u_-sigma(u_-)=(2-tau)^-1=-tau,
    c_++2c_-=1.                                    (13)

For verification, tau is a trace-order unit with inverse tau-2 and full Norm_K(tau)=Norm_F(tau)^2=1.
Also P(1)=-1 and

    P(t)+1=(t-1)(t^3-t^2-2),

so the displayed integral inverse of1-alpha is exact and its full norm is P(1)^-1=-1.
The identity(2-tau)(-tau)=1 follows from the ACTUAL Q.
Both c_+,c_- are nonconstant, so these units are not signed monomial powers of alpha.
No individual original conjugate is dropped in their norms.

Weights1/3 on u_+ and2/3 on u_- have actual unit lifts and give the constant trace-quotient profile1/3.
If the high-lag actual covariance vanished, the forced symbol would be G=1/3, E=1/3 and eta=log3/2, with intrinsic L=3 and n=1.
This passes the algebraic/unit-sign/denominator screens and exhibits a genuine multi-unit mechanism unavailable to one actual unit.
It is not merely an average of the old source33/source34 optimum.

However the UNTWISTED actual residuals cannot satisfy even the scalar target at ANY N>d.
Let x=beta^-1 and use the contracting original root.
For any common q and any actual residual F_+, Cauchy--Schwarz gives

    e_+>=tau_+^2/[sum_(j=0)^T x^(2j)]
       >(1-x^2)tau_+^2,
    E=(e_++2e_-)/3>20/27>1/2.                    (14)

Here tau_+=1+sqrt2>2.
Moreover beta>3/2 because beta+beta^-1=tau_+>13/6 and y+y^-1 is increasing for y>1; hence x<2/3 and1-x^2>5/9.
Formula(14) retains a REAL original-conjugate lower bound on the FULL coefficient energy, and is independent of an uncomputed projector.
It decisively separates actual unit lifting and an algebraically constant profile from feasible original residual energy.
No mathematical program or fixed-window test is needed for this failure.

Common signed monomial twists do preserve(13)'s relative norms, but change their actual original evaluations.
For u_(+,k)=alpha^k u_+ and u_(-,k)=alpha^k u_-, every integer k is an actual order-unit move.
Define positive original constants

    A_c=tau_+^2+2/(1-beta^-1)^2,
    A_e=tau_+^2+2/(1-beta)^2,
    V_+=sum_(j=0)^T beta^(2j), V_-=sum_(j=0)^T beta^(-2j).

Their SAME fixed-window actual weighted residual energy must satisfy

    E_k>=max{beta^(-2k) A_c/(3V_-),
             beta^(2k) A_e/(3V_+)},
    E_k>=sqrt(A_c A_e)/(3sqrt(V_-V_+)).              (15)

These are necessary bounds at both original real embeddings, followed by max>=geometric mean.
No attainment, optimal integer k, cheap twisted family or correlation cancellation is inferred.
They show exactly what a prospective twist must pay before being called a useful covariance repair.
The original window, all contents, both full norm signs and every remaining lag still have to be checked; the constant quotient relation alone remains insufficient.

<a id="mixed-unit-costs-and-boundary"></a>
## 7. Original costs, findings and next discriminator

All material uses the original d,N,T,q, actual integer auxiliaries and their entire signed correlations.
At rational original weights M, the actual integral aggregate is sum_a m_a F_a(t)t^T F_a(t^-1), with center Mq^2 E and lag coefficients Mq^2 H_l.
Its complete signed norm product is q^(dM)product_i Norm_K(u_i)^(m_i).
Negative signs retain every multiplicity parity.
Individual primitive contents are never removed.
Intrinsic symbol denominator L, original weight denominator M and original residual coefficient denominator q are distinct, with L|M only under the PROVED low-lag identity.
The radial expense stays Tm(P)/d on original total measure and degree.

The changed general findings are the exact denominator threshold, the positive mean-three noninteger-square example with its paid denominator repair, the arbitrary-positive-norm constant obstruction, and the negative-sign mass/energy localization(10)--(11).
The changed actual input is the lifted mixed relative-unit identity(13), whose unshifted residual realization is rigorously excluded for every window by(14).
Neither that failure nor the mean-three symbolic example settles a twisted or other multi-unit covariance.
