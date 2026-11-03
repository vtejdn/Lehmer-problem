---
author: Yin
---

# Exact trace and saturated-orbit lattice restrictions on rational conjugate convex means

The complete original mathematical argument is retained from [L433](../ledger/Yin_L_G0433_v1.md#trace-lattice-existence-boundary).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The complete local trace/saturation analysis is dated2026-10-18T12:51 and was retained2026-10-20T08:54 at its author level. DJ20-U001 owns the exact accepted paired totally-real-output reduction; C484/R395 own the separate near-one hull obstruction. Those accounts are not prospective whole review of the present general statement.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Let alpha be an algebraic integer of actual degree d>=1, X={x_1,...,x_d} its FULL distinct rational conjugate set and L its splitting field.
Put G=Gal(L/Q),tau=Tr_(Q(alpha)/Q)(alpha) in Z and
    P_Q={sum_i lambda_i x_i:lambda_i in Q,lambda_i>=0,sum_i lambda_i=1}.
The SAME rational coefficients are used at every embedding; a planar convex hull allowing unrelated real coefficients is a different object.
For EVERY y in P_Q, with N=[Q(y):Q],
    Tr_(L/Q)(y)/[L:Q]=tau/d,
    Tr_(Q(y)/Q)(y)/N=tau/d.
Consequently
    P_Q intersect Q={tau/d},
    P_Q intersect Z={tau/d} if d divides tau, and empty otherwise.
Thus a NONZERO rational integer output exists exactly when tau is a nonzero multiple of d; tau=0 supplies only0.
For every algebraic-integer output y in P_Q,
    d/gcd(d,tau) divides N,
with gcd(d,0)=d.
This own-degree divisibility is necessary, not sufficient; arbitrary positive rational weights cannot create a different rational output.

Let V=span_Q(X),Lambda=sum_i Z x_i and Lambda_sat=O_L intersect V.
If BOTH the x_i are Q-linearly independent and Lambda_sat=Lambda, then
    P_Q intersect O_L=X.
Indeed every integral output has unique integer coordinates in this specific conjugate lattice, and nonnegative coordinates of sum1 select a vertex.
In the independent case, a nonvertex integral point therefore requires a genuine saturation enlargement; that requirement alone does not supply one.
With additive relations, no corresponding vertex-only conclusion is asserted.
A normal integral basis for an unrelated generator theta does not identify theta with alpha or provide an integral simplex point; for its own independent saturated orbit it has the same vertex-only property.
No normal-integral-basis existence or ramification theorem is imported.

Now let alpha be a genuine Salem number of degree d=2t>=4, label all inverse pairs x_(2j)=x_(2j-1)^-1 and put b_j=x_(2j-1)+x_(2j).
Let F=Q(b_1,...,b_t), the totally real normal closure of the ACTUAL degree-t trace field Q(alpha+alpha^-1) inside L, and let L_tr be the elements of L that are TOTALLY real over Q.
At the exact accepted DJ20-U001 scope,
    P_Q intersect L_tr=(1/2)conv_Q{b_1,...,b_t},
    P_Q intersect O_L intersect L_tr
       =O_F intersect[(1/2)conv_Q{b_1,...,b_t}].
The half factor and rational weight sum1 are retained.
This applies to totally real outputs, not merely to a real value in one displayed embedding, and supplies no nonzero integral point or conclusion about all nonreal integral outputs.
For genuine Salem alpha, Q(alpha) is displayed inside R but has nonreal conjugates, hence is not normal; [L:Q]>d, so the d conjugates of alpha cannot be a Q-basis of L or a normal integral basis of O_L.
They could still be a basis of their smaller rational span, whose saturation is a separate arithmetic hypothesis.
The general trace/saturation conclusions have no small-measure premise and do not reopen the separately excluded near-one supply mechanism, supply a new gap class, field construction or unrestricted Mahler conclusion.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:36 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every algebraic integer and its full rational conjugate set, exact normalized trace/rational-output/own-degree denominator identities, conditional independence+saturation vertex-only result, exact genuine-Salem totally-real half-trace reduction and no integral supply/normal-basis inference. |
| argument | [Entire complete argument](#argument) | Every algebraic integer and its full rational conjugate set, exact normalized trace/rational-output/own-degree denominator identities, conditional independence+saturation vertex-only result, exact genuine-Salem totally-real half-trace reduction and no integral supply/normal-basis inference. |
| dependency | [Exact fixed input](../audits/literature/DJ20/Yin_U001.md#dj20-u001) | Exactly paired-rational-convex-hull: Exact accepted totally-real-output theorem and directly proved paired rational convex hull with coefficient half factor and normal-closure/actual-trace-field distinction; source proof scope unchanged. |
| support | [Exact fixed input](Yin_C_G0484_v1.md#conjugate-hull-statement) | Separate already adopted near-one integral-hull rigidity at its actual hypotheses; a boundary comparison, not a premise for the general trace/saturation proof. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:41 |
| status | proved |
| reason | Under current human maintenance authorization, adopt the exact complete current Statement and original Argument after the actual R757 whole constructor SELF inspection. Preserve original dates, source/author/checking/interface limits, open summary predecessor and every unresolved arithmetic/near-one boundary. No new research or producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every algebraic integer and its full rational conjugate set, exact normalized trace/rational-output/own-degree denominator identities, conditional independence+saturation vertex-only result, exact genuine-Salem totally-real half-trace reduction and no integral supply/normal-basis inference. |
| argument | [Entire complete argument](#argument) | Every algebraic integer and its full rational conjugate set, exact normalized trace/rational-output/own-degree denominator identities, conditional independence+saturation vertex-only result, exact genuine-Salem totally-real half-trace reduction and no integral supply/normal-basis inference. |
| dependency | [Exact fixed input](../audits/literature/DJ20/Yin_U001.md#dj20-u001) | Exactly paired-rational-convex-hull: Exact accepted totally-real-output theorem and directly proved paired rational convex hull with coefficient half factor and normal-closure/actual-trace-field distinction; source proof scope unchanged. |
| support | [Exact fixed input](Yin_C_G0484_v1.md#conjugate-hull-statement) | Separate already adopted near-one integral-hull rigidity at its actual hypotheses; a boundary comparison, not a premise for the general trace/saturation proof. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0757_v1.md#current-g434-complete-self-finding) | Entire exact current Statement and complete Argument with all listed actual fixed interfaces, all domains, quantifiers, normalization, source and upper/lower estimate boundaries; constructor SELF. |

## Complete original argument

<a id="argument"></a>

### Original account: Trace and saturation obstructions for rational conjugate convex means

Date of the mathematical analysis: 2026-10-18T12:51.
Human author Yin.
Root proposed investigating automatic algebraic-integer points in the conjugate convex hull and supplied the Dubickas--Jankauskas primary-source lead.
The entropy_attainment_bridge AI authored the bounded trace-lattice analysis.
The general trace and saturation deductions are retained on 2026-10-20T08:54 at their original author-checked scope, without independent review or Claim adoption.
The [L399 hull obstruction](Yin_C_G0484_v1.md#conjugate-hull-statement), independently checked in [R395](../audits/reviews/Yin_R_G0395_v1.md#conjugate-combination-whole-independent-finding), has closed the proposed near-one supply mechanism when q(alpha)<2.
The general formulas below have no small-measure hypothesis; they retain necessary conditions and a useful failure of normal-basis reasoning without reopening that excluded supply problem.
The totally real half-trace reduction is reused from [DJ20-U001](../audits/literature/DJ20/Yin_U001.md#paired-rational-convex-hull), whose inspected source and separate project-application limits remain unchanged.

<a id="trace-lattice-existence-boundary"></a>
## One mechanism: rational trace averaging and the orbit lattice

The original [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) seeks an unrestricted total Mahler gap or a genuine zero-gap family.
The [S1 complete-orbit frontier](../strategies/Yin_S_G0001.md#complete-orbit-arithmetic-frontier-2026-10-18) and [S4 arithmetic route](../strategies/Yin_S_G0004.md) require automatic arithmetic coverage, not another favorable geometry-only test.
The investigated mechanism asked whether normalized traces or an integral-basis theorem automatically give a nonzero algebraic integer as a nontrivial rational convex combination of the actual conjugates.
Nontrivial means that at least two DISTINCT conjugates have positive coefficient.
A vertex is already an algebraic integer and supplies no new transformation.

Let alpha be an algebraic integer of degree d, let X={x_1,...,x_d} be its full rational conjugate set, and let L be its splitting field.
Write G=Gal(L/Q), tau=Tr_(Q(alpha)/Q)(alpha) in Z and

    P_Q={sum_i lambda_i x_i:
         lambda_i in Q, lambda_i>=0, sum_i lambda_i=1}.

Rational coefficients are essential: every Galois automorphism acts on the same coefficient tuple.
The planar convex hull in one displayed complex embedding permits unrelated real coefficients and is not a substitute for P_Q.

### Exact trace constraint and own-degree denominator

For every y in P_Q,

    Tr_(L/Q)(y)/[L:Q]=tau/d.                        (1)

Indeed transitivity makes the uniform Galois average of each x_i equal tau/d, and the coefficients sum to1.
If N=[Q(y):Q], trace transitivity gives the sharper own-field form

    Tr_(Q(y)/Q)(y)/N=tau/d.                         (2)

In particular,

    P_Q intersect Q={tau/d},
    P_Q intersect Z={tau/d} if d divides tau,
                      empty otherwise.             (3)

The inclusion of tau/d follows from the uniform convex combination, so these are equalities, not merely necessary conditions.
Thus the full Galois average supplies a NONZERO rational integer exactly when tau is a nonzero multiple of d.
When tau=0 it supplies only0, which is outside the requested nonzero output class.
Changing the positive rational weights cannot produce a different rational output.

For any algebraic-integer output y in P_Q, (2) implies

    d/gcd(d,tau) divides N,                         (4)

using gcd(d,0)=d.
This is necessary and not sufficient.
It does not assert that y is rational or totally real.
For example, if tau=1 or -1, every integral output has own degree divisible by d; neither an intermediate field nor a denominator-free lower-degree output is supplied by averaging.

### Exact Salem reduction and the retained half factor

Now assume alpha is a genuine Salem number of degree d=2t>=4.
The primary [DJ20-U001](../audits/literature/DJ20/Yin_U001.md#dj20-u001) checks Theorem1.1 and its entire elementary proof.
Its [direct specialization](../audits/literature/DJ20/Yin_U001.md#paired-rational-convex-hull) identifies the totally real part of P_Q exactly as

    (1/2) conv_Q{b_1,...,b_t},
    b_j=x_(2j-1)+x_(2j),                            (5)

where inverse pairs are labelled together.
If F is the field generated by all b_j, the integral-point obligation is exactly the intersection of (5) with O_F.
The actual trace field Q(alpha+alpha^-1) has degree t; F denotes its possibly larger normal closure.
No normality hypothesis on the actual trace field is inserted.

Although all b_j are integral, (5) retains a division by2 before any further rational weights are chosen.
An unnormalized trace, a positive sum of conjugates equal to1, or an integral relation with coefficient sum0 is not an integral convex mean with coefficient sum1.
Dividing a relation by its positive coefficient sum introduces precisely the denominator that must be proved harmless.
A negative coefficient cannot be changed to a positive coefficient merely by invoking an additive relation; the resulting exact identity and coefficient sum must both be checked.

Theorem1.1 gives a rigorous reduction but no supply of nonzero algebraic-integer points in (5).
It applies to totally real outputs only.
No conclusion about all nonreal integral outputs is inferred.

### Why a normal integral basis is not the missing supply theorem

The elementary lattice issue can be stated without invoking an external existence theorem.
Let

    V=span_Q(X), Lambda=sum_(x in X) Z x,
    Lambda_sat=O_L intersect V.

Suppose the x_i are Q-linearly independent and Lambda_sat=Lambda.
If y=sum_i lambda_i x_i belongs to O_L with lambda_i>=0 rational and sum lambda_i=1, then y belongs to Lambda.
Uniqueness of coefficients in the basis X makes every lambda_i an integer.
Nonnegativity and coefficient sum1 force exactly one coefficient to equal1 and all others to equal0.
Under these TWO explicit hypotheses the only integral points of P_Q are its vertices.
Consequently a nonvertex integral point, in the independent case, would require a genuine enlargement of the conjugate lattice inside O_L intersect V; merely producing a normal or integral basis does not provide that enlargement or a point in the simplex.
If additive relations occur, this uniqueness argument does not apply and no analogous conclusion is claimed.

A normal integral basis for L/Q, when available, concerns conjugates of a particular generator theta whose orbit is a Z-basis of O_L.
For that theta it has exactly the vertex-only property just proved.
It does not identify theta with the prescribed alpha or control the coordinate change from theta to the x_i.
For genuine Salem alpha, Q(alpha) is a subfield of R in its displayed embedding but has nonreal conjugates, hence is not normal over Q.
Therefore [L:Q]>d and the d distinct conjugates of alpha cannot even be a Q-basis of L, much less a normal integral basis of O_L.
This does not forbid them from being a basis of the smaller rational span V; saturation of that specific span would remain an additional arithmetic hypothesis.
No normal-integral-basis existence theorem or ramification criterion is imported here.

### Existing source and comparison boundaries

The local screen checked existing C/L/U accounts for convex conjugate sums, integral averages, normal integral bases and trace lattices.
[C16](Yin_C_G0016_v1.md#integer-moment-domain-and-energy) supplies rational representations of a specified rational matrix already in a finite convex hull of INTEGER rank-one atoms; it does not manufacture an integral point in P_Q.
C9--C13 concern actual relative-norm or quadratic unit profiles, with different values and normalization, rather than these linear conjugate means.
The accepted [C165 monomial theorem](Yin_C_G0165_v1.md#statement) and [Bil97-U002 finite-sum input](../audits/literature/Bil97/Yin_U002.md#bil97-u002) likewise do not assert the missing varying-weight integral-point existence.

A bounded primary-web search using convex-combination/conjugate/algebraic-integer and normal-integral-basis queries found no automatic existence theorem applicable to this exact P_Q.
The consequential primary input actually inspected is DJ20 Theorem1.1, as retained in its source unit.
This unsuccessful bounded search is not a proof that no such literature exists or a priority claim.

The trace-averaging mechanism supplies no new covered Salem class automatically.
Its rational-output subcase is fully decided by (3); its totally real subcase reduces to the exact half-trace lattice intersection (5); the normal-basis suggestion points in the opposite direction when it actually applies.
Outside the L399 exclusion, the trace constraints remain necessary and not sufficient, and the conditional vertex-only lattice argument still requires both independence and saturation.
Neither geometric convexity, an integral unnormalized trace, nor an unrelated basis theorem supplies a nonvertex integral mean.
This account provides no numerical scan, new gap class, original-target counterexample or Task completion.
