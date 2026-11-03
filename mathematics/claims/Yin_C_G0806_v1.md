---
author: Yin
---

# Actual critical shift corridors, full-circle essential spectrum and the uniform mixing obstruction

Human author Yin.
Root developed the weighted operator consequences of the adopted C803 forced corridors and C805 actual critical Hilbert-space construction.
This candidate has no independent review or adoption asserted.

## Statement

Use the fixed quartic P(t)=t^4-t^3-t^2-t+1, its Salem root beta, the actual order O=Z[beta] and the complete original core D with strict real bounds B=1/(beta-1) and S=beta B.
Retain the original probabilities p_0=1/2 and p_1=p_(-1)=1/4, true critical radius R, actual first-hit H and stochastic kernel Q(x,y)=R P_D(x,y)H(y)/H(x).
Put Jx=beta^(-1)iota(x), sigma(x)=H(x)H(Jx), and mu=sum_D sigma, allowing infinity.
All spaces below are complex Hilbert spaces using these ACTUAL weights.
Set

    H_sigma=l2(D,sigma),
    H_sigma,0=l2(D minus {0},sigma),
    Q_0 f(x)=sum_(y != 0) Q(x,y)f(y), x != 0.               (SC1)

Here Q_0 is killed on entry into zero, not a renormalized kernel.
Essential norm means distance to the compact operators on the specified Hilbert space.
Essential spectrum means the spectrum of the coset in the bounded-operator algebra modulo its compact ideal.

For EVERY integer m>=1 and every finite F subset D there is a nonzero distinct-state corridor x_0,...,x_m outside F with a common positive ACTUAL weight s=sigma(x_j) and

    Q(x_(j-1),x_j)=1,
    Q(x,x_j)=0 for all x != x_(j-1),     1<=j<=m.           (SC2)

Consequently, writing e_j=1_{x_j}/sqrt(s), one has the exact GLOBAL shift identities

    Q e_j=e_(j-1),     Q_0 e_j=e_(j-1),     1<=j<=m,        (SC3)

on their respective full spaces.
The weights satisfy 0<s<=(R/4)^m, but no positive lower bound is claimed.

Both Q and Q_0 are contractions and, for every m>=1,

    ||Q^m||=||Q^m||_ess=1,
    ||Q_0^m||=||Q_0^m||_ess=1.                            (SC4)

For every complex lambda with |lambda|=1, both operators admit weakly null unit vectors f_n with

    ||(Q-lambda I)f_n|| -> 0,
    ||(Q_0-lambda I)f_n|| -> 0.                            (SC5)

The same explicit vectors work for the two spaces by extending by zero at zero.
In particular the ENTIRE unit circle is contained in each operator's essential spectrum, and both ordinary and essential spectral radii are exactly1.
No assertion about an eigenvector at any such lambda is made.

If mu is finite, define the actual invariant probability pi=sigma/mu and the projection

    Pi f=(sum_D pi(x)f(x))1.

The invariant closed subspace H_perp={f in l2(D,pi):sum pi f=0} is infinite dimensional.
For Q_perp=Q restricted to this space, for every m>=1,

    ||Q_perp^m||=||Q_perp^m||_ess=1,
    ||Q^m-Pi||=||Q^m-Pi||_ess=1.                          (SC6)

For every |lambda|=1, Q_perp also has weakly null unit approximate eigenvectors at lambda.
Thus its essential spectrum contains the entire unit circle and its ordinary and essential spectral radii equal1.
There are no constants C<infinity and theta<1 for which ||Q^m-Pi||<=C theta^m for every m>=1.
Indeed the operator norm in SC6 does not tend to zero at all.
These statements concern the uniform l2 operator norm; they do not exclude convergence for any specified fixed initial vector or distribution.

The theorem is unconditional about SC1--SC5 and conditional only on finite mu for SC6 and the centered-space assertions.
It does not decide whether mu is finite, prove a fixed-start return-tail lower bound or positive linear complete-bridge level growth, or resolve the unrestricted Mahler gap.
The new all-power and whole-circle conclusion uses C803's arbitrarily long ACTUAL constant-weight corridors; it is not inferred from C805's one-step singular modes alone.

## Complete argument

### Exact reused inputs, source depth and distinct scope

