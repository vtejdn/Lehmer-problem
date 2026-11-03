---
author: Yin
---

# G0001 exploration: integer orbit Gram determinants

Date: 2026-10-06.
Owner: assigned trajectory agent for Yin, with the coordinating and separate reviewing agents identified below.
Scope: preserved exploratory research-operation record for [S G0001](../strategies/Yin_S_G0001.md).
This is not a canonical Claim or a solution of Lehmer; execution monitoring belongs to the run record.
The complete precise finite theorem and limits are now in [C209](../claims/Yin_C_G0209_v1.md#statement), and all three original programs and outputs have their native home in [J114](../computations/programs/Yin_J_G0114/readme.md).
The original mathematical and native blocks below remain the fixed historical inputs used by their actual earlier reviewers and by the programs' literal self-read paths.

## First-batch outcome and freeze

First batch fixed on 2026-10-06.
A finite lower certificate was proved with its full boundary penalty:
\[
m(p)\ge\frac{\log\bigl(|\operatorname{disc}p|\det(V_NV_N^{\mathsf T})\bigr)-d\log N}{2(N-1)}.
\]
The exhaustive coefficient-pattern loop covered 1,092 monic reciprocal patterns in even degrees 2--12 with independent coefficients in \(\{-1,0,1\}\).
Within that fixed loop, **386 noncyclotomic irreducible polynomials** obtained direct finite-field certificates, and **206 additional** such polynomials obtained trace-polynomial certificates: **592 certified core examples** altogether.
Another **23 were certified cyclotomic**; **477 had neither sufficient certificate and remain unclassified**.
This is not a complete irreducibility enumeration.

All 592 certified core examples passed \(\Delta G_{2d}>(2d)^d\); **zero positivity failures** were found.
The stronger \((\log2)/8\) certificate at the same window failed for **16 examples** (10 of degree 10, 6 of degree 12).
Lehmer is one: \(\Delta=1332031009=36497^2\), \(G_{20}=79461\), so positivity passes but that fixed threshold fails; \(G_{40}=18006972477\) passes the threshold.
Exact code, inputs and outputs appear below.
No assertion extends to the 477 unclassified cases or to degrees above 12.

The finite inequality is useful for individual certification.
A positive integer surplus at \(N=2d\), even if eventually proved universal, has only a vanishing degree-dependent minimum.
The missing uniform conclusion requires an exponential surplus over \(N^d\).
This batch does not establish it.

## 1. Reuse and the exact question

The primary domain is monic irreducible reciprocal noncyclotomic unit polynomials \(p\in\mathbb Z[t]\), with unbounded degree \(d\).
The lattice is \(L_p=\mathbb Z[t]/(p)\cong\mathbb Z^d\), basis \(1,t,\ldots,t^{d-1}\); \(A\) is multiplication by \(t\).
The constant coefficient \(\pm1\) makes \(A\in\mathrm{GL}_d(\mathbb Z)\).
Natural-log algebraic entropy satisfies
\[
h_{\rm alg}(A)=m(p)=\log M(p)
\]
by the already accepted [GBV15 rational formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) and [DGB16 rationalization](../audits/literature/DGB16/Yin_U001.md#pure-essential-hull).
Their existing proof-inspection limits remain unchanged.

The [prior assessment](Yin_L_G0001_v1.md#lehmer-route-assessment) already excludes generic length-function capture and fixed finite-ball lower-bound reasoning.
The immediate question here is more concrete: can a computable integer orbit volume give a finite, directionally valid lower certificate for entropy, and what degree cost does it incur?

Local reuse found two adequate mechanisms:

- [Den09-U002](../audits/literature/Den09/Yin_U002.md#finite-section-determinant): Toeplitz determinants, their Schur-complement residuals, and the retained classical Szegő limit.
  This supplies the limiting interpretation, not a positive arithmetic gap.
- [Smy08-U003](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation): the Vandermonde/Hadamard discriminant estimate \(|\operatorname{disc}p|\le d^dM(p)^{2d-2}\).
  The estimate below extends that same elementary mechanism to a rectangular orbit matrix.

The uniform-closure and shared-structure method entries are used only as diagnostics: retain the degree-dependent error, and compare the same polynomial relation on the trajectory and relation-lattice sides.
No uniform bound is imported from those methods.

A bounded primary search for “Toeplitz banded determinant Schur polynomial roots polynomial” located Per Alexandersson's 2012 paper, *Schur polynomials, banded Toeplitz matrices and Widom's formula*, arXiv:1208.5607 / DOI 10.37236/2651, as a related attribution lead.
Its abstract and publisher search extract identify the Toeplitz-minor/Schur connection; its full proof was not read and it is **not a premise** below.
A second bounded query for “Mahler measure Gram discriminant polynomial” supplied no needed stronger interface.
The local Hadamard argument suffices, so searching stopped.
No novelty claim or new source acquisition/registration is made.

## 2. Orbit matrix and its exact integer relation lattice

The next calculations hold more generally for every **monic squarefree** \(p\in\mathbb Z[t]\) of degree \(d\ge1\), with \(p(0)\ne0\).
Unit and reciprocity are needed for the target family, not for these identities.
Put
\[
v_j=t^j\bmod p\in\mathbb Z^d,\qquad
V_N=[v_0\;v_1\;\cdots\;v_{N-1}],\quad N\ge d,
\]
\[
W_N=V_NV_N^{\mathsf T},\qquad G_N=\det W_N\in\mathbb Z_{>0},
\qquad \Delta=|\operatorname{disc}p|\in\mathbb Z_{>0}.
\]
The first \(d\) columns of \(V_N\) are the identity.
In particular this is a primitive quotient map of integer lattices.
It is not the cardinality of a binary-digit trajectory.

Write \(k=N-d\).
The kernel of \(V_N:\mathbb Z^N\to\mathbb Z^d\) has the basis consisting of the coefficient vectors of
\[
p,tp,\ldots,t^{k-1}p.
\]
Indeed monic polynomial division gives an integral quotient for every polynomial divisible by \(p\); degree bounds give exactly those shifts.
Let \(K_k\) be the \(N\times k\) matrix of these columns.
The bottom \(k\times k\) block is triangular with diagonal 1, so this is a saturated integral kernel, not a finite-index substitute.

The **finite dual Gram identity** is
\[
G_N=\det(K_k^{\mathsf T}K_k)=:D_k,\qquad D_0=1. \tag{1}
\]
For a direct verification write \(V_N=[I_d\ B]\).
A standard kernel basis is \(K_0=[-B;I_k]\), so
\(\det(K_0^{\mathsf T}K_0)=\det(I_k+B^{\mathsf T}B)=\det(I_d+BB^{\mathsf T})\).
The actual polynomial-shift basis differs by an integral unimodular matrix, by the triangular block above; its Gram determinant is unchanged.
This proves (1) without a lattice covolume theorem.

Thus the trajectory's integer recurrence and an integer Toeplitz determinant encode exactly the same finite object.
If \(p(t)=\sum_{j=0}^d a_jt^j\), then
\[
(K_k^{\mathsf T}K_k)_{ij}=\sum_\ell a_\ell a_{\ell+i-j},
\]
where missing coefficients are zero.
This is the Toeplitz section for \(|p(e^{it})|^2\), including when \(p\) has unit-circle zeros.

<a id="gram-lower-certificate"></a>
## 3. A finite integer lower certificate, with its full dimension cost

Let \(\alpha_1,\ldots,\alpha_d\) be the distinct roots of \(p\), and let
\(E=(\alpha_i^j)_{i=1,\ldots,d;\ j=0,\ldots,d-1}\).
Then \(EV_N=(\alpha_i^j)_{i;\ j=0,\ldots,N-1}\), because reduction modulo \(p\) preserves evaluation at its roots.
Taking Hermitian Gram determinants gives
\[
\Delta G_N
=\det\bigl((EV_N)(EV_N)^*\bigr)
\le \prod_{i=1}^d\sum_{j=0}^{N-1}|\alpha_i|^{2j}
\le N^d M(p)^{2(N-1)}. \tag{2}
\]
Here the first equality uses \(|\det E|^2=\Delta\), the first inequality is Hadamard, and the second bounds each finite geometric sum by \(N\max(1,|\alpha_i|)^{2(N-1)}\).
Every conjugate, including contracting and unit-circle conjugates, is retained.
Repeated roots are excluded because the Vandermonde determinant would vanish.

Consequently, for \(N\ge d\) and \(N>1\),
\[
h_{\rm alg}(A)=m(p)
\ge B_N(p):=
\frac{\log(\Delta G_N)-d\log N}{2(N-1)}. \tag{3}
\]
At \(N=d\), this is exactly the known discriminant lower estimate.
At longer windows \(G_N\) adds genuine orbit information.
A negative value is merely vacuous; taking its positive part is valid since \(m(p)\ge0\).

In particular, the following checks use **only positive integers**, not approximated algebraic roots:

- \(\Delta G_N>N^d\) certifies strictly positive entropy.
- \((\Delta G_N)^4\ge N^{4d}2^{N-1}\) certifies \(m(p)\ge(\log2)/8\).
- More generally, \((\Delta G_N)^b\ge N^{bd}a^{N-1}\), with integers \(a>1,b>0\), certifies \(m(p)\ge(\log a)/(2b)\).

These are sufficient finite tests.
They do not assert that a fixed threshold is met for every noncyclotomic \(p\).
The subtraction \(d\log N\) is indispensable.

## 4. What finite increments can and cannot say

By Den09's retained Toeplitz limit,
\[
\lim_{k\to\infty}D_k^{1/k}=M(p)^2.
\]
The Schur-complement residual interpretation also gives
\[
r_k:=D_k/D_{k-1}\quad\text{nonincreasing in }k,
\qquad r_k\longrightarrow M(p)^2. \tag{4}
\]
To check monotonicity, the residual norm of \(t^{k-1}p\) after projection on \(p,tp,\ldots,t^{k-2}p\) equals \(r_k\).
Multiplication by \(t^{-1}\) is an isometry on the coefficient Hilbert space.
The corresponding residual at the next step has an additional predecessor available for projection, so cannot increase.
The limit follows by taking the geometric mean of the positive decreasing ratios and applying the retained Toeplitz limit.

For a nonconstant **monic** polynomial with nonzero constant coefficient, in fact \(r_k>1\): the residual is \(p(t)q(t)\), where \(q\) is monic of degree \(k-1\); this product is monic, so its squared coefficient norm is at least 1.
Equality would make it the monomial \(t^{k+d-1}\), impossible since \(p\) has a nonzero root.
Because \(D_k\) are integers, \(D_k\ge D_{k-1}+1\).
Yet these facts alone imply no positive limiting entropy.
They hold, for example, for \(p=t-1\), where \(D_k=k+1\), \(r_k=(k+1)/k>1\), and entropy is zero.

Thus a finite residual supplies an **upper** estimate
\(m(p)\le\tfrac12\log r_k\), not a lower estimate.
Formula (3) is the complementary lower estimate, bought by the explicit discriminant/dimension boundary term.
The interval is a finite certificate for an individual polynomial, not a degree-uniform theorem.

The even coarser subgroup-index candidate fails already on the exact hard core.
The subgroup generated by \(v_0,\ldots,v_{N-1}\) is all of \(\mathbb Z^d\) as soon as \(N\ge d\), so every subsequent index is 1, including for \(p=t^2-3t+1\) with positive entropy.
Passing from finite sets to their generated subgroups destroys the needed metric information.

Nor can \(G_N^{1/2}\) be substituted for a binary trajectory cardinality.
For \(p=t^2-at+1\), \(N=3\), one has \(G_3=a^2+2\), while \(T_3(A,\{0,v_0\})\) has at most 8 elements.
Taking \(a=8\) already gives \(\sqrt{G_3}>8\).
This is a reciprocal irreducible unit example.
A comparison to digit counts needs an additional quantization or boundary argument and a declared digit set.

<a id="degree-window-tests"></a>
## 5. Degree-scale candidate and controls

The tested strong short-window candidate is: **every irreducible reciprocal noncyclotomic unit polynomial passes the \((\log2)/8\) certificate at \(N=2d\)**.
The retained exact Lehmer polynomial fails this integer test at \(N=20\), although it passes the weaker positivity test there and passes the \((\log2)/8\) test at \(N=40\).
Thus that universal fixed-threshold, fixed-window sufficient mechanism is false; this is not a refutation of (2), or a proof that the polynomial's true entropy is below the threshold.

The weaker candidate \(\Delta G_{2d}>(2d)^d\) survives the first named samples and is investigated separately below.
Even if it held throughout the core, the minimum integer surplus would give only \(\log(1+(2d)^{-d})/[2(2d-1)]\), which tends to zero.
A uniform gap requires an exponential surplus, not merely a strict integer inequality.

The diagnostic is compatible with time dilation.
If \(q\) is monic squarefree with constant coefficient of modulus one, \(p(t)=q(t^r)\), \(d=r\deg q\), and \(N=rL\), then direct separation into exponent residue classes gives
\[
G_{rL}(q(t^r))=G_L(q)^r,\qquad
|\operatorname{disc}(q(t^r))|=r^d|\operatorname{disc}q|^r,
\]
and therefore
\[
\log(\Delta_pG_{rL})-d\log(rL)
=r\bigl[\log(\Delta_qG_L)-(\deg q)\log L\bigr]. \tag{5}
\]
The Gram identity follows by permuting the orbit coordinates into \(r\) identical blocks.
For the discriminant identity use \(p'(\alpha)=r\alpha^{r-1}q'(\alpha^r)\) and take the product over all roots; unit constant terms remove the absolute-value factor \(\prod|\alpha|^{r-1}\).
No irreducibility of \(q(t^r)\) is asserted.
The \(r^d\) term precisely cancels the added \(d\log r\) boundary penalty.
Thus this normalization does not spuriously divide entropy by the dilation factor.

Cyclotomic controls are sharper.
For \(p=\Phi_\ell\) with \(\ell\) prime and \(N\) a positive multiple of \(\ell\), the rows \((1,\alpha_i,\ldots,\alpha_i^{N-1})\) are pairwise orthogonal and each has squared norm \(N\).
Hence \(\Delta G_N=N^d\) exactly, so (3) returns zero, not a false positive.
For other cyclotomic windows it remains nonpositive by (2).

The nonunit family \(t^d-2\) still has entropy \(\log2\), despite its house approaching one; (2) applies because the polynomial is monic squarefree.
The nonintegral \(2t-1\) is outside this lattice model and requires GBV15's leading-coefficient term.
Weighted semisimple length countermodels have no integral companion-polynomial norm/discriminant data, so this argument is not being applied to their arbitrary weights.
Infinite direct sums of zero-entropy flows are also outside this single finite-rank orbit calculation; nothing here claims their whole group has finite rank.

## 6. Reproducible finite computation

The following is the complete script.
It uses Python standard-library exact integers and Fraction, with no roots, floating point, randomness or external package.
It computes the discriminant by a Sylvester resultant and Bareiss elimination, builds the orbit Gram determinant independently, cross-checks (1) against the relation matrix for small windows, and tests the exact integer certificates.
The decisive inputs and printed output are retained here.
Execution status and results are appended after running this exact block.

```python
from fractions import Fraction
from math import comb
import json, sys

def det(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0: return 1
    sign, old = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j], a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % old == 0
                a[i][j] = num//old
        for i in range(k+1,n): a[i][k] = 0
        old = pivot
    return sign*a[-1][-1]

def resultant(f,g):
    m,n = len(f)-1,len(g)-1
    f,g = f[::-1],g[::-1]
    a = [[0]*(m+n) for _ in range(m+n)]
    for i in range(n): a[i][i:i+m+1]=f
    for i in range(m): a[n+i][i:i+n+1]=g
    return det(a)

def disc(p):
    d=len(p)-1
    return abs(resultant(p,[i*p[i] for i in range(1,d+1)]))

def gram(p,N):
    d=len(p)-1
    assert p[-1]==1 and N>=d
    v=[1]+[0]*(d-1)
    W=[[0]*d for _ in range(d)]
    for _ in range(N):
        for i in range(d):
            for j in range(d): W[i][j]+=v[i]*v[j]
        lead=v[-1]
        v=[-lead*p[0]]+[v[i-1]-lead*p[i] for i in range(1,d)]
    return det(W)

def relation_gram(p,k):
    d=len(p)-1
    K=[[p[i-j] if 0<=i-j<=d else 0 for j in range(k)]
       for i in range(k+d)]
    return det([[sum(K[r][i]*K[r][j] for r in range(k+d))
                 for j in range(k)] for i in range(k)])

def dilate(p,r):
    q=[0]*((len(p)-1)*r+1)
    for i,a in enumerate(p): q[i*r]=a
    return q

inputs={
    'lehmer':[1,1,0,-1,-1,-1,-1,-1,0,1,1],
    'reciprocal_quadratic':[1,-3,1],
    'cyclotomic_3':[1,1,1],
    'cyclotomic_5':[1,1,1,1,1],
    'cyclotomic_7':[1,1,1,1,1,1,1],
    'nonunit_t5_minus2':[-2,0,0,0,0,1],
}
out={'python':sys.version.split()[0],'cases':{}}
for name,p in inputs.items():
    d=len(p)-1; delta=disc(p)
    assert delta>0
    for k in range(0,9): assert gram(p,d+k)==relation_gram(p,k)
    rows=[]
    for mult in [1,2,4,8,16,32]:
        N=d*mult; G=gram(p,N); X=delta*G
        rows.append({'N':N,'gram':G,'positive_certificate':X>N**d,
                     'log2_over8_certificate':X**4>=N**(4*d)*2**(N-1)})
    out['cases'][name]={'coefficients_ascending':p,'degree':d,
                        'discriminant_abs':delta,'windows':rows}
for ell in [3,5,7]:
    p=[1]*ell; d=ell-1
    for N in [ell,2*ell,3*ell]: assert disc(p)*gram(p,N)==N**d
q=inputs['reciprocal_quadratic']
for r in [2,3,5]:
    p=dilate(q,r); d=len(p)-1
    assert disc(p)==r**d*disc(q)**r
    for L in [2,3,4,8]: assert gram(p,r*L)==gram(q,L)**r
out['identity_checks']='passed: dual Gram, prime-cyclotomic equality, dilation'
print(json.dumps(out,indent=2))
```

## 7. Review status and next obligation

The finite lower estimate (2)--(3), exact kernel identity (1), and dilation identity (5) have direct proofs above.
The [original separate Gram finding](../audits/reviews/Yin_R_G0503_v1.md#original-separate-gram-finding) retains the actual Sections1–5/first-output check, no-rerun and uninspected-Szego scope, with its initial inherited context unknown.
The [original coordinating checks](../audits/reviews/Yin_R_G0503_v1.md#original-coordinating-gram-checks) retain the actual proof-contributor checks and later three-program reproduction at their different dates and scopes.
The [current complete theorem](../claims/Yin_C_G0209_v1.md#statement) has its separately dated [actual self-review](../audits/reviews/Yin_R_G0502_v1.md#orbit-gram-current-finding); neither finding supplies a whole-Task completion or new independent replay.

In particular, the retained Toeplitz limit also proves \(B_N(p)\to m(p)\) for each fixed polynomial.
Every threshold strictly below that particular positive entropy is eventually certified.
No degree-uniform bound on when this occurs is supplied.

The next substantive missing input would be an arithmetic lower bound on \(\Delta G_N\) exceeding the boundary \(N^d\) by an exponential factor, valid uniformly over the hard core, at a justified range of windows.
Integrality alone supplies \(\Delta G_N\ge1\), nowhere near this.
The finite identity and certificate therefore preserve the hard obligation rather than hide it.
Continue only if a new structural inequality controls that surplus or the exact experiments identify a narrower testable obstruction.
Do not promote successful sample certificates to a uniform entropy gap.

<a id="bounded-reciprocal-probe"></a>
## 8. Exact bounded reciprocal probe

This extension tests all monic reciprocal degree \(d\in\{2,4,6,8,10,12\}\) polynomials with constant coefficient 1 and each independent remaining coefficient in \(\{-1,0,1\}\).
It first seeks a finite-field irreducibility certificate among the primes listed in the code.
A successful modular certificate proves rational irreducibility; failure to find one does **not** prove reducibility and those cases remain outside the certified sample.
Cyclotomic polynomials are removed by exact equality against the finite list of orders with \(\varphi(n)=d\).
For \(d\le12\), it suffices to list \(n\le288\), using \(\varphi(n)\ge\sqrt{n/2}\).
The latter follows prime-power by prime-power from \(\varphi(n)^2/n=\prod_{p^a\parallel n}p^{a-2}(p-1)^2\), whose only factor below 1 is the single possible factor \(1/2\) at \(p=2,a=1\).

The precise finite outcome is the number of certified noncyclotomic irreducible polynomials, any failed \(N=2d\) positivity tests, and failures of the fixed \((\log2)/8\) threshold.
The latter test is stronger and has already failed for Lehmer, so its failure count is a diagnostic, not a new counterexample to the main Task.
All arithmetic below is exact.

```python
from pathlib import Path
import itertools, json, sys
from math import isqrt
draft=Path('mathematics/ledger/Yin_L_G0004_v1.md')
first=draft.read_text(encoding='utf-8').split('```python\n',1)[1].split('\n```',1)[0]
exec(first.split('\ninputs=',1)[0],globals())

def trim(f):
    while len(f)>1 and f[-1]==0: f.pop()
    return f

def remmod(f,g,q):
    f=trim([a%q for a in f]); g=trim([a%q for a in g])
    inv=pow(g[-1],-1,q)
    while len(f)>=len(g) and f!=[0]:
        c=f[-1]*inv%q; shift=len(f)-len(g)
        for j,a in enumerate(g): f[shift+j]=(f[shift+j]-c*a)%q
        trim(f)
    return f

def mulmod(f,g,p,q):
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): h[i+j]=(h[i+j]+a*b)%q
    return remmod(h,p,q)

def powmod(f,n,p,q):
    z=[1]
    while n:
        if n&1: z=mulmod(z,f,p,q)
        f=mulmod(f,f,p,q); n//=2
    return z

def gcdmod(f,g,q):
    while g!=[0]: f,g=g,remmod(f,g,q)
    return trim(f)

def irreducible_mod(p,q):
    d=len(p)-1; x=[0,1]; u=x
    divisors=[ell for ell in range(2,d+1)
              if d%ell==0 and all(ell%j for j in range(2,isqrt(ell)+1))]
    checks={d//ell for ell in divisors}
    for j in range(1,d+1):
        u=powmod(u,q,p,q)
        if j in checks:
            diff=u+[0]*max(0,2-len(u)); diff[1]=(diff[1]-1)%q
            if len(gcdmod(p,trim(diff),q))!=1: return False
    return trim(u)==x

def divexact(f,g):
    f=f[:]; out=[0]*(len(f)-len(g)+1)
    while len(f)>=len(g) and f!=[0]:
        assert f[-1]%g[-1]==0
        c=f[-1]//g[-1]; shift=len(f)-len(g); out[shift]=c
        for j,a in enumerate(g): f[shift+j]-=c*a
        trim(f)
    assert f==[0]
    return trim(out)

cyclo={}
for n in range(1,289):
    f=[-1]+[0]*(n-1)+[1]
    for j in range(1,n):
        if n%j==0: f=divexact(f,cyclo[j])
    cyclo[n]=f
cyclo_polys={tuple(f):n for n,f in cyclo.items()}
primes=[2,3,5,7,11,13,17,19,23,29,31]
out={'python':sys.version.split()[0],'prime_certificate_list':primes,
     'independent_coefficients':[-1,0,1],'degrees':{},'positivity_failures':[],
     'fixed_threshold_failure_examples':[]}
for d in [2,4,6,8,10,12]:
    counts={'enumerated':0,'modularly_certified':0,'cyclotomic_certified':0,
            'no_modular_certificate':0,'noncyclotomic_certified':0,
            'positivity_failures':0,'fixed_threshold_failures':0}
    for coeff in itertools.product([-1,0,1],repeat=d//2):
        p=[0]*(d+1);p[0]=p[-1]=1
        for i,a in enumerate(coeff,1): p[i]=p[d-i]=a
        counts['enumerated']+=1
        witness=next((q for q in primes if irreducible_mod(p,q)),None)
        if witness is None:
            counts['no_modular_certificate']+=1;continue
        counts['modularly_certified']+=1
        if tuple(p) in cyclo_polys:
            counts['cyclotomic_certified']+=1;continue
        counts['noncyclotomic_certified']+=1
        delta=disc(p);N=2*d;G=gram(p,N);X=delta*G
        assert delta>0 and G>0
        record={'degree':d,'coefficients_ascending':p,'irreducible_mod_prime':witness,
                'N':N,'discriminant_abs':delta,'gram':G,'boundary':N**d}
        if X<=N**d:
            counts['positivity_failures']+=1
            out['positivity_failures'].append(record)
        if X**4<N**(4*d)*2**(N-1):
            counts['fixed_threshold_failures']+=1
            if len(out['fixed_threshold_failure_examples'])<8:
                out['fixed_threshold_failure_examples'].append(record)
    out['degrees'][str(d)]=counts
print(json.dumps(out,indent=2))
```

## 9. Trace-polynomial completion of the bounded probe

The first modular filter can systematically miss irreducible reciprocal polynomials: the Lehmer discriminant is \(36497^2\), and its degree-ten polynomial had no successful certificate in the listed primes.
An even-degree irreducible polynomial with square discriminant cannot have a full-cycle Frobenius at an unramified prime, so extending only that prime list does not solve the coverage problem.

For \(d=2m\), form the integral monic trace polynomial
\[
p(t)=t^m Q(t+t^{-1}),\qquad
Q(x)=a_m+\sum_{j=1}^m a_{m+j}S_j(x),\quad
S_0=2,\ S_1=x,\ S_j=xS_{j-1}-S_{j-2}.
\]
If \(Q\) is irreducible over \(\mathbb Q\) and has a real root in \((-2,2)\), then \(p\) is irreducible: under the associated real embedding, \(u^2-4<0\), so \(u^2-4\) cannot be a square in \(\mathbb Q(u)\); adjoining a root of \(t^2-ut+1\) doubles the degree.
Total reality of every root of \(Q\) is not required.
The finite probe below certifies \(Q\)'s irreducibility by the same finite-field test and its interior real root by exact signs on the rational grid \(a/4\), \(-8\le a\le8\).
Failure of that sufficient test still leaves an unresolved case, not a claim of reducibility.

The finite-field test used in both blocks is the standard exact criterion: a monic degree-\(d\) polynomial is irreducible over \(\mathbb F_q\) iff it divides \(t^{q^d}-t\) and is relatively prime to \(t^{q^{d/\ell}}-t\) for every prime divisor \(\ell\) of \(d\).
The first condition forces all irreducible factor degrees to divide \(d\), with no repetitions; any proper divisor then divides \(d/\ell\) for some such \(\ell\).
This is an elementary finite-field input, not an empirical irreducibility heuristic.

```python
from pathlib import Path
from fractions import Fraction
import itertools,json,sys
draft=Path('mathematics/ledger/Yin_L_G0004_v1.md')
blocks=draft.read_text(encoding='utf-8').split('```python\n')
second=blocks[2].split('\n```',1)[0]
exec(second.split('\nprimes=',1)[0],globals())
primes=[2,3,5,7,11,13,17,19,23,29,31]

def trace_polynomial(p):
    m=(len(p)-1)//2
    S=[[2],[0,1]]
    for j in range(2,m+1):
        v=[0]+S[-1]
        for i,a in enumerate(S[-2]): v[i]-=a
        S.append(trim(v))
    Q=[p[m]]+[0]*m
    for j in range(1,m+1):
        for i,a in enumerate(S[j]): Q[i]+=p[m+j]*a
    return trim(Q)

def evaluate(f,x):
    y=Fraction(0)
    for a in f[::-1]: y=y*x+a
    return y

def real_bracket(Q):
    values=[evaluate(Q,Fraction(a,4)) for a in range(-8,9)]
    for j in range(1,16):
        if values[j]==0: return [str(Fraction(j-8,4))]*2
    for j in range(16):
        if values[j]*values[j+1]<0:
            return [str(Fraction(j-8,4)),str(Fraction(j-7,4))]
    return None

out={'python':sys.version.split()[0],'grid':'a/4, -8<=a<=8',
     'prime_certificate_list':primes,'degrees':{},'positivity_failures':[],
     'trace_added_threshold_failures':[],'lehmer_certificate':None}
for d in [2,4,6,8,10,12]:
    counts={'enumerated':0,'direct_noncyclotomic':0,'trace_added_noncyclotomic':0,
            'cyclotomic_certified':0,'unresolved':0,'positivity_failures':0,
            'fixed_threshold_failures':0}
    for coeff in itertools.product([-1,0,1],repeat=d//2):
        p=[0]*(d+1);p[0]=p[-1]=1
        for i,a in enumerate(coeff,1): p[i]=p[d-i]=a
        counts['enumerated']+=1
        direct=next((q for q in primes if irreducible_mod(p,q)),None)
        Q=trace_polynomial(p)
        qprime=(2 if len(Q)==2 else next((q for q in primes if irreducible_mod(Q,q)),None))
        bracket=real_bracket(Q) if qprime is not None else None
        if direct is None and bracket is None:
            counts['unresolved']+=1;continue
        if tuple(p) in cyclo_polys:
            counts['cyclotomic_certified']+=1;continue
        key='direct_noncyclotomic' if direct is not None else 'trace_added_noncyclotomic'
        counts[key]+=1
        delta=disc(p);N=2*d;G=gram(p,N);X=delta*G
        record={'degree':d,'coefficients_ascending':p,'direct_prime':direct,
                'trace_coefficients':Q,'trace_prime':qprime,'real_bracket':bracket,
                'N':N,'discriminant_abs':delta,'gram':G,'boundary':N**d}
        if p==[1,1,0,-1,-1,-1,-1,-1,0,1,1]: out['lehmer_certificate']=record
        if X<=N**d:
            counts['positivity_failures']+=1
            out['positivity_failures'].append(record)
        if X**4<N**(4*d)*2**(N-1):
            counts['fixed_threshold_failures']+=1
            if direct is None: out['trace_added_threshold_failures'].append(record)
    out['degrees'][str(d)]=counts
print(json.dumps(out,indent=2))
```

## Executed evidence — 2026-10-06

The retained Python block was extracted from this draft and executed by CPython 3.13.15 from repository root.
All assertions passed.
Full exact output follows; integer certificate flags are rigorous finite comparisons, not floating-point approximations.

```json
{
  "python": "3.13.15",
  "cases": {
    "lehmer": {
      "coefficients_ascending": [
        1,
        1,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        0,
        1,
        1
      ],
      "degree": 10,
      "discriminant_abs": 1332031009,
      "windows": [
        {
          "N": 10,
          "gram": 1,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 20,
          "gram": 79461,
          "positive_certificate": true,
          "log2_over8_certificate": false
        },
        {
          "N": 40,
          "gram": 18006972477,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 80,
          "gram": 2174672577497287500,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 160,
          "gram": 108868073231640310520143399334737,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 320,
          "gram": 1031416725526557915703764068207310497506130433615899446229,
          "positive_certificate": true,
          "log2_over8_certificate": true
        }
      ]
    },
    "reciprocal_quadratic": {
      "coefficients_ascending": [
        1,
        -3,
        1
      ],
      "degree": 2,
      "discriminant_abs": 5,
      "windows": [
        {
          "N": 2,
          "gram": 1,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 4,
          "gram": 85,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 8,
          "gram": 194821,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 16,
          "gram": 949006019845,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 32,
          "gram": 22515310644984464780548741,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 64,
          "gram": 12673480336003768886031069539350729440256838859478405,
          "positive_certificate": true,
          "log2_over8_certificate": true
        }
      ]
    },
    "cyclotomic_3": {
      "coefficients_ascending": [
        1,
        1,
        1
      ],
      "degree": 2,
      "discriminant_abs": 3,
      "windows": [
        {
          "N": 2,
          "gram": 1,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 4,
          "gram": 5,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 8,
          "gram": 21,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 16,
          "gram": 85,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 32,
          "gram": 341,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 64,
          "gram": 1365,
          "positive_certificate": false,
          "log2_over8_certificate": false
        }
      ]
    },
    "cyclotomic_5": {
      "coefficients_ascending": [
        1,
        1,
        1,
        1,
        1
      ],
      "degree": 4,
      "discriminant_abs": 125,
      "windows": [
        {
          "N": 4,
          "gram": 1,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 8,
          "gram": 28,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 16,
          "gram": 513,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 32,
          "gram": 8316,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 64,
          "gram": 134017,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 128,
          "gram": 2146300,
          "positive_certificate": false,
          "log2_over8_certificate": false
        }
      ]
    },
    "cyclotomic_7": {
      "coefficients_ascending": [
        1,
        1,
        1,
        1,
        1,
        1,
        1
      ],
      "degree": 6,
      "discriminant_abs": 16807,
      "windows": [
        {
          "N": 6,
          "gram": 1,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 12,
          "gram": 144,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 24,
          "gram": 10800,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 48,
          "gram": 722701,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 96,
          "gram": 46444944,
          "positive_certificate": false,
          "log2_over8_certificate": false
        },
        {
          "N": 192,
          "gram": 2978274096,
          "positive_certificate": false,
          "log2_over8_certificate": false
        }
      ]
    },
    "nonunit_t5_minus2": {
      "coefficients_ascending": [
        -2,
        0,
        0,
        0,
        0,
        1
      ],
      "degree": 5,
      "discriminant_abs": 50000,
      "windows": [
        {
          "N": 5,
          "gram": 1,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 10,
          "gram": 3125,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 20,
          "gram": 4437053125,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 40,
          "gram": 4974623821847602653125,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 80,
          "gram": 6014410023166629976918823622870723941221853125,
          "positive_certificate": true,
          "log2_over8_certificate": true
        },
        {
          "N": 160,
          "gram": 8790070106670411859325354979353790689496381130317201803768093642209399938723599473555916253125,
          "positive_certificate": true,
          "log2_over8_certificate": true
        }
      ]
    }
  },
  "identity_checks": "passed: dual Gram, prime-cyclotomic equality, dilation"
}
```

## Executed bounded reciprocal probe — 2026-10-06

The second retained Python block was extracted and run from repository root with CPython 3.13.15.
The modular tests and all displayed comparisons used exact integer arithmetic.
Full output:

```json
{
  "python": "3.13.15",
  "prime_certificate_list": [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31
  ],
  "independent_coefficients": [
    -1,
    0,
    1
  ],
  "degrees": {
    "2": {
      "enumerated": 3,
      "modularly_certified": 3,
      "cyclotomic_certified": 3,
      "no_modular_certificate": 0,
      "noncyclotomic_certified": 0,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "4": {
      "enumerated": 9,
      "modularly_certified": 4,
      "cyclotomic_certified": 2,
      "no_modular_certificate": 5,
      "noncyclotomic_certified": 2,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "6": {
      "enumerated": 27,
      "modularly_certified": 8,
      "cyclotomic_certified": 4,
      "no_modular_certificate": 19,
      "noncyclotomic_certified": 4,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "8": {
      "enumerated": 81,
      "modularly_certified": 26,
      "cyclotomic_certified": 0,
      "no_modular_certificate": 55,
      "noncyclotomic_certified": 26,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "10": {
      "enumerated": 243,
      "modularly_certified": 94,
      "cyclotomic_certified": 2,
      "no_modular_certificate": 149,
      "noncyclotomic_certified": 92,
      "positivity_failures": 0,
      "fixed_threshold_failures": 6
    },
    "12": {
      "enumerated": 729,
      "modularly_certified": 264,
      "cyclotomic_certified": 2,
      "no_modular_certificate": 465,
      "noncyclotomic_certified": 262,
      "positivity_failures": 0,
      "fixed_threshold_failures": 2
    }
  },
  "positivity_failures": [],
  "fixed_threshold_failure_examples": [
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        -1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        -1,
        1
      ],
      "irreducible_mod_prime": 2,
      "N": 20,
      "discriminant_abs": 1035983667,
      "gram": 140572,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        -1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        -1,
        1
      ],
      "irreducible_mod_prime": 3,
      "N": 20,
      "discriminant_abs": 886967524,
      "gram": 247900,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        0,
        1,
        -1,
        0,
        -1,
        0,
        -1,
        1,
        0,
        1
      ],
      "irreducible_mod_prime": 3,
      "N": 20,
      "discriminant_abs": 379908823,
      "gram": 304513,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        1
      ],
      "irreducible_mod_prime": 3,
      "N": 20,
      "discriminant_abs": 379908823,
      "gram": 304513,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        1,
        0,
        -1,
        0,
        0,
        0,
        -1,
        0,
        1,
        1
      ],
      "irreducible_mod_prime": 3,
      "N": 20,
      "discriminant_abs": 886967524,
      "gram": 247900,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        1,
        0,
        0,
        0,
        -1,
        0,
        0,
        0,
        1,
        1
      ],
      "irreducible_mod_prime": 2,
      "N": 20,
      "discriminant_abs": 1035983667,
      "gram": 140572,
      "boundary": 10240000000000
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        0,
        1,
        0,
        0,
        -1,
        -1,
        -1,
        0,
        0,
        1,
        0,
        1
      ],
      "irreducible_mod_prime": 2,
      "N": 24,
      "discriminant_abs": 484908967805,
      "gram": 2686805,
      "boundary": 36520347436056576
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        0,
        1,
        0,
        0,
        1,
        -1,
        1,
        0,
        0,
        1,
        0,
        1
      ],
      "irreducible_mod_prime": 2,
      "N": 24,
      "discriminant_abs": 484908967805,
      "gram": 2686805,
      "boundary": 36520347436056576
    }
  ]
}
```

## Executed trace-polynomial probe — 2026-10-06

The third retained Python block was extracted and run from repository root with CPython 3.13.15.
All irreducibility and sign brackets are exact.
Full output:

```json
{
  "python": "3.13.15",
  "grid": "a/4, -8<=a<=8",
  "prime_certificate_list": [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31
  ],
  "degrees": {
    "2": {
      "enumerated": 3,
      "direct_noncyclotomic": 0,
      "trace_added_noncyclotomic": 0,
      "cyclotomic_certified": 3,
      "unresolved": 0,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "4": {
      "enumerated": 9,
      "direct_noncyclotomic": 2,
      "trace_added_noncyclotomic": 0,
      "cyclotomic_certified": 4,
      "unresolved": 3,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "6": {
      "enumerated": 27,
      "direct_noncyclotomic": 4,
      "trace_added_noncyclotomic": 8,
      "cyclotomic_certified": 4,
      "unresolved": 11,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "8": {
      "enumerated": 81,
      "direct_noncyclotomic": 26,
      "trace_added_noncyclotomic": 12,
      "cyclotomic_certified": 4,
      "unresolved": 39,
      "positivity_failures": 0,
      "fixed_threshold_failures": 0
    },
    "10": {
      "enumerated": 243,
      "direct_noncyclotomic": 92,
      "trace_added_noncyclotomic": 38,
      "cyclotomic_certified": 2,
      "unresolved": 111,
      "positivity_failures": 0,
      "fixed_threshold_failures": 10
    },
    "12": {
      "enumerated": 729,
      "direct_noncyclotomic": 262,
      "trace_added_noncyclotomic": 148,
      "cyclotomic_certified": 6,
      "unresolved": 313,
      "positivity_failures": 0,
      "fixed_threshold_failures": 6
    }
  },
  "positivity_failures": [],
  "trace_added_threshold_failures": [
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        -1,
        0,
        1,
        -1,
        1,
        -1,
        1,
        0,
        -1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        -3,
        4,
        5,
        -5,
        -1,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-1",
        "-3/4"
      ],
      "N": 20,
      "discriminant_abs": 1332031009,
      "gram": 79461,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        0,
        0,
        0,
        -1,
        -1,
        -1,
        0,
        0,
        0,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        -1,
        4,
        0,
        -5,
        0,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-2",
        "-7/4"
      ],
      "N": 20,
      "discriminant_abs": 1487567761,
      "gram": 184140,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        0,
        0,
        0,
        -1,
        1,
        -1,
        0,
        0,
        0,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        1,
        4,
        0,
        -5,
        0,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-1",
        "-3/4"
      ],
      "N": 20,
      "discriminant_abs": 1487567761,
      "gram": 184140,
      "boundary": 10240000000000
    },
    {
      "degree": 10,
      "coefficients_ascending": [
        1,
        1,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        0,
        1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        3,
        4,
        -5,
        -5,
        1,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-2",
        "-7/4"
      ],
      "N": 20,
      "discriminant_abs": 1332031009,
      "gram": 79461,
      "boundary": 10240000000000
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        -1,
        0,
        0,
        0,
        1,
        -1,
        1,
        0,
        0,
        0,
        -1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        -3,
        -4,
        9,
        5,
        -6,
        -1,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-2",
        "-7/4"
      ],
      "N": 24,
      "discriminant_abs": 392541093961,
      "gram": 2157840,
      "boundary": 36520347436056576
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        -1,
        1,
        0,
        -1,
        1,
        -1,
        1,
        -1,
        0,
        1,
        -1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        1,
        -4,
        4,
        5,
        -5,
        -1,
        1
      ],
      "trace_prime": 3,
      "real_bracket": [
        "-2",
        "-7/4"
      ],
      "N": 24,
      "discriminant_abs": 201018619201,
      "gram": 2425753,
      "boundary": 36520347436056576
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        1,
        0,
        0,
        0,
        -1,
        -1,
        -1,
        0,
        0,
        0,
        1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        -3,
        4,
        9,
        -5,
        -6,
        1,
        1
      ],
      "trace_prime": 2,
      "real_bracket": [
        "-1",
        "-3/4"
      ],
      "N": 24,
      "discriminant_abs": 392541093961,
      "gram": 2157840,
      "boundary": 36520347436056576
    },
    {
      "degree": 12,
      "coefficients_ascending": [
        1,
        1,
        1,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        0,
        1,
        1,
        1
      ],
      "direct_prime": null,
      "trace_coefficients": [
        1,
        4,
        4,
        -5,
        -5,
        1,
        1
      ],
      "trace_prime": 3,
      "real_bracket": [
        "-2",
        "-7/4"
      ],
      "N": 24,
      "discriminant_abs": 201018619201,
      "gram": 2425753,
      "boundary": 36520347436056576
    }
  ],
  "lehmer_certificate": {
    "degree": 10,
    "coefficients_ascending": [
      1,
      1,
      0,
      -1,
      -1,
      -1,
      -1,
      -1,
      0,
      1,
      1
    ],
    "direct_prime": null,
    "trace_coefficients": [
      3,
      4,
      -5,
      -5,
      1,
      1
    ],
    "trace_prime": 2,
    "real_bracket": [
      "-2",
      "-7/4"
    ],
    "N": 20,
    "discriminant_abs": 1332031009,
    "gram": 79461,
    "boundary": 10240000000000
  }
}
```
