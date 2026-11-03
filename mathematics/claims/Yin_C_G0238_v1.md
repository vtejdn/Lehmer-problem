---
author: Yin
---

# Relative-unit stitch obstructions and entropy-increasing upper-half descent

This retains the complete original2026-10-06 algebraic arguments, without promoting a failed descent into a refutation of other methods.

## Statement

Let p be monic irreducible reciprocal in Z[t], M(p)>1, alpha a root, K=Q(alpha) and sigma(alpha)=alpha^-1.
For Q in Z[t] nonzero of degree a, integer k>=0, eta in{1,-1}, x=Q(alpha)!=0 and p dividing t^kQ+eta Q*, one has x/sigma(x)=−eta alpha^(a−k).
Norms and all finite principal-ideal valuations leave an unbounded alpha-unit direction; every positive gap m has a nonzero integer stitch p dividing t^(a+m)Q+eta Q*, with a<deg p, without a promised monic or bounded-length Q or cyclotomic quotient.
If additionally1<M(p)<theta, theta the real root of t^3−t−1, take a cyclotomic completion q minimizing its coefficient length L(p) and then its degree.
The full anti-reciprocal upper-half split of (t−q(0))q yields monic R with R(0)!=0, deg R<deg q and coefficient length at most L(p), but M(R)>=theta>M(p).
Thus that particular degree descent increases entropy, while no nonexistence theorem for other descents or small-measure sequences is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:36 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All stated reciprocal irreducible unit, nonzero evaluation, arbitrary exponent gap, monic minimal-length completion and M<theta domains; preserve the missing monicity/length/cyclotomic-quotient conditions and the exact entropy-increase conclusion. |
| argument | [Argument](#argument) | Complete relative-field, norm and finite-ideal invariant, explicit arbitrary-gap representative, all-parity upper-half splitting and nonreciprocal-factor argument; no uniform shortness or gap follows. |
| dependency | [Nonreciprocal source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only the accepted irreducible nonreciprocal lower bound theta at its original statement/applicability depth; no new source-proof audit. |
| dependency | [Completion definitions](Yin_C_G0233_v1.md#completion-invariants) | Exact monic cyclotomic products, minimum coefficient length and existence of a least-degree minimizing completion. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:44 |
| status | proved |
| reason | The complete exact current statement and retained argument were actually checked in the selected whole self finding; source depths, counterexamples and nonclaims remain explicit. This adoption does not complete any Task or certify an independent relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All stated reciprocal irreducible unit, nonzero evaluation, arbitrary exponent gap, monic minimal-length completion and M<theta domains; preserve the missing monicity/length/cyclotomic-quotient conditions and the exact entropy-increase conclusion. |
| argument | [Argument](#argument) | Complete relative-field, norm and finite-ideal invariant, explicit arbitrary-gap representative, all-parity upper-half splitting and nonreciprocal-factor argument; no uniform shortness or gap follows. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0518_v1.md#current-reciprocal-stitch-finding) | Complete current statement and argument at the exact selected scopes; actual self-review. |
| dependency | [Nonreciprocal source](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only the accepted irreducible nonreciprocal lower bound theta at its original statement/applicability depth; no new source-proof audit. |
| dependency | [Completion definitions](Yin_C_G0233_v1.md#completion-invariants) | Exact monic cyclotomic products, minimum coefficient length and existence of a least-degree minimizing completion. |

## Argument

<a id="relative-unit-orbit"></a>
### Norms and finite valuations leave an unbounded unit direction

Let p be monic irreducible reciprocal, with M(p)>1, and let alpha be a root.
Then p has even degree, constant coefficient 1, and alpha is a unit.
The map alpha -> alpha^{-1} extends to a nontrivial field automorphism sigma of K=Q(alpha).
Its fixed field is K^+=Q(alpha+alpha^{-1}): alpha solves t^2-(alpha+alpha^{-1})t+1, and alpha!=alpha^{-1}, so [K:K^+]=2.

Let Q be a nonzero integer polynomial of degree a, Q*(t)=t^a Q(t^{-1}), eta in {1,-1}, and suppose

    p divides t^k Q+eta Q*,       x=Q(alpha)!=0.

Evaluation gives the exact relation

    x/sigma(x) = -eta alpha^{a-k}.                         (1)

Inversion permutes the conjugates of alpha and N_K/Q(alpha)=1.
Hence Res(p,Q*)=Res(p,Q).
Taking absolute norms of the root relation in (1) yields an identity independent of k.
It cannot bound the exponent gap.

The finite-place information is stronger: (1) implies equality of principal fractional ideals (x)=(sigma(x)) in the full ring of integers.
It must not be discarded as though only the norm were known.
Nevertheless it still leaves an unbounded direction.
For every integer j put x_j=alpha^j x.
Then

    (x_j)=(x),
    x_j/sigma(x_j)=-eta alpha^{a-k+2j}.

All finite valuations stay fixed while the exponent varies through an unbounded arithmetic progression.
If x lies in Z[alpha], so does every x_j, including negative j: alpha^{-1} lies in Z[alpha] because p has constant coefficient 1.
Every x_j therefore has an integer polynomial representative of degree less than deg p, but no uniform coefficient bound follows.

There is also an explicit solution for arbitrarily prescribed positive exponent gaps.
For any m>=1 set beta=-eta alpha^{-m} and x=1+beta.
Non-torsion of alpha ensures x!=0.
Since sigma(beta)=beta^{-1},

    x/sigma(x)=beta.

Choose Q in Z[t] with Q(alpha)=x and a=deg Q<deg p.
Substitution in (1) gives

    p divides t^{a+m}Q+eta Q*.

This is a nonzero polynomial: its upper part starts strictly above degree a while its lower part has degree at most a.
Thus the existence of a reciprocal stitch with arbitrary separation is no obstruction even for a fixed p.
This construction guarantees neither monicity nor bounded coefficient length for Q, nor a cyclotomic quotient.
Those are precisely the conditions a useful arithmetic descent must retain.

<a id="half-prefix-entropy-increase"></a>
### Degree halving can strictly increase entropy

Suppose additionally 1<M(p)<theta.
Choose a monic cyclotomic multiple q=p c minimizing first its coefficient length ||q||_1=L(p), and then its degree N among those minimizers.
Both choices exist by well-ordering of positive integers.
Put epsilon=q(0) in {1,-1}.
Every factor is reciprocal up to sign, so q*=epsilon q.
Consequently

    q'=(t-epsilon)q,        (q')*=-q',       deg q'=D=N+1.

Set k=floor(D/2)+1.
Taking the upper coefficients of q' gives a monic Q of degree D-k with

    q'=t^k Q-Q*,       ||Q||_1=||q'||_1/2<=L(p).

When D is even the central coefficient is zero, by anti-reciprocity, so this splitting includes every term.
Strip the monomial factor Q=t^b R, where R is monic and R(0)!=0.
Since Q*=R*,

    q'=t^{k+b}R-R*,       deg R<=D-k<N,
    ||R||_1<=L(p).

R cannot be reciprocal up to sign.
Otherwise R*=delta R, delta in {1,-1}, and

    q'=R(t^{k+b}-delta).

The binomial is cyclotomic.
The only noncyclotomic irreducible factor of q' is p, of multiplicity one, so R is p times a cyclotomic product.
Its length is at most L(p), and its degree is below the chosen minimum N, a contradiction.

If |R(0)|>=2, M(R)>=2.
Otherwise R is a unit polynomial and, being nonreciprocal, has a nonreciprocal irreducible factor.
The accepted Smyth bound for that factor gives M(R)>=theta.
In either case

    log M(R) >= log theta > log M(p).

Thus this natural degree-reducing prefix operation is not entropy-nonincreasing in the remaining small-measure core.
Its shorter degree and controlled coefficient length do not make it an admissible descent toward a small entropy counterexample.

### Consequence and review boundary

Neither obstruction rules out a descent preserving the full combination of monicity, small coefficient length, and a cyclotomic quotient.
The norm calculation says finite valuations alone do not enforce it; the prefix calculation says a specific natural degree descent violates its entropy requirement.
The next candidate must control that combination directly.
No reduction of general Lehmer to Salem numbers, bound across number fields, or existence of a sequence with M tending to 1 is asserted.
