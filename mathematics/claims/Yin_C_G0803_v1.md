---
author: Yin
---

# Exact reciprocal forced corridors, arbitrary fixed-step norm obstructions and critical harmonic oscillation

Contributor original_signed_asymptotic developed the construction and complete argument for human author Yin.
Root supplied the original-law critical-branch question and requested explicit whole-core, finite-step and actual-H quantifiers.
No independent review or adoption is asserted by this author candidate.
Every path below uses the complete original digit law; no new graph or return-time computation is used.

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior root beta, a neutral conjugate zeta, the actual order O=Z[beta], and the reciprocal involution iota(beta)=beta^(-1).
The original digit probabilities are p_0=1/2 and p_(-1)=p_1=1/4.
Put B=1/(beta-1), S=beta B, and use the entire actual accessible/coaccessible core

    D={x in O: |x_+|<B, |x_-|<S}.

Let P_D be the ORIGINAL killed kernel, R the true return radius, H(0)=1 the actual critical first-hit function, and

    0<H(x)<=1 on D,   H=R P_D H,
    Q(x,y)=R P_D(x,y)H(y)/H(x).

The established actual recurrence makes Q stochastic, and 1<R<2.
Neither finiteness of the critical return mean mu nor a stationary probability is assumed.
Let Q_0 be Q killed on first entry into zero.
For x=sum_(j=0)^3 a_j beta^j, put

    K(x)=-(a0 a1+a1 a2+a2 a3+a0 a2+a1 a3+a0 a3),
    rho(x)=|x(zeta)|,
    N(x)=x iota(x),     Jx=beta^(-1)iota(x).

The adopted exact identity is rho(x)^2=sqrt13 K(x)+x_+x_-; K is a nonnegative integer on D.
The symbol N denotes the relative norm as an algebraic element, not its absolute field norm.

Define the actual order elements and positive real constants

    c=(beta-1)^(-1)=beta^3-beta-2,
    d=beta-beta^(-1),
    v=beta+beta^(-1)-2,
    tau=(3+sqrt13)/2,   a=tau^(-1)=(sqrt13-3)/2.

For EVERY fixed integer m>=1 set

    y_(m,k)=v^k c d (beta^(-m)-1),
    x_(m,k,j)=c+beta^j y_(m,k),   0<=j<=m, k>=0.             (FC1)

There is an explicit sufficient lower range for k.
Put

    C_m=B(beta-beta^(-1))(1-beta^(-m))>0,
    D_m=S(beta-beta^(-1))(beta^m-1)>0.

Every integer k>=0 satisfying

    C_m a^k < beta^(-m-1),    D_m a^k < 2S                (FC2)

has ALL the following properties.
Such k include every sufficiently large integer.

All m+1 states in FC1 lie in D, are nonzero and pairwise distinct.
For every j<m, the ONLY legal next digit is -1, with next state x_(m,k,j+1).
Its original probability is 1/4 and its actual Q probability is 1.
The whole path therefore has original probability4^(-m) and Q probability1.

The path has the exact reciprocal symmetry

    x_(m,k,m-j)=-J x_(m,k,j),   0<=j<=m.                    (FC3)

Consequently its endpoints have exactly equal relative norm, level and neutral radius:

    N(x_(m,k,m))=N(x_(m,k,0)),
    K(x_(m,k,m))=K(x_(m,k,0)),
    rho(x_(m,k,m))=rho(x_(m,k,0)).                          (FC4)

For each fixed m, their radii and levels tend to infinity as k tends to infinity.
For EVERY pointwise finite real function f of the relative norm on N(D), with no monotonicity, positivity or regularity assumption, one has

    Q^m(f composed with N)(x_(m,k,0))
      =Q_0^m(f composed with N)(x_(m,k,0))
      =f(N(x_(m,k,0))).                                    (FC5)

In particular FC5 holds for every finite real function of K, of rho, or jointly of(K,rho).
Thus, for every prescribed m, none of these functions can have strictly negative m-step Q drift at EVERY state outside a finite set.
This excludes both a fixed positive additive deficit and a strictly negative pointwise deficit in that range.
It also excludes the corresponding killed m-step inequality with positive expected accumulated reward.
The horizon m is fixed before choosing the unbounded family; no obstruction to arbitrary state-dependent or unbounded stopping rules is asserted.

