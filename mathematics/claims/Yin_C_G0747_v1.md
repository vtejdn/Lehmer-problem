---
author: Yin
---

# Explicit reflection masks and a zero-trace parity obstruction for height-one lifts

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the odd reciprocal mask reparametrization, explicit reflection-pair basis, improved counts and the separate zero-trace parity test through the full reciprocal carry.
The characteristic_zero_bridge agent checked and authored the complete polynomial bijections, exact sign fibers, global carry and trace jet, full-residual necessary conditions, sharpened endpoint and raised-source consequences.
Root read all saved MP1--MP9 and then all MP10--MP17.
Both agents are substantive contributors; this open fixed candidate awaits fresh isolated whole review and separate adoption.
The independent certificate inquiry retained in D43 is not part of this Claim.
No native coefficient expansion, numerical support count, actual rank computation or sign search is used.

## Statement

Use bars for coefficient reduction modulo2 and Phi=X^2+X+1 over Z, phi=Phibar.
The trace polynomials C_j for j>=1 satisfy C_j(z+z^(-1))=z^j+z^(-j); in particular C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X.
For odd n=2a+1, let B_n=1+sum_(j=1)^a C_jbar be the COMPLETE polynomial of nonidentity n-th-root traces.
For a monic integer trace T, use its OWN canonical polynomials

    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_(s,T)=rem_T(b_T^2-a_T^3+s G_T), s in{1,-1}.

All remainders and scalar divisions are actual integer operations at that SAME T before reduction.
Height1 means all integer coefficients lie in{0,1,-1}, with maximum absolute value1.
The multiplier parameter a is not the canonical polynomial a_T.

### A. Exact full source and explicit reflection basis

Start with an actual complete C691 representative Y as retained in [adopted C740](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25).
Retain Q=2^ell, ell>=82, m_src=Q/4-2, every complete original factor and multiplicity, and

    U_0=X^(2m_src)Y phi^(14m_src), d=deg U_0,
    Pbar_old=z^d U_0(z+z^(-1)),
    Dbar=Pbar_old/(z^2+1), r=2d-2.

In particular Y is prime to Xphi and2m_src>10.
Dbar is monic reciprocal of full degree r, constant1 and central coefficient0.
Let delta_i=[z^i]Dbar in{0,1}, and let its full support size be2k_support.
Choose ANY integer a>=ceil(d/2) for which n=2a+1 is coprime to15, and put

    U_a=U_0 B_n^2, d_a=d+2a,
    Pbar_a=Dbar(1+z^(2n)), deg Pbar_a=2d_a.

Only the actual C738 multiplier choice carries its additional complete-source preservation and paid bounds in Part E; they are not asserted for every a in this algebraic local domain.

If ceil(d/2)<=a<=d-2, set

    h_mask=2(d-a-2), m_mask=h_mask+1=2(d-a)-3,
    I_allowed={i:0<=i<=(m_mask-1)/2,
                     delta_i=delta_(m_mask-i)=1}.

The C740 reciprocal mask space

    Jspace={J in F_2[z]: degJ<=h_mask,
                z^(h_mask)J(z^(-1))=J,
                support((1+z)(1+z^n)J) subset support(Dbar)}

has the EXACT F_2 basis

    J_i=z^i sum_(j=0)^(m_mask-2i-1)z^j, i in I_allowed.

Consequently

    e=dim Jspace=|I_allowed|
      =sum_(i=0)^((m_mask-1)/2)delta_i delta_(m_mask-i),
    e<=min(d-a-1,floor(k_support/2)).

The displayed sum is in the ORDINARY INTEGERS, not in F_2.
The images sigma_i=(1+z)(1+z^n)J_i have four distinct positions i,m_mask-i,n+i,n+m_mask-i, and these supports are disjoint for distinct allowed i.
The J_i geometric-sum supports themselves may overlap.
For a>=d-1 the cap is negative and C740's mask space is{0}, with e=0; no odd ambient degree or basis is assigned to that negative cap.
No actual coefficient delta_i or numerical value of e is evaluated here.

### B. Exact added-modulus counts

Every monic reciprocal height1 integer lift P of Pbar_a with constant1 is uniquely

    P=L+z^(2n)L^*, L^*=z^rL(z^(-1)),
    degL=r, L(0)=1, Lbar=Dbar.

