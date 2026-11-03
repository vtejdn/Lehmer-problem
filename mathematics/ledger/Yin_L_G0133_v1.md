---
author: Yin
---

# Cyclic-return transfer and the near-one boundary for delay seeds

Date: 2026-10-08.
Prepared by assigned AI `growth_arithmetic_status` for Yin under the current bounded G0001 exploration.
The coordinator requested a test of the general delay-seed mechanism after L G0131.
Completed independent review and fixed adoption are recorded below.
No new source, numerical computation, source-proof audit, or novelty claim is a premise.

The motivating accepted restricted construction is [L G0131](Yin_L_G0131_v1.md), where a plastic-number seed admits useful cyclic-norm mass at a return exponent linear in the actual irreducible degree.
This account isolates what transfers to an arbitrary fixed monic integral unit seed, what must still be certified about its noncyclotomic core, and why replacing the seed by a near-one seed does not itself produce a new delay family of near-one cores.

The elementary resultant arguments below are direct.
The arithmetic norm interpretation uses the exact retained interface in [L G0074](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion).
Section 6 alone uses the accepted statement of Smyth's nonreciprocal bound in [Smy08 U002](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number).
Section 7 separately uses Lawton's specialization theorem at the retained statement-level scope in [Den09 U002](../audits/literature/Den09/Yin_U002.md) and already used in [L G0050](Yin_L_G0050_v1.md).
Neither original source proof is independently audited here.

<a id="general-delay-return-factorization"></a>
## 1. Exact factorization, including all degenerate cases

Fix a nonconstant monic polynomial f in Z[t], with degree r>=1 and constant coefficient epsilon=f(0) in {1,-1}.
Put

    f*(t)=t^r f(t^(-1)),
    F_N(t)=t^N f(t)+f*(t),                 N>=1.

Thus F_N is monic of degree N+r and constant coefficient one.
For a nonzero complex polynomial H, write

    m(H)=log|lc(H)|+sum_(H(beta)=0) log max(1,|beta|),
    R_n(H)=|Res(H,t^n-1)|.

Roots in this account always occur with their algebraic multiplicity.
The definition of m includes nonunit leading coefficients and constant polynomials.
The number R_n(H) can be zero.
When H is integral and R_n(H)>0, it is a positive integer.
All logarithms are natural.

Fix an integer k>=1.
For each kth root of unity a set

    Q_a=f*+a f,
    H_k=(f*)^k-(-f)^k=product_(a^k=1) Q_a.                  (1)

This identity follows from product_(a^k=1)(x+a y)=x^k-(-y)^k.
In particular H_k is an integer polynomial.
Actual degrees and leading coefficients in (1) must be used; degree cancellation can occur.

If some Q_a is identically zero, then t^N-a divides F_N for every N, and t^N-a divides t^(kN)-1.
Consequently

    R_(kN)(F_N)=0 for every N>=1.                           (2)

For the present unit seeds, this zero case has the exact description

    Q_a=0  iff  a=-epsilon and f*=epsilon f.

Indeed the coefficient of t^r gives a=-epsilon, after which the polynomial identity is precisely f*=epsilon f.
Therefore H_k=0 iff f*=epsilon f and (-epsilon)^k=1.
We do not assign a finite Mahler measure to the zero polynomial.

Assume for the remainder of Sections 1--5 that H_k is not zero.
Every Q_a is then nonzero.
Denote its actual leading coefficient by c_a, and enumerate all its roots beta_(a,j), allowing roots zero and repetitions.
A constant Q_a contributes its nonzero constant c_a and an empty root list.
Multiplicativity of the resultant, followed by evaluation at the roots of t^N-a, gives

    R_(kN)(F_N)
      = product_(a^k=1) |Res(t^N-a,Q_a)|
      = product_a |c_a|^N product_j |beta_(a,j)^N-a|.        (3)

To check the first equality, t^(kN)-1=product_a(t^N-a), and at each root z of t^N-a one has F_N(z)=a f(z)+f*(z)=Q_a(z).
Interchanging the two arguments of a resultant changes only a sign.
To check the second, factor Q_a=c_a product_j(t-beta_(a,j)) and use that t^N-a is monic.
This also proves (3) when a Q_a is constant or has lower degree than r.
A root beta=0 contributes |0-a|=1, not a missing leading factor.

