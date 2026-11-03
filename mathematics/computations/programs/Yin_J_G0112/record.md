---
author: Yin
---
# Complete reduction for the denominator-three finite screen

The source scope and contributors are stated below.
This is the complete author reduction for this J, not independent review or a general residual theorem.
Accepted inputs are [C178](../../../claims/Yin_C_G0178_v1.md#argument), [C182](../../../claims/Yin_C_G0182_v1.md#singleton-three-adic-companion), and [C184](../../../claims/Yin_C_G0184_v1.md#statement).
The reference to C182's Rolle method is expanded in the actual reduction below, so no unreviewed field-projection claim is needed.

<a id="denominator-three-reduction"></a>
## Exact low-norm reduction for denominator3 affine pairs

2026-10-20 continuation.
Root proposed b=(u/3)c+v with u,v in{-2,-1,1,2}, supplied the3-prime split and the final four representative choices, and authorized one bounded exact factorization batch after this reduction.
The entropy_attainment_bridge author checked every branch, the original norm payments and the conditional field reconstruction.
Both are contributors; the finite result will need a separate reviewer.
The following reduction concerns a putative STRICT violation of abs(Norm_F(g))>=2^([F:Q]/2).
It does not claim that every point excluded from the computation is nonexistent.

More generally assume u,v are nonzero integers prime to3 and b=(u/3)c+v.
Put b(X)=uX/3+v, Q(X)=b(X)^2+s[X^3-2b(X)^5], and

    P_(u,v,s)(X)=27Q(X)^5-8X^6 in Q[X].            (R46)

The actual c is a root, a^3=Q(c), and a=3Q(c)^2/(2c^2).
Thus H=Q(a,b,c)=Q(c).
The same two-half-line Rolle proof as in C182 applies to this rational degree5 Q: the derivative of Q(X)/abs(X)^(6/5) vanishes at the roots of the nonzero degree5 polynomial XQ'-(6/5)Q.
Every nonzero real root of P has Q>0.
There are at most seven such roots, so r_0=[H:Q]<=7.
The original norm tower makes a violation in F equivalent to a violation at the same normalized exponent in H.

At every3-prime of H use the integer-valued normalization and write e=v_p(3), A=v_p(a), B=v_p(b), C=v_p(c).
Integrality of b and the fact that u is a3-unit force C>=e.
If C=e, then f=0 gives A=e/5, so5 divides e.
If C>e, put w=b-v and W=v_p(w)=C-e=(5A-e)/2>0.
Since v is a3-unit, B=0.
The residual equation gives v_p(1-2s b^3)=3A>0.
The rational constant D_0=1-2s v^3 has rational3-valuation0 or1.
Its valuation cannot be0, because all nonconstant terms in the expansion at v have positive valuation.
Thus v_p(D_0)=e, and the remaining terms have valuations e+W,e+2W,3W.
If W<e/3, the unique minimum gives A=W; the identity2W=5A-e then gives W=e/3, a contradiction.
If W>e/3, the unique minimum gives3A=e and again W=e/3, a contradiction.
Consequently W=A=e/3, and3 divides e; the actual cancellation is required to leave valuation exactly e, not a larger one.
The full degree sum with r_0<=7 now implies

    r_0 in{3,5,6}.                                 (R47)

For r_0=3, C178 gives the stronger full2^r_0 norm bound.
For r_0=6, an index5 at2 would leave an unramified degree1 prime, forbidden by C178; every remaining index gives G>=e, again proving2^r_0.
Thus a strict violation can only have r_0=5.
C184 then restricts its norm to1 or5.
Its2-prime norm exponent is a multiple of3, and its3-prime exponent is a multiple of5; both must therefore vanish.
C178 forces the unique2-prime to have e=5,f=1.
The3-prime alternatives in(R47) likewise force a unique3-prime with e=5,f=1; there C=e,A=1 and B=0.
The residue equation gives bbar=-s, while b-v=(u/3)c is a unit there.
Since v is a3-unit, this forces

    v congruent to s mod3.                         (R48)

At2, both b and c are units.
If u and v are both odd, the residue equation becomes cbar^3+cbar^2+1=0, whose irreducible F_2 cubic forces residue degree at least3, contradicting the actual degree5.
If u and v are both even, b cannot be a2-adic unit.
For that even-even case one can also prove the stronger floor directly: in C178's low branch G<e, B=G/2<e/2, whereas b=(u/3)c+v has B>=e.
Therefore only opposite parities and(R48) need a finite search for a violation.

For the specified32 triples u,v in{-2,-1,1,2}, s in{1,-1}, exactly eight survive these necessary conditions.
The sign transformation (b,c,s,g)->(-b,-c,-s,-g) sends (u,v,s) to(u,-v,-s), preserving integrality, total reality and the absolute original norm.
It reduces them to exactly

    (u,v,s)=(1,2,-1),(-1,2,-1),(2,1,1),(-2,1,1).  (R49)

No broader parameter range is authorized by this reduction.

For each representative the computation will clear the rational denominator of(R46), retain every coefficient and the COMPLETE primitive ZZ factorization, and verify the reconstructed factor product.
Only a monic irreducible factor of degree5 with five distinct real roots can contain a violating c.
A nonmonic primitive irreducible factor has no algebraic-integer root; any other degree is outside the only remaining low-norm degree.
For a surviving factor f, b=(u/3)c+v must be separately checked integral: c integral alone is insufficient for this rational affine relation.
Because u!=0, its exact minimal polynomial is (u/3)^5 f(3(Y-v)/u); monic rational coefficients are integral precisely when they are rational integers.
After this check, Q(c) is integral and the reconstruction a=3Q(c)^2/(2c^2), together with a^3=Q(c), proves a integral.
The program must verify every original equation, nonzero a,b,c,g, and the exact full degree5 field norm of g.
The final comparison is Norm_H(g)^2<2^5, with no smaller quotient field or discarded denominator.
Any larger ambient field raises both sides by the same extension-degree factor.

The authorized first batch is exactly these four cases, at most15 seconds per case and60 seconds total, with no retry or automatic enlargement after a mathematical timeout.
A negative complete result would exclude violations only in the original32-case family, including its analytically covered and sign-equivalent members.
It would not resolve arbitrary rational affine coefficients or the unrestricted residual singleton.
