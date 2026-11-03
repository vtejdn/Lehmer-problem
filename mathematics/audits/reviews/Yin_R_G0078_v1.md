---
author: Yin
---

# Retained project review: Trinomial eventual positivity and height-one negative phase balance

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0179_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="trinomial-limit-independent-review"></a>

### Complete separate independent review

On 2026-10-10 the coordinating AI for Yin read and checked the complete frozen proof above and found no mathematical defect at its stated scopes.
It assigned the limiting-sign question but supplied none of the polynomial section, integral, inequalities or uniform-limit derivations; its separate general-height-one construction is not used here.
The review is noncontributing and separately organized, with shared task context and author progress explanations, not blind or a personal human inspection.
No author mathematics was changed by this finding.

The reviewer verified the exact substitution of F,H,G and the complete expansion inherited from L175.
Coprimality gives every integer relation as a multiple of(a-b,-b), so q=max(b,a-b) and its lower bound a/2 are exact.
The already accepted Den09-U002 interface covers arbitrary integral vectors and zeros, and thus yields uniformity over all offsets by the displayed sequence contradiction.
The review reread that source-owned interface; it does not claim to have audited Lawton's original proof or replace it by Den09's invertible-only result.

Dividing the sparse G by its torus monomial and rotating v gives precisely the four cosine terms in(9).
The reciprocal quartic has trace polynomial x squared+2Ax-D squared.
The reviewer directly expanded A squared+D squared and both evaluations at plus/minus two, verifying(10)--(11) including the endpoint degeneracies.
The two trace roots have opposite signs.
In the exterior angular range the square-root product is D(D-2), giving the hyperbolic addition identity and the nonnegative branch in(12).
In the complementary range both roots are in[-2,2], so the Jensen contribution is zero.
The theta parametrization and reflection symmetry give the factor2/pi in(13).
The coefficient absolute sum for G is13.
Its bounded positive logarithmic part and nonnegative monic-quartic section integral bound the negative part before Tonelli/Fubini, so circle zeros create no omitted hypothesis.
The analogous linear Jensen computation gives(14), and the exact phase identity follows from a difference of integrable logarithms, with the doubling map preserving Haar measure.

The integrand is decreasing on the required interval.
Its values at pi/12 and pi/8, their comparisons with cosh(log4) and cosh(log3), and the resulting interval lengths give log48/12 with the correct factor.
Concavity supplies an upper integral estimate on each seed half-interval, and the product of the two midpoint values is1+sqrt3.
The reviewer separately recomputed the final integer values U,V,250(U-V) and12U; they are exactly the displayed integers, proving the strict1/250 margin without decimal quadrature.
Uniform convergence with error less than1/500 then gives the eventual1/500 lower bound and finiteness of exceptions.
It supplies no computable cutoff or proof that the exceptional set is empty.

This is a full written mathematical review of the theorem with its accepted external limit input, not a new source proof audit or finite enumeration.
No new J or numerical integration was needed or claimed.
The earlier45 discovery decimals remain unused, and neither irreducibility nor a near-one/single-Salem-root conclusion has been introduced.
The unrestricted G0001 objective remains unresolved.

<a id="height-one-negative-phase-independent-review"></a>

### Complete independent proof and certificate finding

On 2026-10-10 the separately assigned resultant_research AI for Yin read and checked the entire frozen D45, including its statement, Sections1--5 and source/contribution boundaries, together with J37's program, readme and complete certificate.
No mathematical defect, necessary correction or missing scope condition was found.
The reviewer supplied none of this construction, fixed-seed computation, effective averaging proof or negative-balance deductions.
It had authored the earlier trinomial controls retained in L175, which provide background to the question but are not premises of D45's proof, and received the coordinator's description of the strengthening before review.
This is separately organized noncontributor review, not a blind or human proof inspection.
The author proof was not edited; this finding is appended.

The paired recursion has disjoint blocks and exact coefficient signs at every level.
Its parallelogram identity starts from total squared norm2 and doubles at each level, giving128 for the sixth pair and the displayed sup-norm bound for the normalized monic h0.
The reviewer independently reconstructed h0 by the binary adjacent-one parity formula, then verified that those independently generated lists obey all six of the author's recursive relations.
The entire64-entry coefficient list agrees with the retained artifact, and every paired Laurent autocorrelation is exact.
Squarefreeness is checked by an exact integer-polynomial gcd.
This confirms the precise single input being isolated rather than just reproducing its root-product decimal.

[J38](../../computations/programs/Yin_J_G0038/readme.md) retains the separately written reviewer program and full output.
A fresh320-bit Arb computation with maximum isolation precision1024 returns all63 roots in pairwise disjoint balls, with31 strictly exterior and32 strictly interior to the unit circle.
Their complete exterior-modulus product is enclosed near6.85057293091927989912365455877, rigorously exceeds137/20, and has cube greater than128.
Both the root count and every comparison with one are decided by ball inequalities.
This is an independent implementation/reconstruction and stronger-precision execution, while sharing the underlying FLINT/Arb root-isolation library; it is not an independently proved arithmetic library or a formal proof-assistant certificate.
Rounded displays do not substitute for the actual rerunnable interval operations.
No higher-degree seed or specialization was computed.

