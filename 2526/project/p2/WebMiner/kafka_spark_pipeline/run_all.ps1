# ============================================================
#  run_all.ps1 - Grab Sentiment Pipeline Runner
#  Role: Pipeline & Visualization Engineer
#
#  Usage (from notebooks folder):
#    powershell -ExecutionPolicy Bypass -File run_all.ps1
# ============================================================

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

function Info  { param($msg) Write-Host "[INFO]  $msg" -ForegroundColor Cyan   }
function Ok    { param($msg) Write-Host "[ OK ]  $msg" -ForegroundColor Green  }
function Warn  { param($msg) Write-Host "[WARN]  $msg" -ForegroundColor Yellow }
function Err   { param($msg) Write-Host "[FAIL]  $msg" -ForegroundColor Red    }

# ---------------------------------------------------------------
# Step 0: Prerequisites
# ---------------------------------------------------------------
Info "Checking prerequisites..."

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Err "Docker not found. Install from https://www.docker.com/products/docker-desktop/"
    exit 1
}
Ok "Docker: $(docker --version)"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Err "Python not found. Install from https://www.python.org/downloads/"
    exit 1
}
Ok "Python: $(python --version)"

if (-not (Get-Command java -ErrorAction SilentlyContinue)) {
    Warn "Java not found - PySpark (notebook 07) may fail. Install from https://adoptium.net/"
} else {
    $javaVer = & { $v = java -version 2>&1; "$v" }
    Ok "Java: $($javaVer -split [System.Environment]::NewLine | Select-Object -First 1)"
}

# ---------------------------------------------------------------
# Step 1: Locate and copy data CSV
# ---------------------------------------------------------------
Info "Locating cleaned_data CSV..."

$csvFound = $null
$searchPaths = @(
    "..\cleaned_data (2).csv",
    "..\..\cleaned_data (2).csv",
    "..\cleaned_data.csv",
    "cleaned_data (2).csv",
    "cleaned_data.csv"
)
foreach ($p in $searchPaths) {
    if (Test-Path $p) {
        $csvFound = (Resolve-Path $p).Path
        break
    }
}

if ($null -ne $csvFound) {
    Copy-Item $csvFound ".\cleaned_data.csv"      -Force
    Copy-Item $csvFound ".\cleaned_data (2).csv"  -Force
    Ok "CSV copied from: $csvFound"
} else {
    Warn "CSV not found. Manually copy cleaned_data (2).csv into: $ScriptDir"
}

# ---------------------------------------------------------------
# Step 2: Create google.colab stub
# ---------------------------------------------------------------
Info "Creating google.colab stub..."
New-Item -ItemType Directory -Force -Path "google" | Out-Null

$colabStub = @"
# Stub - allows Colab notebooks to run locally
class files:
    @staticmethod
    def download(path):
        print(f'[LOCAL] Skipping Colab download: {path}')
    @staticmethod
    def upload():
        print('[LOCAL] Skipping Colab upload')
        return {}

def auth_required(f):
    return f
"@
$colabStub | Out-File -FilePath "google\colab.py" -Encoding utf8

# IMPORTANT: use a namespace __init__.py so the real google.protobuf
# (used by TensorFlow) is still findable alongside our google.colab stub.
$googleInit = @"
# Namespace package - do NOT add package-level code here.
# This lets both google.colab (stub) and google.protobuf (real) coexist.
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
"@
$googleInit | Out-File -FilePath "google\__init__.py" -Encoding utf8
Ok "google.colab stub created (namespace-safe)."

# ---------------------------------------------------------------
# Step 3: Environment variables
# ---------------------------------------------------------------
$env:TRANSFORMERS_NO_TF  = "1"
$env:USE_TF              = "0"
$env:TF_USE_LEGACY_KERAS = "1"
Ok "Env vars set: TRANSFORMERS_NO_TF=1, TF_USE_LEGACY_KERAS=1"

# ---------------------------------------------------------------
# Step 4: Install Python dependencies
# ---------------------------------------------------------------
Info "Checking Python dependencies..."

# Check if heavy packages are already installed - skip install on subsequent runs
$depsOk = $true
$checkPkgs = @('torch','tensorflow','pyspark','transformers','papermill','kafka','elasticsearch','sentencepiece')
foreach ($pkg in $checkPkgs) {
    $chk = python -c "import importlib; importlib.import_module('$pkg')" 2>&1
    if ($LASTEXITCODE -ne 0) {
        $depsOk = $false
        Write-Host "  Missing: $pkg" -ForegroundColor DarkGray
        break
    }
}

