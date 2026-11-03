"""Independent all-mask integer verification for J110; no author math imports."""
from __future__ import annotations
import ctypes
from ctypes import wintypes
from functools import lru_cache
import json, os, subprocess, sys, time, traceback
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
AUTHOR=REPO/'mathematics/computations/outputs'/HERE.name/'author'
OUT=REPO/'mathematics/computations/outputs'/HERE.name/'verifier'
SECONDS=300
MEMORY=512*1024*1024
OUTPUT_LIMIT=64*1024*1024
SIZE=1<<21
POSITIONS=tuple((i,j) for i in range(7) for j in range(i+1,7))
BITS={pair:1<<i for i,pair in enumerate(POSITIONS)}
TARGETS={'phi2_phi6_p4':[1,-1,-1,0,0,-1,-1,1],
         'phi2_p6':[1,0,-1,-1,-1,-1,0,1]}
BOUND=176400

def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def binary_matrix(mask):
    out=[[int(i==j) for j in range(7)] for i in range(7)]
    for bit,(i,j) in enumerate(POSITIONS):out[i][j]=int(bool(mask&(1<<bit)))
    return out

def product(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def newton_pencil(u):
    n=len(u)
    assert all(u[i][i]==1 for i in range(n))
    assert all(u[i][j]==0 for i in range(n) for j in range(i))
    inverse=[[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        inverse[i][i]=1
        for j in range(i+1,n):
            inverse[i][j]=-sum(u[i][k]*inverse[k][j] for k in range(i+1,j+1))
    ident=[[int(i==j) for j in range(n)] for i in range(n)]
    assert product(u,inverse)==ident
    transposed=[list(row) for row in zip(*u)]
    companion=[[-x for x in row] for row in product(inverse,transposed)]
    powers=ident
    traces=[0]
    coefficients=[1]
    for k in range(1,n+1):
        powers=product(powers,companion)
        traces.append(sum(powers[i][i] for i in range(n)))
        numerator=-sum(coefficients[k-j]*traces[j] for j in range(1,k+1))
        assert numerator%k==0
        coefficients.append(numerator//k)
    return coefficients[::-1]

def witness_payload(mask):
    u=binary_matrix(mask)
    absolute=[[int(i==j) if i>=j else -abs(u[i][j]) for j in range(7)] for i in range(7)]
    cover=[[int(i==j) for j in range(14)] for i in range(14)]
    for i,j in POSITIONS:
        value=u[i][j]
        for sheet in (0,1):
            if value:
                other=sheet if value<0 else 1-sheet
                cover[2*i+sheet][2*j+other]=-abs(value)
    def describe(matrix):
        return {'matrix':matrix,'polynomial':newton_pencil(matrix),'rank':len(matrix),
                'height':max(abs(x) for row in matrix for x in row),
                'energy':sum(matrix[i][j]**2 for i in range(len(matrix)) for j in range(i+1,len(matrix)))}
    first,second,third=map(describe,(u,absolute,cover))
    assert third['polynomial']==convolution(first['polynomial'],second['polynomial'])
    return {'mask':mask,'original':first,'negative_absolute':second,'literal_cover':third,
            'direct_cover_product_check':True}

def worker():
    if sys.stdin.readline().strip()!='GO':raise RuntimeError('hard guard handshake required')
    started=time.perf_counter()
    def check():
        if time.perf_counter()-started>SECONDS-3:raise TimeoutError('declared aggregate budget; no retry')
    print(json.dumps({'stage':'independent_worker_started'}),flush=True)
    import numpy as np
    inp=json.loads((HERE/'inputs.json').read_text())
    assert inp['rank']==7 and inp['strict_upper_values']==[0,1]
    assert inp['upper_positions']==[list(x) for x in POSITIONS]
    assert inp['target_polynomials']==TARGETS
    assert inp['integer_domain_size']==SIZE
    assert inp['caps']=={'seconds':SECONDS,'worker_memory_bytes':MEMORY,'output_bytes':OUTPUT_LIMIT}
    assert inp['coefficient_dtype']=='int32' and inp['mask_dtype']=='uint32'
    assert inp['selection']=='minimum strict-upper squared-entry energy; smallest mask tie-break'
    assert convolution([1,1],convolution([1,-1,1],[1,-1,-1,-1,1]))==TARGETS['phi2_phi6_p4']
    assert convolution([1,1],[1,-1,0,-1,0,-1,1])==TARGETS['phi2_p6']
    author=json.loads((AUTHOR/'result.json').read_text())
    execution=json.loads((AUTHOR/'execution.json').read_text())
    assert author['status']==execution['status']=='complete' and execution['returncode']==0
    assert author['scope']==inp and author['all_binary_matrices_evaluated']==SIZE
    assert execution['wall_seconds']<=SECONDS
    assert execution['worker_job_memory_cap_bytes']==execution['worker_working_set_cap_bytes']==MEMORY
    assert execution['peak_worker_commit_bytes']<=MEMORY and execution['peak_job_commit_bytes']<=MEMORY

    # First-row recursive Laplace expansion: no permutation generator or author helper.
    @lru_cache(None)
    def minor(columns):
        row=7-len(columns)
        if not columns:return {(0,0):1}
        check()
        result={}
        for position,column in enumerate(columns):
            sign=-1 if position%2 else 1
            sub=minor(columns[:position]+columns[position+1:])
            if row==column:
                entries=((0,0),(0,1))
            else:
                bit=BITS[min(row,column),max(row,column)]
                entries=((bit,int(row<column)),)
            for (support,power),coefficient in sub.items():
                for bit,shift in entries:
                    key=(support|bit,power+shift)
                    result[key]=result.get(key,0)+sign*coefficient
        return {key:value for key,value in result.items() if value}

    terms=minor(tuple(range(7)))
    sparse={}
    for (support,power),value in terms.items():
        assert 0<=power<=7
        sparse.setdefault(support,[0]*8)[power]=value
    for support,row in sparse.items():
        assert row==row[::-1]
        assert row[0]==row[7]==int(support==0)
        assert max(abs(x) for x in row)<=BOUND
    formal_rows=[[support]+row for support,row in sorted(sparse.items())]
    author_formal=json.loads((AUTHOR/'sparse_coefficients.json').read_text())
    assert author_formal['rows']==formal_rows
    assert len(sparse)==author['sparse_nonzero_supports']
    print(json.dumps({'stage':'all_eight_laplace_coefficients_checked','supports':len(sparse),
                      'memoized_minor_states':minor.cache_info().currsize}),flush=True)

    table=np.zeros((3,SIZE),dtype=np.int64)
    for support,row in sparse.items():table[:,support]=row[1:4]
    extrema=[]
    for bit in range(20,-1,-1):
        check()
        step=1<<bit
        blocks=table.reshape(3,-1,2,step)
        blocks[:,:,1,:]+=blocks[:,:,0,:]
        lower,upper=int(table.min()),int(table.max())
        assert -BOUND<=lower<=upper<=BOUND
        extrema.append([bit,lower,upper])
    author_table=np.load(AUTHOR/'coefficients.npy',mmap_mode='r',allow_pickle=False)
    assert author_table.shape==(SIZE,3) and author_table.dtype==np.dtype('int32')
    compared=0
    for first in range(0,SIZE,65536):
        last=min(SIZE,first+65536)
        assert np.array_equal(table[:,first:last],author_table[first:last,:].T)
        compared+=3*(last-first)
    assert compared==3*SIZE
    print(json.dumps({'stage':'full_table_comparison_pass','entries':compared}),flush=True)

    def full(mask):
        a,b,c=map(int,table[:,mask])
        return [1,a,b,c,c,b,a,1]
    controls=[]
    for mask in (0,SIZE-1,7092,2323):
        p=newton_pencil(binary_matrix(mask))
        assert p==full(mask)
        controls.append({'mask':mask,'integer_polynomial':p})
    assert controls==author['direct_integer_controls']

    outcomes={}
    matching={}
    for name,target in TARGETS.items():
        check()
        ids=np.flatnonzero(np.all(table==np.asarray(target[1:4],dtype=np.int64)[:,None],axis=0)).astype(np.uint32)
        matching[name]=ids
        stored=np.load(AUTHOR/f'matches_{name}.npy',allow_pickle=False)
        assert stored.dtype==np.dtype('uint32') and stored.ndim==1
        assert np.array_equal(stored,ids)
        histogram=[0]*22
        best=None
        for raw in ids:
            mask=int(raw)
            assert full(mask)==target
            energy=mask.bit_count()
            histogram[energy]+=1
            if best is None or (energy,mask)<(best.bit_count(),best):best=mask
        witness=None if best is None else witness_payload(best)
        result={'target':target,'match_count':int(ids.size),
                'all_matching_masks_file':f'matches_{name}.npy','energy_histogram':histogram,
                'minimum_energy':None if best is None else best.bit_count(),
                'selected_minimum_energy_mask':best,'witness':witness}
        assert result==author['targets'][name]
        outcomes[name]=result

    payload={'status':'complete','scope':inp,'all_binary_matrices_evaluated':SIZE,
             'all_table_entries_compared':compared,'all_eight_symbolic_coefficients_checked':True,
             'sparse_nonzero_supports':len(sparse),'recursive_minor_states':minor.cache_info().currsize,
             'generation':'recursive Laplace minors; exact Python-integer Boolean supports',
             'evaluation':'descending-bit subset transform; transposed int64 table',
             'coefficient_table_file':'coefficients.npy','coefficient_table_orientation':'3 rows, 2097152 columns',
             'retained_coefficient_dtype':'int32','working_coefficient_dtype':'int64',
             'integer_intermediate_bound':BOUND,'stage_extrema':extrema,
             'full_coefficient_pattern':[1,'a','b','c','c','b','a',1],
             'independent_newton_controls':controls,'targets':outcomes,
             'numpy_version':np.__version__,'shared_engine_boundary':'same NumPy and host; no author mathematics imports',
             'worker_seconds_before_serialization':time.perf_counter()-started}
    result_bytes=(json.dumps(payload,indent=2)+'\n').encode()
    formal_bytes=(json.dumps({'coefficient_order':'ascending t0..t7','rows':formal_rows},indent=2)+'\n').encode()
    retained=table.astype(np.int32)
    planned=retained.nbytes+sum(x.nbytes for x in matching.values())+len(result_bytes)+len(formal_bytes)+65536
    assert planned<OUTPUT_LIMIT
    OUT.mkdir(parents=True,exist_ok=True)
    np.save(OUT/'coefficients.npy',retained,allow_pickle=False)
    for name,ids in matching.items():np.save(OUT/f'matches_{name}.npy',ids,allow_pickle=False)
    (OUT/'sparse_coefficients.json').write_bytes(formal_bytes)
    check()
    used=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    assert used+len(result_bytes)<OUTPUT_LIMIT-65536
    (OUT/'verification.pending').write_bytes(result_bytes)
    (OUT/'verification.pending').replace(OUT/'verification.json')
    print(json.dumps({'status':'complete','full_domain':SIZE,
                      'counts':{name:result['match_count'] for name,result in outcomes.items()}}),flush=True)

# Operational guard definitions below are copied from the reviewer's J107 verifier.
class BasicLimit(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong),
                ("PerJobUserTimeLimit", ctypes.c_longlong), ("LimitFlags", wintypes.DWORD),
                ("MinimumWorkingSetSize", ctypes.c_size_t), ("MaximumWorkingSetSize", ctypes.c_size_t),
                ("ActiveProcessLimit", wintypes.DWORD), ("Affinity", ctypes.c_size_t),
                ("PriorityClass", wintypes.DWORD), ("SchedulingClass", wintypes.DWORD)]

class IOCounters(ctypes.Structure):
    _fields_ = [(x, ctypes.c_ulonglong) for x in ("ReadOperationCount", "WriteOperationCount",
        "OtherOperationCount", "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

class ExtendedLimit(ctypes.Structure):
    _fields_ = [("BasicLimitInformation", BasicLimit), ("IoInfo", IOCounters)] + [
        (x, ctypes.c_size_t) for x in ("ProcessMemoryLimit", "JobMemoryLimit",
                                      "PeakProcessMemoryUsed", "PeakJobMemoryUsed")]

def attach_memory_job(process):
    if os.name != "nt":
        raise RuntimeError("Declared verifier resource wrapper requires Windows; no unguarded fallback")
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
    kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.QueryInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                                wintypes.DWORD, ctypes.c_void_p]
    kernel.SetProcessWorkingSetSizeEx.argtypes = [wintypes.HANDLE, ctypes.c_size_t,
                                                 ctypes.c_size_t, wintypes.DWORD]
    kernel.GetProcessWorkingSetSizeEx.argtypes = [wintypes.HANDLE, ctypes.c_void_p,
                                                 ctypes.c_void_p, ctypes.c_void_p]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = ExtendedLimit()
    limits.BasicLimitInformation.LimitFlags = 0x100 | 0x200 | 0x2000
    limits.BasicLimitInformation.MinimumWorkingSetSize = 1024 * 1024
    limits.BasicLimitInformation.MaximumWorkingSetSize = MEMORY
    limits.ProcessMemoryLimit = MEMORY
    limits.JobMemoryLimit = MEMORY
    if not kernel.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(process._handle)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    # Primary memoryapi contract: disable hard minimum, enable hard maximum.
    handle = wintypes.HANDLE(process._handle)
    if not kernel.SetProcessWorkingSetSizeEx(handle, 1024 * 1024, MEMORY, 0x2 | 0x4):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    lo, hi, flags = ctypes.c_size_t(), ctypes.c_size_t(), wintypes.DWORD()
    if not kernel.GetProcessWorkingSetSizeEx(handle, ctypes.byref(lo), ctypes.byref(hi), ctypes.byref(flags)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    if hi.value > MEMORY or not (flags.value & 0x4):
        kernel.CloseHandle(job)
        raise RuntimeError("Verifier hard working-set maximum was not confirmed")
    return kernel, job

def parent():
    if OUT.exists() and any(OUT.iterdir()):
        raise RuntimeError('existing verifier output: no implicit retry or overwrite')
    started=time.perf_counter()
    process=None
    job=None
    kernel=None
    stdout=stderr=''
    failure=None
    measured=None
    try:
        process=subprocess.Popen([sys.executable,str(Path(__file__).resolve()),'--worker'],
            stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,
            creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0),
            env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1',
                 'MKL_NUM_THREADS':'1','NUMEXPR_NUM_THREADS':'1'})
        kernel,job=attach_memory_job(process)
        stdout,stderr=process.communicate('GO\n',timeout=max(0.001,SECONDS-(time.perf_counter()-started)))
        if process.returncode!=0:failure=f'worker exit {process.returncode}'
        if time.perf_counter()-started>SECONDS:failure='aggregate wall cap exceeded'
    except BaseException as error:
        failure=repr(error)
        if process is not None:
            process.kill()
            stdout,stderr=process.communicate(timeout=5)
    finally:
        if job is not None:
            usage=ExtendedLimit()
            if kernel.QueryInformationJobObject(job,9,ctypes.byref(usage),ctypes.sizeof(usage),None):
                measured={'peak_worker_commit_bytes':usage.PeakProcessMemoryUsed,
                          'peak_job_commit_bytes':usage.PeakJobMemoryUsed}
            kernel.CloseHandle(job)
    OUT.mkdir(parents=True,exist_ok=True)
    if failure and (OUT/'verification.json').exists():
        (OUT/'verification.json').replace(OUT/'verification_incomplete_payload.json')
    execution={'status':'complete' if failure is None else 'incomplete',
               'returncode':None if process is None else process.returncode,
               'failure':failure,'wall_seconds':time.perf_counter()-started,
               'worker_memory_cap_bytes':MEMORY,'worker_working_set_cap_bytes':MEMORY,
               'parent_monitor_excluded_from_worker_memory_limit':True,
               'memory_measurement':measured,'stdout':stdout,'stderr':stderr}
    data=(json.dumps(execution,indent=2)+'\n').encode()
    used=sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
    if used+len(data)>OUTPUT_LIMIT:raise RuntimeError('reserved output cap exceeded')
    (OUT/'execution.json').write_bytes(data)
    print(json.dumps(execution,indent=2))
    return 0 if failure is None else 2

if __name__=='__main__':
    try:
        if sys.argv[1:]==['--worker']:
            worker()
        elif not sys.argv[1:]:
            raise SystemExit(parent())
        else:
            raise RuntimeError('no scope-changing options allowed')
    except Exception:
        traceback.print_exc()
        raise SystemExit(1)
