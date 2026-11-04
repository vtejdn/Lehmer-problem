---
author: Yin
---

<a id="ope26b-u001"></a>
# Ope26b-U001: an integral group-ring determinant below one

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26b, [retained PDF](../../../literature/pdf/Ope26b.pdf), OpenAI, *A Counterexample to the Group-Ring Determinant Conjecture*, September 23, 2026, 9 pages, openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb; PDF. This is the group-ring determinant manuscript in family 197, not every manuscript in that family.

Passages: Theorem 1.1, p.2; exact companion input Theorem 1.2, p.2; internal reduction, Sections 2–5, pp.3–8, especially Proposition 2.2, Lemmas 3.1–3.2 and 4.1–4.2, and Proposition 4.3. Printed and PDF pages coincide.

Inspection: 2026-10-08, human record author Yin.
The coordinating AI reviewer read the full source and inspected rendered pp.1,5,8.
A separately assigned AI reviewer rederived the complete conditional reduction in Sections 2–5, including its conventions, integrality, ordered matrix products and spectral estimates, then reconciled its exact input with the separately reviewed companion.
This arrangement was not blind: the earlier discussion and its explanatory conclusions were supplied as context.
Neither reviewer developed the external proof.
The findings below record the actual mathematical checks; no independent personal human inspection is asserted.


## Assessment and exact dependency boundary

