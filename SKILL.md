---
name: cybersec-ops
description: >
  Comprehensive DevSecOps, SOC, and offensive security operations skill. 
  Use when the user mentions: security operations, SOC, threat hunting, incident response, 
  vulnerability assessment, penetration testing, red team, blue team, purple team, 
  DevSecOps, security automation, security scanning, SIEM, log analysis, forensics, 
  malware analysis, network security, cloud security, identity security, compliance scanning, 
  security hardening, security audit, or any offensive/defensive security scripting in 
  PowerShell or Python. Also triggers for security pipeline creation, security-as-code, 
  IaC security, container security, or Kubernetes security.

  This skill covers: PowerShell offensive scripting (recon, enumeration, exploitation 
  frameworks), Python security ecosystem (Scapy, Impacket, BloodHound, Volatility, 
  YARA, MISP, TheHive), DevSecOps pipelines (SAST/DAST/IaC scanning), SOC workflows 
  (SIEM queries, alert triage, playbooks), and hybrid automation combining both languages.

metadata:
  author: CyberSecOps Skill
  version: 1.0.0
  category: security-operations
  languages: [python, powershell, bash]
  domains: [devsecops, soc, offensive-security, defensive-security, cloud-security]
---

# CyberSec-Ops: The Unified DevSecOps & SOC Skill

## Overview

This skill enables comprehensive security operations across the full spectrum:
- **Offensive Security**: PowerShell-based reconnaissance, enumeration, and exploitation scripting
- **Defensive Security**: SOC workflows, SIEM queries, threat hunting, incident response
- **DevSecOps**: Security pipelines, SAST/DAST integration, IaC scanning, container security
- **Hybrid Automation**: Python + PowerShell interoperability for cross-platform security tooling

## Core Philosophy

Security operations require **language-agnostic thinking**. PowerShell dominates Windows/Active Directory environments. Python dominates Linux/cloud/tooling ecosystems. This skill treats them as complementary forces, not competitors.

## When to Use Which Language

| Scenario | Primary Language | Secondary |
|----------|-----------------|-----------|
| Active Directory / Windows domain | PowerShell | Python (for analysis) |
| Cloud-native (AWS/Azure/GCP) | Python | PowerShell (for Azure AD) |
| Network scanning / packet crafting | Python (Scapy) | PowerShell (for host enum) |
| Malware analysis / forensics | Python | PowerShell (for live response) |
| SIEM automation / SOAR | Python | PowerShell (for endpoint response) |
| Container/K8s security | Python | Bash |
| Compliance / audit scripts | PowerShell (Windows) | Python (cross-platform) |

## Progressive Disclosure Structure

- **SKILL.md** (this file): Core workflows, decision trees, and quick references
- `references/powershell-offensive.md`: PowerShell offensive scripting deep-dive
- `references/python-security-ecosystem.md`: Python security libraries and frameworks
- `references/devsecops-pipelines.md`: CI/CD security integration patterns
- `references/soc-workflows.md`: SOC analyst workflows and playbooks
- `references/hybrid-automation.md`: Python↔PowerShell interoperability patterns
- `scripts/`: Executable security utilities and templates

---

## Section 1: Security Assessment & Reconnaissance

### 1.1 Network Reconnaissance (Python-First)

**Decision**: Use Python when you need cross-platform network scanning, packet crafting, or service enumeration.

**Core Libraries**:
- `scapy` - Packet crafting and network scanning
- `python-nmap` - Nmap integration
- `socket` / `asyncio` - Custom port scanners
- `requests` / `httpx` - Web reconnaissance
- `dnspython` - DNS enumeration
- `shodan` / `censys` - External attack surface

**Workflow**:
1. Define scope (IP ranges, domains, ports)
2. Run passive reconnaissance (OSINT, certificate transparency)
3. Execute active scanning (port scan, service detection)
4. Parse and correlate results
5. Generate actionable report

**Example Pattern**:
```python
# Multi-threaded port scanner with service banner grabbing
import asyncio
import socket

async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), timeout=3
        )
        writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
        await writer.drain()
        banner = await asyncio.wait_for(reader.read(1024), timeout=2)
        writer.close()
        return {"port": port, "banner": banner.decode(errors="ignore").strip()}
    except:
        return None
```

