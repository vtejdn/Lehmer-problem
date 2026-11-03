---
author: Yin
---

<a id="gk24-u001"></a>
# GK24-U001: the finite-field Dirichlet root bound used in irreducible completion

## Source and inspection

[Source and edition notes](readme.md).

Source edition: GK24; [retained PDF](../../../literature/pdf/GK24.pdf).

Passages: Published BLMS 56(7) (2024), 2315--2337, institutional copy of publisher layout. Theorem 3.2 and preceding degree statement, printed p. 2326 / PDF p. 12; Lemma 3.3 and its proof, printed p. 2327 / PDF p. 13.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148. Assigned source reviewer directly read and rendered both pages, checked the logarithmic-derivative deduction and the exact modulus used by Ope26c. Coordinator also inspected the extracted primary statements. Weil's original theorem proof and the rest of the article were not re-audited.


## State and accepted external input

**Read** for the retained Weil theorem; **Audited within scope** for the short logarithmic-derivative consequence and the explicit specialization below.
The established root bound is accepted as an external input after checking its primary statement and applicability.

Let $\chi$ be a nonprincipal Dirichlet character modulo a nonconstant $Q\in\mathbb F_q[t]$, extended by zero on nonunits.
The source gives an $L$-polynomial of degree $d_\chi<\deg Q$ whose reciprocal roots have modulus 1 or $\sqrt q$.
Hence, for every $s\ge1$,
$$\left|\sum_{f\text{ monic},\ \deg f=s}\chi(f)\Lambda(f)\right|\le d_\chi q^{s/2},$$
where $\Lambda(P^k)=\deg P$ and is zero otherwise.
Taking the logarithmic derivative of the Euler product and the finite root product gives the same power sum (up to the displayed common sign); the modulus estimate follows.
This short deduction was checked.
The stated input covers even and imprimitive nonprincipal characters, not only primitive or odd ones.

## Exact specialization used in family153

In [Ope26c-U001](../Ope26c/Yin_U001.md#ope26c-u001), set $q=2$ and $Q=t^\ell$.
There are $2^{\ell-1}$ invertible residue classes.
The nonprincipal weighted degree-$s$ sums have magnitude at most $\ell 2^{s/2}$; the principal sum equals $2^s-1$ because only the prime $t$ is removed.
Character orthogonality gives a uniform lower bound in every invertible residue class.
Proper prime powers contribute at most $s2^{s/2}$.
With $\ell=Dn+1$ and $s=dn$, the positive main term dominates when $d>2D$.
No unchecked restriction on characters prevents the argument.

## Search and proof boundary

The primary paper was retrieved to resolve the classification's exact irreducible-completion dependency, after the local reuse check.
The published article and institutional copy were located from its title/authors and DOI; the web reader's HTTP 403 was followed by a successful ordinary verified-TLS direct download.
No unobserved redirect metadata is asserted.

Weil's original proof is retained, not reconstructed.
The article's high-trace equidistribution results and other conductor estimates are outside scope.
This accepted input resolves this particular external dependency; it is not a new local proof of finite-field RH or a formalization result.
