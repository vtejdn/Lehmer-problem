"""Distinct exact AUTHOR certificate for the complete distance-nine level.

Direct words through nine certify level completeness.  Unrestricted split
word sums (halves at most eight) independently check all required distances
and shortest masses through fifteen.  Explicit shortest-word averaging
checks the accumulated detour costs, without the author BFS/DAG routines.
Verification bounds: 100000 retained words/states, 120 seconds.  No larger
actual-core graph is generated and no independent-agent review is claimed.
"""

from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from time import monotonic

import verify_shortest_witness as exact


T = F(68883,40000)


def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))


def minus(a,b):
    return tuple(x-y for x,y in zip(a,b))


def main():
    started=monotonic()
    def guard():
        if monotonic()-started>120:
            raise RuntimeError("120-second verification bound reached")
    lo,hi=F(43,25),F(173,100)
    def poly(t):
        return sum(c*t**i for i,c in enumerate(exact.POLY))
    assert poly(lo)<0<poly(hi)
    assert 4*lo**3-3*hi**2-2*hi-1>0
    for _ in range(60):
        mid=(lo+hi)/2
        if poly(mid)>0: hi=mid
        else: lo=mid
    exact.LOWER,exact.UPPER=lo,hi
    allowed=lru_cache(None)(lambda x: exact.certificate(x)["strict_core"])
    inverse=(1,1,1,-1)
    inverse_powers=[(1,0,0,0)]
    for _ in range(9):
        inverse_powers.append(exact.times(inverse_powers[-1],inverse))
    distances={exact.ZERO:0}
    numerators={exact.ZERO:1}
    shortest_words=defaultdict(list)
    for n in range(1,10):
        for word in product((-1,0,1),repeat=n):
            x=tuple(-sum(e*inverse_powers[j+1][coordinate] for j,e in enumerate(word))
                    for coordinate in range(4))
            if x in distances and distances[x]<n:
                continue
            if not allowed(x):
                continue
            if x not in distances:
                distances[x]=n
                numerators[x]=0
            numerators[x]+=2**word.count(0)
            shortest_words[x].append(word)
        guard()
        assert len(distances)<=100000
    level9=sorted(x for x,d in distances.items() if d==9)
    assert len(level9)==10

    # All unrestricted forward word endpoint masses for split halves<=8.
    endpoint_masses=[{exact.ZERO:1}]
    for n in range(1,9):
        nxt=defaultdict(int)
        for x,value in endpoint_masses[-1].items():
            for e in (-1,0,1):
                nxt[exact.step(x,e)]+=value*(2 if e==0 else 1)
        assert len(nxt)<=100000
        endpoint_masses.append(dict(nxt))
        guard()
    beta_powers=[(1,0,0,0)]
    for _ in range(15):
        beta_powers.append(exact.times(beta_powers[-1],(0,1,0,0)))
    transformed={}
    for n in range(1,16):
        a=n//2; b=n-a
        transformed[n]=[(exact.times(beta_powers[b],x),w) for x,w in endpoint_masses[a].items()]

    targets=set(distances)
    legal_edges={}
    for x in list(distances):
        if x==exact.ZERO: continue
        legal_edges[x]=[]
        for e in (-1,0,1):
            y=exact.step(x,e)
            if allowed(y):
                targets.add(y)
                legal_edges[x].append((e,y))
    assert len(targets)==73
    verified={exact.ZERO:(0,1)}
    for x in sorted(targets):
        if x==exact.ZERO: continue
        for n in range(1,16):
            guard()
            target=tuple(-c for c in exact.times(beta_powers[n],x))
            right=endpoint_masses[n-n//2]
            mass=sum(weight*right.get(minus(target,endpoint),0) for endpoint,weight in transformed[n])
            if mass:
                verified[x]=(n,mass)
                break
        else:
            raise AssertionError(("No claimed <=15 continuation",x))
    assert max(d for d,m in verified.values())==15
    for x,d in distances.items():
        assert verified[x]==(d,numerators[x])

    author=json.loads((exact.OUT/"shortest_first_hit_24.json").read_text(encoding="utf-8"))
    assert author["status"]=="complete"
    author_states={tuple(s["state"]):(i,s) for i,s in enumerate(author["states"])}
    assert set(distances)=={x for x,(_,s) in author_states.items() if s["distance"]<=9}
    for x,(d,m) in verified.items():
        _,s=author_states[x]
        assert (s["distance"],s["shortest_mass_numerator"])==(d,m)

    def mass(x):
        d,m=verified[x]
        return F(m,4**d)
    def local_defect_polynomial(x):
        d,_=verified[x]
        out=defaultdict(F)
        for e,y in legal_edges[x]:
            dy,_=verified[y]
            excess=1+dy-d
            assert excess>=0
            if excess:
                out[excess]+=F(2 if e==0 else 1,4)*mass(y)/mass(x)
        return out
    author_cost=json.loads((exact.OUT/"geodesic_detour_cost_24.json").read_text(encoding="utf-8"))
    results=[]
    for x in level9:
        coefficients=defaultdict(F)
        total_probability=F(0)
        for word in shortest_words[x]:
            probability=F(2**word.count(0),4**9)/mass(x)
            total_probability+=probability
            current=x
            for j,e in enumerate(word):
                assert verified[current][0]==9-j
                for power,c in local_defect_polynomial(current).items():
                    coefficients[power]+=probability*c
                current=exact.step(current,e)
            assert current==exact.ZERO
        assert total_probability==1
        value=sum((c*T**power for power,c in coefficients.items()),F(0))
        assert value>1
        i,_=author_states[x]
        supplied=author_cost["state_costs"][i]
        assert supplied["exact"]
        assert {power:F(num,den) for power,num,den in supplied["lower_polynomial"]}==dict(coefficients)
        results.append({"state":x,"distance":9,"shortest_words":shortest_words[x],
                        "cost_polynomial":[[power,c.numerator,c.denominator] for power,c in sorted(coefficients.items())],
                        "cost_at_t0":[value.numerator,value.denominator]})
    least=min(F(*r["cost_at_t0"]) for r in results)
    assert least==F(36193899689180879400344643,26214400000000000000000000)
    assert least>F(69,50)>1
    report={"status":"passed","scope":"distinct exact AUTHOR level9 and detour-cost verification",
            "root_interval":[str(lo),str(hi)],"direct_word_depth":9,"complete_states_through9":len(distances),
            "split_word_maximum_length":15,"largest_half_endpoint_set":max(map(len,endpoint_masses)),
            "verified_target_count":len(verified),
            "verified_distances_and_masses":[{"state":x,"distance":d,"mass_numerator_over_4_to_d":m}
                 for x,(d,m) in sorted(verified.items())],
            "t0":[T.numerator,T.denominator],"complete_level9":results,
            "exact_level9_minimum":[least.numerator,least.denominator],"rational_lower_bound":"69/50",
            "extension":"the nonnegative geodesic recursion propagates this lower bound to every d>=9 and every t>=t0",
            "limits":"not unboundedness, not a recurrence/mean classification, not an independent-agent review"}
    path=exact.OUT/"geodesic_level9_check.json"
    path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k not in ("root_interval","complete_level9","verified_distances_and_masses")}),flush=True)


if __name__=="__main__":
    main()