There are exactly2^(2k_support-1) such lifts before any residual condition.
For its OWN trace T of degree d_a define the actual integer half-sum S=(L+L^*)/2 and sigma=Sbar.
The ADDED-MODULUS conditions

    B_n^2 | F_Tbar,
    B_n^2 | X_(s,T)bar

are equivalent and are parameterized by sigma=(1+z)(1+z^n)J with J in Jspace.
This uses C740's genuine integer carry and remains valid when B_n and U_0 overlap.
Each J has exactly2^(k_support-1) actual sign lifts, so

    local passing count=2^(e+k_support-1),
    local passing fraction=2^(e-k_support)
                           <=2^(-ceil(k_support/2)),
    zero-mask count=2^(k_support-1),
    nonzero-mask count=(2^e-1)2^(k_support-1).

These are counts only for the added B_n^2 modulus, not for every old primary condition.
The zero-mask fiber is exactly L^*=-L and P=L(1-z^(2n)), hence is reducible with a cyclotomic factor.

### C. Exact additional zero-trace test and refined counts

In the range h_mask>=0, EVERY height1 lift passing the added B_n^2 condition in Part B satisfies the SAME own-divisor jet

    a_Tbar=J(1)X^2 modulo X^3.

Thus X^3|a_Tbar if and only if J(1)=0.
Writing J=sum_i epsilon_i J_i, every J_i(1)=1, so this is exactly EVEN parity of the F_2 basis coefficients.
Put e_even=max(e-1,0).
The count of actual lifts satisfying BOTH the added B_n^2 condition AND X^3|a_Tbar is EXACTLY

    2^(e_even+k_support-1),

and its nonzero-mask subfamily has exactly

    (2^e_even-1)2^(k_support-1)

members.
The remaining sign choices in each mask fiber are unrestricted by this extra test.
These remain local-plus-X^3 counts, not counts of solutions to the complete old-primary conditions.

### D. Necessary consequences of either FULL own residual condition

On the actual full source, X^(2m_src) divides both b_Tbar and c_Tbar.
Therefore full coefficientwise evenness of EITHER F_T or X_(s,T) separately forces X^3|a_Tbar, since2m_src>10.
Each also forces the added B_n^2 condition by C740.
Their GLOBAL evenness conditions are not asserted equivalent.

In the weak range h_mask>=0, any irreducible height1 lift satisfying either FULL own residual condition must consequently lie in a NONZERO even mask.
Its number is at most

    (2^max(e-1,0)-1)2^(k_support-1).

In particular e<=1 forces the exact reducible form L(1-z^(2n)) for every lift satisfying either global condition.
At a=d-2 one always has e<=1, independently of delta_1.
Together with C740's a>=d-1 result, EVERY admissible a>=d-2 therefore excludes irreducible height1 lifts satisfying either full own residual evenness.
This exclusion concerns the displayed added-multiplier domain, not the original C691 source without that multiplier.
It does not declare all full sign systems inconsistent, and a nonzero even mask does not guarantee full residual success or irreducibility.

### E. Raised sources, actual complete multiplier costs and limits

For every q=2^j, the exact height1 support descent gives P_q=P(z^q), with own trace T(C_q) and FULL reciprocal degree2q d_a.
The added B_n^(2q) condition is equivalent to the base added B_n^2 condition, so Part B's counts and fraction are unchanged.
In the weak range, the additional X^(3q)|a_(T(C_q))bar condition corresponds exactly to Part C, with the same refined counts.
Full residual evenness descends, and every forced zero-mask member has the explicit factorization

    P_q=L(z^q)(1-z^(2nq)).

For the ACTUAL complete WEAK choice of [C738](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25), retain its fresh n_star and

    a=a_mul=30Q n_star ceil(d/(60Q n_star)),
    Y_star=Y B_n^2, U_star=U_a, R_star=R_0 B_n^2.

Here H_aux is the original C691 auxiliary H, B_src=X^(Q-m_src)H_aux(Xphi^2), and R_0=X^(2m_src)Yphi^(12m_src)B_src, with their complete meanings retained by C738.
Its full forward/root/fresh-factor/canonical/layer statements remain those of C738, consumed through C740.
In particular

    degY_star<29040Q^3+7212Q^2+308Q,
    d_a<29040Q^3+7212Q^2+316Q,

