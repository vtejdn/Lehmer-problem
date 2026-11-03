---
author: Yin
---

# G0001: short annihilators, neutral completion and degree cost

Date: 2026-10-06.
This is a bounded continuation of the primary algebraic-entropy route, not a resolution of the Task.
The exact question is whether replacing a minimal annihilator by a short multiple gives a new uniform entropy certificate.
Reused inputs are the rational entropy formula in [G0001](../tasks/Yin_T_G0001_v1.md#algebraic-entropy-contract), the nonvanishing and Frobenius proof in [L G0012](Yin_L_G0012_v1.md#bounded-length-gap), and the support upper bound in [L G0007](Yin_L_G0007_v1.md#pisot-salem-attainment).
The complete current Frobenius proof is [C217v2](../claims/Yin_C_G0217_v2.md#argument), and its support comparison is [C210](../claims/Yin_C_G0210_v1.md#pisot-salem-attainment); the preceding sentence retains this calculation’s actual original input.
No novelty is claimed for these elementary consequences.

<a id="neutral-completion"></a>
## 1. What a cyclotomic multiple preserves

Let p in Z[t] be monic irreducible, noncyclotomic, with p(0) nonzero and degree d.
Let c be a monic product of cyclotomic polynomials, allowing repeated factors and c=1, and put q=pc, D=deg q.
On Q[t]/(q), multiplication by t has an exact sequence

    0 -> Q[t]/(c) -- multiplication by p --> Q[t]/(pc)
      -- reduction modulo p --> Q[t]/(p) -> 0.

The first map is well-defined and injective by cancellation in Q[t]; its image is exactly the kernel of reduction.
Both maps commute with t.
The characteristic polynomial of each quotient operator is its defining monic polynomial.
The rational entropy formula therefore gives

    h(q)=m(q)=m(p)+m(c)=m(p)=h(p),  h(c)=0.

Here m is logarithmic Mahler measure.
This remains true with repeated cyclotomic factors, without assuming the neutral operator is diagonalizable.
It is an equality of total entropies of two finite-rank flows, not an identification of every finite-set trajectory.
Arbitrary reciprocal multiplication does not preserve entropy: for reciprocal p, taking c=p gives h(p^2)=2m(p)>m(p).

<a id="short-annihilator-degree-cost"></a>
## 2. An elementary norm certificate and its exact loss

Write S=||q||_1 and let ell be any prime.
If alpha is a root of p, q(alpha)=0 and Frobenius gives q(alpha^ell) in ell Z[alpha].
This algebraic integer is nonzero: alpha^ell cannot be a root of c because alpha is not a root of unity; it cannot be a root of p by the finite-order Galois argument already proved in L G0012.
Thus its norm over Q(alpha) is a nonzero integer divisible by ell^d.
For each conjugate alpha_i,

    |q(alpha_i^ell)| <= S max(1,|alpha_i|)^(ell D).

Taking products gives

    ell^d <= S^d M(p)^(ell D),
    m(p) >= (d/D) log(ell/S)/ell.                         (1)

For S<=S0 and D/d<=C, any fixed prime ell>S0 yields the uniform positive bound log(ell/S0)/(ell C).
This transfers the previously checked minimal-polynomial certificate to an entropy-preserving presentation with an explicit degree cost.
In the rational primary formula of [L G0002](Yin_L_G0002_v1.md#capture-equivalence), imposing these two fixed bounds on every positive irreducible type therefore ensures finite capture: infinitely many positive types would have infinite total entropy.
This is a restricted consequence only.

Bounded coefficient length does not bound D/d for an arbitrarily chosen completion.
For any fixed p and N>d, take c=t^N-1.
It is a product of cyclotomic polynomials, the two coefficient blocks in q=t^N p-p are disjoint, and

    ||q||_1=2||p||_1,   D/d=1+N/d -> infinity,
    m(q)=m(p)>0.

Thus (1) degenerates on presentations of exactly the same positive-entropy flow value.
This refutes an automatic presentation-degree bound, not the possibility of choosing a better multiplier or proving a stronger sparse-polynomial theorem.
In particular, the existing Mignotte minimal-polynomial result must not be applied to reducible q without checking its hypotheses.
The stronger known sparsity bounds reported in Smy08 have different proofs and are not refuted by this loss.

<a id="binary-relations-boundary"></a>
## 3. What binary trajectory counting actually supplies

For the unit core with M(p)<2, let X_n={sum_(j=0)^(n-1) epsilon_j alpha^j : epsilon_j in {0,1}}.
The accepted BV20 support estimate used in L G0007 is |X_n|<=C_alpha n^s M(p)^n, with constants depending on alpha.
Eventually this is less than 2^n.
Two distinct binary words then have equal value, yielding a nonzero r in Z[t] with coefficients in {-1,0,1}, deg r<n, and p dividing r.

This guarantees a height-one annihilator, but gives neither a uniform bound on its number of terms or coefficient length, nor that r/p is cyclotomic.
Since r/p is an integer polynomial, multiplicativity only gives m(r)=m(p)+m(r/p)>=m(p).
A lower bound on m(r) alone does not give a lower bound on m(p).
Reciprocal symmetrization does not repair this: r(t) t^(deg r)r(t^-1) is reciprocal and has measure M(r)^2; the unwanted factor's measure is doubled as well.

Consequently the finite-digit route needs a controlled annihilator construction (including its multiplier's entropy), or a direct estimate on p.
Pigeonhole collisions by themselves do not supply such a construction.
No upper bound on first collision length uniform in p is asserted.

## Search, review and next action

The local scope checked was L G0007, L G0012, Mig78's Proposition 5 audit, and Smy08-U002 Section 5.4, which already reports known bounded-sparsity gaps but does not audit their original proofs.
On 2026-10-06 the bounded web search for "Dobrowolski Mahler measure number nonzero coefficients lower bound short polynomials length" found the primary 1991 Canadian Mathematical Bulletin article and the primary 2025 El-Serafy--McKee article.
The latter's online Section 2 distinguishes cyclotomic shortness from reciprocal shortness and explicitly warns that they can differ.
These are leads for further source intake, not accepted new theorem dependencies; no source proof, algorithm or numerical result from them is used above, and no new local source artifact is claimed.

Lead locators: [Dobrowolski 1991](https://doi.org/10.4153/CMB-1991-030-5); [El-Serafy--McKee 2025, Section 2](https://doi.org/10.4153/S0008439524000900).
The search stops here because the immediate interface question is settled by the displayed calculation; stronger sparse-polynomial constants require original-source inspection before use.

The original complete author check is retained at [R510](../audits/reviews/Yin_R_G0510_v1.md#original-neutral-completion-author-check).
The current complete neutral and sparse-completion theorem is [C221](../claims/Yin_C_G0221_v1.md#argument), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0510_v1.md#current-sparse-completion-finding).
Next useful work is to inspect the general sparse-polynomial input and then determine whether low entropy controls a measure-preserving short presentation.
Do not infer that from height-one collisions, or add another bounded-family result as if it settled unrestricted finite capture.
