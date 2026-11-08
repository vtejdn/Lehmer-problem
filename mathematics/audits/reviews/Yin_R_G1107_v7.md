---
author: Yin
---

# Independent review of the two-moment chamber at conductor 6561

<a id="whole-6561"></a>
## Finding on the fixed norm and the complete lift

At 2026-11-08T07:04 UTC a separately assigned agent reviewed the [statement](../../claims/Yin_C_G0882_v2.md#statement), the [argument](../../claims/Yin_C_G0882_v2.md#argument) and the complete supporting derivation in L464 v13 for Yin.
The reviewer took no part in their development, inspected the fixed proof and its cited mathematical inputs, and received no proof-generation dialogue, author explanation or prior verdict on these fixed inputs.

I recomputed the sign variations in the odd-grid recurrence at both \(-151157/100000\) and \(-68/45\).
Each count was 2534, both final signs were positive, and \(p|B(-68/45)|>2\).
Since \(|B(-2)|=1\), the partial fractions at \(-2\) give \(P(-1)=U\in\mathbb Z\).
Strict positivity and the upper bound \(U<39/22\) force \(U=1\), and the positive product bound for \(W\) gives \(N<947/90\).
Integrality of \(N\) follows from the expansion of the integer rational function \(C/B\) at infinity with \(B\) monic.
The cubic has discriminant \(-107\) and opposite strict signs at the two separators, so every factor \((2-b)H(b)h(b)\) is positive.

On each primitive layer the residue ring modulo two is a field because doubling traverses the primitive indices up to sign.
Dividing the integral representative by its coefficient content at two leaves odd absolute norm, which is one because the full norm is a power of two.
The primitive-root sums of \(T_i\) are multiples of \(d\), giving the required integrality of the normalized trace.
I computed the layer resultants as determinants of multiplication by \(1+T_d\) on the basis \(1,t,t^2\) modulo \(H\).
The absolute values start with \(4,17,1297,1669767859\), and the eight bit lengths are \(3,5,11,31,92,280,831,2507\).
Each layer therefore contributes normalized trace at least three by the positive arithmetic-geometric mean bound and integrality.
The recursion for \(m_i\) gives \(Z=N-5\), and \(\sum d\,t_\ell=1502\) yields \(Z\ge1594/729>2\).
This checks \(N\in\{8,9,10\}\) for every integral \(h\) in the stated chamber.
I also checked the auxiliary exclusion of \(N=6\) for any nonzero resultant in this profile, including \(|B(\sqrt2)|=1\) by the sine formula and the strict comparison \((452-316\sqrt2)/45<1/2\).

Expanding \(\log(Q/(tB))\) through order four gives trace differences \((-2,-2,-2,18-4N)\) for \(t,t^2,t^3,t^4\).
There are \(n-2\) same-sign gaps and one open interval from \(-2\) to the smallest pole with a forced root.
Pairing each of these \(n-1\) distinct roots with its right pole omits only \(b_*\), and their disjoint intervals bound the total matched difference by the negative variation.
Evaluation at the three critical points and both endpoints reproduced \(V_-=2953/768\), \(\max_{\mathbb R}f=387/256\) and \(B_8-2\max f=1215894119/1049760000\).
Since \(y<b_*<-1\), the pairing gives a strict excess over the sum possible for two real roots, including repeated real roots.
The remaining two roots are conjugate by reality of \(Q\) and exhaust its degree \(n+1\).

I independently formed each rational polynomial \(B_N-2g_R\) and its signed Euclidean remainder chain.
Both endpoint variation counts were two in all three cases, the endpoint values were nonzero, and evaluation at zero was positive.
Harmonicity gives the same upper bound for \(\operatorname{Re}f\) throughout the filled ellipse, while conjugacy gives equal real parts at the two exceptional roots.
For \(\rho>1\) the trace ellipse has semiaxes \(\rho+\rho^{-1}\) and \(\rho-\rho^{-1}\), both strictly increasing.
Each exceptional trace therefore has exterior lift radius greater than its tested \(R\).
All \(n-1\) matched traces lift to unit-circle pairs, so the two exterior radii give exactly \(M(P)=\rho^2\).
This proves the three strict bounds \(2209/1600,\ 16/9,\ 49/25\) as stated.
The review establishes the conditional assertion at this fixed conductor and norm.
Existence of an input satisfying the moments and behavior along growing conductors remain open here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole fixed chamber](#whole-6561) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole fixed chamber](#whole-6561) | [C882 v2 statement](../../claims/Yin_C_G0882_v2.md#statement) | Complete hypotheses, endpoint equality, third-moment set, root counts and all three whole-measure bounds. |
| [Whole fixed chamber](#whole-6561) | [C882 v2 argument](../../claims/Yin_C_G0882_v2.md#argument) | Full implication from prescribed signs, norm and moments through the ellipse estimates. |
| [Whole fixed chamber](#whole-6561) | [L464 v13 layer argument](../../ledger/Yin_L_G0464_v13.md#cubic-layer-traces) | Endpoint, integrality, full eight-layer norm calculation and auxiliary square-root exclusion. |
| [Whole fixed chamber](#whole-6561) | [L464 v13 exterior argument](../../ledger/Yin_L_G0464_v13.md#ellipse-quartic) | Disjoint matching, multiplicities, quartic variation, rational Sturm checks and the complete lift. |
