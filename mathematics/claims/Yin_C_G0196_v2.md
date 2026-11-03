---
author: Yin
---
# Forced dyadic multiplicities of actual residual representatives

Date: 2026-10-20T13:09.
Human author Yin.
This substantive v2 strengthens the [fixed v1 squarefree criterion](Yin_C_G0196_v1.md#statement), whose complete mathematical version remains unchanged.
Root supplied the new congruence obstruction, its exact multiplicity refinement, the degree-three shape and all-measure low-degree consequence.
The entropy_attainment_bridge agent checked that argument, supplied the explicit distinction between arbitrary integer representatives and the canonical one, and assembled the complete proof with the earlier valuation mechanism.
The prior SF1--SF13 argument was developed jointly by root and that agent; its unramified-lift filtration proof was supplied by the latter.
Both are contributors and neither is an independent reviewer.
The independent reviewer pointed to the existing Smy08 scalar-Jensen source interface for SF13; that is source declaration help, not a new proof contribution.
No numerical calculation, coefficient enumeration or new source acquisition is used.

<a id="statement"></a>
## Exact theorem statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, of degree d=2r and constant coefficient1.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), assume F totally real, and let T in Z[X] be the actual monic degree-r trace polynomial.
Thus P(z)=z^r T(z+z^(-1)) and [K:F]=2.
For p=2,3,5 put

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5,

where C_p(z+z^(-1))=z^p+z^(-p).
Assume the FULL actual residual system

    f=e+s g=0, g!=0, s in{1,-1}.                  (MF1)

The nonzero integral values a,b,c are the original trace quotients, not arbitrary integral elements.
Let R in Z[X] be ANY representative with R(delta)=g; no degree or leading-coefficient restriction is imposed on this general representative.
Write bars for reduction modulo2 and factor the nonconstant monic polynomial

    Tbar=product_phi phi^(N_phi)

over F_2 into distinct monic irreducible factors.
Set nu_phi=ord_phi Rbar, with nu_phi=infinity if Rbar=0.
Then

    N_phi>=2,
    nu_phi>=min{3,N_phi}>=2                       (MF2)

for every phi dividing Tbar.
If nu_phi<N_phi, its precise unsaturated value is

    nu_phi=3 ord_phi(theta_5 mod2)>0.             (MF3)

In particular NO integer representative R of g can have a nonzero squarefree reduction modulo2, at any original measure or degree.
The entire zero reduction is allowed by(MF2), and is not called squarefree.
A nonzero constant reduction is also excluded, since there is at least one phi dividing Tbar.

For the ACTUAL canonical representative

    G_can=rem_T(theta_5^3-2theta_3^5) in Z[X],
    w=deg G_can<r,

assume its reduction is nonzero.
Then at least one phi is unsaturated and w>=3.
If w=3, necessarily for some kappa in{0,1},

    G_can mod2=(X-kappa)^3,
    T mod2=(X-kappa)^r, r>=4,
    ord_(X-kappa)(theta_5 mod2)=1.                (MF4)

This is one residue cluster of the chosen generator, not a claim that F has only one prime above2 or that its full residue fields have degree1.
For every actual canonical G_can of degree at most2, its normalized Haar logarithm obeys

    I_can=integral log G_can(z+z^(-1))^2 dmu
                    >=(12/11)log2.               (MF5)

This holds at every original measure, not only when m(P)<log2.
The explicit cubic Q=X^3-4X-1 has squarefree reduction and its reciprocal pullback has0<2m(z^3 Q(z+z^(-1)))<log2.
It nevertheless cannot represent g in(MF1) by R=+/-Q at ANY original measure, even if R is not canonical.
No minimality or first-known status of this comparison polynomial is asserted.

The complete earlier SF1--SF13 valuation proof is preserved below, including its general integer-representative norm bound and canonical coefficient cost.
Its extra nonzero-squarefree hypothesis is now proved impossible for the actual residual system, so its conditional lower bounds are not presented as nonempty new arithmetic coverage.
The periodic-lift sublemma in that proof is independently useful without the squarefree-R premise: its lift eta generates an unramified degree-h local subfield for the actual residue degree h of delta.
No arbitrary-representative squarefreeness is silently transferred to a canonical remainder.
These results do not exclude all actual residual inputs, classify all higher canonical remainders, or prove an unrestricted Mahler gap.

<a id="argument"></a>
## Complete strengthened proof

<a id="dyadic-multiplicity-original-congruence"></a>
### 1. The exact integer representative congruence

C_p(X) is congruent to X^p modulo p, so T(C_p(X)) is congruent to T(X)^p modulo p.
Monic division by T therefore gives theta_p in Z[X].
In particular G_can belongs to Z[X] and has degree below r.
The polynomial R-(theta_5^3-2theta_3^5) vanishes at delta.
Since T is the minimal polynomial of delta and is monic, division in Z[X] has zero remainder and gives the coefficientwise congruence

    R congruent theta_5^3-2theta_3^5 modulo T,
    Rbar congruent theta_5bar^3 modulo Tbar.       (MF6)

This holds for every integer representative R, not merely the canonical one.
It would not follow from an arbitrary real-valued interpolation or from a rational representative after dropping its denominator.

<a id="dyadic-multiplicity-clusters"></a>
### 2. Every actual residue cluster and its full multiplicity

Use the exact local objects of [C191v2 Sections1--3](Yin_C_G0191_v2.md#argument).
For a prime p of F over2 let e_p,f_p be its ramification and residue degrees, h_p the degree of the minimal polynomial phi_p of delta_bar over F_2, and A_p=v_p(a), G_p=v_p(g).
The accepted maximal-order filtration gives

    T_p mod2=phi_p^(e_p f_p/h_p).

Consequently for a common phi of degree h its total exponent is

    N_phi=sum_(p in cluster) e_p f_p/h,
    r_phi=h N_phi=sum_(p in cluster)e_p f_p.

The [C178 full residual theorem](Yin_C_G0178_v1.md#statement) excludes every unramified2-prime, so e_p>=2 and hence N_phi>=2.
This needs both equations in(MF1), not f=0 alone.
The complete per-cluster estimate C191v2(15), together with C178's G_p=3C_p and5A_p=e_p+2C_p, gives

    sum_(p in cluster) f_p G_p
       =(3/2)(5 sum_(p in cluster)f_p A_p-r_phi)
       >=(6/11)r_phi>0.                          (MF7)

Thus some prime in EVERY cluster has G_p>0.
Its residue makes Rbar vanish at a root of phi, whence phi divides Rbar.
Reducing(MF6) modulo phi then shows that phi divides theta_5bar.
This is actual per-cluster support; a merely positive global norm exponent would not suffice.

<a id="dyadic-multiplicity-exact-shape"></a>
### 3. Exact saturated and unsaturated orders

Fix phi and put t_phi=ord_phi theta_5bar, allowing infinity when theta_5bar=0.
The preceding section gives t_phi>=1.
Equation(MF6) says that Rbar-theta_5bar^3 is divisible by phi^(N_phi), and therefore

    nu_phi>=min{3t_phi,N_phi}>=min{3,N_phi}.

This proves(MF2), including the identically zero Rbar branch.
If nu_phi<N_phi, the unequal-order rule for the phi-adic polynomial valuation gives nu_phi=3t_phi.
It is positive and divisible by3, proving(MF3); no bound is asserted above the saturation exponent in the tied case.

Since Tbar is monic of positive degree, it has at least one irreducible factor phi.
Every such factor divides a nonzero Rbar at least twice by(MF2).
Thus nonzero squarefree Rbar is impossible, and the constant nonzero reduction is impossible as well.
For a canonical nonzero G_can mod2, if every nu_phi>=N_phi then Tbar would divide G_can mod2.
That contradicts deg(G_can mod2)<=w<r=deg Tbar.
Hence an unsaturated phi exists; by(MF3) its contribution to the degree is at least3deg phi, so w>=3.

If w=3, this unsaturated contribution consumes the whole degree: deg phi=1, nu_phi=3, and deg(G_can mod2)=3.
Over F_2 the linear factor is X-kappa, and no scalar other than1 is available for its leading coefficient.
There can be no other cluster, because(MF2) would require another irreducible factor of positive degree in G_can mod2.
Thus G_can mod2=(X-kappa)^3 and Tbar=(X-kappa)^r with N_phi=r>3.
Equation(MF3) also gives t_phi=1, proving(MF4).
Multiple primes and residue degrees f_p>h_p=1 remain fully possible; the argument does not remove them.

<a id="dyadic-multiplicity-haar-boundary"></a>
### 4. Low canonical degree and the favorable cubic comparison

The nonzero g makes G_can a nonzero integer polynomial.
If it is a constant k, C191v2 gives |k|^r=|Norm_F g|>=2^(6r/11).
Thus the integer |k| is at least2 and I_can=2log|k|>=2log2>(12/11)log2.
This also deals with an even constant whose entire reduction is0; the constant branch is not excluded merely by assuming nonzero reduction.

For w>=1 let H_can(z)=z^w G_can(z+z^(-1)).
It is an integer polynomial of degree2w with leading and constant coefficient equal to the nonzero leading coefficient c_w of G_can.
The exact scalar Jensen interface in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) gives

    I_can=2m(H_can)>=2log|c_w|.

This includes all circle roots and their logarithmic integrability, with no division by the original d or r.
If I_can<(12/11)log2<2log2, integrality forces c_w=+/-1, so the reduction of G_can is nonzero and has degree w.
The preceding section then forces w>=3.
Its contrapositive proves(MF5) for every w<=2 and every original measure.
It does not classify the cubic repeated-factor shapes in(MF4) or give a general higher-degree Haar bound.

For Q=X^3-4X-1, the exact argument at(SF13) below proves the favorable interval0<2m(z^3Q(z+z^(-1)))<log2.
But Q mod2=(X+1)(X^2+X+1) is squarefree.
The general representative exclusion(MF2) therefore rules out R=+/-Q at every original measure and degree, with no canonical-degree premise needed for this nonexistence conclusion.
The earlier coefficient-only proof's small-measure restriction is genuinely strengthened here.

<a id="retained-squarefree-valuation-argument"></a>
## Preserved complete valuation mechanism and comparison

The following retains the complete mathematical SF1--SF13 argument of v1, with the integer/canonical scope distinction intact.
Its nonzero-squarefree-R hypothesis is impossible by the preceding theorem; the conditional norm and coefficient statements remain logically correct but supply no nonempty residual class.
The periodic unramified-lift argument itself uses no squarefree-R premise and remains a valid actual-input sublemma.
The exact real-root/Haar calculation for the independent comparison cubic also remains valid.
The final comparison wording below identifies precisely where the new main theorem goes beyond that earlier argument.

<a id="conditional-squarefree-statement"></a>
<a id="squarefree-canonical-statement"></a>
### Exact original domain and conclusion

Let P be monic irreducible reciprocal nontorsion in Z[z], of degree d=2r and constant coefficient1.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and assume that the actual trace field F is totally real.
Let T in Z[X] be the monic degree-r trace polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
For p=2,3,5 set C_p(delta)=alpha^p+alpha^(-p) and

    theta_p=rem_T(T(C_p(X)))/p,
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta),
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

The values a,b,c are the actual nonzero integral quotients of C153, not an arbitrary integral triple.
The C_p used here are X^2-2, X^3-3X, X^5-5X^3+5X.
Suppose for s in{1,-1} that

    f=e+s g=0, g!=0,
    Gbar in Z[X], g=Gbar(delta).                  (SF1)

Assume that the reduction of Gbar in F_2[X] is nonzero and squarefree, meaning gcd(Gbar mod2,Gbar' mod2)=1.
Degree drop modulo2 is permitted.
At this general stage Gbar is any actual integer representative of g; no bound on its degree and no monicity of Gbar are assumed.
Then at EVERY prime p of F above2,

    v_p(g)>=6v_p(2),
    abs(Norm_F g)>=2^(6r),
    abs(Norm_K g)>=2^(6d).                       (SF2)

All norms are over the complete named original field to Q.
There is no one-prime, residue-degree, local-Galois or maximal-power-order hypothesis.

A possible input necessarily has w=deg Gbar>=1.
Writing Gbar(X)=sum_(j=0)^w c_j X^j and A_G=sum_(j=0)^w |c_j|2^j gives

    m(P)>=(r/w)log(64/A_G).                       (SF3)

Here m(P) is TOTAL logarithmic Mahler measure of the original degree-d P.
For the canonical specialization, set G_can=rem_T(theta_5^3-2theta_3^5) in Z[X] and choose Gbar=G_can.
Then w<r, so A_G<=32 implies m(P)>log2, without a Haar-saving hypothesis.
This specialization retains the same nonzero squarefree reduction assumption.
The cubic Gbar=+/-(X^3-4X-1) has A_G=17 and squarefree reduction modulo2, so cannot be the canonical residual in(SF1) for an original input with m(P)<log2.
Its reciprocal pullback does have a positive Haar logarithm strictly below log2, as proved below; that comparison does not assert its original realization at any measure.

<a id="conditional-squarefree-argument"></a>
<a id="squarefree-canonical-reuse"></a>
### Existing exact inputs and the canonical integer representative

The [C153v2 original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies the original fields, nonzero quotients and integrality.
The residue-cluster proof and normalized self-factor inequality are the actual accepted [C191v2 Sections1--3](Yin_C_G0191_v2.md#argument), with the [whole independent R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding).
The present author contributed to C191 and reuses that independent finding, rather than claiming an independent reproof of its own upstream work.
The [C178 complete residual calculation](Yin_C_G0178_v1.md#statement) gives the local identities and excludes an unramified2-prime.
Its hypotheses include both equations in(SF1); the identity for g is not borrowed under f=0 alone.
The C194 linear mechanism is a related narrower comparison; no C194 statement or mutable draft is a premise of this argument.

For explicit coefficient-order scope, C_p(X) is congruent to X^p modulo p.
Hence T(C_p(X)) is congruent to T(X)^p modulo p, and can be written T(X)^p+pW(X) with W in Z[X].
Monic division by T gives theta_p=rem_T W in Z[X].
A further monic division gives G_can in Z[X] and degree below r, with G_can(delta)=g.
Any other integer representative Gbar of g differs from G_can by a multiple of the monic T in Z[X].
This establishes the canonical specialization without restricting the general Gbar in(SF1) or claiming Z[delta]=O_F.

<a id="squarefree-canonical-cluster-support"></a>
### 1. Every residue cluster supports a simple root of Gbar

For each p over2 normalize v_p to have value group Z and put

    e_p=v_p(2), f_p=[k_p:F_2],
    A_p=v_p(a), C_p=v_p(c), G_p=v_p(g),
    beta_p=A_p/e_p.

Let phi_p be the minimal polynomial of the residue of delta over F_2, and let h_p=deg phi_p, which divides f_p.
Group primes by the same phi_p as in C191v2.
The complete C178 identities and its unramified exclusion give

    5A_p=e_p+2C_p, G_p=3C_p,
    beta_p=1/5+2G_p/(15e_p), e_p>=2.              (SF4)

For a cluster phi of degree h, let r_phi=sum_(p in cluster)e_p f_p>0.
The per-cluster inequality C191v2(15), including its no-low-beta branch, is

    sum_(p in cluster) f_p A_p >=(3/11)r_phi.

Combining it with(SF4) in this SAME cluster gives

    sum_(p in cluster) f_p G_p >=(6/11)r_phi>0.    (SF5)

This is a proof-level per-cluster input, not an inference from the weaker global sum alone.
Thus G_p>0 for at least one prime of the cluster.
At that prime the residue of Gbar(delta) vanishes, so its residue minimal polynomial phi divides Gbar mod2.
Every other prime in this cluster has a residue conjugate satisfying the same phi, and therefore also G_p>0.
Squarefreeness now implies

    Gbar'(delta_bar_p)!=0,
    G_p=3C_p>=3                                  (SF6)

at every prime over2.
If Gbar were constant, its nonzero squarefree reduction would be1 and no phi could divide it; thus the possible-input case indeed has w>=1.
A polynomial whose entire reduction is0 is excluded by the stated squarefree hypothesis, rather than silently treated as squarefree.

<a id="squarefree-canonical-unramified-lift"></a>
### 2. The periodic lift really lies in an unramified degree-h subfield

For every positive integer n, C_n is the monic integer polynomial satisfying C_n(z+z^(-1))=z^n+z^(-n), as in C191v2.
Fix p, write h=h_p, and use

    F_h(X)=C_(2^h)(X)-X,
    F_h mod2=X^(2^h)-X.

The latter derivative is-1, so it is squarefree.
The accepted complete-field simple-root [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) gives the same unique eta_p in O_(F_p) as in C191v2, satisfying F_h(eta_p)=0 and eta_p mod p=delta mod p.
This application uses a unit derivative and a positive polynomial valuation, in the complete finite extension F_p.
Nontorsion gives delta!=eta_p by the exact C191 argument: equality would force alpha^(2^h)=alpha or alpha^(-1).
Set j_p=v_p(delta-eta_p), a finite positive integer.
The retained self-factor bound is

    beta_p >= m_p j_p-1,
    m_p=f_p/h_p in Z_(>0).                       (SF7)

Now put M_p=Q_2(eta_p), as an actual subfield of F_p, and let Q_eta be the monic minimal polynomial of eta_p over Q_2.
It is integral and divides the monic F_h in Z_2[X].
Indeed all roots of F_h are integral; the monic quotient has Q_2 coefficients integral over Z_2 and therefore belongs to Z_2[X].
Consequently Q_eta mod2 divides the squarefree X^(2^h)-X and is squarefree.

Apply exactly the maximal-order filtration argument in C191v2(7) to O_(M_p), now with generator eta_p.
If its ramification and residue degrees are e_M,f_M, then the residue minimal polynomial of eta_p is the same degree-h phi and

    Q_eta mod2=phi^(e_M f_M/h).

For clarity, multiplication by eta_p on O_(M_p) has characteristic polynomial Q_eta.
The filtration of O_(M_p)/2O_(M_p) has e_M successive copies of its residue field, and on each copy multiplication by the residue has characteristic polynomial phi^(f_M/h).
Their product is the displayed reduction, irrespective of the index of Z_2[eta_p] in O_(M_p).
Since h divides f_M and the reduction is squarefree,

    e_M=1, f_M=h, [M_p:Q_2]=h.                   (SF8)

This proves the needed unramified assertion without presupposing an unramified extension of a desired degree or identifying the original power order with the maximal order.
The local degree and restriction-of-valuation normalizations are those retained in [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001).
In particular every nonzero integral element of M_p has integer2-adic valuation and its v_p valuation is a multiple of e_p.
Since phi divides Gbar mod2, we conclude

    Gbar(eta_p)=0, or
    v_p(Gbar(eta_p))=e_p k_p for an integer k_p>=1.
                                                            (SF9)

This is the exact unramified-lift expense needed below; mere integrality of eta_p would not give(SF9).

<a id="squarefree-canonical-valuation"></a>
### 3. All local cancellation cases and the stronger norm

Suppress the prime subscripts and put K_eta=v_p(Gbar(eta)), allowing infinity when that value is0.
The simple derivative in(SF6) gives the exact Taylor-factor valuation

    v_p(Gbar(delta)-Gbar(eta))=j.                 (SF10)

Indeed divide the difference by delta-eta; its residue is Gbar'(eta_bar), a unit.
No higher-term cancellation changes that unit factor.

If K_eta is infinite or j<K_eta, the unequal-valuation rule gives G=j.
Then j=G>=3 by(SF6), while(SF4),(SF7) would imply

    G-1<=beta=1/5+2G/(15e)<=1/5+2G/15.

This is impossible, since the first side minus the last is(13/15)G-6/5>=7/5>0.
Thus Gbar(eta)!=0 and j>=K_eta=e k for some k>=1.
If j>K_eta, then G=e k and the integer strict inequality j>=e k+1 gives

    beta>=m j-1>=e k>=2k,
    beta=1/5+2k/15.

These are incompatible for k>=1.
The only remaining possibility is j=K_eta=e k; cancellation in Gbar(delta) is allowed and need not be bounded above.
Nevertheless(SF7) now gives

    beta>=m e k-1>=e-1>=1,
    G/e=(15beta-3)/2>=6.                         (SF11)

All primes are covered, including arbitrary residue degree f and arbitrary number of primes in a cluster.
Summing with the original norm weights yields

    v_2(abs(Norm_F g))=sum_(p|2) f_p G_p
          >=6 sum_(p|2)e_p f_p=6r.

The other finite-prime contributions are nonnegative because g is a nonzero algebraic integer.
The full tower Norm_K(g)=Norm_F(g)^2 and d=2r prove(SF2).
The resulting residual value Q_s=g^2 has Norm_F(Q_s)>=2^(12r) and Norm_K(Q_s)>=2^(12d); this is the complete residual branch, not a claim under f=0 alone.

<a id="squarefree-canonical-coefficient-cost"></a>
### 4. Original coefficient expense and a cubic comparison

For each of the r real trace embeddings delta_i, choose the root of z^2-delta_i z+1 with modulus rho_i>=1.
When |delta_i|<=2 both roots have modulus1; otherwise they are reciprocal real roots.
Thus |delta_i|<=rho_i+rho_i^(-1)<=2rho_i and

    sum_(i=1)^r log rho_i=m(P).

For the actual integer coefficients of Gbar,

    |Gbar(delta_i)|<=sum_(j=0)^w |c_j|2^j rho_i^j
                         <=A_G rho_i^w.

The complete product over all trace embeddings gives

    abs(Norm_F g)<=A_G^r exp(w m(P)).             (SF12)

Combining with(SF2) and dividing by w>0 proves(SF3).
For a general representative, inequality(SF3) retains its actual w and A_G; w<r is not assumed.
For the canonical choice Gbar=G_can, if A_G<=32 then log(64/A_G)>=log2 and r/w>1 because its degree is below r.
Consequently m(P)>log2 in that canonical subclass, with no useful-Haar premise or omitted inverse pair.
For A_G>32, or for a general representative of larger degree, the exact inequality(SF3) remains valid but need not exclude the desired small-measure range.

For the explicit comparison set Q(X)=X^3-4X-1.
Its weighted coefficient size is A_Q=8+8+1=17, and

    Q mod2=X^3+1=(X+1)(X^2+X+1)

is squarefree, since its derivative is X^2 and its constant coefficient is1.
The three exact sign intervals for its roots are(-2,-1),(-1,0),(2,3/sqrt2):
Q(-2)=-1, Q(-1)=2, Q(0)=-1, Q(2)=-1 and Q(3/sqrt2)=3/(2sqrt2)-1>0.
These disjoint intervals account for all three cubic roots.
Its reciprocal pullback is

    H_Q(z)=z^3 Q(z+z^(-1))
          =z^6-z^4-z^3-z^2+1.

The first two trace roots each give a unit-circle inverse pair.
The third is y in(2,3/sqrt2), giving a real pair lambda,lambda^(-1) with1<lambda<sqrt2, because rho+rho^(-1) is strictly increasing for rho>1.
The exact scalar Jensen/root-product convention is the existing [Smy08-U001 height-normalization interface](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), including integrable circle zeros.
Therefore

    0<integral log Q(z+z^(-1))^2 dmu
         =2m(H_Q)=2log lambda<log2.              (SF13)

This is a noncyclotomic favorable-Haar comparison proved by exact intervals, not a numerical calculation or a minimality claim.
If Gbar=+/-Q is the actual canonical residual, then w=3<r, so r>=4 and(SF3) gives m(P)>=(r/3)log(64/17)>log2.
Thus the comparison cannot occur in the original residual small-m(P) class, despite its favorable Haar value.
This valuation-and-coefficient argument alone did not exclude its realization at larger original m(P).
The stronger congruence argument in the main proof now excludes that realization at every measure; H_Q itself is never substituted for the original P.

<a id="squarefree-canonical-inputs"></a>
### Inputs and remaining boundary

| Input | Exact scope |
| --- | --- |
| [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual original reciprocal and trace fields, quotient values and nonzero integrality. |
| [C178](Yin_C_G0178_v1.md#statement) | Full residual local identities G_p=3C_p, beta formula and exclusion of every unramified2-prime. |
| [C191v2](Yin_C_G0191_v2.md#argument) and [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Per-cluster income, complete maximal-order filtration and self-factor inequality; upstream author relationship is disclosed. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Existing simple-root Hensel theorem in the actual complete field F_p; no new proof audit or extra local-field existence theorem. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Local degree and original normalized valuation interfaces, at the unit's retained statement/applicability scope. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Jensen/root products and integrable circle zeros in SF13, at the existing source-inspection scope. |
| Elementary monic division and exact real intervals | Canonical integer coefficients, the complete coefficient expense and the cubic comparison. |

The nonzero squarefree reduction is an additional hypothesis on the chosen actual integer representative.
The proof neither assumes it for every representative nor supplies a way to replace a nonsquarefree canonical remainder without changing the chosen polynomial, its degree and its coefficient cost.
Squarefreeness of a higher-degree representative is not silently transferred to the canonical remainder.
The branch A_G>32 remains governed only by the exact coefficient inequality(SF3).
This conditional argument supplies no unrestricted Mahler gap or completion of D35/D36.
Its former nonexistence boundary is strengthened precisely by the main congruence theorem, not by retroactively upgrading the old valuation proof.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:09 |
| status | open |
| reason | Register the substantively stronger actual-representative congruence obstruction, all dyadic multiplicities and the exact canonical degree-three shape, while preserving v1 and its complete valuation mechanism. Whole noncontributor review is required before adoption; no general higher-degree Haar or unrestricted gap conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened theorem](#statement) | Every actual residual integer representative, zero and constant reductions, saturated/unsaturated multiplicities, canonical degree and cubic shape, all-measure low-degree Haar exclusion and favorable nonrealizable comparison. |
| argument | [Complete new proof and retained mechanism](#argument) | MF1--MF7 strengthened proof plus every SF1--SF13 argument and its explicit vacuous-conditional interpretation. |
| dependency | [Actual trace-quotient interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original K/F/T and nonzero integral quotient values; exact integer representative congruence is proved locally. |
| dependency | [Full residual local identities](Yin_C_G0178_v1.md#statement) | G_p=3C_p, beta formula and every unramified2-prime exclusion, under both residual equations. |
| dependency | [Complete actual residue clusters](Yin_C_G0191_v2.md#argument) | Per-cluster positive income, complete exponent sum and maximal-order filtration; no global-income substitution. |
| dependency | [Complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Exact U001 simple-root statement for the retained periodic-lift sublemma; no new source proof audit. |
| dependency | [Local degrees and valuations](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact U002 original normalized degree/valuation interfaces used in both accounts. |
| dependency | [Scalar Jensen and circle zeros](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact U001 height-normalization subsection: full polynomial root-product identity and integrable circle zeros for MF5 and SF13. |
| support | [Whole upstream independent finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Independent review reused for the authors' C191 contribution, not a new review of this theorem. |
| support | [Fixed predecessor](Yin_C_G0196_v1.md#argument) | Complete earlier SF1--SF13 version preserved physically; the stronger main theorem makes its squarefree residual hypothesis empty. |
| support | [Retained input boundaries](#squarefree-canonical-inputs) | Actual general versus canonical scope, seven input rows including scalar Jensen, joint contributions and no numerical/source expansion. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:17 |
| status | proved |
| authority | Internal adoption within Yin's selected actual original residual and transfer inquiries. |
| reason | Adopt the complete actual multiplicity theorem through whole R473. Every integer representative has the stated repeated dyadic support, excluding nonzero squarefree reduction at every measure; canonical saturation and degree-three necessary shape retain their precise scope. The preserved older squarefree valuation condition is empty, not nonempty improved coverage. The retained periodic-lift lemma and independent cubic comparison remain valid; later C5 graph and higher-adic extensions are not adopted here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete strengthened theorem](#statement) | Every actual residual integer representative, zero and constant reductions, saturated/unsaturated multiplicities, canonical degree and cubic shape, all-measure low-degree Haar exclusion and favorable nonrealizable comparison. |
| argument | [Complete new proof and retained mechanism](#argument) | MF1--MF7 strengthened proof plus every SF1--SF13 argument and its explicit vacuous-conditional interpretation. |
| dependency | [Actual trace-quotient interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original K/F/T and nonzero integral quotient values; exact integer representative congruence is proved locally. |
| dependency | [Full residual local identities](Yin_C_G0178_v1.md#statement) | G_p=3C_p, beta formula and every unramified2-prime exclusion, under both residual equations. |
| dependency | [Complete actual residue clusters](Yin_C_G0191_v2.md#argument) | Per-cluster positive income, complete exponent sum and maximal-order filtration; no global-income substitution. |
| dependency | [Complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Exact U001 simple-root statement for the retained periodic-lift sublemma; no new source proof audit. |
| dependency | [Local degrees and valuations](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact U002 original normalized degree/valuation interfaces used in both accounts. |
| dependency | [Scalar Jensen and circle zeros](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact U001 height-normalization subsection: full polynomial root-product identity and integrable circle zeros for MF5 and SF13. |
| support | [Whole upstream independent finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Independent review reused for the authors' C191 contribution, not a new review of this theorem. |
| support | [Fixed predecessor](Yin_C_G0196_v1.md#argument) | Complete earlier SF1--SF13 version preserved physically; the stronger main theorem makes its squarefree residual hypothesis empty. |
| support | [Retained input boundaries](#squarefree-canonical-inputs) | Actual general versus canonical scope, seven input rows including scalar Jensen, joint contributions and no numerical/source expansion. |
| review | [Whole independent multiplicity finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Entire actual MF1--MF7 and SF1--SF13, all inputs and representative/canonical/zero-reduction boundaries, explicit vacuous conditional status and complete source interfaces; upstream author overlap is disclosed and independent R468 reused. |

