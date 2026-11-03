---
author: Yin
---

# Nondegenerate relation blocks and uniform additive-energy moments

Date: 2026-10-07.
Bounded direct derivation by the assigned AI assess_shortness_route for Yin, within G0001.
The coordinator proposed the block-counting question and the direct original-torus collision application.
The nondegenerate-equation theorem used below is an explicitly scoped external statement; its proof is not reproduced here.
No computation or claim of a uniform entropy gap is part of this note.

<a id="nondegenerate-energy-setting"></a>
## The exact conditional input

Let alpha be a nonzero nontorsion algebraic number.
For integers n,r>=1 put

    A_(n,r)=#{(i_1,...,i_r,j_1,...,j_r) in {0,...,n-1}^(2r):
                  sum_l alpha^(i_l)=sum_l alpha^(j_l)}.

This is the original additive energy in [L G0084](Yin_L_G0084_v1.md#faithful-high-moment-arithmetic-interface).
The combinatorial argument does not require alpha to be a unit.
The later torus application is stated on the algebraic-unit domain of that record.

For k>=2 fix an ordered sign vector epsilon in {+1,-1}^k.
A relation sum_(j=1)^k epsilon_j alpha^(e_j)=0, with integer exponents, is nondegenerate when no nonempty proper subset of its k labelled terms sums to zero.
Repeated exponents are permitted.
Two exponent vectors have the same normalized shape if they differ by adding a common integer to every coordinate.

Assume that, for each k and each fixed sign vector, the number of these shapes is at most B_k, uniformly over the alpha under consideration.
We may take B_2=1: an opposite-sign two-term relation forces equal exponents, whereas a same-sign two-term relation would make a power of alpha equal to -1, contrary to nontorsion.
There is no one-term zero relation.

To match this input with a nondegenerate-equation theorem, divide by -epsilon_k alpha^(e_k).
The equation becomes

    sum_(j<k) a_j x_j=1,
    a_j=-epsilon_j/epsilon_k,
    x_j=alpha^(e_j-e_k).                                  (1)

The ambient tuple group is <alpha>^(k-1), of rank k-1, not rank one.
Its coordinate generators are independent because alpha has infinite multiplicative order.
An exponent-difference tuple determines exactly one normalized shape.
Nondegeneracy in (1) is equivalent to the stated condition on the original relation: a zero subset containing the last term has a complementary zero subset not containing it.
No distinct-coordinate hypothesis or extra factor 2^k is used; the signs are fixed before counting.

<a id="uniform-fixed-moment-energy"></a>
## Explicit main term and error for arbitrary shape bounds

For r>=2 define

    B_*(r)=max(1,B_3,...,B_(2r)),
    D_r=(2r)^(2r) B_*(r)^(r-1),
    D_1=0.                                               (2)

Then for every n>=1, uniformly in alpha within the hypothesis,

    r! (n)_r <= A_(n,r) <= r! n^r+D_r n^(r-1),
    |A_(n,r)-r! n^r| <= D_r n^(r-1).                      (3)

Here (n)_r counts ordered r-tuples of distinct elements of an n-element set, so it is zero when r>n.
In particular, for fixed r the energy is r! n^r+O_r(n^(r-1)), with the displayed uniform constant.
The statement is exact A_(n,1)=n when r=1.

First separate the diagonal relations, in which the two labelled r-tuples have the same multiset of exponents.
Their number is

    Delta_(n,r)=sum_(m_0+...+m_(n-1)=r)
                      (r!/(m_0!...m_(n-1)!))^2.          (4)

For each left tuple the number of right permutations is at most r!, and is exactly r! when its exponents are distinct.
Thus

    r! (n)_r <= Delta_(n,r) <= r! n^r,
    0<=r! n^r-Delta_(n,r)
          <=r! binom(r,2) n^(r-1).                      (5)

The last bound follows by a union bound over pairs of equal coordinates in a left tuple.
It remains valid for n<r.
Formula (4), rather than counting every pairing as distinct, accounts for repeated exponents and the lower-degree diagonal correction.

Now view each energy relation as 2r labelled signed terms, with r prescribed positive and r prescribed negative signs.
Repeatedly extract an inclusion-minimal nonempty zero subset.
Its complement is again a zero relation until it is empty.
This produces a partition into nondegenerate zero blocks.
Each block has at least two terms.
A two-term block consists of opposite signs at equal exponents.
Therefore a partition with r blocks is entirely made of such pairs and gives a diagonal relation.
Every non-diagonal relation has, in any such partition, at most r-1 blocks.

The signs within an individual block need not balance.
For example, alpha^2-alpha-1=0 can be a nondegenerate three-term block.
Only the full relation has r terms of each sign.
Keeping the labelled terms also allows same-sign repetitions within a block; opposite-sign repetitions in a larger nondegenerate block would already give a proper two-term zero subset.

Fix one partition with b<=r-1 blocks.
In a block of size k, choose its last labelled coordinate as the normalizing exponent.
For each of its at most B_k shapes, there are at most n possible common translations putting every exponent in {0,...,n-1}: the chosen coordinate alone has n possibilities.
Thus this partition accounts for at most

    n^b product_(blocks C) B_(|C|)
        <=n^(r-1) B_*(r)^(r-1)

tuples.
This bound is unaffected by repeated exponents or by the possible existence of more than one minimal partition.
Taking a union bound is sufficient.
There are at most (2r)^(2r) set partitions: assigning to each label the least label of its block is an injective encoding by functions from a 2r-element set to itself.
Hence the total off-diagonal count is at most D_r n^(r-1).
Together with (5) this proves (3), since for r>=2 one has r! binom(r,2)<=(2r)^(2r)<=D_r.

One may retain the smaller partition-sum constant

    sum_(partitions pi: |C|>=2, |pi|<=r-1)
                        product_(C in pi) B_(|C|)

for the off-diagonal bound.
The simple constant (2) keeps the dependence on an arbitrary supplied sequence B_k explicit.

There is a useful improvement when log B_k<=k f(k) for a nonnegative nondecreasing function f on the positive integers.
For every partition in the proof, the sum of its block sizes is exactly 2r, including repeated labelled terms.
Therefore

    product_(C in pi) B_(|C|)
         <=exp(sum_(C in pi) |C| f(|C|))
         <=exp(2r f(2r)).

In this situation all occurrences of D_r in (3), (7) and (8) may instead use the alternative valid error constant

    Dtilde_r=(2r)^(2r) exp(2r f(2r))   for r>=2,
    Dtilde_1=0.                                         (5a)

The same diagonal-deficit comparison applies.
This refinement does not assert that the partition sum, or (5a), is optimal.

<a id="energy-to-original-binary-collision"></a>
## A direct collision bound without finite quotient transfer

Now let alpha be an algebraic unit with monic irreducible polynomial of degree d, and put O=Z[alpha].
On its dual torus T^d, with normalized Haar measure, write

    Z_n(y)=sum_(j<n) exp(2pi i <y,alpha^j>),
    S_n(y)=sum_(j<n) sin^2(pi <y,alpha^j>),
    W_n(y)=product_(j<n) cos^2(pi <y,alpha^j>).

Characters are interpreted in the integral power basis of O.
Expanding and integrating gives exactly

    integral |Z_n|^(2r)=A_(n,r),
    Col_binary(n)=integral W_n,
    S_n=n/2-Re(Z_n)/2.                                   (6)

These are the original Haar integrals, not averages over a selected residue-field or finite quotient.
Since W_n<=exp(-S_n), the set S_n<n/4 lies inside |Z_n|>n/2.
Markov's inequality yields

    Col_binary(n)<=(4/n^2)^r A_(n,r)+exp(-n/4)
      <=(4r/n)^r+(4/n^2)^r D_r n^(r-1)+exp(-n/4).         (7)

In particular, if D_r<=n, then

    A_(n,r)<=2r! n^r,
    Col_binary(n)<=2(4r/n)^r+exp(-n/4).                   (8)

Thus every improved shape bound can be inserted into (2), followed by (7) or (8).
Neither integrality-based transfer to a finite primitive quotient nor a new nonvanishing assertion is needed for this consequence.
The faithfulness result in L G0084 remains available if a finite-quotient interpretation is wanted.

<a id="ess-explicit-slow-moment-window"></a>
## One fully explicit window from the ESS statement

The externally accepted Evertse--Schlickewei--Schmidt Theorem 1.1, at the [scoped statement and specialization](../audits/literature/ESS02/Yin_U001.md#ess-normalized-power-shapes), gives, for the rank and normalization in (1), the permissible uniform bounds

    B_k=exp(k [6(k-1)]^[3(k-1)])   for k>=3,
    B_2=1.                                               (9)

This is an application of its (k-1)-variable theorem to a tuple group of rank k-1.
No proof of that theorem is inferred from the elementary block argument above.
The following is a fallback obtained from precisely (9), not a claim about the best published nondegenerate-equation estimate.

For every integer n with L=log log n>=64, put

    r=floor[L/(12 log L)].                               (10)

Then r>=1, and (2), with (9), satisfies

    D_r<=exp((log n)^(3/4))<=sqrt(n).                     (11)

For r=1 this is immediate from D_1=0.
For r>=2, (9) is increasing in k and log B_(2r)<=2r(12r)^(6r).
Also 12r<=L/log L<=L, so 6r log(12r)<=L/2.
Consequently

    log D_r
      <=2r log(2r)+2r(r-1)(12r)^(6r)
      <=4L^2 exp(L/2)
      <=exp(3L/4).

For the last inequality use log 4+2 log L<=L/4 for L>=64.
It holds at 64, and its right side minus left side has positive derivative there and thereafter.
Exponentiating gives the first inequality (11); the second follows from log n>=16.
In particular the normalized moment has the uniform bound

    |A_(n,r)/(r!n^r)-1|<=n^(-1/2).                       (12)

Equation (8) now holds at (10).
A convenient explicit consequence for H_2(n)=-log Col_binary(n) is

    H_2(n)>= (log n)(log log n)/(48 log log log n)-log 3
       whenever log log n>=64.                          (13)

Indeed r>=L/(24 log L), since floor x>=x/2 for x>=1.
Writing u=log n, one has r<=log u<=sqrt(u), 4r<=sqrt(n), and 2r log n<=n in this range.
For the latter two estimates, use exp(u)>=u^3/6 and u>=16.
It follows that 2(4r/n)^r+exp(-n/4)<=3exp(-r log n/2), proving (13).

This is a uniform superpolynomial upper bound on collision probability, but its logarithm is sublinear in n.
It is not an exponential-in-n collision bound.
All numerical constants in (10)--(13) are chosen for an elementary safe threshold.

<a id="conditional-polynomial-shape-window"></a>
## A stronger window conditional on a specified shape formula

The [AV09 located-source unit](../audits/literature/AV09/Yin_U001.md#av09-located-count) records a proposed sharper shape formula in the Amoroso--Viada direction, but its original theorem page was not accessed in this round.
The following statement is therefore explicitly conditional on the displayed bound; it is not an adoption or source audit of that theorem.
Suppose, for every k>=3 and every fixed sign vector in the same domain, that

    B_k<=[8(k-1)]^[4(k-1)^4(2k-1)].                      (14)

Then log B_k<=8k^5 log(8k), so one may use (5a) with the nonnegative increasing function f(k)=8k^4 log(8k).
This gives

    log Dtilde_r<=2r log(2r)+256r^5 log(16r)
                  <=512r^5 log(16r)   for r>=2.          (15)

For every integer n with u=log n>=2^14, set

    r=floor[(u/(1024 log u))^(1/5)].                     (16)

Then r>=1, Dtilde_r<=sqrt(n), and the same estimates prove

    |A_(n,r)/(r!n^r)-1|<=n^(-1/2),
    H_2(n)>= (log n)^(6/5)/(16(log log n)^(1/5))-log 3.   (17)

For completeness, u>=1024 log u holds at 2^14 and is preserved thereafter, giving r>=1.
For r>=2, r<=u^(1/5), hence 16r<=u in this range.
Inserting log(16r)<=log u and (16) into (15) gives log Dtilde_r<=u/2.
The r=1 case again uses Dtilde_1=0.
Also r<=sqrt(u), so the elementary comparisons following (13) give H_2(n)>=ru/2-log 3.
Finally floor x>=x/2 for x>=1 and 1024^(1/5)=4 yield (17).
Every implication in this paragraph is a direct consequence of the hypothetical count (14).

The resulting moment order is of size (log n/log log n)^(1/5), larger than (10), but still far below linear order.
Its collision exponent is still o(n).
Retaining this conditional substitution prevents the ESS fallback from being mistaken for an optimal known-source window.
It supplies no unconditional use of the uninspected sharper source.

<a id="fixed-moments-linear-order-boundary"></a>
## What this does and does not supply at growing moment order

For arbitrary B_k, the useful quantitative question is how small D_r/n can be when r is allowed to depend on n.
Merely establishing (3) for every fixed r does not answer it.
With exactly the coarse ESS substitution (9), the explicit constant (2) has

    log log D_r=6r log r+O(r)   as r tends to infinity.

Thus every fixed c<1/6 permits r<=c log log n/log log log n asymptotically in this error estimate.
For c>1/6 its displayed D_r/n instead diverges along that scale; this describes the chosen upper-bound formula, not the true energy or the actual number of relation shapes.
A better external shape estimate, or sharper use of the relation structure, may give a larger window.
No claim of optimality among known methods is made.

In particular these fixed-moment asymptotics and their present quantitative instantiation do not establish L G0084's common-C bound A_(n,r)<=(Crn)^r at r=floor(kappa n).
They do not disprove such a bound either.
The constants in (13) are independent of degree and of the particular nontorsion unit, but (13) divided by n tends to zero.
A finite-time lower bound for H_2(n)/n is also not automatically a lower bound for its subadditive limit.
There is therefore no entropy-gap or finite-capture conclusion from (3), (12), or (13) alone.

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C276](../claims/Yin_C_G0276_v1.md#argument), with its actual selected assessment.
The [current entire finding](../audits/reviews/Yin_R_G0534_v1.md#current-block-energy-finding) is self-reviewed.
The [complete original checking account and exact findings](../audits/reviews/Yin_R_G0534_v1.md#historical-block-author-finding) retain their original2026-10-07 inputs, mathematical contributions, actual scopes and limitations.
Original independent or collaborator wording does not supply unrecorded initial context or transfer an old finding to this new C.
