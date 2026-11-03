---
author: Yin
---

# Complete primitive Fourier criteria, exact moments and a pointwise obstruction

This retains the complete original2026-10-07 [L84 proof](../ledger/Yin_L_G0084_v1.md).
The average escape and common high-moment estimates remain explicit unproved hypotheses.
No source or native calculation is newly executed.

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible P of degree d, O=Z[alpha], A multiplication by alpha and v=1, m=log M(P)>0.
For rational prime q put J_q=(Phi_q(alpha)O:q^infinity), M_q=O/J_q and R_q=|M_q|=Prim_q, the full prime-to-q quotient.
Use the complete primitive-norm witnesses eta<=m, q<=B, q>=2+4d log(2B)/eta and log R_q>=qm/2.
For a fixed input eta=m supplies unbounded witnesses and n=floor(q/4) tending to infinity.
Every1<=n<=floor(q/4) preserves all original binary word fibers and R_q^(-1)<=exp(-2mn).

For independent fair binary digits on the complete quotient, write chi(A^j1)=exp(2pi i theta_j), nu_n the law and W_n(chi)=product_(j<n)cos²(pi theta_j).
Then

    Col(nu_n)=R_q^(-1)sum_chi W_n(chi)=R_q^(-1)+F_n,
    F_n=R_q^(-1)sum_(chi!=1)W_n(chi).

Every nontrivial dual orbit has exact period q, but a shorter window product need not be orbit-constant.
Let E_n(chi)=sum_(j<n)||theta_j||².
For fixed gamma>0, if all but at most R_q exp(-gamma n) nontrivial characters have E_n>=gamma n/4 along unbounded witnesses, then

    F_n<=2exp(-gamma n),
    Col(nu_n)<=exp(-2mn)+2exp(-gamma n),
    H2(nu_n)>=n min(2m,gamma)-log3.

A direct F_n<=Cexp(-gamma n) with fixed-input C independent of n has the same limiting consequence.
The original order-two Renyi entropy is subadditive, its rate h2 exists and h2<=h_support<=m.
Faithful transfer along the unbounded witnesses therefore implies m>=h2>=min(2m,gamma), forcing m>=gamma.
This is conditional: no required averaged estimate or common gamma is established.

For any nonzero cyclic prime-period module of order R coprime to odd q, put Z_n(chi)=sum_(j<n)chi(A^j1) and S_n(chi)=n/2-(1/2)Re Z_n,1<=n<=q.
Uniform averaging over all R characters gives mean S_n=n/2, Var(S_n)=n/4 in characteristic2 and n/8 otherwise.
Chebyshev gives Col(nu_n)<=4/n+exp(-n/4), or2/n+exp(-n/4) outside characteristic2, including the trivial character.
This particular argument certifies only logarithmic entropy.

For every positive n,r let A_(n,r) count all ordered equal r-term power sums in O.
It is exactly the Haar integral of |sum_(j<n)exp(2pi i<y,A^j1>)|^(2r) on T^d.
Norm integrality gives the exact finite-character moment identity

    R_q^(-1)sum_chi |Z_n(chi)|^(2r)=A_(n,r)
    for1<=n<=floor(q/4),1<=r<=B.

If a common C>=1 additionally gives A_(n,r)<=(Crn)^r for r=floor(kappa n),kappa=1/(16C), then discarding finitely many witnesses makes r>=kappa n/2.
Markov's inequality yields F_n<=2exp(-gamma n), gamma=min(1/pi²,kappa log2)>0, hence the conditional gap above.
This common high-moment bound is unproved, original equal-length relations are retained, and full dissociation is unavailable.

For every fixed actual input along the unbounded complete witness quotients,

    max_(chi!=1)W_n(chi) ->1.

In the real diagonal block form the complete proof constructs symmetric shrinking bodies K_n(delta) contained in[-delta,delta]^d, keeping the first n phases within delta, of volume c_A delta^d exp(-nm).
The dual lattice has covolume1/R_q.
With delta_n=exp(-mn/(2d)), elementary lattice averaging yields a nontrivial character and W_n>=1-pi²n delta_n² tending to1.
For every fixed0<delta<1/2, the fraction of nontrivial characters with all first n phases at mostdelta is at least

    (c_A/2^d)delta^d exp(-nm)-R_q^(-1).

