---
author: Yin
---
# Constant, linear and quadratic canonical residuals have no low-Haar small-measure window

Date: 2026-10-20T12:54.
Human author Yin.
This substantive v2 retains the complete five-class linear theorem and proof of [v1](Yin_C_G0194_v1.md#statement), whose adopted decision and whole R616 remain at their original scope.
Root supplied the original per-cluster linear exclusion and Mahler comparison, and then the new low-measure quartic classification, all quadratic local branches and their full original norm and measure bounds.
The draft_inventory_later agent supplied the earlier canonical-remainder screen, checked every inequality and cancellation boundary in both rounds, and assembled this complete fixed successor.
Both are contributors, not independent reviewers.
The earlier canonical screen is provenance, not a mutable logical premise of this proof.
The new quadratic proof and its assembly require a new noncontributor whole review; v1 acceptance is not transferred to the enlarged statement.
No parameter scan, numerical root or native mathematical computation was performed.
Only previously accepted external inputs are used, with Kronecker's exact multiplicity convention now explicitly invoked for the quadratic classification.

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

There is also a complete quadratic comparison under(1).
For epsilon in{1,-1}, suppose g=epsilon R(delta) with R one of the following monic quadratic polynomials.

| R(X) | Consequence |
| --- | --- |
| (X-k_1)(X-k_2), with k_1,k_2 in{-2,-1,0,1,2}, including repetitions | abs(Norm_F(g))>=2^(6r) and m(P)>=r log2. |
| X^2+X-1 | The full residual system is impossible. |
| X^2-X-1, X^2-2, or X^2-3 | abs(Norm_F(g))>=2^(6r) and m(P)>=(r/2)log(64/7)>r log2. |

These alternatives cover every quadratic canonical remainder whose Haar cost is below(12/11)log2, as proved below.
The table does not assume irreducibility of R in its first row, and includes both the repeated-root and mixed-parity cases.
Its last three individual estimates use the displayed common constant7; no best constant is asserted.

There is a canonical-remainder consequence with a precise Haar scope.
Define theta_p=rem_T(T(C_p(X)))/p in Z[X] for p=2,3,5, and put

    Gbar=rem_T(theta_5^3-2theta_3^5) in Z[X].

Under(1), let B_can(z)=Gbar(z+z^(-1))^2 and let I_can be its normalized Haar logarithmic integral.
If m(P)<log2 and deg(Gbar)<=2, then

    I_can >= (12/11)log2.                         (3)

Thus there is no useful canonical degree-at-most-two residual saving below the stronger guaranteed residual income of C191v2 in this original small-measure class.
No conclusion for deg(Gbar)>=3, arbitrary rational representatives, an unrestricted Haar transfer, or the full G0001 contract is asserted.

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
## 4. Constant and linear cases of the canonical consequence

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
This proves(3) for degree at most1 with its stated strict-small-measure and exact canonical restrictions.
The following four sections prove the new quadratic portion; the earlier argument and its stronger linear bounds are retained in full.

<a id="quadratic-low-haar-classification"></a>
## 5. Complete low-Haar quadratic classification without a grid

Suppose Gbar has degree2 and I_can<(12/11)log2.
Equation(11) and the leading-coefficient bound make Gbar monic up to a common sign.
Remove that sign and put R=Gbar, H(z)=z^2 R(z+z^(-1)), M=M(H).
Then H is monic reciprocal of degree4 with constant1, and

    1<=M<2^(6/11)<3/2.                            (12)

The last strict comparison is the exact integer inequality2^17<3^11.
We first show that the roots of R are real.
If they are a+ib and a-ib with b!=0, a root alpha of the corresponding reciprocal quadratic can be chosen with modulus rho>1.
The four roots of H are alpha,alpha^(-1),conjugate(alpha),conjugate(alpha)^(-1), so M=rho^2.
The identity Im(alpha+alpha^(-1))=(rho-rho^(-1))sin(arg alpha) gives

    b^2<=(rho-rho^(-1))^2=M+M^(-1)-2<1/6.

But a monic integer quadratic has negative discriminant at most-3 when its roots are nonreal: the discriminant is0 or1 modulo4.
Thus b^2 is at least3/4, a contradiction.

Now let xi_1,xi_2 be the real roots of R.
For each root outside[-2,2], its reciprocal pair contributes a factor rho_i>=1 to M and satisfies |xi_i|=rho_i+rho_i^(-1).
Since rho_i<=M, every root, including those already inside[-2,2], obeys

    |xi_i|<=L=M+M^(-1)<13/6.

If some xi_i>2 and R(2)!=0, integrality and the other root's bound would imply

    1<=|R(2)|<=(L-2)(L+2)<25/36<1.

If R(2)=0, the other root is an integer, so a root strictly between2 and13/6 is again impossible.
The identical argument at-2 excludes a root below-2, including the case R(-2)=0.
Therefore both roots of R lie in[-2,2], all four roots of H lie on the unit circle, and M=1.
The accepted Kronecker characterization in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) makes H a product of cyclotomic polynomials with multiplicities.
This use retains that source's actual inspection boundary; it is not an audit of Kronecker's original proof.

