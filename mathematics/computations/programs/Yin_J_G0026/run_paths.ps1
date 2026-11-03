param([double]$Radius = 8, [int]$NodeCap = 6000000, [string]$OutputName = 'paths-r8')
$ErrorActionPreference = 'Stop'
$repositoryPath = Get-Item -LiteralPath $PSScriptRoot
while (-not (Test-Path -LiteralPath (Join-Path $repositoryPath.FullName 'repository/config.json'))) { $repositoryPath = $repositoryPath.Parent }
$outputHome = Join-Path $repositoryPath.FullName ('mathematics/computations/outputs/' + (Split-Path $PSScriptRoot -Leaf))
New-Item -ItemType Directory -Path $outputHome -Force | Out-Null
$basePath = $outputHome
$parameters = Get-Content -LiteralPath (Join-Path $basePath 'path-parameters.json') -Raw | ConvertFrom-Json
$embedding = New-Object 'double[,]' 10,10
for ($i=0; $i -lt 10; $i++) { for ($j=0; $j -lt 10; $j++) { $embedding[$i,$j] = $parameters.embedding[$i][$j] } }
$outputPath = Join-Path $basePath $OutputName
New-Item -ItemType Directory -Path $outputPath -Force | Out-Null
Add-Type -TypeDefinition (Get-Content -LiteralPath (Join-Path $PSScriptRoot 'Paths.cs') -Raw)
$timer = [System.Diagnostics.Stopwatch]::StartNew()
$result = [LehmerPathsG26]::Run($embedding,$parameters.expanding_bound,$parameters.contracting_bound,
    $Radius,$NodeCap,(Join-Path $basePath 'compact-states.bin'),$outputPath)
$timer.Stop()
$record = $result | ConvertFrom-Json
$record | Add-Member -NotePropertyName scope -NotePropertyValue 'Floating pruning only discovers integer path witnesses; no nonreturn assertion from missing states or a cap.'
$record | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $outputPath 'discovery.json') -Encoding utf8
$record | ConvertTo-Json -Depth 4
