---
author: Yin
---

# Homogeneous cyclotomic layers: primitive measure costs and Chebyshev source boundaries

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The external_structural_lead delegate developed the phase-sum limit, Gauss-content bound, exact Mobius control and Chebyshev comparisons.
The coordinating main agent proposed testing homogeneous cyclotomic layers and required complete primitive-content, radial and moving-source accounting.
These are author-development contributions and ordinary checks, without independent review, a new Claim assessment or a counterexample to the Task.

<a id="homogeneous-layer-scope"></a>
## Question and normalization

The [L450 positive-factor bridge](Yin_L_G0450_v1.md#positive-factor-counterexample-bridge) requires bounded total logarithmic Mahler measure and an unbounded number r_+ of positive-measure primitive irreducible factors within each actual input, counted with multiplicity.
This exploration tests whether the forced layers in A(z)^n-B(z)^n can supply that combination.
It is distinct from L450 v1's fixed radical substitutions and translated-torsion example, and from [L450 v2's fixed nontorsion-source Blaschke pullbacks](Yin_L_G0450_v2.md#fixed-degree-norm-return).
The present outer source consists of roots of unity; their preimages may have nonunit leading coefficients, common content or nontrivial radial costs.
The existing [C265 layers](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) concern values and ideal norms at a fixed algebraic unit, not the polynomial-output factor count considered here.

All measures m below are total logarithmic Mahler measures, including the leading coefficient and every root with multiplicity, under the accepted [normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
For a nonzero integer polynomial H, cont(H)>0 is the gcd of its coefficients and prim(H)=H/cont(H), allowing either leading sign.
Thus m(prim(H))=m(H)-log cont(H).
The sign, a power of z and cyclotomic factors contribute zero measure; integer content is not counted in r_+.
No degree-normalized height substitutes for these quantities.

The main fixed-pair result assumes nonzero A,B in Z[z], with A/B nonconstant and gcd(cont(A),cont(B))=1.
A common integer factor h may always be divided from both inputs first, because it contributes only h^n to A^n-B^n and leaves its primitive part unchanged.
No coprimality of A and B over Q[z] is needed for the fixed-pair measure and content results.
The proportional case is treated separately below, rather than passing through a zero polynomial in a phase continuity argument.

<a id="homogeneous-layer-accounting"></a>
## The exact layers and what their number does not establish

Write Phi_d(X,Y)=Y^phi(d) Phi_d(X/Y) for the homogeneous cyclotomic polynomial.
For a nonconstant rational function A/B, none of the following polynomials is identically zero, and the usual finite factorization gives
\[
 F_n=A^n-B^n=\prod_{d\mid n}H_d,
 \qquad H_d=\Phi_d(A,B).
 \tag{1}
\]
Content is multiplicative for integer polynomials, as follows also from the Gauss-valuation proof below.
Consequently
\[
 \operatorname{cont}(F_n)=\prod_{d\mid n}\operatorname{cont}(H_d),\qquad
 \operatorname{prim}(F_n)=\prod_{d\mid n}\operatorname{prim}(H_d),
 \tag{2}
\]
and their logarithmic measures add with every multiplicity retained.
A layer may have integer content, split into several rational irreducible factors or consist entirely of zero-measure factors.
Therefore the divisor count of n is not by itself a lower bound for r_+(prim(F_n)).

If A and B are coprime over Q[z], different H_d are coprime over Q[z]: at a common root B cannot vanish, and A/B would otherwise have two different exact orders as a root of unity.
If A=G A_0 and B=G B_0 with primitive G in Z[z] and integer quotients, then H_d=G^phi(d)Phi_d(A_0,B_0), and the common factor appears to the total power n in F_n.
A primitive positive-measure G already costs n m(G); a zero-measure G adds no positive factor.
These common multiplicities must be separated before interpreting layer proliferation.
When G is the complete common polynomial part, every root beta of A_0^n-B_0^n satisfies A_0(beta)/B_0(beta) in the set of nth roots of unity, and hence |A_0(beta)|=|B_0(beta)|.
This is an exact fixed lemniscate constraint, not a claim that beta approaches the unit circle as n grows.

<a id="fixed-pair-phase-limit"></a>
## The full fixed-pair phase sum

For a fixed nonproportional pair define
\[
 h(\zeta)=m(A-\zeta B),\qquad \zeta\in\mathbb T,
 \qquad I(A,B)=\int_{\mathbb T}\log\max(|A(z)|,|B(z)|)\,d\mu(z),
 \tag{3}
\]
where mu is normalized Haar measure.
The coefficient map zeta to A-zeta B stays in a fixed finite coefficient space and never equals the zero vector.
The complete [C_F7 finite-coefficient continuity proof](../claims/Yin_C_F0007_v1.md#coefficient-global-continuity) therefore makes h continuous, including phases at which its actual degree drops.
That proof was read at its actual fixed-degree scope: it homogenizes to a fixed binary-form degree and uses compact normalized linear factors, retaining roots at infinity and their leading-coefficient compensation.
No continuity uniform over increasing input degrees is imported.

Factoring over all nth roots gives the exact finite identity
\[
 m(F_n)=\sum_{k=0}^{n-1}h(e^{2\pi i k/n}).
 \tag{4}
\]
Also Jensen in the phase variable gives
\[
 \int_{\mathbb T}h(\zeta)\,d\mu(\zeta)=I(A,B).
 \tag{5}
\]
For completeness, off the finitely many common zeros of A and B on the circle, divide A-zeta B by max(|A|,|B|).
After a phase rotation its logarithm has the distribution of log|1-r zeta| for some 0<=r<=1.
This normalized logarithm has mean zero, positive part at most log 2 and L1 norm at most 2 log 2, also at r=1 by Jensen and the integrable logarithmic singularity.
The normalizing logarithm log max(|A|,|B|) is integrable, since both polynomial boundary logarithms are integrable.
Thus the two-variable logarithm is absolutely integrable and Fubini justifies (5), including common boundary roots and leading-coefficient cancellations.

The Riemann sums in (4) now prove
\[
 \frac{m(F_n)}n\longrightarrow I(A,B).
 \tag{6}
\]
More explicitly, if omega_h(delta) is the modulus of continuity of theta to h(e^(i theta)) in circular distance, interval comparison gives
\[
 |m(F_n)-nI(A,B)|\le n\,\omega_h(2\pi/n).
 \tag{7}
\]
This is a statement about a full measure growing proportionally to n, not a replacement of that measure by height.
It leaves the size of the continuity modulus dependent on the complete pair.

<a id="fixed-pair-gauss-content"></a>
## Complete fixed-pair content bound, including the binary prime

For a prime p and a nonzero rational polynomial U define
\[
 w_p(U)=\min_j v_p(U_j).
\]
After dividing U and V by their respective p-adic coefficient powers, both reductions are nonzero in F_p[z].
Their product remains nonzero, so w_p(UV)=w_p(U)+w_p(V).
It follows that w_p extends to Q(z) by w_p(U/V)=w_p(U)-w_p(V), with value group Z, w_p(p)=1 and residue field F_p(z).
For an integer polynomial, w_p(U)=v_p(cont(U)).
This proves the content multiplicativity used in (2).

Put R=A/B and c_n=cont(F_n).
The normalization gcd(cont(A),cont(B))=1 means that at every p at least one of w_p(A),w_p(B) is zero.
If these two valuations differ, the two terms in F_n have distinct valuations and w_p(F_n)=0.
Otherwise both are zero, and
\[
 v_p(c_n)=w_p(R^n-1).
 \tag{8}
\]
Positive valuation requires the nonzero residue R_bar in F_p(z) to satisfy R_bar^n=1.
Such a rational function must be constant.
Indeed, a nonconstant rational function r(z) makes z algebraic over F_p(r), by its numerator-denominator equation; if r were algebraic over F_p, this would make z algebraic over F_p, a contradiction.
Thus R_bar=c in F_p^times, of some order e dividing p-1.

Choose a nonzero integer coefficient minor Delta=A_i B_j-A_j B_i; one exists because A and B are not proportional over Q.
When both reductions are nonzero and proportional, p divides every such minor and hence p divides Delta.
Only the finite set of primes dividing Delta can contribute to c_n.
Primes where either the two valuations differ or the residue ratio is nonconstant contribute zero for every n.

Here are the exact lifting calculations for each remaining prime.
In this valuation ring, if w_p(t-1)=a>0 and m is a positive integer prime to p, expansion of t^m-1 around t=1 has linear term of valuation a and all higher terms of strictly greater valuation.
Hence w_p(t^m-1)=a.
For odd p and integer a>=1, the linear term in t^p-1 has valuation a+1; intermediate binomial terms have valuation at least 1+2a, and the last term has valuation pa>a+1.
The linear term is uniquely smallest, so each pth-power step raises the valuation by exactly one.
Therefore, for odd p with residue order e,
\[
 v_p(c_n)=
 \begin{cases}
 0,&e\nmid n,\\
 a_p+v_p(n),&e\mid n,
 \end{cases}
 \qquad a_p=w_p(R^e-1)\ge1.
 \tag{9}
\]
All these a_p are finite because R is nonconstant; e is prime to p.

For p=2 the only nonzero residue constant is one.
Put a=w_2(R-1)>=1 and b=w_2(R+1)>=1, both finite.
For odd n the prime-to-two calculation gives v_2(c_n)=a.
For even n first use R^2-1=(R-1)(R+1), of valuation a+b>=2.
Starting at depth at least two, the two terms in t^2-1=2(t-1)+(t-1)^2 have valuations a'+1<2a', so each subsequent doubling raises the valuation by exactly one.
The remaining odd cofactor changes nothing.
Thus
\[
 v_2(c_n)=
 \begin{cases}
 a,&n\text{ odd},\\
 a+b+v_2(n)-1,&n\text{ even}.
 \end{cases}
 \tag{10}
\]
If the binary prime does not meet the preceding residue and normalization conditions, its contribution is zero instead.
In particular no unjustified stable-depth assumption is made at the first binary doubling.

Choose C_p=a_p for the odd contributing primes, C_2=a+b-1 when two contributes, and zero otherwise, and put C=product_p p^(C_p).
Equations (9)--(10) prove
\[
 c_n\mid Cn,\qquad 0\le\log c_n\le\log C+\log n.
 \tag{11}
\]
The integer C depends on the complete fixed pair, including its exceptional residue orders and depths.
Combining (6) with (11) gives the full primitive-cost limit
\[
 \frac{m(\operatorname{prim}(F_n))}{n}\longrightarrow I(A,B).
 \tag{12}
\]
This argument is an elementary Gauss-valuation and binomial calculation; it does not invoke a new primitive-divisor or number-field theorem.
For changing pairs, neither C nor the modulus in (7) has been bounded uniformly.

<a id="zero-phase-cost-classification"></a>
## Zero phase cost and the excluded proportional case

Since A and B are nonzero integer polynomials, m(A),m(B)>=0.
The maximum in (3) gives I(A,B)>=max(m(A),m(B)).
Suppose I(A,B)=0.
Then m(A)=m(B)=0, and the two nonnegative differences log max(|A|,|B|)-log|A| and log max(|A|,|B|)-log|B| have integral zero.
Consequently |A|=|B| almost everywhere on the unit circle, and continuity of their absolute values extends equality to every circle point.

Zero measure implies that the leading coefficient of each polynomial has absolute value one and that all its roots lie in the closed unit disk.
After removing its zero-root power, its nonzero constant coefficient is an integer of absolute value at least one, equal in absolute value to the product of those root moduli.
Hence every nonzero root has modulus one and the remaining constant coefficient has absolute value one.
Equality of the two boundary absolute values forces the same multiplicity at each such root: near a circle root the modulus has a positive constant times the corresponding power of the angular distance, and unequal powers cannot agree.
Thus there is one monic integer polynomial C_0 with all roots on the circle and integers r,s>=0 such that
\[
 A=\epsilon z^r C_0,\qquad B=\delta z^s C_0,
 \qquad \epsilon,\delta\in\{1,-1\}.
 \tag{13}
\]
The nonproportional hypothesis forces r!=s.
It follows that F_n is C_0^n times a monomial and a binomial with unit coefficients, and hence
\[
 m(F_n)=m(\operatorname{prim}(F_n))=0\quad\text{for every }n\ge1.
 \tag{14}
\]
Conversely (13) has I(A,B)=0 directly.
Together with (12), this proves that a fixed nonproportional normalized pair either gives zero measure at every exponent or has primitive total measure asymptotic to a positive constant times n.
It cannot furnish bounded total measure with unbounded r_+.

If A/B is constant, choose a primitive integer polynomial G and nonzero integers a,b with A=aG,B=bG.
Such a representation follows by clearing the rational proportionality and dividing the coefficient contents.
For every n with a^n!=b^n,
\[
 \operatorname{prim}(A^n-B^n)=\pm G^n,
 \qquad m(\operatorname{prim}(A^n-B^n))=n m(G).
\]
If m(G)=0 there are no positive factors; if m(G)>0 the total cost grows linearly.
Exponents with a^n=b^n give the zero polynomial and are excluded entirely.
This handles the proportional case without applying h at a zero polynomial.

<a id="circle-mobius-layer-control"></a>
## Exact proliferation on the unit circle and its leading-coefficient price

Take
\[
 A(z)=2z-1,\qquad B(z)=z-2,
 \qquad F_n=A^n-B^n.
 \tag{15}
\]
For each nth root of unity zeta the unique root of A-zeta B is
\[
 \beta=\frac{1-2\zeta}{2-\zeta},\qquad |\beta|=1.
 \tag{16}
\]
The denominator is nonzero, and equality of the two squared absolute values follows from |zeta|=1.
The Mobius determinant is -3, so distinct phases give distinct roots and all n roots are simple.
The leading coefficient of F_n is 2^n-1.
Therefore its entire raw measure is log(2^n-1), despite every radial root contribution being zero.

The coefficient minor is 3, so the content calculation permits only p=3.
Modulo three, A/B=-1, of order two.
Moreover A^2-B^2=3(z^2-1), and both A,B have Gauss valuation zero at three, giving w_3(R^2-1)=1.
Equation (9) therefore gives the exact content and primitive measure
\[
 c_n=\begin{cases}1,&n\text{ odd},\\3^{1+v_3(n)},&n\text{ even},\end{cases}
 \qquad
 m(\operatorname{prim}(F_n))=\log(2^n-1)-\log c_n.
 \tag{17}
\]
In particular the primitive cost still grows as n log 2.

For odd n all its homogeneous cyclotomic layers are primitive by (2) and c_n=1.
Each layer H_d=Phi_d(2z-1,z-2) is irreducible over Q.
Indeed the classical irreducibility and degree of Phi_d, reused at the accepted [Bel17 U002 scope](../audits/literature/Bel17/Yin_U002.md#bel17-u002), make its homogenization irreducible in Q[X,Y].
The invertible linear change (X,Y)=(2z-w,z-2w), of determinant -3, preserves irreducibility.
Dehomogenization at w=1 has the same degree phi(d), because its leading coefficient Phi_d(2,1)=Phi_d(2) is nonzero; a nontrivial factorization would homogenize back to one of the transformed form.
This proves the asserted irreducibility without assuming it for general higher-degree A/B.

The layer d=1 is z+1, of measure zero.
For every d>1 all primitive dth roots zeta differ from one, so |2-zeta|>1 and
\[
 \Phi_d(2)=\prod_{\operatorname{ord}(\zeta)=d}|2-\zeta|>1.
\]
This is a positive integer, and (16) shows that all roots of H_d lie on the circle.
Consequently, for odd n,
\[
 r_+(F_n)=\tau(n)-1,\qquad
 m(H_d)=\log\Phi_d(2)>0\ (d\mid n,d>1),\qquad
 m(F_n)=\log(2^n-1).
 \tag{18}
\]
Here tau(n) is the number of divisors, and the factors are distinct and have multiplicity one.
For example n equal to a product of r distinct odd primes gives r_+=2^r-1 within that one polynomial.
This is genuine proliferation, but each positive factor is nonmonic and pays its actual leading coefficient.
No conclusion is based on the number of different factors observed across separate values of n.

More generally, if a primitive integer polynomial has every root on the unit circle, every irreducible factor does as well.
Its measure equals the logarithm of the absolute value of its integer leading coefficient.
A positive-measure factor must therefore have leading coefficient of absolute value at least two.
Adding all factors with multiplicity proves the uniform bound
\[
 m(H)\ge r_+(H)\log2.
 \tag{19}
\]
This applies even when the underlying rational map changes.
Thus perfect radial neutrality is insufficient: bounded total primitive cost still bounds r_+ in this entire all-circle class.

<a id="ordinary-chebyshev-uniform-cost"></a>
## Ordinary monic Chebyshev composition has a uniform linear cost

Use C_0=2,C_1=X,C_(n+1)=X C_n-C_(n-1), so C_n(u+u^(-1))=u^n+u^(-n).
For n>=1 its complete monic factorization over C is
\[
 C_n(X)-2=\prod_{k=0}^{n-1}\left(X-2\cos(2\pi k/n)\right).
 \tag{20}
\]
Multiplicity is included: away from u=1,-1 the inverse pair has the same trace and gives a double root, while at the endpoints the trace map has ramification two and gives a simple root in X.
Equivalently substitute X=u+u^(-1) into both sides: multiplication by u^n changes each side to (u^n-1)^2, and the substitution is injective on C[X].
The polynomial identity (20) thus also covers n=1 and n=2.

Let Q in Z[z] be nonconstant and monic, allowed to depend on n, and put a=Q(0).
Every factor Q-t in (20) is monic, hence its complete measure is at least log^+|a-t| by the product of all root moduli and the leading-coefficient bound.
If a>=0, choose phases in [3pi/4,5pi/4], where t=2cos(theta)<=-sqrt(2); if a<0 choose the circular arc [-pi/4,pi/4], where t>=sqrt(2).
In either case |a-t|>=sqrt(2).
A closed arc of angular length pi/2 contains at least n/4-1 of the n equally spaced phases: after lifting it to a real interval of length n/4, the number of integers it contains is at least that length minus one, with circular endpoints identified.
All other factors have nonnegative measure because they are monic.
Thus
\[
 m(C_n(Q(z))-2)\ge (n/4-1)\log\sqrt2.
 \tag{21}
\]
A negative right side at small n is merely a vacuous lower bound.
This is a bound for every original full polynomial, with all repeated factors in (20), and it is uniform in the degree and coefficients of the monic Q.
The output is monic, so no integer content can remove the cost.
In particular growing ordinary monic sources Q_n cannot make this total measure bounded while n tends to infinity.

<a id="rational-and-reciprocal-chebyshev-boundaries"></a>
## Rational traces and reciprocal lifts are different domains

For R=A/B the rational trace R+R^(-1)=(A^2+B^2)/(AB) satisfies the exact cleared identity
\[
 (AB)^n\left[C_n\left(\frac{A^2+B^2}{AB}\right)-2\right]
       =(A^n-B^n)^2.
 \tag{22}
\]
It follows directly from the defining Chebyshev identity and is a polynomial equality after clearing denominators.
The bracket is generally a rational function, not an ordinary monic integer-polynomial composition to which (21) applies.
If its logarithmic measure is interpreted as the integral of the rational function, (22) retains the term n(m(A)+m(B)); it cannot be dropped as a free normalization.
The primitive content of the cleared output must likewise be handled by (2) or the applicable content calculation.

A separate reciprocal construction takes a fixed nonconstant monic Q in Z[X] of degree D and sets
\[
 V_t(z)=z^D\bigl(Q(z+z^{-1})-t\bigr),\qquad
 K_{n,Q}(z)=z^{nD}\bigl(C_n(Q(z+z^{-1}))-2\bigr).
 \tag{23}
\]
For real t, V_t is a monic degree-2D polynomial with constant coefficient one, so h_Q(t)=m(V_t)>=0.
The same finite-coefficient continuity proof used above makes h_Q continuous on [-2,2].
The output K_(n,Q) is an actual monic reciprocal integer-unit polynomial, with no integer content, and (20) gives
\[
 m(K_{n,Q})=\sum_{k=0}^{n-1}h_Q(2\cos(2\pi k/n)),\qquad
 \frac{m(K_{n,Q})}{n}\longrightarrow
 J_Q=\int_{\mathbb T}h_Q(2\cos\theta)\,d\mu(\theta).
 \tag{24}
\]
If J_Q=0, continuity and nonnegativity force h_Q(t)=0 for every t in [-2,2], since the cosine pushforward has full support on that interval.
Then every K_(n,Q) has measure zero.
If J_Q>0, its total measure grows as nJ_Q.
This gives a complete zero-or-linear dichotomy for each fixed Q, with no irreducibility or Salem assumption.

For changing Q_n the relevant continuity modulus and J_(Q_n) are not controlled uniformly here.
The ordinary constant-term estimate (21) does not transfer: every V_t in (23) has constant coefficient one, independently of t.
Neither (24) nor a count of Chebyshev or cyclotomic layers ensures that those layers contain enough positive-measure irreducible factors.
Thus this changing reciprocal-trace domain remains distinct from the ordinary monic domain already excluded by (21).

<a id="homogeneous-layer-moving-source-limit"></a>
## What remains for a changing source

For varying normalized pairs A_n,B_n, the exact identities (1)--(5) remain valid separately, but (7) and (11) now involve pair-dependent moduli and constants.
The fixed-pair limit is not a uniform theorem that forces primitive cost nI(A_n,B_n) up to a negligible error for an arbitrary diagonal sequence.
A proposed escape must control the actual content, discrete phase sum, leading coefficient and all exterior roots, and must separately exhibit the positive irreducible-factor count inside the same output.
No such construction is supplied here.
The all-circle inequality (19) already excludes one natural attempt to suppress radial costs uniformly, while (21) excludes ordinary monic Chebyshev composition even with changing sources.
The remaining reciprocal-trace or general rational-map inputs need new control of precisely those quantities.

The bounded local reuse pass read L450 v1/v2, the relevant L133 v2 boundaries, C265's distinct algebraic-value layer scope, and C_F7's complete finite-coefficient continuity argument including degree drops.
The classical cyclotomic irreducibility input is reused only at Bel17 U002's accepted statement scope, already used in L450 v1; no new original cyclotomic proof audit is claimed.
The Gauss-valuation lifting, scalar normalization, zero-cost classification, Mobius costs and quarter-arc count are proved above directly.
No new external theorem, source acquisition, numerical parameter scan or native computation is part of this version.
The results are bounded mechanism diagnostics, not an unrestricted Mahler gap or a counterexample sequence.
