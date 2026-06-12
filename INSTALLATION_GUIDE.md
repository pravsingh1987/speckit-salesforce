# SpecKit Generic Edition - Installation & User Guide

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

SpecKit Generic Edition is a universal development accelerator for any Salesforce project. It provides:

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

```bash
git clone https://github.com/pravsingh1987/speckit-generic.git
```

### Step 2: Create Your Project Directory

```bash
mkdir my-salesforce-project
cd my-salesforce-project
```

### Step 3: Run the Installer

```bash
bash /path/to/speckit-generic/install.sh .
```

**Example:**
```bash
bash ~/Downloads/speckit-generic/install.sh .
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

```
/speckit-specify -EPIC "Customer Self-Service Portal"
Objective: Allow customers to view and manage their accounts online
Primary users: Customers, Support Agents
Core objects: Account, Contact, Case, Portal_Session__c
Capabilities:
* Customer login and authentication
* View account details and history
* Submit and track support cases
* Update contact information
* View invoices and payments
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

## Troubleshooting

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
│   └── skills/
│       ├── speckit-specify/SKILL.md
│       ├── speckit-plan/SKILL.md
│       ├── speckit-tasks/SKILL.md
│       ├── speckit-wireframe/SKILL.md    ← Wireframe skill
│       ├── speckit-analyze/SKILL.md
│       ├── speckit-implement/SKILL.md
│       ├── speckit-dashboard/SKILL.md
│       ├── speckit-checklist/SKILL.md
│       ├── speckit-clarify/SKILL.md
│       ├── speckit-constitution/SKILL.md
│       ├── speckit-taskstoissues/SKILL.md
│       └── speckit-agent-context-update/SKILL.md
├── .specify/
│   ├── templates/
│   ├── scripts/
│   ├── memory/
│   └── integrations/
├── docs/
│   ├── progress-dashboard.html
│   ├── progress-tracker.json
│   ├── jira-integration.md
│   └── README.md
└── specs/
    └── (your specifications will be here)
```

---

## Getting Help

- **Documentation:** `docs/README.md`
- **Jira Setup:** `docs/jira-integration.md`
- **Skill Details:** `.cursor/skills/speckit-*/SKILL.md`

---

## Version Information

| Component | Version |
|-----------|---------|
| SpecKit Generic | 1.0.0 |
| Base SpecKit | 0.10.1 |
| Last Updated | June 2026 |