Only cyclotomic orders n with phi(n)<=4 can occur in a degree-four product.
For completeness, a prime divisor p of n satisfies p-1<=4, so only2,3,5 can divide n.
The prime-power totient formula bounds their exponents respectively by3,1,1, and its multiplicativity leaves exactly

    n in{1,2,3,4,5,6,8,10,12}.

The multiplicities of Phi_1 and Phi_2 in H are even, because the trace pullbacks at2 and-2 have double zeros.
The reciprocal degree-two blocks give the linear trace factors X-2,X+2,X+1,X,X-1.
The four degree-four factors give

    z^2(X^2+X-1)|_(X=z+z^(-1))=Phi_5(z),
    z^2(X^2-X-1)|_(X=z+z^(-1))=Phi_10(z),
    z^2(X^2-2)|_(X=z+z^(-1))=Phi_8(z),
    z^2(X^2-3)|_(X=z+z^(-1))=Phi_12(z).

Consequently the complete possibilities are

    R=(X-k_1)(X-k_2), k_i in{-2,-1,0,1,2},
    or R=X^2+X-1, X^2-X-1, X^2-2, X^2-3.         (13)

The original sign epsilon is restored when evaluating g=epsilon R(delta).
This is an exhaustive analytic and cyclotomic classification, not a finite numerical screen.

<a id="quadratic-residue-cluster-cost"></a>
## 6. All quadratic residue clusters and the reducible cases

Keep the actual full residual system and suppose g=epsilon R(delta) for a polynomial in(13).
The per-cluster positive income(5) still applies unchanged.
If a cluster's irreducible phi does not divide R mod2, every g value in that cluster is a unit, contradicting(5).
Thus every occurring cluster satisfies phi divides R mod2.
At every prime within such a cluster the residue of delta is a root of R mod2, so G=v_p(g)>0.
C178 then gives

    e>=2, G=3C>=3,
    beta=1/5+2G/(15e),
    beta>=(f_p/h)j-1,                             (14)

where h=deg(phi) and j=v_p(delta-eta)>0 uses the unique degree-h periodic lift from C191v2.
The residue degree f_p can be larger than h and remains in the self contribution.
The new restriction phi divides R mod2 is not deduced merely from the global norm.

For R=(X-k_1)(X-k_2), the only possible phi are X and X+1, so h=1.
Use eta=2 in the even residue class and eta=-1 in the odd one.
Let nu in{1,2} count the factors k_i with this same parity, including repetitions.
The other factors have unit values at delta.
For every matching factor the difference k_i-eta is0,2,-2 or-4 and has valuation at least e when it is nonzero.
If j<e, each matching factor delta-k_i therefore has exact valuation j and

    G=nu j, 3 divides nu j, hence3 divides j.

The implication uses nu in{1,2}; no repeated factor is discarded.
It follows that j>=3 and the self contribution gives beta>=f_p j-1>=2.
But(14) gives beta=1/5+2nu j/(15e)<1/5+4/15=7/15, a contradiction.
Consequently j>=e, and since e f_p>=2,

    beta>=e f_p-1>=1, G>=6e.                     (15)

This holds at every original prime over2, whether both factors match there or only one does.
In particular mixed parities and repeated linear factors are fully covered.

## 7. The four irreducible trace quadratics

For R=X^2+X-1 or X^2-X-1, reduction modulo2 is the irreducible polynomial X^2+X+1.
Thus h=2, f_p is divisible by2 and e f_p>=4.
The periodic lift eta satisfies

    C4(X)-X=(X-2)(X+1)(X^2+X-1),
    eta^2+eta-1=0.                                (16)

Indeed the linear factors have residues0 and1, whereas delta_bar is a root of X^2+X+1 and is neither.
They are units at eta, so the quadratic factor vanishes there and has a simple root in that residue class.
Its other root has the other F_4 residue, and eta is a unit.
The integer j=v_p(delta-eta) is positive and finite by the same nontorsion argument as C191v2.

For R=X^2+X-1, the other factor of R(delta) is a unit, so G=j>=3.
Equation(14) gives beta>=(f_p/2)j-1>=j-1, whereas beta=1/5+2j/(15e)<=1/5+2j/15.
The same strict comparison used for k=2,-1 contradicts j>=3.
This quadratic admits no actual residual input at any original measure.

For R=X^2-X-1, writing t=delta-eta gives

    R(eta)=-2eta, v_p(R(eta))=e,
    R(delta)=-2eta+(2eta-1)t+t^2.                 (17)

