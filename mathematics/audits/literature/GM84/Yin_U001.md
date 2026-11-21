---
author: Yin
---

# Three fixed primes generating the multiplicative group modulo a prime

<a id="gm84-u001"></a>
## The subgroup and the prime count in Lemma 3

Fix any three distinct rational primes \(q,r,s\).
For each prime \(\ell>\max(q,r,s)\), write \(\Gamma_\ell\) for the image of \(\{q^a r^b s^c:a,b,c\in\mathbb Z\}\) in \(\mathbb F_\ell^\times\).
Gupta and Murty's Lemma 3 gives a constant \(\delta>0\) for this fixed triple such that, for all sufficiently large \(x\), at least \(\delta x/(\log x)^2\) primes \(\ell\le x\) have \(\Gamma_\ell=\mathbb F_\ell^\times\).
Since the ambient group is cyclic, the order of \(\Gamma_\ell\) equals the least common multiple of the three individual multiplicative orders.
The lemma makes no claim that any particular member of the triple is a primitive root.
The paper's subsequent selection among thirteen products concerns its main theorem. [Edition](readme.md#edition) · [Choice of three primes, printed page 127](../../../literature/pdf/GM84.pdf#page=1) · [Definition and Lemma 3, printed page 128](../../../literature/pdf/GM84.pdf#page=2)

The proof takes primes for which \(q\) is a quadratic nonresidue and every odd prime factor of \(\ell-1\) exceeds \(x^{1/4+\varepsilon}\), using a lower-bound sieve.
An index divisible by two would make \(q\) a quadratic residue.
An odd prime divisor of the index forces \(|\Gamma_\ell|<x^{3/4-\varepsilon}\), and the small-subgroup count in Lemma 2 makes these exceptions negligible compared with \(x/(\log x)^2\).
Thus the exceptions have already been removed in Lemma 3.
The subgroup definition, quantifiers, index argument and use of the exceptional-prime estimate were checked against the journal pages.
The analytic sieve estimates used in Lemma 1 are accepted as external inputs. [Lemmas 1–3 and the sieve references](../../../literature/pdf/GM84.pdf#page=1)
