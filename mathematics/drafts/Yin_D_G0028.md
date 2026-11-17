---
author: Yin
---

# Chamber norms and balanced unit orbits in a fixed Salem inverse fiber

This is continuing author-side work for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
The fixed Salem polynomial below is supplied as input.
The construction refines the choice of its Pisot inverse; it does not construct a new Salem polynomial.
The arguments have been checked during development, without an independent review or a fixed mathematical assessment.

<a id="setup"></a>
## The fixed trace order and the inverse chamber

Fix an arbitrary Salem minimal polynomial
\[
 P(z)=z^mQ(z+z^{-1}),\qquad \deg P=2m\ge4.
\]
Write its distinct trace roots as
\[
 T=\sigma+\sigma^{-1}>2,\qquad -2<x_1<\cdots<x_h<2,
 \qquad h=m-1,
\]
and put
\[
 E=T-2,\qquad H(X)=\frac{Q(X)}{X-T},\qquad
 Z=H(T)=Q'(T)>0,
 \qquad D_H=\operatorname{disc}H>0,
 \qquad D_Q=\operatorname{disc}Q=Z^2D_H.
\]
For \(h=1\), the discriminant of the monic linear polynomial \(H\) is one.
Also set
\[
                     \mathfrak a=|H(-2)|=\prod_i(2+x_i)>0.
\]

The trace field \(F=\mathbb Q(T)\) is totally real of degree \(m\).
Indeed the monic integral \(Q\) has degree \(m\), while the quadratic relation for \(\sigma\) over \(F\) and \([\mathbb Q(\sigma):\mathbb Q]=2m\) force \([F:\mathbb Q]=m\).
In particular
\[
                          \mathcal O=\mathbb Z[T]
\]
is a full order in \(F\), with \(\mathbb Z\)-basis \(1,T,\ldots,T^h\).
Each element \(\nu\in\mathcal O\) has a unique representative \(R\in\mathbb Z[X]\) of degree at most \(h\).
Its embeddings are \(R(T),R(x_1),\ldots,R(x_h)\).

