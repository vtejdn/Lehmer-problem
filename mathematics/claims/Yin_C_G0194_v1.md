---
author: Yin
---
# Linear canonical residuals force a large original Mahler measure

Date: 2026-10-20T12:40.
Human author Yin.
Root supplied the new per-cluster exclusion, all five local branches, their stronger norm bounds and the exact original-root Mahler comparison.
The draft_inventory_later agent checked every inequality and boundary, supplied the earlier canonical low-Haar classification, and assembled this complete fixed statement and proof.
Both are contributors, not independent reviewers.
The earlier canonical screen remains at its actual author scope; the present proof does not depend on a mutable draft as a mathematical premise.
No parameter scan, numerical root, native mathematical computation or new external theorem is used.

<a id="statement"></a>
## Exact theorem statement

Let P be a monic irreducible reciprocal nontorsion integer-unit polynomial with constant coefficient1 and degree d=2r.
For a root alpha write K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and let T in Z[X] be the actual monic irreducible trace polynomial, so

    P(z)=z^r T(z+z^(-1)), [K:F]=2, [F:Q]=r.

Assume F is totally real.
Let C_n(delta)=alpha^n+alpha^(-n), and use the actual nonzero integral trace quotients

    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

Suppose, for s in{1,-1},

    f=e+s g=0, g!=0.                              (1)

Suppose additionally that

    g=epsilon(delta-k), epsilon in{1,-1},
    k in{-2,-1,0,1,2}.                            (2)

Then the following exhaustive alternatives hold.

| k | Consequence |
| --- | --- |
| 2 or-1 | The full system(1)--(2) is impossible. |
| 0 | abs(Norm_F(g))>=2^(6r) and m(P)>=5r log2. |
| 1 | abs(Norm_F(g))>=2^(6r) and m(P)>=r log(64/3). |
| -2 | abs(Norm_F(g))>=2^(21r) and m(P)>=19r log2. |

Here m(P) is the TOTAL logarithmic Mahler measure of the original degree-d polynomial.
No ramification, residue-degree, power-order saturation or one-prime hypothesis is imposed.
In particular no such actual residual input has m(P)<log2.
The nonexistence assertions for k=2,-1 have no small-measure restriction.
The other rows are necessary lower bounds and do not assert existence at larger measure.

There is a canonical-remainder consequence with a precise Haar scope.
Define theta_p=rem_T(T(C_p(X)))/p in Z[X] for p=2,3,5, and put

    Gbar=rem_T(theta_5^3-2theta_3^5) in Z[X].

Under(1), let B_can(z)=Gbar(z+z^(-1))^2 and let I_can be its normalized Haar logarithmic integral.
If m(P)<log2 and deg(Gbar)<=1, then

    I_can >= (12/11)log2.                         (3)

Thus there is no useful canonical degree-zero or degree-one residual saving below the stronger guaranteed residual income of C191v2 in this original small-measure class.
No conclusion for deg(Gbar)>=2, arbitrary rational representatives, an unrestricted Haar transfer, or the full G0001 contract is asserted.

<a id="argument"></a>
## 1. Every residue cluster must be the linear k class

The accepted [C153v2 trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) supplies the exact original fields and nonzero integral quotient values.
At every prime p of F over2 use the integer-valued valuation and write

    e_p=v_p(2), f_p=[O_F/p:F_2],
    A_p=v_p(a), C_p=v_p(c), G_p=v_p(g),
    beta_p=A_p/e_p, r_p=e_p f_p.

