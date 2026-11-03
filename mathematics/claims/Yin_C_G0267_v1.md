---
author: Yin
---

# Degree-only primitive-norm windows and exact integer certificate search

This retains the complete original2026-10-07 [L80](../ledger/Yin_L_G0080_v1.md) argument.
Every algebraic proof, exact input guard and source/evidence/coverage limit is preserved.
No native computation, source acquisition or research Task is executed.

## Statement

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d>=2 and m=log M(P).
For any finite rational-prime set S, s=|S|, let D_n=|Norm Phi_n(alpha)| and Prim_n the part of D_n coprime to n, exactly its primitive prime-ideal norm with all valuations.
The only added external premise is the retained2019 Dim19 v1 Theorem1 at statement scope: house(alpha)>=2^(1/(4d)).
Thus with c=log2/4, m>=c/d.
No original proof or later version is newly audited.

There exists a rational prime exponent q outside the primitive forbidden-prime support of S such that

    gcd(Prim_q,product_(ell in S)ell)=1,
    m>=[log Prim_q-d log2]/q>=m/4>=log2/(16d).

The explicit degree/cardinality endpoint is

    A=64d^2+d(s+2)+5,
    B=2 ceil(32A(logA)^2),
    q<=B.

An entirely integer alternative is

    h=ceil(log_2 A)=bit_length(A-1),
    B_int=64A h^2,
    q<=B_int.

Both are O_s(d^2 log^2(d+1)) for fixed s and retain every unit-circle, ramified and powered-degree guard from the complete primitive witness theorem.
The direct earlier endpoint 2ceil(128d max(4d/log2,s+1))^2 is also valid but is O_s(d^4).
The improved constants follow from a new exact varying-threshold calculation, without substituting eta=c/d into a fixed-eta big-O constant.
The complete finite criterion and both asymptotic leading ratios are retained; no prime-number theorem, best constant or numerical search is claimed.

Enumerate all rational primes q<=B_int, compute exact C_q and C_1 and form

    D_q=C_q/C_1,
    Prim_q=D_q/q^v_q(D_q).

The division is exact and C_1 is nonzero.
At least one candidate satisfies the gcd condition and the integer comparison

    Prim_q^(16d)>=2^(16d^2+q).

