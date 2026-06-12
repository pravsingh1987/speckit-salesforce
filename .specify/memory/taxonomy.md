# Project Taxonomy

> **Purpose**: Defines standard naming conventions, terminology, and categorization used across the project. All SpecKit commands reference this file for consistent terminology.

## Naming Conventions

### Object Naming

| Type | Pattern | Example |
|------|---------|---------|
| Custom Objects | `[Namespace]_[EntityName]__c` | `KAM_Visit__c` |
| Junction Objects | `[Object1]_[Object2]_Junction__c` | `Account_Product_Junction__c` |
| Setup Objects | `[EntityName]_Settings__c` | `KAM_Settings__c` |
| Metadata Types | `[EntityName]__mdt` | `Approval_Rule__mdt` |

### Field Naming

| Type | Pattern | Example |
|------|---------|---------|
| Standard Extension | `[Meaningful_Name]__c` | `Wallet_Share__c` |
| Lookup Fields | `[Related_Object]__c` | `Primary_Contact__c` |
| Formula Fields | `[Calculated_Value]__c` | `Calculated_Revenue__c` |
| Rollup Summaries | `Total_[Metric]__c` | `Total_Opportunities__c` |

### Apex Naming

| Type | Pattern | Example |
|------|---------|---------|
| Trigger | `[Object]Trigger` | `AccountTrigger` |
| Trigger Handler | `[Object]TriggerHandler` | `AccountTriggerHandler` |
| Service Class | `[Domain]Service` | `OpportunityService` |
| Selector Class | `[Object]Selector` | `AccountSelector` |
| Controller | `[Feature]Controller` | `Hospital360Controller` |
| Test Class | `[ClassName]Test` | `AccountServiceTest` |
| Batch Class | `[Process]Batch` | `DataCleanupBatch` |
| Queueable | `[Process]Queueable` | `EmailNotificationQueueable` |

### LWC Naming

| Type | Pattern | Example |
|------|---------|---------|
| Components | `camelCase` | `hospitalKpiPanel` |
| Events | `handle[EventName]` | `handleAccountSelected` |
| Wire Methods | `wire[DataName]` | `wireAccountData` |
| Apex Methods | `get[Data]` / `save[Data]` | `getAccountKpis` |

### Permission Set Naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature Access | `[App]_[Feature]_[Level]` | `KAM_Hospital360_Read` |
| Role-Based | `[App]_[Role]_Access` | `KAM_Manager_Access` |
| Integration | `[System]_Integration` | `ERP_Integration` |

## Business Terminology

### Domain Glossary

| Term | Definition | Salesforce Mapping |
|------|------------|-------------------|
| [Business Term 1] | [Definition] | [Object.Field] |
| [Business Term 2] | [Definition] | [Object.Field] |
| [Business Term 3] | [Definition] | [Object.Field] |

### Acronyms

| Acronym | Full Form | Context |
|---------|-----------|---------|
| KAM | Key Account Manager | Sales role |
| HCP | Healthcare Provider | Contact type |
| HCO | Healthcare Organization | Account type |
| RSM | Regional Sales Manager | Sales role |
| YTD | Year to Date | Reporting period |
| MTD | Month to Date | Reporting period |

## Object Categories

### Master Data

| Object | Purpose | Owner |
|--------|---------|-------|
| Account | Customer/Organization records | Sales |
| Contact | Individual person records | Sales |
| Product2 | Product catalog | Product Team |
| User | System users | Admin |

### Transactional Data

| Object | Purpose | Volume |
|--------|---------|--------|
| Opportunity | Sales deals | High |
| Case | Support tickets | High |
| Order | Purchase orders | Medium |
| [Custom Object] | [Purpose] | [Volume] |

### Reference Data

| Object | Purpose | Update Frequency |
|--------|---------|------------------|
| [Picklist Values] | [Purpose] | Quarterly |
| [Custom Metadata] | [Purpose] | As needed |
| [Custom Settings] | [Purpose] | Rarely |

## Status Values

### Opportunity Stages

| Stage | Probability | Description |
|-------|-------------|-------------|
| Prospecting | 10% | Initial contact |
| Qualification | 20% | Needs identified |
| Proposal | 50% | Quote submitted |
| Negotiation | 75% | Terms discussion |
| Closed Won | 100% | Deal completed |
| Closed Lost | 0% | Deal lost |

### Case Statuses

| Status | Description | SLA |
|--------|-------------|-----|
| New | Just created | 4 hours |
| In Progress | Being worked | 24 hours |
| Escalated | Needs attention | 2 hours |
| Resolved | Solution provided | - |
| Closed | Confirmed resolved | - |

## Record Types

### Account Record Types

| Record Type | Description | Layout |
|-------------|-------------|--------|
| [Type 1] | [Description] | [Layout Name] |
| [Type 2] | [Description] | [Layout Name] |

### Opportunity Record Types

| Record Type | Description | Process |
|-------------|-------------|---------|
| [Type 1] | [Description] | [Sales Process] |
| [Type 2] | [Description] | [Sales Process] |

---

**Version**: 1.0
**Last Updated**: [Date]
