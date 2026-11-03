---
author: Yin
---

# Complete expanding correlation, square-density exponent and conditional stationary information

The complete original L224 Sections 1--6/(1)--(18) are retained with every actual-field coordinate, full original word probability, anisotropic factor and conditional density/critical-return boundary.
The original [R793 whole](../audits/reviews/Yin_R_G0793_v1.md#expanding-correlation-complete-independent-review) retains its 2026-10-09T21:35 full-chain inspection.
The separate 21:39 Keh25 attribution supplement is a narrower source-addition recheck, not a backdated second whole inspection; its necessary complete account is retained separately in responsible R.
An available assignment/short overview/common context does not establish the actual additional mathematical content or initial order, and no later C binding is attributed to either old occurrence.

## Statement

<a id="expanding-correlation-fixed-scope"></a>
Let alpha be any nonzero algebraic integer with actual monic irreducible P of degree d and m=log M(P)>0.
Let U be its complete expanding real Minkowski space, with real dimension r>=1 counting each complex pair twice; let q be the analogous real dimension of the unit-circle coordinates.
Use real scalar/complex scale-rotation coordinates, A multiplication by alpha on U, v the image of 1 and kappa=||A^(-1)||<1.
The projection is injective on the number field and |det A|=exp(m).
For every n>=1, finite sums indexed j<n below mean j=0,...,n-1.
For independent iid fair bits xi_j,xi'_j put W_n=sum_(j<n)xi_j alpha^j,p_n=Pr{W_n=W'_n},p_0=1 and X_n=projection_U(W_n-W'_n).
Let nu be the law of Z=sum_(j>=1)xi_j A^(-j)v and mu=nu*reflected(nu) the law of Y=Z-Z'.
Define the actual finite constants
\[
K=||v||\kappa/(1-\kappa),\quad
C_{\rm st,2}=\prod_{|\gamma|<1}2/(1-|\gamma|),\quad
D=(2^q C_{\rm st,2})^{1/r},
\]
where the product uses all contracting embeddings with complex multiplicity and is 1 if empty.
Both ||Z|| and ||Y|| are at most K.
For R>0,c in U define
\[
Q_n(c,R)=\Pr\{A^nY\in\overline B(c,R)\},\quad
a_R=\Pr\{||Y||\le R\},\quad
N(R)=[1+2(R+K)D]^r .
\]
If L_R is the least nonnegative integer with kappa^(L_R)K<=R, a_R>=2^(-L_R)>0.
For all n>=1,
\[
a_Rp_n\le Q_n(0,R),\quad
Q_n(c,R)\le N(R)n^q p_n,\quad
\sup_c\Pr\{X_n\in\overline B(c,R)\}
\le[1+2RD]^r n^q p_n .
\]
The lower bound is only at zero center.
Distinct atoms of X_n have separation at least D^(-1)n^(-q/r), with every original embedding and difference coefficient included.
The fixed-input collision rate exists,
h_2=-lim log(p_n)/n=inf_(n>=1)(-log(p_n)/n) in [0,log2], and for each fixed R>0,
-lim log Q_n(0,R)/n=h_2.
No varying-input or radius exchange is asserted.

Let B be the closed unit ball of volume V_r, E_n=A^(-n)B, rho_n=1_(E_n)/Vol(E_n), f_n=nu*rho_n and Ecal_n=||f_n||_2^2.
Then f_n is a genuine square-integrable probability density even for singular nu and
\[
\mathcal E_n=\frac{e^{nm}}{V_r^2}
 E[\operatorname{Vol}(B\cap(B+A^nY))],
\]
\[
\frac{2^{-r}a_1}{V_r}e^{nm}p_n
\le\mathcal E_n\le\frac{N(2)}{V_r}n^q e^{nm}p_n,\quad
\lim_n\log\mathcal E_n/n=m-h_2,\quad h_2\le m .
\]
Uniform boundedness of all Ecal_n is equivalent to nu having an L2(U) probability density f.
This uses precisely the accepted Keh25 bounded-Hilbert-functional representation interface in the converse.
The L2 condition implies h_2=m; rate equality alone is not claimed to imply bounded energies or an L2 density.

For the stationary application restrict alpha to an algebraic unit and Q to an admissible irreducible positive recurrent law on a subset of the actual original return core containing zero, using chronological x->alpha x+eta with original probabilities (1/4,1/2,1/4), stationary pi and original-row information I.
Every core state has expanding norm at most K.
The full original-path comparison started from the same pi has relative entropy nI and gives, for all n>=1,
\[
nI\ge-\log p_n-q\log n-r\log(1+2KD).
\]
No state entropy, moment, killed-process renormalization or critical minimizer is assumed.
If the additional L2 density exists, then
\[
I\ge m-\frac{\log(||f||_2^2 V_r(2K)^r)}n
\quad(n\ge1),\qquad I\ge m,\quad\inf_Q I=m.
\]
All constants and chronological time remain actual-input costs.

For a Salem beta>1 of actual degree d, r=1,q=d-2,m=log beta, its scalar correlation integral C(epsilon)=Pr{|Z-Z'|<=epsilon} has the full limit
\[
\lim_{\epsilon\downarrow0}\log C(\epsilon)/\log\epsilon
=h_2(\beta)/\log\beta .
\]
Under the additional jointly expanding L2 condition, for every fixed R>0,
Q_n(0,R)~||f||_2^2 V_r R^r e^(-nm), and at each fixed input there are positive constants c,C with
c n^(-q)<=e^(nm)p_n<=C.
For the complete original renewal series U(z)=sum_(n>=0)p_n z^n and F(z), its critical radius in that conditional case is Rcrit=e^m.
If q=0, U(tRcrit)>=c/(1-t), hence F(Rcrit)=1 and Rcrit F'(Rcrit)<infinity.
For units this is the exact rooted finite-mean critical-attainment criterion.
For nontorsion irreducible inputs, any neutral roots are nonreal pairs, so q=0 or q>=2; the q>=2 packing comparison does not classify Green divergence or critical mean, including for Salem inputs.

The actual nonunit alpha=2 calibrates the probability theorem only:
nu is uniform on [0,1], p_n=2^(-n),h_2=m=log2,C(epsilon)=2epsilon-epsilon^2 for 0<=epsilon<=1,U(z)=1/(1-z/2),F(z)=z/2,critical mean 1 and core {0}.
It does not extend the unit-only variational theorem.
No Bernoulli/Salem L2 regularity premise, weighted local limit, varying-input constant bound, critical Salem classification, uniform entropy floor or unrestricted gap is proved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:10 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All nonzero algebraic integers with positive total measure for the full joint expanding weighted probability comparison, exact anisotropic square-density rate and bounded-energy/L2 equivalence; unit-only actual rooted stationary application; scalar Salem correlation dimension and conditional q0 critical-return result versus unresolved q>=2; exact nonunit alpha2 calibration and every finite constant/limit restriction. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(18), complete field-norm packing with all difference coefficients/complex multiplicities, original iid reversal/tail/maximum-atom proof, every Jacobian and smoothing constant, precise Riesz interface, full original stationary likelihood, scalar radius interpolation and positive-coefficient Abel derivative proof, alpha2 calibration, source/contribution and unresolved boundaries. |
| support | [Expanding support/norm-separation antecedent](Yin_C_G0274_v1.md#statement) | Only actual expanding real/complex coordinates and integer-norm separation method; no support-volume result is substituted for the weighted probability proof. |
| dependency | [Exact unit rooted stationary/renewal interface](Yin_C_G0479_v1.md#statement) | Actual unit-only rooted positive recurrent class, full original likelihood, infimum h2, complete original renewal and exact finite-mean attainment criterion; no nonunit variational extension. |
| support | [Full original-path convention](Yin_C_G0531_v1.md#stationary-neutral-concentration-cost) | Only the full original process from the same pi and finite path nI likelihood convention; no neutral small-ball theorem is a premise. |
| dependency | [Standard bounded Hilbert functional](../audits/literature/Keh25/Yin_U001.md#keh25-u001) | Precisely Theorem5.17 p53 bounded L2 integration functional representation/norm; selected original proof reading only, no Bernoulli density or bounded-energy premise. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All nonzero algebraic integers with positive total measure for the full joint expanding weighted probability comparison, exact anisotropic square-density rate and bounded-energy/L2 equivalence; unit-only actual rooted stationary application; scalar Salem correlation dimension and conditional q0 critical-return result versus unresolved q>=2; exact nonunit alpha2 calibration and every finite constant/limit restriction. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(18), complete field-norm packing with all difference coefficients/complex multiplicities, original iid reversal/tail/maximum-atom proof, every Jacobian and smoothing constant, precise Riesz interface, full original stationary likelihood, scalar radius interpolation and positive-coefficient Abel derivative proof, alpha2 calibration, source/contribution and unresolved boundaries. |
| support | [Expanding support/norm-separation antecedent](Yin_C_G0274_v1.md#statement) | Only actual expanding real/complex coordinates and integer-norm separation method; no support-volume result is substituted for the weighted probability proof. |
| dependency | [Exact unit rooted stationary/renewal interface](Yin_C_G0479_v1.md#statement) | Actual unit-only rooted positive recurrent class, full original likelihood, infimum h2, complete original renewal and exact finite-mean attainment criterion; no nonunit variational extension. |
| support | [Full original-path convention](Yin_C_G0531_v1.md#stationary-neutral-concentration-cost) | Only the full original process from the same pi and finite path nI likelihood convention; no neutral small-ball theorem is a premise. |
| dependency | [Standard bounded Hilbert functional](../audits/literature/Keh25/Yin_U001.md#keh25-u001) | Precisely Theorem5.17 p53 bounded L2 integration functional representation/norm; selected original proof reading only, no Bernoulli density or bounded-energy premise. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g224-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R793. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | All nonzero algebraic integers with positive total measure for the full joint expanding weighted probability comparison, exact anisotropic square-density rate and bounded-energy/L2 equivalence; unit-only actual rooted stationary application; scalar Salem correlation dimension and conditional q0 critical-return result versus unresolved q>=2; exact nonunit alpha2 calibration and every finite constant/limit restriction. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/equations(1)--(18), complete field-norm packing with all difference coefficients/complex multiplicities, original iid reversal/tail/maximum-atom proof, every Jacobian and smoothing constant, precise Riesz interface, full original stationary likelihood, scalar radius interpolation and positive-coefficient Abel derivative proof, alpha2 calibration, source/contribution and unresolved boundaries. |
| support | [Expanding support/norm-separation antecedent](Yin_C_G0274_v1.md#statement) | Only actual expanding real/complex coordinates and integer-norm separation method; no support-volume result is substituted for the weighted probability proof. |
| dependency | [Exact unit rooted stationary/renewal interface](Yin_C_G0479_v1.md#statement) | Actual unit-only rooted positive recurrent class, full original likelihood, infimum h2, complete original renewal and exact finite-mean attainment criterion; no nonunit variational extension. |
| support | [Full original-path convention](Yin_C_G0531_v1.md#stationary-neutral-concentration-cost) | Only the full original process from the same pi and finite path nI likelihood convention; no neutral small-ball theorem is a premise. |
| dependency | [Standard bounded Hilbert functional](../audits/literature/Keh25/Yin_U001.md#keh25-u001) | Precisely Theorem5.17 p53 bounded L2 integration functional representation/norm; selected original proof reading only, no Bernoulli density or bounded-energy premise. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0793_v1.md#expanding-correlation-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:39, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

### Reuse and scope of this exploration

[L83](Yin_C_G0274_v1.md#expanding-neighborhood-volume-rate) gives a support-count/expanding-neighborhood volume comparison, using integer-norm separation and its polynomial neutral loss.
The present argument retains word probabilities and uses the difference law, whose maximum atom is its zero atom.
This produces a two-sided probability comparison, not a support-volume or separate-coordinate inference.
[L201](Yin_C_G0479_v1.md#actual-stationary-information-variational-interface) supplies the actual stationary class and its already proved information infimum; [L220](Yin_C_G0531_v1.md#small-ball-quantile-fixed-scope) supplies the recent neutral geometry and full-original-path likelihood convention.
Neither establishes square-integrability of the expanding Bernoulli measure.

A bounded search of the local G ledgers for Bernoulli convolution, correlation dimension, local limits, square-density and stationary diffusion found L83's support result and the earlier explicitly limited uses, not the exact weighted comparison below.
This is a local reuse check, not a literature-wide novelty assertion.
Correlation integrals, smoothing by normalized balls and their elementary square-norm identities are classical constructions; all deductions needed here are proved directly apart from the standard Hilbert-space Riesz representation foundation identified in Section3.
That foundation is recorded in [Keh25-U001](../audits/literature/Keh25/Yin_U001.md#keh25-u001) at its exact statement, applicability and selected-proof inspection scope.
No specialized external Bernoulli regularity theorem, numerical calculation or J program is a premise.

The main probability comparison actually holds for every nonzero algebraic integer alpha with positive logarithmic Mahler measure.
The stationary application is restricted to algebraic units, at the established L201 interface.
The nonunit alpha=2 is used only as an exact calibration, not as a near-one example or as an extension of an uninspected variational theorem.

<a id="expanding-correlation-setup"></a>
### 1. Actual fields, original probabilities and all geometric constants

Let alpha be a nonzero algebraic integer with irreducible monic minimal polynomial P of degree d and m=log M(P)>0.
Split the archimedean embeddings into expanding, unit-circle and contracting coordinates.
Let r>=1 be the real dimension of the expanding space U: count real embeddings once and each nonreal conjugate pair twice.
Let q be the analogous real dimension of the unit-circle space.
Use Euclidean coordinates in U consisting of each real embedding and the real and imaginary parts of one embedding from each complex pair.
Write A for multiplication by alpha on U and v for the expanding image of 1.
These coordinates give

    |det A|=exp(m),       kappa=||A^(-1)||<1.

The expanding projection is injective on the number field, because any one field embedding is injective.
Thus equal expanded endpoints are exactly equal algebraic endpoints.
Complex pairs contribute their squared absolute value in the field norm, as required by their two real dimensions.

Let xi_j and xi'_j be independent fair bits.
Define the original binary endpoint W_n=sum_(j=0)^(n-1) xi_j alpha^j, its independent copy W'_n, and

    p_n=Pr{W_n=W'_n},       p_0=1,
    X_n=projection_U(W_n-W'_n).

The difference digits eta_j=xi_j-xi'_j have precisely the original law p(0)=1/2, p(1)=p(-1)=1/4.
Let nu be the probability law on U of the convergent random series

    Z=sum_(j>=1) xi_j A^(-j)v,

and let mu=nu*reflected(nu) be the law of Y=Z-Z'.
Put

    K=||v|| kappa/(1-kappa)>0,
    C_st,2=product_(|gamma|<1) 2/(1-|gamma|),
    D=(2^q C_st,2)^(1/r).                              (1)

The contracting product runs over all embeddings with conjugate multiplicities, and is 1 if empty.
Both Z and Y have norm at most K.
For Y this follows directly from its digits in {-1,0,1}, without replacing K by the looser 2K estimate.
All constants depend on the actual input; no uniform bound as m tends to zero is being assumed.

For R>0 let B(c,R) be the closed Euclidean ball.
Define the actual expanding correlation profile

    Q_n(c,R)=Pr{A^n Y in B(c,R)},
    a_R=Pr{Y in B(0,R)},
    N(R)=[1+2(R+K)D]^r.                               (2)

If L_R is the least nonnegative integer such that kappa^(L_R) K<=R, then

    a_R>=2^(-L_R)>0.                                  (3)

Indeed the first L_R difference digits can all be zero, with probability 2^(-L_R); the remaining tail is A^(-L_R) times another Y and lies in the stated ball.
This includes L_R=0.
It exposes the small-expansion cost rather than hiding it in a positivity assertion.

<a id="weighted-norm-packing-comparison"></a>
### 2. Complete correlation mass versus exact return probability

For every n>=1, R>0 and c in U,

    a_R p_n <= Q_n(0,R),
    Q_n(c,R) <= N(R) n^q p_n.                         (4)

Thus the upper estimate is uniform in the center, while the lower estimate is asserted at the actual zero center only.

To prove the lower bound, split the infinite digit series after n digits.
Reversal of the first n independent identically distributed digits shows

    A^n Y = X_n + Y_tail   in distribution,             (5)

where Y_tail has law mu and is independent of X_n.
The zero atom of X_n contributes exactly p_n a_R to Q_n(0,R).

For the upper bound first check every multiplicity and separation cost.
Any two distinct atoms of X_n differ by the expanding image of T(alpha), where T is an integer polynomial of degree at most n-1 with all coefficients in {-2,-1,0,1,2}.
This is a nonzero algebraic integer, so its absolute field norm is at least 1.
At a contracting embedding gamma its absolute value is at most 2/(1-|gamma|), and at every unit-circle embedding it is at most 2n.
Hence its product of expanding absolute values is at least

    C_st,2^(-1) (2n)^(-q).

Each expanding absolute value is at most the Euclidean norm of its vector, with a complex pair counted twice.
Consequently distinct atoms are separated by at least

    delta_n=D^(-1)n^(-q/r).                            (6)

A ball of radius T contains at most (1+2T/delta_n)^r such atoms: put disjoint open balls of radius delta_n/2 around them and compare volumes in the enclosing ball.
Tangencies have zero volume, so the weak separation is sufficient.
For n>=1 this is at most [1+2TD]^r n^q.

If X_n+Y_tail lies in B(c,R), then X_n lies in B(c,R+K).
Finally every atom of X_n has probability at most p_n.
To see this, let b_n(x)=Pr{W_n=x} on the finite original algebraic support, extend it by zero, and use Cauchy--Schwarz:

    Pr{W_n-W'_n=z}
       =sum_x b_n(x)b_n(x-z)
       <=(sum_x b_n(x)^2)^(1/2)
          (sum_x b_n(x-z)^2)^(1/2)
       =p_n.                                          (7)

Projection introduces no merged atoms.
Summing (7) over the separated atoms in B(c,R+K) proves (4).
This proof retains the complete word law, not just a selected collection of first-return words or prime factors.
The neutral power n^q is the only time-dependent packing loss; its fixed-input constants are displayed in (1)--(3).

The same argument, before adding Y_tail, gives the useful finite estimate

    sup_c Pr{X_n in B(c,R)}
        <=[1+2RD]^r n^q p_n.                           (8)

The return probabilities are supermultiplicative, since concatenating two zero-difference blocks gives a zero block.
They also satisfy p_n>=2^(-n).
Therefore the elementary superadditive limit yields

    h_2=-lim_(n->infinity) log(p_n)/n
       =inf_(n>=1) [-log(p_n)/n] in[0,log2].             (9)

Combining (4) with (9), for each fixed input and each fixed R>0,

    -lim_n log Q_n(0,R)/n = h_2.                       (10)

There is no exchange with a varying degree, expanding eigenvalue or radius here.
The finite error includes q log n, log N(R), and L_R log2 explicitly.

<a id="expanding-square-density-pressure"></a>
### 3. Exact square-density growth on the jointly expanding space

Let V_r be the volume of the unit ball B in U.
Let E_n=A^(-n)B, and let

    rho_n(x)=1_(E_n)(x)/Vol(E_n),
    f_n=nu*rho_n,       Ecal_n=||f_n||_2^2.

Each f_n is a genuine square-integrable probability density even if nu is singular: it is bounded by 1/Vol(E_n) and has compact support.
Direct integration of the two translated indicator functions gives

    Ecal_n
      =exp(nm)/V_r^2
         E[Vol(B intersect (B+A^n(Z-Z')))].             (11)

The intersection volume is at most V_r and vanishes outside distance 2.
If the center displacement has norm at most 1, the intersection contains the ball of radius 1/2 around the midpoint.
Thus (4) and (11) give the full finite comparison

    [2^(-r)a_1/V_r] exp(nm) p_n
      <= Ecal_n
      <= [N(2)/V_r] n^q exp(nm) p_n.                  (12)

In particular

    lim_n log(Ecal_n)/n = m-h_2.                      (13)

This is the joint anisotropic smoothing defined by the actual matrix A, not a sum of one-dimensional marginal dimensions.
No field factor or expanding direction has been removed.
Since f_n is supported in the fixed ball of radius K+1, Cauchy--Schwarz gives

    Ecal_n >= 1/[V_r(K+1)^r].

Consequently (13) itself implies h_2<=m.
It is consistent with the retained entropy bound but also proves the needed direction locally.

A useful precise regularity condition is that nu has a density f in L2(U).
Then Jensen followed by integration gives ||f*rho_n||_2<=||f||_2, hence

    nu has an L2 density  implies  h_2=m.               (14)

Conversely, boundedness of all Ecal_n is equivalent to that L2 condition.
For completeness, if Ecal_n<=C, then for every compactly supported continuous test function phi the approximate identity E_n shrinking to zero gives

    |integral phi dnu|
      =lim_n |integral phi f_n dx|
      <=sqrt(C)||phi||_2.

This bounded functional extends from those tests to L2, so the Hilbert-space representation of a bounded linear functional supplies f in L2 with nu=f dx and ||f||_2<=sqrt(C).
This is the standard Riesz representation theorem, checked in [Keh25, Theorem5.17, printed/PDF p.53](../literature/pdf/Keh25.pdf), with source scope recorded in Keh25-U001.
Equality of the measures follows on the same continuous tests.
This converse uses bounded energies, not merely their exponential rate.

In contrast, h_2=m in (13) is exactly zero exponential growth of Ecal_n.
The argument does not upgrade subexponential growth to boundedness or prove L2 regularity from rate equality.
No general or Salem-specific density hypothesis has been discharged in this round.

<a id="stationary-expanding-confinement-cost"></a>
### 4. Actual stationary confinement and its finite information price

Now restrict alpha to an algebraic unit and use the exact L201 admissible class: an irreducible positive recurrent Q on a subset of the actual original return core containing zero, with stationary probability pi, the original digit edges, and information rate I.
Every state in that core has expanding image in B(0,K).
Indeed a finite original word of length ell taking x to zero gives

    projection_U(x)=-sum_(j=1)^ell eta_j A^(-j)v,

with the order of its digits chosen from the actual chronological recurrence.
The bound K from (1) follows.
It holds for every state, regardless of how large its neutral coordinates may be.

Start both Q and the complete original iid-digit process from the same pi.
Their length-n relative entropy is nI by the finite path chain rule, exactly as established in L201/L220; no entropy or moment of pi is required.
Under Q the terminal expanding coordinate is in B(0,K) with probability one.
For the original process started at x its terminal coordinate is A^n projection_U(x)+X_n in distribution.
Applying (8) uniformly in the shifted center and then data processing to this terminal event gives

    nI >= -log Pr_original{terminal expanding point in B(0,K)}
       >= -log p_n -q log n -r log(1+2KD).             (15)

A negative right side is harmless; the probability cap by one may be inserted.
The original process is not killed or renormalized.
Its event probability is positive, since it dominates all Q paths under the common starting law.
Taking n to infinity recovers I>=h_2 with every finite packing cost present.

Under the additional L2 hypothesis of (14), there is a sharper direct finite bound without the n^q factor.
The difference law mu then has density

    g(y)=integral f(x)f(x-y) dx,
    0<=g(y)<=||f||_2^2.

Whenever X_n lies in B(c,K), adding its independent Y_tail keeps it in B(c,2K).
Using (5), the probability of the first event is at most that of the second, and therefore

    Pr{X_n in B(c,K)}
       <= ||f||_2^2 V_r(2K)^r exp(-nm).

The same full-path comparison gives

    I >= m - log[||f||_2^2 V_r(2K)^r]/n
    for every n>=1, hence I>=m.                       (16)

Together with L201's exact infimum and (14), the information infimum is m in this conditional case.
This is a real expanding-confinement mechanism on actual nontorsion inputs.
It does not require a bound on stationary neutral radii, nor does it claim one.

It still supplies no fixed positive lower bound independent of m.
Even a future proof of L2 regularity for every near-one Salem input would establish the proportional identity h_2=m; that identity alone would not exclude m tending to zero.
The size and varying-input cost of ||f||_2, K, D and the observation time cannot be suppressed in any stronger finite estimate.

<a id="salem-correlation-critical-boundary"></a>
### 5. Scalar Salem specialization and the critical-return test

For a Salem beta>1 of actual degree d, U is one-dimensional, A=beta, r=1, q=d-2 and m=log beta.
Let nu_beta be its fair binary series law.
Its correlation integral is

    C(epsilon)
      =Pr{|Z-Z'|<=epsilon}
      =integral nu_beta([x-epsilon,x+epsilon]) dnu_beta(x).

This is a probability of closeness of two independent points; the correlation dimension is the limit of log C(epsilon)/log epsilon when it exists.
Equations (4) and (10) give at epsilon=R beta^(-n), and then by monotonicity between consecutive such radii,

    lim_(epsilon down to0) log C(epsilon)/log epsilon
         =h_2(beta)/log beta.                          (17)

The limit exists for this exact algebraic input.
This is a normalized correlation dimension, not an unnormalized entropy floor.
A lower bound independent of beta for the number on the right would still give only a bound proportional to log beta.

There is also a concrete limit to what density regularity would decide about the complete return tail.
If the jointly expanding nu has an L2 density, translation continuity in L2 makes g continuous at zero, with g(0)=||f||_2^2>0.
Since A^(-n)B(0,R) shrinks to zero and has volume V_r R^r exp(-nm),

    Q_n(0,R) ~ ||f||_2^2 V_r R^r exp(-nm).

Using both sides of (4) yields constants c,C>0, depending on the fixed input and R, such that for every sufficiently large n,

    c n^(-q) <= exp(nm) p_n <= C.                     (18)

All finitely many smaller n are positive and can be included by adjusting constants.

Let U(z)=sum_(n>=0) p_n z^n and F(z) be the complete first-return series.
Original renewal gives U(z)=1/(1-F(z)) below the return radius.
Under the L2 hypothesis this radius is Rcrit=exp(m), by (14).

If q=0, the lower bound in (18) implies U(t Rcrit)>=c/(1-t) for 0<t<1 after reducing c if necessary.
Thus F(Rcrit)=1 and

    [1-F(t Rcrit)]/(1-t) <= 1/c.

Passing to the endpoint gives Rcrit F'(Rcrit)<=1/c<infinity.
For algebraic units this is exactly the finite-mean critical attainment criterion in L201.
The proof uses positive coefficients and Abel limits, not an imported renewal asymptotic.

For an actual nontorsion irreducible input, any unit-circle roots are nonreal and occur in conjugate pairs, so q is either zero or at least two.
In the latter case the lower comparison n^(-q) is summable and (18) does not decide whether U(Rcrit) is finite or infinite.
Nor does its upper bound decide the critical first-return mean.
In particular, even the extra unproved L2 hypothesis does not classify the Salem critical law by this packing argument.
A genuine weighted local limit or another sharper actual-state estimate would still be required.
No such estimate is asserted here.

### 6. Exact calibration and the remaining exploration

The nonunit alpha=2 makes the constants and normalizations checkable without a numerical experiment.
Its binary series Z=sum_(j>=1) xi_j 2^(-j) is uniform on [0,1]: its probabilities on dyadic half-open intervals equal their lengths, and these intervals determine the distribution.
Thus nu has the L2 density 1_[0,1], while the binary endpoints at length n are uniform on {0,...,2^n-1}.
Hence

    p_n=2^(-n),       h_2=log2=m,
    C(epsilon)=2epsilon-epsilon^2  for 0<=epsilon<=1.

The correlation profile therefore differs from p_n by bounded factors at the natural scale, as (4) requires.
The complete zero-difference word must have every digit zero, by uniqueness of finite binary expansions.
Thus F(z)=z/2 and U(z)=1/(1-z/2), with critical finite mean one.
The actual return core is {0}.
This is an exact nonunit calibration; it does not replace the unresolved near-one unit class or extend L201's adopted domain.

The changed nontorsion mechanism achieved here is a complete original-probability bridge between arithmetic return atoms and the jointly expanding random series.
It retains all expanding coordinates, displays the polynomial central loss, and converts a clearly stated density hypothesis into a full stationary confinement cost.
It also identifies two precise insufficiencies: correlation dimension is normalized by m in the Salem specialization, and square-integrability alone does not remove the neutral packing loss needed to classify critical returns.

The next substantive test is whether actual expanding/neutral correlations improve that polynomial comparison in a useful original weighted regime, or whether one can bound the square-density profile through nontorsion arithmetic in a way stronger than a proportional entropy identity.
Candidate local-limit or conditional-regularity statements may be explored, but must preserve the actual field, complete word probabilities, varying degree and approach to m=0.
Neither a generic diffusion constraint nor an unproved density premise is adopted as a positive gap.

### Original author check and remaining scope

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g224-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.

No source-proof audit, square-integrability theorem for a Salem input, critical Salem classification or unrestricted Lehmer conclusion is asserted.


Author freeze: 2026-10-09T21:27.
Complete proof and self-check above.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0793_v1.md#expanding-correlation-complete-independent-review), with its original inspected scope and relationship.




The [complete original Keh25 attribution supplement](../audits/reviews/Yin_R_G0793_v1.md#original-g224-keh25-source-supplement) retains the actual 2026-10-09T21:39 two-addition/source-scope check, separately from R123's whole 21:35 inspection.