The linear coefficient is a unit.
If j<e, the unique smallest term gives G=j>=3, while beta>=j-1>=2 and beta<1/3 contradict one another.
If j>e, the unique smallest term is the constant and G=e, so beta=1/3.
But the self contribution is beta>=(f_p/2)j-1>=1, since e>=2,f_p>=2,j>e; this is impossible.
Thus j=e, including any cancellation between the equal-valued constant and linear terms.
The inequality beta>=e f_p/2-1>=1 gives G>=6e.
No equality G=e is asserted in this surviving tied case.

For R=X^2-2, reduction is X^2, h=1 and eta=2.
For R=X^2-3, reduction is(X+1)^2, h=1 and eta=-1.
With t=delta-eta their exact expansions are respectively

    R(delta)=2+4t+t^2,
    R(delta)=-2-2t+t^2.                           (18)

The constant has valuation e and the linear term has valuation strictly greater than e, so only e and2j can be smallest.
If2j<e, then G=2j and3 divides G, hence j>=3.
This gives beta>=f_p j-1>=2 but beta<1/3, a contradiction.
If2j>e, then G=e and beta=1/3.
The self contribution forces the positive integer f_p j to be at most4/3, so f_p=j=1.
But j>e/2 with e>=2 then fails.
Therefore

    2j=e, e is even,
    beta>=e f_p/2-1.                              (19)

If e f_p>=4, the last bound is at least1 and G>=6e follows.
Since e is even and e>=2, the only smaller local degree is e f_p=2, necessarily e=2,f_p=1.
In that case5A=e+2C=2+2C makes the positive integer A even, hence A>=2 and beta=A/e>=1.
This yields G>=6e in that last case also.
Both the equality threshold2j=e and its possible cancellation have thus been retained, without assuming that2 is unramified or that the power order is maximal.

For every allowed quadratic except the impossible X^2+X-1, the conclusion at ALL primes is consequently

    G_p>=6e_p,
    abs(Norm_F(g))>=2^(6r).                       (20)

The full sum uses f_p G_p and sum e_p f_p=r as before.

## 8. Exact original measure payment and completion of the quadratic consequence

Use the same complete inverse-pair representatives rho_i and sum log rho_i=m(P) as in Section3.
For a product of two allowed linear factors, each factor has modulus at most4rho_i, so |R(delta_i)|<=16rho_i^2.
For X^2-X-1, X^2-2 and X^2-3, the bounds |delta_i|<=2rho_i and rho_i>=1 give respectively7rho_i^2,6rho_i^2 and7rho_i^2.
Thus in the reducible case and in the three possible irreducible cases respectively,

    abs(Norm_F(g))<=16^r exp(2m(P)),
    abs(Norm_F(g))<=7^r exp(2m(P)).                (21)

Combining(20) with these bounds gives m(P)>=r log2 in the first case and m(P)>=(r/2)log(64/7)>r log2 in the second.
The latter strict comparison is64/7>4.
All r trace conjugates and the exact original total measure are present; no factor has been replaced by a single exterior-root value.
The estimates assert no existence in these classes.

If the canonical quadratic had I_can<(12/11)log2, Section5 would place it in(13), including its irrelevant common sign.
The impossible class or the resulting m(P)>=r log2 contradicts m(P)<log2.
This proves(3) for degree2 and completes the stated degree-at-most-two consequence together with Section4.
The five original linear conclusions, including their stronger constants and unconditional impossibilities, remain exactly as in v1.

<a id="inputs-and-boundaries"></a>
## Exact inputs and remaining scope

