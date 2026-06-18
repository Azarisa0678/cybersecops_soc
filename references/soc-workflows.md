# SOC Workflows & Playbooks

## Alert Triage Workflow
1. **Initial Assessment**: Severity, asset criticality, alert source
2. **Context Enrichment**: IP reputation, user context, asset details
3. **Correlation**: Related alerts, historical patterns
4. **Validation**: False positive check, known good behavior
5. **Escalation**: Incident creation, stakeholder notification

## SIEM Query Patterns

### Splunk SPL
```spl
# Failed login attempts
index=windows EventCode=4625 
| stats count by Account_Name, src_ip 
| where count > 5

# PowerShell execution
index=windows EventCode=4104 
| search ScriptBlockText="*Invoke-Expression*"

# Network connections
index=network 
| stats count by src_ip, dest_ip, dest_port 
| where count > 100
```

### Elastic KQL
```kql
# Suspicious process execution
event.code:4688 AND process.name:(cmd.exe OR powershell.exe)

# Network connections
event.category:network AND destination.port:(445 OR 3389)

# Failed authentication
event.category:authentication AND event.outcome:failure
```

### Azure Sentinel KQL
```kql
# Sign-in anomalies
SigninLogs
| where ResultType != 0
| summarize count() by IPAddress, UserPrincipalName
| where count_ > 5

# PowerShell downloads
DeviceEvents
| where ActionType == "PowerShellCommand"
| where AdditionalFields contains "DownloadString"
```

## Threat Hunting Playbooks
1. **Living Off The Land**: PowerShell, WMI, certutil abuse
2. **Lateral Movement**: RDP, SMB, WinRM anomalies
3. **Data Exfiltration**: Large transfers, DNS tunneling, cloud uploads
4. **Persistence**: Scheduled tasks, registry run keys, WMI events

## Incident Response
1. **Containment**: Isolate host, disable account, block IP
2. **Eradication**: Kill processes, remove malware, patch vulnerability
3. **Recovery**: Restore from backup, re-enable services
4. **Lessons Learned**: Update detection rules, improve controls
