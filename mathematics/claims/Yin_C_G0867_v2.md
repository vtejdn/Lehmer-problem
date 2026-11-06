---
author: Yin
---
# Uniform disappearance of full small-prime mass in permutation determinants

## Scope and fixed inputs

This project deduction continues [G0001](../tasks/Yin_T_G0001_v1.md#contract) beyond the [first Smith-layer ceiling](Yin_C_G0867_v1.md#statement).
The exact target is actual p-adic valuation mass, including exceptional initial depths rather than only automatic good-prime lifts, within an original degree-linear random-permutation window.
The arithmetic-cycle contributor developed the local-depth decomposition and the coordinator contributed the growing-prime-budget extension and proof-scope checks.
The exact selected assessment, when present below, owns adoption of this version.
Reuse [C256](../claims/Yin_C_G0256_v1.md#statement), [L159](../ledger/Yin_L_G0159_v1.md#automatic-lift-average-capacity) and the retained [random-matrix comparison](../ledger/Yin_L_G0446_v1.md#scope-and-strategic-assessment).
The proof combines the accepted original-measure envelope with local valuation identities; it supplies no new positive arithmetic mass.
The earlier C867v1 first-layer result remains separately valid on its wider general-polynomial domain.
The present full-valuation result instead requires an irreducible nontorsion unit and a fixed bound on its total logarithmic Mahler measure.

## Statement

Let alpha be a nontorsion algebraic unit, K=Q(alpha), d=[K:Q]>=2, P its monic irreducible polynomial, and m=m(P)>0.
For k,t>=1 put R_k=|Norm_(K/Q)(alpha^k-1)| and D_t=|Norm_(K/Q)(Phi_t(alpha))|.
All roots and ideal multiplicities are those of the original field; no power-degree assumption is imposed.
Set b_t=log D_t>=0, and b_(p,t)=v_p(D_t)log p for rational primes p.
Cyclotomic factorization gives R_k=product_(t|k)D_t, and prime factorization of the positive integer D_t gives b_t=sum_p b_(p,t).
Every sum at a fixed t is finite.
These objects and the idealwise formulas are the adopted [C265 statement and argument](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers).
The terminology cyclotomic layer includes both primitive ideals and old p-power lifts; it does not mean rational primes appearing for the first time.

Let Pi_d be a uniformly distributed permutation matrix of size equal to the original degree d.
For a deterministic finite rational-prime set S, possibly dependent on P and d but independent of Pi_d, define

    Y=log|det P(Pi_d)|,
    Y_S=sum_(p in S) v_p(det P(Pi_d))log p,
    Theta_S=sum_(p in S)log p, s=|S|,
    H_n=sum_(j=1)^n 1/j, H_0=0.

Nontorsion and irreducibility make all these finite determinants nonzero; Y and Y_S are nonnegative.
Reciprocity is permitted but is not required.
The exact expectations are

    mu:=E Y=sum_(k<=d)log R_k/k
              =sum_(t<=d)(b_t/t)H_floor(d/t),
    E Y_S=sum_(t<=d)(sum_(p in S)b_(p,t)/t)H_floor(d/t). (HD1)

All these formulas retain the original degree and the full harmonic weighting.

<a id="all-depth-short-clock-localization"></a>
### All primes and all actual depths at sublinear clocks

Fix M>0 and assume 0<m<=M.
Write a=7/16 and use the [C147v5 function](../claims/Yin_C_G0147_v5.md#statement)

    Phi(h)=86 sqrt(h) log(1/h)^(5/2)/[log log(1/h)]^(3/2),
    0<h<=exp(-40).

For 0<x<=1 with xM<=exp(-40), define

    B_M(x)=Phi(xM)[(1+log(1/x))/a+1/a^2].

For every integer 1<=L<=d with LM/d<=exp(-40), the complete low-clock contribution, including every rational prime and every actual valuation depth, satisfies

    (1/d)sum_(t<=L)(b_t/t)H_floor(d/t)<=B_M(L/d).        (HD2)

For fixed M, the displayed B_M(epsilon) tends to zero as epsilon decreases to zero.
In particular, for any sequence d tending to infinity, m<=M and integer 1<=L_d<=d with L_d/d tending to zero, the full low-clock normalized expectation tends to zero uniformly over those inputs.
This remains true for L_d=d/log log d rounded down where defined; it is not restricted to a fixed finite number of initial times or primes.
The assertion uses no existence of near-zero Mahler values.

<a id="terminal-clock-mass"></a>
### A positive mean requires quadratic mass at terminal clocks

Suppose mu/d>=eta>0, with the same bounded-measure hypotheses.
Choose any fixed epsilon in (0,1) so small that epsilon M<=exp(-40) and B_M(epsilon)<eta/2.
For sufficiently large d, with L=floor(epsilon d)>=1, one has

    sum_(L<t<=d)b_t>=eta d L/[2H_floor(d/L)]
                  >=eta epsilon d^2/[4H_floor(2/epsilon)]. (HD3)

For a fixed chosen epsilon this is a positive constant times d^2.
It concerns the full original cyclotomic layer masses, with old and primitive parts both retained.
No such lower mass is supplied by this argument; (HD3) localizes the obligation left by a positive random-determinant mean.

<a id="full-small-prime-budget-ceiling"></a>
### Full actual valuations at a sublogarithmic prime budget vanish

For every M>0 and every sequence of actual inputs with degrees d tending to infinity and 0<m<=M, let S=S(P,d) be finite and independent of Pi_d.
If Theta_S=o(log d), then

    E(Y_S/d) -> 0,
    Pr(Y_S/d>=delta) -> 0 for every fixed delta>0.       (HD4)

More precisely, for every prescribed nonnegative function q(d)=o(log d), the convergence is uniform over all such inputs and deterministic prime sets with Theta_S<=q(d).
In particular it holds for every fixed finite set S.
It includes bad primes, every actual Smith layer, every exceptional initial or critical depth, and all original local multiplicities.
This is stronger in depth scope than C867's first-layer conclusion, with a different prime-budget range.
It neither bounds contributions from unrestricted prime sets nor supplies a lower bound on Y.

Here is an explicit estimate proving (HD4).
For any integer 1<=L<=d with LM/d<=exp(-40), put H=H_floor(d/L) and c_M=M+log 2.
Then

    E(Y_S/d) <= B_M(L/d)
       + c_M (d H/L)[Theta_S/log(L+1)
                         + s log 2/log(L/2+1)]
       + 2 H Theta_S/L.                               (HD5)

The empty S is permitted and has Y_S=0; the bound remains valid.

## Argument

### Exact determinant and harmonic identities

On a k-cycle, the eigenvalues of its permutation matrix are the k-th roots of unity, so the absolute determinant of P on that cycle is |Res(P,x^k-1)|=R_k.
Consequently Y=sum_(k<=d)C_k log R_k, and similarly for each rational-prime valuation, where C_k counts k-cycles of Pi_d.
Counting a distinguished k-cycle gives E C_k=binom(d,k)(k-1)!(d-k)!/d!=1/k.
Cyclotomic factorization gives log R_k=sum_(t|k)b_t and its exact p-adic analogue.
Writing k=t j and interchanging finite sums proves (HD1).
This also directly verifies the [retained L446 cycle interface](../ledger/Yin_L_G0446_v1.md#exact-cycle-law-and-the-probability-step) at the present hypotheses.

### Small-h control of the complete short-clock contribution

Because b_t<=log R_t and [C147v5](../claims/Yin_C_G0147_v5.md#statement) applies at the original degree, b_t/d<=Phi(tm/d)<=Phi(tM/d).
Writing ell=log(1/h), direct differentiation gives

    d log Phi(h)/d log h=1/2-5/(2ell)+3/(2ell log ell)
                        >=a for ell>=40.

Therefore Phi(tM/d)<=Phi(LM/d)(t/L)^a for t<=L.
Also H_floor(d/t)<=1+log(d/t).
The function x^(a-1)(1+log(d/x)) is decreasing on 0<x<=d, since its derivative has the sign of (a-1)(1+log(d/x))-1<0.
Consequently its sum at integers t=1,...,L is at most its integral on (0,L), equal to

    L^a[(1+log(d/L))/a+1/a^2].

Substituting these bounds in (HD1) proves (HD2).
For fixed M the factor sqrt(epsilon M) dominates every displayed power of log(1/epsilon), and the denominator is positive in the stated domain, so B_M(epsilon) tends to zero.
This proves both uniform localization conclusions in the statement.

### Terminal mass from a positive mean

Take epsilon as in (HD3) and L=floor(epsilon d).
The continuity of B_M at epsilon and the strict inequality B_M(epsilon)<eta/2 imply B_M(L/d)<eta/2 for all sufficiently large d.
Equations (HD1)--(HD2) therefore force

    sum_(L<t<=d)(b_t/t)H_floor(d/t)>=eta d/2.

On this range H_floor(d/t)/t<=H_floor(d/L)/L, which proves the first inequality in (HD3).
For d sufficiently large, L>=epsilon d/2 and floor(d/L)<=floor(2/epsilon).
These prove its second inequality without assuming that d/L or epsilon d is an integer.

### Local seeds and the remaining slope-one increments

At a prime ideal q of K above p, write e_q,f_q for its ramification and residue degrees, and put w_q=e_q f_q.
The complete local norm identities give sum_(q|p)w_q=d.
Let o_q be the multiplicative order of alpha modulo q, so p does not divide o_q and o_q<=p^(f_q)-1.
Normalize v_q by v_q(p)=1 and set u_j=v_q(alpha^(o_q p^j)-1)>0.
The contribution of q to b_(p,t) is supported exactly at t=o_q p^j and equals

    w_q u_0 log p at j=0,
    w_q(u_j-u_(j-1))log p at j>=1.                     (HD6)

This is the [C265 idealwise Mobius calculation](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers); its proof uses prime-to-p cofactor invariance and remains valid with ramification.
The [same C265 local-layer argument](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers), equations (4)--(7), gives the complete binomial recursion

    u_(j+1)=p u_j if u_j<1/(p-1),
    u_(j+1)=u_j+1 if u_j>1/(p-1),
    u_(j+1)>=u_j+1 if u_j=1/(p-1).                     (HD7)

Below the critical level the increment is less than one; above it the increment is exactly one.
There is at most one critical increment, because its output is already strictly above the critical level.
For the initial event use its entire weight w_q u_0 log p.
If a critical increment at index j=r has excess E_q=max(u_r-u_(r-1)-1,0), use the exceptional seed w_q E_q log p at clock t_q=o_q p^r.
Every remaining old increment is bounded by w_q log p.
Thus the full actual layer sequence is bounded by these two nonnegative seeds per ideal, when present, together with a slope-one weight w_q log p at every old clock o_q p^j, j>=1.
No bound on the size of E_q or u_0 has been imposed or inferred.

### Long initial seeds and long critical seeds cost local degree

If an initial clock o_q>L, then p^(f_q)>=o_q+1>L+1.
It follows that w_q>=f_q>log(L+1)/log p, so the number of such ideals above p is at most

    d log p/log(L+1).                                 (HD8)

For a critical clock t_q=o_q p^r, C265's exact critical-equality calculation gives p^(r-1)(p-1) dividing e_q.
In particular p<=e_q+1 and p^r<=p e_q/(p-1).
Consequently

    t_q<=e_q p sum_(j=0)^(f_q-1)p^j
        <=2(2^(e_q f_q)-1).                            (HD9)

For completeness, p<=e_q+1<=2^(e_q) and e_q p<=e_q(e_q+1)<=2(2^(e_q)-1), the last inequality holding for e_q=1,2 and then by induction.
Insert these bounds into the geometric sum to obtain (HD9).
Thus if t_q>L then w_q>log(L/2+1)/log 2, and there are at most

    d log 2/log(L/2+1)                                (HD10)

such exceptional ideals above p.
This counts each ideal at most once; no common splitting-field ramification degree is substituted for e_q.

Each individual seed at a clock t<=d is a nonnegative contribution to log D_t, or a nonnegative part of one, and hence at most log R_t.
The [C256 all-root norm estimate](../claims/Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) gives log R_t<=tm+d log 2<=d c_M.
Using H_floor(d/t)/t<=H/L for t>L, the normalized contribution from all long initial and exceptional seeds at this p is at most

    c_M (d H/L)[log p/log(L+1)+log 2/log(L/2+1)].        (HD11)

This is a count of actual ideal seeds, not a uniform valuation-depth bound.
Several ideals sharing a clock may cause this estimate to overcount, which only weakens the upper bound.

### All remaining old lifts and the complete estimate

For each fixed q, the clocks o_q p^j with j>=1 and o_q p^j>L form a tail of a geometric progression.
Their reciprocal sum is at most p/[(p-1)L]<=2/L.
The contribution of the slope-one envelope to the normalized long-clock expectation is therefore at most

    (1/d)sum_(q|p) w_q log p (2H/L)=2H log p/L.        (HD12)

It includes every old lift, rather than stopping at the first Smith layer or a chosen depth.
Sum (HD11)--(HD12) over p in S and bound the entire low-clock portion by the all-prime estimate (HD2).
This proves (HD5).

To deduce (HD4), first fix an arbitrarily small admissible epsilon>0 and take L=floor(epsilon d).
Then H is bounded in d by a constant depending on epsilon, d/L is bounded, and both logarithmic denominators in (HD5) are asymptotic to log d.
Since s<=Theta_S/log 2, the last two terms tend to zero whenever Theta_S=o(log d).
The limit superior is at most B_M(epsilon), by continuity and L/d tending to epsilon.
Now let epsilon decrease to zero and apply (HD2).
Markov's inequality gives the probability assertion because Y_S>=0.
All estimates are uniform in P, the ramification data, the actual initial depths and the chosen admissible prime set.

## Comparison and remaining positive mechanism

[C265](../claims/Yin_C_G0265_v1.md#statement) already supplies the exact cyclotomic local decomposition and critical old-depth classification.
[C267](../claims/Yin_C_G0267_v1.md#statement) supplies an actual primitive-norm witness beyond any finite prime set, with degree-dependent time and lower measure bound; it does not supply linear-window positive density.
[C450](../claims/Yin_C_G0450_v1.md#statement) supplies exact full layer averages, selected-prime spreading controls and their measure restrictions.
The present consequence combines those local structures with C147's original-degree small-h bound and the exact harmonic permutation clock.
No source claim of novelty is made.

The attempted mechanism was to exploit arbitrarily deep initial or critical p-adic divisibility at a few primes after the first-layer ceiling.
The calculation rules out this particular repair uniformly on bounded-total-Mahler inputs: a fixed finite set, and even Theta_S=o(log d), cannot contribute positive normalized random-determinant income through any actual depth.
The conclusion no longer depends on an example with measure growing like log d.
For a positive mean, (HD3) additionally forces quadratic logarithmic mass in degree-proportional cyclotomic clocks.
The remaining possible arithmetic mechanism must therefore supply sufficient actual terminal-clock mass through a prime budget outside this vanishing range, or change the ensemble and prove a new original-measure return.
No lower bound on that mass or a uniform Mahler gap has been proved.
The complete derivation uses no numerical experiment or native mathematical computation.
No formal verification or unrestricted Lehmer conclusion is claimed.

## Assessment history

### Decision whole-full-valuation-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T11:20 |
| status | proved |
| reason | Adopt HD1--HD12 after the independently organized whole finding R1089v2. Full actual prime valuation mass vanishes uniformly at a sublogarithmic prime budget on bounded-total-measure inputs, including every initial and critical depth. The all-prime short-clock bound and conditional quadratic terminal-mass requirement are included. The wider first-layer domain of v1 remains separately valid; no positive arithmetic supply, unrestricted prime-budget bound or Lehmer resolution is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Original irreducible nontorsion-unit domain, HD1--HD5, all-prime localization, terminal mass, prescribed prime budgets, uniform limits, probability consequence and exact scope boundaries. |
| argument | [Complete proof](#argument) | All HD1--HD12, original norm multiplicities, local seeds, unique critical excess, local-degree costs, full old-lift tails, floors and the ordered limiting argument. |
| dependency | [Original-degree norm envelope](Yin_C_G0147_v5.md#statement) | Only the accepted full cyclic norm bound at h=t m/d<=exp(-40), with every powered-field multiplicity and retained external-source proof boundary. |
| dependency | [Exact local cyclotomic layers](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) | Idealwise Mobius layers, prime-to-p cofactors, ramified binomial recursion and the exact critical-event divisibility and local e_q f_q clock bound. |
| dependency | [Norm and multiplicity identities](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original-field ideal norm weights and sum e_q f_q=d; the elementary full-root norm estimate is also checked directly in R1089v2. |
| review | [Independent full-valuation finding](../audits/reviews/Yin_R_G1089_v2.md#whole-full-valuation-finding) | Entire exact statement and argument, all required fixed-input interfaces, actual depths and uniformity; no new audit of original external theorem proofs. |

## Current assessment

[Selected decision](#decision-whole-full-valuation-review-2026-11-05)
