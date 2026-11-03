"""Integer/Fraction certificate checker. No NumPy or discovery outputs trusted."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json,platform
import core

def main():
    start=perf_counter();base=(_J_PROGRAM / 'verify.py').parent
    data=json.loads(((_J_OUTPUT / 'certificate.json')).read_text())
    assert data['pattern_cap']==50000
    pass
    assert data['coordinate_box']==[-8,8,-7,7]
    xp,yp,patterns=core.all_patterns(cap=data['pattern_cap'])
    assert data['axis_intervals']==[len(xp)-1,len(yp)-1]
    assert len(patterns)==data['distinct_patterns']
    q=data['q'];assert type(q) is int and q==97
    seen=set();min_slack=None;max_rows=max_columns=0
    for case in data['certificates']:
        assert perf_counter()-start<60, 'verification time cap reached'
        a=tuple(tuple(row) for row in case['matrix'])
        assert a in patterns and a not in seen and a
        seen.add(a)
        assert tuple(case['example_cell'])==patterns[a]
        assert all(type(x) is int and x in (0,1,2,4) for row in a for x in row)
        v=case['positive_vector']
        assert len(v)==len(a) and all(type(x) is int and x>0 for x in v)
        m=core.gram(a)
        for i,row in enumerate(m):
            slack=q*v[i]-sum(x*y for x,y in zip(row,v))
            assert slack>=0
            min_slack=slack if min_slack is None else min(slack,min_slack)
        max_rows=max(max_rows,len(a));max_columns=max(max_columns,len(a[0]))
    assert seen=={a for a in patterns if a}
    assert len(seen)==data['nonempty_patterns']
    lower=data['actual_lower_witness'];r=tuple(lower['representative'])
    assert len(r)==4 and all(type(x) is int for x in r)
    rs=core.sigma(r)
    assert core.sign(r)>=0 and core.sign(core.sub(core.scale(core.ONE,3),r))>=0
    assert core.sign(rs)>=0 and core.sign(core.sub(core.scale(core.ONE,2),rs))>=0
    a=core.matrix(core.mask_at(0,r),core.mask_at(1,rs))
    assert a==tuple(tuple(row) for row in lower['matrix'])
    v=lower['vector'];assert len(v)==len(a) and all(type(x) is int for x in v)
    m=core.gram(a)
    denominator=sum(x*x for x in v)
    numerator=sum(x*y*m[i][j] for i,x in enumerate(v) for j,y in enumerate(v))
    assert denominator>0 and lower['gram_lower']==96 and numerator>96*denominator
    # Analytic comparison: ||K||^2=(3+2sqrt(2))/8 > 7/10;
    # sqrt(97)/16 < 5/8 < 7/10, all from rational squared bounds.
    assert 97<100 and core.F(5,8)<core.F(7,10)
    assert core.F(13,10)**2<2
    result={'status': 'passed', 'arithmetic': 'integer/Fraction only', 'phase_cells': (len(xp) - 1) * (len(yp) - 1), 'distinct_matrices': len(seen), 'axis_intervals': [len(xp) - 1, len(yp) - 1], 'maximum_shape': [max_rows, max_columns], 'integer_q': q, 'minimum_integer_slack': min_slack, 'actual_lower_representative': list(r), 'lower_Rayleigh_numerator': numerator, 'lower_Rayleigh_denominator': denominator, 'bound': 'sqrt(96)/16 < ||K^2|| <= sqrt(97)/16'}
    ((_J_OUTPUT / 'verified.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