### 1.2 Active Directory Reconnaissance (PowerShell-First)

**Decision**: Use PowerShell when operating in Windows/AD environments. Nothing beats native AD module integration.

**Core Modules**:
- `ActiveDirectory` - Native AD queries
- `PowerView` / `SharpView` - Offensive AD enumeration
- `BloodHound` - AD attack path analysis
- `RSAT` - Remote Server Administration Tools

**Workflow**:
1. Domain enumeration (users, groups, computers, trusts)
2. Permission analysis (ACLs, delegations, GPOs)
3. Attack path mapping (BloodHound ingestor)
4. Credential exposure assessment (Kerberoast, AS-REP Roast)

**Example Pattern**:
```powershell
# Domain enumeration with error handling and output formatting
function Get-DomainRecon {
    param([string]$Domain)

    $results = @{
        Users = Get-ADUser -Filter * -Properties LastLogonDate, PasswordLastSet
        Groups = Get-ADGroup -Filter * | Where-Object { $_.GroupCategory -eq "Security" }
        Computers = Get-ADComputer -Filter * -Properties OperatingSystem
        Trusts = Get-ADTrust -Filter *
        GPOs = Get-GPO -All | Select DisplayName, GpoStatus
    }

    $results | ConvertTo-Json -Depth 5 | Out-File "ad_recon_$Domain.json"
    return $results
}
```

### 1.3 Cloud Attack Surface (Python-First)

**Decision**: Use Python for cloud API enumeration. AWS Boto3, Azure SDK, GCP client libraries are Python-native.

**Core Libraries**:
- `boto3` / `botocore` - AWS enumeration
- `azure-identity` / `azure-mgmt-*` - Azure enumeration
- `google-cloud-*` - GCP enumeration
- `pacu` - AWS exploitation framework
- `cloudmapper` / `cartography` - Cloud visualization

---

## Section 2: Vulnerability Assessment & Exploitation

### 2.1 Automated Vulnerability Scanning

**Hybrid Approach**: Use Python for scanner orchestration, PowerShell for Windows-specific validation.

**Python Scanners**:
- `openvas` / `gvm-tools` - OpenVAS integration
- `nessrest` - Nessus API
- `nuclei` - Fast vulnerability scanner (Go-based, Python wrapper)
- `wapiti` - Web application scanner
- `sqlmap` - SQL injection automation

**PowerShell Validation**:
- Test specific Windows vulnerabilities (e.g., EternalBlue, PrintNightmare)
- Verify patch levels via WMI/CIM
- Check registry keys for known vulnerable configurations

### 2.2 Exploitation Frameworks

**Python Ecosystem**:
- `impacket` - SMB, MSRPC, LDAP protocol implementations
- `pwntools` - CTF/exploit development
- `routersploit` - IoT/embedded exploitation
- `beef` - Browser exploitation framework

**PowerShell Ecosystem**:
- `Empire` / `Starkiller` - Post-exploitation framework
- `PowerSploit` - PowerShell offensive modules
- `Nishang` - Offensive PowerShell for red teaming
- `Invoke-Obfuscation` - PowerShell obfuscation

**Critical Rule**: Only generate exploitation code for authorized penetration testing with proper scope documentation. Always include:
```
# AUTHORIZATION REQUIRED
# Scope: [defined scope]
# Authorized by: [entity]
# Date: [date]
# This code is for authorized security testing only
```

---

## Section 3: SOC & Defensive Operations

### 3.1 SIEM Query Development

**Decision**: Language depends on SIEM platform.

| SIEM | Query Language | Python Role |
|------|---------------|-------------|
| Splunk | SPL | API automation, alert management |
| Elastic | KQL/ES|QL | Data ingestion, ML anomaly detection |
| Sentinel | KQL | Azure SDK automation |
| QRadar | AQL | API automation |
| Chronicle | YARA-L | Python rule generation |
| Sigma | YAML | Python conversion to SIEM dialects |

