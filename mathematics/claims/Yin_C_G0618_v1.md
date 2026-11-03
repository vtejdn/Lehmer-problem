---
author: Yin
---

# Stronger original trace income at the two linear dyadic residue clusters

Human author Yin.
Root supplied and developed the actual C3/C5 self-root calculation and all deductions below during the active G0001 continuation.
This is contributor mathematics, not independent review.
The complete fixed C191v2 proof and C178 valuation identity were read before this continuation.
A targeted local reuse search for the two endpoint clusters and the constants9/11 and51/11 found no retained theorem at this scope.
The fixed C191v2 and its historical review relationship are unchanged.
No mathematical program, parameter scan, source acquisition or new external-source proof inspection is used.

## Statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, constant coefficient1 and degree d=2r>=2.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1) and F=Q(delta), assume F is totally real, and let T be the actual monic minimal trace polynomial.
Thus [F:Q]=r, [K:F]=2 and P(z)=z^r T(z+z^(-1)).
Use C2(X)=X^2-2, C3(X)=X^3-3X and C5(X)=X^5-5X^3+5X.
The actual trace values a,b,c are nonzero algebraic integers, and the residual defects e,f,g are defined by

    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

These are the same values as the divided remainders modulo T evaluated at delta.
Write Tbar for reduction modulo2 and put

    r0=ord_X Tbar, r1=ord_(X+1) Tbar,
    0<=r0+r1<=r.

They count COMPLETE original residue multiplicities, not distinct residue roots.

**A. The f-only domain.**
Assume f=0.
Then

    v_2(Norm_F(a)) >= (3r+6r0+6r1)/11,
    v_2(abs Norm_F(c)) >= (2r+15r0+15r1)/11.       (1)

The integer left sides may equivalently be bounded by the ceilings of the right sides.
In particular each nonempty X or X+1 residue cluster has average normalized a valuation at least9/11, in place of the general3/11 floor.
The original doubled-conjugate resultant satisfies

    Res(P(z),P(z^2))
      =2^d Norm_F(a)^2
      >=2^[d+2ceil((3r+6r0+6r1)/11)].             (2)

No full-residual conclusion for g is asserted from f=0 alone.

**B. The complete residual domain.**
Add e+s g=0 and g!=0 for s in{1,-1}.
At EVERY prime p over2 whose delta residue is zero, the integer-normalized valuation satisfies

    v_p(a)>=v_p(2), v_p(c)>=2v_p(2),
    v_p(g)>=6v_p(2).                             (3)

The complete weighted norms therefore satisfy

    v_2(Norm_F(a)) >= (3r+8r0+6r1)/11,
    v_2(abs Norm_F(c)) >= (2r+20r0+15r1)/11,
    v_2(abs Norm_F(g)) >= (6r+60r0+45r1)/11.      (4)

Again all three right sides may be rounded up.
Moreover r1>0 implies r0>0.
If the entire reduction is supported at X, then abs Norm_F(g)>=2^(6r) and abs Norm_K(g)>=2^(6d), even with multiple original primes above2.
There is no assertion that such an actual residual input exists.

**C. Exact original scalar consequence.**
On the complete residual domain put rho0=r0/r, rho1=r1/r and

    chi=(6+60rho0+45rho1)/11.

Then

    abs Norm_K(g)>=2^(chi d).                    (5)

Consequently, for the ACTUAL maximal quotient Q_s, scalar c_nu and ordinary rational polynomial

    u_s=H35 Q_s/(30375 c_nu q), q>0 rational,

of adopted C614v1, one has

    abs Norm_K(u_s(alpha)) >= (2^chi/q)^d.        (6)

The complete original-order factor, full q^d denominator and all d embeddings are retained.
For a class with a proved lower bound chi>=chi0, any fixed q<2^chi0 gives norm strictly greater than1.
This strengthens only the arithmetic side of that construction.
No upper Mahler estimate, fixed sparse support, coefficient budget, positive density of either cluster, actual residual realization or unrestricted G0001 gap is supplied.

## Complete argument

### 1. Accepted complete cluster mechanism and its precise low case

