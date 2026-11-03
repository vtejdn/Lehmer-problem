---
author: Yin
---

<a id="mat96-u001"></a>
# Mat96-U001: the finite confluent determinant interface and its domain guards

Date: 2026-10-07.
Narrow source-interface inspection by assigned AI ms25_source for Yin during G0001.
The coordinator independently read the principal source pages, identified the torsion correction, and reviewed the complete assembled account.
The actual contribution and review relationships are recorded below.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Mat96, [retained PDF](../../../literature/pdf/Mat96.pdf): Russian published original, Matematicheskie Zametki 59(3) (1996), 415--420, six PDF pages, 166389 bytes. No comparison with the English translation is asserted.

Passages: Printed 415--418 / PDF pp.1--4: opening standing assumption; definition of Omega and Theorems 1--2; Lemmas 1--4; divided derivatives; complete finite arithmetic/Hadamard chain (5)--(7); and the opening single-prime specialization on p.418.

Inspection: 2026-10-07, human author Yin; assigned AI ms25_source directly read the rendered original and checked the complete finite chain, normalization and domain counterexample. The coordinating AI read the complete account and independently checked the arithmetic and normalization; the torsion correction was its contribution and is coauthor self-review for that part. Prime asymptotics, the effective/asymptotic threshold, the original cited proofs and the degree-reduction lemmas on pp.418--420 are outside the audited scope.


**Audited within scope** for the finite construction (5)--(7) with the explicit non-torsion and selected-prime degree hypotheses below.
**Questioned** for the literal torsion-inclusive Theorem 2, with its precise corrected interface retained.
Theorem 1's adopted degree-at-least-two scope remains unchanged; no full-paper audit is asserted.

