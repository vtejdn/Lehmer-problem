---
author: Yin
---
# Complete unbounded one-column exclusion in the ordered conference path basis

The complete original L250 theorem/proof is retained with the exact already proved L246 seed/model interface.
L250 preserves failed exploration, construction questions and the original fixed review inputs.
No Task or execution resumes.

## Statement

In the standard integer lattice Z^6 let

    G0=[[2,1,1,1,1,1],
        [1,2,1,-1,-1,1],
        [1,1,2,1,-1,-1],
        [1,-1,1,2,1,-1],
        [1,-1,-1,1,2,1],
        [1,1,-1,-1,1,2]],
    Q0=(e0,e1-e0,e2-e1,e3-e2,e4-e3,e5-e4).

For every i in{0,1,2,3,4,5} and every c in Z^6 with c_i in{+1,-1} and c^T(Q0^T G0 Q0)c=2, replace only column i of Q0 by Q0 c, obtaining Q.
Define V_aa=1, V_ab=(Q^T G0 Q)_ab for a<b, and V_ab=0 for a>b.
Then Q is unimodular and

    det(tV+V^T) != Phi6(t)(t^4-t^3-t^2-t+1)
                =t^6-2t^5+t^4-t^3+t^2-2t+1.

No coordinate, height or energy bound is imposed.
Signs are included, but the order and five unchanged columns are fixed.
Later reorderings, multicolumn changes, other lattices and other neutral factors are outside this assertion.
Every sign/full coefficient, finite failed test and nonempty survivor set is retained below, along with full original/absolute/cover factors and costs of both actual comparison controls.
No target realization, optimum, near-one coverage or unrestricted gap is asserted.

<a id="argument"></a>
## Complete argument

### Explicit seed, quadratic model and reflection order

Put C=G0-2I.
Direct multiplication gives C^2=5I and tr C=0, hence det G0=-1 and inertia(3,3).
Q0 has determinant1 and norm-two columns.
Map e_i to f0+f_(i+1) in E={y in F2^7:sum y_j=0} with q_E(y)=wt(y)/2 modulo2.
These six independent images have quadratic value one and pairwise polar product one, exactly the reduced data of q(x)=x^T G0 x/2, proving a quadratic isomorphism.
Appending coordinate zero and quotienting the even-weight subspace of F2^8 by its all-ones vector gives an isomorphism, since each class has a unique last-coordinate-zero representative.
Complementation changes wt/2 by an even integer, so the quadratic value descends.
The value-one classes have weights two or six and are exactly two-vertex edges after complementation.
Q0 gives the path0--1--2--3--4--5--6 with isolated vertex7.

For Gram G=V+V^T with norm-two basis vectors, reflection at coordinate i sends x to x-(Gx)_i e_i.
Apply indices5 down to0; later coordinates are already y_j and earlier ones remain x_j.
Then

    y_i=-x_i-sum_(j<i)G_ij x_j-sum_(j>i)G_ij y_j,
    V y=-V^T x.

The reflection product is therefore -V^(-1)V^T.
In the binary model an edge reflection exchanges its endpoints, because its polar pairing is y_a+y_b.
This proves the full characteristic-polynomial interface used in Section4 without a conference/Coxeter classification theorem.
HPM22 remains the original attribution only.

<a id="path-root-unbounded-reduction"></a>
### 1. Reuse boundary and the changed algebraic question

The current Task contract, S3/S6 and reuse/computation rules were read.
The relevant fixed input is [L246](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope), including its complete proof and independent review, actual conference Gram G0, path basis Q0, and exact old-orbit exclusion.
The existing [J53](../computations/programs/Yin_J_G0053/readme.md) author programs and native outputs were read without mutation.
The L191 Phi2^2 P4 control and the separate L242 coupling restriction remain comparisons, not new constructions.
L246's HPM22 attribution check and its direct seed proof are sufficient inputs here: no new conference existence/classification theorem or source acceptance is required for the following parameter substitution.

L246's second changed test used only the114 norm-two vectors in {-1,0,1}^6 and two path columns, giving228 pairs and no prescribed target.
The new question concerns the ENTIRE unbounded one-column replacement family in that same path basis, rather than a larger short-root cube.
Write Q0=(e0,e1-e0,...,e5-e4), with coordinates indexed0 through5.
Replacing column i by Q0 c gives an actual integer basis exactly when c_i=+1 or-1.
A sign change of that column leaves the polynomial unchanged, so c_i=1 suffices.
The new Gram is Q(c)^T G0 Q(c), and the replacement is admissible precisely when c^T(Q0^T G0 Q0)c=2.
Its upper-unitriangular reconstruction V(c) retains this Gram but is not asserted to be a congruent bilinear form.