**Sigma Rule Development** (Python-First):
```python
# Sigma rule generation and conversion
from sigma.rule import SigmaRule
from sigma.backends.splunk import SplunkBackend
from sigma.backends.elasticsearch import ElasticsearchBackend

# Convert Sigma to multiple SIEM formats
rule = SigmaRule.from_yaml("""
title: Suspicious PowerShell Download
logsource:
  product: windows
  service: powershell
detection:
  selection:
    EventID: 4104
    ScriptBlockText|contains:
      - 'Invoke-Expression'
      - 'IEX'
      - 'DownloadString'
  condition: selection
""")
```

### 3.2 Threat Hunting

**Python for Data Analysis**:
- `pandas` / `polars` - Log analysis at scale
- `jupyter` - Interactive hunting notebooks
- `yara-python` - Memory/file hunting
- `volatility3` - Memory forensics
- `msticpy` - Microsoft threat intelligence

**PowerShell for Live Response**:
- `Get-WinEvent` - Windows event log analysis
- `Get-Process` / `Get-WmiObject` - Process/memory inspection
- `Get-ChildItem` with hashing - File integrity monitoring
- `Invoke-WmiMethod` - Remote response

**Hunting Workflow**:
1. **Hypothesis**: Define what you're hunting for (e.g., "Living off the land" binaries)
2. **Data Collection**: Gather logs, memory dumps, network captures
3. **Analysis**: Use Python for statistical analysis, PowerShell for live endpoint data
4. **Pattern Detection**: IOC matching, behavioral analytics, anomaly detection
5. **Triage**: Validate findings, eliminate false positives
6. **Documentation**: Create detection rules, update threat intel

### 3.3 Incident Response Playbooks

**Python Automation**:
- Evidence collection and preservation
- Timeline analysis (`plaso` / `log2timeline`)
- IOC extraction and enrichment (MISP, VirusTotal, AbuseIPDB)
- Report generation

**PowerShell Response**:
- Isolate compromised hosts (firewall rules, network disable)
- Collect forensic artifacts (memory, disk, registry)
- Terminate malicious processes
- Disable compromised accounts

---

## Section 4: DevSecOps Pipeline Integration

### 4.1 Security Gates in CI/CD

**Pipeline Stages**:

```yaml
# Example GitLab CI security pipeline
stages:
  - secrets-scan
  - sast
  - dependency-check
  - container-scan
  - dast
  - iac-scan
  - compliance

secrets-scan:
  stage: secrets-scan
  script:
    - trufflehog filesystem . --json
  artifacts:
    reports:
      sast: secrets-report.json

sast:
  stage: sast
  script:
    - bandit -r . -f json -o bandit-report.json  # Python
    - semgrep --config=auto --json --output=semgrep-report.json
  artifacts:
    reports:
      sast: semgrep-report.json

dependency-check:
  stage: dependency-check
  script:
    - safety check --json --output safety-report.json  # Python
    - pip-audit --format=json --output=pip-audit-report.json
  artifacts:
    reports:
      dependency_scanning: safety-report.json

container-scan:
  stage: container-scan
  script:
    - trivy image --format json --output trivy-report.json $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  artifacts:
    reports:
      container_scanning: trivy-report.json

iac-scan:
  stage: iac-scan
  script:
    - checkov -d . --output json --output-file checkov-report.json
    - tfsec . --format json --out tfsec-report.json
  artifacts:
    reports:
      sast: checkov-report.json
```

### 4.2 Python Security Tooling for DevSecOps

**SAST (Static Analysis)**:
- `bandit` - Python security linter
- `semgrep` - Multi-language pattern matching
- `pylint-security` - Security-focused pylint extensions
- `safety` / `pip-audit` - Dependency vulnerability scanning

**DAST (Dynamic Analysis)**:
- `zap-api-scan` - OWASP ZAP automation
- `burp-suite-enterprise` - Burp automation
- `wapiti` - Web app vulnerability scanner

**Container Security**:
- `trivy` - Container image vulnerability scanner
- `grype` - Container vulnerability scanner (Python wrapper)
- `docker-bench-security` - CIS Docker benchmark
- `kube-bench` / `kube-hunter` - Kubernetes security

