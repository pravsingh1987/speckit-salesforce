# SpecKit Salesforce - Development Accelerator

A comprehensive specification and progress tracking kit for Salesforce development projects. Built for Cursor IDE with AI-powered workflow automation.

## Features

- **Intent-Driven Specs** - Generate detailed specifications from high-level objectives
- **Automated Planning** - Research, data models, Apex contracts, task breakdown
- **Progress Dashboard** - GitHub Pages dashboard with real-time tracking
- **Jira Integration** - Sync story status automatically
- **Token Tracking** - Monitor AI consumption per contributor
- **Multi-Epic Support** - Manage complex projects with multiple workstreams
- **Wireframe Generation** - SLDS-aligned UI mockups for customer sign-off
- **Constitution Governance** - Enforce architectural principles and coding standards

## Quick Install

**One command. Works in Cursor's terminal OR macOS Terminal — your choice.**

Salesforce Internal:

```bash
git clone https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git ~/.speckit-salesforce 2>/dev/null; ln -sf ~/.speckit-salesforce/.cursor/skills ~/.cursor/skills && echo "✅ SpecKit installed — run /speckit-init in any project"
```

External / GitHub:

```bash
git clone https://github.com/pravsingh1987/speckit-salesforce.git ~/.speckit-salesforce 2>/dev/null; ln -sf ~/.speckit-salesforce/.cursor/skills ~/.cursor/skills && echo "✅ SpecKit installed — run /speckit-init in any project"
```

Then open **any** Salesforce project in Cursor and run:

```
/speckit-init
```

That's it. All `/speckit-*` commands now work in every project.

> **Why this works everywhere:** The command clones to `~/.speckit-salesforce` (outside any project) and symlinks the skills into Cursor. Because *you* run it interactively, there's no sandbox — it works identically in Cursor's integrated terminal and macOS Terminal.

### To Update Later

```bash
cd ~/.speckit-salesforce && git pull
```

Skills update instantly — no reinstall needed.

### Alternative: pip Install

```bash
pip install git+https://git.soma.salesforce.com/praveensingh/speckit-salesforce.git
speckit init ./my-project
```

See `INSTALLATION_GUIDE.md` for complete setup instructions.

## What's Included

### Agent Skills (12 Commands)

| Command | Description |
|---------|-------------|
| `/speckit-specify` | Generate specification from objective |
| `/speckit-plan` | Create implementation plan with research |
| `/speckit-tasks` | Break down into actionable tasks |
| `/speckit-analyze` | Validate spec completeness |
| `/speckit-wireframe` | Create SLDS-aligned UI wireframes |
| `/speckit-implement` | Execute task implementation |
| `/speckit-dashboard` | Manage progress dashboard |
| `/speckit-constitution` | Validate against governance principles |
| `/speckit-checklist` | Generate requirement checklists |
| `/speckit-clarify` | Refine ambiguous requirements |
| `/speckit-taskstoissues` | Export tasks to Jira |
| `/speckit-agent-context-update` | Update agent context |

### Memory Files (Project Context)

Files in `.specify/memory/` are **automatically consulted** by all commands:

| File | Purpose |
|------|---------|
| `constitution.md` | Governance principles, coding standards |
| `project-details.md` | Project info, stakeholders, timelines |
| `taxonomy.md` | Naming conventions, glossary, acronyms |
| `domain.md` | Industry knowledge, business processes |
| `regulatory.md` | Compliance requirements, data classification |

### Templates

| Template | Output |
|----------|--------|
| `spec-template.md` | Feature specifications with user stories |
| `plan-template.md` | Implementation plans with constitution check |
| `tasks-template.md` | Task breakdown organized by user story |
| `checklist-template.md` | Requirement checklists |
| `progress-tracker-template.json` | Dashboard data structure |

### Progress Dashboard

- Overview with KPIs and charts
- Built stories tracking
- Multi-contributor token consumption
- Epic & story management
- Jira status sync
- GitHub Pages ready

## Usage Workflow

### Recommended Order

```
1. /speckit-specify     → Create spec from requirements
2. /speckit-wireframe   → Generate wireframes (get sign-off!)
3. /speckit-analyze     → Validate spec completeness  
4. /speckit-plan        → Generate technical plan
5. /speckit-tasks       → Break into tasks
6. /speckit-implement   → Build the solution
7. /speckit-dashboard   → Track progress
```

