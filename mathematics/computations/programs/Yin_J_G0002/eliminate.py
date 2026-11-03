"""Exact finite eliminations for the L G0020 Salem family; retained evidence.

Run: .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0002/eliminate.py
The all-N/all-index reductions and positivity are proved in the L G0038.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

t = s.symbols('t')
f = t**3-t-1
h = 1-t**2-t**3
polys = {
    '4_divides_d_N_even': f*h.subs(t,-t)-h*f.subs(t,-t),
    '4_divides_d_N_odd': f*h.subs(t,-t)+h*f.subs(t,-t),
    'd_odd': h**2*f.subs(t,t**2)+h.subs(t,t**2)*f**2,
    'd_2_mod_4_N_even': h**2*f.subs(t,-t**2)+h.subs(t,-t**2)*f**2,
    'd_2_mod_4_N_odd': -h**2*f.subs(t,-t**2)+h.subs(t,-t**2)*f**2,
}
out={}
orders=set()
for name,g in polys.items():
    g=s.Poly(s.expand(g),t)
    constant,factors=s.factor_list(g)
    fact_rows=[]
    for factor,m in factors:
        if factor.as_expr()==t:
            candidates=[]
        else:
            candidates=[d for d in range(1,101)
                        if s.cyclotomic_poly(d,t)==factor.monic().as_expr()]
        if candidates:
            orders.update(candidates)
        fact_rows.append({'factor':str(factor.as_expr()),'multiplicity':int(m),
                          'cyclotomic_order':candidates})
    out[name]={'polynomial':str(g.as_expr()),'constant':str(constant),'factors':fact_rows}

# Any noncyclotomic factor in an elimination cannot contain a root of unity.
# SymPy's irreducible factorization and cyclotomic predicate supply a separate
# exact check that identifying the factors above leaves no cyclotomic factor.
for name,g in polys.items():
    for factor,m in s.factor_list(s.Poly(g,t))[1]:
        if factor.is_cyclotomic:
            assert any(factor.monic().as_expr()==s.cyclotomic_poly(d,t) for d in orders)

allowed=[]
for d in sorted(orders):
    phi=s.Poly(s.cyclotomic_poly(d,t),t)
    residues=[]
    multiple=[]
    ratios={}
    # q_N modulo Phi_d depends only on N modulo d. For multiplicity>=2,
    # q_N'(z)=0 becomes a linear equation in N after q_N(z)=0.
    for residue in range(d):
        q=s.Poly(t**residue*f+h,t)
        if q.rem(phi).is_zero:
            residues.append(residue)
            # N*h*f = t*(h'*f-h*f') at a common root.
            den=s.Poly(h*f,t).rem(phi)
            rhs=s.Poly(t*(s.diff(h,t)*f-h*s.diff(f,t)),t).rem(phi)
            ratio=(rhs*s.invert(den,phi)).rem(phi)
            ratios[str(residue)]=str(ratio.as_expr())
            if ratio.degree()==0:
                multiple.append(str(ratio.as_expr()))
    if residues:
        allowed.append({'order':d,'N_residues':residues,
                        'possible_repeated_N_constants':sorted(set(multiple)),
                        'repetition_obstruction_remainders':ratios})
out['all_possible_orders_before_residue_filter']=sorted(orders)
out['cyclotomic_divisibility']=allowed
Path(__file__).with_name('elimination.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