**Audited within scope** for Theorem 1.1 and its complete supporting chain, using the reviewed characteristic-two existence theorem in [Ope26-U001](../Ope26/Yin_U001.md#ope26-u001).
That companion in turn uses the established least-prime bound accepted at the statement and applicability scope recorded in [Xyl11-U001](../Xyl11/Yin_U001.md#xyl11-u001).
The latter theorem's original analytic-number-theory proof was not re-audited.

The determinant argument is a complete reduction from its Theorem 1.2; the separate companion review resolves that exact input at the scope recorded in Ope26-U001.
No gap was found in the reduction or its interface with the companion.
This is a checked existence proof, not an executed finite example: no explicit numerical field, finite presentation and fully expanded matrix were computed from the companion's terminating prescription.

The source's historical comparisons and its separate nonsofic consequence are outside the adopted result group here.
Their exclusion does not leave a construction dependency unresolved.

## Statement and conventions

There are a finitely generated discrete group $G_D$, an integer $n\ge1$, and a square matrix
$$
A\in M_n(\mathbb Z[G_D]),\qquad A^{-1}\in M_n(\mathbb Q[G_D]),
$$
whose Fuglede–Kadison determinant lies strictly between zero and one.

The ordinary group ring consists of finite sums.
The source represents it by left convolution:
$$
(L_g\xi)(h)=\xi(g^{-1}h).
$$
For the matrix operator $T_A$ on $\ell^2(G_D)^n$, the trace is the sum of the diagonal group traces, with $\tau_n(I_n)=n$.
For invertible operators,
$$
\log\Delta_{G_D}(A)
=\frac12\tau_n\bigl(\log(T_A^*T_A)\bigr).
$$
The source also uses a probability measure
$$
\mu_A(E)=\frac1n\sum_{i=1}^n
\langle 1_E(T_A^*T_A)e_i,e_i\rangle.
$$
Thus
$$
\log\Delta_{G_D}(A)=\frac n2\int_{(0,\infty)}\log t\,d\mu_A(t).
$$
The matrix determinant itself is not normalized by taking an $n$th root.

The constructed $A$ has a bounded inverse.
Its positive-square spectrum is therefore contained in a compact subinterval of $(0,\infty)$, its zero spectral atom is absent, and its logarithmic integral is finite and negative.
The example violates the lower bound one; it does not exploit a divergent integral or exclusion of a nonzero kernel.

For integral coefficients, the linear inversion unitary $\delta_g\mapsto\delta_{g^{-1}}$ turns this left matrix action on columns into right multiplication by $A^*$ on rows.
The adjoint transposes indices as well as inverting group elements.
Integral coefficients are real, so coefficient conjugation causes no further change.
The identity vectors are fixed, which preserves the corresponding positive-square spectral measures.
This identifies the convention relevant to [Luc22-U001](../Luc22/Yin_U001.md#luc22-u001), without identifying all left and right actions term by term.

## The exact characteristic-two input

Theorem 1.2 supplies a finite field $K_2$ of characteristic two, a finitely generated group $H_2$, and scalar finite sums
$$
a_2,b_2\in K_2[H_2],\qquad a_2b_2=1,\qquad b_2a_2\ne1.
$$
The source neither asserts $K_2=\mathbb F_2$ nor assumes that $H_2$ is torsion-free.
An odd-characteristic theorem would not supply this input.

Lemma 2.1, p.3, uses the regular representation of the field on its binary vector space.
With $d=[K_2:\mathbb F_2]$, it gives an injective unital homomorphism
$$
K_2[H_2]\longrightarrow M_d(\mathbb F_2[H_2]).
$$
Coefficientwise extension preserves products because coefficient matrices commute with the formal group symbols.
Coefficient comparison proves injectivity, so the defect remains nonzero.
For the images $X,Y$, one obtains
$$
XY=I_d,\qquad C=I_d-YX\ne0,\qquad
C^2=C,\quad XC=0,\quad CY=0. \tag{2.1}
$$
This step does not need to preserve the involution.
The rational orthogonal projection is constructed separately.

## A separated coefficient becomes a positive trace surplus

Proposition 2.2, pp.3–4, defines
$$
G_D=\left(\bigoplus_{h\in H_2}C_3\right)\rtimes H_2,
$$
where $H_2$ acts by left translation on the coordinate labels.
Choose a coefficient equal to one in a nonzero entry $C_{ij}$.
Left multiplication by its inverse group label gives
$$
h_0^{-1}C_{ij}=1+\sum_{s\in S}s,
\qquad S\subset H_2\setminus\{1\}\text{ finite}. \tag{2.2}
$$
This is an existence argument and does not require a group-word decision procedure.

Let $z_h$ generate the coordinate $C_3$ at $h$, and set
$$
p_h=\frac{1+z_h+z_h^2}{3},\qquad
p=p_1\prod_{s\in S}(1-p_s).
$$
These are commuting orthogonal projection factors.
For $s\in S$, the conjugate $sps^{-1}$ contains $p_s$, while $p$ contains $1-p_s$.
All factors belong to the abelian base group, so
$$
psp=p(sps^{-1})s=0. \tag{2.3}
$$
No disjointness between the original and translated coordinate sets is needed.
Overlaps, inverse pairs in $S$, and finite-order elements of $S$ do not affect this cancellation.

The original labels in $\{1\}\cup S$ are distinct.
The coefficient of the identity therefore factors:
$$
\tau(p)=\frac13\left(\frac23\right)^{|S|}
=:\theta>0. \tag{2.4}
$$
The empty-support case gives $p=p_1$ and $\theta=1/3$.
The odd integer $D=3^{1+|S|}$ clears denominators.

Reduction modulo two is a ring map on $\mathbb Z[1/3][G_D]$.
Equations (2.2)–(2.3) give
$$
\bar p h_0^{-1}C_{ij}\bar p=\bar p.
$$
Choose the row $f$ with entry $\bar p h_0^{-1}$ in position $i$ and the column $w$ with entry $\bar p$ in position $j$.
Thus $fCw=\bar p$.
Then
$$
P=\operatorname{diag}(I_d,p),\qquad
u=\begin{pmatrix}X\\fC\end{pmatrix},\qquad
v=\begin{pmatrix}Y&Cw\end{pmatrix}
$$
satisfy
$$
uv=
\begin{pmatrix}XY&XCw\\fCY&fC^2w\end{pmatrix}
=\operatorname{diag}(I_d,\bar p)=\bar P.
$$
Hence $\tau_{d+1}(P)=d+\theta>d$, although its binary reduction factors through only $d$ columns.
The real trace surplus belongs to $P$, not to its finite-characteristic reduction.

## Lifting the factorization and enforcing integrality

Lemma 3.1, p.5, needs only an idempotent rational matrix $P$ with odd denominator $D$, and a factorization $\bar P=uv$ through $r$ columns.
For $q=2^k$, reduction gives an idempotent $e=P_q$ over $(\mathbb Z/q)[G]$.
Choose arbitrary lifts $u_0,v_0$ of $u,v$, and work in the corner ring with identity $e$:
$$
Z=eu_0v_0e,\qquad W=e-Z.
$$
Modulo two, $Z$ equals $\bar P^3=\bar P$.
Every coefficient of $W$ is even, so $W^k=0$: each coefficient of the product is a finite sum of products divisible by $2^k$.
This uses nilpotence of the even ideal, not of the entire corner ring.

The finite sum
$$
Q=e+W+\cdots+W^{k-1}
$$
satisfies $QZ=ZQ=e$.
Thus $u_q=Qeu_0$ and $v_q=v_0e$ factor $e$ through the same $r$ columns.
For $k=1$, $W=0$ and $Q=e$.
The argument preserves finite support and requires neither orthogonality nor a left inverse of $u$.

For Lemma 3.2, p.6, choose $q=2^k>1$ with $q\equiv1\pmod D$; such a power exists because $D$ is odd.
Let $U,V$ be arbitrary integral lifts of $u_q,v_q$.
Then
$$
A=
\begin{pmatrix}
qI_r&V\\
U&q^{-1}\bigl(UV-P-q(I_m-P)\bigr)
\end{pmatrix}. \tag{3.1}
$$
The expression $P+q(I_m-P)=qI_m+(1-q)P$ is integral and reduces modulo $q$ to $P_q=UV$.
The bottom-right numerator is therefore an integral matrix divisible coefficientwise by $q$.
This proves integrality over $\mathbb Z[G]$, not merely over a localization.

Set
$$
J=-q^{-1}P-(I_m-P),\qquad
B=\operatorname{diag}(qI_r,J).
$$
Orthogonality gives $J^{-1}=-qP-(I_m-P)$.
The lower and upper shears with off-diagonal blocks $xU/q$ and $xV/q$ satisfy the ordered identity
$$
M(x)=L_xBR_x
=\begin{pmatrix}qI_r&xV\\xU&x^2UV/q+J\end{pmatrix}. \tag{3.2}
$$
The product is $UV$ and no noncommuting factors are interchanged.
At $x=1$, this equals $A$, with inverse $R_1^{-1}B^{-1}L_1^{-1}$ in the finite-support rational group ring.
For real $x$, both the matrix and its inverse vary continuously differentiably in operator norm.
The proof does not assume $PU=U$, $VP=V$, or $V=U^*$.

## The tracial logarithmic derivative and exact determinant

Lemma 4.1, pp.6–7, is proved locally.
The identity-coefficient trace is cyclic and bounded by $n$ times the operator norm, so it extends continuously to the norm closure of the represented matrix group ring.
For an invertible $C^1$ path $M$, compactness gives
$$
0<\delta I\le N=M^*M\le cI.
$$
The logarithmic power series for $W=I-N/c$, with $\|W\|\le\rho<1$, and its derivative converge uniformly in norm.
Indeed the derivative of $W^j/j$ has norm at most $\sup\|W'\|\rho^{j-1}$.
The trace can therefore be differentiated term by term.
Cyclicity combines the $j$ derivative terms without assuming that $N$ and $N'$ commute, giving
$$
\frac{d}{dx}\tau(\log N)
=\tau(N^{-1}N')
=2\operatorname{Re}\tau(M'M^{-1}).
$$

Lemma 4.2, p.7, applies the ordered product rule to the shear path:
$$
M'M^{-1}
=L_x'L_x^{-1}
+(L_xB)(R_x'R_x^{-1})(L_xB)^{-1}.
$$
The two shear derivatives have zero diagonal blocks.
Cyclicity removes the conjugation, so the total trace vanishes.
This proves the needed determinant invariance locally rather than relying on a general multiplicativity theorem.

At $x=0$,
$$
B^*B=\operatorname{diag}(q^2I_r,q^{-2}P+I_m-P),\qquad
\log(B^*B)=2\log q\,\operatorname{diag}(I_r,-P).
$$
Proposition 4.3, p.7, consequently obtains
$$
\log\Delta_G(A)=(r-\tau_m(P))\log q. \tag{4.2}
$$
The bounded rational inverse yields
$$
\|T_A^{-1}\|^{-2}I\le T_A^*T_A\le\|T_A\|^2I.
$$
This verifies determinant class and the finite-integral assertion, including the normalization
$$
\int_{(0,\infty)}\log t\,d\mu_A(t)
=\frac{2(r-\tau_m(P))\log q}{r+m}. \tag{4.3}
$$

Section 5, p.8, substitutes $r=d$, $m=d+1$, and $\tau(P)=d+\theta$.
All hypotheses match, so $n=2d+1$ and
$$
\Delta_{G_D}(A)=q^{-\theta}\in(0,1),\qquad
\int_{(0,\infty)}\log t\,d\mu_A(t)
=-\frac{2\theta\log q}{2d+1}. \tag{5.1--5.2}
$$
A finite generating set of $H_2$, together with $z_1$, generates $G_D$ because $z_h=hz_1h^{-1}$.
Finite presentation, torsion-freeness and a decidable word problem are neither proved here nor required.
The group explicitly contains elements of order three.

## Verification limits

The full conditional determinant reduction and its exact companion interface were checked as described above.
Standard bounded-operator functional calculus is retained as foundational mathematics; the special logarithmic derivative and shear invariance were rederived locally.
The external least-prime input is accepted at the precise, narrower scope of Xyl11-U001.

The source's bibliographic ancestry claims concerning Fuglede–Kadison, de la Harpe–Skandalis and wreath-product projection articles were read but their original publications were not re-audited in this unit.
The background comparisons involving Schick and Kammeyer, and the nonsofic consequence via Elek–Szabó, are not adopted here.
They are neither necessary inputs to the construction nor certified by this finding.

The finite prescription has not been executed to print a concrete matrix.
An existence proof does not require that execution, but this audit supplies no computational witness or computed determinant certificate.
At the user's direction, this intake and audit cover the manuscripts and mathematical proof chain; Lean sources are excluded.

This is an initial inspection of the identified artifact, not a carry-forward of an earlier audit.
No source erratum or different revision was used.
Later revisions require comparison of their statements, construction, and dependency interfaces before this assessment is reused.
