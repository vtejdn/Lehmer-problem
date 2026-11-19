"""Enumerate and finish disjoint degree-60 and degree-62 trace slices."""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import json
from math import comb
import os
from pathlib import Path
import runpy
import shutil
import subprocess
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "v3"
CONFIG = runpy.run_path(str(V3 / "reciprocal.py"))["configuration"]
FINISH = runpy.run_path(str(V3 / "finish.py"))
OUTPUT = HERE.parents[3] / "outputs" / HERE.parents[1].name / "versions" / "v6"


def graeffe_packed(f):
    """Graeffe via exact signed Kronecker substitution and centered decoding."""
    bits = ((2*len(f))*max(map(abs,f))**2).bit_length()
    base = 1 << bits
    even = odd = 0
    for c in reversed(f[::2]):
        even = (even << bits) + c
    for c in reversed(f[1::2]):
        odd = (odd << bits) + c
    packed = even*even - base*odd*odd
    result = []
    for _ in f:
        c = packed & (base-1)
        if c >= base//2:
            c -= base
        result.append(c)
        packed = (packed-c) >> bits
    assert packed == 0
    return result


def finish_vector(half, degree, tests, binomials):
    f = half + half[-2::-1]
    bits = FINISH["bit_polynomial"](f)
    for order, poly, mod2 in tests:
        if FINISH["bit_remainder"](bits, mod2) == 0 and not any(FINISH["divide"](f,poly)[1]):
            return f"cyclotomic_{order}"
    num, den = 1089, 1000
    for k in range(13):
        if any(abs(c)*den > b*num for c,b in zip(f,binomials)):
            return f"graeffe_{k}"
        if k < 12:
            f = graeffe_packed(f)
            num, den = num*num, den*den
    return "unresolved"


def enumerate_slice(job):
    degree, first, binary = job
    bounds = json.loads((OUTPUT/"boxes.json").read_text())[str(degree)]["certified_all_available"]["bounds"]
    with TemporaryDirectory(dir=OUTPUT) as temporary:
        scratch = Path(temporary)
        config = scratch/"input.txt"
        config.write_text(CONFIG(degree,bounds),encoding="ascii")
        survivors = scratch/"endpoints.txt"
        command = [str(binary)] if os.name=="nt" else ["mono",str(binary)]
        proc = subprocess.run([*command,str(config),str(first),"99",str(survivors)],
                              check=True,capture_output=True,text=True)
        summary, counts = proc.stdout.strip().splitlines()
        prefixes, orbits, endpoint_count = map(int,summary.split())
        higher = list(map(int,counts.split()))
        print("enumerated",degree,first,orbits,higher[-1],endpoint_count,flush=True)
        tests = FINISH["cyclotomics"](degree)
        binomials = [comb(degree,j) for j in range(degree+1)]
        labels = Counter()
        unresolved = []
        with survivors.open(encoding="ascii") as rows:
            for line in rows:
                half = list(map(int,line.split()))
                label = finish_vector(half,degree,tests,binomials)
                labels[label] += 1
                if label == "unresolved":
                    unresolved.append(half)
        assert sum(labels.values()) == endpoint_count
        data = {"degree":degree, "s1":first, "accepted_prefixes":prefixes, "prefix_survivors":orbits,
                "higher_traces":higher, "nonzero_at_endpoints":endpoint_count,
                "classifications":dict(labels), "unresolved":unresolved}
        path = OUTPUT/f"d{degree}_s{first}.json"
        temporary_result = scratch/"result.json"
        temporary_result.write_text(json.dumps(data,indent=2)+"\n",encoding="ascii")
        temporary_result.replace(path)
        print("finished",degree,first,sum(labels.values()),len(unresolved),flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("degree",type=int,choices=(60,62))
    parser.add_argument("--first",type=int,nargs="+")
    parser.add_argument("--workers",type=int,default=1)
    args = parser.parse_args()
    rows=json.loads((OUTPUT/"boxes.json").read_text())
    limit=rows[str(args.degree)]["certified_all_available"]["bounds"][0]
    firsts = list(reversed(range(limit+1))) if args.first is None else args.first
    if any(not 0 <= first <= limit for first in firsts) or len(set(firsts))!=len(firsts):
        parser.error("Each first sum must be distinct and in the certified range.")
    compiler = (Path(os.environ["WINDIR"])/"Microsoft.NET/Framework64/v4.0.30319/csc.exe"
                if os.name=="nt" else shutil.which("mcs"))
    if not compiler:
        raise RuntimeError("The native enumeration requires csc on Windows or mcs and mono.")
    with TemporaryDirectory() as directory:
        binary = Path(directory)/"Reciprocal.exe"
        subprocess.run([compiler,"-nologo","-optimize+","-r:System.Numerics.dll","-out:"+str(binary),
                        str(V3/"Reciprocal.cs")],check=True)
        jobs=[(args.degree,first,binary) for first in firsts]
        if args.workers == 1:
            for job in jobs:
                enumerate_slice(job)
        else:
            with ProcessPoolExecutor(max_workers=args.workers) as pool:
                list(pool.map(enumerate_slice,jobs))
