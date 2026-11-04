---
author: Yin
---

# The finite Lehmer dual descends to an explicit E10 Lorentzian lattice

Date: 2026-10-11T21:25.
Human author Yin.
Provenance: project deduction, exact fixed-input interpretation of an adopted finite dual.
Root supplied substantive kernel/isometry/U-split candidates; the responsible author checked and completed the integral E8/E10 bases and all hand arguments.
The reused D2 address has ONLY this new assignment's scope.
Classical lattice names and the companion-versus-Coxeter distinction are explicit.
No novelty, main-theorem designation or unrestricted gap is claimed.

## Statement

Fix the ORIGINAL actual degree10 Lehmer minimal polynomial P with ascending coefficient vector p=(1,1,0,-1,-1,-1,-1,-1,0,1,1), K=Q(alpha), ACTUAL O_0=Z[alpha], A=[I_10,-p_low] and actual COLUMN companion M.
Let beta=(1,0,1,0,0,0,-1,-1,1,1,-1) be C24's finite dual, W_0 the symmetric rational Toeplitz matrix with diagonal1 and lag-h entry-beta_h/2, G its first10 coefficient block and H=2G.

**A. Exact descent and integral lattice.**
One has W_0p=0, W_0=A^TGA and M^TGM=G.
An EXPLICIT unimodular integral basis and its integer inverse identify the lattice(Z^10,H) with U orthogonal-sum E8 and with the T(2,3,7) Cartan root lattice E10.
Here U has Gram[[0,1],[1,0]] and E8 is realized concretely, without an invoked classification theorem.
Consequently

    det H=-1, signature H=(9,1),
    det G=-1/1024, inertia W_0=(9,1,1).

The companion is an integral isometry of this concrete lattice.
Identification with a PARTICULAR ordered Coxeter reflection word is NOT proved merely from its characteristic polynomial.

**B. Explicit missing integer fiber.**
With indices0,...,9, let

    u=(-2,-1,-1,0,0,1,1,2,0,0),
    v=-e8-u,
    r=2u+e8=(-4,-2,-2,0,0,2,2,4,1,0).

Then Hu=-e8, u and v are isotropic with u^THv=1, and r^TGr=-1.
This is the same U-basis sign convention as the complete retained proof.
The corresponding integer polynomial

    R(t)=-4-2t-2t^2+2t^5+2t^6+4t^7+t^8

has ACTUAL width8, coefficient energy49, primitive content1 and nonzero ACTUAL O_0 value.
EVERY rational first-window representative f=(r,0)+cP of this same integer residue has f^TW_0f=-1.
Thus W_0 is not a complete positive Toeplitz/lattice lower certificate.
This does NOT contradict C24: r is outside its ternary restriction and the displayed representative is outside its energy4 cap.
Its nonzero lag8 prevents the singleton from being an exact complementary primal packet.

The full signed original norm remains D=Res(P,R) in Z minus{0}, with numerical value/sign/unit status NOT evaluated by this proof.
Actual singleton coefficient/final-weight denominators are1, but no C10 constant-covariance income estimate is applied to this noncomplementary atom.
Its negative indefinite-form value is not a coefficient energy, field norm, cheap residue or a new scalar Mahler bound.

**C. General RATIONAL boundary obstruction.**
For ANY actual monic irreducible nontorsion integer-unit polynomial Q of degree e>=2 and full coefficient column q, a RATIONAL symmetric Toeplitz matrix W of size e+1 with diagonal1 and Wq=0 CANNOT be PSD.
The local proof descends to the rational companion-invariant form, uses irreducibility to exclude a proper rational radical and uses bounded integer powers to contradict nontorsion.
This assertion is not extended to arbitrary irrational real kernels or used as a uniform input/cost theorem.

