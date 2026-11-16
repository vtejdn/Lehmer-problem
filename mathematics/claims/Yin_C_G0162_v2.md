---
author: Yin
---

# Frobenius matching with the ramification indices of the ratio field

<a id="statement"></a>
## An estimate in the original degree

Let \(\alpha\) be a nontorsion algebraic integer unit of degree \(d\), with total logarithmic Mahler measure \(m=d h(\alpha)>0\).
Let \(p\) be a rational prime and fix a prime above it in the normal closure \(L\) of \(\mathbb Q(\alpha)\).
Take any orbit \(\Omega\) of ordered pairs of roots under \(\operatorname{Gal}(L/\mathbb Q)\), with representative \((x,y)\), size \(sd\), ratio \(\rho=x^p/y\) and \(D=[E:\mathbb Q]\) for \(E=\mathbb Q(\rho)\).
Write \(C\) for the subset of pairs \((z,w)\in\Omega\) with \(\bar z^p=\bar w\) in the chosen residue field, and \(\beta=|C|/(sd)\).
Assume \(\beta>0\).
For each prime \(\mathfrak q\mid p\) of \(E\) where \(\rho\equiv1\bmod\mathfrak q\), write \(e_{\mathfrak q},f_{\mathfrak q}\) for its ramification index and residue degree.
All sums over \(\mathfrak q\) below are restricted to these primes.
For \(t=p^a\) with \(a\ge0\), set
\[
 B(t)=\frac1D\sum_{\mathfrak q} f_{\mathfrak q}\min(e_{\mathfrak q},t),
 \qquad e_*=\max_{\mathfrak q} e_{\mathfrak q}.
\]
Then \(\beta=D^{-1}\sum_{\mathfrak q}e_{\mathfrak q}f_{\mathfrak q}\), and the complete norm satisfies
\[
 B(t)\log p\ \le\ \frac1D\log\left|N_{E/\mathbb Q}(\rho^t-1)\right|,
 \qquad
 m>\frac{d}{(p+1)t}H_5(B(t)\log p).                                  \tag{1}
\]
Here \(H_5\) is the [capped inverse for a cyclic norm](Yin_C_G0147_v5.md#statement).
On \(0<h\le e^{-40}\) its increasing modulus is \(\Phi_5(h)=86\sqrt h\,(\log(1/h))^{5/2}/(\log\log(1/h))^{3/2}\).
The inverse is \(e^{-40}\) when \(\tau/2\ge\Phi_5(e^{-40})\) and otherwise solves \(\Phi_5(H_5(\tau))=\tau/2\).
No small-height assumption is needed for (1).

At exponent one, define \(e_{\mathrm h}=\beta/B(1)\), the harmonic mean of the selected indices with weights \(e_{\mathfrak q}f_{\mathfrak q}\).
For \((p+1)m/d\le e^{-40}\) one has
\[
 \frac{e_{\mathrm h}}{\beta}\ \ge\
             \frac{\log p}{\Phi_5((p+1)m/d)}.                           \tag{2}
\]
In the [Frobenius orbit of \(x\)](Yin_C_G0162_v1.md#statement), take \(y=\sigma x\) for any lift of residue Frobenius and let \(\gamma=d^{-1}\#\{z:(z,\sigma z)\in\Omega\}\).
Then \(\beta\ge\gamma/s\), so (2) also holds with left side \(e_Ls/\gamma\), where \(e_L\) is the ramification index of the chosen prime in \(L\).
In (1), choosing \(t=p^{\lceil\log_p e_*\rceil}<p e_*\) gives
\[
 m>\frac{d}{p(p+1)e_*}\,H_5(\beta\log p).                              \tag{3}
\]
One can also use (1) with a smaller power when some of the local indices are large.
At fixed \(p\) this yields the [growing-degree bound](#degree-range) in terms of \(d,e_*\) and \(\beta\).
For every prescribed finite nonempty prime set there are nevertheless [reciprocal units](#finite-pool) of each degree \(d=2\ell\) with \(\ell\ge5\) prime, of arbitrarily large measure, whose unique compatible orbit has \(\beta=1/(d-2)\) at each designated prime, with unramified distinct reductions.
There is also such a family with coefficient height bounded solely in terms of the prescribed prime set, \(M(\alpha)>2\) and \(m\le\tfrac12\log(d+1)+O_S(1)\), so its absolute heights tend to zero.

<a id="local-proof"></a>
## Embeddings, compatible edges and local depths

Both coordinate projections of \(\Omega\) have fibers of size \(s\), and each distinct conjugate of \(\rho\) occurs \(sd/D\) times among the pairs.
These [pair-field and signed norm identities](Yin_C_G0477_v1.md#statement) give \(h(\rho)\le(p+1)m/d\).
The ratio is a nontorsion unit, since a torsion relation \(x^{pv}=y^v\) with \(v>0\) could be iterated around the finite order of an automorphism sending \(x\) to \(y\).
Every pair above a given conjugate has the same ratio, including its residue at the fixed prime.
The embeddings of \(E\) inducing each selected \(\mathfrak q\) number \(e_{\mathfrak q}f_{\mathfrak q}\), its completion degree.
Precisely these embeddings produce a conjugate reducing to one.
The constant fiber size now gives the formula for \(\beta\), even for repeated reductions.
At exponent one the exact \(p\)-valuation of the norm is \(\sum_{\mathfrak q}f_{\mathfrak q}\operatorname{ord}_{\mathfrak q}(\rho-1)\), by the [ideal norm formula](Yin_C_G0256_v1.md#content-versus-ideal-norm).
Thus \(B(1)\) uses at least one integral order at each of the actual selected primes.

Normalize the valuation by \(v(p)=1\).
At a selected prime, \(v(\rho-1)\ge1/e_{\mathfrak q}\).
The binomial theorem gives \(v(u^p-1)\ge\min(pv(u-1),1+v(u-1))\) whenever \(v(u-1)>0\).
Induction yields \(v(\rho^{p^a}-1)\ge\min(1,p^a/e_{\mathfrak q})\), also at \(p=2\).
Summing with weights \(e_{\mathfrak q}f_{\mathfrak q}\), using integrality at the other primes and nonvanishing of the norm, proves its lower bound in (1).
The [full cyclic estimate](Yin_C_G0147_v5.md#statement) gives \(t h(\rho)>H_5(B(t)\log p)\), including the part of the parameter range above its small-height domain.
The height bound proves (1), and at \(t=1\) the monotonicity of \(\Phi_5\) on its domain proves (2).
Every selected \(e_{\mathfrak q}\) divides \(e_L\) by the ramification tower, and each edge \((z,\sigma z)\) belongs to \(C\) when it belongs to \(\Omega\), by [residue Frobenius](../audits/literature/The26b/Yin_U001.md#the26b-u001).
Since \(B(t)=\beta\) for \(t\ge e_*\), (3) follows.

For return to \(\mathbb Q(x)\), the nonzero integer of this field \(\eta=N_{\mathbb Q(x,y)/\mathbb Q(x)}(x^{pt}-y^t)\) satisfies
\[
 |N_{\mathbb Q(x)/\mathbb Q}(\eta)|
   =|N_{E/\mathbb Q}(\rho^t-1)|^{sd/D}.
\]
This is the [pair-field norm tower](Yin_C_G0162_v1.md#argument), since the omitted unit factor has rational norm of absolute value one.
The relative norm has \(s\) factors and total conjugate exponent at most \(spt\).

<a id="degree-range"></a>
## Growing valency and the logarithmic threshold

Fix \(p\) and put \(k=1/\beta\).
For \(k\to\infty\), the [asymptotic inverse](Yin_C_G0147_v5.md#statement) in (3) yields
\[
 m\ \gg_p\ \frac{d}{e_*k^2}\,
            \frac{(\log\log k)^3}{(\log k)^5}.                          \tag{4}
\]
In particular the original total measure is bounded below if the right-hand expression has positive lower limit.
For example, at an unramified prime this includes \(k\to\infty\) with \(k\le d^{1/2-\epsilon}\) for any fixed \(0<\epsilon<1/2\).
In that example the lower bound tends to infinity.
More generally one can replace \(k\) by \(s/\gamma\) and \(e_*\) by \(e_L\) in (3), by monotonicity, and derive (4) for these weaker parameters when \(s/\gamma\to\infty\).

The [earlier orbital estimate](Yin_C_G0162_v1.md#statement) powers to the whole ratio degree \(D\), giving \(H_5((\gamma/s)\log p)/(p(p+1)s)\) for its cyclic bound.
The factor \(d/e_*\) in (3) retains the original degree when actual local ramification is smaller.
The [complete mixed resultant](Yin_C_G0477_v1.md#statement) has an unconditional \(p^d\) divisor at \(t=1\), spread over \(d^2\) ordered pairs.
This floor alone gives only the mean normalized income \((\log p)/d\) before selecting any orbit.
Independently, [the prior rank-two and residue-mass comparison](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) supplies \(m\ge C_\epsilon d^{1/2-\epsilon}s^{-1/2-\epsilon}\) for multiplicatively independent \(x,y\).
For fixed \(p\), the earlier all-pair bound gives a uniform gap when \(s\) is bounded above and \(\gamma\) is bounded below by a fixed positive constant.
For equal-height nontorsion conjugates a multiplicative dependence gives \(y=\zeta x^{\pm1}\), where \(\zeta\) is a root of unity, by [the dependence calculation](Yin_C_G0483_v1.md#independent-and-dependent-pairs).
At a reciprocal [all-power degree-preserving endpoint](Yin_C_G0231_v1.md#all-positive-power-existence-descent), both \(x\) and \(x^{-1}\) are roots and every positive power is injective on the root set.
Taking the order of \(\zeta\) as the power forces \(y=x\) or \(y=x^{-1}\), so every other pair already has the rank-two bound.
The cited existence descent supplies reciprocal endpoints in the stated small-measure window and does not preserve a given local orbit.
Formula (4) is a degree-sensitive consequence of this Frobenius norm calculation, without a multiplicative independence assumption.

<a id="finite-pool"></a>
## Reciprocal units with sparse matching at every prime in a finite set

Fix any finite nonempty set \(S\) of rational primes.
For each prime \(\ell\ge5\) there are monic irreducible reciprocal unit polynomials of degree \(d=2\ell\) with arbitrarily large total measure such that each \(p\in S\) is unramified in the splitting field and has distinct root reductions.
At each such \(p\) precisely one ordered-pair orbit has \(\beta>0\), and there \(\beta=1/(d-2)\).

To construct them, write \(P(z)=z^\ell F(z+z^{-1})\) with \(F\) monic integral of degree \(\ell\).
For each \(p\in S\) take \(\lambda\) of order \(p^\ell+1\) in \(\mathbb F_{p^{2\ell}}^\times\).
The multiplicative group of a finite field is cyclic, since its exponent is attained in the finite abelian group and the equation \(X^N=1\) has at most \(N\) solutions for the exponent \(N\).
The degree of \(\lambda\) over \(\mathbb F_p\) is \(2\ell\) by [finite-field Frobenius](../audits/literature/Hun74/Yin_U006.md#hun74-u006).
Indeed its order divides \(p^{2\ell}-1\), while a proper divisor \(j\) of \(2\ell\) satisfies \(j\le\ell\) and \(p^j-1<p^\ell+1\).
The trace \(v=\lambda+\lambda^{-1}\) lies in \(\mathbb F_{p^\ell}\) since \(\lambda^{p^\ell}=\lambda^{-1}\), and \([\mathbb F_p(\lambda):\mathbb F_p(v)]\le2\) gives \(\deg v=\ell\).
Prescribe \(F\bmod p\) to be the minimal polynomial of \(v\), so \(P\bmod p\) is irreducible and separable of degree \(2\ell\).

Choose two distinct odd auxiliary primes \(q,q'\notin S\) larger than \(4\ell+5\).
Modulo \(q\), prescribe \(F\) as a product of one irreducible quadratic and \(\ell-2\) distinct linear factors, all with roots different from \(\pm2\).
Modulo \(q'\), take \(\ell\) distinct traces \(u+u^{-1}\), exactly one from a norm-one \(u\in\mathbb F_{q'^2}\setminus\mathbb F_{q'}\) and the others from \(u\in\mathbb F_{q'}^\times\setminus\{1,-1\}\).
Inversion pairs the eligible elements, giving \((q'-1)/2\) available nonsplit traces and \((q'-3)/2\) split ones.
The two sets are disjoint by the root sets of \(z^2-(u+u^{-1})z+1\).
Prescribe \(F\) with these \(\ell\) roots modulo \(q'\).
The integer Chinese remainder theorem realizes all prescriptions simultaneously.
All these local reductions of \(P\) are squarefree, since the trace roots are simple and avoid \(\pm2\) and different trace quadratics have disjoint roots.
At the primes in \(S\) this also follows directly from separability of their irreducible reductions, including characteristic two.
Inertia fixes every root when reductions are distinct, so each specified prime is unramified in the splitting field and a residue-Frobenius lift permutes the roots with the degrees of the reduction factors.

Irreducibility at any \(p\in S\) gives irreducibility over \(\mathbb Q\).
The Galois group permutes the \(\ell\) reciprocal pairs and acts on these blocks through a subgroup of \(S_\ell\) containing an \(\ell\)-cycle from \(p\) and a transposition from \(q\).
Conjugating that transposition by the cycle gives edges of a connected graph on \(\mathbb Z/\ell\mathbb Z\), since their fixed nonzero step generates this prime-order group.
The resulting transpositions generate \(S_\ell\).
The Frobenius at \(q'\) fixes every block and exchanges the two roots in just one block.
Conjugation gives all single-block exchanges, proving the full wreath group \((C_2)^\ell\rtimes S_\ell\).
This action has three ordered-pair orbits, corresponding to equality, inversion and membership in different blocks.
At each \(p\in S\) the block permutation is an \(\ell\)-cycle and the reductions of all \(d\) roots are distinct.
Thus the \(d\) compatible pairs are exactly the Frobenius edges, all in the third orbit of size \(d(d-2)\).

Finally, adding arbitrary integer multiples of \(qq'\prod_{p\in S}p\) to the constant coefficient of \(F\) preserves all these conditions.
As those coefficients grow in magnitude, some trace root grows unboundedly in modulus by their product, and at least one of its reciprocal lifts grows unboundedly too.
The resulting total measures can therefore be arbitrarily large.
This family prevents a universal square-root matching bound for all units at a prescribed finite prime pool.
Whether small original total measure forces a more favorable orbit, greater actual local depth, or another source of norm income remains open.

To see why even vanishing absolute height cannot supply the matching, we now choose two fixed auxiliary odd primes \(q,q'\ge7\) outside \(S\), independently of \(\ell\).
At \(p\in S\) retain the earlier prescription.
At \(q\) prescribe \(F\) to have two irreducible factors of degrees \(2,\ell-2\).
They are distinct, separable, and neither vanishes at \(2\) or \(-2\).
Since \(\ell-2\) is odd, the \((\ell-2)\)-th power of the Frobenius action on the blocks is a transposition.
At \(q'\) take one split linear trace and one nonsplit linear trace as above, and a degree-\((\ell-2)\) trace whose two lifts have that same odd degree.
For the last trace choose a generator \(u\) of \(\mathbb F_{q'^{\,\ell-2}}^\times\) and take \(u+u^{-1}\).
The generator has degree \(\ell-2\) by its order, and the extension of its trace field has degree at most two and divides the odd integer \(\ell-2\), so the two fields coincide.
The conjugates of \(u\) and \(u^{-1}\) form distinct cycles: if Frobenius took one to the other, its action on the cyclic orbit of odd length would induce a nonidentity element of order two there.
Thus the large trace factor lifts to two cycles of length \(\ell-2\), whereas the nonsplit linear trace gives a single exchange.
The \((\ell-2)\)-th power of Frobenius at \(q'\) acts as this single flip and fixes all other roots.
The same group and orbit conclusions follow.

Put \(N=qq'\prod_{p\in S}p\).
Lift the prescribed reciprocal polynomials \(z^\ell F(z+z^{-1})\) by the Chinese remainder theorem applied directly to one integer coefficient for each pair of symmetric positions, including the middle position once.
Keep the leading and constant coefficients equal to one.
At positions \(1,d-1\) choose the representative in the interval \([-4N-4,-3N-4)\); at all other interior positions choose representatives of absolute value at most \(N\).
The resulting monic reciprocal polynomial comes from a monic integral trace polynomial, since \(z^{-\ell}P(z)\) is a symmetric integral Laurent polynomial and \(z^j+z^{-j}=T_j(z+z^{-1})\).
It has exactly the specified reductions.
Writing \(a_{d-1}\) for the coefficient of \(z^{d-1}\), we have \(P(2)/2^{d-1}\le 2+a_{d-1}+N<0\), by summing the geometric series for the remaining powers, whose coefficients are each at most \(N\).
There is a real root above two.
On the other hand the circle mean formula, the arithmetic-geometric mean inequality applied to \(|P|^2\) and character orthogonality give \(M(P)\le(\sum_j |a_j|^2)^{1/2}\le(4N+4)\sqrt{d+1}\).
Thus the absolute height tends to zero while the total logarithmic measure stays above \(\log 2\).

The main researcher proposed using the unpowered ratio norm at the original absolute height for [Yin's Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The construction contributor derived the interpolated local estimate, the growing-degree range and the finite-pool family on 2026-11-16.
The main researcher obtained the bounded-coefficient refinement by fixing the auxiliary primes and lifting the reciprocal coefficients directly.

## Assessment history

### Decision ramification-matching-open

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:59 |
| status | open |
| reason | Register the own-field ramification estimates, original-degree consequences and finite-prime reciprocal construction for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-unit estimate and finite-prime construction](#statement) | Every prime, all residue-compatible orbit edges, all powers with nonnegative exponent, both inversion domains, the growing-degree threshold and the reciprocal family for arbitrary finite prime pools. |
| argument | [Local interpolation](#local-proof) | Constant fibers, local degrees, binomial amplification, height, full norm and return. |
| argument | [Degree threshold](#degree-range) | Inverse asymptotic and comparison with earlier quantitative coverage. |
| argument | [Construction](#finite-pool) | Finite fields, coefficient congruences, Galois actions and archimedean size. |
| dependency | [Cyclic norm estimate](Yin_C_G0147_v5.md#statement) | Full upper modulus, inverse including its cap and its asymptotic at zero. |
| dependency | [Pair calculations](Yin_C_G0477_v1.md#statement) | All-orbit degrees, equal ratio fibers, nontorsion, height and the global resultant floor. |
| dependency | [Orbital norm and return](Yin_C_G0162_v1.md#argument) | Residue-Frobenius graph, relative norm tower, complete original degree and exponent costs. |
| dependency | [Ideal norm counting](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Exact residue-degree weighting, ramification and normalized integer valuations. |
| dependency | [Residue Frobenius](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Existence of the residue lift and local degree decomposition at the checked scope. |
| dependency | [Finite fields](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Finite-field extensions, irreducible degrees and Frobenius at the checked scope. |
| support | [All-power endpoints](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Existence descent, power-degree preservation and endpoint reciprocity in the small-measure window. |
| support | [Rank-two bound](Yin_C_G0483_v1.md#independent-and-dependent-pairs) | Actual multiplicatively independent and dependent pairs at the fixed-rank comparison's scope. |
| support | [Prior coverage](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Earlier residue-mass and multiplicatively independent rank-two estimates. |


### Decision ramification-matching-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T11:08 |
| status | proved |
| reason | Adopt the local ramification bound on the original total measure and the reciprocal finite-prime constructions, including the bounded-coefficient family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-unit estimate and finite-prime construction](#statement) | Every prime, all residue-compatible orbit edges, all powers with nonnegative exponent, both inversion domains, the growing-degree threshold and the reciprocal family for arbitrary finite prime pools. |
| argument | [Local interpolation](#local-proof) | Constant fibers, local degrees, binomial amplification, height, full norm and return. |
| argument | [Degree threshold](#degree-range) | Inverse asymptotic and comparison with earlier quantitative coverage. |
| argument | [Construction](#finite-pool) | Finite fields, coefficient congruences, Galois actions and archimedean size. |
| dependency | [Cyclic norm estimate](Yin_C_G0147_v5.md#statement) | Full upper modulus, inverse including its cap and its asymptotic at zero. |
| dependency | [Pair calculations](Yin_C_G0477_v1.md#statement) | All-orbit degrees, equal ratio fibers, nontorsion, height and the global resultant floor. |
| dependency | [Orbital norm and return](Yin_C_G0162_v1.md#argument) | Residue-Frobenius graph, relative norm tower, complete original degree and exponent costs. |
| dependency | [Ideal norm counting](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Exact residue-degree weighting, ramification and normalized integer valuations. |
| dependency | [Residue Frobenius](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Existence of the residue lift and local degree decomposition at the checked scope. |
| dependency | [Finite fields](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Finite-field extensions, irreducible degrees and Frobenius at the checked scope. |
| support | [All-power endpoints](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Existence descent, power-degree preservation and endpoint reciprocity in the small-measure window. |
| support | [Rank-two bound](Yin_C_G0483_v1.md#independent-and-dependent-pairs) | Actual multiplicatively independent and dependent pairs at the fixed-rank comparison's scope. |
| support | [Prior coverage](Yin_C_G0483_v1.md#own-ratio-old-mass-proof) | Earlier residue-mass and multiplicatively independent rank-two estimates. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G0387_v2.md#ramification-matching-review) | Independent review of the local norm, quantitative inverse, prior comparisons and the finite-prime construction with arbitrarily large total measure. |
| review | [Independent bounded-coefficient construction](../audits/reviews/Yin_R_G0387_v3.md#finite-pool-finding) | Independent examination of the fixed-prime family, its Galois group, coefficient lift and both Mahler bounds. |

## Current assessment
[Selected decision](#decision-ramification-matching-reviewed)
