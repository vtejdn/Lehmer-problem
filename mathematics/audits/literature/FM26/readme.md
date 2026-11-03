# FM26: conditional non-Wieferich counts and initial-depth direction

<a id="fm26-s8-initial-depth-screen"></a>
## Bounded source screen, 2026-10-09

[Retained FM26.pdf](../../../literature/pdf/FM26.pdf);
identity, acquisition and version.
The retained artifact is arXiv:2508.08472v2, 11 February 2026.
Printed and PDF page numbers coincide.
The key follows the verified 2026 journal publication; no comparison with the publisher PDF is claimed.

**Expected use and actual reading.**
[S_G8](../../../strategies/Yin_S_G0008.md#density-capacity-and-isolated-return-boundary) was testing whether actual initial prime-ideal valuations provide positive mass beyond the automatic floors.
The assigned entropy_status AI read Theorems 1.2--1.4 on printed/PDF pp.3--4 and the admissible-base and Wieferich definitions on p.2, with title/version context on p.1.
The retained PDF's pp.3--4 were rendered and visually inspected.
The coordinator separately checked these exact statement/definition passages in the primary versioned HTML and verified the retained PDF bytes.
The proofs, abc assumptions and external dependencies were not audited or adopted.
This is a statement-and-applicability discovery screen, not a fixed source unit, full-paper review, formal verification or new accepted proof dependency.

**Exact screened statements.**
An admissible base is a nonzero algebraic integer alpha which is not a root of unity; K is any number field containing alpha.
A prime ideal q is base-alpha Wieferich when alpha^(Nq-1)=1 modulo q^2, and super-Wieferich when the congruence holds modulo q^3.

- Theorem 1.2, p.3: assuming Masser's abc conjecture for number fields, infinitely many prime ideals are non-Wieferich for the fixed base.
- Theorem 1.3, p.4: the same infinitude follows from the hypothesis that the fixed base has only finitely many super-Wieferich primes.
- Theorem 1.4, p.4: under either assumption, the number of non-Wieferich prime ideals with norm at most x is at least an implicit positive constant times log(x)/log(log(x)) as x tends to infinity.
  The constant may depend on K, alpha, and, in the abc case, epsilon.
  No explicit uniform degree/height threshold or common-return-exponent bound is stated here.

**Direction and transfer boundary.**
For a project unit alpha, every residue is nonzero.
Let o_q be its order modulo q and p the underlying rational prime.
Then o_q divides Nq-1 and the quotient is prime to p.
The elementary prime-to-p factorization already used in [L_G74](../../../ledger/Yin_L_G0074_v1.md#finite-exact-local-cyclic-table) therefore gives

    ord_q(alpha^(Nq-1)-1)=ord_q(alpha^o_q-1).

Thus a non-Wieferich ideal has initial integer depth exactly one.
At a good prime, its ramification index is one, so this is exactly the automatic initial depth, not a positive excess above it.
At a ramified ideal its normalized depth is 1/e_q; the statement does not remove the ramification normalization.
This applicability observation does not assert the source's conditional hypotheses for project inputs.

The counted ideals may have different orders o_q<=Nq-1<=x-1; the theorem does not pay the cost of combining those orders into one exponent.
Its count is of prime ideals, not necessarily new rational primes.
Neither a lower bound on deep/Wieferich mass nor an m-independent arithmetic income follows from the displayed count.

**Existing actual control.**
[J_G11](../../../computations/programs/Yin_J_G0011/readme.md)'s retained Lehmer and degree-22 inputs are low-measure, reciprocal and all-power degree preserving.
For its selected primes {2,3,5,7,11,13,17,19,23,29,31}, every retained initial B entry equals the automatic floor, so the actual selected-prime formula equals that floor for every positive n.
This is the established J11 result, not a fresh execution, and is not extrapolated to untested primes or other inputs.

**Stopping decision.**
This source supplies no unconditional new positive-initial-excess input for the bounded S8 test.
Retain the direction/constant boundary and stop this particular source transfer.
No impossibility result for all p-adic methods is claimed.
A Chinburg search snippet was not selected or used: the full-volume web PDF exceeded the reader's size limit, and no theorem from that snippet was promoted to a proof input.

**Exact search queries.**
The bounded search used three queries:

    algebraic units Wieferich primes abc conjecture non Wieferich primes number fields Silverman theorem
    "Salem" "Wieferich"
    "Wieferich" "unit" "initial" "valuation" primes lower bound

No mathematical numerical scan was run.
The source acquisition and page rendering above are document handling, not a new J computation.
