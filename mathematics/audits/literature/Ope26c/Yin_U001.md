---
author: Yin
---

<a id="ope26c-u001"></a>
# Ope26c-U001: arithmetic classification of Bernoulli-convolution measure type

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26c; [retained PDF](../../../literature/pdf/Ope26c.pdf).

Passages: Manuscript dated 3 October 2026 at fixed upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; complete Sections 2--4, Theorem 2.1 through Propositions 4.1--4.2, printed/PDF pp. 3--11.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148.
Separately assigned reviewer read all of classification.tex, rederived the proof interfaces and visually checked PDF pp. 8--10.
It did not develop the source proof or rely on a prior mathematical review.
The coordinator checked the statement and adopted the report at this exact scope; no second full classification review or formal check is claimed.


## Statement and conventions

Let $\nu_\lambda$ be the law of $\sum_{i\ge0}\epsilon_i\lambda^i$, with independent fair signs and $0<\lambda<1$.
Equivalently use fair bits and the affine relation $Y=2X-(1-\lambda)^{-1}$; this preserves measure type.

For integers $n\ge1,d\ge2$, $R(n,d)$ consists of real algebraic units $r\in(1/2,1)$ of degree $dn$ with minimal polynomial having coefficients in $\{-1,0,1\}$ and irreducible reduction modulo 2.
Normalize its sign to constant coefficient $-1$.
Let $\pi_n$ select coefficients of degrees $0,\ldots,n-1$, and put
$$W_n(r;d)=\{\pi_n(p_q):q\in R(n,d),\ |q-r|\le4^{-n}\}.$$
This is a set of distinct vectors.
For $u\in\{0,1\}^n$, let $\mathcal O_u=\{w:(2u_i-1)w_i\ge0\ \forall i\}$, a closed orthant.
Retain $r$ in $R_*(n,d,j)$ if at least $2^n/d$ orthants contain at least $j(2r)^n$ vectors of $W_n(r;d)$.
Define
$$\mathcal C=(0,1/2)\cup\left((1/2,1)\cap\bigcup_{d\ge2}\bigcap_{j\ge1}\limsup_{n\to\infty}\bigcup_{r\in R_*(n,d,j)}[r-4^{-n},r)\right).$$
Theorem 2.1 asserts that $\nu_\lambda$ is singular exactly on $\mathcal C$, and absolutely continuous on its complement in $(0,1)$.
Replacing limsup by liminf preserves the set.
The degree multiplier is chosen before $j$; thresholds in $n$ may depend on $j$.
The parameter $1/2$ is excluded from $\mathcal C$ and gives a uniform law.

## Verdict and boundaries

**Audited within scope; no mathematical defect found in Sections 2-4.**
This covers Theorem 2.1, Lemmas 2.2-2.3 and 3.1, Propositions 3.2 and 3.5, Lemmas 3.3-3.4, and Propositions 4.1-4.2.
The Weil finite-field Dirichlet L-function root bound is retained as an established external input with exact statement and applicability checked below; its original proof was not re-audited.
Standard measure regularity, finite Shannon entropy identities, analytic identity theorem, elementary field norm facts, and the Riemann-Lebesgue lemma are foundational inputs.

The theorem is an infinite approximation characterization of measure type.
It is not a finite terminating membership algorithm, a characterization of Hausdorff dimension, or a degree-independent Mahler bound.
No formal verification is asserted.

## Checked proof interfaces

### Definitions, quantifiers, and forward implication

Locators: PDF pp. 3-5, Theorem 2.1, equations (2.1)-(2.5); TeX lines 11-71 and 149-202.

The root sets are finite since degree and coefficient alphabet are fixed.
For an algebraic unit with leading coefficient +/-1 and constant +/-1, the signed minimal polynomial with constant -1 is unique.
Counting projected vectors, rather than roots or representatives, correctly removes duplicates.
Closed orthants admit the required identity v=u-w in {0,1}^n when w belongs to the orthant of u; coordinate zeros do not cause repeated neighbors for a fixed u.

For a hit lambda in [r-4^{-n},r), every nearby q differs from lambda by at most 2*4^{-n}.
The derivative bound is independent of degree, and the discarded coefficient tail is at most L lambda^n.
Thus every projection lies in a fixed-width slab B lambda^n, uniformly in d,j,w.
The factor 4^{-n}=o(lambda^n) is valid for lambda>1/2.

The bin incidence bound counts words with multiplicity, so coinciding prefix sums do not invalidate it.
It produces a finite union E_j of length O(1/j) and mu-mass at least 1/d.
This rules out absolute continuity by uniform absolute continuity of a finite measure.
The pure-type lemma then proves singularity.
Only arbitrarily large n for each j are needed here; all sufficiently large n are proved separately in the converse.

