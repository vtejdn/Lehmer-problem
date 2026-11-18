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

<a id="zero-outer-reversal"></a>
## Reversal constraints when both outer coefficients vanish

Let \(H=\max_i|\Delta_i|\), with reversal in the same formal degree \(\ell-1\) even when an outer coefficient vanishes.
For every integral inverse, reduction of the [elimination congruence](../claims/Yin_C_G0345_v295.md#endpoints) modulo \(g=\gcd(L,N)\) gives
\[
                 (1-w)(\Delta^*-q\Delta)\equiv0\pmod g .
\]
Here \(q^2\equiv1\pmod g\), and the leading coefficient of \(1-w\) is a unit, so cancellation gives \(\Delta^*\equiv q\Delta\pmod g\).
Thus \(g\) divides every two-column minor of the matrix whose rows are the coefficient vectors of \(\Delta\) and \(\Delta^*\).
If \(\Delta\ne0\) and all these minors vanish, then \(\Delta^*=\varepsilon\Delta\) over \(\mathbb Q\), where applying reversal twice gives \(\varepsilon\in\{-1,1\}\).
A nonzero minor has absolute value at most \(2H^2\).

Now assume \(a=b=0\), \(q=d^2\), and \(\delta\to0\) along actual Pisot inputs.
The [branch inequalities](../claims/Yin_C_G0345_v293.md#branch) give \(j=o(q)\), so eventually \(0<j<q-1\).
Here \(v=0\), and \(S=(L/N)(q+t)\) with \(|t|<1\) places the integer \(S\) strictly between \(q-1\) and \(q+2\).
The first congruence in (2) gives \(L\mid j^2S\), so \(L/h\mid S\), where \(h=\gcd(L,j^2)=\gcd(L,N^2)\).
Since \(h\le g^2\) by (3) and its proof, we have
\[
                    g^2\ge L/S\ge L/(q+1)>q-1 .
\]
Thus \(g\ge d\), and any defect outside the two reversal symmetries must have \(H\ge\sqrt{d/2}\).
This estimate uses no bound on \(c,e\) or on the other interior coefficients.

When \(S=q+1\), put \(k=\gcd(L,q+1)=\gcd(j,q+1)\).
Then \(L/k\mid j^2\), so \(k\ge L/j^2\to\infty\).
Since \(k\mid g\) and \(q\equiv-1\pmod k\), the congruence above gives \(\Delta^*\equiv-\Delta\pmod k\).
As soon as \(2H<k\), this is the exact equality \(\Delta^*=-\Delta\).
Consequently bounded height on the \(S=q+1\) branch forces this sign for every sufficiently large input.

<a id="reversal-stability"></a>
## Stability of the even part under exact reversal

Suppose \(B(z)=D(z^2)+zE(z^2)\) is real, monic of degree \(2\ell\) and strictly stable, and \(E^*=\varepsilon E\) in formal degree \(\ell-1\), with \(\varepsilon\in\{-1,1\}\).
Then \(D\) is strictly stable.
The preceding reversal constraint on \(\Delta\) supplies the same symmetry of \(E=(q\Delta-\Delta^*)/K\).

To see the role of the symmetry, write \(G(z)=|B(z)|^2-|B^*(z)|^2\).
For each root \(\alpha\) of \(B\),
\[
       |z-\alpha|^2-|1-\overline\alpha z|^2
                         =(|z|^2-1)(1-|\alpha|^2).
\]
Multiplying the factor inequalities gives \(G(z)>0\) for \(|z|>1\).
In each unit direction \(\zeta\), the derivative of \(G(r\zeta)\) at \(r=1\) is strictly positive by the product rule, since the factors there have equal positive squared moduli and each difference has positive derivative.
The parity decomposition of \(B^*\) is \(D^*(z^2)+zE^*(z^2)\).
Averaging at \(z\) and \(-z\) cancels the mixed terms, and \(|E^*|=|E|\) gives
\[
            \frac{G(z)+G(-z)}2=|D(z^2)|^2-|D^*(z^2)|^2 .
\]
Positivity outside the disk excludes every exterior zero of \(D\).
If \(D(\zeta^2)=0\) for \(|\zeta|=1\), then also \(D^*(\zeta^2)=0\), and both squared moduli on the right vanish to at least second order along \(z=r\zeta\).
This contradicts the positive radial derivative on the left, proving strict stability.

For a nonzero symmetric or antisymmetric defect, this gives a necessary stability test at half the degree.
The [full inverse congruence](../claims/Yin_C_G0345_v295.md#parity) still has the term \(w\Delta\), which is absent from the [even-descendant gap](../claims/Yin_C_G0345_v294.md#coefficient-model).

<a id="first-occupied-pair"></a>
## The first occupied coefficient pair

For inputs with both outer coefficients zero, the [fixed first-pair argument](../claims/Yin_C_G0345_v346.md#statement) gives the two trace bounds and an explicit lower bound for the Pisot excess at bounded pair height.
For growing height below \(L/(|qS-L|+S)\), the [integer pair](../claims/Yin_C_G0345_v346.md#pair) must lie on the line spanned by \((qS-L,S)\).
The next coefficient imposes a further restriction even before testing stability.

<a id="isolated-pair"></a>
## An isolated occupied pair has height of order at least the constant term

Keep both outer coefficients zero and \(0<j<q-1\), and put \(W=qS-L\), \(h=\gcd(L,N^2)\).
For all integer indices \(i\) write \(x_i=[w^i]\Delta,\ y_i=[w^i]\Delta^*\), extending each list by zero outside its formal degree.
The [elimination identity](../claims/Yin_C_G0345_v346.md#pair) and its reversal in formal degree \(\ell\) give
\[
 \begin{aligned}
 q(qy_i-x_i)+(qx_{i-1}-y_{i-1})&\equiv0\pmod h,\\
 (qy_i-x_i)+q(qx_{i-1}-y_{i-1})&\equiv0\pmod h.
 \end{aligned}
\]
Indeed the reversed right side is \((q^2w-1)\Delta+q(1-w)\Delta^*\), and the coefficients of both left sides of the polynomial identity are divisible by \(h\).
Since \(L/h\mid S\), define \(U_i=Wy_i-Sx_i\) and \(V_i=Wx_i-Sy_i\) to obtain
\[
                     qU_i+V_{i-1}\equiv U_i+qV_{i-1}\equiv0\pmod L.
\]
In particular, if \((x_{i-1},y_{i-1})=(x_{i+1},y_{i+1})=(0,0)\), the second congruence at \(i\) and the first at \(i+1\) give \(L\mid U_i,V_i\).
For a nonzero pair the two integers \(U_i,V_i\) cannot both be zero, since \(|W|<S\).
Thus every such isolated occupied pair has
\[
            \max(|x_i|,|y_i|)\ge\frac{L}{S+|W|}>\frac{q-1}{2}.
\]
In particular, for a first occupied pair of sublinear height, \((x_{i+1},y_{i+1})\) must be nonzero.
If \(i,i+1\) are the two central indices, the latter pair reads the same two coefficients in reverse order.
On its prescribed line \((x_i,y_i)=t(W/k,S/k)\), \(k=\gcd(L,S)\), the next pair must satisfy
\[
                     U_{i+1}\equiv-q\,t(W^2-S^2)/k\pmod L .
\]
This supplies an inhomogeneous restriction on the second pair with no size assumption on deeper coefficients.
The existence of a full integral, strictly stable descendant satisfying the two consecutive conditions remains open.

<a id="occupied-runs"></a>
## Arithmetic restrictions on a run of occupied pairs

Under the hypotheses of the [isolated-pair calculation](#isolated-pair), let \(a,\ldots,b\) be a maximal run of nonzero pairs, with zero pairs at \(a-1,b+1\).
Put \(n=b-a\), \(g=\gcd(L,N)\), \(h=\gcd(L,N^2)\), \(m=h/g\), and
\[
 X(w)=\sum_{t=0}^n x_{a+t}w^t,\qquad Y(w)=\sum_{t=0}^n y_{a+t}w^t,\qquad
 H=\max_{0\le t\le n} \max(|x_{a+t}|,|y_{a+t}|).
\]
The expressions below apply to a run in the full index list \(0,\ldots,\ell-1\).
If a run crosses the center, the two rows satisfy \(Y=w^nX(1/w)\), so each repeated coefficient retains this constraint.
The following arguments require no independence of the rows.
The congruences at \(a,\ldots,b+1\) from the isolated-pair calculation depend only on two neighboring pairs at a time.
The two flanking zeros therefore give the polynomial congruences
\[
 \begin{aligned}
  (q^2-w)Y-q(1-w)X&\equiv0\pmod h,\\
  (q^2w-1)X+q(1-w)Y&\equiv0\pmod h .
 \end{aligned}                                                     \tag{19}
\]
Here the coefficients at the two ends of (19) include both interfaces with the neighboring zeros.

If each end pair has height below \(L/(S+|W|)\), those end pairs are nonzero integer multiples of \((W/k,S/k)\) and \((S/k,W/k)\), respectively, where \(k=\gcd(L,S)\).
Indeed \(L\mid U_a\) and \(L\mid V_b\) from the two flanking zeros, and the height bound makes each divisible quantity zero.
The two directions are linearly independent since \(|W|<S\).
Every adjacent determinant \(x_t y_{t+1}-y_t x_{t+1}\) is divisible by \(g\), since \(y_t\equiv qx_t\pmod g\).
At least one such determinant must be nonzero, since otherwise all nonzero vectors in the consecutive run would be collinear.
Thus a run with two small end pairs has an adjacent determinant of absolute value at least \(g\ge d\), independently of the heights in its interior.

At \(w=-1\) the two relations (19), using the negative of the second, become \((q^2+1)Y-2qX\equiv(q^2+1)X-2qY\equiv0\pmod h\), with \(X,Y\) evaluated at \(-1\).
Define \(h_+=\gcd(h,(q-1)^2)\) and \(h_-=\gcd(h,(q+1)^2)\).
Since \(q=d^2\) is even and \(h\mid (q^2-1)^2\), these two numbers are coprime and have product \(h\).
Addition and subtraction give
\[
       h_-\mid X(-1)+Y(-1),\qquad h_+\mid Y(-1)-X(-1).
\]
If the two alternating sums have unequal absolute values, their squared difference has absolute value at least \(h\), and therefore \((n+1)H\ge\sqrt h\).
On a central run the formal reversal already gives equality of those absolute values, so this last height test supplies information only on other runs.

<a id="run-resultant"></a>
## A common factor or a lower bound on run height

For \(n\ge1\), the formal-degree resultant of the two integer rows in (19) satisfies
\[
                     g h^{n-1}\mid \operatorname{Res}_{n,n}(X,Y).   \tag{20}
\]
Consequently, if the rows are coprime in \(\mathbb Q[w]\), then
\[
               H\ge\frac{(g h^{n-1})^{1/(2n)}}{\sqrt{n+1}}.         \tag{21}
\]
At least one row has degree exactly \(n\) because the last pair is occupied, so a zero formal resultant here means a common polynomial factor of positive degree when both rows are nonzero.
If one row vanishes identically, the other has degree \(n\) and itself supplies that common factor.
On a central run this possibility is the presence of a common factor of \(X\) and its reversal.

To see (20), use the integral coefficients of \(R=(Y-qX)/g\) and write \(u=N/g\).
Dividing the first congruence in (19) by \(g\) gives
\[
                        (q^2-w)R+quX\equiv0\pmod m .
\]
Here \(\gcd(qu,m)=1\), since every prime dividing \(m\) occurs in \(L\) to higher order than in \(N\), and consequently has its full \(N\)-power in \(g\).
Evaluation at \(q^2\) gives \(m\mid X(q^2)\).
Set \(Q=(X(w)-X(q^2))/(w-q^2)\in\mathbb Z[w]\), of degree at most \(n-1\) if nonzero.
Then \(X\equiv(w-q^2)Q\) and \(R\equiv quQ\pmod m\), by cancellation of the monic factor \(w-q^2\).

Apply the [Sylvester matrix divisibility argument](../claims/Yin_C_G0345_v294.md#divisibility) to \(X,R\), using formal degree \(n\) for each.
Their Sylvester matrix is congruent modulo \(m\) to that of \((w-q^2)Q,quQ\).
The latter matrix has rank at most \(n+1\) over \(\mathbb Q\), since its image in the coefficient representation consists of multiples of \(Q\) by polynomials of degree at most \(n\).
Multilinearity of the determinant then gives \(m^{n-1}\mid\operatorname{Res}_{n,n}(X,R)\).
Replacing \(Y\) by \(Y-qX=gR\) in the Sylvester matrix gives the additional factor \(g^n\) in (20).
Each row norm is at most \(\sqrt{n+1}H\) in the matrix for \(X,Y\), so Hadamard's inequality gives (21).
For example, when \(S=q\) and the first pair of the run lies on the line in the [two-trace calculation](../claims/Yin_C_G0345_v346.md#traces), we have \(h\ge L/k>q^{4/3}\) from \(\lambda=L/k=q\beta+\nu\), \(\lambda\mid j^2\), and \(\beta>q^{1/3}\).
Since \(g^2\ge h\), every such coprime block has \(H>q^{2/3-1/(3n)}/\sqrt{n+1}\).

<a id="two-pair-modulus"></a>
## Exact modulus for a run of two small pairs

Consider \(b=a+1\) with both pairs of height below \(L/(S+|W|)\).
Set \(\lambda=L/k\), \(e=h/\lambda\), \(s=S/k\) and \(\mu=\lambda/\gcd(\lambda,N)\).
Here \(\lambda\mid j^2\) follows from \(L\mid S j^2\) and \(\gcd(\lambda,s)=1\), so \(\lambda\mid h\).
The two pairs have the form \(A(W/k,s)\) and \(B(s,W/k)\) for nonzero integers \(A,B\).
In this representation the local elimination conditions (19) are equivalent to
\[
             A=eA',\qquad B=eB',\qquad B'\equiv-qA'\pmod{\mu}.
\]
Indeed, at the ends (19) requires \(h\mid A\lambda,B\lambda\).
In the middle its two conditions are \(h\mid(qB+A)F,(B+qA)F\), where \(F=(qW-S)/k=Ns-q\lambda\).
After canceling \(e\), the remaining modulus is \(\lambda/\gcd(\lambda,F)=\mu\).
Since \(\lambda\mid N^2\), one has \(\mu\mid N\), so the two middle conditions are equivalent.
If the two-pair run crosses the center, reversal also forces \(A=B\).
These tests concern necessary consequences of the integral inverse.
Whether a run with these coefficients extends to the full inverse congruence modulo \(L\) and a strictly stable \(B(z)\) remains open.

<a id="global-reciprocal-factor"></a>
## A reciprocal factor in the full integral inverse

Let \(G\in\mathbb Z[w]\) be monic, irreducible and reciprocal up to sign, with \(G(0)=\pm1\) and degree \(r\ge1\).
Suppose \(G\mid\Delta\) for the full defect of an actual positive-constant Pisot input.
Then \(G\) also divides its formal reversal \(\Delta^*\).
A common factor of one [run](#run-resultant) gives this hypothesis when every run in the decomposition of \(\Delta\) has that factor.
In particular, for a single reflected pair of runs it suffices that \(G\) divide the two local rows \(X,Y\), since reflecting the second row preserves the reciprocal factor.
Other runs can contribute a nonzero remainder modulo \(G\).

Let \(\lambda=L/\gcd(L,N^2)\).
The remainder of \(V\) on monic division by \(G\) is a nonzero polynomial in \(\lambda\mathbb Z[w]\), and
\[
                 0\ne\operatorname{Res}(G,V)\in\lambda^r\mathbb Z .
\]
Indeed, reduce the [elimination congruence](../claims/Yin_C_G0345_v346.md#pair) in the free \(\mathbb Z\)-module \(\mathbb Z[w]/(G)\).
Its right side vanishes there, so every coefficient of the reduced \(N^2 V\) is divisible by \(L\).
The polynomial \(V\) is nonzero, since an even \(f\) with exterior root \(\theta\) would have the exterior root \(-\theta\) as well.
If \(G\mid V\), reciprocity gives \(G\mid V^*\) as well, and the [exact inverse identity](../claims/Yin_C_G0345_v295.md#parity) gives \(G\mid U\) over \(\mathbb Q\).
Then \(G(z^2)\) would be a proper factor of the irreducible \(f=U(z^2)-zV(z^2)\), since \(0<r\le\deg V\le\ell<d/2\) in this case.
Thus \(G\nmid V\), and irreducibility of \(G\) now gives \(\gcd(G,V)=1\).
Taking the norm of the remainder at a root of \(G\) proves the resultant divisibility.
In particular a proposed inverse with every coefficient of this remainder strictly smaller than \(\lambda\) in absolute value is impossible.

<a id="torsion-factor-returns"></a>
## Factors at \(1,-1\) and the returned polynomial

Write \(P=(zf+f^*)/(z+1)\), keeping the entire integral polynomial of degree \(d\).
The numerator vanishes at \(-1\) because \(d\) is even.
At a root of \(G\), the parity inverse gives \(E=E^*=0\).
If \(w-1\mid\Delta\), its equations at one give \(LU(1)=NV(1)\).
Since \(f(1)<0\), there is a positive integer \(t\) such that
\[
          -P(1)=-f(1)=\frac jg t,\qquad
          f(-1)=\frac{L+N}{g}t,\qquad g=\gcd(L,N).
\]
Indeed \(U(1)=(N/g)t,\ V(1)=(L/g)t\) and \(f(\pm1)=U(1)\mp V(1)\).

If \(w+1\mid\Delta\), put \(\varepsilon=(-1)^\ell\), \(b=(q-\varepsilon)^2\) and \(c=\gcd(L,b)\).
The full descendant has \(B(\pm i)=D(-1)\ne0\) by strict stability.
Since \(D^*(-1)=\varepsilon D(-1)\), the inverse gives \(U(-1)=(q\varepsilon-1)D(-1)\) and \(V(-1)=(L/N)(q+\varepsilon)D(-1)\).
Thus \(b V(-1)=\varepsilon L U(-1)\), and for a nonzero integer \(s\) we obtain
\[
            V(-1)=\frac Lc s,\qquad U(-1)=\frac{\varepsilon b}{c}s,
            \qquad |P(i)|=\frac{|b-L|}{c}|s|.
\]
For the last identity, \(f(i)=U(-1)-iV(-1)\) and \(f^*(i)=-\varepsilon\overline{f(i)}\).
Substitution in \(P(i)\) gives \(|P(i)|=|U(-1)-\varepsilon V(-1)|\).
These tests apply to a Salem minimal polynomial itself when it is the entire return \(P\).

For a concrete stable control take \(d=10,\ q=100\) and
\[
               f(z)=z^{10}-200z^9+z^6+z^4-2z+100 .
\]
On the unit circle the term of magnitude \(200\) dominates the others, whose magnitudes sum to \(105\).
Rouché gives nine roots strictly inside, and \(f(1)<0\) gives a real exterior root greater than one.
Any proper monic factor containing only inside roots would have nonzero integral constant term of absolute value less than one, proving irreducibility.
Here \(N=9999,\ L=19998,\ j=N,\ V=200w^4+2\).
Deleting the two added even terms \(z^6+z^4\) would give \(A=N(2z^9-1)\) and descendant \(z^8\), of zero defect.
Restoring them leaves \(L,V\) fixed and increases \(U\) by \(w^3+w^2\), so the exact inverse identity gives \(\Delta=-Lw(w+1)\).
The central two-pair run therefore has \(w+1\) as a common factor of its two local rows.
Here \(c=\gcd(19998,99^2)=99\) and \(V(-1)=202=L/c\), attaining the nonzero divisibility bound.
This actual input has \(\delta>N/(q+2+q^{-1})>98\) by the [branch inequality](../claims/Yin_C_G0345_v293.md#branch).
It demonstrates compatibility with full stability on a large branch and leaves the shrinking-excess class unresolved.

<a id="remaining"></a>
## Remaining escape patterns

At the prescribed scale \(q=d^2\), the first two exclusions allow arbitrary interior coefficients while requiring bounded \(a,b,c,e\).
With both outer coefficients zero, the [first occupied pair](#first-occupied-pair) must escape every fixed height bound along a shrinking sequence.
At sublinear pair height its ratio is fixed by \(q,j,S\), and the [next pair](#isolated-pair) is nonzero with a prescribed congruence.
In the two exact symmetry classes the [half-degree stability test](#reversal-stability) and the content bound both apply.
Other open patterns include both outer coefficients nonzero and \(a=0\), \(b\ne0\), \(c\ne0\).
The relations \(b=\pm a\) and \(ae=bc\) identify specific arithmetic degeneracies worth testing; their occurrence is not asserted to produce a stable input.
No quantitative positive gap for the full unrestricted model, stable construction, or new Salem output is established here.