For h_k, unique base64 digit expansion really prevents every coefficient collision across the separated factors.
It gives every coefficient a single product of signs and degree64^k-1, with leading coefficient one.
Circle substitution preserves each factor's logarithmic Mahler integral, so multiplicativity supplies M(h_k)=M(h0)^k, while the product of the pointwise bounds gives C_k.
In f_(k,n), n>=1 makes the low block, middle monomial and high block pairwise disjoint.
Its actual degree is2(D+n), leading coefficient one and constant coefficient-1.
Reversal at that exact degree gives f+f*=2t^(D+n).
Consequently gcd(f,f*)=1 over Q[t], excluding every nonconstant reciprocal or cyclotomic factor without asserting irreducibility.
The circle identity has real part one after monomial normalization, proving absence of every unit-circle root and the stated sup-norm estimate.

The complete quantitative averaging step is valid.
On the two-torus, z^(-D)h*(z)=conjugate(h(z)), so P_k/y is exactly1+yh(z)-conjugate(yh(z)).
Its modulus is at least one, making H continuously differentiable with no logarithmic singularity.
Differentiating in theta at fixed phi gives the sum of two coefficient-derivative bounds, exactly D(D+1).
The identity f=t^D P_k(t,t^n) has the displayed exponents.
Partitioning theta into n equal intervals and using phi=n theta-2pi j proves the diagonal-average formula.
Inserting an independent psi average on the same subintervals gives the full torus average.
The two first arguments differ by at most2pi/n, so the Lipschitz estimate proves(6) directly.
This involves only finite continuous integrals; no Lawton theorem, unproved logarithmic interchange or unknown specialization rate is used.

For each nonzero h(z), Jensen in y bounds the quadratic's measure below by the logarithm of its leading coefficient modulus |h(z)|.
Its finitely many exceptional zeros are harmless for the integrable log|h| lower bound.
Thus(7) follows without needing any irreducibility of h or its specialized products.
The scalar inequality log(1+x)>x/(1+x) gives log(137/136)>1/137.
The reviewer checked the exact rational comparisons8/1100<1/137 and1/40<4/137; pi<4 makes both stated error cutoffs strict enough.
The all-k cutoff proves m(f)>k log(34/5), and the sharper four-copy cutoff works for every integer n>=320D_4(D_4+1).
Its numerical integer value is90071987178700800, with D_4=16777215, retained only as a parameter check.
No claim that a polynomial of that size was expanded is made.

The mod-two identity proves G_f integral with the actual reversal in both terms.
Expanding f*=u-f gives(8) with the correct factor two and signs.
The three contributions on the circle give3F_k^2+2F_k after division by two, including the linear term2F_k.
Since f(1)=f*(1)=1, G_f(1)=1 proves both nonvanishing and primitive content; all remaining leading coefficients and factors stay inside m(G_f).
The full phase identity retains its factor2 and all three copies of m(f), because the doubling map preserves normalized circle measure.
The seed has no circle zero and any auxiliary zeros have integrable logarithms, so the phase calculation is complete rather than a selected Fourier mode.

The exact rational quantity in(10) was separately recomputed in J38 and is strictly below2/3.
Combining it with the strict measure lower bound gives Delta(f_(4,n))<log(2/3) throughout the explicit cutoff range.
Distinct n have distinct degrees.
For varying k, F_k<=3C_k and3F_k^2+2F_k<=33C_k^2 give the stated log66 bound.
The exact positive ratio(34/5)^3/128 makes the right side tend to minus infinity, while the proved seed measures grow at least linearly in k.
All these f remain monic units of coefficient height one and have no reciprocal or cyclotomic factor by the same actual-degree argument.

The strengthened conclusion is therefore fully supported at the stated broad height-one scope, and the initial Lawton approach remains truthful historical provenance rather than a current dependency.
This review does not supply irreducibility of f, a three-term example, a small-measure sequence, or an identification with actual delayed Salem-family mixed energies.
The negative conclusion is about the complete defined phase balance.
The full written proof and one-input numerical certificate are reviewed; fixed adoption and the unrestricted G0001 goal remain separate decisions.
Later substantive changes require a correspondingly new finding.

<a id="phase-sign-boundaries-retention-record"></a>

## Retention and review map

On 2026-10-10 D G0044 and D G0045 were adopted together because they settle two distinct sign boundaries for the same complete phase balance.
The former whole proof and the latter whole proof/certificate passed separate noncontributor review at their exact disclosed scopes.
The subsequent literature-rate follow-up is separate ongoing work and is not incorporated as an accepted input here.

The complete arguments and their reviews are retained at the linked scopes, with actual consumers redirected.
Necessary J37/J38 programs, certificates and distinct checking results remain available.
Retention does not replace the mathematical reviews or establish a scale-uniform Lehmer gap.

