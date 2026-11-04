---
author: Yin
---
# AM16-U003: rank-two prior coverage of normal Salem trace fields

Date: 2026-10-18T11:37.
Human record author Yin.
Root requested a bounded reuse and primary-literature screen for genuine Salem numbers whose actual trace field is Galois, without assuming abelianity.
The entropy_attainment_bridge AI directly inspected the existing primary artifact and checked the specialization below.
This records an established external theorem and its immediate application, not a new project height theorem or an independent review of its original proof.

<a id="am16-u003"></a>
## Read; accepted rank-two statement and normal-trace applicability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and David Masser, Lower bounds for the height in Galois extensions, institutional author postprint dated 3 August 2016; six PDF pages including a cover and printed pages 1--5. Same retained AM16--author-postprint.pdf and artifact provenance as U001 and U002.

Passages: Height normalization and Theorem 2.1 on printed 1/PDF 2, continued on printed 2/PDF 3 with its joint-degree convention and attribution; Section 3 printed 2--4 for comparison with the ambient-Galois and Galois-generator scopes.

Inspection: Direct text reading of the complete Theorem 2.1 statement, its continuation and adjacent attribution, with exact K=Q,r=2 hypotheses and the application below checked. No original Amoroso--David or Delsinne proof audit, no source-wide audit, and no numerical constant or varying-rank uniformity claim.


The [retained primary postprint](../../../literature/pdf/AM16--author-postprint.pdf) identifies the inspected edition.
The accepted author-order erratum boundary remains exactly that of [U001](Yin_U001.md#am16-u001).
No new artifact, edition or acquisition is claimed.

### Exact source input

Theorem 2.1 states a height lower bound for multiplicatively independent algebraic numbers alpha_1,...,alpha_r over an abelian base K/Q, with D=[K(alpha_1,...,alpha_r):K].
This unit accepts only its FIXED r=2, K=Q specialization:

    For every epsilon>0 there is C_2(epsilon)>0 such that
    max{h_abs(x),h_abs(y)}
       >=C_2(epsilon)[Q(x,y):Q]^(-1/2-epsilon)       (1)

for all multiplicatively independent nonzero algebraic x,y.
Here multiplicative independence means that x^a y^b=1 with integers a,b implies a=b=0.
The constant is independent of x,y and their joint degree; the subscript 2 makes explicit the fixed rank, which is suppressed in the source notation C(epsilon).
The absolute logarithmic Weil height is the source's printed-page-1 normalization, equivalently total logarithmic Mahler measure divided by the degree of the primitive minimal polynomial.
The base Q is abelian, so this specialization needs no hypothesis on the Galois group of Q(x,y).
Neither integrality nor the Galois property of that joint field is required by (1).
No explicit numerical value or degree-independent absolute-height floor is supplied by (1).

The source immediately attributes the K=Q case of Theorem 2.1 to its reference [1], Amoroso--David, Le probleme de Lehmer en dimension superieure, J. reine angew. Math. 513 (1999), 145--179.
That attribution is read in AM16; the original paper and proof are not accepted here as independently inspected inputs.
The established exact AM16 statement is accepted for use under the existing external-input rule.

### Direct applicability to the actual normal trace field

Let alpha be a genuine Salem number, let d=[Q(alpha):Q]=2t>=4, and put

    F=Q(alpha+alpha^(-1)), [F:Q]=t,
    m=log alpha=d h_abs(alpha).

Assume F ITSELF is Galois over Q.
Choose any nonreal conjugate beta of alpha; it has |beta|=1 and is not a root of unity.
The latter follows because a torsion conjugate would make the common irreducible minimal polynomial cyclotomic, contradicting alpha>1.
The numbers alpha,beta are multiplicatively independent: taking absolute values of alpha^a beta^b=1 gives alpha^a=1 and hence a=0, after which beta^b=1 gives b=0.

Normality of F puts beta+beta^(-1) in F, since this is a conjugate of the primitive generator alpha+alpha^(-1).
Both alpha and beta satisfy monic quadratic equations over F.
Moreover F is contained in Q(alpha,beta), already because F is contained in Q(alpha).
The tower degree therefore gives

    [Q(alpha,beta):Q]
       =[F(alpha,beta):F][F:Q]<=4t=2d.              (2)

Conjugate heights agree, so (1)--(2) immediately give

    h_abs(alpha)>=C_2(epsilon)(2d)^(-1/2-epsilon),
    m>=2^(-1/2-epsilon) C_2(epsilon)
             d^(1/2-epsilon).                     (3)

Taking epsilon=1/4 yields the especially simple fixed statement

    m>=2^(-3/4) C_2(1/4) d^(1/4)
       >=2^(-1/4) C_2(1/4)>0.                    (4)

The final inequality uses d>=4.
Thus all genuine Salem numbers with an ACTUAL normal trace field already have a uniform positive TOTAL logarithmic Mahler gap, without an abelianity, prime, Frobenius-class or ramification hypothesis.
In fact this selected classical estimate grows with their degree.
Its absolute-height bound in (3) still decreases with d; it must not be presented as a uniform positive absolute-height bound over this whole class.

This verification never replaces F by its normal closure.
For a general Salem number only the larger trace splitting field is known to contain all trace conjugates; its degree need not be t, and the decisive 2d bound in (2) is then unavailable.
Consequently this application does not settle the unrestricted Salem gap.

### Reuse conclusion and bounded search scope

The initial reuse pass inspected [L_G397's abelian-trace screen](../../../ledger/Yin_L_G0397_v1.md#abelian-trace-field-reuse-screen), [U002's rank-one abelian-base scope](Yin_U002.md#am16-u002), [U001's distinct Galois-generator scope](Yin_U001.md#am16-u001), and the [existing CM10 kernel reading](../CM10/readme.md#cm10-salem-kernel-attribution).
The retained AM16 primary statement and CM10 printed pages 1--2 were then read directly.
U002 deliberately accepts only r=1, so it is not silently widened; the missing fixed-rank statement and the normal-trace application are retained here.
CM10's kernel structure by itself is not a height theorem, and Q(alpha) itself is not Galois for a genuine Salem number: it is a subfield of R but has nonreal conjugates.
Thus applying AM16 Theorem 3.3 directly to alpha would use the wrong hypothesis, even though the separate Theorem 2.1 does establish the desired coverage.

The bounded external search used Salem numbers with Galois/normal trace field, trace-polynomial Galois group and Mahler lower-bound queries, followed by the specific AM16 almost-Galois/Amoroso--David Corollary 1.8 lead.
The latter's primary institutional metadata was accessible, but its PDF fetch through the web reader returned HTTP 403 and no original statement was inspected or used.
No conclusion about that unchecked corollary is needed: (1) in the already retained primary AM16 artifact is sufficient, so the acquisition branch and broader search were stopped.
Search snippets, third-party summaries and absence of an exact-title hit are not theorem evidence or a novelty argument.

For the [C_G163 normal-trace criterion](../../../claims/Yin_C_G0163_v1.md#normal-trace-class-statement), this changes the prior-coverage comparison: normal trace fields without a supplied small-prime or bounded-class condition are already covered in total measure by (3).
C163 can still provide a distinct explicit conditional estimate or local-method refinement; this unit does not review its proof or amend its decision.
The abelian subclass retains U002's stronger degree-independent absolute-height result.
No claim of new gap coverage for normal trace fields is supported by this screen.
