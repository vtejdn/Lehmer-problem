---
author: Yin
---

# Prime-degree permutation groups and two fixed points

<a id="mu03-u001"></a>
<a id="burnside-affine"></a>
## The source theorem in its affine form

Let \(p\) be prime and let \(G\le\operatorname{Sym}(\Omega)\) act transitively on a set \(\Omega\) of size \(p\).
The [author manuscript](readme.md#arxiv-v1), p. 1, “Proof of Burnside's theorem,” proves that if \(G\) is not doubly transitive, there is a labeling \(\Omega\simeq\mathbb F_p\) under which
\[
       G\le\operatorname{AGL}(1,p)
         =\{x\mapsto ax+b:a\in\mathbb F_p^\times,
                              \ b\in\mathbb F_p\}.
\]
Doubly transitive means transitive on ordered pairs of distinct points.
The affine containment is explicit in this proof, rather than an inference from the abstract's solvability conclusion.

The proof labels a \(p\)-cycle as translation and uses an orbit on ordered unequal pairs to obtain an invariant nonempty proper set of nonzero differences.
Proposition 1 then makes every group element affine.
I read the original PDF pp. 1–3, including rendered formulas, and checked this deduction from Proposition 1.
The proposition's interpolation proof on pp. 2–3 and the cited historical proofs were not independently re-audited.
The established theorem is accepted here at this stated scope.

<a id="two-fixed-points"></a>
## Direct specialization for a nonidentity permutation

If such a \(G\) contains a nonidentity permutation fixing two distinct points, it is doubly transitive.
Indeed an affine map fixing \(x\ne y\) satisfies
\[
        (a-1)x+b=(a-1)y+b=0.
\]
Subtracting gives \(a=1\), and then \(b=0\), so that map is the identity.
This directly excludes the alternative supplied above; it does not require a classification of doubly transitive groups.
For an abstract group action, apply the statement to its permutation image: a nonidentity element in the kernel is not a nonidentity permutation.
The prime degree and transitivity hypotheses remain necessary inputs to this application.
