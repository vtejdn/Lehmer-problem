---
author: Yin
---

# Bounded fringe coefficients of a general Schur defect

This is continuing author-side work for [G0001](../tasks/Yin_T_G0001_v1.md#contract).
It extends the coefficient tests in the [general parity formulation](../claims/Yin_C_G0345_v295.md#parity), rather than imposing a bound on the whole defect or constructing another sparse polynomial family.
The calculations below have been checked during development, without an independent review or a fixed mathematical assessment.

<a id="question"></a>
## Two exclusions with unrestricted interior coefficients

Consider actual positive-constant Pisot inputs in the [Schur correspondence](../claims/Yin_C_G0345_v293.md#correspondence), along a hypothetical sequence
\[
 d=2\ell+2\longrightarrow\infty,\qquad q=d^2,\qquad
 \delta=\theta-q\longrightarrow0.
\]
Use
\[
 N=q^2-1,\quad L=N+j,\quad K=L^2-N^2,\quad \rho=L/N,
 \qquad B=D(z^2)+zE(z^2),\quad
 \Delta=\frac KN(qE+E^*).
\]
The polynomial \(B\) is monic and strictly stable of degree \(s=d-2=2\ell\), and every coefficient denominator divides \(K\).
The integral defect \(\Delta\) has formal degree \(\ell-1\).
Put
\[
 a=\Delta_0,\qquad b=\Delta_{\ell-1},\qquad
 c=\Delta_1,\qquad e=\Delta_{\ell-2}.
\]
Assume only that these four integer coefficients are uniformly bounded.
All other coefficients of \(\Delta\), and all unmentioned coefficients of the integral inverse, may vary without a height bound.

Neither of the following patterns can persist along such a sequence:

1. \(b=0\) and \(a\ne0\), with arbitrary bounded \(c,e\).
2. \(a=c=0\) and \(b\ne0\), with arbitrary bounded \(e\).

The proof uses stability only of the full \(B\).
It does not infer stability of \(D\) or of the half-degree polynomial \(V\) below.
All edge coefficients used in the proof are distinct eventually, since \(\ell\to\infty\).
In particular the coefficient formulas are applied only for \(\ell\ge3\), and the four named defect positions are distinct for \(\ell\ge4\).

<a id="edges"></a>
## Edge identities without a coprimality assumption

Write the integral inverse as \(f=U(z^2)-zV(z^2)\), and set
\[
 S=V_\ell,\qquad T=V_{\ell-1},\qquad
 t=B_0,\quad u=B_1,\quad x=B_2,\quad
 y=B_{s-2},\quad v=B_{s-1},\quad r=B_{s-3}.
\]
The exact inverse gives
\[
 \begin{gathered}
 E=\frac{q\Delta-\Delta^*}{K},\qquad
 u=\frac{qa-b}{K},\quad v=\frac{qb-a}{K},\quad
 r=\frac{qe-c}{K},\\
 S=\rho(q+t)-v,\qquad V_0=qS-L,\\
 T=\rho(qy+x)-r-qu,\qquad
 Lx=qV_1-T+Nr.                                      \tag{1}
 \end{gathered}
\]
Reversal of \(\Delta,E\) uses formal degree \(\ell-1\), while reversal of \(V,D\) uses degree \(\ell\).

The general elimination identity is
\[
 N^2V\equiv(q^2-w)\Delta^*-q(1-w)\Delta\pmod L.
\]
Its leading, next-to-leading and linear coefficients give
\[
 \begin{split}
 j^2S&\equiv qb-a,\\
 j^2(T+S)&\equiv-ja+qe-c,\\
 j^2V_1&\equiv q^2e-b-qc+qa\pmod L.                 \tag{2}
 \end{split}
\]
Here \(N\equiv-j\pmod L\) was used, without dividing by \(N\), \(j\), or any fringe coefficient.

There is a useful limited gcd conclusion.
Let
\[
 g=\gcd(N,L),\qquad h=\gcd(L,N^2).
\]
The first congruence in (2), equivalently \(N^2S\equiv qb-a\), implies \(g\mid qb-a\).
Since \(q^2\equiv1\pmod g\), it follows that
\[
                         g\mid b^2-a^2.             \tag{3}
\]
For every prime, if its exponents in \(L,N\) are \(\lambda,\nu\), then
\(\min(\lambda,2\nu)\le2\min(\lambda,\nu)\).
Consequently \(h\mid g^2\), and in particular \(h\le g^2\).
When \(b^2-a^2\ne0\), bounded fringe coefficients therefore bound both \(g\) and \(h\).
The relations \(b=a\) and \(b=-a\) are exceptions to this bound; (3) alone does not exclude them.
For the second pattern in the statement, \(a=0\) and \(g\mid qb\), while \(\gcd(g,q)=1\), so the stronger conclusion is \(g\mid b\) and \(h\le b^2\).

<a id="bounds"></a>
## Uniform bounds supplied by the actual Pisot input

The [branch identity](../claims/Yin_C_G0345_v293.md#branch) gives \(j/q\to0\).
The [returned-degree requirement](../ledger/Yin_L_G0462_v36.md#degree) also gives
\[
                              j/d\longrightarrow\infty.           \tag{4}
\]
Indeed, if \(j\le Md\) on a subsequence, the required lower bound
\(\log r_{\rm out}\gg(q/j)^{1/6}\log((q/j)^{1/6})\) would contradict \(r_{\rm out}\le d+1\) at \(q=d^2\).
This uses the degree of the returned Salem factor, not an identification of that degree with the seed degree.
In particular \(j\to\infty\).

Bounded fringe coefficients and \(K=j(2N+j)\) give
\[
 |u|+|v|+|r|=O(1/(jq)).
\]
Since \(|t|<1\), the formula for \(S\) in (1) places it between
\[
 q-1+\frac{j}{q+1}-O(1/(jq))
 \quad\hbox{and}\quad
 q+1+\frac{j}{q-1}+O(1/(jq)).
\]
Thus eventually
\[
                         S=q+\sigma,\qquad \sigma\in\{0,1\}.       \tag{5}
\]
The lower endpoint is greater than \(q-1\), because \(j\to\infty\); the upper endpoint is less than \(q+2\), because \(j/q\to0\).

Newton's identity and the product expansions for the strictly interior roots of \(B\) yield
\[
 |y|<\frac{s+v^2}{2}=O(d),\qquad
 |x|<\binom{s}{2}<q/2.
\]
Equation (1) consequently gives
\[
                              T=O(qd)=o(L).                         \tag{6}
\]
Every constant implicit here may depend on the fixed bound for the four fringe coefficients, but not on the unspecified interior coefficients.

We shall also use a consequence of two strict Schur steps.
Put
\[
 \alpha=1-t^2,\qquad \gamma=u-tv,\qquad \kappa=v-tu.
\]
The first transform \((B-tB^*)/z\) has leading coefficient \(\alpha>0\), constant \(\gamma\), next-to-leading coefficient \(\kappa\), and linear coefficient \(x-ty\).
Its next Schur transform has leading coefficient \(\alpha^2-\gamma^2>0\) and constant \(\alpha(x-ty)-\gamma\kappa\).
Strict stability therefore gives
\[
 \left|x-ty-\frac{\gamma\kappa}{\alpha}\right|
      <\alpha-\frac{\gamma^2}{\alpha},\qquad
 |x-ty|<\alpha+\frac{|\gamma\kappa|}{\alpha}.         \tag{7}
\]
This is the [two-Schur inequality](../claims/Yin_C_G0345_v295.md#two-schur), with its short derivation repeated to specify exactly which stability information is used.

The formula for \(S\) gives
\[
 t=\frac{NS-qL+Nv}{L}.
\]
If \(\sigma=0\), then \(t=O(j/q)\) and \(\alpha\to1\).
If \(\sigma=1\), then \(1-t\asymp j/q\) and \(\alpha\asymp j/q\).
In both cases \(\gamma,\kappa=O(1/(jq))\), and
\[
 |\gamma\kappa|/\alpha=o(1).
\]
For the second case it is \(O(1/(j^3q))\); for the first it is \(O(1/(j^2q^2))\).

<a id="low-fringe"></a>
## Nonzero constant fringe and zero top fringe

Assume \(b=0\), \(a\ne0\).
Multiply the second congruence in (2) by \(S\), and use the first one, \(j^2S\equiv-a\).
This yields
\[
 aT\equiv[a(j-1)+c]S+e(j-1-\sigma q)\pmod L,        \tag{8}
\]
where \(qS\equiv1-j+\sigma q\pmod L\) was used.
The left side is \(O(qd)=o(L)\) by (6).
The right side is \(O(jq+q)=o(L)\), since all four fringe coefficients are bounded and \(j/q\to0\).
The congruence is therefore an equality eventually.
Since \(|a|\ge1\), that equality and \(S\asymp q\) force \(j=O(d)\).
More explicitly, the term \(a(j-1)S\) has magnitude at least \((j-1)q\), whereas the remaining terms are bounded by a fixed multiple of \(qd+q+j\).
This contradicts (4).
No modular inverse or coprimality premise was used.

<a id="high-fringe"></a>
## Zero constant and linear fringes, with nonzero top fringe

Assume \(a=c=0\), \(b\ne0\), allowing arbitrary bounded \(e\).
Here
\[
 u=-b/K,\qquad v=qb/K,\qquad r=qe/K,
 \qquad g\mid b,\quad h\le b^2.
\]
Multiply the second congruence in (2) by \(b\), and use the first one to obtain
\[
                    j^2[bT+(b-e)S]\equiv0\pmod L.
\]
Since \(\gcd(L,j^2)=\gcd(L,N^2)=h\), the modulus \(L/h\) divides the bracket.
The bracket is \(O(qd)=o(L/h)\), because \(h\) is uniformly bounded.
Hence eventually
\[
                            bT=(e-b)S.                              \tag{9}
\]

Set
\[
                         Z=bx-et.
\]
Using (1) and \(Lt=NS-qL+Nv\), the terms involving \(r,v\) cancel exactly:
\[
 LZ=bqV_1-bT-eNS+eqL\in\mathbb Z.                  \tag{10}
\]
Also \(KZ\in\mathbb Z\), because the coefficient denominators of \(B\) divide \(K\).
Thus the denominator of \(Z\) divides \(\gcd(L,K)=h\).

To bound \(Z\), equation (9) and the formula for \(T\) give
\[
 y=\left(\frac eb-1\right)
       \left(\frac{NS}{qL}+\frac{bN}{KL}\right)-\frac{x}{q}
   =\Lambda-\frac{x}{q},                            \tag{11}
\]
where \(\Lambda\) is uniformly bounded.
The second inequality in (7) becomes
\[
 |x(1+t/q)-t\Lambda|
     <\alpha+|\gamma\kappa|/\alpha=O(1).
\]
Since \(|t|<1\), it follows that \(x\), and therefore \(Z\), are uniformly bounded.
Write \(Z=p/h\); both integers \(p\) and \(h\) are now uniformly bounded, with \(h>0\).

Substitute (9) into (10), multiply by \(h\), and reduce modulo \(q\).
The result is
\[
                         p(j-1)\equiv hb\sigma\pmod q.              \tag{12}
\]
Both sides have difference \(o(q)\), so (12) is an equality eventually.
Because \(j\to\infty\), bounded integer \(p\) must then vanish, and \(b\ne0\) forces \(\sigma=0\).
Consequently \(S=q\), \(Z=0\), and (10) reduces to
\[
                         bV_1=e(1-j)-b.                             \tag{13}
\]

The first and third congruences in (2) now imply
\[
             L\mid q(j^2-b),\qquad L\mid V_1(j^2-b).                \tag{14}
\]
For the second divisibility, use \(q^2\equiv1-j\pmod L\) and (13).
Let \(r_0=L/\gcd(L,j^2-b)\).
Then (14) gives \(r_0\mid q,V_1\), and \(r_0\mid L\) also gives \(r_0\mid j-1\).
Equation (13) therefore implies \(r_0\mid b\).
It follows that
\[
                              L\mid b(j^2-b).                        \tag{15}
\]
But \(j^2=o(L)\) and \(b\) is bounded, so (15) forces \(j^2=b\) eventually.
This contradicts \(j\to\infty\), proving the second exclusion.

<a id="paired-coefficients"></a>
## A useful paired-coefficient identity and its limit

The integral polynomial \(A=LzB-NB^*\) gives, for \(0\le i\le s-1\),
\[
 \begin{split}
 j(B_i+B_{s-1-i})&\in\mathbb Z,\\
 (L+N)(B_i-B_{s-1-i})&\in\mathbb Z.                 \tag{16}
 \end{split}
\]
Indeed the two paired coefficients of \(A\) are \(LB_i-NB_{s-1-i}\) and \(LB_{s-1-i}-NB_i\); take their sum and difference.
For arbitrary bounded fringe coefficients, put
\[
                       Z=bx-et,\qquad \chi=ae-bc.
\]
Since \(br-ev=\chi/K\), equation (16) gives
\[
          j(Z+\chi/K)\in\mathbb Z,\qquad
          (L+N)(Z-\chi/K)\in\mathbb Z.              \tag{17}
\]
The exact inverse also gives
\[
 LZ-\frac{N\chi}{K}
             =bqV_1-bT-eNS+eqL\in\mathbb Z.         \tag{18}
\]
For the high-fringe class above, \(\chi=0\), so (17)--(18) improve the denominator bound for \(Z\) from \(h\) to \(\gcd(j,L)=g\mid b\).
The proof was written with the weaker \(h\le b^2\) bound to keep the cancellation in (10) explicit.
For general bounded \(\chi\), the error \(j\chi/K\) in (17) is \(O(q^{-2})\).
This is a short arithmetic constraint, but it alone neither bounds \(Z\) nor forces \(\chi=0\).

<a id="remaining"></a>
## Remaining escape patterns

The exclusions concern actual inputs with uniformly bounded fringe coefficients at the prescribed scale \(q=d^2\).
They show that arbitrarily large interior coefficients cannot rescue either of the two stated fringe patterns.
They leave, among other possibilities, both outer fringe coefficients zero, both nonzero, or \(a=0\), \(b\ne0\), \(c\ne0\).
Unbounded fringe coefficients are also outside the hypotheses.
The relations \(b=\pm a\) and \(ae=bc\) identify specific arithmetic degeneracies worth testing; their occurrence is not asserted to produce a stable input.
No quantitative positive gap for the full unrestricted model, stable construction, or new Salem output is established here.