The actual harmonic values telescope exactly:

    H(x_(m,k,j))=(4/R)^j H(x_(m,k,0)),   0<=j<=m.            (FC6)

For every M>0 and L>0 there are two actual states x,z with K(x)=K(z)>M, rho(x)=rho(z)>M and N(x)=N(z), but H(z)/H(x)>L.
Hence no positive profile h depending only on N, K, rho or(K,rho) can have

    c_- h <= H <= c_+ h                                   (FC7)

at all sufficiently high levels or radii, with constants0<c_-<=c_+<infinity.
In particular no uniform relative error epsilon<1 is possible for such a profile.

For C563's ACTUAL critical canonical Fourier coefficients, A_R=H composed with J and B_R=H on D.
Writing x_j=x_(m,k,j), their exact values and unnormalized occupation coefficient are

    B_R(x_j)=(4/R)^j H(x_0),
    A_R(x_j)=(4/R)^(m-j) H(x_0),
    sigma_R(x_j)=A_R(x_j)B_R(x_j)
                =(4/R)^m H(x_0)^2
                =(R/4)^m H(x_m)^2 <= (R/4)^m.              (FC8)

Thus sigma_R is a positive constant on every one of these m+1 distinct states, although the two factors vary oppositely.
The ratios A_R/B_R attain(4/R)^m and(R/4)^m at the endpoints.
Outside every finite set, neither factor is bounded above by a fixed constant times the other.
Likewise sigma_R has no uniform positive lower or finite upper pointwise comparison with either A_R^2 or B_R^2.
This is a coefficientwise obstruction, not a prohibition on every possible comparison of their complete sums or convolution measures.

No finite/infinite critical-mean classification, positive linear bridge-level expectation, summability or nonsummability of sigma_R, fixed-state return-tail lower bound, or unrestricted G0001 conclusion is asserted.
In particular an arbitrarily long deterministic corridor does not supply its own entrance mass.
The bound in FC8 is an upper bound on its occupation height.

## Complete argument

### Reused inputs and the different conclusion

