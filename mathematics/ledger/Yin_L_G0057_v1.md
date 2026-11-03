---
author: Yin
---

# G0001: direct finite-prime confluent determinant and exact block cost

Current complete proof: [C230v1](../claims/Yin_C_G0230_v1.md#finite-prime-confluent-hypotheses), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input, with its exact quantifiers, failed/remaining scope and source limits.

Date: 2026-10-07.
Bounded reconstruction by assigned AI review_matrix_completion for Yin.
The retained Mat96 original was visually inspected at printed pp.417--418 using rendered pages.
Those pages give the node construction, determinant estimates (5)--(7) and the finite-prime specialization.
The source's externally cited confluent-determinant lemma and prime asymptotics are not taken as unreviewed premises here: the finite determinant formula, arithmetic lower bound and norm estimates used below are proved directly.
No parameter scan or claim of novelty is used.
A bounded primary DLMF attribution check is recorded below, separately from the proof.
The retained source statement, normalized convention and torsion guards are recorded separately in [Mat96-U001](../audits/literature/Mat96/Yin_U001.md#mat96-u001).

The result reconstructs the finite-prime mechanism already represented at k=S=1 by [L G0015](Yin_L_G0015_v1.md#finite-prime-discriminant-gap), and retains exact derivative and block-volume costs.
It does not establish an unrestricted entropy gap.
The separate optimization of these finite bounds is an additional question, rather than part of the determinant identity.

<a id="finite-prime-confluent-hypotheses"></a>
## Exact hypotheses and node separation

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2, with monic minimal polynomial P and distinct conjugates alpha_1,...,alpha_d.
Set

    M=M(P),       m=log M,
    Delta=|disc P|,       D_disc=d/Delta^(1/d).

Fix k>=1 and S>=1, and distinct primes p_1,...,p_S such that

    deg(alpha^(p_s))=d       for every selected s.        (1)

They need not be consecutive primes.
Define

    Q_s(t)=product_(i=1)^d (t-alpha_i^(p_s)),
    f=sum_(s=1)^S log p_s,       g=sum_(s=1)^S p_s,
    N=d(k+S).

Q_s is monic integral, and (1) makes its roots distinct.
Its Mahler measure is M^(p_s), by the monic root-product formula.

No additional separation hypothesis across different positive exponents is needed.
Indeed, suppose alpha_i^a=alpha_j^b for positive integers a!=b.
In a finite Galois splitting field choose an automorphism sigma taking alpha_i to alpha_j, and let r be its finite order.
Iterating the equality gives  alpha_i^(a^r)=alpha_i^(b^r).
Since alpha_i is nonzero and nontorsion, this is impossible.
Thus the base conjugates and the S powered conjugate sets are disjoint.
Within each powered set the exact requirement is (1).
In particular the all-prime endpoint supplied by L G0014 suffices for every finite selection here.
All-positive-integer-power degree preservation or a separate assertion about ratios of conjugates is not required.

<a id="direct-confluent-vandermonde"></a>
## A direct normalized-derivative determinant formula

For a node x and derivative index j>=0, let its length-N column be

    c_j(x)_r=binom(r,j) x^(r-j),       0<=r<N,

with zero entry when r<j.
This is the j-th derivative of the monomial column divided by j!.
The normalized convention matters: it removes all factorials from the determinant product itself.

More generally take distinct nodes x_1,...,x_l with positive multiplicities n_1,...,n_l summing to N, and concatenate the columns c_0(x_i)...,c_(n_i-1)(x_i) in that order.
Then

    det V_conf=product_(i<j) (x_j-x_i)^(n_i n_j).         (2)

Here is a direct proof.
Replace the n_i copies of x_i by x_i+epsilon a for a=0,...,n_i-1, and form the ordinary Vandermonde matrix.
Its column at x_i+epsilon a has the exact Taylor expansion sum_r (epsilon a)^r c_r(x_i).
In the determinant, the least possible power of epsilon from the i-th group is n_i(n_i-1)/2: lower powers repeat a derivative column and vanish.
The coefficient at that least power is the confluent determinant times the ordinary Vandermonde determinant on 0,...,n_i-1, for every group.
On the ordinary Vandermonde product side the within-group differences give the same nonzero integer factors and powers of epsilon, and the cross-group differences tend to the right side of (2).
Comparing the least coefficients and cancelling the within-group factors proves (2).
This is a polynomial coefficient argument; no external confluent-determinant theorem is needed.

Apply (2) to the d nodes alpha_i with multiplicity k and the dS nodes alpha_i^(p_s) with multiplicity one.
The separation proof makes this N by N determinant nonzero.
Write it as V_conf from now on.

<a id="confluent-arithmetic-lower-bound"></a>
## The full arithmetic lower bound

Three elementary integral facts give the required bound.

First, coefficientwise Frobenius gives Q_s=P modulo p_s.
This follows by applying Frobenius to the elementary symmetric functions of the roots, and then to the integral coefficients of P.
Write Q_s=P+p_s R_s with R_s integral.
Consequently

    Res(P,Q_s)=product_i Q_s(alpha_i)
              =p_s^d product_i R_s(alpha_i)

is an integer divisible by p_s^d.
It is nonzero by node separation.

Second, the quotient

    b_s=product_(i<j)
          (alpha_j^(p_s)-alpha_i^(p_s))/(alpha_j-alpha_i)

is an integer.
Each divided difference is an integral polynomial in the roots, and their product is symmetric: numerator and denominator both change by the same permutation sign.
It is therefore a rational algebraic integer.
It is nonzero by (1), and

    |disc Q_s|=Delta b_s^2.

Third, for s<t, Res(Q_s,Q_t) is a nonzero integer, again by separation.

Grouping the factors in (2) by their polynomial blocks gives the exact identity

    |det V_conf|^2
      =Delta^(k^2) product_s |disc Q_s|
         product_s |Res(P,Q_s)|^(2k)
         product_(s<t) |Res(Q_s,Q_t)|^2.

Thus the quotient by the following quantity is a positive integer:

    Delta^(k^2+S) product_s p_s^(2dk).

More explicitly, the exact arithmetic surplus is

    Q_arith=|det V_conf|^2
               /[Delta^(k^2+S) product_s p_s^(2dk)]
      =product_s b_s^2
         product_s [Res(P,Q_s)/p_s^d]^(2k)
         product_(s<t) Res(Q_s,Q_t)^2,
    Q_arith is a positive integer.                     (3a)

In particular

    |det V_conf|^2
       >=Delta^(k^2+S) exp(2dk f).                      (3)

This proves simultaneous product divisibility from an exact factorization.
It does not infer divisibility by a product from separate, possibly overlapping divisibility statements.
The cross-prime resultants are retained as nonzero integer factors; no unproved extra prime divisibility is assigned to them.
Replacing Q_arith by one is a deliberate weakening.
Keeping the actual value adds log Q_arith to the numerator of every later unscaled logarithmic bound (or log Q_arith/d after division by d).
An upper ceiling for the sufficient estimates with Q_arith replaced by one therefore does not exclude exploiting growth of this exact surplus.

<a id="exact-confluent-column-cost"></a>
## Column norms, factorials and the original finite estimate

For 0<=j<k put

    B_(N,j)=sum_(r=j)^(N-1) binom(r,j)^2.

Directly from the column entries,

    ||c_j(x)||^2
       <=B_(N,j) max(1,|x|)^(2(N-1-j)).

Hadamard applied to all columns therefore gives

    |det V_conf|^2
       <=[N^S product_(j=0)^(k-1) B_(N,j)]^d
           M^(2[(N-1)(k+g)-k(k-1)/2]).                 (4)

No derivative factorial has been suppressed: the binomial entries are precisely the normalized derivatives in (2).
The elementary estimate B_(N,j)<=N^(2j+1)/(j!)^2 gives the convenient consequence

    |det V_conf|^2
       <=N^(d(k^2+S)) /[product_(j=0)^(k-1) j!]^(2d)
           M^(2[(N-1)(k+g)-k(k-1)/2]).                 (5)

Combining (3) and (4) supplies the exact column-cost lower estimate

    m >= [(k^2+S)log Delta+2dk f
             -d log(N^S product_(j<k) B_(N,j))]
           /[2((N-1)(k+g)-k(k-1)/2)].                  (6)

The factorial version, after dividing numerator and denominator by d and using N=d(k+S), is

    m >= [2k f-(k^2+S)log(D_disc(k+S))
                  +2 sum_(j=0)^(k-1) log(j!)]
           /[2((N-1)(k+g)-k(k-1)/2)/d].               (7)

The numerators in these sufficient bounds may be nonpositive.
Dropping the factorial gain and replacing the exponent in (5) by the larger 2N(k+g) gives directly the coarser inequality

    m >= [2k f-(k^2+S)log(D_disc(k+S))]
           /[2(k+S)(k+g)].                             (8)

To justify this last form even for a negative numerator, derive it from the coarser upper determinant bound itself, using M>=1, rather than manipulating a signed lower bound.
Equation (8) is exactly the finite-prime form of Mat96 (7), with its actual discriminant parameter.
Substituting any larger auxiliary parameter gives a weaker valid estimate.
No prime asymptotic is needed.

<a id="exact-confluent-block-cost"></a>
## A sharper exact block-volume estimate

For a multiplicity-k node, estimate all k columns together.
Let

    A_(N,k)=det[sum_(r=0)^(N-1) binom(r,i)binom(r,j)]_(0<=i,j<k).

Cauchy--Binet and the leading coefficients of binomial polynomials give

    det[(c_i(x)^* c_j(x))_(i,j<k)]
      =sum_(0<=r_1<...<r_k<N)
          [product_(a<b)(r_b-r_a)/product_(j<k)j!]^2
             |x|^(2(sum_a r_a-k(k-1)/2)).

The exponent inside this sum ranges from zero to 2k(N-k), and all coefficients are nonnegative.
Therefore the node block satisfies

    det[(c_i(x)^* c_j(x))_(i,j<k)]
       <=A_(N,k) max(1,|x|)^(2k(N-k)).                 (9)

The squared volume of concatenated column blocks is at most the product of their squared volumes.
One direct proof is block Gram--Schmidt: project each new block orthogonally off the previous blocks; its Gram matrix decreases in positive-semidefinite order, so its determinant does not increase.
Multiply the resulting block volume factors.
Applying this to the d multiplicity-k blocks and the dS singleton blocks yields

    |det V_conf|^2
       <=[N^S A_(N,k)]^d
           M^(2[k(N-k)+(N-1)g]).                       (10)

This pays no larger constant or Mahler exponent than (4): ordinary Hadamard gives A_(N,k)<=product_(j<k)B_(N,j), and k(N-k)<=k(N-1)-k(k-1)/2.
For k=1 both formulas coincide.

The exact constant has the product formula

    A_(N,k)=product_(j=0)^(k-1)
          (N+j)! (j!)^2
             /[(2j+1)(N-j-1)!((2j)!)^2].               (11)

Here is a direct finite-difference proof, included to avoid adding an external discrete-orthogonal-polynomial premise.
For j>=0 let (x)_j=x(x-1)...(x-j+1), let Delta_+ denote forward difference, and set

    f_j(x)=(x)_j(x-N)_j,
    q_j(x)=Delta_+^j f_j(x).

The degree of q_j is j and its leading coefficient is (2j)!/j!.
The polynomial f_j vanishes at the integers 0,...,j-1 and N,...,N+j-1.
Expanding the difference and shifting the summation index therefore gives, for every polynomial h,

    sum_(x=0)^(N-1) q_j(x)h(x)
       =(-1)^j sum_(y=j)^(N-1) f_j(y) nabla^j h(y),

where nabla is backward difference.
This is zero for deg h<j, so the q_j are orthogonal on the integer grid 0,...,N-1.
With h=q_j, nabla^j q_j=(2j)!, and

    (-1)^j f_j(y)
       =(j!)^2 binom(y,j)binom(N+j-1-y,j).

The elementary binomial convolution gives

    sum_(x=0)^(N-1) q_j(x)^2
       =(2j)!(j!)^2 binom(N+j,2j+1).

The monic orthogonal polynomial obtained from q_j must be divided by a further j! to match the leading coefficient 1/j! of binom(x,j).
Thus the squared norm of the j-th Gram--Schmidt residual for the binomial basis is

    (j!)^2 binom(N+j,2j+1)/(2j)!
      =(N+j)!(j!)^2
          /[(2j+1)(N-j-1)!((2j)!)^2].

Multiplying these residual norms proves (11).
All j here satisfy 0<=j<k<=N, so every factorial and residual is well defined.

The known orthogonal-polynomial normalization was checked separately on 2026-10-07 by ms25_source and the coordinator in NIST DLMF [Tables 18.19.1](https://dlmf.nist.gov/18.19#T1) and [18.19.2](https://dlmf.nist.gov/18.19#T2), version 1.2.8.
With Hahn parameters alpha=beta=0 and its grid endpoint set to N-1, the weight is one.
Its squared norm and leading coefficient specialize to

    h_j=(N+j)!(N-j-1)!/[(2j+1)((N-1)!)^2],
    ell_j=(-1)^j(2j)!(N-j-1)!/[(j!)^2(N-1)!].

Thus h_j/(j! ell_j)^2 is exactly the residual norm above.
This is checked attribution and normalization, not an additional premise of the direct finite-difference proof or a claim of novelty.
The original references underlying the DLMF tables were not proof-audited.

Combining (3), (10) and (11) now gives the sharper finite estimate

    m >= [(k^2+S)log Delta+2dk f-d log(N^S A_(N,k))]
           /[2(k(N-k)+(N-1)g)].                        (12)

The positive part of the exact column-cost estimate (6) is at most the positive part of (12): the block numerator is at least the column numerator, while its positive denominator is no larger.
If the column numerator is nonpositive the claim is immediate; otherwise both comparisons have the required direction.
Thus the [uniform block ceiling in L G0058](Yin_L_G0058_v1.md#mat96-optimized-ceilings) also covers the exact binomial-sum version (6), without replacing that sum by the coarser factorial bound.

It is useful to expose its exact gain over the coarse numerator:

    a_(N,k)=k^2 log N-log A_(N,k)
      =sum_(j<k) log[(2j+1)((2j)!)^2/(j!)^2]
         -sum_(j<k)sum_(h=1)^j log(1-h^2/N^2).

Equivalently (12) has numerator, after division by d,

    2k f-(k^2+S)log(D_disc(k+S))+a_(N,k),

and denominator 2[k(N-k)+(N-1)g]/d.
This retains the full block cost for a separate analytic optimization; it does not replace it by an independent arithmetic bonus.

<a id="confluent-versus-fixed-coefficient-space"></a>
## Relation to the earlier coefficient-space boundary

This is a different evaluation map from the d-row remainder map V_N of L G0054--56.
The latter factors through Q[t]/P and kills all coefficient vectors of multiples of P.
The present N-row map records values and normalized derivatives at the base conjugates, as well as values at their selected prime powers.
It is invertible over C.
In particular it does not kill P: if k>=2, the derivative coordinates include P'(alpha_i)!=0, while for every S>=1 its powered coordinates include P(alpha_i^(p_s))!=0.
Thus it cannot factor through that d-dimensional remainder map.

The fixed-span projection ceiling proved in L G0055, or optimization of lifts for a fixed d-row image in L G0056, consequently does not directly give the determinant bounds (3)--(12).
What is used here is the exact product of discriminants and resultants for an enlarged evaluation system, with multiplicity k amplifying the prime divisibility and the original discriminant at different rates.
There is no claim that this enlargement automatically yields a uniform gap.
It is the known Mat96 construction, with directly proved finite bounds and exact costs; its useful information and its discriminant dependence must both remain visible.
In particular, optimizing the estimates (6)--(8) and (12) only optimizes the version that uses Q_arith>=1.
It does not optimize or bound all possible uses of the discarded factors in (3a), nor all possible exponent or multiplicity configurations.

The target is still the original m(P)=h_alg(A) for the companion flow.
No division of entropy by degree, change to the Perron root, bounded-support hypothesis, or unproved all-power endpoint has entered.
Existing source-proof boundaries outside the finite argument reconstructed here remain unchanged.

<a id="confluent-determinant-review"></a>
## Retained formal review

The original complete author/coordinator and separate whole-proof accounts are retained in [R515](../audits/reviews/Yin_R_G0515_v1.md#historical-confluent-author-finding), with the actual coverage contribution and both unknown separate initial arrangements distinguished.
The original2026-10-07 date, all detailed inspection scopes and source-proof limits are preserved there.
The exact Hahn source statement and normalization now have their own [Nat26-U001 home](../audits/literature/Nat26/Yin_U001.md#nat26-u001); the direct finite-difference proof above is complete independently.
