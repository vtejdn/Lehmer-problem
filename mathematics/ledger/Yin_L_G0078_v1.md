---
author: Yin
---

# G0001: exact primitive cyclotomic layers and controlled escape from finite prime sets

Date: 2026-10-07.
Current complete proof and exact statement: [responsible claim](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers).
The original mathematical input below remains fixed; its complete historical review account remains separately located.
Direct proof by assigned AI assess_shortness_route for Yin.
The coordinator and this agent independently identified the ramified exceptional-layer threshold.
The coordinator supplied the degree-only exception cutoff, the strengthened primitive-norm witness constants and the finite-prime-set exclusion argument.
This agent checked those contributions and assembled the proof.
No external primitive-divisor theorem is a premise.
No novelty claim is made for the classical local layer formulas.

The main new interface here is a controlled-time norm certificate supported entirely outside any supplied finite set of rational primes.
It reuses the elementary prime-avoidance method of [L G0076](Yin_L_G0076_v1.md#coprime-avoidance-lemma), not an unquantified periodic growth limit.

<a id="primitive-cyclotomic-local-layers"></a>
## Exact local layers and the meaning of primitive

Let alpha be a nontorsion algebraic unit, K=Q(alpha), O=O_K, P its monic irreducible polynomial, d=deg P>=2, and m=log M(P)>0.
For n>=1 put

    C_n=|Norm_(K/Q)(alpha^n-1)|,
    D_n=|Norm_(K/Q)(Phi_n(alpha))|.

These are nonzero positive integers.
Cyclotomic factorization and Mobius inversion give

    C_n=product_(k|n) D_k,
    v_p(D_n)=sum_(k|n) mu(n/k) v_p(C_k).                    (1)

Fix a rational prime p, with no good-reduction hypothesis.
Use the original-root order groups O_p, their multiplicities w_(p,o), and the normalized valuation sums B_(p,o,r) from [L G0074](Yin_L_G0074_v1.md#finite-exact-local-cyclic-table).
Write n=o p^r with p not dividing o.
Then exactly

    v_p(D_n)=B_(p,o,0)                         if r=0,
             B_(p,o,r)-B_(p,o,r-1)            if r>=1,     (2)

with value zero if o is not in O_p.
In particular the finite local table of L G0074 determines every cyclotomic layer as well as every cyclic norm.

To verify (2), write a divisor of n as a p^j with a|o.
For r>=1, only j=r and j=r-1 survive in (1).
The coefficient of the group with order b|o is then

    sum_(a: b|a|o) mu(o/a),

which is one for b=o and zero otherwise.
For r=0 the same calculation uses just the initial B entry.
The prime-to-p cofactor leaves a positive local valuation unchanged, as proved in L G0074.
This argument includes repeated reduction and does not assume that any power of alpha preserves degree.

At an individual prime ideal q above p, let o_q be the order of alpha in (O/q)^*.
That ideal divides Phi_n(alpha) only when n=o_q p^r.
Its integer valuation is ord_q(alpha^o_q-1) when r=0, and the difference of consecutive integer valuations of alpha^(o_q p^r)-1 when r>=1.
This follows from the identical Mobius calculation before taking a norm.

Call q primitive at n if it divides alpha^n-1 and divides none of alpha^k-1 for 1<=k<n.
This is equivalent to o_q=n.
Since o_q is prime to p, contributions to D_n are primitive precisely at the rational primes p not dividing n.
Define Prim_n as the norm of the product of those primitive prime-ideal contributions, with their full valuations in Phi_n(alpha), and Old_n=D_n/Prim_n.
Thus the exact integer split is

    Prim_n=product_(p not dividing n) p^v_p(D_n),
    Old_n =product_(p dividing n)     p^v_p(D_n).            (3)

In particular Prim_n is the part of D_n coprime to n.
This assertion is about primitive prime ideals, not new rational primes in the earlier cyclic norms.

The distinction already occurs in the actual small-Mahler core.
The retained Lehmer control in [J G0011](../computations/programs/Yin_J_G0011/readme.md) has a squarefree reduction modulo 3 with irreducible factors of degrees 2 and 8, whose exact root orders are 4 and 82 respectively.
Consequently 3 divides C_4, while a degree-eight prime ideal over 3 is primitive at index 82 and contributes to Prim_82.
The rational prime 3 is not new there.
These exact factor/order facts are reused from the retained verified payload, not newly computed or used to infer irreducibility or Mahler bounds for that input.

<a id="old-layer-exception-threshold"></a>
## Exactly where old valuation depth can be exceptional

Fix q above p, write e=e_q, f=f_q, and normalize v=ord_q/e, so v(p)=1.
Put o=o_q and u_j=v(alpha^(o p^j)-1)>0.
The initial valuation satisfies u_0>=1/e.
Binomial expansion gives

    u_(j+1)=p u_j       if u_j<1/(p-1),
    u_(j+1)=u_j+1      if u_j>1/(p-1),
    u_(j+1)>=u_j+1     if u_j=1/(p-1).                    (4)

For the first line the last binomial term has uniquely lowest valuation, and for the second the linear term does.
In the third line those two terms tie and may cancel.
Thus the only possibility of an increment greater than one is this exact critical equality.
After passing the threshold, every subsequent increment is exactly one.

In particular, for r>=1,

    p^(r-1)(p-1)>e  implies  u_r-u_(r-1)=1.                (5)

Indeed if u_(r-1) were at most 1/(p-1), every preceding step would have stayed strictly below that threshold, and (4) would give u_(r-1)=p^(r-1)u_0>=p^(r-1)/e>1/(p-1), a contradiction.
If a previous step had reached the threshold, the next step would already be strictly above it.
This also handles r=1.
If the increment at step r actually exceeds one, the equality case additionally forces

    u_0=1/[p^(r-1)(p-1)],

so p^(r-1)(p-1) divides e.
The weaker inequality in the contrapositive of (5) suffices for the bounds below.

At a good odd prime e=1, every old layer has normalized increment one.
At a good prime 2, this is true for r>=2; the first doubling r=1 can have an arbitrarily large initial increment.
In the original-root notation this says

    v_p(D_(o p^r))=w_(p,o)
        for good odd p and every r>=1,
    v_2(D_(2^r o))=w_(2,o)
        for good p=2 and every r>=2.                       (6)

More generally, since each e_q<=d, the equality in (6) holds at any rational prime p when p^(r-1)(p-1)>d, without requiring good reduction.
The root multiplicity w_(p,o) here counts the original d roots, including repeated reductions.
A contributing prime ideal has ord_q Phi_n(alpha)=e_q in this stable range, so its norm valuation is f_q e_q; their sum is w_(p,o)<=d.

There is also a degree-only bound for all possibly exceptional indices.
If an old contribution has p^(r-1)(p-1)<=e, then o<=p^f-1 and

    n=o p^r <= e p sum_(j=0)^(f-1) p^j
             <=2(2^(ef)-1)<=2(2^d-1).                    (7)

For the middle inequality, p<=e+1<=2^e and ep<=e(e+1)<=2(2^e-1); the last elementary inequality holds for e=1,2 and then by induction.
Multiplying the geometric sum by this bound proves the displayed estimate.
Also ef<=d.
Consequently, for every n>2(2^d-1),

    Old_n divides rad(n)^d,    Old_n<=rad(n)^d<=n^d.        (8)

The same conclusion holds at any specific n for which all contributing old ideals satisfy (5).
In particular, if the index q is a rational prime with q>d+1, its old part is a power of q of exponent at most d:

    Old_q<=q^d.                                           (9)

No upper bound for critical depths at the finitely many exceptional indices follows just from the degree.

For source comparison, the separately inspected [Ste77-U001](../audits/literature/Ste77/Yin_U001.md#ste77-imprimitive-bound) retains the weaker n^d imprimitive bound at its stated external source scope.
The rad(n)^d divisibility and threshold here were proved directly in (4)--(8); they do not depend on adopting that source theorem or its original proof.
No novelty inference follows from the difference between the two recorded formulations.

<a id="critical-old-depth-control"></a>
## An actual critical-depth control and its Mahler boundary

For k>=2 let s=1+2^k and P_k=t^2-s t+1.
Its discriminant s^2-4 lies strictly between (s-1)^2 and s^2, so it is irreducible.
Its roots are alpha>1 and alpha^(-1).
Every positive power still has degree two: a rational power would be a rational integral unit, hence +1 or -1, which is impossible.
Thus irreducibility, reciprocity, the unit condition and all-positive-power degree preservation are present.

Modulo 2 the polynomial is t^2+t+1, so 2 is a good prime and both reduced roots have order 3.
Direct evaluation using alpha^2=s alpha-1 gives

    Phi_6(alpha)=alpha^2-alpha+1=(s-1)alpha,
    D_6=(s-1)^2=2^(2k),    Prim_6=1.                       (10)

This entire growing layer is old, at the first doubling of residue order 3.
It shows why the first-doubling exception cannot be omitted even at a good prime of a reciprocal unit.
Here n=6 is exactly 2(2^2-1), so replacing the strict cutoff in (8) by a weak inequality would be false.
This is not a near-one counterfamily: alpha>s-1=2^k, so its Mahler measure is unbounded.
No failure of primitive coverage in the target small-Mahler class is inferred from this control.

<a id="finite-set-primitive-norm-escape"></a>
## A controlled primitive certificate outside any finite rational prime set

Let S be any finite set of rational primes, s=|S|, and 0<eta<=m.
Define

    W=d max(1,1/eta,s+1),
    B=2 ceil(128W)^2,
    L=max(d+2, ceil(2+4d log(2B)/eta)).                     (11)

Then there is a rational prime exponent q in [L,B] such that

    gcd(Prim_q, product_(ell in S) ell)=1,
    log Prim_q >= q m/2,
    [log Prim_q-d log 2]/q >= m/4 >= eta/4.                (12)

The empty product for S empty is one.
In particular there is a genuinely primitive prime ideal at index q lying over a rational prime outside S.
The bound (11) depends on the number of excluded primes, not on their magnitudes.
The expression in the last line is an actual lower certificate for m, since Prim_q divides D_q, which divides C_q.

Proof.
For every ell in S, P modulo ell has at most d distinct nonzero root orders, even when the reduction has repeated factors.
If a prime ideal above ell is primitive at a prime index q, then one of those orders equals q.
Therefore each ell forbids at most d prime exponent values.
At most ds candidates are forbidden in this way.
An equality ell=q never creates a primitive ideal over ell: a nonzero residue order is prime to its residue characteristic.
Its old contribution is removed in Prim_q.

For the archimedean part, use the d normalized roots z_i in the closed unit disk as in L G0076.
Its polynomial Bezout lemma says that for each z_i, at most one prime q<=B has |Phi_q(z_i)|<1/(2B).
Thus there are at most d additional bad prime exponent values.
Any prime outside these at most d(s+1) exclusions satisfies

    log D_q >=(q-1)m-d log(2B).                            (13)

This follows directly from D_q=M(P)^(q-1) product_i |Phi_q(z_i)|.
For cyclic norms L G0076 additionally needed C_1>=1; no C_1 factor is present in (13).
This is a direct cyclotomic-layer bound.

We check that [L,B] contains at least d(s+1)+1 primes.
The elementary binomial estimate in L G0076 gives pi(B)>=B/(4 log B) for even B>=16.
Here log B>=1, W>=d(s+1), and W>=d/eta.
Consequently

    L+d(s+1)
       <=max(2d+2+d s,
               3+d(s+1)+(8d/eta)log B)
       <=(21/2)W log B.                                  (14)

For the first term, 2d+2+ds<=3W when d>=2; for the second, 3<=3d/2<=3W/2 and each remaining term has the indicated bound.
Also (log B)^2<=3sqrt(B), while sqrt(B)>=128sqrt(2)W>126W.
Thus

    B>42W(log B)^2,
    pi(B)>=(B/(4 log B))>=(21/2)W log B
                            >=L+d(s+1).                  (15)

At most L-1 primes are below L, leaving the required candidates.
Choose q avoiding both finite exclusion lists.
It has no primitive prime-ideal contribution above S.
Since q>=d+2, (9) bounds its entire old part.
Equations (9) and (13) give

    log Prim_q >=(q-1)m-d log(2B)-d log q
                >=(q-1)m-2d log(2B).                     (16)

The lower cutoff q>=2+4d log(2B)/eta and m>=eta make the last quantity at least q m/2.
Also that cutoff implies q>=4d log 2/eta, hence d log 2<=q m/4.
This proves (12).

For fixed eta>0 and fixed s, the same argument gives the smaller asymptotic window O_(eta,s)(d log^2(d+1)).
Indeed it suffices to take any even B>=16 with

    B/(4 log B)>=
       max(d+2,ceil(2+4d log(2B)/eta))+d(s+1).              (17)

Choosing B asymptotic to A d log^2(d+1) works for every A>16/eta as d tends to infinity; a larger constant covers the remaining finite degrees.
Equation (11) is the explicit all-degree bound.
No linear or O(d log d) bound is claimed.

<a id="finite-window-primitive-count"></a>
## How many prime indices the same argument certifies

The proof gives more than one successful index.
For any even integer B>=16, define

    L(B)=max(d+2,ceil(2+4d log(2B)/eta)).

All but at most d(s+1) of the primes q in [L(B),B] satisfy all conclusions (12).
No lower prime-count estimate or special choice of B is needed for this assertion: the same two exclusion lists have at most ds and d members, and every surviving q satisfies (13)--(16).
Therefore the number of certified indices is at least

    max(0, pi(B)-pi(L(B)-1)-d(s+1)).                       (18)

For any N such certified indices, select one primitive prime ideal at each index.
These ideals are distinct because their residue orders are the different indices.
Above any one rational prime there are at most d prime ideals, since their positive integers e_q f_q sum to d.
Thus the selected ideals lie above at least ceil(N/d) distinct rational primes, all outside S.
Equivalently, one can use the fact that at most d distinct residue orders occur over a rational prime.
This counts distinct rational primes across the window, without asserting that each was absent from every earlier cyclic norm.
It uses the same supplied eta; it is not a proof of a common positive entropy threshold.

<a id="primitive-escape-coverage-boundary"></a>
## What this adds to aggregate coverage

L G0074 proved that the actual contribution of a fixed finite rational prime set has zero exponential rate for each fixed input, with input-dependent initial constants.
Equations (11)--(12) instead give a finite-time certificate entirely outside any supplied S, with a bound in terms of d, eta and |S|.
This avoids relying on an unspecified per-input time at which a fixed prime set stops accounting for norm growth.

For an individual input one may set eta=m.
For a family, a common eta would provide common time bounds of the displayed form, but its existence is not established here.
In particular the dependence on 1/eta does not exclude a hypothetical sequence m tending to zero.
The theorem does not confine the allowed divisor primes to a bounded set or interval; it proves escape from a forbidden finite set.
Except for such an explicitly forbidden set, a rational prime under a new ideal may have appeared at an earlier index through another ideal.
An outside-S certificate also does not exclude a positive inside-S certificate for the same input, at the same or a different exponent.
These are compatible lower bounds using different contributions to the cyclic norms.

The old-part bound (8) by itself is only an upper bound.
It cannot manufacture a lower bound for D_n or Prim_n.
The lower bound in (12) instead uses the separate finite prime-avoidance argument and the supplied entropy threshold.
No uniform lower bound for m, resolution of G0001, or degree-only all-index primitive-divisor theorem is inferred.
Any external such theorem inspected in parallel has its own source scope and is not used in this direct proof.


The complete original review account remains in [R23](../audits/reviews/Yin_R_G0023_v1.md#primitive-layer-review).
Its [whole](../audits/reviews/Yin_R_G0023_v1.md#primitive-layer-whole-finding) and [later targeted](../audits/reviews/Yin_R_G0023_v1.md#primitive-count-targeted-finding) findings retain their exact original inputs/scopes with actual finding-specific relationships.