The precise unresolved input remains an actual infinite-tail or positive linear complete-bridge estimate for the original quartic.
The adopted [C400 strict-core theorem](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption), in its fixed-quartic application using C396's complete narrow co-return premise, identifies the displayed strict algebraic strip with the actual accessible/coaccessible D.
Its boundary-state computation already places c in the actual order, with real embeddings(B,-S).
The [C780 level identity](Yin_C_G0780_v1.md#decision-whole-reviewed-2026-10-26) supplies K>=0 and the exact relative-norm formula.
The [C599 actual harmonic interface](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) supplies positive H<=1, true R, stochastic Q and the full original digit weights without a mean assumption.
The [C790 balanced-unit computation](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) supplies the actual-order unit v and its two real and neutral embeddings.
The [C563 whole-order canonical interface](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) supplies B_R=H, A_R=H composed with J and sigma_R=A_R B_R.

The bounded reuse screen read C783's arbitrary level-only ONE-step obstruction and finite same-level ratio, C599's monotone radial ONE-step obstruction, C601's exact forced-boundary/central-clock mechanism, C593v2's central harmonic clock and H-sensitive row identities, and C563's reciprocal convolution distinction.
Targeted searches for fixed horizons, forced equal-level endpoints, reciprocal harmonic ratios and unbounded same-level/radius ratios found no adequate account of FC1--FC8.
This is a bounded reuse statement, not a literature-priority claim.
Those existing inputs suffice for the elementary algebra and finite-row argument below; no new external theorem is invoked.

C783's all-three-successor flat rows retain a separate scope: the present paths have only one legal successor and compare arbitrary fixed horizons.
C601/C593v2's variable-length central reduction likewise remains outside the present fixed-horizon obstruction.
The newer strict R<beta and large lower bound for mu are not needed for this construction and do not alter its scope.

### Actual-order arithmetic and all embeddings

The constant term of P is1, so beta^(-1) belongs to O; explicitly beta^(-1)=-beta^3+beta^2+beta+1.
Reduction by P gives

    (beta-1)(beta^3-beta-2)=1,

which proves c in O with its displayed inverse.
Reciprocity gives iota(c)=-beta c, and hence c_+=B and c_-=-S.
The map J=beta^(-1)iota preserves O, satisfies J^2=identity and maps D to D: its real coordinates are(beta^(-1)x_-,beta x_+).
Both sign reversal and J preserve nonzeroness.

Let u=beta+beta^(-1).
Then u^2-u-3=0, and its values are u_+=(1+sqrt13)/2 at BOTH real embeddings and u_-=(1-sqrt13)/2 at the neutral pair.
Thus

    v=u-2,   v^2+3v-1=0,   v^(-1)=v+3 in O,
    v_+=v_-=a in(0,1),    v(zeta)=-tau,    tau>1.            (FC9)

The involution fixes v and negates d.
Every factor in FC1 therefore belongs to the ACTUAL order; no larger-order or merely projected-lattice construction is used.
At the two real embeddings the increment is exactly

    y_(m,k),+ = -C_m a^k,
    y_(m,k),- = D_m a^k.                                  (FC10)

Both signs point into the strict rectangle from the excluded corner c.

At the neutral embedding, c(zeta) and d(zeta)=zeta-zeta^(-1) are nonzero.
Also zeta^m is never1 for m>=1.
Indeed zeta is conjugate to beta under the irreducible minimal polynomial P; if zeta were a root of unity, its minimal polynomial would divide a polynomial t^n-1, forcing beta^n=1 as well, contrary to beta>1.
For each fixed m, the neutral constant

    E_m=|c(zeta)(zeta-zeta^(-1))(zeta^(-m)-1)|

is therefore strictly positive, and

    |y_(m,k)(zeta)|=E_m tau^k -> infinity.                   (FC11)

No Diophantine rate in m or uniform lower bound for E_m is asserted or needed.

### Explicit true-core legality and forced probabilities

Fix m and k satisfying FC2, and put delta=C_m a^k and epsilon=D_m a^k.
For0<=j<=m, FC10 gives

    x_j,+ = B-beta^j delta,
    x_j,- = -S+beta^(-j)epsilon.

Because delta<beta^(-m-1) and B-B/beta=1/beta, one has

    B/beta < x_j,+ < B,     -S < x_j,- < S.                 (FC12)

For the second inequality,0<beta^(-j)epsilon<=epsilon<2S.
Thus every x_j is in the strict strip and therefore in the ORIGINAL core by the selected C400 application.
Its positive expanding coordinate also makes it nonzero.
The x_j are pairwise distinct since delta>0 and beta>1.

For j<m, the algebraic identity beta c-1=c proves beta x_j-1=x_(j+1), which is legal.
The zero successor has expanding coordinate beta x_j,+>B, and the +1 successor has still larger expanding coordinate.
Those two successors are not in D.
Thus -1 is the unique original legal digit at every required intermediate state, with original probability1/4.
The actual harmonic row equation gives

    H(x_j)=(R/4)H(x_(j+1)),
    Q(x_j,x_(j+1))=1.

Iteration proves FC6 and the exact original and Q path probabilities.
No replacement of H, independence assumption, asymptotic ratio or stationary law enters this calculation.
Since all states are nonzero, killing on entry into zero does not remove any part of this m-step path.

The sufficient conditions FC2 are met for every sufficiently large k because0<a<1 and m is fixed.
They specify the entire required finite path, rather than only its starting or ending real coordinates.

### Reciprocal symmetry and exact norm conservation at the endpoints

Write y=y_(m,k).
The identities iota(c)=-beta c, iota(d)=-d and iota(v)=v imply

    iota(y)=beta v^k c d (beta^m-1),
    -J y=-v^k c d(beta^m-1)=beta^m y,
    Jc=-c.

Therefore, for every0<=j<=m,

    -J(c+beta^j y)=c-beta^(-j)Jy
                  =c+beta^(m-j)y=x_(m-j),

which proves FC3.
This identity also displays the original reciprocal orientation exactly; J is not replaced by ordinary sign symmetry.

The relative norm satisfies N(-Jx)=N(x), because N(-beta^(-1))=1 and iota exchanges the two factors.
Its expanding real value is x_+x_-, and its neutral real value is x(zeta)conjugate(x(zeta))=rho(x)^2.
The endpoint equality in FC3 therefore proves equality of both these quantities.
The exact C780 identity rho^2=sqrt13 K+x_+x_- then proves K equality and all of FC4.
Equivalently, the cross-term norm change vanishes because(beta^m-1)y/c is anti-invariant under iota; no approximation of either norm component is involved.

For fixed m, FC11 and the triangle inequality give

    rho(x_j)>=E_m tau^k-|c(zeta)| -> infinity

for each j, since |zeta^j|=1.
The bounded core product |x_j,+ x_j,-|<BS and the exact level identity then give K(x_j)->infinity.
Thus all the families used here leave every finite core subset.

### Fixed horizons and unbounded harmonic oscillation

At x_0 the actual m-step distribution is the point mass at x_m.
The same holds for the killed kernel because no zero is visited.
This proves FC5 for every finite real f.
For functions of K, rho or their pair, FC4 gives the same equality directly.
If a proposed strict negative m-step drift held outside a finite set, choose k large enough that x_0 lies outside it; FC5 contradicts the proposed strict inequality there.
Any accumulated reward strictly positive along the deterministic segment similarly contradicts equality.
For example the usual m-unit reward has value exactly m on this path.

To prove the harmonic-ratio assertion, first choose the integer m so large that(4/R)^m>L; this is possible since R<2.
Then choose k satisfying FC2 and so large that the endpoint levels and radii exceed M.
FC4 and FC6 give precisely the same-invariant pair and required ratio.
This order of quantifiers is essential: no single finite level is said to contain arbitrarily long corridors.

If FC7 held on all sufficiently high levels or radii, the common invariant would force H(x_m)/H(x_0)<=c_+/c_-.
Choosing m with(4/R)^m>c_+/c_- and then k large contradicts that inequality.
Taking c_-=1-epsilon and c_+=1+epsilon gives the relative-error exclusion for every fixed epsilon<1.
The argument also applies to any other descriptor constant on these reciprocal endpoint pairs.

### Actual dual factors, occupation plateaus and the unpaid-tail boundary

Sign reversal bijects all original first-hit words and preserves every digit probability, length and critical weight.
Thus H(-x)=H(x) for every actual state, with no finite-mean assumption.
C563's actual identifications B_R=H and A_R(x)=H(Jx), together with FC3, give

    A_R(x_j)=H(x_(m-j)).

Substituting FC6 proves every equality in FC8.
The upper bound follows from H(x_m)<=1.
In particular the TOTAL unnormalized occupation over these m+1 distinct states is exactly

    sum_(j=0)^m sigma_R(x_j)
       =(m+1)(R/4)^m H(x_m)^2
       <=(m+1)(R/4)^m.                                    (FC13)

This identity uses actual complete-excursion occupation coefficients, not a newly chosen probability on the corridor.

At x_0, A_R/B_R=(4/R)^m, while at x_m it equals(R/4)^m.
Also sigma_R/B_R^2=A_R/B_R and sigma_R/A_R^2=B_R/A_R.
Letting m grow and then choosing k outside any prescribed finite set proves all stated failures of uniform pointwise comparison.
No inference from a pointwise comparison failure to divergence of a complete sum is made.

The complete sum sum_D sigma_R is the extended critical mean mu by C563.
FC13 alone supplies no lower bound for the occupation of any selected corridor, no disjointness among corridors for different(m,k), and no lower probability of reaching them from zero.
Consequently neither the long deterministic times nor the large harmonic ratios prove mu infinite.
They also give no bound on C785's complete positive-level phase derivative g'(R), and no positive linear complete-bridge level expectation.
A successful argument must still control actual entrance/continuation mass, or use a genuinely state-dependent statistic or stopping rule not excluded by FC5.
This preserves both critical branches and the actual canonical-convolution boundary.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-26)

