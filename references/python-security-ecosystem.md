# Python Security Ecosystem Reference

## Table of Contents
1. Core Libraries
2. Network Security
3. Web Application Security
4. Cryptography
5. Malware Analysis & Forensics
6. Threat Intelligence
7. Vulnerability Scanning
8. Exploitation Frameworks
9. Cloud Security
10. Container & Kubernetes Security
11. SIEM & SOAR Integration
12. Machine Learning for Security

---

## Core Libraries

### Essential Security Libraries
```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
response = session.get("https://api.example.com", verify=True, timeout=30)
```

### Subprocess Security
```python
import subprocess

# SAFE: Use list arguments, avoid shell=True
result = subprocess.run(
    ["nmap", "-sV", "target.com"],
    capture_output=True, text=True, timeout=300
)
```

### Path Security
```python
from pathlib import Path
base_dir = Path("/safe/directory")
user_file = Path(user_input).name
full_path = base_dir / user_file
if not str(full_path.resolve()).startswith(str(base_dir.resolve())):
    raise ValueError("Path traversal detected")
```

### Cryptography
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import secrets, base64

token = secrets.token_urlsafe(32)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
    salt=secrets.token_bytes(16), iterations=480000)
key = base64.urlsafe_b64encode(kdf.derive(b"password"))
f = Fernet(key)
token = f.encrypt(b"sensitive data")
```

---

## Network Security

### Scapy
```python
from scapy.all import *
ans, unans = sr(IP(dst="target.com")/TCP(dport=[22,80,443], flags="S"), timeout=2)
for sent, received in ans:
    if received.haslayer(TCP) and received[TCP].flags == "SA":
        print(f"Port {sent[TCP].dport} is open")
```

### Async Port Scanner
```python
import asyncio, socket

async def scan_port(ip, port, timeout=3):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), timeout=timeout)
        writer.close()
        return {"port": port, "status": "open"}
    except: return None

async def scan_host(ip, ports):
    tasks = [scan_port(ip, p) for p in ports]
    return [r for r in await asyncio.gather(*tasks) if r]
```

### DNS Enumeration
```python
import dns.resolver
resolver = dns.resolver.Resolver()
resolver.nameservers = ["8.8.8.8"]
answers = resolver.resolve("example.com", "A")
for rdata in answers:
    print(f"A: {rdata.address}")
```

---

## Web Application Security

### Security Headers Check
```python
import requests

class SecureScanner:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "SecurityScanner/1.0"})

    def check_headers(self, url):
        response = self.session.get(url, timeout=10)
        required = ["Strict-Transport-Security", "Content-Security-Policy",
                    "X-Frame-Options", "X-Content-Type-Options"]
        return [{"header": h, "missing": h not in response.headers} for h in required]
```

### SQL Injection Detection
```python
class SQLiDetector:
    def __init__(self, target_url):
        self.target_url = target_url
        self.payloads = ["' OR '1'='1", "1 AND 1=1", "1 AND 1=2"]

    def test_parameter(self, param_name):
        results = []
        for payload in self.payloads:
            data = {param_name: payload}
            try:
                response = requests.get(self.target_url, params=data, timeout=10)
                errors = ["sql syntax", "mysql_fetch", "ORA-", "PostgreSQL"]
                for error in errors:
                    if error.lower() in response.text.lower():
                        results.append({"payload": payload, "evidence": error})
            except: continue
        return results
```

---

## Cryptography

### Password Hashing
```python
from argon2 import PasswordHasher
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
hash = ph.hash("user_password")
ph.verify(hash, "user_password")
```

### Certificate Analysis
```python
import ssl, socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def analyze_cert(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = x509.load_der_x509_certificate(
                ssock.getpeercert(binary_form=True), default_backend())
            return {"subject": cert.subject.rfc4514_string(),
                    "not_after": cert.not_valid_after}
```

---

## Malware Analysis & Forensics

### PE File Analysis
```python
import pefile

def analyze_pe(filepath):
    pe = pefile.PE(filepath)
    return {
        "is_dll": pe.is_dll(),
        "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "sections": [{"name": s.Name.decode().strip("\x00"),
                      "entropy": s.get_entropy()} for s in pe.sections]
    }
```

### Volatility3 Memory Forensics
```python
from volatility3.framework import contexts
from volatility3.framework.plugins.windows import pslist

