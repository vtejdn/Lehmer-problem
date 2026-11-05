---
author: Yin
---
# Synchronized exact Hankel valuation indices from split quadratic polynomial lattices

This fixed result strengthens the actual-valuation topic of [C858 v2](Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05) by proving a common nonzero-index progression for finitely many residue fields.
The coordinating root contributed the divisor proposal, zero-index test and general lattice-stabilization mechanism.
The strategy_full_goal_reassessment contributor developed the complete characteristic-two and source/application arguments; odd_curve_index_check contributed the complete odd-characteristic correspondence and checked the characteristic-two and general lattice developments.
These are proof contributions, not an independent review.
The [selected assessment](#decision-whole-independent-review-2026-11-05) adopts the complete result after the [independent whole finding R1074 v4](../audits/reviews/Yin_R_G1074_v4.md#synchronized-hankel-indices-whole).
The complete earlier versions retain their own arguments, decisions and source/review limits.

<a id="exact-theorem"></a>
## Statement

For a power series f(z)=sum_(n>=0) f_n z^n over a field k, define

    H_h(f)=(f_(i+j+1))_(0<=i,j<h),
    Delta_h(f)=det H_h(f), h>=1,
    Delta_0(f)=1.

The constant term does not enter these matrices.
The reversal variable below is X=1/z; no series is moved by one coefficient to fit a continued-fraction convention.

<a id="divisor-conventions"></a>
**Divisor conventions.**
For the smooth projective model C of a one-variable function field K over a finite field k with full constant field k, a k-divisor is a finite integer sum D=sum_P n_P P of closed points, with deg D=sum_P n_P[k(P):k].
A principal divisor is div(r)=sum_P ord_P(r)P for r in K minus zero, and linear equivalence uses these principal divisors of functions in K.
Define L(D)={0} union {r in K minus zero: div(r)+D>=0} and l(D)=dim_k L(D).
The degree-zero k-divisor class group means degree-zero k-divisors modulo these principal divisors, rather than a geometric class before descent.
All orders at the rational split infinity places below use z=1/X as uniformizer.

**G. General split quadratic germ.**
Let k be finite and K/k(X) a separable quadratic extension in which infinity splits into two k-rational places P_+,P_-.
Let f in K be regular at both places, with distinct residue values c_+,c_- in k, and let a(z)=f(1/z) denote the branch at P_+.
Set M=k[X]+k[X]f, let O be the integral closure of k[X] in K, and choose s in k[X] minus zero with sO subset M subset s^(-1)O.
Let T_0 be the order of [P_+-P_-] in the degree-zero k-divisor class group, and choose epsilon in K minus zero with div(epsilon)=T_0(P_+-P_-).
If s is constant put N=1; otherwise let N be the order of the image of epsilon in the finite unit group (O/s^2 O)^times.
Then with T=NT_0 the dimension of the original shifted Hankel kernel is periodic from index zero, with the zero-dimensional kernel convention at h=0, and

    Delta_(jT)(a)!=0 for all j>=1.                         (QL0)

The classes, unit, lattice inclusions and orders exist by the proof below.
This gives an exact period construction, without asserting that T is minimal, uniformly bounded or a period of the determinant values themselves.
The two explicit divisor specializations next give more direct periods in their own ranges.

**A. Odd characteristic.**
Let k be a finite field of odd characteristic, let U,V in k[z] be squarefree and coprime of the same degree d>=1, and suppose U(0)=V(0)=1.
Let f in k[[z]] be the unique square root of V/U with f(0)=1.
Set

    u(X)=X^d U(1/X), v(X)=X^d V(1/X),
    C: y^2=u(X)v(X),
    P_+: y/u ->1, P_-: y/u ->-1 at X=infinity.

The smooth projective curve C is geometrically integral, has genus d-1, and the two named points are k-rational.
Let D_u be the sum of its finite branch places above the zeros of u, with each place included once, and put

    E_h=(h+d-1)P_--(h-d+1)P_+-D_u, h>=0,
    delta=[P_--P_+].                                      (NI1)

Then deg E_h=d-2, and there are exact k-linear isomorphisms

    ker H_h(f) = L(E_h), h>=1,
    L(E_0)=0.                                             (NI2)

Equality in (NI2) denotes the explicit isomorphism constructed below, not equality of the two underlying sets.
If T is the order of delta in the degree-zero k-divisor class group, then

    dim ker H_(h+T)(f)=dim ker H_h(f), h>=1,
    Delta_(jT)(f)!=0 for every integer j>=1.                (NI3)

The nonzero determinant indices, with index zero included by convention, are thus periodic from zero.
No assertion that the determinant values themselves have period T is needed.

**B. Characteristic two with simple poles.**
Let k be a finite field of characteristic two, let u in k[X] be monic and squarefree of degree b>=1, and let w in k[X] satisfy

    w!=0, deg w<b, gcd(u,w)=1.

Let F be the Laurent series at infinity satisfying F^2+F=w/u and F(infinity)=0, and put f(z)=F(1/z).
Use the curve and its branch places

    C: t^2+u(X)t=u(X)w(X),
    P_+: F=t/u ->0, P_-: F=t/u ->1,
    D_u=sum of the finite branch places over u=0.          (NI4)

This curve is geometrically integral and has a smooth projective model of genus b-1, with the two named k-rational points at infinity.
The conclusions (NI1)--(NI3) hold with d replaced by b, y/u replaced by F, and

    E_h=(h+b-1)P_--(h-b+1)P_+-D_u.

In particular the progression consists of multiples of a period, rather than an unspecified nonempty residue class.
The zero-index proof is essential for this conclusion.
Repeated residual poles and a rational Artin--Schreier class are not included in B.

**C. Simultaneous original-prime consequence.**
Let P and its integer power series G=sqrt(P_4/P_2) be the original power-stable reciprocal unit input of [C858 v2](Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05).
For any finite set S of odd primes not dividing

    2 disc(P_2) disc(P_4) Res(P_2,P_4),

there is an integer L>=1, depending on P and S, such that

    v_p(Delta_(jL)(G))=0 for every p in S and j>=1.         (NI5)

If in addition the original reduced Artin--Schreier class is nonzero, L can be chosen so that simultaneously

    v_2(Delta_(jL)(G))=jL for every j>=1.                   (NI6)

This synchronizes the actual original leading determinants, including repeated dyadic poles in the nonzero class.
Moreover S may contain any odd prime for which the reduction of the original G is nonrational, even if that prime divides the displayed discriminant/resultant product.
The general lattice argument below supplies these two extensions beyond the explicit simple-branch divisor models.
It imposes no uniform bound on L and says nothing about an unselected odd prime with rational residue series, the dyadic zero class, primes that grow with the determinant index, or the valuation on an arbitrary different progression.
In particular it does not resolve the unrestricted Lehmer gap.

<a id="source-scope"></a>
## Exact inputs and source scope

The adopted project input is [C858 v2](Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05), with its [R1074 v3 whole finding](../audits/reviews/Yin_R_G1074_v3.md#actual-hankel-residue-whole): original G=1+2H integrality, the nonzero Artin--Schreier residue class, and good odd-prime nonrationality.
Its individual-prime infinite subsequences do not themselves imply the new synchronization.
Its BNZ22 source limits remain unchanged; the new proof does not use Kronecker's criterion to construct the progression.

[The26b-U006](../audits/literature/The26b/Yin_U006.md#accepted-curve-lattice-inputs) supplies the accepted standard model, Riemann--Roch and finite-integral-closure inputs.
The exact editions are official HTML Tags 0BXX and 0B5B retained on 2026-11-05, and the existing Commutative Algebra chapter revision ed88ff78 compiled 2026-07-14, Lemma 161.8/Tag 032L on printed/PDF p.442.
The inspected source statements, selected displayed proof depth and uninspected duality, normalization and trace-pairing ancestors are retained in that unit.
They are accepted at their checked hypotheses, without claiming a full independent audit of the source proofs.
The finite rational class group, polynomial-lattice stabilization and exact original determinant correspondence are proved here.

[Han16-U001](../audits/literature/Han16/Yin_U001.md#shifted-application-and-limit) identifies the established neighboring result: Theorem 1.1(i) of the author manuscript dated 22 August 2016 gives ultimate periodicity of the relevant shifted determinant values after the stated direct series conversion.
Its statement and exact shift application were inspected, not its full proof or algorithm.
This is attribution and comparison, not a premise of the present proof.
Ultimate periodicity alone does not locate a nonzero residue class through zero or synchronize several primes.
The common multiples here come from the actual zero-index calculation and a unit preserving the whole polynomial lattice.
No originality or priority claim for general quadratic finite-field Hankel periodicity is made.
No theta or sigma identity, generic J-fraction condition, Jacobian height estimate, rolling Draft, numerical experiment or hypothetical near-one example is a mathematical premise.

<a id="exact-pade-map"></a>
## The exact shifted coefficient map

This preliminary calculation holds over every field and for every formal series f.
For h>=1 and a vector beta=(beta_0,...,beta_(h-1)), put

    b(z)=sum_(j=0)^(h-1) beta_j z^(h-1-j).

For 0<=i<h the coefficient identity is

    [z^(h+i)] b(z)f(z)=sum_(j=0)^(h-1) beta_j f_(i+j+1).

Thus beta belongs to ker H_h(f) exactly when, with a the degree-below-h truncation of bf,

    deg a,deg b<=h-1,   bf-a=O(z^(2h)).                   (NI7)

The truncation a is uniquely determined by b.
Reverse both polynomials at the same formal degree h-1:

    A(X)=X^(h-1)a(1/X), B(X)=X^(h-1)b(1/X).

Then (NI7) is equivalent to

    deg A,deg B<=h-1,
    B(X)f(1/X)-A(X)=O(X^(-h-1)).                          (NI8)

This is the entire shift and reversal calculation, including possible vanishing endpoint coefficients.

<a id="odd-proof"></a>
## Odd-characteristic curve and complete correspondence

The reversed polynomials u,v are monic of degree d, squarefree and coprime.
Their product cannot be a rational square even after extending constants to an algebraic closure, because each of its zeros has odd order.
The quadratic function field is therefore geometrically integral.
The affine equation is smooth: at a zero of uv its derivative with respect to X is nonzero, and at every other point the derivative 2y is nonzero.
At infinity set z=1/X and eta=y/X^d.
The equation eta^2=U(z)V(z) has the distinct roots eta=1,-1 at z=0, each with nonzero derivative, giving two smooth k-rational points P_+,P_- and the asserted Laurent branches.
The involution sigma(y)=-y exchanges them.
The variable X has a simple pole at each point, while u,v,y have poles of order d at each.
At a simple zero of u, y is a local parameter and ord(u)=2, ord(y)=1.
Consequently div(u)=2D_u-dP_+-dP_-, and deg D_u=d.

For a vector in the Hankel kernel use (NI8) and define

    R=uA-By=u(A-B f(1/X)).                                (NI9)

This function is regular at all finite points, vanishes at least once along D_u, has pole order at most h+d-1 at P_-, and has order at least h-d+1 at P_+.
These are exactly the conditions R in L(E_h).
The map is k-linear and injective: R=0 would give a rational representation of y/u unless B=0, and then A=0 and the original vector is zero.

For surjectivity fix h>=0 and R in L(E_h), writing uniquely R=C(X)+D(X)y with C,D in k(X).
Both R and sigma R have no finite poles.
Thus C=(R+sigma R)/2 is a base-field rational function with no finite poles and is a polynomial.
Likewise Dy=(R-sigma R)/2 has no finite poles.
A finite pole of D away from a branch point would give a pole of Dy.
At a simple branch point every base-function valuation is even and ord(y)=1, so a pole of D would give ord(Dy)<=-1, again impossible.
Hence D is a polynomial.
The zero condition along D_u makes C vanish at every zero of squarefree u, so u divides C.
Write uniquely R=uA-By with A,B in k[X].

Because h>=0, the two allowed pole orders of R and sigma R are at most h+d-1.
Taking their half-sum and half-difference bounds the pole orders of uA and By by the same number.
A nonzero polynomial of degree r has pole order r at each infinity, so

    deg A<=h-1, deg B<=h-1.                                (NI10)

The P_+ condition on R, divided by u, now gives exactly (NI8).
For h>=1 reversing returns the unique kernel vector in (NI7), proving the claimed isomorphism.
For h=0, (NI10) forces A=B=0, proving L(E_0)=0 directly.
In particular the proof of the zero class does not require extending a generic determinant identity to an exceptional initial index.

<a id="binary-proof"></a>
## Characteristic-two curve and complete correspondence

The rational function w/u has at least one simple pole over an algebraic closure.
If Q in the rational function field has a pole of order r>0, then Q^2+Q has pole order 2r there.
Therefore w/u cannot equal Q^2+Q even after extending constants, and t^2+ut=uw defines a geometrically integral quadratic function field.
Its derivative with respect to t is u, so the extension is separable.
At a zero a of u, the affine equation has t=0 and derivative with respect to X equal to u'(a)w(a), which is nonzero.
Away from these zeros its t-derivative is nonzero, so the entire affine model is smooth.
Writing the equation as u=t^2/(w+t) near a shows ord(u)=2 and ord(t)=1, with residue field unchanged.
This gives the reduced branch divisor D_u and deg D_u=b.

At infinity, w/u has positive z-adic order for z=1/X.
Coefficient recursion uniquely solves F^2+F=w/u with constant term zero, since the linear coefficient of the Artin--Schreier polynomial is one.
The other solution is F+1, giving two smooth k-rational infinity points P_+,P_- exchanged by sigma(t)=t+u.
The function X has a simple pole at each, u has pole order b at each, and t has pole order b at P_- and at most b-1 at P_+.
Consequently div(u)=2D_u-bP_+-bP_-.

For a kernel vector define, with (NI8),

    R=uA-Bt=u(A-BF).                                     (NI11)

The characteristic-two sign is harmless, but the same displayed shift is retained.
The degree bounds give the pole bound at P_-, the approximation gives ord_(P_+)R>=h-b+1, and finite regularity plus the zero along D_u are immediate.
Thus R belongs to L(E_h), and the map is injective by geometric nonrationality of F.

For the reverse direction let h>=0 and R in L(E_h), and write R=C+Dt with C,D in k(X).
The trace R+sigma R=uD is a base function with no finite poles, hence uD is a polynomial.
Away from the zeros of u this already excludes finite poles of D.
At a zero of u it permits at most a simple base-field pole of D, whose valuation on C is -2.
Then Dt would have valuation -1, whereas every base function C has even valuation there; cancellation of this negative odd leading order is impossible.
As R has no finite pole, D cannot have such a pole.
Thus D is a polynomial and C=R-Dt, having no finite poles and lying in k(X), is a polynomial as well.
The zero of R at every point of D_u gives u|C, hence a unique representation R=uA-Bt with A,B in k[X].

Both R and sigma R have their two infinity pole orders at most h+b-1.
Their sum is uB, so deg B<=h-1.
Now Bt has pole order at most h+b-1 at both infinities, and uA=R+Bt has the same bound, giving deg A<=h-1.
Dividing the P_+ condition by u gives (NI8), so the reverse construction is exact.
For h=0 the two degree bounds again give A=B=0 and L(E_0)=0.

<a id="genus-and-period"></a>
## Genus, finite class group and the zero progression

For completeness the genus in both cases can be read from the same regular-function argument, without importing a wild ramification formula.
Write r=d in A and r=b in B, and let N>=r.
A function with poles of order at most N at each infinity and no finite poles has a unique representation C+Dy in A, or C+Dt in B, with

    deg C<=N, deg D<=N-r.

In A this follows by the same half-sum and half-difference argument.
In B trace gives deg D<=N-r and subtraction of Dt gives deg C<=N; the converse is immediate from the pole orders already established.
Therefore

    l(N(P_++P_-))=(N+1)+(N-r+1)=2N-r+2.

For sufficiently large N, Riemann--Roch gives the same dimension as 2N+1-g, so g=r-1.
Geometric integrality and a k-rational point ensure that the full constant field is k, as required in this dimension comparison.
In particular deg E_h=r-2=g-1, though the zero-index proof did not need that numerical identity.

Here is the needed finite-class-group argument at its exact rational-divisor scope.
For every degree-zero divisor D defined over k, the accepted Riemann--Roch inequality gives l(D+gP_+)>=1.
A nonzero k-rational section gives an effective k-divisor A linearly equivalent to D+gP_+, of degree g.
There are only finitely many effective k-divisors of degree g: only finitely many closed points can have degree at most g on a curve of finite type over a finite field, because each lies among the finitely many rational points over one of the extensions of degrees 1 through g.
Only finitely many bounded-degree formal sums of those points occur.
Thus all degree-zero k-divisor classes are represented among the finite set [A-gP_+].
For g=0 the only effective divisor of degree zero is zero, so the class group is trivial.
This is a direct consequence of Riemann--Roch, not an assumption about a theta orbit.

The class delta=[P_--P_+] consequently has finite order T>=1, with linear equivalence over k.
Since E_h=E_0+h(P_--P_+), one has E_(h+T) linearly equivalent to E_h for every h>=0.
Multiplication by a rational function realizing the principal difference gives an isomorphism of the two Riemann--Roch spaces.
The kernel isomorphism and L(E_0)=0 prove (NI3), including every positive multiple of T.
At genus zero this proves Delta_h!=0 at every h>=1; no small-genus exception is omitted.

<a id="original-synchronization"></a>
## Return to the original integer series

At a good odd prime p from C, the reductions of U=P_2 and V=P_4 satisfy every hypothesis of A, as proved at the exact scope of C858 v2.
Reduction of the integral original series G is the constant-one square-root branch, and reduction of its determinant is the determinant of that branch.
Let T_p be the period supplied by A.
For every h divisible by T_p the original integer Delta_h(G) is a p-adic unit.
Taking the least common multiple of finitely many T_p proves (NI5), including nonvanishing of those original determinants.

First consider the simple-pole dyadic specialization of the displayed divisor model.
Write G=1+2H with H in Z[[z]], H(0)=0, and

    Hbar^2+Hbar=r(z)=overline((V-U)/4)/Ubar.

These identities and the actual interpretation of the nonzero class are the accepted C858 v2 input.
When Pbar is squarefree, the reduced denominator of r is squarefree and all its finite poles are simple.
The nonzero class means r is nonzero, so write r=a(z)/q(z) in coprime form with q(0)=1 and a(0)=0.
There are no poles at infinity in z because the original numerator degree is less than the denominator degree, and cancellation preserves this inequality.
Put b=deg q and

    u(X)=X^b q(1/X), w(X)=X^b a(1/X).

Then u is monic squarefree of degree b, gcd(u,w)=1, w!=0 and deg w<b because a(0)=0.
The original series Hbar is precisely the branch in B after X=1/z.
Let T_2 be its period.
For h divisible by T_2, Delta_h(Hbar)!=0 and therefore v_2(Delta_h(H))=0.
Factoring two from each row of the original shifted matrix gives the exact identity

    Delta_h(G)=2^h Delta_h(H).

Choose L as the least common multiple of T_2 and all selected T_p.
Then (NI5) and (NI6) hold simultaneously for every h=jL, without changing the original field, determinant shift or coefficient series.
If S is empty and the dyadic assertion is not selected, take L=1; this empty case makes no extra nonvanishing assertion.

<a id="general-quadratic-lattice"></a>
## General split quadratic extension and a lattice-stabilizing unit

The following proof removes the simple-pole limitation without assigning a nonsmooth plane model the divisor formula from B.
Let k be a finite field, K/k(X) a separable extension of degree two, and suppose the place X=infinity splits into two k-rational places P_+,P_-.
Let f in K be regular at those places with distinct residue values c_+,c_- in k, and let a(z)=f(1/z) be its Laurent expansion at P_+ for z=1/X.
Because f is regular there, a belongs to k[[z]].
The hypotheses imply f is not in k(X), so 1,f is a k(X)-basis of K.
The variable X has a simple pole at each of P_+,P_-: the two distinct rational places exhaust the degree-two extension above infinity, with ramification index one at both.
The rational places ensure that the full constant field is k: any algebraic constant has valuation zero and embeds in the residue field k at either place.
Thus l(0)=1 and the same Riemann--Roch and finite rational class group argument applies to this smooth projective model.

Set

    M=k[X]+k[X]f,
    V_h={R in M: ord_(P_+) R>=h+1,
                 ord_(P_-) R>=1-h}, h>=0.                (QL1)

Every element of M has a unique expression R=A-Bf with A,B in k[X].
For h>=1, the already proved exact coefficient reversal gives an injective map ker H_h(a) into V_h.
Conversely suppose R in V_h is nonzero and let r=max(deg A,deg B)>=0, with a_r,b_r the degree-r coefficients, including zero if that degree is absent.
The positive order required at P_+ forces a_r-b_r c_+=0.
The coefficient a_r-b_r c_- is nonzero, because c_+ differs from c_- and (a_r,b_r) is not (0,0).
Hence R has pole order exactly r at P_-, and the second inequality in (QL1) gives r<=h-1.
This is precisely the polynomial degree bound needed in (NI8); its P_+ condition gives the approximation error there.
Thus

    ker H_h(a) is k-linearly isomorphic to V_h, h>=1,
    V_0=0.                                               (QL2)

For h=0 the same argument would require 0<=r<=-1, proving the second assertion.
There is no positivity, theta-avoidance, genericity or simple finite-pole hypothesis in (QL2).

Let O be the integral closure of k[X] in K.
The cited Tag 032L makes O finite over k[X]; it is torsion free and therefore a free module of rank two over that PID.
Its fraction field is K, since clearing the denominators in a monic algebraic equation makes a nonzero polynomial multiple of f integral.
Thus O and M are full rank-two k[X]-lattices in K.
Express a finite O-basis in the basis 1,f and express 1,f in an O-basis, clearing the finitely many polynomial denominators in both directions.
Multiplying the two resulting nonzero denominator polynomials gives s in k[X] minus zero such that

    sO subset M subset s^(-1)O.                          (QL3)

No multiplicative closure of M is asserted or needed.

The finite degree-zero rational-divisor class group proved above supplies T_0>=1 and epsilon in K minus zero with

    div(epsilon)=T_0(P_+-P_-).                           (QL4)

The sign here is chosen to increase the index h under multiplication.
Both epsilon and its inverse have no poles at any finite place.
They belong to O: in this quadratic separable extension the conjugates also have no finite poles, so the trace and norm of either function are base rational functions without finite poles, hence are polynomials in X.
Their monic quadratic equations give integrality over k[X].
Consequently epsilon is a unit of O.

If s is a nonzero constant, (QL3) gives M=O and multiplication by epsilon already stabilizes M; take N=1.
Otherwise O/s^2 O is a finite ring, as a quotient of a finite k[X]-module by a nonconstant polynomial and with k finite.
The image of epsilon belongs to its finite unit group, so for some N>=1 both epsilon^N and epsilon^(-N) are congruent to 1 modulo s^2 O.
For every m in M, (QL3) gives

    (epsilon^(+/-N)-1)m in s^2 O times s^(-1)O
                              =sO subset M.

Thus epsilon^N M subset M and epsilon^(-N)M subset M; together these give the exact equality epsilon^N M=M.
There is no uncharged assertion that an arbitrary unit preserves an arbitrary polynomial lattice.

Put T=NT_0.
The orders in (QL4) and the exact lattice preservation show that multiplication by epsilon^N gives a k-linear bijection

    V_h -> V_(h+T), h>=0.                                (QL5)

Its inverse is multiplication by epsilon^(-N); both the P_+ and P_- inequalities shift by exactly T.
Combining (QL2), (QL5) and V_0=0 proves

    Delta_(jT)(a)!=0 for every j>=1,                      (QL6)

and periodicity of the kernel dimensions and of the nonzero-index set, including index zero.
The period can be larger than the order of [P_+-P_-], because stabilizing M may require the extra factor N.
The explicit divisor models A and B avoid that extra lattice factor; the general result does not identify their sharper periods with its own period.

<a id="all-nonzero-as-synchronization"></a>
## Repeated dyadic poles and nonrational odd residues

For the original dyadic input with c!=0, C858 v2 proves that Hbar is nonrational and satisfies Hbar^2+Hbar=r(z), with r regular at z=0 and r(0)=0.
Consequently K=F_2(X,Hbar(1/X)) is a separable quadratic extension.
The two formal branches Hbar and Hbar+1 at z=0 are regular and have distinct constants 0,1, so infinity splits into the two rational places required by (QL1).
This remains true with repeated poles at other places; no replacement of r by a simple-pole rational function is made.
Apply (QL6) to Hbar to obtain T_2 and then use Delta_h(G)=2^h Delta_h(H) exactly as before.
This proves (NI6) without the squarefree hypothesis.

At any odd prime p where the original Gbar is nonrational, its equation Gbar^2=Vbar/Ubar defines a separable quadratic extension of F_p(X).
The series branch and its negative have distinct constants 1,-1, so (QL6) supplies T_p even when the finite reduction has repeated zeros or poles.
Nonrationality is required; the good-prime conditions in C858 v2 are a sufficient original-input way to guarantee it.
Take the least common multiple of T_2, when selected, and the finitely many chosen odd-prime periods.
Every positive multiple simultaneously satisfies (NI5)--(NI6), with the same original coefficient series and shifted determinant.
The proof gives an existence period depending on the original input, selected primes and their lattices; no effective or uniform period bound is claimed.

<a id="limits"></a>
## Scope and continuation

For each fixed original input and finite set of good odd primes, the selected finite-prime valuation sum is zero along the common progression.
With any nonzero dyadic Artin--Schreier branch included, it is exactly h log 2 there and hence has zero quadratic coefficient as h tends to infinity through that progression.
This excludes a strictly positive all-late quadratic lower bound built only from that selected collection of places.
It does not exclude a lower bound on a different chosen index set, contributions from odd primes with rational reduction, the dyadic zero branch, a prime set growing with h, or a different matrix.
For every nonzero Delta_h(G), the logarithmically weighted sum sum_p v_p(Delta_h(G)) log p equals log|Delta_h(G)| and is not controlled by the present theorem.
No uniform bound on the period, finite-prime list, divisor order or genus is claimed.
This is a synchronization obstruction for a specified arithmetic implementation, not a positive total-Mahler gap, a counterexample to that gap, or evidence that the whole determinant route is exhausted.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:45 |
| status | proved |
| reason | Adopt the complete split-quadratic theorem G/A/B/C and NI1--NI11/QL0--QL6 after independent R1074 v4. The exact shifted kernel, zero-index calculation and bidirectional polynomial-lattice stabilization give a common positive-multiple progression, including every original nonzero dyadic class with repeated poles and each selected nonrational odd residue. The actual period construction pays both divisor and finite-ring orders; no uniform period, determinant-value period, total finite-place bound or unrestricted Mahler gap follows. Source and earlier-version scopes remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete theorem](#exact-theorem) | Entire G/A/B/C, original coefficient shift, divisor conventions, explicit and general periods, all common multiples and exact original-prime limits. |
| argument | [Complete proof](#exact-pade-map) | All ensuing proof sections: NI7/NI8, both curve correspondences and zero index, genus and finite rational class group, full lattice and inverse stabilization, original synchronization and weighted-prime limitations. |
| dependency | [Adopted original residue input](Yin_C_G0858_v2.md#decision-whole-independent-review-2026-11-05) | Original G=1+2H integrality, nonzero AS nonrationality and good odd reductions only; its separate infinite index sets do not supply synchronization. |
| support | [Curve and finite-module inputs](../audits/literature/The26b/Yin_U006.md#the26b-u006) | Exact retained Tags 0BXX/0B5B and Commutative Algebra Tag 032L model, Riemann--Roch and finite-integral-closure statements, at inspected applicability and stated nonrecursive source-proof depth. |
| support | [Established neighboring periodicity](../audits/literature/Han16/Yin_U001.md#han16-u001) | Theorem 1.1(i) and exact leading-to-shifted conversion for attribution and comparison only, not a synchronization premise or a claim of novelty. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1074_v4.md#synchronized-hankel-indices-whole) | Complete final statement, all explicit/general arguments, exact source reading, parameter domains and zero-index/empty-prime boundaries, without total-valuation or G0001 completion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
