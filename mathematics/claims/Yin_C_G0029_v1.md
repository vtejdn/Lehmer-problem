---
author: Yin
---

# First-window integer covariance forces nonzero cross terms for flat coefficients

Date: 2026-10-11T21:22.
Human author Yin.
Provenance: project deduction in the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root supplied the substantive arithmetic-form/covariance candidate; the responsible author reconstructed the entire infinite-residue proof.
The new D4 address was reused only for this assignment and inherited no older D4 scope.
Old projected-lattice and all-odd binomial mechanisms are credited without a novelty or main-theorem designation.

## Statement

Let P(t)=sum_(j=0)^d p_j t^j be an ACTUAL monic irreducible nontorsion integer-unit minimal polynomial, original degree d>=2, with p_j in{0,+1,-1} and n>=2 nonzero coefficients.
Use ACTUAL O_0=Z[alpha] and FIRST allowed coefficient window[0,d], N=d+1.
Let p be its full coefficient column, A=[I_d,-p_low], D=diag(p_i^2), S={i:p_i!=0}, and

    H=I_N+(D-pp^T)/(n-1).

**A. Complete arithmetic form.**
H is rational PSD, has EVERY diagonal entry1 and kernel R p.
For EVERY REAL f with ACTUAL remainder Af in Z^d minus{0},

    f^T H f>=1.

All equality representatives are exactly f=+/-e_j+c p, j=0,...,d and c real, with the appropriate rational restriction in the rational coefficient class.
The proof covers zero-coefficient positions, n2, the full integer quotient and the forbidden zero residue; it does not substitute a finite lattice search or evaluation at one embedding.

**B. Covariance and required cross terms.**
For ANY finite such family with positive normalized real weights, put X=sum_b omega_b f_b f_b^T and E=Tr X.
Then

    Tr(HX)>=1,
    sum_(i!=j) p_i p_j X_ij<=-(n-1)(1-E).

In particular, if E<1 the ORDERED support off-diagonal mass satisfies

    sum_(i,j in S,i!=j)|X_ij|>=(n-1)(1-E)>0.

For unordered pairs i<j the bound is HALF this amount.
Every coefficient covariance matrix that is DIAGONAL therefore has E>=1.
Its restricted first-window capacity is EXACTLY1 for both rational and formal-real packets.
The constant singleton attains this in the allowed window; a positive two-monomial packet attains it with ACTUAL union width exactly d.

**C. Full complementarity is different.**
C16/C17's full domain imposes only aggregate lag sums sum_i X_(i,i+h)=0, not individual off-diagonal entries or atomwise autocorrelations.
Adopted C17 gives FULL E_d<1, so a below-one packet necessarily uses nonzero cross entries whose lag sums cancel.
The singular arithmetic H is not a positive-definite Toeplitz matrix of C16 and cannot be used to infer a full-domain bound E_d>=1.
For original Lehmer n9, the required ordered support mass is at least8(1-E).
No reciprocal hypothesis is needed for A--C.