def analyze_memory(dump_path):
    context = contexts.Context()
    context.config["automagic.LayerStacker.single_location"] = f"file://{dump_path}"
    plugin = pslist.PsList(context)
    return [{"pid": p.UniqueProcessId, "name": p.ImageFileName} for p in plugin.run()]
```

---

## Threat Intelligence

### MISP Integration
```python
from pymisp import PyMISP, MISPEvent

class MISPClient:
    def __init__(self, url, key):
        self.misp = PyMISP(url, key, ssl=True, debug=False)

    def search_ioc(self, value, type_attr="ip-dst"):
        return self.misp.search(controller="attributes", type_attribute=type_attr, value=value)

    def create_event(self, info, threat_level=3):
        event = MISPEvent()
        event.info = info
        event.threat_level_id = threat_level
        return self.misp.add_event(event)
```

### VirusTotal API
```python
import vt

class VTClient:
    def __init__(self, api_key):
        self.client = vt.Client(api_key)

    def get_file_report(self, file_hash):
        file = self.client.get_object(f"/files/{file_hash}")
        return {"hash": file.md5, "stats": file.last_analysis_stats}
```

### AbuseIPDB
```python
import requests

class AbuseIPDB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"Key": api_key, "Accept": "application/json"}

    def check_ip(self, ip):
        params = {"ipAddress": ip, "maxAgeInDays": 90}
        return requests.get("https://api.abuseipdb.com/api/v2/check",
                          headers=self.headers, params=params).json()
```

---

## Vulnerability Scanning

### Nuclei Integration
```python
import subprocess, json

def run_nuclei(targets, severity=None):
    cmd = ["nuclei", "-u", targets, "-json"]
    if severity: cmd.extend(["-severity", severity])
    result = subprocess.run(cmd, capture_output=True, text=True)
    return [json.loads(line) for line in result.stdout.strip().split("\n") if line]
```

### OWASP ZAP
```python
from zapv2 import ZAPv2

class ZAPScanner:
    def __init__(self, api_key="", proxy="http://localhost:8080"):
        self.zap = ZAPv2(apikey=api_key, proxies={"http": proxy, "https": proxy})

    def spider_scan(self, target):
        scan_id = self.zap.spider.scan(target)
        while int(self.zap.spider.status(scan_id)) < 100:
            import time; time.sleep(1)
        return self.zap.spider.results(scan_id)
```

---

## Exploitation Frameworks

### Impacket
```python
from impacket.smbconnection import SMBConnection
conn = SMBConnection("target", "target")
conn.login("username", "password", "domain")
shares = conn.listShares()
```

### Pwntools
```python
from pwn import *
p = remote("target.com", 1337)
payload = b"A" * 100 + p64(0xdeadbeef)
p.sendline(payload)
p.interactive()
```

---

## Cloud Security

### AWS (Boto3)
```python
import boto3
from botocore.exceptions import ClientError

class AWSSecurityScanner:
    def __init__(self, profile=None):
        session = boto3.Session(profile_name=profile)
        self.ec2 = session.client("ec2")
        self.iam = session.client("iam")
        self.s3 = session.client("s3")

    def check_s3_encryption(self):
        violations = []
        for bucket in self.s3.list_buckets()["Buckets"]:
            try:
                self.s3.get_bucket_encryption(Bucket=bucket["Name"])
            except ClientError as e:
                if e.response["Error"]["Code"] == "ServerSideEncryptionConfigurationNotFoundError":
                    violations.append({"resource": bucket["Name"], "severity": "HIGH"})
        return violations

    def check_security_groups(self):
        violations = []
        for sg in self.ec2.describe_security_groups()["SecurityGroups"]:
            for rule in sg["IpPermissions"]:
                for ip_range in rule.get("IpRanges", []):
                    if ip_range["CidrIp"] == "0.0.0.0/0":
                        violations.append({"sg": sg["GroupId"], "severity": "HIGH"})
        return violations
```

### Azure
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.security import SecurityCenter
from azure.mgmt.network import NetworkManagementClient

class AzureSecurityScanner:
    def __init__(self, subscription_id):
        cred = DefaultAzureCredential()
        self.security = SecurityCenter(cred, subscription_id, "centralus")
        self.network = NetworkManagementClient(cred, subscription_id)

    def get_security_alerts(self):
        return [{"name": a.name, "severity": a.alert_severity, "status": a.status}
                for a in self.security.alerts.list()]
```

