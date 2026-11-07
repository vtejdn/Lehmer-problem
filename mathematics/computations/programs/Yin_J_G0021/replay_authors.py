"""Rerun exact author checkers while retaining outputs only in this review J."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from unittest.mock import patch
import json
import runpy


base= _J_OUTPUT
write_text=Path.write_text
summary=[]
for directory,script,output in (
    ('Yin_J_G0018','verify.py','verification.json'),
    ('Yin_J_G0019','enumerate.py','compact.json'),
    ('Yin_J_G0019','verify_paths.py','verification.json'),
):
    location=_J_PROGRAM.parent/directory/script
    expected=base.parent/directory/output
    captured=[]

    def retain(path,text,*args,**kwargs):
        assert path.resolve()==expected
        captured.append(json.loads(text))
        return write_text(base/(directory+'_'+output),text,*args,**kwargs)

    with patch.object(Path,'write_text',retain):
        runpy.run_path(str(location),run_name='__main__')
    assert len(captured)==1
    new=captured[0]
    if script=='enumerate.py':
        saved=json.loads((_J_PROGRAM.parent/directory/'inputs/compact.json').read_text())
        assert new==saved
    elif directory=='Yin_J_G0018':
        assert new['verified_cells']==50 and new['verified_blocks']==150
        assert new['max_block_length']==9 and new['neutral_threshold']==10
        assert new['uniform_squared_norm_drop_lower']=='557/500'
        assert new['all_strict_interval_and_triangle_checks_passed']
    else:
        assert new['verified_paths']==new['candidate_count']==259
        assert new['complete_candidate_coverage'] and not new['uncovered']
        assert new['max_verified_length']==25
    summary.append({'program':str(location.relative_to(_J_REPOSITORY)),
                    'retained_input_and_claimed_finite_scope_verified':True})
write_text(base/'author_replay.json',json.dumps(summary,indent=2)+'\n')
