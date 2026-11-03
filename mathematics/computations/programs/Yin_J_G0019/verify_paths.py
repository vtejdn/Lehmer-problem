"""Check complete compact-candidate coverage and original integer digit paths."""
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def main():
    base= _J_OUTPUT
    compact=json.loads((base/'compact.json').read_text())
    data=json.loads((base/'paths.json').read_text())
    targets={tuple(a) for a in compact['states']}
    assert len(targets)==compact['candidate_count']==len(compact['states'])
    covered=set()
    max_length=0
    for row in data['witnesses']:
        a=tuple(row['state'])
        assert len(a)==4 and all(type(v) is int for v in a)
        assert a in targets and a not in covered
        covered.add(a)
        for digit in row['digits']:
            assert type(digit) is int and digit in (-1,0,1)
            # beta^4 = -1+beta+beta^2+beta^3.
            a=(-a[3]+digit,a[0]+a[3],a[1]+a[3],a[2]+a[3])
        assert a==(0,0,0,0)
        max_length=max(max_length,len(row['digits']))
    missing=targets-covered
    out={'verified_paths':len(covered),'candidate_count':len(targets),
         'complete_candidate_coverage':not missing,
         'uncovered':sorted(missing),'max_verified_length':max_length,
         'scope':'integer path validity and coverage of saved exact enumeration output'}
    (base/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    assert not missing


if __name__=='__main__':main()