The [adopted C803 statement and FC1--FC13 proof](Yin_C_G0803_v1.md#decision-whole-reviewed-2026-10-26) give explicit corridors for each prescribed m and every sufficiently large k.
All their states are nonzero, distinct and in the entire original core; every required Q step is deterministic, and their actual sigma weights have the same positive value at all m+1 states.
For fixed m, the neutral radii of ALL those states tend to infinity with k.
The full input and its complete proof were read, including the lack of a lower entrance mass and the exponential upper weight in FC8/FC13.

The [adopted C805 statement and RB1--RB12 proof](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) construct Q as a contraction on the entire l2(D,sigma), without assuming finite mu.
They give Q=mathsf J L, J-invariant sigma, and the positive finite L blocks with exact invariant weights.
No raw counting-measure operator estimate is transferred to this weighted space.
The full fixed proof and whole independent R1210 were read before use.

The [accepted Pet20 source interface](../audits/literature/Pet20/Yin_U001.md#pet20-u001) supplies the standard compact weak-to-norm property and the closed two-sided compact ideal with its Banach quotient norm.
Its source statements and applicability are accepted at the retained statement-reading depth, not a newly audited source proof.
The spaces used here are infinite-dimensional complex Hilbert spaces; their compact ideal is proper because an infinite orthonormal family has no norm-convergent subsequence.
No further Fredholm theorem is needed: essential spectral inclusion is proved directly from noninvertibility in this quotient.

The focused reuse screen inspected C805's explicit one-step boundary, C803's fixed-horizon state-profile and occupation conclusions, C408's raw counting-space all-power translation theorem and C703's exact cost and stationary-mass distinction.
Searches for weighted essential norms, Q powers and spectral gaps also identified C547/C566/C650/C675, whose word-fiber, overlap-mixture or bridge-count clocks differ from the present chronological actual Q.
None of those selected accounts supplies SC2--SC6 on the actual sigma-weighted space.
This is a bounded reuse statement, not a priority claim.
The finite columns, shift vectors and centering below are direct deductions from the adopted inputs.

### Exact invariant column masses, including infinite total mass

For any y, C805's finite block detailed balance gives sum_x sigma(x)L(x,y)=sigma(y).
The change of variables z=Jx and sigma(Jx)=sigma(x) therefore gives

    sum_x sigma(x)Q(x,y)=sigma(y).                         (SC7)

Every summand is nonnegative and the right side is a finite positive number.
This equality is valid even when sum_D sigma is infinite.
It uses the actual L block containing y, not an assumed normalized stationary law.

Q_0 is the compression of the bounded contraction Q to the closed subspace of H_sigma consisting of functions vanishing at zero: extend by zero, apply Q, and restrict away from zero.
The extension and restriction have norm1, so Q_0 is a contraction on H_sigma,0.
Its powers are the killed-chain powers because each intermediate sum excludes zero.

### A deterministic row with equal actual masses has a unique incoming column

Take a C803 corridor x_0,...,x_m and set s=sigma(x_j)>0.
For 1<=j<=m, the single term x=x_(j-1) in SC7 at y=x_j already equals s, because Q(x_(j-1),x_j)=1.
All other terms are nonnegative, their sum must be zero, and every sigma(x)>0.
It follows that Q(x,x_j)=0 for EVERY x other than x_(j-1).
This proves the second assertion in SC2 and the exact shift SC3 on the entire space, not merely along the corridor.
As no corridor state equals zero, removing the zero row and column changes none of these equalities.

For fixed m, C803's uniform lower bound on all corridor radii tends to infinity as k increases.
Thus choose k large enough to avoid any specified finite F.
Repeatedly include every previously selected corridor in F to obtain infinitely many pairwise disjoint corridors of this fixed length.
The same finite-avoidance construction works successively for lengths m tending to infinity: at each step m is fixed before its sufficiently large k is selected.
No common lower bound on s or quantitative rate in the chosen k is required.

### Every power has full essential norm

Fix m>=1 and choose the disjoint length-m corridors just constructed.
For their endpoint unit vectors e_m^(r), SC3 gives

    Q^m e_m^(r)=e_0^(r),
    Q_0^m e_m^(r)=e_0^(r).                                (SC8)

The inputs form an orthonormal sequence in either space and are weakly null.
Their images have norm exactly1.
For any compact operator K on the corresponding space, the accepted compactness interface gives ||K e_m^(r)||->0.
Consequently ||Q^m-K||>=1 and ||Q_0^m-K||>=1.
The contraction upper bounds prove all equalities in SC4.
This uses actual normalized weights s, so shrinking occupation mass causes no missing factor.
It supplies no probability lower bound from any fixed starting state.

### Explicit whole-circle approximate eigenvectors

Choose pairwise disjoint corridors of lengths n tending to infinity.
Write e_(n,j)=1_{x_(n,j)}/sqrt(s_n),0<=j<=n.
For a FIXED lambda with |lambda|=1 put

    f_n=(1/sqrt(n))sum_(j=1)^n lambda^j e_(n,j).            (SC9)

Its norm is1 and these vectors have disjoint supports, so they are orthonormal and weakly null.
By the exact global shift,

    (Q-lambda I)f_n
       =(lambda e_(n,0)-lambda^(n+1)e_(n,n))/sqrt(n),
    ||(Q-lambda I)f_n||=sqrt(2/n).                         (SC10)

The identical calculation holds for Q_0.
The two boundary vectors are distinct and orthonormal; no value of Q e_(n,0) or Q e_(n,n+1) is needed.

Let T be either operator and suppose its coset T-lambda I were invertible modulo compact operators.
A representative B of the inverse would satisfy B(T-lambda I)=I+K with K compact.
Applied to f_n, the left side tends to zero by SC10, while Kf_n tends to zero and ||f_n||=1.
This is impossible, proving essential spectral inclusion for every lambda on the unit circle.

Both operator norms and quotient norms are at most1.
For |z|>1 the norm-convergent geometric inverse sum_(j>=0) z^(-j-1)T^j inverts zI-T; the same argument works in the quotient.
Thus both spectra are contained in the closed unit disk, while their unit-circle inclusion gives ordinary and essential radii exactly1.
This proves the radius assertions without deriving spectral inclusion from a single one-step norm equality.

### The hypothetical finite-mean branch and centered vectors

Now assume mu<infinity.
Equation SC7 implies pi Q=pi.
For f in l2(D,pi), its absolute first moment is finite by Cauchy--Schwarz and sum pi=1.
Nonnegative stationarity applied to |f| justifies interchanging the absolutely convergent expectation sums, so sum pi Qf=sum pi f.
Together with Q1=1 this proves that H_perp is invariant, Pi Q=Q Pi=Pi, and the orthogonal decomposition into constants and H_perp reduces Q.
The weighted spaces with sigma and pi differ by the scalar norm factor sqrt(mu); the isometry from H_sigma to l2(D,pi) is f -> sqrt(mu)f.
This preserves all operator and compactness questions.

For a fixed length m and disjoint corridors indexed by r, let u_r=sqrt(mu)e_m^(r) and v_r=sqrt(mu)e_0^(r) be unit vectors in l2(D,pi).
They are separately orthonormal, Q^m u_r=v_r, and their common expectation is

    a_r=sqrt(s_r/mu).

Because sum_r s_r<=mu, one has a_r->0.
Also a_r<1 because the positive invariant mass includes other states.
The vectors

    g_r=(u_r-a_r 1)/sqrt(1-a_r^2)

belong to H_perp, have norm1 and are weakly null.
Their images are (v_r-a_r 1)/sqrt(1-a_r^2), also of norm1.
The same compactness argument as for SC8 proves ||Q_perp^m||_ess=||Q_perp^m||=1.
On constants Q^m-Pi vanishes and on H_perp it equals Q_perp^m.
This orthogonal decomposition proves its norm1.
The compact lower bound follows from the same g_r considered in the full space; its contraction upper bound is already established.
This proves SC6 for every fixed m.

For the whole-circle assertion take h_n=sqrt(mu)f_n from SC9, now unit and weakly null in l2(D,pi).
Set b_n=sum pi h_n and g_n=(h_n-b_n1)/sqrt(1-|b_n|^2) for all sufficiently large n.
Weak nullness gives b_n->0, so g_n are well-defined unit vectors in H_perp and remain weakly null.
The exact residual satisfies

    (Q-lambda I)(h_n-b_n1)
       =(Q-lambda I)h_n-(1-lambda)b_n1,

whose norm is at most sqrt(2/n)+2|b_n| and tends to zero.
The quotient-inverse contradiction above applies inside H_perp and gives the full unit circle in the essential spectrum of Q_perp.
Its contraction bound then gives both spectral radii1.
Finally SC6 directly excludes every stated uniform decaying operator-norm bound.

### Mathematical limits

The proof normalizes rare corridor states in l2 using their actual weights; such normalization is legitimate even when their unnormalized total mass tends to zero.
C803's upper bound (m+1)(R/4)^m on a corridor's occupation is consistent with both finite and infinite total mu.
The constructed vectors depend on the desired length or error and escape every prescribed finite set.
Therefore these are uniform operator-norm and spectral obstructions, not lower bounds for a fixed starting distribution, fixed-vector convergence, or the return tail from zero.
No finite/infinite-mean conclusion, entrance-mass estimate, derivative bound for the full positive phase, or unrestricted Lehmer conclusion is supplied.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision critical-shift-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T16:21 |
| status | open |
| reason | Fix the complete actual weighted corridor-shift, all-power essential-norm and whole-unit-circle argument, including the conditional finite-mean centered-space conclusion and every fixed-start/mean limitation. Author self-check is complete; whole independent review is outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire critical-shift statement](#statement) | SC1--SC6 on the true original weighted spaces, all horizons and all unit-circle lambda, killed powers and finite-mean centered branch, with every excluded conclusion. |
| argument | [Complete argument](#complete-argument) | SC1--SC10 and complete infinite-mass invariant-column, global shift, disjoint-corridor, compact quotient, explicit approximate-eigenvector and conditional centering arguments. |
| dependency | [Actual constant-weight forced corridors](Yin_C_G0803_v1.md#decision-whole-reviewed-2026-10-26) | Full original-law FC1--FC13 at this quartic: arbitrary prescribed length, all-state nonzero core legality, exact deterministic Q rows, common positive sigma, all-state escape for fixed length and its upper mass bound. |
| dependency | [Actual weighted contraction and invariant blocks](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Full actual H/sigma conventions, positive finite weights with extended total mu, invariant finite L blocks, J-invariant sigma and bounded Q contraction on all l2(D,sigma), without a finite-mean hypothesis. |
| support | [Accepted compact and quotient interface](../audits/literature/Pet20/Yin_U001.md#pet20-u001) | Standard compact weak-to-norm property and closed two-sided compact ideal with quotient norm on infinite-dimensional complex Hilbert spaces, at the retained source-statement/applicability depth; no new source-proof audit or Fredholm theorem invocation. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T16:32 |
| status | proved |
| reason | Adopt the unchanged complete SC1--SC10 theorem after main readback of the fixed statement/proof and the entire independent R1026. Actual constant-weight forced corridors and infinite-mass invariant columns establish global shifts, every power's norm and essential norm1, and the full unit circle in essential spectrum on the true weighted spaces, including killing at zero. The centered-space and uniform mixing conclusions retain their finite-mu hypothesis. All accepted source-depth, fixed-start, entrance-mass and unresolved mean/Lehmer boundaries remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire critical-shift statement](#statement) | SC1--SC6 on the true original weighted spaces, all horizons and all unit-circle lambda, killed powers and finite-mean centered branch, with every excluded conclusion. |
| argument | [Complete argument](#complete-argument) | SC1--SC10 and complete infinite-mass invariant-column, global shift, disjoint-corridor, compact quotient, explicit approximate-eigenvector and conditional centering arguments. |
| dependency | [Actual constant-weight forced corridors](Yin_C_G0803_v1.md#decision-whole-reviewed-2026-10-26) | Full original-law FC1--FC13 at this quartic: arbitrary prescribed length, all-state nonzero core legality, exact deterministic Q rows, common positive sigma, all-state escape for fixed length and its upper mass bound. |
| dependency | [Actual weighted contraction and invariant blocks](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Full actual H/sigma conventions, positive finite weights with extended total mu, invariant finite L blocks, J-invariant sigma and bounded Q contraction on all l2(D,sigma), without a finite-mean hypothesis. |
| support | [Accepted compact and quotient interface](../audits/literature/Pet20/Yin_U001.md#pet20-u001) | Standard compact weak-to-norm property and closed two-sided compact ideal with quotient norm on infinite-dimensional complex Hilbert spaces, at the retained source-statement/applicability depth; no new source-proof audit or Fredholm theorem invocation. |
| review | [Whole independent critical-shift finding](../audits/reviews/Yin_R_G1026_v1.md#whole-critical-shift-finding) | Entire exact statement and proof, C803/C805 fixed interfaces and Pet20 compact/quotient applicability, all domain and quantifier checks including killed powers and finite-mass centering; no native rerun or formal verification. |

