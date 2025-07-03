import os
import requests
import shutil
from pathlib import Path

def download_file(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

def setup_hadoop():
    hadoop_home = Path("C:/hadoop")
    bin_dir = hadoop_home / "bin"
    
    # Create directories
    bin_dir.mkdir(parents=True, exist_ok=True)
    
    # Download files
    files = {
        "winutils.exe": "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.0/bin/winutils.exe",
        "hadoop.dll": "https://github.com/cdarlint/winutils/raw/master/hadoop-3.2.0/bin/hadoop.dll"
    }
    
    for filename, url in files.items():
        destination = bin_dir / filename
        if not destination.exists():
            print(f"Downloading {filename}...")
            download_file(url, destination)
            print(f"Downloaded {filename}")

if __name__ == "__main__":
    # Setup Hadoop
    setup_hadoop()
    
    # Print instructions
    print("\nSetup completed!")
    print("\nPlease ensure you have:")
    print("1. Java 11 installed (required for Spark 3.2.0)")
    print("2. JAVA_HOME environment variable set")
    print("3. Added C:\\hadoop\\bin to your PATH")
    print("\nYou can download Java 11 from: https://adoptium.net/temurin/releases/?version=11") 