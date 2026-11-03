"""Exact ordered-cycle controls and arbitrary-length path surgery."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations, product
import json
import sympy as sp

t=sp.Symbol('t')


def energy(v):
    return sp.expand(sum(v[i,j]**2 for i in range(v.rows) for j in range(i+1,v.rows)))


def mutate(v,i,inverse=False):
    a=v[i,i+1]
    q=sp.eye(v.rows)
    q[i:i+2,i:i+2]=sp.Matrix([[-a,1],[1,0]]) if inverse else sp.Matrix([[0,1],[1,-a]])
    w=q.T*v*q
    assert w.is_upper and all(w[j,j]==1 for j in range(w.rows))
    return w,q


def cycle(order,positive_index=None):
    n=len(order)
    v=sp.eye(n)
    if positive_index is None:positive_index=n-3
    for k in range(n):
        i,j=sorted((order[k],order[(k+1)%n]))
        v[i,j]=1 if k==positive_index else -1
    return v


def characteristic(v):
    return sp.Poly((-v.inv()*v.T).charpoly(t).as_expr(),t)


def main(output_path=None):
    records=[]
    for n in range(3,13):
        v=cycle(list(range(n)))
        initial=v.copy()
        p=sp.eye(n)
        values=[int(energy(v))]
        moves=[(i,False) for i in range(n-3)]+[(n-3,True)]
        for i,inv in moves:
            v,q=mutate(v,i,inv)
            p=p*q
            values.append(int(energy(v)))
        assert v==p.T*initial*p
        assert abs(p.det())==1
        assert characteristic(v)==characteristic(initial)
        records.append({'length':n,'moves':moves,'energies':values,
                        'initial_polynomial':str(characteristic(initial).as_expr()),
                        'final_matrix':[list(map(int,v.row(i))) for i in range(n)]})
    counter=cycle([0,2,1,3],positive_index=2)
    target=sp.Poly((t*t+1)**2,t)
    assert characteristic(counter)==target
    matches=[]
    inspected=0
    locations=list(combinations(range(4),2))
    for size in range(4):
        for support in combinations(locations,size):
            for signs in product((-1,1),repeat=size):
                v=sp.eye(4)
                for (i,j),sign in zip(support,signs):v[i,j]=sign
                inspected+=1
                if characteristic(v)==target:matches.append(v.tolist())
    assert not matches
    out={'consecutive_cycles':records,
         'rank_four_counterexample':{'matrix':[list(map(int,counter.row(i))) for i in range(4)],'polynomial':str(target.as_expr()),
                                    'all_energy_at_most_three_matrices':inspected,'matching_polynomials':len(matches)}}
    (Path(output_path) if output_path is not None else _J_OUTPUT / 'controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'sequences':[(r['length'],r['energies']) for r in records],
                      'counterexample':out['rank_four_counterexample']},indent=2))


if __name__=='__main__':main()
