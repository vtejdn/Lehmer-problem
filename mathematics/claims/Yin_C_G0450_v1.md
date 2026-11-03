---
author: Yin
---

# Complete cyclic-layer averaging and actual aggregate normalization controls

The complete necessary original D54 mathematical proof is retained from [L188](../ledger/Yin_L_G0188_v1.md#retained-cyclic-layer-spreading-argument).
The arithmetic author supplied the deductions; the coordinator assigned the broad income question and received progress summaries without supplying them.
The entire original whole finding retains its exact mathematics, day precision and unknown initial independent-review relationship in [R669's later comparison](../audits/reviews/Yin_R_G0669_v1.md#l188-r87-and-r802).
Generic progress/shared-context descriptions do not establish actual initial target mathematics or isolation.
The exact original [derivation and listed author-check account](../audits/reviews/Yin_R_G0087_v1.md#cyclic-layer-original-author-check-finding) remains SELF at its recorded component scope.
The accepted Xyl11 theorem is reused solely at its existing least-prime statement/applicability depth.
No source/PDF proof inspection, mathematical program/J, prime search, factorization, native execution or research Task/E is added.

## Statement

Let alpha be any nontorsion algebraic unit of degree d>=2, with irreducible monic minimal polynomial P, K=Q(alpha) and positive full logarithmic Mahler measure m=log M(P).
All logarithms are natural.
Retain the original field K and degree d even when a power alpha^n has smaller degree.
For all integers n,r>=1 put

    C_n=|Norm_(K/Q)(alpha^n-1)|,
    D_r=|Norm_(K/Q)(Phi_r(alpha))|.

These are positive integers, and C_n=product_(r|n)D_r.
For any finite set S of rational primes, including the empty set and allowing dependence on the input and window, define

    B_S(r)=log(D_r)_S>=0,
    A_S(n)=log(C_n)_S=sum_(r|n)B_S(r),
    F_S(X)=sum_(1<=r<=X)B_S(r)/r, integer X>=1.

Every actual cyclotomic factor layer is counted once.
Bad primes, repeated factor contributions, all initial depths and old lift layers are included.
Then

    F_S(X)/2 <= (1/X)sum_(n=1)^X A_S(n)
              =sum_(r=1)^X B_S(r)floor(X/r)/X <=F_S(X),
    max_(1<=n<=X)A_S(n)>=F_S(X)/2,
    F_S(X)<=2max_(1<=n<=X)A_S(n).

The same finite divisor inequalities hold for certified nonnegative b_r<=B_S(r) and A_b(n)=sum_(r|n)b_r.
To interpret A_b as certified income, these must be identified disjoint actual factor-layer lower masses; unrelated overlapping lower certificates cannot be added as new norm mass.
For each fixed eta,C>0, X<=Cd and F_S(X)>=eta d give some1<=n<=Cd with A_S(n)>=eta d/2 and hence the complete general-unit criterion's positive m lower bound depending only on eta,C.
Consequently

    F_S(X)=o(d) uniformly over1<=X<=Cd and every finite S
    as m tends to zero among nontorsion algebraic units.

This also covers the finite union of all primes dividing the D_r in the window, so it holds for the complete masses B(r)=log D_r.
It asserts no existence of a sequence with m tending to zero and supplies no positive-linear near-one layer coverage.

For any finite nonnegative time weights lambda_n with positive total,

    max_(n<=X)A_S(n)
       >=sum_(n<=X)lambda_n A_S(n)/sum_(n<=X)lambda_n.

The denominators are X for unweighted time and H_X=sum_(n<=X)1/n for harmonic time.
A positive-linear lower bound on either unnormalized numerator alone does not give a fixed positive-linear single-time lower bound.
The following two actual reciprocal irreducible unit families realize both losses.

First, the following exact reciprocal lifting lemma holds for every even d=2s>=2 and every odd prime p.
For any prescribed monic degree-s trace polynomial T_0 modulo p^2, coefficientwise CRT yields a monic integer T with

    T=T_0 modulo p^2,
    T=(x-2)^s+2 modulo4,
    P(t)=t^sT(t+t^-1).

Then P is monic reciprocal of degree d with constant term one, and

    P(t+1)=t^d+2(t+1)^s modulo4.

Eisenstein at two proves irreducibility.
Adding a multiple of4p^2 to the trace constant preserves these facts and can make P(1)=T(2)>2^d, proving nontorsion without a near-one measure bound.

For the good-prime exact-depth specification choose s disjoint inverse pairs{a_i,a_i^-1} in F_p^*, with a_i^2!=1.
Their traces b_i=a_i+a_i^-1 are distinct and the corresponding split reciprocal reduction is squarefree.
For any selected subset I of these pairs with p>|I|, one common added trace constant pc modulo p^2 avoids at most|I| forbidden residues.
It forces v_p(T(theta_i))=1 at every selected trace of the unique r_i-th root-of-unity lift, where r_i is the residue order of a_i.
The simple-root trace and root-of-unity differences are p-adic units, so every selected lifted root and its inverse has exactly

    v_p(alpha_i^r_i-1)=1.

The squarefree full split reduction makes p prime to disc(P); its d lifted roots are precisely all original norm factors.

For every sufficiently large even d, choose

    k=ceil(sqrt(d/log d)),
    r_j=d-k+j, 1<=j<=k,
    Q=lcm(r_1,...,r_k).

The primewise consecutive-integer proof gives

    ((d-k+1)/k)^k<=Q<=d^k.

By the already accepted Xyl11 statement, after enlarging its absolute effective constant C_*>=1 there is a prime p congruent to1 modulo Q with

    Q<p<=C_*Q^5.18,
    k log((d-k+1)/k)<log p<=log C_*+5.18k log d.

Eventually p>d(d+1)/2+d+1.
Choose one inverse pair of exact order r_j per j, then fill the remaining d-2k roots by disjoint inverse pairs of order greater than d.
The displayed root count supplies enough such fillers.
Apply the lift and exact depth-one prescription to the k selected pairs.
This constructs actual irreducible reciprocal nontorsion polynomials P_d of degree d with good prime p_d and, for every1<=n<=d, the exact full selected p-part

    A_p(n)=v_p(C_n)log p
          =2log p if n is one of r_1,...,r_k,
           0 otherwise.

Thus

    sum_(n<=d)A_p(n)=2k log p,
    max_(n<=d)A_p(n)=2log p=O(sqrt(d log d))=o(d),
    liminf_(d->infinity,d even)[sum_(n<=d)A_p(n)]/d>=1,
    F_p(d)=2log p sum_(j=1)^k1/r_j=O(1).

In particular the unweighted total is at least d/2 eventually, while no fixed positive-linear single-time conclusion follows from that local total.
This is the entire p-part, rather than a floor hiding larger selected-prime income.

For a second family let d tend to infinity through even integers and put

    b=ceil(d/(log d log2)), Q=2^b.

Choose p congruent to1 modulo Q by the same accepted statement.
Then

    d/log d<=log Q<d/log d+log2,
    log Q<log p<=log C_*+5.18log Q,
    log p=Theta(d/log d).

Again p exceeds the quadratic filler threshold eventually.
Prescribe the reciprocal reduction with double root one and s-1 disjoint inverse filler pairs of orders greater than d.
Choose the trace lift with T(2)=p modulo p^2 and apply the same CRT/Eisenstein/nontorsion construction.
This prime is explicitly bad for the polynomial discriminant.
The exact norm convention gives v_p(C_1)=1.
At every prime ideal over p, only residue one returns in1<=n<=d<p.
For it, (alpha^n-1)/(alpha-1) is a local unit reducing to n, including in ramified completions.
Hence

    v_p(C_n)=1 for every1<=n<=d,
    max_(n<=d)A_p(n)=log p=Theta(d/log d)=o(d),
    sum_(n<=d)A_p(n)/n=(log p)H_d,
    liminf_(d->infinity,d even)[(log p)H_d]/d>=1.

Dividing by H_d recovers exactly log p.
In this window cyclotomic inversion gives B_p(1)=log p and B_p(r)=0 for2<=r<=d, so F_p(d)=log p=o(d).

Both constructions keep original degree, reciprocity, irreducibility, nontorsion and exact local norms.
They leave Mahler measures and all other-prime contributions uncontrolled.
They refute only the specified aggregate-to-single deductions based on the supplied p-part, without a near-one premise.
They are neither near-one counterfamilies nor counterexamples about complete all-prime income or the Mahler gap.
No coverage of F_S(Cd)>=eta d on a near-one class, improved original-law spectral estimate or new research execution is supplied.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:55 |
| status | open |
| reason | Retain the complete actual cyclotomic-layer averaging and both exact reciprocal unit normalization controls, including full original-field degrees/local depths, accepted least-prime statement cost, reciprocal irreducible realization, all asymptotic constants and uncontrolled-measure/other-prime limitations. Complete actual current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire layer and actual-control theorem](#statement) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| argument | [Complete original proof of every implication](#argument) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| dependency | [Complete original norm and local valuation interface](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original degree-d field norm, every prime ideal/residue-degree multiplicity and ramified valuation accounting, without assuming good reduction or preservation of powered degree. |
| dependency | [Complete actual cyclotomic-layer factorization](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) | Exact C_n product over D_r and prime-by-prime Mobius inversion, including every bad prime/initial depth/old layer; unrelated overlapping lower bounds cannot be counted twice. |
| dependency | [Complete general-unit finite income implication](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Uniform original log C_n=o(d) for n<=Cd as full m tends to zero, including actual powered-degree drops and the finite positive eta,C cost. This is a conditional income-to-measure interface, not arithmetic coverage. |
| dependency | [Accepted Xylouris least-prime statement](../audits/literature/Xyl11/Yin_U001.md#xyl11-u001) | Only the already accepted absolute effective bound P(a,Q)<=C_*Q^5.18 for coprime positive a,Q, applied here solely with a=1,Q>=2 and Q<p. Statement/substitution depth is retained; the analytic proof is not newly inspected or re-audited and no least prime is searched. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:58 |
| status | proved |
| reason | Adopt after actual complete current self-check of every original-field cyclotomic layer/floor/finite-cost/uniform-small-measure implication, exact time normalization, reciprocal CRT/Eisenstein and nontorsion realization, selected simple-root exact depth and full good-prime norm contribution, consecutive-lcm/least-prime/filler-root bounds and all asymptotics, and the separate discriminant-bad harmonic family with ramified-safe valuation and every near-one/other-prime limitation. No substantive defect or missing hypothesis was found. The current authored whole SELF does not close original R87 whole UNKNOWN or enlarge its exact derived/listed author SELF; no new source proof, prime search, producer execution or arithmetic coverage is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| argument | [Exact retained argument](#argument) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original degree-d field norm, every prime ideal/residue-degree multiplicity and ramified valuation accounting, without assuming good reduction or preservation of powered degree. |
| dependency | [Exact retained dependency](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) | Exact C_n product over D_r and prime-by-prime Mobius inversion, including every bad prime/initial depth/old layer; unrelated overlapping lower bounds cannot be counted twice. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Uniform original log C_n=o(d) for n<=Cd as full m tends to zero, including actual powered-degree drops and the finite positive eta,C cost. This is a conditional income-to-measure interface, not arithmetic coverage. |
| dependency | [Exact retained dependency](../audits/literature/Xyl11/Yin_U001.md#xyl11-u001) | Only the already accepted absolute effective bound P(a,Q)<=C_*Q^5.18 for coprime positive a,Q, applied here solely with a=1,Q>=2 and Q<p. Statement/substitution depth is retained; the analytic proof is not newly inspected or re-audited and no least prime is searched. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0655_v1.md#current-cyclic-layer-whole-finding) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. Actual current whole relationship is self-reviewed; original whole UNKNOWN and exact listed author SELF remain separate. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:54 |
| status | proved |
| reason | Adopt R669 after complete coordinator reading of the new isolated whole C450 finding, covering all original-field all-prime/all-depth layers and finite-income interfaces, both exact local normalization families, accepted theorem applicability and every other-prime/measure/coverage limitation. Preserve R87 whole UNKNOWN, original/current SELF and source/prime-search limits; no new arithmetic coverage or execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| argument | [Exact argument](#argument) | Entire original D54 mathematical Inputs/Sections1--5/equations(1)--(17), with original Section6 checking/source/contribution boundaries retained separately: any nontorsion algebraic unit/original degree-d field/full Mahler m/all finite input-and-window-dependent prime sets/all integer X>=1/every bad prime and depth, exact cyclotomic divisor layers/floor factors and certified disjoint lower masses/finite eta,C criterion/uniform o(d) without assumed near-one sequence, actual time-weight denominator; every even-degree reciprocal CRT/Eisenstein/nontorsion realization and selected simple-root p-adic exact-depth hypothesis, full primewise consecutive-lcm proof/accepted Xyl11 least-prime bit-length bound/filler roots/exact good-prime income and liminf/O(1)/o(d) scales, separate explicit polynomial-discriminant-bad endpoint family/ramified-safe ideal norms/harmonic loss/full first-layer inversion. Both counterexamples concern only the supplied selected p-part; uncontrolled Mahler measures and other primes do not refute near-one or full-income coverage. No prime search, mathematical producer, new source proof or Task execution occurs. |
| dependency | [Exact dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Original degree-d field norm, every prime ideal/residue-degree multiplicity and ramified valuation accounting, without assuming good reduction or preservation of powered degree. |
| dependency | [Exact dependency](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers) | Exact C_n product over D_r and prime-by-prime Mobius inversion, including every bad prime/initial depth/old layer; unrelated overlapping lower bounds cannot be counted twice. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Uniform original log C_n=o(d) for n<=Cd as full m tends to zero, including actual powered-degree drops and the finite positive eta,C cost. This is a conditional income-to-measure interface, not arithmetic coverage. |
| dependency | [Exact dependency](../audits/literature/Xyl11/Yin_U001.md#xyl11-u001) | Only the already accepted absolute effective bound P(a,Q)<=C_*Q^5.18 for coprime positive a,Q, applied here solely with a=1,Q>=2 and Q<p. Statement/substitution depth is retained; the analytic proof is not newly inspected or re-audited and no least prime is searched. |
| review | [Exact review](../audits/reviews/Yin_R_G0669_v1.md#cyclic-layer-whole-independent-finding) | Complete exact C450v1 Statement and Argument, all equations1--17, every actual cyclotomic layer/depth/local construction/finite criterion and both full-cost negative controls at declared source scope. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-cyclic-layer-spreading-argument"></a>
<a id="cyclic-layer-spreading-fixed-scope"></a>

### Inputs and source boundary

The actual norm and valuation conventions are those of [complete original norm interface](Yin_C_G0256_v1.md#content-versus-ideal-norm), with the exact cyclotomic layers of [complete cyclotomic local layers](Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers).
The already fixed [complete automatic-floor and average interface](Yin_C_G0376_v2.md#automatic-lift-average-capacity) averages first-layer and automatic lifting floors, proves the short-order capacity obstruction and gives an actual isolated-return control showing that a successful single exponent need not fill an average screen.
The present converse-direction controls concern large supplied aggregates that fail to give a large single exponent.
They are not another computation on those old inputs.
The complete [existence-only weighted ceiling](Yin_C_G0361_v1.md#joint-circle-existence-floor-ceiling) remains separate: here the local valuations used in the controls are exact, not just a one-witness order floor.

One previously accepted external input is used solely to construct the examples with a controlled prime bit length.
[Xyl11-U001](../audits/literature/Xyl11/Yin_U001.md#xyl11-u001) accepts: for coprime positive integers a,Q, the least prime p congruent to a modulo Q satisfies p<=C_* Q^5.18 for an absolute effective C_*.
We may enlarge C_* to be at least one.
The source statement and applicability were checked in that retained audit; its analytic proof is not re-audited here.
Every application below has a=1, Q>=2, so gcd(a,Q)=1 and

    Q<p<=C_* Q^5.18.                                  (1)

No least-prime search is claimed.
No new literature theorem is adopted.

<a id="complete-cyclic-layer-average"></a>
### 1. The exact sufficient aggregate uses cyclotomic layers divided by their index

Let alpha be any nontorsion algebraic unit of degree d, with m=log M(P)>0.
Retain the original degree-d field for

    C_n=|Norm(alpha^n-1)|,
    D_r=|Norm(Phi_r(alpha))|.

They are positive integers and C_n=product_(r|n) D_r.
For a finite set S of rational primes, possibly dependent on the input and the window, put

    B_S(r)=log (D_r)_S>=0,
    A_S(n)=log (C_n)_S=sum_(r|n) B_S(r).

The subscript S denotes the positive integer S-part.
These are exact local masses; bad primes, nonprimitive layers and all initial depths are included.
The cyclotomic factorization adds valuations in disjoint factor layers, so it does not count a whole valuation twice.
For an integer X>=1 define

    F_S(X)=sum_(1<=r<=X) B_S(r)/r.

Finite summation and X/(2r)<=floor(X/r)<=X/r for r<=X give

    (1/2)F_S(X)
       <=(1/X)sum_(n=1)^X A_S(n)
        =sum_(r=1)^X B_S(r) floor(X/r)/X
       <=F_S(X).                                     (2)

In particular

    max_(n<=X) A_S(n)>=F_S(X)/2,
    F_S(X)<=2 max_(n<=X) A_S(n).                       (3)

Exactly the same inequalities hold for arbitrary certified nonnegative lower masses b_r<=B_S(r) if the common-exponent income is defined as sum_(r|n)b_r.
They do not hold for a collection of unrelated lower bounds that have not been identified as disjoint actual factor layers.

For fixed eta,C>0, the hypothesis

    X<=Cd,    F_S(X)>=eta d                           (4)

therefore yields some n<=Cd with A_S(n)>=eta d/2.
The [complete general-unit finite income criterion](Yin_C_G0391_v1.md#general-unit-finite-income-criterion), applied with eta/2, supplies a positive measure lower bound depending only on eta,C.
Equivalently, C391 implies

    F_S(X)=o(d) uniformly for X<=Cd and every finite S
    as m tends to zero.                              (5)

Indeed A_S(n)<=log C_n and its uniform o(d) estimate applies before(3).
The same conclusion holds when S contains every prime dividing the finitely many D_r, r<=X, and hence for the complete B(r)=log D_r.
No hypothetical near-one family is assumed to exist.
Neither(4) nor new arithmetic coverage of it is proved here.
Formula(2) is an exact extension of the already retained first-layer averaging mechanism to all actual layers, not a new source of mass.

For contrast, an arbitrary nonnegative time weighting lambda_n supplies only

    max_(n<=X) A_S(n)
       >=[sum_(n<=X)lambda_n A_S(n)]/[sum_(n<=X)lambda_n]
                                                               (6)

when its denominator is positive.
For unweighted times the denominator is X; for lambda_n=1/n it is H_X=sum_(n<=X)1/n.
A lower bound eta d on an unnormalized numerator does not itself give eta' d for fixed eta'>0.
The next sections show that both missing normalization losses occur in genuine irreducible reciprocal local norm sequences.
They are not artifacts of arbitrary real arrays.

<a id="reciprocal-local-realization-lemma"></a>
### 2. A local specification can be lifted without losing irreducibility

Fix even d=2s>=2 and an odd prime p.
Let a monic trace polynomial T_0 in(Z/p^2 Z)[x] of degree s be prescribed.
Coefficientwise Chinese remaindering produces a monic integer T of degree s satisfying

    T=T_0 modulo p^2,
    T=(x-2)^s+2 modulo 4.

Put P(t)=t^s T(t+t^(-1)).
This is an integer monic reciprocal polynomial of degree d with constant term one.
Its translated polynomial satisfies

    P(t+1)=t^d+2(t+1)^s modulo 4.

Consequently every nonleading coefficient is even and its constant coefficient is two modulo four.
Eisenstein at two proves that P(t+1), and therefore P, is irreducible over Q.
This conclusion does not depend on how T_0 factors modulo p.

One may still add any multiple of 4p^2 to the constant coefficient of T.
This preserves both congruences and irreducibility.
Choose that multiple so P(1)=T(2)>2^d.
If every root of P were on the unit circle, their product formula at one would give |P(1)|<=2^d, a contradiction.
In particular its root alpha is a nontorsion algebraic unit.
This choice supplies no upper Mahler bound: coefficients can be tall, and no near-one conclusion is intended.

Here is the good-prime depth prescription needed in Section3.
Suppose over F_p we first select s inverse pairs {a_i,a_i^(-1)} of nonzero elements, with a_i distinct from its inverse and with all pairs disjoint.
The trace values b_i=a_i+a_i^(-1) are distinct, and

    Tbar(x)=product_(i=1)^s(x-b_i),
    Pbar(t)=product_(i=1)^s(t-a_i)(t-a_i^(-1))       (7)

is squarefree.
Let I be a selected subset of the pairs; for i in I prescribe the residue order r_i of a_i.
Then p does not divide r_i.
There is a unique r_i-th root of unity zeta_i in Z_p reducing to a_i, since its equation has nonzero derivative modulo p.
Put theta_i=zeta_i+zeta_i^(-1).
Begin with any monic integer lift T_base of Tbar, and consider T_base+p c modulo p^2, c in F_p.
For each i in I,

    [T_base(theta_i)+p c]/p modulo p

is an affine function of c with coefficient one.
At most |I| values of c are forbidden by asking that none of these expressions vanish.
Thus if p>|I|, a choice makes v_p(T(theta_i))=1 at every selected pair, and the preceding CRT lift preserves it.

For clarity, this is precisely a norm depth-one specification.
By simple-root lifting, each a_i lifts to a unique root alpha_i of P in Z_p, and its trace z_i=alpha_i+alpha_i^(-1) is the root of T lifting b_i.
The identities

    T(theta_i)-T(z_i)=(theta_i-z_i)U_i,
    z_i-theta_i=(alpha_i-zeta_i)(1-1/(alpha_i zeta_i))

have p-adic unit factors U_i and 1-1/(alpha_i zeta_i), because Tbar'(b_i)!=0 and a_i^2!=1.
Also (alpha_i^r_i-1)/(alpha_i-zeta_i) is a p-adic unit, its reduction being r_i a_i^(r_i-1).
Therefore

    v_p(alpha_i^r_i-1)=v_p(T(theta_i))=1.           (8)

The inverse root has the same valuation.
Squarefreeness of(7) implies p does not divide disc(P), so its d lifted roots are precisely the d original factors in the norm and their valuations are added once.
This proves the exact local-depth claim without assuming an unexplained excess or attributing a full resultant floor to C_n.

<a id="actual-incompatible-order-aggregate"></a>
### 3. A good-prime actual linear aggregate with no linear single income

For every sufficiently large even d choose

    k=ceil(sqrt(d/log d)),
    r_j=d-k+j,  1<=j<=k,
    Q=lcm(r_1,...,r_k).

These k orders lie in(d/2,d], and 2k<=d.
Since k>=2, Q is even.
The elementary bounds

    ((d-k+1)/k)^k<=Q<=d^k                         (9)

will control the prime in(1).
Here is a proof of the lower bound.
For each prime ell choose one of the k consecutive integers with maximum ell-adic valuation, at position j.
For every other position i, its ell-adic valuation is at most that of |i-j|: both integers are divisible by the smaller prime power.
Hence the product of all k integers divided by their least common multiple has ell-adic valuation at most that of (j-1)!(k-j)!, which is at most that of (k-1)! by binomial integrality.
Applying this primewise gives product r_j <=Q(k-1)!<=Q k^k.
This proves(9).

Use the accepted least-prime statement with a=1 and this Q.
Then p is odd, every r_j divides p-1, and

    k log((d-k+1)/k)<log p
          <=log C_*+5.18 k log d.                  (10)

In particular log p grows faster than log(d^2); therefore p>d(d+1)/2+d+1 for all sufficiently large d.
In F_p^*, choose one element a_j of exact order r_j for each j and include its inverse.
Such elements exist because F_p^* is cyclic and r_j divides p-1.
These pairs are distinct and neither member equals its inverse.

Fill the remaining d-2k roots by disjoint inverse pairs of order greater than d.
There are enough: in any algebraic closure, at most sum_(r<=d)phi(r)<=d(d+1)/2 elements have order at most d, whereas F_p^* has p-1 elements.
Elements of order greater than d have no fixed point under inversion for d>=2.
Inequality(10) consequently leaves more than d available such elements.
The resulting polynomial Pbar is squarefree, monic and reciprocal of degree d as in(7).

Apply Section2 with I consisting of the k selected pairs and impose depth one at each, using p>k.
This gives an actual irreducible reciprocal nontorsion integer polynomial P_d of degree d, with this good prime p=p_d and these exact root orders and depths.
Define its actual local income A_p(n)=v_p(C_n)log p.
For all 1<=n<=d the exact answer is

    A_p(n)=2log p  if n is one of r_1,...,r_k,
           0      otherwise.                        (11)

Indeed a residue root can contribute only if its order divides n.
A selected order r_j>d/2 has no multiple other than itself in this window; every filler order exceeds d.
At n=r_j, only its two roots contribute and each has valuation one by(8).
No unrecorded higher depth or old lift occurs in this window, because p>d and every selected return has its original order.
Equation(11) gives the full p-part, not a lower floor.

It follows that

    sum_(n<=d) A_p(n)=2k log p,
    max_(n<=d) A_p(n)=2log p=O(sqrt(d log d))=o(d),
    liminf_(d->infinity, d even)
        [sum_(n<=d)A_p(n)]/d >=1.                  (12)

For the last inequality use k^2 log d/d tending to one and log((d-k+1)/k)/log d tending to one half in the lower bound(10).
Thus for all sufficiently large even d the total is at least d/2.
Every sequence assertion refers to these constructed actual degree-d units; the common implicit constant uses only the fixed accepted C_*.

There is no conflict with the sufficient layer criterion.
At p, within this window the only nonzero B_p(r) are B_p(r_j)=2log p.
Consequently

    F_{p}(d)=2log p sum_(j=1)^k 1/r_j
              <=2k log p/(d-k+1)=O(1),             (13)

while (2)'s mean equals 2k log p/d=O(1).
The factor r in the sufficient weighted layer mass removes the apparently large raw aggregate.
In particular no positive uniform eta' follows in max A_p(n)>=eta' d merely from sum A_p(n)>=d/2, even in the actual reciprocal irreducible good-prime domain.
The theorem says nothing comparable about omitted primes or the complete log C_n, and the example is not a near-one Mahler sequence.

<a id="actual-harmonic-time-normalization-loss"></a>
### 4. An actual harmonic time aggregate loses a logarithm

For a second family let d tend to infinity through even integers and set

    b=ceil(d/(log d log2)),    Q=2^b.

Choose p congruent to one modulo Q by(1).
Then p is odd and

    d/log d<=log Q<d/log d+log2,
    log Q<log p<=log C_*+5.18 log Q.                (14)

Thus log p=Theta(d/log d), and again p>d(d+1)/2+d+1 eventually.
Choose the reciprocal reduction

    Pbar(t)=(t-1)^2
           product_(i=1)^(s-1)(t-a_i)(t-a_i^(-1)),

where all the disjoint filler pairs have orders greater than d.
The same counting as above supplies them.
Its trace polynomial is (x-2) product_i(x-b_i), with distinct b_i, all different from2.
In an integer lift T_base, T_base(2) is divisible by p.
Choose a constant p c so that

    T_0(2)=p modulo p^2.

Section2's CRT/Eisenstein construction now supplies an actual irreducible reciprocal nontorsion P_d with this specification.
In contrast to Section3, p is a discriminant-bad prime because its reduction has the double root one; this is allowed in C256's exact norm convention.
Since C_1=|P_d(1)|=|T(2)|,

    v_p(C_1)=1.                                    (15)

At every prime ideal q above p, a residue order can contribute for n<=d only if it is one: all other specified orders exceed d.
For an element u congruent to one modulo q and an integer n with p not dividing n, (u^n-1)/(u-1) is a q-adic unit, reducing to n.
This applies in ramified completions as well.
Since n<=d<p, its ideal valuation at every returning prime q therefore agrees with the one at n=1; all other prime ideals above p contribute zero.
The exact original-field norm valuation gives

    v_p(C_n)=v_p(C_1)=1 for every 1<=n<=d.           (16)

No unramifiedness, power-basis factorization formula or separate residue-degree count was inserted into this step.
It uses only the residue orders and the original ideal norm identity.
The p-part income is exactly the constant A_p(n)=log p throughout the window.
Hence

    max_(n<=d) A_p(n)=Theta(d/log d)=o(d),
    sum_(n<=d) A_p(n)/n=(log p)H_d,
    liminf_(d->infinity, d even)
      [(log p)H_d]/d >=1.                            (17)

The elementary integral comparison log(d+1)<=H_d<=1+log d proves the last assertion using(14).
Thus a positive-linear unnormalized harmonic time aggregate also fails to imply positive-linear single income in this actual class.
Dividing by H_d in(6) gives exactly log p and exposes the missing logarithm.
Within the same window, (16) and cyclotomic inversion give B_p(1)=log p, B_p(r)=0 for2<=r<=d, so F_p(d)=log p=o(d), again consistently with(2)--(4).

### 5. Consequence for the next arithmetic bridge

There are three distinct objects: unweighted total income over many times, an unnormalized harmonic time aggregate, and the reciprocal-index sum of disjoint actual cyclotomic layers.
Only the last of these has the degree-scale transfer(2) without an X or H_X denominator.
Exact local depth and reciprocity alone do not repair the two weaker statements; Sections3--4 realize their losses in actual irreducible units and exact norm valuations, including good and bad prime boundaries separately.

The examples deliberately leave Mahler measure uncontrolled, and their construction may introduce large unrelated prime income.
They do not refute a theorem using a genuinely near-one premise to force a stronger distribution, a certificate with other primes, or the Lehmer gap.
In particular they cannot be used to contradict(5).
Their role is to reject two aggregate-only bridges before an attempted near-one coverage proof silently drops the normalization.
No result here forces actual F_S(Cd)>=eta d on the unrestricted near-one class.

A useful next arithmetic target would establish concentration of full layer mass toward affordable return orders with enough reciprocal-index weight, or another genuine common-exponent gain that survives these exact spreading and endpoint mechanisms.
The current analysis does not recommend a larger fixed-prime scan, automatic-depth extension, or optimizing the already retained finite-income constants.
Those steps do not supply the missing near-one distribution theorem.

## Exact original contribution and current limits

The original author derived and checked the full layer identity, reciprocal realization, lcm estimate, p-adic depths, both actual families and their asymptotics.
The entire original six-section whole R87 account and the1429-character original derivation/listed self-check account remain at their actual scopes and day precision.
Generic shared context/progress summaries do not establish either initial isolation or known prior substantive target mathematics; that whole independent-review obligation stays UNKNOWN.
The two exact selected-prime counterexamples preserve their good-prime versus polynomial-discriminant-bad distinction and cannot be enlarged into near-one or full-prime counterexamples.
All necessary proofs remain here, while the speculative next mechanism and historical research state remain in the fixed original input.
This retention performs no new source proof audit, producer run, prime search, factorization or Task/E transition.
