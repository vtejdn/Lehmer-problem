---
author: Yin
---

# Minimal-Frobenius local rigidity and bounded-residue mass exclusion near one

Date: 2026-10-10.

<a id="local-rigidity-near-one-mass-fixed-scope"></a>
## Adopted scope

The coordinator for Yin retains resultant_research's complete new proof and the coordinator's separate complete noncontributor review.
Earlier dependency contributions are disclosed.
The source-completeness review supplies the precise existing The26b/Tag00PD attribution for the classical DVR characterization, using its already retained chapter; the local argument itself is complete and acquires no new external proof dependency.

Under minimal p-adic Frobenius-resultant valuation d, the actual power-basis order is the maximal completed order at p, including repeated reduction.
Reduced multiplicities and degrees are exactly local ramification and residue degrees.
Every full invariant lattice is locally conjugate at all p-power levels.
The complete later valuation profile, cyclic/cyclotomic norms and additive primary groups are explicit, with at most one undetermined tie transition per local factor.

Separately, without any saturation, ramification or index hypothesis, a positive degree fraction gamma in mod-p factors of degree at most F forces

    m(P)>=gamma log2/[N_(p,F) p^(ceil(1/gamma)+1)],
    N_(p,F)=lcm_(1<=f<=F)(p^f-1).

This is an explicitly credited varying-ramification specialization of the fixed L72 lift, retaining the full same-exponent and d log2 costs.
Every hypothetical total-measure-to-zero sequence must therefore lose all such bounded-residue-degree mass for each fixed p,F.
These are genuine varying-input conclusions, not only fixed-base controls.

The proof supplies no near-one saturation coverage, bound on growing residue degrees or the exceptional tie depth, or control of archimedean inverse/full-cofactor costs.
G0001 remains active and unresolved.
The complete original author argument and review follow; historical pending-review wording preserves chronology.
Only heading depth and relative navigation are transformed.

<a id="retained-local-rigidity-proof"></a>
## Minimal Frobenius valuation and varying-input cyclic coverage

Date: 2026-10-10.
Starting question: Develop the next arithmetic mechanism beyond fixed-base prime-power lifts in L202.
Use its actual-order quotient and irreducibility structure to test a precise varying-input near-one constraint, useful exponent selection or multi-prime interaction, with full costs and genuine input coverage.
Screen existing L arithmetic before choosing a changed question; do not repeat the fixed-base income computation.

The unrestricted Task remains active and unresolved.


### Reuse screen and changed result

