---
author: Yin
---

# Exact full entropy cost of a prescribed Mahler-value Perron root

This retains the full original2026-10-07 direct proof and its counterfamily, with the original source comparison kept separate.

## Statement

Let p be monic irreducible noncyclotomic reciprocal and a unit, of degree d=2r, with k roots strictly outside the circle.
Put beta=M(p)>1, h=m(p), let P_beta be its minimal polynomial and D its degree.
The real sign-corrected kth exterior power of the companion matrix is integral unimodular and has beta as its simple uniquely dominant positive eigenvalue, without squaring; its full entropy lies between h and binomial(d−1,k−1)h.
Among every integral matrix having the prescribed eigenvalue beta, the exact minimum logarithmic Mahler entropy is m(P_beta)=log M(M(p)); it is attained both by the companion and, using the stated neutral-repair interface, by a primitive nonnegative integral matrix with characteristic polynomial t^z P_beta c for a cyclotomic product c.
This minimum equals h precisely when beta is Pisot or Salem, and in 1<beta<theta0 precisely when beta is Salem.
If Omega is the Galois orbit of the expanding subset, different subsets give different products, D=cardinality(Omega), d divides kD and h<=m(P_beta)<=kD h/d, with D<=2^k binomial(r,k).
For every positive odd s the explicit independent quadratic-unit construction gives an irreducible reciprocal all-positive-power degree-preserving unit alpha of degree2^s with M(alpha)=alpha^c_s, c_s=binomial(s−1,(s−1)/2), and m(M(alpha))/m(alpha)=c_s tending to infinity.
This counterfamily has growing original measure and already has an original Perron root; it gives no near-one counterexample or failure of a differently prescribed entropy-preserving realization.
No uniform near-one estimate, sequential descent or unrestricted Mahler gap is proved.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:37 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible noncyclotomic reciprocal unit p of degree d=2r, k expanding conjugates, beta=M(p)>1 and D=degree(beta): sign-corrected exterior-power realization, exact prescribed-root minimum m(P_beta), attainment by primitive nonnegative neutral/zero completion, complete Pisot/Salem equality cases, exact orbit size and h<=m(P_beta)<=kD h/d with d dividing kD and D<=2^k binomial(r,k), plus the full odd multiquadratic all-power-preserving unbounded-inflation family outside the near-one range. |
| argument | [Argument](#argument) | Whole unique-max subset/exterior determinant and full-entropy bounds, irreducible divisor/neutral realization, reciprocal equality-case and Smyth specialization, orbit-product injectivity/root-incidence counting, independent quadratic-prime-support construction and majority-sign coefficient argument, with all prescribed-root and near-one nonimplications. |
| dependency | [Perron neutral realization](Yin_C_G0240_v1.md#perron-neutral-realization) | Actual strict Perron algebraic unit admits a primitive nonnegative integral realization after cyclotomic and optional zero padding; retains the original accepted statement-level KOR00 boundary. |
| dependency | [Accepted nonreciprocal bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only nonzero nonreciprocal algebraic-integer M>=theta0 for the equality-case exclusion; original Smyth proof remains accepted rather than newly audited. |
| support | [Original Perron-value comparison](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Existing direct positive Mahler-value implication and its exact convention; the complete needed product proof is also retained here. |
| support | [Mahler-iteration comparison](../audits/literature/FPZ20/Yin_U001.md#fpz20-u001) | Only the original Introduction/theorem-statement comparison and exact version/proof limits; no iteration classification or near-one estimate is imported. |
### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Adopt the exact complete retained statement and argument after the actual whole constructor self-check recorded in Yin_R_G0528_v1. All original mathematical hypotheses, source acceptance depths, native evidence and unresolved boundaries are retained. This is a present mathematical adoption, not certification of any original unknown isolation, an external-proof upgrade or a Task/E completion decision. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every monic irreducible noncyclotomic reciprocal unit p of degree d=2r, k expanding conjugates, beta=M(p)>1 and D=degree(beta): sign-corrected exterior-power realization, exact prescribed-root minimum m(P_beta), attainment by primitive nonnegative neutral/zero completion, complete Pisot/Salem equality cases, exact orbit size and h<=m(P_beta)<=kD h/d with d dividing kD and D<=2^k binomial(r,k), plus the full odd multiquadratic all-power-preserving unbounded-inflation family outside the near-one range. |
| argument | [Argument](#argument) | Whole unique-max subset/exterior determinant and full-entropy bounds, irreducible divisor/neutral realization, reciprocal equality-case and Smyth specialization, orbit-product injectivity/root-incidence counting, independent quadratic-prime-support construction and majority-sign coefficient argument, with all prescribed-root and near-one nonimplications. |
| dependency | [Perron neutral realization](Yin_C_G0240_v1.md#perron-neutral-realization) | Actual strict Perron algebraic unit admits a primitive nonnegative integral realization after cyclotomic and optional zero padding; retains the original accepted statement-level KOR00 boundary. |
| dependency | [Accepted nonreciprocal bound](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only nonzero nonreciprocal algebraic-integer M>=theta0 for the equality-case exclusion; original Smyth proof remains accepted rather than newly audited. |
| support | [Original Perron-value comparison](../audits/literature/Smy08/Yin_U003.md#smy08-u003) | Existing direct positive Mahler-value implication and its exact convention; the complete needed product proof is also retained here. |
| support | [Mahler-iteration comparison](../audits/literature/FPZ20/Yin_U001.md#fpz20-u001) | Only the original Introduction/theorem-statement comparison and exact version/proof limits; no iteration classification or near-one estimate is imported. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0528_v1.md#current-complete-prescribed-root-finding) | Complete current statement, entire retained argument and every actual needed input interface; constructor self-review, with original scopes and source/native limitations preserved. |

## Argument

### The exterior power gives the Perron value, not its entropy

Let `A` be the integral unimodular companion matrix of `p`, with distinct roots `alpha_1,...,alpha_d`.
Let `E` be the set of the `k` expanding roots.
The eigenvalues of `wedge^k A` are the products over all `k`-element subsets of roots.
The subset `E` uniquely maximizes their modulus: any other subset replaces at least one factor of modulus greater than one by a factor of modulus at most one.
Since `E` is closed under complex conjugation, its product is real and equals `sigma beta`, where `sigma` is 1 or −1.
Consequently

```
B=sigma wedge^k A
```

is an integral unimodular matrix with simple positive uniquely dominant eigenvalue `beta`.
It has dimension `binomial(d,k)` and `log spectral_radius(B)=h`.
Multiplication by the real sign leaves all eigenvalue moduli unchanged.
Passing to a square instead would double the logarithmic spectral radius and is not needed.

Write `x_i=log|alpha_i|`.
Its full algebraic entropy is instead

\[
m(\chi_B)=\sum_{|S|=k}\left(\sum_{i\in S}x_i\right)^+,
\]

which gives only the parameter-dependent bounds

\[
h\le m(\chi_B)\le {d-1\choose k-1}h.
\]

The upper bound counts each positive `x_i` in `binomial(d−1,k−1)` subsets.
Thus no entropy equality follows from the exterior-power spectral-radius identity.

<a id="prescribed-perron-entropy"></a>
### Arithmetic closure gives the exact optimal cost

The value `beta` is an algebraic unit, being a signed product of units.
Its conjugates are products of conjugates of `p`; the same unique-maximum argument shows that all other conjugates have modulus strictly less than `beta`.
Hence `P_beta` satisfies exactly the Perron hypothesis of L G0034.

For any integral matrix `C` with eigenvalue `beta`, its characteristic polynomial is divisible by the monic integer polynomial `P_beta`.
The quotient is monic integral, with nonnegative logarithmic Mahler measure.
Therefore

```
h_alg(C)=m(chi_C)>=m(P_beta).
```

The companion matrix attains this bound.
L G0034 also gives a primitive nonnegative integral matrix with characteristic polynomial `t^z P_beta c`, for a cyclotomic product `c`, attaining the same bound.
Its positive Perron root is still `beta`.
This proves both the lower bound and its attainability within the positive realization class.

Since `beta` itself is a root of `P_beta`,

```
m(P_beta)>=log(beta)=h.
```

Equality holds precisely when every other conjugate of `beta` has modulus at most one.
Because `beta>1` is a unit, it is not a positive rational integer.
If all other conjugates lie strictly inside the circle it is Pisot.
If a conjugate `gamma` lies on the circle, then its complex conjugate `gamma^(-1)` is also a root.
Thus `P_beta` and its reciprocal share a root, and irreducibility makes them equal up to sign.
The negative sign would force a root at 1, which is impossible for this irreducible polynomial, so `P_beta` is reciprocal.
Any contracting root has an expanding inverse; since `beta` is the only expanding root, the only contracting root is `beta^(-1)`.
All remaining roots lie on the circle, so `beta` is Salem.
Conversely both types give equality.
This is a direct equality-case argument, not an adoption of a Mahler-iteration classification.

To exclude the Pisot alternative when `beta<theta_0`, if its polynomial is nonreciprocal, the accepted Smyth bound at the exact locator above gives `beta=M(beta)>=theta_0`.
If its polynomial is reciprocal, the Pisot condition allows only `beta,beta^(-1)`, so its degree is two.
The integral trace `beta+beta^(-1)` is then at least three, giving `beta>=(3+sqrt(5))/2>theta_0`.
This uses no further least-Pisot source.

<a id="galois-orbit-cost"></a>
### Exact degree and expanding-count dependence

Let a Galois group `G` of a splitting field act on the root set, and let `Omega` be the orbit of the expanding subset `E`.
Different subsets in `Omega` give different products.
Indeed, if two such products agree, applying an automorphism taking the first subset back to `E` would give another `k`-subset with the same product as `E`, contradicting the unique maximal modulus unless the subsets agree.
Thus

```
D=|Omega|.
```

Transitivity on the `d` roots implies each root appears in exactly `kD/d` subsets of `Omega`.
In particular this number is an integer.
The same positive-part bound, now restricted to this exact Galois orbit, gives

\[
\boxed{h\le m(P_\beta)\le\frac{kD}{d}h,
\qquad d\mid kD.}
\]

Reciprocity further bounds

\[
D\le 2^k {r\choose k},\qquad r=d/2.
\]

There are `r` inverse pairs.
The expanding set takes at most one root from each pair, and every Galois image retains that property; choose the `k` pairs and one root from each.
This argument does not assume that a single Galois element simultaneously inverts every root, which need not hold.
For `k=1` the bound gives equality of entropies.
For unrestricted degree and expanding count its coefficient is not uniformly bounded.

<a id="unbounded-iteration-inflation"></a>
### An actual unbounded inflation family, outside the near-one range

The coefficient dependence cannot be replaced by a universal constant over all reciprocal units, even if they have all-power degree preservation.
Here is a direct construction, avoiding a numerical root or Galois-group scan.

Take any positive odd integer `s`.
Choose real quadratic norm-one units `u_i>1` in independent quadratic fields, `1<=i<=s`.
One explicit supply is: set `r_1=1`; recursively choose a positive integer `r_i` divisible by all earlier square-free parts `d_j` of `r_j^2+1`, and let `d_i` be the square-free part of `r_i^2+1`.
It is greater than one and coprime to all previous `d_j`.
Then

```
u_i=(r_i+sqrt(r_i^2+1))^2
```

has norm one in `Q(sqrt(d_i))`.
The pairwise disjoint prime supports give a multiquadratic compositum with Galois group `(C_2)^s`.

Choose `T>s max_i log u_i`, and put

```
m_i=floor(T/log u_i),   a_i=m_i log u_i,
alpha=product_i u_i^(m_i).
```

The `2^s` conjugates are the distinct positive numbers `alpha_epsilon=product_i u_i^(epsilon_i m_i)`, for signs `epsilon_i`.
To see distinctness, a relation between two such products can be conjugated by the automorphism inverting only `u_j`; dividing the two relations forces equality of the `j`th exponents.
Thus `alpha` has degree `2^s`.
Its minimal polynomial is reciprocal and a unit polynomial.
All its positive powers retain this degree because its positive distinct conjugates remain distinct under every positive integer power.

Writing `A=max_i log u_i`, one has `T−A<a_i<=T`.
Since `s` is odd and `T>sA`, the sign of `sum epsilon_i a_i` is the sign of `sum epsilon_i`.
Consequently the expanding conjugates are exactly those with a strict majority of plus signs.
For each coordinate, summing its sign over those conjugates gives

```
c_s=binomial(s−1,(s−1)/2).
```

This follows by pairing configurations with that coordinate changed: the unmatched configurations have a tie among the remaining `s−1` signs.
Therefore

\[
M(\alpha)=\alpha^{c_s},\qquad
\frac{\log M(M(\alpha))}{\log M(\alpha)}=c_s\longrightarrow\infty.
\]

The second equality uses degree preservation under powers, so that `m(alpha^(c_s))=c_s m(alpha)`.
These are irreducible reciprocal units with a proved unbounded first-iterate inflation factor.
Their original Mahler measures grow; they do not provide a bounded-small-measure or near-one counterexample.
They are already Perron units, so an algorithm permitted to keep their original Perron root can avoid this unnecessary conversion.
The obstruction specifically concerns prescribing `M(p)` as the new Perron root.

### What is missing for the small-Mahler core

The proposed conversion is a legitimate Perron realization but is not an entropy-preserving extension of L G0034 to arbitrary inputs.
A useful replacement would have to establish, on the relevant reciprocal-unit class, a parameter-uniform estimate such as

```
m(P_(M(p)))<=C m(p),
```

or at least the sequential implication

```
m(p_j)->0  implies  m(P_(M(p_j)))->0.
```

Neither follows from the exterior-power construction, the neutral repair, or the sources inspected here.
The counterfamily excludes a global constant but does not decide either statement restricted sufficiently near one.
Such a near-one assertion must retain its quantifiers: if the Lehmer gap already holds, it can be vacuous below that gap.
It is not a proved arithmetic descent merely because `M(p)` is Perron.

An exact prescribed-root descent in the small core would require proving that the Mahler value is itself Salem.
No such coverage theorem is adopted.
The unrestricted positive-realization existence and its net-trace repair can therefore be used only after this first-iterate entropy cost is paid or independently controlled.