### GCP
```python
from google.cloud import securitycenter_v1, compute_v1

class GCPSecurityScanner:
    def __init__(self, project_id):
        self.project_id = project_id
        self.security = securitycenter_v1.SecurityCenterClient()
        self.compute = compute_v1.FirewallsClient()

    def check_firewall_rules(self):
        violations = []
        for rule in self.compute.list(project=self.project_id):
            for allowed in rule.allowed:
                if "0.0.0.0/0" in rule.source_ranges:
                    violations.append({"rule": rule.name, "severity": "HIGH"})
        return violations
```

---

## Container & Kubernetes Security

### Docker
```python
import docker

class DockerSecurityScanner:
    def __init__(self):
        self.client = docker.from_env()

    def check_privileged(self):
        violations = []
        for c in self.client.containers.list(all=True):
            if c.attrs["HostConfig"]["Privileged"]:
                violations.append({"container": c.name, "severity": "CRITICAL"})
        return violations
```

### Kubernetes
```python
from kubernetes import client, config

class K8sSecurityScanner:
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
        self.rbac = client.RbacAuthorizationV1Api()

    def check_privileged_pods(self):
        violations = []
        for pod in self.v1.list_pod_for_all_namespaces().items:
            for container in pod.spec.containers:
                if container.security_context and container.security_context.privileged:
                    violations.append({"pod": pod.metadata.name, "severity": "CRITICAL"})
        return violations

    def check_rbac(self):
        violations = []
        for role in self.rbac.list_cluster_role().items:
            for rule in role.rules:
                if "*" in rule.verbs or "*" in rule.resources:
                    violations.append({"role": role.metadata.name, "severity": "HIGH"})
        return violations
```

---

## SIEM & SOAR Integration

### Splunk
```python
import splunklib.client as client
import splunklib.results as results

class SplunkClient:
    def __init__(self, host, port, username, password):
        self.service = client.connect(host=host, port=port,
                                      username=username, password=password)

    def search(self, query, earliest="-24h", latest="now"):
        job = self.service.jobs.create(query, earliest_time=earliest, latest_time=latest)
        while not job.is_done(): import time; time.sleep(0.5)
        return [r for r in results.ResultsReader(job.results()) if isinstance(r, dict)]
```

### Elastic
```python
from elasticsearch import Elasticsearch

class ElasticSecurityClient:
    def __init__(self, hosts, username, password):
        self.es = Elasticsearch(hosts, basic_auth=(username, password), verify_certs=True)

    def search_security_events(self, query, index="security-*", size=1000):
        return self.es.search(index=index, body={"query": query, "size": size,
            "sort": [{"@timestamp": "desc"}]})["hits"]["hits"]
```

### TheHive / Cortex
```python
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseObservable

class TheHiveClient:
    def __init__(self, url, api_key):
        self.api = TheHiveApi(url, api_key)

    def create_case(self, title, description, severity=2):
        return self.api.create_case(Case(title=title, description=description, severity=severity))

    def add_observable(self, case_id, data_type, data):
        return self.api.create_case_observable(case_id,
            CaseObservable(dataType=data_type, data=data))
```

---

## Machine Learning for Security

### Anomaly Detection
```python
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.scaler = StandardScaler()
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def fit(self, data):
        self.model.fit(self.scaler.fit_transform(data))

    def predict(self, data):
        scaled = self.scaler.transform(data)
        return pd.DataFrame({"anomaly": self.model.predict(scaled) == -1,
                             "score": self.model.decision_function(scaled)})
```

### LSTM for Behavioral Analysis
```python
import torch, torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

class SecurityLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out, _ = self.lstm(x, (torch.zeros(2, x.size(0), 128), torch.zeros(2, x.size(0), 128)))
        return self.sigmoid(self.fc(out[:, -1, :]))
```

---

## Best Practices

### Secure Coding
1. Never trust user input - sanitize everything
2. Use parameterized APIs, avoid shell=True with user input
3. Never hardcode credentials - use environment variables
4. Always verify SSL/TLS certificates
5. Use secrets module, not random, for security tokens

### Performance
1. Use asyncio for network operations
2. Batch API calls when possible
3. Reuse connections with requests.Session()
4. Cache threat intelligence results

### Error Handling
```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("security")

def security_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed: {e}")
            raise
    return wrapper
```
