---
author: Yin
---

# Whole independent review of the varying-conductor unit-resultant precision theorem

Human record author: Yin.
Review act: 2026-10-28T21:22.
Artifact: [C840 v1](../../claims/Yin_C_G0840_v1.md), with its [open decision](../../claims/Yin_C_G0840_v1.md#decision-varying-conductor-unit-resultant-open), entire [ST1--ST6 statement](../../claims/Yin_C_G0840_v1.md#statement), and complete [VC1--VC8 argument](../../claims/Yin_C_G0840_v1.md#complete-argument).

## Review arrangement and input boundary

This was an initial whole review by a separate subagent outside the substantive development of C840.
The assignment supplied the fixed artifact, its exact scope, necessary dependency locators and administrative limits.
No proof-generation conversation, mutable draft argument, author explanation or prior verdict about C840 was inherited or consulted before the finding.
The reviewer enumerated obligations from the fixed statement, checked VC1--VC8 and the directly consumed accepted interfaces, and formed the finding without supplying a mathematical repair.
The reference to D43 is extraction provenance only; D43 was not read and supplies no premise.

The review covers all original canonical evaluations, every allowed conductor and cofactor, all order and norm assertions, both coefficient ceilings, the general integer-order norm lemma, the explicit positive-measure examples and all stated scope limits.
It is a mathematical review of the fixed proof, not a computational or formal verification.
No native computation is a premise and no native reproduction was needed.
Acceptance remains a separate decision of the responsible Claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Entire C840 statement](../../claims/Yin_C_G0840_v1.md#statement) | All ST1--ST6, ell>=2, arbitrary u,v>=0 and monic U of nonnegative degree with both unit resultants; original remainders, nonvanishing, unbalanced and balanced ceilings, full norms, actual orders, general norm lemma, uniform-six profile, explicit examples, degrees and scope boundaries. |
| [Whole finding](#whole-finding) | [Entire C840 proof](../../claims/Yin_C_G0840_v1.md#complete-argument) | Complete VC1--VC8, including every direct dependency interface, all higher Newton coefficients and every conductor, empty-complement and noncyclotomic endpoint. |
| [Whole finding](#whole-finding) | [C266 selected unit input](../../claims/Yin_C_G0266_v1.md#decision-complete-retained-proof-adoption) | Reuse of the accepted exact-cyclotomic-crt-defect interface: integral Bezout units, exceptional prime-divided units in the actual cyclotomic order and mixed-order one-minus-root units; actual substitutions and scope checked, without a new whole C266 review. |
| [Whole finding](#whole-finding) | [C736 selected canonical input](../../claims/Yin_C_G0736_v1.md#decision-whole-reviewed-2026-10-25) | FT1--FT2 original monic integer divided remainders and exact factor-root evaluation, with arbitrary common/repeated factors and constant cofactors; no unrelated residual or example conclusion imported. |
| [Whole finding](#whole-finding) | [C839 selected predecessor](../../claims/Yin_C_G0839_v1.md#decision-whole-reviewed-2026-10-28) | Fixed-conductor actual-order/Lagrange mechanism and ell=6 family comparison, including its explicitly selected C837 UV1--UV4 elementary cofactor-unit interface; no Yu, height or finite-alphabet premise and no transfer of C839's independent review to C840. |

## Accepted inputs and source completeness

The selected [C266 cyclotomic argument](../../claims/Yin_C_G0266_v1.md#exact-cyclotomic-crt-defect) was read at its actual interface.
Its nonexceptional integer resultant Bezout identity supplies inverses inside the cyclotomic order, and its exceptional case proves Phi_(Mp^j)(zeta_M)/p is an order unit by an integral quotient and a unimodular multiplication matrix.
C266's selected retained complete proof has self-reviewed evidence.
That accepted-input boundary is preserved; the present independent review does not relabel all of C266 as independently reviewed.

The [C736 proof](../../claims/Yin_C_G0736_v1.md#complete-argument), through FT2, supplies integer prime divisions before evaluation.
The proof uses C_p=X^p modulo p, Frobenius and monic division, including repeated factors.
The exact root evaluation follows from the actual original quotient equation, not from an asserted equivalence of canonical systems.

The relevant C839 statement, NC1--NC4 mechanism and selected decision were read, together with [C837's elementary UV1--UV4 interface](../../claims/Yin_C_G0837_v1.md#complete-argument).
Only their stated elementary unit and fixed-family scope is reused.
No C837 logarithmic-form theorem, height bound, native image or unrelated source proof enters C840.

For the explicitly named classical formulas, source attribution is available at [Mas12's selected Newton-identity account](../literature/Mas12/readme.md#newton-identity-selected-attribution) and [Nat26's finite Lagrange interpolation account](../literature/Nat26/readme.md#finite-lagrange-interpolation-attribution-2026-10-12).
Mas12 records the primary Problem7(a), printed/PDF page2, with the coefficient convention c_j=(-1)^j e_j and general-variable power sums.
This matches C840's recurrence for all indices up to the field degree, independently of repeated embedding values.
Nat26 records DLMF3.3(i), equations3.3.1--3.3.2, for distinct real or complex interpolation nodes.
C840's relative polynomial is separable in characteristic zero, so its m distinct roots meet those hypotheses.
These existing source checks are reused for formula attribution; C840 gives the necessary local coefficient derivations itself.
No new original-source proof audit, earliest-source priority, maximal-order theorem or novelty claim is supplied by this review.
At this actual dependency and attribution scope no unresolved external proof input remains.

## Obligation checks

### Original divisor, full domain and actual units

For every allowed monic U, T is a nonconstant monic integer polynomial because it contains F_N.
The original divided remainders a and c exist in Z[X] by C736 even if U shares factors with another factor of T.
Evaluating the integer quotient identities at the root theta of the ORIGINAL T gives a(theta)=T(x_2)/2 and c(theta)=T(x_5)/5.
Evaluating the final remainder similarly gives F(theta)=2C^2-3A^5.
No division by2 or5 occurs in a residue ring, and no proper-factor canonical variables replace a or c.

For M=N/2 or N/5, F_M is monic irreducible and Z[X]/(F_M) is a free integer order.
The determinant of multiplication by U is Res(F_M,U)=+/-1, since interchange of resultant arguments preserves its absolute value.
The integral inverse matrix applied to1 produces an inverse in that actual order.
Thus U(x_2) and U(x_5) are genuine units, without an assumption on roots, constant coefficient, squarefreeness or irreducibility of U.

The exceptional ratios are exactly N/(N/2)=2 and N/(N/5)=5.
C266 therefore supplies F_N(x_2)/2 and F_N(x_5)/5 as order units after the root-of-unity trace conversion.
The other factors required to be units have ratios (N/2)/3=5*2^(ell-1), and the pair15 versus3*2^ell; the first is not a prime power and neither index in the second pair has an integral prime-power ratio with the other.
These facts remain valid for ell=2.
They give A=u_A F_15(x_2)^u and C=u_C F_3(x_5)^v with actual R_full units u_A,u_C.

### Pure dyadic support, nonvanishing and positive full norms

The displayed Phi_15 and Phi_3 identities leave only pi=1-zeta^30 and pi'=1-zeta^15 as nonunit factors.
Their orders are2^(ell-1) and2^ell.
Every other one-minus-root factor has the mixed order stated in VC3, including the smallest case ell=2, so C266 supplies its actual order inverse.

For primitive2^r-root xi and odd j, choose positive odd k with jk=1 modulo2^r.
The geometric sum (1-(xi^j)^k)/(1-xi^j) is the inverse of (1-xi^j)/(1-xi).
The product identity consequently gives (1-xi)^(2^(r-1))/2 as a unit, including r=1.
Hence A and C have no non-dyadic prime support and have normalized valuations u/d_ram and v/(2d_ram) at every dyadic place.

Above3, the term2C^2 has valuation0 while3A^5 has positive valuation.
Thus F(theta) has valuation0 at every such place and is nonzero.
This proves original polynomial nonvanishing in all exponent branches, without a dyadic cancellation assumption.

The degree calculations give [K:Q]=8d_ram, [Q(x_2):Q]=4d_ram and [Q(x_5):Q]=2d_ram.
All K embeddings send theta to a primitive N trace, so the same valuation calculation applies to every conjugate.
Summing valuations gives dyadic norm exponents8u and4v.
There is no other rational-prime support.
Because A and C belong to the indicated subfields with even relative degrees2 and4, their full norms are positive even when a subfield norm is negative.
This proves exactly Norm_K(A)=2^(8u), Norm_K(C)=2^(4v) and the stated rho norm, with all embedding multiplicities.

### Both coefficient branches and the actual denominator order

In the unbalanced case the two dyadic summands have distinct valuations, so the valuation of their difference is exactly min(5u/d_ram,1+v/d_ram).
Coefficientwise divisibility of F by2^n implies the same lower bound n for its value at the integral theta.
Taking the integer floor gives the stated ceiling in the correct implication direction.

Every element of Z[zeta] has form a(theta)+zeta b(theta) by the quadratic relation.
For an element fixed by conjugation, subtraction gives (zeta-zeta^(-1))b(theta)=0, and zeta is nonreal.
Thus R_full intersect K=R, including for inverse units.
Writing A as a unit times pi^u and 2 as a unit times pi^(d_ram) shows directly that 2^(ceil(5u/d_ram))/A^5 is a unit times a nonnegative power of pi.
It lies in R_full and is real, hence lies in R.
The proof does not replace order membership by local integrality.

### Relative trace gain

The primitive order of zeta^m is30 for m=2^(ell-1), so K_0 has degree4 and [K:K_0]=m.
The monic degree-m polynomial C_m(X)-t is therefore the relative minimal polynomial.
Its monic relation spans R over R_0 with the stated powers of theta, and the field degree proves linear independence.
This justifies the relative order basis and the absolute rank before taking traces.

The derivative identity gives f_t'(theta)=m h.
Its numerator and denominator involve mixed orders15 and N/2, so h is a real unit of R_full and therefore a unit of R.
Lagrange interpolation gives the coefficient of X^(m-1) as the sum of g(theta_i)/f_t'(theta_i), namely the relative trace.
For r in R, choose g(theta)=r h in the actual relative order.
The formula then puts Tr_(K/K_0)(r)/m in R_0.
Its absolute trace is integral, proving Tr_(K/Q)(R) subset2^(ell-1)Z for every ell>=2.
No maximal-order or codifferent formula is needed.

### General Newton norm lemma and the balanced contradiction

For any full-rank integer order S and z=r/b in S_(2), b odd, the characteristic polynomial of multiplication by r has integer coefficients.
Its roots count all field embeddings, so e_i(z) is2-integral with the correct multiplicities.
Since z^j stays in S_(2), every power trace has the hypothesized divisibility by2^s.

The logarithmic derivative of product_sigma(1+T sigma(z)) gives exactly i e_i(z)=sum_(j=1..i)(-1)^(j-1)e_(i-j)(z)Tr(z^j).
Every summand on the right is in2^s Z_(2), hence v_2(e_i(z))>=s-v_2(i).
For k>=1 and i>=1, ki-v_2(i)>=k follows from v_2(i)<=i-1.
Every nonconstant full-norm term consequently lies in2^(k+s)Z_(2).
This proves ST4 in every degree and for repeated conjugate values, including s=0 and k=1.
It supplies the higher terms that a fixed quadratic truncation would not control uniformly as ell grows.

When v=5u-d_ram>=0, the exact rho norm becomes3^(-2^(ell+1)).
Repeated difference-of-squares gives valuation ell+3 for its difference from1: the factors3-1 and3+1 contribute1 and2, and each of the ell remaining factors contributes1.
If the original F were divisible by2^(a_den+5), the actual order denominator produces rho-1=2^5 z with z in R_(2).
Applying ST4 with s=ell-1 gives valuation at least ell+4 for the norm difference, a contradiction.
Thus nu_2(F)<=a_den+4, with the ceiling and integer offset stated in ST1.

### Endpoints, uniform-six specialization and predecessor comparison

For ell=2 the real-field degrees are8,4,2, pi=2, and m=2.
All mixed-order units, denominator membership and the trace gain remain valid.
When u=v=0 and U=1 the case is unbalanced, and its upper bound0 together with integer coefficients and nonvanishing gives nu_2(F)=0.
The phrase cyclotomic for T=F_N is interpreted in its defined primitive-trace sense: the associated reciprocal polynomial is Phi_N, while T itself is the irreducible trace polynomial.

For ell>=4, u=v=d_ram/4 are nonnegative integers satisfying balance.
Then ceil(5u/d_ram)=2, giving nu_2(F)<=6 for every allowed U.
The degree is4u+v+8d_ram+deg U=37*2^(ell-4)+deg U.

At ell=6 the C839 family has u=v=4 and U=(X-2)^4 F_5^6 F_9^8 B_187^2 Q.
The selected C837/C839 elementary interface makes each remaining factor a unit at both primitive480 and192 traces, for every Q in its entire allowed monoid.
The values lie in their real subfields and are algebraic units, so their subfield norms, and hence the corresponding resultants, are+/-1.
Thus the predecessor is indeed an allowed specialization, with no Yu or height input.

### Explicit noncyclotomic examples, full measure and limits

For U_M=1+(X-M)F_(N/2)F_(N/5), the degree is6d_ram+1 and the leading coefficient is1.
Reduction modulo either trace polynomial is1.
Both trace degrees are even, so resultant interchange preserves the value1 in both ordered hypotheses.

At X=M-1>=3 all linear root factors of both primitive trace polynomials are strictly larger than1.
Therefore U_M(M-1)<0, whereas U_M(M)=1.
The intermediate value theorem gives a root x_* in(M-1,M), hence x_*>2.
The associated real root of z^2-x_*z+1 has z_*>1.
Since P_(U_M) is monic integer, the full logarithmic Mahler measure includes the strictly positive contribution log z_* and cannot be canceled by the remaining roots.

The reciprocal factorization is exact, with every original cyclotomic factor and multiplicity.
Its full measure is therefore exactly m(P_(U_M))>0.
The original trace degree is14d_ram+4u+v+1, and the balanced uniform-six specialization has degree61*2^(ell-4)+1.
Every reciprocal degree is twice its actual original trace degree.

If4u+v+deg U>0, T=F_N times a positive-degree complementary monic factor, so T is reducible even when factors overlap.
Every balanced input has u>=1, and each explicit U_M has positive degree.
Thus the reducibility claims are correct, while the empty-complement case is correctly excluded.
Nothing in the argument proves irreducible lifting, nearzero measure, a Salem property, optimality or attainment of6, a bound for a different residual alone, or necessity of these auxiliary equations for the unrestricted Lehmer problem.

## Whole finding

PASS for the entire fixed ST1--ST6 statement and complete VC1--VC8 argument at the exact accepted-input and source-attribution scopes above.
No mathematical gap, missing conductor endpoint, unpaid norm term, sign error or hidden original-degree replacement was found.
The review independently checks the new varying-conductor and Newton chain; prior accepted inputs retain their actual review relationships and are not recursively upgraded.
The statement supplies a uniform necessary coefficient-precision ceiling on its defined family and explicit reducible positive-measure examples.
It does not resolve the unrestricted Task, and this R finding itself neither adopts C840 nor changes any execution or Claim decision.
