# Active Directory Enumeration Toolkit
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

function Get-KerberoastTargets {
    Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName |
    Select-Object Name, SamAccountName, ServicePrincipalName
}

function Get-ASREPRoastTargets {
    Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true} -Properties DoesNotRequirePreAuth |
    Select-Object Name, SamAccountName
}
