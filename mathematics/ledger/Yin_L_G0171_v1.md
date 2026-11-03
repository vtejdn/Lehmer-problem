---
author: Yin
---
# Explicit trace-unit families in an exact Salem return core

Date: 2026-10-10.
Direct follow-on by the coordinating AI for Yin from the now fixed [L170 co-return and exact-strip theorem](Yin_L_G0170_v1.md#exact-salem-return-strip).
This supplies explicit infinite algebraic families, rather than only a geometric infinitude proof.
The initial draft was self-checked; the complete separately organized noncontributor review is retained below.
The coordinator fixed this result on 2026-10-10 after that review passed.
No new computation or external source is required.

<a id="explicit-salem-core-families"></a>
## Conditional theorem and its two fixed applications

Let beta in (1,2) be a Salem unit with minimal polynomial P of even degree d=2s+2.
Suppose the narrow co-return premise of L170 holds.
Then the exact original {-1,0,1}-digit return core D has the strip description proved there.
Put

    a=beta+beta^(-1)-2=(beta-1)^2/beta,
    y_n=a^n,   x_n=a^n-1,   n>=1.                   (1)

Here a denotes an actual algebraic integer in O=Z[beta], not only its expanding real value.
Its two real embeddings are equal and belong to (0,1/2).
Consequently all y_n and x_n lie in D: their real coordinates have magnitude less than one, so they already lie in the smaller reciprocal co-return slab of L170.
The elements within each sequence are distinct and x_n is never zero, because their real values are distinct powers of a number strictly between zero and one.

Let a_j=zeta_j+zeta_j^(-1)-2 for the s upper unit conjugates, and define

    lambda=max_j |a_j|,
    h_a=sum_(sigma:Q(beta)->C) log max(1,|sigma(a)|).

Then lambda>1 and h_a>0.
No conjugate of a is zero or has modulus one.
There is a constant c>0, depending on beta, such that

    log |Norm_(Q(beta)/Q)(x_n)| = n h_a+O(exp(-c n)). (2)

In particular x_n gives an explicit exponential-norm family of actual returning states.
The prime-ideal divisors of this one sequence alone have no finite global cover.
Neither assertion requires the ESS counting theorem.

Moreover

    Norm_(Q(beta)/Q)(a)=P(1)^2.                      (3)

If |P(1)|=1, every y_n is an algebraic unit in O.
Thus D contains infinitely many distinct actual unit states, even though its restricted core D_S is finite for each fixed finite prime set S by the accepted L157 theorem.
This distinction has a concrete forced-excursion consequence below.

The co-return premise and P(1)=-1 are established for both the original degree-ten Lehmer input in [L170](Yin_L_G0170_v1.md#lehmer-infinite-core-theorem) and the quartic t^4-t^3-t^2-t+1 in [L169](Yin_L_G0169_v1.md#quartic-infinite-core-theorem).
Therefore all conclusions, including the infinite unit families, apply to those fixed inputs unconditionally relative to their retained proofs.
No co-return assertion for other Salem inputs is made here.

## Proof of hyperbolicity and norm growth

For 1<beta<2, the function beta+beta^(-1)-2 is strictly increasing from zero to one half.
The two real embeddings of a are this same value.
Each neutral value a_j=2Re(zeta_j)-2 belongs to (-4,0).
It cannot be zero, since zeta_j is not one.
It cannot equal -1, since that would make zeta_j a primitive sixth root of unity.
Irreducibility would then force beta itself to be a root of unity.
The value +1 is outside the displayed interval.
Thus all conjugate moduli differ from both zero and one.

The integer a is nonzero, so its nonzero integral field norm has absolute value at least one.
If all its conjugates had modulus at most one, the two strictly contracting real ones would make that norm strictly less than one.
Some neutral modulus therefore exceeds one, giving lambda>1 and h_a>0.
This argument does not assume a is a unit.

For any conjugate u of a, if |u|>1 then

    log|u^n-1|=n log|u|+log|1-u^(-n)|;

if |u|<1, then log|u^n-1|=log|1-u^n|.
The latter terms tend to zero exponentially in either case.
There are only finitely many embeddings and none has modulus one, so their sum proves (2).
The use of all d embeddings retains the multiplicity two when a lies in the real trace subfield.
Formula (3) follows from a=(beta-1)^2/beta, Norm(beta)=1, and Norm(beta-1)=P(1) in even degree.
When this norm is one, multiplication by a on the free order O has integral determinant one and hence an integral inverse, so a is a unit of O itself.

<a id="explicit-prime-escape"></a>
## An elementary prime-divisor escape proof for x_n

Fix any finite set S of nonzero prime ideals of the maximal order of Q(beta).
For each p in S not dividing a, choose the multiplicative order of a in the finite residue field.
Take N to be a common multiple of these orders, or N=1 if there are none.
For p dividing a we instead have a^N=0 modulo p.
Let L be the product of the distinct rational residue characteristics occurring in S, with L=1 for the empty set.

For arbitrarily large k=1+jL, form the algebraic integer

    H_k=1+a^N+...+a^((k-1)N),
    a^(Nk)-1=(a^N-1)H_k.                            (4)

If p in S divides a, then H_k=1 modulo p.
Otherwise a^N=1 modulo p and H_k=k=1 modulo p.
Therefore no p in S divides H_k.
On the other hand (2) and multiplicativity of field norm give

    log|Norm(H_k)|=Nk h_a-log|Norm(a^N-1)|+o(1),

which tends to infinity.
For sufficiently large k the integer H_k is not a unit and must have a prime-ideal divisor outside S.
That prime divides x_(Nk) by (4).
This proves the claimed absence of a finite cover for the explicit sequence.
It uses elementary residue-field orders and integral norms, not a primitive-divisor theorem or a claim that each term has a new prime.

<a id="infinite-units-forced-excursions"></a>
## Infinite returning units and unavoidable nonunit excursions

Assume |P(1)|=1.
For every fixed finite prime set S, all y_n are units and therefore belong to the ambient set

    V_S=D intersect ({0} union E_S)

of L157.
Thus V_S is infinite, including for S empty.
The accepted [L157 restricted-core theorem](Yin_L_G0157_v1.md#finite-prime-return-core) instead makes D_S finite, where D_S comprises states on closed original words whose every nonzero state is an S-unit.
Since the y_n are distinct, all but finitely many fail to belong to D_S.

For each such y_n, every actual zero-to-zero word passing through y_n must contain a nonzero state that is not an S-unit.
All states are algebraic integers, so this means a positive valuation at some prime ideal outside S.
Existence of a closed word through each y_n follows from actual core membership; the conclusion says none can avoid the necessary excursion.
This is not a frequency or probability lower bound for those excursions.

The fixed-core theorem therefore gives more than unbounded state norms: it constructs infinitely many actual unit endpoints that force exit from any prescribed finite-prime restriction somewhere along every completing closed path.
The finite D_S and infinite V_S are compatible.
This directly illustrates why a finite prime-restricted model need not cover returning unit states, and why replacing all units by a single weight or cell loses arithmetic information.
It does not improve the complete weighted return tail, give a uniform near-one estimate, or close G0001.

## Reuse, contribution and review boundary

The coordinator checked the current L169/L170 co-return/strip hypotheses and L157's distinct D_S and V_S definitions before this deduction.
All new formulas and proofs are written above.
The fixed norms/prime conclusions previously obtained through accepted equivalences receive an explicit elementary witness family; the new infinite-unit/forced-excursion conclusion still uses L157's finite restricted-core theorem, including its accepted ESS scope.
The stored fixed proofs are not rewritten and their historical dependency choices remain unchanged.
The proof uses no unvalidated numerical root value and requires no separate program.
The initial authoring stage requested independent review; the completed finding follows below.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0070_v1.md#separate-noncontributor-written-review), with its original inspected scope and relationship.



<a id="explicit-trace-family-fixed-retention"></a>
## Fixed retention

On 2026-10-10 the coordinating AI for Yin adopted this complete proof-only finding at its stated conditional and fixed-input scope after the independent review below the proof had passed without correction.
It replaces the completed rolling draft Yin_D_G0032.
All displayed mathematics and the entire review account are preserved.
The exact-core inputs remain L169/L170; the elementary norm/prime argument does not use ESS, while the forced-excursion conclusion retains L157 and its accepted external scope.
No current Claim or Task completion decision changes.
G0001 remains active and unresolved.
