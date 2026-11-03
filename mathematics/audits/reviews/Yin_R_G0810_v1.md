---
author: Yin
---
# Independent whole review of the normalized complete-group support obstruction

Review act: 2026-10-23T15:48 UTC.
Human record author: Yin.
This is an initial whole mathematical and native-computation review of the fixed [C608 v1 statement](../../claims/Yin_C_G0608_v1.md#statement), complete [SG1--SG11 argument](../../claims/Yin_C_G0608_v1.md#argument) and [J119 certificate](../../computations/programs/Yin_J_G0119/readme.md#results-and-limits), inspected as the 2026-10-23 working-tree revision before a reviewed adoption.
The selected C608 assessment at inspection was [open](../../claims/Yin_C_G0608_v1.md#decision-initial).

## Review arrangement and inputs

A distinct reviewer outside substantive development received this assignment in a fresh isolated context, with the fixed artifact paths, review scope and applicable operational rules.
No exploration notes, proof-generation dialogue, author explanation, mathematical development summary or previous verdict about C608 was supplied or consulted before the findings.
The reviewer read the proof itself and its selected exact dependencies directly, including the original-domain statement and support bridge in C199v5 and the exact-order definitions in C199v2.
The D35 development text and sibling development reports were not consulted.
The reviewer reconstructed the proof and inspected both complete author programs before writing a new checking program.
That independent checker is verification evidence, not a repair of the proof under review.
No substantive proof correction was identified or supplied.

The accepted C199 results are used at their stated scopes after checking their hypotheses and this invocation.
This review does not independently re-prove the entire older C199 chain or reclassify any older review arrangement.
No previous C608 review is used as evidence.
The newly performed review belongs in this fixed R; the native independent checker and its output remain in the existing J119 rather than a separate computation family.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [C608 precise statement](../../claims/Yin_C_G0608_v1.md#statement) | Complete finite-support product, both epsilon values, low-X and full normalized local hypotheses, odd normalized multiplicity at some odd n>5 divisible by5, and exact original-domain application. |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [C608 complete argument](../../claims/Yin_C_G0608_v1.md#argument) | Every SG1--SG11 step, converse local equivalence, older support relation, all-order matrix period, complete-group partition and inversion, character, all32 rows, both targets, even-multiplicity extension and retained limitations. |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [C199v5 normalized gate statement](../../claims/Yin_C_G0199_v5.md#statement) | Exact accepted-input applicability: actual characteristic-zero residual domain, zero Haar, unique unsaturated phi, maximal q, normalized A_0=2, complete complement, low-X coefficients, H/C/V, original-layer parity and root/gate precisions; no new recursive review of its proof. |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [C199v5 complete-group bridge](../../claims/Yin_C_G0199_v5.md#normalized-a2-odd-part-and-degree-return) | QC14--QC16 match the complete normalized multiplicities, exclusion of orders1 and5, unchanged original q and absence of any smaller characteristic-zero realization or individual integer-exponent division. |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [C199v2 exact-order definitions](../../claims/Yin_C_G0199_v2.md#statement) | Exact order is the odd multiplicative order of z for trace z+z^(-1), invariant under inversion and Frobenius; Omega_n is the complete set of irreducible trace factors. Other C199v2 conclusions are not additional premises for the formal support theorem. |
| [Whole support obstruction and native certificate](#whole-support-obstruction-finding) | [J119 complete finite support](../../computations/programs/Yin_J_G0119/readme.md#results-and-limits) | Full author source inspection and reproduction, direct independent reconstruction of every certificate field and all32 displayed C608 rows, matrix identities, both CRT classes, both complete gates and old support congruences, with exact finite scope. |

## Whole support obstruction finding

The complete formal theorem and its stated original-domain application are supported by the reviewed proof and exact certificate.
No unresolved mathematical or native-certificate defect was found in the selected scope.
The following are the decisive checks, not a claim that a program exit code alone proves the theorem.

### Local target reduction and converse

Because chi=X phi^2 has phi-order2, the low-X coefficients give Y(chi)=1+X^2 phi^4 modulo phi^8.
The expansion Psi=1+X phi^2+X^2 phi^4 gives Psi^14=1+X^2 phi^4 at the same precision, so their product is1 and C=X^2.
Substitution into the original gate and division by X^5 yields exactly Z(Y+X)=epsilon X^6Y^2(X+1)^8 phi^4.
All divisions are by local units.
The gate first forces Y=X modulo phi^4, after which the root equation reduces to Z^11=X^7 modulo phi^4.
The identity X^3=1+(X+1)phi gives X^12=1 modulo phi^4, and hence Z=X^5 there.
Eleventh powers are injective on the residue group of order3 and on the principal units: the first nonzero phi-adic coefficient of (1+u)^11-1 equals that of u.
The finite quotient therefore has a unique eleventh root at the stated precisions.

Only depth4 information is used in the coefficient multiplied by phi^4.
In particular X^8(X+1)^8=1 modulo phi^4 and X^12=1 there turn the coefficient into X^7, yielding Y=X+epsilon phi^4 X^7 modulo phi^8.
Conversely that congruence and the low-X condition recover C, Z modulo phi^4 and the entire gate.
Squaring the phi^4 error gives Y^6=X^6 modulo phi^8; X^24=1 then gives H^6=C^21 at depth8.
Thus neither parity is discarded and the older support condition is recovered without a stronger hidden hypothesis.
A representative change of Z by a multiple of phi^6 multiplies Y+X, which already has phi-order at least4, so it cannot affect the depth8 gate.
The checker additionally evaluates every one of the16 representatives modulo phi^8 of each target's prescribed root class modulo phi^6.

### Trace polynomial, period and complete groups

For odd n, the nonidentity n-th roots are distinct and inversion has no fixed point on them in characteristic two.
Two roots with the same trace solve the same quadratic z^2+xz+1, so they are precisely one inverse pair.
Frobenius invariance gives B_n in F_2[X]; its constant coefficient is1 because none of these traces is zero.
The roots of phi correspond precisely to primitive fifth roots, establishing that B_n is a unit modulo M exactly when5 does not divide n.
The Laurent identity determines a monic polynomial of degree(n-1)/2 and proves both initial values and the recurrence through the injective trace substitution.
This includes B_1=1, which is needed at the beginning of the period.

The three displayed matrix identities are valid over the polynomial ring itself.
The second implies A^8=I modulo X^4.
The third is A^5-I divisible by phi, and its eighth power is A^40-I divisible by phi^8 because the matrix and identity commute.
Since40 is a multiple of8 and the two moduli are coprime, A^40=I modulo M.
The vector(B_3,B_1) therefore returns after40 recurrence steps, including the B_1 case, and the shift in odd n is80.
This is an all-order identity; the32 generator classes are not a numerical cutoff in n or degree.

The primitive-order root partition gives B_n=product_(d|n,d>1) W_d with each complete trace group used exactly once.
For n coprime to5, induction on its proper divisors expresses W_n in the subgroup of the B_d, and the reverse inclusion follows directly from the partition.
The displayed divisor inversion is consistent with this induction and the elementary cancellation of squarefree divisor signs.
All factors are units; finiteness of the unit group turns every inverse into a nonnegative power, so arbitrary monic-product multiplicities are covered.
Requiring the actual generating orders also to be coprime to3 does not lose any B residue: every allowed class modulo80 has a positive representative coprime to3.
This does not assert that the individual W_n are themselves80-periodic.

### Character, complete finite certificate and multiplicity conclusion

M=X^20+X^12+X^4 has zero derivative, so ordinary differentiation descends to R and D(u)=u'/u is representative-independent on R units.
The product and inverse rules show that D is a homomorphism to the additive ring, and the coefficient functional Lambda is F_2-linear.
Consequently lambda is a group homomorphism and vanishes on every square.
The CRT components have8 and3*4^7 units, giving393216 units in R; this count is consistent but no subgroup size or membership oracle is used in the exclusion.

Every one of the32 displayed rows matches a polynomial reconstructed independently from the Laurent identity.
Every stored inverse multiplies its B to1 modulo M, every displayed D satisfies B D=B prime modulo M, and its coefficients at X^13 and X^15 agree.
The independent construction uses dense coefficient vectors and triangular inversion of the Laurent expansion, rather than either author implementation or the B recurrence.
Both CRT targets were reconstructed by testing the16 corrections by multiples of phi^8 against the fixed low-X class.
They are uniquely y_0=0x70705 and y_1=0x78f85; both satisfy D(y)=X^15+X^7, have character1 and pass their entire local gate and older support relation.
The independent checker compares all mathematical fields in certificate.json and all32 rows in the fixed Claim, not only a final verdict field.

Every coprime5 W_n has character0 by the proved subgroup equality and period.
For n>5 divisible by5, W_n is still prime to X phi because its roots have exact order n, not1 or5; hence its square contribution is also a unit with character0.
If all such b_n were even, the whole product would have character0, contradicting either target's character1.
This proves the claimed existence of an odd n>5 divisible by5 with b_n odd, for arbitrary finite support, degree and nonnegative multiplicities.
The empty product is allowed in the definition but fails the low-X hypothesis and causes no exceptional case.

### Original-domain applicability and source scope

C199v5 is used only on its actual monic irreducible reciprocal nontorsion original P, totally real trace field, integral theta_2/theta_3/theta_5 and complete residual equations, together with zero canonical Haar, unique unsaturation at phi and normalized A_0=2.
Its statement and QC14 supply exactly H=X^2Y, C=X^2Y(chi)Psi^14, V=X^5Y, the low-X class and complete normalized groups.
Its original layer window in QC6 has4q<lambda_b<12q, so lambda_b/q=8 and b=k+4; this gives exactly epsilon=a_(k+4) modulo2 in SG1.
Its root precision is phi^6 and its full gate/support precision is phi^8, matching every use above.
QC14--QC16 preserve all original q=2^k and imply b_n=nu_n/q for complete group multiplicities, without q dividing any individual original integer cyclotomic exponent.
Thus oddness is a statement about normalized complete multiplicity, not original a_m.
The formal theorem also states its own hypotheses explicitly, so it does not depend on a converse existence claim from local data to characteristic zero.

The exact-order terminology is attributed to the selected C199v2 statement and is consistent with the root construction.
All new algebraic steps, the divisor cancellation and the finite certificate are explicitly proved or checked here; no unidentified external theorem is needed for SG1--SG11.
No literature novelty search or fresh audit of the older source proofs is claimed.
The only documentation correction made in J119 replaces a product of the sets Omega_d by the explicitly defined polynomials W_d; it changes neither C608's already correct notation nor its mathematics.

## Native verification facts

The reviewer read the full main.py, verify.py, readme.md, certificate.json and verification.json, then successfully reran the documented generation and author verification commands.
The independently authored [independent_verify.py](../../computations/programs/Yin_J_G0119/independent_verify.py) imports neither author program and successfully produced independent_verification.json (`mathematics/computations/outputs/Yin_J_G0119/independent_verification.json`).
The exact result records32 generators, two targets,32 root lifts,32 Claim-table rows and three polynomial matrix identities.
Four in-memory corruption controls were rejected: an altered B coefficient, a missing generator row, an altered target coefficient and an altered displayed Claim-table derivative.
These controls changed only copies supplied to the checker, not the retained certificate or Claim.
All arithmetic is exact over F_2 with Python integers and coefficient vectors; there are no floating-point tolerances, random seeds or empirical extrapolations.
The two original implementations remain author work; the present isolated review and distinct verification are the independent evidence.

## Outcome and retained limits

The whole C608 v1 support obstruction, including its precise C199 application and complete native certificate, passes this independent review without a substantive repair.
The result excludes all supports whose odd-multiplicity complete groups are coprime to5, including every wholly coprime15 support family, and requires at least one higher5-order group of odd normalized multiplicity.
It neither excludes the surviving higher5-order supports nor supplies their simultaneous C3/C5 constraints, actual monic T coefficients, divided quotient triple, integer Gamma, characteristic-zero realization, FE5 independence or an unrestricted Mahler estimate.
No same-T coefficient calculation was entered after support exclusion.
This finding supplies review evidence only; C608 adoption and the broader Task's status remain with their responsible C/T/E materials.
