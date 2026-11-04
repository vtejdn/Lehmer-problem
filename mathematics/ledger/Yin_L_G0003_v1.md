---
author: Yin
---
# G0001 exploration: cyclic induction and finite trajectories

Host locations in historical commands and records below are normalized; relative historical paths, arguments and execution facts are unchanged.
This records no new run.

<a id="g0001-cyclic-induction"></a>

Date: 2026-10-06.
Preserved research-operation record for the existing [Task G0001](../tasks/Yin_T_G0001_v1.md#contract), primarily [S G0001](../strategies/Yin_S_G0001.md#entropy-gap-route).
This is a calculation and candidate-screening package, not a new Task, allocated Claim, or solution of Lehmer's problem.
The full current reusable statements and complete arguments are owned by [C G0206](../claims/Yin_C_G0206_v1.md#argument).
The mathematical body below preserves the original fixed input for the [historical agent findings](../audits/reviews/Yin_R_G0800_v1.md#historical-cyclic-review), including their original hypotheses and equation numbers.
Its old no-Claim wording records the 2026-10-06 exploration and supplies no current assessment.


## 1. Reuse, scope and conventions

The needed conclusion is an exact comparison of finite trajectories, local entropy and finite-set attainment for cyclic induction of an arbitrary discrete abelian flow.
A secondary comparison concerns the whole substitution polynomial and a single selected irreducible factor.

Before developing the calculation, the existing [assessment L G0001](Yin_L_G0001_v1.md#lehmer-route-assessment), S G0001, [DGB16-U001](../audits/literature/DGB16/Yin_U001.md#dgb16-u001), [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001), and the applicability discussions in Uniform descent and finite closure; current organization and Shared structure across families; current organization were checked.
The assessment already warns that $m(P(t^k))=m(P)$ and that early word counts do not prove an asymptotic lower bound.
This draft adds the precise trajectory formula, alphabet behavior and selected-factor degree accounting; it does not count the old warning as a new result.

The accepted external inputs are the entropy conventions and elementary laws in DGB16, Proposition 2.8 and the torsion-free rationalization interface, and the rational Algebraic Yuzvinski Formula and finite-set realization interface in the retained GBV15 version.
The final norm argument additionally reuses the absolute-height normalization, coefficient bound and Kronecker interface in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), together with the already recorded fixed-degree finiteness in L G0001.
These adequate local inputs were checked before adopting that argument; no Dirichlet unit theorem is needed.
Their audit boundaries remain those of the linked source units; no original external proof is re-audited here.
In particular there is no new source claim about a rank-uniform realizing set.

A bounded supplementary search used the queries `"algebraic entropy" "induced" "logarithmic law"`, `"algebraic entropy" "cyclic" "trajectory" logarithmic law`, `"algebraic entropy" "induction" "finite index" amenable semigroup actions`, `"algebraic entropy" "P(t" "k"`, and `"algebraic entropy" "companion" "trajectory"`.
It returned the known logarithmic/product laws and related finite-index action literature, but no exact finite-alphabet cyclic-induction statement was verified from those hits.
Those hits are not proof inputs.
The retained local interfaces already suffice for the direct calculation below.
This bounded search is not a novelty claim or an exhaustive literature classification.

All groups below are discrete abelian groups, written additively.
Every alphabet is a nonempty finite **subset**, not necessarily a subgroup.
Write
\[
T_n(\psi,A)=\sum_{j=0}^{n-1}\psi^j A,\qquad T_0(\psi,A)=\{0\},
\]
\[
H(\psi,A)=\lim_{n\to\infty}\frac{\log|T_n(\psi,A)|}{n},
\qquad h(\psi)=\sup_A H(\psi,A).
\]
Logarithms are natural.
Local $H$ is finite and at most $\log|A|$; total $h$ may be infinite.
No division by rank is used.
No injectivity, expansiveness, finite-rank or unit-circle exclusion is implicit.

## 2. Exact cyclic-induction formula

Fix an endomorphism $\psi:B\to B$ and an integer $k\ge1$.
Set $G=B^k$ and
\[
\Phi(b_0,\ldots,b_{k-1})=(\psi b_{k-1},b_0,\ldots,b_{k-2}).
\]
Let $\iota_r:B\to G$ be the injection in coordinate $r$, numbered $0,\ldots,k-1$.
Direct iteration gives
\[
\Phi^k=\psi^{\times k},\qquad
\Phi^{qk+r}\iota_0(b)=\iota_r(\psi^q b)
\quad(q\ge0, 0\le r<k). \tag{2.1}
\]

For every nonempty finite $A\subset B$, put $F=\iota_0 A$.
If $n=qk+s$ with $q\ge0$ and $0\le s<k$, grouping the summands according to their coordinate gives the equality of sets
\[
T_n(\Phi,F)=
\prod_{r=0}^{s-1}T_{q+1}(\psi,A)
\ \times\!
\prod_{r=s}^{k-1}T_q(\psi,A). \tag{2.2}
\]
This is a coordinate identity, not just a counting bound.
At each visit to one coordinate the original time-indexed choice of an element of $A$ is independent of the choices at all other times.
Internal coincidences are precisely those already present in the corresponding base trajectory.
Thus
\[
|T_n(\Phi,F)|=|T_{q+1}(\psi,A)|^s|T_q(\psi,A)|^{k-s}. \tag{2.3}
\]
It includes $q=0$, using $T_0=\{0\}$.
Neither $0\in A$ nor injectivity of $\psi$ is required.

Writing $a_q=\log|T_q(\psi,A)|$, $a_0=0$, we obtain
\[
\frac{\log|T_n(\Phi,F)|}{n}
=\frac{s a_{q+1}+(k-s)a_q}{qk+s},\qquad
\frac{\log|T_{kq}(\Phi,F)|}{kq}=\frac{a_q}{q}\quad(q\ge1), \tag{2.4}
\]
and the increment identity
\[
\log|T_{n+1}(\Phi,F)|-\log|T_n(\Phi,F)|=a_{q+1}-a_q
\quad(n=qk+s, 0\le s<k). \tag{2.5}
\]
Every base increment is repeated exactly $k$ times.
No monotonicity of the sequence of increments is asserted.

Taking the limit, or just the subsequence $n=kq$, gives
\[
H(\Phi,\iota_0 A)=H(\psi,A). \tag{2.6}
\]
For $A=\{0,v\}$ this is the requested binary-alphabet identity, also valid when $v=0$ or has finite order.
In contrast, applying $\Phi^k$ to the **same** alphabet stays in coordinate zero, so
\[
H(\Phi^k,\iota_0 A)=H(\psi,A), \tag{2.7}
\]
whereas the logarithmic law and product law give
\[
h(\Phi^k)=k h(\psi)=k h(\Phi),\qquad h(\Phi)=h(\psi). \tag{2.8}
\]
For finite $h$ one divides the finite equality by $k$; if $h(\psi)=\infty$, the logarithmic law forces $h(\Phi)=\infty$ as well.
Equation (2.7) illustrates why the total-entropy logarithmic law must not be transferred to a fixed finite alphabet.

## 3. Arbitrary finite alphabets and attainment

For a rectangular alphabet $R=A_0\times\cdots\times A_{k-1}$, define
\[
C_r=A_0+\cdots+A_r+\psi(A_{r+1}+\cdots+A_{k-1}),
\quad 0\le r<k, \tag{3.1}
\]
where an empty sum denotes $\{0\}$.
Independence of the coordinate choices in each summand gives $T_k(\Phi,R)=\prod_r C_r$.
The elementary blocking identity
\[
T_q(\Phi^k,T_k(\Phi,R))=T_{qk}(\Phi,R)
\]
therefore yields
\[
T_{qk}(\Phi,R)=\prod_{r=0}^{k-1}T_q(\psi,C_r),\qquad
H(\Phi,R)=\frac1k\sum_{r=0}^{k-1}H(\psi,C_r). \tag{3.2}
\]

Every finite $E\subset B^k$ is contained in the rectangle obtained from its coordinate projections.
Consequently, when $h(\psi)<\infty$, if $H(\Phi,E)=h(\Phi)$, then that rectangle has the same local entropy.
All the $k$ terms on the right of (3.2) are at most $h(\psi)$, so **each** $C_r$ attains $h(\psi)$.
Conversely a realizing base alphabet $A$ induces the realizing alphabet $\iota_0A$ by (2.6).
Hence
\[
\Phi\text{ attains its entropy on a finite set}
\quad\Longleftrightarrow\quad
\psi\text{ does}. \tag{3.3}
\]
The infinite-entropy case has no finite realizing set on either side, because every local $H$ is finite.
At zero entropy every finite nonempty set attains.
Thus (3.3) is valid without a finiteness hypothesis on the total entropy, although the average-equals-maximum argument was used only for finite $h$.

Cyclic induction of a known attaining flow cannot create a nonattainment example.
Conversely, it cannot cure a nonattaining flow.
It also supplies no quantitative bound on the size of a base realizing alphabet from the mere existence of an arbitrary realizing $E$ without accounting for the sums in (3.1).

## 4. Enlarging alphabets in a cyclic module

Two elementary facts about finite sets are useful here.
Translating an alphabet does not change its trajectory cardinalities.
Also
\[
H(\psi,\psi A)=H(\psi,A), \tag{4.1}
\]
because $T_{n+1}(\psi,A)=A+T_n(\psi,\psi A)$ and hence
\[
|T_n(\psi,\psi A)|\le |T_{n+1}(\psi,A)|
\le |A|\,|T_n(\psi,\psi A)|.
\]
The lower inequality uses one translate of the second summand; it does not require an injective endomorphism.

Write $rA=A+\cdots+A$ for the $r$-fold Minkowski sum.
For every integer $r\ge1$,
\[
H(\psi,T_r(\psi,A))=H(\psi,rA). \tag{4.2}
\]
To check this, translate $A$ so that $0\in A$.
For $n\ge r$, the diagonal multiplicities in the double sum defining $T_n(\psi,T_r(\psi,A))$ are at most $r$, and equal $r$ for exponents $r-1,\ldots,n-1$.
Thus
\[
\psi^{r-1}T_{n-r+1}(\psi,rA)
\subseteq T_n(\psi,T_r(\psi,A))
\subseteq T_{n+r-1}(\psi,rA).
\]
Take normalized logarithms and use (4.1) on the left.
This proves (4.2), including noninjective maps.
In particular, replacing $A$ by a trajectory block need **not** preserve local entropy: for multiplication by $3$ on $\mathbb Z$, $A=\{0,1\}$ has $H=\log2$, but $2A=\{0,1,2\}$ has $H=\log3$, so $T_2(\psi,A)$ has local entropy $\log3$.

Suppose now $B=V(\psi,v)=\mathbb Z[t]v$ is a cyclic flow module.
Define
\[
D_m(v)=\{jv:-m\le j\le m\},\quad m\ge1.
\]
Any finite $E\subset B$ is contained in $T_r(\psi,D_m(v))$ for some integers $r,m\ge1$: take a common bound on the integer coefficients and lengths in finitely many expressions for its elements.
Since $rD_m(v)=D_{rm}(v)$ as sets, (4.2) gives
\[
H(\psi,E)\le H(\psi,D_{rm}(v)),\qquad
h(\psi)=\sup_{m\ge1}H(\psi,D_m(v)). \tag{4.3}
\]
The digit sets themselves need not be cofinal among finite subsets; they are cofinal **for this entropy supremum** by the displayed argument.
Moreover, finite-set attainment is equivalent to attainment by some $D_m(v)$.
This statement is specific to a cyclic $\mathbb Z[t]$-module and its specified generator; it is not the claim that an arbitrary $\mathbb Q$-vector space is cyclic over $\mathbb Z[t]$.

Under cyclic induction, $\iota_0 v$ generates all of $B^k$ as a flow module whenever $v$ generates $B$.
Equations (2.6) and (4.3) show, for every $m$, that
\[
H(\Phi,D_m(\iota_0v))=H(\psi,D_m(v)). \tag{4.4}
\]
In particular the set of integers $m$ that attain the total entropy is exactly the same on both sides.
Induction delays the finite-time evidence without increasing this particular alphabet threshold.

There is no uniform alphabet-size bound over all cyclic flows, even in rank one.
For multiplication by an integer $a\ge2$ on $\mathbb Z$, total entropy is $\log a$, whereas every alphabet of cardinality less than $a$ has local entropy at most the logarithm of its cardinality.
For $\{0,1\}$ specifically, all base-$a$ digit sums are distinct, so local entropy is always $\log2$, independently of $a$.
The alphabet $\{0,\ldots,a-1\}$ attains.
This control does **not** reject a uniform alphabet assertion restricted to reciprocal units of Mahler measure less than $2$; its entropy and nonunit hypotheses fall outside that reduced hard core.

## 5. Polynomial substitution and selected factors

Let $P(u)\in\mathbb Z[u]$ be primitive of degree $d\ge1$, with positive leading coefficient.
Every polynomial in $t$ has a unique decomposition into its exponent classes modulo $k$.
Under $u=t^k$, this gives the module isomorphism
\[
\mathbb Z[t]/(P(t^k))\ \cong\
\bigoplus_{r=0}^{k-1} t^r\bigl(\mathbb Z[u]/(P(u))\bigr). \tag{5.1}
\]
Indeed an element $\sum_r t^r f_r(t^k)$ belongs to the ideal $(P(t^k))$ exactly when each $f_r(u)$ belongs to $(P(u))$, by applying the same residue-class decomposition to the multiplier.
Multiplication by $t$ on the right is exactly $\Phi$ above, with $\psi$ multiplication by $u$.
This does not require $P$ or $P(t^k)$ to be irreducible, or $P$ to be monic.

Primitivity implies that these integral quotient modules are torsion-free (Gauss's lemma), and their rationalizations have dimensions $d$ and $kd$.
The rational characteristic polynomials are $P(u)/a$ and $P(t^k)/a$, where $a>0$ is the leading coefficient.
Their primitive integral normalizations are exactly $P$ and $P(t^k)$.
Thus the retained rational entropy formula, or (2.8) together with that formula, gives
\[
h(\mu_t\mid\mathbb Z[t]/(P(t^k)))=m(P(t^k))=m(P)
=h(\mu_u\mid\mathbb Z[u]/(P)). \tag{5.2}
\]
No leading-coefficient term has disappeared.
For monic $P$ with constant term $\pm1$, these are automorphisms of free abelian groups of ranks $d$ and $kd$.
If the constant term vanishes, the statements remain statements about endomorphisms; no inverse is used.
Roots on the unit circle cause no exception to (2.2)--(5.2).

For monic $P$, the powers $1,t,\ldots,t^{kd-1}$ are an integral basis in (5.1).
Therefore for the generator $v=1$ and every $m\ge1$,
\[
|T_n(\Phi,D_m(v))|=(2m+1)^n\quad(1\le n\le kd). \tag{5.3}
\]
This is an initial independence calculation, not an asymptotic entropy formula.

Selecting just one root of $P(t^k)$ changes the module, so (5.2) cannot automatically be assigned to that root's minimal polynomial.
More precisely, let $\alpha\ne0$ be algebraic, let $\beta^k=\alpha$, and put
\[
K=\mathbb Q(\alpha)\subseteq L=\mathbb Q(\beta),\qquad e=[L:K]\le k.
\]
Let $p_\alpha,p_\beta$ be the primitive integer minimal polynomials with positive leading coefficient.
On the additive group of $L$, the $k$th iterate of multiplication by $\beta$ is multiplication by $\alpha$.
A $K$-basis of $L$ identifies the latter map with $e$ copies of multiplication by $\alpha$ on $K$.
Hence the logarithmic and product laws and the rational formula give the exact accounting
\[
k\,m(p_\beta)=e\,m(p_\alpha),\qquad
m(p_\beta)=\frac{e}{k}m(p_\alpha). \tag{5.4}
\]
Neither $e=k$ nor $e=1$ is implicit.
No divisibility claim $e\mid k$ is needed.
For $\alpha=0$ the only root is zero and both measures are zero, separately.
For a root of unity both measures are again zero.
If $P(t^k)$ has several primitive irreducible factors, their measures, with multiplicity, add to $m(P)$; their degrees and measures need not be equal.

Thus a proposed refutation by selected factors must rigorously obtain positive measures with $(e/k)m(p_\alpha)\to0$, while tracking whether $\alpha$ is fixed or varies.
The induction identity alone provides no such bound.
The following standard norm and fixed-degree finiteness argument rules out this construction with seed degree bounded, without a blanket irreducibility assertion.

### 5.1. Fixed-degree seeds do not yield small measures through radicals

For every integer $D\ge1$ there is a constant $c_D>0$ such that every nonzero algebraic number $u$ of degree at most $D$ which is not a root of unity satisfies $h_{\rm abs}(u)\ge c_D$.
Here is the precise elementary fixed-degree input.
If $h_{\rm abs}(u)\le1$ and $d_u\le D$, then its primitive minimal polynomial satisfies $M(p_u)=\exp(d_u h_{\rm abs}(u))\le\exp(D)$.
The coefficient bound $|a_j|\le\binom{d_u}{j}M(p_u)\le2^D\exp(D)$ leaves finitely many possible integer polynomials, hence finitely many possible $u$.
Kronecker identifies the nonzero height-zero exceptions as roots of unity.
Take the minimum of $1$ and all positive heights in this finite set, with minimum $1$ if the set has no positive height.
This gives the stated $c_D$.
No claim of an effective useful numerical value is needed here.

Now assume $\alpha\ne0$ is not a root of unity and put $D=[K:\mathbb Q]$.
The norm
\[
u=N_{L/K}(\beta)\in K^*
\]
satisfies $u^k=\alpha^e$ by multiplicativity of the field norm.
The local absolute-height formula in the accepted source gives $h_{\rm abs}(z^j)=j h_{\rm abs}(z)$ for every positive integer $j$, directly term by term.
Hence
\[
h_{\rm abs}(u)=\frac{e}{k}h_{\rm abs}(\alpha)>0.
\]
Since $u\in K$, its degree is at most $D$, so the fixed-degree lower bound applies:
\[
\frac{e}{k}\ge\frac{c_D}{h_{\rm abs}(\alpha)},\qquad
m(p_\beta)=\frac{e}{k}D h_{\rm abs}(\alpha)\ge D c_D>0. \tag{5.5}
\]
This holds for every $k\ge1$ and every $\beta$ with $\beta^k=\alpha$, not just one chosen branch of the root.
It includes nonintegral seeds; in the algebraic-unit core both $\beta$ and its norm are units, but that additional fact is unnecessary for the argument.

More generally, if the seed degrees are all at most a fixed $D$, the same proof gives $m(p_\beta)\ge d_\alpha c_D\ge c_D$ for each seed of degree $d_\alpha$.
Thus taking arbitrarily deep radicals of a fixed seed, of finitely many seeds, or of seeds with bounded degree cannot supply a refuting sequence.
The constants depend on the seed-degree bound.
No uniform positive lower bound as $D\to\infty$ has been proved; this argument does not settle Lehmer.
It is an application of standard field norm, height and fixed-degree finiteness mechanisms, not a claimed new uniform theorem.

## 6. A precise obstruction to degree-uniform finite-time convergence

The following test is stronger than merely observing early distinct words: it keeps an attaining alphabet, positive total entropy, reciprocity, the unit condition, and unit-circle roots, all while delaying the approximation.

Take
\[
P(u)=u^4-u^3-u^2-u+1.
\]
It is monic, reciprocal and irreducible: modulo $2$ it becomes $u^4+u^3+u^2+u+1$, which has neither a linear factor nor the sole irreducible quadratic $u^2+u+1$ as a divisor.
Dividing $P(u)$ by $u^2$ and setting $y=u+u^{-1}$ gives $y^2-y-3$.
Its two roots are
\[
y_+=(1+\sqrt{13})/2\in(2,5/2),\qquad
y_-=(1-\sqrt{13})/2\in(-2,2).
\]
The four roots of $P$ are a positive real reciprocal pair $\lambda,\lambda^{-1}$ with $1<\lambda<2$ and a conjugate pair on the unit circle.
Therefore
\[
0<h(\psi)=m(P)=\log\lambda<\log2
\]
for $B=\mathbb Z[u]/(P)$ and $\psi=\mu_u$.
The existing finite-rank realization theorem and (4.3) supply some fixed integer $m\ge1$ such that $A=D_m(1)$ attains this entropy.
No explicit value of $m$ is needed or claimed.

For **every** $k\ge1$, the induced integral unit flow $\Phi_k$ on the rank-$4k$ lattice has the same positive entropy, and $F_k=D_m(\iota_0 1)$ is a realizing alphabet of the same fixed cardinality $2m+1$.
Nevertheless (5.3) says
\[
\frac{\log|T_n(\Phi_k,F_k)|}{n}=\log(2m+1)
\quad(1\le n\le4k), \tag{6.1}
\]
whereas its limiting value is $\log\lambda$.
Consequently, for any
\[
0<\varepsilon<\log(2m+1)-\log\lambda
\]
there is **no** $N$ independent of $k$ such that all $n\ge N$ approximate the total entropy within $\varepsilon$ for this family and these realizing alphabets.
Given $N$, choose $k$ with $4k\ge N$ and take $n=N$.
Equivalently, the exact subsequence identity (2.4) repeats every fixed base finite-time error at arbitrarily large induced times.

This rejects a degree-uniform finite-time convergence assertion even with fixed positive entropy and a fixed-size realizing alphabet.
It does not reject an estimate whose required time depends on degree, an existential choice of a different alphabet for each map with additional properties, or an assertion limited to irreducible characteristic polynomials: $P(t^k)$ was not proved irreducible.
It also does not disprove a positive entropy gap; the entropy in the example stays at the same positive constant.

For comparison, the zero-entropy control $B=\mathbb Z$, $\psi=\mathrm{id}$, $A=\{0,1\}$ has $|T_q|=q+1$, and hence
\[
|T_{qk+s}(\Phi_k,\iota_0A)|=(q+2)^s(q+1)^{k-s}. \tag{6.2}
\]
Its first $k$ trajectory counts are $2^n$ although its entropy is zero.
Here $\Phi_k$ is a finite-order permutation of a rank-$k$ lattice.
Formula (6.2) describes the entire decay rather than just the initially collision-free interval.
It is a control for the previously recorded finite-count obstruction, not a new gap counterexample.

## 7. Consequences, checks and remaining boundary

The useful trajectory mechanism is the exact replacement of one base time step by $k$ independent coordinate visits.
The slowdown of each coordinate is compensated by the number of coordinates.
Local entropy for $\iota_0A$, total entropy, and the cyclic digit-attainment threshold are all preserved.
Finite-time quotients and increments are delayed explicitly.
These facts invalidate a uniform time cutoff with no degree dependence; they supply no small-entropy family.

A future finite lower certificate must incorporate arithmetic information not determined by one universally bounded initial trajectory window.
In particular it must survive (2.3), distinguish a bound for local $H$ from one for total $h$, and state whether it permits reducible substitution polynomials.
Passing to a single irreducible factor requires the degree ratio in (5.4).
The present calculation neither accepts nor rejects all possible degree-dependent or algebraically certified lower bounds.

Self-checks: (2.2) and (3.2) were derived as set identities before taking cardinalities; the shift and thickening arguments explicitly permit noninjective maps; the infinite-entropy case in attainment was separated from the finite average argument; polynomial denominators and zero-root cases were retained.
The positive control includes unit-circle roots and its root description is an exact quadratic calculation, not numerical evidence.
The rank-$1$ alphabet obstruction is explicitly excluded as a test of the restricted reciprocal-unit hard core.

As a finite implementation check on 2026-10-06, standard-library Python directly enumerated sets on $B=\mathbb Z/M\mathbb Z$, $M\in\{4,5,6\}$, for every multiplier $0\le a<M$ and $k\in\{1,2,3\}$.
It checked (2.2) for $A\in\{\{1\},\{1,2\},\{0,1,2\}\}$ and $0\le n\le9$, and (3.2) for rectangles alternating $\{0,1\}$ and $\{1,2\}$ with $0\le q\le3$.
All 1,530 set-equality comparisons passed.
They exercise noninjective maps and alphabets omitting zero; they are checks of the formulas, not proofs of entropy limits or positive-entropy evidence.
Relative local link targets, control characters and the repaired spacing in (5.4) were also checked.
No formal proof assistant verification or publication-level independent review is claimed.

The original parent/contributor cross-check and separate-agent finding are retained in [R G0497](../audits/reviews/Yin_R_G0497_v1.md#historical-parent-cyclic-review), with the actual 2026-10-06 input, date precision, mathematical checks and limits.
The separate historical finding's context isolation remains unestablished; this maintenance does not claim a new independent review.

The exact originally supplied finite-check program, its recorded 1,530 comparisons and original stdout are retained in [J G0113](../computations/programs/Yin_J_G0113/readme.md), without rerunning it.