The complete target is

    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    P4=t^4-t^3-t^2-t+1.

For every admissible basis, det(V+V^T)=det G0=-1.
Write the reciprocal full polynomial as

    p_V=t^6+a t^5+b t^4+c_0 t^3+b t^2+a t+1.

Then p_V(1)=-1 forces c_0=-3-2a-2b.
The alternating endpoint is

    p_V(-1)=5+4b=Pf(V-V^T)^2.

Therefore the ENTIRE polynomial equals F if and only if

    a=-2 and Pf(V-V^T)=+3 or-3.                 (1)

This uses the actual six-dimensional alternating determinant and the full symmetric endpoint, not only a congruence or numerical root check.
In the one-column family the alternating Pfaffian is linear in c, because every perfect matching uses that row/column once.
The coefficient a and the norm equation are quadratic in c: determinant expansion uses the varying row and column at most once each.
Thus a complete algebraic test consists of two integer quadratic equations and a linear Pfaffian equation after c_i=1.
A prospective bounded solve will be declared only after these exact equations have been displayed.
No execution or general solvability claim is made at this point.

<a id="one-column-exact-equations"></a>
### 2. Exact reduced equations and the first arithmetic discriminator

[J54](../computations/programs/Yin_J_G0054/readme.md) derives the equations from the displayed actual G0 and Q0 by exact symbolic multiplication, nilpotent inversion and recursive Pfaffian expansion.
It performs no root search in that derivation.
Write k=(5-Pf)/2, so k is1 or4.
For replacement of column3, put x=x0, y=x2-2x4, v=x4, z=x5.
The Pfaffian equation gives x1=5x+y-k.
The norm condition N=0 and coefficient condition A=a+2=0 reduce to N=0 and D=A-N=0, where

    D=x^2+4xy+y^2-kx-(k+1)y+k-3,
    N=21x^2+4xy-10xv+10xz-(9k+10)x+y^2
      -(k+1)y+v^2+(2k+3)v-3vz+z^2-(2k+2)z+k^2+2k.       (2)

These are exact integer equations, with no size or denominators suppressed.
Modulo3, D=(x-y)^2-(x-y)+1, so D=0 forces y=x+1.
On that residue condition,

    N=(v+x+1)^2+(z-x+1)^2 modulo3.

A sum of two squares vanishes modulo3 only when both vanish.
Therefore v=-x-1 and z=x-1, and the only residue triples (x,v,z) are(0,2,2),(1,1,0),(2,0,1).
At all three residues the gradients of D and N vanish modulo3.
Their values modulo9 are consequently unchanged by any lift of the four variables by multiples of3.
At y=x+1 the value D is6x^2+3x-3 when k=1 and6x^2-3x-3 when k=4.
Thus D=0 modulo9 permits only x=2 for k=1 and x=1 for k=4.
At representatives (x,y,v,z)=(2,3,0,1) and(1,2,1,0), respectively, N=3 modulo9.
This is a contradiction.

Hence NO integral one-column replacement at column3 can realize Phi6 P4, without any height, norm-coordinate or search bound.
Column sign normalization covers c_3=-1 too.
This is narrower than all root bases and broader than the228-pair old finite test.
The exact complete modular certificate checked all four systems (both columns and Pfaffian signs) modulo3 and9:26568 residue tuples.
Column3 has three survivors modulo3 and none modulo9 for each sign, while column2 has10 and90; its remaining family is not excluded by this argument.

For column2, put x=x0, b=x1, v=x4, w=x5, with x3=k-3v-w.
Its norm equation and the linear combination R=A+3N are

    N=x^2-xb+b^2+6bv+4bw-(2k+1)b+7v^2+12vw
      -(5k+5)v+4w^2-(4k+3)w+k^2+k,
    R=(4b+4v+8w-2k-4)x-4b^2-8bv-16bw+(4k+6)b
      -11v^2-28vw+(9k+5)v-20w^2+(12k+11)w
      -2k^2-2k-3.                                      (3)

The exact target condition is N=R=0.
A separately declared bounded test ranged only (b,v,w) in[-20,20]^3, both k values:137842 triples.
When the coefficient of x is nonzero, it solved for x by exact divisibility without imposing any size bound on x.
When it vanishes, an exact quadratic discriminant test covers every possible x.
The run completed all137842 triples, including838 singular linear cases and2953 nonsingular integral-x cases, and found no target.
This is an unsuccessful bounded parameter test, not an unbounded exclusion.
Its full declared scope and empty result are retained in J54.

