---
author: Yin
---

# Limiting cuts and exact coefficient rigidity on the Chebyshev trace grid

<a id="statement"></a>
## The possible limits in a strict positive shell

For \(d\ge3\) put \(B=U_{d-1}(t/2)\) and let \(Q\in\mathbb Z[t]\) be monic of degree \(d\).
Write \(Q/B=t-a+\sum_i r_i/(t-b_i)\), where the \(d-1\) poles \(b_i\) are the distinct roots of \(B\).
In increasing pole order require one nonempty block of strictly negative residues followed by one nonempty block of strictly positive residues, and \(Q(-2)/B(-2)<0\).
Write \(P(z)=z^dQ(z+z^{-1})\) and choose a separator anywhere in the gap between the two blocks.
Suppose \(d\to\infty\) and \(1<M(P)\to1\), with the multiplicative Mahler measure of the whole monic lift.

Every accumulation point of the separators belongs to \(\{-2,-1,0,1,2\}\).
Every coefficientwise limit of the original \(P\)'s is \(H(z+z^{-1})\), with \(H=N/D\) a quotient of coprime monic integer polynomials of equal degree at most three whose roots are traces of roots of unity.
For an interior limiting separator \(c_*\), the poles of \(H\) are simple and contained in \(\{-2,c_*,2\}\).
If \(H\) has no pole at that interior \(c_*\), then \(H(t)=(t-c_*)/(t-2)\).
There are only finitely many possible limit functions.
The assertions hold for real or nonreal exceptional trace roots.

