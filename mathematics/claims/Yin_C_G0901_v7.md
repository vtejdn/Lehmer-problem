---
author: Yin
---

# Simultaneous local sharpness at the minimum row width

<a id="statement"></a>
## Height compared with the unrestricted minimum at the same width

Let \(P\) be the monic reciprocal minimum of a nontorsion algebraic unit \(\alpha\) of degree \(e\).
At an odd prime \(p\), group its roots by their residues over \(\overline{\mathbb F}_p\), write \(m_C\) for the sizes of the distinct classes, and assume \(p\ge3\max_Cm_C\).
Put \(z=\alpha^p\), \(J_p=\sum_Cm_C^2\), and \(\iota(Y)=Y^{-1}\).
Consider pairs of nonzero integral rows \(U,V\) of degrees at most \(e\), coprime over \(\mathbb Q\), satisfying
\[
            P^2\mid U(X^p)+XV(X^p),\qquad UU^\iota-VV^\iota\ne0 .
\]
Write \(H_{\min}(P,p)\) for the least \(\max(\|U\|_1,\|V\|_1)\) among these pairs, before the coefficient cutoff in the [finite test](Yin_C_G0345_v408.md#statement).
Let \(H_{\rm sharp}(P,p)\) be the corresponding minimum with both equalities
\[
          v_p\!\left(N_{\mathbb Q(z)/\mathbb Q}V(z)\right)
                 =v_p\operatorname{Res}(U,V)=J_p .                     \tag{1}
\]
The [divided-difference span bound](Yin_C_G0901_v4.md#rows) at the [localized prime threshold](Yin_C_G0901_v5.md#local) makes \(e\) the least possible width.
At every such prime both minima are finite and
\[
              H_{\min}(P,p)\ \le\ H_{\rm sharp}(P,p)\
                   \le\ 32\sqrt{e+2}\,H_{\min}(P,p).                    \tag{2}
\]
The exponent in (1) is the sharp lower bound for coprime contact rows of [unrestricted width](Yin_C_G0901_v6.md#statement).
Here the same least possible valuation for both integers is attained at the least possible width, with a bound relative to the best archimedean height.

<a id="tops"></a>
## Integral coordinates from the two leading coefficients

Work temporarily over the ring \(\mathcal O\) of a finite unramified extension of \(\mathbb Q_p\) splitting all root residues.
In a class with residue \(\xi_C\), put \(m=m_C\), let \(\omega\) be its Teichmüller lift, and set \(c_C=\omega^p\).
Use \(Y=c_C(1+pZ)\) in this class, with \(K_C,\mathcal S_C=\mathcal O[Z]/K_C^2\) and \(f_1(Z)\) as in the [doubled local contact algebra](Yin_C_G0901_v6.md#jets).
In particular \(K_C\bmod p=Z^m\), and the reduction of \(f_1\) modulo \(p\) in this algebra is \(E(Z)=\sum_{j=0}^{2m-1}Z^j/j!\).

Put \(T(Y)=\prod_C(Y-c_C)^{m_C}\), a monic degree-\(e\) polynomial with coefficients in \(\mathbb Z_p\).
For each \(j<m_C\), let \(B_{Cj}\) be the polynomial of degree below \(e\) representing \((Y-c_C)^j\) modulo \((Y-c_C)^{m_C}\) and zero modulo every other \((Y-c_D)^{m_D}\).
Distinct centers have unit differences, so these representatives are integral over \(\mathcal O\) by the Chinese remainder theorem over that ring.
For a row \(W\) of degree at most \(e\), its coefficient \(w\) at \(Y^e\) and its lower \(m_C\) Taylor coefficients at each center determine it uniquely in this basis.
The [necessary Taylor divisibilities](Yin_C_G0901_v6.md#jets) for an integral double-contact pair therefore give, for each of its two rows, the expression
\[
       W(Y)=w T(Y)+
           \sum_C\sum_{j=0}^{m_C-1}p^{m_C-j}a_{Cj}B_{Cj}(Y),
                       \qquad a_{Cj}\in\mathcal O .                     \tag{3}
\]
Write the two top coefficients as \(u,v\).

Conversely fix arbitrary \(u,v\in\mathcal O\) and solve for all lower coordinates in (3).
In the class \(C\), put \(W_C(Z)=p^{-m}W(c_C(1+pZ))\).
This has integral coefficients: all terms in the original Taylor expansion of \(W\) of order less than \(m\) have the divisibility in (3), and terms of higher order carry \(p^m\).
On reduction its polynomial is
\[
 \overline W_C(Z)=g_C\bar w Z^m+\sum_{j<m}\bar c_C^{\,j}\bar a_{Cj} Z^j,
 \qquad
       g_C=\bar c_C^{\,m}\prod_{D\ne C}(\bar c_C-\bar c_D)^{m_D}\ne0 .  \tag{4}
\]
For a lower term indexed by another class, \(B_{Dj}\) vanishes to order \(m\) at \(c_C\), and its prefactor contains at least one additional \(p\).
For a term indexed by \(C\), the difference \(B_{Cj}-(Y-c_C)^j\) also vanishes to order \(m\) and is multiplied by \(p^{m-j}\).

The normalized value and derivative equations are
\[
                    U_C+\omega f_1 V_C=0\quad\text{in }\mathcal S_C
                    \qquad\text{for each }C .
\]
They are equivalent over the fraction field to the \(e\) pairs of Hermite conditions at the distinct powered nodes and thus to the divisibility by \(P^2\).
The coefficient matrix on the \(2e\) lower coordinates of the two rows has, on reduction, one diagonal block per class by (4).
Each block is invertible: up to unit scalars its columns are \(Z^j,E Z^j\) for \(0\le j<m\) modulo \(Z^{2m}\), the [unit basis](Yin_C_G0901_v6.md#jets).
Thus the integral equations admit exactly one solution over \(\mathcal O\) for every pair of top coefficients.
If \(u,v\in\mathbb Z_p\), uniqueness and the permutation of the centers and equations by unramified Galois automorphisms descend the original two rows to \(\mathbb Z_p[Y]\).
This gives an isomorphism of the full \(\mathbb Z_p\) contact lattice with \(\mathbb Z_p^2\) by the top coefficients.
It is an isomorphism on integral rows before imposing coprimality or the norm, resultant or reflection conditions.
In particular a pair of rows is jointly \(p\)-primitive precisely when its top vector has nonzero reduction, and its reductions are \(\bar U=\bar u\bar T,\ \bar V=\bar v\bar T\).

<a id="lines"></a>
## Residue lines that determine sharpness

For a jointly \(p\)-primitive pair denote its top line by \([\bar u:\bar v]\).
In a class \(C\), the reduced local pair solves \(\overline U_C+\bar\omega E\overline V_C=0\bmod Z^{2m}\).
The bad condition \(\overline V_C(0)=0\) specifies exactly one line of top vectors over the residue field, since the constants are then both zero.
Indeed after division by \(Z\) the rows of degrees at most \(m-1\) have contact modulo \(Z^{2m-1}\), a one-dimensional kernel by the factorial basis proof using \(m\) ordinary columns and \(m-1\) exponential columns.
Neither axis is bad: if also one leading coefficient vanishes, the reduced system after division has row degrees at most \(m-1,m-2\) in some order, forcing both rows to vanish by that basis or the corresponding basis for \(E^{-1}\).
Here \(E^{-1}=E(-Z)\bmod Z^{2m}\) since \(2m-1<p\).
For \(m=1\) the same statement uses just the one constant equation after division.
The reduced pairs with the bad constant term indeed form a line, as the ordinary rank-\(2m\) system before division has its full two-dimensional space parametrized by the top coefficients and this is one additional linear equation.

More explicitly the bad line is
\[
                         [(-1)^m\xi_C:1].
\]
For a nonzero pair \((U_1,V_1)\) after dividing out \(Z\), both constants are nonzero; simultaneous zero constants would allow another division and a square nonsingular system of order \(2m-2\) (or zero rows for \(m=1\)).
Both top coefficients in degree \(m-1\) are nonzero by the axis test.
The pair \((\bar\omega^{\,2} V_1(-Z),U_1(-Z))\) satisfies the same equation modulo \(Z^{2m-1}\), so is proportional to \((U_1,V_1)\).
Comparison at zero gives the proportionality factor \(-\bar\omega\).
Hence \(U_1(Z)=-\bar\omega V_1(-Z)\), giving the displayed ratio of leading coefficients because the same unit \(g_C\) occurs on both sides of (4).

At every powered node in \(C\), \(Z\) has positive valuation.
Thus the valuation of \(V\) there is \(m\) exactly when \(\overline V_C(0)\ne0\), and is larger at every such node on the bad line.
This gives the exact criterion for norm equality in (1).
If the top line avoids all bad lines, both local constants are nonzero.
The reduced local polynomials have no common nonconstant factor: a common factor would be a unit at zero, so canceling it would give rows of degrees below \(m\) with contact modulo \(Z^{2m}\), contrary to the basis theorem.
At least one top coefficient is a unit, say \(u\).
Then \(U\) has \(p\)-unit leading coefficient, degree \(e\), and exactly \(m_C\) roots at each residue \(\bar c_C\) counting multiplicities, by \(\bar U=\bar u\bar T\).
All these roots lie in \(v_p(Y-c_C)\ge1\): otherwise the degree-\(m_C\) Taylor term has strictly lowest valuation, using (3) and its unit Taylor coefficient in degree \(m_C\) from (4).
At any such root, coprimality of the reduced polynomials in the normalized variable forces \(V\) to have valuation exactly \(m_C\).
The product formula for the resultant gives \(v_p\operatorname{Res}(U,V)=J_p\).
If \(v\) is a unit instead, interchange the rows for this product formula, retaining the already proved norm equality for \(V\).
These arguments ensure a nonzero resultant, coprimality over the fraction field and nonzero values at the powered nodes.
Finally the reflected determinant is nonzero whenever \(\bar u^2\ne\bar v^2\), by the reduction \((\bar u^2-\bar v^2)\bar T\bar T^\iota\).
In particular the top axis \([1:0]\) satisfies every condition at every prime in the statement.

<a id="height"></a>
## Integral representatives with small archimedean cost

Let \(\Lambda\) be the integer lattice of all width-\(e\) contact pairs.
It is the kernel of the integral linear map taking the remainder of the graph modulo \(P^2\).
A Smith normal form, or a basis of the saturated integer kernel, identifies \(\Lambda\otimes\mathbb Z_p\) with the full local integral kernel just calculated.
Reciprocity of \(P\) makes \(\tau(U,V)=(V^*,U^*)\), with \(A^*(Y)=Y^eA(1/Y)\), an involution of \(\Lambda\) by reversing the graph about degree \(pe+1\).
On the reduced top vectors it interchanges the two entries up to the unit \(\bar T(0)\), by the end of the [integral coordinate calculation](#tops).
Because \(P\) is reciprocal and its powered conjugates are distinct, \(Q\) is monic reciprocal with constant coefficient one and \(\bar T=\bar Q\).
Thus \(\bar T(0)=1\).
At the odd prime \(p\) the two eigenspaces have dimension one on reduction.
The integral local idempotents \((1\pm\tau)/2\) split the local lattice into rank-one summands.
Each global rational eigenline has a primitive integral generator, denoted
\[
                       W_+=(A,A^*),\qquad W_-=(D,-D^*).
\]
Primitivity makes each generator nonzero on reduction, so they generate their respective summands over \(\mathbb Z_p\) and give a basis of the local top plane.
This uses no assumption that they form an integral basis at 2.

There exist admissible integral rows: integer combinations of \(W_+,W_-\) reach every residue top vector, and the line \([1:0]\) supplies sharp rows by the [line criterion](#lines).
For any integral pair of height \(H\) with nonzero reflected determinant, its two projections under \(1+\tau\) and \(1-\tau\) are nonzero integer multiples of the primitive generators.
Indeed an eigenpair has zero reflected determinant.
The one-norm of each projected first row is at most \(2H\), whence \(\|A\|_1,\|D\|_1\le2H_{\min}\) by taking a minimum admissible pair.

If \(p\le64e\), put \(K=\lfloor\sqrt p\rfloor\).
The \((K+1)^2>p\) choices \(0\le a,b\le K\) for \(aW_++bW_-\) give two identical second top coordinates modulo \(p\).
Subtracting the choices yields coefficients of absolute value at most \(K<p\), not both zero modulo \(p\).
Their first top coordinate is nonzero by the residue basis, giving the sharp axis \([1:0]\).
The height is at most \(4K H_{\min}\).

If \(p>64e\), put \(K=\lceil3\sqrt{e+2}\rceil\), so \(K^2<p\) for \(e\ge2\).
Among \(1\le a,b\le K\) at least \(K^2/4\) pairs are coprime, by deleting at most \(K^2\sum_{d\ge2}d^{-2}\le3K^2/4\) pairs with a common divisor (bound the tail after \(d=2\) by \(\int_2^\infty x^{-2}\,dx\)).
They represent distinct projective lines modulo \(p\): a vanishing cross determinant has absolute value below \(p\) and must vanish as an integer, which gives identical positive primitive pairs.
The residue top basis preserves their distinctness.
At most \(e\) lines over \(\mathbb F_p\) are forbidden by the local constant terms and at most two more by \(\bar u=\pm\bar v\).
Since \(K^2/4>e+2\), some pair supplies all desired properties and height at most \(4K H_{\min}\).
Both estimates yield (2).

<a id="consequences"></a>
## What the local equalities contribute to a height bound

For a fixed seed the difference between the two normalized log costs is at most \(\log(32\sqrt{e+2})/p\).
Thus the [fixed-seed cost at width \(e\)](Yin_C_G0345_v413.md#statement) for each Salem input, the [independent inverse-pair formula](Yin_C_G0345_v414.md#statement), and the [progression-wise rates](Yin_C_G0345_v415.md#one) at sufficiently large primes all keep their existing exponential rates upon requiring the two exact divisibilities.
In particular for a Salem number \(\rho\) of degree \(e\) this rate is \(e\log\rho\).
A strict exponential separation from a coefficient cutoff survives the additional conditions; (2) alone does not decide an exact minimum at a finite prime or a cutoff without a strict margin.

For varying seeds, \(\log(H_{\rm sharp}/H_{\min})/p\to0\) whenever \(\log(e+2)=o(p)\) through eligible primes.
This controls the cost of demanding local equality and leaves the size of \(H_{\min}\) to the ordinary coefficient problem.
At widths \(e+k\) with \(k>0\), the contact lattice can have additional directions and the two top coefficients no longer determine its elements.
The [small-height estimates at excess width](Yin_C_G0901_v1.md#width) and the [denominator description for signed rows](Yin_C_G0345_v464.md#statement) have different hypotheses from the width-\(e\) comparison above.
A uniform lower bound for the positive input measures remains open.

## Assessment history

### Decision minimum-width-valuation-cost

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:52 |
| status | proved |
| reason | The local top coordinates give explicit exceptional lines and the signed generators yield integral representatives of bounded relative height. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous least norm and resultant valuations at the minimum width under the stated local condition, with the stated height factor. |
| argument | [tops](#tops) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [lines](#lines) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [height](#height) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [consequences](#consequences) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [Input](Yin_C_G0901_v4.md#rows) | The minimum possible row span. |
| dependency | [Input](Yin_C_G0901_v5.md#local) | The localized prime threshold. |
| dependency | [Input](Yin_C_G0901_v6.md#jets) | The doubled local contact algebra and Taylor divisibilities. |
| dependency | [Input](Yin_C_G0901_v6.md#statement) | Both valuation lower bounds. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1053.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-minimum-width-valuation-cost)
