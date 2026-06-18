[README.md](https://github.com/user-attachments/files/29092140/README.md)
# 🔐 CyberSec-Ops Skill

> A comprehensive DevSecOps, SOC, and offensive/defensive security skill for AI agents. Unifies PowerShell offensive scripting with the Python security ecosystem into a single, coherent skill system.

[![Compatible](https://img.shields.io/badge/Kimi-✓_Agent_Mode-blue)](https://kimi.com)
[![Compatible](https://img.shields.io/badge/Claude_Code-✓_Compatible-green)](https://claude.ai/code)
[![Compatible](https://img.shields.io/badge/Codex_CLI-✓_Compatible-orange)](https://openai.com/codex)
[![Compatible](https://img.shields.io/badge/Cursor-✓_Compatible-purple)](https://cursor.com)
[![Spec](https://img.shields.io/badge/Agent_Skills_Spec-v1.0-red)](https://skillsmp.com)

---

## 📋 Overview

Security operations demand **language-agnostic thinking**. PowerShell dominates Windows/Active Directory environments. Python dominates Linux/cloud/tooling ecosystems. This skill treats them as **complementary forces**, not competitors.

| Domain | PowerShell | Python | Hybrid |
|--------|-----------|--------|--------|
| Active Directory Enumeration | ✅ Native | ⚠️ Via LDAP | ✅ PS enum + Python analysis |
| Network Scanning | ⚠️ Limited | ✅ Scapy/Nmap | ✅ Python scanner + PS validation |
| Cloud Security | ✅ Azure | ✅ AWS/GCP | ✅ Cross-cloud unified scanner |
| SIEM Integration | ⚠️ Limited | ✅ Full SDKs | ✅ Python SOAR + PS endpoint response |
| Malware Analysis | ⚠️ Live response | ✅ Full forensics | ✅ PS collection + Python analysis |
| DevSecOps Pipelines | ✅ Windows CI/CD | ✅ Linux/cloud CI/CD | ✅ Cross-platform pipelines |

---

## 📦 What's Inside

### SKILL.md (29.5 KB) — The Core

The main skill file with **12 comprehensive sections**:

1. **Security Assessment & Reconnaissance** — Network, AD, and cloud attack surface
2. **Vulnerability Assessment & Exploitation** — Automated scanning, exploitation frameworks
3. **SOC & Defensive Operations** — SIEM queries, threat hunting, incident response
4. **DevSecOps Pipeline Integration** — CI/CD security gates, SAST/DAST/IaC scanning
5. **Hybrid Python↔PowerShell Automation** — Interoperability patterns, cross-platform scripts
6. **Forensics & Malware Analysis** — Memory forensics, PE analysis, YARA matching
7. **Threat Intelligence & Automation** — MISP, VirusTotal, AbuseIPDB, SOAR platforms
8. **Compliance & Governance** — CIS benchmarks, NIST/ISO/SOC2 audit automation
9. **Cloud Security** — AWS (Boto3), Azure (SDK), GCP (google-cloud) scanners
10. **Container & Kubernetes Security** — Docker, K8s RBAC, network policies
11. **Security Reporting & Visualization** — Automated report generation, dashboards
12. **Advanced Topics** — Purple team automation, adversary simulation, ML for security

Plus:
- **Language Selection Matrix** — When to use PowerShell vs Python
- **Tool Selection Matrix** — 20+ security tools mapped to use cases
- **Security Ethics Guidelines** — Authorization requirements for all offensive content
- **Gotchas & Critical Considerations** — Platform-specific pitfalls

### References (40.8 KB total)

| File | Size | Content |
|------|------|---------|
| `powershell-offensive.md` | 14.7 KB | PowerView, Kerberoasting, AS-REP, ACL abuse, BloodHound, lateral movement, persistence, defense evasion, obfuscation |
| `python-security-ecosystem.md` | 16.1 KB | Scapy, Impacket, Volatility3, YARA, pefile, MISP, VirusTotal, Splunk, Elastic, TheHive, AWS/Azure/GCP SDKs, Docker, Kubernetes, sklearn, PyTorch |
| `devsecops-pipelines.md` | 3.1 KB | GitLab CI, GitHub Actions, Bandit, Semgrep, Trivy, Checkov, tfsec |
| `soc-workflows.md` | 1.9 KB | Splunk SPL, Elastic KQL, Azure Sentinel KQL, alert triage, IR playbooks |
| `hybrid-automation.md` | 2.3 KB | Python↔PowerShell subprocess patterns, REST API bridges, cross-platform reconnaissance |
| `cloud-security.md` | 1.0 KB | ScoutSuite, Prowler, Pacu, CloudMapper, Azure Security Center, Forseti |
| `forensics-malware.md` | 0.8 KB | Volatility3, Plaso, Autopsy, YARA, PE analysis, artifact collection |

### Scripts (8 files, 8.7 KB)

| Script | Language | Purpose |
|--------|----------|---------|
| `recon-universal.py` | Python | Cross-platform host reconnaissance (Windows via PowerShell, Linux native) |
| `ad-enum.ps1` | PowerShell | Active Directory enumeration toolkit (users, groups, trusts, GPOs, Kerberoast targets) |
| `vuln-scan-orchestrator.py` | Python | Multi-scanner orchestration (Nuclei + Nmap async) |
| `sigma-converter.py` | Python | Sigma rule conversion to Splunk SPL, Elastic KQL, Sentinel KQL |
| `ioc-enricher.py` | Python | Threat intelligence enrichment (VirusTotal, AbuseIPDB) |
| `compliance-audit.py` | Python | Multi-framework compliance scanner template |
| `incident-response.ps1` | PowerShell | Windows IR automation (artifact collection, host isolation) |
| `security-report-generator.py` | Python | Automated HTML/Markdown report generation |

---

## 🚀 Installation

### Kimi (Primary Target)

**Method 1: Via `/skill-creator` (Recommended)**

1. Open [Kimi Agent Mode](https://kimi.com) (Web, App, or Kimi Claw)
2. Type in chat: `/skill-creator`
3. Upload `SKILL.md` or paste its contents
4. Kimi will guide you through refinement questions
5. The skill appears in **Skills Panel → Custom Skills**

**Method 2: Document Upload**

1. Go to **Skills Panel → Office Document to Skill**
2. Upload `SKILL.md` (max 3 files, 100 MB each)
3. Add description: *"DevSecOps and cybersecurity operations covering offensive/defensive security, SOC workflows, and hybrid PowerShell-Python automation"*
4. Click **Create Skill**

**Method 3: Kimi Claw (Desktop)**

1. Open **Kimi Claw**
2. Navigate to **Skills → Clawhub Skill Library**
3. Skills auto-sync between Web and Desktop via your Kimi account

### Claude Code

```bash
# Clone to Claude's skills directory
git clone https://github.com/YOUR_USERNAME/cybersec-ops-skill.git
cp -r cybersec-ops-skill/cybersec-ops ~/.claude/skills/

# Or symlink for development
ln -s $(pwd)/cybersec-ops ~/.claude/skills/cybersec-ops
```

### OpenAI Codex CLI

```bash
# Copy to Codex skills directory
cp -r cybersec-ops ~/.codex/skills/

# Or install via skills.sh (if available)
skills.sh install YOUR_USERNAME/cybersec-ops-skill
```

### Cursor

```bash
cp -r cybersec-ops ~/.cursor/skills/
```

### Gemini CLI

```bash
cp -r cybersec-ops ~/.gemini/skills/
```

---

## 🎯 How It Works

When you send a request, Kimi Agent assesses whether the task involves cybersecurity. If so, it automatically loads this skill and follows its instructions.

**Auto-trigger keywords:**
- Security operations, SOC, threat hunting, incident response
- Vulnerability assessment, penetration testing, red team, blue team, purple team
- DevSecOps, security automation, security scanning, SIEM, log analysis
- Forensics, malware analysis, network security, cloud security
- Identity security, compliance scanning, security hardening, security audit
- PowerShell offensive scripting, Python security ecosystem
- Container security, Kubernetes security, IaC security

### Example Interactions

| You Ask | Skill Response |
|---------|---------------|
| *"Scan my AWS for misconfigurations"* | Loads cloud-security.md, generates Boto3 scanner code |
| *"Write a PowerShell AD enum script"* | Loads powershell-offensive.md, provides PowerView patterns |
| *"Build a DevSecOps pipeline"* | Loads devsecops-pipelines.md, outputs GitLab CI YAML |
| *"Detect anomalies in SIEM logs"* | Loads soc-workflows.md, writes Splunk/Elastic queries |
| *"Analyze a memory dump"* | Loads forensics-malware.md, generates Volatility3 commands |
| *"Combine Python and PowerShell"* | Loads hybrid-automation.md, provides interoperability patterns |

---

## 🧪 Test Prompts

Verify the skill works with these prompts:

```
1. "Scan my AWS infrastructure for security misconfigurations"
2. "Write a PowerShell script to enumerate Active Directory users"
3. "Create a Python tool for network reconnaissance with Scapy"
4. "Build a DevSecOps pipeline with SAST and container scanning"
5. "How do I detect anomalous login patterns in my SIEM?"
6. "Analyze a memory dump for malware indicators"
7. "Convert this Sigma rule to Splunk SPL and Elastic KQL"
8. "Write a compliance audit script for CIS benchmarks"
9. "Check my Kubernetes cluster for privileged pods"
10. "Create a threat hunting playbook for lateral movement"
```

---

## 🛡️ Security Ethics

This skill contains **offensive security techniques** for **authorized testing only**.

All code examples include:
- ✅ Explicit authorization requirements
- ✅ Scope documentation templates
- ✅ Responsible disclosure guidelines

**Never use offensive techniques without explicit written authorization.**

The skill follows the principle: **"Teach defense by understanding offense"** — every attack vector is paired with detection and mitigation guidance.

---

## 📊 Skill Specification

```yaml
name: cybersec-ops
version: 1.0.0
category: security-operations
languages: [python, powershell, bash]
domains:
  - devsecops
  - soc
  - offensive-security
  - defensive-security
  - cloud-security
triggers:
  - security operations
  - penetration testing
  - threat hunting
  - incident response
  - vulnerability assessment
  - malware analysis
  - forensics
  - compliance audit
  - siem
  - devsecops
  - container security
  - kubernetes security
  - cloud security
  - active directory
  - powershell offensive
  - python security
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-addition`)
3. Commit your changes (`git commit -am 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-addition`)
5. Open a Pull Request

### Areas for Contribution

- Additional SIEM query patterns (QRadar, Chronicle, Splunk ES)
- More cloud provider coverage (OCI, Alibaba Cloud, IBM Cloud)
- Windows-specific defensive PowerShell modules
- MITRE ATT&CK mapping for all techniques
- Sigma rule library expansion
- Container escape detection patterns

---

## 📜 License

MIT License — See [LICENSE](LICENSE) file.

This skill is provided for **educational and authorized security testing purposes only**. The authors assume no liability for misuse.

---

## 🌐 Open-Source Skill Marketplaces

| Platform | URL | How to Submit |
|----------|-----|---------------|
| **SkillsMP** | https://skillsmp.com | Upload ZIP or link GitHub repo |
| **SkillsLLM** | https://skillsllm.com | Browse and install via web UI |
| **LobeHub** | https://lobehub.com/skills | Upload SKILL.md package |

---

## 🙏 Acknowledgments

- [Agent Skills Specification](https://skillsmp.com) — The open standard enabling cross-platform skill compatibility
- [Kimi](https://kimi.com) — For the skill system architecture and Agent Mode
- The cybersecurity community — For the tools, frameworks, and knowledge that power this skill

---

<div align="center">

**Built for defenders who understand offense. Powered by AI. Unified by code.**

[⬇ Download ZIP](cybersec-ops.zip) · [📖 SKILL.md](cybersec-ops/SKILL.md) · [🐛 Issues](../../issues)

</div>
