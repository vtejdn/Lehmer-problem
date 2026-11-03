---
author: Yin
---

# Cyclotomic nonvanishing and exact jet costs for sparse multiples of H35

Human author Yin.
The paid_comparison contributor developed the complete argument on 2026-10-23 under the active G0001 continuation.
Root assigned the discriminating multiplier follow-up and authorized registration, without supplying its proof.
The complete author argument is retained here; the selected assessment owns the later independent whole review and adoption.
No native program, parameter enumeration or new source acquisition was performed.

## Statement

Use the UNREDUCED polynomials

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3.

**A. Coprime-order nonvanishing.**
Let P in Z[z], n>=1, and let zeta be a primitive nth root with P(zeta)!=0.
Then

    gcd(n,6)=1  implies H23(zeta)!=0,
    gcd(n,10)=1 implies H25(zeta)!=0,
    gcd(n,15)=1 implies H35(zeta)!=0.              (1)

All norms used here are in Q(zeta), of FULL degree phi(n), including n=1,2.
In particular, if P is monic irreducible nontorsion, every cyclotomic factor of H35 has order divisible by3 or5.
The theorem does not exclude those latter orders.
The explicit monic irreducible reciprocal nontorsion control

    P_*(z)=z^4-1567z^3+3294z^2-1567z+1             (2)

has totally real actual trace field and Phi_3 divides its H35.
It fails the full residual equation f=0, as checked below.
Thus total reality and nontorsion do not enlarge (1) to an all-order exclusion.

**B. Exact multiplier jet inequality.**
Let P in Z[z] be monic nonconstant with P(0)=1 and no cyclotomic factor, d=deg P, and H=H35.
For any nonzero D in Z[z] put

    N=D H, L=deg N=15d+deg D,
    M=||N||_1, K=#supp(N).

For each n>=1 coprime to15 define

    R_n=abs Res(Phi_n,H)>0,
    Delta_n=abs Norm_(Q(zeta_n)/Q) Phi_n'(zeta_n)>0,
    k_n=ord_(Phi_n)D.

These R_n and Delta_n are positive integers, and Delta_n is the absolute polynomial discriminant of Phi_n; Delta_1=Delta_2=1.
Then

    0<=k_n<=K-1,
    R_n Delta_n^(k_n)
           <=[M binom(L,k_n)]^(phi(n)).            (3)

The actual norm of the nonvanishing residual factor D/Phi_n^(k_n) is retained in the proof and only then bounded below by1.
No upper bound on coefficients or Mahler measure of D, no original residual equation and no total-real hypothesis is required for (3).
The bound applies in particular to every candidate D of C605.

**C. Finite additive degree obstruction.**
Fix an integer delta_cap>=0, integer K_0>=1, real M_0>0 and a finite set O of distinct positive orders coprime to15.
For the SAME P,H define L_cap=15d+delta_cap and, for each n in O, the FINITE set

    A_n={ k in Z : 0<=k<=min(K_0-1,floor(delta_cap/phi(n))),
           R_n Delta_n^k
              <=[M_0 binom(L_cap,k)]^(phi(n)) }.   (4)

If a nonzero integer D satisfies

    deg D<=delta_cap, #supp(DH)<=K_0,
    ||DH||_1<=M_0,

then every A_n is nonempty and, with kappa_n=min A_n,

    sum_(n in O) phi(n)kappa_n<=deg D<=delta_cap.   (5)

Consequently one empty A_n, or a weighted sum greater than delta_cap, excludes every such multiplier.
No monotonicity of the inequality in k is assumed; the full feasible set in (4) is essential.
An empty O gives only the vacuous bound0<=deg D.
For C605 use delta_cap=floor(Bd) and M_0=30375qS_0, retaining the ACTUAL fixed rational q and every numerator coefficient.
This supplies a finite necessary test, not a construction or a claim that a particular original input has already failed it.

**D. Explicit endpoint consequences.**
For n=1,2 let a_+=abs P(1) and a_-=abs P(-1), positive integers under B's hypothesis.
Then

    R_1=a_+^3(250a_+^2-243),
    R_2=a_-^3(250a_-^2-243),
    R_1>=7a_+^5, R_2>=7a_-^5.                    (6)

For every multiplier in C's budget, put

    B_max=max_(0<=j<=min(K_0-1,L_cap)) binom(L_cap,j).

