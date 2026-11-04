---
author: Yin
---

<a id="voi98-u001"></a>
# Voi98-U001: Relative Free Entropy and Its Integral Proofs

This current unit retains Section 7 and its original inspection facts only.
The finite-tracial, Fisher-information, regularization, semicontinuity and external-input arguments described under former U001/U006/U007/U009 are not located in the current collection at those scopes.
The references below preserve their historically selected interfaces and actual limits; they are not new proof inspections or complete presently inspectable upstream arguments.
Reusing a conclusion that needs one of those interfaces requires locating or adequately preparing that exact input, rather than using this current U001 as its substitute.

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), Section 7, Definition 7.1 and Propositions 7.2-7.9, printed pp. 222-226 / PDF pp. 34-38.
- Record: 2026-09-08, the coordinating agent, for [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit).
- Kind and depth: reconstructed local entropy proofs and normalization corrections.
  Proposition 7.6's reduction is reviewed, while the earlier scalar heat-energy theorem retains the specific original-source limitation stated below; it is not labelled a complete independent proof of that external analytic theorem.

## Definition and existence of the integral

Use a finite von Neumann algebra with faithful normal tracial state, a finite selfadjoint tuple $X=(X_1,\ldots,X_n)$ and a unital star-subalgebra $B$, at the stated source conventions.
Let $S=(S_1,\ldots,S_n)$ be a free variance-one semicircular family free from $B[X]$, and define

$$f_X(t)=\Phi^*(X+\sqrt tS:B),\quad C^2=\sum_j\tau(X_j^2),\quad c=C^2/n.$$

The historical audit attributed the following $t>0$ Fisher/regularization interface to former U006--U007, whose detailed bodies are not located in the current collection:

$$\frac{n}{t+c}\leq f_X(t)\leq\frac nt,$$

and $f_X$ is nonincreasing and right continuous, including extended value $+\infty$ at zero.
The entropy definition is

$$\chi^*(X:B)=\frac12\int_0^\infty\left(\frac{n}{1+t}-f_X(t)\right)dt+\frac n2\log(2\pi e).\tag{1}$$

The integrand is measurable.
On $[1,\infty)$ it is between $n/(1+t)-n/t$ and $n/(1+t)-n/(t+c)$, both $O(t^{-2})$, so its tail is absolutely integrable.
Near zero its positive part is bounded by $n$, whereas its negative part may have infinite integral.
Thus (1) is well defined in $[-\infty,\infty)$, never an undefined difference of two infinite positive integrals.

If $C^2=0$, faithfulness gives $X_j=0$ for every $j$; then $f_X(t)=n/t$ and $\chi^*(X:B)=-\infty$.
This case is evaluated directly rather than using $0\cdot\infty$ in the Cramer-Rao inequality.

## Propositions 7.2 and 7.3: upper bound and algebra operations

For $c>0$, integrate the lower Fisher bound:

$$\chi^*(X:B)\leq\frac n2\left[\log(2\pi e)+\int_0^\infty\left(\frac1{1+t}-\frac1{c+t}\right)dt\right]=\frac n2\log(2\pi e c).\tag{2}$$

The source's intermediate integral on p. 223 has upper endpoint $1$; it must be $\infty$ to yield the displayed logarithm.
The $c=0$ case agrees with (2) in the extended sense, by the direct calculation above.

For tuples of respective lengths $n,m$, the correct 7.3 assertions are

$$\chi^*(X,Y:B\vee C)\leq\chi^*(X:B)+\chi^*(Y:C),$$

with equality if $B[X]$ and $C[Y]$ are free; $B_1\subseteq B_2$ gives $\chi^*(X:B_1)\geq\chi^*(X:B_2)$; freely adjoining $C$ to $B[X]$ leaves $\chi^*$ unchanged; and replacing $B$ by $W^*(B)$ leaves it unchanged.

Choose all added semicircular variables freely in one extension.
For free additivity the enlarged blocks remain free; apply the corresponding historical Fisher identities to each $t>0$; their former U006 proof home remains unlocated.
The regularizing terms split because $(n+m)/(1+t)=n/(1+t)+m/(1+t)$.
Integrate on truncated intervals and pass to the improper limits; finite upper bounds and integrable positive parts prevent $+\infty-\infty$.
The source's 7.3(a) writes $Y_n$ in the left tuple although the right tuple ends at $Y_m$; use the same $m$ throughout.

## Proposition 7.4: upper semicontinuity and the missing integrable bound

