"""Complete different-method D201 binary certificate review; no author imports."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse, json, platform, time, traceback

BASE=(_J_PROGRAM / 'binary-review.py').parent
CAP=180
START=time.perf_counter()
COUNTS={'strict_scalar_comparisons':0,'matrices':0,'row_operations':0,
        'kernel_vectors':0,'column_span_computations':0}

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


def gate():
    if time.perf_counter()-START >= CAP:
        raise TimeoutError('Declared180second complete reviewer cap')

def eq(a,b):
    assert type(a) is type(b), (type(a),type(b))
    if isinstance(a,list):
        assert len(a)==len(b)
        for x,y in zip(a,b):eq(x,y)
    elif isinstance(a,dict):
        assert a.keys()==b.keys()
        for key in a:eq(a[key],b[key])
    else:
        assert a==b,(a,b)
        COUNTS['strict_scalar_comparisons']+=1

def pack(vector):
    assert all(type(x) is int and x in (0,1) for x in vector)
    return sum(x<<i for i,x in enumerate(vector))

def unpack(bits,n):return [(bits>>i)&1 for i in range(n)]

def span_rank(vectors):
    """High-bit column insertion; no row elimination or RREF construction."""
    COUNTS['column_span_computations']+=1
    basis={}
    for vector in vectors:
        x=pack(vector)
        while x:
            lead=x.bit_length()-1
            if lead not in basis:
                basis[lead]=x
                break
            x^=basis[lead]
    return len(basis)

def graph(k,name):
    if name=='V':
        labels=[]
        for j in range(k):labels += [('a',j),('b',j),('c',j)]
        labels += [('z',j) for j in range(1,k+1)]+[('a',k)]
        edges=[]
        for j in range(k):
            edges += [(('a',j),('b',j),-1),(('a',j),('c',j),-1),
                      (('b',j),('a',j+1),-1),(('c',j),('a',j+1),1)]
        path=[('a',0)]+[('z',j) for j in range(1,k+1)]+[('a',k)]
        edges += [(path[i],path[i+1],-1) for i in range(len(path)-1)]
        edges += [(('a',0),('a',k),-1)]
    else:
        labels=[('u',0)]+[('z',j) for j in range(1,k+1)]+[('v',0)]
        labels += [('L',j) for j in range(2)]+[('R',j) for j in range(2)]
        labels += [('K',j) for j in range(2*(k-1))]+[('I',j) for j in range(k-3)]
        path=[('u',0)]+[('z',j) for j in range(1,k+1)]+[('v',0)]
        edges=[(path[i],path[i+1],-1) for i in range(len(path)-1)]
        edges += [(('u',0),('v',0),-1)]
        edges += [(('u',0),('L',j),-1) for j in range(2)]
        edges += [(('v',0),('R',j),-1) for j in range(2)]
        edges += [(('K',2*j),('K',2*j+1),-2) for j in range(k-1)]
    ix={label:j for j,label in enumerate(labels)}
    n=len(labels)
    assert n==4*k+1
    V=[[int(i==j) for j in range(n)] for i in range(n)]
    for a,b,w in edges:
        i,j=ix[a],ix[b]
        assert i<j and V[i][j]==0
        V[i][j]=w
    return V,labels

def formula_basis(k,name,labels):
    """Direct independent coordinate-vector construction of the displayed free bits."""
    vectors=[]
    def add(active):vectors.append([int(label in active) for label in labels])
    if name=='V':
        active={('a',j) for j in range(k+1)}
        active|={('z',j) for j in range(1,k+1) if j%2==0 or k%2==0}
        if k%2:active|={('c',j) for j in range(k)}
        add(active)
        if k%2:
            add({('z',j) for j in range(1,k+1) if j%2}|{('c',j) for j in range(k)})
        for j in range(k):add({('b',j),('c',j)})
    else:
        if k%2:
            add({('z',j) for j in range(1,k+1) if j%2}|{('L',1),('R',1)})
        add({('L',0),('L',1)})
        add({('R',0),('R',1)})
        for label in labels:
            if label[0] in ('K','I'):add({label})
    return vectors

def check_matrix(k,name,record):
    gate()
    schema={'name','k','dimension','original_matrix','binary_symmetrization','rref','row_transform',
            'row_operations','pivot_columns','nullspace_basis','formula_kernel_basis','formula_basis_rank',
            'rank','nullity','predicted_rank','all_exact_checks'}
    assert set(record)==schema
    V,labels=graph(k,name)
    n=len(V)
    eq(record['name'],name);eq(record['k'],k);eq(record['dimension'],n)
    eq(record['original_matrix'],V)
    S=[[(V[i][j]+V[j][i])&1 for j in range(n)] for i in range(n)]
    eq(record['binary_symmetrization'],S)
    rank=span_rank([list(col) for col in zip(*S)])
    eq(record['rank'],rank);eq(record['nullity'],n-rank)
    predicted=3*k-(k%2) if name=='V' else k+4-(k%2)
    eq(record['predicted_rank'],predicted);eq(rank,predicted)
    bits=list(map(pack,S));transforms=[1<<i for i in range(n)]
    for op in record['row_operations']:
        assert type(op) is list and len(op)==3
        kind,i,j=op
        assert type(kind) is str and kind in ('swap','add')
        assert type(i) is int and type(j) is int and 0<=i<n and 0<=j<n and i!=j
        if kind=='swap':
            bits[i],bits[j]=bits[j],bits[i]
            transforms[i],transforms[j]=transforms[j],transforms[i]
        else:
            bits[i]^=bits[j];transforms[i]^=transforms[j]
        COUNTS['row_operations']+=1
    R=[unpack(x,n) for x in bits]
    E=[unpack(x,n) for x in transforms]
    eq(record['rref'],R);eq(record['row_transform'],E)
    # Witness validity: independent product and column rank of the transform.
    assert span_rank([list(col) for col in zip(*E)])==n
    for i in range(n):
        product=0
        for j in range(n):
            if E[i][j]:product ^= pack(S[j])
        eq(unpack(product,n),R[i])
    pivots=[]
    for i,row in enumerate(R):
        if i<rank:
            j=next(j for j,x in enumerate(row) if x)
            assert not pivots or j>pivots[-1]
            pivots.append(j)
            eq([R[a][j] for a in range(n)],[int(a==i) for a in range(n)])
        else:eq(row,[0]*n)
    eq(record['pivot_columns'],pivots)
    free=[j for j in range(n) if j not in pivots]
    basis=record['nullspace_basis']
    assert len(basis)==n-rank
    for i,vector in enumerate(basis):
        assert len(vector)==n
        packed=pack(vector)
        eq([sum(a*b for a,b in zip(row,vector))%2 for row in S],[0]*n)
        eq([vector[j] for j in free],[int(h==i) for h in range(len(free))])
        # Exact free-coordinate identity plus annihilation uniquely fixes every entry.
        COUNTS['kernel_vectors']+=1
    eq(span_rank(basis),n-rank)
    formula=formula_basis(k,name,labels)
    eq(record['formula_kernel_basis'],formula)
    for vector in formula:
        eq([sum(a*b for a,b in zip(row,vector))%2 for row in S],[0]*n)
        COUNTS['kernel_vectors']+=1
    eq(record['formula_basis_rank'],span_rank(formula))
    eq(len(formula),n-rank)
    eq(record['formula_basis_rank'],n-rank)
    eq(record['all_exact_checks'],True)
    COUNTS['matrices']+=1
    return rank

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'binary-review-result.json'))
    target=ap.parse_args().output.resolve()
    assert target.parent==_J_OUTPUT
    out={'status': 'started', 'domain_k': [3, 4, 5, 6], 'method': 'independent labelled graph, high-bit column insertion, exact certificate replay', 'instances': []}
    observed=['binary-invariants.py','binary-invariants.json','verify.py','result.json',
              'review_independent.py','review_result.json']
    before={name:(((_J_PROGRAM if name in ('binary-invariants.py', 'binary-review.py', 'mutation-probe.py', 'mutation-review.py', 'readme.md', 'repeated-cell-author.py', 'repeated-cell-review.py', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in observed}
    # Draft existence is not an execution prerequisite after fixed retention.
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0201.md')
    draft_before=draft.read_bytes() if draft.exists() else None
    handle=target.open('x',encoding='utf-8')
    try:
        native=json.loads(before['binary-invariants.json'])
        schema={'status', 'domain_k', 'input', 'graph_helper', 'instances'}
        assert set(native)==schema
        eq(native['status'],'complete')
        eq(native['domain_k'],[3,4,5,6]);eq(native['input'],'result.json')
        eq(native['graph_helper'],'review_independent.py:graph')
        pass
        pass
        assert len(native['instances'])==4
        for k,rec in zip((3,4,5,6),native['instances']):
            assert set(rec)=={'k','V','Z','rank_difference','not_integrally_congruent','common_stabilization_excluded'}
            eq(rec['k'],k)
            a=check_matrix(k,'V',rec['V']);b=check_matrix(k,'Z',rec['Z'])
            eq(rec['rank_difference'],a-b);eq(a-b,2*k-4)
            eq(rec['not_integrally_congruent'],True);eq(rec['common_stabilization_excluded'],True)
            out['instances'].append({'k':k,'V_rank':a,'Z_rank':b,'difference':a-b})
        gate()
        out.update(status='complete', counts=COUNTS)
    except Exception as error:
        out.update(status='incomplete',counts=COUNTS,error_type=type(error).__name__,error=_record_text(str(error)),
                   traceback=_record_text(traceback.format_exc()))
        raise
    finally:
        out.update()
        json.dump(out,handle,indent=2);handle.write('\n');handle.close()
        print(json.dumps(out),flush=True)

if __name__=='__main__':main()
