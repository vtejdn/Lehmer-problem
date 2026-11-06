---
author: Yin
---

# Fixed-source Blaschke factor bounds and the mixed-delay proliferation boundary

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The construction contributor identified the fixed-Salem norm-ray argument, checked the mixed-delay common-factor identity and compared the primary specialization sources.
The coordinating contributor generalized the norm return to any fixed-degree nontorsion unit and supplied the primitive-content and complete Poisson-cost comparison.
The construction contributor checked and assembled the complete arguments below.
These are ordinary author-development contributions and checks, not an independent project review or a new Claim assessment.
The bottleneck-diagnosis contributor subsequently read the complete version and found no substantive defect in (B1)--(B17) or (D1)--(D4), including the full relative-norm multiplicities and primitive-content and Poisson costs.
That ordinary cross-check did not reproduce J140 or reread the four external specialization and change-of-variable sources, and does not expand their inspection scopes.

<a id="fixed-source-proliferation-revision"></a>
## Question, retained predecessor and conclusions

[V1](Yin_L_G0450_v1.md#scope-and-factor-proliferation-assessment) remains fixed with its complete radical-saturation proof, translated-torsion countertest and source-reading limits.
Its [positive-factor bridge](Yin_L_G0450_v1.md#positive-factor-counterexample-bridge) asks for bounded total logarithmic measure and unboundedly many positive-measure irreducible factors, counted with multiplicity.
This version tests two actual ways of varying the output beyond the literal fixed polynomial substitution f(x^n).
It neither divides total measure by degree nor assumes that the whole output is irreducible.

For a fixed nontorsion algebraic unit source, every finite-Blaschke pullback factor has a positive lower measure bound depending only on the source degree.
Thus bounded whole measure cannot support positive-factor proliferation in that class, even when the branching degree and the integer denominator vary.
A separate primitive-content and Poisson identity explains the exact whole-output cost for reciprocal sources with endpoint values in {1,-1}.
Neither statement is a degree-uniform Lehmer bound.

For the mixed-delay family A_N below, different parameters have coprime noncyclotomic parts.
The inspected specialization theorems do not supply a uniform bound for the number of its reciprocal noncyclotomic factors.
This is a source-applicability boundary and an unresolved factor-count question, not evidence that the count is unbounded.

The elementary measure and zero-measure conventions are those of the accepted [Kronecker normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
The finite-Blaschke identities are proved here directly.
The external LN23 statement is a comparison and attribution, not an unproved input to those identities.

<a id="blaschke-fibers-and-integral-output"></a>
## The actual pullback and all its fibers

Let alpha be a fixed nontorsion algebraic unit, let K=Q(alpha), and let P be its monic irreducible integer polynomial of degree d.
Let
\[
 g(z)=\sum_{j=0}^{k}g_jz^j\in\mathbb Z[z],
 \qquad k\ge1,\qquad a=g_0\ne0,\quad b=g_k\ne0,
\]
have all roots strictly outside the closed unit disk.
Primitivity of g is not needed for the factor bound.
Write
\[
 g^*(z)=z^kg(1/z),\qquad
 R(z)=\frac{g^*(z)}{g(z)},\qquad
 F_g(z)=g(z)^dP(R(z)).
 \tag{B1}
\]
Expansion of P shows that F_g belongs to Z[z].
The zeros of g^* lie strictly inside the disk, whereas those of g lie outside it, so these polynomials have no common root.
In particular, a zero beta of F_g is not a zero of g.

Since g has real coefficients, |g^*(z)|=|g(z)| on the unit circle.
Thus R is holomorphic on a neighborhood of the closed disk, has modulus one on its boundary and is a nonconstant finite Blaschke product.
The strict maximum principle and the identity
\[
 R(1/\overline z)=1/\overline{R(z)}
 \tag{B2}
\]
give, at every finite point where R is defined,
\[
 \begin{array}{c|c}
 |z|<1&|R(z)|<1\\
 |z|=1&|R(z)|=1\\
 |z|>1&|R(z)|>1 .
 \end{array}
 \tag{B3}
\]
At a pole the exterior statement is interpreted on the Riemann sphere; roots of F_g never occur there.
Consequently every finite preimage of a given nonzero value has the same inside, boundary or outside classification as that value.
This assertion controls every conjugate in a fiber, not merely one selected inverse branch.

The constant and leading coefficients of F_g are respectively
\[
 a^dP(b/a),\qquad b^dP(a/b).
 \tag{B4}
\]
Here |b/a|<1, because the product of the moduli of all roots of g is |a/b|>1.
A rational root of a monic integer-unit polynomial can only be 1 or -1.
Neither argument in (B4) is such a number, so both coefficients are nonzero and deg F_g=kd.
No monicity or unit assumption is imposed on the whole pullback.

<a id="fixed-degree-norm-return"></a>
## Every unit factor returns to the fixed source degree

Choose primitive irreducible factors with positive leading coefficient.
Let f be such a factor of F_g which is a monic unit polynomial, and let beta be one of its roots.
By choosing a conjugate beta if necessary, arrange R(beta)=alpha.
Indeed R has rational coefficients, its value is a root of the irreducible P, and embeddings of Q(R(beta)) extend to Q(beta).
Put L=Q(beta); then K is a subfield of L.
Let e=[L:K] and define the actual relative norm
\[
                         \gamma=N_{L/K}(\beta).
 \tag{B5}
\]
The unit property of beta makes gamma an algebraic integer unit in K.

For each complex embedding sigma of K, the e extensions tau from L satisfy
\[
 R(\tau\beta)=\sigma\alpha,\qquad
 \sigma\gamma=\prod_{\tau\mid\sigma}\tau\beta .
 \tag{B6}
\]
By (B3), all e terms in this product are outside the circle if |sigma alpha|>1, inside if |sigma alpha|<1, and on it if |sigma alpha|=1.
There can therefore be no cancellation between positive and negative logarithmic radii inside this relative norm.
Precisely,
\[
 \sum_{\tau\mid\sigma}\log^+|\tau\beta|
       =\log^+|\sigma\gamma|.
 \tag{B7}
\]
All complex embeddings are counted, including both embeddings of a complex-conjugate pair.

Because alpha is a nontorsion algebraic unit, the accepted Kronecker statement supplies at least one embedding with |sigma alpha|>1.
At that embedding (B6) has every factor of modulus greater than one, so |sigma gamma|>1.
Thus gamma is nontorsion.
Summing (B7) and retaining the possible proper subfield Q(gamma) gives
\[
 \begin{aligned}
 m(f)
 &=\sum_{\sigma:K\hookrightarrow\mathbb C}\log^+|\sigma\gamma|\\
 &=[K:\mathbb Q(\gamma)]\,m(\gamma)
 \ \ge m(\gamma)>0,\\
 [\mathbb Q(\gamma):\mathbb Q]&\le d .
 \end{aligned}
 \tag{B8}
\]
The multiplicity [K:Q(gamma)] is essential.
No equality of K with Q(gamma), normal-closure bound or preservation of a powered degree is assumed.

There is a positive constant delta_d for nontorsion algebraic units of degree at most d.
For completeness, if a monic polynomial of degree n<=d has m<=1, each coefficient satisfies
\[
       |c_{n-j}|\le {n\choose j}\exp(m)\le {n\choose j}\exp(1).
 \tag{B9}
\]
This follows by writing the coefficient as a sum of elementary root products and bounding each product by the full Mahler product.
Only finitely many integer coefficient lists satisfy these bounds.
Among the minimal polynomials of nontorsion units in this finite set, all measures are strictly positive by Kronecker.
Define delta_d to be the minimum of 1 and their positive measures, or 1 if that set is empty.
Every nontorsion unit of degree at most d has measure at least delta_d, including those with measure greater than 1.
Equation (B8) therefore proves
\[
                            m(f)\ge\delta_d.
 \tag{B10}
\]

For any other primitive irreducible factor f of F_g, the nonzero leading and constant coefficients cannot both have absolute value one.
Either the leading coefficient or the constant coefficient has absolute value at least two.
The leading-coefficient bound for Mahler measure, applied also to the reciprocal polynomial, gives
\[
                            m(f)\ge\log2.
 \tag{B11}
\]
In particular all irreducible factors in this pullback are positive: a hypothetical cyclotomic factor would be a monic unit factor and would contradict (B8).

Let H_g be the primitive part of F_g, and count its irreducible factors with their multiplicities.
Writing
\[
                         c_d=\min(\delta_d,\log2)>0
\]
gives the complete factor bound
\[
             r_+(H_g)c_d\le m(H_g).
 \tag{B12}
\]
Hence m(H_g)<=B implies r_+(H_g)<=B/c_d, uniformly in g and k.
The conclusion remains valid if only the larger raw measure m(F_g) is known to be bounded.
It allows reducible outputs and removes no positive factor or multiplicity.

The constant depends on d.
Allowing the source degree to grow leaves delta_d uncontrolled and does not give an unrestricted Lehmer conclusion.
The new mechanism is the common radial classification of an entire relative-norm fiber, followed by return to a bounded source degree.
It is not a claim that arbitrary relative norms preserve total Mahler measure.

For a fixed Salem source, one may sharpen (B10) by reusing the [unit-ray lattice of v1](Yin_L_G0450_v1.md#unit-ray-saturation).
The logarithmic vector of gamma vanishes at all circle embeddings and has opposite entries at the two real source embeddings, so it lies on the positive ray generated by the logarithmic vector of alpha.
If s is v1's saturation index on that ray, lattice membership and (B8) give m(f)>=m(P)/s.
The general argument (B8)--(B12) does not require that Salem restriction or the fixed-field Salem-generator theorem.

<a id="primitive-blaschke-content"></a>
## Complete primitive content for endpoint-unit reciprocal sources

This section uses a different, explicitly stated source domain.
Let P be monic reciprocal in Z[z], of degree d>=1, with
\[
                        P(1),P(-1)\in\{1,-1\}.
 \tag{B13}
\]
It need not be irreducible.
Retain g from (B1), now primitive, and let F_g be the same homogeneous pullback.
Then F_g is primitive.

To prove this, suppose a prime p divides every coefficient of F_g.
A bar denotes reduction modulo p.
Primitivity of g makes both bar g and bar g^* nonzero, even when their actual degrees drop.
In the rational function field F_p(z) one has
\[
                     \overline P(\overline g^*/\overline g)=0.
 \tag{B14}
\]
The polynomial bar P remains monic and nonconstant.
A rational function algebraic over the constant field F_p must itself be constant: if a nonconstant rational function u were algebraic over F_p, then z would be algebraic over the algebraic extension F_p(u) of F_p, contradicting its transcendence.
Thus bar g^*/bar g=c for a nonzero c in F_p.

Use reversal with the fixed original length k:
\[
                    \operatorname{rev}_k(h)=z^kh(1/z).
\]
It is an involution on all coefficient lists of length k+1, including those whose first or last coefficient vanishes.
Applying it to bar g^*=c bar g gives bar g=c bar g^*=c^2 bar g.
Therefore c^2=1, so c is 1 or -1, with these values coinciding in characteristic two.
Equation (B14) contradicts (B13).
This treats all primes, including primes dividing both endpoint coefficients a and b; no coprimality assumption on those two coefficients was used.

<a id="complete-blaschke-poisson-cost"></a>
## Exact Poisson cost and comparison with the primitive linear output

For every g in (B1), set r=b/a, so |r|<1 and R(0)=r.
If phi is a continuous function on the circle and u is its harmonic extension to the disk, then u composed with R is harmonic.
The mean-value property gives
\[
 \int_{\mathbb T}\phi(R(\zeta))\,d\mu(\zeta)
  =u(r)
  =\int_{\mathbb T}
       \frac{1-r^2}{|\zeta-r|^2}\phi(\zeta)\,d\mu(\zeta).
 \tag{B15}
\]
Here mu is normalized Haar measure.
Equality for continuous functions identifies the pushforward measure and extends to all integrable Borel functions.
For fixed |r|<1 its Poisson density is bounded above and below by positive constants.
The boundary function log|P| is integrable, including its finitely many finite-order logarithmic singularities.
Thus (B15) applies to it without deleting a circle-root contribution.

Since all roots of g are outside the disk, m(g)=log|a|.
The full polynomial, including its integer content when present, consequently satisfies
\[
 m(F_g)
   =d\log|a|+
     \int_{\mathbb T}\frac{1-r^2}{|\zeta-r|^2}
                         \log|P(\zeta)|\,d\mu(\zeta).
 \tag{B16}
\]
This proof needs neither irreducibility nor absence of circle roots in P.

Under (B13), put h=gcd(|a|,|b|) and
\[
                         \ell(z)=a/h+(b/h)z.
\]
The polynomial ell is primitive and its root lies outside the disk.
Its reciprocal quotient has the same center r=b/a.
Its pullback F_ell is primitive by the preceding section.
Comparing (B16) for g and ell yields
\[
                         m(F_g)=d\log h+m(F_\ell).
 \tag{B17}
\]
Thus higher branching cannot reduce the complete measure below that of this actual primitive linear output.
This is not a claim that the linear output has measure at least m(P).
It also does not alone bound the number of factors; (B12) supplies that separate conclusion when the source is a fixed-degree nontorsion unit.

For comparison, a zero-centered quotient uses z^s g(1/z)/g(z) with s>k.
The same argument gives pushforward Haar measure and raw cost m(P)+d log|a|.
For monic P the cleared numerator has leading coefficient a^d, so its positive integer content is at most |a|^d.
Its primitive part therefore has measure at least m(P).
This elementary comparison agrees with LN23's zero-centered identity and is distinct from (B16), whose center need not vanish.

The already retained [C166](../claims/Yin_C_G0166_v1.md#salem-mobius-statement) concerns integral positive symmetric Mobius contractions of genuine Salem sources.
It retains its same-field primitive-power restriction and uniform lower bound for the source absolute height, not a uniform bound for all outputs from arbitrary large-height sources.
Its accepted Smy15 fixed-field statement and its original source-review limits are unchanged.
No C166 conclusion is silently extended to arbitrary non-Salem sources here.
Equations (B8)--(B12) instead give their own norm proof with a degree-dependent constant.

<a id="mixed-delay-positive-factor-question"></a>
## A mixed-delay family not settled by the fixed-source bound

Let
\[
 P_L(z)=z^{10}+z^9-z^7-z^6-z^5-z^4-z^3+z+1
\]
be the original Lehmer polynomial and define, for N>=1,
\[
             A_N(z)=P_L(z)(z^{2N}+1)+z^{N+5}.
 \tag{D1}
\]
These are monic reciprocal integer-unit polynomials of degree 2N+10.
Since P_L(1)=-1, one has A_N(1)=-1.
Their monicity and the intermediate value theorem supply a real root greater than one, so m(A_N)>0.
The coefficient sum bound, retaining any overlaps or cancellations at small N, is
\[
           \|A_N\|_1\le 2\|P_L\|_1+1=19,\qquad
                         0<m(A_N)\le\log19 .
 \tag{D2}
\]
The upper measure bound follows directly by integrating log|A_N|<=log||A_N||_1 on the circle.
Consequently unbounded r_+(A_N), with actual factor multiplicities retained, would suffice for the [v1 minimum-factor bridge](Yin_L_G0450_v1.md#positive-factor-counterexample-bridge).
The fixed-support gap for the entire A_N does not assign that gap to its potentially dense irreducible factors.

There is an exact separation across parameters.
Suppose N and M are distinct positive integers and a noncyclotomic irreducible f divides both A_N and A_M.
A root alpha of f is nonzero.
Also P_L(alpha) is nonzero, because otherwise (D1) would give A_N(alpha)=alpha^(N+5) nonzero.
Dividing the two vanishing equations by their respective alpha powers gives
\[
 \alpha^N+\alpha^{-N}
     =-\frac{\alpha^5}{P_L(\alpha)}
     =\alpha^M+\alpha^{-M}.
 \tag{D3}
\]
With u=alpha^N and v=alpha^M, the difference of the two sides factors as
\[
                 (u-v)(uv-1)=0.
\]
Thus alpha^(N-M)=1 or alpha^(N+M)=1.
Either conclusion makes alpha a root of unity, contradicting the choice of f.
Hence
\[
 \gcd(A_N,A_M)\text{ has only cyclotomic irreducible factors}
                       \qquad(N\ne M).
 \tag{D4}
\]
This includes possible multiplicities in the gcd.

Equation (D4) proves that positive factors genuinely change with N.
It gives no growth of the number of positive factors inside a single A_N.
The fixed f(x^n) saturation obstruction of v1 cannot simply be substituted for an argument about (D1).
Nor is (D1) represented here as a finite-Blaschke pullback of a fixed algebraic-unit source, so (B12) is not applied to it.
The subsequently completed [J140 finite test](../computations/programs/Yin_J_G0140/readme.md) retains the exact full factorizations for N=1,2,3,4,5,6,10,12,15,20,24,30.
There are two positive factors at N=1 and one at each other tested parameter; N=1 and N=5 also have the zero-measure factor Phi_6.
These finite results show no positive-factor proliferation in the tested range and establish no all-N bound.
The native program, complete table and explicitly uncertified floating measure diagnostics remain with J140 rather than being duplicated here.

<a id="delayed-factorization-source-boundary"></a>
## Primary specialization sources and their exact applicability

The 2026-11-06 bounded search asked whether fixed reciprocal quadratic Laurent templates specialized along (z,z^N) have a known uniform noncyclotomic factor count.
Local comparison reused v1, its fixed-source radical obstruction, the accepted sparse-gap scope and existing Lawton interfaces.
Primary searches used Schinzel specialization, reciprocal noncyclotomic factors, large-gap polynomials and toric Bertini.
They located the sources below; only the stated passages were inspected.
The search stopped after their actual statements exposed the missing reciprocal-factor coverage.
No exhaustive literature-absence claim, whole-proof review or generic-to-every-parameter inference is made.

**SSS18.**
William Sawin, Mark Shusterman and Michael Stoll, Irreducibility of polynomials with a large gap.
The inspected [author PDF](https://www.mathe2.uni-bayreuth.de/stoll/papers/SaShSt.pdf) has title-page date 28 March 2018 and 25 PDF pages.
The [arXiv metadata](https://arxiv.org/abs/1803.10811) identifies arXiv:1803.10811; equality of this author file with a particular arXiv version was not checked.
The coordinating contributor subsequently acquired the [arXiv v1 original](../literature/pdf/SSS18--arxiv-v1.pdf) and read Theorem 1.2 and its adjacent reciprocal-factor discussion at PDF pages 2--3, confirming the same relevant scope without asserting whole-edition equivalence.
The actual acquisition and edition distinction are maintained in the [SSS18 source notes](../audits/literature/SSS18/readme.md).
Printed pp.1--3 were read for the reciprocal/nonreciprocal definitions, Theorem 1.2 and the adjoining reciprocal-factor discussion.
Theorem 1.2 concerns fixed c,d with nonzero constants, gcd of the reversed c with d equal to one, c!=+/-d and the stated non-Capellian condition.
Its conclusion is eventual irreducibility of the non-reciprocal part of x^N c(x^-1)+d(x).
The reciprocal three-block family (D1) does not acquire a noncyclotomic factor-count bound from this statement.

**Fil22.**
Michael Filaseta, On the Factorization of lacunary polynomials, [arXiv:2207.11648v1](https://arxiv.org/pdf/2207.11648v1), 24 July 2022, 34 PDF pages.
Printed pp.1--4 were read, including the full statement of Theorem 1.1 and the definition removing all irreducible reciprocal factors with their multiplicities.
The shape f_0(x)+f_1(x)x^N+f_2(x)x^(2N) includes (D1), with f_0=f_2=P_L and f_1=x^5.
However, Theorem 1.1 additionally requires irreducibility of specified twisted bivariate polynomials for the permitted representations of N.
Those additional hypotheses have not been verified for (D1).
Even if verified, its conclusion only makes the non-reciprocal part 1 or irreducible.
Because A_N is reciprocal, a nonconstant non-reciprocal irreducible factor would occur together with its distinct reciprocal factor.
Thus that conclusion would force the non-reciprocal part to be 1, leaving all irreducible factors reciprocal.
It would not bound the number of reciprocal noncyclotomic factors or imply irreducibility of the entire noncyclotomic part.

**AS18.**
Francesco Amoroso and Martín Sombra, Factorization of bivariate sparse polynomials, [arXiv:1710.11479v3](https://arxiv.org/pdf/1710.11479v3), 18 December 2018.
The accessed PDF has 17 pages; the abstract-page comment says 16, and no pagination equivalence is presumed.
Printed pp.1--2 were read for Theorem 1.1, Conjecture 1.2 and Theorem 1.3.
The proved factorization theorem retains an additional free variable and gives factorizations over C(t)[z^+/-1].
Its toric Bertini comparison likewise retains a free variable and additional irreducibility hypotheses.
It is not a theorem about all variables specialized to one variable over Q.
The corresponding rational one-variable specialization statement is presented there as Conjecture 1.2.
The source therefore provides no direct uniform positive-factor count for (D1).
This identifies the logical boundary in the inspected edition, not the current status of every possible later result or this particular family.

<a id="blaschke-source-comparison"></a>
**LN23.**
Matilde Lalín and Siva Sankar Nair, An invariant property of Mahler measure, [arXiv:2211.00125v1](https://arxiv.org/pdf/2211.00125v1), 31 October 2022, 12 PDF pages.
Printed pp.2--4 were read for Theorem 1, Lemma 2, Corollary 3, Proposition 4 and their adjacent explanation.
The condition k>deg g in that theorem forces the displayed reciprocal quotient to vanish at zero.
Its invariant rational-function measure does not authorize dropping the cleared denominator's complete measure or treating a nonzero center as Haar-preserving.
The elementary proof (B15)--(B17) supplies that nonzero-center cost here.
The official abstract lists Bulletin of the London Mathematical Society 55 (2023), no.3, 1129--1142, DOI 10.1112/blms.12778; journal/preprint equivalence was not checked.

Retained originals and edition facts are in the responsible [LN23](../audits/literature/LN23/readme.md), [AS18](../audits/literature/AS18/readme.md), [SSS18](../audits/literature/SSS18/readme.md) and [Fil22](../audits/literature/Fil22/readme.md) source notes.
Those source keys identify the actual works without asserting new U acceptance.
No recursive audit of Schinzel, toric Bertini or the sources' other foundations was performed.
The conclusions concerning applicability depend on the displayed statements and their scopes, not on acceptance of uninspected source proofs.

<a id="fixed-source-and-delay-outcome"></a>
## Outcome and reopening boundary

Finite-Blaschke branching over a fixed-degree nontorsion algebraic unit cannot supply bounded total measure with unbounded positive-factor count.
The complete relative norm, its bounded-degree endpoint and the nonunit leading/constant cost prove this without a uniform-degree Lehmer premise.
For reciprocal endpoint-unit sources, primitive content and the exact linear comparison additionally prevent an uncharged whole-measure improvement from higher branching.

The mixed-delay family (D1) remains a different unresolved factor-count question.
Its positive factors are pairwise new across distinct parameters, but within-parameter proliferation has not been established or excluded by the inspected theorems.
J140 has completed the first bounded factor-count test and retains all its positive factors and floating-measure limits.
Cyclotomic count, growing degrees, generic irreducibility and the existence of fresh factors across N do not answer that question.
