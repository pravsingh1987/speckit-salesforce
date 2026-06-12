#!/bin/bash
# SpecKit Generic Installer
# Installs SpecKit for any Salesforce development project

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Banner
echo ""
echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║       SpecKit - Salesforce Development Accelerator        ║${NC}"
echo -e "${CYAN}║                    Generic Edition v1.0                    ║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Target directory
if [ -z "$1" ]; then
    read -p "Enter target project directory (or . for current): " TARGET_DIR
    TARGET_DIR="${TARGET_DIR:-.}"
else
    TARGET_DIR="$1"
fi

TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd || mkdir -p "$TARGET_DIR" && cd "$TARGET_DIR" && pwd)"

echo -e "${BLUE}📁 Installing to: $TARGET_DIR${NC}"
echo ""

read -p "Proceed with installation? (y/N): " CONFIRM
[[ ! "$CONFIRM" =~ ^[Yy]$ ]] && echo "Cancelled." && exit 0

echo ""
echo -e "${BLUE}📦 Installing SpecKit components...${NC}"

# Copy core files
cp -r "$SCRIPT_DIR/.specify" "$TARGET_DIR/"
echo -e "  ${GREEN}✓${NC} Core SpecKit (.specify/)"

mkdir -p "$TARGET_DIR/.cursor"
cp -r "$SCRIPT_DIR/.cursor/skills" "$TARGET_DIR/.cursor/"
echo -e "  ${GREEN}✓${NC} Agent skills (.cursor/skills/)"

cp -r "$SCRIPT_DIR/docs" "$TARGET_DIR/"
echo -e "  ${GREEN}✓${NC} Dashboard templates (docs/)"

# Create specs directory
mkdir -p "$TARGET_DIR/specs"
echo -e "  ${GREEN}✓${NC} Specs directory (specs/)"

# Make scripts executable
find "$TARGET_DIR/.specify/scripts" -name "*.sh" -exec chmod +x {} \;

# Project configuration
echo ""
echo -e "${BLUE}📝 Project Configuration${NC}"
echo ""

read -p "Project Name: " PROJECT_NAME
PROJECT_NAME="${PROJECT_NAME:-My Salesforce Project}"

read -p "Jira Project Key (or press Enter to skip): " JIRA_KEY
read -p "Jira URL (or press Enter to skip): " JIRA_URL
read -p "GitHub Repo URL (or press Enter to skip): " GITHUB_REPO
read -p "Salesforce Org Alias: " SF_ORG
SF_ORG="${SF_ORG:-default}"

read -p "Your Name: " CONTRIBUTOR_NAME
CONTRIBUTOR_NAME="${CONTRIBUTOR_NAME:-Developer}"

read -p "Your Role: " CONTRIBUTOR_ROLE
CONTRIBUTOR_ROLE="${CONTRIBUTOR_ROLE:-Developer}"

CONTRIBUTOR_ID=$(echo "$CONTRIBUTOR_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | cut -c1-20)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Generate progress tracker
cat > "$TARGET_DIR/docs/progress-tracker.json" << EOF
{
  "project": {
    "name": "$PROJECT_NAME",
    "jira_project": "${JIRA_KEY:-}",
    "jira_url": "${JIRA_URL:-}",
    "github_repo": "${GITHUB_REPO:-}",
    "salesforce_org": "$SF_ORG",
    "last_updated": "$TIMESTAMP"
  },
  "summary": {
    "total_epics": 0,
    "total_stories": 0,
    "stories_built": 0,
    "stories_in_progress": 0,
    "stories_in_review": 0,
    "stories_pending": 0,
    "completion_percentage": 0,
    "total_tokens": 0
  },
  "contributors": [
    {
      "id": "$CONTRIBUTOR_ID",
      "name": "$CONTRIBUTOR_NAME",
      "role": "$CONTRIBUTOR_ROLE",
      "total_tokens": 0,
      "sessions_count": 0
    }
  ],
  "token_consumption": {
    "note": "Token estimates based on conversation session length and complexity.",
    "total_estimated_tokens": 0,
    "by_contributor": [],
    "by_epic": []
  },
  "deployment_status": {
    "note": "Track what's deployed to the Salesforce org.",
    "last_deployment": null,
    "deployed_components": {
      "custom_objects": [],
      "custom_fields": [],
      "apex_classes": [],
      "lwc_components": [],
      "permission_sets": [],
      "flexipages": []
    }
  },
  "epics": []
}
EOF

# Initialize git if needed
if [ ! -d "$TARGET_DIR/.git" ]; then
    read -p "Initialize git repository? (y/N): " INIT_GIT
    if [[ "$INIT_GIT" =~ ^[Yy]$ ]]; then
        cd "$TARGET_DIR" && git init
        echo -e "  ${GREEN}✓${NC} Git initialized"
    fi
fi

# Summary
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║              Installation Complete! 🎉                     ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Project: $PROJECT_NAME${NC}"
echo -e "${CYAN}Location: $TARGET_DIR${NC}"
echo ""
echo -e "${CYAN}Next Steps:${NC}"
echo "  1. Open in Cursor IDE"
echo "  2. Create first spec: ${YELLOW}/speckit-specify -EPIC \"Feature\" Objective: ...${NC}"
echo "  3. Generate plan: ${YELLOW}/speckit-plan${NC}"
echo "  4. Break into tasks: ${YELLOW}/speckit-tasks${NC}"
echo "  5. Setup dashboard: ${YELLOW}/speckit-dashboard${NC}"
echo ""
