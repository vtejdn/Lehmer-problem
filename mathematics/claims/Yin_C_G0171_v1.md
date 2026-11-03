---
author: Yin
---
# Separated two-block Salem projections and a singular torus phase

Date: 2026-10-18T15:50.
Human author Yin.
The angular_envelope_review agent develops this S3/S5 inquiry under root's continuing all-strategy allocation.
This is fixed author mathematics, initially registered as proof draft and unreviewed, with no numerical execution or adoption.

<a id="two-block-torus-question"></a>
## Actual question and responsible scope

For the exact moving-prime Salem family of [L402](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule), can the normalized coefficients of the full original-window projection be identified through a separated two-channel limit?
The precise target is the actual joint symbol Xi and kappa in [L402](../ledger/Yin_L_G0402_v1.md#moving-exponent-joint-kernel-question), keeping the original degree d, window2d, complete cyclotomic removal and bounded positive total measure.
The proposed discriminator is a singular phase in a three-variable torus limit, rather than a small Gram eigenvalue or separate inverse-factor estimate.
The complete author proof below establishes divergence for this exact positive-measure family.

[L404](Yin_C_G0499_v1.md#joint-boundary-symbol) already supplies the exact finite joint boundary formula, and its separated-factor bounds are insufficient here.
[C506](Yin_C_G0506_v1.md#joint-cutoff-target) supplies polynomial spectral cutoffs and the paid low-mode remainder.
[C507](Yin_C_G0507_v1.md#neutral-factor-bounded-symbol) proves that a divergent low-mode count alone need not give actual coherence divergence.
[C160](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) supplies the existing original-normalization rank correction, and the present author contributed that accepted upstream theorem.
These accepted inputs are reused at their fixed scopes.
The proof below controls each selected original Fourier coefficient by a finite-rank cyclic comparison and then removes a bounded continuous regularization on the torus.
It assumes no uniform spectral gap.

## Bounded reuse and exact discriminating test

The local finite projection, Toeplitz, Blaschke and coefficient-limit interfaces were searched and the preceding actual materials were read.
[L264](../ledger/Yin_L_G0264_v1.md#blaschke-budget-fixed-scope) concerns fixed-input Hardy/Blaschke limits and explicitly leaves varying-input onset unquantified; it does not supply the required moving-exponent finite-window limit.
[C393](Yin_C_G0393_v1.md#gram-cokernel-outcome) is an integer boundary-cokernel result and supplies no such Fourier estimate.
The complete finite-rank and Fourier argument is elementary; no uninspected Toeplitz asymptotic theorem is a premise.
There is no numerical experiment or change to the large killer exponent K.

The exact test has three parts: equal-modulus channels for A+x^c B, failure of a continuous torus phase representative, and convergence of each fixed torus Fourier coefficient from a distinct original signed diagonal coefficient.
Sections2--5 prove each part with its actual finite costs.

<a id="two-block-torus-statement"></a>
## 1. Exact actual-family statement

Keep EXACTLY the K,a_j,b_j,c_j schedule and full original Salem polynomials P_j of L402.
Suppress j temporarily and write

    L=K+a+b+2, D=c+L, d=D-3, N=2d,
    Q(x)=(x-1)^3 P(x)=A(x)+x^c B(x),
    r=N-D=c+L-6.

Here Q is L402's raw numerator N_j; the letter Q avoids collision with the coordinate-window length N.
The full coefficient matrix T has the r columns Q,xQ,...,x^(r-1)Q in R^N.
Let Pi=T(T^t T)^(-1)T^t and R_Q=I-Pi.
Every normalized Fourier coefficient below uses the ORIGINAL d:

    Xi_j(z)=d^(-1) v_N(z^-1)^t Pi v_N(z),
    kappa_Q,j=sum_(h!=0)|Xihat_j(h)|.                    (1)

The author conclusion developed below is

    kappa_Q,j -> infinity,
    kappa_(2d_j)(P_j) -> infinity.                       (2)

The second assertion follows from the accepted same-window rank-three bound

    |kappa_Q,j-kappa_(2d_j)(P_j)|<6.

This is an actual monic irreducible Salem family of trace -1 and bounded POSITIVE total measure log2<m(P_j)<log4.
It does not supply a sequence with total measure tending to zero or disprove a coherence estimate confined to sufficiently small total measure.
No rate in d_j, numerical lower bound at a specified j, or assertion about the cubic logarithmic polynomial is claimed.
The author proof remains unreviewed until a separate fixed review actually checks it.

<a id="two-block-circulant-rank-transfer"></a>
## 2. Exact finite cyclic comparison with every boundary retained

The actual schedule gives L<c, L>6, L/c->0, b/a->infinity, a->infinity and c/b->infinity.
In R^c let S_c e_i=e_(i+1 mod c), and define the N-by-c matrix

    V=[ A(S_c) ; B(S_c) ; 0_(2L-6)-by-c ].             (3)

This is an auxiliary finite cyclic matrix embedded in the SAME original N coordinates, not a replacement polynomial or original field.
Let Pi_V be its orthogonal range projection, allowing its actual rank defect.
Let T_0 be the first c columns of T.
For each column index0<=i<c-L, multiplication by both A and B has degree below c before the second block is shifted by c.
Thus its column in T_0 equals its column in V.
Only the last L columns can differ, and

    rank(T_0-V)<=L.

If U and W are the two column spaces, then U is contained in W+im(T_0-V), and W is contained in U+im(T_0-V).
Each has codimension at most L over U intersection W.
Their orthogonal projection difference therefore has rank at most2L.
The additional r-c=L-6 columns extend im T_0 inside im T by exactly L-6, because all polynomial shifts are independent.
Consequently

    rank(Pi-Pi_V)<=3L-6,
    ||Pi-Pi_V||_op<=1,
    ||Pi-Pi_V||_trace<=3L-6.                            (4)

For the middle inequality, the quadratic form of a difference of two orthogonal projections lies between-||x||^2 and||x||^2.
For the rank inequality no positivity of their difference is assumed.

For any matrix H, the coefficient of z^h in v_N(z^-1)^t H v_N(z) is the sum of entries H_(i,i+h) that lie in the window.
It is a trace pairing with a truncated shift of operator norm at most1.
The singular-value decomposition gives |trace(HU)|<=||H||_trace ||U||_op.
Hence, for EVERY signed h with |h|<N,

    |Xihat_j(h)-[z^h](d^(-1)v_N(z^-1)^t Pi_V v_N(z))|
                      <=(3L-6)/d ->0.                  (5)

This is coefficientwise convergence, not a small bound on the sum of all errors.
In particular an O(L) rank error is never discarded in a Wiener-norm estimate.
The point is that each of finitely many selected coefficients pays its own vanishing O(L/c) normalized error.
No inverse norm, least Gram eigenvalue or unpriced boundary limit is used.

<a id="two-block-torus-phase"></a>
## 3. The exact equal-modulus channels and their torus phase

Introduce three independent unit variables z,u,v and the fixed integer K from L402.
Set

    R=(z^K-1)(u-1)(v-1),
    S=(z^K+1)(u-1)(v-1)
          +(u+1)(z^K-1)(v-1)+(v+1)(z^K-1)(u-1),
    Acal=-(z^2-1)R-(z/2)R+(z/2)S,
    Bcal= (z^2-1)R-(z/2)R-(z/2)S.                    (6)

Then A_j(z)=Acal(z,z^a,z^b) and B_j(z)=Bcal(z,z^a,z^b), exactly as in L402.
The half coefficients in this multivariable display cause no change to the already proved integrality of the actual one-variable polynomials.
For |w|=1 and w!=1, C(w)=(w+1)/(w-1) is purely imaginary.
Where R!=0 put

    H=-(z-z^(-1))+(C(z^K)+C(u)+C(v))/2.

Then H is purely imaginary and

    Acal/(zR)=-1/2+H,
    Bcal/(zR)=-1/2-H.                                  (7)

Thus |Acal|=|Bcal| and neither vanishes where R!=0.
By continuity the modulus identity holds on the entire torus.
Since Acal+Bcal=-zR, common zeros must have R=0 and S=0.
Checking the three factors in R shows that the common zero set is exactly

    Z={u=v=1} union {z^K=1,u=1} union {z^K=1,v=1}.       (8)

It has three-torus Haar measure zero.
Define the bounded measurable function

    U=Acal/Bcal off Z,       U=0 on Z.

It has modulus1 off Z and is continuous there.
The definition on Z will affect no Haar Fourier coefficient.

For an actual c-th root of unity omega!=1, the distinct prime c is coprime to K,a,b.
Therefore none of omega^K,omega^a,omega^b equals1, and A_j(omega),B_j(omega) are nonzero.
At omega=1 both vanish.
The c-dimensional Fourier basis diagonalizes S_c, so the actual rank of V is c-1.
In the first two coordinate blocks its range projection is

    Pi_V,11=Pi_V,22=(I_c-J_c/c)/2,
    Pi_V,12(i,l)=(1/(2c)) sum_(omega^c=1)
                    U(omega,omega^a,omega^b) omega^(l-i),
    Pi_V,21=Pi_V,12^*.                                 (9)

Here J_c is the all-ones matrix; the zero root-frequency omega=1 is included with U=0.
For clarity, the cyclic eigenvector has entries omega^(-i), so the displayed phase orientation and exponent l-i follow directly from S_c's specified direction.
The final2L-6 rows and columns of Pi_V vanish.
All actual matrices are real, since the samples at conjugate roots are conjugate.

For any integer h with |h|<c, set

    Ubar_j(h)=(1/c) sum_(omega^c=1)
                    U(omega,omega^a,omega^b) omega^h.

Counting the c-|h| entries in the corresponding cross-block diagonal gives the exact finite identity

    [z^(c+h)] d^(-1)v_N(z^-1)^t Pi_V v_N(z)
       =((c-|h|)/(2d)) Ubar_j(h)+min(h,0)/(cd).         (10)

When h<0 the last term is the contribution of the two within-block diagonals, each having entries-1/(2c).
When h>=0 those within-block diagonals are absent.
The other cross block contributes only negative offsets and does not enter this positive coefficient.
Thus the actual missing zero frequency, both finite endpoints and every normalization are explicit.

<a id="two-block-discrete-torus-limit"></a>
## 4. The separated-prime coefficient limit, with the singular set paid

Let mu_j be the probability measure assigning mass1/c_j to each point

    (omega,omega^(a_j),omega^(b_j)), omega^(c_j)=1.

For a fixed integer triple gamma=(gamma_0,gamma_1,gamma_2), its character integral equals1 if c_j divides gamma_0+gamma_1 a_j+gamma_2 b_j, and equals0 otherwise.
If gamma!=0, the integer is nonzero for all large j: the largest nonzero coefficient is decisive first at scale b_j, then a_j, then1.
Its absolute value is less than c_j for all large j.
Therefore each nontrivial character integral is eventually exactly zero, and mu_j converges to normalized Haar measure mu on the three-torus against every continuous function.

Here is a complete elementary density justification for this last step.
The one-variable Fejer kernel m^(-1)|sum_(k=0)^(m-1)e^(ikt)|^2 is nonnegative, has integral1 and has integral outside any fixed neighborhood of0 tending to zero, by the geometric-sum bound away from0.
Its product in three variables has the same approximate-identity property.
Convolving any continuous torus function with that product gives a trigonometric polynomial converging uniformly to the function, by uniform continuity and the tail bound.
Character convergence therefore implies convergence for all continuous functions.
No Toeplitz spectral-distribution theorem or varying-polynomial rate is being assumed.

The phase U itself need not be continuous.
Put g=|Acal|^2+|Bcal|^2, and for delta>0 define the continuous function

    U_delta=2 Acal conjugate(Bcal)/(g+delta).

Because the channel moduli agree, |U_delta|<=1 and, off Z,

    |U-U_delta|=delta/(g+delta).

The inequality with the same right side also holds on Z, where both U and U_delta were set to zero.
For fixed delta, continuous-function convergence applies both to U_delta times any character and to delta/(g+delta).
The Haar integral of the latter tends to zero as delta decreases to zero, since g>0 outside the measure-zero set Z and the integrand is bounded by1.
One can see this without a rate by first excluding {g<epsilon}, whose Haar measure decreases to zero, and then using delta/(epsilon+delta) on its complement.
It follows that, for each fixed gamma,

    Ubar_j(gamma_0+gamma_1 a_j+gamma_2 b_j)
                 -> integral U z^(gamma_0)u^(gamma_1)v^(gamma_2) dmu
                  = Uhat(-gamma).                     (11)

No uniform quadrature estimate near the singular set is claimed or required.
Only fixed delta is passed through the j limit, followed by delta decreasing to zero.

Let h_j(gamma)=gamma_0+gamma_1 a_j+gamma_2 b_j.
For every fixed finite set of triples these offsets are distinct for all sufficiently large j, and |h_j(gamma)|/c_j->0.
Also c_j+h_j(gamma) lies in the positive original frequency interval1,...,N_j-1.
Using d_j/c_j->1 in (5), (10) and (11) gives the actual joint-coefficient limit

    Xihat_j(c_j+h_j(gamma)) -> (1/2) Uhat(-gamma).       (12)

This identifies original signed Fourier diagonals of the finite projection, not merely coefficients of a formal infinite inverse.
It is valid simultaneously for any fixed finite set of gamma.

<a id="two-block-singular-phase-divergence"></a>
## 5. Noncontinuity forces divergent actual coherence

The torus phase U has no continuous representative even after changing it on a set of Haar measure zero.
To prove this, fix z_0=exp(i pi/K), so z_0^K=-1 and C(z_0^K)=0.
Consider the common singular point(z_0,1,1).
For nonzero real t tending to zero, both of the following paths stay outside Z.
Along u=v=exp(it), equation(7) gives

    H=-(z_0-z_0^(-1))-i cot(t/2),

so |H| tends to infinity and U tends to-1.
Along u=exp(it),v=exp(-it), the two cotangent terms cancel and

    H=H_0=-(z_0-z_0^(-1)),
    U=(-1/2+H_0)/(-1/2-H_0).                           (13)

This finite value is not-1, since that equality would give-1/2=1/2.
The denominator is nonzero because H_0 is purely imaginary.
The two limits are incompatible with continuity at the singular point.

If a continuous function agreed with U almost everywhere, it would agree with U everywhere on the open regular set: their difference is continuous there, and any nonzero value has a neighborhood of positive Haar measure.
The preceding two paths therefore also rule out such a continuous representative.

Consequently

    sum_(gamma in Z^3)|Uhat(gamma)|=infinity.           (14)

Indeed absolute summability would make the Fourier series converge uniformly to a continuous function with these coefficients.
Its bounded difference from U would have every Fourier coefficient zero, so convolution with each product Fejer kernel would vanish identically.
At every point outside Z that difference is continuous in a neighborhood of the point.
The same approximate-identity proof then gives convergence to its value there: use local continuity near the point and the global boundedness times the vanishing kernel tail on the complement.
Thus the continuous Fourier sum would agree with U at every regular point, which the two paths in (13) already exclude.
This proves (14) without any unstated varying-input Fourier convergence theorem.

For any finite set F subset Z^3, the distinct positive frequencies in (12) and nonnegativity of absolute values yield

    liminf_j kappa_Q,j >= (1/2) sum_(gamma in F)|Uhat(-gamma)|.  (15)

Given any real M>0, equation(14) supplies a finite F for which the right side exceeds M.
Equation(15) then proves kappa_Q,j tends to infinity.
The original same-window rank-three comparison proves the second assertion of (2).
This proves genuine joint-symbol divergence despite the cancellation of every singular inverse factor inside each finite projection.
The proof does not infer divergence from L402's vanishing Rayleigh quotient or L406's low-mode count.

<a id="two-block-torus-boundaries"></a>
## 6. What the result does and does not settle

The exact varying-seed family in L402 now gives an author proof of unbounded original2d coherence while keeping total Mahler measure in the fixed interval(log2,log4).
C143's earlier examples had growing total measure, and C160/L407 supply contrasting bounded-coherence families at another fixed positive-measure range.
No contradiction with either control follows.
This result also shows why the true joint symbol can carry information invisible to an unnormalized Gram-spectrum diagnosis.
The decisive object is the off-diagonal phase in a finite cyclic comparison, whose singular multivariable limit forces arbitrarily many distinct original Fourier coefficients to carry a large total absolute sum.

The polynomial Q is always the exact numerator of the actually certified Salem polynomial P_j, not an arbitrary multivariate specialization selected after the fact.
The full original degree,2d window, signed frequencies and cyclotomic rank correction are unchanged.
The cyclic matrix is only a finite proof device and its rank defect and boundary discrepancy are paid before any limit.
The result asserts neither a rate nor a practical original-window computation, and leaves sufficiently-small-total-measure coherence estimates and the unrestricted Mahler gap unresolved.
There is no new J, numerical scan, source theorem, T/E/S decision or adoption in this author proof.

<a id="two-block-torus-fixed-inputs"></a>
## Exact input roles

| Role | Target | Scope |
| --- | --- | --- |
| Actual arithmetic family | [L402 schedule](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact fixed K, distinct separated primes, original monic irreducible Salem polynomial, trace -1, original degrees and log2<m<log4; unchanged MS05/RY26 statement and proof-inspection boundaries. |
| Actual raw blocks | [L402 raw numerator](../ledger/Yin_L_G0402_v1.md#moving-exponent-raw-numerator) | Exact A,B,R,S expansion, integrality, degrees and full removal of(x-1)^3. |
| Original joint symbol | [L402 joint question](../ledger/Yin_L_G0402_v1.md#moving-exponent-joint-kernel-question) | Full-column projection and original-d normalization of kappa. |
| Same-window correction | [C160 rank correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Accepted rank-three comparison with additive error<6; this author contributed C160 and does not independently re-review it here. |
| Definition | [C158](Yin_C_G0158_v1.md#statement) | Original rank-d projection and all signed Fourier diagonals; no new cubic-norm conclusion. |
| Joint finite interface | [L404](Yin_C_G0499_v1.md#joint-boundary-symbol) | Comparison and motivation, not an additional inverse estimate or proof premise. |
| Low-mode comparison | [C506](Yin_C_G0506_v1.md#joint-cutoff-target) and [C507](Yin_C_G0507_v1.md#neutral-factor-bounded-symbol) | Previously retained spectrum-versus-coherence boundary; neither supplies this divergence theorem. |
| Other controls | [C143](Yin_C_G0143_v1.md#statement) and [C160](Yin_C_G0160_v1.md#statement) | Growing-measure divergent and fixed-positive-measure bounded examples, respectively; no source-proof upgrade or new near-one coverage. |


## Current assessment
[Selected decision](#decision-current-complete-low-mode-comparison-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T15:59 |
| status | open |
| reason | Register the complete actual moving-prime Salem coherence-divergence statement and unchanged author proof for whole independent review. Original degree,2d window, all signed diagonals, cyclic boundary and rank-three costs, fixed positive-measure range and source/contribution limits remain explicit. No cubic, near-one, rate or unrestricted-gap conclusion is registered. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual-family conclusion](#two-block-torus-statement) | Both raw and original2d coherences tend to infinity on the exact L402 schedule; original irreducible degrees, trace -1 and log2<m<log4, with all stated exclusions. |
| argument | [Complete finite-to-torus proof](#two-block-circulant-rank-transfer) | Entire Sections2--5, formulas3--15, finite cyclic rank price, exact signed coefficient normalization, discrete alias exclusion, regularization, essential discontinuity and Fejer uniqueness. |
| dependency | [Actual L402 family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact K and separated prime sequence, original Salem factor and degree, trace and bounded positive measure; retained MS05/RY26 source-inspection boundary. |
| dependency | [Exact raw blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-raw-numerator) | Integral A,B expansion, polynomial degrees and complete cyclotomic removal. |
| dependency | [Joint projection interface](../ledger/Yin_L_G0402_v1.md#moving-exponent-joint-kernel-question) | Full raw relation columns, actual Xi and original-d normalization. |
| dependency | [Rank-three original correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested same-window projection spaces and additive coherence cost<6; this author contributed the accepted upstream proof. |
| dependency | [Original coherence definition](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection and both signed Fourier directions; no cubic implication is inferred. |
| support | [Complete input roles](#two-block-torus-fixed-inputs) | All eight retained arithmetic, normalization, comparison and contribution roles. |
| support | [L404 joint finite formula](../ledger/Yin_L_G0404_v1.md#joint-boundary-symbol) | Existing comparison and motivation only; no inverse bound is imported. |
| support | [L406 paid low-mode cutoff](../ledger/Yin_L_G0406_v1.md#joint-cutoff-target) | Existing spectral sufficient criterion only, not a premise of divergence. |
| support | [L407 bounded-symbol control](../ledger/Yin_L_G0407_v1.md#neutral-factor-bounded-symbol) | Low-mode rank growth alone is insufficient; this accepted comparison is preserved. |
| support | [C143 growing-measure control](Yin_C_G0143_v1.md#statement) | Earlier actual divergent-coherence family in its different measure range. |
| support | [C160 bounded-coherence control](Yin_C_G0160_v1.md#statement) | Earlier actual fixed-positive-measure bounded family and disclosed upstream author relationship; no conflict or new near-one coverage. |

### Decision whole-reviewed-2026-10-19

| Field | Value |
| --- | --- |
| date | 2026-10-18T16:05 |
| status | proved |
| reason | Adopt the complete actual bounded-positive-measure Salem coherence-divergence proof after whole independent R417. Original degree/window, all finite cyclic boundary costs, singular-set and Fourier limits, rank-three correction and source/contribution limits are preserved. No near-one, cubic, rate or unrestricted-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Actual-family conclusion](#two-block-torus-statement) | Both raw and original2d coherences tend to infinity on the exact L402 schedule; original irreducible degrees, trace -1 and log2<m<log4, with all stated exclusions. |
| argument | [Complete finite-to-torus proof](#two-block-circulant-rank-transfer) | Entire Sections2--5, formulas3--15, finite cyclic rank price, exact signed coefficient normalization, discrete alias exclusion, regularization, essential discontinuity and Fejer uniqueness. |
| dependency | [Actual L402 family](../ledger/Yin_L_G0402_v1.md#fixed-trace-moving-exponent-schedule) | Exact K and separated prime sequence, original Salem factor and degree, trace and bounded positive measure; retained MS05/RY26 source-inspection boundary. |
| dependency | [Exact raw blocks](../ledger/Yin_L_G0402_v1.md#moving-exponent-raw-numerator) | Integral A,B expansion, polynomial degrees and complete cyclotomic removal. |
| dependency | [Joint projection interface](../ledger/Yin_L_G0402_v1.md#moving-exponent-joint-kernel-question) | Full raw relation columns, actual Xi and original-d normalization. |
| dependency | [Rank-three original correction](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested same-window projection spaces and additive coherence cost<6; this author contributed the accepted upstream proof. |
| dependency | [Original coherence definition](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection and both signed Fourier directions; no cubic implication is inferred. |
| support | [Complete input roles](#two-block-torus-fixed-inputs) | All eight retained arithmetic, normalization, comparison and contribution roles. |
| support | [L404 joint finite formula](../ledger/Yin_L_G0404_v1.md#joint-boundary-symbol) | Existing comparison and motivation only; no inverse bound is imported. |
| support | [L406 paid low-mode cutoff](../ledger/Yin_L_G0406_v1.md#joint-cutoff-target) | Existing spectral sufficient criterion only, not a premise of divergence. |
| support | [L407 bounded-symbol control](../ledger/Yin_L_G0407_v1.md#neutral-factor-bounded-symbol) | Low-mode rank growth alone is insufficient; this accepted comparison is preserved. |
| support | [C143 growing-measure control](Yin_C_G0143_v1.md#statement) | Earlier actual divergent-coherence family in its different measure range. |
| support | [C160 bounded-coherence control](Yin_C_G0160_v1.md#statement) | Earlier actual fixed-positive-measure bounded family and disclosed upstream author relationship; no conflict or new near-one coverage. |
| review | [Whole actual-coherence finding](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Complete statement, whole finite-to-torus argument, all15 formulas and eight input roles at the exact fixed Claim scope. |


### Decision current-complete-moving-family-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:21 |
| status | proved |
| reason | Select the complete C494 home for exactly the already used L402 family/blocks/original-degree joint-projection interface. Preserve the statement, entire proof, status, authority, all other input and review tuples/scopes. This same-object maintenance supplies no fresh whole or isolated review and does not backdate C494 as an old input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#two-block-torus-statement) | Both raw and original2d coherences tend to infinity on the exact L402 schedule; original irreducible degrees, trace -1 and log2<m<log4, with all stated exclusions. |
| argument | [Exact argument](#two-block-circulant-rank-transfer) | Entire Sections2--5, formulas3--15, finite cyclic rank price, exact signed coefficient normalization, discrete alias exclusion, regularization, essential discontinuity and Fejer uniqueness. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Exact K and separated prime sequence, original Salem factor and degree, trace and bounded positive measure; retained MS05/RY26 source-inspection boundary. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-raw-numerator) | Integral A,B expansion, polynomial degrees and complete cyclotomic removal. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-joint-kernel-question) | Full raw relation columns, actual Xi and original-d normalization. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested same-window projection spaces and additive coherence cost<6; this author contributed the accepted upstream proof. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection and both signed Fourier directions; no cubic implication is inferred. |
| support | [Exact support](#two-block-torus-fixed-inputs) | All eight retained arithmetic, normalization, comparison and contribution roles. |
| support | [Exact support](../ledger/Yin_L_G0404_v1.md#joint-boundary-symbol) | Existing comparison and motivation only; no inverse bound is imported. |
| support | [Exact support](../ledger/Yin_L_G0406_v1.md#joint-cutoff-target) | Existing spectral sufficient criterion only, not a premise of divergence. |
| support | [Exact support](../ledger/Yin_L_G0407_v1.md#neutral-factor-bounded-symbol) | Low-mode rank growth alone is insufficient; this accepted comparison is preserved. |
| support | [Exact support](Yin_C_G0143_v1.md#statement) | Earlier actual divergent-coherence family in its different measure range. |
| support | [Exact support](Yin_C_G0160_v1.md#statement) | Earlier actual fixed-positive-measure bounded family and disclosed upstream author relationship; no conflict or new near-one coverage. |
| review | [Exact review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Complete statement, whole finite-to-torus argument, all15 formulas and eight input roles at the exact fixed Claim scope. |


### Decision current-complete-toeplitz-comparison-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:03 |
| status | proved |
| reason | Maintain only the exact same-object joint finite-boundary comparison at its complete C499 home. This remains comparison and motivation with no inverse estimate or new logical premise; all other mathematical state, statement/argument/review relations and scopes remain unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#two-block-torus-statement) | Both raw and original2d coherences tend to infinity on the exact L402 schedule; original irreducible degrees, trace -1 and log2<m<log4, with all stated exclusions. |
| argument | [Exact argument](#two-block-circulant-rank-transfer) | Entire Sections2--5, formulas3--15, finite cyclic rank price, exact signed coefficient normalization, discrete alias exclusion, regularization, essential discontinuity and Fejer uniqueness. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Exact K and separated prime sequence, original Salem factor and degree, trace and bounded positive measure; retained MS05/RY26 source-inspection boundary. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-raw-numerator) | Integral A,B expansion, polynomial degrees and complete cyclotomic removal. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-joint-kernel-question) | Full raw relation columns, actual Xi and original-d normalization. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested same-window projection spaces and additive coherence cost<6; this author contributed the accepted upstream proof. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection and both signed Fourier directions; no cubic implication is inferred. |
| support | [Exact support](#two-block-torus-fixed-inputs) | All eight retained arithmetic, normalization, comparison and contribution roles. |
| support | [Exact support](Yin_C_G0499_v1.md#joint-boundary-symbol) | Existing comparison and motivation only; no inverse bound is imported. |
| support | [Exact support](../ledger/Yin_L_G0406_v1.md#joint-cutoff-target) | Existing spectral sufficient criterion only, not a premise of divergence. |
| support | [Exact support](../ledger/Yin_L_G0407_v1.md#neutral-factor-bounded-symbol) | Low-mode rank growth alone is insufficient; this accepted comparison is preserved. |
| support | [Exact support](Yin_C_G0143_v1.md#statement) | Earlier actual divergent-coherence family in its different measure range. |
| support | [Exact support](Yin_C_G0160_v1.md#statement) | Earlier actual fixed-positive-measure bounded family and disclosed upstream author relationship; no conflict or new near-one coverage. |
| review | [Exact review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Complete statement, whole finite-to-torus argument, all15 formulas and eight input roles at the exact fixed Claim scope. |


### Decision current-complete-low-mode-comparison-homes

| Field | Value |
| --- | --- |
| date | 2026-10-22T03:00 |
| status | proved |
| reason | Maintain only the two exact same-object spectral and neutral-factor comparisons at their complete C506/C507 homes. These remain support and motivation, not premises of this divergence theorem; all mathematical state, other relations/scopes, adopted R417 finding and historical inputs are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#two-block-torus-statement) | Both raw and original2d coherences tend to infinity on the exact L402 schedule; original irreducible degrees, trace -1 and log2<m<log4, with all stated exclusions. |
| argument | [Exact argument](#two-block-circulant-rank-transfer) | Entire Sections2--5, formulas3--15, finite cyclic rank price, exact signed coefficient normalization, discrete alias exclusion, regularization, essential discontinuity and Fejer uniqueness. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#fixed-trace-moving-exponent-schedule) | Exact K and separated prime sequence, original Salem factor and degree, trace and bounded positive measure; retained MS05/RY26 source-inspection boundary. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-raw-numerator) | Integral A,B expansion, polynomial degrees and complete cyclotomic removal. |
| dependency | [Exact dependency](Yin_C_G0494_v1.md#moving-exponent-joint-kernel-question) | Full raw relation columns, actual Xi and original-d normalization. |
| dependency | [Exact dependency](Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested same-window projection spaces and additive coherence cost<6; this author contributed the accepted upstream proof. |
| dependency | [Exact dependency](Yin_C_G0158_v1.md#statement) | Original rank-d residual projection and both signed Fourier directions; no cubic implication is inferred. |
| support | [Exact support](#two-block-torus-fixed-inputs) | All eight retained arithmetic, normalization, comparison and contribution roles. |
| support | [Exact support](Yin_C_G0499_v1.md#joint-boundary-symbol) | Existing comparison and motivation only; no inverse bound is imported. |
| support | [Exact support](Yin_C_G0506_v1.md#joint-cutoff-target) | Existing spectral sufficient criterion only, not a premise of divergence. |
| support | [Exact support](Yin_C_G0507_v1.md#neutral-factor-bounded-symbol) | Low-mode rank growth alone is insufficient; this accepted comparison is preserved. |
| support | [Exact support](Yin_C_G0143_v1.md#statement) | Earlier actual divergent-coherence family in its different measure range. |
| support | [Exact support](Yin_C_G0160_v1.md#statement) | Earlier actual fixed-positive-measure bounded family and disclosed upstream author relationship; no conflict or new near-one coverage. |
| review | [Exact review](../audits/reviews/Yin_R_G0417_v1.md#moving-salem-coherence-whole-independent-finding) | Complete statement, whole finite-to-torus argument, all15 formulas and eight input roles at the exact fixed Claim scope. |

