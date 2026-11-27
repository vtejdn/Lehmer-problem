---
author: Yin
---

# What local degrees, residue periods and short orbits detect in the Lehmer problem

This working draft investigates the [unrestricted gap](../tasks/Yin_T_G0001_v1.md#contract) on four families of objects.
The deductions below are author-side calculations.
The cited source theorems and fixed project results retain their own scopes.

<a id="records"></a>
## Which primes carry the norm of a translate between adjacent records?

Suppose the unrestricted gap is zero.
Use [two adjacent strict degree records](../claims/Yin_C_G0901_v165.md#statement), put \(A=A_i,\ B=A_{i+1},\ b=\log B,\ K=\mathbb Q(A),\ F=K(B)\), and write \(n=[F:K],\ D=[F:\mathbb Q]\).
For \(z=2-A^aB\) take the second closest allowed exponent from below.
The known norm calculation gives \(D^{-1}\log|N_{F/\mathbb Q}z|\to\log 2\).
We ask where this mass can occur among the primes of \(F\).

For a prime ideal \(Q\) of \(F\) over \(\mathfrak p\) of \(K\), let \(s_Q=[F_Q:K_{\mathfrak p}]=e_Q f_Q\), where both local indices are relative to \(K\).
Give \(Q\) weight \(w_Q=D^{-1}v_Q(z)\log NQ\), using integer ideal valuations and the absolute ideal norm.
For sufficiently late rows one has
\[
   \sum_Q w_Q\,\frac{s_Q-1}{n-1}\ \ll\ \sqrt{b\log(1/b)}. \tag{1}
\]
In particular, at any fixed \(\delta>0\) the primes with \(s_Q\ge\delta n\) carry \(o(1)\) mass, while the total mass tends to \(\log 2\).
Here the [relative degrees](../claims/Yin_C_G0901_v159.md#orbits) tend to infinity.
The estimate weights each prime by its contribution to this particular translate.

To prove (1), take a normal closure of \(F/K\) and list the \(n\) relative images \(B_j\) of \(B\).
For \(j\ne k\), \(B_j/B_k\) is a nontorsion unit of absolute height at most \(2b\).
Indeed an embedding taking \(B_j\) to the strictly dominant \(B\) takes \(B_k\) to a different conjugate, and all conjugates of \(B\) have modulus at most \(B\).
Set \(z_j=2-A^aB_j\).
The common ideal \((z_j,z_k)\) divides \((B_j/B_k-1)\) since \(A,B_k\) are units.
The [cyclic norm estimate](../claims/Yin_C_G0345_v730.md#statement) bounds its log norm divided by the absolute degree of the normal field by \(O(\sqrt{b\log(1/b)})\), uniformly in \(j,k,a\).
This is the same two-conjugate estimate used for the [window of translates](../ledger/Yin_L_G0462_v326.md#descent).

Average over ordered distinct embeddings \(j,k\).
At a fixed prime of the normal field above \(\mathfrak p\), exactly \(s_Q\) of the \(n\) embeddings induce the place \(Q\).
This follows by decomposing \(F\otimes_K K_{\mathfrak p}\) into its field factors and counting the embeddings of each factor.
When both embeddings induce \(Q\), their valuations of the translates are equal, so the common ideal retains their whole local contribution.
Given the first embedding, the fraction of other embeddings with the same place is \((s_Q-1)/(n-1)\).
Summing the normalized log norms over the primes upstairs and averaging the first embedding recovers \(w_Q\) by the local degree formula.
Pairs inducing different places contribute nonnegative terms.
This proves (1).

The estimate singles out a difficulty in seeking a contradiction by showing that translate norms are large.
Away from primes dividing the index of \(\mathcal O_K[B]\) in \(\mathcal O_F\), a prime dividing \(z\) already has \(f_Q=1\), since \(B\bmod Q=2A^{-a}\bmod\mathfrak p\) generates its residue field over that of \(K\).
Away also from the relative discriminant, such primes have \(s_Q=1\) and contribute zero to the left side of (1).
A comparison between different record rows would need information on these degree-one primes or on the exceptional prime contributions.
The upper bound (1) supplies neither a positive lower bound on the exceptional mass nor an exclusion of the one-sided record limit.

<a id="trace"></a>
## Completing the second residue period on the one-denominator controls

Fix a sufficiently large row of the [full even-modulus construction](../claims/Yin_C_G0901_v196.md#combine).
Use its multiple \(q\) of four, \(p=q+1,\ J=q/2+1,\ d=2D,\ u=2^h,\ A=tn\) and \(C=\operatorname{lcm}(q,2^h)\).
Here \(h\) is the binary precision chosen before the degree and \(t>p\) is the odd prime used for the substitution \(V(Z^t)\).
Choose the allowed denominator prime \(\ell\) prime to \(Cp\).
Retain the row's coefficient word modulo \(C\), including its full order \(A=v-u\), pole \(K_0=(2q+1)^2\), real root conditions and zero low and high offsets through \(J\).
The required order at \(p\) for a [genuine integral solution](../claims/Yin_C_G0901_v177.md#statement) is \(N=A+2u\).

For this row the one-denominator control extends to this second order exactly when there exists a monic reciprocal degree-\(d\) polynomial \(W\) over \(\mathbb Z/p\mathbb Z\) with constant one, zero offsets \(1,\ldots,J\), order \(N\) for \(Z\bmod W\), and coefficient
\[
 [Z^{J+1}]W\equiv
 q^{-(d-J-1)}\frac{K_0-q^d}{p^{J+1}}\pmod p. \tag{2}
\]
The numerator is divisible by \(p^{J+1}\) on the chosen row.
Expanding \(q^d F(p/q)\) modulo \(p^{J+2}\) proves necessity, since exactly the constant term and offset \(J+1\) can contribute.

For sufficiency glue \(W\) and the given word modulo \(C\) coefficientwise by the Chinese remainder theorem with the endpoints and zero prefix fixed over the integers.
At the \(q\)-side the stronger modulus \(Cq^{J+1}\) still gives the old pole congruence: changing coefficients by multiples of \(C\) in the free positions changes the evaluation by multiples of \(C(pq)^{J+1}\).
At the \(p\)-side (2) gives the pole congruence modulo \(p^{J+2}\).
The two conditions give divisibility of the pole discrepancy by \(Cp(pq)^{J+1}\).
The [gcd of the values of the free reciprocal basis](../claims/Yin_C_G0901_v172.md#congruences) is \((pq)^{J+1}\).
Correcting by \(Cp\) times this lattice therefore hits the pole exactly.
The [one-prime approximation and irreducibility argument](../claims/Yin_C_G0901_v172.md#place) with residue modulus \(Cp\) preserves both words throughout the same nonempty real neighborhood.
Thus the remaining existence question for this model is a finite-ring question at each specified row.
Even complete period matching on this construction leaves the denominator at \(\ell\) and the characteristic-zero power relation unresolved for integral solutions.

The substitution used on the even side cannot simply be used on the other side.
Choose a prime \(r\mid p\).
If \(W\bmod r=V(Z^t)\) with \(V\) nonconstant and with nonzero constant term, its nonzero roots include \(\alpha,\zeta_t\alpha\) in an algebraic closure, for \(\zeta_t\) of order \(t\), since \(r\ne t\).
Divisibility by \(Z^N-1\) forces \(t\mid N\), whereas \(N=tn+2u\) is prime to \(t\).
A second-period word must therefore break this substitution, even after reduction at each prime of \(p\).
For composite \(p\), a direct test over the entire ring is \(W\mid Z^N-1\) and \(W\nmid Z^{N/s}-1\) for every prime \(s\mid N\), with (2) imposed.
Single-prime reductions alone can miss the order at a prime power.

<a id="short-period-divisor"></a>
### A divisor of small degree carrying the entire second period

Fix the eligible \(q,h,\ell,t\) above and \(0<\varepsilon<1\), and put \(\theta=u\log p/\log(p/q)\).
There are arbitrarily large rows with all the even-modulus, dyadic-degree and real tests above in which the reduction of the same \(F\) modulo \(p\) contains a monic reciprocal divisor of degree less than \(\varepsilon d\) and exact order \(N\).
Thus \(N\) divides the order of \(Z\) in the full degree-\(d\) quotient modulo \(p\).
The bound on the real-period error is uniform along each chosen sequence and may depend on \(\varepsilon\).

First choose a prime \(\rho>\max(p,t,11,J+1,2\theta/\varepsilon)\) dividing some \(15t\,11^{j_0}-4u\), \(j_0\ge1\).
Such primes are unbounded: start with any positive value of this expression and keep its valuation at every prime up to the proposed bound fixed by restricting \(j\) to an arithmetic progression.
For each such prime \(s\ne11\) use the order of \(11\) modulo \(s^{1+v_s(15t\,11^{j_0}-4u)}\) at the starting exponent; the valuation at \(11\) is always zero.
The values on the progression grow without bound.
Let \(e=v_\rho(15t\,11^{j_0}-4u)\), \(R=\rho^e\) and \(Q=\rho^{e+1}\).
Use the [original period construction](../claims/Yin_C_G0901_v196.md#practical), with \(a\equiv-1\) modulo both its prescribed modulus and \(\operatorname{ord}_Q(2)\).
Also require the original maximal exponents \(j,k\) there to satisfy
\[
   j\equiv j_0\bmod \operatorname{ord}_Q(11),\qquad
   k\equiv0\bmod \operatorname{ord}_Q(7).
\]
Since \((2^a-1)(2^{a+2}-1)\equiv-1/2\bmod Q\), these choices give \(2N\equiv4u-15t\,11^{j_0}\bmod Q\).
Hence \(R\mid N\) and \(\rho\nmid N/R\).

To verify that the maximal exponents attain the required residues, write \(a=Hm-1\) in the chosen progression, \(x=a\log2-2\log a-\log100\), \(b_1=\operatorname{ord}_Q(11)\) and \(b_2=\operatorname{ord}_Q(7)\).
The defining formulas are \(j=1+\lfloor(x-\log10)/\log11\rfloor\) and \(k=1+\lfloor(x-\log3)/\log7\rfloor\).
The points \((x/(b_1\log11),x/(b_2\log7))\) modulo one are equidistributed with weights \(1/m\).
Indeed a nontrivial Fourier character has frequency \(\lambda=i/(b_1\log11)+j'/(b_2\log7)\ne0\), since \(7\) and \(11\) are multiplicatively independent.
If \(\lambda H\log2\notin\mathbb Z\), the geometric sums in \(m\) are bounded and the successive differences of \((Hm-1)^{-4\pi i\lambda}/m\) are summable.
If \(\lambda H\log2\in\mathbb Z\), the character sum with these weights differs by \(O(1)\) from a constant times \(\int_1^X y^{-1-4\pi i\lambda}\,dy\), which is bounded.
Thus each nonconstant weighted Fourier mean tends to zero after division by \(\sum_{m\le X}1/m\).
Trigonometric approximation gives positive limiting mass to the interiors of the intervals specifying both floor residues, so the original block sizes occur on infinitely many such rows.

In the [degree progression](../claims/Yin_C_G0901_v189.md#period) strengthen the endpoint congruence to \((1-p)^D\equiv1-2p\bmod p^{J+2}\).
The [principal-unit construction](../claims/Yin_C_G0901_v172.md#congruences) still gives a progression \(D_0\bmod P\) whose prime divisors in \(P\) are at most \(p\), and (2) now prescribes zero.
Choose \(S\) nearest \(n/(2\theta)\) subject to \(tS\equiv D_0\bmod P\) and \(R\mid S\).
These congruences are compatible and give \(d=2tS\), \(R\mid d\), and \(|A-\theta d|\le\theta tPR\).
For this fixed \(R\) the additional rounding error is bounded as \(a\) grows, so the original [dyadic block filling](../claims/Yin_C_G0901_v196.md#binary) and [real-period estimate](../claims/Yin_C_G0901_v189.md#arch) apply.

Write \(w=N/R\) and \(E_b(Z)=1+Z+\cdots+Z^{b-1}\).
The integer reciprocal polynomial \(U=E_wE_R\) divides \(Z^N-1\), since \(\gcd(w,R)=1\) and the two geometric sums have disjoint cyclotomic factors.
Over \(\mathbb Z/p\mathbb Z\), \(E_b\) has exact order \(b\) for \(b\ge3\): it divides \(Z^b-1\), has degree \(b-1\), and differs from \(Z^{b-1}-1\) in an intermediate coefficient.
Consequently \(U\bmod p\) has exact order \(N\), even at composite \(p\).
Its degree is \(w+R-2\), with \((w+R-2)/d\to\theta/R<\varepsilon\).
For sufficiently large rows choose a monic reciprocal \(G\bmod p\) of the remaining even degree whose coefficients through \(J+1\) agree at zero with \(1/U\).
This is possible by setting the low coefficients and reflecting them into the disjoint high positions.
The polynomial \(W=UG\) now has the required zero offsets through \(J+1\).
The coefficient gluing and exact pole correction above, followed by approximation with denominator prime \(\ell\nmid Cp\), preserve \(W\bmod p\) while retaining the full order \(A\) modulo \(q\).

For this prescribed divisor \(U\), test whether the monic reciprocal factors of \((Z^N-1)/U\bmod p\) include a \(G\) of degree \(d-\deg U\) with those specified low coefficients.
Such a factor would give the full order \(N\); the free completion just constructed only proves divisibility of the full order by \(N\).
An additional sufficient test uses \(R\mid d,N\): a monic reciprocal polynomial of degree \(d/R\), constant one and exact order \(N/R\) modulo \(p\) yields a complete word by substituting \(Z^R\).
Its first \(J+1\) offsets vanish, and the substitution multiplies the order by \(R\), as is seen from the free basis \(1,Z,\ldots,Z^{R-1}\) over the quotient in \(Z^R\).

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
**A finite-time observable for arbitrary irreducible unit companions.**
Use the convention that \(A^\mathsf T\) acts as multiplication by \(\alpha\) on the power basis of \(\mathbb Z[\alpha]\), where \(P\) is the degree-\(d\) minimum of a nontorsion unit \(\alpha\).
Write \(N_j=|\det(A^j-I)|\) and \(r_j=\min\{\|k\|_\infty:0\ne k\in ((A^\mathsf T)^j-I)\mathbb Z^d\}\).
The integer \(r_j\) is the first nonzero Fourier frequency on which averaging over \(\operatorname{Fix}(A^j)\) differs from Haar integration, by finite-group character orthogonality.
For every \(j\ge1\),
\[
 \frac{N_j^{1/d}}{d\,M(P)^{1-1/d}}\ \le\ r_j\ \le\ \lfloor N_j^{1/d}\rfloor . \tag{3}
\]
The upper bound follows by taking integer vectors in a cube of side \(\lfloor N_j^{1/d}\rfloor+1\) modulo a sublattice of index \(N_j\).
For a vector in that sublattice, the corresponding polynomial value \(V(\alpha)=\sum_{l<d}k_l\alpha^l\) lies in \((\alpha^j-1)\mathbb Z[\alpha]\).
For nonzero \(k\), its nonzero absolute field norm is at least \(N_j\) and at most \((d\|k\|_\infty)^d M(P)^{d-1}\), by multiplying the individual archimedean bounds.
This proves (3).
The fixed-polynomial periodic point growth formula gives \(\lim_{j\to\infty} j^{-1}\log r_j=(\log M(P))/d\), including algebraic nontorsion eigenvalues on the circle. [Lind, Section 4](../audits/literature/Lin82/readme.md)
Thus a degree-independent lower bound for the raw rate would already fail for bounded-measure Salem polynomials of growing degree.
For a finite-time test returning to total measure one must recover the factor \(d\), control the error up to \(d\log d+(d-1)\log M(P)\) in (3), and estimate the neutral factors in \(N_j=\prod_i|\alpha_i^j-1|\) at the chosen time.

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
