---
author: Yin
---
# Logarithmic Wiener expense of the universal positive projection symbol

Human author Yin.
Root supplied the exact-value and positive-symbol assembly from the accepted L321/C145 projection formulas.
The cross_term_reuse agent supplied the logarithmic Wiener lower bound, the absolute-convergence justification and the explicit cubic certificate.
Both are contributors and neither can independently review this whole account.
The new deductions were developed in D38 under the continuing G0001 authority.
The universal projection, its Laurent factorization and its radial/contact estimates are reused results, not new constructions or a new Mahler gap.
No numerical computation is used.

## Statement

Let P be a monic irreducible nontorsion polynomial in Z[t], with constant coefficient +/-1 and degree d>=2.
Put N=2d and T=N-1.
Let A_rel be the N-by-d matrix of full coefficient columns of P,tP,...,t^(d-1)P, and define

    R=I_N-A_rel(A_rel^t A_rel)^(-1)A_rel^t,
    v_N(t)=(1,t,...,t^T)^t,
    k(t)=N^(-1)v_N(t^(-1))^t R v_N(t),
    a_n=sum_(j=0)^(N-1-n) R_(j,j+n),
    kappa_R=(2/d)sum_(n=1)^(N-1)|a_n|.

The matrix is the actual rational rank-d residual projection.
Off the unit circle k is evaluated as the displayed rational Laurent polynomial, not as a Hermitian form.
On the unit circle let h=log(1+k), and write hhat(n) for its normalized Fourier coefficients and W_*(h)=sum_(n!=0)|hhat(n)|.
The following conclusions hold.

1. The Fourier coefficients of h are absolutely summable and

       W_*(h)>=log(1+kappa_R/3).                       (1)

   Applying the accepted C143 construction gives actual monic irreducible reciprocal nontorsion integer units of degrees d=(ell+3)/2, for arbitrarily large primes ell congruent 1 modulo 4, with

       W_*(h)>=log[1+(sqrt(ell)-4)/6].                 (2)

   Hence no bound on W_*(h) uniform over all original inputs follows from this projection construction, even though 0<=h<=log2.
   The C143 inputs have total Mahler measure at least log2 and growing scale; (2) is not a counterexample in a near-one regime and is not a sharp growth-rate assertion.

2. Let Q>=1 be any positive integer clearing the rational coefficients of 1+k and put

       A(t)=Q t^T(1+k(t)) in Z[t],
       f(t)=A(t)/(2Q)=t^T(1+k(t))/2.

   For every original root alpha_i,

       f(alpha_i)=alpha_i^T,
       1/2<=|f(z)|<=1 on |z|=1,
       m(f)<=-gamma,       gamma=log(4/3)>0,
       ||f||_1=(3+kappa_R)/4,
       deg A<=4d-2,
       Res(P,A)=(2Q)^d Norm_(Q(alpha)/Q)(alpha)^T,
       |Res(P,A)|=(2Q)^d.                             (3)

   Thus the original value is an actual integral unit, and every original embedding, coefficient and scalar denominator is retained.
   In particular the actual normalized coefficient-l1 norm in (3) is unbounded on the C143 family.

3. Put u=1-k and define the real Laurent polynomial

       G_3=log2-u/2-u^2/8-u^3/24.

   Then

       0<=G_3-h<=1/32<gamma/8 on the circle,
       G_3(alpha_i)=log2 for every original i,
       degree_Laurent(G_3)<=3(2d-1),
       integral G_3<=log(3/2)+1/32.                  (4)

   All nonconstant coefficients of G_3 are rational; the only possibly nonrational coefficient is the constant containing log2.
   The displayed original values are polynomial evaluations, not an algebraic norm or resultant claim for G_3.
   Fixed scalar degree three does not imply a bounded expanded Fourier coefficient norm.

