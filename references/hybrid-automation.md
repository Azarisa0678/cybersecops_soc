# Hybrid Python-PowerShell Automation

## Pattern A: Python Orchestrates PowerShell
```python
import subprocess
import json

result = subprocess.run(
    ["powershell", "-Command", 
     "Get-Process | Select-Object Name, Id | ConvertTo-Json"],
    capture_output=True, text=True
)
processes = json.loads(result.stdout)
```

## Pattern B: PowerShell Calls Python
```powershell
$pythonScript = @"
import json
import sys
from datetime import datetime

data = json.load(sys.stdin)
result = {"analyzed": len(data), "timestamp": datetime.now().isoformat()}
print(json.dumps(result))
"@

$jsonData | python -c $pythonScript | ConvertFrom-Json
```

## Pattern C: REST API Bridge
- Python FastAPI/Flask backend exposing security endpoints
- PowerShell Invoke-RestMethod consuming the API
- Enables microservices architecture for security tools

## Cross-Platform Reconnaissance
```python
#!/usr/bin/env python3
import platform
import subprocess
import json

def windows_recon():
    ps_commands = {
        "system_info": "Get-ComputerInfo | Select WindowsVersion, TotalPhysicalMemory",
        "users": "Get-LocalUser | Select Name, Enabled",
        "services": "Get-Service | Where Status -eq 'Running'",
        "network": "Get-NetTCPConnection | Select LocalAddress, LocalPort"
    }
    results = {}
    for key, cmd in ps_commands.items():
        result = subprocess.run(
            ["powershell", "-Command", cmd + " | ConvertTo-Json"],
            capture_output=True, text=True
        )
        results[key] = json.loads(result.stdout) if result.returncode == 0 else None
    return results

def linux_recon():
    commands = {
        "system_info": "uname -a && cat /etc/os-release",
        "users": "cat /etc/passwd | cut -d: -f1",
        "services": "systemctl list-units --type=service --state=running",
        "network": "ss -tuln"
    }
    results = {}
    for key, cmd in commands.items():
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        results[key] = result.stdout.split("\n") if result.returncode == 0 else None
    return results
```

## Data Serialization Best Practices
- PowerShell to Python: ConvertTo-Json -> json.loads()
- Python to PowerShell: json.dumps() -> ConvertFrom-Json
- Encoding: Windows uses UTF-16-LE; Python may need encoding='utf-8'
