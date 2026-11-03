---
author: Yin
---

# Integral trace-defect classes and a sharper multiplier cap

The current complete mathematical proof is retained in [C304](../claims/Yin_C_G0304_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
This note determines the integral residue class of a rounded trace defect, strengthens the energy floor used in L G0103, and tests the enlarged codifferent domain.
It does not supply the missing lower bound on an optimized Fourier amplitude.
No new source, computation or novelty claim is involved.

Let alpha be an algebraic unit with monic irreducible P(t)=sum_(i=0)^d p_i t^i, p_d=1, and no unit-circle roots.
Put K=Q(alpha), O=Z[alpha], and write O_K for the full integer ring.
Thus alpha and alpha^(-1) lie in O.
The bilateral shift is (Sx)_j=x_(j+1).
All embeddings in a trace include both members of each complex pair.

<a id="canonical-trace-defect"></a>
## A finite defect with exact trace-dual coefficients

For theta in K, let u_(theta,j) and v_(theta,j) be the stable and expanding traces of theta alpha^j.
Define

    w_(theta,j)=u_(theta,j)  for j>=0,
    w_(theta,j)=-v_(theta,j) for j<0.

Both tails decay exponentially, so w_theta is in l2(Z).
Its defect t_theta=P(S)w_theta is supported on j=-d,...,-1.
For 1<=r<=d, direct splitting of the sum at j+i=0 gives

    (t_theta)_(-r)=Tr(theta b_r(alpha)),
    b_r(t)=sum_(i=r)^d p_i t^(i-r).                      (1)

For example, the full trace recurrence converts -sum_(i<r) p_i Tr(theta alpha^(i-r)) into (1).
The polynomials b_d,...,b_1 have successive degrees 0,...,d-1 and leading coefficient one, so their values are an integral basis of O.

Write theta=f(alpha)/P'(alpha), with the unique rational polynomial f of degree less than d.
Then

    (t_theta)_(-r)=f_(r-1).                             (2)

Here is a direct normalization proof.
Lagrange interpolation at the distinct roots beta of P says

    f(t)=sum_beta f(beta) P(t)/[(t-beta)P'(beta)].

The coefficient of t^(r-1) in P(t)/(t-beta) is b_r(beta).
Taking that coefficient gives exactly (2).
In particular, for the trace-dual lattice

    O^vee={theta in K: Tr(theta O) subset Z},

(1)--(2) prove, without an uninspected codifferent formula,

    O^vee=P'(alpha)^(-1)O.                              (3)

Every algebraic integer theta is in O^vee, since the trace of a product of algebraic integers is integral.
Consequently

    P'(alpha) O_K subset O.                             (4)

The right condition for an integral multiplier is therefore stronger than integrality of the unrounded defect t_theta alone.

<a id="rounded-defect-residue-class"></a>
## The exact residue class and a converse

Let theta be a nonzero member of O_K.
As in L G0103, choose the nearest integer n_j to 2u_(theta,j), and put

    e_(theta,j)=2u_(theta,j)-n_j.

There are no half-integer ties: a tie would make u_(theta,j) a nonintegral rational with denominator four, whereas it is an algebraic integer.
Thus |e_(theta,j)|<1/2.
Trace integrality and exponential tails imply

    e_theta=2w_theta-k

for a finitely supported integer sequence k.
Indeed the two sequences differ integrally at every j, and agree outside a finite interval where both nearest-integer tail choices have stabilized.
It follows that

    z_theta=P(S)e_theta=2t_theta-P(S)k.                  (5)

Since e_theta tends to zero at both ends and every coordinate has absolute value strictly less than 1/2, its supremum also is strictly less than 1/2.

Let Z^(Z) denote the finitely supported integer sequences, and define

    Phi(z)=sum_j z_j alpha^(-j-1) in O.

This is surjective: the standard impulse delta_(-r) maps to alpha^(r-1).
Its kernel is exactly P(S)Z^(Z).
To verify the kernel, identify a finite sequence with the Laurent polynomial sum_j z_j t^(-j-1).
Applying P(S) corresponds to multiplication by P(t).
An integral Laurent polynomial vanishing at alpha is divisible by the monic minimal polynomial over Z; multiplication by a power of t reduces this assertion to ordinary monic polynomial division.
Constant coefficient +/-1 ensures the quotient target is O, with alpha invertible.

Equations (2) and (5) now give the exact arithmetic class

    Phi(z_theta)=2P'(alpha)theta
                     in 2P'(alpha)O_K minus {0}.        (6)

There is also a full converse.
The operator P(S) is invertible on l2(Z), since the continuous function P(e^(it)) has no zeros on the circle; coefficient Fourier transform proves the assertion and its bounded inverse directly.
Given z in Z^(Z), suppose that

    Phi(z) in 2P'(alpha)O_K minus {0},
    ||P(S)^(-1)z||_infinity<1/2.                        (7)

Set theta=Phi(z)/(2P'(alpha)).
The kernel identity makes z-2t_theta equal P(S)k for a finite integer sequence k.
Thus P(S)^(-1)z=2w_theta+k.
At every coordinate this differs integrally from 2u_theta.
The bound in (7) therefore forces it to be precisely the unique nearest-integer error e_theta.
This proves that (6)--(7) characterize all nonzero allowable rounded defects.

In particular an arbitrary short nonzero integer forcing sequence is not automatically an admissible trace defect.
Its class must belong to the specific sublattice 2P'(alpha)O_K, and its unique inverse must lie in the open rounding cube.
Both constraints matter.

<a id="two-unit-defect-energy-floor"></a>
## The defect energy is at least two, for every annihilating multiple

Let R=P Q be any nonzero integer polynomial multiple of P, and write z_R=R(S)e_theta.
The proof of L G0103 shows that z_R is a nonzero finite integer sequence, even if R has additional unit-circle factors: a nonzero polynomial of the bilateral shift has no l2 kernel.
The residue map obeys Phi(Q(S)z)=Q(alpha)Phi(z), so

    Phi(z_R)=2P'(alpha)Q(alpha)theta.                    (8)

The defect z_R cannot be a single signed unit impulse.
Such an impulse has residue +/-alpha^k, of field norm of absolute value one.
If Q(alpha)=0, (8) has residue zero.
Otherwise its norm has absolute value

    2^d |Norm(P'(alpha))| |Norm(Q(alpha)theta)| >=2^d.

All factors after 2^d are nonzero integers, since theta and Q(alpha) are integral.
Both cases contradict a unit residue.
Hence the nonzero integer squared norm cannot equal one, and

    ||z_R||_2^2>=2.                                    (9)

Set Q_R=max_(|z|=1)|R(z)|.
The Fourier multiplier bound ||R(S)e||_2<=Q_R||e||_2 now gives ||e_theta||_2^2>=2/Q_R^2.
Combining this with the exact product c_P(theta)=product_j cos(pi e_(theta,j)) and log cos x<=-x^2/2 yields the strengthened cap

    c_P(theta)<=exp[-pi^2/Q_R^2].                       (10)

The independent sup-norm cap cos(pi/||R||_1) from L G0103 remains valid, so one may take the smaller of the two.
This doubles the exponent in that record's circle-norm cap.
It remains an upper cap on optimized amplitude, not the positive lower amplitude needed for a gap.

<a id="sharp-defect-energy-control"></a>
## The integer energy floor is sharp outside the small-measure core

Take P=t^2-3t+1 and alpha=(3+sqrt5)/2.
Its other root is beta=alpha^(-1), and P'(alpha)=sqrt5.
The polynomial is irreducible because its discriminant is the nonsquare 5, and it is a hyperbolic unit.
For theta_0=1/P'(alpha), the canonical kernel above is

    w_j=-beta^|j|/sqrt5,       P(S)w=delta_(-1).          (11)

This follows directly from its stable and expanding conjugates, or by applying the recurrence, with the only defect at -1.

The finite ring O/(2P'(alpha)O) has alpha as a unit, since alpha^(-1)=3-alpha belongs to O.
Thus some integer n>0 satisfies alpha^n=1 modulo 2P'(alpha)O.
The ring is finite because multiplication by the nonzero element 2P'(alpha) has a nonsingular integral matrix on the rank-two lattice O.
Put

    theta=(1-alpha^n)/(2P'(alpha)) in O minus {0},
    z=delta_(-1)-delta_(-n-1).

Then Phi(z)=1-alpha^n=2P'(alpha)theta, and its inverse is

    e_j=w_j-w_(j+n).

All values of w lie in [-1/sqrt5,0], so |e_j|<=1/sqrt5<1/2.
The converse (7) proves that this is exactly the rounded error of the integral theta, not merely a proposed real sequence.
Therefore ||P(S)e||_2^2=||z||_2^2=2.

This is sharpness of the universal integer energy floor (9), not equality in the cosine estimate (10).
Its Mahler measure alpha>2 places it outside the remaining small-Mahler core.
It neither rules out stronger restrictions on that core nor supplies a near-one family.

<a id="codifferent-domain-positivity-obstruction"></a>
## Enlarging to the codifferent can destroy Fourier positivity

The difference between O_K and O^vee is consequential, even though both give integer traces against O.
Consider

    P(t)=t^4-4t^3-1.

On |t|=1, |-4t^3|=4>|t^4-1|, so Rouche's theorem gives exactly three roots inside the disk and one outside, with no boundary root.
The polynomial is irreducible: a nontrivial monic integral factorization would have one factor all of whose roots lie inside the disk.
Its nonzero integral constant coefficient would have absolute value strictly less than one, which is impossible.
Monic integral factors follow from Gauss's lemma.
Thus any root alpha is an irreducible hyperbolic unit.

Newton's identities, or the defining power recurrence, give

    Tr(1)=4,  Tr(alpha)=4,  Tr(alpha^2)=16,
    Tr(alpha^3)=64.

Consequently theta=1/4 belongs to O^vee, by testing the displayed integral basis of O, while it is not an algebraic integer.
Its stable trace at time zero is three times theta, namely 3/4.
Hence

    cos(2pi u_(theta,0))=cos(3pi/2)=0,
    c_P(theta)=0.                                      (12)

For clarity its canonical defect is integral: P'(alpha)theta=alpha^3-3alpha^2 lies in O, in agreement with (2)--(3).
The failure is not trace integrality; it is the algebraic-integrality step that excluded a quarter-integer stable trace in L G0103.

This is also a large-measure control: P(4)=-1 and P(5)>0, so its unique outside root exceeds four.
No assertion puts it in the near-one class.
The example decisively forbids retaining the positive multiplier-amplitude theorem unchanged when replacing O_K by the trace-dual lattice.

## Consequence and actual review scope

The classification (6)--(7), the improved cap (10), the sharp energy-two control, and the zero-amplitude codifferent example are the new bounded conclusions.
They make the lattice restriction on proposed short defects explicit.
A geometry-of-numbers or short-forcing argument must respect that residue class and the rounding constraint; passing to the entire codifferent does not provide a valid shortcut.

No lower estimate for c_opt sufficient to contradict the cubic entropy-deficit budget has been proved.
The two explicit controls lie outside the small-Mahler core, and are used only at their stated obstruction or sharpness scopes.

## Original contribution and actual checks

The complete original author,contributor,partial and whole checking account is retained in [R543](../audits/reviews/Yin_R_G0543_v1.md#complete-original-l107-checking-account).
Its original inputs,date,mathematical scopes and verdicts remain unchanged,with exact finding-specific relationships.