### Pure type, concentration, and overlap of first-bit measures

Locators: PDF pp. 4-6, Lemmas 2.2-2.3 and 3.1; TeX lines 100-144 and 229-274.

The contracting affine operator has a unique invariant probability: lambda^n Z tends to zero in probability for every probability law of Z, without requiring any moment condition.
Finite affine pushforwards preserve both parts of the Lebesgue decomposition.
If both parts had positive mass, normalization would contradict uniqueness.
The endpoint cases lambda<1/2 and lambda=1/2 have the stated support-cover and uniform law proofs.
The compact concentration equivalence follows from regularity and a summable limsup construction; every tail union has full rho-mass because its constituent compact sets have masses tending to one.

If the first-bit measures were mutually singular, disjoint compact sets capture (X,u0) with error less than eta.
Quantizing X at lambda^n, and revealing preceding bits, determines the ith rescaled tail to error at most lambda^{n-i}.
For i<=n-h this is less than one third of the compact-set separation, giving an estimator of ui with error <=eta.
The binary error flag bounds each conditional entropy by h2(eta), while the at most h remaining bits cost h log2.
The quantized position has only O(lambda^{-n}) values.
Chain rule yields log2<=log(1/lambda)+h2(eta) in the limit, contradicted by choosing h2(eta)<log(2lambda).
This establishes positive common measure mass without assuming singularity or separation of cylinder sums.

### Many opposite-first-bit neighbors

Locators: PDF pp. 6-7, Proposition 3.2; TeX lines 291-365.

Fix common mass b>0 and central tail cutoff a before Q.
The tail restriction discards total mass less than b/8, uniformly in n.
For each Q, singular concentration supplies a compact set of arbitrarily small measure and high mass.
Its bins of length a lambda^n number at most 2epsilon/(a lambda^n) eventually, by continuity of measure for shrinking compact neighborhoods.
Common retained bin mass is at least 3b/4.
Bins with fewer than Q(2lambda)^n opposite-first-bit words cost less than b/4, leaving common mass at least b/2.

A fixed central-tail interval meets at most C_a bins, producing at least c2^n distinct zero-first-bit words, c=b/(2C_a)>0.
Each has the stated number of one-first-bit neighbors.
The same-bin location error is less than a lambda^n and the two central-tail values differ by at most (L-2a)lambda^n, yielding (L-a)lambda^n.
Thus a and c are indeed independent of Q and n, with only the threshold in n depending on Q.

### Uniform finite-order nonvanishing

Locators: PDF pp. 7-8, Lemma 3.3 and (3.3); TeX lines 378-417.

Negating a uniform finite jet lower bound produces bounded-coefficient polynomials whose derivatives through order m at lambda all tend to zero.
Coefficientwise compactness supplies an analytic limit on the unit disk; dominated power-series tails give convergence of every fixed derivative on compact subsets.
The limiting function would vanish to infinite order but have constant coefficient -1, a contradiction.

With M fixed, equivalence of polynomial norms applied to p(lambda+xt) gives a lower bound kappa*delta*x^M for its Taylor polynomial, since x^k>=x^M for k<=M and x<=1.
The coefficient bound controls the next derivative uniformly and the remainder is O(x^{M+1}).
This proves the asserted one-sided interval supremum uniformly over arbitrary lengths of the bounded coefficient polynomials.

### Irreducible completion and its external input

Locators: PDF pp. 8-9, Lemma 3.4 and (3.4); TeX lines 419-472.

For q=2, Q=t^ell, every nonprincipal character has L-degree at most ell-1 and inverse roots of modulus at most sqrt(2), including trivial factors.
Its weighted degree-s sum is therefore bounded by ell*2^{s/2}.
The principal weighted sum is exactly 2^s-1, removing the contribution of the prime t.
There are 2^{ell-1} invertible residue classes.
Orthogonality gives the source's lower bound in every class with no dependence on its representative.
Proper prime powers contribute at most sum_{k|s,k>=2}2^{s/k}<=s2^{s/2}, using degree-times-prime-count <=2^{degree}.
With ell=Dn+1 and s=dn, the main exponent d-D exceeds d/2 exactly when d>2D.
Hence one fixed sufficiently large n threshold works for all F, as claimed.

The exact external interface was checked in the cited published article:

- Ofir Gorodetsky and Valeriya Kovaleva, *Equidistribution of high traces of random matrices over finite fields and cancellation in character sums of high conductor*, Bulletin of the London Mathematical Society 56(7) (2024), 2315-2337, DOI `10.1112/blms.13057`.
- Theorem 3.2 and preceding L-polynomial degree statement: printed p. 2326 / PDF p. 12.
  Lemma 3.3 and its logarithmic-derivative proof: printed p. 2327 / PDF p. 13.
  Both pages were rendered and visually read.
