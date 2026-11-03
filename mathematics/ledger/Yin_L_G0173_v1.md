---
author: Yin
---

# Original-law long-block norms, exact collision radius and approximation boundaries

Date: 2026-10-10.
Fixed retention prepared at 2026-10-09T17:09 under the coordinating AI for Yin's explicit adoption instruction, after the separate complete D36 review and the complete D37 review at 2026-10-09T17:04.
This material preserves their full arguments and findings.
It is not a C acceptance or Task-completion decision; G0001 remains active and unresolved.

<a id="collision-operator-fixed-scope"></a>
## Current adopted results and their distinct domains

The original weights throughout are p_0=1/2 and p_1=p_(-1)=1/4, acting on complex counting-measure l2 of the specified algebraic state set.
The adopted conclusions are:

- For every Salem beta in(1,2), the [separated-digit theorem](#separated-digit-strip-norm) gives ||K_strip^n||<=M*2^(-floor((n-1)/a)) for n>=1, where B=1/(beta-1), M=floor(2B)+1 and a=log(1+beta)/log(beta).
  Its explicit exponential prefactor depends only on beta, not on the degree.
  The spectral interval and small-measure comparison retain the accepted fixed-input support estimate and its original source boundary.
- For every algebraic unit alpha, including torsion, the [actual-core theorem](#core-operator-collision-sandwich) proves p_n<=||K_act^n||<=C_alpha(n+1)^q p_n with its displayed embedding constant and neutral dimension q.
  Thus r(K_act)=exp(-h_2(alpha)) at each fixed input.
  The [Salem-strip counterpart](#salem-strip-exact-collision-radius) holds without requiring every strip point to belong to the actual core; only the two separately proved inputs use the existing full-core equality.
- For every such Salem full strip, [all powers have full essential norm](#salem-strip-all-power-essential-norm), and r_ess(K_strip)=r(K_strip)=exp(-h_2(beta)).
  This conclusion is not asserted for every general-unit core.
- For nontorsion algebraic units, the [finite-prime restricted cores](#finite-prime-spectral-exhaustion) are finite at the accepted L157/ESS scope, and their radii increase to the actual-core radius.
  The corresponding negative logarithms approximate entropy from above.
  No effective error estimate or bounded prime set is asserted.

These conclusions do not strengthen L30's scalar collision lower rate into a positive uniform gap.
The dimension-dependent polynomial overhead in the exact identification remains explicit and is distinct from the beta-only prefactor in the separate long-block upper bound.
All old source interfaces and fixed L171/L172 mathematical bodies remain unchanged.

The three full original working accounts follow.
Their date-specific pending, ready-for-review or next-question wording records the state when written and is superseded only by the present adoption statement.
Their mathematics and substantive review facts are preserved; only section depth and navigation are relocated.
The completed identities are D G0036, D G0037 and D G0040, with the precise map below.

<a id="retained-separated-digit-argument"></a>
## Preserved D G0036 argument and complete independent finding

## Separated binary digits give a full-strip operator bound

Date: 2026-10-10.
The coordinating AI for Yin developed this argument under the current G0001 continuation.
This extends the point-atom argument of [L30](Yin_L_G0030_v1.md#greedy-atom-bound) to a bounded real interval and then to the entire counting-measure operator.
It makes no literature novelty claim.
The original digit law and reciprocal strip are those of [D30](../claims/Yin_C_G0203_v1.md#reciprocal-kernel-fiber-norm); no general co-return theorem is assumed.

<a id="separated-digit-strip-norm"></a>
### Exact statement

Let beta in (1,2) be a Salem number, O=Z[beta], B=1/(beta-1), S=beta B, and

    D={x in O: |x_+|<B, |x_-|<S}.

On l2(D) use the unchanged kernel

    (Kf)(x)=sum_eta p_eta 1_D(beta*x+eta) f(beta*x+eta),
    p_0=1/2, p_1=p_(-1)=1/4.

Set

    a=log(1+beta)/log(beta),
    gamma=log(2)/a,
    M=floor(2B)+1,
    q_n=floor((n-1)/a),  n>=1.

Then the row and column sums, and hence the full operator norm, satisfy

    ||K^n|| <= M*2^(-q_n) <= 2*M*exp(gamma)*exp(-gamma*n).   (1)

The prefactor here depends only on beta, not on its algebraic degree or the number of unit-circle embeddings.
No finite-state cutoff or identification of every strip point with the actual core is used.

### 1. Uniform real separation

Choose e_0=0 and S_0=1.
For j>=1 let e_j be the least nonnegative integer with

    beta^(e_j)>S_(j-1)+1,
    S_j=S_(j-1)+beta^(e_j).

The exponents increase strictly.
Minimality gives beta^(e_j)<=beta*(S_(j-1)+1), so

    S_j+1 <= (1+beta)*(S_(j-1)+1) <= 2*(1+beta)^j,
    beta^(e_j) <= 2*beta*(1+beta)^(j-1) <= (1+beta)^(j+1).

Thus e_j<=(j+1)*a for j>=1; the same upper bound trivially holds for j=0.
For q_n>=1 the exponents e_0,...,e_(q_n-1) all lie in {0,...,n-1}.
This supplies at least q_n selected digits.
If q_n=0 the subsequent probability bound is trivial.

Any two distinct binary sums over these selected exponents differ in absolute value by at least one.
If their largest differing exponent is e_0, the difference is one.
Otherwise the largest term dominates all earlier selected weights by strictly more than one.
Therefore an open real interval of length 2B contains at most floor(2B)+1=M such sums.

Represent the original digit eta_j as b_j-b'_j, with all b_j,b'_j independent fair {0,1} bits.
In

    Z_n=sum_(j=0)^(n-1) eta_j beta^j,

condition on every b'_j and all unselected b_j.
The remaining q_n independent bits produce 2^(q_n) distinct, one-separated real values.
For every real interval I of length 2B,

    P(Z_n in I) <= M*2^(-q_n).                            (2)

For q_n=0, (2) follows from probability at most one and M>=1.
Averaging removes the conditioning.
This strengthens separation to a fixed distance; merely distinct sums, as in the original point-atom proof, would not bound interval concentration.

### 2. From endpoint probabilities to the full operator

Every row sum of K^n is the probability that the original affine walk starting at that row state remains inside D for n steps.
It is at most the probability that its final expanding real coordinate lies in (-B,B).
That coordinate is beta^n*x_+ plus a random sum distributed as Z_n, so (2) bounds every row uniformly.
This upper bound needs only endpoint necessity, not endpoint sufficiency.

The additive involution T(x)=beta^(-1)*sigma(x), where sigma(beta)=beta^(-1), preserves O and D.
The original symmetric digit weights give K*=UKU for the unitary (Uf)(x)=f(Tx), as proved directly in D30.
Consequently (K^n)*=UK^nU.
The supremum column sum equals the supremum row sum.
The Schur bound proves the first inequality in (1); explicitly, for a nonnegative matrix A whose row and column sums are at most R, weighted Cauchy--Schwarz gives ||Af||_2^2<=R^2||f||_2^2 first for finitely supported f and then by density.

Finally q_n>(n-1)/a-1 gives

    2^(-q_n) <= 2*exp(-gamma*(n-1)),

which proves the second inequality.
All multiplicities of coinciding algebraic digit sums are retained in the transition probabilities and the conditioning argument.

<a id="strip-radius-small-measure-comparison"></a>
### 3. Spectral radius and the small-measure scale

Let r_2(K) be the spectral radius on l2(D), and m=log(beta).
The spectral-radius formula applied to (1) yields r_2(K)<=exp(-gamma).
The original return probability is p_n=K^n(0,0): every zero-to-zero word has all its states strictly in D by the prefix/suffix bounds in D30, without assuming that every point of D can return.
Hence p_n<=||K^n||.

On the other hand, if nu_n is the binary sum distribution on O, then p_n=sum_x nu_n(x)^2>=1/|supp nu_n|.
The accepted fixed-beta support estimate in [L30](Yin_L_G0030_v1.md#one-expanding-comparison), with its existing [L7](Yin_L_G0007_v1.md#pisot-salem-attainment) source boundary, gives |supp nu_n|<=C_beta*n^s*beta^n.
Taking nth roots gives

    exp(-m) <= r_2(K) <= exp(-gamma),
    gamma <= -log(r_2(K)) <= m.                          (3)

In particular, along any hypothetical Salem sequence with m tending to zero,

    -log(r_2(K))/m -> 1,
    0 <= m+log(r_2(K)) <= m^2/(2*log(2)).                 (4)

The final scalar inequality is exactly the elementary estimate for m-gamma already checked in L30.
These conclusions concern the full infinite operator.
They require no convergence constant uniform in the degree for the lower bound, since the limit in n is taken for each fixed input first.

### Consequence, limitations, and next question

The one-step bound in D30 has exponent of order m^2; (1)--(4) show that the full long-block spectral exponent already has order m.
This supplies an operator-level interface for the known entropy scale.
It does not improve L30's scalar collision-entropy lower bound, exclude m tending to zero, or create same-exponent arithmetic income.
The explicit upper-norm prefactor is degree-independent, but the support estimate used for the lower radius bound is not.

The next separate question is whether r_2(K) equals the actual collision return rate, rather than merely lying in the same small-m interval.
The orbit agent is investigating that identification in a separately allocated material.
Its proof, if obtained, is not used above.
No claim that the spectral radius equals a diagonal coefficient rate is implicit in (3).

### Checking and attribution

The coordinator authored and self-checked the complete argument, including the strict exponent selection, q_n=0 case, fixed separation, original-law conditioning, reciprocal column bound and order of limits.
This is a written proof without a computational premise.
A noncontributor review is pending.
G0001 remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0072_v1.md#complete-independent-written-review), with its original inspected scope and relationship.



<a id="retained-collision-radius-argument"></a>
## Preserved D G0037 argument and contribution account

## The actual collision rate equals the original core-operator spectral radius

Date: 2026-10-10.
The earlier operator and quartic quantitative work is now retained in [C203](../claims/Yin_C_G0203_v1.md); its fixed proofs and certificates are unchanged.

### Question and result

The original weighted operator's l2 spectral radius equals the zero-return collision exponential rate, for every fixed algebraic unit.
The relevant feature is not irreducibility alone: every n-step displacement has probability at most the zero displacement because the law is the difference of two independent identically distributed binary sums.
Bounded nonneutral embeddings and translated norm-grid packing limit every row and column to polynomially many entries.
These two facts give an explicit polynomial sandwich between the operator norm and the diagonal probability.
This new argument is author self-checked and submitted for independent review; no fixed promotion is asserted here.

Reuse the complete original-law convention in [L154](Yin_L_G0154_v1.md#actual-first-return-paths), the norm-grid injection in [L91](Yin_L_G0091_v1.md#norm-grid-support-bound), the existence and comparison of fixed-order entropy rates in [L30](Yin_L_G0030_v1.md#renyi-rates), and the [full-strip block conventions](../claims/Yin_C_G0203_v1.md#reciprocal-kernel-fiber-norm).
The accepted Salem-core geometric input is [L170](Yin_L_G0170_v1.md#exact-salem-return-strip); the identification argument will not require its co-return premise for arbitrary inputs.

The operator-norm/spectral-radius conversion uses the standard Banach-algebra spectral-radius formula.
A bounded local search found no retained precise source for that named theorem.
Direct primary-source reading checked [Pet20, Proposition1.1.6](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), printed/PDF pp.7-8, in the 27 April 2020 edition.
It is accepted at statement-and-applicability depth; the original proof is not independently re-audited.
A bounded acquisition timed out and is truthfully exception-registered.
[Pet20-U001](../audits/literature/Pet20/Yin_U001.md#pet20-u001) records the exact accepted scope, including the quotient and compact-operator facts used below.
No novelty claim or new gap conclusion is asserted.

<a id="core-operator-collision-sandwich"></a>
### 1. General-unit statement and precise domains

Let alpha be any algebraic unit, O=Z[alpha], and let D_act consist of all states lying on finite original-digit paths from zero back to zero, including zero itself.
Use precisely

    X_(j+1)=alpha X_j+eta_j,
    Pr(eta=0)=1/2, Pr(eta=1)=Pr(eta=-1)=1/4.

On complex counting-measure l2(D_act) let

    (K_act f)(x)=sum_eta p_eta 1_(D_act)(alpha*x+eta)f(alpha*x+eta).

Let p_n=Pr_0(X_n=0), p_0=1, and let h_2(alpha)=lim_n -(1/n)log p_n be the fair-binary collision entropy rate, with the original sum convention in L154.
Count embeddings as real places and one representative of each complex pair.
Let r_0 be the number of real places with |sigma(alpha)|=1 and s_0 the number of complex pairs with that modulus, and put q=r_0+2s_0.
For every nonneutral place v define

    rho_v=|v(alpha)|,
    R_v=1/(rho_v-1) if rho_v>1,
    R_v=1/(1-rho_v) if rho_v<1.

Use the explicit positive constant

    C_alpha=2^r_0 8^s_0
       product_(real nonneutral v) (2R_v+2)
       product_(complex nonneutral v) (2sqrt(2)R_v+2)^2.

Then for every n>=0,

    p_n <= ||K_act^n||_(2->2)
        <= C_alpha (n+1)^q p_n.                           (1)

Consequently

    r_(l2)(K_act)=exp(-h_2(alpha)).                        (2)

No degree bound, Salem assumption, reciprocal automorphism, explicit enumeration of D_act, or quantitative co-return theorem is needed for (1)-(2).
The unit hypothesis keeps the ambient order and affine inverse convention within the established G0001 setting; no extension beyond algebraic units is claimed here.
Constants remain dependent on the full input alpha and its conjugates.

### 2. Every actual state is bounded at nonneutral places

If x is reached from zero in a steps, then at a contracting place rho<1,

    |v(x)| <= sum_(j=0)^(a-1) rho^j < 1/(1-rho)=R_v

for a>0; at a=0 the state is zero and the same strict bound holds.
If x has a continuation to zero of length b>0, then

    x=-sum_(j=1)^b eta_j alpha^(-j),
    |v(x)| <= sum_(j=1)^b rho^(-j) < 1/(rho-1)=R_v

at every expanding place.
A zero-length continuation means x=0.
These are modulus bounds, valid equally at real and complex places.
Therefore the actual core lies in the cylinder with |v(x)|<R_v at every nonneutral place.
No assertion of equality with that cylinder is required.

### 3. Zero is a largest atom of the complete displacement law

Let nu_n be the finitely supported distribution of the fair binary sum sum_(j=0)^(n-1) xi_j alpha^j.
Reversing independent indices does not change that distribution.
The complete n-step displacement law for eta digits is

    mu_n(z)=sum_(a in O) nu_n(a)nu_n(a-z).

Both factors have the same l2 norm, so Cauchy--Schwarz gives

    0<=mu_n(z)<=sum_a nu_n(a)^2=mu_n(0)=p_n             (3)

for every z in O.
This uses the entire difference law with its original probabilities.
It is false for an arbitrary biased transition law and is the step that generic irreducible positive-operator counterexamples do not supply.

For actual core states x,y, every path counted by K_act^n(x,y) is among the ambient words with displacement y-alpha^n x.
Hence

    0<=K_act^n(x,y)<=mu_n(y-alpha^n x)<=p_n.              (4)

In fact the first inequality is equality with mu_n: an ambient path from core x to core y can be preceded by a zero-to-x path and followed by a y-to-zero path, so every intermediate point also belongs to the core.
The weaker inequality (4) already suffices for the upper bound.
At zero, all closed words lie in the core by definition, giving K_act^n(0,0)=p_n exactly.

### 4. Uniform translated row and column support counts

Use L91's fixed grid in the full Minkowski embedding: half-open intervals of length1 on real coordinates, and intervals of length1/sqrt(2) on both Cartesian coordinates of each complex place.
Each full product cell contains at most one algebraic integer.
Indeed, a difference of two distinct points in one cell would have every conjugate of modulus strictly less than1, contradicting its nonzero integral norm.
This injection works in any translated region of the embedding space and does not involve a regulator or a discriminant constant.

Fix a starting state x and n.
At a neutral place v with |v(alpha)|=1, any possible endpoint y satisfies

    v(y)=v(alpha)^n v(x)+sum_(j=0)^(n-1) eta_j v(alpha)^j,
    |v(y)-v(alpha)^n v(x)|<=n.                            (5)

Thus at a neutral real place, the possible values lie in an interval of radius n around a possibly unbounded center; at a neutral complex place they lie in a disk of radius n around such a center.
The number of length1 grid intervals hit by a real interval of radius n is at most 2n+2=2(n+1).
A disk of radius n is contained in a Cartesian square, each side meeting at most 2sqrt(2)n+2 grid intervals; their product is at most 8(n+1)^2.
These bounds are uniform in the centers.

At each nonneutral place, Section2 bounds every endpoint by R_v.
The corresponding real or complex grid-cell counts are at most 2R_v+2 and (2sqrt(2)R_v+2)^2.
Multiplying the counts and applying the full-cell injection gives at most C_alpha(n+1)^q possible endpoints.
This bounds the number of nonzero entries in every row of K_act^n, uniformly over x.

For columns, fix y instead.
Any predecessor x with an n-step word to y satisfies

    v(x)=v(alpha)^(-n)v(y)-sum_(j=1)^n eta'_j v(alpha)^(-j),

for the reversed word coefficients eta'_j.
At neutral places the last sum again has modulus at most n.
Every predecessor is itself a core state, so the same fixed nonneutral bounds apply.
The identical translated grid count therefore bounds every column support by C_alpha(n+1)^q.
Neither direction requires the neutral center to remain near zero.

### 5. The norm sandwich and spectral identification

Set A_n=C_alpha(n+1)^q p_n.
Equations(3)-(5) show that every row sum and every column sum of the nonnegative matrix K_act^n is at most A_n.
For finitely supported f, weighted Cauchy--Schwarz gives

    |sum_y K_act^n(x,y)f(y)|^2
       <= A_n sum_y K_act^n(x,y)|f(y)|^2.

Sum over x and use the column bound to obtain ||K_act^n f||_2^2<=A_n^2||f||_2^2.
Nonnegative summation and density extend this to l2.
The matrix coefficient at zero gives the lower bound p_n<=||K_act^n||, proving(1).

The operator is bounded independently of this estimate as well: one-step row and column sums are at most1, since each digit determines at most one successor and at most one predecessor.
The same calculation gives ||K_act||<=1.
Thus it belongs to the complex unital Banach algebra B(l2(D_act)), the exact setting of Pet20's accepted spectral-radius formula.

Closed-word concatenation gives p_(n+m)>=p_n p_m, and the all-zero word gives p_n>=2^(-n)>0.
The fixed-order limit also follows from L30's already retained entropy-rate argument.
Taking nth roots in(1), the factor C_alpha^(1/n)(n+1)^(q/n) tends to1 at each fixed input.
Pet20 then identifies the norm-growth limit with the usual spectral radius, proving(2).

<a id="salem-strip-exact-collision-radius"></a>
### 6. Salem-strip corollary and the full uniformity boundary

For a degree d=2s+2 Salem beta in(1,2), let D_strip={x in Z[beta]:|x_+|<B,|x_-|<S}, B=1/(beta-1), S=beta B, and let K_strip have the same original weights.
Every closed word lies in this open strip by the past/future bounds in Section2.
Therefore K_strip^n(0,0)=p_n even if equality D_strip=D_act has not been established for that beta.
The strip itself supplies all nonneutral bounds needed in Section4, and restriction can only lower each entry from its ambient displacement probability.
Thus the complete argument gives

    p_n<=||K_strip^n||<=C_beta(n+1)^(d-2)p_n,
    C_beta=(2B+2)(2S+2)8^s,
    r_(l2)(K_strip)=exp(-h_2(beta)).                       (6)

For the fixed quartic and original Lehmer inputs, L170's exact core theorem identifies this strip with the actual core, so both descriptions refer to the same operator.

An explicit finite-time form of(6) is

    0 <= log||K_strip^n||-log p_n
       <= log C_beta+(d-2)log(n+1).                       (7)

The overhead is polynomial at each fixed input, but its exponent grows with degree and log C_beta also depends on degree and beta.
This is not a uniform finite-time approximation at n=O(d), and does not supply a positive Mahler gap.

For hypothetical Salem inputs with m=log beta tending to zero, the accepted L30 comparison gives h_2/m->1.
Therefore the actual full-operator radius satisfies -log r_(l2)(K_strip)/m->1, whereas the exact one-step norm in L172 has -log||K_strip|| asymptotic to pi^2 m^2/16.
This distinguishes the strong long-time loss from the weak one-step norm.
The current result identifies these rates; a new degree-independent lower bound for h_2 would still require new mathematics.

<a id="salem-strip-all-power-essential-norm"></a>
### 7. All powers retain their full norm in the essential quotient

This subsection develops the coordinator's separately supplied translation mechanism.
It is about the Salem strip of Section6, not about every general-unit core in Section1.
For every fixed n>=0,

    ||K_strip^n||_ess=||K_strip^n||,
    r_ess(K_strip)=r_(l2)(K_strip)=exp(-h_2(beta)).        (8)

Here essential norm is distance to the compact operators, and essential spectral radius means the spectral radius in the quotient B(l2(D_strip))/K(l2(D_strip)).
The standard closed-ideal, quotient-norm and spectral-radius facts are recorded in the Pet20 source unit.
The strip is infinite, as also follows from the small-real elements constructed next.

There are nonzero h_j in O with both |(h_j)_+| and |(h_j)_-| tending to zero, and with their joint neutral Euclidean norm tending to infinity after passage to a subsequence.
To see existence with arbitrarily small two-real coordinates, use the (N+1)^3 distinct elements a_0+a_1 beta+a_2 beta^2 with a_i in{0,...,N}; they are distinct since degree(beta)>=4.
Their two-real images lie in a rectangle of area O_beta(N^2).
Partition it into cells of fixed small side epsilon.
For large enough N, there are fewer cells than points, so a nonzero difference h has both real values smaller than epsilon in absolute value.
No nonzero h has real value zero, by injectivity of a field embedding.
Choose epsilon tending to zero.
If the neutral coordinates stayed bounded along a subsequence, the full norm-grid injection would leave only finitely many such h, incompatible with nonzero real values tending to zero.
This proves the asserted escape, and permits a subsequence with neutral norms separated by any prescribed finite amount.

Fix n and a finitely supported unit vector f on D_strip with ||K_strip^n f||>=||K_strip^n||-epsilon.
Its image is also finitely supported: each column has at most 3^n predecessors.
Let F and G be these two finite supports.
At every x in G,y in F, endpoint legality identifies the kernel entry with the ambient displacement law.
Indeed, starting in the strip keeps the contracting coordinate within S forward in time, while ending in the strip keeps the expanding coordinate within B backward in time.
Hence all intermediate states of every such ambient word remain in the strip.

For h with sufficiently small real embeddings, F+h and G+beta^(-n)h remain in D_strip, since F,G are finite and all their inequalities have strict margins.
Translate f to f_h on F+h.
For the retained translated rows, the displacement identity

    (y+h)-beta^n(x+beta^(-n)h)=y-beta^n x

gives exact equality of all kernel entries and therefore

    ||K_strip^n f_h|| >= ||K_strip^n f||.

Additional output rows, if present, do not affect this lower bound.
Unit status ensures beta^(-n)h belongs to O.
Choose the small-real h_j above so that the translates F+h_j are pairwise disjoint; their neutral escape permits this.
The f_(h_j) are orthonormal, hence weakly tend to zero.
Any compact operator A sends them to norm zero (Pet20, Theorem3.3.1).
Thus

    ||K_strip^n-A|| >= limsup_j ||(K_strip^n-A)f_(h_j)||
                    >= ||K_strip^n||-epsilon.

Let epsilon decrease to zero and take the infimum over compact A.
The reverse essential-norm inequality is automatic, proving the first part of(8).
Apply the spectral-radius formula in the quotient Banach algebra: the quotient power norm is precisely ||K_strip^n||_ess.
This proves the second part.
At n=0 the same infinite orthonormal sequence gives essential norm1 for the identity.

Consequently no compact perturbation can lower the essential spectral radius below the actual collision radius on these strips.
This rules out a strategy that tries to obtain the full rate only by deleting a finite neutral tail.
It does not rule out justified infinite-dimensional weighted methods, and it is not claimed for a general core that may be finite.

<a id="finite-prime-spectral-exhaustion"></a>
### 8. Finite prime-restricted cores exhaust the radius from below

The coordinator supplied this additional consequence after the identification argument.
Assume now that alpha is nontorsion, so the accepted [L157 finite-prime core theorem](Yin_L_G0157_v1.md#finite-prime-return-core) applies.
For a finite set S of maximal-order prime ideals, let D_S be the states on original zero-to-zero words whose every nonzero state is an S-unit, and let K_S be the original weighted kernel killed outside D_S.
L157 proves that D_S is finite, using its accepted [ESS02 counting input](../audits/literature/ESS02/Yin_U001.md#ess-exact-counting-bound).
That external proof is not re-audited here.
In particular D_S is not replaced by the possibly infinite ambient intersection D_act intersect({0} union E_S).

Then

    sup_(finite S) r(K_S)=r(K_act)=exp(-h_2(alpha)).       (9)

The supremum is monotone under inclusion of finite prime sets.
For S subset S', each admissible restricted word remains admissible, so D_S subset D_(S').
The smaller kernel's powers are entrywise dominated by the compression of the larger kernel's powers.
For nonnegative matrices, entrywise domination implies domination of the l2 norm: first replace a test vector by its coordinatewise absolute value.
Consequently, after extension by zero to the common ambient space,

    ||K_S^k||<=||K_(S')^k||<=||K_act^k||,
    r(K_S)<=r(K_(S'))<=r(K_act).                         (10)

For the reverse approximation, let S_n collect every prime-ideal divisor of every nonzero state on every closed original word of length at most n.
There are finitely many such words, and every nonzero algebraic integer has only finitely many prime-ideal divisors.
Hence S_n is finite, and the sequence is nested.
Every length-n closed word is entirely contained in D_(S_n), so

    (K_(S_n)^n)(0,0)=p_n.

Concatenating k of those loops gives

    (K_(S_n)^(kn))(0,0)>=p_n^k.

Taking kth-block roots and using the ordinary finite-matrix spectral-radius formula yields r(K_(S_n))>=p_n^(1/n).
Supermultiplicativity of p_n gives sup_n p_n^(1/n)=lim_n p_n^(1/n)=exp(-h_2).
Combine this with(2) and(10) to obtain(9); the increasing sequence r(K_(S_n)) itself converges to r(K_act).

The direction matters.
Since the zero self-loop remains in every D_S, all these radii are at least1/2, and their negative logarithms are finite.
The finite-prime quantities -log r(K_S) approximate h_2 from above.
A finite restricted model by itself gives a lower bound for the full radius and an upper bound for the full entropy; it cannot certify an upper full radius or a lower entropy gap without separate tail control.
There is no effective approximation rate or bounded-size prime set in(9).

For the two Salem inputs whose entire strip is the actual core, (8) and(9) hold simultaneously: finite restricted radii approach the full radius, while every fixed power retains its full norm modulo compact operators.
There is no contradiction because these finite compressions need not converge in operator norm.
The quantitative finite-prime estimates and the need to include every excursion retain the exact L157/ESS dependency boundary.

### Contribution, verification and remaining task

The drafting agent supplied the maximal-displacement atom observation, explicit translated row/column count from L91, general-unit sandwich, and exact collision/spectral identification.
The coordinator supplied the all-power essential-norm translation mechanism in Section7 and the finite-prime exhaustion deduction in Section8; the drafting agent supplied the displayed small-real construction and checked their finite support/domain and monotonicity steps.
The source formulas are accepted standard functional-analysis inputs at their recorded statement-and-applicability depth.
Section8 additionally retains L157's ESS-dependent finiteness theorem; Sections1-7 do not use ESS.

No numerical experiment or new J is used.
The entire proof is author self-checked and ready for separately assigned review.
The result resolves the operator/diagonal identification question at fixed input, including the actual quartic/Lehmer cores, while leaving the full G0001 uniform-gap gate unresolved.
The next useful operator estimate must be evaluated as an estimate for the same h_2, with the explicit finite-time overhead(7) retained.

<a id="retained-collision-radius-review"></a>
## Preserved D G0040 complete independent review



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0072_v1.md#maximum-displacement-atom-and-the-operator-limit), with its original inspected scope and relationship.

## Fixed retention map

| Retired working identity | Exact retained material |
| --- | --- |
| D G0036 | [Entire original separated-digit argument](#retained-separated-digit-argument), [exact statement](#separated-digit-strip-norm), [spectral comparison](#strip-radius-small-measure-comparison) and [complete independent finding](../audits/reviews/Yin_R_G0072_v1.md#separated-digit-strip-independent-review) |
| D G0037 | [Entire original collision-radius argument](#retained-collision-radius-argument), including [general-unit theorem](#core-operator-collision-sandwich), [Salem full strip](#salem-strip-exact-collision-radius), [essential norms](#salem-strip-all-power-essential-norm) and [finite-prime exhaustion](#finite-prime-spectral-exhaustion) |
| D G0040 | [Entire complete review account](#retained-collision-radius-review), [dated independent finding](../audits/reviews/Yin_R_G0072_v1.md#collision-radius-complete-independent-review), all inspected-input/source boundaries and its four exact bindings |

There is no new computation group: these are written arguments without a numerical certificate premise.
Existing J33/J34 and other fixed-result programs/data are untouched.
The retained review identifies the inspected D37 argument and its actual scope.
All formula lines, full proof bodies and complete independent review bodies were compared before retiring these three completed drafts.
Actual incoming consumers are relocated before deletion; unrelated working drafts and fixed mathematical sources are preserved.
