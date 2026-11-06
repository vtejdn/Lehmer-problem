---
author: Yin
---

# Moving odd-conductor square layers and the sublinear-factor criterion

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating contributor proposed the odd-prime family and the actual-factor binary period and endpoint refinements.
The construction contributor derived the fixed integer template, complete cyclotomic exclusion, uniform root-height bound and resulting factor-degree criterion, and assembled the arguments below.
The bottleneck contributor developed the changing relative-zero-power comparison, its exact zero-cost baseline, deletion template, complete measure bounds and Newton-sum positivity proof, and retained the single exact factorization in J143.
These are ordinary author-development contributions, not an independent project review, a new Claim assessment or a counterexample to the Task.

<a id="prime-square-family-scope"></a>
## Fixed predecessors and the new input

[V3](Yin_L_G0458_v3.md#cyclotomic-square-factorwise-residue-filter) retains the complete content-two generator and its bounded-odd-order factor filter.
The present family lets the odd conductor grow, so its input is not covered by a single constant M in that filter.
This does not by itself supply a small factor.
The new calculation identifies a fixed bivariate template, excludes every cyclotomic factor and makes small total measure of an actual factor equivalent to its degree being sublinear in the prime parameter.
The separate [dyadic deletion comparison](#dyadic-deletion-inputs) changes the odd part of a relative zero-root power instead of the input conductors.
It supplies bounded positive complete cost after a zero-cost baseline, but no global factor-growth theorem or analogue of the prime-family sublinear-degree equivalence.

The full measure and content conventions remain those of [v2](Yin_L_G0458_v2.md#moving-zero-measure-pair-scope).
All irreducible factors below are actual monic integer factors, and all complete-output sums retain their multiplicities.
No degree-normalized height is substituted for the original Lehmer target.

<a id="prime-square-family-inputs"></a>
## The integral odd-prime family

For an odd prime p set
\[
 A_p=(z-1)\Phi_{8p}(z),\qquad
 B_p=(z+1)\Phi_{4p}(z)^2,\qquad
 H_p=(A_p^2+B_p^2)/2.
 \tag{P1}
\]
The exact cyclotomic quotient identities are
\[
 \Phi_{8p}(z)=\frac{z^{4p}+1}{z^4+1},\qquad
 \Phi_{4p}(z)=\frac{z^{2p}+1}{z^2+1}.
 \tag{P2}
\]
Thus A_p and B_p are coprime monic cyclotomic products of degree 4p-3, with constant coefficients -1 and 1.
Their binary reductions both equal
\[
                 (z+1)\overline{\Phi_p}^{\,4}.
\]
The [content-two calculation in v3](Yin_L_G0458_v3.md#cyclotomic-square-content-and-reversal) therefore applies exactly.
In particular H_p is the primitive integer output, is monic reciprocal, and satisfies
\[
 \deg H_p=8p-6,\qquad H_p(0)=1,\qquad
 \overline H_p=(z+1)^2\overline{\Phi_p}^{\,8}.
 \tag{P3}
\]
Every irreducible factor is a monic algebraic-unit polynomial.

Direct evaluation in (P2) gives
\[
 H_p(1)=H_p(-1)=2,\qquad
 \Phi_{8p}(i)=1,\qquad \Phi_{4p}(i)=p,\qquad
 H_p(i)=i(p^4-1)\ne0.
 \tag{P4}
\]
For the removable value at i, write t=z^2 in (t^p+1)/(t+1); its value at t=-1 is p for odd p.
Also H_p has no real root, because A_p and B_p are real polynomials with no common root and their squared sum is strictly positive on the real axis.

<a id="prime-square-fixed-template"></a>
## A fixed integer template with all denominator costs retained

Put
\[
 D(z)=(z^4+1)(z^2+1)^2,
\]
\[
 L_1(z)=(z-1)^2(z^2+1)^4,\qquad
 L_2(z)=(z+1)^2(z^4+1)^2,
\]
and define the fixed polynomial
\[
 \mathcal G(z,t)
 =\frac{L_1(z)(t^2+1)^2+L_2(z)(t+1)^4}{2}.
 \tag{P5}
\]
This belongs to Z[z,t].
Indeed both L_1 and L_2 reduce to (z+1)^10, while (t^2+1)^2 and (t+1)^4 also agree in characteristic two.
Its coefficient of z^10 t^4 is one, so it is primitive.
The exact cleared identity is
\[
                       \mathcal G(z,z^{2p})=D(z)^2H_p(z).
 \tag{P6}
\]
One may verify it before squaring by multiplying A_p and B_p by D in (P2).

The factor D is monic cyclotomic and has zero logarithmic measure.
Thus no scalar content or denominator cost is discarded in
\[
                       m(H_p)=m(\mathcal G(z,z^{2p})).
 \tag{P7}
\]
For the coefficient one-norm, the two summands in the numerator of (P5) each have norm at most 256.
Division by two gives
\[
               \|\mathcal G\|_1\le256,\qquad
                         m(H_p)\le8\log2.
 \tag{P8}
\]
This is the complete output measure, not a measure of one selected real root.

The accepted full [Lawton interface in Den09 U002](../audits/literature/Den09/Yin_U002.md), Theorem 14 and Example 15, applies to the fixed polynomial G and the specialization vector (1,2p).
Its least nonzero integral relation has sup norm 2p.
The theorem includes polynomials with zeros, rather than only the separately discussed nonvanishing case.
Consequently
\[
                       m(H_p)\longrightarrow m_2(\mathcal G).
 \tag{P9}
\]
No numerical value of this two-variable integral is asserted.
A positive lower bound for it follows below from the actual-factor arithmetic.

<a id="prime-square-no-cyclotomic-factors"></a>
## Complete exclusion of cyclotomic factors

The conductor reduction in [v3](Yin_L_G0458_v3.md#cyclotomic-square-conductor-parameterization) says that the roots of the binary reduction of Phi_(2^k m), for odd m, have exact odd order m.
Equation (P3) therefore restricts a possible cyclotomic factor of H_p to an index 2^k or 2^k p.

For pure powers of two, the total multiplicity two at the binary root one restricts the possible indices to 1,2,4.
All three are excluded by (P4).

For the indices 2^k p, the multiplicity eight of each root of bar(Phi_p) gives phi(2^k)<=8, hence k<=4.
When k=2 or k=3 the candidate is an input factor Phi_(4p) or Phi_(8p).
Such a root cannot lie in H_p, because A_p and B_p are coprime.

For k=0 or k=1, respectively z^p=1 or z^p=-1 on the candidate cyclotomic roots.
Then z^(2p)=1, and (P5)--(P6) show that the candidate must divide
\[
                    J(z)=L_1(z)+4L_2(z).
\]
Here division of G(z,1)=2J by the scalar two is harmless over Q.
But J is an integer polynomial with
\[
                          \overline J=(z+1)^{10}.
\]
A monic cyclotomic divisor has an integer quotient.
Its binary reduction would force a root of exact order p to be a root of (z+1)^10, which is impossible.
This excludes Phi_p and Phi_(2p).

Finally, suppose Phi_(16p) divided H_p.
Its degree is 8p-8, so the quotient would be a monic reciprocal quadratic with constant coefficient one.
Also
\[
 \Phi_{16p}(z)=\frac{z^{8p}+1}{z^8+1},\qquad
 \Phi_{16p}(1)=1.
\]
The quotient has value two at one by (P4), and must therefore equal z^2+1.
That contradicts H_p(i) nonzero.
These cases exhaust all possible cyclotomic factors.

Thus every irreducible factor of H_p is noncyclotomic and has positive logarithmic measure.
Their degrees, counted with all multiplicities, sum to 8p-6.
No all-p irreducibility or squarefreeness of H_p has been assumed or established.

<a id="prime-square-original-factor-cost"></a>
## The original factor degree pays the binary period

Since p is odd, z^p-1 is squarefree in F_2[z] and equals (z+1)bar(Phi_p).
Equation (P3) gives
\[
                   \overline H_p\mid(z^p-1)^8=z^{8p}-1.
\]
Let f be any actual irreducible factor, let e=deg f, and let beta be a root.
Lifting polynomial divisibility yields
\[
               (\beta^{8p}-1)/2\in\mathbb Z[\beta]
                                     \subset O_{\mathbb Q(\beta)}.
 \tag{P10}
\]
The input beta is a nontorsion algebraic unit by the preceding cyclotomic exclusion.

Apply [C864 v2, original binomial norm return](../claims/Yin_C_G0864_v2.md#original-binomial-norm-return), equations (BP13)--(BP14), with the original degree e and period 8p.
The source allows full-ring integrality and does not require that taking powers preserve degree.
Explicitly, v=(beta^(8p)-1)/2 and v+1 are nonzero integral elements, so
\[
 (\beta^{16p}-1)/4=v(v+1),\qquad
 4^e\le\left|N_{\mathbb Q(\beta)/\mathbb Q}
                       (\beta^{16p}-1)\right|
       <2^e\exp(16p\,m(f)).
\]
The strict upper bound uses all original conjugates and a conjugate off the circle.
It follows that
\[
                         m(f)>\frac{e\log2}{16p}.      \tag{P11}
\]
This is a factor-degree bound, not a constant gap when e/p is allowed to decrease.

Summing over every actual factor gives the complete lower cost
\[
                         m(H_p)>
                         \frac{(8p-6)\log2}{16p}.      \tag{P12}
\]
Combining with (P8)--(P9) proves
\[
                 \frac{\log2}{2}\le m_2(\mathcal G)\le8\log2.
 \tag{P13}
\]
The whole family therefore has bounded positive measure approaching a positive limit.
This does not prohibit small individual factors.

<a id="prime-square-root-height-upper"></a>
## A uniform upper height bound for every actual root

Regard G(z,t) as a polynomial in t.
Its coefficients at t^3 and t^2 are
\[
                         2L_2,\qquad L_1+3L_2.
\]
The polynomials L_1 and L_2 have disjoint root sets: the former vanishes only at 1 and the primitive fourth roots, and the latter only at -1 and the primitive eighth roots.
Thus the coefficients of G(beta,t) cannot all vanish at any beta.
For an actual root beta of H_p, the nonzero polynomial G(beta,t) has beta^(2p) as a root.

Every coefficient polynomial in z has degree at most ten and coefficient one-norm at most 256.
For its nonzero projective coefficient vector c(beta), the usual local evaluation bounds give
\[
                         h(c(\beta))\le10h(\beta)+8\log2.
 \tag{P14}
\]
At a finite place, integral coefficients give the maximum-norm bound without the logarithmic constant.
At an archimedean place, the coefficient one-norm supplies the factor 256.
The normalized place weights give exactly (P14).

For a nonzero polynomial with a root w, the local Cauchy bound gives
\[
                         h(w)\le h(\text{coefficient vector})+\log2.
 \tag{P15}
\]
For completeness, choose the actual highest nonzero coefficient c_j.
At a finite place, max(1,|w|) is at most max_i|c_i|/|c_j|.
At an archimedean place it is at most twice that ratio.
Summation removes log|c_j| by the product formula.
The assertion therefore also covers a specialization at which the original top coefficient vanishes.

Using w=beta^(2p) in (P14)--(P15) gives
\[
                  2p\,h(\beta)\le10h(\beta)+9\log2.
\]
Hence, for every prime p>5 and every actual factor,
\[
                h(\beta)\le\frac{9\log2}{2p-10},\qquad
                m(f)\le\frac{9e\log2}{2p-10}.          \tag{P16}
\]
These constants are independent of the chosen factor and of p.

<a id="prime-square-sublinear-factor-criterion"></a>
## The exact remaining small-factor criterion

Together, (P11) and (P16) give
\[
              \frac{e\log2}{16p}<m(f)
                    \le\frac{9e\log2}{2p-10}
                 \qquad(p>5).                        \tag{P17}
\]
Thus along any sequence of actual factors with p tending to infinity,
\[
                    m(f_p)\longrightarrow0
       \quad\Longleftrightarrow\quad
                    \deg(f_p)/p\longrightarrow0.      \tag{P18}
\]
Both implications are uniform over factors.
The bounded complete cost in (P8) does not supply the degree condition.

Any positive-to-zero sequence extracted from this family must use unbounded primes, since finitely many parameter values supply only finitely many positive factor measures.
Moreover its factor degrees must tend to infinity.
Otherwise (P16), bounded degree and Northcott finiteness would leave a fixed finite set of possible roots with positive height, contradicting convergence to zero.
This is consistent with, and does not prove the existence of, sublinear degree growth.

<a id="prime-square-residue-degree"></a>
## Gaussian integrality sharpens the residue-degree restriction

At any root beta, coprimality gives B_p(beta) nonzero and
\[
                         A_p(\beta)/B_p(\beta)=\pm i.
\]
Consequently Q(i) is contained in Q(beta).
For the monic Q(i)-minimal polynomial q of a chosen root above i, integrality gives q in Z[i][z].
The actual field degrees show, exactly as in [v3](Yin_L_G0458_v3.md#gaussian-exception-source-boundary), that
\[
                              f=q\overline q.
\]
Writing q=U+iV with U,V in Z[z] gives
\[
                              \overline f=(\overline U+\overline V)^2
                              \quad\text{in }\mathbb F_2[z].
 \tag{P19}
\]
The leading coefficient of q is one, so the square retains the full degree.
Every binary irreducible factor of f therefore occurs with even multiplicity.

Put rho_p=ord_p(2).
Every irreducible factor of bar(Phi_p) has degree rho_p: Frobenius sends a primitive p-th root xi to xi^2, and the orbit returns precisely when 2^k=1 modulo p.

An actual factor cannot reduce only to a power of z+1.
Equation (P3) would give e<=2, while Q(i) is already a subfield of its root field.
The only possible degree would be two, and an algebraic-integer unit in Q(i) is one of its four roots of unity.
That contradicts the complete cyclotomic exclusion.

Every actual factor therefore contains an irreducible factor of bar(Phi_p), with multiplicity at least two by (P19).
In particular
\[
                  e\ge2\rho_p,\qquad
                  m(f)>\frac{\rho_p\log2}{8p}.        \tag{P20}
\]
If rho_p/p has a fixed positive lower bound along the selected primes, this is a uniform positive-factor gap.

There is a more precise degree partition.
Exactly one rational irreducible factor f_* contains the binary root one, with multiplicity two in its reduction.
It has multiplicity one in H_p because the total such multiplicity in (P3) is two.
The square reductions give
\[
 \deg f_*=2+2\rho_p a_*,\quad a_*\ge1,\qquad
 \deg f_i=2\rho_p a_i,\quad a_i\ge1
\]
for all other factors.
Here repeated appearances of those other factors are retained when summing degrees.
Since the degree sum is 8p-6=8(p-1)+2,
\[
                           r_+(H_p)\le\frac{4(p-1)}{\rho_p}.
 \tag{P21}
\]
Thus a small-measure construction must satisfy both rho_p/p tending to zero and the actual sublinear global-factor condition (P18).
A small residue degree is only a local necessary condition; it does not produce a factor of the suggested degree over Q or Q(i).

<a id="prime-square-endpoint-budget"></a>
## The unique factor carrying the endpoint cost

The entire Gaussian fiber can be normalized as
\[
 Q_p=\frac{A_p-iB_p}{1-i}
    =\frac{A_p+B_p}{2}
       +i\frac{A_p-B_p}{2}.
\]
It is a monic polynomial in Z[i][z], of degree 4p-3 and constant coefficient -i.
For pi=1-i its reduction is
\[
                  \overline Q_p=(z+1)\overline{\Phi_p}^{\,4}
                  \quad\text{over }\mathbb F_2,
\]
because i reduces to one and the two integral halves add to A_p.
Also
\[
                         Q_p(1)=\pi,\qquad Q_p(-1)=-i\pi.
 \tag{P22}
\]

Factor Q_p into its actual monic irreducible Gaussian factors, retaining multiplicities.
Only one can have value divisible by pi at one, and its valuation is exactly one.
The same factor is selected at minus one, since one and minus one have the same residue modulo pi.
Equivalently it is the unique factor whose reduction contains z+1, which has total multiplicity one in the displayed reduction.

Each Gaussian factor has rational norm equal to the corresponding actual rational irreducible factor.
The proof is the field-degree argument above; two roots in the same rational orbit above the fixed value i are in the same Q(i)-orbit because an automorphism taking one to the other fixes their rational-function value i.
Taking Gaussian norms in the endpoint factorization gives
\[
                 f_*(1)=f_*(-1)=2,\qquad
                 f_i(1)=f_i(-1)=1\quad(i\ne *).
 \tag{P23}
\]
Thus the unique factor in the degree partition above also carries both nonunit endpoint values.
This is an actual factor-selection constraint, not a global splitting mechanism.

<a id="dyadic-relative-shift-zero-baseline"></a>
## An unbounded odd shift with exactly zero complete cost

The [relative-zero-power filter in v3](Yin_L_G0458_v3.md#cyclotomic-square-relative-zero-powers) does not give a fixed gap when the odd part of the shift grows.
There is an exact zero-cost control in that remaining range.
For M=2^ell with ell>=2, put
\[
 C_0=z^2-1,\qquad D_0=z^M+1,\qquad r_0=M/2-1.
 \tag{D1}
\]
The two cyclotomic products are coprime and have only power-of-two conductors.
Their reciprocal signs are opposite, and deg(D_0)=deg(C_0)+2r_0.
The positive shift r_0 is odd and tends to infinity.
Nevertheless direct expansion gives
\[
 z^{2r_0}C_0^2+D_0^2
       =(z^{M-2}+1)(z^{M+2}+1).
 \tag{D2}
\]
Every factor of the complete output is cyclotomic, and its measure is exactly zero.
Thus growth of the permitted odd shift or of the output conductors does not itself produce a positive factor.

<a id="dyadic-deletion-inputs"></a>
## Deleting two dyadic factors gives a different bounded-cost template

For k>=2 set
\[
 n=2^k,\qquad
 C=\frac{z^n-1}{z^2+1},\qquad D=z^{2n}+1,\qquad
 r=n/2+1,\qquad F_k=z^{2r}C^2+D^2.
 \tag{D3}
\]
Equivalently, C is obtained by deleting the two dyadic factors z^n+1 and z^2+1 from z^(2n)-1.
This quotient is an integer monic cyclotomic product because four divides n.
Its degree is n-2, its constant coefficient is -1, and C*=-C.
The polynomial D is reciprocal, has degree 2n, and has constant coefficient one.

If C(zeta)=0, then zeta^n=1 and D(zeta)=2.
Also D(0)=1, so z^r C and D are coprime, including at zero.
Their effective phase difference is zero and their reciprocal signs are opposite, because
\[
                         \deg D=\deg C+2r.
\]
Here r is odd and unbounded.
Thus these pure dyadic inputs escape the bounded-odd-shift hypothesis of v3 without adding an odd input conductor.

The complete output F_k is monic of degree 4n and has constant coefficient one.
Indeed its first summand has degree 3n-2, strictly smaller than the degree of D^2.
The degree balance and the two reciprocal identities show that F_k is reciprocal.
No content is removed: F_k itself is the primitive output.

There is an exact complete-cost identity
\[
 (z^2+1)^2F_k(z)=G(z,z^n),\qquad
 G(z,w)=z^2w(w-1)^2+(z^2+1)^2(w^2+1)^2.
 \tag{D4}
\]
In expanded form,
\[
 G=(z^4+2z^2+1)(w^4+1)
       +2(z^4+z^2+1)w^2+z^2(w^3+w).
 \tag{D5}
\]
This has eleven nonzero terms, all coefficients are positive, and their sum is sixteen.
Specialization leaves at most eleven nonzero coefficients and preserves coefficient sum sixteen.
The multiplier in (D4) is monic cyclotomic, of zero measure and content one.
Therefore
\[
                    m(F_k)=m(G(z,z^n))\le\log16.
 \tag{D6}
\]
This equality retains all original roots, every factor and every multiplicity.

<a id="dyadic-deletion-newton-positivity"></a>
## Newton sums separate every non-telescoping input from zero measure

At k=2, (D3) is still the zero-cost control:
\[
                         F_2=(z^6+1)(z^{10}+1).
\]
For every k>=3, positivity follows without numerical root approximation.
The quotient in (D3) is
\[
                    C=-\sum_{j=0}^{n/2-1}(-1)^jz^{2j}.
\]
For 0<=j<n/2, the coefficient of z^(2j) in C^2 is (-1)^j(j+1).
Since
\[
                         F_k=z^{n+2}C^2+(z^{2n}+1)^2,
\]
its coefficients at degrees one through n+1 vanish.
Reciprocity gives the same vanishing for its first n+1 descending coefficients.

Write F_k=z^(4n)+a_1 z^(4n-1)+...+a_(4n), and let s_j be the sum of the j-th powers of all 4n roots.
Newton's identities first give s_j=0 for 1<=j<=n+1.
For any index t<2(n+2), every cross term a_j s_(t-j) in the t-th Newton identity vanishes: a_j=0 when j<n+2, and otherwise t-j<n+2.
Consequently s_t=-t a_t throughout that range.

For n>=16, the coefficient at degree n+8 is -4, coming from the z^6 coefficient of C^2.
There is no contribution from D^2 because n+8<2n.
Reciprocity gives a_(n+8)=-4, and n+8<2(n+2), so
\[
                         s_{n+8}=4(n+8)>4n.
 \tag{D7}
\]
If all roots had modulus at most one, the triangle inequality would give |s_(n+8)|<=4n.
Thus an exterior root exists.

For n=8, the coefficient at degree fourteen is three.
The same Newton argument gives s_14=-42, whereas the degree is thirty-two.
This again forces an exterior root.
Hence m(F_k)>0 for every k>=3.

Apply the accepted [DS17 univariate fixed-support statement](../audits/literature/DS17/Yin_U001.md#ds17-u001) to the actual completion G(z,z^n), using (D4)--(D6).
It follows that
\[
                    \eta_{11}\le m(F_k)\le\log16
                    \qquad(k\ge3).
 \tag{D8}
\]
The positive constant eta_11 is not evaluated.
This excludes complete measures tending to zero in this family.
It does not provide a uniform lower bound on each irreducible factor, and it does not bound the number of positive irreducible factors.

<a id="dyadic-deletion-exact-factor-control"></a>
## The first non-telescoping input has one positive factor

The single exact computation in [J143](../computations/programs/Yin_J_G0143/readme.md) uses k=3 only, so n=8, r=5, C=z^6-z^4+z^2-1 and D=z^16+1.
Its complete factorization over Z is
\[
 F_3=\Phi_{12}(z)H(z),\qquad \Phi_{12}=z^4-z^2+1,
\]
\[
 H=z^{28}+z^{26}-z^{22}-z^{20}+z^{18}+2z^{14}
       +z^{10}-z^8-z^6+z^2+1.
 \tag{D9}
\]
Both returned multiplicities are one.
The exact symbolic factorization returns H as irreducible and noncyclotomic.
Complete coefficient reconstruction, the displayed product, input normalization and the degree sum were checked.
Thus this input has one positive irreducible factor and cyclotomic degree four, using the accepted Kronecker characterization for the monic unit factors.
The irreducibility assertion is finite symbolic-library evidence, without a separate hand certificate or formal independent review.
No numerical Mahler measure or further parameter value was computed.

The deletion template supplies actual positive inputs outside the bounded-odd-shift restriction, with uniformly bounded complete cost.
The first non-telescoping input does not show positive-factor proliferation.
Whether individual factors become small remains unproved.

<a id="prime-square-source-and-next-step"></a>
## Source scope and the next construction

The arithmetic return is the already accepted C864 v2 original binomial norm argument, reused at its full original-degree scope.
The binary conductor rules and Gaussian field-degree accounting are the fixed arguments of v3.
The full Lawton statement is reused only at the Theorem 14/Example 15 interface actually retained in Den09 U002; neither Lawton's original proof nor an additional source edition was audited here.
The coefficient and root-height inequalities were proved directly above.
No new numerical parameter scan, root approximation or native mathematical computation was performed for this prime-family derivation.

The odd-prime family has escaped the fixed odd-conductor hypothesis, but it has not supplied a small factor.
Its complete outputs have no cyclotomic factors, have uniformly bounded measure, and approach a positive full-measure limit.
Every factor is governed by (P17), and its binary reduction and endpoints satisfy (P19)--(P23).
The missing input is a genuine global factor of degree o(p), necessarily along primes with ord_p(2)/p tending to zero.
Neither the fixed bivariate representation nor the local residue splitting establishes that input.
A further construction must produce such a factor with its full integer coefficients, or prove that the required global degree condition cannot occur.

<a id="moving-square-author-check-scope"></a>
## Ordinary author check scope

The construction contributor read the complete saved prime-family argument (P1)--(P23), and the coordinating contributor separately read and checked those arguments, their source interfaces and the full appended dyadic argument.
The bottleneck contributor reread the retained dyadic argument (D1)--(D9), the J143 native program and README, and the actual generated result with its seventeen exact checks.
That native computation covers only k=3 and includes no numerical roots or further parameter value.
The coordinating contributor also read the J143 README, program and generated checks without rerunning the program.
These are ordinary author checks, not a formal independent review of either family.
