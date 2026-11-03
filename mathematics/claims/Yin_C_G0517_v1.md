---
author: Yin
---

# Complete actual finite inverse pressure, prefix costs and real-tail geometry

This organizes the complete original2026-10-10 result from [L282](../ledger/Yin_L_G0282_v1.md#complete-retained-proof-and-review).
The entire original argument and fixed input/source/review history remain below at their actual scope; their dated active/pending language supplies no present Task/E authority.

## Statement

Let P be the ACTUAL monic irreducible minimal polynomial of a nonzero algebraic integer alpha, of degree d>=1, with total m=log M(P)>=0.
Nonunits and torsion are included in every finite assertion below.
Let xi_j be independent ORIGINAL digits with probabilities Pr(0)=1/2 and Pr(+/-1)=1/4, put p_n=Pr(sum_(j<n)xi_j alpha^j=0), p_0=1, and retain the established collision exponent h2=lim -log(p_n)/n.
In the actual integral power basis, M is multiplication by alpha and v represents1.
Define z_j=-M^(d+j)v, A_k=[z_0 ... z_(k-1)] and A_0 empty; M is invertible over R because P(0)!=0, without a unimodularity assumption.

For EVERY integer k>=1, N=d+k, monic division and all original weights give exactly

    p_N=2^-d E[exp(-a0||A_k xi||^2) 1_(||A_k xi||_infinity<=1)],
    Q_N=2^-d E exp(-a0||A_k xi||^2), a0=log2,
    p_N<=Q_N<=Theta^d p_N,
    Theta=sum_(z in Z)2^(-z^2), 1<Theta<15/7.

The endpoint zero atom is exactly p_k and every endpoint atom is at most p_k, also for nonunits.
The complete finite error is at most d log Theta, so Q_N has exponent h2 at FIXED P.
No varying-degree/time interchange or free repetition certificate follows.

For every integer i>=0 and b>=1, let X=[z_i ... z_(i+b-1)], W_i=(I_d+A_i A_i^T)^-1 and D_i=det Gram(P,...,t^(i-1)P), with D_0=1.
The ACTUAL nested digit-coordinate matrix T=R U^-1 and pivots delta_j have their original shifted-polynomial/Gram--Schmidt definitions.
For its b-by-b diagonal block C and Lambda=diag(delta_(i+1),...,delta_(i+b)),

    det(W_i)^-1=D_i,
    C^T Lambda C=I_b+X^T W_i X,
    W_(i+b)=(W_i^-1+XX^T)^-1
      =W_i-W_i X(I_b+X^T W_i X)^-1 X^T W_i.

These are real quadratic-form identities, not discrete prefix integration or conditional digit independence.
The COMPLETE unshifted block is exactly

    G_(i,b)=2^-b sum_(e in{-1,0,1}^b)
                  exp[-a0(Ce)^T Lambda(Ce)]
           =E exp[-a0(Xxi)^T W_i(Xxi)],
    p_b<=G_(i,b)<=Theta(W_i)p_b<=K_d sqrt(D_i)p_b,
    Theta(W)=sum_(z in Z^d)exp(-a0 z^T Wz),
    K_d=2^(d/4)(2pi/a0)^(d/2).

For i>=1, with Delta=|disc P|>=1 and degree-one Delta=1, the complete cost is

    Delta D_i<=(i+d)^d exp[2m(i+d-1)],
    0<=log G_(i,b)-log p_b
      <=log K_d+mi+(d/2)log(i+d)-(1/2)log Delta+m(d-1).

At i=0 the direct Theta^d bound applies.
For EVERY sequence of nonnegative INTEGER prefixes i_b=o(b), at FIXED P and b tending to infinity, G_(i_b,b) has exponent h2.
This includes bounded, zero and nonmonotone subsequences; it gives no input-uniform rate or arbitrary late-prefix limit.

For any finite total k>=i+b+d, let Y be all actual subsequent remainder columns and f any real future coefficient vector, with u=Yf.
The actual outside shift is

    x=Lambda^-1 C^-T X^T W_i u,
    x^T Lambda x=u^T(W_i-W_(i+b))u.

The entire finite REAL outside-tail span has dimension min(b,d), because any d consecutive future columns span R^d.
Bounded original digit tails need not fill that span.
For the translated COMPLETE block,

    G_(i,b)(x)=2^-b sum_e exp[-a0(Ce+x)^T Lambda(Ce+x)]
      =exp[a0 u^T W_(i+b)u]
           E exp[-a0(Xxi+u)^T W_i(Xxi+u)].

The POSITIVE prefactor is retained.
For b<d the representing u need not be unique; the product is invariant under the resulting choice, not necessarily either scalar factor separately.

Only when m>0, the existing fixed-diagonal/pivot limits and full expanding real kernel identify the LIMITING tail-span rank min(b,r), where r counts all expanding real dimensions, with each complex conjugate pair counted twice.
They provide no uniform arbitrary-tail convergence.
For the actual golden minimal polynomial t^2-t-1, d=2 and r=1: every b>=2 has finite tail rank2 when enough future coordinates are present, versus limiting rank1.
This refutes the proposed inference from entrywise convergence alone to replacing an entire finite-tail span in a supremum.
It does NOT prove that the two optimized exponents differ, or obstruct every constrained original-digit-tail argument.
All original reuse/source/contribution/failed-inference and expense limits are part of this complete fixed scope.
No h2=m, all-real-translation maximum theorem, critical-moment conclusion, uniform near-one entropy floor, unrestricted gap or Task completion is asserted.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:47 |
| status | open |
| reason | Register the exact complete theorem and entire unchanged original argument at their proper C home; actual written whole inspection and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every nonzero algebraic integer/nonunit/torsion finite case; exact original hard-soft pressure/full prefixes/REAL tail rank and positive completion, fixed-input sublinear-prefix limit, distinct m>0 limiting rank and all negative scopes. |
| argument | [Exact argument](#argument) | Entire original Sections1--5/equations1--18, exact remainder/Gram/Schur/cube proofs, all constants and determinant/discriminant/time costs, golden control, author/reuse/source/no-program and inference limits. |
| dependency | [Exact dependency](Yin_C_G0436_v1.md#exact-return-integral-gaussian-partition) | Complete original monic quotient, hard cube and all exact original digit weights; no replacement Gaussian probability law. |
| support | [Exact support](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | Only the already proved full pivot-product comparison and its weaker g(m) rate; it is distinct from the complete finite pressure. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#true-digit-coordinate-square-matrix) | Actual rational Gram--Schmidt R, integral unit-upper U, nested true digit-coordinate T=R U^-1 and full pivots. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#all-lag-actual-center-limits) | Fixed-lag inverse coefficient and pivot limits at m>0 only; no growing-window or arbitrary-tail uniform limit. |
| dependency | [Exact dependency](Yin_C_G0448_v1.md#finite-pivot-limit-and-boundary) | Full-root integer Gram/discriminant estimate on every nonzero algebraic integer, including nonunits/torsion; separate unit-only operator use is not imported. |
| dependency | [Exact dependency](../ledger/Yin_L_G0232_v1.md#all-state-return-dominance) | Original fair-binary autocorrelation atom maximum; its elementary proof is recalled here to cover nonunits, without extending the unit state kernel. |
| dependency | [Exact dependency](Yin_C_G0503_v1.md#full-expanding-positive-kernel) | Complete positive form on the conjugation-compatible expanding REAL space, all root dimensions and nested cross-kernel identity. |
| dependency | [Exact dependency](Yin_C_G0509_v1.md#actual-tail-space-completion) | Entire limiting-tail parametrization and positive translation compensation at the stated m>0 scope, not replacement of actual finite matrices. |


### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:53 |
| status | proved |
| reason | Adopt the entire exact finite-pressure theorem and unchanged18-equation proof after actual written whole inspection and its explicit current SELF finding; all real-tail/limiting-tail distinctions, original-law costs, R135 UNKNOWN and original author SELF remain. No research Task/E, source acquisition or mathematical program is executed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every nonzero algebraic integer/nonunit/torsion finite case; exact original hard-soft pressure/full prefixes/REAL tail rank and positive completion, fixed-input sublinear-prefix limit, distinct m>0 limiting rank and all negative scopes. |
| argument | [Exact argument](#argument) | Entire original Sections1--5/equations1--18, exact remainder/Gram/Schur/cube proofs, all constants and determinant/discriminant/time costs, golden control, author/reuse/source/no-program and inference limits. |
| dependency | [Exact dependency](Yin_C_G0436_v1.md#exact-return-integral-gaussian-partition) | Complete original monic quotient, hard cube and all exact original digit weights; no replacement Gaussian probability law. |
| support | [Exact support](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | Only the already proved full pivot-product comparison and its weaker g(m) rate; it is distinct from the complete finite pressure. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#true-digit-coordinate-square-matrix) | Actual rational Gram--Schmidt R, integral unit-upper U, nested true digit-coordinate T=R U^-1 and full pivots. |
| dependency | [Exact dependency](Yin_C_G0459_v1.md#all-lag-actual-center-limits) | Fixed-lag inverse coefficient and pivot limits at m>0 only; no growing-window or arbitrary-tail uniform limit. |
| dependency | [Exact dependency](Yin_C_G0448_v1.md#finite-pivot-limit-and-boundary) | Full-root integer Gram/discriminant estimate on every nonzero algebraic integer, including nonunits/torsion; separate unit-only operator use is not imported. |
| dependency | [Exact dependency](Yin_C_G0560_v1.md#all-state-return-dominance) | Original fair-binary autocorrelation atom maximum; its elementary proof is recalled here to cover nonunits, without extending the unit state kernel. |
| dependency | [Exact dependency](Yin_C_G0503_v1.md#full-expanding-positive-kernel) | Complete positive form on the conjugation-compatible expanding REAL space, all root dimensions and nested cross-kernel identity. |
| dependency | [Exact dependency](Yin_C_G0509_v1.md#actual-tail-space-completion) | Entire limiting-tail parametrization and positive translation compensation at the stated m>0 scope, not replacement of actual finite matrices. |
| review | [Exact review](../audits/reviews/Yin_R_G0728_v1.md#current-finite-pressure-whole-self-finding) | ENTIRE actual current Statement and complete unchanged original Argument, every input/interface/source/native/cost/negative boundary; this actual maintaining whole finding is SELF, not isolated independent replacement. |

## Complete original argument

<a id="argument"></a>

## Actual finite inverse pressure, boundary cost and full tail rank

Date:2026-10-10.
The coordinating AI for Yin develops this argument for the actual G0001 contract.
All candidate routes remain active.
This is an author argument pending full separately organized review, not a resolution of the unrestricted gap.

<a id="finite-pressure-reuse"></a>
### 1. Changed question and responsible premises

[L278](../ledger/Yin_L_G0278_v1.md#tail-translation-pressure-fixed-scope) proves that maximizing the limiting inverse Gaussian partition over its entire outside-tail space preserves exponent h2.
It expressly does not substitute actual finite quotient matrices or growing windows.
The present question examines those actual matrices before making such a substitution.

The local reuse screen by full Gaussian partition, discarded boundary constraints, finite tail rank, remainder maps and relative zero-atom bounds located [L256](../ledger/Yin_L_G0256_v1.md#triangular-gram-collision-bound), [L263](../ledger/Yin_L_G0263_v1.md#true-digit-coordinate-square-matrix), [L260](../ledger/Yin_L_G0260_v1.md#finite-pivot-limit-and-boundary), [L232](../ledger/Yin_L_G0232_v1.md#unrooted-stationary-variational-extension), L277 and L278.
The exact quotient/Gram representation and fixed-diagonal convergence are reused from L263; the full-root determinant estimate is the actual inequality retained in L260, with its L4 provenance.
The original difference-law atom maximum is the elementary binary-autocorrelation Cauchy--Schwarz calculation already retained in L232/L277; its proof is recalled to cover nonunits explicitly.
These inputs are sufficient.
The finite remainder and square-completion calculations below are direct consequences, not an invocation of a new source theorem.
No additional external input, numerical experiment or J is used, and no historical novelty claim is made.

Write P(t)=t^d+...+p0 for the actual monic minimal polynomial of a NONZERO algebraic integer alpha, d>=1, with m=log M(P)>=0.
Nonunits and torsion are allowed in Sections2--5.
Let a0=log2.
Original independent digits xi have Pr(0)=1/2 and Pr(+/-1)=1/4.
Write p_n=Pr(sum_(j=0)^(n-1)xi_j alpha^j=0), with p0=1 when this subscript denotes a probability; the polynomial constant coefficient above is written P(0) below to avoid ambiguity.
The actual collision exponent h2=lim -log(p_n)/n is the existing original-law limit.
No degree normalization or law change is made.

In the power basis1,alpha,...,alpha^(d-1), let M be multiplication by alpha and v the coordinate vector of1.
M is an INTEGER d-by-d matrix and is invertible over R because P(0)!=0.
It need not be unimodular.
For j>=0 define
    z_j=-M^(d+j)v, A_k=[z_0 ... z_(k-1)], A_0 empty.
All these columns are integer vectors.
They are minus the coefficient remainder of t^(d+j) modulo P.
The first d orbit vectors v,Mv,...,M^(d-1)v are the power basis, so EVERY consecutive d columns z_j are linearly independent.
Smaller consecutive sets are also independent.

The parallel D150--D152 arguments are not premises.
All new derivations below are by the coordinator; no sibling has contributed their proof.

<a id="integer-boundary-softening"></a>
### 2. Exact integer boundary and its degree-only total cost

For N=d+k with k>=1, choose the LAST k original coefficients e=(xi_d,...,xi_(d+k-1)).
Monic division gives a unique polynomial divisible by P with those last k coefficients.
Its first d coefficients are exactly A_k e: the lower polynomial cancels the remainder of sum_j e_j t^(d+j).
Thus the original return identity is
    p_(d+k)=2^(-d) E[
         exp(-a0||A_k xi||^2) 1_(||A_k xi||_infinity<=1)],
                                                             (1)
where xi now consists of k ORIGINAL independent digits.
The factor2^(-d) and the Gaussian factor give exactly the probabilities of the first d digits when they are0,+/-1.
Outside that set the indicator is essential.
No quotient multiplicity remains.

Define the COMPLETE boundary-softened certificate
    Q_(d+k)=2^(-d) E exp(-a0||A_k xi||^2),
    Theta=sum_(n in Z)2^(-n^2).                             (2)
Then, uniformly over every actual P and every k>=1,
    p_(d+k)<=Q_(d+k)<=Theta^d p_(d+k),
    1<Theta<15/7.                                         (3)
In particular the entire discarded boundary costs at most d log Theta, independently of coefficients, root separation and k.

Here is the full comparison.
If nu is the finite endpoint law of the corresponding independent fair binary sum, the original difference law is mu(z)=sum_y nu(y)nu(y-z).
Cauchy--Schwarz gives mu(z)<=sum_y nu(y)^2=mu(0).
This applies to the integer map A_k without any unit assumption.
Since M^d is invertible, A_k xi=0 if and only if sum xi_j alpha^j=0.
Therefore mu(0)=p_k.
Summing over the ACTUAL integer endpoint support, then enlarging only a nonnegative Gaussian sum to Z^d, gives
    p_k<=E exp(-a0||A_k xi||^2)<=Theta^d p_k.              (4)
The lower inequality is the zero atom.
Independently the event consisting of d initial zero digits followed by a returned k-word has probability2^(-d)p_k, and hence p_(d+k)>=2^(-d)p_k.
This also follows from (1)'s zero endpoint.
Combining it with (4) proves the upper bound in (3); (1) proves its lower bound.
No comparison of a finite p_k with its infinite-time exponent is used.

For the numerical constant, the n=0,+/-1 terms sum to2.
For n>=2, n^2>=4+3(n-2), with strictness for some n.
Thus sum_(n>=2)2^(-n^2)<(1/16)/(1-1/8)=1/14, giving Theta<2+1/7.
The exact Theta is retained in (3); no decimal approximation is needed.

At every fixed input, (3) yields
    lim_(N->infinity) -log Q_N/N=h2.
At varying degree the explicit error remains
    0<=log Q_N-log p_N<=d log Theta.                    (5)
Thus replacing these d hard boundary inequalities by their COMPLETE Gaussian weight loses no fixed-input exponent.
This is not a claim that subsequently estimating that complete sum by independent triple maxima is sharp: L260 proves that that further product has only rate g(m).
It also does not evaluate the exponential-size complete sum, bound h2 uniformly away from0, or allow free repetition of one finite return probability.

<a id="finite-prefix-schur-remainder"></a>
### 3. Exact finite prefix geometry and complete unshifted block

Use L263's actual matrices.
B_(d+k) has columns P,tP,...,t^(k-1)P in every coefficient row; U_k is its unit upper triangular last-k-row block.
In the coefficient ordering used above,
    B_(d+k) U_k^(-1) = [ A_k ; I_k ],
    U_k integral, det U_k=1.                            (6)
The upper block is precisely the remainder calculation in Section2.
Let F_j be the monic Gram--Schmidt residual of t^jP, squared norm delta_(j+1).
If R is its upper expansion matrix and T=R U^(-1), the nested identities are
    T_k^T diag(delta_1,...,delta_k) T_k=I_k+A_k^T A_k.
                                                               (7)
This is L263's actual finite energy, now with an explicit integer boundary map.
Extending k changes no existing column of A or entry of T.

For i>=0 put
    W_i=(I_d+A_i A_i^T)^(-1), D_i=det(B_(d+i)^T B_(d+i)),
    D_0=1.
Here 0<W_i<=I.
Taking determinants in (6), and eliminating the block matrix with diagonal identities in either order, proves
    det(W_i)^(-1)=det(I_i+A_i^T A_i)=D_i.                (8)
This is a finite block-elimination identity; it does not replace an integer determinant by an approximation.

Take a consecutive block of b>=1 coordinates beginning at i.
Write
    X=[z_i ... z_(i+b-1)],
    C=T_[i,i+b),[i,i+b), Lambda=diag(delta_(i+1)...,delta_(i+b)).
Eliminating the first i REAL coordinates in the quadratic form (7) gives exactly
    C^T Lambda C=I_b+X^T W_i X,
    W_(i+b)=W_i-W_i X(I_b+X^T W_i X)^(-1)X^T W_i
           =(W_i^(-1)+X X^T)^(-1).                     (9)
For example, completing the prefix square in
||u||^2+||e||^2+||A_i u+Xe||^2
leaves ||e||^2+(Xe)^T W_i(Xe).
The second identity follows by the same completion on the next block; multiplication by W_i^(-1)+XX^T verifies its inverse form.
These are identities for the existing Gram elimination.
They do NOT integrate out or approximate the original finite digit sum.

The complete unshifted actual block partition is therefore
    G_(i,b)=2^(-b) sum_(e in{-1,0,1}^b)
                         exp[-a0 (Ce)^T Lambda(Ce)]
           =E exp[-a0 (X xi)^T W_i(X xi)].              (10)
Again the factor2^(-b)exp(-a0||e||^2) is EXACTLY the original difference-word weight.
X is an injective fixed linear map on the actual algebraic endpoint, so its zero atom is p_b and all its atoms are at most p_b.
Define the finite lattice sum
    Theta(W)=sum_(z in Z^d) exp(-a0 z^T W z), W>0.
Then
    p_b<=G_(i,b)<=Theta(W_i) p_b.                       (11)
This is valid for all i,b without a root-separation or unit hypothesis.
At i=0, W_0=I and Theta(W_0)=Theta^d, recovering the original total certificate.

There is an explicit determinant cost.
Set
    K_d=2^(d/4) (2pi/a0)^(d/2).
For 0<W<=I,
    Theta(W)<=K_d /sqrt(det W).                        (12)
To prove this, assign to each z the unit cube z+[-1/2,1/2]^d.
If x lies in it, the squared W-norm triangle inequality in the form
x^T W x<=2 z^T W z+2(x-z)^T W(x-z)
and W<=I imply z^TWz>=x^TWx/2-d/4.
Integrate
exp(-a0 z^TWz)<=2^(d/4)exp(-a0 x^TWx/2)
over that cube and sum.
The disjoint cubes cover R^d up to boundaries; the product Gaussian integral after an orthogonal change of coordinates is (2pi/a0)^(d/2)/sqrt(det W).
Nonnegative summation justifies the passage without a support or convergence presumption.

The actual full-root determinant estimate retained in L260 is, for i>=1 and Delta=|disc P|>=1,
    Delta D_i<=(i+d)^d exp[2m(i+d-1)].                 (13)
Its hypotheses are exactly the present monic irreducible nonzero algebraic integer.
For d=1 use Delta=1.
Combining (8),(11)--(13) gives
    0<=log G_(i,b)-log p_b
       <=log K_d +m i+(d/2)log(i+d)
                        -(1/2)log Delta+m(d-1).        (14)
The right side retains EVERY degree/discriminant/prefix cost.
In particular for a FIXED actual P and any nonnegative integer sequence i_b=o(b),
    lim_(b->infinity) -log G_(i_b,b)/b=h2.              (15)
For bounded i_b use (11) directly or the displayed bound and i=0 case.
For unbounded sublinear i_b the right side of (14), divided by b, tends to0.
No assertion uniform in P or for arbitrarily late prefixes i_b is made.
This proves a nontrivial growing-window actual-matrix comparison without interchanging the entrywise limiting matrix with an infinite digit sum.

<a id="actual-finite-tail-space-rank"></a>
### 4. Actual finite tail rank and its positive completion expense

There is a crucial distinction for translations.
In (7), allow at least d further tail coordinates, with their boundary column matrix Y=[z_(i+b)...,z_(k-1)].
Let f be an arbitrary REAL tail vector and u=Yf.
Let x=T_[i,i+b),[i+b,k) f be the shift appearing in this actual block.
Prefix square completion gives the cross identity
    C^T Lambda x=X^T W_i u,
    x=Lambda^(-1) C^(-T) X^T W_i u.                   (16)
The at-least-d consecutive tail columns span R^d, while rank X=min(b,d).
All displayed matrices outside X are invertible.
Hence the ENTIRE real span of actual finite outside-tail shifts has EXACT dimension
    min(b,d),                                         (17)
for every finite i and every k>=i+b+d.
This uses the FULL actual polynomial, including stable and neutral conjugates.
It is not a statement that bounded original digit tails fill that real span.

Equation (9) implies
    x^T Lambda x=u^T(W_i-W_(i+b))u.
Thus the complete normalized translated block is exactly
    G_(i,b)(x)
       =exp[a0 u^T W_(i+b)u]
             E exp[-a0 (Xxi+u)^T W_i(Xxi+u)].          (18)
Every original probability and the positive completion factor is present.
If b<d, u can be nonunique; (16) fixes x and the combined expression in (18) is independent of that representative, as is clear by expanding the square.
Individual factors need not separately be independent.
Formula (18) is not the unshifted inequality (11) with the positive factor erased.

For each fixed b and fixed future offset, L263 proves T_(i,i+l)->h_l and delta_(i+1)->exp(2m) as i tends to infinity when m>0.
L277/L278 show that the ENTIRE limiting outside-tail span instead has dimension min(b,r), where r is the number of expanding conjugates, including both members of complex pairs.
If r<d and b>r, its dimension is strictly smaller than (17).

For an actual nontorsion unit control take P=t^2-t-1, irreducible by its nonsquare discriminant5.
Its roots are (1+sqrt5)/2>1 and (1-sqrt5)/2 of modulus below1.
Thus d=2,r=1.
Every actual finite block with b>=2 and at least two future coordinates has two-dimensional tail span, whereas its limiting tail span is one-dimensional.
This is an actual algebraic input, not an arbitrary analytic pole list.

Consequently fixed-entry convergence alone cannot justify replacing the supremum over every actual finite tail by L278's supremum over its smaller limiting span.
Nonzero but small directions can disappear in the limit, while an unrestricted real-span supremum permits arbitrarily large coefficients along them.
This is a precise rank obstruction to that proposed inference, not a proof that the two supremum exponents differ.
A bound for actual ORIGINAL future digit tails could still exploit their constrained coefficients; (17) does not dismiss that possibility.

<a id="finite-pressure-outcome"></a>
### 5. Consequence and remaining discriminating question

The complete initial finite Gaussian certificate already captures the exact original collision exponent, and differs from the exact finite p_N by at most the coefficient-independent factor Theta^d.
Therefore the weak rate of the subsequently factorized pivot product is not caused by an uncontrolled exponential loss in the first d discarded constraints.
The full finite sum retains the decisive coupled arithmetic.
This changes which simplification must be improved.

More generally, (10)--(15) retain the entire actual finite unshifted block and prove its exponent on sublinear prefix offsets, paying the complete determinant cost.
On the other hand, (16)--(18) identify the actual finite translated geometry and explain exactly why a direct transfer of the limiting-tail supremum theorem by entrywise convergence would omit directions and a positive expense.

Next seek control of the CONSTRAINED original future tails in (18), or evaluate the complete integer-remainder expectation using new arithmetic structure.
A paid finite block may be useful only after its original-law repetition/whole-state expense is included; neither (3) nor (15) supplies that for free.
A uniform near-one argument must still manage varying degree, input, time and any additional costs.
No h2=m assertion, all-real-translation maximum theorem, critical-moment result or positive Mahler gap follows.
Other active routes remain available.

Author self-check: verified monic remainder signs and row order, injectivity for nonunits, every original2^(-d) and2^(-b) weight, the zero-atom comparison and theta bound, determinant equality and the full discriminant exponent, all i=0/d=1/torsion boundaries, growing-prefix quantifiers, order of inverses in (16), dimension of both finite and limiting tail spaces, nonunique u in (18), and the golden-unit control.
No program, finite search or numerical approximation is used.
Whole separate review and fixed adoption remain pending.



Author freeze:2026-10-10T04:13.
Complete Sections1--5 and equations(1)--(18) are frozen for whole separate noncontributor review.
The coordinator authored all new calculations, performed the stated self-check and passed the scoped material check.
No program was run.
No independent review or fixed adoption is implied by this freeze.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0135_v1.md#complete-separate-noncontributor-review), with its original inspected scope and relationship.
