---
author: Yin
---

# Independent review of the degree-18 trace-lattice certificate and discriminant obstruction

## Review arrangement and fixed inputs

The two review acts are dated 2026-11-10T01:38, with Yin as the human record author.
A separately organized reviewer read the complete fixed J158 descriptions and author programs, the designated J144 polynomial, and both actual generated certificates without participating in their development or receiving author derivation dialogue.
No substantive repair was supplied.
The first scope is the exact integral splitting; the second is the subsequent discriminant obstruction, added before this review record was finalized.

The original input is field H_ascending of the [fixed J144 document](../../computations/programs/Yin_J_G0144/trace56_cell.json).
Its existing known-core provenance and sign convention were read in the [J144 discussion](../../computations/programs/Yin_J_G0144/trace56_cell.md#removing-both-complete-known-value-fibers) and [prior preparation finding](Yin_R_G1111_v14.md#fixed-cell-preparation-review), without a new root or factorization audit.
The finite matrix checks below are performed directly from the exact polynomial.
The [ERT19 trace-Gram unit](../literature/ERT19/Yin_U001.md#companion-trace-gram) and [GHS09 group conventions](../literature/GHS09/Yin_U001.md#integral-transvection-groups) were read at their recorded source-inspection depths.
Their original foundational proofs and the separate two-plane generation theorem were not newly audited or adopted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Integral splitting finding](#trace-lattice-splitting-review) | independently reviewed |
| [Discriminant obstruction finding](#discriminant-action-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Integral splitting finding](#trace-lattice-splitting-review) | [J158 trace description](../../computations/programs/Yin_J_G0158/readme.md) | Complete finite question, companion and Gram conventions, witness search, integral splitting, reported matrices and limits. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [Author trace program](../../computations/programs/Yin_J_G0158/trace_lattice.py) | Whole integer/rational implementation, Newton traces, determinant and inertia routines, search semantics, Bezout completion and certificate checks. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [Original J144 input](../../computations/programs/Yin_J_G0144/trace56_cell.json) | Exact H_ascending polynomial only; unrelated cell and solver data are outside this review. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [Actual trace certificate](../../computations/outputs/Yin_J_G0158/trace_lattice.json) | Every exact vector and matrix entry, all traces, both inertias and determinants, the reported search prefix and complete characteristic-polynomial preservation. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [Independent trace checker](../../computations/programs/Yin_J_G0158/checks/independent_trace_lattice_review.py) | Separate quotient-algebra reconstruction, rational determinants, positive principal minors and full matrix identities, without importing author code. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [Independent trace result](../../computations/outputs/Yin_J_G0158/independent_trace_lattice_review.json) | Actual successful verification, including all sixteen positive leading principal minors and the exact checked search prefix. |
| [Integral splitting finding](#trace-lattice-splitting-review) | [ERT19 construction convention](../literature/ERT19/Yin_U001.md#companion-trace-gram) | Matching column companion and integral bilinear Gram G, equal to twice the source's quadratic coefficient matrix; no integral-splitting theorem is imported. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Exact representation question](../../computations/programs/Yin_J_G0158/discriminant_action.md#fixed-question) | Same fixed lattice and isometry, positive rank sixteen, two fixed cusp groups and arbitrary finite word length. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Necessary word condition](../../computations/programs/Yin_J_G0158/discriminant_action.md#necessary-condition) | Trivial transvection action on the discriminant group, finite positive-isometry product and uniform exponent 24504480. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Integer obstruction certificate](../../computations/programs/Yin_J_G0158/discriminant_action.md#integer-certificate) | Exact dual-lattice criterion, adjugate normalization and actual nonzero modular witness. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Conclusion and limits](../../computations/programs/Yin_J_G0158/discriminant_action.md#conclusion-and-limits) | Exclusion at every word length and every integral positive-plus-U splitting of this same lattice, with other lattices and representations left open. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Author discriminant program](../../computations/programs/Yin_J_G0158/discriminant_action.py) | Whole exact adjugate calculation, modular exponentiation, complete defect matrix, witness and Boolean conclusion. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Actual modular certificate](../../computations/outputs/Yin_J_G0158/discriminant_action.json) | Every adjugate, modular-power and defect-matrix entry, plus all polynomial, rank, exponent, determinant, modulus and witness fields. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Verified splitting input](#trace-lattice-splitting-review) | Exact original Gram and companion matrices, nonzero determinant and unimodular splitting used by the second stage. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Independent discriminant checker](../../computations/programs/Yin_J_G0158/checks/independent_discriminant_review.py) | Separate quotient-polynomial exponentiation, adjugate identities, full modular comparisons and split-basis transfer. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Independent discriminant result](../../computations/outputs/Yin_J_G0158/independent_discriminant_review.json) | Actual successful verification of the whole modular certificate and nontrivial action after integral basis change. |
| [Discriminant obstruction finding](#discriminant-action-review) | [GHS09 group conventions](../literature/GHS09/Yin_U001.md#integral-transvection-groups) | Integral dual, discriminant group and allowed transvections; the separate two-plane generation theorem is not used. |
| [Discriminant obstruction finding](#discriminant-action-review) | [Finite positive-isometry argument](../../claims/Yin_C_G0885_v2.md#argument) | Bounded-column proof of finiteness for a fixed positive integral lattice; no Mahler-gap assertion is a premise. |

<a id="trace-lattice-splitting-review"></a>
## Finding: the actual integral splitting certificate

No mathematical or implementation defect was found in the finite trace-lattice calculation or its actual output.
The certificate proves an integral unimodular splitting of the original degree-eighteen lattice as a positive definite rank-sixteen lattice plus the standard hyperbolic plane, preserving the complete original characteristic polynomial by integral conjugacy.
The author's construction remains at its [responsible description](../../computations/programs/Yin_J_G0158/readme.md#results-and-limits); the checks below identify the decisive independent evidence.

### Input, traces and arithmetic implementation

The input and output agree on all nineteen designated ascending coefficients, including monicity, constant coefficient one and reciprocity.
The companion columns implement multiplication by \(\alpha\) in \(1,\alpha,\ldots,\alpha^{17}\); the last column is the negative lower-coefficient vector of \(p\).
The author's coefficient reversal and Newton recurrence have the correct signs and indexing.
The independent checker instead constructs multiplication in \(\mathbb Q[x]/(p)\) by convolution and monic reduction, obtains \(\alpha^{-1}\) directly from \(p(\alpha)=0\), and computes traces of both positive and negative powers.
Every reported trace and every Gram entry agrees, with the common trace list
\[
(18,1,-1,1,3,1,5,1,3,1,9,1,9,14,13,16,19,18).
\]
Reciprocity justifies replacing the exponent \(i-j\) by \(|i-j|\), and the direct negative-power calculation checks that interface independently.

The full matrix satisfies \(C^{\mathsf T}GC=G\).
Its diagonal entries are 18, so it is even integral.
This is the ERT19 integral bilinear normalization \(G=2A_{\mathrm{source}}\), not the source's half-sized quadratic coefficient matrix.
No rescaling of the lattice precedes the divisor-one or hyperbolic-plane test.

The whole author program was inspected, including the fraction-free determinant, rational integral-inverse checks, symmetric-congruence inertia routine and Bezout updates.
The inertia routine's zero-diagonal case is valid: adding a basis vector with a nonzero off-diagonal pairing creates the nonzero pivot \(2a_{ij}\); an entirely zero residual contributes its full nullity.
The determinant row swaps track the sign, and exact division and inverse integrality are checked.
This is finite-input coverage at the actual dimensions, not validation of an unrestricted matrix library.

### Witness, integral completion and full matrix verification

The finite search is exactly the stated support-at-most-four subset of \(\{0,\pm1\}^{18}\), modulo overall sign by a positive first coordinate.
Its expiry branch is explicitly incomplete, while an exhausted finite set would provide no general lattice obstruction.
The twenty-second allowance governs the search; it is not a total bound on the later certificate calculation.
The independent checker verifies the actual prefix: eighteen singleton norms are 18, the next thirty-two pair norms \(36\pm2s_j\), \(1\le j\le16\), are nonzero, and the next candidate is
\[
e=1-\alpha^{17},\qquad e^2=0,\qquad \gcd(Ge)=1.
\]
Thus the counts 18 and 33 and the single isotropic vector seen before stopping are exact.
No support-three or support-four search or historical elapsed-time replay is claimed.

The Bezout column update has determinant one and sends each row pair \((a,b)\) to \((\gcd(a,b),0)\).
It yields a partner and an integral kernel basis; the inverse-transpose completion of the primitive kernel coordinates has the required first column \(e\).
Evenness makes \(f=f_0-(f_0^2/2)e\) integral, and replacing each remaining kernel vector \(k\) by \(k-(k,f)e\) makes it orthogonal to both null vectors through integral basis operations.
For the actual output the independent checker verifies
\[
f_0=\alpha-\alpha^2-\alpha^9,\qquad (e,f_0)=1,\qquad f_0^2=48,\qquad f=f_0-24e,
\]
which is precisely the stored vector in the author description.

Every entry of \(C,G,T,T^{-1},H_+\), the full split Gram \(S\), and \(A\) was independently checked.
The decisive complete identities are
\[
TT^{-1}=T^{-1}T=I,\qquad
T^{\mathsf T}GT=S=H_+\oplus U,\qquad
A=T^{-1}CT,\qquad CT=TA,\qquad A^{\mathsf T}SA=S.
\]
The last basis columns agree with the actual \(e,f\), and all positive/hyperbolic cross blocks vanish.
Ordinary rational determinant elimination, separate from the author's Bareiss routine, gives
\[
\det G=-2915479459020775961521,\qquad \det T=-1.
\]
All sixteen leading principal minors of the actual \(H_+\) are positive; their full list is in the independent output, with first value 10422 and last value \(2915479459020775961521\).
Sylvester's criterion and the verified \(U\)-splitting therefore prove the inertias \((16,0,0)\) and \((17,1,0)\) without reusing the author's inertia implementation.
Exact matrix traces independently reconstruct both full characteristic polynomials and give \(\chi_A=\chi_C=p\).
This establishes the original lattice's integral splitting and conjugacy, with no added dimension, substituted matrix power, discarded root or transvection decomposition.

<a id="discriminant-action-review"></a>
## Finding: the arbitrary-word-length obstruction on this fixed lattice

No mathematical or implementation defect was found in the complete discriminant-action argument or its actual output.
On this fixed natural trace lattice, the companion isometry cannot be represented by the stated positive-summand isometries and fixed-cusp transvections at any finite word length.
The conclusion holds for every integral positive-rank-sixteen-plus-\(U\) splitting of this same lattice.
The necessary condition and certificate are retained in the [author's fixed argument](../../computations/programs/Yin_J_G0158/discriminant_action.md#necessary-condition).

### Necessary condition and its exact scope

For \(x\in L^\vee\), the pairings with the integral vectors \(e,v\) are integers, and the even norm makes \((v,v)/2\) integral.
The displayed transvection difference therefore belongs to \(L\), proving trivial action on \(D(L)\).
Passing any permitted word to its discriminant action removes those factors and leaves the action of the ordered product of its positive isometries.
They need not commute, and their product still belongs to the finite integral isometry group of a positive rank-sixteen lattice.

If an eigenvalue of that finite-order matrix has order \(n\), its cyclotomic minimal polynomial divides a degree-sixteen characteristic polynomial.
Hence \(\varphi(n)\le16\), and every prime power \(p^a\mid n\) satisfies \(p^{a-1}(p-1)\le16\).
The maximal possible prime powers are exactly \(32,9,5,7,11,13,17\), whose product is
\[
E=24504480.
\]
Every eigenvalue order divides \(E\), and finite-order matrices are diagonalizable in characteristic zero.
Thus every permitted word has \(E\)-th power acting trivially on \(D(L)\).
This concerns the discriminant action, not finite order of the whole word matrix, and the bound is uniform over all positive rank-sixteen Gram matrices.

### Complete modular certificate and independent calculation

With \(d=\det G\) and \(Q=\operatorname{adj}(G)\), the columns of \(Q/d\) generate \(L^\vee=G^{-1}\mathbb Z^{18}\).
Consequently the exact trivial-action criterion is
\[
(C^E-I)Q\equiv0\pmod{|d|}.
\]
The negative sign of \(d\) does not affect divisibility.
No Smith-normal-form assumption or restriction to a selected subgroup is hidden in this criterion.

The complete author program was checked: rational inversion gives an integral adjugate and both defining identities are verified; binary matrix exponentiation reduces after each product; the entire defect matrix determines its first row-major nonzero witness and the Boolean result.
Its shared matrix routines and the original trace certificate are covered by the first finding.
The result is a necessary-condition test, so a hypothetical zero defect would not establish a factorization.

The independent checker revalidates the first certificate and verifies all entries of \(GQ=QG=dI\), which uniquely certify the adjugate because \(d\ne0\).
It separately computes \(\alpha^E\) in \((\mathbb Z/|d|\mathbb Z)[x]/(p)\), using polynomial convolution and reduction with binary exponentiation from the highest bit downward.
The resulting multiplication operator agrees in all 324 entries with the stored matrix power.
Monicity makes this polynomial reduction valid over the composite modulus.
All 324 defect entries and all polynomial, rank, exponent, determinant, modulus, witness and result fields also agree.

The actual nonzero entry is
\[
\bigl((C^E-I)Q\bigr)_{00}
\equiv2850856976087321421046
\pmod{2915479459020775961521}.
\]
It is strictly between zero and the modulus.
The first column of \(Q/d\) therefore represents an explicit dual-lattice class whose change has a nonintegral first coordinate.
This directly contradicts the necessary condition for every permitted word.

The checker also verifies the full split-coordinate transfer.
For \(S=T^{\mathsf T}GT\), unimodularity gives \(\operatorname{adj}(S)=T^{-1}QT^{-\mathsf T}\), and the new defect is
\[
T^{-1}\bigl((C^E-I)Q\bigr)T^{-\mathsf T}\pmod{|d|}.
\]
It agrees with the separately formed split-coordinate defect and remains nonzero.
Intrinsically the discriminant action is independent of integral coordinates, while every other positive-plus-\(U\) splitting of this same rank-eighteen lattice has the same rank-sixteen exponent bound.
This proves the claimed extension across all those splittings, without extending to another integral lattice.

### Source and mathematical limits

ERT19 supplies the trace-form convention, not a theorem that this natural lattice contains an integral \(U\).
GHS09 supplies the dual and transvection conventions; finding one \(U\) in signature \((17,1)\) does not meet its separate two-plane generation hypotheses, and no such theorem is used.
The original foundational source proofs retain their recorded inspection limits.

The obstruction leaves other \(C\)-stable integral lattices, changed generators, stabilization and different realizations of the same polynomial open.
The auxiliary \(C^E\) tests the original discriminant action; it is not substituted as a new representation with the same Mahler measure.
These certificates produce no new small value, general one-plane generation theorem or unrestricted Mahler gap.
The [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Independent execution and reproduction

Both reviewer-owned programs ran successfully with CPython 3.14.7 using only standard-library integers and fractions.Fraction.
The second imports only the first reviewer's helpers and rechecks the fixed input; neither imports or executes author code.
Both independently generated result files report verified and retain the exact evidence described above.
With the interpreter selected as python, the repository-root verification commands are:

~~~text
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_trace_lattice_review.py
python -B mathematics/computations/programs/Yin_J_G0158/checks/independent_discriminant_review.py
~~~

The fixed J144 input and both actual J158 author output files are required.
The author descriptions supply their generation order when those reproducible local certificates are absent.
The checkers write separate result files and preserve the author inputs and programs.
No new search beyond checking the reported prefix, numerical roots, transvection-word search, matrix enumeration or historical timing replay was performed.

