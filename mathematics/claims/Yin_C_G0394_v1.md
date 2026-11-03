---
author: Yin
---

# Exact primitive integer failure of the coefficient-one circle-zero L2 candidate

This retains the complete necessary mathematical argument from [complete original L365 failure and source comparison](../ledger/Yin_L_G0365_v1.md#circle-zero-prediction-candidate).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For a nonzero primitive integer polynomial P of degree d, let k count its unit-circle zeros with multiplicity, and let q_n minimize ||Pq||_2^2 for q(0)=1 and degree<=n, where n>=0 is an integer and n+d>0.
The proposed universal coefficient-one inequality r_n/M(P)^2>=1+k/(n+d) is false in that full primitive integer class.
The exact primitive reciprocal squarefree input P=10+9t+10t^2 has d=k=2, full M(P)=10 and, at n=1, unique optimizer q=1-(180/281)t with its zero outside the closed disk.
Its residual is r_1=46561/281 and r_1/M(P)^2=46561/28100<5/3; the actual least integer multiplier281-180t has complete product2810+729t+1190t^2-1800t^3 and energy13083641=281*46561.
Any coefficient c valid in the analogous universal inequality can therefore be at most55383/56200; no validity at that smaller coefficient is claimed.
The equality controls P=1-t^s at n=sL and the candidate's upper-trial direction are retained with their exact degrees, integer parameters and M=1.
TV07 Theorem1(i), at its actual retained statement/comparison scope, is a supremum-norm result with an unspecified positive coefficient, not an L2 theorem; reversal and root reflection preserve the applicable circle normalization, while Cauchy--Schwarz/Parseval retains the sqrt(N+1) loss.
The complete Sections1--4/(1)--(2), full coefficient arithmetic, source comparison, discovery/search limits and failed norm transfer are retained below or at their responsible original source account.
This nonmonic fixed-measure example does not refute a theorem restricted to the irreducible monic-unit core, and neither a weaker positive L2 constant nor that restriction is settled here.
No numerical scan, new source-proof audit, optimum constant, near-one counterexample or finite-to-infinite Mahler lower inference is asserted.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:38 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Complete actual prediction and cyclotomic control](Yin_C_G0392_v1.md#cyclotomic-cofactor-cancellation) | Only the actual optimizer, exact primitive denominator and equality family at n=sL, without an input-uniform estimate. |
| dependency | [Fixed-input circle normalization](Yin_C_G0380_v3.md#integer-multiplier-variational-formula) | Only original root reflection, Jensen and q(0)=1 normalization, retaining the leading coefficient and circle-zero scope. |
| dependency | [Canonical TV07 norm comparison](../audits/literature/TV07/Yin_U001.md#tv07-u001) | Only the original inspected supremum-norm statement and its normalization/application boundary; no Bernstein/source proof or L2 strengthening is adopted. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:40 |
| status | proved |
| reason | Adopt the complete exact retained local theorem/failure after actual whole SELF checking and full original source/review/input comparison. No weaker inequality, original source proof, unexplored case or new execution is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0392_v1.md#cyclotomic-cofactor-cancellation) | Only the actual optimizer, exact primitive denominator and equality family at n=sL, without an input-uniform estimate. |
| dependency | [Exact accepted input](Yin_C_G0380_v3.md#integer-multiplier-variational-formula) | Only original root reflection, Jensen and q(0)=1 normalization, retaining the leading coefficient and circle-zero scope. |
| dependency | [Exact accepted input](../audits/literature/TV07/Yin_U001.md#tv07-u001) | Only the original inspected supremum-norm statement and its normalization/application boundary; no Bernstein/source proof or L2 strengthening is adopted. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0597_v1.md#circle-zero-current-whole-finding) | Complete exact statement and entire retained proof, all actual original arithmetic/source/norm/input-class limitations, with original author and unknown whole findings separately preserved. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:56 |
| status | proved |
| reason | Adopt the actual complete independent finding after autonomous exact-statement/whole-proof reconstruction and complete original-review/source comparison. The useful candidate failure, exact source norm, original unknown and SELF relationships and every unchanged input/cost boundary remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0392_v1.md#cyclotomic-cofactor-cancellation) | Only the actual optimizer, exact primitive denominator and equality family at n=sL, without an input-uniform estimate. |
| dependency | [Exact accepted input](Yin_C_G0380_v3.md#integer-multiplier-variational-formula) | Only original root reflection, Jensen and q(0)=1 normalization, retaining the leading coefficient and circle-zero scope. |
| dependency | [Exact accepted input](../audits/literature/TV07/Yin_U001.md#tv07-u001) | Only the original inspected supremum-norm statement and its normalization/application boundary; no Bernstein/source proof or L2 strengthening is adopted. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0600_v1.md#g397v1-whole-isolated-finding) | Whole exact current statement and entire mathematical argument, all original mathematical/source-reading and useful negative scopes, upper-trial directions, complete constants, original costs and explicitly unrun limits. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="circle-zero-prediction-candidate"></a>
## 1. Precise candidate and estimate direction

Let P be a nonzero primitive integer polynomial of degree d with k circle zeros counted with multiplicity, and let q_n(0)=1 be the degree<=n finite prediction optimizer for |P|^2.
Write r_n=||Pq_n||_2^2.
The sharpened test was
\[
\frac{r_n}{M(P)^2}\ \stackrel{?}{\ge}\ 1+\frac{k}{n+d}.          \tag{1}
\]
This asks whether the coefficient1 suggested by several exact cyclotomic controls is universal; no assertion was made that it holds.
For P=1-t^s at n=sL, [L363](Yin_C_G0392_v1.md#cyclotomic-cofactor-cancellation) gives equality in(1): k=s,d=s and r_n=1+1/(L+1).
A repeated root or an evenly spaced configuration may pay more, so those controls do not settle all arrangements.

Even a valid inequality of this kind is a cost on a finite **upper** trial for M(P)^2.
It can require a longer window to approximate a fixed value accurately; it does not directly lower-bound the infinite infimum or resolve Lehmer.
All normalization and input classes must remain explicit.

<a id="primitive-integer-sharp-constant-failure"></a>
## 2. Exact primitive integer failure of coefficient1

Take
\[
P(t)=10+9t+10t^2.
\]
It is primitive, reciprocal and squarefree.
Its discriminant is -319, so its roots are a conjugate nonreal pair; their product is1, hence both have modulus1.
Thus d=k=2 and M(P)=10, retaining the full leading coefficient.

For n=1 and q=1+ct, Parseval gives
\[
\|Pq\|_2^2=281+360\operatorname{Re}c+281|c|^2.
\]
The exact unique optimizer is c=-180/281.
Its zero281/180 lies outside the closed disk, and
\[
r_1=281-\frac{180^2}{281}=\frac{46561}{281},\qquad
\frac{r_1}{M(P)^2}=\frac{46561}{28100}<\frac53=1+\frac23.        \tag{2}
\]
The strict integer comparison is 3*46561=139683<140500=5*28100.
No root approximation or numerical scan was used.

The actual primitive integer multiplier Q=281-180t has constant281 and product
\[
PQ=2810+729t+1190t^2-1800t^3.
\]
Its full coefficient energy is
\[
2810^2+729^2+1190^2+1800^2=13083641=281\cdot46561.
\]
Dividing by281^2 reproduces r_1 exactly, in agreement with the primitive denominator formula.
Thus(1) fails on an actual primitive integer input, not only in an unconstrained complex shadow.
More generally a universal coefficient c in its place could be at most55383/56200, as follows by solving c<=(r_1/M^2-1)*3/2.

This control is **nonmonic**, with total m(P)=log10 already bounded away from zero.
It does not exclude a theorem restricted to the irreducible monic-unit hard core, or a weaker absolute positive coefficient in a general L2 inequality.
Its purpose is to reject the exact proposed coefficient and expose the input-class and norm distinctions before investing in a uniform argument.

<a id="supremum-versus-l2-source-boundary"></a>
## 3. The related primary theorem controls a different norm

The bounded source screen found [TV07-U001](../audits/literature/TV07/Yin_U001.md#tv07-u001), Theorem1(i), printed p.593/PDFp.1.
That source gives an absolute positive coefficient for the **supremum** norm of a monic complex degree-N polynomial with k circle zeros.
Coefficient reversal gives its constant-term-one formulation.
The source was acquired and the exact statement and normalization were checked; its full original proof was not independently re-audited.

For a degree<=N polynomial, the ordinary Cauchy--Schwarz/Parseval conversion is
\[
\|R\|_\infty\le\sqrt{N+1}\|R\|_2.
\]
Accordingly the source's lower infinity norm supplies only an L2 lower bound divided by sqrt(N+1), which can be weaker than the elementary constant coefficient floor1.
The opposite inequality ||R||_2<=||R||_infinity cannot transfer a lower bound at all.
No theorem of TV07 is stated as an L2 result here, and its unspecified source constant is not replaced by1.

For the original symbol one may reflect the roots of P and divide its modulus by M(P), as in L359, obtaining an outer polynomial O(0)=1 with |P|=M(P)|O| on the circle.
It preserves circle roots and degree cannot increase.
The source comparison therefore has a meaningful normalized circle object, but still retains its supremum norm.
This is a comparison interface, not a proof of(1).

The related primary curves PDF was used only to locate the circle source and norm type.
The sufficient source check stopped at TV07, rather than acquiring or re-auditing general Jordan-curve results.
No historical priority claim is made.

## 4. Outcome, review and continuation

The exact coefficient1 circle-zero L2 candidate is refuted within its stated unrestricted primitive integer domain.
The monic-unit specialization and a weaker general L2 coefficient remain open here.
Any continuation should identify a correctly normalized original integer class and the exact norm in which a root constraint is being paid, with an implication useful for the unrestricted Task.
Merely quoting a supremum-norm theorem or reusing cyclotomic equality controls does not provide that implication.
