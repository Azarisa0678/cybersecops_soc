#!/usr/bin/env python3
"""Cross-platform host reconnaissance"""
import platform
import subprocess
import json
import sys

def windows_recon():
    ps_commands = {
        "system_info": "Get-ComputerInfo | Select WindowsVersion, TotalPhysicalMemory, CsProcessors",
        "users": "Get-LocalUser | Select Name, Enabled, LastLogon",
        "services": "Get-Service | Where-Object {$_.Status -eq 'Running'} | Select Name, DisplayName",
        "network": "Get-NetTCPConnection | Select LocalAddress, LocalPort, RemoteAddress, State"
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

def main():
    os_type = platform.system()
    if os_type == "Windows":
        data = windows_recon()
    else:
        data = linux_recon()
    print(json.dumps(data, indent=2))
    with open(f"recon_{os_type.lower()}.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