**IaC Security**:
- `checkov` - Multi-framework IaC scanner
- `tfsec` - Terraform security scanner
- `cfn-lint` / `cfn-nag` - CloudFormation security
- `ansible-lint` - Ansible security

### 4.3 PowerShell for Windows DevSecOps

**Windows-Specific Security**:
- `Pester` - Security testing framework for PowerShell
- `SecurityPolicyDSC` - Desired State Configuration for security baselines
- `AuditPolicyDSC` - Audit policy management
- `WindowsDefender` - Defender configuration and scanning

**Example: Security Baseline Validation**:
```powershell
# Validate CIS Windows 10/11 benchmarks
$benchmarks = @{
    "PasswordPolicy" = {
        $policy = Get-ADDefaultDomainPasswordPolicy
        $policy.MinPasswordLength -ge 14
    }
    "AuditPolicy" = {
        $audit = Get-AuditPolicy -SubCategory "Logon"
        $audit.Setting -eq "Success and Failure"
    }
    "FirewallEnabled" = {
        (Get-NetFirewallProfile -Profile Domain).Enabled -eq "True"
    }
}

$results = foreach ($benchmark in $benchmarks.GetEnumerator()) {
    [PSCustomObject]@{
        Benchmark = $benchmark.Key
        Compliant = & $benchmark.Value
        Severity = "High"
    }
}

$results | Export-Csv -Path "security_baseline.csv" -NoTypeInformation
```

---

## Section 5: Hybrid Python ↔ PowerShell Automation

### 5.1 Interoperability Patterns

**Pattern A: Python Orchestrates PowerShell**:
```python
import subprocess
import json

# Run PowerShell from Python, parse JSON output
result = subprocess.run(
    ["powershell", "-Command", 
     "Get-Process | Select-Object Name, Id | ConvertTo-Json"],
    capture_output=True, text=True
)
processes = json.loads(result.stdout)
# Analyze in Python ecosystem
```

**Pattern B: PowerShell Calls Python**:
```powershell
# Run Python analysis from PowerShell
$pythonScript = @"
import json
import sys
from datetime import datetime

data = json.load(sys.stdin)
# Process data
result = {"analyzed": len(data), "timestamp": datetime.now().isoformat()}
print(json.dumps(result))
"@

$jsonData | python -c $pythonScript | ConvertFrom-Json
```

**Pattern C: REST API Bridge**:
- Python FastAPI/Flask backend exposing security endpoints
- PowerShell `Invoke-RestMethod` consuming the API
- Enables microservices architecture for security tools

### 5.2 Cross-Platform Security Scripts

**Universal Reconnaissance**:
```python
#!/usr/bin/env python3
"""Cross-platform host reconnaissance"""
import platform
import subprocess
import json
import sys

def windows_recon():
    """PowerShell-based Windows reconnaissance"""
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
    """Native Linux reconnaissance"""
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

    # Save for analysis
    with open(f"recon_{os_type.lower()}.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
```

---

## Section 6: Forensics & Malware Analysis

### 6.1 Memory Forensics

**Python-First** (Volatility3):
```python
import volatility3.framework.plugins.linux.pslist
import volatility3.framework.plugins.windows.pslist
from volatility3.framework import contexts

# Analyze memory dump for malicious processes
context = contexts.Context()
context.config["automagic.LayerStacker.single_location"] = "file:///path/to/memory.dmp"

# Windows process list
plugin = volatility3.framework.plugins.windows.pslist.PsList(context)
for process in plugin.run():
    print(f"PID: {process.UniqueProcessId}, Name: {process.ImageFileName}")
```

**PowerShell Live Memory**:
```powershell
# Dump process memory for analysis
$process = Get-Process -Name "suspicious_process"
$dumpPath = "C:\forensics\process_dump.dmp"

# Using Windows Error Reporting or DebugDiag
# Alternative: MiniDumpWriteDump via P/Invoke
```

### 6.2 File Analysis

**Python**:
- `pefile` - PE file analysis
- `python-magic` - File type identification
- `yara-python` - YARA rule matching
- `capstone` / `keystone` - Disassembly framework
- `uncompyle6` / `decompyle3` - Python bytecode decompilation