Define the strict sign chamber
\[
 \mathcal C=\{R(T)\in\mathcal O:
       R(T)<0,\quad R(x_i)H'(x_i)<0\text{ for every }i\}.
                                                               \tag{1}
\]
It is nonempty.
For example reduce \((2-X)Q'(X)\) modulo the monic \(Q\), and call the resulting integer polynomial \(R_0\).
At \(T\) its value is \((2-T)Q'(T)<0\), while
\[
 R_0(x_i)=(2-x_i)(x_i-T)H'(x_i)
\]
has the required opposite sign to \(H'(x_i)\).

Consequently the positive integer
\[
              \mu(P)=\min_{\nu\in\mathcal C}
                        |N_{F/\mathbb Q}(\nu)|                     \tag{2}
\]
exists.
The displayed element also gives
\[
                  1\le\mu(P)\le |P(1)|D_Q.                         \tag{3}
\]
For the upper bound use the product of \((2-y)Q'(y)\) over all roots \(y\) of \(Q\), together with \(Q(2)=P(1)\) and the discriminant formula.
The equality \(\mu(P)=1\) holds precisely when this chamber contains an order unit.

<a id="simplex"></a>
## Exact quantities for an actual inverse

The [full inverse simplex](../claims/Yin_C_G0345_v4.md#simplex) writes every Pisot inverse of constant \(q\ge2\) as
\[
 f=P+(z-1)z^{m-1}R(z+z^{-1}),\qquad
 R=(1-q)H-\sum_{i=1}^h b_i\frac{H}{X-x_i},                         \tag{4}
\]
where \(R\in\mathbb Z[X]\) and
\[
 b_i=-\frac{R(x_i)}{H'(x_i)}>0,\qquad
 c_i=\frac{b_i}{2+x_i}>0,\qquad
                         \sum_i c_i<q+T/2.                         \tag{5}
\]
These inequalities are necessary and sufficient for a Pisot minimal polynomial of exactly degree \(2m\) returning \(zf+f^*=(z+1)P\).
Equation (4) gives
\[
 |R(T)|=Z\left(q-1+\sum_i\frac{b_i}{T-x_i}\right).                  \tag{6}
\]
Thus every actual inverse supplies an element of \(\mathcal C\).

The [reciprocal-resultant calculation](../claims/Yin_C_G0345_v296.md#fiber) gives
\[
 \begin{gathered}
 n:=|N_{F/\mathbb Q}(R(T))|
      =|R(T)|D_H\prod_i b_i,\\
 f(-1)=\mathfrak a\left(2q+T-2\sum_i c_i\right)>0,\\
 \mathcal R(f):=|\operatorname{Res}(f,f^*)|
                =f(-1)|P(1)|n^2.                                 \tag{7}
 \end{gathered}
\]
For the first identity, \(R(x_i)=-b_iH'(x_i)\) and \(\prod_i|H'(x_i)|=D_H\).
For the second, substitute \(-2\) into (4) and use \(H(-2)=(-1)^h\mathfrak a\).
For the third, evaluation of \(zf+f^*=(z+1)P\) on the roots of the monic \(f\) gives
\(\operatorname{Res}(f,f^*)=f(-1)\operatorname{Res}(f,P)\).
Evaluation of (4) on the roots of \(P\), whose trace roots each occur twice, gives
\(\operatorname{Res}(P,f)=P(1)\operatorname{Res}(Q,R)^2\).
Both polynomials have even degree, so the two orders of the last resultant agree, and \(\operatorname{Res}(Q,R)=N_{F/\mathbb Q}(R(T))\).
Here \(P(1)=(2-T)H(2)<0\), which explains the absolute value in (7).

Let \(\theta>q\) be the Pisot root, \(\delta=\theta-q\), and \(X_\theta=\theta+\theta^{-1}\).
The [exact excess identity](../claims/Yin_C_G0345_v4.md#second-order) is
\[
 \delta=\frac{E\theta}{\theta-1}+\eta,
 \qquad
 \eta=\sum_i\frac{b_i}{X_\theta-x_i}>0.                             \tag{8}
\]
The two-point bound at the same source gives \(\delta<T+2\), uniformly over this fixed fiber, so \(\theta=q+O_P(1)\).
Along a sequence with \(\delta\to E\), necessarily \(q\to\infty\): otherwise the strict lower term \(E/(\theta-1)\) in (8) stays bounded away from zero.
Every denominator in (8) is then \(q+O_P(1)\).
It follows that
\[
 \delta\to E
 \quad\Longleftrightarrow\quad
 \sum_i b_i=o(q),
 \qquad
 \frac{|R(T)|}{q}\to Z,
 \qquad
 \frac{f(-1)}q\to2\mathfrak a.                                    \tag{9}
\]
The equivalence is understood along \(q\to\infty\); all root gaps in this paragraph are fixed positive numbers depending on \(P\).

<a id="unit-orbit"></a>
## Every chamber norm is realized infinitely often

Use the accepted [order-level logarithmic unit theorem](../audits/literature/Con26/Yin_U001.md#con26-u001).
For the full order \(\mathcal O\), the vectors
\[
 \lambda(\varepsilon)=
       (\log|\varepsilon(T)|,\log|\varepsilon(x_1)|,
                         \ldots,\log|\varepsilon(x_h)|)
\]
of its units form a full lattice in \(\sum_{i=0}^h\lambda_i=0\).
The logarithms of the totally positive units also form a full lattice: they contain the logarithms of all squared units, which give twice the original lattice, and they are a subgroup of the original lattice.
Totally positive units have norm one.

Fix any \(\nu\in\mathcal C\), with absolute norm \(n\).
A bounded fundamental parallelepiped of this positive-unit lattice supplies, for each sufficiently large real \(u\), a totally positive unit \(\varepsilon_u\) whose logarithmic vector differs by a bounded amount from
\[
                              (hu,-u,\ldots,-u).                    \tag{10}
\]
Represent \(\nu\varepsilon_u\) by its unique integer polynomial \(R_u\) of degree at most \(h\).
It remains in the same strict chamber, its absolute norm is exactly \(n\), and
\[
 |R_u(T)|\asymp_{P,\nu}e^{hu},\qquad
 |R_u(x_i)|\asymp_{P,\nu}e^{-u},\qquad
 b_{u,i}\asymp_{P,\nu}e^{-u}.                                      \tag{11}
\]
The constants also incorporate a fixed covering radius for the chosen order-unit lattice.

The leading coefficient in Lagrange interpolation at all the roots of \(Q\) is
\[
 \operatorname{lc}_h R_u
  =\frac{R_u(T)}{Z}
       +\sum_i\frac{R_u(x_i)}{Q'(x_i)}
  =-\frac{|R_u(T)|}{Z}
       +\sum_i\frac{b_{u,i}}{T-x_i}.                               \tag{12}
\]
Here \(\operatorname{lc}_h\) means the coefficient of \(X^h\), including when a polynomial has smaller degree.
Set
\[
                         q_u=1-\operatorname{lc}_h R_u.
\]
This is an integer, and (11)--(12) give
\[
                   q_u\sim |R_u(T)|/Z\asymp e^{hu}\to\infty.
\]
In particular \(R_u\) eventually has degree exactly \(h\) and \(q_u\ge2\).
Moreover \(\sum_i c_{u,i}=O(e^{-u})\), so the strict simplex inequality (5) holds eventually.
The inverse (4) is therefore an actual Pisot minimal polynomial of degree \(2m\), returns exactly the prescribed \(P\), and satisfies
\[
 \delta_u\to E,\qquad
 |N(R_u(T))|=n,
 \qquad
 b_{u,i}\asymp q_u^{-1/h}.                                         \tag{13}
\]
Since \(q_u\) is unbounded, this realizes the norm \(n\) at infinitely many distinct constants, after taking a subsequence if necessary.
Together with the converse chamber inclusion following (6), this proves that the absolute norms occurring in the full Pisot inverse fiber are exactly the absolute norms in \(\mathcal C\).

The external input used here is the complete real logarithmic lattice for an arbitrary order, as recorded from Conrad's Theorem 1.1 and Section 3, especially the compactness and full-lattice conclusion.
The passage from that lattice to (10), the sign preservation, the interpolation, and the strict inverse test are local deductions above.
The accepted source supplies no degree-uniform covering radius, effective regulator bound, or prescribed values of \(q_u\).

<a id="resultant-minimum"></a>
## The exact normalized resultant minimum

Let \(\mathcal S_P\) be the collection of sequences of actual inverses of this fixed \(P\) with \(q\to\infty\) and \(\delta\to E\).
The unit construction shows that this collection is nonempty.
Equations (2), (7), and (9) imply
\[
 \boxed{
 \inf_{(f_k)\in\mathcal S_P}
       \liminf_k\frac{\mathcal R(f_k)}{q_k}
          =2\mathfrak a\,|P(1)|\,\mu(P)^2.}
                                                                    \tag{14}
\]
For the lower bound, \(n_k\ge\mu(P)\) and \(f_k(-1)/q_k\to2\mathfrak a\).
For equality, choose a chamber element attaining \(\mu(P)\), and use its balanced totally positive unit orbit.
On this sequence the normalized resultants converge to the displayed value.
More generally every chamber norm \(n\) is realized with the exact limit \(2\mathfrak a|P(1)|n^2\).

One may also write the constant as
\[
          \frac{2P(-1)|P(1)|}{T+2}\,\mu(P)^2,                       \tag{15}
\]
because \(P(-1)=(T+2)\mathfrak a>0\).
This minimization concerns the near-optimal portion \(\delta\to E\) of the full fixed-output fiber; it makes no assertion at a prescribed integer constant.

<a id="third-order"></a>
## The optimal power for the remaining excess

The exact subtraction in (8) is useful: set
\[
                    \eta=\delta-\frac{E\theta}{\theta-1}.
\]
For any actual inverse, the arithmetic-geometric mean inequality applied to the positive summands in (8), together with (7), gives
\[
 \eta\ge h\left(
       \frac{n}{|R(T)|D_H H(X_\theta)}\right)^{1/h}.                 \tag{16}
\]
Along any sequence in \(\mathcal S_P\), equation (9) gives \(|R(T)|/q\to Z\), and \(H(X_\theta)/q^h\to1\).
Thus
\[
 \liminf q^{1+1/h}\eta
      \ge h\left(\frac{\mu(P)}{Z D_H}\right)^{1/h}
       =h\left(\frac{\mu(P)Z}{D_Q}\right)^{1/h}>0.                 \tag{17}
\]
On a balanced unit orbit with any fixed chamber norm, (13) and the denominators \(q+O_P(1)\) in (8) give
\[
                 0<\liminf q^{1+1/h}\eta
                    \le\limsup q^{1+1/h}\eta<\infty.               \tag{18}
\]
Consequently the power \(q^{-1-1/h}\) is attained up to fixed multiplicative constants and cannot be replaced by a smaller asymptotic order over all favorable sequences in the fixed fiber.
This is a refinement after removing the exact positive term \(E\theta/(\theta-1)\), not merely after subtracting \(E+E/q\).

The lower constant in (17) has not in general been proved attainable.
To describe the missing condition, fix an element \(\nu\) of norm \(n\), write \(\nu_0,\nu_i\) for its embeddings, and let \(\lambda\) be a positive-unit logarithmic vector.
Along orbits with the required growth and bounded normalized residue shape,
\[
 \log(q^{1/h}b_i)
   =\log\frac{|\nu_i|}{|H'(x_i)|}
       +\frac1h\log\frac{|\nu_0|}{Z}
       +\lambda_i+\frac{\lambda_0}{h}+o(1).                        \tag{19}
\]
The sum of these coordinates tends to \(\log(n/(ZD_H))\).
Equality in the asymptotic arithmetic-geometric mean bound would require all coordinates in (19) to approach the same value.
Bounded covering distance to (10) ensures bounded coordinates, but does not itself prove that specific approximation in the projected unit lattice.
For \(h=1\) there is only one coordinate, so every fixed-norm balanced orbit does attain the constant \(n/Z\) in (17).
No stronger shape-density theorem is assumed for \(h>1\).

<a id="lehmer-unit"></a>
## An exact minimum-norm example for Lehmer's polynomial

For the accepted [degree-ten Lehmer benchmark](../claims/Yin_C_G0345_v291.md#benchmark-proof),
\[
 Q(X)=X^5+X^4-5X^3-5X^2+4X+3.
\]
Let
\[
 \alpha=(-1-\sqrt5)/2,\qquad \gamma=(-1+\sqrt5)/2,
 \qquad V(X)=-(X+1)(X^2+X-1).
\]
The exact intervals in that benchmark place \(x_1,x_2,x_3,x_4\) respectively in
\[
 (-2,\alpha),\quad(\alpha,-1),\quad(-1,\gamma),\quad(\gamma,2).
\]
Thus \(V(x_i)\) has signs \(+,-,+,-\), opposite to the signs of \(H'(x_i)\), and \(V(T)<0\).
So \(V(T)\in\mathcal C\).
Its absolute norm is one, without a numerical root or unit search:
\[
 |N(T+1)|=|Q(-1)|=1,
\]
and the remainder \(Q(X)\equiv X+2\pmod{X^2+X-1}\) gives
\[
 |N(T^2+T-1)|
   =|Q(\alpha)Q(\gamma)|
   =(\alpha+2)(\gamma+2)=1.
\]
Hence \(\mu(P)=1\).
The representative \(V\) itself has coefficient of \(X^4\) zero and so does not supply an admissible constant \(q\ge2\); the balanced unit orbit is what supplies the actual inverses.

For this polynomial \(|P(1)|=P(-1)=1\), so (14) becomes the exact value
\[
                            \frac{2}{T+2}.                         \tag{20}
\]
Here \(h=4\), and the third-order lower bound is \(4(Z/D_Q)^{1/4}\), with its power attained up to fixed multiplicative constants as above.
The scalar value (20) is attained as a limit along same-output, same-degree inverses whose constants tend to infinity.

<a id="diagonal"></a>
## A restricted input class sufficient for the Salem gap question

Let \(F(d)>0\) and \(\epsilon(d)>0\) be arbitrary prescribed functions of the even degree.
If Salem numbers tend to one, there are monic positive-constant Pisot minimal polynomials \(f\) of increasing even degrees \(d\), with constants \(q\ge F(d)\), such that
\[
 \theta-q\longrightarrow0,\qquad
 q^{1-\epsilon(d)}<|\operatorname{Res}(f,f^*)|<q^{1+\epsilon(d)} .
\]
In addition one may require \(q^{-(1+\epsilon(d))/h}<b_i<q^{-(1-\epsilon(d))/h}\) for every neutral residue of the corresponding inverse, with \(h=d/2-1\).

Indeed choose a sequence of supplied Salem polynomials approaching one in strictly increasing degrees, using bounded-degree finiteness.
At each fixed polynomial first choose one of the orbits (13).
As \(q\to\infty\) on that orbit, \(\mathcal R(f)/q\) tends to the positive finite number \(2\mathfrak a|P(1)|n^2\), and each \(q^{1/h}b_i\) stays between two strictly positive constants.
The constants may depend arbitrarily on that polynomial and on the orbit.
Since \(\epsilon(d)\) is already fixed at this degree, choose one sufficiently large orbit member satisfying both power windows, the stated lower bound on \(q\), and \(\delta-E<1/d\).
This diagonal choice proves the assertion.
Conversely, excess tending to zero in this restricted class gives Salem numbers tending to one by the [positive return and two-point bound](../claims/Yin_C_G0345_v292.md#prescribed).
Thus excluding such sequences would suffice for a uniform Salem gap.
The argument permits an arbitrarily large lower threshold for \(q\) and selects its value separately for each output.
It gives no upper threshold for \(q\), and a Salem gap would still leave reciprocal units with several exterior pairs to treat for G0001.

One can also prescribe a positive integer modulus \(M\) and any residue polynomial \(W\in(\mathbb Z/M)[X]\) of formal degree at most \(h\), separately for each supplied \(P\) before selecting \(q\).
Lift \(W\) to an integer polynomial of degree at most \(h\).
Adding a sufficiently large positive integer multiple of \(MR_0\), where \(R_0\) is the strict chamber representative in (1), puts this lift into the chamber without changing its coefficient residues.
Use this element as \(\nu\) and restrict (10) to totally positive units congruent to one in \(\mathcal O/M\mathcal O\).
This subgroup has finite index because reduction has finite image, so its logarithms still form a full lattice.
Reduction of the products modulo the monic \(Q\) preserves the representative congruence \(R_u\equiv W\pmod M\) in the power basis.
Equations (11)--(13) therefore give the same diagonal windows with this additional condition, including \(q\equiv1-[X^h]W\pmod M\).
For \(M=1\) the congruence is vacuous.
The chosen chamber element and its norm can depend on \(W,M,P\), so this argument does not prescribe the minimum norm simultaneously.

<a id="comparison"></a>
## What this changes and what remains supplied

The [fixed-output inverse](../claims/Yin_C_G0345_v2.md#optimum) already gives the limiting excess \(E\), and the [full simplex result](../claims/Yin_C_G0345_v4.md#second-order) gives the sharp second-order lower limit by making positive residues tend to zero along favorable constants.
The [least-excess envelope](../ledger/Yin_L_G0462_v33.md#least-excess) already connects these fixed-output inverses to the unrestricted near-one question by a diagonal choice of constants.
The additional information here is exact preservation and realization of every chamber norm, the minimum (14), and the power bound (17)--(18).
The [low-degree residue-representative bound](../claims/Yin_C_G0345_v33.md#statement) concerns a different normalization and degree window; no low degree or bounded height of the representatives \(R_u\) beyond reduction modulo \(Q\) is asserted here.

The construction begins with the entire Salem polynomial and retains its field and output throughout.
The chamber is always nonempty, so its mere existence provides no new obstruction to a small Salem measure.
The sign class of its units, the value \(\mu(P)\), and the projected logarithmic shapes in (19) are concrete additional quantities to investigate as the supplied polynomial varies.
The Lehmer example shows that the required sign class can already contain a unit.
None of the current arguments controls these quantities, the unit-lattice covering radius, or the required constants uniformly as the degree varies.
In particular they do not put these near-minimal resultant orbits at \(q=d^2\), and they neither construct Salem numbers tending to one nor rule them out.
