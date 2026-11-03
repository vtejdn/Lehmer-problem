"""Exact stdout-only review of the frozen signed-power classification.

Uses binary modular polynomial powers and a polynomial-multiple projection.
Does not import author or review programs and does not write result files.
"""
import json, math, sys, time
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
import subprocess

if Path(__file__).name != "<stdin>" and "--worker" not in sys.argv:
    try:
        result = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()), "--worker", *sys.argv[1:]],
            timeout=30,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(json.dumps({"status": "incomplete", "error": "aggregate 30-second review cap"}))
        raise SystemExit(1)
    raise SystemExit(result.returncode)
if "--worker" in sys.argv:
    sys.argv.remove("--worker")

import sympy as sp

START = time.perf_counter()
J_PROGRAM = Path(__file__).resolve().parent
ROOT = next(parent for parent in (J_PROGRAM, *J_PROGRAM.parents) if (parent / "repository/config.json").is_file())
if Path(__file__).name == "<stdin>":
    J_PROGRAM = ROOT / "mathematics/computations/programs/Yin_J_G0079"
SOURCE = ROOT / "mathematics/computations/outputs" / J_PROGRAM.name / "residual-lattice-output.json"
t = sp.Symbol("t")
if any(arg != "--compare-saved" for arg in sys.argv[1:]):
    raise SystemExit("usage: power-classification-isolated-review.py [--compare-saved]")

def check(truth, label):
    if time.perf_counter()-START>30:
        raise TimeoutError("Fixed-domain review aggregate 30-second cap")
    if not truth:
        raise AssertionError(label)

def coeffs(poly):
    poly = sp.Poly(poly, t, domain=sp.QQ)
    return [int(poly.nth(i)) for i in range(max(0, int(poly.degree()))+1)] if not poly.is_zero else [0]

def poly(a):
    return sp.Poly.from_list(list(reversed(a)), gens=t, domain=sp.ZZ)

def trim(a):
    a = list(a)
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return a

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return trim(c)

def rem(a,p):
    a=trim(a)
    while len(a)>=len(p):
        c=a[-1]; shift=len(a)-len(p)
        for j,x in enumerate(p):
            a[shift+j]-=c*x
        a=trim(a)
    return a+[0]*(len(p)-1-len(a))

