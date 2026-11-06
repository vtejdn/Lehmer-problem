---
author: Yin
---
# Arithmetic random matrices: full local depths, prime mass and integral minors

## Scope and strategic assessment

This 2026-11-05 continuation of [G0001](../tasks/Yin_T_G0001_v1.md#contract) examines the mechanisms left open by [L446v1](Yin_L_G0446_v1.md#scope-and-strategic-assessment).
The earlier fixed comparison remains preserved at its original scope.
The full local-depth deduction belongs to [C867v2](../claims/Yin_C_G0867_v2.md#statement), with its own complete proof and selected assessment; the wider general-polynomial first-layer theorem remains in [C867v1](../claims/Yin_C_G0867_v1.md#statement).
The present material owns the complementary prime-growth, graph and integral-minor explorations, their direct checks, source applicability and remaining uncertainty.
These comparisons are author-checked explorations, not independently reviewed Claims or a whole-Task completion finding.
No literature-novelty claim is made.

The continuation found no positive uniform arithmetic lower bound.
C867v2 excludes full actual contributions from fixed prime sets, and from deterministic prime budgets with sum log p=o(log d), uniformly on bounded-total-measure inputs.
Its all-prime localization also forces any positive normalized mean to obtain quadratic total logarithmic cyclotomic mass at orders proportional to the original degree.
Thus arbitrary depths at a few primes do not repair the first-layer deficit in this ensemble.
The primitive-existence and graph comparisons below fail to supply the missing mass or original-measure return.
Volume sampling keeps the original polynomial, but its full certificate is exactly C209 with its boundary retained; the new regular-matroid comparison supplies only a first nonunit minor, without uniform proliferation.
Retain these findings inside S3, S8 and S6 rather than introduce an independently selectable new strategy.

## Prime-growth notation and actual clock weights

Let P be monic irreducible and noncyclotomic with constant coefficient plus or minus one, original degree d, root alpha and total logarithmic measure m.
Set R_k=|Norm(alpha^k-1)|, D_r=|Norm(Phi_r(alpha))|, b_r=log D_r and H_n=sum_(j=1)^n 1/j.
For the uniform N-by-N permutation matrix, the exact finite divisor summation is

    mu_N=E log|det P(Pi_N)|
        =sum_(r<=N)(b_r/r)H_floor(N/r).                  (GP1)

It follows directly from E C_k=1/k and R_k=product_(r|k)D_r, as proved at N=d in C867v2.
All primes, depths and original-field multiplicities are included, without an independence assumption across primes or cycles.
The [complete short-clock localization](../claims/Yin_C_G0867_v2.md#all-depth-short-clock-localization) and [terminal mass criterion](../claims/Yin_C_G0867_v2.md#terminal-clock-mass) own the stronger quantitative consequences.
At N=d and m<=exp(-40), [L446v1](Yin_L_G0446_v1.md#original-scale-upper-interface) gives mu_d/d<=(16/7)Phi(m), with Phi the original-measure envelope defined there, which tends to zero with m.
A positive uniform arithmetic lower bound would therefore imply a positive Mahler gap; none is supplied by the identity alone.

## Full order coverage still needs mass beyond primitive existence

For reciprocal P and each r>=3, [C361](../claims/Yin_C_G0361_v1.md#primitive-inversion-orbits) identifies the actual primitive part Prim_r as an integer square.
If a primitive prime ideal exists, the inversion-closed orbit gives log Prim_r>=2 log(r-1), including ramified primes and both possible residue involution types.
Its stated current review relationship and external-source limits remain those of C361; this exploration does not upgrade them.

Grant the much stronger hypothetical coverage that a primitive ideal exists at every order 3<=r<=N, including orders far below the available general existence theorem's cutoff.
Using only that order-floor information gives the deterministic cycle reward

    A_floor(k)=2 sum_(r|k, r>=3) log(r-1) <= log R_k.

The ideal sets have distinct residue orders, so this sum is a legitimate disjoint primitive-layer lower certificate.
Its exact expected value and a simple upper bound are

    E sum_(k<=N) C_k A_floor(k)
      =2 sum_(3<=r<=N) [log(r-1)/r] H_floor(N/r)
      <=2 log(N+1) H_N^2.                                (GP3)

Indeed H_floor(N/r)<=H_N, log(r-1)<=log(N+1), and sum_(r<=N)1/r=H_N.
Thus even idealized coverage at every order yields only O(log^3 N) certified mean from this information, and its normalized contribution vanishes for N comparable to d tending to infinity.
This is an upper bound on the existence-only certificate, not on the true primitive part or determinant.
The random-cycle weighting is different from C361's weighted auxiliary-degree and common-exponent tests; those older obstructions need not be reproved.

More generally, suppose a proposed certified layer profile satisfies

    0<=c_r<=b_r,     c_r<=A (log(r+1))^q

for fixed A>0 and q>=0.
Its entire random-cycle expected income is at most A (log(N+1))^q H_N^2.
Consequently any fixed number of primitive witnesses per order with only fixed-power-of-order norm floors remains below the required linear scale, even when every order and every resulting rational prime is selected.
The statement concerns the guaranteed floor only; an actual witness with much larger norm, many independent orbits or unexpectedly large depth can escape it.

At terminal orders N/2<r<=N, if log D_r is bounded by A log(N+1) times an integer packet count t_r, the corresponding GP1 terms give

    mu_top <= [2A log(N+1)/N] sum_(N/2<r<=N)t_r.

Hence mu_top>=eta N would require at least eta N^2/[2A log(N+1)] such packets in that window.
Here a packet must be an explicitly disjoint actual logarithmic prime-power contribution satisfying the displayed size bound; splitting or relabeling one contribution supplies no new mass.
This calculation distinguishes large prime availability from enough contributing multiplicity at the orders the original ensemble samples.

## Choosing primes after observing the permutation gives no extra income

Let S(pi) be any finite prime set selected after observing pi, with no cardinality or budget restriction.
Its selected full-depth logarithmic contribution is pointwise at most log|det P(Pi_N)| because every prime valuation is nonnegative.
It follows that its expectation is at most the all-prime GP1.
For prescribed deterministic certified layer masses c_r, selecting a subset of their primes or layers after seeing pi is likewise dominated pointwise by using all the c_r.
Thus GP3 also bounds every adaptive selection from that particular existence-only certificate.

One must not factor an adaptive selection indicator out of the cycle expectation E C_k=1/k.
Pointwise domination avoids that invalid independence step and shows why adaptive prime selection does not amplify a fixed collection of lower rewards.
It can still reveal actual large rewards omitted by the chosen certificate, which would be genuinely additional arithmetic information.

The all-prime factorization also prevents treating CRT cardinality as independent fresh income: product structure adds valuations only for the same original integer determinant.
A large available prime budget without any contributing root order is insufficient even outside the near-one regime.
Indeed [C536](../claims/Yin_C_G0536_v1.md#fixed-prime-invisibility-statement) permits any prescribed finite set for each input degree, hence also sets growing with d, and makes its entire contribution zero throughout every fixed degree-linear window for large enough d.
That construction has m(P)>=log(d+1), so it is not a counterexample to near-one coverage or to Lehmer.

## Why conjugation does not multiply one primitive witness by d

Passing to a normal closure L does not turn one primitive ideal for alpha into a full degree-d packet for the same element.
For a field automorphism sigma, an ideal Q dividing alpha^r-1 is sent to sigma(Q), which divides sigma(alpha)^r-1.
This is a witness for the conjugated element unless sigma fixes alpha, or a specific algebraic symmetry such as inversion proves the original return condition again.
Its contribution is already included with the actual residue degree in the norm; it cannot be multiplied by the number of conjugates a second time.

An exact small reciprocal control makes both this issue and repeated underlying rational primes visible.
The rational-prime repetition itself is already demonstrated by the Lehmer modulo-3 control in [C265](../claims/Yin_C_G0265_v1.md#primitive-cyclotomic-local-layers), with distinct residue orders 4 and 82.
The smaller calculation below is retained only to make the additional exact depth-one, inverse-pair-size and full-small-norm checks transparent; it is not a new general distinction or proposed Claim.
Take

    T(z)=z^2-7z+13,
    P(x)=x^2 T(x+x^(-1))=x^4-7x^3+15x^2-7x+1.

The discriminant of T is -3, so T is irreducible over Q.
For a root z, Norm_(Q(z)/Q)(z^2-4)=T(2)T(-2)=3*31=93 is not a rational square.
Therefore z^2-4 is not a square in Q(z), x^2-zx+1 remains irreducible over that quadratic field, and P is irreducible of degree four.
It is noncyclotomic because its trace roots are nonreal, whereas traces of roots of unity are real.
This is an actual reciprocal integer unit input with positive measure, without a near-one assertion.

Modulo 7 it factors into four distinct linear factors:

    P(x)=(x^2+x+1)(x^2-x+1)
        =(x-2)(x-4)(x-3)(x-5) modulo 7.

The first inverse pair has exact order 3, and the second has exact order 6.
The squarefree reduction makes 7 a good prime for the original order, so these describe actual prime ideals in the maximal order as well.
The exact complete primitive-order layers are

    D_3=T(-1)^2=441=3^2*7^2,
    D_6=T(1)^2=49=7^2.

Thus the same rational prime 7 supports two different primitive ideal orders, and each order receives only its own inverse pair, each at depth one.
The degree-four irreducibility does not make every prime ideal above 7 primitive at either chosen order, and rational-prime novelty cannot replace ideal primitiveness.
This finite control is not a counterexample to a near-one mass theorem; it shows the exact missing premise in an attempted Galois-multiplicity shortcut.
The computations are direct symbolic expansions and field-norm arguments given here; no numerical search or independent review is claimed.

## Existing primary-source interfaces and their uniformity

The directly needed source information already has local responsible homes, which were reused before extending the argument.

| Mechanism | Exact available scope | Consequence for this test |
| --- | --- | --- |
| [C265](../claims/Yin_C_G0265_v1.md#finite-window-primitive-count), exact finite-window escape | A controlled window outside a supplied finite prime set, with a known positive eta<=m; N certified primitive ideal indices imply at least ceil(N/d) rational primes. | O(d) primitive indices alone certify only O(1) distinct rational primes by this count. The time bound depends on the unknown positive eta and does not supply an independent uniform gap. |
| [Ste77-U001](../audits/literature/Ste77/Yin_U001.md#ste77-theorem-one), Theorem 1 | Primitive prime ideals exist for n>max{2(2^d-1),exp(452)d^67}; all nontorsion algebraic units, including unit-circle conjugates. | The cutoff is outside a fixed Cd window. Even hypothetical full coverage inside the window gives only GP3 if one retains order floors alone. |
| [Ste13 source screen](../audits/literature/Ste13/readme.md#ste13-discovery-screen), Theorems 1.1--1.2 | Cyclotomic norm comparison with main term phi(n)m, degree-dependent threshold and exception count; exact constants and proof boundaries retained there. | The main term remains proportional to the unknown m and does not become an m-independent reward. |
| [BGH21 source screen](../audits/literature/BGH21/readme.md#bgh21-s8-discovery-screen), Theorems 1.1--1.4 | Large-prime lower statements are for rational or quadratic inputs; the general-degree statement is a valuation upper bound with a degree/height cost. | The inspected lower log-prime scale is logarithmic in the order. A valuation ceiling requires independent total mass before it can force many contributing primes. |
| [CLOZ25 source screen](../audits/literature/CLOZ25/readme.md#cloz25-s8-frobenius-screen) | Actual Frobenius-class existence retains splitting-field discriminant and group-dependent constants. | No degree-uniform affordable budget or root-order coverage for the original near-one input follows. |

The bounded primary-source lookup on 2026-11-05 searched primitive ideal divisors, degree-uniform cutoffs and Lehmer--Pierce sequences and located the already retained [institutional Ste77 chapter](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/trans-theory-adv-appl-1977_0.pdf).
No newly acquired theorem is required: source reliance is at the exact local inspections above, rather than at search-result excerpts or an asserted fresh full-proof audit.
No Bogomolov theorem is used to replace these quantitative conditions; this source inspection makes no exhaustive claim about that literature.

## Assessment and useful next distinction

This investigation does not establish a new positive lower bound or justify a new Strategy.
It sharpens the random-cycle test: full primitive-order coverage and growing prime support still fail when the guaranteed layer rewards remain polylogarithmic, and adaptive selection cannot repair that floor.
The full product must carry actual extra size, depth or multiplicity at the correct order weights; terminal orders require the quadratic-scale mass in [C867v2](../claims/Yin_C_G0867_v2.md#terminal-clock-mass).
That is a concrete restriction on proposed prime-growth mechanisms, not a conditional restatement that prime coverage would help.

A useful continuation should therefore demonstrate actual initial primitive norms of substantially greater size or many disjoint primitive packets at orders proportional to d for a specified near-one structural class.
The [all-prime localization](../claims/Yin_C_G0867_v2.md#all-depth-short-clock-localization) excludes obtaining positive normalized mean solely from sublinear clocks under bounded total measure, so an original coefficient relation must force income beyond that range rather than evade its cost by reusing short orders.
The present source checks and integer/CRT identities do not supply such a forcing mechanism.
The unrestricted near-one and Lehmer questions remain unresolved.

## Graph lifts: one holonomy is still the cyclic model

Let a connected finite graph have q vertices and e edges, with an N-dimensional permutation transport H_a on each oriented edge a and inverse transport on the reverse edge.
Consider a q-by-q block matrix whose diagonal blocks are integer scalar multiples of I_N and whose off-diagonal blocks are integer scalar combinations of these transports.
Choose a spanning tree and a root.
Recursive vertex changes of basis by permutation matrices G_v make every tree transport the identity: on an edge u to v the new transport is G_v^(-1) H_a G_u, so define G_v=H_a G_u along the tree.
The block diagonal basis change preserves the determinant and integrality.
There remain exactly e-q+1 non-tree transports, which are the independent cycle holonomies.

If e-q+1=1, write the remaining permutation as H.
All blocks of the transformed matrix then lie in Z[H,H^(-1)], so they are evaluations of a q-by-q Laurent polynomial matrix B(z).
Writing Q(z)=det B(z), simultaneous diagonalization of H gives

    det B(H)=product_(zeta in spec H) Q(zeta).

For an H-cycle of length k its contribution is product_(zeta^k=1) Q(zeta), the ordinary cyclic resultant of Q.
Thus a lift with one graph cycle and an exact scalar linearization Q=P returns to the same permutation/resultant model analyzed in L446.
The many random labels on tree edges add no determinant randomness after the basis change.
If Q has extra factors, all of their resultant contributions remain; if B has q scalar rows, dividing its logarithmic determinant by qN changes the original normalization and must be charged.
No extra factor or trace normalization is silently discarded here.

For independent uniform edge permutations the residual holonomy is uniform as well, conditional on the tree labels, since it is a fixed left and right translate of the independent non-tree edge permutation.
This direct argument agrees with the spanning-tree flattening in Shashwat Silas, [delta-Connectivity in Random Lifts of Graphs](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i1p46/pdf/), Sections 3.1--3.2, printed pages 3--4, actually inspected in this round.
Only the flattening and cycle-generator interface is used, not its later connectivity probability estimates.

With at least two non-tree edges, genuinely independent holonomies are possible, but diagonal scalar specialization does not prove a return to m(P).
The elementary polynomial F(U,V)=I+U+UV has diagonal specialization F(z,z)=1+z+z^2=Phi_3(z).
Take U,V independently uniform on {I_2,S}, where S interchanges the two coordinates.
The four determinants are 9,3,-3,3, respectively, and consequently

    E[(1/2) log|det F(U,V)|]=(5/8) log 3>0,
    m(Phi_3)=0.

Independent block sums of this experiment retain the same positive normalized mean in arbitrarily large dimension.
Even this commuting two-label example already separates diagonal specialization from the desired original-P return; noncommutativity cannot be assumed to repair it.
It is a calibration failure for this proposed comparison, not a theorem excluding every multiholonomy construction or the positive-measure task class.
The missing interface for a genuinely different graph mechanism is an estimate that controls the full logarithmic determinant by the original total m(P), with every extra graph factor and dimension cost included, while passing this cyclotomic calibration.

[Bordenave--Collins, Eigenvalues of random lifts and polynomials of random permutation matrices](https://annals.math.princeton.edu/2019/190-3/p03), the actual abstract inspected, concerns strong asymptotic freeness of independent random permutations on the zero-sum subspace.
That is a relevant source lead for the changed model, but the inspected material supplies neither control of the logarithmic singular-value tail nor a degree-uniform original-P comparison.
No such estimate is imported from a norm-convergence statement.

## Integer minors and the volume-sampling probability law

Let P be the actual monic squarefree integer polynomial of degree d, with nonzero constant term, and use the unnormalized logarithmic Mahler measure m(P).
For N>=1 let A_N be the (N+d)-by-N integer matrix whose columns are the full coefficient vectors of P,tP,...,t^(N-1)P.
Set L=N+d and D_N=det(A_N^T A_N)>0.
For an N-element row set S put a_S=det(A_N[S,:]).
Cauchy--Binet gives the exact identities

    D_N=sum_(|S|=N) a_S^2,
    E_uniform a_S^2=D_N/binom(N+d,N).

The distribution pi(S)=a_S^2/D_N on the nonzero minors is volume sampling.
Its Shannon entropy H_N and its expected logarithmic squared minor W_N satisfy

    H_N=-sum_S pi(S) log pi(S),
    W_N=E_pi log a_S^2>=0,
    log D_N=H_N+W_N.

The inequality W_N>=0 is where integrality enters: every nonzero a_S is an integer of absolute value at least one.
The exact normalization and maximal-size sampling law appear in Dereziński--Warmuth, [Reverse Iterative Volume Sampling for Linear Regression](https://jmlr.org/papers/volume19/17-781/17-781.pdf), Section 2.1, Theorem 2 and equation (1), printed page 7, actually inspected.
Their statistical applications are not used; the displayed identities here follow directly from Cauchy--Binet.

Writing Delta=|disc P|, the already proved [C209](../claims/Yin_C_G0209_v1.md#statement) bound, with its orbit window L=N+d, becomes

    log Delta+log D_N-d log(N+d)<=2(N+d-1)m(P),
    log Delta+H_N+W_N-d log(N+d)<=2(N+d-1)m(P).

Thus volume sampling separates the existing scalar certificate into an entropy term and a minor-size term; it does not create an additional term in that certificate.
Any new arithmetic gain would have to bound those terms from below after their entire discriminant and finite-window boundary, rather than merely rename log D_N.
For fixed d the number of available minors is binom(N+d,d), whose logarithm is o(N), so counting nonzero minors alone has zero limiting rate.

## Exact irreducible cyclotomic calibration and the cost of weighting

Take P=t^d+1 with d a power of two, so P=Phi_(2d) is irreducible and m(P)=0, and take N=kd with k a positive integer.
Reorder input and output coordinates by their residue modulo d.
Then A_N is a direct sum of d copies of the (k+1)-by-k matrix with j-th column e_j+e_(j+1).
Each block has Gram matrix with diagonal 2 and neighboring entries 1.
Its determinant b_k obeys b_k=2b_(k-1)-b_(k-2), with b_0=1 and b_1=2, so b_k=k+1.
Consequently

    D_N=(k+1)^d.

A nonzero maximal minor must select exactly k rows from each block: otherwise some block has fewer than k selected rows and loses column rank.
Deleting any one row from a block gives determinant of absolute value one, as is seen by splitting the remaining bidiagonal array at the deleted row into triangular pieces with unit diagonal.
There are therefore exactly (k+1)^d nonzero maximal minors, and every one has absolute value one.
It follows that

    H_N=d log(k+1),
    W_N=0,
    H_N/N=log(k+1)/k,
    Pr_uniform(a_S!=0)=(k+1)^d/binom((k+1)d,kd).

At k=1, uniform row sampling has success probability 2^d/binom(2d,d), asymptotic to sqrt(pi*d)/2^d, while volume sampling has conditioned away all zero minors.
Thus any claimed lower probability must specify which of these different laws is being used and pay the normalization when transferring between them.
The discriminant has absolute value d^d, so the full boundary cancels exactly:

    log Delta+H_N+W_N-d log(N+d)=0.

This calibration allows arbitrarily large d and any chosen fixed k, not only a degree-one or reducible control.
It does not refute a genuinely stronger noncyclotomic lower estimate at a sufficiently large fixed k, since log(k+1)/k tends to zero.
It does refute the inference that positive volume entropy per input coordinate at a fixed linear window is already positive Mahler income.

## A distinct structural lead: escape from unit maximal minors

For the actual unit polynomial P, let C be its integral companion and let v_j be the coefficient column of t^j modulo P in the power basis.
Let V_L=[v_0,...,v_(L-1)]; its first d columns are I_d and v_(j+1)=C v_j.
The kernel of V_L over Z is freely generated by the columns of A_(L-d), because division by monic P preserves integral coefficients.
Complementary maximal minors satisfy

    |det A_(L-d)[S,:]|=|det V_L[:,S^c]|.

Indeed, the two exterior products span complementary integral one-dimensional exterior lines, and the common scale is one: the first d columns of V_L have determinant one and the last L-d rows of A_(L-d) form a triangular matrix with diagonal one.
Equivalently, this is the primitive complementary-minor identity underlying the same-P orbit/kernel relation in C209.
If all d-by-d minors of V_L lie in {0,1,-1}, then V_L is totally unimodular: any nonzero smaller square minor extends to a maximal minor by adjoining the complementary columns of I_d.

For an irreducible nontorsion unit P, the columns v_i are nonzero and pairwise nonparallel over Q.
If v_i=c v_j with c rational and i>j, evaluation at a root alpha gives alpha^(i-j)=c.
Both alpha and alpha^(-1) are algebraic integers, so the rational number c and its inverse are integers, forcing c=1 or -1 and contradicting nontorsion.

The modern primary paper Oxley--Walsh, [2-Modular Matrices](https://www.math.lsu.edu/~oxley/2-Modular_Matroids_SIAM.pdf), introductory definition and discussion on printed page 1, explicitly states Heller's bound: a rank-d integer matrix whose maximal minors have absolute value at most one has at most binom(d+1,2) nonzero pairwise nonparallel columns.
The original reference is Heller, On linear systems with integral valued solutions, Pacific Journal of Mathematics 7 (1957), 1351--1364, [DOI](https://doi.org/10.2140/pjm.1957.7.1351).
The original proof was not inspected: its DOI fetch failed and the complete-issue PDF exceeded the web tool size limit.
The modern source supplies the exact statement needed for this attributed working corollary, so no further original-proof acquisition is required for the present use; no independent inspection of that proof is claimed.
At the stated external-theorem interface, the actual companion transfer therefore gives

    L>binom(d+1,2) ==> some |det V_L[:,T]|>=2,
    hence some maximal minor of A_(L-d) has absolute value at least 2.

A weaker self-contained eventual escape follows without Heller: unit maximal minors force all entries of V_L into {0,1,-1}, leaving at most (3^d-1)/2 nonzero columns up to sign, while the actual orbit has no parallel repeats.
Both arguments use exact integer orbit structure rather than a continuous spectral limit.
This is a concrete new testing angle for the existing S6 arithmetic-minor question, with a source lead and an explicit original-P transfer, not a new uniform Mahler bound.

The limitation is quantitative and survives weighting.
A single nonunit minor supplies only one summand at least 4 in D_N; its volume probability is at least 4/D_N, which need not be bounded away from zero.
Shifting a fixed d-column witness by j multiplies its determinant by det(C)^j=1 or -1, so it reproduces witnesses but does not multiply their sizes.
Even a linear count of such translates gives only a logarithmic contribution to log D_N and hence zero rate after division by N.
Obtaining a witness in O(d) time would still leave this missing proliferation step; neither a witness nor a regular-matroid column bound supplies a positive uniform density of independent determinant growth.
Accordingly the next useful structural question is whether the actual shift and the Pluecker relations force quantitatively many compatible nonunit minors, beyond translated copies, or instead allow long windows whose entire growth is boundary entropy.
Any positive answer must be tested in the corrected quantity log Delta+H_N+W_N-d log(N+d); a statement only about one witness should not be promoted to a new strategy.

## Toeplitz source gate: the remainder is still a new obligation

The full convolution Gram A_N^T A_N is the N-by-N Toeplitz section with symbol |P(e^(it))|^2.
Borodin--Okounkov, [A Fredholm determinant formula for Toeplitz determinants](https://arxiv.org/pdf/math/9907165v1), 1999 arXiv v1 (published in 2000), Sections 1--2, Theorem 1 and Remark 3, printed pages 1--4, were inspected at the statement and applicability level.
For a normalized symbol exp V, the analytic theorem assumes that the Laurent series V converges on an annular neighborhood of the unit circle and expresses the determinant as a Szego prefactor times a tail Fredholm determinant.
The proof and general limiting extensions were not checked or imported.

If P has no unit-circle roots, V=log|P|^2-2m(P) has a suitable analytic Laurent representation, but the allowed annulus and tail constants depend on the distances of the actual roots from the circle.
No degree-uniform lower bound on that annulus is available from this source interface.
If P has roots on the circle, the inspected analytic hypothesis fails, including for Salem and cyclotomic inputs relevant to the present problem.
For the explicit control P=t^d+1, the nonzero positive Fourier coefficients of V are v_(rd)=(-1)^(r+1)/r for r>=1, so

    sum_(n>=1) n |v_n|^2=d sum_(r>=1) 1/r=infinity.

Thus the finite nonzero Szego prefactor in that analytic formula cannot simply be applied to this calibration.
Regularization or a different singular-symbol theorem would require a fresh simultaneous degree, root-distance and tail estimate and, if it changes coefficients, a paid return to the original integral minors.
The inspected identity alone gives no independent control of that remainder and no new arithmetic lower estimate.

## Bounded strategic assessment

The graph construction with one cycle is an exact reduction to the existing cyclic model; multiple independent cycles first lose the scalar return, as the explicit Phi_3 control shows.
The volume-sampling object keeps the original P and places integer minors inside a probability law, but its full Mahler certificate is exactly the existing C209 certificate, with the cyclotomic boundary and changed-law normalization visible.
The nearest prior route is S6's arithmetic control of the sum of squared orbit minors, rather than a replacement of S3 or S8 by general random-matrix universality.
The possible new structural tool is quantitative escape from the regular-matroid regime, and the present Heller-interface observation establishes only a first nonunit witness, without the required proliferation.
This bounded comparison therefore does not justify an independently selectable new G0001 strategy.
Reopening is justified by either an original-P comparison for a genuinely multiholonomy object that passes the explicit calibrations, or an independently proved quantitative minor-proliferation mechanism that exceeds the entire C209 boundary uniformly.
No Claim adoption, formal review, new numerical scan, uniform gap theorem or global impossibility for all arithmetic random-matrix models is asserted.
