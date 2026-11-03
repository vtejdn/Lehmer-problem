---
author: Yin
---
# Actual trace-quotient residual norm income at every prime over two

Date: 2026-10-20T12:10.
Human author Yin.
This substantive v2 extends the [fixed totally ramified v1](Yin_C_G0191_v1.md#statement), whose proof and independent-review scope remain separate.
The entropy_attainment_bridge agent supplied the actual self-composition valuation mechanism, its periodic Hensel-lift extension and the maximal-order filtration count, and assembled the new arithmetic bound with the existing original polynomial return.
Root and that agent developed parallel residue-cluster proofs of the constant6/11; root supplied the weighted-A formulation and its simpler low-beta<1 split used below.
Both are contributors, not independent reviewers of this version.
The original-return identities are reused mathematics: entropy_attainment_bridge's earlier unbuffered-family formulas are retained in [L438](../ledger/Yin_L_G0438_v1.md#unbuffered-balanced-reassessment), and draft_inventory_later supplied the q=1 original-return specialization in the former D35 Section12, formulas52--54, fully retained in [this version's original-return proof](#exact-original-return).
That prior contribution prevents treating draft_inventory_later's checking of the reused return as an independent review of that portion, even though it did not contribute to this version's new cluster proof.
The complete new arithmetic theorem and its assembly with the old return require a separately scoped whole independent finding.
The proof uses the actual original trace quotients; abstract residual triples, including unit-g triples, do not satisfy that additional hypothesis automatically.
No numerical calculation, parameter scan or global existence theorem is a premise.

<a id="statement"></a>
## Exact theorem statement

Let P be a monic irreducible reciprocal nontorsion integer-unit polynomial with constant coefficient1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and let T be the actual monic irreducible integer trace polynomial, so

    P(z)=z^r T(z+z^(-1)), [K:F]=2, [F:Q]=r.

Assume F is totally real.
Use C_n(delta)=alpha^n+alpha^(-n), with C2(X)=X^2-2, C3(X)=X^3-3X and C5(X)=X^5-5X^3+5X, and define the ACTUAL nonzero integral quotients

    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.           (1)

There is no ramification, residue-degree, Galois, maximal-power-order or small-measure hypothesis.
If f=0, then a is totally positive and

    v_2(Norm_F(a))>=ceil(3r/11),
    v_2(abs(Norm_F(c)))>=ceil(2r/11),
    Res(P(z),P(z^2))
      >=2^(d+2ceil(3r/11))>=2^(14d/11).            (2)

If also e+s g=0 and g!=0 for s in{1,-1}, then

    v_2(abs(Norm_F(g)))>=ceil(6r/11),
    abs(Norm_F(g))>=2^(6r/11)>2^(r/2),
    abs(Norm_K(g))>=2^(6d/11).                     (3)

If F has only ONE prime over2, with arbitrary residue degree, the stronger conclusions are

    f=0 implies Norm_F(a)>=2^r,
       abs(Norm_F(c))>=2^(2r),
       Res(P(z),P(z^2))>=2^(2d);
    f=e+s g=0, g!=0 implies
       abs(Norm_F(g))>=2^(6r),
       abs(Norm_K(g))>=2^(6d).                    (4)

As in C178, an unramified2-prime excludes the complete residual system, including its r=1 case.
No f-only case is excluded merely because r=1.
Every norm is over the complete named field to Q.

For EVERY input in this domain, without assuming f=0, the unbuffered value

    Q_s=(e+s g)^2+f^2+g^2

satisfies

    Norm_F(Q_s)>=2^r, Norm_K(Q_s)>=2^d.            (5)

In the residual branch f=e+s g=0 these lower bounds strengthen to2^(12r/11) and2^(12d/11).
Section5 gives the exact integer original numerator, supplied denominator972000^2, ordinary degree30d and radial price30m(P).
This arithmetic gate does not provide a free original-root/Haar transfer or a uniform Mahler gap.

<a id="argument"></a>
## 1. Actual local factors and complete residue multiplicities

The accepted [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) gives the actual field degrees, nonzero integrality and phases in(1).
Membership in Z[delta] does not assert that this order is maximal.
In particular a=T(C2(delta))/2 is exact; an arbitrary positive integral element cannot replace it.

For every prime p of F over2 let L_p=F_p and normalize v_p to have value group Z.
Write

    e_p=v_p(2), f_p=[k_p:F_2],
    A_p=v_p(a), C_p=v_p(c), beta_p=A_p/e_p.

The accepted [local degree interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) retains sum_p e_p f_p=r and v_2=v_p/e_p.
The ordinary completion decomposition F tensor Q_2=product_p L_p gives

    T=product_p T_p in Q_2[X], deg(T_p)=e_p f_p,   (6)

where T_p is the minimal polynomial of delta in L_p.
Indeed the completion of Q[delta] at p is Q_2[delta]=L_p, and multiplication by delta on this factor has its degree-e_p f_p minimal polynomial.
The factors are monic integral over Z_2 and all their roots are integral.

Let phi_p be the minimal polynomial over F_2 of the residue of delta in k_p, and put h_p=deg(phi_p), a divisor of f_p.
Then

    T_p mod2=phi_p^(e_p f_p/h_p).                  (7)

To retain every multiplicity even for a nonmaximal power order, use multiplication by delta on O_(L_p), a free Z_2 lattice of rank e_p f_p.
Its characteristic polynomial is T_p.
The filtration of O_(L_p)/2O_(L_p) by maximal-ideal powers has e_p successive quotients, each one-dimensional over k_p.
On each quotient the operator is multiplication by delta_bar, whose F_2 characteristic polynomial is phi_p^(f_p/h_p).
Multiplication over the filtration proves(7).
Thus each geometric residue root of phi_p occurs among the roots of T_p exactly

    n_p=e_p f_p/h_p                               (8)

times.
This argument does not identify O_(L_p) with Z_2[delta].

Group the primes into clusters with a common phi_p.
Inside a cluster put h=deg(phi_p), m_p=f_p/h and n_p=e_p m_p.
Its contribution to r is h sum_p n_p.
Squaring permutes the roots of each irreducible phi, so a squared residue never moves to another cluster.

## 2. Periodic Hensel lifts and the self-factor contribution

For a prime in a cluster of degree h use F_h(X)=C_(2^h)(X)-X.
Modulo2 it is X^(2^h)-X with derivative-1.
The [accepted Con26e-U001 complete-field Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) supplies a unique eta_p in O_(L_p) with the same residue as delta and F_h(eta_p)=0.
Its simple-root hypotheses hold at delta.
The lift is algebraic and integral, since F_h is a monic integer polynomial.

One has delta!=eta_p: equality would give C_(2^h)(delta)=delta and hence alpha^(2^h)=alpha or alpha^(-1), contradicting nontorsion.
Therefore

    j_p=v_p(delta-eta_p) in Z_(>0),
    t_p=j_p/e_p,
    ell_p=v_2(C2(delta)-C2(eta_p))>t_p.             (9)

The strict inequality follows from the exact identity

    C2(delta)-C2(eta_p)
      =2eta_p(delta-eta_p)+(delta-eta_p)^2.

Both terms have valuation greater than t_p; cancellation only increases it.
An infinite ell_p causes no problem in the inequalities; the low-beta case below has a specified finite value.

The polynomial C2 commutes with C_(2^h), so C2(eta_p) is the unique periodic lift with residue delta_bar_p^2.
For any root delta_i of T_q having this residue, the image of eta_q is the same C2(eta_p), by simple-root uniqueness in a finite complete field containing both lifts.
Every embedding of L_q preserves its unique extended2-adic absolute value, and consequently

    v_2(delta_i-C2(eta_p))=t_q.                    (10)

By(7)--(8) there are exactly n_q such roots from each q in this cluster and none from other clusters.
A nonmatching factor C2(delta)-delta_i is a unit.
Each matching factor has valuation at least min(ell_p,t_q), exactly that value when the two arguments differ.
For q=p the valuation is exactly t_p because ell_p>t_p.
Factoring the ACTUAL T therefore gives

    1+beta_p=v_2(T(C2(delta)))
      >=m_p j_p
        +sum_(q!=p in cluster)n_q min(ell_p,t_q).  (11)

The first equality pays the actual division by2 in a.
Tied-factor cancellation may increase a term and is never discarded as an equality.
All local factors and all residue repetitions remain present.

## 3. The complete cluster estimate under f=0

Assume f=0.
At every p,

    5A_p=e_p+2C_p, beta_p>=1/5.                   (12)

In a fixed cluster, if every beta_p>=1, its weighted average is at least1 and hence at least3/11.
Otherwise choose p with beta_p<1.
The self contribution m_p j_p in(11) is a positive integer smaller than2, so

    m_p=j_p=1, n_p=e_p, t_p=1/e_p.

Since A_p is positive integral and A_p<e_p, one has e_p>=2.
The two terms of the difference in(9) have valuations at least1+1/e_p and exactly2/e_p, so the latter is the unique smaller value and

    ell_p=2/e_p.                                  (13)

For q!=p its contribution in(11) is at least

    min(2n_q/e_p,m_q j_q)>=min(2n_q/e_p,1).

The self contribution is exactly1, so the sum of the other contributions is beta_p<1.
Every such q must have n_q<e_p/2.
Since e_q<=n_q and j_q>=1, it follows that

    t_q>=1/e_q>2/e_p=ell_p.

Thus every q contribution is exact, without tied cancellation.
With R=sum_(q!=p)n_q one obtains

    beta_p=2R/e_p, R>=e_p/10.                     (14)

The second inequality uses(12), so R is nonzero.
At a q!=p, its own matching factors contribute m_q j_q>=1.
The factors from p contribute exactly n_p t_p=1, because ell_q>t_q>t_p.
Every further contribution is nonnegative.
Equation(11) applied at q therefore gives beta_q>=1, proving uniqueness of the low-beta prime in this cluster.
Consequently

    sum_q n_q beta_q
      >=e_p beta_p+R=3R
      >=(3/11)(e_p+R)=(3/11)sum_q n_q.             (15)

The middle inequality is exactly e_p<=10R.
Together with the no-low-beta case, this covers every cluster.
Multiplying by its degree h and summing over ALL clusters proves

    sum_(p|2) f_p A_p>=3r/11,
    sum_(p|2) f_p C_p
      =(5 sum_(p|2) f_p A_p-r)/2>=2r/11.          (16)

These are complete original-field norm weights, not a bound inferred from one good prime.
Both norm exponents are integers, giving the ceilings in(2).
The nonzero integral a is totally positive under f=0, so Norm_F(a)>0.
The exact original relation P(alpha^2)=2alpha^d a and Norm_K(alpha)=1 give

    Res(P(z),P(z^2))=2^d Norm_F(a)^2,              (17)

with the full quadratic extension multiplicity.
This proves the remainder of(2).

If there is only one prime over2, the self-factor equality is beta_p=m_p j_p-1.
It is an integer and is positive under f=0, so beta_p>=1.
Thus A_p>=e_p and C_p>=2e_p; multiplying by f_p proves the f-only part of(4), without assuming f_p=1 or h_p=f_p.

## 4. Full residual norm and the unbuffered arithmetic gate

Now add e+s g=0 and g!=0.
The accepted [C178 exact identity](Yin_C_G0178_v1.md#statement) gives G_p=v_p(g)=3C_p at every prime over2.
It applies to the actual nonzero integral triple in the totally real F.
It is NOT invoked under f=0 alone.
Equation(16) yields

    v_2(abs(Norm_F(g)))
      =sum_(p|2)f_p G_p=3sum_(p|2)f_p C_p>=6r/11. (18)

All other finite-prime valuations are nonnegative; this proves(3), including its ceiling.
The original quadratic tower gives Norm_K(g)=Norm_F(g)^2.
In the one-prime case the stronger bound is sum f_p G_p>=6e_p f_p=6r, proving(4).
The unramified exception, including r=1 for the full residual system, is exactly C178's separate exclusion.

For arbitrary e,f,g from(1) put x=e+s g.
The [C153v2 pair exclusions](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) exclude f=g=0 and e=g=0 over this totally real trace field.
They exclude a sole nonzero x, a sole nonzero f and the all-zero case.
If at least two of x,f,g are nonzero, select that pair in F once.
At every real embedding, Q_s is at least twice the absolute product of that pair.
Multiplication over all r embeddings gives Norm_F(Q_s)>=2^r, since both nonzero integral values have nonzero integer norms.
If g is the sole nonzero value, then x=f=0 and(3) gives

    Norm_F(Q_s)=abs(Norm_F(g))^2>=2^(12r/11)>2^r.

The complete K-norm is the square of the F-norm in both cases, proving(5) and its residual improvement.
The arbitrary abstract residual domain is not substituted for the actual self-composition hypothesis at this step.

<a id="exact-original-return"></a>
## 5. Exact integer numerator and all original logarithmic costs

This section reuses the earlier unbuffered-family numerator and q=1 specialization identified in the contribution paragraph, applying the new arithmetic floor without claiming a new construction of those original-return identities.
Use the unreduced polynomials of [C153v2](Yin_C_G0153_v2.md#two-label-original-norms-and-costs):

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3.

Their degrees are6d,10d,15d and their endpoint coefficients are1,11,7.
With L=972000 put

    A_s=[13500z^(9d/2)H23+32sH35]^2
         +1215^2 z^(5d)H25^2+32^2 H35^2,
    B_s=z^(-15d)A_s/L^2.                          (19)

All exponents are integral because d is even.
The integer reciprocal numerator has exact degree30d and leading and constant coefficient100352 for either sign: only the H35 terms reach either endpoint, so cancellation is impossible there.
L^2 is the supplied denominator; leastness is not asserted.
On the circle put

    E=-z^(-3d)H23/72, F_0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375.

These functions are real by reciprocity.
The exact original phases give E(alpha)=e, F_0(alpha)=f and G(alpha)=g, and therefore

    B_s=(E+sG)^2+F_0^2+G^2 on the circle,
    B_s(alpha)=Q_s,
    Norm_K(B_s(alpha))=Norm_F(Q_s)^2
      =Res(P,A_s)/L^(2d)>=2^d.                   (20)

The centering monomial has norm1 and the resultant is positive.
The last lower bound strengthens to2^(12d/11) in the residual branch.

Let M_s=sup_(|z|=1) B_s(z)>0 and m=m(P).
The nonzero numerator has finitely many finite-order circle zeros, so log B_s is integrable for normalized Haar probability mu, with

    integral log B_s dmu=m(A_s)-2log L,
    (1/d)log Norm_K(B_s(alpha))
       <=log M_s+30m.                            (21)

The maximum principle for A_s inside and outside the circle gives abs(B_s(rho z))<=M_s exp(15d abs(log rho)).
Summing over all original roots uses sum_i abs(log abs(alpha_i))=2m, because alpha is a unit.
No Haar mean is substituted for M_s or for the original conjugate mean.
No F_0 component is discarded because f vanishes at original roots.
Thus the proved arithmetic gate retains a separate paid-transfer obligation.

<a id="inputs-and-boundaries"></a>
## Exact inputs, proof relationships and remaining scope

| Input | Exact scope used |
| --- | --- |
| [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual T and degrees, integral nonzero quotient values, phases and the two simultaneous-zero exclusions. |
| [C153v2 original polynomials](Yin_C_G0153_v2.md#two-label-original-norms-and-costs) | Every unreduced numerator, scalar, degree and reciprocal phase in(19)--(21). |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Accepted Theorem9.1 simple-root existence and uniqueness in the actual finite complete extensions; no new source-proof audit. |
| [The26b-U001](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Complete ramification/residue degree sum and valuation normalization at its recorded source scope. |
| [C178](Yin_C_G0178_v1.md#statement) | G_p=3C_p only after BOTH residual equations and g!=0; its separate unramified exclusion. |
| Elementary local linear algebra | Completion decomposition, unique extended absolute value, free maximal-order lattice and residue filtration; all new root counts and cluster estimates are proved above. |

All primes, residue orbits, matching roots and original norm weights are included.
No assumption that delta generates the full residue field, that Z[delta] is maximal, or that a generates F is made.
The one-prime consequence contains the earlier totally ramified theorem, but its new proof and enlarged scope need this version's own review.
A field realization of an abstract residual triple as some Salem trace field does not realize the three prescribed quotients(1).
This theorem excludes unit g in the actual residual class while leaving the independently studied abstract class unchanged.
It establishes the unbuffered arithmetic gate, not a uniform Mahler gap or completion of all D35/D36 logarithmic-transfer tasks.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:10 |
| status | open |
| reason | Register the complete all-prime actual-trace cluster argument, original unbuffered norm gate and all polynomial costs; v1 and its review retain their narrower fixed scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete all-prime theorem](#statement) | All actual totally real trace inputs, f-only income, complete residual6/11 bound, one-prime strengthening and unbuffered gate. |
| argument | [Entire five-section proof](#argument) | Local factors, Hensel lifts, exact clusters and weights, all norm towers, original numerator and logarithmic costs. |
| dependency | [Actual quotients and pair exclusions](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original domains, phases, nonzero integrality and actual two-label guards. |
| dependency | [Original defect polynomials](Yin_C_G0153_v2.md#two-label-original-norms-and-costs) | Exact numerators, scalars and degrees used for the original return. |
| dependency | [Hensel input](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Periodic residue lifts and uniqueness in finite complete fields. |
| dependency | [Local degree interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Sum e_p f_p=r and actual valuation normalization, without expanding source-proof scope. |
| dependency | [Exact residual valuation](Yin_C_G0178_v1.md#statement) | G_p=3C_p with the complete residual hypotheses, and the unramified exception. |
| support | [Inputs and contribution boundaries](#inputs-and-boundaries) | Parallel contributors, independently needed v2 review, no global-existence premise and no unpaid transfer. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:24 |
| status | proved |
| authority | Internal adoption within Yin's selected actual-trace arithmetic and unbuffered-return inquiries. |
| reason | Adopt the complete all-prime C191v2 through whole R468. All actual original trace inputs now satisfy the unbuffered norm gate, with the full residual exponent6/11, original quotient normalization and all degree/scalar/radial costs retained. R467's independent arithmetic scope and author-return scope stay distinct; the abstract unit residuals and the unpaid logarithmic transfer remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete all-prime theorem](#statement) | All actual totally real trace inputs, f-only income, complete residual6/11 bound, one-prime strengthening and unbuffered gate. |
| argument | [Entire five-section proof](#argument) | Local factors, Hensel lifts, exact clusters and weights, all norm towers, original numerator and logarithmic costs. |
| dependency | [Actual quotients and pair exclusions](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original domains, phases, nonzero integrality and actual two-label guards. |
| dependency | [Original defect polynomials](Yin_C_G0153_v2.md#two-label-original-norms-and-costs) | Exact numerators, scalars and degrees used for the original return. |
| dependency | [Hensel input](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Periodic residue lifts and uniqueness in finite complete fields. |
| dependency | [Local degree interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Sum e_p f_p=r and actual valuation normalization, without expanding source-proof scope. |
| dependency | [Exact residual valuation](Yin_C_G0178_v1.md#statement) | G_p=3C_p with the complete residual hypotheses, and the unramified exception. |
| support | [Inputs and contribution boundaries](#inputs-and-boundaries) | Parallel contributors, independently needed v2 review, no global-existence premise and no unpaid transfer. |
| review | [Whole all-prime and original-return finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Entire actual five-section theorem, all1--21 formulas, same original input, every prime/residue weight, source interface and full original return; no contributor is relabelled independent. |
| support | [Prior scoped arithmetic finding](../audits/reviews/Yin_R_G0467_v1.md#all-prime-trace-arithmetic-finding) | Independently checked new Sections1--4 only; its separate original-return author finding is not promoted to independent review. |

