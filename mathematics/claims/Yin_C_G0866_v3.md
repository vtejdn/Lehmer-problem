---
author: Yin
---

# Raw-p2 costs of coupled Salem-root units and Cayley constructions

Human author Yin.
This version extends the arithmetic-return topic to genuinely coupled rational functions of several original Salem inverse pairs.
Its [selected whole assessment](#decision-whole-independent-review-2026-11-04) adopts the complete stated scope after the [independent R1088 v3 finding](../audits/reviews/Yin_R_G1088_v3.md#whole-coupled-output-finding).
The complete [v1 radical-degree result](Yin_C_G0866_v1.md#statement) and its [selected assessment](Yin_C_G0866_v1.md#decision-whole-independent-review-2026-11-04), and the complete [v2 arbitrary separate-factor dichotomy](Yin_C_G0866_v2.md#statement) and its [selected assessment](Yin_C_G0866_v2.md#decision-whole-independent-review-2026-11-04), remain unchanged at their fixed homes.
Neither earlier assessment or independent review covers the statements below, and their conclusions are not premises of this version.

## Exact inputs and source limits

The only numerical height input is the already accepted [C147 v5 consequence](Yin_C_G0147_v5.md#argument), equation (4) multiplied by the actual output degree D:
for a nontorsion algebraic integer unit beta and D>=exp(e),

    m(beta)>=(1/2400)(log log D/log D)^3.                 (IN1)

Its underlying accepted statement is [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001), retained survey printed p.326 equation (11), M(beta)>1+(1/1200)(log log D/log D)^3.
The elementary conversion log(1+x)>=x/2 applies here because 0<x<=1 for D>=exp(e).
Only that numerical source statement and conversion are used, not C147's cyclic-norm estimate, inverse threshold or small-height premise for establishing the degree condition in its other application.
The source's statement/applicability inspection, original Dobrowolski-proof limits and the ancestor review's actual relationship remain unchanged.
The survey's defective resultant explanation is not used.

The only distribution input is [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), Theorem 3.1/equation (3.2) of the retained arXiv:1307.5734v1 edition.
For an integer polynomial Q of degree d>=55 with simple roots, a globally A-Lipschitz real function supported in the disk of radius R has full-root discrepancy from normalized circle measure at most A(2R+1)sqrt(log(max(d,M(Q)))/d).
The exact test function, support, Lipschitz constant, circle mean, original-root degree and actual Mahler measure are verified below.
This is accepted at its retained statement/applicability scope; the source potential-theory proof and original inputs are not newly independently audited.

The optional common-power specialization uses only the accepted positive Salem power degree/field preservation in [Smy15-U001](../audits/literature/Smy15/Yin_U001.md#smy15-u001), at its retained statement/displayed-proof inspection.
The original Salem publications are not newly audited.
The [actual Salem conjugations in C383](Yin_C_G0383_v1.md#salem-kernel-class-population) are a reuse and attribution input at their retained SELF/source scope; their needed construction and sign actions are also proved directly below.
No assertion about a full symmetric top group, splitting of the Galois extension, regulator, primitive generator or arbitrary unit lattice is imported.

[C852's fixed-function result](Yin_C_G0852_v1.md#fixed-rational-function-height-gap) and [C865's real-or-circle output result](Yin_C_G0865_v1.md#statement) are comparisons only.
Neither theorem, its source machinery, the v1/v2 conclusions, nor the universal raw-p2 floor is a proof premise here.
No mathematical novelty or unrestricted G0001 completion is asserted.

## All-place normalization

All logarithms are natural.
For a nonzero algebraic number z of actual degree D_z and own field K_z=Q(z), let v run over its places with the usual extensions of rational absolute values and local degrees n_v.
At an archimedean place n_v is 1 or 2 and the absolute value is the usual modulus.
At a finite place above p, use the integer valuation ord_v, ramification index e_v and residue degree f_v, so n_v=e_v f_v and log|z|_v=-(ord_v(z)/e_v)log p.
Define

    h_abs(z)=(1/D_z)sum_v n_v log^+|z|_v,
    m(z)=D_z h_abs(z),
    M_2(z)^2=D_z sum_v n_v (log|z|_v)^2.                 (N1)

Thus m(z) is total logarithmic Mahler measure of the primitive irreducible polynomial, including its leading coefficient.
The raw quantity M_2 is not a degree-normalized height or an FM13 operator identity.
Write

    M_(2,arch)(z)^2=D_z sum_(j=1)^(D_z)log^2|z_j|,       (N2)

where all embeddings are counted, including both members of each nonreal pair.
When z is an algebraic integer unit, all finite terms vanish and M_2=M_(2,arch); the product formula then gives sum_j log|z_j|=0 and 2m(z)=sum_j |log|z_j||.
No assertion about an arbitrary nonunit below discards its finite-place terms.

## Statement

### A. Varying functions and actual coupling arity

Let alpha be any genuine Salem number of degree d=2t>=4, let L be its splitting field, and choose 1<=r<=t oriented roots u_1,...,u_r from distinct inverse pairs.
Let F belong to Q(X_1,...,X_r), possibly chosen from the current input with arbitrary degree, coefficients and denominators, and suppose beta=F(u_1,...,u_r) is defined, nonzero and a nontorsion algebraic integer unit.
Require only the actual-orbit condition that |sigma(beta)|=1 for every sigma in Gal(L/Q) for which all |sigma(u_i)|=1.
Let D=[Q(beta):Q] and let k count its actual off-circle conjugates.
Then

    k/D<=2r/d,
    d/r<=D<=product_(j=0)^(r-1)(d-2j)<=d^r,
    M_2(beta)>=2m(beta)sqrt(d/(2r)).                     (S1)

If d/r>=exp(e), then

    M_2(beta)>=sqrt(d)/(1200sqrt(2) r^(7/2))
                  [log(r log d)/log d]^3.               (S2)

In particular M_2(beta) tends uniformly to infinity for fixed r, or along any sequence with r=o(d^(1/7)), as d tends to infinity.
For fixed B>0, a sequence with d tending to infinity and M_2(beta)<=B must eventually satisfy

    r>=[1/(1200sqrt(2)14^3 B)]^(2/7)d^(1/7).             (S3)

For fixed r and C>0, the original Salem sources with m(alpha)<=1 admitting such an output with M_2(beta)<=C m(alpha) have bounded degrees and form a finite set.
The same conclusions hold after replacing all selected u_i by a common positive integer power, with the actual-orbit condition imposed on that powered tuple.
Neither primitive-source status nor a near-one hypothesis is required for S1--S3.

### B. Two-variable rationally weighted Cayley output

Let alpha be a genuine Salem number with degree d>=4 and 0<m=log alpha<=1, and choose x,y from distinct inverse pairs.
For rational a,b>=1 put C(z)=(z+1)/(z-1), R=coth(m/2), and

    Z=aC(x)+bC(y),
    beta=(Z+1)/(Z-1).                                   (S4)

Every conjugate is defined and nonzero.
All-neutral input conjugates have output modulus one; every real-input conjugate is nonreal and off the circle.
At the actual output degree D, one has

    d<=D<=d(d-2),
    k/D=4/d,
    M_(2,arch)(beta)^2
       <=(2D^2/d)m^2(a^(-2)+b^(-2)).                    (S5)

If beta is an algebraic integer it is a nontorsion unit.
When also d>=10^6, this integrality necessarily implies a<=64 and b<=64.
These are necessary conditions, not a unit-existence statement or an all-place estimate for nonintegral outputs.
Every actual unit output satisfies Part A with r=2, uniformly even when a,b depend on the input.

### C. Arbitrarily many nonvanishing rational Cayley weights

Let alpha be a genuine Salem number of degree d=2t>=4.
Choose 1<=r<=t oriented roots u_i from distinct inverse pairs and rational a_i>=1, and put

    Z=sum_(i=1)^r a_i C(u_i),
    beta=(Z+1)/(Z-1).                                   (S6)

If d>=10^6, 0<m(alpha)<log(9/8), and beta is an algebraic integer, then it is a nontorsion unit and

    r<d/8,
    r<=R_0:=96(2^288-1).                                (S7)

For every fixed C>0 there is no sequence of genuine Salem sources with m(alpha) tending to zero and outputs in S6 satisfying integrality and M_2(beta)<=C m(alpha).
By reorienting each chosen root, the same assertions hold for arbitrary nonzero rational weights with |a_i|>=1.
The constant R_0 and all displayed constants are not claimed sharp.
Weights of arbitrarily small absolute value, input-field-dependent coefficients, other coupled rational functions and general splitting-field units remain outside this particular conclusion.

## Argument

<a id="p2-bounded-coupling-arity"></a>
### Varying torus-preserving functions of few Salem root pairs

The question is whether a genuinely coupled rational function can turn a Salem source into a unit with bounded raw M_2, while preserving modulus one whenever all its selected input roots are neutral.
Unlike the fixed-function result [C852](Yin_C_G0852_v1.md#fixed-rational-function-height-gap), the function, its degree, coefficients and denominators may depend arbitrarily on the current input.
Unlike [C865](Yin_C_G0865_v1.md#statement), the output may have nonreal conjugates off the unit circle.
The actual number of coupled inverse pairs supplies a different obstruction.

#### Actual orbit support and field degree

Let alpha be any genuine Salem number of degree d=2t>=4, with splitting field L.
Choose 1<=r<=t oriented roots u_1,...,u_r from distinct inverse pairs.
Let F belong to Q(X_1,...,X_r), with F(u_1,...,u_r) defined and nonzero, and set beta=F(u_1,...,u_r).
Assume beta is a nontorsion algebraic integer unit.
Assume also the following actual-orbit property:

    |F(sigma(u_1),...,sigma(u_r))|=1
    whenever every |sigma(u_i)|=1, for sigma in Gal(L/Q).    (BA1)

A rational function mapping its defined nonzero unit-torus inputs to the unit circle is sufficient for BA1, but only the displayed finite orbit property is required.
No fixedness, coefficient-size, rational-function-degree or primitive-source hypothesis is imposed.
The exact output field has degree D=[Q(beta):Q], and k denotes its number of conjugates of modulus different from one.

Every embedding of Q(u_1,...,u_r) is determined by an ordered tuple of distinct oriented inverse pairs.
Therefore

    D<= [Q(u_1,...,u_r):Q]
      <= product_(j=0)^(r-1)(d-2j) <= d^r.                 (BA2)

Under the uniform measure on Gal(L/Q), each sigma(u_i) is uniform among the d original roots.
Exactly two of those roots are real and off the circle.
The events that sigma(u_i) is one of those two roots are disjoint for distinct i, since embeddings preserve the distinct inverse pairs.
Their union has probability exactly 2r/d.
By BA1, the event |sigma(beta)|!=1 is contained in that union.
Every actual embedding of Q(beta) has the same number [L:Q(beta)] of extensions to L, so this count uses the actual output degree:

    k/D<=2r/d.                                            (BA3)

The unit product formula says that the actual logarithms b_j=log|beta_j| sum to zero.
Since beta is nontorsion, at least one b_j is nonzero.
Indeed, if all conjugates had modulus one, the monic polynomials whose roots are their n-th powers would have integer coefficients bounded by the fixed binomial coefficients, for every n>=1.
Those coefficients are algebraic integers and are fixed by the full Galois group, hence are rational integers.
Only finitely many such polynomials and their roots exist, so the sequence of powers of beta would be finite and beta would be torsion.
There must consequently be both a positive and a negative b_j, so k>=2.
Combining this with BA3 gives

    d/r<=D<=d^r.                                          (BA4)

The same conclusions hold when every u_i is replaced by the same positive integer power u_i^n.
Original Salem powers keep their degrees and inverse-pair distinction at the accepted [Smy15-U001 scope](../audits/literature/Smy15/Yin_U001.md#smy15-u001), and the generated tuple field remains a subfield of the one in BA2.
This power variant still requires BA1 for its actual powered tuple; no phase approximation is inferred.

#### Raw norm divergence, including a growing arity

Because beta is a unit, all finite-place contributions vanish and

    sum_j |b_j|=2m(beta),
    M_2(beta)^2=D sum_j b_j^2.

Cauchy--Schwarz on the k nonzero entries and BA3 give

    M_2(beta)>=2m(beta)sqrt(D/k)
             >=2m(beta)sqrt(d/(2r)).                     (BA5)

Use exactly the [accepted C147 v5 numerical consequence](Yin_C_G0147_v5.md#argument), equation (4) multiplied by the actual degree, as already consumed in C865:

    m(beta)>=(1/2400)(log log D/log D)^3
    for D>=exp(e).                                       (BA6)

Its retained source-statement and original-proof inspection limits are unchanged.
No new Dobrowolski source proof or stronger constant is claimed.
The function x -> log log x/log x is positive and nonincreasing for x>=exp(e), since its derivative has the sign of 1-log log x.
If d/r>=exp(e), BA4 therefore permits substitution of the upper endpoint d^r in BA6, yielding the completely paid bound

    M_2(beta)>=(1/1200)sqrt(d/(2r))
                 [log(r log d)/(r log d)]^3
             =sqrt(d)/(1200sqrt(2) r^(7/2))
                 [log(r log d)/log d]^3.                 (BA7)

For every fixed r this tends to infinity as d tends to infinity, uniformly over all functions and actual units in the stated domain.
The same divergence holds for every integer-valued r=r(d) with r=o(d^(1/7)).
Indeed, if r<=d^(1/14), BA7 is at least

    d^(1/4)/(1200sqrt(2))
      [log log d/log d]^3,

which tends to infinity.
If r>d^(1/14), the last bracket in BA7 is at least 1/14 for d>1, while sqrt(d)/r^(7/2) tends to infinity under r=o(d^(1/7)).
The condition d/r>=exp(e) holds eventually in both cases.

Consequently, for any fixed B>0, a sequence of such units with d tending to infinity and M_2(beta)<=B must have r bounded below by a positive B-dependent constant times d^(1/7) eventually.
To see the full eventual assertion rather than merely exclusion of one little-o sequence, first handle d/r<exp(e).
In that branch r>d/exp(e), which exceeds the right-hand side of (BA8) for all sufficiently large d at each fixed B, because d^(6/7) tends to infinity.
Otherwise d/r>=exp(e), so BA7 applies; its first case is impossible for large d and its second case gives

    r >= [1/(1200sqrt(2) 14^3 B)]^(2/7) d^(1/7).          (BA8)

In particular a fixed-r family satisfying M_2(beta)<=C m(alpha), with fixed C and m(alpha)<=1, can arise only from bounded original degrees.
The coefficients of a monic degree-d polynomial with total measure at most one obey |a_(d-j)|<=binomial(d,j)e, so those bounded-degree Salem sources form a finite set.
This is a restriction on this construction class, not a uniform positive gap for arbitrary Salem numbers or unrestricted G0001.

#### Boundary of the obstruction

BA7 is independent of the unknown existence of suitable units and applies after any actual finite-place cancellation has succeeded.
It excludes bounded raw norm for input-dependent torus-preserving rational functions of a fixed number of original inverse pairs, even when they genuinely couple those pairs and have nonreal off-circle output.
It does not classify general units in the splitting field, arbitrary auxiliary coefficient fields, or outputs obtained through external radicals with unbounded extra degree.
It does not apply when wholly neutral input tuples can produce off-circle output: those extra radial places must instead be counted and paid.
The growth rate in BA8 is a necessary condition from this particular numerical Dobrowolski bound, not an asserted sharp coupling threshold or a construction at that threshold.

<a id="p2-cayley-coupled-unit-gate"></a>
### Weighted Cayley constructions and their exact unit restrictions

It supplies a concrete genuinely coupled candidate in BA1, allowing angular spread instead of forcing all output conjugates close to one.
Its rational weights can depend arbitrarily on the input.

Let alpha be a genuine Salem number with degree d>=4 and m=log alpha<=1, and let x,y be oriented roots from two distinct inverse pairs.
Put C(z)=(z+1)/(z-1), choose rational a,b>=1, and define

    Z=a C(x)+b C(y),
    beta=(Z+1)/(Z-1).                                    (CY1)

No original root is 1 or -1, so the Cayley expressions are defined.
At every embedding, either both input roots are neutral, or exactly one is real and positive.
For a neutral root z, C(z) is purely imaginary and nonzero.
For a real root alpha^epsilon, epsilon in {1,-1}, C(alpha^epsilon)=epsilon R with R=coth(m/2)>2.
Thus Z cannot equal 1 or -1: in the both-neutral case it is imaginary, and in a real-input case its real part has absolute value at least R>2.
The output beta is therefore defined, nonzero and different from one at every embedding.

Both-neutral inputs give |beta|=1.
If x is real and C(y)=i v, the actual radial value satisfies

    |log|beta|| <= log((aR+1)/(aR-1))
                   =2atanh(1/(aR)) <= m/a.               (CY2)

The first inequality follows directly by comparing ((aR+1)^2+b^2v^2)/((aR-1)^2+b^2v^2) with its value at v=0.
The second follows from convexity of atanh on [0,1), with atanh(0)=0 and 2atanh(1/R)=m.
When y is real, the corresponding bound is m/b.
The imaginary part of Z is nonzero in either real-input case, so beta is nonreal there; its modulus is different from one because Re Z is nonzero.
Hence this family is outside the real-or-circle output geometry of C865.

The two disjoint real-input events each have probability 2/d, and they are exactly the events of nonzero radial logarithm.
Thus k/D=4/d.
Every off-circle output conjugate is nonreal, and complex conjugation together with simultaneous inversion produces the four distinct values beta, conjugate(beta), beta^(-1) and conjugate(beta)^(-1).
Consequently k>=4 and the actual output degree obeys d<=D<=d(d-2).
Consequently the full archimedean quantity, at that actual degree, satisfies

    M_(2,arch)(beta)^2
       <=(2D^2/d)m^2(a^(-2)+b^(-2)).                     (CY3)

This upper bound alone suggests that very large a,b could compress the raw norm.
It is not a unit or all-place estimate for arbitrary weights.
If beta is an algebraic integer, the automorphism which inverts both x and y sends Z to -Z and beta to beta^(-1), so beta is then a unit.
The needed automorphism is the product of the actual Salem conjugations c_x and c_y fixing the respective pair and inverting every other pair, at the retained [C383 scope](Yin_C_G0383_v1.md#salem-kernel-class-population).
Here is the needed elementary construction directly.
For each original inverse pair i choose g in G sending its oriented root to the positive real root alpha, and set c_i=g^(-1)c g, where c is ordinary complex conjugation on L in the chosen embedding.
Ordinary c fixes the real inverse pair and inverts every neutral root, so c_i fixes pair i pointwise and inverts every other pair.
The action on all roots determines an automorphism of the splitting field, so the construction is independent of the choice of g and all these c_i commute.
Thus c_i c_j inverts exactly pairs i,j, and the required two-coordinate and later selected-coordinate sign actions are actual automorphisms.
The following argument bounds both weights whenever this exact integrality condition holds.

#### Four-sign averages and the ordinary integer norm

Assume beta is an algebraic integer.
Since beta-1 is a nonzero algebraic integer, its ordinary norm in L is a nonzero integer.
Uniform averaging over G=Gal(L/Q), denoted E_G, and beta-1=2/(Z-1) give

    E_G log|Z-1|<=log 2.                                 (CY4)

For each embedding, compose on its target side with the two actual conjugate complex conjugations fixing the image pairs of x and y.
On these two coordinates their action independently inverts x and y, producing four equally weighted sign choices for their Cayley values.
Equivalently this is averaging over a four-element action on each ordered-pair orbit; no full symmetric Galois group or independence of random phases is assumed.

When both roots are neutral, write C(x)=i u and C(y)=i v with real u,v.
The average over the four signs is

    (1/4)log{[1+(au+bv)^2][1+(au-bv)^2]}
       >=(1/2)log^+(2a|u|).                             (CY5)

For completeness, with A=au and B=bv, the product equals

    (1+A^2+B^2)^2-4A^2B^2.

As a function of B^2>=0 its minimum is (1+A^2)^2 when A^2<=1, and 4A^2 when A^2>=1.
In both cases it is at least max(1,4A^2), which proves CY5.
The same inequality holds with a|u| replaced by b|v|.

If x is real, put A=aR>2 and B=bv.
The corresponding four-sign average is

    (1/4)log{[(A-1)^2+B^2][(A+1)^2+B^2]} >=0,           (CY6)

because the product is at least (A^2-1)^2>1.
The same conclusion holds when y is real.
Thus no omitted real-input block contributes a negative offset to CY5.

#### A fixed positive source-angle proportion bounds the weights

The only distribution input here is the already accepted [Pri11-U001 Theorem 3.1 interface](../audits/literature/Pri11/Yin_U001.md#pri11-u001), with the statement and original-proof inspection limits retained in C865.
Define globally on C

    A(z)=min(1,max(0,Re z+1/2)),
    B(z)=min(1,max(0,e+1-|z|)),
    psi(z)=A(z)B(z).

Each factor lies in [0,1] and is 1-Lipschitz, so psi is 2-Lipschitz and is supported in the disk of radius e+1.
On the unit circle B=1 and A(z)+A(-z)=1, so the normalized circle mean of psi is 1/2.
All original roots have modulus at most e because m<=1.
Since M(P_alpha)=exp(m)<=e<d, the accepted discrepancy estimate gives

    (1/d)sum_(z:P_alpha(z)=0) psi(z)
       >=1/2-epsilon_d,
    epsilon_d=2(2e+3)sqrt(log d/d).                       (CY7)

For a neutral root with psi(z)>0 one has Re z>-1/2, and hence

    |C(z)|^2=(1+Re z)/(1-Re z)>1/3>1/4.

The two nonneutral original roots contribute at most 2/d to the average in CY7.
The fraction of G for which x is neutral and |C(x)|>=1/2 is therefore at least 1/2-epsilon_d-2/d.
Removing the embeddings for which y is real costs at most a further 2/d.
Write p for the remaining both-neutral fraction; then

    p>=1/2-epsilon_d-4/d.                                (CY8)

For d>=10^6, log d/d is decreasing and elementary bounds e<3, log(10^6)<14 give epsilon_d<18sqrt(14/10^6)<0.068.
Consequently CY8 gives p>1/3 throughout that range.
The condition defining this fraction is invariant under the four sign changes used in CY5.
Since a>=1, CY5 is at least (1/2)log a on these blocks, and CY6 and the remaining neutral blocks are nonnegative.
Together with CY4 this proves

    log 2 >= (p/2)log a >= (1/6)log a,
    a<=64.                                               (CY9)

Interchanging x,y gives b<=64 as well.
Thus for every genuine Salem input with m<=1 and d>=10^6, integrality of the rationally weighted Cayley output with a,b>=1 requires both rational weights to lie in [1,64].
This is only a necessary condition: no weight pair in that square is asserted to produce an integer.
The bound is not claimed optimal.

#### Consequence and surviving scope

The candidate has exact modulus-one behavior on neutral pairs and nonreal off-circle behavior at the remaining embeddings, with all actual field and radial costs retained in CY1--CY3.
Nevertheless the arbitrarily large weights suggested by CY3 cannot meet its unit gate on the stated large-degree, bounded-measure sources.
Even for weights within the necessary range, every nontorsion unit output obeys BA7 with r=2 and therefore has diverging raw M_2 as d tends to infinity.
No finite-place cost may be discarded when the candidate is not integral.
The inequalities do not establish that all coupled units are two-variable torus-preserving outputs, and do not resolve the unrestricted G0001 objective.

#### Arbitrarily many positive Cayley weights still have bounded usable arity

The same norm calculation controls the positive-weight Cayley family even when its number of input pairs is allowed to grow.
Choose 1<=r<=t oriented roots u_1,...,u_r from distinct inverse pairs and rational weights a_i>=1, and put

    Z=sum_(i=1)^r a_i C(u_i),
    beta=(Z+1)/(Z-1).                                    (CY10)

Assume d>=10^6, 0<m<log(9/8), and that beta is an algebraic integer.
As before Z avoids 1 and -1 at every embedding: its real part is either zero or exactly one of the numbers +/-a_i R, where R=coth(m/2)>2.
Thus beta is defined and beta-1 is nonzero.
The integer-norm proof of CY4 applies without change.
On an all-neutral embedding one has |Z-1|>=1.
When an input pair is real, |Z-1|>=R-1>1; this event has probability exactly 2r/d.
It follows that

    (2r/d)log(R-1)<=log 2.                               (CY11)

If r>=d/8, this gives R<=17 and hence m>=log(9/8), contrary to the assumption.
Therefore r<d/8.
In particular at least one original inverse pair is unused.

Fix such an unused pair j_0.
For each used pair i, the product c_i c_(j_0) of actual Salem conjugations inverts the i-th used root and fixes all the other used roots.
These commuting involutions generate a group whose action on the selected tuple is the full 2^r sign group in Cayley coordinates.
Every right coset in G therefore gives an equally weighted independent choice of signs for the r selected Cayley values.
This is an actual finite Galois action, not a probabilistic independence hypothesis about root angles.
Inverting all selected roots is also an actual automorphism, so it sends beta to beta^(-1).
Consequently the assumed integrality makes beta a unit in the current small-m domain.
At an embedding with a real selected root, Re Z is nonzero, so |beta|!=1 and beta is nontorsion.

Let N_good count the used roots which are neutral and satisfy |C(u_i)|>=1/2 at an embedding.
Applying CY7 separately to the uniform marginal of each selected root gives

    E_G N_good >= r(1/2-epsilon_d-2/d).

The event that some selected input is real has probability 2r/d and N_good<=r everywhere.
Consequently

    E_G[1_(all neutral) N_good]
      >=r(1/2-epsilon_d-2/d-2r/d)
      >r(1/4-epsilon_d-2/d) >=r/6,                       (CY12)

where d>=10^6 and the explicit epsilon_d<0.068 from CY7 justify the final inequality.
Let E denote the all-neutral event with N_good>=r/12.
Outside E the random variable 1_(all neutral)N_good is at most r/12, while everywhere it is at most r.
Thus CY12 implies P_G(E)>=1/12.
The event E and the value N_good are constant on each full-sign coset.

On an all-neutral coset write C(u_i)=i v_i, v_i real, and let independent signs epsilon_i range uniformly over {1,-1}.
Set S=sum_i epsilon_i a_i v_i and V=sum_i a_i^2 v_i^2.
Direct expansion gives

    E_sign S^2=V,
    E_sign S^4=sum_i a_i^4 v_i^4
                 +6sum_(i<j)a_i^2v_i^2 a_j^2v_j^2
               <=3V^2.

For completeness, put Y=S^2 and A={Y>=V/2}.
The contribution of A^c to E_sign Y is at most V/2, so E_sign[Y 1_A]>=V/2.
Cauchy--Schwarz gives (V/2)^2<=E_sign(Y^2) P_sign(A)<=3V^2 P_sign(A), and therefore P_sign(A)>=1/12.
No external probabilistic inequality is needed beyond this calculation.
It follows that

    E_sign log|Z-1|=(1/2)E_sign log(1+S^2)
       >=(1/24)log(1+V/2).

On E, the weights a_i>=1 and at least r/12 values |v_i|>=1/2 give V>=r/48.
All remaining neutral cosets and real-input cosets have nonnegative logarithms, as observed before CY11.
Averaging the last bound over the at least 1/12 fraction of cosets in E, and then using CY4, yields

    log 2 >= (1/288)log(1+r/96),
    r <= R_0 := 96(2^288-1).                             (CY13)

The constant is deliberately coarse and no sharpness is asserted.
It is independent of the original degree, source measure, rational weights and their denominators.

Now fix any C>0.
There cannot be a sequence of genuine Salem sources with m(alpha)->0 and outputs from CY10 satisfying the actual integrality condition and M_2(beta)<=C m(alpha).
If source degrees were bounded along an infinite subsequence, the elementary bounded-coefficient argument following BA8 would already preclude m(alpha)->0.
Otherwise source degrees tend to infinity after subsequence selection, the assumptions of CY10 eventually hold, and CY13 uniformly bounds r.
The unit and nontorsion conclusions proved above make BA7 applicable; uniformly over 1<=r<=R_0 its lower bound tends to infinity with d, contradicting M_2(beta)<=C m(alpha).
Thus allowing arbitrary positive rational weights and arbitrarily many selected root pairs does not supply the sought uniform raw-p2 compression through this Cayley-addition operation.
Changing the orientation of an input root changes the sign of its Cayley value, so the same conclusions cover arbitrary nonzero rational weights with |a_i|>=1 after reorientation.
The conclusion concerns this exact operation; weights of arbitrarily small absolute value, input-field-dependent coefficients, other coupled rational functions and general splitting-field units are not classified by it.

## Scope and review boundary

The complete fixed statement and argument comprise Parts A--C with N1--N2, S1--S7 and the full BA1--BA8 and CY1--CY13 arguments above.
Its own-degree, original-input, unit, finite-place, rational-coefficient and actual-orbit hypotheses are essential to the stated scope.
The methods exclude these precise raw-p2 compression constructions; they neither supply a useful coupled unit nor classify every unit in a Salem splitting field.
Arbitrary auxiliary coefficient fields or external radicals with unbounded additional degree are not covered by Part A's degree bound.
The actual-orbit modulus-one condition cannot be discarded: additional radial output on wholly neutral tuples would require its own support and norm accounting.
The fixed results and exact adopted evidence of v1 and v2 remain unchanged at their separate scopes.
No numerical experiment, polynomial enumeration, native computation or new source-proof audit is used.
The unrestricted [G0001 total-Mahler objective](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:50 |
| status | proved |
| reason | Adopt complete N1--N2, A--C/S1--S7 and BA1--BA8/CY1--CY13 after independent whole R1088 v3, including its independent recheck of every eventual arity branch. The exact actual-degree support bound excludes bounded raw-p2 compression for the stated slowly growing coupling class, and the full rational Cayley weight class with absolute weights at least one has the stated unit restrictions. No useful coupled unit, universal unit classification or total-Mahler gap is supplied; all prior versions and source/ancestor review limits retain their separate scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | All A--C/S1--S7: actual output degree and finite-place normalization, input-dependent functions, growing arity, common powers, two-variable and arbitrary-arity rational Cayley constructions and exact exclusions. |
| argument | [Complete argument](#argument) | All BA1--BA8 and CY1--CY13, including every BA8 domain branch, actual Galois sign actions, full integer norm, original-root discrepancy, sign moments and uniform sequence consequences. |
| dependency | [Numerical source interface](Yin_C_G0147_v5.md#reuse-and-source-scope) | Only the accepted Smy08 numerical statement and elementary conversion, not the cyclic-norm theorem; actual ancestor unknown/SELF relationships are retained. |
| dependency | [Salem conjugation interface](Yin_C_G0383_v1.md#salem-kernel-class-population) | Actual conjugates of complex conjugation, with the needed construction independently checked in this version; no whole ancestor review or upgrade of its SELF relationship. |
| support | [Smy08 numerical statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact constant and total-measure normalization at retained survey statement/applicability scope; no defective resultant mechanism or new original Dobrowolski audit. |
| support | [Pri11 original-root discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact Theorem 3.1/(3.2), actual original input and full-root distribution, displayed compact Lipschitz test and retained source-proof limits. |
| support | [Smy15 positive powers](../audits/literature/Smy15/Yin_U001.md#smy15-u001) | Only positive Salem powers preserve degree and field at the retained statement/displayed-proof scope. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v3.md#whole-coupled-output-finding) | Complete current statement and argument after the actual independent domain recheck, including source and ancestor limits and no G0001 completion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
