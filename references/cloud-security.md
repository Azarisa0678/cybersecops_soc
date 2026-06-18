# Cloud Security Reference

## AWS Security
- **ScoutSuite**: Multi-service security audit
- **Prowler**: CIS benchmark compliance
- **Pacu**: AWS exploitation framework
- **CloudMapper**: Network visualization

### Key Checks
- S3 bucket encryption and public access
- IAM password policies and MFA
- Security group rules (0.0.0.0/0)
- CloudTrail logging enabled
- EBS volume encryption

## Azure Security
- **Azure Security Center**: Unified security management
- **Azure Sentinel**: Cloud-native SIEM
- **Microsoft Defender**: Endpoint protection

### Key Checks
- NSG overly permissive rules
- Storage account public access
- Key Vault access policies
- RBAC role assignments

## GCP Security
- **Security Command Center**: Centralized visibility
- **Forseti Security**: Policy enforcement
- **Cloud Asset Inventory**: Resource tracking

### Key Checks
- Firewall rules with 0.0.0.0/0
- IAM binding over-permissions
- Cloud Storage bucket permissions
- VPC flow logs enabled
