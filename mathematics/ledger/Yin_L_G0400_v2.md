---
author: Yin
---
# Salem unit regulators and exterior products: exact packet equality and ambient-degree costs

<a id="salem-unit-exterior-comparison"></a>
## Scope and retained comparison

This 2026-11-05 exploration for [G0001](../tasks/Yin_T_G0001_v1.md#contract) asks whether simultaneous independence of Salem conjugate units supplies an arithmetic gain that the earlier rank-one regulator comparison did not provide.
The assigned strategic-discovery agent developed the source comparison and direct calculations for Yin and checked their normalization.
These are author calculations and ordinary checks, not an independent project review, a new Claim assessment or a proof of a uniform Mahler gap.
The domain below consists of genuine Salem numbers only; no reduction of unrestricted reciprocal inputs to that domain is asserted.

The earlier [relative-regulator comparison](Yin_L_G0400_v1.md#salem-regulator-finding) remains fixed.
Its complete mathematical home is [C485](../claims/Yin_C_G0485_v1.md#argument), with its selected complete SELF review retained there.
In particular, the normalized relative regulator of the full Salem field equals the logarithm of its smallest Salem generator, whereas the ordinary regulator ratio includes a degree-dependent power of two and a unit index.
This version reuses those conclusions and their source/review limits without copying the old proof or replacing its assessment.

The [C165 monomial argument](../claims/Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) already supplies independence of inverse-pair representatives modulo torsion.
Its [complete-packet supplement](../claims/Yin_C_G0165_v1.md#complete-salem-packet-specialization) records the sparse embedding geometry and the distinct coordinate/projective heights.
That supplement is expressly outside the family's selected original monomial statement and old review scope.
The direct calculation below checks the particular embedding and exterior norms needed here, without transferring that older review to this version.
The only nontrivial group-size input used below is [C383's actual Salem sign-kernel statement](../claims/Yin_C_G0383_v1.md#statement), at its retained assessment and CM10 source scope.

<a id="av24-inspected-source"></a>
## AV24 source, exact statements and inspection limits

The source is Shabnam Akhtari and Jeffrey D. Vaaler, [A bound for the exterior product of S-units](https://arxiv.org/html/2009.10857v2), arXiv:2009.10857v2, revised 19 October 2023.
The work was published in Algebra & Number Theory 18(9) (2024), 1589--1617, DOI [10.2140/ant.2024.18.1589](https://doi.org/10.2140/ant.2024.18.1589), and is recorded as AV24 in the canonical bibliography.
The actual inspected original was the online arXiv v2 HTML, Sections 1--2, including equations (1.1)--(1.16), Theorems 1.1--1.2 and Conjecture 2.1.
The published rendering is not asserted to be byte-identical or mathematically identical throughout to that preprint.
No local original download, original-proof review or whole-paper audit is claimed.

The 2026-11-05 bounded search followed the question whether several conjugate units can supply a lower-volume input unavailable from one relative-unit direction.
It compared the existing C165, AM16, Del09 and L400 source interfaces, then used conjugate-unit/regulator/exterior-product terms and the exact AV24 title.
Reading the exact source constants and applying them to the original packet was sufficient to stop this comparison.
This is not an exhaustive literature or novelty claim.

For a number field k and a finite set S of places containing every archimedean place, the source puts r=|S|-1 and uses the unnormalized weighted logarithmic vector

    v(u)=(d_v log ||u||_v)_(v in S),
    d_v=[k_v:Q_v],
    ||v(u)||_1=2[k:Q] h_abs(u).                    (AV1)

Here ||.||_v extends the usual rational absolute value.
The quotient of the S-unit group by its roots of unity maps to the lattice Gamma_S(k).
The exterior l1 norm is the sum of the absolute values of the coordinates in the standard wedge basis, equivalently the sum of the absolute values of the maximal minors of the column matrix.
The exterior l2 norm is the square root of the sum of their squares.

For q multiplicatively independent S-units, with 1<=q<=r, Theorem 1.1 states

    ||v(u_1) wedge ... wedge v(u_q)||_1
      <=2^(-q) C(q,r) product_i ||v(u_i)||_1,

    C(q,r)=min{2^q,
               ((r+1)/(r+1-q))^(r+1-q)}.          (AV2)

The source explicitly gives C(q,r)=2^q when 2q<=r+1.
Thus this range has coefficient one in front of the product of vector norms.
The height form of the same inequality uses the ambient factor [k:Q] for every unit; it does not use the unit's own degree in its place.

For a rank-q subgroup A of Gamma_S(k), Theorem 1.2 constructs a rank-q subgroup B of A, with generators w_1,...,w_q, such that

    [A:B]<=q!,
    ||w_1 wedge ... wedge w_q||_1
       =[A:B] ||v_1 wedge ... wedge v_q||_1,
    product_i ||w_i||_1
       <=q! ||v_1 wedge ... wedge v_q||_1,          (AV3)

where v_1,...,v_q are generators of A.
In particular B is contained in A.
The theorem does not introduce arbitrary units of k or rational division of vectors in A.

Conjecture 2.1, attributed there to F. Rodriguez Villegas, proposes absolute c_0>0 and c_1>1 such that

    ||v_1 wedge ... wedge v_q||_1>=c_0 c_1^q       (AV4)

for independent ordinary-unit logarithmic vectors in their ambient field.
The source labels (AV4) a conjecture.
It is not an established input in this comparison.

<a id="actual-salem-exterior-norms"></a>
## Direct exterior calculation on the actual Salem packet

Let alpha>1 be a genuine Salem number of degree d=2t>=4, with monic irreducible minimal polynomial P.
Its roots are alpha, alpha^(-1), and d-2 distinct roots on the unit circle, arranged into t inverse pairs.
Put m=log alpha>0, let L be the splitting field inside C, and write D=[L:Q].
Choose representatives u_1,...,u_q of distinct inverse pairs, where 1<=q<=t.

The field L contains a nonreal root of P because d>=4.
Since L/Q is normal, every embedding of L into C has image L.
If one such embedding were real, it would follow that L is contained in R, a contradiction.
Thus L is totally imaginary and has exactly D/2 archimedean places, each of local degree two.
For S consisting of those places, the source's ambient unit rank is

    r=D/2-1.

For an archimedean place v represented by an embedding sigma_v:L->C, define

    v_i=(2 log |sigma_v(u_i)|)_(v in S).           (SP1)

This is independent of the choice between the two conjugate embeddings representing v.
Every u_i is an algebraic integer unit, so finite-place terms vanish and (SP1) is exactly (AV1).

Transitivity on the d roots implies that precisely D/d embeddings of L send a fixed u_i to alpha, and precisely D/d send it to alpha^(-1).
These two sets are disjoint.
At each of their 2D/d embeddings the logarithm has absolute value m; at every other embedding it is zero.
Complex-conjugate embeddings have the same absolute value, so passing from embeddings to archimedean places halves this support count.
Consequently v_i has exactly D/d nonzero coordinates, each equal to +2m or -2m, and

    ||v_i||_1=2m D/d,
    ||v_i||_2=2m sqrt(D/d).                         (SP2)

The supports of the distinct vectors v_i are disjoint.
Indeed, an embedding permutes the inverse pairs of P and can send only one selected pair to the unique real pair {alpha,alpha^(-1)}.
For the complete packet q=t, precisely one column is nonzero in each row; for a selected subpacket there can also be zero rows.
Disjoint nonempty supports prove real linear independence of the columns, and hence multiplicative independence of the units modulo roots of unity.

Consider the (D/2)-by-q matrix with columns v_i.
A q-by-q minor is nonzero exactly when its rows include one coordinate from each of the q supports.
For each support there are D/d choices, and the supports are disjoint, so there are exactly (D/d)^q nonzero minors.
Each such minor has absolute value (2m)^q: after a row permutation the selected matrix is diagonal with entries +2m or -2m.
All other maximal minors vanish.
It follows that

    ||v_1 wedge ... wedge v_q||_1
      =(2m)^q (D/d)^q=(2m D/d)^q,

    ||v_1 wedge ... wedge v_q||_2
      =(2m)^q (D/d)^(q/2)
      =(2m sqrt(D/d))^q.                            (SP3)

These identities retain the local complex weight two and the complete ambient embedding multiplicity.
Replacing D by d in (SP2)--(SP3) would change the source's logarithmic lattice.

<a id="actual-av24-upper-equality"></a>
## The upper bound is an equality throughout the actual packet range

C383 applies to every genuine Salem P used above.
If H is the transitive action on its t inverse pairs and V is the kernel, then D=|V||H| and |H|>=t.
For even t, V is the full sign group F_2^t.
For odd t, V contains the even-weight sign subgroup, so |V|>=2^(t-1).
No full symmetric pair action or splitting of the group extension is required.
Thus

    D>=t 2^t       when t is even,
    D>=t 2^(t-1)   when t is odd.                   (SP4)

For t=2 the first bound gives D>=8=4t.
For every odd t>=3 the second gives D>=4t.
For even t>=4 the first also gives D>=4t.
Hence, for every allowed q,

    2q<=2t<=D/2=r+1.                               (SP5)

In particular q<=r, so every hypothesis of Theorem 1.1 is satisfied.
Its coefficient in (AV2) is exactly one by (SP5).
Using (SP2)--(SP3) gives

    ||v_1 wedge ... wedge v_q||_1
       =product_i ||v_i||_1.                       (SP6)

Therefore the new upper inequality is attained by the actual packet.
This application supplies no strict gain from its joint independence or disjoint supports.

<a id="original-conjugate-unit-group"></a>
## Subgroup selection cannot shorten the original directions

Let

    A=Z v_1+...+Z v_q.

The units giving this logarithmic subgroup are precisely the products of the selected u_i with integer exponents, modulo roots of unity.
For every integer vector a=(a_1,...,a_q), disjoint supports give the exact formula

    ||sum_i a_i v_i||_1
       =(2m D/d) sum_i |a_i|.                       (SP7)

For a nonzero vector of A at least one integer coefficient is nonzero.
Its l1 norm is therefore at least 2mD/d, with equality already attained by each v_i.
For q independent vectors w_1,...,w_q in any subgroup B of A, each vector is nonzero, so

    product_i ||w_i||_1
       >=(2mD/d)^q
       =||v_1 wedge ... wedge v_q||_1.             (SP8)

The original generating set already attains this lower value.
Consequently the subgroup and generators supplied by Theorem 1.2 cannot improve this minimum.
Its q! upper allowance is unnecessary for the original packet and cannot be interpreted as a factor that lowers its height.
This conclusion concerns the integer group A only.
It does not classify its primitive saturation, units outside A, or transformations with a separately justified change of field and degree.

<a id="conjectural-lower-return"></a>
## Even the proposed ambient lower bound retains its degree expense

For comparison only, assume the conjectural inequality (AV4) for this packet.
Combining it with (SP3) gives exactly

    m>=(d/(2D)) c_0^(1/q) c_1.                      (SP9)

This is the floor delivered by that particular ambient application.
It is not a bound from an accepted theorem.
From (SP4),

    D/d>=2^(t-2)

for every t>=2, with a stronger estimate for even t.
Also c_0^(1/q)<=max{1,c_0}.
Thus the right side of (SP9) tends to zero as t tends to infinity, uniformly over 1<=q<=t.
The calculation establishes a loss in this certificate, not the existence of Salem numbers with m tending to zero.

Conjecture 2.1 itself includes Lehmer's problem by taking q=1 in an algebraic unit's own field.
Nothing here disputes that implication.
The failed return is specifically the attempt to obtain an extra gain by placing several original conjugates in their much larger common field L.
Likewise, the l2 identity in (SP3) retains a factor sqrt(D/d) per direction; passing to that norm does not erase the ambient multiplicity.

<a id="unit-exterior-outcome"></a>
## Outcome and reopening condition

The simultaneous-unit approach uses a different object from the integral auxiliary, carry process or finite original core.
However, this actual source application changes none of their unresolved original-input coverage.
The two proved AV24 inequalities yield exact packet equality and a selection inside an integer group whose shortest nonzero directions are already supplied.
The proposed lower inequality remains conjectural, and its direct common-field return retains the explicit D/d loss.

This extends the L400 normalization comparison without replacing its rank-one result or the C165/Del09 packet boundaries.
It rules out obtaining a new gain merely by applying AV24 Theorems 1.1--1.2 to these original conjugate units, optimizing their displayed constants, or changing the integer generators of A.
It does not rule out another arithmetic theorem or a construction outside that group.
Reopening would require a concrete new arithmetic object or operation with its actual field, unit property, degree and total-Mahler return supplied; a new name for a uniform regulator lower bound would not provide that input.
No additional conjecture, computation, field construction or source-proof reconstruction is selected by this fixed comparison.
