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
    saved=json.loads(expected.read_text())
    new=captured[0]
    same=new==saved
    assert same
    summary.append({'program':str(location.relative_to(_J_REPOSITORY)),
                    'same_mathematical_result':same})
write_text(base/'author_replay.json',json.dumps(summary,indent=2)+'\n')
