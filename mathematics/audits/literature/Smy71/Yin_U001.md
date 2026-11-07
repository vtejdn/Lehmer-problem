---
author: Yin
---

# Smy71-U001: complete nonreciprocal-bound proof and corollary inspection

<a id="smy71-u001"></a>
## Source, question and review scope

This inspection uses the [published 1971 edition](readme.md#published-1971-edition), all of printed pp.169--175 / PDF pp.1--7.
On 2026-11-07 the coordinating agent for Yin read the complete text, checked every page visually, reconstructed the coefficient estimates and both proof branches, and checked the corollaries and the final introductory example.
The OCR layer omits or corrupts several displayed formulas; the mathematical transcription below was checked against the page images.
Exact rational arithmetic was used only to corroborate the stated numerical separation and the final algebraic simplification.
The displayed reasoning supplies the proof evidence without a numerical root computation or a retained computation program.

The agent had previously read the Smy08 survey inspection and discussed the status of the 1971 source.
This is a direct full-article mathematical inspection, not a context-isolated independent review or proof-assistant verification.
The paper's references to Siegel, Chamfy and Cassels identify earlier work and comparisons, rather than premises in Sections2--5's proof of the main theorem.
Their original proofs were not recursively audited.
Standard Parseval, the maximum-modulus principle, elementary polynomial/field facts and transitivity of algebraic integrality are used at their ordinary established scope.

The main theorem, its sharpness, the three corollaries and the stated asymptotic house obstruction are supported by the checked arguments below.
The displayed coefficient lemma needs a separate constant-function branch at |e_0|=1; every application in the main proof already satisfies 0<e_0<1.
That endpoint qualification does not invalidate the theorem.
This unit supplies primary-source proof evidence, while actual adoption by a project Claim remains the consumer's responsibility.

<a id="smy71-statement-and-conventions"></a>
## Exact theorem and conventions

Let alpha be an algebraic integer other than0 or1, and let P be its monic irreducible polynomial of degree n.
Set Q(z)=z^n P(1/z) and let theta be the real root greater than1 of x^3-x-1.
With roots counted with multiplicity, put

\[
 \Lambda=M(P)=\prod_{j=1}^n\max(1,|\alpha_j|).
\]

The theorem on printed p.169 states that Lambda<theta implies P=Q.
The project convention allowing P*=plus or minus P agrees with this conclusion after excluding the irreducible anti-reciprocal exception P=z-1.
The source excludes alpha=1 explicitly for that reason.
Its product over roots of modulus at least one has the same value as the displayed max-product.
The complete [Mahler/height normalization](../Smy08/Yin_U001.md#smy08-height-normalization) remains unchanged: m(P)=log M(P), without division by degree.

Equivalently, a nonzero nonreciprocal algebraic integer has M(alpha)>=theta.
The cubic x^3-x-1 is irreducible by the rational-root test and has one real root theta and a conjugate nonreal pair of modulus theta^(-1/2)<1.
It is nonreciprocal and has measure theta, so the constant is sharp.
Its unique-real-root assertion follows, for example, by evaluating the cubic at its two stationary points: even the local maximum is negative.
This is the nonreciprocal theorem; no positive gap for arbitrary reciprocal polynomials follows.

<a id="smy71-coefficient-lemma"></a>
## Section2: coefficient inequalities and the endpoint qualification

Let h(z)=sum e_j z^j have real coefficients, be holomorphic on a neighborhood of the closed disk, and satisfy |h|<=1 on its boundary.
For 0<|s|<1, where s=e_0, the source lemma gives, for every i>=1,

\[
 |e_i|\le1-s^2,
\qquad
 -(1-s^2)+\frac{e_i^2}{1+s}
 \le e_{2i}\le
 1-s^2-\frac{e_i^2}{1-s}.                 \tag{L1--L2}
\]

For the first inequality, Parseval applied to h(z)(beta+z^i), followed by retention of the coefficients at0 and i, gives

\[
 (s\beta)^2+(s+e_i\beta)^2\le1+\beta^2.
\]

Choosing beta=s^(-1)sign(e_i) proves L1; if e_i=0 it follows directly from |s|<=1.
For L2 use h(z)(beta_2+beta_3 z^i+z^(2i)) and retain the coefficients at0, i and2i:

\[
 (s\beta_2)^2+(s\beta_3+e_i\beta_2)^2
 +(s+e_i\beta_3+e_{2i}\beta_2)^2
 \le1+\beta_2^2+\beta_3^2.
\]

Put beta_2=rho/s and beta_3=rho e_i/((delta-s)s), with rho,delta in {1,-1}.
The first two squares are1 and beta_3^2, respectively.
The resulting inequality is

\[
 \left|\rho s^2+\frac{e_i^2}{\delta-s}+e_{2i}\right|\le1.
\]

Using both rho signs and then both delta signs gives L2, with positive denominators 1-s and1+s.
This checks the complete Parseval proof on printed pp.170--171.

The printed lemma assumes only e_0 nonzero and therefore literally includes e_0=1 and e_0=-1.
For h identically1, for example, its displayed expression e_i^2/(1-e_0) is0/0.
At |e_0|=1 the maximum-modulus principle forces h to be constant and all higher coefficients to vanish.
State that case separately, or restrict the displayed L2 fractions to |e_0|<1.
No such undefined endpoint occurs below.

<a id="smy71-inner-products"></a>
## Section3: the unit reduction and bounded holomorphic products

Assume P is not reciprocal.
It suffices to consider Lambda<=4/3, because theta<4/3.
The integer P(0) is nonzero, and |P(0)|<=Lambda, so P(0)=plus or minus1.
This unit reduction is explicit on printed p.171; it is not a hypothesis silently supplied by the later survey.

There are no unit-circle roots.
Indeed, such a root beta has beta^(-1)=conjugate(beta) as a conjugate, so P and Q have a common root and are associates.
The plus association gives reciprocity, while the minus association gives P(1)=0 and the excluded alpha=1.
This also proves that P and Q are relatively prime in the present nonreciprocal case.

A finite Blaschke product means a constant of modulus one times a finite product of factors (z-a)/(1-conjugate(a)z), with |a|<1, allowing the empty product.
It is holomorphic near the closed disk and has boundary modulus one.
The source constructs real-coefficient products

\[
 f(z)=\pm\prod_{|\alpha_j|<1}
        \frac{z-\alpha_j}{1-\overline{\alpha_j}z},
\qquad
 g(z)=\pm\prod_{|\alpha_j|>1}
        \frac{1-\overline{\alpha_j}z}{z-\alpha_j},
\]

with signs chosen to make the constant terms positive.
Conjugation preserves each root set, so these products have real Taylor coefficients.
All their denominator zeros lie outside the closed disk.
The unit norm and the product identities give

\[
 f(0)=g(0)=c=\Lambda^{-1},\qquad
 \frac{P(0)P(z)}{Q(z)}=\frac{f(z)}{g(z)}
   =1+a_kz^k+a_lz^l+\cdots.                 \tag{S1}
\]

The a_j are integers because Q(0)=1.
If c=1, the maximum-modulus principle would make both f and g constant and their quotient equal to1, contradicting nonreciprocity.
Thus c<1 before either displayed L2 fraction is used.
The rational quotient is nonconstant and cannot be a nonconstant polynomial of degree zero at infinity, so its series has at least two nonzero positive-index terms.
Thus k<l are well defined.
Write f=c+sum c_j z^j and g=c+sum d_j z^j.
The exact coefficient comparisons used in source equations(3)--(4) are

\[
 c_j=d_j\ (j<k),\quad c_k-d_k=a_kc,\quad
 c_{k+i}-d_{k+i}=a_kd_i\ (1\le i<l-k),\quad
 c_l-d_l=a_lc+a_kd_{l-k}.                  \tag{S2}
\]

L1 and |a_k|>=1 imply c/2<=1-c^2, hence

\[
 \Lambda\ge\frac{1+\sqrt{17}}4.
\]

The inequality is strict: Lambda is an algebraic integer, being up to sign a product of real roots and complete conjugate pairs outside the circle, whereas (1+sqrt(17))/4 has irreducible primitive polynomial 2x^2-x-2 and is not an algebraic integer.
Consequently

\[
 \frac34\le c<\frac{\sqrt{17}-1}4<1.       \tag{S3}
\]

If |a_k|>=2, then c<=1-c^2, contradicting S3.
Thus |a_k|=1.
The same bound excludes c_k,d_k having the same sign or either being zero, and gives

\[
 |c_k|+|d_k|=c.                            \tag{S4}
\]

If |a_l|>=2, S2 forces one of |c_l|, |d_l|, |d_(l-k)| to be at least2c/3.
L1 then gives Lambda>=(1+sqrt(10))/3>4/3, again impossible.
Therefore |a_l|=1.

<a id="smy71-early-coefficient-branch"></a>
## Section4: the branch k<l<2k

Replacing the unit by its inverse interchanges the normalized P,Q and replaces the series in S1 by its formal inverse, so assume a_k=1.
Put q=l-k and s=2k-l; both are strictly between0 and k.
Parseval for (1+gamma z^q-z^k+beta z^l)f and (-1-gamma z^q-z^k+beta z^l)g, retaining coefficients at the four distinct indices0,q,k,l, gives the two inequalities printed on p.172.
Their averaging uses c_q=d_q and c_s=d_s and therefore remains valid even when q=s.
Using S2 and setting x=-a_l c_q gives, after the source's sign substitutions,

\[
 \frac54c^2+(x+\gamma c)^2+
 \left(\frac{c+x-\gamma c}{2}+\beta c\right)^2
 \le2+\gamma^2+\beta^2                 \tag{E1}
\]

for every real beta,gamma.
Because c<1, maximizing the left-minus-right quadratic in beta yields

\[
 \frac54c^2+(x+\gamma c)^2+
 \frac{(c+x-\gamma c)^2}{4(1-c^2)}
 \le2+\gamma^2.                         \tag{E2}
\]

Let t=c^2, D=4t^2-9t+4 and A=5-8t.
S3 gives D>0 and A>0.
The gamma quadratic in E2 has coefficient -D/(4(1-t)), so maximizing it is legitimate and gives

\[
 \frac54t+
 \frac{A x^2+2c(1-2t)x+t(1-t)}D\le2.
\]

Completing the remaining square is especially transparent in the identity

\[
 A x^2+2c(1-2t)x+t(1-t)
 =A\left(x+\frac{c(1-2t)}A\right)^2+\frac{tD}A.
\]

It follows that (5/4)t+t/(5-8t)<=2, or

\[
 40c^4-93c^2+40\ge0,
\qquad
 40\Lambda^4-93\Lambda^2+40\ge0.         \tag{E3}
\]

At Lambda=theta the divided quartic Lambda^4-(93/40)Lambda^2+1 equals theta^2(theta-53/40), which is negative because theta<1.325.
On the present Lambda range E3 therefore forces

\[
 \Lambda\ge
 \sqrt{\frac{93+\sqrt{2249}}{80}}
 =1.3248755734\ldots>\theta+10^{-4}.
\]

The decimal is explanatory, not the certification.
Exact rational checks give 1324717/10^6<theta<1324718/10^6 and a negative quartic at B=1324818/10^6, which exceeds theta+10^-4.
The quartic is increasing on Lambda>=(1+sqrt(17))/4, so these rational signs certify the strict separation.
This 10^-4 improvement applies to this Taylor-index branch only; it is not a global isolation theorem for every non-extremal nonreciprocal measure.

<a id="smy71-late-coefficient-branch"></a>
## Section5: the branch l>=2k

If l=2k, formal inversion changes its second nonzero coefficient a_(2k) to1-a_(2k), because a_k^2=1.
The value2 is excluded by the preceding coefficient bound; the other value is0.
After this permitted interchange one may take l>2k, without assuming a_k is positive.
In particular,

\[
 c_{2k}-d_{2k}=a_kd_k.                    \tag{T1}
\]

Applying L2 to f and g gives the exact source equation(7):

\[
 -2(1-c^2)+\frac{d_k^2}{1-c}+\frac{c_k^2}{1+c}
 \le a_kd_k\le
 2(1-c^2)-\frac{d_k^2}{1+c}-\frac{c_k^2}{1-c}.
\]

Let a=c^2+c-1, b=1-c^2, u=|c_k| and v=|d_k|.
S4 and L1 give u+v=c, u,v in [a,b], and a_kd_k=-v.
The left inequality above consequently implies

\[
 a\le v\le2b-H(u),\qquad
 H(x)=\frac{x^2}{1+c}+\frac{(c-x)^2}{1-c}.
\]

The dummy-variable interval [a,b] is unchanged by x to c-x, which explains either order of the two denominators in the source's maximum expression.
Since

\[
 \tfrac12H'(x)=\frac{2x-c-c^2}{1-c^2},
\]

and b<(c+c^2)/2 for c>2/3, H is strictly decreasing throughout [a,b].
Its minimum is at b, so

\[
 a\le2b-\frac{b^2}{1+c}-\frac{a^2}{1-c}.
\]

Multiplying the difference of the right and left sides by1-c gives exactly1-c^2-c^3.
Hence

\[
 1-c^2-c^3\ge0,
\qquad \Lambda^3-\Lambda-1\ge0,
\qquad \Lambda\ge\theta.
\]

All denominators are positive by S3, and the cubic is strictly increasing on the Lambda range in use.
This closes the remaining branch and the main theorem without an uninspected analytic coefficient criterion.

<a id="smy71-pv-definitions-and-corollary-one"></a>
## Corollary1 and PV conventions

In the source's convention a PV-number is an algebraic integer alpha with |alpha|>1 and all other conjugates strictly inside the unit circle.
It must be real, because a nonreal alpha would also have its conjugate outside.
The usual positive Pisot convention further requires alpha>1; the source's modulus formulation also permits its negative.
The minimum assertion is theta among positive PV-numbers, or theta as the minimum modulus with the signed convention.

If its polynomial is nonreciprocal, the main theorem gives |alpha|=M(alpha)>=theta.
If it is reciprocal, every inside root must be the inverse of the sole outside root, so its degree is two.
It has polynomial x^2-tx+1 with integer |t|>=3, giving |alpha|>=(3+sqrt(5))/2>theta.
The cubic example above is a positive PV-number of measure theta.
This checks Corollary1, including the reciprocal exception omitted from the word immediate on p.169.

<a id="smy71-equality-analysis"></a>
## Equality analysis needed for Corollary2

The paper states the complex-PV equality cases on p.169 without a separate derivation.
They can be checked directly from equality in its own inequalities, as follows.
Suppose Lambda=theta and choose the orientation with l>2k above.
Then c^2+c^3=1, a=c^4 and b=c^3.
The final necessary inequality is equality, and strict decrease of H forces

\[
 |c_k|=b=c^3,\quad |d_k|=a=c^4,
\quad c_k=\varepsilon c^3,\quad d_k=-\varepsilon c^4,
\quad\varepsilon=a_k\in\{1,-1\}.
\]

Equality in L1 for f forces equality in the retained-coefficient Parseval estimate.
All omitted coefficients of the product then vanish, giving, with T=z^k,

\[
 f(z)=\frac{c+\varepsilon T}{1+\varepsilon cT}.
\]

Equality in T1's lower bound forces the upper L2 bound for g to be attained.
In the L2 proof take rho=delta=1, beta_2=1/c and beta_3=d_k/(c(1-c)).
The retained product coefficients are1, beta_3 and beta_2 and exhaust the Parseval norm, so every other coefficient vanishes.
Using c^5=1-c gives

\[
 g(z)=\frac{c-\varepsilon T/c+T^2}{1-\varepsilon T/c+cT^2},
\qquad
 \frac fg=\frac{1-T^2+\varepsilon T^3}
                 {1-\varepsilon T+\varepsilon T^3}.       \tag{EQ}
\]

The numerator and denominator in EQ are relatively prime, even after T=z^k: a common root would have T=epsilon, where the numerator is1.
Since the original P,Q are also relatively prime, the chosen monic P is epsilon times1-T^2+epsilon T^3 and has degree3k.
The product f has exactly k inside zeros, and g has exactly2k inside zeros, so this orientation of P has k inside and2k outside roots.
For g this also follows from its quadratic numerator: its two T roots form a nonreal pair of product c and modulus sqrt(c)<1.
These calculations justify the equality consequences actually needed next; they do not claim that the paper separately states a general equality-classification theorem.

<a id="smy71-complex-pv-corollary"></a>
## Corollary2: smallest complex PV modulus and its cases

A complex PV-number here is a nonreal algebraic integer alpha whose conjugate pair alpha,conjugate(alpha) has modulus R>1 and whose other conjugates all have modulus less than1.
Thus M(alpha)=R^2.

For nonreciprocal inputs the theorem gives R>=sqrt(theta).
The reciprocal case cannot attain or improve this value.
Reciprocity and the two outside roots force degree four and roots alpha, conjugate(alpha), 1/alpha and1/conjugate(alpha).
For t=alpha+1/alpha, the trace polynomial is x^2+Ax+(B-2) with integers A,B, and t is nonreal.
Its negative integer discriminant gives |Im(t)|>=1/2.
But |Im(t)|<=(R-R^(-1)), so R>=(1+sqrt(17))/4>sqrt(theta).

At R=sqrt(theta) the equality analysis therefore applies.
If its chosen orientation is the original one, there are2k=2 outside roots, hence k=1.
EQ gives the nonreal conjugates of plus or minus theta^(-1).
If the chosen orientation was inverted, the original outside-root count is k=2.
Its polynomial is the reciprocal of the chosen numerator in EQ, with T=z^2.
The epsilon=1 case is x^6-x^2+1 and gives alpha=plus or minus i sqrt(theta).
The epsilon=-1 case is x^6-x^2-1 and has two real outside roots, so it is not a complex PV case.

The stated examples really occur.
The cubic x^3+x^2-1 is the reciprocal of x^3-x-1 up to sign and has exactly the required nonreal pair of modulus sqrt(theta).
For alpha=i sqrt(theta), the field Q(alpha) contains Q(theta), and x^2+theta is irreducible over that real cubic field because -theta is negative at its real embedding.
Thus alpha has degree six with polynomial x^6-x^2+1; its other four roots have modulus theta^(-1/4)<1.
Changing signs preserves the property.
This verifies the minimum and the full list stated in Corollary2.

<a id="smy71-house-corollary-and-degree"></a>
## Corollary3 and the introductory sharpness obstruction

Let R=max_j |alpha_j| be the house.
For nonzero algebraic integers R>=1, and M(P)<=R^n.
If R<1+log(theta)/n, then R^n<theta by (1+x/n)^n<exp(x) for x>0.
The main theorem proves reciprocity, as claimed in Corollary3.
The strict inequalities and full degree n are essential.
This is a reciprocity criterion, not a general degree-independent positive Mahler gap.

The p.169 comparison says its house constant cannot exceed (3/2)log(theta), using alpha_m=theta^(-1/m) of degree3m.
Here is a check of the omitted degree assertion for every m>=1, without a new external irreducibility input.
Put K=Q(theta), a real cubic field.
The element theta is not a q-th power in K for any q>=2: its positive q-th root, if in K, would be an algebraic integer with one outside conjugate and all others inside, of positive value smaller than theta, contradicting the already proved Corollary1.

If x^m-theta had a proper monic factor over K of degree s, 0<s<m, let b in K be the positive absolute value of the product of its roots at the fixed real embedding.
Then b^m=theta^s.
For g=gcd(s,m), choose integers u,v with us+vm=g and put delta=b^u theta^v>0.
One has delta^m=theta^g, hence delta^(m/g)=theta by positivity, contradicting the preceding non-power property.
Thus x^m-theta is irreducible over K and [Q(alpha_m):Q]=3m.

Its house is theta^(1/(2m)), since the two nonreal conjugates of theta have modulus theta^(-1/2).
Its minimal polynomial x^(3m)+x^(2m)-1 is nonreciprocal.
These examples have total Mahler measure theta, so their houses tending to1 do not provide positive Mahler measures tending to1.
Consequently

\[
 3m\bigl(\operatorname{house}(\alpha_m)-1\bigr)
   \longrightarrow\tfrac32\log\theta.
\]

Any proposed replacement constant greater than this limit fails for sufficiently large m.
This checks the source's asymptotic upper obstruction; it does not assert optimality of its proved log(theta) constant.
The historical numerical comparison with Cassels and the priority statements about Siegel and Chamfy were read as attributed history, not as a new audit of those three original articles.

<a id="smy71-assessment-and-use"></a>
## Source assessment and reuse boundary

The complete supplied main proof and all conclusions of the short paper have been checked at the stated scope, including the omitted elementary corollary and degree details above.
No unresolved mathematical input remains in that checked chain beyond the expressly accepted standard analytic and algebraic facts.
The only literal domain issue identified is the displayed lemma's |e_0|=1 endpoint; the separate constant case resolves it and is never needed in Sections3--5.
The original file is not edited.

For use on a nonreciprocal integer polynomial with nonzero constant term, multiplicativity reduces to an irreducible nonreciprocal factor.
Nonunit leading coefficients or content already give M>=2; the remaining monic irreducible factor is covered by the theorem.
Keep the nonzero constant-term condition when using reversal, and retain the stronger unit reduction in any reuse of the f/g proof.
The theorem is now supported by a full primary-source inspection rather than only the author's later survey statement.
This does not retroactively enlarge any older review's scope, select a new project Claim assessment or resolve the reciprocal Lehmer problem.
