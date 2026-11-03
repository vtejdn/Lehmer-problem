$ErrorActionPreference = 'Stop'
$repositoryPath = Get-Item -LiteralPath $PSScriptRoot
while (-not (Test-Path -LiteralPath (Join-Path $repositoryPath.FullName 'repository/config.json'))) { $repositoryPath = $repositoryPath.Parent }
$outputHome = Join-Path $repositoryPath.FullName ('mathematics/computations/outputs/' + (Split-Path $PSScriptRoot -Leaf))
New-Item -ItemType Directory -Path $outputHome -Force | Out-Null
Add-Type -Path (Join-Path $PSScriptRoot 'Search.cs')
$result = [SalemBicyclicSearch]::Run(250000)
[System.IO.File]::WriteAllText((Join-Path $outputHome 'search.json'), $result + "`n", [System.Text.UTF8Encoding]::new($false))
Write-Output $result