Before any further continuous/root search, the remaining exact equations will be tested at the two-adic levels2,4,8, for the two signs:8736 residue tuples.
This is a specifically declared congruence discriminator for(3), not an enlargement of the old short-vector scan.
No result of this new test is asserted here before execution.

<a id="two-adic-whole-column-obstruction"></a>
### 3. A two-adic obstruction in the other central column

The declared8736 residue tuples were all checked.
For each Pfaffian sign, column2 has two solutions modulo2 and none modulo4 or8.
Here is a written proof independent of the finite table.
From(3),

    N = x(1+b)+kv+w modulo2,
    R = kv+w+1 modulo2.

Consequently N=R=0 forces x odd, b even and kv+w odd.
All four partial derivatives of R-N are even on those residue conditions.
Thus its value modulo4 is unchanged when any variable is changed by2.
Substituting x=1,b=0 and reducing v,w only modulo2 in the displayed exact expression gives

    R-N = 2(kv+w) modulo4,                               (4)

for k=1 or4: the remaining constant is -k(3k+5), divisible by4 in both cases.
The right side is2 modulo4, contradicting N=R=0.
This proves the entire unbounded column2 exclusion, including both signs of its primitive basis coefficient after column sign normalization.
The unsuccessful137842-triple test remains a discovery observation, not the premise of this proof.

<a id="all-path-column-completion"></a>
### 4. Every other single-column position and the complete theorem

The old central positions do not exhaust all possible replacements.
We now cover the remaining four positions by exact arithmetic, without another integer-box search.

First reuse the precise eight-coordinate model from L246: the norm-one classes of the reduced even quadratic lattice are the two-element subsets of eight vertices in the even-weight quotient by the all-ones vector.
The six path basis roots are the edges of a path on vertices0 through6, with isolated vertex7.
Removing column i deletes its path edge and leaves three tree components of sizes i+1,6-i,1.
The replacing norm-two root is an edge in this model.
Since an integral unimodular basis remains a basis modulo2, that edge cannot lie within a component or repeat an edge: a graph cycle would give a linear dependence.
It must join two components.
The resulting six-edge forest has two components.
Its six edge classes are independent in the quotient exactly when both component sizes are odd: the all-ones vector belongs to the edge span exactly when both component sizes are even, while before quotient the forest edges are independent.

For i=0 or5, the three sizes are1,6,1.
The only independent completion therefore has sizes7+1.
In any fixed ordering the corresponding reflection product is a7-cycle and a fixed point; on the even quotient its characteristic polynomial is Phi7 modulo2.
This is incompatible with the target Phi3 Phi5.
This excludes both end positions.
Positions1 through4 admit the3+5 partition, so the mod2 partition alone cannot exclude them; Sections2--3 supplied genuinely additional arithmetic for positions2--3.

For position1, exact Pfaffian expansion gives

    Pf(V-V^T)=5-10x0.                                    (5)

It is divisible by5 and cannot equal+3 or-3.
The rational solutions x0=1/5 or4/5 displayed by the symbolic elimination are NOT integral bases and are not treated as constructions.
No other coordinate bound is involved.

For position4 put x=x0,b=x1,c=x2,d=x3 and k=(5-Pf)/2 in{1,4}.
The Pfaffian equation gives x5=-2b+2d+k.
The exact norm equation and coefficient equation A=a+2 are

    N=x^2-xb+b^2+3bc-2bd-(2k+2)b+c^2-3cd
      -(2k+2)c+d^2+(2k+3)d+k^2+k,
    A=-3x^2+2xb+xc+xd-x-3b^2-8bc+7bd+(6k+4)b
      -5c^2+10cd+(8k+5)c-5d^2-(8k+5)d-4k^2-3.           (6)

Modulo2 they become

    N=x(1+b)+b(1+c)+c(1+d),
    A=x(c+d)+b(1+d)+1.

Their only common zero is(x,b,c,d)=(1,0,1,0).
To see completeness directly, if d=1 then A=0 forces x=1,c=0, and N=1.
If d=0 then A=0 gives b=1+xc; c=0 makes N=1, whereas c=1 forces x=1,b=0.
At this sole residue all four partial derivatives of A are even.
Every lift by multiples of2 has the same value modulo4, namely

    A(1,0,1,0)=-4k^2+8k-6 = 2 modulo4.                  (7)

