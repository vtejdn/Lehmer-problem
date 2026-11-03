---
author: Yin
---

# Inversion-matching class unions and the actual Salem splitting-field cost

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001/S_G0008 candidate written by assigned AI `entropy_status` for Yin.
Complete independent written review and fixed-ledger adoption are recorded below.
It is not a new uniform Mahler gap or a claim that a required small prime exists.

The directly reused interfaces are [L66](Yin_L_G0066_v1.md), [L74](Yin_L_G0074_v1.md#content-versus-ideal-norm), [L75](Yin_L_G0075_v1.md#chebotarev-period-cost), and [L160](Yin_L_G0160_v1.md#inversion-matched-frobenius-return).
The bounded reuse also checked L152 and L159; neither primitive-part existence nor a first-layer averaging estimate supplies the prime coverage used below.
No computation, prime scan, or Galois-group software run was performed.

<a id="actual-inversion-matching-average"></a>
## 1. The matching average in the actual reciprocal root action

Let P be a monic irreducible reciprocal noncyclotomic polynomial in Z[t], of degree d=2s>=4 and constant coefficient one.
Let Omega be its set of roots, L its splitting field inside C, and G=Gal(L/Q).
Inversion iota(rho)=rho^(-1) is a fixed-point-free involution of Omega commuting with G.
It has no fixed root because a root 1 or -1 would contradict irreducibility and the stated degree.
Define

    M(g)=#{rho in Omega : g(rho)=rho^(-1)}.                   (1)

This count is even: if rho is matched, then its inverse is matched as well.
It is also a class function, since inversion commutes with every element of G.
Transitivity of G on Omega implies that, for each rho, exactly |G|/d elements send rho to rho^(-1).
Double counting therefore gives

    (1/|G|) sum_(g in G) M(g)=1,
    |{g : M(g)>=a}|/|G|<=1/a   for every real a>0.           (2)

In particular the set A={g : M(g)>=s} has proportion at most 1/s=2/d.
Equation (2) concerns the actual finite Galois action.
It is not an assertion that primes in a finite range are uniformly distributed over G.
Nor is M(g) an upper bound on actual valuations: exceptional initial depths or other returning roots may add mass.

Let H be the image of G on the s unordered inverse pairs, and V its kernel.
Then H is transitive, and V embeds in F_2^s: a coordinate records whether the corresponding pair is flipped.
The conjugation action on V is the coordinate permutation induced by H.
In particular

    |G|=|V| |H|,                 s<=|H|<=s!.                (3)

If z_i=rho_i+rho_i^(-1) for one root from each pair, the z_i are distinct.
An automorphism fixes every z_i exactly when it fixes every pair.
Thus the fixed field of V is the splitting field of the trace polynomial from L66.
No splitting of the group extension is assumed or required.

One additional sufficient structural condition is available without a Salem hypothesis.
If V is nonzero, every coordinate projection V->F_2 is nonzero: the set of nonzero projections is a nonempty H-invariant subset of the transitive set of pairs.
Each coordinate is consequently one on exactly half of V, so the mean weight in V is s/2.
Some v in V has M(v)=2 wt(v)>=s.
This does not prove V nonzero for every reciprocal input, and supplies no bound for a prime realizing that element or a matching class.

<a id="salem-kernel-class-population"></a>
## 2. The actual Salem kernel and its complex-conjugation class

Now assume P is a Salem polynomial: its roots are tau>1, tau^(-1), and 2s-2 roots on the unit circle.
Complex conjugation c fixes the real pair and flips every other pair.
Hence c belongs to V and, if its fixed pair is i, its vector is

    v_i=1+e_i in F_2^s.                                     (4)

Here 1 is the all-one vector and e_i is the i-th coordinate vector.
Transitivity of H implies that all s vectors v_i are conjugate to c and belong to V.
Conversely every conjugate of c has this form.
The vectors are distinct, so its class has exactly s elements.

If s is even, sum_i v_i=1, and e_i=v_i+1 belongs to their span.
Thus V=F_2^s.
If s is odd, all v_i have even weight, and their differences v_i+v_j=e_i+e_j span the even-weight space E_s.
It follows that E_s<=V<=F_2^s, and the codimension-one property gives

    V=F_2^s                              if s is even;
    V=E_s or F_2^s                       if s is odd;
    [L:Q]=|V| |H|>=s 2^(s-1).                              (5)

For even s the last lower bound improves to s 2^s.
In particular the complex-conjugation class has exact proportion

    delta_c=s/(|V| |H|)<=2^(-(s-1)),                         (6)

with the stronger upper bound 2^(-s) for even s.
This is a bound on the class proportion and splitting-field degree of an actual Salem input, not a lower bound on its least matching prime.

The full/even kernel classification is known: Christopoulos and McKee, *Galois theory of Salem polynomials*, Math. Proc. Cambridge Philos. Soc. 148 (2010), 47--54, Proposition 2.3, pp. 4--5 of the [retained accepted manuscript](../literature/pdf/CM10.pdf), [DOI](https://doi.org/10.1017/S0305004109990284).
The coordinating AI acquired the seven-page accepted manuscript, read and visually checked its pp. 1--5, including Theorem 1.1 and the Section 2 proof, and retained its identity and reading scope in the [CM10 attribution note](../audits/literature/CM10/readme.md#cm10-salem-kernel-attribution).
This source reading supplies attribution and applicability checks; the short proof above is complete and does not use the source as an additional accepted premise.
The paper's separate splitting assertion is not used.
Neither the classification nor its elementary reconstruction is presented as a new classification result.

<a id="salem-many-matching-union"></a>
## 3. A larger conjugacy-invariant matching selector

Within the actual V of Section 2 put

    U={v in V : wt(v)>=ceil(s/2)}.                           (7)

Weight is preserved by conjugation in G, so U is a union of entire G-conjugacy classes.
Every element of U matches at least s=d/2 roots, and U contains the class of c because s-1>=ceil(s/2) for s>=2.
Thus U is contained in A from Section 1.

If V=F_2^s, pairing a vector with its complement gives |U|>=2^(s-1)=|V|/2.
If V=E_s, then s=2r+1 is odd and r>=1.
The even-weight binomial tail is exactly

    |U|=2^(s-2)+((-1)^(r+1)/2) binom(s-1,r)
       >=2^(s-3)=|V|/4.                                   (8)

For completeness, the unweighted upper half of the odd binomial sum is 2^(s-1), and Pascal's identity gives sum_(j=r+1)^s (-1)^j binom(s,j)=(-1)^(r+1)binom(s-1,r).
Taking half their sum proves the equality.
Also binom(2r,r)<=2^(2r-1): its ratio to 4^r equals 1/2 at r=1 and decreases under r->r+1 by the factor (2r+1)/(2r+2).
This proves the inequality including all small odd s.

Consequently the exact group proportions satisfy

    delta_U=|U|/(|V| |H|)>=1/(4|H|),
    delta_U>=1/(2|H|)                       if V=F_2^s,
    delta_U<=delta_A<=1/s.                                  (9)

Relative to selecting only the class of c, the exact gain in group population is delta_U/delta_c=|U|/s.
It is at least 2^(s-3)/s in general, and at least 2^(s-1)/s when V is full.
These lower bounds express the possible exponential improvement of this selector over the single class; they do not assert a strict improvement in every small degree.

These are proved proportions inside the finite group G.
No prime-density theorem is needed or newly adopted in this argument, and no effective bound for the first prime in U or A follows from these counts.
The order |H| may still be large, and (2) bounds even A's group proportion by 2/d.
The full splitting field L and its discriminant remain the inputs to a least-prime result that requires them, at L75's existing effective-cost scope.

<a id="matching-union-local-cost"></a>
## 4. The exact local certificate and every small-prime case

Return temporarily to any P satisfying Section 1.
Write m=log M(P)>0, K=Q(alpha), and C_n=|Norm_(K/Q)(alpha^n-1)|.
Let p be any rational prime unramified in L whose Frobenius class contains g with u=M(g) matched roots.
At a prime Q of O_L over p, Frob_Q(rho)=rho^p modulo Q and v_Q(p)=1.
Each matched root then satisfies v_Q(rho^(p+1)-1)>=1.
The product over the original d roots is the integer signed norm in K.
All other valuations are nonnegative, and its v_Q equals its rational v_p.
Therefore, with precisely the L160 accounting,

    v_p(C_(p+1))>=u,
    v_p(C_((p+1)p^r))>=(r+1)u               for r>=0,
    m>=[(r+1)u log p-d log 2]/[(p+1)p^r].                  (10)

The second line follows by the binomial expansion: if v_Q(x-1)=a>=1 then v_Q(x^p-1)>=min(a+1,pa)>=a+1.
The final line uses C_n<=2^d M(P)^n.
It remains valid for primes dividing the power-basis discriminant when they are unramified in L; no good-polynomial-prime restriction is added.
It is a lower bound for actual valuations, not an exact-order claim or an upper bound on their initial depth.

For any class of degree d>=4 inputs satisfying Section 1, suppose there is a common B>0 such that each input has an unramified prime p whose Frobenius lies in A and satisfies

    p<=B d log p.                                          (11)

Then u>=d/2.
For p=2 use r=2 in (10), and for p=3 use r=1.
Both exponents equal 12, and respectively

    m>=d log 2/24>=log 2/6,
    m>=d log(3/2)/12>=log(3/2)/3.                           (12)

For p>=5 use r=0 and put a_0=1/2-log 2/log 5>0.
Since p+1<=6p/5, equations (10)--(11) give

    m>=a_0 d log p/(p+1)>=5a_0/(6B),
    m>=min{log 2/6,log(3/2)/3,5a_0/(6B)}>0.                (13)

Thus the identical L160 uniform constant follows from the weaker matching-set hypothesis (11).
In particular it suffices to find such a prime in U for a Salem input, instead of the one class of complex conjugation.
For general reciprocal inputs, A may be empty without further information; the nonzero-kernel observation in Section 1 is only a sufficient condition for nonemptiness.
No claim of the degree-uniform prime coverage (11) is made, and no reduction of unrestricted G0001 to Salem inputs is used.

<a id="actual-quartic-matching-population"></a>
## 5. One actual quartic and the remaining transfer boundary

Use the retained irreducible Salem polynomial P_4(t)=t^4-t^3-t^2-t+1 from L8 and L160 Section 4.
Here s=2, so transitivity forces |H|=2 and Section 2 gives |V|=4.
Hence the actual splitting field has degree eight, and

    |class(c)|=2,       delta_c=1/4,
    |U|=3,              delta_U=3/8.                       (14)

In this case A=U.
Indeed an element outside V exchanges the two pairs and cannot match any root with its inverse.
The three nonzero elements of V match respectively two, two, and four roots.
Their total matching count is eight, in agreement with the exact average one over the eight elements of G.
This is a deduction about an already retained actual input, not a new Galois-group computation or an abstract group proposed as a near-one counterexample.
Its Mahler measure is fixed above one.

The selector U addresses a real avoidable restriction of the single-class method: many other actual classes supply the same local positive threshold.
Nevertheless it leaves a definite unfilled input.
One needs an effective prime bound for this larger matching set at the scale p<=B d log p, with a common B, or an alternative direct arithmetic certificate with its full cost.
The known exponentially large lower bound for [L:Q] and the upper bound delta_A<=2/d prevent replacing these field/class parameters by a degree-independent positive group proportion.
Neither fact proves that small useful primes fail to exist.
A standard bound too large to establish (11) is still only a failure of that sufficient certificate, not a lower bound on the least prime and not a Mahler exclusion.

## Contribution and current review scope

The coordinating AI proposed the actual Salem conjugates v_i, their full/even span, the exact size of class(c), and its splitting-field cost, and identified the known CM10 attribution.
The assigned AI `entropy_status` checked those arguments and derived the exact average (2), the nonzero-kernel observation, the larger union with its counts (7)--(9), the transfer of all small-prime constants (10)--(13), and the quartic population (14).
The local valuation proof and small-prime device themselves are fixed L160 interfaces, not claimed as new here.
The contributor checks were followed by the complete independent written review recorded below.
Review of a reused interface was not substituted for review of this full proof.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0061_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
