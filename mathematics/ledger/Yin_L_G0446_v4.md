---
author: Yin
---
# Arithmetic random matrices: joint cycle constraints and finite-window coefficient compatibility

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This 2026-11-05 continuation tests whether simultaneous arithmetic across cycle lengths and primes supplies the missing income for the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The main agent and the joint-cycle and terminal-prime contributors developed and checked the arguments below as ordinary author exploration.
They are not independently reviewed Claims or a whole-Task solution.
The earlier [orbit-count comparison](Yin_L_G0446_v1.md#positive-determinant-moments-and-orbit-count-integrality), [primitive-existence ceiling](Yin_L_G0446_v2.md#full-order-coverage-still-needs-mass-beyond-primitive-existence) and [minor propagation test](Yin_L_G0446_v3.md#scope-and-strategic-assessment) retain their separate scopes.

For an original monic irreducible noncyclotomic integer-unit polynomial P of degree d, write

    R_n(P)=|Res(P,x^n-1)|,
    D_n(P)=|Res(P,Phi_n)|,
    R_n(P)=product_(t|n) D_t(P).

All these numbers are positive integers.
The adopted [C867v2 terminal-mass conclusion](../claims/Yin_C_G0867_v2.md#terminal-clock-mass) says that a positive degree-normalized random-permutation mean, for bounded original measure, requires quadratic logarithmic mass at orders proportional to d.
Its exact mean is sum_(t<=d) (log D_t(P)/t) H_floor(d/t).
The present controls distinguish several weaker joint conditions from that original-input requirement.
They do not refute a near-one mass theorem.

<a id="slow-integral-cycle-control"></a>
## Slow abstract sequences with simultaneous integer cycle conditions

Fix an odd prime L, put q=L^2, and define

    R_n=1                         if L does not divide n,
    R_n=(q^(n/L)-1)^2             if L divides n.

These are abstract sequences, not asserted norm sequences of an algebraic unit.
For s_n(a)=1_(L divides n)*a^(n/L), one has s_(n+L)(a)=a*s_n(a) and R_n=1+s_n(q^2)-2s_n(q).
Thus the shift operator E satisfies

    (E-1)(E^L-q)(E^L-q^2)R=0.

This is a monic integer linear recurrence.
The multiplicative Mobius layers are positive integers, explicitly

    D_t=Phi_(t/L)(q)^2            if L divides t,
    D_t=1                        otherwise.

Indeed their product over divisors of Lm is product_(k|m) Phi_k(q)^2=(q^m-1)^2, while a nonmultiple of L has only unit layers.
The sequence even satisfies gcd(R_a,R_b)=R_gcd(a,b): if one index is not a multiple of L this follows from R=1 there, and otherwise it follows from gcd(q^a-1,q^b-1)=q^gcd(a,b)-1.

The additive orbit counts O_n=(1/n) sum_(e|n) mu(n/e)R_e are also nonnegative integers.
To check both assertions, let

    N_m(a)=(1/m) sum_(e|m) mu(m/e) a^e

be the number of primitive necklaces of length m on an a-letter alphabet.
Partitioning words by least period and then cyclic rotation proves this formula and its integer interpretation.
Direct Mobius inversion gives

    O_1=1,
    O_n=0                        if n>1 and L does not divide n,
    O_(Lm)=(N_m(q^2)-2N_m(q))/L.

Two disjoint q-letter alphabets fit in a q^2-letter alphabet, and their primitive necklaces remain disjoint and primitive, so the last numerator is nonnegative.
It remains to check divisibility by L.
Write m=L^v u with L not dividing u.
If v=0, the Mobius numerator for N_m(q) is divisible by L^2, and division by m does not remove that divisibility.
If v>=1, the numerator is

    sum_(e|u) mu(u/e) [q^(L^v e)-q^(L^(v-1) e)].

Every summand has L-adic valuation at least 2*L^(v-1)>=v+1.
After division by m, N_m(q) remains divisible by L.
The same argument applies to q^2=L^4, proving all the stated orbit-count integrality.

The growth assertion is precisely

    liminf_(n->infinity) log R_n/n=0,
    limsup_(n->infinity) log R_n/n=2 log(q)/L=4 log(L)/L.

The latter tends to zero as L tends through odd primes.
For each fixed L there is no full growth limit, since the two displayed subsequences have different limits.
This distinction is part of the control's scope.

The formal dynamic zeta function is

    zeta_R(z)=exp(sum_(n>=1) R_n z^n/n)
             =(1-z)^(-1)*[(1-q*z^L)^2/(1-q^2*z^L)]^(1/L),

where the root denotes the formal branch with constant term one.
Although this function is not rational, the further sequence S_n=L*R_n repairs that condition:

    zeta_S(z)=(1-q*z^L)^2/[(1-z)^L*(1-q^2*z^L)].

Multiplying by L preserves the integer recurrence, nonnegative integer orbit counts, strong gcd property and both growth limits.
Its multiplicative layers satisfy D'_1=L and D'_t=D_t for t>1, because sum_(e|t)mu(t/e)=0 for t>1.
Thus positive integer recurrence, positive integer multiplicative layers, realizable nonnegative orbit counts, strong gcd and rational dynamic zeta can coexist with arbitrarily small positive upper growth rate.

<a id="residue-degree-excludes-abstract-control"></a>
## The actual norm constraint already excludes this control at the first layer

The preceding list omits essential arithmetic.
Take L=5 and q=25, so R_1=1 and R_5=24^2, with v_3(R_5)=2.
If these were the actual absolute norms of alpha^n-1 for an algebraic integer unit alpha, every prime ideal above 3 dividing alpha^5-1 would have residue order exactly 5.
Order one is excluded by R_1=1.
For each such prime ideal, its residue degree f must satisfy 5 divides 3^f-1, hence 4 divides f.
Its contribution f*ord_(prime ideal)(alpha^5-1) to v_3(R_5) is therefore at least 4, contradicting v_3(R_5)=2.
The same argument applies to S_n=5R_n, since S_1=5 has no factor 3 and v_3(S_5)=2.
No good-prime or unramified hypothesis is needed for this contradiction.
The later identity v_3(R_(5*3^j))=2(1+j), obtained by the elementary odd-prime lifting formula, supplies an additional tail mismatch but is unnecessary.

Consequently the L=5 members fail the actual first-layer arithmetic of [C867](../claims/Yin_C_G0867_v1.md#statement), and the family has not supplied that arithmetic as an additional uniform property.
They cannot disprove a claim using that arithmetic together with the other global conditions.
They show why those global integer conditions cannot replace the residue-order and residue-degree information retained in the [actual local table](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers).

<a id="local-reciprocal-control-without-global-recurrence"></a>
## A complementary local reciprocal model without a global recurrence

An actual local matrix supplies the converse diagnostic.
On G=(Q_3/Z_3)^2 take A=diag(-4,-1/4) in SL_2(Z_3).
Its characteristic polynomial is x^2+(17/4)x+1, which is reciprocal and 3-adically integral but is not in Z[x].
Both diagonal entries act invertibly on G.
For a nonzero scalar b in Z_3, the kernel of multiplication by b on Q_3/Z_3 has size 3^v_3(b), by writing b as a power of 3 times a unit.
Thus the finite fixed-point counts are r_n=3^v_3(det(A^n-I)).
For odd n both eigenvalues have residue -1, giving r_n=1.
For n=2m one has

    det(A^(2m)-I)=-(16^m-1)^2/16^m,
    v_3(16^m-1)=1+v_3(m),
    r_(2m)=3^(2(1+v_3(m))).

The valuation identity follows by binomial expansion starting from 16-1=15, with multiplication by 3 increasing the valuation by one and a prime-to-3 exponent preserving it.
The complete multiplicative layers are D_t=9 for t=2*3^j, j>=0, and D_t=1 otherwise.
Their divisor products recover the displayed r_n directly.
These are actual split-quadratic local norms, with two residue-degree-one components of residue order two and total stable lift slope two.
There is no residue-degree mismatch of the preceding kind.

The nonnegative integer orbit counts are explicitly

    O_1=1,
    O_(2*3^j)=4*3^j              for j>=0,
    O_n=0                       otherwise.

For even n, their divisor sum is 1+sum_(j<=v_3(n/2)) (2*3^j)(4*3^j)=9^(1+v_3(n/2)), while for odd n it is one.
Since 1<=r_n<=max(1,9*n^2/4), this sequence has the full growth limit log(r_n)/n -> 0.
Thus all-depth local lifting and orbit-count integrality alone supply no exponential gap.

However, this sequence satisfies no eventual constant-coefficient linear recurrence, even with complex coefficients.
Suppose r_n=sum_(j=1)^D c_j*r_(n-j) held for all sufficiently large n.
Take N_k=2*3^k with k sufficiently large compared with the finitely many v_3(j/2) for even j<=D.
For odd j, both r_(N_k-j) and r_j equal one.
For even j, v_3(3^k-j/2)=v_3(j/2), so r_(N_k-j)=r_j again.
The entire right side at n=N_k is therefore independent of k, whereas r_(N_k)=3^(2(k+1)) is unbounded, a contradiction.

An actual global resultant sequence cannot have this defect.
For the integer companion matrix C, det(I-C^n)=sum_j (-1)^j tr((exterior^j C)^n) satisfies an integer constant-coefficient recurrence.
The sign needed to take its absolute value is a fixed sign times a parity sign, as is seen separately on real eigenvalues in (-infinity,-1), (-1,1) and (1,infinity), and on conjugate nonreal pairs.
It therefore preserves such a recurrence for noncyclotomic irreducible inputs.
The local model is not a global integer-polynomial norm sequence, and no common realization across all primes is asserted.
It shows that local norm compatibility cannot replace that global structure, just as the preceding slow sequences show that the stated global integer conditions cannot replace actual local compatibility.

<a id="rational-norms-do-not-have-strong-gcd"></a>
## Strong gcd is not an additional universal original-input hypothesis

Conversely, imposing strong gcd on actual norm integers would discard legitimate original polynomials.
Consider

    T(y)=y^2+y+13,
    P(x)=x^2*T(x+x^(-1))=x^4+x^3+15x^2+x+1.

The discriminant of T is -51, so T is irreducible over Q.
For a root theta, Norm_(Q(theta)/Q)(theta^2-4)=T(2)T(-2)=19*15=285 is not a rational square.
Thus theta^2-4 is not a square in Q(theta), and x^2-theta*x+1 is irreducible over that quadratic field.
It follows that P is irreducible of degree four.
Its trace roots are nonreal, whereas the trace zeta+zeta^(-1) of a root of unity is real, so P is noncyclotomic.

Evaluation on the relevant roots of unity gives

    R_1=P(1)=19,
    D_2=P(-1)=15,
    D_3=T(-1)^2=169,
    D_4=T(0)^2=169.

Hence R_3=19*169=3211 and R_4=19*15*169=48165, so

    gcd(R_3,R_4)=3211>19=R_gcd(3,4).

Modulo 13 the exact factorization is P=Phi_3*Phi_4=(x-3)(x-9)(x-5)(x-8).
The distinct inverse pairs have orders 3 and 4.
The common rational prime therefore comes from different local roots; taking norms loses the same-ideal gcd information.
This is a small explicit control for the existing ideal-versus-rational-prime distinction, not a near-one example or a new general norm theorem.

<a id="finite-window-irreducible-coefficient-control"></a>
## Finite terminal data can share actual irreducible integer coefficients

Fix an even integer d>=4 and put I={d/2+1,...,d}.
The accepted [Xyl11 Theorem 1.1](../audits/literature/Xyl11/Yin_U001.md#xyl11-u001), with a=1 and modulus d^2*r, supplies an absolute C>=1 and, for each r in I, a prime

    p_r=1 modulo d^2*r,
    p_r<=C*(d^2*r)^5.18<=C*d^15.54.

Let S={p_r:r in I}, allowing repeated choices of the same prime.
There exists an actual monic irreducible reciprocal P in Z[x] of degree d, constant coefficient one and m(P)>0, with

    v_p(D_n(P))=2                 if n in I and p=p_n,
    v_p(D_n(P))=0                 otherwise,

for every p in S and 1<=n<=d.
Every resultant in this statement is nonzero.
The construction below proves these assertions without a small-measure bound.

For p in S, let I_p={r in I:p_r=p} and k=|I_p|.
For each r in I_p choose an element a_r in F_p^* of exact order r, and include its inverse.
Such elements exist since r divides p-1.
Because r>=3, the two elements are distinct, and pairs with different orders are disjoint.
They use 2k<=d roots.
There are enough additional reciprocal pairs of orders exceeding d to complete the set to d distinct roots: at most sum_(n<=d) phi(n)<=d(d+1)/2 nonzero elements have order at most d, whereas p-1>=d^2*r>d^3/2.
For d>=4 the remaining set has more than d elements, is closed under inversion and has no inversion-fixed element.
Select (d-2k)/2 pairs from it.

For every designated order-r pair, lift a_r to beta_r in Z_p^* with v_p(beta_r^r-1)=1 and use its exact inverse as the other root.
This is possible because p>d>=r and the derivative of x^r-1 is nonzero at a_r: precisely one of the p lifts modulo p^2 solves x^r=1 modulo p^2, and any other lift has valuation exactly one.
Lift the supplementary pairs arbitrarily, again using exact inverses.
The product of the d/2 factors (x-beta)(x-beta^(-1)) is a monic reciprocal Q_p in Z_p[x], of degree d and constant coefficient one, with squarefree completely split reduction modulo p.
For n<=d, a root contributes to Phi_n precisely when its residue order is n.
At each designated order r, both roots have valuation exactly one in Phi_r, since all the other factors of beta_r^r-1=product_(j|r)Phi_j(beta_r) are p-adic units.
Supplementary roots contribute to none of these n.

Impose the reciprocal coefficient conditions

    P=Q_p modulo p^2             for every p in S,
    P=(x-1)^d+2x^(d/2) modulo 4.

All p in S are odd, so these conditions are compatible by ordinary coefficient CRT on the d/2 independent reciprocal coefficients.
Keep the leading and constant coefficients exactly one.
Evenness of d ensures that the prescribed polynomial modulo 4 is reciprocal with the same endpoint coefficients.
The congruence

    P(x+1)=x^d+2(x+1)^(d/2) modulo 4

makes every nonleading coefficient divisible by 2 and the constant coefficient equal to 2 modulo 4.
Eisenstein's criterion at 2 proves P irreducible.

To recover the exact valuations, congruence of resultants merely modulo p^2 would be insufficient.
Instead squarefree splitting gives d distinct Hensel roots of P in Z_p, each agreeing modulo p^2 with its prescribed root of Q_p.
The two designated roots therefore retain valuation exactly one in Phi_r, while all other relevant factors remain units.
Their product proves v_p(D_r(P))=2, as well as the zero valuations at other indicated orders.
This also proves that the full resultants for n<=d cannot be zero.

Put B=4*product_(p in S)p^2.
Changing P to P+A*B*x^(d/2), for integer A, preserves all these conditions including irreducibility.
Choose A so that the absolute central coefficient exceeds binomial(d,d/2).
The elementary symmetric formula bounds this coefficient by binomial(d,d/2) if every root has modulus at most one.
Thus the chosen polynomial has a root outside the unit disk and m(P)>0, so it is a noncyclotomic original integer-unit input.
No upper bound for its measure is asserted.

Define the captured part of the actual layer by

    D_n^S(P)=product_(p in S)p^v_p(D_n(P)).

It is exactly p_n^2 for n in I and one for 1<=n<=d outside I.
In particular

    sum_(r in I) log D_r^S(P)<=d*(log C+15.54 log d)=O(d log d),
    sum_(n<=d) (log D_n^S(P)/n)*H_floor(d/n)
      =sum_(r in I) 2 log(p_r)/r<=2 log C+31.08 log d.

The harmonic factor is one on I, so the last quantity is the complete captured contribution to the degree-d permutation mean.
This control simultaneously satisfies actual coefficient integrality, irreducibility, reciprocal pairing, the per-prime degree budget, squarefree splitting, lifting and primitive coverage at every terminal order.
It does not identify the full D_n(P) with its S-part.
Primes outside S, the complete terminal mass and any upper bound on m(P) remain uncontrolled.
In particular neither a bounded-measure nor a near-one counterexample follows.

<a id="joint-arithmetic-return-and-limits"></a>
## Remaining original-input requirement

If the same rational prime p supplies k distinct terminal orders r_i through degree-one inverse pairs, then lcm(r_1,...,r_k) divides p-1.
Those actual pairs yield total logarithmic mass at least 2k*log(lcm(r_1,...,r_k)+1).
This conditional strengthening follows directly from the local orders, but no argument here forces such clustering for a near-one original input.
The CRT control allows the selected orders to use distinct primes and keeps the captured mass below the quadratic scale even when some primes repeat.

These separate tests cannot be combined into an impossibility theorem for the intersection of all actual constraints.
The slow abstract family has not supplied actual residue-degree arithmetic and fails it already at L=5, the local reciprocal model lacks a global recurrence, and the finite-window integer-polynomial construction has no small-measure control.
A successful continuation must use a new link between the original small Mahler measure and the complete joint local data, forcing additional norm size, additional contributing primes or another fully paid source of mean income.
That missing link is not supplied by Dold congruences, rational dynamic zeta, finite coefficient CRT or primitive existence alone.
No uniform arithmetic lower bound and no separately supported new Strategy are adopted.

The only external theorem used in the finite-window construction is the exact already accepted Xyl11 least-prime bound.
The contributor directly reread the retained publisher statement on printed pages 65--66; its proof and numerical estimates were not re-audited.
All sequence, field-norm, congruence and lifting calculations needed here are given explicitly, without native numerical evidence or a new source-proof claim.