Use the complete original-prime decomposition of C191v2.
At p|2 write E_p=v_p(2), A_p=v_p(a), B_p=v_p(b), C_p=v_p(c), beta_p=A_p/E_p, and let f_p be the full residue degree.
If the minimal polynomial of the residue of delta has degree h, put m_p=f_p/h and n_p=E_p m_p.
The corresponding local polynomial has exactly n_p roots above each geometric root of that residue polynomial.
Every root in the cluster is retained, including repetitions arising from a nonmaximal power order.
The cluster contributes h sum_p n_p to r and h sum_p n_p beta_p to v_2(Norm_F(a)).
In particular the X and X+1 clusters have h=1 and contribute exactly r0 and r1.

The accepted C191v2 proof under f=0 gives beta_p>=1/5 and a weighted cluster average at least3/11.
More precisely, if a cluster has beta_p<1 at a prime p, that prime is unique in the cluster and

    m_p=j_p=1, n_p=E_p, E_p>=2,
    beta_p=2R/E_p,
    0<R=sum_(q!=p) n_q<E_p/2,
    t_q=j_q/E_q>2/E_p for every q!=p,             (7)

while beta_q>=1 for all q!=p.
Here j_q is the positive integral distance from delta to its periodic C2 lift, and t_q is its normalized distance.
The proof obtains (7) from the exact self-composition a and unequal valuation minima, not from an arbitrary integral element.
We reuse its complete factor-counting, periodic-lift, low-prime uniqueness and noncancellation argument at that exact scope.

The C2 fixed points solve X^2-X-2=0 and are2 and-1.
Thus the common periodic lift is eta=2 for the X cluster and eta=-1 for X+1.
Both are rational fixed points and are the unique lifts at their respective residues by the accepted simple-root Hensel interface.

### 2. Exact additional self-root contribution at both fixed points

Fix a low prime in (7), write E=E_p, and write delta=eta+w with v_2(w)=1/E.
Every other root from p is at distance1/E from eta; every root from another prime q in the cluster is at distance t_q>2/E.
These statements are invariant under all local embeddings and count every original root.

At eta=2 one has

    C3(2+w)-(2+w)=8w+6w^2+w^3,
    C5(2+w)-(2+w)=24w+50w^2+35w^3+10w^4+w^5.

The first expression has valuation3/E because E>=2 makes3/E strictly smaller than3+1/E and1+2/E.
For the second, 35w^3 is uniquely minimal with valuation3/E: the other valuations are3+1/E,1+2/E,1+4/E,5/E.
Thus both self-root differences have exactly3/E.
Also C3(2+w)-2 and C5(2+w)-2 have valuation1/E, since their linear coefficients9 and25 are odd and all higher terms have larger valuation.

At eta=-1 the exact C5 self-root factorization is

    C5(delta)-delta=delta(delta^2-1)(delta^2-4).

Here delta is odd, delta^2-4 is odd, and delta^2-1=w(w-2) has valuation2/E because1/E<1.
Hence C5(delta)-delta has valuation2/E.
Also C5(-1+w)+1 has valuation1/E: its linear coefficient is-5, an odd unit, and every higher power has larger valuation.

For a polynomial T(Cj(delta)), the factor corresponding to the SAME root delta has the larger self-root distance just calculated.
Every other root from p contributes at least1/E, since both its distance and Cj(delta)'s distance from eta have valuation1/E.
Every root from another prime in that cluster contributes exactly1/E, because its distance t_q is strictly larger.
All roots in other residue clusters contribute zero valuation, as Cj preserves eta modulo2 in each of the cases being used.
The denominators3 and5 are2-adic units.

There are E roots from p and R other roots in this degree-one cluster.
Consequently the X cluster satisfies, for BOTH j=3 and j=5,

    B_p/E >= 1+(R+2)/E,
    C_p/E >= 1+(R+2)/E.                          (8)

The X+1 cluster satisfies

    C_p/E >= 1+(R+1)/E.                          (9)