Put

    D=sum_a deg Q_a=deg H_k <=kr,
    Lambda=sum_a m(Q_a)=m(H_k).                             (4)

The equality of Mahler measures is exact multiplicativity, including the leading coefficients.
The nonzero integer polynomial H_k has Lambda>=0, although an individual complex Q_a need not have nonnegative logarithmic Mahler measure.

Split the root occurrences in (3) into J off the unit circle and U on the unit circle, so D=J+U.
A zero root belongs to the first group.
For each off-circle root set

    rho_beta=|beta|       if |beta|<1,
    rho_beta=|beta|^(-1)  if |beta|>1.

Let rho be the maximum of these finitely many numbers; take rho=0 if J=0.
Thus 0<=rho<1.
Splitting off |beta|^N for exterior roots in (3) gives the exact expression

    R_(kN)(F_N)=exp(N Lambda) E_N
                product_(a,beta: |beta|=1) |beta^N-a|,      (5)

where E_N is a product of factors |1-a^(-1) beta^N| for interior roots and |1-a beta^(-N)| for exterior roots.
Hence

    (1-rho^N)^J <= E_N <= (1+rho^N)^J,
    R_(kN)(F_N) <= exp(N Lambda) 2^D.                       (6)

Empty products are one.
In particular these formulas include J=0, zero roots, and zero resultants caused by unit-circle phases.
Set

    N_h=1                                    if rho=0,
    N_h=max(1,ceil(log 2/(-log rho)))          if 0<rho<1.

For N>=N_h one has E_N>=2^(-J).
A rational or integer certified upper bound for N_h is sufficient in any implementation.

<a id="baseline-phase-selection"></a>
## 2. A finite phase selector on any anchored progression

A nonzero H_k does not alone guarantee a nonzero cyclic resultant: for example a common factor t-1 of f and f* divides every F_N.
We therefore impose the separate, exact hypothesis that an integer N_0>=1 is supplied with

    R_(kN_0)(F_(N_0))>0.                                   (7)

Fix any progression modulus b>=1.
No Salem or irreducibility assumption is needed in this section.

Let L_f be the sum of absolute values of the coefficients of f, and put

    K=2 L_f^k,
    eta=2^(-D) K^(-N_0),
    Q=13/eta.                                              (8)

These are explicit, with K and Q positive integers and 0<eta<=1.
The coefficient norm is submultiplicative, so

    exp(Lambda)=M(H_k)<=||H_k||_1<=2 L_f^k=K.

By (5), (6), and the positive integer bound in (7),

    product_(a,beta: |beta|=1) |beta^(N_0)-a|
          >=K^(-N_0)2^(-J).

If U>0, every other one of the U factors is at most two.
Each single factor is therefore at least K^(-N_0)2^(-(D-1)), hence at least eta.
For U=0 there is no phase condition to check.

For every integer L>=1, apply the elementary simultaneous Dirichlet pigeonhole argument to the U unit complex numbers beta^(bL).
Partition the U-dimensional unit cube into Q^U half-open cubes of side 1/Q and compare its Q^U+1 multiples numbered 0 through Q^U.
Subtracting two in the same cube gives an integer

    1<=q<=Q^U

with |beta^(bLq)-1|<2 pi/Q<eta/2 for every unit root occurrence.
The final strict inequality follows from 4 pi<13.
Repetitions cause no problem; the argument is permitted to use redundant coordinates.
If U=0, simply use q=1=Q^0.
Put

    N=N_0+bLq.

Then

    N_0+bL <= N <= N_0+bL Q^U,
    N congruent to N_0 modulo b,
    |beta^N-a| >= |beta^(N_0)-a|-|beta^(bLq)-1|
                  >eta/2                                 (U>0).   (9)

If N_0+bL>=N_h, (5) now gives

    log R_(kN)(F_N) >= N Lambda-kappa,
    kappa=J log2+U log(2/eta).                              (10)

Thus the selected N are unbounded: their lower bound grows with L, even though values obtained for different L need not all be distinct.
This proves the exact rate

    limsup_(N->infinity; N=N_0 mod b)
           log R_(kN)(F_N)/N = Lambda,                     (11)

