---
author: Yin
---
# Complete all-expanding Gaussian kernel, original weighted law and exact collision pressure

The complete original argument and every source/contribution/cost/domain/negative boundary are retained.
The original L remains meaningful development and a fixed review input; no research Task/E resumes.

## Statement

Let alpha be ANY nonzero algebraic integer with ACTUAL monic irreducible minimal polynomial P of degree d and TOTAL logarithmic Mahler measure m>0.
Include ALL exterior conjugates alpha_1,...,alpha_r, counting both nonreal members; actual characteristic-zero roots are distinct,1<=r<=d.
Set

    s=exp(-m), a0=log2, a=a0/s^2,
    H(z)=product_l(1-z/conj(alpha_l))/(1-alpha_l*z)
        =sum_(j>=0)h_j*z^j,h0=1.

The coefficients h_j are real, and the exact partial fraction expansion is

    H(z)=s^2+sum_l A_l/(1-alpha_l*z), A_l!=0,
    h_j=sum_l A_l*alpha_l^j for j>=1,
    h0=s^2+sum_l A_l=1, H(alpha_l)=0.

The last equality evaluates the RATIONAL function, not a Taylor series outside its convergence disk; every denominator1-alpha_b*alpha_l is nonzero.
For EVERY integer n>=1 let C_n be the UPPER h-coefficient matrix and define the nested real symmetric kernel

    K_(i,j)=a*sum_(k=0)^min(i,j)h_(i-k)*h_(j-k)
            -a0*1_(i=j),
    W_(b,l)=a*A_b*A_l*alpha_b*alpha_l/(alpha_b*alpha_l-1),
    K_(i,j)=sum_(b,l)W_(b,l)*alpha_b^i*alpha_l^j.

Every finite n block is a*C_n^T*C_n-a0*I, positive semidefinite of EXACT rank min(n,r); the first r-by-r block is positive definite.
The finite calculation includes i=j=0 and its single h0 correction a*s^2=a0, and uses the correct transposed Gram product rather than interchanging factors.

Let E be the conjugation-compatible REAL subspace of C^r, with one real coordinate per real root and real/imaginary coordinates per nonreal pair, of REAL dimension r.
On E define Phi(z)=sum_(b,l)W_(b,l)*z_b*z_l.
Conjugate pairing makes this expression real; the r Vandermonde vectors (alpha_l^j)_l,0<=j<r, form a real basis and prove Phi POSITIVE DEFINITE.
Let lambda_P>0 be its least eigenvalue in this specified real-coordinate Euclidean norm.
W is complex symmetric and is not asserted positive Hermitian on unrestricted C^r.

For ORIGINAL independent difference digits Pr(xi=0)=1/2,Pr(xi=+/-1)=1/4 and expanding endpoint X_n=(sum_(j=0)^(n-1)xi_j*alpha_l^j)_l in E, the COMPLETE finite unshifted identity is

    Gamma_n:=2^-n*sum_(e in{-1,0,1}^n)
                        exp[-a*norm(C_n e)^2]
            =E_original exp[-Phi(X_n)].

All3^n words and weights, all exterior embeddings and ALL n<r/n=r/n>r cases are retained.
The zero endpoint is exactly the original algebraic return event, not only the all-zero word.

Let q count ALL unit-circle conjugates including both nonreal members, and let

    C_st=product_(abs(alpha_i)<1)(1-abs(alpha_i))^-1,
    B=2^(d-r)*C_st,
    delta_n=(B*n^q)^(-1/r)<=1,
    C_P=[2^r*exp(lambda_P/4)*(2pi/lambda_P)^(r/2)/omega_r]*B,

where omega_r is the unit-ball volume in the stated REAL coordinates.
Empty stable/neutral products, all-expanding inputs and degree-one nonunits are included.
Distinct original difference-word endpoints have real Euclidean separation at least delta_n: coefficient differences have absolute value<=2, their nonzero integer norm includes EVERY d-r nonexpanding embedding and both complex exterior factors.
The maximum atom is p_n=Pr_original(sum_(j=0)^(n-1)xi_j*alpha^j=0) by finite binary-endpoint autocorrelation/Cauchy--Schwarz, without any unit-only state-kernel extension.
Disjoint radius-delta_n/2 balls and COMPLETE Gaussian integration give for EVERY n>=1

    p_n<=Gamma_n<=C_P*n^q*p_n.

