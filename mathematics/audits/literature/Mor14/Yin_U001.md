---
author: Yin
---

# Mor14-U001: two-generator semigroup polynomials and alternating coefficients

<a id="mor14-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Moree, MPIM Preprint Series 2013 (45), MPIM 13-45; [retained original PDF](../../../literature/pdf/Mor14--mpim-2013-45.pdf), with acquisition and edition facts. The canonical work key Mor14 uses the verified 2014 journal-publication year; the journal text is not this inspection's input.

Passages: Section 1 numerical-semigroup definition, printed p. 1/PDF p. 5; Hilbert series, semigroup polynomial and Theorem 1, printed p. 2/PDF p. 6; equation (10), printed p. 4/PDF p. 8; Theorem 4, Corollaries 2--3, Apéry-set definition and complete first proof of Theorem 4, printed p. 5/PDF p. 9.

Inspection: On 2026-10-26, semigroup_source_preparation directly checked these definitions, exact statements, hypotheses and the complete first Apéry proof against the acquired original and rendered pages. This is source inspection for the D48 attribution follow-up, not an independent project proof review. The second proof, the remaining results, cited predecessors and journal-version comparison were not audited.


<a id="numerical-semigroup-and-semigroup-polynomial"></a>
## Numerical semigroups and their polynomials

**Definition.**
For positive integers \(a_1,\ldots,a_m\), let
\[
S(a_1,\ldots,a_m)=\left\{\sum_{i=1}^m a_i u_i:u_i\in\mathbb Z_{\ge0}\right\}.
\]
This additive semigroup contains zero and is numerical when \(\mathbb Z_{\ge0}\setminus S\) is finite.
For a numerical semigroup \(S\), its Hilbert series and semigroup polynomial are
\[
H_S(x)=\sum_{s\in S}x^s\in\mathbb Z[[x]],\qquad P_S(x)=(1-x)H_S(x)\in\mathbb Z[x].
\]
Each semigroup element occurs once in \(H_S\), regardless of how many expressions it has in the chosen generators.
The series is formal; no analytic convergence assumption is used.
Its polynomial character follows directly from the finite complement:
\[
P_S(x)=1-(1-x)\sum_{g\in\mathbb Z_{\ge0}\setminus S}x^g.
\]
These are the Section 1 conventions at printed pp. 1--2/PDF pp. 5--6.

<a id="apery-set"></a>
## Apéry set

**Definition.**
For a numerical semigroup \(S\) and a nonzero \(m\in S\), Moree defines
\[
\operatorname{Ap}(S;m)=\{s\in S:s-m\notin S\}.
\]
Here \(m\) is positive and membership in \(S\subseteq\mathbb Z_{\ge0}\) excludes negative integers.
The definition occurs in the first proof of Theorem 4 at printed p. 5/PDF p. 9.
The proof uses that this set consists of the least element of \(S\) in each residue class modulo \(m\), and that every \(s\in S\) has a unique expression \(w+im\), with \(w\in\operatorname{Ap}(S;m)\) and \(i\ge0\).
These existence and uniqueness facts are part of the inspected proof mechanism, rather than extra defining conditions.

<a id="two-generator-formula-and-alternation"></a>
## Checked formula and alternating-support mechanism

For all coprime integers \(p,q>1\), Theorem 1 states
\[
P_{S(p,q)}(x)
 =\frac{(x^{pq}-1)(x-1)}{(x^p-1)(x^q-1)}.
\]
Equation (10) denotes the right-hand side by \(Q_{\{p,q\}}(x)\), the binary inclusion-exclusion polynomial.
Theorem 4 restates the equality in that notation.
Its first proof identifies
\[
\operatorname{Ap}(S(p,q);p)=\{0,q,\ldots,(p-1)q\}
\]
and obtains
\[
H_{S(p,q)}(x)
 =\frac{\sum_{b=0}^{p-1}x^{bq}}{1-x^p}
 =\frac{1-x^{pq}}{(1-x^p)(1-x^q)}.
\]
The residue classes are distinct because \(\gcd(p,q)=1\); reducing the coefficient of \(q\) modulo \(p\) supplies the nonnegative normal form.
This verifies the whole first proof using the definitions above.

For \(k\ge0\), Corollary 2 describes the coefficient as
\[
[x^k]P_{S(p,q)}=\mathbf1_{S(p,q)}(k)-\mathbf1_{S(p,q)}(k-1),
\]
where \(\mathbf1_{S(p,q)}(-1)=0\).
Corollary 3 states that its nonzero coefficients alternate between \(1\) and \(-1\).
The checked explanation is the successive change of a zero-or-one membership sequence; after a positive change another positive change requires an intervening negative change, and conversely.
The constant coefficient is \(1\), and cofiniteness makes the differences eventually zero.
Thus the coefficients belong to \(\{-1,0,1\}\), with alternating signs on their nonzero support.

<a id="d48-attribution-and-limits"></a>
## Attribution, specialization and limits

The [D_G8 semigroup screen](../../../drafts/Yin_D_G0008.md#cyclotomic-semigroup-source-multiplicity-screen) uses \(x=z\), \(p=5\) and \(q=q_{\rm cyc}=2^r\), \(r\ge1\).
These satisfy \(p,q>1\) and \(\gcd(p,q)=1\), so its displayed \(A_{\rm cyc}\) is exactly \(P_{S(5,q_{\rm cyc})}\), and the normal form and alternating-support mechanism are the direct specialization of the checked source.
The formula and alternation are accepted at this precise scope as established external results; their present role is attribution for the self-contained calculation retained in D48.
They add no premise or alteration to fixed [C_G807](../../../claims/Yin_C_G0807_v1.md).

Moree calls Theorem 1 a folklore result.
The distinct-prime identification \(P_{S(p,q)}=\Phi_{pq}\) is separately stated in equation (5), with an attribution to Carlitz (1966); this record does not independently verify that historical priority.
For \(r>1\), \(q_{\rm cyc}\) is composite, so equation (5) is not the applicable specialization.
D48 instead uses its explicit cyclotomic ratio \(F_5(z^{q_{\rm cyc}})/F_5(z)\).

The source gives no match to the current project's complete binary source or its prescribed multiplicities, noncyclotomic factors, degree budget or sign-completion constraints.
The two explicit dyadic failures and their exact qualifications remain in D48.
No full-paper audit, independent proof review, formal verification or equivalence of preprint and journal text is asserted.
