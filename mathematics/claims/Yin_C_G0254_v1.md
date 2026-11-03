---
author: Yin
---

# Ramified cyclic-norm capture with explicit local powering costs

The complete original 2026-10-07 proof of [L72](../ledger/Yin_L_G0072_v1.md) is retained below.
Only its already used local/entropy interfaces are selected; all missing coverage and source limits remain explicit.

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible P of degree d and m=log M(P).
Fix a rational prime p, a finite p-adic splitting field with valuation v(p)=1, integers a,N,E>=1 and 0<gamma<=1.
If at least gamma d original root indices satisfy v(alpha_i^(aN)-1)>=1/E, let k be the least nonnegative integer with p^k>=E.
For every integer r>=0,

    m>=d[gamma(r+1)log p-log2]/(aN p^(k+r)).

The full binomial and cyclic-resultant proof includes fractional valuations and p2; no unramifiedness, distinct powered roots or degree preservation is required.
Fix p_0>=2,E,F>=1, C>0 and 0<gamma<=1.
If some prime p<=p_0 and integer a<=Cd put at least gamma d powered roots alpha_i^a in actual finite local fields with ramification index <=E and residue degree <=F, put

    N_p=lcm_(1<=f<=F)(p^f-1),
    k_p=min{k>=0:p^k>=E},
    Q_*=max_(p prime,p<=p_0) N_p p^k_p,
    R=ceil(1/gamma).

Then the original total measure satisfies

    m(P)>=gamma log2/[C Q_* p_0^R]>0.

