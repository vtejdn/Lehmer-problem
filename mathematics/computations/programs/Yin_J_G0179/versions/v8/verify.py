"""Check every pair count and compare fixed slices with direct integer recurrences."""

from collections import Counter
import json
from math import comb
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory

import numpy as np

import sieve


def tensor_totals(bounds):
    v2=runpy.run_path(str(sieve.HERE.parent/"v2"/"cyclotomic_prefixes.py"))
    factors,_=v2["completion_factors"](bounds)
    counts={}
    for x in range(bounds[0]+1):
        for y in range(-bounds[1],bounds[1]+1):
            if (x-y)%2:
                continue
            rows=v2["prefixes"](bounds,x,y)
            if x==0:
                odds=rows[:,::2]
                first=np.argmax(odds!=0,axis=1)
                rows=rows[odds[np.arange(len(rows)),first]>0]
            ways=np.ones(len(rows),dtype=np.uint64)
            for scope,table in factors:
                addresses=tuple(rows[:,k-1]+bounds[k-1] for k in scope)
                ways*=table[addresses]
            counts[x,y]=int(ways.sum())
    return counts


def check_direct(prefix, config, bounds):
    """Use no suffix linearization, machine-word Newton sums or modular squaring."""
    exact=runpy.run_path(str(sieve.HERE.parent/"v7"/"affine_tail.py"))
    finish=runpy.run_path(str(sieve.HERE.parent/"v3"/"finish.py"))
    quadratic=[p for n,p,_ in finish["cyclotomics"](64) if n in (3,4,6)]
    graeffe_caps=[
        [int(comb(64,i)*sieve.T**(2**g)) for i in range(33)] for g in range(1,11)]
    totals=Counter(dict.fromkeys(sieve.FIELDS,0))
    c=exact["coefficients"](prefix)
    sums=[0,*prefix]
    word=2**64

    def visit():
        k=len(c)
        if k<=32:
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
        totals["representatives"]+=1
        full=c+c[-2::-1]
        local=sums[:]
        for j in range(33,121):
            if j==42 and (sum(full)==0 or sum(full[::2])==sum(full[1::2])):
                totals["endpoint_zero"]+=1
                return
            v=-(j*full[j] if j<=64 else 0)-sum(
                full[i]*local[j-i] for i in range(1,min(65,j)))
            if abs(v)>config[j]:
                if j>=42:
                    totals["later_trace_exclusion"]+=1
                return
            local.append(v)
            if j in (33,41):
                totals[f"through_{j}"]+=1
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


def main():
    dest=sieve.OUTPUT/"v8"
    source=json.loads((sieve.OUTPUT/"v7"/"boxes.json").read_text())["64"]["certified_all_available"]
    bounds=source["bounds"]
    totals,labels=Counter(),Counter()
    unresolved=[]
    pairs=tensor_totals(bounds)
    for (x,y),expected in pairs.items():
        report=json.loads((dest/f"slice_{x}_{y}.json").read_text())
        counts=report["counts"]
        assert report["degree"]==64 and report["cutoff"]==[1091,1000] and report["prefix"]==[x,y]
        assert counts["representatives"]==expected
        assert counts["through_41"]==sum(counts[k] for k in sieve.FIELDS[3:])
        assert counts["fallback"]==sum(report["fallback_classifications"].values())
        assert len(report["unresolved"])==report["fallback_classifications"].get("unresolved",0)
        totals.update(counts)
        labels.update(report["fallback_classifications"])
        unresolved+=report["unresolved"]
    assert totals["representatives"]==source["no_power_substitution_up_to_sign"]
    config=sieve.configuration(bounds)
    limits=list(map(int,config.splitlines()[0].split()))
    primes=(5,7,11,17,23)
    prefix=tuple((-1)**k*sum(q-1 if k%q==0 else -1 for q in primes) for k in range(1,17))
    samples=[prefix,(5,)*16,tuple(3 if k%3==0 else 0 for k in range(1,17))]
    checks=[]
    with TemporaryDirectory(dir=dest) as folder:
        scratch=Path(folder)
        command=sieve.compile_worker(scratch)
        file=scratch/"caps.txt"
        file.write_text(config,encoding="ascii")
        for p in samples:
            direct=check_direct(p,limits,bounds)
            native=sieve.run_slice(p,command,file,True,scratch)
            assert direct==native["counts"]
            checks.append({"prefix":p,"counts":direct})
    data={"degree":64,"cutoff":[1091,1000],"tensor_verified_pairs":len(pairs),
          "counts":dict(totals),"fallback_classifications":dict(labels),
          "direct_prefix_checks":checks,"unresolved":unresolved}
    (dest/"summary.json").write_text(json.dumps(data,indent=2)+"\n",encoding="ascii")
    print(dict(totals),flush=True)


if __name__=="__main__":
    main()