**PowerShell**:
- `Get-FileHash` - Hash verification
- `Get-AuthenticodeSignature` - Signature validation
- `Get-ItemProperty` - Metadata extraction
- `Select-String` - String searching in files

### 6.3 Network Forensics

**Python**:
- `scapy` - Packet capture and analysis
- `pyshark` - Wireshark integration
- `dpkt` - Packet parsing
- `flowcontainer` - NetFlow analysis

---

## Section 7: Threat Intelligence & Automation

### 7.1 IOC Management

**Python Ecosystem**:
- `pymisp` - MISP (Malware Information Sharing Platform)
- `thehive4py` - TheHive case management
- `cortex4py` - Cortex analyzers
- `stix2` / `taxii2-client` - STIX/TAXII threat intel
- `vt-py` - VirusTotal API
- `greynoise` - Internet noise filtering

### 7.2 SOAR Automation

**Python for SOAR Platforms**:
- `demisto-py` / `pan-devops` - Palo Alto XSOAR
- `splunk-sdk` - Splunk Phantom
- `swimlane-py` - Swimlane
- Custom webhooks and API integrations

**PowerShell for Endpoint Response**:
- Isolate hosts via firewall
- Collect forensic artifacts
- Execute remediation scripts
- Query/update Active Directory

---

## Section 8: Compliance & Governance

### 8.1 Security Benchmarks

**CIS Benchmarks**:
- Python: `cis-compliance` scanners for cloud
- PowerShell: `CIS-Benchmark-PowerShell` for Windows
- Both: Custom audit scripts

**NIST / ISO / SOC2**:
- Python: `compliance-as-code` frameworks
- PowerShell: `SecurityPolicyDSC` for Windows hardening

### 8.2 Audit Automation

**Python**:
```python
# Cloud compliance scanner
import boto3
from botocore.exceptions import ClientError

def check_s3_encryption():
    s3 = boto3.client('s3')
    violations = []
    for bucket in s3.list_buckets()['Buckets']:
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket['Name'])
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                violations.append({
                    'resource': bucket['Name'],
                    'control': 'S3 encryption at rest',
                    'severity': 'HIGH',
                    'remediation': 'Enable default encryption'
                })
    return violations
```

**PowerShell**:
```powershell
# Windows compliance audit
function Test-ComplianceControl {
    param(
        [string]$ControlName,
        [scriptblock]$TestScript,
        [string]$Severity = "Medium"
    )

    try {
        $result = & $TestScript
        return [PSCustomObject]@{
            Control = $ControlName
            Compliant = $result
            Severity = $Severity
            Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    }
    catch {
        return [PSCustomObject]@{
            Control = $ControlName
            Compliant = $false
            Severity = $Severity
            Error = $_.Exception.Message
            Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    }
}
```

---

## Section 9: Cloud Security

### 9.1 AWS Security (Python-First)

**Core Tools**:
- ` ScoutSuite` - AWS security audit
- `Prowler` - AWS CIS benchmark tool
- `CloudSploit` / `Aqua CloudSploit` - AWS security scanning
- `pacu` - AWS exploitation framework
- `cloudmapper` - AWS network visualization

### 9.2 Azure Security (PowerShell + Python)

**PowerShell**:
- `Az.Security` - Azure Security Center
- `Az.Monitor` - Azure Monitor and Log Analytics
- `AzureAD` / `Microsoft.Graph` - Identity security

**Python**:
- `azure-identity` / `azure-mgmt-security` - Azure SDK
- `microsoft-defender-atp` - Defender for Endpoint API

### 9.3 GCP Security (Python-First)

- `google-cloud-securitycenter` - Security Command Center
- `forseti-security` - GCP security toolkit
- `prowler` (GCP module) - Multi-cloud security

---

## Section 10: Container & Kubernetes Security

### 10.1 Container Security

**Python Tools**:
- `docker-py` - Docker API for security scanning
- `trivy` - Container vulnerability scanner
- `syft` / `grype` - SBOM generation and vulnerability scanning
- `clair` - Container vulnerability analysis

**PowerShell** (Windows Containers):
- `Docker PowerShell` module
- `Get-Container` - Container inspection
- Windows-specific container hardening

### 10.2 Kubernetes Security

