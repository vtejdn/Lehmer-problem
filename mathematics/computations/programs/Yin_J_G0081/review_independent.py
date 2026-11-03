"""Independent complete J81 review for Yin; declared before first execution.

Domain: exactly k=2..6, all 30 saved literal matrices and mathematical fields.
Aggregate cap: 120 seconds; no search, random choices or domain extension.
Method: integer Bareiss at dimension+1 points (550 full-pencil determinants),
matching-polynomial continuants, explicit DAG paths, integer factor convolution.
No author program imports, inverse computation, characteristic polynomial routine,
floating root calculation, irreducibility oracle, or retired-draft requirement.
Native readme/verify/result bytes are compared within this run, not fingerprinted.
First output, including a failed execution if any, is retained; no overwrite.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from math import comb, isfinite
import argparse
import json
import time

HERE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 120
START = time.perf_counter()
COUNTS = {'matrices': 0, 'pencil_determinants': 0, 'residual_determinants': 0,
          'factor_products': 0, 'continuants': 0, 'mixed_trace_entries': 0}


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


def guard():
    assert time.perf_counter()-START < CAP, 'declared aggregate cap'


def ints(values):
    assert all(type(x) is int for x in values)


def trim(p):
    p = list(p)
    while len(p)>1 and not p[-1]:
        p.pop()
    return p


def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]+=a*b
    return trim(r)


def power(p,n):
    r=[1]
    for _ in range(n):
        r=mul(r,p)
    return r


def add(p,q):
    r=[0]*max(len(p),len(q))
    for i,a in enumerate(p): r[i]+=a
    for i,a in enumerate(q): r[i]+=a
    return trim(r)


def ev(p,t):
    r=0
    for a in reversed(p): r=r*t+a
    return r


def det(a):
    """Integer fraction-free elimination, with exact pivot row swaps."""
    guard()
    a=[row[:] for row in a]
    n=len(a); old=1; sign=1
    for k in range(n-1):
        p=next((j for j in range(k,n) if a[j][k]),None)
        if p is None: return 0
        if p!=k: a[p],a[k]=a[k],a[p]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator%old==0
                a[i][j]=numerator//old
            a[i][k]=0
        old=pivot
    return sign*a[-1][-1] if n else 1


def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def inputs(k):
    labels=[]
    for i in range(k): labels.extend([('a',i),('b',i),('c',i)])
    labels.append(('a',k))
    index={v:i for i,v in enumerate(labels)}
    v=identity(len(labels))
    for i in range(k):
        for source,target,s in [(('a',i),('b',i),-1),
                                (('a',i),('c',i),-1),
                                (('b',i),('a',i+1),-1),
                                (('c',i),('a',i+1),1)]:
            v[index[source]][index[target]]=s
    v[index['a',0]][index['a',k]]=-1
    z=identity(3*k+1)
    for i in range(k+1): z[2*i][2*i+1]=-2 if i<k else -1
    return v,z


def absolute(v):
    n=len(v)
    return [[v[i][j] if i==j else -abs(v[i][j]) for j in range(n)]
            for i in range(n)]


def cover(v):
    n=len(v); w=identity(2*n)
    for i in range(n):
        for j in range(i+1,n):
            a=v[i][j]
            for sheet in (0,1):
                dest=sheet if a<=0 else 1-sheet
                w[2*i+sheet][2*j+dest]=-abs(a)
    return w


def matching_f(j):
    if j==-1: return [0]
    result=[0]
    for m in range(j//2+1):
        p=power([1,-2,1],j-2*m)
        term=[0]*(2*m)+[comb(j-m,m)*(-4)**m*a for a in p]
        result=add(result,term)
    return result


def mixed_paths(v):
    n=len(v); neighbors=[[j for j in range(i+1,n) if v[i][j]] for i in range(n)]
    values=[0]*(n-1)
    for source in range(n):
        stack=[(source,0)]
        while stack:
            here,length=stack.pop()
            if length and v[source][here]: values[length-1]+=1
            for nxt in neighbors[here]: stack.append((nxt,length+1))
    return values


def record_check(rec,v):
    assert set(rec)=={'matrix','dimension','height','energy','total_square_sum',
                      'monodromy_trace','polynomial','integer_factors'}
    n=len(v)
    assert type(rec['dimension']) is int and rec['dimension']==n
    assert rec['matrix']==v and len(rec['matrix'])==n
    for i,row in enumerate(rec['matrix']):
        ints(row); assert len(row)==n and row[i]==1
        assert all(row[j]==0 for j in range(i))
    e=sum(v[i][j]**2 for i in range(n) for j in range(i+1,n))
    expected={'height':max(abs(x) for row in v for x in row),
              'energy':e,'total_square_sum':n+e}
    for key,val in expected.items():
        assert type(rec[key]) is int and rec[key]==val
    poly=rec['polynomial']; ints(poly)
    assert len(poly)==n+1 and poly[0]==poly[-1]==1 and poly==poly[::-1]
    # An n-degree polynomial is fixed by these n+1 distinct evaluations.
    for t in range(n+1):
        value=det([[t*v[i][j]+v[j][i] for j in range(n)] for i in range(n)])
        assert value==ev(poly,t),(n,t,value,ev(poly,t))
        COUNTS['pencil_determinants']+=1
    assert type(rec['monodromy_trace']) is int and rec['monodromy_trace']==-poly[-2]
    rebuilt=[1]
    for factor in rec['integer_factors']:
        assert set(factor)=={'polynomial','multiplicity'}
        f=factor['polynomial']; m=factor['multiplicity']; ints(f)
        assert type(m) is int and m>=1 and len(f)>=2 and f[-1]==1
        rebuilt=mul(rebuilt,power(f,m))
    assert rebuilt==poly
    COUNTS['factor_products']+=1; COUNTS['matrices']+=1
    return poly


def verify(data):
    assert set(data)=={'scope', 'controls', 'success'} and data['success'] is True
    assert data['scope']=={'k_values': [2, 3, 4, 5, 6], 'paired_controls': 5, 'complete_polynomials': 30, 'search': False, 'coefficient_order': 'ascending', 'arithmetic': 'exact integer'}
    pass
    pass
    pass
    pass
    assert len(data['controls'])==5
    for k,row in zip(range(2,7),data['controls']):
        guard()
        assert set(row)=={'k','target','residual_D','continuants','path_terms_j1_to_nminus1',
                          'reciprocal_epsilon','twice_cosh_lower_bound','exp_measure_lower_bound','records'}
        assert type(row['k']) is int and row['k']==k
        n=3*k+1; v,z=inputs(k)
        matrices={'connected_original':v,'connected_absolute':absolute(v),'connected_cover':cover(v),
                  'disconnected_original':z,'disconnected_absolute':absolute(z),'disconnected_cover':cover(z)}
        assert set(row['records'])==set(matrices)
        ps={name:record_check(row['records'][name],matrix) for name,matrix in matrices.items()}
        target=mul(mul(power([1,1],k-1),power([-1,1],2*k)),[1,1,1])
        ints(row['target']); assert row['target']==target
        assert ps['connected_original']==ps['disconnected_original']==ps['disconnected_absolute']==target
        assert ps['connected_cover']==mul(target,ps['connected_absolute'])
        assert ps['disconnected_cover']==mul(target,target)
        assert set(row['continuants'])=={str(i) for i in range(-1,k)}
        for j in range(-1,k):
            ints(row['continuants'][str(j)])
            assert row['continuants'][str(j)]==matching_f(j)
            COUNTS['continuants']+=1
        residual=row['residual_D']; ints(residual)
        assert len(residual)==2*k+3 and residual[0]==residual[-1]==1 and residual==residual[::-1]
        assert mul(power([1,1],k-1),residual)==ps['connected_absolute']
        # Independent reduced determinant, without using the saved continuant formula.
        for t in range(2*k+3):
            q=t+1; a=[[0]*(k+1) for _ in range(k+1)]
            for i in range(k+1): a[i][i]=t*t+1 if i in (0,k) else (t-1)**2
            for i in range(k): a[i][i+1]=-2*t*t; a[i+1][i]=-2
            a[0][k]=-t*q; a[k][0]=-q
            assert det(a)==ev(residual,t)
            COUNTS['residual_determinants']+=1
        paths=mixed_paths(v); ints(row['path_terms_j1_to_nminus1'])
        assert paths==row['path_terms_j1_to_nminus1']
        assert paths==[4*k+1 if j==1 else 2**k if j==2*k else 0 for j in range(1,n)]
        COUNTS['mixed_trace_entries']+=len(paths)
        assert -n+sum(paths)==ps['connected_absolute'][-2]*-1==k+2**k
        scalars={'reciprocal_epsilon':n%2,'twice_cosh_lower_bound':2**k-2*k+1+2*(n%2),
                 'exp_measure_lower_bound':max(1,2**k-2*k)}
        for key,value in scalars.items(): assert type(row[key]) is int and row[key]==value
        for name,record in row['records'].items():
            scale=2 if name.endswith('cover') else 1
            assert record['dimension']==scale*(3*k+1) and record['energy']==scale*(4*k+1)
            assert record['total_square_sum']==scale*(7*k+2)
    assert COUNTS=={'matrices':30,'pencil_determinants':550,'residual_determinants':55,
                    'factor_products':30,'continuants':25,'mixed_trace_entries':60}
    return {'all_native_mathematical_fields_checked': True, 'exact_schema_checked': True, 'factor_scope': 'complete exact product identities; no residual irreducibility assertion'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=(_J_OUTPUT / 'review_result.json'))
    output=parser.parse_args().output
    assert not output.exists(), 'preserve first review result'
    names=['readme.md','verify.py','result.json']
    before={name:(((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
    report={'scope': 'all five k2..6 controls, 30 matrices, entire saved mathematical payload', 'method': 'Bareiss pencil evaluations; matching expansion; DAG paths; integer convolution; no author imports'}
    try:
        report.update(verify(json.loads(before['result.json'])))
        report['success']=True
    except BaseException as error:
        report.update(success=False,error_type=type(error).__name__,error=_record_text(str(error)))
        raise
    finally:
        report['counts']=COUNTS
        pass
        pass
        pass
        with output.open('x',encoding='utf-8') as f: json.dump(report,f,indent=2); f.write('\n')
        print(json.dumps(report))
    assert all(((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name).read_bytes() == data for name, data in before.items())
    assert time.perf_counter()-START < CAP