| Former material | Complete retained scope | Actual review |
| --- | --- | --- |
| D G0044 | [Full primitive-trinomial limit argument](../../ledger/Yin_L_G0179_v1.md#retained-trinomial-limit-argument) | [Coordinator noncontributor finding](#trinomial-limit-independent-review) |
| D G0045 | [Full height-one negative construction](../../ledger/Yin_L_G0179_v1.md#retained-height-one-negative-argument) | [Resultant AI noncontributor finding and J38](#height-one-negative-phase-independent-review) |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete trinomial-limit finding](#trinomial-limit-independent-review) | [Entire primitive-trinomial limit argument](../../ledger/Yin_L_G0179_v1.md#retained-trinomial-limit-argument) | Entire original D44: primitive-exponent hypotheses, exact full auxiliary, accepted qualitative Lawton interface including zeros and uniformity, quartic sectional trace/branch calculation, Fubini/logarithmic integrability, exact rational Delta_infinity>1/250 certificate and eventual Delta>1/500, with no effective cutoff or all-degree sign claim. |
| [Complete height-one negative finding](#height-one-negative-phase-independent-review) | [Entire height-one negative construction](../../ledger/Yin_L_G0179_v1.md#retained-height-one-negative-argument) | Entire original D45 Sections1--5 and J37 certificate, separately authored J38 input/root check, recursion and separated products, actual-degree monic-unit/height-one and no-reciprocal-factor identities, elementary quantitative averaging and explicit cutoff, complete auxiliary integral and negative/divergent balance, with growing measure and no irreducibility/three-term/near-one conclusion. |
| [Original complete trinomial-limit author check](#trinomial-limit-original-author-check-finding) | [Original complete primitive-trinomial proof](../../ledger/Yin_L_G0179_v1.md#retained-trinomial-limit-argument) | Actual original2026-10-10day-precision explicit complete author self-check of D44: relation-parameter/uniform Lawton application, rotated quartic/Jensen/integrability, exact positive rational certificate and finite-exception conclusion, with the exact accepted source interface and original pending/fixed/source limits. |

## Review relationships

The entire original mathematical/native/source/contribution account, dates, verdicts, retention map and both original whole bindings remain unchanged.
The original independent titles and earlier administrative independently-reviewed labels remain historical declarations.
These declarations assess the actual recorded input arrangement without a new old inspection or an invented communication history.

The original complete trinomial-limit finding assigned the question and supplied none of the derivations.
Its generic shared Task context and author progress explanations do not preserve their actual initial mathematical contents.
Neither noncontribution nor that generic description establishes isolation or known substantive prior sharing.
Its entire original D44 scope therefore remains unknown for independent-review purposes.

The original complete height-one proof/certificate finding received a coordinator description of the strengthening before review.
The record does not preserve the actual contents of that description or establish whether it supplied substantive target mathematics rather than scope/status information.
The frozen proof does preserve exactly what changed: its valid qualitative Lawton argument was strengthened before review to a direct quantitative estimate using the positive torus modulus.
That proof history is not automatically the missing communication transcript.
The reviewer's earlier L175 trinomial authorship is background, explicitly not a premise of this proof, and does not by itself make this finding self-reviewed.
Its entire original D45 Sections1--5/J37/J38/source/contribution target remains unknown.
The original separately authored fixed-seed reconstruction and stronger-precision Arb check remain actual evidence with their shared FLINT/Arb library boundary.
No new native run, input hash, source proof audit, mathematical error or repaired-proof episode is inferred.

The original D44 explicitly records a complete author self-check.
That known arrangement is self-reviewed below with the original paragraph preserved verbatim.
D45 records its coordinator authorship and three successful fixed-input J37 runs at successive sufficient thresholds, but does not separately record a complete author-review event.
No additional original D45 author/coordinator whole finding or finer timestamp is invented.
Both unknown whole targets retain their complete existing scope for fresh isolated coverage.
Current authored self-checks do not discharge those original independent-review obligations.

| Review | Relationship |
| --- | --- |
| [Original complete trinomial-limit finding](#trinomial-limit-independent-review) | unknown |
| [Original complete height-one proof/certificate finding](#height-one-negative-phase-independent-review) | unknown |
| [Original complete trinomial-limit author check](#trinomial-limit-original-author-check-finding) | self-reviewed |

<a id="trinomial-limit-original-author-check-finding"></a>
## Original complete trinomial-limit author check

Date: 2026-10-10.
This retains the exact original complete author-checking/contribution/source paragraph, including its then-pending disposition.

The assigned orbit_research AI supplied the exact relation-parameter application, rotated quartic section, trace-root classification, hyperbolic simplification, two-interval/concavity bounds and finite-exception conclusion in this draft.
The parent selected the precise trinomial-versus-controlled-measure question and supplied no steps of this derivation.
The complete argument has been self-checked; independent review and fixed adoption remain outstanding.
The fixed L175 sparse polynomial and source-scoped Den09-U002/L50 Lawton interface were reused explicitly.
No new source intake, new J computation, enlarged pilot or novelty claim was made.
G0001 remains active and unresolved.
