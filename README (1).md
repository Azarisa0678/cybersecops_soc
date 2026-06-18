# CyberSec-Ops Skill

A comprehensive DevSecOps, SOC, and offensive/defensive security skill for AI agents. Combines PowerShell offensive scripting with the Python security ecosystem into a unified skill system.

## Overview

This skill covers the full spectrum of cybersecurity operations:

- **Offensive Security**: PowerShell-based reconnaissance, enumeration, and exploitation
- **Defensive Security**: SOC workflows, SIEM queries, threat hunting, incident response
- **DevSecOps**: Security pipelines, SAST/DAST integration, IaC scanning, container security
- **Hybrid Automation**: Python + PowerShell interoperability for cross-platform tooling

## Supported Platforms

| Platform | Status | Installation |
|----------|--------|-------------|
| **Kimi** (Agent Mode / Claw) | ✅ Fully compatible | `/skill-creator` or Document Upload |
| **Claude Code** | ✅ Compatible | `~/.claude/skills/` |
| **OpenAI Codex CLI** | ✅ Compatible | `.codex/skills/` |
| **Cursor** | ✅ Compatible | `.cursor/skills/` |
| **Gemini CLI** | ✅ Compatible | `.gemini/skills/` |
| **Kilo Code** | ✅ Compatible | `.kilo/skills/` |

## Installation

### Kimi (Recommended)

**Method 1: Via `/skill-creator`**
1. Open Kimi Agent Mode
2. Type `/skill-creator`
3. Upload the `SKILL.md` file or describe: "Install the CyberSec-Ops skill for DevSecOps and cybersecurity operations"

**Method 2: Document Upload**
1. Go to Skills Panel → "Office Document to Skill"
2. Upload `SKILL.md`
3. Add description: "Cybersecurity operations covering DevSecOps, SOC, offensive/defensive security"
4. Click Create Skill

**Method 3: Kimi Claw (Desktop)**
1. Open Kimi Claw
2. Navigate to Skills → Clawhub Skill Library
3. Sync with Kimi Agent (skills auto-sync between web and desktop)

### Claude Code / Codex CLI / Cursor

```bash
# Clone to skills directory
git clone https://github.com/YOUR_USERNAME/cybersec-ops-skill.git

# For Claude Code
cp -r cybersec-ops-skill/cybersec-ops ~/.claude/skills/

# For Codex CLI
cp -r cybersec-ops-skill/cybersec-ops ~/.codex/skills/

# For Cursor
cp -r cybersec-ops-skill/cybersec-ops ~/.cursor/skills/
```

### Open-Source Marketplaces

| Marketplace | URL | Command |
|-------------|-----|---------|
| SkillsMP | https://skillsmp.com | Upload ZIP or link GitHub repo |
| SkillsLLM | https://skillsllm.com | Browse and install |
| LobeHub | https://lobehub.com/skills | Upload SKILL.md package |

## Skill Structure

```
cybersec-ops/
├── SKILL.md                          # Main skill definition (29 KB)
│   ├── 12 major sections
│   ├── Language selection matrix
│   ├── Tool selection matrix
│   ├── Security ethics guidelines
│   └── Progressive disclosure structure
├── references/
│   ├── powershell-offensive.md       # PowerShell offensive deep-dive (15 KB)
│   ├── python-security-ecosystem.md  # Python security libraries (16 KB)
│   ├── devsecops-pipelines.md        # CI/CD security integration (3 KB)
│   ├── soc-workflows.md              # SOC analyst playbooks (2 KB)
│   ├── hybrid-automation.md          # Python-PowerShell bridge (2 KB)
│   ├── cloud-security.md             # AWS/Azure/GCP security (1 KB)
│   └── forensics-malware.md          # Memory forensics & malware (1 KB)
└── scripts/
    ├── recon-universal.py            # Cross-platform host recon
    ├── ad-enum.ps1                   # Active Directory enumeration
    ├── vuln-scan-orchestrator.py     # Multi-scanner orchestration
    ├── sigma-converter.py            # Sigma rule conversion
    ├── ioc-enricher.py               # Threat intel enrichment
    ├── compliance-audit.py           # Compliance framework scanner
    ├── incident-response.ps1         # Windows IR automation
    └── security-report-generator.py  # Automated report generation
```

## Trigger Words

The skill automatically activates when you mention:

- Security operations, SOC, threat hunting, incident response
- Vulnerability assessment, penetration testing, red team, blue team, purple team
- DevSecOps, security automation, security scanning, SIEM, log analysis
- Forensics, malware analysis, network security, cloud security
- Identity security, compliance scanning, security hardening, security audit
- PowerShell offensive scripting, Python security tools
- Container security, Kubernetes security, IaC security

## Test Prompts

Try these to verify the skill works:

1. *"Scan my AWS infrastructure for security misconfigurations"*
2. *"Write a PowerShell script to enumerate Active Directory users"*
3. *"Create a Python tool for network reconnaissance with Scapy"*
4. *"Build a DevSecOps pipeline with SAST and container scanning"*
5. *"How do I detect anomalous login patterns in my SIEM?"*
6. *"Analyze a memory dump for malware indicators"*
7. *"Convert this Sigma rule to Splunk SPL and Elastic KQL"*
8. *"Write a compliance audit script for CIS benchmarks"*

## Language Selection Matrix

| Scenario | Primary | Secondary |
|----------|---------|-----------|
| Active Directory / Windows domain | PowerShell | Python (analysis) |
| Cloud-native (AWS/Azure/GCP) | Python | PowerShell (Azure AD) |
| Network scanning / packet crafting | Python (Scapy) | PowerShell (host enum) |
| Malware analysis / forensics | Python | PowerShell (live response) |
| SIEM automation / SOAR | Python | PowerShell (endpoint) |
| Container/K8s security | Python | Bash |
| Compliance / audit scripts | PowerShell (Windows) | Python (cross-platform) |

## Security Ethics

**IMPORTANT**: This skill contains offensive security techniques for authorized testing only. All code examples include:

- Authorization requirements
- Scope documentation
- Responsible disclosure guidelines

**Never use offensive techniques without explicit written authorization.**

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License - See LICENSE file

## Author

Created for the AI security community. Compatible with all major AI agent platforms supporting the Agent Skills Specification.