with complete degree gap degU_star-degR_star=m_src-8-5degH_aux>5m_src/256.
At q the full trace degree and gap are multiplied by q, the reciprocal degree is2q d_a, and the actual canonical binary G equals R_star^q for every corresponding Tbar=U_star^q.
These are the enlarged bounds, not the original DG8 numerical bounds.
The synthetic integer layer polynomial is not identified with the actual integer canonical G.

This theorem neither evaluates the actual weak-ceiling branch nor the actual low Dbar coefficients.
It supplies no full old-primary solution, irreducible passing input, higher residual precision, original total-Mahler bound, characteristic-zero identity or unrestricted G0001 conclusion.
The separate true-certificate analysis in D43 is outside this Claim.

## Complete argument

<a id="explicit-reflection-basis-for-height-one-masks"></a>
### Explicit reflection basis and exact local height1 counts

This is the complete fixed author argument contributed by root and characteristic_zero_bridge.
Root proposed the odd ambient reciprocal reparametrization, explicit allowed pairs and improved dimension/count bounds; characteristic_zero_bridge checked every polynomial bijection, block separation, support condition, endpoint and scope below.
The sole mathematical interface needed is [adopted C740's complete local mask theorem](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25), including its actual canonical carry with old-source overlap, allowed signs, local counts and raised-source descent.
The new argument evaluates the structure of that mask space explicitly; it does not calculate any previously unknown coefficient of a chosen full C691 representative.
C783 and the separate certificate inquiry are not premises of this mask theorem.

#### Exact domain and explicit basis

Retain C740's complete original C691 source U_0 of trace degree d and

    Pbar_old=z^d U_0(z+z^(-1)),
    Dbar=Pbar_old/(z^2+1), r=2d-2.

Thus Dbar is an ACTUAL full monic reciprocal binary polynomial of degree r, constant1 and central coefficient0.
Let delta_i=[z^i]Dbar in{0,1}, and write its full support size as2k_support.
The integer k_support counts reciprocal supported pairs in Dbar and is unrelated to a dyadic exponent or binary root polynomial.
Choose an integer multiplier parameter

    ceil(d/2)<=a<=d-2, n=2a+1, gcd(n,15)=1,
    h_mask=r-n-1=2(d-a-2),
    m_mask=h_mask+1=r-n=2(d-a)-3.              (MP1)

Here h_mask is even and nonnegative, and m_mask is odd and positive.
Moreover n>=d+1 and m_mask<=d-3, so

    m_mask<d-1=r/2<n, m_mask<n.                (MP2)

The mask-space notation h_mask is C740's h; m_mask is not C691's source parameter m.
Set A_n=(1+z)(1+z^n).
The actual C740 space consists of exactly the binary polynomials J with

    deg J<=h_mask,
    z^(h_mask)J(z^(-1))=J(z),
    support(A_n J) subset support(Dbar).       (MP3)

The reciprocal equation uses the indicated ambient degree, allowing endpoint coefficients of J to vanish.
For every allowed low reflection pair define

    I_allowed={i: 0<=i< m_mask-i<=m_mask,
                   delta_i=delta_(m_mask-i)=1}.

Its condition on i is equivalently0<=i<=(m_mask-1)/2.
Then MP3 has the explicit F_2 basis

    J_i=z^i sum_(j=0)^(m_mask-2i-1) z^j,
                         i in I_allowed.      (MP4)

In particular its dimension is the ORDINARY INTEGER pair count

    e=|I_allowed|
     =sum_(i=0)^((m_mask-1)/2) delta_i delta_(m_mask-i).
                                                   (MP5)

The sum in MP5 is not taken in F_2; binary addition there would retain only parity and would not give the dimension.
No actual numerical value of e or of any unknown delta_i is asserted here.

#### Bijection with the odd reciprocal coefficient space

Set B_mask=(1+z)J, so deg B_mask<=m_mask and

    sigma=A_nJ=(1+z^n)B_mask.                  (MP6)

Reversing with the stated ambient degrees gives

    z^(m_mask)B_mask(z^(-1))
       =(1+z)z^(h_mask)J(z^(-1)).

Thus ambient reciprocity of J implies ambient reciprocity of B_mask.
Conversely, if a binary polynomial B_mask has degree at most m_mask and is reciprocal at that ODD ambient degree, its coefficients come in pairs i,m_mask-i without a central singleton.
Their sum at z=1 is0 in F_2, so1+z divides B_mask.
The unique quotient J=B_mask/(1+z) has degree at most h_mask, and cancelling the nonzero polynomial1+z in the displayed reversal identity proves its ambient h_mask reciprocity.
This is a linear bijection between the two reciprocal spaces, including the zero polynomial and all polynomials whose actual degree is below the ambient degree.
No additional condition at z=1 is required on the odd reciprocal B_mask.

By MP2, the two blocks in sigma=B_mask+z^n B_mask are disjoint.
Its coefficient at each i in[0,m_mask] is B_mask,i and its coefficient at n+i is the same B_mask,i; every coefficient outside those two intervals is0.
Since r=n+m_mask and Dbar is reciprocal,

    delta_(n+i)=delta_(r-n-i)=delta_(m_mask-i).

Hence the FULL support condition in MP3 is equivalent to allowing B_mask,i=1 only when delta_i=delta_(m_mask-i)=1.
This condition is imposed on an entire low reflection pair, because B_mask,i=B_mask,(m_mask-i).
The central index d-1 lies strictly between the two blocks by MP2 and automatically has zero sigma coefficient.
Thus no central condition or high-block condition has been lost in this reduction.

An odd ambient reciprocal B_mask has the standard coefficient-pair expansion

    B_mask=sum_i epsilon_i B_i,
    B_i=z^i+z^(m_mask-i), 0<=i<=(m_mask-1)/2.

The support conditions set precisely the disallowed epsilon_i to0 and leave each allowed epsilon_i free.
This proves that the B_i with i in I_allowed are a basis of the allowed B_mask space.
Since m_mask-2i is odd and positive,

    B_i/(1+z)=z^i(1+z+...+z^(m_mask-2i-1)),

which is exactly MP4, and the bijection proves MP5.
The full mask images are

    sigma_i=A_nJ_i
      =z^i+z^(m_mask-i)+z^(n+i)+z^(n+m_mask-i). (MP7)

These four positions are all distinct, and distinct allowed i give disjoint FOUR-POSITION supports by block separation and distinct low pairs.
The B_i supports are also disjoint.
The geometric-sum supports of the J_i themselves can overlap; their independence follows from the injective map to the disjoint B_i or sigma_i, not from a false disjointness assertion about J_i.

#### Exact dimension bound, local fraction and realization limits

There are only(m_mask+1)/2=h_mask/2+1=d-a-1 possible low reflection pairs.
Every allowed pair in MP7 uses four distinct positions of support(Dbar).
Since distinct masks use disjoint such supports and Dbar has total support2k_support, one has4e<=2k_support.
Equivalently each mask uses two distinct full ambient-r reciprocal pairs, namely{i,n+m_mask-i} and{m_mask-i,n+i}.
Therefore

    e<=min(d-a-1, floor(k_support/2)).          (MP8)

This improves the earlier bound e<=k_support without omitting any full support positions.
In particular e=0 if and only if there is no pair of supported indices in[0,m_mask] summing to m_mask.
This is an exact support criterion, not a declaration that it holds for the actual C691 source.
At a=d-2 one has h_mask=0,m_mask=1 and I_allowed is{0} precisely when delta_1=1, since delta_0=1.
Thus the endpoint recovers exactly C740's e=1 iff[z]Dbar=1, when the required coprimality condition holds.
The separate a>=d-1 range has h_mask<0 and e=0 by C740; MP1--MP7 do not assign an odd ambient degree to a negative cap.

For clarity, the full binary reciprocal extension is

    Pbar_a=Dbar(1+z^(2n)),
    U_a=U_0 B_n^2, d_a=d+2a.

The B_n here is the COMPLETE trace polynomial used in C740 and is distinct from the coefficient polynomial B_mask above.
Every monic reciprocal height1 lift of Pbar_a is uniquely P=L+z^(2n)L^*, with degL=r, L(0)=1 and Lbar=Dbar.
There are2k_support supported coefficients of L, one of which has fixed value L(0)=1; all others may independently be either sign.
Thus there are EXACTLY2^(2k_support-1) allowed height1 lifts before imposing any residual equation.

C740 identifies the ADDED B_n^2 residual condition with the mask sigma=A_nJ, and each such J has exactly2^(k_support-1) actual sign lifts.
Combining that adopted integer-carry equivalence with MP5 gives

    local passing count = 2^(e+k_support-1),
    local passing fraction = 2^(e-k_support)
                             <=2^(-ceil(k_support/2)),
    zero-mask count = 2^(k_support-1),
    nonzero-mask count = (2^e-1)2^(k_support-1). (MP9)

The fraction is an exact ratio among all allowed coefficient signs for this FIXED binary polynomial, not a probability assertion about sources or irreducibility.
The local first and second residual conditions are equivalent here only modulo the ADDED B_n^2, as in C740, and allow overlap between B_n and U_0.
Additional old multiplicity on an overlapping factor, all other old primary conditions and higher bits remain outside this count.
The ordinary integer canonical divisions and SAME own divisor T are exactly those in C740; replacing the mask space by MP4 does not replace its actual carry by a free trace coordinate.

The zero-mask fiber is exactly L^*=-L and P=L(1-z^(2n)), so every such member is reducible with a cyclotomic factor.
Any irreducible lift satisfying full evenness of EITHER own residual F_T or X_(s,T) must therefore come from a nonzero mask.
Its number is at most the nonzero-mask count in MP9, without asserting that any such member satisfies the full old equations or is irreducible.
A nonzero basis vector does supply local passing sign lifts through C740's actual pairwise sign construction, but supplies neither complete first-bit success nor irreducibility.

For every q=2^j, the exact height1 support descent in C740 identifies P_q=P(z^q) and its own trace T(C_q), with full original degree2q d_a.
The ADDED B_n^(2q) local condition is equivalent to the base one, so the dimensions, bases at the base, all counts and the fraction in MP9 are unchanged after this actual descent.
The zero-mask family becomes L(z^q)(1-z^(2nq)), retaining its explicit reducibility.
No dyadic enlargement supplies extra sign freedom or turns a nonzero mask into an irreducible full-source input.

For C738's actual complete WEAK multiplier, all of its retained forward/root/fresh-factor data, actual binary canonical G, enlarged degree/gap and separate synthetic-layer statements remain exactly at their adopted scopes through C740.
The new reflection calculation neither chooses a different completion nor evaluates the old actual degree against30Q n_star, nor computes the necessary low Dbar coefficients.
It supplies a finite explicit coefficient-pair interface in place of an unspecified matrix rank, while the actual source evaluation and complete old-primary/irreducible realization remain unresolved.
No original total-Mahler bound, characteristic-zero identity or unrestricted G0001 conclusion follows from this local support theorem.

<a id="zero-trace-parity-refinement-of-local-masks"></a>
#### A separate zero-trace parity constraint on the explicit mask basis

Root proposed testing the existing X-primary through the GLOBAL reciprocal integer carry after the added-component condition is imposed.
Characteristic_zero_bridge checked that carry, both constant/linear zeros of Delta(L), the missing odd coefficient at order5, the exact own-trace remainder, all sign fibers and the full-first-bit consequences below.
This is an additional part of the same fixed MP author theorem, not an independent review or a contribution to the separate certificate analysis.
Retain MP1--MP9 and the actual original C691 source parameter m_src, so U_0=X^(2m_src)Y phi^(14m_src), with Y prime to Xphi and2m_src>10.
The symbol m_src is distinct from m_mask throughout.

Put y=z+1 and work in F_2[[y]] for orders and Taylor coefficients, with z=1+y a unit.
The trace substitution is x=z+z^(-1)=y^2/z.
The full original reciprocal quotient satisfies

    Dbar(z)=z^(d-2m_src)y^(4m_src-2)
               Y(x)phi(x)^(14m_src),
    ord_y Dbar=4m_src-2.                       (MP10)

The equality is interpreted through the exact trace substitution; the right side is a polynomial overall and its other factors are units at y=0.
In particular Dbar(1)=Dbar'(1)=0.
This uses the FULL source's X^(2m_src) factor and unit conditions, not just a root-set description of that primary.

Let P=L+z^(2n)L^* be any height1 lift passing the added B_n^2 condition, and retain its ACTUAL integers

    E=(L^*-L)/2, S=(L+L^*)/2,
    Dbar=Lbar=L^*bar, sigma=Sbar=Dbar+Ebar.

For an integer z-polynomial A define Delta_z(A)=[A(z^2)-A(z)^2]/2.
For the own trace T define Delta_T=[T(C_2)-T^2]/2; these are distinct operations in their indicated variables, both integral.
The exact integer identities from C740 are

    Delta_z(P)=Delta_z(L)+z^(4n)Delta_z(L^*)
                                      -z^(2n)LL^*,
    Delta_z(L^*)-Delta_z(L)=E(z^2)-2LE-2E^2.

Reduce those actual integer identities only AFTER their divisions by2.
Set v=1+z^n and u=z^(2n); thus v^2=1+u and v^4=1+u^2 over F_2.
Writing Deltabar_L for Delta_z(L)bar gives the GLOBAL binary polynomial identity

    Delta_z(P)bar
      =v^4 Deltabar_L+u^2 sigma^2+u v^2 Dbar^2. (MP11)

Indeed Ebar^2=(sigma+Dbar)^2, so the Dbar terms combine as(u^2+u)Dbar^2=u v^2Dbar^2.
This identity holds as a full binary polynomial, not merely at the added roots.

Write J=sum_(i in I_allowed) epsilon_i J_i, and let r_active be the ordinary number of epsilon_i equal to1.
The disjoint FOUR-POSITION supports in MP7 give wt(sigma)=4r_active.
Since the actual S has entries0 or either sign and zero center, sigma records exactly its nonzero paired positions; there are2r_active same-sign pairs in L.
Each such pair contributes either2 or-2 to S(1), so S(1) is divisible by4.
Also L^*(1)=L(1), hence S(1)=L(1).
It follows that

    Delta_z(L)(1)=[L(1)-L(1)^2]/2=0 modulo2.

Differentiate the integer carry before reduction:

    Delta_z(L)'=z L'(z^2)-L L'.

At z=1 its binary value is(1-L(1))L'(1)bar=Dbar'(1)=0 by MP10.
Therefore

    4|L(1), ord_y Deltabar_L>=2.               (MP12)

This conclusion is independent of the remaining sign choices within each allowed mask fiber.

Let S_n(z)=1+z+...+z^(n-1); since n is odd, v=yS_n and S_n(1)=1 in F_2.
The local mask formula is sigma=yvJ=y^2S_nJ.
In MP11 the first term has y-order at least4+2=6, and the third has y-order at least2+2(4m_src-2)=8m_src-2>=6.
The second term is u^2 sigma^2, an actual square over F_2, so it has NO odd powers in its y expansion.
Its coefficient at y^4 is u(1)^2 S_n(1)^2 J(1)^2=J(1).
Consequently the full carry satisfies the precise jet

    Delta_z(P)bar=J(1)y^4 modulo y^6.          (MP13)

The zero y^5 coefficient is part of this argument; knowing only the y^4 coefficient would not by itself give the following divisibility equivalence.

Now use the exact integer trace identity, still at P's OWN divisor,

    Delta_z(P)=z^(2d_a)Delta_T(z+z^(-1)),
    a_T=rem_T Delta_T.

The complete binary Tbar=U_a=U_0B_n^2 has exact X-order2m_src, since B_n(0)=1, Y(0)=1 and phi(0)=1.
Thus a_Tbar=Delta_Tbar modulo X^3 because2m_src>=3.
In the trace identity, z^(2d_a) is a unit at y=0 and x=y^2/z has y-order2 and leading coefficient1.
The absence of y-orders0 and2 in MP13 first forces the constant and linear coefficients of Delta_Tbar to vanish; its coefficient of X^2 then equals the y^4 coefficient J(1).
Equivalently,

    a_Tbar=J(1)X^2 modulo X^3,
    X^3|a_Tbar iff J(1)=0.                    (MP14)

Here zero polynomials have infinite order, and the equivalence includes the zero-mask fiber.
The actual monic divisor carry is retained: a_Tbar is identified with Delta_Tbar only at the proved X^3 precision, using the complete old X-primary multiplicity.

For every basis element in MP4, J_i(1)=m_mask-2i=1 in F_2 because its geometric length is odd.
Therefore J(1)=sum_i epsilon_i in F_2, and MP14 is exactly the EVEN-parity condition on the explicit basis coefficients.
If e>0 this evaluation is a nonzero linear functional on the e-dimensional mask space and has kernel dimension e-1; if e=0 its kernel is the zero space.
Put e_even=max(e-1,0).
The remaining2^(k_support-1) actual signs in each mask fiber are unrestricted by MP14, since MP12--MP14 hold for EVERY such choice.
Hence

    dim{J in Jspace:J(1)=0}=e_even,
    count(added B_n^2 condition AND X^3|a_Tbar)
                      =2^(e_even+k_support-1),
    nonzero-mask count under both conditions
                      =(2^e_even-1)2^(k_support-1). (MP15)

These are exact local-plus-X^3 counts for the actual height1 lifts, not counts for the complete old-primary equations.
When e>=1 exactly half the previously passing masks survive this extra test; when e=0 the zero mask survives and no artificial loss of a factor2 is imposed.

Finally both odd canonical polynomials b_Tbar,c_Tbar are divisible by X^(2m_src).
Indeed Tbar has that factor, C_3bar=X^3+X and C_5bar=X^5+X^3+X=Xphi^2 each have an X factor, so Tbar(C_3bar),Tbar(C_5bar) also have it; actual monic remainder and odd scalar division preserve the indicated binary divisibility.
Reducing the full canonical identities modulo this old X-primary therefore gives

    F_Tbar=a_Tbar^5 modulo X^(2m_src),
    X_(s,T)bar=a_Tbar^3 modulo X^(2m_src).      (MP16)

If the FULL own F_T is even, then5ord_X(a_Tbar)>=2m_src>10, which forces X^3|a_Tbar.
If the FULL own X_(s,T) is even, then3ord_X(a_Tbar)>=2m_src>10, which also forces X^3|a_Tbar.
Each full condition separately also implies the added B_n^2 condition by C740, so each necessarily lies in the counted subspace of MP15.
This does not assert equivalence of the two GLOBAL residual conditions or sufficiency of the X^3 test for their much higher old-primary multiplicities.

Every irreducible height1 lift satisfying either FULL own first residual or FULL own second residual evenness must consequently belong to a NONZERO even mask.
Its number is at most(2^max(e-1,0)-1)2^(k_support-1).
In particular e<=1 forces J=0 and the exact reducible form P=L(1-z^(2n)), for any lift satisfying either of those global conditions.
At a=d-2, MP8 gives e<=1 without evaluating delta_1; this excludes irreducible full-first-bit lifts at that endpoint regardless of which local mask count occurs.
Together with C740's a>=d-1 result, the same conclusion holds for EVERY admissible a>=d-2 in this added-multiplier domain.
It is not extended to the original C691 source without that multiplier, and it does not declare all full sign systems inconsistent.

For raised q=2^j, exact own-canonical covariance gives a_(T(C_q))bar=a_Tbar(X^q).
Thus the added B_n^(2q) condition together with X^(3q)|a_(T(C_q))bar has exactly the same counts in MP15, at full original degree2q d_a.
Full residual evenness descends, and any forced zero-mask output is

    P_q(z)=L(z^q)(1-z^(2nq)).                 (MP17)

All zero-mask reducibility and full-source exclusions above persist after this actual descent.
No delta_i, actual e, full old-primary solution, irreducible passing input, higher residual precision or total-Mahler bound has been produced by the parity refinement.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision reflection-zero-trace-mask-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T20:31 |
| status | open |
| reason | Register the complete MP1--MP17 author theorem after root read both the full reflection-basis proof and the full zero-trace extension. The former turns C740's exact local mask space into an explicit low-pair count with disjoint four-position images; the latter retains the global integer carry and own-divisor trace jet, giving an exact even-basis-parity subspace for the additional X3 condition. Full evenness of either own residual separately requires that subspace and forces reducibility when e<=1, including every admissible a>=d-2. Added-modulus counts, local-plus-X3 counts, full necessary conditions and actual C738 complete-source costs remain distinct. Root and characteristic_zero_bridge are contributors; fresh isolated whole review and separate adoption remain outstanding. No actual C691 coefficient/e value, full old-primary solution, irreducible realization, total-Mahler bound or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire explicit mask and zero-trace theorem](#statement) | Parts A--E with complete original source, arbitrary admissible multiplier versus actual complete choice, ambient reciprocal masks, integer pair count and disjoint images, exact local and local-plus-X3 fibers, full-own-F/X necessary consequences, endpoint, raised q and every original cost/realization boundary. |
| argument | [Complete MP1--MP17 proof](#complete-argument) | Odd ambient reciprocal bijection, exact support reduction and basis/counts, global integer reciprocal carry, full original X-primary order, Delta(L) double zero, missing y5 coefficient, same-divisor trace jet, F2 parity versus integer counts, refined fibers and full residual/raised consequences. |
| dependency | [Adopted actual local mask and sign interface](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | Entire WM1--WM15 actual full-support input, squared added-modulus equivalence including old overlap, monic trace/reciprocal carry, integer half-sum and allowed sign fibers, existing a>=d-1 obstruction and exact raised-source descent. The explicit reflection basis and extra X3 parity test are new and proved here. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Full original U_0=X^(2m_src)Yphi^(14m_src), Y prime to Xphi, Q>=2^82 and m_src=Q/4-2, full degree and retained factor multiplicities. These give the exact old X-order and Dbar order used in MP10/MP16; no coefficient or support count is inferred without calculation. |
| dependency | [Adopted complete weak multiplier costs](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | Only for its actual weak a_mul choice: complete forward/root/fresh/canonical/gap/layer data and the newly paid degree bounds. These source properties are not claimed for every multiplier in the broader algebraic local domain, and synthetic/canonical integer polynomials remain distinct. |
| dependency | [Adopted actual height1 descent and canonical covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact height1 support substitution and all-six own-canonical covariance, consumed through C740 for every raised q with full reciprocal degree. No ascending irreducibility, new precision or unconstructed field norm is inferred. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T20:48 |
| status | proved |
| reason | Adopt the complete Parts A--E and MP1--MP17 theorem after fresh isolated whole R967 PASS. Root read both entire author proof parts, the exact fixed statement/input scopes and complete independent finding. The explicit reflection basis gives the ordinary integer dimension and exact local sign counts with full support retained. The actual global reciprocal carry, Delta(L) double zero and missing y5 term give the own-trace a_Tbar=J(1)X^2 modX^3 for every passing sign fiber, hence the exact even-mask refinement. Full evenness of either own residual separately requires this condition; e<=1 and every admissible a>=d-2 therefore force the zero-mask reducible form. All raised-q and actual complete-multiplier expenses remain scoped. No actual source coefficient/e evaluation, full old-primary solution, irreducible realization, higher precision, characteristic-zero or Mahler conclusion or unrestricted Task completion is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire explicit mask and zero-trace theorem](#statement) | Parts A--E with complete original source, arbitrary admissible multiplier versus actual complete choice, ambient reciprocal masks, integer pair count and disjoint images, exact local and local-plus-X3 fibers, full-own-F/X necessary consequences, endpoint, raised q and every original cost/realization boundary. |
| argument | [Complete MP1--MP17 proof](#complete-argument) | Odd ambient reciprocal bijection, exact support reduction and basis/counts, global integer reciprocal carry, full original X-primary order, Delta(L) double zero, missing y5 coefficient, same-divisor trace jet, F2 parity versus integer counts, refined fibers and full residual/raised consequences. |
| dependency | [Adopted actual local mask and sign interface](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | Entire WM1--WM15 actual full-support input, squared added-modulus equivalence including old overlap, monic trace/reciprocal carry, integer half-sum and allowed sign fibers, existing a>=d-1 obstruction and exact raised-source descent. The explicit reflection basis and extra X3 parity test are new and proved here. |
| dependency | [Adopted complete original source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Full original U_0=X^(2m_src)Yphi^(14m_src), Y prime to Xphi, Q>=2^82 and m_src=Q/4-2, full degree and retained factor multiplicities. These give the exact old X-order and Dbar order used in MP10/MP16; no coefficient or support count is inferred without calculation. |
| dependency | [Adopted complete weak multiplier costs](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | Only for its actual weak a_mul choice: complete forward/root/fresh/canonical/gap/layer data and the newly paid degree bounds. These source properties are not claimed for every multiplier in the broader algebraic local domain, and synthetic/canonical integer polynomials remain distinct. |
| dependency | [Adopted actual height1 descent and canonical covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact height1 support substitution and all-six own-canonical covariance, consumed through C740 for every raised q with full reciprocal degree. No ascending irreducibility, new precision or unconstructed field norm is inferred. |
| review | [Fresh independent whole reflection and zero-trace finding](../audits/reviews/Yin_R_G0967_v1.md#whole-reflection-zero-trace-finding) | Entire fixed Parts A--E and MP1--MP17, complete basis/support/counting bijections, integer and binary parity distinctions, global carry and exact own-trace jet, every sign fiber/necessary condition/endpoint/raised-q assertion and actual complete-source cost boundary. |

