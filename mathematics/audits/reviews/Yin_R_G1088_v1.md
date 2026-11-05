---
author: Yin
---

# Independent whole review of primitive Salem monomial radical degree costs

Review act: 2026-11-04T22:20 UTC.
Human record author: Yin.
The reviewer is a separately assigned noncontributor to C866, outside its substantive proof development and without inherited proof-generation discussion or a mathematical development summary.
The supplied assignment identified the fixed candidate, directly needed inputs, whole A--E scope, review rules and actual execution limits.
The reviewer read the fixed candidate and its directly needed mathematical inputs, and formed the initial mathematical findings before consulting previous R conclusions.
D1, generation notes and contributor conversations were not read.
The subsequent readings of R391, the C383 finding in R588 and the C485 finding in R698 checked their actual recorded relationships and limits; they did not supply the initial verdict or receive a new whole review here.

The target is the unassessed 2026-11-05 author proof in [C866v1](../../claims/Yin_C_G0866_v1.md), including the entire Statement A--E, complete argument Sections 1--8, exact control, consequence and review limits.
No target mathematics was edited or repaired.
The relevant erratum file was empty at inspection.
This new whole inspection provides necessary independent evidence absent from the candidate; it does not select a C assessment, complete G0001 or change an ancestor's review relationship.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C866 statement](../../claims/Yin_C_G0866_v1.md#statement) | Entire A--E, S1--S8, all degrees, primitive and nonprimitive hypotheses, arbitrary external torsion and radicals, coordinate assertion, support cases, exact control and stated limitations. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C866 argument](../../claims/Yin_C_G0866_v1.md#argument) | Complete Sections 1--8 and consequences: actual exponent orbit, all support/parity counts, positive coordinate descent, full-field norm-one interface, ordinary external norm, exact full-degree measure scaling, nonprimitive conversion, odd-t torsion and the primitive quartic. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C165 monomial field argument](../../claims/Yin_C_G0165_v1.md#fixed-support-salem-monomial-proof) | Signed-exponent stabilizer and Q(eta^n)=Q(eta) for every n>=1, with actual own degree, arbitrary nonzero integer exponents and all genuine Salem degrees; no AM16 bound or later packet comparison. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C165 independence argument](../../claims/Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) | Complete torsion-valued independence proof, including the real inverse pair, negative exponents and alpha>1 without an alpha<2 restriction; classical attribution remains at its existing source scope. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C383 Salem kernel](../../claims/Yin_C_G0383_v1.md#salem-kernel-class-population) | Conjugate-complex-conjugation patterns, even-weight flips and full inversion kernel for even t; the direct reconstruction is checked, without full top group, split extension, prime or density claims. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [C485 full-field kernel](../../claims/Yin_C_G0485_v1.md#salem-relative-regulator-identity) | Only actual Salem trace-field signature, compatible inverse involution, exclusion of relative norm -1 and the full integer-unit norm-one kernel {+/-tau^j}; regulator and index comparisons are outside this review. |
| [Whole radical-degree finding](#whole-salem-radical-degree-finding) | [Smy15 canonical source unit](../literature/Smy15/Yin_U001.md#smy15-u001) | Accepted Lemma 2/Proposition 3 fixed-field generator, same degree and positive powers, at the retained selected statement/displayed-proof inspection; applicability to C485 and C866, without a new source-PDF or original-Salem proof audit. |

<a id="whole-salem-radical-degree-finding"></a>
## Whole finding

PASS for the entire fixed C866v1 Statement A--E and complete argument at the exact accepted-source boundaries above.
No substantive gap, missing hypothesis, incorrect field identification, uncharged degree loss or required correction was found.
The conclusions hold for every stipulated genuine Salem degree d=2t>=4, all allowed supports and signs, every reduced positive g/s and arbitrary roots of unity, including those outside L.
The proof does not require a bound for mu(L) in even trace degree.

### Integer monomials, actual degree and support endpoints

Sending one chosen inverse-pair representative to alpha sends every other representative to the unit circle, so a torsion-valued relation forces that one exponent to vanish.
Repeating this for every coordinate proves independence modulo torsion for the full chosen t-tuple.
It makes the monomial nontorsion, identifies N with its signed-exponent orbit and makes its stabilizer unchanged after every positive power.
The resulting power-field identity is exact, rather than a degree inequality or a prime-power-only result.
Negative coefficients preserve unit status because every Salem root and its inverse are integral.

At each Galois embedding at most one coordinate contributes a nonzero real logarithm, so there are no missing cross terms in the square average.
Uniform root transitivity gives the exact mean m^2 sum(b_i^2)/t; multiplying by the own degree in the definition of M_2 gives N m sqrt(sum(b_i^2)/t).
Each support contributes its own disjoint collection of exponent vectors.
Transitivity makes the support union cover all t pairs, requiring at least t/r supports.
For r<t an unused coordinate supplies any needed parity correction, giving all 2^r signs on each support.
For full support the even-weight group gives 2^(t-1) signs; at t=r=2 the full inversion kernel gives four.
The three cases prove every bound in S6, without multiplying overlapping orbits or assuming a symmetric top action.
The scalar inequalities 4^(r-1)>=r and 2^(t-1)>=2sqrt(t) for t>=3, together with the separate t=2 calculation, prove S5 including every endpoint.

### Internal coordinate descent and primitive-field cost

For each i the conjugate c_i of complex conjugation fixes u_i and flips every other pair.
Its sign pattern commutes with the entire point stabilizer H_i, even when H_i permutes and reverses other pairs.
Every c_i inverts every root of unity in L because any automorphism sends a root of unity to another root of unity.
Consequently delta_i^s=u_i^(2A_i) has no residual torsion factor.
For h in H_i, the quotient h(delta_i)/delta_i is torsion, while after g_i both numerator and denominator are positive squared complex moduli.
Thus that quotient is one, proving delta_i lies in the actual field Q(u_i).
This positivity argument avoids any assumption that mu(L) consists only of real roots of unity.

The descended v_i is an integer unit in K and has positive distinguished real value.
Its relative norm to the totally real trace field is torsion, hence +/-1; a nonsplit real place excludes -1 because t>=2.
The used portion of C485 identifies the complete full-ring norm-one group.
Its local proof is applicable: after sign and inversion a nontorsion norm-one unit has exactly one expanding K-embedding, so a proper own subfield would repeat that value and is impossible.
The accepted Smy15 fixed-field theorem then makes it a power of the smallest Salem generator.
For primitive alpha, positivity removes the sign, giving v_i=alpha^j and s j=2A_i, including A_i=0 and negative A_i.
This establishes the full assertion B without an actual-order substitution or an even-t torsion hypothesis.

### External torsion, ordinary norm and exact scaling

In S1 the equation places xi in E=L(beta), even when xi is not in L.
If w is its actual order, beta^(sw)=eta^(gw), and power stability proves Q(eta) is contained in Q(beta).
Thus N divides D, and extension of the minimal polynomial from Q(eta) to L gives q<=D/N with no unjustified compositum-degree equality.
The ordinary E/L norm of beta is a unit and its s-th power is eta^(gq) times the torsion norm of xi.
No Galois hypothesis on E/L or normalized relative norm is needed.
Applying the internal assertion to each coordinate, then Bezout for gcd(b_i)=1 and cancellation using gcd(g,s)=1, gives s|2q and D>=sN/gcd(s,2).
The q=1 consequence and odd-s no-loss statement follow exactly.
The same monic equations prove integrality of beta and its inverse; torsion beta would contradict nonzero b.

A common number field counts every embedding of each own field with constant extension multiplicity.
Averaging s log|beta|=g log|eta|, first after squaring and then after taking positive parts, gives both exact S3 scalings with factor gD/(sN).
This includes both embeddings of a nonreal pair and uses the actual degrees in both raw quantities.
The finite-place terms vanish because the elements are units.
The lower bound M_2(beta)>=M_2(alpha)/2 follows with the correct direction and no extra height normalization.
Common-denominator extraction and cancellation change only the allowed torsion representative, so the stated rational-exponent normalization is complete.

### Nonprimitive sources and odd trace degree

For alpha=alpha_0^A the accepted source theorem preserves the degree and field.
The reciprocal rational-polynomial expressions for the two generators preserve their splitting fields and identify the conjugate pairs by A-th powers.
Repeating the coordinate equation gives s j=2A A_i, so the external norm gives s|2Aq and the exact denominator gcd(s,2A).
Both measure identities remain unchanged and S7 retains the full original power cost; it supplies no uniform bound relative to arbitrary nonprimitive alpha.
For odd t the commuting c_i have identity product and each inverts torsion, forcing every root of unity in L to have square one.
This ancillary conclusion is independent of the degree proof, as claimed.

### The complete primitive quartic control

The discriminant v^2-4 has rational norm 21, excluding a square in Q(v); beta therefore has degree four and the stated reciprocal polynomial.
A nonreal trace excludes real and unit-circle roots of its quadratic, so precisely one root has modulus greater than one.
The expansions for A+Z=1 and AZ=-5 give A=(1+sqrt(21))/2 and Z=(1-sqrt(21))/2.
The discriminant A^2-4=A+1 is negative at the other trace-field embedding, proving nonsquareness, degree four, the exact Salem polynomial and the stated four roots.
A>5/2 proves alpha>2 without a numerical approximation.

The primitiveness argument uses the same trace field and inverse involution for any smaller Salem tau in K.
Its trace h is integral, so its rational trace a is an integer and squarefreeness of 21 forces the coefficient b in h=(a+b sqrt(21))/2 to be an integer.
The two archimedean intervals force 0<b sqrt(21)<5, hence b=1, then simultaneously a>=1 and a<1.
This is a contradiction, with no omitted intermediate Salem generator or numerical search.

The eta quadratic discriminant is v^2 times the already nonsquare discriminant, and its trace generates Q(v), proving N=4 and the stated P_eta.
Its trace conjugates have sum -5 and product 7, which yield the coefficient 9 of X^2.
Q(beta,conjugate(beta)) has degree at most eight and contains all four Salem roots.
The actual t=2 full inversion kernel and transitive two-pair image force [L:Q]=4*2=8, so that overfield equals L and beta lies in L.
Thus q=1 and D=N=4 attain D=sN/2 for the primitive b=(1,1), g=1, s=2 data.
The logarithmic lists for beta, eta and alpha give exactly M_2(beta)=2m, M_2(eta)=4m, M_2(alpha)=sqrt(8)m and the three stated total measures.
This attains the factor two relative to eta and the factor 1/sqrt(2) relative to alpha, not the final factor-one-half bound.

### Source, prior-review and consequence boundaries

The accepted Smy15 unit supplies the fixed-field theorem at its actual Lemma 2/Proposition 3 statement and displayed-proof inspection; its original Salem publications were not newly inspected.
The canonical unit and its source entrance were read here, without a new PDF acquisition, rendering or proof audit.
The C165 independence attribution was compared with the retained Dub23 source account and canonical U001: the joint statement is distinct from individual irrationality, and the original monograph remains uninspected.
The C383 attribution was compared with the CM10 source account: only the accepted-manuscript Section 2 kernel scope is used, not its split-extension theorem.
The local independence and sign-kernel arguments are complete and were rechecked directly here.
No AM16 theorem, regulator estimate, Frobenius density, favorable prime bound or universal raw-p2 theorem is consumed.

R391's current whole relationship is unknown; the selected C383/R588 and C485/R698 whole findings are self-reviewed.
Those facts and the older recorded source limits are preserved, not promoted to independent review by the present use.
This finding independently checks the exact interfaces used by C866 and C866's complete proof; it is not an independent whole re-review of C165, C383, C485 or their unrelated dependencies and comparisons.

The final unbounded-degree obstruction follows from M_2(beta)/log(alpha)>=sqrt(2d)/2 for primitive sources.
It excludes a fixed-C reduction of the stated rational radical construction class, including external torsion and extension fields.
It neither proves the original Lehmer gap nor adds a favorable p=1 coverage theorem.
The actual control is a fixed positive-measure example, not a near-zero family; quadratic saturation is not classified and final factor-one-half sharpness is not asserted.
No exhaustive literature or novelty conclusion is supplied by this review.
All checks were symbolic mathematical inspection; no numerical experiment, native program, polynomial enumeration or formal verification was used or required by this argument.
