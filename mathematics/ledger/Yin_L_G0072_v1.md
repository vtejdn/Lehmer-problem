---
author: Yin
---

# G0001: cyclic norms with bounded local ramification after powering

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0254_v1.md#ramified-valuation-capture).
The original mathematical input below remains fixed; its actual historical review account remains separately located.
Direct argument by the coordinating AI for Yin.
This extends the explicit cyclic-norm interface of [L G0068](Yin_L_G0068_v1.md#cyclic-norm-residue-density) to a ramified valuation hypothesis.
It is not a coverage theorem for arbitrary small-Mahler inputs.
The relation to the newly inspected single-local-field discriminant criterion is recorded below; no external height theorem or numerical computation is a proof premise.

<a id="ramified-valuation-capture"></a>
## A quantitative distance to roots of unity suffices

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
## A fixed positive fraction of powered roots in bounded local fields

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
## Degree normalization and the comparison with a local-field criterion

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
## Entropy meaning and missing coverage

By the already accepted companion-flow entropy formula, (4) bounds the original algebraic entropy.
A finite-entropy rational flow whose positive irreducible unit factors all satisfy the same fixed parameters p_0,E,F,C,gamma therefore has only finitely many positive factors counted with multiplicity, and L G0002 gives finite capture.

The valuation condition (1) includes the earlier unramified input and also permits controlled ramification.
Actual membership in bounded local fields is one sufficient way to obtain (1); it is not identified with the weaker condition of bounded degree of a reduced value.
This result supplies no theorem that all sufficiently small positive Mahler measures satisfy that condition.
In particular, every individual algebraic root generates a finite local extension, but the ramification and residue-degree bounds may grow with the input.
Finite local degree without uniform bounds is not (4).

The complete original review account and actual finding-specific relationships are retained in [R527](../audits/reviews/Yin_R_G0527_v1.md#historical-ramified-author-finding).
The original date, exact proof scope and source/coverage limits remain unchanged.
