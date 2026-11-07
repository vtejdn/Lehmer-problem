# Finite certificates for the original Lehmer return core

This part of the attachment verifies the computational premise of the report's theorem on the original Lehmer return core, labelled `ret:lehmer-core`, and the finite compact-termination input reused in `ret:linear-control`.
The polynomial is

\[
 P(t)=t^{10}+t^9-t^7-t^6-t^5-t^4-t^3+t+1.
\]

Write \(\beta>1\) for its expanding root, \(S=\beta/(\beta-1)\), and

\[
 \rho(a)^2=\sum_{j=1}^4 |a(\zeta_j)|^2,
 \qquad
 K_8=\{a\in\mathbb Z[\beta]:|a(\beta)|\leq1,
       |a(\beta^{-1})|\leq S,\ \rho(a)<8\},
\]

where the \(\zeta_j\) are the four upper unit-circle conjugates.
The checked conclusion is that the report's neutral descent is valid and every actual point of \(K_8\) has an original-digit path to zero of length at most 25.
The report supplies the subsequent arguments for arbitrary neutral radius, reciprocal reachability, the full return-core strip and its lattice growth.
Those analytic and lattice arguments remain distinct from this finite computation.

## Portable files and command

Copy these three files into the same directory:

- [verify_return_core.py](verify_return_core.py), the separately implemented and commented verifier;
- [return-core.json](return-core.json), the exact word supports, rational axis targets and enclosing-ellipsoid data;
- [return-paths.bin.gz](return-paths.bin.gz), the necessary original-digit ancestry certificate.

The program requires Python, NumPy and python-flint.
The packages are publicly obtainable through the usual Python package index, for example with `python -m pip install numpy python-flint` in a suitable Python environment.
The full calculation was checked with Python 3.12.14, NumPy 2.3.5 and python-flint 0.9.0.
It uses no optimizer, random generator, numerical discovery output, research-repository import or network access.
It writes no files and resolves both input paths relative to its own file.
Run:

```text
python -I -B verify_return_core.py
```

The expected output is:

```text
Original polynomial, trace identity, irreducibility and all conjugates verified.
Closed expanding cell [50, 75] drop >= 57/100; 16 axis certificates passed.
Closed expanding cell [75, 100] drop >= 57/100; 16 axis certificates passed.
Complete enumeration: 4818379 nodes; 3077691 leaves; 797507 distinct candidates.
Exact paths: 1044588 acyclic nodes; 797437 covered candidates; maximum length 25
All 70 others excluded: 68 by rho^2 >= 64, 2 by the contracting strip.
PASS: the complete finite neutral-descent and compact-termination premise of the return-core theorem.
```

A failed check raises an exception and returns a nonzero exit code.
Checks remain active with Python's `-O` option.
The complete check takes tens of seconds and a few hundred megabytes of memory on an ordinary desktop; it traverses the entire stated finite domain, with no smaller control substituted.

## Normalized displacement certificate

The trace polynomial

\[
 Q(u)=u^5+u^4-5u^3-5u^2+4u+3
\]

satisfies \(P(t)=t^5Q(t+t^{-1})\).
The verifier checks this identity by Laurent expansion, checks irreducibility of \(P\) over the integers, and isolates every trace root by rational sign bisection.
There are four roots in \((-2,2)\) and one in \((2,21/10)\); these determine every required embedding with outward Arb balls at 360-bit precision.
The expanding root satisfies \(117/100<\beta<118/100\), and the stable strip satisfies \(S<67/10\).

For a word \(w=(\eta_1,\ldots,\eta_\ell)\), the verifier evaluates the endpoint translation by forward Horner recurrence and divides by \(\zeta_j^\ell\) to reconstruct

\[
 c_w=\left(\sum_{i=1}^{\ell}\eta_i\zeta_j^{-i}\right)_{j=1}^4.
\]

