---
author: Yin
---
# Squarefree dyadic residual representatives and original Mahler costs

Date: 2026-10-20T13:03.
Human author Yin.
Root supplied the squarefree-modulo-two candidate, the local valuation alternatives, the stronger norm and weighted-coefficient comparison, and the explicit cubic test.
The entropy_attainment_bridge agent checked the full argument and supplied the unramified-lift proof using the accepted maximal-order filtration, together with the exact original-field and small-measure boundaries.
Both are contributors; this complete candidate awaits a separately organized independent review.
The proof was developed in the newly allocated D37 on2026-10-20; that reused address does not inherit the earlier abstract-singleton draft or its review.
The general integer-representative scope below isolates the part of the proof independent of canonical degree; the degree-below-r corollary is explicitly canonical.
No numerical computation, parameter scan, new source acquisition or assertion of a minimal/first-known comparison polynomial is made.
The separate C194 linear/quadratic account and C195 rational regularizer are not modified.

<a id="statement"></a>
<a id="squarefree-canonical-statement"></a>
## Exact original domain and conclusion

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

<a id="argument"></a>
<a id="squarefree-canonical-reuse"></a>
## Existing exact inputs and the canonical integer representative

The [C153v2 original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies the original fields, nonzero quotients and integrality.
The residue-cluster proof and normalized self-factor inequality are the actual accepted [C191v2 Sections1--3](Yin_C_G0191_v2.md#argument), with the [whole independent R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding).
The present author contributed to C191 and reuses that independent finding, rather than claiming an independent reproof of its own upstream work.
The [C178 complete residual calculation](Yin_C_G0178_v1.md#statement) gives the local identities and excludes an unramified2-prime.
Its hypotheses include both equations in(SF1); the identity for g is not borrowed under f=0 alone.
The existing C194 linear mechanism is a related narrower comparison; neither its pending successor nor a mutable draft is a premise of the argument here.

For explicit coefficient-order scope, C_p(X) is congruent to X^p modulo p.
Hence T(C_p(X)) is congruent to T(X)^p modulo p, and can be written T(X)^p+pW(X) with W in Z[X].
Monic division by T gives theta_p=rem_T W in Z[X].
A further monic division gives G_can in Z[X] and degree below r, with G_can(delta)=g.
Any other integer representative Gbar of g differs from G_can by a multiple of the monic T in Z[X].
This establishes the canonical specialization without restricting the general Gbar in(SF1) or claiming Z[delta]=O_F.

<a id="squarefree-canonical-cluster-support"></a>
## 1. Every residue cluster supports a simple root of Gbar

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
## 2. The periodic lift really lies in an unramified degree-h subfield

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
## 3. All local cancellation cases and the stronger norm

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
## 4. Original coefficient expense and a cubic comparison

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
Therefore

    0<integral log Q(z+z^(-1))^2 dmu
         =2m(H_Q)=2log lambda<log2.              (SF13)

This is a noncyclotomic favorable-Haar comparison proved by exact intervals, not a numerical calculation or a minimality claim.
If Gbar=+/-Q is the actual canonical residual, then w=3<r, so r>=4 and(SF3) gives m(P)>=(r/3)log(64/17)>log2.
Thus the comparison cannot occur in the original residual small-m(P) class, despite its favorable Haar value.
The proof does not exclude its realization at larger original m(P), and H_Q itself is not substituted for the original P.

<a id="squarefree-canonical-inputs"></a>
## Inputs and remaining boundary

| Input | Exact scope |
| --- | --- |
| [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual original reciprocal and trace fields, quotient values and nonzero integrality. |
| [C178](Yin_C_G0178_v1.md#statement) | Full residual local identities G_p=3C_p, beta formula and exclusion of every unramified2-prime. |
| [C191v2](Yin_C_G0191_v2.md#argument) and [R468](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Per-cluster income, complete maximal-order filtration and self-factor inequality; upstream author relationship is disclosed. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Existing simple-root Hensel theorem in the actual complete field F_p; no new proof audit or extra local-field existence theorem. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Local degree and original normalized valuation interfaces, at the unit's retained statement/applicability scope. |
| Elementary monic division and exact real intervals | Canonical integer coefficients, the complete coefficient expense and the cubic comparison. |

The nonzero squarefree reduction is an additional hypothesis on the chosen actual integer representative.
The proof neither assumes it for every representative nor supplies a way to replace a nonsquarefree canonical remainder without changing the chosen polynomial, its degree and its coefficient cost.
Squarefreeness of a higher-degree representative is not silently transferred to the canonical remainder.
The branch A_G>32 remains governed only by the exact coefficient inequality(SF3).
No general canonical-Haar exclusion, automatic residual impossibility, uniform unrestricted Mahler gap or completion of D35/D36 is asserted.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:03 |
| status | open |
| reason | Register the complete all-degree squarefree-modulo-two criterion for actual integer representatives, with its full original norm and coefficient expense, the separate canonical degree corollary and the exact cubic comparison. This is a complete candidate awaiting whole noncontributor review, not an adopted general canonical-Haar exclusion or unrestricted gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete representative and canonical criterion](#statement) | All original actual residual inputs, arbitrary integer representatives with nonzero squarefree mod2 reduction, constant branch, complete norm and separate canonical degree/weighted-coefficient consequences. |
| argument | [Complete SF1--SF13 proof](#argument) | Per-cluster support, degree-h unramified lift from the maximal-order filtration, every local cancellation case, full norm weights, inverse-pair coefficient expense and exact cubic real intervals. |
| dependency | [Actual trace-quotient interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Exact original K/F/T and nonzero integral a,b,c; no arbitrary abstract triple substitution. |
| dependency | [Full residual local identities](Yin_C_G0178_v1.md#statement) | G_p=3C_p, beta formula and unramified2-prime impossibility under both residual equations. |
| dependency | [Complete actual residue-cluster argument](Yin_C_G0191_v2.md#argument) | Its per-cluster positive income, maximal-order filtration, periodic simple-root lift and normalized self-factor inequality; the field/filtration application to Q2(eta) is supplied in the new proof. |
| dependency | [Complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Exact U001 simple-root specialization in F_p, unit derivative and positive valuation; no new source proof audit. |
| dependency | [Local degree and valuations](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Exact U002 retained local-degree and original normalized valuation interfaces, not a new assumed unramified-field existence theorem. |
| support | [Whole upstream independent finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Independent review reused for the present author's upstream C191 contribution; not a review of this new squarefree theorem. |
| support | [Exact input and remaining scope](#squarefree-canonical-inputs) | Six input rows, joint contributions, integer versus canonical representatives, no numerical/source expansion and no unrestricted conclusion. |
