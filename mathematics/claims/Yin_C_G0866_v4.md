---
author: Yin
---

# Coordinate norms and small convex Cayley units of Salem roots

Human author Yin.
This version extends the same arithmetic-return topic to positive rational Cayley weights, including arbitrarily small convex weights.
Its [selected whole assessment](#decision-whole-independent-review-2026-11-05) adopts the complete stated scope after the [independent R1088 v4 finding](../audits/reviews/Yin_R_G1088_v4.md#whole-convex-cayley-finding).
The [v1 monomial-radical and quartic results](Yin_C_G0866_v1.md#decision-whole-independent-review-2026-11-04), [v2 separate-factor dichotomy](Yin_C_G0866_v2.md#decision-whole-independent-review-2026-11-04), and [v3 coupling-arity and Cayley restrictions](Yin_C_G0866_v3.md#decision-whole-independent-review-2026-11-04) retain their fixed statements, proofs, selected assessments and review scopes.
Those earlier reviews do not cover the new CQ1--CQ24 argument, its changed small-weight domain, original-measure return, degree comparison or new unit control.

## Exact inputs and their limits

The fixed-field input is exactly [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001), Lemma 2 and Proposition 3 at the retained statement/displayed-proof inspection.
Every positive Salem power preserves degree and field; every Salem number in a fixed Salem field is a positive integer power of its smallest Salem generator, and generates that field.
The original Salem publications are not newly audited, and no degree-uniform generator estimate or regulator bound is inferred.

The numerical height input is the accepted [C147 v5 interface](Yin_C_G0147_v5.md#reuse-and-source-scope), equation (4) multiplied by its actual degree d:
for a nontorsion algebraic integer unit of degree d>=exp(e), its total logarithmic Mahler measure is at least (1/2400)(log log d/log d)^3.
Its underlying [Smy08-U001 statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001), retained survey printed p.326 equation (11), states M>1+(1/1200)(log log d/log d)^3; the elementary log(1+x)>=x/2 conversion applies on this domain.
Only that statement and conversion are used, not C147's cyclic-norm argument or its other small-height degree-exclusion application.
The retained original-proof and ancestor review limits remain unchanged; the survey's defective resultant explanation is not used.

The exceptional norm branch uses exactly the accepted [Smy08-U002 Schinzel statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002), retained survey equation (22): a totally real algebraic integer outside {0,1,-1} has absolute height at least log(phi)/2, where phi=(1+sqrt(5))/2.
It is applied only to an actual nontorsion unit in a totally real field; the original Schinzel proof is not newly audited.
The ordinary field-norm height inequality and the actual degree comparison needed here are explicitly retained below.

The [C383 actual Salem conjugations and trace field](Yin_C_G0383_v1.md#salem-kernel-class-population) are used at their retained SELF/source scope.
The needed one-pair-fixed sign actions are reconstructed directly below, without a full symmetric top group or split-extension hypothesis.
The [C866 v1 orbit-count argument](Yin_C_G0866_v1.md#salem-monomial-orbits) is reused only for its elementary support and sign counting, after a new proof of additive coefficient-vector injectivity.
For the exact control, [C866 v1's adopted primitive quartic](Yin_C_G0866_v1.md#quadratic-saturation-control) supplies the original polynomial's genuine Salem property, primitiveness, degree four, alpha>2, and splitting-field degree eight.
All properties of the new Cayley output, its irreducibility, own measure and full raw norm are proved in this version.

The preceding v2/v3 inequalities, a universal raw-p2 floor, a joint phase law, Pri11 discrepancy, Bilu equidistribution and any general inverse-Mahler classification are not premises.
The Dubickas inverse-Mahler paper mentioned at the end is a comparison-only lead, not proof support.
No mathematical novelty, short-unit supply for arbitrary original inputs or unrestricted G0001 solution is claimed.

## All-place normalization

All logarithms are natural unless a base is explicitly written.
For a nonzero algebraic number z of actual degree D_z and own field K_z=Q(z), use the places v with their usual extensions of rational absolute values and local degrees n_v.
An archimedean place has n_v=1 or 2 and the usual modulus.
At a finite place above p, use integer ord_v, ramification index e_v, residue degree f_v, n_v=e_v f_v and log|z|_v=-(ord_v(z)/e_v)log p.
Define

    h_abs(z)=(1/D_z)sum_v n_v log^+|z|_v,
    m(z)=D_z h_abs(z),
    M_2(z)^2=D_z sum_v n_v (log|z|_v)^2.                 (N1)

Thus m(z) is total logarithmic Mahler measure of the primitive irreducible polynomial, including its leading coefficient.
For an algebraic integer unit all finite terms vanish and, counting all D_z embeddings separately,

    M_2(z)^2=D_z sum_j log^2|z_j|,
    sum_j log|z_j|=0,
    2m(z)=sum_j |log|z_j||,
    M_2(z)>=2m(z).                                      (N2)

These are the raw own-degree quantities, not degree-normalized heights or FM13 operator identities outside their own domain.
No construction below drops finite places before its actual unit condition is established.

## Statement

### A. Actual coefficient orbit and positive coordinate norms

Let alpha be a genuine Salem number of degree d=2t>=4, L its splitting field, G=Gal(L/Q), V the actual inverse-pair kernel and E_0=L^V.
Choose oriented roots u_1,...,u_t from the distinct inverse pairs and put X_i=(u_i+1)/(u_i-1).
The X_i are linearly independent over E_0.
Select 1<=r<=t pairs, relabelled 1,...,r, and arbitrary positive rational weights a_i, possibly chosen from the current input.
Set

    Z=sum_(i=1)^r a_i X_i,
    beta=(Z+1)/(Z-1),
    K_beta=Q(beta), D=[K_beta:Q].                         (S1)

The expression is defined and nonzero at every embedding and beta is nontorsion.
For Parts A and B impose the explicit sign-domain condition

    r<t, or V is the full inverse-pair flip group.        (S2)

The second alternative is automatic when t is even, including r=t; no such full-kernel assumption is inferred for odd t.
Under S2, integrality of beta is equivalent to being a unit.
Assume that actual integrality.
The output degree is exactly the signed-permutation orbit size of the rational coefficient vector a, extended by zeros, and satisfies D>=2^r t/r.

Let H=Gal(L/K_beta) and let O be its orbits on the selected oriented roots, of sizes q_O and number kappa.
Each O has one common rational weight.
Write alpha=alpha_0^A for its actual smallest Salem field generator alpha_0 and integer source power A>=1, let v_i^A=u_i be the coherent conjugates of alpha_0, and put m_0=log alpha_0=m(alpha)/A.
For i in O define the actual fields and degrees

    K_i=Q(u_i), F_i=K_beta(u_i),
    [F_i:K_beta]=q_O,
    [F_i:K_i]=D q_O/d.

There are integers n_O>=1, and signs epsilon_i in {1,-1}, such that

    Norm_(F_i/K_i)(beta)=epsilon_i v_i^(n_O),
    m(beta)=N m_0, N=sum_O n_O>=kappa,
    M_2(beta)^2>=2d m_0^2 sum_O n_O^2/q_O.               (S3)

For r>=2 the norm signs are positive under the specified positive-root identification.
The factor A and every actual coordinate-field index are retained; these statements do not assert automatic integrality of S1.

### B. Small convex weights and a uniform original-input comparison

In Part A also require sum_i a_i=1 and 0<m(alpha)<=1.
Put B=M_2(beta)/m_0.
Then

    B>=2N>=2kappa,
    q_O>=2d n_O^2/B^2,
    r>=2d kappa/B^2,
    a_i<=B^2/(2d n_O^2)<=B^2/(2d) for i in O.           (S4)

There is an absolute d_0 such that every such source and actual output with d>=d_0 satisfy

    M_2(beta)>=(1/2)d^(1/4)m_0,
    M_2(beta)/m(alpha)>=(1/(2A))d^(1/4)
      >=(1/4800)d^(1/4)(log log d/log d)^3.              (S5)

The last lower bound tends to infinity with d, uniformly over all positive rational convex weights and all original sources of total measure at most one in the exact sign domain S2.
For each fixed C>0, original sources in this domain admitting M_2(beta)<=C m(alpha) therefore have bounded degrees and form a finite set.
No numerical value of d_0 or sharpness of these constants is asserted.

### C. An exact actual-unit control with weights one half

Take the adopted primitive quartic Salem source

    P_alpha(T)=T^4-T^3-3T^2-T+1,
    alpha>2,
    alpha+alpha^(-1)=(1+sqrt(21))/2.

Choose x=alpha and an oriented root y from its other inverse pair, and set beta=Cayley^(-1)((Cayley(x)+Cayley(y))/2), where Cayley(z)=(z+1)/(z-1).
This is the full-sign t=r=2 case of S2.
The output is an actual unit of degree four with irreducible minimal polynomial

    P_beta(T)=T^4-16T^3+78T^2-16T+1,
    m(beta)=5m(alpha),
    M_2(beta)=10m(alpha).                               (S6)

Its two coordinate fields F_i equal the degree-eight splitting field L, its single H-orbit has size q_O=2 and n_O=5, and equality holds in the raw-norm inequality of S3.
All finite places vanish by the actual polynomial.
This source already has m(alpha)>log 2; the control supplies neither a near-zero sequence nor new unrestricted total-gap coverage.

### D. The exceptional full-use odd-kernel norm gate

Suppose r=t is odd, V is exactly the even-flip kernel, all a_i>0 are rational, and beta from S1 is an actual unit.
This part does not assert integrality alone is enough without S2.
Put

    P_even(T)=product_(epsilon in {1,-1}^t,
                     product_i epsilon_i=1)
                  (T-sum_i epsilon_i a_i X_i),
    Gamma=Norm_(L/E_0)(beta).

Then E_0(beta)=L, Gamma is a totally positive unit, and

    Gamma=P_even(-1)/P_even(1).

If Gamma is nontorsion, then M_2(beta)>=log(phi), with phi=(1+sqrt(5))/2.
Its only torsion alternative is Gamma=1, equivalent to the exact equation P_even(-1)=P_even(1).
When t=3 the difference is 16 product_i(a_i X_i), which is nonzero, so the constant floor applies.
For higher odd t, the possible actual unit solutions of that norm equation remain unresolved here.
No missing individual flip or full odd-kernel branch is supplied by Parts A and B.

## Argument

<a id="p2-convex-cayley-unit-norms"></a>
### Small convex Cayley weights: actual units, coordinate norms and a paid original-measure comparison

The inquiry asks whether positive rational Cayley weights whose sum is one can produce actual units with M_2(beta)<=C m(alpha), uniformly on original Salem inputs approaching one.
The weights may depend on the input and may be arbitrarily small.
The fixed [C866 v3 Cayley conclusion](Yin_C_G0866_v3.md#p2-cayley-coupled-unit-gate) does not cover them merely because it handles weights of absolute value at least one.
The argument below constructs one exact unit control and returns the actual output to the original total measure through coordinate norms before estimating its full raw norm.
It never assumes that the original root angles are independent or Haar distributed.

#### Exact original input and the available sign actions

Let alpha>1 be a genuine Salem number of degree d=2t>=4, with splitting field L and G=Gal(L/Q).
Choose oriented roots u_1,...,u_t, one from each inverse pair, and set X_i=(u_i+1)/(u_i-1).
Write C(z)=(z+1)/(z-1), so X_i=C(u_i).
Let V be the actual inverse-pair kernel of G and E_0=L^V.
For each i, the actual conjugate complex conjugation c_i fixes u_i and inverts every u_j with j!=i.
The construction and its source limits are retained in [C866 v3](Yin_C_G0866_v3.md#p2-cayley-coupled-unit-gate), with the [C383 attribution](Yin_C_G0383_v1.md#salem-kernel-class-population).
Explicitly, choose g taking u_i to alpha and let c_i=g^(-1)c g, where c is ordinary complex conjugation in the chosen embedding of L.
It fixes the real inverse pair and inverts every neutral pair after applying g, so its action is exactly the stated one.
The original roots generate L, making that action independent of the choice of g and making all c_i commute.
Thus c_i(X_i)=X_i and c_i(X_j)=-X_j for j!=i, while c_i fixes E_0.

The elements X_1,...,X_t are linearly independent over E_0.
Indeed, if sum_j b_j X_j=0 with b_j in E_0, adding its image under c_i gives 2b_i X_i=0, hence b_i=0 for every i.
None of the X_i is zero, because no genuine Salem root is -1.
In particular they are linearly independent over Q.                         (CQ1)

Select r of these pairs, relabelled 1,...,r, with positive rational a_i, and define

    Z=sum_(i=1)^r a_i X_i,
    beta=(Z+1)/(Z-1),
    K_beta=Q(beta), D=[K_beta:Q].                         (CQ2)

Require the following explicit sign-domain condition for the norm argument:

    r<t, or V contains every individual inverse-pair flip. (CQ3)

When r<t, flipping a used pair together with one unused pair realizes every sign pattern on the used coordinates.
When V is full this is immediate, including r=t.
The latter condition is automatic when t is even: the products c_i c_j give all even flips, while each c_i itself then has odd weight t-1 and generates the full kernel together with them.
No full-sign assertion is made when r=t, t is odd and V is only the even-flip subgroup.
That branch is outside CQ3 and all conclusions below that use it.

The expression CQ2 is defined, nonzero and different from 1 or -1.
For r>=2, at an embedding with a real selected input the remaining selected X_j have a nonzero purely imaginary sum by CQ1, so Z is not 1 or -1.
With all selected inputs neutral, Z is purely imaginary, and CQ1 excludes Z=0.
For r=1, equality a_1 X_1=1 or -1 would make u_1 rational, impossible at degree d>=4.
These facts also exclude Z=0 and the corresponding output -1.

At an embedding where u_i is the positive real root alpha, Re Z=a_i R>0 with R=coth(m(alpha)/2), so |beta|>1.
Where u_i=alpha^(-1), the real part is negative and |beta|<1.
If all selected roots are neutral, |beta|=1.
There is at most one real selected input at each embedding, so these are disjoint and exhaustive radial cases.
Under CQ3, simultaneous inversion of all selected roots sends beta to beta^(-1).
Consequently integrality of beta is equivalent to being a unit; assume that actual integrality from now on.
The real-input cases show that beta is nontorsion.
All finite-place terms therefore vanish, with the raw own-degree normalization [C866 v3 N1--N2](Yin_C_G0866_v3.md#all-place-normalization).

#### Actual output orbit and the coordinate fields

Extend a=(a_1,...,a_r) by zeros to t coordinates.
Every g in G acts by a signed permutation on the X_i, and CQ1 implies

    g(beta)=beta iff g(Z)=Z iff g(a)=a.

Thus D is exactly the signed-permutation orbit size |G.a|.
The support-orbit and sign count from the [fixed C866 v1 argument](Yin_C_G0866_v1.md#salem-monomial-orbits) applies to this additive coefficient vector for the same elementary reason: distinct vectors have distinct values by CQ1.
The support orbit covers all t pairs, each support has r elements, and each support supplies all 2^r sign choices when r<t.
For r=t under the full-kernel branch of CQ3, the full 2^r sign orbit exists directly.
Therefore

    D>=2^r t/r for r<t,
    D>=2^r for r=t under CQ3,
    D>=2^r in both cases.                               (CQ4)

Let H=Gal(L/K_beta), and let O_1,...,O_kappa be its orbits on the selected oriented roots.
Positivity of the a_i and the exact coefficient-vector stabilizer show that H permutes selected roots without inversion, preserving their rational weights.
Write q_O=|O|, so sum_O q_O=r and a_i is constant on each O.
For a selected i set

    K_i=Q(u_i), F_i=K_beta(u_i),
    q_i=[F_i:K_beta]=|H.u_i|=q_O for i in O,
    e_i=[F_i:K_i]=D q_i/d.                              (CQ5)

These are actual fields and degrees; q_i is not replaced by a chosen tuple-field degree or by r unless only an upper bound is wanted.

#### Positive coordinate norms return exact original Mahler powers

Put Gamma_i=Norm_(F_i/K_i)(beta), an actual integer unit of K_i.
At an embedding of K_i taking u_i to a neutral root, average log|beta| over the extensions to F_i.
If another selected root u_j is real, the sign action in CQ3 can flip u_j alone among the selected coordinates while fixing u_i.
For r<t this action flips u_j together with an unused pair; in the full-kernel case it flips u_j itself.
It preserves the selected imaginary coordinates and changes the real part of Z from A to -A.
The identity

    |(A+1+iS)/(A-1+iS)|
      |(-A+1+iS)/(-A-1+iS)|=1

pairs the corresponding logarithms with opposite signs.
The all-neutral extensions already have log|beta|=0.
Right multiplication by the indicated actual Galois element pairs the relevant embeddings, with their uniform restriction multiplicities, so every such embedding of Gamma_i has modulus one.

At the embedding taking u_i to alpha, every extension has log|beta|>0; at u_i=alpha^(-1), every extension has log|beta|<0.
Thus Gamma_i has exactly one expanding and one contracting embedding when counted over K_i, and all other K_i-embeddings have modulus one.
For r>=2 its value at the positive real embedding is positive: the nonzero imaginary sum noted after CQ3 makes the relative embeddings nonreal, and complex-conjugate pairs have positive products.
For r=1 a negative real value is possible, and its sign is retained below.
For r>=2 both real norm values are positive, and their product is one because Gamma_i is a unit and all its other complex-conjugate pairs have product one.
For r=1 the two real values are reciprocal directly from C(u_i^(-1))=-C(u_i), so their signs agree as well.
The unique expanding K_i-embedding also proves that Gamma_i has degree d: every embedding of a proper subfield would occur with extension multiplicity greater than one.
Under the embedding taking u_i to alpha, its sign-corrected value is therefore a genuine Salem number in Q(alpha).

Write alpha=alpha_0^A, where alpha_0 is the smallest Salem generator in Q(alpha) and A>=1 is the actual integer source power.
Use precisely the accepted fixed-field statement [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001), at its retained statement/displayed-proof inspection; no new original Salem proof or regulator estimate is used.
Let v_i be its coherent conjugates, with v_i^A=u_i and Q(v_i)=K_i, and put m_0=log alpha_0=m(alpha)/A.
The actual coordinate norms have the form

    Gamma_i=epsilon_i v_i^(n_i),
    epsilon_i in {1,-1}, n_i>=1 integer.                 (CQ6)

For r>=2 all epsilon_i are positive at the chosen positive-root identification; the possible sign for r=1 has no logarithmic cost.
An h in H carrying u_i to u_j also carries F_i,K_i,Gamma_i,v_i to their j counterparts, so n_i is constant on each orbit O; denote it n_O.

Let ell_i be the average of log|beta| conditional on u_i mapping to alpha, with the uniform full Galois measure.
Each actual extension of that K_i-embedding to F_i has the same number of extensions to L.
The field norm and CQ5--CQ6 therefore give

    ell_i=n_i m_0/e_i=d n_i m_0/(D q_i).                (CQ7)

The conditional mean at u_i=alpha^(-1) is -ell_i.
Each positive-root event has probability 1/d, and they are exactly all the positive-output radial events.
It follows that

    m(beta)=D sum_i ell_i/d
           =m_0 sum_i n_i/q_i
           =m_0 sum_O n_O=:N m_0,
    N=sum_O n_O>=kappa.                                (CQ8)

In particular the output's multiplicative Mahler measure is the actual positive Salem power alpha_0^N.
No field index is discarded in this integer exponent: the q_i denominators cancel only after summing each actual H-orbit of size q_i.
Conditional Cauchy--Schwarz on both radial signs also gives

    M_2(beta)^2
      >=2d m_0^2 sum_i (n_i/q_i)^2
       =2d m_0^2 sum_O n_O^2/q_O.                      (CQ9)

These are positive original-measure return identities conditional on an actual unit, not an assertion that the unit can always be constructed.

#### What a bounded return would force on convex weights

Now impose sum_i a_i=1 and write B=M_2(beta)/m_0.
The unit product formula gives M_2(beta)>=2m(beta), and CQ8--CQ9 imply

    B>=2N>=2kappa>=2,
    q_O>=2d n_O^2/B^2 for every O,
    r>=2d kappa/B^2,
    a_i<=1/q_O<=B^2/(2d n_O^2)<=B^2/(2d).              (CQ10)

Every orbit is contained in an equal-weight class, so the necessary large q_O cannot be supplied by distinct weights.
For a primitive source and a proposed bound M_2(beta)<=C m(alpha), one has B<=C: there must be only boundedly many such orbits, each with a positive degree-proportional size, and every convex weight is O_C(1/d).
For a nonprimitive source the exact effective bound is B<=CA; the source power A is not silently omitted.

The following complete argument deals with the small weights forced by CQ10 without any joint angle-distribution assertion.
Assume 0<m(alpha)<=1.
The accepted numerical Dobrowolski input, in the [C147 v5 normalization](Yin_C_G0147_v5.md#reuse-and-source-scope), gives

    m_0>=(1/2400)(log log d/log d)^3
    for d>=exp(e).                                    (CQ11)

Here alpha_0 has exactly the original degree d by Smy15-U001.
In particular there is an absolute d_0>=16 such that m_0>=3/(4sqrt(d)) for all d>=d_0.
No effective numerical value of d_0 is claimed.

Suppose for contradiction, for such a source, that B<(1/2)d^(1/4).
Since R=coth(m(alpha)/2)<=1+2/m(alpha)<=3/m(alpha), CQ10 gives

    max_i a_i R <=3B^2/(2d m(alpha))
                <=3B^2/(2d m_0)<=1/2.                 (CQ12)

At any actual embedding write Z=W+iS, with S real; W is zero or one of +/-a_i R.
Thus |W|<=1/2 and

    |Z-1|^2=(W-1)^2+S^2 >=(1/4)(1+S^2).

Since beta-1=2/(Z-1) is a nonzero algebraic integer, its ordinary norm in L has absolute value at least one.
With E denoting the uniform Galois average, this implies

    E log|Z-1|<=log 2,
    E log(1+S^2)<=log 16.                              (CQ13)

Choose an H-orbit O carrying at least 1/kappa of the convex weight mass.
Its common weight a satisfies a>=1/(kappa q_O)>=4/(Bd), using kappa<=B/2 and q_O<=d/2.
The event that some selected root in O is real has probability 2q_O/d>=4/B^2.
Define T_B by T_B^2=2^(2B^2)-1.
Markov's inequality applied directly to the nonnegative variable log(1+S^2) in CQ13 gives

    P(|S|>T_B)<=2/B^2.

Therefore a set of actual embeddings of probability at least 2/B^2 has a real selected root from O and |S|<=T_B.
This intersection estimate uses the actual Galois probability measure and no independence between the two events.
On that set, put A_+=aR>0.
Because coth(m(alpha)/2)>=2/m(alpha), one has A_+>=8/(Bd m(alpha)), while CQ12 gives A_+<=1/2.
The exact radial logarithm obeys

    |log|beta||
      =atanh(2A_+/(1+A_+^2+S^2))
      >=2A_+/(2+T_B^2)
      >=16/[Bd m(alpha)(2+T_B^2)].                     (CQ14)

Multiplying its squared Galois average by the square of the actual own degree D yields

    M_2(beta)>=16sqrt(2) D/[B^2 d m(alpha)(2+T_B^2)],
    D<=B^3 d m(alpha)m_0(2+T_B^2)/(16sqrt(2))
      <=B^3 d(1+2^(2B^2))/(16sqrt(2)).                 (CQ15)

On the other hand CQ4 and CQ10 give log_2 D>=r>=2d/B^2.
The assumed B<(1/2)d^(1/4) makes the latter greater than 8sqrt(d), whereas CQ15 gives

    log_2 D <=(7/4)log_2 d+(1/2)sqrt(d)+1
             <=(5/2)sqrt(d) for d>=16.

The last elementary comparison follows from (7/4)log_2 d+1<=2sqrt(d), with equality at d=16 and an increasing difference thereafter.
This contradiction proves, for every d>=d_0 in the exact sign domain CQ3,

    M_2(beta)>=(1/2)d^(1/4)m_0,
    M_2(beta)/m(alpha)>=(1/(2A))d^(1/4).                (CQ16)

Since m(alpha)=A m_0<=1, one has 1/A>=m_0; combining CQ11 and CQ16 gives the degree-uniform original-input comparison

    M_2(beta)/m(alpha)
       >=(1/4800)d^(1/4)(log log d/log d)^3 ->infinity. (CQ17)

Thus even arbitrarily small positive convex weights cannot give a fixed-C return on unbounded-degree sources of total measure at most one in this exact domain.
For fixed C the admitted original sources have bounded degree and form a finite set by the usual bounded integer-coefficient estimate.
This conclusion pays the actual source power A rather than assuming all sources primitive.
It uses the coordinate-norm identities, actual sign-orbit degree and an integer norm of beta-1; no uniform or independent phase law, finite experiment or universal raw-p2 floor is a premise.

#### An exact positive unit control at small weights

The integrality hypothesis is not empty and cannot simply be discarded as impossible for convex weights.
Use the [adopted primitive quartic control](Yin_C_G0866_v1.md#quadratic-saturation-control)

    P_alpha(T)=T^4-T^3-3T^2-T+1,
    alpha>2,
    theta=alpha+alpha^(-1)=(1+sqrt(21))/2.

The source's primitiveness, actual degree four and splitting-field degree eight remain at that fixed proof and its assessment.
Let x=alpha and let y be either oriented root from the other inverse pair, with trace theta'=(1-sqrt(21))/2.
Put X=C(x), Y=C(y), choose a_1=a_2=1/2, and let beta=C^(-1)((X+Y)/2).
Here t=r=2 is covered by the full-sign branch of CQ3.
Since C(u)^2=(u+u^(-1)+2)/(u+u^(-1)-2), direct trace arithmetic gives

    X^2+Y^2=6, X^2Y^2=-1/3,
    Z^2=(3+XY)/2,
    gamma:=beta+beta^(-1)=2(Z^2+1)/(Z^2-1)
                              =8-6XY=8+/-2sqrt(-3).   (CQ18)

For the middle simplification use (XY)^2=-1/3, so (5+XY)/(1+XY)=4-3XY.
The element gamma has degree two in Q(sqrt(-3)).
The discriminant gamma^2-4=48+/-32sqrt(-3) has norm 5376=256*21, which is not a rational square.
It cannot be a square in Q(sqrt(-3)), since the norm of a square in that field is a rational square.
Therefore beta has actual degree four and its minimal polynomial is

    P_beta(T)=(T^2-gamma T+1)(T^2-conjugate(gamma)T+1)
             =T^4-16T^3+78T^2-16T+1.                   (CQ19)

This monic polynomial with constant coefficient one proves actual integrality and invertibility, so every finite-place contribution vanishes.
The original Re Z>0 gives |beta|>1; the four conjugates are beta, conjugate(beta), beta^(-1), and conjugate(beta)^(-1), all distinct and nonreal.
Write Q=|beta|^2>1, the multiplicative Mahler measure of this degree-four output.
Using gamma=beta+beta^(-1) and gamma^2-4=(beta-beta^(-1))^2 gives

    Q+Q^(-1)=(|gamma|^2+|gamma^2-4|)/2
             =38+8sqrt(21).                            (CQ20)

On the source side theta^2=theta+5, so

    alpha^5+alpha^(-5)
      =theta^5-5theta^3+5theta
      =16theta+30=38+8sqrt(21).

Both Q and alpha^5 exceed one, so the unique larger root of the same reciprocal quadratic gives Q=alpha^5 exactly.
Consequently

    m(beta)=5m(alpha),
    M_2(beta)=10m(alpha).                               (CQ21)

The last equality uses its actual four conjugates, whose logarithmic moduli are twice +5m(alpha)/2 and twice -5m(alpha)/2.
The coordinate field F_i equals L here: K_i is real at its positive-root embedding, beta is nonreal, and the known splitting-field degree is eight.
Thus q_i=2, there is one H-orbit of size two, and CQ6--CQ9 have n_O=5 and attain equality in CQ9.
This is an exact actual-unit example, with no numerical approximation or native computation used as evidence.
Its source has m(alpha)>log 2, so it supplies no near-one sequence or unrestricted gap coverage.

#### Remaining construction scope and a literature comparison

The full-use case r=t with odd t and only the even-flip kernel has not been discharged by these coordinate norms.
The unused-pair or full-kernel step in CQ3 cannot be inferred from sign-orbit size alone.
Input-field-dependent coefficients, nonconvex rational weights and other coupled unit operations also retain their own unresolved arithmetic and norm costs.
The exact control CQ18--CQ21 proves that convex Cayley units exist, while CQ16--CQ17 show that this construction cannot yield the proposed uniform return in the proved sign domain.
The next positive construction must change that domain or operation and still supply an actual unit, rather than replacing the missing integrality by a formal torus identity.

For the exceptional full-use odd case, a further exact gate can be isolated without pretending to settle it.
Assume r=t is odd, V is exactly the even-flip kernel, a_i>0 are rational, and beta from CQ2 is an actual unit.
Set

    P_even(T)=product_(epsilon in {1,-1}^t,
                     product_i epsilon_i=1)
                  (T-sum_i epsilon_i a_i X_i),
    Gamma=Norm_(L/E_0)(beta).

CQ1 makes the V-orbit of Z free, so E_0(beta)=L and [L:E_0]=2^(t-1)<=D.
The field E_0 is totally real at the retained C383 trace-field scope.
At every real embedding of E_0, the corresponding complex conjugation belongs to V and pairs the nonzero factors in the norm, so Gamma is a totally positive unit.
If Gamma is nontorsion, the accepted [Schinzel interface](../audits/literature/Smy08/Yin_U002.md#smy08-u002) and the same ordinary-norm inequality used in [C866 v2](Yin_C_G0866_v2.md#trace-field-and-unit-norm) give

    h_abs(Gamma)>=log(phi)/2,
    h_abs(Gamma)<=[L:E_0]h_abs(beta),
    M_2(beta)>=2D h_abs(beta)>=log(phi),
    phi=(1+sqrt(5))/2.                                  (CQ22)

For the height inequality, at each place the norm is a product of the corresponding conjugate values, with their actual local multiplicities.
The inequality log^+|product z_j|<=sum_j log^+|z_j|, followed by the usual local-degree-weighted sum, gives h_abs(Gamma)<=[L:E_0]h_abs(beta).
The other comparison uses E_0(beta)=L, which implies [L:E_0]<=D, together with the unit inequality N2.
This uses only the accepted totally real integer statement and its retained source-proof limits.
It supplies no uniform small unit when the norm is torsion.
Since Gamma is totally positive, its torsion alternative is exactly Gamma=1.
The even-sign orbit has even size and all denominators are nonzero, so

    Gamma=P_even(-1)/P_even(1),
    Gamma=1 iff P_even(-1)=P_even(1).                    (CQ23)

For t=3, writing A_i=a_i X_i, direct expansion gives

    P_even(T)=T^4-2(sum_i A_i^2)T^2-8A_1A_2A_3 T
                +sum_i A_i^4-2sum_(i<j)A_i^2 A_j^2,
    P_even(-1)-P_even(1)=16A_1A_2A_3!=0.                (CQ24)

Thus CQ22 applies to every actual unit in that t=3 full-use domain.
For larger odd t, the analogous difference has additional polynomial factors; no assertion that they avoid zero on every original Salem input has been proved here.
The unresolved branch is the actual unit condition together with the exact norm equation CQ23, rather than an assumed supply of missing independent flips.

A bounded comparison inspected the introduction and theorem statements of [Dubickas, Salem numbers as Mahler measures of nonreciprocal units, Acta Arithmetica 176 (2016), 81--88](https://epublications.vu.lt/object/elaba:18919615/18919615.pdf).
It gives inverse-Mahler constructions, including quartic and certain higher-degree Salem measures; the inspected passages do not classify every preimage of a Salem measure as a radical of its original conjugates.
That paper is a further-reading lead, not an adopted proof input to CQ1--CQ24; no original proof or general inverse classification is asserted here.
The present exact identities do not themselves imply such a classification.

## Scope and review boundary

The complete fixed statement and argument comprise N1--N2, Statement A--D/S1--S6 and CQ1--CQ24.
The general coordinate-norm and convex comparison conclusions require precisely r<t or the actual full flip kernel.
The exceptional odd full-use branch retains its separate actual-unit assumption, norm dichotomy and unresolved norm-one equation.
The positive quartic control is one verified finite algebraic construction, with every polynomial, field, irreducibility, own-measure and full-norm identity proved above; it is not original near-one coverage.
The fixed v1--v3 statements and selected evidence retain their separate scopes, and their independent reviews do not certify this changed argument.
No numerical experiment, native computation or new original-source proof audit is used.
The unrestricted [G0001 total-Mahler objective](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:37 |
| status | proved |
| reason | Adopt complete N1--N2, A--D/S1--S6 and CQ1--CQ24 after independent whole R1088 v4. Positive coordinate norms give an exact integer original-Mahler return, and the actual orbit degree plus integer norm excludes uniform raw-p2 compression by small convex weights in the exact unused-pair or full-kernel domain, with nonprimitive source powers paid. The exact quartic control is an actual unit above log2. The higher odd full-use norm-one branch remains the stated unresolved equation; no unrestricted total-Mahler gap or general unit supply follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire A--D/S1--S6 with N1--N2, arbitrary positive rational weights, explicit sign domain, exact own degree and coordinate fields, convex comparison, primitive quartic output and exceptional norm gate. |
| argument | [Complete argument](#argument) | All CQ1--CQ24, actual coefficient orbits, coordinate norms and integer exponent, conditional Cauchy and Markov estimates, degree contradiction, source-power comparison and exact symbolic control. |
| dependency | [Salem conjugation and trace-field interface](Yin_C_G0383_v1.md#salem-kernel-class-population) | Exact actual signs and totally real fixed field at retained SELF/source scope; the needed sign construction is checked directly in this version. |
| dependency | [Numerical source interface](Yin_C_G0147_v5.md#reuse-and-source-scope) | Only the numerical Dobrowolski statement and conversion at actual degree d, retaining original proof and ancestor relationship limits. |
| dependency | [Support-count interface](Yin_C_G0866_v1.md#salem-monomial-orbits) | Only elementary support and sign counting after the new additive injectivity proof; no radical classification transferred. |
| dependency | [Adopted primitive source control](Yin_C_G0866_v1.md#quadratic-saturation-control) | Actual quartic Salem source, primitiveness, trace and splitting-field degrees; the new output is proved here. |
| support | [Fixed-field Salem generator](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Positive powers preserve degree/field and all Salem elements in that field are powers of the smallest generator, at retained statement/displayed-proof scope. |
| support | [Numerical height statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact accepted numerical constant and total-measure normalization; defective resultant mechanism and uninspected original proof are excluded. |
| support | [Totally real height statement](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Exact Schinzel statement only for the actual nontorsion totally positive norm, with no new original proof audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v4.md#whole-convex-cayley-finding) | Complete current normalization, statement and proof, exact control and higher-odd exception, with all source/ancestor limits and no G0001 completion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
