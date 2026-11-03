"""Exact proper rank-seven coefficient test; guarded first execution."""
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

def matrix(mask,correction=0):
    u=[[int(i==j) for j in range(7)] for i in range(7)]
    for k,(i,j) in enumerate(UP):u[i][j]=((mask>>k)&1)+2*((correction>>k)&1)
    return u

def full_witness(mask,correction,columns,rhs):
    u=matrix(mask,correction)
    minus=[[1 if i==j else -abs(u[i][j]) for j in range(7)] for i in range(7)]
    cover=[[0]*14 for _ in range(14)]
    for i in range(7):
        for j in range(i,7):
            value=u[i][j]
            for s in range(2):
                if i==j:cover[2*i+s][2*j+s]=1
                elif value:
                    cover[2*i+s][2*j+(s if value<0 else 1-s)]=-abs(value)
    pu,pa,pc=pencil(u),pencil(minus),pencil(cover)
    assert pc==mul(pu,pa)
    return {'binary_mask':mask,'correction_mask':correction,'derivative_columns':columns,'right_side':rhs,
            'matrix':u,'absolute_matrix':minus,'cover_matrix':cover,
            'integer_polynomial':pu,'absolute_polynomial':pa,'cover_polynomial':pc,
            'energy':sum(u[i][j]**2 for i,j in UP),'height':max(abs(v) for row in u for v in row)}

def worker():
    if sys.stdin.readline().strip()!='JOB_READY':raise RuntimeError('guard required')
    started=time.monotonic()
    def check():
        if time.monotonic()-started>CAP_SECONDS-2:raise TimeoutError('aggregate deadline')
    print(json.dumps({"stage":"worker_started"}),flush=True)
    import numpy as np
    print(json.dumps({"stage":"numpy_imported"}),flush=True)
    # The full products fix every coefficient before the coefficient test.
    assert mul([1,1],mul([1,-1,1],[1,-1,-1,-1,1]))==TARGETS['phi2_phi6_p4']
    assert mul([1,1],[1,-1,0,-1,0,-1,1])==TARGETS['phi2_p6']
    table=np.zeros((1<<21,3),dtype=np.uint8)
    derivative=[{} for _ in UP]
    for perm in itertools.permutations(range(7)):
        check();sign=(-1)**sum(perm[i]>perm[j] for i in range(7) for j in range(i+1,7))
        counts=[0]*21;fixed=0;asc=0
        for i,j in enumerate(perm):
            if i==j:fixed+=1
            else:counts[INDEX[min(i,j),max(i,j)]]+=1;asc+=int(i<j)
        support=sum((count>0)<<j for j,count in enumerate(counts))
        vals=[sign*math.comb(fixed,k-asc) if 0<=k-asc<=fixed else 0 for k in (1,2,3)]
        table[support]=[(int(table[support,k])+vals[k])%4 for k in range(3)]
        bits=sum((v%2)<<k for k,v in enumerate(vals))
        if bits:
            for j,count in enumerate(counts):
                if count%2:
                    assert count==1
                    s=support^(1<<j);derivative[j][s]=derivative[j].get(s,0)^bits
    for j in range(21):
        check();step=1<<j;view=table.reshape(-1,2*step,3)
        np.add(view[:,step:,:],view[:,:step,:],out=view[:,step:,:])
    table &=3
    residue_hist=np.bincount(table[:,0].astype(np.int16)+4*table[:,1]+16*table[:,2],minlength=64).tolist()
    result={'status':'partial','binary_bases':1<<21,'permutations':math.factorial(7),
            'target_polynomials':TARGETS,'coefficient_residue_histogram':residue_hist,
            'derivative_monomials':[sum(bool(v) for v in d.values()) for d in derivative], 'targets':{}}
    # Compute EVERY derivative map by packed F2 subset transforms.
    # This is the same formal derivative polynomial, with vectorized evaluation.
    all_columns=np.zeros((1<<21,21),dtype=np.uint8)
    images=np.ones(1<<21,dtype=np.uint8)
    translate=np.zeros((256,8),dtype=np.uint8)
    for value in range(256):
        for c in range(8):
            translate[value,c]=sum(((value>>v)&1)<<(v^c) for v in range(8))
    for j,d in enumerate(derivative):
        check();values=np.zeros(1<<21,dtype=np.uint8)
        for mask,c in d.items():values[mask]=c
        for k in range(21):
            step=1<<k;view=values.reshape(-1,2*step)
            np.bitwise_xor(view[:,step:],view[:,:step],out=view[:,step:])
        all_columns[:,j]=values
        images |= translate[images,values]
    print(json.dumps({'stage':'all_coefficient_and_derivative_maps_complete','binary_bases':1<<21}),flush=True)
    for name,target in TARGETS.items():
        trip=target[1:4];par=np.array([v%2 for v in trip],dtype=np.uint8)
        matches=np.flatnonzero(np.all((table&1)==par,axis=1))
        rhs_values=np.zeros(len(matches),dtype=np.uint8)
        for k in range(3):
            rhs_values |= (((trip[k]-table[matches,k].astype(np.int16))//2)&1).astype(np.uint8)<<k
        feasible=np.flatnonzero((images[matches]>>rhs_values)&1)
        witness=None
        if len(feasible):
            mask=int(matches[int(feasible[0])]);cols=[int(v) for v in all_columns[mask]]
            image={0:0}
            for j,c in enumerate(cols):
                for v,solution in tuple(image.items()):image.setdefault(v^c,solution^(1<<j))
            rhs=int(rhs_values[int(feasible[0])]);base=[int(v) for v in table[mask]]
            witness=full_witness(mask,image[rhs],cols,rhs)
            witness['base_coefficient_residues']=base
            witness['derivative_image']=sorted(image)
            assert sum(1<<v for v in image)==int(images[mask])
            assert [v%4 for v in witness['integer_polynomial']]==[v%4 for v in target]
        result['targets'][name]={'target_parity_bases':int(len(matches)),
                                 'derivative_bases_checked':int(len(matches)),
                                 'compatible_binary_bases':int(len(feasible)),
                                 'modular_status':'compatible' if witness else 'exhausted_no_solution',
                                 'witness':witness}
    result['all_binary_derivative_maps_evaluated']=1<<21
    OUT.mkdir(parents=True,exist_ok=True)
    # The entire finite payload is below the declared64MiB even uncompressed.
    np.savez(OUT/'tables.npz',coefficient_residues=table,derivative_columns=all_columns,image_bits=images)
    assert sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())<CAP_OUTPUT-65536
    check();result['status']='complete';result['arithmetic']='integer determinants and exact modulo-four/Boolean arithmetic'
    OUT.mkdir(parents=True,exist_ok=True)
    payload=(json.dumps(result,indent=2)+'\n').encode()
    assert sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+len(payload)<CAP_OUTPUT-65536
    (OUT/'result.pending').write_bytes(payload)
    (OUT/'result.pending').replace(OUT/'result.json')
    print(json.dumps({'status':'complete','targets':{k:v['modular_status'] for k,v in result['targets'].items()}}))
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
