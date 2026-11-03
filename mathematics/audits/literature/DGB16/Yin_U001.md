---
author: Yin
---

<a id="dgb16-u001"></a>
# DGB16-U001: algebraic entropy, rationalization and finite-flow reductions

## Source and inspection

[Source and edition notes](readme.md).

Source edition: DGB16, [retained published PDF](../../../literature/pdf/DGB16.pdf), *Advances in Mathematics* 298 (2016), 612--653, DOI 10.1016/j.aim.2016.04.020; 42 PDF pages. The entry-key correction from DB16 to DGB16 does not change the artifact.

Passages: Sections 2--4 in full, printed pp.620--635 (PDF pp.9--24), and introductory definitions/conventions on pp.613--616,619--620. In particular: Lemma 2.2, Proposition 2.8, Lemmas 3.3/3.5, Proposition 3.7, Corollaries 3.9/3.10, Lemmas 4.3/4.4/4.6 and Proposition 4.7.

Inspection: 2026-10-06, human author Yin, prepared by an assigned AI source-review agent. Direct reading of the complete assigned passages and self-check of this record; no independent human review or independent project-proof review is asserted. Layout extraction was checked against rendered PDF pp.12,15--19,22--23 for the formulas and findings below.


## Assessment and coverage

**Audited within scope** for the basic entropy properties, torsion-free rationalization and equality of entropy on essential subgroups, and the finite-flow/support reduction in Proposition 4.7, with the retained external interfaces below.
The extra conclusion that the essential torsion quotient has zero entropy in Corollary 3.6 retains an unverified primary-source interface to [16, Proposition 1.18], explicitly separated below.
Proof arguments printed in Sections 2--4 were examined; the precise corrections in the findings section are part of the reusable interface.

**Questioned at literal scope** for the paragraph after Example 3.1, which gives an insufficient definition of integral endomorphism and then makes a false zero-entropy assertion; the unrestricted purification definition on p.628; and the literal missing hypotheses/incorrect estimates itemized below.
These defects do not invalidate the reviewed main reduction chain when the stated repairs are applied.
Fact 2.4 and the externally reported results in Remark 2.11 were read, but their cited original proofs were not audited.

