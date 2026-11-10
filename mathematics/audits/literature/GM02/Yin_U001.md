---
author: Yin
---

# GM02: unchanged-polynomial realization on an even unimodular lattice

<a id="gm02-u001"></a>
## Inspected scope

Use the [author copy displaying 1 January 2002](readme.md#author-copy).
The selected passages are Theorems 1.2--1.3 on printed pages 1--2, the number-field and trace-dual conventions and Proposition 3.1 in Section 3, Theorems 4.1--4.2 and the completeness remark in Section 4 on pages 10--12, and the ideal-norm/sign interface in Section 5 on pages 13--15.
Sections 7--8 on pages 18--23 were additionally read for the bounded explicit-example lookup below.
The title/contents page and printed pages 1, 10--11, 15 and 21 were also checked visually against the retained PDF, including the conjugation bars, ideal equation and numbered examples.
This is direct statement and construction-interface reading, not an independent proof audit of the paper or of its class-field-theoretic inputs.

<a id="unramified-reciprocal"></a>
## Unramified polynomial and realization theorem

**Definition (GM02, printed page 1).**
A monic reciprocal polynomial $S\in\mathbb Z[x]$ of degree $2n$ is called unramified when
\[
|S(1)|=|S(-1)|=1.
\]
The source's Proposition 3.3 also gives $S(-1)S(1)=(-1)^n$ and the parity restriction $n\equiv s\pmod2$ when $2s$ roots lie off the unit circle.
The polynomial terminology concerns these endpoint values; Proposition 3.1 separately relates it to the associated quadratic extension being unramified at finite primes.
It does not mean that the full number field is unramified over $\mathbb Q$.

<a id="unimodular-realization"></a>
**Theorem 1.2 (source statement).**
Let $S\in\mathbb Z[x]$ be monic, irreducible, reciprocal and unramified, of degree $2n$, with $2s$ roots off the unit circle.
For an even indefinite unimodular lattice $II_{p,q}$ with
\[
p+q=2n,\qquad p,q\ge s,\qquad p\equiv q\equiv s\pmod2,
\]
there is an isometry with characteristic polynomial exactly $S$.
The existence of $II_{p,q}$ itself requires $p,q>0$ and $p\equiv q\pmod8$, as recalled by the source; the notation does not suppress this additional signature condition.
Theorem 1.3 states the finer real-conjugacy formulation: if $F\in SO_{p,q}(\mathbb R)$ has irreducible unramified characteristic polynomial in $\mathbb Z[x]$ and $p\equiv q\pmod8$, it preserves an even unimodular lattice in the real representation space.

For the direct specialization to a degree-18 Salem polynomial with $S(1)=-1$ and $S(-1)=1$, take $n=9$, $s=1$ and $(p,q)=(17,1)$.
All the displayed signature and endpoint conditions hold.
This specialization starts from the given irreducible Salem polynomial; it does not establish irreducibility or the Salem root shape for a new input.
It changes neither the polynomial nor its complete Mahler measure and uses no power or added dimension.

<a id="ideal-trace-pairing"></a>
## Fractional ideal and invariant pairing

**Definition and conventions (Sections 3--4).**
Put $K=\mathbb Q[\alpha]=\mathbb Q[x]/(S)$ and $k=\mathbb Q[\alpha+\alpha^{-1}]$.
Write $\bar a$ for the involution of $K/k$ taking $\alpha$ to $\alpha^{-1}$, and $\bar I$ for its action on a nonzero fractional $\mathcal O_K$-ideal $I$.
The trace dual is
\[
\mathcal O_K^\vee
=\{b\in K:\operatorname{Tr}_{K/\mathbb Q}(b\mathcal O_K)\subseteq\mathbb Z\}.
\]
For $\xi\in k^\times$, the associated invariant bilinear pairing is
\[
B_\xi(a,b)=\operatorname{Tr}_{K/\mathbb Q}(\xi a\bar b).
\]

Theorem 4.1 gives a unimodular lattice $(I,B_\xi)$ under the exact ideal condition
\[
I\bar I(\xi)=\mathcal O_K^\vee.
\]
It is even when $K/k$ is unramified at finite primes, which Proposition 3.1 supplies for an unramified $S$.
Multiplication $f(a)=\alpha a$ preserves every fractional $\mathcal O_K$-ideal because $\alpha$ is a unit, and its characteristic polynomial is exactly $S$.

For each real place $\tau$ of $k$ that becomes complex in $K$, Theorem 4.2 identifies the sign of the corresponding real two-dimensional summand with $\operatorname{sign}(\tau(\xi))$.
In the Salem case the one split real place contributes $(1,1)$, and choosing $\tau(\xi)>0$ at every remaining place gives signature $(2n-1,1)$.
For degree 18 there are eight such remaining places.

Section 5 uses the norm map from ideal classes and the Artin map to choose $\xi$ with the required signs and a fractional ideal $I$ satisfying
\[
N_{K/k}(I)(\xi)=\mathcal O_k^\vee,
\qquad N_{K/k}(I)=I\bar I\cap k.
\]
The proof may modify $\xi$ while preserving its required signs.
This is the source's existence mechanism; it is not a displayed basis algorithm, a bounded ideal/unit search, or an explicit ideal and pairing for the degree-18 project input.
The completeness remark on printed page 12 assumes $\mathcal O_K=\mathbb Z[\alpha]$ when classifying all realizations by this ideal construction.
That equality is not a hypothesis of Theorem 1.2 and must not be inferred from unramified endpoint values.

<a id="pairing-and-construction-limits"></a>
## Change of pairing and remaining construction limits

The [ERT19 trace Gram construction](../ERT19/Yin_U001.md#companion-trace-gram), used in the [fixed J158 representation test](../../../computations/programs/Yin_J_G0158/readme.md#question), has the order lattice $\mathbb Z[\alpha]$ with $B_1$ in its power basis.
GM02 instead permits both a fractional ideal $I$ and a different invariant pairing $B_\xi$.
Its theorem does not assert that $I$ contains that order, that $\xi=1$, or that the new lattice is an overlattice in the original rational quadratic space with its fixed form.
The real realization in Theorem 1.3 is likewise not a claimed rational isometry to that fixed form.

For an explicit new integral model one still needs an actual $I$, $\xi$, integral basis and exact pairing and multiplication matrices satisfying the source conditions.
No such lattice construction or ideal/unit calculation is performed here.
Unimodularity makes the new discriminant group trivial, so the particular discriminant-action test on the old lattice supplies no obstruction on this new lattice.
It does not follow that multiplication by $\alpha$ is a word in the prescribed integral Eichler transvections and positive-lattice isometries on one fixed hyperbolic splitting.
The [inspected GHS09 generation statements](../GHS09/Yin_U001.md#two-plane-generation) retain their separate two-hyperbolic-plane and local-rank hypotheses.
GM02 supplies no word decomposition or word-length bound for that one-plane problem.

The input is an already known Salem polynomial.
This realization theorem alone produces neither a new small Mahler value nor a sequence of positive complete logarithmic measures tending to zero.
No project Claim assessment or route adoption is made by this source unit.

<a id="explicit-example-lookup"></a>
## Degree-18 example lookup

The comparison input is the exact H_ascending polynomial in [J144's fixed input](../../../computations/programs/Yin_J_G0144/trace56_cell.json), rather than a polynomial inferred from a decimal measure.
Section 7's three numbered examples on printed page 21 have degrees 6, 10 and 22.
They provide polynomial families and invoke the realization theorem; they do not supply explicit invariant ideals, Gram matrices or isometry matrices for these families.
The same page reports that the six smallest then-known Salem numbers, referring to its source [B], are unramified special cases of Theorem 7.3.
It does not display the project degree-18 polynomial or specify its parameters in that construction.
That secondary remark was not checked against [B].

Theorem 7.3 and the proof of Theorem 1.6 give a polynomial construction for every odd half-degree at least three, hence include degree 18, with an integer parameter required to be sufficiently large.
This does not provide a fixed degree-18 ideal, form or matrix, or a construction aimed at measures tending to one.
Section 8 on printed pages 22--23 concerns realization of degree-22 unramified Salem polynomials by K3 automorphisms.
The inspected example/application passages therefore supply no explicit degree-18 realization for the selected input; this is a bounded source lookup, not a claim about other literature or a full proof audit of those sections.
