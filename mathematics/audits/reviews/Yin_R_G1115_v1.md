---
author: Yin
---

# Independent whole review of balanced disjoint-edge rotating shears

## Review arrangement and inspected inputs

The review act is dated 2026-11-10T09:27 UTC, with Yin as the human record author.
This is an initial independent whole-proof inspection of the fixed [C889 v1](../../claims/Yin_C_G0889_v1.md), including every control, consequence and stated scope boundary.
The reviewer did not participate in the development of its disjoint-edge transfer, balanced-word reduction, Gaussian factorization or proof.
No author-development dialogue, mathematical summary, author explanation or prior C889 review conclusion was supplied or consulted before forming the findings.
The reviewer had previously worked on the broader strategy comparison and a separate periodic-symbol argument, and knew the common L462 v5 rotating-shear model.
That prior model familiarity supplies definition context, not development context for the distinct proof reviewed here.
The fixed Claim and its direct inputs were read as the initial mathematical evidence for this review.
No substantive repair was supplied, and no Claim text was changed.

The entire Claim was read, its local algebra and all displayed special cases were rederived by hand, and its full-degree, multiplicity and measure interfaces were checked from the actual matrices.
The [L462 v5 model](../../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law) and the construction/orientation portion of [J153's program](../../computations/programs/Yin_J_G0153/rotating_shears.py) were inspected as the directly cited definition controls.
No numerical experiment, sampling run, root calculation or program-based mathematical test was performed.
The old 72-input J153 experiment is not a premise of this proof, and its native result certificates were not newly reviewed.

The reviewer read [Den09-U001](../literature/Den09/Yin_U001.md#den09-u001), its actual [Mahler-measure section](../literature/Den09/Yin_U001.md#mahler-measure), and its edition note.
Only nonzero one-variable polynomial logarithmic integrability and the full Jensen/root-product identity, with unit-circle zeros allowed, are reused as accepted analytic inputs at the unit's recorded depth.
The original PDF and the foundational proofs of Jensen's formula and logarithmic integrability were not newly inspected.
No Fuglede--Kadison approximation, multiplicativity or normalized-height assertion is used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [C889 v1 complete artifact](../../claims/Yin_C_G0889_v1.md) | Entire fixed statement and argument, every displayed control and consequence, exact directly used inputs and original-goal limits. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [C889 v1 statement](../../claims/Yin_C_G0889_v1.md#statement) | Every g and every disjoint signed edge set, empty products, exact full characteristic identity, balanced c classification, norm factorization, full-measure bound and overlapping-edge exclusion from scope. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Local transfer and determinant](../../claims/Yin_C_G0889_v1.md#local-transfer) | Shift orientation, DE=ED=0, two-site equations, pivots and block signs, h=g-k, full cycle determinant, singular-parameter polynomial continuation and reciprocal normalization. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [One-edge and two-edge controls](../../claims/Yin_C_G0889_v1.md#one-two-edges) | All sign cases in the table, balanced two-edge neutrality, complete trace criterion, neutral-site placement and sufficient scalar-product condition. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Balanced-word argument](../../claims/Yin_C_G0889_v1.md#balanced-word) | Actual sign counts, anticommutation and scalar signs, effective parity, cyclic-start invariance of c, trace powers and exact Gaussian norm with all degrees and constants. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Whole-measure gap](../../claims/Yin_C_G0889_v1.md#whole-measure-gap) | Nonnegative binomial bound, boundary zeros, logarithmic integrability, exact sine integral from Jensen, complete norm cost and c=0 versus c>=1 alternatives. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Exceptional roots](../../claims/Yin_C_G0889_v1.md#exceptional-roots) | Exact zeros at 1 and -1, their simplicity in G, exclusion at i and -i, all unit-circle multiplicities and reciprocal exterior-root count. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Placement and limit consequences](../../claims/Yin_C_G0889_v1.md#placement-and-limit) | Actual balanced words at g=8, exact degree-twelve residual, g=9 norm and its only unit-circle factor, distinction of residual polynomials and the complete probability-shell exclusion. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Den09 canonical source unit](../literature/Den09/Yin_U001.md#den09-u001) | Canonical binding for the retained arXiv:0905.0604v1 scalar Mahler/Jensen input only; preserves source identity, accepted-input depth, height correction and unreviewed foundational proofs. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Actual Den09 analytic scope](../literature/Den09/Yin_U001.md#mahler-measure) | Natural logarithm, normalized Haar integral, integrability for a nonzero complex Laurent polynomial, one-variable full root-product formula and allowance for unit-circle zeros. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [Original rotating-shear model](../../ledger/Yin_L_G0462_v5.md#rotating-symplectic-law) | Actual integer matrices, independent balanced sign lists, cyclic sites and the inclusion of pairwise disjoint edge outcomes; no review of its entire unbounded sampling law or unrelated source arguments. |
| [Whole disjoint-edge finding](#balanced-disjoint-edge-transfer-review) | [J153 matrix implementation](../../computations/programs/Yin_J_G0153/rotating_shears.py) | Read-only check of shear_matrix and the sign-list construction: rotation orientation and block matrix agree with the Claim; no execution or renewed review of numerical certification. |

<a id="balanced-disjoint-edge-transfer-review"></a>
## Finding: the complete disjoint-edge proof is sufficient

No substantive gap was found in the full statement, argument, controls, source interface or stated consequences of C889 v1.
For every actual balanced pairwise-disjoint edge input, the claimed integer c is well defined independently of the cyclic starting point.
The complete polynomial is cyclotomic when c=0, and for c>=1 its full Mahler measure is at least c^2 4^c, hence at least four.
This conclusion is uniform in the allowed total length, number of active edges, neutral gaps and sign order, but does not cover overlapping active edges.
The finding supports acceptance at the source-inspection depth stated above; it does not itself select a C assessment or complete G0001.

### Full local transfer and determinant normalization

The support condition makes every v_i orthogonal to every w_j, including i=j, so both DE and ED vanish.
The original product of shears is therefore exactly the displayed block matrix with identity diagonal blocks.
The shift matrix in J153 is np.roll(identity,1,axis=0), which has S e_j=e_(j+1), agreeing with the Claim.
Left multiplication by diag(S^-1,S^-1) has determinant one and changes the eigenvalue equations to z u_(j+1) at the next site.
Directly expanding D and E on the two endpoints gives both equations (5), including the opposite upper-right sign in Q and the positive lower-left sign.
Adjacent active macro-steps are allowed as long as the original two-site supports are disjoint; no neutral site between them was assumed.
A cyclic choice of the starting site handles an edge crossing the coordinate boundary without changing the determinant.

The checked algebra is Q^2=-sI, C^2=sI and CQ=-QC.
It gives the displayed numerator F after elimination and det F=s(z^2+s)^2.
Each eliminated internal two-coordinate variable contributes exactly z^2+s.
All required row or column rearrangements exchange whole two-dimensional blocks and therefore have positive permutation sign.
One variable block is removed per active edge, leaving h=g-k cyclic vertices, rather than g-2k.
Eliminating the forward equations of that remaining cycle yields det(z^h I_2-W_h...W_1), with all powers of z accounted for.
The resulting scalar H and the determinant of the full ordered F product give equation (1) exactly.

The argument initially avoids the finite pivot-zero set and z=0, then compares two polynomial expressions on an infinite set.
This proves the identity at the excluded values as well; it does not discard their roots.
Because 2k<=g and g>=3, h=g-k is positive.
The leading term is z^(2g), the trace term has strictly smaller degree, and the constant term is sigma H(0)=1.
For k=0 the empty trace is two and the complete polynomial is (z^g-1)^2.
The usual exact symplectic block identities, with symmetric D,E and orthogonal S, give determinant one and reciprocal eigenvalue multiplicities.

### Low-edge controls and the order criterion

The single-edge trace is 2z(1+s), yielding both stated one-edge polynomials.
For two edges the cross coefficient is epsilon_2 eta_1+eta_2 epsilon_1=chi(s_1+s_2).
Substitution into the general identity verifies every row of (11): unequal s signs, two negative s signs, and the two possible chi signs when both s values are positive.
In the balanced two-edge case the second sign pair is the negative of the first, so chi=-1 and the resulting full binomial product is cyclotomic for either s.
No balanced-law conclusion was incorrectly imposed on a one-edge input.

At fixed g and fixed multiset of s values, k,h,H and sigma are fixed.
Equality of the complete polynomials is therefore equivalent to equality of the ordered trace polynomials, since the factor z^h is a nonzero polynomial.
Neutral steps contribute identity matrices, so redistributing them while preserving total length and cyclic sign order changes nothing.
The sufficient scalar-product condition gives sigma=1 by determinants and the stated full square; it is correctly not asserted to characterize all unbalanced inputs.

### Balanced signs, cyclic parity and the Gaussian factorization

The two independent balancing equations imply n_(++)=n_(--) and n_(+-)=n_(-+).
The K,J identities in (13) were checked by direct multiplication.
Extracting the b signs from -J and collecting 2b copies of J gives (-1)^b J^(2b)=(4-t^2)^b I.
Moving each J left toggles the sign of K in precisely the factors it crosses and introduces no additional scalar sign.
In the product N_k...N_1, the preceding active edges are to the right, so the exponent r_j in (2) has the correct orientation.
The effective plus and minus counts p,q obey p+q=2a, making |p-q|/2 an integer in [0,a].
Moving the cyclic start changes all effective signs by the common parity of the crossed negative-s edges, since their total number 2b is even.
This verifies the claimed invariance of c.

Pairing the commuting factors 2I+K and 2I-K gives the t^(2a-2c) factor.
Their equal even-power traces follow from zero traces of odd powers of K and cover both p>=q and p<q.
The substitutions t=z+z^-1 and w=z-z^-1 give the scalar factor (-1)^(b+c) z^-k in (16), with the stated powers of z^2+1 and z^2-1.
Multiplying G and its coefficient conjugate reproduces the remaining bracket without changing the variable.
The exponents 2a-2c and 2b are nonnegative, and h>0 makes G monic of degree h+2c with constant (-1)^(b+1).
The complete degree is 2g and the norm has integer coefficients.
All cancellations used to derive the Laurent identity are justified by its final polynomial identity; no selected Gaussian factor replaces the full integer polynomial.
The c=0 specialization is exactly the claimed cyclotomic binomial product, including the empty balanced case.

### Analytic input and the complete lower bound

On z=e^(i theta), the squared distances to -i and i are 2+2sin(theta) and 2-2sin(theta), respectively.
The two summands of G have those c-th-power moduli, because z^h and tau have modulus one.
The reverse triangle inequality therefore gives (17).
After replacing sin(theta) by its absolute value, every odd binomial term is nonnegative, and the first term yields c 2^(c+1)|sin(theta)|.
The bound is valid for every c>=1 and is independent of h and the phase of either summand.

The actual Den09-U001 interface covers nonzero complex polynomials, so it applies to the Gaussian polynomial G as well as to 1-z^2.
It permits unit-circle zeros and uses the unnormalized total root-product measure with normalized Haar integration.
Since G is monic of positive degree, it is not the zero polynomial.
The source's integrability assertion and Jensen identity for 1-z^2 give the sine logarithm integral -log 2, including its two integrable singularities.
Taking logarithms of (17) off those two points and integrating is therefore legitimate without a principal value, truncation error or nonvanishing hypothesis.
This yields m(G)>=log c+c log 2.
Coefficient conjugation preserves every root modulus and polynomial products add all root contributions, so the complete identity is m(P_A)=2m(G), not a degree-normalized version.
All remaining factors in (3) have measure one.
Exponentiation gives precisely M(P_A)>=c^2 4^c.

The review accepts only that scalar analytic interface at the source unit's recorded depth.
The normalized-Weil-height sentence questioned in Den09-U001 is not used by the Claim.
The original proof of logarithmic integrability and Jensen's formula was not independently re-audited, and the source unit's unrelated determinant results supply no premise here.

### Exceptional multiplicities and exterior roots

For c>=1 the strict positive lower bound in (17) away from the sine zeros rules out any unit-circle zero of G other than 1 or -1.
At 1 the ratio of the two nonzero powers is (-1)^c, giving the condition b even.
At -1 the additional factor (-1)^h gives exactly h congruent to b modulo two.
At either possible zero, the difference of logarithmic derivatives is the stated h/z-4ci/(z^2+1), whose imaginary part at each endpoint is nonzero because c>=1.
Thus each permitted endpoint root is simple in G and its coefficient conjugate.
Direct substitution at i and -i gives the displayed nonzero values, so only the explicit prefactor contributes those roots.

Adding every prefactor and norm multiplicity yields the whole table (18).
Subtracting that total unit-circle count from degree 2g and pairing all remaining roots reciprocally gives exactly the stated N_+(A).
The c=0 case is correctly handled by its full binomial product rather than by the c>=1 table.
No algebraic multiplicity is replaced by a count of distinct roots.

### Concrete order and length controls

For the first g=8 word the two same-sign factors have effective signs +1 and -1, so c=0.
For the reordered word they both have effective sign +1, so a=b=c=1.
Both sign lists satisfy the two original balancing conditions and use actual disjoint edges.
With h=4 and tau=1, direct expansion of G times its coefficient conjugate gives the stated even degree-twelve polynomial, and its prefactor is (z^2-1)^2.
The endpoint table gives no unit-circle root in that degree-twelve residual.

At g=9 the same word has h=5.
Expansion gives the stated norm (z^2+1)^2(z^10+1)-2z^5(z^4-6z^2+1).
The endpoint conditions give its only unit-circle factor (z+1)^2.
The leading coefficient after division is one and the next coefficient is -2, confirming the stated difference from the even degree-twelve residual at g=8.
Their equal degree and nonzero constant terms exclude a proper power substitution from one of these two residual polynomials to the other.
This is a comparison of complete noncyclotomic residual polynomials, not an irreducibility or primitive-core classification, and no inequality between their individual measures is claimed or needed.

### Conclusion and limits

The exact identity and the analytic bound cover every balanced disjoint-edge input, including unbounded k and the dilute regime k=o(g) when the edges satisfy the support condition.
They give no mass in the strict shell 1<M<4 for any law supported there.
This conclusion follows from the exact per-input theorem, without a distributional or numerical extrapolation.
Overlapping edges can make DE nonzero and change the actual local equations; the proof correctly supplies no exclusion for that remaining class.
The theorem is a restricted construction obstruction and does not resolve the unrestricted Lehmer contract.
No computational certificate, source-proof coverage or independent verification beyond the actual checks above is claimed.
