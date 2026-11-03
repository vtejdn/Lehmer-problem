---
author: Yin
---

# Complete original-law parity carries, all Renyi rates and conditional-information limits

The complete original L219 Sections 1--6/(1)--(18) are retained with their original probabilities, all negative-floor and overlapping-boundary cases, actual torsion/positive controls and finite costs.
The original [R793 whole](../audits/reviews/Yin_R_G0793_v1.md#parity-carry-complete-independent-review) inspected that frozen proof on 2026-10-09T21:09 after its 21:06 freeze.
Its statement that a prior author summary was available does not identify that summary's mathematical content or initial inspection order; the missing relationship declaration is not rewritten as an explicit unknown row or inferred independence/self-review.

## Statement

<a id="parity-carry-fixed-scope"></a>

Let alpha be any algebraic unit, including torsion, with actual monic minimal polynomial P(t)=sum_(i=0)^d p_i t^i, p_d=1 and p_0 in {-1,1}.
For two-sided iid fair bits xi_j define, for every j in Z,
\[
Y_j=\sum_{i=0}^d p_i\xi_{j-i},\quad
\sigma_j=Y_j\bmod2\in\{0,1\},\quad
C_j=(Y_j-\sigma_j)/2=\lfloor Y_j/2\rfloor.
\]
Then sigma is the complete iid fair binary process, not independent of xi in general.
C is a stationary finite-alphabet process of memory d with |C_j|<=(||P||_1+1)/2.
For every integer n>=1, every finite endpoint sum indexed j<n below means j=0,...,n-1; put S_n=sum_(j<n)sigma_j alpha^j and T_n=sum_(j<n)C_j alpha^j.
With
\[
B_n=\sum_{i=0}^d p_i\alpha^i
\left[\sum_{u=-i}^{-1}\xi_u\alpha^u-
      \sum_{u=n-i}^{n-1}\xi_u\alpha^u\right],
\quad E_n=(\xi_u:u\in[-d,-1]\cup[n-d,n-1]),
\]
where repeated indices occur only once and empty sums vanish, S_n+2T_n=B_n.
This includes n<d and overlapping boundary ranges.
The joint laws of (S_n,E_n) and (T_n,E_n) have the same probability masses, and
\[
H(T_n|E_n)=H(S_n|E_n),\quad
H(T_n)-H(S_n)=I(T_n;E_n)-I(S_n;E_n).
\]
For every Renyi order a in [0,infinity], including support, Shannon and min-entropy conventions,
|H_a(T_n)-H_a(S_n)|<=2d log2.
Every fixed-input endpoint rate exists and agrees with the original iid binary rate; no varying-degree loss 2d log2/n is suppressed.

Let Q_j=sum_(i=1)^d p_i xi_(j-i), a_j=floor(Q_j/2), b_j=Q_j mod2 and M_j=(1-p_0)/2+p_0 b_j.
The exact rule is C_j=a_j+p_0 M_j xi_j.
M is iid Bernoulli(1/2) and measurable in the full past F_(j-1), while xi_j is independent of that past.
The averaged conditional entropy is H(C_j|F_(j-1))=(log2)/2; at a realized past it equals M_j log2.
The carry need not be iid:
\[
(n/2)\log2\le H(C_0,\ldots,C_{n-1})\le(n+d)\log2,
\quad
H(C_0,\ldots,C_{n-1}|T_n)\ge(n/2)\log2-H(S_n)-2d\log2 .
\]
The corresponding fixed-input redundancy rate is the symbolic carry rate minus the original Shannon rate h_1, and is at least (log2)/2-h_1.

Writing epsilon_j=1-2xi_j, eta_j=1-2sigma_j and S={i:p_i odd},
\[
\eta_j=\prod_{i\in S}\epsilon_{j-i},\quad
\mu_C=(P(1)-1)/4,\quad
C_j-\mu_C=-\tfrac14\sum_i p_i\epsilon_{j-i}+\tfrac14\eta_j .
\]
With coefficients outside 0,...,d zero,
\[
\operatorname{Cov}(C_0,C_h)=\tfrac1{16}
(\sum_i p_i p_{i+h}+1_{h=0}),\quad
\operatorname{Cov}(\xi_0,C_h)=p_h/8.
\]
The covariance series f_C(theta)=(1+|P(e^(i theta))|^2)/16 and the input/carry two-by-two covariance determinant is 1/64 at every theta.
For every unit-circle root beta of P, with D_P=2sum_i i|p_i|,
\[
n/16\le E|\sum_{j<n}(C_j-\mu_C)\beta^j|^2
 \le n/16+D_P^2/16.
\]
No discrete entropy bound or independence is inferred from these covariance identities.

For d a power of two and alpha a primitive 2d-th root, P=t^d+1, C_j=xi_j xi_(j-d), M_j=xi_(j-d), and M_(j+d)=xi_j.
These actual inputs have zero endpoint rates despite the same positive local innovation, arbitrarily long degree-sized free windows and iid predictable mask.
The future full mask reveals the whole input; the independent summand-selection premise of the thinning theorem is absent.
For alpha=phi with P=t^2-t-1, C_j=-majority(xi_j,xi_(j-1),1-xi_(j-2)), Cov(C_0,C_2)=-1/16 and the original/carry collision rates are positive.
The radical controls t^(2r)-t^r-1 with r a power of two retain their actual degrees and fixed M=phi and supply no near-one reciprocal family.

For adjacent blocks of positive lengths n,m, writing T'_m=sum_(j<m)C_(n+j)alpha^j,
\[
I(T_n;T'_m)\le d\log2,\quad
D(\mathcal L(T_n+\alpha^nT'_m)\|
 \mathcal L(T_n)*\mathcal L(\alpha^nT'_m))\le d\log2.
\]
The convolution uses independent marginal copies.
The exact boundary seam is B_(n+m)(xi)=B_n(xi)+alpha^n B_m(shift^n xi).
These statements give no two-sided collision comparison or positive fraction of local information surviving algebraic summation.
Every degree, memory, coefficient and chronological cost remains explicit; no uniform growth floor or Mahler gap is proved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:05 |
| status | open |
| reason | Register the exact complete statement and every necessary original argument, with genuine author, source, finite-evidence and failure boundaries. Current whole mathematical inspection and adoption are separate actual acts; no old review is backfilled with this C input and no research execution is resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit including torsion; complete iid parity output, exact positive-power carry/boundary bijections, all Renyi endpoint rates and finite2d costs, actual iid predictable mask and symbolic redundancy, all signed lag/covariance formulas and beta-window bounds, both actual controls and precise adjacent-block seam/relative-entropy limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/formulas(1)--(18), every finite-rank/floor/boundary/Renyi case, both p0 signs, finite-memory Walsh and conditional sigma-fields, exact torsion/positive/radical controls, and finite same-law seam proof with all negative information-transfer limits. |
| support | [Fixed actual affine controls](Yin_C_G0522_v1.md#statement) | Exact torsion, golden-ratio and radical original-law growth/control inputs only; not a uniform near-one lower rate. |
| support | [Independent thinning boundary](Yin_C_G0282_v1.md#statement) | Only actual independent external summand selection; no conditioning on the dependent predictable carry mask. |
| support | [Finite-memory Walsh context](Yin_C_G0326_v1.md#statement) | Comparison to original finite-memory symbolic/endpoint and covariance distinctions; current explicit parity/Walsh calculation is complete locally. |
| support | [Actual radical-family identity](Yin_C_G0212_v1.md#statement) | Exact high-degree t^(2r)-t^r-1 controls with fixed M=phi; no near-one or reciprocal extension. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:21 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire retained argument after the actual whole SELF inspection recorded in R735. Every used mathematical dependency is resolved at its explicit scope, the complete original proof and necessary source/native/failure facts are retained, and no unresolved mathematical issue affects this restricted theorem. The old whole review retains its missing declaration and unestablished initial context; this current SELF neither creates independent evidence nor closes M04 or any research Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit including torsion; complete iid parity output, exact positive-power carry/boundary bijections, all Renyi endpoint rates and finite2d costs, actual iid predictable mask and symbolic redundancy, all signed lag/covariance formulas and beta-window bounds, both actual controls and precise adjacent-block seam/relative-entropy limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/formulas(1)--(18), every finite-rank/floor/boundary/Renyi case, both p0 signs, finite-memory Walsh and conditional sigma-fields, exact torsion/positive/radical controls, and finite same-law seam proof with all negative information-transfer limits. |
| support | [Fixed actual affine controls](Yin_C_G0522_v1.md#statement) | Exact torsion, golden-ratio and radical original-law growth/control inputs only; not a uniform near-one lower rate. |
| support | [Independent thinning boundary](Yin_C_G0282_v1.md#statement) | Only actual independent external summand selection; no conditioning on the dependent predictable carry mask. |
| support | [Finite-memory Walsh context](Yin_C_G0326_v1.md#statement) | Comparison to original finite-memory symbolic/endpoint and covariance distinctions; current explicit parity/Walsh calculation is complete locally. |
| support | [Actual radical-family identity](Yin_C_G0212_v1.md#statement) | Exact high-degree t^(2r)-t^r-1 controls with fixed M=phi; no near-one or reciprocal extension. |
| review | [Actual current whole SELF](../audits/reviews/Yin_R_G0735_v1.md#current-g219-whole-self-finding) | Entire exact current statement and complete argument with every explicit domain, input interface, full mathematical proof, source/native/control scope and limitation inspected at this current C; actual SELF, not a retrospective old review or isolated replacement. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:48 |
| status | proved |
| reason | Adopt the entire exact current Statement and complete retained Argument after the actual independently reviewed whole finding in R793. All eight batch initial conclusions preceded every old target finding and Assessment. Necessary inputs are resolved at their exact fixed scopes, original mathematical and evidence/source/failure/negative history is retained, and no unresolved issue affects this restricted result. This is a new actual current adoption, with no old relationship or binding backfill and no Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | Any actual algebraic unit including torsion; complete iid parity output, exact positive-power carry/boundary bijections, all Renyi endpoint rates and finite2d costs, actual iid predictable mask and symbolic redundancy, all signed lag/covariance formulas and beta-window bounds, both actual controls and precise adjacent-block seam/relative-entropy limits. |
| argument | [Complete argument](#argument) | Entire original Sections1--6/formulas(1)--(18), every finite-rank/floor/boundary/Renyi case, both p0 signs, finite-memory Walsh and conditional sigma-fields, exact torsion/positive/radical controls, and finite same-law seam proof with all negative information-transfer limits. |
| support | [Fixed actual affine controls](Yin_C_G0522_v1.md#statement) | Exact torsion, golden-ratio and radical original-law growth/control inputs only; not a uniform near-one lower rate. |
| support | [Independent thinning boundary](Yin_C_G0282_v1.md#statement) | Only actual independent external summand selection; no conditioning on the dependent predictable carry mask. |
| support | [Finite-memory Walsh context](Yin_C_G0326_v1.md#statement) | Comparison to original finite-memory symbolic/endpoint and covariance distinctions; current explicit parity/Walsh calculation is complete locally. |
| support | [Actual radical-family identity](Yin_C_G0212_v1.md#statement) | Exact high-degree t^(2r)-t^r-1 controls with fixed M=phi; no near-one or reciprocal extension. |
| review | [Actual current whole independent finding](../audits/reviews/Yin_R_G0793_v1.md#parity-carry-current-independent) | Entire exact current Statement and complete Argument, with every actual domain, fixed mathematical interface, complete proof, finite/source/failure/control boundary and cost; true isolated initial mathematical conclusion 2026-10-22T21:34, followed by old-scope comparison, without rewriting historical relations or resuming research. |

## Complete argument

<a id="argument"></a>

### Reuse, definitions and the changed target

[L215's exact matching and original-law comparison](Yin_C_G0522_v1.md#growth-defect-fixed-scope) distinguishes persistent finite-block strictness from new information across scales.
The author also read the exact original-binary increment and overlap mechanism in [L92](Yin_C_G0283_v1.md#binary-increment-js-divergence), the generic inverse-rank/time obstruction in [L93](Yin_C_G0286_v1.md#power-orbit-inverse-time-cost), and the finite-memory linear/nonlinear distinctions in [L121](Yin_C_G0326_v1.md#nonlinear-finite-memory-central-dichotomy) and [L124](Yin_C_G0329_v1.md#original-input-boundary-entropy-cost).
A bounded local search did not find the particular parity representation below.
No novelty or external theorem is claimed.

This round does not optimize L215's matching constant.
It retains exact lags through a polynomial filter whose parity output has the COMPLETE original iid law.
Its integer carry process is dependent, and is not substituted for iid digits without the exact endpoint identity and boundary cost.
The representation preserves the actual endpoint entropy rates; its fresh local randomness is then tested against real algebraic torsion controls.
This supplies a controlled algebraic redundancy mechanism and an explicit missing independence condition, rather than a positive growth exponent.

Let alpha be any algebraic unit, including torsion, with monic minimal polynomial

    P(t)=sum_(i=0)^d p_i t^i,   p_d=1,   p_0 in{-1,1}.

Let xi_j, j in Z, be independent fair bits.
Define the causal integer filter, its parity bit and its integer carry by

    Y_j=sum_(i=0)^d p_i xi_(j-i),
    sigma_j=Y_j mod2 in{0,1},
    C_j=(Y_j-sigma_j)/2=floor(Y_j/2).                  (1)

The floor identity applies also when Y_j is negative.
The carry alphabet is finite, with |C_j|<=(||P||_1+1)/2, and its memory is d.
Throughout, logarithms are natural.
The name carry refers only to this exact integer division by2; it is not a Markov carry state or a return-core stationary law.
The actual nonsymmetric affine generators remain x -> alpha x and x -> alpha x+1 in fixed dimension2.
The coordinator proposed the broad continuation question and supplied no derivation below.

<a id="parity-filter-original-iid-law"></a>
### 1. The parity output is exactly the original iid binary process

For every finite set of distinct indices j_1,...,j_n, the vector (sigma_(j_1)...,sigma_(j_n)) is uniform on F_2^n.
Here is a finite proof, so no infinite-product surjectivity theorem is needed.
A nonempty F_2-linear combination of those outputs corresponds to multiplying the nonzero Laurent polynomial sum_a t^(j_a) by the nonzero Laurent polynomial sum_(i:p_i odd) t^(-i).
Their product is nonzero because F_2[t,t^(-1)] has no zero divisors.
Thus the selected linear output functionals are independent on the finitely many input bits they use.
The resulting linear map has full row rank n, and its uniform input has a uniform output with exactly equal fiber sizes.

Consequently sigma is an iid fair binary process, not merely pairwise independent or a process with the same marginal.
This assertion is independent of P(alpha)=0; that equation enters the actual endpoint identity next.
Original probabilities are unchanged: every length-n sigma word has probability2^(-n).
The output sigma is not claimed independent of the input xi; they are deterministically coupled.

<a id="parity-carry-exact-endpoint-information"></a>
### 2. Exact conditional endpoint information and all Renyi costs

Put

    S_n=sum_(j=0)^(n-1) sigma_j alpha^j,
    T_n=sum_(j=0)^(n-1) C_j alpha^j.

S_n has exactly the original binary endpoint distribution.
Directly reindexing the filter in(1), in the positive-power convention actually used here, gives

    S_n+2T_n=B_n,
    B_n=sum_(i=0)^d p_i alpha^i [
             sum_(u=-i)^(-1) xi_u alpha^u
               -sum_(u=n-i)^(n-1) xi_u alpha^u].       (2)

The omitted main term is P(alpha) sum_(u=0)^(n-1) xi_u alpha^u=0.
Negative powers are legitimate because alpha is a nonzero unit.
Empty sums vanish; when n<d the two displayed boundary ranges can overlap and cancel, and the identity remains valid.
No reciprocal assumption or reversal of a dependent process is used.

Let E_n be the vector of input bits with indices in

    {-d,...,-1} union {n-d,...,n-1}.

It has at most2d distinct entries and at most M_n=2^(2d) possible values.
B_n is a deterministic function of E_n.
For each realized E_n, multiplication by-2 and translation by B_n identify the two endpoint variables bijectively.
Hence the exact Shannon identity is

    H(T_n|E_n)=H(S_n|E_n),
    H(T_n)-H(S_n)=I(T_n;E_n)-I(S_n;E_n).              (3)

There is no independence assertion between the boundary and either endpoint.
The difference in(3) can have either sign; both terms on its right are at most2d log2.

More generally, for EVERY Renyi order a in[0,infinity], including support entropy at a=0, Shannon entropy at a=1 and min-entropy at infinity,

    |H_a(T_n)-H_a(S_n)|<=2d log2.                     (4)

For completeness, if E has at most M values, marginalizing a finite joint law obeys

    H_a(X)<=H_a(X,E)<=H_a(X)+log M.

For a>1 this follows from sum_e w_e^a<=(sum_e w_e)^a<=M^(a-1)sum_e w_e^a, with the sign of1/(1-a) retained.
For0<a<1 the concave inequalities give the same entropy conclusion.
The support and maximum-atom cases are direct, and the Shannon case is the conditional-entropy bound.
The joint laws (S_n,E_n) and (T_n,E_n) have exactly the same probability masses by their bijection, so their marginal entropies lie in the same interval of width log M_n.
This proves(4), not a doubled boundary charge.
In particular the two collision probabilities differ by at most the factor2^(2d) in either direction.

The original iid endpoint Renyi entropies are subadditive in n: independent sums can be grouped by their common output, and the same power-sum inequalities give H_a(X+Y)<=H_a(X)+H_a(Y); translation and multiplication by alpha^n preserve finite distributions.
The Shannon and endpoint orders satisfy the familiar direct versions.
Thus their rates exist by the elementary subadditive limit argument.
For every FIXED alpha, (4) proves that the dependent carry endpoints have exactly the same rate at every order.
This includes the original support-growth, Shannon and collision rates.

For varying inputs the normalized loss is explicitly2d log2/n.
It is not negligible at n comparable to d, and no such limit is interchanged.
Equation(3), rather than an assumed beneficial boundary term, is the exact information comparison available at a finite time.

<a id="predictable-iid-carry-innovation-mask"></a>
### 3. A predictable iid mask with exactly half a bit of fresh local information

Write

    Q_j=sum_(i=1)^d p_i xi_(j-i),
    a_j=floor(Q_j/2),    b_j=Q_j mod2,
    M_j=(1-p_0)/2+p_0 b_j in{0,1}.

The floor in(1) gives the exact pointwise update

    C_j=a_j+p_0 M_j xi_j.                            (5)

If p_0=1, M_j is the parity b_j; if p_0=-1, it is1-b_j.
These formulas follow by separately putting Q_j=2a_j or2a_j+1, and retain negative Q_j.
The sigma-field F_(j-1) generated by all xi_i with i<=j-1 determines a_j and M_j.
The bit xi_j is independent of it.
Conditional on a realized past, C_j is deterministic if M_j=0 and takes two equiprobable distinct values if M_j=1.

The mask process M itself is iid Bernoulli(1/2).
Indeed the parity filter for b_j has nonzero polynomial sum_(i>=1:p_i odd) t^(-i), since p_d=1.
The same finite-rank proof as Section1 gives its full iid law; a fixed bit complement preserves it.
In particular

    H(C_j|F_(j-1))=(log2)/2.                          (6)

Here the displayed conditional entropy includes expectation over the past; at a realized past its value is M_j log2.
This is actual fresh local randomness at a fixed positive density, and its constant has no degree dependence.

It does NOT make the carry process iid.
For its symbolic block one has only the bounds

    (n/2)log2 <= H(C_0,...,C_(n-1)) <=(n+d)log2.       (7)

For the lower bound, the previous carry values are measurable with respect to F_(j-1), so conditioning on that full past can only reduce entropy; sum(6) by the chain rule.
For the upper bound, the block is determined by n+d input bits.
The stationary finite-alphabet carry process therefore has a symbolic entropy rate in[(log2)/2,log2].
This is a rate of whole symbolic blocks, not their algebraic endpoints.

The distinction can be quantified using the actual endpoint.
Since T_n is a function of the carry block, (3)--(7) give

    H(C_0,...,C_(n-1)|T_n)
       >= (n/2)log2-H(S_n)-2d log2.                  (8)

At fixed input, the conditional-entropy rate is the symbolic carry rate minus the original binary Shannon rate h_1.
In particular it is at least(log2)/2-h_1.
The retained upper comparison h_1<=m makes this at least(log2)/2-m if that comparison is desired.
This is a lower bound on redundancy, not a lower bound on growth, and it uses no Mahler gap.
Along a hypothetical near-one family it identifies the extensive information which an endpoint-growth argument would still have to recover; the generic inequality alone does not recover it.

<a id="actual-carry-lag-spectrum-and-polynomial"></a>
### 4. Exact lag data recover P, while white covariance is not independence

Put epsilon_j=1-2xi_j and S={i:p_i is odd}.
Both0 and d belong to S, so |S|>=2.
The parity sign is

    eta_j=1-2sigma_j=product_(i in S) epsilon_(j-i).

By Section1 the process eta is iid fair signs.
Nevertheless eta is a deterministic nonlinear function of the entire input epsilon.
Direct expansion gives

    mu_C=E C_j=(P(1)-1)/4,
    C_j-mu_C=-(1/4)sum_i p_i epsilon_(j-i)+(1/4)eta_j. (9)

Every eta_j is orthogonal in L2 to every individual epsilon_h, since the associated Walsh product has at least two distinct input positions.
The shifted eta variables are orthogonal, indeed independent by their already proved parity law.
Thus all lags are explicit:

    Cov(C_0,C_h)=(1/16)[sum_i p_i p_(i+h)+1_(h=0)],
    Cov(xi_0,C_h)=p_h/8.                              (10)

Coefficients outside0,...,d are zero.
The second identity recovers the signed actual polynomial coefficients from the input-carry cross-lags; maximizing a matching statistic as in L215 would discard this information.

For clarity the covariance Fourier series is defined here by summing the finite lag sequence against exp(i h theta).
Formula(10) yields

    f_C(theta)=[1+|P(exp(i theta))|^2]/16.              (11)

The input covariance series is1/4, and the cross-series is P(exp(i theta))/8 with its conjugate in the opposite entry.
Their two-by-two covariance matrix has determinant exactly1/64 at every theta.
This follows by direct multiplication; it does not assert independence, Gaussianity or an entropy formula for these discrete processes.

At every unit-circle root beta of P, (11) has the universal value1/16.
One can see the finite-window cost without any spectral limit.
For the centered carry sum at beta, (9) and orthogonality give

    E|sum_(j=0)^(n-1)(C_j-mu_C) beta^j|^2
       =n/16+(1/16)E|sum_(j=0)^(n-1)
                         sum_i p_i epsilon_(j-i) beta^j|^2.

The last double sum is the boundary in(2) with xi replaced by epsilon, because P(beta)=0.
Consequently, with D_P=2 sum_i i|p_i|,

    n/16 <= E|sum_(j<n)(C_j-mu_C) beta^j|^2
                  <= n/16+D_P^2/16.                 (12)

No mean-zero assumption about the uncentered carry is inserted.
These exact covariance statements are consistent with the general finite-memory Walsh analysis in L121; the new feature is the original-iid parity output and the explicit single nonlinear shape in(9).
A uniform positive covariance innovation, even together with the actual coefficient cross-lags, is not yet a proved entropy-growth inequality.

<a id="iid-predictable-mask-dependent-selection-control"></a>
### 5. Actual high-degree controls expose the missing thinning condition

Take d a power of two and alpha a primitive2d-th root of unity, whose actual minimal polynomial is P=t^d+1.
Section1 gives the original iid parity process

    sigma_j=xi_j XOR xi_(j-d),
    C_j=xi_j xi_(j-d),    M_j=xi_(j-d).                (13)

The carry is the AND of two actual fair bits.
Its mask M is iid, is determined by the past, and is independent of the current bit xi_j at every individual time.
Every conclusion(2)--(12) applies, including the degree-free fresh local information(log2)/2 and the positive flat nonlinear covariance term.

Yet the original affine growth and every endpoint entropy rate are zero.
There are only2d possible powers of alpha, so length-n endpoints have at most(n+1)^(2d) values; Section2 transfers the zero rates to the carry endpoints.
The first d binary powers remain linearly independent, giving the already retained arbitrarily long free initial windows.
These are actual fixed-dimension affine inputs, not finite-quotient surrogates.

The precise independence failure is visible without an entropy estimate:

    M_(j+d)=xi_j.                                    (14)

Thus the future mask reveals each selected or unselected input bit.
Knowing the mask vector from d through n-1+d reconstructs the entire input block xi_0,...,xi_(n-1).
It is false that conditioning on the whole selection mask leaves independent fair bits at its selected positions, despite predictability, its iid law and its independence from the current bit.
In particular the independent-mask hypothesis of [L90's thinning estimate](Yin_C_G0282_v1.md#sharp-thinning-laplace-bound) is absent.
This is a verified failure of that proposed transfer, not a failure of the retained thinning theorem.

For an explicit positive-growth comparison, take phi with P=t^2-t-1.
The rule is

    C_j=-majority(xi_j,xi_(j-1),1-xi_(j-2)),          (15)

where majority of three bits is1 when at least two are1.
Indeed Y_j=xi_(j-2)-xi_(j-1)-xi_j, and floor(Y_j/2) is-1 exactly when xi_j+xi_(j-1)-xi_(j-2)>=1.
The marginal of C_j is uniform on{-1,0}, but the process is dependent: (10) gives Cov(C_0,C_2)=-1/16.
It has the same local conditional information(log2)/2 as the torsion examples.
The original binary collision rate at phi is positive directly because conditioning on odd positions leaves distinct sums in powers of phi squared greater than2, as in L215.
By(4) the dependent majority carry endpoints have the same positive collision rate.
No assertion that the carry digits themselves are independent is used.

If an unbounded-degree positive control is wanted, the actual minimal polynomials t^(2r)-t^r-1 for r a power of two are the fully verified radical family in L215/L5.
Their carry rule replaces lags1,2 in(15) by r,2r.
Their original rates remain positive by the exact relative-field product, and Section2 transfers them.
Their M is fixed at phi, so they do not refute or prove a near-one reciprocal statement.
The torsion and positive controls establish that the universal local innovation and covariance properties above do not by themselves distinguish asymptotic growth.

### 6. Conditional seams and the exact next obligation

There is a useful bound on what dependence between adjacent carry blocks costs, but it does not repair the independence failure.
For adjacent blocks of lengths n,m, the enclosing input intervals overlap in exactly the d bits xi_(n-d)...,xi_(n-1).
Given this vector E_mid the two carry blocks, and hence their two algebraic endpoints, are conditionally independent: their remaining input coordinates are disjoint independent sets.
Therefore

    I(T_n; T'_m)<=H(E_mid)<=d log2,                  (16)

where T'_m=sum_(j=0)^(m-1) C_(n+j) alpha^j.
For the first inequality use the Markov chain through E_mid, or the chain rule and conditional independence.
Applying data processing to addition also gives

    D(law(T_n+alpha^n T'_m)
        || law(T_n)*law(alpha^n T'_m))<=d log2.        (17)

The convolution on the right uses independent copies of the two marginal laws; it is not silently identified with the actual left law.
These finite laws have well-defined relative entropy since every actual joint atom lies in the support of the product marginals.
The bound in(17) is the data processing of D(joint||product)=I, and gives no two-sided pointwise or collision-probability comparison.

The original filter boundaries in(2) also cancel exactly at a seam:

    B_(n+m)(xi)=B_n(xi)+alpha^n B_m(shift^n xi).       (18)

Here (shift^n xi)_j=xi_(j+n); the identity follows either by canceling the displayed interior terms or by additivity of the filtered partial sum.
The outer boundary is paid once.
This equality does not make the two endpoint information terms in(3) additive, nonnegative or independent.

The new usable representation therefore retains the COMPLETE original binary distribution in sigma, all endpoint rates in the dependent integer carry, the actual signed polynomial through cross-lags, and the precise conditional boundary/seam charges.
It supplies a concrete way to formulate a next test: control how much of the carry's fresh local information survives algebraic summation after conditioning only on information actually available at that scale, without revealing the future mask.
One may seek a lag-sensitive integral recurrence criterion or a conditional information inequality that separates nontorsion near-one inputs from(13), but either requires proof and quantitative degree, memory, coefficient and time costs.
No such positive survival estimate is asserted here.

Merely importing independent thinning, adding the constant in(6) over time to bound H(T_n), using the positive spectral density in(11) as an entropy lower bound, or repeating an O(d) boundary charge would be invalid.
L93's generic rank/time limitation remains applicable, and L121/L124's local-rule variance and concentration bounds do not provide the missing endpoint survival.
The present parity representation preserves the rate rather than improving it.

### Original author check and scope

The [complete original author checking/evidence account](../audits/reviews/Yin_R_G0735_v1.md#original-g219-author-self-finding) retains its actual original input, recorded precision and scope, separately from the current whole SELF finding.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0793_v1.md#parity-carry-complete-independent-review), with its original inspected scope and relationship.