**Python**:
- `kubernetes` client - K8s API security queries
- `kube-hunter` - K8s penetration testing
- `kube-bench` - CIS K8s benchmark
- `kyverno` / `OPA` - Policy as code

**PowerShell**:
- `kubectl` via PowerShell
- `AKS` module for Azure Kubernetes security

---

## Section 11: Security Reporting & Visualization

### 11.1 Report Generation

**Python**:
- `jinja2` - Template-based report generation
- `markdown` / `pdfkit` - Multi-format output
- `plotly` / `matplotlib` - Data visualization
- `pandas` - Data aggregation and analysis

**PowerShell**:
- `Export-Excel` - Excel report generation
- `ConvertTo-Html` - HTML reports
- `Out-GridView` - Interactive GUI (Windows)

### 11.2 Dashboards

**Python**:
- `streamlit` / `dash` - Interactive security dashboards
- `grafana-api` - Grafana dashboard automation
- `splunk-sdk` - Splunk dashboard creation

---

## Section 12: Advanced Topics

### 12.1 Purple Team Automation

**Concept**: Automate the feedback loop between red team (attack) and blue team (defense).

**Python**:
- Attack simulation frameworks (Caldera, Atomic Red Team)
- Detection rule validation
- MITRE ATT&CK mapping

**PowerShell**:
- Atomic Red Team execution (PowerShell-based tests)
- Windows-specific attack simulation
- Detection validation via event logs

### 12.2 Adversary Simulation

**Python**:
- `caldera` - Automated adversary emulation
- `atomic-red-team` - MITRE ATT&CK tests
- `prelude` - Continuous security testing

**PowerShell**:
- `Invoke-AtomicTest` - Execute atomic tests
- `Empire` modules - Advanced persistent threat simulation

### 12.3 Machine Learning for Security

**Python**:
- `scikit-learn` / `tensorflow` - Anomaly detection
- `pytorch` - Deep learning for security
- `isolation-forest` - Outlier detection
- `lstm` - Sequence analysis for behavioral detection

---

## Gotchas & Critical Considerations

### PowerShell Gotchas
- **Execution Policy**: `Set-ExecutionPolicy` is not a security boundary. Use code signing or constrained language mode.
- **AMSI**: Windows Defender AMSI scans PowerShell scripts. Use legitimate testing frameworks, not evasion.
- **Logging**: PowerShell 5.1+ has extensive logging (Script Block Logging, Module Logging, Transcription). Assume all actions are logged.
- **Constrained Language Mode**: In CLM, many .NET types are unavailable. Use approved modules only.
- **PowerShell 7 vs 5.1**: PowerShell 7 is cross-platform but lacks some Windows-specific modules. Use 5.1 for AD operations, 7 for cross-platform scripts.

### Python Gotchas
- **Dependency Confusion**: Always pin versions in `requirements.txt`. Use `pip-audit` or `safety` to check for vulnerabilities.
- **Pickle Deserialization**: Never unpickle untrusted data. Use `json` or `msgpack` instead.
- **Subprocess Injection**: Always sanitize inputs to `subprocess.run()`. Use list arguments, not shell=True with user input.
- **SSL Verification**: Never disable SSL verification (`verify=False`) in production. Use proper certificate chains.
- **Cryptography**: Use `cryptography` library, not `pycrypto` (deprecated). Use `secrets` module for token generation, not `random`.

