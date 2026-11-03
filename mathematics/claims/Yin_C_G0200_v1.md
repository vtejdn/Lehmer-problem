---
author: Yin
---
# Cyclotomic H35 costs: unbounded energy and uniformly negative Haar logarithm

Date: 2026-10-20T15:38.
Human author Yin.
Root proposed the prime-cyclotomic input, exact sparse numerator, denominator and coefficient-inner-product argument.
The draft_inventory_later agent checked every exponent, sign, original field value and complete energy/logarithmic comparison on2026-10-20T15:32.
Both are mathematical contributors; this fixed candidate has no independent review yet.
The complete TC1--TC10 proof retains the necessary mathematics of that author account.
This is a domain calibration for the existing D36 logarithmic-cost question, not a nontorsion residual construction or a new objective.
No numerical computation, enumeration or source acquisition was used.

<a id="statement"></a>
## Exact theorem statement

For every prime p>30, let

    P_p(z)=Phi_p(z)=1+z+...+z^(p-1), d=p-1,
    H_p(z)=250P_p(z^3)^5-243P_p(z^5)^3,
    G_p(z)=-z^(-15d/2)H_p(z)/30375,
    J_p=integral_T log G_p(z)^2 dmu.             (TC1)

The sign is the displayed H35 convention of [C177](Yin_C_G0177_v1.md) and C195.
C189v4 uses the opposite H35 sign, which does not change any energy or Haar logarithm used here.
All Haar integrals and Lq norms use probability measure mu on the unit circle.
Then

    ||P_p||_2^2=p,
    ||H_p||_2^2>=p^3(250p-243)^2 ->infinity,
    J_p<=log(612120960/922640625)<0.              (TC2)

The upper bound is independent of p, and 922640625=30375^2 is the full unchanged normalization.
Here ||H_p||_2^2 is exactly the sum of squares of all coefficients, by finite Fourier orthogonality.
The assertions hold along the unbounded family of prime inputs; there is no finite table or sampled set of p.

These P_p are monic, irreducible, integral and reciprocal, with even degree, constant coefficient 1 and totally real trace field.
They are TORSION inputs with m(P_p)=0.
Every actual original quotient a,b,c is zero, as proved below.
Thus this family belongs to neither the nonzero-quotient original domain nor the full actual residual branch with g!=0.

For the actual trace polynomial T, the quotient polynomials rem_T(T(C_q))/q for q=2,3,5 are identically zero.
Consequently e=f=g=Q_s=0 and the H35 original resultant is zero; no logarithm of that zero norm is invoked.
The theorem disproves energy-to-positive-infinite-Haar inference on the enlarged torsion-inclusive class, not on the nontorsion nonzero-quotient domain.
It supplies neither a near-one nontorsion family nor an unrestricted original transfer.

<a id="argument"></a>
## Complete author proof and domain calibration

<a id="cyclotomic-h35-energy-log-calibration"></a>
## Exact question, reuse and result

