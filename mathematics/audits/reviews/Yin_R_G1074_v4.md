---
author: Yin
---
# Independent review of synchronized quadratic Hankel nonzero indices

Review act: 2026-11-05T00:41 UTC.
The human record author is Yin.
This is a separately organized whole-proof agent review of the fixed [C858 v3 theorem](../../claims/Yin_C_G0858_v3.md#exact-theorem), its [divisor conventions](../../claims/Yin_C_G0858_v3.md#divisor-conventions), and the complete argument from the [exact coefficient map](../../claims/Yin_C_G0858_v3.md#exact-pade-map) through the [final limits](../../claims/Yin_C_G0858_v3.md#limits).
The reviewer did not develop this version and received no proof-development dialogue, proposing-agent mathematical summary or previous verdict on this candidate.
The fixed candidate, necessary C/U inputs and actual selected primary source passages were read directly; D19, D20 and development conversations were not read.
The reviewer supplied no substantive proof repair.
The final statement's polynomial domain for s and the nonzero-determinant domain of the all-prime identity were checked in the final text.

The earlier [R1074 v3 finding](Yin_R_G1074_v3.md#actual-hankel-residue-whole) remains evidence for the exact adopted C858 v2 input: original integrality, the nonzero dyadic residue layer and odd-prime nonrationality.
Its individual-prime infinite index sets do not supply a common progression, and its verdict is not transferred to the new argument.
This new finding is retained in the same review family because it checks genuinely new synchronization and lattice evidence for the same actual Hankel-valuation question.

<a id="synchronized-hankel-indices-whole"></a>
## Complete split-quadratic and synchronization finding

**Finding:** no unresolved mathematical gap was found in the whole final C858 v3 theorem G/A/B/C and its complete argument, including QL0--QL6, NI1--NI11, both genus assertions, zero-index normalizations and the original-prime consequence.
The common positive multiples follow from an actual zero-index proof and preservation of the entire polynomial lattice, rather than from separate infinite subsequences or ultimate periodicity alone.
The explicit divisor models and the general lattice construction have their different stated periods and hypotheses.
This finding selects no Claim assessment, supplies no original-task completion, and does not assert any uniform period or total-prime valuation bound.

### Exact shift and reversal

For b(z)=sum_j beta_j z^(h-1-j), the coefficient of z^(h+i) in bf is exactly sum_j beta_j f_(i+j+1).
The h kernel equations therefore kill precisely the coefficients from degree h through 2h-1.
The unique degree-below-h truncation a gives bf-a=O(z^(2h)), with no extra equation on the constant coefficient of f.
Reversing both polynomials at degree h-1 multiplies this error by X^(h-1), giving O(X^(-h-1)).
The degree bounds deg A,deg B<=h-1 are preserved even when endpoint coefficients vanish.
Thus NI7 and NI8 identify the original shifted h-square matrix, rather than an adjacent Hankel convention.
All subsequent maps use this same normalization.

### Odd-characteristic model and its complete kernel map

The reversal sends U,V to monic degree-d polynomials u,v with the same squarefreeness and coprimality, since U(0)=V(0)=1 and both original degrees are d.
The squarefree product uv is not a square over the algebraic closure, proving geometric integrality.
The affine derivative test is valid at branch points as well as away from them because the characteristic is odd.
At infinity eta=y/X^d satisfies eta^2=U(z)V(z) and has the two simple roots 1,-1 at z=0.
These give two smooth k-rational unramified places with z=1/X as uniformizer and f=y/u having residues 1,-1.

At each closed branch place above u=0, ord(u)=2 and ord(y)=1, and the residue field is the corresponding residue field of u.
Thus D_u includes each such closed place once, its degree is d with residue degrees counted, and div(u)=2D_u-dP_+-dP_-.
It follows directly that deg E_h=d-2.
For R=uA-By the NI8 error gives ord_(P_+)R>=h-d+1, while the degree bounds give the pole bound h+d-1 at P_- and a zero along D_u.
This proves the forward inclusion in L(E_h); nonrationality makes it injective.

For the reverse map, finite regularity of R and sigma R makes C=(R+sigma R)/2 a polynomial in the representation R=C+Dy.
Finite regularity of Dy excludes poles of D both away from branch points and at them: at a branch point a base-function pole has even negative valuation, while y has valuation one.
Hence D is polynomial, and the required zero along D_u forces squarefree u to divide C.
Both R and sigma R have pole orders at most h+d-1 at either infinity for every h>=0.
Their half-sum and half-difference therefore bound deg A and deg B by h-1 in the unique representation R=uA-By.
Dividing the P_+ condition by u recovers exactly NI8 and then the original kernel vector.
At h=0 both degree bounds are negative, forcing R=0; this proves L(E_0)=0 independently of the positive-index map.

### Characteristic-two model and its complete kernel map

The nonzero w/u has simple geometric poles, so it cannot equal Q^2+Q even over an algebraic closure: every pole of such an image has even highest order.
This proves geometric integrality, while the nonzero derivative u with respect to t proves separability.
At u=0 the other affine derivative is u'w!=0, and away from u=0 the t-derivative is nonzero.
The identity u=t^2/(w+t) at a branch point gives ord(u)=2 and ord(t)=1 with unchanged residue field, so deg D_u=b.

Since deg w<b, the equation F^2+F=w/u has a unique Laurent branch with constant zero and the second branch F+1 with constant one.
Its derivative in F is one, so these are distinct rational unramified infinity places, with z as uniformizer.
The pole order of t is b at P_- and at most b-1 at P_+; that asymmetry is retained throughout the degree estimates.
The forward map R=uA-Bt satisfies exactly the required orders and is injective.

In the reverse map R=C+Dt, the trace R+sigma R=uD is a polynomial.
Any remaining possible finite pole of D must therefore be a simple base-field pole at a zero of u.
Its valuation on the curve would be -2, giving Dt valuation -1, which cannot be cancelled by the even valuation of the base function C.
Finite regularity excludes this possibility, so C,D are polynomials.
The zero along D_u gives u|C, and trace at infinity bounds deg B by h-1 in R=uA-Bt.
Subtracting Bt then bounds deg A by h-1 as well.
The P_+ order recovers NI8, and h=0 again forces A=B=0.
Thus the characteristic-two isomorphism and zero-index result do not use division by two or an unproved tame-ramification formula.

### Genus and the rational divisor class group

The same finite-regularity arguments apply without the zero condition along D_u.
For N>=r, where r=d or b, a function with poles at most N at both infinities has unique polynomial coordinates C,D with deg C<=N and deg D<=N-r.
In characteristic two it is trace, followed by subtraction of Dt, that proves these bounds despite the unequal pole orders of t.
This gives dimension 2N-r+2.
For sufficiently large N the accepted Riemann--Roch formula gives dimension 2N+1-g, since the complementary canonical divisor has negative degree.
Therefore g=r-1 and deg E_h=g-1 in both explicit models.
Geometric integrality and the rational infinity places give full constant field k, so these dimensions and genera are over the stated field.

The class group used in the proof is explicitly the group of degree-zero k-divisors modulo principal divisors of functions in K.
Riemann--Roch gives a nonzero k-rational section of D+gP_+ for every such divisor D, representing its class by A-gP_+ with A effective of degree g.
Only finitely many closed points have degree at most g over a finite field, and only finitely many effective sums of bounded degree can be formed from them.
This proves finiteness at the required rational-divisor scope, including the trivial group when g=0.
There is no descent from an unspecified geometric Jacobian point.
Since E_h=E_0+h(P_--P_+), the order T of that class makes L(E_(h+T)) and L(E_h) isomorphic for all h>=0.
Together with L(E_0)=0 this proves every positive multiple in NI3, not merely some periodic nonempty class.
The case d=1 or b=1 is covered: the genus is zero and every positive index is nonzero.

### General split germ and polynomial-lattice preservation

In G, the distinct infinity residues imply that f is not in k(X), so 1,f is a basis and M is a full rank-two polynomial lattice.
The two rational places have ramification index one and exhaust the degree above infinity, giving the asserted uniformizer.
Any algebraic constant embeds in their residue field k, which verifies the full-constant-field hypothesis for the smooth projective model and the rational class-group argument.

The key reverse implication in QL2 was checked directly.
For nonzero R=A-Bf, let r=max(deg A,deg B) and take the degree-r coefficients a_r,b_r.
Positive order at P_+ forces a_r-b_r c_+=0.
Since c_+!=c_- and the leading pair is nonzero, a_r-b_r c_-!=0, so the order at P_- is exactly -r.
The second V_h inequality therefore forces r<=h-1.
This recovers NI8 for every h>=1 and makes V_0=0 because r cannot be negative.
Finite poles of f are unrestricted and no finite-pole divisor formula from A or B is being applied here.

Tag 032L applies to k[X], a Noetherian normal domain, and to the separable quadratic field extension.
Thus O is finite and torsion free over this PID.
Clearing an algebraic equation makes a nonzero polynomial multiple of f integral, so O spans K and its free rank is exactly two.
Clearing the two basis changes gives the explicitly stated polynomial s in k[X] minus zero with sO subset M subset s^(-1)O.
No ring property of M is required.

The rational class-group order T_0 supplies an actual epsilon in K with divisor T_0(P_+-P_-).
Both epsilon and its inverse have no finite poles.
Their conjugates have the same property, so trace and norm are polynomials in X and the associated monic equations put both functions in O.
This establishes that epsilon is an O-unit, rather than assuming that every class-group function preserves M.

If s is constant, the two lattice inclusions give M=O.
Otherwise the finite k[X]-module O has finite quotient O/s^2 O, and the image of epsilon has finite order N in its unit group.
Both epsilon^N-1 and epsilon^(-N)-1 lie in s^2 O.
Multiplying these differences by M subset s^(-1)O lands in sO subset M, giving both inclusions and hence epsilon^N M=M.
This is the necessary full-lattice preservation; nilpotents in the finite quotient cause no difficulty for its finite unit group.

The sign of the divisor is consistent with increasing h: multiplication by epsilon^N adds T=NT_0 to the order at P_+ and subtracts T at P_-.
It therefore bijects V_h with V_(h+T), with its inverse preserving the exact opposite inequalities.
Combining this with V_0=0 proves periodic kernel dimensions from zero and QL0/QL6.
Neither minimality of T nor periodicity of the determinant values is inferred.
The extra factor N is permitted; the sharper divisor periods in A and B are not silently assigned to the general lattice.

### Original-prime application and finite synchronization

The adopted C858 v2 input supplies exactly G=1+2H in Z[[z]], the nonzero-class nonrationality of Hbar, and the squarefree/coprime reductions of P_2,P_4 at good odd primes.
Thus A supplies a period for each such odd prime using the same constant-one branch and the same shifted determinants.
For the simple-pole dyadic specialization, reversing the reduced fraction a/q gives the required monic squarefree u and nonzero w, with deg w<b because a(0)=0 and with coprimality preserved.
The original Hbar is B's constant-zero branch.

For repeated dyadic poles, Hbar^2+Hbar=r and nonrationality give a separable quadratic function field.
At infinity the two formal branches have distinct constants 0,1, supplying Part G's rational split places without replacing r or imposing simple finite poles.
At an odd prime with nonrational Gbar, the quadratic square-root equation is separable and its two formal branches have constants 1,-1.
Thus Part G also covers the extra odd primes allowed in C, irrespective of finite singularities of an unreduced plane equation.
The normalized smooth model and lattice, rather than that plane equation, are used in this extension.

At every selected odd prime the determinant is a unit at all positive multiples of its period.
For the selected dyadic branch, the exact row factor Delta_h(G)=2^h Delta_h(H) makes its valuation exactly h at those multiples.
Taking the least common multiple of finitely many periods consequently proves NI5 and NI6 for every j>=1, with no compatibility assumption between unspecified residue classes.
If the odd set is empty and the dyadic assertion is not selected, L=1 is a vacuous choice and does not assert nonvanishing.
If at least one place is selected, its unit determinant or exact dyadic valuation itself guarantees that the original integer determinant is nonzero.

The selected logarithmic finite-prime sum is therefore zero, or h log 2 when the dyadic branch is included, on this progression.
It cannot supply a positive all-late quadratic lower bound using only those fixed places.
The final all-prime identity is correctly restricted to nonzero determinants and concerns the logarithmically weighted sum sum_p v_p(Delta_h(G)) log p.
Neither that entire sum nor a prime set growing with h is controlled by the theorem.

### Actual source inspection and evidence limits

The reviewer read [The26b U006](../literature/The26b/Yin_U006.md#accepted-curve-lattice-inputs) and the actual retained official HTML editions identified in its [source notes](../literature/The26b/readme.md#curves-and-finite-lattices).
Tag 0BXX, Theorem 53.2.6 and Lemma 53.2.8, provide the nonsingular projective model and smoothness over the perfect finite field.
Tag 0B5B, equation 53.5.0.3 and Lemma 53.5.2, provide Riemann--Roch, the canonical degree and the dimension duality used here, with no characteristic-zero restriction.
Their exact statements and displayed explanations were inspected; normalization, compactification and full duality ancestors were not independently audited.
The retained Commutative Algebra chapter was read at printed/PDF page 442, Lemma 161.8/Tag 032L, including its finite trace-dual-module proof.
Its underlying trace-pairing and minimal-polynomial inputs were not separately audited.
These accepted source inputs meet the actual hypotheses above and are not being claimed as newly proved project theorems.

The reviewer also read [Han16 U001](../literature/Han16/Yin_U001.md#shifted-application-and-limit) and the retained author manuscript dated 22 August 2016, printed/PDF pages 1--3, definition 1.1 and Theorem 1.1(i).
The source uses H_h(F)=det(F_(i+j)), so F=(G-1)/z or F=H/z gives precisely the original shifted sequence.
The displayed polynomial conversions have B(0)=1 and nonzero C with C(0)=0, as required for the original prime-field applications.
Its conclusion is ultimate periodicity; the text correctly uses it only for attribution and comparison, not as evidence for a zero residue class or synchronized primes.
Section 3's full proof, Algorithm 3.3 and any implementation were not audited or executed.
No source-wide priority conclusion, numerical determinant experiment, proof-assistant verification or unrestricted Mahler-gap result follows from this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete finding](#synchronized-hankel-indices-whole) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete finding](#synchronized-hankel-indices-whole) | [C858 v3 complete theorem](../../claims/Yin_C_G0858_v3.md#exact-theorem) | All G/A/B/C, QL0 and NI1--NI6, original shifted convention, rational divisor normalization, periods from index zero, simultaneous prime conclusions and exact limitations. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Divisor conventions](../../claims/Yin_C_G0858_v3.md#divisor-conventions) | Closed-point degrees, principal divisors over K, rational class group, L(D), field of sections and split-infinity uniformizer. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Complete argument entrance](../../claims/Yin_C_G0858_v3.md#exact-pade-map) | Entire assembled proof from NI7/NI8 through the two curve correspondences, genus/class-group argument, general lattice stabilization, original synchronization and final limits. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Odd-characteristic correspondence](../../claims/Yin_C_G0858_v3.md#odd-proof) | Exact model and valuations, bidirectional map NI9/NI10, closed branch divisor, all h>=1 and independent h=0 proof. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Characteristic-two correspondence](../../claims/Yin_C_G0858_v3.md#binary-proof) | Separability, smoothness, ramification, trace/parity reverse map, NI11 and L(E_0)=0. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Genus and finite rational class group](../../claims/Yin_C_G0858_v3.md#genus-and-period) | Exact dimensions and genus, accepted Riemann--Roch interface, finite k-divisor classes, genus-zero case and nonzero multiples of the explicit divisor period. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Original synchronization](../../claims/Yin_C_G0858_v3.md#original-synchronization) | Same original series and shifted determinants, simple-pole dyadic reversal, exact row factor, finite least common multiple and empty-set boundary. |
| [Complete finding](#synchronized-hankel-indices-whole) | [General quadratic lattice](../../claims/Yin_C_G0858_v3.md#general-quadratic-lattice) | Complete QL1--QL6, full constants, exact kernel and zero index, finite integral closure, polynomial lattice, unit and inverse, finite quotient stabilization and signed index shift. |
| [Complete finding](#synchronized-hankel-indices-whole) | [All nonzero AS and odd-residue extension](../../claims/Yin_C_G0858_v3.md#all-nonzero-as-synchronization) | Repeated dyadic poles, every selected nonrational odd residue, separable rational split branches and common positive multiples. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Final limitations](../../claims/Yin_C_G0858_v3.md#limits) | Selected logarithmic finite-prime sum on the progression, nonzero domain of the all-prime identity, and absence of total-valuation, uniform-period or unrestricted Lehmer conclusions. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Adopted C858 v2 input](../../claims/Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05) | Reuse only original integrality, nonzero AS nonrationality and good odd-prime hypotheses at the actual v2 review/source scope; no transfer of its individual index sets into the new synchronization. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Accepted curve and finite-module inputs](../literature/The26b/Yin_U006.md#accepted-curve-lattice-inputs) | Exact model, Riemann--Roch and Tag 032L statements and applicability, directly checked in the retained editions at the stated nonrecursive source-proof depth. |
| [Complete finding](#synchronized-hankel-indices-whole) | [Han16 comparison](../literature/Han16/Yin_U001.md#shifted-application-and-limit) | Definition 1.1, Theorem 1.1(i), exact shifted polynomial conversions and ultimate-periodicity comparison only; no full source proof, algorithm or synchronization reliance. |
