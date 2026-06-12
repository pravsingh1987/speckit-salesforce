# Domain Context

> **Purpose**: Captures industry-specific knowledge, business processes, and domain rules that inform all specifications. SpecKit commands reference this file to ensure domain alignment.

## Industry Overview

**Industry**: [e.g., Healthcare, Financial Services, Manufacturing, Retail]

**Sub-Sector**: [e.g., Pharmaceuticals, Insurance, Automotive, E-commerce]

**Business Model**: [e.g., B2B, B2C, B2B2C, Marketplace]

## Key Business Processes

### Process 1: [Process Name]

**Description**: [What this process accomplishes]

**Actors**:
- [Role 1]: [Responsibility]
- [Role 2]: [Responsibility]

**Steps**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Systems Involved**:
- Salesforce: [Objects/Features used]
- [Other System]: [Integration point]

**Success Criteria**:
- [Measurable outcome 1]
- [Measurable outcome 2]

---

### Process 2: [Process Name]

**Description**: [What this process accomplishes]

**Actors**:
- [Role 1]: [Responsibility]

**Steps**:
1. [Step 1]
2. [Step 2]

---

## Business Rules

### Rule Category 1: [e.g., Pricing Rules]

| Rule ID | Description | Enforcement |
|---------|-------------|-------------|
| BR-001 | [Rule description] | [Validation/Trigger/Flow] |
| BR-002 | [Rule description] | [Validation/Trigger/Flow] |

### Rule Category 2: [e.g., Approval Rules]

| Rule ID | Description | Threshold | Approver |
|---------|-------------|-----------|----------|
| AR-001 | [Rule description] | [Amount/Condition] | [Role] |
| AR-002 | [Rule description] | [Amount/Condition] | [Role] |

## Domain Entities

### Primary Entities

| Entity | Business Meaning | Salesforce Object | Key Relationships |
|--------|-----------------|-------------------|-------------------|
| Customer | Organization we sell to | Account | Contacts, Opportunities |
| Contact | Individual at customer | Contact | Account, Cases |
| Deal | Sales opportunity | Opportunity | Account, Products |
| Product | What we sell | Product2 | Pricebook, Opportunities |

### Domain-Specific Entities

| Entity | Business Meaning | Salesforce Object | Domain Context |
|--------|-----------------|-------------------|----------------|
| [Entity 1] | [Meaning] | [Object] | [Why it matters] |
| [Entity 2] | [Meaning] | [Object] | [Why it matters] |

## Industry Metrics & KPIs

### Sales Metrics

| Metric | Definition | Calculation | Target |
|--------|------------|-------------|--------|
| Win Rate | Deals won / Total deals | `Closed Won / (Closed Won + Closed Lost)` | >30% |
| Average Deal Size | Revenue per deal | `Total Revenue / Deal Count` | $[X] |
| Sales Cycle | Time to close | `Close Date - Create Date` | <[X] days |

### Operational Metrics

| Metric | Definition | Calculation | Target |
|--------|------------|-------------|--------|
| [Metric 1] | [Definition] | [Formula] | [Target] |
| [Metric 2] | [Definition] | [Formula] | [Target] |

## Competitive Landscape

### Key Competitors

| Competitor | Strengths | Weaknesses | Our Differentiation |
|------------|-----------|------------|---------------------|
| [Competitor 1] | [Strengths] | [Weaknesses] | [How we're different] |
| [Competitor 2] | [Strengths] | [Weaknesses] | [How we're different] |

### Market Position

- **Market Share**: [X%]
- **Target Segment**: [Description]
- **Value Proposition**: [Statement]

## Seasonal / Cyclical Factors

| Factor | Timing | Impact | System Consideration |
|--------|--------|--------|---------------------|
| [Fiscal Year End] | [Month] | [Impact on deals] | [Reporting needs] |
| [Industry Event] | [Month] | [Impact on activity] | [Capacity planning] |
| [Regulatory Deadline] | [Date] | [Compliance requirement] | [Automation needs] |

## Industry-Specific Considerations

### [Industry] Specific Requirements

- **[Requirement 1]**: [Description and impact]
- **[Requirement 2]**: [Description and impact]

### Common Challenges

| Challenge | Mitigation | Salesforce Solution |
|-----------|------------|---------------------|
| [Challenge 1] | [How addressed] | [Feature/Configuration] |
| [Challenge 2] | [How addressed] | [Feature/Configuration] |

---

**Domain Expert**: [Name/Role]
**Last Validated**: [Date]
