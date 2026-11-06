---
author: Yin
---
# Arithmetic random matrices: global residue costs and invariant full-rank Hankel determinants

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This 2026-11-05 continuation tests global constraints omitted by the [v4 joint-local controls](Yin_L_G0446_v4.md#scope-and-strategic-assessment), under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The main agent and the terminal-prime, coefficient-lattice and joint-cycle contributors supplied and checked the arguments as ordinary author exploration.
No new Claim or independent review is asserted.
The new findings concern the measure cost of the actual v4 output, uniqueness in a prescribed coefficient class, and translation of complete Hankel determinants.
None supplies a uniform lower bound on unrestricted original inputs.

<a id="fixed-eisenstein-output-already-has-a-gap"></a>
## The actual mod-four output already has a uniform gap

The [v4 construction](Yin_L_G0446_v4.md#finite-window-irreducible-coefficient-control) imposes

    P=(x-1)^d+2x^(d/2) modulo 4

to make the translated polynomial Eisenstein at 2.
Its P is monic, irreducible and reciprocal of even degree d, has constant coefficient one and is noncyclotomic.
Put h=2^ceil(log_2 d), so d<=h<2d.
Modulo 2, P=(x-1)^d divides (x-1)^h=x^h-1.
Lifting the quotient gives integer polynomials H,B with x^h-1=PH+2B.
For any original root alpha, therefore,

    (alpha^h-1)/2=B(alpha) in Z[alpha].

This is the one-pair binary auxiliary of [C864v2](../claims/Yin_C_G0864_v2.md#statement), with actual span h<2d.
Its stronger [original-degree binomial norm bound](../claims/Yin_C_G0864_v2.md#original-binomial-norm-return) directly yields

    m(P)>d log2/(2h)>log2/4.

For completeness, write v=(alpha^h-1)/2 in O_K, where K=Q(alpha) has the original degree d.
Both v and v+1 are nonzero by nontorsion, so (alpha^(2h)-1)/4=v(v+1) is a nonzero algebraic integer.
Its full norm gives |Norm(alpha^(2h)-1)|>=4^d.
The product over all original embeddings also satisfies |Norm(alpha^(2h)-1)|<2^d exp(2h*m(P)); strictness follows from an off-circle conjugate.
These two inequalities prove the stated gap without replacing alpha by the minimal polynomial of a power.

This is a direct application of the accepted C864v2 mechanism, and is the same type of return already used for the [Eisenstein realization outputs](Yin_L_G0454_v1.md#same-output-eisenstein-return).
It strengthens the v4 assessment: not only was a small-measure upper bound absent, but this entire mod-four output family is separated from zero.
The exact captured-prime resultants and O(d log d) captured terminal mass of v4 remain valid.
They test the sufficiency of those selected local contributions, not a possible near-one family.

Replacing 2 by a fixed odd prime ell in the irreducibility congruence does not remove every uniform cost.
If P=(x-1)^d+ell*x^(d/2) modulo ell^2, put h_ell=ell^ceil(log_ell d), with d<=h_ell<ell*d.
The same Frobenius and quotient-lifting argument gives (alpha^h_ell-1)/ell in O_K.
Consequently ell^d<=|Norm(alpha^h_ell-1)|<2^d exp(h_ell*m(P)), whence

    m(P)>d*log(ell/2)/h_ell>log(ell/2)/ell>0.

This comparison allows ell to be any fixed odd prime for which the congruence is imposed.
If ell varies with d, the displayed lower bound can tend to zero, but no small-measure upper construction follows.

<a id="terminal-orders-force-crt-box-uniqueness"></a>
## Terminal residue orders force uniqueness in each small coefficient box

The next observation does not require the mod-four condition or any Eisenstein argument.
Let d=2N>=4, I={N+1,...,2N}, and for each r in I choose a prime p_r with r dividing p_r-1, as in v4.
Let S be the set of distinct selected primes and put

    R=product_(p in S)p,
    B_0=R^2,
    L_d=lcm(1,...,d),
    C=binomial(d,N).

Each a<=N has an integer multiple in I: take the least multiple strictly larger than N, which is at most N+a<=2N.
Hence lcm(I)=L_d.
For any prime ell, some r in I realizes the largest ell-power in L_d, and r divides its assigned p_r-1.
Thus L_d divides product_(p in S)(p-1), including when several orders use the same prime.
In particular R>L_d.

An elementary integral gives the stronger divisibility N*C divides L_d:

    integral_0^1 x^(N-1)(1-x)^N dx
      =(N-1)! N!/(2N)!=1/(N*C).

Expand (1-x)^N and integrate each term.
All resulting denominators are among N,N+1,...,2N, so multiplication by L_d makes the integral an integer.
The beta-integral evaluation itself follows by repeated integration by parts.
This proves the divisibility without an asymptotic estimate for primes or lcm growth.

For any monic integer polynomial with m(P)<=1, the elementary symmetric formula and the definition of Mahler measure give

    |a_j|<=exp(m(P))*binomial(d,j)<=e*C.

For reciprocal P these bounds apply to its N independent coefficients.
Since C>=6>2e,

    B_0=R^2>L_d^2>=C^2>2e*C.

Two different integer vectors in the same complete coefficient class modulo B_0 differ by at least B_0 in one coordinate.
Two vectors in the necessary small-measure coefficient box differ by at most 2e*C in every coordinate.
Therefore each fixed complete reciprocal coefficient class modulo B_0 contains at most one polynomial in this necessary box.
When N>=6, the stronger R>L_d>=N*C>2e*C shows that even a complete first-layer coefficient class modulo R has at most one such point.

For a chosen class this is an exact finite filter: take the centered representative of each independent coefficient and test the sharper bounds |a_j|<=e*binomial(d,j).
If any coordinate fails, there is no polynomial of measure at most one in that class.
If all pass, the sole candidate still needs its actual measure and the complete local constraints checked.
Changing the central coefficient by a nonzero multiple of B_0 cannot move between two candidates in the small-measure necessary box.
The central adjustment in v4 therefore supplies no small-measure tuning parameter, even after deleting its separate mod-four restriction.

Uniqueness is not nonexistence.
The allowed local roots and coefficient classes may vary, and the argument does not show that every different class fails the filter.
The coefficient bounds are necessary, not sufficient, for small Mahler measure.
No lower bound on omitted-prime mass is established.
This is a discrete prescribed-class constraint complementary to [L449's single-point/volume boundary](Yin_L_G0449_v1.md#jacobian-and-one-point-mass), not a repair of its continuous neighborhood loss.

The selected primes also supply no discriminant divisor.
The actual v4 conditions are squarefree modulo every p in S, so p does not divide disc(P) and gcd(R,disc(P))=1.
Thus B_0 cannot be inserted as a lower factor in the existing discriminant estimate |disc(P)|<=d^d exp(2(d-1)m(P)).

<a id="unit-resultant-full-rank-hankel-invariance"></a>
## Full-rank Hankel translations have invariant absolute determinant

Let P be an original monic irreducible noncyclotomic integer-unit polynomial, with companion matrix C and degree d.
Expanding det(C^n-I), combining equal products of conjugates and applying the fixed and parity signs needed for the absolute value gives

    R_n(P)=sum_(i=1)^r c_i*beta_i^n,

where the beta_i are distinct algebraic units and the nonzero c_i are integers.
The subset-product expansion is Galois invariant, and equal products carry the same combined coefficient under every Galois action.
The nonzero active set of beta_i is therefore Galois stable, also after multiplying all of them by the rational parity sign.
Its product is a rational algebraic unit, hence product_i beta_i=1 or -1.
No independence of the original roots or genericity of their subset products is assumed.

For a>=1 set H_a=(R_(a+i+j)(P))_(0<=i,j<r) and V=(beta_j^i)_(0<=i<r,1<=j<=r).
Direct multiplication gives

    H_a=V*diag(c_j*beta_j^a)*V^T,
    det H_a=(product_j c_j*beta_j^a)*product_(i<j)(beta_j-beta_i)^2.

The latter is nonzero, since the beta_i are distinct and all coefficients are nonzero.
Its absolute value is independent of a, because |product_j beta_j|=1.
Every H_a has integer entries, but the resulting nonzero integer witness cannot accumulate growth simply by moving the complete window forward.
The same conclusion holds for the active exponential expansion of any individual exterior-power trace.

The determinant factorization is classical; in Toeplitz order it is [Hillar--Levine, Theorem 3.1](https://lionellevine.github.io/hillarlevineAMSrevised.pdf), printed page 7.
The relevant feature here is its specialization after all original unit products and cancellations have been retained.
This is not a new general Hankel determinant formula, and it says nothing comparable about every smaller-rank minor.

For the original power sums s_n=tr(C^n), the same calculation at rank d gives

    |det(s_(a+i+j))_(0<=i,j<d)|=|disc P|.

The Vandermonde row norm bound then gives |disc P|<=d^d exp(2(d-1)m(P)), exactly the N=d boundary of [C209](../claims/Yin_C_G0209_v1.md#statement).
This lower-order complete determinant thus returns the existing discriminant cost, with no new income from translation.

For any incomplete size k>=1, the elementary bound R_n(P)<=2^d exp(n*m(P)) instead gives

    |det(R_(a+i+j)(P))_(0<=i,j<k)|
      <=k^(k/2)*2^(d*k)*exp(m(P)*(k*a+k*(k-1))).

To see this, divide row i by exp(m(P)*(a+i)) and column j by exp(m(P)*j).
Every remaining entry is at most 2^d in absolute value, and Hadamard supplies the stated factor.
A nonzero integer lower bound of one is compatible with the large baseline even at m=0, so this estimate alone gives no positive measure lower bound.
The sharper information needed for these smaller minors remains unsupplied.

<a id="global-cost-return-and-source-limits"></a>
## Return and source limits

The actual v4 mod-four family is now explicitly assigned to an existing uniform-gap class.
The independent prescribed-class uniqueness argument survives without that mod-four condition, but leaves a possible single candidate in each changing class.
The complete Hankel determinant is shift-invariant on the original unit domain, whereas the smaller-minor estimate retains a dimension baseline.
None of these statements forces the missing quadratic terminal mass for arbitrary sufficiently small original measure.
The current random-matrix direction therefore remains a diagnostic within the existing strategies, without a newly selected covering mechanism.

Hillar--Levine is recorded as HL04 in the [bibliography](../literature/references.bib).
The actually inspected original is the linked twelve-page author manuscript, not an identified final publisher edition.
Theorem 3.1 and its Vandermonde proof on printed page 7 were directly read by the main agent and the joint-cycle contributor; the same factorization is supplied above.
The introductory Theorems 1.1, 1.4 and 1.5 and the concluding discussion on printed page 10 distinguish exponentially many generic reconstruction data from short input-dependent nonlinear relations.
Those short relations are not short linear recurrences or uniform integer-height estimates, and no source-wide proof audit is claimed.
The existing [Ste13 statement screen](../audits/literature/Ste13/readme.md#ste13-discovery-screen) already records the full-layer estimates proportional to m(P), with their degree-dependent threshold and source limits; rereading those statements supplies no additional constant floor.
The proofs of the original-input norm return and the coefficient-class assertions above use no new native computation or uninspected source theorem.