No new primal packet, exact full capacity, effective norm/height/denominator bound, matrix-radius-to-scalar transfer or near-one coverage is established.
The proof is entirely hand algebra; no saved J89 native output is a premise.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T21:25 |
| status | open |
| reason | Register the complete05:05 new D2 hand proof, explicit integral bases and negative fiber, general rational boundary lemma and exact source naming/limitations. Separate whole and actual extraction review remain required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE actual original-Lehmer dual/lattice/fiber plus the precisely stated GENERAL RATIONAL Toeplitz boundary lemma; no primal or unrestricted conclusion. |
| argument | [Argument](#argument) | COMPLETE05:05 D2 Sections1--7/statement/equations1--15, every kernel/companion/integral basis/inverse/Schur/negative-atom/rational-module proof. |
| dependency | [Adopted finite dual and its restricted scope](Yin_C_G0024_v1.md#statement) | Exact beta coefficients and finite13197atom comparison ONLY; no global PSD or all-integer floor is imported. |
| dependency | [Actual original-Lehmer input](../ledger/Yin_L_G0055_v1.md#lehmer-joint-prime-control) | Actual degree10 irreducible reciprocal Salem/nontorsion identity and O_0 power basis, without a new source/native root audit. |
| support | [Positive Toeplitz capacity domain](Yin_C_G0016_v1.md#statement) | Distinguishes the required positive-definite whole-lattice class from this indefinite finite-only dual. |
| support | [Complete first-window context](Yin_C_G0017_v1.md#statement) | Related bounded-powers mechanism and full-domain E_10<1, not a substitute for the present explicit integral construction. |
| support | [Classical diagram and naming](../audits/literature/McM11/Yin_U001.md#mcm11-u001) | Exact selected author-preprint Coxeter Gram/diagram/U/E10 naming only; original classification/glue/K3 proofs uninspected and NOT premises. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T21:32 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE actual original-Lehmer dual/lattice/fiber plus the precisely stated GENERAL RATIONAL Toeplitz boundary lemma; no primal or unrestricted conclusion. |
| argument | [Argument](#argument) | COMPLETE05:05 D2 Sections1--7/statement/equations1--15, every kernel/companion/integral basis/inverse/Schur/negative-atom/rational-module proof. |
| dependency | [Dependency](Yin_C_G0024_v1.md#statement) | Exact beta coefficients and finite13197atom comparison ONLY; no global PSD or all-integer floor is imported. |
| dependency | [Dependency](../ledger/Yin_L_G0055_v1.md#lehmer-joint-prime-control) | Actual degree10 irreducible reciprocal Salem/nontorsion identity and O_0 power basis, without a new source/native root audit. |
| support | [Support](Yin_C_G0016_v1.md#statement) | Distinguishes the required positive-definite whole-lattice class from this indefinite finite-only dual. |
| support | [Support](Yin_C_G0017_v1.md#statement) | Related bounded-powers mechanism and full-domain E_10<1, not a substitute for the present explicit integral construction. |
| support | [Support](../audits/literature/McM11/Yin_U001.md#mcm11-u001) | Exact selected author-preprint Coxeter Gram/diagram/U/E10 naming only; original classification/glue/K3 proofs uninspected and NOT premises. |
| review | [Current finding](../audits/reviews/Yin_R_G0790_v1.md#c30-lorentzian-dual-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision current-joint-minor-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:52 |
| status | proved |
| reason | Select C226#lehmer-joint-prime-control as the complete current responsible home of the identical retained L55 original degree10 irreducible Salem/nontorsion control, at exactly the already used identity and original power-basis scope. The complete original control, accepted MS26 premise and source-depth limits were actually read. This is a same-content interface adoption; mathematical status, statement/proof and selected finding remain, with no new independent inspection or cyclic-return calculation. Old dated decisions and R bindings retain the original L55 address and inspection facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE actual original-Lehmer dual/lattice/fiber plus the precisely stated GENERAL RATIONAL Toeplitz boundary lemma; no primal or unrestricted conclusion. |
| argument | [Argument](#argument) | COMPLETE05:05 D2 Sections1--7/statement/equations1--15, every kernel/companion/integral basis/inverse/Schur/negative-atom/rational-module proof. |
| dependency | [Dependency](Yin_C_G0024_v1.md#statement) | Exact beta coefficients and finite13197atom comparison ONLY; no global PSD or all-integer floor is imported. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Actual degree10 irreducible reciprocal Salem/nontorsion identity and O_0 power basis, without a new source/native root audit. |
| support | [Support](Yin_C_G0016_v1.md#statement) | Distinguishes the required positive-definite whole-lattice class from this indefinite finite-only dual. |
| support | [Support](Yin_C_G0017_v1.md#statement) | Related bounded-powers mechanism and full-domain E_10<1, not a substitute for the present explicit integral construction. |
| support | [Support](../audits/literature/McM11/Yin_U001.md#mcm11-u001) | Exact selected author-preprint Coxeter Gram/diagram/U/E10 naming only; original classification/glue/K3 proofs uninspected and NOT premises. |
| review | [Review](../audits/reviews/Yin_R_G0790_v1.md#c30-lorentzian-dual-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:33 |
| status | proved |
| reason | Adopt the separately assigned complete mathematical inspection of this actual fixed statement and entire selected argument at its actual SELF relationship. Its recorded initial finding preceded old target verdict comparison, but the initial fixed argument included completed author-validation conclusions beyond the necessary mathematical derivation. Preserve the exact current mathematical domain, complete proof, source-depth and native-execution limits, all earlier findings and their original relationships, and every arithmetic and physical-window charge. No new uniform construction, optimality or Task/E resumption is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE actual original-Lehmer dual/lattice/fiber plus the precisely stated GENERAL RATIONAL Toeplitz boundary lemma; no primal or unrestricted conclusion. |
| argument | [Argument](#argument) | COMPLETE05:05 D2 Sections1--7/statement/equations1--15, every kernel/companion/integral basis/inverse/Schur/negative-atom/rational-module proof. |
| dependency | [Dependency](Yin_C_G0024_v1.md#statement) | Exact beta coefficients and finite13197atom comparison ONLY; no global PSD or all-integer floor is imported. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Actual degree10 irreducible reciprocal Salem/nontorsion identity and O_0 power basis, without a new source/native root audit. |
| support | [Support](Yin_C_G0016_v1.md#statement) | Distinguishes the required positive-definite whole-lattice class from this indefinite finite-only dual. |
| support | [Support](Yin_C_G0017_v1.md#statement) | Related bounded-powers mechanism and full-domain E_10<1, not a substitute for the present explicit integral construction. |
| support | [Support](../audits/literature/McM11/Yin_U001.md#mcm11-u001) | Exact selected author-preprint Coxeter Gram/diagram/U/E10 naming only; original classification/glue/K3 proofs uninspected and NOT premises. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0790_v1.md#current-lorentzian-fiber) | Complete current fixed statement and entire selected argument, actual required mathematical interfaces and all quantifier, source and execution limits; initial direct reconstruction precedes old target verdict comparison. |

## Argument

The COMPLETE05:05 new D2 author account follows unchanged apart from first-title depth and final whitespace.
All integral basis and inverse identities, coordinate pairings, positive complement/Schur determinants, explicit appended E10 roots, companion orientation and rational-module argument are physically local.
Existing McM02/L238/L246 comparisons retain their original matrix/scalar boundaries.
The separate D3/J89 program was not read as proof input or run by this author.
Root's and the responsible author's construction contributions remain disclosed; neither is an independent reviewer of this argument.

## Lorentzian meaning of the finite Lehmer Toeplitz dual

Date: 2026-10-11T20:47.
Internal author periodic_packet_author_finish AI for Yin.
Root supplied the substantive W0/Lehmer-kernel/invariant-form candidate and the UNVERIFIED II_(9,1)/E10 identification question.
This is author development and checking, not independent review.
No claim of lattice identity is a premise.

## Assigned question and scope

Take the exact finite C24 dual beta=(1,0,1,0,0,0,-1,-1,1,1,-1), W0 diagonal1 and lag entries-beta_h/2, original Lehmer coefficients ascending[1,1,0,-1,-1,-1,-1,-1,0,1,1], A=[I_10,-p_low] and G the first10 coefficient block.
Verify the actual algebraic meaning of W0P=0 and W0=A^T G A, companion invariance and the SIGNED lattice2G.
Determine whether an explicit integral congruence to the even unimodular Lorentzian II_(9,1)/E10 lattice is proved or remains unverified.
Supply concrete basis/determinant/signature if asserting it.
Explain the restricted finite certificate versus the full positive Toeplitz capacity class, with a precise changed-residue/negative-cone mechanism and full original order/norm costs.

First read L10/L238/McM02/L246 and relevant existing Lorentz/Coxeter records.
The separate native author owns the actually allocated D3/J89 (the assignment's predicted D24 address was not allocated); this stream must not write, run or independently review that work.
Saved exact Phase A outputs may be read as AUTHOR inputs with their true scope.
No native mathematical program, matrix computation rerun, scan or new J is authorized here.
Substantive arguments belong directly in this D.
Classical E10/Coxeter identifications require bounded primary attribution if recognized.
No matrix-radius gap is transferred automatically to scalar Lehmer or to uniform input coverage.
Freeze at a complete bounded result or explicit remaining gap.

<a id="lorentzian-dual-reuse-and-source"></a>
## 1. Reuse, source depth and contribution

The [current C24 statement](Yin_C_G0024_v1.md#statement) is adopted only for its declared finite family: ternary actual remainders, five specified kernel parameters, energy at most4, and eleven additional initial atoms.
Its exact inequality is not a whole-lattice or all-denominator9 assertion.
[C16](Yin_C_G0016_v1.md#statement) supplies the actual integer-residue capacity domain; [C17](Yin_C_G0017_v1.md#statement) supplies positive-definite rational Toeplitz dual completeness and the full original-Lehmer first-window inequality E_10<1.
Their proofs and the [C10 v2 full-cost inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) were read at these interfaces.
C17 already uses companion invariance and bounded integer powers in a related limit argument.
No novelty is claimed for that mechanism or for classical indefinite root lattices.

The bounded screen read [L10](../ledger/Yin_L_G0010_v1.md#general-reciprocal-necessary-bound), [L9's inverse-trace form](../ledger/Yin_L_G0009_v1.md#inverse-trace-orbit), [L238](../ledger/Yin_L_G0238_v1.md#bounded-companion-factor-fixed-scope), [L246](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope), the retained [McM02 source record](../audits/literature/McM02/readme.md), and the relevant local Lorentz/Coxeter search hits.
The inverse-trace form's Salem signature alone does not identify an integral lattice; its discriminant costs and actual integral orbit conditions remain.
L246 already distinguishes a changed norm-two basis from cancellation of full factors.
L238's accepted canonical Coxeter theorem applies to its specified absolute companion, and its matrix/scalar obstruction remains unchanged here.

For bounded naming attribution, the author read McMullen's primary author preprint [K3 surfaces, entropy and glue](https://people.math.harvard.edu/~ctm/papers/home/text/papers/glue/glue.pdf), dated13 September2009, printed p.7/Section2, which gives the root-diagram convention and E10 congruent to E8 plus a hyperbolic plane, hence II_(9,1).
The published metadata is Journal fuer die reine und angewandte Mathematik658(2011),1--25, DOI10.1515/crelle.2011.048; the inspected edition is the29-page author preprint, not an authenticated comparison with published bytes.
The retained McM02 PDF was also text-read at printed pp.154--155 and180 for its Y_(2,3,5)/Y_(2,3,7) and II_(9,1) terminology.
These are bounded classical attributions; no lattice classification, entire source proof, Coxeter-element realization, or new original-proof audit is imported.
The explicit integral congruence below proves the actual identity locally.

Root supplied the substantive W0/kernel/invariance question, the general rational PSD boundary lemma candidate, and subsequently the explicit null vector, hyperbolic-plane split, Schur determinant calculation and negative vector.
This author independently checked the hand algebra as AUTHOR work and supplied the complete module argument, explicit Euclidean E8 coordinate model, integral simple-root basis/inverse, the two-root extension, and the precise certificate/cost distinction.
Root is a contributor and cannot be the independent whole reviewer.
No saved J89 Phase A output is used in this proof.
No native mathematical program or new J was run or written in this stream.

<a id="lehmer-dual-exact-statement"></a>
## 2. Exact statement

Fix the ORIGINAL irreducible nontorsion Lehmer polynomial, the actual field K=Q(alpha), and the actual monogenic order O_0=Z[alpha], as in C24.
Write

    P(t)=1+t-t^3-t^4-t^5-t^6-t^7+t^9+t^10,
    p=(1,1,0,-1,-1,-1,-1,-1,0,1,1)^T.

Indices for coefficient vectors start at0.
Let K0=2W0 be the11-by-11 symmetric Toeplitz matrix with lags

    (c_0,...,c_10)=(2,0,-1,0,0,0,1,1,-1,-1,1),
    (K0)_(i,j)=c_|i-j|.

Let G be the leading10-by-10 block of W0, H=2G, and A=[I_10,-p_low].
Then:

1. W0 p=0, W0=A^T G A, and the ACTUAL integer multiplication companion M of alpha in the power basis satisfies M^T G M=G.
2. H is integrally congruent to the explicit E10 Cartan form on the T(2,3,7) tree, with diagonal2 and off-diagonal-1 on its edges.
   It is also integrally isometric to U plus the standard even positive E8 lattice, where U=[[0,1],[1,0]].
   Thus det H=-1, signature(H)=(9,1), det G=-1/1024, and inertia(W0)=(9,1,1).
   The II_(9,1) notation denotes this proved concrete even unimodular Lorentzian lattice, without using a classification premise.
3. The integer remainder

       r=(-4,-2,-2,0,0,2,2,4,1,0)^T

   has r^T G r=-1.
   Its polynomial R(t)=-4-2t-2t^2+2t^5+2t^6+4t^7+t^8 has actual nonzero integral O_0 value.
   It violates the global extension of C24's pointwise dual inequality, while falling outside C24's declared finite family.
   Its ordinary coefficient energy is49, not negative.
4. More generally, for ANY actual monic irreducible nontorsion integer-unit polynomial of degree d, a rational symmetric Toeplitz (d+1)-by-(d+1) matrix W of diagonal1 with Wp=0 cannot be positive semidefinite.
   This statement concerns rational boundary forms annihilating the actual minimal relation; it is not a claim about all singular real Toeplitz forms or all kernel relations.

These are fixed-input lattice/certificate statements.
No new primal exact complementary packet, exact full capacity, unit norm for R(alpha), uniform near-one coverage, denominator/height algorithm or Lehmer gap follows.

<a id="minimal-relation-invariant-form"></a>
## 3. Kernel, companion orientation and the rational boundary lemma

First check K0 p=0 without a matrix program.
Both p and K0 commute with reversal, so it suffices to check rows0 through5.
Their products with p, grouping the nonzero lags, are respectively

    2-0-1-1-0-1+1=0,
    2+1-1+0-1-1=0,
    0-1+1+0+1-1=0,
    -2-1+1+1+1=0,
    -2-0+1+1=0,
    -2+1+1=0.                                      (1)

The reversed rows supply6 through10.
This checks every entry and the lag10 sign.

Here is the general kernel algebra, with no assumption that W is definite.
Let the actual monic polynomial have coefficient vector p=(l,1)^T, where l has length d, and block W=[[G,b],[b^T,c]].
Then Wp=0 gives b=-Gl and c=l^TGl.
Consequently

    W=A^T G A,       A=[I_d,-l].                     (2)

The columns a_j of A are the actual coordinates of alpha^j for0<=j<=d.
In the ACTUAL power basis1,alpha,...,alpha^(d-1), multiplication by alpha has columns

    M e_i=a_(i+1),        0<=i<=d-1.

This is the column-companion convention; no transposed companion is substituted.
Toeplitzness and(2) give, for0<=i,j<d,

    (M^T G M)_(i,j)=a_(i+1)^T G a_(j+1)
                    =W_(i+1,j+1)=W_(i,j)=G_(i,j).   (3)

For the stated unit inputs M is an invertible integer matrix, with an integer inverse, since the constant coefficient is+1 or-1.

Suppose now that W is rational, of diagonal1 and positive semidefinite.
Its principal block G is rational PSD, nonzero because its diagonal is1.
If G were singular, its rational kernel V={x in Q^d:Gx=0} would be nonzero.
Equation(3) and invertibility of M^T imply GMx=0 whenever Gx=0, so V is an M-invariant rational subspace.
Identify Q^d with Q[t]/(P) by the actual power basis.
A rational subspace invariant under multiplication by alpha is invariant under every rational polynomial in alpha.
If it contains any nonzero x, irreducibility makes this quotient a field, and x^-1 is a rational polynomial in alpha.
Multiplication by that polynomial puts1 in V and then every power of alpha in V.
Hence V=Q^d, contradicting G nonzero.
Thus G is nonsingular and, being PSD, positive definite.

Equation(3) now bounds every entry of M^n uniformly for n>=0: each column has fixed G length, and the smallest positive eigenvalue of G bounds its ordinary squared Euclidean length.
These are integer matrices, so only finitely many powers occur.
M^a=M^b with b>a then yields M^(b-a)=I.
Applying this multiplication identity to1 in K gives alpha^(b-a)=1, contrary to nontorsion.
Therefore W cannot be PSD.
This proves conclusion4.
Rationality was used to produce a nonzero rational kernel and invoke the actual irreducible module; a real irrational invariant line is not an allowable replacement for that argument.

Since the real quadratic form is not PSD, it has a strictly negative vector.
Continuity gives a rational negative vector, and clearing its denominator gives an integer one.
By(2) a negative coefficient vector cannot have zero actual remainder.
This qualitative fact supplies neither a height bound for the negative vector nor a complementary primal packet.
For this W0, Sections4--6 give a concrete negative integer remainder and the complete lattice type instead.

<a id="explicit-hyperbolic-plane-split"></a>
## 4. Explicit integral hyperbolic plane and positive complement

In Z^10 with form H and standard vectors e_0,...,e_9, set

    u=(-2,-1,-1,0,0,1,1,2,0,0)^T.

Direct row substitution in the lags of H gives

    H u=(0,0,0,0,0,0,0,0,-1,0)^T.                   (4)

For completeness, the ten row expressions are

    -4+1+1+2=0,
    -2+2=0,
    -2+2=0,
    1-1=0,
    1-1=0,
    2-2=0,
    -2+2=0,
    -2-1-1+4=0,
    2-1-1-1=-1,
    2+1-1-2=0.

Thus u^2=0, <u,e_8>=-1 and e_8^2=2.
Define v=-e_8-u.
Then v^2=0 and <u,v>=1.
They span an integral hyperbolic plane U.
Use the ordered index list J=(0,2,3,4,5,6,7,9); these e_i all pair to zero with u.
Put b_i=<e_i,e_8> and w_i=e_i+b_i u.
Then <w_i,u>=<w_i,e_8>=0, hence also <w_i,v>=0, and <w_i,w_j>=H_(i,j).

The basis change is unimodular, not merely rational.
The ordered vectors (u,e_8,e_0,e_2,e_3,e_4,e_5,e_6,e_7,e_9) have determinant+1 or-1 because the omitted coordinate e_1 has coefficient-1 in u.
Replacing e_8 by v=-e_8-u and replacing every listed e_i by e_i+b_i u preserve absolute determinant1.
Name the resulting orthogonal-complement basis

    a=e_0-u,  b=e_2+u, c=e_3, d=e_4,
    e=e_5,    f=e_6-u, g=e_7, h=e_9.                (5)

In order(a,b,d,f | c,e,g,h) its Gram matrix C is [[B,X],[X^T,B]], with

    B=[[2,-1,0,1], [-1,2,-1,0],
       [0,-1,2,-1], [1,0,-1,2]],
    X=[[0,0,1,-1], [0,0,0,1],
       [0,0,0,0], [0,0,0,0]].                     (6)

All entries follow directly by restricting H to J; the added u terms pair to zero with every e_i in J.
The leading principal determinants of B are2,3,4,4, so B is positive definite and det B=4.
The leading two-by-two block of B^-1 is [[1,1/2],[1/2,1]].
Hence the Schur complement of the first B is

    S=[[2,-1,0,1], [-1,2,-1,0],
       [0,-1,1,-1/2], [1,0,-1/2,1]].               (7)

Splitting its leading A2=[[2,-1],[-1,2]], the final two-by-two Schur complement is [[1/3,-1/6],[-1/6,1/3]].
Its eigenvalues are1/2 and1/6, so S is positive definite with determinant3/12=1/4.
Thus C is positive definite with det C=4/4=1.
We have proved H integrally congruent to U direct-sum C, det H=-1 and signature(9,1).
H has integer entries and even diagonal, so it is even unimodular.
This establishes the arithmetic assertions without any classification theorem.

<a id="explicit-e8-coordinate-and-simple-basis"></a>
## 5. Concrete E8 model and an integral T(2,3,7) basis

Let E_1,...,E_8 be an orthonormal basis of Euclidean R^8.
Send the complement vectors of(5) to

    a=E_1-E_2,              b=E_2-E_3,
    c=E_5-E_6,              d=E_3-E_4,
    e=E_6-E_7,              f=E_1+E_4,
    g=(E_1-E_2-E_3-E_4-E_5-E_6+E_7-E_8)/2,
    h=E_2+E_5.                                     (8)

Their norms are2.
Their pairings within(a,b,d,f) and(c,e,g,h) are B, and their cross pairings are X of(6): only a.g=1, a.h=-1 and b.h=1 are nonzero.
Thus(8) is an isometry on the whole rank-eight complement.

It identifies the entire standard E8 lattice, not only a sublattice of its rational span.
Define D8={z in Z^8:sum z_i even}, delta=(1/2,...,1/2), and L8=D8 union(delta+D8).
The displayed vectors all lie in L8: the integer roots have even coordinate sum, and g-delta is an integer vector with even sum.
D8 has covolume2, delta is not in D8 and2delta is in D8, so L8 has covolume1.
It is integral and even: <delta,z>=(sum z_i)/2 is integral for z in D8, delta^2=2, z^2 is even, and (delta+z)^2=2+sum z_i+z^2 is even.
The Gram determinant1 in Section4 gives covolume1 for the integer span of(8).
Inclusion and equal finite covolume imply equality.
This supplies an explicit E8 coordinate model rather than citing uniqueness of even unimodular positive rank-eight lattices.

For a concrete integral root-diagram congruence define

    q_1=a+2b+c+d-g-2h,       q_2=b+d+f,
    q_3=-a,                 q_4=-b,
    q_5=-d,                 q_6=a-f+h,
    q_7=-c,                 q_8=-e.                 (9)

Their Euclidean coordinates from(8) are, in the same order,

    (E_1+E_8-E_2-E_3-E_4-E_5-E_6-E_7)/2,
    E_1+E_2, -E_1+E_2, -E_2+E_3, -E_3+E_4,
    -E_4+E_5, -E_5+E_6, -E_6+E_7.

Each has norm2; distinct pairings are-1 exactly on

    q_1--q_3--q_4--q_5--q_6--q_7--q_8,
               |
              q_2,                               (10)

where the vertical edge attaches q_2 to q_4.
All other distinct pairings vanish.
This is the T(2,3,5) E8 diagram.
The change(9) is integral unimodular: recover a=-q_3, b=-q_4, d=-q_5, c=-q_7, e=-q_8, f=q_2+q_4+q_5, h=q_6+q_3+q_2+q_4+q_5, and finally g=a+2b+c+d-2h-q_1.
These integer inverse formulas also verify generation directly.

Set

    theta=2a+b-c-2e-f-2g=E_7+E_8
         =2q_1+3q_2+4q_3+6q_4+5q_5+4q_6+3q_7+2q_8.

Its norm is2, its pairing with q_8 is1, and its pairing with q_i for1<=i<=7 is0, as the Euclidean coordinates show.
In the orthogonal U summand of Section4 define

    q_0=u-theta,       q_-1=-u-v.                   (11)

Both have norm2.
They pair to-1 with each other; q_0 pairs to-1 with q_8 and to zero with the other eight-root vectors, and q_-1 is orthogonal to every q_1,...,q_8.
Consequently (q_-1,q_0,q_1,...,q_8) has diagonal2 and off-diagonal-1 exactly on the tree obtained by appending q_0,q_-1 to the q_8 end of(10).
The central vertex q_4 has arms of edge lengths1,2,6, the T(2,3,7) or E10 diagram.
These ten roots are an INTEGRAL basis: the q_i for1<=i<=8 generate the complement, u=q_0+theta, and v=-q_-1-u recover the hyperbolic plane.
This is the requested explicit integral congruence to E10, not a conclusion from signature alone.
Together with(8) it proves the actual U plus E8 and II_(9,1) descriptions.

The companion M from Section3 is therefore an actual integral isometry of this concrete lattice.
Nothing above proves that the transported M is the product of these ten simple reflections in any stated order.
A classical E10 Coxeter-element spectral-radius identity is not being asserted for M by a lattice congruence alone.
In this one fixed example its characteristic polynomial is P because M is the original multiplication companion, not because of an imported Coxeter classification.
Finally, the coefficient basis(e_0,...,e_9,p) is unimodular in Z^11 and puts W0 in the block form G direct-sum0, proving its stated inertia(9,1,1); det G=det H/2^10=-1/1024.

<a id="negative-cone-and-finite-certificate"></a>
## 6. Changed integer residue, the finite certificate and full costs

Take r=2u+e_8, the vector in Section2.
From(4),

    r^T H r=4u^2+4<u,e_8>+e_8^2=-4+2=-2,
    r^T G r=-1.                                    (12)

Its coefficient polynomial R has degree8, width8, actual least coefficient denominator1, content1 (the t^8 coefficient is1), and energy16+4+4+4+4+16+1=49.
Since degree R<degree P and R is not zero, R(alpha) is a nonzero element of the ORIGINAL order O_0.
Its full signed field norm is

    D=Norm_K(R(alpha))=Res(P,R) in Z minus{0}.        (13)

No value, sign, unit property or small bound for D is assumed or computed here.
The singleton has weight1 and least weight denominator1, numerator resultant D and normalized income log|D|/10.
These are actual original-degree costs; no trace-degree substitution, order enlargement or division by an unrecorded content is used.
Its covariance is NOT constant, since its lag8 is(-4)*1=-4.
Therefore the C10 constant-covariance income/expense inequality is not applied to this singleton as if it were a complementary packet.
The allowed comparison window is[0,10], but this atom's actual support width is8.

For any rational coefficient vector f in the allowed11-coordinate window, its actual remainder is Af.
Equations(2) and(12) give

    f^T W0 f=(Af)^T G(Af).

In particular EVERY representative of the residue r, f=(r,0)+c p with rational c, has value-1 under this dual form; moving only in this kernel fiber cannot repair it.
Replacing r by any nonzero integer multiple n r gives value-n^2 and actual nonzero residue, with ordinary representative nR of energy49n^2, content|n| and field norm n^10 D.
This is a concrete negative-cone mechanism with all scalar costs, not a source of free arithmetic income.

To connect the form exactly with C24's notation, for all f define a_h(f)=sum_j f_j f_(j+h).
The lag list gives

    f^T W0 f=||f||^2-a_2(f)+a_6(f)+a_7(f)
                         -a_8(f)-a_9(f)+a_10(f).    (14)

For the representative R the complete contributions are a_2=8+8+2=18 from the pairs(0,2),(5,7),(6,8); a_6=-8-8-2=-18 from(0,6),(1,7),(2,8); a_7=-16-2=-18 from(0,7),(1,8); a_8=-4 from(0,8); and a_9=a_10=0.
All unlisted pairs have a zero coefficient.
Thus(14) gives49-18-18-18+4=-1, agreeing exactly with(12).
The author's initially unfreezed lag transcription omitted a pair; this complete hand recomputation repairs it before the entire-author freeze.
The actual vector, norm and theorem are unchanged.

The C24 pointwise inequality is f^T W0 f>=1 for its DECLARED finite family.
The negative residue r has coordinates of magnitude2 and4, so it is outside the selected ternary remainders, even after global sign.
Its representative R also has energy49>4; its residue is not one of the eleven added initial atoms.
Hence it contradicts no adopted finite-family assertion.
It does exclude the extension f^T W0 f>=1 to all admissible actual nonzero integer residues and excludes W0 from the positive-definite/PSD dual class of C16/C17.
A negative point of a proposed dual form does not itself give positive weights satisfying all ten lag-cancellation equations, and R alone supplies none.
Full E_10<1 comes from the already adopted C17, not from mistaking R for a complementary packet.

If any later finite rational complementary packet is actually obtained, with values u_b in O_0 minus{0}, least coefficient denominator q, least weight denominator M_w and m_b=M_w omega_b, its ORIGINAL full resultants and complete product remain

    Res(P,q f_b)=q^10 Norm_K(u_b),
    product_b Res(P,q f_b)^(m_b)
                  =q^(10M_w) product_b Norm_K(u_b)^(m_b).

Its content factors and every signed norm are retained.
For its actual constant rational energy E and actual common union width T, the adopted C10 inequality is

    (1/10)sum_b omega_b log|Norm_K(u_b)|
                         -(1/2)log E <=(T/10)m(P).  (15)

The factors log q cancel only after q has entered BOTH numerator income and integer energy q^2E.
An integral lattice basis change preserves H pairings, not polynomial coefficient energy, lag constraints, a seed-norm inventory, q or the physical window.
It cannot remove these costs or replace the actual O_0 membership test by an arbitrary root-coordinate lattice calculation.

<a id="lorentzian-dual-author-selfcheck"></a>
## 7. Author self-check and precise remaining scope

The complete bounded result is the rational annihilating-form obstruction, the actual invariant lattice's explicit E10 congruence, and a named actual integer negative residue.
It explains how positivity on C24's restricted residue list can coexist with global indefiniteness.
It does not provide a new exact complementary below-one primal packet, numerical or theoretical exact E_10, the missing norm D, a classification of all negative residues, effective height/denominator bounds or input-uniform coverage.
The main G0001 near-one arithmetic-income/cost gate remains unresolved.
In particular the fixed Lehmer measure and the E10 name do not establish a scalar lower bound for arbitrary original units.
L238's separate absolute-companion obstruction and all full factors remain in force.

The complete author self-check covers every kernel row in(1) including reversal and lag10; the ACTUAL column-companion orientation in(3); the irreducible rational-module and PSD-versus-PD step; the bounded integer-powers/torsion implication; all ten products in(4); the unimodular U splitting and every cross entry in(6); the two Schur complements, signs and determinants; every Euclidean vector and pairing in(8)--(10); the complete integer inverse basis formulas; theta's coefficients and pairings; both additional roots, all new edges and their generation of u,v; the W0 inertia and factor2^10; both evaluations of the negative integer vector; all contributing lag pairs and the repaired pre-freeze transcription; actual width8/nonzero O_0 residue/content1/q=M_w=1; the unknown full signed norm rather than a unit claim; kernel-fiber invariance versus changed residue; the finite C24 exclusions and all later-packet q/M_w/content/width expenses.
The naming-only primary-source passage and edition limit are retained in Section1.
No original-source classification or reflection-word theorem is silently selected.

This D is author material, not an independently reviewed Claim.
Root will separately organize a noncontributor whole review and any actual extraction/adoption.
The D identifier was allocated under the reusable-D rule; no history or authority from a retired previous D2 is inherited.
Operational scoped validation and the dated entire freeze are recorded below after the final material check.

<a id="lorentzian-dual-entire-author-freeze"></a>
## Entire author freeze

At2026-10-11T21:05 the ENTIRE assigned account, Sections1--7, exact statement, general rational-boundary lemma, equations(1)--(15), explicit integral E8/E10 bases, negative-residue/full-cost discussion, bounded source attribution, contribution disclosure and author self-check are frozen for a separate whole noncontributor review.
All proofs were developed and checked by hand directly in this responsible D.
There is no native mathematical execution, no J89 output dependency and no independent-review claim by this author.
Scoped `.venv/Scripts/python.exe scripts/material.py check mathematics/drafts/Yin_D_G0002.md` returned checked1 before the freeze and is repeated on this final frozen file; this operational validation checks material structure, not mathematical correctness.

Root retains later source intake and fixed extraction or adoption.
The main G0001 Task remains active and unresolved; this freeze establishes only the bounded statements and retains all explicit nonconclusions in Sections2 and7.


## Canonical naming interface

Subsequent canonical intake [McM11-U001](../audits/literature/McM11/Yin_U001.md#mcm11-u001) retains the exact author-hosted29-page PDF with title-page date13September2009 and selected printedpp6--7, including Figure2.
Publication metadata2011/volume658/pages1--25 is distinguished from that inspected edition.
It supplies diagram/sign/name attribution only.
The local constructive identity above invokes no uniqueness classification; neither that source nor matching characteristic polynomials identifies this actual companion with an unverified specific reflection word.

## Registration and preservation operation

2026-10-11T21:25: retain the ENTIRE2026-10-11T21:05 new D2 freeze as the selected fixed argument.
The separately completed whole finding does not automatically cover the actual summary or subsequent canonical source interface; actual extraction review is pending.
Working-address retirement requires complete preservation and incoming-reference maintenance.
No native program, new allowance or unrestricted Task completion accompanies registration.
