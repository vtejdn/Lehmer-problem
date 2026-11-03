"""Complete exact integer Boolean rank-seven enumeration; one guarded batch."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
from fractions import Fraction
import itertools,json,math,os,subprocess,sys,time,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=REPO/'mathematics/computations/outputs'/HERE.name/'author'
CAP_SECONDS=300
CAP_MEMORY=512*1024*1024
CAP_OUTPUT=64*1024*1024
UP=[(i,j) for i in range(7) for j in range(i+1,7)]
INDEX={ij:k for k,ij in enumerate(UP)}
TARGETS={'phi2_phi6_p4':[1,-1,-1,0,0,-1,-1,1],
         'phi2_p6':[1,0,-1,-1,-1,-1,0,1]}
# Exact determinant helpers and hard launcher are copied from J107, not an independent route.
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def bareiss(a):
    a=[row[:] for row in a];n=len(a);old=1;sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        q=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*q-a[i][k]*a[k][j]
                assert value%old==0
                a[i][j]=value//old
            a[i][k]=0
        old=q
    return sign*a[-1][-1]

def pencil(a):
    n=len(a)
    values=[bareiss([[t*a[i][j]+a[j][i] for j in range(n)] for i in range(n)]) for t in range(n+1)]
    coeff=[Fraction(0)]*(n+1);basis=[Fraction(1)]
    differences=values
    for k in range(n+1):
        for i,x in enumerate(basis):coeff[i]+=differences[0]*x
        differences=[differences[i+1]-differences[i] for i in range(len(differences)-1)]
        if k<n:basis=[x/(k+1) for x in mul(basis,[-k,1])]
    assert all(x.denominator==1 for x in coeff)
    return [int(x) for x in coeff]


def matrix(mask):
    u=[[int(i==j) for j in range(7)] for i in range(7)]
    for bit,(i,j) in enumerate(UP):u[i][j]=(mask>>bit)&1
    return u

def costs(mask):
    u=matrix(mask)
    a=[[int(i==j) if i>=j else -abs(u[i][j]) for j in range(7)] for i in range(7)]
    w=[[0]*14 for _ in range(14)]
    for i in range(7):
        for j in range(i,7):
            for s in range(2):
                if i==j:w[2*i+s][2*j+s]=1
                elif u[i][j]:w[2*i+s][2*j+(s if u[i][j]<0 else 1-s)]=-abs(u[i][j])
    pu,pa,pw=pencil(u),pencil(a),pencil(w)
    assert pw==mul(pu,pa)
    def describe(v,p):
        return {'matrix':v,'polynomial':p,'rank':len(v),
                'height':max(abs(x) for r in v for x in r),
                'energy':sum(v[i][j]**2 for i in range(len(v)) for j in range(i+1,len(v)))}
    return {'mask':mask,'original':describe(u,pu),'negative_absolute':describe(a,pa),
            'literal_cover':describe(w,pw),'direct_cover_product_check':True}

def worker():
    if sys.stdin.readline().strip()!='JOB_READY':raise RuntimeError('guard required')
    started=time.monotonic()
    def check():
        if time.monotonic()-started>CAP_SECONDS-2:raise TimeoutError('aggregate deadline')
    print(json.dumps({'stage':'worker_started'}),flush=True)
    import numpy as np
    print(json.dumps({'stage':'numpy_imported'}),flush=True)
    inp=json.loads((HERE/'inputs.json').read_text())
    assert inp['rank']==7 and inp['strict_upper_values']==[0,1]
    assert inp['upper_positions']==[list(p) for p in UP]
    assert inp['target_polynomials']==TARGETS
    assert inp['caps']=={'seconds':CAP_SECONDS,'worker_memory_bytes':CAP_MEMORY,'output_bytes':CAP_OUTPUT}
    assert mul([1,1],mul([1,-1,1],[1,-1,-1,-1,1]))==TARGETS['phi2_phi6_p4']
    assert mul([1,1],[1,-1,0,-1,0,-1,1])==TARGETS['phi2_p6']
    sparse={}
    for perm in itertools.permutations(range(7)):
        check()
        sign=(-1)**sum(perm[i]>perm[j] for i in range(7) for j in range(i+1,7))
        support=0;fixed=0;asc=0
        for i,j in enumerate(perm):
            if i==j:fixed+=1
            else:
                support|=1<<INDEX[min(i,j),max(i,j)]
                asc+=int(i<j)
        row=sparse.setdefault(support,[0]*8)
        for power in range(fixed+1):row[asc+power]+=sign*math.comb(fixed,power)
    sparse={s:v for s,v in sparse.items() if any(v)}
    for support,row in sparse.items():
        assert row==row[::-1]
        assert row[0]==row[7]==int(support==0)
        assert max(abs(x) for x in row)<=176400
    table=np.zeros((1<<21,3),dtype=np.int32)
    for support,row in sparse.items():table[support]=row[1:4]
    stage_extrema=[]
    for bit in range(21):
        check();step=1<<bit;view=table.reshape(-1,2*step,3)
        np.add(view[:,step:,:],view[:,:step,:],out=view[:,step:,:])
        mn,mx=int(table.min()),int(table.max())
        assert -176400<=mn<=mx<=176400
        stage_extrema.append([bit,mn,mx])
    print(json.dumps({'stage':'full_integer_table_complete','masks':1<<21}),flush=True)
    def full(mask):
        a,b,c=map(int,table[mask]);return [1,a,b,c,c,b,a,1]
    controls=[]
    for mask in [0,(1<<21)-1,7092,2323]:
        direct=pencil(matrix(mask));assert direct==full(mask)
        controls.append({'mask':mask,'integer_polynomial':direct})
    matches={};outcomes={}
    for name,target in TARGETS.items():
        check()
        ids=np.flatnonzero(np.all(table==np.array(target[1:4],dtype=np.int32),axis=1)).astype(np.uint32)
        matches[name]=ids
        histogram=[0]*22;best=None;best_e=22
        for raw in ids:
            mask=int(raw);e=mask.bit_count();histogram[e]+=1
            if e<best_e:best=mask;best_e=e
        witness=costs(best) if best is not None else None
        if witness:
            assert witness['original']['polynomial']==target==full(best)
            assert witness['original']['energy']==best_e
            assert witness['negative_absolute']['energy']==best_e
            assert witness['literal_cover']['energy']==2*best_e
        outcomes[name]={'target':target,'match_count':int(len(ids)),
                        'all_matching_masks_file':f'matches_{name}.npy',
                        'energy_histogram':histogram,'minimum_energy':None if best is None else best_e,
                        'selected_minimum_energy_mask':best,'witness':witness}
    result={'status':'complete','scope':inp,'all_binary_matrices_evaluated':1<<21,
            'permutations_evaluated':math.factorial(7),'sparse_nonzero_supports':len(sparse),
            'coefficient_table_file':'coefficients.npy','coefficient_columns':[1,2,3],
            'full_coefficient_pattern':[1,'a','b','c','c','b','a',1],
            'integer_intermediate_bound':176400,'stage_extrema':stage_extrema,
            'direct_integer_controls':controls,'targets':outcomes,
            'arithmetic':'exact integers; no modular reduction; int32 zeta with proved overflow bound',
            'numpy_version':np.__version__,'worker_seconds_before_serialization':time.monotonic()-started}
    formal={'mask_order':'same row-major21-bit order as inputs','coefficient_order':'ascending t0..t7',
            'rows':[[s]+v for s,v in sorted(sparse.items())]}
    formal_bytes=(json.dumps(formal,indent=2)+'\n').encode()
    result_bytes=(json.dumps(result,indent=2)+'\n').encode()
    planned=table.nbytes+sum(a.nbytes for a in matches.values())+len(formal_bytes)+len(result_bytes)+4096
    assert planned<CAP_OUTPUT-65536
    OUT.mkdir(parents=True,exist_ok=True)
    np.save(OUT/'coefficients.npy',table,allow_pickle=False)
    for name,ids in matches.items():np.save(OUT/f'matches_{name}.npy',ids,allow_pickle=False)
    (OUT/'sparse_coefficients.json').write_bytes(formal_bytes)
    check()
    used=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    assert used+len(result_bytes)<CAP_OUTPUT-65536
    (OUT/'result.pending').write_bytes(result_bytes)
    (OUT/'result.pending').replace(OUT/'result.json')
    print(json.dumps({'status':'complete','matches':{k:v['match_count'] for k,v in outcomes.items()}}),flush=True)
    return 0

def make_job():
    """Hard worker commit/job-memory and working-set limits; fail closed."""
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    class Basic(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_longlong), ("job_time", ctypes.c_longlong),
                    ("flags", wintypes.DWORD), ("min_ws", ctypes.c_size_t), ("max_ws", ctypes.c_size_t),
                    ("active", wintypes.DWORD), ("affinity", ctypes.c_size_t),
                    ("priority", wintypes.DWORD), ("scheduling", wintypes.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_ulonglong) for name in
                    ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]
    class Extended(ctypes.Structure):
        _fields_ = [("basic", Basic), ("io", IO), ("process_memory", ctypes.c_size_t),
                    ("job_memory", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                    ("peak_job", ctypes.c_size_t)]
    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p, wintypes.LPCWSTR)
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD)
    kernel.AssignProcessToJobObject.argtypes = (wintypes.HANDLE, wintypes.HANDLE)
    kernel.SetProcessWorkingSetSizeEx.argtypes = (wintypes.HANDLE, ctypes.c_size_t,
                                                  ctypes.c_size_t, wintypes.DWORD)
    kernel.GetProcessWorkingSetSizeEx.argtypes = (wintypes.HANDLE, ctypes.c_void_p,
                                                  ctypes.c_void_p, ctypes.c_void_p)
    kernel.TerminateJobObject.argtypes = (wintypes.HANDLE, wintypes.UINT)
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    kernel.QueryInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                                 wintypes.DWORD, ctypes.c_void_p)
    handle = kernel.CreateJobObjectW(None, None)
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = Extended()
    limits.basic.flags = 0x100 | 0x200 | 0x2000
    limits.basic.min_ws, limits.basic.max_ws = 1024 * 1024, CAP_MEMORY
    limits.process_memory = limits.job_memory = CAP_MEMORY
    if not kernel.SetInformationJobObject(handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        kernel.CloseHandle(handle)
        raise ctypes.WinError(ctypes.get_last_error())
    return kernel, handle, limits


def launch():
    if os.name != "nt":
        raise RuntimeError("the declared hard-memory launcher requires Windows")
    if OUT.exists() and any(OUT.iterdir()):
        raise RuntimeError("author output already exists; do not overwrite a prior run implicitly")
    kernel, job, limits = make_job()
    start = time.monotonic()
    process = None
    try:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, creationflags=subprocess.CREATE_NO_WINDOW,
                                   env={**os.environ,"OPENBLAS_NUM_THREADS":"1","OMP_NUM_THREADS":"1",
                                        "MKL_NUM_THREADS":"1","NUMEXPR_NUM_THREADS":"1"})
        if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(process._handle)):
            process.kill()
            raise ctypes.WinError(ctypes.get_last_error())
        child_handle = wintypes.HANDLE(process._handle)
        if not kernel.SetProcessWorkingSetSizeEx(child_handle, 1024 * 1024, CAP_MEMORY, 0x2 | 0x4):
            raise ctypes.WinError(ctypes.get_last_error())
        minimum, maximum, flags = ctypes.c_size_t(), ctypes.c_size_t(), wintypes.DWORD()
        if not kernel.GetProcessWorkingSetSizeEx(child_handle, ctypes.byref(minimum),
                                                ctypes.byref(maximum), ctypes.byref(flags)):
            raise ctypes.WinError(ctypes.get_last_error())
        if maximum.value > CAP_MEMORY or not flags.value & 0x4:
            raise RuntimeError("worker hard working-set limit was not confirmed")
        try:
            stdout, stderr = process.communicate("JOB_READY\n", timeout=max(0.001, CAP_SECONDS - (time.monotonic() - start)))
            status = "complete" if process.returncode == 0 else "failed_or_stopped"
        except subprocess.TimeoutExpired:
            kernel.TerminateJobObject(job, 3)
            stdout, stderr = process.communicate(timeout=5)
            status = "wall_time_stop"
        queried = bool(kernel.QueryInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits), None))
        result = {"status": status, "returncode": process.returncode,
                  "wall_seconds": time.monotonic() - start,
                  "worker_job_memory_cap_bytes": CAP_MEMORY, "worker_working_set_cap_bytes": CAP_MEMORY,
                  "peak_worker_commit_bytes": limits.peak_process if queried else None,
                  "peak_job_commit_bytes": limits.peak_job if queried else None,
                  "author_stdout": stdout, "author_stderr": stderr,
                  "completed_result_files": sorted(p.name for p in OUT.glob("result.json")),
                  "parent_monitor_excluded_from_worker_memory_limit": True}
        OUT.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(result, indent=2) + "\n").encode("utf-8")
        used = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        if used + len(payload) > CAP_OUTPUT:
            raise RuntimeError("reserved execution-status output would exceed cap")
        (OUT / "execution.json").write_bytes(payload)
        print(json.dumps(result, indent=2))
        return 0 if status == "complete" else 2
    finally:
        if process is not None and process.poll() is None:
            kernel.TerminateJobObject(job, 4)
            process.wait(timeout=5)
        kernel.CloseHandle(job)


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--worker"]:
            raise SystemExit(worker())
        if sys.argv[1:]:
            raise RuntimeError("no scope-changing command-line parameters are permitted")
        raise SystemExit(launch())
    except Exception:
        traceback.print_exc()
        raise SystemExit(1)