The screen read [L202](Yin_L_G0202_v1.md#minimal-frobenius-fixed-scope), [L63](Yin_L_G0063_v1.md), [L64's elementary complete local algebra](Yin_L_G0064_v1.md#direct-etale-frobenius-lift), [L70's lattice and conductor comparison](Yin_L_G0070_v1.md#local-conductor-period-bound), [L72's ramified cyclic-norm lift](Yin_L_G0072_v1.md#ramified-valuation-capture), [L74's full local table](Yin_L_G0074_v1.md#finite-exact-local-cyclic-table), [L78's cyclotomic layers](Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers), L159's short-order capacity, [L168's actual cost](Yin_L_G0168_v1.md#general-unit-finite-income-criterion), and L188's aggregate-normalization obstructions.
L68/L73 were inspected for the bounded-residue and local-field comparison.
No new computational scan was needed.

The changed structure is that L202's minimal Frobenius hypothesis makes the actual power-basis order maximal at that prime, even with arbitrary repeated reduction.
It determines the actual ramification, removes every local lattice shortcut, and reduces the complete later valuation profile to a deterministic recurrence with at most one potentially exceptional transition per local factor.
This extends the earlier L64 unramified algebra; it is not a restatement that a squarefree power-basis order is maximal.

A separate all-input consequence uses the old L72 lift with ramification allowance E=d and unpowered exponent1.
It gives an explicit measure lower bound whenever a positive fraction of the original degree is concentrated in bounded-degree reduction factors.
Thus high ramification or an order-index defect cannot hide that fraction in a hypothetical total-measure-to-zero sequence.
This is a new recorded varying-input corollary of the displayed old estimate, not a claim to have invented the binomial lift or a general local-field height theorem.
Its proof does not assume minimal Frobenius valuation.
The first theorem has restricted coverage; the second necessary near-one condition holds for all nontorsion units.
Neither supplies unrestricted positive income coverage.

<a id="minimal-frobenius-maximal-order"></a>
### 1. The minimal Frobenius condition forces the actual maximal local order

Let alpha be a nontorsion algebraic unit with monic irreducible P in Z[t] of actual degree d.
Let O=Z[alpha], K=Q(alpha), and fix a prime p for which

    v_p Res(P,P^[p])=d.                                      (1)

Every powered polynomial retains all original conjugate multiplicities.
Factor

    Pbar=product_phi phi^(e_phi) in F_p[t],
    f_phi=deg phi,
    r_phi=the multiplicative order of a root of phi.

The factors phi are distinct and monic; r_phi is prime to p because P has unit constant term.
Put n=lcm_phi r_phi and z=alpha^n-1.
L202 gives the entire finite quotient

    (O/zO)_(p)=product_phi F_(p^f_phi).                       (2)

In particular it is reduced and killed by p.
We claim

    O tensor Z_p = O_K tensor Z_p,
    p does not divide [O_K:O],                              (3)

and there is exactly one local field factor for each phi, with residue degree f_phi, ramification index e_phi, and alpha^(r_phi)-1 a uniformizer in that factor.
The multiplicities e_phi are therefore actual ramification here, not power-basis index artifacts.

Here are the complete local steps.
Write S=O tensor Z_p, a finite free, complete Z_p-algebra.
The residue decomposition

    S/pS=product_phi F_p[t]/phi^(e_phi)

lifts to S=product_phi S_phi.
For completeness, lift each idempotent using the polynomial X^2-X: its derivative2X-1 is a unit at an idempotent, and Newton correction squares the error ideal.
Completeness gives a unique lift with that residue.
Products of the lifts and their sum are the uniquely lifted zero and one idempotents, proving the decomposition.
This is the same elementary idempotent mechanism as L64, now applied to local Artinian residue factors rather than only fields.
An element of S_phi is a unit precisely when its image in F_p[t]/phi is nonzero: first invert it modulo p in the local ring F_p[t]/phi^e, then lift that inverse by a convergent geometric series.
Thus S_phi is local.

Tensoring(2) with Z_p gives S_phi/zS_phi=F_(p^f_phi).
Hence the maximal ideal of S_phi is precisely zS_phi.
Multiplication by z is injective: in S[1/p]=K tensor Q_p it is invertible, since none of the original conjugates of alpha is a root of unity, and S is Z_p-torsion-free.
Also z modulo p is nilpotent, since every r_phi divides n.
If E=max_phi e_phi, then z^E lies in pS.
Consequently

    intersection_(a>=0) z^a S_phi = 0.                       (4)

Every nonzero x in S_phi can therefore be divided by z until the quotient is a unit, after a finite number of steps.
Thus x=z^a u for a uniquely determined a>=0 and a unit u.
Uniqueness follows from injectivity of multiplication by z and the fact that z is not a unit.
Products of nonzero elements stay nonzero, so S_phi is a domain.
Since p belongs to its maximal ideal, the same argument writes

    p=z^b v,              b>=1, v a unit.

The successive quotients z^a S_phi/z^(a+1) S_phi are all its residue field.
Counting the F_p-dimension of S_phi/pS_phi gives b f_phi=e_phi f_phi; hence b=e_phi.
In particular S_phi[1/p] is its fraction field, of Q_p-degree e_phi f_phi, and every nonzero fraction has a unique integer z-valuation.
If a fraction has negative valuation, a monic integral equation over Z_p is impossible: its highest power has uniquely smallest valuation.
Conversely all elements of S_phi are integral over Z_p because S_phi is finite over Z_p.
It is therefore the full valuation ring of this local field, with uniformizer z, residue degree f_phi and ramification e_phi.
These direct facts are the usual discrete-valuation-ring characterization; no additional local normality theorem is assumed.

Each element of O_K is integral over Z_p in every component and thus belongs to S.
Since O_K/O is a finite group, as recalled in L70, its p-primary part is zero.
This proves(3) and equality of the completed orders.
Finally n/r_phi is prime to p, and

    alpha^n-1=(alpha^(r_phi)-1)
                 [1+alpha^(r_phi)+...+alpha^((n/r_phi-1)r_phi)].

The bracket reduces to n/r_phi in the residue field and is a unit.
Hence alpha^(r_phi)-1 is itself a uniformizer of S_phi.
The proof uses repeated reduction throughout and neither assumes nor proves a bound on e_phi or f_phi.

<a id="minimal-frobenius-all-level-lattice-rigidity"></a>
### 2. No local change of invariant lattice improves any finite level

Let L be any full Z-lattice in K with alpha L contained in L.
The unit norm makes alpha L=L.
Then L_p=L tensor Z_p is a full S-module inside K tensor Q_p.
Each component L_phi is a finitely generated fractional S_phi-ideal.
Taking a nonzero generator of least z-valuation shows directly that

    L_phi=u_phi S_phi,             u_phi in S_phi[1/p]^*.

Thus L_p=u S for a componentwise nonzero u.
Multiplication by u gives a Z_p-module isomorphism S to L_p commuting with alpha.
Consequently the integral multiplication matrices for alpha on O and on L are conjugate over GL_d(Z_p), and remain conjugate after reduction modulo p^a for every a>=1.
This is stronger than equality of just one mod-p scalar period; it is not a claim of integral GL_d(Z) conjugacy or a simultaneous conjugacy at other primes.

For example, with u_0=lcm_phi r_phi and e_max=max_phi e_phi, the common mod-p identity period is exactly

    u_0 p^ceil(log_p e_max).                                (5)

The meaning of the ceiling is the least nonnegative k with p^k>=e_max.
To check(5), on each primary companion factor t^n-1 vanishes exactly when its prime-to-p exponent contains r_phi and its p-power multiplicity is at least e_phi.
The same answer holds on every invariant lattice by the established conjugacy.
The projective scalar period likewise remains the L70 value n_p p^ceil(log_p e_max), with its explicitly defined semisimple projective period n_p.
In particular the earlier conductor-based potential improvement is unavailable under(1), even if p ramifies severely.
No small upper bound on u_0 or n_p is supplied.

<a id="minimal-frobenius-complete-valuation-profile"></a>
### 3. Every later layer has at most one exceptional transition

Normalize the discrete valuation ord_phi of S_phi by ord_phi(alpha^(r_phi)-1)=1, so ord_phi(p)=e_phi.
Define the finite positive integers

    t_(phi,s)=ord_phi(alpha^(r_phi p^s)-1),       s>=0.

Nontorsion makes every argument nonzero, and Section1 gives t_(phi,0)=1.
The binomial expansion, now with the exact initial value and actual ramification known, gives

    t_(phi,s+1)=min(p t_(phi,s),e_phi+t_(phi,s))
                       if (p-1)t_(phi,s)!=e_phi;            (6)
    t_(phi,s+1)>=p t_(phi,s)
                       if (p-1)t_(phi,s)=e_phi.

For1<=j<=p-1, the coefficient binomial(p,j) has ord_phi equal to e_phi.
Among those terms the linear term has uniquely least valuation e_phi+t; the last term has valuation pt.
Thus a unique lowest term gives equality except in the displayed tie.
This includes p=2.
Once t>e_phi/(p-1), every subsequent step adds exactly e_phi.
Before this threshold every step multiplies t by p.
Hence a tie can occur only if

    e_phi=(p-1)p^a for an integer a>=0,                     (7)

in which case it occurs exactly at s=a.
There is at most one uncertain transition: the single value t_(phi,a+1)>=p^(a+1).
All following values are that value plus successive multiples of e_phi.
When(7) fails, the entire profile is forced by p and e_phi alone.
The exceptional value is not asserted uniformly bounded; the result does not delete a possible local cancellation surplus.

For every u>=1 prime to p, a prime-to-p cofactor preserves a positive valuation by the same unit-sum argument used in Section1.
Therefore the complete cyclic norm satisfies

    v_p |Norm(alpha^(u p^s)-1)|
        =sum_(r_phi divides u) f_phi t_(phi,s).             (8)

No extra factor e_phi belongs in(8): each uniformizer step has additive index p^f_phi, and the ramification is already in t_(phi,s).
The complete cyclotomic layers are correspondingly

    v_p |Norm Phi_u(alpha)|=sum_(r_phi=u) f_phi,
    v_p |Norm Phi_(u p^s)(alpha)|
       =sum_(r_phi=u) f_phi(t_(phi,s)-t_(phi,s-1)), s>=1.    (9)

These follow from exact cyclotomic inversion as in L78, not from a primitive-prime heuristic.
They include all local fields, ramification and complete root multiplicities.
They refine L74's finite initial table under the added hypothesis(1); outside that hypothesis the earlier general table remains necessary.

Even the full p-primary additive group can be read from these same data.
The active component of O/(alpha^(u p^s)-1)O is S_phi/(pi_phi^t), with t=t_(phi,s) and pi_phi any uniformizer.
If t=a e_phi+b with0<=b<e_phi, its additive group is

    (Z/p^(a+1) Z)^(b f_phi)
        direct-sum (Z/p^a Z)^((e_phi-b)f_phi).              (10)

An exponent zero contributes the zero group.
Indeed the quotient modulo p^j has cardinality p^(f_phi min(t,j e_phi)), since p is a unit times pi_phi^e_phi.
These cardinalities determine the elementary divisors and give exactly(10).
The components with r_phi not dividing u contribute zero.
This is an additive-group description, not a canonical ring isomorphism with a product of these cyclic groups.
Other rational prime parts remain uncontrolled.

<a id="bounded-residue-mass-near-one-escape"></a>
### 4. An all-input varying-degree constraint, with the whole exponent cost

Now remove hypothesis(1).
Let P be any monic irreducible nontorsion unit polynomial of degree d, and m=log M(P)>0.
Fix a rational prime p and an integer F>=1.
In the complete reduction Pbar=product phi^(e_phi), put

    W_(p,F)(P)=sum_(deg phi<=F) e_phi deg phi,
    gamma=W_(p,F)(P)/d,
    N_(p,F)=lcm_(1<=f<=F)(p^f-1).                           (11)

Here e_phi are only polynomial multiplicities; without(1) they are not called actual local ramification.
Suppose W_(p,F)>0.
Then the following explicit all-degree inequality holds:

    m >= gamma log2 / [N_(p,F) p^(ceil(1/gamma)+1)].         (12)

To prove it, label all d original roots in a finite p-adic splitting field, with normalized v(p)=1.
Exactly W_(p,F) root indices, counted with multiplicity, reduce to roots of the selected factors.
Their reduced orders divide N_(p,F), so v(alpha_i^N-1)>0.
Each individual root generates a local field of degree at most d, hence ramification at most d, and its positive normalized valuation is at least1/d.
This is the individual-field guard from L74; the common splitting field is not claimed to have ramification at most d.

Set k=min{j>=0:p^j>=d} and R=ceil(1/gamma).
The reused elementary inequality

    v(x^p-1)>=min(p v(x-1),1+v(x-1))

first raises these selected valuations to at least one after k steps, and then to at least R+1 after R additional steps.
At the single exponent L=N_(p,F) p^(k+R), all other roots still have nonnegative valuation.
Thus

    log C_L >= gamma d(R+1)log p,
    log C_L <= d log2+L m,
    L <= N_(p,F) p^(R+1)d.                                 (13)

The last estimate also covers d=1.
Since gamma R>=1 and log p>=log2, subtracting the two norm bounds gives a numerator at least gamma d log2.
This proves(12).
Every contribution is at the same exponent; no raw aggregate, discarded cyclotomic factor, powered-degree preservation or loss of field norm multiplicity is involved.

Equivalently, for fixed p,F and 0<delta<=1, all inputs satisfying W_(p,F)>=delta d have the uniform bound

    m >= delta log2 / [N_(p,F) p^(ceil(1/delta)+1)].         (14)

To obtain this directly one may select a fraction at least delta and use R=ceil(1/delta); it need not rely on monotonicity across ceilings.
Consequently, on any hypothetical sequence of nontorsion units with total m tending to zero,

    W_(p,F)(P)/deg P ->0   for every fixed p and F.          (15)

This is a degree-weighted statement about the full reduction, including repeated factors and bad index primes.
In the minimal-Frobenius class, Section1 identifies the same weights with the actual local degrees e_phi f_phi.
Thus arbitrarily high ramification cannot leave a positive fraction of degree in bounded-residue-degree fields along such a near-one sequence.
Neither the existence of that sequence nor its satisfaction of(1) is asserted.
The bound depends on p,F and delta, and gives no uniform restriction when those quantities vary without control.

### 5. Mathematical income and remaining coverage

The complete new structural deductions are(3), all-level lattice conjugacy, and(6)-(10) from L202's already exact initial quotient.
Formula(12) is the separately derived unpowered varying-ramification corollary of L72/L74.
It supplies an actual near-one exclusion at the stated local concentration, with exponent and amplification costs shown.
It is valid on varying polynomials, not merely radical lifts of one fixed base.
No external source theorem or new computation is required; the elementary complete-ring argument reuses the lifting method written in L64, and the usual discrete valuation characterization is proved at the precise needed scope above.
No historical novelty is claimed for that characterization, binomial valuation rules or Kronecker/height background.

The direction changes in two ways.
A minimal-Frobenius input cannot hide a cheaper finite-level matrix period in a larger order or different invariant lattice.
Its remaining local uncertainty is confined to actual residue orders, ramification multiplicities and at most one tie depth per component.
Separately, hypothetical near-one inputs must evade every fixed bounded-residue-degree concentration, even if large ramification is allowed.
A useful next exponent-selection theorem must therefore control the distribution at residue degrees growing with the input, use several primes with their actual costs, or find arithmetic income beyond these bounded-degree clusters.
This proof does not force any of those alternatives to succeed.

The full inverse and complementary auxiliary cost on varying near-one inputs remains open.
The local maximal-order conclusion controls integrality, not archimedean heights of an inverse.
The prescribed periods in(5) may be much larger than d; their occurrence is not a linear-cost coverage theorem.
The one exceptional transition in(7) has not been replaced by an a priori bounded value.
All other primes and nonsaturated inputs remain admissible research directions, and unrestricted G0001 remains active and unresolved.

### Contribution and author checking

The coordinator supplied only the broad round question.
The assigned resultant_research AI developed Sections1-5, with the existing results explicitly reused above.
No derivation was supplied by another agent.
Author checking includes the completed product decomposition with nonreduced residue rings, injectivity and separated powers, derivation of a domain rather than assuming it, ramification/rank equality, finite-index passage, full-lattice fractional ideals and all finite levels, the unique-lowest binomial term and single-tie exception, norm and Smith multiplicities, actual root-field ramification rather than splitting-field degree, original-root counting at bad primes, and all exponent/measure normalizations.
The author self-check is complete.
The complete author proof is ready for full noncontributor review; no independent review is asserted here.
Fixed adoption remains separate and pending.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0104_v1.md#minimal-frobenius-local-complete-independent-review), with its original inspected scope and relationship.