### 1. Initialize a New Feature

```
/speckit-specify -EPIC "Feature Name" 
Objective: what you want to achieve
Primary users: who will use it
Core objects: Salesforce objects involved

[Optionally include:]
- Meeting transcripts
- Recording summaries
- Wireframe descriptions
- Requirements documents
- Discussion notes
```

### 2. Generate Wireframes (Recommended)

```
/speckit-wireframe  # Generates SLDS-aligned visual mockups
```

Creates `wireframes.md` with screen inventory, Figma links, and sign-off checklist.

> ⚠️ **Best Practice**: Get stakeholder sign-off on wireframes before proceeding to plan.

### 3. Validate Specification

```
/speckit-analyze  # Returns PASS/FAIL with recommendations
```

### 4. Generate Plan & Tasks

```
/speckit-plan    # Creates research, data model, Apex contracts
/speckit-tasks   # Breaks down into implementable tasks
```

### 5. Implement

```
/speckit-implement  # Execute tasks with guidance
```

### 6. Track Progress

```
/speckit-dashboard        # Generate/update dashboard
/speckit-dashboard sync   # Sync from Jira
```

## Project Structure

After installation:

```
your-project/
├── .cursor/
│   └── skills/                    # Agent skills (12 commands)
├── .specify/
│   ├── templates/                 # Document templates
│   ├── scripts/                   # Setup scripts
│   ├── memory/                    # Project context
│   │   ├── constitution.md        ← Governance principles
│   │   ├── project-details.md     ← Project info
│   │   ├── taxonomy.md            ← Naming conventions
│   │   ├── domain.md              ← Industry knowledge
│   │   └── regulatory.md          ← Compliance rules
│   └── integrations/
├── docs/                          # GitHub Pages
│   ├── progress-dashboard.html
│   └── progress-tracker.json
├── sample-constitution.md         # Customizable template
└── specs/                         # Your specifications
    └── 001-feature-name/
        ├── spec.md
        ├── plan.md
        ├── tasks.md
        ├── wireframes.md
        └── data-model.md
```

## Configuration

### Required Settings

| Setting | Description | Example |
|---------|-------------|---------|
| `name` | Your project name | "Customer Portal" |
| `salesforce_org` | SF org alias | "devhub" |

### Optional Settings (Recommended)

| Setting | Description | Example |
|---------|-------------|---------|
| `github_repo` | Full GitHub URL | `https://github.com/myorg/myrepo` |
| `jira_project` | Jira project key | `PORTAL-123` |
| `jira_url` | Jira board URL | `https://mycompany.atlassian.net/...` |

### GitHub Pages Setup

1. Push your code to GitHub
2. Go to: `Settings → Pages`
3. Source: `main` branch, `/docs` folder
4. Your dashboard URL: `https://<org>.github.io/<repo>/progress-dashboard.html`

### Jira Integration

For automatic story sync, see `docs/jira-integration.md`:
- **Manual sync**: Tell agent "Sync from Jira"
- **Automated**: Set up Jira webhook (requires admin)

## Salesforce PS Audit Tool Integration

The constitution references the Salesforce PS Audit Tool for code validation:

```bash
# Run audit
cd ~/Documents/Sf\ PS\ Audit\ Tool/salesforce-audit-tool-v1.2.17
python3 salesforce_audit.py --sfdx my-org
```

See `INSTALLATION_GUIDE.md` for complete audit tool setup.

## Requirements

- Cursor IDE with agent mode enabled
- Git repository
- Jira project (optional)
- GitHub Pages (optional)
- Salesforce CLI (for deployment)

## Documentation

- **Installation Guide**: `INSTALLATION_GUIDE.md`
- **Jira Integration**: `docs/jira-integration.md`
- **Dashboard Guide**: `docs/README.md`
- **Skill Details**: `.cursor/skills/speckit-*/SKILL.md`

## Support

For issues or enhancements, contact your SpecKit administrator.

## Version

- **SpecKit Salesforce**: 1.0.0
- **Based on**: SpecKit 0.10.1
