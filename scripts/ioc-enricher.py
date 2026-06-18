#!/usr/bin/env python3
"""Threat intelligence enrichment"""
import requests
import json
import os

class IOCEnricher:
    def __init__(self):
        self.vt_key = os.getenv("VT_API_KEY")
        self.abuse_key = os.getenv("ABUSEIPDB_KEY")

    def enrich_ip(self, ip):
        results = {}
        if self.abuse_key:
            headers = {"Key": self.abuse_key, "Accept": "application/json"}
            params = {"ipAddress": ip, "maxAgeInDays": 90}
            resp = requests.get("https://api.abuseipdb.com/api/v2/check",
                              headers=headers, params=params)
            results["abuseipdb"] = resp.json()
        return results

    def enrich_hash(self, file_hash):
        results = {}
        if self.vt_key:
            headers = {"x-apikey": self.vt_key}
            resp = requests.get(f"https://www.virustotal.com/api/v3/files/{file_hash}",
                              headers=headers)
            results["virustotal"] = resp.json()
        return results

if __name__ == "__main__":
    enricher = IOCEnricher()
    print(json.dumps(enricher.enrich_ip("8.8.8.8"), indent=2))
