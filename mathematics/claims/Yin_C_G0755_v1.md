---
author: Yin
---

<a id="paid-dense-support-old-x-affine-feasibility"></a>
# Paid dense complete-row support and actual height-one old-X feasibility

Human author Yin.
Provenance: project deduction under the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root identified the unresolved actual endpoint-column problem and proposed the low-X Chebyshev-period reduction.
Salem_completion derived and checked the complete-row dense-support construction, full actual column rank, genuine canonical target, exact sign counts and all paid source and degree interfaces.
Root read the entire saved PX1--PX7 argument and checked the C753-consuming PX8 interface and numerical substitution.
Both agents are substantive contributors; this complete fixed candidate was OPEN at author registration, pending fresh isolated whole review and separate adoption.
The stable [D6 endpoint calculation](../drafts/Yin_D_G0006.md#next-endpoint-edge-sign-and-old-x-interface) is contributor context, and every necessary sign/canonical interface is explicitly retained below or consumed from the adopted fixed local proofs.
Adopted C753 supplies the unconditional source in PX8; its fresh review is not a review of the new dense-support argument.
No native computation, numerical support enumeration or external source theorem is used.
The separate proposed all-old-primary mechanism is not part of this Claim.

## Statement

### PX1. Exact conditional input and conclusion

Work over F_2 for binary polynomials and use bars for reduction of actual integer polynomials.
The integer trace polynomials satisfy C_0=2, C_1=X and C_(j+1)=XC_j-C_(j-1), so C_j(z+z^(-1))=z^j+z^(-j).
For every actual monic integer T use its OWN canonical polynomials

    a_T=rem_T(T(C_2))/2, b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_(epsilon,T)=rem_T(b_T^2-a_T^3+epsilon G_T),
    epsilon in{1,-1}.

All scalar divisions are actual integer divisions before reduction, and all remainders use the indicated SAME monic divisor.
Retain an actual complete C691-type row representative with

    Q=2^ell, ell>=82, m=Q/4-2, N_src=8m, L_src=4Q,
    phi=X^2+X+1, chi=Xphi^2, Psi=phi(chi),
    Y=Y_pre B_(n_star)^3,
    H_0=X^(2m)Y, U_0=H_0phi^(14m), d_0=deg U_0,
    B_src=X^(Q-m)H_aux(chi),
    R_0=H_0phi^(12m)B_src.                         (PX1)

Here B_b is the COMPLETE nonidentity odd-order trace row, not an arbitrary selected irreducible factor.
Retain all C691 DG3/DG6 jets, both full forward divisibilities, the multiplicity floor2, X^(8m)|Y', the same beta and Z_0, and the full canonical identity R_0=rem_(U_0)(U_0(chi)^3)!=0.
Retain the exact positive gap

    g_0=deg U_0-deg R_0=m-8-5deg H_aux>5m/256.

The selected primitive-order factor psi_star of order n_star has EXACT multiplicity3 in Y and Y B_src, with

    n_star>30L_src, n_star=1 modulo10L_src,
    gcd(n_star,15)=1,
    n_star<4Q^2+80Q+1.                            (PX2)

The last upper bound is used only for the optional coarse cost estimate, and is available for the original selected C691 fresh row.
An input already extended by C751's paid rows is allowed if it retains these actual properties and its enlarged degree d_0 is used.
Do not assign it the original DG8 degree bound automatically.
Let E_pre count all nontrivial ordinary-row exponents before the SAME selected fresh cubic, with the exact C751 convention excluding B_1 and divided rows.
Assume

    E_pre=0 modulo4, gcd(2d_0-5,15)=1.            (PX3)

Thus the starting endpoint is admissible and has the two-dimensional mask e=2.
No value of E_pre or admissibility of an unspecified original bounded witness is inferred.

The construction below gives a new ACTUAL complete source U_*=X^(2m)Y_*phi^(14m), of a paid larger degree d_*, still satisfying PX1--PX3 with the SAME m, H_aux, B_src, n_star and gap g_0.
For the recomputed endpoint

    a_*=d_*-3, n_e=2d_*-5, d_e=3d_*-6,
    U_e=U_* B_(n_e)^2, deg U_e=d_e,              (PX4)

consider the genuine monic reciprocal height1 integer lifts P of Pbar_e, and their OWN trace T of degree d_e.
Set

    R_p=ceil(2m/p),
    v_p=ceil(m/p)-2, p in{5,3}.                 (PX5)

All these dimensions are positive in the stated source range.
For the unique nonzero even added mask, the ACTUAL nonedge sign columns span the whole space V_(R_p)=span_F2{X^4,X^6,...,X^(2ceil(R_p/2)-2)}.
In particular the affine target is attained for EVERY one of the four edge patterns (++-),(+-+),(-++),(---), with no replacement of supported height1 signs by unrestricted trace coefficients.
If the actual full support of D_*=P_(U_*)/(z^2+1) has size2k_*, the exact number for each one of those edge patterns is

    2^(k_*-4-v_p),                               (PX6)

for the old-X condition X^(R_p)|a_Tbar.
Combining the four patterns gives2^(k_*-2-v_p), and the combined EP10 affine map has rank v_p+1.
For BOTH old-X residual conditions use p=3; this also pays the weaker p=5 condition.
Every counted lift passes the added B_(n_e)^2 condition for BOTH residuals and has gcd_(Q[z])(P,z^(2n_e)-1)=1.
No condition at all remaining old primaries, irreducibility, higher coefficient precision or Mahler bound is asserted.
For EVERY Q=2^ell with ell>=82, PX8 supplies such an actual source and these height1 sign lifts without assuming admissibility of an original bounded witness, with d_*<14640Q^4+6006Q^3+945Q^2.

## Complete argument

### PX2. Two paid invisible rows with their full source properties

Take C751's small row

    c_s=1 if L_src=1 modulo3, and2 otherwise,
    n_s=1+10L_src c_s, b_s=(n_s-1)/2<=40Q.

First put

    Y_1=Y B_(n_s)^9, U_1=U_0 B_(n_s)^9,
    R_1=R_0 B_(n_s)^9, d_1=d_0+9b_s,
    r_1=2d_1-2.                                  (PX7)

The exponent9 is in C751's admissibility-preserving set.
It changes E_pre from0 to1 modulo4 and leaves d_1=d_0 modulo15.
Its exact degree cost is9b_s<=360Q.
The complete source properties and original exact triple factor are retained by C751 WR5--WR9.
When the starting source is itself an already paid extension, the same proof applies: the row is still invisible at the unchanged full source precision and still misses the selected n_star, while overlaps with other old factors only increase their multiplicities.

Choose the low-X jet parameters

    R=R_3=ceil(2m/3), K=ceil(R/2)-1=ceil(m/3)-1,
    P_run=the least power of2 at least2K+1,
    B_step=30L_src n_star,
    c_p=ceil((r_1+P_run)/B_step),
    n_p=1+B_step c_p, b_p=(n_p-1)/2,
    k_0=4m-2, rho=k_0+1=4m-1.                    (PX8)

Here c_p is a positive ordinary integer, n_p is odd, n_p=1 modulo15, n_p=1 modulo10L_src, and n_p=1 modulo n_star.
Consequently n_p is coprime to15 and the complete row B_(n_p) contains no primitive-order-n_star factor.
The full safe period from C664, as used at the actual C691 precision in C751, gives

    B_(n_p)=1 modulo X^(N_src)phi^(2N_src).

Its degree b_p is divisible by15.
Define the final source by the ACTUAL polynomials

    M_p=B_(n_p)^rho,
    Y_*=Y_1 M_p, U_*=U_1 M_p, R_*=R_1 M_p,
    d_*=d_1+rho b_p.                             (PX9)

The exponent rho is at least3.
Every new factor has multiplicity at least2, every existing multiplicity only increases, and the selected psi_star still has EXACT multiplicity3 in Y_* and Y_* B_src.
All orders of B_(n_p) are odd and prime to3 and5, so the complete root sets are preserved by both powering maps.
Since these maps are unramified at their nonzero roots in characteristic2, the full multiplicities give both forward divisibilities for Y_*; proper-divisor overlap with the old rows creates no problem.
In the C667 complete row presentation only ordinary exponents increase, so its ordinary/divided multiplicity inequalities also remain valid.
Neither n_p being prime nor being coprime to every old row index is needed.

The following checks explicitly extend C751's proof to the large rho; its finite list of exponents is not cited as if it already included rho.
Since M_p=1 modulo X^(N_src)phi^(2N_src), both DG3 jets are unchanged.
Also M_p(chi)=1 modulo phi^(2N_src), because the low X^(N_src) factor acquires phi-order2N_src under chi.
Thus the actual new H_*=X^(2m)Y_*, V_*=H_*B_src and C_*=X^(2m)Y_*(chi)Psi^(14m) have exactly the old DG6 data at precision phi^(16m), with the same beta and Z_0.
The derivative condition survives: write the low error as X^(N_src)A; N_src is even, so its derivative is X^(N_src)A'.
Multiplying the retained Y_1 by M_p therefore still gives X^(8m)|Y_*'.

The forward condition gives H_*|C_*.
The exact binary identity

    U_*(chi)^3+R_*=phi^(12m)(V_*+C_*^3)          (PX10)

vanishes on H_* and on phi^(14m), using respectively full forward divisibility and the unchanged DG6 relation.
Those full moduli are coprime.
The degree gap g_0 is unchanged, hence deg R_*<deg U_* and R_*!=0.
Therefore R_*=rem_(U_*)(U_*(chi)^3), with full canonical bbar=0, Gbar=R_* for any integer trace reducing to this PRE-endpoint source.
The sole unsaturated primary remains phi with orders14m/12m.
No dyadic lift or passing full residual for the endpoint U_e is smuggled into this source assertion.

The new ordinary exponent class is

    E_pre,*=E_pre+9+rho=E_pre+4m+8=0 modulo4.

Moreover d_*=d_1=d_0 modulo15.
Thus the recomputed a_*=d_*-3 endpoint remains admissible and C751's exact low reciprocal formula gives delta_0=delta_1=delta_2=delta_3=1.
It again has e=2, although the intermediate source Y_1 has e=0 at its own endpoint.
No height1 problem is solved at that intermediate endpoint.

### PX3. A consecutive block in the ACTUAL low-half support

Let

    D_1=z^(d_1)U_1(z+z^(-1))/(z^2+1).

The exact old X-order is2m, because every added ordinary row is a unit at X=0.
Trace substitution X=(z+1)^2/z consequently gives

    D_1=(1+z)^(k_0)H(z),
    H in F_2[z], deg H=r_1-k_0, H(1)=1.         (PX11)

This uses the EXACT order k_0=4m-2, not merely a lower bound; Y_1(0)=phi(0)=1.
The complete ordinary-row reciprocal identity P_(B_n)=S_n=(1+z^n)/(1+z) gives

    D_*=D_1 S_(n_p)^rho
       =H(z)(1+z^(n_p))^rho/(1+z).             (PX12)

The right side is an exact polynomial, since 1+z divides1+z^(n_p); it may also be expanded as a formal power series at z=0 to inspect coefficients.
For every integer j<n_p, the factor (1+z^(n_p))^rho has only its constant term at degree at most j.
Thus

    [z^j]D_*=sum_(i=0)^j [z^i]H=1
                    whenever deg H<=j<n_p.     (PX13)

This is a coefficientwise full-polynomial calculation, not a support-density estimate or an uncomputed native expansion.
In particular all P_run consecutive indices

    J_run={r_1,r_1+1,...,r_1+P_run-1}            (PX14)

belong to the ACTUAL support of D_*.
Indeed r_1>=deg H and the choice in PX8 gives r_1+P_run<=n_p-1.
Also r_1>=4, so none of these positions is an edge index0,1,2,3.
They all lie in the permitted LOW HALF j<d_*-1: the run ends before n_p-1=2b_p, while

    d_*-1-(n_p-1)=d_1-1+(rho-2)b_p>0.

Thus these are genuine independent nonedge pair signs of the height1 mask fiber.
Their reflected high partners remain distinct, and no forbidden central coefficient or additional variable is introduced.

### PX4. A whole safe period spans every required low-X direction

For clarity write c_j=C_jbar, with c_0=0 and c_1=X.
The exact binary recurrence is c_(j+1)=Xc_j+c_(j-1).
For the companion matrix A=[[X,1],[1,0]], one has A^2=XA+I and c_j=tr(A^j).
The latter identity includes j=0 because tr(I)=0 in characteristic2.
Raising the matrix identity to the dyadic power P_run/2 gives

    A^(P_run)=I+X^(P_run/2)A^(P_run/2).

Since P_run/2>=K, it follows that

    c_(j+P_run)=c_j modulo X^K for every j>=0. (PX15)

This is the low-X part of the already adopted C664 HG7 mechanism; no claim of a minimal period is made.
The polynomials c_1,...,c_(K-1) are monic of their respective degrees, with zero constant term.
Their triangular coefficient matrix therefore makes them a basis of

    V_root=XF_2[X]/X^K,
    dim V_root=K-1=ceil(m/3)-2=v_3.              (PX16)

For j in J_run, the positive indices l_j=d_*-1-j run through P_run consecutive integers in reverse order.
Their residues modulo P_run include every residue, so PX15 shows that their ACTUAL c_(l_j) jets contain in particular the basis jets c_1,...,c_(K-1).
Hence these supported, nonedge c_(l_j) span V_root.

The endpoint n_e=2d_*-5 is odd.
The adopted C734 recurrence calculation gives c_(n_e)=Xu_n with u_n(0)=1; equivalently this follows from the odd-index linear coefficient1 and zero constant term.
Put s=ceil(R/2)=K+1.
The map

    XF_2[X]/X^K -> X^2F_2[X]/X^s,
    v -> c_(n_e)v

is an isomorphism: multiplication by X shifts the valuation by1 and multiplication by the unit u_n is invertible in the truncated ring.
Squaring is then an F_2-linear isomorphism from X^2F_2[X]/X^s onto V_R, because it sends the distinct monomials X^i to X^(2i) and the precise cutoff2i<R is i<s.
Consequently the ACTUAL nonedge columns

    W_j=(c_(n_e)c_(d_*-1-j))^2 modulo X^R,
                    j in J_run,                (PX17)

span all of V_R, with rank v_3.
Projection from R_3 to the smaller R_5 gives the same full-rank conclusion v_5 there.
No free trace coefficient has been substituted for a supported sign, and no individual primitive-root representative has replaced a complete source row.

### PX5. The actual reference target and own-divisor carry

The following explicitly checks the EP10 interface on the new source, rather than treating a support rank as already a canonical solution.
The complete C740/C747 local proof applies at the properties just retained, without its original degree bound: D_*=z^(d_*-1)(U_*/X)(z+z^(-1)) is monic reciprocal with zero central coefficient, since U_*/X vanishes at0 and every positive binary C_j has zero constant term.
The added row is squarefree and prime to Xphi, its indices are coprime to3 and5, and n_e>=d_*+1; these are exactly the full-factor and disjoint-block hypotheses used in C740 WM1--WM10.
The zero-trace carry in C747 MP10--MP14 uses the retained exact order4m-2 at z=1 and the same supported reciprocal mask, not the original numerical degree expense.
Set r_*=2d_*-2 and I={j:0<=j<d_*-1, [z^j]D_*=1}, so |I|=k_* and0,1,2,3 are in I.
For j in I put rho_j=1 on0,1,2,3 and rho_j=-1 otherwise.
Retain the ACTUAL integer reference

    L_ref=sum_(j in I)(z^j+rho_j z^(r_*-j)),
    L_ref^*=z^(r_*)L_ref(z^(-1)),
    P_ref=L_ref+z^(2n_e)L_ref^*,
    T_ref=sum_(j in I)
         (C_(d_e-j)+rho_j C_(d_e-r_*+j)).        (PX18)

Every Chebyshev index is positive since d_e-r_*=d_*-4>0.
The trace T_ref is monic of degree d_e and has binary reduction U_e.
Let alpha_ref be its OWN canonical polynomial a_(T_ref) reduced modulo2.
It is determined by the full source and this exact integer reference, not by a freely chosen target vector.

The unique nonzero even mask at this endpoint is J=1+z^2, with sigma=(1+z)^3(1+z^(n_e)).
For the reference, all eight edge positions have same-sign reciprocal partners and all other supported pairs have opposite signs, giving exactly this sigma.
Every member of the same mask fiber is uniquely

    T=T_ref-2 sum_(j in I,j>0)epsilon_j V_j,
    V_j=C_(d_e-j)+rho_j C_(d_e-r_*+j),
    epsilon_j in{0,1}.                          (PX19)

These are actual height1 signs: in L the change replaces the pair with coefficients (1,rho_j) by (-1,-rho_j), leaving every coefficient supported, of magnitude1, and keeping L(0)=1.
The associated P=L+z^(2n_e)L^* is monic reciprocal of degree2d_e and constant1; the two blocks are disjoint because2n_e>r_*.
The edge signs are eta_j=1-2epsilon_j for j=1,2,3.

For a monic integer T write Delta_T=[T(C_2)-T^2]/2, so its actual canonical a_T is rem_T Delta_T.
For every actual integer V,

    Delta_(T_ref-2V)=Delta_(T_ref)-V(C_2)
                                  +2T_ref V-2V^2. (PX20)

This is an integer identity before reduction or division in a residue ring.
The two monic divisors have the SAME binary reduction U_e; hence reduction of their genuine remainders and c_j(C_2bar)=c_j(X)^2 give

    a_Tbar=rem_(U_e)(alpha_ref+
                         sum_j epsilon_j V_jbar^2).

The Laurent product identity c_n c_l=c_(n+l)+c_(n-l), here n=n_e and l=d_*-1-j, gives V_jbar=c_(n_e)c_(d_*-1-j).
Since X^(2m)|U_e, at any R<=2m the actual affine formula is therefore

    a_Tbar=alpha_ref+sum_j epsilon_j W_j
                                  modulo X^R.    (PX21)

The target and columns really lie in V_R.
Indeed the retained derivative property gives X^(10m)|U_e', because U_e=U_*B_(n_e)^2 and the latter multiplier has derivative0.
Differentiate the integer identity Delta_T=TQ_D+a_T before reducing:

    Delta_T'=XT'(C_2)-TT'.

The two terms on the right have X-orders at least20m+1 and12m after reduction.
In the quotient identity U_e'Q_Dbar+U_e Q_Dbar'+a_Tbar', the first two terms have orders at least10m and2m.
Thus X^(2m)|a_Tbar'; every odd coefficient of a_Tbar below X^(2m) vanishes.
Adopted C747's own-divisor formula a_Tbar=J(1)X^2 modulo X^3 gives X^3|a_Tbar for this even mask.
Together these prove a_Tbar modulo X^(2m) lies in X^4F_2[X^2], including the actual reference alpha_ref.
The column formula gives the same space directly since every positive c_l has zero constant term and c_(n_e) has order1.

### PX6. Exact feasible counts, actual edge signs and residual scope

Fix any one of (++-),(+-+),(-++),(---), equivalently epsilon_1+epsilon_2+epsilon_3=1.
After fixing these three genuine edge bits, the equation is

    sum_(j in I,j>=4)epsilon_j W_j
        =alpha_ref+epsilon_1 W_1+epsilon_2 W_2
                                      +epsilon_3 W_3 in V_(R_p). (PX22)

The right side is the actual edge-adjusted target just proved to be in V_(R_p).
PX17 shows that the map on the k_*-4 nonedge bits is onto and has rank v_p.
Thus every such target is attained, with exactly2^(k_*-4-v_p) solutions by the dimension of the kernel.
The supported run also proves k_*-4>=v_p, so this exponent is nonnegative without a guessed support count.
For the map on all k_*-1 bits with the additional edge-parity output, surjectivity of the nonedge part onto V_(R_p) makes the parity row independent.
Its rank is exactly v_p+1 and its target (alpha_ref,1) has exactly2^(k_*-2-v_p) preimages.

For completeness, the actual edge test has no hidden assumption on the nonedge signs.
With A_edge=1+eta_1z+eta_2z^2+eta_3z^3, the integer half-sum is

    (L+L^*)/2=A_edge+z^(n_e)A_edge^*,
    A_edge^*=z^3 A_edge(z^(-1)).

If zeta^(2n_e)=1, then P(zeta)=2(A_edge(zeta)+zeta^(n_e)A_edge^*(zeta)).
For eta_3=-1 and eta_1=eta_2=eta, the two sums are2eta z(1+z) and2(1-z^3).
For eta_3=1 and eta_1=-eta_2=eta, they are2(1+z^3) and2eta z(1-z).
At zeta^(n_e)=1 the applicable sum has no nonzero zero, and at zeta^(n_e)=-1 the applicable difference has no zero, since n_e is odd.
Therefore each of the four edge patterns has gcd_(Q[z])(P,z^(2n_e)-1)=1 for EVERY nonedge sign choice.
This excludes only factors whose roots satisfy that displayed equation.

All these lifts lie in the same unique nonzero even added mask, so C747's actual local theorem gives BOTH B_(n_e)^2|F_Tbar and B_(n_e)^2|X_(epsilon,T)bar, for either sign epsilon of the second residual.
That application uses its complete monic canonical carry and allows overlap between B_(n_e) and old factors.
The exact old-X calculation is also retained: Tbar has X^(2m), as do Tbar(C_3bar) and Tbar(C_5bar); actual monic remainder and odd division therefore give X^(2m)|b_Tbar,c_Tbar.
Consequently

    F_Tbar=a_Tbar^5 modulo X^(2m),
    X_(epsilon,T)bar=a_Tbar^3 modulo X^(2m).     (PX23)

The conditions in PX5 are exactly the necessary and sufficient old-X conditions for these respective residuals.
Since R_3>=R_5, the p=3 solutions satisfy BOTH old-X conditions and BOTH added-modulus conditions at the actual SAME integer T.
These conclusions are independent of the sign epsilon only at this binary local level.
They are not global coefficientwise evenness of the residual polynomials.

### PX7. Exact costs, maximal powers and retained limits

The actual source expense is

    d_1=d_0+9b_s<=d_0+360Q,
    b_p=15L_src n_star ceil((2d_1-2+P_run)/(30L_src n_star)),
    d_*=d_1+(4m-1)b_p,
    deg Y_*=deg Y+9b_s+(4m-1)b_p,
    deg R_*=deg R_0+9b_s+(4m-1)b_p.             (PX24)

Thus the pre-endpoint gap is EXACTLY g_0, not just positive.
The long-row degree need not be small: it is explicitly paid, rather than absorbed into the old DG8 bound.
From the ceiling formula,

    n_p-1<r_1+P_run+B_step,
    d_*<4m d_1+2m(P_run+30L_src n_star).         (PX25)

Also P_run<=4K<=4m/3<Q/3.
Using L_src=4Q and the optional selected n_star bound in PX2 gives the concrete estimate

    d_*<Q(d_0+360Q)+240Q^4+4800Q^3+(361/6)Q^2. (PX26)

Here (361/6)Q^2 is the sum of60Q^2 from120Q in30L_src n_star and Q^2/6 from P_run; the360Q preliminary term is already inside Q(d_0+360Q).
For example, CONDITIONAL on an input e=2 admissible source actually having d_0<=14400Q^3+1206Q^2+128Q, this implies the new bound d_*<14640Q^4+6006Q^3+549Q^2.
The example does not assert that the original unspecified bounded witness has either admissibility or e=2.
For an already enlarged source use its actual d_0 in PX24--PX26.

The FINAL endpoint trace degree is d_e=3d_*-6 and its full reciprocal degree is2d_e=6d_*-12.
That last B_(n_e)^2 multiplier is selected for the algebraic mask endpoint, not for an unproved full DG3/DG6 invariance.
Accordingly the pre-endpoint canonical formula R_* and gap g_0 are not automatically assigned to its integer lifts.
The old-X and added-modulus conclusions for those lifts are exactly PX23 and C747's local theorem, with the remaining primary equations still open.

Before the endpoint multiplier, the selected exact triple factor retains the actual maximal Frobenius power q after raising U_*,R_* and their full reciprocal binary source by any q=2^j.
The complete synthetic integer row lift gains the full trace degree q(9b_s+rho b_p), with every odd-order factor and multiplicity retained and the same layer vector a_0=12mq, a_b=0 for b>=1.
Its zero normalized Haar integral remains the accepted complete-row statement; it is not the actual integer canonical G.
At the endpoint the same selected factor has odd multiplicity3+2v_(psi_star)(B_(n_e)), so the actual maximal binary power is still1 before raising, even if the extra row overlaps it.
For each dyadic q, the exact height1 support descent and C724/C747 own-canonical covariance give the same finite sign counts at degree2q d_e, with old X-primary X^(2mq) and added modulus B_(n_e)^(2q).
No ascending irreducibility or new precision follows from that substitution.

This proof solves the actual OLD-X affine feasibility problem for a new, explicitly enlarged complete source.
It does not evaluate the original unmodified source's rank or alpha_ref, and it does not imply that every originally admissible e=2 representative already has full rank.
The source support, actual canonical reference and supported height1 signs have been retained throughout; no native computation or J evidence is used.
Reuse checking found the adequate C608/C664 recurrence-period and C734 odd-index inputs, but no fixed support-restricted rank theorem deciding this endpoint.
The additional complete-row support block and its exact rank/count consequence are the new author argument.
All remaining old primaries, full passing residuals, irreducibility and controlled absolute Mahler measure remain separate obligations.
No unrestricted G0001 conclusion is asserted.

### PX8. Actual unconditional source and the paid endpoint family

For each Q=2^ell, ell>=82, choose ANY actual bounded whole-row witness supplied by adopted C691.
Apply [adopted C753 Parts A--D and UC1--UC10](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25), whose selected decision consumes fresh independent whole R973.
Its actual source U_sharp supplies PX1--PX3 with the same original m, H_aux, B_src, beta, Z_0 and selected n_star, all complete factors and DG3/DG6 data, X^(8m)|Y_sharp', exact fresh multiplicity3, and the unchanged positive gap.
In particular E_pre,sharp=0 modulo4 and gcd(2deg U_sharp-5,15)=1 are proved outputs, not assumptions on the uncomputed original witness.
The new source has

    d_0=deg U_sharp<=14400Q^3+1206Q^2+524Q.

Now apply PX2--PX7 to this actual input, including the additional B_(n_s)^9 and B_(n_p)^(4m-1) costs.
All their hypotheses hold at the full new degree; the original selected fresh row is unchanged, so PX2's n_star upper bound is still available.
The source existence and the actual affine sign existence are therefore unconditional within this explicit Q-domain.
The support and reference polynomial remain the actual ones produced by these finite constructions; neither has been replaced by a freely assigned vector.

Substituting the displayed d_0 bound into PX26 gives

    d_*<14640Q^4+6006Q^3+(5665/6)Q^2
        <14640Q^4+6006Q^3+945Q^2,               (PX27)

because524+360+361/6=5665/6.
The FINAL endpoint trace degree is3d_*-6 and its reciprocal degree is6d_*-12, or2q(3d_*-6) after the exact dyadic height1 descent.
For every such source there are exactly the PX6 counts of actual height1 lifts in each of the four indicated edge patterns satisfying the old-X and added-modulus first-bit conditions.
In particular taking p=3 gives an actual nonempty family satisfying both local residual requirements at once and avoiding every factor of z^(2n_e)-1.
The cardinalities are expressed in the ACTUAL support size k_*; no numeric support enumeration is asserted or needed for the nonemptiness and exact formula.

This existence statement still does not solve the remaining old-primary equations or prove irreducibility, full coefficientwise evenness, higher dyadic precision or a total-Mahler estimate.
The complete pre-endpoint source and its further outer multiplier remain distinct exactly as in PX7 and C753 Part D.
The separate proposed all-old-primary mechanism is not a premise or conclusion of this theorem.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision paid-dense-support-old-x-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:51 |
| status | open |
| reason | Register the complete PX1--PX8 author theorem after root read all PX1--PX7 and checked the adopted C753 input and PX27 substitution. Two actual complete invisible rows preserve the full source and create a consecutive block in its genuine low-half support, long enough for a paid low-X Chebyshev period. The actual nonedge height1 columns therefore span the full required old-X space; every genuine reference target and each of four unexcluded edge patterns has the exact stated number of sign solutions. C753 supplies an unconditional source for each Q=2^ell, ell>=82, with the new paid bound d_*<14640Q^4+6006Q^3+945Q^2 and final full reciprocal degree6d_*-12. Actual source properties, original fresh factor, gap, canonical carries, added-modulus conditions, edge gcd and raised scopes are retained. Root and Salem_completion are contributors, not independent reviewers; fresh isolated whole review and adoption remain outstanding. No original unmodified rank, all-old-primary solution, full coefficientwise residual evenness, higher precision, irreducibility, total-Mahler estimate or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete conditional mechanism and unconditional family](#statement) | PX1 exact full-source domain and height1 old-X/added-modulus rank, target, per-edge and combined counts; the complete actual construction and expenses in PX2--PX7; PX8 unconditional C753-consuming existence at every Q>=2^82, precise bound and all local-versus-global exclusions. |
| argument | [Entire dense-support and actual canonical proof](#complete-argument) | Full PX2--PX8 and equations PX7--PX27, with PX1--PX6 definitions: both actual row choices, large-exponent full-source reconstruction, exact support plateau and low-half indices, companion period, supported column span, true reference/carry/derivative jet, affine counts and edge gcd, source/outer degree and raised limits, and paid unconditional application. |
| dependency | [Adopted unconditionally admissible complete source](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25) | Parts A--D and UC1--UC10 supply PX8's actual source with E_pre=0, endpoint gcd15, original full finite/root/forward/derivative/canonical/gap and exact fresh3 data, <=396Q increase and d_0<=14400Q^3+1206Q^2+524Q. Its outer endpoint and remaining rank/primary exclusions are retained. |
| dependency | [Adopted whole-row class and invisible-source extension](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | WR1--WR11 precise pre-fresh exponent convention and z4 class, actual small invisible row and exponent9 admissibility preservation, source reconstruction and complete synthetic-layer interface. The new long row and large exponent4m-1 are verified here and are not imported from its finite exponent lists. |
| dependency | [Adopted explicit reflection and zero-trace mask](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Exact a=d-3 reflection basis, unique nonzero even mask, actual own-divisor X3 jet, local added-modulus conditions, and raised height1 covariance. Its structural proof is reapplied at the retained source order and actual enlarged degree; its old numerical degree bound and global residual success are not presumed. |
| dependency | [Adopted full local height1 carry with overlap](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | WM1--WM10 actual reciprocal support, integer half-sum/carry and added B_n^2 equivalence, allowing old-factor overlap. PX5 verifies its structural inputs on the enlarged source; no arbitrary endpoint source-jet preservation is imported. |
| dependency | [Adopted safe complete-row periods](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | HG7 exact companion identities and full safe B-index period at the original doubled source precision; PX4 uses and explicitly proves only its low-X matrix-period mechanism, not a full-quotient period or native rank. |
| dependency | [Adopted complete original source and expense](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and original selected fresh row: Q/m, complete actual rows, doubled jets, derivative, full canonical R_0, positive gap, exact selected multiplicity3, n_star bound and original costs. Every extension is charged its own new degree. |
| dependency | [Adopted full ordinary-row and synthetic factor mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Complete ordinary/divided row products, both forward maps and full multiplicities, original fresh primitive-order separation, and complete synthetic integer trace-factor/layer interface. No synthetic polynomial is identified with integer canonical G. |
| dependency | [Adopted complete row Laurent identity](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n nonidentity-root partition and exact P_(B_n)=S_n, used for actual padding support and root separation; no native finite certificate, normalized gate or field realization is imported. |
| dependency | [Adopted odd-index Chebyshev coefficients](Yin_C_G0734_v1.md#decision-whole-reviewed-2026-10-25) | Complete trace-factor argument giving positive c_j constant0, odd-index c_j=X times a unit and dyadic recurrence. It supplies no support-restricted rank; that span is proved in PX4. |
| dependency | [Adopted height1 support descent and canonical covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact dyadic substitution P(z^q), trace T(C_q) and own binary canonical covariance, consumed with the actual enlarged endpoint degree and source factors. No ascending irreducibility or higher precision is asserted. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T22:03 |
| status | proved |
| reason | Register the complete PX1--PX8 author theorem after root read all PX1--PX7 and checked the adopted C753 input and PX27 substitution. Two actual complete invisible rows preserve the full source and create a consecutive block in its genuine low-half support, long enough for a paid low-X Chebyshev period. The actual nonedge height1 columns therefore span the full required old-X space; every genuine reference target and each of four unexcluded edge patterns has the exact stated number of sign solutions. C753 supplies an unconditional source for each Q=2^ell, ell>=82, with the new paid bound d_*<14640Q^4+6006Q^3+945Q^2 and final full reciprocal degree6d_*-12. Actual source properties, original fresh factor, gap, canonical carries, added-modulus conditions, edge gcd and raised scopes are retained. Adopt fresh isolated whole R975 after root read the entire PX1--PX8 proof, fixed statement and exact input scopes, then the complete independent finding. Root and Salem_completion remain contributors; the independent reviewer contributed no repair. All actual support, canonical target, rank/count, edge, cost and unconditional-source obligations passed, with the local-versus-global limitations retained. No original unmodified rank, all-old-primary solution, full coefficientwise residual evenness, higher precision, irreducibility, total-Mahler estimate or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete conditional mechanism and unconditional family](#statement) | PX1 exact full-source domain and height1 old-X/added-modulus rank, target, per-edge and combined counts; the complete actual construction and expenses in PX2--PX7; PX8 unconditional C753-consuming existence at every Q>=2^82, precise bound and all local-versus-global exclusions. |
| argument | [Entire dense-support and actual canonical proof](#complete-argument) | Full PX2--PX8 and equations PX7--PX27, with PX1--PX6 definitions: both actual row choices, large-exponent full-source reconstruction, exact support plateau and low-half indices, companion period, supported column span, true reference/carry/derivative jet, affine counts and edge gcd, source/outer degree and raised limits, and paid unconditional application. |
| dependency | [Adopted unconditionally admissible complete source](Yin_C_G0753_v1.md#decision-whole-reviewed-2026-10-25) | Parts A--D and UC1--UC10 supply PX8's actual source with E_pre=0, endpoint gcd15, original full finite/root/forward/derivative/canonical/gap and exact fresh3 data, <=396Q increase and d_0<=14400Q^3+1206Q^2+524Q. Its outer endpoint and remaining rank/primary exclusions are retained. |
| dependency | [Adopted whole-row class and invisible-source extension](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | WR1--WR11 precise pre-fresh exponent convention and z4 class, actual small invisible row and exponent9 admissibility preservation, source reconstruction and complete synthetic-layer interface. The new long row and large exponent4m-1 are verified here and are not imported from its finite exponent lists. |
| dependency | [Adopted explicit reflection and zero-trace mask](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Exact a=d-3 reflection basis, unique nonzero even mask, actual own-divisor X3 jet, local added-modulus conditions, and raised height1 covariance. Its structural proof is reapplied at the retained source order and actual enlarged degree; its old numerical degree bound and global residual success are not presumed. |
| dependency | [Adopted full local height1 carry with overlap](Yin_C_G0740_v1.md#decision-whole-reviewed-2026-10-25) | WM1--WM10 actual reciprocal support, integer half-sum/carry and added B_n^2 equivalence, allowing old-factor overlap. PX5 verifies its structural inputs on the enlarged source; no arbitrary endpoint source-jet preservation is imported. |
| dependency | [Adopted safe complete-row periods](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | HG7 exact companion identities and full safe B-index period at the original doubled source precision; PX4 uses and explicitly proves only its low-X matrix-period mechanism, not a full-quotient period or native rank. |
| dependency | [Adopted complete original source and expense](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and original selected fresh row: Q/m, complete actual rows, doubled jets, derivative, full canonical R_0, positive gap, exact selected multiplicity3, n_star bound and original costs. Every extension is charged its own new degree. |
| dependency | [Adopted full ordinary-row and synthetic factor mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Complete ordinary/divided row products, both forward maps and full multiplicities, original fresh primitive-order separation, and complete synthetic integer trace-factor/layer interface. No synthetic polynomial is identified with integer canonical G. |
| dependency | [Adopted complete row Laurent identity](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n nonidentity-root partition and exact P_(B_n)=S_n, used for actual padding support and root separation; no native finite certificate, normalized gate or field realization is imported. |
| dependency | [Adopted odd-index Chebyshev coefficients](Yin_C_G0734_v1.md#decision-whole-reviewed-2026-10-25) | Complete trace-factor argument giving positive c_j constant0, odd-index c_j=X times a unit and dyadic recurrence. It supplies no support-restricted rank; that span is proved in PX4. |
| dependency | [Adopted height1 support descent and canonical covariance](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Exact dyadic substitution P(z^q), trace T(C_q) and own binary canonical covariance, consumed with the actual enlarged endpoint degree and source factors. No ascending irreducibility or higher precision is asserted. |
| review | [Fresh independent whole paid dense-support review](../audits/reviews/Yin_R_G0975_v1.md#whole-paid-dense-support-finding) | Entire fixed PX1--PX8, every conditional/source and unconditional Q-domain, genuine supported signs and canonical targets, exact ranks/counts, local residual and edge gcd, full source/degree/raised costs and all unresolved global/analytic boundaries; independently reviewed with exact statement and proof bindings. |

