---
author: Yin
---

# Near-one coefficient and convolution budgets in the retained collar recipe

Date: 2026-10-08--09.
Bounded G0001 derivation by the coordinating AI and the assigned execution_and_deliverables AI for Yin, with the separate endpoint/discriminant gate contributed by entropy_status.
The coordinator accepted this result for fixed-ledger preservation on 2026-10-09 after the complete independent review recorded below.
No numerical mathematical run, optimization or new source intake is involved.
The mathematical cost below concerns the specified sufficient recipe, not the actual least energy window or a necessary orbit length.

<a id="convolution-norm-mahler-bound"></a>
## 1. A retained norm mechanism also bounds the actual convolution norm

First let P be any monic irreducible noncyclotomic integer polynomial of degree d with nonzero constant coefficient.
Write

    m=log M(P)>0, W=sum_k |p_k|,
    H_inf=max_(|z|=1) |P(z)|,             1<=H_inf<=W.

The lower bound H_inf>=1 follows, for example, by integrating |P|^2 on the circle and retaining its monic coefficient.
The maximum modulus principle, applied inside the disk to P and to t^d P(1/t), gives

    |P(z)|<=H_inf max(1,|z|)^d              for every complex z.   (1)

For completeness retain the exact Frobenius resultant of [C217v2](../claims/Yin_C_G0217_v2.md#bounded-length-gap).
For a prime p and the integral companion matrix A of P, P(A^p)=0 modulo p, since commuting powers give P(A^p)=P(A)^p modulo p.
Therefore det P(A^p) is divisible by p^d.
It is nonzero: a zero would give alpha_i^p=alpha_j for two roots; an automorphism of the finite normal closure sending alpha_i to alpha_j, iterated through its finite order, would make alpha_i a root of unity.
That contradicts irreducibility and noncyclotomicity.
Applying (1) to all alpha_i^p consequently yields

    p^d<=|det P(A^p)|<=H_inf^d exp(p d m),
    m>=log(p/H_inf)/p.                                           (2)

This uses all d conjugates, with their multiplicities after powering.
No minimal polynomial of a powered root is substituted for that product.

To apply Bertrand's theorem to the real number H_inf without an unjustified real-interval version, put n=floor(2H_inf)>=2.
There is a prime n<p<2n.
Since p is an integer, p>=n+1>2H_inf and p<2n<=4H_inf.
On 2<=x<=4 the minimum of log(x)/x is log(2)/2: its derivative changes sign only at its maximum x=e, and the two endpoint values agree.
Formula (2) thus gives

    m>=log(2)/(2H_inf),
    W>=H_inf>=log(2)/(2m)>1/(3m).                                (3)

Here log(2)>2/3.
The coefficient-length version is already identified in L G0012 with its checked Mig78 Proposition 5 interface.
The H_inf version follows from the displayed maximum-principle substitution in that same retained proof.
Bertrand is the same standard prime existence input already used there, not newly proved here.
No new audit of an original source proof is claimed.

<a id="near-one-integer-defect-budget"></a>
## 2. Both budgets are valid for the same finite cube problem

Now P is an actual monic irreducible Salem minimal polynomial, with exterior root exp(m), 0<m<=1/32, degree d, and q=d-2>=2 central roots.
Let B>0 be rational.
Use exactly the finite problem E_R of [L G0130](Yin_L_G0130_v1.md#finite-rational-energy-coercivity): x is real on I_R=[-R,R+d], |x_j|<=1/2, its defects z_j=P(S)x_j are integers on [-R,R], and z_0!=0.
Suppose its energy is at most B.

Extend x by zero to all integers.
This is only an estimate for that finite vector; no recurrence, integrality or cube condition is imposed on defects outside [-R,R].
Parseval's identity for the bilateral shift gives

    sum_(-R<=j<=R) |z_j|
      <=sum_(-R<=j<=R) z_j^2
      <=sum_(j in Z) |P(S)x_j|^2
      <=H_inf^2 sum_(j in I_R) x_j^2 <=H_inf^2 B.                (4)

Indeed the Fourier multiplier is P(e^(it)) or P(e^(-it)), depending on the Fourier convention, and either has supremum H_inf.
Thus either choice C=W or C=H_inf supplies the valid integer budget

    K=floor(C^2 B),             Z=floor(W/2),
    ||Z_c||_1<=A_*(ell)=min(K,Z(ell+1))                          (5)

for every actual cluster polynomial of span ell.
The entry bound Z still uses the cube and W; replacing the total budget does not silently replace that separate bound.
Since P is a unit polynomial, W>=2, so Z>=1.
The tighter H_inf budget is an exact mathematical alternative; no evaluation of H_inf or K is performed here.

Keep the exact Salem target of [L G0132](Yin_L_G0132_v1.md#tunable-salem-finite-energy-envelope):

    T_m=m exp(-2m)/(32d^2),
    B_m=2log(1/(16m))/pi^2+T_m,             B>=B_m.

Then B>=B_m>2log(2)/pi^2>2/15, using pi^2<10.
Also 36m^2<=9/256<2/15<B.
Formula (3), for either choice of C, proves

    K-1>C^2 B-2>B/(9m^2)-2>B/(18m^2).                          (6)

In particular K>=2.
This is a lower bound on the worst-case integer budget used by the recipe.
It does not assert that an actual feasible vector has K defects, or that its squared-defect sum attains K.

<a id="retained-norm-collar-cost"></a>
## 3. The norm term persists after an arbitrarily improved endpoint

Use precisely the flux constant Phi of [L G0141](Yin_L_G0141_v1.md#exact-central-boundary-flux).
For each central beta let q_beta be the coefficient row of P(t)/(t-beta), and let B_c have all those q rows.
Then

    Phi=min{(product_beta ||q_beta||_2^2)^(1/q),
             ||B_c||_op^2/q} >=1.                              (7)

The first quantity is at least one because every q_beta is monic of degree d-1.
The last column of B_c consists of q ones, so its operator norm squared is at least q; this proves the second lower bound.

Set lambda=2m/q and retain the norm component

    X(ell)=2B Phi A_*(ell)^(4/q) exp(lambda ell),
    L_norm(ell)=d[1+ceil X(ell)].                             (8)

Consider any positive integer-valued nondecreasing local collar function L that has a complete every-cluster exclusion proof and satisfies L(ell)>=L_norm(ell) for every integer ell>=0.
These hypotheses include the safe minimum in [L G0144](Yin_L_G0144_v1.md#full-collar-flux-interface) and its replacement of the endpoint by [L G0147's phase bound](Yin_L_G0147_v1.md#uniform-phase-observability-loss).
More explicitly they include

    L_flux=d[1+ceil(X+4B Psi^2)],
    min{L_flux, max(L_norm,L_end)},

whenever L_end is a proved sufficient endpoint length with the required finite guards.
Even an exact endpoint oracle does not remove (8) if it is combined this way.
A finite minimum among such proved monotone choices also retains (8).
Merely having a successful isolated same-window endpoint test does not supply the assumed monotone local theorem for all larger lengths.

The fixed local proofs use K only as an upper bound for the integer defect l1 mass.
Thus their proofs and finite indices remain valid after the substitution (4)--(5).
No new norm or endpoint argument is inferred from changing that budget.
This is not a global textual replacement of W^2B: the old coefficient-only bound using C_1<=dW retains that norm factor, as do Phi and the separate entry bound Z.
The delta_0 control and its B>=1/2 threshold in L G0143 are not used here.
Because A_*(ell)>=1, equations (7)--(8) give

    L(ell)>c exp(lambda ell),
    lambda L(ell)>a exp(lambda ell),
    c=2dB Phi,        a=lambda c=4mdB Phi/q>4mB Phi.             (9)

This conclusion contains neither D_C nor the old endpoint term 32q/m.
It does not assume a>=1 and does not impose or assert a tower growth bound on every nested level.

<a id="near-one-balanced-recipe-cost"></a>
## 4. A common lower cost for the old and balanced sufficient radii

For this same K,L define both previously proved sufficient recipes:

    s_0=0,       s_(j+1)=s_j+L(s_j),       0<=j<K,
    F(1)=0,     F(n)=(n-1)L(F(floor(n/2))),       n>=2,
    R_orig=s_K, R_bal=K L(F(K)), R_use=min(R_orig,R_bal).        (10)

The original cluster closure and [L G0143](Yin_L_G0143_v1.md#every-cluster-energy-coercivity) give E_R>B for every integer R>=R_use.
Their full every-cluster cube/integer-response premise remains essential.

Since every increment L(s_j)>c, one has lambda s_(K-1)>a(K-1).
Likewise lambda F(K)>a(K-1) directly from its defining formula and (9).
Both final evaluations of L in (10) therefore give

    R_orig>c exp(a(K-1)),
    R_bal>c exp(a(K-1)),
    R_use>2dB Phi exp(a(K-1))
          >2dB Phi exp(2B^2 Phi/(9m))=:R_0.                   (11)

The final inequality uses (6) and a>4mB Phi.
All strict inequalities hold also when B=B_m, if that choice is otherwise allowed; rational B is the choice used for finite-energy decisions.
Formula (11) applies separately to each budget C=W and C=H_inf.
Thus using the actual bilateral convolution norm instead of W does not evade this cost.

The balanced nesting count remains 1+floor(log_2 K).
The present lower bound keeps the integer multipliers and the final exponential; it neither identifies that nesting count with a practical cost nor claims one recipe is pointwise smaller than the other.

Put Lambda=log(1/(16m))>0.
Since B>=B_m>2Lambda/pi^2 and Phi>=1,

    2B^2 Phi/(9m)>8Lambda^2/(9pi^4 m)
                       >2Lambda^2/(225m).                     (12)

Along any hypothetical sequence of actual Salem inputs with m tending to zero, this displayed recipe cost consequently grows faster than every fixed power of 1/m, even before any extra endpoint cost is added.
No existence of such a sequence is assumed.
In particular the bounded W=6 and fixed-B budget used by the actual plastic family in L G0147 cannot be transferred to this domain as uniform constants.
This does not rule out a different norm argument, a more informative defect description, or a proof that avoids exhausting the budget K.

<a id="same-input-cutoff-and-sufficient-threshold"></a>
## 5. Exact comparison with the same-input transition window

Retain every parameter of L G0132.
For the same P define

    U(M)=q log M/(8m)+b_P,
    b_P=25/32+[log(16d C_P)+(q/2)log(16q)]/(2m)
                    +3exp(-2m)/[64(1-exp(-2m))],
    M_0=2R_0+d+1.                                            (13)

Here C_P is exactly the coefficient-box constant of [L G0123](Yin_L_G0123_v1.md#polynomial-height-central-approximation).
L G0132 proves E_R<=U(M_R), M_R=2R+d+1.
The positive function U(M)/M is strictly decreasing for M>=3.
Therefore for any fixed integer N>=1 satisfying

    N<=m M_0/[64 U(M_0)],                                    (14)

every integer R>=R_use satisfies E_R<=U(M_R)<=mM_R/(64N).
The actual L G0132 upper-envelope value is then exactly one, even using the exact E_R, throughout that guaranteed radius range.
This is an explicit same-P,N comparison with the [finite candidate cutoff](Yin_L_G0132_v1.md#finite-energy-candidate-window-cutoff).
The right side of (14) retains b_P and C_P; no uniform estimate for them or nonemptiness of its integer N range is asserted.
This conclusion does not exclude successful earlier energy windows R<R_use.

Alternatively choose B>B_m and use E_(R_use)>B as the sufficient energy certificate.
Let g_B=sqrt(B)-sqrt(B_m)>0 and define the real threshold

    N_suff=m(2R_use+d+1)/(64g_B^2)
       > md Phi/16 exp(2B^2 Phi/(9m))
       > md/16 exp(2Lambda^2/(225m)).                         (15)

Indeed 2R_use+d+1>2R_use, (11) applies, and g_B^2<B.
Every integer N>=max(1,N_suff), with the same central-smallness and actual enlarged transition window required by L G0132, forces C_delta<16m.
Equality N=N_suff is sufficient here because the energy certificate is strict: E_(R_use)>B.
The real expression N_suff is the output threshold of this chosen sufficient test, not a necessary lower bound on actual N or on the first possible transition exclusion.
The other L G0129 guards still have to hold whenever one uses its full Fourier contradiction scheme.

<a id="generic-discriminant-substitution-gate"></a>
## 6. Separate endpoint/discriminant substitution gate

The following argument, contributed by entropy_status, has the wider Salem domain 0<m<=1.
Write s=exp(m)+exp(-m)=2cosh(m).
Since P(1) and P(-1) are nonzero integers, the root products give

    |P(1)|=(s-2) product_central |1-beta|>=1,
    |P(-1)|=(s+2) product_central |1+beta|>=1.                  (16)

The central roots are nonreal and occur in conjugate pairs.
For either real point, choose a closest central root; its distinct conjugate has the same distance.
Bounding the other factors by two yields

    min_beta |1-beta|^2>=2^(2-q)/(s-2),
    min_beta |1+beta|^2>=2^(2-q)/(s+2),
    1<=|P(1)P(-1)|=4sinh(m)^2 product_central |1-beta^2|
                                      <=4sinh(m)^2 2^q.      (17)

These retain exponential degree costs and concern two fixed real points, not the separation of arbitrary central pairs.
No c/d angular separation estimate is deduced from them.

Use exactly the valid separation envelope of [L G0144](Yin_L_G0144_v1.md#degree-measure-separation-bound):

    D_C=2 max_i sum_(j!=i) 1/|beta_i-beta_j| <=D_hat,
    s_d=sum_(k=0)^(d-1) k^2,
    D_hat=4(q-1)m exp((d-1)m) s_d d^((d-2)/2),
    lambda=2m/q.                                            (18)

This bound comes from the two-column Vandermonde difference argument and the actual nonzero integer discriminant.
It is not an assertion that D_C attains the envelope.
The power series of cosh gives s-2<=2m^2(cosh(1)-1)<2m^2 for 0<m<=1, since cosh(1)<2.
Hence (16) imposes the actual arithmetic restriction

    1<=|P(1)|<=2^q(s-2)<2^(q+1)m^2,
    m^2>2^(-(d-1)).                                         (19)

As (q-1)/q>=1/2, exp((d-1)m)>1 and d>=4, it follows that

    lambda D_hat>4m^2 s_d d^((d-2)/2)
                 >4*2^(-(d-1))*s_d*2^(d-2)
                  =2s_d>=28.                               (20)

Here d^((d-2)/2)>=2^(d-2), and s_4=14.
Thus substituting this generic envelope into the phase endpoint of L G0147 gives

    L_phase_hat=1+ceil[92D_hat+32qB+16B],
    lambda L_phase_hat>2576.                                (21)

For K>=1, the proposed scaled-endpoint gate lambda K L<1 therefore cannot be certified by this substitution on any actual input in that domain.
This is a lower cost of the chosen sufficient envelope, not a lower bound for D_C, the exact projected Gramian, the least successful endpoint, the true energy radius, or an allowed orbit length.
It does not imply that the actual same-window test fails.
In particular it must not be used in place of the separate norm-budget proof (1)--(15).

## Contributions, retained interfaces and bounded decision

The coordinator identified and supplied the decisive L G0012 reuse, the resulting inverse-m coefficient budget, the final-exponential comparison for both radii, and the extension to H_inf including the integer Bertrand choice.
The execution_and_deliverables AI checked all steps, developed the finite zero-extension and recipe scopes, assembled the complete proof and the same-input cutoff and threshold comparisons.
Both are contributors to Sections 1--5.
The Phi>=1 observation was also supplied by the coordinator and had already been used in L G0146.
The entropy_status AI derived the separate endpoint products and D_hat gate now assembled as Section 6; that AI is a contributor to this combined proof, not its independent reviewer.
It also checked the K_inf substitution against the fixed L G0135/L G0141/L G0143 local and closure interfaces, with the norm-factor and unused delta_0 boundaries just stated; that was a contributor check.

The coordinator first checked existing Smy08 sparsity reports and made a bounded public search that rediscovered the already retained Smy08/DS17 material, then located the decisive fixed L G0012 mechanism.
Only that fixed prime-norm proof and the direct deductions displayed here are used for the new budget argument.
No bounded-support theorem is an additional premise; no source was downloaded, newly registered or newly source-audited for this proof.

The L G0132, L G0141, L G0143, L G0144 and L G0147 interfaces are reused as fixed mathematical inputs with their original hypotheses.
The execution_and_deliverables AI coauthored L G0143; use of that interface is not a new independent review of its old proof.
The coordinator read the complete assembled proof (1)--(21) and found no mathematical defect; because of the contributions recorded above, that was a contributor check rather than independent review.

On 2026-10-08--09, the separately assigned growth_arithmetic_status AI for Yin independently read and checked all of Sections 1--6, equations (1)--(21), and the stated scope boundaries.
It supplied no mathematical derivation, edits or numerical computation.
It had received the research question and branch context, so this was not blind review.
It directly checked the used scopes of the fixed interfaces; those old proofs were reused rather than claimed as newly independently audited in full.

Coverage included the inner/outer maximum-principle estimate, nonzero Frobenius resultant and conjugate multiplicities, real H_inf and the integer Bertrand interval, both defect budgets and all finite zero-extension indices, the separate Z/Phi/C_1 boundaries, the target B_m and floor losses, Phi>=1, and the complete monotone local collar premises after an endpoint replacement.
It checked both recursions, their common strict lower bound and minimum, the distinction between budget K and actual defects, the logarithmic target comparison, the full C_P-dependent same-input cutoff, and the sufficient rather than necessary N_suff threshold including its equality case.
It also checked both real-point integer products, the conjugate-pair estimate, the actual m,d restriction, every D_hat constant, and the limited scope of that literal sufficient-envelope substitution.

The reviewer identified one wording ambiguity: the closest pair in Section 6 must mean a root closest to the fixed real point and its conjugate, not two central roots closest to each other.
The final text states that selection explicitly.
The reviewer reread and closed this correction, with no substantive defect or missing hypothesis remaining.
Subsequent changes only added this completed-review and acceptance record; the proof (1)--(21) was unchanged.

This is complete independent AI written-proof review, not a numerical experiment, formal verification, blind review or new external-source proof audit.
The coordinator accepted the result for fixed-ledger preservation on 2026-10-09.
The unrestricted G0001 Task remains unresolved.

This closes the proposed endpoint-only repair of the retained recipe: even removing its explicit inverse-m endpoint cost and replacing W by the true bilateral operator norm leaves (11)--(15).
A meaningful restart needs a proved change to the norm/defect-budget mechanism, an early actual energy certificate, or other actual input structure that avoids this particular exhaustive cost.
Merely refining D_C or the endpoint constants while keeping (8)--(10) does not remove it.
No general lower bound on actual energy growth, transition-product lower bound, near-one family construction, or unrestricted Mahler gap has been established by this cost calculation.