The norm/packing constant retains the original degree d, all stable factors, neutral count q, real-space eigenvalue and every factor2.
For EACH FIXED input the original collision exponent exists and

    lim_n -log Gamma_n/n=h2(alpha)=lim_n -log p_n/n.

Writing Z_n=2^n*Gamma_n, c_a=1+2exp(-a), g(m)=log(2/c_a) and G_n=log(c_a^n/Z_n), also

    lim_n G_n/n=h2(alpha)-g(m).

There is no uniform bound on C_P, lambda_P, onset or convergence as the input changes.
The theorem identifies the complete UNshifted limiting inverse pressure without evaluating h2 or proving h2=m, positive recurrence, finite critical mean, a near-one entropy floor or a Mahler gap.
It does not replace an actual finite-position matrix by a growing limiting window under arbitrary translations, add overlapping loss certificates or discard any exterior/neutral/degree expense.
The concurrent D143 and other current unfinished arguments are motivation only, not consumed premises; every finite probability and fixed-input limit step is proved here.

<a id="argument"></a>
## Complete original argument

The following complete original author body is historical at its original date; its initial/pending/next-direction language supplies no current research authority.
Same-scope mathematical href maintenance does not backdate current home reading; every original L/R input and date remains fixed.

## Complete expanding-conjugate Gaussian kernel and original collision rate

<a id="full-expanding-gaussian-reuse"></a>
### Exact scope and changed question

Date:2026-10-10.
The coordinating AI for Yin authors this G0001 argument.
This complete self-reviewed author material is not independently reviewed or adopted.
D143 is separately frozen for review and is not changed by this further generalization.

