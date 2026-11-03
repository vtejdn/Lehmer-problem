"""Independent J109 tensor/Newton reconstruction and complete finite-algebra check."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
import itertools,json,math,os,subprocess,sys,time,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=REPO/'mathematics/computations/outputs'/HERE.name/'verifier_revised'
CAP_SECONDS=30
CAP_MEMORY=256*1024*1024
CAP_OUTPUT=32*1024*1024
ZERO=(0,0,0,0)

class Poly:
    def __init__(self,x=0):
        self.d=({k:v for k,v in x.items() if v} if isinstance(x,dict) else ({ZERO:x} if x else {}))
    def __add__(self,b):
        if not isinstance(b,Poly):b=Poly(b)
        d=dict(self.d)
        for k,v in b.d.items():d[k]=d.get(k,0)+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.d.items()})
    def __sub__(self,b):return self+-aspoly(b)
    def __rsub__(self,b):return aspoly(b)+-self
    def __mul__(self,b):
        b=aspoly(b);d={}
        for k,v in self.d.items():
            for l,w in b.d.items():
                e=tuple(i+j for i,j in zip(k,l));d[e]=d.get(e,0)+v*w
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0;r=Poly(1)
        for _ in range(n):r=r*self
        return r
    def __eq__(self,b):return self.d==aspoly(b).d
    def value(self,point):return sum(v*math.prod(a**b for a,b in zip(point,k)) for k,v in self.d.items())
    def encode(self):return [list(k)+[v] for k,v in sorted(self.d.items())]

def aspoly(b):return b if isinstance(b,Poly) else Poly(b)

def multiply(a,b):return [[sum(a[i][k]*b[k][j] for k in range(7)) for j in range(7)] for i in range(7)]

def scalar_pencil(u):
    inv=[[int(i==j) for j in range(7)] for i in range(7)]
    for i in range(6,-1,-1):
        for j in range(i+1,7):inv[i][j]=-sum(u[i][k]*inv[k][j] for k in range(i+1,j+1))
    assert multiply(u,inv)==[[int(i==j) for j in range(7)] for i in range(7)]
    a=multiply(inv,[list(r) for r in zip(*u)])
    power=[[int(i==j) for j in range(7)] for i in range(7)];tr=[0]
    for k in range(1,8):
        power=multiply(power,a);tr.append(sum(power[i][i] for i in range(7)))
    e=[1]
    for k in range(1,8):
        v=sum((-1)**(i-1)*e[k-i]*tr[i] for i in range(1,k+1));assert v%k==0;e.append(v//k)
    result=e[::-1]
    assert result==result[::-1] and result[0]==result[-1]==1
    return result

def worker():
    if sys.stdin.readline().strip()!='JOB_READY':raise RuntimeError('guard required')
    start=time.monotonic()
    def check():
        if time.monotonic()-start>CAP_SECONDS-1:raise TimeoutError('aggregate verifier cap')
    inp=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    positions=[[0,2],[3,4],[4,6],[3,5]]
    base=[[1,0,0,1,0,1,1],[0,1,0,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,2,2,0],[0,0,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
    assert inp['base_matrix']==base and inp['variable_positions']==positions
    assert inp['target_polynomial']==[1,-1,-1,0,0,-1,-1,1]
    nodes=[]
    numerator=[{} for _ in range(8)]
    bases=[[2,-3,1],[0,4,-2],[0,-1,1]]
    for point in itertools.product(range(3),repeat=4):
        check();u=[r[:] for r in base]
        for (i,j),v in zip(positions,point):u[i][j]=v
        pencil=scalar_pencil(u);nodes.append({'point':point,'pencil':pencil})
        for exponent in itertools.product(range(3),repeat=4):
            weight=math.prod(bases[v][k] for v,k in zip(point,exponent))
            if not weight:continue
            for k,c in enumerate(pencil):numerator[k][exponent]=numerator[k].get(exponent,0)+c*weight
    coefficients=[]
    for d in numerator:
        assert all(v%16==0 for v in d.values())
        coefficients.append(Poly({k:v//16 for k,v in d.items()}))
    assert coefficients==coefficients[::-1] and coefficients[0]==1
    author=json.loads((REPO/'mathematics/computations/outputs'/HERE.name/'author/result.json').read_text(encoding='utf-8'))
    assert [p.encode() for p in coefficients]==author['full_symbolic_pencil']
    x,y,z,w=[Poly({tuple(int(i==j) for i in range(4)):1}) for j in range(4)]
    a=-1+x+2*w-x*w+2*y-x*x-y*y-z*z-w*w-x*z-y*z+x*y*z
    b=-7+7*w-2*w*w+(3-w)*z+(w*w-2*w)*z*z+(6-2*w)*y+(w-3)*y*z-2*y*y+x*(6-3*w+(w*w-2)*z+(w-1)*z*z+(w-3)*y+y*z)+x*x*(w*w-w-2+z*z-y+y*y)
    c=-12+11*w-3*w*w+(8-5*w)*z+3*(w-1)**2*z*z+(9-4*w)*y+(3*w-4)*y*z-2*y*y+x*(13-6*w+(w*w-w-3)*z+(w-3)*z*z+(3*w-7)*y+y*z)+x*x*(2*w*w-3*w-1+(1+w-w*w)*z*z+(2*w-3)*y+2*y*y)
    assert [a,b,c]==coefficients[1:4]
    H=7-5*a+3*b-c;q=y-w;r=w*(1+x*z);den=1+x*x
    A=7*x**4+4*x**3+2*x*x+4*x+4;B=6*x**3-4*x*x+8;C=7*x*x-4*x+10
    assert H==den*q*q-(1+2*x+3*x*z)*q+r*r+(2*z-1-x*z)*r+3+z+2*z*z+2*x*z+2*x*x*z*z
    assert 4*den*H==(2*den*q-(1+2*x+3*x*z))**2+den*(2*r+2*z-1-x*z)**2+A*z*z+B*z+C
    square=(2*y-2+z*(1-x))**2+(2*w+x-2)**2+(3-z*z)*x*x+2*z*z*x-(8-4*z-3*z*z)
    assert square==-4*(a+1)
    ranges={-2:[0,1],-1:[-3,-2,-1,0,1,2,3],0:[-3,-2,-1,0,1],1:[-1,0,1],2:[-1,0]}
    quad_expected={-2:[84,-56,-134],-1:[5,-2,-51],0:[4,8,-26],1:[21,10,-59],2:[164,40,-150]}
    for xx,zs in ranges.items():
        aa=A.value((xx,0,0,0));bb=B.value((xx,0,0,0));cc=C.value((xx,0,0,0))-36*(1+xx*xx)
        assert [aa,bb,cc]==quad_expected[xx]
        f=lambda zz:aa*zz*zz+bb*zz+cc
        assert all(f(zz)<=0 for zz in zs) and f(zs[0]-1)>0 and f(zs[-1]+1)>0
        assert 2*aa*(zs[0]-1)+bb<0 and 2*aa*(zs[-1]+1)+bb>0
    remaining=[(-1,-2),(-1,-1),(-1,0),(-1,1),(0,-2),(0,-1),(0,0),(0,1),(1,-1),(1,0)]
    candidates=[]
    for xx,zz in remaining:
        budget=8-4*zz-3*zz*zz-(3-zz*zz)*xx*xx-2*zz*zz*xx
        root=math.isqrt(budget)
        lowy=-((-root+2-zz*(1-xx))//-2);highy=(root+2-zz*(1-xx))//2
        loww=-((-root-xx+2)//-2);highw=(root-xx+2)//2
        for yy in range(lowy,highy+1):
            for ww in range(loww,highw+1):
                point=(xx,yy,zz,ww)
                if square.value(point)!=0:continue
                abc=[poly.value(point) for poly in (a,b,c)];assert abc[0]==-1
                candidates.append({'point':point,'abc':abc})
    assert len(candidates)==32
    survivors=[list(v['point'])+[v['abc'][2]] for v in candidates if v['abc'][1]==-1]
    expected=[[-1,0,0,2,-2],[-1,2,0,1,3],[-1,2,0,2,4],[0,0,0,2,-2],[0,0,1,1,-1],[0,1,1,1,1],[1,0,0,1,1]]
    diagnostic=(json.dumps({'complete_32_candidates':candidates,'computed_survivors':sorted(survivors),'author_corrected_expected':expected},indent=2)+'\n').encode('utf-8')
    assert len(diagnostic)<65536
    OUT.mkdir(parents=True,exist_ok=True);(OUT/'comparison_input.json').write_bytes(diagnostic);check()
    assert sorted(survivors)==expected and all(v[-1] for v in survivors)
    result={'status':'complete','scope':inp,'method':'81 tensor nodes; integer inverse/Newton; exact tensor interpolation; written finite-algebra check','nodes':nodes,'full_symbolic_pencil':[p.encode() for p in coefficients],'author_full_map_agrees':True,'grouped_map_agrees':True,'all_square_identities':True,'necessary_z_ranges':ranges,'complete_32_candidates':candidates,'seven_survivors':survivors,'no_integer_target_in_proved_full_family':True}
    check();payload=(json.dumps(result,indent=2)+'\n').encode('utf-8');assert len(payload)+len(diagnostic)<=CAP_OUTPUT-65536
    OUT.mkdir(parents=True,exist_ok=True);pending=OUT/'result.pending';pending.write_bytes(payload);check();pending.replace(OUT/'result.json');check()
    print(json.dumps({'status':'complete','nodes':len(nodes),'finite_candidates':len(candidates),'survivors':len(survivors),'map_agrees':True}));return 0

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
        raise RuntimeError("verifier output already exists; do not overwrite a prior run implicitly")
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
                  "verifier_stdout": stdout, "verifier_stderr": stderr,
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
