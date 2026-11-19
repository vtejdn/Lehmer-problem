"""Check every pair count and compare fixed slices with direct integer recurrences."""

from collections import Counter
from itertools import combinations
import json
from math import comb, prod
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory

import numpy as np

import sieve


def tensor_totals(bounds,divisors):
    v2=runpy.run_path(str(sieve.HERE.parent/"v2"/"cyclotomic_prefixes.py"))
    counts={(x,y):0 for x in range(bounds[0]+1)
            for y in range(-bounds[1],bounds[1]+1) if (x-y)%2==0}
    for size in range(len(divisors)+1):
        for primes in combinations(divisors,size):
            q=prod(primes)
            restricted=[b if k%q==0 else 0 for k,b in enumerate(bounds,1)]
            factors,_=v2["completion_factors"](restricted)
            for x,y in counts:
                if x>restricted[0] or abs(y)>restricted[1]:
                    continue
                rows=v2["prefixes"](restricted,x,y)
                ways=np.ones(len(rows),dtype=np.uint64)
                for scope,table in factors:
                    addresses=tuple(rows[:,k-1]+restricted[k-1] for k in scope)
                    ways*=table[addresses]
                counts[x,y]+=(-1)**size*int(ways.sum())
    for (x,y),n in counts.items():
        if x==0:
            assert n%2==0
            counts[x,y]=n//2
    return counts


def check_direct(degree,divisors,prefix,config,bounds):
    """Use no suffix linearization, machine-word Newton sums or modular squaring."""
    exact=runpy.run_path(str(sieve.HERE.parent/"v7"/"affine_tail.py"))
    finish=runpy.run_path(str(sieve.HERE.parent/"v3"/"finish.py"))
    h=degree//2
    quadratic=[p for n,p,_ in finish["cyclotomics"](degree) if n in (3,4,6)]
    graeffe_caps=[
        [int(comb(degree,i)*sieve.T**(2**g)) for i in range(h+1)] for g in range(1,11)]
    totals=Counter(dict.fromkeys(sieve.FIELDS,0))
    c=exact["coefficients"](prefix)
    sums=[0,*prefix]
    word=2**64

    def visit():
        k=len(c)
        if k<=h:
            previous=sum(c[i]*sums[k-i] for i in range(1,k))
            for value in range(-bounds[k-1],bounds[k-1]+1):
                if (previous+value)%k:
                    continue
                sums.append(value)
                c.append(-(previous+value)//k)
                visit()
                c.pop()
                sums.pop()
            return
        if any(all(c[i]==0 for i in range(1,h+1) if i%q!=0) for q in divisors):
            return
        if next(v for j,v in enumerate(sums) if j%2==1 and v!=0)<0:
            return
        totals["representatives"]+=1
        full=c+c[-2::-1]
        local=sums[:]
        for j in range(h+1,121):
            if j==h+10 and (sum(full)==0 or sum(full[::2])==sum(full[1::2])):
                totals["endpoint_zero"]+=1
                return
            v=-(j*full[j] if j<=degree else 0)-sum(
                full[i]*local[j-i] for i in range(1,min(degree+1,j)))
            if abs(v)>config[j]:
                if j>=h+10:
                    totals["later_trace_exclusion"]+=1
                return
            local.append(v)
            if j==h+1:
                totals["first_reflected"]+=1
            if j==h+9:
                totals["nine_reflected"]+=1
        if any(not any(finish["divide"](full,p)[1]) for p in quadratic):
            totals["quadratic_cyclotomic"]+=1
            return
        for row in graeffe_caps:
            full=finish["graeffe"](full)
            if any(min(v%word,-v%word)>cap for v,cap in zip(full,row)):
                totals["modular_graeffe"]+=1
                return
        totals["fallback"]+=1

    visit()
    return dict(totals)


def verify(degree,source):
    dest=sieve.OUTPUT/"v10"/f"d{degree}"
    bounds=source["bounds"]
    divisors=[p for p,q in runpy.run_path(str(sieve.GROUP/"count_prefixes.py"))["prime_powers"](degree)]
    totals,labels=Counter(),Counter()
    unresolved=[]
    witnesses=[]
    graeffe=runpy.run_path(str(sieve.HERE.parent/"v3"/"finish.py"))["graeffe"]
    pairs=tensor_totals(bounds,divisors)
    for (x,y),expected in pairs.items():
        report=json.loads((dest/f"slice_{x}_{y}.json").read_text())
        counts=report["counts"]
        assert report["degree"]==degree and report["cutoff"]==[1091,1000] and report["prefix"]==[x,y]
        assert counts["representatives"]==expected
        assert counts["nine_reflected"]==sum(counts[k] for k in sieve.FIELDS[3:])
        assert counts["fallback"]==sum(report["fallback_classifications"].values())
        assert len(report["unresolved"])==report["fallback_classifications"].get("unresolved",0)
        local=report["exact_witnesses"]
        assert len(local)==sum(n for name,n in report["fallback_classifications"].items()
                               if name.startswith("exact_graeffe_"))
        for w in local:
            half=w["half"]
            assert len(half)==degree//2+1 and half[0]==1
            poly=half+half[-2::-1]
            for _ in range(w["round"]):
                poly=graeffe(poly)
            i=w["index"]
            assert poly[i]==w["coefficient"] and w["upper"]==int(comb(degree,i)*sieve.T**(2**w["round"]))
            assert abs(poly[i])>w["upper"]
        witnesses+=local
        totals.update(counts)
        labels.update(report["fallback_classifications"])
        unresolved+=report["unresolved"]
    assert totals["representatives"]==source["no_power_substitution_up_to_sign"]
    config=sieve.configuration(degree,bounds)
    limits=list(map(int,config.splitlines()[0].split()))
    primes=(5,7,11,17,23)
    prefix=tuple((-1)**k*sum(q-1 if k%q==0 else -1 for q in primes) for k in range(1,17))
    samples=[prefix,(5,)*16,tuple(3*(k%3==0)+5*(k%5==0) for k in range(1,17))]
    samples.extend(tuple(q if k%q==0 else 0 for k in range(1,17)) for q in divisors)
    checks=[]
    with TemporaryDirectory(dir=dest) as folder:
        scratch=Path(folder)
        command=sieve.compile_worker(scratch)
        file=scratch/"caps.txt"
        file.write_text(config,encoding="ascii")
        for p in samples:
            assert all(abs(x)<=b for x,b in zip(p,bounds))
            direct=check_direct(degree,divisors,p,limits,bounds)
            native=sieve.run_slice(degree,p,command,file,True,scratch)
            assert direct==native["counts"]
            checks.append({"prefix":p,"counts":direct})
    data={"degree":degree,"cutoff":[1091,1000],"tensor_verified_pairs":len(pairs),
          "counts":dict(totals),"fallback_classifications":dict(labels),
          "direct_prefix_checks":checks,"exact_graeffe_witnesses":witnesses,"unresolved":unresolved}
    (dest/"summary.json").write_text(json.dumps(data,indent=2)+"\n",encoding="ascii")
    print(degree,dict(totals),flush=True)


if __name__=="__main__":
    for d,source in sieve.boxes().items():
        verify(d,source)
