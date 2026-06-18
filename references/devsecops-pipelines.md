# DevSecOps Pipeline Integration

## CI/CD Security Gates

### GitLab CI Example
```yaml
stages:
  - secrets-scan
  - sast
  - dependency-check
  - container-scan
  - dast
  - iac-scan

secrets-scan:
  stage: secrets-scan
  script:
    - trufflehog filesystem . --json
  artifacts:
    reports:
      sast: secrets-report.json

sast:
  stage: sast
  script:
    - bandit -r . -f json -o bandit-report.json
    - semgrep --config=auto --json --output=semgrep-report.json
  artifacts:
    reports:
      sast: semgrep-report.json

dependency-check:
  stage: dependency-check
  script:
    - safety check --json --output safety-report.json
    - pip-audit --format=json --output=pip-audit-report.json
  artifacts:
    reports:
      dependency_scanning: safety-report.json

container-scan:
  stage: container-scan
  script:
    - trivy image --format json --output trivy-report.json $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  artifacts:
    reports:
      container_scanning: trivy-report.json

iac-scan:
  stage: iac-scan
  script:
    - checkov -d . --output json --output-file checkov-report.json
    - tfsec . --format json --out tfsec-report.json
  artifacts:
    reports:
      sast: checkov-report.json
```

### GitHub Actions Example
```yaml
name: Security Pipeline
on: [push, pull_request]

jobs:
  secrets-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
          head: HEAD

  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: returntocorp/semgrep-action@v1
      - uses: PyCQA/bandit@main
        with:
          args: "-r . -f json -o bandit-report.json"

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pypa/gh-action-pip-audit@release/v1
      - run: safety check --json

  container-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myapp:latest'
          format: 'json'
          output: 'trivy-report.json'

  iac-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: bridgecrewio/checkov-action@master
        with:
          directory: .
          output_format: json
          output_file_path: checkov-report.json
```

## SAST Tools
- **Bandit**: Python security linter
- **Semgrep**: Multi-language pattern matching
- **Pylint-security**: Security-focused extensions
- **SonarQube**: Continuous code quality

## DAST Tools
- **OWASP ZAP**: Web application scanner
- **Burp Suite Enterprise**: Enterprise web scanning
- **Wapiti**: Web app vulnerability scanner

## Container Security
- **Trivy**: Container image vulnerability scanner
- **Grype**: Alternative container scanner
- **Docker Bench**: CIS Docker benchmark
- **Kube-bench**: Kubernetes CIS benchmark

## IaC Security
- **Checkov**: Multi-framework IaC scanner
- **tfsec**: Terraform security scanner
- **cfn-nag**: CloudFormation security
- **ansible-lint**: Ansible security