- Theorem 3.2 is explicitly stated for nonprincipal Dirichlet characters; no primitiveness or odd-character restriction prevents its use for characters modulo t^ell over F2.
  It gives inverse-root moduli 1 or sqrt(q); the required bound is consequently valid also for even and imprimitive characters.
  Lemma 3.3's short deduction was checked.
- Acceptance: use this established Weil bound as an external theorem, with exact q=2, Q=t^ell applicability checked.
  The original proof of Weil's theorem and the rest of Gorodetsky-Kovaleva were not reviewed.

The exact external input and its acceptance boundary are retained in [GK24-U001](../GK24/Yin_U001.md#gk24-u001).

### Realization of every prefix with one fixed degree multiplier

Locators: PDF pp. 9-10, Proposition 3.5, (3.5)-(3.7); TeX lines 474-572.

For |e|>1 the nearest permitted digit has the same sign and the update is L+(|e|-L)/lambda.
The initial margin |e|<=L-a therefore reaches [-1,1] in a number of steps depending only on lambda,a.
One further nearest-digit step puts the residual in [-1/(2lambda),1/(2lambda)], which remains inside [-1,1].
Since (D-1)n tends to infinity, the final residual estimate |p0(lambda)|<=lambda^{Dn}/(2lambda) is valid uniformly in the original w.

Choose D with lambda^D<4^{-M} and d0=2D+1.
The appendage size divided by x_n^M, x_n=4^{-n}/2, tends to zero uniformly, since ((lambda+x_n)/lambda)^{Dn}=exp(O(n x_n)) tends to one and the strict exponential inequality dominates.
The finite-order point t_n therefore has nonzero p0-value too large for any appendage to change its sign.

Irreducible completion prescribes a 1 at index Dn and at the leading index dn.
Both p0+T and p0-T reduce to that same irreducible polynomial over F2.
At lambda their signs are strictly positive and strictly negative because 1/(2lambda)<1; at t_n they have the same nonzero sign.
Thus one crosses strictly to the right of lambda.
The degree is preserved under reduction, leading coefficient is +/-1, and constant coefficient is -1, so Gauss's lemma gives irreducibility over Q and each root is an algebraic unit.
The resulting signed minimal polynomial has exactly the required prefix.
The construction is uniform over w for every fixed d>=d0; it does not claim a uniform threshold over all d.

### Completion of the converse and classical cases

Locators: PDF pp. 10-11; TeX lines 574-704.

Choose d>=d0 with 1/d<c before choosing j.
For each j choose Q>2j.
All realized roots lie in one interval of length 4^{-n}/2 immediately above lambda.
Any one may be the common center, and all associated projections lie in its W_n set.
For fixed u, distinct neighbors still give distinct vectors after completion.
The estimate (r/lambda)^n->1 is uniform over all chosen centers, so Q(2lambda)^n>=j(2r)^n eventually.
There are c2^n>2^n/d good orthants.
Consequently this same d works for every j and all sufficiently large n, with the threshold allowed to depend on j.
This proves liminf membership; the forward implication then proves that liminf and limsup define the same set.

For Proposition 4.1, subtracting two vectors in the same closed orthant retains coefficients in {-1,0,1}.
A nonzero such polynomial cannot vanish at the Garsia parameter beta: after removing a power of t, divisibility by the monic minimal polynomial with constant term of magnitude 2 would force its nonzero constant +/-1 to be even.
The nonzero norm estimate gives separation >=c_beta*2^{-n}.
Slab packing uniformly bounds the orthant count by C_beta(2lambda)^n; a fixed j>C_beta rules out every sufficiently late hit for all d.
The classification then gives absolute continuity.

For Proposition 4.2, a Pisot number in (1,2) has nonzero integer norm of magnitude less than 2 and is a unit.
Thus no beta^ell is a rational odd half-integer.
Both tails of the log-cosine sum converge, one by geometric smallness and the other by integer trace approximation.
The Fourier transform has a positive lower bound along unbounded frequencies; Riemann-Lebesgue excludes absolute continuity and pure type gives singularity.
Theorem 2.1 supplies the claimed approximation property.

## Relation to G0001

This characterization uses a degree multiplier that may depend on the particular lambda, and arbitrarily large finite polynomial collections at arbitrarily large n.
It produces neither a uniform finite detection scale nor a uniform lower bound for positive Mahler measures.
No G0001 completion or new research continuation is authorized by this source review alone.
