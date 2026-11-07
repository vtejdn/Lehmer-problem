"""Exact parent-edge, acyclicity, compact coverage and exclusion verification.

No discovery helper, floating-point embedding, or C# path code is imported.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from array import array
import struct,json,gzip
import estimate as e

iv=e.iv;BASE=(_J_PROGRAM / 'verify_paths.py').parent
POLY=[1,1,0,-1,-1,-1,-1,-1,0,1,1]


def repack(key):
    out=0
    for i in range(10):out|=(((key>>(4*i))&15)+8)<<(5*i)
    return out


def verify_path_records(original, raw_parts, expected_nodes, expected_depth, saved,
                        expected_remaining):
    """Check exact edges, parent order and set coverage from supplied records."""
    targets={repack(key) for key in original};assert len(targets)==len(original)
    remaining=set(targets);seen=set();keys=array('Q');depth=array('I');maxdepth=0
    zero=sum(16<<(5*i) for i in range(10))
    for raw in raw_parts:
        assert len(raw)%13==0
        for key,parent,digit_code in struct.iter_unpack('<QIB',raw):
            index=len(keys)
            assert key<1<<50 and key not in seen and digit_code in (0,1,2)
            if index==0:
                assert key==zero and parent==0 and digit_code==1
                level=0
            else:
                assert parent<index
                a=[((key>>(5*i))&31)-16 for i in range(10)]
                lead=a[-1];digit=digit_code-1
                forward=[digit-lead]+[a[i-1]-lead*POLY[i] for i in range(1,10)]
                expected=[((keys[parent]>>(5*i))&31)-16 for i in range(10)]
                assert forward==expected
                level=depth[parent]+1
            keys.append(key);depth.append(level);seen.add(key);remaining.discard(key)
            maxdepth=max(maxdepth,level)
    assert len(keys)==expected_nodes and maxdepth==expected_depth
    assert len(set(saved))==len(saved)
    assert remaining==set(saved) and len(remaining)==expected_remaining
    return targets, remaining, keys, maxdepth


def main():
    inputs=_J_PROGRAM/'inputs'
    data=json.loads((inputs/'path-certificate.json').read_text())
    original=array('Q');original.frombytes(gzip.decompress((inputs/'compact-states.bin.gz').read_bytes()))
    assert len(original)==797507
    saved=array('Q');saved.frombytes((inputs/'uncovered.bin').read_bytes())
    raw_parts=[gzip.decompress((inputs/'path-nodes.bin.gz').read_bytes())]
    targets,remaining,keys,maxdepth=verify_path_records(
        original,raw_parts,data['retained_path_nodes'],data['max_retained_path_length'],saved,70)
    beta,M=e.embeddings();S=iv.div(beta,iv.sub(beta,iv.point(1)))
    exclusions={}
    for key in sorted(remaining):
        a=[((key>>(5*i))&31)-16 for i in range(10)]
        values=[iv.sum_intervals(iv.mul(iv.point(v),m) for v,m in zip(a,row)) for row in M]
        rho2=iv.sum_intervals(iv.square(v) for v in values[2:])
        if values[0][0]>1 or values[0][1]<-1:reason='expanding'
        elif values[1][0]>S[1] or values[1][1]<-S[1]:reason='contracting'
        elif rho2[0]>=64:reason='neutral_strict_boundary'
        else:raise AssertionError(('uncovered K8 candidate',a))
        exclusions[reason]=exclusions.get(reason,0)+1
    result={'integer_edges_and_acyclic_parents_verified':True,
            'retained_path_nodes':len(keys),'covered_initial_candidates':len(targets)-len(remaining),
            'initial_complete_superset_count':len(targets),'exactly_excluded_uncovered_candidates':len(remaining),
            'exclusion_reasons':exclusions,'max_verified_path_length':maxdepth,
            'every_actual_K8_state_has_a_verified_path':True,
            'arithmetic':'standard-library integer recurrence and Fraction embedding exclusions',
            'scope':'complete compact termination conditional only on separately verified enumeration completeness'}
    ((_J_OUTPUT / 'path-verification.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
