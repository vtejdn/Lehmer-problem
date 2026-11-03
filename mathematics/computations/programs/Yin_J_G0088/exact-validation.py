"""New bounded AUTHOR validation; never executes/imports the Phase A worker."""
from fractions import Fraction as F
from itertools import product
from math import lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse
import json
import subprocess
import sys
import time
import traceback

HERE=(_J_PROGRAM / 'exact-validation.py').parent
CAP=180
P=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
D,N,Q=10,11,9

# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def solve(rows,rhs):
    m=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,rhs)]
    for j in range(N):
        i=next(i for i in range(j,N) if m[i][j])
        m[j],m[i]=m[i],m[j]
        v=m[j][j];m[j]=[x/v for x in m[j]]
        for i in range(N):
            if i!=j and m[i][j]:
                v=m[i][j];m[i]=[x-v*y for x,y in zip(m[i],m[j])]
    return [r[-1] for r in m]

def run_worker(result_path):
    start=time.monotonic()
    out={'status': 'started', 'coefficients': P, 'd': D, 'allowed_T': D, 'method': 'Exact unchanged-family regeneration and final-basis transpose dual; AUTHOR validation, no LP rerun.'}
    def cap():
        if time.monotonic()-start>=CAP:raise TimeoutError('Exact-phase180-second cap')
    def save(name):
        pass
        pending=_J_OUTPUT/(name+'.pending')
        pending.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
        pending.replace(((_J_PROGRAM if name in ('exact-validation.py', 'main.py', 'readme.md', 'review-check.py', 'worker.py') else _J_OUTPUT) / name))
    try:
        original=json.loads(result_path.read_text(encoding='utf8'))
        assert original['status']=='complete' and original['coefficients']==P
        assert original['allowed_T']==D and original['distinct_atoms']==13197
        assert original['generated_labels']==147631
        assert original['parameters']['k']==[-2,-1,0,1,2]
        assert original['parameters']['coefficient_denominator_divides']==Q
        assert original['parameters']['atom_energy_cap']==4
        assert original['initial_basis']==original['floating_lead']['basis']
        atoms=[];labels=[];index={};generated=0
        def add(v,label):
            f=tuple(v)
            if next(x for x in f if x)<0:f=tuple(-x for x in f)
            if f not in index:
                index[f]=len(atoms);atoms.append(f);labels.append(label)
        for count,r in enumerate(product((-1,0,1),repeat=D)):
            if count%1024==0:cap()
            if not any(r) or next(x for x in r if x)!=1:continue
            dot=sum(r[j]*P[j] for j in range(D))
            for k in (-2,-1,0,1,2):
                generated+=1;c=k-dot
                f=[Q*r[j]+c*P[j] for j in range(D)]+[c]
                if sum(x*x for x in f)<=4*Q*Q:add(f,{'r':list(r),'k':k})
        true_initial=[]
        for h in range(N):
            f=[0]*N;f[0]=Q
            if h:f[h]=Q
            add(f,{'initial_basis_h':h})
            true_initial.append(index[tuple(f)])
        assert generated==147620 and len(atoms)==13197
        assert len(set(true_initial))==N
        energy=[];lag=[]
        for j,f in enumerate(atoms):
            if j%256==0:cap()
            r=[f[i]-f[-1]*P[i] for i in range(D)]
            assert all(x%Q==0 for x in r) and any(r)
            ee=sum(x*x for x in f)
            assert 0<ee<=4*Q*Q
            energy.append(ee)
            lag.append([sum(f[i]*f[i+h] for i in range(N-h)) for h in range(1,N)])
        final=original['floating_lead']['basis']
        assert len(final)==N and len(set(final))==N
        assert all(type(i)is int and 0<=i<len(atoms) for i in final)
        system=[[Q*Q]+lag[j] for j in final]
        rhs=[energy[j] for j in final]
        beta=solve(system,rhs)
        assert all(sum(F(a)*b for a,b in zip(row,beta))==e for row,e in zip(system,rhs))
        common=lcm(*(b.denominator for b in beta))
        bb=[int(b*common) for b in beta]
        out.update({'regenerated_labels':generated+N,'regenerated_atom_count':len(atoms),
            'true_initial_basis':true_initial,'true_initial_numerators':[list(atoms[j]) for j in true_initial],
            'saved_alias_affected_initial_basis':original['initial_basis'],
            'saved_final_basis':final,'transpose_system_rows':system,'transpose_rhs':rhs,
            'dual_beta':[[b.numerator,b.denominator] for b in beta],
            'dual_common_denominator':common,'dual_integer_numerators':bb,
            'slack_denominator':Q*Q*common})
        slacks=[]
        for j,(ee,hh) in enumerate(zip(energy,lag)):
            if j%256==0:cap()
            slack=common*ee-Q*Q*bb[0]-sum(a*b for a,b in zip(bb[1:],hh))
            slacks.append(slack)
            if slack<0:
                out.update({'status':'complete','outcome':'exact-final-basis-dual-failed',
                    'checked_atom_count':len(slacks),'first_negative_atom':{
                        'index':j,'generator_label':labels[j],'numerator_coefficients':list(atoms[j]),
                        'coefficient_denominator':Q,'energy_numerator':ee,
                        'lag_numerators':hh,'slack_numerator':slack},
                    'limits':'This exact dual candidate fails; no different basis/LP rerun or finite-family optimum is claimed.'})
                save('exact-validation.json')
                print(json.dumps({'outcome':out['outcome'],'checked_atoms':len(slacks),'negative_index':j}))
                return
        assert beta[0]==1
        assert atoms[true_initial[0]]==tuple([Q]+[0]*D)
        assert original['energy']==[1,1]
        out.update({'status':'complete','outcome':'exact-finite-family-minimum-one',
                    'checked_atom_count':len(slacks),'all_slack_numerators':slacks,
                    'minimum_slack_numerator':min(slacks),
                    'exact_minimum':[1,1],
                    'limits':'Only the original declared13197-atom finite family. C17/full capacity allows other rational representatives and remains unchanged.'})
        save('exact-validation.json')
        print(json.dumps({'outcome': out['outcome'], 'atoms': len(atoms), 'true_initial': true_initial, 'beta': out['dual_beta']}))
    except BaseException as error:
        out.update({'status':'failed','error_type':type(error).__name__,'error':_record_text(str(error)),
                    'traceback':_record_text(traceback.format_exc())})
        save('exact-failure.json')
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result', type=Path, default=_J_PROGRAM / 'inputs/result.json')
    parser.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        run_worker(args.result)
    else:
        try:
            result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'exact-validation.py'), '--worker', '--result', str(args.result)], timeout=CAP)
            code = result.returncode
        except subprocess.TimeoutExpired:
            (_J_OUTPUT / 'exact-failure.json').write_text(json.dumps({'status':'supervisor-timeout','complete':False})+'\n',encoding='utf-8')
            code = 124
        raise SystemExit(code)