Repeated roots of T modulo2 do not cause a missing factor: exactly one characteristic-zero factor is singled out as delta, all other E-1 are still counted.
T is separable in characteristic zero, and the actual a,b,c are nonzero.

### 3. Improved f-only cluster averages

The equation f=0 gives5A_p=E+2C_p.
At a low prime, A_p/E=2R/E, so

    C_p/E=5R/E-1/2.

For X, combining this with (8) yields8R>=3E+4.
For X+1, combining it with (9) yields8R>=3E+2.
In either case R/E>=3/8.
Since every other beta_q>=1, the complete cluster numerator is at least

    E beta_p+R=3R.

Thus

    sum_q n_q beta_q / sum_q n_q
       >=3R/(E+R)>=9/11.                        (10)

If no low prime exists, every beta_q>=1, which is stronger than (10).
This proves the claimed9/11 floor for both linear clusters without the second residual equation.

All other clusters retain the complete3/11 bound from C191v2.
Adding their exact degree weights gives the first inequality in (1).
The exact norm-weighted identity

    2 sum_(p|2) f_p C_p
       =5 sum_(p|2) f_p A_p-r

gives the second.
Integrality gives the ceilings.
Under f=0, a is totally positive, and the unchanged original relation P(alpha^2)=2alpha^d a with Norm_K(alpha)=1 proves (2).

### 4. Exclusion of a low prime in the zero-residue cluster

Assume the complete residual equations.
Suppose for contradiction that the X cluster has a prime with beta_p<1.
Then (7)--(8) apply, and R<E/2 gives

    2 B_p/E >=2+2R/E+4/E >6R/E=3 A_p/E.

Therefore b^2-a^3 has valuation exactly3A_p, with no tied cancellation.
The accepted C178 complete-residual identity gives v_p(g)=3C_p.
The equation e+s g=0 then forces A_p=C_p.
Together with5A_p=E+2C_p this forces3A_p=E, so A_p/E=C_p/E=1/3.
But (8) gives C_p/E>1, a contradiction.
Hence every prime in the X cluster has beta_p>=1.
The same f identity gives C_p>=2E_p, and C178 gives v_p(g)>=6E_p.
This proves the pointwise assertions (3), not merely a cluster average.

The X+1 cluster keeps its9/11 average and all other clusters their3/11 average.
Adding the exact original weights gives the first bound in (4), since the gains over3/11 are8/11 on X and6/11 on X+1.
The f identity then gives the second bound, and v_p(g)=3C_p at EVERY original prime gives the third.
No good prime is selected in place of the full sum.

For the support implication, suppose r1>0 and choose an actual prime with delta residue1.
Then C5(delta) has residue1, so the actual c=T(C5(delta))/5 has positive valuation.
The f equation gives A_p>0 at every2-prime.
Thus g has positive valuation by C178, and e+s g=0 forces b^2 to have positive valuation, hence B_p>0.
But C3(delta) has residue0 and3 is a unit, so Tbar(0)=0.
Therefore r0>0.
No quantitative lower bound for r0/r follows from this implication alone.

If r0=r, (3) summed over all primes yields v_2(abs Norm_F(g))>=6r.
This includes several primes above2 and does not assume a maximal power order.

### 5. Complete original norms and the unchanged multiplier

The nonzero integral g has full F norm a nonzero integer.
Every finite-prime contribution away from2 is nonnegative.
The quadratic tower gives Norm_K(g)=Norm_F(g)^2.
Doubling the third bound in (4) and using d=2r gives (5).

At the exact adopted C614 interface, Q_s(alpha)=c_nu b_s(alpha), where b_s(alpha) is a nonzero element of the original order Z[alpha].
Its complete norm is therefore a nonzero rational integer.
The actual original phase is H35(alpha)=-30375 alpha^(15d/2) g, with Norm_K(alpha)=1.
The SAME ordinary rational polynomial u_s consequently satisfies

    abs Norm_K u_s(alpha)
      =abs Norm_K(g) abs Norm_K(b_s(alpha))/q^d
      >=(2^chi/q)^d.

