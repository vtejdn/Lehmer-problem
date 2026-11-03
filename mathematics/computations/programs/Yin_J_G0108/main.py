"""Exact three-entry coefficient slice and complete prime-three test."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
from fractions import Fraction
import itertools,json,math,os,subprocess,sys,time,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=REPO/'mathematics/computations/outputs'/HERE.name/'author'
CAP_SECONDS=30
CAP_MEMORY=256*1024*1024
CAP_OUTPUT=32*1024*1024
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


def costs(u):
    n=len(u);a=[[1 if i==j else -abs(u[i][j]) for j in range(n)] for i in range(n)]
    w=[[0]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(i,n):
            for s in range(2):
                if i==j:w[2*i+s][2*j+s]=1
                elif u[i][j]:w[2*i+s][2*j+(s if u[i][j]<0 else 1-s)]=-abs(u[i][j])
    pu,pa,pw=pencil(u),pencil(a),pencil(w);assert pw==mul(pu,pa)
    return {'original_matrix':u,'absolute_matrix':a,'cover_matrix':w,'original_polynomial':pu,
            'absolute_polynomial':pa,'cover_polynomial':pw,
            'energy':sum(u[i][j]**2 for i in range(n) for j in range(i+1,n))}

def worker():
    if sys.stdin.readline().strip()!='JOB_READY':raise RuntimeError('guard required')
    start=time.monotonic()
    def check():
        if time.monotonic()-start>CAP_SECONDS-1:raise TimeoutError('aggregate deadline')
    inp=json.loads((HERE/'inputs.json').read_text())
    assert inp['grid_values']==[0,1,2] and inp['prime']==3
    assert inp['variable_positions']==[[0,2],[3,4],[4,6]]
    assert inp['target_polynomial']==mul([1,1],mul([1,-1,1],[1,-1,-1,-1,1]))
    assert inp['caps']=={'seconds':CAP_SECONDS,'worker_memory_bytes':CAP_MEMORY,'output_bytes':CAP_OUTPUT}
    lagrange=[[Fraction(1),Fraction(-3,2),Fraction(1,2)],
              [Fraction(0),Fraction(2),Fraction(-1)],
              [Fraction(0),Fraction(-1,2),Fraction(1,2)]]
    polys=[{} for _ in range(3)];rows=[];exact=[]
    for point in itertools.product(inp['grid_values'],repeat=3):
        check();u=[r[:] for r in inp['base_matrix']]
        for (i,j),value in zip(inp['variable_positions'],point):u[i][j]=value
        full=pencil(u);assert full==full[::-1] and full[0]==full[-1]==1
        rows.append({'point':list(point),'integer_polynomial':full,
                     'target_residual_mod3':[(full[i]-inp['target_polynomial'][i])%3 for i in (1,2,3)]})
        if full==inp['target_polynomial']:exact.append(costs(u))
        for power in itertools.product(range(3),repeat=3):
            scale=lagrange[point[0]][power[0]]*lagrange[point[1]][power[1]]*lagrange[point[2]][power[2]]
            for j in range(3):polys[j][power]=polys[j].get(power,Fraction(0))+full[j+1]*scale
    for poly in polys:assert all(c.denominator==1 for c in poly.values())
    coeffs=[{p:int(c) for p,c in poly.items() if c} for poly in polys]
    def evaluate(poly,point):return sum(c*point[0]**p[0]*point[1]**p[1]*point[2]**p[2] for p,c in poly.items())
    solutions=[]
    for row in rows:
        point=row['point'];assert [evaluate(poly,point) for poly in coeffs]==row['integer_polynomial'][1:4]
        if row['target_residual_mod3']==[0,0,0]:
            jac=[]
            for poly in coeffs:
                jac.append([sum(c*p[j]*point[j]**(p[j]-1)*point[(j+1)%3]**p[(j+1)%3]*
                                point[(j+2)%3]**p[(j+2)%3] for p,c in poly.items() if p[j])%3 for j in range(3)])
            solutions.append({'point':point,'jacobian_mod3':jac,'determinant_mod3':bareiss(jac)%3,
                              'integer_polynomial':row['integer_polynomial']})
    check()
    result={'status':'complete','scope':inp,'coefficient_order':['a','b','c'],
            'coefficient_polynomials':[[list(p)+[c] for p,c in sorted(poly.items())] for poly in coeffs],
            'grid_rows':rows,'prime3_solutions':solutions,'integer_target_witnesses_in_cube':exact,
            'all_parameter_degree_bound':[2,2,2],
            'methods':['integer Bareiss node determinants','rational forward-difference pencil interpolation',
                       'tensor Lagrange coefficient interpolation','complete27-point prime3 residuals']}
    payload=(json.dumps(result,indent=2)+chr(10)).encode();assert len(payload)<CAP_OUTPUT-65536
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'result.pending').write_bytes(payload);(OUT/'result.pending').replace(OUT/'result.json')
    print(json.dumps({'status':'complete','prime3_solutions':len(solutions),
                      'nonsingular_prime3_solutions':sum(r['determinant_mod3']!=0 for r in solutions),
                      'exact_integer_cube_targets':len(exact)}))
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
