---
author: Yin
---
# Trace-cusp obstruction and degree-two/four nonvanishing of the reciprocal two-prime auxiliary

Human author Yin.
New G0001 author inquiry assigned to g_bridge_audit.
Root supplied the existing nonvanishing question, not proof steps.
The author retains all new mathematics here.
The declared native discriminator has its actual [J96 home](../computations/programs/Yin_J_G0096/readme.md); its execution and mathematical limits are recorded below.

## Exact question and scope

Let P be an ACTUAL monic irreducible reciprocal nontorsion integer-unit polynomial with constant1, degree d=2r.
Is it possible that P divides H_P(t)=9P(t^2)^3-8P(t^3)^2?
Equivalently, at an original root alpha, can the two known nonzero integral quotients u2=P(alpha^2)/2 and u3=P(alpha^3)/3 satisfy u2^3=u3^2?
Prove nonvanishing in the full stated domain, find a verified actual counterexample/family, or preserve a concrete structural reduction.
A nonzero conclusion alone would NOT pay the original coefficient/Archimedean expense or prove a gap.

<a id="statement"></a>
The completed author round proves the exact trace-field cusp equivalence in Section1 and nonvanishing for every admissible original polynomial of degree2 in Section2.
Section4 gives a computation-assisted classification of ALL monic reciprocal integer quartics with constant1: precisely Phi5, (t^2-1)^2, (t-1)^2 Phi3 and (t-1)^4 divide their H.
Consequently all admissible degree4 inputs are nonvanishing.
The quartic classification depends on the exact retained J96 elimination and factorization, whose independent reproduction is outstanding at author freeze.
Both degree statements transfer to ACTUAL irreducible compositions P(t)=Q(t^N), N>=1, from their indicated degree2/4 bases.
No assertion covers all higher-degree reciprocal inputs, supplies near-one examples, or pays the Archimedean bound required for a gap.

<a id="argument"></a>
The complete argument consists of Sections1--5, including the full native interface, exceptional-branch analysis and remaining costs.
Section3 retains the original pre-execution declaration; Section4 records its actual outcome rather than changing that declared range.

## Bounded reuse before the new proof

