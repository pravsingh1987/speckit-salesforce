---
name: speckit-dashboard
description: Generate and manage the project progress dashboard with Jira sync, token tracking, and GitHub Pages publishing.
version: 1.0.0
---

# SpecKit Dashboard

Generate and manage the project progress tracking dashboard.

## Commands

### `/speckit-dashboard`

Generate or update the progress dashboard.

**Usage:**
```
/speckit-dashboard              # Generate full dashboard
/speckit-dashboard sync         # Sync from Jira
/speckit-dashboard add-epic     # Add new epic to tracker
/speckit-dashboard add-contrib  # Add contributor
```

## Dashboard Features

1. **Overview Tab** - Summary stats, progress bars, charts
2. **Built Stories Tab** - What's deployed to Salesforce org
3. **Contributors Tab** - Multi-person token tracking
4. **Epics & Stories Tab** - Full story list by epic
5. **Token Details Tab** - Session-level breakdown

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Dashboard HTML | `docs/progress-dashboard.html` | GitHub Pages UI |
| Tracker JSON | `docs/progress-tracker.json` | Data source |
| Template | `.specify/templates/progress-tracker-template.json` | Initial setup |

## Workflow

### Initial Setup

1. Run setup script:
   ```bash
   bash .specify/scripts/bash/setup-dashboard.sh
   ```

2. Generate dashboard:
   ```
   /speckit-dashboard
   ```

3. Configure GitHub Pages:
   - Repository Settings → Pages
   - Source: `main` branch, `/docs` folder

### Syncing from Jira

When stories change status in Jira:

```
/speckit-dashboard sync
```

Or tell the agent:
- "Sync dashboard from Jira"
- "Mark PR1070767-24 as built"
- "Update progress tracker"

### Adding Contributors

When a new team member starts working:

```json
{
  "id": "john",
  "name": "John Doe",
  "role": "Developer",
  "total_tokens": 0,
  "sessions_count": 0
}
```

### Adding Token Sessions

After each working session, add to `token_consumption.by_epic[].sessions`:

```json
{
  "date": "2026-06-12",
  "contributor": "john",
  "activity": "Implemented US1: KPI Header Bar",
  "tokens": 45000
}
```

## Jira Integration

### Option 1: Manual Sync (No Admin Required)

Tell the agent: "Sync from Jira"

### Option 2: Automated Webhook (Requires Jira Admin)

See `docs/jira-integration.md` for setup instructions.

**Jira Automation Rule:**
- Trigger: Issue transitioned
- Action: Send webhook to GitHub
- Updates dashboard automatically

### Status Mapping

| Jira Status | Dashboard Status |
|-------------|------------------|
| Open / To Do | `pending` |
| In Progress | `in-progress` |
| In Review / QA | `in-review` |
| Done / Closed | `built` |

## Dashboard Generation

The agent will:

1. Query Jira for all epics and stories
2. Extract status, priority, and metadata
3. Calculate token consumption totals
4. Generate/update `progress-dashboard.html`
5. Update `progress-tracker.json`
6. Commit and push to GitHub

## Customization

### Adding Custom Metrics

Edit `progress-tracker.json` to add project-specific tracking:

```json
{
  "custom_metrics": {
    "code_coverage": 0,
    "test_cases_passed": 0,
    "deployment_count": 0
  }
}
```

### Styling

The dashboard uses CSS variables. Override in the HTML:

```css
:root {
  --accent-blue: #58a6ff;
  --accent-green: #3fb950;
}
```

## Troubleshooting

### GitHub Pages 404
- Ensure `docs/` folder exists at repo root (not inside subdirectory)
- Check Pages settings: source = `main`, folder = `/docs`

### Jira Sync Fails
- Verify Jira project key is correct
- Check MCP authentication status

### Dashboard Not Updating
- Run `/speckit-dashboard sync` to force refresh
- Check `progress-tracker.json` for data integrity
