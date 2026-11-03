---
author: Yin
---

# Exact joint matching separation, regular trace action, and the finite error budget

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001/S_G0008 candidate written by assigned AI `entropy_status` for Yin.
Self/contributor checked; complete noncontributor independent AI review and fixed adoption are recorded below.
No new analytic prime theorem or uniform Mahler gap is claimed.
The single actual control reuses the retained Lehmer input; there is no new numerical computation or prime scan.

Reuse the actual Salem kernel from [L162](Yin_L_G0162_v1.md#salem-kernel-class-population), the exact induced/Euler and removal interfaces from [L164](Yin_L_G0164_v1.md#matching-induced-character), the trace construction from [L66](Yin_L_G0066_v1.md#reciprocal-trace-domain), and the actual trace-factor classification from [L161](Yin_L_G0161_v1.md#trace-factor-common-exponent).
No additional external source is used for the proofs below.

<a id="joint-matching-regularity-criterion"></a>
## 1. The exact support question and its answer

Let P be an irreducible Salem polynomial of degree d=2s>=4, K=Q(alpha), F_0=Q(alpha+alpha^(-1)), L its splitting field and G=Gal(L/Q).
Denote the action on the s inverse pairs by H and its kernel by V.
L162 gives V=F_2^s, except that when s is odd it may instead be the even-weight subspace E_s.
For g in G set

    F(g)=number of inverse pairs fixed by g=chi_(F_0)(g),
    M(g)=number of roots sent by g to their own inverses,
    A={g:M(g)>=s}.                                          (1)

The symbols F(g) and F_0 distinguish the observable and the field.
Both F and M are class functions, M is even, and 0<=M<=2F.
Transitivity and L162/L164 give the exact uniform group means

    E_G F=1,                 E_G M=1.                       (2)

A transitive action is called regular if every point stabilizer is trivial, equivalently no nonidentity element fixes any point.
The exact answer to the support question is:

    There is a probability measure nu on the actual G with
    nu(A)=0 and (E_nu F,E_nu M)=(1,1)
    if and only if H is not regular.                        (3)

The measure in (3) may always be chosen conjugacy invariant.
It is not asserted to be an actual Frobenius distribution in any finite or infinite prime range.
The theorem characterizes only what the two specified means can force without further input.

## 2. Full proof in the nonregular case

Suppose H is not regular.
Some h!=1 fixes f>=1 of the s pairs.
A nonidentity permutation moves at least two points, so

    1<=f<=s-2.                                              (4)

Choose any lift g in G.
Multiplying g by elements of V can prescribe the signs independently on these f fixed pairs.
For full V this is immediate.
For E_s the fixed-pair set is proper; any prescribed vector on it extends to an even vector by choosing one coordinate outside it to correct parity.
Thus the projection of V to those f coordinates is surjective.
On a fixed pair, composing with its flip toggles the sign; no moved pair contributes to M.
This proves the following actual choices of lifts, without assuming that G is a split semidirect product.

If f is even, choose a lift with exactly f/2 flipped fixed pairs, so (F,M)=(f,f).
If f is odd, choose two lifts with (f-1)/2 and (f+1)/2 flipped fixed pairs; their respective observables are (f,f-1) and (f,f+1).
Their equal mixture has means (f,f).
Every lift just selected lies outside A, because by (4)

    M<=f+1<=s-1<s.                                         (5)

There is also a derangement in H.
Indeed its transitive fixed-point average is one, while the identity has s>1 fixed points; if all elements had at least one fixed point this average would be larger than one.
Every lift of a derangement has (F,M)=(0,0).
Give total probability 1/f to the selected lift or equal mixture, and probability 1-1/f to such a derangement lift.
All weights are nonnegative, the support avoids A, and both means equal one.
For f=1 the derangement weight is zero and no exception is needed.
Finally average this probability measure under conjugation by G.
The means and the exclusion of A are unchanged because F,M,A are conjugacy invariant.
This proves the forward construction.

<a id="regular-trace-joint-separator"></a>
## 3. Exact regular-case separator and its margin

Suppose H is regular.
Then F(g)=s for g in V and F(g)=0 otherwise; when F=0 also M=0.
On V, M(v)=2wt(v).
The largest value of M on V outside A is exactly

    b=2ceil(s/2)-2                 if V=F_2^s;
    b=4floor((s-1)/4)              if V=E_s (s odd).         (6)

In the second case admissible weights are even and must satisfy 2wt(v)<s; every such weight occurs.
In both cases 0<=b<s, and the maximum is attained, including b=0 when applicable.
Consequently the entire complement obeys

    M(g)<=(b/s)F(g)               for g outside A.           (7)

In fact the convex hull of its observable pairs is exactly the triangle with vertices (0,0),(s,0),(s,b), with a degenerate segment when b=0.
The vertices are realized by a derangement lift, the identity of G, and a kernel vector attaining b.
All other points lie in that triangle by the preceding description.
A measure supported on the complement therefore cannot have means (1,1).
Together with Section 2 this proves both directions of (3).

Put

    c=1-b/s>0,                 a=2-b/s=1+c.                 (8)

The exact separation margin at (1,1) is c.
Its values are 2/s for full V with even s, and 1/s for full V with odd s.
For E_s, it is 1/s when s=1 modulo 4, and 3/s when s=3 modulo 4.
These include s=2 with full V and s=3 with even V, where c=1.
Thus no degree-independent positive precision margin is inferred.

For any probability measure mu on G, regularity also gives

    E_mu M-(b/s)E_mu F<=(d-b)mu(A).                         (9)

Outside A the integrand is nonpositive by (7); on A the element belongs to V, so the integrand is M-b<=d-b.
In particular the exact means (1,1) force mu(A)>=c/(d-b).
The larger upper bound d used here is harmless when E_s lacks the full-flip vector; no sharpness claim is made for this last numerical lower bound.

<a id="regular-joint-finite-prime-budget"></a>
## 4. Finite prime sums and the required analytic precision

Continue to assume regular H.
Let D_K be the absolute field discriminant and x>=2.
As proved in L164, p does not divide D_K exactly when p is unramified in L.
Choose its Frobenius g_p and put

    S_F(x)=sum_(p<=x,p not dividing D_K) F(g_p)log p,
    S_K(x)=sum_(p<=x,p not dividing D_K) chi_K(g_p)log p,
    S_M(x)=2S_F(x)-S_K(x),
    Theta_A(x)=sum_(p<=x,p not dividing D_K,g_p in A)log p.

The pointwise separator (9), without normalizing prime weights, implies

    T(x):=S_M(x)-(b/s)S_F(x)=a S_F(x)-S_K(x)
         <=(d-b)Theta_A(x).                                (10)

For a number field E let psi_E be its exact Dedekind prime-power sum, with every finite prime ideal included as in L164.
Put

    R_K(x)=sum_(p<=x,p dividing D_K)log p,
    B_F(x)=s sqrt(x)log x+s R_K(x).

The same elementary coefficient bound and prime-power count as L164, now with degree s, give

    0<=psi_(F_0)(x)-S_F(x)<=B_F(x),
    0<=psi_K(x)-S_K(x).                                    (11)

The first removal uses the common excluded set p|D_K, including primes unramified in F_0 but ramified in K.
Its contribution is still at most s R_K.
The second inequality needs no upper removal estimate.
In particular no cancellation between omitted coefficients is presumed.

If separate proved analytic estimates give |psi_(F_0)(x)-x|<=E_F(x) and |psi_K(x)-x|<=E_K(x), then

    T(x)>=c x-a E_F(x)-E_K(x)-a B_F(x),
    Theta_A(x)>=max(0,[c x-a E_F(x)-E_K(x)-a B_F(x)]/(d-b)). (12)

To check the sign of every removal, substitute S_F=psi_(F_0)-L_F and S_K=psi_K-L_K, with L_F<=B_F and L_K>=0.
Then T=a psi_(F_0)-psi_K-a L_F+L_K, proving (12).
Strict positivity of its numerator is a finite sufficient test for a matched prime p<=x.
It does not by itself give the stronger L162 budget p<=B d log p for a common B; any transfer to that budget must keep the actual selected p and all small-prime cases.

No error functions E_F,E_K are proved in this source, and no ERH assumption is silently inserted.
A later source-specific comparison can substitute its stated estimates into (12).
The exact margin c, degree s in B_F, common ramification set and the one-sided use of the K removal must then remain.
Replacing c by a positive absolute constant or silently dropping the prime-power cost is invalid.

<a id="lehmer-nonregular-joint-control"></a>
## 5. One actual nonregular trace action

The retained Lehmer polynomial is

    P(t)=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.

Writing P(t)=t^5 T(t+t^(-1)) gives, directly from the expressions for t^j+t^(-j),

    T(z)=z^5+z^4-5z^3-5z^2+4z+3,
    T(z)=z(z^4+z^3+z^2+z+1)=z Phi_5(z) modulo 3.          (13)

The multiplicative order of 3 modulo 5 is four: 3^2=-1 mod5 and 3^4=1 mod5.
The four primitive fifth roots therefore form one Frobenius orbit over F_3, so Phi_5 is irreducible there.
It is separable since 3 does not divide 5, and its constant term is one, so the factor z is disjoint.
Also T(1)=2 and T(-1)=2 modulo 3.
Thus T is squarefree and T(2)T(-2) is nonzero modulo3; L66's discriminant identity proves that p=3 is good for P.
This agrees with the retained mod-3 data in [J11](../computations/programs/Yin_J_G0011/readme.md) and [L159](Yin_L_G0159_v1.md#actual-isolated-linear-return-certificate), which were read rather than rerun.

Hence the actual trace-group Frobenius at 3 has cycle type 1+4 on five points.
In particular it is nonidentity with f=1 fixed pair, and the actual H is not regular.
The construction in Section 2 specializes to two actual lifts with (F,M)=(1,0) and (1,2); their equal mixture has joint means (1,1) while both lie outside A={M>=5}.
This assertion concerns actual elements of this input's G, and requires no determination of the entire Galois group or an assumption about which of these lifts is the specific Frobenius at 3.
It is not an actual prime-distribution counterexample or a family approaching Mahler measure one.

## Scope and contributions

The two-mean discriminator is now complete: regularity of the actual trace action is exactly the condition under which these two expected means alone separate the large-matching set.
On a nonregular trace action, stop this exact two-mean-only transfer; it needs additional arithmetic, another observable, or more joint information.
On a regular trace action, the finite test (12) is valid but its analytic precision and prime/exponent budget remain to be filled.
Neither branch resolves sufficiently-near-one coverage or substitutes Salem inputs for unrestricted G0001.

The coordinator proposed the regular-case discriminator and a one-fixed-pair diagnostic, and supplied the one-sided finite prime-sum transfer in Section 4.
The assigned entropy_status AI derived and checked the exact regular-if-and-only-if criterion, the arbitrary-fixed-count nonregular construction, the precise full/even-kernel margins, and the Lehmer mod-3 control, and checked the coordinator's finite transfer before assembly.
These are contributor checks, not independent review.
No source acquisition, new numerical run or canonical edit was performed for this proof.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0064_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
