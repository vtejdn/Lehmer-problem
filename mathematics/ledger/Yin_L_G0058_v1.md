---
author: Yin
---

# G0001: uniform ceilings for the optimized Mat96 finite certificates

Current complete proof: [C232v2](../claims/Yin_C_G0232_v2.md#mat96-optimized-ceilings), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input, with its exact quantifiers, failed/remaining scope and source limits.

Date: 2026-10-07.
Direct analytic calculation by assigned AI assess_shortness_route for Yin.
The exact Mat96 finite-parameter interface is retained in [Mat96 U001](../audits/literature/Mat96/Yin_U001.md#mat96-u001), with the earlier single-prime application in [L G0015](Yin_L_G0015_v1.md#finite-prime-discriminant-gap).
The normalized-derivative and full-block expressions have direct finite proofs in [L G0057](Yin_L_G0057_v1.md#exact-confluent-column-cost).
This record proves the optimization ceilings for those displayed expressions; it does not silently adopt an additional source theorem or replace their arithmetic validity conditions.

The result is an upper bound on the positive part of a sufficient entropy lower estimate, not an upper bound on entropy.
Even after optimizing all allowed integer parameters and all choices of eligible primes, each of the three estimates tends uniformly to zero in the regime D tending to infinity.
All three estimates use the exact positive integer arithmetic surplus of [L G0057](Yin_L_G0057_v1.md#confluent-arithmetic-lower-bound) only through Q_arith>=1; the argument does not bound its actual value.
No prime number theorem, numerical scan, existence of a vanishing-entropy sequence or assumption that Lehmer is false is used.

<a id="mat96-optimized-ceilings"></a>
## Parameters and exact claims

Let d>=2 and k,S>=1 be integers.
Let p_1,...,p_S>=2 be the selected primes, and put

    f=sum_(i=1 to S) log p_i,
    P=sum_(i=1 to S) p_i,
    N=d(k+S),
    D=d/Delta^(1/d).

The analytic argument only uses p_i>=2: it does not require distinctness or primality.
Allowing this larger class can only make an upper bound on optimization stronger.
The actual arithmetic lower estimates still require the separately stated eligible-prime and degree-preservation conditions.
All logarithms are natural, and [x]_+=max(x,0).

Define the original expression

    B_0=[2kf-(k^2+S)log(D(k+S))]
          /[2(k+S)(k+P)].                              (1)

For the normalized derivative rows put

    T_k=2 sum_(j=0 to k-1) log(j!),
    B_der=[2kf-(k^2+S)log(D(k+S))+T_k]
          /{(2/d)[(N-1)(k+P)-k(k-1)/2]}.              (2)

For the full root-block Hadamard refinement put

    A_(N,k)=product_(j=0 to k-1)
      [(N+j)!(j!)^2 / ((2j+1)(N-j-1)!((2j)!)^2)],
    a_(N,k)=k^2 log N-log A_(N,k),

    B_block=[2kf-(k^2+S)log(D(k+S))+a_(N,k)]
              /{(2/d)[k(N-k)+(N-1)P]}.                (3)

The exact denominators in (2)--(3) are retained; replacing them by the coarser denominator of (1) is not needed.
For D>1,

    [B_0]_+ <= 2/[e^2 log D],
    [B_der]_+ <= 8/[3e^2 log D].                        (4)

For D>c_0, where c_0=4/sqrt(3),

    [B_block]_+ <= 4/[e^2 log(D/c_0)].                   (5)

These bounds are uniform in d,k,S and the selected primes.
The same ceilings therefore bound the supremum of the positive parts over all those choices.
The optional auxiliary parameter delta>=D in Mat96's statement cannot evade them: replace D in the proof by delta, and then weaken the resulting decreasing ceiling back to the one at D.

<a id="prime-sum-square-bound"></a>
## One elementary estimate controls every prime choice

Put x=P/S>=2.
Concavity of the logarithm gives f<=S log x, and therefore

    f^2/(SP) <= (log x)^2/x <= 4/e^2.                   (6)

The last inequality follows by differentiating (log x)^2/x on x>=1; its maximum occurs at x=e^2.
Neither the number nor the size of the primes is fixed in (6).

For every L>0,

    2kf-k^2 L = f^2/L-L(k-f/L)^2 <= f^2/L.              (7)

Consequently, if a certificate numerator is at most 2kf-k^2 L and its positive denominator is at least

    2c(k+S)(k+P),       c>0,

then its positive part is at most

    f^2/[2c L (k+S)(k+P)]
       <=f^2/(2c L SP)<=2/(c e^2 L).                   (8)

If the numerator is nonpositive the assertion is immediate; otherwise the positive denominator comparisons have the indicated direction.
This one bound allows k,S and the entire prime set to vary simultaneously.

<a id="factorial-parameter-ceiling"></a>
## Original and factorial-corrected cases

For D>1, the numerator in (1) is at most 2kf-k^2 log D after dropping only nonpositive terms.
Equation (8) with c=1 gives the first claim in (4).

For every k>=1,

    T_k<=2 sum_(j=0 to k-1) j log k
        =k(k-1)log k
        <=(k^2+S)log(k+S).                             (9)

The case k=1 uses 0!=1 and log 1=0.
Thus the factorial addition is fully absorbed by the dimension logarithm already present in the numerator.
The numerator of (2) is still at most 2kf-k^2 log D.

The ratio of the exact denominator in (2) to 2(k+S)(k+P) is

    1-(1/d)[1/(k+S)+k(k-1)/(2(k+S)(k+P))].

The bracket is at most 1/2.
To see this, clear its positive denominator: the desired inequality is equivalent to

    (k+S)(k+P)-2(k+P)-k(k-1)
       =k(S+P-1)+P(S-2)>=0.

For S=1 this is P(k-1)>=0, and for S>=2 it is plainly nonnegative.
Hence the exact denominator is at least

    (1-1/(2d)) 2(k+S)(k+P)
        >=(3/4) 2(k+S)(k+P).

Using c=3/4 in (8) proves the second claim in (4).
If one uses the weaker factorial expression with the original denominator of (1), its sharper ceiling is simply 2/[e^2 log D].

<a id="block-parameter-ceiling"></a>
## The full block gain still leaves a logarithmic barrier

The exact factorial product in (3) gives

    a_(N,k)=sum_(j=0 to k-1)
                  log[(2j+1)((2j)!)^2/(j!)^2]
             -sum_(j=0 to k-1)sum_(h=1 to j)
                  log(1-h^2/N^2).                     (10)

This follows by pairing the factors N-h and N+h in
(N+j)!/(N-j-1)!.
The [finite-difference derivation of A_(N,k)](Yin_L_G0057_v1.md#exact-confluent-block-cost) is supplied in the separate finite construction; the estimate here follows directly from its displayed product.

For j<k one has (2j)!/j!<= (2k)^j and 2j+1<=2k.
Since N=d(k+S)>2k, also h/N<1/2 in every term.
Therefore

    a_(N,k)
      <= k^2 log(2k) + [k(k-1)/2]log(4/3)
      <= k^2 log[(4/sqrt(3))k]
       = k^2 log(c_0 k).                               (11)

For D>c_0>1, insert (11) in the numerator of (3), use k<=k+S, and discard the remaining nonpositive S terms.
The result is at most

    2kf-k^2 log(D/c_0).                                (12)

The ratio of its exact denominator to 2(k+S)(k+P) is

    1-(k^2+P)/[d(k+S)(k+P)].

Since

    (k+S)(k+P)-(k^2+P)=kS+kP+P(S-1)>=0,

this ratio is at least 1-1/d>=1/2.
Equation (8), now with c=1/2 and L=log(D/c_0), proves (5).
The factorial gain and the stronger full-block gain therefore change the numerical estimate but cannot prevent uniform decay under unrestricted parameter optimization.

The same ceiling also covers the exact sum-binomial column-cost estimate between these two refinements.
In the notation of L G0057, put B_(N,j)=sum_(s=j)^(N-1) binom(s,j)^2.
Ordinary Hadamard gives A_(N,k)<=product_(j<k) B_(N,j), so the full-block estimate has at least as large a numerator as that exact column estimate.
Its positive denominator is no larger, since

    [(N-1)(k+P)-k(k-1)/2]
      -[k(N-k)+(N-1)P]=k(k-1)/2>=0.

If the column numerator is positive, both comparisons improve the estimate; if it is nonpositive, its positive part is zero.
Thus the exact column-cost positive part is at most [B_block]_+, and (5) bounds it as well.

<a id="mat96-ceiling-scope"></a>
## Consequence and the exact stopping boundary

The [discriminant-escape implication in L G0015](Yin_L_G0015_v1.md#discriminant-escape) says that a hypothetical reduced vanishing-positive-entropy sequence must have D tending to infinity.
Equations (4)--(5) show that no choice of k,S, eligible prime set or auxiliary delta within the three displayed formulas can maintain a positive absolute certificate on that regime.
This is true even if the parameter choices depend arbitrarily on the individual polynomial.

This conclusion does not assert that such a sequence exists, that its true entropy is at most (4) or (5), or that Lehmer is false.
It also does not remove the valid restricted positive bounds on bounded-D families.
It closes a specific attempt to obtain a D-independent gap merely by optimizing these established finite inequalities and their row-volume refinements after replacing Q_arith by one.
Keeping the actual integer surplus adds (log Q_arith)/d to each numerator as normalized here; neither that gain nor its growth has been bounded above in this proof.
A further argument could exploit precisely that new arithmetic information or change the actual determinant construction and resulting estimate.
Multiplicities at several powered levels, if they change the displayed numerator and denominator, are not analyzed by this record.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0019_v1.md#actual-review-and-provenance), with its original exact scopes, known author/contributor checks and separately unknown initial review arrangements.
