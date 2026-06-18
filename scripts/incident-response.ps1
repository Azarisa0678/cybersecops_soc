# Windows Incident Response Automation
function Start-IncidentResponse {
    param([string]$TargetHost)

    $artifacts = @{
        Processes = Get-Process | Select Name, Id, Path
        Services = Get-Service | Where {$_.Status -eq "Running"}
        Network = Get-NetTCPConnection | Select LocalAddress, LocalPort, RemoteAddress, State
        Users = Get-LocalUser | Select Name, Enabled, LastLogon
    }

    $isolate = Read-Host "Isolate host $TargetHost? (y/n)"
    if ($isolate -eq "y") {
        Get-NetAdapter | Disable-NetAdapter -Confirm:$false
        New-NetFirewallRule -DisplayName "IR-Block-Inbound" -Direction Inbound -Action Block
    }

    $artifacts | ConvertTo-Json -Depth 5 | Out-File "ir_artifacts_$TargetHost.json"
    return $artifacts
}

function Get-MemoryDump {
    param([string]$ProcessName)
    $proc = Get-Process -Name $ProcessName
    & procdump.exe -ma $proc.Id "$ProcessName.dmp"
}
