---
author: Yin
---

# Whole independent review of the real-or-circle raw-p2 finiteness and trace return

Review time: 2026-11-04T22:00 UTC.
Human record author: Yin.
This is an initial whole mathematical review of [C865 v1](../../claims/Yin_C_G0865_v1.md#statement), all Statement parts A--C and the complete argument, in its present fixed physical version.
The reviewing agent did not contribute to that proof and received no substantive proof-development conversation or summary.
The reviewer read the fixed candidate and its necessary mathematical inputs directly, enumerated the obligations from the full statement, and formed the initial finding before any earlier review conclusion was consulted.
No earlier R finding is used as mathematical review evidence here.
The rolling D1, proof-generation notes and author explanations outside the fixed candidate were not read.
The candidate's own contributor disclosures are part of the reviewed artifact, not independent evidence.

The new necessary evidence is the whole independent finding below; no adequate existing whole review of this fixed candidate was found.
This R records that finding without changing a Claim assessment or a Task decision.
The review uses accepted external statements at their recorded applicability scope and does not independently reprove Pritsker's potential-theory theorem or Dobrowolski's original theorem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | [C865 complete Statement](../../claims/Yin_C_G0865_v1.md#statement) | All hypotheses and conclusions A--C, actual degree and raw-p2 normalization, uniform bounded-total-measure divergence, finite sublevels, full-ring positive-unit construction, both e branches, every radial cost and finite source conclusion. |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | [C865 complete argument](../../claims/Yin_C_G0865_v1.md#argument) | All six sections, equations IN1/A1--A2/B1--B4/P1--P5, direct source matching, compact tent, constants, field generation, integrality, finite places, complete embeddings, coefficient finiteness and all stated limitations. |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | [Pri11 accepted finite discrepancy interface](../literature/Pri11/Yin_U001.md#pri11-u001) | Pritsker, Distribution of algebraic numbers, arXiv:1307.5734v1, Theorem 3.1 equation (3.2), simple integral polynomial degree at least 55, global Lipschitz constant, support radius, normalized circle probability and full Mahler measure; statement/application only. |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | [C147 v5 numerical conversion](../../claims/Yin_C_G0147_v5.md#argument) | Only the quoted Smy08 numerical M>1+x bound and equation (4) converted to total m at actual degree D>=exp(e), with constant 1/2400; no cyclic-norm envelope, small-height exclusion or positive-income premise. |
| [Whole real-or-circle and trace-return finding](#real-circle-p2-whole-independent-finding) | [Smy08 recorded source and normalization](../literature/Smy08/Yin_U001.md#smy08-u001) | Recorded arXiv:math/0701397v2 edition, Section 4.2 numerical benchmark context and height/total-measure normalization; the explicit numerical quotation is in fixed C147 v5, and the defective minimal-polynomial resultant explanation is not used. |

<a id="real-circle-p2-whole-independent-finding"></a>
## Whole finding

The complete Statement A--C is mathematically supported by the written proof and its two accepted external statement interfaces.
No mathematical gap, suppressed degree multiplier, omitted real expanding branch or unsupported existence assertion was found.
This finding concerns the fixed restricted theorem, not completion of the unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract).
The decisive checks follow.

### A: uniform divergence and finite raw sublevels

For a unit, the product formula at all archimedean embeddings gives sum a_i=0 and sum |a_i|=2m, while every finite-place logarithm vanishes.
The full Cauchy--Schwarz inequality therefore gives 2m<=M_2 at the actual degree.
Every root has modulus at most exp(m)<=exp(H).
Under the real-or-circle hypothesis only real roots have nonzero radial logarithms, and a real root of modulus one would be the rational root 1 or -1, forcing beta itself to equal that root of unity.
The supported Cauchy--Schwarz inequality is consequently M_2>=2m sqrt(D/k), with k>0 in the large-degree application by IN1.

The test phi_r(z)=max(0,r-dist(z,[-exp(H),exp(H)])) is real, nonnegative and globally 1-Lipschitz.
Its closed support is contained in the disk of radius exp(H)+r<=exp(H)+1, and its value at every real root is exactly r.
On the unit circle its segment distance is |sin(theta)| because exp(H)>=1.
Normalized circle measure of |sin(theta)|<=r is 2 arcsin(r)/pi, including r=1.
The convexity chord inequality arcsin(r)<=pi r/2 gives integral phi_r<=r^2.
All remaining root contributions are nonnegative, so retaining only the k real roots gives a valid upper bound on k/D after the discrepancy estimate.

The minimal polynomial is monic integral with D distinct roots in characteristic zero.
D>=max(55,exp(H)) supplies every Pri11 hypothesis and makes log(max(D,M))=log D.
With support radius exp(H)+1 the source factor is exactly 2exp(H)+3.
Writing q=(log D/D)^(1/4), the choice r=q lies in (0,1] and yields

    k/D<=q+(2exp(H)+3)q=(2exp(H)+4)q.

For the other input, C147 v5 quotes x=(1/1200)(log log D/log D)^3 and M>1+x.
At D>=exp(e), 0<x<=1; log(1+x)>=x/2 gives m>=(1/2400)(log log D/log D)^3.
This conversion itself needs only the stated degree threshold, not the small-height condition used in other parts of C147's cyclic argument.
Since 55>exp(e), it applies throughout the displayed A range.
Combining the two inequalities gives precisely

    M_2>=[1/(1200 sqrt(C_H))]
           D^(1/8)(log log D)^3/(log D)^(25/8).

Thus both the numerical constant and logarithmic exponent in A2 are correct.
For fixed H the expression tends to infinity; no finite-degree monotonicity is needed.
If M_2<=B, then m<=B/2, so H=B/2 yields a degree bound.
For each bounded degree, every elementary-symmetric product is bounded by the full multiplicative Mahler measure, giving coefficient bounds binom(D,j)exp(B/2).
Finite integer coefficient ranges and finitely many roots per polynomial establish the asserted finiteness without an unstated enumeration or an additional finiteness theorem.

### B: field, degree and all radial costs

For the Salem source the trace field F is totally real, and the quadratic equation for alpha makes [Q(alpha):F]<=2.
Equality one would make Q(alpha) totally real, contradicting its nonreal conjugates for d>=4.
Hence the original trace degree is exactly t=d/2.
The inverse-pair factorization gives P_alpha(X)=X^t T(X+X^(-1)), and at X=1 its nonzero endpoint norm is exactly (theta_0-2) product_(j>0)(2-theta_j) in absolute value.

Using a unit of the full O_F makes u^(-1) integral, so gamma is integral.
Total positivity gives one and only one trace value above 2.
If Q(gamma) were proper in F, its distinguished real embedding would have [F:Q(gamma)] extensions and would repeat that value above 2 among the embeddings of F.
This proves Q(gamma)=F without assuming a generic unit or a degree-preserving transform.
An embedding value gamma_j=2 or -2 would, by injectivity on gamma minus that rational number, force gamma itself to equal it, a contradiction.

The chosen beta is integral by transitivity of integrality, and beta^(-1)=gamma-beta is integral as well.
It is therefore a unit, and beta>1 excludes torsion.
Since gamma=beta+beta^(-1), its field contains F and its exact degree is D=et with e=1 or 2.
A trace in (-2,2) makes gamma^2-4 negative under a real embedding, so it cannot be a square in F and forces e=2.
If e=1, beta belongs to the totally real field F, and every trace has absolute value strictly above 2.
When all traces have absolute value above 2, the proof correctly retains both possible splitting cases.
Each conjugate is a root of a real reciprocal quadratic, so a nonreal pair has modulus one and every other root is real.

At j=0, the identity gamma_0=2+4sinh^2(m/2)/u_0 gives the stated r_0.
For j>0, a_j=(2-theta_j)/(4u_j) gives gamma_j=2-4a_j.
The a_j<1 branch has zero radius, while a_j>1 gives negative real reciprocal roots with cosh(r_j)=2a_j-1.
The formally included endpoint a_j=1 cannot occur because gamma_j=-2 has already been excluded; the radial identities are nevertheless continuous there.
This establishes r_j=2arcosh(exp(epsilon_j/2)) and epsilon_j=2log cosh(r_j/2) in every permitted branch.

Every embedding of F has e extensions to Q(beta).
For e=2 their logarithmic absolute values are +/-r_j; for e=1 the single squared logarithm is r_j^2 regardless of which reciprocal root is chosen.
Thus the sum of squares is e sum r_j^2, and multiplication by D=et gives the full factor e^2t in B1.
For e=2, one expanding root from every nonzero pair contributes to m(beta)=sum r_j, including all negative real pairs.
No formula for e=1 total measure is silently imported.

Integrating tanh(x)<=x yields log cosh(x)<=x^2/2 and therefore epsilon_j<=r_j^2/4.
Summation proves B2 with denominator 4e^2t.
The assumed output bound gives r_0<=Cm/(e sqrt(t)), and the exact r_0 identity yields B4 with denominator sinh^2(Cm/(2e sqrt(t))).
The sinh denominator is strictly positive because C,m,t and e are positive in the stated domain.
Finally the totally positive unit has norm product u_j=1, while u_j>=(2-theta_j)exp(-epsilon_j)/4 for each j>0.
Multiplication and the retained nonzero integer endpoint norm prove exactly B3, including 4^(t-1) and theta_0-2.
These are necessary costs for an actual unit and contain no unit-lattice occupancy or existence conclusion.

### C: finite source class and scope

For fixed C and 0<m(alpha)<=1 the actual outputs satisfy M_2(beta)<=C.
A bounds their degrees; B gives d=2t<=2D in both splitting cases.
The original source measure bound then gives finite integer coefficient ranges at bounded source degree, hence finitely many Salem sources.
Their logarithmic measures are strictly positive, so a nonempty class has a positive minimum, while the empty class satisfies the asserted lower-bound conclusion vacuously.
The argument neither assumes that a prescribed unit exists nor bounds the original degree using the ambient field in place of beta's actual field.

## Source completeness and review limits

The two substantive imported inequalities have precise source identities and locators, and their hypotheses, constants, normalizations and actual use were checked against the identified local accepted interfaces.
The Smy08 resultant defect is explicitly outside this proof; no step uses that mechanism.
No unresolved source-identification issue was found for these two invocations at their stated acceptance scope.
The originals were not newly downloaded or visually reread in this review, and their full original proofs and ancestor inputs were not independently audited.
The review reuses the accepted statements and independently checks the complete new deductions and interfaces.

C855 is identified by the candidate only as a reuse lead, and its unassessed proof is not needed or relied upon.
The universal raw-p2 floor, FM13 operator identities and the mutable extraction provenance are likewise not premises.
The argument is exact and uses no numerical experiments or polynomial enumeration; no computation rerun or formal proof-assistant verification is asserted.
The theorem establishes neither a novelty claim nor an unrestricted total-Mahler gap, a reduction of arbitrary reciprocal units to Salem numbers, or coverage for outputs with nonreal off-circle conjugates.
There is no remaining repair request within the reviewed Statement A--C.
Any later substantive change to the candidate or its accepted input interfaces requires checking the affected scope before reusing this finding.
