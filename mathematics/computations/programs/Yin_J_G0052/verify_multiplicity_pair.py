"""Exact author check of the two-row multiplicity-aware obstruction.

Uses the retained generic polynomial/direct-word verifier, not BFS helpers.
Only words of length at most seven at three additional specified states are
enumerated.  The existing depth24 data are comparison input, not an oracle
for the independent distance and mass calculation.  No new graph or
numerical optimization is run; this is not independent-agent review.
"""

from fractions import Fraction as F
import json

import verify_shortest_witness as exact


U = (-2, 1, 0, 0)
LEFT = (-1, -2, 1, 0)
CENTER = (0, -2, 1, 0)
RIGHT = (1, -2, 1, 0)


def main():
    lo, hi = F(43, 25), F(173, 100)
    def polynomial(t):
        return sum(c*t**i for i,c in enumerate(exact.POLY))
    assert polynomial(lo)<0<polynomial(hi)
    assert 4*lo**3-3*hi**2-2*hi-1>0
    for _ in range(20):
        mid=(lo+hi)/2
        if polynomial(mid)>0:
            hi=mid
        else:
            lo=mid
    exact.LOWER, exact.UPPER = lo, hi
    assert [exact.step(U,e) for e in (-1,0,1)]==[LEFT,CENTER,RIGHT]
    certificates=[exact.certificate(x) for x in (U,LEFT,CENTER,RIGHT)]
    assert [c["strict_core"] for c in certificates]==[True,False,True,True]
    targets=((U,7,8),(CENTER,6,4),(RIGHT,7,2))
    data=json.loads((exact.OUT/"shortest_first_hit_24.json").read_text(encoding="utf-8"))
    assert data["status"]=="complete" and data["known_rows"]==354
    results=[]
    for x,d,m in targets:
        direct=exact.direct_words(x,d)
        assert direct[-1]["length"]==d
        assert F(*direct[-1]["mass"])==F(m,4**d)
        supplied=next(s for s in data["states"] if tuple(s["state"])==x)
        assert supplied["distance"]==d and supplied["shortest_mass_numerator"]==m
        results.append({"state":x,"distance":d,"mass_numerator_over_4_to_d":m,"direct_word_checks":direct})
    # The previous witness supplies d=2,m=1, then d=1,m=1 and d=4,m=2.
    previous=json.loads((exact.OUT/"shortest_first_hit_witness_check.json").read_text(encoding="utf-8"))
    assert previous["status"]=="passed" and previous["row_coefficients"]==[[-2,2],[1,1]]
    assert F(68883,40000)>F(17,10)>F(4,3)
    assert 51**3>2*40**3
    report={"status":"passed","scope":"distinct exact author two-row check, no new BFS or optimization",
            "root_interval":[str(lo),str(hi)],"root_refinements":20,
            "certificates":certificates,"direct_checks":results,
            "coordinates":{"a":"lambda*2^(2*theta)","z":"2^theta"},
            "row_at_x":"a/4+z/(2*a^2)","row_at_u":"a/(2*z)+1/(4*z^2)",
            "theta_nonpositive_lower_bound_for_max":"3/4",
            "theta_nonnegative_lower_bound_at_x":"3/(4*cuberoot(2)) > 10/17",
            "conclusion":"for all lambda>0 and real theta, some specified row violates t B0 W<=W for every t>=17/10",
            "limitations":"finite global-candidate obstruction only; no finite-exception or all-time mean conclusion"}
    path=exact.OUT/"shortest_multiplicity_pair_check.json"
    path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report),flush=True)


if __name__=="__main__":
    main()