The same parameters on all positive irreducible constituents, with multiplicity, give restricted finite entropy capture.
Local fields may differ and may be ramified; bounded reduced-root degree alone is insufficient.
For beta=alpha^a of degree d', the exact identities h(beta)=a h(alpha) and m(P_beta)=(a d'/d)m(P) retain every original embedding multiplicity.
A constant lower bound for m(P_beta) alone therefore does not erase a or d'.
The retained single-field DK25 comparison is conditional and supplies no missing uniform local-field or valuation coverage.
No external height theorem, numerical calculation or unproved prime-existence estimate is a premise of the direct proof.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:36 |
| status | open |
| reason | Register the entire retained original proof with explicit statement and exact existing interfaces; current whole review and any adoption follow separately. This performs no source acquisition, native execution or research resumption and claims no independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Complete valuation-amplification inequality, bounded actual-local-field uniform constant and exact degree/entropy/coverage boundaries. |
| argument | [Complete argument](#argument) | Entire original binomial/capped-recurrence, cyclic-resultant, local-membership and degree-normalization proof; all original indices and costs retained. |
| dependency | [Accepted total entropy](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Only the adopted monic irreducible companion total Mahler entropy, without a dimension divisor or fresh source audit. |
| dependency | [Finite capture](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible constituents counted with multiplicity; common positive gap yields restricted finite capture. |
| support | [Earlier cyclic norm interface](Yin_C_G0245_v1.md#cyclic-norm-residue-density) | Earlier unramified fixed-density special case, with the entire ramified extension proved here directly. |
| support | [Exact single-field comparison](../audits/literature/DK25/Yin_U001.md#dk25-u001) | Only the already retained finite single-field inequality and Proposition1.3 at its source-reading scope; not a premise of the direct valuation theorem or a coverage theorem. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:40 |
| status | proved |
| reason | Adopt the complete original ramified valuation/local-field theorem and exact degree-normalization/capture boundaries after actual whole current self-review. All fractional and binary depth costs, original-root multiplicities and conditional coverage guards remain explicit; no source was newly inspected and no native program or Task was run. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete valuation-amplification inequality, bounded actual-local-field uniform constant and exact degree/entropy/coverage boundaries. |
| argument | [Argument](#argument) | Entire original binomial/capped-recurrence, cyclic-resultant, local-membership and degree-normalization proof; all original indices and costs retained. |
| dependency | [Dependency](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Only the adopted monic irreducible companion total Mahler entropy, without a dimension divisor or fresh source audit. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible constituents counted with multiplicity; common positive gap yields restricted finite capture. |
| support | [Support](Yin_C_G0245_v1.md#cyclic-norm-residue-density) | Earlier unramified fixed-density special case, with the entire ramified extension proved here directly. |
| support | [Support](../audits/literature/DK25/Yin_U001.md#dk25-u001) | Only the already retained finite single-field inequality and Proposition1.3 at its source-reading scope; not a premise of the direct valuation theorem or a coverage theorem. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0527_v1.md#current-ramified-capture-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; original findings retain their actual old inputs and scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="ramified-valuation-capture"></a>
### A quantitative distance to roots of unity suffices

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d, and m=log M(P).
All logarithms are natural.
Fix a rational prime p and a finite p-adic splitting field of P, with valuation v normalized by v(p)=1.
Label all d roots alpha_i.
They are units.
Fix integers a,N,E>=1 and 0<gamma<=1.
Assume that at least gamma d root indices satisfy

    v(alpha_i^(aN)-1)>=1/E.                         (1)

Write k=ceil(log_p E), equivalently the least nonnegative integer with p^k>=E.
Then, for every integer r>=0,

    m >= d[gamma(r+1)log p-log2]/(aN p^(k+r)).       (2)

Proof.
For any v(x-1)>0, binomial expansion gives

    v(x^p-1)>=min(v(x-1)+1,p v(x-1)).               (3)

Each middle binomial coefficient is divisible by p; this includes p=2, where there is no middle term.
For any real t>0,

    min(1,min(t+1,pt))=min(1,pt).

Induction in (3) therefore shows that after k powerings, v(x^(p^k)-1)>=min(1,p^k/E)=1 whenever v(x-1)>=1/E.
Once the valuation is at least one, (3) raises it by at least one per further p-th power.
Consequently (1) implies

    v(alpha_i^(aN p^(k+r))-1)>=r+1.

The nonzero cyclic resultant C_L=Res(P,t^L-1), L=aNp^(k+r), is an integer and retains all d conjugates.
Nonvanishing follows from irreducibility and nontorsion.
Contributions from the other indices have nonnegative valuation, so

    v_p(C_L)>=gamma d(r+1),
    |C_L|>=p^(gamma d(r+1)).

At the complex embeddings, |C_L|<=2^d M(P)^L.
Taking logarithms proves (2).
No unramifiedness or degree-preservation condition is used, either for alpha or for its powered conjugates.
In particular this is not a discriminant argument with distinct powered nodes.

<a id="bounded-local-field-capture"></a>
### A fixed positive fraction of powered roots in bounded local fields

Fix integer bounds p_0>=2, E>=1, F>=1, a real C>0 and 0<gamma<=1.
Suppose some p<=p_0 and a<=Cd have the following property: at least gamma d of the roots beta_i=alpha_i^a belong to finite extensions K_i of Q_p with ramification index e_i<=E and residue degree f_i<=F.
The fields may differ; they need not be unramified, normal, or equal to the original root fields Q_p(alpha_i).

Put

    N_p=lcm_(1<=f<=F)(p^f-1),
    k_p=min{k>=0:p^k>=E},
    Q_*=max_(p prime,p<=p_0) N_p p^k_p,
    R=ceil(1/gamma).

All these constants are finite and independent of alpha and d.
Each selected beta_i is a unit of K_i, so its reduction has order dividing p^f_i-1.
Thus v(beta_i^N_p-1)>=1/e_i>=1/E.
Use (2) with N=N_p and r=R.
Since gamma R>=1,

    gamma(R+1)log p-log2>=gamma log2.

The conclusion is the all-degree uniform gap

    m(P)>= gamma log2/[C Q_* p_0^R] >0.             (4)

If all selected beta_i lie in one fixed field with residue degree f, N=p^f-1 is enough; the least common multiple is only used to cover possibly different residue degrees.
Condition (1), rather than local-field membership itself, is the exact proof input.

The original polynomial P may have highly repeated reduction modulo p.
Repeated reduction alone supplies neither the bound 1/E in (1) nor the bounded local ramification used to obtain it.
The valuation cost p^k_p is explicit and must not be omitted.
Conversely an actual order congruence alpha^a-c in pZ[alpha] already provides an integral norm route as in L G0067--G0069, without needing a bound on field ramification.

<a id="powered-height-and-local-occupancy"></a>
### Degree normalization and the comparison with a local-field criterion

Let beta=alpha^a and d'=[Q(beta):Q].
The exact height identities are

    h(beta)=a h(alpha),
    m(P_beta)=(a d'/d)m(P),
    m(P)=(d/(a d'))m(P_beta).                       (5)

Each distinct conjugate of beta occurs d/d' times among the d values beta_i.
Thus a fixed positive fraction counted using all original indices is the same fraction of the d' distinct values.
Equations (2)--(4) do not replace d by d' or discard multiplicity.

The single-field criterion of Dixit--Kala, arXiv:2507.20141v1, Proposition1.3, concerns actual conjugates lying in a fixed local field.
Its exact statement and full finite proof are retained in [DK25-U001](../audits/literature/DK25/Yin_U001.md#dk25-u001).
A lower bound m(P_beta)>=c by itself becomes only (d/(a d'))c under (5).
With a<=Cd and d' unbounded, that available guarantee can shrink to zero; a claim of a fixed gap cannot silently omit this degree and power cost.
The positive-fraction criterion above uses a quantitative height bound for beta, rather than just a constant lower bound for its logarithmic Mahler measure.
This comparison is not a claim that the source's full quantitative inequality can never do better for additional input data.

<a id="ramified-capture-entropy-scope"></a>
### Entropy meaning and missing coverage

By the already accepted companion-flow entropy formula, (4) bounds the original algebraic entropy.
A finite-entropy rational flow whose positive irreducible unit factors all satisfy the same fixed parameters p_0,E,F,C,gamma therefore has only finitely many positive factors counted with multiplicity, and L G0002 gives finite capture.

The valuation condition (1) includes the earlier unramified input and also permits controlled ramification.
Actual membership in bounded local fields is one sufficient way to obtain (1); it is not identified with the weaker condition of bounded degree of a reduced value.
This result supplies no theorem that all sufficiently small positive Mahler measures satisfy that condition.
In particular, every individual algebraic root generates a finite local extension, but the ramification and residue-degree bounds may grow with the input.
Finite local degree without uniform bounds is not (4).