The accepted [C178 residual theorem](Yin_C_G0178_v1.md#statement) gives

    5A_p=e_p+2C_p, G_p=3C_p,
    beta_p=1/5+2G_p/(15e_p).                      (4)

It also excludes any unramified prime over2 in this full residual system.
Consequently e_p>=2 and r_p>=2 at every prime of a possible input.
These uses require both equations in(1), not merely f=0.

Let phi be the minimal polynomial over F_2 of the residue of delta at a cluster of primes, in the exact sense of [C191v2 Sections1--3](Yin_C_G0191_v2.md#argument).
Write r_phi=sum_(p in cluster)e_p f_p>0.
Its complete per-cluster estimate(15), including the no-low-beta case, gives

    sum_(p in cluster)f_p A_p >= (3/11)r_phi.

Using(4) within that SAME cluster yields

    sum_(p in cluster)f_p G_p
      =(3/2)(5 sum_(p in cluster)f_p A_p-r_phi)
      >=(6/11)r_phi>0.                            (5)

This is a per-cluster consequence of the accepted proof, not a conclusion inferred from a global sum alone.
All local residue weights are retained.

If phi differs from the linear polynomial X-(k mod2), then delta_bar-k is nonzero at every prime of that cluster.
Equation(2) makes g a unit at every one of them, so every G_p would be0, contradicting(5).
Therefore all primes have

    delta_bar=k mod2, h_p=deg(phi_p)=1,
    G_p>0, G_p=3C_p>=3.                           (6)

This does not say f_p=1 or that there is only one prime above2.
The residue of the chosen generator can lie in F_2 even when the full residue field is larger.

## 2. The exact fixed-point lift and all five valuation branches

For h=1 the periodic polynomial of C191v2 is

    C2(X)-X=X^2-X-2=(X-2)(X+1).

Its simple residue lifts are therefore eta=2 for even k and eta=-1 for odd k.
The actual nontorsion trace delta cannot equal either fixed point.
For a prime p suppress subscripts and put j=v_p(delta-eta)>0.
The self contribution in C191v2(11) has m_p=f_p/h_p=f_p, and hence gives the exact useful inequality

    beta>=f_p j-1.                               (7)

It is valid with any number of other primes in the same cluster; their extra contributions are nonnegative.
The normalization of j is the integer valuation, whereas beta=A/e and the distance used in the accepted factor proof is j/e.
No factor of e or f_p has been removed from(7).

For k=2 or-1 one has k=eta, so j=G.
Using G>=3, f_p>=1 and e>=1, equations(4),(7) would imply

    G-1 <= beta=1/5+2G/(15e) <=1/5+2G/15.

This is impossible: the left side minus the last right side is(13/15)G-6/5>=7/5>0.
Thus these two cases have no actual input at any measure.

For k=0 or1, v_p(k-eta)=e.
If0<G<e, the two terms of delta-eta=(delta-k)+(k-eta) have different valuations, so j=G.
Then(7) gives beta>=G-1>=2, whereas(4) gives beta<1/3, a contradiction.
In the remaining case G>=e the ultrametric inequality gives j>=e, including the possible cancellation when G=e.
Consequently

    beta>=e f_p-1=r_p-1,
    G/e=(15beta-3)/2
        >=(15r_p-18)/2>=6.                        (8)

For k=-2, eta=2 and v_p(k-eta)=2e.
If0<G<2e, the unequal-valuation rule again gives j=G>=3.
Equations(4),(7) would give beta<7/15 and beta>=2 simultaneously.
Thus G>=2e, so j>=2e, including equality and cancellation, and

    beta>=2e f_p-1=2r_p-1,
    G/e=(15beta-3)/2>=15r_p-9>=21.                (9)

All comparisons hold at EVERY original prime over2.
The sign epsilon in(2) is a unit and changes none of the valuations.
The two signs s in the residual equation were already covered by the accepted C178 and C191v2 inputs.

## 3. Full norm and the original Mahler price

For k=0,1, equation(8) and the complete decomposition sum give

    v_2(abs(Norm_F(g)))=sum_(p|2)f_p G_p
       >=6 sum_(p|2)e_p f_p=6r.

For k=-2 the same argument with(9) gives21r.
Since g is nonzero and integral, its other finite-prime contributions are nonnegative and the stated full-norm lower bounds follow.
No smaller own field of g has replaced F in these equalities.

List the r inverse pairs of roots of P and choose alpha_i from each pair with rho_i=|alpha_i|>=1.
The corresponding delta_i=alpha_i+alpha_i^(-1) run through all r trace conjugates once.
Reciprocity gives

    sum_(i=1)^r log rho_i=m(P).

For every i the exact triangle bound is

    |delta_i-k|<=rho_i+rho_i^(-1)+|k|
                <=(|k|+2)rho_i.

Equation(2) and multiplication over all r conjugates therefore yield

    abs(Norm_F(g))
       <=(|k|+2)^r exp(m(P)).                     (10)

This is a bound for the original total m(P), with coefficient1, not twice that quantity or a normalized height.
Combining it with the preceding norm bounds gives5r log2 for k=0, r log(64/3) for k=1, and19r log2 for k=-2.
Each is greater than log2 for r>=1.
The impossible unramified case already handles r=1 in the full residual domain; it was not silently used as an extra hypothesis in the archimedean comparison.
This proves every row of the statement.

<a id="canonical-linear-haar-consequence"></a>
## 4. Complete degree-at-most-one Haar consequence

C153v2's monic-remainder divisibility proves that each theta_p has integer coefficients.
Consequently Gbar is an integer polynomial of degree less than r and Gbar(delta)=g.
Minimality of T and g!=0 make Gbar nonzero.
For w=deg(Gbar) let H_G(z)=z^w Gbar(z+z^(-1)); this is an integer reciprocal polynomial and

    I_can=2m(H_G).                                (11)

The equality, integrability of its finite-order circle zeros, and the leading-coefficient bound are exactly the accepted [scalar Jensen convention](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).
No new original-source proof audit is claimed for that interface.

If w=0, write Gbar=q in Z minus{0}.
C191v2's actual residual norm gives |q|^r>=2^(6r/11), so |q|>=2 and I_can=2log|q|>=(2log2)>(12/11)log2.
The original-root and Haar logarithms also agree exactly in this constant case.

If w=1 and, contrary to(3), I_can<(12/11)log2, write Gbar=lX+b with l a nonzero integer.
Jensen gives m(H_G)>=log|l|, so |l|=1.
Thus Gbar=epsilon(X-k) for an integer k.
If |k|>=3, the larger modulus rho of a root of z^2-kz+1 satisfies rho+rho^(-1)=|k|>=3 and hence rho>2.
It follows that m(H_G)>log2, contradicting the assumed Haar bound.
Therefore k belongs to the five-element set in(2).
Sections1--3 now contradict m(P)<log2.
This proves(3) with its stated strict-small-measure and exact canonical restrictions.
It does not classify or exclude higher-degree canonical remainders.

<a id="inputs-and-boundaries"></a>
## Exact inputs and remaining scope

| Input | Scope used |
| --- | --- |
| [C191v2 full argument](Yin_C_G0191_v2.md#argument) | Per-cluster equation(15), all residue multiplicities and the h=1 self contribution(11); its global norm bound is used separately for the constant canonical case. |
| [C191v2 adopted statement](Yin_C_G0191_v2.md#statement) | Complete actual original trace domain and residual6/11 income, at its adopted all-prime scope. |
| [C178](Yin_C_G0178_v1.md#statement) | Both residual equations imply G=3C,5A=e+2C and exclude each unramified2-prime; this is not an f-only use. |
| [C153v2 exact trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees and phases, nonzero integral quotient values and coefficientwise integral monic remainders. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only its scalar Mahler/Jensen normalization, leading coefficient bound and finite circle-zero convention for Section4; no new Kronecker or nonreciprocal theorem is needed. |
| Elementary exact identities | The explicit fixed points2,-1, strict-minimum valuations and cancellation inequalities, complete ideal-norm weights and the original inverse-pair product in(10). |

The necessary local restrictions are applied to the actual original quotient a=T(C2(delta))/2, never to an unrelated integral triple.
The per-cluster positive income is essential: a global norm lower bound alone would not eliminate all other residue clusters.
All original primes and trace conjugates are present, and the original unit polynomial's total measure is retained.
The statement proves no universal nonexistence of residual triples, no failure of the abstract unit-residual construction, and no uniform logarithmic transfer for higher-degree canonical or rational auxiliaries.
The author check verified the two equal-threshold cancellation cases G=e and G=2e, both signs, the r=1 exclusion, nonprimitive residue fields and every factor in the archimedean product.
A noncontributor whole review and any adoption remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:40 |
| status | open |
| reason | Register the complete five-class actual residual exclusion and exact canonical degree-at-most-one Haar consequence, with full cluster and original-measure costs, for a separate noncontributor whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete five-class theorem and canonical consequence](#statement) | All original inputs and signs, two impossible classes, three exact original norm/Mahler bounds and the low-Haar degree-at-most-one conclusion. |
| argument | [Complete four-section proof](#argument) | Every cluster, fixed-point lift and valuation branch, original full norm and inverse-pair price, followed by the exact constant/linear Haar classification. |
| dependency | [Actual cluster and self-factor proof](Yin_C_G0191_v2.md#argument) | Per-cluster(15), full local multiplicities, h=1 own-factor inequality(11), and accepted original normalization. |
| dependency | [Actual global residual income](Yin_C_G0191_v2.md#statement) | Residual6/11 bound for the constant canonical case. |
| dependency | [Exact residual valuations](Yin_C_G0178_v1.md#statement) | G=3C,5A=e+2C and unramified impossibility under both full residual equations. |
| dependency | [Original integral trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Exact fields, values and coefficientwise divided remainders. |
| dependency | [Scalar normalization source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the recorded Jensen/leading-coefficient and circle-zero conventions, at their existing inspection scope. |
| support | [Inputs, contributions and limits](#inputs-and-boundaries) | Original-field and per-cluster requirements, actual author checking, no higher-degree or unrestricted completion inference. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:47 |
| status | proved |
| authority | Internal adoption within Yin's selected canonical-remainder and actual original-transfer inquiry. |
| reason | Adopt the entire five-class original residual theorem and canonical degree-at-most-one consequence through whole R470. The per-cluster local constraints and exact original inverse-pair cost exclude every useful constant or linear canonical residual in the stated small-measure domain. Higher-degree canonical cases and full logarithmic transfer remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete five-class theorem and canonical consequence](#statement) | All original inputs and signs, two impossible classes, three exact original norm/Mahler bounds and the low-Haar degree-at-most-one conclusion. |
| argument | [Complete four-section proof](#argument) | Every cluster, fixed-point lift and valuation branch, original full norm and inverse-pair price, followed by the exact constant/linear Haar classification. |
| dependency | [Actual cluster and self-factor proof](Yin_C_G0191_v2.md#argument) | Per-cluster(15), full local multiplicities, h=1 own-factor inequality(11), and accepted original normalization. |
| dependency | [Actual global residual income](Yin_C_G0191_v2.md#statement) | Residual6/11 bound for the constant canonical case. |
| dependency | [Exact residual valuations](Yin_C_G0178_v1.md#statement) | G=3C,5A=e+2C and unramified impossibility under both full residual equations. |
| dependency | [Original integral trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Exact fields, values and coefficientwise divided remainders. |
| dependency | [Scalar normalization source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the recorded Jensen/leading-coefficient and circle-zero conventions, at their existing inspection scope. |
| support | [Inputs, contributions and limits](#inputs-and-boundaries) | Original-field and per-cluster requirements, actual author checking, no higher-degree or unrestricted completion inference. |
| review | [Whole independent linear-canonical finding](../audits/reviews/Yin_R_G0470_v1.md#linear-canonical-residual-whole-finding) | Complete actual four-section statement, all1--11 formulas and six inputs, every residue/valuation branch and original norm/Mahler factor, exact constant/linear Haar scope and contributor boundaries. |