This unit supplies foundational interfaces for [DGB16-U002](Yin_U002.md#dgb16-u002).
It selects no project Task, proves no new project Claim, and makes no formal-verification claim.

<a id="entropy-trajectory"></a>
## Finite trajectories and algebraic entropy

All groups here are discrete abelian groups, written additively, and all endomorphisms are group endomorphisms.
Write $\mathbb N=\{0,1,\ldots\}$ and $[G]^{<\omega}$ for **nonempty** finite subsets of $G$.
The logarithm is natural.
For $\phi\in\operatorname{End}(G)$, $F\in[G]^{<\omega}$ and $n\ge1$,

$$
T_n(\phi,F)=F+\phi(F)+\cdots+\phi^{n-1}(F),\qquad
H(\phi,F)=\lim_{n\to\infty}\frac{\log|T_n(\phi,F)|}{n},
$$

$$
h(\phi)=\sup_{F\in[G]^{<\omega}}H(\phi,F)\in[0,\infty].
$$

The limit exists: $T_{n+m}=T_n+\phi^n(T_m)$ implies subadditivity of $\log|T_n|$, and Fekete's lemma gives the limit as the infimum of the quotients.
Each local $H(\phi,F)$ is finite, bounded above by $\log|F|$.
The supremum $h$ may be infinite.
Inclusion of finite sets makes $H$ monotone; any cofinal collection of finite sets computes $h$.
In particular, one may require $0\in F$, or enlarge further to symmetric finite sets.
These are source-definition conversions, not changes to the entropy.

The older entropy $\operatorname{ent}$ takes the same supremum over finite **subgroups**.
Thus

$$
\operatorname{ent}(\phi)=\operatorname{ent}(\phi|_{t(G)})
=h(\phi|_{t(G)}),
$$

since every finite subset of a torsion abelian group is contained in a finite subgroup.
In general $\operatorname{ent}(\phi)$ need not equal $h(\phi)$: multiplication by $k>1$ on $\mathbb Z$ has $h=\log k$, whereas $\operatorname{ent}=0$.

For a finite **subgroup** $F$, Fact 2.4 reports, with $N=\sum_{j\ge0}\phi^j(F)$,

$$
H(\phi,F)=\log|N/\phi(N)|-\log|\ker\phi\cap N|.
$$

Both groups whose orders occur are finite.
The kernel term must be retained unless injectivity on $N$ is known.
This is a read external formula, not a proof-audited input here; the source attributes its corrected general form to [9, Lemma 4.1].
None of this unit's reduction proofs needs that formula.

## Basic properties and inspected proof mechanisms

1. **Monotonicity (Lemma 2.7).**
   For a $\phi$-invariant subgroup $H\le G$ and the induced $\bar\phi:G/H\to G/H$,
   $h(\phi)\ge\max\{h(\phi|_H),h(\bar\phi)\}$.
   For the quotient direction lift an arbitrary finite subset of $G/H$ to a finite subset of $G$; the quotient map sends its trajectories onto the quotient trajectories.
   No injectivity assumption is needed.
2. **Conjugacy (Proposition 2.8(a)).**
   If $\xi:G\to G'$ is an isomorphism and $\eta\xi=\xi\phi$, then $H(\eta,\xi F)=H(\phi,F)$ and $h(\eta)=h(\phi)$.
   The trajectory bijection proves the assertion, using the correctly typed identity $\eta^j\xi=\xi\phi^j$.
3. **Logarithmic law (Proposition 2.8(b)).**
   $h(\phi^k)=k h(\phi)$ for positive integers $k$.
   For automorphisms, $h(\phi^{-1})=h(\phi)$ and therefore $h(\phi^k)=|k|h(\phi)$ for nonzero integers $k$; the $k=0$ case is separately $h(\mathrm{id})=0$.
   One bound uses $T_n(\phi^k,F)\subseteq T_{kn-k+1}(\phi,F)$ when $0\in F$; the other uses $T_n(\phi^k,T_k(\phi,F))=T_{kn}(\phi,F)$.
   Inverse trajectories are images under the automorphism $\phi^{-n+1}$, hence have the same cardinality.
   Also $h(-\phi)=h(\phi)$, for example by squaring and applying the law.
4. **Directed unions (Proposition 2.8(c)).**
   If $G=\bigcup_iG_i$ is a directed union of invariant subgroups, then $h(\phi)=\sup_i h(\phi|_{G_i})$, because every finite set lies in one $G_i$.
   This is the stated direct-limit-of-subgroups interface; no arbitrary noninjective direct-limit extension is claimed.
5. **Finite products (Proposition 2.8(d)).**
   For $\phi=\phi_1\times\phi_2$, product trajectories give $H(\phi,F_1\times F_2)=H(\phi_1,F_1)+H(\phi_2,F_2)$ and then $h(\phi)=h(\phi_1)+h(\phi_2)$.
   Product finite sets are cofinal.
   Extended nonnegative addition entails no subtraction of infinities.
6. **Hyperkernel (Proposition 2.6).**
   $\ker_\infty\phi=\bigcup_{n\ge1}\ker\phi^n$ is invariant, its restriction has zero entropy, and the induced map on $G/\ker_\infty\phi$ is injective.
   Every finite subset of the hyperkernel is killed by one common iterate, so its trajectories stabilize after adjoining zero.
   Equality of the full entropy with the quotient entropy is not proved by this proposition alone.
7. **Bernoulli shifts (Example 2.10).**
   On $K^{(\mathbb N)}$, $\beta_K(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)$ has $h(\beta_K)=\log|K|$, with value $\infty$ for infinite $K$.
   The source retains the finite case from [16].
   A direct check is also available: the subgroup in coordinate zero has $n$-trajectory cardinality $|K|^n$, and every finite subset is supported in finitely many coordinates, giving the reverse exponential bound when $K$ is finite.
   For $K=\mathbb Z$, quotients modulo arbitrary primes give unbounded lower bounds; infinite torsion groups contain arbitrarily large finite subgroups, and nontorsion groups contain $\mathbb Z$.

The identity/zero endomorphism examples use polynomial/constant growth.
The elementary computations for integer multiplication, the shear, and rational multiplication were inspected; the corrected bounds are retained below.

<a id="flow-module"></a>
## Invariant generation and the flow-module correspondence

Define

$$
V(\phi,F)=\langle\phi^j(F):j\ge0\rangle
=\sum_{g\in F}V(\phi,g).
$$

It is the smallest invariant subgroup containing $F$.
The group is **finitely $\phi$-generated** if $G=V(\phi,F)$ for one finite nonempty $F$ (Definition 2.1).
A flow is a pair $(G,\phi)$; a morphism $u:(G,\phi)\to(H,\psi)$ obeys $u\phi=\psi u$.
Let $G_\phi$ be the $\mathbb Z[t]$-module with $t\cdot g=\phi(g)$.
Sending a module $M$ back to $(M,\mu_t)$ provides the inverse correspondence.
Thus finite generation of the flow means finite generation of $G_\phi$ as a module, **not** finite generation of the underlying abelian group (Section 4, Definition 4.2).

Since $\mathbb Z[t]$ is Noetherian, invariant subgroups and quotients of a finitely generated flow are finitely generated flows.
Such underlying groups are countable.
Applying this to $t(G)$ shows that it is generated by a finite set of torsion elements and their iterates, so some positive integer $m$ annihilates all of $t(G)$.
The bounded pure-subgroup splitting theorem then gives an abelian-group decomposition $G\cong K\oplus t(G)$ with $K$ torsion-free (Lemma 4.3).
**The complement $K$ is not asserted to be $\phi$-invariant.**
The splitting theorem is a retained standard external input, not a proof recursively reviewed here.

## Infinite-rank cyclic trajectories

Lemma 3.3 states that, for arbitrary abelian $G$, infinite free rank of $V(\phi,g)$ forces

$$
V(\phi,g)\cong\mathbb Z[t],\qquad
h(\phi|_{V(\phi,g)})=h(\phi)=h(\bar\phi_{G/t(G)})=\infty.
$$

The proof first passes to the torsion-free quotient of $V(\phi,g)$.
Any nonzero integer relation among successive iterates would become a finite recurrence over $\mathbb Q$, forcing finite rational rank.
Thus all iterates are integrally independent in the quotient, and a torsion element represented by their finite linear combination must have all coefficients zero.
The resulting restriction is the right shift on $\mathbb Z^{(\mathbb N)}$; its image in $G/t(G)$ remains injective because its intersection with $t(G)$ is zero.

For a torsion-free, finitely generated flow, finite rank is equivalent to finite entropy (Corollary 3.4(a)).
The finite-rank direction uses the Algebraic Yuzvinski Formula on the rational hull; the reverse direction applies Lemma 3.3 to each of finitely many module generators.
For any nonzero $z\in V(\phi,g)$ of infinite rank, the cyclic submodule generated by $z$ again has infinite rank: under $V(\phi,g)\cong\mathbb Z[t]$, it is the nonzero principal ideal generated by the polynomial representing $z$.
This checks the compressed step in Corollary 3.4(b).

With the necessary qualification that $H$ is **$\phi$-invariant**, Lemma 3.5 gives the Addition Theorem whenever some cyclic trajectory has infinite rank.
If $H\cap V(\phi,g)\ne0$, a nonzero cyclic submodule therein has infinite entropy, so $h(\phi|_H)=\infty$.
Otherwise the cyclic trajectory embeds equivariantly into $G/H$, whose entropy is infinite.
In either case the equality is an equality of nonnegative extended numbers.
The literal unrestricted word “subgroup” in the source is not reusable; see finding F2.

<a id="pure-essential-hull"></a>
## Rational hull, purity and essential subgroups

For torsion-free $G$, its divisible hull is $D(G)=\mathbb Q\otimes_{\mathbb Z}G$, and $\phi$ extends uniquely to a $\mathbb Q$-linear $\widetilde\phi$.
Every finite $F\subset D(G)$ has a common positive denominator $m$ with $mF\subset G$.
Multiplication by $m$ is an automorphism of $D(G)$ commuting with $\widetilde\phi$, whence

$$
H(\widetilde\phi,F)=H(\widetilde\phi,mF)=H(\phi,mF),
\qquad h(\widetilde\phi)=h(\phi).
$$

This proves Proposition 3.7 in full generality of torsion-free groups, with no finite-rank assumption.
The torsion-free assumption is essential; the source's shift on $\mathbb Z(2)^{(\mathbb N)}$ and its divisible-hull extension have respective entropies $\log2$ and $\infty$.

A subgroup $H$ is **pure** if $H\cap mG=mH$ for all integers $m$; it is **essential** if every nonzero cyclic subgroup meets $H$ nontrivially.
For torsion-free $G$, these are equivalent respectively to $G/H$ being torsion-free and torsion.
In this torsion-free setting the purification is

$$
H_* =\{x\in G:\text{some }m\ge1\text{ has }mx\in H\},
$$

the smallest pure subgroup containing $H$.
This last definition is deliberately restricted: the source's broader wording is false, as shown in F3.
If $H$ is invariant, so is $H_*$, because $m\phi(x)=\phi(mx)$.
A divisible subgroup is pure; in a divisible ambient group, a pure subgroup is divisible (Lemma 3.8).

If $H\le G$ is essential and invariant with $G$ torsion-free, then $D(H)=D(G)$, so Proposition 3.7 gives $h(\phi|_H)=h(\phi)$.
If this value is finite, Corollary 3.6 gives $h(\bar\phi)=0$; if infinite, the Addition Theorem follows without requiring quotient entropy to vanish.
The proof of Corollary 3.6 checks the induced map on every $(G/H)[p]$: lift a point to $x\in G$, use finite rational rank of $V(\phi,x)$ to obtain an integer recurrence, and divide the common power of $p$ from its coefficients using torsion-freeness.
Modulo $H$ the recurrence is nonzero over $\mathbb F_p$, giving a finite orbit span.
The final passage from all $p$-socles to zero entropy of the torsion quotient retains [16, Proposition 1.18] as an external interface.

Consequently $h(\phi|_H)=h(\phi|_{H_*})$ (Corollary 3.9).
If $H$ is pure and invariant in torsion-free $G$, then $D(H)\cap G=H$, and $G/H$ embeds as an essential subgroup of $D(G)/D(H)$.
Applying rationalization or essential-subgroup invariance to all three terms gives

$$
\operatorname{AT}_h(G,\phi,H)
\iff\operatorname{AT}_h(D(G),\widetilde\phi,D(H))
$$

(Corollary 3.10).
Here $\operatorname{AT}_h$ means $h(\phi)=h(\phi|_H)+h(\bar\phi)$ for an invariant subgroup; it never denotes a quotient action for a noninvariant subgroup.

<a id="entropy-support"></a>
## Countable entropy supports and the simultaneous reduction

Let $\mathcal F(G,\phi)=\{V(\phi,F):F\in[G]^{<\omega}\}$.
It is directed by sums and exhausts $G$.
Therefore

$$
h(\phi)=\sup_{N\in\mathcal F(G,\phi)}h(\phi|_N).
$$

An **entropy support** is a countable invariant subgroup $S\le G$ such that $h(\phi|_S)=h(\phi)$ (Definition 4.5).
Such a subgroup exists (Lemma 4.6): choose finite sets $F_n$ whose local entropies approach the supremum, unbounded if the supremum is infinite, and set $S=\sum_n V(\phi,F_n)$.
The upper bound follows by monotonicity and the lower bound by these chosen finite sets.
The zero-entropy case allows $S=0$.
This does **not** say one finite set realizes the entropy, and the support is generally not unique or finitely generated as a flow.

For invariant $H\le G$, let $\pi:G\to G/H$.
Proposition 4.7 checks the following stronger simultaneous form:

- $\mathcal F(H,\phi|_H)=\{N\cap H:N\in\mathcal F(G,\phi)\}$, using Noetherianity for the nontrivial containment; $\mathcal F(G/H,\bar\phi)=\{\pi(N):N\in\mathcal F(G,\phi)\}$, by finite lifting.
- One can choose a single increasing sequence $L_n\in\mathcal F(G,\phi)$ with $h(\phi|_{L_n})\to h(\phi)$, $h(\phi|_{L_n\cap H})\to h(\phi|_H)$, and $h(\bar\phi|_{\pi(L_n)})\to h(\bar\phi)$.
- To obtain this sequence, enlarge an entropy support of $G$ by an entropy support of $H$ and invariant trajectories of countably many lifts of a support of $G/H$.
  The resulting $S$ is still countable and preserves all three entropies.
  Enumerating $S$ and taking modules generated by initial finite sets yields the required cofinal chains in $S$, $S\cap H$ and $\pi(S)$.
- If the Addition Theorem holds for every $N\in\mathcal F(G,\phi)$ and $N\cap H$, apply it along this one sequence.
  Equivariant $N/(N\cap H)\cong\pi(N)$ and monotone limits of nonnegative numbers give the global equality, including infinite limits.
- It suffices to check such $N$ of finite free rank.
  If a cyclic trajectory has infinite rank, the corrected Lemma 3.5 applies immediately.
  Otherwise each finite sum of cyclic trajectories has finite rank, so the previous reduction applies.

The simultaneous chain is important: taking unrelated suprema of two summands without this directedness argument would not establish their required equality.
Equation (4.6) should be read via the equivariant isomorphism $N/(N\cap H)\cong\pi(N)$; the quotient action is not a literal restriction of the map on $G/H$ to a different underlying quotient set.

## Retained dependencies and unchecked scope

| Input | Exact use and inspection boundary |
| --- | --- |
| Fekete subadditive lemma | Lemma 2.2: a nonnegative subadditive sequence has normalized limit equal to its infimum. The trajectory inequality and all hypotheses were checked; the historical proof in reference [21] was not reread. |
| Algebraic Yuzvinski Formula | Theorem 1.2, pp.615--616, gives $h(\psi)=m(\psi)$ for all $\psi\in\operatorname{End}(\mathbb Q^n)$, including noninvertible maps. Used in Corollary 3.4 solely for finiteness at finite rank. Primary-source statement/version and normalization are retained in [GBV15-U001](../GBV15/Yin_U001.md#gbv15-u001); its full original proof is outside this review. |
| Torsion $p$-socle zero-entropy criterion | Source [16, Proposition 1.18], invoked in Corollary 3.6: zero entropy on every invariant $T[p]$ implies zero entropy on the torsion group $T$. The local reduction to finite orbit spans was checked. The exact external proposition was not accessed in this run; its statement is retained as the identified source-reported interface, not independently primary-verified. |
| Noetherianity and bounded splitting | Noetherianity of $\mathbb Z[t]$ gives invariant-subgroup finite generation. The standard theorem that a bounded pure subgroup of an abelian group splits, cited as Kulikov in [22, Section 27.5], is applied to $t(G)$, which is pure because $G/t(G)$ is torsion-free. Its hypotheses were checked; the original book proof was not reviewed. |
| External reports not needed for this chain | The finite-subgroup entropy formula of Fact 2.4, generalized-shift calculations and Pinsker/recurrence results in Remark 2.11 were read as reports. Their original proofs and a whole-source errata history were not audited. |

The source-reported $p$-socle criterion is a precise retained dependency of the finite-entropy essential-quotient step; primary-source verification remains an explicit access limitation.
The independent rationalization equality, equality of entropy on essential subgroups, purification equality and pure-subgroup divisible-hull equivalence do not require the zero-entropy criterion.
This distinction prevents the inaccessible external proof from being silently represented as checked.

## Findings and minimal corrections

All findings below were first recorded in this repository on 2026-10-06 against the unchanged published artifact.
They are pre-existing source defects, not errors introduced by the entry-key correction.
No evidence of an author-issued correction was obtained.
The counterexamples/repairs below are elementary checks of the cited source passages, not claims of new mathematical results.

<a id="finding-integral"></a>
### F1: the stated integral condition does not imply zero torsion entropy

**Severity: substantive false literal assertion; source p.626, paragraph after Example 3.1 (PDF p.15).**
The source calls $\phi$ integral whenever some nonzero $f\in\mathbb Z[t]$ satisfies $f(\phi)=0$, then asserts that torsion $G$ implies $\operatorname{ent}(\phi)=0$, attributing this to [16, Lemma 2.2].

Take $G=(\mathbb Z/p\mathbb Z)^{(\mathbb N)}$ and $\phi=\beta_{\mathbb Z/p\mathbb Z}$.
The nonzero constant polynomial $f=p$ kills the whole group, so the displayed definition holds, but the subgroup in coordinate zero has $n$-trajectory cardinality $p^n$.
Thus $\operatorname{ent}(\phi)=h(\phi)=\log p>0$.
Even requiring positive degree would not fix the condition, since $f=pt$ also annihilates $\phi$.

**Reusable repair:** require a monic annihilating integer polynomial for this assertion.
If its degree is $d$, iterates of each finite torsion subgroup are contained in the finite subgroup generated by its first $d$ images, so trajectory entropy is zero.
This establishes sufficiency of the repair directly; it does not assert the inaccessible [16] uses this exact wording.
The contrast with multiplication by $k>1$ on $\mathbb Z$ remains valid because $t-k$ is monic.
No proof step in the reviewed Addition-Theorem reduction uses the false unrestricted assertion.

**Targeted search evidence:** query `Dikranjan Goldsmith Salce Zanardo algebraic entropy 2009 Lemma 2.2 integral monic`, then the [author repository record](https://arrow.tudublin.ie/scschmatart/29/) identifying DOI 10.1090/S0002-9947-09-04843-0.
The repository's [PDF endpoint](https://arrow.tudublin.ie/cgi/viewcontent.cgi?article=1027&context=scschmatart) and the [AMS PDF endpoint](https://www.ams.org/journals/tran/2009-361-07/S0002-9947-09-04843-0/S0002-9947-09-04843-0.pdf) returned HTTP 403 to web access; the coordinating agent also reported HTTP 403 for direct verified-TLS acquisition.
No external Lemma 2.2 text or original proof was read.
Search stopped because the source-internal counterexample already resolves the literal assertion, while original-citation verification is explicitly outstanding.

<a id="finding-invariance"></a>
### F2: Lemma 3.5 needs invariance of the subgroup

**Severity: missing domain hypothesis; p.627 (PDF p.16).**
Its conclusion says the Addition Theorem holds “for every subgroup $H$”.
Yet $\phi|_H$ is an endomorphism of $H$, and $\bar\phi$ is defined on $G/H$, only when $\phi(H)\subseteq H$.
For example, take the shift on $\mathbb Z^{(\mathbb N)}$ and $H=\mathbb Z e_0$; the infinite-rank hypothesis holds but neither required action on $H$ or $G/H$ exists.
Insert “$\phi$-invariant” in the statement and proof.
All later uses in Proposition 4.7 already have that hypothesis; the corrected proof was checked above.

<a id="finding-purification"></a>
### F3: a smallest pure overgroup need not exist with torsion

**Severity: overbroad definition; p.628, before Lemma 3.8 (PDF p.17).**
The source introduces purification for an arbitrary subgroup of an arbitrary abelian group as its smallest pure overgroup.
Let $G=\mathbb Z/4\mathbb Z\oplus\mathbb Z/2\mathbb Z$ and $H=\langle(2,0)\rangle$.
The subgroups $A=\langle(1,0)\rangle$ and $B=\langle(1,1)\rangle$ are direct summands, hence pure, and $A\cap B=H$.
But $H\cap2G=H\ne0=2H$, so $H$ is not pure.
A smallest pure overgroup would be contained in both $A$ and $B$, hence equal to $H$, a contradiction.

Restrict this definition to torsion-free ambient groups, as done in the precise definition above.
Corollaries 3.9 and 3.10 already impose torsion-freeness; their uses and conclusions are unaffected.
Lemma 3.8's three separate purity statements remain correct for their stated hypotheses.

### F4: Example 3.2 uses a false lattice-cardinality estimate

**Severity: repairable proof estimate; p.626 (PDF p.15).**
For $\phi(x,y)=(x+ky,y)$ the printed bound is $|T_n(\phi,F_m)|\le2n^2m^2(2+nk-k)$.
At $n=m=1$, the left side is $9$ and the right side is $4$, for every $k$; for negative $k$ the bound even becomes negative at sufficiently large $n$.

For a trajectory point $(X,Y)$, the exact iterate formula gives

$$
|Y|\le nm,\qquad |X|\le nm+|k|m\,n(n-1)/2.
$$

Therefore the valid integer-box bound is

$$
|T_n(\phi,F_m)|\le
(2nm+1)\bigl(2nm+|k|m n(n-1)+1\bigr).
$$

Its polynomial growth proves the stated zero entropy for every integer $k$.
This fixes the proof without altering the example's conclusion or any later reduction.

### F5: Example 3.11 needs endpoint terms and a reduced fraction

**Severity: repairable estimate and omitted parameter condition; p.630 (PDF p.19).**
In (a), write $a>b>0$, $\gcd(a,b)=1$ and $F_m=b^{-m}\mathbb Z\cap[-m,m]$.
The source's cardinality estimate omits an endpoint term, and its logarithmic estimate also drops $\log m$.
Already $a=3,b=2,n=m=1$ gives $|F_m|=5$, whereas the printed cardinality upper bound is $4$.
The valid bound from the same grid containment is

$$
|T_n(\mu_{a/b},F_m)|\le 2nmb^m a^{n-1}+1,
$$

whose normalized logarithm still has limsup at most $\log a$.
For the lower bound, multiplying an equality of digit expansions by $b^{n-1}$ and reducing modulo $a$ forces the first digit difference to vanish; induction proves all $a^n$ sums distinct.

Part (b) states $h(\mu_{a/b}:\mathbb Q^n\to\mathbb Q^n)=n\log a$ for $a>b>0$, but must retain the coprimality condition from (a).
Without it $a=4,b=2$ incorrectly yields $n\log4$ for multiplication by $2$.
With a reduced fraction, the general scalar statement is $h(\mu_{a/b})=\log\max\{|a|,|b|\}$ for nonzero reduced $a/b$; the zero map has entropy zero.
This follows from (a), sign invariance and inverse invariance.
Part (c)'s torsion-free multiplication formula remains valid.

### F6: two typed errors in Proposition 2.8's proof

**Severity: local typographical defects; p.623 (PDF p.12).**
In (a), the printed $\xi\phi^k=\phi^k\xi$ has incompatible domains for different groups; use $\xi\phi^k=\eta^k\xi$.
In (b), the final numerator of the first limit display changes $T_{kn-k+1}$ to $T_{kn-n+1}$; retain $kn-k+1$.
The surrounding argument supplies the correct expressions, and the statements follow by the checked trajectory identities.

## Verification boundary and downstream effects

The assigned agent read all of Sections 2--4, not just extracted theorem statements, and visually confirmed the suspect formulas and delicate barred/extended endomorphism notation.
All counterexamples and corrective estimates in F1--F6 were checked directly by finite arithmetic or the displayed elementary argument.
No proof assistant, general computational theorem check, or independent reviewer certification was used.

For subsequent use, cite this unit's corrected hypotheses and definitions.
F1 and F3 must not be imported in their literal unrestricted forms; F2 requires invariance; F4--F6 require the displayed repairs.
The core reduction interfaces supplied to [DGB16-U002](Yin_U002.md#dgb16-u002) remain valid with their retained dependencies.
No existing project Claim is reassessed by this source entry; consumers beyond the linked source units were not invented.
A later primary check of [16] may improve attribution and external-interface evidence, but cannot remove the explicit counterexamples to the words printed in DGB16.