This unit supplies the source-normalized determinant interface to [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), its primary [algebraic-entropy route](../../../strategies/Yin_S_G0001.md#entropy-gap-route) and supporting [arithmetic route](../../../strategies/Yin_S_G0004.md#arithmetic-resultant-route).
The separate local construction and uniform-ceiling arguments belong to [L G0057](../../../ledger/Yin_L_G0057_v1.md) and [L G0058](../../../ledger/Yin_L_G0058_v1.md); those deductions do not upgrade the uninspected source asymptotics.

## Source, locators and actual inspection

The artifact is the retained Russian original [Mat96.pdf](../../../literature/pdf/Mat96.pdf): E. M. Matveev, *On a connection between the Mahler measure and the discriminant of algebraic numbers*, Matematicheskie Zametki 59(3) (1996), 415--420.
Printed page equals one-based PDF page plus 414.

The inspected passages are printed 415 for the standing assumptions; 416 for Omega, Theorems 1--2, Lemmas 1--3 and the normalized derivative definition; 417 for Lemma 4 and equations (3)--(7); and the opening of 418 for the single-prime specialization and the proof boundary of the asymptotic step.
Pages 419--420 were viewed for orientation but their degree-reduction lemmas and proofs are not audited here.

The source images were read directly.
Existing renders `tmp/g0001-mat96-general-2.png` and `tmp/g0001-mat96-proof-3.png` through `-6.png` supplied pages 416--420.
The author rendered page 415 to `tmp/g0001-mat96-interface-1.png` and inspected the complete page.
The mathematical source is the retained PDF; these images record the actual visual inspection.
There was no new source acquisition or web search.

This inspection strengthens the selected equation-(7) reading already recorded in [L G0015](../../../ledger/Yin_L_G0015_v1.md).
It does not claim an audit of the full paper, the original Dobrowolski/Cantor--Straus/Meray proofs, or the prime asymptotics in (3)--(4).

<a id="mat96-normalized-confluent-interface"></a>
## Exact normalization: the factorials are already divided out

On printed 416 the source defines, for a chosen positive integer N,

    v(x)=(1,x,x^2,...,x^(N-1)),
    v_n(x)=v^(n)(x)/n!,              n=0,1,2,... .           (A)

For points x_1,...,x_m and positive multiplicities n_1,...,n_m with sum_i n_i=N, V(x,n) is the determinant with the rows v_n(x_j), 0<=n<n_j, in successive point blocks.
In column r, indexed from zero, its entry is

    binomial(r,n) x_j^(r-n),

interpreted as zero when r<n.
Thus these are divided derivatives, not unnormalized derivatives and not powers of x d/dx.

Printed 417, Lemma 4, states exactly

    V(x,n)=product_(i<j) (x_j-x_i)^(n_i n_j).              (B)

There is no omitted factorial in (B).
A direct verification of the normalization is to replace each point block by distinct points x_i+epsilon y_0,...,x_i+epsilon y_(n_i-1) in the ordinary Vandermonde.
Divide by each within-block Vandermonde in epsilon y_j and let epsilon tend to zero.
Taylor's coefficient v^(n)(x_i)/n! yields (A); the surviving cross-block factors are precisely (B).
This local check does not claim to inspect Meray's original proof, cited as [6].

If ordinary derivative rows v^(n) were used instead, the determinant would acquire product_i product_(n=0)^(n_i-1) n!, and its square would acquire the square of that factor.
Such a convention cannot be mixed with (B).
In the source's normalization the determinant and the Hadamard estimate are compatible.

<a id="mat96-finite-multiprime-formula"></a>
## The exact finite construction and printed equations (5)--(7)

The safe finite interface is as follows.
Let alpha be a nonzero algebraic integer which is not a root of unity, let P be its monic minimal polynomial of degree d, and let alpha_1,...,alpha_d be the conjugates.
Choose distinct primes p_1,...,p_S such that deg(alpha^(p_s))=d for every selected prime.
Take integers k,S>=1, put p_0=1, and set

    x_(sd+j)=alpha_j^(p_s),     j=1,...,d,  s=0,...,S,
    n_(j)=k for s=0,           n_(sd+j)=1 for s>0,
    N=d(k+S),
    f(S)=sum_(s=1)^S log p_s,  g(S)=sum_(s=1)^S p_s.

The source uses the first S primes (p_1=2).
The same finite argument works for any distinct selected primes satisfying the displayed degree conditions.
That extension concerns only this finite formula; it does not import the source's prime asymptotics for arbitrary sets.

Let Delta=abs(disc P), delta(alpha)=d/Delta^(1/d), and M=M(alpha).
The transcription of printed 417 equation (5) is

    |V(x,n)|^2 <= [d(k+S)]^[d(k^2+S)]
                         M^[2d(k+S)(k+g(S))].            (5)

Here the brackets enclose bases and exponents, not floor functions.
Equation (6) states that the positive integer |V|^2 is divisible by

    Delta^(k^2+S) product_(s=1)^S p_s^(2dk)
      =Delta^(k^2+S) exp(2dk f(S)).                       (6)

The printed equation (7), for any auxiliary delta>=delta(alpha), is

    log M >= [2k f(S)-(k^2+S)log((k+S)delta)]
                  /[2(k+S)(k+g(S))].                    (7)

All logarithms are natural.
The finite formula needs no asymptotic threshold and delta is any positive number above the actual parameter.
The numerator may be nonpositive, in which case this particular lower bound supplies no positive gap.
Degree d cancels in (7), but the actual discriminant parameter is not thereby bounded.

## Nonvanishing and simultaneous arithmetic divisibility

The following verifies the complete finite arithmetic chain rather than multiplying unrelated divisibility statements.

First, if alpha_i^a=alpha_j^b for positive integers a!=b, choose a Galois automorphism sigma of a splitting field sending alpha_i to alpha_j.
From alpha_i^a=sigma(alpha_i)^b, induction gives alpha_i^(a^r)=sigma^r(alpha_i)^(b^r).
Taking r equal to the finite order of sigma would make alpha_i^(a^r-b^r)=1.
This contradicts the non-torsion hypothesis.
Therefore distinct exponent blocks have no common root.
Within a selected prime block the roots are distinct by its degree-preservation assumption.
The original block is separable in characteristic zero.
All points x_i are consequently distinct, and (B) gives V!=0.

For each selected prime set

    P_s(t)=product_(j=1)^d (t-alpha_j^(p_s)).

It is monic integral.
Its d factors, including any possible multiplicities in the Frobenius congruence argument, must not be replaced prematurely by a powered root's minimal polynomial.
Under the selected degree condition it is in fact squarefree of degree d.
The product

    U_s=product_(i<j)
              (alpha_j^(p_s)-alpha_i^(p_s))/(alpha_j-alpha_i)

is a nonzero integer.
Each quotient is a polynomial in the roots; the whole product is symmetric, and hence an integer polynomial in the elementary symmetric functions.
Therefore

    abs(disc P_s)=Delta U_s^2,

so Delta divides each powered discriminant.

Next P_s=P modulo p_s by Frobenius on the elementary symmetric functions.
Write P_s=P+p_s R_s with R_s integral.
Taking the norm of P_s(alpha)=p_s R_s(alpha) proves

    p_s^d divides Res(P,P_s).

The resultant is nonzero by the distinct-exponent argument.
This is the source's Lemma 2 with its complete multiplicity normalization, and the same interface used in L G0012 and L G0015.

Finally, (B) grouped by exponent blocks gives the exact factorization

    |V|^2
      = Delta^(k^2) product_s abs(disc P_s)
          product_s abs(Res(P,P_s))^(2k)
          product_(s<t) abs(Res(P_s,P_t))^2.               (C)

Each last resultant is a nonzero integer.
Substitution of the two preceding divisibilities into the separate factors of (C) proves the entire product divisibility (6), even when Delta has prime divisors in common with the selected primes.
No invalid inference from “each factor separately divides V” to “their product divides V” is required.
Equivalently V^2 is an integer by symmetry in the original conjugates, and |V|^2=abs(V^2) is a positive integer.

The source's use of all-prime Omega is sufficient but stronger than necessary for this finite step: only the selected primes need degree preservation.
Non-torsion is separately indispensable for the cross-block nonvanishing argument.

## Hadamard's bound and the harmless discarded factorial improvement

For 0<=nu<k the squared norm of the divided-derivative row at a base root alpha_i is at most

    N^(2nu+1)/(nu!)^2
        *max(1,abs(alpha_i))^[2(N-1-nu)],

using binomial(r,nu)<=N^nu/nu! and at most N terms.
A simple row at alpha_i^(p_s) has squared norm at most

    N max(1,abs(alpha_i))^[2p_s(N-1)].

Multiplying all these bounds in Hadamard's inequality actually gives

    |V|^2 <= N^[d(k^2+S)]
        *M^[2(N-1)(k+g(S))-k(k-1)]
        /(product_(nu=0)^(k-1) nu!)^(2d).                 (D)

The source's (5) follows by discarding the denominator, replacing N-1 by N, and discarding the nonnegative subtraction k(k-1).
These relaxations are valid because M>=1 for an algebraic integer.
Thus the absence of a factorial in (5) is a weaker upper bound, not a normalization defect.
Formula (D) is a direct check of the printed estimate, not a claim that the source printed the refinement.

Taking logarithms of (5)--(6), dividing by d and using log Delta=d(log d-log delta(alpha)) cancels the two d log d terms and yields (7) with delta(alpha).
Increasing that parameter to delta decreases the right side, proving the stated auxiliary-delta scope.
The denominator is 2(k+S)(k+g(S)); there is no remaining factor d or hidden normalization by degree in log M.

<a id="mat96-torsion-guards"></a>
## Actual source omissions and the adopted corrections

The opening of printed 415 specifies only a standing assumption alpha!=0.
It does not impose non-torsion or degree at least two on all subsequent statements.
Printed 416 defines Omega as the nonzero algebraic integers satisfying deg(alpha^p)=deg(alpha) for every prime p.
The literal definition includes alpha=1 and alpha=-1.

The printed Theorem 2 assumes p>2 prime, alpha!=0 integral, deg(alpha^p)=deg(alpha), and delta(alpha)<=1, and concludes

    log M(alpha)>=log(p/2)/[2(p+1)].                       (E)

It omits the non-torsion condition required by its determinant proof.
The explicit counterexample to the literal statement is alpha=i, p=3: the degree is two for both i and i^3, Delta=4, delta(alpha)=1, and log M(alpha)=0, while the right side of (E) is strictly positive.
Here the two root blocks actually coincide, so V=0.

The corrected adopted interface adds that alpha is not a root of unity.
With k=S=1 and one good prime p, (7) then gives

    log M(alpha)>=log(p/(2delta))/[2(p+1)],

and delta=1 proves (E) on its corrected domain.
This is already the explicit non-torsion domain of L G0015's independently complete finite-prime proof; that retained result needs no mathematical correction.

For Theorem 1 the needed proof-interface guard is to exclude the torsion elements of Omega.
The already accepted Smy08-U003 scope uses degree d>=2, which excludes the two elements +/-1 and preserves the source's intended nonvanishing argument.
We do not claim that the preceding observation alone refutes Theorem 1's literal existential-threshold statement: a special choice delta_0=e makes its right side zero on +/-1.
The precise finding is that its printed determinant argument and large-auxiliary-delta application must not be used for those elements.
The local non-torsion/d>=2 guards avoid that issue without a claim about an uninspected erratum.

The source's Omega condition is explicitly about every prime exponent.
Nothing in the inspected passage upgrades it to preservation under every composite exponent; that stronger condition is unnecessary for (5)--(7).

## Remaining external boundaries and review

Printed 417 also states f(S)=(1+o(1))S log S and g(S)=(1/2)(1+o(1))S^2 log S for the first S primes.
Printed 418 selects k=floor(log delta/log log delta), S=floor(k^2/2) to pass to Theorem 1.
Those asymptotic estimates and the resulting threshold are outside this finite-interface audit.
We supply no effective delta_0, no uniform bound on delta(alpha), and no new Lehmer gap.

The author checked the source's divided derivatives, determinant identity normalization, complete arithmetic factorization, nonvanishing, row-norm exponents, factorial relaxation, auxiliary delta direction, and the single-prime counterexample.
It also read the opening page to rule out a silently inherited non-torsion hypothesis.

The coordinator read and checked the complete assembled account, including the normalized confluent determinant, simultaneous discriminant/resultant divisibility, nonvanishing, full row-bound exponents, and every domain guard.
It found no mathematical gap at the stated scope.
The coordinator supplied the Theorem 2 torsion correction; its check of that portion is coauthor self-review, while the assigned author independently inspected the original and checked the counterexample and absence of a standing exclusion.
The coordinator's remaining proof-interface checks are independent review of the author's account.
No human or formal verification, full-paper audit, or original-reference proof audit is asserted.
