---
author: Yin
---

# Trace-factor inertia, exact common exponents, and a squareclass-only stop

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded arithmetic candidate screen written by assigned AI `growth_arithmetic_status` for Yin.
The coordinator selected the question of actual trace reduction and asked for a forcing mechanism or a precise stop.
This AI derived the factor classification and checks below.
Complete independent review and fixed-ledger adoption are recorded below.
No external search, numerical run or new prime scan was performed for this argument.

The fixed interfaces reused are the trace construction and signed discriminant identity in [L66](Yin_L_G0066_v1.md#reciprocal-trace-domain), the actual good-prime root-count/norm accounting in [L74](Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail), and the distinction between inversion-orbit existence and true mass in [L152](Yin_L_G0152_v1.md#primitive-inversion-orbits).
[L159](Yin_L_G0159_v1.md#good-prime-short-order-capacity) already separates finite-field capacity from actual low-Mahler coverage.
[L160](Yin_L_G0160_v1.md#inversion-matched-frobenius-return) provides the previously fixed inversion-matched return mechanism.
The present screen neither replaces its least-prime obligation nor proves a new near-one coverage theorem.

<a id="trace-factor-common-exponent"></a>
## 1. Exact classification at a good odd prime

Let P be monic, irreducible, reciprocal and noncyclotomic in Z[t], with degree d=2s, constant coefficient one, and positive logarithmic Mahler measure m.
Write

    P(t)=t^s T(t+t^(-1)),       T in Z[x] monic, deg T=s.

Take an odd prime p not dividing disc(P).
L66 gives

    disc(P)=disc(T)^2 T(2)T(-2).                           (1)

Thus T modulo p is squarefree and neither 2 nor -2 is a root.
Factor it into distinct monic irreducibles Q_j of degrees f_j.
For a root z_j of Q_j in F_(p^f_j), set

    epsilon_j=chi_(p^f_j)(z_j^2-4) in {1,-1}.              (2)

This does not depend on the chosen conjugate of z_j.

If epsilon_j=1, the roots of t^2-z_j t+1 lie in F_(p^f_j).
Each has degree exactly f_j: its trace generates F_(p^f_j), while the root belongs to that field.
They lie in two distinct Frobenius orbits.
Indeed, an equality alpha^(p^a)=alpha^(-1) would imply z_j^(p^a)=z_j and hence f_j divides a; the equality would then give alpha=alpha^(-1), contrary to z_j not being 2 or -2.
This trace factor therefore gives two reciprocal factors of P, each of degree f_j, and both root orders divide p^f_j-1.

If epsilon_j=-1, that quadratic is irreducible over F_(p^f_j).
Its root has degree exactly 2f_j over F_p and

    alpha^(p^f_j)=alpha^(-1).

It gives one self-reciprocal factor of P of degree 2f_j, whose root order divides p^f_j+1.
This is a classification of the actual reduction of P, with no global Frobenius-class hypothesis.

For every integer H>=1, let k_p(n) be the number of roots of P modulo p satisfying alpha^n=1, counted as in L74.
Then

    k_p(p^H+1)
      =2 sum_(epsilon_j=-1, f_j|H, H/f_j odd) f_j.         (3)

To prove the converse as well as the forward implication, a return alpha^(p^H)=alpha^(-1) forces the trace z_j to be fixed by Frobenius^H, and hence f_j divides H.
A split quadratic then cannot return, since Frobenius^H is the identity on its roots and alpha is not its own inverse.
On an inert quadratic, Frobenius^f_j is inversion, so Frobenius^H is inversion exactly when H/f_j is odd.
This proves (3), including possible actual orders smaller than p^f_j+1.

In particular, if b_1 is the number of inert linear factors of T,

    k_p(p+1)=2b_1,
    v_p(|Norm(alpha^(p+1)-1)|)>=2b_1,
    m>=[2b_1 log p-d log 2]/(p+1).                       (4)

For general H, replace 2b_1 by the right side of (3) and p+1 by p^H+1.
Distinct factors are disjoint root sets, so the accounting does not count any ideal twice.
These are first-layer lower bounds, not upper bounds on actual initial valuations or true norm mass.
Bad or ramified polynomial reductions are outside this proof.

<a id="trace-discriminant-parity-only"></a>
## 2. What the relative discriminant norm does and does not force

For any a in F_(p^f)^*, the finite-field definitions give

    chi_(p^f)(a)=chi_p(Norm_(F_(p^f)/F_p)(a)).

Multiplying this identity over the factors of T proves

    product_j epsilon_j=chi_p(T(2)T(-2)).                 (5)

Indeed, the product of the conjugate values z_j^2-4 equals T(2)T(-2).
Thus a nonsquare right side forces an odd, and hence nonzero, number of inert trace factors.
This is an unweighted count of factors: neither their degrees nor their inclusion in the sum in (3) is determined by (5).

In particular, (5) does not force an inert linear factor.
If the only known inert trace degree is f, its guaranteed return exponent is p^f+1, not p+1.
Combining several known inert factors by (3) requires their degrees to divide a common H with odd quotients; even if such H is available, its cost is p^H+1.
This screen makes no assertion that every formally allowed factor pattern occurs on an actual irreducible low-Mahler input.

There is an elementary finite-field diagnostic even when every trace factor is linear.
Among z in F_p other than 2 and -2, exactly (p-3)/2 have chi_p(z^2-4)=1 and exactly (p-1)/2 have chi_p(z^2-4)=-1.
To see this, the number of pairs (z,y) satisfying y^2=z^2-4 is p-1: the substitution

    a=z-y,     b=z+y,     ab=4

is a bijection with nonzero choices of a, because 2 is invertible.
On the other hand the count is p+sum_z chi_p(z^2-4).
The character sum is therefore -1; subtracting the two excluded zero-character values proves the claimed counts.

Consequently, if T splits completely modulo p, its number b of inert factors satisfies exactly the elementary capacity bounds

    max(0,s-(p-3)/2)<=b<=min(s,(p-1)/2).                 (6)

The lower bound can be useful only with the additional strong arithmetic premise of complete trace splitting at a suitably small good prime.
No such coverage premise is proved here.
When p>=2s+1 one can choose s-1 distinct split trace values and one inert trace value, obtaining a monic squarefree split polynomial of degree s, avoiding 2 and -2, with nonsquare T(2)T(-2) and b=1.
This is a finite-field countermodel to a stronger implication from the squareclass alone, not an irreducible integer lift, a near-one family, or a counterexample to the Task.

<a id="lehmer-trace-squareclass-control"></a>
## 3. One retained actual input and the stopping decision

The retained Lehmer polynomial has degree ten and

    P(1)=-1,       P(-1)=1,

as checked in [L79](Yin_L_G0079_v1.md).
Since s=5, its trace polynomial has

    T(2)=-1,       T(-2)=-1,       T(2)T(-2)=1.           (7)

Thus at every odd good prime, (5) says that the number of inert trace factors is even.
It supplies no nonzero lower count at any such prime.
This does not say that there are no inert factors or that the actual norm mass is zero.
The retained input has fixed positive measure; it is not a family tending to one and does not refute coverage on a smaller near-one domain.

Stop the proposed relative-discriminant-squareclass forcing route at this point.
The norm-one relation and (5) do not fill the degree-weighted sum in (3), while (6) is capacity conditional on unproved small-prime splitting.
Higher residue degrees can increase mass but cost p^H+1 and require genuine degree alignment.
This is not repaired by retaining an unweighted parity or by replacing the matching condition with cycle type.

The next admissible arithmetic input must control actual inert trace factors of aligned degrees at a prime with a proved exponent budget, or provide separate actual valuation surplus.
No such input is selected by this bounded test.
The general direct norm criterion, extra actual depths, and L160's matched-return interface remain open for a different forcing mechanism.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0060_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
