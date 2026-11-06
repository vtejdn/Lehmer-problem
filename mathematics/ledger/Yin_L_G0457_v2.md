---
author: Yin
---

# Cyclotomic central perturbations: the minus-one branch and bounded-prime-count obstruction

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The external_structural_lead delegate developed the trace reduction, complete finite cyclotomic extraction and numerical probe.
The coordinating main agent proposed the minus-one branch and the bounded-prime-count sparse completion; the delegate checked the completion and its accepted-source interface.
These are author-development contributions and ordinary checks, without independent review, a new Claim assessment or a counterexample to the Task.

<a id="cyclotomic-central-minus-one-scope"></a>
## Variant, reuse and result

Let n be odd and squarefree with at least two distinct prime factors, and write
\[
 D=\varphi(n)=2d,\qquad Q_n(z)=\Phi_n(z)-z^d.
 \tag{1}
\]
The integer d is even.
This changes the central subtraction from two in [L457 v1](Yin_L_G0457_v1.md#cyclotomic-central-minus-two-scope) to one.
The original minus-two conclusions remain at that fixed version, and neither its no-cyclotomic-factor proof nor its dyadic lower bound is transferred to (1).
Here Q_n(1)=Q_n(-1)=0, so all zero-measure factors must be removed before counting the degrees of positive-measure factors.

[C414's central-shift criterion](../claims/Yin_C_G0414_v1.md#real-trace-shift-criterion) already owns the general trace-perturbation mechanism and the obligation to retain nonreal roots.
The local reuse search found that general mechanism and the minus-two specialization, but no prior analysis of this exact minus-one cyclotomic family.
This is a specified application and failure diagnosis, not a newly claimed perturbation method or a complete classification of central shifts.
The only finite inputs below are n=35,105,1155.
They have positive total logarithmic measure, with no exterior real roots at all.
Their numerical totals do not approach zero in these three observations, but finite data make no asymptotic exclusion.
The proved sparse completion excludes positive-to-zero sequences with bounded numbers of distinct prime factors; it leaves the unbounded-prime-count range unresolved.

<a id="central-minus-one-trace-reduction"></a>
## Exact trace quotient and absence of exterior real roots

The [integer trace construction and endpoint derivatives](Yin_L_G0457_v1.md#actual-trace-and-endpoint-roots) give a monic polynomial Psi_n in Z[y] with
\[
 \Phi_n(z)=z^d\Psi_n(z+z^{-1}),\qquad
 \Psi_n(y)=\prod_{i=1}^{d}(y-\beta_i),\qquad -2<\beta_i<2,
 \tag{2}
\]
where the beta_i are the distinct inverse-pair traces of primitive nth roots.
The same fixed derivation gives
\[
 \Psi_n(2)=\Psi_n(-2)=1,\qquad
 \Psi_n'(2)=\frac{J_2(n)}{24}>0,\qquad
 \Psi_n'(-2)=-\frac{J_2(n)}8<0,
 \quad J_2(n)=n^2\prod_{p\mid n}(1-p^{-2}).
 \tag{3}
\]
The derivative computation is retained in [L457 v1](Yin_L_G0457_v1.md#jordan-endpoint-bound); its inputs (2) are unchanged.

Since both endpoints are simple roots of Psi_n(y)-1, monic integer division gives
\[
 R_n(y)=\frac{\Psi_n(y)-1}{y^2-4}\in\mathbb Z[y],\qquad
 \deg R_n=d-2,
 \tag{4}
\]
with
\[
 R_n(2)=\frac{J_2(n)}{96}>0,\qquad
 R_n(-2)=\frac{J_2(n)}{32}>0.
\]
Substitution and (z+z^{-1})^2-4=(z^2-1)^2/z^2 yield the exact polynomial identity
\[
 Q_n(z)=(z^2-1)^2 z^{d-2}R_n(z+z^{-1}).
 \tag{5}
\]
Thus the multiplicity of each of z=1 and z=-1 is exactly two.
The remaining expression z^{d-2}R_n(z+z^{-1}) is an integer polynomial, by its degree and the displayed identity.

For y>2 all factors y-beta_i are positive and increase strictly, so Psi_n(y)>Psi_n(2)=1.
For y<-2 the even number d of factors gives the positive product of beta_i-y; each exceeds its value at y=-2, so Psi_n(y)>Psi_n(-2)=1.
Consequently Psi_n(y)=1 has no real solution outside [-2,2].
For every nonzero real z other than 1 or -1, the trace z+z^{-1} lies outside that interval.
Since Q_n has constant coefficient one, zero is not a root either.
Therefore the only real roots of Q_n are the double roots at 1 and -1.
In particular its entire logarithmic Mahler measure is
\[
 m(Q_n)=\sum_{\substack{Q_n(\alpha)=0,\ |\alpha|>1\\\alpha\notin\mathbb R}}
                \log|\alpha|,
 \tag{6}
\]
with all multiplicities retained.
This identity allows zero measure and does not assert positivity for every n.
Whenever Q_n has positive measure, it cannot be a Salem polynomial times cyclotomic factors, because it has no exterior real root.
Such inputs remain legitimate for the unrestricted Task, which is not restricted to Salem numbers.

<a id="central-minus-one-exhaustive-cyclotomic-test"></a>
## Exhaustive finite cyclotomic extraction

The [native center_one.py program](../computations/programs/Yin_J_G0138/center_one.py) exhausts all possible cyclotomic divisors of each specified Q_n.
The following finite order bound and rejection argument justify that completeness; a finite cutoff chosen from numerical root proximity is not used.

If Phi_k divides a degree-D polynomial, then phi(k)<=D.
For every positive integer k, multiplicativity gives
\[
 \frac{\varphi(k)^2}{k}
   =\prod_{p^a\parallel k}p^{a-2}(p-1)^2\ge\frac12.
 \tag{7}
\]
For an odd prime and a=1, the factor is (p-1)^2/p>=1, and increasing a multiplies it by p.
For p=2, the factor is 1/2 when a=1 and at least one when a>=2.
There is at most one factor of this exceptional type.
For k=1 the empty product is one.
This proves (7) and hence
\[
 \varphi(k)\ge\sqrt{k/2},\qquad
 \varphi(k)\le D\Longrightarrow k\le2D^2.
 \tag{8}
\]
An exact integer totient sieve on 1<=k<=2D^2 therefore lists every possible order with phi(k)<=D.

For each listed order the program generates Phi_k exactly over Z and first divides its reduction into the reduction of the original Q_n over F_2.
Failure of this modular divisibility implies failure of integer divisibility: any integer factorization would reduce to the modular one, while monicity keeps Phi_k nonzero and of unchanged degree modulo two.
Thus this filter rejects no genuine cyclotomic divisor.
A modular pass is only a necessary condition; the program then performs exact integer polynomial division on the current residual and repeats it until division fails, recording its actual multiplicity.
Distinct cyclotomic polynomials are coprime over Q, so removing an earlier one does not remove or create divisibility by any different later order.
The modular screen uses the original input throughout, so every factor of the residual that could occur also passed the necessary test on that original input.
The final residual has no cyclotomic factor, and the product of the extracted block and residual is checked against the original polynomial exactly.
This supplies a complete classification only for the three finite inputs, not for all n in (1).

Put
\[
 C(z)=\Phi_1(z)^2\Phi_2(z)^2\Phi_3(z)\Phi_4(z)\Phi_6(z)\Phi_8(z),
 \qquad \deg C=14.
 \tag{9}
\]
The completed exact outputs are as follows.

| n | Degree of Q_n | Entire cyclotomic block | Remaining degree | Positive irreducible factors, with multiplicity |
| --- | --- | --- | --- | --- |
| 35 | 24 | C | 10 | Exactly one |
| 105 | 48 | C | 34 | Exactly one |
| 1155 | 480 | C Phi_5 Phi_10 Phi_12 Phi_24 | 446 | At least one; exact count not determined |

The last cyclotomic block has degree 34.
At n=35 the remaining irreducible polynomial is exactly z^10-z^9+z^5-z+1.
At n=105 exact rational factorization of the degree-34 residual returns one irreducible factor; its complete integer coefficients are reproduced by J138.
No complete rational factorization of the degree-446 residual was attempted in this retained program.
For that input the sieve uses the bound 460800 and leaves 954 possible orders with phi(k)<=480, the largest being 2310.
The only orders passing its modular screen are 1,2,3,4,5,6,8,10,12,16,20,24,32,48; exact integer division retains precisely the factors displayed above.

Each residual is monic with constant coefficient one, is nonconstant, and has no cyclotomic factor.
Every one of its irreducible factors is therefore an algebraic-unit polynomial of positive measure by the accepted [Kronecker normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
Their degrees with multiplicity sum to 10,34,446 respectively.
The n=1155 conclusion concerns all its positive-measure irreducible factors together and does not say there is just one such factor.
This is the necessary degree accounting for this branch; the original degree 480 includes 34 degrees of zero measure.

<a id="central-minus-one-finite-measure"></a>
## Complete numerical measure and its limits

The [J138 reproduction account](../computations/programs/Yin_J_G0138/readme.md) retains exact input generation, exact residual coefficients, exhaustive extraction parameters and the completed finite output.
Because the removed cyclotomic block has measure zero, the residual has exactly the same total logarithmic Mahler measure as Q_n.
The program evaluates that residual on shifted boundary grids with 2^17, 2^19 and 2^21 points; at degrees 10 and 34 it also performs a floating-point root screen.
The finest-grid estimates are approximately 0.24965569, 0.41441535 and 0.74500526 for n=35,105,1155 respectively.
The first two numerical root sums are approximately 0.2496548880 and 0.4144129341, with two and eight exterior roots in the corresponding numerical screens.
There is no certified error interval or certified numerical root count, and no root screen was run for the degree-446 residual.
The exact identity (6), rather than a numerical real-root test, establishes that all these measures come from nonreal exterior roots.
Positivity of the three total measures follows from exact noncyclotomic extraction and Kronecker, not from these decimal approximations.
No rate, monotonicity or positive-to-zero sequence is inferred from three inputs.

<a id="bounded-prime-count-completion"></a>
## Bounded prime count is already excluded by sparse completion

Let n>1 be squarefree with r distinct prime factors.
Let H be an integer polynomial with at most h nonzero coefficients, c an integer and k a nonnegative integer, and suppose
\[
 F(z)=H(z)\Phi_n(z)-cz^k
\]
is nonzero.
The Mobius formula gives
\[
 A_n(z)=\prod_{\substack{e\mid n\\\mu(n/e)=1}}(z^e-1),\qquad
 B_n(z)=\prod_{\substack{e\mid n\\\mu(n/e)=-1}}(z^e-1),\qquad
 \Phi_n=A_n/B_n.
 \tag{10}
\]
Squarefreeness implies there are exactly 2^(r-1) divisors of each sign: toggling any fixed prime pairs subsets of opposite parity.
Each product therefore has at most 2^(2^(r-1)) nonzero monomials, since expansion chooses one of two terms from each binomial and cancellation can only reduce support.
Multiplication by H increases that bound by at most the factor h.
Consequently the nonzero integer polynomial
\[
 B_nF=HA_n-cz^kB_n
\]
has at most
\[
 K=(h+1)\,2^{\,2^{r-1}}
 \tag{11}
\]
nonzero coefficients.
Every binomial z^e-1 has measure zero, so additivity of logarithmic Mahler measure gives m(B_nF)=m(F).
The accepted [DS17 fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001), specifically its univariate total-measure consequence, now gives
\[
 m(F)=0\quad\text{or}\quad m(F)\ge\eta_K>0.
 \tag{12}
\]
For r and h bounded by fixed constants, one may take the single corresponding upper bound for K in that same theorem; no monotonicity of independently chosen eta_K values is assumed.
The degrees, exponents, coefficient heights and c need not be bounded.

For H=1, (12) covers both central shifts one and two, with any choice of the central exponent allowed by the actual polynomial.
For H=(z-1)^2 it also covers the endpoint variant (z-1)^2 Phi_n-z^(phi(n)/2+1), since h=3.
This is an application of an already accepted sparse-gap statement, retaining DS17's actual source-proof inspection limits and without an explicit value of eta_K.
It is not a new sparse-gap theorem or a new uniform bound over r.
In particular, support growth of Phi_n alone does not escape this filter when r is bounded: multiplication by the zero-measure B_n supplies the bounded-support completion.
Any positive-to-zero sequence in the stated central-shift families must have unbounded numbers of distinct prime factors.
The family with growing r remains unresolved, and neither the exact finite extraction nor the numerical measures above supplies a mechanism controlling its full nonreal exterior cost.
