---
author: Yin
---

# C868 v2: independent whole-proof review for arbitrary reciprocal blocks

Review act: 2026-11-05T18:38, UTC.
The human record author is Yin.
This new review examines the entire fixed C868 v2 statement and argument and is independent of the development of that version.
The reviewer did not develop v1 or v2 and received no v2 development dialogue, mathematical summary, author explanation or proposed review verdict.
The fixed v1 proof and this reviewer's earlier [R1091 v1 finding](Yin_R_G1091_v1.md#whole-proof-finding) were already in the current context.
That prior finding is retained only at its actual v1 scope and supplies no automatic review of changed hypotheses or new reasoning.
The reviewer read the actual full v2 text, enumerated its obligations and formed initial findings, then inspected the selected predecessor calculations and source interfaces below.
No L development body, strategy or other agent's proof-development messages were read.
This is a new independent whole-proof finding for the substantive generalization, not a correction of the old finding or a retroactive enlargement of it.

## Inputs and inherited scope

- [C868 v2 statement](../../claims/Yin_C_G0868_v2.md#statement) and [complete argument](../../claims/Yin_C_G0868_v2.md#argument): all of GM1-GM2 and RG1-RG6, exact exceptional cases, both full-gap subdomains and the specialization limitations.
- [V1 first crossing](../../claims/Yin_C_G0868_v1.md#first-energy-crossing): the finite integer minimization and coefficient estimate, with the new germ identity independently checked in v2.
  V1's disk-holomorphic hypothesis is not imposed on the new meromorphic quotient.
- [V1 quadratic calculation](../../claims/Yin_C_G0868_v1.md#quadratic-cost-integrability): the normalized linear-factor L1 estimate and real reciprocal quadratic calculation.
  Their use is checked without inheriting the cyclotomic simplification m(A0)=0.
- [V1 boundary-root Poisson calculation](../../claims/Yin_C_G0868_v1.md#boundary-log-poisson): the radial L1 argument for roots exactly on T.
  V2's inside-root inequality and denominator reflection are new inputs checked directly here.
- [V1 short-polynomial calculations](../../claims/Yin_C_G0868_v1.md#short-polynomial-completion): only their integer coefficient, monic, reciprocal and even-degree scope is needed.
  Their estimates concern epsilon and are transferred to tau using tau>=epsilon, without requiring the new polynomial quotient to be cyclotomic.
- [Den09 U002](../literature/Den09/Yin_U002.md#den09-u002): the accepted full fixed-Laurent-polynomial Lawton statement for arXiv:0905.0604v1, Theorem14 and Example15, including torus zeros and the sup-norm relation parameter.
  The statement and current application are checked; Lawton's original proof is not newly audited.
- [C296 comparison](../../claims/Yin_C_G0296_v1.md#endpoint-row-hardy-closure): its displayed normalized finite Blaschke factors and coefficient-space mechanism were inspected as method attribution.
  Its endpoint relation-space theorem, closure proof and other conclusions are not premises for C868 v2 and are not reviewed here.
- [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract): the unrestricted total-Mahler gap, used for the explicit noncompletion comparison.

V1's BM05 attribution and its limits remain at [the source account](../../claims/Yin_C_G0868_v1.md#source-and-scope), with the actual [quadratic source mechanism](../literature/BM05/Yin_U001.md#source-quadratic-families) and [bounded source scope](../literature/BM05/Yin_U001.md#numerical-scope-and-prefix-boundary) already read in the present review context.
No fresh BM05 original inspection, numerical reproduction or priority search is claimed.
The new review evidence requires its own retained version because arbitrary block roots and pole cancellation are outside the previous candidate's hypotheses.

## Review relationships

| Review | Relationship |
| --- | --- |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V2 statement](../../claims/Yin_C_G0868_v2.md#statement) | Entire GM1-GM2 and RG1-RG6 statement, exact zero conditions, common-content qualifications, normalization and all quantifiers. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V2 complete argument](../../claims/Yin_C_G0868_v2.md#argument) | All six sections, including the new germ interface, numerator-root inequality, denominator reflection, exact multiplier cost, subdomain gaps and finite-specialization examples. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V1 first crossing](../../claims/Yin_C_G0868_v1.md#first-energy-crossing) | Finite coefficient truncation and integer minimization; application to a germ is separately checked in v2 and does not inherit v1's disk-holomorphic premise. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V1 quadratic calculation](../../claims/Yin_C_G0868_v1.md#quadratic-cost-integrability) | Reciprocal quadratic root calculation and normalized linear-factor L1 bounds, without using the cyclotomic zero-measure simplification for general A0. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V1 boundary-root calculation](../../claims/Yin_C_G0868_v1.md#boundary-log-poisson) | Radial L1 convergence and exact Poisson equality for unit-circle root factors only. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [V1 short-polynomial estimates](../../claims/Yin_C_G0868_v1.md#short-polynomial-completion) | Energy1-4 coefficient classification and lower bounds under monicity, reciprocity and even degree; no cyclotomic-root conclusion is transferred. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [Den09 Lawton input](../literature/Den09/Yin_U002.md#den09-u002) | Theorem14/Example15 statement and applicability to the fixed F and (1,N), including torus zeros; no new proof audit of Lawton or other results in U002. |
| [General-blocks whole-proof finding](#general-blocks-whole-proof-finding) | [Original Task contract](../../tasks/Yin_T_G0001_v1.md#contract) | Comparison with the unrestricted unnormalized objective only; no Task-completion review or claim of resolution. |

## Obligations and decisive checks

### The finite argument uses only a germ

The first obligation is to establish GM2 when f may have no analytic continuation across some interior pole.
All coefficient H2 estimates apply instead to the disk-holomorphic q and u of GM1.
Radial Parseval and monotone convergence give ||q||_H2<=1 and ||u||_H2<=2.
Because q(0)=exp(-tau) is real and positive, expansion of ||1-q||_H2^2 gives the bound 2(1-exp(-tau))<=2tau.

At the first prefix crossing energy5, c_0=1 makes N>=1.
Every earlier nonzero coefficient is a unit, because a coefficient of modulus at least2 together with c_0 would have crossed already.
Thus s belongs to {1,2,3,4}, c>=1, s+c^2>=5, and the prefix P has H2 norm sqrt(s+c^2) and coefficient absolute sum s+c.
The local identity u=fq is sufficient to prove S_N u=S_N(Pq) by the order of vanishing of f-P.
The ensuing estimate uses truncation only on u and P(1-q), both in H2, and multiplication only by the finite polynomial P.
No tail of the full germ is treated as an H2 function.

The same integer minimization remains exhaustive: c=1 forces s=4; c=2,s=1 improves the denominator from5 to3; c=2,s>=2 gives at least (sqrt(6)-2)/6>1/15; and c>=3 gives at least (c-2)/(c+4)>=1/7.
These bounds yield tau>=(sqrt(5)-2)^2/50.
If no prefix crosses, integrality and total energy at most4 force finitely many nonzero coefficients.
This proves the exact polynomial-germ conclusion and does not replace the germ by a chosen finite truncation.

### The full quadratic cost retains m(A0)

Reciprocity and real coefficients make A and B real on T, and the centered monomials give |B/A|=|B0/A0| wherever the quotient is defined.
The v1 reciprocal quadratic calculation applies fiberwise without a restriction on the roots of the polynomial blocks.
The normalized factor bound gives a fiberwise absolute logarithmic integral at most phi(t)+4log2.
The bound phi(t)<=log^+|B0|+log^-|A0| is integrable for arbitrary fixed polynomial blocks: roots off T cause no boundary singularity, and roots on T have integrable logarithmic singularities.
Together with integrability of log|A|, this establishes absolute integrability of log|F| before Fubini is used.
Exceptional fibers at common or repeated boundary roots form a finite null set.

The outer contribution is now m(A0), so the result is tau=m(A0)+epsilon.
Monicity gives m(A0)=sum log^+|alpha|>=0 and hence tau>=epsilon>=0.
The old cyclotomic simplification is not used in this enlarged domain.

### Numerator roots supply the correct Poisson inequality

The constant coefficients exclude zero roots and give the constant-normalized factorizations into 1-z/beta.
For |beta|<1, the boundary identity gives the harmonic extension -log|beta|+log|1-conj(beta)z|.
The identity
\[
 |1-\overline\beta z|^2-|z-\beta|^2
   =(1-|\beta|^2)(1-|z|^2)>0
\]
therefore gives the needed inequality for log|1-z/beta|, including its value minus infinity at beta.
For |beta|>1 the zero-free factor gives equality; for |beta|=1 the reread v1 radial L1 proof gives equality.
Adding the finite set of factors establishes log|B0|<=P[log|B0|] without assuming that B0 has no interior zeros.
All boundary logarithms being combined are integrable.

### Denominator poles are canceled at the exact cost

For every interior root alpha, the displayed factor I_alpha is a normalized finite Blaschke factor with its zero at alpha and value |alpha| at0.
The same squared-modulus identity proves its modulus at most1 in the disk and equal to1 on T.
The factor is holomorphic across the closed disk since 1-conj(alpha)z has its zero outside it.
Taking the product with multiplicity preserves all these properties.

Multiplication of the explicitly written factors gives A0=I_A A_out exactly.
The polynomial A_out has no interior zero, keeps all boundary roots and satisfies |A_out|=|A0| on T.
Thus f I_A extends to B0/A_out throughout the disk even when f itself has interior poles or canceled common factors.
Because A0 is monic with constant coefficient1, the product of the moduli of all its roots is1.
It follows that
\[
 I_A(0)=\prod_{|\alpha|<1}|\alpha|
       =\exp(-m(A0)),\qquad A_{\mathrm{out}}(0)=\exp(m(A0)).
\]
This includes constant A0 and arbitrary root multiplicities and introduces no additional symmetry assumption.

Every nonconstant factor of A_out is zero-free in the disk, and its boundary-root factors have the exact Poisson extension already checked.
Consequently log|A_out|=P[log|A0|].
Subtracting this equality from the numerator inequality proves the interior majorant for the holomorphic extension B0/A_out.
This subtraction is between finite harmonic quantities on the denominator side and the numerator's possibly minus-infinite logarithm; canceled poles create no undefined interior expression.

For g=phi(B/A), the coefficient recursion gives the integral germ f with f(0)=1, while g is nonnegative and integrable by RG1.
The boundary estimate log|f|<=log2+g and the positive Poisson kernel give the interior bound after reflection.
The analytic exponential exp(-H_g) has modulus at most1 and value exp(-epsilon) at0.
Therefore q=I_A exp(-H_g) and u=(B0/A_out)exp(-H_g) satisfy all of GM1, with q(0)=exp(-m(A0)-epsilon)=exp(-tau).
The proof establishes the interior bound directly; it does not invoke an unverified almost-everywhere boundary maximum principle.

### Structural completion and both full-gap subdomains

For tau<gamma, GM2 gives a polynomial germ f.
The near-zero identity A0 f=B0 is then a polynomial identity, yielding integer coefficients, monicity, constant coefficient1, even degree and reciprocity.
The reversal cancellation is valid after polynomiality.
The subsequent short-polynomial arguments use no claim about the locations of f's roots.

Energy1 and energy2 give exactly f=1 and f=1+x^(2h).
At energy3, symmetry leaves the central coefficient sigma in {1,-1}; the set sigma cos(h theta)>=sqrt(3)/2 has normalized measure1/6 and gives epsilon>=log2/6.
At energy4, X=|f|^2-4 has mean0, range [-4,12] and two extreme Fourier coefficients of modulus1.
Thus E X^2>=2, E X_+=E X_- and E X_+>=1/8.
The estimate phi(B/A)>=(1/2)log(1+X/4)>=X/32 on X>0 gives epsilon>=1/256.
Both bounds exceed gamma and hence also exclude tau<gamma because tau>=epsilon.
This is the required interface from the inherited coefficient calculations to the new total cost.

In the two remaining identities the degree relation gives B/A=1 or x^h+x^(-h), respectively.
Their costs epsilon vanish, so tau=m(A0) exactly.
Conversely, tau=0 is impossible outside these identities by RG2 and requires m(A0)=0 within them.
This proves RG2-RG3 and the general zero condition without assuming a one-variable Mahler gap.

For cyclotomic A0, m(A0)=0 gives RG4 for every allowed numerator.
For coprime inputs either exceptional identity forces A0=1, since A0 divides B0 and is monic.
The resulting B0 are exactly1 and1+x^(2h), and both give zero cost.
Every other coprime pair lies outside RG3, proving RG5 and its nonconstant-denominator conclusion.
No additional gcd-decomposition theorem is required.

### Specializations, varying inputs and surviving common content

For N>max(0,b-a), k=N+a-b>0 and k+2b=N+a+b<2(N+a).
The shifted B0 term cannot cancel either endpoint of P_N; the two A0 blocks have constant and top coefficients1.
Reflection about degree N+a exchanges those blocks and preserves the shifted B0 block.
This verifies the claimed actual degree and reciprocal integer structure without a cyclotomic hypothesis.

The exact monomial identity identifies m(P_N) with m(F(t,t^N)).
The nonzero integer relations on (1,N) are (-Nj,j), so their least sup norm is N.
The accepted Lawton theorem applies to this fixed nonzero Laurent polynomial F, including its torus zeros.
Taking logarithms of its multiplicative limit is legitimate because M(F)=exp(tau)>0.
This proves RG6 and gives gamma/2 eventually for each fixed nonexceptional pair, without a cutoff uniform in the pair.

For A0=1, B0=1-x^h+x^(2h), N=2h, the stated inequality N>b-a=h holds.
The energy3 calculation with sigma=-1 gives epsilon>=log2/6 independently of h.
Direct substitution gives
\[
 P_N=x^{4h}-x^{3h}+x^{2h}-x^h+1
     =\Phi_{10}(x^h)
     =\frac{x^{5h}+1}{x^h+1}.
\]
All its roots are roots of unity, so it is a cyclotomic product of measure0.
This verifies the obstruction even while N tends to infinity, without contradicting the limit for any fixed h.

Finally, A0=B0=P retains m_2(F)=m(P) for every monic reciprocal even-degree integer P with constant coefficient1.
For the first exceptional case the specialization is A0(t)(t^(2N)-t^N+1).
For the second it is A0(t)(t^(N-h)-1)(t^(N+h)-1), with N>h.
The factors outside A0 are cyclotomic in both cases, so all these finite specializations retain m(A0) exactly.
The candidate therefore leaves the one-variable reciprocal unit problem in its common content and does not solve the unrestricted G0001 contract.

## Source and review limits

The predecessor calculations are reused only at the precise scopes listed above; the general root comparisons, normalization and every changed implication were checked in this review.
The normalized Blaschke factors agree with the displayed method in C296, but no closure or endpoint result from that claim is needed.
The reciprocal quadratic calculation keeps its established BM05 attribution and is locally proved at the current scope.
Lawton is the only external theorem invoked without a local proof, and its exact retained statement and hypotheses match RG6.
No unresolved source-interface or mathematical dependency was found for the argument actually used.
No original source proof, numerical search, literature-priority assertion or unrestricted Task completion is certified here.
R1091 v1, C868 v1 and their actual adopted scope remain unchanged.

## General-blocks whole-proof finding

The full fixed C868 v2 statement and complete six-section argument are mathematically supported under their stated hypotheses, with no gap found.
This independently reviewed finding covers GM1-GM2, RG1-RG6, both exceptional identities, both full-gap subdomains and the exact common-content and specialization limitations.
No substantive repair was contributed by the reviewer.
There is no remaining mathematical review obligation identified within this candidate's stated scope.
Adoption of the finding remains a separate C decision; the unrestricted G0001 problem and any varying-pair positive-measure construction remain unresolved.
This review changes no C assessment, strategy, index, execution boundary or repository configuration.