Thus position4 is impossible too.
The separately declared complete13828-tuples comparison at moduli2,4,3,9 corroborates this exact distinction: the two signs each have1,0,10,90 survivors, respectively.
The mod3/mod9 survivors are retained; they are not silently discarded or claimed to vanish.

Together these arguments prove the following complete restricted theorem.
Start with the actual ordered path basis Q0 of the L246 conference lattice.
Replace ANY ONE of its six columns by ANY integer norm-two vector, requiring the new basis to be unimodular.
Reconstruct the standard integer upper-unitriangular V from the resulting Gram.
Then

    det(tV+V^T) is not Phi6 P4.                           (8)

There is no coefficient, height, energy or coordinate bound.
Independent sign changes of columns do not affect this statement: V changes by diagonal sign congruence and the determinant polynomial is unchanged.
The column order in(8) is fixed.
Arbitrary reordering after replacement, simultaneous changes of two or more columns, reflections that also change the other columns, different integral lattices and other cyclotomic multipliers are OUTSIDE this theorem.
In particular it does not exclude all bases having the admissible3+5 reduced partition or all rank-six upper-unitriangular matrices.
It is compatible with L246's successful different sextic from one column, because that polynomial has b=-1 and alternating endpoint1 rather than the target's b=1 and endpoint9.

<a id="path-column-costs-and-open-construction"></a>
### 5. Full costs, useful limitation and the changed next test

No new realization was produced in this round.
The intended entire target is Phi6 P4, with degree6, neutral degree2 and original measure log beta_4.
These are properties of the requested polynomial, not an achieved V.
A hypothetical such V would have a rank12 literal cover and the complete extra factor det(tV^-+(V^-)^T); that factor and its measure are unknown, and no small cost is assigned to it.

The actual known comparison remains L191: rank6, height1, energy5, complete polynomial Phi2^2 P4, identical absolute companion, and rank12 height1 energy10 cover with complete polynomial Phi2^4 P4^2 and measure2log beta_4.
The current exclusion does not change that realization.
L246 also still provides its actual different irreducible no-padding sextic P_new=t^6-2t^5-t^4+3t^3-t^2-2t+1, standard integral root basis, rank6 height2 energy24, and complete absolute polynomial t^6-38t^5-61t^4-69t^3-61t^2-38t+1.
Its rank12 height2 energy48 cover is their whole product, with measure log lambda+log rho, beta_4<lambda<2 and38<rho<40; companion/original>5 and cover/original>6.
No factor in either actual control has been deleted, rescaled or reclassified as zero cost.

The new gain is a full unbounded obstruction that survives the3+5 binary partition for this ONE-COLUMN construction.
It justifies changing the construction instead of enlarging the previous short-root cube or repeating the same reflection orbit.
A discriminating future test is a simultaneous two-column replacement, imposing the exact2-by-2 replacement minor equal to+1 or-1 and both norm-two equations before the full coefficient/Pfaffian equations.
Different orderings or a different seed are also legitimate.
This is a next question, not a claim that such a construction succeeds, that a uniform coverage theorem is necessary before experimenting, or that this restricted exclusion suspends the route.
The unrestricted Lehmer gap and near-one realization problem remain unresolved.

### Complete coefficient certificate and its limits

Only one row/column of V varies linearly, so determinant coefficients have total degree at most two in five free variables; the Pfaffian is linear.
The21 points0,e_i,2e_i,e_i+e_j determine all constant, linear, square and mixed coefficients.
J54/verify.py computes84 full polynomials at these points for positions1--4, including24 actual norm-two endpoint checks.
This is a different calculation by the same original author, not independent agent review.
The written modular/parity argument above proves the unbounded assertion; the bounded unsuccessful search does not.

## Current assessment

[Selected decision](#decision-complete-home-open)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:43 |
| status | open |
| reason | Retain the complete six-position proof, exact seed/model, both signs, finite failures and full costs pending actual whole checking of this fixed Claim. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Theorem](#statement) | Every integer norm-two replacement at all six fixed positions, without coordinate bound; full target and exclusions. |
| argument | [Whole proof](#argument) | Explicit seed/model/reflection interface, full Sections1--5/equations1--8, all lifts/end forest proof, exact certificate and all cost/scope limits. |
| support | [Native evidence](../computations/programs/Yin_J_G0054/readme.md) | Seven author programs/outputs, every survivor list and bounded failed solve, separately implemented reviewer checker, all at original finite domains. |
| support | [Lattice and sextic](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Direct original seed/model and actual original/absolute/cover comparison costs; no new source theorem or target realization. |
| support | [Quartic control](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Existing k4 rank6/height1/energy5 realization, identical companion and complete rank12 cover. |