The existing [C189v4 energy proof](Yin_C_G0189_v4.md#argument) bounds the actual coefficient energy and Fourier expense of a protected G component.
It does not give a lower bound for its Haar logarithm J_G tending to infinity with coefficient energy.
The [C195v2 signed comparison](Yin_C_G0195_v2.md#statement) retains that logarithmic quantity, the original contact term and the full same-input resultant as separate terms.
The present control tests the proposed inference from large energy to large Haar logarithm, while making the changed torsion domain explicit.
The existing G-series cyclotomic and energy materials were checked for this specific numerator mechanism; no exact matching H35 comparison was located.
This bounded reuse result is not a novelty claim about sparse cyclotomic quotients.

For every prime p>30, let

    P_p(z)=Phi_p(z)=1+z+...+z^(p-1), d=p-1,
    H_p(z)=250P_p(z^3)^5-243P_p(z^5)^3,
    G_p(z)=-z^(-15d/2)H_p(z)/30375,
    J_p=integral_T log G_p(z)^2 dmu.             (TC1)

The sign is the displayed H35 convention of [C177](Yin_C_G0177_v1.md) and C195.
C189v4 uses the opposite H35 sign, which does not change any energy or Haar logarithm used here.
All Haar integrals and Lq norms use probability measure mu on the unit circle.
Then

    ||P_p||_2^2=p,
    ||H_p||_2^2>=p^3(250p-243)^2 ->infinity,
    J_p<=log(612120960/922640625)<0.              (TC2)

The upper bound is independent of p, and 922640625=30375^2 is the full unchanged normalization.
Here ||H_p||_2^2 is exactly the sum of squares of all coefficients, by finite Fourier orthogonality.
The assertions hold along the unbounded family of prime inputs; there is no finite table or sampled set of p.

These P_p are monic, irreducible, integral and reciprocal, with even degree, constant coefficient 1 and totally real trace field.
They are TORSION inputs with m(P_p)=0.
Every actual original quotient a,b,c is zero, as proved below.
Thus this family belongs to neither the nonzero-quotient original domain nor the full actual residual branch with g!=0.

## Exact field and original-value boundary

The irreducibility and cyclotomic polynomial facts are the retained accepted scope of [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001).
For a primitive p-th root alpha, the field K=Q(alpha) has degree d=p-1.
Put delta=alpha+alpha^(-1) and F=Q(delta).
Every conjugate of delta is real, complex conjugation is nontrivial on K because p>2, and alpha satisfies X^2-delta X+1=0.
Therefore [K:F]=2, [F:Q]=(p-1)/2 and the actual monic trace polynomial T satisfies P_p(z)=z^(d/2)T(z+z^(-1)).
These statements also directly check the trace normalization without importing the nontorsion domain of a project theorem.

Use C_q(z+z^(-1))=z^q+z^(-q), a=theta_2(delta), b=theta_3(delta), c=theta_5(delta), and e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.
For q=2,3,5, the integer q is coprime to p.
Hence alpha^q and every corresponding conjugate are again primitive p-th roots, giving T(C_q(delta))=0.
Monic division by the minimal T in Z[X] therefore has zero remainder:

    theta_q=rem_T(T(C_q))/q=0, q=2,3,5,
    a=b=c=e=f=g=0,
    Q_s=(e+s g)^2+f^2+g^2=0.                   (TC3)

In particular P_p divides H_p, and the original H35 resultant is zero.
No logarithm of that zero resultant, positive original norm floor or original/Haar transfer inequality is invoked.
The circle function G_p is nonetheless a nonzero real Laurent polynomial: H_p has degree 15d and leading and constant coefficients 250-243=7, and its reciprocity makes the centered Laurent expression real on the circle.
Its finite circle zeros have integrable logarithms, by the exact scalar convention in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001).
Thus J_p is finite and well defined even though the original field values vanish.

## A fixed-degree cyclotomic denominator and the complete sparse numerator

Use the exact polynomial identity P_p(z^q)(z^q-1)=z^(qp)-1.
Set

    D(z)=(z^3-1)^5(z^5-1)^3,
    U_p(z)=(z^(3p)-1)^5(z^5-1)^3,
    V_p(z)=(z^(5p)-1)^3(z^3-1)^5,
    N_p(z)=250U_p(z)-243V_p(z).

Then, as an identity of integer polynomials,

    H_p D=N_p,
    deg D=30, deg H_p=15(p-1),
    deg N_p=15p+15=15d+30.                      (TC4)

The leading and constant coefficients of N_p are both 7, so it is nonzero.
All factors of D have their roots on the unit circle and leading coefficient 1; consequently m(D)=0.
The exact multiplicative Mahler identity therefore gives

    m(H_p)=m(N_p).                              (TC5)

This does not drop the denominator or any zero multiplicity.
All apparent poles of N_p/D are removable because (TC4) is an exact polynomial factorization.
No limiting comparison, root separation or approximation parameter is used.

## Every diagonal term and the four cross terms

Expand U_p using indices 0<=j<=5 and 0<=k<=3.
Its exponent is 3pj+5k and its coefficient is

    (-1)^(8-j-k) binom(5,j)binom(3,k).

Two such exponents can coincide only if 3p(j-j')=5(k'-k).
The right side has absolute value at most 15, whereas any nonzero left side has absolute value at least 3p>90.
Thus the pair (j,k) is unique.
The analogous expansion of V_p uses 0<=l<=3 and 0<=m<=5, exponent 5pl+3m and coefficient

    (-1)^(8-l-m) binom(3,l)binom(5,m),

and its exponents are likewise distinct.
Finite Fourier orthogonality and the elementary Vandermonde identity sum_j binom(s,j)^2=binom(2s,s) give

    ||U_p||_2^2=||V_p||_2^2
       =binom(10,5)binom(6,3)=252*20=5040.       (TC6)

For a cross term, equality of exponents is exactly

    p(3j-5l)=3m-5k.

The right side is between -15 and 15, so p>30 forces both sides to be zero.
The complete index ranges then give

    j=5t, l=3t, k=3u, m=5u,
    t,u in {0,1}.                              (TC7)

These are four distinct coinciding exponents, 15pt+15u.
Every involved binomial coefficient is 1, and the U_p and V_p signs are both (-1)^(t+u).
Each coefficient product is therefore +1.
There are no other cross terms, and the normalized inner product is exactly

    <U_p,V_p>=4,
    ||N_p||_2^2=5040(250^2+243^2)-8*250*243
                 =612120960.                   (TC8)

This is a complete symbolic exponent-collision proof, not a computer enumeration of a prime or a coefficient list.

## Normalized Haar upper bound versus divergent actual energy

Jensen's inequality for the probability measure and the integrable polynomial logarithm gives

    2m(N_p)=integral log|N_p|^2 dmu
       <=log integral|N_p|^2 dmu
       =log(612120960).

The centering monomial in (TC1) has modulus 1 on the circle.
Using (TC5), the precise scalar is therefore

    J_p=2m(H_p)-2log30375
       <=log(612120960/922640625)<0,             (TC9)

where 922640625-612120960=310519665>0 proves strict negativity without numerical logarithm evaluation.
The scalar lower bound m(H_p)>=log7 also confirms J_p>=2log(7/30375), although no sharp value or limit of J_p is claimed.

For completeness, the energy mechanism of C189 is applied through its explicit proof, not by extending its nontorsion theorem to this family.
Put x=||P_p||_10 and y=||P_p||_6.
Haar invariance under power maps, monotonicity of Lq norms on a probability space and the p unit coefficients give

    ||P_p(z^3)^5||_2=x^5,
    ||P_p(z^5)^3||_2=y^3,
    y<=x, x>=||P_p||_2=sqrt(p).

The reverse triangle inequality yields ||H_p||_2>=250x^5-243y^3>=250x^5-243x^3.
The derivative of 250t^5-243t^3 is t^2(1250t^2-729)>0 for t>=1.
Since p>30, this gives the actual lower bound

    ||H_p||_2^2>=p^3(250p-243)^2,
    integral G_p^2 dmu>=p^3(250p-243)^2/30375^2. (TC10)

Both quantities tend to infinity as p tends to infinity through the primes.
All coefficients, circle powers and the denominator are retained; this is not growth of a supplied upper estimate.

## Precise use and remaining obligation

The control disproves any implication from coefficient-energy divergence to J_G tending to positive infinity that uses only the enlarged monic irreducible reciprocal integral and totally-real-trace class.
It does not disprove an implication that essentially uses nontorsion or the actual nonzero original quotient values, since (TC3) violates those conditions.
In particular it is no near-one nontorsion family and no counterexample to the original norm floor, C189 or C195.
It shows concretely why the unresolved logarithmic comparison must use more than its retained energy obstruction.
The unchanged nontorsion problem still needs the same original resultant/Haar discrepancy, including all actual norm, scalar and transfer costs.

The complete inputs are C177/C195 for the exact H35/G normalization and comparison target, C189v4's explicit Lp/triangle mechanism rechecked at the present hypotheses, Bel17-U001 for the actual prime-cyclotomic identity and irreducibility, and Smy08-U001 for scalar Mahler/Jensen normalization and logarithmic zeros.
The new sparse factorization, all exponent collisions, exact L2 constant and torsion original-value boundary are proved here.
No independent acceptance of this new control, no value of an original zero logarithm and no solution of the D36 or G0001 goal is asserted.

<a id="exact-inputs"></a>
## Exact input roles

| Input | Exact role |
| --- | --- |
| [C177 convention](Yin_C_G0177_v1.md#statement) | Only original H35/G scalars and phase; no expansion of its nonzero original-norm theorem. |
| [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Cyclotomic identity, integrality and irreducibility at the actual retained scope. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Mahler normalization, multiplicativity, Jensen and integrable circle zeros. |
| [C189v4 mechanism](Yin_C_G0189_v4.md#argument) | Explicit Lp argument repeated completely at the changed hypotheses, not an application of its noncyclotomic-domain theorem. |
| [C195v2 comparison](Yin_C_G0195_v2.md#statement) | Responsible logarithmic question only; its nonzero-domain identities are not applied to these inputs. |

No mutable draft or computation is a mathematical premise.
The new sparse numerator, four cross terms and zero-value boundary are all proved above.
The root/inventory author check is not an independent review, and source-proof scopes are unchanged.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:38 |
| status | open |
| reason | Register the uniform prime-cyclotomic energy/logarithm separation, exact numerator constant and original zero-quotient boundary. Whole independent review remains required; no nontorsion counterexample or uniform gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact calibration](#statement) | Every prime p>30, divergent H35 energy, uniform negative normalized Haar upper bound and actual quotient/domain limits. |
| argument | [Complete TC proof](#argument) | All TC1--TC10, sparse exponents, four cross terms, scalars, multiplicities, Jensen and actual trace boundary. |
| dependency | [H35 convention](Yin_C_G0177_v1.md#statement) | Fixed definitions only, not the nontorsion arithmetic theorem. |
| dependency | [Cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Identity and irreducibility at actual source scope. |
| dependency | [Scalar Mahler source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Multiplicativity, probability Haar/Jensen and logarithmic zeros. |
| support | [Prior energy mechanism](Yin_C_G0189_v4.md#argument) | Full elementary recheck in TC10; no domain expansion of the older theorem. |
| support | [Signed comparison question](Yin_C_G0195_v2.md#statement) | Motivation and missing logarithmic term only; no zero original resultant evaluation. |
| support | [All input roles](#exact-inputs) | Exact definition/source/comparison roles, contributor boundaries and no mutable-D premise. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T15:45 |
| status | proved |
| authority | Internal adoption of the bounded logarithmic-cost calibration within Yin's retained D36 inquiry. |
| reason | Adopt the complete prime-cyclotomic TC1--TC10 control through actual whole independent R484. The actual H35 coefficient energy diverges while its normalized Haar logarithm has the stated uniform negative upper bound. All three original quotient polynomials and Q_s vanish, so the input is torsion and supplies no nontorsion or nonzero-original-norm counterexample. Every sparse coefficient, cross term, removable factor, logarithmic zero and scalar is retained. The original varying-input transfer remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact calibration](#statement) | Every prime p>30, divergent H35 energy, uniform negative normalized Haar upper bound and actual quotient/domain limits. |
| argument | [Complete TC proof](#argument) | All TC1--TC10, sparse exponents, four cross terms, scalars, multiplicities, Jensen and actual trace boundary. |
| dependency | [H35 convention](Yin_C_G0177_v1.md#statement) | Fixed definitions only, not the nontorsion arithmetic theorem. |
| dependency | [Cyclotomic source](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Identity and irreducibility at actual source scope. |
| dependency | [Scalar Mahler source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Multiplicativity, probability Haar/Jensen and logarithmic zeros. |
| support | [Prior energy mechanism](Yin_C_G0189_v4.md#argument) | Full elementary recheck in TC10; no domain expansion of the older theorem. |
| support | [Signed comparison question](Yin_C_G0195_v2.md#statement) | Motivation and missing logarithmic term only; no zero original resultant evaluation. |
| support | [All input roles](#exact-inputs) | Exact definition/source/comparison roles, contributor boundaries and no mutable-D premise. |
| review | [Whole cyclotomic H35 finding](../audits/reviews/Yin_R_G0484_v1.md#cyclotomic-h35-cost-whole-independent-finding) | Entire actual statement and TC1--TC10, all three dependencies and three supports, exact exponent/sign/constant calculations, complete scalar and zero multiplicities, actual trace and all-zero original-value boundary; no repair or enlargement of source scope. |

