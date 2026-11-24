---
author: Yin
---

# Primitive two-row graphs at every prime above a prescribed degree-dependent cutoff

<a id="statement"></a>
## One seed at each selected degree

For an even degree \(d\ge2\) and an odd prime \(p\), consider graphs
\[
                   G(X)=A(X^p)+X C(X^p)
\]
with nonzero integral rows \(A,C\) of degrees at most an integer \(d\le b\le2d\).
Require the rows to be coprime over \(\mathbb Q[Y]\), to satisfy \(AA^\iota-CC^\iota\ne0\), with \(\iota(Y)=Y^{-1}\), and to have \(H=\max(\|A\|_1,\|C\|_1)\le2^p\), where \(\|\cdot\|_1\) is coefficient one-norm.
Require that \(G\) have a double monic reciprocal irreducible factor of degree \(d\) with a nontorsion unit root.
Require also that the gcd of the differences of the occupied exponents of \(G\) be one.
In fact one may require that each of \(A,C\) have two consecutive occupied exponents.
Let \(S(d,p)\) be the least of \(\log 2\) and the scores
\[
                         (b-d)/d +(\log H)/p
\]
of the graphs passing the stated conditions.
Testing a fixed \(d,p\) uses finite coefficient enumeration and factorization and imposes no restriction on the other factors of \(G\).

Write \(\lambda\) for the infimum of positive logarithmic Mahler measures of nonzero integer polynomials.
For every prescribed real function \(L(d)\to\infty\), the following assertions are equivalent.

1. \(\lambda=0\).
2. There are even degrees \(d_j\to\infty\) and positive \(\eta_j\to0\) such that, for every odd prime \(p\ge L(d_j)\), a graph passes with score at most \(\eta_j\). At each \(d_j\), the same irreducible double factor can be used for all those primes.

