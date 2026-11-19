"""Stream a primitive, sign-normalized degree-66 Newton box at measure 1091/1000."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import json
from math import comb
import os
from pathlib import Path
import runpy
import shutil
import subprocess
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions"
T = Fraction(1091, 1000)
FIELDS = ("representatives", "through_34", "through_42", "endpoint_zero",
          "later_trace_exclusion", "quadratic_cyclotomic", "modular_graeffe", "fallback")


def configuration(bounds):
    if len(bounds) != 33 or any(not j <= 2*b+1 < 2*j for j,b in enumerate(bounds,1) if j>=18):
        raise ValueError("Each suffix residue must have one or two representatives.")
    if any(bounds[j-1] >= j for j in range(18,34)):
        raise ValueError("Vanishing outside a power in the prefix must force the entire substitution.")
    coeff = [1]
    for k in range(1,34):
        coeff.append(sum(bounds[j-1]*coeff[k-j] for j in range(1,k+1))//k)
    if max(bounds)*(1+sum(coeff)) >= 2**31 or 2*sum(coeff) >= 2**31:
        raise ArithmeticError("Signed Newton divisions and endpoint evaluations require a wider type.")
    limits = [0,*bounds,*(int(64+T**k+T**-k) for k in range(34,121))]
    full = coeff+coeff[-2::-1]
    for k in range(34,121):
        absolute = (k*full[k] if k<=66 else 0) + sum(
            full[i]*limits[k-i] for i in range(1,min(k,67)))
        if absolute >= (2**31 if k<=42 else 2**63):
            raise ArithmeticError("The reflected Newton sum requires a wider type.")
    rows = [limits]
    for g in range(1,11):
        cut = T**(2**g)
        values = [int(comb(66,j)*cut) for j in range(34)]
        rows.append([b if b < 2**63 else -1 for b in values])
    return "\n".join(" ".join(map(str,row)) for row in rows)+"\n"


def compile_worker(scratch):
    if os.name == "nt":
        compiler = Path(os.environ["WINDIR"])/"Microsoft.NET/Framework64/v4.0.30319/csc.exe"
    else:
        compiler = shutil.which("mcs")
    binary = scratch/"Sieve66.exe"
    subprocess.run([compiler,"-nologo","-optimize+","-checked-","-out:"+str(binary),
                    HERE/"Sieve66.cs"],check=True)
    if os.name == "nt":
        dotnet = shutil.which("dotnet")
        if dotnet:
            versions = subprocess.check_output([dotnet,"--list-runtimes"],text=True).splitlines()
            versions = [v.split()[1] for v in versions if v.startswith("Microsoft.NETCore.App ")]
            if versions:
                version = max(versions,key=lambda v:tuple(map(int,v.split("."))))
                runtime = {"runtimeOptions":{"framework":{"name":"Microsoft.NETCore.App","version":version}}}
                binary.with_suffix(".runtimeconfig.json").write_text(json.dumps(runtime),encoding="ascii")
                return [dotnet,binary]
        return [binary]
    return ["mono",binary]


def fallback(rows):
    finish = runpy.run_path(str(HERE.parent/"v3"/"finish.py"))
    extend = runpy.run_path(str(HERE.parent/"v6"/"extend.py"))
    verify = runpy.run_path(str(HERE.parent/"v6"/"verify_totals.py"))
    divide = finish["divide"]
    polynomials = {n:f for n,f,_ in finish["cyclotomics"](66)}
    polynomials.update(verify["remaining_cyclotomics"](66,divide))
    tests = [(n,phi,finish["bit_polynomial"](phi)) for n,phi in polynomials.items()]
    labels, unresolved, witnesses = {}, [], []
    for half in rows:
        full = half+half[-2::-1]
        bits = finish["bit_polynomial"](full)
        for n, phi, phi2 in tests:
            if (finish["bit_remainder"](bits,phi2) == 0
                    and not any(divide(full,phi)[1])):
                key = f"phi_{n}"
                break
        else:
            for g in range(13):
                cut = T**(2**g)
                index = next((j for j,a in enumerate(full)
                              if abs(a)*cut.denominator > comb(66,j)*cut.numerator),None)
                if index is not None:
                    key = f"exact_graeffe_{g}"
                    witnesses.append({"half":half,"round":g,"index":index,"coefficient":full[index],
                                      "upper":int(comb(66,index)*cut)})
                    break
                if g<12:
                    full = extend["graeffe_packed"](full)
            else:
                key = "unresolved"
                unresolved.append(half)
        labels[key] = labels.get(key,0)+1
    return labels, unresolved, witnesses


def run_slice(first, command, config, audit, dest=None):
    dest = OUTPUT/"v9" if dest is None else dest
    name = "slice_"+"_".join(map(str,first))
    with TemporaryDirectory(dir=dest) as folder:
        uncategorized = Path(folder)/"survivors.txt"
        cmd = [*command,config,uncategorized,"audit" if audit else "search",*map(str,first)]
        raw = subprocess.check_output(cmd,text=True).split()
        if len(raw)!=len(FIELDS):
            raise ValueError("Incomplete native count vector")
        counts = dict(zip(FIELDS,map(int,raw)))
        rows = [list(map(int,line.split())) for line in uncategorized.read_text().splitlines()]
        if counts["through_42"]!=sum(counts[k] for k in FIELDS[3:]) or len(rows)!=counts["fallback"]:
            raise ArithmeticError("The disjoint classification totals disagree.")
        labels, unresolved, witnesses = fallback(rows) if rows else ({},[],[])
        data = {"degree":66,"cutoff":[1091,1000],"prefix":first,"counts":counts,
                "fallback_classifications":labels,"exact_witnesses":witnesses,"unresolved":unresolved}
        tmp = Path(folder)/"report.json"
        tmp.write_text(json.dumps(data,indent=2)+"\n",encoding="ascii")
        tmp.replace(dest/(name+".json"))
        print(name,counts,len(unresolved),flush=True)
        return data


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--prefix",type=int,nargs="+")
    cli.add_argument("--workers",type=int,default=1)
    cli.add_argument("--audit",action="store_true")
    cli.add_argument("--resume",action="store_true",help="Reuse existing disjoint pair reports")
    args=cli.parse_args()
    source=json.loads((OUTPUT/"v7"/"boxes.json").read_text())["66"]["certified_all_available"]
    bounds=source["bounds"]
    if args.workers<1:
        cli.error("The worker count must be positive.")
    if args.prefix:
        if len(args.prefix)>17 or any(abs(x)>b for x,b in zip(args.prefix,bounds)):
            cli.error("The fixed prefix falls outside the certified box.")
        slices=[tuple(args.prefix)]
    else:
        slices=[(x,y) for x in range(bounds[0],-1,-1)
                for y in range(-bounds[1],bounds[1]+1) if (x-y)%2==0]
    dest=OUTPUT/"v9"
    dest.mkdir(parents=True,exist_ok=True)
    if args.resume:
        slices=[p for p in slices if not (dest/("slice_"+"_".join(map(str,p))+".json")).exists()]
    with TemporaryDirectory(dir=dest) as folder:
        scratch=Path(folder)
        command=compile_worker(scratch)
        config=scratch/"limits.txt"
        config.write_text(configuration(bounds),encoding="ascii")
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            list(pool.map(lambda p:run_slice(p,command,config,args.audit),slices))


if __name__=="__main__":
    main()
