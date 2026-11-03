---
author: Yin
---

# Complete uniform ceilings for finite-prime and arbitrary multilevel certificates

This retains the complete original 2026-10-07 analytic proofs of [L58](../ledger/Yin_L_G0058_v1.md) and [L60](../ledger/Yin_L_G0060_v1.md), preserving each proof's own local equation numbers.
The first proof controls every finite-prime parameter choice; the second genuinely enlarges the exponent and multiplicity class and controls it by a prime-factor graph-energy estimate.
Both concern sufficient lower certificates using only Q_arith>=1, and neither upper-bounds true entropy or the discarded surplus.

## Statement

A. Fix integersd>=2,k,S>=1, integers p_1,...,p_S>=2 (the analytic proof needs neither primality nor distinctness), and positive realD.
Put f=sum_i logp_i,P=sum_i p_i,N=d(k+S), and define the exact original, factorial and full-block expressions B_0,B_der,B_block by PartI formulas1--3, including the exact binomial Gram product A_(N,k) and actual denominators.
With [x]_+=max(x,0) and c_0=4/sqrt3,

    [B_0]_+<=2/[e^2 logD],
    [B_der]_+<=8/[3e^2 logD]                       forD>1,
    [B_block]_+<=4/[e^2 log(D/c_0)]               forD>c_0.

The exact sum-binomial individual-column expression is dominated in positive part by the full-block expression and has the same block ceiling.
All bounds are simultaneous in every integer parameter and entire selected number set, including choices depending arbitrarily onD or the individual input, and the corresponding suprema.
Any auxiliarydelta>=D weakens the same estimates.
The arithmetic interpretation still separately requires actual distinct eligible primes and the original nonzero nontorsion integral conjugates at the selected degree-preserving levels; the larger analytic domain does not certify invalid arithmetic inputs.

B. Let alpha be nonzero nontorsion integral of degreed>=2, Delta=abs(discP),D=d/Delta^(1/d), and let A be any finite nonempty set of positive integers with positive integer multiplicitiesm_a, such that deg(alpha^a)=d for every selecteda.
Use all original powered conjugates, without removing multiplicities at intermediate levels, and set

    s=sum_a m_a, q=sum_a m_a^2,H=sum_a a m_a,N=ds,
    E=sum_(a,b inA,b/a=ell^r) m_a m_b logell,

where each ordered increasing pair with primeell and integerr>=1 is counted once.
The edge has weightlogell, without an extra factorr.
The complete determinant factorization is

    |detV_conf|^2=Delta^q exp(2dE)Q_arith,

with the exact positive integer product in PartII formula5, including all powered indices, normalized edge resultants and unnormalized nonedge resultants.
Every simultaneous Frobenius floor is paid through its own resultant, and the sharp stated uniform energy bound is

    E<=(2/e)sqrt(qsH).

For the exact coarse, factorial-corrected and full-block expressions in PartII formulas8,10,12--15, the same three positive-part ceilings inA hold at their displayed domains.
They hold uniformly over every eligible finiteA and all its multiplicities, even when these choices depend on the input orD.
The single-level and d=2 boundaries, exact weighted denominators and exact column domination are included.
The complete C231 norm descent supplies eligible all-positive-power endpoints only for counterexample-existence reductions, not for an arbitrary unreplaced input.

Both parts tend uniformly to zero asD tends to infinity.
This closes only parameter optimization of the displayed floor-only sufficient estimates.
Keeping the actual integerQ_arith adds log(Q_arith)/d to the normalized numerators; no bound on that addition, existence of a vanishing-entropy sequence, all-methods obstruction or unrestricted entropy gap is asserted.