Thus a uniform bound for every nontrivial character is false even for each fixed actual core; the average criterion remains distinct.
No field-component estimate replaces the full character sum, and no new source, computation, universal moment estimate or Lehmer solution is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:39 |
| status | open |
| reason | Register the entire original conditional theorems and unconditional exact identities/obstruction with their fixed accepted inputs; actual whole current review and adoption follow separately. No missing arithmetic hypothesis is promoted to a theorem. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire full-quotient Fourier/Plancherel normalization, conditional averaged gap and genuine limit, all exact second/high moments and ranges, full real-block shrinking-body obstruction and quantitative lower tail, with every unresolved arithmetic hypothesis. |
| argument | [Entire original proof](#argument) | Complete original character/orbit, collision-subadditivity, Chebyshev/Markov, integral norm transfer, Haar relation count, real diagonal volume and dual-lattice translate/count proofs; every constant, floor, multiplicity and probability guard. |
| dependency | [Full faithful binary model](Yin_C_G0272_v1.md#short-binary-faithful-primitive-quotient) | Entire companion-order q-saturation, norm divisibility and exact word-fiber transfer for every1<=n<=floor(q/4); original collisions are retained. |
| dependency | [Controlled primitive witness](Yin_C_G0265_v1.md#finite-set-primitive-norm-escape) | Exact q/B/eta cutoffs and log Prim_q>=qm/2; fixed-input eta=m is permitted without a uniform threshold. |
| dependency | [Complete window count](Yin_C_G0265_v1.md#finite-window-primitive-count) | Exact candidate/exclusion count and sufficient even-B criterion, yielding unbounded q for fixed d and eta; no common family cutoff or prime range is inferred. |
| dependency | [Rational entropy formula](Yin_C_G0205_v1.md#rational-primary-formula) | Accepted rational companion entropy on Q^d equals m and its monotonicity upper bound only; all Fourier, moment and lattice arguments are proved here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T06:45 |
| status | proved |
| reason | Adopt every original exact Fourier/moment/pointwise-obstruction assertion and precisely conditional gap implication after actual whole self-review. Full quotient normalization, unbounded faithful subsequence, all moment cutoffs and lattice counts are retained; common averaged escape/high-moment estimates remain unproved hypotheses and no Lehmer solution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire full-quotient Fourier/Plancherel normalization, conditional averaged gap and genuine limit, all exact second/high moments and ranges, full real-block shrinking-body obstruction and quantitative lower tail, with every unresolved arithmetic hypothesis. |
| argument | [Argument](#argument) | Complete original character/orbit, collision-subadditivity, Chebyshev/Markov, integral norm transfer, Haar relation count, real diagonal volume and dual-lattice translate/count proofs; every constant, floor, multiplicity and probability guard. |
| dependency | [Dependency](Yin_C_G0272_v1.md#short-binary-faithful-primitive-quotient) | Entire companion-order q-saturation, norm divisibility and exact word-fiber transfer for every1<=n<=floor(q/4); original collisions are retained. |
| dependency | [Dependency](Yin_C_G0265_v1.md#finite-set-primitive-norm-escape) | Exact q/B/eta cutoffs and log Prim_q>=qm/2; fixed-input eta=m is permitted without a uniform threshold. |
| dependency | [Dependency](Yin_C_G0265_v1.md#finite-window-primitive-count) | Exact candidate/exclusion count and sufficient even-B criterion, yielding unbounded q for fixed d and eta; no common family cutoff or prime range is inferred. |
| dependency | [Dependency](Yin_C_G0205_v1.md#rational-primary-formula) | Accepted rational companion entropy on Q^d equals m and its monotonicity upper bound only; all Fourier, moment and lattice arguments are proved here. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0533_v1.md#current-primitive-fourier-finding) | Entire current statement, complete original argument and all selected interfaces at their exact scope, self-reviewed; old findings keep their original fixed inputs and relationships. |

## Complete retained argument

<a id="argument"></a>

<a id="primitive-fourier-setting"></a>
### The full quotient and its exact binary Fourier law

Let alpha be a nontorsion algebraic unit, P its monic irreducible polynomial of degree d, O=Z[alpha], and m=log M(P)>0.
Identify O with Z^d in its power basis, let A be multiplication by alpha, and v=1=e_0.
For a prime index q put

    J_q=(Phi_q(alpha)O:q^infinity),
    M_q=O/J_q,    R_q=|M_q|=Prim_q.

These are the companion-order objects of [L G0081](Yin_C_G0272_v1.md#short-binary-faithful-primitive-quotient).
In particular M_q is the entire prime-to-q quotient, not one residue-field image.
We use witnesses from [L G0078](Yin_C_G0265_v1.md#finite-window-primitive-count) with parameters eta<=m, B and q satisfying

    q<=B,    q>=2+4d log(2B)/eta,
    log R_q>=qm/2.                                       (1)

For each fixed input, set eta=m.
The finite-window count in that record supplies such witnesses for arbitrarily large B and with q tending to infinity: its sufficient inequality (17) holds for all sufficiently large even B, and its lower endpoint tends to infinity.
Hence n=floor(q/4) tends to infinity.
For every 1<=n<=floor(q/4), projection to M_q preserves all original length-n binary word fibers, not only their number, and

    R_q^(-1)<=exp(-2mn).                                  (2)

Here and below, a character of a finite additive group has values in the unit circle.
Write its values on v_j=A^jv as chi(v_j)=exp(2pi i theta_j), with theta_j in R/Z.
For independent fair binary digits let X_n=sum_(j<n) epsilon_j v_j, with law nu_n.
Independence gives exactly

    nuhat_n(chi)=product_(j<n) (1+chi(v_j))/2,
    W_n(chi)=|nuhat_n(chi)|^2
             =product_(j<n) cos^2(pi theta_j).             (3)

Character orthogonality gives the finite Plancherel identity

    Col(nu_n)=sum_x nu_n(x)^2
      =R_q^(-1) sum_chi W_n(chi)
      =R_q^(-1)+F_n,
    F_n=R_q^(-1) sum_(chi!=1) W_n(chi).                    (4)

For example, expanding the squared transform and summing uses R_q^(-1)sum_chi chi(x-y)=1 for x=y and zero otherwise.
This proves the identity with its stated normalization.

The dual action A^*chi=chi composed with A has order q, and every nontrivial character has exact period q.
Indeed the same Phi_q relation holds on the dual, and a fixed character would be killed by q, which is invertible on this finite group.
Thus the nontrivial sum in (4) can be grouped as

    R_q^(-1) sum_(nontrivial dual orbits U)
      sum_(r=0)^(q-1) product_(j=0)^(n-1)
                       cos^2(pi theta_(r+j)).             (5)

The phase sequence in each orbit is q-periodic.
The product is constant along an orbit when n=q.
For a shorter window it need not be constant.
A bound restricted to characters from one field quotient does not bound the full sum (4): the remaining characters have nonnegative contributions that must also be controlled.

<a id="averaged-fourier-gap-criterion"></a>
### A sufficient averaged estimate which would give an entropy gap

Put E_n(chi)=sum_(j<n) ||theta_j||_(R/Z)^2.
The elementary inequalities sin(pi x)>=2x for 0<=x<=1/2 and 1-u<=exp(-u) give

    W_n(chi)<=exp(-4E_n(chi)).                            (6)

Fix gamma>0.
Suppose, along arbitrarily large witnesses (1) with n=floor(q/4), that all but at most R_q exp(-gamma n) nontrivial characters have E_n(chi)>=gamma n/4.
Then

    F_n<=2 exp(-gamma n),
    Col(nu_n)<=exp(-2mn)+2exp(-gamma n),
    H_2(nu_n)>=n min(2m,gamma)-log 3.                      (7)

The exceptional characters contribute at most their fraction; each other product is at most exp(-gamma n).
More generally, the direct assumption F_n<=C exp(-gamma n), with C independent of n for the fixed input, gives the same limiting consequence.
This is an average with normalization R_q, not a bound for each nontrivial character.

To take the limit legitimately, let H_2^O(n) be the order-two Renyi entropy of the original binary law in O.
The two independent blocks of lengths n and r give

    Col^O(n+r)>=Col^O(n)Col^O(r).

Indeed coincidence of both block pairs implies coincidence of their sums, and multiplication by alpha^n is injective.
Thus H_2^O is subadditive and h_2=lim_n H_2^O(n)/n exists.
Also H_2^O(n)<=log|T_n(alpha,{0,1})|; subadditivity of the latter and the accepted rational algebraic-entropy formula give

    h_2<=h_support<=h(A|Q^d)=m.                            (8)

The source interface is [L G0002](Yin_C_G0205_v1.md#rational-primary-formula); no equality h_support=m is assumed.
The faithful transfer of L G0081 identifies H_2^O(n) with (7) along this unbounded subsequence.
Therefore

    m>=h_2>=min(2m,gamma).                                (9)

Consequently (7)'s hypothesis is impossible when 0<m<gamma.
If a common gamma were proved for every member of the target unit class along such witnesses, it would establish m>=gamma on that class.
Existing support-entropy deficits do not alter this implication, which only uses the upper bound (8).
No common gamma, or estimate (7)'s hypothesis, is proved here.

<a id="automatic-fourier-second-moments"></a>
### Positive mean energy is automatic; its elementary tail is only polynomial

The following calculation holds in every nonzero finite cyclic module generated by 1 with Phi_q(A)=0, q odd and q coprime to its order R.
It does not use the arithmetic witness (1).
For 1<=n<=q the v_j are distinct nonzero elements.
If 2*1!=0, no two of these elements, including one repeated, sum to zero.
For A^i1=-A^j1 would imply A^(2(i-j))1=1, forcing i=j modulo q, and then 2*1=0.
The alternative 2*1=0 makes the entire cyclic module have exponent two.

Define the sine energy and orbit sum by

    S_n(chi)=sum_(j<n) sin^2(pi theta_j)
             =n/2-(1/2)Re Z_n(chi),
    Z_n(chi)=sum_(j<n) chi(v_j).

Uniform averaging over all R characters gives

    average S_n=n/2,
    average [(Re chi(v_i))(Re chi(v_j))]
      =(1/2)(1_(v_i=v_j)+1_(v_i=-v_j)),
    Var(S_n)=n/4 if 2*1=0, and n/8 otherwise.              (10)

These formulas follow by expanding real parts into chi and its inverse and applying character orthogonality.
In particular a positive average sine energy is already automatic and supplies no additional arithmetic information.
Chebyshev's inequality and W_n<=exp(-S_n) yield

    fraction{chi:S_n<n/4}<=4/n,
    Col(nu_n)<=4/n+exp(-n/4),                             (11)

with 2/n replacing 4/n when 2*1!=0.
The trivial character is included in both averages; no extra R^(-1) term is needed in (11).
This particular second-moment argument gives at most a logarithmic entropy lower certificate.
It does not provide the exponential exceptional-character bound needed in (7).

<a id="faithful-high-moment-arithmetic-interface"></a>
### Exact high moments turn the required tail into original additive energy

Let O's Pontryagin dual be the ordinary compact torus T^d=Hom(O,R/Z), with normalized Haar measure dy.
Thus the original integral flow uses a continuous torus average, whereas the quotient uses the finite uniform average in (4).
For positive integers n,r define the original additive energy

    A_(n,r)=#{(i_1,...,i_r,j_1,...,j_r) in {0,...,n-1}^(2r):
                 sum_l alpha^(i_l)=sum_l alpha^(j_l) in O}
       =integral_(T^d) |sum_(j<n) exp(2pi i<y,A^j1>)|^(2r) dy.
                                                               (12)

The equality follows by expanding the power and integrating each integer character.
The corresponding finite-character moment counts precisely the same relations modulo J_q.
The difference polynomial R(t) of any two r-term sums has degree at most n-1 and coefficient l1 norm at most 2r.
For R(alpha)!=0 its field norm obeys

    log|Norm R(alpha)|<=d log(2r)+(n-1)m.                   (13)

If 1<=n<=floor(q/4) and 1<=r<=B, (1) makes the right side strictly smaller than qm/2<=log R_q.
Membership in J_q would force R_q to divide this nonzero norm, by L G0081's q-saturation argument, and is therefore impossible.
Hence

    R_q^(-1) sum_chi |Z_n(chi)|^(2r)=A_(n,r)
         for 1<=n<=floor(q/4), 1<=r<=B.                   (14)

This transfers all original relations at these moment orders, including their multiplicities.
It does not assert the absence of original relations or bound their number.

Here is one explicit sufficient target, with no optimization of constants.
Suppose there is a common C>=1 for a class of inputs such that, along their witnesses with n=floor(q/4),

    A_(n,r)<=(C r n)^r,
    kappa=1/(16C),    r=floor(kappa n)>=1.                 (15)

One may discard finitely many witnesses to have n>=2/kappa.
Then r<=B and r>=kappa n/2.
By (14) and Markov's inequality,

    fraction{chi:|Z_n(chi)|>=n/2}
       <=(4Cr/n)^r<=4^(-r)
       <=exp(-kappa(log2)n).                              (16)

If E_n<n/(4pi^2), then sin^2(pi theta)<=pi^2||theta||^2 and Re Z_n=n-2S_n give Re Z_n>n/2.
All characters outside this exceptional set have W_n<=exp(-n/pi^2).
It follows that

    F_n<=2exp(-gamma n),
    gamma=min(1/pi^2,kappa log2)>0.                        (17)

Thus (15) implies the genuine conditional gap conclusion (9).
The universal C is the unproved part.
Equations (12)--(14) make it a precise bound on original orbit additive relations, not an estimate on a selected field component.
Norm integrality supplies exact transfer, while a bound on the original relation count remains separate.
Complete dissociation is not available: the integer relation (t-1)P(t) has total coefficient sum zero and provides a nontrivial equality between two equal-length lists of powers of alpha once n and r are large enough.

<a id="actual-core-pointwise-fourier-obstruction"></a>
### Every fixed actual core has almost undamped nontrivial characters

In contrast to the averaged condition, a uniform estimate for every nontrivial character is impossible even on the actual full witness quotients of any one fixed input above.
Along the unbounded witnesses (1), with n=floor(q/4), we prove

    max_(chi!=1) W_n(chi) -> 1.                           (18)

Use the real diagonal form A^T=U D U^(-1), which exists because P is separable.
Its real blocks are scalar eigenvalues; its complex blocks are two-dimensional rotation-dilations rho R.
Let K_0 be the product of [-1,1] for real blocks and closed unit disks for complex blocks.
Fix C_A>=1 such that ||Uw||_infinity <=C_A for w in K_0.
In each block of modulus rho, scale K_0 by max(1,rho)^(-n), then apply (delta/C_A)U, obtaining K_n(delta).
It is a symmetric convex body, and for 0<delta<1/2,

    K_n(delta) subset [-delta,delta]^d,
    |<y,A^j1>|<=delta for y in K_n(delta), 0<=j<n,
    vol K_n(delta)=c_A delta^d exp(-nm),   c_A>0.           (19)

Indeed D^j times each scaled block remains in its original interval or disk for these j.
The determinant volume factor from expanding blocks is exactly exp(-nm), counting complex blocks twice.
The constant c_A depends on the fixed input.

The dual lattice Lambda_q=J_q^* consists of the y in R^d with <y,J_q> contained in Z.
It contains Z^d, has covolume 1/R_q, and Lambda_q/Z^d is the full character group of M_q.
For any lattice Lambda and bounded measurable body K, averaging the number of points of Lambda in translates of K/2 over a fundamental domain gives vol(K)/(2^d covol Lambda).
If this is greater than one, some translate contains at least two lattice points; their difference is a nonzero lattice point of K when K is symmetric convex.
This is the needed elementary lattice-volume argument.

Set delta_n=exp(-mn/(2d)).
For all sufficiently large witnesses it is less than 1/2, and by (2) and (19),

    R_q vol K_n(delta_n)>=c_A exp(mn/2) -> infinity.

There is therefore a nonzero y in Lambda_q intersect K_n(delta_n).
It is not an integer vector by (19), so it defines a nontrivial character whose first n phases are all within delta_n of zero.
Consequently

    W_n(chi)>=cos(pi delta_n)^(2n)
             >=1-pi^2 n delta_n^2 -> 1,                  (20)

Indeed cos(pi delta_n)^(2n)=(1-sin^2(pi delta_n))^n is at least 1-n sin^2(pi delta_n), which is at least the displayed lower bound.
Since W_n<=1, this proves (18).
It applies to every fixed actual core, including any small-Mahler core to which (1) applies; it does not rely on lifting a finite-field example.

The same averaging also quantifies why an average is essential.
For any fixed 0<delta<1/2, choose a translate containing at least R_q vol(K_n(delta))/2^d lattice points.
Subtracting one of them gives that many distinct points in Lambda_q intersect K_n(delta).
They are distinct modulo Z^d because the difference of two points of that body has all coordinates of absolute value less than one.
Apart from the zero character, this gives

    R_q^(-1) #{chi!=1:max_(j<n)||theta_j||<=delta}
       >=(c_A/2^d) delta^d exp(-nm)-R_q^(-1).              (21)

This lower tail floor is compatible with averaged escape only at an appropriate rate.
It does not itself prove a lower bound for m.
In particular it explains why replacing (7) by a pointwise escape claim would be a substantive and false change.
