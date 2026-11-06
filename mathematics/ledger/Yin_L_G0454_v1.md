---
author: Yin
---

# Arithmetic measure realization, prescribed residues and total Mahler cost

Date: 2026-11-05–06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The global_synthesis delegate inspected the selected sources and developed the congruence comparison and prescribed-residue adaptation.
The coordinating agent supplied the factor-degree return, proposed the prescribed-residue test, and derived the equilibrium and scaled-Chebyshev controls, which the delegate checked below.
These are author contributions and ordinary checks, not independent review or a new Claim assessment.

<a id="arithmetic-realization-scope"></a>
## Question and existing inputs

Can recent arithmetic realization theorems turn measures near the unit circle, or trace measures near the interval [-2,2], into integer polynomials with positive total logarithmic Mahler measure tending to zero?
The question concerns the full unrestricted Task, not normalized height, a fixed degree, or only Salem polynomials.
This bounded inquiry tests particular source constructions and one modification; it does not replace the Task by the real-trace subclass.

[C192](../claims/Yin_C_G0192_v1.md#real-arcs-and-supercritical-capacity) already uses Fekete–Szegő existence on a curve with strict supercritical capacity.
Its [global output](../claims/Yin_C_G0192_v1.md#global-output-and-norm) supplies totally real integral unit residuals, with no prescribed degree or small-total-Mahler conclusion for an original polynomial.
[L449](Yin_L_G0449_v1.md#original-trace-lattice) retains the original integer trace lattice and its total Green-function cost; continuous shell volume and a thin Jacobian shell do not establish the needed integer points.
The new sources supply actual integer-polynomial constructions with prescribed limiting distributions, so they contain information different from that continuous-volume comparison.
Their dependence on degree, support enlargement and irreducibility must still be charged.

The only uniform gap used here is the supplied-auxiliary theorem [C864 v2, Part A](../claims/Yin_C_G0864_v2.md#statement).
For an original nontorsion algebraic integer unit of degree d, it gives m(f)>Gamma_bin(C)>0 from an integer V of degree at most Cd, integral V(alpha)/2, and a binary reflection with at most four pairs.
Its original field, multiplicities, zero-value allowance, dependencies and review limits remain those of that fixed input.
This inquiry constructs such an auxiliary for the particular source outputs; it supplies no automatic auxiliary for the unrestricted domain.

<a id="source-editions-and-inspection"></a>
## Sources, editions and inspected scope

The local capacity and trace-lattice records were reused before a bounded primary-source search for Smith's converse to Fekete and the Orloski–Sardari quantitative constructions.
The following exact online preprint editions supplied the mathematical text.
Their keys are registered in the [bibliography](../literature/references.bib).

| Key | Actual inspected original | Passages used |
| --- | --- | --- |
| Smi24 | Alexander Smith, [Algebraic integers with conjugates in a prescribed distribution, arXiv:2111.12660v2](https://arxiv.org/html/2111.12660v2), version dated 16 March 2024; [v2 PDF](https://arxiv.org/pdf/2111.12660v2) | Theorem 1.5; Proposition 2.5 statement; Corollary 3.3; Proposition 4.1 and its construction in Sections 4.1–4.2, especially Lemma 4.5, Definition 4.6 and Lemmas 4.7–4.8; Remark 5.14. |
| OS23 | Bryce Joseph Orloski and Naser Talebizadeh Sardari, [Limiting Distributions of Conjugate Algebraic Integers, arXiv:2302.02872v2](https://arxiv.org/html/2302.02872v2), 5 April 2024; [v2 PDF](https://arxiv.org/pdf/2302.02872v2) | Definition 1.1, Theorem 1.2, Corollary 1.3, Definition 1.4, Theorems 1.5–1.6; the even-coefficient construction and the actual outputs in Sections 3.1 and 4.3, including equation (49). |
| SO23 | Bryce Joseph Orloski and Naser Talebizadeh Sardari, [A quantitative converse of Fekete's theorem, arXiv:2304.10021v2](https://arxiv.org/html/2304.10021v2), 25 March 2024; [v2 PDF](https://arxiv.org/pdf/2304.10021v2) | Generic-sampling setup and Theorem 1.14; the strict-supercritical lower-bound construction in Section 3.2 and its actual congruence class. |

Smi24 is published in Annals of Mathematics 200(1) (2024), 71–122, [DOI 10.4007/annals.2024.200.1.2](https://doi.org/10.4007/annals.2024.200.1.2).
That bibliographic identification does not turn the inspected arXiv text into a journal-body inspection.
The Smi24 v2 PDF's printed first-page date is 19 March 2024; the fixed edition here is the arXiv v2 identified above.
OS23 and SO23 use their first public year, 2023, rather than their inspected v2 dates.
For SO23, the v2 PDF first page and v2 HTML title list Orloski before Sardari, whereas the [arXiv abstract metadata](https://arxiv.org/abs/2304.10021) list Sardari before Orloski; the source table records the inspected body's order.
No author-supplied table of contents was observed in any of the three exact v2 PDFs; the HTML renderer's navigation is not transcribed as an author-supplied contents list.
The online originals were sufficient for this inquiry; no local original copy is asserted or needed for its source locators.

This is a targeted inspection of statements and the construction steps used below, not a complete audit of any paper, its source dependencies or its computations.
In particular, the approximation and geometry-of-numbers results invoked by the papers are retained at their source scope; no new verification of all their proofs is claimed.
The prescribed-residue argument below is this exploration's adaptation of the inspected steps, not a theorem quoted from the source.

<a id="realization-theorem-ranges"></a>
## What the realization results actually supply

Write kappa for ordinary logarithmic capacity, so the critical capacity is kappa=1 and strict supercriticality is log(kappa)>0.

<a id="arithmetic-measure-and-potential-conventions"></a>

**Definition (potential and arithmetic measure conventions).**
Let mu be a compactly supported Borel probability measure on C, with support contained in Sigma.
Use the positive-log-kernel potential
\[
 v_\mu(z)=\int\log|z-t|\,d\mu(t),\qquad
 w_\mu(z)=e^{-v_\mu(z)}.
\]
Smith's potential convention has the opposite sign, while the displayed weight is the same.
For a compact real set Sigma define
\[
 W_j(F)=\|w_\mu^j F\|_\Sigma.
\]
Here j is a weight exponent; m(P) will always mean total logarithmic Mahler measure.
Auxiliary degrees called m in the sources are renamed k_n or r below.

Call this measure arithmetic here when it is invariant under conjugation and satisfies
\[
 \int\log|A|\,d\mu\geq0
 \quad(0\ne A\in\mathbb Z[y]).
\]
On a real set the invariance is automatic.
This inequality formulation is OS23's set B_Sigma; its Definition 1.1 instead defines A_Sigma by weak limits of distinct complete conjugate sets eventually in every neighborhood of Sigma, using real neighborhoods for its real variant.
The equality A_Sigma=B_Sigma on compact conjugation-symmetric sets is the source's Theorem 1.2, not a definitional identity proved here.
The local word arithmetic uses that inequality formulation, and the logarithmic integral is understood in the extended sense when a polynomial vanishes on its support.
The positive-potential convention is OS23 equation (4).
Hölder means that there are constants C>0 and eta_H>0 with mu([a,b] times [c,d])<=C*max(b-a,d-c)^(eta_H) for every rectangle with a<b and c<d, as in the source's text before Corollary 1.3.
Smi24 Theorem 1.5 treats a compact real Sigma with at most countably many components and capacity greater than one.
It characterizes such arithmetic measures by weak limits of distinct monic irreducible integer polynomials whose roots all lie in Sigma.
Its concrete proof first reduces to a Hölder measure and a finite union of intervals and then uses the construction inspected below.
This is a real theorem, not a theorem for arbitrary complex supports.

OS23 Theorem 1.2 gives a complex-conjugation-invariant compact-set characterization using arbitrarily small neighborhoods, including capacity one; Corollary 1.3 supplies an exact-support conclusion for finite unions of rectangles or real intervals at capacity greater than one.
The quantitative Theorems 1.5–1.6 assume empty interior and connected complement, an arithmetic Hölder probability measure, and a fixed open neighborhood D of its compact support.
For sufficiently large degree n they produce monic irreducible integer polynomials with roots in D and, respectively,
\[
 \|Q_n\|_n\leq \exp(n^{1-\eta}),\qquad
 \|Q_n\|_n\leq
 \exp\!\left(Cn\frac{(\log\log n)^3}{\log n}\right),
 \quad
 \|Q\|_n=\max_{z\in\mathbb C}e^{-nv_\mu(z)}|Q(z)|.
\tag{1}
\]
The positive eta depends on the Hölder exponent, and the algorithmic constant C depends on the measure.
The large-degree threshold and root localization are not supplied uniformly for a neighborhood shrinking with n.
The real version allows an open neighborhood in the real topology.
The interval [-2,2] has empty interior in the complex plane and connected complement; the unit circle has disconnected complement, so these quantitative statements cannot be applied to that circle without another step.

SO23 Theorem 1.14 concerns arithmetic Hölder measures on a finite union of rectangles and real intervals, with a conjugation-symmetric generic n-point sample satisfying its stated sampling and polynomial-separation conditions.
More precisely, Definition 1.13 uses partitions into M pieces per side, with n^epsilon<M<=n^(1/2-epsilon) and L<n^(1-epsilon)M^(-2) for some fixed epsilon>0.
The sample count in each cell differs from n times its measure by at most L, and distinct sample points and sample-to-cell-boundary distances are bounded below by a constant times n^(-A), for fixed A>0.
The output degree is n+k_n, not n, with k_n at least a source-dependent power n^(1-tau), where tau>0.
It counts irreducible integer outputs with n matched roots at an exponentially small scale of the form kappa^(-k_n(1-O(n^(-eta)))) and all n+k_n roots in the prescribed set.
The inspected Section 3.2 construction starts with capacity greater than one and an interior set of capacity greater than one.
No critical-boundary application or assertion uniform in a degenerating interior set is made here.
The counting asymptotic is not needed for the conclusions below; its full proof and all generic-sampling constants were not audited.

<a id="same-output-eisenstein-return"></a>
## The actual Eisenstein outputs return to a supplied binary gap

Smi24 Section 4.1 produces a polynomial of the form
\[
 Q(y)=y^n+\sum_{j=n-k_n}^{n-1}a_jy^j+4R(y)-2,
 \qquad a_j\in2\mathbb Z,\quad \deg R<n-k_n.
\tag{2}
\]
The displayed outputs in OS23 Sections 3.1 and 4.3 have the same congruence properties.
SO23 Section 3.2 starts with such an output and adds four times integer polynomials, preserving those properties throughout its counted subfamily.
Thus each inspected output is monic and 2-Eisenstein:
\[
 Q\bmod2=y^n,\qquad Q(0)\equiv2\pmod4.
\tag{3}
\]
Here n denotes its entire actual degree, including complementary roots when the source first writes that degree as n+k_n.
As a direct candidate for Lehmer, Q already has m(Q)>=log|Q(0)|>=log 2.

Passing to a reciprocal unit through the trace map does not evade the congruence cost.
Set
\[
 P(x)=x^nQ(x+x^{-1})\in\mathbb Z[x].
\tag{4}
\]
It is monic of degree 2n with constant coefficient one, and
\[
 \overline P=(x^2+1)^n=(x+1)^{2n}\quad\hbox{in }\mathbb F_2[x].
\tag{5}
\]
Take
\[
 L=2^{\lceil\log_2(2n)\rceil}.
\]
For every n>=1, including n=1 where L=2, one has 2n<=L<4n and
\[
 x^L-1=(x+1)^L\quad\hbox{in }\mathbb F_2[x],\qquad
 \overline P\mid x^L-1.
\tag{6}
\]

It is unnecessary to assume that the trace lift P is irreducible.
Let f be any monic irreducible integer factor of P, and alpha any root of f.
Since all monic factor constant coefficients multiply to one, each is 1 or -1, so alpha is an algebraic integer unit.
Set beta=alpha+alpha^(-1).
The 2-Eisenstein polynomial Q is irreducible of degree n and has beta as a root, while alpha satisfies X^2-beta X+1=0 over Q(beta).
Consequently
\[
 d=\deg f=[\mathbb Q(\alpha):\mathbb Q]
    \in\{n,2n\},\qquad L<4n\leq4d.
\tag{7}
\]
Lift the quotient in (6) to an integer polynomial H.
For some B in Z[x] one has x^L-1=P H+2B, and evaluation at alpha gives
\[
 \frac{\alpha^L-1}{2}=B(\alpha)\in\mathbb Z[\alpha]
       \subseteq\mathcal O_{\mathbb Q(\alpha)}.
\tag{8}
\]
The integer auxiliary V=x^L-1 has one reflected binary pair, its two endpoint residues are nonzero, and its degree is less than 4d.
For each nontorsion factor f, C864 v2 therefore gives
\[
 m(f)>\Gamma_{\rm bin}(4)>0.
\tag{9}
\]
Mahler measure is additive over the complete factorization, including multiplicities.
If m(P)>0, at least one factor has positive measure and is nontorsion; its contribution alone proves m(P)>Gamma_bin(4).
Cyclotomic factors contribute zero and do not affect this return.
This is a strict necessary floor for the positive trace lifts of the actual 2-Eisenstein outputs inspected above, rather than a conclusion drawn from an inadequate upper bound.
It excludes that output family as a positive-to-zero sequence, but does not exclude all realizations permitted by the main existence theorems.

<a id="prescribed-residue-adaptation"></a>
## Replacing the Eisenstein residue without increasing the inspected error budget

Fix a compact finite union of real intervals Sigma with kappa>1 and an arithmetic Hölder probability measure mu supported there.
Supply a monic irreducible polynomial
\[
 \overline h_n(y)=y^n+\sum_{j=0}^{n-1}b_jy^j
       \in\mathbb F_2[y],\qquad b_j\in\{0,1\}.
\tag{10}
\]
The argument is conditional on this supplied finite-field polynomial; no finite-field existence theorem or algorithm is being newly invoked here.
The degree n is sufficiently large for the source construction below, so n>1 and irreducibility in (10) implies b_0=1.
The proposed replacement assigns the coefficient of y^j to the coset b_j+2Z instead of to 2Z.
It is important to change the high-coefficient construction as well as the final rounding.
Changing only the final lower coefficients leaves the wrong high residues.

### The high-coefficient stage

Here is the actual dependence of Smi24 Lemma 4.5 and Definition 4.6 on evenness.
Use a distinct constant c_1 for their Chebyshev bounds and set
\[
 D_*=\left\lceil\frac{4c_1^2}{\kappa-1}\right\rceil.
\tag{11}
\]
Let G be their monic real base polynomial of degree N, and let r>=2 be their complementary-degree parameter.
Starting from the pruned monic Chebyshev polynomial T_tilde_r, Lemma 4.5 adjusts it in descending degrees by lambda_i T_i, where T_i is monic of degree i.
In the coefficient of degree D_*r+N-(r-i) of T^(D_*)G, the new lambda_i has coefficient D_*; higher coefficients are unchanged.
The next point of any coset b+2Z is less than or equal to two above the current coefficient.
Thus the same triangular choices give
\[
 0\leq\lambda_i\leq2/D_*,\qquad
 \left|\sum_{i=0}^{r-1}\lambda_iT_i(y_j)\right|
 \leq\frac{2c_1\kappa^r}{D_*(\kappa-1)}
 \leq\tfrac12c_1^{-1}\kappa^r
\tag{12}
\]
at every source root-separating point y_j.
The top r nonleading coefficients of T^(D_*)G can therefore have their prescribed residues while the same sign and size estimates hold.

Definition 4.6 next forms
\[
 B_0=\prod_{j=0}^{D_*-1}
       \left(T-\frac{2j+1}{4D_*c_1}\kappa^r\right),
 \qquad d_*=D_*r-r.
\tag{13}
\]
The difference B_0-T^(D_*) has degree at most d_*.
Multiplication by G consequently leaves coefficients above N+d_* unchanged; the coefficient at N+d_* is included in the next correction stage.
Descending additions epsilon_i T_i to B_0, for d_*>=i>=1, adjust the coefficient of G B_0 at degree N+i with coefficient one and leave higher coefficients fixed.
Targeting the relevant cosets gives the same 0<=epsilon_i<=2 and
\[
 \left|\sum_{i=1}^{d_*}\epsilon_iT_i(x)\right|
 \leq\frac{2c_1\kappa^{d_*+1}}{\kappa-1}
       \quad(x\in\Sigma).
\tag{14}
\]
Finally the source adds a nonnegative real constant a to avoid small values at the roots of G.
With c_2=8(4D_*c_1)^(D_*), the same avoidance argument gives
\[
 0\leq a\leq2c_2^{-1}\kappa^{D_*r}.
\tag{15}
\]
This changes G times the complementary polynomial only in degrees at most N, outside the prescribed range [N+1,N+D_*r-1].
The estimates in Lemmas 4.7–4.8 use (12)–(15), the root-separating points and the unchanged magnitude bounds, rather than the value zero of the target parity.
In particular their sign margin uses
\[
 6c_2^{-1}-\frac{2c_1\kappa^{-r+1}}{\kappa-1}>C^{-1}
\tag{16}
\]
for sufficiently large r, exactly as in the source.
This margin is retained, not replaced by an unquantified assertion that bounded coefficient changes preserve roots.

In the proof of Proposition 4.1 the complementary parameter is r=ceil((k_n+1)/D_*), with base degree N=n-D_*r>=2.
Then N+1<=n-k_n, so the range fixed above contains every required coefficient of degree n-k_n through n-1.
Using the same source root-separation and weighted estimates gives a monic real polynomial A_n, all of whose roots are simple and lie in Sigma, such that its top k_n nonleading coefficients are integers with the prescribed residues and
\[
 W_{n-k_n}(A_n)\leq n^{C_1}\kappa^{k_n}.
\tag{17}
\]
Each source isolating interval has opposite endpoint signs and weighted endpoint magnitudes at least n^(-C_1)kappa^(k_n).
Here C_1 is the Proposition 4.1 constant, distinct from c_1 in (11).
All constants and sufficiently-large-degree conditions retain their source dependence on Sigma, mu and the chosen degree budget.
This coefficient-by-coefficient argument is the justification for the modified Proposition 4.1 input; the source's general congruence comment in Remark 5.14 is compatible with it but is not used as a substitute for these steps.

### The final integer rounding

Choose C_0>=1 large enough for the same applications of Theorem 3.1 and Corollary 3.3 as in Smi24 Section 4.1, and put
\[
 B=\frac{2C_0}{\log\kappa},\qquad
 k_n=\lfloor B\sqrt n\log n\rfloor,\qquad s=n-k_n.
\tag{18}
\]
Use the source's sufficient choices
\[
 n>C_1,\qquad
 4n^{C_0+C_0\sqrt n}<n^{-C_1}\kappa^{k_n},\qquad
 n-B\sqrt n\log n\geq2.
\tag{19}
\]
The lower bound C_0>=1 is a conservative permissible enlargement of a valid source constant, not a source theorem that every implementation must use a constant at least one.
For each fixed Sigma and mu, these conditions hold for all sufficiently large n.

Write A_n=A_high+A_low, with deg A_low<s and A_high including the leading monomial and the prescribed high coefficients.
Set H_low=sum_(j=0)^(s-1)b_j y^j and
\[
 F=(A_{\rm low}-H_{\rm low})/2.
\]
Corollary 3.3 applies to any real F of degree at most s-1, any squarefree integer S of degree s, a Hölder mu, and a compact finite union of intervals Sigma; it returns R in Z[y] of degree at most s-1 with
\[
 W_s(F-R)\leq s^{C_0}W_s(S).
\tag{20}
\]
The same Section 4.1 use of Theorem 3.1 supplies squarefree S of degree s with W_s(S)<=s^(C_0 sqrt(s))<=n^(C_0 sqrt(n)).
The arithmetic hypothesis on mu is retained for that input; squarefreeness and degree s are required, not an arbitrary small auxiliary polynomial.
Consequently
\[
 Q_n=A_{\rm high}+H_{\rm low}+2R\in\mathbb Z[y],
 \qquad
 W_s(Q_n-A_n)\leq2n^{C_0+C_0\sqrt n}.
\tag{21}
\]
It is monic of degree n, has reduction h_bar_n, and is irreducible over Q by reduction modulo two and Gauss's lemma.
There is no additional norm penalty for H_low: it is subtracted inside the unrestricted real input F to Corollary 3.3, rather than added after rounding.
By (19), the perturbation in (21) is smaller than every weighted endpoint margin of A_n.
Thus Q_n has a root in each of the n disjoint isolating intervals, and degree n ensures these are all its roots and each is simple.

Put M_w=max_(x in Sigma)w_mu(x).
The complete weighted upper bound is
\[
 W_n(Q_n)
 \leq(M_w\kappa)^{k_n}
       \left(2n^{C_0+C_0\sqrt n}+n^{C_1}\right).
\tag{22}
\]
Indeed W_n<=M_w^(k_n)W_s, and (17), (21) and kappa>1 give (22).
This is the same type of estimate as the original source's bound with four in place of two.
It removes the specific forced residue Q_bar=y^n and hence the particular short nilpotent-period argument (5)–(8).
It does not show that every other degree-linear reflected auxiliary is absent.
The constant coefficient of Q_n is odd but need not be 1 or -1; its trace lift is nevertheless a monic integer unit polynomial by (4).
No numerical implementation or actual positive-to-zero sequence is asserted by this symbolic adaptation.

<a id="total-green-function-budget"></a>
## Returning every error to total Mahler measure

For a monic degree n polynomial Q with roots t_j, the trace lift (4) has the exact total measure
\[
 m(P)=\sum_{j=1}^n g(t_j),\qquad
 g(t)=\log\max\{|z|:z^2-tz+1=0\}.
\tag{23}
\]
Every quadratic factor has root product one, so its contribution is precisely g(t), with all multiplicities retained.
For real t this is
\[
 g(t)=
 \begin{cases}
 0,&|t|\leq2,\\
 \operatorname{arcosh}(|t|/2),&|t|>2.
 \end{cases}
\tag{24}
\]
This is the total normalization retained in L449, not m(P)/(2n).

Consider the real neighborhood
\[
 \Sigma_\delta=[-2-\delta,2+\delta],\qquad
 \kappa=1+\delta/2>1.
\tag{25}
\]
Root support alone supplies
\[
 0\leq m(P)\leq n\operatorname{arcosh}(1+\delta/2)
                    \leq n\sqrt\delta.
\tag{26}
\]
To make this particular upper certificate tend to zero would require n sqrt(delta) to tend to zero.
That condition is not necessary for actual small measure when most roots lie well inside [-2,2].

For the conservative sufficient budget (18)–(19), n-B sqrt(n) log n>=2 implies
\[
 \log\kappa>\frac{2C_0\log n}{\sqrt n},\qquad
 \delta\sqrt n>4C_0\log n\geq4\log n,
\tag{27}
\]
where log(1+delta/2)<=delta/2 was used.
Hence that guaranteed parameter regime does not overlap with n sqrt(delta)->0, or even with n delta->0.
This is an incompatibility of the displayed sufficient budget and those prospective upper certificates, not a necessary lower bound on all possible degrees, all optimized constants, or the actual Mahler measure of the modified outputs.
The inspected source does not give stronger estimates uniform in delta that replace this budget near capacity one.
The explicit D_* in (11) and margin (16) also retain their dependence on kappa-1; fixing delta before taking n large does not remove it.

There is a separate weighted estimate that also shows the required total normalization.
Let mu_0 be the arcsine measure on [-2,2].
Its positive potential is zero on [-2,2] and is g outside that interval, so w_mu0=1 on [-2,2] and M_w=1 on Sigma_delta.
It is a Hölder arithmetic measure: for A=a product(y-beta_i) in Z[y], its log integral is log|a|+sum_i g(beta_i)>=0, equivalently the Mahler integral of x^(deg A)A(x+x^(-1)).
The identity follows by writing t=2 cos(theta) in the arcsine integral and factoring each x^2-beta_i x+1; it is valid for complex beta_i as well.
For the output Q_n of (21), Jensen's formula on the unit circle gives
\[
 m(P_n)=\frac1{2\pi}\int_0^{2\pi}
       \log|Q_n(2\cos\theta)|\,d\theta
 \leq\log\|Q_n\|_{[-2,2]}
 \leq\log W_n(Q_n).
\tag{28}
\]
Thus (22) yields the fully paid total bound
\[
 m(P_n)\leq k_n\log\kappa+
       \log\left(2n^{C_0+C_0\sqrt n}+n^{C_1}\right)
       =O_{\Sigma_\delta,\mu_0}(\sqrt n\log n).
\tag{29}
\]
This bound is sublinear in degree but is not o(1), and its constants are not uniform as delta tends to zero.
The original Eisenstein construction has the same upper-bound issue and also the strict floor (9); only the latter is a lower-bound exclusion.

Applying (28) to the OS23 norm in (1) similarly gives total upper bounds n^(1-eta) and Cn(log log n)^3/log n for the corresponding trace outputs.
Neither is a vanishing total error, despite becoming small after division by degree.
The inspected algorithm's localization step in Section 4.3 chooses
\[
 k_n=\left\lceil\frac{2Cn}{\log\kappa}
                   \frac{(\log\log n)^3}{\log n}\right\rceil<n
\tag{30}
\]
for a fixed enlarged compact set with kappa>1.
It supplies no simultaneous shrinking-neighborhood bound that can simply be substituted into (1).
Its actual output also has the strict floor (9).

For SO23's matching construction, suppose the first n target trace roots lie in [-2,2] and their output roots are within epsilon_n in the real line.
Each matched contribution is at most sqrt(epsilon_n) by (24), while every one of the k_n additional roots must also be paid.
If the entire output lies in Sigma_delta, the resulting elementary certificate is
\[
 m(P)\leq n\sqrt{\epsilon_n}
              +k_n\operatorname{arcosh}(1+\delta/2).
\tag{31}
\]
An exponentially good match for the first n roots cannot discard the second term.
The inspected theorem supplies neither a uniform shrinking-set version controlling that term nor a different irreducibility mechanism for its counted subfamily.
Again the growing upper budget alone is not an actual lower bound; the separate congruence argument gives the strict floor for this inspected family.

<a id="equilibrium-and-scaled-chebyshev-control"></a>
## An exact equilibrium model separates distribution cost from integrality

The support-only estimate (26) overcharges a nearly equilibrium distribution.
This can be checked directly, without an unquantified appeal to weak convergence.
The equilibrium measure mu_delta on [-2kappa,2kappa] is the image of uniform dtheta/pi on [0,pi] under t=2kappa cos(theta).
Define f_kappa(theta) to be arcosh(kappa|cos(theta)|) when kappa|cos(theta)|>=1, and zero otherwise.
Then
\[
 I(\kappa)=\int g\,d\mu_\delta
   =\frac2\pi\int_0^{\arccos(1/\kappa)}
                      \operatorname{arcosh}(\kappa\cos\theta)\,d\theta.
\tag{32}
\]
For kappa>1, write the integrand as the nonnegative integral
\[
 \operatorname{arcosh}(\kappa\cos\theta)
   =\int_{1/\cos\theta}^{\kappa}
       \frac{\cos\theta}{\sqrt{s^2\cos^2\theta-1}}\,ds
\]
on its indicated domain.
Tonelli's theorem and u=sin(theta) give
\[
 I(\kappa)=\frac2\pi\int_1^\kappa
   \left(\int_0^{\sqrt{1-s^{-2}}}
           \frac{du}{\sqrt{s^2-1-s^2u^2}}\right)ds
 =\int_1^\kappa\frac{ds}{s}=\log\kappa.
\tag{33}
\]
Thus the ideal total equilibrium cost is n log(kappa), asymptotic to n delta/2, substantially smaller than n sqrt(delta).
For an actual root measure nu_n the exact discrepancy is
\[
 m(P_n)=n\log\kappa+
          n\left(\int g\,d\nu_n-\int g\,d\mu_\delta\right).
\tag{34}
\]
Weak convergence for each fixed delta gives no uniform o(1/n) bound on the parenthesized error when both delta and degree vary.
The conservative sufficient regime (27) already fails to certify n delta->0; this observation does not prohibit improved realization estimates outside that regime.

There is also an explicit real-polynomial model with a quantitative discrepancy bound.
Let T_n denote the classical Chebyshev polynomial satisfying T_n(cos(theta))=cos(n theta), and put
\[
 Q_{n,\kappa}(t)=2\kappa^nT_n(t/(2\kappa)),\qquad
 t_j=2\kappa\cos\frac{(j-1/2)\pi}{n}.
\tag{35}
\]
It is monic and has exactly these midpoint roots.
The variation of f_kappa on [0,pi] is 2 arcosh(kappa): it decreases from arcosh(kappa) to zero, stays zero, and increases back to arcosh(kappa).
For each of the n equal subintervals, the difference between its midpoint value and its average is at most the oscillation there.
Summing and using (33) proves
\[
 \left|m\bigl(x^nQ_{n,\kappa}(x+x^{-1})\bigr)
                    -n\log\kappa\right|
       \leq2\operatorname{arcosh}\kappa.
\tag{36}
\]
In particular the ideal real model can have total measure tending to zero if n delta tends to zero.
This is not an integer construction.

For n>=2 the first two nonzero terms of 2T_n(t/2) are t^n-n t^(n-2), as follows either from its recurrence or its usual leading coefficients.
Hence Q_(n,kappa) has coefficient -n kappa^2 at degree n-2.
If this exact polynomial is integral and kappa>1, then
\[
 n(\kappa^2-1)\in\mathbb Z_{>0},\qquad
 \kappa\geq\kappa_0=\sqrt{1+1/n}.
\tag{37}
\]
Each f_kappa(theta_j) is nondecreasing in kappa, so (36) at kappa_0 yields
\[
 \begin{aligned}
 m\bigl(x^nQ_{n,\kappa}(x+x^{-1})\bigr)
 &\geq\frac n2\log(1+1/n)
          -2\operatorname{arsinh}(1/\sqrt n)\\
 &\geq\frac12-\frac1{4n}-\frac2{\sqrt n}
 >\frac14\qquad(n\geq100).
 \end{aligned}
\tag{38}
\]
The second inequality uses log(1+x)>=x-x^2/2 for x>=0 and arsinh(x)<=x.
Degree n=1 is excluded from (37), since its polynomial is just t and its trace lift is cyclotomic.
This arithmetic obstruction concerns only the exact scaled-Chebyshev family (35).
It does not extend to arbitrary integer polynomials with approximately the same root distribution or to the modified Smith outputs.
It is independent of the Eisenstein residue obstruction and of the source's sufficient rounding budget.

<a id="outcome-and-reopening-test"></a>
## Outcome and discriminating next test

The source comparison yields a genuine change of arithmetic input: the inspected Smith construction can target a supplied irreducible residue polynomial modulo two while retaining its endpoint and weighted-error estimates.
The precise adaptation is (10)–(22), rather than a claim that all irreducibility mechanisms have the same binary obstruction.
The strict obstruction (9) belongs only to the inspected 2-Eisenstein outputs; the modified output has not been shown to have a positive uniform floor by that argument.

What remains unsupported is the simultaneous realization of shrinking capacity and total Green-function discrepancy tending to zero, with an actual positive integer-polynomial output.
A useful next test must therefore provide estimates uniform in delta for a changed construction and bound the full sum in (23), including complementary roots and rounding.
For equilibrium targets, (34) identifies the exact quantity to control; for an exact scaled-Chebyshev proposal, (37) is an immediate arithmetic test before further approximation work.
Merely giving weak convergence, normalized height tending to zero, or a vanishing average support error does not meet this obligation.

No new unrestricted covering dichotomy, uniform Mahler gap, or positive-to-zero sequence was obtained in this inspected scope.
The conclusions leave other realization methods and stronger uniform estimates open.
No Claim version or assessment is changed by this exploratory record.
