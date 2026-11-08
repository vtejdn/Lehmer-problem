// Enumerate the full reciprocal integer coefficient space at M <= 6/5.
// All powers of 6/5 and all rounding allowances are computed as exact ratios.
"use strict";
const degree = Number(process.argv[2]);
if (![14, 18, 20].includes(degree)) throw Error("Expected degree 14, 18 or 20");
const half = degree / 2;
const maxPower = 32;
const denom = 30n ** BigInt(maxPower);
const error = Array.from({length: maxPower + 1}, (_, k) => {
  const a = 6n ** BigInt(k), b = 5n ** BigInt(k);
  return (a-b)**2n * (denom/(a*b));
});
const bound = error.map(e => degree + Number(e / denom));
const powers = new Array(maxPower + 1).fill(0);
const coeff = new Array(degree + 1).fill(0);
coeff[0] = coeff[degree] = 1;
const projection = [[2], [2,-2], [2,-1,-1], [2,0,-2,0], [2,1,-1,-2,-1,1]];
// For each prefix length, retain Fejer tests whose last moment has nonzero weight.
const cuts = [null];
for (let k=1; k<=half; ++k) {
  const row = [];
  for (let h=1; h<=k; ++h) {
    if (k % h) continue;
    const m=k/h;
    for (const phase of projection) {
      const weights = [];
      let allowance = 0n;
      for (let j=1; j<=m; ++j) {
        const w=(m+1-j)*phase[j%phase.length];
        weights.push(w);
        allowance += BigInt(Math.abs(w))*error[h*j];
      }
      const last=weights.pop();
      if (last) row.push({h, weights, last, constant:(m+1)*degree+Number(allowance/denom)});
    }
  }
  cuts.push(row);
}
const counts = new Array(half+1).fill(0);
const survivors = [];
function checkTail() {
  for (let k=half+1; k<=maxPower; ++k) {
    let value = k<=degree ? -k*coeff[k] : 0;
    for (let i=1; i<=Math.min(degree,k-1); ++i) value -= coeff[i]*powers[k-i];
    if (!Number.isSafeInteger(value)) throw Error("Unsafe tail moment");
    if (Math.abs(value)>bound[k]) return;
    powers[k]=value;
  }
  survivors.push(coeff.slice(1,half+1));
}
function visit(k) {
  let lo=-bound[k], hi=bound[k];
  for (const {h,weights,last,constant} of cuts[k]) {
    let base=constant;
    for (let j=0; j<weights.length; ++j) base+=weights[j]*powers[(j+1)*h];
    if (last>0) lo=Math.max(lo,Math.ceil(-base/last));
    else hi=Math.min(hi,Math.floor(-base/last));
    if (lo>hi) return;
  }
  let offset=0;
  for (let j=1; j<k; ++j) offset-=coeff[j]*powers[k-j];
  if (!Number.isSafeInteger(offset)) throw Error("Unsafe prefix");
  for (let v=Math.ceil((offset-hi)/k); v<=Math.floor((offset-lo)/k); ++v) {
    powers[k]=offset-k*v;
    coeff[k]=coeff[degree-k]=v;
    ++counts[k];
    if (k===half) checkTail();
    else visit(k+1);
  }
}
visit(1);
process.stdout.write(JSON.stringify({degree,counts,survivors}));