The candidate extends the complete unshifted Gaussian comparison from one expanding conjugate to EVERY nonzero algebraic integer with positive total measure.
The direct inputs are [L268's exact inverse defect rank](Yin_C_G0475_v1.md#statement), [L83's complete norm separation](Yin_C_G0274_v1.md#norm-separation-with-central-loss) and [C560's maximum difference atom](Yin_C_G0560_v1.md#all-state-return-dominance).
D143's current proof is motivation, not a fixed dependency.
Its one-factor matrix and actual/analytic dyadic control will retain their distinct scopes.

The substantive new result is an exact fixed positive quadratic form on ALL expanding embeddings whose finite-word expectation equals the full unshifted limiting inverse partition.
A polynomial packing comparison then identifies its exponent with the original collision exponent, with every neutral and degree constant retained.
This is not an evaluation of that exponent, a translated actual-block estimate, a uniform-in-input convergence theorem or a positive gap.

<a id="full-expanding-positive-kernel"></a>
### 1. Exact kernel derivation

Let P be the actual monic irreducible minimal polynomial of a nonzero algebraic integer alpha, degree d, total logarithmic Mahler measure m>0.
Its r exterior roots alpha_1,...,alpha_r are distinct and closed under conjugation.
Put s=exp(-m), a0=log2 and a=a0/s^2.
Reuse L268's normalization

    H(z)=product_l (1-z/conj(alpha_l))/(1-alpha_l z)
         =sum_(j>=0) h_j z^j, h_0=1.

The coefficients are real.
The roots are simple because the actual irreducible polynomial has characteristic zero, and no exterior root has modulus at most1.
Therefore the partial fraction expansion has the form

    H(z)=s^2+sum_l A_l/(1-alpha_l z),     A_l !=0.      (1)

The constant at infinity is s^2 because the ratio of leading coefficients is product_l|alpha_l|^(-2).
Every residue is nonzero since numerator and denominator roots lie on opposite sides of the circle.
In particular

    h_j=sum_l A_l alpha_l^j for j>=1,
    h_0=s^2+sum_l A_l=1,
    H(alpha_l)=0.                                    (2)

The final identity uses closure under conjugation.
All denominators1-alpha_l alpha_b in its partial fractions are nonzero because their product has modulus greater than1.

For n>=1 let C_n be the upper triangular coefficient matrix, (C_n)_(i,j)=h_(j-i) for j>=i.
Define the nested real symmetric kernel

    K_(i,j)=a sum_(k=0)^min(i,j) h_(i-k)h_(j-k)
                        -a0 1_(i=j), i,j>=0.         (3)

Every finite n block is a C_n^T C_n-a0 I.
By L268 and the singular-value invariance under transpose it is positive semidefinite, with rank min(n,r); in particular its first r-by-r block is positive definite.
This does not transpose a product incorrectly: C_n is the transpose of the lower matrix, and both Gram products have the same positive singular-value squares.

For j>=i, replacing the h_(j-k) by its exponential expression has just one correction, at j=i=k.
Its amount a s^2=a0 cancels the diagonal subtraction in(3).
Hence

    K_(i,j)=a sum_l A_l alpha_l^j
                       sum_(k=0)^i h_(i-k)alpha_l^(-k).

Finite geometric summation and H(alpha_l)=0 give

    sum_(k=0)^i h_(i-k)alpha_l^(-k)
       =sum_b A_b [alpha_l alpha_b/(alpha_l alpha_b-1)]
                    alpha_b^i.

Consequently, for all i,j>=0 by symmetry,

    K_(i,j)=sum_(b,l) W_(b,l) alpha_b^i alpha_l^j,
    W_(b,l)=a A_b A_l alpha_b alpha_l/
                              (alpha_b alpha_l-1).    (4)

This is a symmetric complex coefficient expression representing a REAL form, not a Hermitian form on unrestricted complex coordinates.
Let E be the r-dimensional REAL conjugation-compatible subspace of C^r: coordinates on real roots are real and the coordinates at each conjugate pair are conjugates.
Identify it with one real coordinate per real root and real/imaginary coordinates per pair.
Define

    Phi(z)=sum_(b,l) W_(b,l) z_b z_l, z in E.

This expression is real by conjugate pairing.
The first r coefficient vectors v_j=(alpha_l^j)_l,0<=j<r, form a real basis of E: the complex Vandermonde is nonsingular, and its conjugation symmetry makes the inverse preserve real coefficients.
The positive definiteness of the first r kernel block in(3) therefore proves Phi is positive definite on E.
Let lambda_P>0 be its least eigenvalue in the stated real-coordinate Euclidean norm.
No positivity on the larger complex-coordinate space is asserted.

Let xi_j have the original law Pr(0)=1/2,Pr(+/-1)=1/4.
Its expanding-coordinate endpoint is

    X_n=(sum_(j=0)^(n-1) xi_j alpha_l^j)_l in E.

Equations(3)--(4) give the exact finite identity

    Gamma_n:=2^(-n) sum_(e in{-1,0,1}^n)
                         exp[-a||C_n e||^2]
          =E exp[-Phi(X_n)].                         (5)

All3^n words and weights are retained because exp(-a0 e^2)/2 is precisely the original law.
No outside translation or convergence-rate claim is made here.

<a id="full-expanding-soft-return-comparison"></a>
### 2. Complete arithmetic packing comparison

Let q be the number of unit-circle conjugates, counted with both members of complex pairs.
Put

    C_st=product_(|alpha_i|<1)(1-|alpha_i|)^(-1),
    B=2^(d-r) C_st, delta_n=(B n^q)^(-1/r)<=1.

For two distinct original difference-word endpoints, the coefficient difference is bounded by2.
The nonzero algebraic-integer norm and all d-r nonexpanding embeddings give product_(l=1)^r |z_l| >=1/(B n^q).
Each |z_l| is at most the Euclidean norm in the real coordinates of E, with both members of a complex pair counted in the product.
Distinct expanding endpoints are therefore at Euclidean distance at least delta_n.
They are indeed distinct: a nonzero algebraic number has no zero field embedding.

The original difference law has maximum atom at zero by the complete Cauchy--Schwarz argument of L232; write that atom p_n.
Since Phi>=lambda_P||.||^2, it remains to sum a Gaussian over a delta_n-separated set in R^r.
The radius delta_n/2 balls are disjoint.
For x in the ball centered at z,

    ||z||^2 >= ||x||^2/2-delta_n^2/4.

Integrating the resulting pointwise inequality over each ball and summing yields, with omega_r the unit-ball volume,

    sum_z exp[-lambda_P||z||^2]
      <= 2^r exp(lambda_P/4) (2pi/lambda_P)^(r/2)
                         /(omega_r delta_n^r)
      =C_P n^q,

where C_P is the displayed finite input-dependent constant times B.
The complete original support is finite, so this summation needs no convergence interchange.
Thus(5) gives

    p_n <= Gamma_n <= C_P n^q p_n.                   (6)

The lower bound is its exact zero term.
Independent zero blocks and p_n>=2^(-n) give existence of the collision exponent, as in D143's elementary argument, independently of its unadopted conclusions.
For each fixed input, (6) then identifies

    lim -log Gamma_n/n = h2(alpha).                  (7)

No uniformity in P, r, degree, neutral count, lambda_P or m is supplied.
The positive form generally depends on all expanding roots and residues; replacing it by one root or by an uncharged scalar determinant invalidates the claimed comparison.
The complete author check is recorded below; independent review remains required before fixed adoption.

<a id="full-expanding-gaussian-rate"></a>
### 3. Complete conclusion, costs and author self-check

The preceding derivation proves(1)--(7) for every nonzero algebraic integer whose actual total logarithmic Mahler measure is positive.
To spell out the finite probability point, the expanding-coordinate map is injective on field elements because any one field embedding is injective.
Its zero atom is therefore exactly the original p_n, and its maximum atom is at zero: writing its law as the difference of two independent finite binary endpoint laws, Cauchy--Schwarz gives mu_n(z)<=sum_x nu_n(x)^2=p_n for every z.
Thus neither the packing step nor the use of all expanding coordinates changes a single original probability.

Existence of the limit in(7) needs no new pressure theorem.
Independent zero blocks imply p_(n+k)>=p_n p_k.
For n=lk+t with0<=t<k, p_n>=p_k^l 2^(-t), so limsup(-log p_n/n)<=-log p_k/k for every k.
Taking the infimum yields the limit.
The logarithm of C_P n^q divided by n tends to zero for this fixed input, proving(7) from both sides of(6).

Set c_a=1+2exp(-a), g(m)=log(2/c_a) and G_n=log(c_a^n/Z_n), where Z_n=2^n Gamma_n is the complete unshifted partition from(5).
The exact normalization gives also

    lim_(n->infinity) G_n/n=h2(alpha)-g(m).           (8)

The actual inverse coefficients, their full real quadratic form and the whole digit cube carry precisely the original collision exponent.
This generalizes the single exterior real coordinate without treating several growing conjugates as one.
It does not calculate h2(alpha), prove h2=m, or show a positive gap.
All degree, neutral count, root-shape and least-eigenvalue expenses are explicit in C_P; no uniform bound on that constant or a common onset is asserted.

This is a statement about the COMPLETE unshifted limiting inverse matrix, not its actual finite-position predecessor.
L263/L268's fixed-window convergence does not by itself permit a growing-window substitution in an arbitrary translated finite collision upper bound.
Conversely, the direct finite identities and norm packing here require no such substitution: their left side is explicitly defined and their right side is the original n-digit law.
A later use requiring outside-tail translations must prove that further interface.
General spectral eigenvalues alone do not determine the form Phi relative to the original digit lattice.

The author checked the H normalization and value at infinity, simple-pole residues, the use of H(alpha_l)=0 through conjugate closure, exact finite geometric summation including i=j=0, upper/lower matrix orientation, all n<r and n=r rank boundaries, the conjugation-compatible REAL space and Vandermonde basis, positive definiteness from the complete first r block, maximum-atom and zero-injectivity identities, every factor2 in the norm bound, the r-dimensional packing volume and fixed-input exponent limit.
In particular W is not called positive Hermitian on C^r, complex conjugate embeddings are counted twice in the norm but only once as two real coordinates, and the original degree is never replaced by r in an arithmetic norm.
No current D140--D143 result supplies a proof premise.
No new computation or source acquisition was performed.
The entire written argument is ready for a separate complete noncontributor review; no fixed adoption or Task completion is asserted.

Author freeze:2026-10-10T03:11.
Entire scope, Sections1--3 and equations(1)--(8) passed the complete author self-check and scoped material check1.
This additional generalization was developed after D143 froze, without consuming its unfinished review or altering its original body.
No new program or source.
Ready for whole separate noncontributor review.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:55 |
| status | open |
| reason | Register the complete original theorem and every actual domain, finite/infinite quantifier, full probability, source, contribution, cost and negative boundary. Sufficient existing inputs are reused; inspection of the actually written whole target, a real whole finding and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete all-expanding pressure theorem](#statement) | EVERY actual nonzero positive-total-measure algebraic integer/full exterior multiset/exact residue kernel/REAL positive form/ALL finite n/original word law/complete norm-packing costs/fixed-input rates and every nonclaim boundary. |
| argument | [Entire original proof](#argument) | Original starting/reuse/Sections1--3/equations1--8/every residue and h0 cancellation/finite geometric identity/upper-transpose orientation/n-r boundaries/real Vandermonde positivity/all original probabilities/complete norm-packing/constants/limits/source-contribution-self-check and negative scope. |
| dependency | [Exact finite defect rank](Yin_C_G0475_v1.md#finite-inner-compression-exact-rank) | Entire actual inverse normalization/isometry/coprime finite kernel/rank min(n,r)/PSD Gram, explicitly including n<r and transpose singular-value invariance; no later lag detection or source-wide re-audit. |
| support | [Full norm-separation mechanism](Yin_C_G0274_v1.md#norm-separation-with-central-loss) | Complete existing actual unit/binary norm/stable-neutral/complex counting comparison; present proof supplies its own full nonunit doubled-coefficient word argument. |
| support | [Original finite maximum atom](../ledger/Yin_L_G0232_v1.md#all-state-return-dominance) | Exact original unit/core autocorrelation input; present local finite proof covers every original difference-word law without extending that kernel. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:08 |
| status | proved |
| reason | The actually written open Statement and complete Argument have been fully read and checked under the explicit entire SELF finding. Adopt the complete fixed-input original-law theorem with every actual root, real-space, degree, stable-neutral and eigenvalue cost. R712v2 corrects only its own explanatory review notation; the target proof was already correct. Original R130 whole UNKNOWN and the separate isolated-coverage obligation remain; no research Task/E resumes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete all-expanding pressure theorem](#statement) | EVERY actual nonzero positive-total-measure algebraic integer/full exterior multiset/exact residue kernel/REAL positive form/ALL finite n/original word law/complete norm-packing costs/fixed-input rates and every nonclaim boundary. |
| argument | [Entire original proof](#argument) | Original starting/reuse/Sections1--3/equations1--8/every residue and h0 cancellation/finite geometric identity/upper-transpose orientation/n-r boundaries/real Vandermonde positivity/all original probabilities/complete norm-packing/constants/limits/source-contribution-self-check and negative scope. |
| dependency | [Exact finite defect rank](Yin_C_G0475_v1.md#finite-inner-compression-exact-rank) | Entire actual inverse normalization/isometry/coprime finite kernel/rank min(n,r)/PSD Gram, explicitly including n<r and transpose singular-value invariance; no later lag detection or source-wide re-audit. |
| support | [Full norm-separation mechanism](Yin_C_G0274_v1.md#norm-separation-with-central-loss) | Complete existing actual unit/binary norm/stable-neutral/complex counting comparison; present proof supplies its own full nonunit doubled-coefficient word argument. |
| support | [Original finite maximum atom](Yin_C_G0560_v1.md#all-state-return-dominance) | Exact original unit/core autocorrelation input; present local finite proof covers every original difference-word law without extending that kernel. |
| review | [Entire current SELF finding](../audits/reviews/Yin_R_G0712_v2.md#full-expanding-whole-self-finding) | ENTIRE actual Statement and complete original Argument, all three sections/equations1--8, every actual exterior root/residue/h0 finite cancellation/transpose rank/REAL positivity/original word law/full norm-packing and all finite/infinite/source/contribution/negative scope. |
