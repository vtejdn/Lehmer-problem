"""Bounded exact signed-power classification; no optimizer or new candidates."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json,sys,time,subprocess,traceback
HERE=(_J_PROGRAM / 'power-classification-author.py').parent
OUT=(_J_OUTPUT / 'power-classification-output.json')
# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def forward(a,p):
 c=a[-1];return [-p[0]*c]+[a[i-1]-p[i]*c for i in range(1,len(a))]
def backward(a,p):
 assert abs(p[0])==1
 c=-a[0]//p[0]
 return [a[i]+p[i]*c for i in range(1,len(a))]+[c]
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def quotient(f,p):
 a=trim(f[:]);d=len(p)-1;q=[0]*max(1,len(a)-d)
 while len(a)>d:
  k=len(a)-1-d;c=a[-1];q[k]=c
  for j,x in enumerate(p):a[j+k]-=c*x
  trim(a)
 assert not any(a)
 return trim(q)
def relation(z,p,k,sgn):
 if k>=0:
  a=[0]*max(k+1,len(z));a[k]=1
  for j,x in enumerate(z):a[j]-=sgn*x
 else:
  a=[0]*(-k+len(z));a[0]=-sgn
  for j,x in enumerate(z):a[j-k]+=x
 a=trim(a);q=quotient(a,p)
 rebuilt=[0]*(len(q)+len(p)-1)
 for i,x in enumerate(q):
  for j,y in enumerate(p):rebuilt[i+j]+=x*y
 assert trim(rebuilt)==a
 return {"identity_coefficients":a,"quotient_coefficients":q}
def worker():
 start=time.perf_counter();out={'schema': 'J79-exact-signed-power-classification-v1', 'status': 'running', 'input': 'residual-lattice-output.json', 'domain_n': [18, 30], 'power_bound_multiplier': 4, 'records': []}
 try:
  source=json.loads((_J_OUTPUT/out["input"]).read_text(encoding="utf8"))
  assert source["status"]=="complete"
  for r in source["records"]:
   n,d,N=r["n"],r["d"],r["N"];assert (n,d,N) in[(18,20,40),(30,32,64)]
   p=r["coefficients"];assert len(p)==d+1 and p[-1]==1 and abs(p[0])==1
   K=4*N;powers={0:[1]+[0]*(d-1)}
   for k in range(1,K+1):powers[k]=forward(powers[k-1],p)
   for k in range(-1,-K-1,-1):powers[k]=backward(powers[k+1],p)
   for k in range(-K,K):
    assert forward(powers[k],p)==powers[k+1]
    assert backward(powers[k+1],p)==powers[k]
   rec={"n":n,"d":d,"N":N,"q":r["q"],"coefficients":p,"k_min":-K,"k_max":K,"power_table":[{"k":k,"coefficients":powers[k]} for k in range(-K,K+1)],"candidates":[]}
   for index,seed in enumerate(r["candidates"]):
    if time.perf_counter()-start>29:raise TimeoutError("Declared aggregate mathematical cap")
    z=seed["z"];assert len(z)==d and seed["B"]==z+[0]*(N-d)
    ep=[z==powers[k] for k in range(-K,K+1)]
    en=[z==[-x for x in powers[k]] for k in range(-K,K+1)]
    matches=[]
    for k in range(-K,K+1):
     for sgn,truth in[(1,ep[k+K]),(-1,en[k+K])]:
      if truth:matches.append({"k":k,"sign":sgn,**relation(z,p,k,sgn)})
    assert len(matches)<=1
    rec["candidates"].append({"source_index":index,"kind":seed["kind"],"basis_index":seed["basis_index"],"sign":seed["sign"],"z":z,"B":seed["B"],"F_coefficients":seed["F_coefficients"],"signed_res_B":seed["signed_res_B"],"content":seed["content"],"e_B":seed["e_B"],"equal_positive":ep,"equal_negative":en,"matches":matches,"bounded_match":bool(matches)})
   assert len(rec["candidates"])==3*d-2
   rec["candidate_count"]=len(rec["candidates"])
   rec["matched_indices"]=[s["source_index"] for s in rec["candidates"] if s["matches"]]
   rec["unmatched_indices"]=[s["source_index"] for s in rec["candidates"] if not s["matches"]]
   rec["matched_exponents"]=[{"index":s["source_index"],"k":s["matches"][0]["k"],"sign":s["matches"][0]["sign"]} for s in rec["candidates"] if s["matches"]]
   out["records"].append(rec)
  out["status"]="complete"
 except BaseException as exc:out.update(status="incomplete",error=_record_text(repr(exc)),traceback=_record_text(traceback.format_exc()))
 pass;pass
 with OUT.open("x",encoding="utf8",newline="\n") as f:json.dump(out,f,separators=(",",":"))
 return 0 if out["status"]=="complete" else 1
def main():
 assert not OUT.exists(),"Preserve first native report"
 start=time.perf_counter();timedout=False
 try:r=subprocess.run([sys.executable,str((_J_PROGRAM / 'power-classification-author.py')),"--worker"],timeout=30,check=False);status=r.returncode
 except subprocess.TimeoutExpired:timedout=True;status=None
 if OUT.exists():out=json.loads(OUT.read_text(encoding="utf8"))
 else:out={"schema":"J79-exact-signed-power-classification-v1","status":"incomplete","error":"outer cap before native worker report"}
 out.update(actual_worker_exit_code=status, outer_timed_out=timedout)
 OUT.write_text(json.dumps(out,separators=(",",":")),encoding="utf8",newline="\n")
 print(json.dumps({'status': out['status'], 'records': [{'n': r['n'], 'matched': len(r['matched_indices']), 'total': r['candidate_count'], 'powers': r['matched_exponents']} for r in out.get('records', [])]}))
 return 0 if status==0 and not timedout else 1
if __name__=="__main__":raise SystemExit(worker() if "--worker" in sys.argv else main())
