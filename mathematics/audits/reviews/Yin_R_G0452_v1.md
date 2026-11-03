---
author: Yin
---
# Whole independent review of the exact finite affine residual screen

Date: 2026-10-20T10:24.
Human record author Yin.
Root separately assigned draft_inventory_later to review the actual J111 reduction, main program and completed results.json for the predeclared32 parameter triples.
Root proposed the finite affine elimination; entropy_attainment_bridge supplied the even-even consequence and the integrality simplification.
This reviewer did not contribute those reductions or the author program.
The reviewer previously collaborated on general field-generation arguments for the broader D37 inquiry, but none is a premise of this affine reconstruction or this review.
The present verification derives its field directly from c and the displayed rational formula for a.
The arrangement is nonblind: root supplied the intended review obligations, and the reviewer read the actual author program, results and README before writing an independent verifier.
The separate later all-affine analytic argument was mentioned but was neither supplied as an input nor used to certify this finite computation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [J111 question and scope](../../computations/programs/Yin_J_G0111/readme.md#question-and-scope) | Exact u,v in{-2,-1,1,2}, both signs,24 computed and eight analytic cases, original nonzero integral totally real domain, norm target and finite limits. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [J111 analytic reduction](../../computations/programs/Yin_J_G0111/readme.md#analytic-reduction-and-checking-arrangement) | Both elimination directions, rational reconstruction, integrality, total reality, primitive nonmonic exclusion, full original-field norm and even-even consequence. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Actual author main program](../../computations/programs/Yin_J_G0111/main.py) | Complete fixed grid, polynomial construction, factorization, complete product, real-root counts, conditional field reconstruction and norm branch, resource limits and publication behavior. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Independent verifier](../../computations/programs/Yin_J_G0111/verify.py) | Independent integer-list coefficients and product, complete Fraction Sturm chains, cleared reconstruction identities and same-SymPy irreducibility recheck; no expanded parameter grid. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [C178 exact valuation statement](../../claims/Yin_C_G0178_v1.md#statement) | dependency: Full original residual domain, low branch B=G/2<e/2, complete prime weights and the resulting even-even floor2^r. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [C178 complete argument](../../claims/Yin_C_G0178_v1.md#argument) | Adopted local split and full norm normalization, used only to justify the eight analytic cases. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Prior whole C178 finding](Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Accepted valuation theorem at its existing scope; it does not certify the new affine elimination, program or24 factorizations. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Classical algorithm and source interface](#sturm-and-symbolic-source-interface) | Checked Sturm theorem at infinite endpoints, positive sequence rescaling and exact SymPy domain/API meanings; no PVS or independent second-engine certification. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0111/readme.md#recorded-runs) | Every coefficient, signed content, factor, multiplicity, leading coefficient, real-root count and disposition; all32 labels with no duplicate or missing case. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0111/results.json`; this target locates that original run's computation account. |
| [Whole finite affine finding](#affine-screen-whole-independent-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0111/readme.md#recorded-runs) | Complete24-case agreement, full chain degrees and infinite-endpoint sign variations, eight analytic labels and explicit unexercised norm-branch boundary. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0111/verification.json`; this target locates that original run's computation account. |

<a id="affine-screen-whole-independent-finding"></a>
## Whole finding

**PASS for J111's complete declared32-case result and its analytic reduction, with the exact symbolic-engine and unexercised-branch limits below.**
The24 computed affine choices have no algebraic-integer root c and hence no original integral triple.
The eight even-even choices satisfy the stronger full norm floor2^r whenever an original triple exists; they were not factored and their nonexistence is not asserted.
No admissible factor, original counterexample, actual norm violation, unrestricted affine theorem or general D37 completion is inferred.
No mathematical program repair or changed input was necessary.
The README's generic description of generated identities was clarified to distinguish the actual stored factorization data from its unexercised conditional norm branch.
This wording clarification changed no mathematical result or program behavior.
The review records evidence and selects no Claim or Task adoption.

### Exact elimination and full reconstruction

Write b=u c+v and Q=b^2+s(c^3-2b^5).
An original solution has a^3=Q and2c^2=3a^5, so27Q^5=8c^6.
Conversely take a nonzero root c of H=27Q^5-8X^6 with b(c) and g(c) nonzero.
Then Q(c) is nonzero and the displayed a=3Q(c)^2/(2c^2) is an actual element of Q(c).
Writing A=3Q^2 and D=2X^2, the exact cleared identities are

    A^3-Q D^3=Q H,
    3A^5-2X^2 D^5=H(27Q^5+8X^6).

Division by the nonzero denominators gives a^3=Q and3a^5=2c^2, followed by both residual identities with the same sign s.
The verifier checked these cleared polynomial identities using independently constructed integer coefficients for every one of the24 cases.
This does not turn a nonintegral factor field into an admissible original example.

If c is integral then b(c), g(c) and Q(c) are integral; a satisfies the monic equation T^3-Q(c)=0 over the ring of algebraic integers.
Transitivity of integrality therefore makes a integral as claimed, without requiring the displayed rational denominator to be a unit.
At every real root c!=0, Q(c)^5=8c^6/27>0, so Q(c)>0 and a>0.
The reconstructed primitive triple field is exactly Q(c), since it contains a and b and the triple itself contains c.
No earlier general field-generation lemma is needed for this argument.

### Factors, integrality, total reality and norm semantics

Every original integral c has a monic irreducible minimal polynomial in Z[X] dividing H over Q.
A primitive irreducible integer factor can be associated over Q to such a monic integer polynomial only when its leading coefficient is1 or-1.
Primitivity is essential here; a mere nonmonic presentation would not exclude integral roots.
The actual factors were separately checked primitive with positive leading coefficient and irreducible over Q.

For a monic irreducible factor of characteristic zero, all its roots are simple, and total reality of Q(c) is equivalent to having degree-many distinct real roots.
The author program's subsequent zero checks correctly reject field elements c,b or g that vanish.
Its inversion of c^2 and four reduced identities implement the above reconstruction in the quotient field.
For a surviving monic factor f, Res(f,g) is the full Q(c)/Q norm, independent of whether g generates that field.
The exact squared target is Norm(g)^2>=2^deg(f).
For any larger ambient totally real F containing the triple, both this norm-square and the target are raised to [F:Q(c)], so the original degree and all embedding multiplicities are retained.
The branch was inspected algebraically and in code, but no surviving factor exercised its field-inversion or resultant/norm execution.
Neither program reports an executed admissible norm test for this dataset.
No synthetic or out-of-grid input was added to exercise it.

### Complete actual data and independent execution

The reviewer read the actual completed results.json, not a summary substituted for unavailable evidence.
The verifier checks the exact expected set of32 triples and rejects repeated or omitted rows; the eight even-even triples and the other24 form the precise disjoint partition.
For each computed triple it expands b^2 and b^5 from integer binomial coefficients, forms Q and H by integer-list addition/convolution, and compares every stored coefficient.
It recomputes the integer content and its sign, checks every factor's degree, positive leading coefficient, primitive content and multiplicity, and multiplies the full supplied factorization back to the independently constructed H.
The verification imports no function or constant from main.py and does not call the author's one_case helper.

All24 H polynomials have degree25 and signed content1 or-1.
Each has exactly one primitive irreducible factor of degree25 and multiplicity1.
Its leading coefficient is864 when abs(u)=1 and28991029248 when abs(u)=2, always greater than1.
Both magnitudes agree with the degree25 leading term -864s u^25 of H.
The complete factor product, not just its degree or leading coefficient, agrees in all cases.
Thus every computed row's nonintegral_root disposition is supported.

The verifier separately builds the entire signed Euclidean Sturm chain using Python Fraction arithmetic.
Each remainder is multiplied only by a positive rational when denominators and content are removed; signs are never normalized by forcing a positive leading coefficient.
Every chain reaches a nonzero constant, verifying squarefreeness, and the full degree sequence is retained in the output.
The degree drop from20 to10 in these chains is retained rather than filled with nonexistent degrees.
At each infinite endpoint the sign follows from the actual leading sign and degree parity.
Subtracting the two complete variation counts gives one real root for14 factors and three for10 factors, with exact case-by-case agreement with the author program.
No floating-point root approximation or omitted interval is used.

The actual executed command was

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0111/verify.py

It completed all24 checks within its declared per-case and whole-pass resource controls and published the complete verification.json.
The author output was not overwritten and its entire parsed mathematical payload remained unchanged during verification.
The verification parent derives paths from its actual J directory, executes only existing case keys, preserves15-second child and120-second pass limits, and publishes a separate incomplete record on failure.
Complete output is published only after all cases pass.

<a id="sturm-and-symbolic-source-interface"></a>
### Standard algorithm attribution and engine limits

The reuse check read the existing [MS26-U001 exact terminal verification](../literature/MS26/Yin_U001.md), which already retains rational Sturm use in J1; its different input range supplies no J111 result.
For the exact classical theorem interface I directly read Section2, formulas(3)--(4), Theorem1 and the infinite-endpoint reduction on printed pages3--4, PDF pages8--9, of Narkawicz--Munoz, NASA/TM-2014-218548, November2014, [official primary report](https://ntrs.nasa.gov/api/citations/20150001256/downloads/20150001256.pdf).
The statement allows positive rescaling of negative remainders and extended-real endpoints, matching the verifier's sign-variation count.
The positive initial derivative rescaling also preserves the Sturm signs and remainder property.
This standard theorem is accepted at that checked statement/applicability scope; the report's PVS formal development was not executed or independently audited here.

The [official SymPy1.14.0 polynomial reference](https://docs.sympy.org/latest/modules/polys/reference.html) was checked for the actual is_irreducible and count_roots interfaces.
The verifier tests each recorded factor over QQ using Poly.is_irreducible, whereas the author obtained it from factor_list over ZZ.
Both operations use the same installed SymPy1.14.0 engine; this is not independent symbolic-engine evidence for irreducibility.
Coefficient construction, factor multiplication, cleared identities and Sturm arithmetic are independently implemented with Python integers/Fraction and do not call SymPy polynomial operations.
The result is exact computation under these disclosed algorithm/library assumptions, not a formal proof artifact or a second-engine factorization certificate.

### Eight analytic cases and the boundary of the negative result

When both u and v are even, b=uc+v belongs to2O_F, so B_p=v_p(b)>=e_p=v_p(2) at every prime over2.
In C178's low branch G_p<e_p, its displayed valuations give2B_p=G_p, hence B_p<e_p/2, contradicting B_p>=e_p.
Therefore G_p>=e_p at all2-primes.
The full ideal-norm sum gives v_2(abs Norm_F(g))>=sum e_p f_p=r, and nonzero integrality yields abs Norm_F(g)>=2^r.
This uses exactly the full original residual hypotheses and the adopted C178 local split, without assuming an unramified prime or existence of a triple.
The eight output rows only record this analytic coverage; their labels do not constitute an independent computation of their roots or norms.

The finite result neither depends on nor reviews the later all-affine analytic argument.
The24 computed nonexistence conclusions and eight conditional analytic floors together settle only the predeclared32 choices.
The arbitrary non-affine residual norm question and G0001 remain outside this finding.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