with log0=-infinity.
The upper bound is (6), and (10) supplies the matching lower subsequence.
This is a varying-polynomial statement for F_N, not a fixed-input norm asymptotic substituted into a uniform assertion.

The selector is finite as well as existential.
For each chosen L above the stated threshold, search q=1,...,Q^U and test

    R_(kN)(F_N) >= exp(N Lambda) 2^(-J)(eta/2)^U,
    N=N_0+bLq.                                             (12)

At least one test passes.
All quantities on the right are positive real algebraic numbers: M(H_k) is a finite product of moduli of algebraic numbers selected by comparison with one.
Algebraic root isolation and exact real-algebraic comparison suffice in principle.
The left is the absolute value of an integer resultant.
No practical complexity bound, numerical execution, or uniform size bound as f varies is asserted.
More economical selectors may discard redundant phases, but are not needed for (8)--(12).

<a id="delay-return-net-cost"></a>
## 3. The exact generic cost and the actual-core transfer

For any nonzero return, the elementary root estimate

    R_n(F_N)<=2^(N+r) exp(n m(F_N))

gives a lower certificate for m(F_N).
Define its net rate

    Gamma=(Lambda-log2)/k.

Equations (6) and (10) prove

    [log R_(kN)(F_N)-(N+r)log2]/(kN)
        >= Gamma-[kappa+r log2]/(kN)      on the selected N,

    [log R_(kN)(F_N)-(N+r)log2]/(kN)
        <= Gamma+[(D-r)log2]/(kN)         on every nonzero return.
                                                               (13)

Its limsup on the progression is exactly Gamma, again allowing -infinity at zero returns.
A positive constant floor for this certificate along unbounded N needs Lambda>log2.
The selection argument alone does not supply this inequality.

Suppose in addition that, for every sufficiently large N in the progression under consideration, a factorization has been certified

    F_N=P_N C_N,                                           (14)

where P_N is monic irreducible and noncyclotomic and C_N is a monic product of cyclotomic polynomials, with multiplicities permitted.
This is a separate family-specific obligation, not a consequence of (1)--(13).
A factorization known only on a smaller subset does not suffice unless the phase selector is shown to land in that subset.

At a selected N, R_(kN)(F_N)>0, so both factor resultants are positive integers.
Write c_N=deg C_N and d_N=deg P_N=N+r-c_N.
Since every root of C_N has modulus one,

    1<=R_(kN)(C_N)<=2^(c_N).

Exact multiplicativity therefore yields

    log R_(kN)(P_N)-d_N log2
      =log R_(kN)(F_N)-(N+r)log2
         +c_N log2-log R_(kN)(C_N)
      >=log R_(kN)(F_N)-(N+r)log2.                          (15)

The possible cyclotomic loss of norm is paid for by the corresponding reduction of the generic degree cost.
Consequently no bound on c_N is needed for the lower certificate

    m(P_N) >= Gamma-[kappa+r log2]/(kN)                     (16)

at the selected N.
If Gamma>0, all sufficiently large selected N give at least Gamma/2, for example as soon as N>=2(kappa+r log2)/(k Gamma), in addition to the family and hyperbolic thresholds.

Because P_N is monic, irreducible, noncyclotomic and has constant coefficient +/-1, a root alpha_N is a nontorsion algebraic unit.
The norm is exactly R_(kN)(P_N).
In the full ring of integers of Q(alpha_N), its logarithm is

    sum_q f_q ord_q(alpha_N^(kN)-1) log p_q,

over distinct prime ideals with positive valuation.
This is exactly the full arithmetic mass of L G0074, including ramified primes and all valuation depths.
Formula (16) is therefore a certificate in the stated aggregate cyclic-norm sense.
No prescribed set of primes, whole-ring scalar return, or efficient ideal factorization is being claimed.
Any certified subset of valuations is bounded by this full mass and cannot automatically inherit its lower bound.

A separate degree control is essential to call the return linear in the actual irreducible degree.
If c_N<=B on the same progression, then

    d_N=N+r-c_N,
    kN=k d_N+O_(k,r,B)(1),

and the selected core degrees are unbounded.
Moreover, using R_(kN)(P_N)<=R_(kN)(F_N) at nonzero full returns gives the upper bound

    [log R_(kN)(P_N)-d_N log2]/(kN)
       <=Gamma+[(D-r+B)log2]/(kN).                         (17)

