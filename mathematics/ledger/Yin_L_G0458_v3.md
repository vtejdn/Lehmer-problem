---
author: Yin
---

# Exceptional cyclotomic layers: Gaussian restrictions and actual factor filters

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The source contributor supplied the Gaussian-field boundary and the rotation reduction.
The construction contributor developed the integral halves, conductor parameterization, exact degree-ten control and relative-zero-power extension.
The coordinating contributor proposed the degree-ten input and the factorwise bounded-order filter, checked the assembled arguments and supplied the explicit Lehmer rotation control.
The bottleneck contributor tested the changing three-block Lehmer family and its complete measure and unit costs.
These are author-development contributions and ordinary checks, without independent project review, a new Claim assessment or a resolution of the Task.

<a id="exceptional-cyclotomic-layer-scope"></a>
## The surviving construction question

[V2's low-order reduction](Yin_L_G0458_v2.md#moving-pair-low-order-factor-reduction) confines sufficiently small actual factors of moving zero-measure pairs to A-B, A+B and the specified balanced A^2+B^2 layer.
This version tests those exceptions themselves.
The full outer-exponent bounds and their general signed and zero-root conventions remain in v2.

Two distinctions govern this test.
A fixed-support lower bound on a complete polynomial is not a lower bound on each of its factors.
A Gaussian polynomial norm is not an integer Hermitian square on the circle.
The arguments below retain the actual primitive normalization, factor degrees, field inclusions and all-root measure.

<a id="gaussian-exception-source-boundary"></a>
## The Gaussian exceptional fiber is already self-inversive

Retain the coprime inputs A=eta_A z^r C and B=eta_B z^s D from v2, with min(r,s)=0.
Here eta_A,eta_B are signs, and C,D are monic cyclotomic products.
Consider the exceptional branch epsilon=C(0)/D(0)=-1 and Delta=2(r-s)+deg C-deg D=0.
Put
\[
 h=2r+\deg C=2s+\deg D,\qquad q=A-iB.
\]
Then q has actual degree h and nonzero constant coefficient.
If r or s is positive, the other input has degree h and supplies its leading coefficient.
If r=s=0, the leading coefficient is eta_A-i eta_B, which is nonzero.
The constant coefficient is likewise nonzero in every case.

The cyclotomic reversal identities give
\[
 z^h A(1/z)=C(0)A(z),\qquad
 z^h B(1/z)=D(0)B(z)=-C(0)B(z).
\]
Consequently, with coefficientwise conjugation,
\[
 q^\dagger(z)=z^h\overline q(1/z)=C(0)q.              \tag{G1}
\]
This is self-inversiveness at the actual degree.
Thus the whole Gaussian fiber fails the non-self-inversive hypothesis of [Sch75 Corollary 1'](../audits/literature/Sch75/Yin_U001.md#sch75-monic-integral-gap).

There is a precise factorwise statement.
Let f be a primitive irreducible positive-measure rational factor of A^2+B^2 with m(f)<log 2.
Its leading and constant coefficients have absolute value one; choose its monic sign.
Choose a root beta with R(beta)=i, replacing beta by its complex conjugate if necessary, where R=A/B.
The inputs are coprime, so B(beta) is nonzero.
Therefore K=Q(i) is a subfield of L=Q(beta).
Let p be the monic K-minimal polynomial of beta.
It belongs to Z[i][z], since beta is integral.
The polynomial p bar(p) is monic rational integral, vanishes at beta, and has degree 2[L:K]=[L:Q]=deg f.
Hence
\[
              f=p\overline p,\qquad
              m(f)=m(p)+m(\overline p).              \tag{G2}
\]

In this particular fiber, f is reciprocal if and only if p is self-inversive.
Indeed, ordinary inversion exchanges the two fibers R=i and R=-i.
If f is reciprocal, beta^(-1) is a root of f and belongs to the opposite fiber, hence to bar(p).
The irreducible polynomials p* and bar(p) are consequently proportional.
Conjugating this identity makes p self-inversive.
Conversely, p^dagger=c p implies f*=|c|^2 f=f, because self-inversiveness forces |c|=1.

For a non-self-inversive p, the two-embedding Sch75 inequality gives
\[
               m(f)\ge\log\varphi,\qquad
               \varphi=(1+\sqrt5)/2.                 \tag{G3}
\]
Factors with m(f)>=log 2 already satisfy this bound.
Thus every nonreciprocal positive factor of this exceptional layer costs at least log varphi.
The reciprocal factors are precisely the relative self-inversive case on which this source supplies no bound.
No conclusion here extends Sch75 to self-inversive polynomials.

<a id="gaussian-norm-counterexample-equivalence"></a>
## Gaussian integrality alone retains the original small-measure difficulty

The multiplicative parity transform is already retained in [L133 v17, equation (17)](Yin_L_G0133_v17.md#degree-preserving-positive-parity-descent).
For P(z)=U(z^2)+zV(z^2), the polynomial T(x)=U(x)^2-xV(x)^2 satisfies T(z^2)=P(z)P(-z) and m(T)=2m(P).
This is distinct from that material's positive-symbol construction.
The following reduction supplies its formerly assumed non-even input and records the field consequences.

Suppose there exists an unrestricted Lehmer counterexample sequence of primitive irreducible integer polynomials with positive total measure tending to zero.
This irreducible formulation loses no generality: from a positive-measure integer polynomial choose a positive-measure irreducible factor, whose measure is no larger.
Discard finitely many terms so that the measures are below both log 2 and the accepted Smyth nonreciprocal gap used in [v2](Yin_L_G0458_v2.md#moving-pair-effective-phase).
The polynomials are then monic units and reciprocal.
Their constant coefficients are one: constant coefficient minus one in the reciprocal identity would force the root 1.
Their degrees are even, since an odd-degree reciprocal polynomial has the root -1.

Whenever such a polynomial is even, write P(z)=Q(z^2).
The polynomial Q is monic integral with constant one and is irreducible, because any factorization of Q would factor P.
Its reciprocity follows by comparing the reciprocal identity after substitution.
Moreover m(Q)=m(P)>0: each root gamma of Q contributes two square roots whose combined exterior logarithmic contribution is log^+|gamma|.
Repeatedly perform this operation until the polynomial is not even.
The process terminates because the degree decreases.
Write P_j for the resulting sequence.
It still consists of monic, irreducible, reciprocal integer polynomials with constant one and positive m(P_j) tending to zero.

For any root alpha of a non-even P_j,
\[
                       \mathbb Q(\alpha)
                         =\mathbb Q(\alpha^2).        \tag{G4}
\]
The extension has degree at most two.
If its degree were two, the nontrivial automorphism would send alpha to -alpha.
Thus -alpha would be a rational conjugate, and irreducibility would force P_j(-z)=P_j(z), a contradiction.

Form the Gaussian norm
\[
       G_j(z)=P_j(iz)P_j(-iz)=T_j(-z^2),\qquad
       m(G_j)=2m(P_j)>0.                              \tag{G5}
\]
It is monic integral with constant one.
Equivalently it is the norm of the monic Gaussian integer polynomial i^(-deg P_j)P_j(iz).
Rotation and the retained parity identity give exactly the full measure in (G5).

Every root beta of G_j has the form beta=+/-i alpha for a root alpha of P_j.
Equation (G4) therefore gives
\[
 \mathbb Q(\alpha)=\mathbb Q(\alpha^2)
 =\mathbb Q(-\beta^2)\subset\mathbb Q(\beta),
 \qquad i\in\mathbb Q(\beta).                        \tag{G6}
\]
This holds for every actual factor.
Also G_j has no real root.
Otherwise alpha would be purely imaginary, so -alpha=bar(alpha) would be another root of the rational polynomial P_j, again forcing it to be even.

Choose any positive-measure irreducible factor f_j of G_j.
Such a factor exists, and multiplicativity with all multiplicities retained gives
\[
                        0<m(f_j)\le2m(P_j)\to0.      \tag{G7}
\]
For a root beta of f_j, let p_j be its monic minimal polynomial over Q(i).
Equation (G6) and the degree argument in (G2) give f_j=p_j bar(p_j).
If p_j were not self-inversive, Sch75 would give m(f_j)>=log varphi.
Thus all sufficiently late p_j are self-inversive.
Separately, the ordinary Smyth gap forces all sufficiently late f_j to be reciprocal.
The action of inversion on i is not inferred merely from reciprocity.

Consequently an unrestricted counterexample sequence exists if and only if one exists among monic irreducible reciprocal units with no real conjugates, whose root fields contain Q(i), and whose Q(i)-minimal polynomials are self-inversive.
The reverse implication is inclusion in the original domain.
Gaussian integrality and these field conditions alone retain the original small-measure difficulty.

This construction does not show that both real and imaginary parts of P_j(iz) have zero measure.
In parity notation G_j=U_j(-z^2)^2+z^2 V_j(-z^2)^2, but neither summand base is thereby a cyclotomic product.
Thus it is not a reduction to the two-zero-measure-input construction.

For the [fixed Lehmer seed](Yin_L_G0458_v2.md#moving-pair-lehmer-exception-control), direct expansion gives
\[
 P_L(iz)=A_L+iB_L,\quad
 A_L=(1-z^4)(1+z^6),\quad
 B_L=z(z^8+z^6-z^4+z^2+1).
\]
The first base has zero measure; the second does not.
Writing t=z^2+z^(-2) gives z^(-4)(B_L/z)=t^2+t-3.
Its roots are (-1+sqrt(13))/2 in (-2,2) and (-1-sqrt(13))/2<-2.
The latter produces two exterior z-roots and two interior z-roots; the former produces four circle roots.
Including the zero root and every exterior contribution,
\[
 m(B_L)=\log\left(
       \frac{1+\sqrt{13}+\sqrt{2\sqrt{13}-2}}4
                         \right)>0.                 \tag{G8}
\]
Even this explicit Gaussian rotation therefore fails the required two-zero-measure-input condition.

<a id="cyclotomic-square-content-and-reversal"></a>
## Integral halves and the actual circle expression

Now let A and B be coprime monic cyclotomic products of the same degree d_0 with opposite reciprocal signs.
Write A(0)=s and B(0)=-s, where s is either sign.
The leading coefficient of A^2+B^2 is two, so its content is either one or two.
In characteristic two its reduction is (bar A+bar B)^2.
Consequently
\[
 \operatorname{cont}(A^2+B^2)=2
       \quad\Longleftrightarrow\quad \overline A=\overline B.
                                                               \tag{S1}
\]
In this case put
\[
 X=(A+B)/2,\quad Y=(A-B)/2,\quad
 H=(A^2+B^2)/2=X^2+Y^2.
\]
Then X,Y are integral, X is monic of degree d_0 with X(0)=0, and Y has smaller degree with Y(0)=s.
For the fixed-length reversal U^{*d_0}=z^{d_0}U(1/z),
\[
 X^{*d_0}=sY,\qquad Y^{*d_0}=sX.                      \tag{S2}
\]
The second identity uses padding and is not reversal at the actual degree of Y.
If t=ord_0 X, then deg Y=d_0-t.

The polynomial H is monic reciprocal of degree 2d_0 with constant coefficient one.
Also G=X+iY is monic in Z[i][z], has constant coefficient is, and satisfies H=G bar(G) and G*=is bar(G), with ordinary reversal of actual degree d_0.
This is a polynomial norm, not a Hermitian square on the circle.
Indeed, for |z|=1,
\[
 Y(z)=s z^{d_0}\overline{X(z)},\qquad
 H(z)=2z^{d_0}\operatorname{Re}
                         \left(z^{-d_0}X(z)^2\right). \tag{S3}
\]
No nonnegative circle integrand follows from X^2+Y^2.

<a id="cyclotomic-square-conductor-parameterization"></a>
## Two weighted partitions give the content-two inputs

For odd m and k>=0, let a_(m,k),b_(m,k) be the multiplicities of Phi_(2^k m) in A,B.
Set w_k=phi(2^k), so w_0=w_1=1 and w_k=2^(k-1) for k>=2.
Reduction gives
\[
              \overline{\Phi_{2^km}}
                 =\overline{\Phi_m}^{\,w_k}.
\]
For k>=1 this follows from the quotient identity for Phi_(2^k m) and Frobenius in characteristic two; k=0 is immediate.
For odd m, the reduction of z^m-1 is squarefree.
Its cyclotomic product formula shows that bar(Phi_m) has roots of exact order m.
Thus these reductions are pairwise coprime for distinct odd m, and
\[
 \overline A=\overline B
 \quad\Longleftrightarrow\quad
 \sum_k w_k a_{m,k}=\sum_k w_k b_{m,k}
                     \quad\hbox{for every odd }m.    \tag{S4}
\]
This supplies actual integral inputs through two finite weighted partitions at each odd conductor.
Coprimality means that the multiplicities at any one cyclotomic index are not both positive.
The opposite reciprocal-sign condition is a_(1,0)-b_(1,0) congruent to one modulo two, since Phi_1 is the only cyclotomic polynomial with constant coefficient minus one.

<a id="cyclotomic-square-factorwise-residue-filter"></a>
## The primitive output preserves a factorwise bounded-order obstruction

Let M be the odd least common multiple of the conductors' odd parts.
Since B=A+2C for an integer polynomial C,
\[
 H=A^2+2AC+2C^2,\qquad \overline H=\overline A^{\,2}. \tag{S5}
\]
Let f be any actual positive-measure irreducible factor of H, with original degree e and root beta.
It is a monic unit polynomial because H is monic with constant coefficient one.
Every root of bar(f) has order dividing M.
The polynomial z^M-1 is squarefree over F_2.

Choose Q=2^ceil(log_2 e), so e<=Q<2e.
Every multiplicity in bar(f) is at most e.
Therefore
\[
 \overline f\mid(z^M-1)^Q=z^{MQ}-1,\qquad
 (\beta^{MQ}-1)/2\in\mathbb Z[\beta]
                           \subset O_{\mathbb Q(\beta)}.        \tag{S6}
\]
The integral half-value follows by lifting the quotient polynomial in the displayed binary divisibility and evaluating at beta.

Apply [C864 v2's original binomial norm return](../claims/Yin_C_G0864_v2.md#original-binomial-norm-return), equations (BP13)--(BP14).
It retains the original degree and full-ring integrality, without requiring powered-degree preservation.
For clarity, write L=MQ and v=(beta^L-1)/2.
Nontorsion makes v and v+1 nonzero, and
\[
 (\beta^{2L}-1)/4=v(v+1)\in O_{\mathbb Q(\beta)}\setminus\{0\}.
\]
Taking the norm and then using all e original conjugates gives
\[
 4^e\le\left|N_{\mathbb Q(\beta)/\mathbb Q}(\beta^{2L}-1)\right|
       <2^e\exp(2L\,m(f)).
\]
The strict upper bound uses a conjugate off the circle.
Hence
\[
             m(f)>\frac{e\log2}{2MQ}>
                              \frac{\log2}{4M}.       \tag{S7}
\]
The norm of beta^L-1 alone would not give this positive bound; the amplification to 2L is essential.

Thus every content-two input pair with bounded odd conductor least common multiple has a uniform bound for each positive factor, including proper factors.
Pure dyadic cyclotomic inputs have M=1 and satisfy m(f)>log2/4.
The degree selecting Q is the degree of f, not the degree of H.
The general [bounded-residue principle in C491](../claims/Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape), equations (12)--(15), already retains this type of obstruction.
The direct dependency here is the accepted C864 norm argument; the new construction-specific fact is (S5).
M can be replaced by the least common multiple of the actual odd orders in bar(f).
A positive-to-zero sequence in this equal-degree content-two class must make those actual orders unbounded.

<a id="cyclotomic-square-irreducible-control"></a>
## An exact noncyclotomic integral control

Take
\[
 A=(z-1)(z^4+1),\qquad B=(z+1)(z^2+1)^2.
\]
These are coprime, have degree five and opposite reciprocal signs.
The weights in (S4) are 1+4=1+2(2)=5.
Their exact integral halves are
\[
 X=z^5+z^3+z^2+z,\qquad Y=-z^4-z^3-z^2-1.
\]
The complete primitive output is
\[
 H=z^{10}+3z^8+4z^7+6z^6+4z^5+
                    6z^4+4z^3+3z^2+1.             \tag{S8}
\]
It is irreducible.
Indeed H=z^5 Q_0(z+z^(-1)), where
\[
 Q_0(y)=y^5-2y^3+4y^2+2y-4.
\]
Modulo three, Q_0 has values 2,1,2 at 0,1,2.
Its remainders modulo the three monic irreducible quadratics y^2+1, y^2+y+2 and y^2+2y+2 are respectively 2y+1, 2y+2 and y+1.
A reducible degree-five polynomial has a factor of degree at most two, so this proves irreducibility of Q_0.

For any root beta of H, its trace generates a degree-five subfield.
Also A(beta)/B(beta)=+/-i, with nonzero denominator by coprimality.
Thus Q(beta) contains both a degree-five field and Q(i).
Its degree is divisible by ten and at most ten, proving irreducibility of H.

Its binary reduction is (z+1)^10.
If H were cyclotomic, the conductor formula above would force its conductor to be a power of two, whose cyclotomic degree cannot equal ten.
Thus H is noncyclotomic and has positive measure.
For its complete degree-ten factor, Q=16 in (S6), giving
\[
                         m(H)>5\log2/16.             \tag{S9}
\]
This exact control shows that the integral sum-of-squares structure does not force zero measure.
The algebraic expansion, finite-field divisions and degree argument are displayed in full; no numerical root computation or native scan is used.

<a id="cyclotomic-square-relative-zero-powers"></a>
## Relative zero-root powers have a different remaining parameter

For pure dyadic C,D, suppose
\[
 A=z^r C,\quad B=D,\quad r>0,\quad
 c=\deg C,\quad\deg D=c+2r,
\]
with opposite reciprocal signs and coprimality as before.
Then F=A^2+B^2 itself is monic of degree 2deg D with constant coefficient one; no content is removed.
The binary reduction is
\[
 \overline F=(z+1)^{2c}
                   [z^r+(z+1)^{2r}]^2.
\]
If r=2^t u with u odd, put E_u=z^u+(z+1)^(2u) in F_2[z].
Frobenius gives
\[
 z^r+(z+1)^{2r}=E_u^{\,2^t},\qquad
 E_u(0)=E_u(1)=1,\quad E_u'=z^{u-1}.                 \tag{S10}
\]
Consequently E_u is squarefree and has no zero root.
Let M_u be the odd least common multiple of its root orders.
This is finite for fixed u, since the roots lie in finite extensions of F_2.
All roots of bar(F) have order dividing M_u, including the possible root one from the first factor.
The same original-factor-degree argument proves
\[
                         m(f)>\log2/(4M_u)           \tag{S11}
\]
for every positive factor f of F.
For u=1, E_1=z^2+z+1 and M_1=3, giving log2/12.

Thus fixed odd part of r is excluded in this relative-power family.
The equal-degree conclusion about growing odd conductors must not be transferred unchanged to inputs with relative zero-root powers.
No small-factor exclusion is claimed here for arbitrary content-one equal-degree pairs or for unbounded actual binary root orders.

<a id="changing-three-block-lehmer-family"></a>
## Changing the three Lehmer blocks preserves bounded whole cost, not factor growth

A direct varying family through the Lehmer seed is
\[
 P_a=(z+1)(z^a-1)(z^{2a}-1)-z^{(3a+1)/2},
                         \qquad a\ge1\hbox{ odd}.    \tag{L1}
\]
It is monic reciprocal with constant one and degree 3a+1.
Also P_a(1)=-1, while P_a(x) tends to positive infinity as x tends to positive infinity.
There is therefore an actual real root greater than one, and m(P_a)>0.

The exact expansion is
\[
 P_a=z^{3a+1}+z^{3a}-z^{2a+1}-z^{2a}
           -z^{a+1}-z^a+z+1-z^{(3a+1)/2}.
\]
After any collisions it has at most nine terms and coefficient absolute sum at most nine.
The accepted [DS17 univariate fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) and the elementary coefficient-sum upper bound give
\[
                         \eta_9\le m(P_a)\le\log9.  \tag{L2}
\]
The positive constant eta_9 is not evaluated.
This rules out whole-output measures tending to zero in this family, but is not a lower bound on its individual factors.

The exact controls are P_3=P_L and
\[
                  P_1=(z^2-z-1)(z^2+z-1).
\]
They supply no growth mechanism for the number of positive factors as a varies.
No such growth or uniform individual-factor floor is established here.

For any actual factor root beta, the defining identity gives
\[
 (\beta+1)(\beta^a-1)(\beta^{2a}-1)=\beta^{(3a+1)/2}. \tag{L3}
\]
Every factor root is an algebraic unit.
All three factors on the left are algebraic integers and their product is a unit, so each is a unit.
Factoring beta^(2a)-1 and beta^a-1 shows that beta^a+1 and beta-1 are units too.
The endpoint identities also show that every monic integer factor of P_a has unit values at both endpoints, since P_a(1)=-1 and P_a(-1)=-(-1)^((3a+1)/2).
These are unit conditions; they do not give an integral binary half-value or an additional normalized joint Taylor relation.

More generally, a product of r blocks z^n+/-1 with positive exponents has coefficient absolute sum at most 2^r.
Subtracting a central monomial gives an upper bound log(2^r+1) on the complete measure.
Its growth as an upper bound does not prove actual measure growth.
Repeating an entire fixed block group with a synchronized center returns to the outer-power problem already treated in v2.
Independent changes of block orders and block count remain outside the present exclusions.

<a id="exceptional-layer-next-construction"></a>
## Remaining construction and the small positive allocation

The square branch now has an explicit input generator and a factorwise rejection test.
An equal-degree content-two candidate sequence with positive measures tending to zero must escape bounded actual odd orders in its binary reduction.
With relative zero-root powers and pure dyadic input factors, the odd part of the relative shift must grow, or the candidate is already covered by (S11).
Neither necessary condition supplies decreasing measure or global factor production.

The Gaussian norm reduction explains why removing only real roots or imposing Q(i)-integrality does not solve the remaining question.
The additional two-cyclotomic-input condition must be used, with full primitive cost.
The three-block family has bounded complete cost and positive output, but its individual-factor construction remains missing.
The earlier [mixed-map relative-norm-one class](Yin_L_G0450_v6.md#moving-map-restricted-next-question) remains an unresolved comparison.

For the complementary S9 effort, the binary half-values in (S6) and (S11) are already paid scalar obstructions on excluded candidate classes.
They are not new divisibility of normalized joint Taylor minors.
Likewise (L3) supplies units rather than an integral half-value.
No new admissible original polynomial with an unexplained residual rank loss has been supplied.
Thus this round gives no reason to enlarge the retained small S9 allocation or repeat its covered finite control.

All conclusions are symbolic author work and applications of already inspected source statements.
No new source acquisition, native mathematical computation or formal review is part of this version.
The source contributor read and checked the saved Gaussian and rotation arguments (G1)--(G8), including the field degrees and the full measure in (G8).
The construction contributor read the complete saved account and checked (S1)--(S11), including the conductor classification, exact irreducible control and relative-zero-power boundary.
The bottleneck contributor read the saved three-block argument and continuation scope, checked (L1)--(L3) and the used source boundary, and additionally checked (S1)--(S3) and (S5)--(S7).
The coordinating contributor read the complete saved account and corrected the two scope phrasings identified in that check.
These are ordinary author checks, not independent review.
