"""J109 exact formal four-entry identity; two author methods, no parameter search."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
from functools import lru_cache
import itertools,json,os,subprocess,sys,time,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=REPO/'mathematics/computations/outputs'/HERE.name/'author'
CAP_SECONDS=30
CAP_MEMORY=256*1024*1024
CAP_OUTPUT=32*1024*1024
ZERO=(0,0,0,0,0)


def product(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            key=tuple(a[i]+b[i] for i in range(5))
            out[key]=out.get(key,0)+x*y
    return {k:v for k,v in out.items() if v}


def add_scaled(out,p,scale):
    for key,value in p.items():
        out[key]=out.get(key,0)+scale*value
        if not out[key]:del out[key]


def encode(p):
    return [list(k)+[v] for k,v in sorted(p.items())]


def worker():
    if sys.stdin.readline().strip()!='JOB_READY':raise RuntimeError('guard required')
    start=time.monotonic()
    def check():
        if time.monotonic()-start>CAP_SECONDS-1:raise TimeoutError('symbolic aggregate cap')
    inp=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    assert inp['variable_positions']==[[0,2],[3,4],[4,6],[3,5]]
    assert inp['variable_names']==['x','y','z','w']
    assert inp['target_polynomial']==[1,-1,-1,0,0,-1,-1,1]
    assert inp['caps']=={'seconds':CAP_SECONDS,'worker_memory_bytes':CAP_MEMORY,'output_bytes':CAP_OUTPUT}
    base=inp['base_matrix']
    assert base==[[1,0,0,1,0,1,1],[0,1,0,1,1,1,0],[0,0,1,1,1,0,0],
                  [0,0,0,1,2,2,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
    variables={tuple(pos):axis+1 for axis,pos in enumerate(inp['variable_positions'])}
    matrix=[]
    for i in range(7):
        row=[]
        for j in range(7):
            if i==j:row.append({ZERO:1,(1,0,0,0,0):1});continue
            pair=(min(i,j),max(i,j));key=[int(i<j),0,0,0,0]
            if pair in variables:key[variables[pair]]=1;row.append({tuple(key):1})
            else:
                value=base[pair[0]][pair[1]]
                row.append({tuple(key):value} if value else {})
        matrix.append(row)
    total={};count=0
    for permutation in itertools.permutations(range(7)):
        count+=1
        if count%128==0:check()
        sign=(-1)**sum(permutation[i]>permutation[j] for i in range(7) for j in range(i+1,7))
        term={ZERO:sign}
        for i,j in enumerate(permutation):
            term=product(term,matrix[i][j])
            if not term:break
        add_scaled(total,term,1)
    assert count==5040

    @lru_cache(None)
    def laplace(columns):
        check()
        row=7-len(columns)
        if not columns:return {ZERO:1}
        result={}
        for position,column in enumerate(columns):
            if matrix[row][column]:
                minor=laplace(columns[:position]+columns[position+1:])
                add_scaled(result,product(matrix[row][column],minor),(-1)**position)
        return result
    second=laplace(tuple(range(7)))
    assert total==second
    assert all(0<=key[0]<=7 and all(0<=e<=2 for e in key[1:]) for key in total)
    coefficients=[{key[1:]:value for key,value in total.items() if key[0]==power} for power in range(8)]
    assert coefficients[0]==coefficients[7]=={(0,0,0,0):1}
    assert coefficients==coefficients[::-1]
    first={(0,0,0,0):-1,(1,0,0,0):1,(0,0,0,1):2,(1,0,0,1):-1,
           (0,1,0,0):2,(2,0,0,0):-1,(0,2,0,0):-1,(0,0,2,0):-1,
           (0,0,0,2):-1,(1,0,1,0):-1,(0,1,1,0):-1,(1,1,1,0):1}
    assert coefficients[1]==first
    reduced=[]
    for poly in coefficients[1:4]:
        small={}
        for ex,value in poly.items():
            small[ex[:3]]=small.get(ex[:3],0)+value*(2**ex[3])
        reduced.append({e:v for e,v in small.items() if v})
    prior=json.loads((REPO/'mathematics/computations/outputs/Yin_J_G0108/verifier/verification.json').read_text())
    assert [encode(p) for p in reduced]==prior['coefficient_polynomials']
    result={'status':'complete','scope':inp,'formal_permutation_count':count,
            'laplace_states':laplace.cache_info().currsize,'methods_agree':True,
            'variable_order':['x','y','z','w'],'full_symbolic_pencil':[encode(p) for p in coefficients],
            'coefficient_order':['a','b','c'],'coefficient_polynomials':[encode(p) for p in coefficients[1:4]],
            'separate_variable_degree_bounds':[2,2,2,2],
            'trace_first_coefficient_agrees':True,'w_equals_two_matches_accepted_J108':True,
            'no_parameter_grid_or_modular_search':True}
    check();payload=(json.dumps(result,indent=2)+'\n').encode('utf-8')
    assert len(payload)<=CAP_OUTPUT-65536
    OUT.mkdir(parents=True,exist_ok=True)
    pending=OUT/'result.pending';pending.write_bytes(payload);check();pending.replace(OUT/'result.json');check()
    print(json.dumps({'status':'complete','permutations':count,'laplace_states':laplace.cache_info().currsize,
                      'methods_agree':True,'coefficient_term_counts':[len(p) for p in coefficients[1:4]]}))
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
    start = time.monotonic()
    kernel, job, limits = make_job()
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
        if time.monotonic() - start > CAP_SECONDS:
            result["status"] = "wall_time_stop_preservation"
            result["wall_seconds"] = time.monotonic() - start
            (OUT / "execution.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(result, indent=2))
            return 2
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
