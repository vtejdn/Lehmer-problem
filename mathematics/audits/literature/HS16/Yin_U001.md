---
author: Yin
---

<a id="hs16-u001"></a>
# HS16-U001: the multidimensional interior criterion with its path-sum step repaired

## Source and inspection

[Source and edition notes](readme.md).

Source edition: HS16, [retained PDF](../../../literature/pdf/HS16.pdf), arXiv:1506.08714v4, 11 January 2016; 10 pages.

Passages: Section 1: Theorem 1.1 p.1; Proposition 1.5 pp.2--3; Lemmas 1.6--1.7 and Corollary 1.8 p.3; full Theorem 1.1 proof pp.3--4. Printed and PDF pagination coincide.

Inspection: 2026-10-07, coordinating AI for Yin read the complete selected text and inspected local renders of pp.1--4. Assigned AI review_matrix_completion supplied the endpoint-path repair below; the coordinator checked its complete proof and applicability. Original connectedness sources were not separately audited.


## Adopted statement and conventions

Let B be a real r by r matrix, r>=2, all of whose eigenvalues have modulus strictly less than one.
Let v be cyclic for B.
For digits epsilon_j in {0,1}, put

    T(B,v)={sum_(j>=0) epsilon_j B^j v}.

The series converges uniformly over digit choices, including nonnormal B.
Theorem 1.1 asserts that T(B,v) has nonempty interior if

    |det B|>=2^(-1/r).                              (1)

The source uses digits {-1,+1}; its affine translation and scaling to {0,1} are explicit on pp.3--4 and preserve interior.
Its Corollary 1.8 states that the binary attractor is path connected when |det B|>=1/2, at the source's nondegenerate cyclic scope.
We accept that connectedness interface at checked statement scope; its inputs are source Lemma 1.6, cited there to Shmerkin--Solomyak [11, Lemma 2.3], and Lemma 1.7, cited to Odlyzko--Poonen [10, Lemma 4.1].
Those original proofs remain external and their bibliography entries are not separately adopted sources here.

The local reconstruction below validates the residue-class argument for (1) using this accepted path-connectedness input and an explicit replacement for the source's path-sum assertion.
It does not assert that the literal wording of every intermediate source proposition is correct.

## Why the path-sum wording needs a restriction

Proposition 1.5 says that n paths whose span is R^n have a Minkowski sum with nonempty interior.
Read as the ordinary linear span of their images, this is false: in R^2 take the two constant paths at e_1 and e_2.
Their images span R^2 but their sum is one point.
Its proof's appeal to the Jordan--Brouwer theorem does not supply a missing endpoint condition for arbitrary paths.
We do not adopt that general statement or its proof.

The actual interior proof needs only paths beginning at zero and ending at linearly independent vectors.
On p.4, replace the choice of any path merely containing v by a path from 0 to v.
Both endpoints belong to T(B^r,v), so the accepted path-connectedness result supplies that choice.
The following elementary argument proves precisely the needed replacement.

### Independent endpoint-path lemma

Suppose gamma_i:[0,1]->R^r are continuous, gamma_i(0)=0, and gamma_i(1)=v_i, for i=1,...,r, where the v_i are linearly independent.
Then

    S=gamma_1([0,1])+...+gamma_r([0,1])

has nonempty interior.
For each integer k extend gamma_i by gamma_i(t+k)=gamma_i(t)+k v_i.
Endpoint agreement makes the extension continuous.
If V has columns v_i, then

    F(t_1,...,t_r)=sum_i gamma_i(t_i)=Vt+g(t)

with g continuous, bounded and Z^r-periodic.
For any y, the continuous map t -> V^(-1)(y-g(t)) maps a sufficiently large closed ball into itself.
Brouwer's fixed-point theorem gives F(t)=y.
Thus F is onto and

    R^r=union_(k in Z^r)(S+Vk).

S is compact.
If its interior were empty, all these translates would be nowhere dense, contradicting the Baire category theorem.
This proves the lemma.
Brouwer and Baire are standard foundational inputs; no differentiability, rectifiability, simplicity or separation of the paths is assumed.