Read the actual retained [C146v1 different-prime calculation](Yin_C_G0146_v1.md#different-prime-defect-calculation) and its corrected [BS09-U001v2 source interface](../audits/literature/BS09/Yin_U001.md#bs09-u001).
The full free-ring mixed-derivation identity, H(alpha)/72=u2^3-u3^2, degree6d, constant1 and the dense coefficient bound are OLD and will be cited rather than rederived.
These facts do not make H(alpha) nonzero.
The ordinary linear two-prime coefficient-space and projection approaches remain covered by L54--56 and are not restarted.

Read L66's exact reciprocal trace field, trace polynomial, C2/C3 substitutions, integral theta quotients and full two-copy/norm identities.
In particular a trace-field argument must keep the ORIGINAL quadratic extension, and no total-real/Salem assumption may be imposed on the general reciprocal input.
The intended first reduction is in that actual trace field.
The elementary rational parametrization of the cusp x^3=y^2 may identify a stronger integral condition, but it is not itself a nonvanishing theorem.
An initial overbroad local text query was truncated; the corrected exact-string G search found only the current C146 two-prime passage at the needed displayed expression.
This is a bounded reuse observation, not a global novelty claim.

Any continued symbolic or finite exact search will first receive its own declared J home with retained native program, exact ranges, useful outcomes and independent-reproduction boundary.
No mathematical code or output belongs in temporary operational storage.

<a id="trace-cusp-exact-reduction"></a>
## 1. Exact trace-field cusp condition, with the order boundary retained

Use the adopted [C243 trace setting](Yin_C_G0243_v1.md#reciprocal-trace-domain): z=alpha+alpha^(-1), F=Q(z), [Q(alpha):F]=2, and P(t)=t^r T(t+t^(-1)) for the actual monic irreducible integer T of degree r.
Put C2(x)=x^2-2 and C3(x)=x^3-3x.
The retained [integral trace quotient](Yin_C_G0243_v1.md#reciprocal-frobenius-two-copy-module) gives nonzero elements

    a=theta2(z)=T(C2(z))/2 in B=Z[z],
    b=theta3(z)=T(C3(z))/3 in B,
    u2=alpha^(2r)a, u3=alpha^(3r)b.                    (1)

No all-power degree-preservation or total-reality hypothesis is needed here.
Let

    J_T(x)=9T(C2(x))^3-8T(C3(x))^2.

The previously retained reciprocal substitution, not a new free-ring derivation, gives

    H_P(alpha)=alpha^(6r) J_T(z),
    P divides H_P iff T divides J_T iff a^3=b^2.        (2)

The divisibilities are in Q[t] and Q[x], respectively, and therefore in the corresponding integer polynomial rings because the divisors are monic.
The factor alpha^(6r) is a nonzero unit.
J_T is monic of degree6r, and H_P retains degree6d; halving the trace degree does not delete the original quadratic norm multiplicity.

If(2) holds, define v=b/a in the ACTUAL field F.
Since a,b are nonzero, the elementary cusp calculation gives

    v^2=a, v^3=b.                                    (3)

Conversely(3) implies(2).
In particular v is an algebraic integer: it satisfies X^2-a over the integral elements of F, so integrality is transitive over Z.
Thus v belongs to the FULL O_F.
Membership v in the monogenic order B does NOT follow from v^2,v^3 in B without a further order property, and is not assumed.
Nor is v a unit unless its actual norm or ideal valuations establish that separately.

Necessary consequences include: every real embedding of F sends a to a strictly positive real number; Norm_F(a)=Norm_F(v)^2 is a positive INTEGER square; Norm_F(b)=Norm_F(v)^3 is an integer cube with its actual sign; and at each prime ideal of O_F the nonnegative valuations of a,b are respectively twice and three times the same integer.
These are exact necessary conditions, not a proof that the simultaneous conditions are impossible.
A trace norm which is merely a square after returning to the degree2r original field supplies no such new evidence: L66 already explains that automatic square.

<a id="quadratic-original-nonvanishing"></a>
## 2. Complete nonvanishing in original degree two

For P(t)=t^2-A t+1, the original integer-unit/nontorsion/irreducible domain is exactly integer A with |A|>2.
The trace polynomial is T(x)=x-A.
Substitution in(2) gives

    J_T(A)=(A-2)^2 f(A),
    f(A)=A^4-23A^3-59A^2-45A-18.                     (4)

This expansion is checked directly from T(C2(A))=(A-2)(A+1) and T(C3(A))=A(A-2)(A+2).
For A=-B with B>=3,

    f(-B)=B^4+B^2(23B-59)+45B-18>0.

For3<=A<=23, the form A^3(A-23)-59A^2-45A-18 is strictly negative.
The remaining two integers have f(24)=-21258 and f(25)=-6768.
For A>=26,

    f(A)>=A^2(3A-59)-45A-18
          >=19A^2-45A-18>0.

Therefore f has no zero in the stated integer domain, and P does not divide H_P.
This is a full degree-two statement, not an enumeration with a coefficient cutoff.
It gives no conclusion for arbitrary higher-degree trace fields.

More generally, if an ACTUAL irreducible original polynomial is P(t)=Q(t^N) with N>=1 and Q(t)=t^2-A t+1, |A|>2, then H_P(alpha)=H_Q(alpha^N)!=0 by the same degree-two conclusion.
The irreducibility premise is retained; arbitrary substitutions need not preserve it.
Such fixed-base radical extensions do not supply a hypothetical near-one sequence or a full-domain answer.

<a id="two-prime-native-predeclaration"></a>
## 3. Bounded exact symbolic discriminator declared before execution

The first native scope will have ONE author run under an aggregate180-second supervisor, after its own J allocation and source inspection.
Use the shared repository Python environment and exact SymPy1.14.0 integer/rational polynomial arithmetic; no random inputs or numerical roots are needed.

First retain exact H remainders and full polynomial factorization for these fixed controls: t^2-3t+1; t^2+3t+1; t^4-t^3-t^2-t+1; t^4-3t^3+3t^2-3t+1; t^4-4t^2+1; the actual degree10 Lehmer polynomial; Phi5=t^4+t^3+t^2+t+1; Phi7=sum_(j=0)^6 t^j; and(t-1)^2.
The last three explicitly test torsion/reducible zero branches and are NOT admissible counterexamples.
A nonzero finite control does not prove the general question.

Then compute the FULL SYMBOLIC remainder of J_T(x) modulo T(x) for T=x^2-Ax+B in Z[A,B][x].
Retain both coefficient polynomials, their gcd, the resultant eliminating B and the resultant eliminating A, and their exact factorizations.
If a nonzero elimination polynomial results, retain all its integral linear-root candidates and, after substitution, the exact gcd in the remaining parameter and all its integral roots.
A zero elimination or a whole surviving parameter line is retained as unresolved, not silently called a finite classification.
For every resulting isolated integer pair, retain the original quartic P=t^4-A t^3+(B+2)t^2-A t+1, exact H remainder, factorization, irreducibility and cyclotomic checks.
The computation is exploratory until its analytic projection/completeness argument and independent reproduction are checked.

No larger coefficient box, additional trace degree, Gröbner search, changed range, precision or retry is included in this initial run.
Partial stages and the first failure or timeout will remain in the J record.
Any consequential counterexample must still have every actual original-domain hypothesis verified, and any all-quartic claim must pay the elimination completeness and all exceptional parameter branches.
No new program has yet run at this declaration.

<a id="quartic-exact-classification"></a>
## 4. Full quartic classification and the actual native proof interface

The author calculation completed on 2026-10-15.
The exact [program](../computations/programs/Yin_J_G0096/main.py) and complete result (`mathematics/computations/outputs/Yin_J_G0096/results.json`) retain the nine-control and full symbolic trace-quadratic scope.
No retry or scope extension occurred; inspecting the saved payload afterward was not another mathematical run.
These author calculations remain distinct from the separately recorded independent reconstruction.

Every monic reciprocal integer quartic with constant1 has a UNIQUE expression

    P=t^4-A t^3+(B+2)t^2-A t+1,
    T=x^2-Ax+B,                         A,B in Z.       (5)

This parametrization does not require irreducibility.
In the quotient Z[A,B][x]/(T), represent ux+v by the pair(u,v).
Its multiplication is exactly

    (u,v)*(u',v')=(Auu'+uv'+u'v, vv'-Buu').            (6)

Set c=A^2-B-3.
Direct substitution gives the following SMALL reconstruction of the two inputs to the native remainder:

    T(C2(x)) = [A(A^2-A-2B-4)]x
                  -A^2B+AB+2A+B^2+5B+4,
    T(C3(x)) = [Ac(c-2B-1)]x
                  +B[-c^2+A^2(B+1)+1]       modulo T. (7)

Let U(A,B)x+V(A,B) be nine times the cube of the first pair in(7) minus eight times the square of the second, using(6).
The author program separately computes this defined remainder by polynomial composition/division; this is not independent reproduction.
Its full coefficient polynomials, coefficients and factorizations occur at `trace_quadratic.coefficient_x` and `.coefficient_1`; their gcd is1.
For every integer specialization, monic division commutes with specialization.
Thus T divides J_T if and only if

    U(A,B)=V(A,B)=0.                                   (8)

The equivalence with P dividing H does not rely on T or P being irreducible in this quartic classification.
Indeed H=t^(12)J_T(t+t^(-1)), and reduction of J_T modulo T gives the remainder Ux+V in the injective coefficient module generated by1,x.
Equivalently, the map Z[A,B][x]/(T) into the Laurent quotient by P sends x to t+t^(-1), and is injective: the resulting t^(-1)(U t^2+V t+U) cannot be divisible by the monic degree4 P unless U=V=0.
The factor t is invertible because P has constant1.
After specializing A,B, the same degree argument applies even when P has repeated roots.

The exact native resultant, with B eliminated, is

    Res_B(U,V) = -A^8(A+1)^4(A-1)^6(A-4)^6
                   *(A^3-32A^2+80A+32)^2*R36(A).      (9)

Here R36 is the following exact monic polynomial, also retained with its full coefficient vector in J96:

```text
A^36-180A^35+13534A^34-540490A^33+11770348A^32
-114864754A^31-262331314A^30+13148388170A^29-15611822701A^28
-834338855938A^27-727247776684A^26+31228769262968A^25
+165614693805728A^24+176402321229872A^23-1332504884780656A^22
-6240323227931872A^21-10540443341070832A^20+3925536672033248A^19
+60824438493508288A^18+155111749102644992A^17+230523558630612928A^16
+219317254472817024A^15+118825661399252800A^14+6854710714485120A^13
-38244971717832000A^12-16060617293008896A^11+15082838630141760A^10
+15889459278137472A^9-2220678301941504A^8-12140747365814784A^7
-7504730327771136A^6+544177950105600A^5+3598184804696064A^4
+2487460466589696A^3+854184926380032A^2+144457797206016A
+9588782923776.
```

The native complete rational factorization treats the displayed cubic and R36 as irreducible; in particular neither has a rational, and hence neither has an integer, root.
This is an ACTUAL computational premise of the classification, not a fact inferred merely from the polynomial's degree or from unsuccessful bounded search.
Independent reproduction must check that factorization or supply a separate no-integer-root certificate, as well as(9).
The other resultant `trace_quadratic.resultant_eliminate_A` is nonzero and fully retained as a second calculation; the proof needs only(9).

If(8) holds at a finite pair(A0,B0), the specialized Sylvester determinant defining(9) vanishes.
This implication remains valid when a leading coefficient specializes to zero: both polynomials still have the common finite root B0, so evaluation at B0 annihilates the Sylvester polynomial span.
Possible degree drops may create additional resultant zeros, but do not lose actual solutions.
Therefore every integral solution has A in{-1,0,1,4}.
The exact specialized gcds are:

| A | gcd of U(A,B), V(A,B) in Q[B], monic | Integral roots B |
| --- | --- | --- |
| -1 | (B+1)^2 | -1 |
| 0 | (B+4)^2(B^4+31B^3+103B^2+117B+36) | -4 |
| 1 | (B+2)^2 | -2 |
| 4 | (B-4)^2 | 4 |

The remaining quartic factor in the A=0 row is irreducible in the native complete rational factorization.
In this exceptional row U(0,B) is identically zero, but V(0,B) is the displayed nonzero degree6 polynomial; it is NOT an unrestricted vertical line.
In every row the gcd is nonzero, and both elimination resultants are nonzero, so there is no unhandled whole-line or zero-resultant branch.
The full specialized U,V,gcd and integer candidates remain in `trace_quadratic.specialized_branches` rather than only in this table.

Substitution into(5), and exact original-polynomial remainders, give:

| (A,B) | Original P | Why outside the intended domain |
| --- | --- | --- |
| (-1,-1) | t^4+t^3+t^2+t+1=Phi5 | Torsion |
| (0,-4) | (t-1)^2(t+1)^2 | Reducible, all roots torsion |
| (1,-2) | (t-1)^2(t^2+t+1) | Reducible, all roots torsion |
| (4,4) | (t-1)^4 | Reducible, torsion |

All four have zero original H remainder; no admissible quartic remains.
The factorization and original remainders are retained at `trace_quadratic.isolated_integer_candidates`.
Thus this is a full integer-parameter classification, not a coefficient-box search.
The nine separate fixed controls have zero remainder only for Phi5, Phi7 and(t-1)^2; all six stated nontorsion controls have nonzero remainder.
In particular the degree10 Lehmer control is only ONE verified original polynomial, not a theorem about its degree or any hypothetical near-one sequence.

For any actually irreducible composition P(t)=Q(t^N), with Q one of the admissible degree2/4 inputs, the earlier identity H_P(alpha)=H_Q(alpha^N) gives the same nonvanishing.
For Q of degree4, irreducibility means alpha^N is a root in its stated domain.
No irreducibility claim for arbitrary compositions is being made.

<a id="two-prime-unresolved-costs"></a>
## 5. Failed shortcuts, original norm expense and the remaining question

The cusp reduction does not by itself exclude higher-degree trace fields.
The fact that a is a square at every real embedding would be useful only if one could force a negative embedding for the actual P; general reciprocity does not do this.
Even the trace polynomial x^2-3x+1 has a root z=(3-sqrt(5))/2 in(-2,2) for which T(z^2-2)=10>0 (use z^2=3z-1), so an individual circle conjugate does not force the desired negative sign.
The original field norm square from reciprocity is already automatic by L66 and cannot be counted as a new cusp obstruction.
Membership v in the monogenic trace order remains unproved even though v is integral in the full ring.
These points exclude the corresponding proposed shortcuts, not the original nonvanishing question.

Likewise, isolating every integral point in this PARTICULAR two-parameter quartic elimination cannot be extrapolated to higher trace degree.
No coefficient cutoff, genericity argument or empirical absence of a counterexample replaces the missing all-degree step.
The general target is now precisely whether an actual irreducible nontorsion trace polynomial T of higher degree can have T(C2(z))/2=v^2 and T(C3(z))/3=v^3 in its full trace ring.
The quartic torsion/repeated controls show why irreducibility and nontorsion must stay in the hypotheses; they are not near-one counterexamples.

Finally, even if H(alpha)!=0 in a retained class, only then does the old identity produce a nonzero algebraic integer beta=H(alpha)/72 and

    log|Norm_(Q(alpha)/Q) H(alpha)| >= d log72.         (10)

Every original conjugate still appears here, and neither the trace reduction nor the cusp parameter removes the original degree d.
The old coefficient estimate has

    deg H=6d,
    ||H||_1 <= 9||P||_1^3+8||P||_1^2,
    log|Norm H(alpha)|
       <= d log(9||P||_1^3+8||P||_1^2)+6d m(P).        (11)

The last inequality follows from |H(alpha_i)|<=||H||_1 max(1,|alpha_i|)^(6d) and multiplying all ORIGINAL conjugates.
It is only a crude paid upper bound.
Inserting the general coefficient estimate ||P||_1<=2^d exp(m(P)) leaves a term of order d^2, so(10)--(11) do not supply an original O(d) archimedean cost or a uniform Mahler gap.
No cyclic-norm modulus has been applied to this nonmultiplicative difference without a valid new interface.

The mathematically complete outcome of this bounded round is the trace-cusp equivalence, all-degree2 analytic exclusion, the native full-degree4 classification subject to independent reproduction, and their stated composition corollary.
The all-degree nonvanishing question and the small-measure Archimedean income comparison remain open.
Root contributed the question only; the trace/cusp, sign analysis, elimination interpretation and paid-return reasoning in this draft are g_bridge_audit's author work.
There is no claim of independent review or field-wide novelty.

<a id="author-freeze"></a>
Author freeze2026-10-15T14:40: the complete statement, Sections1--5/formulas(1)--(11), native declaration/results/branch interpretation and original norm costs have been self-checked.
The source reconstruction in(7) was checked by direct quotient-ring multiplication; the degree2 signs and all native surviving original factors were checked against their stated domains.
The independent native and whole-proof reviews remain outstanding.
The original author handoff supplied main.py, the complete mathematical results and the J96 account for the different verifier.
That actual relationship is retained without a permanent duplicate progress/execution archive requirement; the author did not write the separate verifier.

## Fixed organization

Retain the entire completed trace-cusp inquiry, all five sections and eleven formulas, the native full quartic classification, useful failed sign/order shortcuts, original norm and coefficient costs, and composition scope.
The general higher-degree nonvanishing and gap questions remain open.
g_bridge_audit supplied the new proof and J96 author implementation; root supplied the question and this retention only.
Independent native reproduction and whole review remain to be completed on this actual fixed artifact.

## Current assessment
[Selected decision](#decision-current-local-trace-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T14:43 |
| status | open |
| reason | Retain the full trace-cusp equivalence and degree-two/four nonvanishing candidate, including exact all-integer quartic elimination, exceptional branches and original costs. Independent native reproduction and complete review are pending. No all-degree nonvanishing or uniform gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete stated scope](#statement) | General actual trace-cusp equivalence; all admissible degree2/4 nonvanishing, full quartic zero classification and actual irreducible composition consequences. |
| argument | [Whole author argument](#argument) | Sections1--5 and all eleven formulas, native projection completeness and all exceptional branches, useful failed inferences and full original costs. |
| dependency | [Existing two-prime integer identity](Yin_C_G0146_v1.md#different-prime-defect-calculation) | H(alpha)/72=u2^3-u3^2, nonzero individual quotients, degree6d and complete coefficient bound; no prior nonvanishing of H is assumed. |
| dependency | [Actual reciprocal trace setting](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual trace polynomial/field and quadratic extension for irreducible reciprocal nontorsion units. |
| dependency | [Integral trace quotients](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module) | Exact nonzero theta2/theta3 quotients in Z[z] and two-copy norm boundary. |
| support | [Exact native elimination evidence](../computations/programs/Yin_J_G0096/readme.md) | Nine declared controls and full symbolic trace quadratic, both resultants, factorization, integer projection and candidate verification; author run only until independent reproduction. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T14:50 |
| status | proved |
| reason | Adopt the entire trace-cusp equivalence and degree-two/four result after actual whole noncontributor R365 and complete independent J96 native reproduction. Every integral quartic parameter and exceptional branch is covered at the stated computational scope. General higher-degree nonvanishing, controlled Archimedean expense and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete stated scope](#statement) | General actual trace-cusp equivalence; all admissible degree2/4 nonvanishing, full quartic zero classification and actual irreducible composition consequences. |
| argument | [Whole author argument](#argument) | Sections1--5 and all eleven formulas, native projection completeness and all exceptional branches, useful failed inferences and full original costs. |
| dependency | [Existing two-prime integer identity](Yin_C_G0146_v1.md#different-prime-defect-calculation) | H(alpha)/72=u2^3-u3^2, nonzero individual quotients, degree6d and complete coefficient bound; no prior nonvanishing of H is assumed. |
| dependency | [Actual reciprocal trace setting](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Actual trace polynomial/field and quadratic extension for irreducible reciprocal nontorsion units. |
| dependency | [Integral trace quotients](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module) | Exact nonzero theta2/theta3 quotients in Z[z] and two-copy norm boundary. |
| support | [Exact native elimination evidence](../computations/programs/Yin_J_G0096/readme.md) | Nine declared controls and full symbolic trace quadratic, both resultants, factorization, integer projection and candidate verification; actual author run and separately implemented complete native reproduction, with shared exact SymPy kernels and no formal verification. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0365_v1.md#trace-cusp-quartic-whole-independent-finding) | Entire statement and five proof sections/eleven formulas, original input/cost scope, independent symbolic reconstruction and complete quartic projection, with all native and contribution limits disclosed. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General actual trace-cusp equivalence; all admissible degree2/4 nonvanishing, full quartic zero classification and actual irreducible composition consequences. |
| argument | [Argument](#argument) | Sections1--5 and all eleven formulas, native projection completeness and all exceptional branches, useful failed inferences and full original costs. |
| dependency | [Dependency](Yin_C_G0146_v1.md#different-prime-defect-calculation) | H(alpha)/72=u2^3-u3^2, nonzero individual quotients, degree6d and complete coefficient bound; no prior nonvanishing of H is assumed. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Actual trace polynomial/field and quadratic extension for irreducible reciprocal nontorsion units. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-frobenius-two-copy-module) | Exact nonzero theta2/theta3 quotients in Z[z] and two-copy norm boundary. |
| support | [Support](../computations/programs/Yin_J_G0096/readme.md) | Nine declared controls and full symbolic trace quadratic, both resultants, factorization, integer projection and candidate verification; actual author run and separately implemented complete native reproduction, with shared exact SymPy kernels and no formal verification. |
| review | [Review](../audits/reviews/Yin_R_G0365_v1.md#trace-cusp-quartic-whole-independent-finding) | Entire statement and five proof sections/eleven formulas, original input/cost scope, independent symbolic reconstruction and complete quartic projection, with all native and contribution limits disclosed. |

