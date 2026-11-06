---
author: Yin
---

# Cyclotomic central perturbations: Gaussian cancellation and the exact reciprocal two-block boundary

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The external_structural_lead delegate developed the finite Gaussian identities, complete measure reduction and reciprocal case analysis.
The coordinating main agent checked the Gaussian quotient and cancellation, and required the actual-degree reversal and both possible constant signs in the final case analysis.
These are author-development contributions and ordinary checks, without independent review, a new Claim assessment or a counterexample to the Task.

<a id="gaussian-cyclotomic-scope"></a>
## Question, comparison and outcome

The question is whether two cyclotomic blocks and their intervening shift can grow together so that correlated cancellation gives positive total logarithmic Mahler measures tending to zero.
This is a further variant of the cyclotomic central-perturbation exploration, following the [minus-two analysis](Yin_L_G0457_v1.md#cyclotomic-central-minus-two-scope) and the [minus-one and bounded-prime-count analysis](Yin_L_G0457_v2.md#cyclotomic-central-minus-one-scope).
Both earlier versions retain their own conclusions and limitations.

[L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) already treats arbitrary cyclotomic blocks with an independent circle phase, and its stated large-delay range.
[C868 v1](../claims/Yin_C_G0868_v1.md#fixed-pair-specialization-return) retains the corresponding distinction between fixed-pair limits and changing pairs at finite delays for its reciprocal three-block construction.
Neither limit argument is used as a uniform finite-delay estimate here.
Instead, the identities below evaluate the complete measure of a specified synchronously varying family before any limit.
The exact cancellation subfamily has measure zero, and every positive measure in its larger Gaussian two-block family has the already accepted fixed-support gap.
The reciprocal filter then identifies the central alignment that a general two-block input must satisfy if it is to have positive measure below the accepted nonreciprocal gap.
No positive-to-zero sequence is obtained, and the general centrally aligned family remains unresolved.

Throughout, m is total logarithmic Mahler measure, including the leading coefficient and every exterior root with multiplicity.
It is never divided by degree.
A cyclotomic product is a monic product of cyclotomic polynomials with nonnegative multiplicities, including the empty product 1 and excluding the factor z.
Its constant coefficient is 1 or -1 and its total measure is zero.

<a id="gaussian-finite-cancellation"></a>
## A finite growing-block identity with exactly zero cost

For integers 0<=k<=n, define the rational expression
\[
 G(n,k;z)=\prod_{i=1}^{k}\frac{1-z^{n-k+i}}{1-z^i},
 \qquad G(n,0;z)=G(n,n;z)=1.
 \tag{1}
\]
This is the usual Gaussian binomial polynomial; its required properties follow directly here.
For 1<=k<n, cancellation in the finite products gives
\[
 \frac{G(n-1,k;z)}{G(n,k;z)}=\frac{1-z^{n-k}}{1-z^n},\qquad
 \frac{G(n-1,k-1;z)}{G(n,k;z)}=\frac{1-z^k}{1-z^n}.
\]
Adding the first ratio to z^(n-k) times the second proves the polynomial recurrence
\[
 G(n,k;z)=G(n-1,k;z)+z^{n-k}G(n-1,k-1;z).
 \tag{2}
\]
Induction from the endpoint values proves that (1) belongs to Z[z].
Its constant coefficient is one, and the leading terms of (1) show that it is monic of degree k(n-k).
All its zeros are roots of the numerator binomials in (1), hence roots of unity.
It is therefore a cyclotomic product and m(G(n,k;z))=0.
The recurrence and product computation supply the properties used below without a source theorem about Gaussian polynomial norms.

For r>=1 put
\[
 A_r=G(2r+1,r;z),\qquad B_r=G(2r-1,r-1;z).
\]
Their degrees are respectively r(r+1) and r(r-1), so the shift z^r aligns their reciprocal centers.
Finite product cancellation yields
\[
 \frac{A_r}{B_r}
 =\frac{(1-z^{2r})(1-z^{2r+1})}{(1-z^r)(1-z^{r+1})}
 =\frac{(1+z^r)(1-z^{2r+1})}{1-z^{r+1}}.
\]
Subtracting z^r and expanding the numerator gives the exact identity
\[
 (1-z^{r+1})(A_r-z^rB_r)=(1-z^{3r+1})B_r.
 \tag{3}
\]
Every factor outside A_r-z^rB_r in (3) has measure zero.
The difference is a nonzero monic integer polynomial with constant coefficient one: its A_r term has strictly larger degree than its shifted B_r term.
Additivity of total logarithmic Mahler measure on the polynomial identity therefore gives
\[
 m(A_r-z^rB_r)=0.
 \tag{4}
\]
There is no removal of an uncounted exterior root or use of a normalized height in this equality.
For example, G(5,2;z)=(1+z^2)(1+z+z^2+z^3+z^4), and direct subtraction gives
\[
 G(5,2;z)-z^2G(3,1;z)=1+z+z^2+z^3+z^4+z^5+z^6=\Phi_7(z).
\]
This is an exact finite control, not numerical evidence for small positive measure.

<a id="gaussian-eight-term-full-cost"></a>
## The adjacent Gaussian family has the complete eight-term cost

Let n>=3 be odd, 1<=k<n, and j=(n-1)/2.
Put
\[
 A=G(n,k;z),\qquad B=G(n-2,k-1;z),\qquad F=A-z^jB.
\]
Both blocks are defined even at k=1 or k=n-1, using the endpoint value in (1).
Their degree difference is n-1=2j, so F is a nonzero monic reciprocal polynomial of degree k(n-k) with constant coefficient one.
The reciprocal assertion also follows from the general case analysis below; it is not needed for its measure identity.
The finite products give
\[
 \frac AB=
 \frac{(1-z^{n-1})(1-z^n)}{(1-z^k)(1-z^{n-k})}.
\]
Consequently
\[
 (1-z^k)(1-z^{n-k})F=B T_{n,k},
 \tag{5}
\]
where
\[
 T_{n,k}(z)=
 (1-z^{n-1})(1-z^n)
 -z^j(1-z^k)(1-z^{n-k}).
 \tag{6}
\]
The polynomial T_(n,k) has constant coefficient one, so it is nonzero.
Its displayed expansion has at most eight nonzero coefficients; exponent collisions or cancellation can only decrease that number.
All factors other than F and T_(n,k) in (5) have measure zero, so
\[
 m(F)=m(T_{n,k}).
 \tag{7}
\]
This identity includes the full leading-coefficient and exterior-root costs on both sides, including all multiplicities.
It is valid for each finite input without a separation condition or passage to a multivariable limit.

The accepted [DS17 fixed-support statement](../audits/literature/DS17/Yin_U001.md#ds17-u001) applied with K=8 therefore gives
\[
 m(F)=0\quad\text{or}\quad m(F)\ge\eta_8>0,
 \tag{8}
\]
uniformly in all the stated n,k and hence in their synchronized shift j.
The source's exact accepted univariate total-measure scope and original-proof inspection limits are unchanged.
No explicit value of eta_8 is asserted.
The special choice n=2r+1,k=r recovers (3)--(4); no classification of every other zero case is required for (8).
Thus increasing the degrees and supports of these two Gaussian blocks does not supply a positive-to-zero counterexample family.

<a id="actual-degree-two-block-reciprocity"></a>
## Conditional unit-reciprocal filter for arbitrary two blocks

Let A,B be cyclotomic products with
\[
 a=\deg A,\quad b=\deg B,\quad u=A(0)\in\{1,-1\},\quad v=B(0)\in\{1,-1\}.
\]
Fix j>=1 and s in {1,-1}, and set
\[
 P(z)=A(z)+s z^jB(z),\qquad d=\deg P,\qquad \ell=\operatorname{lc}(P).
 \tag{9}
\]
Here P is nonzero because P(0)=u.
For every nonzero polynomial H define its reversal using its actual degree by H*(z)=z^(deg H)H(1/z).
The cyclotomic identities are A*=uA and B*=vB, including cyclotomic products whose constant coefficient is -1.

The case analysis first assumes the precise unit and reciprocal conditions
\[
 \ell\in\{1,-1\},\qquad
 P^*=\lambda P,\qquad \lambda=\frac{P(0)}{\ell}=\frac u\ell\in\{1,-1\}.
 \tag{10}
\]
Thus anti-reciprocal polynomials are included.
No implication from small measure is needed for this conditional algebra; that implication is established separately below with the accepted Smyth input.

### Case a>j+b

The actual degree is d=a and ell=1, so lambda=u.
Reversing (9) at that actual degree gives
\[
 P^*=uA+s v z^{a-j-b}B.
\]
Equality with uP and cancellation of the nonzero polynomial sB yields
\[
 v z^{a-j-b}=u z^j.
\]
Hence necessarily
\[
 a=b+2j,\qquad u=v.
 \tag{11}
\]
Conversely, these two conditions imply P*=uP for either sign s.
No positivity or smallness of m(P) follows from this alignment alone.

### Case a<j+b

Now d=j+b, ell=s and lambda=u/s.
The actual reversal identity is
\[
 u z^{d-a}A+s vB=\lambda(A+s z^jB).
\]
Rearranging and substituting back into P gives the exact polynomial identity
\[
 (\lambda z^j-v)P=A(u z^{d-a+j}-v).
 \tag{12}
\]
Both binomials in (12) have positive exponents, leading and constant coefficients in {1,-1}, and all roots on the unit circle.
Their logarithmic measures are zero.
Since m(A)=0, additivity on (12) proves m(P)=0.
Writing this as a binomial ratio is permissible algebraically, but the measure argument uses the polynomial identity and retains every root after cancellation.

### Case a=j+b

For s=1 the leading coefficient of P is exactly 2, so the unit hypothesis (10) fails and m(P)>=log 2 directly.
No primitive-content division removes that expense: P(0)=u is a unit, so P is already primitive.

For s=-1 the leading terms cancel, and the actual degree is some d'<a.
If the resulting leading coefficient has absolute value at least two, the same direct leading-coefficient lower bound applies.
Otherwise set ell=lc(P) in {1,-1}, lambda=u/ell and q=a-d'>0, and impose (10) with actual degree d'.
Reversing at the old degree a must include the lost-degree factor:
\[
 z^aP(1/z)=uA-vB
 =z^{a-d'}P^*
 =\lambda z^q P.
 \tag{13}
\]
It follows that
\[
 (u-\lambda z^q)A=(v-\lambda z^{q+j})B,
\]
and substitution into P=A-z^jB gives
\[
 (v-\lambda z^{q+j})P=(v-u z^j)A.
 \tag{14}
\]
Again both binomials have positive exponents and measure zero, so (14) proves m(P)=0.
This also covers a constant unit P; no false use of degree a in its reciprocal condition is made.

Together, the three cases prove that a unit-reciprocal P in (9) of positive measure must have the strict central alignment (11), with A the higher-degree unshifted block.
They neither classify the positive measures within that aligned case nor cover j=0 after possible removal of a zero-root factor.

<a id="small-measure-two-block-consequence"></a>
## Exact connection with the accepted nonreciprocal gap

Let theta_0>1 denote the positive real root of t^3-t-1.
The accepted [Smyth statement in Smy08 U002](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number), Section 5.1 equation (15) of the inspected 2008 preprint, says that every nonzero nonreciprocal algebraic integer has logarithmic measure at least log(theta_0).
The source unit retains statement-level use and its original-proof inspection limit.
The factorwise extension below is the same interface already used in [L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap), written here to fix its normalization for P with either leading sign.

For every P in (9), Jensen's formula gives m(P)>=log|ell|.
Thus m(P)<log 2 forces ell in {1,-1}.
Under this condition ell is a unit, and because P(0)=u in {1,-1}, the monic integer polynomial P_hat=P/ell factors into monic irreducibles g_i, each with nonzero unit constant coefficient.
All their measures are nonnegative and their sum with multiplicity is m(P).
If every factor were reciprocal, its leading coefficient one would give g_i*=g_i(0)g_i.
Multiplying these equations gives P_hat*=P_hat(0)P_hat, equivalently P*=(u/ell)P.
Therefore, with ell already a unit, failure of the reciprocal identity in (10) implies that some actual irreducible factor g_i is nonreciprocal.
Its roots are nonzero algebraic integers, so the accepted Smyth statement gives m(g_i)>=log(theta_0) and hence m(P)>=log(theta_0).
This does not assert that every noncyclotomic factor of an arbitrary P has that lower bound.

Since 1<theta_0<2, any input (9) satisfying
\[
 0<m(P)<\log\theta_0
\]
necessarily satisfies (10).
The three cases then force (11).
This establishes a necessary central alignment for a hypothetical positive-to-zero sequence with j>=1, without assuming irreducibility, Salem geometry or preservation of degrees under powers.

<a id="gaussian-two-block-reuse-and-limit"></a>
## Common roots, search scope and the remaining obstruction

If C is the monic gcd of A and B, then C is cyclotomic and
\[
 P=C\bigl(A/C+s z^j B/C\bigr),\qquad
 m(P)=m\bigl(A/C+s z^j B/C\bigr).
\]
This removes shared circle zeros at zero total cost, including their actual common multiplicities.
It does not itself reduce a positive measure or justify discarding any noncyclotomic factor.
The central degree difference in (11) is unchanged when a common factor is removed.
In the Gaussian family the stronger exact reduction (5)--(7) shows why the growing blocks still have only a bounded-support full cost.

The bounded 2026-11-06 reuse search read the relevant L133 v2 and C868 v1 boundaries and the existing BM05, MS12b and MS26 source accounts.
Targeted local searches for Gaussian-binomial and two-block phase-cancellation formulas did not locate this exact Gaussian specialization; that is a search limitation, not a priority or absence claim.
The two public queries were "Mahler measure difference products cyclotomic polynomials Gaussian binomial" and "Mahler measure small cyclotomic sum difference interlacing polynomials construction".
They disclosed no concrete synchronized positive-to-zero construction usable in this bounded inquiry.
The publisher abstract of Boyd and Rodriguez-Villegas, [Mahler's Measure and the Dilogarithm (I), Canadian Journal of Mathematics 54 (2002), 468--492](https://doi.org/10.4153/CJM-2002-016-9), was read directly; its stated object is the two-variable measure of p(x)y-q(x) for cyclotomic p,q.
Its full text and proof were not read in this inquiry, and no finite correlated-specialization conclusion is adopted from that abstract.
The exact identities and three-case filter above are direct calculations, not results attributed to that paper.

No numerical parameter sweep, root approximation or new computation program is part of this version.
The remaining target would need centrally aligned blocks with unbounded complexity after zero-measure completion and a mechanism controlling their complete nonreal and real exterior-root costs together.
The Gaussian identities here supply neither that mechanism nor a uniform exclusion of all centrally aligned two-block inputs.
