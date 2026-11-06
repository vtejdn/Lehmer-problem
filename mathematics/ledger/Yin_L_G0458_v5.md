---
author: Yin
---

# Gaussian rotations and fixed-curve obstructions for moving square layers

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The bottleneck contributor derived the dyadic rotation, sparse completion, rotation-coprimality and even-power bivariate obstruction, and assembled this version.
The construction contributor derived the prime-template discriminant, squarefreeness certificate, genus-two model and fixed-composition obstruction, and inspected the stated Riemann-Hurwitz interface.
The coordinating contributor checked the rational rotation, supplied the small cyclotomic factors, retained the exact degree-fourteen rotation control in J143, and read the same Riemann-Hurwitz interface.
These are ordinary author-development contributions, not a formal independent review, a new Claim assessment or a counterexample to the Task.

<a id="moving-square-structural-scope"></a>
## The two fixed templates and the question about actual factors

[V4](Yin_L_G0458_v4.md#prime-square-family-scope) retains the complete odd-prime family and the dyadic deletion comparison, with their actual primitive costs and limitations.
This version asks whether rotation, further power substitutions or rational parametrization can produce a moving positive factor or an unbounded number of global factors.
The dyadic output does have a rational rotation factorization with exactly half the original complete measure.
Its sparse completion still excludes whole measures tending to zero, and the rotation does not automatically iterate.
The two bivariate irreducibility arguments below concern fixed curves and their stated base changes.
Neither argument proves irreducibility, bounded factor count or a uniform factor-degree lower bound for the changing diagonal specializations.

<a id="dyadic-rational-rotation"></a>
## An exact rational rotation halves the degree and the complete measure

Retain the [dyadic deletion input](Yin_L_G0458_v4.md#dyadic-deletion-inputs), with n=2^k, k>=2, r=n/2+1,
\[
 C=\frac{z^n-1}{z^2+1},\qquad D=z^{2n}+1,\qquad
 F_k=z^{2r}C^2+D^2.
\]
Put
\[
 B_n=\frac{z^n-1}{z^2-1},\qquad
 Q_n=z^{2n}+1-z^rB_n.
 \tag{R1}
\]
The polynomial B_n is the integer sum 1+z^2+...+z^(n-2), and r is odd.
Since four divides n, C(iz)=-B_n(z) and D(iz)=D(z).
Also i^(2r)=-1.
Consequently
\[
 F_k(iz)=Q_n(z)Q_n(-z),\qquad
 \deg Q_n=2n,\qquad m(F_k)=2m(Q_n).
 \tag{R2}
\]
Both factors in (R2) are actual monic reciprocal integer polynomials with constant coefficient one.
The measure identity includes every root and uses only invariance under the rotations z to iz and z to -z.
It is not a comparison of selected exterior roots.

Multiplication by a zero-measure factor gives the six-term completion
\[
 (z^2-1)Q_n
 =z^{2n+2}-z^{2n}-z^{3n/2+1}+z^{n/2+1}+z^2-1.
 \tag{R3}
\]
The [positivity proof in v4](Yin_L_G0458_v4.md#dyadic-deletion-newton-positivity) and (R2) give m(Q_n)>0 for k>=3.
The accepted [DS17 univariate fixed-support statement](../audits/literature/DS17/Yin_U001.md#ds17-u001), applied to the actual completion (R3), therefore gives
\[
                  \eta_6\le m(Q_n)=m(F_k)/2\le\log4
                  \qquad(k\ge3).
 \tag{R4}
\]
The upper bound is the complete log(16) bound from v4 divided by two.
The positive constant eta_6 is not evaluated.
This is a whole-output floor and does not pass to each factor of Q_n.

There is always a small specified cyclotomic factor.
For odd k>=3, a primitive sixth root zeta has n congruent to two modulo six and r congruent to five modulo six.
Then B_n(zeta)=1 and D(zeta)=zeta^5, so Phi_6 divides Q_n.
For even k>=2, a primitive third root omega has n congruent to one modulo three and r congruent to zero modulo three.
Then B_n(omega)=1/(omega+1)=-omega=D(omega), so Phi_3 divides Q_n.
Thus the corresponding integer quotient has degree 2n-2 and the same positive measure as Q_n when k>=3.
These are supplied cyclotomic factors, not an exhaustive cyclotomic classification or a claim that the quotient is irreducible.
At k=2 one has the exact zero-cost identity Q_4=(z^3-1)(z^5-1).

<a id="dyadic-rotation-coprimality"></a>
## The first rotation does not supply a repeated parity decomposition

The polynomials D and z^rB_n are coprime: their possible nonzero common roots would satisfy z^n=1 and D(z)=2, while D(0)=1.
Adding and subtracting Q_n(z) and Q_n(-z) consequently shows
\[
                         \gcd(Q_n(z),Q_n(-z))=1.
 \tag{R5}
\]
In particular no nonconstant polynomial in z^2 divides Q_n.
Otherwise that polynomial would divide both members of (R5).
This also excludes an entire factor of the form H(z^(2^j)) for j>=1.
It does not exclude an accidental factorization into polynomials lacking that symmetry.

The quarter-turn rotations are disjoint as well.
Suppose gamma were a common root of Q_n(z) and Q_n(iz), and first assume gamma^2 is neither one nor minus one.
The first equation gives D(gamma)=gamma^r B_n(gamma), with both sides nonzero.
Using
\[
 B_n(i\gamma)
   =-\frac{\gamma^2-1}{\gamma^2+1}B_n(\gamma)
\]
in the second equation gives
\[
 1+i^r\frac{\gamma^2-1}{\gamma^2+1}=0,
 \qquad \gamma^2=i^r,\qquad \gamma^4=-1.
\]
For n>=8 this implies gamma^n=1 and B_n(gamma)=0, a contradiction.
For n=4, the required equality D(gamma)=gamma^rB_n(gamma) is also impossible: its two sides have absolute values two and sqrt(2).
At the omitted points, Q_n(i)=Q_n(-i)=2 and Q_n(-1)=2+n/2; Q_n(1)=2-n/2 vanishes only when n=4, and Q_4(i)=2.
Thus no omitted point is a common root.
The same argument with -i gives the other quarter-turn, so the four rotations by powers of i are pairwise coprime.
These statements block the displayed parity or quarter-turn orbit from automatically forcing another factorization of Q_n.
They are not a general exclusion of further arithmetic factorizations.

<a id="dyadic-degree-fourteen-control"></a>
## The finite rotation control is positive and is not Salem

The [rational rotation control in J143](../computations/programs/Yin_J_G0143/readme.md#rational-rotation-control) retains only k=3, so n=8.
Its exact factorization is
\[
 Q_8=(z^2-z+1)R_{14},
\]
\[
 R_{14}=z^{14}+z^{13}-z^{11}-z^{10}-z^9-z^5-z^4-z^3+z+1.
 \tag{R6}
\]
Both multiplicities are one, and the exact symbolic calculation returns R_14 as irreducible and noncyclotomic.
For the degree-twenty-eight factor H already retained in [v4](Yin_L_G0458_v4.md#dyadic-deletion-exact-factor-control), the exact identity is
\[
 H(iz)=R_{14}(z)R_{14}(-z),\qquad
 m(R_{14})=m(H)/2=m(F_3)/2>0.
 \tag{R7}
\]
This is an actual positive integer factor after rotation, not an arbitrarily small sequence or a repeated-halving result.

The same finite control verifies the trace identity
\[
 R_{14}(z)=z^7T(z+z^{-1}),\qquad
 T(x)=x^7+x^6-7x^5-7x^4+13x^3+12x^2-4x-2.
\]
The exact trace-root count is zero below -2, four in (-2,2), one above two and two nonreal roots.
The endpoint values are nonzero and the trace polynomial is squarefree.
Thus R_14 has eight unit-circle roots, two positive real roots and four nonreal roots off the circle.
It is not a Salem polynomial, and its complete measure cannot be replaced by its single positive real exterior-root contribution.
These factorization and root-count facts are finite symbolic-library evidence at J143's recorded author-check scope, without a separate hand irreducibility certificate or formal review.
No numerical Mahler value is asserted.

<a id="dyadic-even-power-bivariate-obstruction"></a>
## Further even power substitutions do not split the rational bivariate template

Retain the fixed dyadic polynomial
\[
 G(z,w)=z^2w(w-1)^2+(z^2+1)^2(w^2+1)^2.
\]
For every integer m>=1 there is a Gaussian factorization
\[
 G(z,t^{2m})=q_+(z,t)q_-(z,t),
\]
\[
 q_\pm=(z^2+1)(t^{4m}+1)
                 \mathbin{\pm}izt^m(t^{2m}-1).
 \tag{B1}
\]
Each q_pm is absolutely irreducible.
Indeed its discriminant as a quadratic in z is
\[
 -H(t^m),\qquad H(t)=4t^8+t^6+6t^4+t^2+4.
 \tag{B2}
\]
The polynomial H is not a square even in C[t].
If H=P^2, then H(-t)=H(t) and deg(P)=4 force P to be even, so P=a t^4+b t^2+c.
The leading and constant coefficients give a^2=c^2=4, while the t^6 and t^2 coefficients give 2ab=2bc=1.
Hence c=a and b=1/(2a), making the t^4 coefficient b^2+2ac=129/16 instead of six.
This contradiction proves nonsquareness.

It follows that H has a root of odd multiplicity, and this root is nonzero because H(0)=4.
The substitution t to t^m is unramified at every preimage of that root, so H(t^m) still has an odd-multiplicity root.
Therefore -H(t^m) is not a square in C(t).
The quadratic coefficients in (B1) have no common factor: t^(4m)+1 and t^m(t^(2m)-1) have no common root.
Gauss's lemma and the quadratic discriminant criterion prove absolute irreducibility of each q_pm in C[z,t].

The two factors are distinct and are exchanged by complex conjugation.
They are not associates: their equal nonzero z^2 coefficients would force the association scalar to be one, inconsistent with the opposite nonzero z coefficients.
Thus they are exactly the two absolute factors in (B1).
Any proper factor over Q would have to be associated to one of them, which cannot be invariant under complex conjugation.
Consequently
\[
                         G(z,t^{2m})
                  \text{ is irreducible in }\mathbb Q[z,t]
                  \quad(m\ge1).
 \tag{B3}
\]
It becomes reducible over Q(i), with exactly the two absolutely irreducible factors in (B1).
In particular repeated dyadic base changes in w do not produce additional rational bivariate factors.
This does not imply irreducibility after setting t to a power of z.
The retained cyclotomic factors and the finite rotation control already demonstrate why that specialization step requires its own argument.

<a id="prime-template-absolute-components"></a>
## The odd-prime template has exactly two absolute Gaussian components

This section concerns the separate [odd-prime template in v4](Yin_L_G0458_v4.md#prime-square-fixed-template).
Put
\[
 U=(z-1)(z^2+1)^2,\qquad V=(z+1)(z^4+1),\qquad
 D=(z^4+1)(z^2+1)^2,
\]
\[
 \mathcal G(z,t)
  =\frac{U^2(t^2+1)^2+V^2(t+1)^4}{2}.
\]
Define Q_+=U(t^2+1)-iV(t+1)^2 and Q_-=conjugate(Q_+).
Then G=Q_+Q_-/2, with G denoting this section's mathcal G.
The two real polynomial bases agree modulo two, so q=Q_+/(1-i) belongs to Z[i][z,t], and mathcal G=q conjugate(q).

As a quadratic in t,
\[
 Q_+=(U-iV)t^2-2iVt+(U-iV).
\]
Put E=U-2iV.
Its discriminant and polynomial resultant with the t-derivative are
\[
 \Delta_t(Q_+)=-4UE=-4(z^2+1)^2(z-1)E,
\]
\[
 \operatorname{Res}_t(Q_+,\partial_tQ_+)=4(U-iV)UE.
 \tag{P1}
\]
The latter is the resultant of the displayed degree-two and degree-one forms; degree-drop special fibers do not alter the generic discriminant calculation.
Also gcd(U,V)=1, so Q_+ is primitive over C[z].

A hand squarefreeness certificate is available for S=-(z-1)E, which has degree six.
Reduce Z[i] modulo the Gaussian prime (2-i), with residue field F_5 and i mapping to two.
Then
\[
 \overline E=U+V=2zR(z),\qquad
 R=z^4+z^2-z+1.
\]
The values of R at zero through four are 1,2,4,3,4, so it has no linear factor.
A repeated irreducible factor would therefore have degree two and force R to be the square of a monic quadratic (z^2+bz+c)^2.
Its zero z^3 coefficient would force b=0, contradicting its nonzero z coefficient.
Thus R is squarefree.
Since R(0)=1 and R(1)=2, the degree-six reduction Sbar=-2z(z-1)R is squarefree, with its degree preserved.
Consequently S is squarefree in characteristic zero.

The discriminant in (P1) has the squarefree part S with six simple zeros, so it is not a square in C(z).
Gauss's lemma proves Q_+ absolutely irreducible, and Q_- is likewise absolutely irreducible.
They are not associates: their nonzero t coefficients would require association scalar minus one, incompatible with their U terms.
These are exactly the two absolute components of mathcal G.
Complex conjugation exchanges them, so mathcal G is irreducible in Q[z,t].

<a id="prime-template-genus-and-parametrization"></a>
## A genus-two model excludes rational parametrization of the fixed component

On a nonempty open set put T=(t-1)/(t+1).
The equation Q_+=0 becomes T^2=(2iV-U)/U.
With Y=(z-1)(z^2+1)T this is
\[
                    Y^2=-(z-1)(U-2iV)=S(z).
 \tag{P2}
\]
Conversely T=Y/[(z-1)(z^2+1)] and t=(1+T)/(1-T), so (P2) is a birational model.
Its smooth projective model is a degree-two cover of the z-line with six simple finite branch points.
Infinity is unramified: with s=1/z and Y'=Ys^3, the equation has nonzero constant term at s=0 and gives two smooth points there over C.

Use the characteristic-zero Riemann-Hurwitz statement for smooth proper curves over C, as specified in the [source interface below](#riemann-hurwitz-source-scope).
It gives
\[
                         2g-2=2(-2)+6,
                         \qquad g=2.
 \tag{P3}
\]
It also excludes a nonconstant map from P^1 to this curve: the right side of the formula would be 2deg(f)+deg(R)>=2, whereas the left side is -2.
Thus no pair of rational functions z(s),t(s), with at least one nonconstant, satisfies Q_+(z(s),t(s)) identically.
This excludes rational and fixed monomial parametrizations of the component.
It does not exclude finite intersections with changing monomial curves.

A narrower fixed-composition check is elementary.
Writing Q_+=0 as t+t^(-1)=W(z) gives
\[
                         W(z)=\frac{2iV}{U-iV}.
\]
This rational map has degree five: numerator and denominator have degree five, their leading coefficients are nonzero, and gcd(U,V)=1 prevents cancellation.
Multiplicativity of rational-map degree excludes W=W_1 composed with W_2 when both degrees are at least two.
This does not classify arbitrary changing compositions of the diagonal specializations.

<a id="prime-template-specialization-limit"></a>
## Fixed-curve irreducibility does not settle the original factor question

For every odd prime p, the actual specializations satisfy
\[
 Q_+(z,z^{2p})=D(z)(A_p(z)-iB_p(z)),
\]
\[
 q(z,z^{2p})=D(z)q_p(z),\qquad
 q_p=(A_p-iB_p)/(1-i).
 \tag{P4}
\]
Thus a fixed cyclotomic multiplier appears in every specialization even though Q_+ is absolutely irreducible.
Neither absolute irreducibility nor genus two proves q_p or H_p irreducible after D is removed.
Neither supplies a positive lower bound on every remaining factor.
Small residue order gives only the local necessary conditions retained in v4.
The prime-template argument produces no actual sublinear global factor.
Its conclusion is a failure of the stated rational-parametrization and fixed-composition mechanisms, not a rejection of the prime family or a bound on all specialized factor degrees.

<a id="riemann-hurwitz-source-scope"></a>
## Source interface and actual checking scope

The Riemann-Hurwitz input is accepted here only for nonconstant morphisms of smooth proper curves over C, with its effective ramification divisor and characteristic-zero local contributions e_x-1.
The actual reference is [The Stacks Project, Section 53.12, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B), specifically the characteristic-zero formula preceding Lemma 53.12.1 and Lemma 53.12.2.
The existing bibliography identity is The26b in [references.bib](../literature/references.bib).
The construction, coordinating and bottleneck contributors read that current official HTML interface on 2026-11-06.
The short surrounding derivation and lemma statements were inspected; their linked foundational proofs were not recursively audited.
This use does not inherit the edition or reading scope of a different chapter PDF retained under the same Stacks bibliography identity.
The degree-six branch calculation and the applications to the two fixed curves are author deductions, not source statements about these polynomial families.

The dyadic argument is elementary apart from the explicitly reused DS17 fixed-support interface and the finite J143 results at their recorded scope.
The J143 rotation computation is limited to k=3; its actual author checks are recorded in that native home.
This version introduces no additional parameter computation or root approximation.
The source reading and author checks are not a formal independent review.
The bottleneck and coordinating contributors each read the complete saved version and checked the displayed algebra, parameter domains and specialization limits.
