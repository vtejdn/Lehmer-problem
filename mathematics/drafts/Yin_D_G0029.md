---
author: Yin
---

# Radial deficits at the neutral pairs of an exact Salem return

This continuing calculation for [G0001](../tasks/Yin_T_G0001_v1.md#contract) concerns the roots of the Pisot input at a fixed supplied Salem output.
The phase and radial estimates below are author calculations awaiting independent review.
Their purpose is to test which root configurations a proof for the restricted Pisot inputs must cover.

<a id="local"></a>
## Motion at each original circle pair

Use a fixed Salem minimal polynomial \(P=z^mQ(z+z^{-1})\), with exterior trace \(T>2\), \(E=T-2\), internal traces \(x_i=2\cos t_i\), \(0<t_i<\pi\), and \(h=m-1\).
Write \(H=Q/(X-T)\) and \(\zeta_i=e^{it_i}\).
In the [exact inverse simplex](../claims/Yin_C_G0345_v4.md#simplex), let \(q\to\infty\) with \(0<b_i\le B\) for a fixed bound \(B\).
There is one root \(z_i\) of the monic Pisot inverse \(f\) near each \(\zeta_i\), and one near each \(\overline{\zeta_i}\).
Writing \(X_i=z_i+z_i^{-1}\), the individual deficits satisfy
\[
 -\log|z_i|=\frac{T-x_i}{2(2-x_i)}\frac{b_i}{q^2}
                      \bigl(1+O_{P,B}(q^{-1})\bigr).                 \tag{1}
\]
In particular the relative error remains controlled when one positive residue is much smaller than all the others.

Indeed for \(X=z+z^{-1}\), the inverse formula gives
\[
 f(z)=z^{m-1}\left[p_q(z)H(X)
          -(z-1)\sum_k b_k\frac{H(X)}{X-x_k}\right],
 \qquad p_q(z)=(z-1)(z-q)-Ez .
\]
The polynomials \(f/q\) converge locally uniformly to \(-(z-1)z^{m-1}H(X)\).
This limit has simple roots at \(1,\zeta_i,\overline{\zeta_i}\).
On small disjoint circles about these points Rouché's theorem gives exactly one nearby root of \(f\), with convergence to the indicated center.
Near \(\zeta_i\) all other denominators stay bounded away from zero and \(z\mapsto X\) has nonzero derivative.
At \(X=x_i\) the \(i\)-th summand prevents vanishing.
Thus the root equation can be written exactly as
\[
 X_i-x_i=\frac{b_i}{-q+C(z_i)-\sum_{k\ne i}b_k/(X_i-x_k)},\qquad
                     C(z)=z-\frac{Ez}{z-1}.
\]
The bounded correction to \(-q\) gives \(X_i-x_i=O_{P,B}(b_i/q)\), hence \(z_i-\zeta_i=O_{P,B}(b_i/q)\) by the local inverse.
Expanding the denominator once more gives
\[
 X_i-x_i=-\frac{b_i}q-\frac{b_i}{q^2}
       \left(C(\zeta_i)-\sum_{k\ne i}\frac{b_k}{x_i-x_k}\right)
       +O_{P,B}(b_i/q^3).                                          \tag{2}
\]
Only \(C(\zeta_i)\) has an imaginary part in that coefficient.
Its imaginary part is \(\sin t_i+(E/2)\cot(t_i/2)>0\).
For \(z_i=e^{-u_i+i\phi_i}\), one has
\(\Im X_i=-2\sinh(u_i)\sin\phi_i\), with \(\sin\phi_i=\sin t_i+O_{P,B}(q^{-1})\).
Dividing the imaginary part of (2) by this factor proves (1), since
\[
 \frac{\sin t_i+(E/2)\cot(t_i/2)}{2\sin t_i}
                =\frac{T-x_i}{2(2-x_i)} .
\]

The remaining interior root \(z_0\) is real and positive near one by conjugation and uniqueness there.
Its deficit satisfies \(-\log z_0\sim E/q\).
In fact the positive product of all interior moduli is \(q/\theta\), so its total negative logarithm is \(\log(\theta/q)\sim E/q\) by the [exact excess identity](../claims/Yin_C_G0345_v4.md#second-order).
Equation (1) puts the entire contribution of the \(h\) neutral pairs at \(O_{P,B}(q^{-2})\).
Thus almost all radial loss in this limit occurs at the real root, regardless of the relative shares among the neutral pairs.

<a id="radial-identity"></a>
## An exact identity at every nonreal inverse root

The same radial coefficient holds throughout the fixed-output range \(\delta\to E\), which allows individual residues to grow.
For any nonreal root \(z\) of any of the actual inverses, with \(X=z+z^{-1}\), one has
\[
 \bigl(|z|^{-2}-1\bigr)\sum_k\frac{b_k}{|X-x_k|^2}
                         =1+\frac{E}{|z-1|^2}.                       \tag{4}
\]
Indeed the root equation is \(C(z)-q=\sum b_k/(X-x_k)\).
The imaginary parts are \(\Im C(z)=(\Im z)(1+E/|z-1|^2)\) and \(\Im X=(\Im z)(1-|z|^{-2})\).
Taking imaginary parts on both sides and canceling \(\Im z\) gives (4).
All divisors are nonzero because \(f\) has nonzero constant and no roots on the unit circle.

In the fixed fiber with \(q\to\infty\) and \(\delta\to E\), the [excess identity](../claims/Yin_C_G0345_v4.md#second-order) gives \(\sum b_k=o(q)\).
The same polynomial limit and local labeling therefore hold.
In the isolated equation for \(X_i-x_i\), the denominator is \(-q+o(q)\), because the other poles stay a fixed positive distance away.
Hence \(X_i-x_i=-(b_i/q)(1+o(1))\).
In the sum in (4) its own term is asymptotic to \(q^2/b_i\), whereas the other terms have sum \(O_P(\sum b_k)=o(q)\).
Since \(b_i=o(q)\), the own term dominates.
Taking \(z_i\to\zeta_i\) in (4) proves (1) with relative error \(o(1)\) for all of these sequences.
In particular the total radial loss in the neutral pairs is \(o(1/q)\), compared with total loss \(\log(\theta/q)\sim E/q\).

A polynomial with integer coefficients sees the individual deficits via conjugate products.
Let \(G(Y)=\prod_{a<b}(Y-\alpha_a\alpha_b)\), with the \(\alpha_a\) the roots of \(f\), counted with multiplicity.
This polynomial is integral by symmetry.
The product formula for the reciprocal resultant gives
\[
 \operatorname{Res}(f,f^*)=f(1)f(-1)G(1)^2,
 \qquad |G(1)|=|N_{\mathbb Q(T)/\mathbb Q}(R(T))|.
\]
For the second equality use \(f(1)=P(1)\) and the [fiber identity](../claims/Yin_C_G0345_v296.md#fiber).
In a fixed fiber along \(\delta\to E\), exactly \(h\) of the pair products converge to one, namely \(|z_i|^2\) for the original circle pairs.
Products with \(\theta\) diverge in modulus, and the remaining bounded roots have distinct limiting arguments at \(1,\zeta_i,\overline{\zeta_i}\).
Hence no other pair has limiting product one.
At these \(h\) real roots of \(G\), the distances from one are asymptotic to \((T-x_i)b_i/((2-x_i)q^2)\).
This identifies the small factors in the integer \(G(1)\) and provides a direct polynomial for investigating whether information beyond its value at one can constrain simultaneous radial concentration.

<a id="shares"></a>
## Prescribing the distribution within the neutral pairs

Fix any probability vector \(p=(p_1,\ldots,p_h)\), allowing zero entries.
Fix a positive modulus \(M\) and a coefficient residue class \(W\) in the power basis of \(\mathbb Z[T]\) modulo \(M\).
There is a sequence of actual same-degree Pisot inverses with \(q\to\infty\), returning the same \(P\) and satisfying \(R\equiv W\pmod M\), such that
\[
 \frac{-\log|z_i|}{\sum_k(-\log|z_k|)}\longrightarrow p_i,\qquad
 \frac{\log b_i}{\log q}\longrightarrow-1/h,\qquad
 \frac{\log|\operatorname{Res}(f,f^*)|}{\log q}\longrightarrow1 .     \tag{3}
\]
The denominator in the first expression sums one root per original neutral pair.
It excludes the real root near one.

Here is a construction that permits the chamber norm to vary.
In embedding coordinates the class \(W+M\mathbb Z[T]\) is a translate of a full lattice in \(\mathbb R^{h+1}\), by the invertible Vandermonde matrix at \(T,x_1,\ldots,x_h\).
For each strictly positive target vector \(p'\), choose a vector with negative distinguished coordinate and with internal coordinates
\[
      -H'(x_i)\,p'_i\,\frac{2(2-x_i)}{T-x_i}.
\]
Approximate a sufficiently large positive multiple of this vector in the given lattice translate, with bounded absolute error.
This produces a strict chamber element \(\nu\), with the proportions of the positive quantities
\[
           \frac{T-x_i}{2(2-x_i)}
                         \frac{|\nu(x_i)|}{|H'(x_i)|}
\]
as close to \(p'\) as desired.

There are totally positive units in the congruence kernel with logs
\[
         (hu,-u,\ldots,-u)+o(1),\qquad u\to\infty .
\]
To see this, use its full logarithmic lattice from the [congruence-class unit construction](../claims/Yin_C_G0345_v297.md#congruences).
The integer multiples of \(v=(h,-1,\ldots,-1)\) in the compact quotient of the log hyperplane by this lattice have a convergent subsequence.
Choosing increasingly widely separated pairs from that subsequence gives \(u\to\infty\) with the distance of \(uv\) to the lattice tending to zero.
This also covers a periodic orbit in the quotient.

For each fixed \(\nu\), multiplication by these units preserves the required coefficient congruence.
The inverse interpolation formula gives \(q\asymp_\nu e^{hu}\), while every internal \(b_i\) equals \(e^{-u}|\nu(x_i)|/|H'(x_i)|\,(1+o(1))\).
The full [inverse conditions](../claims/Yin_C_G0345_v297.md#unit-orbit) hold eventually, and the [reciprocal resultant formula](../claims/Yin_C_G0345_v296.md#fiber) gives a positive finite limit of \(|\operatorname{Res}(f,f^*)|/q\) on each of these individual orbits.
Use positive vectors \(p'\to p\) and progressively more accurate chamber approximations.
For each successive chamber element choose one orbit member sufficiently far along to have \(b_i<1\) for all \(i\), \(q\) strictly increasing, and errors tending to zero in (1) and in the limits (3).
This proves (3), including its boundary cases.
The varying chamber elements need not preserve an individual norm level or its minimum.

<a id="pair-coefficients"></a>
## Coefficients at one in a fixed fiber

Write \(g_j(f)=[X^j]G(1+X)\).
For the fixed-output sequences with \(\delta\to E\), put \(d_i=1-|z_i|^2>0\).
For \(1\le j\le h\) the coefficient ratios satisfy
\[
 \frac{g_j(f)}{G(1)}
     =(1+o(1))\,e_j(d_1^{-1},\ldots,d_h^{-1}),
\]
where \(e_j\) denotes the elementary symmetric function.
Indeed \(G(1+X)/G(1)\) is the product of \(1+X/(1-\alpha_a\alpha_b)\) over all pairs.
The reciprocals on the \(h\) indicated pairs tend to positive infinity, and all remaining reciprocals are bounded.
For \(0\le k<j\le h\), extending each \(k\)-subset to \(j\)-subsets gives \(e_k/e_j=O_h((\min_i d_i^{-1})^{k-j})\).
Thus every summand using at least one of the remaining pairs has smaller order, even if the rates of the \(d_i\) differ.

In particular
\[
                \frac{g_h(f)}{q^{2h+1}}\longrightarrow-H(2)D_H .
\]
To see the sign and the full coefficient limit directly, let \(\Lambda\) consist of \(1,\zeta_i,\overline{\zeta_i}\) for \(1\le i\le h\), with \(1\) listed once.
The \(2h+1\) factors belonging to pairs with \(\theta\), divided individually by \(q\), tend coefficientwise to constants whose product is \(-1\), since \(\theta/q\to1\) and \(\prod_{\lambda\in\Lambda}\lambda=1\).
Consequently \(G(Y)/q^{2h+1}\) converges coefficientwise to minus the product of \(Y-\lambda\lambda'\) over unordered distinct members of \(\Lambda\).
Exactly \(h\) factors are \(Y-1\).
The remaining factors at \(Y=1\) from pairs involving the member \(1\) multiply to \(H(2)\).
For two distinct internal traces \(x_i,x_j\), the four cross products contribute \((x_i-x_j)^2\), by grouping each product with its inverse and using \(\zeta_i+\zeta_i^{-1}=x_i\).
Their product over \(i<j\) is \(D_H\), proving the limit including \(h=1\).

<a id="integral-expansion"></a>
## Simultaneous divisibility and the first nonzero homogeneous part

The arithmetic behavior of these coefficients also has an exact local calculation at the original Salem polynomial.
For an integer polynomial \(W\) of degree at most \(h\), introduce an indeterminate \(u\) and set
\[
 f_u(z)=P(z)+u(z-1)z^{m-1}W(z+z^{-1}).
\]
Let \(G_u(Y)\) be the polynomial of pair products formed from \(f_u\).
It belongs to \(\mathbb Z[u,Y]\), by symmetry and monicity.
If \(y_1,\ldots,y_m\) are all roots of \(Q\), including \(T\), then the first nonzero total-degree part at \(X=u=0\) is
\[
 G_u(1+X)=D_Q\prod_{i=1}^m
             \left(X+u\,\frac{W(y_i)}{Q'(y_i)}\right)
               + \text{terms of total degree greater than }m,
 \qquad D_Q=\operatorname{disc}Q .
\]
For a simple reciprocal pair \(a,a^{-1}\) of \(P\), with \(y=a+a^{-1}\), choose the two local root branches of \(f_u\).
Their derivatives at zero are \(-aW(y)/((a+1)Q'(y))\) and the same expression with \(a^{-1}\).
Here \(P'(a)=a^mQ'(y)(1-a^{-2})\), and \(a\ne\pm1\).
The derivative of their product equals \(-W(y)/Q'(y)\), using \(1/(a+1)+1/(a^{-1}+1)=1\).
Each of the \(m\) reciprocal pairs therefore contributes the displayed first-degree factor.
All cross factors at the origin multiply to \(\prod_{i<j}(y_i-y_j)^2=D_Q\), by the same four-factor identity as above.
This proves the expansion, whose homogeneous coefficients are integers because they are coefficients of \(G_u(1+X)\).

Write \(L_j=[X^j]D_Q\prod_i(X+W(y_i)/Q'(y_i))\).
For every integer \(M\ge2\) and \(0\le j\le m\) the expansion gives
\[
          g_j(f_M)\equiv M^{m-j}L_j\pmod {M^{m-j+1}}.
\]
This holds for every integral direction \(W\), regardless of the location of the roots of \(f_M\).
In particular every actual inverse with \(R\equiv0\pmod M\) has \(M^{m-j}\mid g_j(f)\) for \(0\le j<m\), since \(R=MW\).
The [zero-class norm construction](../claims/Yin_C_G0345_v297.md#congruences) gives arbitrarily large actual constants at each fixed \(P,M\).
Thus these simultaneous divisibilities coexist with the preceding fixed-fiber limit for \(g_h\).
The remaining question is whether estimates uniform in the varying trace roots and the inverse constant can impose stronger arithmetic restrictions.

<a id="scope"></a>
## The remaining degree issue

The local estimates contain constants depending on the full supplied trace configuration.
For a hypothetical sequence of Salem polynomials approaching one, one may choose a separate accuracy, a target vector, a coefficient congruence and an arbitrarily large lower bound on \(q\) at each degree.
Applying (1)--(3) to each polynomial before choosing its constant yields small-excess Pisot inverses with those neutral shares to the requested accuracy and with the real root carrying a proportion arbitrarily close to one of the total radial loss.
One may likewise require \(b_i\in(q^{-(1+\epsilon)/h},q^{-(1-\epsilon)/h})\) and the resultant power window of the [diagonal construction](../claims/Yin_C_G0345_v297.md#diagonal) for each assigned \(\epsilon>0\).
This supplies a test for proposed uniform estimates on the actual roots.
Its degree-dependent choices leave open how far the constant must grow and how to produce a shrinking sequence of outputs in the first place.
