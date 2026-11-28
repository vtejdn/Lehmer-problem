---
author: Yin
---

# What local degrees, residue periods and short orbits detect in the Lehmer problem

This working draft investigates the [unrestricted gap](../tasks/Yin_T_G0001_v1.md#contract) on four families of objects.
The deductions below are author-side calculations.
The cited source theorems and fixed project results retain their own scopes.

<a id="records"></a>
## Which primes carry the norm of a translate between adjacent records?

The [local degree estimate](../claims/Yin_C_G0901_v200.md#records) puts asymptotically all the norm at primes of small relative degree.

<a id="across-records"></a>
### How much ideal norm can earlier rows recover?

[Comparison across consecutive rows](../claims/Yin_C_G0901_v200.md#across-records) leaves almost all the normalized norm on pairwise coprime ideal divisors over a growing window.
Above each rational prime, the [largest local depths](../claims/Yin_C_G0901_v202.md#depth) carry almost all the normalized norm when summed over all primes.
An [irreducible strict Perron unit family](../claims/Yin_C_G0901_v202.md#one-prime) realizes the whole mass above three.
For a later Salem record, the [involution over the relative trace field](../claims/Yin_C_G0901_v204.md#salem) puts almost all this mass on one prime per split pair and bounds the discarded mass explicitly.
When both records are Salem, [absolute local degrees and the two independent Salem inversions](../claims/Yin_C_G0901_v206.md#trace) restrict almost all the weight to one place per completely split quartet.
The [trace norm equation](../claims/Yin_C_G0901_v206.md#conic) leaves open how deeply a small local factor over a fixed rational prime can divide that norm.
If a fixed prime set carries a fixed positive mass and the later record is Salem, a positive mass must reach [depth at least a constant times \(n/\log n\) at relative degrees \(O(\log n)\)](../claims/Yin_C_G0901_v208.md#records), where \(n=[\mathbb Q(A,B):\mathbb Q(A)]\).
Two [fixed quartic Salem numbers](../claims/Yin_C_G0901_v208.md#example) attain arbitrarily large depth at a smooth conic point over 17 when the exponent is unrestricted.
For two shrinking Salem records, [all earlier powers in the allowed window](../claims/Yin_C_G0901_v210.md#window) are already separated at depth \(O(\sqrt{D\log D}/\log p)\), where \(D=\deg A\).
The much deeper congruence to \(2/B\) requires [large multiplicative order](../claims/Yin_C_G0901_v210.md#order) at its actual precision.
The two units then [generate the same local field](../claims/Yin_C_G0901_v212.md#records) whenever their joint absolute local degree exceeds a fixed power of the logarithm of the later degree.

<a id="trace"></a>
## Completing the second residue period on the one-denominator controls

[The rowwise criterion and pole correction](../claims/Yin_C_G0901_v198.md#trace) specify the coefficient at offset \(J+1\) and reduce exact order \(N=A+2u\) to polynomial division over \(\mathbb Z/(q+1)\mathbb Z\).
The even-side substitution \(V(Z^t)\) fails this test at every prime of \(q+1\).

<a id="short-period-divisor"></a>
### A divisor of small degree carrying the entire second period

[The synchronized rows and short divisor](../claims/Yin_C_G0901_v198.md#short-period-divisor) give exact order \(N\) on a reciprocal divisor of degree less than \(\varepsilon d\).
To complete its word one can test the complementary divisors of \(Z^N-1\) at the required degree and prefix.

<a id="period-completion"></a>
### Matching the second period on all but a vanishing fraction of the degree

[The large divisor and the remaining prime-power excess](../claims/Yin_C_G0901_v198.md#period-completion) give exact order \(N\) on degree \(d-o(d)\) while retaining the even-side and real bounds.
At \(q+1=3^\nu\) with \(\nu\) even, the [boundary coefficient restriction](../claims/Yin_C_G0901_v201.md#boundary) excludes all but three residue classes.
On the strengthened zero-boundary rows, the [finite group calculation](../claims/Yin_C_G0901_v203.md#count) counts full-degree words of exact order, so the existence problem becomes positivity of an integer attached to the row.
Chosen words on actual rows can have returned fraction tending to one at linear time and [full period arbitrarily close to quadratic on a logarithmic scale](../claims/Yin_C_G0901_v203.md#order).
One can now choose a [factor of degree \(d-o(d)\)](../claims/Yin_C_G0901_v205.md#large-roots) with the required zero prefix and exact order \(N\) such that each of its residue roots has multiplicative order at least \(N/(8\tau(N))\), where \(\tau\) counts divisors.
The [remaining degree correction](../claims/Yin_C_G0901_v205.md#filler) can introduce a power of three into the order of the full word.
The [quotient Fourier test](../claims/Yin_C_G0901_v207.md#frequencies) excludes rows whose known vanishing frequencies cover the nonzero part of a subgroup.
Even bounded multiplicities in each fixed residue field allow [orders of size \(d^{2-o(1)}\)](../claims/Yin_C_G0901_v207.md#repetitions) when the roots of greatest multiplicity have growing prime order.
At the neighboring period \(A=N-2u\), a [full-degree word of exact order \(A\)](../claims/Yin_C_G0901_v209.md#times) exists on every sufficiently large strengthened row.
The two possible words on the same row have opposite return behavior at \(A\) and \(N\).
At a separate [family of periods](../claims/Yin_C_G0901_v211.md#subfields), two proper subfields supply the final \(O(\log d)\) degrees without introducing a power of three into the order.
The even-side word remains to be constructed on those same rows.

<a id="dynamics"></a>
## Central directions, finite memory and periodic orbit resolution

Consider the toral automorphism \(A\) attached to an irreducible monic unit polynomial \(P\) with a root \(\beta>1\) and a conjugate \(\omega\) on the unit circle.
All conjugates have infinite multiplicative order.
Lindenstrauss and Schmidt prove that the homoclinic group of this nonexpansive ergodic irreducible system is trivial. [Theorem 4.1 and Corollary 4.2](../audits/literature/LS05/readme.md)
The homoclinic group consists of the points tending to zero under both forward and backward iteration.
It is the same for each \(A^N\), since convergence along multiples of \(N\) gives convergence along each of the \(N\) residue classes by continuity.
A continuous equivariant injection of a two-sided full shift with at least two symbols into any iterate would send a pair of sequences differing at just one coordinate to two distinct points with homoclinic difference.
Thus this particular approach to repeatable binary choices fails even on a single Salem torus.
The direction of the map matters: this argument concerns a continuous embedding of a shift into the torus.
[Quas and Soo, Theorem 2](../audits/literature/QS16/readme.md) gives a measurable embedding of an ergodic system of strictly lower entropy, which already requires an entropy comparison.

**A finite-memory test on the actual digits.**
Suppose integer digits \(a_e\) label the edges of a finite irreducible stationary Markov chain with \(s\) states.
Keep the edges of positive transition probability and allow parallel edges.
For a stationary path consider \(S_n=\sum_{k=0}^{n-1}\omega^k a_{e_k}\).
Its laws are tight exactly when there are complex \(g_i\) such that \(a_e=g_i-\omega g_j\) on every edge \(i\to j\).
To see this, let \(P_0\) be the state transition matrix and solve \((I-\omega P_0)g=(\mathbb E_i a_e)_i\).
This is possible because the peripheral eigenvalues of a finite irreducible stochastic matrix are roots of unity.
The bounded variables \(D_e=a_e-g_i+\omega g_j\) are martingale differences along the chain.
Then \(S_n=g_{i_0}-\omega^n g_{i_n}+\sum_{k<n}\omega^kD_{e_k}\).
The last sum has second moment \(n\mathbb E|D_e|^2\) by orthogonality.
Its fourth moment is \(O(n^2)\), by integrating the bounded-difference martingale tail inequality for its real and imaginary parts.
If the variance is positive, the second-moment lower bound on the probability of a nonnegative variable exceeding half its mean, applied to the squared modulus, gives \(\mathbb P(|S_n|\ge c\sqrt n)\ge c'>0\) for large \(n\).
If the variance vanishes, the edge relation holds and the endpoint expression is bounded.

Summing on a return path to state \(i\) gives \((1-\omega^j)g_i\in\mathbb Z[\omega]\) for some \(j>0\), whence each \(g_i\in\mathbb Q(\omega)\).
Transporting the endpoint identity to any conjugate of \(\omega\) leaves at most \(s^2\) different length-\(n\) digit evaluations.
For Salem \(\beta\) take the conjugate \(\beta^{-1}\).
Zero-padding a finite word of the two-sided \(\beta\)-shift preserves admissibility.
Two such words with the same evaluation have Laurent polynomial difference in the ideal generated by the minimum of \(\beta\).
The finite-support case of [LS05, Proposition 5.1(2), page 22](../literature/pdf/LS05.pdf#page=22) therefore identifies the words.
Bounded word count gives zero entropy on this shift.
In particular, the positive-entropy digit measures of [Theorem 7.1](../literature/pdf/LS05.pdf#page=28), which satisfy the central boundedness condition, cannot be stationary finite-state hidden Markov laws of this kind.
This conclusion uses the specific digits and the [necessary tightness of their central sums](../audits/literature/LS05/Yin_U001.md#ls05-u001).

<a id="periodic"></a>
**Periodic Fourier resolution.**
The [periodic-character estimate](../claims/Yin_C_G0904_v1.md#periodic) compares the shortest nonzero frequency in the annihilator of \(\operatorname{Fix}(A^j)\) with its cardinality \(N_j\).
A remaining question is whether arithmetic information about the individual neutral factors in \(N_j\) can produce a positive lower bound for total measure across degrees.

<a id="finite-time-dynamics"></a>
## Which finite-time measurements could force a gap?

The [periodic median](../claims/Yin_C_G0904_v1.md#finite-time-dynamics) at times of order \(d(\log(2d))^4\) and the [Gaussian estimate at one time](../claims/Yin_C_G0904_v1.md#deterministic) of order \(d^2(\log(2d))^4\) approximate total logarithmic measure as \(d\to\infty\).
The [modular criterion](../claims/Yin_C_G0904_v2.md#statement) gives such a constant on a class detected from the polynomial.
For strict records it suffices to find a fixed positive fraction of the full degree in a [cyclic mod-\(p\) homology return](../claims/Yin_C_G0904_v2.md#return-ranks) at an order \(O(d)\).
For Lehmer's \(P=X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1\), reduction modulo two gives \(\bar P\mid X^{31}-1\).
One can check this by multiplying \(\bar P\) by the sum of monomials with exponents \(0,1,2,5,7,9,10,11,12,14,16,19,20,21\) over \(\mathbb F_2\).
The return inequality at \(a=1\) gives \(\log M(P)\ge(5/31)\log 2\) directly from this congruence.
For the growing [Salem family with \(s=d+1\)](../claims/Yin_C_G0904_v2.md#statement), the same calculation gives \(\log M(F_d)\ge d\log2/(2(d+1))\).
If the polynomial consists of two end blocks of width \(r+1\) with \(r=o(d)\), the [coefficient reversal test](../claims/Yin_C_G0904_v3.md#statement) characterizes exactly when a fixed list of primes works.
For the whole irreducible polynomial, [signed reversal at even one prime forces \(M(P)>\sqrt{3/2}\)](../claims/Yin_C_G0904_v5.md#binomial).
A strict record from degree ten onward therefore has asymmetric end support modulo two at height one whenever it has this presentation.
For complete irreducible record closures the [reciprocal resultant and weighted local zero counts](../claims/Yin_C_G0904_v9.md#width) now force \(r\gg d\).
Thus the sublinear-width obstruction to returns cannot occur on this class of records.
Strict minimality also requires every shorter closure \(X^jQ\pm Q^*\), \(1\le j<n\), of positive logarithmic measure to have larger measure than the record.
On the positive Salem branch there is a [sign and crossing test](../claims/Yin_C_G0904_v8.md#shorter) for a competing closure.
In a [degree-twenty example](../claims/Yin_C_G0904_v8.md#example), shortening \(j=15\) to \(j=12\) and taking the minus sign gives precisely Lehmer's polynomial times cyclotomic factors.
Along a [decreasing Salem sequence](../claims/Yin_C_G0904_v3.md#salem) even the supremum over all primes has vanishing rank fraction in linear time.
The [fibers of a fixed hyperbolic exterior](../claims/Yin_C_G0904_v4.md#braid) have the same uniform obstruction by a different calculation, which counts repeated roots as well.
On the Salem branch, the [subfield estimate](../claims/Yin_C_G0904_v2.md#salem-subfields) requires consideration of vectors whose relative norms generate the whole trace field.
The [short-time Salem examples](../claims/Yin_C_G0904_v1.md#salem) and the [initial Gaussian behavior](../claims/Yin_C_G0904_v1.md#heat) constrain attempts to use shorter intervals.

<a id="geometry"></a>
## A second short element in the same arithmetic space

Douba and Huang's Theorem 2 realizes each \(\log\lambda\) for a Salem number \(\lambda\) as the systole of a closed arithmetic surface. [Journal article](https://doi.org/10.5802/crmath.689)
Frączyk and Pham's Theorem 5.1 gives another test: in a single arithmetic lattice in a fixed semisimple group without compact factors, rationally independent squared lengths force the sum of the two lengths to be at least \(c_G\sqrt e\,(\log e)^{-C_G}\) as the trace-field degree \(e\) grows.
Their Proposition 3.1 forces multiplicative dependence of pairs of nontorsion root values of a bounded-measure element for sufficiently large \(e\) with the ambient group fixed.
The passage from root values to a Salem unit in the simple real case uses the Galois action on the roots and a shortened product.
The proof displays a factor up to \((\dim G-\operatorname{rank}G)!/2\) in transferring the measure. [ArXiv v1, pages 8 and 15](../audits/literature/FP23/readme.md)
This is useful for a fixed hyperbolic plane; substituting general growing-dimensional companion matrices leaves the dependence on the ambient group to be controlled.
Putting two unrelated lengths on separate surfaces does not meet Theorem 5.1's common-lattice hypothesis. [Cost of joining marked trace fields](../claims/Yin_C_G0901_v170.md#statement)

One arithmetic version of the second-element test has an explicit height budget.
Put \(k=\mathbb Q(t)\), \(t=\lambda+\lambda^{-1}\), \(e=[k:\mathbb Q]\).
If \(\nu\) is multiplicatively independent of \(\lambda\) and \([k(\nu):k]\le2\), then their joint degree is at most \(4e\).
The two-variable [Amoroso–David product bound](../audits/literature/AD99/Yin_U001.md#ad99-u001) and \(h(\lambda)=\log\lambda/(2e)\) give
\[
  (\log\lambda) h(\nu)\ \gg\ (\log(12e))^{-212}. \tag{4}
\]
Finding such a \(\nu\) with \(h(\nu)\ll(\log(12e))^{-212}\) for every putative shrinking Salem sequence, with absolute constants, would suffice for a Salem gap.
The rank-one relative unit group in \(k(\lambda)/k\) accounts for the dependence of all its norm-one units. [Full-field regulator calculation](../claims/Yin_C_G0485_v1.md)

There is an obstruction to producing \(\nu\) by a fixed integral trace transformation.
Let \(\lambda_j\) be bounded Salem numbers of degree \(2e_j\to\infty\), fix nonconstant \(f\in\mathbb Z[X]\), and take either root of \(\nu_j+\nu_j^{-1}=f(t_j)\).
Writing \(g(x)=\operatorname{arcosh}(\max(1,|x|/2))\) for real \(x\), one has
\[
   h(\nu_j)=\frac{1}{2e_j}\sum_{\sigma:k_j\hookrightarrow\mathbb R}g(f(\sigma t_j))
   \longrightarrow \frac12\int_{-2}^{2}g(f(x))\,\frac{dx}{\pi\sqrt{4-x^2}} .
\]
Indeed \(\nu_j\) is a unit and the absolute log modulus at either root is \(g\); the height is half the mean absolute log modulus.
The \(\lambda_j\) have heights tending to zero and escaping degree, so [Bilu's equidistribution theorem](https://doi.org/10.1215/S0012-7094-97-08921-3) and \(z\mapsto z+z^{-1}\) give the arcsine law for their traces.
The trace values stay in a common compact interval, permitting this continuous test function.
If \(f([-2,2])\) leaves \([-2,2]\), the integral is positive, exceeding the required vanishing height scale eventually.
Otherwise the minimax property of the monic Chebyshev polynomial on \([-2,2]\), whose minimum supremum norm is 2 and whose minimizer is unique, forces \(f=\pm 2T_m(X/2)\) for \(m=\deg f\).
Indeed the integer leading coefficient has absolute value at least one, and equality throughout the minimax bound forces the signed minimizer.
The resulting roots are \(\pm\lambda_j^{\pm m}\) with the prescribed sign, so they are multiplicatively dependent with \(\lambda_j\).
Thus the fixed-trace construction cannot supply the second element for (4).
The same obstruction holds for varying integral \(f_j\) of uniformly bounded degree \(L\), even without a bound on their coefficients.
Choose \(L+1\) disjoint compact intervals separated by positive gaps inside \((-2,2)\), each with positive arcsine mass.
If \(h(\nu_j)\to0\), the proportion of embeddings with \(|f_j(\sigma t_j)|>3\) tends to zero by the height formula, whereas each interval contains a positive proportion of the trace conjugates for all sufficiently large \(j\).
Choose a point from each interval where \(|f_j|\le3\).
Interpolation at these \(L+1\) points bounds every coefficient uniformly, since the points are bounded and separated.
Only finitely many integer polynomials can occur.
The fixed-polynomial argument leaves eventually only signed Chebyshev polynomials and constants of modulus at most two, the latter producing roots of unity.

In fact, for every fixed \(L\ge1\) and every sequence of bounded Salem numbers \(\lambda_j\) with \(e_j=[k_j:\mathbb Q]\to\infty\), one eventually has
\[
 \mathcal O_{k_j}\cap\operatorname{span}_{\mathbb Q}\{1,t_j,\ldots,t_j^L\}
   =\operatorname{span}_{\mathbb Z}\{1,t_j,\ldots,t_j^L\},
 \qquad k_j=\mathbb Q(t_j).
\]
To prove this, take \(e_j>L\) and \(y=f(t_j)\in\mathcal O_{k_j}\) with \(f\in\mathbb Q[X]\) of degree at most \(L\).
Let \(q\) be the least positive integer with \(qf\in\mathbb Z[X]\), choose \(C\ge1\) bounding all \(|\sigma t_j|\) in the sequence, and take an integer \(M>\sum_{i=0}^{L} C^i\).
The \(q\) multiples of the coefficient vector of \(f\) indexed by \(0,\ldots,q-1\) are distinct modulo \(\mathbb Z^{L+1}\).
If \(q>M^{L+1}\), two of their representatives in the unit cube belong to the same box of side \(1/M\).
Their difference gives \(0<s<q\) and \(g\in\mathbb Z[X]\) of degree at most \(L\) such that every coefficient of \(sf-g\) has absolute value less than \(1/M\).
Every conjugate of the algebraic integer \(sy-g(t_j)\) then has absolute value less than one, so its norm forces it to vanish.
Since \(e_j>L\), this forces \(sf=g\), contrary to the choice of \(q\).
Thus \(q\le M^{L+1}\) uniformly in \(j\) and \(y\).

Suppose a rational prime \(p\) divides \(q\), and write \(G=qf\).
Minimality of \(q\) gives \(G\bmod p\ne0\), while \(G(t_j)\in p\mathcal O_{k_j}\).
The polynomial \(H=X^LG(X+X^{-1})\bmod p\) has degree at most \(2L\) and is nonzero because the highest Laurent power from the leading term of \(G\bmod p\) survives.
In the full residue ring \(\mathcal O_{\mathbb Q(\lambda_j)}/p\mathcal O_{\mathbb Q(\lambda_j)}\) the relation \(H(\bar\lambda_j)=0\) shows that the subalgebra \(\mathbb F_p[\bar\lambda_j]\) has at most \(p^{2L}\) elements.
Multiplication by \(\bar\lambda_j\) is injective on this finite subalgebra since it is a unit in the full ring.
It is therefore a unit of the subalgebra and has an order \(r<p^{2L}\), allowing nilpotents in the residue ring.
For \(p\ge3\), the absolute norm of the nonzero \(\lambda_j^r-1\) is at least \(p^{2e_j}\) and at most \(2^{2e_j}\lambda_j^r\).
For \(p=2\), write \(\lambda_j^r=1+2w\) with \(w\) integral, so that \(\lambda_j^{2r}-1=4w(w+1)\) has absolute norm at least \(4^{2e_j}\) and at most \(2^{2e_j}\lambda_j^{2r}\).
In both estimates the upper bound uses the single exterior conjugate of a Salem number.
Each fixed \(p\) thus bounds \(e_j\) in terms of \(p,L\) and the upper bound for \(\lambda_j\).
Only finitely many \(p\) can divide the bounded denominator \(q\), so eventually every such \(q\) is one, proving the equality.
There is also a rate for a representative with a genuine denominator.
If \(\lambda_j\le B\), use the monic integral basis \(1,2T_i(X/2)\) for \(1\le i\le L\) in the pigeonhole argument.
The triangular change of polynomial basis preserves the coefficient denominator.
Put \(M=4(L+1)\).
At every nondistinguished embedding each basis value has modulus at most two, so the small box gives a conjugate of absolute value less than \(1/2\).
At the distinguished embedding the corresponding bound is \(B^L+1\), since \(2T_i(t_j/2)=\lambda_j^i+\lambda_j^{-i}\).
For \(e_j>1+\log_2(B^L+1)\) the product is again less than one, giving \(q\le M^{L+1}\); otherwise \(e_j=O_B(L+1)\) already.
In the former case \(\log p\le (L+1)\log(4(L+1))\), and the norm inequalities give \(e_j=O_B(r)\), since \(\log(p/2)\ge\log(3/2)\) for \(p\ge3\).
Together with \(r<p^{2L}\) this gives \(\log e_j=O_B((L+1)^2\log(L+2))\) whenever \(q>1\).
This rate concerns denominators; the bounded-degree obstruction for integer representatives above is qualitative.

Consequently even rational polynomials of uniformly bounded degree producing integral traces fall under the preceding Chebyshev argument.
An independent unit \(\nu_j\) with \(\nu_j+\nu_j^{-1}\in\mathcal O_{k_j}\) and \(h(\nu_j)\to0\) would require the degree of its trace representative in the power basis of \(t_j\) to tend to infinity.
Constructing such a companion within the height budget of (4) remains open here.

<a id="ramification"></a>
**What a ramification sieve or a congruence cover would have to detect.**
Fix one Salem number \(\lambda\) and put \(L=k(\lambda)\).
Any prescribed finite set of finite places of \(k\) can be avoided by the finite ramification of infinitely many quaternion algebras over \(k\) into which \(L\) embeds.
Choose all real places except the distinguished one as ramified places and adjoin one or two distinct finite primes inert in \(L/k\), outside the prescribed set, to make the total number even.
There are infinitely many choices by the prime splitting theorem for a quadratic extension.
The classification and embedding criterion for quaternion algebras give the claim, since no ramified place splits in \(L\). [Linowitz, McReynolds, Pollack and Thompson, Section 2](https://doi.org/10.4310/MRL.2017.v24.n5.a8)
A maximal order can be chosen containing \(\mathcal O_L\): in a presentation \(L+Lj\), scale \(j\) to make \(j^2\) integral, take the order \(\mathcal O_L+\mathcal O_Lj\) and extend it to a maximal order.
The norm-one element \(\lambda\) then gives a closed geodesic of length \(2\log\lambda\) for the associated Fuchsian lattice, counting iterates if the element is imprimitive.
The orbifold is compact because there is finite ramification.
Lemma 2.1 of the same paper selects a torsion-free cover retaining the geodesic (or its underlying primitive geodesic).
This gives a surface systole at most \(2\log\lambda\) and explains why a sieve confined to one fixed list of finite primes cannot eliminate the same eigenvalue in all ambient algebras.
It uses the norm-one matrix convention; Douba and Huang obtain the exact systole \(\log\lambda\) by their own realization.

In a principal congruence cover, lifting a given geodesic can instead require a power.
For a fixed first-type arithmetic subgroup of \(\mathrm{Spin}(1,n)\), Murillo's Theorem 6.1 gives \(\operatorname{sys}(M_I)\ge 8\log\operatorname{vol}(M_I)/(n(n+1))-c\) at sufficiently large admissible levels.
The excluded finite set of primes and the additive constant can depend on the initial arithmetic data.
If the shortest power of the chosen element lying in the cover subgroup is \(r\), the length available for comparison upstairs is \(r\) times its length downstairs. [Theorem and normalization](../audits/literature/Mur19b/readme.md)
Even in the maximal order of the number field the return exponent need not be linear in degree at bounded Mahler measure.
Let \(r\) be the order of a nontorsion unit \(\alpha\) modulo \(2\mathcal O_{\mathbb Q(\alpha)}\).
Then \(\alpha^{2r}-1\in4\mathcal O_{\mathbb Q(\alpha)}\) and is nonzero.
Taking its absolute norm gives \(4^d\le2^d M(\alpha)^{2r}\), hence \(r\log M(\alpha)\ge d\log(2)/2\); compare the [binary resultant criterion in the power order](../claims/Yin_C_G0345_v166.md#statement).
On the [cubic-pole Salem family](../claims/Yin_C_G0901_v195.md#cubic), \(n=2^k\) runs through the specified subsequence, \(d=n-2\), and \(X^nP-P^*=(X^5-1)S_n\) for \(P=X^3-X-1\).
Squarefree reduction at two makes the power order maximal there and \(\overline P,\overline P^*,X\) are pairwise coprime.
Write \(r=an+b\) with \(a\ge0,\ |b|\le n/2\).
Modulo two, \(S_n\) divides \(X^{\max(b,0)}(P^*)^a-X^{\max(-b,0)}P^a\) by the two power identities in the residue ring.
The polynomial is nonzero by coprimality when \(a>0\), and by \(r>0\) when \(a=0\).
Its degree is at most \(n/2+3a\).
Consequently \(a\ge(n/2-2)/3\) and \(r\ge n(n-7)/6\).
These genuine Salem numbers converge to the plastic number from below, so the obstruction to fast dyadic return reaches that bounded-measure family.
Whether a degree-linear return, or a different small-height second element, is forced specifically along a sequence tending to one remains open.

<a id="geometric-tools"></a>
## Degrees of integral trace constructions and return to a reflection group

For a bounded Salem number of degree \(2e\), an integral trace construction of an independent unit at the height scale in (4) requires polynomial degree \(\gg(\log(12e))^{212}\). [Trace-degree statement and proof](../claims/Yin_C_G0901_v199.md#trace-proof)
A separate [Leech lattice example](../claims/Yin_C_G0901_v199.md#reflection) has a degree-four Salem spectral radius and no positive power in the root-reflection group.
The remaining question is whether a sequence approaching one supplies either a sufficiently small independent companion of growing trace degree or a Coxeter realization with controlled power.

<a id="mapping-tori"></a>
## Realizing the whole record polynomial in a hyperbolic three-manifold

The [closed mapping-torus construction](../claims/Yin_C_G0883_v2.md#mapping-tori) realizes every late reciprocal record in the original cyclic homology tower.

<a id="bounded-volume"></a>
### The unresolved volume range

The [finite-parent and torsion argument](../claims/Yin_C_G0883_v2.md#bounded-volume) gives a gap at each fixed volume ceiling, including zero intersection with filling cores.
The [cyclotomic support estimate](../claims/Yin_C_G0883_v3.md#statement) bounds that minimum below, while the [coefficient positions](../claims/Yin_C_G0883_v4.md#upper-bound) give a constructive upper bound.
In the [circle-of-handles realization](../claims/Yin_C_G0883_v5.md#positions), a common unit modulo \(g\) can move several active coefficient positions near zero.
For a single active position, compression makes its residue invertible and this removes the entire logarithmic cost.
There are [irreducible two-position controls](../claims/Yin_C_G0883_v6.md#positions) with each index invertible and a complete return modulo two whose least sum of cyclic distances is exactly \(\sqrt g\).
Their measure exceeds two, leaving the small-measure requirement available for a genuine record argument.
For \(s\) occupied positions, counting the two possible residues at each distance gives a [quadratic lower bound on the sum of separate costs](../claims/Yin_C_G0883_v6.md#many).
In the [joint realization](../claims/Yin_C_G0883_v7.md#support) a whole interval of inactive handles rotates as a single block and a fixed drilled layer handles each active index.
It gives \(V_{\min}(P)\le C(1+s)\) for the whole polynomial with an absolute constant.
One can ask whether a sparse cyclotomic multiple can realize the same closed polynomial by capping, as happens in the [closed-fiber specialization](../claims/Yin_C_G0883_v5.md#hironaka).
If the open polynomial has a signed binomial divisor modulo a prime, the [overlap with its boundary factor](../claims/Yin_C_G0904_v6.md#boundary) imposes a necessary condition on the boundary periods.
The [boundary inversion and orbit test](../claims/Yin_C_G0883_v8.md#cycles) determine the only possible cycle counts and give a sufficient way to realize them.
The [six-term minimum for Lehmer's \(L(x)\)](../claims/Yin_C_G0883_v8.md#lehmer) is attained by puncturing two fixed points, while a [five-term open fiber](../claims/Yin_C_G0883_v8.md#partial) caps to \(L(-x)\).
For a choice of closed monodromy with the prescribed homological action, [filling orbits and a bounded number of twists per cycle](../claims/Yin_C_G0883_v9.md#filling) realize every boundary profile.
The open volume is \(O(1+s(P)+t)\) for \(t\) cycles, independently of their lengths.
One can [correct any sparse cyclotomic completion](../claims/Yin_C_G0883_v11.md#correction) by binomials whose number is bounded in terms of the original support.
When \((x-1)P\) has four terms the [open volume is bounded absolutely](../claims/Yin_C_G0883_v10.md#four), including on an explicit dense Salem family.
For shrinking records, the admissible support must grow, and volume control linear in that support for dense \(P\) remains open.
A lift can have arbitrarily large volume with every homology group in the original tower fixed.