The reused setup additionally has k(alpha_i)=1, 0<=k<=1 and integral k=1/2, so the original average of log(1+k(alpha_i)) is exactly log2 while the Haar mean is at most log(3/2).
This supplies uniform positive Haar coverage for all original integer-unit inputs, without reciprocity or total reality, but does not estimate the moving-test transfer from Haar to the original conjugates.
The accepted C145 obstruction at this exact symbol remains in force.
No unrestricted gap, small-total-measure Fourier bound, new source theorem or computation is asserted.

<a id="argument"></a>
## 1. Accepted projection setup and the exact original value

[L321's exact Laurent identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) supplies, for the above actual coefficient projection,

    N k(t)=N-P(t)P(t^(-1))B_d(t),
    B_d(t)=v_d(t^(-1))^t(A_rel^t A_rel)^(-1)v_d(t).

The relation columns are independent by their distinct highest degrees, so the inverse exists; R is the rational rank-d orthogonal projection already used there.
At every original nonzero root, P(alpha_i)=0, giving k(alpha_i)=1 without any assumption on P(alpha_i^(-1)).
Alternatively R v_N(alpha_i)=v_N(alpha_i), followed by the indicated bilinear pairing, gives v_N(alpha_i^(-1))^t v_N(alpha_i)=N.
This is direct specialization of the accepted identity, not a new identity or positivity argument at complex roots.

On the circle the left vector is v_N(z)^*, so positivity and contraction of R give 0<=k(z)<=1.
Its constant coefficient is trace(R)/N=d/N=1/2.
Consequently

    0<=h<=log2,
    integral h<=log(integral(1+k))=log(3/2).           (5)

The last step is the elementary concavity inequality for the real logarithm on a probability space.
There are no circle zeros of 1+k and no logarithmic regularization error.
These range, mean and contact properties are the same setup used in [C145](Yin_C_G0145_v1.md#all-root-radial-kernel-contact).

The exact-value and positive-symbol assembly itself also holds at every integer window M>d, as already contemplated in D38.
Use the corresponding M-coordinate residual projection and divide its Laurent kernel by M.
The same L321 identity gives k_M(alpha_i)=1, circle range 0<=k_M<=1 and mean d/M; hence 1+k_M has full original norm 2^d and Haar logarithm at most log(1+d/M).
Clearing a positive coefficient denominator Q and multiplying by t^(M-1) gives an ordinary integer numerator of degree at most 2(M-1), with full signed resultant (2Q)^d Norm(alpha)^(M-1).
This is only the general-window version of the accepted identity and its immediate normalization; conclusions (1)--(4) above retain their stated N=2d specialization.

## 2. Absolute Fourier convergence and the lower bound

For this fixed P, k is a real trigonometric polynomial and 1+k>=1, so h is smooth and periodic.
For n!=0, two integrations by parts give |hhat(n)|<=||h''||_(L1)/n^2 when derivatives use the angular variable and L1 uses normalized Haar measure.
The boundary terms vanish by periodicity.
Thus sum_n |hhat(n)| is finite for this fixed input; there is no asserted uniform derivative bound.

For absolutely summable Fourier series define ||g||_W=sum_n |ghat(n)|.
Multiplying the absolutely convergent series and summing coefficient absolute values gives

    ||g_1 g_2||_W<=||g_1||_W||g_2||_W.

The exponential series therefore converges absolutely in coefficient norm and represents the pointwise exponential, since this norm dominates the uniform norm.
It follows that

    ||exp h||_W<=sum_(j>=0)||h||_W^j/j!=exp(||h||_W).  (6)

This is direct absolute summation and convolution; no inverse-closedness or uninspected Wiener-lemma theorem is invoked.

The actual coefficient expansion is

    k(t)=1/2+(1/N)sum_(n=1)^(N-1)a_n(t^n+t^(-n)).

Since N=2d, its nonconstant absolute coefficient sum is

    (2/N)sum_n |a_n|=kappa_R/2.

The positive constant coefficient of 1+k is 3/2, whence

    ||1+k||_W=3/2+kappa_R/2.                          (7)

By (5), 0<=hhat(0)<=log(3/2), so ||h||_W=hhat(0)+W_*(h).
Combining exp h=1+k with (6)--(7) gives

    3/2+kappa_R/2<=exp(hhat(0)+W_*(h))
                   <=(3/2)exp(W_*(h)).

Divide by 3/2 and take logarithms to obtain (1).

The independently accepted [C143 statement](Yin_C_G0143_v1.md#statement) supplies actual integer inputs of the present domain with kappa_R>=(sqrt(ell)-4)/2.
Substitution into (1) gives (2) and divergence as ell grows.
The [actual-input cost section](Yin_C_G0143_v1.md#projection-obstruction-original-costs) explicitly gives total m(P)>=log2 and its growing-scale bounds.
None of those original coefficients, conditioning choices or degree costs is removed here.
The present deduction transfers the already proved coherence obstruction to the nonsingular logarithm; it does not claim that C143's printed result itself proves a logarithmic theorem or a small-measure obstruction.

## 3. The integral unit-valued ordinary auxiliary

The Laurent support of 1+k lies within [-T,T], so the declared A is an integer polynomial of degree at most 2T=4d-2.
Its values follow from k(alpha_i)=1:

    A(alpha_i)=2Q alpha_i^T,
    f(alpha_i)=alpha_i^T.

Since P is monic with constant coefficient +/-1, every alpha_i is an algebraic integer unit.
The complete original resultant is the product of these d values, giving precisely (3), including the possible sign Norm(alpha)^T.
No own-field multiplicity is removed.
The polynomial is nonconstant: a constant f would make alpha^T rational; as a rational algebraic integer unit it would be +/-1, contradicting nontorsion.

On the circle the monomial t^T has modulus one, so |f|=(1+k)/2 belongs to [1/2,1].
The scalar Mahler/Haar normalization at the actual rational scale is the accepted [C_F6 identity](Yin_C_F0006_v1.md#scalar-capacity-normalization).
Thus

    m(f)=integral h-log2<=log(3/2)-log2=-gamma.

Shifting Laurent coefficients by t^T preserves their absolute sum, and dividing by 2 halves it.
Equation (7) therefore gives ||f||_1=(3+kappa_R)/4 exactly.
This proves all of (3) and the stated unbounded normalized-coefficient consequence.

The [C140 normalized sparse criterion](Yin_C_G0140_v1.md#statement) can use A/(2Q)'s ACTUAL integral unit value directly, with degree at most 4d-2 and a fixed negative normalized Mahler margin.
This is a comparison of its hypotheses, not an application of its conclusion: the term count and normalized coefficient-l1 budget are not uniformly bounded here.
In particular no additional norm-only adaptation or new divisibility theorem is needed for this exact auxiliary.

## 4. A fixed cubic scalar majorant and its actual Fourier width

For 0<=u=1-k<=1,

    h=log(2-u)=log2+log(1-u/2)
      =log2-sum_(j>=1) u^j/(j 2^j).

The series converges uniformly on this interval, and omitting its terms j>=4 yields G_3.
Every omitted term is nonnegative before subtraction, so

    0<=G_3-h<=sum_(j>=4)2^(-j)/j
                 <=(1/4)sum_(j>=4)2^(-j)=1/32.

The elementary integral estimate log(4/3)>1/4 follows because 1/x>3/4 except at the upper endpoint of [1,4/3].
Hence 1/32<gamma/8.
The Laurent degree of u is at most T, so its cubic has degree at most 3T.
The exact original identity u(alpha_i)=0 gives G_3(alpha_i)=log2, independently of circle positivity or approximation.
Integrating the uniform bound and using (5) proves the last inequality in (4).
All rational-coefficient and evaluation qualifications in the statement follow directly from the displayed formula.

<a id="existing-transfer-obstruction"></a>
## Existing transfer obstruction and precise strategic consequence

The accepted [C145 logarithmic-contact result](Yin_C_G0145_v1.md#logarithmic-contact-discrepancy) at delta=1 concerns exactly h=log(1+k).
For all original roots alpha_i=r_i z_i, its angular empirical measure satisfies

    empirical h-integral h>=gamma-(log2)D_N(P),
    D_N(P)<=2(N-1)m(P)/d<=4m(P).

Thus the actual bounded range and lack of singularities do not imply a small moving-test discrepancy.
C145 Section4 further proves that every uniformly eta-accurate real Laurent approximation G of degree at most L obeys, on the actual L229 domain 0<Lm(P)/d<=h0,

    epsilon(Lm(P)/d) W_*(G)
       >=gamma-(log2)D_N(P)-2eta.                   (8)

When m(P)<=gamma/(16log2) and eta<=gamma/8, this gives W_*(G)>=gamma/[2epsilon(Lm(P)/d)].
The present explicit G_3 meets the error condition with eta=1/32 and has a degree-O(d) frequency bound, but its expanded coefficient norm is still subject to (8).
These are direct uses of the existing conditional estimate, not a claim that a near-one sequence exists or a newly proved angular theorem.

The universal positive-symbol/Haar assembly already removes the need to find another isolated favorable Haar example merely for auxiliary existence.
The remaining question is an actual small-total-measure arithmetic estimate on expanded Fourier coefficients or their joint angular contribution, or a different rigorously paid transfer.
The new all-input obstruction (1)--(2) and the existing conditional obstruction (8) supply distinct scope tests for proposed bounds.
Neither an additional constant lower floor on the circle nor a fixed scalar approximation degree supplies the missing estimate.
The earlier single-column reciprocal completion from L237 remains valid at its exact scope; the present all-column use of L321 supplies wider input coverage and bounded range without changing its accepted antecedents.

## Author check, provenance and fixed scope

The authors checked the exact Laurent rather than Hermitian evaluation, every original nonzero root, rational projection rank/mean, positivity only where it is used, original signed resultant, actual integral unit values and complete coefficient normalization.
The local new proof was checked for periodic integration-by-parts boundary terms, absolute coefficient convergence, the exponential convolution inequality, cancellation of the mean bound with (7), the C143 actual large-measure scope, all cubic signs and coefficients, the geometric tail and true frequency upper bound.
This is an author check and not independent acceptance.

The bounded reuse screen read the actual relevant sections of L237, L321, C140, C143, C145, C10v2 and D35.
L321/C145 already own the projection, Laurent identity and moving-test estimates; their full proofs are not copied or reclassified here.
No external theorem beyond these declared accepted interfaces is introduced, and no novelty claim is made for the elementary Fourier convolution or logarithmic series.
This fixed account retains all useful mathematics of D38, including the exact integral auxiliary and the distinction between all-input and small-total-measure bounds.
Root supplied the symbol/exact-value assembly; cross_term_reuse supplied (1), its local proof and (4).
Both are contributors; separate whole review is pending.

## Current assessment
[Selected decision](#decision-current-haar-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:13 |
| status | open |
| reason | Register the complete logarithmic Wiener lower bound, its actual C143 family consequence, exact integral auxiliary normalization and cubic finite certificate for separate whole review; no acceptance or unrestricted gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every original integer-unit input at N=2d; Fourier lower bound, actual large-measure family, integral auxiliary with exact normalization and finite cubic certificate. |
| argument | [Complete local proof](#argument) | Sections1--4, existing-transfer scope, all coefficient and original-field costs, and declared contribution limits. |
| dependency | [Accepted Laurent projection identity](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact actual residual projection, rank and coefficient conventions, Nk=N-P(t)P(t^-1)B and every-original-root specialization. |
| dependency | [Accepted actual square-root family](Yin_C_G0143_v1.md#statement) | Actual monic irreducible reciprocal integer inputs, coherence lower bound, unbounded prime sequence and full large-measure boundary. |
| dependency | [Existing radial and logarithmic contact](Yin_C_G0145_v1.md#argument) | Exact same symbol's range/mean and the existing original-angular discrepancy/Fourier-budget inequalities, with actual L229 domain. |
| dependency | [Scalar Mahler normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Rational scalar and monomial normalization for m(A/(2Q)) with all original coefficients retained. |
| support | [Normalized sparse transfer comparison](Yin_C_G0140_v1.md#statement) | Actual integral-unit premise matches, while uniform term-count and normalized coefficient-l1 hypotheses remain unsupplied. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T10:25 |
| status | proved |
| reason | Adopt the complete local Wiener lower bound, actual large-measure consequence, exact unit-valued auxiliary normalization and cubic certificate after the actual whole R380 review. The accepted projection identity and C145 discrepancy remain reused inputs; neither universal Haar coverage nor a bounded circle logarithm supplies an unproved transfer estimate or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every original integer-unit input at N=2d; Fourier lower bound, actual large-measure family, integral auxiliary with exact normalization and finite cubic certificate. |
| argument | [Complete local proof](#argument) | Sections1--4, existing-transfer scope, all coefficient and original-field costs, and declared contribution limits. |
| dependency | [Accepted Laurent projection identity](../ledger/Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact actual residual projection, rank and coefficient conventions, Nk=N-P(t)P(t^-1)B and every-original-root specialization. |
| dependency | [Accepted actual square-root family](Yin_C_G0143_v1.md#statement) | Actual monic irreducible reciprocal integer inputs, coherence lower bound, unbounded prime sequence and full large-measure boundary. |
| dependency | [Existing radial and logarithmic contact](Yin_C_G0145_v1.md#argument) | Exact same symbol's range/mean and the existing original-angular discrepancy/Fourier-budget inequalities, with actual L229 domain. |
| dependency | [Scalar Mahler normalization](../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Rational scalar and monomial normalization for m(A/(2Q)) with all original coefficients retained. |
| support | [Normalized sparse transfer comparison](Yin_C_G0140_v1.md#statement) | Actual integral-unit premise matches, while uniform term-count and normalized coefficient-l1 hypotheses remain unsupplied. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G0380_v1.md#projection-log-whole-independent-finding) | Complete statement and argument, all four dependency interfaces, C140 comparison, signed full normalization, absolute Fourier convergence, actual C143 scope and exact C145/L229 domain. |

### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:45 |
| status | proved |
| reason | Select adopted C_F6 as the current complete responsible home of the identical retained scalar Haar/Jensen normalization. Its actual selected adoption and complete normalization section were read and matched to the original fixed L_F5 text, including Laurent shifts, leading coefficients, all root multiplicities and integrable circle zeros. Only that normalization is reused here, with every original scalar, phase and cost retained; no Gram optimization, root-distribution transfer or new review is supplied. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every original integer-unit input at N=2d; Fourier lower bound, actual large-measure family, integral auxiliary with exact normalization and finite cubic certificate. |
| argument | [Complete local proof](#argument) | Sections1--4, existing-transfer scope, all coefficient and original-field costs, and declared contribution limits. |
| dependency | [Accepted Laurent projection identity](Yin_C_G0592_v2.md#residual-laurent-square-identity) | Exact actual residual projection, rank and coefficient conventions, Nk=N-P(t)P(t^-1)B and every-original-root specialization. |
| dependency | [Accepted actual square-root family](Yin_C_G0143_v1.md#statement) | Actual monic irreducible reciprocal integer inputs, coherence lower bound, unbounded prime sequence and full large-measure boundary. |
| dependency | [Existing radial and logarithmic contact](Yin_C_G0145_v1.md#argument) | Exact same symbol's range/mean and the existing original-angular discrepancy/Fourier-budget inequalities, with actual L229 domain. |
| dependency | [Scalar Mahler normalization](Yin_C_F0006_v1.md#scalar-capacity-normalization) | Rational scalar and monomial normalization for m(A/(2Q)) with all original coefficients retained. |
| support | [Normalized sparse transfer comparison](Yin_C_G0140_v1.md#statement) | Actual integral-unit premise matches, while uniform term-count and normalized coefficient-l1 hypotheses remain unsupplied. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0380_v1.md#projection-log-whole-independent-finding) | Complete statement and argument, all four dependency interfaces, C140 comparison, signed full normalization, absolute Fourier convergence, actual C143 scope and exact C145/L229 domain. |