There is also a finite determination result without a Mahler upper bound.
There exists an absolute integer \(L_0\) such that for \(d>L_0\), agreement of the coefficients of \(P\) through degree \(L_0\) with \((1+z^2)/(1-z)\) forces
\[
         Q(t)=t\big(B(t)+U_{d-2}(t/2)\big).
\]
In particular the whole lift then has \(M(P)=1\).
This strengthens the [fourth-root condition on the same prefix](../ledger/Yin_L_G0464_v3.md#fourth-root).
The argument gives no numerical value of \(L_0\).

<a id="moments"></a>
## A fixed weight and the limiting density

Index the grid for the following calculations by \(\theta_i=\pi i/d\), \(b_i=2\cos\theta_i\), \(1\le i\le n=d-1\).
Put \(\nu_i=2\sin^2\theta_i/d\), the residues of \(U_{d-2}(t/2)/B(t)\).
Let \(\nu\) be the semicircle probability law \(\sqrt{4-t^2}\,dt/(2\pi)\).
Its Cauchy transform is \(z\) at \(t=z+z^{-1}\), \(|z|<1\), by sine orthogonality in the \(U_j(t/2)\) expansion.
The discrete \(\nu_i\)'s integrate any fixed polynomial exactly for sufficiently large \(d\), by the same orthogonality on this grid.

Choose the angular midpoint \(c_d\) of the transition gap.
All choices of separator have the same subsequential limits because the mesh tends uniformly to zero.
Take a subsequence on which \(c_d\to c_*\) and \(F_d=zQ/B=P(1-z^2)/(1-z^{2d})\) converges coefficientwise to \(F\).
In a shrinking shell such subsequences exist and \(F\) is a normalized quotient of cyclotomic polynomials by [the integral limit theorem](../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix).
The arguments below up through the integer recurrence also apply whenever these limits are given, all \(\sum_i(b_i-c_d)r_i\) are bounded and this particular \(F\) is cyclotomic rational.
The total is bounded in the stated shell by [the first three trace sums](../ledger/Yin_L_G0462_v2.md#central-sign-test).

Write \(R(z)=F(z)/z=J(t)+zg(t)\) in the quadratic extension \(\mathbb Q(z)/\mathbb Q(t)\).
There is a monic \(A\in\mathbb Z[t]\) with only torsion traces as roots such that \(AJ,Ag\) are integral polynomials.
Indeed take a monic cyclotomic denominator \(E(z)\) for \(F\), allowing constant signs in the numerator.
The symmetric Laurent polynomial \(E(z)E(1/z)\) gives such an \(A\) up to sign, since \(g=(R(z)-R(1/z))/(z-z^{-1})\).
Dividing an antisymmetric integral Laurent polynomial by \(z-z^{-1}\) yields a symmetric integral Laurent polynomial, hence an integral polynomial in \(t\).
The formula \(J=(zR(1/z)-z^{-1}R(z))/(z-z^{-1})\) works with the same denominator.
Set \(w=A^2\) and \(G=wg\in\mathbb Z[t]\).

For every fixed polynomial \(h\), the following moment equality is eventually exact along the subsequence:
\[
            \sum_i h(b_i)w(b_i)r_i=\sum_i h(b_i)G(b_i)\nu_i=\int hG\,d\nu .
\]
Indeed the Laurent coefficients at infinity of \(wQ/B\) eventually agree, to each fixed order, with those of \(wR\), by integrality of the convergent Taylor coefficients of \(F_d\) and the fixed change of variable \(z=t^{-1}+O(t^{-3})\).
The proper part of \(wQ/B\) has residues \(w(b_i)r_i\).
The proper part of \(wR=wJ+zG\) equals \(\int G(b)/(t-b)\,d\nu(b)\), because the difference between \(G(t)/(t-b)\) and \(G(b)/(t-b)\) is polynomial in \(t,b\).

Let \(\mu_i=(b_i-c_d)r_i>0\) and \(X_i=nw(b_i)\mu_i\).
The measures \(n^{-1}\sum_i X_i\delta_{\theta_i}\) converge weakly to \(f(\theta)d\theta/\pi\), where
\[
           f(\theta)=2\sin^2\theta\,(t-c_*)G(t),\qquad t=2\cos\theta .
\]
This follows from the exact moments, uniform bounded total mass and polynomial approximation on the trace interval.
In particular \(f\) is continuous and nonnegative.

<a id="saturation"></a>
## The lower bound for the product and its equality case

Let \(I_d\) consist of the grid indices with \(A(b_i)\ne0\).
Its complement has bounded cardinality.
Writing \(\Delta_d=|\operatorname{Res}(B,Q)|\), the [angular-midpoint product](../ledger/Yin_L_G0464_v2.md#torsion-limits) implies
\[
 \prod_{i=1}^n n\mu_i
     = \left(\frac{n}{2d}\right)^n d^2 |B(c_d)|\Delta_d,\qquad |B(c_d)|\ge1,\quad \Delta_d\ge1 .
\]
Deleting the omitted indices costs at most \(O(\log d)\) in the log product since \(\mu_i\) have bounded sum.
Also \(\prod_{i\in I_d}|A(b_i)|\ge1\) by the nonzero integral resultant of \(A\) with the monic integer polynomial \(B/\gcd(A,B)\).
Hence
\[
           \liminf \frac1n\sum_{i\in I_d}\log X_i\ \ge -\log 2 .
\]
In particular \(f\) is not identically zero, by arithmetic-geometric mean and weak convergence of the total mass.

Suppose \(\int_0^\pi\log f\,d\theta/\pi=-\log2\).
Then
\[
                  \frac1n\sum_i |X_i-f(\theta_i)|\longrightarrow0 .
\]
To see this, at \(i\in I_d\) put \(Y_i=X_i/(f(\theta_i)+\epsilon)\) with fixed \(\epsilon>0\).
Write \(\langle h\rangle=\pi^{-1}\int_0^\pi h(\theta)\,d\theta\).
Since the angles are equidistributed and the weighted measures converge,
\[
 \limsup\frac1n\sum_{I_d}(Y_i-1-\log Y_i)
 \le \left\langle\frac{f}{f+\epsilon}\right\rangle-1+
          \langle\log(f+\epsilon)\rangle+\log2 .
\]
The right side tends to zero as \(\epsilon\downarrow0\).
The inequality \((y-1)^2\le2\max(1,y)(y-1-\log y)\) follows by integrating \(1-1/y\) on either side of one.
Cauchy–Schwarz now controls the mean of \(|Y_i-1|\), since the limiting mean of \(Y_i\) is at most one.
Multiplying by \(f+\epsilon\) and accounting for the boundedly many omitted points proves the convergence.

<a id="integer-recurrence"></a>
## Exact recovery from the cyclotomic phase

Write \(D_0\) for the degree of the numerator of \(F\) minus that of its denominator.
Cyclotomic reversal gives \(F(1/z)=s z^{-D_0}F(z)\), \(s=\pm1\).
If \(D_0\ne2\), then \(\langle\log f\rangle=-\log2\).
Indeed at \(z=e^{-i\theta}\), away from finitely many singular or zero points,
\[
 |g(t)|=\frac{|F(z)|}{2\sin\theta}\,|1-s z^{2-D_0}|,
 \qquad
 f=2\sin^2\theta\,|t-c_*|\,|A(t)|^2\,|g(t)|.
\]
The logarithmic means of \(|F|, |A(t)|, |t-c_*|\) are zero by the unit-circle root formula for Mahler measure and symmetry on the two semicircles.
Here \(z(t-c_*)\) means \(1-c_*z+z^2\), whose roots are on the circle even at the endpoints.
For the nonzero integer \(2-D_0\), the same mean of \(|1-s z^{2-D_0}|\) is zero and \(\langle\log\sin\theta\rangle=-\log2\).
All log singularities are integrable.
When \(D_0=2,s=1\) one has \(g=0\), already excluded by positive mass.

For \(D_0\ne2\), the equality case just proved, \(n/d\to1\) and \(c_d\to c_*\) give
\[
       \sum_i |(b_i-c_d)e_i|\to0,\qquad e_i=w(b_i)r_i-G(b_i)\nu_i .
\]
For \(\xi_i=e^{i\theta_i}\) put \(h_j=\sum_i e_i(\xi_i^j+\xi_i^{-j})\).
These are integers because every trace power sum of the residues of a proper integral rational function with monic denominator is integral, by expansion at infinity.
Here the two terms defining \(e_i\) arise by polynomial multiplication from \(Q/B\) and \(U_{d-2}/B\).
By the exact first moments, \(h_0=h_1=0\) for all sufficiently large \(d\).
For all \(j\ge1\), uniformly in \(j\),
\[
       |h_{j+1}+h_{j-1}-c_d h_j|\le2\sum_i |(b_i-c_d)e_i|<1 .
\]
Induction forces every \(h_j=0\) for those \(d\), even though \(c_d\) need not be rational.
The functions \(\xi^j+\xi^{-j}\) span all polynomials in \(b=\xi+\xi^{-1}\), so distinctness of the nodes gives \(e_i=0\) for every \(i\).
In particular \(\sum_i|w(b_i)r_i|\le\max_{[-2,2]}|G|\).
The [fixed-weight gap](Yin_C_G0880_v2.md#statement) precludes this on a positive shrinking-shell sequence.
The sole remaining phase is \(D_0=2,s=-1\).

<a id="five-cuts"></a>
## The remaining rational functions

In that phase \(P_*=F/(1-z^2)\) is invariant under \(z\mapsto1/z\) and hence belongs to \(\mathbb Q(t)\).
Write \(P_*=H(t)\).
Its value at \(t=\infty\) is one, and its finite zeros and poles are torsion traces by the cyclotomic quotient description.
Thus in lowest terms \(H=N/D\) with monic integer polynomials of equal degree, since the zeros and poles are algebraic integers with their conjugates.
Now \(R(z)=(z^{-1}-z)H(t)\), so \(g=-2H\).
Off the finite zero set of \(A\), the limiting measure \(\sum_i\mu_i\delta_{b_i}\) has density \(-2(t-c_*)H(t)\) relative to \(\nu\), by the weighted convergence above.
Take a weakly converging subsequence of these positive measures, which have uniformly bounded mass.
Finite total mass makes this density locally integrable across all the excluded points, including interval endpoints.
Positivity implies \(H(t)>0\) to the left of an interior \(c_*\) and \(H(t)<0\) to its right, except at finitely many zeros or poles.
An interior pole away from \(c_*\) is therefore impossible by integrability, and a pole at that cut is at most simple.
An endpoint pole is at most simple unless it is itself the cut, when it is at most double, because \(\nu\) has a square-root zero at each endpoint.
It follows that \(\deg D\le3\).
There are finitely many possible monic \(N,D\) of these degrees with all roots in the compact trace interval.

If an interior cut is a pole, it is rational since any other algebraic conjugate of that pole would lie in the interior and could not be a pole.
A conjugate equal to a rational endpoint would force the original pole to be that endpoint.
Thus the interior pole is one of the integers \(-1,0,1\).
If the interior cut is not a pole, \(D\) divides \((t-2)(t+2)\).
A constant denominator cannot supply the sign change.
With degree two both endpoints are poles and every zero of the monic quadratic numerator is strictly interior, by coprimality.
Its two roots counted with multiplicity cannot give just one change of sign between the endpoints.
With degree one the required sign order forces \(D=t-2\) and \(N=t-c_*\), so again \(c_*\in\{-1,0,1\}\).

<a id="central-isolation"></a>
## Finite determination for the central comparison

Suppose the asserted finite determination failed and take \(L_j\to\infty\), \(d_j>L_j\), with a different \(Q\) agreeing through \(L_j\).
Then \(F=(1+z)(1+z^2)\), even without assuming an upper bound on \(M(P)\).
Here \(F/z=t+1+z^2=t+zt\), so \(g(t)=t\) and one can take \(A=1\).
The first coefficients give \(\sum_i r_i=0,\ \sum_i b_i r_i=1,\ a=-1\) for all large \(j\).
Thus \(\sum_i\mu_i=1\) and the preceding moment, product and integer recurrence argument applies with \(D_0=3\).
Take a convergent subsequence of the cuts as before.
It gives \(r_i=b_i\nu_i\) at every grid point, while the integer \(a\) fixes the polynomial part.
These residues and that polynomial part are precisely those of the [neutral comparison](../ledger/Yin_L_G0464_v3.md#central-control), by the recurrence for \(U_j\), valid also at even \(d\) when the reference has a zero residue.
Thus \(Q= t(B+U_{d-2}(t/2))\), a contradiction.
At even \(d\) the required strict signs exclude the neutral polynomial itself.

## Assessment history

### Decision five-cuts

| Field | Value |
| --- | --- |
| date | 2026-11-08T03:12 |
| status | proved |
| reason | A separate whole-proof review checked the product equality, integer recovery, limiting functions and finite determination. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Limiting cuts and finite determination](#statement) | The original strict transition on the full Chebyshev grid, for either exceptional root type. |
| argument | [Weighted moments](#moments) | Convergence of integral polynomial tests and the positive limiting density. |
| argument | [Product equality](#saturation) | The lower geometric mean and its equality consequences with omitted nodes. |
| argument | [Integer recurrence](#integer-recurrence) | Recovery of discrete residues from the angular phase and the weighted error. |
| argument | [Five cuts](#five-cuts) | Real rational descent, sign, integrability and the possible cut limits. |
| argument | [Central determination](#central-isolation) | Uniform finite determination for the specified neutral prefix at any measure. |
| dependency | [Fixed-weight gap](Yin_C_G0880_v2.md#statement) | Exclusion of a positive shrinking sequence after recovery with a fixed integral weight. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1106_v1.md#chebyshev-shell-review) | All assertions and the particular hypotheses used from the earlier grid results. |

## Current assessment

[Selected decision](#decision-five-cuts)
