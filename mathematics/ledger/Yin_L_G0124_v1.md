---
author: Yin
---

# A finite concentration threshold forces exact local-rule cancellation

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
The coordinator proposed combining the finite-memory moment mechanism with algebraic norm separation.
This note checks that combination, its degree loss, and an original-input boundary entropy estimate.
No source, computation or novelty claim is involved.

Use the hypotheses of [L G0121](Yin_L_G0121_v1.md#nonlinear-finite-memory-central-dichotomy): P is a monic irreducible algebraic-unit polynomial of degree d, m=log M(P)>0, beta is a unit-circle root, and xi_j are iid fair signs.
Let F:{-1,1}^{0,...,L}->Z, v_j=F(xi_j,...,xi_(j+L)), and write

    B=max|F|, mu=E F, B_0=||F-mu||_infinity,
    v_j-mu=sum_A R_A(S)Y_(A,j),
    V_beta=sum_A |R_A(beta)|^2.                       (1)

The translation-shape notation and rational Walsh coefficients are exactly those of L G0121.
Constants may depend on P, L and F.
The constant rule has zero algebraic-sum entropy and can be omitted below; otherwise B>=1 and B_0>0.

<a id="walsh-algebraic-norm-threshold"></a>
## A discrete lower threshold without counting all shapes

Put D=2^(L+1).
Every Walsh coefficient lies in D^(-1)Z.
Parseval for the complete Walsh expansion gives

    sum_(nonempty C) |c_C|^2=Var(F)<=B^2.

For any one shape A, its polynomial has degree at most L and coefficient Euclidean norm at most B.
At every conjugate gamma of P,

    |R_A(gamma)|<=B sqrt(L+1) max(1,|gamma|)^L.        (2)

Suppose V_beta>0 and select just one A with R_A(beta)!=0.
Q=D R_A is an integer polynomial, and Q(beta) is a nonzero algebraic integer.
Hence its field norm is a nonzero integer.
The roots beta and conjugate(beta)=beta^(-1) are distinct: irreducibility and m>0 exclude beta=+/-1.
Since R_A has real coefficients, those two norm factors give |R_A(beta)|^2.
Bound all other factors by (2).
This proves

    1<=|Norm Q(beta)|
      <=D^d |R_A(beta)|^2 [B sqrt(L+1)]^(d-2) exp(Lm),
    V_beta>=eta:=2^(-d(L+1))
                  [B sqrt(L+1)]^(-(d-2)) exp(-Lm)>0. (3)

The field degree in the norm is d, even if Q(beta) generates a smaller field.
No extra factor equal to the number of Walsh shapes occurs.
In particular, 0<V_beta<=epsilon requires

    log(1/epsilon)<=d(L+1)log2+(d-2)log B
                         +(d-2)log(L+1)/2+Lm.         (4)

This is a quantitative memory/height cost.
It explicitly worsens with d; it is not a degree-independent arithmetic separation bound.

<a id="finite-local-rule-endpoint-threshold"></a>
## Endpoint concentration and exact divisibility

Let W_N=sum_(j<N)(v_j-mu)beta^(-j), and let T_N be the same sum without centering.
L G0121 proves, for N>=max(1,2L),

    P(|W_N|>=sqrt(N V_beta)/2)
                >=V_beta^2/[384(L+1)^2 B_0^4]        (5)

when V_beta>0.
The mean contribution is uniformly bounded by

    |T_N-W_N|<=M_beta:=2|mu|/|1-beta|.

Consider any two complex random endpoint coordinates satisfying the actual central cocycle identity

    X_N-beta^N X_0=beta^(N-1)T_N/P'(beta).            (6)

They may depend arbitrarily on every input sign.
Fix a radius R>=0 and set

    tau=P(|X_0|>R)+P(|X_N|>R),
    D_R=2|P'(beta)|R+M_beta.

On the event that both endpoints lie within R, (6) implies |W_N|<=D_R.
Thus if N V_beta>4D_R^2, (5) forces tau>=V_beta^2/[384(L+1)^2B_0^4].
Equivalently,

    V_beta<=max{4D_R^2/N,
                   sqrt(384)(L+1)B_0^2 sqrt(tau)}.   (7)

Combining (3) with the strict finite conditions

    N>=max(1,2L),
    N>4D_R^2/eta,
    tau<eta^2/[384(L+1)^2B_0^4]                      (8)

forces V_beta=0.
The minimal-polynomial argument of L G0121 then gives P|R_A in Q[t] for every shape A.
This conclusion uses the actual endpoint concentration, not the mere existence of a formal central recurrence.
The two strict inequalities in (8) avoid an endpoint equality being counted as escape.

<a id="original-input-boundary-entropy-cost"></a>
## Exact cancellation has only an original-input boundary cost

When all P|R_A, L G0121 supplies

    v=P(S)g,
    g_j=mu/P(1)+sum_A (R_A/P)(S)Y_(A,j).             (9)

There is a sharper memory statement than just finite range.
A nonzero quotient R_A/P has degree at most L-max A-d, so each term of g_j uses only input indices from j through j+L-d.
If L<d all R_A vanish and F is constant.
If L>=d, g can therefore be taken to depend on at most L-d+1 consecutive input signs.

The exact P-filter boundary identity for sum_(j<N)v_j alpha^(-j) uses g_i only for i in [0,d-1] union [N,N+d-1].
Their underlying signs are contained in [0,L-1] union [N,N+L-1].
Consequently,

    H(sum_(j<N)v_j alpha^(-j))<=2L log2.              (10)

This holds even when the two input boundary intervals overlap.
The coefficient heights and the size of the rational alphabet of g do not appear.
The same bound holds for positive powers: P is reciprocal in the present irreducible unit-circle setting, and the positive-power filter identity has P(alpha^(-1))=0.
No reversal in law of the dependent filtered process is assumed.

For a sequence of rules F_N, (8) can be checked separately at each N with its actual L_N, B_N, endpoint radius and tail probabilities.
If it holds for all sufficiently large N and L_N=o(N), (10) gives vanishing normalized algebraic-sum entropy.
This is a pointwise finite-window statement and does not interchange a fixed-rule entropy limit with a varying-rule limit.

## Meaning and limitations

The bound (3) turns sufficiently small central variance, or the specific concentration data (8), into exact cancellation and hence the boundary entropy estimate (10).
It does not estimate entropy from a small but nonzero V_beta.
It does not supply the endpoint concentration needed in (8).
Its threshold can be exponentially small in dL and retains both the derivative |P'(beta)| and the distance |1-beta| in the finite-window test.
Therefore it does not give a uniform Mahler gap or prohibit arbitrary growing-memory repairs with positive algebraic entropy.

The coordinator proposed the norm/concentration task.
The assigned agent derived the conjugate-pair norm bound using Walsh Parseval, the endpoint constants, and the original-input boundary estimate, and checked all displayed formulas.

The coordinator read and checked the complete assembled (1)--(10), including the norm's degree-d normalization, the direction of (4), arbitrary-dependent endpoint coordinates, both strict inequalities, the quotient memory and original-sign boundary, and the varying-rule scope.
It found no defect.
This is collaborator verification because it proposed the combination and discussed its finite-memory use.

The separate agent review_matrix_completion independently read and checked all of (1)--(10).
Its review passed the Walsh denominator, one-shape Parseval estimate, conjugate-pair norm even when the value lies in a proper subfield, the threshold and logarithmic direction, all endpoint constants, the exact input boundary, positive-power reciprocity and varying-rule quantifiers.
It found no substantive mathematical defect.
This was a complete written proof review with no new source inspection or computation.