if ($depsOk) {
    Ok "All dependencies already installed - skipping pip."
} else {
    Info "Installing Python dependencies (first run only)..."
    python -m pip install -r requirements.txt --quiet 2>&1 | Out-Null
    Info "Installing PyTorch CPU..."
    python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu --quiet 2>&1 | Out-Null
    python -m pip install tf-keras papermill joblib "transformers>=4.41.0" "pyspark==3.4.2" sentencepiece --quiet 2>&1 | Out-Null
    Ok "Dependencies installed."
}

# ---------------------------------------------------------------
# Step 4b: Fix Spark environment
# ---------------------------------------------------------------
# If SPARK_HOME points to a pre-installed Spark it will conflict
# with the pip-installed pyspark JARs -> Py4J constructor errors.
# Force pyspark to use its own bundled JARs instead.
if ($env:SPARK_HOME) {
    Warn "SPARK_HOME is set to $($env:SPARK_HOME) - clearing it to avoid JAR version conflict."
    Remove-Item Env:SPARK_HOME -ErrorAction SilentlyContinue
}
# Tell pyspark which Python executable to use on workers
$env:PYSPARK_PYTHON  = (Get-Command python).Source
$env:PYSPARK_DRIVER_PYTHON = (Get-Command python).Source
Ok "Spark env: SPARK_HOME cleared, PYSPARK_PYTHON=$($env:PYSPARK_PYTHON)"

# ---------------------------------------------------------------
# Step 5: Start Docker services
# ---------------------------------------------------------------
Info "Removing leftover containers..."
docker compose down 2>&1 | Out-Null
docker rm -f elasticsearch zookeeper kafka kibana 2>&1 | Out-Null

Info "Starting Kafka + Elasticsearch + Kibana..."
docker compose up -d 2>&1 | Write-Host

if ($LASTEXITCODE -ne 0) {
    Err "docker compose up failed. Is Docker Desktop running?"
    exit 1
}
Ok "Docker services started."

# ---------------------------------------------------------------
# Step 6: Wait for Kafka
# ---------------------------------------------------------------
Info "Waiting for Kafka (up to 120s)..."
$kafkaReady = $false
for ($i = 0; $i -lt 24; $i++) {
    docker exec kafka kafka-broker-api-versions --bootstrap-server localhost:9092 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        $kafkaReady = $true
        break
    }
    Write-Host "  [$i] Kafka not ready, retrying in 5s..." -ForegroundColor DarkGray
    Start-Sleep 5
}
if (-not $kafkaReady) {
    Err "Kafka timed out."
    exit 1
}
Ok "Kafka is healthy."

# ---------------------------------------------------------------
# Step 7: Wait for Elasticsearch
# ---------------------------------------------------------------
Info "Waiting for Elasticsearch (up to 180s)..."
$esReady = $false
for ($i = 0; $i -lt 36; $i++) {
    try {
        $resp = Invoke-RestMethod -Uri "http://localhost:9200/_cluster/health" -TimeoutSec 3
        if ($resp.status -in @("green", "yellow")) {
            $esReady = $true
            break
        }
    } catch { }
    Write-Host "  [$i] Elasticsearch not ready, retrying in 5s..." -ForegroundColor DarkGray
    Start-Sleep 5
}
if (-not $esReady) {
    Err "Elasticsearch timed out."
    exit 1
}
Ok "Elasticsearch is healthy at http://localhost:9200"

# ---------------------------------------------------------------
# Helper: run a notebook
# ---------------------------------------------------------------
function Run-Notebook {
    param(
        [string]$Name,
        [string]$InputNb,
        [string]$OutputNb,
        [int]$Timeout = 0
    )
    Info "Running $Name ..."
    $start = Get-Date
    if ($Timeout -gt 0) {
        python -m papermill $InputNb $OutputNb --no-progress-bar --execution-timeout $Timeout 2>&1 | Out-Host
    } else {
        python -m papermill $InputNb $OutputNb --no-progress-bar 2>&1 | Out-Host
    }
    $status = $LASTEXITCODE
    $elapsed = [math]::Round(((Get-Date) - $start).TotalSeconds)
    if ($status -eq 0) {
        Ok "$Name completed in ${elapsed}s"
    } else {
        Warn "$Name FAILED after ${elapsed}s - check $OutputNb"
    }
    # Return as script-level variable to avoid PS pipeline capture issue
    $script:LastNotebookStatus = $status
}

