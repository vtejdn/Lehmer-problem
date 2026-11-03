"""Separately implemented dense congruence replay; same authoring agent."""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

import sympy as sp

HERE = _J_OUTPUT
T = sp.Symbol("t")
L = T**10 + T**9 - T**7 - T**6 - T**5 - T**4 - T**3 + T + 1


def energy(v):
    return sum(int(v[i, j])**2 for i in range(v.rows) for j in range(i+1, v.cols))


def dense_move(v, move):
    i = move["index"]
    a = v[i, i+1]
    p = sp.eye(v.rows)
    p[i:i+2, i:i+2] = sp.Matrix([[-a, 1], [1, 0]]) if move["inverse"] else sp.Matrix([[0, 1], [1, -a]])
    d = sp.diag(*move.get("signs", [1]*v.rows))
    p = p*d
    w = p.T*v*p
    assert w.is_upper and all(w[j, j] == 1 for j in range(w.rows))
    assert abs(p.det()) == 1
    return w, p


def gauge(v):
    # Depth-first gauge, intentionally different from the breadth-first
    # normalization in the discovery program. Unbalanced cycles are checked.
    signs = {}
    for root in range(v.rows):
        if root in signs:
            continue
        signs[root] = 1
        stack = [root]
        while stack:
            i = stack.pop()
            for j in range(v.rows):
                if i == j:
                    continue
                a = v[min(i,j), max(i,j)]
                if a and j not in signs:
                    signs[j] = -int(sp.sign(a))*signs[i]
                    stack.append(j)
    d = sp.diag(*(signs[j] for j in range(v.rows)))
    w = d*v*d
    return tuple(w), all(w[i,j] <= 0 for i in range(v.rows) for j in range(i+1,v.rows))


def main():
    paths = json.loads((HERE/'paths.json').read_text())
    checked_moves = goals = 0
    for record in paths['records']:
        start = sp.Matrix(record['initial_matrix'])
        assert sp.expand((-start.inv()*start.T).charpoly(T).as_expr()-L) == 0
        ptotal = sp.diag(*record['initial_signs'])
        current = ptotal.T*start*ptotal
        for move in record['moves']:
            w,p = dense_move(current,move)
            assert energy(w) <= energy(current)
            ptotal = ptotal*p
            current = w
            checked_moves += 1
        assert current == sp.Matrix(record['final_matrix'])
        assert ptotal.T*start*ptotal == current
        assert energy(current) == record['final_energy']
        _,balanced = gauge(current)
        if record['outcome']=='goal':
            assert balanced
            goals += 1
    assert goals == 44 and len(paths['records']) == 66

    barrier = json.loads((HERE/'barrier.json').read_text())
    base = sp.Matrix(barrier['matrix'])
    assert sp.expand((-base.inv()*base.T).charpoly(T).as_expr()-L) == 0
    states = [sp.Matrix(10,10,s) for s in barrier['closed_plateau']['states']]
    canonical = {gauge(s)[0] for s in states}
    assert len(canonical)==50 and gauge(base)[0] in canonical
    transitions = 0
    for v in states:
        assert energy(v)==10 and not gauge(v)[1]
        for i in range(9):
            for inverse in (False,True):
                w,_ = dense_move(v,{'index':i,'inverse':inverse})
                if energy(w)<=10:
                    assert gauge(w)[0] in canonical
                    transitions += 1
    current=base
    d=sp.diag(*barrier['initial_signs'])
    current=d*current*d
    sequence=[energy(current)]
    for move in barrier['excursion']['moves']:
        current,_=dense_move(current,move)
        sequence.append(energy(current))
    assert sequence==[10,11,11,9]
    assert current==sp.Matrix(barrier['excursion']['final_matrix']) and gauge(current)[1]
    # Symbolic local surgery with arbitrary tail coefficients and arbitrary
    # entries of an upper unitriangular outside block. The general proof
    # is block algebra in D G0012, not extrapolation from this size-seven test.
    u,v,x,y,z=sp.symbols('u v x y z',integer=True)
    a=sp.Matrix([[1,-1,0,0],[0,1,-1,0],[0,0,1,1],[0,0,0,1]])
    outside=sp.Matrix([[1,x,y],[0,1,z],[0,0,1]])
    cross=sp.Matrix([[-1,0,0],[0,0,0],[0,0,0],[-1,u,v]])
    block=a.row_join(cross).col_join(sp.zeros(3,4).row_join(outside))
    initial_energy=sum(block[i,j]**2 for i in range(7) for j in range(i+1,7))
    symbolic_changes=[]
    macro_p=sp.eye(7)
    for i,inverse in [(0,False),(1,False),(2,True)]:
        block,p=dense_move(block,{'index':i,'inverse':inverse})
        macro_p=macro_p*p
        symbolic_changes.append(sp.expand(sum(block[i,j]**2 for i in range(7) for j in range(i+1,7))-initial_energy))
    assert symbolic_changes==[1,1,-1]
    assert block[:4,4:]==sp.Matrix([[0,0,0],[0,0,0],[0,u,v],[-1,0,0]])
    assert macro_p[:4,:4]==sp.Matrix([[0,0,-1,1],[1,0,-1,1],[0,1,-1,1],[0,0,1,0]])
    report={'path_inputs':66,'successful_paths':goals,'replayed_mutations':checked_moves,
            'closed_plateau_states':50,'checked_nonincreasing_transitions':transitions,
            'minimal_required_energy_increase':1,'excursion_energy_sequence':sequence,
            'symbolic_macro_energy_changes':[int(v) for v in symbolic_changes],
            'checking_relationship':'Different implementation by the authoring agent; not independent agent review.'}
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
