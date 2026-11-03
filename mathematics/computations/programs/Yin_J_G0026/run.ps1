$ErrorActionPreference = 'Stop'
$repositoryPath = Get-Item -LiteralPath $PSScriptRoot
while (-not (Test-Path -LiteralPath (Join-Path $repositoryPath.FullName 'repository/config.json'))) { $repositoryPath = $repositoryPath.Parent }
$outputHome = Join-Path $repositoryPath.FullName ('mathematics/computations/outputs/' + (Split-Path $PSScriptRoot -Leaf))
New-Item -ItemType Directory -Path $outputHome -Force | Out-Null
$basePath = $outputHome
$certificate = Get-Content -LiteralPath (Join-Path $basePath 'enumeration-certificate.json') -Raw | ConvertFrom-Json
function Matrix-Long($rows) {
    $matrix = New-Object 'long[,]' 10,10
    for ($i=0; $i -lt 10; $i++) {
        for ($j=0; $j -lt 10; $j++) { $matrix[$i,$j] = [long]$rows[$i][$j] }
    }
    return ,$matrix
}
$triangle = Matrix-Long $certificate.integer_triangular_T
$transform = Matrix-Long $certificate.unimodular_U
$lower = Matrix-Long $certificate.embedding_lower
$upper = Matrix-Long $certificate.embedding_upper
Add-Type -TypeDefinition (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'Enumerate.cs') -Raw)
$timer = [System.Diagnostics.Stopwatch]::StartNew()
$result = [LehmerCompactG26]::Run($triangle,$transform,$lower,$upper,
    [long[]]$certificate.original_coefficient_bounds,[long[]]$certificate.reduced_coefficient_bounds,
    $certificate.embedding_scale,$certificate.stable_outer_bound_scaled,$certificate.squared_enumeration_radius,
    $certificate.node_cap,$certificate.candidate_cap,(Join-Path $basePath 'compact-states.bin'))
$timer.Stop()
$record = $result | ConvertFrom-Json
$record | Add-Member -NotePropertyName encoding -NotePropertyValue 'little-endian uint64; coefficient a_j is nibble j minus 8'
$record | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $basePath 'enumeration.json') -Encoding utf8
$record | ConvertTo-Json
