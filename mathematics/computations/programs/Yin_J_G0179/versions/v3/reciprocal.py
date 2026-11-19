"""Prepare the certified integer input and run a disjoint Newton-trace slice."""

import argparse
import json
import os
import runpy
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name
V2 = runpy.run_path(str(GROUP / "versions" / "v2" / "cyclotomic_prefixes.py"))
T = Fraction(1089, 1000)
LAST = 120


def joined(values):
    return " ".join(map(str, values))


def configuration(degree, bounds):
    tests = V2["inequalities"](degree, bounds)
    half = degree // 2
    trace_limits = [0, *bounds]
    for k in range(half+1, LAST+1):
        trace_limits.append(int(degree-2 + T**k + T**-k))
    coefficient_bounds = [1]
    for k in range(1, half+1):
        coefficient_bounds.append(sum(bounds[i-1]*coefficient_bounds[k-i] for i in range(1,k+1)) // k)
    assert sum(coefficient_bounds)*max(bounds) < 2**31 - max(bounds)
    assert max(trace_limits) < 2**31-1
    assert 2*sum(coefficient_bounds)*max(degree,max(trace_limits)) < 2**63-1
    lines = [str(degree), joined(trace_limits)]
    for m in V2["ORDERS"]:
        rows = [tests["trace_box", m, k] for k in range(1,16)]
        lines += [joined([0, *(row[0] for row in rows)]), joined([0, *(row[1] for row in rows)])]
        lines += [joined([row[3], *row[2]]) for row in rows]
    return "\n".join(lines)+"\n"


def run_slice(degree, first, second, destination, binary, scratch):
    bounds = json.loads((OUTPUT/"prefixes.json").read_text())[str(degree)]["certified_all_available"]["bounds"]
    config = scratch/"input.txt"
    config.write_text(configuration(degree,bounds),encoding="ascii")
    survivors = scratch/"survivors.txt"
    command = [str(binary)] if os.name=="nt" else ["mono",str(binary)]
    proc = subprocess.run([*command,str(config),str(first),str(second),str(survivors)],
                          check=True,capture_output=True,text=True)
    summary, counts = proc.stdout.strip().splitlines()
    prefixes, orbits, endpoints = map(int,summary.split())
    first_half = [list(map(int,line.split())) for line in survivors.read_text().splitlines()]
    assert endpoints == len(first_half)
    data = {"degree":degree,"s1":first,"s2":None if second==99 else second,
            "accepted_prefixes":prefixes,"version_two_orbits":orbits,
            "higher_traces":list(map(int,counts.split())),"nonzero_at_endpoints":endpoints,
            "first_halves":first_half}
    target=destination/f"d{degree}_s{first}_{second}.json"
    with NamedTemporaryFile(mode="w",encoding="ascii",dir=destination,delete=False) as temporary:
        temporary.write(json.dumps(data,separators=(",",":"))+"\n")
    Path(temporary.name).replace(target)
    print(degree,first,second,orbits,data["higher_traces"][:3],endpoints,flush=True)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("degree",type=int,choices=(56,58),nargs="?")
    parser.add_argument("first",type=int,choices=range(7),nargs="?")
    parser.add_argument("second",type=int,nargs="?",default=99)
    args=parser.parse_args()
    destination = OUTPUT/"versions"/"v3"
    destination.mkdir(exist_ok=True,parents=True)
    compiler = (Path(os.environ["WINDIR"])/"Microsoft.NET/Framework64/v4.0.30319/csc.exe"
                if os.name=="nt" else shutil.which("mcs"))
    if not compiler:
        raise RuntimeError("The native enumeration requires csc on Windows or mcs and mono.")
    with TemporaryDirectory() as directory:
        scratch=Path(directory)
        binary=scratch/"Reciprocal.exe"
        subprocess.run([compiler,"-nologo","-optimize+","-r:System.Numerics.dll","-out:"+str(binary),
                        str(HERE/"Reciprocal.cs")],check=True)
        for degree in ((args.degree,) if args.degree is not None else (56,58)):
            for first in ((args.first,) if args.first is not None else range(7)):
                run_slice(degree,first,args.second,destination,binary,scratch)
