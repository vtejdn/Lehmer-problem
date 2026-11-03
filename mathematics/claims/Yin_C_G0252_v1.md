---
author: Yin
---

# Exact torsion scalar periods and complete twist/substitution boundaries

This retains the entire original 2026-10-07 proof of [L71](../ledger/Yin_L_G0071_v1.md).
Neutral whole-flow obstructions, fixed-seed twists and full root substitutions remain separate from the unproved pure-positive irreducible near-one coverage problem.

## Statement

For every monic integer polynomial P of positive degree and constant coefficient +/-1, let a_p(P) be the least positive exponent for which t^a is a nonzero scalar in the full algebra F_p[t]/P, equivalently for the integral companion matrix.
All quotient multiplicities and nilpotents remain present.
For a root of unity xi and any rational prime p, integrality of (xi-c)/p for a nonzero scalar residue c forces xi=1 or-1.
Conversely both possibilities are scalar at every prime.
Thus for every N>=1 and every prime p, including ramified ones,

    a_p(Phi_N)=N/gcd(N,2),

also if order divisibility is weakened to mere number-field integrality.
For the primorial N_X=product_(ell<=X,ell prime)ell, X>=2,

    a_p(Phi_(N_X))/phi(N_X)
      =(1/2)product_(ell<=X)(1-1/ell)^(-1) -> infinity

uniformly over the chosen prime, by the complete elementary Euler-product/harmonic proof.
This is zero entropy, where the nontorsion auxiliary's nonvanishing hypothesis is unavailable.

Fix a nontorsion algebraic unit beta of degree delta with m_beta>0 and companion B.
The semisimple integral automorphisms A_N=B direct_sum Companion(Phi_N), N=N_X, have rank delta+phi(N) and fixed entropy m_beta, but every whole-flow scalar exponent at any prime satisfies a>=N/2 and a/rank(A_N) tends to infinity.
The neutral block is explicit; removing it leaves the same fixed positive irreducible core, which already captures all entropy.
This does not give an irreducible positive small-Mahler counterfamily, even if the fixed beta is the accepted small Lehmer control.

For the fixed-seed twists alpha_N=beta zeta_N with d_N=deg alpha_N,

    m(alpha_N)/d_N=m_beta/delta,
    phi(N)<=delta d_N,
    m(alpha_N)>=phi(N)m_beta/delta^2.

Hence their Mahler measures diverge along the primorials rather than staying small, without assuming generation of the full compositum.
They eventually lose degree under their N-th powers when phi(N)>delta^2.
No statement about varying positive seeds is inferred.

For any monic integer P of degree delta>=1 with unit constant coefficient, any n>=1 and every prime p, the full root substitution Q_n(t)=P(t^n) satisfies

    a_p(Q_n)=n a_p(P),
    a_p(Q_n)/deg Q_n=a_p(P)/delta,
    M(Q_n)=M(P),
    house(Q_n)=house(P)^(1/n).

The complete free-module proof includes nonreduced quotients and primes dividing n, with no irreducibility assumption for these identities.
If both P and P(t^n) are irreducible and n>1, a root alpha has beta=alpha^n of degree delta<n delta and relative minimal polynomial X^n-beta, so

    Norm_(Q(alpha)/Q(beta))(alpha)=(-1)^(n+1)beta.

The displayed norm-descent step returns the original seed up to sign and the same positive Mahler measure.
For an individually chosen factor of a reducible substitution, degree and period require separate analysis; no full-quotient ratio is silently transferred.
No general scalar coverage, unrestricted gap or entropy noncapture counterexample is constructed.

## Current assessment

