---
author: Yin
---
# Inverse additive structure: exact integer carry and conditional entropy costs

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This 2026-11-05 continuation tests the explicit integer lift left unresolved by [L447 v1](Yin_L_G0447_v1.md#original-binary-input-to-inverse-addition).
That earlier version retains the inverse-theorem source comparison and the whole-block expansion budgets at their actual scope.
The present version retains the separate original power-basis carry test; it supplies no uniform arithmetic gain or new independent proof review.
The exact carry representation and cycle equation below expose the original unresolved conditional information rather than estimate it away.

<a id="power-basis-carry-cocycle-test"></a>
## The actual power-basis carry cocycle preserves the unresolved information

Contributor plan_entropy prepared this bounded 2026-11-05 test for Yin, at author-checking scope.
The inspected [C530 carry innovation argument](../claims/Yin_C_G0530_v1.md#predictable-iid-carry-innovation-mask) already exhibits exactly half a bit of fresh local carry information while its [endpoint identity](../claims/Yin_C_G0530_v1.md#parity-carry-exact-endpoint-information) preserves every original endpoint entropy rate, with the explicit boundary cost 2d log2.
That construction filters a two-sided bit process by P; the state-section cocycle below is a different representation and does not inherit independence of its carries.
[C556's exact integer-fiber formula](../claims/Yin_C_G0556_v2.md#exact-mask-kernel-height-one-enumerator) already identifies genuine height-one integral lifts, with their actual probabilities, as information absent from binary rank alone.
The present test does not replace that arithmetic count or supply its missing input-uniform estimate.

Fix an actual algebraic unit alpha with monic irreducible P(t)=t^d+sum_(j=0)^(d-1)a_j t^j and a_0 in{-1,1}.
Identify O=Z[alpha] with Z^d in the power basis, let M be multiplication by alpha, and let s(r) be the binary-coordinate section of r in F_2^d.
For independent fair bits use X_0=0 and X_(n+1)=alpha X_n+epsilon_n; reversing the independent bits identifies its endpoint law with the original binary law in [C283](../claims/Yin_C_G0283_v1.md#binary-increment-js-divergence).
Write uniquely X_n=s(r_n)+2Y_n, with Y_n in O, and use natural entropies H_n=H(X_n), Delta_(n+1)=H_(n+1)-H_n.
The exact update is

    r'=M r+epsilon e_0 mod2,
    Y'=M Y+kappa(r,epsilon),
    2kappa(r,epsilon)=M s(r)+epsilon e_0-s(r').       (PC1)

Here e_0 is the constant-coordinate vector, and the residues in s are always 0 or1, including for negative pre-remainders.
Put b=r_(d-1), z_0=epsilon-a_0 b, and z_j=r_(j-1)-a_j b for1<=j<d.
Then r'_j=z_j mod2 in{0,1} and kappa_j=floor(z_j/2).
For b=0 all coordinates of kappa vanish.
For b=1 and a_j=2c_j+e_j with e_j in{0,1}, the higher coordinates are kappa_j=-c_j-e_j(1-r_(j-1)); the constant coordinate is -(1-epsilon) when a_0=1 and epsilon when a_0=-1.
These formulas retain the actual integer coefficients rather than just their reductions.

For n>=d, r_n is exactly uniform on all 2^d residues: the last d independent bits form a power-basis block, and the preceding state contributes a translation modulo2.
Since M mod2 is invertible, epsilon_n is also independent of r_(n+1).
Consequently the local carry innovation is exactly H(kappa(r_n,epsilon_n)|r_n)=(log2)/2.
It is not the entropy increase of Y_n or its algebraic endpoint.
Define C_n=H(Y_n|r_n)=H_n-d log2 for n>=d.
For each realized epsilon_n the map X_n to X_(n+1) is bijective on O, so

    Delta_(n+1)=log2-H(epsilon_n|X_(n+1))
       =I(epsilon_n;Y_(n+1)|r_(n+1))
       =C_(n+1)-C_n.                                (PC2)

For an explicit version let nu_(n,r)=law(Y_n|r_n=r), and, for e in{0,1}, set r_e=M^(-1)(r'-e e_0) mod2 and lambda_(r',e)=tau_(kappa(r_e,e)) M_*nu_(n,r_e).
The two branches have equal conditional probability given r', and hence

    Delta_(n+1)=2^(-d) sum_(r' in F_2^d)
                     JS(lambda_(r',0),lambda_(r',1)). (PC3)

This is exactly the original binary Jensen--Shannon increment in residue coordinates; small original Delta makes the average branch separation small despite the half-bit local innovation.
No independence between Y_n and r_n, or between Y_n and kappa, is available from PC1.

The residue chain has an exact d-step uniform transition kernel, because its d new bits give every power-basis residue exactly once from each starting residue.
It is therefore already aperiodic; a separate permutation period of M mod2 is not a new mixing resource.
For n>=d the pair of residues at times n and n+d is uniform on 2^(2d) pairs.
Writing the d-bit block as s(U), with U uniform on F_2^d, gives X_(n+d)=M^d X_n+s(U), and the same argument yields

    H_(n+d)-H_n=I(U;Y_(n+d)|r_(n+d))
              =sum_(j=1)^d Delta_(n+j).              (PC4)

Here U is independent of the final residue because the initial residue is uniform and M is invertible; conditional on that final residue the 2^d branches still carry their weights 2^(-d).
Thus blocking keeps all 2^d states and all 2^(2d) starting/ending residue pairs, rather than making the conditional integer laws uniform.
When all these increments are at most delta, PC4 is at most d delta; division by d changes only the normalization, not the unresolved endpoint separation.

For any prescribed L-bit path from r_0 to r_L, put B_L=sum_(i=0)^(L-1) M^(L-1-i)epsilon_i e_0 and K_L=sum_(i=0)^(L-1) M^(L-1-i)kappa(r_i,epsilon_i).
Telescoping PC1 gives the full integral compatibility condition

    2K_L=M^L s(r_0)+B_L-s(r_L).                     (PC5)

For a residue cycle this becomes 2K_L=(M^L-I)s(r_0)+B_L, not K_L=0.
Requiring the full integer state to close adds (M^L-I)(s(r_0)+2Y_0)+B_L=0, exactly the original affine periodic-path equation.
At a time with uniform initial residue, one specified initial residue and one specified L-bit word have mass 2^(-d-L).
For L>=d, the event r_L=r_0 with the initial residue unrestricted has mass exactly2^(-d), and specifying that residue as well costs another factor2^(-d).
These statements concern residue paths only; imposing a full integer-state return can reduce the mass further.
Cycles cannot be selected without their elapsed time L and these original word and residue probabilities.

The actual torsion control alpha=-1, P=t+1, already satisfies PC1--PC5 and has the same local half-bit carry innovation, while its endpoint has at most n+1 values and H_n/n tends to0.
This checks the invalid inference from local carry noise and integral cycle compatibility to positive endpoint growth; it is not a nontorsion near-one input or a counterexample on the C231 endpoints.
For those endpoints, an additional arithmetic statement would have to control the actual conditional laws nu_(n,r), for example uniformly positive branch separation on a uniformly positive fraction of all residues at all sufficiently large times.
Such constants would pass through PC3 to a uniform positive h_1 and hence to a Mahler gap; PC1 and PC5 supply no such estimate.
The tested state-section implementation therefore stops here as an exact rewriting of the original law, with the lost conditional information and all state, cycle, mass and time costs exposed.
No impossibility of a stronger arithmetic carry argument is asserted.
