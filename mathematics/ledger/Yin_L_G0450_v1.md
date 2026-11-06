---
author: Yin
---
# Positive-factor proliferation: fixed radical saturation and the cost of translated torsion

<a id="scope-and-factor-proliferation-assessment"></a>
## Question, outcome and checking scope

This bounded 2026-11-05 exploration concerns the unrestricted [G0001 Mahler-gap contract](../tasks/Yin_T_G0001_v1.md#contract).
The attempted mechanism is to construct integer polynomials with bounded total logarithmic Mahler measure and unboundedly many positive-measure irreducible factors.
The factor_proliferation agent developed and checked the calculations for human author Yin.
These are ordinary author checks within an exploration, with no independent project review, Claim assessment or resolution of the Task.

The sufficient counterexample implication is elementary, but does not itself supply a construction or a new strategy.
Fixed monomial substitutions cannot produce the required growth.
For the integer-unit core, the obstruction has the exact logarithmic-lattice and relative-norm proof below, using the accepted Con26-U002 interface.
A translated torsion resultant does produce arbitrarily many distinct positive-measure irreducible unit factors, but each factor pays a fixed positive total-measure cost.
No independent construction satisfying the bounded-total-measure requirement was found in this inspected scope.

<a id="positive-factor-counterexample-bridge"></a>
## The sufficient bridge and its actual counting convention

For a nonzero primitive Q in Z[x], let r_+(Q) be the number of primitive nonconstant irreducible factors having positive logarithmic Mahler measure, counted with multiplicity.
The factor x, cyclotomic factors and the sign contribute zero.
Integer content is not counted as a nonconstant factor; primitivity removes its separate measure contribution here.
Mahler multiplicativity and the nonnegativity of every integer-polynomial logarithmic measure give

\[
 m(Q)=\sum_{i=1}^{r_+(Q)}m(q_i),\qquad m(q_i)>0.
 \tag{1}
\]

The measure-one characterization, including zero roots, is reused at [Smy08-U001's normalization scope](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
If actual polynomials Q_j satisfy m(Q_j)<=B for a fixed finite B and r_+(Q_j) tends to infinity, choose a positive factor q_j of smallest measure.
Then

\[
 0<m(q_j)\le \frac{B}{r_+(Q_j)}\longrightarrow0.
 \tag{2}
\]

This would meet the original refutation criterion, without dividing any polynomial's measure by its degree.
The minimum in (2) is over the actual factors, not over conjugate roots or a degree-normalized height.
Repeated copies are allowed in this sufficient condition; the translated construction below instead has distinct factors.
The condition is an existence bridge requiring an independent algebraic mechanism, not evidence that such polynomials exist.

<a id="unit-ray-saturation"></a>
## Fixed integer-unit seeds: the exact saturation obstruction

Let f in Z[x] be monic irreducible, with f(0)=+1 or -1, and let its root alpha be nontorsion.
Put K=Q(alpha), d=[K:Q]=deg f, and use the full integer ring O_K.
For signature (r_1,r_2), choose every real embedding and one embedding from each complex pair, and write

\[
 L(u)=\bigl(\log|\sigma_1u|,\ldots,\log|\sigma_{r_1}u|,
 2\log|\tau_1u|,\ldots,2\log|\tau_{r_2}u|\bigr).
 \tag{3}
\]

The accepted [Con26-U002 general-signature statement](../audits/literature/Con26/Yin_U002.md#con26-u002) gives a discrete full lattice Lambda=L(O_K^times) in the sum-zero hyperplane and identifies the kernel as the finite root-of-unity group.
This reuses its actual-order, complex-weight and foundational-proof limits; no regulator estimate or effective unit algorithm is assumed.
Since alpha is nontorsion, L(alpha) is nonzero.
The intersection of Lambda with its real line is a nonzero discrete cyclic group.
Choose its generator v in the direction of L(alpha), so that

\[
 \mathbb R L(\alpha)\cap\Lambda=\mathbb Z v,
 \qquad L(\alpha)=s v,
 \qquad s\in\mathbb Z_{>0}.
 \tag{4}
\]

Thus s is the saturation index of this particular unit ray in this particular number field.
It is not a constant asserted to be uniform in f or K.
Choose an actual u in O_K^times with L(u)=v.
The kernel statement gives alpha=xi u^s for a root of unity xi in K.
The word primitive, when applied to u here, refers only to generation of this lattice intersection.

Fix n>=1 and an irreducible factor g of f(x^n).
Choose a root beta of g with beta^n=alpha; this is possible by conjugating any root of g so that its nth power becomes the chosen conjugate alpha of f.
Let H=Q(beta), e=[H:K], and gamma=N_(H/K)(beta).
The inclusion K subset H holds because alpha=beta^n.
Both beta and its inverse are algebraic integers, by their monic nth-power equations over the algebraic units alpha and alpha^(-1), so beta and gamma are units.
Every K-embedding of H sends beta to an nth root of alpha, whence

\[
 \gamma^n=\alpha^e,
 \qquad L(\gamma)=\frac enL(\alpha)=\frac{es}{n}v,
 \qquad \frac{es}{n}\in\mathbb Z_{>0}.
 \tag{5}
\]

The last membership is in the actual lattice Lambda; neither an ambient normal-closure degree nor a root count replaces e.
In particular e/n>=1/s.
Every embedding of K into C has exactly e extensions to H, and under each extension the modulus of beta is the nth root of the modulus of the image of alpha.
Counting all complex embeddings, including both members of each complex pair, therefore gives

\[
 \deg g=de,
 \qquad m(g)=m(\beta)=\frac enm(f)\ge\frac{m(f)}s.
 \tag{6}
\]

All quantities in (6) are total logarithmic Mahler measures of the actual monic minimal polynomials.
The same embedding calculation retains the possible degree loss of the norm endpoint.
If t=[Q(gamma):Q], then t divides d and

\[
 m(\gamma)=\frac td\frac enm(f),
 \qquad m(g)=\frac dtm(\gamma).
 \tag{7}
\]

Indeed, the positive-coordinate sum of L(gamma), formed in K, is d/t times gamma's own-degree measure.
This verifies the multiplicity factor rather than silently assuming Q(gamma)=K.
It is compatible with the [C231 all-positive-power norm descent](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent).

Since f is separable and f(0) is nonzero, f(x^n) is squarefree in characteristic zero.
None of its roots is torsion, since a torsion beta would make beta^n=alpha torsion.
Writing its distinct irreducible factors as g_1,...,g_r and their relative degrees as e_1,...,e_r, degree addition gives sum_i e_i=n.
Equation (5) now proves the uniform-in-n bound

\[
 r=r_+(f(x^n))\le s,
 \qquad m(f(x^n))=m(f).
 \tag{8}
\]

For a fixed product of integer-unit seeds with fixed multiplicities a_i, this argument bounds the positive factor count by sum_i a_i s_i.
A fixed zero-root or cyclotomic part contributes no positive factor after any monomial substitution.
The internal proof here concerns monic unit seeds; the general fixed-polynomial comparison is stated separately below.

<a id="varying-seed-primitive-unit-cost"></a>
## Varying the seed does not supply an independent root-extraction gain

Retain the actual u from (4), and put d_u=[Q(u):Q]<=d.
Positive-coordinate sums in K give the exact identity

\[
 m(u)=\frac{d_u}{d s}m(f)\le\frac{m(f)}s,
 \qquad m(u)>0.
 \tag{9}
\]

Positivity follows from L(u) being nonzero and its coordinate sum being zero.
The factor d_u/d is necessary because u need not generate K.
Thus, if varying irreducible unit seeds f_j have bounded m(f_j) while r_+(f_j(x^(n_j))) tends to infinity, (8) forces s_j to infinity and (9) already supplies small positive measures in their original fields K_j.
This is a diagnostic of the proposed mechanism: the primitive unit in the seed field contains the required small measure before the radical substitution is applied.
It neither constructs such primitive units nor proves a uniform bound on s_j over varying fields.

<a id="translated-torsion-unit-countertest"></a>
## A genuine factor-growth construction and its unavoidable cost

Let p_1,...,p_j be distinct odd primes, j>=2, and set N=product_i p_i.
Use the standard cyclotomic product identity to define

\[
 U_j(x)=\frac{(x+1)^N-1}{x\prod_{p\mid N}\Phi_p(x+1)}
       =\prod_{\substack{d\mid N\\d\text{ composite}}}\Phi_d(x+1).
 \tag{10}
\]

The equality follows because N is squarefree, its only noncomposite divisors are 1 and its prime divisors, and Phi_1(x+1)=x.
Thus U_j is an actual monic integer polynomial.
Evaluating after cancellation at x=0 gives

\[
 U_j(0)=\frac{N}{\prod_{p\mid N}p}=1,
 \qquad\deg U_j=N-1-\sum_{p\mid N}(p-1).
 \tag{11}
\]

Here the numerator quotient by x has value N, and Phi_p(1)=p.
Every individual Phi_d(x+1) in (10) has a positive integer constant coefficient Phi_d(1).
Positivity follows by pairing the nonreal conjugate primitive dth roots in product_(gcd(a,d)=1)(1-zeta_d^a), since these odd d exceed one.
Their product is one by (11), so each constant coefficient is one and each factor is a unit polynomial.
This avoids assuming a separate general formula for Phi_d(1).

The substitution x->x+1 is an automorphism of Q[x], so it preserves cyclotomic irreducibility and preserves distinctness of these factors.
The classical monic integral irreducibility of Phi_d is reused from [Bel17-U002](../audits/literature/Bel17/Yin_U002.md#bel17-u002) at its recorded accepted-statement scope; no integer-ring or discriminant assertion from that unit is needed.
There are exactly 2^j-j-1 composite divisors of N, hence that many distinct irreducible factors of U_j.
To check that every one has positive measure, let d be any odd integer at least three and choose a=(d-1)/2.
One has gcd(a,d)=1, since any common divisor divides both d and d-1.
The corresponding actual conjugate root of Phi_d(x+1) is zeta_d^a-1 and satisfies

\[
 |\zeta_d^a-1|=2\cos\frac{\pi}{2d}\ge\sqrt3>1.
 \tag{12}
\]

Monicity and the root-product definition of Mahler measure now imply

\[
 m(\Phi_d(x+1))\ge\tfrac12\log3,
 \qquad r_+(U_j)=2^j-j-1,
 \qquad m(U_j)\ge (2^j-j-1)\tfrac12\log3.
 \tag{13}
\]

The growing factor count is real and requires no multiplicities, but its average total measure per positive factor is bounded away from zero.
Removing the nonunit prime-divisor factors therefore does not repair the construction.
This is a failure of a specific translated torsion/resultant mechanism, not a counterexample to Lehmer positivity and not an obstruction to every possible resultant.
No finite polynomial scan, numerical root approximation or asymptotic equidistribution statement is used.

<a id="good-heredity-source-comparison"></a>
## General fixed seeds: exact external comparison and limited source check

The inspected primary work is Alice Medvedev and Ramin Takloo-Bighash, [Multiplicative groups of fields and hereditarily irreducible polynomials](https://arxiv.org/html/1601.03424v1), arXiv:1601.03424v1, 13 January 2016, 21 pages.
The [online PDF](https://arxiv.org/pdf/1601.03424) displayed that same v1 version strip.
This exploration read Definition 6 on p.4, the finite-tree statement and displayed argument of Lemma 12 on p.6, Lemma 21 on pp.8--9, Theorem 24 on pp.9--10, Definition 25 on p.10, and Proposition 32(2)/Corollary 33 on pp.13--14.
The source defines good heredity by a fixed substitution P(x^A) factoring into polynomials h for which h(x^n) is irreducible for every positive n.
Its number-field conclusion applies when P has no zero or root-of-unity zero.

Applied to the positive-measure part P of a fixed integer polynomial, viewed in Q[x], this gives P(x^A)=c product_i h_i(x)^(a_i) for a fixed A and fixed factors.
Then P(x^(An)) has exactly sum_i a_i irreducible factors counted with multiplicity.
Each factor of P(x^n) has at least one factor after x->x^A, while distinct factors remain coprime, so r_+(P(x^n))<=sum_i a_i.
The removed zero-root and cyclotomic factors remain measure zero after substitution.
This extracts the general fixed-f bound, including nonmonic seeds, from the external statement; it does not extend the internal unit-lattice proof by assumption.

The printed v1 proof of Theorem 24 incorrectly calls x-a hereditarily irreducible from rootlessness modulo torsion and cites Proposition 16 there.
For a=4 over Q that intermediate assertion is false because x^2-4 is reducible.
The already inspected Lemma 21 gives good heredity instead, which suffices: the selected factors over F(a) form the same strictly branching chain, contradicting the finite-tree criterion of Lemma 12.
More explicitly, if Q_i divides P(x^(n_i)), its roots over the chosen a form one Galois orbit of size k_i over F(a).
The corresponding irreducible factor of x^(n_i)-a divides the appropriate substitution of the preceding factor, and the original proper branching gives k_(i+1)/n_(i+1)<k_i/n_i.
Thus the restricted chain still branches properly, whereas Lemma 21 and Lemma 12 make such an infinite chain impossible.
This checks that replacement at the displayed argument's scope, without claiming a complete source-proof or ancestral audit.
The internal calculation (3)--(9) does not depend on the defective printed sentence or on this source repair.

The 2026-11-05 bounded source search used fixed f(x^n), irreducible-factor bounds, Capelli, good heredity and rootlessness modulo torsion after checking the local mechanisms below and [The26-U001](../audits/literature/The26/Yin_U001.md#the26-u001).
The latter supplies only the recorded prime-binomial interface, not a uniform composite-exponent factor-count theorem.
The search stopped once the exact primary statement and the internal unit diagnostic settled the proposed fixed-seed mechanism.
No exhaustive literature coverage, original priority, whole journal/preprint equivalence or separately archived original is asserted.

<a id="comparison-and-reopening-condition"></a>
## Comparison with the retained routes and reopening condition

[C221](../claims/Yin_C_G0221_v1.md#neutral-completion) preserves total measure through cyclotomic completion and controls sparse multipliers at its stated entropy overhead; it does not add positive factors.
[C231](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) gives the relevant norm descent with actual degree loss and measure multiplicity, while (4)--(8) identify a fixed seed's ray-saturation obstruction to factor growth.
[C252 v2](../claims/Yin_C_G0252_v2.md#statement) already retains the full monomial-substitution measure identity and distinguishes individual factors from the full quotient.
[C376 v2](../claims/Yin_C_G0376_v2.md#statement) supplies actual irreducibility for the Lehmer polynomial's prime radical substitutions at every prime q>40.
Those growing-degree examples have one positive irreducible factor.

[C866 v7](../claims/Yin_C_G0866_v7.md#statement) constructs an actual irreducible norm endpoint, and [v8](../claims/Yin_C_G0866_v8.md#statement) and [v9](../claims/Yin_C_G0866_v9.md#statement) retain their inverse-realization, signature and basal/raw distinctions.
A large conjugate orbit, many possible same-measure realizations, or a large realization degree is not an increasing number of rational positive-measure factors in one bounded-measure polynomial.
No statement from those versions supplies that missing construction.

The present comparison rules out the fixed-seed radical mechanism and the specific translated torsion construction at their exact scopes.
It supplies no uniform positive Mahler gap and no positive-measure sequence tending to zero.
A reason to reopen this branch would be an actual new algebraic construction together with a checkable positive-factor count and a total-measure estimate that overcomes the displayed costs.
The sufficient counting condition alone, or a replacement of factor count by degree, root count or house, is not such a new input.
