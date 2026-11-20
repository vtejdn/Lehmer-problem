---
author: Yin
---

<a id="ps91-u001"></a>
# Zeros of a local exponential polynomial on one residue class

Normalize \(v_p(p)=1\) in a finite extension of \(\mathbb Q_p\).
Lemma 1 uses a nonzero series \(\sum b_h t^h\) converging on the closed unit disk, normalized so its coefficients are integral and at least one is a unit.
If \(k\) is the last index with unit coefficient, Strassmann's theorem gives at most \(k\) zeros there, via a degree-\(k\) polynomial times an everywhere unit-valued factor.
The article cites the proof of this lemma. [§2, pp. 217–218](../../../literature/pdf/PS91.pdf#page=3)

For Lemma 2 take pairwise distinct \(\phi_i\) with \(v_p(\phi_i)>R=1/(p-1)+\epsilon\), where \(\epsilon>0\), and nonzero polynomial coefficients \(B_i\) of degrees \(n_i-1\).
Write \(n=\sum n_i\).
Then \(F(t)=\sum B_i(t)\exp(\phi_i t)\) has at most \((n-1)(1+1/(\epsilon(p-1)))\) zeros in the closed unit disk.
The estimate is uniform in the coefficients and requires the displayed valuation inequality for each frequency. [Lemma 2, p. 218](../../../literature/pdf/PS91.pdf#page=4)

The proof annihilates \(F\) by \(\prod_i(D-\phi_i)^{n_i}\), producing a recurrence for \(c_h=h!b_h\) whose coefficient in position \(j\) has valuation greater than \(jR\).
After normalizing the \(b_h\) as in Lemma 1, induction shows \(v_p(c_{h+n-1})>hR\) for \(h\ge1\).
The factorial valuation formula then gives \(v_p(b_{h+n-1})>h\epsilon-(n-2)/(p-1)\).
For \(n\ge2\) this proof actually bounds the last unit index by \(n-1+\lfloor(n-2)/(\epsilon(p-1))\rfloor\); the single constant times an exponential when \(n=1\) has no zero.
Lemma 1 completes the stated estimate. [Eqs. (2.6)–(2.10) and conclusion, pp. 218–220](../../../literature/pdf/PS91.pdf#page=4)

<a id="classes"></a>
## Partition of the integer arguments

In §3 the roots \(\alpha_i\) are units at the chosen prime of the number field \(K\); the rational prime is chosen greater than \([K:\mathbb Q]+1\).
With residue degree \(f\) and \(q=p^f-1\), write \(h=r+qk\).
On each class the coefficients are \(B_i(t)=\alpha_i^r A_i(r+qt)\) and the frequencies are \(\phi_i=\log(\alpha_i^q)\).
Reduction in the residue field gives \(v_p(\alpha_i^q-1)\ge1/e\) with ramification index \(e\); the large-prime hypothesis puts these logarithms strictly inside the range for \(\epsilon=1/(p(p-1))\).
The assumption that no quotient of distinct roots is a root of unity makes these frequencies distinct.
Lemma 2 therefore gives at most \((n-1)(p+1)\) integer zeros in each class, for arbitrary nonzero polynomial coefficients of the indicated degrees. [§3, eqs. (3.1)–(3.6), pp. 220–221](../../../literature/pdf/PS91.pdf#page=6)

In an application with another modulus one must check the logarithm valuations and distinctness for the resulting powered roots.
If frequencies coincide, one must first combine their coefficients and check that a nonzero exponential polynomial remains; an identically vanishing residue class admits no finite zero bound.
The inspection covers Lemma 1 at statement level, the coefficient estimates proving Lemma 2 and the local residue-class substitution in §3. [Inspected edition](readme.md#edition)
