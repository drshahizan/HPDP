# Create hadoop directory if it doesn't exist
$hadoopHome = "C:\hadoop"
New-Item -ItemType Directory -Force -Path $hadoopHome

# Download winutils.exe
$winutilsUrl = "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.0/bin/winutils.exe"
$winutilsPath = Join-Path $hadoopHome "bin\winutils.exe"
New-Item -ItemType Directory -Force -Path (Split-Path $winutilsPath)
Invoke-WebRequest -Uri $winutilsUrl -OutFile $winutilsPath

# Download hadoop.dll
$hadoopDllUrl = "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.0/bin/hadoop.dll"
$hadoopDllPath = Join-Path $hadoopHome "bin\hadoop.dll"
Invoke-WebRequest -Uri $hadoopDllUrl -OutFile $hadoopDllPath

# Set HADOOP_HOME environment variable
[System.Environment]::SetEnvironmentVariable("HADOOP_HOME", $hadoopHome, [System.EnvironmentVariableTarget]::User)

Write-Host "Hadoop binaries have been downloaded and HADOOP_HOME has been set to $hadoopHome"
Write-Host "Please restart your terminal for the changes to take effect." 