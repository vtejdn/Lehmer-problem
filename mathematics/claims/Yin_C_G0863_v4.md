---
author: Yin
---
# Four-pair torus bounds in dimension at least two and an explicit finite circle reduction

Human author Yin.
This version advances the four-pair good-sign problem within the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The rank_two_route contributor developed the coordinate-projection envelope, exact pair-transform calculation and complete new proof below.
Root clarified the finite-circle assembly and the distinction between a candidate finite remainder and an actual counterexample.
These are proof contributions, not independent review.

## Revision scope and inputs

On 2026-11-04, this version retains the complete [v3 theorem](Yin_C_G0863_v3.md#statement) and replaces its unresolved general rank-two Haar inequality by a universal bound in every dimension at least two.
The remaining circle question is reduced to an explicitly enumerable finite set, with a primitive frequency bound128^3.
The exact inherited dependency is [v3's selected decision](Yin_C_G0863_v3.md#decision-whole-independent-review-2026-11-04), supported by [R1083](../audits/reviews/Yin_R_G1083_v1.md#whole-version-and-effective-certificate), including its inherited source/native limits.
That review does not inspect the new Fourier-envelope proof or computation in this version.
The selected assessment and this version's separate independent review are recorded in its decision below.

| Input | Adopted scope |
| --- | --- |
| [C863 v3](Yin_C_G0863_v3.md#decision-whole-independent-review-2026-11-04) | All five unchanged conclusions; normalized Haar/Laurent integrability, finite logarithm certificates, saturated sign-average locality, and the exact inherited v2/v1/source/native boundaries. |
| [Exact Fourier-envelope program](../computations/programs/Yin_J_G0134/rank-two-fourier-envelope.py) | Complete common-denominator coefficient construction, canonical finite enumeration, projected maxima and strict rational comparison, with direct small controls. |
| [Selected Fourier-envelope certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-fourier-envelope.json) | Order128, all550775 canonical admissible Fourier classes, the4158 nonzero projected-envelope rows, exact free/envelope numerators, common denominator and positive comparison at71/25. |

The new argument uses the existing finite logarithm and Fourier framework with elementary linear algebra and finite coefficient calculations.
No new external theorem, quadrature, original-source proof inspection or priority claim is made.
No rolling Draft or ignored output file is a proof premise.

## Statement

Let K be the same space of connected subtori H of T^4 whose four restricted coordinate characters chi_j are nontrivial and distinct up to inversion.
Put

    L(H)={a in Z^4:product_j chi_j^(a_j)=1},
    F_epsilon=sum_(j=1..4)epsilon_j(chi_j-chi_j^(-1)),
    G_epsilon=F_epsilon/i,
    g(H)=min_(epsilon in {+1,-1}^4) integral_H log|F_epsilon|,
    P_N(u)=sum_(j=1..N)(1-u^2/64)^j/j,
    Sbar_N(H)=(1/16)sum_epsilon integral_H P_N(G_epsilon),
    B_N={a in Z^4:||a||_1<=N},
    eta_2=127/4050.

The annihilator L(H) is saturated and contains none of e_j or e_i+/-e_j for i different from j.
All integrals use normalized Haar measure and natural logarithms, and every F_epsilon is nonzero and logarithmically integrable.
The conclusions are as follows.

1. All five conclusions of [v3](Yin_C_G0863_v3.md#statement) remain valid with their actual constants, quantifiers and evidence limits.
2. Every H in K with dim H>=2 satisfies

       Sbar_128(H)>71/25,
       g(H)<33/50<log2-eta_2.                           (S1)

   This is existence of a favorable sign; no bound for every individual sign is asserted.
3. The same bound (S1) holds in every rank whenever span_Q(L(H) intersect B_128) has dimension at most two.
4. Enumerate independent triples u,v,w in B_128 and take the distinct admissible circles whose annihilator is span_Q(u,v,w) intersect Z^4.
   This is an explicit finite candidate set E.
   Every admissible circle outside E satisfies (S1).
   One may discard any member of E whose exact Sbar_128 already exceeds71/25 without changing this conclusion.
   Every member of E has a primitive integer frequency representative with all four absolute values at most128^3=2097152.
   In particular every tuple of distinct positive integer frequencies, after division by its common gcd, whose largest entry exceeds2097152 has a sign with the strict margin in (S1).

The finite candidate-circle enumeration has not been performed and does not certify that any remaining circle fails the good-sign inequality.
The general rank-two Haar problem is resolved at the stated scope, while the finite remaining rank-one checks and arbitrary original-input auxiliary supply remain unresolved.
No same-margin assertion for every circle inside an arbitrary good rank-two host is inferred from its host's Haar bound.

<a id="inherited-arguments"></a>
## Exact inherited scope and logarithm interface

Part1 invokes the complete [v3 selected theorem](Yin_C_G0863_v3.md#decision-whole-independent-review-2026-11-04), whose arguments, computations and reviews remain at their responsible fixed homes.
For the new proof, its [finite logarithm argument](Yin_C_G0863_v3.md#finite-moment-locality) gives

    integral_H log|F_epsilon|
      <=1/2[log64-integral_H P_N(G_epsilon)].           (FE1)

Its saturation argument also proves that Sbar_N(H) depends exactly on L(H) intersect B_N.
That locality proof is restated below where used, without changing any hypothesis.
The elementary bounds56/81<log2<52/75 from the same inherited argument imply log64<104/25.
Thus Sbar_128(H)>71/25 yields a sign whose integral of P_128 is greater than71/25, and (FE1) gives

    g(H)<1/2(104/25-71/25)=33/50,
    56/81-33/50=127/4050.                              (FE2)

The task is therefore the exact uniform certificate Sbar_128(H)>71/25 for rank L(H)<=2.

<a id="ambient-even-fourier-polynomial"></a>
## Ambient even Fourier coefficients

On T^4 define

    Q_N(theta)=(1/16)sum_epsilon
                 P_N(2sum_j epsilon_j sin(theta_j)).

Sign averaging kills every Fourier exponent with an odd coordinate.
Indeed changing epsilon_j is the ambient translation theta_j -> theta_j+pi, whose effect on the coefficient at exponent b is multiplication by (-1)^(b_j).
This uses ambient translations only; it does not assume that the same translations belong to H.
Since P_N has degree2N, write the resulting finite Fourier expansion as

    Q_N(theta)=sum_(a in B_N) q_N(a) exp(2i<a,theta>).   (FE3)

Permuting theta coordinates or inverting any one of them preserves the sign-averaged function.
Consequently q_N(a) is unchanged by coordinate permutations and independent sign changes of the entries of a.
The function is real and even, so these coefficients are real; the exact formulas below show they are rational.
In particular q_N(0)=S_N(T^4), the free-torus finite logarithm sum.

On an admissible connected H, integration of the term in (FE3) keeps it exactly when2a belongs to L(H).
Saturation makes this equivalent to a in L(H), giving

    Sbar_N(H)=sum_(a in L(H) intersect B_N)q_N(a).      (FE4)

For nonzero a in L(H), saturation and admissibility exclude every multiple of e_j or e_i+/-e_j.
In canonical sorted absolute coordinates, the excluded shapes are exactly

    (0,0,0,d), d>=1,
    (0,0,c,c), c>=1.                                  (FE5)

There is no primitive-vector restriction on the remaining Fourier exponents: every allowed multiple is retained in the calculation.
Other canonical shapes may or may not occur in a particular lattice; allowing all of them makes a valid upper bound on the negative contribution.

<a id="two-coordinate-projection-envelope"></a>
## An injective coordinate pair bounds every rank-two relation lattice

If a rational subspace V of Q^4 has dimension at most two, there are two coordinate positions whose joint projection is injective on V.
For dimension two, choose a basis and a nonzero2-by-2 minor of its4-by-2 coordinate matrix.
For dimension one, choose a nonzero coordinate of a generator and any distinct second position; the zero-dimensional case is immediate.
Apply this to V=span_Q L(H) when rank L(H)<=2.
By the coefficient symmetry in (FE3), the envelope bound is the same whichever pair of positions is chosen, so take them to be the first two.
For each projected integer pair (x,y), at most one vector a in L(H) has those first two coordinates.
For (x,y)=(0,0), injectivity permits only a=0.

For 0<=x<=y with (x,y)!=(0,0), define e_N(x,y) as the maximum of zero and all values -q_N(a) satisfying these conditions:

- a is a nonzero vector in B_N outside the forbidden shapes (FE5);
- some pair of its absolute coordinate entries is x,y.

Symmetry makes this the maximum possible negative coefficient for any fixed ordered signed projected pair with unordered absolute values x,y.
The number of those ordered signed pairs is

    mu(x,y)=4  if x=0<y or 0<x=y,
             8  if 0<x<y.                             (FE6)

Put

    E_N=sum_(0<=x<=y, (x,y)!=(0,0))mu(x,y)e_N(x,y).    (FE7)

This sum is finite, since x+y<=N whenever e_N is nonzero.
Dropping all nonnegative terms in (FE4), then using projection injectivity and (FE6), proves the universal inequality

    Sbar_N(H)>=q_N(0)-E_N  whenever rank L(H)<=2.       (FE8)

It does not assume that all envelope-maximizing vectors can occur simultaneously in one lattice.
Nor does it require enumeration or classification of the relation lattices themselves.
The exact calculation below proves q_128(0)-E_128>71/25, completing the general rank-two step.

<a id="exact-pair-transform"></a>
## Exact common-denominator pair transforms

For N>=1, finite binomial expansion and the identity binom(j,k)/j=binom(j-1,k-1)/k give

    P_N(u)=h_N+sum_(k=1..N)
                    (-1)^k binom(N,k)u^(2k)/(k*64^k),
    h_N=sum_(j=1..N)1/j.                              (PT1)

Indeed sum_(j=k..N)binom(j-1,k-1)=binom(N,k), by partitioning the k-element subsets of {1,...,N} according to their largest element.
Put

    Lambda=lcm(1,...,N), D=Lambda*64^N,
    w_0=64^N sum_(j=1..N)Lambda/j,
    w_k=(-1)^k binom(N,k)(Lambda/k)64^(N-k), k>=1.      (PT2)

These are integers.
Let A_n(v) be the coefficient of z^v in [sum_j(z_j+z_j^(-1))]^n.
A length2k sine walk ending at2a has phase (-1)^(sum_j a_j) times its positive cosine-walk count: multiplying -i for every positive step and i for every negative step gives this phase.
It follows that

    D*q_N(a)=(-1)^(sum_j a_j)
                  sum_(k=0..N)w_k A_(2k)(2a).         (PT3)

Here A_0(2a) is one when a=0 and zero otherwise, so the k=0 term supplies exactly the constant h_N.

For nonnegative r,s define

    B_l(r,s)=binom(2l,l+r+s)binom(2l,l+r-s),            (PT4)

using zero for an out-of-range index.
In particular B_l(r,s)=0 when l<r+s.
The coordinate change (u,v)->(u+v,u-v) turns a walk step in a coordinate pair into two independent signs.
Thus B_l(r,s) counts the pair walks of length2l ending at(2r,2s).
Splitting the4-coordinate walk between its first and second coordinate pairs yields

    A_(2k)(2a)=sum_(l+m=k)binom(2k,2l)
               B_l(a_1,a_2)B_m(a_3,a_4).              (PT5)

Equations (PT3)--(PT5) give an integer matrix kernel and its pair transforms:

    K_(l,m)=w_(l+m)binom(2(l+m),2l), l+m<=N,
    T_l(c,d)=sum_(m=c+d..N-l)K_(l,m)B_m(c,d),
    n(a,b,c,d)=(-1)^(a+b+c+d)
          sum_(l=a+b..N-c-d)B_l(a,b)T_l(c,d).          (PT6)

The integer n(a,b,c,d) is exactly D*q_N(a,b,c,d).
The common denominator permits every negative-envelope maximum and every final comparison to be computed using integers alone.
The precomputed pair transforms accelerate this exact finite sum; no truncation or approximation is introduced.

<a id="complete-finite-envelope-certificate"></a>
## Complete order128 envelope and native evidence

The [native program](../computations/programs/Yin_J_G0134/rank-two-fourier-envelope.py) computes (PT2), (PT4) and (PT6) at N=128.
It then enumerates every canonical nonnegative sorted quadruple

    0<=a<=b<=c<=d, a+b+c+d<=128,                       (EC1)

excluding the origin and precisely the forbidden shapes (FE5).
The four nested loop bounds are

    a<=floor(N/4),
    b<=floor((N-a)/3),
    c<=floor((N-a-b)/2),
    c<=d<=N-a-b-c,

with the lower bounds a<=b and b<=c retained.
These bounds include each quadruple in (EC1) exactly once.
They neither impose primitivity nor discard repeated coordinates other than the forbidden equal-support-two shape.

For a second exact count, put (a,b,c,d)=(a,a+x,a+x+y,a+x+y+z).
The number of sorted nonnegative quadruples of weight at most N is

    sum_(a=0..floor(N/4))
    sum_(x=0..floor((N-4a)/3))
    sum_(y=0..floor((N-4a-3x)/2))(N-4a-3x-2y+1).

At N=128 this is550968.
Removing the origin,128 nonzero support-one shapes and64 equal-support-two shapes leaves exactly550775 canonical admissible classes.
The program checks this independent integer count against its actual enumeration.

For each class with n(a,b,c,d)<0, the program considers every distinct unordered coordinate pair among its six pair choices.
It excludes (0,0) and updates the maximum negative numerator for that projected absolute pair.
Thus every envelope value in (FE7) is computed over the complete canonical support, including large frequencies through the exact boundary128.
There is no unestimated Fourier tail.
The actual run found232646 negative canonical classes and4158 nonzero projected-envelope rows.

Let f be the computed free numerator n(0,0,0,0), and let e be the integer weighted sum of envelope numerators using (FE6).
The [selected native certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-fourier-envelope.json) retains N,D,f,e, all4158 exact maximum/witness/multiplicity rows, the full finite scope and the positive comparison integer

    25(f-e)-71D>0.                                    (EC2)

Consequently

    q_128(0)-E_128=(f-e)/D>71/25.                      (EC3)

Exact integer division also gives the optional rational displays

    114488225296/10^12<=E_128<114488225297/10^12,
    2842086038655/10^12<=(f-e)/D<2842086038656/10^12.    (EC4)

These displays are not premises replacing (EC2).
A witness row alone proves attainment of its displayed value; maximality is supplied by the complete enumeration and must be checked at that full scope.
Likewise the short controls below do not replace the order128 computation.

### Author controls and reproduction

For each N from1 through5, the program directly expands the integer antisymmetric Laurent polynomial sum_j(z_j-z_j^(-1)).
At even degree2k it deletes odd endpoint coordinates to average signs, and uses G^(2k)=(-1)^k F^(2k).
Combined with (PT1), this checks all43 canonical coefficients across those degrees against the pair-transform formula, including the constant and zero-coordinate cases.
This direct expansion does not use (PT4)--(PT6).
At N=128 the independently retained free-torus fraction in the previous selected moment certificate agrees exactly with the new f/D; this was an additional author comparison, not a new old-certificate run or a premise of the new envelope bound.

The calculation used CPython3.13.15 and only its standard library.
All evidence arithmetic uses integers; Fraction and floating-point formatting appear only in the final human-readable diagnostic display.
The selected certificate was generated and then fully recomputed and matched using

    python mathematics/computations/programs/Yin_J_G0134/rank-two-fourier-envelope.py --verify-certificate

The generation and reproduction both covered all550775 classes and all4158 maximum rows.
These are author calculation checks, not an independent review of the new theorem.
No quadrature or ignored output is used.

Combining (FE8), (EC3) and (FE2) proves Part2 for every admissible torus of dimension at least two.
The proof includes all genuine rank-two configurations, with no common-phase, coloop, deletion-index, coefficient-bound or special-family condition.

<a id="explicit-finite-circle-reduction"></a>
## The actual circle question reduces to a finite bounded set

For any H in K, put W=span_Q(L(H) intersect B_128) and L'=W intersect Z^4.
Because L(H) is saturated, L' is a saturated sublattice of L(H).
Its annihilator H' is an admissible connected torus containing H: a forbidden relation in L' would also lie in L(H).
Furthermore

    L' intersect B_128=L(H) intersect B_128.           (CR1)

One inclusion uses L' subset L(H), and the other follows because every short member of L(H) belongs to W by definition.
By (FE3)--(FE4), or the inherited sign-average locality, (CR1) gives

    Sbar_128(H')=Sbar_128(H).                           (CR2)

If dim W<=2, then dim H'>=2, so Part2 and (CR2) prove Part3.
This transfers an exact finite polynomial certificate and does not infer logarithmic monotonicity under torus restriction.

Now let H have dimension one.
If dim W<=2, Part3 already supplies its good sign.
Otherwise W has dimension three, and three independent vectors u,v,w in L(H) intersect B_128 span the rational space of L(H).
Saturation gives

    L(H)=span_Q(u,v,w) intersect Z^4.                  (CR3)

Thus H belongs to the finite triple enumeration in Part4.
The exact rational span, saturation, character exclusions and duplicate tests are finite integer/rational operations, so this is an effective enumeration specification.
It has not been executed here.

For a rank-three matrix with rows u,v,w, its signed3-by-3 minors give a nonzero integer vector orthogonal to all rows.
Dividing by the common gcd gives a primitive integer frequency vector for the connected circle in (CR3).
Every minor has absolute value at most ||u||_1||v||_1||w||_1<=128^3: expand the determinant, and bound the sum of absolute terms by the product of the three row sums.
This proves the stated bound2097152.
Inverting and permuting coordinates replaces the primitive entries by their sorted positive absolute values and preserves the minimum over signs.
Admissibility ensures those values are nonzero and distinct.
Therefore a primitive positive tuple whose largest entry exceeds that bound cannot lie in the finite candidate set and satisfies Part3.
A common integer scaling of the frequencies does not change the circle or its Haar logarithmic means.

## Remaining original-task boundary

The new theorem settles the four-pair Haar sign inequality for every admissible torus of dimension at least two.
It does not settle the actual finite remaining circle configurations or provide the original-field integral auxiliary for every arbitrary near-one minimal polynomial.
The [binary reflection inquiry](../drafts/Yin_D_G0013.md#binary-reflection-reduction) and [original-input confinement theorem](Yin_C_G0864_v1.md#statement) retain their own exact arithmetic hypotheses and unresolved supply condition.
No completion of unrestricted G0001 follows from this analytic theorem alone.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:54 |
| status | proved |
| reason | Adopt the complete four-part v4 theorem after independent R1083 v2: the exact Fourier projection envelope covers every admissible torus of dimension at least two, with a bounded finite remainder of actual circles. The full 550775-class and 4158-row computation was independently reproduced. Remaining circle inequalities and arbitrary original-input auxiliary supply are not asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact v4 statement](#statement) | All four conclusions, inherited v3 theorem, universal dimension-at-least-two bound, short-relation transfer and exact finite primitive-frequency scope. |
| argument | [Complete assembled proof](#inherited-arguments) | Entire FE, PT, EC and CR argument, including the full coefficient envelope and original-task limits. |
| dependency | [Adopted v3 theorem](Yin_C_G0863_v3.md#decision-whole-independent-review-2026-11-04) | All five unchanged conclusions, finite logarithm and saturated sign-average locality, with inherited source/native/review boundaries. |
| dependency | [Exact envelope program](../computations/programs/Yin_J_G0134/rank-two-fourier-envelope.py) | Full integer coefficient and envelope construction, complete finite ranges, controls and reconstruction procedure. |
| dependency | [Selected envelope certificate](../computations/programs/Yin_J_G0134/inputs/rank-two-fourier-envelope.json) | All550775 canonical classes and4158 projected maxima at order128, with exact positive comparison at71/25, independently recomputed. |
| review | [Independent whole-v4 finding](../audits/reviews/Yin_R_G1083_v2.md#whole-v4-and-complete-fourier-envelope) | Complete statement, argument and native premise at the actual new scope; prior v3 review remains distinct, with no new order4096 run or original-source proof audit. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
