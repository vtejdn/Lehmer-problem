"""Distinct author verification of the d<=8 resummation at t=173/100.

Checks the supplied finite distance certificate by complete predecessor
closure and decreasing continuations, using generic quotient arithmetic.
No new graph or author BFS/resummation routine is imported.  Finite matrix
identities and explicit complete geodesic-prefix averages verify the new
cost at every distance-14 state.  This is not independent-agent review.
"""

from fractions import Fraction as F
from functools import lru_cache
import json
from time import monotonic

import verify_shortest_witness as exact


def enc(q):
    return [q.numerator, q.denominator]


def main():
    started = monotonic()

    def guard():
        if monotonic()-started > 120:
            raise RuntimeError("120-second core-verification bound reached")

    lo, hi = F(43,25), F(173,100)
    def poly(t):
        return sum(c*t**i for i,c in enumerate(exact.POLY))
    assert poly(lo)<0<poly(hi)
    assert 4*lo**3-3*hi**2-2*hi-1>0
    for _ in range(60):
        mid=(lo+hi)/2
        if poly(mid)>0: hi=mid
        else: lo=mid
    exact.LOWER, exact.UPPER = lo, hi
    allowed=lru_cache(None)(lambda x:exact.certificate(x)["strict_core"])
    data=json.loads((exact.OUT/"shortest_first_hit_24.json").read_text())
    result=json.loads((exact.OUT/"finite_core_resummation_8.json").read_text())
    assert data["status"]==result["status"]=="complete"
    assert data["completed_depth"]==24 and result["t"]==[173,100]
    states=[tuple(s["state"]) for s in data["states"]]
    assert len(states)==len(set(states))==417 and states[0]==exact.ZERO
    ids={x:i for i,x in enumerate(states)}
    ds=[s["distance"] for s in data["states"]]
    ms=[F(s["shortest_mass_numerator"],4**ds[i]) for i,s in enumerate(data["states"])]
    assert ds[0]==0 and ms[0]==1 and all(allowed(x) for x in states)
    assert data["levels"]==[[i for i,d in enumerate(ds) if d==n] for n in range(25)]
    inverse=(1,1,1,-1)
    # Completeness: every predecessor of every certified distance<=23 state
    # is present with the necessary upper bound.  Existence is supplied by
    # a decreasing legal successor at each nonzero state.
    predecessor_tests=0
    for i,y in enumerate(states):
        guard()
        if ds[i]>=24: continue
        for e in (-1,0,1):
            ye=tuple(a-(e if k==0 else 0) for k,a in enumerate(y))
            x=exact.times(inverse,ye)
            assert exact.step(x,e)==y
            predecessor_tests+=1
            if allowed(x):
                assert x in ids and ds[ids[x]]<=ds[i]+1
    edges={}
    for i,x in enumerate(states[1:],1):
        edges[i]=[]
        geo_mass=F(0)
        for e in (-1,0,1):
            y=exact.step(x,e)
            if not allowed(y): continue
            j=ids.get(y)
            weight=F(2 if e==0 else 1,4)
            edges[i].append((j,weight,e,y))
            if j is not None:
                assert ds[j]>=ds[i]-1
                if ds[j]==ds[i]-1:geo_mass+=weight*ms[j]
        assert geo_mass==ms[i]>0

    t=F(173,100)
    core=[i for i in range(1,417) if ds[i]<=8]
    assert core==result["core_states"] and len(core)==46
    pos={i:j for j,i in enumerate(core)}
    u=list(map(lambda q:F(*q),result["core_u"]))
    z=[[F(*q) for q in row] for row in result["core_inverse"]]
    baseline=[F(*q) for q in result["baseline"]]
    feedback=[F(*q) for q in result["core_exit_feedback"]]
    bcc=[[F(0) for _ in core] for _ in core]
    rhs=[F(0)]*46
    exit_rhs=[F(0)]*46
    exits=set()
    for i in core:
        for j,w,e,y in edges[i]:
            assert j is not None
            if j==0:rhs[pos[i]]+=t*w
            elif j in pos:bcc[pos[i]][pos[j]]+=w
            else:
                exits.add(j)
                exit_rhs[pos[i]]+=t*w*baseline[j]
    a=[[F(i==j)-t*bcc[i][j] for j in range(46)] for i in range(46)]
    assert [[enc(q) for q in row] for row in bcc]==result["core_matrix"]
    assert min(u)>0 and all(q>=0 for row in z for q in row)
    # Right multiplication is distinct from the producer's column solves.
    for i in range(46):
        guard()
        for j in range(46):
            assert sum((z[i][k]*a[k][j] for k in range(46)),F(0))==(i==j)
        assert sum((a[i][j]*u[j] for j in range(46)),F(0))==rhs[i]
        assert sum((a[i][j]*feedback[j] for j in range(46)),F(0))==exit_rhs[i]
    assert sorted(exits)==result["exit_targets"]
    assert [enc(q) for q in exit_rhs]==result["core_exit_rhs"]
    for i in core:assert baseline[i]==u[pos[i]]
    for i in range(1,417):
        if i in pos:continue
        assert baseline[i]>0
        assert baseline[i]==sum((t*w*baseline[j] for j,w,e,y in edges[i]
                                if j is not None and ds[j]==ds[i]-1),F(0))

    # Positive u and a geodesic path in C to an actual zero edge pay the
    # strict finite-killing assertion.  Check the explicit eight-step row.
    surv=[F(1)]*46
    for _ in range(8):
        surv=[sum((t*bcc[i][j]*u[j]/u[i]*surv[j] for j in range(46)),F(0)) for i in range(46)]
    assert [enc(q) for q in surv]==result["normalized_core_survival8"]
    assert max(surv)<F(893,1000)

    @lru_cache(None)
    def paths(i):
        if i in pos:return [((i,),F(1))]
        out=[]
        for j,w,e,y in edges[i]:
            if j is not None and ds[j]==ds[i]-1:
                out.extend(((i,)+path,t*w*weight) for path,weight in paths(j))
        assert 0<len(out)<=100000
        guard()
        return out

    def delta(i):
        total=F(0)
        for j,w,e,y in edges[i]:
            assert j is not None  # decisive rows have no omitted target
            if ds[j]>=ds[i]:total+=t*w*baseline[j]/baseline[i]
        return total

    checked=[]
    max_prefixes=0
    for i in data["levels"][14]:
        pref=paths(i)
        max_prefixes=max(max_prefixes,len(pref))
        total_prob=F(0)
        cost=F(0)
        for path,w in pref:
            assert len(path)==7 and ds[path[-1]]==8
            mass=w*baseline[path[-1]]/baseline[i]
            total_prob+=mass
            cost+=mass*(sum((delta(j) for j in path[:-1]),F(0))+
                        feedback[pos[path[-1]]]/u[pos[path[-1]]])
        assert total_prob==1
        row=result["state_costs"][i]
        assert row["exact"] and cost==F(*row["lower_cost"])
        checked.append({"state":states[i],"id":i,"prefixes":len(pref),"exact_cost":enc(cost)})
    minimum=min(F(*row["exact_cost"]) for row in checked)
    assert len(checked)==20 and minimum>F(11,10)
    report={"status":"passed","scope":"distinct AUTHOR finite-core/matrix/prefix check, not independent-agent review",
            "t":[173,100],"root_interval":[str(lo),str(hi)],
            "distance_certificate":"all417 supplied states through24; predecessor closure, decreasing continuations and all shortest masses",
            "predecessor_tests":predecessor_tests,"core_states":46,"exit_targets":len(exits),
            "maximum_exit_distance":max(ds[i] for i in exits),
            "strict_core_survival8":enc(max(surv)),"core_survival8_bound":[893,1000],
            "level14":checked,"maximum_geodesic_prefix_count":max_prefixes,
            "complete_level14_minimum":enc(minimum),"rational_lower_bound":[11,10],
            "method":"generic quotient/interval arithmetic, exact matrix residuals and all six-step geodesic-prefix averages",
            "limits":"fixed t only; no new graph, global upper bound, critical mean or R_f assertion"}
    target=exact.OUT/"core_resummation_check.json"
    tmp=target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    tmp.replace(target)
    print(json.dumps({"status":"passed","predecessor_tests":predecessor_tests,
                      "core_states":46,"exit_targets":len(exits),"level14_states":20,
                      "maximum_geodesic_prefix_count":max_prefixes,
                      "minimum_display":float(minimum),"minimum_exceeds":"11/10"}))


if __name__=="__main__":
    main()