Together with (15), this shows that the actual-core certificate has limsup exactly Gamma over the progression restricted to nonzero full returns.
The restriction matters: at other N a cyclotomic factor can make the full resultant zero while the core resultant is still positive.
A hypothesis c_N=o(N) similarly gives d_N/N->1 and the same rate conclusion, without the bounded additive error.

Without either padding control, (16) remains valid but there is no deduction that d_N tends to infinity or that kN is bounded by a fixed multiple of d_N.
If the noncyclotomic part is reducible, the same net-cost calculation applies to that whole product; it does not justify transferring the positive certificate to an arbitrarily chosen irreducible factor.

<a id="seed-measure-ceiling"></a>
## 4. The seed-measure ceiling

On the unit circle, real coefficients give |f*(z)|=|f(z)|.
Thus

    |H_k(z)| <= 2 |f(z)|^k.

Integrating logarithms gives

    Lambda=m(H_k)<=log2+k m(f),
    Gamma<=(m(f)).                                         (18)

Nonzero polynomial logarithms are integrable on the circle; their finitely many zeros cause no obstruction to integrating this almost-everywhere inequality.
Equivalently use the elementary one-variable Mahler integral identity for the root definition.

Consequently even ideal phase selection cannot make this generic net rate uniformly positive while m(f) tends to zero.
This statement holds for each k separately and also pointwise if k is allowed to vary with f.
For actual cores, the conclusion about the asymptotic rate uses the padding control in (17); without that control one must not substitute Gamma for the core certificate's actual rate.
Nor does (18) by itself rule out exceptional finite N or other archimedean costs.
It locates the limit of this specific generic d log2 transfer mechanism.

<a id="bounded-phase-occurrence-boundary"></a>
## 5. Root-count cost of the all-unit-phase mechanism

The phase selector is explicitly finite for each fixed seed, but that is not a uniform bound on its phase list as seeds vary.
The following elementary count identifies a restriction on the case where all nonzero roots in (3) are on the unit circle.

Suppose f is not reciprocal up to sign, so

    h=f*-epsilon f !=0.

Its constant and leading coefficients vanish.
Let ell=ord_0(h)>=1, where reversal is temporarily taken with ambient degree r.
Then

    t^r h(t^(-1))=-epsilon h(t),
    deg h=r-ell,
    1<=ell<=r/2.

If (-epsilon)^k=1, expand

    H_k=(epsilon f+h)^k-(-f)^k.

The j=0 term cancels.
The j=1 term k epsilon^(k-1) f^(k-1)h has degree kr-ell and order at zero ell.
Each term with j>=2 has strictly smaller degree kr-j ell and strictly larger order j ell.
There can be no cancellation at the two extreme surviving coefficients.
Hence

    deg H_k=kr-ell,
    ord_0(H_k)=ell,
    number of nonzero root occurrences =kr-2ell >=(k-1)r.

The other parity case is epsilon=1 and k odd.
Here the leading and constant coefficients of H_k are both two, so its degree is kr and its order at zero is zero.
Thus in all cases, for k>=2,

    number of nonzero root occurrences of H_k >=(k-1)r.     (19)

If all these roots have modulus one, then U is exactly their count.
A bounded U therefore forces bounded r when k>=2.
This concerns root occurrences, not the dimension of their generated compact torus: repeated roots and multiplicative relations can reduce the number of independent phases.
If some roots are off the circle, (19) does not supply a lower bound for U alone; the remaining roots instead affect J, rho, and the hyperbolic threshold N_h.
No uniform separation of rho from one is proved.

<a id="near-one-seed-reciprocal-degeneration"></a>
## 6. Near-one seeds give exact reciprocal degeneration

Let theta_0>1 be the positive real root of t^3-t-1.
Use precisely the retained Smyth statement that every nonzero nonreciprocal algebraic integer has Mahler measure at least theta_0.
As in the existing source audit, its sharp-bound proof is an accepted external input.

If the present monic unit seed satisfies M(f)<theta_0, factor f over Z into monic irreducibles, counted with multiplicity.
Every factor g is a unit polynomial since their integer constant coefficients multiply to epsilon.
Its Mahler measure satisfies

    1<=M(g)<=M(f)<theta_0.

