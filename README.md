# SpecKit - Salesforce Development Accelerator

A comprehensive specification and progress tracking kit for Salesforce development projects. Built for Cursor IDE with AI-powered workflow automation.

## Features

- **Intent-Driven Specs** - Generate detailed specifications from high-level objectives
- **Automated Planning** - Research, data models, Apex contracts, task breakdown
- **Progress Dashboard** - GitHub Pages dashboard with real-time tracking
- **Jira Integration** - Sync story status automatically
- **Token Tracking** - Monitor AI consumption per contributor
- **Multi-Epic Support** - Manage complex projects with multiple workstreams

## Quick Install

```bash
# Clone the package
git clone https://git.soma.salesforce.com/praveensingh/speckit-generic.git

# Install to your project
bash speckit-generic/install.sh /path/to/your-project
```

## What's Included

### Agent Skills (12 Commands)

| Command | Description |
|---------|-------------|
| `/speckit-specify` | Generate specification from objective |
| `/speckit-plan` | Create implementation plan with research |
| `/speckit-tasks` | Break down into actionable tasks |
| `/speckit-analyze` | Validate spec completeness |
| `/speckit-dashboard` | Manage progress dashboard |
| `/speckit-implement` | Execute task implementation |
| `/speckit-checklist` | Generate requirement checklists |
| `/speckit-wireframe` | Create UI wireframes |
| `/speckit-constitution` | Define project guardrails |
| `/speckit-clarify` | Refine ambiguous requirements |
| `/speckit-taskstoissues` | Export tasks to Jira |
| `/speckit-agent-context-update` | Update agent context |

### Progress Dashboard

- Overview with KPIs and charts
- Built stories tracking
- Multi-contributor token consumption
- Epic & story management
- Jira status sync

### Templates

- Specification template
- Plan template
- Tasks template
- Checklist template
- Progress tracker JSON

## Usage

### 1. Initialize a New Feature

```
/speckit-specify -EPIC "Feature Name" 
Objective: what you want to achieve
Primary users: who will use it
Core objects: Salesforce objects involved
Capabilities: list of requirements
```

### 2. Generate Plan & Tasks

```
/speckit-plan    # Creates research, data model, Apex contracts
/speckit-tasks   # Breaks down into implementable tasks
```

### 3. Validate Before Implementation

```
/speckit-analyze  # Returns PASS/FAIL with recommendations
```

### 4. Track Progress

```
/speckit-dashboard        # Generate/update dashboard
/speckit-dashboard sync   # Sync from Jira
```

## Project Structure

After installation:

```
your-project/
├── .cursor/
│   └── skills/           # Agent skills
├── .specify/
│   ├── templates/        # Document templates
│   ├── scripts/          # Setup scripts
│   ├── memory/           # Constitution & context
│   └── integrations/     # Cursor agent config
├── docs/                  # GitHub Pages
│   ├── progress-dashboard.html
│   └── progress-tracker.json
└── specs/                 # Your specifications
    └── 001-feature-name/
        ├── spec.md
        ├── plan.md
        ├── tasks.md
        └── data-model.md
```

## Configuration

### Project Settings

Edit `docs/progress-tracker.json`:

```json
{
  "project": {
    "name": "Your Project Name",
    "jira_project": "YOUR-KEY",
    "jira_url": "https://your-instance.atlassian.net/...",
    "github_repo": "https://github.com/org/repo",
    "salesforce_org": "Your Org Alias"
  }
}
```

### Adding Team Members

```json
{
  "contributors": [
    {
      "id": "jane",
      "name": "Jane Smith",
      "role": "Developer",
      "total_tokens": 0,
      "sessions_count": 0
    }
  ]
}
```

## Jira Integration

### Manual Sync (No Admin)
Tell the agent: "Sync from Jira"

### Automated Webhook (Requires Admin)
See `docs/jira-integration.md` for setup instructions.

## GitHub Pages

1. Push to GitHub
2. Settings → Pages → Source: `main`, Folder: `/docs`
3. Access dashboard at your Pages URL

## Requirements

- Cursor IDE with agent mode enabled
- Git repository
- Jira project (optional)
- GitHub Pages (optional)

## Customization

### Add Custom Templates

Create templates in `.specify/templates/`:
- Use `{{PLACEHOLDER}}` for variables
- Reference in skills as needed

### Modify Skills

Edit skills in `.cursor/skills/speckit-*/SKILL.md`:
- Customize prompts and workflows
- Add project-specific guidance

## Support

For issues or enhancements, contact your SpecKit administrator.

## Version

- **SpecKit Generic**: 1.0.0
- **Based on**: SpecKit 0.10.1
