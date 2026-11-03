"""Independent finite exact checks plus non-destructive author reruns.

General determinant coefficients use a sparse permutation expansion, not
the author's inverse/characteristic polynomial or point interpolation.
Path couplings are checked as exact coefficient matrices. No author
function is imported for the independently implemented checks.
"""

from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, permutations, product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import io
import json

import sympy as sp

HERE = (_J_PROGRAM / 'review.py').parent
AUTHOR = (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0025')


def det_polynomial(v):
    """Return ascending coefficients of det(tV+V^T) by exact permutations."""
    n = v.rows
    out = [0]*(n+1)

    def recurse(row,used,inversions,poly):
        if row == n:
            sign = -1 if inversions%2 else 1
            for j,c in enumerate(poly):out[j] += sign*c
            return
        for col in range(n):
            if col in used:continue
            constant,slope = int(v[col,row]),int(v[row,col])
            if not (constant or slope):continue
            new = [0]*(len(poly)+1)
            for j,c in enumerate(poly):
                new[j] += c*constant
                new[j+1] += c*slope
            recurse(row+1,used+(col,),inversions+sum(j>col for j in used),new)
    recurse(0,(),0,[1])
    return out


def energy(v):
    return sum(v[i,j]**2 for i in range(v.rows) for j in range(i+1,v.rows))


def basis_move(v,i,inverse=False):
    basis = [sp.eye(v.rows)[:,j] for j in range(v.rows)]
    x,y,a = basis[i],basis[i+1],v[i,i+1]
    basis[i:i+2] = [y-a*x,x] if inverse else [y,x-a*y]
    change = sp.Matrix.hstack(*basis)
    result = change.T*v*change
    assert result.is_upper and all(result[j,j] == 1 for j in range(v.rows))
    return result,change


def ordered_cycles():
    counts = {}
    for n in range(3,8):
        count = 0
        for tail in permutations(range(1,n)):
            order = (0,)+tail
            if order[1]>order[-1]:continue
            k = sum(order[j]<order[(j+1)%n] for j in range(n))
            for frustrated in (False,True):
                v = sp.eye(n)
                for j in range(n):
                    a,b = sorted((order[j],order[(j+1)%n]))
                    v[a,b] = 1 if frustrated and j == 0 else -1
                expected = [0]*(n+1)
                expected[0] = expected[n] = 1
                sign = 1 if frustrated else -1
                expected[k] += sign
                expected[n-k] += sign
                assert det_polynomial(v) == expected
            count += 1
        counts[n] = count
    return counts


def low_rank():
    count,matches = 0,0
    det_one_values = set()
    for size in range(4):
        for positions in combinations(list(combinations(range(4),2)),size):
            for signs in product((-1,1),repeat=size):
                v = sp.eye(4)
                for (i,j),s in zip(positions,signs):v[i,j] = s
                coefficients = det_polynomial(v)
                matches += coefficients == [1,0,2,0,1]
                det_one_values.add(sum(coefficients))
                count += 1
    assert count == 233 and matches == 0
    assert det_one_values == {0,4,5,8,9,12,16}
    return {"inputs":count,"target_matches":matches,"det_at_one_values":sorted(det_one_values)}


def path_basis_checks():
    count = 0
    for m in range(3,17):
        initial = sp.eye(m)
        for i in range(m-1):initial[i,i+1] = 1 if i == m-2 else -1
        unit = [sp.eye(m)[:,j] for j in range(m)]
        current,accumulated = initial,sp.eye(m)
        for j in range(1,m-1):
            current,change = basis_move(current,j-1)
            accumulated = accumulated*change
            h = sum(unit[:j+1],sp.zeros(m,1))
            direct = sp.Matrix.hstack(*(unit[1:j+1]+[h]+unit[j+1:]))
            assert accumulated == direct
            assert energy(current) == m
            assert direct*direct.T-sp.eye(m) == h*h.T-unit[0]*unit[0].T
            count += 1
        current,change = basis_move(current,m-2,True)
        accumulated = accumulated*change
        h = sum(unit[:-1],sp.zeros(m,1))
        direct = sp.Matrix.hstack(*(unit[1:-1]+[unit[-1]-h,h]))
        assert accumulated == direct and abs(direct.det()) == 1
        assert energy(current) == m-1
        coefficient = 2*h*h.T-unit[-1]*h.T-h*unit[-1].T-unit[0]*unit[0].T
        assert direct*direct.T-sp.eye(m) == coefficient
        count += 1
    return {"sizes":list(range(3,17)),"prefix_and_final_checks":count,
            "coupling_method":"exact T T^T-I coefficient matrix for arbitrary outside coordinates"}


def all_small_triangle_free():
    graphs,steps,zero = 0,0,0
    locations = list(combinations(range(4),2))
    for values in product((-1,0,1),repeat=6):
        v = sp.eye(4)
        for (i,j),a in zip(locations,values):v[i,j] = a
        if any(v[i,j] and v[j,k] and v[i,k] for i,j,k in combinations(range(4),3)):
            continue
        graphs += 1
        degree = [sum(v[min(i,j),max(i,j)] != 0 for j in range(4) if j != i) for i in range(4)]
        for i in range(3):
            for inverse in (False,True):
                w,_ = basis_move(v,i,inverse)
                a = v[i,i+1]
                expected = degree[i if inverse else i+1]-1 if a else 0
                assert energy(w)-energy(v) == expected and expected>=0
                if expected == 0:
                    swap = sp.eye(4)
                    swap.col_swap(i,i+1)
                    gauge = sp.eye(4)
                    if a:gauge[i+1 if inverse else i,i+1 if inverse else i] = -1
                    # The claim is signed-graph equivalence, not equality of
                    # ordered bilinear forms after an arbitrary permutation.
                    assert w+w.T == gauge*swap.T*(v+v.T)*swap*gauge
                    zero += 1
                steps += 1
    return {"all_signed_triangle_free_rank4":graphs,"directed_steps":steps,
            "zero_steps_with_explicit_permutation_gauge":zero}


def rerun_author(filename,output):
    spec = spec_from_file_location("author_"+filename.removesuffix(".py"),AUTHOR/filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    capture = io.StringIO()
    with redirect_stdout(capture):
        module.main(output_path=_J_OUTPUT / output)
    recalculated = json.loads((((_J_PROGRAM if output in ('readme.md', 'review.py') else _J_OUTPUT) / output)).read_text())
    retained = json.loads((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0025' / output).read_text())
    assert recalculated == retained
    return {"source":str((AUTHOR/filename).relative_to(_J_ROOT)),
            "review_output":output,"all_json_mathematical_fields_equal":True}


def main():
    result = {'ordered_cycles': ordered_cycles(), 'rank4': low_rank(), 'paths': path_basis_checks(), 'triangle_free': all_small_triangle_free()}
    print(json.dumps(result,indent=2),flush=True)
    result["author_reruns"] = [rerun_author("controls.py","controls.json"),
                              rerun_author("verify_family.py","verification.json")]
    ((_J_OUTPUT / 'review-results.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("All independent exact controls and both non-destructive author reruns passed.",flush=True)


if __name__ == "__main__":main()