No such factor can be nonreciprocal by the stated theorem.
For a monic irreducible unit factor, reciprocal up to sign means exactly g*=g(0)g, by comparing leading coefficients.
Multiplying these identities gives

    f*=epsilon f,
    F_N=f(t)(t^N+epsilon).                                 (20)

The second factor is a monic product of cyclotomic polynomials.
The noncyclotomic part of F_N is exactly that of the original fixed seed f, including multiplicities, for every N.
Thus this use of delay cannot produce unbounded noncyclotomic degree from that seed.
This argument allows reducible seeds and includes cyclotomic factors; irreducibility of f was not used.

There is also exact return bookkeeping.
If epsilon=-1, t^N-1 divides F_N and every full R_(kN)(F_N) is zero.
If epsilon=1 and k is even, t^N+1 divides both F_N and t^(kN)-1, giving the same zero result.
If epsilon=1 and k is odd, then

    H_k=2 f^k,
    Lambda=log2+k m(f),
    R_(kN)(F_N)=2^N R_(kN)(f).                             (21)

For the last identity, every root z of t^N+1 has z^(kN)=-1, so |z^(kN)-1|=2 and its resultant is 2^N.
When the resultants are nonzero, the full-polynomial certificate becomes exactly

    [log R_(kN)(F_N)-(N+r)log2]/(kN)
      =[log R_(kN)(f)-r log2]/(kN).                         (22)

The added norm 2^N cancels the added degree cost N log2.
Thus this positive-looking exponential norm is precisely cyclotomic padding; the remaining arithmetic question is the original seed at a longer return time.
If a seed has full returns zero because of its own cyclotomic factors, (20) still proves the core identity, while (22) is used only at nonzero returns.

Equivalently, every nonreciprocal monic integral unit seed has M(f)>=theta_0, by the same factorwise argument.
This is a seed obstruction, not a claim that all irreducible factors of arbitrary delay polynomials have measure at least theta_0.

<a id="fixed-seed-limit-and-scope"></a>
## 7. The fixed-seed measure limit and the remaining boundary

For completeness the already retained Lawton interface shows

    m(F_N) -> m(f) as N->infinity                           (23)

for every fixed seed here, whether reciprocal or not.
Indeed let

    G(x,y)=y f(x)+f*(x).

For |x|=1 outside the finitely many roots of f, Jensen's one-variable formula in y gives

    integral_(|y|=1) log|y f(x)+f*(x)|
        =log max(|f(x)|,|f*(x)|)=log|f(x)|.

The iterated integral is justified directly: away from those finitely many x one can write log|G|=log|f(x)|+log|y+u(x)| with |u(x)|=1.
The first term has integrable absolute value in x, and the absolute integral of the second over y is finite and independent of u by rotation.
Fubini therefore applies and m(G)=m(f).

Specializing (x,y)=(t,t^N) gives F_N.
The integer relations on the vector (1,N) are nonzero multiples of (N,-1), so the exact sup-norm relation parameter is N.
The accepted Lawton theorem, including the case of torus zeros, gives (23).
No effective rate is imported or proved by this step.

If (14) holds, cyclotomic factors have measure one, so (23) also gives m(P_N)->m(f).
A fixed nonreciprocal seed therefore has limiting measure at least theta_0>1 for that unique noncyclotomic core.
A reciprocal near-one seed instead has the exact degeneration (20).
These two facts explain why the fixed plastic-seed success cannot be promoted to coverage of all near-one cores by merely replacing its seed and repeating the same fixed-seed delay construction.

What has not been proved is a uniform theorem when the seed varies with N, a bound on every factor when several noncyclotomic factors occur, exclusion of exceptional finite delays, or failure of other return exponents or sharper archimedean costs.
In particular the conclusions do not establish a Lehmer gap, an all-input arithmetic coverage theorem, or a solution of G0001.

For this route the concrete remaining choices are now separated: verify a nonzero anchored return and Lambda>log2 for a particular seed; independently certify the actual noncyclotomic factorization and padding bound if linear actual-degree cost is wanted; or change the construction/core-selection mechanism when approaching near-one inputs.
Phase optimization within the present fixed-seed construction does not remove (18), (20), or the fixed-seed limit (23).




The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0040_v1.md#contributions-and-actual-review), with its original inspected scope and relationship.
