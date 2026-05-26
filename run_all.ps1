$ErrorActionPreference = "Stop"
$python = "py"
& $python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Blad instalacji requirements.txt" }
$scripts = @(
    ".\scripts\00_download_data.py",
    ".\scripts\01_prepare_data.py",
    ".\scripts\02_summary_statistics.py",
    ".\scripts\03_cases_deaths_trends.py",
    ".\scripts\04_usa_vs_poland.py",
    ".\scripts\05_vaccination_analysis.py",
    ".\scripts\06_hospital_testing.py",
    ".\scripts\07_inferential_regression.py",
    ".\scripts\08_build_dashboard.py"
)
foreach ($script in $scripts) {
    & $python $script
    if ($LASTEXITCODE -ne 0) { throw "Blad w skrypcie $script" }
}
Write-Host "Gotowe. Otworz plik html\index.html"
