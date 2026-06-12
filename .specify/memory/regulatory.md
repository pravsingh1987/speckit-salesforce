# Regulatory & Compliance Requirements

> **Purpose**: Documents regulatory requirements, compliance standards, and data governance rules that MUST be followed. All SpecKit commands check this file to ensure compliance alignment.

## Applicable Regulations

### Primary Regulations

| Regulation | Jurisdiction | Applicability | Compliance Owner |
|------------|--------------|---------------|------------------|
| GDPR | EU/EEA | Personal data of EU residents | [Role] |
| CCPA/CPRA | California, USA | California consumer data | [Role] |
| HIPAA | USA | Protected health information | [Role] |
| SOX | USA | Financial reporting | [Role] |
| PCI-DSS | Global | Payment card data | [Role] |

### Industry-Specific Regulations

| Regulation | Industry | Requirement | Impact |
|------------|----------|-------------|--------|
| [Reg 1] | [Industry] | [Requirement] | [How it affects design] |
| [Reg 2] | [Industry] | [Requirement] | [How it affects design] |

## Data Classification

### Classification Levels

| Level | Description | Examples | Handling Requirements |
|-------|-------------|----------|----------------------|
| **Public** | No restrictions | Marketing content | Standard access |
| **Internal** | Business use only | Internal reports | Authenticated access |
| **Confidential** | Restricted access | Customer data | Role-based access, encryption |
| **Highly Confidential** | Strict controls | PII, PHI, financial | MFA, audit logging, encryption |

### Salesforce Field Classification

| Object | Field | Classification | Justification |
|--------|-------|----------------|---------------|
| Contact | Email | Confidential | PII |
| Contact | SSN__c | Highly Confidential | Sensitive PII |
| Account | Annual_Revenue__c | Confidential | Financial data |
| [Object] | [Field] | [Level] | [Reason] |

## Data Retention Requirements

### Retention Policies

| Data Category | Retention Period | Legal Basis | Deletion Method |
|---------------|------------------|-------------|-----------------|
| Customer Records | 7 years | Tax regulations | Archive then delete |
| Transaction Data | 10 years | Financial regulations | Archive |
| Marketing Consent | Duration of consent + 2 years | GDPR | Anonymize |
| Support Cases | 5 years | Business need | Archive |
| [Category] | [Period] | [Basis] | [Method] |

### Archival Strategy

| Object | Archive After | Archive Location | Retrieval SLA |
|--------|---------------|------------------|---------------|
| [Object 1] | [Period] | [Location] | [SLA] |
| [Object 2] | [Period] | [Location] | [SLA] |

## Consent Management

### Consent Types Required

| Consent Type | Purpose | Collection Point | Renewal |
|--------------|---------|------------------|---------|
| Marketing Email | Email campaigns | Signup form | Annual |
| Data Processing | Service delivery | Contract | Contract renewal |
| Third-Party Sharing | Partner programs | Opt-in form | Per use |
| [Type] | [Purpose] | [Collection] | [Renewal] |

### Consent Tracking in Salesforce

| Consent | Object | Field | Values |
|---------|--------|-------|--------|
| Email Opt-In | Contact | `HasOptedOutOfEmail` | Boolean |
| Do Not Call | Contact | `DoNotCall` | Boolean |
| [Consent] | [Object] | [Field] | [Values] |

## Audit Requirements

### Audit Trail Requirements

| Requirement | Implementation | Retention |
|-------------|----------------|-----------|
| All record changes | Salesforce Field History | 18 months |
| Login history | Salesforce Login History | 6 months |
| Setup changes | Setup Audit Trail | 6 months |
| API access | Event Monitoring | 1 year |
| [Requirement] | [Implementation] | [Retention] |

### Required Audit Fields

| Object | Field | Purpose | Trigger |
|--------|-------|---------|---------|
| All Custom Objects | `CreatedById` | Creation audit | Standard |
| All Custom Objects | `LastModifiedById` | Modification audit | Standard |
| [Object] | `Approved_By__c` | Approval audit | Process |
| [Object] | `Compliance_Check__c` | Compliance verification | Validation |

## Security Requirements

### Access Control Requirements

| Requirement | Implementation | Verification |
|-------------|----------------|--------------|
| Least privilege access | Permission Sets | Quarterly review |
| Role hierarchy | Salesforce Roles | Annual review |
| Data segregation | Sharing rules | Per release |
| MFA for sensitive data | Salesforce MFA | Login policy |

### Encryption Requirements

| Data Type | At Rest | In Transit | Key Management |
|-----------|---------|------------|----------------|
| PII Fields | Shield Encryption | TLS 1.2+ | Salesforce managed |
| Attachments | Shield Encryption | TLS 1.2+ | Salesforce managed |
| API Payloads | N/A | TLS 1.2+ | Certificate rotation |

## Compliance Checklist

### Pre-Deployment Checklist

- [ ] Data classification completed for all new fields
- [ ] Consent requirements identified and implemented
- [ ] Audit trail enabled for sensitive objects
- [ ] Field-level security configured
- [ ] Sharing rules reviewed
- [ ] Encryption applied where required
- [ ] Retention policy documented
- [ ] Privacy notice updated (if applicable)

### Periodic Compliance Tasks

| Task | Frequency | Owner | Due Date |
|------|-----------|-------|----------|
| Access review | Quarterly | [Role] | [Date] |
| Data retention cleanup | Monthly | [Role] | [Date] |
| Consent audit | Annual | [Role] | [Date] |
| Security assessment | Annual | [Role] | [Date] |

## Regulatory Contacts

| Regulation | Internal Contact | External Contact |
|------------|------------------|------------------|
| GDPR | [DPO Name/Email] | [Legal counsel] |
| [Regulation] | [Contact] | [External] |

---

**Compliance Officer**: [Name]
**Last Compliance Review**: [Date]
**Next Review Due**: [Date]
