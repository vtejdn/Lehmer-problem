---
author: Yin
---
# Integer Frobenius lifts, rank-one degeneration and the true determinant cost

Human author Yin.
New G0001 author inquiry by g_bridge_audit.
Root is a substantive proof contributor: it proposed the canonical rank-one defect, U=U0+pV and scalar-perturbation nonvanishing, then separately supplied the sharper k^(d-1)(kD+H) factorization and +/-1 choice.
The author checks these statements and investigates their actual algebraic and analytic content.
This author owns this new D and any separately declared J.
No new native computation is allocated or run.

## Exact question and reuse

For an ACTUAL nontorsion integer unit alpha with monic irreducible P of original degree d, use its actual companion matrix A in the basis1,alpha,...,alpha^(d-1).
Can a single integer matrix U reducing to Frobenius yield a useful d by d determinant det(A^p U-U A), retaining all integer-lattice and complex-embedding costs and avoiding the full pair-orbit multiplicity of L397?
An integer matrix determinant is not automatically the norm of an original-field element.
Nonzero existence alone is insufficient; distinguish a new usable quantity from an old cyclic or coefficient-Gram expression.

Read [L55's exact coefficient-space ceiling](../ledger/Yin_L_G0055_v1.md#coefficient-subspace-optimum), [L56's full projection cancellation](../ledger/Yin_L_G0056_v1.md#projection-cost-identity), [L63's canonical integral Frobenius lift and primitive rank-d summand](../ledger/Yin_L_G0063_v1.md#frobenius-intertwiner-floor), and [L64's actual unramified Frobenius construction](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift).
L63 already retains the canonical integral lift, but its full Sylvester determinant is a rank-d^2 operator which reduces to the old resultant.
L55--56 control every coefficient lift at a fixed window, not only their displayed prime generators.
L64's good-prime automorphism is not assumed in the integral calculation below.
[L397](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) already excludes free removal of the class cost by positive products over every local lift.
No new external theorem is needed for the direct matrix identities; any recognized new source mechanism will be checked before use.

<a id="statement"></a>
In the exact actual-unit setting above, the canonical lift has the rank-one defect(2) at every prime.
One of the two scalar perturbations V=+I,-I always gives a nonzero d by d determinant, with the exact cyclic/trace factorization(5).
Every commuting integer perturbation has the stronger full-commutant factorization(6).
For arbitrary integer V, the actual integer column lift(7)--(8) has N=pd and the old L56 bound gives(9), cancelling the mandatory p^d factor with its coefficient-volume cost.
The integer affine coset has the exact old-cokernel class(12), of additive order p; relaxing V to Q deletes the restriction and gives every rational matrix.
The actual reciprocal control(13)--(14) has a unimodular U and exactly the mandatory p^d determinant, with normalized determinant1 despite old base quotient norm4.
Sections7--8 retain the complete coefficient and embedding costs, show what is and is not reduced, and specify the unresolved noncommuting/analytic route.
No statement proves a gap or a uniform extra determinant divisor.

<a id="argument"></a>
The full argument is Sections1--8, formulas(1)--(19), including the actual control and precise comparison with the old projection theorem.
The root's rank-one/scalar contributions and this author's trace, commutant, affine-module and cost extensions are distinguished at the end.
No native mathematical computation is used.

<a id="canonical-lift-rank-one"></a>
## 1. Canonical lift and exact affine defect

Write P(t)=t^d+sum_(j=0)^(d-1)c_j t^j.
Let e_j denote the actual power-basis column and ell=e_(d-1)^T.
Then A e_j=e_(j+1) for j<d-1 and A e_(d-1)=-sum_j c_j e_j.
For a rational prime p define U0 by

    U0 e_j=A^(pj)e_0, 0<=j<d,
    rho_p(t)=rem_P P(t^p)/p in Z[t],
    q=rho_p(A)e_0.                                     (1)

The remainder integrality and nontorsion nonvanishing are the adopted L63/L59 interfaces.
The first d-1 columns of A^p U0-U0 A cancel.
Its last column is P(A^p)e0=pq.
Hence

    A^p U0-U0 A=pq ell.                                (2)

This is the canonical rank-one defect, at ALL primes including nonreduced reductions.
In the actual integer-unit domain d>=2, so its determinant is zero.
Reduction of U0 is the Frobenius endomorphism of F_p[t]/Pbar; no invertibility is assumed when the reduction is nonreduced.

Every integer matrix in that SAME Frobenius residue class is U=U0+pV with V in M_d(Z), and then

    A^p U-U A=p C(V),
    C(V)=q ell+A^p V-V A in M_d(Z).                    (3)

Thus a nonzero det C(V) gives the original integer determinant divisible by p^d.
It is not yet a nonzero field norm, and no height or operator-norm control on U0 or V follows from(3).

<a id="scalar-rank-one-reduction"></a>
## 2. Scalar perturbations reduce to two terms

Put M=A^p-A, Delta=det M=Norm_K(alpha^p-alpha)!=0.
This is the old cyclic norm times the signed unit norm.
For V=kI the elementary rank-one determinant expansion gives

    det C(kI)=k^(d-1)(k Delta+H),
    H=ell adj(M)q in Z.                               (4)

The identity follows by multilinearity in the columns: two columns from q ell are dependent, so only zero or one such column contributes.
Since Delta!=0, k=1 and k=-1 cannot both make the second factor zero.
Thus one of those two bounded perturbations has nonzero determinant, sharpening the general degree-d interpolation argument without a growing k.
This is existence only; the canonical U0 and the embedding/basis costs remain.

The author obtains a further exact identification of H.
Since M commutes with A and A^p, taking a trace in(2) after left multiplication by M^(-1) gives

    p ell M^(-1)q
      =Tr[M^(-1)(A^p U0-U0 A)]
      =Tr[U0 M^(-1)(A^p-A)]
      =Tr U0.

Consequently

    p H=Delta Tr U0,
    det(A^p(U0+pkI)-(U0+pkI)A)
       =p^(d-1) k^(d-1) Delta(pk+Tr U0).               (5)

Every trace here is the ordinary trace of the full d by d rational matrix, not an unlabelled smaller-field trace.
H is integral from(4), so(5) also records p dividing Delta Tr U0; no division by p is treated as free.
The scalar determinant therefore factors into the OLD cyclic norm and an explicit canonical-lift trace factor.
Its actual new arithmetic content, coefficient expense and relation to general noncommuting V are the next issue.

<a id="all-commuting-perturbations"></a>
## 3. Every commuting integer perturbation has the same cyclic factor

The scalar reduction extends to the ENTIRE integer commutant of A.
If V commutes with A, its first column is v(A)e0 for a unique integer polynomial v of degree<d; its other columns are A^j V e0=v(A)e_j.
Hence V=v(A).
Conversely every such V commutes.
No larger rational commutant or maximal-order multiplier is substituted for this exact original power-basis condition.

Since adj(V) also commutes with A and M, the rank-one expansion and cyclicity of trace give

    p det C(V)=Delta[p det V+Tr(U0 adj(V))],
    det(A^p U-U A)
       =p^(d-1) Delta[p det V+Tr(U0 adj(V))],
                   U=U0+pV, AV=VA.                    (6)

For verification, det(MV+q ell)=Delta det V+ell adj(V)adj(M)q.
Multiply the second summand by p and use(2):

    p ell adj(V)M^(-1)q
      =Tr[adj(V)M^(-1)(A^p U0-U0 A)]
      =Tr[U0 adj(V)M^(-1)(A^p-A)]
      =Tr(U0 adj(V)).

This proves(6) without assuming V invertible; the adjugate identity remains valid when det V=0.
Thus every commuting perturbation carries the SAME old cyclic norm Delta, times the explicit integer trace/adjugate factor in(6).
That factor may have additional arithmetic, but no universal lower surplus or inexpensive upper bound for it has been proved.
Formula(6) is not a claim that every noncommuting V has the same factor.

<a id="full-original-coefficient-window"></a>
## 4. General V has an exact original coefficient lift; its p-floor cancels in the old projection method

For a general V in M_d(Z), let f_j(t) be its jth column as a polynomial of degree<d.
Define the already integral free-ring polynomial

    delta_p P(t)=[P(t^p)-P(t)^p]/p in Z[t].

Its leading degree-pd terms cancel, so its degree is at most pd-1.
Its evaluation at alpha is q as an element of R, even though it is usually not the reduced rho_p representative.
Put

    h_j(t)=t^p f_j(t)-f_(j+1)(t),       0<=j<d-1,
    h_(d-1)(t)=t^p f_(d-1)(t)+sum_j c_j f_j(t)
                                      +delta_p P(t).   (7)

All these are integer polynomials of degree at most pd-1: p+d-1<=pd-1 for p,d>=2.
Their ORIGINAL power-basis value columns are exactly C(V).
Let N=pd, let R_N be the d by N reduction matrix with columns t^j mod P for0<=j<N, and let Q(V) be the N by d coefficient matrix of(7).
Then

    C(V)=R_N Q(V),
    A^p U-U A=R_N[p Q(V)].                            (8)

This is an actual coefficient representation in a degree-linear window for FIXED p; no matrix determinant has been silently called a field norm.
If det C(V)!=0, Q(V) has full column rank.
Apply the already proved [C226 retained projection identity](Yin_C_G0226_v1.md#projection-cost-identity) with these exact matrices.
Writing G_N=det(R_N R_N^T), it gives

    det(C(V))^2/det(Q(V)^T Q(V))<=G_N,
    det(A^p U-U A)^2/det([pQ(V)]^T[pQ(V)])
       =det(C(V))^2/det(Q(V)^T Q(V))<=G_N.             (9)

In particular the mandatory p^(2d) in the squared determinant is accompanied by EXACTLY the same p^(2d) in the full squared coefficient-volume cost.
That automatic factor supplies no additional certificate after this normalization.
Optimizing arbitrary rational coefficient lifts of the same image recovers exactly G_N, by L56, while actual integer lifts can retain a further projection loss.
This applies to every V, not just the commuting class.

This is a precise limitation of the coefficient/exterior-volume proof mechanism.
It does NOT extend L55's specific Lehmer counterexample to an unproved new subspace, assert that all V lie in the old two-prime coefficient space, or rule out a genuinely arithmetic lower bound for the actual G_N.
The new affine congruence restriction on V is integral information, but any use of it must establish the missing quantitative Gram or coefficient control rather than preserve an independent p^d gain after(9).

<a id="rational-affine-coset-boundary"></a>
## 5. What a rational relaxation deletes

Let S_p(V)=A^pV-VA on M_d(Q).
On passing to the complete complex eigenbasis of A, it multiplies the(i,j) matrix coordinate by alpha_i^p-alpha_j.
Every such number is nonzero by the original nontorsion mixed-exponent argument.
Hence S_p is invertible over Q, and

    {q ell+S_p(V):V in M_d(Q)}=M_d(Q).                (10)

This is an exact description of the relaxed image.
It shows why a real/rational optimization of C alone cannot retain the integer determinant floor: it can make C any arbitrarily small nonzero rational scalar matrix.
The original domain was V in M_d(Z); dropping it is not a harmless change of coordinates.
Clearing a denominator in V also changes the affine q ell term relative to the chosen image and is not an automatic image-preserving repair.

At the integer level the possible C form ONE affine coset

    q ell+S_p(M_d(Z)) subset M_d(Z).                  (11)

The finite cokernel of S_p is the old mixed-resultant module from L63, up to interchanging its two tensor coordinates.
Under the exact coefficient-pairing identification of End_Z(R) with R tensor R, q ell corresponds to q tensor1, and S_p becomes multiplication by x^p-y.
Eliminating y maps(11)'s distinguished class to

    q in R/P(alpha^p)R=R/(p q)R.                     (12)

Its additive order is EXACTLY p.
Multiplication by p kills it, and q cannot equal p q r for r in R, since q!=0 would give1=pr.
Thus C(V) can never be the zero matrix for an integer V, although it can be singular, as the canonical V=0 example shows.
The distinction between a nonzero matrix and a nonzero determinant is essential.
The index of the homogeneous matrix lattice S_p(M_d(Z)) remains the old full mixed resultant; merely expressing it as a coset does not reduce its known analytic cost.

<a id="saturated-reciprocal-control"></a>
## 6. An actual reciprocal input saturates the complete mandatory determinant income

Take P=t^2-3t+1, alpha=(3+sqrt5)/2, d=2,p=2.
It is the actual irreducible reciprocal nontorsion unit already used in L63/C150 controls.
In the basis1,alpha,

    A=[[0,-1],[1,3]], U0=[[1,-1],[0,3]],
    V=-I, U=U0-2I=[[-1,-1],[0,1]],
    C(V)=[[1,0],[-2,1]],
    A^2U-UA=2C(V), det C(V)=1, det(A^2U-UA)=4.        (13)

These identities are obtained by direct2 by2 multiplication.
In particular U itself is unimodular, with determinant-1.
The OLD base quotient is q=2alpha^2, whose norm is4; thus this new normalized determinant can be1 even when the old normalized base Frobenius norm is4.
It does not automatically preserve that extra base income.

For a direct check of the entire coefficient cost, delta_2 P=3t^3-7t^2+3t.
Formula(7) for V=-I gives

    h0=t-t^2, h1=2t^3-7t^2+6t-1,
    Q^T Q=[[2,13],[13,90]], det(Q^T Q)=11.             (14)

The normalized ratio in(9) is1/11, and the raw representation pQ has exactly the same ratio after its p^(2d) scaling.
Reducing the two columns instead to their degree<2 representatives gives1-2t and t, whose coefficient-volume squared is1; that changes the representative and gives the old trivial ratio1, not an independent arithmetic gain.
No numerical approximation, symbolic program, near-one sequence or new universal counterexample is being used.
This fixed positive-measure control rejects a uniform EXTRA determinant divisor for all eligible V or for these bounded scalar/unimodular lifts; it does not reject the possibility of choosing another V with a useful paid estimate on a genuinely small-measure class.

<a id="explicit-column-and-embedding-costs"></a>
## 7. Actual coefficient cost can be bounded without declaring U0 inexpensive

Put L=||P||_1 and S=max_j ||f_j||_1.
For a nonzero determinant S>=1, since V=0 is singular by(2).
The free-ring quotient has

    ||delta_p P||_1<=(L+L^p)/p.

The particular columns(7) therefore obey

    ||h_j||_1<=2S                 for j<d-1,
    ||h_(d-1)||_1<=L S+(L+L^p)/p,
    det(Q^T Q)<=(2S)^(2(d-1))
                            *[L S+(L+L^p)/p]^2.       (15)

The last line follows from the Gram/Hadamard inequality and ||h_j||_2<=||h_j||_1.
In the middle line,1+sum|c_j|=L.
This is a REAL cost saving compared with separately pricing every large remainder column of U0: only the last output column contains delta_p P.
For fixed p and a FIXED bound S<=S0, L<=2^d exp(m(P)) makes the logarithm of the displayed coefficient-volume cost O_(p,S0)(d+m(P)), not an asserted unavoidable O(d^2) cost.
However the raw pQ still has the extra exactly2d log p in its squared-volume logarithm, so this improvement does not undo the cancellation in(9).
There is no assumption that small total m bounds L or U0 uniformly.

For an alternative direct all-root check, let W=(alpha_i^j)_(1<=i<=d,0<=j<d).
It is invertible because P is separable.
Multiplying(8) by W evaluates each original polynomial column at all d original conjugates.
Factoring max(1,|alpha_i|)^(N-1) from row i and applying column Hadamard gives

    |det C(V)| sqrt(|disc P|)
       <=d^(d/2) product_j ||h_j||_1
                                *exp((N-1)m(P)).       (16)

Thus replacing coefficient volume by these individual bounds leaves the genuine discriminant and d log d terms.
The matrix determinant has not been identified with a degree-d field norm in deriving(16); all d evaluations and the Vandermonde determinant remain.

To display the separate embedding obstruction, write tilde(V)=W V W^(-1).
The polynomial of degree<d taking value1 at alpha_j and0 at the other roots is P(t)/[(t-alpha_j)P'(alpha_j)].
Its leading coefficient is1/P'(alpha_j).
Evaluating this polynomial at alpha_i^p and using(1)--(3) gives the exact matrices

    (W U0 W^(-1))_(ij)
       =P(alpha_i^p)/[(alpha_i^p-alpha_j)P'(alpha_j)],
    (W C(V) W^(-1))_(ij)
       =P(alpha_i^p)/[p P'(alpha_j)]
                        +(alpha_i^p-alpha_j) tilde(V)_(ij).
                                                               (17)

Every displayed denominator is nonzero by separability and mixed-exponent nontorsion.
This directly checks the formula, without importing a root-separation estimate.
In particular

    Tr U0=sum_i P(alpha_i^p)
                        /[(alpha_i^p-alpha_i)P'(alpha_i)]. (18)

Even when V has tiny integer entries in the power basis, its conjugate tilde(V) includes W and W^(-1).
A bound for its embedding norm cannot be inferred merely from those integer entries or from Frobenius being a permutation on an auxiliary residue field.
Likewise the local Frobenius eigenvalue picture is not a global complex unitary operator.
Formula(18) retains the actual derivative/separation terms; no favorable cancellation in that trace is claimed without proof.

For comparison, a crude POWER-BASIS operator estimate is

    |Tr U0|<=d max{1,||A||_2^(p(d-1))}.                (19)

Each jth diagonal entry is a coordinate of A^(pj)e0, proving the estimate.
It can be much more costly than(15), and is not asserted optimal.
A change to another integral basis conjugates the actual operators and preserves their determinant and trace; it does not certify a cheap embedding norm or remove the covolume/derivative data in(16)--(18).

<a id="frobenius-lift-outcome-and-next-boundary"></a>
## 8. Outcome and the remaining genuinely different opportunity

There IS an original d by d integer determinant with a bounded +/-1 perturbation and at least the mandatory p^d floor.
Its existence has been proved with no ramification or degree-preservation restriction.
The complete scalar and commuting classes reduce to the old cyclic norm times an explicit trace/adjugate factor, while the full integer congruence class occupies the old Sylvester cokernel.
Thus the simple nonzero construction does not by itself provide new inexpensive original arithmetic income.

For all noncommuting V as well, applying the existing coefficient/exterior-volume method returns the known orbit-Gram certificate at N=pd, with the exact prime-factor cancellation(9).
This is the fully identified failure of the proposed free-prime mechanism.
It is not a proof that every such determinant is merely a field norm, every possible noncommuting estimate fails, or the original Gram problem has no uniform surplus.
The actual reciprocal saturation example prevents claiming a mandatory extra divisor even for a unimodular lift, but its positive fixed m is not a small-measure counterfamily.

The concrete unclosed opportunity identified in this round is a genuinely new integer/embedding estimate for the restricted affine class(11), or for the explicit trace factor in(6), using small TOTAL m and paying(15)--(18).
A rational relaxation cannot retain its arithmetic floor, another canonical/scalar lift does not eliminate the cyclic/trace factorization, and a mere assertion that Frobenius permutations have norm1 would use the wrong metric.
No new bounded-complexity condition is substituted for that problem.
These are exact remaining proof obligations rather than an exhaustive barrier theorem or a claim that a new positive class has already been found.

Contribution boundary: root supplied the canonical rank-one degeneration, the affine perturbation and polynomial-in-k nonvanishing idea, and separately the sharp two-term scalar factorization/+/-1 choice.
The author independently checked those statements and supplied the trace identity(5), entire commutant formula(6), exact general coefficient window/projection application, rational and integer coset interpretation, reciprocal saturation/control costs, and embedding/trace formulas and full expense comparison.
Root and this author are contributors to this round.
The old L55/L56/L63/L64 statements and their original contribution/review scopes remain inherited inputs, not newly reviewed theorems.
No code, native output, source acquisition or independent project review occurred.

<a id="author-freeze"></a>
Author freeze2026-10-15T16:06.
The complete statement and eight-section argument/formulas(1)--(19) have been self-checked: actual companion column signs; canonical rank and d>=2; adjugate identities including singular commuting V; signed cyclic Delta and trace normalization; N=pd for every prime/dimension endpoint; complete coefficient scaling and scope of L56 rather than L55's restricted counterexample; invertible rational Sylvester map versus its integral coset and exact p-order class; all original2 by2 control arithmetic; the free delta representative versus reduced rho; fixed-S0 coefficient cost; and every Vandermonde/derivative/embedding term.
Root and this author are proof contributors; a separate noncontributor must review the actual fixed whole result.
The standalone nonzero existence is not called a new gap, and no uniform obstruction to all noncommuting estimates is asserted.

## Current assessment
[Selected decision](#decision-current-local-trace-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:08 |
| status | open |
| reason | Fix the complete original integer Frobenius-lift determinant account, including bounded nonzero perturbations, full commuting factorization, general coefficient/coset return, actual saturation and every original expense. Root and g_bridge_audit are new proof contributors. Whole noncontributor review is pending; no automatic new arithmetic surplus or G0001 gap is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire Frobenius-lift statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Complete eight-section argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Actual canonical Frobenius lift](../ledger/Yin_L_G0063_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Integral quotient and remainder](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Mixed-exponent nonvanishing](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Coefficient projection identity](../ledger/Yin_L_G0056_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Earlier coefficient-subspace limitation](../ledger/Yin_L_G0055_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Earlier good-prime local construction](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Earlier full local-lift products](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |

### Decision whole-reviewed-2026-10-16

| Field | Value |
| --- | --- |
| date | 2026-10-15T16:18 |
| status | proved |
| reason | Adopt the entire integer Frobenius-lift determinant account after R370 whole independent review. The actual bounded-sign nonzero construction and fixed-p/bounded-column O(d+m) output-volume estimate are retained; the entire commutant still has the explicit old cyclic/trace factor, and the specified general coefficient-volume method exactly cancels the mandatory prime factor. Record the precise already-used coefficient-pairing and rational-minimum interfaces identified by the review. No new universal surplus, inexpensive complex metric or G0001 gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire Frobenius-lift statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Complete eight-section argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Actual canonical Frobenius lift](../ledger/Yin_L_G0063_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Integral quotient and remainder](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Mixed-exponent nonvanishing](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Coefficient projection identity](../ledger/Yin_L_G0056_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Earlier coefficient-subspace limitation](../ledger/Yin_L_G0055_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Earlier good-prime local construction](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Earlier full local-lift products](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |
| dependency | [Exact integral coefficient pairing](../ledger/Yin_L_G0063_v1.md#coefficient-pairing-sylvester-presentation) | The already used unimodular R tensor R identification sends q ell to q tensor1 and supplies the exact integral affine-cokernel class; it is not the field-trace pairing. |
| dependency | [Actual rational minimum lift](../ledger/Yin_L_G0056_v1.md#unique-minimum-lift) | Arbitrary rational coefficient representatives of the same full-rank image attain the original Gram value; no optimizer is assumed to remain in the constrained integer V family. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0370_v1.md#integer-frobenius-lift-whole-independent-finding) | Complete eight sections and19 formulas, all original algebra/coset/control/expense interfaces, exact additional bindings, source/comparison and contribution boundaries. |


### Decision current-joint-minor-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:52 |
| status | proved |
| reason | Select C226 as the complete current home of the identical retained L55/L56 coefficient-space comparison and full original fixed-window projection/lift proofs at the exact anchors below. The complete argument, scalar/rank domains and actual current statement were read; mathematical status, own proof and selected finding remain. This is routine same-content interface adoption, not a new proof or independent review. Original dated decisions and R bindings keep their actual L inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Dependency](../ledger/Yin_L_G0059_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Support](Yin_C_G0226_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Support](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Support](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#coefficient-pairing-sylvester-presentation) | The already used unimodular R tensor R identification sends q ell to q tensor1 and supplies the exact integral affine-cokernel class; it is not the field-trace pairing. |
| dependency | [Dependency](Yin_C_G0226_v1.md#unique-minimum-lift) | Arbitrary rational coefficient representatives of the same full-rank image attain the original Gram value; no optimizer is assumed to remain in the constrained integer V family. |
| review | [Review](../audits/reviews/Yin_R_G0370_v1.md#integer-frobenius-lift-whole-independent-finding) | Complete eight sections and19 formulas, all original algebra/coset/control/expense interfaces, exact additional bindings, source/comparison and contribution boundaries. |


### Decision current-confluent-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:12 |
| status | proved |
| reason | Select C231#mixed-power-resultant-identities as the complete current home of the identical original L59 full-root cross-exponent nonvanishing, multiplicity and exact resultant conventions at the unchanged used scope. The complete retained proof and actual current statement were read, including non-torsion and degree-drop boundaries; this is routine same-content interface adoption. Mathematical status, selected statement/argument/finding and every relation scope remain. Original dated decisions and R bindings retain their actual L59 inputs, and no new independent review or additional arithmetic surplus is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Support](Yin_C_G0226_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Support](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Support](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |
| dependency | [Dependency](../ledger/Yin_L_G0063_v1.md#coefficient-pairing-sylvester-presentation) | The already used unimodular R tensor R identification sends q ell to q tensor1 and supplies the exact integral affine-cokernel class; it is not the field-trace pairing. |
| dependency | [Dependency](Yin_C_G0226_v1.md#unique-minimum-lift) | Arbitrary rational coefficient representatives of the same full-rank image attain the original Gram value; no optimizer is assumed to remain in the constrained integer V family. |
| review | [Review](../audits/reviews/Yin_R_G0370_v1.md#integer-frobenius-lift-whole-independent-finding) | Complete eight sections and19 formulas, all original algebra/coset/control/expense interfaces, exact additional bindings, source/comparison and contribution boundaries. |


### Decision current-sylvester-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:29 |
| status | proved |
| reason | Select C237 as the complete current responsible home of the identical retained L63 original-order prime quotient, nonreduced Frobenius and exact integral coefficient-pairing/Sylvester interfaces at the actual anchors below. The full proof, current statement and each used scalar/local/index boundary were read; this is same-content locator adoption. Mathematical status, selected statement/argument/finding and all relation scopes remain unchanged. All prior current C226/C231/Haar homes remain selected where present, while old dated decisions and R bindings keep their actual L63 inputs. No new independent review, low-cost norm or uniform arithmetic gain is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Dependency](Yin_C_G0237_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Support](Yin_C_G0226_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Support](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Support](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |
| dependency | [Dependency](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) | The already used unimodular R tensor R identification sends q ell to q tensor1 and supplies the exact integral affine-cokernel class; it is not the field-trace pairing. |
| dependency | [Dependency](Yin_C_G0226_v1.md#unique-minimum-lift) | Arbitrary rational coefficient representatives of the same full-rank image attain the original Gram value; no optimizer is assumed to remain in the constrained integer V family. |
| review | [Review](../audits/reviews/Yin_R_G0370_v1.md#integer-frobenius-lift-whole-independent-finding) | Complete eight sections and19 formulas, all original algebra/coset/control/expense interfaces, exact additional bindings, source/comparison and contribution boundaries. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All actual original nontorsion integer units and every rational prime, exact matrix/arithmetic/affine-coset/expense conclusions and actual control. |
| argument | [Argument](#argument) | All19 formulas, companion signs, singular commuting matrices, finite prime/dimension endpoints, signed original cyclic factor, exact costs and remaining scope. |
| dependency | [Dependency](Yin_C_G0237_v1.md#frobenius-intertwiner-floor) | Integral full power-basis lift, residue Frobenius including nonreduced reduction and original Sylvester module. |
| dependency | [Dependency](Yin_C_G0237_v1.md#base-prime-power-extra-valuation) | Original q=P(alpha^p)/p, integer remainder and full normalized resultant/module. |
| dependency | [Dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | All original pair differences alpha_i^p-alpha_j are nonzero by nontorsion; no powered-degree or normality restriction. |
| dependency | [Dependency](Yin_C_G0226_v1.md#projection-cost-identity) | Exact R_N/Q coefficient-volume inequality and rational optimum for the actual window N=pd; no restricted counterexample enlarged to all lifts. |
| support | [Support](Yin_C_G0226_v1.md#coefficient-subspace-optimum) | Bounded reuse comparison; its restricted example is not promoted to a general impossibility theorem. |
| support | [Support](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Distinct source of the local Frobenius interface, not an unramified assumption or cheap complex metric in the new proof. |
| support | [Support](../ledger/Yin_L_G0397_v1.md#all-local-lifts-symmetrization) | Previously paid multiplicative globalizations, distinct from the present actual matrix determinant and coefficient lift. |
| dependency | [Dependency](Yin_C_G0237_v1.md#coefficient-pairing-sylvester-presentation) | The already used unimodular R tensor R identification sends q ell to q tensor1 and supplies the exact integral affine-cokernel class; it is not the field-trace pairing. |
| dependency | [Dependency](Yin_C_G0226_v1.md#unique-minimum-lift) | Arbitrary rational coefficient representatives of the same full-rank image attain the original Gram value; no optimizer is assumed to remain in the constrained integer V family. |
| review | [Review](../audits/reviews/Yin_R_G0370_v1.md#integer-frobenius-lift-whole-independent-finding) | Complete eight sections and19 formulas, all original algebra/coset/control/expense interfaces, exact additional bindings, source/comparison and contribution boundaries. |

