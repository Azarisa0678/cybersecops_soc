#!/usr/bin/env python3
"""Automated security report generation"""
import json
from datetime import datetime

class SecurityReport:
    def __init__(self, title, findings):
        self.title = title
        self.findings = findings
        self.timestamp = datetime.now().isoformat()

    def generate_markdown(self):
        md = f"# {self.title}\n\nGenerated: {self.timestamp}\n\n"
        md += "| Severity | Issue | Remediation |\n"
        md += "|----------|-------|-------------|\n"
        for f in self.findings:
            md += f"| {f.get('severity','')} | {f.get('issue','')} | {f.get('remediation','')} |\n"
        return md

    def generate_html(self):
        html = f"""<html><head><title>{self.title}</title></head><body>
<h1>{self.title}</h1><p>Generated: {self.timestamp}</p>
<table border="1"><tr><th>Severity</th><th>Issue</th><th>Remediation</th></tr>"""
        for f in self.findings:
            html += f"<tr><td>{f.get('severity','')}</td><td>{f.get('issue','')}</td><td>{f.get('remediation','')}</td></tr>"
        html += "</table></body></html>"
        return html

if __name__ == "__main__":
    findings = [
        {"severity": "High", "issue": "Open S3 bucket",
         "remediation": "Enable encryption and block public access"}
    ]
    report = SecurityReport("AWS Security Audit", findings)
    print(report.generate_markdown())
