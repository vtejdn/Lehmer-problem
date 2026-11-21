---
author: Yin
---

# Common invariant sizes of four independent permutations

<a id="efg17-u001"></a>
## A uniform tail bound

Let \(\pi_1,\ldots,\pi_4\) be independent uniform elements of \(S_n\).
Call \(\ell\) a common invariant size if for each \(i\) there exists a set \(A_i\subseteq\{1,\ldots,n\}\) of size \(\ell\) with \(\pi_i(A_i)=A_i\).
Each \(A_i\) is a union of cycles of its own permutation, so the four subsets may differ.
Proposition 2.1 on page 3 of the [revised preprint](readme.md#arxiv-v2) gives absolute constants \(C,c>0\) such that, for all integers \(1\le k\le n/2\), the probability of a common invariant size in \((k/2,k]\) is at most \(Ck^{-c}\).
The proof on pages 5–6 uses Lemma 2.2 to discard permutations with too many short cycles, then applies Lemma 2.3 and independence before summing over candidate sizes.
The two counting lemmas are used as stated here.

For an integer \(1\le K\le N=\lfloor n/2\rfloor\), the probability of a common invariant size in \((K,N]\) is \(O(K^{-c})\), uniformly in \(n\).
Indeed, take all full intervals \((2^{j-1}K,2^jK]\) with \(j\ge1\) and \(2^jK\le N\).
The remaining interval lies in \((N/2,N]\), so the total bound is at most \(CK^{-c}\sum_{j\ge1}2^{-jc}+CN^{-c}\).
The authors use this finite tail estimate on page 8 in the proof of Theorem 1.1 with \(\pi_1\) conditioned to be odd.
For any specified signs on \(r\) of the four permutations, the conditioning event has probability \(2^{-r}\) for \(n\ge2\), so the same upper bounds hold with constants multiplied by at most \(2^r\).
This conditioning argument also covers four independent uniform even permutations.
Lemma 2.6 on page 7 concerns the separate limit of counts of cycles of bounded length under a prescribed sign as \(n\to\infty\), with the length cutoff fixed.