In particular, for any preassigned odd prime \(p(d)\) at each even degree with \(p(d)\to\infty\),
\[
                \lambda=0\quad\Longleftrightarrow\quad
                    \liminf_{\substack{d\to\infty\\2\mid d}}S(d,p(d))=0.
\]
The degree sequence may depend on the prescribed cutoff.
The [linear prime interval for an original seed](Yin_C_G0901_v2.md#window) leaves the seed unchanged and allows exceptional primes.
Here the new degrees come from irreducible power substitutions of the seeds, while the parent graphs are primitive in their exponent differences.

<a id="offset"></a>
## A base pair uniform in the residue offset

Fix the monic reciprocal minimum \(P_0\) of a nontorsion unit \(\alpha\), with degree \(e\) and \(0<h=m(P_0)\le1\).
Put \(k=\lceil e\sqrt h\rceil,\ B=e+k,\ R=k+1,\ s=\min(e,R)\).
For every sufficiently large prime \(p\) and every integer \(1\le t<p\) there are coprime integral rows \(U,V\) of degrees at most \(B\) such that
\[
 P_0^2\mid F(X)=U(X^p)+X^t V(X^p),\qquad \Delta_0=UU^\iota-VV^\iota\ne0 .
\]
The rows are nonzero and can be selected with
\[
 \limsup_{p\to\infty}\ \max_{1\le t<p}
       \frac{\log\max(\|U\|_1,\|V\|_1)}p \ \le\ \frac{2(B+1)h}{s}.       \tag{1}
\]

For the details take \(p>e+1\) with \(p\nmid\operatorname{disc}P_0\), put \(z=\alpha^p\), and let \(Q\) be its monic minimum.
The [power-field argument](Yin_C_G0901_v2.md#finite) gives \(\deg Q=e\).
For pairs divisible by \(Q\) in both rows, the quotient rows \(U_1,V_1\) satisfy \(U_1(z)+\alpha^t V_1(z)=0\) since \(Q(X^p)\) has a simple zero at \(\alpha\).
This value map has rank at least \(\min(e,R)\) on its first row alone.
For integral pairs of double contact, the derivative on reduction modulo \(p\) is \(tX^{t-1}\bar V(X)^p\).
Since \(t\not\equiv0\bmod p\) and \(X\) is coprime to \(\bar P_0\), squarefreeness and the graph value force \(\bar P_0\) to divide both reduced rows.
On a rational subspace with identically zero reflected determinant, reduction of its saturated lattice therefore injects into the \(R\)-dimensional space for the first row, as a zero first row forces the second to vanish as well.
Both unwanted dimensions are at most \(2R-s\).

The coefficient box has \(N=2B+2\) positions and largest possible exponent \(D=pB+t\).
The [two-jet count and four scalar choices](Yin_C_G0901_v2.md#finite) now apply with this \(D\) and zero rank loss at the prime.
They give a pair with nonzero reflected determinant and both row values nonzero at \(z\).
Its logarithmic height before removing common factors is at most
\[
 \frac{2Dh+2e\log(6N)+e\log(1+D)+(2R-s)\log3}{s}+\log(10(B+1)).
\]
Removing the common divisor preserves the double factor and nonzero reflected determinant, since its value at \(z\) is nonzero.
For fixed \(B\) the log cost of that division is at most \(B\log 2\) by the elementary symmetric coefficient bound.
The estimate \(D\le p(B+1)\) gives (1) uniformly in \(t\).

<a id="primitive"></a>
## Mixing a power substitution with its reflection

Let \(n\ge3\) be a power of an odd prime \(\ell\ne p\), and take \(1\le t<p\) with \(nt\equiv1\bmod p\).
For a base pair as above put \(w=(nt-1)/p\) and \(Y=X^p\).
Then
\[
       f(X)=F(X^n)=u(Y)+Xv(Y),\qquad
       u(Y)=U(Y^n),\quad v(Y)=Y^wV(Y^n).
\]
Choose \(a=n(pB+t)+p=1+pJ\), so \(J=nB+w+1\) and \(a\ge\deg f\).
For a positive integer \(c\), set
\[
                G_c(X)=f(X)+(c+X^p)X^a f(1/X).
\]
The three summands have disjoint exponent classes \(0,p,2p\bmod n\), since \(n>2\) and \(\gcd(p,n)=1\).
The original graph \(f\) occupies both classes \(0,1\bmod p\), and so does its shifted reflection.
For each occupied exponent of that reflection, its two copies have exponents differing by \(p\).
Thus each row of \(G_c\) has two consecutive occupied exponents, and the gcd of the graph's exponent differences is one.
The polynomial \(P_0(X^n)^2\) divides both \(f\) and \(X^a f(1/X)\) by reciprocal symmetry and the nonzero constant term of \(P_0\).

The two rows of \(G_c\) are
\[
 A=u+(c+Y)Y^Jv^\iota,\qquad C=v+(c+Y)Y^Ju^\iota.
\]
Their degrees are at most \(b=nB+w+2\).
Their reflected determinant is
\[
 AA^\iota-CC^\iota=
       \bigl(1-(c+Y)(c+Y^{-1})\bigr)\Delta_0(Y^n)\ne0 ,
\]
by cancellation of the mixed terms.
Their one-norms are at most \((c+2)\max(\|U\|_1,\|V\|_1)\).

A common nonzero row root \(\gamma\) would give \(y=\gamma^n\) with \(\Delta_0(y)=0\): the determinant of the two *unmixed* row vectors \((u,v)\) and \(Y^J(v^\iota,u^\iota)\) is \(Y^J\Delta_0(Y^n)\), and the vectors would be proportional at \(\gamma\).
There are at most \(2B\) possible \(y\), by clearing the Laurent powers in \(\Delta_0\).
For each such \(y\), both \((U(y),V(y))\) and \((V(1/y),U(1/y))\) are nonzero by base coprimality.
The equation \(\Delta_0(y)=0\) makes these vectors proportional.
Using either nonzero coordinate in \(A(\gamma)=C(\gamma)=0\) and \(J-w=nB+1\) therefore gives
\[
                         \gamma^2+c\gamma=D_y\in\mathbb Q(y)^\times ,
\]
where \(D_y=-y^{-B}U(y)/V(1/y)\) when that quotient is defined, and otherwise \(D_y=-y^{-B}V(y)/U(1/y)\).
In particular every possible \(\gamma\), allowing \(c\) to vary, has degree at most two over \(\mathbb Q(y)\).
If one such \(\gamma_0\) exists, any ratio \(\gamma/\gamma_0\) is an \(n\)-th root of unity in an extension of absolute degree at most \(4[\mathbb Q(y):\mathbb Q]\le8B\).
Its order is a power of \(\ell\), hence at most \(16B\), because \(\varphi(\ell^j)\ge\ell^j/2\).
All such roots of unity lie in the group of the largest allowed \(\ell\)-power order.
Thus at most \(16B\) different \(\gamma\)'s occur at each \(y\), and each \(\gamma\) forbids at most one integer \(c\) by the quadratic equation.
Some \(1\le c\le32B^2+1\) avoids all common nonzero roots, independently of \(n\) and \(p\).
At this \(c\), remove the common power of \(Y\) from the two rows.
This merely translates the exponents of the graph, preserving the double factor, the nonzero reflected determinant, the two adjacent exponents in each row and the coefficient norms.
The resulting rows are coprime over \(\mathbb Q[Y]\).

<a id="tower"></a>
## Choosing one degree for the entire tail of primes

For each fixed seed \(P_0\) one can choose an odd prime \(\ell\) such that \(P_0(X^{\ell^m})\) is irreducible for every \(m\ge1\), with logarithmic measure \(h\).
Indeed \(\alpha\) can be an \(\ell\)-th power in \(\mathbb Q(\alpha)\) for only finitely many primes \(\ell\).
Any such root has degree at most \(e\) and absolute logarithmic height equal to the height of \(\alpha\) divided by \(\ell\); bounded degree and height allow only finitely many algebraic numbers, and \(\alpha\) is nontorsion.
Take an odd \(\ell\) outside this finite set and apply the [prime binomial criterion and norm induction](Yin_C_G0345_v387.md#substitutions) at the repeated prime \(\ell\).
Explicitly, if \(X^{\ell^m}-\alpha\) is irreducible over \(\mathbb Q(\alpha)\), a root has relative norm \(\alpha\) since \(\ell^m\) is odd.
Its being an \(\ell\)-th power in the new field would make \(\alpha\) an \(\ell\)-th power in the base field.
Irreducibility therefore persists at the next step, starting at \(m=0\).
The absolute degree is \(e\ell^m\) by the tower law, and replacing each root of \(P_0\) by all its \(\ell^m\)-th roots preserves the sum of positive logarithms.

Assume \(\lambda=0\).
By the [reciprocal reduction](Yin_C_G0345_v408.md#lower) choose seeds \(P_{0,j}\) with log measures \(0<h_j\le1\) tending to zero and degrees \(e_j\to\infty\).
For each seed fix \(k_j,B_j,s_j\) as in (1) and choose its tower prime \(\ell_j\).
Since \(s_j\ge k_j\ge e_j\sqrt{h_j}\), one has \(2(B_j+1)h_j/s_j\le 2\sqrt{h_j}+4h_j\).
Equation (1) supplies a finite threshold \(T_j>\ell_j\) beyond which the normalized base log height is at most \(3\sqrt{h_j}+4h_j\) for every offset.
Enlarge \(T_j\) so that \(\log(32B_j^2+3)/T_j\le\sqrt{h_j}\).
Choose \(n_j=\ell_j^{m_j}\ge3\) so large that \(d_j=e_jn_j\) exceeds all earlier chosen degrees and \(L(d_j)\ge T_j\).
This is possible for every prescribed \(L(d)\to\infty\).

For every prime \(p\ge L(d_j)\), the base construction applies at the required offset and \(p\ne\ell_j\).
The mixed graph at this prime has the same degree-\(d_j\) double factor \(P_{0,j}(X^{n_j})\) with log measure \(h_j\).
It satisfies \((\log H)/p\le4\sqrt{h_j}+4h_j\).
As \(0\le w<n_j\), we may take \(b=n_jB_j+w+2\), with
\[
             0\le (b-d_j)/d_j
                   \le (k_j+1+1/n_j)/e_j \longrightarrow0 .
\]
Hence \(b\le2d_j\) and \(H\le2^p\) after discarding finitely many initial \(j\), and the score tends to zero uniformly over all the indicated primes.
Conversely, every qualifying pair has \((\log H)/p\ge\lambda\) by the [individual determinant bound](Yin_C_G0345_v408.md#lower), and the fallback also bounds \(\lambda\).
This proves both equivalences.
The primitive exponent differences belong to the parent graph; its irreducible repeated factor in this construction is a power substitution and has the same measure as its base seed.

## Assessment history

### Decision prescribed-prime-test

| Field | Value |
| --- | --- |
| date | 2026-11-24T17:52 |
| status | proved |
| reason | The offset construction and reflection give an equivalent test with one prescribed prime per degree and primitive parent supports. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Prime schedules](#statement) | Equivalent zero-gap criteria for primitive parent graphs with one double factor for the full tail at each selected degree. |
| argument | [Uniform base construction](#offset) | Two-jet witnesses at every residue offset for the fixed seed. |
| argument | [Mixing and coprimality](#primitive) | Primitive span, adjacent positions in each row and the bounded cost of avoiding common nonzero roots. |
| argument | [Irreducible representatives](#tower) | Degree selection, preservation of measure and the simultaneous prime quantifiers. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1044.md#finding) | The full statement, base estimates, mixing, choice of degrees and the restriction on the constructed factors. |

## Current assessment

[Selected decision](#decision-prescribed-prime-test)
