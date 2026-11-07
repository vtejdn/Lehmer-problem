---
author: Yin
---

# MV226-U001: elementary mechanisms, companion-code checks and source-use limits

<a id="mv226-u001"></a>
## Inspected edition and scope

This inspection uses [Version 1.0 at the fixed 25cfec7 edition](readme.md#edition-1-0-25cfec7).
On 2026-11-07 the coordinating agent for Yin read the complete README, lines 1--362, the complete `lehmer.py`, lines 1--476, and the complete `test_lehmer.py`, lines 1--213.
The opening license statement was checked to identify the text/code licenses.
The elementary arguments in Sections 2--3 and the integer bounds in Section 11 were checked mathematically, and the companion's integer and numerical paths were inspected separately.
The source's own tests and the targeted checks below were executed with CPython 3.13.15.

The review context includes the earlier discussion of this source and existing local corrections.
This is an ordinary agent source inspection with direct checks, not a separately isolated independent review, a formal verification or a new project Claim assessment.
Reading all of this short exposition does not constitute recursive proof review of its bibliography.
The later sections' reported theorems, examples and current-status assertions retain the specific limits below.

The source attributes the work to MV2 of Munim, Inc.
Yin is the author of this local inspection, not the author of the external work.

<a id="mv226-conventions"></a>
## Normalization and existing definitions

The domain is nonzero integer polynomials, with all roots counted with multiplicity and natural logarithms for total logarithmic measure.
Use the complete [Mahler/height normalization](../Smy08/Yin_U001.md#smy08-height-normalization), including the primitive integer minimal polynomial and its leading coefficient for an algebraic number.
The source's multiplicative quantity is M(P), while the project generally writes m(P)=log M(P).
Its fixed-degree minimum denoted m_n in Section 2(f) is a minimum of multiplicative measures and must not be confused with this project notation.
The source's reciprocal convention allows P*=P or P*=-P; reversal in Section 2(b) assumes P(0) is nonzero.
The code removes powers of x before testing reciprocity or Kronecker's criterion.
These removals preserve measure but are not the literal reversal operation on a polynomial with zero constant term.

The [existing Salem convention](../Smy08/Yin_U003.md#smy08-salem-number) supplies the complete definition and degree qualification.
A small real root alone is not a small Mahler measure, and a bound for Salem numbers alone is not an established reduction of the unrestricted project target.

<a id="mv226-graeffe-transform"></a>
## Graeffe root squaring and the exact elementary bounds

For a nonzero polynomial P in Z[x] of degree n, write

\[
 P(x)=E(x^2)+xO(x^2),\qquad
 G(P)(y)=(-1)^n\bigl(E(y)^2-yO(y)^2\bigr).
\]

This defines the Graeffe root-squaring transform used in Sections 2(g), 3 and 11 and in `lehmer.py` lines 177--194.
If P has leading coefficient a_n and roots alpha_i, then

\[
 G(P)(x^2)=(-1)^nP(x)P(-x)
             =a_n^2\prod_i(x^2-\alpha_i^2),\qquad
 M(G(P))=M(P)^2.
\]

The source's sign, leading coefficient, preserved degree and root multiplicities were checked directly in this identity.
In particular, this forward integer construction doubles m(P); it does not supply an inverse integer construction that halves arbitrary measures.

Sections 2(a)--2(f) give valid multiplicativity, reversal, coefficient and Landau arguments at their stated domains.
For the coefficient bound, each elementary-symmetric summand has modulus at most the product of max(1,|alpha_i|), and there are binomial(n,j) relevant summands.
For Landau, apply the concavity of log to |P|^2 and then Parseval, using the scalar Jensen integral with its integrable unit-circle logarithmic singularities.
The scalar Jensen identity and irreducibility of cyclotomic polynomials are standard inputs, rather than additional proofs supplied by this exposition.
The finite coefficient box proves fixed-degree finiteness and existence of the fixed-degree minimum; its size depends on n.

For k>=0 let Q=G^k(P), after optional removal of a power of x, and let n>=1 be its degree.
Define the exact real expressions

\[
 A=\max_{0\le j\le n}\frac{|Q_j|}{\binom nj},\qquad
 B=\left(\sum_{j=0}^nQ_j^2\right)^{1/2}.
\]

The proved enclosure is

\[
 2^{-k}\log A\ \le\ m(P)\ \le\ 2^{-k}\log B.
\]

Since |Q_j|<=A binomial(n,j), one has B/A<=sqrt(binomial(2n,n))<2^n.
Thus the logarithmic width is less than n log(2)/2^k, as claimed in Section 11.
These are exact mathematical inequalities; the returned floating-point endpoints require the separate qualification below.
Constants have measure equal to their absolute integer value and are handled separately.

<a id="mv226-kronecker-algorithm"></a>
## Kronecker's theorem and the terminating integer test

For monic P with P(0) nonzero and all roots in the closed unit disk, every iterate G^k(P) stays monic, integral and within the same binomial coefficient box.
A repeated polynomial supplies a permutation of the powered root multiset; iterating that permutation shows that every nonzero root is a root of unity.
This checks the source's Section 3 proof and yields the measure-one classification after removing zero roots and normalizing an initial leading coefficient of minus one.

The code's initial leading/constant coefficient tests are necessary for M(P)=1.
After those tests, the two possible termination mechanisms are valid.
For a measure-one input, root squaring eventually removes the 2-primary parts of all root orders and fixes the resulting multiset of odd-order cyclotomic roots.
For a positive-measure input, M(G^k(P))=M(P)^(2^k) eventually exceeds 2^n, whereas Landau bounds a polynomial inside the binomial box by sqrt(binomial(2n,n))<2^n.
Consequently some coefficient exits the box and the test rejects.
A fixed point with nonzero constant coefficient has all root moduli equal to one, because its positive largest and smallest moduli satisfy r^2=r.
The termination argument is degree/input dependent; the source's informal phrase about a handful of squarings is not a uniform complexity theorem.

The exact division and cyclotomic-product routines were also inspected.
Their finite cyclotomic candidate range uses phi(m)>=sqrt(m/2), hence phi(m)<=n implies m<=2n^2.
This elementary estimate follows prime-power by prime-power from phi(m)^2/m: the factor from 2 can be 1/2, and every odd-prime factor is at least one.
The test suite's degree-at-most-four comparison checks all coefficient lists with leading coefficient plus or minus one and lower coefficients in {-1,0,1}, rather than all integer polynomials of those degrees.

<a id="mv226-pierce-numbers"></a>
## Pierce numbers, determinant convention and asymptotic limits

For a monic P in Z[x] of degree n with roots alpha_i and an integer k>=1, define the Pierce number in the source's convention by

\[
 \Delta_k(P)=\prod_{i=1}^n(\alpha_i^k-1)
            =\operatorname{Res}(P,x^k-1).
\]

It is an integer, and a root of unity can make it zero for some k.
Let C_{P,k} be the integer matrix of multiplication by P on Z[x]/(x^k-1), in the basis 1,x,...,x^(k-1).
Evaluation at the k-th roots of unity gives

\[
 \det C_{P,k}=\prod_{\zeta^k=1}P(\zeta),\qquad
 \Delta_k(P)=(-1)^{nk}\det C_{P,k}.
\]

The sign is needed when nk is odd.
README lines 131--133 omit it in their determinant description; `lehmer.py` lines 352--368 state and implement it correctly.
For P=x-2 and k=1, the determinant is -1 while Delta_1=1.
The Bareiss implementation uses integer arithmetic and row-pivot signs, and the source tests reproduce the Mersenne and Lucas controls.

When no root is on the unit circle, the elementary factor limits give |Delta_k|^(1/k)->M(P).
An extension allowing unit-circle roots requires that none be roots of unity and uses the source's named Diophantine lower bounds.
Those Gelfond/Baker original proofs were not audited here.
The extension must not be applied to a polynomial with a root-of-unity factor or treated as an effective uniform convergence estimate.

<a id="mv226-actual-code-checks"></a>
## Actual companion runs and their mathematical limits

From the [fixed local original directory](../../../literature/pdf/MV226/25cfec788c330430968048a3f95a88e2d952f440/), the command `python -B -m unittest -v test_lehmer` completed with all 27 tests passing on CPython 3.13.15.
The CLI error messages within `TestCli.test_commands` are expected test cases.
This run is a reproducible source-program check, not an independent proof of every numerical claim in the README.
Only this Python runtime was tested; compatibility with every advertised Python version was not verified.

The separate direct calls reproduced 243 enumerated degree-ten reciprocal inputs, 16 entries selected numerically by `small_measures(..., limit=1.3)`, and a smallest reported measure approximately 1.1762808182599174.
The source's degree-at-most-six nonreciprocal enumeration tested 650 inputs and reported a minimum approximately 1.3247179572447452.
The exact Kronecker test distinguishes M=1, but the ordering of positive measures and comparison with 1.3 are double-precision computations.
These runs do not supply exact separation certificates for the complete finite search or an arbitrary-degree lower bound.

`roots` returns after a tolerance condition or its iteration limit without a certified residual enclosure.
`root_profile` uses a tolerance band of width 10^-6 and labels the resulting circle count as numerical.
Neither this count nor midpoint quadrature for Jensen's integral proves that a root lies exactly on the unit circle.
Cyclotomic factors are removed exactly before `mahler_measure`, but the remaining positive measure is computed numerically.

<a id="mv226-resultant-error"></a>
## Confirmed arithmetic error: powered minimal polynomials lose multiplicity

README Section 6, lines 171--172, claims p^d divisibility for the resultant of the minimal polynomials of alpha and alpha^p for every prime p.
This is the same literal error already resolved at [Smy08's multiplicity correction](../Smy08/Yin_U001.md#smy08-resultant-multiplicity).
Its exact counterexample alpha=sqrt(2), p=2 has

\[
 \operatorname{Res}(t^2-2,t-2)=2\notin4\mathbb Z.
\]

Reuse that existing complete correction with all d powered conjugates, including multiplicity, or separately establish degree preservation.
No new copy of its proof or new Claim is needed.
The error concerns this stated arithmetic interface, not a refutation of Dobrowolski's theorem.

<a id="mv226-floating-certification-error"></a>
## Confirmed code error: returned endpoints are not certified enclosures

`mahler_bounds`, lines 225--243, computes the valid integer expressions above but applies ordinary floating-point log and exp without outward rounding.
Its constant branch also converts an arbitrary integer directly to float and returns that value as both endpoints.
The tests at `test_lehmer.py` lines 137--150 permit errors of 10^-12 or use approximate equality, so they do not check literal containment.

The following direct calls in the original directory reproduce the issue without modifying the source:

```python
import lehmer as L
for p, exact in (([-3, 1], 3), ([2**53 + 1], 2**53 + 1)):
    lo, hi = L.mahler_bounds(p)
    print(repr(lo), repr(hi), exact, lo <= exact <= hi)
```

The observed CPython 3.13.15 output was

```text
2.9999999999999996 2.9999999999999996 3 False
9007199254740992.0 9007199254740992.0 9007199254740993 False
```

The first true measure is M(x-3)=3, and the second is the exact absolute value of the nonzero constant polynomial.
Thus the function's universal certified-interval promise is false even on elementary allowed inputs, despite the 27 passing tests.
Keep the exact integer inequalities or supply rigorously outward-rounded endpoints before using such output as a certificate.
The original files are retained without a local patch that could obscure which version was checked.

<a id="mv226-secondary-results-and-updates"></a>
## Secondary results, source updates and non-adopted breadth

Sections 5--10 and the complete source list were read as reports of external results and problem status.
For the nonreciprocal bound, height normalization, house comparison and degree-dependent estimates, reuse the inspected statements and original-proof limits in [Smy08-U001](../Smy08/Yin_U001.md#smy08-u001) and [Smy08-U002](../Smy08/Yin_U002.md#smy08-u002).
The quantitative table's constants, asymptotic ranges and small-degree conventions are not newly certified merely by its presence in MV226.
The Voutier primary abstract at [arXiv:1211.3110](https://arxiv.org/abs/1211.3110) was checked at statement scope in the preliminary comparison, not as a review of its original proof.

The [Mossinghoff--Rhin--Wu primary abstract](https://doi.org/10.1080/10586458.2008.10128872) confirms the even-degree-through-54 minimum calculation and the M<1.3 enumeration through degree 44 at its stated primitive irreducible domain.
The algorithms, numerical certificates and complete minimum tables were not independently reproduced here.
The [Sac-Epee v3 text](https://arxiv.org/html/2409.11159v3), Sections 2--3, was checked for its random separator/integer-programming method and reported recovery of 47 known Salem numbers below 1.3 plus 10 new examples between 1.3 and 49/37.
That search is not a new exhaustive certification through all degrees up to its sampling limit.

README Section 7, lines 207--208, gives an outdated degree-72 description of known small-measure lists.
The [current MMD26 primary README](https://github.com/mossinghoff/Mahler-Measure-Database) read on 2026-11-07 describes known examples through degree 200.
Reuse the [existing bounded primary-table inspection](../../../ledger/Yin_L_G0133_v11.md#bounded-small-measure-source-screen) for the distinction between those known-example lists and reported completeness through degree 44.
Neither description certifies all degree-200 inputs or a new record below Lehmer's value.

The [Annals publisher record](https://annals.math.princeton.edu/articles/22975) was checked and lists Dimitrov's work as forthcoming, revised 2026-06-11 and accepted 2026-08-27.
The article's 2019 preprint pointer does not reflect this later publication status.
The publisher statement concerns the house-scale problem; it does not supply the unrestricted total Mahler gap.
The accepted revision's full proof was not compared with the 2019 edition here.

The single-polynomial entropy sentence in Section 8 does not specify the finite-dimensional or algebraic-presentation hypotheses under which such a formula is being used.
It is not accepted here as an unconditional representation theorem for every finite-entropy automorphism of an arbitrary compact abelian group.
The following all-values/countable dichotomy and its original Lind proof were not newly audited.
The [existing DGB16 spectral boundary](../DGB16/Yin_U004.md#exact-auxiliary-interfaces-used-in-the-realization-proof) remains in force; this exposition does not resolve that local original-source obligation.
This is a limit on adoption, rather than a claim that a counterexample to the unrestricted entropy sentence has been constructed.

The topology, surface dynamics, multivariable identities, elliptic analogues, claimed-proof reception and other 2026 research announcements remain source-reported background unless an adequate existing primary inspection is selected by an actual consumer.
No blanket proof, novelty, priority or current-status certification is inferred for them from this audit.
The source itself disclaims progress on the unrestricted conjecture.

<a id="mv226-project-use-boundary"></a>
## Permitted reuse and project boundary

The elementary definitions, checked root-squaring/Kronecker mechanisms and exact pre-rounding inequalities can be reused at the explicit domains above.
The defective powered-minimal-polynomial assertion and literal floating-point enclosure promise cannot be used as proof inputs.
Finite numerical minima, approximate root profiles and a passing source test suite must retain their actual computational limits.
An actual Claim consumer owns any later applicability check and adoption; this unit selects no project assessment or strategy.
The [unrestricted Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract) and its human-directed pause are unchanged by this literature assignment.
This source provides no new automatic auxiliary supply, actual sublinear-degree factor sequence or repeatable integer measure-halving construction.
