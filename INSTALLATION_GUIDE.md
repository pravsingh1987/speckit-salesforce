# SpecKit Salesforce Edition - Installation & User Guide

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation Steps](#installation-steps)
4. [Required Information](#required-information)
5. [Post-Installation Setup](#post-installation-setup)
6. [How to Use SpecKit](#how-to-use-speckit)
7. [Available Commands](#available-commands)
8. [Creating Your First Specification](#creating-your-first-specification)
9. [Wireframes](#wireframes)
10. [Dashboard & Tracking](#dashboard--tracking)
11. [Jira Integration](#jira-integration)
12. [Adding Team Members](#adding-team-members)
13. [Troubleshooting](#troubleshooting)

---

## Overview

SpecKit Salesforce Edition is a universal development accelerator for any Salesforce project. It provides:

- **12 Agent Skills** for spec-driven development
- **Clean Templates** (no pre-built samples - start fresh)
- **Progress Dashboard** with GitHub Pages support
- **Jira Integration** for story status sync
- **Multi-Contributor Token Tracking**
- **Wireframe Generation** for UI mockups

---

## Prerequisites

| Requirement | Description | How to Get |
|-------------|-------------|------------|
| **Cursor IDE** | AI-powered IDE | [cursor.sh](https://cursor.sh) |
| **Git** | Version control | `brew install git` or [git-scm.com](https://git-scm.com) |
| **Bash/Zsh** | Terminal | Built into macOS/Linux |
| **GitHub Account** | Repository hosting | [github.com](https://github.com) |
| **Jira Access** | (Optional) Story tracking | Your organization's Jira |
| **Salesforce CLI** | (Optional) Deployment | `npm install -g @salesforce/cli` |

---

## Installation Steps

### Step 1: Clone the Package

> ⚠️ **IMPORTANT: Use macOS Terminal, NOT Cursor Terminal**
> 
> Cursor's sandbox blocks `git clone` for security reasons (to prevent malicious git hooks).
> You MUST run the clone command in your **macOS Terminal app** or **iTerm**, not in Cursor's integrated terminal.

**For Salesforce Internal Users (Recommended):**

Open **macOS Terminal** and run:
```bash
git clone https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git
```

**For External Users:**

Open **macOS Terminal** and run:
```bash
git clone https://github.com/pravsingh1987/speckit-salesforce.git
```

### Step 2: Create Your Project Directory

```bash
mkdir my-salesforce-project
cd my-salesforce-project
```

### Step 3: Run the Installer

```bash
bash /path/to/speckit-salesforce/install.sh .
```

**Example (Salesforce Internal):**
```bash
bash ~/speckit-salesforce/install.sh .
```

### Step 4: Answer the Configuration Prompts

The installer will guide you through setup interactively.

### Step 5: Open in Cursor

```bash
cursor .
```

---

## Required Information

### During Installation

The installer will prompt for:

#### Required (Must Provide)

| Field | What It Is | Example |
|-------|------------|---------|
| **Project Name** | Display name for your project | `Customer Portal` |

#### Recommended (Enter if Available)

| Field | What It Is | Example |
|-------|------------|---------|
| **Salesforce Org Alias** | Your SF CLI org alias | `my-dev-org` |
| **GitHub Repository URL** | Where you'll push code | `https://github.com/mycompany/customer-portal` |
| **Jira Project Key** | Your Jira project identifier | `PORTAL` |
| **Jira Board URL** | Full URL to your Jira board | `https://mycompany.atlassian.net/jira/software/projects/PORTAL/boards/1` |
| **Your Name** | For contributor tracking | `Jane Smith` |
| **Your Role** | Your job title | `Lead Developer` |

### Example Installation Session

```
╔════════════════════════════════════════════════════════════════╗
║        SpecKit - Salesforce Development Accelerator            ║
║                     Generic Edition v1.0                       ║
╚════════════════════════════════════════════════════════════════╝

Where would you like to install SpecKit?
Target directory (. for current): .

📁 Install location: /Users/jane/projects/customer-portal

Proceed? (Y/n): Y

📦 Installing components...
  ✓ SpecKit core
  ✓ Agent skills (12 commands)
  ✓ Progress dashboard
  ✓ Specs directory

════════════════════════════════════════════════════════════════
                    PROJECT CONFIGURATION
════════════════════════════════════════════════════════════════

Project Name [required]: Customer Portal
Salesforce Org Alias: portal-dev

─── GitHub Configuration ───
Full URL to your repository (for dashboard links)
Example: https://github.com/myorg/my-project
GitHub URL: https://github.com/mycompany/customer-portal

─── Jira Configuration ───
Jira Project Key (e.g., MYPROJ): PORTAL
Jira Board URL: https://mycompany.atlassian.net/jira/software/projects/PORTAL/boards/1

─── Your Information ───
Your Name: Jane Smith
Your Role: Lead Developer

✅ Installation Complete!
```

---

## Post-Installation Setup

### 1. Initialize Git Repository

If the installer didn't initialize git:

```bash
git init
git add .
git commit -m "Initial SpecKit setup"
```

### 2. Connect to GitHub

```bash
git remote add origin https://github.com/your-org/your-repo.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/docs`
4. Click **Save**
5. Wait 2-3 minutes for deployment
6. Your dashboard will be at: `https://<username>.github.io/<repo>/progress-dashboard.html`

### 4. Verify Installation

Open Cursor and try:
```
/speckit-specify
```

You should see the skill activate and prompt for input.

---

## How to Use SpecKit

### The SpecKit Workflow

```
   ┌──────────────────────────────────────────────────────────┐
   │                    SPECKIT WORKFLOW                      │
   └──────────────────────────────────────────────────────────┘
   
   Step 1          Step 2          Step 3          Step 4
   ┌─────┐        ┌─────┐        ┌─────┐        ┌─────┐
   │SPEC │───────▶│PLAN │───────▶│TASKS│───────▶│BUILD│
   └─────┘        └─────┘        └─────┘        └─────┘
      │              │              │              │
      │   ┌──────────┴──────────┐  │              │
      │   │                     │  │              │
      ▼   ▼                     ▼  ▼              ▼
   ┌─────────┐              ┌─────────┐      ┌─────────┐
   │WIREFRAME│              │ ANALYZE │      │DASHBOARD│
   └─────────┘              └─────────┘      └─────────┘
```

### Quick Start Commands

| Step | Command | What It Does |
|------|---------|--------------|
| 1 | `/speckit-specify` | Define what you want to build |
| 2 | `/speckit-plan` | Research and create implementation plan |
| 3 | `/speckit-wireframe` | Generate UI mockups |
| 4 | `/speckit-tasks` | Break into actionable tasks |
| 5 | `/speckit-analyze` | Validate before building |
| 6 | `/speckit-implement` | Build the solution |
| 7 | `/speckit-dashboard` | Track progress |

---

## Available Commands

### Primary Commands

| Command | Purpose | Creates |
|---------|---------|---------|
| `/speckit-specify` | Generate specification from objective | `specs/<feature>/spec.md` |
| `/speckit-plan` | Create implementation plan with research | `plan.md`, `data-model.md` |
| `/speckit-tasks` | Break spec into implementable tasks | `tasks.md` |
| `/speckit-wireframe` | Generate SLDS-aligned UI mockups | `wireframes.md` |
| `/speckit-analyze` | Validate spec completeness | PASS/FAIL verdict |
| `/speckit-implement` | Execute task implementation | Code files |
| `/speckit-dashboard` | Generate/update progress dashboard | Dashboard update |

### Supporting Commands

| Command | Purpose |
|---------|---------|
| `/speckit-checklist` | Generate requirement checklist |
| `/speckit-clarify` | Refine ambiguous requirements |
| `/speckit-constitution` | Define project guardrails |
| `/speckit-taskstoissues` | Export tasks to Jira |
| `/speckit-agent-context-update` | Update agent context |

### Natural Language Commands

You can also use natural language:

| Say This | What Happens |
|----------|--------------|
| "Sync from Jira" | Pulls latest story statuses |
| "Mark PROJ-123 as built" | Updates story to built |
| "Add contributor John Doe" | Adds team member |
| "Show me the dashboard" | Opens/generates dashboard |

---

## Creating Your First Specification

### Step 1: Define Your Feature

The `/speckit-specify` command accepts multiple input types. You can provide as much context as available:

#### Input Types Accepted

| Input Type | Description | Example |
|------------|-------------|---------|
| **Objective Statement** | High-level goal | "Allow customers to manage their accounts online" |
| **Meeting Transcripts** | Recorded meeting notes | Paste transcript from Zoom/Teams/Otter.ai |
| **Recording Summaries** | AI-generated meeting summaries | GPT/Claude summary of stakeholder call |
| **Discussion Notes** | Email threads, Slack conversations | Copy relevant discussion points |
| **Wireframes/Mockups** | Visual references | Describe or reference Figma/sketch |
| **Requirements Documents** | PRDs, BRDs, user stories | Paste or summarize key requirements |
| **Existing System Analysis** | Current state documentation | "Currently using spreadsheets for X..." |
| **Stakeholder Interviews** | Interview transcripts | Q&A format from discovery sessions |
| **Competitor Analysis** | Reference implementations | "Similar to how Competitor X does..." |

#### Basic Format

```
/speckit-specify -EPIC "Feature Name"
Objective: What you want to achieve
Primary users: Who will use it
Core objects: Salesforce objects involved
Capabilities:
* Capability 1
* Capability 2
```

#### Rich Input Example (with Meeting Transcript)

```
/speckit-specify -EPIC "Customer Self-Service Portal"

## Meeting Transcript (Discovery Call - June 10, 2026)

**Participants**: John (Product Owner), Sarah (Business Analyst), Mike (IT Lead)

**John**: "We need customers to log in and see their account status without calling support."

**Sarah**: "They should be able to submit cases directly and track them. Currently they email us and it's chaos."

**Mike**: "We have Account and Contact data. Cases are already in Salesforce. We just need the portal layer."

**John**: "Budget for Phase 1 is basic - login, view account, submit case. Phase 2 adds payments."

---

## Intent Summary

Objective: Allow customers to self-serve for account inquiries and case submission
Primary users: B2B Customers (portal users), Support Agents (internal)
Core objects: Account, Contact, Case, User (Community)

## Key Requirements from Discussion

* SSO integration with customer's Azure AD
* Read-only account view (no editing in Phase 1)
* Case submission with file attachments
* Email notifications on case status change
* Mobile-responsive design

## Constraints Mentioned

* Must use Salesforce Experience Cloud
* Go-live target: Q3 2026
* No custom authentication - use standard Salesforce login
```

#### Example with Wireframe Reference

```
/speckit-specify -EPIC "Sales Dashboard"

## Wireframe Description

The dashboard shows:
- Top row: 4 KPI cards (Pipeline Value, Win Rate, Avg Deal Size, Deals Closing This Month)
- Middle: Bar chart showing pipeline by stage
- Bottom left: Table of top 10 opportunities
- Bottom right: Activity feed of recent updates

## Figma Reference
See: https://figma.com/file/xxx/Sales-Dashboard-Mockup

## Discussion Summary (from Slack #sales-ops)

Sales VP wants to see their team's pipeline at a glance. Current reports require 5 clicks.
Must work on mobile for field reps. Real-time data preferred but 15-min delay acceptable.
```

#### Example with Requirements Document

```
/speckit-specify -EPIC "Order Management Enhancement"

## PRD Summary (from Confluence)

### Problem Statement
Order processing takes 3 days due to manual approval routing.

### Proposed Solution
Automated approval workflow based on order value and customer tier.

### User Stories (from Jira)
- US-101: As a sales rep, I want orders under $10K auto-approved
- US-102: As a manager, I want to approve orders $10K-$50K in one click
- US-103: As a director, I want visibility into all pending approvals

### Acceptance Criteria
- Orders < $10K: Auto-approve, notify rep
- Orders $10K-$50K: Route to manager, 24hr SLA
- Orders > $50K: Route to director with full margin analysis
```

### Step 2: Review the Generated Spec

The agent will create `specs/001-customer-portal/spec.md` containing:
- Detailed requirements
- User stories
- Acceptance criteria
- Edge cases
- Technical considerations

### Step 3: Generate Implementation Plan

```
/speckit-plan
```

This creates:
- `plan.md` - Implementation approach
- `data-model.md` - ERD and field specifications
- `contracts/apex-controllers.md` - Apex interface definitions

### Step 4: Create Wireframes

```
/speckit-wireframe
```

Generates `wireframes.md` with:
- SLDS-aligned ASCII mockups
- Component specifications
- Screen flow diagrams

### Step 5: Break Into Tasks

```
/speckit-tasks
```

Creates `tasks.md` with:
- Prioritized task list
- Dependencies
- Acceptance criteria per task
- Estimated complexity

### Step 6: Validate

```
/speckit-analyze
```

Returns:
- PASS or FAIL verdict
- Missing requirements
- Recommendations

---

## Wireframes

### Generating Wireframes

```
/speckit-wireframe
```

### What You Get

The wireframe skill generates SLDS-aligned mockups:

```
┌─────────────────────────────────────────────────────────────┐
│ ☰  Customer Portal                    🔔  👤 John Smith ▼   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Welcome, John Smith                                 │   │
│  │  Account: Acme Corporation                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 📊       │ │ 📋       │ │ 💳       │ │ 📞       │       │
│  │ Dashboard│ │ Cases    │ │ Billing  │ │ Support  │       │
│  │          │ │ 3 Open   │ │ $1,234   │ │          │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘

LWC: portalDashboard
SLDS: slds-card, slds-grid, slds-icon
```

### Using Wireframes

1. **Customer Sign-off**: Share wireframes.md for approval
2. **Development Reference**: Use as UI specification
3. **Jira Attachment**: Link wireframes to stories

---

## Dashboard & Tracking

### Dashboard Features

| Tab | What It Shows |
|-----|---------------|
| **Overview** | KPIs, progress bar, token charts |
| **Built Stories** | What's deployed to Salesforce |
| **Contributors** | Token consumption per person |
| **Epics & Stories** | Full backlog with status |
| **Token Details** | Session-by-session breakdown |

### Accessing the Dashboard

**Locally:**
```bash
open docs/progress-dashboard.html
```

**GitHub Pages:**
```
https://<username>.github.io/<repo>/progress-dashboard.html
```

### Updating the Dashboard

```
/speckit-dashboard
```

Or tell the agent:
- "Sync from Jira"
- "Update dashboard"
- "Mark story X as done"

---

## Jira Integration

### Manual Sync (No Admin Required)

1. Update story status in Jira
2. Tell agent: "Sync from Jira"
3. Dashboard updates automatically

### Automated Sync (Requires Jira Admin)

See `docs/jira-integration.md` for webhook setup.

### Status Mapping

| Jira Status | Dashboard Status | Color |
|-------------|------------------|-------|
| Open / To Do | Pending | Gray |
| In Progress | In Progress | Blue |
| In Review | In Review | Yellow |
| Done / Closed | Built | Green |

---

## Adding Team Members

### Method 1: During Installation

The installer prompts for your information automatically.

### Method 2: Edit JSON

Edit `docs/progress-tracker.json`:

```json
{
  "contributors": [
    {
      "id": "jane-smith",
      "name": "Jane Smith",
      "role": "Lead Developer",
      "total_tokens": 150000,
      "sessions_count": 5
    },
    {
      "id": "john-doe",
      "name": "John Doe",
      "role": "Developer",
      "total_tokens": 75000,
      "sessions_count": 3
    }
  ]
}
```

### Method 3: Tell the Agent

"Add contributor John Doe as Developer"

---

## Salesforce Constitution

The Salesforce Constitution is a governance document that defines architectural principles, security rules, and development standards for your project.

### Why Use a Constitution?

| Benefit | Description |
|---------|-------------|
| **Consistency** | All code follows the same patterns and standards |
| **Security** | Enforces CRUD/FLS, user mode, and access controls |
| **Quality** | Mandates testing standards, code coverage, and documentation |
| **Governance** | Provides audit trail and change management |

### Setting Up Your Constitution

1. **Copy the sample constitution:**
   ```bash
   cp sample-constitution.md .specify/memory/constitution.md
   ```

2. **Customize for your project:**
   - Replace `[YOUR-PROJECT]` with your project name
   - Replace `[Your Organization]` with your org name
   - Add industry-specific principles if needed
   - Update Salesforce org alias

3. **Verify with SpecKit:**
   ```
   /speckit-constitution
   ```

### Sample Constitution Sections

The included `sample-constitution.md` covers:

- **Principle I**: Architectural Integrity & Platform-First
- **Principle II**: Security & Access Control
- **Principle III**: Governor Limits & Bulkification
- **Principle IV**: Apex Code Quality Standards
- **Principle V**: Apex Testing Standards
- **Principle VI**: Permission Sets & Security Governance
- **Principle VII**: Lightning Web Components Standards
- **Principle VIII**: Agentforce & Agent Script Standards

### Industry Extensions

For specific industries, add additional principles:

**Healthcare/Life Sciences:**
```markdown
### IX. Industry-First, Minimal Customization
Standard and industry-cloud capabilities MUST be preferred over bespoke build.

### X. Salesforce Life Sciences Data Model Alignment
HCO = Account; HCP = Contact. Use native Health Cloud affiliations.
```

**Financial Services:**
```markdown
### IX. Financial Services Cloud Data Model
Use standard FSC objects (FinancialAccount, FinancialGoal, etc.)

### X. Compliance & Audit Trail
All changes must be auditable. Implement Field History Tracking.
```

---

## Salesforce PS Audit Tool Integration

The Salesforce Professional Services Audit Tool validates your implementation against best practices.

### Tool Overview

| Feature | Description |
|---------|-------------|
| **Static Analysis** | Scans Apex, LWC, and metadata for anti-patterns |
| **5-Tier Grading** | CRITICAL, High, Medium, Low, Informational |
| **Coverage Areas** | Governor limits, security, performance, testing |

### Installation

1. **Obtain the Audit Tool:**
   - Contact Salesforce Professional Services
   - Or download from internal Salesforce Partner Portal

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure in Constitution:**
   Update `.specify/memory/constitution.md`:
   ```markdown
   ## Audit & Anti-Pattern Tooling
   
   | Setting | Value |
   |---------|-------|
   | **Tool Location** | `~/Documents/Sf PS Audit Tool/salesforce-audit-tool-v1.2.17` |
   | **Target Org** | `my-org-alias` |
   ```

### Running an Audit

```bash
# 1. Navigate to audit tool
cd ~/Documents/Sf\ PS\ Audit\ Tool/salesforce-audit-tool-v1.2.17

# 2. Authenticate target org
sf org login web --alias my-org

# 3. Run audit
python3 salesforce_audit.py --sfdx my-org

# 4. Review report
open audit_reports/latest_report.html
```

### Audit Categories

| Category | What It Checks |
|----------|---------------|
| **Governor Limits** | SOQL/DML in loops, query limits |
| **Security** | CRUD/FLS enforcement, SOQL injection, XSS |
| **Performance** | SOQL selectivity, query optimization |
| **Test Coverage** | 75% minimum, meaningful assertions |
| **Apex Patterns** | Trigger handler, bulkification, error handling |
| **LWC Standards** | Component structure, wire adapters, SLDS |

### Integrating with SpecKit

1. **Run audit during `/speckit-analyze`:**
   ```
   /speckit-analyze --with-audit
   ```

2. **Constitution gate enforcement:**
   - CRITICAL/High findings block completion
   - Medium findings flagged for review
   - Low findings tracked for future iterations

### Sample Audit Report

```
╔══════════════════════════════════════════════════════════════╗
║            SALESFORCE AUDIT REPORT - my-org                  ║
╠══════════════════════════════════════════════════════════════╣
║ OVERALL GRADE: B (78/100)                                    ║
╠══════════════════════════════════════════════════════════════╣
║ CRITICAL: 0  │  HIGH: 2  │  MEDIUM: 5  │  LOW: 12           ║
╚══════════════════════════════════════════════════════════════╝

HIGH FINDINGS:
━━━━━━━━━━━━━━
[H-001] AccountTriggerHandler.cls:45
        SOQL inside FOR loop detected
        Fix: Move query outside loop, use Map for lookup

[H-002] ContactService.cls:112
        Missing CRUD check before DML
        Fix: Add Schema.sObjectType.Contact.isCreateable()

MEDIUM FINDINGS:
━━━━━━━━━━━━━━━━
[M-001] OpportunityController.cls:23
        System.debug() in production code
        Fix: Remove debug statements

...
```

---

## Troubleshooting

### Git Clone Blocked in Cursor

**Error:** "The sandbox is blocking git clone" or "Unable to create .git directory"

**Cause:** Cursor's sandbox blocks `git clone` for security (prevents malicious git hooks).

**Solution:** Run `git clone` in **macOS Terminal**, not Cursor:
```bash
# Open Terminal.app (not Cursor)
git clone https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git
```

After cloning, you can open the folder in Cursor:
```bash
cursor /path/to/speckit-salesforce
```

### Installation Problems

**"Permission denied"**
```bash
chmod +x install.sh
bash install.sh .
```

**"Command not found: git"**
```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt install git
```

### Dashboard Issues

**GitHub Pages 404**
1. Check `/docs` folder exists at repo root
2. Verify Pages settings: `main` branch, `/docs` folder
3. Wait 2-3 minutes after enabling

**Empty dashboard**
1. Run `/speckit-dashboard`
2. Check `docs/progress-tracker.json` has data

### Jira Sync Issues

**"Cannot connect to Jira"**
1. Verify Jira URL in `progress-tracker.json`
2. Check Atlassian MCP authentication
3. Ensure project key is correct

### Skill Not Found

**"/speckit-specify not recognized"**
1. Verify `.cursor/skills/` folder exists
2. Restart Cursor IDE
3. Check skill files are present

---

## File Structure

After installation, your project will have:

```
your-project/
├── .cursor/
│   └── skills/                          ← Agent commands
│       ├── speckit-specify/SKILL.md
│       ├── speckit-plan/SKILL.md
│       ├── speckit-tasks/SKILL.md
│       ├── speckit-wireframe/SKILL.md
│       ├── speckit-analyze/SKILL.md
│       ├── speckit-implement/SKILL.md
│       ├── speckit-dashboard/SKILL.md
│       ├── speckit-checklist/SKILL.md
│       ├── speckit-clarify/SKILL.md
│       ├── speckit-constitution/SKILL.md
│       ├── speckit-taskstoissues/SKILL.md
│       └── speckit-agent-context-update/SKILL.md
├── .specify/
│   ├── templates/                       ← Output templates
│   │   ├── spec-template.md
│   │   ├── plan-template.md
│   │   ├── tasks-template.md
│   │   ├── checklist-template.md
│   │   ├── constitution-template.md
│   │   └── progress-tracker-template.json
│   ├── scripts/
│   │   └── bash/
│   │       └── setup-dashboard.sh
│   ├── memory/                          ← Project context (ALWAYS consulted)
│   │   ├── constitution.md              ← Governance principles
│   │   ├── project-details.md           ← Project info, stakeholders
│   │   ├── taxonomy.md                  ← Naming conventions, glossary
│   │   ├── domain.md                    ← Industry knowledge, processes
│   │   └── regulatory.md                ← Compliance requirements
│   └── integrations/
├── docs/
│   ├── progress-dashboard.html
│   ├── progress-tracker.json
│   ├── jira-integration.md
│   └── README.md
├── sample-constitution.md
└── specs/
    └── (your specifications will be here)
```

---

## Memory Files (Project Context)

The `.specify/memory/` folder contains files that are **automatically consulted** by all SpecKit commands. These files provide persistent project context.

### Available Memory Files

| File | Purpose | When to Use |
|------|---------|-------------|
| `constitution.md` | Governance principles, coding standards | Every project (required) |
| `project-details.md` | Project info, stakeholders, timelines | Every project (recommended) |
| `taxonomy.md` | Naming conventions, glossary, acronyms | Multi-team projects |
| `domain.md` | Industry knowledge, business processes | Domain-specific projects |
| `regulatory.md` | Compliance requirements, data classification | Regulated industries |

### constitution.md

**Purpose**: Defines architectural principles and coding standards that MUST be followed.

**Key Sections**:
- Core Principles (Platform-First, Security, Governor Limits)
- Code Quality Standards (Apex, LWC, Testing)
- Permission Set Governance
- Audit Tool Configuration

**Example Usage**:
```markdown
### II. Security & Access Control (NON-NEGOTIABLE)
All database operations MUST run in user mode.
Classes MUST use `with sharing`.
```

### project-details.md

**Purpose**: Central reference for project context.

**Key Sections**:

| Section | What to Include |
|---------|----------------|
| **Project Information** | Name, code, org alias, API version |
| **Stakeholders** | Names, roles, responsibilities |
| **Timeline** | Milestones, target dates |
| **Environments** | Dev, QA, UAT, Prod org details |
| **Scope** | In scope, out of scope, future phases |
| **Success Metrics** | KPIs, targets, measurement methods |

### taxonomy.md

**Purpose**: Ensures consistent naming and terminology.

**Key Sections**:

| Section | Contents |
|---------|----------|
| **Object Naming** | `[Namespace]_[Entity]__c` patterns |
| **Field Naming** | Standard extensions, lookups, formulas |
| **Apex Naming** | Triggers, handlers, services, tests |
| **LWC Naming** | Components, events, methods |
| **Permission Sets** | `[App]_[Feature]_[Level]` format |
| **Business Glossary** | Term → Definition → Salesforce mapping |
| **Acronyms** | KAM, HCP, HCO, RSM, etc. |

**Example**:
```markdown
### Apex Naming
| Type | Pattern | Example |
|------|---------|---------|
| Trigger | `[Object]Trigger` | `AccountTrigger` |
| Handler | `[Object]TriggerHandler` | `AccountTriggerHandler` |
| Service | `[Domain]Service` | `OpportunityService` |
```

### domain.md

**Purpose**: Captures industry-specific knowledge.

**Key Sections**:

| Section | Contents |
|---------|----------|
| **Industry Overview** | Sector, business model |
| **Business Processes** | Step-by-step workflows |
| **Business Rules** | Validation rules, approvals |
| **Domain Entities** | Business → Salesforce mapping |
| **Industry Metrics** | KPIs, calculations, targets |
| **Competitive Landscape** | Competitors, differentiation |
| **Seasonal Factors** | Cyclical impacts on system |

**Example**:
```markdown
## Business Rules
| Rule ID | Description | Enforcement |
|---------|-------------|-------------|
| BR-001 | Orders > $50K need director approval | Approval Process |
| BR-002 | Discounts capped at 20% | Validation Rule |
```

### regulatory.md

**Purpose**: Documents compliance requirements.

**Key Sections**:

| Section | Contents |
|---------|----------|
| **Applicable Regulations** | GDPR, HIPAA, SOX, PCI-DSS |
| **Data Classification** | Public, Internal, Confidential, Highly Confidential |
| **Retention Policies** | How long data must be kept |
| **Consent Management** | Types, collection points, tracking |
| **Audit Requirements** | What must be logged |
| **Security Requirements** | Access control, encryption |
| **Compliance Checklist** | Pre-deployment verification |

**Example**:
```markdown
## Data Classification
| Level | Examples | Handling |
|-------|----------|----------|
| **Confidential** | Customer PII | Role-based access, encryption |
| **Highly Confidential** | SSN, PHI | MFA, audit logging, Shield |
```

### Setting Up Memory Files

1. **Copy templates to memory folder**:
   ```bash
   # Constitution is already there, copy others
   cp sample-project-details.md .specify/memory/project-details.md
   ```

2. **Customize each file** with your project-specific information

3. **Verify with SpecKit**:
   ```
   /speckit-constitution
   ```
   This validates your constitution and shows what memory files are active.

---

## Templates Reference

The `.specify/templates/` folder contains templates that define output formats.

### spec-template.md

**Purpose**: Structure for feature specifications

**Key Sections**:
- User Scenarios & Testing (prioritized user stories)
- Requirements (functional requirements with FR-XXX IDs)
- Key Entities
- Panel/Screen Content (fields visible)
- Navigation & Interactions
- Persona Capabilities (CRUD matrix)
- Success Criteria
- Wireframes (populated by `/speckit-wireframe`)
- Assumptions

**Format Features**:
- User stories with priorities (P1, P2, P3)
- Acceptance scenarios in Given/When/Then format
- Pharma domain field grounding (customizable)

### plan-template.md

**Purpose**: Implementation plan structure

**Key Sections**:
- Summary
- Technical Context (language, dependencies, platform)
- Constitution Check gate
- Project Structure
- Complexity Tracking (for justified violations)

**Format Features**:
- Constitution check must pass before proceeding
- Multiple project structure options
- Clear technical context requirements

### tasks-template.md

**Purpose**: Task breakdown structure

**Key Sections**:
- Phase 1: Setup (project initialization)
- Phase 2: Foundational (blocking prerequisites)
- Phase 3+: User Stories (one phase per story)
- Phase N: Polish (cross-cutting concerns)

**Format Features**:
- `[P]` marker for parallel tasks
- `[US1]`, `[US2]` markers for story mapping
- MVP-first implementation strategy
- Checkpoint validation points

### Customizing Templates

1. **Edit template files** in `.specify/templates/`
2. **Add industry-specific sections** (e.g., pharma fields, compliance checks)
3. **Remove unused sections** for your project type
4. **Templates are automatically used** by SpecKit commands

---

## Getting Help

- **Documentation:** `docs/README.md`
- **Jira Setup:** `docs/jira-integration.md`
- **Skill Details:** `.cursor/skills/speckit-*/SKILL.md`

---

## Updating SpecKit

### Update the SpecKit Source Package

To get the latest version of SpecKit:

```bash
cd /path/to/speckit-salesforce
git pull origin main
```

### Update an Installed Project

Use the `update.sh` script to update a project while preserving your configuration:

```bash
bash /path/to/speckit-salesforce/update.sh /path/to/your-project
```

**Example:**
```bash
bash ~/speckit-salesforce/update.sh ~/my-salesforce-project
```

### What the Update Script Does

1. **Pulls latest** from GitHub (optional)
2. **Creates backup** of your configuration
3. **Lets you choose** what to update:
   - All components (recommended)
   - Agent skills only
   - Templates only
   - Dashboard only
   - Memory templates only
   - Custom selection
4. **Preserves** your `progress-tracker.json` and constitution customizations
5. **Shows backup location** in case you need to restore

### Update Options

| Option | What It Updates |
|--------|----------------|
| **All components** | Skills, templates, dashboard, scripts |
| **Skills only** | `.cursor/skills/` (12 commands) |
| **Templates only** | `.specify/templates/` |
| **Dashboard only** | `docs/progress-dashboard.html` |
| **Memory templates** | `.specify/memory/` (overwrites customizations) |

### Manual Update (Alternative)

If you prefer to update manually:

```bash
# Update skills only
cp -r /path/to/speckit-salesforce/.cursor/skills/* /path/to/your-project/.cursor/skills/

# Update templates only
cp -r /path/to/speckit-salesforce/.specify/templates/* /path/to/your-project/.specify/templates/

# Update dashboard only
cp /path/to/speckit-salesforce/docs/progress-dashboard.html /path/to/your-project/docs/
```

### After Updating

1. **Restart Cursor** to load updated skills
2. **Review changes** if you updated memory files
3. **Check backup** at `.speckit-backup-YYYYMMDD-HHMMSS/` if needed

---

## Version Information

| Component | Version |
|-----------|---------|
| SpecKit Salesforce | 1.0.0 |
| Base SpecKit | 0.10.1 |
| Last Updated | June 2026 |