## Current assessment
[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:03 |
| status | open |
| reason | Register both complete retained analytic proofs with exact constants, scalar/degree/level domains and the arithmetic-surplus boundary; actual current complete inspection and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete exact statement](#statement) | Both original finite-prime parameter ceilings and arbitrary finite prime-power-ratio level/multiplicity ceilings, exact domains, all positive-part/supremum/auxiliary-parameter limits and discarded-surplus boundary. |
| argument | [Both complete proofs](#argument) | Entire original L58 and L60 arguments: square completion, both denominator comparisons, exact block gain, full edge factorization and incoming-square energy, single-level case, all exact weighted costs and scope guards. |
| dependency | [Complete finite construction](Yin_C_G0230_v1.md#argument) | Normalized confluent determinant for arbitrary multiplicities, exact arithmetic product and directly proved finite-difference block constant; no source asymptotic is imported. |
| support | [All-positive-power existence descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Only existence-scope access to every selected exponent, not a pointwise implication from prime stability or a needed premise of the guarded finite formulas. |
| support | [Discriminant escape](Yin_C_G0219_v1.md#discriminant-escape) | Conditional relevance of D tending to infinity on a hypothetical reduced vanishing-positive-measure sequence, without asserting one exists. |
| support | [Mat96 exact finite source unit](../audits/literature/Mat96/Yin_U001.md#mat96-u001) | Classical source interface and corrected eligibility only; both optimized ceiling proofs are complete local arguments and do not audit prime asymptotics. |

## Complete retained arguments

<a id="argument"></a>

Each proof retains its original 2026-10-07 mathematics and local formula numbers.

## PartI: complete finite-prime parameter optimization

<a id="mat96-optimized-ceilings"></a>
### Parameters and exact claims

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
### One elementary estimate controls every prime choice

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
### Original and factorial-corrected cases

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
### The full block gain still leaves a logarithmic barrier

The exact factorial product in (3) gives

    a_(N,k)=sum_(j=0 to k-1)
                  log[(2j+1)((2j)!)^2/(j!)^2]
             -sum_(j=0 to k-1)sum_(h=1 to j)
                  log(1-h^2/N^2).                     (10)

This follows by pairing the factors N-h and N+h in
(N+j)!/(N-j-1)!.
The [finite-difference derivation of A_(N,k)](Yin_C_G0230_v1.md#exact-confluent-block-cost) is supplied in the separate finite construction; the estimate here follows directly from its displayed product.

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
### Consequence and the exact stopping boundary

The [discriminant-escape implication in L G0015](Yin_C_G0219_v1.md#discriminant-escape) says that a hypothetical reduced vanishing-positive-entropy sequence must have D tending to infinity.
Equations (4)--(5) show that no choice of k,S, eligible prime set or auxiliary delta within the three displayed formulas can maintain a positive absolute certificate on that regime.
This is true even if the parameter choices depend arbitrarily on the individual polynomial.

This conclusion does not assert that such a sequence exists, that its true entropy is at most (4) or (5), or that Lehmer is false.
It also does not remove the valid restricted positive bounds on bounded-D families.
It closes a specific attempt to obtain a D-independent gap merely by optimizing these established finite inequalities and their row-volume refinements after replacing Q_arith by one.
Keeping the actual integer surplus adds (log Q_arith)/d to each numerator as normalized here; neither that gain nor its growth has been bounded above in this proof.
A further argument could exploit precisely that new arithmetic information or change the actual determinant construction and resulting estimate.
Multiplicities at several powered levels, if they change the displayed numerator and denominator, are not analyzed by this record.

## PartII: complete arbitrary-level Frobenius energy and costs

<a id="multilevel-degree-hypotheses"></a>
### Selected levels and the precise degree guard

Let alpha be a nonzero nontorsion algebraic integer of degree d>=2, with monic minimal polynomial P, conjugates alpha_1,...,alpha_d, Mahler logarithm h=log M(P), and

    Delta=|disc P|,       D=d/Delta^(1/d).

Choose a finite nonempty set A of positive integers and, for every a in A, a positive integer multiplicity m_a.
Assume explicitly

    deg(alpha^a)=d       for every selected a in A.      (1)

This is a hypothesis on exactly the selected levels, including any composite levels.
No implication from L G0014's prime-exponent endpoint to all composite powers is assumed.
Intermediate levels between selected exponents need not be included or satisfy an additional hypothesis.

For the existence question behind an entropy gap, the [norm descent in L G0059](Yin_C_G0231_v1.md#all-positive-power-existence-descent) permits replacing an input by an all-positive-power degree-preserving algebraic integer with no larger positive Mahler logarithm; units remain units.
Every finite exponent set is eligible on that replacement.
This is an existence reduction to a possibly different input and flow, not a pointwise strengthening of prime stability for the original alpha.
It does not remove condition (1) when applying the formulas to a specified unreplaced input.

Put

    P_a(t)=product_(i=1)^d (t-alpha_i^a),
    s=sum_a m_a,       q=sum_a m_a^2,
    H=sum_a a m_a,     N=ds.

The polynomials P_a are monic integral and squarefree by (1), and M(P_a)=M(P)^a.
The distinct exponent levels are disjoint: an equality alpha_i^a=alpha_j^b with a!=b, transported around a finite-order Galois automorphism taking alpha_i to alpha_j, would imply alpha_i^(a^r)=alpha_i^(b^r) for some r>0.
This would make alpha_i torsion, contrary to the hypothesis.
Thus every node used in the confluent construction is distinct except for its prescribed multiplicity.

<a id="prime-power-edge-floor"></a>
### Every prime-power-ratio floor can be counted simultaneously

Call (a,b) an edge when a,b belong to A and b/a=ell^r for a prime ell and an integer r>=1.
Its weight is log ell, not r log ell.
Define

    E=sum_(edges a->b) m_a m_b log ell.                 (2)

At such a pair, iterated coefficientwise Frobenius gives

    P_b=P_a modulo ell.

Indeed the roots at level b are the ell^r-th powers of the roots at level a; elementary symmetric functions commute with Frobenius modulo ell, and integer coefficients are fixed modulo ell.
This argument retains all d roots through intermediate powering, so it does not require degree preservation at the intermediate levels.
Consequently

    0!=Res(P_a,P_b) is divisible by ell^d.              (3)

Only this floor is asserted.
In particular ell^(rd) is not inferred from r Frobenius iterations.

For each level define the integral nonzero divided-difference product

    b_a=product_(i<j)
          (alpha_j^a-alpha_i^a)/(alpha_j-alpha_i).

Its integrality and nonvanishing follow exactly as in [L G0057](Yin_C_G0230_v1.md#confluent-arithmetic-lower-bound): it is a symmetric integral polynomial in the original roots, and (1) excludes zero.
Thus |disc P_a|=Delta b_a^2.

Use the normalized derivative columns of multiplicity m_a at every root of P_a.
The resulting square matrix V_conf has size N.
The direct confluent product formula gives

    |det V_conf|^2
      =product_a |disc P_a|^(m_a^2)
          product_(a<b) |Res(P_a,P_b)|^(2m_a m_b)
      =Delta^q exp(2dE) Q_arith,                       (4)

where the exact positive integer surplus is

    Q_arith=product_a b_a^(2m_a^2)
       * product_(edges a->b)
           [Res(P_a,P_b)/ell^d]^(2m_a m_b)
       * product_(nonedges a<b)
           Res(P_a,P_b)^(2m_a m_b) >=1.                (5)

Each ratio b/a that is a prime power has a unique underlying prime.
Hence no pair receives two floors.
Different edges may use the same prime, but their factors in (4) are separate resultants; the product divisibility follows from the displayed exact factorization.
No unproved extra divisibility for nonedges is used.

<a id="frobenius-prime-factor-energy"></a>
### A uniform graph-energy inequality

The decisive bound, independent of the number or spacing of levels, is

    E <= (2/e) sqrt(q s H).                            (6)

For a fixed upper level b, the possible predecessors b/ell^r are distinct.
Cauchy--Schwarz therefore gives

    sum_(ell^r|b, b/ell^r in A) m_(b/ell^r) log ell
      <=sqrt(q) sqrt(sum_(ell^r|b) (log ell)^2).

Writing v_ell(b) for the prime valuation, the last sum is

    sum_ell v_ell(b)(log ell)^2 <= (log b)^2.

For the inequality, expand the square of the sum of the nonnegative multiset consisting of v_ell(b) copies of log ell; its sum is log b.
Multiplying the previous bound by m_b and summing over b proves

    E<=sqrt(q) sum_b m_b log b.

Finally (log x)^2/x<=4/e^2 for x>=1, with maximum at x=e^2.
A second Cauchy--Schwarz inequality gives

    (sum_b m_b log b)^2
      <=(sum_b m_b)(sum_b m_b(log b)^2)
      <=(4/e^2)sH,

which is (6).
The level b=1 has no incoming edge and contributes log 1=0.
No prime asymptotic is hidden in this proof; the arithmetic input is just unique prime factorization of the integer b.

For every L>0, (6) implies

    2E-Lq <= E^2/(Lq) <=4sH/(e^2 L).                  (7)

The first inequality is equivalent to (E-Lq)^2>=0.
Thus the multiplicities and the exponent graph cannot produce an unbounded edge gain relative to the quadratic multiplicity penalty and the exponent cost.

<a id="multilevel-coarse-factorial"></a>
### Coarse and normalized-derivative certificates

Applying the column estimates of [L G0057](Yin_C_G0230_v1.md#exact-confluent-column-cost) at every level gives the coarse upper bound

    |det V_conf|^2<=N^(dq) M(P)^(2NH).

Combining this with (4) after replacing Q_arith by one yields the valid finite lower estimate

    h>=B_0:=[2E-q log(Ds)]/(2sH).                      (8)

For D>1 its numerator is at most 2E-q log D.
Hence (7) proves

    [B_0]_+<=2/(e^2 log D).                            (9)

The factorial-corrected column bound instead has normalized numerator

    2E-q log(Ds)+T,
    T=2 sum_a sum_(j=0 to m_a-1) log(j!),

and exact positive denominator

    D_der=(2/d)[(N-1)H
                   -(1/2)sum_a a m_a(m_a-1)].         (10)

The bound T<=sum_a m_a(m_a-1)log m_a<=q log s again leaves a numerator at most 2E-q log D.
If A has only one level then E=0, so the positive part is zero for D>1.
Otherwise each integer multiplicity satisfies m_a+1<=s.
Therefore

    D_der/(2sH)
      =1-[sum_a a m_a(m_a+1)]/(2dsH)
      >=1-1/(2d)>=3/4.

Using (7) once more, the exact factorial certificate satisfies

    [B_der]_+<=8/(3e^2 log D),       D>1.               (11)

The positive-part convention matters: denominator improvements are used only when the numerator is positive.
The underlying entropy estimates themselves can alternatively be derived directly from their respective determinant upper bounds, without manipulating a signed estimate.

<a id="multilevel-exact-block-ceiling"></a>
### Full block cost and its uniform optimized ceiling

For 1<=m<=N let the exact binomial block constant be

    A_(N,m)=product_(j=0 to m-1)
       [(N+j)!(j!)^2 / ((2j+1)(N-j-1)!((2j)!)^2)],
    a_(N,m)=m^2 log N-log A_(N,m).

The product formula and its finite-difference proof are retained in [L G0057](Yin_C_G0230_v1.md#exact-confluent-block-cost).
Applying that block bound separately to all nodes gives

    |det V_conf|^2
      <=[product_a A_(N,m_a)]^d
            M(P)^(2 sum_a a m_a(N-m_a)).              (12)

Let c_0=4/sqrt(3).
The elementary bound in [L G0058](../ledger/Yin_L_G0058_v1.md#block-parameter-ceiling) applies to every selected block:

    a_(N,m_a)<=m_a^2 log(c_0 m_a).

For completeness, N=ds>=2m_a and each correction index j<m_a has j/N<1/2.
The exact product then gives

    a_(N,m_a)
      <=m_a^2 log(2m_a)
           +[m_a(m_a-1)/2]log(4/3)
      <=m_a^2 log(c_0 m_a).

Thus the full-block normalized numerator, with Q_arith replaced by one, is

    U=2E-q log(Ds)+sum_a a_(N,m_a)
      <=2E-q log(D/c_0).                              (13)

Its exact denominator is

    D_block=(2/d)sum_a a m_a(N-m_a)
       =2[sH-(1/d)sum_a a m_a^2]
       >=(1-1/d)2sH>=sH.                             (14)

Here m_a<=s implies sum_a a m_a^2<=sH.
Both the exact denominator and its comparison are positive.
For D>c_0, equations (7), (13) and (14) prove

    [B_block]_+=[U/D_block]_+
       <=4/[e^2 log(D/c_0)].                          (15)

The exact sum-binomial individual-column bound is covered too.
Its constant is at least the product of the corresponding block constants, and its entropy exponent exceeds the block exponent by sum_a a m_a(m_a-1).
Hence its positive part is no larger than [B_block]_+.

Equations (9), (11) and (15) are uniform over every finite exponent set, every collection of positive integer multiplicities, and every eligible selection of degrees satisfying (1).
They also bound the supremum when all those parameters depend on D or on the individual input.
Any auxiliary delta>=D makes the estimates only weaker.
Thus arbitrary finite layering, repeated prime-power Frobenius floors and these exact row-volume refinements do not evade the D-to-infinity decay.

<a id="multilevel-surplus-boundary"></a>
### The remaining arithmetic information is explicit

The result concerns the specific lower estimates obtained by using Q_arith>=1 in (4).
Keeping its actual value adds (log Q_arith)/d to each normalized numerator.
Neither (6) nor (15) bounds that contribution.
In particular the divided-difference indices, extra valuations beyond the single ell^d floor, and cross-resultants at non-prime-power ratios all remain visible in the exact product (5).

The [discriminant-escape conclusion in L G0015](Yin_C_G0219_v1.md#discriminant-escape) explains why a uniformly positive certificate in the D-to-infinity regime would matter for the reduced Lehmer route.
The present theorem proves that the enlarged family of floor-only formulas cannot supply it by parameter choice alone.
It does not construct a vanishing-entropy sequence, upper-bound the true h, refute Lehmer, or exclude a new arithmetic lower estimate on Q_arith.
It also does not assert that every composite exponent is available at an L G0014 endpoint: condition (1) stays explicit throughout.