[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:19 |
| status | open |
| reason | Register the complete original mathematical argument, exact domains and already retained evidence interfaces; actual current whole review and adoption follow separately. Registration performs no computation, source acquisition, numerical certification, research resumption or independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact statement](#statement) | All-prime torsion scalar periods and unbounded degree ratio, semisimple positive whole-flow obstruction, fixed-seed twist height/degree escape and exact full-substitution period/measure identities. |
| argument | [Entire retained proof](#argument) | Complete torsion norm/equality argument, Euler-product divergence, neutral direct-sum entropy/semisimplicity/asymptotics, full compositum height proof and nonreduced free-module/relative-norm substitution proof. |
| dependency | [Accepted total entropy](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Only the finite-dimensional characteristic-polynomial Mahler formula and neutral cyclotomic weight, with total rather than normalized entropy. |
| dependency | [Integral-lattice entropy transfer](Yin_C_G0236_v1.md#adjoint-entropy-comparison) | Complete rational-to-integral finite-set transfer for the actual integral direct-sum automorphisms. |
| support | [Exact scalar power-order interface](Yin_C_G0244_v1.md#scalar-collapse-root-matrix-interface) | Full quotient including nilpotents and the nontorsion nonvanishing boundary; the torsion equality case is proved here directly. |
| support | [Weaker field-integral scalar transfer](Yin_C_G0246_v1.md#gim%2B10-arbitrary-prime-scalar-transfer) | Context for the weaker divisibility convention only; no published numerical margin is needed by any torsion/twist/substitution proof here. |
| support | [Rational positive-factor capture scope](Yin_C_G0205_v1.md#capture-equivalence) | Coverage belongs to positive irreducible factors with multiplicity; arbitrary neutral factors cannot be imposed in a stronger common-period target. |
| support | [Complete all-power existence descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Only the exact displayed special norm step and unchanged positive measure for an irreducible full root substitution; no factor-wise or arbitrary-input pointwise strengthening. |
| support | [Accepted optional small positive seed](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | A fixed genuine positive small-measure irreducible unit can be chosen for the reducible whole-flow example; it does not make a pure-positive-core counterfamily. |

## Complete retained argument

<a id="argument"></a>

<a id="scalar-period-definition"></a>
### Actual scalar periods, with no squarefree-reduction assumption

For a monic integer polynomial P of positive degree and constant coefficient +/-1, write x for the residue of t in

    R_p(P)=F_p[t]/(P mod p).

It is a unit in this finite algebra.
Define a_p(P) to be the least positive integer a for which x^a=c for some c in F_p^*.
Such an exponent exists, since some positive power of the unit x is 1.
Equivalently the integral companion matrix satisfies A^a=cI modulo p.
This definition uses the entire quotient algebra, including nilpotents at ramified primes, not only its distinct geometric roots.

For irreducible P and a root alpha, this is the actual order congruence alpha^a-c in p Z[alpha].
The distinction from a root-only assertion is the one in [L G0067](Yin_C_G0244_v1.md#scalar-collapse-root-matrix-interface).
The stronger transfer of [L G0069](Yin_C_G0246_v1.md#gim%2B10-arbitrary-prime-scalar-transfer) only requires (alpha^a-c)/p to be an algebraic integer.
The next torsion calculation applies even to that weaker divisibility condition.

<a id="root-of-unity-exact-scalar-period"></a>
### A root of unity has no earlier modular scalar power

Let xi be any root of unity, p any rational prime, and suppose that (xi-c)/p is integral for a nonzero scalar residue c modulo p.
Then

    xi=1 or xi=-1.                                   (1)

This follows directly from norms, without a ramification analysis.
For odd p choose the balanced integer representative c, so 1<=|c|<=(p-1)/2.
If xi-c were nonzero, its norm over Q(xi), of degree d, would satisfy

    p^d<=|Norm(xi-c)|
         <=(1+|c|)^d<=((p+1)/2)^d<p^d.

The first inequality uses integrality of (xi-c)/p and its nonzero integer norm.
Every conjugate of xi has modulus 1, giving the upper bound.
Therefore xi=c is a rational root of unity, hence 1 or -1.

For p=2 take c=1.
Either xi=1, or the same norm argument gives

    2^d<=|Norm(xi-1)|<=2^d.

Equality forces every conjugate factor |sigma(xi)-1| to be 2.
A point on the unit circle has distance 2 from 1 only at -1, so xi=-1.
Conversely both 1 and -1 satisfy a scalar congruence at every prime.
This proves (1), including the equality boundary that prevents applying a positive nonzero-norm gap to torsion.

Apply (1) to xi=zeta_N^a, with zeta_N primitive.
The condition is equivalent to N dividing 2a.
Thus for every rational prime p,

    a_p(Phi_N)=N/gcd(N,2).                            (2)

The value is independent of p, even at primes dividing N.
It is also the minimum if one replaces order divisibility by mere integrality of (zeta_N^a-c)/p.
No inference that repeated reduced roots alone give scalar multiplication is used.

<a id="cyclotomic-period-degree-obstruction"></a>
### The scalar period divided by cyclotomic degree is unbounded

Let N_X be the product of all primes at most X, with X>=2.
Then N_X is even and deg Phi_(N_X)=phi(N_X), so (2) gives

    a_p(Phi_(N_X))/phi(N_X)
       =N_X/[2phi(N_X)]
       =(1/2) product_(ell<=X, ell prime) (1-1/ell)^(-1).
                                                               (3)

This tends to infinity uniformly with respect to the choice of p.
An elementary proof needs no prime-distribution asymptotic: expanding the finite Euler product into geometric series includes every term 1/n with n<=X, because its prime divisors are at most X.
The product is therefore at least sum_(1<=n<=X) 1/n, which diverges.

Consequently no fixed C can cover all cyclotomic inputs by actual scalar congruences a<=C deg P, even if one may select an arbitrary prime separately for each input.
These inputs have exactly zero entropy.
In the norm certificates of L G0067--0069 the relevant auxiliary value can vanish when the scalar power becomes +/-1; the nonvanishing hypothesis is indispensable.
This is not a positive-entropy counterexample or a failure of their stated non-torsion theorems.

<a id="positive-whole-flow-neutral-obstruction"></a>
### A semisimple positive-entropy whole-flow obstruction

Fix a nontorsion algebraic unit beta of degree delta, with companion matrix B and m_beta=log M(P_beta)>0.
For N=N_X above consider the actual integral automorphism

    A_N=B direct_sum Companion(Phi_N).

Its rank and algebraic entropy are

    rank(A_N)=delta+phi(N),       h(A_N)=m_beta.       (4)

The characteristic polynomial is P_beta Phi_N.
These are distinct separable irreducible polynomials, so A_N is semisimple over an algebraic closure; no nontrivial Jordan block causes this example.
The entropy equality follows directly from the accepted characteristic-polynomial Mahler formula, since M(Phi_N)=1.

If A_N^a=cI modulo any prime p, its cyclotomic block has that same scalar power.
Hence (2) implies

    a>=N/2,
    a/rank(A_N)>=N/[2(delta+phi(N))] -> infinity.     (5)

For example once phi(N)>=delta, the last ratio is at least N/[4phi(N)], and the Euler-product argument applies.
The totients along these primorials tend to infinity, since their product formula contains increasingly many factors ell-1>=2.
Some full scalar exponent always exists at every p because A_N mod p is an invertible matrix over a finite field; (5) is an actual lower bound on that exponent, not a claim of nonexistence.

Thus even fixed positive entropy and semisimplicity do not force a linearly bounded whole-flow scalar exponent.
One may choose the retained Lehmer input for beta, putting the common positive Mahler measure in its known small-measure window.
The obstruction is still explicitly reducible: all extra degree comes from the neutral factor Phi_N.
Removing it leaves the same fixed positive irreducible factor B, which already captures all entropy.

This explains the scope needed when using the local criteria of L G0067--0068 in the finite-capture statement of [L G0002](Yin_C_G0205_v1.md#capture-equivalence): coverage belongs to the positive irreducible constituents, counted with multiplicity.
A requirement that the complete flow, including arbitrary neutral constituents, have a short scalar period is strictly stronger and is false by (4)--(5).
No irreducible nontorsion small-core counterfamily has been produced here.

<a id="fixed-seed-torsion-twist-boundary"></a>
### Twisting a fixed nontorsion unit does not preserve small measure

Keep beta fixed and set alpha_N=beta zeta_N.
These are nontorsion algebraic units.
Write d_N=deg alpha_N.
In a common number field L containing beta and zeta_N, every embedding has |sigma(alpha_N)|=|sigma(beta)|.
Counting the embedding fibers gives

    m(alpha_N)/d_N=m_beta/delta.                     (6)

This is invariance of absolute logarithmic height under a root-of-unity twist, not invariance of the unnormalized Mahler measure.
Also zeta_N=alpha_N/beta belongs to Q(alpha_N,beta), so

    phi(N)<=[Q(alpha_N,beta):Q]<=delta d_N.

Together with (6),

    m(alpha_N)>=phi(N) m_beta/delta^2.               (7)

In particular it tends to infinity along the primorial sequence.
Thus a fixed positive seed cannot transfer (3) into an unbounded family of sufficiently small positive Mahler measures by twisting.
No assumption that alpha_N generates the entire compositum is needed for (6)--(7).

There is a separate endpoint obstruction as well.
Since alpha_N^N=beta^N has degree at most delta, whereas d_N>delta whenever phi(N)>delta^2, these twists eventually lose degree under the N-th power.
They do not remain all-power-stable inputs.
This argument is only for a fixed beta.
It does not rule out a construction with varying positive seeds; such a construction would need its own measure and degree estimates.

<a id="root-substitution-scalar-cost-invariance"></a>
### Full root substitution preserves normalized scalar cost

There is an exact algebraic comparison for the other natural operation Q_n(t)=P(t^n), where P is any monic integer polynomial of degree delta>=1 and unit constant coefficient, and n>=1.
At every prime p,

    a_p(Q_n)=n a_p(P),
    a_p(Q_n)/deg Q_n=a_p(P)/delta.                   (8)

Indeed put R=F_p[x]/(P(x)) and form

    R[t]/(t^n-x),

which is canonically F_p[t]/(P(t^n)).
The relation is monic, so this is a free R-module with basis 1,t,...,t^(n-1).
Moreover x is a unit because P(0) is a unit, and consequently t is a unit too.
Write a=nq+r with 0<=r<n.
Then t^a=t^r x^q.
If r!=0 its coefficient in the r-th free summand is the nonzero unit x^q, so it cannot equal a scalar c in F_p^* in the zeroth summand.
If r=0, the equality is exactly x^q=c in R.
Thus the positive scalar exponents are precisely n times those for P, proving (8).
This holds in nonreduced algebras as well; no prime dividing n is excluded.

Root products also give the exact identities

    M(P(t^n))=M(P),
    house(P(t^n))=house(P)^(1/n).                    (9)

Each root of P contributes n roots of equal modulus equal to its n-th root, proving both formulas.
Moving the roots toward the unit circle therefore does not move the Mahler measure toward one; (8) shows that the normalized scalar cost is unchanged too.

If P is irreducible and P(t^n) is also irreducible, a root alpha of the latter satisfies beta=alpha^n with deg beta=delta and deg alpha=n delta.
For n>1 this explicitly fails all-power degree preservation.
Moreover the relative minimal polynomial is X^n-beta, and

    Norm_(Q(alpha)/Q(beta))(alpha)=(-1)^(n+1) beta.    (10)

Thus the existence descent of [L G0059](Yin_C_G0231_v1.md#all-positive-power-existence-descent) returns the original seed up to sign, with the same positive Mahler measure.
No assertion of irreducibility for arbitrary or infinitely many n is needed for (8)--(9).
If one instead selects an irreducible factor of a reducible P(t^n), its degree and scalar period must be analyzed separately; (8) for the full quotient does not establish the same ratio for that factor.