## Assessment history

### Decision forced-corridor-open

| Field | Value |
| --- | --- |
| date | 2026-10-26T15:01 |
| status | open |
| reason | Fix the complete FC1--FC13 author argument: explicit actual-order forced corridors for every fixed horizon, all-step strict-core legality and original weights, exact reciprocal/norm endpoint identity, unbounded level/radius growth, arbitrary invariant-profile fixed-step obstruction, exact true-H oscillation and actual canonical-factor/occupation plateaus with every entrance-mass and critical-mean limitation. Whole independent review remains outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire forced-corridor statement](#statement) | Complete fixed-quartic FC1--FC8 and all finite/infinite quantifiers, actual law/core/H/Q, every profile/dual comparison obstruction and all stated exclusions. |
| argument | [Complete argument](#complete-argument) | Entire FC1--FC13 proof, actual-order and embedding algebra, explicit sufficient k conditions, all-step legality, deterministic original/Q path, reciprocal norm equality, fixed-m and increasing-m order, exact actual factors/occupation and unpaid-tail boundary. |
| dependency | [Exact actual core and excluded boundary state](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals the original accessible/coaccessible O-core using C396's complete narrow co-return premise; actual c boundary element, without an arbitrary Salem extension or timing extrapolation. |
| dependency | [Exact level and relative norm identity](Yin_C_G0780_v1.md#decision-whole-reviewed-2026-10-26) | Actual quartic K>=0, rho^2=sqrt13 K+x_+x_- and full core coordinate convention; no linear bridge moment imported. |
| dependency | [Actual critical harmonic and kernel interface](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) | True R<2, positive actual H<=1, H=R P_D H and stochastic critical Q with original p_e in either mean branch; no stationary assumption or successful drift witness borrowed. |
| support | [Existing balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | Only actual-order v unit and exact contracting real/expanding neutral embeddings; specialized formulas are checked explicitly here, with no counting/probability inference. |
| dependency | [Actual canonical reciprocal factors and occupation](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) | Whole-order B_R=H, A_R=H composed with J, nonnegative sigma_R=A_R B_R and extended total mu; no bounded critical convolution or finite mean is assumed. |

### Decision whole-reviewed-2026-10-26

| Field | Value |
| --- | --- |
| date | 2026-10-26T15:34 |
| status | proved |
| reason | Root read the complete fixed FC1--FC13 and entire independent whole R1023 and adopts the actual forced-corridor construction and its exact invariant-profile, harmonic-ratio and canonical-coefficient consequences without substantive repair. Every original-order embedding, all-step strict-core test, fixed-horizon/increasing-horizon quantifier and original/Q probability is retained. Constant occupation along a long corridor has the proved exponentially small upper height; no entrance-mass lower bound, critical-mean branch or linear bridge-growth conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire forced-corridor statement](#statement) | Complete fixed-quartic FC1--FC8 and all finite/infinite quantifiers, actual law/core/H/Q, every profile/dual comparison obstruction and all stated exclusions. |
| argument | [Complete argument](#complete-argument) | Entire FC1--FC13 proof, actual-order and embedding algebra, explicit sufficient k conditions, all-step legality, deterministic original/Q path, reciprocal norm equality, fixed-m and increasing-m order, exact actual factors/occupation and unpaid-tail boundary. |
| dependency | [Exact actual core and excluded boundary state](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed-quartic strict strip equals the original accessible/coaccessible O-core using C396's complete narrow co-return premise; actual c boundary element, without an arbitrary Salem extension or timing extrapolation. |
| dependency | [Exact level and relative norm identity](Yin_C_G0780_v1.md#decision-whole-reviewed-2026-10-26) | Actual quartic K>=0, rho^2=sqrt13 K+x_+x_- and full core coordinate convention; no linear bridge moment imported. |
| dependency | [Actual critical harmonic and kernel interface](Yin_C_G0599_v1.md#decision-complete-isolated-whole-adoption) | True R<2, positive actual H<=1, H=R P_D H and stochastic critical Q with original p_e in either mean branch; no stationary assumption or successful drift witness borrowed. |
| support | [Existing balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | Only actual-order v unit and exact contracting real/expanding neutral embeddings; specialized formulas are checked explicitly here, with no counting/probability inference. |
| dependency | [Actual canonical reciprocal factors and occupation](Yin_C_G0563_v1.md#decision-complete-isolated-whole-adoption) | Whole-order B_R=H, A_R=H composed with J, nonnegative sigma_R=A_R B_R and extended total mu; no bounded critical convolution or finite mean is assumed. |
| review | [Independent whole forced-corridor finding](../audits/reviews/Yin_R_G1023_v1.md#whole-forced-corridor-finding) | Entire Statement and FC1--FC13 with all actual fixed interfaces, explicit finite-path legality, reciprocal endpoint invariants, all drift/profile quantifiers, true canonical factor/occupation identities and exact unpaid-mass limitations. |