This proves (6), without asserting coefficientwise integrality of Q_s/c_nu or substituting its lower-degree remainder for its circle function.
A fixed class bound chi>=chi0 is a separate hypothesis when choosing a larger fixed q.
All Mahler, support, coefficient, degree and analytic transfer costs remain to be paid exactly as in C614.
The new norm income does not establish such a class or any unrestricted Mahler gap.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision linear-clusters-open

| Field | Value |
| --- | --- |
| date | 2026-10-23T17:20 |
| status | open |
| reason | Register the complete actual linear-cluster self-root refinement, f-only norm bounds, pointwise zero-residue low-prime exclusion under the full residual system, full weighted arithmetic gain and exact original multiplier consequence. The correct periodic lift2 is used at residue0. Root is the proof contributor; fresh whole independent review and adoption remain separate. No density, upper analytic budget, input realization or unrestricted Task conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire linear-cluster theorem](#statement) | Complete original domain; f-only versus full residual hypotheses; all original residue multiplicities, pointwise and full-norm assertions, support implication and actual scalar consequence. |
| argument | [Complete proof](#complete-argument) | All accepted low-case conditions, exact fixed-point expansions, every self and other root, weighted cluster inequalities, pointwise contradiction, full prime sum and quadratic original norm with unchanged multiplier costs. |
| dependency | [Complete actual cluster proof](Yin_C_G0191_v2.md#argument) | Full original local factors, residue multiplicities, unique low-beta prime, m=j=1 and exact beta=2R/E, all other distances and valuations, general3/11 bound and full norm weights; no stronger linear-cluster claim imported. |
| dependency | [Full-residual local identity](Yin_C_G0178_v1.md#statement) | G_p=3C_p for every original prime over2 under the explicitly retained nonzero integral full residual equations; not invoked on the f-only domain. |
| dependency | [Actual trace values and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual quadratic trace field, integral nonzero divided quotients and full original phases; no arbitrary abstract triple substitutes for them. |
| dependency | [Actual maximal quotient](Yin_C_G0614_v1.md#complete-argument) | Only exact original-order nonzero b_s, full original degree/norm, same H35 phase and rational normalization; all analytic budgets remain unsupplied and no new C196 application is claimed. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T17:29 |
| status | proved |
| reason | Adopt the entire original linear-cluster theorem after reading its complete fixed proof and fresh isolated R821 finding. The nonzero introductory wording now explicitly concerns only a,b,c. All f-only versus full-residual hypotheses, actual fixed points, original root multiplicities, pointwise zero-cluster result, full norm weights and unchanged scalar costs are retained. No cluster density, upper analytic budgets, actual residual realization or unrestricted gap is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire linear-cluster theorem](#statement) | Complete original domain; f-only versus full residual hypotheses; all original residue multiplicities, pointwise and full-norm assertions, support implication and actual scalar consequence. |
| argument | [Complete proof](#complete-argument) | All accepted low-case conditions, exact fixed-point expansions, every self and other root, weighted cluster inequalities, pointwise contradiction, full prime sum and quadratic original norm with unchanged multiplier costs. |
| dependency | [Complete actual cluster proof](Yin_C_G0191_v2.md#argument) | Full original local factors, residue multiplicities, unique low-beta prime, m=j=1 and exact beta=2R/E, all other distances and valuations, general3/11 bound and full norm weights; no stronger linear-cluster claim imported. |
| dependency | [Full-residual local identity](Yin_C_G0178_v1.md#statement) | G_p=3C_p for every original prime over2 under the explicitly retained nonzero integral full residual equations; not invoked on the f-only domain. |
| dependency | [Actual trace values and phases](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual quadratic trace field, integral nonzero divided quotients and full original phases; no arbitrary abstract triple substitutes for them. |
| dependency | [Actual maximal quotient](Yin_C_G0614_v1.md#complete-argument) | Only exact original-order nonzero b_s, full original degree/norm, same H35 phase and rational normalization; all analytic budgets remain unsupplied and no new C196 application is claimed. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G0821_v1.md#linear-clusters-whole-finding) | Complete fixed statement, entire argument, every selected and actually used interface, full proof and native roles where applicable, and exact historical review/source limits. |

