---
author: Yin
---

# G0001: bounded base orders and the cost of deleting a cyclotomic block

The complete current mathematical home is [Yin_C_G0262_v2](../claims/Yin_C_G0262_v2.md#argument), adopted at 2026-10-21T06:39 after the [actual complete current self-check](../audits/reviews/Yin_R_G0532_v1.md#current-complete-unit-root-block-finding).
The original2026-10-07 mathematics and still-needed fixed review input below retain their original scope and date; this is no new research run.


Date: 2026-10-07.
Direct derivation by the assigned AI assess_shortness_route for Yin, with the coordinating AI independently identifying the whole-block divisibility step.
Authoring-agent self-review, complete coordinator review and separate assigned-agent review are complete at the scopes recorded below.

## Question, precise scope and result

The question is the existential bounded-order follow-up in [L G0040](Yin_L_G0040_v1.md#bounded-order-followup).
For each edge excess bound e, does every eligible irreducible reciprocal unit p with 1<M(p)<theta_0 and all-power degree preservation admit a positive primitive presentation of excess at most e whose neutral cyclotomic orders are bounded in terms of e, whenever some presentation of excess at most e exists?
A redundant presentation with high-order neutral factors does not disprove this assertion.

Let A be such a primitive nonnegative integer presentation, with chi_A(t)=t^z p(t)c(t), where c is a cyclotomic product and the unique noncyclotomic irreducible factor p occurs once.
Strip t^z and write

    q(t)=p(t)c(t)=sum_(i=1)^s a_i t^(n_i),

with distinct nonnegative exponents, nonzero integer coefficients and nonzero constant coefficient.
Edge excess means sum A_ij-dim A, counting edge multiplicity.
L G0034 gives s<=||q||_1<=2^(e+1).
The branch-return presentation of [L G0041](Yin_L_G0041_v1.md#branch-return-budget) has at most e states and coefficient mass at most 2e, but its delays are unbounded.
The arithmetic argument below applies to the resulting scalar polynomial; it supplies no deletion operation on that positive matrix.

For an integer k>=2, let P_k be the product of all primes at most k.
If Phi_m divides q, decompose q(zeta)=0, for a primitive m-th root zeta, into minimal nonempty vanishing subsums of the displayed monomials.
For each component I put

    g_I=gcd{n_i-n_j : i,j in I},
    g=gcd_I g_I,       b=m/gcd(m,g),
    ell=max_I |I|.

All these exponent gcds are positive.
Then

    b divides P_ell,             Phi_b(t^g) divides q(t).          (1)

Thus the original high-order factor belongs to an entire cyclotomic block with bounded base order.
The unbounded parameter is g.
If there is more than one component, ell<=s-2.
If the entire evaluation is minimal, the all-power hypothesis forces g=1, and consequently m divides P_s.

Deleting the block in (1) preserves Mahler measure and the noncyclotomic core, but it need not preserve a coefficient bound: an explicit family below has ||q||_1=6 and quotient length 2r+2.
No positive realization of the quotient at the same excess is proved.
These conclusions neither prove nor refute the existential bounded-order assertion.

<a id="mann-source-inspection"></a>
## Known-result identification and actual source access

The finite relative-order input is Mann's theorem.
The bounded primary search on 2026-10-07 used `Mann 1965 linear relations between roots of unity irreducible relation product primes k theorem pdf` and a targeted sparse polynomial / exponent-gcd query.
The primary publisher metadata is:

Henry B. Mann, *On linear relations between roots of unity*, Mathematika **12** (1965), no. 2, 107--117, [DOI 10.1112/S0025579300005210](https://doi.org/10.1112/S0025579300005210).
The publisher records first publication on 1 December 1965.
The attempted original PDF endpoint `https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/S0025579300005210` redirected in the web reader to the publisher abstract/metadata page `https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0025579300005210`.
No original PDF was obtained and Mann's original proof was not inspected.

The coordinator subsequently checked the publisher metadata and attempted the exact PDF endpoint with curl; it returned HTTP 403, zero bytes.
The Man65 acquisition failed.
The assigned AI assess_shortness_route for Yin inspected primary publisher metadata; the coordinator independently checked the title, author, journal volume, pages and print date against the Wiley and Cambridge records.
The DOI opener also failed, and no original theorem passage or original proof was obtained.
This metadata inspection adopts no source theorem, and known-result attribution does not turn the local proof below into an audit of Mann's original argument.
No exhaustive-public-access search is claimed.
The complete rational-coefficient argument needed here is supplied next, so no uninspected external theorem is a premise.
No classification result from the search leads is adopted, and no novelty claim is made.

<a id="minimal-vanishing-order"></a>
## A direct proof of the rational minimal-relation bound

Suppose

    sum_(i=1)^k c_i omega_i=0,

where c_i are nonzero rational numbers, the omega_i are roots of unity, and no nonempty proper subset of these k terms vanishes.
The roots need not be distinct.
Normalize omega_1=1 by dividing the relation by its first root.
Let M be the least common multiple of the orders of the normalized roots; equivalently M is the order of the finite cyclic group generated by all pairwise ratios.
We prove M divides P_k.

First suppose p^a exactly divides M with a>=2, and write M=p^a h with gcd(p,h)=1.
Choose a primitive p^a-th root eta.
Every omega_i has a representation eta^(u_i) xi_i, with xi_i an h-th root.
The field

    K=Q(zeta_h, eta^p)=Q(zeta_(M/p))

has [Q(zeta_M):K]=p by the cyclotomic degree formula.
Since eta satisfies X^p-eta^p over K, this polynomial is its minimal polynomial over K, and 1,eta,...,eta^(p-1) are K-linearly independent.
Grouping the terms by u_i modulo p therefore makes the sum in each occupied group separately zero.
Minimality allows only one occupied group.
The normalized term 1 is in the residue-zero group, so every u_i is divisible by p.
All the normalized roots then have order dividing M/p, contrary to the definition of M.
Thus M is square-free.

For a prime p dividing this square-free M, set h=M/p and K=Q(zeta_h).
Write omega_i=eta^(u_i)xi_i with eta a primitive p-th root, xi_i an h-th root, and 0<=u_i<p.
The extension Q(zeta_M)/K has degree p-1, including the case p=2.
The minimal polynomial of eta over K is consequently

    Phi_p(X)=1+X+...+X^(p-1).

For A_j=sum_(i:u_i=j) c_i xi_i, the relation says sum_(j=0)^(p-1) A_j eta^j=0.
Comparing degrees with Phi_p implies all A_j are equal.
If their common value were zero, each occupied group would itself vanish; minimality and the normalized term 1 would force every term into the residue-zero group, contradicting the occurrence of p in M.
Thus every A_j is nonzero and all p groups are occupied.
Hence p<=k.
Since M is square-free, this proves M divides P_k.

This proof uses only the elementary cyclotomic degree and irreducibility facts, and accommodates signs and arbitrary nonzero rational coefficients without expanding an integer coefficient into repeated unit terms.

## Support gcd and the all-power hypothesis

The all-power hypothesis means that for a root alpha of p,

    [Q(alpha^a):Q]=deg p for every integer a>=1.

Under the unique-core factorization q=pc above, it implies that the gcd of all exponent differences in the support of q is one.
Indeed q has a nonzero constant coefficient.
If this gcd were d>1, then q(t)=R(t^d) for an integer polynomial R.
For every d-th root of unity epsilon, epsilon alpha would also be a root of q.
It is noncyclotomic: otherwise alpha would be a root of unity.
Because p is the only noncyclotomic irreducible factor of q, all these distinct roots belong to p.
At least two conjugates therefore have the same d-th power, which makes the number of distinct conjugates of alpha^d smaller than deg p.
This contradicts the stated degree preservation.

The argument uses the unique noncyclotomic core and all-power condition; irreducibility of q is neither assumed nor available.
It does not claim that every exponent gcd attached to a proper subsum is one.

<a id="bounded-base-cyclotomic-block"></a>
## From minimal components to one entire cyclotomic block

Every finite vanishing sum can be partitioned into minimal nonempty vanishing subsums by successively removing a minimal vanishing subset.
There are no singleton components here.
For a component I, the group generated by ratios zeta^(n_i-n_j) has exact order

    d_I=m/gcd(m,g_I).

The direct minimal-relation theorem gives d_I divides P_(|I|).
The common gcd g satisfies

    m/gcd(m,g)=lcm_I [m/gcd(m,g_I)].

This identity follows prime by prime, or from the fact that the relevant ratio subgroups together generate the subgroup of order m/gcd(m,g).
Thus b divides the least common multiple of the P_(|I|), which is P_ell for ell=max_I |I|.
The maximum is essential; no minimum-size bound is asserted.

Let r_I be the least exponent in I.
Since g divides every internal exponent difference, its component polynomial has the form

    sum_(i in I) a_i t^(n_i)=t^(r_I) F_I(t^g),
    F_I in Z[t].

The vanishing evaluation says F_I(zeta^g)=0, and zeta^g has exact order b.
Hence Phi_b divides F_I in Z[t], using monic polynomial division and the minimal polynomial of a primitive b-th root.
Therefore Phi_b(t^g) divides each component polynomial and hence their sum q.
This proves (1).
Every root of Phi_b(t^g) is a root of unity, so this factor lies entirely in c; its deletion preserves the noncyclotomic core and Mahler measure.
It is monic, so the quotient is again integral.

If the partition has at least two components, each has size at most s-2.
If there is just one, g is the global support gcd, equal to one by the preceding argument, and b=m divides P_s.
For a bounded-excess sequence with unbounded cyclotomic orders, the nontrivial-component case is therefore eventually necessary and g must be unbounded: m divides P_ell g.

<a id="block-deletion-length-cost"></a>
## Exact coefficient-growth countercontrol for deleting the block

For integers N>=2 and r>=1 put x=t^N and

    q_(N,r)(t)=1+x+x^(3r+2)-t(1+x+x^2).

It has six distinct unit-coefficient monomials, so ||q_(N,r)||_1=6.
Its global support gcd is one because exponents 0 and 1 occur.
At a primitive 3N-th root zeta, x=zeta^N is a primitive cube root.
The displayed positive triple and negative triple both vanish and each is minimal: no pair of cube roots differs by the sign -1.
Their respective exponent gcds are N and N.
Thus the procedure above yields precisely g=N and b=3, and the forced block is Phi_3(t^N).

The exact division identity is

    q_(N,r)(t)/Phi_3(t^N)
       =1-t+sum_(j=0)^(r-1)
               [t^((3j+3)N)-t^((3j+2)N)].                         (2)

Indeed 1+x+x^(3r+2) equals Phi_3(x)+x^2(x^(3r)-1), and (x^(3r)-1)/Phi_3(x)=(x-1)sum_(j=0)^(r-1)x^(3j).
All exponents displayed on the right of (2) are distinct for N>=2, so its coefficient length is exactly 2r+2.
This diverges while the original length stays six.
Taking both N and r to infinity gives unbounded order and unbounded deletion cost for the exact block obtained from the minimal-component partition.

This control does not supply an eligible p or a positive graph.
It does not establish irreducibility, reciprocity, all-power degree preservation of the noncyclotomic factors, or M<theta_0.
It proves only that bounded scalar length and global support gcd one cannot justify a bounded-length block-deletion step.
In particular there is no claimed counterexample to the existential bounded-order conjecture.
The displayed identities are exact and need no numerical experiment.

## Remaining graph and arithmetic obligation

For bounded e, the conclusion reduces an arbitrarily large order to a bounded-base cyclotomic block, with at most 2^(e+1) scalar terms and a minimal-component partition.
It controls the shape of the neutral obstruction, not its removable cost.
The global period-one condition of a primitive graph concerns all closed-walk lengths; it does not directly bound the gcd of exponent differences inside each vanishing component.

To prove L G0040's conjecture by this route one still needs a theorem that, in its small reciprocal all-power scope, removes or replaces such blocks through positive presentations without increasing excess beyond the original e, until the remaining orders are uniformly bounded.
A coefficient estimate alone would still require a converse positive realization construction at that same excess.
Neither follows from Mann's theorem, from the support-gcd observation, or from L G0041's exact return presentation.
The explicit quotient growth rules out the naive unrestricted scalar-division justification, while leaving this stronger scope-specific positive reduction unresolved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0011_v1.md#review-boundary), with its original inspected scope and relationship.
