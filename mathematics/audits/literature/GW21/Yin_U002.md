---
author: Yin
---
# GW21-U002: finite pair-law concentration and its minimal-counterexample boundary

Date: 2026-10-15.
Human author Yin.
The separately assigned f_unitary_scope reader used the already retained published PDF, verified its registered artifact identity, text-read and visually checked printed923--926/PDF2--5, and reconstructed the complete Lemma2.1 proof on924--925.
Root records that actual source-only inspection.
This is not a proof or applicability certification of the new G0001 capacity adaptation.

<a id="gw21-u002"></a>
## Accepted concentration lemma; source proof checked at the stated scope

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Green and Walker, Extremal problems for GCDs, published CPC30(6)(2021),922--929, DOI10.1017/S0963548321000092; exact retained8-page Cambridge PDF, unchanged from GW21-U001. No arXiv substitution or new acquisition.

Passages: Global epsilon setup on922; Lemma2.1 and its complete proof on924--925; Proposition1.2 on923 and the local Proposition3.1/application interface on925--926.

Inspection: Lemma2.1 statement and entire displayed proof checked, Audited within that lemma scope. Proposition1.2 and the selected minimal-counterexample/application steps were read to delimit applicability, not independently re-audited as a complete global proof. Sections4 onward and the original Koukoulopoulos--Maynard proof were not audited.


Fix the source's epsilon in(0,1), put q=2+epsilon and q'=q/(q-1), so2<q<3 and3/2<q'<2.
Let mu be a FINITELY supported probability measure on Z^2.
Let x,y be nonnegative sequences indexed by Z with their respective counting-measure l^{q'} norms equal to1.
They can be countably supported and need not be equal or be the marginals of mu.
For the positive-parameter domain needed here, take0<c<=1 and0<lambda<=4/5, and suppose for every i,j,

    mu(i,j)<=c lambda^abs(i-j) x_i y_j.

Lemma2.1 implies c>=1/9 and the existence of an integer k such that

    sum_(abs(i-k)+abs(j-k)>=2) mu(i,j)
                          <=C_epsilon lambda^(q+epsilon),

for a finite constant depending on the fixed epsilon.
The exponent q+epsilon is2+2epsilon.
The conclusion controls mass OUTSIDE the five-point cross consisting of(k,k) and its four nearest coordinate neighbors.
It does not state that the single diagonal atom has mass1 minus that same error.
No numerical C_epsilon, uniformity as epsilon approaches0, separate t parameter or extra small-lambda threshold is supplied.

Accept this established lemma at that exact domain.
The source-only proof check reconstructed the sum over displacement diagonals and the bound sum_m lambda^abs(m)<=9, the q'<2 norm comparison and Cauchy--Schwarz giving c>=1/9, and the six-region decomposition about a maximizing product x_k*y_k.
The maximum exists because the normalized l^{q'} sequences tend to0 at infinity.
With gamma=1-max_i x_i*y_i, the proof obtains gamma bounded by a fixed-epsilon multiple of lambda^q.
The final four-region tail is bounded by a multiple of lambda^(2q/q'), and2q/q'=q+epsilon.
The source's q<=3 estimate absorbs the indicated intermediate terms; the declared epsilon domain remains OPEN.
This inspection supplies no endpoint extension or numerical hidden constant.

## Why the global GCD conclusion is not an arbitrary-law theorem

Proposition1.2 is stated for a HYPOTHETICAL counterexample to Theorem1.1 that minimizes the number of primes dividing the input sets.
For the relation Omega of pairs with gcd at least D, its conclusion gives a subrelation of at least half the original size and one integer N on which every prime valuation pair has total distance at most1 from the corresponding valuations of N.
These minimum-counterexample and dense-GCD hypotheses are essential to the source's proof; this U does not export that conclusion for arbitrary capacity arrays.

The selected pages925--926 explain the connection.
The probability law mu(i,j) is the distribution of prime valuations among pairs CONDITIONED on belonging to Omega.
The quantities alpha_i and beta_j are the separate set-size proportions of the two input sets, and x_i=alpha_i^(1/q'), y_j=beta_j^(1/q').
The domination required by Lemma2.1 comes from the smaller-prime-support counterexample exclusion in equation3.1 and its consequence3.4.
It is not a general identity about marginals or a consequence of merely defining those sequences.

In that application lambda=p^(-1/q), while c is1 for the large-prime case and1/10 for the small-prime case.
The lower bound c>=1/9 excludes the latter.
The tail has exponent lambda^(q+epsilon)=p^(-1-epsilon/q), at most p^(-1-epsilon/3); the source then chooses an epsilon-dependent prime threshold for its finite total-loss bound.
These are the source's particular hypotheses and use, not a checked mapping of the new project energy-pair law.

## Actual project role and limits

The trigger was a proposed normalized exponent-pair law in the continuing G0001 weak-capacity inquiry.
Its author must still prove that law is a finite probability, produce the required normalized sequences, verify domination with c<=1 and0<lambda<=4/5, fix epsilon in the accepted range, and pay every arithmetic/totient constraint after concentration.
Neither the global integer N nor a capacity inequality follows from this source inspection alone.
The source-only reader supplied no new project phi-capacity proof or verification of the proposed parameter mapping.

The existing [GW21-U001](Yin_U001.md#gw21-u001) remains the independent earlier Theorem1.1 reading record; its reading history is not expanded retroactively.
Source: [retained published PDF](../../../literature/pdf/GW21.pdf).
This source unit concerns the new exact lemma interface and its inspection limits, not an unrestricted Mahler-gap result.