**D. Wider-window and full-cost boundary.**
For DENSE flat P, all coefficients are odd and the actual full quotient gives alpha^(d+1)=1 modulo2O_0.
The old pair f_+=(1+t^(d+1))/2, f_-=(1-t^(d+1))/2 with weights1/2 has ACTUAL nonzero integral values, diagonal coefficient covariance and E1/2 at actual width d+1, q=M=2 and primitive numerators.
Hence the diagonal restricted capacity there is at most1/2, without claiming equality.
No such wider-window theorem is inferred for arbitrary sparse inputs.
All full signed norms D_+,D_- are retained as nonzero integers, Res(P,F_+/-)=2^dD_+/- and copied product2^(2d)D_+D_-, with the original width expense and actual q/M.
No general numerical norm values/signs, fixed norm inventory or uniform Lehmer gap are asserted.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T21:22 |
| status | open |
| reason | Register the complete05:05 author proof of the all-real integer-fiber form and covariance obstruction, with exact restricted capacities and wider-window/full-cost boundaries. Separate whole and actual extraction review are required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ACTUAL flat minimalP/O_0/FIRST window, ALL real integer residues and finite weights, full equality/cross-term/diagonal-restricted conclusions and stated dense wider control only. |
| argument | [Argument](#argument) | COMPLETE05:05 D4 Sections1--10/theorem/equations1--15, every PSD/kernel/integer minimum/equality/averaging/lag and original arithmetic argument. |
| dependency | [Actual integer-residue and moment domain](Yin_C_G0016_v1.md#statement) | Full remainder condition, finite covariance and rational/formal-real conventions; no diagonal restriction is silently substituted for its full domain. |
| dependency | [Full-domain strict first-window result](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Actual monic irreducible nontorsion unit gives FULL E_d<1; distinguishes the restricted diagonal result without a new primal construction. |
| dependency | [Actual short-width and modulo2 controls](Yin_C_G0014_v2.md#statement) | Original order/nonzero membership, actual versus allowed width and full possibly nonreduced monogenic quotient; no overorder or field replacement. |
| dependency | [Generic-monic original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual rational complementary packets and the explicit wider pair, with true denominators, signed full norms, contents and actual width. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T21:30 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ACTUAL flat minimalP/O_0/FIRST window, ALL real integer residues and finite weights, full equality/cross-term/diagonal-restricted conclusions and stated dense wider control only. |
| argument | [Argument](#argument) | COMPLETE05:05 D4 Sections1--10/theorem/equations1--15, every PSD/kernel/integer minimum/equality/averaging/lag and original arithmetic argument. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Full remainder condition, finite covariance and rational/formal-real conventions; no diagonal restriction is silently substituted for its full domain. |
| dependency | [Dependency](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Actual monic irreducible nontorsion unit gives FULL E_d<1; distinguishes the restricted diagonal result without a new primal construction. |
| dependency | [Dependency](Yin_C_G0014_v2.md#statement) | Original order/nonzero membership, actual versus allowed width and full possibly nonreduced monogenic quotient; no overorder or field replacement. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual rational complementary packets and the explicit wider pair, with true denominators, signed full norms, contents and actual width. |
| review | [Current finding](../audits/reviews/Yin_R_G0790_v1.md#c29-flat-covariance-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:33 |
| status | proved |
| reason | Adopt the separately assigned isolated complete mathematical inspection of this actual fixed statement and entire selected argument. Its recorded initial finding preceded all old target verdicts and substantive target-development context was not shared. Preserve the exact current mathematical domain, complete proof, source-depth and native-execution limits, all earlier findings and their original relationships, and every arithmetic and physical-window charge. No new uniform construction, optimality or Task/E resumption is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ACTUAL flat minimalP/O_0/FIRST window, ALL real integer residues and finite weights, full equality/cross-term/diagonal-restricted conclusions and stated dense wider control only. |
| argument | [Argument](#argument) | COMPLETE05:05 D4 Sections1--10/theorem/equations1--15, every PSD/kernel/integer minimum/equality/averaging/lag and original arithmetic argument. |
| dependency | [Dependency](Yin_C_G0016_v1.md#statement) | Full remainder condition, finite covariance and rational/formal-real conventions; no diagonal restriction is silently substituted for its full domain. |
| dependency | [Dependency](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | Actual monic irreducible nontorsion unit gives FULL E_d<1; distinguishes the restricted diagonal result without a new primal construction. |
| dependency | [Dependency](Yin_C_G0014_v2.md#statement) | Original order/nonzero membership, actual versus allowed width and full possibly nonreduced monogenic quotient; no overorder or field replacement. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Applied ONLY to actual rational complementary packets and the explicit wider pair, with true denominators, signed full norms, contents and actual width. |
| review | [Isolated complete current finding](../audits/reviews/Yin_R_G0790_v1.md#current-flat-covariance) | Complete current fixed statement and entire selected argument, actual required mathematical interfaces and all quantifier, source and execution limits; initial independent reconstruction precedes old target verdict comparison. |

## Argument

The COMPLETE05:05 D4 frozen author account follows unchanged apart from first-title depth and final whitespace.
Every all-integer minimum and equality statement is proved locally by the signed integer support projection and squared pair differences.
MCQ08 is definition attribution only.
Existing C25 and earlier covariance records are credited comparisons, not a missing proof.
No current D2 lattice argument, D3/J89 computation or uninspected source theorem is a premise.
The distinction between coefficient-matrix entries, lag sums and individual atom autocorrelations is retained throughout.

## First-window covariance obstruction for flat minimal polynomials

Date: 2026-10-12.
Human author Yin.
The integer_moment_whole_review AI is the substantive author of this new draft, not its independent reviewer.
Root supplied the general rational PSD matrix and complete candidate covariance-obstruction mechanism; root is a substantive contributor.
The current task is to develop and check that bounded candidate directly here, with no native mathematical program, scan, solver or J.
This reused D address inherits no earlier content, proof or review.

<a id="flat-covariance-reuse-and-attribution"></a>
## 1. Exact reuse, source scope and changed question

The author read the adopted [C16 finite nonzero-integer moment conventions](Yin_C_G0016_v1.md#statement), its [all-representative weighted-quotient argument](Yin_C_G0016_v1.md#weighted-quotient-lattice-certificate), and its explicit [Euclidean projection failure](Yin_C_G0016_v1.md#sharp-quadratic-window-minimum).
C16's quadratic control has shortest Euclidean representatives with strictly positive lag-two correlation, so a positive mixture of those representatives is not complementary.
Projecting a packet to least representatives cannot preserve its lags without a proof.
The present argument instead tests EVERY representative and never projects an existing packet.

The exact adopted [C17 statement](Yin_C_G0017_v1.md#statement) supplies only the later comparison that the full first-window capacity is strictly below1 for each actual irreducible nontorsion input.
Its full dual-completeness proof is an accepted prior result, not newly re-audited here.
The adopted [C25 complete flat-coefficient denominator minimum](Yin_C_G0025_v1.md#statement) gives the different individual Euclidean floor1-1/n and a necessary coefficient denominator for a below-one packet.
It does not give the covariance obstruction below; in particular one low-energy coordinate is not a complementary packet.

The author also read [L367's actual selected-lag unit obstruction and Lehmer controls](../ledger/Yin_L_G0367_v1.md#actual-unit-selected-lag-controls).
That account concerns original monomial residuals plus one actual nonmonomial unit and its forced trace symbol.
Its restrictions do not cover every integer residue in the first window.
The new argument has no selected norm or unit inventory.
Directory/glob screens by diagonal covariance, lag cancellation and projection failure identified those accounts and unrelated probabilistic covariance arguments; no matching general first-window diagonal-covariance conclusion was located in that bounded screen.
This is not an exhaustive novelty or priority search.

The classical name for the support calculation is already covered by [MCQ08-U001](../audits/literature/MCQ08/Yin_U001.md#mcq08-u001).
The selected primary source is McKilliam--Clarkson--Quinn, arXiv:0801.1364v2, SectionII/p.1/equations(1)--(2): A_l star is the projection of Z^(l+1) onto the all-ones perpendicular hyperplane.
The source unit is Read/definition attribution only; no shortest-vector theorem, nearest-point algorithm or original source proof is accepted from it.
This author read that actual source unit, not the primary PDF anew.
Here l=n-1, the support has lengthn and the signed support block is n/(n-1) times that projection.
The complete integer minimum needed below is proved by squared differences.
No new source intake or external search is necessary for this direct deduction, and no novelty is asserted for the projected-lattice form.

Root supplied H and the substantive integer-fiber/covariance candidate, including the diagonal restriction and wider-window comparison.
The author supplies the full reconstruction, zero-support and equality analysis, actual/formal-real boundary, lag-sum interpretation and complete stated costs.
Prior reviews by this author concern upstream materials only; they do not independently review this new construction.
The two other current author streams are not premises and were not reviewed or consumed during this assignment.

<a id="flat-first-window-covariance-statement"></a>
## 2. Precise statement

Let P(t)=sum_(i=0)^d p_i t^i be the ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, d>=2, p_d=1, p_0 in{1,-1}, and every p_i in{0,1,-1}.
Put

    N=d+1, p=(p_0,...,p_d)^T,
    S={i:p_i!=0}, n=|S|>=2,
    A=[I_d,-p_low], D=diag(p_i^2),
    H=I_N+(D-p p^T)/(n-1).                         (1)

Use the ACTUAL order O_0=Z[alpha] and allowed window[0,d].
A rational coefficient vector f is admissible exactly when Af is a nonzero integer vector.
In the FORMAL-REAL extension, real f is admissible only under this same full coordinate condition Af in Z^d minus{0}; membership tested at one real embedding is not a substitute.
A finite packet has positive real weights omega_b, sum omega_b=1, admissible real f_b and

    X=sum_b omega_b f_b f_b^T, E=Tr X.             (2)

The rational subclass requires rational f_b and rational omega_b.
No finite denominator is required for the formal-real class.

**Theorem.** H is rational PSD with diagonal1 and kernel Rp.
Its eigenvalue on the signed-support perpendicular subspace is n/(n-1), and its eigenvalue on the zero-coefficient positions is1.
For EVERY admissible real representative,

    f^T H f>=1,                                  (3)

with equality exactly for f=epsilon e_j+c p, where epsilon in{1,-1},0<=j<=d and c is real.
In the rational subclass c is rational.
Consequently EVERY packet(2), before any lag condition, obeys

    Tr(HX)>=1,
    sum_(i!=j) p_i p_j X_ij<=-(n-1)(1-E).        (4)

If E<1, then the ORDERED total off-diagonal absolute mass in the nonzero coefficient support satisfies

    sum_(i,j in S, i!=j)|X_ij|>=(n-1)(1-E)>0.    (5)

For an unordered sum over i<j the right side is divided by2.

In particular the first-window capacity restricted to DIAGONAL coefficient covariance X is EXACTLY1, for both the rational and formal-real classes.
Here first-window means the allowed window[0,d], as in C16/C17; constant1 is an attainer.
The same value is attained with actual union widthd by the two monomials1,t^d at equal weights.

Exact complementarity imposes only

    L_h(X)=sum_(j=0)^(d-h)X_(j,j+h)=0,
                         1<=h<=d,               (6)

not entrywise diagonality.
C17 gives full E_d^Q=E_d^R<1 for every stated input, so its below-one packets necessarily have nonzero off-diagonal entries whose contributions cancel within ALL the required lag sums.
No atomwise vanishing of autocorrelations is asserted.
The theorem is specific to flat coefficients, O_0 and the first allowed window; it gives no general non-flat, overorder or wider-window extension and no scalar Mahler gap.

<a id="flat-covariance-actual-fiber"></a>
## 3. Actual integer values and the complete first-window fiber

Since P is monic of actual degree d,1,alpha,...,alpha^(d-1) is a Q-basis of K and a Z-basis of O_0.
Reducing the last coefficient by P gives, for rational f,

    f(alpha)=sum_(i=0)^(d-1)(f_i-f_d p_i)alpha^i.

Thus actual O_0 membership is exactly Af in Z^d, and nonzero actual value is exactly Af!=0.
This uses actual minimality and the actual power basis, not an integral-norm test.
For formal real coefficients it is retained as the definition of the extended quotient; Q-linear independence does not justify an embedding-only equivalence for arbitrary real coefficients.

The real kernel of A is exactly Rp: its first d equations say f_i=f_d p_i, and p_d=1.
If r=Af is integral, define z=(r,0) in Z^N.
Then

    f=z+c p, c=f_d,
    Az=Af=r!=0.                                 (7)

Conversely every integer z with Az!=0 and every real c give an admissible formal-real f=z+cp.
Rational f correspond to rational c.
This establishes the entire fiber over EVERY integer residue, without a coefficient cutoff, chosen nearest representative or assumption that f itself is integral.
A common Laurent shift into[0,d] preserves the original integer-value class because alpha and alpha^-1 are units in O_0; the coordinates and X in this theorem are the shifted common-window coefficients.

<a id="flat-covariance-matrix-and-projection"></a>
## 4. The matrix and its projected support block

Order the zero-coefficient positions first and the support positions second.
There are no cross blocks between them in H.
On the zero positions H is I.
On the support put s=(p_i)_(i in S), J=diag(s), and let1 be the all-ones vector of lengthn.
Since J^2=I and s=J1,

    H_SS=(n I_n-s s^T)/(n-1)
        =[n/(n-1)] J [I_n-11^T/n] J.            (8)

The bracket is the ordinary Euclidean orthogonal projection onto1-perpendicular.
Therefore H is PSD; the support kernel is Rs and the complete kernel is Rp.
The nonzero support eigenvalues are n/(n-1), with multiplicity n-1, and the zero-position eigenvalues are1, with multiplicity N-n.
Each diagonal entry is1 directly from(1).
In particular H has rank N-1=d, and H p=0.
No invertibility of H is claimed or needed.

For f=z+cp in(7), H p=0 gives f^T H f=z^T H z.
On the support define integer w_i=p_i z_i.
Expanding(8) gives the exact identity

    f^T H f=sum_(i notin S)z_i^2
      +[n sum_(i in S)w_i^2-(sum_(i in S)w_i)^2]/(n-1)
     =sum_(i notin S)z_i^2
      +[1/(n-1)]sum_(i<j, i,j in S)(w_i-w_j)^2. (9)

The last equality follows because each w_i^2 occurs n-1 times in the pair sum and the cross terms occur twice in the square of the sum.
This is the complete local calculation; MCQ08 is used only to attribute the projected-lattice name.

<a id="flat-covariance-complete-integer-minimum"></a>
## 5. Every integer class and all equality representatives

If some z_i with i outside S is nonzero, its integer square is at least1, and all other terms in(9) are nonnegative.
This proves(3) in that case.

Otherwise every zero-support coordinate vanishes.
If w were constant, say w_i=k for every i in S, then z_i=k p_i on S and z_i=0 elsewhere, so z=kp and Az=0.
This is exactly the forbidden zero residue.
Conversely such a constant w with zero outside coordinates has Az=0.
Thus EVERY admissible z in the remaining case has a nonconstant integer support vector w.

Let its minimum occur a times,1<=a<=n-1.
Each of the a(n-a) pairs from a minimum coordinate to a different coordinate has squared difference at least1.
All other pair terms are nonnegative.
Hence

    sum_(i<j)(w_i-w_j)^2>=a(n-a)>=n-1,
    a(n-a)-(n-1)=(a-1)(n-a-1)>=0.              (10)

Division by the positive n-1 proves(3), including n2.
This tests the WHOLE nonzero integer quotient, not a selected finite family or continuous-residue relaxation.

For completeness, equality in the outside-support case requires exactly one outside coordinate equal+/-1, all other outside coordinates zero, and the support term zero.
The latter means w constant.
Thus f=+/-e_j+cp for an outside-support j after absorbing the constant multiple of p.

In the support-only case, equality in(10) forces a=1 or a=n-1, every cross difference exactly1 and all within-group differences0.
This includes n2.
Accordingly w=k1+epsilon e_j for some integer k, a support indexj and epsilon=+/-1.
Undoing the sign change and absorbing kp gives f=+/-e_j+cp.
Conversely every such vector has f^T H f=H_jj=1.
Every A e_j is nonzero: for j<d it is a basis vector, and for j=d it is-p_low, whose constant coordinate is nonzero.
Thus all displayed equality representatives are admissible.
If f is rational then c is rational by any nonzero coordinate of p, or directly by the last-coordinate form in(7).
This proves the complete equality statement in the theorem.

<a id="flat-covariance-packet-and-lags"></a>
## 6. Averaging and the off-diagonal deficit

Finite positive normalized averaging of(3) proves Tr(HX)>=1, without assuming any lag equation or rational weight.
From(1),

    Tr(HX)
      =E+[sum_i p_i^2 X_ii-sum_(i,j)p_i p_j X_ij]/(n-1)
      =E-[1/(n-1)]sum_(i!=j)p_i p_j X_ij.        (11)

The diagonal terms cancel exactly.
Rearrangement gives(4).
If E<1, the signed sum in(4) is negative and has absolute value at least(n-1)(1-E).
Because |p_i p_j|=1 on S and zero off S, the triangle inequality gives(5).
The ordered versus unordered factor2 is explicit.
If E>=1, (4) still holds; the claimed strictly positive mass inference is only for E<1.

For an exact complementary packet, expansion of sum omega_b f_b(t)f_b(t^-1) shows that its positive-lag coefficient is exactly L_h(X).
Symmetry supplies the negative lags, so(6) is precisely constant covariance of energy E.
A diagonal X implies(6), but (6) does not imply diagonal X.
The signed sum in(11) uses coefficient products p_i p_j, which in general vary among pairs with the same lag.
The lag sums can therefore vanish while this signed sum remains strictly negative.

In particular if E<1 at least one X_ij with distinct i,j in S is nonzero.
In its lag h=j-i after ordering i<j, the zero sum L_h(X) forces at least one further nonzero entry of the opposite sign in that same lag; a single nonzero entry cannot sum to zero.
This concerns the AGGREGATE covariance entries.
Individual coordinate autocorrelations may be nonzero and are required only to cancel after the same packet weights are applied.
No claim is made that every lag is active or every individual autocorrelation vanishes.

H is a PSD matrix with diagonal1, but is singular and generally is NOT Toeplitz.
It is therefore not one of C16/C17's positive-definite Toeplitz certificates and does not give a full-capacity lower bound1 by discarding its off-diagonal terms.
This exact distinction reconciles(3)--(5) with full E_d<1.

<a id="flat-diagonal-capacity-and-lehmer"></a>
## 7. Exact diagonal restriction and the original Lehmer input

If X is diagonal, then Tr(HX)=sum_i H_ii X_ii=Tr X=E.
Equation(4) thus implies E>=1.
The one-label packet f=1, weight1 has diagonal X=e_0 e_0^T, nonzero actual value1, E1 and exact complementarity.
It is rational and formal-real admissible.
Both restricted infima are consequently EXACTLY1 and attained.
There is no need to invoke equality of infima or a closure of the integer moment hull for this conclusion.

The allowed-window attainer has actual width0.
If actual union width exactlyd is required instead, take f_1=1,f_2=t^d with weights1/2,1/2.
Their second moment is diag(1/2,0,...,0,1/2), their actual union width isd, their residues are nonzero integer units and their energy is1.
Thus the same restricted minimum1 is attained under that stricter width requirement as well.

By the adopted exact C17 first-window statement, each stated actual P has a finite rational exact complementary packet with E<1 and actual union widthd; formal-real infimum agrees.
The present theorem says every such packet must retain nonzero off-diagonal covariance satisfying(4)--(5), with the lag cancellations(6).
It excludes diagonal covariance as a universal first-window construction, while permitting full complementarity.
It does not construct a below-one packet, quantify C17's strict deficit or assert a full optimizer.

For the original Lehmer polynomial, the actual accepted identity is [C226 retained original input](Yin_C_G0226_v1.md#lehmer-joint-prime-control):

    P_L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,
    d10, n9, S={0,1,3,4,5,6,7,9,10}.            (12)

Its original irreducible Salem/nontorsion classification is reused at that accepted project scope; it is not re-proved from root approximations.
The theorem applies to all first-window actual integer residues and all real formal representatives, with no denominator9 or finite atom restriction.
Therefore its diagonal-covariance restricted capacity is1, although full E_10<1.
Any actual complementary E<1 must satisfy

    sum_(i,j in S, i!=j)|X_ij|>=8(1-E).          (13)

C25's different coefficient-denominator bound and C24/J88's finite restricted atom result are not premises or substitutes for this complete-domain inequality.
No independent native replay or broader source-proof inspection is claimed here.

<a id="flat-covariance-wider-window-and-costs"></a>
## 8. Wider-window boundary and complete original costs

At allowed widthd+1 the residue map has kernel containing BOTH P and tP, so the one-dimensional fiber(7) and matrix(1) cannot simply be padded to prove the same theorem.
There is an explicit old boundary on dense all-odd inputs.
If every p_i=+/-1, reduction modulo2 gives P_bar=1+t+...+t^d in the FULL monogenic quotient, whence (t-1)P_bar=t^(d+1)-1 and alpha^(d+1)=1 modulo2O_0.
Put h=d+1 and take the old [C14 two-binomial packet](Yin_C_G0014_v2.md#minimum-integer-energy-complementary-classification):

    f_+=(1+t^h)/2, f_-=(1-t^h)/2,
    omega_+=omega_-=1/2,
    X=diag(1/4,0,...,0,1/4), E=1/2.             (14)

The quotient congruence makes both values u_+,u_- actual O_0 integers; nontorsion makes both nonzero, since alpha^h cannot be+1 or-1.
Direct expansion gives(14), zero aggregate cross term and every lag sum zero.
Thus the diagonal obstruction cannot be extended to all wider windows.
This is the already retained binomial mechanism, also displayed with full norms in [C22's same-input comparison](Yin_C_G0022_v1.md#salem-one-power-packet-complete-norms), not a new all-odd gap theorem or a claim that every flat input escapes at one extra power.
There is no assertion that the full capacity at d+1 equals1/2.

For a rational packet in the theorem let q be the ACTUAL least common coefficient denominator, F_b=q f_b integral, M the ACTUAL least final rational-weight denominator and m_b=M omega_b.
Every D_b=Norm_K(f_b(alpha)) is a nonzero signed INTEGER full original degree-d norm.
The exact arithmetic is

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^m_b=q^(dM)product_b D_b^m_b,
    S_int=q^2 E,
    Lambda=(1/d)sum_b omega_b log|D_b|,
    I=log q+Lambda,
    I-(1/2)log S_int=Lambda-(1/2)log E.           (15)

No numerator is primitively reduced without its content factor; primitive reduction would divide its full resultant by that content to the powerd.
Common Laurent shifts multiply actual values by alpha to the shift power and retain the full original unit-norm sign in each copied multiplicity.
The actual union width is the width of those same common shifted coefficients, not a powered or trace-field degree.
For exact complementary packets ONLY, [C10's complete direct original-root inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) charges (T/d)m(P)>=Lambda-(1/2)log E.
It is not inferred merely from(3) or an individual coordinate.
Formal-real packets may have no q or M, so(15)'s denominator/resultant bookkeeping is asserted only for the rational class.

For the constant coordinate f=1, the diagonal restricted attainer, q=M=1, content1, full norm/resultant1, S_int1, I0, surplus0 and actual width0.
For the actual-widthd monomial pair, q1,M2, both contents1, full norms1 and Norm(alpha)^d=[(-1)^d p_0]^d, copied signed product that same sign, S_int1, Lambda0,I0 and surplus0.
Thus the diagonal restriction itself supplies no positive norm-floor Mahler certificate.

For(14), ACTUAL q=M=2, m_+=m_-=1, both integer numerator contents1, S_int2 and full original resultants2^d D_+,2^d D_-.
No general formula or sign for these nonzero integer D_+,D_- is silently inserted.
The copied signed product is2^(2d)D_+D_-, and the actual width isd+1.
Its true surplus is(log2)/2+log|D_+D_-|/(2d), at the actual original-root width cost.
Dense all-odd inputs already satisfy old sufficient congruence bounds; this example only proves the stated covariance scope boundary.
It does not address an arbitrary near-one reciprocal input or uniformly bounded coefficient/weight denominators.

<a id="flat-covariance-self-check-and-limits"></a>
## 9. Author self-check, outcome and remaining obligations

The complete author reconstruction checks: actual minimality and O_0 membership versus formal-real residue definition; p_d1/p_0+/-1 and n>=2; the full first-window fiber and forbidden kernel class; rationality, every diagonal entry, rank and all three matrix eigenspaces; the exact support sign change and squared-pair identity; every zero-support integer coordinate and EVERY nonconstant support vector; the minimum-multiplicity proof including n2 and all equality representatives; finite positive real averaging; cancellation of every diagonal term and the signed inequality direction; ordered/unordered absolute-mass factor2; all versus individual lag correlations; exact diagonal restricted attainment in both allowed and actual-width senses; C17 comparison without a false PSD/Toeplitz identification; the original Lehmer n9 support; the two-dimensional wider kernel and actual all-odd modulo2 packet; all actual q/M/content/full signed norm/copied multiplicity/unit-shift/original-width expenses and the rational-only guards on them.

The changed result is a complete first-window covariance obstruction for flat minimal polynomials: a below-one packet must spend nonzero signed off-diagonal covariance, and diagonal covariance has exact restricted minimum1.
The full E_d<1 result is compatible because lag sums can cancel without entrywise diagonal covariance.
The proof supplies no lower bound on full E_d stronger than adopted results, no uniform deficit or diagonal-free construction, no specified norm/ideal inventory, no height or q/M bound, no non-flat/overorder/wider-window theorem and no unrestricted scalar Mahler gap.
The next authorized decision is separate whole noncontributor review, then root's fixed extraction/adoption if warranted.

Root and the present author are substantive contributors; neither can provide the independent whole review.
This is AUTHOR self-check only.
The MCQ08 unit remains Read/definition attribution, and upstream project/source proofs retain their prior accepted inspection scopes.
No native mathematical program, scan, solver, J or source intake was performed.
The scoped material checker verifies structure and locators, not mathematics.

<a id="flat-covariance-entire-author-freeze"></a>
## 10. Entire author freeze

2026-10-11T21:05.
The COMPLETE Sections1--10, theorem and equations(1)--(15) are author-frozen after the full reconstruction and self-check described above.
This includes every actual/formal-real/order/first-window guard, all integer residues and representatives, zero-support and signed-support cases, all equality representatives, matrix eigenvalues/kernel/diagonal, positive real averaging, exact signed and absolute off-diagonal bounds, every lag versus entrywise/atomwise distinction, both diagonal restricted attainments, original Lehmer support, old one-extra-power all-odd boundary, full rational q/M/content/signed-original-norm/copied-product/shift/width costs and source/reuse/contribution limits.
The scoped material check passed before this freeze and is repeated after this final append.

This is a completed AUTHOR investigation and self-check, not independent review or adopted Claim.
Root supplied a substantive proof candidate; the present author completed its proof and accounting.
A separate noncontributor whole review and root's actual fixed extraction/interface review remain required before adoption.
No further author mathematical development remains under this bounded assignment.
G0001 remains active and unrestrictedly unresolved.


## Registration and preservation operation

2026-10-11T21:22: physically retain the ENTIRE2026-10-11T21:05 new D4 author freeze as the selected fixed argument.
The separate whole finding does not automatically cover this actual statement/selection; an actual extraction review is pending.
Working-address retirement waits for full preservation and incoming-reference maintenance.
No native program, new execution allowance or unrestricted Task completion accompanies this registration.
