---
author: Yin
---
# Whole independent review of complete trace-group images and local square saturation

Review act: 2026-10-23T17:22 UTC.
Human record author Yin.
This is a fresh isolated whole review of the fixed C617v1 statement and proof and the native J123 computation at its exact two-precision scope.
The distinct reviewer was outside substantive proof development and received only fixed target paths, the requested scope, applicable rules and nonmathematical execution metadata.
No development dialogue, mathematical summary, author draft or sibling development report was supplied or consulted.
The fixed target and direct dependencies necessarily contain their own provenance and assessment text; these were read as mathematical inputs.
The reviewer formed the mathematical findings and independently reconstructed the native evidence before consulting R812/R810 and the historical R489 relationship declaration.
No proof repair was identified or supplied.
The reviewer added a separate native checker within J123; this checks the existing proof rather than furnishing a missing argument.
The inspected C617 assessment was its [initial open decision](../../claims/Yin_C_G0617_v1.md#decision-initial); this review changes no Claim decision, Task, strategy or execution boundary.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole group-image and square-saturation finding](#whole-group-saturation-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-group-saturation-finding) | [C617v1 statement](../../claims/Yin_C_G0617_v1.md#statement) | Entire FS1--FS3, all complete odd orders at precisions8 and16, endpoint extension, square intersection and unique root, explicit globally nonsquare witness, character descent and all original-input limitations. |
| [Whole finding](#whole-group-saturation-finding) | [C617v1 argument](../../claims/Yin_C_G0617_v1.md#argument) | Whole proof: all-order period and predivision precision, exact96 generator equivalence, filtration and closure, all pivots, character bounds, square map, every product/multiplicity row, integer lift, full degrees and maximal Frobenius power. |
| [Whole finding](#whole-group-saturation-finding) | [C609v2 character argument](../../claims/Yin_C_G0609_v2.md#argument) | Precisely AP3--AP7 and complete divisor induction proving character0 for every allowed W_n and character1 for X; projection, chain rule and truncation rechecked. Original-input parity applications are not premises here. |
| [Whole finding](#whole-group-saturation-finding) | [C608v1 whole-root argument](../../claims/Yin_C_G0608_v1.md#argument) | Whole-root Laurent identity, squarefree root partition, recurrence and matrix identity; all32 displayed coprime-five character rows independently reconstructed. SG1--SG4 target classification and original gate applications are not needed by C617. |
| [Whole finding](#whole-group-saturation-finding) | [J123 results and limits](../../computations/programs/Yin_J_G0123/readme.md#results-and-limits) | Exact96 representatives, four bounded subgroup certificates, all pivot expressions and square relations, both derivative kernels, all roots/membership checks and explicit degree2813 witness; author reruns and reviewer reconstruction completed. |
| [Whole finding](#whole-group-saturation-finding) | [J123 author generator](../../computations/programs/Yin_J_G0123/main.py) | Entire source read and rerun; finite bounds, moduli, normalization, generator vectors, membership, derivative ranks, witness and native publication inspected. |
| [Whole finding](#whole-group-saturation-finding) | [J123 author verifier](../../computations/programs/Yin_J_G0123/verify.py) | Entire source read and rerun; dense arithmetic, Laurent reconstruction, source rows, pivot/closure checks and all square/product payloads inspected without treating same-contributor code as independent agent review. |
| [Whole finding](#whole-group-saturation-finding) | [J123 reviewer checker](../../computations/programs/Yin_J_G0123/reviewer_check.py) | Independent sparse-exponent arithmetic and full B_n reconstruction as1+sum C_j, supplied-certificate checks rather than an insertion rerun, both matrix periods, every selected finite input and displayed C617 table. |
| [Whole finding](#whole-group-saturation-finding) | [Actual normalized gate](../../claims/Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | Scope comparison only: actual canonical remainder and original q, complete original layer multiplicities, specified root and full UR19 remain required; no witness realization is asserted. |
| [Whole finding](#whole-group-saturation-finding) | [Actual complete complement](../../claims/Yin_C_G0199_v4.md#normalized-low-degree-complement) | Scope comparison only: full monic B, every surplus/extra factor and deg B<2A_0 remain; no A_0=2 endpoint formula is imposed for higher multiplicity. |
| [Whole finding](#whole-group-saturation-finding) | [Complete exact-order definitions](../../claims/Yin_C_G0199_v2.md#statement) | Definition of complete Omega_n, exact odd order, inversion/Frobenius invariance and endpoint convention; other original-residual conclusions are not premises of this finite local-image theorem. |

<a id="whole-group-saturation-finding"></a>
## Whole finding

PASS for the entire fixed C617v1 statement and argument, including its native evidence and stated limitations.
No unresolved mathematical defect, omitted hypothesis, precision loss or finite-certificate discrepancy was found.
All complete odd orders are covered by a proved exact reduction; the conclusion is nevertheless confined to the two stated local precisions.
The whole proof refutes the proposed abstract square-saturation equality and supplies the asserted explicit counterexample.
It does not resolve the actual normalized gate or the original G0001 Task.
Adoption belongs to a separate exact Claim decision.

### All-order reduction and division precision

For odd n, the n-th roots are distinct and the nonidentity inverse pairs have distinct traces because an equal trace determines the quadratic z^2+Xz+1.
The complete root set is Frobenius-invariant, giving monic squarefree B_n over F_2; trace0 is absent and its constant coefficient is1.
The roots of phi are exactly the complete order-five trace set.
Thus B_n has exactly one phi factor when5 divides n, even when n contains higher powers of5, and has none otherwise.
The Laurent identity is injective as a polynomial identity because the leading positive Laurent exponent records the polynomial degree.
It gives the stated recurrence and initial vector.

The exact matrix identity A^5-I=phi[phi A+(X+1)I] holds over F_2[X].
Commuting characteristic-two powers give phi^16 divisibility of A^80-I and phi^32 divisibility of A^160-I.
Each matrix step increases n by2, yielding periods160 and320 at the required precisions, including the initial n=1 class.
Using phi^17 before division is sufficient for D_n modulo phi^16; dividing a phi^16 congruence alone would lose one required order.
The64 B classes and32 D classes therefore exhaust their corresponding all-order images.
The complete divisor partition gives both subgroup containments by induction over proper divisors, omitting only W_5.
This covers every power of5 and uses no bound on actual order or degree.

### Filtration, character and exact group size

For N=8,16 the unit group has order3*4^(N-1).
The element t=(X+1)^N lies in the generated group and has exact order3 with nontrivial residue.
Every unit can therefore be normalized into the principal units.
For a first nonzero phi-adic digit, multiplication adds its two binary coefficients; cancellation by an inverse pivot moves strictly to a later bit.
Squaring a pivot also moves strictly later.
Distinct binary pivot products are distinct because the earliest differing bit survives, so the certified pivot expressions already give the required lower bounds.
The checked square relations also establish closure of those forms by carrying exponents to later pivots, and hence justify the recorded membership procedure and exact orders.

The reviewer independently checked all96 source residues, every generator-label list, pivot expression, first bit, original-generator membership and pivot-square relation for all four groups.
The principal counts are13,29,14,30 for G_8,G_16,E_8,E_16.
For G the omitted position is exactly5 at both precisions.
The resulting orders are24576,1610612736,49152,3221225472.

C609v2's projection is valid because subtracting phi^8Q with deg Q<4 cannot change coefficients13 or15.
Differentiation descends through phi^8 and logarithmic differentiation is additive on units.
The all-five-order identity B_(5m)=phi B_m(Xphi^2) and chain rule restrict D_(5m)'/D_(5m) to the span of phi^2,Xphi^4,X^2phi^6 modulo phi^8.
The13/15 functional vanishes on all three.
Together with the independently checked32 C608 rows and divisor induction this proves zero character on every allowed W_n.
The reviewer also checked zero character directly on all96 representatives.
The exact inverse X^(-1)=X^15+X^7 gives character1, so the character kernels have exactly the certified lower-bound sizes.
This establishes FS1 and the endpoint extensions without needing a closure oracle or a guessed group order.

### Squares and both derivative kernels

If f and g differ by phi^8h then their squares agree modulo phi^16, and the reverse divisibility follows from doubling the phi valuation.
This proves that Fr:S_8^* to S_16^* is well-defined and injective.
Every square has zero logarithmic derivative and therefore lies in ker lambda_16=G_16.
Its full image has49152 elements, whereas Fr(G_8) has24576, proving the index2 statement.

For the native corroboration, the logarithmic derivative sends every binary normal form to the corresponding binary sum of pivot images.
The residue order-three factor has derivative zero.
The independent row reduction gives ranks15 and16, respectively, and verifies independent kernel words of the required nullities.
Every kernel product, exponent vector, even-power condition, unique extracted root, membership answer, residual and root-expression factorization was checked.
Both intersections have49152 elements, so saturation fails for G with quotient2 and holds for E.
These are exact group calculations at the declared finite precision.

### Explicit polynomial, global multiplicities and characteristic-zero lift

Every one of the15 displayed B_n/D_n factors is the full polynomial required by its order, and both D rows are divided in F_2[X] before reduction.
Independent multiplication verifies every factor residue, powered residue and cumulative product, ending at4, the encoding of X^2.
Expanding each complete divisor product reproduces every displayed primitive-order multiplicity and the degree2813.
Different exact orders have disjoint squarefree trace factors, and the listed odd multiplicities therefore make Y globally nonsquare.
Every factor has constant coefficient1 and is prime to phi, proving gcd(Y,X phi)=1 and endpoint exponent0.
The unique local square root is X, whose character1 excludes membership in G_8.

The reciprocal cyclotomic Laurent polynomial z^(-phi_Euler(n)/2)Phi_n(z) is symmetric with integer coefficients.
Triangular subtraction of the monic terms z^k+z^(-k), which are integer polynomials in z+z^(-1), supplies the stated monic F_n in Z[X].
For odd n, reduction modulo2 preserves the distinct primitive roots, so its trace reduction is exactly W_n.
The product lift consequently has trace degree2813 and reciprocal degree5626.
Raising to q=2^t multiplies all complete reduction multiplicities byq; because at least one original multiplicity is odd, their maximal common Frobenius power is exactlyq.
This is a formal complete-product lift, with no claim that it is an actual U or G in the original residual problem.

### Descent, original-gate boundary and historical evidence

For u=1+phi^4h in S_8 one has u'/u=phi^4h' modulo phi^8.
Both phi^4 and h' contain only even powers of X, so the13/15 functional vanishes.
The reduction map on unit groups onto S_4^* is surjective and its kernel consists exactly of these units, proving the claimed character descent without a minimal-conductor assertion.

The actual C199v4 gate uses canonical R_0=rem_(U_0)(U_0(chi)^3), the same H_0,V_0,C_00, original q and original integer layer parities.
The complement bound counts every extra factor and surplus multiplicity.
A freely chosen local class Y congruent to X^2 supplies none of that actual data.
The fixed statement correctly leaves these requirements, all higher-precision questions and the original characteristic-zero problem unresolved.

The accepted C609v2 character input has the separately recorded [R812 whole finding](Yin_R_G0812_v1.md#whole-trace-parity-finding).
The C608 predecessor has its [R810 whole finding](Yin_R_G0810_v1.md#whole-support-obstruction-finding).
This review independently rechecked their actually used character/whole-root interfaces and finite rows; it does not retrospectively create a new review of all their unrelated applications.
The comparison-only C199v4 input retains [R489's actual unknown relationship](Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding).
No historical unknown relationship is upgraded, and no old source proof, C197/C199 ancestry or original-domain theorem is recursively re-audited here.
The new proof uses explicit polynomial identities and finite-group filtration arithmetic; no additional external theorem dependency or unresolved attribution issue was identified.
No literature survey, novelty determination, formal verification or Task-completion audit is claimed.

### Reproduction and retained evidence

The reviewer read and successfully reran both original programs, then independently executed the new checker with no author arithmetic imports.
The reviewer's B_n reconstruction uses1+sum_(j=1)^((n-1)/2) C_j, with C_0=0,C_1=X,C_(j+1)=X C_j+C_(j-1), rather than the author's B recurrence or triangular Laurent inversion.
Its sparse exponent-set operations, Euclidean inverses and independent row elimination check the supplied mathematical certificate and all displayed C617 tables.
The decisive mathematical findings above explain why these finite checks suffice.

Run from the repository root, preserving this command order:

~~~text
python mathematics/computations/programs/Yin_J_G0123/main.py
python mathematics/computations/programs/Yin_J_G0123/verify.py
python mathematics/computations/programs/Yin_J_G0123/reviewer_check.py
~~~

The actual certificate (`mathematics/computations/outputs/Yin_J_G0123/certificate.json`), author verification (`mathematics/computations/outputs/Yin_J_G0123/verification.json`) and reviewer verification (`mathematics/computations/outputs/Yin_J_G0123/reviewer-verification.json`) are native same-J outputs.
The first command generates the certificate without prior output; the other two require it.
The independent checker additionally reads only the two fixed C608v1 and C617v1 table inputs named above.
The checker completed with verified status,96 source rows, four groups, ranks15/16,32 predecessor character rows, all displayed C617 tables, degree2813 and final residue4.
These outputs are reproducible evidence, not a substitute for the all-order reduction, mathematical review or separate adoption decision.