Suppose $X_j^{(k)}\to X_j$ strongly in a common $M$, with all variables selfadjoint.
Uniform boundedness gives a common finite $C_0^2\geq\sum_j\tau((X_j^{(k)})^2)$ and $\sum_j\tau(X_j^2)$; enlarge it to be strictly positive.
The normal trace then gives $L^2$ convergence.
The same bounded sequences converge strongly in the tracial free-product extension: check on its dense bounded vectors using the $L^2$ norm and then use uniform boundedness.
The historically selected regularization interface applies there for every fixed $t>0$; its former U007 proof account remains unlocated.

Put $c_0=C_0^2/n$ and $g_k(t)=n/(1+t)-f_{X^{(k)}}(t)$.
The required common upper bound is

$$g_k(t)\leq G(t):=\frac{n}{1+t}-\frac{n}{t+c_0},\qquad G\in L^1(0,\infty).\tag{3}$$

Fisher lower semicontinuity gives $\limsup_k g_k(t)\leq g_X(t)$.
Apply Fatou to the nonnegative $G-g_k$ to obtain $\limsup_k\int g_k\leq\int g_X$, including value $-\infty$.
Consequently $\limsup_k\chi^*(X^{(k)}:B)\leq\chi^*(X:B)$.

On p. 224 the source drops the second numerator $n$ in (3), yielding $n/(1+t)-1/(t+c_0)$.
For $n>1$ this behaves as $(n-1)/t$ and is not integrable.
Restoring $n$ repairs this actual failed estimate.
The proof also has a limit index $n\to\infty$ where $k\to\infty$ is intended and omits conditioning $B$ in that displayed limit; both are retained in the corrected argument.

## Proposition 7.5: the heat trajectory and the zero endpoint

Let $h(t)=\chi^*(X+\sqrt tS:B)$.
Independent semicircular increments identify its Fisher trajectory with $f_X(t+s)$.
For $0<u<v$, integrate (1) with a finite common upper cutoff, shift variables, and use $f_X(s)\leq n/s$ to make the residual tail integral tend to zero.
This gives

$$h(v)-h(u)=\frac12\int_u^v f_X(s)\,ds.\tag{4}$$

The same identity holds for $u=0$ with extended values: truncated integrals at zero converge by the one-sided integrability established above.
If $h(0)=-\infty$, the right side is $+\infty$, while $h(v)$ is finite for $v>0$.
No subtraction of two values $-\infty$ is used.

For $t>0$, the upper Fisher bound in (1) yields $h(t)\geq(n/2)\log(2\pi e t)$; (2) supplies a finite upper bound.
Equation (4) and the monotonicity of $f_X$ show that $h$ is nondecreasing and concave.
It is continuous on $(0,\infty)$, and at zero in the extended-real sense, since either $\int_0^v f_X$ is finite and its small-interval integral tends to zero, or it diverges and $h(u)\downarrow-\infty$ as $u\downarrow0$.

Right continuity of $f_X$ gives the right derivative

$$h'_+(t)=\tfrac12 f_X(t).\tag{5}$$

When $h(0)$ is finite but $f_X(0)=\infty$, the right derivative is infinite by (4).
If $h(0)=-\infty$, $f_X(0)=\infty$ as well: a finite initial value would bound $f_X$ near zero and make (1) finite.
Thus the source's endpoint derivative can be interpreted in the extended sense; an ordinary finite derivative at every $t\geq0$ is not asserted.

## Proposition 7.6: scalar comparison and its exact proof boundary

For $n=1$ and $B=\mathbb C$, the source concludes $\chi^*(X:\mathbb C)=\chi(X)$.
It invokes the earlier logarithmic-energy heat identity, explicitly correcting constants from Part I, Lemma 3.2:

$$\chi(X+\sqrt tS)-\chi(X)=\frac12\int_0^t\Phi^*(X+\sqrt sS:\mathbb C)\,ds.\tag{6}$$

Given (6), scalar entropy scaling and free-convolution monotonicity, the remaining comparison is as follows.
Set $C_X^2=\tau(X^2)$.
The normalization at large time follows from

$$\chi(S)\leq\chi(t^{-1/2}X+S)\leq\tfrac12\log(2\pi e(1+C_X^2/t)).\tag{7}$$

Thus $\chi(t^{-1/2}X+S)\to\chi(S)=\tfrac12\log(2\pi e)$.
Subtract $\tfrac12\log(1+t)$ from (6), use $\chi(X+\sqrt tS)=\tfrac12\log t+\chi(t^{-1/2}X+S)$, and let $t\to\infty$.
The result is precisely (1).
If the integral diverges at zero, (6) gives $\chi(X)=-\infty$, agreeing with $\chi^*$.

The source's p. 225 bound writes $1+t^{-1}$ in place of $1+C_X^2/t$ without normalizing $X$.
The latter is sufficient and valid for arbitrary bounded selfadjoint $X$.
Its factor $1/2$ in (6) is an explicit correction by the author, distinct from our newly identified printed errors.