New-Item -ItemType Directory -Force -Path "output" | Out-Null
New-Item -ItemType Directory -Force -Path "models" | Out-Null
New-Item -ItemType Directory -Force -Path "data"   | Out-Null

# ---------------------------------------------------------------
# Phase 1: EDA + Model Training
# ---------------------------------------------------------------
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host " Phase 1: EDA and Model Training"          -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host ""

$p1 = @(
    @{ Name="01 EDA and Split";      In="01_eda_split.ipynb";         Out="output/01_eda_split_out.ipynb" },
    @{ Name="02 Naive Bayes";        In="02_model_naive_bayes.ipynb"; Out="output/02_model_naive_bayes_out.ipynb" },
    @{ Name="03 LSTM";               In="03_model_lstm.ipynb";        Out="output/03_model_lstm_out.ipynb" },
    @{ Name="04 DistilBERT";         In="04_model_distilbert.ipynb";  Out="output/04_model_distilbert_out.ipynb"; Timeout=300 },
    @{ Name="05 Model Comparison";   In="05_compare_models.ipynb";    Out="output/05_compare_models_out.ipynb" }
)

$failP1 = 0
foreach ($nb in $p1) {
    $script:LastNotebookStatus = 0
    if ($nb.Timeout) {
        Run-Notebook -Name $nb.Name -InputNb $nb.In -OutputNb $nb.Out -Timeout $nb.Timeout
    } else {
        Run-Notebook -Name $nb.Name -InputNb $nb.In -OutputNb $nb.Out
    }
    if ($script:LastNotebookStatus -ne 0) {
        $failP1 = $failP1 + 1
    }
}

if ($failP1 -gt 0) {
    Warn "$failP1 notebook(s) in Phase 1 had errors - pipeline will still attempt to run."
} else {
    Ok "All Phase 1 notebooks passed."
}

# ---------------------------------------------------------------
# Phase 2: Real-Time Pipeline
# ---------------------------------------------------------------
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host " Phase 2: Real-Time Pipeline"              -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host ""

Info "Starting Kafka Producer (notebook 06) in background..."

$pyExe = (Get-Command python).Source
$producerJob = Start-Job -ScriptBlock {
    param($dir, $pyExe)
    Set-Location $dir
    $env:TRANSFORMERS_NO_TF       = "1"
    $env:USE_TF                   = "0"
    $env:TF_USE_LEGACY_KERAS      = "1"
    $env:PYSPARK_PYTHON           = $pyExe
    $env:PYSPARK_DRIVER_PYTHON    = $pyExe
    Remove-Item Env:SPARK_HOME -ErrorAction SilentlyContinue
    python -m papermill 06_kafka_producer.ipynb output/06_kafka_producer_out.ipynb --no-progress-bar 2>&1
} -ArgumentList $ScriptDir, $pyExe

Ok "Producer running in background (Job ID: $($producerJob.Id))"
Info "Waiting 15s for producer to warm up..."
Start-Sleep 15

$script:LastNotebookStatus = 0
Run-Notebook -Name "07 Spark Streaming" `
    -InputNb  "07_spark_streaming.ipynb" `
    -OutputNb "output/07_spark_streaming_out.ipynb"
$rc7 = $script:LastNotebookStatus

Info "Waiting for Kafka Producer to finish..."
Wait-Job    $producerJob | Out-Null
Receive-Job $producerJob | Out-Null
Remove-Job  $producerJob
Ok "Producer job finished."

$script:LastNotebookStatus = 0
Run-Notebook -Name "08 Visualization" `
    -InputNb  "08_visualization.ipynb" `
    -OutputNb "output/08_visualization_out.ipynb"
$rc8 = $script:LastNotebookStatus

# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------
Write-Host ""
Write-Host "==========================================" -ForegroundColor Magenta
Write-Host " Run Summary"                              -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Magenta

Get-ChildItem -Path "output" -Filter "*_out.ipynb" | Sort-Object Name | ForEach-Object {
    Write-Host "  $($_.Name)" -ForegroundColor White
}

Write-Host ""
Ok "Kibana:        http://localhost:5601"
Ok "Elasticsearch: http://localhost:9200/grab_sentiment/_search?pretty"
Ok "Charts:        $ScriptDir\charts\"
Write-Host ""
Info "To stop services: docker compose down"
Info "To wipe data:     docker compose down -v"
