# Lupin Project Shikhar - Progress Dashboard

This directory contains the progress tracking dashboard for the Lupin KAM Salesforce implementation project.

## Files

| File | Purpose |
|------|---------|
| `progress-dashboard.html` | Static HTML dashboard for GitHub Pages |
| `progress-tracker.json` | Single source of truth for all metrics |

## Viewing the Dashboard

### Option 1: GitHub Pages (Recommended)

1. Enable GitHub Pages in repository settings
2. Set source to `main` branch, `/docs` folder
3. Access at: `https://git.soma.salesforce.com/pages/praveensingh/Lupin-Pharma/progress-dashboard.html`

### Option 2: Local Viewing

Open `progress-dashboard.html` directly in a browser. The dashboard works offline with embedded data.

### Option 3: Cursor Canvas

An interactive canvas is available at:
`~/.cursor/projects/Users-praveensingh-Documents-LUPIN/canvases/lupin-progress-dashboard.canvas.tsx`

## Tracked Metrics

### 1. Token Consumption (per Epic)

Token estimates based on conversation session length and complexity:

| Epic | Estimated Tokens |
|------|------------------|
| Hospital 360 View | 130K |
| Contact 360 (HCP) | 175K |
| Opportunity Journey | 180K |
| **Total** | **485K** |

### 2. Epics & Stories Created

| Metric | Count |
|--------|-------|
| Total Epics | 3 |
| Total User Stories | 33 |
| - Hospital 360 | 13 stories |
| - Contact 360 | 10 stories |
| - Opportunity Journey | 10 stories |

### 3. Build Progress

Track story implementation status:
- **Pending**: Not started
- **In Progress**: Currently being built
- **Built**: Deployed to Salesforce org

## Updating the Dashboard

### Manual Update

Edit `progress-tracker.json` to update:
- Story status (`built: true/false`)
- Token consumption (add new sessions)
- Build counts

### Automated Sync (Future)

Consider adding a script to sync with Jira status automatically.

## Data Structure

```json
{
  "summary": {
    "total_epics": 3,
    "total_stories": 33,
    "stories_built": 0,
    "completion_percentage": 0
  },
  "token_consumption": {
    "by_epic": [
      {
        "epic_name": "Hospital 360 View",
        "total_tokens": 130000,
        "sessions": [...]
      }
    ]
  },
  "epics": [
    {
      "jira_key": "PR1070767-1",
      "stories": [
        { "key": "PR1070767-24", "built": false }
      ]
    }
  ]
}
```

## Links

- **Jira Board**: https://salesforce.atlassian.net/jira/software/c/projects/PR1070767/boards/15888
- **GitHub Repo**: https://git.soma.salesforce.com/praveensingh/Lupin-Pharma
