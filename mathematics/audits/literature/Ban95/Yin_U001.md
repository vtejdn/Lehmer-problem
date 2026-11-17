---
author: Yin
---

# Cube covering and the dual first minimum

<a id="ban95-u001"></a>
<a id="lattice-conventions"></a>
## Conventions

For a full-rank lattice \(L\subset\mathbb R^n\), put
\[
 L^*=\{y:\langle y,L\rangle\subset\mathbb Z\},\qquad
 B_p^n=\{x:\|x\|_p\le1\},
\]
\[
 \mu(L,U)=\inf\{r>0:L+rU=\mathbb R^n\},\qquad
 \lambda_1(L,V)=\min_{v\in L\setminus\{0\}}\|v\|_V.
\]
Here \(U,V\) are origin-symmetric convex bodies and \(\|\cdot\|_V\) is their gauge.
These conventions are from printed pp. 218--219 of the [published edition](readme.md#published-edition).

<a id="cube-covering"></a>
## Explicit specialization

Write \(\rho(A)=\sum_{x\in A}e^{-\pi\|x\|_2^2}\).
On printed p. 221, the source defines
\[
 \alpha(U)=\sup_L\frac{\rho(L\setminus U)}{\rho(L)},\qquad
 \beta(U)=\sup_{L,u}\frac{\rho((L+u)\setminus U)}{\rho(L)}.
\]
Lemma 1.5, p. 222, gives
\[
 \beta(U)+2\alpha(V)\le1
 \Longrightarrow
 \mu(L,U)\lambda_1(L^*,V)\le1.
\]
The \(p=1\) moment estimate in Lemma 2.6, p. 225, followed by Markov's inequality gives \(\beta(sB_1^n)\le n/s\).
Lemma 2.10, p. 226, gives \(\beta(rB_\infty^n)\le2ne^{-\pi r^2}\), and \(\alpha\le\beta\).
Thus \(U=rB_\infty^n\), \(V=sB_1^n\), \(r=\sqrt{\log(8n)/\pi}\), \(s=4n\) give a left side at most \(3/4\), hence
\[
 \mu(L,B_\infty^n)\lambda_1(L^*,B_1^n)
 \le4n\sqrt{\frac{\log(8n)}\pi}.
\]
This is a direct specialization, valid also for \(n=1\).
I checked the online original's extracted statements and this substitution, not the underlying Gaussian proofs or rendered pages.
