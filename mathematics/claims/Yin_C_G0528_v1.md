---
author: Yin
---

# Complete multipoint rank-seven kernel fibers, exact exclusions and all cover costs

The exact ordered multipoint architecture and its complete original L218 Sections 1--5/(1)--(10), eighteen-row certificate and four exceptional quadratics are retained below.
The original [R792 whole account](../audits/reviews/Yin_R_G0792_v1.md#multipoint-constructor-complete-independent-review) retains its 2026-10-09T21:15 full frozen-input inspection, original read-only replays and the resolved author kernel-sign failure.
An author scope/correction notice and shared-task wording alone do not establish the additional mathematical contents and their initial order; no new C coverage or retrospective relationship declaration is attributed to that old finding.

## Statement

<a id="multipoint-realization-fixed-scope"></a>

Let a,b,c,d,e,f be arbitrary integers and set
\[
B=\begin{pmatrix}1&1&0&0\\0&1&1&0\\0&0&1&1\end{pmatrix},\quad
C=\begin{pmatrix}1&a&b&c\\0&1&d&e\\0&0&1&f\\0&0&0&1\end{pmatrix},
\quad V=\begin{pmatrix}I_3&-B\\0&C\end{pmatrix}.
\]
Write p_V(t)=det(tV+V^T) and F(t)=(t+1)(t^6-t^5-t^3-t+1)=t^7-t^5-t^4-t^3-t^2+1.
Then
\[
(t+1)p_V=\det((t+1)(tC+C^T)-tB^TB),\quad
p_V=t^7+A t^6+D t^5+H t^4+H t^3+D t^2+A t+1 .
\]
The full target is equivalent to A=0,D=H=-1, or to A=0,p_V(1)=-2,p'_V(-1)=5.

Put u=-a+b-c,v=-b+c+d-e,w=-c+e-f.
The entire integer alternating kernel is generated primitively by z=(-u,-v,-w;1,-1,1,-1), and
\[
p'_V(-1)=z^TVz
=u^2+v^2+w^2+4+u-v+w-b+2c-e .
\]
With R=u^2+v^2+w^2+u-v+w-1, the condition p'_V(-1)=5 has the complete integer parameterization
\[
(a,b,c,d,e,f)=(h-u,k+h,k,k+R+v,k+R-h,R-h-w),
\quad u,v,w,h,k\in\mathbb Z.
\]
Every target realization in this architecture must satisfy max(|u|,|v|,|w|)>=2.
The proof excludes all 27 triples (u,v,w) in {-1,0,1}^3 with h,k completely unbounded, using the full printed resultant/modular certificate and its four k=0 exceptional quadratic cases.
No restriction on the six entry sizes is used in that theorem.
The separate narrower b=c=e=0 family has A=1-a(a-1)-d(d-1)-f(f-1), which is always odd and cannot realize F.

For every parameter tuple,
\[
p_V=(t+1)t^3q_V(t+t^{-1}),\quad
q_V=x^3+(A-1)x^2+(D-A-2)x+(H-D-A+1).
\]
Let V^- replace each strict upper entry by minus its absolute value.
The literal two-sheet signed cover W has complete polynomial p_V p_(V^-), rank 14, height H_0=max(1,|a|,...,|f|) and energy 2E, where V and V^- have rank 7 and E=6+a^2+b^2+c^2+d^2+e^2+f^2.
For each trace root x, including multiplicities and nonreal roots, let eta(x)>=1 be the larger modulus of the two roots of z^2-xz+1.
Then m(p_V)=sum_(q_V(x)=0)log eta(x) and m(p_W) is the sum of that full expression for V and V^-.
If d_j=(1,2,2,1)_j and ell_j is the incident core-edge square sum, both m(p_V) and m(p_(V^-)) are at most
\[
C_0=\tfrac32\log6+\tfrac12\sum_{j=1}^4\log(4+d_j+\ell_j),
\]
and m(p_W)<=2C_0.
Every factor and full absolute-companion expense is retained.

The original J47 entry box [-3,3]^6 comprised exactly 117649 tuples: 1341 were excluded by the separately proved E>=13 target condition, 116308 tested, 1255 met A=0, 13 also met D=-1, and none met the full target.
Its moduli 2,3,4,5 have respectively 4,10,32,93 target residue classes and do not themselves give a constructor-wide obstruction.
Within this finite box H_0<=3,E<=60 and C_0<=3log6/2+log1056.
The full finite box failure, unbounded 27-fiber exclusion and general full-cost formulas are distinct conclusions.
No larger-kernel exclusion, other ordered architecture exclusion, rank-seven integral witness, optimized cover cost, near-one coverage or Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:03 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | The exact fixed 3+4 integral architecture with all six entries unbounded; full determinant/endpoint conditions, primitive alternating kernel and complete five-parameter norm5 form, all27 unbounded kernel fibers and separate finite117649 box, and every original/absolute/cover factor and full cost with their distinct limitations. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(10), all18 printed modular certificate rows, reversal/leading-degree specializations/four exceptional quadratics, exact costs and actual J47 evidence including the original author kernel-sign failure and scope; no producer replay or search is newly executed. |
| dependency | [Integral signature/energy theorem](Yin_C_G0505_v2.md#statement) | Exact integer-only rank7 determinant-2 inertia(4,3) and E>=13, used solely for the original finite-box exclusions. |
| support | [Distinct common-stabilizer obstruction](Yin_C_G0521_v1.md#statement) | Comparison only: excludes common identical stabilization, not a different independently constructed rank7 form. |
| support | [Distinct pendant-forest exclusion](Yin_C_G0497_v1.md#statement) | Comparison only: arbitrary rank4 core plus unit pendant forest; this multipoint B lies outside that architecture. |
| dependency | [Literal signed cover](Yin_C_G0002_v1.md#statement) | Exact negative-entry I2/positive-entry -S2 cover convention and full determinant product; no integral diagonalizing change of basis. |
| support | [Original complete J47 evidence](../computations/programs/Yin_J_G0047/readme.md) | The fixed entry box, all27 exact fibers, full native certificates and original distinct replay evidence; no new program run or domain expansion. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | The exact fixed 3+4 integral architecture with all six entries unbounded; full determinant/endpoint conditions, primitive alternating kernel and complete five-parameter norm5 form, all27 unbounded kernel fibers and separate finite117649 box, and every original/absolute/cover factor and full cost with their distinct limitations. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(10), all18 printed modular certificate rows, reversal/leading-degree specializations/four exceptional quadratics, exact costs and actual J47 evidence including the original author kernel-sign failure and scope; no producer replay or search is newly executed. |
| dependency | [Integral signature/energy theorem](Yin_C_G0505_v2.md#statement) | Exact integer-only rank7 determinant-2 inertia(4,3) and E>=13, used solely for the original finite-box exclusions. |
| support | [Distinct common-stabilizer obstruction](Yin_C_G0521_v1.md#statement) | Comparison only: excludes common identical stabilization, not a different independently constructed rank7 form. |
| support | [Distinct pendant-forest exclusion](Yin_C_G0497_v1.md#statement) | Comparison only: arbitrary rank4 core plus unit pendant forest; this multipoint B lies outside that architecture. |
| dependency | [Literal signed cover](Yin_C_G0002_v1.md#statement) | Exact negative-entry I2/positive-entry -S2 cover convention and full determinant product; no integral diagonalizing change of basis. |
| support | [Original complete J47 evidence](../computations/programs/Yin_J_G0047/readme.md) | The fixed entry box, all27 exact fibers, full native certificates and original distinct replay evidence; no new program run or domain expansion. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g218-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R792. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | The exact fixed 3+4 integral architecture with all six entries unbounded; full determinant/endpoint conditions, primitive alternating kernel and complete five-parameter norm5 form, all27 unbounded kernel fibers and separate finite117649 box, and every original/absolute/cover factor and full cost with their distinct limitations. |
| argument | [Complete argument](#argument) | Entire original Sections1--5/equations(1)--(10), all18 printed modular certificate rows, reversal/leading-degree specializations/four exceptional quadratics, exact costs and actual J47 evidence including the original author kernel-sign failure and scope; no producer replay or search is newly executed. |
| dependency | [Integral signature/energy theorem](Yin_C_G0505_v2.md#statement) | Exact integer-only rank7 determinant-2 inertia(4,3) and E>=13, used solely for the original finite-box exclusions. |
| support | [Distinct common-stabilizer obstruction](Yin_C_G0521_v1.md#statement) | Comparison only: excludes common identical stabilization, not a different independently constructed rank7 form. |
| support | [Distinct pendant-forest exclusion](Yin_C_G0497_v1.md#statement) | Comparison only: arbitrary rank4 core plus unit pendant forest; this multipoint B lies outside that architecture. |
| dependency | [Literal signed cover](Yin_C_G0002_v1.md#statement) | Exact negative-entry I2/positive-entry -S2 cover convention and full determinant product; no integral diagonalizing change of basis. |
| support | [Original complete J47 evidence](../computations/programs/Yin_J_G0047/readme.md) | The fixed entry box, all27 exact fibers, full native certificates and original distinct replay evidence; no new program run or domain expansion. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0792_v1.md#multipoint-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:42, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

<a id="multipoint-construction-question"></a>
### 1. Reuse boundary and predeclared experiment

The prescribed input is
\[
P_6(t)=t^6-t^5-t^3-t+1,\qquad
F(t)=(t+1)P_6(t)=t^7-t^5-t^4-t^3-t^2+1.
\]
The [full energy constraint](Yin_C_G0505_v2.md#signature-energy-fixed-scope) requires every integral upper-unitriangular realization of F to have inertia(V+V^T)=(4,3) and E(V)>=13.
The [common-stabilizer obstruction](Yin_C_G0521_v1.md#stable-cancellation-fixed-scope) excludes cancellation of one Phi2 from the known rank-eight realization through adding the identical integral block on both sides.
Neither result excludes an independently constructed rank-seven form.
The [pendant-forest exclusion](Yin_C_G0497_v1.md#adjustable-core-forest-fixed-scope) covers an arbitrary integral rank-four core with three unit pendant-forest vertices.
The construction below instead attaches each of three auxiliary vertices to two core vertices.
These retained inputs supply the needed determinant, endpoint and cover conventions; the following is a direct finite-dimensional coefficient calculation, with no external theorem or novelty claim.

Set
\[
B=\begin{pmatrix}1&1&0&0\\0&1&1&0\\0&0&1&1\end{pmatrix},\quad
C=\begin{pmatrix}1&a&b&c\\0&1&d&e\\0&0&1&f\\0&0&0&1\end{pmatrix},\quad
V=\begin{pmatrix}I_3&-B\\0&C\end{pmatrix}.
\]
All seven diagonal entries are one and all variables are integers.
The exact costs are rank7, E(V)=6+a^2+b^2+c^2+d^2+e^2+f^2, and height max(1,|a|,|b|,|c|,|d|,|e|,|f|).
The original parameter box was fixed before execution to [-3,3]^6, containing117649 tuples.
Tuples of energy below13 were discarded using L210 without testing them as admissible candidates.
The other tuples were tested by complete exact polynomial coefficients; the entire declared box was completed.
No conclusion outside that entry box follows from its failure alone.
The programs and mathematical outputs are retained in J47.

For s=t+1, Schur complementation gives the polynomial identity
\[
s\det(tV+V^T)=\det\bigl(s(tC+C^T)-tB^TB\bigr). \tag{1}
\]
Indeed the upper-left block of tV+V^T is sI3, its other blocks are -tB,-B^T,tC+C^T, and the usual Schur formula holds for s nonzero; clearing its denominator gives (1) identically, including t=-1.
Thus a4-by-4 determinant suffices, with its exact divisibility by s retained.
Because V is integral upper unitriangular, p_V(t)=det(tV+V^T) is monic reciprocal of degree7 and constant term1.
It has the form
\[
p_V=t^7+A t^6+D t^5+H t^4+H t^3+D t^2+A t+1.
\]
The prescribed target is exactly the three coefficient equations A=0,D=H=-1.
As a separate equivalent check, A=tr(V^{-1}V^T), p_V(1)=2(1+A+D+H), and p'_V(-1)=7-5A+3D-H.
Hence A=0, p_V(1)=-2 and p'_V(-1)=5 also force the entire target, rather than just an endpoint or spectral-radius match.

### 2. Complete first box and an exact kernel reduction

[J47](../computations/programs/Yin_J_G0047/readme.md) executed the whole declared box:117649 tuples,1341 discarded by energy,116308 tested,1255 satisfying A=0, and13 satisfying both A=0,D=-1.
None satisfies the complete target.
The saved three exact coefficient expressions and full-determinant cross-check logic remain in the program and output.
Modular tests at2,3,4,5 have respectively4,10,32,93 admissible target residue classes; none of these moduli gives a constructor-wide obstruction.
These are finite exact diagnostics, not a claim of local solvability at every modulus.

Write v0=(1,-1,1,-1)^T.
Since B has a3-by-3 minor1, the entire integer kernel of B is Z v0.
Solving (V^T-V)(x,y)^T=0 therefore gives the entire primitive integer alternating kernel generated by
\[
z=(-u,-v,-w;1,-1,1,-1)^T,
\quad u=-a+b-c,\quad v=-b+c+d-e,\quad w=-c+e-f. \tag{2}
\]
Here u,v,w are the negatives of the auxiliary coordinates of the generator; the use of v for the second scalar coordinate is separate from v0.
The first three equations force y=q v0; the last four force x=-q(u,v,w), with no denominator and no remaining free variable.
In particular z is primitive.
Its exact norm is
\[
z^TVz=u^2+v^2+w^2+4-a+b-c-d+e-f
 =u^2+v^2+w^2+4+u-v+w-b+2c-e. \tag{3}
\]
Here is a direct proof that p'_V(-1)=z^TVz.
Put A0=V^T-V.
Its principal6-by-6 minor obtained by deleting the final core coordinate has determinant1: its off-diagonal3-by-3 block is the first three columns of B, of determinant1.
Hence A0 has rank6.
Its adjugate has all columns and rows in its one-dimensional kernel, so adj(A0)=lambda zz^T; symmetry follows because the dimension is odd and A0 is skew symmetric.
The final diagonal cofactor is1 and the final coordinate of z is-1, giving lambda=1.
Differentiating det(A0+sV) at s=0 now gives tr(adj(A0)V)=z^TVz.
Thus the alternating quotient has no hidden square multiplier in this architecture.
J47 separately checks the same polynomial identity through the full determinant.

Set R=u²+v²+w²+u-v+w-1.
The exact equation z^TVz=5 is equivalent to the following complete parameterization by five integers u,v,w,h,k:
\[
(a,b,c,d,e,f)=(h-u,\ k+h,\ k,\ k+R+v,\ k+R-h,\ R-h-w). \tag{4}
\]
Indeed choose k=c,h=b-c; (2) determines a,d,f, and (3) determines e.
Conversely substitution checks both (2) and the norm5 condition.
This handles every integer parameter tuple of norm5, without restricting matrix height or energy.
Under (4), A=0,D=-1 already imply H=-1 from7-5A+3D-H=5.


<a id="multipoint-kernel-fiber-obstruction"></a>
### 3. An unbounded-entry obstruction in the new architecture

**Proposition.** If the integral matrix V of Section1 has p_V=F, then
\[
\max(|-a+b-c|,|-b+c+d-e|,|-c+e-f|)\ge2. \tag{5}
\]
There is no restriction on the six entry sizes in this statement.
In particular the obstruction covers27 entire integer fibers, each with two otherwise unbounded parameters after imposing the necessary norm5 equation.
It is a restriction on this multipoint architecture, not an invariant of every rank-seven realization.

**Proof.** Use (4), and regard A and D+1 as polynomials in h with integer polynomial coefficients in k.
For the27 triples under consideration they have degree2 in h; write them a2 h²+a1 h+a0 and b2 h²+b1 h+b0.
Their Sylvester determinant is
\[
\mathcal R(k)=(a_2b_0-a_0b_2)^2
 -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1). \tag{6}
\]
Any simultaneous solution has Rcal(k)=0, including a specialization at which a leading coefficient vanishes: (6) is the polynomial determinant identity, so its necessary vanishing does not rely on a specialized degree assumption.

The following small modular certificate gives Rcal(k)=k^j Q(k) for each of the18 reversal representatives u<=w.
The fourth column lists the coefficients of Q modulo m in ascending powers of k, retaining zero trailing coefficients when present.
The final column is its complete value set on Z/mZ.
Each avoids zero.
All data follow by substituting the specified triple into (1),(4),(6), and can be checked by at most13 residue evaluations per row.
The full integer polynomials and a separate integer-divisor check are in J47; the table itself is a finite certificate for all integer k.

| (u,v,w) | j | m | Coefficients of Q modulo m, constant first | Value set modulo m |
| --- | --- | --- | --- | --- |
|(-1,-1,-1)|0|5|4,1,0,0,2,0,0,3,4|1,4|
|(-1,-1,0)|0|9|7,3,6,8,0,5,3,4,7|1,3,4,7|
|(-1,-1,1)|2|3|1,1,1,2,2,0,0|1|
|(-1,0,-1)|0|13|1,7,1,10,0,9,8,3,9|1,3,4,9,10,12|
|(-1,0,0)|0|11|9,10,9,3,10,10,1,7,5|1,2,3,4,7,9,10|
|(-1,0,1)|0|5|4,0,0,2,4,0,3,2,4|1,2,4|
|(-1,1,-1)|0|5|1,4,2,2,2,2,0,2,4|1,4|
|(-1,1,0)|0|5|1,3,4,3,3,1,3,4,1|1,2,3,4|
|(-1,1,1)|0|5|1,2,0,4,3,2,3,2,4|1,4|
|(0,-1,0)|0|3|1,0,1,0,2,0,2,0,1|1|
|(0,-1,1)|2|3|2,1,1,2,0,0,1|1,2|
|(0,0,0)|0|7|4,4,2,5,0,4,3,6,4|1,2,4|
|(0,0,1)|0|5|4,4,3,1,2,3,2,3,1|1,3,4|
|(0,1,0)|0|11|4,9,4,8,7,6,8,0,3|1,3,4,5,9|
|(0,1,1)|0|3|1,0,2,2,0,2,0,2,1|1|
|(1,-1,1)|0|3|1,2,2,0,0,1,1,0,0|1|
|(1,0,1)|0|3|1,0,1,2,1,1,1,0,0|1|
|(1,1,1)|0|3|1,2,2,0,0,1,1,0,0|1|

For completeness, transposing and reversing the core sends (a,b,c,d,e,f) to(f,e,c,d,b,a), hence (u,v,w,h,k) to(w,v,u,R-h,k).
The reversal matrix J4 preserves B^TB.
Therefore the matrix inside (1) for the changed core is J4 times the transpose of the original matrix times J4, and its determinant is unchanged.
Thus the pairs of h-polynomials are related by h↦R-h; both have degree2, so (6) is unchanged.
The table covers all27 triples.

When j=0, the table rules out every integer k.
When j=2, only k=0 remains.
Including the reversals, the four remaining D+1 equations in h are respectively
\[
\begin{array}{c|c|c}
(u,v,w)&(D+1)|_{k=0}&\text{discriminant}\\\hline
(-1,-1,1)&7h^2-9h+1&53\\
(1,-1,-1)&7h^2-33h+37&53\\
(0,-1,1)&4h^2-6h+1&20\\
(1,-1,0)&4h^2-18h+19&20.
\end{array}
\]
In each case A vanishes identically at k=0, but the displayed quadratic has no rational, hence no integer, root because its discriminant is not a square.
This excludes all cases and proves (5).
No energy bound or finite bound on h,k was used.
QED.

The narrower subfamily b=c=e=0 also illustrates a different exact restriction: A=1-a(a-1)-d(d-1)-f(f-1) is odd for all integers a,d,f and therefore cannot vanish.
Allowing the three omitted core edges removes that immediate parity obstruction; the full multipoint family has target solutions modulo2,3,4,5 as already recorded.
Those local tests neither establish integral solvability nor explain the complete fiber obstruction by themselves.

<a id="multipoint-complete-polynomials-costs"></a>
### 4. Complete polynomials and all representation costs

Every matrix in this family, whether or not it realizes the target, has exactly the full polynomial in (1).
In terms of its three coefficients A,D,H, this is equivalently
\[
p_V(t)=(t+1)t^3 q_V(t+t^{-1}),\qquad
q_V(x)=x^3+(A-1)x^2+(D-A-2)x+(H-D-A+1). \tag{7}
\]
This equality keeps every factor; it does not assert that the quotient is irreducible or that Phi2 is its entire cyclotomic part.
For the prescribed target, q=x³-x²-3x+1 and the entire permitted padding would be exactly one Phi2, rank7.
No such integer witness was found in this round.
The previously known rank8 realization and its two Phi2 factors remain the different settled control from L210.

Define V^- by replacing each strict upper entry of V by minus its absolute value.
It has the same fixed -B and replaces the six core variables by their negative absolute values.
Thus (1) and (7), evaluated at those six integers, are also exact formulas for its entire polynomial p_{V^-}, without keeping only a dominant root.
Both V and V^- have entry height
\[
H_0=\max(1,|a|,|b|,|c|,|d|,|e|,|f|)
\]
and squared-entry sum E=6+a²+b²+c²+d²+e²+f².

For the canonical signed cover from [D9](Yin_C_G0002_v1.md), replace each diagonal entry by I2, each negative strict upper entry v by v I2, and each positive entry v by -v S2, where S2 exchanges the two sheets.
The resulting integer upper-unitriangular W has rank14, height H0, energy2E and full polynomial
\[
p_W=p_V p_{V^-}. \tag{8}
\]
Indeed the symmetric and antisymmetric sheet subspaces yield V^- and V respectively; this real direct-sum computation proves the determinant identity without claiming an integral basis change.
Equation(8) retains at least the two displayed Phi2 factors and every other actual factor.
No cyclotomic cancellation is imposed on the integral lattice.

The complete logarithmic measure can also be read from the two trace cubics.
For each root x of q_V, counted with multiplicity, let eta(x) be the larger modulus of the two roots of z²-xz+1; eta(x)>=1 because their product is1.
Then
\[
m(p_V)=\sum_{q_V(x)=0}\log\eta(x),\qquad
m(p_W)=\sum_{q_V(x)=0}\log\eta(x)+\sum_{q_{V^-}(x)=0}\log\eta(x). \tag{9}
\]
This includes nonreal trace roots and all expanding factors.
For a hypothetical target witness the first sum would be log beta, with beta the Salem root of P6, but its extra cost remains the full second sum.
Equation(9) is an exact cost expression for every parameter tuple, not a claimed favorable upper bound for an unknown witness.

For a finite explicit upper bound, let d_j=(1,2,2,1)_j be the column degrees of B and let ell_j be the sum of squares of the three core edge weights incident to core vertex j.
On |t|=1, the first three rows of tV+V^T have squared norm at most6, and the four other rows have squared norm at most4+d_j+ell_j.
Hadamard's determinant inequality, followed by integration, gives for both signs
\[
m(p_V),\ m(p_{V^-})\le C_0
 :=\tfrac32\log6+\tfrac12\sum_{j=1}^4\log(4+d_j+\ell_j),
\quad m(p_W)\le2C_0. \tag{10}
\]
In the declared box H0<=3, E<=60 and C0<=3log6/2+log1056.
These are representation costs of the tested architecture, with no conclusion about near-one input coverage.
The unbounded h,k fibers in Section3 retain the same exact formulas (7)-(10), rather than an entry-height-independent estimate.

### 5. Evidence, correction and contribution scope

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g218-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.

The parent supplied the broad independent-realization question, assigned D85/J47, and required full costs and bounded evidence; it supplied none of equations(1)-(10), the matrix architecture, kernel reduction or elimination certificate.
The orbit subagent authored this argument and all J47 programs under Yin's continuing G0001 authorization.
L210,L214,L207 and D9 are retained reused inputs at their existing review scope.
No new external source was needed for the direct integer determinant calculation, and no external novelty claim is made.

This round finds no rank-seven realization.
It supplies a genuinely different multipoint-attachment architecture, an exact necessary kernel-coordinate restriction with no entry bound, and a full finite parameter-box failure.
It leaves unrestricted rank-seven realization open, including this architecture outside the27 excluded fibers, other multiple-attachment blocks, and different cyclotomic stabilization.
A further useful discriminating test would alter the integral kernel vector of B or the independent-vertex order and derive its own exact norm/endpoint equations before selecting another bounded experiment.
Enlarging the old six-entry box alone is not the retained next mechanism.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0792_v1.md#multipoint-constructor-complete-independent-review), with its original inspected scope and relationship.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0047](../computations/programs/Yin_J_G0047/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