The endpoint consequence is

    7 abs P(+/-1)^5<=M_0 B_max
                    <=M_0(L_cap+1)^(K_0-1).      (7)

Thus fixed K_0,M_0 and delta_cap=O(d) force polynomial growth at the two actual endpoint values, with exponent at most(K_0-1)/5.
For O containing1,2, the two separately forced multiplicities also add in (5).
Neither endpoint size is claimed to grow automatically on a hypothetical near-one full-residual family.

The C200 torsion calibration remains outside the original norm-positive domain.
Its bounded numerator is consistent with the jet obstruction: for its prime p inputs, any multiplier with deg(DH)<=16p and ||DH||_1<=M_0 must have order at least5 at z=1 once p>M_0*16^4/7.
The actual C200 multiplier has order8 at1.
No uniform D_G comparison, actual full-residual class or useful multiplier existence is supplied.

## Reuse and source scope

The motivating sufficient class and its exact scalar/degree costs are the adopted [C605](Yin_C_G0605_v1.md#statement).
Its content and exterior-root proofs are reused at their exact scope and are not reopened or revised.
The new question is whether concrete cyclotomic evaluations force factors and multiplicities in ANY low-cost multiplier, before the analytic C605 theorem can be applied.
This is stronger information about actual coefficients than merely restating C605's abstract escape on a hypothetical near-one sequence.

The sparse-root multiplicity fact used in (3) is already proved in [C250's bounded-order follow-up](Yin_C_G0250_v1.md#bounded-order-followup), by the exponent Vandermonde argument in characteristic zero.
That fact is a reused elementary input, not a new general sparse-polynomial theorem.
[Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) supplies the accepted monic integral irreducible Phi_n, its degree and full cyclotomic conjugates at the source's recorded statement/proof scope.
[Bel17-U002](../audits/literature/Bel17/Yin_U002.md#bel17-u002) supplies the existing discriminant convention and its actual source-inspection limits; the derivative-norm identity needed here is also written directly below.
Neither the explicit general cyclotomic discriminant formula nor a new original Washington or Neukirch proof is required.
[C200](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) supplies only its unchanged torsion input, multiplier factorization and zero-original-norm boundary.

Before proof development, the author read C605's selected isolated-review adoption, C200's full proof, C250's exact sparse multiplicity argument, and both named Bel17 units.
Targeted searches in G Claims and ledger records for H35 cyclotomic factors, coprime-order norm comparisons, cyclotomic jets and multiplier multiplicity costs found no matching combined argument.
The existing exact algebraic and norm inputs suffice; no external theorem or new computation was needed.
This bounded reuse finding makes no literature novelty claim.
The canonical trace representative in C199 remains a DIFFERENT object throughout.

## Complete argument

### 1. Same full cyclotomic norm at coprime powers

Let f=phi(n), F_n=Q(zeta), and R=abs Norm_(F_n/Q)P(zeta).
Since P(zeta) is a nonzero algebraic integer, R is a positive rational integer.
For any integer j coprime to n, the map zeta to zeta^j permutes all f primitive nth roots.
It is an automorphism of F_n, and therefore

    abs Norm_(F_n/Q)P(zeta^j)=R.

This equality uses the FULL degree f, even if P(zeta) generates a smaller field.
Nonvanishing at every such power follows from the same automorphism.

If gcd(n,15)=1 and H35(zeta)=0, then

    250P(zeta^3)^5=243P(zeta^5)^3.

Absolute norms give 250^f R^5=243^f R^3, hence

    R^2=(243/250)^f<1,

contradicting R>=1.
For H23 the same reasoning at coprime powers2,3 gives R=(8/9)^f<1, and for H25 at powers2,5 gives R^3=(64/75)^f<1.
This proves (1), without imposing any real-root or trace-field condition.
The integers1 and2 cause no exception: their cyclotomic fields have degree1 and the same coprime-power permutation argument applies.

For a monic irreducible nontorsion P, no root of unity is a root of P.
Thus the H35 assertion applies at every order coprime to15.
If3 or5 divides the order, the corresponding power can have smaller order and a different field norm.
The same-R equation above must not be used there.
The following actual example shows why retaining that distinction matters.

### 2. A genuine order-three factor outside the excluded range

Take P_* in (2), and its trace polynomial

    T_*(x)=x^2-1567x+3292,
    P_*(z)=z^2 T_*(z+z^(-1)).                      (8)

The discriminant of T_* is2442321, strictly between1562^2=2439844 and1563^2=2442969, so T_* is irreducible over Q.
Moreover T_*(2)=162>0 and T_*(3)=-1400<0, so one trace root lies in(2,3).
The other is1567 minus that root and hence lies in(1564,1565).
Both trace conjugates are real and greater than2.
For a trace root delta, the norm of delta^2-4 is

    T_*(2)T_*(-2)=162*6430=1041660.

This lies strictly between1020^2=1040400 and1021^2=1042441.
If delta^2-4 were a square in Q(delta), its rational norm would be a rational square, and an integer that is a rational square is an integer square.
The displayed nonsquare norm rules this out.
Thus z^2-delta z+1 is irreducible over the degree-two trace field, and P_* is irreducible of degree4 over Q.
Its roots are positive real reciprocal pairs, with expanding roots greater than1, so it is nontorsion and its actual trace field is totally real.
No numerical root approximation is used.

At a primitive cube root zeta, direct reduction by zeta^2+zeta+1=0 gives

    P_*(1)=162,
    P_*(zeta)=4860 zeta^2,
    P_*(zeta^2)=4860 zeta,
    4860=30*162.

Since250*162^2=243*30^3=6561000, it follows exactly that

    H35(zeta)=250*162^5-243*4860^3=0.

The monic minimal polynomial Phi_3 therefore divides this H35 in Z[z].
This is an original nontorsion input, not cyclotomic padding of P or an arbitrary auxiliary chosen independently of it.

For completeness it is not an actual full-residual input.
Use its actual divided trace quotients a=rem_(T_*)T_*(x^2-2)/2 and c=rem_(T_*)T_*(x^5-5x^3+5x)/5, evaluated at delta.
Both are integral in the trace order: modulo p=2 or5, the corresponding Chebyshev polynomial is x^p and T_*(x^p)=T_*(x)^p, so its monic remainder modulo T_* is coefficientwise divisible by p.
Modulo4, T_*(x)=x^2+x, so in the quotient by T_* one has x^2=-x and

    T_*(x^2-2)=2-2x modulo(4,T_*),
    a=1+x modulo(2,T_*).

The first congruence follows by substituting x^2-2=-x-2 into x^2+x and reducing once more.
Monic division makes these remainder computations valid modulo4, and the numerator is divisible by2 coefficientwise as for the actual divided quotient.
At the F_2 root x=0 of T_* mod2, the value of a is1.
If f=2c^2-3a^5 were zero in the actual trace field, reduction in the actual trace order modulo2 would force a^5=0, contradicted by that evaluation.
Thus the example does not satisfy f=0 and supplies no full-residual construction.
It proves only the stated boundary of the coprime-order exclusion.

### 3. First nonzero derivatives retain the whole cyclotomic norm

Now take P,H,D,N as in B and let n be coprime to15.
By A, H(zeta_n)!=0.
Set k=ord_(Phi_n)D and write

    D=Phi_n^k E, E in Z[z], Phi_n does not divide E.

The quotient is integral because Phi_n is monic.
Its value E(zeta_n) is a nonzero algebraic integer, so its full field norm has absolute value at least1.
All roots of Phi_n are simple.
Hence N has multiplicity EXACTLY k at every primitive nth root, and its first nonzero normalized derivative is

    N^(k)(zeta_n)/k!
        =H(zeta_n)Phi_n'(zeta_n)^k E(zeta_n).       (9)

For k=0 this is just the original evaluation identity, with no derivative factor.
For k>0 it follows by taking the coefficient of(z-zeta_n)^k in the local finite product.
Neither a lower-order derivative nor a sum over selected embeddings can replace it.

Put Delta_n=abs Norm Phi_n'(zeta_n).
The value Phi_n'(zeta_n) is nonzero and integral, so Delta_n is a positive integer.
Multiplying its finite products over all primitive roots gives the absolute product of every pair difference squared, which is the absolute discriminant of the monic Phi_n.
For Phi_1=z-1 and Phi_2=z+1 the derivative is1, giving Delta_1=Delta_2=1.
The proof needs no closed formula for Delta_n.

Taking absolute norms in (9), keeping all phi(n) embeddings, gives the EXACT identity

    abs Norm[N^(k)(zeta_n)/k!]
       =R_n Delta_n^k abs Norm E(zeta_n)
       >=R_n Delta_n^k.                           (10)

Write N=sum_(j=0)^L b_j z^j.
Then N^(k)(z)/k!=sum_(j>=k) b_j binom(j,k)z^(j-k), an integer polynomial.
For every abs(z)=1, since binom(j,k)<=binom(L,k),

    abs[N^(k)(z)/k!]
        <=sum_(j>=k) abs(b_j)binom(j,k)
        <=M binom(L,k).

Applying this at ALL primitive roots bounds the left side of (10) above by[M binom(L,k)]^phi(n).
This proves the second part of (3), with the correct field degree on the complete coefficient bound.
The first part of (3), k<=K-1, is exactly the already retained C250 sparse-root multiplicity theorem, applied to the nonzero characteristic-zero polynomial N and the nonzero root zeta_n.
Its distinct-exponent Vandermonde proof needs no assumption about the coefficient signs or their sizes.
Thus all of (3) holds for arbitrary integer multipliers, including ones with noncyclotomic factors or nonunit leading coefficients.

### 4. Finite feasible multiplicities and additive degree

Under the budgets in C, every actual L is at most L_cap and every actual coefficient mass M is at most M_0.
For fixed k<=L, binom(L,k)<=binom(L_cap,k).
Each actual k_n also obeys k_n phi(n)<=deg D<=delta_cap and k_n<=K_0-1 by (3).
Therefore its exact inequality places k_n in A_n as DEFINED in (4).
An empty set consequently rules out the proposed multiplier immediately.

If all the sets are nonempty, k_n>=kappa_n holds simply by minimality in a finite set.
It uses no interval, monotonicity or convexity assertion about the binomial/discriminant comparison.
Distinct Phi_n are coprime monic irreducibles over Q, so their entire product with these actual multiplicities divides D over Z.
Consequently

    deg D>=sum_(n in O)phi(n)k_n
          >=sum_(n in O)phi(n)kappa_n,

proving (5).
This counts every imposed factor only once and retains its actual multiplicity.
The finite set O is explicitly supplied; no all-order scan or claim that a chosen finite list is exhaustive is built into the test.
All inequalities can be evaluated exactly for rational M_0 through integer resultants and rational comparisons, but no such test has been executed here.

### 5. Endpoint information is a concrete coefficient obstruction

At z=+1 and z=-1 the odd powers3 and5 have the same value z.
Thus H(z)=P(z)^3(250P(z)^2-243), giving (6).
The no-cyclotomic-factor hypothesis ensures P(+/-1)!=0.
For any integer a>=1,

    250a^2-243>=7a^2,

because the difference is243(a^2-1)>=0.
Combining (3) with Delta_1=Delta_2=1 gives

    7a_+^5<=M binom(L,k_1),
    7a_-^5<=M binom(L,k_2).

Using the actual budgets and then the maximum in D proves the first inequality in (7).
For0<=j<=K_0-1, binom(L_cap,j)<=L_cap^j<=(L_cap+1)^(K_0-1), including j=0, which proves its second inequality.
Here L_cap>=15 because d>=1, so no zero-width convention is needed.
The explicit upper exponent follows directly when delta_cap=O(d) and the other two budgets are fixed.
This is a necessary restriction on the ACTUAL sums P(1) and P(-1), rather than a conclusion about an unspecified varying-test cost.
It does not assert that those sums are large in the residual domain.

### 6. Torsion calibration and unresolved coverage

C200's prime p>30 input P_p=Phi_p has P_p(1)=p and admits

    D0=(z^3-1)^5(z^5-1)^3,
    N_p=D0 H35,
    deg N_p=15p+15<=16p,
    ||N_p||_1<=126208.

The last bound follows directly from its two binomial-product summands: each has coefficient mass at most2^8 and their scalar coefficients total493.
This preserves C200's exact numerator and all its original zero-value restrictions.
Although P_p is torsion, the proof of (3) at n=1 still applies: P_p(1)!=0 and the coprime-order nonvanishing proof at that specified order holds.
If an integer multiplier on this input has degree of DH at most16p and coefficient mass at mostM_0, and k=ord_(z-1)D<=4, then (3) and (6) give

    7p^5<=M_0 binom(16p,k)<=M_0(16p)^4.

This is impossible for p>M_0*16^4/7, proving the claimed eventual lower bound k>=5.
The actual D0 has order5+3=8 at1, consistent with that necessary bound.
No optimality of5 or8 is claimed.
At order p the calibration instead has P_p(zeta_p)=0, so the nonzero norm premise of A fails and H35 can vanish there.
This is precisely why the torsion family cannot be treated as an original norm-positive residual example.

No current result supplies a useful full-residual multiplier class or an automatic lower bound on enough R_n to violate (5).
A concrete next use is to evaluate a justified finite order set on a separately supplied actual candidate, or to derive those resultant lower bounds from the SAME original residual equations.
The present result supplies the exact nonvanishing, multiplicity and degree accounting required for that step.
It changes neither canonical zero-Haar status nor the unrestricted G0001 objective.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:27 |
| status | open |
| reason | Register the complete coprime-order nonvanishing, actual order-three boundary control, exact norm-jet inequality, finite feasible-multiplicity degree obstruction, endpoint bound and torsion calibration. Separate whole review and adoption remain pending; no actual full-residual multiplier class, executed sieve, uniform discrepancy theorem or Task completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | All parts A--D, actual complete cyclotomic norms, order-three original control, every finite set and budget, nonmonotone feasible multiplicities, both endpoints and exact calibration boundaries. |
| argument | [Complete argument](#complete-argument) | All six complete proof sections, every original scalar, field degree, nonzero value, normalized derivative, factor multiplicity, coefficient and full multiplier degree. |
| dependency | [Existing sparse-root multiplicity](Yin_C_G0250_v1.md#bounded-order-followup) | Only its characteristic-zero distinct-exponent Vandermonde multiplicity bound k<=K-1 for an actual nonzero sparse polynomial at a nonzero root. |
| dependency | [Cyclotomic field facts](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Accepted monic integral irreducible Phi_n, degree phi(n), primitive-root conjugates and the actual field norm, at the retained source-proof scope. |
| support | [Discriminant convention](../audits/literature/Bel17/Yin_U002.md#bel17-u002) | Existing naming and absolute-discriminant convention only; the finite derivative-norm equality is proved locally, with no new source-proof inspection or use of the closed formula. |
| support | [Actual multiplier sufficient class](Yin_C_G0605_v1.md#statement) | Exact target budgets and scalar30375q, unreduced H35 scope and existing content/exterior-root boundaries; no new adoption or expansion of that analytic theorem. |
| support | [Torsion numerator calibration](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) | Existing prime-cyclotomic P_p and exact D0 H35=N_p with zero original norm; no new numerical run or nontorsion interpretation. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:42 |
| status | proved |
| reason | Adopt the complete coprime-order nonvanishing, actual order-three boundary control, exact norm-jet inequality, finite feasible multiplicity budgets, endpoint bounds and torsion calibration after the selected isolated whole review. No useful full-residual multiplier, executed sieve, automatic resultant growth or unrestricted Mahler conclusion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | All parts A--D, actual complete cyclotomic norms, order-three original control, every finite set and budget, nonmonotone feasible multiplicities, both endpoints and exact calibration boundaries. |
| argument | [Complete argument](#complete-argument) | All six complete proof sections, every original scalar, field degree, nonzero value, normalized derivative, factor multiplicity, coefficient and full multiplier degree. |
| dependency | [Existing sparse-root multiplicity](Yin_C_G0250_v1.md#bounded-order-followup) | Only its characteristic-zero distinct-exponent Vandermonde multiplicity bound k<=K-1 for an actual nonzero sparse polynomial at a nonzero root. |
| dependency | [Cyclotomic field facts](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Accepted monic integral irreducible Phi_n, degree phi(n), primitive-root conjugates and the actual field norm, at the retained source-proof scope. |
| support | [Discriminant convention](../audits/literature/Bel17/Yin_U002.md#bel17-u002) | Existing naming and absolute-discriminant convention only; the finite derivative-norm equality is proved locally, with no new source-proof inspection or use of the closed formula. |
| support | [Actual multiplier sufficient class](Yin_C_G0605_v1.md#statement) | Exact target budgets and scalar30375q, unreduced H35 scope and existing content/exterior-root boundaries; no new adoption or expansion of that analytic theorem. |
| support | [Torsion numerator calibration](Yin_C_G0200_v1.md#cyclotomic-h35-energy-log-calibration) | Existing prime-cyclotomic P_p and exact D0 H35=N_p with zero original norm; no new numerical run or nontorsion interpretation. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G0808_v1.md#cyclotomic-jet-whole-finding) | Entire unchanged statement and complete argument, every exact selected input, all limitations and actual source inspection boundaries. |

