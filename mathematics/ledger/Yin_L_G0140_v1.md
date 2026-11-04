---
author: Yin
---

# Summable central-mode energy charges on actual zero-defect gaps

Current checking scope is owned by [R44](../audits/reviews/Yin_R_G0044_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-08.
Direct bounded G0001 derivation by the assigned execution_and_deliverables AI for Yin.
The coordinator requested actual realizability information beyond a support count and the empty-collar condition.
The coordinator and entropy_status AI investigated the exact P/(t-beta) boundary flux in parallel and checked its normalization.
This branch derives a finite filtered Gramian inequality and the coupled weighted-variance charge below.
No mathematical computation, optimization or source acquisition has been executed.
The complete written proof received the recorded checks below, at the responsible findings' actual relationships.

The used fixed interfaces are the [finite-cluster proof](Yin_L_G0135_v1.md#explicit-finite-energy-coercivity-radius), the [exact sparse threshold search](Yin_L_G0136_v1.md#sparse-energy-threshold-decision), the [actual long-window control](Yin_L_G0137_v1.md#actual-salem-bounded-energy-window), and the [all-central norm and abstract collar boundary](Yin_L_G0138_v1.md#all-central-coercivity-radius).
The inequalities below are derived directly for the actual finite recurrence.

## Finite data and exact root factors

Use the positive-Mahler irreducible algebraic-unit domain of [L G0130](Yin_L_G0130_v1.md#finite-rational-energy-coercivity).
Thus P is a monic irreducible polynomial in Z[t] of degree d with constant coefficient plus or minus one and M(P)>1.
It has distinct nonzero roots, and q>0 of them lie on the unit circle.
Count both members of each complex pair.
Put h=d-q and factor over the algebraic numbers

    C(t)=product_(|beta|=1)(t-beta),
    Q(t)=product_(|gamma|!=1)(t-gamma),
    P=CQ,   deg C=q, deg Q=h,
    W_Q=sum_(i=0)^h |[t^i]Q|.                            (1)

Both factors have real algebraic coefficients, since their root sets are invariant under conjugation.
W_Q>0.
No uniform bound on its size or on root separation is assumed.

Let R>=0 be an integer and x a real vector on I_R={-R,...,R+d}.
Set

    z_t=(P(S)x)_t,  -R<=t<=R,
    E=sum_(t in I_R) x_t^2,   (Sx)_t=x_(t+1).            (2)

The gap identities do not require integrality or the box.
Their application to E_R uses the original constraints |x_t|<=1/2, integer z_t, and z_0!=0 without relaxing any of them.

Choose ordered nonempty integer gaps

    G_j=[u_j,v_j] subset [-R,R],   0<=j<=p,
    v_j<u_(j+1),   z_t=0 for every t in G_j.

Their raw coordinate intervals are disjoint.
Write L_j=v_j-u_j+1 and T_j=max(L_j-h,0).
Energy will be charged only to x-coordinates in these raw gaps, not to overlapping d-coordinate boundary tails.

On G_j the recurrence implies a unique homogeneous representation

    x_t=sum_(P(gamma)=0) c_(j,gamma) gamma^t,
                   u_j<=t<=v_j+d.                       (3)

Indeed choose the d coefficients from the first complete state (x_(u_j)...,x_(u_j+d-1)) using its invertible Vandermonde matrix; the monic recurrence continues it through v_j+d.
Nonzero roots allow the global exponent convention gamma^t.
For each central root define

    a_(j,beta)=Q(beta)c_(j,beta),
    a_j=(a_(j,beta))_(|beta|=1) in C^q.                  (4)

These actual amplitude vectors have conjugate symmetry.
Later minimization over all complex vectors merely relaxes that symmetry and therefore remains a valid lower bound.

<a id="filtered-gap-energy-charge"></a>
## 1. A finite Gramian charges each actual gap

Enumerate the central roots beta_1,...,beta_q.
For T>=0 let

    (G_T)_(i,k)=sum_(t=0)^(T-1) overline(beta_i)^t beta_k^t,
    g_T=lambda_min(G_T),
    D_C=max_i sum_(k!=i) 2/|beta_i-beta_k|.              (5)

G_0 is the zero matrix.
Every G_T is Hermitian positive semidefinite; it is positive definite for T>=q because the q by q initial Vandermonde block is invertible.
Geometric sums give diagonal entries T and off-diagonal absolute values at most 2/|beta_i-beta_k|.
Hence

    g_T>=max(T-D_C,0).                                  (6)

For gap j with L_j>h, apply the hyperbolic annihilator Q(S) only at indices t=u_j,...,v_j-h.
By (3),

    (Q(S)x)_t=sum_(|beta|=1) a_(j,beta) beta^t.          (7)

There are exactly L_j-h=T_j such indices.
Every input coordinate t,...,t+h is in [u_j,v_j].
Thus weighted Cauchy--Schwarz and then summing the shifted coordinate energies give

    sum_(t=u_j)^(v_j-h) |(Q(S)x)_t|^2
       <= W_Q^2 sum_(t=u_j)^(v_j) x_t^2.                (8)

For example, coordinatewise |sum_i Q_i x_(t+i)|^2 is at most W_Q sum_i |Q_i| |x_(t+i)|^2.
Each shifted sum in (8) lies within the same raw gap, which proves the stated bound without borrowing any adjacent-gap energy.

Changing the start index from zero to u_j conjugates G_(T_j) by a diagonal unitary matrix.
Equations (7)--(8) therefore imply

    sum_(t in G_j) x_t^2 >= w_j ||a_j||_2^2,
    w_j=g_(T_j)/W_Q^2
       >=max(L_j-h-D_C,0)/W_Q^2.                        (9)

If L_j<=h, define w_j=0; then (9) is the trivial nonnegative bound and no filter output is used.
Summing disjoint raw gaps gives the actual finite-energy constraint

    E>=sum_(j=0)^p w_j ||a_j||_2^2.                     (10)

All filter indices, d-coordinate recurrence states and shortened Gramian lengths are retained.
In particular no double counting of overlapping recurrence-state tails occurs in (10).

<a id="integer-cluster-central-amplitude-jump"></a>
## 2. Every intervening integer defect enters the amplitude jump

For a central root beta put

    Q_beta(t)=P(t)/(t-beta),
    F_beta(t)=(Q_beta(S)x)_t.

Here the second use of t is an integer sequence index.
The polynomial identity (S-beta)Q_beta(S)=P(S) gives, for every -R<=t<=R,

    F_beta(t+1)-beta F_beta(t)=z_t.                      (11)

The state needed for F_beta(t+1) ends at t+d, which is available in I_R.
On homogeneous gap j, (3) and Q_beta(gamma)=0 for every other root give

    F_beta(t)=P'(beta)c_(j,beta) beta^t,
                        u_j<=t<=v_j+1.

Since P'(beta)=Q(beta)C'(beta), the normalized boundary flux beta^(-t)F_beta(t)/C'(beta) is precisely a_(j,beta).
Telescoping (11) between the end state of one gap and the start state of the next therefore gives

    a_(j,beta)-a_(j-1,beta)
      = [sum_(t=v_(j-1)+1)^(u_j-1)
                     z_t beta^(-t-1)]/C'(beta)
      =: Delta_(j,beta),                 1<=j<=p.        (12)

Every intervening defect is included.
Zero defects may remain inside that sum; no cluster partition or omission is assumed.
When the raw gaps are adjacent the sum is empty and the jump is zero.
All its recurrence indices lie in [-R,R].
At the two cut states the vectors end at v_(j-1)+d and u_j+d-1, respectively, both within the original available interval.

The phases beta^(-t-1) and the denominator C'(beta) are essential.
There is no extra P'(beta), inverse-Vandermonde, or hyperbolic factor left after the amplitude normalization (4).

<a id="summed-gap-weighted-variance"></a>
## 3. The coupled charge and the independent-charge accounting boundary

Put S_0=0, S_j=sum_(i=1)^j Delta_i, and W=sum_j w_j.
Then the actual amplitudes satisfy a_j=a_0+S_j.
If W>0, completing the square in the common unknown a_0 gives the exact identity

    sum_j w_j ||a_0+S_j||_2^2
      =W ||a_0+S_bar||_2^2
         +(1/W) sum_(i<j) w_i w_j ||S_i-S_j||_2^2,
    S_bar=(1/W)sum_j w_j S_j.

Consequently every actual x under the finite hypotheses obeys

    E >= (1/W) sum_(i<j) w_i w_j ||S_i-S_j||_2^2.        (13)

If W=0 the supplied bound is simply zero.
Formula (13) is independent of any assumed initial central amplitude: it has minimized that amplitude while retaining every relative jump.
For an integer-defect candidate z, the right side is determined by P, the selected gaps, and those actual intervening defects.

For just two gaps with positive weights this reduces to

    E >= [w_0 w_1/(w_0+w_1)] ||Delta_1||_2^2.            (14)

One must not sum (14) over all adjacent pairs without charging shared gaps.
Direct summation of the pair inequalities gives only the universally valid consequence

    E >= (1/2) sum_(j=1)^p
            [w_(j-1)w_j/(w_(j-1)+w_j)] ||Delta_j||_2^2,

where a term is zero if both its weights are zero.
Each internal gap was charged at most twice; the endpoint gaps were charged once.
The global variance (13) avoids this repeated accounting by doing the single common-offset minimization directly.

An exact matrix version can preserve more information than the smallest eigenvalues in (9).
Define positive semidefinite matrices

    (H_j)_(i,k)=(1/W_Q^2)
        sum_(t=u_j)^(v_j-h) overline(beta_i)^t beta_k^t,

with H_j=0 when L_j<=h.
Equations (7)--(8) give E>=sum_j a_j^* H_j a_j.
If H=sum_j H_j is positive definite, put b=sum_j H_j S_j.
Completing the same square gives

    E >= sum_j S_j^* H_j S_j - b^* H^(-1)b.             (15)

For a singular H the same statement holds with its Moore--Penrose inverse: every vector in ker H lies in each ker H_j, so it is orthogonal to b and the square completion on range H is valid.
This is a finite algebraic quadratic form, not a claim that it has been evaluated or that its root-separation costs are small.

<a id="nonzero-cluster-two-gap-energy-bound"></a>
## 4. A nonzero algebraic residue gives an explicit two-gap charge

Suppose the interval between two gaps is [a,b], with ell=b-a>=0, and contains integer defects.
Let

    Z_c(t)=sum_(j=a)^b z_j t^(b-j),
    A_c=sum_(j=a)^b |z_j|,
    D_*=product_(|beta|=1) |C'(beta)| >0.

Assume P does not divide Z_c.
In particular A_c>=1.
Equation (12) becomes

    Delta_beta=beta^(-b-1) Z_c(beta)/C'(beta).

Irreducibility makes every conjugate value Z_c(gamma) nonzero.
Their product is a nonzero integer.
At the h hyperbolic roots, |Z_c(gamma)|<=A_c max(1,|gamma|)^ell.
Thus

    product_(|beta|=1) |Z_c(beta)| >= A_c^(-h) M^(-ell),
    ||Delta||_2^2 >= q D_*^(-2/q)
                           A_c^(-2h/q) M^(-2ell/q),      (16)

where M=M(P).
The second inequality is the arithmetic--geometric mean inequality applied to the q numbers |Delta_beta|^2.
D_* is the absolute discriminant of the central factor C; its coefficients need not be integers, so no integer-discriminant lower bound is being asserted.

If both raw gaps have length at least L>h+D_C, (9), (14) and (16) give

    E >= (L-h-D_C)/(2W_Q^2)
                 q D_*^(-2/q) A_c^(-2h/q) M^(-2ell/q).  (17)

In particular a feasible energy-at-most-B vector with this nonzero residue cannot have both gap lengths greater than

    h+D_C+(2B W_Q^2/q) D_*^(2/q)
                                A_c^(2h/q) M^(2ell/q).   (18)

These bounds retain the exact central root separations, the hyperbolic filter coefficient norm, cluster span, actual integer coefficient mass, and every finite filter endpoint.
They provide an actual energy charge even before imposing the box.
In the original finite-energy problem one may additionally use its proved integer bound A_c<=floor(||P||_1^2 B), but it is not substituted for actual A_c in (16)--(18).

## Scope and the unresolved residue-zero branch

For a nonzero integer Z_c, its amplitude jump vector is zero if and only if P divides Z_c.
One direction follows immediately from (12).
For the other, vanishing at one central algebraic conjugate implies divisibility by its irreducible minimal polynomial P.
This is a real kernel of the central certificate: a nonzero integer polynomial such as P has zero central residue.
No feasible cube response for such a prescribed cluster is being asserted.
The integer response and hyperbolic endpoint information must still be used if a proposed proof needs to exclude it.

Likewise one observed gap alone permits the unknown common central amplitude to cancel in (13).
Several clusters may cancel their cumulative jumps before a later heavily weighted gap.
The complete variance or matrix expression retains these correlations; a free positive charge for each nonzero defect or each abstract cluster does not follow.

The new statements concern actual finite x and disjoint pieces of its energy, with exactly computed transitions between them.
They are not the abstract support-placement model of L G0138 and do not repeat the long bounded-energy witness of L G0137.
They can add a valid lower bound to an actual integer-defect candidate in the sparse L G0136 search, including a rejection if (13) or (15) exceeds the permitted energy B.
Completeness of such a rejection still requires the original exhaustive defect handling; this additional bound does not make a selected sample exhaustive.

No theorem is supplied here that these charges are uniformly large enough on every near-one input or on every permitted integer-defect pattern.
In particular no logarithmic lower growth for E_R, practical exact search, transition-product lower bound, or Mahler gap has been obtained.
The remaining useful question is whether nonzero residues or the residue-zero hyperbolic branch can be controlled at the actual early windows.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0044_v1.md#contributions-and-review), with its original inspected scope and relationship.