Full factorization of Prim_q and numerical knowledge of m are unnecessary.
This is a terminating finite certificate search, with height-dependent integer arithmetic and no coefficient-independent bit-complexity claim.
It guarantees a suitable prime in the range, not success at every prime.
The floor log2/(16d) vanishes with degree, and m/4 may vanish with m; no common positive gap, entropy-noncapture family or all-index primitive-divisor theorem follows.
The rational supporting primes need not be new at every earlier norm index, except for the explicitly forbidden set S.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:18 |
| status | open |
| reason | Register the entire retained original argument and exact existing inputs; actual current whole review and adoption follow separately. This performs no independent-review certification, source-proof audit, native execution or research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Exact external house premise, full primitive certificate and all-degree real/integer endpoints, varying-threshold asymptotics, terminating integer predicate and complete source/complexity/gap guards. |
| argument | [Entire original proof](#argument) | Every original substitution/ceiling/logarithm/constant/bit-length calculation, leading asymptotic comparison, exact norm division and integer-certificate equivalence. |
| dependency | [Complete primitive witness](Yin_C_G0265_v1.md#finite-set-primitive-norm-escape) | Entire finite-S primitive norm theorem with actual original root/ideal counts, thresholds, costs and eta dependence; no uniform eta is inferred. |
| dependency | [Exact finite window criterion](Yin_C_G0265_v1.md#finite-window-primitive-count) | Exact candidate/exclusion count and even-B finite criterion, including empty or insufficient windows; the varying-eta constants are proved here. |
| dependency | [Retained external house statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the original Dim19 2019v1 Theorem1 house>=2^(1/(4d)) for noncyclotomic monic irreducible degree>1 and house<=M; original proof and later version remain outside this check. |
| support | [Finite capture boundary](Yin_C_G0205_v1.md#capture-equivalence) | Only the distinction from a common positive lower bound on all positive constituent weights; no summable algebraic-unit family is constructed. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:23 |
| status | proved |
| reason | Adopt the entire original house-conditional degree-window and integer-certificate theorem after actual whole current self-review. The original 2019v1 external statement, fresh varying-eta constants, all-degree real/bit-length endpoints, exact norm predicate and height/vanishing-gap limits remain fixed; no source proof, native calculation or independent review is newly certified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact external house premise, full primitive certificate and all-degree real/integer endpoints, varying-threshold asymptotics, terminating integer predicate and complete source/complexity/gap guards. |
| argument | [Argument](#argument) | Every original substitution/ceiling/logarithm/constant/bit-length calculation, leading asymptotic comparison, exact norm division and integer-certificate equivalence. |
| dependency | [Dependency](Yin_C_G0265_v1.md#finite-set-primitive-norm-escape) | Entire finite-S primitive norm theorem with actual original root/ideal counts, thresholds, costs and eta dependence; no uniform eta is inferred. |
| dependency | [Dependency](Yin_C_G0265_v1.md#finite-window-primitive-count) | Exact candidate/exclusion count and even-B finite criterion, including empty or insufficient windows; the varying-eta constants are proved here. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the original Dim19 2019v1 Theorem1 house>=2^(1/(4d)) for noncyclotomic monic irreducible degree>1 and house<=M; original proof and later version remain outside this check. |
| support | [Support](Yin_C_G0205_v1.md#capture-equivalence) | Only the distinction from a common positive lower bound on all positive constituent weights; no summable algebraic-unit family is constructed. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0531_v1.md#current-degree-window-finding) | Entire exact current statement, full original argument and every selected interface, self-reviewed; original findings retain their actual old inputs and precise scopes. |

## Complete retained argument

<a id="argument"></a>

<a id="degree-only-primitive-escape"></a>
### Statement and exact external input

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P, degree d>=2, and m=log M(P).
Let S be any finite set of rational primes and s=|S|.
For n>=1 write

    D_n=|Norm(Phi_n(alpha))|,
    Prim_n=the part of D_n coprime to n.

By [L G0078](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers), Prim_n is exactly the norm of the primitive prime-ideal part, including full valuations.
This does not mean that every underlying rational prime is new in the earlier cyclic norms.

The only additional external input is the retained Dim19 v1 Theorem 1 at the statement scope in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-house): for a noncyclotomic monic irreducible polynomial of degree d>1,

    house(alpha)>=2^(1/(4d)).

The theorem's original proof is not newly audited, and no later source version is being substituted.
Since house(alpha)<=M(P), putting c=log 2/4 gives the exact usable consequence

    m>=c/d.                                                 (1)

There is a rational prime exponent q for which

    gcd(Prim_q, product_(ell in S) ell)=1,
    m >= [log Prim_q-d log 2]/q >=m/4>=log 2/(16d).          (2)

An explicit upper bound depending only on d and s is

    A=64d^2+d(s+2)+5,
    B=2 ceil(32 A(log A)^2),
    q<=B.                                                  (3)

In particular B=O_s(d^2 log^2(d+1)) for fixed s.
The magnitudes of the excluded primes do not enter this exponent bound.
All unit-circle conjugates, ramified primes and degree-losing powers remain within the scope inherited from L G0078.

<a id="varying-threshold-window-check"></a>
### Rechecking the time bound when eta varies with degree

First, direct substitution eta=c/d into the explicit theorem of [L G0078](Yin_C_G0265_v1.md#finite-set-primitive-norm-escape) already gives the valid degree-only window

    B_0=2 ceil(128d max(4d/log 2,s+1))^2.                   (4)

The entry 1 in the earlier maximum is redundant because d>=2.
For fixed s this is O(d^4).
One cannot obtain a better uniform bound by simply substituting eta=c/d into an O_(eta,s) expression proved while eta was fixed; its implicit constant and threshold may themselves depend on d after that substitution.

Instead use the exact finite criterion from L G0078.
With

    L_d(B)=max(d+2,ceil(2+(4d^2/c)log(2B))),

it suffices that an even integer B>=16 satisfy

    B/(4 log B)>=L_d(B)+d(s+1).                             (5)

That criterion counts enough candidate primes to survive all d archimedean exclusions and at most ds exclusions from S; its conclusions are the full inequalities (2), not merely the existence of a divisor.

We now verify (5) for (3) in all degrees.
For B>=16, log B>=1, log(2B)<=2 log B, and log 2>1/2.
The ceiling and the maximum therefore give

    L_d(B)+d(s+1)
       <=d(s+2)+5+(8d^2/c)log B
       <=[64d^2+d(s+2)+5]log B
        =A log B.                                         (6)

Here 8/c=32/log 2<64.
Also A>=128, and the even rounding in (3) implies

    64A(log A)^2<=B<=128A(log A)^2.

The upper inequality uses that the unrounded lower quantity is already at least 2.
Since (log x)^2<=x for x>=1, and log 128<=log A, we obtain

    log B<=log 128+log A+2 log log A<=3 log A.

For completeness, the elementary inequality (log x)^2<=x follows by maximizing (log x)/sqrt(x), whose maximum is 2/e<1.
Hence

    B>=64A(log A)^2>36A(log A)^2>=4A(log B)^2,
    B/(4 log B)>A log B>=L_d(B)+d(s+1).                    (7)

This proves the explicit improved window (3).
Its asymptotic order follows directly from A=O_s(d^2) and log A=O_s(log d).
No prime number theorem or new numerical search is used.

One can also check the leading scale in (5) directly.
For fixed s, an even B asymptotic to K d^2 log^2(d+1) satisfies

    [B/(4 log B)]/[d^2 log d] -> K/8,
    [L_d(B)+d(s+1)]/[d^2 log d] -> 8/c.

Thus every K>64/c=256/log 2 is sufficient for all sufficiently large d, with an enlarged constant covering the remaining finite degrees.
This is a fresh varying-eta calculation: log B/log d tends to two, rather than the value one used in the fixed-eta proof.
Formula (3) provides the simpler explicit all-degree choice; no best-constant claim is made.

For an entirely integer cutoff, there is the alternative

    h=ceil(log_2 A)=bit_length(A-1),
    B_int=64A h^2.                                         (7a)

Here A>=265, so h>=4 and h^2<=2^h<2A.
The first inequality holds at h=4 and persists by induction.
Consequently B_int<128A^2<=A^3, giving log B_int<=3 log A.
Also h>=log A, so

    B_int>=64A(log A)^2>4A(log B_int)^2.

Thus (6)--(7) and the finite criterion (5) apply to B_int as well.
It is even, is computed with integer arithmetic only, and is still O_s(d^2 log^2(d+1)).
This avoids needing to evaluate a real-valued ceiling to select a search endpoint.

<a id="integer-primitive-escape-certificate"></a>
### A finite certificate search with integer comparisons

No approximation of the unknown m is required to find a certificate for the promised floor log 2/(16d).
Enumerate the rational primes q<=B_int; it is harmless to include the smaller primes below L_d(B_int).
Compute the nonzero integer C_q=|Norm(alpha^q-1)|, for example as an integer determinant in the companion order.
Then

    D_q=C_q/C_1,
    Prim_q=D_q/q^(v_q(D_q)),                               (8)

because q is prime.
The division is exact by cyclotomic factorization, and C_1 is nonzero.
Full factorization of Prim_q is not necessary: its coprimality with the known product of S can be checked by a gcd.
Moreover

    [log Prim_q-d log 2]/q>=log 2/(16d)

is equivalent to the exact integer inequality

    Prim_q^(16d)>=2^(16d^2+q).                             (9)

At least one candidate passes both the gcd test and (9), by (2)--(7a).
This is a terminating finite search with a degree-and-cardinality bound on its exponent range.
It is not a bound on bit complexity independent of the coefficients of P: the integer norms and their computation still depend on the input's height.
Likewise, the claim is existence of an eligible witness in this range, not success at every prime in it.
No numerical execution is claimed here.

<a id="degree-only-escape-gap-boundary"></a>
### Why this does not supply a uniform Mahler gap

The corollary removes the need to supply an unknown positive entropy threshold to obtain some controlled-time primitive certificate outside S.
It is valid throughout the positive irreducible unit class, subject to the explicitly accepted house theorem.
Its guaranteed numerical floor is nevertheless log 2/(16d), which tends to zero.
The stronger relative guarantee m/4 also becomes small if m itself becomes small.
No combination of these two observations supplies a positive constant independent of degree.

In particular this does not establish the common-constant capture hypothesis of [L G0002](Yin_C_G0205_v1.md#capture-equivalence).
A degree-dependent lower bound can be summable along an unbounded degree sequence; that observation is only about the strength of the inequality, not a constructed family of units with summable positive Mahler weights.
The remaining arithmetic obligation is a degree-independent positive certificate, or another mechanism that rules out the uncaptured small-entropy sequence.
A bound on where a vanishing certificate can be found is different information.

The outside-S statement does not prohibit useful inside-S certificates for the same input.
It also does not assert that the rational primes supporting Prim_q are new relative to every earlier index, except insofar as they are excluded by the supplied S.
No new uniform gap, all-index primitive divisor statement or source-proof audit is claimed.
