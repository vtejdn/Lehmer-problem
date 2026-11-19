---
author: Yin
---

<a id="eps99-u001"></a>
# Parabolic fixed points and infinite critical orbits of a rational map

<a id="fixed-points"></a>
## Theorem 1 at multiplier one

Let \(T\) be a rational self-map of the complex projective line of degree greater than one.
An infinite critical orbit tail is an equivalence class of critical points with infinite forward orbit, where two such points are equivalent when some forward iterates coincide.
Write \(\delta(T)\) for the number of these classes.
For a fixed point \(a\) of multiplier one, write \(q_a=\operatorname{ord}_a(T-\mathrm{id})-1\), taking the difference in a local coordinate centered at \(a\).
This positive integer is the parabolic multiplicity \(\nu\) of [Eps99, Section 1, equation (1), p. 1](readme.md#arxiv-v1) when the multiplier has order one.

For every set \(S\) of distinct fixed points of multiplier one, Theorem 1, p. 1, gives
\[
                      \sum_{a\in S}q_a\le\delta(T).
\]
Indeed the theorem bounds the sum of Epstein's weights over periodic cycles by \(\delta(T)\), and the weight of each fixed point in \(S\) is \(q_a\) or \(q_a+1\) according to its iterative residue.
Replacing each critical point by its first image preserves whether its forward orbit is infinite and whether it eventually meets another orbit.
Thus \(\delta(T)\) can equally be counted using the orbits of the distinct critical values.
The dimension argument on pp. 4–5 identifies \(\delta(T)\) with the number of new forward images after an initial segment containing all critical orbit relations.

I checked the statement, the multiplier-one specialization and this interpretation of the orbit count, and accept Theorem 1 as an external input for maps of degree greater than one.
The analytic arguments establishing its supporting Propositions 1 and 2 were outside this inspection.
