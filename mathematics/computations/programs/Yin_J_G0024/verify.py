"""Exact normalized many-vertex certificate, using frozen J22 interval primitives."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
import importlib.util,json,platform

base=(_J_PROGRAM / 'verify.py').parent
repository=next(parent for parent in base.resolve().parents if (parent/'repository/config.json').is_file())
spec=importlib.util.spec_from_file_location('j22_intervals',repository/'mathematics/computations/programs/Yin_J_G0022/verify.py')
iv=importlib.util.module_from_spec(spec);spec.loader.exec_module(iv)


def main(output_path=None):
    data=json.loads((_J_PROGRAM/'inputs/pilot.json').read_text())
    assert data['grid']==100 and [r['cell'] for r in data['cells']]==[[50,75],[75,100]]
    iv.check_trace_identity_and_irreducibility()
    beta,zs,_=iv.roots()
    sqrt8=iv.sqrt_interval(iv.point(8))
    R=8;cell_results=[];total_words=0;distinct=set()
    for row in data['cells']:
        cell=tuple(F(v,100) for v in row['cell'])
        target=F(row['target_numerator'],row['target_denominator'])
        assert target>0
        certs=row['certificates']
        assert sorted((r['coordinate'],r['sign']) for r in certs)==[(i,s) for i in range(8) for s in (-1,1)]
        minimum_norm2=None;minimum_weight=None
        for cert in certs:
            assert len(cert['digits'])==9
            vertices=[]
            for word in cert['digits']:
                x,c=iv.block(word,cell,beta,zs)
                assert -1<x[0] and x[1]<1
                norm2=iv.sum_intervals(iv.square(v) for v in c)
                assert norm2[0]>0
                minimum_norm2=norm2[0] if minimum_norm2 is None else min(minimum_norm2,norm2[0])
                vertices.append([iv.div(v,norm2) for v in c])
                total_words+=1;distinct.add(tuple(word))
            A=[[vertices[j][i] for j in range(9)] for i in range(8)]+[[iv.point(1)]*9]
            inverse=iv.inverse(A)
            rhs=[iv.point(0) for _ in range(8)]+[iv.point(1)]
            rhs[cert['coordinate']]=iv.point(cert['sign']*target)
            weights=[iv.sum_intervals(iv.mul(a,b) for a,b in zip(r,rhs)) for r in inverse]
            assert all(w[0]>0 for w in weights)
            minimum_weight=min(w[0] for w in weights) if minimum_weight is None else min(minimum_weight,*[w[0] for w in weights])
        radius=target/sqrt8[1]
        factor=2*R*radius-1
        assert factor>0
        drop=minimum_norm2*factor
        rowout={'cell':row['cell'],'crosspolytope_axis_radius':str(target),
                'norm_squared_min_lower':str(F(iv.floor(minimum_norm2*1000),1000)),
                'barycentric_weight_min_lower':str(F(iv.floor(minimum_weight*10**9),10**9)),
                'squared_descent_drop_lower':str(F(iv.floor(drop*1000),1000))}
        cell_results.append(rowout)
    uniform=min(F(r['squared_descent_drop_lower']) for r in cell_results)
    assert uniform>0
    out={'arithmetic': 'outward Fraction intervals from frozen J22', 'joint_real_dimension': 8, 'verified_cells': 2, 'verified_axis_targets': 32, 'verified_word_uses': total_words, 'distinct_words': len(distinct), 'max_block_length': max((len(w) for w in distinct)), 'neutral_euclidean_threshold': R, 'uniform_squared_norm_drop_lower': str(uniform), 'cells': cell_results, 'all_joint_target_and_whole_cell_checks_passed': True, 'scope': 'normalized many-vertex joint descent; no compact enumeration or termination asserted'}
    (Path(output_path) if output_path is not None else _J_OUTPUT / 'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
