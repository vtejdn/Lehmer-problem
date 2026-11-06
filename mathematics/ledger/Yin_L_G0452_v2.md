---
author: Yin
---

# Finite cyclotomic logarithmic auxiliaries: a positive-kernel bound without a common period

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent posed the mixed-order test and supplied the total-weight deduction below.
The responsible delegate developed the positive-weight adaptation of the existing finite Fejer argument, combined it with L452 v1's Fourier constraint, and checked the finite constants, integer cutoff, total-weight deduction and arithmetic return.
These are ordinary author calculations, not independent review, a new Claim assessment or Task completion.

<a id="mixed-order-positive-kernel-scope"></a>
## Question and relation to v1

[L452 v1](Yin_L_G0452_v1.md#mean-times-radial-slope-bound) proves \(cK\ge D^2/(4\ell)\) for a finite nonnegative cyclotomic logarithmic auxiliary, with \(\ell\) the least common multiple of its orders.
That bound may weaken when the orders vary together and \(\ell\) is much larger than the original degree.
A complete-period Ramanujan orthogonality identity alone does not control the short prefix needed in that joint limit.

The finite positive-kernel identity already retained in [C168](../claims/Yin_C_G0168_v1.md#phase-alias-fejer-lower-bound) supplies the needed comparison without waiting for a complete period.
C168 proves its finite Fourier expansion and keeps only nonnegative diagonal contributions for unweighted labelled circle points.
The present calculation applies precisely that method to positive weights on all primitive roots, and then combines it with v1's particular coefficient constraint and radial budget.
No new Fejer principle or external theorem is asserted.
The actual C168 subsection was read at this finite identity and positivity scope; its separate Salem and Sobolev results are not inputs.

This version preserves v1's disk extension, original-root return, single-order estimates and Abel controls at their original addresses.
It adds a period-free mixed-order bound and a weaker but fully normalized consequence using only the total logarithmic weight.
Every conclusion still concerns v1's stated absolute-coefficient radial envelope, not a lower bound on the actual original-root sum.

<a id="mixed-order-weights-and-budget"></a>
## Exact finite data and reused interfaces

Combine all equal cyclotomic orders by adding their positive weights, and omit all zero weights.
Let \(\mathcal Q\) be the resulting finite nonempty set of distinct positive integers, with \(b_q>0\) for \(q\in\mathcal Q\).
For a finite polynomial
\[
 A(z)=\sum_{n=1}^N a_nz^n,\qquad a_n\in\mathbb C,\qquad N\ge0,
\]
assume
\[
 H(z)=\Re A(z)-c+\sum_{q\in\mathcal Q}b_q\log|\Phi_q(z)|
                                  \le0\qquad(|z|=1).
\tag{1}
\]
The normalization is \(A(0)=0\); positive-weight circle zeros have value \(-\infty\).
All coefficients, orders, weights and \(N\) may depend on the original input.

Define
\[
 \begin{aligned}
 W&=\sum_qb_q,&
 D&=\sum_qb_q\varphi(q),&
 S&=\sum_qb_q^2\varphi(q),&
 v&=S/D,\\
 B_n&=\sum_qb_qc_q(n),&
 R(t)&=Dt+2\sum_{n=1}^N|a_n|\sinh(nt),&
 K&=R'(0)=D+2\sum_{n=1}^Nn|a_n|.
 \end{aligned}
\tag{2}
\]
Here \(c_q(n)\) is the complete real Ramanujan sum.
The symbol \(v\) in this version is an effective logarithmic weight, not a finite place or a rational denominator.
The factor list is nonempty, so \(W,D,S,v\) are positive.

[V1's zero-mean argument](Yin_L_G0452_v1.md#zero-mean-and-disk-extension) gives \(c>0\).
Its finite real-weight disk extension remains valid for the complex coefficients in (1).
Its [Fourier constraint](Yin_L_G0452_v1.md#finite-log-fourier-constraint), with \(a_n=0\) for \(n>N\), is
\[
                           |a_n-B_n/n|\le2c\qquad(n\ge1).
\tag{3}
\]
These interfaces keep their exact finite hypotheses and do not require integer weights.
The maximum modulus and circle-logarithm source scopes remain exactly those recorded in v1.

Put weight \(w_\zeta=b_q\) at each primitive \(q\)-th root \(\zeta\), for every \(q\in\mathcal Q\).
The supports for distinct orders are disjoint, so
\[
          B_n=\sum_\zeta w_\zeta\zeta^n,\qquad
          \sum_\zeta w_\zeta=D,\qquad
          \sum_\zeta w_\zeta^2=S.
\tag{4}
\]
Thus
\[
                      |B_n|\le D,\qquad S\le D^2,\qquad
                      0<v\le D\le K,\qquad D\ge W.
\tag{5}
\]
The root weights in (4) are auxiliary weights, not a selection or reweighting of the original conjugates in the Mahler return.

For comparison, if \(\ell=\operatorname{lcm}_{q\in\mathcal Q}q\), finite character orthogonality gives the complete-period identity
\[
                         \frac1\ell\sum_{n=0}^{\ell-1}|B_n|^2=S.
\tag{6}
\]
Indeed the average of \((\zeta\bar\xi)^n\) is one when \(\zeta=\xi\) and zero otherwise.
This identity identifies the quadratic weight but is not used to approximate any shorter sum.

<a id="weighted-finite-fejer-bound"></a>
## A finite positive-kernel bound at every integer length

For every integer \(L\ge1\), use the finite kernel
\[
 F_{L-1}(z)=\frac{|1+z+\cdots+z^{L-1}|^2}{L}
          =\sum_{|n|<L}\left(1-\frac{|n|}{L}\right)z^n
          \qquad(|z|=1).
\tag{7}
\]
Its expansion follows by counting pairs of indices with each difference.
It is nonnegative everywhere and \(F_{L-1}(1)=L\).
Summing over the positive weights in (4) gives
\[
 \begin{aligned}
 D^2+2\sum_{n=1}^{L-1}\left(1-\frac nL\right)|B_n|^2
 &=\sum_{\zeta,\xi}w_\zeta w_\xi F_{L-1}(\zeta\bar\xi)\\
 &\ge L\sum_\zeta w_\zeta^2=LS.
 \end{aligned}
\tag{8}
\]
The inequality retains the diagonal terms and drops only nonnegative cross terms.
This is the exact positive-weight adaptation of C168's finite argument.
No root separation, uniform distribution, relation between \(L\) and \(\ell\), or limiting interchange is needed.

Equation (3) gives
\[
                      |B_n|\le n|a_n|+2cn.
\]
Multiplying by \(|B_n|\le D\), obtain the complete finite estimate
\[
                     |B_n|^2\le Dn|a_n|+2cDn.
\tag{9}
\]
It remains valid when \(n>N\), because the coefficient in (3) is then zero.
Use (9) in the upper bound for the left side of (8).
The coefficient contribution is at most
\[
 2D\sum_{n=1}^{L-1}\left(1-\frac nL\right)n|a_n|
       \le2D\sum_{n=1}^Nn|a_n|=D(K-D),
\]
while the elementary sum is
\[
                 \sum_{n=1}^{L-1}\left(1-\frac nL\right)n
                                =\frac{L^2-1}{6}.
\]
Consequently the initial \(D^2\) cancels against the \(-D^2\) in \(D(K-D)\), leaving
\[
          \boxed{LS\le DK+\frac23cD(L^2-1)\qquad(L\in\mathbb Z,\ L\ge1).}
\tag{10}
\]
Equivalently,
\[
                       K\ge Lv-\frac23c(L^2-1).
\tag{11}
\]
The case \(L=1\) is included.
The argument permits \(L>N\) and \(L\ll\ell\), and all quantities are at their actual finite values.

<a id="integer-cutoff-period-free-tradeoff"></a>
## The integer cutoff and its uniform consequence

The real quadratic on the right of (11) is maximized at
\[
                                x=\frac{3v}{4c}.
\]
If \(x\le1\), then \(c\ge3v/4\), and (5) gives
\[
                             cK\ge cv\ge3v^2/4.
\]
If \(x>1\), choose a nearest integer \(L\ge1\), so \(|L-x|\le1/2\).
Completing the square in (11) gives
\[
 \begin{aligned}
 K&\ge \frac{3v^2}{8c}+\frac23c-\frac23c(L-x)^2\\
  &\ge \frac{3v^2}{8c}+\frac12c.
 \end{aligned}
\tag{12}
\]
The constant term \(2c/3\) pays the entire integer-rounding loss, at most \(c/6\).
Both cases prove
\[
                              \boxed{cK\ge\frac38(S/D)^2.}
\tag{13}
\]
This is a finite-parameter consequence of (10), not a fixed-period asymptotic.

Since
\[
                    v=\sum_q\frac{b_q\varphi(q)}{D}\,b_q
\]
is a weighted average of the positive \(b_q\), any lower bound \(b_q\ge b_0>0\) gives
\[
                              cK\ge3b_0^2/8.
\tag{14}
\]
This applies to arbitrary finite mixtures, arbitrary orders and arbitrarily large least common multiple.
In particular it applies with \(b_0=1\) for positive integer weights, or \(b_0=1/M\) for positive rational weights with a fixed common denominator \(M\).
For the single \(\Phi_6\) term of weight \(1/2\), it gives \(cK\ge3/32\).
V1's different order-sensitive estimate may still be stronger for other parameters, and is not deleted.

For an original polynomial of degree \(d\ge1\), if \(c\le B/d\) for a fixed \(B>0\) and \(v\ge v_0>0\), (13) gives
\[
                              K\ge\frac{3v_0^2d}{8B}.
\tag{15}
\]
Thus the former least-common-multiple loss is not essential in this normalized class, even when \(\ell\gg d\).
As in v1, \(R(t)\ge Kt\), so this particular envelope cannot have a uniform upper comparison \(R(t)\le Ct\) in that regime.

<a id="total-logarithmic-weight-consequence"></a>
## A total-weight consequence allowing arbitrarily small individual weights

The coordinating agent supplied the following additional deduction, which was checked with its actual constants.
It avoids a lower bound on each \(b_q\) by keeping the total weight \(W\) in the conclusion.

V1's prime-power calculation gives \(\varphi(q)^2/q\ge1/2\), hence
\[
                                  \varphi(q)\ge\sqrt{q/2}.
\tag{16}
\]
Set the real cutoff
\[
                                  Q=8(D/W)^2\ge8.
\]
If \(q>Q\), then \(\varphi(q)>2D/W\).
Since \(\sum_qb_q\varphi(q)=D\), the total weight at those orders is at most \(W/2\), and therefore
\[
                              \sum_{\substack{q\in\mathcal Q\\q\le Q}}b_q
                                         \ge W/2.
\tag{17}
\]
Also
\[
 \begin{aligned}
 \sum_{\substack{q\in\mathcal Q\\q\le Q}}\frac1{\varphi(q)}
 &\le\sqrt2\sum_{q=1}^{\lfloor Q\rfloor}q^{-1/2}\\
 &\le2\sqrt{2Q}=\frac{8D}{W}.
 \end{aligned}
\tag{18}
\]
The finite sum estimate follows from
\(1+\int_1^M x^{-1/2}\,dx=2\sqrt M-1\le2\sqrt M\) for \(M=\lfloor Q\rfloor\ge1\).
Finite Cauchy--Schwarz on the low-order set in (17) now gives
\[
 \frac{W^2}{4}
 \le\left(\sum_{q\le Q}b_q^2\varphi(q)\right)
      \left(\sum_{q\le Q}\frac1{\varphi(q)}\right)
 \le S\,\frac{8D}{W}.
\]
It follows that
\[
                       S\ge\frac{W^3}{32D},\qquad
                       v\ge\frac{W^3}{32D^2}.
\tag{19}
\]
Combining (13), (19) and \(D\le K\), obtain
\[
                  \boxed{cKD^4\ge\frac{3W^6}{8192},\qquad
                         cK^5\ge\frac{3W^6}{8192}.}
\tag{20}
\]
There is no minimum-weight, order-count or least-common-multiple hypothesis in (20).

For fixed \(W>0\), a bound \(cd\le B\) consequently forces
\[
                              K\ge
                     \left(\frac{3W^6d}{8192B}\right)^{1/5}.
\tag{21}
\]
This is weaker than (15) when a fixed positive effective weight is available, but it covers arbitrarily small individual weights at fixed total weight.
It excludes simultaneous bounded \(cd\) and bounded \(K\) under that normalization, hence excludes a uniform linear original-measure comparison through this envelope.
It does not show that the actual original-root sum has size \(K m(P)\), nor that every useful certificate must make \(cd\) bounded.

<a id="small-weight-two-order-control"></a>
## A real small-weight control and the exact norm income

The weight normalization cannot be removed.
For a prime \(p\), take precisely the two orders \(1,p\), with
\[
                  b_1=b_p=1/p,\qquad A=0,\qquad c=\frac{\log2}{p}.
\tag{22}
\]
Their complete product is \(\Phi_1(z)\Phi_p(z)=z^p-1\).
Thus (1) holds because \(|z^p-1|\le2\) on the circle, with equality at points satisfying \(z^p=-1\).
The actual parameters are
\[
             W=2/p,\qquad D=K=1,\qquad S=v=1/p,\qquad
             \ell=p,\qquad R(t)=t.
\tag{23}
\]
In particular \(cK=(\log2)/p\to0\).
If \(p/d\to\infty\), then \(cd\to0\) as well.
This is a finite positive-weight family with fixed weighted degree and fixed radial slope; it does not contradict (13) or (20), because \(v\) and \(W\) both tend to zero.

For any actual monic integer \(P\) of degree \(d\) relatively prime to \(X^p-1\), every original root and its multiplicity give the exact income
\[
 \begin{aligned}
 I_p(P)
 &=\frac1p\left(\log|\operatorname{Res}(P,\Phi_1)|
               +\log|\operatorname{Res}(P,\Phi_p)|\right)\\
 &=\frac1p\log|\operatorname{Res}(P,X^p-1)|.
 \end{aligned}
\tag{24}
\]
The unchanged all-root return is
\[
                             I_p(P)-\frac{d\log2}{p}\le m(P).
\tag{25}
\]
The nonzero integer resultant guarantees only \(I_p(P)\ge0\), making that lower-income use vacuous.
Even knowing its absolute value is at least two would supply only \((\log2)/p\).
A separate all-root divisibility floor \(2^d\), if actually supplied, would give \(d\log2/p\), exactly the scale of the displayed constant cost and tending to zero when \(p/d\to\infty\).
No such divisibility is presumed for this control.

On an original irreducible nontorsion unit input, the coprimality in (24) is automatic, and the resultant is the norm of \(\alpha^p-1\) in the original degree-\(d\) field.
No powered-field degree is substituted.
The control is available on those actual inputs without assuming a near-zero sequence, but it supplies no uniform positive certificate for them.
It illustrates why a small weighted budget cannot be judged separately from its weighted arithmetic income.

<a id="positive-kernel-original-return-boundary"></a>
## Original arithmetic normalization and the scope of the obstruction

For the general auxiliary, the complete original-root interface remains [v1's equation (13)](Yin_L_G0452_v1.md#full-original-root-radial-envelope).
For a monic integer \(P\) relatively prime to the positive-weight cyclotomic factors, it is
\[
 \Delta_A(P)+I(P)\le R(m(P)),\qquad
 \Delta_A(P)=\Re\sum_na_ns_n-cd,\qquad
 I(P)=\sum_qb_q\log|\operatorname{Res}(P,\Phi_q)|\ge0.
\tag{26}
\]
The original degree, every root multiplicity, complex coefficients and actual weights are unchanged.
On reducible inputs the exact removed-factor correction remains [v1's equation (27)](Yin_L_G0452_v1.md#rational-regularization-and-zero-boundary); no free zero removal is introduced.
Arbitrary real weights and complex coefficients still do not supply an integer positive defect.

Under multiplication of all \(b_q,A,c\) by \(\lambda>0\), the quantities \(W,D,K,c\) and \(I(P)\) scale by \(\lambda\), whereas \(S\) scales by \(\lambda^2\) and \(v\) by \(\lambda\).
Consequently (13) and (20) have exactly the required homogeneous scales.
Normalizing \(v\) or \(W\) also rescales the whole arithmetic income and the trace functional in (26); it does not retain an unscaled integer margin.

The finite positive-kernel method removes the common-period obstruction for the explicit bounds (13) and (20), including their joint dependence on a changing input.
For fixed \(W\), it rules out the simultaneous cheap constant and cheap radial-envelope proposal even if the individual weights become small.
It does not establish a bound on \(I(P)/W\), a universally positive \(\Delta_A(P)+I(P)\), or a necessary lower bound on the true correlated root sum.
A method with additional original norm income, a useful cancellation of the degree term, or a sharper correlated root estimate is therefore not ruled out.
The supplied-auxiliary and income obligations retained in C139, C141 and C570 remain at the scopes compared in v1.
No unrestricted Mahler gap or strict counterexample is obtained.

The author check covered the merged-order normalization, finite geometric orthogonality, the positive weighted kernel and diagonal, every Fourier factor and finite sum in (10), the integer-rounding and small-optimum cases, the total-weight cutoff and reciprocal-totient sum, all homogeneous powers, and the two-order control's original norm and degree accounting.
No numerical experiment, native mathematical computation, new external theorem or independent review is claimed.
