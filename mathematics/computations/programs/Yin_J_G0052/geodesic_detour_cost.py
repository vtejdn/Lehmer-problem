"""Fold first-nongeodesic costs over the existing complete distance DAG.

No graph or state is generated.  Exact original shortest masses normalize
the geodesic transitions.  Missing nongeodesic targets contribute zero ONLY
to a declared lower bound.  A row is exact only when every nongeodesic term
and every geodesic descendant cost is known.  Complete-level minima of these
lower bounds are valid all-larger-distance lower certificates, by the
nonnegative geodesic recursion explained in D49.
"""

from fractions import Fraction as F
import json
from pathlib import Path
from time import monotonic


HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "outputs" / HERE.name
POINTS = (F(68883,40000), F(173,100))


def encoded(q):
    return [q.numerator,q.denominator]


def main():
    started=monotonic()
    data=json.loads((OUT/"shortest_first_hit_24.json").read_text(encoding="utf-8"))
    assert data["status"]=="complete" and data["completed_depth"]==24
    assert len(data["states"])==417 and data["known_rows"]==354
    states=data["states"]
    rows={r["id"]:r for r in data["rows"]}
    masses=[F(s["shortest_mass_numerator"],4**s["distance"]) for s in states]
    polynomials=[{} for _ in states]
    exact=[False]*len(states)
    exact[0]=True
    for i,s in enumerate(states[1:],1):
        if monotonic()-started>120:
            raise RuntimeError("Existing-data fold exceeded its 120-second bound")
        row=rows[i]
        p={}
        total_geo=F(0)
        all_known=True
        for edge in row["successors"]:
            if not edge["legal"]:
                continue
            if not edge["distance_known"]:
                all_known=False
                continue
            j=edge["id"]
            ratio=F(edge["integer_weight"],4)*masses[j]/masses[i]
            excess=1+states[j]["distance"]-s["distance"]
            assert excess>=0
            if excess==0:
                assert j<i
                total_geo+=ratio
                all_known=all_known and exact[j]
                for power,coefficient in polynomials[j].items():
                    p[power]=p.get(power,F(0))+ratio*coefficient
            else:
                assert j!=0
                p[excess]=p.get(excess,F(0))+ratio
        assert total_geo==1
        assert all(power>=1 and coefficient>0 for power,coefficient in p.items())
        polynomials[i]=p
        exact[i]=all_known
    evaluations=[]
    for t in POINTS:
        values=[sum((coefficient*t**power for power,coefficient in p.items()),F(0)) for p in polynomials]
        levels=[]
        for d,ids in enumerate(data["levels"]):
            least=min(ids,key=lambda i:values[i])
            largest=max(ids,key=lambda i:values[i])
            levels.append({"distance":d,"states":len(ids),"all_costs_exact":all(exact[i] for i in ids),
                           "minimum_lower_cost":encoded(values[least]),"minimum_state_id":least,
                           "maximum_lower_cost":encoded(values[largest]),"maximum_state_id":largest,
                           "minimum_exceeds_one":values[least]>1})
        evaluations.append({"t":encoded(t),"state_lower_costs":[encoded(q) for q in values],"levels":levels})
    payload={"status":"complete","scope":"existing417-state depth24 DAG only; no new graph",
             "normalization":"g_t=t^d M; G(x,y)=p_e M(y)/M(x) on geodesic edges",
             "cost":"known direct nongeodesic excess powers plus complete geodesic-prefix accumulation",
             "missing_target_policy":"omit positive unknown terms for lower bounds; exact flags propagate",
             "exact_cost_states":sum(exact),"state_costs":[{"id":i,"exact":exact[i],
                  "lower_polynomial":[[power,*encoded(c)] for power,c in sorted(p.items())]}
                  for i,p in enumerate(polynomials)],"evaluations":evaluations}
    target=OUT/"geodesic_detour_cost_24.json"
    temporary=target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload,separators=(",",":"))+"\n",encoding="utf-8")
    temporary.replace(target)
    print(json.dumps({"status":"complete","exact_cost_states":sum(exact),
          "results":[{"t":str(F(*e["t"])),
           "first_complete_level_minimum_above_one":next((x for x in e["levels"] if x["minimum_exceeds_one"]),None),
           "display_only_level_minima":[[x["distance"],float(F(*x["minimum_lower_cost"])),x["all_costs_exact"]] for x in e["levels"]]}
           for e in evaluations]}),flush=True)


if __name__=="__main__":
    main()