The scalar microstates formula and upper bound were primary-statement-checked in the author's later survey, identified by the historical external-interface account as a primary-statement reading.
That former U009 account is not located, so the exact selected survey passage and its existing acceptance limit need to be recovered before this source interface is reused.
Direct access to the earlier Part I/II proof passages was not obtained in the bounded search.
In particular, the complete regularity/limit justification behind (6) and the original free-convolution monotonicity proof were not independently audited.
This unit checks the stated reduction, constants, tail limit and extended endpoints **conditional on those earlier analytic inputs**.
The scalar equality also has a later author restatement, but that restatement does not constitute an independent review of the missing original proof.
No multivariable or relative microstates equality follows from 7.6.

## Propositions 7.7 and 7.8: orthogonal maps and corrected scaling

An orthogonal real matrix preserves the joint distribution of a standard semicircular family.
The historically selected information-covariance interface, whose former U006 proof home remains unlocated, therefore makes the integrands in (1) equal and proves $\chi^*(AX:B)=\chi^*(X:B)$, including infinite negative entropy.

For real $a\ne0$, the correct scaling formula is

$$\boxed{\chi^*(aX_1,\ldots,aX_n:B)=\chi^*(X_1,\ldots,X_n:B)+n\log|a|.}\tag{8}$$

The source's Proposition 7.8 itself omits $n$ and is false as printed for $n>1$.
For example, a free variance-one semicircular pair has entropy $\log(2\pi e)$, whereas the pair scaled by $a$ has entropy $\log(2\pi e)+2\log|a|$, directly by (1) with information $2/(a^2+t)$.

To prove (8), use information scaling and the invariance under sign change of the semicircular family to get $f_{aX}(t)=a^{-2}f_X(t/a^2)$.
Substitute $r=t/a^2$ on truncated intervals in (1).
The difference from the original entropy integrand is the absolutely integrable function

$$\frac n2\left(\frac1{a^{-2}+r}-\frac1{1+r}\right).$$

Its integral over $(0,\infty)$ is $n\log|a|$.
This also proves (8) when the original entropy is $-\infty$, since adding an integrable function does not change that value.
The source's displayed proof also has erroneous cutoffs, duplicated factors, a missing square root in one semicircular perturbation, and a lost $X_1$; the substitution above replaces that calculation completely.

## Proposition 7.9: finite information implies finite entropy

If $\alpha=\Phi^*(X:B)<\infty$, the historically selected Cramer--Rao interface, whose former U006 argument remains unlocated, ensures $\alpha>0$, and Stam gives

$$f_X(t)\leq(\alpha^{-1}+t/n)^{-1}=\frac{n}{n/\alpha+t}.$$

Integrating this bound in (1) gives

$$\chi^*(X:B)\geq\frac n2\log\left(\frac{2\pi e n}{\alpha}\right)>-\infty.$$

The source's last integral prints $1+t^{-1}$ where $(1+t)^{-1}$ is needed.
The former diverges at both endpoints in that expression; using the latter gives the stated logarithm.
This proof uses only Stam and the defining integral, so it is independent of the limited scalar comparison in 7.6.

## Review facts and downstream effects

The coordinating agent read all Section 7 passages and visually inspected PDF pp. 35-38.
The integral existence, zero-energy case, repaired upper/Fatou bounds, heat-increment cutoffs, extended endpoints, dimension-dependent scaling and finite-information estimate were reconstructed.
These universal calculations require no numerical quadrature or finite tests.
On 2026-09-08, both the external-input agent and the derivation agent independently read the full unit and the relevant rendered source pages, recomputed these integral arguments and found no local gap within the stated input limits.
In particular neither review upgrades the conditional analytic-input boundary of 7.6.
The historical audit separated accepted and inaccessible external inputs in former U009.
That detailed external-interface body is not located in the current collection; no present external-proof coverage is inferred from the obsolete unit number.

The corrections preserve 7.2-7.5, 7.7 and 7.9's stated conclusions and replace 7.8 with the correct dimension-dependent assertion.
Proposition 7.6 retains its stated scalar scope and the analytic proof boundary above.
None of these observations independently establishes general $\chi=\chi^*$ or upgrades an unrelated source audit.

## Source and inspection

Source edition: Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body.

Passages: Section 7, Definition 7.1 and Propositions 7.2-7.9, printed pp. 222-226 / PDF pp. 34-38.

Inspection: 2026-09-08: integral existence, algebra operations, upper semicontinuity, heat trajectory, orthogonal invariance, corrected scaling and the finite-information bound reconstructed and independently reviewed. Proposition 7.6 remains a scalar reduction conditional on the specified earlier heat-energy and free-convolution analytic inputs; their original proofs were not obtained or independently audited. No general microstates/nonmicrostates equality follows.
