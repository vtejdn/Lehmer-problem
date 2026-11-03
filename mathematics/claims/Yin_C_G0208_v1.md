---
author: Yin
---

# Unbounded short-free-pair obstruction in the exact two-map affine family

Provenance: source specialization with the complete local positive-word argument.
The mechanism is attributed to Bre07, Theorem1.7 and Section7, Theorem7.2/proof, at the exact passage scope retained in [L G0001](../ledger/Yin_L_G0001_v1.md#affine-free-pair-obstruction).
The original local argument dates to 2026-10-06.
No novelty, whole-paper audit or uniform growth-gap conclusion is asserted.
[G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Statement

For every integer N>=1, put r=N!, let y in (-1,0) be the real root of y^3+y+1=0, and choose any algebraic x with x^r=y.
Then x is a nonzero algebraic unit with |x|<1, is not a root of unity and has positive unnormalized logarithmic Mahler measure.
Let S_x consist of the two affine maps z->xz-1 and z->xz+1 over Qbar.
No pair of nonempty positive words in S_x, each of length at most N, generates a free semigroup on those two chosen words.
Thus no universal bounded-word free-pair construction exists in this precise positive-Mahler same-slope two-map family.
The parameter field is Qbar; no assertion that x lies in Q or R is imposed.

More explicitly, after conjugating S_x to A(z)=xz and B(z)=xz+1, any pair U,V of lengths q,p<=N either has a common fixed point and commutes, or admits a simultaneous affine conjugacy under which

    U^(4r/q)=V^(2r/p) U^(r/q) V^(r/p).

The positive integers r/q and r/p exist because q,p divide N!.
Every conjugate of x has logarithmic modulus of absolute value at most C/r, where C is the maximum of |log|y_i|| over the three roots y_i of t^3+t+1, independently of N and of the chosen radical.
This small individual-root bound is not a statement that the total Mahler measure tends to zero, and the theorem does not refute a uniform growth gap.

## Current assessment

[Selected decision](#decision-current)

## Assessment history

### Decision current

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:08 |
| status | proved |
| reason | The exact affine conjugacy, common-fixed-point branch, positive-word relation and algebraic-unit domain are completely retained and checked by the selected current agent self-review. The source attribution and growth-gap limitation remain explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every N, every selected radical above the stated y, and every bounded-length positive pair in the exact affine family; no rational/real parameter restriction or growth-gap refutation. |
| argument | [Argument](#argument) | Complete retained conjugacy, nonzero translations, exact composition and conjugate-modulus accounting below. |
| dependency | [Smy08 Kronecker interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | A nonzero algebraic integer with positive primitive measure unless it is a root of unity; the polynomial/root conventions and no new original-proof audit remain. |
| review | [Current affine obstruction finding](../audits/reviews/Yin_R_G0498_v1.md#affine-current-finding) | Whole exact registered statement and local proof, original Bre07 attribution and actual domain/cost limitations; contributor self-review. |

## Argument

The cubic changes sign on (-1,0) and has derivative 3t^2+1>0, so its specified real root exists uniquely.
The equation x^(3r)+x^r+1=0 and its reciprocal polynomial show that x and x^(-1) are algebraic integers.
For every conjugate x_i, the number x_i^r is one of the three nonzero cubic roots y_j; hence |log|x_i||<=max_j|log|y_j||/r.

Bre07, Theorem 1.7 on p.4 and Section 7, Theorem 7.2 and proof on pp.14--15, gives unbounded positive-independence diameter in metabelian polycyclic subgroups of GL_2(Qbar).
The overbar matters.
The following direct positive-word check records its applicability to the Task's S_x={z maps to xz-1, z maps to xz+1}; the source's more general signed-exponent argument is not required.

For any integer N>=1, put r=N!.
Let y in (-1,0) be the real root of y^3+y+1=0, and choose x with x^r=y.
Then x is a nonzero algebraic unit, |x|<1 and x is not a root of unity; hence m(x)>0 by Kronecker.
The affine change g(z)=z/2+1/(2(1-x)) conjugates S_x to A(z)=xz, B(z)=xz+1.

Take any two nonempty positive words U,V in A,B of lengths q,p<=N.
Their slopes are x^q,x^p, neither equal to one.
If their fixed points coincide they commute and are not free.
Otherwise a simultaneous affine conjugacy puts them in the form U(z)=x^q z, V(z)=x^p z+1.
Consequently
\[
U^{r/q}(z)=yz,\qquad V^{r/p}(z)=yz+b,\qquad
b=(1-y)/(1-x^p)\ne0.
\]
Composition is read right to left.
For C(z)=yz and D(z)=yz+b, direct multiplication yields
\[
D^2CD(z)=y^4z+b(y^3+y+1)=C^4(z).
\]
Therefore
\[
U^{4r/q}=V^{2r/p}U^{r/q}V^{r/p}.
\]
This is a nontrivial equality of distinct positive words in the proposed generators U,V.
All pairs in the positive ball of radius N fail to generate a free semigroup.
Since N was arbitrary, there is **no universal bounded-word free-pair construction even in this same-slope two-map family with positive Mahler measure**.
This excludes the initial prospective mechanism, not the uniform growth-gap target.
The source explicitly separates these questions.

It also explains a weakness of single-place ping-pong.
Every conjugate of x has logarithmic modulus bounded in absolute value by C/r, where C depends only on the three roots of t^3+t+1.
No fixed power makes a uniformly contracting/expanding conjugate.
A many-conjugate entropy argument could still succeed.
Do not infer small total entropy from these small individual logarithms: M(p(t^r))=M(p), and field-extension multiplicity matters when passing from that polynomial to a chosen irreducible factor.
