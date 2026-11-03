---
author: Yin
---

# Actual finite-deletion nonclosure and the boundary excursion criterion

Human author Yin.
Root proposed testing the universal boundary closing-path hypothesis and the replacement by a fully paid finite-boundary mechanism.
Contributor characteristic_zero_bridge derived the actual two-state and first-two-distance-core nonclosure examples BC1--BC4, including the alternative forced-prefix identity.
Contributor core_feedback_structure derived the finite-boundary excursion matrix, strongly connected component criterion, explicit bounds, two generic acyclic counterexamples and paid critical finite-coupling argument BA1--BA10.
Root read and checked these complete author arguments before their fixed extraction.
The current adopted assessment is [the whole-reviewed decision](#decision-whole-reviewed-2026-10-28), selecting [whole independent R1061](../audits/reviews/Yin_R_G1061_v1.md#whole-boundary-criterion-finding).
The actual diagonal and acyclic-crossing estimates remain unresolved; the strict-radius and finite-mean implication retains both hypotheses.

## Statement

### General original-clock conventions

Let D be a countable state set with distinguished0 and P a substochastic kernel having finitely many positive successors at every state.
Write P_D=P when emphasizing that D is the allowed state set.
For a finite K containing0 put G=D minus K and B_K=P restricted to G, without row renormalization.
Assume its outside entrance set U={u in G:P(a,u)>0 for some a in K} and exit set V={v in G:P(v,b)>0 for some b in K} are finite, and set A=U union V.
Every path weight is the product of ORIGINAL edge probabilities; a chronological path of length l has generating weight p(w)z^l.
Let E_n(a,b) be the total weight of paths from a to b in K whose first positive visit to K occurs at chronological time n, so

    E_1(a,b)=P(a,b),
    E_n(a,b)=sum_(u,v in G)P(a,u)B_K^(n-2)(u,v)P(v,b), n>=2,
    E_K(z)=sum_(n>=1)E_n z^n.

Let d_n=sum_(x in G)B_K^n(x,x), and assume every d_n is finite wherever its root-limsup is used.
Write D_K(t)=sum_(n>=1)d_n t^n, allowing infinity.
For u,v in A, let Lambda_uv(z) sum all positive-length G-paths from u to v with no intermediate visit to A, and let Gamma_uv(z)=sum_(m>=0)B_K^m(u,v)z^m.
All formal identities below are identities of nonnegative original-word series, and all assertions of finite evaluated matrices require their stated hypotheses.

### Exact conclusions

1. The complete boundary matrix satisfies Gamma_AA=sum_(k>=0)Lambda^k and E_K=zP_(K,K)+z^2P_(K,A)Gamma_AA P_(A,K).
   Condensing the finite graph of nonzero Lambda entries into strongly connected components gives the exact finite directed-acyclic product expansion BA3.
   No component is inferred from a finite approximation to the infinite exterior graph.
2. At any t>0 with D_K(t)<infinity, all entries of Gamma_AA(t) are finite if and only if every cross-component Lambda_uv(t) is finite.
   The within-component connector bound BA5 and finite product bound BA6 retain all fixed positive connector weights and chronological shifts.
   With alpha=limsup_n d_n^(1/n) and chi the maximum coefficient root-limsup of the finitely many crossing series, every boundary coefficient sequence B_K^n(u,v) has root-limsup at most max(alpha,chi).
   Use chi=0 when there are no crossing series and the usual infinite-radius convention when the maximum vanishes.
   In particular polynomial crossing series transfer a diagonal exponential estimate to every boundary entry.
3. For the ACTUAL quartic model specified below, a supplied finite K and t_*>R satisfying D_K(t_*)<infinity and finiteness of every crossing series imply R_f>R, a positive exponential moment of the actual critical first-return law and finite critical mean.
   BA10 proves this through the recurrent critical H-transform, paid finite killing and an explicit positive delta with F(R+delta)<infinity; finiteness of E_K(t_*) alone is not mistaken for convergence of all repeated nonzero-K visits at t_*.
   These diagonal and crossing hypotheses are NOT established for any new actual K or parameter by the present theorem.
4. The actual universal closing-path hypothesis is false.
   For K={0,beta^(-1)}, the relevant outside pair(1,-b) has B_K^6(1,-b)>=1/2048 and E_8(0,beta^(-1))>=1/32768, but there is no outside path from-b back to1 and B_K^j(1,1)=0 for every j>=1.
   For the actual distance cores C_1={+/-beta^(-1)}, C_2=C_1 union{+/-b} and K_j={0} union C_j, the analogous relevant pairs are(1,b) and(1,a), with E_4(beta^(-1),-beta^(-1))>=1/128 and E_3(beta^(-1),b)>=1/32.
   Both original nonzero core matrices are nilpotent, so their geometric series converge at every t>0.
   Nevertheless the alternative exact identity B_(K_2)^m(1,a)=(1/4)B_(K_2)^(m-1)(a,a), m>=1, transfers this particular pair to the other endpoint's diagonal.
5. The two complete generic acyclic counterexamples in BA8--BA9 exclude a purely formal removal of the crossing-series condition.
   One is an irreducible recurrent stochastic chain with finite predecessor/successor degrees and finite shortest-distance levels, all deleted diagonals zero and every finite nonzero distance core nilpotent, but R_f=R=1 and infinite critical mean.
   The other uses only nonzero probabilities1/4 and1/2 and still has zero deleted diagonals but boundary root-limsup1/2.
   Neither graph is the actual quartic affine system.

If A is empty, the exterior term in E_K vanishes and the boundary assertions are vacuous.
The actual conditional consequence handles K={0} separately without an empty-matrix maximum.
The statement supplies neither a counterexample to an actual quartic tail estimate nor an actual strict radius gap, critical-mean classification, all-large-core conclusion or unrestricted G0001 solution.

### Actual quartic model and radii

Fix q(X)=X^4-X^3-X^2-X+1 and its exterior root beta with17/10<beta<18/10.
Use O=Z[beta], the expanding and contracting embeddings x_+,x_-, and the actual core

    D={x in O: |x_+|<B, |x_-|<S},
    B=1/(beta-1), S=beta/(beta-1).

Original transitions are x->beta*x+e, with p_0=1/2 and p_(-1)=p_1=1/4; successors outside D are killed.
The symbols B_K for a kernel and B for the strip constant have these separate indicated roles.
Set a=beta-1, b=beta^(-2)(beta-1), and let d(x) be original shortest distance to0.
Let F(z)=sum_(n>=1)f_n z^n be the COMPLETE original first-return series, U(z)=sum_(n>=0)P^n(0,0)z^n the complete return series, and R_f and R their respective radii.
The actual critical facts reused in the conditional implication are F(R)=1, H(0)=1,0<H<=1 and the recurrent stochastic kernel Q(x,y)=R P(x,y)H(y)/H(x), with H the complete original first-hit function at R.

## Exact inputs and extraction scope

[C785](Yin_C_G0785_v1.md#complete-argument) supplies the exact actual zero-level graph, all incoming/outgoing rows used below, membership of +/-a and +/-b, and the retained strip and root-bound conventions.
[C546](Yin_C_G0546_v1.md#actual-periodic-congruence-diagonal) supplies the unique affine fixed-point convention used to justify finite actual deleted diagonals; no arithmetic tail upper bound is imported.
[C590](Yin_C_G0590_v1.md#critical-escape-reuse) supplies only the actual critical recurrent H-transform and its original chronological weighting for the final conditional finite coupling.
[C796](Yin_C_G0796_v1.md#statement) supplies only R<beta in the final illustrative sufficient rate condition; its finite numerical certificate is not a new computation here.
[C234](Yin_C_G0234_v1.md#cycle-counting-bound) is credited for the already used elementary finite component/block-triangular mechanism.
[C838](Yin_C_G0838_v1.md#original-clock-definitions) supplies the distance-core convention and a comparison with its already proved conditional resummation; the present nonclosure examples do not contradict that theorem.
The general boundary proof below is self-contained and invokes no new pressure-at-infinity or stochastic-complement theorem.
No literature novelty is asserted.

The two arguments were developed at [D9's actual nonclosure section](../drafts/Yin_D_G0009.md#finite-deletion-boundary-nonclosure) and [boundary-condensation section](../drafts/Yin_D_G0009.md#finite-boundary-condensation-and-acyclic-channels).
Those links record extraction provenance only; no mutable Draft supplies a proof premise.
All necessary actual derivations, general word arguments, constants, counterexamples and conditional coupling are retained in this fixed material.
The examples are hand calculations with no J or native output input.

## Complete argument

<a id="actual-diagonal-word-finiteness"></a>
### Actual diagonal finiteness without a tail estimate

For a chronological digit word w=(e_1,...,e_n), put S(w)=sum_(j=1..n)e_j beta^(n-j).
The affine n-step map has the unique possible fixed starting state x(w)=-S(w)/(beta^n-1), because beta>1.
Thus for every actual finite deletion K,

    d_n=sum_w p(w) 1_(every cyclic state of w lies in D minus K),
    0<=d_n<=sum_w p(w)=1.

Nonintegral fixed points contribute zero, and there are at most3^n contributing starting states.
This is the original finite word identity credited to C546, not a trace-class operator assertion or an exponential tail bound.

<a id="actual-boundary-rows"></a>
### BC1. Exact states, edges and predecessors

Keep the same quartic beta, actual strict core D and original digit probabilities p_0=1/2 and p_+=p_-=1/4.
Write a=beta-1 and b=beta^(-2)(beta-1).
The adopted bound 17/10<beta<18/10 implies beta^2-beta-1>0 and hence

    0<b<beta^(-1)<a<1.

Thus these four positive states, their negatives and zero are pairwise distinct.
C785 places all of them in the actual core.
The quartic identity gives beta*a-1=b and beta*b-1=-beta^(-1), so the original path and its negative are

    1 ->a ->b ->-beta^(-1) ->-1,
    -1 ->-a ->-b ->beta^(-1) ->1.

Each displayed four-edge path has chronological digits respectively(-1,-1,-1,0) or(1,1,1,0), and weight1/128.
All possible predecessors of1 are0,beta^(-1),2beta^(-1).
The last is outside D: its contracting coordinate has magnitude2beta, which exceeds S=beta/(beta-1) since1/(beta-1)<2.
Consequently the ONLY actual predecessors of1 are0 and beta^(-1), with respective edge weights1/4 and1/2.
Also1 has the ONLY legal successor a, with weight1/4, by C785's complete outgoing row.
No omitted edge is renormalized.

<a id="actual-two-state-nonclosure"></a>
### BC2. The proposed two-state deletion

Take K={0,beta^(-1)}, G=D minus K, and B_K=P_D restricted to G.
The relevant boundary pair u=1,v=-b has the wholly outside six-edge path

    1 ->a ->b ->-beta^(-1) ->-1 ->-a ->-b,
    digits=(-1,-1,-1,0,1,1), weight1/2048.

Every state on this path is distinct and avoids K by BC1.
Its entrance0->1 and exit-b->beta^(-1) each have weight1/4.
Thus the original first-return-to-K coefficients defined in the statement satisfy

    B_K^6(1,-b)>=1/2048,
    E_8(0,beta^(-1))>=1/32768.

Since all actual predecessors of1 lie in K, no positive-length path in G can end at1.
In particular there is NO path from v=-b to u=1 in G and B_K^j(1,1)=0 for every j>=1.
Therefore no fixed positive closing-path weight c and length ell>=0 can justify the universal closing-path comparison c B_K^m(1,-b)<=B_K^(m+ell)(1,1) for all m; it already fails at m=6.
This is an actual relevant entrance/exit pair, not merely a pair of states in different abstract graph components.

<a id="actual-distance-core-nonclosure"></a>
### BC3. Exact first two distance cores

Let d be the original shortest distance to zero and C_j={1<=d<=j}, as in C838.
C785's complete predecessor rows at0 and at+/-beta^(-1) give

    C_1={+beta^(-1),-beta^(-1)},
    C_2=C_1 union{+b,-b},
    d(+/-b)=2, d(+/-a)=3, d(+/-1)=4.

For completeness, the only nonzero predecessors of0 are+/-beta^(-1).
The only actual predecessors of either+/-beta^(-1) are the opposite-sign b states; the two other algebraic candidates are outside the strict strip, as proved in C785.
Thus the first two displayed levels are complete.
The state a is not in C_2 by BC1 and reaches zero through b,-beta^(-1) in three steps, so d(a)=3; sign symmetry gives d(-a)=3.
The unique outgoing row at+/-1 then gives d(+/-1)=4.

To compare C838 with the boundary-return construction, delete K_j={0} union C_j, so the exterior G_j={d>j} is exactly the exterior of the zero-killed distance-core construction.
For j=1, take u=1,v=b.
The path1->a->b stays in G_1, and the genuine NONZERO core entrance beta^(-1)->1 and exit b->-beta^(-1) have weights1/2 and1/4.
Therefore

    B_(K_1)^2(1,b)>=1/16,
    E_4(beta^(-1),-beta^(-1))>=1/128.

For j=2, take u=1,v=a.
The path1->a stays in G_2, while beta^(-1)->1 and a->b are a nonzero core entrance and exit.
Consequently

    B_(K_2)(1,a)=1/4,
    E_3(beta^(-1),b)>=1/32.

For both j=1,2, all actual predecessors of1 are deleted.
Thus there is no outside path v->1 and all positive-length diagonal entries at1 vanish, just as in BC2.
Both pairs really occur in the finite-core feedback, without using an entrance from0 instead of a nonzero core state.

These examples satisfy the original core convergence condition for EVERY t>0.
Indeed P_(C_1,C_1)=0, and the only within-C_2 edges are b->-beta^(-1) and-b->beta^(-1), each of weight1/4.
It follows that P_(C_2,C_2)^2=0, so both original matrix geometric series are finite sums.
The failure of the universal closing-path hypothesis therefore occurs inside C838's actual nested-core setting m=1,n=2, not because a convergence hypothesis was unpaid.

<a id="nonclosure-limit-and-forced-prefix"></a>
### BC4. What fails and what remains possible

The universal assertion that every relevant ordered outside boundary pair has a fixed outside path from its exit state back to its entrance is false, both for arbitrary finite deletions and for the actual distance-core family.
This disproves the proposed universal closing-path mechanism for transferring deleted-diagonal estimates directly to all boundary entries.
It does NOT refute C838, whose shell elimination and supersolution transfer use complete original word partitions and never assume the failed closing-path property.
It also supplies no failure at the particular distance-eight core, no statement for every sufficiently large core, and no critical-mean or first-return-radius conclusion.

Even for the displayed pairs, a different diagonal comparison may exist.
For example the unique first step from1 gives the exact identity

    B_(K_2)^m(1,a)=(1/4) B_(K_2)^(m-1)(a,a), m>=1.

Thus the same distance-two pair whose exit cannot return to its entrance has its open-path tail controlled exactly by a diagonal at the OTHER endpoint, after removing one forced step.
The absence of the particular closing path must not be promoted to an impossibility of all diagonal-tail comparisons or of other finite-boundary couplings.
The actual distance-eight exterior and every larger core retain their own unresolved boundary structure and tail-comparison obligations.

<a id="finite-boundary-excursion-matrix"></a>
### BA1. Definition and exact finite-boundary first-return matrix

Keep a finite K containing0, G=D minus K and the ORIGINAL killed kernel B=B_K=P_D restricted to G, without row renormalization.
Let U={u in G:P_D(a,u)>0 for some a in K} and V={v in G:P_D(v,b)>0 for some b in K}, and put A=U union V.
These sets are finite for the actual quartic because every original state has at most three successors and at most three predecessors.
If A is empty, the boundary-return formula has no exterior term; below assume A is nonempty.
The same construction applies to any countable finite-row substochastic law with these finite boundary sets.

For u,v in A let lambda_l(u,v) be the total ORIGINAL weight of length-l paths from u to v that stay in G and have no intermediate visit to A.
Define the finite matrix of formal nonnegative series

    Lambda_uv(z)=sum_(l>=1)lambda_l(u,v)z^l,
    Gamma_uv(z)=sum_(m>=0)B^m(u,v)z^m.

The constant coefficient of Lambda is zero.
Splitting each finite G-path at all of its visits to A gives exactly

    Gamma_AA(z)=sum_(k>=0)Lambda(z)^k.                  (BA1)

At each fixed chronological length only finitely many k and finitely many original paths starting at a fixed u contribute.
Thus BA1 is first a coefficientwise word identity, and then an identity of extended nonnegative sums at positive z.
The power k counts visits only for the partition; the factors z^l keep every original chronological step.
No inverse or convergence is presumed.

Writing E_K(z)=sum_(n>=1)E_n z^n for the first-positive-return-to-K matrix defined above gives exactly

    E_K(z)=z P_(K,K)+z^2 P_(K,A) Gamma_AA(z) P_(A,K).   (BA2)

Both entrance and exit edges are paid once, and all repeated exterior visits to A remain in Gamma.
The matrices P_(K,A) and P_(A,K) include their zero entries; replacing U,V by their union introduces no new word.

<a id="finite-boundary-condensation-criterion"></a>
### BA2. Finite condensation, with the previously missing channels explicit

**Definition (boundary communication graph).**
Form the directed graph on the FINITE set A with arrow u->v precisely when Lambda_uv is not the zero series.
Its reachability is exactly original reachability between those boundary states through G, because every G-path splits into A-excursions.
Let I_1,...,I_s be its strongly connected components and order them so that arrows between different components form a directed acyclic graph.
The partition is defined using actual whole-exterior paths; a finite induced graph or incomplete search does not certify it.

For each component set H_i(z)=sum_(k>=0)Lambda_(I_i,I_i)(z)^k.
A path can leave a component at most once, so the exact block expansion is

    Gamma_(I_i,I_j)(z)
      =sum_(component paths i=i_0->...->i_r=j)
         H_(i_0)(z) Lambda_(i_0,i_1)(z) H_(i_1)(z)
              ... Lambda_(i_(r-1),i_r)(z) H_(i_r)(z).  (BA3)

The r=0 term is H_i when i=j.
Every component path has distinct vertices and r<=s-1, so BA3 has only finitely many summands.
The formula follows by grouping the consecutive visits belonging to each component in BA1.
It remains a formal nonnegative word identity before any evaluation or analytic claim.

Put d_n=t_n(K)=sum_(x in G)B^n(x,x), and suppose at a chosen t>0 that

    D_K(t):=sum_(n>=1)d_n t^n<infinity.                (BA4)

For u,v in the SAME component I_i, choose a fixed positive G-path v->u of length ell_uv and original weight c_uv>0.
For u=v use the empty path, with ell_uu=0 and c_uu=1.
Appending that fixed path is injective on original paths and gives

    c_uv B^m(u,v)<=B^(m+ell_uv)(u,u),
    H_i(t)(u,v)=Gamma_uv(t)
          <=[1+D_K(t)]/[c_uv t^ell_uv].               (BA5)

The equality holds because a G-path between two states in I_i cannot visit a different A-component and return: that would put the other visited boundary state in I_i as well.
The bound includes the possible zero-length diagonal term explicitly.
It pays only within-component entries and uses no nonexistent return connector between different components.

Define the finite within-component constants M_i(t) and the possibly infinite cross-component quantities L_ij(t) by

    M_i(t)=[1+D_K(t)] max_(u in I_i)
                         sum_(v in I_i)1/[c_uv t^ell_uv],
    L_ij(t)=||Lambda_(I_i,I_j)(t)||_infinity, i!=j.

The EXACT additional requirement for all boundary Green entries to be finite, under BA4, is that every nonzero cross-component Lambda_uv(t) be finite.
Sufficiency follows from BA3 and BA5; a concrete bound is

    ||Gamma_AA(t)||_infinity
      <=sum_(all directed component paths i_0->...->i_r)
             product_(q=0..r) M_(i_q)(t)
             product_(q=0..r-1) L_(i_q,i_(q+1))(t).   (BA6)

This finite sum may overcount row contributions but is a valid upper bound.
Necessity follows from Lambda_uv<=Gamma_uv coefficientwise.
Since the entrance and exit matrices have row sums at most one, BA2 also gives ||E_K(t)||_infinity<=t+t^2||Gamma_AA(t)||_infinity when these quantities are finite.
Finite dimensionality of A does not by itself make the cross-component series finite: their entries sum arbitrarily long excursions through the infinite set G minus A.

Assume each d_n is finite, as the actual unique-fixed-point argument above guarantees for the quartic.
Let alpha=limsup_n d_n^(1/n), and let chi be the maximum coefficient root-limsup among the finitely many cross-component Lambda_uv, with chi=0 when there are none.
For every t<1/max(alpha,chi), with the usual infinite-radius convention when the maximum is zero, BA4 and all crossing-series convergence hold.
Consequently every boundary coefficient sequence B^n(u,v) has root-limsup at most max(alpha,chi).
In particular polynomial cross-component series transfer a diagonal exponential estimate to every boundary entry.
A sufficient concrete structural condition for that polynomial case is a finite bound on the length of every G-path between different boundary components whose interior avoids A.
No such global bound or crossing-rate estimate for the actual chosen K is inferred from condensation alone.

<a id="actual-forced-prefix-diagonal-transfer"></a>
### BA3. The actual distance-two forced-prefix comparison

For the actual K_2 of BC3, take the LOCAL test set A'={1,a}, where a=beta-1, solely to inspect that ordered pair.
This does not assert that A' is the full exterior entrance/exit boundary.
All predecessors of1 are deleted, while its unique original successor is a with weight1/4.
The A'-excursion graph therefore has separate components{1} and{a}, with the exact cross-channel Lambda_(1,a)(z)=z/4 and no arrow back.
Its first component has H_1=1, and BA3 gives

    Gamma_(1,a)(z)=(z/4)Gamma_(a,a)(z),
    B_(K_2)^m(1,a)=(1/4)B_(K_2)^(m-1)(a,a), m>=1.    (BA7)

Thus a polynomial acyclic channel supplies the valid diagonal transfer for this pair even though the proposed closing path a->1 does not exist.
This reuses BC4 exactly; it supplies no decomposition or crossing bound for every actual boundary pair, the distance-eight exterior, or all larger cores.

<a id="acyclic-boundary-counterexamples"></a>
### BA4. Acyclic boundary tails are not controlled by deleted diagonals

The following is a GENERAL counterexample, not the actual quartic digit system.
Take states0,a_n,b_n for n>=0, put K={0}, and use the stochastic rows

    P(0,a_0)=1,                  P(b_0,0)=1,
    P(a_n,a_(n+1))=(n+1)/(n+2), P(a_n,b_n)=1/(n+2),
    P(b_n,b_(n-1))=1, n>=1.

Every state has at most two predecessors and two successors.
The full graph is irreducible and every state lies on an original root-return word.
Outside K, a path moves up the a ray, crosses once to the b ray and moves down it; it can never return to a previously visited state.
Hence d_n=t_n(K)=0 for EVERY n>=1.
The full outside boundary is A={u=a_0,v=b_0}, and its sole nonzero excursion channel is u->v.
The only u-to-v path of length2n+1 crosses at a_n, and its exact original weight is

    product_(j=0..n-1)(j+1)/(j+2) times1/(n+2)
      =1/[(n+1)(n+2)].

Thus

    B_K^(2n+1)(u,v)=1/[(n+1)(n+2)],
    f_(2n+3)=1/[(n+1)(n+2)],
    sum_(n>=0)f_(2n+3)=1,
    sum_(n>=0)(2n+3)f_(2n+3)
       =sum_(n>=0)[1/(n+1)+1/(n+2)]=infinity.          (BA8)

The open-channel radius and R_f are both1.
The complete return radius R is also1: return coefficients are at most one, while F(1)=1 makes the nonnegative renewal sum U(1)=sum_k F(1)^k infinite.
The original chain is therefore critically recurrent with infinite mean and R_f=R despite identically zero deleted diagonal sums.
Its shortest distances are d(b_n)=n+1 and d(a_n)=n+2, so all distance levels are finite and every finite nonzero distance-core matrix is nilpotent.
Consequently the generic finite-level and original-core convergence hypotheses of C838 do not remove this missing acyclic-channel obligation.
The variable rational transition probabilities distinguish this example from the fixed original digit law.

Even restricting nonzero edge probabilities to the quartic's palette{1/4,1/2} does not give a formal diagonal-to-open-path radius comparison for arbitrary graphs.
On the same outside graph instead take

    P(a_n,a_(n+1))=1/2, P(a_n,b_n)=1/4,
    P(b_n,b_(n-1))=1/2, n>=1,
    P(0,0)=1/2, P(0,a_0)=1/4, P(b_0,0)=1/4,

with every missing row mass killed.
Again all deleted diagonals vanish, but

    B_K^(2n+1)(u,v)=4^(-(n+1)),
    Gamma_uv(z)=(z/4)/(1-z^2/4),
    F(z)=z/2+z^3/[64(1-z^2/4)],                       (BA9)

where the displayed evaluations hold for0<z<2 and the nonnegative series diverge at z=2.
The open-path root-limsup is1/2, while the deleted-diagonal root-limsup is0.
This second graph retains the weight palette but not the quartic affine transitions or its order/embedding geometry.
Neither example is a counterexample to an actual quartic estimate; together they show why a proof based only on formal finite-boundary elimination, local finiteness, finite levels and deleted diagonal bounds is insufficient.

<a id="conditional-critical-radius-transfer"></a>
### BA5. A paid conditional route from the boundary estimate to R_f>R

For the ACTUAL quartic, suppose a finite K containing0 and a t_*>R have been supplied such that D_K(t_*)<infinity and every cross-component boundary channel in BA2 is finite at t_*.
BA1--BA6 then prove E_K(t_*) is a finite matrix, with all original entrance, exit and excursion clocks retained.
This does not by itself assert convergence of repeated nonzero-K visits at t_*.
That remaining finite coupling can instead be paid at a nearby parameter above the true R as follows.

Use C590's accepted critical facts F(R)=1, H(0)=1,0<H<=1, and the recurrent stochastic law Q(x,y)=R P_D(x,y)H(y)/H(x).
Its first-positive-return-to-K matrix is

    S_K(a,b)=E_K(R)(a,b)H(b)/H(a).

It is stochastic because the actual recurrent chain returns to0 and therefore to K almost surely, and the equality follows by telescoping H on every finite original excursion.
Let C=K minus{0}.
For the following finite-coupling argument assume C is nonempty; its empty case is treated below.
For each a in the finite set C, choose a fixed original first-hit word from a to0, of length ell_a and weight p_a>0.
It produces a finite sequence of K-visits ending at0 with at most ell_a induced steps and Q probability R^ell_a p_a/H(a)>0.
With J the maximum of these induced step counts and epsilon the minimum of their positive probabilities, the restricted matrix S_(C,C) satisfies ||S_(C,C)^J||_infinity<=1-epsilon<1.
This finite induced-step estimate justifies convergence; the original chronological lengths remain in E_K(z), not in the induced step count J.
Positive finite diagonal similarity gives convergence of sum_k E_(C,C)(R)^k.

For nonempty C set w=(I-E_(C,C)(R))^(-1)1, so1<=w<infinity and E_(C,C)(R)w=w-1.
Put z_0=(R+t_*)/2 and

    L=max_(a in C)(E_(C,C)(t_*)w)(a)
                   /[t_*(1-z_0/t_*)^2],
    delta=min{z_0-R, 1/[2 max(1,L)]}>0.

Coefficientwise differentiation below t_* gives E'_(C,C)(z_0)w<=L1: for every n>=1, n(z_0/t_*)^(n-1)<=1/(1-z_0/t_*)^2.
Monotonicity of the derivative then gives

    E_(C,C)(R+delta)w
       <=E_(C,C)(R)w+delta E'_(C,C)(z_0)w
       <=w-1/2.

Thus its geometric series converges by the positive w-normalization, with row factor at most1-1/(2 max w)<1.
The unique first-hit-to0 partition at intermediate K-visits now gives the finite ORIGINAL-clock value

    F(R+delta)=E_00(R+delta)
      +E_(0,C)(R+delta)[I-E_(C,C)(R+delta)]^(-1)
                                      E_(C,0)(R+delta)<infinity. (BA10)

If C is empty, simply use F(t_*)=E_00(t_*)<infinity and omit the finite coupling argument.
Consequently the stated diagonal-plus-crossing hypotheses imply R_f>R, a positive exponential moment of the actual critical first-return law, and finite critical mean.
The constants above depend on the TRUE R, the supplied t_*, complete E_K(t_*), and the selected finite positive paths; none has been numerically evaluated here.

For example, an actual bound alpha<=1/beta together with chi<=1/beta would permit any R<t_*<beta and satisfy the needed convergence hypotheses.
The exact diagonal word formula alone provides neither this diagonal estimate nor the missing acyclic-channel estimate.
The concrete remaining task is to identify and bound the actual cross-component first-A-return series, or prove a structural condition such as bounded-length crossing paths; a generic pressure-at-infinity assertion or formal matrix inverse does not replace that work.
No actual new tail estimate, native computation, parameter grid or larger graph is asserted by this conditional deduction.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision boundary-criterion-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T21:33 |
| status | open |
| reason | Fix the complete combined actual nonclosure and conditional finite-boundary theorem, full BC1--BC4 and BA1--BA10 proofs, every original-clock factor, SCC connector/product bound, exact extra acyclic-channel condition, both generic counterexamples and paid critical finite-coupling implication. Separate whole review and adoption remain outstanding; no actual new diagonal/crossing bound or radius/mean classification is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Exact actual quartic two-state and distance-core nonclosure examples, general finite-boundary/SCC criterion with its additional crossing-series condition, complete rate/counterexample claims and strictly conditional actual critical consequence. |
| argument | [Complete combined proof](#complete-argument) | Entire actual diagonal word finiteness, BC1--BC4, BA1--BA10, all weights/lengths and finite/infinite word sums, SCC bounds and both directions, generic examples, explicit positive delta, finite killing and empty-core case. |
| dependency | [Actual complete boundary graph](Yin_C_G0785_v1.md#complete-argument) | Exact actual core/strip conventions, beta bounds, membership and original predecessor/successor rows used in every actual BC example; no positive-phase derivative estimate is imported. |
| dependency | [Actual periodic fixed-point identity](Yin_C_G0546_v1.md#actual-periodic-congruence-diagonal) | Unique fixed starting state for each original digit word, finite actual complete/deleted diagonal sums and original weighting; no finite-deletion exponential estimate. |
| dependency | [Actual critical recurrent law](Yin_C_G0590_v1.md#critical-escape-reuse) | F(R)=1, finite positive H, original-clock recurrent Q and positive finite first-hit words, used only to pay the critical induced finite-K killing and conditional extension. |
| dependency | [Strict actual radius bound](Yin_C_G0796_v1.md#statement) | Only R<beta for the conditional example alpha,chi<=1/beta; no new source/native replay or stronger numerical deficit. |
| support | [Existing finite component mechanism](Yin_C_G0234_v1.md#cycle-counting-bound) | Attribution for finite strong-component ordering and block triangularization; the boundary word product argument is proved completely here. |
| support | [Original-clock distance-core convention](Yin_C_G0838_v1.md#original-clock-definitions) | Exact comparison convention for C_1,C_2 and their convergent original core matrices; nonclosure supplies no refutation of C838's conditional theorem. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T21:43 |
| status | proved |
| reason | Adopt the entire actual diagonal/BC1--BC4/BA1--BA10 statement and proof after root's complete argument and fixed-scope reading and the fresh whole independent R1061 finding. All original weights, chronological partitions, SCC connector and crossing costs, both generic counterexamples, critical finite killing, explicit positive extension and empty cases are covered. The actual diagonal and acyclic-crossing estimates remain unresolved; no new actual radius gap, finite mean, all-large-core theorem or unrestricted G0001 conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Exact actual quartic two-state and distance-core nonclosure examples, general finite-boundary/SCC criterion with its additional crossing-series condition, complete rate/counterexample claims and strictly conditional actual critical consequence. |
| argument | [Complete combined proof](#complete-argument) | Entire actual diagonal word finiteness, BC1--BC4, BA1--BA10, all weights/lengths and finite/infinite word sums, SCC bounds and both directions, generic examples, explicit positive delta, finite killing and empty-core case. |
| dependency | [Actual complete boundary graph](Yin_C_G0785_v1.md#complete-argument) | Exact actual core/strip conventions, beta bounds, membership and original predecessor/successor rows used in every actual BC example; no positive-phase derivative estimate is imported. |
| dependency | [Actual periodic fixed-point identity](Yin_C_G0546_v1.md#actual-periodic-congruence-diagonal) | Unique fixed starting state for each original digit word, finite actual complete/deleted diagonal sums and original weighting; no finite-deletion exponential estimate. |
| dependency | [Actual critical recurrent law](Yin_C_G0590_v1.md#critical-escape-reuse) | F(R)=1, finite positive H, original-clock recurrent Q and positive finite first-hit words, used only to pay the critical induced finite-K killing and conditional extension. |
| dependency | [Strict actual radius bound](Yin_C_G0796_v1.md#statement) | Only R<beta for the conditional example alpha,chi<=1/beta; no new source/native replay or stronger numerical deficit. |
| support | [Existing finite component mechanism](Yin_C_G0234_v1.md#cycle-counting-bound) | Attribution for finite strong-component ordering and block triangularization; the boundary word product argument is proved completely here. |
| support | [Original-clock distance-core convention](Yin_C_G0838_v1.md#original-clock-definitions) | Exact comparison convention for C_1,C_2 and their convergent original core matrices; nonclosure supplies no refutation of C838's conditional theorem. |
| review | [Whole independent finding](../audits/reviews/Yin_R_G1061_v1.md#whole-boundary-criterion-finding) | Entire exact fixed statement and proof, actual diagonal finiteness, BC1--BC4 and BA1--BA10, all six accepted dependency/support interfaces, every word/convergence/constant/rate/counterexample/empty-case boundary; no author development, prior verdict or substantive repair. |