def power(k,p):
    d=len(p)-1
    base=([0,1]+[0]*(d-2)) if k>=0 else [-p[j+1]//p[0] for j in range(d)]
    acc=[1]+[0]*(d-1)
    exponent=abs(k)
    while exponent:
        if exponent&1:
            acc=rem(conv(acc,base),p)
        base=rem(conv(base,base),p)
        exponent//=2
    return acc

def relation(z,p,k,sgn):
    if k>=0:
        a=[0]*max(k+1,len(z)); a[k]=1
        for i,x in enumerate(z): a[i]-=sgn*x
    else:
        a=[0]*(-k+len(z)); a[0]=-sgn
        for i,x in enumerate(z): a[i-k]+=x
    a=trim(a)
    q,r=sp.div(poly(a),poly(p),domain=sp.ZZ)
    check(r.is_zero,"ordinary polynomial identity remainder")
    u=coeffs(q)
    check(conv(p,u)==a,"full ordinary polynomial coefficient convolution")
    return {"k":k,"sign":sgn,"identity_coefficients":a,"quotient_coefficients":u}

def ac(a):
    return [sum(a[i]*a[i+h] for i in range(len(a)-h)) for h in range(1,len(a))]

def frac(a):
    return F(*a)

def pair(a):
    a=F(a)
    return [a.numerator,a.denominator]

def mtrim(a,q):
    return trim([x%q for x in a])

def mrem(a,b,q):
    a=mtrim(a,q); b=mtrim(b,q)
    while len(a)>=len(b) and any(a):
        c=a[-1]*pow(b[-1],-1,q)%q
        shift=len(a)-len(b)
        for j,x in enumerate(b): a[shift+j]=(a[shift+j]-c*x)%q
        a=mtrim(a,q)
    return a

def mpow(a,k,p,q):
    out=[1]
    while k:
        if k&1: out=mrem(conv(out,a),p,q)
        a=mrem(conv(a,a),p,q); k//=2
    return out

def mgcd(a,b,q):
    a=mtrim(a,q); b=mtrim(b,q)
    while any(b): a,b=b,mrem(a,b,q)
    c=pow(a[-1],-1,q)
    return mtrim([c*x for x in a],q)

def irreducibility(p,q):
    d=len(p)-1
    x=[0,1]
    check(mpow(x,q**d,p,q)==x,("Frobenius",d,q))
    for ell in sp.factorint(d):
        r=mpow(x,q**(d//ell),p,q)
        r += [0]*max(0,2-len(r)); r[1]=(r[1]-1)%q
        check(mgcd(p,r,q)==[1],("proper-degree gcd",d,q,ell))

raw=json.loads(SOURCE.read_text(encoding="utf8"))
check(raw["status"]=="complete" and raw["domain_n"]==[18,30],"raw complete domain")
check([r["n"] for r in raw["records"]]==[18,30],"exact record order")
records=[]
summaries=[]
total_powers=total_comparisons=total_matches=0
for r in raw["records"]:
    n,d,N,q=r["n"],r["d"],r["N"],r["q"]
    check((n,d,N) in [(18,20,40),(30,32,64)],"exact original n,d,N")
    p=r["coefficients"]
    numerator=[0]*(n+4)
    for i,c in [(n+3,1),(n+1,-1),(n,-1),(3,-1),(2,-1),(0,1)]:
        numerator[i]+=c
    check(conv(p,[1,1])==trim(numerator),"actual selected P=(t^n A+A*)/(t+1)")
    irreducibility(p,2 if n==18 else 11)
    check(poly(p).eval(1)<0<poly(p).eval(2),"real expanding root")
    K=4*N
    check(rem(conv([0,1],power(-1,p)),p)==[1]+[0]*(d-1),"integral inverse polynomial for alpha")
    powers={k:power(k,p) for k in range(-K,K+1)}
    total_powers+=len(powers)
    X=sp.Matrix.hstack(*(sp.Matrix(powers[j]) for j in range(N)))
    check(X.tolist()==r["X_rows"],"all original remainder columns")
    check((X*X.T).tolist()==r["Q_rows"],"original remainder Gram")
    A=sp.zeros(N,N-d)
    for j in range(N-d):
        for i,c in enumerate(p): A[i+j,j]=c
    R=sp.eye(N)-A*(A.T*A).inv()*A.T
    check(X*R==X and R*R==R and R.T==R,"polynomial-multiple projection")
    check(q==sp.ilcm(*(x.q for x in R)),"actual original least projection scale")
    C=(q*R).applyfunc(int)
    check(C[:,:d].tolist()==r["L_rows"],"original lattice basis")
    check(r["degree_bound"]==N-1 and r["radial_multiplier"]==[N-1,d],"original degree and radial bound")
    rows=r["U_rows"]
    basis=sp.Matrix(rows); inverse=sp.Matrix(r["U_inverse_rows"])
    check(int(basis.det())==r["det_U"] and abs(r["det_U"])==1,"frozen integer basis unimodular")
    check(basis*inverse==sp.eye(d) and inverse*basis==sp.eye(d),"both complete frozen integer inverse products")
    check((basis*C[:,:d].T).tolist()==r["reduced_rows"],"full frozen reduced basis rows")
    expected_labels=[("basis",i,0,list(rows[i])) for i in range(d)]
    for i in range(d-1):
        for sgn in [-1,1]:
            expected_labels.append(("adjacent",i,sgn,[a+sgn*b for a,b in zip(rows[i],rows[i+1])]))
    check(len(r["candidates"])==3*d-2==len(expected_labels),"complete frozen label count")
    cand=[]
    columns=[[int(C[i,j]) for i in range(N)] for j in range(N)]
    old_e=[F(sum(x*x for x in a),q*q) for a in columns]
    old_h=[[F(x,q*q) for x in ac(a)] for a in columns]
    check([pair(x) for x in old_e]==r["old_r"],"all old monomial energies")
    check([[pair(old_h[j][h]) for j in range(N)] for h in range(N-1)]==r["old_H"],"all old monomial correlations")
    for index,(seed,label) in enumerate(zip(r["candidates"],expected_labels)):
        z=seed["z"]; B=z+[0]*(N-d)
        check((seed["kind"],seed["basis_index"],seed["sign"],z)==label,("frozen label",n,index))
        check(seed["B"]==B,("full original B",n,index))
        f=[int(x) for x in C*sp.Matrix(B)]
        check(f==seed["F_coefficients"],("original F projection",n,index))
        difference=[q*x-y for x,y in zip(B,f)]
        u,rr=sp.div(poly(difference),poly(p),domain=sp.ZZ)
        check(rr.is_zero and coeffs(u)==trim(seed["kernel_multiplier"]),("full original congruence",n,index))
        D=int(poly(p).resultant(poly(z)))
        content=reduce(math.gcd,map(abs,f),0)
        energy=F(sum(x*x for x in f),q*q)
        hs=[F(x,q*q) for x in ac(f)]
        check(D==seed["signed_res_B"],("full original residue norm",n,index))
        check(q**d*D==seed["signed_res_F"],("full original F norm",n,index))
        check(content==seed["content"] and [x//content for x in f]==seed["primitive_coefficients"],("original content",n,index))
        check(F(q**d*D,content**d)==seed["signed_res_primitive"],("primitive full norm",n,index))
        check(pair(energy)==seed["e_B"] and sum(x*x for x in f)==seed["integer_energy"],("original energy",n,index))
        check(ac(f)==seed["integer_autocorrelations"] and [pair(x) for x in hs]==seed["h_B"],("all original correlations",n,index))
        check(max(i for i,x in enumerate(f) if x)==seed["actual_degree"]<=N-1,("actual degree",n,index))
        ep=[z==powers[k] for k in range(-K,K+1)]
        en=[z==[-x for x in powers[k]] for k in range(-K,K+1)]
        matches=[relation(z,p,k,sgn) for k in range(-K,K+1) for sgn,yes in [(1,ep[k+K]),(-1,en[k+K])] if yes]
        check(len(matches)<=1,("unique signed power",n,index))
        for m in matches:
            check(0<=m["k"]<N,("old-window exponent",n,index))
            check(f==[m["sign"]*x for x in columns[m["k"]]],("actual original monomial auxiliary",n,index))
        cand.append({"source_index":index,"kind":seed["kind"],"basis_index":seed["basis_index"],"sign":seed["sign"],"z":z,"B":B,"F_coefficients":f,"signed_res_B":D,"content":content,"e_B":pair(energy),"equal_positive":ep,"equal_negative":en,"matches":matches,"bounded_match":bool(matches)})
        total_comparisons+=2*len(powers); total_matches+=len(matches)
    rec={"n":n,"d":d,"N":N,"q":q,"coefficients":p,"k_min":-K,"k_max":K,"power_table":[{"k":k,"coefficients":powers[k]} for k in range(-K,K+1)],"candidates":cand,"candidate_count":len(cand),"matched_indices":[s["source_index"] for s in cand if s["matches"]],"unmatched_indices":[s["source_index"] for s in cand if not s["matches"]],"matched_exponents":[{"index":s["source_index"],"k":s["matches"][0]["k"],"sign":s["matches"][0]["sign"]} for s in cand if s["matches"]]}
    records.append(rec)
    summaries.append({"n":n,"d":d,"N":N,"q":q,"powers":len(powers),"signed_comparisons":2*len(powers)*len(cand),"matched":len(rec["matched_indices"]),"unmatched":len(rec["unmatched_indices"]),"matched_exponents":rec["matched_exponents"],"cost_fields_reconstructed_for":len(cand)})
    if n==18:
        z=cand[17]["z"]
        check(z==[-36,9,7,41,-5,32,-12,27,-16,24,-18,23,-19,22,-20,21,-20,21,16,48],"specific frozen successful row17")
        check(poly(p).eval(-1)==19,"P(-1)=19")
        even=sum(z[::2]); odd=sum(z[1::2]); image=(even-odd)%19
        check((even,odd,even-odd,image)==(-123,268,-391,8),"mod19 all-exponent obstruction")
        check(cand[17]["signed_res_B"]==1 and cand[17]["content"]==1 and cand[17]["e_B"]==[19325311,36887312],"specific unit original cost")
        inv=sp.invert(poly(z),poly(p))
        check(all(x.q==1 for x in inv.all_coeffs()) and sp.rem(poly(z)*inv,poly(p)).as_expr()==1,"inverse in original order")
        y=[frac(x) for x in r["old_y"]]; lam=frac(r["old_lambda"]); mu=frac(r["old_mu"])
        b=[frac(x) for x in r["old_pair_masses"]]
        v=[b[min(j,N-1-j)]/2 for j in range(N)]
        kh=2*sum(abs(sum(v[j]*old_h[j][h] for j in range(N))) for h in range(N-1))
        check(sum(v)==2 and sum(v[j]*old_e[j] for j in range(N))==1,"old monomial primal feasible")
        check(all(abs(x)<=1 for x in y) and mu>0,"old dual feasible y and mu")
        check(all(2*sum(y[h]*old_h[j][h] for h in range(N-1))-lam*old_e[j]-mu>=0 for j in range(N)),"old dual all original columns")
        check(kh==lam+2*mu==frac(r["old_kappa"]),"old global conservative monomial optimum")
        f=cand[17]["F_coefficients"]; s=r["candidates"][17]["conservative_step"]
        w=[frac(x) for x in s["weights"]]
        es=old_e+[frac(cand[17]["e_B"])]
        hs=old_h+[[F(x,q*q) for x in ac(f)]]
        ee=sum(w[j]*es[j] for j in range(N+1))
        aa=[sum(w[j]*hs[j][h] for j in range(N+1)) for h in range(N-1)]
        kk=2*sum(abs(x) for x in aa)/ee
        denominator=sp.ilcm(*(x.denominator for x in w))
        check(len(w)==N+1 and min(w)>=0 and sum(w)==1 and ee==F(1,2),"actual frozen bundle paid energy")
        check(kk==frac(s["kappa"])<kh and denominator==s["weight_denominator"],"strict complete old optimum improvement")
        check([int(x*denominator) for x in w]==s["multiplicities"],"actual finite multiplicities")
        slack=2*sum(y[h]*hs[-1][h] for h in range(N-1))-lam*es[-1]-mu
        check(slack==frac(r["candidates"][17]["reduced_cost"])<0,"old dual row17 slack")
        summaries[-1]["row17"]={"even_sum":even,"odd_sum":odd,"B_minus_one":even-odd,"mod19_image":image,"residue_norm":1,"inverse_integral_degree":int(inv.degree()),"energy":cand[17]["e_B"],"content":1,"old_dual_slack":pair(slack),"strict_bundle_kappa":pair(kk),"bundle_weight_denominator":int(denominator),"all_exponent_exclusion":True}
check((total_powers,total_comparisons,total_matches)==(834,133680,31),"complete announced domain totals")

comparison_summary=None
if "--compare-saved" in sys.argv:
    scalar_count=[0]
    def exact(a,b,path):
        check(type(a) is type(b),("schema type",path,type(a).__name__,type(b).__name__))
        if isinstance(a,dict):
            check(a.keys()==b.keys(),("schema keys",path))
            for k in a: exact(a[k],b[k],path+"/"+k)
        elif isinstance(a,list):
            check(len(a)==len(b),("schema list length",path))
            for i,(x,y) in enumerate(zip(a,b)): exact(x,y,path+"/"+str(i))
        else:
            check(a==b,("exact saved scalar",path,a,b)); scalar_count[0]+=1
    saved=json.loads((SOURCE.parent/"power-classification-output.json").read_text(encoding="utf8"))
    expected={"schema":"J79-exact-signed-power-classification-v1","status":"complete","input":"residual-lattice-output.json","domain_n":[18,30],"power_bound_multiplier":4,"records":records,"actual_worker_exit_code":0,"outer_timed_out":False}
    exact(saved,expected,"classification")
    old=json.loads((SOURCE.parent/"power-classification-review-result.json").read_text(encoding="utf8"))
    old_expected=[{"n":s["n"],"powers":s["powers"],"signed_comparisons":s["signed_comparisons"],"quotients":s["matched"],"matched_exponents":s["matched_exponents"],"all_copied_arithmetic_fields_recomputed":True,"all_schema_fields_checked":True} for s in summaries]
    exact(old["records"],old_expected,"historical-review-records")
    check(old["status"]=="passed" and old["all_integer_exponent_mod19_written_control_checked"] is True and old["author_replayed"] is False,"original saved historical controls")
    comparison_summary={"all_saved_classification_fields_equal":True,"all_old_summary_records_equal":True,"new_exact_scalar_comparisons":scalar_count[0],"original_saved_scalar_tally":old["exact_scalar_comparisons"]}
print(json.dumps({"status":"complete","method":"binary modular powers; polynomial-multiple orthogonal projection; subresultant residue norms","total_powers":total_powers,"total_signed_comparisons":total_comparisons,"total_integral_quotients":total_matches,"records":summaries,"saved_comparison":comparison_summary},separators=(",",":")))