It checks the complete closed expanding cell and every intermediate expanding-strip condition, rather than testing a midpoint.
The two cells are \([1/2,3/4]\) and \([3/4,1]\).
For each cell, sixteen signed coordinate targets have positive barycentric representations in nine normalized vertices \(c_w/\|c_w\|^2\).
There are 32 certificates, 288 word uses and 217 distinct words, each of length at most eleven.
All squared normalization denominators are certified positive.
The JSON gives only the integer words, exact cells and rational targets; no saved numerical weights are trusted.

The signed-axis radii are \(r=101/500\) and \(r=207/1000\).
Their cross-polytopes contain Euclidean balls of radius \(r/\sqrt8\).
For every neutral vector of norm at least eight, the positive barycentric relations imply that one selected word has negative normalized projection of magnitude at least \(r/\sqrt8\).
Thus its squared-norm decrease is at least

\[
 \min_w\|c_w\|^2\left(16\frac r{\sqrt8}-1\right).
\]

The verifier encloses this expression and proves the common lower bound \(57/100\).
The report explains the separate sign symmetry, zero prefixes and contracting-strip invariance needed to apply these positive-cell certificates to actual algebraic states.

## Complete compact enumeration

The full embedding sends the coefficient vector \(a\in\mathbb Z^{10}\) to the two real coordinates and eight neutral real coordinates.
The verifier derives the required inverse-embedding bounds

\[
 |a_i|\leq (7,6,7,7,6,5,5,5,5,6)_i.
\]

It checks the integral unimodular transformation \(a=bU\) by computing an exact integral inverse.
The integer matrix \(B\) at scale \(10^8\) approximates the weighted embedding with real-coordinate weights \(\sqrt8\) and \(\sqrt8/(67/10)\).
Every actual compact point has weighted norm at most \(\sqrt{80}\).
Exact rational LDL decomposition and two explicitly propagated error bounds then certify the integer triangular enclosure

\[
 \sum_{j=0}^9\left(\sum_{i=j}^9 b_iT_{ij}\right)^2
 \leq 800554833912,
 \qquad \text{triangular scale }10^5.
\]

The program traverses this whole ellipsoid with arbitrary-precision integer division and integer square roots.
There are 4818379 recursion nodes and 3077691 leaves.
Conservative coordinate filters at scale \(10^6\) retain 797507 distinct candidate states.
Every possible actual \(K_8\) state remains retained, including ambiguous boundary cases.
The larger dense coefficient box has 108561184875 points; it is unnecessary to traverse that box.

NumPy performs only integer basis conversion and batched outward filters.
Before those operations, the program proves bounds for every relevant signed 64-bit sum, product and squared-coordinate accumulation, including the larger coefficient range before filtering.
No floating pruning or volume estimate is a completeness premise.
The 50000000-node and 2000000-candidate caps are enforced and remain unhit.
No saved candidate list is required by this standalone implementation: it reconstructs every candidate itself.

## Integer paths and exact exclusions

The compressed ancestry input contains only the 1044588 original nodes needed by the selected target paths, rather than the full discovery store.
After gzip decompression, each record has the explicit little-endian format `<QIB`: an unsigned 64-bit state key, unsigned 32-bit parent index and byte digit code.
The coefficient \(a_i\) is bits \(5i\) through \(5i+4\) of the key, minus sixteen.
The original digit is the byte code minus one.
The first record is zero; every other record has a strictly smaller parent index.

For every edge, the exact monic reduction of \(t a(t)+\eta\) modulo \(P(t)\) must equal the parent's complete coefficient vector.
Strict parent-index decrease proves termination at zero; recomputed depths prove the maximum path length 25.
Unique state keys and comparison against the entire newly enumerated candidate set give 797437 covered candidates and exactly seventy uncovered candidates.
All seventy are checked by the full algebraic embeddings: 68 have \(\rho^2\geq64\) and two lie outside the contracting strip.
None is an uncovered actual point of \(K_8\).
The complete original 797507-candidate finite scope is preserved.

The data retain the adopted word supports and ancestry, without replacing them by a fresh floating discovery.
The verifier re-implements their mathematical checks as a standalone attachment.
The implementation and its executions are distinct from independent-agent proof review and from the historical reviews cited in the report.
