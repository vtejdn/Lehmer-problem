---
author: Yin
---

# Actual degree costs for arbitrary rational Cayley weights

Human author Yin.
The coordinating agent proposed the strict source marginal and the two-integer-norm comparison; the arithmetic contributor checked their full assembly, and a separate contributor checked the norm-to-degree chain conditional on the marginal bound.
These contributor checks are not independent whole review evidence for this version.
The complete fixed statement and argument are adopted at the [selected whole assessment](#decision-whole-independent-review-2026-11-05), supported by the [independent R1088 v5 finding](../audits/reviews/Yin_R_G1088_v5.md#whole-arbitrary-weight-cayley-finding).
The adopted [C866 v4 coordinate-norm result](Yin_C_G0866_v4.md#decision-whole-independent-review-2026-11-05) is reused only at its exact general positive-weight interfaces; the older v1--v3 results and their own assessments remain unchanged as well.
For the convex subfamily, v4 retains its stronger coefficient 1/2 in the bound M_2(beta)>=(1/2)d^(1/4)m_0; the smaller coefficient k_0 here accompanies the extension to arbitrary weight scale and does not replace that stronger subfamily result.
No old review of v1--v4 certifies the new FW1--FW12 proof.
The extraction source is [D1's arbitrary-weight inquiry](../drafts/Yin_D_G0001.md#p2-arbitrary-rational-cayley-weights), which is provenance rather than a proof premise.

## Fixed arithmetic and source interfaces

Use exactly [C866 v4 Part A](Yin_C_G0866_v4.md#statement), at the selected assessment linked above, with the fixed CQ4--CQ9 argument in [its complete proof](Yin_C_G0866_v4.md#p2-convex-cayley-unit-norms).
For a genuine Salem input alpha of degree d=2t, positive rational weights on r distinct oriented inverse pairs, and r<t or an actual full flip kernel, the Cayley output is defined and nonzero; integrality makes it a nontorsion unit and excludes beta=1,-1.
The actual output degree D is at least 2^r.
The exact stabilizer H=Gal(L/Q(beta)) has coefficient-preserving orbits O of sizes q_O and count kappa, with positive integer coordinate-norm exponents n_O.
Writing alpha=alpha_0^A for the smallest Salem field generator and m_0=log alpha_0, the used conclusions are

    m(beta)=N m_0, N=sum_O n_O>=kappa,
    M_2(beta)^2>=2d m_0^2 sum_O n_O^2/q_O.               (IN1)

These are v4's arbitrary-positive-weight conclusions; its convex normalization, later Markov estimate and 1/2 constant are not assumed for this larger weight domain.
The exact degree of alpha_0 is d, its source power is the actual integer A, and the actual field indices underlying IN1 remain at the fixed proof.
The [Smy15-U001 fixed-field and power interface](../audits/literature/Smy15/Yin_U001.md#smy15-u001), including its retained statement/displayed-proof inspection, is unchanged; no new original Salem proof or regulator estimate is imported.

The analytic source is exactly [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), Theorem 3.1/equation (3.2) of the retained arXiv:1307.5734v1 edition.
For an integer polynomial P with simple roots and degree d>=55, a globally L-Lipschitz real function supported in the disk of radius R has discrepancy of its full-root mean from normalized circle mean at most L(2R+1)sqrt(log(max(d,M(P)))/d).
This accepts the retained statement/application interface; the original potential-theory proof and its external inputs are not newly independently audited.
The compact test functions, global Lipschitz constant, original total measure, both source errors and strict numerical margin are all proved below.

Only the final degree-uniform comparison for nonprimitive sources uses the accepted [C147 v5 numerical interface](Yin_C_G0147_v5.md#reuse-and-source-scope), equation (4) multiplied by the actual degree d.
Its underlying [Smy08-U001 statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001), retained survey printed p.326 equation (11), and the elementary logarithm conversion give

    m_0>=(1/2400)(log log d/log d)^3 for d>=exp(e).        (IN2)

The source statement, original-proof inspection and ancestor-review limits remain unchanged; neither the defective survey resultant explanation nor C147's cyclic-norm estimate is used.
The raw lower bound before that final nonprimitive comparison does not require IN2.
No joint phase distribution, Bilu input, numerical experiment, universal raw-p2 floor or new original-source proof audit is used.

## All-place normalization

All logarithms are natural unless a base is written.
For a nonzero algebraic number z of actual degree D_z and own field K_z, use its usual places v and local degrees n_v.
At infinite places n_v is 1 or 2 and the absolute value is the usual modulus.
At a finite place above p, use integer ord_v, ramification e_v and residue degree f_v, with n_v=e_v f_v and log|z|_v=-(ord_v(z)/e_v)log p.
Then

    h_abs(z)=(1/D_z)sum_v n_v log^+|z|_v,
    m(z)=D_z h_abs(z),
    M_2(z)^2=D_z sum_v n_v(log|z|_v)^2.                 (N1)

Thus m(z) is total logarithmic Mahler measure of the primitive irreducible polynomial, including its leading coefficient.
For a unit beta of actual degree D, all finite terms vanish.
If E denotes uniform averaging over the Galois group of any containing normal field, its restrictions to Q(beta) have constant fiber size, and

    h_beta=E log^+|sigma(beta)|=m(beta)/D,
    M_2(beta)=D sqrt(E[(log|sigma(beta)|)^2]),
    2m(beta)<=M_2(beta).                                (N2)

This retains the actual own degree even when Q(beta) is not Galois.
All integer-norm arguments below are used for actual nonzero algebraic integers; no favorable archimedean estimate is substituted for an unpaid finite-place contribution.

## Statement

### A. A strict Cayley marginal for general integer inputs

Put

    L_0=1+log(e+2),
    epsilon_d=L_0(2e+3)sqrt(log d/d),
    K=(2/3)log(707/250),
    eta=(log 2-K)/2>0,
    c=log 2-eta,
    k_0=(eta/8)^(1/4).                                 (S1)

There is an absolute d_1>=55 such that 2epsilon_d<=eta for every d>=d_1.
For every monic irreducible noncyclotomic P in Z[T] of degree d>=d_1 and total logarithmic Mahler measure m(P)<=1,

    (1/d)sum_(u:P(u)=0)log^+|(u+1)/(u-1)|<=c<log 2.      (S2)

The sum counts every root, including both roots of each nonreal pair.
No Salem, reciprocal or unit condition is needed for S2.
At these degrees the roots 1 and -1 are excluded by irreducibility, and the roots are simple.

### B. Arbitrary positive rational weights and the paid original return

Let alpha be a genuine Salem number of degree d=2t>=4, with splitting field L and actual inverse-pair kernel V.
Choose r distinct oriented inverse pairs, 1<=r<=t, with representatives u_i, and arbitrary positive rational weights a_i.
The weights, their denominators and their total W=sum_i a_i may depend arbitrarily on the original input, and no normalization or positive lower bound is assumed.
Set

    X_i=(u_i+1)/(u_i-1),
    Z=sum_i a_i X_i,
    beta=(Z+1)/(Z-1),
    D=[Q(beta):Q].                                      (S3)

Require the exact sign-domain condition

    r<t, or V is the full inverse-pair flip group,        (S4)

and require beta to be an actual algebraic integer.
The adopted v4 interface then makes it a nonzero nontorsion unit and gives all fields and norms in IN1.
Write alpha=alpha_0^A, m=log alpha, m_0=log alpha_0=m/A, with the actual integer power A>=1.
Assume 0<m<=1.

There is an absolute d_2, independent of the input and all weights, such that every such input and output with d>=d_2 satisfy

    M_2(beta)>=k_0 d^(1/4)m_0,
    M_2(beta)/m(alpha)>=k_0 d^(1/4)/A
      >=(k_0/2400)d^(1/4)(log log d/log d)^3.             (S5)

The last expression tends to infinity with d.
The last comparison is taken after enlarging d_2 to include d>=exp(e); the preceding raw estimate is independent of IN2.
For each fixed C>0, original sources in this exact domain with m(alpha)<=1 and an actual output satisfying M_2(beta)<=C m(alpha) have bounded degree and form a finite set.
The degree thresholds are not evaluated numerically, and k_0 is not claimed sharp.
The stronger coefficient 1/2 in the already adopted v4 convex subfamily remains available in its own exact scope.

### C. Signed rational coefficients and the retained exception

For an arbitrary rational linear combination of Cayley values of original roots, combine terms from the same inverse pair using C(u^(-1))=-C(u), where C(u)=(u+1)/(u-1), and remove zero coefficients.
If all coefficients cancel, the output is beta=-1 and is outside the nontorsion return problem.
Otherwise reorient the roots with negative surviving coefficients, making the weights positive without changing Z or beta.
Part B then applies whenever the resulting r distinct inverse pairs satisfy S4 and the output is integral.
Thus no sign, denominator, total-weight or input-dependent choice of nonzero rational weights evades the conclusion within that sign domain.

The higher odd full-use case r=t with the actual even-flip kernel is not supplied with missing individual flips.
It retains the exact v4 actual-unit norm-one gate; input-field-dependent coefficients, other coupled functions and general splitting-field units are outside this rational linear Cayley operation.
No unrestricted G0001 positive total-Mahler gap or automatic unit supply follows from these construction restrictions.

## Argument

<a id="p2-arbitrary-rational-cayley-weights"></a>
### Arbitrary rational Cayley weights in the supplied sign domain

The question is whether varying the total weight, rather than imposing the convex normalization in C866 v4, can supply a uniform raw-p2 return to the original total Mahler measure.
The argument treats arbitrary positive rational weights, and then arbitrary signed rational weights by combining inverse-pair terms and reorienting the surviving roots.
It keeps the same exact unused-pair or full-kernel sign domain as the adopted coordinate-norm result; it does not settle the higher odd full-use norm-one equation.

#### Fixed arithmetic inputs and the remaining scale

Use the original Salem setting and definitions of [C866 v4 Part A](Yin_C_G0866_v4.md#statement): d=2t, selected oriented roots u_1,...,u_r from distinct inverse pairs, X_i=(u_i+1)/(u_i-1), and actual sign condition r<t or a full inverse-pair kernel V.
Let a_i>0 be arbitrary rational numbers, with no normalization or lower bound, and set

    Z=sum_i a_i X_i,
    W=sum_i a_i>0,
    beta=(Z+1)/(Z-1),
    D=[Q(beta):Q],
    alpha=alpha_0^A, m=log alpha, m_0=log alpha_0=m/A,
    B=M_2(beta)/m_0.                                    (FW1)

Assume beta is an actual algebraic integer; the adopted sign-domain argument then makes it a nontorsion unit and proves beta!=1,-1.
Assume also 0<m<=1.
All finite-place terms of beta therefore vanish, and all averages E below use the uniform actual Galois group G of the original splitting field.
Restriction from G to the embeddings of Q(beta) has constant fiber size |G|/D, so the same average gives the actual own-degree height and raw norm even when Q(beta) is not Galois.
Write h_beta=h_abs(beta)=E log^+|sigma(beta)|.

The adopted CQ4--CQ9 give actual H=Gal(L/Q(beta)) orbits O on the selected roots, with sizes q_O, positive norm exponents n_O and orbit count kappa.
The common weight within O is denoted a_O.
Their consequences needed here do not use convex normalization:

    B>=2N>=2kappa>=2,
    q_O>=2d n_O^2/B^2>=2d/B^2,
    r=sum_O q_O>=2d kappa/B^2>=2d/B^2,
    D>=2^r.                                             (FW2)

For the q_O inequality use B^2>=2d sum_O n_O^2/q_O; summing q_O>=2d n_O^2/B^2 gives the displayed r bound.
The earlier equal-weight field multiplicities and primitive-source power are retained at that fixed home rather than replacing D by a tuple or splitting-field degree.
The new issue is to pay W, which is no longer one.

<a id="strict-cayley-marginal"></a>
#### A strict marginal for arbitrary monic irreducible integer inputs

Let P be any monic irreducible noncyclotomic integer polynomial of degree d, with total logarithmic Mahler measure m(P)<=1.
There is an absolute d_1 and a fixed constant c<log 2 such that every such input with d>=d_1 satisfies

    (1/d)sum_(u:P(u)=0)log^+|(u+1)/(u-1)|<=c.            (FW3)

No Salem, reciprocity or unit hypothesis is imposed on this marginal statement.
At the large degrees used below, irreducibility in characteristic zero gives simple roots and excludes the roots 1 and -1.
The average is over all d roots, including both members of each nonreal pair.
For an application to an original Salem input, the actual Galois marginal of each selected root is exactly this uniform average; no joint distribution statement is required.
We prove the generic statement with explicit constants except for the eventual degree threshold.

For any root u of P,

    log^+|(u+1)/(u-1)|
      <=log^+|u+1|+log^-|u-1|,
    log^-x=max(0,-log x).

Since P(1) is a nonzero rational integer,

    (1/d)sum_(u:P(u)=0)log|u-1|
      =(1/d)log|P(1)|>=0.

The average of log^-|u-1| is consequently at most the average of log^+|u-1|.
It remains to bound the sum of the two full-root means of log^+|u+1| and log^+|u-1|.

Define chi(z)=min(1,max(0,e+1-|z|)) and

    phi_+(z)=chi(z)log^+|z+1|,
    phi_-(z)=chi(z)log^+|z-1|.

Each function is supported in the disk of radius e+1.
The function log^+|z+/-1| is globally 1-Lipschitz; it may first be capped at log(e+2), without changing its product with chi on the support.
The capped function is bounded by log(e+2) and is still 1-Lipschitz, while chi is 1-Lipschitz and bounded by one.
Thus both products are globally L_0-Lipschitz for L_0=1+log(e+2).
All roots of P lie in |z|<=e because P is monic and m(P)<=1, so the cutoff is exactly one at every root.

Apply exactly the accepted [Pri11-U001 Theorem 3.1 interface](../audits/literature/Pri11/Yin_U001.md#pri11-u001), with its retained statement/applicability and original-proof limits.
The polynomial P is an integer polynomial with simple roots and actual degree d>=55; M(P)=exp(m(P))<=e<d.
The two normalized circle means are the same, by z -> -z, and equal

    J=(1/(2pi))integral_0^(2pi) log^+|1-exp(i theta)| dtheta.

Their respective full-root means differ from J by at most

    epsilon_d=L_0(2e+3)sqrt(log d/d).                   (FW4)

On the positive arc pi/3<=theta<=5pi/3, the square of |1-exp(i theta)| is 2-2cos(theta), and outside that arc its positive logarithm is zero.
Concavity of log on this arc, whose normalized measure is 2/3, gives

    J<=(1/3)log(2+3sqrt(3)/(2pi)).                      (FW5)

Indeed the average of cos(theta) over the arc is -3sqrt(3)/(4pi), and log|1-exp(i theta)| is half the logarithm of that squared modulus.
For an explicit strict bound, use sqrt(3)<1733/1000 and pi>157/50 to obtain

    2+3sqrt(3)/(2pi)<17759/6280<707/250,
    (707/250)^2=499849/62500<8.

The square-root bound follows by squaring the positive rational number.
The pi bound can be checked without a decimal approximation: pi/4=atan(1/2)+atan(1/3), and integration of 1/(1+x^2)>1-x^2+x^4-x^6 gives

    pi>4[(1/2-1/24+1/160-1/896)
         +(1/3-1/81+1/1215-1/15309)]
       =7693325/2449440>157/50.

The two final rational comparisons are direct integer inequalities: 707*6280-17759*250=210 and 7693325*50-2449440*157=104170.
Set

    K=(2/3)log(707/250)<log 2,
    eta=(log 2-K)/2>0,
    c=log 2-eta=K+eta.                                 (FW6)

Choose d_1 so that d>=d_1 implies d>=55 and 2epsilon_d<=eta.
Combining the integer value P(1), both source errors and 2J<=K bounds the full-root Cayley mean by K+2epsilon_d<=c.
This proves FW3 uniformly over all the stated integer polynomials.
For the original Salem P_alpha, its full-root average is E log^+|sigma(X_i)| for every selected i, which is the exact application used below.
The use of two error terms is essential; no singular logarithm was inserted directly into the source theorem.

#### Both integer norms bound the total rational scale

The nonzero algebraic integers beta-1 and beta+1 have ordinary norms of absolute value at least one in the splitting field.
The first identity beta-1=2/(Z-1) gives

    E log|Z-1|<=log 2.

Pointwise, |beta-1|<=2max(1,|beta|), so |Z-1|>=1/max(1,|beta|).
Consequently

    E log^-|Z-1|<=h_beta,
    E log^+|Z-1|<=log 2+h_beta,
    E log|Z-1|>=-h_beta.                               (FW7)

The other identity beta+1=2Z/(Z-1) and its integer norm imply

    E log|Z|>=E log|Z-1|-log 2>=-h_beta-log 2.

All these logarithms are finite: the adopted linear independence excludes Z=0 and Z=1,-1, and beta is nonzero.
Put b_i=a_i/W; these are positive rational numbers with sum one, although the original weights are not normalized.
Pointwise,

    |Z/W|=|sum_i b_i X_i|
      <=max_i |X_i|<=product_i max(1,|X_i|),
    log|Z/W|<=sum_i log^+|X_i|.

Taking the actual Galois average and using FW3 gives

    log W>=-r c-log 2-h_beta,
    log(DW)>=eta r-log 2-h_beta.                        (FW8)

The last inequality uses D>=2^r and log 2-c=eta.
This pays even an exponentially small total weight through the actual output degree.

#### Actual radial events and the opposing degree bound

Fix k_0=(eta/8)^(1/4), so 0<k_0<1 and k_0^4<eta/4.
Suppose B<k_0 d^(1/4).
By FW2,

    r>=2d/B^2>(2/k_0^2)sqrt(d),
    D>=2^((2/k_0^2)sqrt(d)).

The unit normalization and m_0<=1 give

    h_beta<=B m_0/(2D)<=B/(2D),
    |log|sigma(beta)||<=B m_0/sqrt(D)<=B/sqrt(D).

These are at most 1/2 and 1, respectively, for every sufficiently large d, uniformly over 2<=B<k_0 d^(1/4), by the displayed exponential lower bound for D.
Enlarge the absolute degree threshold to include this condition and d>=d_1.

Choose an H-orbit O carrying at least W/kappa of the total weight mass.
Its common weight a satisfies

    a>=W/(kappa q_O)>=4W/(Bd),

using kappa<=B/2 and q_O<=t=d/2.
The actual event that a selected root from O is real has probability 2q_O/d>=4/B^2.
By FW7 and h_beta<=1/2, one has E log^+|Z-1|<=log 2+1/2<2.
Markov's inequality gives probability at most 2/B^2 for |Z-1|>exp(B^2).
Therefore an actual set of embeddings of probability at least 2/B^2 has both a real selected root from O and |Z-1|<=exp(B^2).
No independence between these two events is assumed.

On this intersection, |beta|<=e gives |Z+1|=|beta||Z-1|<=exp(B^2+1).
The absolute real part of Z is

    A_+=a coth(m/2)>=2a/m>=8W/(Bd m).

For positive x,y, |log x-log y|>=|x-y|/max(x,y).
Apply this to x=|Z+1|^2 and y=|Z-1|^2, whose difference has absolute value 4A_+, to get

    |log|beta||
      >=2A_+/max(|Z+1|^2,|Z-1|^2)
      >=[16W/(Bd m)]exp(-2B^2-2).                      (FW9)

At the actual own degree, M_2(beta)=D sqrt(E[(log|beta|)^2]).
The probability lower bound and FW9 imply

    M_2(beta)>=16sqrt(2) DW/(B^2 d m) exp(-2B^2-2),
    DW<=B^3 d m m_0/(16sqrt(2)) exp(2B^2+2)
       <=B^3 d/(16sqrt(2)) exp(2B^2+2).                 (FW10)

There is no finite-place omission: beta is already an actual unit, and both integer norms were taken before any logarithmic averaging.

#### Uniform contradiction and the original-measure conclusion

FW8, h_beta<=1/2, and FW2 give

    log(DW)>=eta r-log 2-h_beta
             >=2eta d/B^2-2
              >(2eta/k_0^2)sqrt(d)-2.

On the other hand FW10, B<k_0 d^(1/4), k_0<1, and 16sqrt(2)>1 give

    log(DW)<=(7/4)log d+2k_0^2 sqrt(d)+2.               (FW11)

The coefficient difference 2eta/k_0^2-2k_0^2 is positive; with k_0^4=eta/8 it equals 14k_0^2.
For every sufficiently large d the positive multiple 14k_0^2 sqrt(d) exceeds (7/4)log d+4.
Thus FW11 contradicts the preceding lower bound, uniformly over the entire assumed range of B.
There is consequently an absolute d_2 such that every actual unit in FW1's exact domain, with m<=1 and d>=d_2, satisfies

    M_2(beta)>=k_0 d^(1/4)m_0,
    M_2(beta)/m(alpha)>=k_0 d^(1/4)/A.                  (FW12)

The argument for this raw comparison uses no numerical lower bound for m_0.
To obtain a uniform original-source ratio including nonprimitive inputs, use 1/A>=m_0 from A m_0=m<=1 and exactly the accepted [C147 v5 numerical interface](Yin_C_G0147_v5.md#reuse-and-source-scope) at the actual degree d of alpha_0:

    M_2(beta)/m(alpha)
      >=(k_0/2400)d^(1/4)(log log d/log d)^3 ->infinity.

The source statement, its elementary conversion and original-proof limits are unchanged.
For each fixed C>0, original sources of m<=1 in this domain admitting M_2(beta)<=C m(alpha) therefore have bounded degree and form a finite set by the bounded integer-coefficient estimate.
The thresholds d_1,d_2 are not evaluated numerically, and k_0 is not claimed sharp.

#### Signed coefficients and the remaining exact boundary

For an arbitrary rational linear combination of Cayley values of original roots, first combine terms from the same inverse pair using C(u^(-1))=-C(u), and remove zero coefficients.
If all coefficients cancel, Z=0 and beta=-1 is torsion, outside the proposed nontorsion return.
Otherwise invert the orientation of each surviving root with a negative coefficient, making all remaining weights positive without changing Z or beta.
The theorem above therefore covers all nonzero rational weights on the surviving r distinct inverse pairs whenever r<t or the actual kernel is full.
No positive lower bound, total-weight normalization, denominator bound or fixedness in the original input is imposed.

The surviving higher odd full-use case with the actual even-flip kernel still has the exact [C866 v4 norm-one gate](Yin_C_G0866_v4.md#statement); this proof supplies no missing individual flips.
Input-field-dependent coefficients, other coupled functions and general splitting-field units remain outside this rational linear Cayley operation.
The exact adopted quartic unit control remains valid, and neither its existence nor the present exclusion resolves the unrestricted G0001 total-Mahler objective.

## Scope and review boundary

This fixed result consists of N1--N2, Statement A--C/S1--S5 and the complete FW1--FW12 argument, including the generic marginal proof and the signed-coefficient reduction.
The fixed v4 coordinate norms and actual degree are used precisely without its convex hypothesis; their proof is not copied or newly claimed as this version's contribution.
The strict marginal lemma uses only full original root means, the nonzero integer P(1), compact Lipschitz source tests and the exact circle calculation.
The probability intersection and both degree bounds use the actual Galois distribution and actual own degree, without joint-angle independence.
The original source power A, both integer norms and every finite-place condition remain explicit.
The previous v4 coefficient 1/2 is retained for its convex subfamily; this version extends the weight domain with the smaller explicit k_0.
No earlier review certifies this changed proof; the independent whole finding for this version is selected below, with its actual source and ancestor limits.
The unrestricted [G0001 total-Mahler objective](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:12 |
| status | proved |
| reason | Adopt complete N1--N2, A--C/S1--S5 and FW1--FW12 after independent whole R1088 v5. The generic strict Cayley marginal and both integer norms pay arbitrary positive or signed rational weights and their total scale; the actual output degree then gives a uniform divergent original-Mahler ratio in the exact unused-pair or full-kernel domain, with nonprimitive source powers paid. The stronger convex coefficient remains at v4. The higher odd full-use norm-one branch and other coupled operations remain outside this conclusion; no unrestricted total-Mahler gap or automatic output supply follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire A--C/S1--S5 with N1--N2, generic monic integer marginal, arbitrary rational weight scale and signs, exact sign domain, actual integrality, source powers, degree comparison and finite source consequence. |
| argument | [Complete argument](#argument) | Entire FW1--FW12, strict source marginal with both errors, two integer norms, actual radial event, uniform degree contradiction and signed reduction, with all stated exceptions. |
| dependency | [Adopted coordinate norms](Yin_C_G0866_v4.md#decision-whole-independent-review-2026-11-05) | Exactly Part A and CQ1--CQ9 for arbitrary positive weights, actual fields and output degree; the convex coefficient, quartic control and exceptional gate retain their own v4 scopes. |
| dependency | [Numerical source interface](Yin_C_G0147_v5.md#reuse-and-source-scope) | Only the numerical Dobrowolski statement and conversion at actual degree d for the final nonprimitive comparison; no raw-bound dependence on this input. |
| support | [Lipschitz discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact retained Theorem 3.1/equation (3.2), full-root probability, compact support and global Lipschitz assumptions, at accepted statement/application scope without a new source-proof audit. |
| support | [Fixed-field Salem generator](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Exact same-field degree and positive-power generator interface at retained statement/displayed-proof scope. |
| support | [Numerical height statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact numerical statement and normalization used through C147v5; original proof and defective resultant explanation are not invoked. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v5.md#whole-arbitrary-weight-cayley-finding) | Complete normalization, A--C/S1--S5 and FW1--FW12, generic marginal, both norms, actual field/degree and source costs, signed reduction and precise exceptions; ancestor and original-source limits retained. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