## Checked reconstruction of Theorem 1.1

Separate digit positions by residue modulo r:

    T(B,v)=sum_(j=0)^(r-1) B^j T(B^r,v).             (2)

The determinant hypothesis gives |det(B^r)|>=1/2.
To cover the possible loss of cyclicity under powers, let W be the B^r-invariant span of v,(B^r)v,... .
On W, v is cyclic for B^r.
Every eigenvalue of B^r on the quotient has modulus less than one.
Therefore

    |det(B^r|_W)| >= |det(B^r)| >= 1/2.

Here B is invertible under (1); the determinant factorization through W is valid.
If dim W>=2, the accepted Corollary 1.8 on W gives a path from 0 to v in T(B^r,v).
If dim W=1, that same conclusion is elementary: the scalar binary series is an interval when its contraction has absolute value at least 1/2, including a negative contraction.
This also handles r=1 for the converted interior criterion.

Let gamma be such a path.
By cyclicity of B, the r vectors v,Bv,...,B^(r-1)v form a basis: a dependence among these first r vectors would bound the entire cyclic span below r by the minimal-polynomial recurrence.
Hence gamma,B gamma,...,B^(r-1) gamma meet the endpoint lemma's hypotheses.
Their sum is a subset of (2) and has interior.
This proves the adopted interior statement at the displayed dependency scope.

## Conversion for G0001 and limits

For a real expanding cyclic pair (A,v), put B=A^(-1).
The attractor in [L G0035](../../../claims/Yin_C_G0239_v1.md#positive-volume-support-interface) is A^(-1)T(B,v), so it also has interior if

    |det A|^r<=2.                                    (3)

For multiplication by an algebraic unit on its full expanding real Minkowski space, v is the embedding of 1, distinct conjugates give cyclicity, and |det A|=M(p).
Complex conjugates count separately in r.
Thus r*m(p)<=log 2 is a sufficient interior condition; it is not a lower bound for m(p).
Positive volume then gives binary support entropy m(p) by the already checked L G0035 interface.
Weighted digit entropies remain separate.

The source's Remark 1.2 itself asks whether the dimension-dependent constant can be replaced by a dimension-independent one.
This audit does not claim its current open/closed status beyond the inspected source.
Neither (3), connectedness at |det A|<=2, nor interior proves a Mahler gap.
Failure of (3) only means that this sufficient theorem does not decide the input.
No many-digit Corollary 1.3, uniqueness-dimension classification, or assertion that interior implies a convex binary covering body is adopted.

## Search and review boundary

The 2026-10-07 search followed the unadopted interior lead in HS16b and the remaining question in L G0035.
Queries included self-affine attractors with interior, two maps, higher dimensions, determinant and Sidorov.
The primary arXiv record and complete Section 1 of the retained v4 supplied the needed theorem; the search stopped at that exact interface.
No novelty or absence claim is made.

The original coordinator, path-repair contributor and separate whole reconstruction findings are retained at [R_G528](../../reviews/Yin_R_G0528_v1.md#original-hs16-path-contributor-finding).
Their actual2026-10-07 scopes and connectedness-source limits remain separate; the known repair contribution is self-review and the two other initial arrangements are unknown.
The complete mathematical reconstruction and adopted source interface above remain unchanged.

## Current local mathematical review

The complete adopted statement, local endpoint-path replacement and affected interior/expanding/support chain now have the newly performed [R_G529 isolated finding](../../reviews/Yin_R_G0529_v1.md#isolated-hs16-corrected-chain-finding), recorded2026-10-21T05:57.
The independent first-stage inspection preceded comparison with the three old accounts and included the retained HS16 v4 pp.1–4 and the exact C_G239/accepted GBV15 support interfaces.
The old unrestricted path-sum counterexample remains valid; the original repair contributor remains self-reviewed and the two old arrangements remain unknown.
The new finding supplies present independent mathematical coverage without backdating those accounts or extending to the two original connectedness proofs, original GBV15 proof, unadopted many-digit results or a Mahler gap.
The original2026-10-07 inspection table and actual primary-version identity above retain their original roles.
