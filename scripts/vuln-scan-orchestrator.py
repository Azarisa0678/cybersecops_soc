#!/usr/bin/env python3
"""Multi-scanner vulnerability orchestration"""
import subprocess
import json
import asyncio

class VulnScanner:
    def __init__(self, target):
        self.target = target
        self.results = {}

    async def run_nuclei(self):
        result = subprocess.run(
            ["nuclei", "-u", self.target, "-json"],
            capture_output=True, text=True
        )
        findings = []
        for line in result.stdout.strip().split("\n"):
            if line:
                findings.append(json.loads(line))
        return findings

    async def run_nmap(self):
        result = subprocess.run(
            ["nmap", "-sV", "-O", self.target, "-oX", "-"],
            capture_output=True, text=True
        )
        return result.stdout

    async def run_all(self):
        self.results["nuclei"] = await self.run_nuclei()
        self.results["nmap"] = await self.run_nmap()
        return self.results

if __name__ == "__main__":
    scanner = VulnScanner("target.com")
    results = asyncio.run(scanner.run_all())
    print(json.dumps(results, indent=2))
