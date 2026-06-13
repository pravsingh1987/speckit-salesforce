# Dashboard Update Reminder

You just completed a git commit. Check if the dashboard needs updating.

## Instructions

1. **Check what was committed** - Review the commit message and files
2. **Determine if stories were completed** - Look for:
   - LWC components completed
   - Apex classes finished
   - User story implementations
   - Feature completions

3. **If work was completed**, ask the user:
   > "I noticed you committed [description]. Would you like me to update the progress dashboard?"
   > - Mark story as built
   > - Add token consumption for this session
   > - Sync with Jira

4. **If user agrees**, run:
   - Update `docs/progress-tracker.json` with:
     - Story status → `built: true`
     - `built_by` → contributor ID
     - `built_date` → today's date
     - Token session entry

5. **Commit the tracker update**:
   ```
   git add docs/progress-tracker.json
   git commit -m "Update dashboard: [story key] marked as built"
   ```

## Story Key Detection

Look for patterns in commit messages:
- `PROJ-XXX` (Jira key pattern)
- `US1:`, `US2:` (User story references)
- `EPIC-00X` (Epic references)

## Token Estimation

Estimate tokens based on session activity:
- Simple component: ~15,000 tokens
- Complex feature: ~45,000 tokens
- Full epic work: ~85,000 tokens
