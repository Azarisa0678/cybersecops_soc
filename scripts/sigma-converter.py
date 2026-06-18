#!/usr/bin/env python3
"""Sigma rule format conversion"""
import yaml
import json

class SigmaConverter:
    def __init__(self, rule_path):
        with open(rule_path) as f:
            self.rule = yaml.safe_load(f)

    def to_splunk(self):
        detection = self.rule.get("detection", {})
        return f"index=* {detection}"

    def to_elastic(self):
        detection = self.rule.get("detection", {})
        return f"event.category:* AND {detection}"

    def to_sentinel(self):
        detection = self.rule.get("detection", {})
        return f"SecurityEvent | where {detection}"

if __name__ == "__main__":
    converter = SigmaConverter("rule.yml")
    print("Splunk:", converter.to_splunk())
    print("Elastic:", converter.to_elastic())
    print("Sentinel:", converter.to_sentinel())