### Cross-Platform Gotchas
- **Path Separators**: Use `pathlib.Path` in Python, `Join-Path` in PowerShell. Never hardcode `\` or `/`.
- **Encoding**: Windows uses UTF-16-LE for PowerShell output. Python `subprocess` may need `encoding='utf-8'` or `errors='ignore'`.
- **Line Endings**: Use `.gitattributes` to enforce LF. PowerShell scripts with CRLF may fail on Linux.
- **Case Sensitivity**: Windows is case-insensitive. Linux is case-sensitive. Always use exact case in scripts.

### Security Ethics
- **Authorization**: Only run offensive tools against systems you own or have explicit written authorization to test.
- **Scope**: Respect defined scope. No lateral movement beyond authorized targets.
- **Data Handling**: Encrypt sensitive findings. Use secure channels for report delivery.
- **Responsible Disclosure**: Report vulnerabilities through proper channels. Never exploit for personal gain.

---

## Quick Reference: Tool Selection Matrix

| Task | Recommended Tool | Language | Notes |
|------|-----------------|----------|-------|
| Network scanning | Nmap + Python wrapper | Python | Use python-nmap for automation |
| AD enumeration | PowerView / SharpView | PowerShell | BloodHound for visualization |
| Web app scanning | Burp Suite / ZAP | Python (API) | Use official APIs |
| Memory forensics | Volatility3 | Python | Cross-platform |
| SIEM query dev | Sigma | Python (conversion) | Convert to target SIEM |
| Container scanning | Trivy | Python (wrapper) | Also supports SBOM |
| IaC scanning | Checkov | Python | Multi-cloud support |
| Cloud enumeration | ScoutSuite / Prowler | Python | AWS/Azure/GCP |
| Malware analysis | YARA + Python | Python | Use yara-python bindings |
| Threat intel | MISP + TheHive | Python | REST API clients |
| Incident response | Velociraptor | PowerShell/Python | Agent-based |
| Compliance audit | CIS-CAT / Prowler | Python | Benchmark automation |
| Password audit | Hashcat + Python | Python (automation) | Use official APIs |
| Log analysis | Jupyter + Pandas | Python | Interactive notebooks |
| Endpoint hardening | PowerShell DSC | PowerShell | Windows-native |
| K8s security | kube-bench / kube-hunter | Python | CIS benchmarks |
| Secret scanning | TruffleHog / GitLeaks | Python | CI/CD integration |
| SAST | Semgrep / Bandit | Python | Multi-language support |
| DAST | OWASP ZAP | Python (API) | Automation framework |
| SOAR | XSOAR / Phantom | Python | Custom integrations |

---

## Reference Files

Load these on-demand based on the specific task:

- `references/powershell-offensive.md` - Deep-dive into PowerShell offensive scripting, Empire modules, AMSI bypass (for authorized testing), obfuscation techniques, and Windows-specific attack vectors.
- `references/python-security-ecosystem.md` - Comprehensive Python security library guide: Impacket, Scapy, Volatility, YARA, MISP, TheHive, and custom framework development.
- `references/devsecops-pipelines.md` - CI/CD security integration patterns, tool configurations, and pipeline-as-code examples for GitLab CI, GitHub Actions, Azure DevOps, and Jenkins.
- `references/soc-workflows.md` - SOC analyst workflows: alert triage, threat hunting playbooks, incident response procedures, and SIEM query patterns for Splunk, Elastic, Sentinel, and QRadar.
- `references/hybrid-automation.md` - Python↔PowerShell interoperability: subprocess patterns, REST API bridges, data serialization, and cross-platform security script architecture.
- `references/cloud-security.md` - AWS, Azure, and GCP security tooling, enumeration techniques, and compliance scanning.
- `references/forensics-malware.md` - Memory forensics, disk forensics, malware analysis techniques, and artifact extraction.

---

## Scripts Directory

The `scripts/` directory contains executable utilities:

- `recon-universal.py` - Cross-platform host reconnaissance
- `ad-enum.ps1` - Active Directory enumeration toolkit
- `vuln-scan-orchestrator.py` - Multi-scanner orchestration
- `sigma-converter.py` - Sigma rule format conversion
- `ioc-enricher.py` - Threat intelligence enrichment
- `compliance-audit.py` - Multi-framework compliance scanner
- `incident-response.ps1` - Windows incident response automation
- `security-report-generator.py` - Automated report generation

---

## Skill Usage Checklist

When approaching a security task:

- [ ] Identify the target environment (Windows/Linux/Cloud/Container)
- [ ] Determine offensive vs defensive vs DevSecOps context
- [ ] Select primary language based on environment
- [ ] Load relevant reference file for deep-dive guidance
- [ ] Verify authorization and scope before offensive operations
- [ ] Use appropriate tool from the selection matrix
- [ ] Document findings in standardized format
- [ ] Generate actionable remediation guidance
- [ ] Follow responsible disclosure practices