| Input | Scope used |
| --- | --- |
| [C191v2 full argument](Yin_C_G0191_v2.md#argument) | Per-cluster equation(15), all residue multiplicities and the h=1 or h=2 self contribution(11), including the periodic-lift uniqueness; its global norm bound is used separately for the constant canonical case. |
| [C191v2 adopted statement](Yin_C_G0191_v2.md#statement) | Complete actual original trace domain and residual6/11 income, at its adopted all-prime scope. |
| [C178](Yin_C_G0178_v1.md#statement) | Both residual equations imply G=3C,5A=e+2C and exclude each unramified2-prime; this is not an f-only use. |
| [C153v2 exact trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original degrees and phases, nonzero integral quotient values and coefficientwise integral monic remainders. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Mahler/Jensen normalization, leading-coefficient and finite circle-zero conventions, plus the already recorded Kronecker product-with-multiplicities characterization for Section5; no nonreciprocal theorem or new source-proof audit is used. |
| Elementary exact identities | The explicit degree-one/two periodic lifts, strict-minimum and tied valuation branches, complete ideal-norm weights, elementary degree-four cyclotomic classification and the original inverse-pair products(10),(21). |

The necessary local restrictions are applied to the actual original quotient a=T(C2(delta))/2, never to an unrelated integral triple.
The per-cluster positive income is essential: a global norm lower bound alone would not eliminate all other residue clusters.
All original primes and trace conjugates are present, and the original unit polynomial's total measure is retained.
The statement proves no universal nonexistence of residual triples, no failure of the abstract unit-residual construction, and no uniform logarithmic transfer for higher-degree canonical or rational auxiliaries.
The author check verified both rounds: the original equal-threshold cases G=e and G=2e, the quadratic j=e and2j=e cases, the exceptional e=2,f_p=1 parity, the complete low-Haar classification and repeated factors, both signs, the r=1 exclusion, nonprimitive residue fields and every original archimedean factor.
A noncontributor whole review and any adoption remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T12:54 |
| status | open |
| reason | Retain the entire adopted linear theorem and append the complete low-Haar quadratic classification, every actual local branch and original measure bound, extending the canonical exclusion to degree at most2. This enlarged version awaits its own noncontributor whole review; v1/R616 remain at their original scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete linear/quadratic theorem and canonical consequence](#statement) | All original signs and inputs, preserved five linear conclusions, complete quadratic classes, full norm/Mahler bounds and exact degree-at-most-two low-Haar restriction. |
| argument | [Complete eight-section proof](#argument) | Original linear proof plus the exact small-measure quartic classification, all possible cyclotomic trace factors and repeated roots, all h1/h2 local cases and complete original norm/measure payment. |
| dependency | [Actual cluster and periodic self-factor proof](Yin_C_G0191_v2.md#argument) | Per-cluster(15), original multiplicities, periodic lifts and h1/h2 own-factor inequality(11); no new residue primitivity assumption. |
| dependency | [Actual global residual income](Yin_C_G0191_v2.md#statement) | Residual6/11 norm for the constant canonical branch and exact original input domain. |
| dependency | [Exact residual valuations](Yin_C_G0178_v1.md#statement) | G=3C,5A=e+2C and unramified impossibility under both residual equations. |
| dependency | [Original integral trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Exact fields, values and coefficientwise divided remainders. |
| dependency | [Scalar normalization and Kronecker source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing Jensen/leading-coefficient and finite circle-zero conventions, plus the exact product-with-multiplicities measure-one characterization at its recorded inspection scope. |
| support | [Inputs, contributions and limits](#inputs-and-boundaries) | Full old/new author roles and comparison boundaries, no independent author review, no degree-at-least-three or unrestricted conclusion. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:09 |
| status | proved |
| authority | Internal adoption within Yin's selected actual residual and original-transfer inquiries. |
| reason | Adopt the complete constant, linear and quadratic canonical theorem through whole R472, retaining the stronger five linear bounds and the unchanged v1/R616 scope. The complete low-Haar quartic classification and every quadratic local cancellation branch give the exact degree-at-most-two exclusion in the original small-measure class. This does not cover higher-degree remainders or complete the original transfer. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete linear/quadratic theorem and canonical consequence](#statement) | All original signs and inputs, preserved five linear conclusions, complete quadratic classes, full norm/Mahler bounds and exact degree-at-most-two low-Haar restriction. |
| argument | [Complete eight-section proof](#argument) | Original linear proof plus the exact small-measure quartic classification, all possible cyclotomic trace factors and repeated roots, all h1/h2 local cases and complete original norm/measure payment. |
| dependency | [Actual cluster and periodic self-factor proof](Yin_C_G0191_v2.md#argument) | Per-cluster(15), original multiplicities, periodic lifts and h1/h2 own-factor inequality(11); no new residue primitivity assumption. |
| dependency | [Actual global residual income](Yin_C_G0191_v2.md#statement) | Residual6/11 norm for the constant canonical branch and exact original input domain. |
| dependency | [Exact residual valuations](Yin_C_G0178_v1.md#statement) | G=3C,5A=e+2C and unramified impossibility under both residual equations. |
| dependency | [Original integral trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Exact fields, values and coefficientwise divided remainders. |
| dependency | [Scalar normalization and Kronecker source](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing Jensen/leading-coefficient and finite circle-zero conventions, plus the exact product-with-multiplicities measure-one characterization at its recorded inspection scope. |
| support | [Inputs, contributions and limits](#inputs-and-boundaries) | Full old/new author roles and comparison boundaries, no independent author review, no degree-at-least-three or unrestricted conclusion. |
| review | [Whole quadratic-canonical finding](../audits/reviews/Yin_R_G0472_v1.md#quadratic-canonical-extension-whole-independent-finding) | Entire eight-section actual proof and all inputs, unchanged v1 portion explicitly reused at its actual scope, complete new quadratic classification, local multiplicities and original norm/measure payment; no contributor self-review. |

